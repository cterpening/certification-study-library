---
exam_code: 1Z0-997-26
vendor_id: oracle
official_blueprint: https://mylearn.oracle.com/ou/learning-path/become-an-oci-architect-professional-2026/163270
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-04
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-04
---

# 1Z0-997-26 Oracle Cloud Infrastructure Architect Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide maps Oracle University's public 2026 learning-path scope checked September 4, 2026. It is unofficial and may contain errors. The [official OCI Architect Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oci-architect-professional-2026/163270) is authoritative.

**Assessment contract exposed by the current path:** Oracle Cloud Infrastructure Architect Professional, exam 1Z0-997-26, 90 minutes.<br>
**Published scope:** high availability and disaster recovery; cloud-native solutions; Terraform and Resource Manager; security services; Base Database Service and Autonomous Database; Monitoring and Logging.<br>
**Source boundary:** the public path exposes capability groups rather than weights, question count, or passing score. This guide preserves that boundary. **VERIFY CURRENT** in MyLearn before scheduling.

## How to use this guide

Treat every prompt as an architecture review. Extract constraints, draw control and data paths, declare failure boundaries, compare at least two viable designs, and state how the chosen design will be deployed, observed, recovered, and paid for. Build only in an authorized tenancy and remove resources after collecting evidence.

> **About related items:** A `Related item:` callout adds practical architecture context. It is supporting knowledge, not a claim that its wording appears in Oracle's published scope.

## Objective map

| Published capability | Professional proof |
|---|---|
| High availability and disaster recovery | A tested service-recovery plan connects dependencies, recovery groups, ordering, RPO/RTO, switchover, and return-to-service evidence |
| Cloud-native solutions | Runtime choices and service boundaries support scaling, delivery, security, and failure isolation |
| Infrastructure as code | Versioned Terraform and Resource Manager workflows produce controlled, reviewable, repeatable change |
| Security services | Identity, network, application, certificate, key, and administrative controls form one traceable defense system |
| Databases | Base Database Service or Autonomous Database is selected from workload and operating constraints rather than habit |
| Observability | Metrics and logs prove service health, explain failure, and trigger useful response |

## 1. High availability and disaster recovery

Start with business services and dependencies, not regions and products. Translate availability targets, RPO, RTO, maximum tolerable outage, consistency, residency, and recovery authority into a failure model. Distinguish a fault-domain or availability-domain failure from regional loss, destructive change, credential compromise, and dependency failure.

Use redundancy only where the complete request and state path remains viable. Load balancers, compute capacity, DNS, identity, keys, artifacts, data, and operator access may each need a recovery design. Backups provide recoverable copies; replication reduces data lag; neither proves that an application can restart correctly.

For Full Stack Disaster Recovery, define protected applications as recovery groups, model dependencies and sequencing, create plans for switchover or failover, perform prechecks, and capture plan-run evidence. Design failback and data reconciliation before declaring the service recoverable.

> **Related item:** A low database RPO does not imply a low application RTO when images, secrets, network paths, DNS, or approval steps are missing at the recovery site.

## 2. Cloud-native solutions

Choose VMs, Container Instances, OKE, or Functions from execution duration, orchestration, scaling, isolation, portability, networking, and operations requirements. Container Registry stores versioned images; an immutable digest gives stronger deployment identity than a mutable tag. Keep build identity, runtime identity, and human administration separate.

In OKE, reason across cluster control, node pools or virtual nodes, workload scheduling, Services and ingress, configuration, secrets, persistent state, disruption, and upgrades. Define resource requests and limits, readiness and liveness behavior, rollout safety, and capacity during failure.

Functions suit bounded event-driven work; API Gateway provides a managed API boundary for routing, authentication, transformation, validation, and throttling. Make retries, idempotency, timeouts, dead-letter handling, and downstream backpressure explicit. Container Instances can be appropriate when containers need direct execution without a complete Kubernetes control model.

## 3. Infrastructure as code

Treat Terraform configuration, provider constraints, modules, state, plans, policies, and promotion as one delivery system. Pin intentional versions, make inputs and outputs clear, protect remote state, and review saved plans before applying. Separate reusable modules from environment composition and avoid secrets in configuration, state, logs, or outputs.

Resource Manager provides managed Terraform stacks, jobs, state, configuration sources, drift detection, and private endpoints. Give the stack principal only the permissions needed by its resources. A successful apply is not sufficient evidence: verify service behavior, alarms, policy boundaries, and rollback or forward-fix options.

Drift requires a decision. Import or codify an approved emergency change, replace an invalid resource, or revert unauthorized state. Do not automatically overwrite production simply to make configuration and reality match.

## 4. Security architecture

Build controls around trust transitions. Use federation and short-lived access for people, dynamic groups and resource or instance principals for workloads, scoped policies, and logged emergency access. Trace every permission from principal through verb, resource, compartment, and condition.

Use Bastion for controlled administrative sessions to private resources instead of permanent public management endpoints. Combine route intent with NSGs or security lists, Network Firewall inspection policy, and service-specific controls. WAF protects supported web entry points; it does not replace application authorization or network segmentation.

Certificates establish endpoint identity and encrypted transport, while Vault and Key Management protect keys and secrets according to ownership, rotation, recovery, and deletion requirements. Test rotation consumers and define what happens when a key, certificate, secret, or identity provider is unavailable.

## 5. Database architecture

