---
exam_code: SPLUNK-O11Y-METRICS-USER
vendor_id: splunk
official_blueprint: https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-o11y-cloud-metrics-user.pdf
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-10-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-10-28
---

# Splunk O11y Cloud Certified Metrics User Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live certification page, four-page public blueprint, current Splunk Observability Cloud/OpenTelemetry documentation, and selected resources were checked October 28, 2026. This contains original learning material, not exam items. Recheck the [certification page](https://www.splunk.com/en_us/training/certification-track/splunk-o11y-cloud-certified-metrics-user.html) and [official blueprint](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-o11y-cloud-metrics-user.pdf) before scheduling.

**Current baseline:** OpenTelemetry ingest 10%; Metrics Concepts 15%; Built-in Content 10%; Visualizing Metrics 15%; Introductory Detectors 10%; Efficient Dashboards/Alerts 10%; Analytics 15%; Detector Use Cases 15%.<br>
**Exam contract:** foundational; 54 questions; 60 total minutes including three minutes for the exam agreement.<br>
**Prerequisites:** no prerequisite exams.<br>
**Lifecycle/product boundary:** active; no retirement/replacement announcement was visible. Splunk Observability Cloud is a continuously delivered SaaS product, so UI, navigation, integrations, entitlements, and defaults can change. Use the blueprint for exam scope and current tenant/official docs for operation.<br>

## How to use this guide

Use a sandbox organization and synthetic workload. For each chart or detector, preserve the metric and dimensions, aggregation/rollup, resolution, analytic pipeline, missing/late-data policy, population, threshold, duration, notification/routing, owner, and expected action.

> **About related items:** `Related item:` adds reliability, telemetry governance, OpenTelemetry, or operational context; it is not claimed as exact blueprint wording.

## Blueprint map

| Capability | Weight | Evidence |
|---|---:|---|
| OTel collection and metric model | 25% | Valid collector pipeline plus metric/MTS/metadata trace |
| Built-in content and visualization | 25% | Correct chart interpretation and navigable dashboard |
| Detector construction and dashboard efficiency | 20% | Actionable detector, mute, links/instructions, failure tests |
| Analytics and production detector patterns | 30% | Correct population/time-window math and low-noise cyclic/ephemeral monitoring |

## 1. Get metrics in with OpenTelemetry — 10%

OpenTelemetry separates APIs/SDKs/instrumentation from collectors and backends. A collector configuration composes **receivers → processors → exporters** into service pipelines; extensions support concerns such as health/authentication. Deploy the supported Splunk Distribution of the OpenTelemetry Collector on compatible Linux, provide realm/access token through approved secret handling, enable needed receivers, export to the correct endpoint, and validate collector health plus received metrics.

YAML structure/indentation, component IDs, pipeline references, environment-variable expansion, permissions, endpoint/DNS/TLS/proxy, invalid tokens/realm, ports, resource pressure, and exporter queues are common failure areas. Validate config before restart, inspect service logs and internal telemetry, then prove a known metric and dimensions in the backend. Do not print tokens in diagnostics.

> **Related item:** Collector processors can enrich, batch, filter, transform, sample, or protect telemetry. Every processor changes cost or meaning; keep configuration reviewed, versioned, canaried, and observable.

## 2. Metrics concepts — 15%

A metric identifies a measurement; a datapoint contains a value at a timestamp plus identifying metadata; a metric time series (MTS) is the unique stream formed by metric name and its dimension set. Dimensions identify/filter/group series and are part of MTS cardinality. Properties enrich metadata without necessarily defining MTS identity in the same way. Metadata source and precedence matter when host/cloud/Kubernetes/integration attributes overlap.

Resolution is the time granularity returned/displayed. Rollups summarize datapoints into resolution windows. Common rollups—average, sum, min, max, count, latest, rate/delta depending on metric type—answer different questions. A counter total usually needs rate/delta or appropriate sum semantics; a gauge is sampled state. Chart resolution may coarsen with long time ranges, changing visible peaks and totals.

