---
exam_code: DP-300
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# DP-300 Administering Microsoft Azure SQL Solutions Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#dp-300-coverage-record). The [official DP-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300) is authoritative.

**Current baseline:** Skills measured as of April 24, 2026.<br>
**Upcoming blueprint change:** None announced as of August 31, 2026.<br>
**Lifecycle status:** Active; no retirement or replacement was announced on the official pages checked.<br>
**Exam page:** [Azure Database Administrator Associate](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/) · 100-minute assessment · annual renewal for the earned role-based certification.<br>
**Official course:** [DP-300T00 Implement scalable database solutions using Azure SQL](https://learn.microsoft.com/en-us/training/courses/dp-300t00) · four instructor-led days.<br>
**Practice:** A free Microsoft Practice Assessment is linked from the credential and study-guide pages.

## How to use this guide

DP-300 is an operational database exam. For every objective, be able to move through this chain:

```text
requirement -> deployment target -> configuration -> observed state
identity -> authentication -> authorization -> data operation
workload -> query -> plan -> waits/resources -> correction -> regression proof
RPO/RTO -> protection mechanism -> failover/restore -> application validation
desired state -> automation identity -> execution -> alert -> idempotent recovery
```

Do not reduce Azure SQL to a list of portal blades. Practice the same task through T-SQL and at least one deployment/automation interface where the objective names it. Record prerequisites, scope, identity, command or template, observable result, failure evidence, rollback, and cost. Azure SQL Database, Managed Instance, SQL Server VMs, networking, backup retention, geo-replicas, database watcher data stores, and supporting services can incur cost.

> **About related items:** A `Related item:` callout adds prerequisite, architectural, migration, security, operational, or adjacent context that makes the objective easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in Microsoft's published exam objectives.

## Objective map

| Published domain | Weight | Administrator question |
|---|---:|---|
| Plan and implement data platform resources | 15–20% | Can you select, deploy, size, partition, migrate, and patch the right Azure/hybrid SQL platform? |
| Implement a secure environment | 20–25% | Can the intended identity reach only permitted data through a protected network and encryption/key boundary, with auditable controls? |
| Monitor, configure, and optimize database resources | 20–25% | Can you establish a baseline, isolate the limiting resource or query behavior, correct it safely, and prove no regression? |
| Configure and manage automation of tasks | 15–20% | Can recurring work and resource deployment run under controlled identities, schedules, alerts, and repeatable definitions? |
| Plan and configure a high availability and disaster recovery environment | 20–25% | Can you derive HA, backup, replication, failover, and recovery tests from application RPO/RTO and dependency requirements? |

---

## 1. Build an Azure SQL operating model

### Separate platform responsibility from database responsibility

| Layer | Azure SQL Database | Azure SQL Managed Instance | SQL Server on Azure VM / hybrid SQL Server |
|---|---|---|---|
| OS and engine patching | Microsoft-managed | Microsoft-managed | Customer-managed; automate and stage safely |
| Instance surface | Database/logical-server oriented; some instance features differ | High SQL Server instance compatibility in a managed VNet service | Full supported SQL Server/OS control |
| Backup service | Automated PITR/LTR capabilities | Automated PITR/LTR plus supported native operations | Customer designs native/Azure Backup or other protection |
| HA inside service/host scope | Built into service tier/architecture | Built into service tier/architecture | Customer configures VM/platform and SQL HA |
| Scaling unit | database, elastic pool, serverless/Hyperscale choices | managed instance, instance pool where supported | VM, disks, SQL instance, and database |
| Administration | Database plus logical server and Azure resource | Instance/database plus Azure resource | OS, storage, network, engine, instance, database, and Azure resource |

PaaS does not remove database administration. Microsoft operates more infrastructure, but you still own target selection, data model, principals and permissions, firewall/private access, keys where customer-managed, classification/audit, performance, automation, retention, geo-configuration, application retry behavior, and recovery validation.

### Distinguish control, data, and observability paths

- **Azure control plane:** resource creation, scaling, firewall/private endpoints, diagnostic settings, backup retention, failover operations, RBAC, policy, locks, and activity logs.
- **SQL data plane:** TDS connection, authentication, database/instance principals, T-SQL authorization, transactions, queries, Query Store, DMVs, Extended Events, SQL Agent, and backup/restore commands where supported.
- **Supporting data path:** DNS, private/public endpoint, routes/firewalls, proxy/redirect connection policy, client driver, TLS, connection pool, retries, and application transaction.
- **Observability path:** metrics/logs/events/query telemetry -> collector/destination -> query/dashboard -> alert -> action/owner.

An Azure deployment can succeed while TDS connections fail. A login can authenticate but lack database access. An alert can be healthy while its data collection is absent. Prove each boundary independently.

### Use a safe change sequence

1. State the workload transaction, service-level objective, security boundary, RPO/RTO, and cost constraint.
2. Inventory target type, tier, region/zone, engine/version/compatibility, network, identity, dependencies, and current load.
3. Capture baseline queries, plans, waits, resource metrics, backup/replica health, and configuration.
4. Test in a representative environment with production-like data distribution and concurrency.
5. Use a small deployment ring or reversible operation where supported.
6. Monitor engine, Azure resource, and application signals during the change.
7. Validate the original transaction and negative security tests.
8. Record effective state and retain rollback/recovery evidence.

> **Related item:** Availability, performance, recoverability, and data integrity can conflict. For example, asynchronous geo-replication lowers write latency across distance but permits an RPO greater than zero; synchronous replicas reduce that exposure but add latency and distance constraints. Start with requirements, not a favorite feature.

---

## 2. Plan and implement data platform resources (15–20%)

### Choose the database offering from workload constraints

| Requirement | Strong candidate | Verify before selection |
|---|---|---|
| Cloud-native app, database-scoped isolation, minimal administration | Azure SQL Database single database | feature compatibility, tier, max size, connection behavior, cross-database needs |
| Many databases with variable/noncoincident usage | Azure SQL Database elastic pool | aggregate eDTU/vCore/storage limits, noisy-neighbor behavior, per-database min/max |
| Intermittent single-database workload | Azure SQL Database serverless where supported | auto-pause/resume latency, min/max vCores, memory/cache behavior, billing and feature limits |
| Very large/rapidly scaling database or read-scale needs | Azure SQL Database Hyperscale | storage/compute/replica architecture, backup/restore behavior, tier transition limits |
| Instance-scoped features and high SQL Server compatibility without OS ownership | Azure SQL Managed Instance | subnet/address capacity, connectivity, instance/database feature differences, maintenance/cost |
| Full OS/engine/agent/third-party control or unsupported PaaS feature | SQL Server on Azure VM | VM/disk/network design, patching, backup, HA, licensing and operations |
| Existing on-premises/multicloud SQL with Azure governance/security/assessment | SQL Server enabled by Azure Arc | Connected Machine and Azure extension requirements, permissions, connectivity, service cost |
| Managed SQL engine on customer/edge Kubernetes | Azure Arc-enabled SQL Managed Instance | data-controller/Kubernetes/storage prerequisites and supported release/connectivity mode |
| Transactional application tightly integrated with Fabric/OneLake analytics | SQL database in Microsoft Fabric | Fabric capacity, workspace/item permissions, Entra-only access, feature/network limits |

[Azure SQL service documentation](https://learn.microsoft.com/en-us/azure/azure-sql/) should be the selection starting point. SQL Server enabled by Azure Arc and Azure Arc-enabled data services are different products: the first projects existing SQL Server instances into Azure management; the second deploys managed data services on Arc-enabled Kubernetes.

SQL database in Fabric uses the Azure SQL Database engine for an operational database within Fabric and automatically exposes replicated analytics-ready data in OneLake. It is not simply an Azure SQL Database moved into a workspace. Include Fabric capacity, workspace/item permissions, Entra authentication, analytics endpoint behavior, source control/deployment, network availability, and portability in the decision. See the current [SQL database in Fabric overview](https://learn.microsoft.com/en-us/fabric/database/sql/overview).

**VERIFY CURRENT:** tiers, hardware generations, region/zone availability, service limits, serverless/Hyperscale behavior, Fabric capabilities, Arc releases, maintenance windows, reservations and licensing change. Recheck the target-specific limits and pricing before design or purchase.

### Plan automated deployment

Use portal deployment to learn properties, then create repeatable definitions with ARM/Bicep, Azure CLI, Azure PowerShell, REST, Terraform, or approved platform tooling. The blueprint explicitly requires ARM/Bicep, PowerShell, and CLI automation knowledge later; treat first deployment as the beginning of lifecycle management.

A complete definition includes more than the database:

- subscription, resource group, region, tags, naming, locks, policy and deployment identity;
- logical server/managed instance/VM/Fabric workspace and the database/instance settings;
- tier, compute, storage, zone redundancy, backup redundancy/retention and maintenance settings;
- Entra administrator or supported identity configuration;
- public access/firewall or private endpoint, DNS zone/link, VNet/subnet/delegation/NSG/route;
- auditing, diagnostic/monitoring destination, Defender option, alerts and action ownership;
- keys, managed identities and Key Vault permissions where customer-managed encryption is required;
- HA/DR counterpart, replication/failover policy and application endpoints where required.

Prefer declarative, parameterized, version-controlled, idempotent deployments. A successful ARM deployment proves resource-provider state reached the declared configuration; it does not prove a client can resolve DNS, authenticate, execute a transaction, meet latency, or restore data.

### Configure scale and performance by platform

#### Azure SQL Database

Understand DTU versus vCore purchasing models, provisioned versus serverless compute, single database versus elastic pool, General Purpose/Business Critical/Hyperscale purposes, storage limits, read scale, zone redundancy, and backup-storage redundancy. Select from measured CPU, data/log I/O, memory, storage growth, concurrency, latency, HA, recovery, and cost—not database size alone.

Scaling is usually online but can move data or replicas and cause brief connection interruptions. Applications need transient-fault retry with bounded backoff and idempotent transaction handling. An elastic pool saves cost only when combined usage and per-database limits fit; a constantly saturated member can harm the pool.

#### Azure SQL Managed Instance

Plan service tier/hardware, vCores, storage, subnet/address capacity, zone redundancy where available, maintenance, licensing, and connectivity. Instance creation and some scaling/network operations can take substantial time. Validate instance-level dependencies, SQL Agent, cross-database queries, linked-server/distributed-transaction needs, and source feature compatibility.

#### SQL Server on Azure VMs

Coordinate VM series/vCPU/memory with SQL edition/licensing and storage. Separate data, log, `tempdb`, and backup workloads when their I/O patterns require it; choose managed disk type/size/count, caching, striping and allocation unit intentionally. Verify aggregate VM and disk IOPS/throughput limits—the smallest limiting layer wins. Register/manage with the SQL IaaS Agent extension where applicable, then plan Automated Patching or another controlled patch process, Automated Backup or another protection process, and maintenance/restart coordination.

### Partition, compress, and shard deliberately

**Table partitioning** divides a table/index into partitions by a partition function and scheme. It supports manageability and partition elimination only when queries filter on the partitioning key in a usable way. Align related indexes where switching is required. Boundary choice, data skew, statistics and too many partitions affect performance. Partitioning does not distribute one database across multiple servers.

**Data compression** reduces pages and I/O at CPU cost. Row compression reduces storage representation overhead; page compression adds prefix/dictionary techniques; columnstore has its own compression behavior. Estimate savings, test CPU/log/maintenance effects and rebuild only with space/log capacity. Backup compression and network compression solve different problems.

**Sharding** distributes rows/databases across multiple database units using a shard key and routing/catalog strategy. It can scale beyond one database and isolate tenants, but creates cross-shard query, transaction, schema deployment, rebalancing, hotspot, monitoring, backup and recovery complexity. Elastic pools do not automatically shard data; table partitioning remains inside one database.

> **Related item:** Read scale, partitioning, sharding, caching and replicas solve different bottlenecks. A query blocked on a write lock will not be fixed by adding storage; a skewed shard key will not be fixed by partition elimination; a read replica does not accept the primary write workload.

### Plan hybrid SQL and patching

For SQL Server VMs/on-premises, inventory OS, SQL version/edition/build, features, drivers, agents/jobs, linked servers, credentials, certificates/keys, databases, HA, backup, monitoring, storage, network and maintenance dependencies. Define supported upgrade paths, cumulative update policy, GDR/CU choice, staging rings, prechecks, backup/recovery point, failover or downtime, restart sequence, health gates and rollback.

For SQL Server enabled by Azure Arc, distinguish resource projection and extension health from the SQL instance itself. Arc can enable inventory, assessment, Defender, best-practices assessment, licensing/ESU and other Azure services according to current support. It does not transfer engine ownership to Microsoft or make a failed workload healthy.

For Arc-enabled SQL Managed Instance, plan the Kubernetes/data-controller/custom-location/storage/connectivity architecture and supported version path. Use [Azure Arc-enabled data-services planning](https://learn.microsoft.com/en-us/azure/azure-arc/data/plan-azure-arc-data-services) and release notes; do not infer Azure SQL Managed Instance capabilities apply identically.

### Evaluate and implement migration

Treat migration as workload change, not file movement.

#### Discover and assess

1. Inventory instances, databases, size/growth, compatibility level, features, dependencies, jobs/logins, keys/certificates, linked servers, SSIS/SSRS/SSAS, application owners and traffic.
2. Capture representative performance and concurrency to size the target.
3. Run compatibility/readiness assessment for each candidate target and classify blocker, warning, remediation, owner and retest.
4. Select target from required features and operating model before selecting a migration tool.
5. Define data/schema/object scope and separately migrate server-level objects and external dependencies.

Current Microsoft paths include the [SSMS migration component](https://learn.microsoft.com/en-us/ssms/migrate/migrate-sql-server-azure-sql), Azure Arc readiness assessment, Azure Migrate, [Azure Database Migration Service](https://learn.microsoft.com/en-us/azure/dms/dms-overview), native backup/restore, Managed Instance link, transactional replication, BACPAC/SqlPackage, and workload-specific methods. Support varies by source, target, online/offline mode, authentication, networking, encryption and region.

> **LEGACY/RETIRED:** Azure Data Studio retired February 28, 2026 and no longer receives updates or security fixes. Use supported current experiences such as SSMS migration capabilities, Azure DMS/portal, or Visual Studio Code with the MSSQL extension as applicable. Older courses may still show the Azure SQL migration extension in Azure Data Studio; reconcile those steps with [Microsoft's retirement guidance](https://learn.microsoft.com/en-us/sql/tools/whats-happening-azure-data-studio?view=sql-server-ver17).

#### Choose online versus offline

| Mode | Strength | Cost/risk |
|---|---|---|
| Offline | Simpler consistency boundary; source stops, then data moves/restores | Downtime includes final backup/export, transfer, restore/import, validation and cutover |
| Online | Source remains available while changes replicate; cutover downtime can be short | More prerequisites, continuous sync health, lag, source change control, and precise cutover/fallback |

Base the choice on allowed downtime, data change rate, network throughput/latency, log retention, source/target support, object scope and rollback. “Online” still needs a write freeze, final synchronization, connection change and acceptance window.

#### Execute and validate

1. Provision and secure the target; test DNS/network, identities, keys and capacity.
2. Migrate schema and server-level dependencies in the correct order.
3. Seed/copy data and monitor throughput, errors, log growth, lag and resource pressure.
4. Rehearse cutover and rollback with application owners.
5. Freeze or redirect writes, complete synchronization, switch endpoints/configuration and restart pools safely.
6. Compare row counts/checksums or domain reconciliation, schema, principals/permissions, jobs, query results, latency and business transactions.
7. Establish target backup, monitoring, maintenance, security and HA/DR before acceptance.
8. Retain the source under a controlled rollback/decommission policy.

Azure SQL Managed Instance online copy/move maintains near-real-time replication until completion. A move removes the source at completion and starts a new backup chain on the destination; a copy leaves independent databases. Review current prerequisites and the 24-hour completion window in [copy or move a Managed Instance database](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/database-copy-move-how-to?view=azuresql).

#### Migration failure patterns

| Symptom | Avoid conclusion | Inspect first |
|---|---|---|
| Assessment says ready | production will work | data distribution/load, drivers, network, identity, jobs and external dependencies |
| Online migration lag grows | tool is broken | source log/change rate, backup chain, throughput, target write capacity, agent/service health |
| Database is online | migration complete | logins/users, permissions, jobs, keys, synonyms/linked resources, application transaction |
| Queries regress | Azure SQL is slower | compatibility level, plans/Query Store, statistics, cardinality, tier/storage, latency/concurrency |
| Cutover fails | immediately delete target | preserve source/target/replication state; apply rehearsed rollback decision |

#### Primary references

- [Azure SQL documentation](https://learn.microsoft.com/en-us/azure/azure-sql/)
- [Azure SQL Managed Instance overview](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview?view=azuresql)
- [SQL database in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/database/sql/overview)
- [Migrate to Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/migration-guides/?view=azuresql)
- [SQL Server to Azure SQL Database migration overview](https://learn.microsoft.com/en-us/data-migration/sql-server/database/overview)
- [Table and index partitioning](https://learn.microsoft.com/en-us/sql/relational-databases/partitions/partitioned-tables-and-indexes?view=sql-server-ver17)
- [Data compression](https://learn.microsoft.com/en-us/sql/relational-databases/data-compression/data-compression?view=sql-server-ver17)

---

## 3. Implement a secure environment (20–25%)

### Trace identity through two authorization planes

Azure RBAC authorizes management of Azure resources; SQL permissions authorize data-plane operations. Contributor on a logical server does not automatically grant `SELECT` inside a database, and a database user does not automatically gain portal control-plane access.

Trace:

```text
identity source
  -> client authentication method/token or login
  -> logical server/instance endpoint and network path
  -> server login or contained database user
  -> database user/group/role
  -> GRANT/DENY/ownership/module execution context
  -> row/column/object result
```

#### Configure Microsoft Entra authentication

- Establish the supported Entra administrator or server identity prerequisite for the target.
- Prefer groups or managed identities/service principals over individual assignments and stored passwords.
- Create contained users from external provider/identity or supported Entra server principals as the platform requires.
- Grant minimum database roles/object permissions; avoid treating `db_owner` as a connection fix.
- Configure the client driver/tool for the intended Entra method and token audience.
- For applications, test managed-identity token acquisition, connection pooling and failover behavior.

For SQL Server on Azure VM/on-premises, distinguish Windows authentication, SQL authentication and supported Entra authentication configuration. Domain reachability, SPNs, Kerberos delegation, certificates, Entra application/server identities and SQL build/platform support are separate dependencies.

#### Model SQL authorization

Server principals/logins authenticate to an instance; database users map identities into a database. Contained database users reduce instance-level mapping and improve database mobility where supported. Roles collect permissions. Ownership chains and module signing/execution context can allow access without direct permission, while `DENY` normally overrides a `GRANT` at the same hierarchy subject to ownership/sysadmin behavior.

Use schemas as permission boundaries. Grant `SELECT`, `EXECUTE` or other required rights at the narrowest maintainable scope. Separate deployment/migration identity, runtime application identity, operator, auditor, security administrator and break-glass access. Regularly enumerate effective permissions and orphaned users.

Authentication troubleshooting order:

1. endpoint/DNS/TCP/TLS and target database;
2. token/login method, tenant/domain and client driver;
3. server/Entra administrator and principal existence;
4. login-to-user mapping/default database;
5. group/token propagation and conditional/security policy;
6. database role, explicit grant/deny, schema/object ownership and execution context;
7. row-level predicate, masking/client behavior and application query.

### Protect network and transport

Azure SQL Database logical-server firewall rules and database-level firewall rules permit public endpoint sources; they do not grant SQL authentication or permissions. “Allow Azure services and resources to access this server” is broad and should not be confused with a specific service identity.

Virtual network service endpoints keep the Azure SQL public endpoint model while allowing VNet rules and optimized Azure backbone routing from an enabled subnet. Private endpoints place a private IP NIC for the service in a VNet through Private Link. Private endpoint creation does not automatically disable public network access.

For Private Link, verify:

- endpoint approval/state and correct target subresource;
- private DNS zone and VNet links, on-premises conditional forwarding, and client answer;
- routes, NSGs/firewalls, proxy/connection policy and return path;
- public network access/firewall posture;
- client uses the canonical server name so TLS certificate validation and routing work.

SQL Managed Instance has native VNet placement and distinct subnet, NSG/route, private/public endpoint and connectivity architecture. SQL Server VMs require VNet/NSG/load-balancer or listener plus guest firewall and SQL listener configuration. Do not transfer logical-server firewall rules to these architectures by analogy.

TLS protects data in transit between client and endpoint. Enforce supported minimum TLS/certificate validation and current drivers; TLS does not encrypt data at rest or prevent an authorized query from reading plaintext.

### Choose the correct encryption boundary

| Control | Protects | Key/visibility boundary | Does not do |
|---|---|---|---|
| TDE | database/log/backup files at rest | engine decrypts pages; service-managed or supported customer-managed protector | hide query results from DBA/engine; replace permissions |
| Object-level SQL encryption | selected values/modules using SQL key hierarchy/functions | engine performs encryption/decryption under granted key/certificate permissions | transparently protect an unchanged application |
| Always Encrypted | selected columns from server/DBA visibility | capable client driver holds/accesses column master key and encrypts/decrypts | support every expression or eliminate key/client operations |
| Always Encrypted with secure enclaves | richer operations and in-place crypto inside protected enclave | supported enclave, keys, client driver and optional/recommended attestation model | make every enclave technology/threat model identical |
| TLS | client-server traffic | endpoint certificate and client validation | protect stored files or authorized query output |

For TDE with customer-managed keys, include managed identity, Key Vault key/version, permissions/RBAC, soft delete/purge protection, network access, rotation, geo-secondary/restore availability, alerting and break-glass recovery. Disabling or deleting the required key can make databases inaccessible; never test key removal casually.

Always Encrypted has a column master key (key-protecting key, normally outside the database) and column encryption keys stored as encrypted metadata. Deterministic encryption enables equality-style operations but reveals equality patterns; randomized encryption provides stronger pattern protection with fewer operations unless a secure enclave enables supported richer queries. The application driver must be Always Encrypted-aware.

Use the current [Always Encrypted overview](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver17) and [secure-enclave guidance](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves?view=sql-server-ver17). Supported enclaves, regions, drivers, attestation modes and query operators change.

### Apply compliance controls without confusing their guarantees

#### Classification and auditing

Classification labels sensitive columns and supports discovery/governance workflows; it does not enforce access by itself. Establish taxonomy, owner, scanning/review, false-positive process and downstream handling.

SQL auditing records configured event/action groups to a target such as Azure Storage, Log Analytics or Event Hubs depending on platform. Define who can change audit policy or delete/read evidence, retention/immutability, network access, storage failure behavior, alerting and cost. Generate a known event and query the destination. Azure Activity Log records control-plane activity; it does not replace SQL audit.

#### Change tracking and change data capture

The blueprint says “change data tracking,” so distinguish:

- **Change Tracking:** records that rows changed and version metadata; consumers retrieve current rows and track synchronization versions.
- **Change Data Capture (CDC):** captures historical insert/update/delete change data in change tables/functions according to platform support.

Neither is a security audit or immutable ledger. Retention/cleanup, primary keys, consumer checkpoints, schema change and workload overhead need design.

#### Dynamic data masking

DDM changes query presentation for users without `UNMASK`; it does not encrypt stored data, prevent inference, or protect users who can bypass/alter permissions. Use it as least-exposure convenience alongside permissions, row/column security and encryption—not as a high-assurance boundary.

#### Row-level security

RLS uses a security predicate function and security policy to filter or block rows based on execution context/session state. Schema-bind and permission-test the predicate, protect session-context assignment, and test `SELECT`, DML, bulk, ownership/privileged users, plan behavior and support tooling. Application users sharing one database identity require a trustworthy mapping into session context.

#### Ledger

Ledger adds cryptographic evidence to make database history tamper-evident and supports digest verification according to the ledger type/platform. It does not prevent authorized changes, replace audit/backup, or prove application input was truthful. Protect digest storage/verification and rehearse verification after restore/migration.

> **Related item:** Preventive, detective, confidentiality and evidentiary controls are different. RLS restricts rows, Always Encrypted separates plaintext from the engine, auditing records selected activity, and ledger helps detect tampering. A compliance design often needs several layers.

### Security failure patterns

| Symptom | Common layer | Evidence-led check |
|---|---|---|
| Entra token acquired but login fails | server identity/admin or database principal | token tenant/audience/identity, endpoint, Entra admin, contained user, target DB |
| Login succeeds; query denied | SQL authorization | user mapping, roles, explicit grant/deny, schema/object, execution context, RLS |
| Private endpoint exists; client resolves public address | DNS | client resolver, private zone record/link, on-prem conditional forwarder, cache |
| Public connection still works after Private Link | public endpoint remains enabled | public network access and firewall; do not assume PE disables it |
| Always Encrypted query fails | driver/key/query capability | AE-enabled current driver, CMK access, CEK metadata, encryption type, enclave/attestation |
| Audit is configured but no records found | action selection/destination | generate known event, audit state/spec, destination network/permissions/retention |
| Masked user infers values | DDM is presentation, not cryptographic isolation | reduce permission/query surface; use RLS/AE/other control based on threat |

#### Primary references

- [Secure Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/secure-database?view=azuresql)
- [Microsoft Entra service principals with Azure SQL](https://learn.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-service-principal-tutorial?view=azuresql)
- [Azure SQL Database firewall rules](https://learn.microsoft.com/en-us/azure/azure-sql/database/firewall-configure?view=azuresql)
- [Private Link for Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/private-endpoint-overview?view=azuresql)
- [Transparent data encryption](https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-tde-overview?view=azuresql)
- [SQL Database auditing](https://learn.microsoft.com/en-us/azure/azure-sql/database/auditing-overview?view=azuresql)
- [Row-level security](https://learn.microsoft.com/en-us/sql/relational-databases/security/row-level-security?view=sql-server-ver17)
- [Ledger overview](https://learn.microsoft.com/en-us/sql/relational-databases/security/ledger/ledger-overview?view=sql-server-ver17)

---

## 4. Monitor, configure, and optimize database resources (20–25%)

### Start with an operational baseline

A useful baseline captures the same workload dimension at comparable time windows:

- application transaction rate, latency percentiles, errors/timeouts and retry volume;
- CPU, worker/session pressure, memory indicators and grants;
- data/log I/O latency, IOPS, throughput, queueing, log-write rate and space;
- database/storage size, growth, `tempdb`, transaction-log use and backup/replica lag;
- waits, blocking/deadlocks, top resource-consuming queries and plan variability;
- tier/compute/storage/configuration, maintenance, deployments and business calendar;
- Azure service health, resource health, throttling/governance and platform events.

A baseline is not a single average. Retain peaks, percentiles, concurrency and workload labels. Compare like for like: changing compatibility level, hardware/tier, data volume or query mix can invalidate the comparison.

### Choose the signal source

| Source | Best question | Boundary |
|---|---|---|
| Azure Monitor metrics | Is the Azure resource approaching compute, storage, connection or service limits over time? | Aggregated platform metrics; limited query detail |
| Diagnostic/resource logs | What control/service/security events were emitted and routed? | Must enable correct categories/destination; cost/retention apply |
| Database watcher | What near-real-time fleet-level Azure SQL database/MI performance datasets show the issue? | Requires watcher, target connectivity/auth, data store, permissions and current regional support |
| DMVs | What is happening in engine memory now/recently? | Often reset on restart/failover; scope/permissions/platform differences |
| Query Store | Which query/plan/runtime/wait history regressed? | Capture mode, storage quota, cleanup and aggregation determine evidence |
| Extended Events | Which precisely filtered engine events/actions prove the behavior? | Poor filtering/target sizing can add overhead or lose events |
| Execution plan | Why did the optimizer choose these operators/estimates/access paths? | Estimated differs from actual; one plan may not represent all parameters/load |
| SQL Agent/elastic-job history | Did scheduled work execute and what did each step/target return? | History retention and alert delivery must be configured |
| Application telemetry | Did the user transaction meet its objective and which dependency consumed time? | Requires correlation IDs and instrumentation outside SQL |

Use [Azure SQL monitoring and tuning](https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-tuning-index?view=azuresql) as the current navigation source.

### Configure database watcher

Database watcher is a managed monitoring capability for Azure SQL Database and SQL Managed Instance that queries SQL system views and sends datasets to Azure Data Explorer or a Real-Time Analytics database in Fabric according to current support.

Plan:

1. target scope, tenant/subscription, supported region and target tier;
2. watcher's managed identity or SQL authentication and least permissions;
3. public or managed-private-endpoint paths to SQL targets, data store and Key Vault when needed;
4. data store capacity, retention, cost, RBAC and data residency;
5. datasets, dashboards, query/alert requirements and operator ownership;
6. target overhead, collection gaps and monitoring of the watcher itself.

After deployment, generate a known workload, verify samples in the expected dataset/table, inspect dashboard/query, create an actionable alert and test its action group. A provisioned watcher without target connectivity is not monitoring.

**VERIFY CURRENT:** Microsoft's documentation still labels some database-watcher pages or datasets preview even while the DP-300 objective explicitly names the service. Supported regions, target types, data stores, datasets, private connectivity and alert templates change. Start with the [database watcher overview](https://learn.microsoft.com/en-us/azure/azure-sql/database-watcher-overview?view=azuresql).

### Use Extended Events with narrow intent

An Extended Events session defines events, optional actions, predicates, targets and retention/dispatch behavior. Use the least event volume that answers the question. Common questions include deadlocks, long statements, errors, waits or query execution details.

1. Write the symptom and exact fields needed.
2. Select events and add actions such as database/session/query identifiers only when useful.
3. Filter by database, duration, error or query context before capture.
4. Choose ring buffer for small transient inspection or event file for durable volume as supported.
5. Set size/rollover/retention and start state.
6. Reproduce the workload and correlate timestamps/activity.
7. Stop/remove the session or document its steady-state purpose.

Do not enable broad statement-level capture across a busy server without estimating overhead and sensitive-data exposure. Protect event files and retention.

### Configure and interpret Query Store

Query Store persists query text, plans, runtime statistics and wait statistics according to engine/platform and settings. Know:

- operation mode (`READ_WRITE`, `READ_ONLY`, `OFF`) and why it may become read-only;
- capture mode and which queries are retained;
- interval length, statistics aggregation and max storage/cleanup;
- query, plan and runtime-stat identity relationships;
- plan forcing, automatic plan correction and how to unforce/rollback;
- read/write replicas and hint capabilities where supported.

Regression workflow:

1. Identify the application/query and regression time.
2. Compare before/after runtime distributions, waits and plans.
3. Determine whether data/cardinality, parameters, statistics, index, compatibility/IQP, resource tier or blocking changed.
4. If needed, force a known good plan as a controlled mitigation and monitor failures/performance.
5. Correct the root cause; remove temporary forcing when safe.

A plan that was good yesterday can be wrong after data or workload changes. Plan forcing is operational state that must be inventoried and reviewed.

### Diagnose blocking, deadlocks and waits

**Blocking** is expected when one session holds an incompatible lock needed by another; prolonged blocking is the problem. Capture head blocker, waiters, resource/database, transaction age, isolation level, open transaction, SQL text/plan, client and time. Correct transaction scope, missing/inefficient access path, isolation/concurrency design or application behavior. Killing a session causes rollback and may move the symptom.

**Deadlock** is a cycle in which SQL Server chooses a victim. Capture the deadlock graph, identify resource/access order and transaction context, then enforce consistent access order, shorten transactions, improve indexes/query patterns or use suitable row-versioning. Retrying the victim can preserve availability but does not remove a frequent deadlock's cause.

**Wait statistics** show where workers spend time, not a verdict. Exclude benign background waits, compare rates/deltas over the incident window and correlate with queries, resource metrics and workload. High `PAGEIOLATCH`-style waits, log waits, lock waits, memory-grant waits or parallelism waits lead to different hypotheses; do not tune one configuration solely from a top cumulative wait.

DMVs such as active requests/sessions, waiting tasks, locks, cached query statistics, missing-index suggestions, index usage/operational stats, file I/O and resource governance differ by platform and permission. DMV state is often transient/reset; persist evidence when trend/history matters.

### Read execution plans and improve query constructs

Read from data access toward joins/aggregates while checking:

- estimated versus actual rows at each operator and where divergence begins;
- scan/seek and the predicate versus residual predicate;
- lookup frequency and whether a covering/filtering/index redesign is justified;
- join choice and build/probe inputs;
- sorts, hashes, spools, spills, memory grant and parallelism exchanges;
- implicit conversions, scalar functions, non-SARGable expressions and parameter sensitivity;
- warnings, missing statistics, compile/recompile and plan reuse.

Make predicates SARGable where possible: avoid wrapping indexed columns in functions or implicit type conversion; use correct datatypes; express ranges precisely; reduce rows/columns early without changing semantics. Do not blindly replace a scan with a seek—large result sets can make a scan correct.

#### Index decisions

An index benefits reads only if its key order, included columns, filter and data distribution match workload. Every index consumes storage and adds DML, logging, backup and maintenance cost. Consolidate overlapping indexes and verify usage across a representative business cycle before dropping. DMV missing-index suggestions omit important workload/cost context and reset.

For rowstore fragmentation, distinguish logical fragmentation from page density and actual workload effect. Do not rebuild every index nightly. Use size, write/read pattern, page fullness, log/IO window, edition/platform online/resumable support and measured benefit. Update statistics when distributions/row modifications make cardinality estimates unreliable; sampling, full scan, incremental statistics and asynchronous update have tradeoffs.

Columnstore organizes column segments and is strong for scans/analytics; rowgroup health, delete bitmap, compression and ordered/partition design matter. It is not universally better for singleton OLTP access.

### Configure maintenance and integrity checks

- **Index maintenance:** targeted reorganize/rebuild or resumable/online operation where supported; plan log, space, replica and blocking effects.
- **Statistics:** auto creation/update plus targeted manual update when evidence requires; do not assume an index rebuild updates every statistic.
- **Integrity:** run `DBCC CHECKDB` or supported integrity validation at a cadence and on a system that meets load/recovery constraints; retain results and alert. A clean check is not a backup.
- **`tempdb`:** size/files/growth and workload design on IaaS/on-premises; understand platform-managed behavior on PaaS.
- **Log:** recovery model, backups where applicable, VLF/growth, long transactions, replication/AG/CDC consumers and free space.

Never use repair options as a routine response. Preserve damaged databases/logs/backups, identify recovery options, and restore from a known-good copy when possible.

### Use automatic tuning and Intelligent Query Processing safely

Azure SQL automatic tuning can create/drop indexes or force last good plans according to platform and configuration. Understand recommendation state, action, validation/revert behavior, scope, inherited/server settings and operational ownership. Monitor automatic actions like any other change; exclude or disable deliberately only with evidence.

Intelligent Query Processing is a family of compatibility-level and version-dependent features such as adaptive behaviors, memory-grant feedback, scalar UDF inlining, table-variable deferred compilation, parameter-sensitive plan optimization and newer capabilities. Know the problem each feature addresses and validate using Query Store/actual workload. A compatibility-level change can enable multiple optimizer behaviors at once; use controlled rollout and Query Store regression protection.

### Configure server and database performance settings

Database-scoped configurations make settings portable and can differ for primary/secondary where supported. Examples include compatibility level, MAXDOP, parameter sniffing behavior, legacy cardinality estimation and IQP controls. Instance-level settings on SQL Server/MI include memory, MAXDOP, cost threshold and others; scope and platform support differ.

Resource Governor on supported SQL Server/Managed Instance platforms classifies sessions into workload groups/resource pools to constrain or prioritize CPU, memory grants and other supported resources. Design classifier reliability, group caps/minimums, internal/default group impact and fail-open behavior. It does not replace application workload management or add resources.

Scaling compute/storage can solve verified capacity limits and provide a safe short-term mitigation. It does not repair blocking, bad plans, unbounded transactions, excessive indexes or inefficient application calls. Capture before/after cost and performance.

### Performance failure patterns

| Symptom | Bad shortcut | Better evidence path |
|---|---|---|
| CPU high | scale immediately | top query/load delta, plans, compilations, concurrency, tier limit, before/after |
| Query suddenly slow | create suggested index | Query Store plan/runtime/waits, statistics/data/deploy/config change |
| Sessions waiting | kill blockers repeatedly | head blocker, transaction age, query/plan, access order, isolation, rollback cost |
| Storage latency | add disks blindly | VM limit, disk limit, cache, file latency, queue, read/write pattern, throttling |
| Query Store read-only | turn it off | quota, cleanup, capture volume, database state and operation mode reason |
| Watcher empty | no database issue | target auth/network, watcher state, datastore, collection datasets and time range |

#### Primary references

- [Database watcher overview](https://learn.microsoft.com/en-us/azure/azure-sql/database-watcher-overview?view=azuresql)
- [Query Store usage scenarios](https://learn.microsoft.com/en-us/sql/relational-databases/performance/query-store-usage-scenarios?view=sql-server-ver17)
- [Extended Events overview](https://learn.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver17)
- [Monitor performance with DMVs](https://learn.microsoft.com/en-us/azure/azure-sql/database/monitoring-with-dmvs?view=azuresql)
- [Execution plans](https://learn.microsoft.com/en-us/sql/relational-databases/performance/execution-plans?view=sql-server-ver17)
- [Automatic tuning for Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/automatic-tuning-overview?view=azuresql)
- [Intelligent Query Processing](https://learn.microsoft.com/en-us/sql/relational-databases/performance/intelligent-query-processing?view=sql-server-ver17)
- [Resource Governor](https://learn.microsoft.com/en-us/sql/relational-databases/resource-governor/resource-governor?view=sql-server-ver17)

---

## 5. Configure and manage automation of tasks (15–20%)

### Choose the task engine by scope

| Mechanism | Natural scope | Key dependencies |
|---|---|---|
| SQL Server Agent | SQL Server/Managed Instance instance jobs, schedules, steps, operators/alerts | Agent availability, service/proxy identity, `msdb`, Database Mail/operator, target resources |
| Elastic jobs | T-SQL across groups of Azure SQL Database targets | job agent/database, target groups, credentials/managed identity, private endpoints, output/history |
| Azure Automation | Azure/control and hybrid runbooks | Automation identity, modules/runtime, network/Hybrid Worker, schedule/webhook, job logs |
| Logic Apps / Functions | Event/workflow orchestration and integrations | connector/function identity, secrets, networking, retry/idempotency, state/cost |
| ARM/Bicep | Declarative Azure resource deployment | resource-provider API, deployment identity, scopes, parameters, what-if/history |
| Azure CLI/PowerShell | Imperative deployment/operations | module/version/auth context, error handling, idempotency, logging |

Do not use an application timer or personal credential when a managed, observable service fits. Every automation needs owner, source version, execution identity, target scope, secret/key handling, retries/timeouts, concurrency, output/history, alert and safe rerun behavior.

### Create and manage SQL Server Agent jobs

A job contains ordered steps, each with a subsystem, database/context, command, retry and success/failure action. A schedule attaches timing; an operator/alert/notification reports outcomes through configured Database Mail and Agent settings.

Security boundaries:

- job owner affects execution and whether non-sysadmin owners can run it;
- T-SQL steps commonly run in the owner's context; other subsystems use Agent service/proxy/credential rules;
- proxies should expose one subsystem and minimum external permissions;
- avoid `sa` or a departing human as an unexplained owner;
- protect command text/output because it may contain sensitive data.

Troubleshoot from Agent service/instance support -> job enabled/owner -> schedule/time zone -> current activity -> step history/output -> subsystem/proxy -> target DB/network -> command error -> notification pipeline. Increase history/logging before rerunning a destructive or expensive step.

Maintenance plans generate Agent-backed workflows but are not automatically appropriate. Prefer targeted backups, integrity checks, statistics and index operations driven by actual platform/workload needs. Azure SQL Database does not expose SQL Server Agent; use elastic jobs or another supported orchestrator.

### Automate resource deployment with ARM and Bicep

ARM templates and Bicep define desired Azure control-plane resources. Bicep compiles to ARM JSON. Know:

- resource type/API version, parent-child/symbolic dependency and existing resource references;
- parameters, secure parameters, variables, modules, outputs and deployment scope;
- incremental behavior versus explicit complete/stack deletion semantics;
- what-if, validation, deployment operation logs and correlation IDs;
- identity/RBAC, policy denial, locks, provider registration, quota and regional availability;
- secrets: reference Key Vault or identity-driven deployment; never commit plaintext outputs/parameters.

Database schema is a different lifecycle. Use SQL projects/DACPAC, migrations or another controlled data-plane method after the endpoint and identity are ready. An ARM deployment does not apply arbitrary T-SQL schema changes.

For Azure CLI/PowerShell, pin/test versions, use noninteractive workload identity, set explicit subscription/context, fail on errors, emit structured logs, handle long-running operations and implement idempotent checks. Avoid blind “exists, so skip” logic when existing configuration may drift.

### Build elastic jobs

Elastic jobs run T-SQL across one or many Azure SQL Database targets. Core objects include:

- elastic job agent and job database;
- credentials or Microsoft Entra authentication according to current support;
- target groups containing servers, pools, databases or exclusions;
- jobs, ordered steps, schedules and output/history;
- private endpoint/network configuration and Azure Monitor alerts.

Design each step for retry and partial failure. A target group can change between executions; schema or data commands must be safe when some databases are already updated. Limit concurrency/batch impact, route output to a controlled database, and prove which exact targets succeeded.

Use [elastic jobs guidance](https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-jobs-overview?view=azuresql) for current authentication, capacity, limits and private-endpoint behavior, and the [configuration tutorial](https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-jobs-tutorial?view=azuresql) for supported setup paths.

### Automate database tasks in Azure

Azure Automation runbooks can scale a database, invoke a controlled T-SQL task, check status or coordinate maintenance. Prefer PowerShell 7.x or supported current runtimes/modules. Use managed identity with least Azure/SQL permissions; run within a Hybrid Runbook Worker or private network path when endpoints are not public. Record module/runtime versions and test upgrades.

Logic Apps can react to schedule/event/approval and call Azure/SQL/notification operations. Configure connector identity, networking, state/retention, retry policy and duplicate-delivery handling. Do not assume at-least-once workflow delivery means exactly-once database mutation.

#### Alert on automation

Monitor at least:

- scheduler triggered and job started within expected window;
- target list and per-target success/failure;
- duration, retry, timeout and concurrency threshold;
- output/history retention and queryability;
- notification/action delivery;
- automation agent/runtime/identity expiration or permission drift;
- expected database postcondition.

An “Succeeded” orchestration status may mean the script exited zero even though zero target rows changed. Assert a business/technical postcondition.

### Automation failure patterns

| Symptom | First checks |
|---|---|
| Agent job never ran | Agent/service support, job/schedule enabled, next run/time zone, owner |
| Step succeeds manually only | Agent/proxy identity, database context, environment/path, permissions, network |
| Elastic job partial success | target membership, per-target history/output, retry/idempotency, schema version |
| ARM deployment failed | operation detail, API/version/property, RBAC/policy/lock/quota/dependency |
| Runbook cannot reach private SQL | worker/network/DNS/route/firewall, identity/token, SQL principal |
| Repeated workflow duplicates data | retry/delivery semantics; add idempotency key/transactional guard |

#### Primary references

- [SQL Server Agent](https://learn.microsoft.com/en-us/sql/ssms/agent/sql-server-agent?view=sql-server-ver17)
- [Elastic jobs overview](https://learn.microsoft.com/en-us/azure/azure-sql/database/elastic-jobs-overview?view=azuresql)
- [Bicep overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview?tabs=bicep)
- [ARM deployment operations](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deployment-history?tabs=azure-portal)
- [Azure Automation runbook types](https://learn.microsoft.com/en-us/azure/automation/automation-runbook-types)

---

## 6. Plan and configure high availability and disaster recovery (20–25%)

### Translate business objectives into mechanisms

- **RPO:** maximum tolerable data loss, measured as time/transactions.
- **RTO:** maximum time until the application transaction is restored.
- **Availability:** continuity during expected local component failures.
- **Disaster recovery:** recovery from a larger fault such as region/site loss.
- **Backup retention:** historical points for deletion, corruption, ransomware, compliance or rollback.

Derive design from failure scenarios: database/service process, host/zone, storage, operator deletion, logical corruption, credential/key loss, region, network/DNS, identity, and full application dependency. Built-in local HA does not protect from every logical or regional failure; geo-replication is not historical backup.

Document workload/write rate, allowable data loss/downtime, read needs, consistency, failover authority, endpoint changes, capacity at secondary, identity/network/key dependencies, backup retention, test frequency, failback and cost.

### Compare Azure SQL Database continuity options

| Mechanism | Unit/path | Strong use | Boundary |
|---|---|---|---|
| Built-in service HA / zone redundancy | tier architecture, same region | local component/zone availability according to configuration | not regional DR or historical recovery |
| Active geo-replication | individual database, asynchronous readable geo-secondaries | per-database DR/read scale/migration | application endpoint changes; independent server settings; possible data loss |
| Failover group | group of databases between logical servers; stable read-write/read-only listeners | coordinated database failover and connection endpoint | asynchronous geo lag; only group members; external dependencies not replicated |
| Geo-restore | geo-redundant backup creates new DB/server target | lower-cost regional recovery | higher RTO/RPO, new endpoint/configuration, latest geo backup only |
| PITR | automated backup chain inside retention | user error/corruption/time recovery | restores a new database; not instant failover |
| LTR | selected retained full backups | compliance/history up to configured policy | restore creates new database; no continuous RPO |

Active geo-replication streams transaction log asynchronously. A secondary is transactionally consistent but can lag. Failover groups build on geo-replication and provide stable listener names for group failover. Neither automatically replicates all server-level logins, firewall/private endpoints, Entra administrator, auditing, alerts, jobs, keys or application dependencies. Configure and test both regions.

For business-critical transactions, understand the latency/availability effect of `sp_wait_for_database_copy_sync` where applicable; it waits for committed log to harden remotely but can block if connectivity is impaired. Do not promise zero regional data loss from ordinary asynchronous replication.

### Plan SQL Managed Instance and SQL Server HA/DR

Azure SQL Managed Instance has built-in service HA and supports failover groups for cross-region continuity according to tier/region/network prerequisites. It also supports link scenarios using distributed availability group technology for migration/hybrid needs. Keep instance-level objects, jobs/logins, keys, network and failover endpoints in the plan.

On SQL Server/VMs:

- **Always On availability group (AG):** replicates selected user databases to replicas; synchronous/asynchronous modes, automatic/manual failover, readable secondaries and listener. It depends on WSFC on Windows or supported Linux cluster manager and does not replicate instance objects such as logins/jobs.
- **Failover cluster instance (FCI):** protects the whole SQL instance using clustered shared storage; one active instance owns the disks at a time. Azure VM designs use supported storage/witness/DNN or load-balancer patterns according to current architecture.
- **Log shipping:** scheduled backup/copy/restore to warm secondaries; simple and tolerant of distance but manual/operated failover with RPO/RTO from schedule and lag.
- **Backup/restore:** historical recovery and portable mechanism; can seed/migrate but requires restore time and log-chain discipline.

AG is database-level replication, FCI is instance-level shared-storage failover, and log shipping is backup-log delivery. Combining FCI/AG can cover different failure scopes but adds operational complexity. Validate quorum/witness, cluster networks, listener/name resolution, load balancer or distributed network name, storage fencing, replica health and client connection behavior.

### Back up and restore by platform

#### SQL Server native backup

Choose full, differential and transaction log backups from recovery model and RPO. A restore chain usually starts with a full, optional differential, then ordered log backups through the target point. Tail-log backup may protect final unbacked log when source state permits. `COPY_ONLY` avoids disrupting differential base or normal log sequence according to backup type.

Back up to Azure Blob Storage using supported `BACKUP TO URL`, credential/managed identity/SAS and stripe/compression/encryption options for the platform/version. Protect the backup encryption certificate/key separately; without it encrypted backup is unrecoverable. Validate with restore, not only `RESTORE VERIFYONLY`.

#### Azure SQL Database and Managed Instance automated backup

Azure SQL creates automated backups for PITR according to platform. Restore produces a new database; account for name/server, tier, network, identity, jobs and application cutover. Configure short-term retention and backup storage redundancy. LTR copies selected full backups under weekly/monthly/yearly policy for longer retention and restores a new database.

Do not memorize limits from an old course. As of validation, current docs describe SQL Database short-term retention up to 35 days for applicable tiers and LTR up to ten years, but exact tier/platform/immutability/API behavior is volatile. Verify [automated backups](https://learn.microsoft.com/en-us/azure/azure-sql/database/automated-backups-overview?view=azuresql) and [LTR](https://learn.microsoft.com/en-us/azure/azure-sql/database/long-term-retention-overview?view=azuresql) before design.

#### Restore validation

1. Select a recovery point known to precede the incident and preserve evidence.
2. Restore to isolated/new location with sufficient quota, identity, network and key access.
3. Run integrity checks and reconcile expected data/time/transaction.
4. Recreate or verify users/logins, jobs, external credentials, keys/certificates, dependencies and compatibility.
5. Test representative read/write application transaction and performance.
6. Establish protection/monitoring for the restored target before production acceptance.
7. Record actual recovery point age and elapsed RTO.

### Configure and operate AGs, FCIs, geo-replication and log shipping

For any replica mechanism, monitor transport/send/redo queue and rate, synchronization/health, endpoint/session, replica/database state, cluster/quorum, listener, storage, errors and application latency. Establish alert thresholds derived from RPO and rate—queue size without throughput context is incomplete.

Planned failover sequence:

1. confirm target health/synchronization/capacity and external dependencies;
2. freeze or coordinate transactions if the mechanism/application requires it;
3. initiate the supported failover operation at the correct layer;
4. validate listener/DNS/connection policy, authentication, network and application transaction;
5. verify former primary/new secondary and protection direction;
6. monitor data/latency/jobs/backups; document actual RPO/RTO;
7. plan failback as a separate controlled operation.

Forced failover can lose data when the secondary is not synchronized. Never treat it as a harmless test. Use test environments or platform-supported drills and explicitly choose the recovery point/data-loss decision.

### Test the complete recovery path

A credible HA/DR test includes:

- event/failure scope and decision authority;
- alert detection and incident communication;
- identity, MFA/break-glass, subscription/RBAC and key access independent of failed region/site;
- DNS/private endpoints/firewalls/routes/listeners and application retry/pooling;
- target compute/storage capacity and quotas;
- database consistency and data/RPO reconciliation;
- logins/users/jobs/agents/external services and monitoring/backup at recovery site;
- representative business transaction, not just `SELECT 1`;
- failback/reprotection and cleanup;
- measured actual RTO/RPO and remediation owners.

> **Related item:** A stable database listener does not guarantee stable application state. Connection pools may retain dead sockets, DNS may cache, tokens/keys may be region-bound, and message/storage services may have different recovery. The database is one dependency in the service recovery plan.

### HA/DR failure patterns

| Symptom | Avoid assumption | Evidence-led response |
|---|---|---|
| Geo-secondary healthy | zero data loss guaranteed | replication lag and business RPO; async semantics |
| Failover group completed | app recovered | listener/DNS, private network, identity, key, app pool/retry and transaction |
| Backup job successful | database recoverable | restore chain/key/quota/permissions plus isolated restore and validation |
| AG replica connected | ready for automatic failover | synchronization/commit mode, cluster vote, failover mode, database health |
| FCI role online | clients can connect | listener/name/IP/probe, SQL service, storage, firewall, authentication |
| Log shipping copy current | RPO met | last restored log/time, restore delay/mode, gaps and monitor server |

#### Primary references

- [Business continuity with Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/business-continuity-high-availability-disaster-recover-hadr-overview?view=azuresql)
- [Active geo-replication](https://learn.microsoft.com/en-us/azure/azure-sql/database/active-geo-replication-overview?view=azuresql-db)
- [Failover groups overview](https://learn.microsoft.com/en-us/azure/azure-sql/database/failover-group-sql-db?view=azuresql)
- [Restore Azure SQL Database from backup](https://learn.microsoft.com/en-us/azure/azure-sql/database/recovery-using-backups?view=azuresql)
- [Always On availability groups on Azure VMs](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/availability-group-overview?view=azuresql)
- [Failover cluster instances on Azure VMs](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/failover-cluster-instance-overview?view=azuresql)
- [Log shipping](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver17)
- [SQL Server backup and restore](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17)

---

## 7. Integrated scenarios

### Scenario A — Migrate a regulated SQL Server workload with minimal downtime

**Requirements:** Instance-level dependencies, customer-managed key control, less than 30 minutes write outage, regional DR, and auditable administration.

1. Inventory databases plus logins/users, Agent jobs, credentials, certificates/keys, linked servers, CLR/features, drivers, SSIS/reporting and application transaction paths.
2. Run current readiness/compatibility and performance-based sizing against SQL Managed Instance and SQL Server on Azure VM; document every blocker and responsibility trade-off.
3. Select target from required instance surface, patch/OS ownership, RPO/RTO, network and compliance—not from migration convenience.
4. Build private DNS/network, Entra/SQL identities, least permissions, Key Vault/key lifecycle, auditing and monitoring before data movement.
5. Choose Managed Instance link or supported Azure DMS online migration when prerequisites meet the outage target; otherwise quantify offline transfer/restore.
6. Rehearse schema/server-object sequence, synchronization, write freeze, final catch-up, endpoint/connection pool switch and rollback.
7. Validate reconciliation, permissions, jobs, encryption, query plans/performance and actual application transactions.
8. Configure failover group/AG and backup retention, then execute an isolated recovery test before accepting and later decommissioning the source.

The migration tool moves supported state; it does not discover or operate every external dependency. Acceptance evidence must span data, security, performance, automation and recovery.

### Scenario B — Diagnose a multitenant Azure SQL performance incident

**Symptoms:** Latency rose after a deployment, one tenant is much slower, pool CPU is high, and blocking appears intermittently.

1. Define affected transactions, tenants, time window, deployment/config/data changes and error/retry behavior.
2. Correlate application traces with pool/database metrics, database watcher datasets, Query Store runtime/waits and targeted DMVs.
3. Compare old/new plans and cardinality by tenant parameters; find head blockers and transaction scope.
4. Determine whether the bottleneck is plan regression/parameter sensitivity, missing/overlapping index, non-SARGable predicate, long transaction, pool cap or skewed tenant/shard design.
5. If risk requires, force a verified prior plan or isolate/scale as a reversible mitigation with monitoring.
6. Correct query/index/statistics/transaction or workload placement; test representative tenant distributions and concurrency.
7. Remove temporary mitigation when stable and retain Query Store/performance evidence.
8. Add regression alert and a deployment gate tied to the real transaction, not only CPU.

### Scenario C — Recover a regional database service after identity and network changes

**Requirements:** Failover-group database, private connectivity, Entra application identity, customer-managed TDE and 15-minute RTO.

1. Confirm failover authority and replica lag against RPO; preserve outage and replication evidence.
2. Verify secondary capacity, Key Vault key/version and identity permissions in the recovery region.
3. Verify private endpoints/DNS forwarding, firewall/routes and the failover-group listener from the application network.
4. Confirm contained/Entra database principals and server-level configuration are ready; separately synchronize any nonreplicated objects.
5. Perform planned or forced failover with the explicit possible-data-loss decision.
6. Flush/recycle connection pools only as necessary and validate token acquisition, listener resolution, TLS and read/write transaction.
7. Confirm auditing, database watcher/alerts, backup policy and automation jobs operate against the new primary without duplicates.
8. Measure RPO/RTO, reprotect the database and plan failback after root cause/region recovery.

---

## 8. Hands-on labs

These original labs are not copied exam or paid-course content. Use disposable Azure resources, set budgets and clean up promptly. Keep an evidence journal containing requirement, architecture, commands/templates, effective state, known signal, injected failure, diagnosis, repair, validation and cost.

### Lab 1 — Compare and deploy Azure SQL targets

Deploy a small Azure SQL Database using Bicep or ARM plus CLI/PowerShell parameters. Model—but do not necessarily deploy—a Managed Instance and SQL Server VM for the same workload. Compare feature/ownership, tier/compute/storage, network, identity, backup and HA/DR.

**Evidence:** decision matrix, template/parameters, deployment history, resource state, TDS transaction, retry observation, cost estimate and cleanup.

### Lab 2 — Assess and rehearse a database migration

Create a disposable source SQL Server database containing schema, data, login/user, Agent-style task and one deliberately target-incompatible or warning-producing feature. Run a current supported readiness assessment, select target/method, remediate or document exclusion, migrate offline or through a supported sandbox method, then reconcile.

**Evidence:** inventory, assessment findings, source/target versions, migration job, row/hash/schema comparison, principal/object mapping, application transaction, cutover and rollback runbook.

### Lab 3 — Implement layered Azure SQL security

Create an Entra group or test identity and contained database user, a custom role/schema permission, one explicit deny test, server/database firewall or private endpoint plan, TDE state, audit destination, classification, DDM and RLS policy. If resources permit, test Always Encrypted with a supported client.

**Evidence:** identity/token method, Azure RBAC versus SQL permissions, positive/negative queries, DNS/network result, encryption/key boundary, audit record, masking/RLS tests and cleanup.

### Lab 4 — Build a baseline and diagnose a query regression

Load a test data set with skew, enable/configure Query Store, capture baseline and execute parameter variants. Introduce a safe index/statistics/query change that produces a measurable regression. Use plan, Query Store, waits/DMVs and resource metrics to isolate it; mitigate and correct it.

**Evidence:** workload generator, latency distributions, query/plan IDs, actual plans, estimates versus actuals, waits/resource graph, mitigation, final performance and regression test.

### Lab 5 — Capture blocking and an Extended Events signal

Open two sessions, hold a transaction in one and create blocking in the other. Capture requests, locks, waiting tasks and transaction state. Build a narrowly filtered Extended Events session for a safe error, long statement or deadlock exercise. Repair transaction/query behavior rather than merely killing it.

**Evidence:** session timeline, head blocker/resource, transaction age, event-session definition/file, event fields, root cause, rollback time and corrected transaction.

### Lab 6 — Automate a fleet task safely

Use SQL Agent on a local/VM SQL instance or elastic jobs against two small Azure SQL databases. Create target selection, idempotent schema/data task, schedule, controlled partial failure, per-target output, retry and alert. Rerun it safely.

**Evidence:** execution identity, job/steps/targets, first and repeated run, partial failure, history/output, alert delivery, database postcondition and cleanup.

### Lab 7 — Restore and validate a database

Create known rows, permissions and checksum markers. Use native backup/restore in a local/VM lab or Azure SQL PITR to restore to a new database. If possible, configure an LTR policy but do not retain costly artifacts unnecessarily. Measure recovery point age and elapsed time.

**Evidence:** policy/job/recovery point, restore operation, restored time/data, integrity/reconciliation, user/permission behavior, application read/write, actual RPO/RTO and cleanup.

### Lab 8 — Configure and test an HA/DR path

Choose active geo-replication/failover group in an Azure sandbox or AG/log shipping in an isolated SQL Server lab. Configure replication, observe lag/health, execute a planned test failover, validate endpoint and transaction, then reprotect/fail back. Do not force data loss in a shared environment.

**Evidence:** topology, RPO/RTO target, health/lag, prechecks, failover timeline, DNS/listener, data reconciliation, app transaction, backup/monitoring state and reprotection.

---

## 9. Knowledge checks

These are original reasoning checks based on public objectives, not recalled exam questions.

### Platform and migration

1. **When does Managed Instance fit better than Azure SQL Database?** When required instance-level features, cross-database/Agent behavior and SQL Server compatibility fit MI while the organization still wants PaaS patching/backup/HA. Validate feature and network differences rather than assuming full parity.
2. **Why can an elastic pool cost less but perform worse?** Members share aggregate resources. Savings depend on noncoincident usage and correct per-database limits; a noisy or constantly saturated member can constrain others.
3. **How do partitioning and sharding differ?** Partitioning divides one table/index inside a database for elimination/manageability. Sharding routes data across multiple database units and adds routing, cross-shard and fleet operations.
4. **What is the difference between SQL Server enabled by Azure Arc and Arc-enabled SQL Managed Instance?** The former projects/manages existing SQL Server instances through Azure; the latter deploys a managed SQL service on Arc-enabled Kubernetes through an Arc data controller.
5. **Why is “online migration” not zero downtime?** The source can remain writable during sync, but cutover still coordinates final changes, connection switch, validation and possible rollback. Lag and prerequisites add operational risk.
6. **Why must a migrated database be validated beyond row count?** Schema, users/logins, permissions, jobs, keys, external dependencies, plans/performance and business semantics can fail while rows match.

### Security

7. **Why does Azure Contributor not imply database `SELECT`?** Azure RBAC governs the resource control plane; SQL authentication/principals/permissions govern the data plane.
8. **What does a private endpoint not do automatically?** It does not necessarily disable public access, create every client/on-prem DNS path, grant SQL access or make the client use the private IP.
9. **How do TDE and Always Encrypted differ?** TDE protects database/log/backup files while the engine sees plaintext. Always Encrypted uses a client/key boundary so the engine normally does not see protected column plaintext.
10. **Why is deterministic Always Encrypted weaker than randomized encryption?** Equal plaintext produces equal ciphertext, exposing equality patterns, but allowing equality lookup/join operations without an enclave.
11. **Why is DDM not a security boundary for highly privileged users?** It changes result presentation for users without `UNMASK`; it does not encrypt data or prevent inference/permission bypass.
12. **What does ledger prove?** It provides cryptographic tamper evidence for recorded database history according to its model; it does not prevent changes or prove input truth and does not replace backup/audit.

### Monitoring and performance

13. **Why is one CPU average a poor baseline?** It hides peaks, concurrency, query mix and application latency and cannot identify whether compute was the limiting resource.
14. **When is Query Store more useful than a current DMV snapshot?** When comparing query/plan/runtime/wait history across a regression window, restart or deployment; DMVs are often current/transient.
15. **What is the first purpose of an Extended Events predicate?** Reduce event volume/overhead and sensitive data so the session captures only evidence needed for the question.
16. **Why can killing a head blocker worsen the incident?** Its transaction must roll back, which can take time and consume resources; the application can recreate the same long transaction.
17. **Why should a missing-index DMV suggestion not be implemented blindly?** It is reset/scoped and lacks full write, storage, overlap, maintenance and complete workload context.
18. **What should happen after forcing a last good plan?** Monitor it as mitigation, investigate and fix the root cause, test representative parameters/load and later remove forcing when safe.

### Automation

19. **Why can a SQL Agent job succeed manually but fail on schedule?** Scheduled execution can use a different owner, service account, proxy, database context, environment/path and network/permission boundary.
20. **What makes an elastic-job step safely repeatable?** Idempotent or transactionally guarded logic, schema/version checks, per-target result tracking and safe handling when some targets already succeeded.
21. **What does an ARM deployment success not prove?** That a client can resolve/connect/authenticate, the schema exists, data migrated, queries meet latency or restore works.
22. **Why assert a postcondition after an automation status is Succeeded?** The script may exit successfully while selecting no targets or changing zero intended rows; validate the required database outcome.

### HA/DR

23. **How do RPO and RTO differ?** RPO limits acceptable lost data/time; RTO limits elapsed time until the application service is restored.
24. **Why can active geo-replication lose committed data?** It is asynchronous across distance, so a forced failover can promote a secondary before the latest log hardened there.
25. **What does a failover-group listener solve?** A stable read-write/read-only connection endpoint across group failover; it does not replicate all server/network/identity/key/application dependencies.
26. **How do AG and FCI differ?** AG replicates selected databases between SQL instances/replicas; FCI fails over one SQL instance using clustered shared storage.
27. **Why is replication not backup?** Deletion, corruption or malicious change can replicate quickly, while backups retain independent historical recovery points.
28. **What is the only convincing backup-success test?** A supported restore into an isolated target followed by integrity, data, security/dependency and application transaction validation with measured RPO/RTO.

---

## 10. Final review checklist

- [ ] I can select Azure SQL Database, elastic pool/serverless/Hyperscale, Managed Instance, SQL VM, Fabric SQL or an Arc SQL option from requirements.
- [ ] I can automate a complete resource including identity, network, monitoring, backup and security—not only a database SKU.
- [ ] I can explain partitioning, compression and sharding and diagnose when each will not solve the stated bottleneck.
- [ ] I can assess, choose online/offline, migrate, cut over, reconcile and troubleshoot a SQL workload using current supported tools.
- [ ] I can separate Azure RBAC from SQL authentication and authorization and trace Entra/SQL/Windows identities.
- [ ] I can configure firewall/service endpoint/private endpoint/TLS paths and diagnose DNS before changing SQL permissions.
- [ ] I can compare TDE, object encryption, Always Encrypted, secure enclaves and TLS by threat/key boundary.
- [ ] I can implement and explain classification, audit, change tracking/CDC, DDM, ledger and RLS without overstating them.
- [ ] I can build a baseline and choose metrics, watcher, DMVs, Query Store, Extended Events, plan or application evidence.
- [ ] I can diagnose blocking/deadlocks/waits, plans/cardinality, indexes/statistics, integrity, automatic tuning, IQP and capacity.
- [ ] I can implement SQL Agent, elastic jobs, ARM/Bicep, PowerShell/CLI and Azure workflow automation with least privilege and safe retry.
- [ ] I can derive Azure SQL geo/PITR/LTR, Managed Instance, AG, FCI, log shipping and native backup choices from RPO/RTO.
- [ ] I can perform a planned failover/restore and prove data, identity, network, keys, jobs, monitoring and the application transaction.
- [ ] I can explain why Azure Data Studio material is legacy after February 28, 2026 and identify current migration/tooling paths.
- [ ] I completed at least one security, query-regression, automation and recovery failure-injection lab.
- [ ] I rechecked the official April 24, 2026 blueprint and lifecycle status before scheduling.

---

## Places to learn

This is **not a complete list**, and it is not meant to be consumed end to end. Pick the resources and formats that work for you. A practical plan is the official blueprint/documentation, one primary structured course or book, hands-on labs, and one legitimate practice assessment used to find weak domains. Avoid any provider selling recalled live questions, “dumps,” VCE files, or guarantees based on leaked content.

Estimated times describe content consumption or a reasonable assessment session, not total preparation. Add lab time, notes, current-document checks, spaced review and remediation. Provider access, catalog, duration, price and April 2026 alignment can change; verify them before purchase. Older SQL content can teach durable engine concepts, but reconcile Azure Data Studio retirement, current migration paths, database watcher, Fabric SQL, service tiers, security and HA/DR with current official documentation.

### Microsoft resources

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official DP-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300) | Free; authoritative April 24, 2026 objectives | 45–75 min to map; 10–15 min weekly | Coverage checklist, weights, changes and official links |
| [Azure Database Administrator Associate page](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/) | Free | 20–30 min; recheck before scheduling | Current status, 100-minute exam, practice and renewal links |
| [DP-300T00 course and self-directed modules](https://learn.microsoft.com/en-us/training/courses/dp-300t00) | Modules free; instructor-led access varies | **4 instructor-led days**; plan 35–55 hr self-paced with labs | Structured official path across all five domains |
| [Microsoft free DP-300 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/dp-300/practice/assessment?assessment-type=practice&assessmentId=58) | Free; sign-in may be required | 45–90 min per attempt; 4–8 hr with remediation | Baseline, then diagnose weak objectives from explanations |
| [Exam Readiness Zone DP-300 search](https://learn.microsoft.com/en-us/shows/exam-readiness-zone/?terms=DP-300) | Free | Estimate 2–4 hr plus notes | Objective review; verify recording date against April 2026 |
| [Azure SQL documentation](https://learn.microsoft.com/en-us/azure/azure-sql/) and [SQL Server documentation](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver17) | Free | Select 15–40 hr by gap | Current behavior, prerequisites, limitations and implementation details |

### Courses, books, and practice providers

| Resource | Access | Estimated time | Notes |
|---|---|---:|---|
| [Pluralsight DP-300 path](https://www.pluralsight.com/paths/microsoft-certified-azure-database-administrator-associate) | Paid; four courses, one lab, practice exam displayed | **7 hr** displayed; plan 12–20 hr with lab/docs | Recent 2025–July 2026 content; verify whether every planning and HA/DR objective is present in the current path |
| [O'Reilly/Apress DP-300 study companion](https://www.oreilly.com/library/view/administering-microsoft-azure/9798868815850/) | Paid subscription; Geoff Hiten, September 2025 | **9h 44m**, 388 pages; plan 15–24 hr with exercises/current diff | Broad exam-aligned book; reconcile April 2026 objective additions and retired Azure Data Studio |
| [O'Reilly Administering Microsoft Azure SQL video](https://www.oreilly.com/videos/administering-microsoft-azure/0636920934721/) | Paid subscription; Mikey Bronowski, September 2024 | **1h 44m** plus 2–4 hr practice/docs | Compact overview, not sufficient alone; older tooling/monitoring needs reconciliation |
| [O'Reilly DP-300 certification-prep catalog](https://www.oreilly.com/products/certification-prep.html) | Paid; catalog lists DP-300 book, guide, practice and on-demand formats | Verify selected item; plan 2–4 hr per practice attempt plus review | Use the current item page to confirm version and blueprint alignment |
| [Udemy DP-300 course by Phillip Burton](https://www.udemy.com/course/dp-300-administering-relational-databases-azure-dba/) | Paid; page showed April 2026 alignment, 173 lectures | **17h 40m** video; plan 25–40 hr with labs | Current commercial structured option; independently verify every claim with official docs |
| [Whizlabs DP-300](https://www.whizlabs.com/microsoft-azure-certification-dp-300/) | Paid; packaging can include course/practice/labs | Verify current displayed duration/question/lab count; plan 10–25 hr selectively | Map coverage to April 2026 blueprint and use practice diagnostically |
| [MeasureUp DP-300 practice test](https://www.measureup.com/microsoft-practice-test-dp-300-administering-relational-databases-on-microsoft-azure.html) | Paid | Estimate 4–8 hr across baseline, explanation review and retest | Verify current objective date/question count; use explanations for remediation, not memorization |

### Supplemental experts and channels

| Resource | Access | Estimated time | Notes |
|---|---|---:|---|
| [Data Exposed](https://learn.microsoft.com/en-us/shows/data-exposed/) | Free Microsoft show | Select 4–12 hr; episodes commonly 10–40 min | Azure SQL and SQL Server feature explanations/demos; check date and platform |
| [Azure SQL YouTube channel](https://www.youtube.com/@AzureSQL) | Free | Select 3–10 hr by weak topic | Product-team demos and deep dives, not a single exam path |
| [John Savill Azure SQL YouTube search](https://www.youtube.com/@NTFAQGuy/search?query=Azure%20SQL) | Free | Select 2–6 hr | Architecture/context supplement; validate detailed operational steps in official docs |
| [John Savill public GitHub repositories](https://github.com/johnthebrit) | Free; license varies by repository/file | 1–2 hr to find matching whiteboards/materials | Link or reuse only under the actual repository/file license |
| [Microsoft Reactor YouTube channel](https://www.youtube.com/@MicrosoftReactor) | Free | Select 2–8 hr; sessions often 45–120 min | Azure/data community sessions; verify date, service version and objective fit |

### Suggested selective plans

#### Experienced SQL Server DBA, newer to Azure

1. Map the blueprint and take the free assessment: 2–3 hours.
2. Study target selection, Azure resource/network/Entra security, DMS/current migration, PaaS monitoring/automation and Azure SQL continuity: 20–35 hours.
3. Complete Labs 1–3, 6 and 8: 25–40 hours.
4. Use one structured resource selectively and remediate from official docs: 10–20 hours.

**Planning range:** approximately 60–95 focused hours when T-SQL, Query Store/plans, SQL Agent, backup/restore and AG concepts are already routine.

#### Azure administrator/developer, newer to database administration

1. Learn relational/transaction/log, SQL security, indexing/statistics, plans/waits/blocking, recovery models and native backup foundations: 35–60 hours.
2. Complete the official path or one complete mapped course/book: 35–55 hours.
3. Complete all eight labs and repeat the query, security and restore labs with new faults: 50–75 hours.
4. Use assessments to drive documentation and hands-on remediation: 12–25 hours.

**Planning range:** approximately 135–210 hours depending on existing T-SQL, networking and operations experience.

#### Final review

1. Recheck the official blueprint, credential page and lifecycle status.
2. Rebuild the five-domain map and service/feature comparison tables from memory.
3. Explain every **VERIFY CURRENT**, **LEGACY/RETIRED**, identity/key boundary and RPO/RTO decision.
4. Diagnose one query regression and one failed automation from evidence before changing configuration.
5. Restore/fail over a disposable database and prove the full application transaction.
6. Use one legitimate practice assessment, research every uncertain answer and stop repeating once recall replaces reasoning.

---

### Currency and integrity note

This guide is an independent synthesis of public sources. It does not reproduce exam questions and is not an exam dump. Microsoft can change DP-300 objectives, exam delivery, Azure SQL/Fabric/Arc capabilities, service tiers, regions, limits, pricing/licensing, migration tools, clients/drivers, preview/GA state, monitoring, security, automation, backup retention and HA/DR behavior. Verify the official blueprint, credential page and linked product documentation before an exam or production decision.
