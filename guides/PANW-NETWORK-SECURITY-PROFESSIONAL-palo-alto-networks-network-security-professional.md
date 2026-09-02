---
exam_code: PANW-NETWORK-SECURITY-PROFESSIONAL
vendor_id: palo-alto-networks
official_blueprint: https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/netsec-professional-datasheet.pdf
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Palo Alto Networks Certified Network Security Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live certification page, June 2026 datasheet, July 2025 certification handbook, official technical documentation, and selected public learning sources were checked September 2, 2026. This does not guarantee that every explanation is error-free or remains current. The [official certification page](https://www.paloaltonetworks.com/services/education/palo-alto-networks-netsec-professional) and [datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/netsec-professional-datasheet.pdf) are authoritative.

**Current baseline:** Fundamentals 17%; solution functionality 13%; platform solutions/services/tools 30%; maintenance/configuration 10%; infrastructure/CDSS 17%; connectivity/security 13%; June 2026 datasheet<br>
**Exam contract:** professional-level English Pearson VUE certification. Under the current handbook, all Palo Alto Networks certification exams use an 860 passing score on a 300–1000 scaled range and provisional results. The datasheet does not publish item count, base duration, or price; verify them in the live registration flow.<br>
**Experience boundary:** the target audience installs, deploys, operates, or administers the network-security portfolio. The exam requires basic configuration/maintenance knowledge across NGFW, SASE, management, and CDSS products—not merely definitions.<br>
**Validity and renewal:** two years under the July 2025 handbook, subject to current exam/higher-level same-track recertification rules.<br>
**Upcoming change:** no retirement or dated replacement was found September 2, 2026. This June 2026 blueprint includes newly volatile NGTS, quantum-security, and AI-security material; verify current docs during study.<br>
**Integrity:** actual exam content is confidential. This guide uses the public blueprint, original checks, isolated labs, and public documentation only.

## How to use this guide

Build a small network-security design and operate it through its lifecycle. Every objective should become a packet-flow diagram, configuration intent, dependency, validation query/log, failure condition, and rollback. Do not memorize menus: management surfaces and product packaging change.

For each change:

1. state the desired application/user/device/data outcome;
2. walk routing, NAT, policy, decryption, content inspection, and logging in order;
3. identify where configuration is authored and pushed—local, Panorama, or Strata Cloud Manager;
4. predict commit/deployment and traffic impact;
5. validate both permitted and denied paths, logs, HA/failure behavior, and rollback.

Use a licensed lab only when authorized. Vendor-free diagrams and packet/log exercises still teach the dependencies needed before product configuration.

> **About related items:** A `Related item:` callout adds architecture, operations, governance, implementation, or lifecycle context. It makes the published objective more useful in real work but does not imply that the extra wording appears in the official datasheet.

## Blueprint map

| Domain | Weight | Evidence of readiness |
|---|---:|---|
| 1. Network Security Fundamentals | 17% | Explain first/subsequent packet handling, App-ID, decryption choices, and layered identity/content policy |
| 2. NGFW and SASE Solution Functionality | 13% | Select PA/VM/CN/Cloud NGFW, Prisma SD-WAN/Access, Panorama, and SCM by use case |
| 3. Platform Solutions, Services, and Tools | 30% | Apply App/User/Device/Content context, CDSS, AIOps/BPA, NGTS, quantum, and AI risk controls |
| 4. Maintenance and Configuration | 10% | Plan safe policy/profile/content/software change and prove deployment health |
| 5. Infrastructure Management and CDSS | 17% | Operate subscriptions, IoT, data/SaaS, onboarding, reporting, and configuration at scale |
| 6. Connectivity and Security | 13% | Maintain hybrid and remote-user routing, segmentation, policy, certificates, and evidence |

## 1. Network Security Fundamentals — 17%

### Application inspection and session processing

Application-layer inspection identifies traffic from protocol behavior and signatures rather than trusting only ports. App-ID can use application signatures, protocol decoding, heuristics, and contextual identification; some applications begin as a parent/underlying protocol until enough traffic is observed. Security policy must accommodate identification safely without leaving broad permanent access.

The first packet of a new flow takes the slow path to establish session state and evaluate forwarding, NAT, policy, and inspection requirements. Eligible subsequent packets use a fast path based on established session information. A changed rule does not necessarily rewrite the state of an existing session immediately; understand session lifetime and when clearing or re-establishing is appropriate.

Walk a flow using ingress interface/zone, route and destination, NAT evaluation, Security policy, App-ID/User-ID/Device-ID context, profiles/CDSS inspection, egress, return traffic, and logs. The exact internal order and exceptions are release-specific; use [current packet-flow documentation](https://docs.paloaltonetworks.com/pan-os) for the target platform/version.

### Decryption

SSL Forward Proxy intermediates outbound client TLS so authorized traffic can be inspected. SSL Inbound Inspection decrypts traffic to a server when its certificate/private key and supported parameters are available. SSH Proxy enables policy/inspection controls for SSH according to platform capability. No Decrypt policy intentionally exempts selected traffic.

Design requires certificate trust and private-key protection, scope, legal/privacy review, unsupported/pinned application handling, cryptographic policy, performance sizing, failure behavior, exclusions, logging, and certificate lifecycle. Decrypting without attaching threat/data controls adds exposure without delivering the intended prevention benefit.

### Hardening through context

Zones establish policy boundaries. Zero Trust uses explicit verification, least privilege, and assume-breach decisions. User-ID maps activity to users/groups; Device-ID identifies/classifies devices for policy; App-ID identifies applications; Content-ID is the content/threat inspection layer. Treat mappings as evidence with freshness and confidence, not infallible identity.

Use application-default service where appropriate, security profiles/profile groups, log at session end and start only when needed, administrative least privilege, management-plane restrictions, configuration versioning, dynamic updates, and a cleanup rule with explicit action/logging. Validate unused/shadowed rules and exceptions.

> **Related item:** Application policy migration is an observation-and-tightening process. Replacing a broad port rule without measuring actual apps/dependencies can create an outage or a bypass.

## 2. NGFW and SASE solution functionality — 13%

### NGFW form factors

PA-Series is dedicated hardware for perimeter/core/branch/data-center use. VM-Series is a virtualized firewall for cloud/virtual environments. CN-Series integrates enforcement with container/Kubernetes architectures. Cloud NGFW offerings deliver managed cloud-integrated firewall capability. All enforce security outcomes, but routing insertion, scaling, HA/resilience, lifecycle, responsibility, telemetry, orchestration, and licensing differ.

For each form, design zones/segmentation, routing, Security and NAT policy, high availability or provider resilience, updates, management, logs, and failure modes. NAT changes addressing; Security policy authorizes traffic. One does not imply the other.

### Prisma SD-WAN and Prisma Access

Prisma SD-WAN uses application/path awareness and policy to steer WAN traffic, with NAT, zone-based firewall capability, monitoring, and logging. Separate transport availability/performance from security inspection. Prove brownout/failover behavior rather than only link-up state.

Prisma Access provides cloud-delivered security/connectivity for remote users and remote networks, with public/private application access, policy, NAT where applicable, monitoring, and logs. Remote user components include identity, client/proxy/browser access pattern, endpoint/device posture, gateway/service connection design, DNS, routes, certificates, authentication, and policy.

### Management planes

Panorama centrally manages supported firewall and related deployments through templates/template stacks, device groups, shared policy/objects, collectors/logging, and operational workflows. Strata Cloud Manager is a cloud-delivered management/operations surface across supported Strata/SASE capabilities. Scope and feature availability evolve; verify what each platform can manage for the target tenant/device/version.

Avoid configuration ownership conflicts. Define local versus inherited settings, hierarchy precedence, target devices, commit versus push/deploy behavior, validation, administrator roles, audit, configuration locks/workflow, and rollback.

> **Related item:** Central management increases consistency and blast radius. Stage changes, use scoped targets/canaries where supported, and preserve an out-of-band recovery path.

## 3. Platform solutions, services, and tools — 30%

### Security efficacy and CDSS

Security efficacy comes from combined application/user/device context, least-privilege policy, correct NAT/routing, decryption visibility, threat/data profiles, fresh content, and monitored outcomes. A subscription enabled without a profile/policy and traffic path may provide no protection.

Know the function and prerequisites of current CDSS-related capabilities:

- IoT Security discovers/classifies devices and risk/behavior using network telemetry and supports Device-ID policy;
- Enterprise DLP discovers/classifies and controls sensitive content across supported channels;
- SaaS Security discovers/governs sanctioned and unsanctioned SaaS using inline and/or API visibility depending on capability;
- PAN-OS SD-WAN selects paths for PAN-OS-managed branch connectivity;
- Premium GlobalProtect extends remote-access capability/support according to current packaging;
- Advanced WildFire analyzes suspicious files/content and distributes protections;
- Advanced Threat Prevention detects/blocks exploit, command-and-control, and other threat activity;
- Advanced URL Filtering classifies web destinations/content risk;
- Advanced DNS Security detects/prevents malicious DNS activity.

For each, state data source, inline/out-of-band position, action, update mechanism, privacy, licensing, logs, and failure behavior. Check current product docs rather than assuming an “Advanced” label means the same features across releases.

### AIOps and best practices

AIOps for NGFW analyzes telemetry and configuration against operational/security best practices and surfaces health/posture insights. Best Practice Assessment provides a baseline and prioritized remediation context. Use dashboards to find drift and risk, but validate relevance and operational impact before remediation. Track exception owner, justification, expiration, and compensating control.

A finding is not a deployed fix. Follow identify, scope, plan, test, approve, push, verify, and monitor. Measure reduced risky rules, stale objects, update gaps, capacity pressure, and recurrent deviations—not merely dashboard color.

### NGTS and quantum readiness

Next-Generation Trust Security is a 2026 certificate lifecycle management and private PKI capability integrated with Strata Cloud Manager. Its functions include certificate discovery/inventory, issuance/renewal/deployment workflows, multi-CA/private PKI support, policy/posture, and crypto-agility. It supports trust across firewalls, remote access, inspection, workloads, and enterprise systems; it is not an end-user authentication product label.

Quantum risk includes “harvest now, decrypt later”: adversaries retain encrypted traffic until future cryptanalysis becomes practical. Readiness requires cryptographic inventory, data lifetime/risk, algorithm and certificate dependencies, vendor/protocol support, crypto-agility, staged testing, and migration governance. Hybrid cryptography combines classical and post-quantum mechanisms during transition to reduce reliance on one new assumption; it also adds compatibility/performance/operational complexity.

### AI security

Separate securing AI use (employees accessing public/approved tools), securing AI applications (models, data, APIs, retrieval, agents/tools), and defending against AI-enabled threats. Risks include sensitive prompt/upload/output exposure, unsanctioned use, excessive permissions/agency, prompt injection, model/data/supply-chain issues, insecure APIs, and faster/socially convincing attacks.

Platform capabilities can discover AI use/assets, apply identity/access/data policy, inspect traffic, assess code/cloud/runtime posture, protect AI runtime interactions, and correlate/respond to threats. State visibility and enforcement boundaries. AI output and risk scores require evidence, monitoring, and human accountability.

> **Related item:** A certificate or AI inventory without owner, business purpose, renewal/remediation authority, and deletion trigger produces visibility—not governance.

## 4. NGFW and SASE maintenance/configuration — 10%

Security policy matches source/destination zones and addresses, user/device/application/service and other supported criteria, then applies an action and profiles/logging. NAT policy translates source/destination under its match rules. Security profiles apply threat/content controls to allowed traffic. Profile groups promote consistency.

Maintain hardware/VM/CN/Cloud NGFW and Prisma Access through configuration backups/versions, health/capacity monitoring, dynamic content updates, certificates/licenses, software upgrades, compatibility/dependency checks, staging, HA/resilience sequencing, commit validation, post-change verification, and rollback.

Content updates and software upgrades have different cadence/risk. Review release notes, preferred releases, known issues, plugin/manager compatibility, disk/capacity, bootstrap/orchestration, and downgrade constraints. In HA, validate state/config synchronization and failover before/after change. For cloud-managed services, understand the provider/customer boundary and scheduled/automatic components.

Policy tuning uses rule hit/app visibility, logs, Policy Optimizer/BPA where available, owner/business context, and a safe observation period. Remove broad/stale rules deliberately and test application dependencies.

## 5. Infrastructure management and CDSS — 17%

CDSS operation needs licensing/activation, supported platform/version, profiles/policy attachment, content/model updates, telemetry/connectivity, action mode, exceptions, logs, and health monitoring. A “licensed” dashboard does not show traffic is inspected; prove it with controlled test traffic and the expected log/action.

IoT Security depends on telemetry and classification. Map Device-ID to policy, device owner/type/risk/behavior, recommended access, and monitored deviations. Use passive methods first for OT/IoT and verify false classifications before enforcement.

Enterprise DLP and SaaS Security require data classification, access policy, encryption considerations, channel/tenant coverage, inline versus API behavior, incident workflow, privacy, and logs. Encryption at rest/in transit protects different states; access control determines who/what can use data; monitoring validates policy and investigation.

Onboard supported devices/products to Panorama or SCM with identity/serial/tenant association, licenses, connectivity, certificates/keys, software compatibility, templates/device groups/folders/snippets as applicable, and configuration ownership. Establish naming, hierarchy, admin roles, audit, reporting, log retention/forwarding, backup, and decommissioning.

> **Related item:** Decommissioning is part of management. Remove devices from policy targets, revoke certificates/tokens, preserve required logs, reclaim licensing, and eliminate stale objects/routes.

## 6. Connectivity and security — 13%

For on-premises, cloud, and hybrid networks, model underlay routing, overlay/tunnels, DNS, NAT, zones, segmentation, asymmetric paths, MTU, certificates, HA, policy, and monitoring. Cloud route tables/security constructs and provider-managed services coexist with Palo Alto Networks enforcement; assign responsibility explicitly.

Certificates support management, decryption, remote access, device/service identity, and trust. Track issuer/trust chain, subject names, key use, algorithms, private-key custody, expiration/renewal, revocation/status, deployment, and rollback. Automate carefully and validate from the relying endpoint after renewal.

Remote access can be client-based, proxy-based, enterprise-browser, or RBI-supported as the datasheet notes. Maintain identity/authentication, endpoint posture, route/access scope, app reachability, DNS, certificate trust, split/full tunnel or proxy behavior, segmentation, policy tuning, updates, logs, and user experience. Test revoked users, unmanaged endpoints, expired certificates, unavailable gateways, overlapping routes, and private-app failure.

Monitoring combines traffic, threat, URL/data, system/config, authentication, tunnel/path, and service-health logs. Synchronize time, preserve correlation identifiers, forward/retain safely, alert on collection gaps, and distinguish a denied packet from routing/DNS/certificate/application failure.

## Integrated scenarios

### Branch migration

Move a branch from legacy routing/firewall to Prisma SD-WAN plus centralized security. Inventory apps/users/devices, choose paths, design zones/NAT/Security policy/CDSS, integrate management/logging, migrate certificates, stage a canary, test link brownout and rollback, and prove access for public/private/SaaS traffic.

### Hybrid application publishing

Publish an on-prem/private-cloud application to remote users through Prisma Access. Walk DNS, identity, device state, certificate/TLS, decryption decision, route/service connection, zones, NAT, App-ID, User-ID/Device-ID, profiles, logs, and HA/failure behavior. Explain why a successful tunnel is not proof the app is safely reachable.

### Quantum/AI policy update

Use NGTS-style inventory to locate certificates/algorithms and plan one hybrid-cryptography pilot. Simultaneously map workforce AI traffic and an internal agent application. Apply access/data/runtime/network controls, stage policies, monitor false positives, and retain human approval for disruptive response.

## Hands-on labs

1. **Packet/session walk:** build an isolated routed/NAT path, capture first/subsequent packets, document session state, and map hypothetical App-ID/decryption/profile/log stages.
2. **Policy model:** author a vendor-neutral table for zones, apps, users, devices, services, actions, profiles, and logs; test allowed, denied, unidentified, and changed-application cases.
3. **Decryption PKI:** create a lab CA, outbound interception proxy, and inbound server test; observe trusted/untrusted/pinned/expired cases and document no-decrypt governance.
4. **Form-factor design:** choose PA/VM/CN/Cloud NGFW for four workloads and justify routing insertion, scaling, HA, management, responsibility, and evidence.
5. **SASE branch/remote lab:** simulate path steering and remote app access; test brownout, identity/device denial, DNS/route/certificate failures, and logging.
6. **CDSS validation matrix:** for each named service, record license/support, traffic/telemetry prerequisite, attached policy/profile, safe test, expected log/action, failure behavior, and owner.
7. **Management/change lab:** model Panorama/SCM hierarchy and device onboarding; stage an update/upgrade, validate dependencies, push to a canary, verify, roll back, and decommission.
8. **NGTS/AI readiness:** inventory lab certificates and AI data/flows, prioritize migration/data risks, apply one policy, and prove expiry/renewal or allow/block outcomes.

## Original readiness checks

1. Why is application-layer inspection more than port matching?
2. What broadly distinguishes slow-path and fast-path handling?
3. Why might an application identity evolve during a session?
4. Compare Forward Proxy, Inbound Inspection, SSH Proxy, and no-decrypt choices.
5. Which governance and operational concerns accompany decryption?
6. How do App-ID, User-ID, Device-ID, Content-ID, and zones contribute?
7. Why may existing sessions outlive a policy change?
8. Compare PA-Series, VM-Series, CN-Series, and Cloud NGFW.
9. How do Security and NAT policy differ?
10. What does Prisma SD-WAN optimize/control?
11. What does Prisma Access provide for users/networks/apps?
12. How do Panorama and SCM differ at a durable level?
13. Why does central management increase blast radius?
14. What proves a CDSS subscription is actually protecting traffic?
15. What are the distinct functions of IoT Security, DLP, and SaaS Security?
16. How do WildFire, Threat Prevention, URL Filtering, and DNS Security differ?
17. What does AIOps/BPA produce, and what does it not do automatically?
18. What durable functions belong to NGTS?
19. What is a harvest-now-decrypt-later risk?
20. Why use hybrid cryptography during transition?
21. Distinguish securing AI use, applications, and defending against AI threats.
22. What must accompany an AI-generated security conclusion?
23. How do software and content updates differ operationally?
24. What must be checked before an HA upgrade?
25. How should broad rules be tightened?
26. Why does IoT enforcement begin with classification validation?
27. How do inline and API SaaS/DLP controls differ?
28. What belongs in new-device onboarding?
29. What belongs in device decommissioning?
30. Which dependencies form a hybrid connectivity design?
31. What certificate lifecycle fields/actions must be governed?
32. Compare client, proxy, enterprise-browser, and RBI remote paths.
33. Why is tunnel-up not proof of secure application access?
34. Which logs distinguish policy denial from routing/DNS/certificate failure?
35. What does scaled 860 not mean?
36. Why are count, base duration, and price not stated here?
37. How long is certification valid under the checked handbook?
38. Which blueprint domain has the largest weight?
39. Why is the June 2026 blueprint especially volatile?
40. What must you recheck before scheduling?

## Answer key

1. It identifies protocol/application behavior and context independent of expected ports.
2. New-flow evaluation/session creation versus eligible cached established-session processing.
3. Initial traffic may reveal only an underlying/parent protocol until more payload behavior is observed.
4. Outbound TLS mediation; inbound server decryption; SSH mediation; governed exemption.
5. Authorization/privacy, trust/keys, compatibility, capacity, inspection policy, exceptions, logs, and failure modes.
6. Application, human/group, device, content/threat, and boundary context for policy.
7. A committed rule change does not necessarily rebuild already established session state.
8. Dedicated hardware, virtualized, container/Kubernetes, and cloud-managed/integrated enforcement forms.
9. Authorization/inspection action versus address translation.
10. WAN path selection/optimization, policy, and connectivity telemetry with supported security/NAT functions.
11. Cloud-delivered security/connectivity for remote users/networks and public/private applications.
12. Central on-prem/product management versus cloud-delivered cross-portfolio management, with current support varying.
13. One inherited/pushed error can affect many devices; stage and preserve recovery.
14. Supported/active license plus policy/profile attachment, visible test traffic, expected action/log, and healthy updates/telemetry.
15. Device discovery/risk/policy; sensitive-data classification/control; cloud-app discovery/governance.
16. File/content analysis; exploit/C2/threat prevention; web categorization; malicious DNS detection/prevention.
17. Telemetry/configuration-derived health/best-practice insights; it does not safely deploy every remediation by itself.
18. Certificate discovery/inventory, PKI/CA integration, issuance/renewal/deployment automation, policy, and crypto-agility.
19. Retaining currently encrypted data for future cryptanalytic capability.
20. Combine established and PQ mechanisms while new algorithms/interoperability mature, accepting added complexity.
21. Workforce tool access/data; model/app/data/agent lifecycle; adversaries' AI-amplified techniques.
22. Corroborating evidence, confidence/limitations, monitoring, and accountable human decision.
23. Threat/app/content packages can change frequently; platform software changes execution/components and needs fuller compatibility/rollback planning.
24. Health, synchronization, compatibility, capacity, sequence, failover, state, rollback, and out-of-band access.
25. Observe apps/dependencies, assign owner, design replacement, stage/test, monitor, and remove with rollback.
26. A mistaken device identity can apply unsafe policy, especially in OT/IoT.
27. Traffic-path enforcement versus provider-API/posture/data-at-rest activity, with different coverage/timing.
28. Identity/serial/tenant, licenses, connectivity/trust, version support, hierarchy/policy, logs, roles, validation.
29. Remove targets/routes/objects, revoke trust/tokens, retain required logs, reclaim licenses, and prove removal.
30. Routing/overlay, DNS, NAT, zones, segmentation, MTU, certificates, HA, cloud constructs, policy, and logs.
31. Discovery, owner/use, issuer/chain/name, key custody/use, algorithm, expiry, issuance/renewal/deployment/revocation/validation.
32. Endpoint tunnel, application proxy, controlled browser, and remotely isolated content execution.
33. Identity, routes, DNS, certificates, Security/NAT policy, inspection, app health, and logs can still fail.
34. Traffic/threat plus routing/system, DNS, authentication, decryption/certificate, tunnel/path, and application evidence.
35. It is not 86% raw correct; scaling accounts for exam-form differences.
36. The public datasheet/handbook omit them; live registration is authoritative.
37. Two years, subject to current recertification rules.
38. Platform Solutions, Services, and Tools at 30%.
39. It adds recent NGTS, post-quantum, AI-security, and evolving platform/packaging objectives.
40. Active blueprint, product docs, registration details, handbook, learning path, versions, and policies.

## Final readiness checklist

- [ ] I can walk new/established sessions through routing, NAT, policy, App/User/Device/Content context, decryption, and logs.
- [ ] I select PA/VM/CN/Cloud NGFW and Prisma SD-WAN/Access by architecture and operational responsibility.
- [ ] I distinguish Panorama and SCM hierarchy, configuration ownership, push/deploy, onboarding, reporting, and rollback.
- [ ] I can activate/attach/test/monitor every named CDSS function without assuming license equals enforcement.
- [ ] I use AIOps/BPA findings in a governed remediation workflow.
- [ ] I explain NGTS, certificate lifecycle, quantum risk, hybrid migration, and current AI security use cases.
- [ ] I plan profiles/policies/content/software/certificate changes with HA and canary validation.
- [ ] I operate IoT, DLP, SaaS, remote access, and hybrid connectivity with owners and evidence.
- [ ] I completed the three scenarios and eight labs with both allow and failure proof.
- [ ] I rechecked the June 2026 datasheet, current technical docs, handbook, and registration before purchase.

## Places to learn

This is not a complete list, and it is not a prescription to consume everything. Start with the blueprint and official path, then select documentation and labs for measured gaps. Product pages, UI, licensing, and course versions change; record the version you used.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Network Security Professional certification page](https://www.paloaltonetworks.com/services/education/palo-alto-networks-netsec-professional) | Public | 10–15 minutes | Current credential, official blueprint/path/registration links |
| [June 2026 datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/netsec-professional-datasheet.pdf) | Public PDF | 60–90 minutes | Canonical six-domain scope and all named product capabilities |
| [Certification Handbook](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/ebooks/panw-certification-handbook.pdf) | Public PDF | 30–45 minutes | Scoring, ESL, result, retake, validity, renewal, and integrity policy |
| [Official digital learning](https://learn.paloaltonetworks.com/learn) | Free account/login may be required | 30 minutes planning; modules vary | Follow page-linked Professional learning plan and record current duration/version |
| [PAN-OS documentation](https://docs.paloaltonetworks.com/pan-os) | Public | 15–30 hours selected topics | Packet flow, policy, NAT, App/User/Device-ID, decryption, profiles, updates, HA, logs |
| [Strata Cloud Manager documentation](https://docs.paloaltonetworks.com/strata-cloud-manager) | Public | 8–15 hours selected topics | Cloud management, AIOps/BPA, supported products, policy and operations |
| [Prisma Access documentation](https://docs.paloaltonetworks.com/prisma-access) | Public | 8–15 hours selected topics | Remote-user/network connectivity, policy, operations, and logging |
| [Prisma SD-WAN documentation](https://docs.paloaltonetworks.com/prisma-sd-wan) | Public | 5–10 hours selected topics | Path policy, branch connectivity, NAT/security, monitoring, failover |
| [Next-Generation Trust Security](https://www.paloaltonetworks.com/network-security/next-gen-trust-security) | Public | 2–4 hours with current docs | Certificate lifecycle, private PKI, crypto-agility, post-quantum transition |
| [Palo Alto Networks YouTube](https://www.youtube.com/@PaloAltoNetworks) | Free video | 4–10 hours selected current videos | Visual product and architecture explanations; map each to blueprint |
| [Pluralsight Palo Alto Firewalls for Network Protection](https://www.pluralsight.com/paths/palo-alto-firewalls-for-network-protection) | Paid; older path | About 4h05m listed core course plus labs | NGFW subset and alternative explanation; reconcile release/UI |
| [NDG PAN11 Firewall Essentials](https://www.netdevgroup.com/online/courses/cybersecurity/pan11-firewall-essentials) | Paid/institutional lab access | 14 labs; plan 15–25 hours | Configuration practice; older PCNSA alignment means map carefully to current blueprint |

No current official practice exam, MeasureUp product, or Whizlabs product explicitly aligned to this June 2026 credential was verified. Use original operational scenarios and current documentation; avoid any source claiming live questions or guaranteed matches.
