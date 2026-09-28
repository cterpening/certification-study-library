---
exam_code: AZ-305
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# AZ-305 Designing Microsoft Azure Infrastructure Solutions Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 28, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#az-305-coverage-record). The [official AZ-305 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305) is authoritative.

**Current baseline:** Skills measured as of April 17, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 28, 2026.<br>
**Certification prerequisite:** Azure Administrator Associate is required for the Azure Solutions Architect Expert certification; it is not a prerequisite merely to sit AZ-305.<br>
**Official source:** [AZ-305 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305)

The [September 28 deep-review report](../docs/research/2026-09-28-az-305-deep-review.md) maps all 49 detailed objectives. Seven worked examples, ten labs and 48 explained checks support design practice. Calculations and the local transaction example were tested offline; Azure deployment, failover and paid course content were not tested. Independent human review remains pending.

The [credential profile](https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/) lists ten exam languages and certification renewal. Check scheduling for your delivery details; this review did not verify an exact exam duration.

## How to use this guide

AZ-305 tests design judgment. A technically possible service is not automatically the best answer. For every scenario, turn prose into explicit requirements, eliminate choices that violate a hard constraint, and compare the remaining choices across reliability, security, cost, operations, and performance.

Use this guide after administrator-level practice. You should already understand what core Azure resources do and how identity, networking, storage, compute, monitoring, and governance are configured. The architect-level step is explaining *why this combination* meets the stated requirements and what trade-offs it introduces.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Design question |
|---|---:|---|
| Design identity, governance, and monitoring solutions | 25–30% | How will the solution establish trust, constrain change, prove compliance, and expose useful operational signals? |
| Design data storage solutions | 20–25% | Which data model and service meet transaction, query, scale, durability, integration, and cost requirements? |
| Design business continuity solutions | 15–20% | Which failure modes must be survived, and how will recovery be measured and proven? |
| Design infrastructure solutions | 30–35% | Which compute, application, migration, and network architecture best fits the workload and operating model? |

---

## 1. Architect decision method

### Translate narrative into constraints

Start with a small decision record rather than a product list:

| Requirement class | Questions to extract | Evidence in a proposed design |
|---|---|---|
| Functional | What must users and systems do? Which protocols, APIs, query shapes, and integrations exist? | Component responsibilities and data flows |
| Reliability | What are the availability target, RTO, RPO, failure boundaries, and degraded modes? | Redundancy, failover, backup, restore, and validation plan |
| Security | Who or what accesses each plane? Which data is sensitive? Where are trust boundaries? | Identity flow, least privilege, network path, encryption, logging |
| Performance | What latency, throughput, concurrency, data volume, and geography are required? | Service tier, scale unit, partition strategy, caching and routing |
| Operations | Who deploys, monitors, patches, rotates, restores, and supports the workload? | Automation, ownership, alerts, runbooks, service-management boundary |
| Governance | Which residency, compliance, policy, tagging, separation, and audit requirements apply? | Hierarchy, policy, evidence retention, exemptions and review |
| Cost | What is the budget, growth curve, licensing constraint, and tolerance for idle capacity? | Cost model, scale behavior, reservations/commitments, lifecycle controls |

Treat words such as **must**, **only**, **without**, and **least administrative effort** as hard constraints. A preferred feature cannot compensate for violating one. Record assumptions when the scenario does not supply enough information.

### Apply the Well-Architected lenses

The [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/) uses five pillars: reliability, security, cost optimization, operational excellence, and performance efficiency. A design choice often improves one while adding cost or operational complexity elsewhere.

Examples:

- Active-active regional deployment improves some availability and latency goals but adds data-consistency, routing, deployment, testing, and cost concerns.
- Platform as a service usually reduces patching and infrastructure ownership but can impose service limits, supported-runtime constraints, and migration work.
- Private endpoints reduce public exposure but add DNS, address-space, routing, endpoint-per-subresource, and operational dependencies.
- Customer-managed keys can satisfy control requirements but add identity, key-store availability, rotation, recovery, and separation-of-duties dependencies.

Use the [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/) for patterns and reference architectures, then adapt them. A reference architecture is evidence and a starting point, not a substitute for workload requirements.

> **Related item:** The [Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/) addresses organizational adoption, landing zones, governance, security, management, migration, and modernization. Well-Architected focuses primarily on workload quality. A good enterprise design uses both at their appropriate scopes.

### Separate control, data, and management responsibilities

For every component, identify:

```text
control/management plane: create, configure, authorize, audit changes
data plane: serve application requests and manipulate workload data
operations plane: observe, deploy, back up, restore, rotate, and respond
```

Also state the service model. In IaaS, the customer normally owns more guest configuration and patching. In managed PaaS and serverless services, Microsoft owns more platform work, while the customer still owns identity, data, application behavior, configuration, observability, and recovery decisions.

---

## 2. Design identity, governance, and monitoring solutions (25–30%)

### Logging and monitoring

Design observability from decisions that operators must make, not from a desire to collect everything. The [Azure Monitor documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/) distinguishes platform metrics, logs, traces, changes, and health signals across Azure Monitor capabilities.

#### Build a signal-routing design

| Source | Typical information | Design considerations |
|---|---|---|
| Azure Activity Log | Subscription-level control-plane events | Export beyond default retention when audit or central analysis requires it |
| Resource logs | Service-specific operational or data events | Diagnostic categories, cost, destinations, schema, regional requirements |
| Platform metrics | Numeric time-series resource health/performance | Dimensions, aggregation, alert sensitivity, retention/export |
| Guest OS and application telemetry | Workload logs, dependencies, traces, custom metrics | Agent/SDK, sampling, sensitive data, correlation IDs, workspace design |
| Microsoft Entra logs | Sign-ins, audit, provisioning, risk-related evidence | Licensing, retention, access separation, export and investigation needs |
| Service Health / Resource Health | Platform incidents and individual resource health | Subscription scoping, action groups, operational ownership |

A diagnostic setting routes supported signals to destinations such as Log Analytics, Storage, or Event Hubs. Choose destinations by use case: interactive KQL and alerting, long-term/immutable-oriented retention, or streaming to external systems. One destination does not inherently satisfy every requirement.

Workspace design balances central oversight against data residency, access boundaries, query scope, chargeback, retention, and operational autonomy. A single workspace is simple but can create broad access and ingestion concentration; many workspaces improve isolation but complicate cross-workspace queries and governance.

Design alerts as an owned response system:

```text
meaningful signal -> condition/window -> alert rule -> action group
                  -> owner/runbook -> acknowledgement -> learning/tuning
```

Do not use a metric threshold when absence of data, a multi-resource correlation, or an application SLO is the real condition. **VERIFY CURRENT:** supported diagnostic categories, workspace features, table plans, retention, pricing, alert limits, and region availability.

> **Related item:** An SLI is the measured behavior, an SLO is the target, and an SLA is a commitment with defined consequences. Azure service SLAs do not automatically become the end-to-end workload SLA; dependencies and application design change the result.

#### Match the log table plan to the operational question

The current [Azure Monitor Logs comparison](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-platform-logs) separates Analytics, Basic and Auxiliary/Lake. Basic supports Simple Log Alerts; Auxiliary/Lake does not support alerts. Auxiliary/Lake also lacks workspace replication and is intended for less frequent analysis. Basic and Auxiliary queries incur query charges, so cheaper ingestion alone does not establish lower total cost.

For a payment-failure alert, an incident investigation and a long-retention audit, record the required alert type, query scope, table eligibility, retention, replication and expected query frequency separately. Verify the table's supported plan before changing it. An infrequently queried audit copy should not silently become the only source for a time-sensitive alert.

### Authentication and authorization

Keep identity proof, policy evaluation, and resource authorization separate:

