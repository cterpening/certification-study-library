---
exam_code: NSE-7-SECURITY-OPERATIONS
vendor_id: fortinet
official_blueprint: https://training.fortinet.com/local/staticpage/view.php?page=security_operations_architect_exam
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-10-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-10-28
---

# Fortinet NSE 7 in Security Operations Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live NSE 7 Security Operations and Security Operations 7.6 Architect pages, current FortiSIEM/FortiSOAR documents, and public NIST/MITRE guidance were checked October 28, 2026. Fortinet's pages remain authoritative.

**Current baseline:** Security Operations 7.6 Architect, using FortiSOAR 7.6 and FortiSIEM 7.3. Published domains are SOC Concepts and Frameworks; Detection Capabilities; SOAR Incident Handling and Threat Hunting; and SOAR Playbook Development. Fortinet publishes no weights for these domains; do not invent them.<br>
**Exam contract:** 35–40 questions, 75 minutes, English, Pearson VUE, pass/fail. It includes operational scenarios, incident analysis, integrations, and troubleshooting.<br>
**Delivery:** Since September 21, 2026, NSE 7 exams are available only at Pearson VUE-authorized test centers; OnVUE remote delivery ended. Check current local availability when scheduling.<br>
**Certification contract:** This guide covers the required NSE 7 Security Operations exam, not the credential alone. NSE 7 in Security Operations also requires NSE 4 FortiOS and either NSE 5 Security Operations or NSE 6 Security Operations; the NSE 7 exam must be passed within two years of the last prerequisite. The credential is active for two years under the official recertification policy; the current track page's validity sentence is malformed, so verify the credential record for its exact expiration date.<br>
**Experience boundary:** Fortinet recommends one year of network-security experience and six months of SOC experience. The scenario depth still requires practical SIEM/SOAR work.<br>
**Upcoming change:** No additional retirement or dated replacement was announced as of October 28, 2026. FortiSIEM is listed at 7.3 even though later product documentation may exist; study the exam baseline and note later-version differences.<br>
**Integrity:** Never use customer incidents or unauthorized exam content as study material. Use sanitized synthetic evidence and official sample questions only for format/scope.

## How to use this guide

Study each objective as a defensible incident workflow: telemetry source, collection/parsing/normalization, correlation, alert, triage, enrichment, scope, evidence, containment, eradication, recovery, communication, and improvement. State confidence and missing evidence. A closed ticket is not proof that the threat was removed.

Use an owned or explicitly authorized lab with synthetic identities, endpoints, logs, indicators, and harmless emulation. Record FortiSIEM/FortiSOAR versions, content/connector versions, time zone, parser/rule/playbook revision, and cleanup. Never transmit real secrets or sensitive records to a training integration.

> **About related items:** A `Related item:` callout adds detection-engineering, incident-response, operations, governance, or lifecycle context. It is useful practice but not claimed as verbatim blueprint text.

## Blueprint map

| Domain | Published weight | Evidence of readiness |
|---|---:|---|
| SOC concepts and frameworks | Not published | Explain adversary behavior and a resilient Fortinet SOC architecture using an incident framework |
| Detection capabilities | Not published | Build, tune, validate, and investigate FortiSIEM queries/rules with measurable coverage |
| SOAR incident handling and threat hunting | Not published | Run governed hunts/cases, workload, evidence, collaboration, containment, and learning |
| SOAR playbook development | Not published | Build least-privilege connector/playbook flows with Jinja, tests, error handling, and debugging |

## 1. SOC concepts and frameworks

### Analyze incidents and adversary behavior

Separate event, alert, incident, and problem. Establish what happened, affected entities, first/last seen, current activity, business impact, confidence, evidence gaps, and the next reversible action. Build a timeline from raw evidence and preserve provenance, time zone, and chain of custody where applicable.

