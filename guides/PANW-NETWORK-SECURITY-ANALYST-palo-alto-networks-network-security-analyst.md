---
exam_code: PANW-NETWORK-SECURITY-ANALYST
vendor_id: palo-alto-networks
official_blueprint: https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/netsec-analyst-datasheet.pdf
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Palo Alto Networks Certified Network Security Analyst Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live certification page, August 2025 datasheet, July 2025 certification handbook, Strata Cloud Manager/PAN-OS documentation, and selected public learning sources were checked September 2, 2026. This does not guarantee that every explanation is error-free or remains current. The [official page](https://www.paloaltonetworks.com/services/education/palo-alto-networks-netsec-analyst) and [datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/netsec-analyst-datasheet.pdf) are authoritative.

**Current baseline:** object configuration 30%; policy creation 30%; management/operations 26%; troubleshooting 14%; August 2025 datasheet<br>
**Exam contract:** specialist-level English Pearson VUE certification. Under the checked handbook, all Palo Alto Networks certification exams use an 860 passing score on a 300–1000 scaled range and provisional results. The public datasheet does not state item count, base duration, price, or formal experience; verify live registration.<br>
**Platform boundary:** Strata Cloud Manager and Strata Logging Service are explicit. The role creates objects/policy, improves posture, handles incidents/alerts, and troubleshoots management/on-box/runtime/push/health issues. UI and supported products evolve; learn object-policy-operation relationships.<br>
**Validity and renewal:** two years under the July 2025 handbook, subject to current pathway rules.<br>
**Upcoming change:** no retirement or dated replacement was found September 2, 2026.<br>
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

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Start with the blueprint and page-linked official path, then choose current SCM/PAN-OS documentation and authorized labs for gaps. Record platform/version because interfaces and feature support change.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Network Security Analyst page](https://www.paloaltonetworks.com/services/education/palo-alto-networks-netsec-analyst) | Public | 10–15 minutes | Current credential, datasheet, learning path, registration |
| [August 2025 datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/netsec-analyst-datasheet.pdf) | Public PDF | 45–75 minutes | Canonical four-domain weighted objective map |
| [Certification Handbook](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/ebooks/panw-certification-handbook.pdf) | Public PDF | 30–45 minutes | Scoring, ESL, result, retake, validity, renewal, and integrity |
| [Official digital learning](https://learn.paloaltonetworks.com/learn) | Free account/login may be required | 30 minutes planning; modules vary | Follow the certification-page plan and record current duration/version |
| [Strata Cloud Manager documentation](https://docs.paloaltonetworks.com/strata-cloud-manager) | Public | 20–35 hours selected topics/labs | Folders/snippets, objects/policy, deployment, insights, optimizer, logs, incidents, health |
| [PAN-OS policy documentation](https://docs.paloaltonetworks.com/pan-os) | Public | 15–25 hours selected topics | Security/NAT/decryption/override/PBF/profiles/objects and packet/runtime behavior |
| [Security Policy Best Practices](https://docs.paloaltonetworks.com/best-practices/security-policy-best-practices) | Public | 5–10 hours | App-based migration, profiles, decryption, cleanup, and Policy Optimizer context |
| [Palo Alto Networks YouTube](https://www.youtube.com/@PaloAltoNetworks) | Free video | 4–10 hours selected current demos | SCM/Strata architecture and workflow visuals; verify current UI |
| [Pluralsight Palo Alto Firewalls for Network Protection](https://www.pluralsight.com/paths/palo-alto-firewalls-for-network-protection) | Paid; older path | About 4h05m listed core course plus labs | PAN-OS policy subset; not SCM-complete and may use older UI |
| [NDG PAN11 Firewall Essentials](https://www.netdevgroup.com/online/courses/cybersecurity/pan11-firewall-essentials) | Paid/institutional | 14 labs; plan 15–25 hours | Authorized firewall configuration practice; map older PCNSA alignment to this blueprint |

No current official practice exam, MeasureUp product, or Whizlabs product explicitly aligned to this exact Network Security Analyst blueprint was verified. Prefer current documentation and original change/troubleshooting labs over unsourced question banks.
