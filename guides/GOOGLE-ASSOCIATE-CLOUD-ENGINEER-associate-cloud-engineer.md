---
exam_code: GOOGLE-ASSOCIATE-CLOUD-ENGINEER
vendor_id: google-cloud
official_blueprint: https://cloud.google.com/learn/certification/cloud-engineer
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# Google Cloud Associate Cloud Engineer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 29, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#google-associate-cloud-engineer-coverage-record). The [official certification page](https://cloud.google.com/learn/certification/cloud-engineer) and its linked [exam guide](https://services.google.com/fh/files/misc/associate_cloud_engineer_exam_guide_english.pdf) are authoritative.

**Current baseline:** Four domains weighted approximately 20%, 30%, 30%, and 20%; all 94 considerations under 12 numbered objectives in the actual five-page PDF reviewed September 29, 2026<br>
**Published change notice:** Google says the exam was updated for recent branding changes and directs candidates to the exam guide for the product names used on the exam. No future effective date is announced.<br>
**Official source:** [Associate Cloud Engineer certification page](https://cloud.google.com/learn/certification/cloud-engineer) · [official detailed exam guide](https://services.google.com/fh/files/misc/associate_cloud_engineer_exam_guide_english.pdf)

## How to use this guide

ACE tests whether you can turn a requirement into a working, secured, observable Google Cloud solution and operate it safely. Learn each service through a repeated loop: choose it, configure it, verify it, observe it, diagnose it, change it, and recover it. Practice in the console and Cloud Shell, then repeat important tasks with `gcloud`, `kubectl`, and Terraform. Memorizing a service catalog is not enough.

The standard exam is two hours, USD 125 before applicable tax or regional differences, 50–60 multiple-choice and multiple-select questions, online- or onsite-proctored, available in English, Japanese, Spanish, and Portuguese, and valid for three years. There is no formal prerequisite; Google recommends at least six months of hands-on experience. Verify the [live page](https://cloud.google.com/learn/certification/cloud-engineer) before scheduling.

**VERIFY CURRENT — renewal:** The page lists a one-hour, USD 75 before tax renewal exam with 20 questions in English/Japanese and three-year validity for eligible active holders. A separate designated Google Skills course/badge route grants one-year validity and requires completion within the final year of the active certification, plus linked accounts. Completing an arbitrary preparation course is not that renewal route; check your eligibility dashboard.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central operational question |
|---|---:|---|
| Setting up a cloud solution environment | ~20% | Is the hierarchy, identity, policy, API, quota, network, location, observability, and billing foundation ready? |
| Planning and implementing a cloud solution | ~30% | Which compute, data, storage, network, and provisioning choices satisfy the workload? |
| Ensuring the successful operation of a cloud solution | ~30% | Can you inspect, change, scale, monitor, troubleshoot, back up, and restore it safely? |
| Configuring access and security | ~20% | Does each human and workload get the minimum usable access without durable credentials? |

This four-domain blueprint supersedes older five-domain outlines that separated planning from deployment. The current PDF also uses 2026 names such as **Gemini Enterprise Agent Platform**, **Agent Runtime**, **Gemini Enterprise Agent Platform Workbench**, **Cloud Run functions**, and **Cloud NGFW**. Older courses may say Vertex AI Agent Engine, Vertex AI Workbench, Cloud Functions, or VPC firewall rules. Learn the conceptual continuity, but use the current PDF as the naming baseline.

---

## 1. Setting up a cloud solution environment — about 20%

### Resource hierarchy and guardrails

The resource hierarchy is organization → folders → projects → resources. A project is a billing, quota, API, IAM, and lifecycle boundary, not merely a visual grouping. Folders model administration or policy boundaries. Policies and IAM bindings inherit downward; a child can add access but an inherited binding is not removed by omitting it locally. Design the hierarchy around ownership, environment separation, regulatory boundary, and delegated administration rather than copying an org chart blindly.

Create projects with a naming and labeling convention, link the correct billing account, enable only required APIs, and verify quotas and regional product availability before deployment. Service activation and quota are separate checks: enabling an API does not guarantee sufficient quota, and a quota increase does not prove the product is available in the chosen region.

Organization policies constrain what configurations are permitted, while IAM decides who can perform allowed actions. Examples include permitted regions, external IP restrictions, domain-restricted sharing, and service-account key controls. Test policies in a lower-risk scope and know the inheritance path before broad enforcement.

Cloud Identity manages users and groups; groups simplify role assignment and lifecycle. Workforce Identity Federation lets external workforces use an external identity provider without creating long-lived Google identities for every user. Keep break-glass access narrow, monitored, tested, and outside routine workflows.

The blueprint also names **standalone organizations**. Current [setup documentation](https://docs.cloud.google.com/resource-manager/docs/standalone-organization-overview) describes automatic creation for new Free Trial customers without Cloud Identity, and excludes existing accounts from that creation route. Organization Owner is managed outside IAM and differs from Organization Administrator; at least one active Google Account must remain an owner, and a service account cannot be an owner. Organization Administrator does not by itself confer every project/folder creation permission. Verify eligibility and ownership recovery before designing a lab around this route.

### Networking and location foundation

A VPC is global; its subnets are regional. Custom mode gives explicit address control. Shared VPC centralizes a host project’s network while service projects own workload resources. VPC Network Peering connects networks without transitive routing and does not merge IAM or administration. Plan non-overlapping address space, DNS, routing, hybrid connectivity, egress, private access, firewall policy, and IP capacity before deployment.

Regions contain zones. Zonal placement is a single failure-domain choice; regional or multi-regional design trades cost and complexity for resilience. Check latency, residency, availability, service features, and recovery requirements rather than choosing the nearest region automatically.

### Observability, assets, quotas, and AI assistance

Provision Cloud Logging and Cloud Monitoring deliberately: retention, log buckets, sinks, metrics, dashboards, alerts, notification channels, and operational ownership. Audit logs answer control-plane and data-access questions only when the required log types are enabled and retained. Cloud Asset Inventory provides searchable inventory, history, feeds, and policy-analysis inputs. Gemini Cloud Assist can help analyze resources and operations, but validate suggestions against actual state, permissions, policy, cost, and change controls.

Quotas protect platform and tenant capacity. Distinguish allocation quota from rate quota, regional from global limits, and project from account scope. A production readiness check includes current use, expected peak, lead time for increases, fallback capacity, and alerts.

### Billing configuration

Billing accounts fund projects. Use alerts-only budgets for visibility; those budgets do not stop spend. **VERIFY CURRENT:** [spend cap budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps) are a separate preview for one project, one eligible service and a monthly period. Enforcement uses gross estimated costs, can lag, and lets in-flight and ongoing fixed-resource charges continue; manual lifting restores usage. Treat both approaches as configured controls with different boundaries, not a universal zero-overrun guarantee. Export detailed billing data to BigQuery for allocation, anomaly analysis, forecasting, and FinOps reporting. Labels, tags, project boundaries, committed-use planning, and accountable owners make costs actionable.

> **Related item:** Resource Manager tags can be used by policy-aware services; labels are key/value metadata often used for organization and cost reporting. Do not assume they have identical inheritance, authorization, or enforcement behavior.

---

## 2. Planning and implementing a cloud solution — about 30%

### Choose compute by operating responsibility

| Need | Likely starting point | Key boundary |
|---|---|---|
| OS control, legacy software, special networking | Compute Engine | You manage guest OS, patching, sizing, and instance lifecycle |
| Stateless containers with request/event-driven scaling | Cloud Run | Container contract, statelessness, concurrency, timeout, min/max instances |
| Managed Kubernetes APIs and ecosystem | GKE | Cluster/workload operations remain; Autopilot shifts more node management to Google |
| Event or HTTP function | Cloud Run functions | Current function surface; understand trigger, identity, retries, idempotency |
| Managed agent execution | Agent Runtime on Gemini Enterprise Agent Platform | Current name; verify release stage, region, identity, data, tools, quotas, and observability |
| Specialized accelerators | GPU or TPU-backed compute | Framework fit, capacity, topology, cost, utilization, quota, and fallback |

For Compute Engine, choose zone/region, machine family/type, boot image, disk, network, service account, shielded/security settings, availability policy, and metadata. Instance templates produce managed instance groups; autoscaling reacts to signals, while autohealing recreates unhealthy instances. Keep load-balancer health checks and MIG autohealing checks separate: one removes a backend from traffic while the other can recreate a VM. Use a more conservative autohealing check, allow its probes through the firewall, and configure startup delay from evidence; a blocked probe can cause unnecessary replacements. [MIG repair documentation](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs).

Spot VMs reduce cost but may be preempted, so workloads need checkpointing or retry tolerance. OS Login centralizes SSH authorization in IAM. VM Manager supports inventory, patch, configuration, and OS-policy operations.

Persistent Disk and Hyperdisk are block storage choices with different performance and availability profiles. Regional Persistent Disk replicates across zones; it does not replace application-aware backup, recovery testing, or a database-native HA design.

GKE mode is an operating-model choice. Autopilot manages more infrastructure and enforces workload-oriented resource behavior; Standard exposes node pools and more configuration. Regional clusters improve control-plane availability; private clusters reduce public exposure. Deploy containers from Artifact Registry, set resource requests/limits, choose Services/Ingress or Gateway exposure, and understand Pods, Deployments, StatefulSets, ConfigMaps, Secrets, volumes, and disruption behavior.

Cloud Run revisions support gradual rollout and traffic splitting. Events commonly reach services/functions through Eventarc or Pub/Sub. Design for duplicate delivery, retries, ordering limits, dead-letter handling, and idempotency. [Pub/Sub exactly-once delivery](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery) is scoped to supported pull/StreamingPull subscriptions within a region, not push/Eventarc HTTP processing. Acknowledgment expiry permits valid redelivery; repeated publishing can still produce duplicates. Commit the business effect and deduplication record atomically using a stable business-operation key, then acknowledge. If an external effect cannot join the transaction, consider an outbox and an idempotent receiver; neither message delivery nor the outbox alone proves a payment or email happens once.

### Data and storage selection

Choose by access pattern and operational contract:

| Requirement | Candidate | Watch for |
|---|---|---|
| Object/blob storage and lifecycle tiers | Cloud Storage | Location, class, lifecycle, retention, versioning, access, egress |
| Managed relational MySQL/PostgreSQL/SQL Server | Cloud SQL | HA, backups/PITR, connection limits, maintenance, read scaling |
| PostgreSQL compatibility with higher scale/performance | AlloyDB | Workload fit, region/HA, migration, connection and cost model |
| Horizontally scalable relational/global consistency | Spanner | Schema/key design, instance capacity, cost, locality |
| Document database for application data | Firestore | Mode, query/index model, consistency and cost behavior |
| Wide-column, high-throughput low-latency data | Bigtable | Row-key design, hotspots, cluster capacity, replication |
| Analytics warehouse | BigQuery | Partitioning, clustering, slots/on-demand cost, data governance |
| Cache | Memorystore | Engine, persistence/HA, eviction, private connectivity |
| Event messaging | Pub/Sub | delivery semantics, ordering, retention, retry/dead letter |
| Managed streaming platform compatibility | Managed Service for Apache Kafka | Kafka requirement, capacity, networking, ecosystem fit |
| Batch/stream data processing | Dataflow | Beam pipeline behavior, workers, autoscaling, job monitoring |
| Managed shared files | Filestore / NetApp Volumes | protocol, performance tier, capacity, availability |
| HPC file system | Managed Lustre | workload/client fit, throughput, lifecycle and availability |

Cloud Storage classes—Standard, Nearline, Coldline, Archive—trade storage price against retrieval and minimum-duration behavior. Autoclass and lifecycle rules can automate transitions, but retention and deletion requirements need separate controls. Use Storage Transfer Service for managed bulk or recurring transfers; plan validation, cutover, bandwidth, permissions, and rollback.

### Network implementation

Firewall evaluation is direction-aware and stateful. Specify ingress/egress, action, source/destination, protocol/port, priority, and target. Cloud NGFW policies can centralize hierarchical/global/regional control and use secure Tags or service accounts as workload-aware targets. Evaluate policy layers before comparing priorities: hierarchical and regional system policies precede the remaining layers, while the network's `BEFORE_CLASSIC_FIREWALL` or default `AFTER_CLASSIC_FIREWALL` setting changes the relative position of network policies and classic VPC rules. An earlier terminating allow/deny can decide the result; `goto_next` delegates to the next evaluation step. A low numeric priority in a later layer cannot override an earlier decision. For matching classic VPC rules at equal priority, deny wins. [Evaluation order](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order).

Cloud VPN supplies encrypted IP connectivity; Cloud Interconnect supplies dedicated or provider-based connectivity and normally still needs an encryption decision. Peering provides private network-to-network reachability without transitivity. Cloud NAT supplies outbound translation for resources without external IPv4 addresses; it is not an inbound proxy or firewall. Choose the load balancer by internal/external reachability, global/regional scope, L4/L7 protocol, backends, TLS, and resilience requirement. Premium and Standard Network Service Tiers differ in routing scope and supported features.

### Provision consistently

Terraform declares infrastructure through providers, resources, modules, state, plan, and apply. Protect state, review plans, pin/upgrade providers deliberately, detect drift, and separate reusable modules from environment inputs. Config Connector represents Google Cloud resources through Kubernetes objects; Helm packages Kubernetes applications. Fabric FAST supplies opinionated Terraform foundations. AI-assisted tools such as Gemini CLI, Google Antigravity, Gemini Cloud Assist, and Application Design Center can accelerate design or code, but their output remains proposed change: review identity, policy, region, dependency, cost, security, and destroy/rollback impact.

> **Related item:** Infrastructure as code makes a configuration reproducible; it does not make the design correct. Policy checks, peer review, tests, state protection, controlled credentials, and post-deployment verification remain necessary.

---

## 3. Ensuring successful operation — about 30%

### Operate compute safely

Inventory first: confirm project, region/zone, resource name, labels/tags, desired state, dependency, and recent changes. For a VM, inspect status, serial output, logs, service health, network path, disk/CPU/memory, and guest state before restarting it. Use IAP or OS Login patterns where appropriate rather than distributing SSH keys. Images are reusable boot-disk templates; snapshots are incremental point-in-time disk protection. Schedule them, monitor success, define retention, and prove restore. A snapshot of a running disk can be crash consistent while omitting pending application writes. Application consistency needs application/OS coordination: current documentation distinguishes Persistent Disk guest-flush/VSS support from Hyperdisk, which requires manual application coordination. An operation marked DONE is not alone proof of a usable snapshot; inspect its resource status and restore the workload. [Snapshot guidance](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices).

For GKE, inspect clusters, nodes/node pools, Pods, Services, Deployments/StatefulSets, events, logs, resource requests, health probes, autoscalers, disruption budgets, and rollout status. Horizontal Pod Autoscaling changes replica count; Vertical Pod Autoscaling recommends or changes resource requests; cluster/node autoscaling changes capacity. Autopilot scheduling depends strongly on valid Pod requests. Diagnose image access separately from in-container API access. Normal kubelet image pulls use the node's IAM service account, or configured image-pull credentials, rather than the Pod's Workload Identity Federation identity. Check the actual identity, repository role, account status, node access scopes and network path. Adding a storage role to the Pod will not repair every `ImagePullBackOff`. [Image-pull troubleshooting](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/image-pulls).

Use Artifact Registry for current exercises. Container Registry writes stopped in March 2025; a `gcr.io` URL can now be backed by Artifact Registry and is not alone evidence of obsolete storage. A public course outcome that still says Container Registry needs a migration check. [Registry transition](https://docs.cloud.google.com/artifact-registry/docs/transition/transition-from-gcr).

For Cloud Run, deploy immutable revisions, direct a small traffic percentage, observe errors/latency, and promote or roll back. Minimum instances reduce cold-start exposure at a cost; concurrency changes per-instance pressure. Configure the [service-level maximum](https://docs.cloud.google.com/run/docs/configuring/max-instances) deliberately and distinguish it from older revision-level limits, traffic splits and tagged revision behavior. Maximum instances is a scaling control, not a strict database-connection or spending boundary: [temporary excess instances and deployment overlap](https://docs.cloud.google.com/run/docs/about-instance-autoscaling) are documented. Bound each application's connection pool, reserve headroom for other clients and transient overlap, observe connections, and use backpressure. Twenty instances with eight pooled connections each plus twenty other connections implies 180 connections; an invented 26-instance overlap gives 228, exceeding a fictional 200-connection budget. Neither count forecasts Google's actual autoscaler. Attach accelerators only after verifying quota, region, runtime support, utilization, and fallback.

Agent and notebook operations require the same discipline as other workloads: named owner, identity, authorized data and tools, versioned artifact, evaluation, quotas/cost, logs/traces, stop/rollback, and incident response. The current blueprint calls these Agent Runtime and Gemini Enterprise Agent Platform Workbench (formerly Vertex AI Agent Engine and Vertex AI Workbench).

**Cloud Workstations is a separate developer-environment service.** Its cluster defines region/network, configuration defines the VM/image/storage template, and workstation is the user's running environment. A workstation cluster is not a GKE cluster. Configuration updates take effect on restart; stopping deletes the ephemeral VM/runtime data, while an explicitly configured persistent home directory survives. Verify where work is saved and test restart/update behavior. [Workstations overview](https://docs.cloud.google.com/workstations/docs/overview).

### Operate data and storage

With fine-grained access, bucket/object ACLs and IAM can independently grant access. Enabling [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) disables ACL authorization and ACL operations; migrate necessary object-level access without granting the whole bucket too broadly. It becomes irreversible after 90 consecutive days, and earlier reversal has additional conditions. This feature is required for federated workforce/workload identities to access Cloud Storage. It governs authorization, not retention or backups. Lifecycle rules manage transitions/deletion; retention policies and holds prevent deletion. Versioning aids recovery but can increase cost and does not replace independent backup. CMEK changes key ownership and failure modes: rotation, permission, availability, disablement, destruction, and recovery must be managed.

For managed databases, monitor availability, connections, CPU/storage, replication, query latency, backup status, recovery point, and maintenance. Backups are valuable only if restorations are tested. Use native query and diagnostic tools within least privilege. Database Center provides fleet visibility; it is not a substitute for engine-specific remediation. For BigQuery and Dataflow, inspect job status, errors, bytes/slots/workers, skew, retries, output correctness, and downstream effects. For BigQuery on-demand queries, estimate processed bytes with validation/dry run and use maximum bytes billed as a per-query control. `LIMIT` on a non-clustered table does not reduce scanned bytes; project needed columns and use appropriate partition filters. Clustered-table estimates can be conservative, and a dry run against row-level-security-protected data can return zero rather than a trustworthy free-query estimate. [Cost-control documentation](https://docs.cloud.google.com/bigquery/docs/best-practices-costs).

### Operate the network

Reserve static IPs when endpoints must remain stable. A primary IPv4 range can expand but cannot be replaced or shrunk. The expanded CIDR must contain the existing block and avoid conflicting primary, secondary and connected ranges; inventory those ranges before changing it. Ordinary primary IPv4 ranges reserve the first two and last two addresses, unlike secondary ranges. Google's virtual gateway does not respond to ping, so a failed gateway ping alone does not establish a network fault. [Subnet constraints](https://docs.cloud.google.com/vpc/docs/subnets). Custom routes need destination, next hop, scope, priority, and reachability validation. Cloud DNS controls name resolution; Cloud NAT controls outbound translation. Diagnose in layers: DNS → route → firewall/policy → load balancer/health check → service/listener → application → dependency. VPC Flow Logs and firewall logs provide evidence but must be enabled and sampled appropriately.

### Monitoring, logging, and diagnosis

Start from a service-level symptom and a time window. Metrics quantify behavior; logs record events; traces follow requests; profiles show runtime resource use. Create alerts on actionable conditions tied to an owner and runbook. Avoid alerting only on raw utilization when user impact is what matters. Custom metrics and log-based metrics can expose application signals but add cardinality, cost, and lifecycle concerns.

Cloud Logging uses log buckets for storage/retention, Log Router sinks for routing, and Log Analytics for analytical queries. Exports to BigQuery or external systems need destination permissions, capacity, retention, and sensitive-data handling. Audit, VPC Flow, and firewall logs answer different questions. Each sink normally evaluates matching entries independently, so a second destination does not automatically remove storage in the first. Intercepting aggregated sinks can change child routing, with the originating `_Required` sink exception. New or repaired sinks do not backfill entries already received; historical copying is a separate operation. Router buffering is not protection from an incorrect filter or destination permission. [Log routing](https://docs.cloud.google.com/logging/docs/routing/overview).

Cloud Trace, Cloud Profiler, Query Insights, and index advisor target different bottlenecks. Personalized Service Health identifies relevant Google incidents. Ops Agent collects guest telemetry. Managed Service for Prometheus supports Prometheus-compatible metrics. Active Assist recommends optimization; review risk and evidence before applying. Cloud Hub aggregates active events and application-health information. Gemini Cloud Assist can accelerate investigation, but confirm every proposed cause or command.

An incident loop is detect → scope impact → stabilize → preserve evidence → diagnose → repair → verify user outcome → monitor → document learning. Rollback can be safer than debugging in production, but only when data and dependency compatibility permit it.

> **Related item:** An SLI is a measured indicator, an SLO is its target, and an error budget is the tolerated unreliability. Alerts work best when they connect to user impact and an action, not merely the existence of a resource metric.

---

## 4. Configuring access and security — about 20%

### IAM policies and roles

An IAM policy binds principals to roles at a resource. A role is a permission bundle. Basic roles are broad; predefined roles are service-specific; custom roles support narrower organizational needs but require maintenance. Grant at the lowest practical scope, prefer groups for humans, separate administration from use, time-bound elevation where available, and review effective/inherited access.

Policy inheritance means access granted at organization or folder applies below. Deny and organization-policy behavior must be evaluated alongside allow bindings. Use Policy Analyzer, IAM recommender, audit logs, and asset inventory as evidence, but do not apply recommendations blindly when a rare operational path is not visible in recent usage.

### Service accounts and federation

A service account is a workload identity, not a generic shared user. Give each workload a purpose-specific identity and minimum role, attach it to the resource, and control who can impersonate or act as it. Distinguish permissions **on the service account** (for example, impersonation) from permissions **granted to the service account** on other resources.

Separate the caller, credential mechanism, resource authorization and deployment permissions:

| Question | Required distinction |
|---|---|
| Can I attach a service account to a workload? | Resource-creation permissions plus `iam.serviceAccounts.actAs`, often through Service Account User |
| Can I mint short-lived credentials as it? | Token-creation permission, commonly Service Account Token Creator; Service Account User alone is insufficient |
| Can its token read a bucket? | Permissions granted to that service account on the target resource, plus applicable restrictions |
| Does successful `gcloud` access prove my application uses that identity? | No; CLI credentials and Application Default Credentials are distinct |

[Service-account authentication roles](https://docs.cloud.google.com/iam/docs/service-account-permissions) explain the first two permissions. [ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials) looks for an environment-selected credential configuration, then local ADC credentials, then an attached identity through metadata. A credential configuration can represent federation; it is not always a downloaded private key. Inspect provenance without printing tokens or private files, and do not broaden IAM to conceal use of the wrong identity.

Prefer attached identities, service-account impersonation, short-lived tokens, Workload Identity Federation for external workloads, and Workload Identity Federation for GKE over downloadable keys. If a key is unavoidable, inventory, restrict, rotate, monitor, and retire it. Federation exchanges a trusted external assertion for short-lived Google credentials; trust configuration, attribute mapping/conditions, audience, and principal binding are core controls.

Google-managed service accounts and service agents perform platform functions. Removing their permissions can break services. Identify the agent and required role from first-party documentation before modifying it.

For GKE, [Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) can grant IAM access directly to the Kubernetes workload principal; impersonating an IAM service account is an alternative when needed for product compatibility. It does not always require one Google service account for every Kubernetes service account. Identical namespace/service-account identities in clusters sharing the same project pool can receive the same permissions; choose trust boundaries, distinct names or supported conditions deliberately. Also apply Kubernetes RBAC, namespace, network, image, secret, and admission controls; Google IAM alone does not govern every in-cluster action.

> **Related item:** Authentication establishes identity; authorization determines permitted action. A valid token does not prove that the request should be allowed, and encryption does not repair excessive authorization.

---

## Integrated scenarios

### Scenario 1 — Public API with unpredictable traffic

A stateless container receives HTTPS traffic, writes relational orders, publishes fulfillment events, and must deploy without downtime. Start with Cloud Run behind the appropriate managed endpoint/load-balancing design, Cloud SQL or AlloyDB based on scale/compatibility evidence, Pub/Sub for decoupling, Secret Manager for secrets, a dedicated service account, private connectivity where required, and Logging/Monitoring. Set min/max instances and concurrency based on latency and database connection capacity. Deploy a revision to a small traffic share, observe application and dependency SLIs, then promote or roll back. Make event consumers idempotent and configure retry/dead-letter behavior. Test commit-before-ack failure, changed payload under the same operation key and a duplicate publish with a new message ID. Verify service-level scaling settings and pooled database connections under rollout overlap; the instance setting alone cannot prove the database stays inside its budget.

### Scenario 2 — Governed multi-team platform

Several teams need isolated projects but shared private networking and central security policy. Use organization/folder policy boundaries, service projects attached to a Shared VPC host project, group-based roles, workload federation, Cloud NGFW policy, centralized DNS/connectivity, billing export, budgets, asset inventory, and log routing. Delegate only the roles teams need. Trace firewall policy layers and actual credential identities before granting more access. Test inherited policy, quotas, regional availability, and incident ownership before onboarding workloads; record whether centralized sinks intercept child routing and where historical logs already reside.

### Scenario 3 — GKE service is slow after release

Confirm user impact and recent rollout. Inspect Cloud Monitoring metrics, GKE events, Pod status/probes, requests/limits, HPA/VPA, node capacity, logs, traces, dependency/query latency, load-balancer health, and service health. Stabilize by traffic rollback or scaling only when safe. If Pods are pending, distinguish quota/node capacity, affinity/taints, resource request, volume, and policy causes. Distinguish an image-pull failure under the node identity from an API denial under the running Pod identity; also compare cluster identity-pool boundaries. Verify the user SLI, then record the detection and deployment-control improvements.

---

## Hands-on lab path

These eight Google Cloud labs are **proposed, not executed in this review**. Use a disposable authorized project, recorded identities and locations, cost controls, and explicit cleanup. Save expected/observed results and recovery evidence; do not enable irreversible retention locks as a casual exercise.

| Lab | Exercise and acceptance evidence | Negative/recovery case |
|---|---|---|
| 1. Foundation | Inspect hierarchy, project/billing/API/quota and budget type; query inventory; document standalone-organization eligibility separately | Demonstrate that API enablement and sufficient quota are separate checks; verify only the intended disposable scope is removed |
| 2. IAM | Compare CLI/ADC identity, attachment versus token creation, and target-resource access with narrow roles | Wrong credential source and missing target permission must be diagnosed separately; remove temporary bindings and verify denial |
| 3. Network | Plan non-overlapping primary/secondary ranges; configure VPC, DNS, NAT and effective firewall policy; prove allowed/denied paths | Reject an overlapping expansion; trace an earlier terminating firewall rule and avoid treating gateway ping as decisive evidence |
| 4. Compute Engine | Deploy a MIG, separate load-balancing/autohealing checks, measure startup, snapshot and restore application data | Block a test probe in a disposable scope, observe diagnosis, restore it; verify restored application consistency rather than only operation completion |
| 5. Cloud Run/events | Deploy two revisions, measure traffic/latency/connections, inspect service/revision limits and process events with a business key | Retry after commit but before acknowledgment; reject changed payload under the same key; prove rollback and connection backpressure |
| 6. GKE | Deploy app/probes/resources/HPA; configure workload IAM and repository access; record node and Pod identities | Contrast image-pull denial with in-container API denial, then restore each narrow permission; delete test workload/cluster resources |
| 7. Data | Migrate test ACLs to IAM, compare retention/lifecycle, restore database data, estimate a BigQuery query and inspect a Dataflow/Pub/Sub job | Verify access formerly supplied only by ACLs; reject query over the chosen bytes budget; do not mistake backup success for tested recovery |
| 8. Operations/IaC | Review Terraform plan/state; route a unique new test log to its destination; inspect Workstations configuration, storage and restart behavior | Check sink filters/permissions and existing-log boundary; inject and recover a small failure, then remove temporary infrastructure and retained chargeable resources |

### Offline operations worksheet — executed

Save the following as `ace_operations_workbook.py` and run `python ace_operations_workbook.py`. It uses only Python's standard library and an in-memory SQLite database. The exact code below passed **32 checks** on September 29, 2026, including expected failures.

CIDR checks validate only containment, prefix size and supplied overlap inventory; they do not validate Google's complete range restrictions, routing, IAM or quotas. Capacity arithmetic uses invented counts, not a service simulator. SQLite executes a real local transaction linking a business reservation, deduplication record and outbox row; no message, cloud database, payment or email is sent. The injected exception proves transaction rollback in this process, not machine-crash durability or concurrent distributed processing. An outbox dispatcher and idempotent destination would still need implementation and testing.

```python
"""Offline ACE exercises: CIDR arithmetic and atomic business deduplication."""
from ipaddress import IPv4Network
import sqlite3


def expansion_ok(old, proposed, occupied):
    # Arithmetic only: occupied must include relevant primary/secondary/peer ranges.
    before, after = IPv4Network(old), IPv4Network(proposed)
    return (4 <= after.prefixlen <= 29 and before.subnet_of(after)
            and not any(after.overlaps(IPv4Network(x)) for x in occupied))


def primary_capacity(cidr):
    network = IPv4Network(cidr)
    if not 4 <= network.prefixlen <= 29:
        raise ValueError("Outside the primary IPv4 prefix-size envelope")
    return network.num_addresses - 4


def connection_estimate(instances, pool_per_instance, other_clients):
    values = (instances, pool_per_instance, other_clients)
    if any(type(x) is not int or x < 0 for x in values):
        raise ValueError("Use nonnegative integer scenario counts")
    return instances * pool_per_instance + other_clients


def open_store():
    db = sqlite3.connect(":memory:")
    db.executescript("""
      CREATE TABLE stock(sku TEXT PRIMARY KEY, available INTEGER NOT NULL);
      INSERT INTO stock VALUES ('book', 10);
      CREATE TABLE applied(operation_id TEXT PRIMARY KEY, sku TEXT, units INTEGER);
      CREATE TABLE outbox(operation_id TEXT PRIMARY KEY, payload TEXT NOT NULL);
    """)
    return db


def reserve(db, operation_id, sku, units, fail_after_update=False):
    # The operation key belongs to the business operation, not its delivery attempt.
    if not isinstance(operation_id, str) or not operation_id.strip():
        raise ValueError("Missing business operation ID")
    if not isinstance(sku, str) or not sku.strip():
        raise ValueError("Missing SKU")
    if type(units) is not int or units <= 0:
        raise ValueError("Units must be a positive integer")
    db.execute("BEGIN IMMEDIATE")
    try:
        prior = db.execute("SELECT sku, units FROM applied WHERE operation_id=?",
                           (operation_id,)).fetchone()
        if prior is not None:
            if prior != (sku, units):
                raise ValueError("Operation ID reused with different payload")
            db.commit()
            return "duplicate"
        changed = db.execute(
            "UPDATE stock SET available=available-? WHERE sku=? AND available>=?",
            (units, sku, units)).rowcount
        if changed != 1:
            raise ValueError("Unknown SKU or insufficient stock")
        if fail_after_update:
            raise RuntimeError("Injected failure before ledger/outbox write")
        db.execute("INSERT INTO applied VALUES (?,?,?)", (operation_id, sku, units))
        db.execute("INSERT INTO outbox VALUES (?,?)", (operation_id, "reserved"))
        db.commit()
        return "applied"
    except Exception:
        db.rollback()
        raise


def state(db):
    return (db.execute("SELECT available FROM stock WHERE sku='book'").fetchone()[0],
            db.execute("SELECT COUNT(*) FROM applied").fetchone()[0],
            db.execute("SELECT COUNT(*) FROM outbox").fetchone()[0])


def run():
    passed = 0

    def check(condition):
        nonlocal passed
        if not condition:
            raise AssertionError("Exercise check failed")
        passed += 1

    def rejects(error, function, *args, **kwargs):
        try:
            function(*args, **kwargs)
        except error:
            check(True)
        else:
            raise AssertionError("Expected failure was not observed")

    check(primary_capacity("10.0.0.0/24") == 252)
    check(primary_capacity("10.0.0.0/29") == 4)
    rejects(ValueError, primary_capacity, "10.0.0.0/30")
    rejects(ValueError, primary_capacity, "10.0.0.5/24")
    check(expansion_ok("10.0.0.0/24", "10.0.0.0/23", ["10.0.2.0/24"]))
    check(not expansion_ok("10.0.0.0/24", "10.0.0.0/23", ["10.0.1.0/24"]))
    check(not expansion_ok("10.0.0.0/24", "10.0.0.0/25", []))
    check(not expansion_ok("10.0.0.0/24", "10.0.2.0/23", []))
    check(connection_estimate(20, 8, 20) == 180)
    check(connection_estimate(26, 8, 20) == 228)  # invented overlap scenario
    check(connection_estimate(26, 8, 20) > 200)  # fictitious database budget
    rejects(ValueError, connection_estimate, -1, 8, 20)
    rejects(ValueError, connection_estimate, True, 8, 20)

    db = open_store()
    try:
        check(state(db) == (10, 0, 0))
        check(reserve(db, "order-1", "book", 3) == "applied")
        check(state(db) == (7, 1, 1))
        check(reserve(db, "order-1", "book", 3) == "duplicate")
        check(state(db) == (7, 1, 1))
        rejects(ValueError, reserve, db, "order-1", "book", 4)
        check(state(db) == (7, 1, 1))
        rejects(RuntimeError, reserve, db, "order-2", "book", 2,
                fail_after_update=True)
        check(state(db) == (7, 1, 1))  # stock and deduplication both rolled back
        check(reserve(db, "order-2", "book", 2) == "applied")
        check(state(db) == (5, 2, 2))
        rejects(ValueError, reserve, db, "order-3", "book", 6)
        rejects(ValueError, reserve, db, "order-4", "unknown", 1)
        rejects(ValueError, reserve, db, "", "book", 1)
        rejects(ValueError, reserve, db, "order-5", "book", 0)
        rejects(ValueError, reserve, db, "order-5", "book", True)
        check(state(db) == (5, 2, 2))
        check(reserve(db, "order-6", "book", 3) == "applied")
        check(state(db) == (2, 3, 3))  # new key legitimately creates new work
    finally:
        db.close()
    print(f"{passed} offline checks passed; no Google Cloud API or message delivered")
    return passed


if __name__ == "__main__":
    run()
```

Discuss the last two checks: a new business key legitimately creates new work even with the same SKU/quantity. If a producer invents a new operation key on every retry, database deduplication cannot recognize the retry as the same operation. Define that identity before choosing messaging options.

## Original readiness checks

These are original concept checks, not recalled exam items. Answer before opening the key.

1. Why is a project more than a folder for resources?
2. A budget reaches 100%. Does Google Cloud necessarily stop resources?
3. An API is enabled but deployment reports capacity/quota failure. What should you inspect?
4. What is the important scope difference between a VPC and a subnet?
5. When is Shared VPC preferable to ordinary peering?
6. Why might a regional disk still need backup?
7. A stateless HTTP container has bursty demand. Which compute service is a good starting point?
8. What is the operational difference between GKE Autopilot and Standard?
9. Why must an event-driven function be idempotent?
10. Which service fits analytical SQL across very large datasets?
11. What data-model decision is critical for Bigtable performance?
12. Why is Cloud Storage Archive not simply “cheap Standard”?
13. What does Cloud NAT provide, and what does it not provide?
14. Which fields determine a firewall rule’s result?
15. Why inspect an IaC plan before apply?
16. A new Cloud Run revision fails. What makes traffic splitting useful?
17. A GKE Pod is Pending. Name four evidence areas.
18. What is the difference between HPA and cluster autoscaling?
19. Why test a database restore instead of checking only backup success?
20. What is a log sink responsible for?
21. When would Trace help more than a host CPU chart?
22. Why should an alert have an owner and runbook?
23. What is the difference between a role and a policy binding?
24. Why prefer predefined roles to basic roles?
25. What is service-account impersonation useful for?
26. Why are service-account keys high-risk?
27. What does Workload Identity Federation replace?
28. A user has no project binding but still has access. Where should you look?
29. Why should AI-generated infrastructure advice be treated as proposed change?
30. Which current name replaces Cloud Functions in the blueprint?
31. Which current agent runtime name replaces Vertex AI Agent Engine?
32. What should a safe production change verify after rollout?
33. What is the difference between a snapshot and an image?
34. Why can deleting a Google-managed service-agent role break a product?
35. What should determine region selection besides latency?
36. Which evidence helps distinguish DNS, route, firewall, and application failure?
37. Why does a larger quota not prove a resilient design?
38. What does CMEK add besides encryption?
39. When might Cloud Interconnect be preferable to Cloud VPN?
40. What is the first question when selecting among Compute Engine, GKE, and Cloud Run?

41. Why can `gcloud` succeed while a Python client gets a permission error?
42. Does Service Account User grant token impersonation and bucket access?
43. Why might adding a role to a Pod not fix its image pull?
44. Can the lowest firewall priority number anywhere in the hierarchy decide access?
45. Does a new sink copy yesterday's logs automatically?
46. Why can a 20-instance Cloud Run setting fail to protect a database connection budget?
47. Does Pub/Sub exactly-once delivery cover a push handler's external payment?
48. What changes when uniform bucket-level access is enabled?
49. Does a zero-byte dry run always mean a free BigQuery query?
50. What survives a Cloud Workstations stop/restart?

## Answer key

1. It is also an IAM, API, quota, billing, lifecycle, and policy scope. 2. No; alerts-only budgets do not stop usage. A separate eligible-service spend-cap preview has explicit scope, delay and ongoing-charge boundaries. 3. The relevant project/region/service quota, current use, capacity, limits, and regional availability. 4. VPC is global; subnets are regional. 5. When centrally governed networking should be consumed by separately owned service projects. 6. Replication/HA does not cover every deletion, corruption, retention, or recovery requirement. 7. Cloud Run. 8. Autopilot shifts more node/infrastructure management to Google and emphasizes workload requests; Standard exposes node pools/control. 9. Delivery can be retried or duplicated. 10. BigQuery. 11. Row-key design and hotspot avoidance. 12. Retrieval fees and minimum-duration billing differ; Archive remains online object storage, not an offline restore queue. 13. Outbound address translation; not inbound access or firewall authorization. 14. Direction, priority, action, source/destination, protocol/port, and target/effective policy. 15. To review intended create/change/destroy actions, dependencies, policy, cost, and drift. 16. It limits exposure and permits evidence-based promotion or rollback. 17. Events, scheduler/resource requests, node/quota capacity, affinity/taints, volume, image, identity, or policy. 18. HPA changes replicas; cluster autoscaling changes node capacity. 19. A successful backup may still be unusable, incomplete, too slow, or unauthorized at recovery time. 20. Routing matching logs to a destination. 21. For request-path latency across services/dependencies. 22. An unowned, non-actionable alert adds noise rather than recovery. 23. A role is permissions; a binding grants that role to principals at a resource. 24. Basic roles are very broad; predefined roles are service-specific and maintained by Google. 25. Obtaining short-lived credentials to act as a service account under controlled authorization. 26. They are long-lived bearer secrets that are difficult to bound and may leak. 27. Long-lived external workload/user credentials with trusted assertion exchange for short-lived credentials. 28. Inherited folder/organization access, group membership, impersonation, and deny/effective-policy state. 29. It may be stale or wrong and lacks implicit authorization; review and test it. 30. Cloud Run functions. 31. Agent Runtime on Gemini Enterprise Agent Platform. 32. User outcome/SLIs, errors, dependencies, security, cost, and rollback readiness. 33. Snapshot protects disk state; an image is a reusable boot template. 34. The product’s control plane may use that identity and permission. 35. Residency, service/features, availability, cost, connectivity, capacity, and recovery. 36. DNS results, routes/connectivity tests, effective firewall/logs/flow logs, health checks, listener/app logs, and traces. 37. Quota is only a permitted ceiling, not multi-zone design, scaling behavior, dependency capacity, or recovery. 38. Customer control of key lifecycle plus new permission, availability, rotation, disablement/destruction, and recovery failure modes. 39. For predictable high-throughput private hybrid connectivity when its provisioning/cost model is justified; encryption is still a separate decision. 40. How much platform versus guest/orchestrator operation the workload needs, alongside workload constraints.

41. The application may use a different ADC credential source from the CLI; check identity provenance before changing permissions.
42. No. Attachment, short-lived token creation and access to a target resource are separate permission checks.
43. Kubelet normally pulls using the node service account or image-pull credentials, while workload federation governs the running application's API calls.
44. No. First trace policy-layer order and any terminating decision; priority is evaluated within the applicable rules, not one global flattened list.
45. No. Sinks handle entries received after their valid configuration; historical copying requires a separate route.
46. Revision overlap, documented temporary excess instances, pool size and other clients can increase connections; enforce application limits and observe the database.
47. No. The delivery feature has pull/regional/message-ID boundaries; transaction deduplication and external-effect handling are separate.
48. ACL authorization and ACL APIs are disabled, leaving IAM; migration can remove access, and after 90 consecutive days the feature cannot be disabled.
49. No. Row-level security can suppress the estimate to zero; estimates and billing controls need context, and `LIMIT` is not a scan cap on non-clustered tables.
50. Configured persistent home-directory data survives; ephemeral VM/runtime data does not. Updated configuration applies at the next start.

## Source and freshness notes

- The live certification page was checked for status, delivery, renewal, high-level capability lines, and its branding-update notice on September 29, 2026.
- The actual five-page official PDF was extracted in layout mode and mapped through 94 considerations in groups of 16/24/43/11 under 12 numbered objectives on September 29, 2026. It exposes no visible revision date, so this repository records the verification date rather than inventing one.
- The objective monitor hash is unchanged. A previously missing lifecycle snapshot was explicitly established after reviewing the live standard and renewal details; this is baseline initialization, not evidence that the exam just changed.
- The [April 22, 2026 Google announcement](https://cloud.google.com/blog/products/ai-machine-learning/the-new-gemini-enterprise-one-platform-for-agent-development) provides app/platform naming context; the exam PDF defines the tested names. Marketing descriptions do not replace permission and service documentation.
- This review executed only the 32-check local worksheet. No Google Cloud CLI was found on PATH, and no cloud project, billing, IAM, network, GKE, database or event runtime was exercised. Independent human review remains pending.
- Product release stages, regions, quotas, limits, names, prices, course catalogs, durations, and renewal options are volatile. Verify first-party documentation during study and the live certification page before purchase or scheduling.
- The explanations, scenarios, labs, and checks here are original synthesis from public sources. No recalled exam question, answer key, proprietary course text, or exam dump was used.

> **Related items remain contextual:** They help connect exam tasks to architecture, security, reliability, and operations. The published exam guide—not the callout—defines assessable scope.

## Places to learn

This is intentionally **not a complete list**, and it is not a prescription to consume everything. Pick one coherent teaching route, use first-party documentation to close its version gaps, spend substantial time hands-on, and use assessments only to locate weak objectives. Public metadata was checked September 29, 2026. Distinguish card totals from overall schedule estimates; add lab, note, review and troubleshooting time. Paid course interiors and provider labs were not accessed.

| Resource | Access | Estimated time | Best use / currency note |
|---|---|---:|---|
| [Official exam guide](https://services.google.com/fh/files/misc/associate_cloud_engineer_exam_guide_english.pdf) | Public | 45–90 min first pass; revisit weekly | The scope and current-name authority; turn every bullet into a task and decision |
| [Google Skills ACE path](https://www.skills.google/paths/11) | Account; many activities no cost, labs may require credits/entitlement | 17 activities; current per-activity durations were not exposed | Public page showed a relative update of 20 hours, which is an update age, not course duration. The earlier 73h15m total was not reverified; select activities by objective |
| [Google official sample questions](https://docs.google.com/forms/d/e/1FAIpQLSfexWKtXT2OSFJ-obA4iT3GmzgiOCGvjrT9OfxilWC1yPtmfQ/viewform) | Public | 30–60 min plus review | Learn official wording and expose gaps; Google says samples do not predict exam result |
| [Google Cloud Engineer professional certificate](https://www.coursera.org/professional-certificates/cloud-engineering-gcp) | Subscription; audit terms vary | Six course cards total 42h; landing estimate 4 weeks at 10h/week; FAQ says 1.5 months at 5h/week | Public first course now teaches Gemini Notebook study preparation. GKE course outcome still names Container Registry: apply current Artifact Registry guidance. Reconcile the inconsistent schedule estimates |
| [Google Cloud Certified Associate Cloud Engineer Study Guide, 2nd ed.](https://www.oreilly.com/library/view/google-cloud-certified/9781119871446/) | Paid O’Reilly access | Planning allowance 10–15h reading plus labs; current metadata blocked | Prior record says 2023/352 pages, not reverified. Use the current-product and added-service gap checklist; no paid text reviewed |
| [Whizlabs ACE course and practice](https://www.whizlabs.com/google-cloud-certified-associate-cloud-engineer/) | Paid; limited free test | Current full page did not render in this review; verify duration before purchase | Search-index metadata differed from the old 350+ question claim; do not treat either as a newly verified catalog. Public outline and paid lessons were not fully inspected |
| [Google Cloud Tech](https://www.youtube.com/@googlecloudtech) | Public | Pick focused playlists/videos; typically 2–8h total | First-party demonstrations and product updates; use for services you cannot yet explain or operate |
| [Google Cloud Architecture Center](https://cloud.google.com/architecture) | Public | 4–12h targeted reading | Production patterns, decisions and operational tradeoffs rather than exam-only memorization |

The [Pluralsight ACE path](https://www.pluralsight.com/paths/google-associate-cloud-engineer-pluralsight) is now verified: seven course cards total **7h39m**, plus four labs totaling **2h15m**, or **9h54m** versus its rounded ten-hour header. Most core course dates are July–September 2025; a gcloud/IAM demonstration is May 2026 and labs span April–June 2026. Titles still separate planning and deployment, so map them to the current combined domain and fill new-service gaps. This is a public-catalog comparison, not proof that every paid lesson is current. No verified MeasureUp ACE item is added.

### Current-version gap checklist

Before relying on any course or book, confirm that you can map older coverage to the current PDF and independently study:

- the four-domain 20/30/30/20 structure rather than the older five-domain outline;
- Cloud Run functions in place of Cloud Functions branding;
- Agent Runtime and Workbench on Gemini Enterprise Agent Platform, including the former Vertex AI names;
- Gemini Cloud Assist, Gemini CLI, Google Antigravity, and Application Design Center as AI-assisted tools whose output needs validation;
- Cloud NGFW policies, secure Tags, service-account targeting, Cloud Hub, Personalized Service Health, and Managed Service for Prometheus;
- AlloyDB, Database Center, Managed Service for Apache Kafka, NetApp Volumes, Managed Lustre, Hyperdisk, GPU/TPU operations, and current GKE Autopilot behavior;
- Workforce and Workload Identity Federation, short-lived credentials, service-account impersonation, and Workload Identity Federation for GKE.