Use MITRE ATT&CK to describe observed tactics and techniques, choose relevant data sources, find visibility gaps, and communicate coverage. A technique mapping is a hypothesis aid, not attribution or proof. Identify attack vectors such as exposed services, phishing, credential misuse, vulnerable applications, supply chain, removable media, trusted relationships, and cloud/API abuse without forcing evidence into a preferred narrative.

The NIST incident-response lifecycle supports preparation; detection/analysis; containment, eradication, and recovery; and post-incident improvement. Current organizational guidance may use different phase names. What matters is clear authority, evidence, decisions, communications, recovery criteria, and learning.

> **Related item: confidence language.** Distinguish fact, corroborated inference, working hypothesis, and unknown. Record what would confirm or falsify each important conclusion.

### Explain Fortinet SOC architecture

Map data producers, collectors, parsers, normalization/enrichment, FortiSIEM workers/supervisors/storage, analytics/rules, incidents, FortiSOAR connectors/playbooks/cases, FortiAnalyzer/FortiEDR/FortiGate and other Fabric integrations, identity/asset/vulnerability context, ticketing, threat intelligence, notifications, and evidence storage.

Design for source volume, burst, EPS, retention, search latency, parser/content change, network segmentation, encryption, certificate and secret rotation, RBAC, tenancy, HA/DR, backups, time, monitoring, and degraded operation. Reconcile expected sources/assets with observed data and alert on collection silence.

> **Related item: control-plane blast radius.** SIEM/SOAR accounts can read sensitive data and isolate systems. Separate authoring, approval, execution, and emergency disable; protect service identities and audit every action.

## 2. Detection capabilities

### Build useful FortiSIEM queries

Begin with a behavior hypothesis and required fields. Confirm time window/time zone, parser and normalized field mapping, entity identity, filters, aggregation/grouping, sequence, joins, thresholds, baseline, exclusions, and result limits. Search raw events when normalized fields are missing or misleading, then fix the parser rather than embedding permanent workarounds.

A hunt query optimized for exploration may be too expensive or noisy for continuous detection. Measure scanned volume, execution time, result cardinality, false-positive drivers, and missing telemetry. Save a reproducible query with owner, purpose, ATT&CK mapping where appropriate, data prerequisites, version, and validation evidence.

### Engineer and validate incident rules

Define rule scope, triggering logic, grouping/entity, threshold/window, severity, incident attributes, deduplication/suppression, clear condition, notification/automation, and exception governance. Test true positive, near miss, benign control, boundary/time cases, duplicate events, delayed/out-of-order data, parser changes, and source outage.

Analyze an incident by pivoting to related users, hosts, IPs, processes, assets, vulnerabilities, and timeline. Verify the exact events that satisfied the rule, then expand carefully. Tuning can adjust logic, threshold, grouping, context, or data quality; global exclusions should be a last resort.

> **Related item: detection as code.** Version rules, queries, parsers, tests, fixtures, approvals, deployments, monitoring, and rollback. Coverage without validation is an assertion.

## 3. SOAR incident handling and threat hunting

### Hunt from a falsifiable hypothesis

State the behavior, population, time range, data sources, expected evidence, alternate explanations, and decision criteria. Iterate broad-to-narrow while recording queries, results, pivots, gaps, and negative findings. Absence of evidence only has meaning when collection, parser, retention, and query coverage are known.

Turn a confirmed hunt into an engineered detection only after testing representativeness, performance, false positives, ownership, runbook, and response. Track whether the new analytic would have detected the original activity and how quickly.

### Manage incidents as controlled cases

In FortiSOAR, preserve case ownership, severity/priority, status, SLA, evidence, tasks, notes, relationships, approvals, communications, and closure criteria. Queues distribute categories of work; shifts model staffing/availability. Test reassignment, escalation, backlog, handoff, leave, and after-hours behavior.

War rooms centralize authorized collaboration and action context. They do not replace evidence storage, decision logs, or approved external communications. Restrict membership and integrations; sanitize sensitive data and preserve an export where policy requires.

