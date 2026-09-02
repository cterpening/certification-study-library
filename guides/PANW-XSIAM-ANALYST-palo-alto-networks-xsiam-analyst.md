---
exam_code: PANW-XSIAM-ANALYST
vendor_id: palo-alto-networks
official_blueprint: https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/XSIAMAnalyst-datasheet.pdf
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Palo Alto Networks Certified XSIAM Analyst Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live certification page, August 2025 datasheet, July 2025 certification handbook, Cortex XSIAM documentation, and public incident/detection sources were checked September 2, 2026. This does not guarantee that every explanation is error-free or remains current. The [official page](https://www.paloaltonetworks.com/services/education/palo-alto-networks-xsiam-analyst) and [datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/XSIAMAnalyst-datasheet.pdf) are authoritative.

**Current baseline:** alert/detection 19%; incident response 20%; automation/playbooks 15%; XQL 14%; endpoint management 12%; threat intelligence/ASM 20%; August 2025 datasheet<br>
**Exam contract:** specialist-level English Pearson VUE certification. The current handbook uses an 860 passing score on a 300–1000 scaled range and provisional results. The datasheet does not state item count, base duration, price, or formal experience; verify registration.<br>
**Experience boundary:** job-ready XSIAM analysis: prioritization, investigations, playbooks, XQL, endpoints, intelligence, exposure, reports, and compliance. The official page also recommends the instructor-led Cortex XSIAM for Investigation and Analysis course.<br>
**Validity and renewal:** two years under the July 2025 handbook, subject to current pathway rules.<br>
**Upcoming change:** no retirement or dated replacement was found September 2, 2026. XSIAM interface, content, automation, and incident scoring are volatile; verify current documentation.<br>
**Integrity:** actual exam content is confidential. This guide uses the published blueprint, original checks, synthetic data, and public docs only.

## How to use this guide

Prepare by completing investigations, not by recognizing screen labels. For each alert, record source, analytic logic, evidence, score/priority, grouping/stitching, incident domain, featured fields, affected entities, timeline/causality, queries, playbook tasks, response, and outcome.

Use this loop:

1. prove data/source health and state a hypothesis;
2. validate alert evidence and prioritize from confidence plus impact;
3. query/pivot across normalized XDM data, endpoints, identity, intelligence, and attack surface;
4. use playbooks/native actions under least privilege and explicit approval;
5. close with tuned content, recovered state, report, and prevention/detection improvement.

Use synthetic or approved telemetry. Avoid submitting proprietary files/indicators to public services and never run endpoint response on production without authorization.

> **About related items:** A `Related item:` callout adds operational, governance, implementation, or lifecycle context. It helps turn an objective into reliable work but is not claimed as verbatim exam scope.

## Blueprint map

| Domain | Weight | Evidence of readiness |
|---|---:|---|
| 1. Alerting and Detection | 19% | Explain analytic sources and configure defensible prioritization |
| 2. Incident Handling and Response | 20% | Build and act on an evidence-led incident story |
| 3. Automation and Playbooks | 15% | Use tasks/sub-playbooks/error handling/playground safely |
| 4. Data Analysis with XQL | 14% | Query XDM data reproducibly and schedule controlled analytics |
| 5. Endpoint Security Management | 12% | Validate policy/agent/activity and bound response actions |
| 6. Threat Intelligence and ASM | 20% | Govern indicators/verdicts/relationships/assets/external threats |

## 1. Alerting and detection processes — 19%

Analytic alerts can arise from correlation logic, endpoint agent prevention/detection, behavioral indicator (BIOC) rules, IOC matches, and other supported XSIAM analytics/content. For any type, identify required source/schema, logic/model/content version, trigger, entities/artifacts, severity, action, exclusions, and test case.

An IOC is an observable associated with suspected malicious activity, such as hash/domain/IP/URL. A BIOC describes a behavioral pattern using event fields/relationships. Correlations connect multiple events/conditions/context. Agent alerts come from endpoint prevention/analytics. None is automatically an incident verdict.

Incident scoring combines alert and context signals according to current platform logic. Alert starring marks analyst attention/importance. Featured fields surface fields selected as investigation-relevant. Incident domains categorize operational/security area. Custom prioritization applies organization context and rules. Verify current calculation/field behavior rather than reverse-engineering a static formula.

Priority should combine confidence, asset/user/data criticality, exposure, privilege, scope, behavior, and business impact. Preserve the reason for any manual/custom override and measure whether priority routes cases appropriately.

> **Related item:** A high-severity alert on an expired lab asset and a medium alert on a domain controller should not be routed only by vendor severity. Context is part of detection operations.

## 2. Incident handling and response — 20%

Incidents are created by grouping/correlation of alerts under platform rules or analyst action. Alert grouping places related alerts into one incident based on grouping logic. Data stitching links related events/entities across sources to build context. Grouping manages alert units; stitching enriches the underlying evidence relationships.

Review raw evidence before conclusions: source/time, event fields, process command/path/hash/signature, parent/child causality, identity/session, endpoint/cloud/network activity, prevalence/intelligence, and missing data. Causality chain shows activity relationships; timeline orders events; neither eliminates source validation.

Forensics collects/deeply examines endpoint evidence under licensing/permissions. ITDR detects/investigates identity threats through authentication, account, privilege, behavior, and endpoint relationships. Treat both as scoped evidence with privacy/retention/chain-of-custody implications.

Identify and analyze using hypothesis, scope, ATT&CK behavior, affected users/assets, entry/lateral/persistence/action evidence, impact, and confidence. Respond through the least disruptive effective action: isolate endpoint, kill/block/quarantine, revoke identity/session, block indicator, run scan, collect file, or orchestrate another system as supported. Confirm authority, evidence preservation, target, reversibility, dependencies, and post-action proof.

Native automation can execute platform response without a separate external workflow. Begin with enrichment/notification; gate disruptive action by evidence/confidence and policy. Hunt leads/IOCs across a defined time/data range, pivot to behavior and entities, record queries/results, and turn validated patterns into durable content.

Incident context can include score/domain, starred alerts, featured fields, assets/users, alert sources, artifacts, chronology, causality, intelligence, vulnerabilities/exposure, actions, and playbook status. Missing evidence should lower confidence, not disappear from the narrative.

## 3. Automation and playbooks — 15%

A playbook expresses incident workflow through task types such as automated commands/scripts, conditions, data collection/transformation, and manual analyst actions as currently supported. Sub-playbooks encapsulate reusable workflows. Define inputs/outputs, context keys, permissions, owners, timeouts, and version compatibility.

Error handling needs alternate paths for missing data, integration failure, rate limit, timeout, partial completion, and rejected approval. Design idempotency so retries do not block twice, duplicate tickets, or destroy evidence. Record actions and results in the incident audit trail.

The playground is a non-production/testing workspace for developing and trying commands/automation/content without using an active case as the first test. It is not permission to call production integrations or use sensitive data casually. Use test instances/fixtures, expected outcomes, cleanup, and change review.

> **Related item:** Automation is executable policy. Apply version control, peer review, test fixtures, staged rollout, monitoring, rollback, and secret scanning just as you would for application code.

## 4. Data analysis with XQL — 14%

Cortex Data Models (XDMs) normalize source-specific events into consistent fields/entities so queries and analytics work across products. Normalization can lose or reinterpret detail; retain access to raw/source fields and validate mappings, time, identity, and asset resolution.

XQL queries datasets through pipeline-style stages and operators defined by current XSIAM documentation. Know how to select a dataset/time range, filter early, transform/alter fields, aggregate, sort, limit, join/enrich where supported, and present results. Exact syntax/operators evolve; use the current schema browser/helper.

Start every query with question, data prerequisites, time zone/range, entity/field definitions, and expected positive/negative cases. Filter early for performance/cost, avoid unbounded output, and validate null/missing/type values. Aggregation can hide individual evidence; preserve drill-down keys.

The Query Library provides saved/provider queries; XQL Helper assists syntax/schema/fields; scheduled queries run at defined intervals for recurring search/detection/report use. Review borrowed queries for dataset/schema/version, parameterize safely, assign owner, choose lookback wider than ingestion delay where needed, deduplicate repeated matches, monitor failures, and expire obsolete schedules.

> **Related item:** Store a hunting query with objective, ATT&CK mapping, data contract, expected runtime/volume, test fixtures, result interpretation, and revision history—not only query text.

## 5. Endpoint security management — 12%

Endpoint profiles/policies define prevention, agent behavior, extensions/modules, and configuration by supported OS/workload/group. Validate hierarchy/assignment, license, supported version, content, exclusions, enforcement mode, and expected effective policy. Exceptions need owner, justification, scope, compensating control, and expiry.

Agent operational status includes installed/connected/protected/content/version/policy and other current health states. Determine expected inventory, last seen, network/proxy, service/process, tenant association, upgrade state, and policy. An installed but disconnected/outdated/misassigned agent is not effective coverage.

Monitor process, file, network, user, prevention, health, and policy activity with appropriate privacy/retention. Response options in the blueprint include:

- Live Terminal for authorized remote investigation/commands;
- isolation to restrict network communication while preserving management channels;
- malware scan for supported inspection/remediation;
- endpoint file retrieval for evidence.

Each action needs target verification, least privilege, evidence/custody, user/business impact, time limit, approvals, and exit criteria. Retrieved files are sensitive/untrusted evidence; store/analyze safely.

## 6. Threat Intelligence Management and ASM — 20%

Import indicators from vetted feeds/manual/API sources with type, source reliability, confidence, classification/handling, first/last seen, expiration, relationships, and tenant relevance. Normalize/deduplicate and test actions. An imported feed is not automatically authoritative.

Artifacts are observed entities; verdicts classify them under provider/analyst logic; reputation aggregates history/context; impact estimates what the artifact/activity did or could do in this environment. Validate source/time/evidence and record analyst verdict overrides. Verdict management should preserve reason, author, time, scope, downstream propagation, rollback, and review.

Indicator rules can detect or prevent matching activity. Choose exact/domain/wildcard and other supported match semantics carefully, validate shared infrastructure, observe first where risk permits, and expire stale blocks. Indicator relationships connect resolutions, files, URLs, campaigns, assets, and activity; relationships support pivots but do not prove causation.

Asset inventory should reconcile discovered internet-facing assets with authoritative CMDB/cloud/DNS/account ownership, business purpose, exposure, certificate/software, risk, and lifecycle. Unknown does not automatically mean malicious; it means ownership and intended exposure must be established.

The Attack Surface Threat Response Center uses current external exposure/threat context to identify, assess, research, assign, and remediate emerging risks. Attack-surface rules define detection/prioritization/workflow conditions. Validate asset ownership and finding accuracy, integrate tickets/owners, track SLA/exceptions, verify remediation externally, and suppress only with reason/expiry.

> **Related item:** ASM views the organization from outside; XSIAM internal telemetry shows activity. Correlating exposure with exploit/identity/runtime evidence produces better priority than either alone.

## Integrated scenarios

### Suspicious PowerShell chain

Group agent/BIOC/IOC/correlation alerts into an incident, validate process causality/timeline and identity context, query XDM data, enrich indicators, use a playbook with approval, isolate/retrieve safely, and tune a correlation. Document false-positive alternatives and recovery.

### Exposed remote-management host

ASM discovers an internet service. Validate ownership and exposure, correlate endpoint/identity/vulnerability events, calculate custom priority, hunt related activity, assign remediation, verify externally, and decide whether exposure became incident.

### Feed-driven alert storm

Trace feed source, indicator type/relationship/verdict/expiry and alert source/grouping/stitching. Use XQL to measure prevalence, validate shared services, change verdict/rule carefully, and update playbook error/rate handling without creating a false-negative gap.

## Hands-on labs

1. **Alert-source matrix:** model agent, IOC, BIOC, and correlation alerts with data/logic/evidence/action/test cases.
2. **Prioritization:** score/star/feature/domain synthetic incidents, configure context-based priority, and evaluate routing against known outcomes.
3. **Investigation:** build forensics/ITDR/causality/timeline evidence, distinguish grouping from stitching, and perform an approved response with verification.
4. **Playbook:** implement synthetic enrichment, conditions, sub-playbook, approval, action, timeout/rate/error branches, audit, and rollback; test first in a playground.
5. **XQL workbook:** write ten queries using XDM fields for filter/transform/aggregate/pivot; test nulls, time, schema, volume, and scheduled-query overlap.
6. **Endpoint management:** validate profiles/effective policy and agent health, simulate stale version/content, then document live terminal/isolation/scan/retrieval controls.
7. **TIM lifecycle:** import synthetic indicators, normalize/deduplicate/enrich, manage verdict/relationships/expiry, and create observation-before-prevention rules.
8. **ASM workflow:** reconcile synthetic external assets to owners, research an emerging threat, prioritize, ticket, remediate, verify externally, and expire an exception.

## Original readiness checks

1. Which analytic alert sources does the blueprint name?
2. How do IOC, BIOC, and correlation logic differ?
3. What context should influence priority beyond severity?
4. What do starring, featured fields, and incident domains contribute?
5. Why preserve custom-priority rationale?
6. How does alert grouping differ from data stitching?
7. What evidence belongs in a causality/timeline review?
8. How do forensics and ITDR differ?
9. What must precede a native response action?
10. What makes an IOC hunt reproducible?
11. What can missing incident context mean?
12. Which task concerns belong in a playbook?
13. Why use sub-playbooks?
14. What does idempotency prevent?
15. What is the playground for and not for?
16. What does XDM provide?
17. Why retain raw/source fields?
18. What belongs in an XQL query contract?
19. Why filter early?
20. What risks accompany scheduled queries?
21. What should be reviewed in a Query Library query?
22. What must endpoint policy validation prove?
23. Why is installed agent not equivalent to coverage?
24. What controls apply to Live Terminal?
25. How should retrieved files be handled?
26. Which metadata belongs on imported indicators?
27. How do artifact, verdict, reputation, and impact differ?
28. What belongs in analyst verdict management?
29. Why can an indicator prevention rule cause damage?
30. Do indicator relationships prove causation?
31. How should an ASM asset be validated?
32. What is the Threat Response Center workflow for?
33. What belongs in an attack-surface rule exception?
34. Why correlate ASM and internal telemetry?
35. Which two domains each weigh 20%?
36. What does scaled 860 not mean?
37. Why are count/base duration/price absent here?
38. How long is validity under the checked handbook?
39. Why must XQL/UI behavior be rechecked?
40. What must you verify before scheduling?

## Answer key

1. Correlations, XDR Agent, BIOCs, and IOCs.
2. Observable match; behavior logic; multi-event/context relationship logic.
3. Confidence, user/asset/data criticality, privilege, exposure, scope, behavior, and business impact.
4. Analyst attention, investigation-relevant context, and operational categorization.
5. So routing/overrides are explainable, testable, auditable, and removable.
6. It combines alert units into incidents; stitching links underlying related data/entities.
7. Raw source/time, processes/commands/files/network, identities, assets, relationships, intelligence, missing data.
8. Endpoint evidence collection/analysis versus identity-threat evidence/response.
9. Target/evidence validation, authority, preservation, impact, reversibility, and success/exit criteria.
10. Defined question/time/data/query, validated hits, pivots, recorded results, and conclusion.
11. Absent collection, parsing, identity, retention, source, or evidence—not absence of attack.
12. Inputs/outputs, tasks/conditions, permissions, timeouts/retries/errors, approvals, evidence, monitoring, rollback.
13. Reuse/version/test common workflows and reduce duplication.
14. Duplicate harmful effects when actions retry or resume.
15. Safe content/command development; not unrestricted use of production systems/sensitive data.
16. Normalized consistent schemas/entities across sources.
17. Normalization may lose/mis-map detail needed to validate conclusions.
18. Question, sources/schema/time, filters, null/type handling, expected cases, performance, output interpretation.
19. Reduce scanned data/cost/runtime and make intent clearer.
20. Overlap/gaps from lookback/cadence/delay, repeated actions, schema change, failure, stale ownership, resource cost.
21. Dataset/schema/version, time, parameters, assumptions, performance, permissions, expected results.
22. Correct target assignment/effective profile, supported/license/content state, action/exclusions, and safe test outcome.
23. It may be disconnected, stale, unhealthy, misassigned, or not represent expected assets.
24. Least privilege, approval, target, command logging, time, user/business impact, and exit/cleanup.
25. As sensitive, potentially malicious evidence with custody, access, storage, and sandbox controls.
26. Type/value, source/reliability, confidence, handling, time, relationships, relevance, verdict/action, expiry.
27. Observable; classification; accumulated context/history; environment consequence.
28. Evidence, source, author/time, reason, scope, propagation, rollback, review/expiry.
29. Shared/reassigned infrastructure and weak matches can block legitimate business activity.
30. No; they support hypotheses and pivots needing evidence.
31. Reconcile discovery to DNS/cloud/CMDB/account and establish owner, purpose, exposure, lifecycle, and accuracy.
32. Find, research, prioritize, assign, remediate, and verify emerging external threats/exposures.
33. Owner, reason, scope, compensating control, approval, expiry/review, and verification.
34. Exposure plus actual activity/identity/runtime context yields stronger risk priority.
35. Incident Handling/Response and Threat Intelligence/ASM.
36. It is not 86% raw correct; it is a scaled threshold across forms.
37. Current public datasheet/handbook omit them; live registration is authoritative.
38. Two years, subject to current recertification rules.
39. Product features, data schemas, syntax/helpers, scoring, and interface evolve.
40. Active datasheet, current XSIAM docs/path/course, registration, handbook, tenant/version/licenses, and policies.

## Final readiness checklist

- [ ] I distinguish agent/IOC/BIOC/correlation alerts and can configure context-led priority.
- [ ] I investigate grouped/stitched evidence using forensics, ITDR, causality, timeline, context, and safe response.
- [ ] I design playbooks/sub-playbooks/error handling/playground tests with least privilege and idempotency.
- [ ] I use XDM/XQL/Library/Helper/schedules through documented queries and data-health checks.
- [ ] I validate endpoint policies, agent health/activity, and authorized response controls.
- [ ] I manage indicator import, verdict, relationships, rules, lifecycle, and false-positive risk.
- [ ] I reconcile ASM assets, Threat Response Center findings, remediation, rules, and external verification.
- [ ] I completed all scenarios/labs with synthetic data, audit evidence, failure paths, and rollback.
- [ ] I reject live/leaked questions and unauthorized public intelligence uploads.
- [ ] I rechecked the August 2025 datasheet, current docs/course/path, handbook, and registration before purchase.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Start with the blueprint and official XSIAM path/course, then use documentation and synthetic investigations for measured gaps. Record tenant/release because XQL schemas, content, and UI evolve.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [XSIAM Analyst certification page](https://www.paloaltonetworks.com/services/education/palo-alto-networks-xsiam-analyst) | Public | 10–15 minutes | Current credential, datasheet, official learning routes, registration |
| [August 2025 datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/XSIAMAnalyst-datasheet.pdf) | Public PDF | 60–90 minutes | Canonical six-domain weighted blueprint |
| [Certification Handbook](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/ebooks/panw-certification-handbook.pdf) | Public PDF | 30–45 minutes | Scoring, ESL, results, retakes, validity, renewal, integrity |
| [Official digital learning](https://learn.paloaltonetworks.com/learn) | Free account/login may be required | 30 minutes planning; modules vary | Follow the certification-page path and record live durations |
| [Cortex XSIAM: Investigation and Analysis](https://www.paloaltonetworks.com/services/education/ilt-xsiam-investigation-analysis) | Paid instructor-led/authorized partner route | 2 days | Officially recommended hands-on analyst workflow course; duration published on the live course page |
| [Cortex XSIAM documentation](https://cortex-docs.paloaltonetworks.com/) | Public | 25–40 hours selected topics/labs | Alerts/incidents, playbooks, XQL/XDM, endpoint, TIM/ASM, reports |
| [MITRE ATT&CK](https://attack.mitre.org/) | Public | 4–8 hours plus mapping labs | Behavior, data sources, mitigations, detection and hunt context |
| [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | Public primary guidance | 3–5 hours | Current incident-response lifecycle and improvement context |
| [Unit 42 Research](https://unit42.paloaltonetworks.com/) | Public | 4–8 hours selected reports | Current threats, indicators, behavior, and investigations |
| [Palo Alto Networks YouTube](https://www.youtube.com/@PaloAltoNetworks) | Free video | 4–10 hours selected current XSIAM demos | Visual workflows; validate release/UI against docs |
| [O'Reilly Practical Security Automation and Testing](https://www.oreilly.com/library/view/practical-security-automation/9781098143160/) | Paid; vendor-neutral | 10–18 hours selected chapters/labs | Safe automation, APIs, testing, secrets, repeatability |

No current official practice exam, MeasureUp product, or Whizlabs product explicitly aligned to this exact XSIAM Analyst blueprint was verified. Prefer the official course/path and original tenant/synthetic-data labs over unsourced question banks.