- **Authentication** establishes which principal is acting.
- **Conditional Access** evaluates contextual access policy for supported sign-in flows.
- **Microsoft Entra roles** authorize directory administration.
- **Azure RBAC** authorizes management- and supported data-plane actions at Azure scopes.
- **Application roles/scopes/claims** authorize behavior inside an application or API.

An Azure role assignment combines principal, role definition, and scope. The [Azure RBAC overview](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) should anchor least-privilege designs. Prefer group-based human assignments and workload identities for applications. Use managed identities when an Azure-hosted workload can use them; this removes the need to distribute an application secret but does not remove the need for scoped authorization and lifecycle control.

For hybrid/on-premises access, first identify whether the target trusts Active Directory Domain Services, Microsoft Entra ID, certificates, Kerberos, an application identity provider, or another protocol. Synchronization does not make two authorization systems identical. Consider authentication availability during WAN or cloud outages and how privileged access is recovered.

#### Secrets, certificates, and keys

[Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview) centralizes supported secret, key, and certificate operations. Design includes:

- vault boundary and tenancy;
- RBAC/access model and separation of duties;
- managed identity for callers;
- public firewall or private endpoint plus DNS;
- rotation, expiry notification, version pinning versus latest-version behavior;
- soft delete, purge protection, backup/recovery and regional dependency;
- logging and emergency access.

Storing a secret in Key Vault is incomplete if the deployment pipeline copies it into logs, a template parameter file, or application configuration. Prefer secretless/federated patterns where supported.

> **Related item:** Microsoft Entra Privileged Identity Management makes supported role assignments eligible and time-bound, with controls such as approval or MFA. It reduces standing privilege; it does not repair an over-broad role definition or scope.

#### Key Vault creation and recovery boundaries