High-cardinality dimensions create many MTS, increasing cost and analytic complexity. Use stable bounded identifiers, avoid unbounded request/user IDs, and define naming/unit/type/owner conventions.

## 3. Built-in content and Kubernetes navigation — 10%

Built-in navigators/dashboards provide curated metrics, filters, charts, alerts, and drilldowns for supported integrations. Confirm the expected integration, data, permissions, and time range before diagnosing an empty view. Interpret every chart from signal, population, aggregation, rollup, analytics, resolution, and missing-data behavior.

Kubernetes Navigator moves among cluster, node, namespace, workload, pod, and container context. Use filters and linked signals to correlate saturation, errors, restarts, scheduling, and resource requests/limits. Cluster Analyzer presents detected conditions to focus investigation; it is evidence, not automatically root cause. Built-in Kubernetes dashboards help validate scope and compare infrastructure signals. Alert subscription controls who receives existing detector notifications; ownership and response remain necessary.

## 4. Visualizing metrics — 15%

Search/select a metric, filter dimensions, then aggregate/group and apply analytics in a deliberate order. Choose line/area for time trends, single value for current/summary status, list/table for ranked populations, histogram/heatmap for distributions where supported, and event overlays for change correlation. A visually attractive chart with ambiguous units, population, or time math is not useful.

Dashboards group related charts; dashboard groups organize dashboards. Add title, purpose, variable/filter scope, units, data source, owner, expected ranges, and response links. Test default and alternate variables, empty/error states, long/short time ranges, resolution changes, timezone, permissions, and high-cardinality populations.

Rollup operates within time buckets; analytics operate across or between time series/windows. Order matters. Validate chart math against a small hand-calculated dataset.

## 5–6. Detectors, muting, and efficient operational content — 20%

A detector evaluates one or more signal flows/rules and emits alert events when conditions meet severity/duration criteria. Create from a validated chart when its signal is correct; clone only after reviewing inherited population, links, recipients, thresholds, and ownership; use standalone construction when chart context is unnecessary. Test clear as well as fire behavior.

Muting suppresses notifications/events under a scoped condition/time; it should not silently become permanent blindness. Set owner, reason, scope, start/end, review, and maintenance correlation. Prefer precise scope over muting a whole detector.

Reduce cognitive load: dashboard instructions state purpose and response; single-instance dashboards preserve a narrowed entity context; event overlays connect deploy/change/alert events; local data links route selected dimensions to related dashboards or systems; customized alert messages include what, scope, severity, timing, observed/threshold value, likely impact, dashboard/runbook, owner, and routing context.

Late datapoints can revise windows after evaluation. Extrapolation policies define how missing values are estimated/handled. Choose policy from source behavior and desired false-positive/false-negative tradeoff, then simulate delay, loss, and recovery.

> **Related item:** An alert is valuable only if a recipient can decide and act. Track ownership, actionability, precision, recall, time-to-detect, time-to-resolve, and stale detectors.

## 7. Analytics — 15%

To total across sources, aggregate the intended population with correct units and rollup; do not add rates and totals indiscriminately. Combining plots enables ratios, derived signals, comparisons, and correlations, but align filters, dimensions, units, and resolution first. Guard ratios against zero denominators and mismatched populations.

Moving windows slide continuously over recent duration; calendar windows align to calendar boundaries/timezone. Timeshift/cycle comparisons can compare hour/day/week, but seasonality, holidays, deployments, missing data, and DST affect meaning. Apply analytics before or after aggregation based on the question; calculating per-MTS then aggregating can differ from aggregating then calculating.

Apply functions to subsets by filters/grouping, and preserve enough dimensions to identify the affected entity without uncontrolled cardinality. Hand-calculate a tiny dataset to verify order of operations.

## 8. Detector patterns — 15%

Common detector failures include wrong population, rollup/resolution, static threshold, duration, missing/late-data policy, excessive cardinality, no clear condition, notification routing, permissions, or stale ownership. Troubleshoot with signal preview, historical replay, rule state, alert events, delayed/missing data simulation, and known-good intervals.

