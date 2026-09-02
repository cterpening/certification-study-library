---
exam_code: PANW-SECURITY-OPERATIONS-PROFESSIONAL
vendor_id: palo-alto-networks
official_blueprint: https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/secops-professional-datasheet.pdf
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Palo Alto Networks Certified Security Operations Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live certification page, July 2026 datasheet, July 2025 certification handbook, official Cortex documentation, NIST/MITRE sources, and selected public learning sources were checked September 2, 2026. This does not guarantee that every explanation is error-free or remains current. The [official page](https://www.paloaltonetworks.com/services/education/palo-alto-networks-secops-professional) and [datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/secops-professional-datasheet.pdf) are authoritative.

**Current baseline:** SecOps fundamentals 25%; threat intelligence/incident response 16%; Cortex XDR 23%; Cortex XSOAR 16%; Cortex XSIAM 20%; July 2026 datasheet<br>
**Exam contract:** professional-level English Pearson VUE certification. Under the current handbook, Palo Alto Networks exams use an 860 passing score on a 300–1000 scaled range and provisional results. The datasheet omits item count, base duration, and price; verify them in live registration.<br>
**Experience boundary:** job-ready basic application in a SOC, including dashboards/reports, cases, indicators, hunting, playbooks, escalation, and response. Product screens vary; prepare around workflows, evidence, permissions, and outcomes.<br>
**Validity and renewal:** two years under the July 2025 handbook, subject to current recertification pathway rules.<br>
**Upcoming change:** no retirement or dated replacement was found September 2, 2026. The July 2026 blueprint is recent; Cortex XDR/XSIAM/XSOAR packaging and interfaces remain volatile.<br>
**Integrity:** actual exam content is confidential. This guide uses only the public blueprint, original questions, synthetic telemetry, and public documentation.

## How to use this guide

Build one incident from raw event to learning loop. For every Cortex concept, identify input data, normalization/stitching, analytic/detection, case or incident representation, investigation evidence, automation, response authority, and audit trail. A dashboard is not an investigation; an indicator match is not a verdict.

Practice this loop:

1. state a hypothesis and expected evidence;
2. validate sensor/data health, identity, time, parsing, and retention;
3. scope related users/assets/artifacts and build a timeline/causality story;
4. categorize/prioritize, contain or escalate under authority, and preserve evidence;
5. improve detections, playbooks, controls, reports, and data coverage.

Use synthetic or organization-approved data. Do not upload proprietary indicators/files to public services without authorization; VirusTotal submissions can be shared with its ecosystem according to service terms.

> **About related items:** A `Related item:` callout adds operational, architectural, governance, implementation, or lifecycle context. It helps turn a published objective into safer real work but is not claimed as verbatim exam scope.

## Blueprint map

| Domain | Weight | Evidence of readiness |
|---|---:|---|
| 1. Security Operations Fundamentals | 25% | Govern roles/data/logs and produce an accurate report/dashboard tied to a SOC decision |
| 2. Threat Intelligence and Incident/Case Response | 16% | Prioritize and hunt a case using evidence, intelligence, classification, and current NIST context |
| 3. Cortex XDR | 23% | Explain sensor-to-stitching-to-causality-to-response and manage agent coverage |
| 4. Cortex XSOAR | 16% | Drive a case through integrations, TIM, playbooks, War Room evidence, scripts, and jobs |
| 5. Cortex XSIAM | 20% | Explain ingestion, analytics/correlation, incidents, queries, BIOCs, automation, and content |

## 1. Security Operations fundamentals — 25%

### SOC roles, tools, and analytics

A SOC combines people, processes, technology, intelligence, and authority. Roles can include monitoring/triage analyst, investigator, incident commander, threat hunter, detection/content engineer, platform/data engineer, automation engineer, threat-intelligence analyst, forensics/malware specialists, and management. Define handoffs and escalation by evidence, impact, confidence, and authority—not tier numbers alone.

Core capabilities include telemetry collection/normalization, SIEM analytics, endpoint/network/cloud/identity detection, case management, SOAR, threat intelligence, hunting/query, vulnerability/exposure context, reporting, and response integrations. Asset/identity criticality and business context turn observations into risk decisions.

Machine learning learns statistical relationships from data for classification, clustering, anomaly detection, ranking, or other tasks. AI is a broader umbrella that includes ML and generative/reasoning systems. In a SOC, both can prioritize/correlate/summarize or recommend actions. Validate source evidence, confidence, drift, bias, evasion, prompt injection, privacy, and hallucination; analysts remain accountable.

### Cortex XDR governance, logs, reports, and dashboards

Users and roles implement least privilege for administration, investigation, hunting, content, response, and data access. Separate duties for high-impact actions. Review inactive users, service accounts/API keys, role changes, and emergency access.

Log management includes source onboarding, parsing/normalization, timestamps/time zones, identifiers, completeness, retention, access, privacy, integrity, storage cost, and collection health. Data protection governs sensitive endpoint/user/content data and exports. Compliance maps evidence to requirements but a passing dashboard is not proof that every control operates effectively.

Dashboards summarize current state/trends for an audience; reports preserve/share defined evidence over a period. Start with a decision and metric definition, scope/filter/time zone, source freshness, denominator, exclusions, owner, and drill-down. Avoid vanity counts and charts that hide ingestion gaps.

> **Related item:** “No alerts” can mean no attacks, failed collection, broken parsing, disabled rules, or insufficient coverage. Dashboard health must include the pipeline itself.

## 2. Threat intelligence and incident/case response — 16%

### Incident lifecycle and management

The current [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) integrates incident response into CSF 2.0 risk management: preparation spans Govern/Identify/Protect; incident activity uses Detect/Respond/Recover; improvement feeds every function. Older training often describes preparation; detection/analysis; containment/eradication/recovery; post-incident activity. Understand both mappings and use the current document for practice rather than assuming a memorized list is timeless.

Incident management assigns ownership, category, severity/priority, status, evidence, tasks, approvals, communications, service/legal/privacy obligations, containment, recovery criteria, and lessons. Category describes what kind of issue; priority decides handling order using confidence, asset/user/data criticality, exposure, scope, and impact. Escalate when authority/skill/impact thresholds are crossed.

### Intelligence and indicators

Threat intelligence is evidence-based context about threats relevant to decisions. Evaluate source, timeliness, confidence, specificity, sharing/handling, and corroboration. Strategic, operational, tactical, and technical products serve different audiences. ATT&CK behavior can be more durable than individual indicators.

File hashes, IPs, domains, and URLs can enrich/detect/block, but each can be shared, reassigned, compromised, sinkholed, or short-lived. Record type, value, time, source, confidence, relationships, first/last seen, verdict, and action. Normalize carefully—URL paths/case/encoding and domain hierarchy affect matching.

Advanced WildFire analyzes suspicious files/content and returns/distributes verdict and protections in its ecosystem. Unit 42 produces Palo Alto Networks research/intelligence and human-delivered services. VirusTotal aggregates many engines/data relationships as an external service. None is an absolute oracle; do not treat multi-engine counts as ground truth, and follow data-sharing authorization.

True positive means the case correctly identifies targeted malicious/undesired behavior; false positive means benign activity was flagged; false negative means relevant activity was missed. A true negative is correctly ignored benign activity. Tune using coverage, precision, recall, workload, detection latency, and impact—not alert volume alone.

Basic indicator-led hunting searches relevant time ranges/data sources for the indicator and related behavior, validates hits, pivots across users/assets/processes/domains, scopes impact, and preserves a reproducible query/timeline. It can seed a broader hypothesis, but an IOC search alone is not mature threat hunting.

> **Related item:** Before blocking an IP/domain/hash globally, check shared services, business dependencies, prevalence, confidence, and rollback. Enrichment can be automated more safely than disruptive enforcement.

## 3. Cortex XDR — 23%

### Evidence pipeline and investigation

Sensors collect endpoint and supported broader telemetry. Data sources supply events plus users, assets, and artifacts. Log stitching links records that describe the same or related activity across sources. Behavioral analytics identify deviations/patterns; detections generate alert evidence; Cortex can correlate related alerts into incident/case context depending on current product workflow.

Causality View organizes process/activity relationships so an analyst can trace parent/child execution, files, network activity, users, and alerts. It is a hypothesis aid: verify timestamps, sensor coverage, command/path, signatures, prevalence, identity, network/cloud evidence, and missing nodes. Artifacts are observable evidence; assets/users are affected or contextual entities.

Detection/response actions can include investigation acquisition/query and endpoint/process/file/network/account-related containment depending on licensing/integration. Confirm target, business impact, authority, evidence preservation, reversibility, and post-action verification before initiating.

WildFire verdict/context contributes file-related evidence. Behavioral analytics complements signatures but can create anomalies that need context. XDR extends beyond endpoint-only EDR by correlating multiple security data sources and analytics; choose it where cross-domain causality and unified investigation/response reduce gaps. It does not eliminate source-specific expertise or data-quality work.

### Agent management and deployment

Plan supported OS/cloud workload, agent version/content, tenant association, proxy/network reachability, installation package/profile, security permissions, tamper protection, policy assignment, staged rollout, reboot/user impact, upgrades, health, isolation behavior, uninstall/decommission, and rollback. Cloud workloads can be ephemeral or autoscaled, so integrate deployment with images/orchestration and verify coverage by expected-versus-seen assets.

Test sensor health, policy/content, data arrival, detection, and a safe response on a canary. An installed agent that cannot communicate or load protection is not coverage.

## 4. Cortex XSOAR — 16%

Marketplace content provides supported integrations/content packs according to current versions. Integrations connect external systems through credentials, endpoints, instances, and commands. Use least-privilege service identities, secret rotation, network restrictions, version compatibility, rate limits, and test instances.

A playbook is an orchestrated workflow of tasks, conditions, data transformations, manual approvals, and automation. Design idempotency, retries/timeouts, error branches, evidence, human gates, rollback, and test cases. The War Room records investigation activity, commands, results, notes, files, and collaboration; maintain useful evidence rather than noisy secrets or unbounded output.

Threat Intelligence Management ingests indicators/feeds, normalizes/deduplicates/enriches, applies confidence/reliability/lifecycle, and supports sharing/action. Feed ingestion is not truth. Expire stale indicators and protect handling restrictions.

Scripts are reusable automation logic/commands invoked by analysts or playbooks. Jobs schedule recurring or one-time execution of supported tasks/playbooks on a defined cadence. A script defines work; a job schedules work. Check execution context, permissions, inputs, side effects, timeout, concurrency, and audit.

Case investigation moves through categorization, enrichment, evidence, tasks, collaboration, decisions, response, closure, and learning. Third-party systems remain systems of record for some actions; reconcile status and avoid duplicate execution.

> **Related item:** A playbook is executable policy. Treat changes like code: source/version, review, test data, staged release, monitoring, rollback, and an owner.

## 5. Cortex XSIAM — 20%

XSIAM combines broad data ingestion, normalization/stitching, analytics/detection, incidents, investigation/hunting, automation, response, and security operations management. Sensors and integrations provide data. Content packs package supported content/integrations; playbooks and automations execute workflows. Validate version/dependencies and never assume installed content is enabled or tuned.

Data ingestion requires source inventory, schema/parsing, time, identity/asset normalization, deduplication, filtering, retention, cost, sensitive-data governance, and health monitoring. Build expected-event tests and collection-gap alerts. Log stitching connects related evidence only when identifiers and time/context support the relationship.

Investigation artifacts include files, hashes, URLs, domains, IPs, processes, commands, registry/cloud objects, and other observables; assets and users supply affected/contextual entities. Use incident/case chronology and graph relationships, then pivot with queries. Preserve query text, time range, data source, assumptions, and result counts.

An IOC is an observable associated with suspected compromise. A BIOC expresses behavior-based logic in Cortex terminology. Correlation rules combine events/alerts/context to detect multi-step conditions. Each needs objective, data prerequisites, logic, exceptions, severity, mapping, response, owner, version, test cases, and false-positive/false-negative review.

Threat management covers intake, enrichment, prioritization, investigation, containment/remediation, recovery, and learning. Hunting searches/queries should test a behavior or gap and become reproducible detection/content improvements. XSIAM automation may enrich, assign, notify, query, isolate, block, or otherwise act through integrations—gate high-impact steps.

> **Related item:** Detection-as-code practices make rules portable and reviewable, but production behavior still depends on the target data model, parsing, timing, and platform-specific semantics.

## Integrated scenarios

### Malicious-document incident

Trace email delivery, file analysis/verdict, endpoint process causality, outbound domain/IP, user/asset context, and related identity/cloud logs. Categorize and prioritize; use XDR evidence/response, XSIAM search/correlation, XSOAR enrichment/approval; preserve timeline and update a detection/playbook.

### Cloud workload agent gap

A dashboard shows fewer reporting agents than cloud assets. Validate inventory and ephemeral lifecycle, deployment image/profile, network/proxy, version, tenant, policy, and ingestion. Determine whether this is compliance drift, operational issue, or incident blind spot. Remediate through a canary and report denominator/exceptions accurately.

### Noisy-domain correlation

A domain feed creates hundreds of alerts. Evaluate intelligence source/confidence/time, shared infrastructure, resolution history, asset/user/causality context, and related techniques. Classify TP/FP/FN risks, tune matching/correlation, expire stale data, and add human approval before global block.

## Hands-on labs

1. **SOC RACI:** define roles, permissions, escalation, data access, response authority, metrics, and after-hours handoffs for the three scenarios.
2. **Telemetry health:** generate synthetic endpoint/DNS/auth/cloud events; normalize time/user/asset/indicator fields, introduce a collection gap, and make the dashboard reveal it.
3. **NIST case:** run a simulated incident through current CSF-aligned NIST guidance and map the older four-phase vocabulary for recognition.
4. **Indicator workbook:** safely analyze synthetic hash/IP/domain/URL records with confidence/lifetime/relationships; compare mock WildFire, Unit 42, and VirusTotal evidence.
5. **XDR causality:** build a process/network/file graph and identify sensors, stitched evidence, assets, users, artifacts, behavioral signal, uncertainty, and authorized response.
6. **Agent rollout:** design endpoint/cloud-workload deployment with a canary, policy assignment, health/coverage denominator, upgrade/rollback, and decommission proof.
7. **XSOAR playbook:** model intake, enrichment, conditions, manual approval, response, errors/retries, War Room evidence, TIM lifecycle, one script, and one scheduled job.
8. **XSIAM content:** write a behavior hypothesis, ingestion prerequisites, query, IOC/BIOC/correlation logic, test cases, tuning measures, automation boundary, and versioned deployment plan.

## Original readiness checks

1. Which roles and handoffs form a basic SOC?
2. How do AI and ML differ?
3. What risks accompany AI-assisted analysis?
4. What belongs in Cortex role/access governance?
5. What makes log management more than retention?
6. How does a dashboard differ from a report?
7. Why must a dashboard show collection health?
8. How did NIST SP 800-61 Rev. 3 reframe incident response?
9. How do category and priority differ?
10. When should a case be escalated?
11. What makes threat intelligence decision-useful?
12. Why are file/IP/domain/URL indicators not verdicts?
13. Compare WildFire, Unit 42 intelligence, and VirusTotal.
14. Define TP, FP, and FN.
15. What makes an indicator search a useful basic hunt?
16. What do Cortex XDR sensors and data sources provide?
17. What is log stitching?
18. What is Causality View used for?
19. Why must a causality graph still be verified?
20. How does XDR differ from endpoint-only EDR?
21. What precedes a response action?
22. What must an agent deployment plan include?
23. Why is installed-agent count not coverage proof?
24. What does XSOAR Marketplace content provide?
25. What makes a playbook production-safe?
26. What belongs in the War Room?
27. How should TIM manage indicator lifetime/confidence?
28. How do scripts and jobs differ?
29. What must be protected in a third-party integration?
30. What capabilities does XSIAM combine?
31. What does data-ingestion health require?
32. How do artifacts, assets, and users differ in an investigation?
33. How should a hunting query be recorded?
34. How do IOC, BIOC, and correlation rule differ?
35. What content metadata/testing should a detection include?
36. Which automation needs a human gate?
37. What does scaled 860 not mean?
38. Why are base duration/count/price absent from this guide?
39. How long is the credential valid under the checked handbook?
40. What must you recheck before scheduling?

## Answer key

1. Monitoring/triage, investigation/response, hunting/detection, platform/data/automation/intelligence, command/management with explicit escalation.
2. ML is a family of data-learned techniques within broader AI.
3. Hallucination, bias/drift/evasion, prompt injection, privacy, hidden uncertainty, and unapproved actions.
4. Least privilege, separation, lifecycle/review, API/service accounts, changes, emergency access, and audit.
5. Sources, parsing, time, identities/assets, completeness, integrity, access/privacy, health, and cost.
6. Interactive current/trend summary versus defined distributable evidence over a period.
7. No events may mean a broken pipeline rather than a safe environment.
8. It integrates preparation and response/improvement across CSF 2.0 Govern/Identify/Protect/Detect/Respond/Recover.
9. Type of case versus order/urgency based on risk and confidence.
10. When impact, uncertainty, authority, skill, legal/privacy, or service thresholds require it.
11. Relevant evidence/context with known source, timeliness, confidence, and handling.
12. They can be shared, reassigned, stale, or context-dependent and need corroboration.
13. File/content analysis ecosystem; vendor research/intelligence/services; external multi-provider aggregation.
14. Correct malicious detection; benign flagged; relevant malicious behavior missed.
15. Defined time/data, validated hits, contextual pivots, reproducible evidence, and a broader hypothesis/improvement.
16. Endpoint and supported broader telemetry plus entities/observables used by analytics/investigation.
17. Linking records believed to describe related activity across sources.
18. Tracing process/activity relationships and associated evidence.
19. Missing/incorrect telemetry, time, identity, and inferred relationships can mislead.
20. Cross-source correlation/investigation/response beyond endpoint telemetry alone.
21. Target/context validation, evidence preservation, authority, impact, reversibility, and a verification plan.
22. Support/version, package/profile, connectivity, permissions, staging, health, upgrades, response behavior, rollback, and removal.
23. Agents may be stale, disconnected, unhealthy, misassigned, or absent from ephemeral expected assets.
24. Versioned integrations/content packs and related supported automation content.
25. Defined inputs, least privilege, idempotency, approvals, retries/timeouts/errors, audit, tests, monitoring, and rollback.
26. Relevant commands/results, evidence, notes, decisions, files, tasks, and collaboration without leaking secrets.
27. Normalize, deduplicate, enrich, score source/confidence, observe handling, expire, and audit use.
28. A script defines reusable automation; a job schedules execution.
29. Least-privilege credentials/secrets, endpoints, permissions, versions, network, rate limits, and audit.
30. Broad ingestion, analytics/detection, incident/hunt, automation/integration, response, and SecOps management.
31. Source/schema/time/entity quality, expected events, completeness, retention/cost/privacy, and gap alerting.
32. Observables/evidence; affected systems/resources; human/nonhuman identities/context.
33. Text, time range, data sources, parameters/assumptions, result counts, pivots, and conclusion.
34. Compromise-associated observable; behavior rule; multi-event/context relationship rule.
35. Objective, prerequisites, logic, exceptions, severity/mapping, response, owner/version, positive/negative tests, and tuning evidence.
36. Disruptive actions such as isolation, blocking, disabling accounts, or deleting/quarantining data under policy.
37. It is not 86% raw correct; it is a scaled threshold across forms.
38. Current public datasheet/handbook omit them; live registration is authoritative.
39. Two years, subject to current recertification rules.
40. Active datasheet, live product docs/path, registration details, handbook, versions, and policies.

## Final readiness checklist

- [ ] I can design SOC roles, permissions, telemetry governance, compliant evidence, and decision-centered dashboards/reports.
- [ ] I distinguish AI/ML value and risk and validate every generated claim against evidence.
- [ ] I run an incident under current NIST guidance and preserve older lifecycle vocabulary for exam recognition.
- [ ] I evaluate intelligence/indicators, TP/FP/FN tradeoffs, and conduct a reproducible basic hunt.
- [ ] I explain Cortex XDR sensors, stitching, causality, WildFire, behavioral analytics, entities, response, and agent lifecycle.
- [ ] I design XSOAR integrations, TIM, playbooks, War Room evidence, scripts, jobs, and case flow safely.
- [ ] I explain XSIAM ingestion, content packs, queries, IOC/BIOC/correlations, automation, and response.
- [ ] I completed all scenarios/labs with synthetic data, evidence, failure cases, authority, and improvement.
- [ ] I reject leaked/live exam questions and unapproved uploads to public intelligence services.
- [ ] I rechecked the July 2026 datasheet, Cortex docs, handbook, and registration before purchase.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Start with the blueprint and official digital path, then choose product documentation and vendor-neutral incident/detection material for measured gaps. Verify product version, licensing, and access before investing time.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Security Operations Professional page](https://www.paloaltonetworks.com/services/education/palo-alto-networks-secops-professional) | Public | 10–15 minutes | Current credential, datasheet, learning path, and registration |
| [July 2026 datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/secops-professional-datasheet.pdf) | Public PDF | 45–75 minutes | Canonical five-domain scope and named workflows/features |
| [Certification Handbook](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/ebooks/panw-certification-handbook.pdf) | Public PDF | 30–45 minutes | Scoring, ESL, retakes, validity, renewal, integrity, and results |
| [Official digital learning](https://learn.paloaltonetworks.com/learn) | Free account/login may be required | 30 minutes planning; modules vary | Follow the certification-page learning plan and record live durations |
| [Cortex XDR documentation](https://docs.paloaltonetworks.com/cortex/cortex-xdr) | Public | 12–20 hours selected topics | Access/logs, agents, incidents, causality, hunting, analytics, response, reports |
| [Cortex XSOAR documentation](https://docs.paloaltonetworks.com/cortex/cortex-xsoar) | Public | 10–18 hours selected topics | Integrations, TIM, playbooks, War Room, scripts/jobs, cases, Marketplace |
| [Cortex XSIAM documentation](https://cortex-docs.paloaltonetworks.com/) | Public | 12–20 hours selected topics | Ingestion, content, incidents, analytics, BIOCs/correlations, queries, automation |
| [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | Public primary guidance | 3–5 hours | Current incident response and CSF 2.0 lifecycle integration |
| [MITRE ATT&CK](https://attack.mitre.org/) | Public | 4–8 hours plus mapping lab | Behavior, data sources, mitigations, groups/software, and hunt/detection mapping |
| [Palo Alto Networks Unit 42](https://unit42.paloaltonetworks.com/) | Public | 3–8 hours selected reports | Current threat research and evidence-led case studies |
| [Palo Alto Networks YouTube](https://www.youtube.com/@PaloAltoNetworks) | Free video | 4–10 hours selected current content | Visual Cortex/SOC demonstrations; reconcile UI and licensing with docs |
| [O'Reilly Practical Security Automation and Testing](https://www.oreilly.com/library/view/practical-security-automation/9781098143160/) | Paid; broader/vendor-neutral | 10–18 hours selected chapters/labs | Automation design, APIs, testing, safety, and repeatable workflows |

No current official practice exam, MeasureUp product, or Whizlabs product explicitly aligned to the July 2026 Security Operations Professional blueprint was verified. Use current official documentation and original synthetic investigations instead of unsourced question banks.