Containment actions—block indicator, disable identity, isolate endpoint, quarantine email, or change network policy—need evidence threshold, authority, scope, expected impact, expiry, monitoring, rollback, and exception. Simulation mode can validate flow without executing destructive actions, but connector/API test coverage is still required.

> **Related item: human-in-the-loop design.** Require approval when confidence is low, impact is high, an action is difficult to reverse, or legal/business coordination is required. Automation should speed judgment, not bypass it.

## 4. SOAR playbook development

### Design playbooks for predictable outcomes

Define trigger, inputs/schema, preconditions, enrichment, decision points, actions, approvals, outputs, logging, timeout, retry/backoff, pagination/rate limit, idempotence, partial failure, compensation/rollback, and terminal states. Keep enrichment separate from containment where practical.

Connectors hold or use trust to external systems. Use dedicated least-privilege identities, managed secrets, certificate validation, network restrictions, documented scopes, rotation, health checks, and audit. Test expired/revoked credentials, permission loss, unreachable service, malformed response, quota, rate limit, duplicate action, and partial success.

Jinja filters transform values and collections for supported playbook logic. Treat all input as untrusted: validate types, missing/null values, encodings, dates, escaping, list/dictionary shape, and output schema. Do not log secrets while debugging.

### Debug systematically

Reproduce with a sanitized test incident and known inputs. Identify the failing step and compare inputs, expression/filter output, connector request/response, permissions, endpoint/certificate, timeout, rate limit, downstream state, and playbook logs. Distinguish design error from connector/content version, external API change, or bad incident data.

Use unit-like tests for transformations, connector mocks or safe test tenants, integration tests, end-to-end simulation, canary promotion, and post-deployment monitoring. Roll back the playbook/content version rather than editing production blindly.

> **Related item: automation observability.** Track success/failure/timeout/approval/retry rates, execution duration, external API latency, action volume, rollback outcomes, and business impact—not only whether a playbook started.

## Integrated scenarios

### Suspected credential compromise

Correlate authentication, endpoint, VPN, identity, cloud, and network evidence. Build a timeline and ATT&CK mapping, query related accounts/devices/IPs, scope assets, open a case, enrich indicators, require approval, revoke sessions or disable the account, isolate only where warranted, recover, monitor, and convert learning into a tested rule.

### Ransomware-like endpoint activity

Synthetic telemetry shows suspicious execution, file changes, and outbound traffic. Verify parser/sequence, correlate FortiEDR and network events, distinguish simulation from real impact, preserve evidence, isolate safely, block validated indicators, search peers, coordinate restoration, and measure whether prevention and playbooks worked.

### Collection blind spot

A critical segment produces no events after a maintenance window. Compare expected inventory and last-seen, collector/network/time/parser/permission/storage state, source-local logs, queue/backpressure, and HA. Restore telemetry before claiming no malicious activity, and add silence detection and ownership.

## Hands-on labs

Use synthetic data and authorized systems only. Never run malware or disruptive containment in production.

1. Draw a resilient FortiSIEM/FortiSOAR architecture with data, trust, management, execution, HA/DR, and telemetry-silence paths.
2. Ingest a safe synthetic dataset; verify raw-to-normalized fields, time, entities, parser behavior, retention, and source health.
3. Build three FortiSIEM queries: behavior hunt, entity timeline, and coverage-gap search; record performance and evidence limits.
4. Build and validate an incident rule with positive, near-miss, benign, delayed, duplicate, and missing-source tests.
5. Manage a synthetic incident through queue, shift, case, tasks, evidence, war room, approvals, closure, and lessons learned.
6. Create an enrichment-only playbook with two connectors; handle missing value, revoked credential, timeout, rate limit, and partial response.
7. Add an approval-gated reversible containment action, expiry, verification, and rollback; first exercise simulation mode.
8. Manipulate nested synthetic values with Jinja; test nulls, lists, dates, escaping, wrong schema, and secret redaction.
9. Hunt a harmless ATT&CK-mapped simulation, document negative findings and gaps, and promote one result into a tested detection.
10. Restore from a simulated collector or playbook/content failure and validate monitoring, backlog, data continuity, and audit.