Select Base Database Service or Autonomous Database from compatibility, control, administration, scaling, patching, availability, recovery, connectivity, performance, and cost constraints. Avoid treating “managed” as “no operations”: access, workload design, observability, recovery tests, and data governance remain architectural responsibilities.

Place database connectivity on private, explainable paths. Account for connection management, service names, authentication, encryption, maintenance behavior, backup retention, restore targets, and cross-region strategy. Validate query and transaction behavior during failover rather than checking only that a database resource reports available.

## 6. Observability and architecture governance

Define service-level symptoms first, then connect OCI Monitoring metrics and alarms to resource and application causes. Use Logging for service, custom, and audit evidence, with retention and access aligned to investigation and compliance needs. Correlate telemetry by time, request, resource, deployment, and region.

An alarm should identify an actionable condition, carry useful context, route to an owner, and recover cleanly. Test missing data, noisy thresholds, notification failure, and automation safeguards. Dashboards support decisions only when units, aggregation, dimensions, and time windows are understood.

Close the architecture loop with cost estimates, quotas, budgets, capacity tests, documented assumptions, and architecture decision records. Revisit the design when workload, threat, region, feature, or price assumptions change.

## Integrated practice scenarios

1. **Regulated regional service:** Design a private three-tier service with explicit RPO/RTO, controlled administration, Base Database Service, immutable delivery, and Full Stack Disaster Recovery orchestration.
2. **Global cloud-native API:** Select OKE, Functions, Container Instances, API Gateway, and Autonomous Database components; design safe scaling, regional recovery, security boundaries, and request-level telemetry.
3. **Shared enterprise landing zone:** Build compartment, network, policy, key, Terraform, logging, quota, and chargeback patterns for independent teams without creating an unrestricted shared operator.

## Hands-on labs

1. Convert one narrative into measurable service, data, security, residency, and cost constraints plus a declared failure model.
2. Draw primary and recovery dependency graphs; create a paper or authorized Full Stack Disaster Recovery plan with prechecks, ordering, and evidence gates.
3. Compare OKE, Container Instances, Functions, and VMs for three workloads and defend each rejection.
4. Deploy a small container by immutable digest, test a failed readiness condition, and observe rollout behavior.
5. Build a Terraform or Resource Manager stack using remote protected state, a reviewed plan, scoped permissions, verification, and cleanup.
6. Trace one request through WAF, load balancing, network policy, workload identity, key/secret use, and a private database connection.
7. Run a backup/restore or paper recovery exercise and measure data loss, restoration time, application validation, and failback work.
8. Create a dashboard and two actionable alarms, inject one safe failure, correlate metrics and logs, and write the architecture decision record.

## Original readiness checks

1. Availability target versus failure model? 2. RPO versus RTO? 3. Backup versus replication? 4. What does Full Stack Disaster Recovery orchestrate? 5. Why plan failback? 6. Mutable tag risk? 7. OKE readiness versus liveness? 8. Function retry hazard? 9. When prefer Container Instances? 10. Terraform plan purpose? 11. Why protect state? 12. Resource Manager principal scope? 13. Legitimate drift response? 14. Bastion benefit? 15. Route rule versus NSG? 16. Network Firewall versus WAF? 17. Certificate versus key versus secret? 18. Base Database versus Autonomous decision? 19. Why test application recovery? 20. Symptom metric versus cause metric? 21. What makes an alarm actionable? 22. Missing telemetry risk? 23. Quota versus budget? 24. Why record rejected designs? 25. What exam details remain unpublished? 26. What proves professional readiness?

### Answer guide

1. A target has meaning only against declared failures. 2. Acceptable data loss versus restoration time. 3. Recoverable copy versus maintained secondary state. 4. Cross-stack recovery dependencies and ordered actions. 5. Returning safely can require reconciliation and another outage. 6. It can resolve to different content. 7. Traffic eligibility versus process recovery. 8. Duplicate side effects without idempotency. 9. Direct container execution without Kubernetes orchestration. 10. Review intended change before execution. 11. It can contain sensitive data and governs resource ownership. 12. Minimum resources and actions required by the stack. 13. Codify, import, replace, or revert after approval. 14. Time-bounded audited access without permanent public management. 15. Next-hop choice versus traffic permission. 16. Network traffic inspection versus supported web-edge protection. 17. Endpoint identity, cryptographic control, and sensitive value. 18. Compatibility, control, operating model, recovery, performance, and cost. 19. Resource availability does not prove usable service or correct transactions. 20. User impact versus underlying explanation. 21. Clear condition, context, owner, and response. 22. Silence can be mistaken for health. 23. Consumption boundary versus financial signal. 24. Preserve assumptions and tradeoffs. 25. Weights, question count, and passing score. 26. Defensible designs plus tested deployment, security, failure, recovery, telemetry, and cost evidence.

## Readiness checklist

- I can turn ambiguous requirements into testable architecture constraints and a failure model.
- I can defend runtime, database, network, security, and recovery choices against credible alternatives.
- I can deploy repeatably, trace least privilege, and prove failure and recovery behavior.
- I can explain which facts Oracle publishes and which details remain intentionally unknown.

## Places to learn

This is a selective learning path, not a complete list of OCI architecture resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official OCI Architect Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oci-architect-professional-2026/163270) | Oracle account/subscription may be required | **26+ hours** as published by Oracle University |
| [OCI best practices and reference architectures](https://docs.oracle.com/en/solutions/oci-best-practices/) | Public | **10–14 hours** targeted study |
| Eight labs in this guide | Authorized OCI tenancy or paper design | **28–40 hours** plus two timed architecture reviews |
