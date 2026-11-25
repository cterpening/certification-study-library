---
exam_code: 1Z0-1067-26
vendor_id: oracle
official_blueprint: https://mylearn.oracle.com/ou/learning-path/become-an-oci-cloud-operations-professional-2026/163390
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-10-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-10-28
---

# 1Z0-1067-26 Oracle Cloud Infrastructure Cloud Operations Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide maps Oracle University's public 2026 learning-path scope checked October 28, 2026. It is unofficial and may contain errors. The [official OCI Cloud Operations Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oci-cloud-operations-professional-2026/163390) is authoritative.

**Assessment contract exposed by the current path:** Oracle Cloud Infrastructure Cloud Operations Professional, exam 1Z0-1067-26, 90 minutes.<br>
**Published scope (high-level path topics):** security posture; billing and account management; OCI CLI and shell operations; Terraform, Resource Manager, and Ansible; resilient network and disaster-recovery design; observability and monitoring. The guide uses custom images, scaling, DNS, load balancing, and troubleshooting as derived examples/practice areas within those topics; Oracle’s path does not enumerate these as separate published objectives.<br>
**Recommended experience on the path:** strong core IAM, networking, compute, and storage knowledge plus at least one year of hands-on OCI work.<br>
**Source boundary:** no public weights, question count, or passing score are inferred. **VERIFY CURRENT** in MyLearn before scheduling.

**Japanese-language option (Japan only; checked October 28, 2026):** Oracle's September 4 launch notice added 1Z0-1067-26-JPN. The current Japanese exam list shows 90 minutes, 50 questions, and a 68% pass score for that distinct code. This route does not replace the English exam or its contract. [Japan launch notice](https://www.oracle.com/jp/education/news/) · [Japanese exam list](https://www.oracle.com/jp/education/certification/certification-exam-list/).
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

**Related item: current OKE version boundary (October 2026).** Oracle lists Kubernetes 1.36.4 as GA and 1.37.0 as preview for OC1 only; 1.37 is not recommended for production. The preview changes LoadBalancer defaults and requires a TLS Secret in the Service namespace. This version-sensitive example may help test the guide's OKE operations workflow, but it is not an exam baseline. Check the [supported-version calendar](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutk8sversions.htm) before a lab.

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

## Key terms and phrases

**Operational identity and account controls**