## Readiness checks and answers

These are original prompts, not Fortinet exam questions.

| # | Check | Concise answer |
|---:|---|---|
| 1 | Event versus alert versus incident? | Event is an observation; alert is analytic output; incident is a governed investigation/response record. |
| 2 | What starts incident analysis? | Known facts, affected entities, timeline, impact, confidence, evidence gaps, and next safe action. |
| 3 | What does ATT&CK provide? | A common behavior/technique model for analysis, data-source selection, coverage, and communication—not attribution proof. |
| 4 | Why map an attack vector? | To understand entry assumptions, required evidence, prevention, scope, and alternate paths. |
| 5 | What protects evidence quality? | Provenance, timestamps/time zone, integrity, access control, chain of custody where needed, and reproducible queries. |
| 6 | Core SOC architecture planes? | Collection/data, analytics, case/orchestration, management, execution, and evidence/reporting. |
| 7 | Why alert on missing logs? | A silent source creates a detection blind spot and makes negative findings unreliable. |
| 8 | What reconciles coverage? | Expected source/asset inventory versus observed current events, parser health, retention, and query access. |
| 9 | First query design step? | State a falsifiable behavior hypothesis and required data/fields. |
| 10 | Why inspect raw events? | Normalization may omit or mis-map decisive fields; raw data can prove the parser issue. |
| 11 | Hunt query versus detection rule? | Hunts favor exploration; production rules need predictable performance, precision, grouping, ownership, and response. |
| 12 | What must a rule specify? | Scope, logic, time/threshold, grouping, severity, dedup/suppression, outputs, actions, and clear conditions. |
| 13 | Essential rule tests? | True, near-miss, benign, boundary/time, duplicate, delayed, parser-change, and source-outage cases. |
| 14 | Why avoid global exclusions? | They can hide unrelated threats; improve data, context, or narrowly scoped logic instead. |
| 15 | What is detection-as-code? | Versioned rule/query/parser plus tests, review, deployment, monitoring, and rollback. |
| 16 | What makes a hunt falsifiable? | Explicit behavior, population/time, expected evidence, alternatives, and confirm/refute criteria. |
| 17 | Meaning of no results? | Only as strong as collection, parser, retention, permissions, query, and time-window coverage. |
| 18 | Queue versus shift? | Queue groups/routs work; shift models analyst availability and handoff timing. |
| 19 | War-room limitation? | Collaboration does not replace evidence integrity, formal decisions, or approved communications. |
| 20 | What gates containment? | Confidence, authority, impact, scope, reversibility, approval, expiry, monitoring, and rollback. |
| 21 | What does simulation mode prove? | Workflow/logic without production action; it cannot fully prove external permissions or real effects. |
| 22 | What makes a playbook idempotent? | Repeated execution recognizes prior state and avoids duplicating harmful actions. |
| 23 | How handle partial failure? | Record completed steps, prevent unsafe continuation, retry safely, compensate/roll back, and escalate. |
| 24 | Why dedicated connector identities? | Least privilege, attribution, rotation, monitoring, and revocation without disrupting people. |
| 25 | Connector fault tests? | Credential, permission, TLS, endpoint, timeout, malformed data, pagination, quota/rate, duplicate, and partial success. |
| 26 | Jinja safety boundary? | Validate untrusted type/schema/null/encoding and redact secrets before transformation or logging. |
| 27 | First debugging action? | Reproduce with sanitized known input and isolate the exact failing step. |
| 28 | What separates content from API failure? | Compare version, generated request, endpoint response, permissions, and a controlled known-good call. |
| 29 | Useful automation metrics? | Success/failure/timeout/retry/approval, duration, action volume, external latency, rollback, and impact. |
| 30 | When require a human? | Low confidence, high impact, difficult reversal, ambiguous scope, or legal/business coordination. |
| 31 | Does the blueprint publish weights? | No; do not invent them. |
| 32 | Current exam baseline? | 35–40 questions, 75 minutes, English; FortiSOAR 7.6 and FortiSIEM 7.3. |
| 33 | Does passing this exam alone earn NSE 7? | No; NSE 4 and NSE 5 or 6 Security Operations prerequisites must also meet the timing rule. |
| 34 | Why study the listed versions? | Exam scenarios target them; later product behavior can differ and should be labeled separately. |
| 35 | Safe lab evidence? | Synthetic, sanitized, authorized, versioned, reproducible, and cleaned up. |
| 36 | Forbidden preparation material? | Leaked, recalled, braindump, guaranteed-match, or unauthorized real exam content. |

