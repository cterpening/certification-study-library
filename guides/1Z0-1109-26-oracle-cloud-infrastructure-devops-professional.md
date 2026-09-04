---
exam_code: 1Z0-1109-26
vendor_id: oracle
official_blueprint: https://mylearn.oracle.com/ou/learning-path/become-an-oci-devops-professional-2026/162852
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-04
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-04
---

# 1Z0-1109-26 Oracle Cloud Infrastructure DevOps Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide maps Oracle University's public 2026 learning-path scope checked September 4, 2026. It is unofficial and may contain errors. The [official OCI DevOps Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oci-devops-professional-2026/162852) is authoritative.

**Assessment contract exposed by the current path:** Oracle Cloud Infrastructure DevOps Professional, exam 1Z0-1109-26, 90 minutes.<br>
**Published scope:** microservices on Container Registry, Container Instances, and OKE; OCI DevOps repositories, build and deployment pipelines, and artifact registries; Terraform and Resource Manager; IAM, key and secret management, and container-image security; Monitoring, Logging, and Events.<br>
**Source boundary:** the public path exposes five capability groups rather than weights, question count, or passing score. This guide preserves that boundary. **VERIFY CURRENT** in MyLearn before scheduling.

## How to use this guide

Practice complete delivery loops: commit → build → test → immutable artifact → approval → deployment → verification → observation → recovery. Every exercise should record identity, inputs, outputs, evidence, and failure behavior. Use only repositories, tenancies, and targets you are authorized to change.

> **About related items:** A `Related item:` callout adds practical DevOps context. It is supporting knowledge, not a claim that its wording appears in Oracle's published scope.

## Objective map

| Published capability | Delivery proof |
|---|---|
| Microservices with Container Registry, Container Instances, and OKE | A versioned image is deployed safely to an appropriate runtime and survives a controlled failure |
| OCI DevOps CI/CD components | Source, build, artifact, environment, deployment, approval, and rollback evidence form one traceable release |
| Terraform and Resource Manager | Infrastructure changes are versioned, planned, authorized, repeatable, and reconciled with drift |
| DevSecOps | Least privilege, protected keys and secrets, image policy, and promotion gates are enforced and tested |
| Monitoring, Logging, and Events | Delivery and runtime signals expose impact, automate bounded response, and support diagnosis |

## 1. Microservices, artifacts, and runtimes

Define service boundaries, API or event contracts, data ownership, timeouts, retries, and failure isolation before choosing a runtime. Containers package an application and dependencies; they do not by themselves supply orchestration, secure identity, durable state, or observability.

Container Registry stores container images and related artifacts. Build reproducibly, minimize the image, pin trusted bases, scan it, sign or attest where the delivery policy requires it, and promote by immutable digest. Keep artifact identity independent from an environment-specific configuration.

Use Container Instances when direct managed container execution fits the workload. Use OKE when scheduling, service discovery, rolling deployment, policy, scaling, and Kubernetes integration justify the orchestration layer. In OKE, connect requests and limits, probes, disruption, autoscaling, secrets, storage, and network policy to release safety.

## 2. OCI DevOps continuous integration and delivery

An OCI DevOps project groups repositories, connections, build pipelines, deployment pipelines, artifacts, environments, triggers, logs, and notifications. Trace a release from an exact commit through a build run to a digest or artifact version and a specific deployment run.

Build pipelines should make checkout, dependency resolution, compilation, unit and security tests, artifact creation, and delivery explicit. Separate build-time and runtime secrets. Fail closed when a required test or policy gate cannot produce trustworthy evidence.

Deployment pipelines deliver artifacts to supported environments such as OKE, compute instance groups, and Functions. Choose rolling, canary, or blue-green behavior from capacity, risk, state compatibility, validation, and recovery needs. Define approvals and separation of duties around production rather than relying on an informal message.

> **Related item:** Rollback is unsafe when a deployment includes an incompatible data migration. Prefer backward-compatible expand-and-contract changes and define a forward-fix path.

## 3. Infrastructure as code

Terraform configuration should express desired infrastructure in reviewed modules with clear inputs, outputs, provider constraints, and lifecycle intent. Protect state because it controls resource identity and may contain sensitive values. A plan is a proposed transition; review it in the same environment and identity context that will apply it.

Resource Manager provides managed stacks, configuration sources, jobs, state, drift detection, and private access options. Scope the stack principal to the resources it manages. Treat infrastructure and application delivery as coordinated but independently recoverable workflows.

Handle drift by classifying its cause and desired outcome. Codify or import an approved emergency change, replace a damaged resource, or revert unauthorized state. Do not normalize every difference automatically. Test modules and policies, verify deployed behavior, and preserve job evidence.

## 4. DevSecOps controls

Map human, pipeline, build runner, Resource Manager stack, deployment, and workload identities separately. Give each only required permissions and keep emergency access time-bounded and auditable. Protect repository connections, tokens, signing material, keys, and secrets from build output and logs.

Use Vault and workload principals so consumers retrieve secrets without embedding user credentials. Rotation is complete only when every consumer reloads or redeploys successfully. Define recovery and deletion behavior for keys before depending on them.

