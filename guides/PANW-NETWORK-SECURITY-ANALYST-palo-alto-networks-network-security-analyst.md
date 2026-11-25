---
exam_code: PANW-NETWORK-SECURITY-ANALYST
vendor_id: palo-alto-networks
official_blueprint: https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/netsec-analyst-datasheet.pdf
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-10-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-10-28
---

# Palo Alto Networks Certified Network Security Analyst Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live certification page, August 2025 datasheet, July 2025 certification handbook, Strata Cloud Manager/PAN-OS documentation, and selected public learning sources were checked October 28, 2026. This does not guarantee that every explanation is error-free or remains current. The [official page](https://www.paloaltonetworks.com/services/education/palo-alto-networks-netsec-analyst) and [datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/netsec-analyst-datasheet.pdf) are authoritative.

**Current baseline:** object configuration 30%; policy creation 30%; management/operations 26%; troubleshooting 14%; August 2025 datasheet<br>
**Exam contract:** specialist-level English Pearson VUE certification. Under the checked handbook, all Palo Alto Networks certification exams use an 860 passing score on a 300–1000 scaled range and provisional results. The public datasheet does not state item count, base duration, price, or formal experience; verify live registration.<br>
**Platform boundary:** Strata Cloud Manager and Strata Logging Service are explicit. The role creates objects/policy, improves posture, handles incidents/alerts, and troubleshoots management/on-box/runtime/push/health issues. UI and supported products evolve; learn object-policy-operation relationships.<br>
**Validity and renewal:** two years under the July 2025 handbook, subject to current pathway rules.<br>
**Upcoming change:** no additional retirement or dated replacement was found as of October 28, 2026.<br>
**Integrity:** actual exam content is confidential. This guide uses the public blueprint, original checks, safe labs, and public documentation only.

## How to use this guide

Treat every configuration as an intent-to-evidence chain: object → policy reference → deployment target → commit/push → runtime session → log/alert → posture/tuning → rollback. A correctly saved object that is not referenced, pushed, licensed, supported, or receiving traffic has no enforcement outcome.

For each lab:

1. define traffic/application/user/device/data/path and desired allow/deny/inspect/log result;
2. place reusable objects and profiles in the correct folder/snippet/hierarchy;
3. predict rule match order, NAT/forwarding/decryption interactions, and inherited configuration;
4. validate locally and centrally, deploy to a canary, then test both success and failure;
5. correlate traffic/threat/system/config/incident/health evidence and document rollback.

> **About related items:** A `Related item:` callout adds architecture, operations, governance, implementation, or lifecycle context. It makes the objective useful in real work but does not imply the added wording appears in the official datasheet.

## Blueprint map

| Domain | Weight | Evidence of readiness |
|---|---:|---|
| 1. Object Configuration | 30% | Create reusable inspection/data/IoT/DoS/log/SD-WAN objects with correct dependencies |
| 2. Policy Creation | 30% | Order and validate Security/NAT/decryption/override/PBF/SD-WAN decisions for real flows |
| 3. Management and Operations | 26% | Govern SCM hierarchy/deployment/logging and remediate posture/alerts through evidence |
| 4. Troubleshooting | 14% | Isolate intent/config/deploy/runtime/health faults and prove root cause/fix |

## 1. Object configuration creation and application — 30%

### Security and decryption profiles

Security profiles inspect traffic already allowed by Security policy. Profile types can address threats, vulnerabilities/exploits, anti-spyware/C2, files/WildFire, URLs, data, and other current capabilities. A profile group attaches a consistent bundle. Verify subscriptions/content versions, action modes, exceptions, packet/decryption visibility, and logs. An Allow rule without profiles is not equivalent to inspected allow.

A decryption profile governs protocol/certificate/failure handling for traffic selected by decryption policy. Separate policy selection—who/what/where should be decrypted—from profile behavior—how supported/unsupported certificates/protocols are handled. Plan forward-trust/untrust certificates, inbound private keys, SSH, pinned/unsupported apps, no-decrypt exceptions, legal/privacy, capacity, and post-decrypt threat/data inspection.

### Dynamic and custom objects

External Dynamic Lists retrieve supported IP/domain/URL entries from a configured source so policy can change without a full object edit. Secure and monitor source authenticity/availability, formatting, refresh, size, last success, stale behavior, and false positives. EDLs are data inputs; the referencing policy determines action.

