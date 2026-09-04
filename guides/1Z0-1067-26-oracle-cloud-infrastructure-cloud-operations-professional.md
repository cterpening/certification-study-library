---
exam_code: 1Z0-1067-26
vendor_id: oracle
official_blueprint: https://mylearn.oracle.com/ou/learning-path/become-an-oci-cloud-operations-professional-2026/163390
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-04
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-04
---

# 1Z0-1067-26 Oracle Cloud Infrastructure Cloud Operations Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide maps Oracle University's public 2026 learning-path scope checked September 4, 2026. It is unofficial and may contain errors. The [official OCI Cloud Operations Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oci-cloud-operations-professional-2026/163390) is authoritative.

**Assessment contract exposed by the current path:** Oracle Cloud Infrastructure Cloud Operations Professional, exam 1Z0-1067-26, 90 minutes.<br>
**Published scope:** security posture; billing and account management; OCI CLI and shell operations; Terraform, Resource Manager, and Ansible; resilient network and disaster-recovery design; observability and monitoring; custom images, scaling, DNS, load balancing, and troubleshooting.<br>
**Recommended experience on the path:** strong core IAM, networking, compute, and storage knowledge plus at least one year of hands-on OCI work.<br>
**Source boundary:** no public weights, question count, or passing score are inferred. **VERIFY CURRENT** in MyLearn before scheduling.

## How to use this guide

Practice every operation as declared state → authorized change → pre-check → execution → observable result → rollback or recovery. Prefer repeatable CLI/IaC over screenshots, but never run destructive commands against resources you do not own.

> **About related items:** A `Related item:` callout adds production-operations context. It is supporting knowledge, not a claim that its wording appears in Oracle's published scope.

## Objective map

| Oracle-published skill group | Operational proof |
|---|---|
| Enhance security posture | Findings become prioritized, least-privilege remediations with evidence |
| Billing and account management | Ownership, allocation, budgets, subscriptions, and support paths are clear |
| Command-line proficiency | Scripts are authenticated safely, idempotent where possible, and observable |
| Infrastructure as code | Terraform/Resource Manager/Ansible changes are reviewed, repeatable, and recoverable |
| Network design and disaster recovery | Paths survive selected failures and recovery meets declared objectives |
| Observability and monitoring | Signals detect user impact, localize causes, and trigger governed response |

## 1. Operational identity and account controls

Separate human, automation, and service identities. Use groups and federation for people; instance/resource principals or other workload identity for automation. Bound permissions by compartment, resource, verb, and condition. Protect break-glass access, API keys, tokens, and secrets with ownership, rotation, and audit evidence.

Track tenancy contacts, subscriptions, service limits, quotas, budgets, tagged owners, and support escalation. A cost anomaly needs workload context before action; an expired owner or missing tag is also an operational risk.

## 2. CLI and safe scripting

Know profile/config locations, regions, compartments, output formats, JMESPath-style query use, pagination, waiters, work requests, and exit/error handling. Avoid parsing human-formatted tables. Scripts should validate target tenancy/region/compartment, log request IDs, tolerate retryable errors, and stop safely on unexpected state.

Use shell strictness thoughtfully, quote identifiers, protect temporary credentials, and make deletion an explicit reviewed path. Dry runs, plans, tags, and allowlists reduce scope mistakes.

## 3. Terraform, Resource Manager, and Ansible

Terraform providers translate configuration into API operations; state binds configuration to remote objects. Protect state because it can contain sensitive values and governs future changes. Review plans, pin/validate dependencies, separate environments, constrain credentials, and detect drift.

Resource Manager runs Terraform with OCI-managed workflows such as stacks and jobs. Ansible configures systems and can orchestrate cloud modules. Choose the tool according to resource lifecycle versus in-guest configuration and keep overlapping ownership explicit.

## 4. Compute, images, and scaling

Use images, boot volumes, instance configurations, pools, placement, and autoscaling to make compute reproducible. Patch and replace rather than accumulating undocumented manual changes. Confirm shape capacity, quotas, initialization, health signals, and graceful termination.

Custom images capture a baseline but need versioning, vulnerability review, testing, deprecation, and rollback. Scaling policies require meaningful metrics, cooldowns, safe bounds, and downstream capacity awareness.

## 5. Network operations and recovery

Operate VCN routes, NSGs/security lists, gateways, DRGs, load balancers, DNS, and hybrid links as one bidirectional path. Use flow logs, route inspection, Network Path Analyzer where appropriate, health checks, and endpoint evidence. Preserve change windows and rollback for shared routes or DNS.

