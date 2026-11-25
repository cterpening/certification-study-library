---
exam_code: NSE-5-SASE
vendor_id: fortinet
official_blueprint: https://training.fortinet.com/local/staticpage/view.php?page=fortisase_and_sd-wan_core_administrator_exam
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-10-28
upcoming_change_status: scheduled
upcoming_change_checked: 2026-10-28
---

# Fortinet NSE 5 in SASE Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Fortinet's live NSE 5 SASE track, FortiSASE and SD-WAN Core Administrator exam page, current course pages, and official product documentation were rechecked October 28, 2026. The [exam page](https://training.fortinet.com/local/staticpage/view.php?page=fortisase_and_sd-wan_core_administrator_exam) is authoritative for scope.

**Current baseline:** Fortinet NSE 5 - FortiSASE and SD-WAN **26** Core Administrator: FortiSASE 26, FortiOS 7.6, FortiClient 7.0, FortiAuthenticator 6.5, and FortiManager 7.6. Decentralized SD-WAN 20–30%; Rules and routing 15–25%; SASE deployment 20–30%; SIA and SSA 15–25%; Analytics 15–25%. These ranges deliberately overlap; do not normalize them into invented fixed weights.<br>
**Exam contract:** 30–35 questions, 65 minutes, English and Japanese, pass/fail score report, multiple-choice and drag-and-drop under the track's general proctored-exam rules.<br>
**Credential contract:** Hold active NSE 4 FortiOS and pass the NSE 5 SASE exam within two years. The credential is active for two years from the NSE 5 exam date; confirm the live track page for renewal and exam reuse rules.<br>
**Upcoming change:** The earlier FortiSASE and SD-WAN 7.6 Core Administrator exam remains available only until **November 14, 2026**. Its FortiSASE 25 baseline and unweighted topic list are not the current 26 blueprint. New candidates should use version 26 unless they deliberately booked the retiring form.<br>
**October 28, 2026 product note:** Current FortiSASE feature release notes describe expanded REST API coverage, remote-user SAML onboarding, and new points of presence with specific availability or eligibility conditions. Verify the feature train, tenant, region, and license before applying them; sovereign deployments have separate guidance. See the [FortiSASE feature-release notes](https://docs.fortinet.com/document/fortisase/latest/feature-release-notes/661728/whats-new).<br>
**Integrity:** Use official samples only for format and original scenarios for readiness. Reject recalled, leaked, or guaranteed-match questions.

> **September 17, 2026 contract check:** Current official exam and track pages were inspected; the exam times and prerequisite statements above reflect that check. Historical objective snapshots and full technical-review dates remain unchanged. See the [exam validation report](../docs/research/2026-09-17-exam-validation.md).

## How to use this guide

Treat SASE as an end-to-end access decision, not a cloud proxy checkbox. For each task, trace user/site, device, identity, transport, service edge, policy, inspection, destination, response, log, failure, and responsibility. Build the SD-WAN and FortiSASE pieces separately, then prove their integration.

> **About related items:** A `Related item:` callout adds architecture, operations, governance, or lifecycle context. It makes an official task useful in real deployments but is not claimed as verbatim exam scope.

## Blueprint map

| Domain | Published range | Evidence of readiness |
|---|---:|---|
| Decentralized SD-WAN | 20–30% | Working DIA topology with members/zones, relevant SLA, state/logs, and failure proof |
| Rules and routing | 15–25% | Explained route and SD-WAN rule choice, session behavior, FortiManager state, and return path |
| SASE deployment | 20–30% | Provisioned tenant/site/user onboarding with identity, residency, license, and integration evidence |
| SIA and SSA | 15–25% | Scoped inspection and endpoint compliance with trust, privacy, exceptions, and positive/negative tests |
| Analytics | 15–25% | Correlated SD-WAN/user/security events, useful dashboards/reports, external delivery, and freshness checks |

## 1. Decentralized SD-WAN (20–30%)

### Design the DIA path

Identify branch/users, applications, underlays, overlays, internet egress, FortiGate, FortiManager, FortiSASE points of presence, DNS, identity, security inspection, and return path. Direct internet access can reduce backhaul but moves policy, logging, and failure responsibilities to each edge and service path.

Create members from usable interfaces/tunnels and group them into zones according to policy intent. Record addressing, gateways, route availability, bandwidth, cost, metering, carrier, NAT, MTU, and failure domain. Do not assume two links are diverse because their provider names differ.

### Build meaningful performance SLAs

Active probes generate tests; passive measurements observe relevant traffic where supported. Define target, source/interface, protocol, frequency, thresholds, loss/latency/jitter criteria, update/fail/recovery behavior, member-state action, and business meaning. A public ping can stay healthy while DNS, TLS, SaaS, or the intended overlay fails.

Monitor members, SLA state, widgets, traffic logs, events, and actual application experience. Test hard-down, brownout, target-only failure, asymmetric return, and restored-but-unstable path. Use hysteresis or appropriate recovery settings to prevent flapping.

**Related item: failure domains.** Carrier, last mile, power, DNS, service edge, identity, cloud application, and configuration may be shared even when underlay interfaces are separate.

## 2. Rules and routing (15–25%)

### Derive an SD-WAN rule decision

Rules can match source, destination/internet service, user/application, protocol, and other supported criteria. Know explicit order, the implicit rule, and when application learning delays or changes steering. For manual, best-quality, and lowest-cost/SLA strategies, explain eligibility, preferred-member election, quality metric, priority, load balancing, SLA targets, and the effect of minimum members meeting SLA.

Do not treat an SD-WAN rule as a firewall policy. Routing establishes reachable candidate paths; the SD-WAN rule selects eligible members; firewall policy and SNAT permit/translate traffic. Existing sessions may remain, be re-evaluated, or break according to protocol, flags, route change, and settings.

### Explain routing and sessions

Read the routing and session tables. Compare most-specific route, administrative preference/distance, member or zone route, policy route, probe route, local-out traffic, selected egress, translated tuple, and return path. A healthy SLA cannot select a member that lacks valid reachability.

FortiManager can centrally manage supported SD-WAN configuration and templates. Understand ownership, install preview/diff, target scope, revisions, errors, drift, and rollback. Verify installed device state and runtime behavior; a successful policy-package install is not proof of working applications.

**Related item: session evidence.** Save original/translated tuples, rule, route, member, protocol state, timestamps, logs, and behavior before and after failover.

## 3. SASE deployment (20–30%)

### Provision responsibly

Map tenant, region and data residency/sovereignty, licensing, administrators, identity sources, points of presence, sites, users, endpoints, connectors/tunnels, IP address management, certificates, logs, external integrations, retention, and support. Confirm feature and regional availability under the current FortiSASE 26 entitlement.

Restrict administration with federation/MFA, least-privilege roles, named accounts, emergency access, audit logs, and periodic review. Document provider/customer responsibility for platform, endpoint, identity, policy, data, integration, and evidence.

### Onboard users and sites

Agent-based onboarding uses FortiClient and endpoint configuration to steer and evaluate managed users/devices. Agentless secure-web-gateway mode uses supported proxy/browser patterns and has different traffic, protocol, identity, and posture coverage. Test install/enrollment, configuration delivery, upgrade, user switch, network transition, tamper/offline state, and uninstall.

Local identity, LDAP, RADIUS, and SAML SSO have different trust, availability, group, certificate, and lifecycle dependencies. Test correct group, wrong group, disabled account, expired certificate, identity-provider outage, stale session, and emergency recovery.

Integrate FortiSASE with SD-WAN by mapping site tunnels/connectivity, routing, communities/tags or current integration objects, security policy, failover, logging, and ownership. Confirm that private, internet, and SaaS traffic take the intended paths without loops or unintended bypass.

**Related item: identity confidence.** A successful login is not sufficient; authorization group, device posture, session freshness, risk, and destination sensitivity shape the decision.

## 4. Secure internet and SaaS access (15–25%)

SIA applies security to internet-bound access. SSA focuses on SaaS visibility and control, including supported inline CASB and FortiCASB patterns. Define traffic coverage, managed versus unmanaged access, sanctioned/unsanctioned apps, tenant instance, upload/download/action, and data sensitivity. Do not assume inline and API-based CASB have identical visibility or timing.

Security profile groups can combine certificate/full SSL inspection, web filtering, application control/inline CASB, antivirus, DLP, video filtering, and IPS. Match profiles to policy, user/device, geography, application, risk, and legal/privacy requirements. Full inspection requires managed trust, protected CA keys, exceptions for pinning/mTLS or regulated traffic, capacity, and failure handling.

DLP needs accurate data classification, direction, application/action, inspection visibility, incident ownership, false-positive workflow, exception expiry, and protected logs. Geofencing and IPAM need correct address/location sources and change handling; neither should become the sole identity signal.

Endpoint profiles and compliance rules bind supported posture and protection settings to managed endpoints. Define required versions/settings, grace and remediation, user message, exception, offline behavior, and evidence. Test compliant, noncompliant, stale, unsupported, and unenrolled devices.

**Related item: safe rollout.** Stage controls in monitor mode or a pilot group, measure false positives and application impact, then enforce with rollback and emergency access.

## 5. Analytics (15–25%)

Trace log workflow from FortiGate/FortiClient/FortiSASE event through timestamp, identity, policy/rule, session, forwarding, storage, FortiView/dashboard, report, external server, alert, retention, and access. Log anonymization can reduce personal exposure but must preserve correlation required for authorized investigation.

Use SD-WAN logs to explain rule match, member selection, SLA and route/session behavior. Use security logs for user, device, application, URL/category, file/threat, action, profile, location, and incident context. Distinguish no event from missing telemetry, delayed indexing, wrong time/filter, unsupported coverage, or successful prevention elsewhere.

Build dashboards and reports for a decision: unhealthy members, users bypassing expected onboarding, blocked high-risk activity, DLP incidents, policy exceptions, capacity, and data freshness. Reconcile summaries to raw events and a known synthetic test; schedule delivery securely and alert when expected reports or feeds stop.

## Integrated scenarios

### Hybrid workforce rollout

Inventory 500 managed users, contractors, two branches, SaaS, private apps, data regions, identity, and current VPN. Pilot agent-based and agentless groups, design SIA/SSA policy and compliance, integrate branch SD-WAN, validate logs, and define coexistence, support, rollback, and privacy boundaries.

### SaaS performance brownout

Users report intermittent SaaS failure while both links show up. Correlate application DNS/TLS, SLA target relevance, rule lookup, selected member, route/SNAT/session, FortiSASE PoP, inspection, and SaaS status. Change only after isolating the failing dependency; test stable recovery.

### Sensitive upload attempt

Trace user/device identity, SaaS tenant/action, TLS inspection, inline CASB/DLP, matched policy/profile, block/coaching outcome, log/report/external alert, exception workflow, privacy handling, and evidence retention. Use synthetic data only.

## Hands-on labs

1. Build a two-link DIA SD-WAN lab with members, zones, relevant active SLA, widgets, logs, brownout, outage, and stable recovery.
2. Create manual, best-quality, and lowest-cost/SLA rules; predict and verify route/member selection and implicit-rule behavior.
3. Capture session and SNAT state before and after route/SLA change for TCP and UDP synthetic flows.
4. Use FortiManager or a documented simulation to install scoped SD-WAN changes with preview, revision, validation, drift, and rollback.
5. In an entitled tenant/partner lab, provision FortiSASE roles, license/region, identity, one test user, and protected audit evidence.
6. Compare agent-based and agentless onboarding for protocols, identity, posture, failover, user experience, and removal.
7. Integrate one site with FortiSASE; prove internet, SaaS, private/bypass, failure, and return paths.
8. Apply SIA/SSA security profiles to harmless test traffic; validate inspection trust, allow/block, false positive, and expiring exception.
9. Create an endpoint compliance rule using disposable devices/synthetic posture; test remediation, grace, stale/offline, and deny.
10. Build a dashboard/report, forward selected logs, inject a known event, and detect a stopped pipeline.

## Original readiness checks

1. What prerequisites earn NSE 5 SASE?
2. Which exam version is the current baseline?
3. What is changing November 14, 2026?
4. How do underlay and overlay differ?
5. What belongs in an SD-WAN member inventory?
6. How do active and passive health measurements differ?
7. What makes an SLA target representative?
8. Why can interface-up still mean application-down?
9. How do manual, best-quality, and lowest-cost strategies differ?
10. What is the role of the implicit SD-WAN rule?
11. How does application learning affect steering?
12. Why does a healthy member still need a route?
13. How do route, SD-WAN rule, firewall policy, and SNAT relate?
14. What determines session behavior after a path change?
15. What must FortiManager change evidence include?
16. Which choices belong in initial FortiSASE provisioning?
17. How do residency and sovereignty differ operationally?
18. How do agent-based and agentless onboarding differ?
19. What must SAML/LDAP/RADIUS integration tests include?
20. What proves FortiSASE/SD-WAN integration?
21. How do SIA and SSA differ?
22. Why can inline and API CASB produce different evidence?
23. What does full SSL inspection require?
24. Which controls make DLP usable?
25. Why is geolocation not an identity?
26. What belongs in an endpoint compliance rule?
27. Why use a pilot before enforcement?
28. What constitutes the SASE log pipeline?
29. How do you distinguish no event from missing telemetry?
30. What makes a dashboard decision-ready?
31. Why monitor report or feed silence?
32. Which evidence explains an SD-WAN brownout?
33. How should an inspection exception be governed?
34. What is safe synthetic DLP testing?
35. Why must the live exam page be rechecked?

## Answers and reasoning

1. Active NSE 4 FortiOS plus the proctored NSE 5 FortiSASE and SD-WAN Core Administrator exam within two years.
2. Version 26 with FortiSASE 26 and the listed FortiOS/FortiClient/FortiAuthenticator/FortiManager baselines.
3. The older 7.6-named form using FortiSASE 25 reaches its published last-delivery date.
4. Underlay is transport; overlay is logical/tunneled connectivity built across it.
5. Interface/tunnel, addressing/gateway, zone, route, carrier/failure domain, bandwidth/cost, NAT/MTU, owner, and health.
6. Active sends probes; passive derives quality from observed traffic where supported.
7. It tests the relevant path/service property with correct source, protocol, frequency, thresholds, and recovery meaning.
8. DNS, route, loss/jitter, overlay, service edge, identity, inspection, destination, or return path can fail.
9. Manual uses configured preference/load distribution; best-quality compares metrics; lowest-cost selects eligible members using SLA/cost logic.
10. It handles traffic not matched by an earlier explicit rule under the documented default strategy.
11. Classification may require initial sessions, so early traffic may use a different rule/path than learned application traffic.
12. SLA describes quality; forwarding still requires an eligible route and next hop.
13. Route makes paths eligible, SD-WAN chooses a member, policy authorizes/inspects, and SNAT transforms the source when configured.
14. Protocol/state, session flags, reevaluation triggers/settings, NAT, route/member availability, and return symmetry.
15. Owner/target, preview/diff, template/package revision, install result, device state, runtime validation, drift, and rollback.
16. Tenant/region, residency, license, roles/identity, users/sites/endpoints, connectivity, IPAM/certificates, logs/retention, and integrations.
17. Residency is where data is stored/processed; sovereignty concerns which jurisdictions and laws govern it.
18. Agent mode can steer/control a managed endpoint broadly; agentless proxy mode covers supported proxy traffic with different posture/protocol limits.
19. Trust/certificate, source connectivity, groups/attributes, correct/wrong/disabled identities, outage, stale session, logs, and recovery.
20. Expected routes/tunnels/policy carry internet/SaaS/private flows through intended paths, survive failures, log correctly, and avoid bypass/loops.
21. SIA protects general internet access; SSA adds SaaS-specific visibility/control such as tenant and action where supported.
22. Inline sees transiting requests in real time; API inspection queries provider data/actions later and has different scope.
23. Managed CA trust, protected signing key, supported traffic, privacy/legal basis, capacity, exceptions, logs, and failure plan.
24. Classification, scope/direction/action, inspection coverage, owner, workflow, testing, false-positive tuning, exception expiry, and protected evidence.
25. VPNs, mobile networks, proxies, stale databases, and shared egress make an IP-derived place uncertain and spoofable.
26. Device scope, required posture/version/settings, evaluation cadence, grace/remediation, user message, exceptions, offline/stale behavior, and logs.
27. It measures false positives, performance, compatibility, support load, and rollback before broad impact.
28. Source event, time/identity/session/policy, transport, storage/index, dashboard/report/alert/external delivery, retention, and access.
29. Check source health, coverage, timestamps, delivery/index lag, filters/schema, license, and a known test event.
30. Defined audience/decision, correct denominator/time, freshness/missing-data signal, owner/threshold, raw drill-down, and validated result.
31. A silently failed pipeline creates false confidence that nothing happened.
32. SLA measurements, rule/member, routing, session/SNAT, application DNS/TLS, FortiSASE edge/inspection, destination, and timestamps.
33. Narrow stable scope, reason/risk, owner/approval, compensating control, expiry, monitoring, and restoration test.
34. Use invented patterns/files without real personal or regulated data, in an authorized tenant, with cleanup and protected logs.
35. Versions, retirement, weights, contract, products, policies, and eligibility can change independently of this guide.

## Key terms and phrases

**Decentralized SD-WAN (20–30%)**

| Term or phrase | Meaning |
|---|---|
| [Direct internet access (DIA)](#design-the-dia-path) | An arrangement in which branch internet traffic exits locally instead of traveling through a central site first. |
| [Availability](#design-the-dia-path) | Timely and reliable access to a resource by authorized users. A running server may still be unavailable to the business if a required dependency fails. |
| [Bandwidth](#design-the-dia-path) | The nominal data-carrying capacity of a link, usually expressed in bits per second. It does not by itself establish delay or delivered throughput. |
| [Failure domain](#design-the-dia-path) | A set of components that can fail together, such as workloads sharing a physical host, power source or region. |
| [FortiGate](#design-the-dia-path) | The Fortinet firewall platform that applies routing, access policy and security inspection to traffic traversing its interfaces. |
| [FortiManager](#design-the-dia-path) | A platform for centrally managing Fortinet device configurations and policy. A change staged in its database must reach the intended devices to affect traffic. |
| [FortiSASE](#design-the-dia-path) | Fortinet’s cloud-delivered access and security service for supported users and sites, with different traffic paths for internet, SaaS and private access. |
| [Jitter](#build-meaningful-performance-slas) | Variation in packet delay. A link with acceptable average latency can still deliver poor real-time voice quality. |
| [Packet loss](#build-meaningful-performance-slas) | The share of transmitted packets that do not arrive. If 100 probes are sent over a path and 97 arrive, measured loss for that sample is 3%. |
| [Latency](#build-meaningful-performance-slas) | Elapsed time for data or a request to travel a defined path. Specify whether the measure is one-way delay or round-trip time. |
| [Overlay](#build-meaningful-performance-slas) | A logical network formed over underlying links, commonly using tunnels between branches and hubs. |
| [Performance SLA](#build-meaningful-performance-slas) | A Fortinet SD-WAN health measurement that compares eligible links against targets such as delay, jitter or loss for steering decisions. |
| [Source interface](#build-meaningful-performance-slas) | The interface on which traffic enters a firewall. Its zone and context can affect which routes and policies apply. |

**Rules and routing (15–25%)**

| Term or phrase | Meaning |
|---|---|
| [SD-WAN rule](#derive-an-sd-wan-rule-decision) | A policy that identifies a class of traffic and chooses among eligible links using its configured strategy. |
| [Firewall policy](#derive-an-sd-wan-rule-decision) | A rule that identifies matching traffic and determines its treatment. Rule order can change which action applies. |
| [Load balancer](#derive-an-sd-wan-rule-decision) | A component that sends eligible requests or connections to selected backends using health and distribution policy. |
| [Software-defined WAN (SD-WAN)](#derive-an-sd-wan-rule-decision) | A way to steer traffic among network connections according to policy and measured link conditions. |
| [Source NAT (SNAT)](#derive-an-sd-wan-rule-decision) | Rewriting the source address of a packet, commonly so internal hosts can use a shared external address. |
| [SD-WAN member](#derive-an-sd-wan-rule-decision) | An interface or connection eligible for SD-WAN forwarding under its zone, route and steering policies. |
| [Policy package](#explain-routing-and-sessions) | A managed set of policies assigned to installation targets. Editing the package and installing it on a device are separate steps. |
| [Rollback](#explain-routing-and-sessions) | Returning a change to a known acceptable state when results do not meet defined conditions. A valid rollback also accounts for data changed in the meantime. |

**SASE deployment (20–30%)**

| Term or phrase | Meaning |
|---|---|
| [Point of presence (PoP)](#provision-responsibly) | A service location where users or sites connect to the SASE provider for access and inspection. |
| [Data residency](#provision-responsibly) | The geographic location in which data is stored or processed. Copies, support access and backups can affect the answer. |
| [Data sovereignty](#provision-responsibly) | The effect of jurisdiction and legal authority on who may control or obtain data. A storage-region label alone is insufficient evidence. |
| [Federation](#provision-responsibly) | An arrangement that lets one security domain rely on identity information issued by another, under agreed trust and validation rules. |
| [Least privilege](#provision-responsibly) | Giving an identity only the permissions needed for its task, for as long as it needs them. |
| [Log retention](#provision-responsibly) | The period for which records remain available for an investigation or other defined purpose. Missing results outside that period cannot establish inactivity. |
| [Endpoint onboarding](#onboard-users-and-sites) | Enrolling a user device and establishing the identity, connection and settings it needs to reach the service. |
| [Failover](#onboard-users-and-sites) | Transfer of service to another HA member after a failure. Some sessions may need to reconnect. |
| [FortiClient](#onboard-users-and-sites) | Endpoint software used for supported connectivity and security functions, with effective capabilities determined by the deployment and assigned configuration. |
| [Identity provider (IdP)](#onboard-users-and-sites) | The service that authenticates an identity and makes assertions or issues tokens that a relying service can validate. |
| [Remote Authentication Dial-In User Service (RADIUS)](#onboard-users-and-sites) | A protocol used by network access equipment to consult a central authentication and authorization service and record accounting events. |
| [Security assertion markup language (SAML)](#onboard-users-and-sites) | A federation standard in which an identity provider issues signed assertions to a relying service, often for browser-based single sign-on. |
| [Single sign-on (SSO)](#onboard-users-and-sites) | An arrangement in which an authenticated session can be reused to access multiple authorized applications without a fresh sign-in at each. |

**Secure internet and SaaS access (15–25%)**

| Term or phrase | Meaning |
|---|---|
| [Secure internet access (SIA)](#4-secure-internet-and-saas-access-1525) | Protection applied to internet-bound traffic as it passes through the security service. |
| [Secure SaaS access (SSA)](#4-secure-internet-and-saas-access-1525) | Visibility and policy controls for use of supported software-as-a-service applications. |
| [Application control](#4-secure-internet-and-saas-access-1525) | A control that identifies the application using a connection and applies policy to it, even when several applications share a port. |
| [Endpoint profile](#4-secure-internet-and-saas-access-1525) | A set of managed configuration or protection settings assigned to selected endpoints. Group membership and precedence affect the effective settings. |
| [False positive](#4-secure-internet-and-saas-access-1525) | A detection that matches benign activity. Tuning requires understanding which condition made it match. |
| [Security profile](#4-secure-internet-and-saas-access-1525) | A set of inspection settings attached to a policy, such as antivirus or web filtering for allowed traffic. |
| [Software as a service (SaaS)](#4-secure-internet-and-saas-access-1525) | An application operated by a provider and consumed as a service. The customer still governs tenant settings, access and use of its data. |
| [Web filtering](#4-secure-internet-and-saas-access-1525) | A control that allows or blocks web access according to a URL, category or other policy criterion. |
| [Cloud access security broker (CASB)](#4-secure-internet-and-saas-access-1525) | A control between users and cloud services, or integrated through service APIs, that provides visibility and enforces policies on cloud application use. |

**Analytics (15–25%)**

| Term or phrase | Meaning |
|---|---|
| [Log anonymization](#5-analytics-1525) | Reducing the identifying detail in logs to protect privacy while retaining enough context for authorized analysis. |
| [Alert](#5-analytics-1525) | A notification that an observed condition met a detection criterion. An analyst needs context before treating it as an incident. |
| [FortiView](#5-analytics-1525) | A set of views that summarize activity from available log data and let an analyst narrow a result to its underlying records. |
| [Incident](#5-analytics-1525) | A case representing a security event or set of related events requiring coordinated investigation and response. |
| [Telemetry](#5-analytics-1525) | Logs, events and measurements supplied by managed systems. Customer attribution and collection health determine whether the records are usable. |
| [Timestamp](#5-analytics-1525) | A recorded time associated with an event. Distinguish source event time from collection or indexing time when building a timeline. |

**Worked examples and practice**

| Term or phrase | Meaning |
|---|---|
| [Virtual private network (VPN)](#hybrid-workforce-rollout) | A protected logical connection over a shared network. Its permitted destinations and traffic depend on routes and access policy. |

## Places to learn

This is a selective starting set, not a complete list and not a prescription to consume everything. Start with the exam page and official courses, then choose documentation and labs that close your gaps. Times are publisher-listed or planning estimates.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [NSE 5 SASE track page](https://training.fortinet.com/local/staticpage/view.php?page=nse_5_sase) | Public | 20–30 min | Prerequisite, credential, renewal, and current exam route |
| [FortiSASE and SD-WAN Core Administrator exam](https://training.fortinet.com/local/staticpage/view.php?page=fortisase_and_sd-wan_core_administrator_exam) | Public | 45–75 min | Canonical version 26 ranges, tasks, contract, experience, and 7.6 retirement |
| [FortiSASE 26 Core Administrator course](https://training.fortinet.com/local/staticpage/view.php?page=library_fortisase-core-administrator) | Free account; labs may vary | 8–16 hr estimate | Official SASE provisioning, onboarding, SIA/SSA, endpoint, and analytics instruction |
| [SD-WAN Core Operations Administrator](https://training.fortinet.com/local/staticpage/view.php?page=library_sd-wan-core-operations-administrator) | Free account; labs/ILT may cost | 12 hr lecture+lab listed | Members, SLA, rules, routing, sessions, and troubleshooting |
| [FortiSASE documentation](https://docs.fortinet.com/product/fortisase) | Public; automated access may be blocked | 15–30 hr selected | Current administration, architecture, deployment, and reference source |
| [FortiOS 7.6 documentation](https://docs.fortinet.com/product/fortigate/7.6) | Public | 12–25 hr selected | SD-WAN, routing, sessions, NAT, policies, inspection, and operations |
| [FortiManager documentation](https://docs.fortinet.com/product/fortimanager/7.6) | Public | 5–12 hr selected | Central management ownership, templates, installation, revision, and troubleshooting |
| [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) | Public | 3–5 hr selected | Vendor-neutral identity/policy/access context; not product authority |
| [Fortinet exam release notices](https://helpdesk.training.fortinet.com/support/solutions/articles/73000659982-nse-exam-release-notices-new-and-discontinued-exams) | Public | 15–20 min | Current release and last-delivery dates |
| [Fortinet YouTube](https://www.youtube.com/@Fortinet) | Free/YouTube | 5–12 hr selected | Official SASE/SD-WAN architecture and demonstrations; check version |
| Authorized FortiSASE partner/tenant and FortiGate/FortiManager lab | Gated/paid entitlement | 30–60 hr | Highest-value end-to-end deployment, failure, analytics, rollback, and cleanup practice |

## Final preparation

- Use the current version 26 blueprint unless intentionally booked for the retiring 7.6 form.
- Rebuild SD-WAN, onboarding, SIA/SSA, compliance, and analytics labs with failure and rollback evidence.
- Verify active NSE 4, exam availability/version, count, time, language, delivery, price, retake, and renewal immediately before booking.
- Use official sample questions only; reject real/recalled-question claims.
