---
exam_code: 1Z0-1084-26
vendor_id: oracle
official_blueprint: https://mylearn.oracle.com/ou/learning-path/become-an-oci-developer-professional-2026/162926
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-04
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-04
---

# 1Z0-1084-26 Oracle Cloud Infrastructure Developer Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide maps Oracle University's public 2026 learning-path scope checked September 4, 2026. It is unofficial and may contain errors. The [official OCI Developer Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oci-developer-professional-2026/162926) is authoritative.

**Assessment contract exposed by the current path:** Oracle Cloud Infrastructure Developer Professional, exam 1Z0-1084-26, 90 minutes.<br>
**Published scope:** cloud-native and microservices fundamentals; OKE and Container Registry; Functions and API Gateway; Streaming, Queue, and Events; OCI Streaming with Apache Kafka; Vault, image scanning, and testing; application observability.<br>
**Source boundary:** the public path exposes capabilities rather than weights, question count, or passing score. This guide does not infer them. **VERIFY CURRENT** in MyLearn before scheduling.

## How to use this guide

For each topic, produce a working request or event path and evidence for success, rejection, retry, scaling, failure, and recovery. Keep source, artifact, configuration, secret, and runtime identity distinct. Use only authorized OCI resources, synthetic data, and disposable environments.

> **About related items:** A `Related item:` callout adds practical development context. It is supporting knowledge, not a claim that its wording appears in Oracle's published scope.

## Objective map

| Published capability | Developer proof |
|---|---|
| Cloud-native fundamentals and microservices | Boundaries, contracts, state, failure, and ownership are explicit |
| OKE and Container Registry | An immutable image reaches a healthy, scalable workload through a controlled deployment |
| Functions and API Gateway | A secured API invokes bounded, observable, idempotent serverless work |
| Streaming, Queue, and Events | Delivery semantics, ordering, retries, poison messages, and backpressure are handled deliberately |
| OCI Streaming with Apache Kafka | Kafka-compatible producers and consumers use appropriate partition and consumer-group design |
| Testing and security | Controls are verified across code, image, identity, secret, API, and runtime boundaries |
| Observability | Metrics, logs, and traces reconstruct user-visible behavior and dependency failure |

## 1. Cloud-native and microservice design

Split services around cohesive business capabilities and independent change, not arbitrary code size. Define API or event contracts, ownership, data authority, compatibility, timeouts, and failure behavior. A microservice architecture trades local simplicity for distributed latency, partial failure, versioning, and operational work.

Design stateless request handling where practical, while explicitly locating durable state. Prefer asynchronous communication when temporal decoupling and buffering help; prefer synchronous calls when the caller needs an immediate outcome and can tolerate the dependency. Use correlation and idempotency keys across both.

Twelve-factor ideas—external configuration, disposable processes, explicit dependencies, and observable event streams—help, but do not replace OCI identity, networking, availability, or data design.

## 2. Containers, Container Registry, and OKE

Build small reproducible images, run as a non-root user where possible, pin trusted bases, scan dependencies and layers, and promote by digest. Container Registry stores images and manifests; repositories, IAM, retention, and regional availability belong in the delivery design.

In OKE, understand clusters, node pools or virtual nodes, pods, Deployments, Services, ingress, ConfigMaps, Secrets, storage, namespaces, service accounts, and network policy. Resource requests influence scheduling; limits bound consumption. Readiness controls traffic, liveness can restart a stuck container, and startup probes protect slow initialization.

Plan rolling updates, surge and unavailable capacity, disruption budgets, graceful termination, autoscaling signals, and rollback. A healthy pod count is not proof that an end-to-end request works.

## 3. Functions and API Gateway

Functions execute bounded code in response to invocation. Keep handlers small, configuration external, initialization deliberate, and downstream calls time-bounded. Account for concurrency, cold paths, retries, duplicate delivery, and idempotent side effects. Use workload principals rather than embedded user credentials.

API Gateway creates public or private API boundaries with deployments and routes. Design authentication and authorization, request validation, transformation, CORS only where needed, rate limiting, response mapping, and backend timeouts. Version contracts without silently breaking clients.

> **Related item:** An accepted request is not necessarily completed work. For asynchronous operations, return a stable operation identity and expose status or a completion event.

## 4. Events, Queue, and Streaming

OCI Events routes matched resource state-change events to supported actions. Treat rules as filters over event envelopes and verify that the target has permission and handles duplicates. Events are signals, not a durable business ledger.

Queue supports asynchronous work distribution. Design visibility or processing timeouts, acknowledgment, retry limits, dead-letter handling, poison-message investigation, and scale based on age and backlog—not merely message arrival rate.

Streaming supports ordered records within partitions and parallel consumption across partitions. Choose partition keys from ordering and load-distribution requirements. Track offsets, lag, retention, replay, schema compatibility, and idempotent downstream processing.

## 5. OCI Streaming with Apache Kafka

Use the Kafka-compatible interface when existing Kafka clients and ecosystem integration are required, while checking OCI-specific endpoints, authentication, supported behavior, and limits. Separate broker-compatible client configuration from application delivery semantics.

Partitions define the ordering and scaling unit. A consumer group coordinates work so a partition is actively assigned within the group according to the client protocol. More consumers than useful partitions do not create more partition parallelism. Rebalancing, retries, offset commits, and side effects can produce duplicate processing; design for it.

## 6. Testing and application security

Layer unit, contract, integration, end-to-end, load, resilience, and security tests. Contract tests protect service evolution; integration tests prove OCI wiring and permissions; resilience tests reveal retry storms, dependency assumptions, and data loss paths. Use synthetic data and scoped nonproduction resources.