With [API version 2026-02-01 and later](https://learn.microsoft.com/en-us/azure/key-vault/general/access-control-default), new vaults default to Azure RBAC. Updating an existing vault with that API does not switch its access model. Make the intended authorization model explicit and test caller data permissions. Earlier control-plane API versions retire February 27, 2027; an API upgrade and an access-model migration are separate changes.

[Manual Key Vault backup](https://learn.microsoft.com/en-us/azure/key-vault/general/backup) is per object, not a single whole-vault export. Its encrypted backup must be restored within the same Azure subscription and geography; more than 500 historical versions of one object are unsupported. This is not an arbitrary cross-subscription escape path. Document key versions, certificates, identity, network access and restore prerequisites alongside the data that depends on them.

### Governance and identity governance

Use different controls for different jobs:

| Control | Primary design purpose | Common mistake |
|---|---|---|
| Management group/subscription hierarchy | Apply governance and access across organizational/resource boundaries | Mirroring a frequently changing organization chart too literally |
| Azure Policy | Audit, deny, modify, or deploy required resource configuration | Treating compliance state as proof of security or granting access |
| Azure RBAC | Authorize a principal at scope | Assigning Owner broadly to solve one missing action |
| Resource lock | Prevent management-plane deletion or modification | Assuming it protects data-plane deletion or replaces backup |
| Tag | Ownership, classification, automation, and cost metadata | Assuming tags always inherit without policy/automation |
| Cost budget/alert | Detect spending thresholds or forecast conditions | Assuming a budget automatically shuts resources down |

The [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview) explains definitions, initiatives, assignments, exemptions, effects, compliance, and remediation. Design policy-as-code with testing, versioning, staged rollout, exemptions that have owners/expiry, and remediation permissions. A deny-first rollout without impact analysis can block recovery, platform automation, or application deployment.

Identity governance adds joiner-mover-leaver lifecycle, entitlement management, access packages, access reviews, privileged access, and separation-of-duties thinking. Decide who approves access, how expiry works, which connected systems participate, and how evidence is retained. **VERIFY CURRENT:** licensing and feature availability.

#### Domain failure modes

- Collecting logs without a query, retention, alert, owner, or response purpose.
- Sending every tenant to one workspace without designing residency and access boundaries.
- Confusing Entra directory roles, Azure RBAC, and application authorization.
- Using stored credentials where workload identity or federation is supported.
- Designing a private Key Vault endpoint without hybrid/private DNS resolution.
- Assigning a policy effect without planning existing-resource remediation and exemptions.
- Treating an annual access review as a complete privileged-access strategy.

---

## 3. Design data storage solutions (20–25%)

### Start with access patterns, not product names

The [Azure data-model decision guidance](https://learn.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/understand-data-store-models) emphasizes transactions, point reads, aggregations, full-text/vector search, time-window scans, object delivery, consistency, latency, governance, and cost. Model the following before choosing a service:

```text
data shape + access/query pattern + transaction boundary
+ read/write rate + latency + scale/partition key
+ consistency + durability/retention + geography
+ compatibility/migration + security/governance + operations/cost
```

Polyglot persistence can fit divergent access patterns, but every added store adds identity, network, backup, replication, monitoring, skills, and consistency work. Prefer the smallest set that meets the requirements.

### Relational data

| Choice | Strong fit | Design questions |
|---|---|---|
| Azure SQL Database | Cloud applications needing managed SQL Server capabilities | Single database versus elastic pool; provisioned/serverless/hyperscale; zone and geo design; compatibility |
| Azure SQL Managed Instance | High SQL Server compatibility and instance-scoped features with managed operations | Subnet/networking, migration compatibility, service tier, maintenance, failover design |
| SQL Server on Azure VMs | OS/instance control or features unavailable in managed services | Patching, backup, availability group, storage performance, licensing, cluster operations |
| Azure Database for PostgreSQL/MySQL | Managed open-source engine compatibility | Extension/version support, compute/storage, HA, replicas, migration and connection limits |

Choose tier and compute from measured CPU, memory, I/O, storage, log rate, concurrency, latency, scale, and availability requirements. Serverless or elastic pooling can improve utilization for certain variable workloads; provisioned dedicated compute may better support predictable sustained demand. **VERIFY CURRENT:** service tiers, availability modes, engine versions, limits, licensing, region support, and pricing.

Separate high availability from disaster recovery. A zone-redundant database can address an in-region zone failure; geo-replication/failover groups address regional design needs; backups provide point-in-time or longer-term recovery. They have different consistency, data-loss, failover, endpoint, validation, and cost characteristics.

[SQL Database failover groups](https://learn.microsoft.com/en-us/azure/azure-sql/database/failover-group-sql-db?view=azuresql) provide stable read/write and read-only listener names. Client reconnects, retry handling and every non-database dependency still need recovery design. Microsoft currently recommends customer-managed failover; Microsoft-managed failover responds to widespread regional outages and should not be assumed to cover an isolated application failure. The SQL Database and Managed Instance procedures differ. Specify who declares an incident, evaluates potential data loss, authorizes failover and validates the application.

### Semi-structured and unstructured data

| Requirement | Likely design family | Important discriminator |
|---|---|---|
| JSON aggregates with global distribution and low-latency point access | Azure Cosmos DB | API, partition key, request units/autoscale, consistency, multi-region writes, indexing |
| Binary objects, media, logs, backups, data-lake zones | Blob Storage / Data Lake Storage | Namespace, access tier, redundancy, lifecycle, immutable retention, analytics access |
| Managed file protocol compatibility | Azure Files or Azure NetApp Files | SMB/NFS requirements, identity, performance tier, replication/backup, network access |
| Low-latency cache/session data | Azure Managed Redis | Cache-aside behavior, eviction, persistence, clustering, zone/geo needs, source of truth |
| Full-text/vector retrieval over indexed content | Azure AI Search or supported database feature | Indexing pipeline, freshness, query semantics, scale, primary source of truth |

For Cosmos DB, a poor partition key can create hot partitions, limited transaction scope, uneven storage, and expensive queries. Evaluate value cardinality, distribution, query routing, growth, and transactional boundaries before deployment. Consistency level, region topology, failover, conflict resolution, and retry behavior belong to the application design.

For Azure Storage, [redundancy options](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy) protect against specified infrastructure failures; they do not inherently protect against replicated logical deletion or corruption. Add versioning, soft delete, immutability, lifecycle, or backup based on the threat and recovery need.

> **Related item:** Data durability is the probability that data remains intact; availability is the ability to serve a request; consistency defines what version a read may observe. A service can offer high durability while an application is temporarily unavailable or reads an older replica.

For Cosmos DB, a logical partition groups items with the same partition-key value and defines the scope for transactions described in the [partitioning overview](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview). A large account-wide throughput budget does not fix a heavily skewed key. Evaluate write distribution, point-read routing, cross-partition queries and atomic business operations together. Example 2 uses fictional limits to practice this trade-off without presenting them as Azure service limits.

### Data integration and analysis

Classify the movement first:

| Pattern | Typical requirement | Design direction |
|---|---|---|
| Batch copy/orchestration | Scheduled movement, dependencies, transformations, hybrid sources | Data Factory/Fabric pipeline-style orchestration and integration runtime design |
| Streaming/event ingestion | High-rate ordered telemetry or event stream with retention/replay | Event Hubs or an appropriate managed streaming platform |
| Business message | Durable command/work queue, topics/subscriptions, dead lettering, transactions | Service Bus |
| Discrete event notification | React to a state change and route to subscribers | Event Grid |
| Database change propagation | Incremental processing from source changes | Native CDC/change feed plus idempotent consumers |

Do not choose only by volume. Consider delivery semantics, ordering scope, replay, retention, dead lettering, duplicate handling, back pressure, protocol, network path, schema evolution, and operational ownership. Consumers should be idempotent whenever delivery can repeat.

For analysis, decide whether the workload is transactional, near-real-time operational analytics, lake/lakehouse, warehouse/BI, log/time-series analysis, or data science. Separate storage and compute when that improves scale/cost, but account for data movement, governance, lineage, concurrency, freshness, and serving requirements.

#### Domain failure modes

- Selecting a database by familiar brand rather than transaction and query requirements.
- Assuming PaaS eliminates schema, index, connection, partition, or capacity design.
- Using one Cosmos DB logical partition for a globally growing workload.
- Treating geo-redundant storage as point-in-time recovery from logical deletion.
- Confusing Event Grid events, Event Hubs streams, and Service Bus business messages.
- Adding multiple data stores without defining source of truth and consistency workflow.
- Designing an analytical platform without ingestion failure, lineage, security, and cost controls.

---

## 4. Design business continuity solutions (15–20%)

### Convert business impact into engineering targets

| Term | Meaning | Design implication |
|---|---|---|
| RTO | Maximum acceptable time to restore a service | Automation, warm capacity, orchestration, DNS/routing and validation time |
| RPO | Maximum acceptable data loss measured in time | Replication or backup frequency and application consistency |
| Availability target | Required successful service over a measurement period | Redundancy, dependency design, maintenance, monitoring and error budget |
| Retention | How far back recovery points/evidence must exist | Backup tiers, immutability, legal requirements and cost |
| Failure domain | Event the design must tolerate | Host, rack, zone, region, identity, network, deployment, operator or dependency |

The [Well-Architected reliability guidance](https://learn.microsoft.com/en-us/azure/well-architected/reliability/) treats reliability as a workload property. Inventory dependencies, identify critical flows, model failure modes, define health, design graceful degradation, and test recovery.

### Backup and disaster recovery

[Azure Backup](https://learn.microsoft.com/en-us/azure/backup/backup-overview) provides workload-specific protected recovery points and restore workflows. [Azure Site Recovery](https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-overview) provides replication and recovery orchestration for supported machine workloads. Database-native backup and geo features may be the correct tools for managed data services.

A backup design must specify:

- protected workload/data and consistency requirement;
- vault/service boundary, region and subscription;
- schedule, RPO, retention, tier and legal hold/immutability needs;
- encryption and administrative separation;
- soft delete/resource guard/multi-user authorization where supported;
- cross-region or cross-subscription recovery requirement;
- restore target, network, identity, DNS, application order and validation;
- routine restore-test frequency, evidence and owner.

Replication reduces recovery time for some failures but can propagate corruption, deletion, compromised credentials, or bad application writes. Backup supplies historical recovery points but restore may take longer. Many systems need both.

> **Related item:** A cyber-recovery design assumes an attacker may control production identities and automation. Isolation, immutable or protected recovery points, separate authorization, known-clean configuration, credential rotation, and recovery-environment validation matter beyond ordinary infrastructure failure.

### High availability by workload type

#### Compute

- Availability sets distribute supported VMs across fault/update domains within a datacenter-oriented design.
- Availability zones place resources across independent datacenter zones in a region.
- Virtual Machine Scale Sets manage a fleet and scaling; orchestration and application state still matter.
- App Service, Functions, Container Apps, and AKS expose different zone, scale, revision/deployment, and networking models.
- Multi-region deployment needs traffic routing, data topology, deployment consistency, capacity, and failover/failback procedures.

#### Relational data

Distinguish automatic local HA, zone redundancy, read replicas, active geo-replication, failover groups, database/server scope, and backup restore. The application connection string, DNS/endpoint, transaction semantics, and read/write behavior during failover determine whether the service-level feature produces workload recovery.

#### Semi-structured and unstructured data

Storage account redundancy, Cosmos DB region topology/consistency, file-service replication/backup, and cache persistence solve different problems. An active-active application may still have a single-region database or key store. Draw the dependency graph and find the narrowest failure boundary.

#### Region pairs and recovery ownership

[Region pairing](https://learn.microsoft.com/en-us/azure/reliability/regions-paired) does not automatically replicate a workload, provide HA or fail it over. Some services use the paired region; others support different choices. Select locations from the service's replication support, residency, capacity and latency requirements. Record recovery actions for DNS, identity, configuration, keys and deployment tooling as well as data. Microsoft-managed regional recovery is not a substitute for a workload recovery plan.

Use [failure mode analysis](https://learn.microsoft.com/en-us/azure/well-architected/reliability/failure-mode-analysis) to examine running operations and recovery operations separately. A healthy data-plane probe can coexist with a failed identity or management dependency that prevents scaling, rotating a key or redeploying. Define a useful degraded mode and evidence that it is working.

### Availability mathematics and dependency design

For independent serial dependencies, availability is approximately the product of component availabilities. Adding a required dependency can reduce end-to-end availability even when that service has a strong SLA. Parallel redundant paths can improve availability only if traffic actually fails over and shared dependencies do not fail with both paths.

Avoid multiplying published numbers mechanically when dependencies are correlated or when the application cannot use the redundancy. The useful question is: *Can the critical user flow complete during the stated failure, and has that behavior been tested?*

#### Domain failure modes

- Choosing a service feature before defining RTO, RPO, retention, and failure scope.
- Treating a backup success event as proof of application recovery.
- Deploying across zones while retaining a single-zone dependency.
- Calling a read replica a disaster-recovery plan without write failover and client behavior.
- Assuming geo-replication protects against every logical or security incident.
- Omitting DNS, identity, secrets, certificates, quotas, and third-party dependencies from recovery.
- Testing failover but not failback, data reconciliation, or operating capacity.

---

## 5. Design infrastructure solutions (30–35%)

### Compute selection

Use the [Azure compute decision guide](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree) as a structured comparison, then verify current service capabilities.

| Workload characteristic | Candidate | Customer responsibility that remains |
|---|---|---|
| OS control, legacy agent, custom appliance, unsupported runtime | Azure VMs / VM Scale Sets | Image, guest patching, hardening, availability, scaling and application operations |
| Managed web/API runtime with deployment slots | App Service | Application, plan sizing/scaling, identity, configuration, networking and observability |
| Event-driven functions and orchestrated work | Azure Functions | Trigger behavior, idempotency, timeout/scale plan, dependencies and monitoring |
| Container without full orchestrator ownership | Container Apps or Container Instances | Image, ingress, revisions/jobs, secrets, scale rules and application health |
| Kubernetes API/ecosystem and orchestration control | AKS | Cluster/workload design, node strategy, upgrades, policy, networking and observability split |
| Large parallel or scheduled jobs | Azure Batch or suitable data/compute service | Job/task model, pool/image, data staging, retry, quotas and cost |

Specify CPU architecture, memory, accelerator, ephemeral/persistent storage, network throughput, startup time, state, scale unit, deployment strategy, health probes, maintenance, availability zones/regions, and cost behavior. “Serverless” changes capacity management; it does not make state, latency, limits, retries, or observability disappear.

For Functions, separate the function execution timeout from the caller's deadline. The [hosting guidance](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale) gives an HTTP response limit of 230 seconds regardless of the configured function timeout. Queue-based or Durable Functions patterns can return an accepted-operation response and expose status. A plan without an enforced execution maximum still has platform-update and scale-in interruptions to design for. Apps using the v3 runtime on Linux Consumption stop running after September 30, 2026; migrate those apps to v4. Linux Consumption hosting retires September 30, 2028. These are distinct from Windows Consumption and from the AZ-305 exam lifecycle.

### Application architecture

#### Messaging and event-driven designs

The [Azure asynchronous messaging guide](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/messaging) separates commands from events and compares brokered patterns. Design for:

- queue versus publish/subscribe versus stream;
- delivery and ordering scope;
- duplicate detection and idempotent processing;
- poison messages, dead-letter handling and replay;
- transactions and temporal coupling;
- schema/version compatibility;
- back pressure, throttling and consumer scale;
- correlation, tracing and audit.

#### Select the Service Bus recovery feature deliberately

| Choice | State protected and design consequence |
|---|---|
| [Geo-Disaster Recovery](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-geo-dr) | Replicates namespace metadata, not queued or dead-lettered messages. Alias failover breaks the pairing. RBAC assignments and several network/security settings need separate preparation. |
| [Geo-Replication](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-geo-replication) | Premium replication includes messages and state. Currently one secondary; applications use the primary. Synchronous acknowledgment adds latency and dependency on active replicas; asynchronous replication allows a data-loss window and throttles publishing at its lag threshold. |

Geo-Replication cannot be combined with Geo-Disaster Recovery. Partitioned-namespace Geo-Replication remains public preview and large messages are unsupported in the current feature documentation. Planned promotion catches up first; forced promotion can lose or redeliver messages. Inventory access, network and downstream effects separately from namespace availability.

For current implementations, the [Service Bus settlement guidance](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-transfers-locks-settlement) identifies September 30, 2026 as the retirement of WindowsAzure.ServiceBus, Microsoft.Azure.ServiceBus and com.microsoft.azure.servicebus. Older SDKs can continue without support; SBMP itself cannot be used after the deadline. Plan supported SDK/AMQP migration and verify retry, settlement and duplicate behavior.

The [idempotent consumer pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer) requires a stable event identity and an atomic relationship between the processed marker and the business update. A correlation ID shared by several events is insufficient. A [transactional outbox](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos) addresses the producer's database/message handoff; it does not remove the consumer's need to handle repeats. Example 7 demonstrates only a local database transaction. External payment APIs require their own idempotency and reconciliation strategy.

#### API integration

API Management can provide gateway policies, authentication enforcement, transformation, throttling, caching, versioning, developer discovery, and analytics. It does not repair an unreliable or insecure backend. Decide gateway topology, network placement, regional deployment, custom domains/certificates, policy ownership, product/subscription model, backend identity, rate limits, version/revision strategy, and observability. **VERIFY CURRENT:** tiers, v2 capabilities, networking, multi-region support, limits, and retirement notices in the [API Management overview](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts).

Check the [v2 capability matrix](https://learn.microsoft.com/en-us/azure/api-management/v2-service-tiers-overview), not just a tier name. Standard v2/Premium v2 VNet integration connects to private backends; it does not by itself make the gateway, management plane or developer portal private. Premium v2 adds VNet injection for gateway isolation and zone redundancy. Current v2 tiers do not support multi-region deployment or an automated classic-to-v2 upgrade.

Classic [Premium multi-region deployment](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-deploy-multi-region) replicates gateways; management and the developer portal remain in the primary region. Compare gateway continuity, backend recovery and management availability independently. Do not confuse the classic platform's stv2 version with a v2 pricing tier.

#### Caching and configuration

Cache only when access pattern and invalidation behavior are understood. Define source of truth, key, TTL, eviction, stampede protection, consistency tolerance, warm-up, failure behavior, and sensitive-data handling. A cache-aside consumer must tolerate a miss and usually tolerate stale data within a defined bound.

Central configuration services separate deployable code from environment settings. Use managed identity and least privilege, label/version configuration, treat secrets separately, and design application behavior when the configuration service is unavailable. Feature flags need ownership, expiry, telemetry, and removal—not just a toggle.

[App Configuration geo-replication](https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-geo-replication) uses separate replica endpoints and eventual consistency. Configure a supported provider's replica discovery/failover, or implement and test equivalent client behavior. Updates can temporarily differ between regions. Design refresh, cached values and safe defaults; a feature flag should not be treated as an instantaneous global security revocation mechanism.

The [Redis retirement FAQ](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/retirement-faq) distinguishes Azure Cache for Redis Enterprise/Enterprise Flash retirement on March 31, 2027 from Basic/Standard/Premium on September 30, 2028; disablement begins the following day for each group. Assess Azure Managed Redis compatibility, region/SKU, clustering, authentication and endpoint changes. Budget for cold-cache load and data semantics; do not infer that a replacement deployment automatically carries over application state.

#### Automated deployment

Choose an infrastructure/application delivery design that provides versioned artifacts, environment promotion, policy and security gates, idempotent infrastructure as code, secretless identity where possible, staged rollout, health validation, rollback/roll-forward, and evidence. Blue-green, canary, rolling, slots, and immutable replacement have different cost, state, routing, and database-compatibility requirements.

> **Related item:** Backward- and forward-compatible database changes are often the limiting dependency in zero-downtime deployment. An application rollback is unsafe if a destructive schema migration already removed the prior version’s contract.

### Migration design

Use the [Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/) to connect business outcomes, readiness, landing zones, migration, modernization, governance, and operations. Use [Azure Migrate](https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview) and workload-specific tools for discovery, assessment, dependency analysis, business case, replication, and migration where supported.

For each workload, document:

1. inventory, owner, criticality, dependencies and unknowns;
2. utilization and right-sizing evidence rather than allocated capacity alone;
3. compatibility blockers, data volume/change rate and network throughput;
4. migration approach—rehost, replatform, refactor/rearchitect, replace, retire, retain, or relocate as appropriate;
5. landing-zone, identity, network, security, policy and operations readiness;
6. pilot/wave grouping and shared-dependency order;
7. initial sync, delta sync, freeze, cutover, validation and rollback criteria;
8. decommission, license/cost cleanup and post-migration optimization.

Database migration assessment must cover engine/version/features, collation, extensions, jobs, linked dependencies, downtime, consistency, replication/cutover, application connection behavior and rollback. Unstructured-data migration adds namespace, metadata/ACL preservation, small-file behavior, change tracking, transfer appliance/network capacity and validation checksums.

### Network solutions

#### Internet and hybrid connectivity

| Need | Design family | Distinguishing constraints |
|---|---|---|
| Public HTTP(S) global entry and acceleration | Front Door | Global edge, Layer 7 routing, WAF, origin health, TLS and caching |
| Regional HTTP(S) ingress | Application Gateway | Regional Layer 7, WAF, private/public frontend, backend/probe behavior |
| Regional TCP/UDP load distribution | Load Balancer | Layer 4, public/internal frontend, rules, probes and outbound design |
| DNS-based global routing | Traffic Manager | DNS response and endpoint monitoring; client DNS caching affects convergence |
| Encrypted site-to-site/user tunnel | VPN Gateway | Internet path, throughput/SKU, active-active/BGP choices, tunnel/device behavior |
| Private provider connectivity | ExpressRoute | Circuit/provider, peering, redundancy, routing/BGP and VPN coexistence |
| Managed hub transit at scale | Virtual WAN | Hub/routing intent, branch/VNet connectivity, security integration and cost |

The [Azure load-balancing decision guide](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview) compares scope and traffic layer. Designs often compose a global and a regional service; ensure health probes reflect meaningful application readiness and that origin access is restricted as intended.

#### Performance and network security

Optimize performance by placing services near users/data, reducing round trips, using an appropriate global entry point/CDN/cache, selecting sufficient gateway/VM/service throughput, avoiding forced-tunneling bottlenecks, and measuring the complete path. Check asymmetric routing when introducing firewalls or network virtual appliances.

Apply layered controls:

- non-overlapping address space and subnet/delegation design;
- NSGs/ASGs for stateful Layer 3/4 filtering;
- Azure Firewall or NVA for centralized inspection and egress policy where required;
- WAF for supported HTTP(S) threats;
- DDoS protections appropriate to public endpoints;
- Private Link/private endpoints for private PaaS access;
- DNS Private Resolver/forwarding and private zones for hybrid resolution;
- route tables/BGP propagation designed for both forward and return path;
- Network Watcher/flow/connectivity evidence.

A private endpoint is an interface for a service subresource. It does not by itself disable public access, grant data permission, configure every required subresource, or guarantee correct DNS. Design those gates explicitly. **VERIFY CURRENT:** service support, SKU/tier, regional/zone availability, throughput, quotas, pricing, and retirements in the [Azure networking documentation](https://learn.microsoft.com/en-us/azure/networking/).

#### Domain failure modes

- Selecting Kubernetes for packaging portability when no orchestration requirement exists.
- Treating serverless or PaaS as operationally ownerless.
- Designing at-least-once messaging without idempotent consumers and poison handling.
- Adding a gateway without defining backend identity and end-to-end observability.
- Migrating before the landing-zone identity, policy, DNS, route, quota and support model are ready.
- Using DNS-based routing while assuming immediate client convergence.
- Deploying a private endpoint without a public-access and hybrid DNS design.
- Optimizing one network leg while an inspection path or application dependency is the bottleneck.

---

### Current network migration boundaries

For API versions released after March 31, 2026, [new virtual networks default to private subnets](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access). Existing VNets are not automatically changed. Specify NAT Gateway, applicable Load Balancer outbound rules or a designed firewall/NVA egress path and verify DNS, routing and required public dependencies. A private endpoint for one service does not provide general internet egress.

[Front Door classic retires March 31, 2027](https://learn.microsoft.com/en-us/azure/frontdoor/migrate-tier). Migration to Standard/Premium requires readiness checks such as HTTPS for custom domains and compatible affinity settings. The documented flow avoids DNS changes before/during migration but requires the DNS update afterward; retain verification and rollback decision points appropriate to the actual migration stage.

---

## 6. Integrated architecture scenarios

### Scenario A — regulated regional web application

Requirements: internet-facing application, private data services, two-zone resilience, auditable access, 15-minute RPO, four-hour regional RTO, and controlled deployment.

1. Convert those statements into measurable critical flows and failure tests; confirm whether the RPO/RTO apply to all data or only transactions.
2. Use a global or regional HTTP(S) entry service based on geography, failover, WAF, and routing needs; restrict origin exposure.
3. Choose zonally capable compute and a deployment strategy with health validation. Keep state outside disposable compute.
4. Give each workload component a managed identity and only the required data-plane roles. Put human privileged access behind eligible/time-bound governance.
5. Connect data and key services privately; design public-access state, private DNS, hybrid resolution, routing and inspection as one system.
6. Select the data model from transactions and query patterns. Configure zone HA, a regional recovery topology and historical backup to meet distinct failure modes.
7. Route control, identity, resource and application signals to stores that satisfy operational and audit requirements; alert on user-flow symptoms, not only resource CPU.
8. Deploy policy and infrastructure as code through staged environments. Preserve immutable artifacts and evidence.
9. Test zone loss, regional failover, backup restore, lost secrets/keys, DNS failure, deployment rollback, and operating capacity.

No single Azure service “provides compliance.” The evidence comes from the complete identity, configuration, data, operational and review system.

### Scenario B — migrate a stateful line-of-business application

Requirements: legacy Windows application, SQL Server features, 2 TB file share, six-hour weekend outage, minimal code change now, modernization later.

1. Discover server utilization, dependencies, authentication flows, ports, batch jobs, certificates, DNS names, SQL features, file ACLs, and owners.
2. Assess SQL Database, Managed Instance, and SQL on VMs against actual compatibility and operations requirements. “Minimal change” is a constraint, not an automatic command to choose VMs.
3. Evaluate Azure Files/NetApp Files or another supported target against protocol, identity, performance, ACL, capacity, backup, and migration tooling.
4. Prepare the landing-zone connectivity, DNS, identity, policy, backup, monitoring, quotas, support ownership and cost controls.
5. Rehearse initial and delta transfer. Measure transfer/cutover time; validate data, application behavior and rollback before the weekend.
6. Group shared dependencies before application waves. Freeze changes, perform final sync, redirect endpoints, validate business transactions and observe.
7. Retain rollback until acceptance criteria and reconciliation pass. Then decommission source capacity deliberately.
8. Capture modernization candidates separately so the low-risk migration does not become an accidental permanent architecture.

---

### Worked examples — calculate before choosing a tier

All values below are invented exercise inputs. They are not Azure limits, SLA forecasts, measured capacity or proof of successful recovery. Recheck assumptions against a real workload.

#### Example 1 — serial availability and error budget

Two mandatory, statistically independent components have availability 99.9% and 99.95%. Multiplication gives `0.999 × 0.9995 = 0.9985005`, or **99.85005%**. Over a 30-day, 43,200-minute month, that model implies **64.7784 minutes** unavailable, exceeding the **43.2-minute** budget for 99.9%. Shared dependencies, correlated failures and failover time invalidate a simple independence model. Adding a second region only helps if the user flow and state can actually survive the intended failure.

#### Example 2 — skew defeats aggregate partition capacity

Assume four partitions each support **5,000 work units/s** in a fictional store. Total capacity is 20,000, but one customer key receives 80% of a 10,000-unit/s workload: **8,000 units/s**. That partition overloads even though aggregate demand is below total capacity. A better key or bounded subpartition may spread the work, but explain how reads and multi-item transactions change. Simply buying more aggregate capacity is not a complete answer.

#### Example 3 — a queue absorbs a deficit, not unlimited work

Arrival rate is 2,400 messages/s; processing is 2,000/s for 15 minutes. The backlog grows by `(2400 − 2000) × 900 = 360,000` messages. Raising processing to 3,000/s leaves **600/s** for catch-up while arrivals continue, so draining takes **600 seconds / 10 minutes**. Capacity must account for downstream throttles, retries, lock duration and poison messages. Prefetch is not proof that business processing achieves the advertised rate.

#### Example 4 — a cache failure becomes a database load event

At 2,000 requests/s and a 95% hit rate, the database receives **100 misses/s**. Immediately after a full flush, a no-hit assumption gives **2,000/s**, a **20-fold** increase. Stagger expiry, coalesce concurrent cache fills and limit fallback load where appropriate. For authorization-sensitive data, define safe invalidation and failure behavior instead of serving stale permissions indiscriminately.

#### Example 5 — migration time and ongoing change

Four TiB equals 4,194,304 MiB. At an effective 250 MiB/s, a baseline copy needs **16,777.216 seconds**, about **4h 39m 37s**. In a simplified backlog model where ongoing changes consume 50 MiB/s of that same capacity, net drain is 200 MiB/s: **20,971.52 seconds**, about **5h 49m 32s**. Add 45 minutes of sequential verification and the estimate becomes **6h 34m 32s**, beyond a six-hour window. Real convergence depends on change amplification and tool behavior. Pre-staging can move the baseline copy outside the outage; downtime is then the remaining delta, quiescence, final copy, validation and cutover, not necessarily the full transfer time.

#### Example 6 — recovery uses the critical path

Assume DNS preparation takes 15 minutes in parallel with 35 minutes of infrastructure recovery; then a 40-minute restore and 20-minute validation run sequentially. Total is `max(15, 35) + 40 + 20 = 95 minutes`, missing a 90-minute RTO. Summing everything gives 110 minutes and overstates this particular dependency graph. If the newest usable recovery point is 12:35 and the incident is at 13:00, **25 minutes** of exposure also misses a 15-minute RPO. Faster compute startup alone fixes neither gap.

#### Example 7 — duplicate delivery and a failed transaction

This standard-library Python example uses an in-memory SQLite database. A processed-event marker and an integer-cent balance change commit together. The key includes the consumer, so independent consumers can handle the same event. The event ID must be stable across retries and uniquely identify the business event; reject conflicting payloads for a reused ID in a real application.

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE inbox (
    consumer TEXT NOT NULL,
    event_id TEXT NOT NULL,
    PRIMARY KEY (consumer, event_id)
);
CREATE TABLE balances (consumer TEXT PRIMARY KEY, cents INTEGER NOT NULL);
INSERT INTO balances VALUES ('billing', 0), ('reporting', 0);
""")

def apply(consumer, event_id, cents, *, fail_before_commit=False):
    if not event_id or type(cents) is not int or cents <= 0:
        raise ValueError("A stable event ID and positive integer cents are required")
    with db:
        inserted = db.execute(
            "INSERT INTO inbox VALUES (?, ?) ON CONFLICT DO NOTHING",
            (consumer, event_id),
        ).rowcount
        if not inserted:
            return False
        changed = db.execute(
            "UPDATE balances SET cents = cents + ? WHERE consumer = ?",
            (cents, consumer),
        ).rowcount
        if changed != 1:
            raise ValueError("Unknown consumer")
        if fail_before_commit:
            raise RuntimeError("Injected failure before commit")
    return True  # Acknowledge the transport only after this commit.

def balance(consumer):
    return db.execute(
        "SELECT cents FROM balances WHERE consumer = ?", (consumer,)
    ).fetchone()[0]

assert apply("billing", "order-7", 1250)
assert balance("billing") == 1250
assert not apply("billing", "order-7", 1250)
assert balance("billing") == 1250
try:
    apply("billing", "order-8", 250, fail_before_commit=True)
except RuntimeError:
    pass
else:
    raise AssertionError("The simulated failure must occur")
assert balance("billing") == 1250
assert db.execute("SELECT COUNT(*) FROM inbox WHERE event_id = 'order-8'").fetchone()[0] == 0
assert apply("billing", "order-8", 250)
assert balance("billing") == 1500
assert apply("reporting", "order-7", 1250)
assert balance("reporting") == 1250
assert not apply("reporting", "order-7", 1250)
assert balance("billing") == 1500
```

This verifies rollback and replay in one local database. It does not test Service Bus, concurrent workers or an external payment side effect. Retain deduplication state for the supported replay window and reconcile ambiguous external outcomes. A producer outbox and a consumer inbox solve different failure boundaries.

---

## 7. Hands-on design labs

Use a disposable subscription where implementation is useful. For every lab, produce a short architecture decision record (ADR): context, requirements, options, decision, trade-offs, verification, cost considerations and open risks.

### Lab 1 — Observability architecture

1. Take a two-tier sample application and define three critical user flows and SLOs.
2. Map control-plane, resource, guest/application, identity and platform-health signals.
3. Design diagnostic routing, workspace/storage boundaries, retention and access.
4. Write two metric alerts and one log/absence-of-data alert with owners and runbooks.
5. Estimate ingestion/retention drivers and document data-reduction choices.

### Lab 2 — Identity and governance landing-zone slice

1. Draw tenant, management group, subscription, resource group, platform and workload scopes.
2. Define human and workload identities, roles, scopes, PIM/access-review lifecycle and emergency access.
3. Create a small policy initiative in audit mode, inspect impact, then plan deny/remediation rollout.
4. Model a Key Vault private-access, rotation, recovery and logging design.
5. Explain which controls prevent, detect, respond to, and recover from misconfiguration.

### Lab 3 — Data-store decision

1. Model an order system with transactions, product search, event history, documents and reporting.
2. Compare one-store and polyglot designs by access pattern, consistency, scale, recovery and operations.
3. For the chosen stores, specify partition/index, tier/compute, HA, geo, backup, identity and network decisions.
4. Introduce a tenfold growth requirement and identify what changes.
5. Introduce a regional outage and an operator deletion; show which controls address each.

### Lab 4 — Messaging proof

1. Implement or diagram order commands, state-change events and a telemetry stream with the appropriate service family.
2. Define message schema/version, correlation, ordering scope, retry and dead-letter behavior.
3. Force duplicate delivery and prove idempotent consumer behavior.
4. Force poison processing, inspect evidence and replay safely.
5. Explain why the other messaging choices fit less well.

### Lab 5 — Recovery architecture game day

1. Define workload RTO, RPO, retention, failure scopes and recovery ownership.
2. Map every critical dependency: compute, data, identity, keys, DNS, network, images, configuration and external services.
3. Design zone availability, regional recovery and historical backup separately.
4. Execute or tabletop a region loss and a compromised-production-identity scenario.
5. Record measured recovery time/point for executed work, or clearly labeled estimates for a tabletop; include manual steps, capacity gaps and corrective actions.

### Lab 6 — Compute and deployment decision

1. Compare VMs, App Service, Functions, Container Apps and AKS for a given API plus worker workload.
2. Score runtime support, scale, state, network, availability, operations, portability and cost.
3. Deploy a small version using the selected platform and a managed identity.
4. Perform a staged deployment with health validation and rollback/roll-forward criteria.
5. Add a breaking database change and redesign it for compatible deployment.

### Lab 7 — Migration wave plan

1. Inventory five fictional applications and their shared identity, database, file and network dependencies.
2. Assess readiness, utilization, compatibility, business impact and target approach.
3. Build dependency-aware waves and a migration runbook with timing.
4. Define validation and rollback decision points plus communication owners.
5. Include source decommission, license cleanup and post-migration optimization.

### Lab 8 — Hybrid network design and failure analysis

1. Design hub-spoke or Virtual WAN connectivity for two Azure regions and on-premises networks.
2. Add internet ingress, centralized egress/security, private endpoints and hybrid DNS.
3. Produce route tables for representative flows and prove symmetric return paths.
4. Compare VPN and ExpressRoute requirements, including redundancy and coexistence.
5. Fail one gateway/path and one DNS dependency; document expected detection and recovery.

---

### Lab 9 — application state during regional failure

1. Draw an order flow with API Management, Service Bus, a database, App Configuration and a cache. List data-plane and recovery dependencies.
2. Compare Geo-Disaster Recovery against Geo-Replication, including message loss, lag, RBAC, private access and promotion ownership.
3. Run example 7 locally; explain failure before commit and failure after commit but before acknowledgment. Propose retention and reconciliation rules.
4. Tabletop stale configuration, cold cache and a healthy API gateway with an unavailable backend. Calculate backlog and database fallback demand.
5. Produce an ADR with allowed data loss, client behavior, recovery evidence and a rollback decision. This design lab is not evidence of a cloud failover.

### Lab 10 — capability and lifecycle review

1. Compare classic Premium and Premium v2 API Management against inbound privacy, private backends, zones, multiple regions and management-plane recovery.
2. Inventory fictional Key Vault API versions, Redis tiers, Front Door tiers, Functions host/runtime and Service Bus SDK/protocol.
3. Attach the current primary lifecycle source to each affected item; distinguish support retirement from traffic/execution disablement.
4. Build a migration order from dependencies and test evidence. Include explicit outbound access and DNS checks after Front Door migration.
5. Use the blog exercises below to challenge the ADR. Record assumptions and unresolved questions instead of treating launch claims as current feature matrices.

---

## 8. Original knowledge checks

1. A solution meets feature requirements but violates a stated data-residency rule. Is it viable? **Answer:** No. Eliminate any option that violates a hard constraint before comparing preferences.
2. When is a central Log Analytics workspace a poor default? **Answer:** When residency, access isolation, ingestion concentration, ownership, or chargeback requirements outweigh the simplicity of centralization.
3. Does Azure RBAC authorize every action inside an application? **Answer:** No. It governs Azure resource scopes and supported data actions; application authorization remains an application design.
4. Why does managed identity improve a design? **Answer:** It avoids distributing application credentials, while still requiring explicit scoped authorization and lifecycle controls.
5. What is missing from “put secrets in Key Vault”? **Answer:** Caller identity, access scope, network/DNS, rotation, recovery, availability, logging, and protection from downstream disclosure.
6. Policy says a resource is compliant. Is the workload secure? **Answer:** Not necessarily; policy evaluates configured rules, not every application, identity, runtime, data and operational risk.
7. First input to a database choice? **Answer:** Data shape, access/query pattern, transaction boundary, scale, consistency, geography, recovery, compatibility, operations and cost—not a preferred product name.
8. Why can Cosmos DB partition-key choice become an architectural constraint? **Answer:** It controls distribution, transaction scope, query routing, hot partitions and scale behavior.
9. Does GRS protect against a deletion that validly replicates? **Answer:** Not by itself; historical protection such as versioning, soft delete or backup is needed according to the recovery requirement.
10. Event Grid, Event Hubs or Service Bus for a durable order command? **Answer:** Usually Service Bus; exact requirements for transactions, ordering, delivery and protocol decide.
11. Why should at-least-once consumers be idempotent? **Answer:** Retries or delivery behavior can present a message more than once; repeated handling must not duplicate the business effect.
12. RPO versus RTO? **Answer:** Maximum acceptable data loss in time versus maximum acceptable restoration time.
13. Does zone redundancy provide regional disaster recovery? **Answer:** No; it addresses supported failures within a region, not total regional loss.
14. Why combine replication with backup? **Answer:** Replication can reduce outage time but propagate bad changes; backup supplies historical recovery points for different failure modes.
15. What makes an SLA number insufficient for architecture? **Answer:** End-to-end flows include serial/shared dependencies, application behavior, exclusions and failover that a component SLA does not capture.
16. App Service versus AKS: what decides? **Answer:** Runtime, orchestration/API control, portability, scaling, networking, availability, skills and operational ownership—not container packaging alone.
17. Command versus event? **Answer:** A command asks a specific receiver to do something; an event states that something occurred for interested consumers.
18. Why is API Management not a backend security fix? **Answer:** A gateway can enforce edge policies, but backend identity, authorization, exposure, vulnerabilities and observability still require design.
19. What is the first migration deliverable? **Answer:** A trustworthy inventory with owners, dependencies, utilization, compatibility, criticality and unknowns.
20. Why can right-sizing from allocated VM capacity be wrong? **Answer:** Allocation does not show actual utilization, peak behavior or growth; assessment evidence should drive target capacity.
21. Front Door versus Traffic Manager? **Answer:** Front Door proxies global HTTP(S) at Layer 7; Traffic Manager returns DNS-based endpoint choices and is affected by DNS caching.
22. Private endpoint created: is public access disabled? **Answer:** Not automatically; public access, private DNS, routes, permissions and required subresources remain separate decisions.
23. Why can forced tunneling cause performance or availability problems? **Answer:** Central inspection paths can bottleneck, add latency, create asymmetric routing or become shared failure points.
24. What belongs in an ADR? **Answer:** Context, requirements, considered options, decision, trade-offs/consequences, evidence, verification and unresolved risks.

---

25. Does moving an alert table to Auxiliary preserve alerting? **Answer:** No. Check the current table-plan capability matrix, including alert type, query costs and replication; Auxiliary/Lake does not support alerts.
26. Does updating an existing vault with API 2026-02-01 switch it to RBAC? **Answer:** No. The new-vault default and explicit migration of existing authorization are separate.
27. Can a Key Vault object backup be restored into any subscription? **Answer:** No. The documented restore boundary is the same Azure subscription and geography.
28. Does a SQL failover-group listener recover the entire application? **Answer:** No. It redirects database connections; clients, identity, DNS, compute and other state still need recovery.
29. Does an Azure region pair supply an application failover plan? **Answer:** No. Service-specific replication and workload recovery must be designed and tested.
30. Can a green data-plane probe hide a recovery dependency failure? **Answer:** Yes. Existing requests may work while identity or control-plane failures prevent scaling or redeployment.
31. Are 99.9% and 99.95% serial independent components sufficient for a modeled 99.9% flow? **Answer:** No. Their product is 99.85005%; real shared failures need additional analysis.
32. Can an overloaded partition coexist with spare aggregate capacity? **Answer:** Yes. A hot key can saturate one partition; revisit key distribution and transaction/query requirements.
33. A queue receives 2,400/s and processes 2,000/s for 15 minutes. Backlog? **Answer:** 360,000 messages. At 3,000/s processing with arrivals continuing, catch-up takes another ten minutes.
34. Does Service Bus Geo-Disaster Recovery replicate queued messages? **Answer:** No. It protects metadata; message/state replication belongs to the separate Geo-Replication feature.
35. Is all Service Bus Geo-Replication functionality GA? **Answer:** No. The current document still marks partitioned-namespace support public preview; check feature-specific limits.
36. Why can asynchronous replication affect publisher availability? **Answer:** Reaching the configured replication-lag threshold can throttle publishing when the secondary cannot keep up.
37. Does a producer outbox eliminate duplicate consumer effects? **Answer:** No. Dispatch and delivery may repeat; atomically couple the consumer marker with its business update where possible.
38. Why use consumer plus event ID for a shared inbox? **Answer:** Independent consumers each need to process an event once within their own business boundary.
39. What happens if the example fails after the balance update but before commit? **Answer:** Both the balance update and inbox marker roll back, so a retry can safely apply the local transaction.
40. Does the SQLite example prove exactly-once external payments? **Answer:** No. An external API is outside the transaction; use supported idempotency and reconcile ambiguous outcomes.
41. Does increasing a Functions timeout extend the HTTP response limit? **Answer:** No. The documented 230-second response limit remains; use an asynchronous operation pattern when appropriate.
42. Does VNet integration alone make API Management v2 private inbound? **Answer:** No. Private backend connectivity and gateway inbound isolation are separate requirements and configurations.
43. Does Premium v2 imply classic Premium multi-region capability? **Answer:** No. The current v2 matrix excludes multi-region; classic Premium also keeps management and the developer portal in the primary region.
44. Are App Configuration replica writes instantly consistent worldwide? **Answer:** No. Replication is eventual; configure client failover and safe stale/default behavior.
45. At 2,000 requests/s and 95% cache hits, what happens to database load after a no-hit flush? **Answer:** It rises from 100/s to 2,000/s, or twenty-fold, under the stated assumptions.
46. Does a five-hour baseline data copy imply five hours of downtime? **Answer:** No. Pre-staging, ongoing deltas, write quiescence, validation and cutover determine the outage window.
47. What is RTO for parallel 15/35-minute tasks followed by 40-minute restore and 20-minute validation? **Answer:** 95 minutes, assuming exactly those dependencies; a 90-minute target is missed.
48. Do the new private-subnet defaults automatically change existing VNets? **Answer:** No. The change applies to new VNets through the relevant API versions; inventory actual egress configuration.

---

## 9. Readiness checklist

You are approaching readiness when you can:

- turn a long scenario into functional and nonfunctional constraints before choosing services;
- use all five Well-Architected pillars and explain cross-pillar trade-offs;
- design signal collection, routing, retention, workspace access, alerts, ownership and response;
- separate authentication, Conditional Access, Entra roles, Azure RBAC and application authorization;
- design hierarchy, policy, compliance remediation, identity governance and key/secret lifecycle;
- select relational, document, object/file, cache, search and analytical stores from access patterns;
- specify partitioning, tier, consistency, HA, geo, backup and integration behavior;
- distinguish commands, events, streams, batch integration and change propagation;
- derive availability, RTO, RPO and retention controls from failure modes and prove recovery;
- compare VM, web PaaS, serverless, managed containers, Kubernetes and batch options;
- design messaging, APIs, caching, configuration and compatible automated deployment;
- build a dependency-aware migration assessment, wave, cutover, validation and rollback plan;
- select ingress, load balancing, hybrid connectivity, routing, DNS and network-security controls;
- explain every lab decision and why plausible alternatives fail a stated constraint;
- answer the original checks by reasoning, not recognizing memorized phrases.

### Primary references

- [Official AZ-305 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305)
- [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)
- [Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/)
- [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/)
- [Azure Monitor documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/)
- [Azure data-model decision guidance](https://learn.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/understand-data-store-models)
- [Well-Architected reliability guidance](https://learn.microsoft.com/en-us/azure/well-architected/reliability/)
- [Azure compute decision guide](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree)
- [Azure asynchronous messaging guide](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/messaging)
- [Azure load-balancing decision guide](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview)

---

## Places to learn

This is a curated starting set, not a complete list. Do **not** consume every resource. Pick one structured spine, use documentation and architecture case studies for weak objectives, complete design/lab work, and add one assessment source. Time estimates are planning ranges, not guarantees; playback speed, prior Azure experience, exercises, lab cleanup, and vendor changes matter. Verify the current blueprint before buying or starting a course.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Microsoft Learn AZ-305 course](https://learn.microsoft.com/en-us/training/courses/az-305t00) | Free self-directed content; instructor delivery varies | Published: 4 instructor-led days; plan 20–30 hours reading or 30–45 with case studies/labs | Best official objective-aligned spine; assumes administration experience |
| [Microsoft free Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/?practice-assessment-type=certification) | Free account | Plan 45–90 minutes including review | Baseline and gap finding; not a substitute for design practice |
| [John Savill AZ-305 Study Cram](https://www.youtube.com/watch?v=vq9LuCM4YP4) | Free | Historical estimate: about 4 hours, not reverified from the accessible video shell; plan 5–7 hours with pauses and current-objective checks | High-density review after primary study; recording predates the 2026 baseline |
| [John Savill AZ-305 whiteboard](https://github.com/johnthebrit/CertificationMaterials/blob/main/whiteboards/AZ-305-Whiteboard.png) | Free public GitHub resource | Plan 1–2 hours to annotate and reproduce from memory | Visual recall companion to the study cram; reconcile labels with current docs |
| [Pluralsight AZ-305 certification path](https://www.pluralsight.com/paths/az-305-designing-microsoft-azure-infrastructure-solutions) | Paid/trial or organization access | Public header: 18 hours; five courses total 13h 48m and three labs 4h 15m (18h 03m combined); plan 24–35 hours with review | 2024–2025 courses with 2026 labs; latest listed lab September 18. Compare older course coverage with current docs |
| [O'Reilly/ACI Learning AZ-305 course](https://www.oreilly.com/videos/designing-microsoft-azure/9781836200659/) | Paid subscription | Indexed provider metadata: May 2024, 18h 46m; direct retrieval blocked; plan 24–32 hours with design notes | Detailed video alternative; verify older terminology and changed bullets |
| [O'Reilly Exam Ref AZ-305](https://www.oreilly.com/library/view/exam-ref-az-305/9780137878758/) | Paid subscription/book | Indexed provider metadata: November 2022, 192 pages / reading estimate 5h 32m; direct retrieval blocked; plan 8–14 hours | Compact objective reference; 2022 edition must be paired with current blueprint/docs |
| [Udemy AZ-305 course by Christopher Nett](https://www.udemy.com/course/az-305-microsoft-azure-solutions-architect-expert-i/) | Paid; frequent discounts | Public provider page via browser: January 2026, 13 sections, 164 lectures, 16h 51m; direct fetch blocked; plan 22–32 hours | Compact video option predating the April baseline; paid lessons and complete coverage not audited |
| [Whizlabs AZ-305 preparation resources](https://www.whizlabs.com/blog/microsoft-azure-az-305-exam/) | Public overview; linked course/labs/tests are paid | Plan 12–25 hours when selecting videos, labs and practice tests | Targeted lab and assessment supplement; verify bundle quantities/current objective mapping |
| [MeasureUp AZ-305 practice test](https://www.measureup.com/microsoft-practice-test-az-305-designing-microsoft-azure-infrastructure-solutions.html) | Paid; free demo available | Plan 3–6 hours across timed attempt and explanation review | Product now lists 164 questions and September 2026 update; paid questions, explanations and complete objective alignment not audited |

Practice products should contain independently authored questions and explanations, not recalled live-exam content. Use results by objective domain, revisit primary documentation and design labs, then retest with unseen questions.

### Blog reading with an architecture deliverable

| Reading | Why it helps | Exercise and boundary |
|---|---|---|
| [Proactive reliability: fault types in Azure](https://techcommunity.microsoft.com/blog/azurearchitectureblog/proactive-reliability-series-%E2%80%94-article-1-fault-types-in-azure/4507006) — Zoran Jovanovic, April 1, 2026 | Broadens analysis beyond a total regional outage | Write a fault matrix for request serving, scaling and recovery when only identity or management is unavailable. The author explicitly writes personally, without Microsoft endorsement. Treat the taxonomy as commentary; do not use its qualitative likelihood labels as measured probabilities. Current Well-Architected failure-mode guidance controls. |
| [API Management Premium v2 GA](https://techcommunity.microsoft.com/blog/integrationsonazureblog/announcing-the-general-availability-ga-of-the-premium-v2-tier-of-azure-api-manag/4471499) — Sreekanth Thirthala, November 19, 2025 | Introduces gateway isolation and zone design choices | Produce separate inbound-gateway, outbound-backend and recovery diagrams. Check today's v2 matrix for missing classic features; the launch region list and broad marketing descriptions are not current coverage guarantees. |
| [Service Bus Premium Geo-Replication GA](https://techcommunity.microsoft.com/blog/messagingonazureblog/announcing-general-availability-of-geo-replication-for-azure-service-bus-premium/4413164) — Eldert Grootenboer, December 17, 2025 | Explains data/state replication and acknowledgment trade-offs | Compare synchronous and asynchronous operation during a slow secondary, then planned and forced promotion. Specify what an acknowledgment proves, tolerated data loss and replay handling. Current product documentation controls preview and large-message restrictions. |

Blog reading was limited to the recorded sections in the review report. No paid lessons or live-exam questions were used. Use the articles to challenge an ADR, then verify exact support and migration steps in primary documentation.
