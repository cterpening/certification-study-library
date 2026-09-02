---
exam_code: GOOGLE-ASSOCIATE-CLOUD-ENGINEER
vendor_id: google-cloud
official_blueprint: https://cloud.google.com/learn/certification/cloud-engineer
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Google Cloud Associate Cloud Engineer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 2, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#google-associate-cloud-engineer-coverage-record). The [official certification page](https://cloud.google.com/learn/certification/cloud-engineer) and its linked [exam guide](https://services.google.com/fh/files/misc/associate_cloud_engineer_exam_guide_english.pdf) are authoritative.

**Current baseline:** Four domains weighted approximately 20%, 30%, 30%, and 20%; detailed PDF and live page checked September 2, 2026<br>
**Published change notice:** Google says the exam was updated for recent branding changes and directs candidates to the exam guide for the product names used on the exam. No future effective date is announced.<br>
**Official source:** [Associate Cloud Engineer certification page](https://cloud.google.com/learn/certification/cloud-engineer) · [official detailed exam guide](https://services.google.com/fh/files/misc/associate_cloud_engineer_exam_guide_english.pdf)

## How to use this guide

ACE tests whether you can turn a requirement into a working, secured, observable Google Cloud solution and operate it safely. Learn each service through a repeated loop: choose it, configure it, verify it, observe it, diagnose it, change it, and recover it. Practice in the console and Cloud Shell, then repeat important tasks with `gcloud`, `kubectl`, and Terraform. Memorizing a service catalog is not enough.

The standard exam is two hours, USD 125 before applicable tax or regional differences, 50–60 multiple-choice and multiple-select questions, online- or onsite-proctored, available in English, Japanese, Spanish, and Portuguese, and valid for three years. There is no formal prerequisite; Google recommends at least six months of hands-on experience. Verify the [live page](https://cloud.google.com/learn/certification/cloud-engineer) before scheduling.

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

### Networking and location foundation

A VPC is global; its subnets are regional. Custom mode gives explicit address control. Shared VPC centralizes a host project’s network while service projects own workload resources. VPC Network Peering connects networks without transitive routing and does not merge IAM or administration. Plan non-overlapping address space, DNS, routing, hybrid connectivity, egress, private access, firewall policy, and IP capacity before deployment.

Regions contain zones. Zonal placement is a single failure-domain choice; regional or multi-regional design trades cost and complexity for resilience. Check latency, residency, availability, service features, and recovery requirements rather than choosing the nearest region automatically.

### Observability, assets, quotas, and AI assistance

Provision Cloud Logging and Cloud Monitoring deliberately: retention, log buckets, sinks, metrics, dashboards, alerts, notification channels, and operational ownership. Audit logs answer control-plane and data-access questions only when the required log types are enabled and retained. Cloud Asset Inventory provides searchable inventory, history, feeds, and policy-analysis inputs. Gemini Cloud Assist can help analyze resources and operations, but validate suggestions against actual state, permissions, policy, cost, and change controls.

Quotas protect platform and tenant capacity. Distinguish allocation quota from rate quota, regional from global limits, and project from account scope. A production readiness check includes current use, expected peak, lead time for increases, fallback capacity, and alerts.

### Billing configuration

Billing accounts fund projects. Use budgets and alerts for visibility; a budget does not automatically cap or stop spend. Export detailed billing data to BigQuery for allocation, anomaly analysis, forecasting, and FinOps reporting. Labels, tags, project boundaries, committed-use planning, and accountable owners make costs actionable.

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

For Compute Engine, choose zone/region, machine family/type, boot image, disk, network, service account, shielded/security settings, availability policy, and metadata. Instance templates produce managed instance groups; autoscaling reacts to signals, while autohealing recreates unhealthy instances. Spot VMs reduce cost but may be preempted, so workloads need checkpointing or retry tolerance. OS Login centralizes SSH authorization in IAM. VM Manager supports inventory, patch, configuration, and OS-policy operations.

Persistent Disk and Hyperdisk are block storage choices with different performance and availability profiles. Regional Persistent Disk replicates across zones; it does not replace application-aware backup, recovery testing, or a database-native HA design.

GKE mode is an operating-model choice. Autopilot manages more infrastructure and enforces workload-oriented resource behavior; Standard exposes node pools and more configuration. Regional clusters improve control-plane availability; private clusters reduce public exposure. Deploy containers from Artifact Registry, set resource requests/limits, choose Services/Ingress or Gateway exposure, and understand Pods, Deployments, StatefulSets, ConfigMaps, Secrets, volumes, and disruption behavior.

Cloud Run revisions support gradual rollout and traffic splitting. Events commonly reach services/functions through Eventarc or Pub/Sub. Design for duplicate delivery, retries, ordering limits, dead-letter handling, and idempotency rather than assuming exactly-once execution.

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

Firewall evaluation is direction-aware and stateful. Specify ingress/egress, action, source/destination, protocol/port, priority, and target. Cloud NGFW policies can centralize hierarchical/global/regional control and use secure Tags or service accounts as workload-aware targets. Validate effective rules; a configured allow rule may lose to a higher-priority deny.

Cloud VPN supplies encrypted IP connectivity; Cloud Interconnect supplies dedicated or provider-based connectivity and normally still needs an encryption decision. Peering provides private network-to-network reachability without transitivity. Cloud NAT supplies outbound translation for resources without external IPv4 addresses; it is not an inbound proxy or firewall. Choose the load balancer by internal/external reachability, global/regional scope, L4/L7 protocol, backends, TLS, and resilience requirement. Premium and Standard Network Service Tiers differ in routing scope and supported features.

### Provision consistently

Terraform declares infrastructure through providers, resources, modules, state, plan, and apply. Protect state, review plans, pin/upgrade providers deliberately, detect drift, and separate reusable modules from environment inputs. Config Connector represents Google Cloud resources through Kubernetes objects; Helm packages Kubernetes applications. Fabric FAST supplies opinionated Terraform foundations. AI-assisted tools such as Gemini CLI, Google Antigravity, Gemini Cloud Assist, and Application Design Center can accelerate design or code, but their output remains proposed change: review identity, policy, region, dependency, cost, security, and destroy/rollback impact.

> **Related item:** Infrastructure as code makes a configuration reproducible; it does not make the design correct. Policy checks, peer review, tests, state protection, controlled credentials, and post-deployment verification remain necessary.

---

## 3. Ensuring successful operation — about 30%

### Operate compute safely

Inventory first: confirm project, region/zone, resource name, labels/tags, desired state, dependency, and recent changes. For a VM, inspect status, serial output, logs, service health, network path, disk/CPU/memory, and guest state before restarting it. Use IAP or OS Login patterns where appropriate rather than distributing SSH keys. Images are reusable boot-disk templates; snapshots are incremental point-in-time disk protection. Schedule them, monitor success, define retention, and prove restore.

For GKE, inspect clusters, nodes/node pools, Pods, Services, Deployments/StatefulSets, events, logs, resource requests, health probes, autoscalers, disruption budgets, and rollout status. Horizontal Pod Autoscaling changes replica count; Vertical Pod Autoscaling recommends or changes resource requests; cluster/node autoscaling changes capacity. Autopilot scheduling depends strongly on valid Pod requests. Configure Artifact Registry access with the workload/node identity model actually used.

For Cloud Run, deploy immutable revisions, direct a small traffic percentage, observe errors/latency, and promote or roll back. Minimum instances reduce cold-start exposure at a cost; maximum instances protect dependencies and spend; concurrency changes per-instance pressure. Attach accelerators only after verifying quota, region, runtime support, utilization, and fallback.

Agent and notebook operations require the same discipline as other workloads: named owner, identity, authorized data and tools, versioned artifact, evaluation, quotas/cost, logs/traces, stop/rollback, and incident response. The current blueprint calls these Agent Runtime and Gemini Enterprise Agent Platform Workbench (formerly Vertex AI Agent Engine and Vertex AI Workbench).

### Operate data and storage

Use uniform bucket-level access when IAM is the intended authorization model; know whether legacy ACLs are still present. Lifecycle rules manage transitions/deletion; retention policies and holds prevent deletion. Versioning aids recovery but can increase cost and does not replace independent backup. CMEK changes key ownership and failure modes: rotation, permission, availability, disablement, destruction, and recovery must be managed.

For managed databases, monitor availability, connections, CPU/storage, replication, query latency, backup status, recovery point, and maintenance. Backups are valuable only if restorations are tested. Use native query and diagnostic tools within least privilege. Database Center provides fleet visibility; it is not a substitute for engine-specific remediation. For BigQuery and Dataflow, inspect job status, errors, bytes/slots/workers, skew, retries, output correctness, and downstream effects.

### Operate the network

Reserve static IPs when endpoints must remain stable. Subnet expansion is one-way in common workflows and must not overlap existing ranges. Custom routes need destination, next hop, scope, priority, and reachability validation. Cloud DNS controls name resolution; Cloud NAT controls outbound translation. Diagnose in layers: DNS → route → firewall/policy → load balancer/health check → service/listener → application → dependency. VPC Flow Logs and firewall logs provide evidence but must be enabled and sampled appropriately.

### Monitoring, logging, and diagnosis

Start from a service-level symptom and a time window. Metrics quantify behavior; logs record events; traces follow requests; profiles show runtime resource use. Create alerts on actionable conditions tied to an owner and runbook. Avoid alerting only on raw utilization when user impact is what matters. Custom metrics and log-based metrics can expose application signals but add cardinality, cost, and lifecycle concerns.

Cloud Logging uses log buckets for storage/retention, Log Router sinks for routing, and Log Analytics for analytical queries. Exports to BigQuery or external systems need destination permissions, capacity, retention, and sensitive-data handling. Audit, VPC Flow, and firewall logs answer different questions.

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

Prefer attached identities, service-account impersonation, short-lived tokens, Workload Identity Federation for external workloads, and Workload Identity Federation for GKE over downloadable keys. If a key is unavoidable, inventory, restrict, rotate, monitor, and retire it. Federation exchanges a trusted external assertion for short-lived Google credentials; trust configuration, attribute mapping/conditions, audience, and principal binding are core controls.

Google-managed service accounts and service agents perform platform functions. Removing their permissions can break services. Identify the agent and required role from first-party documentation before modifying it.

For GKE, map Kubernetes service accounts to Google Cloud identities through Workload Identity Federation for GKE so Pods receive bounded credentials without node-wide keys. Also apply Kubernetes RBAC, namespace, network, image, secret, and admission controls; Google IAM alone does not govern every in-cluster action.

> **Related item:** Authentication establishes identity; authorization determines permitted action. A valid token does not prove that the request should be allowed, and encryption does not repair excessive authorization.

---

## Integrated scenarios

### Scenario 1 — Public API with unpredictable traffic

A stateless container receives HTTPS traffic, writes relational orders, publishes fulfillment events, and must deploy without downtime. Start with Cloud Run behind the appropriate managed endpoint/load-balancing design, Cloud SQL or AlloyDB based on scale/compatibility evidence, Pub/Sub for decoupling, Secret Manager for secrets, a dedicated service account, private connectivity where required, and Logging/Monitoring. Set min/max instances and concurrency based on latency and database connection capacity. Deploy a revision to a small traffic share, observe application and dependency SLIs, then promote or roll back. Make event consumers idempotent and configure retry/dead-letter behavior.

### Scenario 2 — Governed multi-team platform

Several teams need isolated projects but shared private networking and central security policy. Use organization/folder policy boundaries, service projects attached to a Shared VPC host project, group-based roles, workload federation, Cloud NGFW policy, centralized DNS/connectivity, billing export, budgets, asset inventory, and log routing. Delegate only the roles teams need. Test inherited policy, quotas, regional availability, and incident ownership before onboarding workloads.

### Scenario 3 — GKE service is slow after release

Confirm user impact and recent rollout. Inspect Cloud Monitoring metrics, GKE events, Pod status/probes, requests/limits, HPA/VPA, node capacity, logs, traces, dependency/query latency, load-balancer health, and service health. Stabilize by traffic rollback or scaling only when safe. If Pods are pending, distinguish quota/node capacity, affinity/taints, resource request, volume, and policy causes. Verify the user SLI, then record the detection and deployment-control improvements.

---

## Hands-on lab path

Use a disposable project, budgets, and explicit teardown. Save commands, expected results, evidence, and recovery notes.

1. **Foundation:** create a project, link billing, enable APIs, inspect quota, create a budget alert, query Cloud Asset Inventory, and verify effective policies.
2. **IAM:** create groups/service accounts, grant narrow roles, test inheritance and impersonation, then remove access and verify denial.
3. **Network:** create a custom VPC and regional subnets, firewall/NGFW rules, Cloud NAT, DNS, and flow logging; prove allowed and denied paths.
4. **Compute Engine:** deploy a template and managed instance group, configure health checking/autoscaling, use OS Login, snapshot a disk, and perform a restore test.
5. **Cloud Run/events:** deploy two revisions, split traffic, cap scaling, invoke through an authenticated path, process a Pub/Sub/Eventarc event idempotently, and roll back.
6. **GKE:** deploy an Autopilot or Standard cluster and app, configure Artifact Registry identity, Services, probes, requests, HPA, rollout, logs, and Workload Identity Federation.
7. **Data:** compare Cloud Storage lifecycle/retention, Cloud SQL backup/restore, a BigQuery query/job, and Pub/Sub retry/dead-letter behavior.
8. **Operations/IaC:** provision a small stack with Terraform, review plan/state, create dashboard/alert/log sink, inject a failure, diagnose it with evidence, recover, and destroy safely.

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

## Answer key

1. It is also an IAM, API, quota, billing, lifecycle, and policy scope. 2. No; alerts provide visibility unless separately automated controls take action. 3. The relevant project/region/service quota, current use, capacity, limits, and regional availability. 4. VPC is global; subnets are regional. 5. When centrally governed networking should be consumed by separately owned service projects. 6. Replication/HA does not cover every deletion, corruption, retention, or recovery requirement. 7. Cloud Run. 8. Autopilot shifts more node/infrastructure management to Google and emphasizes workload requests; Standard exposes node pools/control. 9. Delivery can be retried or duplicated. 10. BigQuery. 11. Row-key design and hotspot avoidance. 12. Retrieval, minimum-duration, latency/workflow, and cost behavior differ. 13. Outbound address translation; not inbound access or firewall authorization. 14. Direction, priority, action, source/destination, protocol/port, and target/effective policy. 15. To review intended create/change/destroy actions, dependencies, policy, cost, and drift. 16. It limits exposure and permits evidence-based promotion or rollback. 17. Events, scheduler/resource requests, node/quota capacity, affinity/taints, volume, image, identity, or policy. 18. HPA changes replicas; cluster autoscaling changes node capacity. 19. A successful backup may still be unusable, incomplete, too slow, or unauthorized at recovery time. 20. Routing matching logs to a destination. 21. For request-path latency across services/dependencies. 22. An unowned, non-actionable alert adds noise rather than recovery. 23. A role is permissions; a binding grants that role to principals at a resource. 24. Basic roles are very broad; predefined roles are service-specific and maintained by Google. 25. Obtaining short-lived credentials to act as a service account under controlled authorization. 26. They are long-lived bearer secrets that are difficult to bound and may leak. 27. Long-lived external workload/user credentials with trusted assertion exchange for short-lived credentials. 28. Inherited folder/organization access, group membership, impersonation, and deny/effective-policy state. 29. It may be stale or wrong and lacks implicit authorization; review and test it. 30. Cloud Run functions. 31. Agent Runtime on Gemini Enterprise Agent Platform. 32. User outcome/SLIs, errors, dependencies, security, cost, and rollback readiness. 33. Snapshot protects disk state; an image is a reusable boot template. 34. The product’s control plane may use that identity and permission. 35. Residency, service/features, availability, cost, connectivity, capacity, and recovery. 36. DNS results, routes/connectivity tests, effective firewall/logs/flow logs, health checks, listener/app logs, and traces. 37. Quota is only a permitted ceiling, not multi-zone design, scaling behavior, dependency capacity, or recovery. 38. Customer control of key lifecycle plus new permission, availability, rotation, disablement/destruction, and recovery failure modes. 39. For predictable high-throughput private hybrid connectivity when its provisioning/cost model is justified; encryption is still a separate decision. 40. How much platform versus guest/orchestrator operation the workload needs, alongside workload constraints.

## Places to learn

This is intentionally **not a complete list**, and it is not a prescription to consume everything. Pick one coherent teaching route, use first-party documentation to close its version gaps, spend substantial time hands-on, and use assessments only to locate weak objectives. Times are provider estimates or page-derived totals checked September 2, 2026; add lab, note, review, and troubleshooting time.

| Resource | Access | Estimated time | Best use / currency note |
|---|---|---:|---|
| [Official exam guide](https://services.google.com/fh/files/misc/associate_cloud_engineer_exam_guide_english.pdf) | Public | 45–90 min first pass; revisit weekly | The scope and current-name authority; turn every bullet into a task and decision |
| [Google Skills ACE path](https://www.skills.google/paths/11) | Account; many activities no cost, labs may require credits/entitlement | 17 activities totaling about 73h15m as listed | Broad modular menu with courses, labs and badges; select to close gaps rather than treating every activity as mandatory |
| [Google official sample questions](https://docs.google.com/forms/d/e/1FAIpQLSfexWKtXT2OSFJ-obA4iT3GmzgiOCGvjrT9OfxilWC1yPtmfQ/viewform) | Public | 30–60 min plus review | Learn official wording and expose gaps; Google says samples do not predict exam result |
| [Preparing for Your Associate Cloud Engineer Journey](https://www.coursera.org/professional-certificates/cloud-engineering-gcp) | Subscription; audit terms vary | Six courses list about 42 content hours; page also estimates three months at 10h/week | Coherent Google Cloud route with broader learning/practice; reconcile every module to the new four-domain PDF |
| [Google Cloud Certified Associate Cloud Engineer Study Guide, 2nd ed.](https://www.oreilly.com/library/view/google-cloud-certified/9781119871446/) | Paid O’Reilly access | Roughly 10–15h reading plus labs (352 pages) | Structured reference, but published in 2023: use the explicit current-product and added-service gap checklist below |
| [Whizlabs ACE course and practice](https://www.whizlabs.com/google-cloud-certified-associate-cloud-engineer/) | Paid; limited free test | Page currently advertises 9+ video hours, 350+ questions, and 40+ labs; budget 25–45h with review | Useful lab/practice menu; verify each explanation against first-party docs and reject dump-like or unsupported material |
| [Google Cloud Tech](https://www.youtube.com/@googlecloudtech) | Public | Pick focused playlists/videos; typically 2–8h total | First-party demonstrations and product updates; use for services you cannot yet explain or operate |
| [Google Cloud Architecture Center](https://cloud.google.com/architecture) | Public | 4–12h targeted reading | Production patterns, decisions and operational tradeoffs rather than exam-only memorization |

No current ACE-specific MeasureUp product or current Pluralsight certification path was located during this check, so neither is invented here. Vendor catalogs change; add one when a live product page can be verified.

### Current-version gap checklist

Before relying on any course or book, confirm that you can map older coverage to the current PDF and independently study:

- the four-domain 20/30/30/20 structure rather than the older five-domain outline;
- Cloud Run functions in place of Cloud Functions branding;
- Agent Runtime and Workbench on Gemini Enterprise Agent Platform, including the former Vertex AI names;
- Gemini Cloud Assist, Gemini CLI, Google Antigravity, and Application Design Center as AI-assisted tools whose output needs validation;
- Cloud NGFW policies, secure Tags, service-account targeting, Cloud Hub, Personalized Service Health, and Managed Service for Prometheus;
- AlloyDB, Database Center, Managed Service for Apache Kafka, NetApp Volumes, Managed Lustre, Hyperdisk, GPU/TPU operations, and current GKE Autopilot behavior;
- Workforce and Workload Identity Federation, short-lived credentials, service-account impersonation, and Workload Identity Federation for GKE.

## Source and freshness notes

- The live certification page was checked for status, delivery, renewal, high-level capability lines, and its branding-update notice on September 2, 2026.
- The detailed official PDF was independently extracted and mapped through every section and consideration on September 2, 2026. It exposes no visible revision date, so this repository records the verification date rather than inventing one.
- Product release stages, regions, quotas, limits, names, prices, course catalogs, durations, and renewal options are volatile. Verify first-party documentation during study and the live certification page before purchase or scheduling.
- The explanations, scenarios, labs, and checks here are original synthesis from public sources. No recalled exam question, answer key, proprietary course text, or exam dump was used.

> **Related items remain contextual:** They help connect exam tasks to architecture, security, reliability, and operations. The published exam guide—not the callout—defines assessable scope.