Population monitoring should detect both aggregate impact and outliers. Percent-of-population, percentile/deviation, top-N, and grouped rules answer different questions. Avoid flapping with duration, hysteresis/separate clear conditions, appropriate resolution, smoothing, and missing-data policy—without delaying a true urgent event.

Cyclic metrics need calendar/cycle-aware or historical comparison rather than one static threshold. Large fleets need scalable grouped/population signals and actionable entity context, not one manually cloned rule per host. Ephemeral infrastructure requires stable workload/service dimensions, discovery-aware population, sensible extrapolation, and treatment of normal disappearance versus failure.

## Integrated scenarios

### Scenario 1: Linux service onboarding

Deploy/configure a collector with synthetic host/service metrics; prove receiver-to-exporter health; define bounded dimensions; create charts with validated rollups; link to a runbook; alert on sustained error/saturation; simulate late/lost data and recovery.

### Scenario 2: Kubernetes regression

Use Navigator, Cluster Analyzer, built-in dashboards, events, and workload/pod/container dimensions to distinguish rollout, node pressure, restart, and requests/limits hypotheses. Produce an actionable detector without alerting on normal pod churn.

### Scenario 3: Seasonal fleet detector

Build weekly comparison and population ratio for many ephemeral instances. Test zero denominator, DST, missing/late data, cardinality, flapping, muting, message context, and clear behavior.

## Current product context — separate from exam objectives