## Final preparation

- Recheck exam and certification pages for baseline, availability, objective, prerequisite, policy, and renewal changes.
- Rebuild one query/rule and one playbook from blank state; test success, benign, malformed, timeout, unavailable-source, and rollback cases.
- Practice incident answers that separate facts, hypotheses, confidence, gaps, authority, reversible action, evidence, and learning.
- Keep FortiSIEM 7.3 and FortiSOAR 7.6 differences explicit when consulting newer documentation.

## Key terms and phrases

**SOC concepts and frameworks**

| Term or phrase | Meaning |
|---|---|
| [Tactic](#analyze-incidents-and-adversary-behavior) | An adversary objective, such as obtaining access to protected data. A technique describes a way to pursue that objective. |
| [Chain of custody](#analyze-incidents-and-adversary-behavior) | A record of who collected, possessed or transferred evidence, when it changed hands and how its integrity was protected. |
| [Containment](#analyze-incidents-and-adversary-behavior) | Limiting the scope or ongoing effects of an incident, such as isolating the affected device under an approved response plan. |
| [Eradication](#analyze-incidents-and-adversary-behavior) | Removing the cause and remaining artifacts of an incident before or alongside controlled restoration of normal operation. |
| [Phishing](#analyze-incidents-and-adversary-behavior) | An impersonation attempt that tries to induce an unsafe action or disclosure. Message appearance alone cannot establish the sender’s identity. |
| [Encryption](#explain-fortinet-soc-architecture) | A reversible transformation that protects readable data using a key. Someone with the appropriate key can recover the original. |
| [FortiAnalyzer](#explain-fortinet-soc-architecture) | A platform for collecting and analyzing supported Fortinet telemetry, including searching logs, generating reports and handling security events. |
| [Normalization](#explain-fortinet-soc-architecture) | Converting fields from different sources to a common representation so that the records can be compared. |
| [Security operations center (SOC)](#explain-fortinet-soc-architecture) | The people, processes and technology responsible for monitoring, investigating and coordinating response to security events. |
| [Threat intelligence](#explain-fortinet-soc-architecture) | Assessed information about adversary activity or indicators, with source, context and freshness to guide a decision. |
| [Vulnerability](#explain-fortinet-soc-architecture) | A weakness that can expose an asset to harm. Risk also depends on who or what could act on it and the consequences. |
| [FortiSOAR](#explain-fortinet-soc-architecture) | A platform for handling cases and orchestrating investigation and response workflows across connected security tools. |

**Detection capabilities**

| Term or phrase | Meaning |
|---|---|
| [Aggregation](#build-useful-fortisiem-queries) | Combining events by a key such as account or host to compute a count or other measure for a time window. |
| [FortiSIEM](#build-useful-fortisiem-queries) | A platform that collects and correlates events across infrastructure and security products to help identify and investigate incidents. |
| [Normalized field](#build-useful-fortisiem-queries) | A field mapped to a common name or type across sources. An analyst should preserve the source’s value when checking an unexpected match. |
| [Raw event](#build-useful-fortisiem-queries) | The original source observation before a parser or normalization rule transforms its fields. It provides a reference for checking a derived result. |
| [Telemetry](#build-useful-fortisiem-queries) | Logs, events and measurements supplied by managed systems. Customer attribution and collection health determine whether the records are usable. |
| [Time window](#build-useful-fortisiem-queries) | The interval over which events are selected or grouped. Changing it can split one sequence across windows or merge unrelated activity. |
| [Correlation window](#engineer-and-validate-incident-rules) | The time span over which a rule considers events together. It affects whether related observations form a single incident. |
| [False positive](#engineer-and-validate-incident-rules) | A detection that matches benign activity. Tuning requires understanding which condition made it match. |
| [Deduplication](#engineer-and-validate-incident-rules) | Recognizing and handling repeated copies of the same observation or request so duplication does not inflate counts or repeat an action. |
| [Grouping key](#engineer-and-validate-incident-rules) | The attribute or combination of attributes used to combine observations, such as user plus hostname. A poor key can merge unrelated activity. |
| [Incident](#engineer-and-validate-incident-rules) | A case that groups evidence of related activity for investigation, ownership and resolution. |
| [Intrusion prevention system (IPS)](#engineer-and-validate-incident-rules) | A control that inspects traffic for signs of known or suspicious activity and can block matching traffic. |
| [Threshold](#engineer-and-validate-incident-rules) | The value or condition that triggers a rule or changes an operational decision, such as five matching events in a ten-minute interval. |
| [True positive](#engineer-and-validate-incident-rules) | A detection supported by evidence that the condition it was intended to identify really occurred. |

**SOAR incident handling and threat hunting**

| Term or phrase | Meaning |
|---|---|
| [Threat-hunting hypothesis](#hunt-from-a-falsifiable-hypothesis) | A testable statement about activity that might be present, with specified evidence that could support or disprove it. |
| [Pivot](#hunt-from-a-falsifiable-hypothesis) | Following an entity from one relevant record to related evidence, such as taking a host from an alert and examining its activity around the same time. |
| [Runbook](#hunt-from-a-falsifiable-hypothesis) | Documented operational steps for a defined situation, with roles, expected observations and criteria for escalation or recovery. |
| [Case disposition](#manage-incidents-as-controlled-cases) | The recorded outcome of an investigation, including the evidence used to classify or close it. |
| [Availability](#manage-incidents-as-controlled-cases) | Timely and reliable access to a resource by authorized users. A running server may still be unavailable to the business if a required dependency fails. |
| [Case owner](#manage-incidents-as-controlled-cases) | The person or team accountable for moving an investigation forward, recording its status and arranging escalations. |
| [Escalation](#manage-incidents-as-controlled-cases) | Passing a case to the person or team with authority or expertise to make the next decision when defined conditions are met. |
| [Quarantine](#manage-incidents-as-controlled-cases) | A containment action that restricts a device’s connectivity while responders investigate or remediate it. |

**SOAR playbook development**

| Term or phrase | Meaning |
|---|---|
| [Idempotent action](#design-playbooks-for-predictable-outcomes) | An action that can be repeated after a retry without producing a second unintended change. |
| [Health check](#design-playbooks-for-predictable-outcomes) | A defined test of reachability or service behavior used to decide whether a path or backend remains eligible. A TCP response may test less than an application transaction. |
| [Idempotence](#design-playbooks-for-predictable-outcomes) | Making an operation safe to repeat without accumulating unintended effects. A retried request to create one case should still yield one case. |
| [Least privilege](#design-playbooks-for-predictable-outcomes) | Giving an identity only the permissions needed for its task, for as long as it needs them. |
| [Playbook](#design-playbooks-for-predictable-outcomes) | A workflow of decisions and tasks for a recurring case. It can combine automated enrichment with human authorization for disruptive actions. |
| [Rate limiting](#design-playbooks-for-predictable-outcomes) | Restricting the number or rate of operations in a defined interval to protect capacity. A limit applied per identity behaves differently from one applied per IP address. |
| [Schema](#design-playbooks-for-predictable-outcomes) | A definition of expected data structure, field types and constraints. A syntactically valid payload may still fail schema or business validation. |
| [Playbook execution trace](#debug-systematically) | A record of the inputs, branches and outcomes of a run that helps identify where an automated response failed. |

**Worked examples and practice**

| Term or phrase | Meaning |
|---|---|
| [Authentication](#suspected-credential-compromise) | The check that establishes who a user or device is. Authorization determines what that identity may do next. |
| [Indicator](#suspected-credential-compromise) | An observable value or pattern used to find potentially relevant activity. A match needs source context and timing before it supports an incident conclusion. |
| [Virtual private network (VPN)](#suspected-credential-compromise) | A protected logical connection over a shared network. Its permitted destinations and traffic depend on routes and access policy. |
| [Evidence preservation](#ransomware-like-endpoint-activity) | Maintaining the integrity and provenance of information needed for investigation, including original timestamps, collection method and access history. |
| [Ransomware](#ransomware-like-endpoint-activity) | Malware used to extort a victim, often by making files unusable. A tested backup helps recover the data. |
| [Telemetry gap](#collection-blind-spot) | A portion of the expected population, time period or activity for which the system lacks observations. Silence in that gap does not establish normal behavior. |

## Places to learn

This is not a complete list, and it is not a prescription to consume everything. Start with the official contract and select the course, documentation, framework, and lab sections that close measured gaps. Times are publisher-listed where visible or clearly labeled estimates.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Security Operations Architect exam](https://training.fortinet.com/local/staticpage/view.php?page=security_operations_architect_exam) | Public | 30–50 min | Current unweighted objectives, versions, experience, and official-resource boundary |
| [NSE 7 in Security Operations](https://training.fortinet.com/local/staticpage/view.php?page=nse_7_security_operations) and [Fortinet recertification policy](https://helpdesk.training.fortinet.com/support/solutions/articles/73000672593-exam-policy-recertification) | Public | 20–40 min | Credential prerequisites and renewal; the track page validity sentence is malformed, while the current policy states NSE certifications expire two years after issue |
| [Fortinet Training Institute library](https://training.fortinet.com/local/library/?search=security%20operations) | Free account; labs/ILT may cost | 20–40 min selection; course varies | Locate current Security Operations 7.6 Architect course and hands-on lab |
| [FortiSIEM 7.3 documentation](https://docs.fortinet.com/product/fortisiem/7.3) | Public | 18–30 hr selected reading/labs | Architecture, collection, parsers, queries, analytics/rules, incidents, HA and troubleshooting |
| [FortiSOAR 7.6 documentation](https://docs.fortinet.com/product/fortisoar/7.6) | Public | 18–30 hr selected reading/labs | Cases, queues/shifts, war rooms, connectors, playbooks, Jinja, debugging and administration |
| [MITRE ATT&CK](https://attack.mitre.org/) | Public | 5–10 hr selected techniques/data sources | Primary adversary-behavior vocabulary and detection data-source mapping |
| [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | Public | 4–7 hr | Current primary incident-response recommendations and organizational integration |
| [Fortinet Training Institute policies](https://helpdesk.training.fortinet.com/support/solutions/73000238852) | Public | 30–60 min | Delivery, retake, results, integrity, voucher, and renewal policy |
| [Fortinet YouTube](https://www.youtube.com/@Fortinet) | Free/YouTube | 3–8 hr selected current videos | Official SOC/product demonstrations; verify version and reproduce with synthetic evidence |

