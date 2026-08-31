---
exam_code: AZ-120
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-120
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# AZ-120 Planning and Administering Microsoft Azure for SAP Workloads Study Guide

> **Independent AI-assisted resource — SOURCE-VALIDATED.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [source-validation record](../docs/SOURCE-VALIDATION.md). The [official AZ-120 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-120) is authoritative.

**Current baseline:** Skills measured as of April 17, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of August 31, 2026.<br>
**Certification lifecycle:** Active; no retirement or replacement is announced on the [official credential page](https://learn.microsoft.com/en-us/credentials/certifications/azure-for-sap-workloads-specialty/) as of August 31, 2026.<br>
**Official source:** [AZ-120 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-120)

## How to use this guide

AZ-120 is a specialist exam. It assumes that you can reason about an SAP landscape—not just individual Azure resources—and that you know where Microsoft support, SAP certification, operating-system support, database support, and business recovery requirements intersect. Start every design with the SAP system identifiers, tiers, interfaces, business criticality, maintenance model, and measurable SAPS, memory, storage, latency, RPO, and RTO requirements.

Use a decision record for every scenario:

```text
business process and SLA
-> SAP products, versions, database, OS and support notes
-> migration pattern and downtime budget
-> landing zone, identity and network boundaries
-> certified compute and supported storage
-> application/database HA and fencing
-> regional DR and backup/restore
-> monitoring, operations, ownership and cost
-> tested evidence and rollback plan
```

Do not deploy costly SAP-sized infrastructure merely to complete every exercise. Most labs can be done as architecture reviews, configuration inventories, Bicep linting, policy tests, tabletop exercises, or small representative deployments. Estimate cost, quotas, licensing, and cleanup before provisioning.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Landscape question |
|---|---:|---|
| Migrate SAP workloads to Azure | 25–30% | What target, operating model, integration design, migration method, sequence, downtime and validation plan fit this landscape? |
| Design and implement infrastructure to support SAP workloads | 25–30% | Are compute, network, storage, images and deployment automation both SAP-supported and fit for measured demand? |
| Design and implement high availability and disaster recovery | 20–25% | Which failures are absorbed locally, which require regional recovery, and how are split-brain, data loss and recovery order controlled? |
| Maintain SAP workloads on Azure | 20–25% | Can teams observe, protect, optimize and safely operate the complete system throughout its lifecycle? |

---

# 1. Build the SAP-on-Azure mental model

## Separate the layers

A typical SAP system contains several independently scaled and protected layers:

| Layer | Typical responsibility | Questions to ask |
|---|---|---|
| Entry and presentation | SAP GUI, Fiori, Web Dispatcher, load distribution | Where do TLS, DNS and user routing terminate? |
| Application | Primary and additional application servers | Can instances scale horizontally, and is session/state behavior understood? |
| Central services | ASCS/SCS and ERS | Which singleton services need clustering, a virtual name/IP and shared state? |
| Database | HANA or supported AnyDB | What are the certified compute/storage combinations, replication mode and recovery sequence? |
| Shared files | SAP global/transports/interfaces | Which protocol, consistency, latency and HA behavior are supported? |
| Platform | Azure compute, network, storage, identity, policy and monitoring | Which team owns each control and escalation path? |

Availability of one layer does not make the SAP system available. An application tier with several servers still fails if ASCS, the database, DNS, shared storage, identity, a network path, or an upstream interface is unavailable.

## Treat supportability as a design constraint

Use this evidence hierarchy:

1. current SAP Product Availability Matrix, hardware directory and SAP Notes;
2. current Microsoft [supported-products guidance](https://learn.microsoft.com/en-us/azure/sap/workloads/supported-product-on-azure) and [supported deployment scenarios](https://learn.microsoft.com/en-us/azure/sap/workloads/planning-supported-configurations);
3. operating-system, database and Azure service documentation;
4. tested customer-specific evidence.

“Technically possible” is not equivalent to “supported.” Check the exact SAP product and kernel, database release, OS version, VM family, storage type, filesystem, HA framework and region. Record the relevant note numbers and access dates in the architecture decision.

**VERIFY CURRENT:** SAP Notes and the HANA hardware directory can require an SAP login; VM certification, supported releases, regional availability, quotas and service limitations change independently of this guide.

> **Related item:** The cloud shared-responsibility model does not replace the Microsoft/SAP support boundary. A reproducible configuration inventory and clear first-call routing reduce time lost between Azure, SAP, OS, database and network support teams.

## Translate business requirements into engineering measures

| Business statement | Engineering evidence |
|---|---|
| “Month-end cannot stop” | Critical transaction map, dependency map, capacity headroom, component SLA model and tested failover |
| “No data loss” | Explicit RPO, synchronous-replication feasibility, commit-path latency and failure-mode analysis |
| “Recover in four hours” | Ordered runbook, replication/backup lag, infrastructure deployment time, restore time and application validation time |
| “Move as-is” | Source inventory, target certification, sizing, platform compatibility and cutover rehearsal |
| “Reduce cost” | Demand profile, rightsizing evidence, reservation/savings-plan scope, storage tiering and nonproduction schedule |

An SLA is a provider commitment under stated conditions. It is not the same thing as an application SLO, and percentages cannot simply be copied into an end-to-end availability promise. Model serial dependencies and validate the resulting design against business risk.

---

# 2. Migrate SAP workloads to Azure (25–30%)

## Discover and size the source landscape

Inventory at least:

- SAP SIDs, products, versions, enhancement packs, kernels and Unicode state;
- database engines, versions, size, growth, compression and largest tables;
- OS versions, CPU, memory, SAPS, IOPS, throughput and latency at peak and batch windows;
- application servers, central services, shared filesystems and print services;
- interfaces, RFCs, IDocs, middleware, file transfers, jobs and external dependencies;
- identity sources, service accounts, certificates, secrets and license servers;
- existing HA, backup, restore, DR, monitoring and operational procedures;
- change freezes, business blackout periods, cutover duration and acceptable data loss.

Do not size from average CPU alone. SAP application tiers are commonly reasoned about with SAPS; HANA sizing is memory-led and also constrained by certified VM and storage combinations. Database and application sizing are separate. Include growth, failover capacity, maintenance headroom, nonproduction demand, storage throughput and VM-level I/O limits.

The [SAP deployment planning guide](https://learn.microsoft.com/en-us/azure/virtual-machines/workloads/sap/planning-guide) explains the Azure infrastructure considerations, while the SAP quick sizing process and current support notes supply workload-specific inputs.

### Quotas, capacity, licensing, support and cost

Before committing to a region and zone, validate:

- subscription vCPU and VM-family quotas;
- actual SKU capacity in the required zones—not just nominal regional availability;
- disk, network-interface, IP, load-balancer and storage limits;
- Azure and SAP licensing, OS subscription and marketplace image terms;
- Azure support plan plus Microsoft/SAP/partner escalation responsibilities;
- reserved-capacity or savings-plan eligibility and utilization risk;
- cross-zone, cross-region, ExpressRoute, backup, logging and egress charges.

**VERIFY CURRENT:** prices, quotas, VM availability, reservation rules, licensing, service SLAs and support-plan entitlements at design and again before cutover.

## Choose the target and migration pattern

| Pattern | What changes | When it fits | Principal risk |
|---|---|---|---|
| Lift and shift / rehost | Infrastructure location; application platform stays substantially the same | Supported source stack, tight transformation scope | Carries technical debt and may not exploit HANA/cloud capabilities |
| Lift, shift and migrate | Infrastructure plus OS or database platform transformation | Source combination is unsupported or strategic replatforming is required | More test scope and cutover complexity |
| Lift, shift and migrate to HANA | Infrastructure plus database move to HANA | S/4HANA or HANA strategy is already justified | Conflates cloud move and major data-platform change |
| Rearchitect/new implementation | New SAP design and migration of required processes/data | Business transformation permits redesign | Largest organizational and validation scope |

Homogeneous migration retains the OS/database platform family; heterogeneous system copy changes it. SAP Software Provisioning Manager, database-native backup/restore or replication, Database Migration Option (DMO), DMO with System Move, Near-Zero Downtime techniques, Azure Site Recovery, Data Box, and partner tools solve different parts of the problem. Select them from platform compatibility, data volume, bandwidth, change rate, downtime, rollback and supportability—not from familiarity alone.

> **Related item:** Network transfer time is only part of downtime. Export/import, log catch-up, technical post-processing, interface changes, validation, business sign-off and rollback decision time often dominate the cutover critical path.

## Build a migration factory

Group systems into waves by dependency and risk rather than moving isolated servers:

1. establish governance, connectivity, identity, management and security in the SAP landing zone;
2. run representative technical proof-of-concept migrations;
3. move lower-risk development and quality systems;
4. rehearse production with current data volume and measured timings;
5. execute cutover with entry/exit criteria and a protected rollback point;
6. validate infrastructure, database, SAP transactions, interfaces, jobs, monitoring and backup;
7. stabilize before decommissioning the source.

The [Cloud Adoption Framework SAP plan](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/sap/plan) distinguishes rehost, replatform and rearchitect decisions. The [SAP landing-zone guidance](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/sap/ready) provides the platform context.

## Design the management hierarchy and controls

Map management groups, subscriptions, resource groups and resource ownership to policy scope, billing, quotas, blast radius, lifecycle and separation of duties. Avoid a resource-group structure based only on the visual SAP diagram: resources that must be deployed, authorized, protected and retired together are better lifecycle boundaries.

Use:

- Microsoft Entra groups and least-privilege Azure RBAC;
- privileged identity management and time-bound elevation where licensed;
- managed identities for Azure automation where supported;
- Azure Policy for required tags, regions, SKUs, diagnostics and security posture;
- resource locks where they reduce accidental deletion without blocking required automation;
- workload identities, SAP authorization concepts and SaaS federation as distinct control planes.

An Azure role does not grant an SAP authorization, and an SAP role does not grant Azure control-plane rights. Document both sides plus the identities used by connectors, backups, monitoring, deployment pipelines and LaMa.

For SAP applications hosted in Azure, distinguish OS/domain authentication, database authentication, SAP users/roles, and Microsoft Entra integration. For SAP SaaS, the organization normally configures an enterprise application and the vendor-supported SAML or OpenID Connect federation, claim/group mapping, conditional access, certificate rollover, break-glass access, and—when supported—SCIM or another provisioning lifecycle. Test sign-in and deprovisioning; successful federation does not prove that SAP authorizations are correct.

## Integrate RISE with SAP

In RISE with SAP on Azure, SAP owns and operates the RISE subscription and its resources; the customer owns its connected Azure estate. The [RISE integration guidance](https://learn.microsoft.com/en-us/azure/sap/workloads/rise-integration) makes that boundary central.

Design:

- customer-to-RISE connectivity, routing, DNS and firewall ownership;
- address-space nonoverlap and resilient on-premises paths;
- identity federation, application SSO and privileged access;
- integration with data, archive, monitoring and security services in customer subscriptions;
- incident triage based on whether the failing resource is SAP-managed or customer-managed;
- throughput, latency, egress and compliance for every cross-boundary flow.

Do not assume that you can inspect or change the Azure resources inside SAP’s subscription. Contractual service, change and support processes are part of the technical design.

### Migration failure modes

| Symptom | Likely design gap | Evidence to collect |
|---|---|---|
| Target is under-sized at peak | Averages substituted for workload/SAPS and memory evidence | Source peak metrics, SAP sizing output, VM/storage limits |
| Cutover exceeds window | Transfer time modeled without post-processing and validation | Timed rehearsal phase log and dependency map |
| System works but interfaces fail | DNS, route, certificate, allowlist or source-IP changes omitted | Packet/DNS traces, interface inventory, certificate chain |
| Deployment blocked | Quota or zonal SKU capacity checked too late | Quota state, capacity reservation/availability evidence |
| RISE incident loops between teams | Responsibility boundary and first-call routing not documented | Resource ownership, contract and triage matrix |

### Primary references

- [SAP on Azure supported products](https://learn.microsoft.com/en-us/azure/sap/workloads/supported-product-on-azure)
- [Cloud Adoption Framework plan for SAP](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/sap/plan)
- [Azure landing zone for SAP](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/sap/ready)
- [Integrate Azure with SAP RISE managed workloads](https://learn.microsoft.com/en-us/azure/sap/workloads/rise-integration)

---

# 3. Design and implement infrastructure (25–30%)

## Choose certified compute

Start from required SAPS and database memory, then filter to current certified VM/OS/database combinations. Finally test region, zone, quota, storage throughput, network bandwidth, maintenance behavior and cost. A VM with enough vCPU or memory is not automatically SAP-certified.

| Decision | Validate |
|---|---|
| Application-server VM | SAPS, CPU/memory ratio, horizontal scale, network/disk bandwidth, constrained-vCPU support |
| HANA VM | HANA hardware-directory certification, memory, OS release, scale-up/scale-out support, storage configuration |
| AnyDB VM | SAP Note support, database vendor support, HA framework and storage layout |
| Image | Marketplace support, update entitlement, cloud-init/agent behavior, hardening and repeatability |
| Custom image | Generalization, patch provenance, extensions, secrets removed and ongoing image lifecycle |

Install and validate the [Azure VM extension for SAP solutions](https://learn.microsoft.com/en-us/azure/sap/workloads/vm-extension-for-sap) when required by the supported design. Treat extension version, connectivity, SAP Host Agent and kernel prerequisites as current vendor facts.

Use a supported Azure Marketplace image when its publisher, OS release and entitlement fit the certified combination. If a custom image is required, build it from a controlled source, patch and harden it, remove host-specific state and secrets, generalize it correctly, version it in Azure Compute Gallery, and test that agents/extensions and SAP prerequisites initialize after deployment. Rebuild instead of manually repairing drifted clones.

> **Related item:** Proximity placement groups can reduce latency by influencing colocation, but they can constrain capacity and conflict with zone-spanning goals. Measure latency and availability requirements before choosing placement mechanics.

## Design networking from flows

Create a flow matrix with source, destination, protocol/port, DNS name, expected address, route, security control, throughput, latency, owner and evidence. Cover:

- user and application access to SAP entry points;
- application-to-central-services and application-to-database flows;
- HANA System Replication, cluster heartbeat and fencing paths;
- SAProuter, Web Dispatcher, interfaces, printers and batch transfers;
- Microsoft Entra, Key Vault, Azure management, monitoring, backup and repository endpoints;
- on-premises, partner, RISE and DR-region connectivity.

Use Accelerated Networking on supported SAP VMs. Design ExpressRoute for required bandwidth and resilience, including provider/peering location, redundant circuits or paths, gateway resiliency, BGP, route filtering, DNS and failover. VPN can be a primary or fallback path only when its measured performance and failure behavior satisfy requirements.

NSGs filter flows but do not provide application-aware inspection. Azure Firewall or a supported NVA may centralize inspection; UDRs must preserve symmetric, supported paths. Private endpoints change DNS as well as routing. Document forced tunneling, egress identity, service tags, FQDN dependencies and return paths.

For Azure Storage, a service endpoint keeps the service's public endpoint but lets its firewall recognize the selected subnet; a private endpoint places a private IP for the service subresource in the VNet and requires correct private DNS. Neither is an SAP authorization mechanism. Choose from exposure, routing, DNS, cross-network access and current storage/SAP support requirements.

The [SAP planning guide](https://learn.microsoft.com/en-us/azure/virtual-machines/workloads/sap/planning-guide) recommends validating Accelerated Networking and enterprise connectivity for SAP VMs.

## Choose and lay out storage

Separate capacity, IOPS, throughput, latency, durability, filesystem/protocol, sharing and recovery requirements for:

- OS and SAP binaries;
- database data, log, shared and backup areas;
- SAP global, transport and interface files;
- staging and archive data.

For HANA, design `/hana/data`, `/hana/log`, `/hana/shared` and `/usr/sap` from current supported configurations. The transaction log latency path differs from the data-volume throughput path. Disk striping aggregates performance but also changes the failure and operational unit. Host caching and Write Accelerator are workload-, disk-, and SKU-dependent choices.

The current [HANA VM storage guidance](https://learn.microsoft.com/en-us/azure/sap/workloads/hana-vm-operations-storage) lists Premium SSD, Premium SSD v2, Ultra Disk and Azure NetApp Files among certified options, with important mixing, filesystem and throughput constraints. Azure Files and Azure NetApp Files serve different shared-storage requirements. Verify protocol, regional availability, service level, delegated subnet, proximity, backup and replication behavior.

**VERIFY CURRENT:** supported storage combinations, VM/disk limits, bursting, caching, Write Accelerator, shared-disk, Azure Files and Azure NetApp Files behavior.

## Encrypt and protect data

Distinguish:

- platform-managed versus customer-managed encryption keys;
- encryption at host, managed-disk encryption and database-native encryption;
- TLS for application, database, backup, monitoring and replication flows;
- key availability, rotation, access, purge protection and regional recovery;
- backup immutability and separation of duties.

Encryption is a dependency in recovery. A backup without the required keys, certificates, credentials or catalog is not recoverable.

## Automate repeatable deployment

ARM templates and Bicep describe Azure resources; OS/database/SAP configuration needs additional automation. Microsoft’s [SAP Deployment Automation Framework](https://learn.microsoft.com/en-us/azure/sap/automation/tutorial) uses a control plane, workload zones and system deployments, with Terraform and Ansible. [Azure Center for SAP solutions](https://learn.microsoft.com/en-us/azure/sap/center-sap-solutions/overview) offers guided deployment plus registration and management through a Virtual Instance for SAP solutions (VIS).

| Approach | Best fit | Watch for |
|---|---|---|
| Bicep/ARM | Organization-owned Azure resource patterns | SAP/OS installation and day-2 configuration remain separate |
| SAP Deployment Automation Framework | Repeatable enterprise SAP landing zones and systems | Control-plane security, state, parameters, versioning and pipeline ownership |
| Azure Center for SAP solutions | Guided supported patterns and a unified SAP management resource | Current supported topologies, regions, software and permissions |
| Manual deployment | Constrained proof of concept or diagnosis | Drift, weak repeatability and undocumented decisions |

Make parameters, state, secrets, approvals and generated artifacts explicit. Validate before deployment, lint templates, test idempotence and protect state. Do not embed credentials or SAP media entitlements in source control.

### Infrastructure failure modes

| Symptom | Likely cause | Check first |
|---|---|---|
| Certified VM cannot be deployed | Zone capacity or quota, not certification | SKU availability by zone and family quota |
| HANA latency remains high | Layout exceeds disk or VM caps; cache/striping mismatch | Disk and VM metrics, HANA tools, supported layout |
| HA IP does not respond | Load-balancer probe/rule or cluster resource mismatch | Probe port, frontend, floating IP, listener and cluster state |
| Private storage name resolves publicly | Private DNS zone/link/forwarding gap | Answer from the workload VM and DNS query path |
| Automation differs by environment | Mutable images, unversioned parameters or manual post-steps | Pipeline artifacts, state and configuration drift |

### Primary references

- [Plan and implement an SAP deployment on Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/workloads/sap/planning-guide)
- [SAP HANA VM storage configurations](https://learn.microsoft.com/en-us/azure/sap/workloads/hana-vm-operations-storage)
- [Azure Center for SAP solutions overview](https://learn.microsoft.com/en-us/azure/sap/center-sap-solutions/overview)
- [SAP Deployment Automation Framework enterprise tutorial](https://learn.microsoft.com/en-us/azure/sap/automation/tutorial)

---

# 4. Design and implement HA and DR (20–25%)

## Keep HA, DR and backup distinct

| Capability | Protects mainly against | Typical scope | Does not by itself provide |
|---|---|---|---|
| High availability | Host, process, zone or component failure | One region | Recovery from corruption or regional loss |
| Disaster recovery | Regional/site loss or prolonged outage | Second region/site | Historical recovery from logical corruption |
| Backup | Deletion, corruption and point-in-time recovery | Recovery store/vault | Fast automatic application failover |

Define RPO and RTO per business process, then map each SAP layer and dependency to a mechanism. Include identity, DNS, network, keys, images, automation, shared storage, interfaces and monitoring—not only VMs and the database.

## Design in-region high availability

Availability Sets separate fault/update domains within a datacenter construct; Availability Zones separate physical locations within a region. A zone-spanning design can improve fault isolation but adds cross-zone latency, traffic cost and zonal dependency requirements. The [SAP availability-zone guidance](https://learn.microsoft.com/en-us/azure/sap/workloads/high-availability-zones) recommends measuring latency with representative SKUs and SAP `niping`, not assuming zone numbers or using ordinary ping as proof.

Protect each singleton:

- deploy redundant application servers;
- cluster ASCS/SCS with ERS on a supported Pacemaker or Windows Server Failover Clustering pattern;
- use a supported load-balancer/virtual-name design;
- use HANA System Replication, SQL Server Always On or another supported database-native HA pattern;
- select a supported shared-storage design;
- validate quorum and fencing under partition, loss and maintenance conditions.

For SQL Server, distinguish an Always On availability group from a failover cluster instance and use only the SAP-, Microsoft-, OS- and storage-supported pattern. For central-services shared state, storage-level replication is valid only where the chosen SAP/OS architecture documents it; shared managed disks, Azure Files, Azure NetApp Files and replicated local filesystems are not interchangeable.

The [SAP HA architecture guidance](https://learn.microsoft.com/en-us/azure/sap/workloads/sap-high-availability-architecture-scenarios) describes redundancy across application, central-services and database components.

## Understand fencing and split brain

Pacemaker decides resource ownership; STONITH/fencing prevents a failed or isolated node from continuing to write. An Azure fence agent powers off or controls the node through Azure APIs; SBD uses a shared block device and watchdog semantics. The exact supported combination depends on OS, SAP component, storage and topology.

Test more than graceful failover:

- process failure;
- VM loss and host maintenance;
- network partition and loss of quorum;
- database replication break or excessive lag;
- load-balancer probe failure;
- fencing identity/API failure;
- restoration of the old primary without dual ownership.

> **Related item:** Automatic failover is unsafe when the cluster cannot prove that the previous owner is fenced. Availability is not improved by allowing two primaries to corrupt shared state.

## Design regional disaster recovery

The [SAP DR guidance](https://learn.microsoft.com/en-us/azure/sap/workloads/disaster-recovery-sap-guide) separates database, non-database and backup choices. A common pattern uses asynchronous database-native replication across regions and Azure Site Recovery or reproducible deployment for non-database VMs. It is not universally valid: current support matrices, database behavior, change rate, storage and RPO/RTO decide.

For Azure Site Recovery, inventory supported OS/disks, churn limits, target networking, capacity, encryption, agents/extensions and application-consistency requirements. Map recovery plans to SAP dependency order and automation, but keep database-native replication and cluster ownership authoritative where the supported database design requires them. A test failover should use an isolated network and must not accidentally advertise production DNS or start a competing primary.

Plan recovery order:

1. incident declaration, authority and change freeze;
2. identity, DNS, connectivity, routing, firewall and keys;
3. required storage and shared services;
4. database promotion or restoration with data-loss decision;
5. central services and enqueue recovery;
6. application servers and entry points;
7. interfaces, jobs and downstream integrations;
8. technical checks, business transactions and formal service acceptance.

Design failback while designing failover. Record how to protect changes made in the recovery region, reverse replication, reconcile DNS/routes and avoid an unplanned second outage.

The same dependency discipline applies to routine restart. Stop inbound work and scheduled jobs, drain application activity, stop application instances, central services and the database in the supported order; start the database and required shared/central services before application instances and entry points, validating at every gate. Exact commands and sequence remain system-specific.

## Backup and restore

Back up all required layers and catalogs. Database-consistent backups are different from VM crash-consistent recovery points. For HANA, Azure Backup integrates through Backint and supports documented HANA/HSR scenarios; the [HANA backup guidance](https://learn.microsoft.com/en-us/azure/backup/sap-hana-database-with-hana-system-replication-backup) is the current source for topology and vault limitations.

For each policy define:

- full/differential/incremental/log or snapshot behavior;
- frequency, retention, immutable or soft-delete controls;
- vault region/subscription and administrative separation;
- encryption-key and catalog recovery;
- restore target prerequisites and network access;
- evidence from scheduled restore tests.

A green backup job proves collection, not recoverability. Measure restore throughput and full application validation time.

## Recovery test scorecard

| Measure | Evidence |
|---|---|
| Achieved RPO | Last usable transaction/log timestamp against incident time |
| Achieved RTO | Declaration-to-business-acceptance timeline |
| Data consistency | Database and SAP consistency checks plus interface reconciliation |
| Isolation | Proof that old primary cannot serve or write |
| Dependency completeness | DNS, identity, routes, certificates, integrations and schedulers tested |
| Repeatability | Runbook deviations, automation logs, owners and corrective actions |

### Primary references

- [SAP high-availability architecture and scenarios](https://learn.microsoft.com/en-us/azure/sap/workloads/sap-high-availability-architecture-scenarios)
- [SAP workload configurations with Availability Zones](https://learn.microsoft.com/en-us/azure/sap/workloads/high-availability-zones)
- [Disaster-recovery recommendations for SAP](https://learn.microsoft.com/en-us/azure/sap/workloads/disaster-recovery-sap-guide)
- [Back up HANA System Replication with Azure Backup](https://learn.microsoft.com/en-us/azure/backup/sap-hana-database-with-hana-system-replication-backup)

---

# 5. Maintain SAP workloads on Azure (20–25%)

## Observe by layer and business service

Azure Monitor resource metrics alone cannot prove SAP health. Combine:

- Azure activity, resource health, VM, disk, storage, network and load-balancer telemetry;
- guest OS, filesystem, process and cluster telemetry;
- database capacity, latency, backup and replication state;
- SAP application, work process, queue, lock, job and transaction evidence;
- synthetic business transactions and interface health.

[Azure Monitor for SAP solutions](https://learn.microsoft.com/en-us/azure/sap/monitor/about-azure-monitor-sap-solutions) collects data through configured providers for components such as HANA, NetWeaver, SQL Server and Pacemaker into Azure Monitor Logs. Use workbooks for correlation and alerts for actionable symptoms; protect provider credentials and monitor the monitoring path itself.

Azure Network Watcher supports topology and packet-path investigation, but SAP-specific tools and database/OS evidence remain necessary. Time synchronization, consistent naming and correlated change records are prerequisites for useful incident timelines.

## Operate with Azure Center for SAP solutions

A VIS is a logical Azure representation of an SAP SID and its central services, database and application instances. Depending on support and registration, Azure Center for SAP solutions can show health and metadata, quality checks, infrastructure metrics, costs, and start/stop operations.

Do not confuse a VIS with the actual SAP resources or with SAP-native authorization. Validate prerequisites, managed-identity/RBAC scope, supported systems and effects before registration or automation.

## Optimize performance and cost

Use evidence in this order:

1. confirm business and recovery requirements;
2. find the bottleneck—CPU, memory, storage, network, lock/contention, code or dependency;
3. check current SAP/Microsoft support boundaries;
4. change one controlled factor;
5. measure business and platform results;
6. retain rollback evidence.

Cost levers include rightsizing, application-server elasticity, scheduled nonproduction shutdown, reserved instances or savings plans, storage selection, backup retention, archive/data aging and removal of unused resources. Do not compromise certified sizing, failover headroom or RTO merely to improve a cost dashboard.

Archiving and HANA data aging can reduce hot working-set and premium-storage demand, but they change retrieval paths, retention controls and recovery dependencies. Measure business response, interface behavior, archive availability and compliance before treating data movement as a performance improvement.

**VERIFY CURRENT:** recommendation scope in Azure Advisor, pricing commitments, ACSS capabilities, Azure Monitor for SAP provider support and storage-tier economics.

## Start, stop and landscape automation

Start and stop in dependency order. A simplified stop sequence moves from entry points and jobs through application servers and central services to the database; start usually reverses it, with validation gates. Actual sequences depend on the SAP design.

[SAP LaMa’s Azure connector](https://learn.microsoft.com/en-us/azure/sap/workloads/lama-installation) can use an Azure service principal or managed identity to manage permitted resources. Prefer managed identities when supported, constrain RBAC scope, protect against concurrent automation and test storage-tier or VM lifecycle actions.

## Operational failure modes

| Symptom | First distinction | Evidence |
|---|---|---|
| Slow dialog response | SAP/application contention versus infrastructure saturation | SAP response breakdown, DB waits, CPU, memory, disk and network |
| HANA replication lag | Network/throughput limit versus database workload | HSR state, log generation, latency, bandwidth and storage metrics |
| Cluster alert without outage | Monitoring/provider failure versus cluster degradation | Pacemaker state, provider health, Log Analytics ingestion |
| Cost spike | Demand growth versus idle/oversized resources or data transfer | Cost dimensions, utilization, topology and reservation coverage |
| Backup succeeds but restore misses RTO | Restore never tested at production scale | Timed restore and end-to-end SAP validation log |

### Primary references

- [Azure Monitor for SAP solutions](https://learn.microsoft.com/en-us/azure/sap/monitor/about-azure-monitor-sap-solutions)
- [Azure Center for SAP solutions](https://learn.microsoft.com/en-us/azure/sap/center-sap-solutions/overview)
- [SAP LaMa connector for Azure](https://learn.microsoft.com/en-us/azure/sap/workloads/lama-installation)
- [SAP HANA Azure VM storage operations](https://learn.microsoft.com/en-us/azure/sap/workloads/hana-vm-operations-storage)

---

# 6. Integrated scenarios

## Scenario A: ECC on AnyDB to S/4HANA on Azure

The source is a large on-premises ECC landscape with a non-HANA database, several interfaces and a strict weekend outage window.

Reason through it:

1. **Compatibility:** establish SAP-supported source/target paths, required maintenance levels and conversion prerequisites.
2. **Sizing:** use measured workload plus SAP sizing for application SAPS and HANA memory; include growth and failover.
3. **Pattern:** recognize that moving to Azure and changing to S/4HANA/HANA expands the transformation and test surface beyond rehost.
4. **Landing zone:** complete subscriptions, policy, identity, ExpressRoute, DNS, security, backup and monitoring before migration.
5. **Migration:** select supported DMO/system-move or partner tooling from data size, bandwidth and downtime; rehearse with production-scale copies.
6. **Availability:** design ASCS/ERS, application-server redundancy, HANA System Replication, fencing and zonal behavior.
7. **Cutover:** time every technical and business step, define rollback criteria and validate interfaces and critical transactions.
8. **Operations:** confirm backup restore, monitoring, capacity, support routing and DR before ending hypercare.

The wrong shortcut is to select a large HANA VM and treat the project as a server copy. Application conversion, data consistency, interfaces, business validation and operating-model change remain critical.

## Scenario B: RISE private edition integrated with customer Azure

SAP operates S/4HANA in its Azure subscription. The customer operates data integration, identity and other applications in its own landing zone.

1. Draw the ownership boundary and record support contacts.
2. Allocate nonoverlapping address spaces and choose supported redundant connectivity.
3. Design DNS and routing in both directions; list every required port and owner.
4. Federate identities and separate application SSO from Azure control-plane RBAC.
5. Place archive/data/security services in the appropriate customer subscriptions and use private connectivity where required.
6. Define which side monitors each hop and which evidence accompanies an incident.
7. Test loss of one path, DNS failure, certificate rollover, throughput and business transactions.

The customer cannot fix a SAP-managed resource by granting itself more Azure rights. The operating contract is part of the architecture.

## Scenario C: Region-loss tabletop

A zone-resilient SAP production system must recover to another region after a prolonged regional outage.

1. Verify that the scenario exceeds local HA scope and triggers the DR authority.
2. Determine the last usable database recovery point and get business acceptance of potential data loss.
3. restore or activate network, DNS, identity, security, keys and shared services;
4. promote/restore the database and prove the old primary cannot write;
5. start central services, application servers, entry points and interfaces in order;
6. validate technical consistency and named business transactions;
7. record achieved RPO/RTO and plan controlled failback.

Do not declare success when the Azure VMs are running. Success is business acceptance with reconciled data and dependencies.

---

# 7. Hands-on labs

These labs are independent. Use diagrams and tabletop evidence where a real SAP system or large VM is not available.

## Lab 1 — Source inventory and target decision

Create a fictional three-system SAP landscape. Record SIDs, tiers, OS/database, size, growth, SAPS, memory, interfaces, RPO/RTO and downtime. Produce a target option matrix for rehost, replatform and HANA conversion. Cite the support evidence you would need before approval.

**Evidence:** inventory, dependency graph, assumptions, option scorecard and unresolved support questions.

## Lab 2 — SAP landing-zone design

Design management groups, subscriptions, resource groups, Entra groups, RBAC, policy, naming, DNS, ExpressRoute and monitoring for production and nonproduction. Add an ownership/RACI table and explain why each scope is a lifecycle or control boundary.

**Evidence:** annotated diagram, flow matrix, role matrix and five tested policy rules.

## Lab 3 — Certified compute and storage workbook

Given application SAPS and HANA memory/storage requirements, build a workbook that filters candidate VM and storage configurations through certification, region/zone capacity, quotas, VM I/O limits, storage throughput, latency and HA headroom. Do not claim a final supported SKU without current SAP evidence.

**Evidence:** calculations, source links, eliminated options, risks and verification date.

## Lab 4 — Deployment automation review

Inspect the public SAP Deployment Automation Framework samples. Trace control plane, workload zone and SAP system parameters; identify state, secrets and approval boundaries. Compare the result with a Bicep-only approach and ACSS guided deployment.

**Evidence:** component diagram, pipeline gates, secret/state controls and rollback plan.

## Lab 5 — Packet and DNS walk

Trace a user-to-Fiori flow, application-to-HANA flow, HSR flow and Azure Backup/Monitor flow. For both directions record DNS answer, addresses, route, NSG/firewall, translation/load balancer, listener and observable evidence. Introduce one DNS and one asymmetric-route fault.

**Evidence:** before/after traces and first-failing-layer diagnosis.

## Lab 6 — HA failure matrix

Model ASCS/ERS and HANA clusters. Test or tabletop process loss, node loss, probe failure, network partition, quorum loss and fence-agent failure. State the safe owner after each event and why split brain is prevented.

**Evidence:** failure matrix, cluster state, fencing proof and corrective actions.

## Lab 7 — Regional DR rehearsal

Write an ordered regional recovery runbook for network/DNS, keys, database, central services, application servers and interfaces. Run a timed tabletop, inject stale replication and a missing certificate, then calculate achieved RPO/RTO.

**Evidence:** timeline, decision log, validation checklist, data-loss approval and failback outline.

## Lab 8 — Operations and cost review

Design a workbook/alert set that correlates Azure, OS, cluster, database and SAP signals. Add backup restore evidence, a nonproduction start/stop schedule and three cost improvements that retain certified performance and recovery headroom.

**Evidence:** signal-to-action table, restore report, automation controls and before/after cost assumptions.

---

# 8. Knowledge checks

Answer in your own words before opening the answers.

1. Why is enough vCPU and memory insufficient evidence that a VM is valid for SAP HANA?
2. What is the difference between application SAPS sizing and HANA memory sizing?
3. When does a migration become a heterogeneous system copy rather than a rehost?
4. Why must a cutover rehearsal include business validation and interfaces?
5. Which control planes govern Azure resources and SAP application access?
6. What changes in the responsibility model for RISE with SAP?
7. Why should zonal VM availability be tested before finalizing an architecture?
8. Why can disk-level throughput still be poor when each disk meets its own target?
9. What problem does Accelerated Networking address for SAP?
10. How do private endpoints create a DNS requirement?
11. What is the difference between application-server redundancy and central-services HA?
12. Why is fencing required in a clustered singleton design?
13. How do synchronous and asynchronous replication typically map to HA and DR?
14. Why is backup not a substitute for HA?
15. What proves that a backup meets the application RTO?
16. Which dependencies normally recover before the SAP database and application?
17. What does a Virtual Instance for SAP solutions represent?
18. How does SAP Deployment Automation Framework divide deployment scope?
19. Why can stopping an SAP VM directly be unsafe?
20. What is the role of Azure Monitor for SAP solutions providers?
21. Why can Azure Advisor alone not justify rightsizing a production SAP VM?
22. What must a supportability record contain?
23. What makes a DR test complete?
24. Which facts in this guide should always be reverified?

## Answers

1. SAP HANA requires an exact certified VM, OS and supported configuration; raw capacity alone does not establish supportability.
2. SAPS characterizes application transaction throughput, while HANA sizing is memory-led and must also satisfy certified compute/storage performance.
3. It becomes heterogeneous when the OS/database platform changes, requiring supported migration tooling and a broader validation scope.
4. Infrastructure completion does not prove that transactions, jobs, interfaces and reconciled data work within the outage window.
5. Microsoft Entra/Azure RBAC governs Azure control-plane access; SAP identities and authorizations govern SAP application access.
6. SAP owns and operates the RISE subscription/resources, while the customer owns connected Azure resources and the integration boundary is shared.
7. A certified SKU may lack quota or physical capacity in the required zone, invalidating placement and recovery assumptions.
8. The aggregate workload can hit the VM’s total IOPS/throughput cap, or the layout/cache/queue can be wrong.
9. It reduces virtualization overhead and improves supported VM network performance/latency.
10. The service name must resolve to the private endpoint address from every intended client through the correct private-zone/forwarding path.
11. Application servers can usually scale horizontally; ASCS/SCS is a singleton service requiring a supported cluster, name/IP and state design.
12. It prevents an isolated former owner from continuing to write and causing split brain or corruption.
13. Low-latency synchronous replication commonly supports in-region HA; asynchronous replication accommodates cross-region latency for DR at a nonzero RPO.
14. Backup requires detection and restore and therefore does not automatically preserve service during component failure.
15. A timed restore plus complete SAP and business validation at representative scale.
16. Decision authority, identity, DNS, connectivity, routing, security, keys and required storage/shared services.
17. A logical Azure representation of an SAP system/SID and its central-services, database and application instances.
18. Into control-plane/management components, workload zones and individual SAP system deployments, followed by configuration/install workflows.
19. SAP dependencies, jobs, database consistency and cluster ownership require an ordered, application-aware sequence.
20. Providers collect component-specific data such as HANA, NetWeaver, SQL Server or Pacemaker signals into Azure Monitor Logs.
21. Rightsizing must preserve SAP certification, peak workload, HA capacity, recovery targets and current support constraints.
22. Exact product/kernel/database/OS/VM/storage/HA combination, relevant SAP/Microsoft sources, decision owner and verification date.
23. Measured RPO/RTO, proven isolation, recovered dependencies, data consistency, technical and business acceptance, deviations and a failback plan.
24. Certification/support matrices, SAP Notes, versions, regional/zonal availability, quotas, SKUs, limits, pricing, licensing, SLA and preview/retirement status.

---

# 9. Final review checklist

- [ ] I can map all four official domains and every subobjective to a section or lab.
- [ ] I start with SAP product/version/support evidence and measured requirements.
- [ ] I distinguish SAPS, HANA memory, storage performance and VM-level limits.
- [ ] I can compare rehost, replatform, HANA conversion and new implementation.
- [ ] I can explain landing-zone, identity, governance and RISE ownership boundaries.
- [ ] I can design SAP network flows, DNS, ExpressRoute, security and private access.
- [ ] I can select certified compute, images and supported storage without guessing.
- [ ] I can compare Bicep/ARM, SAP Deployment Automation Framework and ACSS.
- [ ] I distinguish HA, DR and backup and can explain fencing and recovery order.
- [ ] I can correlate Azure, OS, cluster, database and SAP monitoring evidence.
- [ ] I can optimize cost without removing performance or recovery headroom.
- [ ] I have completed architecture, HA/DR and operations exercises with evidence.

---

# Places to learn

This is **not a complete list**, and it is not a recommendation to consume everything. Pick the combination that fits how you learn and use the official April 17, 2026 objective list as the coverage checklist. Time estimates are planning ranges, not vendor promises; pause-and-practice time is included where useful. Verify subscription access, course freshness and exact duration before purchase.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official AZ-120 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-120) | Free; authoritative objectives and update history | 45–75 min initially; 10–15 min before exam |
| [Microsoft Learn AZ-120 course](https://learn.microsoft.com/en-us/training/courses/az-120t00/) | Free self-paced paths; instructor-led delivery may be paid; official page lists 3 days | About 29 hr displayed path content; plan 38–55 hr with notes and exercises |
| [SAP on Azure training videos](https://learn.microsoft.com/en-us/shows/sap-on-azure-training-videos/) | Free Microsoft technical video series | Pick relevant episodes; plan 2–6 hr |
| [Pluralsight: SAP on Azure—The Big Picture](https://www.pluralsight.com/courses/sap-azure-big-picture) | Subscription/trial; Steve Buchanan; updated June 2026 | 1 hr 28 min video; plan 2–3 hr |
| [Pluralsight: Building and Deploying Azure for SAP Workloads](https://www.pluralsight.com/courses/building-deploying-azure-sap-workloads) | Subscription/trial; Tim Warner; updated June 2026 | 2 hr 52 min video; plan 4–6 hr |
| [Pluralsight: Designing and Implementing Azure Infrastructure to Support SAP Workloads](https://www.pluralsight.com/courses/azure-infrastructure-designing-implementing-sap-workloads-cert) | Subscription/trial; Steve Buchanan; updated June 2026 | 1 hr 14 min video; plan 2–3 hr |
| [Pluralsight: Designing and Implementing HA/DR for SAP Workloads](https://www.pluralsight.com/courses/azure-sap-workloads-designing-implementing-ha-disaster-recovery-cert) | Subscription/trial; Roosevelt Wilmot; updated June 2026 | 1 hr 12 min video; plan 2–3 hr |
| [O'Reilly: SAP on Azure Implementation Guide](https://www.oreilly.com/library/view/sap-on-azure/9781838983987/) | Subscription/book; 2020 Packt title, useful for durable SAP architecture and migration context but pre-dates current objectives and services | 242 pages / 6 hr 56 min displayed; plan 10–16 hr plus current-doc reconciliation |
| [Udemy: AZ-120 Microsoft Azure for SAP Workloads Exam Preparation](https://www.udemy.com/course/microsoft-azure-for-sap-workloads-az-120-exam-preparation/) | Paid; ReTeam Labs; 5 hr 42 min; last updated September 2021 | Plan 8–12 hr and verify every service/objective against 2026 sources |
| [MeasureUp AZ-120 practice test](https://www.measureup.com/microsoft-practice-test-az-120-planning-and-administering-microsoft-azure-for-sap-workloads.html) | Paid practice test | Plan 3–6 hr across baseline, review and retest |

The official credential page did not offer a free Microsoft Practice Assessment for AZ-120 during the August 31, 2026 review. Do not substitute remembered or leaked exam questions for learning. Use legitimate practice questions to expose reasoning gaps, then return to the official documentation and a lab or tabletop exercise.

## Suggested routes

### SAP professional newer to Azure

1. Azure administrator/networking/storage prerequisites.
2. Microsoft Learn course and Big Picture course.
3. Infrastructure plus HA/DR Pluralsight courses.
4. Labs 2–8 and current Microsoft/SAP support documents.
5. Legitimate practice test, gap review and retest.

**Planning range:** 70–110 hours, excluding prerequisite Azure training.

### Azure architect newer to SAP

1. Formal SAP HANA/NetWeaver and Basis fundamentals before exam preparation.
2. Microsoft Learn course with emphasis on SAP tiers, SAPS, support notes and migration.
3. Build decision workbooks and complete all eight labs/tabletops.
4. Review current SAP support sources with an experienced SAP practitioner.

**Planning range:** 90–140 hours after SAP prerequisites; reading Azure service summaries cannot replace SAP experience.

### Experienced SAP-on-Azure practitioner

1. Diff the April 17, 2026 blueprint against current responsibilities.
2. Review RISE, ACSS, SDAF, current storage/HA/backup guidance and changed support notes.
3. Complete Labs 3, 6, 7 and 8; use assessment results to target gaps.

**Planning range:** 30–50 focused hours.

---

## Currency and integrity note

This guide summarizes public material; it does not reproduce exam questions and is not an exam dump. Microsoft and SAP can change objectives, certification status, support notes, VM/storage certification, products, quotas, pricing and service behavior. Recheck the official blueprint, credential page, SAP Notes/hardware directory and linked product documentation before making a production or exam decision.