Apply least privilege to people, build systems, functions, pods, gateways, and services. Store secrets in Vault, fetch them through a workload identity, prevent accidental logs, rotate deliberately, and test consumers after rotation. Image scanning is a decision input: define severity policy, exceptions, remediation ownership, and promotion gates.

Protect APIs against invalid input, excessive work, unintended exposure, and confused-deputy paths. Validate authorization at the resource operation, not only at the outer gateway.

## 7. Application observability

Instrument service-level outcomes, latency, errors, saturation, dependency calls, retries, queue age, consumer lag, and deployment identity. Structured logs should carry correlation context without secrets. Distributed traces connect service spans and expose critical paths, but sampling and missing instrumentation limit conclusions.

Build alerts from user impact and actionable failure conditions. A dashboard should let a responder move from symptom to suspect deployment, dependency, partition, route, or policy. Test telemetry during degraded behavior, not only normal operation.

## Integrated practice scenarios

1. **Order API:** Publish a secured API Gateway route to a Function that validates a request, writes an idempotent command to Queue, and exposes correlated status without duplicate fulfillment.
2. **Media-processing platform:** Promote scanned images from Container Registry to OKE, process jobs asynchronously, autoscale on backlog, and preserve failure evidence in a dead-letter workflow.
3. **Real-time telemetry service:** Partition a Kafka-compatible stream, operate consumer groups, evolve an event schema, measure lag, and replay safely into a new projection.

## Hands-on labs

1. Write two service contracts with compatibility, timeout, retry, identity, and error rules; test a breaking and nonbreaking change.
2. Build and scan a minimal container, push it to an authorized registry, record its digest, and reject a deliberately unsafe build.
3. Deploy the image to OKE or a local Kubernetes substitute; test readiness, liveness, resources, rollout, and rollback.
4. Implement a small Function behind an API route with validation, scoped identity, safe configuration, and an idempotency test.
5. Route a synthetic resource event to an authorized target and prove both a matching and nonmatching rule.
6. Process Queue messages with retry, acknowledgment, poison-message, and dead-letter evidence.
7. Produce partitioned records and operate two consumer groups through lag, restart, replay, and duplicate-delivery tests using OCI Streaming or a local Kafka-compatible lab.
8. Correlate API, function, queue or stream, and workload telemetry during one injected dependency failure; write the diagnosis and fix.

## Original readiness checks

1. Good service boundary? 2. Sync versus async decision? 3. Why idempotency? 4. Immutable digest benefit? 5. Request versus limit? 6. Readiness versus liveness? 7. Rollout safety controls? 8. Function retry hazard? 9. Gateway authentication versus application authorization? 10. Why validate input early? 11. Event rule purpose? 12. Queue acknowledgment meaning? 13. Poison-message response? 14. Partition-key tradeoff? 15. Consumer lag meaning? 16. Replay prerequisite? 17. Consumer-group role? 18. More consumers than partitions? 19. Offset commit hazard? 20. Contract versus integration test? 21. What does image scanning prove? 22. Safe Vault use? 23. Useful correlation field? 24. Trace limitation? 25. User-impact alert? 26. Secret-logging risk? 27. What remains unpublished? 28. What proves professional readiness?

### Answer guide

1. Cohesive capability, owned data, and independent change. 2. Immediate coupled result versus buffered temporal decoupling. 3. Retries and duplicates must not repeat harmful effects. 4. It identifies exact content. 5. Scheduling guarantee versus consumption ceiling. 6. Traffic eligibility versus process restart. 7. Capacity, health gates, graceful termination, and rollback. 8. Duplicate side effects. 9. Entry identity versus permission for the actual operation. 10. Reduce unsafe or expensive work. 11. Match state-change envelopes to actions. 12. Processing completed under the consumer's contract. 13. Isolate, preserve, alert, diagnose, and remediate. 14. Ordering locality versus load balance. 15. Distance between produced and processed work. 16. Retained data, compatible consumers, and idempotent effects. 17. Coordinate partition assignments among cooperating consumers. 18. They cannot add partition parallelism. 19. Failure around processing and commit can lose or repeat work depending on the design. 20. Interface compatibility versus live component wiring. 21. Known findings at scan time, not total safety. 22. Scoped workload retrieval, no disclosure, tested rotation. 23. Request, trace, message, or operation identity. 24. Sampling and uninstrumented dependencies leave gaps. 25. Actionable evidence of customer harm. 26. Durable credential exposure. 27. Weights, question count, and passing score. 28. Working systems plus evidence for security, delivery, failure, replay, and diagnosis.

## Readiness checklist

- I can implement and defend synchronous, asynchronous, container, serverless, and Kafka-compatible designs.
- I can trace source to immutable artifact to runtime identity and observable request or event.
- I test retries, duplicates, unhealthy rollout, poison messages, lag, secret rotation, and dependency failure.
- I keep Oracle's published capability groups separate from supporting development knowledge.

## Places to learn

This is a selective learning path, not a complete list of OCI development resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official OCI Developer Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oci-developer-professional-2026/162926) | Oracle account/subscription may be required | **19+ hours** as published by Oracle University |
| [OCI services and developer documentation](https://docs.oracle.com/en-us/iaas/Content/services.htm) | Public | **10–14 hours** targeted study |
| Eight labs in this guide | Authorized OCI tenancy or local substitutes | **26–38 hours** plus one timed build-and-diagnose exercise |