| Term or phrase | Meaning |
|---|---|
| [Compartment quota](#1-operational-identity-and-account-controls) | An administrator-defined limit on resource consumption within a compartment. |
| [Federation](#1-operational-identity-and-account-controls) | Trusting an external identity provider’s assertions so people can authenticate through their established organization identity. |
| [Audit log](#1-operational-identity-and-account-controls) | Records of administrative actions that help identify who performed an operation, on what resource and when. |
| [Secret rotation](#1-operational-identity-and-account-controls) | Replacing a secret under controlled conditions, confirming that its consumers use the replacement before retiring the old credential. |
| [Tenancy](#1-operational-identity-and-account-controls) | The organization’s root OCI account and administrative boundary in which compartments and resource policies are managed. |
| [Group](#1-operational-identity-and-account-controls) | A collection of identities to which access can be granted through a policy, reducing the need to manage permissions user by user. |
| [Resource principal](#1-operational-identity-and-account-controls) | An identity allowing a supported OCI resource to call other services under the permissions assigned to that resource. |
| [Break-glass access](#1-operational-identity-and-account-controls) | An exceptional, controlled access path for recovery when normal administrative access is unavailable, with auditing and review. |
| [Service limit](#1-operational-identity-and-account-controls) | A tenancy’s allowed service resource capacity under provider rules, distinct from a compartment quota an administrator sets. |
| [Cost allocation tag](#1-operational-identity-and-account-controls) | A metadata label used to attribute resources or consumption to an owner, environment or cost center. |
| [Budget](#1-operational-identity-and-account-controls) | A target for planned spending with alerts that support investigation when spending approaches an agreed threshold. |

**CLI and safe scripting**

| Term or phrase | Meaning |
|---|---|
| [Pagination](#2-cli-and-safe-scripting) | Reading a list result in successive pages until the service indicates that no more items remain. |
| [Work request](#2-cli-and-safe-scripting) | A record exposing progress and errors for an asynchronous operation after the initial API request returns. |
| [Compartment](#2-cli-and-safe-scripting) | A logical OCI grouping for resources, policy scope, ownership and cost reporting, which can span regions. |
| [Region](#2-cli-and-safe-scripting) | A geographic area containing OCI infrastructure. Region choice affects service locality, latency, residency and recovery options. |

**Terraform, Resource Manager, and Ansible**

| Term or phrase | Meaning |
|---|---|
| [Terraform state](#3-terraform-resource-manager-and-ansible) | The record connecting declared resource addresses to remote objects, used to decide what to change on the next run. |
| [Resource Manager stack](#3-terraform-resource-manager-and-ansible) | A managed Terraform configuration and associated state on which OCI can run planning or application jobs. |
| [Terraform provider](#3-terraform-resource-manager-and-ansible) | The component translating Terraform resource definitions into service API operations under its configuration and credentials. |
| [Plan job](#3-terraform-resource-manager-and-ansible) | An evaluation of proposed infrastructure changes for review before applying them. Its usefulness depends on the state and configuration remaining relevant. |

**Compute, images, and scaling**

| Term or phrase | Meaning |
|---|---|
| [Cooldown](#4-compute-images-and-scaling) | A waiting interval between scaling decisions that gives the previous change time to affect measured demand. |
| [Baseline](#4-compute-images-and-scaling) | An agreed reference configuration or historical measurement used to evaluate change in a comparable environment. |
| [Metric](#4-compute-images-and-scaling) | A numeric measurement recorded over time, such as failed requests or queue depth, with defined units and dimensions. |
| [Deployment rollback](#4-compute-images-and-scaling) | Restoring a previously working release or configuration after an unsuccessful change, with separate treatment for state already modified. |
| [IAM policy](#4-compute-images-and-scaling) | An authorization statement identifying who may perform which class of operations on which resources within a specified scope and conditions. |
| [Shape](#4-compute-images-and-scaling) | An OCI compute configuration defining available processing, memory and other hardware characteristics. |
| [Instance configuration](#4-compute-images-and-scaling) | A reusable specification of the settings needed to launch instances consistently, often used by an instance pool. |
| [Instance pool](#4-compute-images-and-scaling) | A group of instances managed together from a reusable configuration for scaling and availability. |
| [Autoscaling](#4-compute-images-and-scaling) | Adjusting capacity when a defined condition or schedule warrants it, subject to limits, capacity and application readiness. |
| [Boot volume](#4-compute-images-and-scaling) | Persistent block storage containing the operating system and startup files used to boot an instance. |

**Network operations and recovery**

| Term or phrase | Meaning |
|---|---|
| [Failback](#5-network-operations-and-recovery) | Returning service to its intended primary environment after recovery, while preserving the state accumulated during failover. |
| [Recovery point objective (RPO)](#5-network-operations-and-recovery) | The largest tolerable amount of lost recent data expressed as time. A 15-minute objective limits how far back recovery may fall. |
| [Recovery time objective (RTO)](#5-network-operations-and-recovery) | The longest acceptable interval to return the service to usable operation after a disruption, including validation. |
| [Backup](#5-network-operations-and-recovery) | A retained copy created to support recovery. Validate it by restoring the relevant data and exercising the service that depends on it. |
| [Health check](#5-network-operations-and-recovery) | A targeted test of a component’s ability to perform a particular task. Its scope determines what a successful result proves. |
| [DNS](#5-network-operations-and-recovery) | The naming system resolving service names to addresses or other records. Correct resolution alone does not establish reachability. |
| [Load balancer](#5-network-operations-and-recovery) | A component distributing incoming work among eligible backends under its routing and health policy. |
| [Virtual cloud network (VCN)](#5-network-operations-and-recovery) | A configurable regional network containing subnets, routes and security controls for OCI resources. |
| [Security list](#5-network-operations-and-recovery) | A set of traffic rules associated with a subnet and applied to its VNICs under OCI networking rules. |
| [Network security group (NSG)](#5-network-operations-and-recovery) | Traffic rules applied to chosen VNICs or other supported resource endpoints rather than every VNIC in a subnet. |
| [Dynamic routing gateway (DRG)](#5-network-operations-and-recovery) | A virtual router joining attached networks or connectivity resources, with route policies determining which paths are available. |

**Observability and troubleshooting**

| Term or phrase | Meaning |
|---|---|
| [Correlation identifier](#6-observability-and-troubleshooting) | A value carried across logs or requests so an operator can connect evidence from different components. |
| [Alert](#6-observability-and-troubleshooting) | A notification that a configured condition was met, requiring interpretation with its time window, source and affected scope. |
| [Encryption in transit](#6-observability-and-troubleshooting) | Protecting data while it travels between endpoints, commonly through authenticated TLS connections. |
| [Oracle Kubernetes Engine (OKE)](#6-observability-and-troubleshooting) | OCI’s managed Kubernetes service for running orchestrated container workloads on configured cluster capacity. |
| [Service-level indicator (SLI)](#6-observability-and-troubleshooting) | A measured aspect of service behavior, such as successful request latency or the percentage of requests returning a valid response. |
| [Event rule](#6-observability-and-troubleshooting) | A condition matching attributes of a resource event and routing matches to a permitted action. |
| [Monitoring alarm](#6-observability-and-troubleshooting) | A rule that evaluates a metric query over time and signals a state change when the configured condition is met. |
| [Distributed trace](#6-observability-and-troubleshooting) | A record linking the timed work of multiple instrumented components for a single request or transaction. |

**Original readiness checks**

| Term or phrase | Meaning |
|---|---|
| [Restore](#answer-guide) | Recreating data or a resource from a retained recovery copy, followed by checks that it meets the intended recovery point. |
| [Runbook](#answer-guide) | A documented response procedure identifying evidence to gather, safe actions, decision owners and verification steps. |

**Worked examples and practice**

| Term or phrase | Meaning |
|---|---|
| [Least privilege](#integrated-practice-scenarios) | Granting only the access a specific identity needs for its assigned work, then checking both allowed and denied actions. |
| [Subnet](#integrated-practice-scenarios) | An address range inside a VCN used to place network interfaces and associate applicable route and security settings. |

## Places to learn

This is a selective learning path, not a complete list of OCI operations resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official OCI Cloud Operations Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-an-oci-cloud-operations-professional-2026/163390) | Oracle account/subscription may be required | **22+ hours** as published by Oracle University |
| [OCI APM with OpenTelemetry tutorial](https://docs.oracle.com/en/learn/oci-apm-with-opentelemetry/index.html) | Public tutorial; OCI tenancy and Node.js sample app required; usage may incur charges | No publisher duration; 2–4 hours is a coordinator estimate for selected steps | Instrument an application, send traces/metrics to APM and logs to Logging Analytics; current commands and tenant costs must be verified |
| [OCI documentation](https://docs.oracle.com/en-us/iaas/Content/home.htm) | Public | **12–18 hours** targeted operational reading |
| Eight labs in this guide | Authorized OCI tenancy | **28–40 hours** plus two timed incidents |
