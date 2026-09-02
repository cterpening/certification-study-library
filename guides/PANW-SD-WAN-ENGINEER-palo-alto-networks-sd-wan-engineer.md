---
exam_code: PANW-SD-WAN-ENGINEER
vendor_id: palo-alto-networks
official_blueprint: https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/sd-wan-engineer-datasheet.pdf
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Palo Alto Networks Certified SD-WAN Engineer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live certification page, August 2025 datasheet, July 2025 certification handbook, and current public Prisma SD-WAN/SASE documentation were checked September 2, 2026. This does not guarantee that every explanation is error-free or remains current. The [official page](https://www.paloaltonetworks.com/services/education/palo-alto-networks-sd-wan-engineer) and [datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/sd-wan-engineer-datasheet.pdf) are authoritative.

**Current baseline:** planning/design 24%; deployment/configuration 24%; operations/monitoring 18%; Unified SASE 14%; troubleshooting 20%; August 2025 datasheet<br>
**Exam contract:** specialist-level English Pearson VUE certification. The current handbook uses an 860 passing score on a 300–1000 scaled range and provisional results. The datasheet does not publish item count, base duration, price, or a formal experience duration; verify registration.<br>
**Experience boundary:** the audience is experienced Prisma SD-WAN/SASE and network engineers. The blueprint expects engineering-level Prisma SD-WAN knowledge, TCP/IP and routing, topology, network security, SASE, automation, security architecture, and basic Python, PowerShell, and SQL.<br>
**Validity and renewal:** two years under the July 2025 handbook, subject to current pathway rules.<br>
**Upcoming change:** no retirement or dated replacement was found September 2, 2026. ION/controller releases, Strata Cloud Manager workflows, licenses, policy models, SASE integrations, ADEM, analytics, Device-ID, CIE, and copilot behavior are volatile; use the current release selector and tenant help.<br>
**Integrity:** actual exam content is confidential. This guide follows the public blueprint and uses original questions, synthetic data, and authorized labs only.

## How to use this guide

Approach Prisma SD-WAN as an application-aware forwarding and operations system. For each design, show the existing topology and traffic, applications/SLA, sites/circuits/bandwidth, failure modes, routing/VRFs, policies, identity/security integration, monitoring, ownership, and rollback. For each lab, retain before/after configuration, a uniquely identifiable flow, path/routing evidence, performance measurements, incident/audit evidence, and a failure test.

Use this operating loop:

1. baseline applications, topology, circuits, routing, capacity, and security;
2. define measurable outcomes and failure behavior;
3. select ION form/licensing, site roles, HA, interconnection, and policy hierarchy;
4. deploy a pilot, verify path/routing/security and telemetry, then expand;
5. monitor experience, incidents, device/circuit health, capacity, and changes;
6. troubleshoot from flow to policy to path to route to underlay, then optimize with measured evidence.

Use an authorized lab. Path, QoS, performance, routing, VRF, NAT, security, Prisma Access, identity, and template changes can disrupt or expose production traffic.

> **About related items:** A `Related item:` callout adds operational, governance, implementation, or lifecycle context. It helps connect a blueprint objective to reliable production work but is not claimed as verbatim exam scope.

## Blueprint map

| Domain | Weight | Evidence of readiness |
|---|---:|---|
| 1. Planning and Design | 24% | Turn inventory, application/SLA, bandwidth, topology, HA, security, and policy needs into a testable design |
| 2. Deployment and Configuration | 24% | Onboard sites/devices, apply controlled templates/settings, tune routing, and prove VRF segmentation |
| 3. Operations and Monitoring | 18% | Explain and validate device/controller evidence, notification workflows, reports, tool integrations, and SASE events |
| 4. Unified SASE | 14% | Connect Prisma SD-WAN with Prisma Access, ADEM, Device-ID, CIE, and user/group-aware enforcement |
| 5. Troubleshooting | 20% | Isolate connectivity, forwarding, performance, and policy failures; use copilot/analytics as evidence, not authority |

## 1. Planning and design — 24%

### 1.1 Device selection criteria

Start with site role (branch, data center, lab), deployment mode/topology, interface/circuit count and types, bandwidth, packets/sessions, application mix, HA, power/environment, routing, VRFs, services, encryption, cellular needs, and growth. Map those requirements to a currently supported physical or virtual ION model and software release. Include management reachability, licensing, spare/RMA approach, and lifecycle.

Prisma SD-WAN documentation distinguishes Analytics, Control, and Disabled modes. Analytics observes but does not apply policy or select application paths; Control forwards and applies path/security/QoS behavior; Disabled is in-path without monitoring/policy/path selection. Confirm current mode support and consequences in official documentation rather than assuming every device/site works identically.

### 1.2 Bandwidth plan

Inventory each circuit's provider, medium, committed/burst bandwidth, billing/metering, public/private addressing, MTU, NAT, SLA, measured latency/jitter/loss, availability, and failure correlation. Baseline ingress and egress by site, circuit, application, user, time, and growth. Size normal operation and degraded cases: if the best link fails, remaining links must carry prioritized demand without uncontrolled queueing.

Configured circuit capacities feed utilization and policy decisions, so wrong values corrupt both behavior and reporting. Define QoS classes/priorities, reserved or shaped capacity as supported, DSCP trust/rewrite, bulk scheduling, and oversubscription response. Validate with controlled load and application experience, not only a carrier speed test.

> **Related item:** Two circuits are not independent when they share a last mile, provider core, conduit, power, building entry, or cloud edge. Record common-mode failure explicitly.

### 1.3 Licensing options and tiers

Licenses determine available capacity, services, analytics/reports, integrations, or support under the current commercial model. Build a requirements-to-entitlement matrix with site/device, measured or licensed bandwidth, term, feature, tenant/region, start/expiry, renewal owner, and overage/service behavior. Verify current names and restrictions with Palo Alto Networks or an authorized partner; do not learn price or tiers from an old slide.

Test what happens before expiry or capacity limit: alerts, operational grace, reporting, configuration, and traffic impact. License presence is not proof that configuration, role, or data is enabled.

### 1.4 Assess the existing network

Capture physical/logical diagrams, WAN/LAN addresses, VLANs, routing/redistribution, NAT, DHCP/DNS/NTP, firewalls/proxies, identity, QoS/DSCP, applications/flows, circuits, monitoring/logging, change windows, and ownership. Measure route scale/convergence, bandwidth/performance, outages, packet size, asymmetric flows, overlapping prefixes, and undocumented dependencies.

For every application, record client/server/site, protocol/ports, discovery/classification, business priority, latency/jitter/loss/availability objectives, security path, failover tolerance, and validation owner. Identify whether insertion is router replacement, in-path, or another documented topology and define bypass/rollback before installation.

### 1.5 Data centers and DCI

Choose data-center site roles and endpoints from service reachability, route scale, redundancy, east/west needs, cloud/on-prem destinations, circuit diversity, traffic symmetry, and disaster recovery. DCI must define which networks/services are reachable, how routes are learned/advertised/filtered, preferred/backup paths, loop prevention, encryption, segmentation, failure convergence, and capacity in a one-data-center-loss case.

Avoid indiscriminate route advertisement or a default that hairpins cloud/SaaS unnecessarily. Test branch-to-data-center, branch-to-branch if intended, data-center-to-data-center, direct internet, and loss of every endpoint/path. Prove return routing and security path.

### 1.6 Branch gateway configuration

Define site, device, interfaces, circuit labels/categories/capacity, LAN networks, routing, DNS/DHCP dependencies, overlays, data-center/service groups, NAT/security/QoS/path/performance policy bindings, HA, and controller reachability. Standardize through templates where requirements match but leave documented, governed site-specific values.

Pilot a low-risk site. Establish acceptance tests for onboarding, routes, controller/device state, overlays, application identification, path choice, policy, direct/private traffic, logs/statistics, failover, and rollback. Record cabling/port mapping and out-of-band recovery.

### 1.7 Security requirements and configuration

Threat-model management/controller access, underlays/overlays, branch LAN, direct internet, east/west, cloud/data center, identity, APIs/integrations, logs, and administrators. Define segmentation, allowed flows, security policy, encryption/key/certificate lifecycle, role/MFA, secrets, device hardening, audit retention, vulnerability/software lifecycle, and incident response.

Prisma SD-WAN security policy, Prisma Access integration, and an external/on-prem firewall are distinct enforcement placements. For each flow, identify which control inspects it and what happens if the integration or tunnel is unavailable. Prevent bypass caused by alternate paths or fail-open assumptions.

### 1.8 Interconnectivity and HA

Map underlay, overlay, direct, standard VPN, service links, hubs/endpoints, routing adjacencies, cloud/service connectivity, and management dependencies. Define ION HA mode and supported topology, peer links/state, active roles, addresses, upstream/downstream convergence, session impact, circuit/path diversity, and split-brain prevention.

Test ION, LAN port/link, WAN circuit, overlay, data-center endpoint, controller reachability, power, and routing failures. Separate dataplane survivability from the ability to make changes or receive analytics while a control service is unavailable.

### 1.9 Policy design and management

Path policy selects allowed/preferred path types/categories for matching application, network context, prefix, user/group, and other current criteria. QoS policy classifies/queues/prioritizes/shapes traffic. Performance policy measures defined SLA conditions and can raise an incident or take supported remediation such as moving flows; probe and Link Quality Monitoring evidence have different scopes. Security policy permits/blocks according to supported match conditions. NAT policy translates source/destination using ordered rules/zones/pools/prefixes.

Use explicit intent, specific-before-general ordering, reusable stacks/sets, controlled defaults, owner, version, change ticket, test flow, rollback, and expiration where temporary. Model interactions: an allowed path can still be pruned by availability/performance/reachability; routing and most-specific destination can constrain choices; QoS cannot create bandwidth; NAT changes the identity used downstream. Verify the effective stack at the site and live flow decision.

> **Related item:** An aggressive SLA threshold without hysteresis, sufficient sample window, and a stable alternate can cause path flapping. Measure baseline, define raise/clear conditions, and test degraded-but-not-dead links.

## 2. Deployment and configuration — 24%

### 2.1 Deploy and configure Prisma SD-WAN

Prepare tenant/access/roles, subscriptions, sites, devices, activation/onboarding, software compatibility, topology, interfaces/circuits, controller reachability, overlays, routing, policy stacks, logging/integrations, and maintenance/rollback. Protect activation secrets and use least-privilege accounts. Confirm time/DNS/certificate and outbound requirements before shipping equipment.

Stage configuration and templates, inventory serial/virtual identity, validate cabling and bypass, then activate within a controlled window. Check controller association, device software, site assignment, interfaces/circuits, routes, VPNs/paths, application flows, policies, statistics, alarms, audit events, and failure recovery. Roll out in rings after the pilot.

### 2.2 Site-specific settings

Site-specific values commonly include addresses/VLANs, circuits/providers/capacities, device/port mapping, LAN networks, routing peers/ASNs, prefixes, NAT, local services, HA, and policy/template bindings. Classify every value as global standard, site class, or unique exception. Store authoritative inputs with validation and ownership; prevent copy/paste collisions.

An exception needs business reason, risk, compensating controls, approver, expiry/review, and a test. Compare configured and effective values after deployment. A syntactically valid duplicate subnet, ASN, interface, or site label can cause operational ambiguity.

### 2.3 Configuration templates

Create branch and data-center templates from validated common intent, with parameterized site-specific inputs. Define scope, inheritance/precedence, required/optional parameters, constraints, supported model/release, dependencies, owner, version, migration, and rollback. Keep branch and data-center differences explicit: site roles, endpoints, route scale, interfaces, HA, security, and policy bindings may differ.

Test a template with valid minimum/maximum and invalid inputs, two site types, idempotent reapplication, an upgrade, and a rollback. Use canary sites and diff/review. Template success does not prove every device accepted or every traffic path works.

### 2.4 Tune dynamic and static routing

For each supported protocol or static route, define neighbors/next hops, authentication, timers, prefixes, metrics/attributes, filters, redistribution, summarization, defaults, failover, and maximum scale. Tune only from measured convergence, stability, provider/device behavior, and application requirements. Fast timers can increase churn/CPU or produce false failures.

Troubleshoot neighbor/session state, received/advertised routes, best path, installed forwarding, reachability/ARP, policy, NAT, overlay/path status, and return traffic. Prevent leaks and loops with exact filters and tagging/community/metric strategy as supported. Test route withdrawal, peer loss, default loss, and recovery.

### 2.5 Implement VRFs for segmentation

A VRF creates a separate routing context. Define tenant/function, interfaces, route tables/protocols, overlapping-address needs, direct internet/service access, shared services, route leaking, policy/NAT, monitoring, capacity, and ownership. Segmentation is effective only when unauthorized inter-VRF paths are absent or explicitly denied at the enforcement point.

Test same-prefix cases, allowed shared service, forbidden cross-segment route/flow, failover, management/telemetry, and troubleshooting visibility. Document where identity and security policy are applied after route leaking or service chaining.

## 3. Operations and monitoring — 18%

### 3.1 Device-level statistics

Monitor device/controller state, software, CPU/memory/storage as available, interfaces/errors/drops, circuits/capacity/utilization, paths/overlays, routing, flows/applications, QoS, latency/jitter/loss, probes/LQM, HA, alarms, and time. Establish expected population and baselines by model/site/circuit/application; a single green status or average can hide tail loss and local outages.

Correlate time ranges and event time. Compare client/application evidence with ION and provider evidence. Retain enough history for trends and incidents, respecting entitlement, privacy, and cost.

### 3.2 Controller incidents, alerts, statistics, and audit logs

Statistics are measured time-series evidence; alerts signal conditions; incidents organize sustained/correlated operational issues under product logic; audit logs record administrative/configuration activity. Names and lifecycle fields vary by release. For each, understand source, trigger, severity, timestamps, affected entity, evidence, state, owner, notification, retention, and closure criteria.

Correlate a degradation with device/path statistics, flow/application data, routing, provider events, and audit changes. Closing an incident does not remediate the cause. Export/integrate events only with stable schema, authentication, deduplication, time, owner, and failure monitoring.

### 3.3 Alerts and notifications

Define conditions/severity, scope, suppression/deduplication, recipients/integration, schedule/escalation, runbook, acknowledgement, and recovery notification. Route actionable symptoms to the team able to act. Test delivery, unavailable integration, duplicate storms, maintenance suppression, and all-clear behavior.

Avoid static thresholds that ignore site size or expected pattern. Pair service-impact alerts with data-health alerts so telemetry silence is not interpreted as healthy service.

### 3.4 WAN Clarity reports

Current documentation describes weekly WAN Clarity packages/views covering traffic distribution, circuit utilization/percentiles, hotspots, top applications/clients/servers/pairs/domains, branches, and aggregate bandwidth, depending on license and scope. Use them for capacity, path/QoS adjustment, and usage investigation. Their utility depends on accurate configured circuit capacity and overlay/data coverage.

Record scope, period/time zone, direction, percentile/aggregation, included paths/sites, missing data, baseline, and action. Reconcile a surprising report with raw/device statistics before changing policy. A weekly aggregate can conceal short application-impacting bursts.

### 3.5 Network-monitoring tools

Integrate approved syslog/API/SNMP or other currently supported outputs with secure transport, least privilege, stable identifiers, time sync, schema/units, polling/rate limits, retention, and health monitoring. Preserve site/device/circuit/path/application dimensions. Build drill-down from enterprise view to raw evidence.

Test data presence, delay, duplication, counter reset/wrap, unit conversion, partial outage, credential rotation, and version change. External tools supplement—not replace—controller/device diagnostics.

### 3.6 SASE-related events

Monitor SD-WAN device/path and Prisma Access/service connectivity, onboarding/integration state, policy/identity propagation, tunnel/service-link state, application experience, security events, licensing, and audit changes according to deployed architecture. Establish ownership across network, security, identity, endpoint, and cloud teams.

Use correlation IDs, tenant/site/device/user/app/time, policy revision, and path when tracing an event. Determine whether the failure is branch forwarding, underlay, overlay, integration, cloud security, identity, application, or telemetry before remediation.

## 4. Unified SASE — 14%

### 4.1 Prisma Access integration and Security policy

Prisma SD-WAN can connect branches to Prisma Access through current supported onboarding/integration methods. Design tenant association, sites, service connections/locations, tunnels/paths, routes, NAT, identity, certificates/keys, security policy, logging, HA, capacity, and failure/alternate behavior. Clearly locate path policy versus cloud security policy responsibilities.

Validate controller/integration state, route exchange, tunnel/path health, user/application identification, policy match, security logs, egress identity/IP, DNS, direct-versus-inspected cases, and loss of a service path. Do not assume that an up tunnel proves inspection.

### 4.2 ADEM application-performance monitoring

Autonomous Digital Experience Management measures supported user/application/network/service-path experience through deployed telemetry and tests. Define monitored applications, user/site population, test targets/frequency, success and latency thresholds, baselines, ownership, privacy, and remediation workflow. Entitlement and architecture determine available capabilities.

Correlate ADEM symptoms with endpoint/Wi-Fi/LAN/ION/underlay/Prisma Access/internet/SaaS layers. Synthetic success does not guarantee every real transaction; passive/user evidence and application telemetry add context.

### 4.3 Device-ID for IoT connectivity

Device-ID supplies supported device classification/context that policy can use. Establish discovery/telemetry sources, confidence/freshness, categories, unknown-device behavior, spoofing risk, privacy, policy mapping, and response. Treat identity as evidence, not an immutable fact.

Build least-privilege policy for known classes and a safe quarantine/onboarding path for unknown or low-confidence devices. Test new, reclassified, stale, offline, shared-NAT, and spoofed cases. Verify actual rule/path/security outcome and logs.

### 4.4 Cloud Identity Engine integration

CIE maps directory identities/groups for supported SASE use. Current Prisma SD-WAN documentation shows user-to-IP context learned through supported User-ID integration and user-to-group mapping through CIE for compatible tenants. Define directory source/scope, tenant association, formats, filters, sync/freshness, privileges, privacy, conflicts, and outage behavior.

Test group addition/removal, user address change, duplicate/format mismatch, stale mapping, source outage, and policy propagation. The controller knowing a group is not proof that the current flow has correct user context.

### 4.5 User/group-based path and Security policy

User/group match can refine path, QoS, and security outcomes where supported. Specificity/precedence and unknown-user handling matter. Combine identity only with required application, network, destination, and context constraints. Define safe defaults if mapping is absent or stale.

Validate an explicit user, group member, nonmember, unknown user, IP reassignment, group change, and identity-source failure. Logs must expose the resolved identity/group and matched policy revision. Avoid routing privileged traffic differently solely on an uncorroborated IP mapping.

> **Related item:** Identity-aware networking creates a joined system. Directory health, mapping age, IP reuse, tenant format, and propagation latency become forwarding/security dependencies.

## 5. Troubleshooting — 20%

### 5.1 Connectivity between sites

Define the failing source/destination/application/time and compare with a known-good flow. Check LAN/interface/VLAN/ARP, addressing, ION/device/HA, circuits/underlay, controller, overlays/tunnels, site/DC/service groups, routes, VRF, path/security/NAT, application classification, MTU/DNS, and return path. Use flow records, counters, routes, path state, incidents, captures or safe probes as supported.

Change one variable and preserve evidence. “Ping fails” is not sufficient because ICMP may be treated differently from the application; “ping succeeds” does not prove DNS, TCP/TLS, application, policy, or performance.

### 5.2 Routing and forwarding

Separate neighbor formation, route reception, policy/filter/redistribution, best-route selection, route installation, next-hop resolution, VRF, flow classification, path-policy filtering, performance/reachability filters, NAT/security/QoS, and return route. Check overlapping prefixes, defaults, summarization, asymmetric routes, stale sessions, and recent audit changes.

Predict the expected decision before reading the result. Current flow-selection documentation describes multiple stages; use release-specific diagnostics because policy and algorithm details can change.

### 5.3 Application performance

Quantify symptom and affected population, time, transaction, baseline, latency, jitter, loss, throughput, retransmission, DNS, TLS, server time, and application SLA. Compare client/LAN, ION queues, circuit utilization/errors, path LQM/probes, carrier, Prisma Access, internet/SaaS, and server. Check application classification, QoS, path and performance policies, MTU, NAT, route changes, and capacity under failure.

Do not automatically move flows: all alternatives may be degraded, duplication/FEC has overhead, and the server may be slow. Test an action and validate user outcome plus unintended congestion.

### 5.4 Policy issues

Identify effective site binding, stack/set and rule order, enabled state, match fields, application discovery, network context, prefixes, user/group, path availability, SLA, default/fallback, security/NAT/QoS interaction, version, and audit change. Reproduce with a unique flow and inspect the actual matched decision.

Beware shadowed/general rules, empty criteria interpreted broadly, stale identity, wrong circuit labels, template overrides, and path excluded by reachability/performance. Roll back or make the smallest reviewed change, then test intended and denied traffic.

### 5.5 Data analysis with the copilot

The blueprint names “co-pilot” without defining an exam-stable UI/answer contract. Treat any tenant-provided AI assistant as an investigative accelerator. Provide scoped questions and verify its interpretation, time range, entities, query/data sources, calculations, cited evidence, permissions, and proposed actions in authoritative telemetry/configuration. Do not send secrets or regulated data outside approved controls.

AI output can be incomplete, stale, hallucinated, or overconfident. Preserve the prompt/context and evidence used for a consequential decision. Never allow an unverified narrative or generated remediation to replace change approval.

### 5.6 Analytics optimization and reporting

Start with a question and baseline; segment by site/circuit/path/application/user/time; find trend/outlier/correlation; validate data completeness and raw samples; form a hypothesis; pilot a routing/capacity/policy change; compare before/after; watch regressions; document/revert if needed. Correlation does not establish root cause.

Reports need audience, decision, metric definition, units, denominator, percentile/aggregation, scope/time zone, exclusions, freshness, missing-data flag, threshold, owner, and drill-down. Optimization is continuous because applications, circuits, users, releases, and business priorities change.

> **Related item:** A path change that improves median latency but harms voice-tail loss or consumes expensive metered capacity is not a complete optimization. Define multiple success and guardrail metrics first.

## Integrated scenarios

### Dual-circuit branch rollout

Baseline applications and circuits, choose ION/capacity/license, define Control-mode insertion and bypass, route/DC endpoints, path/QoS/performance/security/NAT policy, HA, templates, alerts, and acceptance tests. Pilot, fail each circuit and ION, confirm prioritized service and reporting, then expand in rings.

### Identity-aware branch to Prisma Access

Integrate CIE/User-ID and Prisma Access, then bind narrowly scoped user/group application policy. Test member/nonmember/unknown, mapping expiry and IP reuse, service-path loss, cloud security match/logging, application experience, and safe default. Distinguish identity failure from branch or cloud forwarding failure.

### Intermittent voice impairment

Establish affected sites/users/time and voice SLA; inspect classification, QoS queue/drop, LQM/probe latency/jitter/loss, bandwidth/hotspots, path/performance rule, routing and provider evidence. Pilot a threshold/path/QoS adjustment with raise/clear hysteresis and compare voice-tail metrics plus other application/cost guardrails.

## Hands-on labs

1. **Assessment and selection:** inventory three fictional sites and map application/SLA, topology, circuits, capacity, HA, security, licensing, and current supported ION choice with assumptions.
2. **Bandwidth failure model:** create hourly demand and circuit data, calculate normal/degraded headroom, define QoS and metered constraints, then test one common-mode failure.
3. **Policy workbook:** design ordered path, QoS, performance, security, and NAT policies for voice/SaaS/bulk/admin traffic; predict live decisions and test defaults.
4. **Pilot deployment:** onboard or model a branch and data-center site using templates/site variables; verify controller/device, routes, paths, flows, policy, logs, rollback, and site-specific drift.
5. **Routing and VRF:** implement or simulate dynamic/static routing, filters/redistribution, failure tuning, two VRFs, one allowed shared service, and explicit cross-segment denial.
6. **Monitoring pipeline:** generate a unique degradation/change, trace device statistics, controller alert/incident, audit log, notification, external tool, and recovery; measure delay and missing-data behavior.
7. **WAN Clarity review:** annotate a synthetic report with scope, utilization math, top contributors and caveats; propose capacity/path/QoS changes and validation metrics.
8. **Unified SASE:** diagram and, where entitled, test Prisma Access, ADEM, Device-ID, and CIE paths; include user/group/unknown and integration-failure cases.
9. **Connectivity fault set:** inject a LAN, underlay, overlay, route, VRF, policy, NAT, and return-path fault one at a time; isolate each from evidence before repair.
10. **Performance investigation:** degrade one path, measure app and network layers, validate classification/QoS/SLA, test alternate action, and compare user/cost/other-app guardrails.
11. **Copilot verification:** ask an available assistant to analyze synthetic telemetry; inventory every claim/source/time/filter, independently verify, and reject one unsupported remediation.
12. **Optimization report:** produce a one-page decision report with defined metrics/denominator/percentile, baseline, hypothesis, canary, before/after, regression guardrails, and rollback.

## Original readiness checks

1. Which inputs drive ION device selection?
2. How do Analytics and Control modes differ?
3. Why size bandwidth for degraded operation?
4. Why must configured circuit capacity be accurate?
5. What can make two providers one failure domain?
6. What belongs in a license-entitlement record?
7. Which evidence should an existing-network assessment preserve?
8. What makes an application requirement testable?
9. Which controls prevent DCI route leaks and loops?
10. What proves a branch is accepted after activation?
11. Where can security enforcement occur in a SASE design?
12. How do dataplane survivability and controller availability differ?
13. How do path and performance policies differ?
14. Why can QoS not fix every congestion problem?
15. What changes downstream when NAT rewrites an address?
16. Why can an aggressive SLA flap traffic?
17. What belongs in an activation runbook?
18. How should site-specific values differ from standards?
19. What makes a template production-safe?
20. Why should routing timers not simply be minimized?
21. What proves VRF segmentation?
22. Which device statistics need a baseline?
23. How do incidents, alerts, statistics, and audit logs differ?
24. What makes a notification actionable?
25. What can WAN Clarity aggregates hide?
26. Why must an external monitoring integration monitor itself?
27. What dimensions correlate a SASE-related event?
28. What proves traffic is actually inspected by Prisma Access?
29. What are the limits of an ADEM synthetic test?
30. Why is Device-ID context not immutable truth?
31. How do User-ID and CIE contribute different identity context?
32. What should happen when user mapping is unknown or stale?
33. Why do both failed and successful ping provide incomplete evidence?
34. Which stages separate a routing route from a forwarded application flow?
35. Which layers must be checked for slow SaaS?
36. Why can moving a flow worsen service?
37. Which mistakes commonly cause policy mismatch?
38. How should copilot output be verified?
39. What makes an analytics optimization controlled?
40. Which metadata makes a report decision-ready?

## Answers and reasoning

1. Site role/mode/topology, interfaces/circuits, capacity/session/application needs, HA/environment, routing/VRF/services, lifecycle and current support.
2. Analytics observes without path/policy control; Control forwards and applies path, security, and QoS behavior.
3. A failed link concentrates traffic; critical applications need enough remaining capacity and deliberate prioritization.
4. Utilization, policy, capacity planning, and reporting depend on that denominator.
5. Shared last mile, provider core, conduit, power, building entry, cloud edge, or administrative dependency.
6. Site/device, capacity/tier/features, tenant/region, term/expiry, owner, renewal, limit/expiry behavior and source.
7. Diagrams, addressing/routes/NAT, circuits, apps/flows/SLA, performance, policy/security/identity, monitoring, ownership, failures and dependencies.
8. Named population/flow, measurable latency/loss/availability/capacity/security outcome, test method, failure case and owner.
9. Exact advertisements/filters, summarization, tags/attributes/metrics, default handling, topology, route validation and failure tests.
10. Correct onboarding/site/software/interfaces/routes/paths, application decisions, policy/security/logs, failures and rollback evidenced end to end.
11. On the ION/security policy, Prisma Access, or another firewall/control according to the flow; document one accountable control path.
12. Existing forwarding may continue during some controller outage while management, policy changes, visibility or analytics are impaired.
13. Path policy constrains/preferences eligible paths; performance policy measures SLA and triggers supported actions when conditions occur.
14. It prioritizes constrained capacity but cannot create bandwidth or repair loss/latency/server problems.
15. Logs, routing lookup, policy identity, return path, downstream attribution, and overlapping-address handling may change.
16. Noise and threshold crossings can repeatedly move flows; use baseline, sampling, hysteresis, alternates and tests.
17. Access/subscriptions, device/site identity, configuration, cabling/bypass, dependencies, maintenance, acceptance, communications and rollback.
18. Classify inputs as global, site-class, or unique; validate and govern exceptions instead of cloning configuration.
19. Defined scope/parameters/constraints/version/dependencies, invalid-input tests, diffs/review, canary, effective-state validation and rollback.
20. Very fast timers can create false failure, churn and load; tune to evidence and peer/application requirements.
21. Separate routes/interfaces plus an allowed shared-service test and denied cross-segment route/flow, including failure paths.
22. Health/resource, interface/error/drop, circuit/utilization, path/overlay, route, flow/app, QoS, SLA, HA and time evidence.
23. Statistics are measurements, alerts signal a condition, incidents organize an operational issue, and audit logs record changes/actions.
24. Correct scope/severity, owner, evidence, timely delivery, dedup/suppression, runbook/escalation and tested recovery notification.
25. Short bursts, tail performance, incomplete data, non-overlay traffic, local outliers and bad capacity settings.
26. Credentials, transport, schema, polling/rate, ingestion and time can fail silently.
27. Tenant, site/device, user/application, path/service, policy revision, time/correlation ID and evidence across involved systems.
28. Route/tunnel state plus an identifiable flow matching cloud policy and producing expected security/log evidence and negative tests.
29. It covers configured target/path/population and can miss real transactions, endpoints, identity, or intermittent/tail conditions.
30. Classification depends on telemetry, confidence, freshness and spoofable/changing attributes.
31. Supported User-ID mechanisms associate user and IP; CIE supplies directory user/group mapping/context.
32. Apply an explicit safe default, alert/monitor freshness, and avoid privileged routing/security based on untrusted identity.
33. ICMP can take different policy/path; application DNS/TCP/TLS/server behavior can fail independently.
34. Neighbor/learn/filter/select/install/next-hop, VRF, flow/app classification, eligible path/performance, security/NAT/QoS and return path.
35. Client/Wi-Fi/LAN, ION queues/classification, path/circuit/provider, Prisma Access/internet, DNS/TLS and application/server.
36. Alternatives may also be degraded, overloaded, metered, higher latency or unable to preserve the session; FEC/duplication consumes capacity.
37. Wrong site binding/order/match/application/context/identity/labels, shadowing, defaults, unavailable path, stale template or interaction with another policy.
38. Check scope/time/entities, underlying query/data, calculation, sources, permissions and action in authoritative telemetry/configuration.
39. A defined baseline/hypothesis, data-quality check, canary, before/after metrics, guardrails, approval, monitoring and rollback.
40. Audience/decision, metric/units/denominator/aggregation, scope/time zone, exclusions, freshness/missing data, threshold/owner and drill-down.

## Readiness checklist

- [ ] I can select a current ION/device/mode and licensing approach from site, capacity, topology, HA, security, and lifecycle inputs.
- [ ] I can produce bandwidth plans for normal and degraded states with accurate capacities, QoS, growth, metering, and common-mode failures.
- [ ] I can assess an existing network and express application, DCI, branch, security, interconnection, and HA requirements as tests.
- [ ] I can design and explain path, security, QoS, performance, and NAT policy interactions, ordering, defaults, failure, and rollback.
- [ ] I can onboard a pilot, manage site-specific values/templates, validate effective state, and expand in rings.
- [ ] I can tune and troubleshoot static/dynamic routing from neighbor through forwarding/return path without causing leaks or instability.
- [ ] I can implement VRFs and prove both approved shared service and denied cross-segment traffic.
- [ ] I can interpret device statistics, controller incidents/alerts/audit logs, notifications, WAN Clarity, and external monitoring with data-health caveats.
- [ ] I can trace SASE events across branch, underlay/overlay, integration, Prisma Access, identity, application, and telemetry ownership.
- [ ] I can integrate and validate Prisma Access security, ADEM experience, Device-ID, CIE, and user/group policy including failure/default cases.
- [ ] I can isolate site connectivity, routing/forwarding, application performance, and policy faults with preserved evidence.
- [ ] I can independently verify copilot output and use analytics for controlled, measured, reversible optimization.
- [ ] I can answer all original checks and complete the labs with diagrams, configuration, test evidence, and rollback.
- [ ] I rechecked the live page, datasheet, handbook, Prisma SD-WAN/SASE release docs, tenant capabilities, and registration terms.

## Places to learn

This is a selective starting set, not a complete list and not a prescription to consume everything. Pick and choose the official documentation, structured training, demonstrations, and labs that close your gaps. Times are planning estimates unless the provider states a duration; access, licensing, versions, titles, and prices change.

- [Official certification page](https://www.paloaltonetworks.com/services/education/palo-alto-networks-sd-wan-engineer) and [August 2025 datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/sd-wan-engineer-datasheet.pdf) — **45–75 minutes** to annotate; public; canonical scope.
- [Palo Alto Networks Certification Handbook](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/ebooks/panw-certification-handbook.pdf) — **30–45 minutes**; public; verify current delivery, score, retakes, validity/renewal, accommodations, and program rules.
- [Official Palo Alto Networks digital learning](https://learn.paloaltonetworks.com/learn) — locate the **SD-WAN Engineer** learning path; **estimate 15–30 hours** depending on experience; login may be required and the public certification link currently resolves to the learning portal rather than a stable deep link.
- Official instructor-led **Prisma SD-WAN: Design and Operation** — **estimate 3–5 training days plus labs**; commercial/authorized training; explicitly recommended on the certification page, but schedules and exact duration vary.
- [Prisma SD-WAN documentation](https://docs.paloaltonetworks.com/prisma-sd-wan) — **25–45 hours targeted reading and lab repetition**; public; canonical product study source; select the current ION/controller release and cover onboarding, deployment, policy, routing, VRF, monitoring, incidents, and release notes.
- [Prisma SD-WAN Administrator’s Guide](https://docs.paloaltonetworks.com/prisma-sd-wan/administration) — **12–25 hours targeted**; public; policy ordering/features and UI paths are release-sensitive.
- [WAN Clarity Reports](https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-clarity-reports) — **2–4 hours plus report review**; public documentation, but report access requires relevant tenant/license.
- [Prisma SASE documentation](https://docs.paloaltonetworks.com/sase) and [Prisma Access documentation](https://docs.paloaltonetworks.com/prisma-access) — **8–15 hours targeted**; public; hands-on access/entitlements may be required.
- [ADEM documentation](https://docs.paloaltonetworks.com/autonomous-dem) and [Cloud Identity Engine overview](https://docs.paloaltonetworks.com/identity/cloud-identity-engine/cloud-identity-engine-overview) — **5–10 hours targeted**; public; validate current license, tenant, data, and deployment prerequisites.
- [Palo Alto Networks LIVEcommunity](https://live.paloaltonetworks.com/) and [official YouTube channel](https://www.youtube.com/@PaloAltoNetworks) — **4–10 hours selected SD-WAN/SASE troubleshooting and release sessions**; public; corroborate community/older media with current docs.
- Vendor/partner lab, evaluation tenant, or authorized proof of concept — **20–40 hours**; access varies and partner login/entitlement may be required; practice end-to-end deployment, failures, integrations, and reports without production impact.
- Adjacent O’Reilly, Pluralsight, Udemy, or other SD-WAN/SASE networking courses — **6–20 hours selected**; subscription/purchase may be required; useful for routing, QoS, SD-WAN, and SASE foundations, but no current course specifically aligned to this Palo Alto Networks credential was verified September 2, 2026. Map every module to the official blueprint and current product docs.
- Practice questions, if used — **2–4 hours per timed set plus review**; no current official, MeasureUp, or Whizlabs credential-specific practice product was verified September 2, 2026. Use only authorized, explanation-rich questions; avoid dumps and treat results as one signal, not proof of readiness.