Custom URL categories group sites for policy/URL handling. Custom signatures identify application/threat patterns using protocol context and match rules; test precision, order/context, performance, and evasion. Data patterns identify sensitive content, with confidence/occurrence/context and false-positive implications. Custom objects need owner, source/rationale, version, test cases, scope, and expiry/review.

Log Forwarding profiles route selected logs/events to destinations or actions according to supported match lists/settings. Verify log generation, forwarding destination/connectivity/certificate, filtering, format/parsing, time, rate/queue, retention, privacy, and failure alerts. Do not conclude “no events” until collection health is proven.

Data Security profiles apply current data classification/control capabilities to supported traffic/channels. IoT Security profiles connect identified device/risk/context to policy and monitoring. DoS Protection profiles set classified/aggregate protection behavior and thresholds. Establish baselines and tune carefully; thresholds too low cause outages, too high fail to protect.

SD-WAN link/path profiles and templates define reusable connectivity and quality characteristics. Capture link type/bandwidth, path monitoring, SLA thresholds, fail/recovery timing, traffic distribution, NAT/zones, and target variables. Test brownout, not only hard link failure.

> **Related item:** Every reusable object needs ownership and lifecycle. Stale custom categories, EDLs, exceptions, and thresholds silently accumulate risk even when syntax remains valid.

## 2. Policy creation and application — 30%

### Security, NAT, and decryption

Security policy is top-down first match under applicable platform semantics. It combines source/destination zones/addresses, application, user/device, service, action, profiles, and logging. App-ID identifies the application; User-ID/Device-ID contribute entity context; Content-ID-related profiles inspect allowed content. Use application-default where appropriate and retain a logged cleanup rule.

NAT policy selects flows and translates source/destination addresses/ports as configured. Security policy and routing reason about original/translated fields at defined stages; learn the current packet-processing rules rather than guessing. Troubleshoot with original and translated tuples plus ingress/egress zones, route, and session.

Decryption policy selects traffic for forward proxy, inbound inspection, SSH proxy, or no-decrypt behavior. A no-decrypt exception still needs security policy and alternate endpoint/application visibility. Verify rule order, URL/category/user/device destination scope, certificates, profile, and post-decrypt inspection.

### Override, forwarding, and SD-WAN policy

Application Override assigns a custom application identity to matching traffic and bypasses normal App-ID classification for that flow; this can also bypass related content inspection expectations. Use only for validated exceptional applications with narrow match, owner, test, and review—not as a quick fix for unidentified traffic.

Policy Based Forwarding overrides normal routing for selected traffic to a next hop/path. It can create asymmetric routing, failed return traffic, tunnel/path monitoring issues, and bypassed controls. Define next-hop health and symmetric/return design. PBF changes path; it does not authorize traffic.

SD-WAN policy steers application traffic among links based on path/SLA characteristics and policy. SLA profiles define thresholds such as latency/jitter/loss under current capabilities. Test threshold breach, flap damping/recovery, preferred/fallback path, NAT/zones, session behavior, monitoring, and logs.

> **Related item:** Four policy sets can affect one flow—Security, NAT, decryption, and forwarding/SD-WAN. Draw their independent questions and processing stages before changing any one rule.

## 3. Management and operations — 26%

### SCM hierarchy and deployment

Strata Cloud Manager centrally manages supported Network Security/SASE configurations. Folders organize devices/deployments and inheritance. Snippets provide reusable configuration applied across targets. Variables parameterize values per environment/device. Automations invoke supported workflows/APIs. Model parent/child precedence, scope, references, variable resolution, target support, and who owns shared versus local configuration.

Saving configuration is not deploying it. Validate syntax/references, inspect candidate changes/diff, select correct targets, commit/push, observe job status, and verify device/runtime state. Use roles, approvals/locks where available, audit history, configuration versioning, backups, canaries, and rollback.

Strata Logging Service centralizes supported logs for search, analytics, reporting, alerts, and retention according to entitlement/configuration. Confirm ingestion sources, time, schema, tenant/region, privacy, retention, forwarding, query scope, and collection gaps.

### Posture, policy optimization, and incidents

