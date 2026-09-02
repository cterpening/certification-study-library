---
exam_code: PANW-CYBERSECURITY-PRACTITIONER
vendor_id: palo-alto-networks
official_blueprint: https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/practitioner-datasheet.pdf
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Palo Alto Networks Certified Cybersecurity Practitioner Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live certification page, December 2025 datasheet, July 2025 certification handbook, official documentation, public standards, and selected learning sources were checked September 2, 2026. This does not guarantee that every explanation is error-free or remains current. The [official certification page](https://www.paloaltonetworks.com/services/education/panw-cybersecurity-practitioner) and [datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/practitioner-datasheet.pdf) are authoritative.

**Current baseline:** Cybersecurity 19%; Network Security 19%; Secure Access 14%; Cloud Security 20%; Endpoint Security 15%; Security Operations 13%; December 2025 datasheet<br>
**Exam contract:** foundational English-language Pearson VUE certification; no recommended work experience. The handbook sets an 860 passing score on a 300–1000 scaled range and calls results provisional until data-forensics review. The public datasheet does not state item count, base duration, or price; verify these in the live registration flow.<br>
**Validity and renewal:** certification validity is two years under the July 2025 handbook. Recertification is by examination; an active higher-level credential can renew active lower-level credentials in the same track under the current pathway rules. Recheck before scheduling.<br>
**Upcoming change:** no retirement or dated replacement was found September 2, 2026. Product names and bundles are volatile even while the blueprint is active; verify live documentation, especially Cortex Cloud, Prisma AIRS, AI Access, and cloud-delivered services.<br>
**Integrity:** Palo Alto Networks says actual exam content is confidential and substantially similar/leaked questions are unauthorized. This guide uses the public blueprint, original checks, safe labs, standards, and public product documentation only.

## How to use this guide

The Practitioner blueprint adds basic product-family application to durable security concepts. For each objective, answer four questions: what problem does it address, where does it enforce or observe, what input/context does it require, and what remains uncovered? Then map the capability to the current Palo Alto Networks portfolio without assuming a product name is itself a control outcome.

Study in dependency order:

1. identity, threats, ATT&CK, and Zero Trust;
2. network enforcement, inspection, and segmentation;
3. branch/remote/SaaS/AI access paths;
4. cloud code/posture/runtime responsibilities;
5. endpoint evidence and response;
6. SOC hunting, incident response, exposure, and automation.

Use synthetic data and isolated labs. You can learn most foundational behavior without a paid product tenant. Where product access exists, verify current screens and documentation rather than memorizing interface positions.

> **About related items:** A `Related item:` callout adds architecture, operations, governance, implementation, or lifecycle context. It makes the published objective more useful in real work but does not imply the added wording appears in the official datasheet.

## Blueprint map

| Domain | Weight | Evidence of readiness |
|---|---:|---|
| 1. Cybersecurity | 19% | Map AAA, ATT&CK behavior, Zero Trust, APTs, and identity/mobile/email controls to evidence and decisions |
| 2. Network Security | 19% | Design layered NGFW/CDSS/microsegmentation inspection for network, OT, and IoT paths |
| 3. Secure Access | 14% | Compare SASE/SSE/SD-WAN and protect data/apps/AI use across distributed access |
| 4. Cloud Security | 20% | Distinguish AppSec, posture, workload/runtime, CSPM, CWPP, CNAPP, and Cortex Cloud |
| 5. Endpoint Security | 15% | Use behavior/IOC/context plus layered controls and Cortex XDR concepts |
| 6. Security Operations | 13% | Hunt, investigate/respond, manage exposure, and position SIEM/SOAR/XSIAM/Xpanse/Unit 42 |

## 1. Cybersecurity — 19%

### AAA, identity, and mobile/email controls

Authentication establishes an identity claim; authorization decides permitted actions; accounting records activity and consumption for audit, detection, troubleshooting, and sometimes billing. Keep AAA decisions correlated through stable identity/session context and protected timestamps/logs. A successful login is not authorization to every resource, and a log is useful only if it is complete, trustworthy, retained, and reviewed.

An identity provider authenticates identities and issues assertions/tokens to relying services. IAM manages identities, entitlements, policy, lifecycle, and review. MFA combines independent factor categories; two passwords are still one factor type. Evaluate phishing resistance, enrollment/recovery, token lifetime, device state, conditional access, and logging—not only the presence of MFA.

MDM manages device configuration/compliance and often OS-level controls; MAM governs enterprise application/data behavior, potentially without fully managing a personal device. Secure email gateways inspect mail flow for spam, phishing, malware, impersonation, and policy violations; integrated cloud email security can add API-based/internal-message visibility. Neither eliminates user, identity, endpoint, and incident-response needs.

> **Related item:** Recovery and enrollment are authentication paths. A strong primary factor with a weak help-desk reset process still creates an easy takeover route.

### ATT&CK, APTs, and Zero Trust

[MITRE ATT&CK](https://attack.mitre.org/) organizes observed adversary behavior. Tactics describe goals; techniques/sub-techniques describe how goals are pursued; procedures are observed implementations. Software, groups, mitigations, and detections connect behavior to intelligence. ATT&CK is not a chronological checklist and technique presence alone does not attribute an actor.

Use ATT&CK to map coverage: identify data sources, write detection logic, test a safe emulation, record blind spots, and improve. A signature/indicator can support a technique hypothesis, but behavioral and contextual evidence is needed.

An advanced persistent threat is typically capable, targeted, and sustained, adapting to defenses to pursue strategic objectives. “Advanced” does not mean every tool is custom; valid credentials and ordinary administration tools can support sophisticated campaigns. Attribution requires evidence and confidence, not branding every long intrusion as one named group.

Zero Trust continuously verifies relevant context, grants least privilege, and assumes breach. Apply it across identities, devices, applications/workloads, networks, and data. ZTNA provides policy-controlled access to specific private applications/resources rather than broad network presence. Continuous validation does not mean prompting for MFA every minute; it means reevaluating risk/context and enforcing session decisions.

## 2. Network Security — 19%

### Firewalls, microsegmentation, and inspection

A stateless filter evaluates packets independently against fields such as addresses, protocol, and ports. Stateful inspection tracks connection state and can validate return traffic. An NGFW adds application, user, device, threat, content, and other context to policy. Policy outcomes still depend on correct routing/zones, identity mapping, ordering, service/application behavior, profiles, decryption visibility, logging, and change control.

Microsegmentation places policy between fine-grained workload groups to reduce lateral movement. Define assets, identities, dependencies, expected flows, enforcement location, default behavior, exception owner, and telemetry. Segmentation labels without path enforcement do not reduce reachability.

IPS blocks or alerts on suspicious network behavior inline. URL filtering classifies web destinations; DNS Security analyzes/prevents malicious domain-resolution activity; VPN protects traffic through a tunnel but does not make endpoints trustworthy. Outbound forward-proxy TLS decryption lets an authorized enterprise intermediary inspect sessions by establishing separate trust relationships. It requires certificate deployment, privacy/legal scope, performance capacity, bypass governance, key protection, and failure-mode design.

Signature-based detection is efficient for known patterns but can miss mutation, obfuscation, unknown behavior, encrypted content, and context-dependent misuse. Combine signatures with protocol decoding, behavior, analytics, sandboxing, intelligence, endpoint/cloud context, and human investigation.

### NGFW deployment, OT/IoT, CDSS, and Precision AI

Physical/bare-metal firewalls provide dedicated appliances and interfaces; virtual NGFWs place enforcement in virtual/cloud architectures. Consider throughput/features, high availability, routing, east-west insertion, orchestration, licensing, log paths, management plane, and failure behavior. Cloud-native traffic paths may need several enforcement patterns rather than one perimeter appliance.

OT prioritizes safety, availability, deterministic processes, long asset lifecycles, specialized protocols, and controlled maintenance. IoT adds large numbers of often weakly managed devices with uncertain ownership and update support. Begin with passive discovery/classification, owner/use-case mapping, baseline behavior, least connectivity, monitoring, and compensating segmentation. Never run intrusive tests against operational systems without authorization and safety review.

Palo Alto Networks Cloud-Delivered Security Services attach centrally updated protections to enforcement platforms. The portfolio can include threat, URL, DNS, malware/sandbox, data, SaaS, and IoT-related capabilities; names and bundles change. For each service, identify traffic/telemetry prerequisites, inline versus API/out-of-band behavior, update path, fail-open/closed choice, privacy, and evidence.

Precision AI is Palo Alto Networks' umbrella positioning for combining machine learning, deep learning, and generative AI in security outcomes. Prepare at the function level: learn baselining/classification/detection/automation use, required data, confidence, evasion/drift, explainability, adversarial input, and human approval. Do not treat an AI-generated claim as evidence.

> **Related item:** Encrypted inspection and AI both create governance questions. A technically effective control can still fail if data use, access, retention, model behavior, and exceptions are not accountable.

## 3. Secure Access — 14%

SASE converges networking and security capabilities as cloud-delivered services for distributed users/sites/apps. SSE is the security-focused subset, commonly including secure web access, CASB, ZTNA, and data protection; it does not by itself include the complete WAN networking function. SD-WAN selects and steers paths across transports using centrally defined policy and application/network conditions. Prisma SASE combines current Palo Alto Networks access/security/networking offerings; verify the live bundle.

Apply confidentiality, integrity, and availability to:

- data itself, including classification, sharing, storage, transfer, and deletion;
- private apps, including identity-aware least access and hidden/reduced exposure;
- SaaS, including sanctioned/unsanctioned use, tenant/configuration, OAuth, data sharing, and API visibility;
- AI apps/tools/platforms, including prompts, uploads, outputs, model/API access, data retention, plugins/tools, and agent actions.

A Secure Web Gateway enforces web access and inspection. CASB discovers/governs cloud-app use via inline and/or API approaches. DLP classifies and enforces policy on sensitive data. Enterprise Browser applies controls inside a managed browser experience. Remote Browser Isolation executes risky web content away from the endpoint and delivers a safer representation/interaction. Each sees a different portion of the transaction; map overlaps and gaps.

Current product mappings in the datasheet include Prisma Access, Prisma SD-WAN, Prisma Access Browser, Enterprise DLP, AI Access, and Prisma AIRS. Learn the distinction:

- access/connectivity and security-policy delivery;
- WAN path selection;
- browser-level control;
- sensitive-data discovery/enforcement;
- governance of workforce AI use;
- security for AI applications/models/agents.

Names and capabilities evolve. Use current datasheets/docs and explain the security outcome rather than memorizing slogans.

> **Related item:** A distributed access policy needs identity, device, application, data, and location/risk context that remain consistent across office, branch, home, cloud, and SaaS paths.

## 4. Cloud Security — 20%

### Architectures, topologies, and challenge layers

Cloud systems can span public/private/hybrid/multicloud, regions/zones, VPCs/VNets, subnets, gateways, managed services, containers/Kubernetes, serverless, APIs, and SaaS. Diagram control-plane and data-plane paths plus internet, east-west, management, build, identity, and third-party trust boundaries.

Application Security addresses code, dependencies, APIs, build pipelines, artifacts, and design flaws. Cloud Posture Security discovers configuration, exposure, identity/permission, compliance, and control-plane risk. Cloud Runtime Security observes/protects running hosts, VMs, containers, serverless workloads, and processes. Findings can cross layers: an internet-exposed vulnerable workload with excessive cloud permissions is more urgent than three isolated scores.

CSPM continuously assesses cloud configuration/posture and policy. CWPP protects workloads across build/deploy/runtime, with coverage depending on agent, agentless scan, admission, and runtime mechanisms. CNAPP unifies several cloud-native security functions and their context, commonly including code/application, posture, entitlement, workload/runtime, data, and response. Acronym coverage differs by vendor; evaluate evidence and enforcement.

Shared responsibility varies by IaaS/PaaS/SaaS and exact service. Assign an owner for identity, configuration, software, network policy, data, keys, logging, backup, incident response, and deletion. “Cloud provider” and “customer” are not sufficient without a service-specific responsibility matrix.

### Cortex Cloud

The blueprint asks for features/functionality of Cortex Cloud. At a durable level, understand the platform's purpose as unifying application/cloud security context and SecOps workflows from code/cloud posture through runtime, detection, investigation, and response. Current offerings and packaging can include cloud security, application security, posture, runtime, data, and SOC integrations. Verify exact names and availability in [current Cortex Cloud documentation](https://docs.paloaltonetworks.com/resources/all-products-a-z).

Explain how prioritization combines attack paths, exposure, vulnerability, identity, data sensitivity, and runtime behavior; how developers/cloud/security operations receive findings; and where prevention or response occurs. A unified dashboard is not proof of unified telemetry, ownership, remediation, or policy.

> **Related item:** Ephemeral assets can exist for minutes. Effective cloud inventory and runtime protection must follow provider APIs, orchestrators, identities, and deployment events rather than a periodic spreadsheet.

## 5. Endpoint Security — 15%

An indicator of compromise is an observable associated with suspected malicious activity—such as a file hash, domain, process behavior, registry change, or account event. Indicators vary in durability and confidence. A single shared infrastructure IP is not automatically proof of compromise; correlate time, process ancestry, identity, endpoint, network, and threat intelligence.

Signature anti-malware identifies known patterns efficiently but can miss novel/modified/fileless/living-off-the-land behavior and encrypted/packed content. Behavioral Threat Prevention evaluates activity and relationships rather than only a static fingerprint. UEBA builds or applies behavioral expectations to users/entities and highlights anomalies; anomaly is a lead, not a verdict.

EDR continuously records/analyzes endpoint activity and supports detection, investigation, containment, and response. XDR correlates across endpoint plus other data sources such as identity, network, email, and cloud to form incidents and richer causality. Data quality, retention, sensor health, permissions, time, and analyst workflow determine usefulness.

Layer supporting controls:

- host firewall/HIPS limits connections and blocks host-observed exploit/activity patterns;
- device/USB control governs peripherals and removable media;
- application control limits executable/software behavior;
- disk encryption protects data at rest when devices/storage are lost, with key recovery requirements;
- patch management inventories, tests, deploys, verifies, and handles exceptions.

Cortex XDR's durable functions include endpoint telemetry/protection, behavioral and analytic detection, incident correlation, investigation/causality, threat hunting, and response actions. Verify current licensing and platform requirements; a feature name does not guarantee sensor coverage or authorization to isolate a production endpoint.

## 6. Security Operations — 13%

### Hunting and incident response

Threat hunting is a hypothesis-led, iterative search for adversary behavior not adequately surfaced by existing alerts. Start from threat intelligence, ATT&CK technique, asset risk, anomaly, or observed gap; identify required telemetry; query; investigate; record negative/positive evidence; and turn validated findings into detections or control improvements. Random searching is not a measurable hunt.

Incident response prepares, detects/analyzes, contains, eradicates, recovers, and learns. Exact frameworks vary. Preserve evidence, decision times, scope, owners, legal/privacy/communications obligations, containment tradeoffs, recovery criteria, and lessons. An outcome is not only “ticket closed”; it includes trusted restoration and reduced recurrence.

SIEM ingests/normalizes/searches/correlates telemetry and supports detection/reporting. SOAR orchestrates cases, enrichment, playbooks, and response actions across tools. XSIAM aims to unify/automate SOC data, analytics, incident operations, and response. These overlap but do not eliminate detection engineering, data governance, or human accountability.

### Exposure, Cortex solutions, and Unit 42

Attack Surface Management discovers and continuously assesses internet-facing/external assets and exposures from an outside perspective. It must establish asset ownership and validate findings; discovered infrastructure can be third-party, stale, or intentionally exposed. Cortex Xpanse maps to this external attack-surface role.

Cortex XSOAR centers on orchestration, automation, incident/case workflows, integrations, and threat-intelligence processes. Cortex XSIAM centers on an AI/automation-driven security operations platform and broad telemetry/incident handling. Xpanse supplies attack-surface discovery/context. Know what evidence moves between them and where an analyst approves disruptive actions.

Unit 42 provides threat intelligence, incident response, managed detection/response, and assessment/advisory services as currently offered. Distinguish product capability from a human-delivered service engagement, and verify the live service catalog.

> **Related item:** Automation should be idempotent, authorized, observable, rate-limited, and reversible where possible. Enrichment can be automatic; account disablement or network isolation may require confidence and approval tiers.

## Integrated scenarios

### Compromised remote developer

Trace a phishing-resistant identity failure or token theft through ZTNA access to a private app, endpoint execution, source access, cloud credentials, and data movement. Map IdP/MFA, MDM/MAM, email security, Prisma Access/Browser, NGFW/CDSS, Cortex XDR, Cortex Cloud, XSIAM/XSOAR, DLP, and incident response. Identify which telemetry proves scope and which control can contain without destroying evidence.

### AI application launch

Model developers, repository, pipeline, cloud resources, model/API, prompts/retrieval data, agent tools, user access, and logs. Assign AppSec/posture/runtime/data/identity owners and place AI Access versus Prisma AIRS by use case. Threat-model prompt injection, sensitive-data leakage, excessive agency, poisoned dependencies/data, stolen API keys, and unreviewed model output.

### Unknown internet-facing service

An ASM finding identifies an exposed cloud service. Validate ownership/DNS/cloud account, classify data/app, correlate posture and runtime risk, restrict access, inspect network/endpoint/cloud evidence, hunt for ATT&CK behaviors, and decide whether it is exposure or incident. Automate enrichment while requiring approval for destructive containment.

## Hands-on labs

1. **AAA and ATT&CK:** generate synthetic login/access/accounting events, map a benign emulation to tactics/techniques/data sources, and write a detection hypothesis without claiming attribution.
2. **Zero Trust/ZTNA:** design identity/device/app/data context for three private-app decisions; test revoked identity, unmanaged device, excessive role, and session risk changes.
3. **Network enforcement:** build isolated stateful/stateless rules, DNS/URL block tests, microsegments, and a TLS forward-proxy design review; prove allow/deny/log paths.
4. **Secure access:** diagram office/branch/home/SaaS/private/AI flows and map SWG, CASB, DLP, enterprise browser, RBI, SD-WAN, and SSE/SASE without duplicating or missing responsibilities.
5. **Cloud graph:** inventory a disposable cloud workload from code/dependency through posture/identity/data/runtime. Prioritize combined attack paths and verify remediation evidence.
6. **Endpoint timeline:** generate harmless process/file/network activity, form an IOC-plus-behavior timeline, compare signature/UEBA/EDR/XDR reasoning, and document containment authorization.
7. **Hunt-to-detection:** write a hypothesis, identify telemetry, query synthetic logs, investigate exceptions, create a detection, measure false positives, and update a playbook.
8. **Exposure-to-incident:** use authorized local assets to simulate ASM discovery, owner validation, risk correlation, ticketing, containment decision, automation guardrails, and lessons learned.

## Original readiness checks

1. How do authentication, authorization, and accounting differ?
2. Why is two-password authentication not MFA?
3. What is the difference between MDM and MAM?
4. How do tactics, techniques, and procedures differ in ATT&CK?
5. Why does ATT&CK technique overlap not prove attribution?
6. What distinguishes an APT from ordinary “advanced malware” labeling?
7. What three Zero Trust principles does the blueprint name?
8. How does ZTNA differ from broad network VPN access?
9. How do stateless, stateful, and NGFW policy decisions differ?
10. What must exist for microsegmentation to reduce reachability?
11. Which problem is addressed by IPS, URL filtering, DNS Security, and VPN respectively?
12. What governance is required for outbound TLS decryption?
13. Why are signatures insufficient by themselves?
14. How do physical and virtual NGFW deployment concerns differ?
15. Why should OT discovery begin passively?
16. What must be checked for a cloud-delivered security service?
17. What does Precision AI describe at a durable level?
18. How do SASE and SSE differ?
19. How does SD-WAN differ from an SWG?
20. Compare SWG, CASB, DLP, Enterprise Browser, and RBI enforcement/visibility.
21. Which risks are specific to workforce AI use versus building an AI application?
22. How do AppSec, posture security, and runtime security differ?
23. What do CSPM and CWPP contribute to CNAPP?
24. Why must shared responsibility be service-specific?
25. What is the durable purpose of Cortex Cloud?
26. Why is an IOC not proof of compromise?
27. How do signature, behavior, UEBA, EDR, and XDR build different evidence?
28. Which supporting endpoint controls does the blueprint list?
29. What makes threat hunting hypothesis-led?
30. What outcomes should incident response produce?
31. How do SIEM, SOAR, and XSIAM differ/overlap?
32. What must ASM do after discovering an asset?
33. How do XSOAR, Xpanse, and XSIAM differ?
34. How do Unit 42 services differ from a product license?
35. Which actions are safe to automate without approval, and why?
36. Why are item count, base duration, and price absent from this snapshot?
37. What does an 860 scaled pass score not mean?
38. How long is the credential valid under the checked handbook?
39. Why must product details be checked again even if the blueprint is unchanged?
40. How can you identify unauthorized exam material?

## Answer key

1. Establish identity; decide permitted actions; record activity/use.
2. Both are the same knowledge-factor category.
3. Device-wide configuration/compliance versus enterprise app/data policy, potentially without full device control.
4. Goal; behavioral method; observed implementation.
5. Many actors reuse techniques; attribution requires broader evidence and confidence.
6. Sustained, targeted, capable/adaptive pursuit of strategic objectives, not one tool label.
7. Continuous monitoring/validation, least privilege, and assume breach.
8. App/resource-specific contextual access versus placement onto a broad network.
9. Independent packet fields; connection state; richer app/user/device/threat/content context.
10. Enforced policy on the relevant paths with known dependencies and default/exception behavior.
11. Intrusion behavior, web destinations, malicious domain resolution, and protected tunneling.
12. Authorization, certificates/keys, privacy/legal scope, capacity, bypass, logging, and failure behavior.
13. Unknown, modified, contextual, or invisible behavior can evade them.
14. Appliance/interface/HA/capacity versus virtual insertion/orchestration/cloud routing, with shared policy needs.
15. Active probing can disrupt fragile/safety-critical systems.
16. Visibility prerequisites, enforcement point, updates, failure mode, privacy, and evidence.
17. A portfolio approach combining ML/deep learning/generative AI for security, with data/confidence/governance limits.
18. SASE includes converged networking plus security; SSE is the security-services subset.
19. WAN path selection/steering versus web traffic security/inspection.
20. Web gateway; cloud-app inline/API governance; data classification/enforcement; in-browser control; remote execution/isolation.
21. Employee prompt/upload/tool governance versus model/data/code/supply-chain/agent/runtime security.
22. Code/build/API; control-plane configuration/exposure/identity; running workload behavior/protection.
23. Configuration/posture assessment and workload protection, integrated with wider application/data/identity context.
24. Customer/provider duties vary for each exact IaaS/PaaS/SaaS capability.
25. Unified code-to-cloud/runtime context and security-operations investigation/response across current offerings.
26. Indicators vary in confidence/sharedness and require contextual corroboration.
27. Known pattern; activity; anomaly; endpoint telemetry/response; cross-domain correlation.
28. Host firewall/HIPS, device/USB control, application control, disk encryption, and patching.
29. It starts with a testable behavior/gap hypothesis and defined data, evidence, result, and improvement.
30. Containment/eradication, trusted recovery, evidence/decisions, communication, and reduced recurrence.
31. Telemetry/search/correlation; orchestration/playbooks; broader unified analytics/data/incident automation.
32. Validate ownership and exposure, enrich/prioritize, and route accountable remediation or investigation.
33. Orchestration; external attack surface; unified security operations.
34. They are expert-delivered intelligence, response, managed, or advisory engagements rather than software functionality alone.
35. Low-impact, authorized, idempotent enrichment is easier to automate; disruptive actions need confidence/approval/rollback.
36. The current public datasheet/handbook do not publish them; live registration is authoritative.
37. It is not 86% raw correct; scaling accounts for exam-form difficulty.
38. Two years, subject to current recertification rules.
39. Product packaging and capabilities change faster than certification titles/weights.
40. It claims live/leaked/substantially similar questions, guaranteed matches, or lacks legitimate blueprint-based provenance.

## Final readiness checklist

- [ ] I connect AAA, IdP/IAM/MFA, MDM/MAM, email security, ATT&CK, APTs, and Zero Trust in one identity-threat story.
- [ ] I select stateless/stateful/NGFW, microsegmentation, IPS, URL/DNS, VPN, and decryption controls by visibility and outcome.
- [ ] I can map current CDSS and Precision AI functions without inventing capabilities.
- [ ] I distinguish SASE/SSE/SD-WAN and SWG/CASB/DLP/browser/RBI responsibilities.
- [ ] I protect private, SaaS, and AI use while preserving confidentiality, integrity, and availability.
- [ ] I distinguish AppSec/posture/runtime, CSPM/CWPP/CNAPP, shared responsibility, and Cortex Cloud.
- [ ] I correlate IOC, behavior, UEBA, EDR/XDR, and supporting endpoint controls.
- [ ] I execute a documented hunt and incident-response flow and distinguish SIEM/SOAR/ASM/XSIAM/XSOAR/Xpanse/Unit 42.
- [ ] I can complete all integrated scenarios with evidence, owners, failure paths, and automation guardrails.
- [ ] I rechecked the live datasheet, product docs, handbook, and registration details before purchase.

## Places to learn

This is not a complete list, and it is not a prescription to consume everything. Start with the blueprint, select the official learning modules that close measured gaps, and use standards/labs for durable concepts. Durations are publisher-listed or clearly labeled estimates and can change.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Cybersecurity Practitioner certification page](https://www.paloaltonetworks.com/services/education/panw-cybersecurity-practitioner) | Public | 10–15 minutes | Current credential identity, datasheet, learning path, and registration |
| [December 2025 exam datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/practitioner-datasheet.pdf) | Public PDF | 45–75 minutes | Canonical six-domain weighted blueprint and named product functions |
| [Palo Alto Networks Certification Handbook](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/ebooks/panw-certification-handbook.pdf) | Public PDF | 30–45 minutes | Scoring, ESL, retakes, validity, renewal, integrity, and result policy |
| [Official Palo Alto Networks digital learning](https://learn.paloaltonetworks.com/learn) | Free account/login may be required | 20–30 minutes planning; modules vary | Locate the Cybersecurity Practitioner path; the public certification page currently resolves to the portal rather than a stable deep link |
| [Palo Alto Networks technical documentation](https://docs.paloaltonetworks.com/) | Public | 8–15 hours selected topics | Current NGFW, Prisma, Cortex, cloud, and CDSS behavior |
| [MITRE ATT&CK Enterprise](https://attack.mitre.org/matrices/enterprise/) | Public | 3–6 hours overview and mapping lab | Tactics, techniques, sub-techniques, software/groups, mitigations, and data sources |
| [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) | Public | 2–4 hours | Durable Zero Trust concepts and policy decision/enforcement architecture |
| [Cortex Cloud documentation](https://docs.paloaltonetworks.com/resources/all-products-a-z) | Public | 3–6 hours selected current pages | Code/cloud/runtime/SOC platform mapping; verify packaging |
| [Cortex XDR documentation](https://docs.paloaltonetworks.com/cortex/cortex-xdr) | Public | 3–6 hours selected current pages | Endpoint telemetry, incidents, investigation, hunting, and response concepts |
| [Palo Alto Networks YouTube](https://www.youtube.com/@PaloAltoNetworks) | Free video | 3–8 hours selected current videos | Visual product/concept explanations; map every video to a blueprint gap |
| [Palo Alto Networks Cybersecurity Fundamentals](https://www.oreilly.com/videos/palo-alto-networks/9781835885468/) | Paid/O'Reilly; 2024 course | 6h47m listed plus labs | Broad alternate introduction; older product names require current-doc reconciliation |
| [Pluralsight Palo Alto Firewalls for Network Protection](https://www.pluralsight.com/paths/palo-alto-firewalls-for-network-protection) | Paid; older NGFW-focused path | About 4h05m listed core course plus labs | Network-security subset only; not full exam coverage and may use older UI/features |
| [NDG Cybersecurity Essentials PAN8 labs](https://www.netdevgroup.com/content/paloalto/labs/cybersecurity_essentials.html) | Institution/NETLAB+ access; academic partner may be required | 12 labs; plan 12–24 hours | Legacy but practical Zero Trust/authentication/App-ID/decryption/endpoint-style exercises; reconcile PAN-OS version |

No current official practice exam, MeasureUp product, or Whizlabs product explicitly aligned to this exact Practitioner blueprint was verified. Prefer original scenario checks and the current official learning path over question banks that do not identify source, version, and authorization.
