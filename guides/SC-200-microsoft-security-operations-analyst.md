---
exam_code: SC-200
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# SC-200 Microsoft Security Operations Analyst Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#sc-200-coverage-record). The [official SC-200 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) is authoritative.

**Current baseline:** Skills measured as of July 28, 2026; official study-guide page last updated June 26, 2026.<br>
**Exam state:** Active; the official credential page lists no retirement date.<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 1, 2026.<br>
**Localized exams:** Microsoft says localized versions normally follow the English update by approximately eight weeks; verify your language version before scheduling.<br>
**Platform transition:** Microsoft says Sentinel in the Azure portal stops being supported after March 31, 2027. Learn the unified Microsoft Defender portal experience and understand where current Azure-portal workflows still differ. **VERIFY CURRENT** before planning a migration.<br>
**Official source:** [SC-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200)

## How to use this guide

SC-200 is an operator's exam. Product recognition is not enough: practice moving from signal to decision to safe action while preserving evidence. For each objective, be able to answer this chain:

```text
security question
  -> required data and permissions
  -> query, correlation, or investigation surface
  -> confidence, scope, and business impact
  -> containment or remediation action
  -> validation, evidence, tuning, and closure
```

Read Sections 1–3, work all three scenarios, complete or tabletop the eight labs, and answer all 36 checks. Keep a current test tenant or Microsoft-provided lab nearby. The July 2026 blueprint includes fast-moving Sentinel platform, graph, data-lake, MCP, Security Copilot, and agentic capabilities, so always resolve a disagreement in favor of the current Microsoft documentation.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Exam profile and complete objective map