> **Related item:** October 2026 Observability Cloud notes change APM tag `!=` filtering for missing tags and describe Controlled Availability for MetricSets that include spans without parents. These changes can alter metric values, charts, detector behavior and cardinality; the additional-spans feature is not universal. Check realm and account rollout before comparing or changing a production signal. [October 2026 release notes](https://help.splunk.com/en/splunk-observability-cloud/release-notes/october-2026)

## Hands-on labs

1. Install/configure OTel Collector on Linux; diagnose five config/network/auth/resource faults.
2. Map metric → datapoints → MTS and demonstrate a cardinality explosion safely.
3. Compare rollups/resolutions against hand calculations for gauge and counter data.
4. Investigate a Kubernetes fault using Navigator, Analyzer, and built-in dashboards.
5. Build a dashboard group with variables, instructions, event overlay, and local links.
6. Create/clone/standalone detectors and a time-bounded scoped muting rule.
7. Simulate late/missing datapoints under different extrapolation policies.
8. Build ratio, total, moving/calendar window, and cycle comparison analytics.
9. Create non-flapping population and seasonal detectors.
10. Monitor ephemeral entities using stable workload identity and disappearance tests.

## Original readiness checks

1. Name the collector pipeline component types. 2. What should be checked after collector service start? 3. Why protect realm/access token? 4. What defines an MTS? 5. How do dimensions and properties differ? 6. What is resolution? 7. What does a rollup do? 8. Why can a long time range hide peaks? 9. What causes metric cardinality growth? 10. What must precede built-in-content diagnosis? 11. What scopes does Kubernetes Navigator traverse? 12. Why is Cluster Analyzer not root-cause proof? 13. Which chart fits a time trend? 14. What belongs in dashboard instructions? 15. Why does analytic order matter? 16. What should variables be tested against? 17. What does a detector evaluate? 18. When is chart-created detector appropriate? 19. What must be reviewed after clone? 20. What makes a muting rule safe? 21. What does a local data link provide? 22. What belongs in an alert message? 23. Why do late datapoints matter? 24. What does extrapolation control? 25. How do moving/calendar windows differ? 26. What invalidates a ratio? 27. Why align populations before combining plots? 28. Why can aggregate-then-function differ? 29. What creates detector flapping? 30. Name two anti-flapping techniques. 31. How should cyclic data be monitored? 32. Why avoid one detector per ephemeral instance? 33. Which dimensions survive pod churn? 34. How should disappearance be interpreted? 35. Which four domains weigh 15%? 36. How many questions/minutes? 37. Are prerequisite exams required? 38. What SaaS caveat applies? 39. What must a readiness lab never ingest? 40. What must be rechecked before scheduling?

## Answer key

1. Receivers, processors, exporters in service pipelines. 2. Logs/internal telemetry plus a known backend metric/dimensions. 3. It authorizes telemetry access and is a secret. 4. Metric name plus unique dimension set. 5. Dimensions identify/group MTS; properties enrich metadata without the same identity role. 6. Returned/displayed time granularity. 7. Summarizes datapoints within resolution windows. 8. Coarser rollups smooth short peaks. 9. Unbounded/highly varied dimension values. 10. Integration/data, permissions, time range, filters. 11. Cluster/node/namespace/workload/pod/container. 12. It surfaces evidence/conditions requiring correlation. 13. Line/area. 14. Purpose, scope, interpretation, owner and action/runbook. 15. Aggregation/function sequence changes math. 16. Default/alternate/empty/error/high-cardinality states. 17. Signals/rules over time/population. 18. When chart signal is already validated. 19. Population, links, recipients, threshold, ownership. 20. Narrow scope, owner/reason, bounded time/review. 21. Context-aware navigation using dimensions. 22. What/scope/severity/time/value/threshold/impact/dashboard/runbook/owner. 23. They can revise evaluated windows and alert state. 24. Missing-data estimation/handling. 25. Sliding recent duration versus calendar-aligned boundary/timezone. 26. Zero denominator, unit or population mismatch. 27. Otherwise comparisons/ratios combine unlike series. 28. Functions are not always distributive. 29. Noise around threshold, resolution, delay/loss, poor clear logic. 30. Duration, hysteresis, smoothing, suitable resolution/clear condition. 31. Cycle/calendar-aware baseline/comparison. 32. Churn, management load, noise and cost. 33. Service/workload/namespace/cluster and other stable bounded identifiers. 34. Against expected lifecycle and missing-data policy. 35. Metrics, Visualization, Analytics, Common-use Detectors. 36. 54; 60 total including agreement. 37. No. 38. UI/features/defaults/entitlements can change continuously. 39. Production secrets or sensitive/real customer data. 40. Live page/blueprint, tenant UI/docs, price/delivery/retake/renewal.

## Final readiness checklist

- [ ] I can deploy, configure, troubleshoot, and securely operate a Linux OTel Collector.
- [ ] I can explain and hand-calculate MTS, metadata, cardinality, rollup, resolution, and analytic order.
- [ ] I can investigate built-in and Kubernetes content without treating correlation as proof.
- [ ] I can build usable dashboards, links, event overlays, and alert messages.
- [ ] I can build/troubleshoot non-flapping detectors for fleets, cycles, and ephemeral infrastructure.
- [ ] I completed all ten labs and tested missing, late, empty, and recovery paths.
- [ ] I rechecked the live SaaS, exam, and policy contracts.

## Key terms and phrases

**Get metrics in with OpenTelemetry**

| Term or phrase | Meaning |
|---|---|
| [OpenTelemetry Collector](#1-get-metrics-in-with-opentelemetry-10) | A process that receives telemetry, processes it and exports it to a destination according to configured pipelines. |
| [OpenTelemetry](#1-get-metrics-in-with-opentelemetry-10) | A shared set of interfaces, data formats and tools for collecting telemetry and sending it to a backend. |
| [Processor](#1-get-metrics-in-with-opentelemetry-10) | The Collector component that transforms, filters or batches data before export. Its position can change what reaches the backend. |
| [Receiver](#1-get-metrics-in-with-opentelemetry-10) | The Collector component that accepts or scrapes telemetry at the beginning of a pipeline. |
| [Realm](#1-get-metrics-in-with-opentelemetry-10) | The deployment location used to identify the appropriate Splunk Observability Cloud endpoint. A valid token sent to the wrong endpoint may still fail. |
| [Instrumentation](#1-get-metrics-in-with-opentelemetry-10) | Code or an integration that emits telemetry from a workload. A collector cannot export a measurement that was never produced. |
| [Access token](#1-get-metrics-in-with-opentelemetry-10) | A credential whose configured scope authorizes requests such as ingesting telemetry. Keep its value out of diagnostic output. |
| [Exporter](#1-get-metrics-in-with-opentelemetry-10) | The Collector component that sends telemetry to a destination. Verify both its delivery and the backend's receipt of a known metric. |

**Metrics concepts**

| Term or phrase | Meaning |
|---|---|
| [Metric time series (MTS)](#2-metrics-concepts-15) | A sequence of timestamped values for a metric with a specific combination of dimensions. |
| [Dimension](#2-metrics-concepts-15) | A key-value attribute that distinguishes one metric series from another, such as service name or deployment region. |
| [Cardinality](#2-metrics-concepts-15) | The number of distinct dimension combinations for a metric. If all four services report from each of three regions and there are no other dimensions, the metric has 12 time series. |
| [Resolution](#2-metrics-concepts-15) | Time granularity used for data points shown or returned. A five-minute rollup can hide a spike visible in one-minute results. |
| [Delta](#2-metrics-concepts-15) | The change between two values. A cumulative request count moving from 80 to 92 increases by 12, assuming no reset. |
| [Rate](#2-metrics-concepts-15) | Change divided by elapsed time. Sixty additional requests in 30 seconds means an average of two requests per second. |
| [Datapoint](#2-metrics-concepts-15) | One measured value at a particular timestamp. Several datapoints sharing a metric and dimensions form a time series. |
| [Property](#2-metrics-concepts-15) | Metadata associated with monitored entities that can assist exploration or filtering. Dimension sets determine time-series identity. |
| [Counter](#2-metrics-concepts-15) | A cumulative measurement within a collection period or process lifetime. An increase from 100 to 160 over 30 seconds implies an average of 2 per second if no reset occurred. |
| [Gauge](#2-metrics-concepts-15) | A measurement of current state, such as queue length. It can rise or fall between successive observations. |
| [Host dimension](#2-metrics-concepts-15) | A dimension that identifies the host associated with measurements. Grouping a CPU metric by host shows whether one machine accounts for a fleet-wide spike. |

**Built-in content and Kubernetes navigation**

| Term or phrase | Meaning |
|---|---|
| [Filter](#3-built-in-content-and-kubernetes-navigation-10) | Restricts the series entering a chart or calculation, such as keeping only the production environment before computing an error rate. |
| [Navigator](#3-built-in-content-and-kubernetes-navigation-10) | An infrastructure view used to move from a fleet or cluster overview toward a particular workload and its metrics. |
| [Chart time range](#3-built-in-content-and-kubernetes-navigation-10) | The interval of observations shown on a chart. Changing from one hour to one week gives a longer view and can change the resolution at which measurements are displayed. |
| [Detector alert](#3-built-in-content-and-kubernetes-navigation-10) | The state raised for a signal when a detector rule triggers. A subscription can notify responders while the chart helps explain which measurements crossed the threshold. |

**Visualizing metrics**

| Term or phrase | Meaning |
|---|---|
| [Rollup](#4-visualizing-metrics-15) | A calculation that summarizes the points within a time interval for each series, such as a mean or a maximum. |
| [Event overlay](#4-visualizing-metrics-15) | Timestamped events displayed on the same chart as a metric. Overlaying a deployment on a latency chart helps determine whether their timing supports further investigation. |
| [Dashboard group](#4-visualizing-metrics-15) | An organizational container for related dashboards. A service team can group its latency, capacity and dependency dashboards so responders know where to look. |

**Detectors, muting, and efficient operational content**

| Term or phrase | Meaning |
|---|---|
| [Detector](#56-detectors-muting-and-efficient-operational-content-20) | A set of rules that evaluates a signal and produces alert events when defined conditions are met. |
| [Muting rule](#56-detectors-muting-and-efficient-operational-content-20) | A rule that suppresses matching alert notifications for a defined scope or interval, useful during planned maintenance. |
| [Extrapolation](#56-detectors-muting-and-efficient-operational-content-20) | Estimating values when new observations have not arrived. Check how this affects signals for short-lived or terminated workloads. |
| [Detector event](#56-detectors-muting-and-efficient-operational-content-20) | A timestamped occurrence a detector records when its alert condition changes state. Compare the event time with the metric that triggered it. |

**Analytics**

| Term or phrase | Meaning |
|---|---|
| [Aggregation](#7-analytics-15) | Combining multiple series into fewer results, such as summing request counts across instances grouped by service. |
| [Calendar window](#7-analytics-15) | An interval aligned to a calendar boundary such as a day in a specified time zone. It need not contain the same observations as the last 24 hours. |
| [Derived signal](#7-analytics-15) | A signal computed from other signals, such as errors divided by requests for the same population and interval. |
| [Moving window](#7-analytics-15) | A calculation over the most recent interval as time advances, such as mean latency over the trailing ten minutes. |
| [Timeshift](#7-analytics-15) | Aligning an earlier time interval with the present signal for comparison, for example comparing this Monday with the previous Monday. |
| [Grouping](#7-analytics-15) | Keeping separate statistics for selected dimensions. Grouping by service preserves service-level differences a fleet-wide total can hide. |

**Detector patterns**

| Term or phrase | Meaning |
|---|---|
| [Missing-data policy](#8-detector-patterns-15) | The rule for interpreting absent measurements. A missing report can mean a failed collector or an intentionally retired instance. |
| [Detector duration](#8-detector-patterns-15) | How long a condition must persist to trigger. A duration can reduce transient noise at the cost of a later alert. |
| [Hysteresis](#8-detector-patterns-15) | Using different trigger and clear conditions to prevent rapid alarm state changes near a threshold. |
| [Percentile](#8-detector-patterns-15) | A value at or below which a given portion of observations falls. The 95th percentile describes the upper tail of latency better than its average alone. |

## Places to learn

This is not a complete list, and it is not meant to be consumed end to end. Choose resources for measured gaps. Times are planning estimates; access, price, tenant features, and availability change.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official certification page](https://www.splunk.com/en_us/training/certification-track/splunk-o11y-cloud-certified-metrics-user.html) and [blueprint](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-o11y-cloud-metrics-user.pdf) | Free | 45–75 min | Canonical scope |
| [Splunk Observability Cloud docs](https://help.splunk.com/en/splunk-observability-cloud) | Free | 15–30 hr targeted | Current product behavior; tenant entitlements vary |
| [OpenTelemetry Collector docs](https://opentelemetry.io/docs/collector/) | Free/open source | 5–10 hr targeted | Collector concepts; use Splunk docs for supported packaging/export |
| [Official Metrics User track flowchart](https://www.splunk.com/en_us/pdfs/training/splunk-o11y-cloud-certified-metrics-user-track.pdf) | Free self-paced and selected paid options; account/access may vary | Combined runtime not stated; individual paths vary | Recommended learning sequence, not an exam prerequisite; check current catalog |
| [Fundamentals of Metrics Monitoring](https://www.splunk.com/en_us/pdfs/training/fundamentals-of-metrics-monitoring-course-description.pdf) and [Visualizing and Alerting](https://www.splunk.com/content/dam/splunk2/en_us/pdfs/training/visualizing-and-alerting-in-splunk-im-course-description.pdf) | Paid instructor-led/blended training; check current delivery | 6 hours; 4.5-hour instructor-led portion respectively | Optional metric/MTS and dashboard/detector practice; neither covers the whole blueprint |
| Sandbox tenant plus synthetic Linux/Kubernetes metrics portfolio | Trial/employer/partner access may be needed | 20–40 hr | Applied evidence; never use production secrets/data |