Command Center summarizes security/operational posture across current capabilities. Activity Insights provides application/user/device/network activity context. Policy Optimizer uses observed application usage to help convert/tighten port-based or broad rules and identify unused applications/rules. Establish a representative observation period, business owner, dependencies, replacement plan, canary, and rollback; “unused” is not proof of safe deletion.

Log Viewer supports filtered investigation across relevant logs. Start with time zone/range, device/source, traffic tuple, rule, action, session, app/user/device, NAT, threat/content, and reason. Pivot into Incidents and Alerts to review correlated evidence, scope, severity, status, assignments, and remediation. Validate recommended actions against business context and authorization.

> **Related item:** A posture percentage is a prioritization signal. Preserve the underlying failed check, affected target, exception, compensating control, and verification evidence.

## 4. Troubleshooting — 14%

Use layers rather than random edits:

1. **Intent:** expected flow, policy owner, topology, change window, and success criteria.
2. **Management configuration:** scope/hierarchy, object references, variables, rule order, licensing/support.
3. **Commit/push:** validation message, job target/status, connectivity, version/plugin compatibility, locks, dependencies.
4. **Runtime:** DNS/routing/NAT/zones/session/App-ID/User-ID/Device-ID/decryption/profile/logging and return path.
5. **Device/service health:** CPU/memory/session/log capacity, interfaces/routes/tunnels, certificates, HA, content/software, telemetry, subscriptions.

A commit validates and activates candidate configuration on a target management/device context; a push distributes centrally managed changes to selected targets. Read the first causal error and affected path/object, not only the final job failure. Fix the source layer rather than editing a derived target that will be overwritten.

Misconfiguration can arise locally/on-box or centrally and from inheritance/variables. Compare intended versus effective configuration. Runtime failure despite successful deployment can be routing, zone, application identification, identity mapping, decryption, profile action, service health, certificate, or upstream/downstream behavior.

Device usage/health includes capacity, license/subscription, content/software, log collection, management connectivity, clock, interface, tunnel, HA, and resource pressure. Correlate onset with changes and scope across targets. Preserve evidence before restart/failover and validate recovery after rollback/fix.

## Integrated scenarios

### SaaS data-control rollout

Create URL/custom data objects, Security/decryption/data profiles, Log Forwarding, and a policy in the correct folder/snippet. Pilot users, validate decryption exceptions and SaaS traffic, inspect logs/alerts, tune false positives, and prove rollback without weakening unrelated traffic.

### Dual-link branch

Build SD-WAN profiles/templates/SLA and routing policy plus zones, NAT, Security, and logs. Parameterize two sites through variables. Test loss/latency brownout, hard failure, return path, session behavior, commit/push failure, and central/device health.

### Unknown IoT alert

Validate device identity and owner, observed behavior, IoT profile/policy, Security/profile/log evidence, and business/safety constraints. Use Log Viewer/Incidents, isolate only with approval, tune EDL/custom object if applicable, and record exception expiry.

## Hands-on labs

1. **Object dependency graph:** model every objective object, its policy reference, license/content/data prerequisite, target hierarchy, expected log, owner, and expiry.
2. **Security stack:** create an isolated allow policy with application/user/device context, profile group, logging, and explicit deny; test allowed, blocked, unknown, and identity-stale cases.
3. **Decryption design:** build a lab proxy/PKI and map policy/profile choices for normal, untrusted, expired, pinned, excluded, inbound, and SSH traffic.
4. **EDL/custom data:** host a signed/controlled test list, simulate refresh failure/stale values, use custom URL/data patterns, and prove policy/log effects without public blocking.
5. **Policy interaction:** trace original/translated tuple, route/PBF/SD-WAN path, Security, decryption, App-ID override, session, and return for five flows.
6. **SCM hierarchy:** model folders/snippets/variables/automation, validate effective configuration, simulate a failed push, deploy a canary, inspect audit, and roll back.
7. **Posture-to-remediation:** use synthetic Command Center/Activity/Policy Optimizer findings, validate owner/observation period, change policy, and verify logs/incidents.
8. **Troubleshooting game:** create one scope, reference, commit, routing, NAT, identity, certificate, content, logging, and health fault; isolate each with a written evidence tree.

## Original readiness checks

