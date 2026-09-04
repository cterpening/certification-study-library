---
exam_code: 1Z0-1111-26
vendor_id: oracle
official_blueprint: https://mylearn.oracle.com/ou/learning-path/become-an-oracle-cloud-infrastructure-observability-professional-2026/162237
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-04
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-04
---

# 1Z0-1111-26 Oracle Cloud Infrastructure Observability Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide maps Oracle University's public 2026 learning-path scope checked September 4, 2026. It is unofficial and may contain errors. The [official OCI Observability Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oracle-cloud-infrastructure-observability-professional-2026/162237) is authoritative.

**Assessment contract exposed by the current path:** Oracle Cloud Infrastructure Observability Professional, exam 1Z0-1111-26, 90 minutes.<br>
**Published scope:** Monitoring metrics and alarms; Events rules and automated actions; centralized service, custom, and audit logs; Log Analytics ingestion, enrichment, aggregation, correlation, and visualization; Application Performance Monitoring with distributed tracing, real-user monitoring, and synthetic monitoring.<br>
**Source boundary:** the public path exposes five capability groups rather than weights, question count, or passing score. This guide preserves that boundary. **VERIFY CURRENT** in MyLearn before scheduling.

## How to use this guide

Begin with a user-visible question, then choose the minimum telemetry that can answer it. For every exercise, record signal source, resource and application identity, dimensions, units, aggregation, time window, retention, access, cost, expected failure signature, and response. Use only authorized systems and synthetic traffic.

> **About related items:** A `Related item:` callout adds practical observability context. It is supporting knowledge, not a claim that its wording appears in Oracle's published scope.

## Objective map

| Published capability | Observability proof |
|---|---|
| OCI Monitoring | Correctly interpreted metrics and alarms expose symptoms and actionable resource conditions |
| OCI Events | Precisely matched state changes trigger bounded, idempotent, observable actions |
| OCI Logging | Service, custom, and audit logs are enabled, searched, protected, retained, and routed deliberately |
| OCI Log Analytics | Ingested records are parsed, enriched, correlated, aggregated, and visualized into defensible findings |
| OCI Application Performance Monitoring | Traces, real-user monitoring, and synthetic monitoring distinguish user experience from application and dependency causes |

## 1. Monitoring metrics and alarms

OCI Monitoring stores metric streams identified by namespace, metric name, dimensions, and metadata. Interpret units, emission interval, aggregation, statistic, grouping, and query window before drawing a conclusion. A mean can hide a small population of severe latency; a sum can mislead when streams or intervals change.

Use Metrics Explorer and Monitoring Query Language to select and aggregate the intended streams. Separate service-level indicators such as successful request latency from resource indicators such as CPU, memory, throttling, or capacity. Missing data is a state to handle, not proof of health.

An alarm combines a query, interval, trigger delay or pending duration, severity, destination, and message. Design thresholds from an operating objective and historical behavior, not round numbers. Test firing, notification, repeat behavior, suppression, recovery, and ownership.

> **Related item:** Percentiles preserve the experience of slower requests better than an average, but low sample counts and aggregation across unlike populations can still distort the result.

## 2. Events and automated actions

OCI services emit structured events for supported resource state changes. Event rules match attributes in the event envelope and route matches to supported actions. Verify event type, compartment and resource scope, pattern logic, target permissions, and the target's handling of duplicates or out-of-order delivery.

Use Events when a resource change should initiate notification or automation; use Monitoring alarms when a metric condition persists or crosses a threshold. Some operational flows need both. Preserve the original event identity and result so a responder can reconstruct the automation path.

Automated actions require least privilege, input validation, idempotency, retry bounds, loop prevention, rate limits, and escalation. Never let a broadly matched event execute an unrestricted destructive response.

## 3. Centralized Logging

OCI Logging brings supported service logs and custom logs into log groups; Audit records control-plane API activity. Know which source produces each record, how it is enabled, and what absence means. Standardize useful fields such as time, environment, resource, service, deployment, request or trace identity, outcome, and error class.

Search by a narrowing hypothesis: time and scope first, then structured fields and correlation. Avoid relying on free-text coincidence when a stable field exists. Redact secrets, tokens, personal data, and regulated content before ingestion where possible.

Design log-group access, retention, archive or downstream routing, and deletion around incident, legal, privacy, and cost requirements. Service Connector Hub can move supported data to other services; monitor the connector and destination so a broken pipeline is visible.

## 4. Log Analytics

Log Analytics ingests logs from OCI, on-premises, and other supported sources for parsing, enrichment, search, aggregation, correlation, pattern analysis, and visualization. Reliable analysis begins with correct source association, parser behavior, entity identity, time normalization, and ingestion health.

Enrichment adds useful context but can introduce stale or incorrect assumptions. Preserve raw evidence and distinguish observed fields from derived labels. Aggregate only comparable values, track denominator and time window, and drill from a visualization back to representative records.

Use correlations and clusters to form hypotheses, then validate them against topology, deployment history, metrics, traces, and source logs. Machine-generated patterns accelerate investigation; they do not prove causality.

## 5. Application Performance Monitoring

Distributed tracing follows work through instrumented services using traces and spans. Interpret parent/child relationships, duration, status, attributes, sampling, and missing spans. A slow parent can be waiting on a child, consuming local work, queued, or blocked by an uninstrumented dependency.

Real-user monitoring observes actual browser or client experience and distribution across geography, device, page, and network conditions. Synthetic monitoring runs controlled, repeatable journeys or availability checks even when real traffic is absent. RUM gives realism; synthetic tests give controlled continuity. Neither alone represents every user or dependency.