Image scanning identifies known findings at a moment in time. Combine scan policy with base-image maintenance, dependency inventory, provenance, configuration checks, runtime controls, exception expiry, and remediation ownership. Promote the same tested digest rather than rebuilding separately for production.

## 5. Measurement, instrumentation, and automation

Observe both delivery and service outcomes. Pipeline metrics include lead time, failure rate, duration, queueing, and recovery; runtime signals include availability, latency, errors, saturation, backlog, and dependency health. Use structured logs to connect commit, build, artifact, deployment, environment, resource, and request identities.

OCI Monitoring provides metrics and alarms; Logging centralizes supported service and custom logs; Events can route state-change notifications to bounded actions. Automations need narrow permissions, idempotency, rate limits, loop prevention, and human escalation when the response becomes risky.

Measure whether a canary is safe against a declared baseline. A green pipeline proves its encoded checks passed—not that omitted tests, permissions, data behavior, or user experience are correct.

## Integrated practice scenarios

1. **OKE application release:** Build a microservice image, scan and promote its digest, deploy a canary to OKE, evaluate health and service indicators, and complete or reverse the release.
2. **Infrastructure-plus-application change:** Use Resource Manager and OCI DevOps to add a dependency and deploy compatible code with ordered approval, verification, and recovery.
3. **Compromised build credential:** Detect unusual pipeline activity, contain identities and secrets, establish artifact provenance, rotate safely, and restore delivery with an evidence trail.

## Hands-on labs

1. Map source, build, artifact, deployment, runtime, and observability identities for one service; remove an unnecessary permission.
2. Build a minimal container twice, compare reproducibility, scan it, and promote one immutable digest.
3. Deploy to Container Instances or a local substitute and to OKE or local Kubernetes; compare control, scaling, and operational evidence.
4. Create an OCI DevOps or paper pipeline with build, tests, artifact delivery, approval, deployment, and post-deployment verification.
5. Simulate rolling, canary, and blue-green release decisions; test an unhealthy version and document rollback or forward-fix behavior.
6. Build a small Terraform/Resource Manager stack with protected state, a reviewed plan, scoped identity, drift classification, and cleanup.
7. Retrieve a secret through a workload identity or safe local substitute, rotate it, and prove the consumer no longer depends on the old value.
8. Correlate commit-to-request telemetry during an injected failure and design one safe event-driven response with loop protection.

## Original readiness checks

1. Container versus orchestrator? 2. Digest versus tag? 3. Container Instances versus OKE? 4. Request versus resource limit? 5. Readiness-probe role? 6. Release trace begins where? 7. Build secret versus runtime secret? 8. Artifact promotion benefit? 9. Canary decision signal? 10. Blue-green cost tradeoff? 11. Why can rollback fail? 12. Terraform plan purpose? 13. Why protect state? 14. Resource Manager stack identity? 15. Valid drift responses? 16. Separation-of-duties purpose? 17. Rotation completion evidence? 18. What does image scanning not prove? 19. Pipeline metric versus service metric? 20. Correlation dimensions? 21. Event-automation hazard? 22. Green-pipeline limitation? 23. Safe failure injection? 24. What remains unpublished? 25. What proves professional readiness?

### Answer guide

1. Packaged process versus scheduling and runtime control. 2. Exact immutable content versus movable label. 3. Direct container execution versus Kubernetes orchestration needs. 4. Scheduling guarantee versus consumption ceiling. 5. Decide when traffic is safe. 6. Exact source commit and reviewed inputs. 7. Build-only material versus values needed by the running service. 8. The tested bytes remain identical across environments. 9. Declared service indicators compared with a valid baseline. 10. Duplicate environment capacity for fast traffic switching. 11. Data or contract changes may be incompatible. 12. Review proposed infrastructure transition. 13. It governs resource identity and can expose values. 14. Dedicated principal with scoped permissions. 15. Codify/import, replace, or revert after classification. 16. Prevent one identity from silently authoring and approving production change. 17. Every consumer works after the old value is invalid. 18. Unknown flaws, business logic, runtime configuration, and future vulnerabilities. 19. Delivery-system performance versus user-visible behavior. 20. Commit, build, artifact, deployment, environment, resource, request. 21. Excess privilege, retries, or feedback loops. 22. Only encoded checks ran successfully. 23. Authorized, bounded, observable, reversible, and cleaned up. 24. Weights, question count, and passing score. 25. Traceable releases plus tested security, drift, degraded delivery, rollback, and diagnosis evidence.

## Readiness checklist

- I can trace a release from commit to immutable artifact to runtime request and recovery decision.
- I can select and operate Container Instances or OKE from workload constraints.
- I can implement least privilege, protected state and secrets, image policy, and production approval boundaries.
- I can diagnose delivery and runtime failure using correlated metrics, logs, and events.

## Places to learn

This is a selective learning path, not a complete list of OCI DevOps resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official OCI DevOps Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oci-devops-professional-2026/162852) | Oracle account/subscription may be required | **35+ hours** as published by Oracle University |
| [A DevOps Engineer's Guide to OCI](https://docs.oracle.com/en-us/iaas/Content/GSG/Reference/getting-started-as-devops.htm) | Public | **10–14 hours** targeted study |
| Eight labs in this guide | Authorized OCI tenancy or local substitutes | **28–40 hours** plus one timed release-and-recovery exercise |
