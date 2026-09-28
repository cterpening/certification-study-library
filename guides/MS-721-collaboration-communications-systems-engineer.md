---
exam_code: MS-721
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-721
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# MS-721 Collaboration Communications Systems Engineer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide was checked against the April 28, 2026 objectives and cited public sources on September 28, 2026. The whole-guide deep review mapped 173 objectives in 19 groups; live infrastructure and independent human review remain pending. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ms-721-coverage-record). The [official MS-721 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-721) is authoritative.

**Current baseline:** Skills measured as of April 28, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 28, 2026.<br>
**Official source:** [MS-721 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-721)

The [deep-review report](../docs/research/2026-09-28-ms-721-deep-review.md) records the evidence and limits. The current credential lists 100 minutes; practice vendors’ question counts are not promises about the exam.

## How to use this guide

MS-721 is a systems-engineering exam. A feature is not finished when a portal toggle is on: its identity, license, number, carrier/SBC, policy, network, endpoint, emergency behavior, monitoring and support boundary must all agree. For each objective, practice this chain:

1. translate business, regulatory, room and user requirements into a supported topology;
2. choose licenses, identities, numbers, PSTN connectivity, devices and policy objects;
3. configure the smallest appropriate scope through Teams admin center or PowerShell;
4. validate inbound, outbound, failover, emergency, meeting and device behavior;
5. collect evidence in Call Analytics, Call Quality Dashboard (CQD), device portals and logs;
6. isolate the failing administrative, media, carrier, SBC, network, identity or endpoint boundary;
7. restore service and prove the expected and denied paths.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Plan and design collaboration communications systems | 20–25% | Which meeting, voice, room and network architecture meets the requirement with a supportable boundary? |
| Configure and manage Teams meetings, webinars, and town halls | 15–20% | Which tenant setting, policy, template, event setting and license controls the intended experience? |
| Implement and configure Teams Phone | 30–35% | Can users and voice applications make, receive, route and survive calls safely? |
| Configure and manage Teams Rooms and devices | 20–25% | Are shared endpoints correctly identified, enrolled, secured, configured, updated and monitored? |

---

## 1. Plan and design collaboration communications systems

### Meeting and event architecture

Select the collaboration format from audience, interaction, registration, production and control requirements—not just maximum attendance:

| Experience | Best fit | Design questions |
|---|---|---|
| Meeting | Many-to-many collaboration | Lobby, presenters, chat, apps, breakout rooms, recording/transcription and content control |
| Virtual appointment | Scheduled customer or client interaction | Booking workflow, browser join, reminders, queue/analytics and advanced appointment capabilities |
| Webinar | Structured event with registration | Public versus organization scope, registration fields, presenters, Q&A, branding and attendee reporting |
| Town hall | Produced one-to-many broadcast | Producers/presenters, attendee scale, eCDN, moderated interaction, recording and publishing |

Tenant meeting settings define service-wide capabilities/defaults. Meeting policies apply to organizers or participants depending on the setting. Templates package supported meeting options; template policies determine who can use them. Sensitivity labels can enforce protected meeting settings under applicable licensing. Per-meeting options finish the instance. Determine the controlling layer before changing global policy.

