---
exam_code: MS-700
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-700
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: review-required
last_verified: 2026-09-28
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-28
---

# MS-700 Managing Microsoft Teams Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The September 28, 2026 deep review read the whole guide and mapped all 97 published October objectives while preserving the July 29 accepted baseline. A private-channel Workflows documentation conflict remains open; human review and tenant execution are pending. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ms-700-coverage-record). The [official MS-700 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-700) is authoritative.

**Current baseline:** Skills measured as of July 29, 2026<br>
**Upcoming blueprint change (checked September 28, 2026):** The English blueprint changes October 27, 2026. The revision uses Teams Network planner, Teams Advisor, and Teams admin center terminology. Domain weights are unchanged; these naming changes do not establish a new exam domain. The current baseline below remains dated separately. See the [official revision](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-700).<br>
The [deep-review report](../docs/research/2026-09-28-ms-700-deep-review.md) records the evidence and limitations. The credential page lists **100 minutes** and seven exam languages; do not use a practice vendor’s question count as a promise about the exam.

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

Calculate capacity by modality, expected concurrent sessions, direction and site population, then reserve headroom. Network planner models personas, sites and usage assumptions; validate assumptions with actual telemetry. Use the [Microsoft 365 network connectivity test](https://connectivity.office.com/) for path/egress/DNS insight and current Teams network assessment tooling for media readiness. The [Teams Network Assessment Tool](https://www.microsoft.com/en-us/download/details.aspx?id=103017) listing shows version 1.9.0.0, March 5, 2026. It measures relay connectivity, loss, jitter and RTT; it is a single-instance diagnostic, not a load generator. The installer was not downloaded or executed in this review. [Network planner](https://learn.microsoft.com/en-us/microsoftteams/network-planner) models site capacity and personas; neither a model nor a successful connectivity test proves peak-hour media quality.

**Worked example 1 — Capacity belongs to endpoints and directions.** Assume 24 concurrent meeting-video endpoints at the documented recommended 2.5 Mbps upstream/4 Mbps downstream, plus 40 audio-only endpoints at 58 Kbps each way. Demand is **62.32 Mbps up / 98.32 Mbps down**. A chosen 25% planning allowance produces **77.90 / 122.90 Mbps**. A 100/100 link fails the downstream budget by 22.90 Mbps before other traffic. These are planning assumptions, not a codec guarantee; add screen sharing separately and count a person’s second device as another endpoint. For a broadcast, 200 local viewers at a chosen 3 Mbps each need 600 Mbps without eCDN; test actual eCDN offload rather than assuming a savings percentage.

[QoS guidance](https://learn.microsoft.com/en-us/microsoftteams/qos-in-teams) distinguishes **client source ports** from service destination ports: audio 50000–50019/DSCP 46, video 50020–50039/34, screen sharing 50040–50059/18. Browser clients use dynamic ports; Mac/mobile hard-code AF41 for video **and sharing**. Enable the supported client settings, configure network queues, and capture at both ends to check marks survive. QoS on your managed LAN does not reserve Internet bandwidth.

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

Choose the least-privileged Teams role: Teams Administrator for broad service management, Teams Communications Administrator/Support Engineer/Specialist for communications/support scopes, Teams Devices Administrator for devices, and other workload roles for Purview, Defender, Entra, SharePoint and telephony responsibilities. The [role matrix](https://learn.microsoft.com/en-us/microsoftteams/using-admin-roles) also includes Teams Telephony Administrator. Creating voice resource accounts needs the applicable Teams role plus User Administrator. Teams Device Administrator does not grant call analytics; Teams Reader has exceptions, including user meeting/call details. Assign the role for the evidence needed, not just the word “reader.”

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

Start policies in simulation/audit where supported, test representative internal/guest/shared-channel/meeting cases, define alerts and reviewer roles, then enforce. Licensing, workload locations and policy precedence matter. Use the [security and compliance map](https://learn.microsoft.com/en-us/microsoftteams/security-compliance-overview) to identify each workload. A Teams-only Conditional Access policy does not secure direct access to the same files through SharePoint; test both entry points. Treat Teams chat/message policy and file policy as separate enforcement paths.

### Governance and policy assignment

A team normally uses a Microsoft 365 group for membership and lifecycle. Configure who may create groups, group naming prefix/suffix and blocked words, expiration/renewal, ownership and access reviews. Creation restrictions require correct Entra configuration/licensing and should include a supported request path.

Archive makes a team read-only for most activity while preserving it; unarchive restores activity. Delete starts a recoverable period under current Microsoft 365 group behavior; restoration requires the group and dependent resources to remain recoverable. Retention/hold can preserve compliance copies without making the user-facing team active. Test delete/restore and document ownership transfer.

Teams policies have global defaults, direct assignments, group assignment, batch operations and policy packages. A policy package is a collection of policies for a persona; changing package assignments/effective policy must be verified at the user. For supported policy types, [assignment precedence](https://learn.microsoft.com/en-us/microsoftteams/assign-policies-users-and-groups) is direct user policy, then the highest-ranked group assignment (lowest rank number), then global. Only direct group members inherit these assignments; nested members do not. Propagation is asynchronous and hidden-membership groups are unsupported. Record effective policy after processing.

**Worked example 2 — A package is not the final policy.** Alice has a direct meeting policy A and belongs directly to groups assigned B/rank 1 and C/rank 2. She receives A; removing A lets B win after propagation. Bob belongs only to a nested child group and has no other assignment: he receives global. Compare the effective meeting policy separately from calling policy; removing A does not delete the underlying policy or change unrelated types.

[Client updates](https://learn.microsoft.com/en-us/microsoftteams/teams-client-update) roll out gradually; a published build is not proof every device already runs it. Update policies control which supported client features/users receive under the current release model. Pair with targeted validation and communication. Use Teams PowerShell and Microsoft Graph for repeatable operations with least privilege, object-ID safety, pagination/throttling, logs and rollback.

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

Shared channels use B2B direct connect cross-tenant access settings and their own membership/site. Both organizations' policy can affect access. [Granular federation policies](https://learn.microsoft.com/en-us/microsoftteams/manage-external-access) can replace the organization domain list for selected users/groups, provided tenant federation remains enabled and the partner permits communication. A custom allowlist is not necessarily intersected with the tenant list. Global inherits organization settings; custom lists support up to 100 domains. Blocking a parent domain does not automatically block its subdomains, and federation blocking does not prevent anonymous meeting entry when that is allowed. For MTO, understand member tenant, synchronization/collaboration settings, identity lifecycle and user experience. **VERIFY CURRENT:** MTO capabilities, cross-tenant sync, shared-channel limitations and licensing.

[Shared channels](https://learn.microsoft.com/en-us/microsoftteams/shared-channels) exclude conventional guest accounts, yet Teams guest access must still be enabled for external invitations. Their site membership follows the channel. A SharePoint location-based access policy can allow channel conversation while denying its files. Removing channel membership does not revoke an independently granted internal-user file share; test that residual route separately.

Remove external access at every applicable layer: team/channel membership, guest object or cross-tenant access, sharing links/groups, app grants and sessions. Preserve required content/audit/retention evidence.

### Teams clients and devices

Teams Phone and resource accounts, Teams Rooms and device features have distinct license requirements. A resource account represents an auto attendant/call queue and typically needs the applicable resource-account license; users need Teams Phone and PSTN connectivity entitlements appropriate to the chosen model. [Voice licensing](https://learn.microsoft.com/en-us/microsoftteams/aa-cq-reference-prerequisites-licensing) keeps auto-attendant/queue accounts disabled for sign-in. A Rooms account instead signs a device into services and has an Exchange resource mailbox; the shared word “resource” does not make these accounts interchangeable.

In Teams admin center, use configuration profiles, device tags, accounts, health, firmware/software updates, restart and diagnostic actions. Tags organize devices for operations/policy targeting under supported features; they are not Entra security boundaries. Remote sign-in/provisioning should protect codes, verify physical custody and remove stale credentials.

Teams Rooms design includes certified hardware, room/resource account, mailbox/calendar processing, licensing, network/media readiness, Conditional Access compatible with resource accounts, update rings, peripherals and support ownership. The [Rooms authentication article](https://learn.microsoft.com/en-us/microsoftteams/rooms/rooms-authentication) describes the legacy Windows/ROPC design and its interactive-MFA limits. The July blog below announces newer Windows passwordless support; do not apply a legacy authentication recipe to every deployment. [Device-code guidance](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-teams-devices-device-code-flow) calls for a monitored, persistent exception for genuine device accounts and a Device Registration Service resource exclusion. Passwordless devices still need recovery/reprovisioning. An account exception permits device code flow for other resources in policy scope; it is not restricted to the room scenario or the technician who provisions it. Pilot in report-only and inspect sign-ins.

For VDI, plan supported platform/provider, client and optimization component, media offload, versions, peripherals, network, roaming profile/cache and feature limitations. The [VDI deployment guidance](https://learn.microsoft.com/en-us/microsoftteams/new-teams-vdi-requirements-deploy) ends support for WebRTC optimization on **Windows endpoints connecting to Citrix/AVD/Windows 365 on October 1, 2026**; it ends availability April 1, 2027. These dates do not describe every Linux/mobile endpoint. Inventory the endpoint plugin and virtual-desktop stack; verify the new optimization is active. An unoptimized fallback renders media on the VM and can degrade quality even though sign-in works.

---

## 2. Manage teams, channels, chats, and apps

### Team rollout and creation

[Teams Advisor](https://learn.microsoft.com/en-us/microsoftteams/use-advisor-teams-roll-out) creates a deployment team and workload plans/surveys (with required licensing); it is unavailable in GCC High/DoD. Its assessment can flag configuration gaps, but adoption needs stakeholders, use cases, champions, training, governance, support and measures. Start with representative pilots and explicit success/stop criteria.

Create teams through client, admin center, PowerShell or Graph; automation needs owners, privacy, membership, classification, naming, lifecycle and idempotency. A team can be created from an existing Microsoft 365 group, SharePoint site or another team/template, but source artifacts and permissions do not always copy identically. Verify membership, settings, apps/tabs and files.

Templates standardize channels, tabs/apps and settings for repeatable scenarios; template policies control user visibility. They are starting configurations, not continuous enforcement. Team owners manage membership/settings within tenant constraints; admins manage service/policy and can remediate ownerless teams.

Frontline experiences can use dynamic team deployment and standardized configurations under supported licensing. Validate workforce source attributes, location boundaries, owners and offboarding before scaling.

### Channel and messaging decisions

Standard channels share team membership and the parent site. Private channels have restricted membership and a separate SharePoint site. Shared channels can include people outside the parent team and support cross-tenant collaboration with a separate site. Choose by the required membership boundary, not just convenience.

Deleting a channel affects conversations and related content under current lifecycle behavior; the separate SharePoint site for private/shared channels has its own lifecycle considerations. Manage membership and ownership at the channel where applicable. A user can be a shared-channel member without being a member of the host team.

Teams/channel policies govern who can create private/shared channels and share externally. Messaging policies control supported chat capabilities such as editing/deleting, read receipts, URL previews, translation and user experiences. Meeting chat behavior can also depend on meeting policy/options. Resolve effective user policy and scope before blaming client cache.

### Teams apps and extensibility

The app lifecycle is **discover/purchase → allow/block and permission/consent review → assignment/availability → setup/pin → use/monitor → update/respond/retire**. Org-wide app settings establish broad behavior; [app-centric management](https://learn.microsoft.com/en-us/microsoftteams/app-centric-management) replaces deprecated app permission policies as tenants migrate and determines who can use an app; setup policies install/pin supported apps. Blocking an app and removing OAuth consent are separate actions. [Migration checks](https://learn.microsoft.com/en-us/microsoftteams/pre-and-post-migration) should compare exported before/after user availability; migration does not change existing Graph consent. [App administration](https://learn.microsoft.com/en-us/microsoftteams/manage-apps) requires settings in both Teams and Microsoft 365 admin centers to agree until unified management is enabled.

**Worked example 3 — Check the audience, not the icon.** After migration, app X displays Unblocked but Available to **No one**. An installed/pinned X remains unavailable. App Y is assigned to 12 named employees and a group of 8, with 3 overlapping employees: the intended distinct audience is **17**. Reconcile actual availability against those 17; do not count assignment rows as users. Selected-user/group availability excludes guests even if assigned. Nested groups supported for app availability must not be confused with ordinary Teams group-policy inheritance.

Assess publisher, certification, permissions, delegated/application access, data destination, owners, audience, licensing/purchase, support, telemetry and revocation. Upload custom apps only through controlled review; verify manifest, domains, identity, permissions and versioning. Store customization affects discovery/branding, not security approval.

Choose extension point from interaction:

- tabs embed a web experience in team/chat/meeting context;
- bots/agents converse and act within their permissions;
- message extensions add search/action behavior in compose/message context;
- meeting apps integrate before/during/after meetings;
- workflows automate events/actions through Power Automate or supported app capabilities.

Legacy Office 365 connector webhooks reached their final disablement rollout May 18–22, 2026, according to the updated developer blog below. Use supported Workflows or app notification patterns. [Workflow ownership guidance](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/what-are-webhooks-and-connectors) ties flows to users, not channels: provide co-owners, maintain connection authentication, and test owner departure.

**Open source conflict:** The April 14 blog update says private-channel Workflows webhook support is available, while the platform overview still describes private-channel Flow bot support as under development. Record the cloud, posting identity, entry point and actual result before promising private-channel delivery. Shared-channel support does not resolve this conflict.

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

Keep the exam’s webinar/town-hall distinctions, but recognize the current [unified Events experience](https://learn.microsoft.com/en-us/microsoftteams/plan-town-halls). The **Optimize for large audience** setting selects town-hall policy behavior; when off, webinar settings apply. It is mandatory above 1,000 attendees. A 1,500-person event requiring everybody’s microphone/camera therefore needs a revised design, not simply a higher capacity license. Teams Enterprise supports different interaction levels at 1,000, 3,000 and 10,000 attendees; larger capacity requires an add-on. Recheck the current feature/license matrix rather than assuming every former Premium feature still requires Premium.

[Legacy live events](https://learn.microsoft.com/en-us/microsoftteams/teams-live-events/plan-for-teams-live-events) retired June 30, 2026. Events scheduled before that date remain supported through February 28, 2027. Do not build new rollout labs around legacy live-event creation.

Meeting settings establish tenant-wide defaults/capabilities; meeting policies govern users who organize/participate; templates package supported options for scenarios; template policies control availability; customization policies apply branding; per-meeting options refine an instance. Event policies/settings govern webinar/town-hall capabilities. Test organizer, presenter, attendee, guest/external and anonymous experiences.

Policies can control scheduling, recording, transcription, lobby, content sharing, chat, reactions, attendance, watermarking, end-to-end encryption and Copilot relationships under current licensing. Sensitivity labels/templates can enforce protected meeting configurations. Validate each participant role against the current feature/license matrix, particularly when capacity or cloud changes.

For Copilot in meetings, trace user license, meeting policy/option, transcript/recording context, client, organizer settings, data policy and service availability. The [Copilot policy table](https://learn.microsoft.com/en-us/microsoftteams/copilot-teams-transcription) separates defaults from enforcement: `Disabled` makes Off the organizer default but allows changes; `EnabledWithTranscript` enforces During and after. During-only speech-to-text is temporary, yet Commercial-cloud prompts/responses can remain under Purview retention. Organizer Off also disables recording/transcription. End-to-end encrypted meetings do not support Copilot. Test the actual option and available transcript, not merely the policy name.

### Teams Phone numbers, policies, and call flows

Separate the cloud phone system from PSTN connectivity. Microsoft Calling Plans, Operator Connect and Direct Routing provide different number/carrier/SBC/operating models. MS-700 focuses managing numbers and services; MS-721 goes deeper on systems engineering.

Number types include user/subscriber, service and conferencing bridge numbers under applicable availability. Assign the correct license and usage location, acquire/port/provision the number, assign to user or resource account, configure emergency/calling settings and test inbound/outbound/caller ID/emergency behavior.

Calling policies govern user call capabilities; voice-routing policy/PSTN usages/routes determine Direct Routing path; caller ID, dial plan and emergency policies solve other tasks. Voicemail policies govern cloud voicemail behavior.

Auto attendants provide menus, greetings, schedules/holidays and routing. Call queues distribute calls among agents using routing and presence/overflow/timeout settings. Both use licensed resource accounts and can transfer to people, queues, voicemail or external numbers as supported. Directly answering queues require resource accounts; nested voice applications can use the parent’s account. Check the route rather than licensing every diagram box. Since November 1, 2025, minute-based Calling Plan licenses alone do not fund resource-account on-behalf-of outbound calls, external transfers or callbacks: validate pay-as-you-go/credits/overage for the subscription. Operator Connect needs carrier confirmation; Direct Routing uses its voice routing policy. Design a call-flow diagram and test business hours, after hours, holiday, no-answer, overflow, agent opt-in, delegation and failure.

**Worked example 4 — Callback timing is part of call routing.** In a synthetic [queue](https://learn.microsoft.com/en-us/microsoftteams/aa-cq-setup-call-queue), eligibility begins at 70 seconds; the current music ends at 90, caller input completes at 98, an agent is available at 150, and answers at 165. A 160-second timeout fails this path by **5 seconds**, despite early eligibility. A 180-second timeout leaves only **15 seconds** of margin for this sample, not a service guarantee. Validate publicly dialable E.164 caller eligibility, outbound funding and failure-notification handling as well. Callback eligibility alone does not ensure an offer or a completed callback.

> **Related item:** A resource account is an identity used to anchor voice service; an auto attendant or call queue is the call-flow application. Licensing the resource account does not build or validate the call flow.

---

## 4. Monitor, report on, and troubleshoot Teams

### Monitoring and reporting

[Teams meeting and call troubleshooting](https://learn.microsoft.com/en-us/microsoftteams/monitor-troubleshoot-teams-meetings-calls) spans service health, usage reports, CQD, Call Analytics, real-time telemetry, device/client health and diagnostics. Define audience, freshness, denominator, privacy and action for every report.

- CQD finds organization/site/build/network patterns and uses tenant data/reporting labels for meaningful locations.
- Call Analytics investigates a specific user's meetings/calls and device/network/system details.
- The current user/meeting/participant troubleshooting views expose in-progress data for all license types. Granular telemetry persists seven days for Teams Premium/Rooms Pro; other users retain it only during the meeting. Aggregate telemetry remains for 30 days. Completed data can take 30 minutes–2 hours to process. Event attendee delivery is not covered by presenter/organizer telemetry.
- usage reports cover active users, team activity, apps, meetings, devices and other adoption signals.
- Microsoft 365 reports/storage views provide related group/SharePoint/OneDrive information.
- audit and group lifecycle evidence identify team creation/deletion and guest changes.

Configure alert rules for supported call-quality/device conditions and assign response ownership. Manage user feedback policy and review feedback as a signal, not proof. Correlate the Microsoft 365 network connectivity dashboard with actual affected sites and call evidence.

**Worked example 5 — Count affected people separately from sessions.** A synthetic incident has 120 sessions from 100 participants. Of 18 issue-marked sessions, 6 are second affected sessions for the same participants: **12 distinct affected participants**, or **12%**, versus **15% of sessions**. Keep both denominators, media direction and time window. In the current troubleshooting view, issue classification replaces the older Good/Poor labels; one red metric alone is not proof of a bad experience.

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

Copilot/AI troubleshooting adds license/service plan, meeting policy/option, transcript/recording, supported client/language, source permission, Purview control and feature rollout. A missing transcript is not fixed by granting broad SharePoint access. Use the Copilot decision table above and record tenant/cloud availability before changing access.

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

**Execution boundary:** This review ran offline arithmetic and repository checks only. None of the tenant, media, VDI, workflow, event or PSTN labs below was executed. Use a test tenant and synthetic data/phone plans where available. Do not test PSTN emergency calling casually; use carrier-approved validation procedures.

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

### Lab 9 — App and connector migration

Build a before/after audience matrix using example 3. Design a nonproduction Workflow notification with a co-owner, a replaced connection and both valid/invalid payload tests. Verify MessageCard content separately from interactive Adaptive Card actions. For private channels, record the unresolved documentation conflict and test the precise supported cloud/identity path before adoption. **Evidence:** intended versus effective audience, consent inventory, ownership continuity, posting results and rollback.

### Lab 10 — VDI and room authentication transition

Inventory endpoint OS, provider/plugin, Teams build and actual optimization status; identify the Windows WebRTC cohort before October 1. Tabletop a room’s initial sign-in, reauthentication, reprovisioning and retirement with narrowly scoped device-code exceptions. Do not infer successful passwordless migration from a blog announcement. **Evidence:** support dates, actual media path, account type, access-policy evaluation, recovery owner and pilot results.

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

37. **Which meeting policy wins over group rank 1?** A directly assigned policy of that same type.
38. **Does an allowed/pinned app with audience No one work?** No; effective availability, installation and consent are different controls.
39. **Can a custom federation domain list differ from the tenant list?** Yes, while tenant federation and partner trust must still allow communication.
40. **What changes October 1 for Windows VDI endpoints?** Legacy WebRTC optimization loses support for the specified Citrix/AVD/Windows 365 cohort; April 1, 2027 ends availability.
41. **Does Copilot policy Disabled enforce an unchangeable ban?** No; it sets an organizer-editable default.
42. **What fails in the 160-second callback example?** The sample completes at 165 seconds, beyond queue timeout.
43. **Can presenter telemetry prove every event attendee received good media?** No; attendee delivery requires separate evidence.
44. **Can the private-channel webhook conflict be closed by an HTTP 200 source fetch?** No; confirm current supported cloud, posting identity and an actual scoped delivery result.

---

## Places to learn

This is a curated starting point, **not a complete list**, and it is not meant to be consumed in full. Choose one primary path, practice in a tenant, and select supplements from measured gaps. Reconcile all older resources with the July 29, 2026 blueprint, especially MTO, Copilot/AI troubleshooting, current events, policies and external collaboration.

The four official paths are [get started](https://learn.microsoft.com/en-us/training/paths/get-started-managing-microsoft-teams/) (3h36), [prepare the environment](https://learn.microsoft.com/en-us/training/paths/prepare-environment-for-microsoft-teams-deployment/) (3h20), [manage chat/teams/channels/apps](https://learn.microsoft.com/en-us/training/paths/manage-chat-teams-channels-apps-microsoft-teams/) (3h02), and [manage meetings/calling](https://learn.microsoft.com/en-us/training/paths/manage-meetings-calling-microsoft-teams/) (9h03), a historical total of **19 hours 1 minute** from the earlier review. Current pages list **20 modules (4/4/3/9)** but do not expose those runtimes in the retrieved text; treat the old times as planning estimates, not freshly verified durations.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MS-700 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-700) and [credential page](https://learn.microsoft.com/en-us/credentials/certifications/m365-teams-administrator-associate/) | Public | 1–2 hours initially; 15 minutes per recheck |
| Four official paths from [MS-700T00](https://learn.microsoft.com/en-us/training/courses/ms-700t00) | Public | Historical 19h01 estimate; 20 modules currently listed; allow 30–50 hours with labs/notes |
| MS-700T00 instructor-led course | Paid/partner delivery | 4 days listed |
| [Microsoft MS-700 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/m365-teams-administrator-associate/practice/assessment?assessment-type=practice&assessmentId=55&practice-assessment-type=certification) | Public | 45–75 minutes per attempt plus source review |
| [Pluralsight MS-700 path](https://www.pluralsight.com/paths/managing-microsoft-teams) | Paid | Five public course listings total 18h58 (path rounds to 19h); 2022/2024 dates require current-doc supplements |
| [O'Reilly/Packt MS-700 Third Edition](https://www.oreilly.com/library/view/ms-700-managing-microsoft/9781835883945/) by Nate Chamberlain and Peter Rising | Paid | Historical 10h41 / 502 pages, August 2024; page blocked on recheck, current edition/content unverified |
| [O'Reilly/ACI MS-700 video](https://www.oreilly.com/videos/managing-microsoft-teams/9781836643135/) with Adam Gordon | Paid | Historical 31h03, August 2024; page blocked on recheck, current content unverified |
| [Udemy MS-700 with labs](https://www.udemy.com/course/microsoft-teams-examlabpractice/) by John Christopher | Paid | Page blocked; historical February 2026 update and runtime unverified now; allow 20–35 hours with practice |
| [MeasureUp MS-700](https://www.measureup.com/microsoft-practice-test-ms-700-managing-microsoft-teams.html) | Paid | 155 questions (69/36/31/19), September 2025 update verified from public listing; paid questions and July/October completeness unreviewed; allow 6–10 hours |
| [Udemy current-blueprint practice](https://www.udemy.com/course/ms-700-practice-tests-teams-administrator-2026/) by Dean Ellerby | Paid | Page blocked; historical 360-question/August 2026 claims and originality unverified; allow 10–16 hours with source review |
| [Microsoft Mechanics](https://www.youtube.com/@MSFTMechanics), [Microsoft Reactor](https://www.youtube.com/@MicrosoftReactor), and [John Savill](https://www.youtube.com/@NTFAQGuy) | Public | 2–10 hours selectively; no complete current MS-700 playlist was confirmed |
| [Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner-restricted | Schedule dependent; use the published event start/end times after sign-in |

Public page retrieval does not establish access to course lessons or practice questions. Practice Assessment, video channels, connectivity dashboard and Partner Skilling Hub returned shells; their interactive content was not reviewed. MS-700T00 currently lists four days and English. Older catalogs still use connectors, live events and older appointment names; supplement those with current primary documentation.

### Blog reading with a task

| Reading | Why it earns a place | Learning output |
|---|---|---|
| [Office 365 connectors retirement](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/) — Microsoft developer team, original July 3, 2024; controlling update April 14, 2026 | Records successive deadline changes; the latest update supersedes older dates. MessageCard rendering is not interactive-button support. | Inventory notifications, convert interactive payloads to Adaptive Cards, and document ownership/recovery. Keep the private-channel conflict open. |
| [What’s new in Teams, July 2026](https://techcommunity.microsoft.com/blog/microsoftteamsblog/what%E2%80%99s-new-in-microsoft-teams--july-2026/4542510) — Kerry Perez Heffernan, July 31 | Highlights app/agent request handling and Windows Rooms passwordless support. Announcement scope must be checked against the deployed device/cloud. | Trace request → approval → audience → consent → working app; separately write a room migration acceptance/recovery checklist. Neither demo execution nor fleet-wide feature availability was verified. |

Start with Microsoft's free Practice Assessment. Add paid questions only for a different explanation style or measured gap; reject any provider claiming recalled live questions.

## Final readiness checklist

- I can map each objective to its owning Teams/Microsoft 365 object, role, policy, evidence and recovery.
- I can calculate and validate network/media readiness and use CQD versus Call Analytics correctly.
- I can govern team/group/data lifecycle, external/guest/shared-channel/MTO collaboration and device clients.
- I can manage teams, channels, chats, apps and extensibility without confusing Teams policy with Entra/resource authorization.
- I can select and configure meeting/event and Teams Phone objects, policies, licenses and call flows.
- I can troubleshoot client, sign-in, media, meeting and Copilot issues without erasing evidence or weakening policy broadly.
- I completed or tabletop-tested all ten labs and can prove positive and negative outcomes.
- I passed an independent readiness check without relying on recalled live-exam content.