Protect telemetry from sensitive payload and high-cardinality field leakage. Connect trace, deployment, service, log, and infrastructure identities so responders can move from user symptom to code or dependency evidence. Use sampling deliberately and retain enough context to investigate rare failures.

## 6. Operational observability design

Build observability around service objectives and responder decisions. For each critical service, define golden signals, dependency and queue indicators, change markers, dashboards, alarms, runbooks, escalation, and evidence retention. Monitor the monitoring path: agents, ingestion, connectors, queries, notification topics, and synthetic probes can fail independently.

During an incident, create a timeline, establish blast radius, correlate recent changes, test hypotheses, mitigate safely, and preserve evidence. Afterward, improve the system, alert, runbook, or ownership model rather than merely adding more telemetry.

Control cost through purposeful collection, cardinality, retention, query design, and routing. Dropping low-value noise is healthy only when required security, audit, diagnostic, and service evidence remains available.

## Integrated practice scenarios

1. **Intermittent checkout latency:** Use RUM to scope affected users, synthetic tests to reproduce the journey, traces to find a slow dependency, metrics to confirm saturation, and logs to validate the error path.
2. **Unauthorized network change:** Detect the control-plane action in Audit, correlate resource and flow evidence, route a bounded event response, and preserve an investigation timeline.
3. **Growing async backlog:** Connect queue age and consumer metrics, application traces, deployment markers, and Log Analytics patterns to distinguish traffic growth, poison messages, throttling, and a bad release.

## Hands-on labs

1. Build a metric dictionary with namespace, dimensions, units, interval, aggregation, owner, and expected failure signature for one service.
2. Write and compare mean, percentile, rate, and grouped metric queries; show one misleading aggregation and correct it.
3. Create or simulate an alarm through normal, pending, firing, repeat, suppression, missing-data, and recovery states.
4. Match a synthetic resource event, route it to a safe target, prove a nonmatch, retry the same event, and prevent a response loop.
5. Enable or model service, custom, and audit log paths; search a correlated request and verify redaction, access, retention, and pipeline health.
6. Ingest a synthetic mixed log set into Log Analytics or a local substitute; parse, enrich, aggregate, correlate, visualize, and trace one result back to raw records.
7. Instrument a small service or use an authorized sample to compare distributed traces, real-user evidence, and synthetic checks during an injected delay.
8. Run a timed incident: establish scope, timeline, change correlation, hypothesis, mitigation, recovery evidence, and one observability improvement.

## Original readiness checks

1. Metric stream identity? 2. Mean-risk example? 3. Rate versus sum? 4. Missing-data meaning? 5. Actionable alarm parts? 6. Why pending duration? 7. Event versus alarm? 8. Event-rule scope risk? 9. Automation idempotency? 10. Service log versus Audit log? 11. Useful correlation fields? 12. Why redact before ingestion? 13. Connector monitoring? 14. Parser-association risk? 15. Raw versus enriched evidence? 16. Correlation versus causation? 17. Trace versus span? 18. Missing-span meaning? 19. RUM versus synthetic? 20. Sampling tradeoff? 21. Cardinality risk? 22. Monitor-the-monitoring examples? 23. Incident first step? 24. What remains unpublished? 25. What proves professional readiness?

### Answer guide

1. Namespace, name, dimensions, and metadata. 2. A few very slow requests hidden by many fast ones. 3. Change per time versus accumulated value. 4. Silence, ingestion failure, unsupported emission, or no activity—not automatic health. 5. Correct query, timing, severity, context, destination, owner, and response. 6. Avoid reacting to transient conditions. 7. Resource state change versus metric condition. 8. Excessive matches can trigger unsafe or costly work. 9. Duplicate delivery must not repeat harmful effects. 10. Service behavior versus control-plane API activity. 11. Time, environment, resource, deployment, request/trace, and outcome. 12. Reduce durable exposure. 13. A failed route can silently remove evidence. 14. Misparsed data creates false fields and conclusions. 15. Observed record versus derived context. 16. Co-occurrence supports a hypothesis, not proof. 17. End-to-end unit of work versus one operation. 18. Sampling, missing instrumentation, propagation failure, or absent call. 19. Actual user diversity versus controlled repeatable journey. 20. Cost and volume versus rare-event visibility. 21. Unbounded dimensions increase cost and fragment analysis. 22. Agents, ingestion, connectors, queries, notifications, probes. 23. Establish user impact and blast radius. 24. Weights, question count, and passing score. 25. Correct signal interpretation plus tested alert, automation, correlation, diagnosis, recovery, privacy, and cost evidence.

## Readiness checklist

- I can explain units, dimensions, aggregation, intervals, windows, missing data, and alarm state behavior.
- I can distinguish Events, Monitoring, Logging, Audit, Log Analytics, traces, RUM, and synthetic monitoring by evidence need.
- I can correlate user impact to application, dependency, resource, change, and security evidence.
- I can design safe automation and manage telemetry access, retention, privacy, cardinality, and cost.

## Places to learn

This is a selective learning path, not a complete list of OCI observability resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official OCI Observability Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oracle-cloud-infrastructure-observability-professional-2026/162237) | Oracle account/subscription may be required | **9+ hours** as published by Oracle University |
| [OCI monitoring and observability guidance](https://docs.oracle.com/en-us/iaas/Content/cloud-adoption-framework/monitoring-and-observability.htm) | Public | **10–14 hours** targeted study |
| Eight labs in this guide | Authorized OCI tenancy or local substitutes | **24–36 hours** plus two timed incident drills |