Plan polls, Forms, apps, Q&A, breakout rooms, avatars, controlled content, recording, transcription and Microsoft 365 Copilot together. Copilot behavior can depend on license, effective meeting policy, organizer options, transcript/recording choice, client and feature rollout. Teams Premium adds capabilities such as advanced meeting protection, templates, branding and enhanced event/appointment experiences; verify exact entitlement before promising a feature. The [current Copilot matrix](https://learn.microsoft.com/en-us/microsoftteams/copilot-teams-transcription) distinguishes the organizer-editable `Disabled` default from the enforced `EnabledWithTranscript` option. During-only speech processing does not imply that compliance copies of prompts/responses vanish. E2EE meetings do not support Copilot. Verify actual participant entitlements, options and transcript access in a rehearsal.

Audio Conferencing brings PSTN dial-in/out capabilities to meetings. Plan licenses, supported countries, default bridge number, toll versus toll-free inventory, dial-out restrictions and numbers shown in invitations. The bridge is a tenant service; a user-specific conferencing number and an organizer's policy/license still affect the invitation and behavior.

> **Related item:** PSTN Audio Conferencing connects a caller to a meeting. Teams Phone connects a user or voice application to ordinary telephone calling. Both use numbers, but they are different services and license/configuration paths.

### Teams Phone and PSTN connectivity

[Set up Teams Phone](https://learn.microsoft.com/en-us/microsoftteams/setting-up-your-phone-system) separates the cloud phone service from the method used to reach the public switched telephone network. Select per user/site/persona where supported:

| PSTN model | Carrier/infrastructure boundary | Strong fit | Main tradeoff |
|---|---|---|---|
| Microsoft Calling Plan | Microsoft supplies cloud PSTN service | Straightforward supported-region deployments | Availability, number and plan constraints vary by market |
| Operator Connect | Certified operator supplies PSTN and manages operator infrastructure | Retain a participating operator without customer SBCs | Operator geography/features and joint support boundary |
| Teams Phone Mobile | Participating mobile operator makes a SIM number the Teams number | Mobile-first users needing one business number | Supported operators/regions and user-number focus |
| Direct Routing | Organization/operator connects a certified SBC to Teams | Existing carriers, PBXs, analog devices, complex routing or multinational requirements | Organization owns more design, security, monitoring and support work |

Calling Plans include domestic, international and pay-as-you-go choices where offered. Teams Phone Mobile is for user numbers; do not assume it supplies Audio Conferencing or voice-application numbers. A tenant can mix connectivity models, but every user/number needs an unambiguous operational and emergency-calling design.

Shared Calling lets eligible users make PSTN calls through a shared resource-account number rather than each receiving a dedicated number. Plan the resource account, number, emergency policy/location, voice routing and user calling policy. [Shared Calling planning](https://learn.microsoft.com/en-us/microsoftteams/shared-calling-plan) uses an auto attendant for inbound reachability and its number for outbound identity. Users still need Teams Phone and voice enablement. [Configuration guidance](https://learn.microsoft.com/en-us/microsoftteams/shared-calling-setup) requires the user’s ordinary voice-routing policy to have **no PSTN usages**, while a Direct Routing resource account needs a policy with the appropriate usages. An inherited global usage list can silently defeat the design. Optional extension dialing is a documented exception to the ordinary “no user number” setup. Moving the shared resource number leaves policy objects present but can break calls.

Inventory number purpose and ownership:

- **user/subscriber number:** assigned to a voice-enabled user;
- **service number:** used for services such as auto attendants, call queues or conferencing under the applicable model;
- **resource-account number:** anchors a voice application or Shared Calling design;
- **private line:** gives an eligible user another inbound route under current limitations;
- **SMS-capable Calling Plan number:** supports current Teams SMS behavior only in supported markets/configurations.

[SMS planning](https://learn.microsoft.com/en-us/microsoftteams/sms-overview) currently limits this service to eligible Microsoft Calling Plan users/numbers in the US (including Puerto Rico) and Canada, with approved Brand and Campaign registration even for individual business messages. Voice enablement alone is insufficient. Do not infer SMS support for Operator Connect, Direct Routing, toll-free numbers, shared queue inboxes or other clouds from ordinary calling support.

**Worked example 1 — Count SMS segments, not chat bubbles.** Suppose ten Domestic licenses contribute 200 segments each and two PAYG licenses contribute zero: the tenant pool is **2,000 segments**. Measured outbound traffic contains 900 one-segment messages and 300 two-segment messages; inbound traffic adds 650 segments. Total usage is **2,150**, leaving **150 segments over the pool**. Use measured encoding/segment counts and current billing terms; the displayed number of messages or a simple character count can understate usage.

Document acquire versus port, losing/gaining carrier, authorization, emergency address, usage location, assignment date, rollback and validation. Porting is a business cutover: freeze conflicting changes, test temporary and final routing, and retain carrier escalation details.

### Direct Routing, extensions and survivability

[Direct Routing planning](https://learn.microsoft.com/en-us/microsoftteams/direct-routing-plan) starts with a Microsoft-certified Session Border Controller (SBC), a public trusted certificate, supported TLS/SRTP and DNS, a verified tenant domain and supported network paths. The SBC terminates/normalizes the carrier or PBX side and connects it to Teams; it is a security and availability boundary, not merely a route entry.

The outbound decision chain is:

**dialed string → tenant/user dial plan normalization → E.164 number → online voice routing policy → ordered PSTN usages → matching voice route → gateway/SBC → carrier**.

A dial plan changes what number the user meant. A voice route chooses where a normalized call goes. A translation rule at a gateway can adapt the called/calling number for the SBC/carrier. Do not use all three layers to repair the same malformed number without documenting ownership.

**Worked example 2 — Usage order can beat a more specific route.** In a synthetic [routing design](https://learn.microsoft.com/en-us/microsoftteams/direct-routing-voice-routing), usage Local contains pattern `^\+1425555[0-9]{4}$` and usage Broad contains `^\+[1-9][0-9]{7,14}$`. Both match `+14255550123`. Ordering Broad first sends this call through Broad; placing Local first selects Local. This is not automatic longest-prefix routing. Gateway order within one route is randomized, so a two-SBC list does not define deterministic primary/secondary preference. Use separate route priorities where needed, and test reachable-but-rejecting gateways as well as outages. Do not treat Calling Plan fallback as proof every Direct Routing failure is recoverable.

Plan redundant SBCs, routes and carriers with explicit priority/capacity and test failure—not only configuration presence. Local Media Optimization (LMO), Location-Based Routing (LBR) and media bypass solve different topology/regulatory/media-path problems. On-network conferencing can route applicable dial-out calls through Direct Routing. [SBA guidance](https://learn.microsoft.com/en-us/microsoftteams/direct-routing-survivable-branch-appliance) assumes the branch LAN and SBC/PSTN path still work, requires media bypass and a previously assigned survivability policy, and excludes VDI/web clients. Check the actual appliance-mode banner. Current supported functions include local-user VoIP behind the same SBA and selected forwarding/transfer/queue redirects; this does not make the cloud queue service available locally. Validate supported client/vendor versions, notification/recording limitations and failback after active outgoing calls finish.

SBA has material limits: clients need a prior connection within 24 hours; restarting can require a token the offline client cannot obtain. The documentation limits CAE-token operation to roughly 30 minutes. It also excludes dynamic E911 location sharing and emergency call routing policies; emergency strings need valid regular voice-route patterns. Include these limits in the approved continuity design and carrier test plan.

Certified compliance recording and contact-center solutions integrate through supported Teams models. Assign policies and validate vendor responsibilities, recording notification/storage/access, agent routing and failure mode. The Queues app provides supported delegated call-queue/auto-attendant management and operational experiences under its licensing and policy model. [Voice-application licensing](https://learn.microsoft.com/en-us/microsoftteams/aa-cq-reference-prerequisites-licensing) requires Teams Premium for Queues app users; its delegated controls still need authorization. Calling Plan resource-account outbound transfers/callbacks/on-behalf-of calling need current PAYG/credits/overage funding rather than an ordinary minute bundle. Confirm Operator Connect carrier support separately; Direct Routing needs its own voice route.

> **Related item:** A carrier says whether it accepted or delivered a PSTN call; Teams reports policy and cloud call legs; the SBC exposes SIP/TLS/media behavior. A complete Direct Routing incident often needs evidence from all three.

### Teams Rooms and certified-device design

Start with room purpose, size, layout, acoustics, sightlines, lighting, accessibility, occupancy, join patterns, support model and budget. Then choose certified compute, camera, microphone, speaker, display, console/panel and cabling. A technically certified kit can still fail in a room with poor acoustics or obstructed viewing.

Teams Rooms Basic and Pro differ in entitlement and management features. Windows and Android rooms differ in hardware architecture, enrollment/management and feature timing. [Rooms licensing](https://learn.microsoft.com/en-us/microsoftteams/rooms/rooms-licensing) limits Basic to 25 systems per organization, excludes panels, and requires Pro for multiple room systems using one account. Shared Space licensing is not a substitute for a Rooms license. For 28 single-system rooms with no advanced requirements, at least **3** need Pro because of the Basic cap; security, management or interop requirements can make more rooms need Pro. Plan a distinct room resource account, Exchange room mailbox/calendar processing, supported Rooms license, network access, Conditional Access posture, naming/location metadata and ownership.

Interoperability choices include:

- Direct Guest Join for supported third-party meeting services;
- Cloud Video Interop (CVI) for supported legacy/video conferencing endpoints joining Teams meetings;
- SIP Guest Join extends a CVI provider’s supported legacy SIP-room scenario to external Teams meetings;
- [cross-platform SIP/H.323 dialing](https://learn.microsoft.com/en-us/microsoftteams/rooms/meetings-with-sip-h323-devices) lets Windows **and Android** Teams Rooms with Pro, a supporting provider plan and the assigned video-teleconferencing policy call other SIP/H.323 endpoints;
- BYOD rooms, where a user's laptop provides compute and the shared room peripherals/identity/location supply the space experience.

The [third-party join comparison](https://learn.microsoft.com/en-us/microsoftteams/rooms/third-party-join) distinguishes DGJ’s browser path from SIP interop: examples include up-to-720p versus up-to-1080p video, one versus two displays, and HDMI sending support on the SIP path. These are conditional capabilities, not quality guarantees. Preserve external invitation bodies and verify mailbox processing and rewritten URLs when the join button is missing. Test the exact partner meeting type; a CVI agreement is not evidence every external feature works.

Personal/shared phones, displays, panels, Surface Hub, common-area phones, analog/SIP devices through SIP Gateway, bookable desks and full Teams Rooms are distinct endpoint types. Choose license, enrollment, configuration profile, calling/hotline behavior and management portal by device role.

### Network and media design

[Prepare the network for Teams](https://learn.microsoft.com/en-us/microsoftteams/prepare-network) before procurement or migration. Model personas, sites, concurrent modalities, direction and headroom. Use [Network planner](https://learn.microsoft.com/en-us/microsoftteams/network-planner) for assumptions and the current [Network Assessment Tool](https://www.microsoft.com/en-us/download/details.aspx?id=103017) for measured relay/connectivity diagnostics. The latter’s 1.9.0.0 listing is current as of this review; it is not a load/stress generator and was not executed here.

Favor local Internet breakout and a short supported media path. Define VPN split tunneling where appropriate. QoS requires aligned client port ranges, DSCP marking and network trust/queuing; it prioritizes during congestion but cannot add bandwidth. [QoS guidance](https://learn.microsoft.com/en-us/microsoftteams/qos-in-teams) separates client source-port marking from service destination requirements; browser ports and Mac/mobile sharing markings differ from the default Windows table. [Network roaming](https://learn.microsoft.com/en-us/microsoftteams/network-roaming-policy) controls IP video and total average audio/video/video-sharing media bitrate at a site on supported Windows/macOS clients. Non-voice-enabled users need meeting-policy network lookup enabled. MBR is not a physical circuit reservation or a per-room capacity guarantee.

Upload tenant data and reporting labels to CQD so subnet/building/site patterns become meaningful. Network roaming policies can apply media settings based on network location. Maintain topology data as subnets change. CQD building labels, network policy sites and LIS emergency locations are separate datasets; updating one does not populate the others. eCDN reduces duplicate video delivery across constrained corporate networks for applicable town hall/streaming scenarios; validate provider, licensing, topology, capacity and test-event telemetry.

**Worked example 3 — Measure eCDN offload.** Assume 240 viewers each demand 3 Mbps: unoptimized site delivery is **720 Mbps**. A rehearsal measures 540 Mbps served through peers and 180 Mbps from the WAN: offload is **75%**. With 120 Mbps of other WAN traffic, total is **300 Mbps**. A 350 Mbps link with a chosen 20% reserve permits 280 Mbps, so this sample still misses the target by **20 Mbps**. [Microsoft eCDN](https://learn.microsoft.com/en-us/ecdn/intro) reduces duplicate delivery; it does not remove presenter contribution, Wi-Fi or peer-network constraints. Measure again with the real audience/network layout.

| Metric | Interpretation in context |
|---|---|
| Packet loss | Missing audio/video data; inspect direction and burst pattern |
| Jitter | Variable packet arrival; can exhaust playout buffers |
| Round-trip time | Conversational delay and talk-over risk |
| Bitrate/resolution/frame rate | Adaptation to bandwidth, policy, CPU or endpoint constraint |
| Concealment/poor-stream percentage | User-impact signal that needs endpoint/path correlation |

---

## 2. Configure and manage Teams meetings, webinars, and town halls

### Meeting policy stack and advanced experiences

Configure meeting settings first for tenant-wide behavior, then policies for cohorts, templates/labels for repeatable protected scenarios and meeting options for a specific event. For ordinary supported Teams policy types, [direct assignment beats ranked group assignment, then global](https://learn.microsoft.com/en-us/microsoftteams/assign-policies-users-and-groups); lower rank numbers win and nested membership does not inherit. Emergency site policy has a different precedence rule described below. Inspect the effective result for each policy type. Allow propagation time, but do not use propagation as an explanation without evidence.

Build a test matrix for organizer, co-organizer, presenter, internal attendee, guest/external attendee and anonymous participant. Validate scheduling, lobby, who can present, content sharing, chat, reactions, apps, recording/transcription, attendance reports, breakout rooms, Q&A and captions. Protected meetings may add watermarking, encryption, recording restrictions or sensitivity-label enforcement under applicable licensing.

Controlled-content scenarios require more than disabling screen sharing: decide who can present, whether attendees can request control, which apps/polls/forms are permitted, how files are shared and whether external participants can access downstream artifacts. Recording and transcript retention/access are governed by storage location, meeting roles, sharing and Purview policies as well as the Teams meeting setting.

Virtual appointments add external scheduling/join and operational requirements. Determine whether basic scheduling is enough or advanced appointment policies, queue views, notifications, analytics and branding are required. Test a browser/mobile external attendee rather than only a signed-in employee.

### Audio Conferencing

Assign the entitlement to organizers who need to create dial-in meetings. Configure the default conference bridge language and numbers, acquire toll/toll-free inventory, determine which numbers appear in invitations and configure user-specific default number/toll-free behavior where supported. Validate dial-in, meeting ID/passcode behavior, dial-out/call-me, anonymous restrictions and cost controls in every required country.

Changing the default bridge does not necessarily rewrite existing meeting invitations. Define when organizers must resend or recreate meetings and test a previously scheduled meeting during migration.

### Webinars and town halls

The [unified Events experience](https://learn.microsoft.com/en-us/microsoftteams/plan-town-halls) preserves webinar/town-hall policy controls. Optimize for large audience chooses town-hall behavior and is mandatory above 1,000 attendees; disabling it uses webinar controls. Retain the exam’s format distinctions while checking actual interaction and license requirements. [Legacy live events](https://learn.microsoft.com/en-us/microsoftteams/teams-live-events/plan-for-teams-live-events) retired June 30, 2026, with a grace period through February 28, 2027 for previously scheduled events.

For webinars, configure who may schedule, organization-only versus public registration, presenter/co-organizer roles, registration capacity/questions, communications, interaction, recording/publishing and reporting. Teams Premium may add advanced webinar functions; verify current license and organizer requirements.

For town halls, configure scheduling policy, organizers/co-organizers, presenters, attendee access, Q&A/chat/reactions as supported, recording and reporting. Plan rehearsals, producer/presenter device and network readiness, support bridge and contingency content. For corporate networks, evaluate and configure eCDN and validate with a representative audience; do not first test distribution at the production event.

> **Related item:** Webinar registration controls who receives an event join experience; lobby policy controls admission to a meeting. Similar-looking attendee problems can belong to different control planes.

---

## 3. Implement and configure Teams Phone

### User calling configuration and policies

For a voice user, verify identity, usage location, Teams Phone entitlement, PSTN-connectivity entitlement/model, TeamsOnly requirement where applicable, number assignment, emergency location/policy, dial plan, voice routing policy and calling/caller-ID/voicemail policies. Test internal Teams call, inbound PSTN, outbound local/national/international, transfer, forwarding, voicemail and emergency validation using approved procedures.

Policies have separate jobs:

| Object | Controls |
|---|---|
| Calling policy | Call features such as forwarding, delegation, simultaneous ring, call park, private lines and inbound handling where applicable |
| Caller ID policy | Presented caller identity and replacement/service-number behavior |
| Tenant dial plan | Number normalization rules |
| Online voice routing policy | PSTN usage/routes for Direct Routing |
| Emergency calling policy | Emergency notifications and related user experience |
| Emergency call routing policy | Emergency numbers, routes and dynamic behavior |
| IP phone/configuration profile | Supported phone/device settings |
| Voice applications policy | Delegated auto-attendant/call-queue/Queues app capabilities |

Call park retains a call against a retrieval code; group call pickup, simultaneous ring, forwarding and delegation distribute or hand off a user's calls. Cloud Voicemail handles unanswered calls with policies/settings for prompts, transcription and routing. Outbound restrictions and PSTN-usage design limit cost/risk. Unassigned-number routing sends calls to numbers in specified ranges to an announcement, user or voice application instead of failing unpredictably.

### Auto attendants and call queues

An auto attendant applies greetings, menus, schedules and routing. A call queue distributes callers to agents. Design them on paper before configuration:

1. create the application and its resource account where needed (directly answering applications require one; nested applications can use the parent’s account);
2. assign the Microsoft Teams Phone Resource Account license;
3. assign a service number if PSTN callers must reach it;
4. configure language, greetings/music, business hours and holidays;
5. configure destinations, agents, routing method, presence/opt-in, callback, overflow and timeout;
6. assign authorized users/voice applications policy for delegated management or Queues app;
7. test every branch, including closed, holiday, no agent, overflow, timeout and transfer failure.

[Resource-account guidance](https://learn.microsoft.com/en-us/microsoftteams/manage-resource-accounts) distinguishes the identity/number anchor from the application. Do not enable voice-application resource accounts for interactive sign-in. Resource accounts for Rooms are a different device identity type.

Routing methods and call priorities should match work rather than preference: serial, round robin, longest idle or attendant-style behavior can create different fairness and pickup outcomes. Presence-based routing, agent opt-out and callback change capacity assumptions. [Queue configuration](https://learn.microsoft.com/en-us/microsoftteams/aa-cq-setup-call-queue) makes callback eligibility, completion of music, caller response and agent answer share the timeout budget. A callback request can itself time out. Validate E.164 caller eligibility and failure notifications. Conference mode is recommended but incompatible with calls arriving from an LBR-enabled Direct Routing gateway; transfer mode is legacy, so retain a support-plan follow-up. Use custom music/prompts only with appropriate rights and a fallback.

### Dynamic emergency calling

Treat emergency calling as a life-safety design. Define civic addresses/emergency locations, network sites/subnets/switches/ports/wireless access points, Location Information Service (LIS), trusted IPs, emergency numbers, routing policies, notification/security-desk workflow and carrier/PSTN responsibility. A verified address is a prerequisite for applicable number assignment; it does not prove that a roaming client receives the right dynamic location.

**Worked example 4 — Location matching must use the client’s prefix.** A synthetic client reports `10.20.30.170/25`; its network ID is **10.20.30.128/25**. An LIS entry only for `10.20.30.0/24` does not satisfy that documented exact network-ID calculation. If a mapped wireless access point identifies Floor 3 while the subnet says Floor 1, the WAP wins. [Dynamic emergency guidance](https://learn.microsoft.com/en-us/microsoftteams/configure-dynamic-emergency-calling) orders WAP, switch/port, switch, then subnet. Confirm the client’s actual reported location after propagation; successful number assignment does not validate LIS.

Network-site emergency policy overrides the user’s policy at that site. Keep ordinary Direct Routing emergency-route requirements separate from the special Shared Calling procedure: Shared Calling requires a routing policy for every number model, with PSTN usages only for its Direct Routing path. Its emergency callback numbers must be routable, of the right number type/country and not reused across policies. A toll-free shared number cannot supply the empty-list callback fallback.

Test only through carrier-approved validation numbers/processes. Validate fixed office, remote user, VPN, branch/SBA, room/common phone and mobile scenarios. Record dispatchable-location behavior, callback, notification, route and failure escalation. Revalidate after network, carrier, SBC, office or number changes. Dynamic emergency calling/security notifications are not supported by the Teams web client. Direct Routing requires appropriate PIDF/LO support plus the emergency routing provider/ELIN design. Treat emergency-route tests and ordinary PSTN tests as separate acceptance results.

> **Related item:** A dial plan normalizes an ordinary number. Emergency call routing recognizes emergency dial strings and selects emergency behavior/routes. Never hide an emergency-design defect inside a broad normalization rule.

### Direct Routing implementation and troubleshooting

Implement in dependency order: verified domain/DNS and public certificate; supported SBC software/configuration; network/firewall; SBC pairing and health; PSTN usages/routes/gateways; voice routing/dial plans/translations; user assignment; emergency/LBR/LMO/media-bypass/SBA features; validation and monitoring.

When a call fails, collect UTC time, calling/called number, user, policy, correlation/call ID, location/client, SBC SIP ladder and carrier reference. Trace:

1. did Teams normalize the number as intended?
2. did effective voice routing policy expose a PSTN usage?
3. did an enabled route match the number and select a healthy gateway?
4. did TLS/SIP reach the SBC with expected identities/numbers?
5. did SBC translation/routing send it to the carrier/PBX?
6. what final SIP response and reason came from each boundary?
7. if signaling succeeded, did media negotiate and flow both ways?

[Current media-protocol guidance](https://learn.microsoft.com/en-us/microsoftteams/direct-routing-protocols-media) still limits the SBC ICE-Lite candidate to IPv4; signaling IPv6 support does not establish IPv6 media-bypass support. Correlate the selected endpoint after forked early responses, final answer and ICE nomination. One-way audio usually points to media path/NAT/firewall/SBC negotiation, not dial-plan matching. A 4xx/5xx/6xx SIP response must be interpreted at the hop that generated it. Use synthetic tests and Call Analytics/CQD trends, then prove failover by disabling a safe test route/gateway rather than waiting for an outage.

---

**Worked example 5 — Transfer acceptance is not destination answer.** In a synthetic Direct Routing trace, a blind transfer receives `202 Accepted` at 12:00:02 and the original leg ends immediately; the target later returns busy at 12:00:05. [June 2026 transfer behavior](https://learn.microsoft.com/en-us/troubleshoot/microsoftteams/phone-system/direct-routing/issues-with-call-transfers) permits the original-leg termination after SBC acceptance. Diagnose the subsequent target leg instead of treating that BYE alone as premature. Consultative transfers still require their own progress/completion handling. Preserve the Refer-To/Referred-By strings and correlate SIP legs; do not rewrite them as ordinary dial strings.

## 4. Configure and manage Teams Rooms and devices

### Resource accounts, enrollment and secure access

Each Teams Room needs its own room resource account/mailbox and supported license. Configure calendar processing, booking behavior, display name/location/capacity and Exchange room-list/Places metadata. Use a naming standard that identifies site/building/floor/room without exposing sensitive details.

[Microsoft's room-account guidance](https://learn.microsoft.com/en-us/microsoftteams/rooms/create-resource-account) and [Conditional Access guidance](https://learn.microsoft.com/en-us/microsoftteams/rooms/conditional-access-and-compliance-for-devices) require a device-compatible identity design. Do not apply ordinary interactive MFA, smart-card or certificate prompts to a headless shared-room sign-in. Use supported modern authentication, compliant device, known network/location and scoped Conditional Access. Pilot on test rooms and keep an exclusion/recovery path while proving policy behavior.

Android Teams devices use current AOSP/Microsoft Device Ecosystem Platform (MDEP) enrollment paths and supported Intune policies. Windows Rooms use Windows/Intune enrollment and device-specific configuration. Enrollment is not merely inventory: it supplies device compliance and access context. [AOSP enrollment](https://learn.microsoft.com/en-us/microsoftteams/devices/teams-aosp-enrollment) uses one corporate-owned, user-associated enrollment profile with For Microsoft Teams devices enabled. Teams devices use account credentials rather than its QR code. An expired token blocks enrollment/sign-in. Intune entitlement and assigned AOSP compliance policy must be ready before compliance-based CA; Basic alone does not include Intune. MDEP/OEM firmware readiness and Intune enrollment are different checks. Scope Teams compliance by enrollment profile when other AOSP devices share the tenant.

The [device-code policy guidance](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-teams-devices-device-code-flow) uses persistent, monitored exceptions for real device accounts and excludes Device Registration Service from the blocking policy. Exceptions are account-wide, not limited to a single room action. Include reprovisioning/recovery even for passwordless devices; confirm the installed authentication design rather than copying a legacy ROPC procedure.

### Operations and lifecycle

The [Android management transition](https://learn.microsoft.com/en-us/microsoftteams/rooms/aboutunifieddevicemanagement-pmp1) makes Rooms Pro Management the primary portal, with overlapping TAC workflows retiring during September 2026. Devices appear automatically after prerequisites; **configuration profiles must be imported as settings templates**. Portal entitlement does not mean every device needs a new Pro license. Check access/RBAC, required endpoints, minimum Admin Agent and actual device actions; an Entra AU-scoped administrator needs appropriate PMP role delegation. Existing pause settings generally carry over, but mandatory migration Agent updates are non-pausable. Follow the dated transition guidance and cloud-specific release status before relying on a rollout date. [Device management guidance](https://learn.microsoft.com/en-us/microsoftteams/devices/device-management) also distinguishes partial settings application from overwriting a full profile. Compare effective device settings after template import. [The XML reference](https://learn.microsoft.com/en-us/microsoftteams/rooms/xml-config-file) remains relevant to the exam, but Microsoft now recommends PMP settings and no longer publishes new XML settings. A correctly processed `SkypeSettings.xml` is consumed and deleted at startup; malformed XML can apply earlier settings before failure, omitted values stay unchanged, and unknown elements are ignored. File disappearance alone does not prove the intended outcome. Validate supported elements/case, keep a known-good configuration, and inspect effective settings after restart.

Create update rings: pilot representative hardware/peripherals first, observe meetings/sign-in/HDMI/content/camera/audio, then stage production. [Current Rooms release notes](https://learn.microsoft.com/en-us/microsoftteams/rooms/rooms-release-note) separate installed app updates from web-delivered features. Windows 5.6.210.0 (August 3) enables the Windows 11 25H2 update; an app update can therefore precede an OS change. September Android notes include SIP/H.323 dialing, subject to supported partner/configuration. [Admin Agent 865](https://learn.microsoft.com/en-us/microsoftteams/devices/certified-device-apps) lists provisioning/health fixes, with government-cloud rollout separate from public cloud. Match OEM, app, OS, Agent, cloud and management surface in acceptance evidence. A device shown as online is not proof that camera framing, microphone pickup, speaker output, dual display, HDMI ingest or guest join works.

September Android build `1449/1.0.96.2026249711` also fixes continued EWS calendar use on certain devices. The release excludes Cisco pending a later build. Verify the model-specific fix before disabling Exchange Web Services; a release-note date does not prove the device has migrated.

For Windows Rooms, exclude unsupported domain Group Policy/user security settings that interfere with the appliance account while retaining required device security. Validate custom display layouts and XML syntax/version support. For Android, use configuration profiles for supported settings, IP phone policies, hotline and remote deployment, and verify that the correct account/device type receives them.

[SIP Gateway](https://learn.microsoft.com/en-us/microsoftteams/devices/sip-gateway-plan) brings supported SIP devices into Teams. It requires a PSTN-enabled phone number, does not publish device presence for presence-based queue routing, and can offboard disconnected signed-in devices after 30 days (signed-out devices after 14). A desk phone in storage may need reprovisioning; basic SIP connectivity does not prove native Teams feature parity. Verify device model/firmware, network provisioning, authentication, policy, calling/emergency behavior and feature limitations. Common-area and conference phones, panels and displays need the correct shared-device identity/license and operational profile, not a reused personal account.

### Room features and flexible workspaces

Optional room capabilities include HDMI ingest, content camera, casting, proximity join, room remote, speaker recognition/intelligent audio/video, Direct Guest Join and hot desking. For each, record hardware/room/license/client prerequisites, privacy/accessibility effect and support fallback.

For BYOD rooms and bookable desks, define the physical-space inventory, peripheral association/discovery, building/floor/room metadata, booking/resource behavior and user workflow. Import or discover devices and assign them to the correct space; monitor adoption and bad mappings. A BYOD room may rely on a user's device for compute, but shared peripherals and space identity still require governance.

**Worked example 6 — Desk discovery needs distinct signals.** In [bookable desks](https://learn.microsoft.com/en-us/microsoftteams/rooms/bookable-desks), assume an auto-association threshold of three unique users. Alice docks four times, Bob once and Carol once: six events supply **three distinct users**, so the threshold is reached only with Carol. Alice’s repetitions alone do not qualify. Auto-association is for individual desks; pools follow their own mapping/capacity path. Missing, duplicate or invalid peripheral serial numbers are unsupported. Verify the actual desk and peripheral association, allow directory/association propagation, and distinguish a single reserved seat from a pool’s remaining capacity. Work-location updates also depend on policy and user opt-in.

### Device troubleshooting

Start with resource-account sign-in test, license, password/credential lifecycle, Conditional Access sign-in logs, device compliance/enrollment, Exchange calendar processing and service health. Then inspect Teams admin center/Pro portal health, app/OS/firmware version, network/DNS/proxy/time, peripherals and logs.

For remote provisioning failure, validate supported device/firmware, management URL/DHCP/DNS, provisioning code validity and physical possession. For proximity/casting failure, isolate Bluetooth/network/client/room policy. For calendar failure, compare Exchange room mailbox behavior with Teams sign-in rather than resetting the device immediately. Preserve logs before factory reset.

---

## Integrated scenarios

### Scenario 1: Multinational Teams Phone migration

Segment countries and personas. Choose Calling Plan, Operator Connect, Teams Phone Mobile or Direct Routing per regulatory/carrier/feature need; inventory licenses and numbers; design dial plans, routing, emergency calling and support boundary. Pilot porting and test inbound/outbound/emergency/voicemail/failover. Use CQD and carrier/SBC evidence during phased migration rather than changing all users at once.

### Scenario 2: Headquarters Rooms sign-in failure after security rollout

Identify room type, resource accounts, license, enrollment/compliance and exact Conditional Access result. Compare a working pilot room and inspect supported authentication requirements. Narrowly revise the device-account policy, validate sign-in plus blocked misuse, then expand through rings. Do not exempt all shared accounts or disable tenant MFA globally.

### Scenario 3: Executive town hall with remote sites

Select town hall rather than a meeting from scale/interaction; assign organizers/presenters; configure policy, eCDN and recording/Q&A; validate producer devices and contribution networks. Run a representative rehearsal, monitor real-time/presenter evidence and provide alternate content/support. Afterward, correlate attendee analytics, site delivery and support tickets.

---

## Hands-on labs

**Execution boundary:** This review performed offline calculations/decision checks and repository validation only. No tenant, room, SIP, emergency, PSTN, media, SMS, portal migration or network diagnostic was executed. Use a test tenant, lab numbers and synthetic data. Do not place test emergency calls except through carrier-approved procedures.

### Lab 1 — Architecture and licensing matrix

Design two sites and four personas. Compare all PSTN models, user/resource/room licenses, number types, room/device options and support owners. **Evidence:** decision matrix, assumptions and rejected alternatives.

### Lab 2 — Network, CQD and eCDN plan

Model concurrency and bandwidth, document ports/QoS/split tunnel/MBR, upload sample tenant topology/reporting labels and plan eCDN validation. **Evidence:** capacity worksheet and before/after test plan.

### Lab 3 — Meetings, webinar and town hall controls

Create a meeting policy/template and event policies. Test organizer, presenter, internal/external/anonymous attendee, recording/transcription and protected content. **Evidence:** effective-policy matrix and experience results.

### Lab 4 — Audio Conferencing and voice-user build

Map bridge/toll/toll-free and invitation behavior. Build a lab voice user with number, dial plan, calling/caller-ID/voicemail/emergency policies. **Evidence:** entitlement/object map and call test sheet.

### Lab 5 — Auto attendant and queue

Create resource accounts, schedules/holidays, menu, queue, agents, callback/overflow/timeout and authorized-user policy. Test every route. **Evidence:** call-flow diagram and positive/failure recordings or logs.

### Lab 6 — Direct Routing tabletop or lab

Build a sanitized topology with SBC, certificate/DNS, routes/usages/policies, translations, emergency and redundancy. If available, trace a synthetic call and failover. **Evidence:** SIP/routing trace and boundary-specific runbook.

### Lab 7 — Teams Room deployment

Create a room account and booking policy, model supported Conditional Access/compliance, assign configuration/update ring and validate peripherals/guest join. **Evidence:** room acceptance checklist and sign-in evidence.

### Lab 8 — Device and call-quality incident

Investigate one controlled sign-in/calendar/peripheral issue and one poor-media sample using Pro portal/TAC, Call Analytics, CQD, network and client/device evidence. **Evidence:** timeline, layer isolation, fix and retest.

---

### Lab 9 — Shared Calling and emergency-location evidence

Tabletop user and resource-account routing separately, including inherited global usages, extension dialing, shared-number replacement, emergency callback ownership and the LIS example. If an authorized test environment exists, use only the carrier-approved test process. **Evidence:** user/resource policy matrix, correct client location, return-call route, negative cases and recovery ownership.

### Lab 10 — Device-management and interop migration

Inventory app/OS/OEM/Agent/cloud versions, portal access and AOSP compliance. Reconcile settings-template imports and actual device state; test delegated scope, meeting join, required third-party capabilities and recovery after an unsuccessful configuration. **Evidence:** inventory, before/after settings, precise interop entitlement and feature tests; no completion claim based on devices merely appearing in PMP.

---

## Knowledge checks

1. **Teams Phone versus PSTN connectivity?** Teams Phone supplies cloud calling control; Calling Plan, Operator Connect, Teams Phone Mobile or Direct Routing supplies the public-network path.
2. **Why mix PSTN models?** Different countries/personas may need different carriers, mobile integration, legacy connectivity or operating control.
3. **Teams Phone Mobile best fit?** Mobile-first users using one participating-operator SIM number across native mobile and Teams endpoints.
4. **Shared Calling purpose?** Eligible users place PSTN calls through a shared resource-account number without dedicated numbers.
5. **Dial plan versus voice route?** Normalize what was dialed versus select an outbound PSTN path.
6. **PSTN usage purpose?** Link a user's voice routing policy to eligible ordered routes.
7. **SBC purpose?** Securely interconnect Teams Direct Routing with carrier/PBX signaling and media.
8. **SBA purpose?** Preserve supported branch calling during cloud-connectivity loss.
9. **LBR versus LMO?** Regulatory/location routing constraints versus optimizing media through local SBC topology.
10. **Why test Direct Routing failover?** Redundant configuration does not prove DNS, TLS, routing, carrier and media recovery.
11. **User versus service number?** Person endpoint versus voice application/conferencing service under applicable model.
12. **Resource account versus auto attendant?** Identity/number anchor versus menu/schedule routing application.
13. **Auto attendant versus queue?** Menu/time routing versus distribution to agents.
14. **Why test holiday/overflow?** The normal business-hours path does not prove exceptional routing.
15. **Verified emergency address enough?** No; validate dynamic client location, route, notification and callback under approved procedures.
16. **Meeting setting versus policy?** Tenant-wide capability/default versus scoped organizer/participant control.
17. **Template versus template policy?** Reusable meeting configuration versus which users can select it.
18. **Meeting versus webinar versus town hall?** Collaboration, registration-led structured event and produced one-to-many broadcast.
19. **Audio Conferencing versus Teams Phone?** Meeting PSTN access versus ordinary user/application telephony.
20. **Why resend an invitation after bridge changes?** Existing invitation details may retain old conferencing information.
21. **What affects meeting Copilot?** Entitlement, policy/options, transcript/recording context, client and rollout.
22. **Why eCDN?** Reduce duplicate corporate-network streaming traffic for applicable large events.
23. **QoS purpose?** Prioritize media during contention; it does not create capacity.
24. **CQD versus Call Analytics?** Aggregate site/subnet/build patterns versus a user/session investigation.
25. **Rooms Windows versus Android?** Different compute/enrollment/management and sometimes feature timing; validate requirements.
26. **Room resource account purpose?** Device sign-in plus Exchange booking identity for a shared room.
27. **Why not ordinary interactive MFA on Rooms?** The shared appliance sign-in cannot satisfy unsupported user prompts; use supported CA/compliance controls.
28. **Teams Rooms Pro management value?** Eligible proactive room monitoring/operations beyond ordinary device administration.
29. **Why update rings for rooms?** Validate hardware, peripherals, sign-in and meeting behavior before fleet rollout.
30. **SIP Gateway purpose?** Connect supported SIP devices to Teams with documented feature limits.
31. **BYOD room still needs governance?** Yes; physical space, peripherals, discovery, booking and metadata remain managed.
32. **Calendar missing but device online—first boundary?** Inspect Exchange room mailbox/calendar processing separately from Teams sign-in.
33. **One-way Direct Routing audio suggests?** Media/NAT/firewall/SBC negotiation before dial-plan changes.
34. **What proves a voice-user deployment?** Effective objects plus inbound/outbound/features/emergency-approved validation and telemetry.
35. **What proves a room deployment?** Booking, sign-in, meeting join, content, every peripheral, guest join, update and monitoring acceptance tests.
36. **Safest first incident action?** Capture user/device, UTC time, call/meeting ID, number, policy, location, logs and recent changes before resetting.

---

37. **Does Shared Calling remove the user’s Teams Phone requirement?** No; it shares the number, not the user’s entitlement.
38. **Which ordinary routing policy should be empty of usages?** The Shared Calling user’s; a Direct Routing resource account needs the proper usages.
39. **What is the SMS example’s excess?** 150 measured segments over the pooled 2,000.
40. **Does the most specific number pattern always win?** No; PSTN usage order and route priority matter.
41. **Is an SBC list an ordered failover pair?** No; gateways within a route are tried in randomized order.
42. **Is a valid address proof of dynamic location?** No; inspect actual LIS match, client and propagation.
43. **Can a site emergency policy override a direct user policy?** Yes; ordinary Teams policy precedence cannot be generalized to this case.
44. **Does a blind-transfer BYE prove the target answered?** No; acceptance and target completion are distinct.
45. **Does the AOSP profile QR code onboard a Teams room?** No; Teams uses its account-based enrollment path.
46. **Does deleting the processed XML prove every requested setting applied?** No; compare effective supported settings, including possible partial application.
47. **Do six dock events mean six distinct auto-association signals?** No; the example contains only three users.
48. **Does CVI enable every Teams Room to join every third-party meeting?** No; direction, endpoint, plan, policy and platform feature support differ.

---

## Places to learn

This is a curated starting point, **not a complete list**, and it is not meant to be consumed in full. Choose one primary route, build a lab/topology, and add resources only for measured gaps. Reconcile every older source with the April 28, 2026 blueprint, especially Shared Calling, SMS, Queues app, Copilot, current events, Android enrollment/MDEP, flexible workspaces and room/device features.

The two official paths are [plan and design Teams collaboration communications systems](https://learn.microsoft.com/en-us/training/paths/plan-configure-teams-voice/) (6h38) and [manage Teams collaboration communications systems](https://learn.microsoft.com/en-us/training/paths/manage-teams-voice/) (8h05), a historical total of **14 hours 43 minutes**. Current public pages list **15 modules (7/8)** without those runtimes in retrieved text; use the previous timings only as planning estimates.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MS-721 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-721) and [credential page](https://learn.microsoft.com/en-us/credentials/certifications/m365-collaboration-communications-systems-engineer/) | Public | 1–2 hours initially; 15 minutes per recheck |
| Two official paths from [MS-721T00](https://learn.microsoft.com/en-us/training/courses/ms-721t00) | Public | Historical 14h43; current 15 modules; allow 30–50 hours with labs/notes |
| MS-721T00 instructor-led course | Paid/partner delivery | 5 days listed |
| [Microsoft MS-721 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/m365-collaboration-communications-systems-engineer/practice/assessment?assessment-type=practice&assessmentId=78&practice-assessment-type=certification) | Public | 45–75 minutes per attempt plus source review |
| [Pluralsight MS-721 path](https://www.pluralsight.com/paths/microsoft-collaboration-communications-systems-engineer-ms-721) | Paid | Five public course listings total 8h04 (path rounds to 8h); 2023–March 2024 dates; paid lessons/practice unreviewed |
| [O'Reilly/Apress MS-721 Certification Companion](https://www.oreilly.com/library/view/microsoft-365-certified/9798868805189/) by Fabrizio Volpe | Paid | Historical 6h08 / 333 pages, October 2024; page blocked on recheck, current edition/content unverified |
| [MeasureUp MS-721](https://www.measureup.com/ms-721-exam.html) | Paid | 167 questions (47/26/59/35), January 2025 update verified publicly; paid content/April completeness unreviewed; allow 6–10 hours |
| [Microsoft Mechanics](https://www.youtube.com/@MSFTMechanics), [Microsoft Reactor](https://www.youtube.com/@MicrosoftReactor), and [John Savill](https://www.youtube.com/@NTFAQGuy) | Public | 2–10 hours selectively; no complete current MS-721 playlist was confirmed |
| [Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner-restricted | Schedule dependent; use published start/end times after sign-in |

Practice Assessment and video/partner sites returned public shells; no interactive questions or videos were reviewed. No exact current Whizlabs MS-721 offering was independently verified. Udemy listed several MS-721 question-only products, but this review did not establish enough provenance and freshness to recommend one. Start with Microsoft's free Practice Assessment; add paid questions only for a different explanation style or measured gap, and reject any provider claiming recalled live exam questions.

### Blog readings with an output

| Reading | Useful task and boundary |
|---|---|
| [Teams Rooms interop comparison](https://empowering.cloud/microsoft-teams-rooms-cloud-video-interop-vs-direct-guest-join-vs-cross-platform-meetings-via-sip/) — Tom Arbuthnot with Pexip’s Marius Nilsen, May 11, 2026 | Draw both calling directions and choose DGJ, CVI/SIP Guest Join or cross-platform SIP from requirements. The public synopsis is AI-assisted and team-reviewed; the video was not watched. Provider claims and older Android availability wording must be checked against current Microsoft documentation. |
| [What’s new in Teams, July 2026](https://techcommunity.microsoft.com/blog/microsoftteamsblog/what%E2%80%99s-new-in-microsoft-teams--july-2026/4542510) — Kerry Perez Heffernan, July 31 | Turn Windows passwordless Rooms and Android settings-management announcements into a device/version/license/policy/recovery acceptance sheet. The main article was read; demos and actual device deployment were not tested. |

## Final readiness checklist

- I can choose a meeting/event, PSTN model, device and network architecture from requirements and explain its support boundary.
- I can map every voice user, room and voice application to identity, license, number, policy, network and evidence.
- I can build and troubleshoot dial plans, voice routing, auto attendants, call queues, emergency calling and Direct Routing.
- I can configure policies/templates/settings for meetings, Audio Conferencing, webinars and town halls and prove participant behavior.
- I can deploy and secure Windows/Android Rooms, phones, SIP devices, BYOD spaces and bookable desks through supported enrollment and access controls.
- I can use Teams admin center, Rooms Pro Management, PowerShell, Call Analytics, CQD, device and SBC/carrier evidence without erasing the incident first.
- I have completed the current blueprint checklist, hands-on labs and at least two timed readiness attempts using original, source-explained questions.