1. How does a Security profile differ from Security policy?
2. Why use a profile group?
3. How do decryption policy and profile differ?
4. What must be monitored for an EDL?
5. What risks accompany custom signatures/data patterns?
6. What proves Log Forwarding works end to end?
7. How should DoS thresholds be selected?
8. Which SD-WAN conditions belong in profiles/templates?
9. What roles do App-ID, User-ID, Device-ID, and Content-ID play?
10. Why is application-default useful?
11. How do Security and NAT policy differ?
12. Which tuple/context fields should be traced around NAT?
13. What remains required after no-decrypt?
14. Why is Application Override risky?
15. What does PBF change and not change?
16. How should SD-WAN brownout be tested?
17. What relationship connects folders, snippets, and variables?
18. Why is saved configuration not enforced configuration?
19. What belongs in commit/push validation?
20. What must be governed in Strata Logging Service?
21. How does Activity Insights differ from Policy Optimizer?
22. Why is an unused rule not automatically removable?
23. What should seed a Log Viewer query?
24. What context should be verified before alert remediation?
25. What are the five troubleshooting layers?
26. How do commit and push differ?
27. Why fix the source hierarchy rather than a derived target?
28. What can fail after a successful commit/push?
29. Which device-health areas should be correlated?
30. Why preserve evidence before restart/failover?
31. Which objective families combine in the SaaS scenario?
32. Which policies combine in the branch scenario?
33. Why must IoT identity be verified before isolation?
34. Which two domains each carry 30%?
35. What does scaled 860 not mean?
36. Why are count/base duration/price absent here?
37. How long is the credential valid under the checked handbook?
38. What should every custom object have beyond syntax?
39. Why must UI locations not be memorized as the core skill?
40. What must you recheck before scheduling?

## Answer key

1. Inspection/actions for already allowed traffic versus flow authorization/match.
2. Consistent reusable attachment of a defined inspection bundle.
3. Select which traffic/decryption mode versus govern protocol/certificate/failure behavior.
4. Source trust/reachability, format/size, refresh/last success, stale behavior, errors, and false positives.
5. False positives/negatives, performance, evasion, scope, ownership, versioning, and expiration.
6. Generated event, correct match, successful transport/trust, destination ingestion/parsing/time, and visible alert/query.
7. From representative baseline/capacity and safe tests with owner, action, exceptions, and monitoring.
8. Link attributes, SLA latency/jitter/loss, monitoring, fail/recovery, path preference, NAT/zones, and targets.
9. Application, user/group, device, and content/threat context.
10. It constrains an allowed application to its expected standard service behavior where appropriate.
11. Authorization/inspection versus address/port translation.
12. Ingress/egress zones, original/translated source/destination/ports, route, rule, app, and return path.
13. Security authorization plus alternative endpoint/application controls and logging.
14. It forces identification and can bypass normal App-ID/content inspection expectations.
15. Forwarding path/next hop; it does not authorize traffic.
16. Introduce threshold-crossing loss/latency/jitter and verify failover, recovery, flapping, sessions, logs.
17. Hierarchical target grouping, reusable config, and target-specific parameter values with defined precedence.
18. It must validate, target, deploy successfully, become effective, and process test traffic.
19. Diff, references/variables, target, compatibility/license, job, effective config, traffic/log result, rollback.
20. Sources, schema/time, tenant/region, access/privacy, retention/cost, forwarding/query, and collection health.
21. Observed activity context versus policy-use analysis and tightening recommendations.
22. Observation may miss seasonal/DR/rare critical use; validate ownership/dependencies first.
23. Time, source/device, flow tuple/session/rule/action and relevant app/user/device/threat context.
24. Raw evidence, scope, affected asset/user, confidence, business impact, authority, and reversibility.
25. Intent, management configuration, deploy job, runtime packet/session, and device/service health.
26. Activate a candidate in its target context versus distribute central configuration to managed targets.
27. A central redeploy can overwrite the local change and preserve the actual defect.
28. DNS/routing/NAT/zones, session, app/identity, decryption/profile, certificate, service/return path, or logs.
29. Resources/capacity, interfaces/routes/tunnels, HA, management/log connectivity, licenses/content/software, certificates/time.
30. Restart/failover may destroy volatile state and hide root cause.
31. URL/data/log objects, Security/decryption/data policy/profiles, hierarchy, logs/alerts, tuning/rollback.
32. SD-WAN/SLA, routing/PBF as applicable, zones, NAT, Security, and logging.
33. Misclassification and safety/business impact can make containment harmful.
34. Object Configuration and Policy Creation/Application.
35. It is not 86% raw correct; scaling accounts for exam forms.
36. Current public datasheet/handbook omit them; live registration is authoritative.
37. Two years, subject to current recertification rules.
38. Owner, purpose/source, scope, dependencies, tests, version, review/expiry, and rollback.
39. Surfaces change; relationships, dependencies, outcomes, validation, and troubleshooting remain durable.
40. Active datasheet, current SCM/PAN-OS docs/path, registration, handbook, supported versions/licenses, and policies.