Define RPO/RTO, failure scope, backups/replication, traffic switch, dependency order, decision authority, and return-to-primary. Run recovery exercises and record actual results.

## 6. Observability and troubleshooting

Metrics summarize behavior; logs retain events; alarms evaluate signals; Events reacts to state changes; Notifications routes messages; tracing/request IDs correlate work. Build service-level indicators before alert thresholds and test that notifications reach an accountable responder.

Troubleshoot from symptom and timeline through recent changes, identity, quotas, DNS, route, security, capacity, health, dependency, and application evidence. Preserve evidence before remediation when incident handling may be required.

> **Related item:** An alarm that fires without an owned response path is telemetry, not an operational control.

## Integrated practice scenarios

1. **Failed deployment:** Correlate Resource Manager job output, work requests, IAM denial, and Terraform state; repair least privilege and rerun safely.
2. **Intermittent public service:** Trace DNS, load-balancer health, autoscaling, subnet capacity, flow logs, and backend metrics without widening all ingress.
3. **Regional recovery:** Declare an outage, restore data and dependencies in order, switch traffic, measure RPO/RTO, and document failback.

## Hands-on labs

1. Inventory an authorized tenancy by CLI with structured output, pagination, region, and compartment safeguards.
2. Write a read-only script that records request IDs and fails closed for an unexpected tenancy.
3. Create a Terraform stack, review its plan, introduce drift, reconcile it, and protect state.
4. Use Ansible or cloud-init to configure an instance reproducibly; prove rerun behavior.
5. Build and version a custom image; test replacement and rollback.
6. Diagnose three network failures using routes, security rules, DNS, health, and flow evidence.
7. Create one meaningful metric alarm and verify notification ownership and recovery closure.
8. Execute a tabletop or authorized recovery drill and compare measured versus required RPO/RTO.

## Original readiness checks

1. Human versus workload identity? 2. Why validate target scope? 3. Structured CLI output benefit? 4. Waiter versus blind sleep? 5. Work-request value? 6. What does Terraform state do? 7. Why protect it? 8. Plan review purpose? 9. Drift response choices? 10. Resource Manager role? 11. Terraform versus Ansible? 12. Custom-image lifecycle? 13. Autoscaling guardrails? 14. Quota versus capacity? 15. Route versus security failure? 16. DNS rollback concern? 17. RPO versus RTO? 18. Recovery dependency order? 19. Metric versus log? 20. Event versus alarm? 21. Request ID value? 22. What makes an alert actionable? 23. What remains unpublished? 24. What proves readiness?

### Answer guide

1. Interactive person versus service/resource principal. 2. Prevent cross-tenancy/region/compartment damage. 3. Stable machine parsing. 4. Observe asynchronous completion rather than guessing. 5. Track asynchronous API state and errors. 6. Maps desired configuration to managed objects. 7. It can expose secrets and controls change decisions. 8. Detect scope, replacement, and policy/cost effects. 9. Accept/import, change code, or restore resource under explicit ownership. 10. Managed Terraform stack/job workflow. 11. Infrastructure lifecycle versus system configuration/orchestration. 12. Build, scan, test, version, deprecate, rollback. 13. Signal, cooldown, safe bounds, dependency capacity. 14. Administrative allowance versus available service resources. 15. Next hop versus permission; inspect both directions. 16. Cached changes and shared blast radius. 17. Data-loss tolerance versus restoration time. 18. Recover prerequisites before dependents. 19. Aggregated measurement versus event records. 20. State-change routing versus threshold evaluation. 21. Correlate support and service-side operations. 22. Owned severity, context, runbook, and closure condition. 23. Weights, count, and score. 24. Safe repeatable changes plus evidence-led incident and recovery execution.

## Readiness checklist

- I can operate OCI with scoped identities, repeatable commands, and reversible IaC changes.
- I can diagnose identity, quota, network, compute, data, and dependency failures from evidence.
- I can define and test monitoring, escalation, backup, recovery, and failback.
- I can explain the security, availability, and cost consequence of an operational change.

## Places to learn

This is a selective learning path, not a complete list of OCI operations resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official OCI Cloud Operations Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oci-cloud-operations-professional-2026/163390) | Oracle account/subscription may be required | **22+ hours** as published by Oracle University |
| [OCI documentation](https://docs.oracle.com/en-us/iaas/Content/home.htm) | Public | **12–18 hours** targeted operational reading |
| Eight labs in this guide | Authorized OCI tenancy | **28–40 hours** plus two timed incidents |