The certification is intermediate and renews every 12 months. The current exam page gives 100 minutes for the proctored assessment and provides a free Practice Assessment and exam sandbox. Microsoft expects familiarity with its security, compliance, and identity solutions; Microsoft 365; Azure; AI agents and Copilots; and Windows, Linux, and mobile operating systems. Confirm administrative details on the [Security Operations Analyst Associate credential page](https://learn.microsoft.com/en-us/credentials/certifications/security-operations-analyst/).

| Official domain | Weight | Operational question |
|---|---:|---|
| Manage a security operations environment | 40–45% | How should automation, Sentinel, ingestion, and detections be configured for useful, governed signal? |
| Respond to security incidents | 35–40% | How do you establish scope and confidence, contain the attack, remediate safely, and preserve a defensible case record? |
| Perform threat hunting | 20–25% | How do you turn a hypothesis into KQL, graph, data-lake, notebook, or MCP-assisted investigation and then operationalize the result? |

### Published objective-to-guide map

| Published objective area | Primary coverage | Practice evidence |
|---|---|---|
| Defender XDR email/alert notifications, tuning/suppression/correlation, Endpoint advanced features/rules/custom collection/ASR | Section 1 | Scenario 1; Labs 1 and 4 |
| Automated investigation and response, automatic attack disruption, Endpoint device groups/permissions/automation levels | Section 1 | Scenarios 1 and 3; Labs 1 and 6 |
| Sentinel automation rules and playbooks | Section 1 | All scenarios; Labs 1 and 5 |
| Sentinel roles; Analytics, Data lake, and XDR retention tiers; workbooks; SOC optimization | Section 1 | Scenarios 2–3; Labs 2–3 |
| Connector selection; Windows events with AMA/DCR and WEF; Syslog/CEF with AMA; Azure Policy/diagnostics; threat indicators; custom tables | Section 1 | Scenarios 2–3; Labs 2–3 |
| Defender XDR custom detections; Sentinel scheduled/NRT/TI/ML analytics; ATT&CK coverage; anomalies | Section 1 | All scenarios; Labs 3–4 |
| Incidents across Office 365, Purview, Defender for Cloud, Cloud Apps, Entra ID, Defender for Identity, and Sentinel | Section 2 | All scenarios; Labs 5–7 |
| Agentic AI/Security Copilot, complex multi-stage/multi-domain/lateral-movement attacks, and case management | Section 2 | Scenarios 1 and 3; Labs 5–6 |
| Endpoint timelines, device actions/live response/packages, evidence/entities, and attack-disruption incidents | Section 2 | Scenario 1; Labs 5–6 |
| Purview Audit, eDiscovery Content search, and Microsoft Graph activity logs | Section 2 | Scenario 2; Lab 7 |
| Defender XDR tables, KQL, Advanced Hunting, threat analytics, hunting graphs/blast radius, and Sentinel Graph | Section 3 | All scenarios; Labs 4 and 8 |
| Sentinel hunting queries, data-lake KQL jobs, summary-rule tables, notebooks, and Sentinel MCP Server | Section 3 | Scenario 3; Labs 3 and 8 |

## 1. Manage a security operations environment

### Design operations before configuring tools

A useful SOC design starts with outcomes, not alert volume. Inventory critical services, identities, data, cloud subscriptions/accounts, endpoints, and external dependencies. For each priority threat, define:

- the question the SOC must answer and the response-time target;
- the authoritative signal sources, required fields, expected latency, retention, and owner;
- detection logic, severity, entity mappings, correlation, and known blind spots;
- analyst decision points and which actions may be automated;
- escalation, legal/privacy, service-owner, and recovery boundaries;
- test method, success criteria, tuning cadence, and evidence retained.

Use a lifecycle such as prepare, detect, analyze, contain, eradicate, recover, and learn. A closed incident is not the same as removed risk: verify containment, credential rotation, persistence removal, restored control health, and follow-up detection improvements.

> **Related item:** Track mean time to detect/respond, false-positive rate, recurrence, telemetry health, and percentage of tested use cases together. Any single metric can be gamed or conceal a blind spot.

### Configure Defender XDR and Endpoint automation deliberately

#### Notifications, alert tuning, suppression, and correlation

Email notifications help reach the right responders when incidents, threat analytics, or Endpoint actions require attention. Scope recipient rules by severity, device group, or source where supported, use monitored distribution paths, and test delivery. Notifications do not replace queue ownership or an on-call process.

Treat alert tuning as detection engineering:

1. Confirm the alert is understood and the benign pattern is stable.
2. Prefer the narrowest condition that removes the known pattern.
3. Preserve visibility for variants and high-value assets.
4. Record the owner, rationale, expiry/review date, and before/after volume.
5. Replay or simulate malicious and benign examples.

Suppression prevents selected matches from becoming alerts; tuning can adjust rule conditions or thresholds; correlation joins signals into incidents. Do not suppress evidence just because an incident is noisy. Microsoft's [Defender XDR alert-investigation and tuning guidance](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts) emphasizes using conditions carefully and monitoring rule performance.

#### Endpoint advanced features, rule settings, custom collection, and ASR

Endpoint advanced features enable integrations and behaviors such as live response, Microsoft Intune connection, authenticated telemetry, and sharing signals across Defender services. Enable only what the design and licenses require, validate roles and privacy implications, and recheck after tenant changes. Use the current [Defender for Endpoint advanced-features reference](https://learn.microsoft.com/en-us/defender-endpoint/advanced-features) rather than memorizing a portal screenshot.

Endpoint rule settings include alert notifications, suppression, indicators, web-content controls, automation, and related tenant/device behavior. Separate these concepts:

- an **indicator** allows, audits, warns, or blocks a file, certificate, IP, URL, or domain within product constraints;
- a **custom detection** runs an Advanced Hunting query and can create an alert and take response actions;
- **custom data collection** extends endpoint telemetry for a defined investigation/detection need and carries performance, privacy, schema, and retention responsibilities;
- **attack surface reduction (ASR)** rules reduce exploit and abuse opportunities on devices before an alert is needed.

Roll out ASR in audit or warn mode where appropriate, review exclusions, pilot representative devices, then enforce. An exclusion is a security decision, not simply an application-compatibility fix. Read [ASR rule deployment guidance](https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-deployment) and validate effective device policy rather than relying only on the management console.

Custom data collection is a current Endpoint-to-Sentinel telemetry path, not the older support-package/client-analyzer workflow. In Defender, a rule selects a supported custom event table and action/field conditions, targets all eligible devices or devices with **dynamic tags**, and sends matching events to the selected connected Sentinel workspace. Current tables cover custom process, image-load, file, network, and script events. Build a rule from the question backward: select only the event/action/fields needed, pilot on a small dynamic-tag scope, wait for deployment, query the corresponding `DeviceCustom*Events` table by `RuleName` and device, then measure volume and field quality before expanding.

The current [Endpoint custom-data-collection guide](https://learn.microsoft.com/en-us/defender-endpoint/create-custom-data-collection-rules) documents Defender for Endpoint Plan 2, a connected/selected Sentinel workspace, dynamic tags, supported Windows versions, deployment timing, per-rule event limits, Sentinel ingestion charges, monitoring queries, and enable/edit/delete behavior. Broad collection can hit a device's rolling limit and create material cost; overly narrow filters create blind spots. **VERIFY CURRENT:** this recently changed capability has had preview/GA and limit changes, so recheck licensing, operating systems, tables, one-workspace constraint, event limit, and portal path before implementation or exam day.

> **Related item:** Prevention, detection, and response overlap but are not interchangeable. ASR may block a behavior; a custom detection may identify it; live response may investigate or remediate it. Strong designs connect all three.

#### AIR, automatic attack disruption, and device automation scope

Automated investigation and response (AIR) investigates alerts, assembles evidence, determines verdicts, and recommends or performs remediation according to product and automation settings. Analysts review the investigation graph and pending/completed actions in Action center rather than assuming that “automated” means “resolved.”

Automatic attack disruption is different: Defender XDR correlates high-confidence, cross-domain attack evidence and takes containment actions against compromised entities to stop attack progress. Verify licensing, Defender product coverage, identity auditing/action accounts, device versions, and automation settings. Microsoft's [attack-disruption configuration guide](https://learn.microsoft.com/en-us/defender-xdr/configure-attack-disruption) notes that Endpoint device-group remediation levels affect behavior.

Device groups provide operational scope and RBAC boundaries. Plan grouping attributes, rank/precedence, user-group access, and automation level together. Overlapping rules or an overly broad group can send a critical server into a workstation automation policy. Test group membership and permissions with representative analysts.

Use this decision model:

| Mechanism | Trigger/logic | Typical scope | Analyst responsibility |
|---|---|---|---|
| Endpoint AIR | Product investigation from alerts/evidence | Device and related evidence | Review verdicts/actions and automation level |
| Automatic attack disruption | High-confidence correlated XDR attack | Compromised users/devices and connected attack | Validate containment, business impact, and full remediation |
| Defender custom detection | Scheduled/continuous Advanced Hunting logic | Returned devices/files/users/emails | Validate query, frequency, entity/action columns, scope, and noise |
| Sentinel automation rule | Incident/alert create or update plus conditions | Incident workflow | Control ordering, expiry, owner/status/tag/action, and playbook call |
| Sentinel playbook | Logic Apps workflow invoked manually or by automation | Cross-service orchestration | Secure identity/connections; handle retries, idempotency, approval, and failure |

### Engineer Sentinel automation safely

An automation rule evaluates incident/alert events and performs built-in actions or invokes a playbook. A playbook is an Azure Logic Apps workflow that can enrich, notify, ticket, contain, or remediate. Microsoft's current [playbook automation guidance](https://learn.microsoft.com/en-us/azure/sentinel/automation/run-playbooks) directs new automatic playbook invocation through automation rules; direct calls from analytics rules were a legacy path.

For every automation:

- define the trigger, provider, analytics-rule and severity conditions precisely;
- order rules intentionally and use expiration for temporary event handling;
- give the playbook's managed identity only the needed Sentinel/resource permissions;
- protect connector credentials and understand tenant/subscription context;
- make repeat execution safe (idempotent), catch partial failures, and log outcomes;
- require approval for destructive, ambiguous, high-impact, or legally sensitive actions;
- define timeout, retry, rollback, manual alternative, and owner;
- test with synthetic incidents and monitor failed runs.

A useful low-risk first automation enriches an incident, assigns an owner, adds a tag, and opens a ticket. Auto-isolating a business-critical host without confidence, approval, and recovery design is not a good first automation.

> **Related item:** Automation reduces handling time only if its inputs are trustworthy. Schema drift, missing entity mappings, expired connectors, and duplicate incidents can turn a correct playbook into an unsafe action.

### Configure the Sentinel SIEM and platform

#### Choose portal and workspace boundaries

Sentinel is integrated into the Microsoft Defender portal for unified operations with Defender XDR. Know the current capability boundary and migration prerequisites. Microsoft has announced that [Sentinel support in the Azure portal ends after March 31, 2027](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-reference), so prefer current Defender-portal workflows while recognizing that some configuration or edit experiences may still link to Azure.

Workspace topology affects access, residency, retention, cost, cross-workspace queries, incident ownership, and delegated operations. Centralization improves correlation and consistency; separate workspaces can satisfy tenant, region, billing, sovereignty, or organizational isolation. Do not create a workspace per team without examining cross-boundary response and data duplication.

#### Apply least-privilege roles

Sentinel Reader views data/incidents, Responder adds incident management, Contributor adds broader Sentinel configuration, and Playbook Operator can run playbooks. Logic Apps permissions and resource-group/workspace permissions also matter. Data-lake features can use tenant-wide Entra roles or workspace-level Azure RBAC. Use [Sentinel roles and permissions](https://learn.microsoft.com/en-us/azure/sentinel/roles) to reason from task and scope to role; avoid solving an access failure by assigning Owner.

Test four planes independently:

1. Can the analyst see the workspace/data?
2. Can they manage the incident or detection?
3. Can Sentinel invoke the playbook?
4. Can the playbook identity perform its downstream action?

#### Understand Analytics, Data lake, XDR, Basic/Auxiliary, and long-term data

The July blueprint explicitly names Analytics, Data lake, and XDR tiers. Think in terms of purpose rather than memorizing one price table:

- **Analytics tier** supports low-latency, full analytics used by detections, investigations, dashboards, and response.
- **Sentinel data lake tier** provides economical long-term, high-volume security data for historical investigation, jobs, notebooks, graph, and AI-connected scenarios. It is not a drop-in substitute for every real-time analytic.
- **XDR data** is held according to the Defender service and unified-portal retention model; understand when data is queried in Advanced Hunting and when Sentinel ingestion/retention is needed.
- **Basic/Auxiliary plans and long-term retention/archive** trade query features, latency, and access cost for lower ingestion/storage cost in eligible Log Analytics tables.

Start with use case, maximum acceptable detection latency, query operators, investigation horizon, regulatory hold, deletion/residency, and expected volume. Then choose table plan and retention. A cheaper table that cannot support the required rule or timely investigation is false economy. Conversely, expensive real-time ingestion of unused verbose data is not coverage.

**VERIFY CURRENT:** table eligibility, tier names, retention limits, query/operator support, ingestion/query pricing, and XDR/Sentinel integration behavior can change. Recheck the source table and region before making a design or cost decision.

> **Related item:** Retention is only part of forensic readiness. Validate time synchronization, parsing, stable identity/device/resource keys, integrity, access logging, case export, and legal-hold procedure.

#### Build decision-oriented workbooks

Sentinel workbooks use Azure Monitor Workbooks to present queries, parameters, charts, and drill-down links. A good workbook answers an operational question: connector health, incident aging, use-case performance, identity-risk trend, data-cost value, or response SLA. It declares time range and scope and permits drill-down to raw evidence.

Avoid impressive dashboards with ambiguous denominators. Test queries against empty, delayed, duplicated, and high-volume data; apply least-privilege sharing and source control/templates where practical. Use the [workbooks documentation](https://learn.microsoft.com/en-us/azure/sentinel/monitor-your-data) for current creation and portal behavior.

#### Use SOC optimization as a recommendation system

SOC optimization identifies data-value and detection-coverage opportunities. It can recommend enabling relevant analytics, connecting missing sources, changing a table plan, or stopping low-value ingestion. Coverage views may compare enabled detections/data with threat or business-risk scenarios; data-value views consider recent usage.

Do not accept a recommendation blindly. Check compliance retention, investigation use, seasonal threats, dormant-but-critical systems, custom queries, and downstream consumers. Document accept/dismiss decisions. Microsoft's [SOC optimization reference](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-reference) explains that unused-table analysis is time-bounded and that some recommendations remain preview.

### Ingest data for a defined use case

#### Select connectors by evidence requirements

For each connector, document supported deployment model, authentication, tenant/workspace scope, tables/fields, latency, volume, cost, normalization, health monitoring, throttling, and failure recovery. Confirm whether the connector creates incidents, alerts, raw logs, or all three. The [Sentinel connector catalog](https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources) is the starting point, not proof that the expected events have arrived.

Validate end to end:

```kusto
// Replace the table and expected source with your connector's schema.
CommonSecurityLog
| where TimeGenerated > ago(30m)
| summarize Events=count(), LastEvent=max(TimeGenerated) by DeviceVendor, DeviceProduct
| extend MinutesSinceLast = datetime_diff("minute", now(), LastEvent)
| order by MinutesSinceLast desc
```

The query must be adapted to the source; its purpose is to establish count, freshness, and recognizable producer. Add field-quality assertions needed by detections.

#### Windows Security Events via AMA and WEF

The Windows Security Events via AMA connector uses Azure Monitor Agent and data collection rules (DCRs) to select and route events. Design DCR association/scope, event-set filtering, destination, agent health, and duplication. “All events” can produce noise/cost; “Common” may omit an event a custom detection needs. Express the necessary Windows event IDs from the use-case inventory.

Windows Event Forwarding (WEF) centralizes events from source computers on a Windows Event Collector. Sentinel then collects from the collector. Plan source-initiated/collector-initiated subscriptions, WinRM/firewall/GPO, collector capacity, bookmarks, channel permissions, event latency, and high availability. WEF is transport/aggregation; the AMA/DCR still determines onward collection.

> **Related item:** An installed agent is not healthy telemetry. Test a known event on a source endpoint and trace source channel -> WEF subscription/collector -> AMA/DCR -> Sentinel table -> analytic.

#### Syslog and CEF via AMA

Syslog via AMA generally lands in `Syslog`; CEF via AMA normalizes security-appliance events into `CommonSecurityLog`. A Linux forwarder may receive device messages and the DCR filters facilities/severities before ingestion. Follow current [Syslog/CEF via AMA guidance](https://learn.microsoft.com/en-us/azure/sentinel/connect-cef-syslog-ama) and verify the proper stream (`Microsoft-Syslog` or `Microsoft-CommonSecurityLog`).

Test transport, TLS/network controls where applicable, facility/severity, CEF header/extension parsing, timestamps/time zone, hostname/device identity, duplicate forwarding, queue/disk behavior, and recovery after outage. A malformed CEF field can silently destroy entity mapping even while event counts look normal.

#### Azure Activity and resource logs

Azure Activity Log records subscription control-plane events; resource logs expose service-specific data/control-plane activity and require diagnostic settings. Azure Policy can deploy diagnostic settings at scale and remediate existing noncompliance, but policy assignment does not prove data arrival. Handle regional destinations, category groups, destination limits, policy identity permissions, exemptions, and duplicate settings.

Use [Azure Monitor diagnostic settings](https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings) to distinguish metrics/log categories and destination behavior. Confirm a known resource operation appears with caller, target, action, result, and correlation fields.

#### Threat intelligence and custom tables

Ingest threat indicators from supported platforms/connectors using standardized STIX/TAXII or APIs where possible. Preserve type, value, confidence, source, valid-from/until, labels, and revocation. Expire indicators and measure matches; more indicators can increase noise and query cost. Use the current `ThreatIntelIndicators`/`ThreatIntelObjects` schema rather than the retired legacy table, as highlighted in [Sentinel what's new](https://learn.microsoft.com/en-us/azure/sentinel/whats-new).

Create a custom Log Analytics table only after defining schema, transformations, DCR/data collection endpoint, retention/table plan, access, volume, and queries. Use a stable time column and meaningful identifiers. Test type coercion, malformed/missing fields, schema evolution, and ingestion latency. A custom table name normally ends in `_CL`; design it as an owned contract, not a dumping ground.

### Configure detections that analysts can operate

#### Defender XDR custom detection rules

A Defender custom detection begins with an Advanced Hunting KQL query. The query must meet frequency/lookback and required timestamp/entity-column rules. It can create alerts and optionally act on returned device, file, user, or email entities. Microsoft's [custom detection guide](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules) recommends validating the query before creating the rule.

For each rule, specify hypothesis, ATT&CK mapping, data/tables, frequency/lookback, entity and alert enrichment, action scope, exclusions, expected volume, owner, test cases, and rollback. A query that returns useful hunt context may still be unsuitable for automated action.

#### Sentinel analytics rule types

- **Scheduled** rules run KQL on a configurable schedule/lookback; handle ingestion delay, thresholds, grouping, suppression, and event-to-alert logic.
- **Near-real-time (NRT)** rules run every minute with a short ingestion-time delay for eligible scenarios. Use them only when the lower latency matters and the query meets constraints. See [NRT rule behavior](https://learn.microsoft.com/en-us/azure/sentinel/near-real-time-rules).
- **Threat-intelligence matching** compares indicators with relevant event fields; tune indicator quality, expiry, field mapping, and source trust.
- **Machine-learning/anomaly** detections use Microsoft or configurable anomaly logic depending on feature. Treat anomaly as investigation input: unusual is not necessarily malicious.

Entity mappings connect alerts to accounts, hosts, IPs, URLs, cloud resources, and other investigation objects. Custom details and dynamic alert properties put decision context in the incident. Alert grouping affects case scope: grouping unrelated events hides parallel attacks; fragmenting one campaign raises workload.

Map each analytic to ATT&CK tactics/techniques and verify it with safe tests. ATT&CK shows coverage intent, not effectiveness. Measure data health, test pass rate, false-positive/false-negative observations, analyst disposition, and detection-to-containment time.

> **Related item:** Detection-as-code can source-control templates, queries, workbooks, playbooks, and tests. Deployment automation does not remove the need for environment-specific baselines and response ownership.

## 2. Respond to security incidents

### Use a disciplined investigation loop

For every incident:

1. Validate source, time, severity, analytic, and data health.
2. Establish the earliest known activity and current attack state.
3. Identify affected identities, devices, mailboxes, apps, cloud resources, and data.
4. Build a timeline and relationship graph; separate fact, hypothesis, and unknown.
5. Look for persistence, privilege escalation, lateral movement, command/control, and exfiltration.
6. Choose containment that balances confidence, blast radius, service impact, reversibility, and approval.
7. Eradicate root cause and persistence; recover controls and services.
8. Validate no continuing activity, preserve evidence, document decisions, and improve detections/playbooks.

Incidents correlate alerts and entities; alerts describe detected activity; evidence/entities are the artifacts you investigate. Changing status or resolving an alert does not perform remediation.

### Investigate through Microsoft Defender XDR

The unified Defender incident queue combines eligible signals from Defender XDR and onboarded Sentinel workspaces. Start with incident story, alerts, entities/assets, evidence and response, investigation graph, timeline, and similar incidents. Confirm product-specific context before taking action.

#### Defender for Office 365

For phishing/business-email-compromise scenarios, inspect sender/recipient, message trace, headers, authentication results, URLs, attachments, campaigns, mailbox activity, sign-ins, forwarding/inbox rules, OAuth grants, and impacted recipients. Use Explorer/email entity pages, Automated Investigation and Response, and threat hunting as licensed. Remediation may include soft/hard deletion or move, URL/file blocking, account/session action, rule/app removal, and user notification. Automatic attack disruption can contain high-confidence business email compromise, but analysts must validate all affected entities.

#### Microsoft Purview

Purview alerts may expose DLP, insider-risk, communication/compliance, data-security, or audit context. Respect role separation and privacy: an investigator may see pseudonymized or limited data until explicitly authorized. Correlate sensitive-data actions with identity, device, app, and network evidence. Preserve the case trail and escalate through HR/legal/privacy workflows when required; do not make an insider judgment from one anomalous action.

#### Defender for Cloud workload protections

Investigate the protected resource, alert evidence, attack path, timeline, subscription/account, recent control-plane changes, identity, network flow, vulnerability/posture context, and connected logs. Containment differs by workload: revoke an identity, isolate a VM, block a network route, disable a public endpoint, rotate a secret, quarantine an image, or stop a workload. Before acting, understand availability and forensic impact. The [Defender for Cloud alert response guidance](https://learn.microsoft.com/en-us/azure/defender-for-cloud/managing-and-responding-alerts) explains alert states and response workflow.

#### Defender for Cloud Apps

Use activity, app, file, OAuth-app, and user/entity context to investigate impossible travel, anomalous download, risky OAuth consent, session-policy signals, or shadow IT. Determine whether the activity is sanctioned, whether Conditional Access App Control/session policy applies, and whether identity risk is present. Actions can suspend a user, revoke an app, quarantine/govern a file, or change an app's sanction status, subject to permissions and business impact.

#### Microsoft Entra ID and Defender for Identity

Entra investigation combines risky users/sign-ins, sign-in logs, audit logs, Conditional Access result, authentication method, device, IP/location, token/session context, and workload identities. Remediation can confirm compromise, dismiss safe risk, reset credentials, revoke sessions/tokens, require secure authentication, disable an identity, remove malicious app consent, and close persistence.

Defender for Identity adds on-premises identity signals from sensors, including reconnaissance, credential access, lateral movement, directory changes, and entity profiles. Check domain-controller sensor health, account/device relationships, lateral movement paths, honeytoken/sensitive entity context, and the Entra hybrid link. Resetting a cloud password alone may not remove on-premises persistence.

#### Microsoft Sentinel incidents

Review incident provider, analytic, entities, alerts, tasks, comments, owner/status/classification, bookmarks, investigation graph/timeline, automation history, and related raw events. Run pivots across authoritative tables, add findings as bookmarks/evidence, and use incident tasks/checklists for repeatability. For multitenant or multiworkspace cases, document where the authoritative case lives and how evidence is synchronized.

### Use agentic AI and Security Copilot with verification

Embedded Security Copilot and agents can summarize incidents, generate/interpret queries, analyze scripts, enrich entities, create briefings, recommend actions, or automate bounded workflows. Agentic AI may plan and invoke tools with less step-by-step prompting. This changes the control problem: verify identity, delegated permission, tool scope, grounding sources, action boundaries, approval, logs, and rollback.

Use AI output as a hypothesis and acceleration layer:

- supply clear scope, time range, objective, and desired evidence;
- inspect citations/query/results rather than trusting prose;
- distinguish observed facts from inferred narrative;
- remove unnecessary sensitive data from prompts and outputs;
- require human approval for disruptive/irreversible actions;
- record prompt/tool/action provenance where case policy requires;
- test prompt injection, malicious evidence, hallucinated entities, stale context, and partial failure.

> **Related item:** A confident narrative can create anchoring bias. Ask for disconfirming evidence and independently query the highest-impact claims.

### Investigate complex, multi-stage, multi-domain attacks

Build a single temporal and entity model across email, identity, endpoint, SaaS, cloud control plane/workload, and data. Normalize time to UTC; identify the initial access, first compromised identity/device, credential/token acquisition, privilege changes, remote execution, persistence, discovery, collection, and exfiltration. Graph views help expose paths but still require raw-event validation.

Contain in an order that prevents the attacker from adapting:

- protect evidence and emergency administration;
- block command/control or malicious infrastructure;
- isolate compromised endpoints/workloads when service impact permits;
- revoke sessions/tokens and rotate credentials/secrets from a clean control plane;
- remove persistence and excessive privilege;
- close original weakness and validate monitoring;
- restore from known-good state and watch for recurrence.

Coordinate owners. Endpoint isolation can break a live identity investigation; password reset can alert an attacker; shutting down a cloud workload can destroy volatile evidence. Record who authorized each tradeoff.

### Manage the incident as a case

A defensible case record includes unique identifier, scope, severity/priority and changes, assigned owner, chronology, evidence links, hypotheses, decisions/actions with actor/time/result, communications, business impact, containment/eradication/recovery verification, classification, root cause, and follow-ups. Use tasks, tags, comments, bookmarks, activity/audit history, and ticket integration consistently.

Separate classification from status. A true positive can be active, contained, or resolved; a false positive may indicate tuning work. Do not put secrets or unnecessary personal data in comments. Define retention/export and chain-of-custody needs before a major incident.

### Respond through Defender for Endpoint

#### Device timeline and entity evidence

The device timeline orders processes, files, registry, network, logon, and detections for one endpoint. Filter around the suspected time, identify parent/child chains and user context, then pivot to file, IP, URL, user, and alert pages. A timeline event is telemetry, not automatically malicious.

Evidence/entity pages aggregate prevalence, signer/hash, observed devices, alerts, reputation, and relationships. Compare tenant prevalence and global reputation carefully: a rare file may be legitimate; a common signed binary may be abused. Preserve hash, path, command line, user, timestamps, and source record.

#### Device actions and live response

Common actions include isolate device, contain device, run antivirus scan, collect investigation package, restrict app execution, initiate automated investigation, and live response. Know supported operating systems, role requirements, action state, and undo path. Isolation generally preserves Defender service communication but can disrupt business services.

Live response opens a remote shell for approved investigation/remediation commands. Use role separation, signed-script/library controls, session auditing, a written objective, and minimal commands. Avoid modifying evidence before collecting it. The [Endpoint response-action reference](https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts) lists capabilities and platform constraints.

For an incident touched by attack disruption, review contained entities and Action center history. Automated containment buys time; it does not replace persistence search, scope validation, credential recovery, or root-cause remediation.

### Investigate Microsoft 365 activities

#### Purview Audit

Audit searches activity across Microsoft 365 services and, depending on licensing, retention and premium capabilities. Define date/time, workload, users, operations, and record types; export the exact result set; preserve query criteria and UTC interpretation. Audit records can lag and schemas vary by workload. Use [Purview Audit search guidance](https://learn.microsoft.com/en-us/purview/audit-search) and validate fields against the activity's service.

#### eDiscovery Content search

Content search finds mailbox and supported site content by location, custodians, keywords, dates, participants, properties, and conditions. Use it for authorized evidence discovery, not telemetry hunting. Estimate/test the query, minimize scope, preserve search/export metadata, and apply appropriate eDiscovery roles and legal controls. Search results show content matching the query; absence is not proof an event never happened.

#### Microsoft Graph activity logs

Microsoft Graph activity logs expose HTTP requests handled by Graph for the tenant and can be sent through Azure Monitor diagnostic settings to supported destinations. They help investigate app/user API access, response status, client/request IDs, IP/user agent, tenant/app identity, permission/scopes, and requested resource paths. Protect sensitive fields and manage volume. Use the [Graph activity-log overview](https://learn.microsoft.com/en-us/graph/microsoft-graph-activity-logs-overview) to understand availability and schema.

> **Related item:** Entra audit/sign-in logs, Microsoft 365 unified audit, service-specific logs, and Graph activity logs answer different questions. Correlate rather than treating one as a universal audit trail.

## 3. Perform threat hunting

### Turn a hypothesis into repeatable evidence

A hunt is not browsing alerts. State a falsifiable hypothesis derived from threat intelligence, an incident, ATT&CK, an exposure, or a baseline deviation. Define entities, time range, required tables/fields, expected benign behavior, known gaps, and stop/escalation conditions. Run broad discovery, narrow with evidence, save high-value findings as bookmarks, document null results, and promote repeatable/high-confidence logic to detections.

Example hypothesis: “A compromised user used a newly consented OAuth application to enumerate files and download an unusual volume outside the normal client pattern.” Required evidence may span Entra audit/sign-ins, Graph activity logs, Defender for Cloud Apps, Purview audit, and endpoint/network context.

### Select the right KQL schema and operators

Defender Advanced Hunting and Sentinel Log Analytics both use KQL, but table availability, retention, functions, and schema differ. Start by choosing the table that owns the event:

- `DeviceProcessEvents`, `DeviceNetworkEvents`, `DeviceFileEvents`, `DeviceLogonEvents` for Endpoint behavior;
- `EmailEvents`, `EmailUrlInfo`, `UrlClickEvents` for mail/URL activity;
- `IdentityLogonEvents`, `IdentityDirectoryEvents`, and identity-related Entra tables for identity behavior;
- `AlertInfo`, `AlertEvidence`, `IncidentInfo`, and relevant graph/entity tables for correlated security records;
- Sentinel tables such as `SecurityEvent`, `WindowsEvent`, `Syslog`, `CommonSecurityLog`, `SigninLogs`, `AzureActivity`, and custom tables for collected data.

Use schema reference and `getschema`/field inspection rather than guessing columns. Query narrowly by time and projection, filter early, normalize casing, parse dynamic data intentionally, and avoid expensive unconstrained joins.

```kusto
let lookback = 24h;
let threshold = 20;
SigninLogs
| where TimeGenerated > ago(lookback)
| where ResultType != 0
| summarize Failures=count(), IPs=make_set(IPAddress, 20),
            FirstSeen=min(TimeGenerated), LastSeen=max(TimeGenerated)
            by UserPrincipalName
| where Failures >= threshold
| order by Failures desc
```

This is a learning pattern, not a production detection. A real rule must handle table semantics, result codes, service accounts, ingestion delay, baselines, entity mapping, and validation.

Core operator reasoning:

- `where` reduces rows; `project` controls columns; `extend` derives fields;
- `summarize ... by` aggregates and creates a new schema;
- `join` correlates matching keys but can multiply rows; choose kind and time relationship deliberately;
- `union` combines compatible streams; `search` is broad discovery and often inefficient for production;
- `parse`, `parse_json`, `extract`, and dynamic access turn raw fields into queryable values;
- `let`, functions, and watchlists make logic reusable;
- `bin`, `make-series`, `series_decompose_anomalies`, and `render` support time-series investigation;
- `arg_max`, `dcount`, `make_set`, `mv-expand`, and `lookup` solve common entity/history problems.

Test query boundaries: empty results, duplicate events, missing fields, late arrival, UTC window, high-cardinality keys, and known benign/malicious samples.

### Hunt and detect with Defender XDR

Advanced Hunting supports proactive querying across Defender data. Use the schema pane, sample queries, query resources, and results-to-entity pivots. Confirm retention and whether Sentinel integration extends access to additional tables. The [Advanced Hunting overview](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview) is the current feature reference.

A custom detection operationalizes a query; it is not simply a saved hunt. Make the rule return required timestamp and entity identifiers, match frequency/lookback constraints, and include actionable context. Test result rate and permissions, then monitor alert/action results.

Threat analytics reports provide Microsoft research, affected-asset status, related incidents, and detection/mitigation guidance. Use them to form hypotheses and prioritize validation against your environment; “no affected assets” depends on telemetry and product coverage.

Hunting graph visually connects entities and relationships. Blast-radius views show potential impact paths, while Sentinel Graph can connect activity, assets, and threat intelligence. Microsoft's [Sentinel Graph overview](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-graph-overview) distinguishes pre-breach exposure paths, incident blast radius, and interactive graph hunting. A graph edge expresses a modeled relationship; validate critical edges and timestamps in source data.

### Hunt on the Sentinel platform

#### Hunting queries, hunts, bookmarks, and livestream

Built-in and custom hunting queries provide hypotheses mapped to tactics/techniques. Review each query's required tables and logic before running it. A hunt groups a hypothesis, queries, bookmarks, and findings as a trackable investigation. Bookmarks preserve selected query results and notes and can be promoted to incidents. Livestream can repeatedly run a query for short-term monitoring, subject to feature constraints.

Convert proven, repeatable, time-sensitive logic to an analytic rule with owner, entity mapping, severity, test, and response. Leave exploratory or expensive multi-step reasoning as a hunt/notebook.

#### Choose KQL jobs, summary rules, or search jobs

The Sentinel data lake changes long-horizon hunting:

- **KQL jobs** run one-time or scheduled asynchronous, fuller-KQL queries over data-lake and federated tables and write results to Analytics. They suit historical multi-table investigation or enrichment.
- **Summary rules** periodically aggregate high-volume data into custom Analytics tables, supporting faster repeated detection/reporting with controlled loss of granularity.
- **Search jobs** hydrate results from a single large/historical table into an Analytics custom table for investigation; their operators and scope differ.

The current [KQL jobs, summary rules, and search jobs comparison](https://learn.microsoft.com/en-us/azure/sentinel/datalake/kql-jobs-summary-rules-search-jobs) is essential because supported source tiers, joins, scheduling, lookback, timeouts, and cost differ. Choose based on the investigation question, not the newest feature.

For a KQL job, define time range, source tables/tier, result table, schedule, cost guardrail, permissions, idempotency/deduplication, and lifecycle. For a summary table, document grain, dimensions, aggregation window, source latency, retained detail, update behavior, and consumer detections. Always retain a path back to raw evidence when required.

#### Use notebooks for advanced, documented analysis

Sentinel data-lake notebooks run in Visual Studio Code with Jupyter, Python, Spark, and the Microsoft Sentinel extension/provider. They suit multi-step transformations, visualization, statistical/ML work, reusable investigation narrative, and scheduled jobs. Select runtime size consciously and treat notebook output/custom tables as governed data.

Use a clean environment, pin/document logic, protect credentials, separate exploratory from production notebooks, parameterize tenant/time/entity inputs, avoid unnecessary data export, and validate results with KQL/source records. Review current [Sentinel data-lake notebook guidance](https://learn.microsoft.com/en-us/azure/sentinel/datalake/notebooks) for permissions, runtime, library, concurrency, and timeout limits.

#### Connect to the Sentinel MCP Server safely

The hosted Sentinel MCP Server exposes scenario-focused tool collections to compatible AI clients for data exploration, entity analysis, incident triage, hunting, and agent building. Most data-exploration capabilities require Sentinel data-lake onboarding, and the user/client retains permission requirements. The [MCP getting-started guide](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-get-started) lists prerequisites and current clients.

Treat MCP as a governed tool boundary:

- authenticate with Entra and least privilege; do not expose a broad shared identity;
- approve only needed collections/tools and limit client/workspace scope;
- treat alert text, logs, files, and external intelligence as untrusted prompt content;
- inspect tool inputs/results, source tables, time range, and evidence behind conclusions;
- prevent an exploratory agent from taking destructive response actions;
- audit sessions and test data leakage, prompt injection, overbroad retrieval, and failure handling.

Natural language lowers the query barrier but does not eliminate schema, evidence, or critical-thinking requirements. Reproduce high-impact findings with deterministic queries or records.

**VERIFY CURRENT:** Sentinel Graph, data-lake jobs/notebooks, MCP tool collections, compatible clients, licensing, region availability, roles, and preview/GA boundaries are fast-moving July 2026-era capabilities.

> **Related item:** Security Copilot, an embedded agent, a notebook, a playbook, and an MCP-connected client can all participate in one workflow. Document which identity executes each step and where human approval and audit evidence live.

## 4. Integrated scenarios

### Scenario 1 — Business email compromise becomes ransomware

A finance user opens a malicious attachment. The attacker steals a session, registers persistence, consents an OAuth app, uses remote administration on a workstation, compromises an on-premises admin, and begins encrypting a file server.

**Reasoning path:**

1. Validate and correlate Office 365, Entra, Endpoint, Defender for Identity, and Sentinel evidence into one UTC timeline.
2. Determine the initial message/recipients, clicked URL/file, token/app activity, process tree, credential/lateral-movement path, affected devices, and encryption scope.
3. Review automatic attack disruption and AIR actions; confirm which users/devices were contained and what remains active.
4. Preserve volatile and message evidence, isolate affected endpoints where safe, revoke sessions/consent, disable or reset compromised identities from a clean admin path, block indicators, and protect recovery systems.
5. Find persistence in mailbox rules, OAuth grants, scheduled tasks/services, directory privilege, remote tools, and backup access.
6. Recover in business-priority order, validate clean identity/device state, monitor recurrence, and update detection/automation.

**Evidence:** incident graph and timeline, mail/header/campaign records, OAuth/audit changes, device process/network events and package, identity lateral-movement evidence, action history, containment authorization, recovery validation, root cause, and tuned detections.

### Scenario 2 — Cost-aware multicloud ingestion and a suspicious workload

A SOC ingests Azure, AWS, firewall CEF, Windows WEF, and Linux Syslog data into one workspace. Cost rises 70%, a critical Azure workload alert fires, and analysts discover a missing identity field in firewall events.

**Reasoning path:**

1. Define the critical workload attack questions and required fields/latency/retention before changing data plans.
2. Validate each source end to end: policy/diagnostic settings, WEF-to-AMA/DCR, Linux forwarder/DCR/CEF parsing, multicloud connector, and Defender for Cloud integration.
3. Investigate the workload alert across control-plane changes, identity, endpoint/workload, network, and posture/attack-path evidence.
4. Use SOC optimization and usage queries to identify unused/verbose tables and columns, but preserve regulatory and forensic requirements.
5. Keep detection-critical data in Analytics; consider data lake/basic/auxiliary/long-term options for appropriate sources and use summaries/jobs for repeatable historical questions.
6. Fix the CEF mapping and replay a synthetic event before relying on entity correlation.

**Evidence:** source/use-case matrix, connector health/freshness tests, parsed sample fields, table plan/retention decision, before/after volume/cost, incident case, containment record, and rule regression tests.

### Scenario 3 — Long-horizon identity hunt with AI assistance

Threat intelligence suggests an adversary quietly abuses dormant accounts over nine months. The recent Analytics window is clean; data exists in the Sentinel data lake. An analyst uses a KQL job, notebook, Sentinel Graph, and an MCP-connected assistant.

**Reasoning path:**

1. State the hypothesis and define dormant-account baseline, time window, authoritative identity/sign-in/activity tables, and exclusions.
2. Use a bounded KQL job across long-term tables to create a reviewable Analytics result set; record query, cost, schedule, and result table.
3. Use a notebook for sequence/baseline analysis and Sentinel Graph to inspect privilege and asset relationships; validate high-impact edges against raw records.
4. Ask the MCP tool to find supporting and disconfirming evidence, then inspect actual tool results and reproduce important findings deterministically.
5. Open a hunt/case with bookmarks, scope identities/devices/apps, contain only after confidence and business-owner checks, and preserve evidence.
6. Create a summary/detection only if the pattern is stable and response-actionable; document data-lake and field dependencies.

**Evidence:** hypothesis, permissions and tool audit, KQL job definition/history, notebook/version/output, graph pivots, MCP prompts/tool results, raw-source confirmation, bookmarks, case actions, and operationalized rule test.

## 5. Study and readiness plan

### Four-week applied plan

**Week 1 — Platform and ingestion:** Map every objective. Configure or tabletop workspace/portal, roles, data tiers/retention, workbooks, SOC optimization, connectors, AMA/DCR, WEF, Syslog/CEF, diagnostics, indicators, and custom tables. Produce a source/use-case matrix and three freshness/field-quality queries.

**Week 2 — Detection and automation:** Build one Defender custom detection and one Sentinel scheduled or NRT analytic. Add ATT&CK/entity mappings, validate benign/malicious tests, configure a safe automation rule/playbook, and inspect AIR/attack-disruption/device-group settings.

**Week 3 — Incident response:** Work the cross-domain and cloud-workload scenarios. Practice Defender incident/entity/timeline pivots, Endpoint actions, Purview/Entra/Identity/Cloud Apps evidence, Sentinel case management, Audit/eDiscovery/Graph logs, and agentic-investigation verification.

**Week 4 — Hunting and consolidation:** Write KQL from scratch, then practice data-lake jobs, summaries, notebooks, graphs, and MCP as available or tabletop them from documentation. Take the free Practice Assessment, research every weak answer, repeat labs, and do a timed original-question review.

### Readiness rubric

You are approaching readiness when you can, without step-by-step instructions:

- map every blueprint bullet to a feature, decision, implementation surface, and validation artifact;
- explain AIR versus attack disruption versus Defender custom detections versus Sentinel automation/playbooks;
- choose a Sentinel data/retention tier from latency, query, history, cost, and compliance requirements;
- trace Windows, Syslog/CEF, Azure, threat-intelligence, and custom ingestion from source to usable fields;
- build/tune a KQL detection with entity mapping, ATT&CK, grouping, test, and response;
- investigate a multi-domain incident and justify containment order;
- select Advanced Hunting, a Sentinel hunt, KQL job, summary rule, search job, graph, notebook, or MCP tool for a given question;
- identify limitations, permissions, evidence, and verification for AI-assisted analysis.

## 6. Hands-on labs

Use a disposable tenant/subscription and synthetic data. Defender, Purview, Sentinel data-lake, graph, Security Copilot, and agentic features may require licenses, preview enrollment, or provider-hosted labs. Tabletop unavailable features using current documentation. The public [MicrosoftLearning SC-200 lab repository](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst) is designed around a training environment; read its setup instructions before use.

### Lab 1 — Automation and action boundaries

1. Inventory Defender notifications, Endpoint advanced features, device groups, permissions, automation levels, AIR, and attack-disruption prerequisites.
2. Create a synthetic low-severity incident and a Sentinel automation rule that tags, assigns, and invokes a non-destructive notification/enrichment playbook.
3. Test ordering, condition mismatch, duplicate execution, connector failure, retry, and expiry.
4. Tabletop a high-confidence ransomware incident and define which actions remain manual.

**Evidence:** configuration matrix, least-privilege identities, rule/playbook export or diagram, run history, failure/rollback notes, and approval boundary.

### Lab 2 — Workspace, roles, tiers, workbook, and optimization

1. Define workspace boundaries for a two-region, two-team SOC.
2. Map Reader/Responder/Contributor/Playbook Operator and data-lake access to five job tasks.
3. Classify six tables among Analytics/data lake/basic/auxiliary/long-term options from use cases.
4. Build a connector-health or incident-aging workbook with scope/time/drill-down.
5. Evaluate three SOC optimization recommendations and document accept/dismiss reasoning.

**Evidence:** topology, role matrix, table/retention/cost decision, workbook export/screenshot plus queries, and optimization decisions.

### Lab 3 — Multisource ingestion validation

1. Define security questions and fields for Windows logon, firewall connection, Linux authentication, Azure resource change, and threat-indicator sources.
2. Configure or diagram Windows Events via AMA/DCR and a WEF collector path.
3. Configure or diagram a Linux Syslog/CEF forwarder and DCR.
4. Create an Azure Policy/diagnostic-settings plan and custom-table schema.
5. Generate/tabletop one event per source and trace arrival, latency, parsing, entity fields, and failure alert.

**Evidence:** data-flow diagrams, DCR/policy/schema artifacts, sample queries/results, latency/field test table, and troubleshooting runbook.

### Lab 4 — Detection engineering with KQL

1. Choose a safe hypothesis such as repeated failures followed by success or suspicious process/network behavior.
2. Write a time-bounded query, inspect schema, filter/project early, aggregate, and enrich entities.
3. Adapt it to a Defender custom detection or Sentinel scheduled/NRT analytic as appropriate.
4. Configure grouping, ATT&CK mapping, severity, custom details, and response action without destructive automation.
5. Replay benign/malicious synthetic cases and tune without hiding variants.

**Evidence:** hypothesis, query versions, rule configuration, test data/results, false-positive notes, and owner/tuning cadence.

### Lab 5 — Cross-domain incident investigation

1. Use a simulated phishing-to-endpoint incident or the Microsoft lab scenario.
2. Build a UTC timeline across mail, user/sign-in, endpoint process/network, OAuth, and identity evidence.
3. Identify initial access, persistence, lateral movement, scope, and potential data impact.
4. Use bookmarks/comments/tasks and record confidence versus unknowns.
5. Propose ordered containment, eradication, recovery, and validation steps.

**Evidence:** incident/case record, entity/timeline graph, evidence references, hypotheses, actions/approvals, and closure criteria.

### Lab 6 — Endpoint response and attack disruption

1. Investigate a synthetic device alert and review timeline, process tree, file/user/IP entities, prevalence, and related alerts.
2. Collect or tabletop an investigation package before altering the endpoint.
3. Test a safe action such as antivirus scan in an authorized lab; document isolation/live-response prerequisites and undo paths.
4. Review Action center/AIR evidence and tabletop automatic attack-disruption containment.
5. Verify persistence removal and restored telemetry.

**Evidence:** device/action timeline, hashes/commands, package record, action authorization/result, disruption review, and recovery validation.

### Lab 7 — Microsoft 365 evidence search

1. Generate or use synthetic mailbox/file/app activity.
2. Define and run/tabletop a Purview Audit search with exact operations, users, and UTC range.
3. Design a least-scope eDiscovery Content search and record authorization/export controls.
4. Query or inspect Graph activity-log records and correlate request/client/app/user identifiers.
5. Compare which evidence each log/search can and cannot establish.

**Evidence:** search definitions, result samples, role/privacy decisions, correlation table, export/hash procedure, and identified blind spots.

### Lab 8 — Long-term hunt, graph, notebook, and MCP

1. State a long-horizon hypothesis and map tables/fields/time/expected benign behavior.
2. Write/tabletop a KQL job and choose between job, summary rule, and search job.
3. Create a small parameterized notebook or pseudocode analysis and specify runtime/output governance.
4. Inspect a hunting/blast-radius graph and validate two edges from source evidence.
5. Use or tabletop Sentinel MCP prompts that seek both supporting and disconfirming evidence; constrain permissions and tools.
6. Decide whether the result becomes a bookmark, case, analytic, summary, or documented null hunt.

**Evidence:** hypothesis/query/job, summary grain if used, notebook, graph validation, MCP tool trace, cost/permission record, and operationalization decision.

## 7. Knowledge checks

These are original study questions, not recalled exam content.

1. **Why is an email notification not incident ownership?** Delivery can fail or be ignored; an operational queue, on-call process, escalation, and acknowledgment establish ownership.
2. **How should you suppress a recurring benign alert?** Confirm the pattern, create the narrowest condition, preserve malicious variants/high-value scope, record owner/expiry, and regression-test it.
3. **How do an indicator, ASR rule, and custom detection differ?** An indicator allows/audits/warns/blocks known artifacts; ASR reduces classes of endpoint behavior; a custom detection queries telemetry to alert or act.
4. **What does AIR provide?** Automated evidence investigation and verdict/remediation workflow governed by product and device-group automation settings.
5. **How is automatic attack disruption different from an ordinary playbook?** It uses high-confidence, correlated cross-domain Defender signals and built-in containment logic; a playbook executes explicitly designed Logic Apps workflow.
6. **Why do device-group rank and automation level belong together?** Overlap resolution determines which permissions and remediation behavior apply to the device.
7. **When should a playbook require approval?** Before ambiguous, destructive, irreversible, legally sensitive, or high-business-impact actions.
8. **What four permission planes should you test for a playbook?** Analyst/workspace visibility, incident management, Sentinel invocation, and the playbook identity's downstream action.
9. **Why is one centralized Sentinel workspace not automatically best?** Residency, tenant, billing, access isolation, ownership, volume, and delegated operations may justify boundaries despite correlation benefits.
10. **What belongs in Analytics rather than only the data lake?** Data requiring supported low-latency detection/investigation queries and actions; exact eligibility and features must be verified per table.
11. **Why can low-cost storage increase total risk or cost?** Unsupported/slow queries can miss detection SLAs or require expensive scans/hydration during incidents.
12. **What makes a workbook operationally useful?** A defined question, correct denominator/scope/time, validated queries, and drill-down to actionable evidence.
13. **Why review rather than automatically apply SOC optimization?** Recent usage cannot fully capture compliance, rare-but-critical investigations, seasonal threats, or custom/downstream dependencies.
14. **What proves a connector works?** A known source action appears in the intended table on time with required parsed/entity fields and downstream detection behavior.
15. **How do AMA/DCR and WEF relate?** WEF aggregates Windows events to a collector; AMA/DCR selects and routes the collector/source events into Azure Monitor/Sentinel.
16. **Where do Syslog and CEF via AMA normally land?** `Syslog` and `CommonSecurityLog`, respectively, subject to correct streams and parsing.
17. **What does Azure Policy add to diagnostic settings?** At-scale deployment/compliance/remediation; it does not prove that expected resource logs arrive.
18. **Why must threat indicators expire?** Infrastructure changes; stale indicators create noise, misleading matches, and unnecessary cost.
19. **When is a custom table justified?** When a defined security use case needs data not represented appropriately elsewhere and schema, collection, access, plan, retention, and ownership are designed.
20. **Scheduled versus NRT analytic?** Scheduled rules offer configurable cadence/lookback; NRT rules run every minute with constrained low-latency behavior for eligible queries.
21. **Why map entities in an analytic?** Correct mappings enable correlation, graphs, investigation pivots, automation context, and case scope.
22. **What does an ATT&CK mapping prove?** Intended technique coverage—not that telemetry, query, alert, and response work in the environment.
23. **What is the first response step after an alert?** Validate the signal, data/source health, time, scope, and current attack state before choosing action.
24. **Why can isolating a device be harmful?** It may interrupt critical service, remote evidence access, or coordinated identity investigation; authorization and undo paths matter.
25. **What should you verify after attack disruption?** Exact contained entities/actions, remaining scope/persistence, business impact, credential recovery, telemetry, and recurrence.
26. **Why are Purview insider-risk findings handled differently?** Privacy, pseudonymization, role separation, legal/HR authorization, and incomplete behavioral context demand controlled review.
27. **What is the danger of an AI-generated incident summary?** It can confidently merge inference with fact; verify citations, queries, entities, time, and disconfirming evidence.
28. **What distinguishes status from classification?** Status tracks workflow state; classification records whether/why the detection represented malicious or benign activity.
29. **What does a device timeline establish?** Ordered endpoint telemetry for that device; it does not alone establish attacker intent or full cross-domain scope.
30. **How do Audit, eDiscovery Content search, and Graph activity logs differ?** Audit records activities, Content search finds authorized stored content, and Graph logs record API requests; each has different schema, scope, latency, and retention.
31. **Why choose the table before writing KQL?** The event owner, schema, retention, and semantics determine whether the query can answer the hypothesis correctly.
32. **When should a hunt become a detection?** When logic is repeatable, timely, sufficiently precise, tested, owned, and connected to an actionable response.
33. **KQL job versus summary rule versus search job?** KQL jobs run fuller multi-table lake queries; summaries repeatedly aggregate into Analytics; search jobs hydrate results from a large single table under different constraints.
34. **Why validate a graph edge?** It is a modeled relationship that may be stale, indirect, or incomplete; source evidence establishes the relevant fact and time.
35. **When is a notebook better than one KQL query?** For documented multi-step analysis, Spark/Python transformations, statistics/ML, visualization, or scheduled data-lake processing.
36. **What is the core MCP safety boundary?** The connected identity, allowed tools/workspaces, untrusted retrieved content, action authority, audit, and deterministic verification of important results.

## Places to learn

This is a curated starting point, not a complete list. Do **not** try to consume every resource. Pick a primary path that fits how you learn, use documentation and labs for weak areas, and use assessments to decide what to revisit. Verify every course against the July 28, 2026 blueprint—especially data-lake tiers/jobs, Sentinel Graph, agentic investigation, embedded Security Copilot, and Sentinel MCP Server.

### Time-planning summary

| Resource | Access | Estimated time |
|---|---|---:|
| Official blueprint, credential/exam page, and change log | Free | 45–75 minutes |
| Ten official Microsoft Learn paths in the current course syllabus | Free | 43 hours 12 minutes listed; allow 55–75 hours with exercises and notes |
| SC-200T00-A instructor-led course | Provider/schedule dependent | 4 days |
| Microsoft Learn free Practice Assessment | Free; launch from credential page | 45–75 minutes per attempt plus 1–3 hours source review |
| MicrosoftLearning public SC-200 labs | Free; many expect a prepared tenant | 10–20 hours selected labs; full use depends on environment |
| Microsoft Exam Readiness Zone SC-200 videos | Free | About 1–2 hours; reconcile the recording date with July 2026 |
| Pluralsight SC-200 path | Paid/trial | 6 hours listed plus labs/review; courses date 2022–2024 |
| O'Reilly/Packt SC-200 video | Paid/trial | 12 hours 50 minutes; June 2022 baseline |
| O'Reilly live SC-200 crash course by Tim Warner | Paid/subscription; schedule dependent | 2 sessions of 3 hours (6 hours listed) plus review; older domain wording |
| Microsoft Press Exam Ref SC-200, 2nd Edition | Paid; preview/sample availability varies | 416 pages; allow about 14–22 hours plus labs |
| Udemy 2026 SC-200 practice tests by Dean Ellerby | Paid | 6 tests / 360 questions; allow about 9–15 hours with explanation/source review |
| MeasureUp SC-200 practice test | Paid; demo available | 170 questions; allow about 7–12 hours for diagnostic, review, and timed retest |
| Partner Skilling Hub SC-200 offering | Microsoft partner login required | Schedule-dependent; allow about 4–5 days for a certification-week format, verify listing |

### Official Microsoft resources

- [SC-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) — authoritative July 28, 2026 objectives and change log.
- [Security Operations Analyst Associate credential](https://learn.microsoft.com/en-us/credentials/certifications/security-operations-analyst/) — status, renewal, 100-minute exam, free Practice Assessment, sandbox, and prep-video entry point.
- [SC-200T00-A course](https://learn.microsoft.com/en-us/training/courses/sc-200t00) — four instructor-led days and the current self-directed syllabus.
- [Mitigate threats using Defender XDR](https://learn.microsoft.com/en-us/training/paths/sc-200-mitigate-threats-using-microsoft-365-defender/) — 6 hours 6 minutes.
- [Mitigate threats using Security Copilot](https://learn.microsoft.com/en-us/training/paths/sc-200-mitigate-threats-using-microsoft-copilot-for-security/) — 4 hours 54 minutes.
- [Mitigate threats using Microsoft Purview](https://learn.microsoft.com/en-us/training/paths/sc-200-mitigate-threats-using-microsoft-purview/) — 4 hours 19 minutes.
- [Mitigate threats using Defender for Endpoint](https://learn.microsoft.com/en-us/training/paths/sc-200-mitigate-threats-using-microsoft-defender-for-endpoint/) — 5 hours 49 minutes.
- [Mitigate threats using Defender for Cloud](https://learn.microsoft.com/en-us/training/paths/sc-200-mitigate-threats-using-azure-defender/) — 4 hours 17 minutes.
- [Create Sentinel queries with KQL](https://learn.microsoft.com/en-us/training/paths/sc-200-utilize-kql-for-azure-sentinel/) — 2 hours 10 minutes.
- [Configure your Sentinel environment](https://learn.microsoft.com/en-us/training/paths/sc-200-configure-azure-sentinel-environment/) — 3 hours 45 minutes.
- [Connect logs to Sentinel](https://learn.microsoft.com/en-us/training/paths/sc-200-connect-logs-to-azure-sentinel/) — 3 hours 4 minutes.
- [Create detections and investigate with Sentinel](https://learn.microsoft.com/en-us/training/paths/sc-200-create-detections-perform-investigations-azure-sentinel/) — 6 hours 34 minutes.
- [Perform threat hunting in Sentinel](https://learn.microsoft.com/en-us/training/paths/sc-200-perform-threat-hunting-azure-sentinel/) — 2 hours 14 minutes.
- [MicrosoftLearning SC-200 lab repository](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst) — public course lab instructions and setup notes.
- Use the prep-video link on the [credential page](https://learn.microsoft.com/en-us/credentials/certifications/security-operations-analyst/) for Microsoft's Exam Readiness Zone material; verify the episode date and its objective weights before relying on it.

### Video, books, and structured courses

- [Pluralsight Microsoft Security Operations Analyst (SC-200)](https://www.pluralsight.com/paths/microsoft-security-operations-analyst-sc-200) — three courses/six hours and a practice exam. The listed courses date from 2022–2024 and still use older product/domain language, so use them for foundations and build a July 2026 gap list.
- [O'Reilly/Packt SC-200 Microsoft Security Operations Analyst](https://www.oreilly.com/videos/sc-200-microsoft-security/9781804611777/) — 12 hours 50 minutes with Anand Rao Nednur, published June 2022. Useful demonstrations, but it predates Defender-portal unification and the current data-lake, graph, MCP, Copilot, and agentic objectives.
- [O'Reilly live SC-200 crash course](https://www.oreilly.com/live-events/exam-sc-200-microsoft-security-operations-analyst-crash-course/0636920075286/) with Tim Warner — two three-hour sessions in the listed agenda. Verify the next event date and treat its older Microsoft 365 Defender/domain terminology as supplemental.
- [Microsoft Press Exam Ref SC-200, 2nd Edition](https://www.microsoftpressstore.com/store/exam-ref-sc-200-microsoft-security-operations-analyst-9780135592595) by Yuri Diogenes, Tom Janetscheck, and Gianni Castaldi — 416 pages, published in 2026. Check its stated exam-update chapter against the July 2026 outline.
- [Udemy SC-200 practice tests (2026)](https://www.udemy.com/course/sc-200-practice-tests-security-operations-analyst-2026/) by Dean Ellerby — six tests/360 original questions, listed as updated August 2026 with per-option explanations and documentation links. Use practice mode ethically and validate disputed answers against Microsoft sources.
- [Cloud 360 Training SC-200 course](https://www.youtube.com/watch?v=HsqdfQdg08k) — free YouTube series entry point published February 2025. The first video is only a short orientation and the series predates July 2026; sample its depth before using it and fill the current-objective gaps.
- [John Savill's Technical Training channel](https://www.youtube.com/@NTFAQGuy/videos) is excellent for Microsoft security foundations, and his public [Azure Master Class repository](https://github.com/johnthebrit/AzureMasterClass) includes monitoring/security material and downloadable whiteboards. No current SC-200-specific course was confirmed in this review, so use individual KQL, Sentinel, Defender, and security videos only as product background and verify every topic against current documentation.

### Assessment and partner resources

- Use the free Microsoft Practice Assessment on the [SC-200 credential page](https://learn.microsoft.com/en-us/credentials/certifications/security-operations-analyst/) as a diagnostic, not a question bank. Research every weak or ambiguous answer in current product documentation.
- [MeasureUp SC-200 practice test](https://www.measureup.com/microsoft-practice-test-sc-200-microsoft-security-operations-analyst.html) — 170 original questions, practice and certification modes, explanations/references, and an August 2026 update listed. A demo is available.
- [Microsoft Partner Skilling Hub security playbook](https://media.skilling-hub.com/main/pdf/e95c2a9e-6e1c-4cb4-94a6-15a1c70ba1eb/fy26-partner-skilling-playbook.pdf) lists Security Operations Analyst (SC-200) among security credential offerings. Partner sign-in is required for underlying event content; dates and duration are schedule-specific.

Avoid sites selling “real questions,” dumps, guarantees based on recalled exam content, or unauthorized copies. Use original practice questions, the free official assessment, current documentation, and authorized labs to build transferable security-operations skill.
