---
exam_code: 1Z0-1111-26
vendor_id: oracle
official_blueprint: https://mylearn.oracle.com/ou/learning-path/become-an-oracle-cloud-infrastructure-observability-professional-2026/162237
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-10-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-10-28
---

# 1Z0-1111-26 Oracle Cloud Infrastructure Observability Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide maps Oracle University's public 2026 learning-path scope checked October 28, 2026. It is unofficial and may contain errors. The [official OCI Observability Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oracle-cloud-infrastructure-observability-professional-2026/162237) is authoritative.

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

## Current product context — separate from exam objectives

> **Related item:** Oracle’s 2026 OCI refresh removed calendar years from certification names while keeping exam codes; Oracle states OCI credentials are valid for 24 months and professional-level courses require paid access. For observability, the OCI Monitoring API added dual-stack IPv4/IPv6 endpoints in September 2026. Verify endpoint, SDK, region, and client-network support before adopting IPv6; this release note is product context, not an exam-objective change.

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

## Key terms and phrases

**Monitoring metrics and alarms**

| Term or phrase | Meaning |
|---|---|
| [Metric dimension](#1-monitoring-metrics-and-alarms) | An attribute attached to a metric stream, such as a resource identifier, used to filter or group measurements. |
| [Alarm](#1-monitoring-metrics-and-alarms) | A rule that evaluates a metric condition over time and can notify a responder when the condition is met. |
| [Latency](#1-monitoring-metrics-and-alarms) | The time for a request or operation to complete, measured at a specified boundary from the selected start to finish. |
| [Metric](#1-monitoring-metrics-and-alarms) | A numeric measurement recorded over time, such as failed requests or queue depth, with defined units and dimensions. |
| [Service-level indicator (SLI)](#1-monitoring-metrics-and-alarms) | A measured aspect of service behavior, such as successful request latency or the percentage of requests returning a valid response. |
| [Metric namespace](#1-monitoring-metrics-and-alarms) | An identifier grouping related OCI metric definitions, commonly by service or publishing application. |
| [Statistic](#1-monitoring-metrics-and-alarms) | The calculation applied to samples in an interval, such as mean or maximum. The choice changes what the chart reveals. |
| [Query window](#1-monitoring-metrics-and-alarms) | The time interval considered when selecting, aggregating or comparing telemetry. |
| [Monitoring Query Language (MQL)](#1-monitoring-metrics-and-alarms) | The syntax OCI Monitoring uses to select metric streams and apply grouping or statistical operations. |

**Events and automated actions**

| Term or phrase | Meaning |
|---|---|
| [Event rule](#2-events-and-automated-actions) | A filter for resource-change events that sends matches to a configured action. |
| [Least privilege](#2-events-and-automated-actions) | Granting only the access a specific identity needs for its assigned work, then checking both allowed and denied actions. |
| [Compartment](#2-events-and-automated-actions) | A logical OCI grouping for resources, policy scope, ownership and cost reporting, which can span regions. |
| [Retry budget](#2-events-and-automated-actions) | A limit on repeated attempts to keep a temporary dependency failure from turning into runaway load. |
| [Idempotency](#2-events-and-automated-actions) | Designing repeated delivery or repeated requests to yield one intended business effect instead of duplicating the change. |

**Centralized Logging**

| Term or phrase | Meaning |
|---|---|
| [Log group](#3-centralized-logging) | An OCI container for organizing log objects and managing access to them. |
| [Control plane](#3-centralized-logging) | The management interfaces and services that configure resources and policies, as distinct from using the configured workload. |
| [Audit log](#3-centralized-logging) | Records of administrative actions that help identify who performed an operation, on what resource and when. |
| [Structured log](#3-centralized-logging) | A record with separately identifiable fields, enabling a search by request ID, service, status or other explicit attributes. |
| [Service log](#3-centralized-logging) | Records emitted by a supported OCI service about its activity, enabled and accessed under the service’s logging configuration. |
| [Custom log](#3-centralized-logging) | Application or host records collected into OCI Logging under a configured source, distinct from events emitted by OCI’s control plane. |

**Log Analytics**

| Term or phrase | Meaning |
|---|---|
| [Log enrichment](#4-log-analytics) | Adding derived or external context to a log record to make analysis easier while preserving the original observation. |
| [Parsing](#4-log-analytics) | Extracting structured fields from raw log content so timestamps, identities and outcomes can be queried consistently. |

**Application Performance Monitoring**

| Term or phrase | Meaning |
|---|---|
| [Span](#5-application-performance-monitoring) | A timed unit of work within a distributed trace, such as one service call made while handling a request. |
| [Real-user monitoring](#5-application-performance-monitoring) | Collecting measurements from actual client sessions to see how experience varies across users and environments. |
| [Synthetic monitoring](#5-application-performance-monitoring) | Running a controlled, repeatable request or user journey to observe availability or performance under known conditions. |
| [Availability](#5-application-performance-monitoring) | The ability of a service to remain usable for the intended requests over a specified measurement period. |
| [Distributed trace](#5-application-performance-monitoring) | A record linking the timed work of multiple instrumented components for a single request or transaction. |
| [Span parent](#5-application-performance-monitoring) | The span from which another operation was invoked, establishing a causal relationship within a trace. |
| [Sampling](#5-application-performance-monitoring) | Recording a subset of traces or observations according to a policy, which affects how confidently missing evidence can be interpreted. |

**Operational observability design**

| Term or phrase | Meaning |
|---|---|
| [Alert](#6-operational-observability-design) | A notification that a configured condition was met, requiring interpretation with its time window, source and affected scope. |
| [Runbook](#6-operational-observability-design) | A documented response procedure identifying evidence to gather, safe actions, decision owners and verification steps. |
| [Queue](#6-operational-observability-design) | A buffer of messages decoupling producers and consumers so work can continue asynchronously. |
| [Service-level objective (SLO)](#6-operational-observability-design) | A target value for a service measure over a defined time window, used to judge whether observed operation meets expectations. |
| [Blast radius](#6-operational-observability-design) | The set of users, services or resources affected by a fault, established from observed scope and dependencies. |

**Worked examples and practice**

| Term or phrase | Meaning |
|---|---|
| [Saturation](#integrated-practice-scenarios) | The extent to which demand uses up a resource’s available capacity, often becoming visible as queues or increased latency. |

## Places to learn

This is a selective learning path, not a complete list of OCI observability resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official OCI Observability Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oracle-cloud-infrastructure-observability-professional-2026/162237) | Paid Professional course; Oracle account sign-in | **9+ hours** as published by Oracle University |
| [OCI monitoring and observability guidance](https://docs.oracle.com/en-us/iaas/Content/cloud-adoption-framework/monitoring-and-observability.htm) | Public | **10–14 hours** targeted study |
| Eight labs in this guide | Authorized OCI tenancy or local substitutes | **24–36 hours** plus two timed incident drills |