## Final readiness checklist

- [ ] I can create/apply every named profile/object and prove its policy, dependency, target, log, and lifecycle.
- [ ] I can trace Security, NAT, decryption, Application Override, PBF, and SD-WAN decisions for one flow.
- [ ] I understand App/User/Device/Content context and the impact of stale or forced identification.
- [ ] I can organize folders/snippets/variables/automation without unclear central/local ownership.
- [ ] I validate commit/push, effective configuration, runtime traffic, logs, incidents, and rollback.
- [ ] I use Command Center, Activity Insights, Policy Optimizer, and Log Viewer for evidence-led improvement.
- [ ] I troubleshoot intent, configuration, deployment, runtime, and health systematically.
- [ ] I completed all scenarios/labs with an authorized canary and explicit failure cases.
- [ ] I reject leaked questions and do not test against assets I do not own.
- [ ] I rechecked the August 2025 datasheet, current docs/path, handbook, and registration before purchase.

## Key terms and phrases

**Object configuration creation and application**

| Term or phrase | Meaning |
|---|---|
| [Security profile](#security-and-decryption-profiles) | Threat-inspection settings attached to a security policy rule that allows traffic. An Antivirus profile can scan downloads that the rule permits. |
| [Decryption profile](#security-and-decryption-profiles) | Settings governing how the firewall handles encrypted sessions selected by a decryption rule. |
| [Advanced WildFire](#security-and-decryption-profiles) | A Palo Alto Networks malware analysis service that can examine submitted files and supply verdicts to participating controls. |
| [Packet](#security-and-decryption-profiles) | A network-layer unit carrying a source and destination IP address. Routers use the destination and their forwarding tables to send it onward. |
| [Vulnerability](#security-and-decryption-profiles) | A weakness in design, configuration, process or implementation that can affect a security objective under applicable conditions. |
| [Security profile group](#security-and-decryption-profiles) | A collection of inspection profiles attached together to eligible Security policy rules so protection settings can be reused consistently. |
| [Dynamic address group](#dynamic-and-custom-objects) | An address group whose membership is selected by tags, allowing membership to change without editing every policy reference. |
| [External dynamic list](#dynamic-and-custom-objects) | An externally maintained list of values the firewall can use in policy, subject to retrieval and update health. |
| [Authenticity](#dynamic-and-custom-objects) | Confidence that an entity, message or artifact is what it claims to be, based on an appropriate means of verification. |
| [Availability](#dynamic-and-custom-objects) | Timely and reliable access to a resource by authorized users. A running server may still be unavailable to the business if a required dependency fails. |
| [Bandwidth](#dynamic-and-custom-objects) | The nominal data-carrying capacity of a link, usually expressed in bits per second. It does not by itself establish delay or delivered throughput. |
| [Data classification](#dynamic-and-custom-objects) | Assigning sensitivity categories to information so access and inspection policy can reflect its handling requirements. |
| [False positive](#dynamic-and-custom-objects) | An alert that classifies benign activity as a target condition. Repeated benign alerts can distort operational priorities. |
| [Log forwarding](#dynamic-and-custom-objects) | Sending selected logs to other systems under configured match and destination rules. A local log and a successfully received remote record are separate observations. |
| [Parsing](#dynamic-and-custom-objects) | Extracting structured values from an incoming record. Correct parsing must preserve the distinction between a missing value and a value of zero. |
| [Retention](#dynamic-and-custom-objects) | The period for which telemetry remains available for investigation. A search outside that period cannot establish inactivity. |

**Policy creation and application**

| Term or phrase | Meaning |
|---|---|
| [Network address translation (NAT)](#security-nat-and-decryption) | Rewriting source or destination addressing for a connection. A translation rule alone does not grant permission to pass traffic. |
| [Decryption policy](#security-nat-and-decryption) | Rules that decide which encrypted flows receive TLS inspection and which are excluded. |
| [Application identification (App-ID)](#security-nat-and-decryption) | Palo Alto Networks application identification, which classifies traffic using attributes beyond the port number. |
| [Content-ID](#security-nat-and-decryption) | Content inspection capabilities used to evaluate allowed traffic for threats, files or sensitive data according to the enabled profiles. |
| [Device identification (Device-ID)](#security-nat-and-decryption) | Device classification and context used to make policy decisions about assets such as IoT endpoints. |
| [Entity](#security-nat-and-decryption) | An identifiable resource such as a user, workload or host whose activities and relationships can be investigated. |
| [Forward proxy](#security-nat-and-decryption) | An intermediary acting on behalf of a client for outbound connections, often to apply access policy or inspection. |
| [SSL Inbound Inspection](#security-nat-and-decryption) | Inspection of eligible encrypted traffic arriving at a protected server using the configured server-side certificate and key material. |
| [User identification (User-ID)](#security-nat-and-decryption) | A way to associate network traffic with user and group identity for policy and reporting. |
| [Policy-based forwarding](#override-forwarding-and-sd-wan-policy) | Selection of a forwarding path using configured match criteria in addition to ordinary destination routing. |
| [Application override](#override-forwarding-and-sd-wan-policy) | A policy mechanism that classifies matching traffic as a specified application under defined conditions. Its effect on inspection must be understood before use. |
| [Asymmetric routing](#override-forwarding-and-sd-wan-policy) | Forward and return traffic following different network paths. A stateful device may lose visibility of half the flow. |
| [Jitter](#override-forwarding-and-sd-wan-policy) | Variation in packet delay that can disrupt real-time applications even when average throughput looks adequate. |
| [Latency](#override-forwarding-and-sd-wan-policy) | Elapsed time for data or a request to travel a defined path. Specify whether the measure is one-way delay or round-trip time. |
| [Next hop](#override-forwarding-and-sd-wan-policy) | The adjacent router or forwarding destination selected for the next stage of a packet’s path. |
| [Software-defined WAN (SD-WAN)](#override-forwarding-and-sd-wan-policy) | A way to apply policy across WAN links, selecting paths according to traffic needs and measured link conditions. |

**Management and operations**

| Term or phrase | Meaning |
|---|---|
| [Configuration scope](#scm-hierarchy-and-deployment) | The set of devices or locations that receive a setting, including inherited settings and narrower overrides. |
| [Commit](#scm-hierarchy-and-deployment) | Validating and applying a candidate configuration on the relevant management system. Distributing a centrally managed change to devices is a separate step. |
| [Ingestion](#scm-hierarchy-and-deployment) | Bringing source records into the security platform for analysis. Missing input limits what a dashboard can show. |
| [Secure access service edge (SASE)](#scm-hierarchy-and-deployment) | An architecture that brings wide-area connectivity and cloud-delivered security together for distributed users and sites. |
| [Strata Cloud Manager (SCM)](#scm-hierarchy-and-deployment) | A cloud management platform for supported network security deployments, including configuration, monitoring and policy administration. |
| [Strata Logging Service](#scm-hierarchy-and-deployment) | A cloud service for storing and making security logs available to authorized management and investigation tools. |
| [Tenant](#scm-hierarchy-and-deployment) | An administrative or customer boundary in a shared service. Data, identities, configurations and actions must stay within the intended tenant. |
| [Policy optimization](#posture-policy-optimization-and-incidents) | Review of observed applications and rule usage to narrow or improve policy while preserving needed access. |
| [Authorization](#posture-policy-optimization-and-incidents) | Determining whether a given identity may perform a specific action on the particular resource requested. |
| [Incident](#posture-policy-optimization-and-incidents) | A case representing a security event or set of related events requiring coordinated investigation and response. |
| [Remediation](#posture-policy-optimization-and-incidents) | Action taken to remove or correct the cause of an incident after its immediate effects are contained. |
| [Severity](#posture-policy-optimization-and-incidents) | A rating of expected or observed impact. It differs from confidence, which expresses how strongly the evidence supports the assessment. |

**Troubleshooting**

| Term or phrase | Meaning |
|---|---|
| [Evidence preservation](#4-troubleshooting-14) | Maintaining the integrity and provenance of information needed for investigation, including original timestamps, collection method and access history. |
| [Telemetry](#4-troubleshooting-14) | Records of activity from endpoints, networks or other systems that investigators can correlate into a timeline. |

**Worked examples and practice**

| Term or phrase | Meaning |
|---|---|
| [Software as a service (SaaS)](#saas-data-control-rollout) | An application operated by a provider and consumed as a service. The customer still governs tenant settings, access and use of its data. |
| [Alert](#unknown-iot-alert) | A detection output identifying an event or pattern that warrants assessment. |

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Start with the blueprint and page-linked official path, then choose current SCM/PAN-OS documentation and authorized labs for gaps. Record platform/version because interfaces and feature support change.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Network Security Analyst page](https://www.paloaltonetworks.com/services/education/palo-alto-networks-netsec-analyst) | Public | 10–15 minutes | Current credential, datasheet, learning path, registration |
| [August 2025 datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/netsec-analyst-datasheet.pdf) | Public PDF | 45–75 minutes | Canonical four-domain weighted objective map |
| [Certification Handbook](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/ebooks/panw-certification-handbook.pdf) | Public PDF | 30–45 minutes | Scoring, ESL, result, retake, validity, renewal, and integrity |
| [Official digital learning](https://learn.paloaltonetworks.com/learn) | Free account/login may be required | 30 minutes planning; modules vary | Follow the certification-page plan and record current duration/version |
| [Strata Cloud Manager documentation](https://docs.paloaltonetworks.com/strata-cloud-manager) | Public | 20–35 hours selected topics/labs | Folders/snippets, objects/policy, deployment, insights, optimizer, logs, incidents, health |
| [Get Started with Strata Cloud Manager](https://docs.paloaltonetworks.com/strata-cloud-manager/navigation/get-started) | Public | 1–2 hours selected | Current folder scope, configuration, variables/snippets and push status; verify feature availability by managed product, service and license |
| [PAN-OS policy documentation](https://docs.paloaltonetworks.com/pan-os) | Public | 15–25 hours selected topics | Security/NAT/decryption/override/PBF/profiles/objects and packet/runtime behavior |
| [PAN-OS NAT rules](https://docs.paloaltonetworks.com/ngfw/networking/nat/nat-policy-rules), [decryption policy rules](https://docs.paloaltonetworks.com/network-security/decryption/administration/enabling-decryption/create-decryption-policy-rule), and [decryption profiles](https://docs.paloaltonetworks.com/network-security/decryption/administration/enabling-decryption/create-decryption-profile) | Public | 4–8 hours selected | First-match NAT behavior and current decryption setup; note version- and model-specific behavior |
| [Strata Cloud Manager: NGFW Management OLX announcement](https://live.paloaltonetworks.com/t5/news/introducing-palo-alto-networks-nbsp-on-demand-learning/ta-p/1252677) | Free according to Palo Alto Networks announcement; Learning Center access may vary | Course lessons/hours not inspected | Optional SCM orientation, not full Network Security Analyst coverage; public announcement inspected, course content was not |
| [Security Policy Best Practices](https://docs.paloaltonetworks.com/best-practices/security-policy-best-practices) | Public | 5–10 hours | App-based migration, profiles, decryption, cleanup, and Policy Optimizer context |
| [Palo Alto Networks YouTube](https://www.youtube.com/@PaloAltoNetworks) | Free video | 4–10 hours selected current demos | SCM/Strata architecture and workflow visuals; verify current UI |
| [Pluralsight Palo Alto Firewalls for Network Protection](https://www.pluralsight.com/paths/palo-alto-firewalls-for-network-protection) | Paid; older path | About 4h05m listed core course plus labs | PAN-OS policy subset; not SCM-complete and may use older UI |
| [NDG PAN11 Firewall Essentials](https://www.netdevgroup.com/online/courses/cybersecurity/pan11-firewall-essentials) | Paid/institutional | 14 labs; plan 15–25 hours | Authorized firewall configuration practice; map older PCNSA alignment to this blueprint |

No current official practice exam, MeasureUp product, or Whizlabs product explicitly aligned to this exact Network Security Analyst blueprint was verified. Prefer current documentation and original change/troubleshooting labs over unsourced question banks.
