---
exam_code: AZ-802
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-802
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# AZ-802 Administering Windows Server Study Guide

> **BETA EXAM:** AZ-802 is currently the beta exam for the [Microsoft Certified: Windows Server Administrator Associate](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-administrator-associate/) credential. Beta objectives, delivery, scoring timelines, training, and provider coverage can change before general availability. Microsoft states that beta results are not immediate. Recheck the official pages before scheduling.

> **REPLACEMENT PATH:** AZ-800 and AZ-801 retire on **September 30, 2026, at 5:00 PM Central Standard Time**. Microsoft states that AZ-802 will remain as the available path after those exams retire. AZ-802 is one consolidated exam; do not assume a partial pass in the old two-exam route transfers automatically.

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#az-802-coverage-record). The [official AZ-802 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-802) is authoritative.

**Current baseline:** Official study-guide page last updated July 6, 2026; Microsoft does not publish a separate “skills measured as of” date on that page.<br>
**Upcoming blueprint change:** None announced, but beta content is inherently subject to change before general availability.<br>
**Certification transition:** AZ-800 and AZ-801 retire September 30, 2026 at 5:00 PM Central Standard Time; AZ-802 is the replacement path.<br>
**Training status:** The direct [AZ-802T00 course page](https://learn.microsoft.com/en-us/training/courses/az-802t00) is live and lists five days. At verification time, the credential page still displayed “No training available,” apparently lagging the course release.<br>
**Practice status:** Microsoft says an AZ-802 Practice Assessment is not currently available and is usually released within eight weeks after an exam leaves beta and becomes generally available.<br>
**Official sources:** [AZ-802 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-802) · [credential and exam page](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-administrator-associate/) · [AZ-802T00 course](https://learn.microsoft.com/en-us/training/courses/az-802t00) · [old-exam retirement list](https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams)

## How to use this guide

Study AZ-802 as one operating model spanning local datacenters, Azure, and connected non-Azure servers. For every task, trace:

```text
identity -> authentication -> authorization
name -> address -> route/firewall -> listener -> application
desired state -> management channel -> local execution -> evidence
workload -> compute -> network -> storage -> availability -> recovery
signal -> collection -> alert -> diagnosis -> repair -> validation
```

The exam is broader than product recognition. You should be able to choose a scope, configure the feature, explain dependencies, identify the first broken layer, make a reversible repair, and prove the user transaction. Build an isolated lab domain plus an authorized Azure sandbox. Azure VMs, Bastion, storage, Arc-connected services, Defender, Monitor, log ingestion, and public IPs can cost money. Never test directory recovery, trust changes, encryption recovery, or production failover merely for study.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, migration, security, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Administrator question |
|---|---:|---|
| Deploy and manage AD DS | 20–25% | Can directory authority, topology, principals, service identities, and policy remain correct across sites and forests? |
| Manage Windows Server instances and workloads in a hybrid environment | 10–15% | Can operators reach, constrain, configure, update, and automate servers through the right local or Azure management plane? |
| Manage virtual machines | 10–15% | Can Hyper-V and Azure VMs run with correct resources, devices, network, storage, availability, and management access? |
| Implement and manage an on-premises and hybrid networking infrastructure | 10–15% | Can clients obtain addresses and resolve authoritative names through resilient, secure on-premises and hybrid paths? |
| Manage storage and file services | 15–20% | Can administrators place, authorize, synchronize, accelerate, protect, and recover file and block data? |
| Secure Windows Server infrastructure | 10–15% | Can host, credential, directory, network, and cloud protection controls prevent, detect, and contain compromise? |
| Monitor and troubleshoot Windows Server environments | 15–20% | Can operators collect useful evidence, isolate the first failed dependency, recover safely, and prove normal service? |

---

## 1. Build the Windows Server operating model

### Separate identity, management, workload, and evidence planes

| Plane | Examples | Question |
|---|---|---|
| Identity | AD DS, Microsoft Entra ID, local accounts, managed identities | Which authority authenticates this actor, and which SID/token reaches the resource? |
| Management | Windows Admin Center, PowerShell/SSH/RDP, Azure Arc, Azure Resource Manager | Which channel requests the change, and where does it execute? |
| Workload | AD DS, SMB, Hyper-V guest, Azure VM application | What must remain available if management is unavailable? |
| Network | DNS, DHCP, routes, NSGs, Windows Firewall, virtual switch | How does the client discover and reach the intended listener? |
| Data | NTFS/ReFS, Azure Files, File Sync, Storage Spaces, managed disks | Which copy is authoritative, cached, replicated, encrypted, or recoverable? |
| Evidence | event logs, counters, agent/extension health, replication, alerts | What proves actual state matches the intended state? |

An Azure VM can show `Running` while the guest is hung. An Arc resource can exist while the Connected Machine agent is disconnected. A GPO can be linked while security filtering prevents application. A DNS record can be correct while the client asks the wrong resolver. Preserve these boundaries when reasoning.

### Use a dependency-first troubleshooting sequence

1. Define the failed transaction, affected scope, exact error, and first/last known-good time.
2. Record recent configuration, update, security, network, or identity changes.
3. Verify local host boot, clock, CPU, memory, disk, service, and event state.
4. Verify address, route, firewall/NSG, listener, and return path.
5. Verify DNS suffix, queried resolver, answer, authority, TTL, and cache.
6. Verify identity authority, ticket/token/certificate, trust, SPN, and time.
7. Verify authorization at Azure, local, share, filesystem, and application layers.
8. Verify agent, extension, policy, sync, replication, cluster, or storage state.
9. Compare with a healthy peer and baseline.
10. Change one reversible item, rerun the original transaction, and retain evidence.

Time is a dependency for Kerberos, certificates, signed tokens, replication, clusters, and log correlation. Establish reliable time before drawing conclusions from timestamps.

> **Related item:** Availability, replication, backup, and disaster recovery solve different problems. AZ-802 includes Hyper-V Replica and S2D/Storage Replica but does not make backup design disappear; operational administrators still need independent tested recovery points.

---

## 2. Deploy and manage AD DS (20–25%)

### Deploy domain controllers locally and in Azure

A domain controller is a security authority, DNS participant, replication partner, and source of policy—not an ordinary server. Before promotion decide:

- forest/domain design and supported functional levels;
- site/subnet mapping, replication links, closest clients, and WAN behavior;
- writable versus RODC, global catalog, DNS, and FSMO placement;
- physical/virtual security and privileged management path;
- system-state/full-server backup and forest-recovery responsibilities;
- Azure region/zone, VNet DNS, availability, disk, route, and dependency design.

Install AD DS, validate static addressing and DNS, promote into the intended forest/domain, then verify `SYSVOL` and `NETLOGON`, DNS locator records, replication, time, GC state, and a client authentication/policy transaction. Do not clone or snapshot-restore a DC as though it were a generic VM; use supported DC cloning, backup, and recovery procedures.

For an Azure-hosted DC, put database/log/SYSVOL on suitable persistent disks, never on temporary storage; map Azure regions/zones to real AD sites/subnets; avoid a circular VNet-DNS dependency; protect management without blocking AD ports; and maintain more than one failure domain and a path to a writable DC. Azure platform availability does not replace directory replication and forest recovery.

**VERIFY CURRENT:** Supported Windows Server releases, Azure VM sizes, disk caching, accelerated networking, availability-zone behavior, and DC backup guidance change. Confirm the current [AD DS in Azure architecture](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/identity/adds-extend-domain).

### Deploy and secure RODCs

An RODC stores read-only directory partitions and can cache only credentials allowed by its Password Replication Policy (PRP). It fits sites with weaker physical/admin trust or unreliable WAN links, but it does not eliminate risk.

| Decision | Writable DC | RODC |
|---|---|---|
| Directory writes | Processes locally | Forwards to a writable DC |
| Password caching | Normal | Controlled by PRP |
| Local delegated administration | High-risk if broad | Administrator-role separation available |
| WAN outage | Local writes/auth normally available | Cached users can authenticate; uncached users and writes need writable path |
| Compromise response | Full writable-DC scope | Reset actually cached credentials and investigate delegated/local scope |

Explicitly deny privileged accounts in PRP, allow only appropriate branch identities, prepopulate required credentials before a planned outage, and review the revealed list. Validate DNS, site/subnet placement, replication, writable-DC referral, local administration, and authentication during a safe WAN-isolation test.

### Manage FSMO roles

| Role | Scope | Main serialized responsibility |
|---|---|---|
| Schema master | Forest | Schema changes |
| Domain naming master | Forest | Domain/application-partition additions and removals |
| RID master | Domain | RID pool allocation and related SID functions |
| PDC emulator | Domain | Password-change priority, time hierarchy, lockout, and compatibility behavior |
| Infrastructure master | Domain | Cross-domain reference updates under its operating rules |

Discover current owners, monitor health, transfer roles during planned maintenance, and seize only when the old owner will not return. After a seizure, prevent the former owner from rejoining until it is properly rebuilt/cleaned. An offline role holder is not always an immediate outage; determine which operation is affected.

The forest-root PDC emulator normally anchors the domain time hierarchy to a reliable external source. Verify with `netdom query fsmo`, PowerShell, `w32tm`, replication evidence, and event logs rather than relying on a diagram.

### Configure sites and replication

AD sites model network topology. Subnet objects map client addresses to sites; site links express intersite connectivity, cost, schedule, and replication behavior. Missing subnets can send clients to distant DCs and make healthy directory services appear slow.

Within a site, replication favors rapid convergence. Across sites, the Knowledge Consistency Checker builds topology based on sites, links, schedules/cost, bridge behavior, and available partners. Directory partitions—including DNS application partitions—can have different replication scopes.

Troubleshoot with `repadmin /replsummary`, `repadmin /showrepl`, `dcdiag`, DNS locator records, time/Kerberos, RPC/firewall, connection objects, naming contexts, and Directory Service/DFSR events. Capture source, destination, partition, last success, consecutive failures, error, and topology before forcing replication.

### Configure trusts and multiple forests/domains

Trust creates an authentication path; it does not grant resource access by itself.

| Concept | Meaning |
|---|---|
| Direction | The trusting domain accepts identities from the trusted side |
| Transitivity | Whether trust can extend through other trust relationships |
| Forest trust | Connects forest roots with selectable direction/transitivity/auth scope |
| External trust | Connects particular domains, often for non-forest-wide or legacy cases |
| Selective authentication | Requires explicit permission to authenticate to target computers/services |
| SID filtering | Reduces malicious/unintended SIDHistory use across boundaries |

Diagram `identity domain -> trust direction -> allowed authentication -> target authorization`. Validate DNS name resolution, time, ports, trust password, suffix routing, selective-authentication ACEs, and SID filtering. Do not disable SID filtering casually to make a migration “work.”

Prefer fewer forests/domains unless security, autonomy, legal, replication, namespace, or merger boundaries justify more. A forest remains the meaningful AD DS security boundary.

### Create and manage principals

Separate identity lifecycle from access:

```text
authoritative person/workload -> account -> role group
-> resource group -> permission -> monitoring/review -> removal
```

Use global groups for same-domain role membership, domain-local groups to authorize resources in their domain, and universal groups for forest-wide membership/use when global-catalog replication cost is acceptable. A durable multidomain model is accounts → global role group → domain-local resource group → permission.

Protect account flags, delegation, Kerberos encryption types, logon rights, expiry, password policy, and group nesting. Disabling an account is immediately reversible and often precedes deletion; preserve retention/audit requirements.

#### Choose service accounts

| Identity | Best fit | Main consideration |
|---|---|---|
| Virtual/local service account | Supported service on one host | Limited portability/network identity |
| sMSA | Managed password for one host | Single-host placement |
| gMSA | Supported service/farm across authorized hosts | KDS root key, host retrieval permission, SPN/application support |
| dMSA | Supported Windows Server 2025 migration from traditional service identities | New release/domain/application requirements |
| Traditional domain user | Legacy workload unable to use managed identity | Manual password lifecycle, interactive use, SPNs, overprivilege |

For gMSA, create/verify the KDS root key, authorize only intended hosts, grant only required resource/logon rights, configure SPNs, and test from each host. Managed password rotation does not automatically enforce least privilege.

**VERIFY CURRENT:** Delegated managed service account requirements and support are Windows Server 2025-era and evolving. Use current [service-account documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/group-managed-service-accounts-overview).

> **Related item:** A service principal name binds a Kerberos service instance to an account. Missing or duplicate SPNs can cause authentication failure or NTLM fallback even when the password and network are correct.

### Implement Group Policy and Preferences

A GPO has computer/user configuration and a Group Policy container/template stored in AD DS and SYSVOL. Application depends on site/domain/OU links, inheritance, enforcement, block inheritance, link order, security filtering, WMI filtering, loopback mode, connectivity, replication, and client-side extensions.

Use OUs for management/delegation structure, not as a substitute for security groups. Put settings at the narrowest stable scope, document ownership and rollback, keep policy names purposeful, test with representative accounts/computers, and verify with `gpresult`, Resultant Set of Policy, operational events, AD version, and SYSVOL version.

Preferences configure items such as mapped drives, registry values, files, shortcuts, local users/groups, and scheduled tasks with targeting and action semantics. Unlike policy settings, some preference values can tattoo—remain after the item no longer applies. Understand Create/Replace/Update/Delete behavior, “remove when no longer applied,” and item-level targeting.

Never place reusable secrets in Group Policy Preferences. Historical GPP password encryption is not secret protection. Use LAPS, gMSA/dMSA, managed identity, Key Vault, or an approved secrets platform.

#### AD DS failure patterns

| Symptom | Likely layer | First evidence |
|---|---|---|
| Client uses distant DC | subnet/site/locator DNS | client IP-to-subnet mapping, `nltest /dsgetsite`, SRV query |
| Replication fails one direction | DNS/time/RPC/topology/authentication | `repadmin /showrepl`, partner DNS, clocks, event code |
| Trust validates but access denied | resource authorization/selective auth/SID filtering | authentication event plus target ACL/effective access |
| Service falls back to NTLM | SPN/DNS/account/delegation | ticket request, `setspn`, NTLM audit, service identity |
| GPO linked but absent | scope/filter/inheritance/replication/client extension | `gpresult`, GPMC result, GroupPolicy events |
| Branch user fails during WAN outage | PRP not allowed/cached | RODC PRP effective/revealed state and auth event |

#### Primary references

- [AD DS overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)
- [FSMO placement and optimization](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/fsmo-placement-and-optimization-on-ad-dcs)
- [AD replication concepts](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts)
- [AD DS Configuration Wizard and RODC Password Replication Policy](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-installation-and-removal-wizard-page-descriptions)
- [Group Policy overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview)

---

## 3. Manage Windows Server instances and workloads in a hybrid environment (10–15%)

### Choose the remote-management channel

| Channel | Strong fit | Main dependency/risk |
|---|---|---|
| Windows Admin Center | Browser-based server, cluster, VM, storage, and hybrid administration | gateway identity, certificate, RBAC/effective node rights, WinRM |
| PowerShell remoting | Repeatable Windows automation and rich object pipeline | WinRM, authentication, endpoint/session configuration, second hop |
| SSH | Cross-platform shell/PowerShell remoting and automation | OpenSSH service, key/password policy, firewall, shell/subsystem configuration |
| Remote Desktop | Interactive GUI or application troubleshooting | broad interactive privilege, credential exposure, firewall/licensing/session policy |
| Azure Arc | Azure governance/extension/update/configuration plane for non-Azure servers | agent identity, outbound connectivity, Azure RBAC/policy/extension health |

Prefer the least interactive, most auditable channel that completes the task. Separate management-plane availability from workload availability: Arc or WAC can be unreachable while the application still works, and a successful remote shell does not prove the application is healthy.

### Deploy Windows Admin Center

Choose local client or gateway deployment. For a shared gateway, use a trusted TLS certificate, hardened host, controlled inbound access, least-privilege gateway authorization, and constrained delegation only when required. Add servers/clusters, verify WinRM/firewall/name resolution, configure Azure registration for hybrid functions, and audit both gateway access and actions on targets.

The Azure portal Windows Admin Center experience uses Azure control-plane integration and a VM extension under current architecture. Verify current region, OS, network, identity, port, and extension support. Do not assume an Azure-portal blade bypasses guest permissions.

### Configure PowerShell remoting, second hop, and JEA

PowerShell remoting over WinRM uses endpoints/session configurations. Configure listeners, firewall, authentication, TrustedHosts only where Kerberos/trust cannot be used and risk is accepted, HTTPS where required, and constrained endpoints.

The second-hop problem occurs when credentials that authenticated from client to server A are not available to access server B. Options include Kerberos constrained/resource-based constrained delegation, CredSSP, RunAs endpoints, JEA virtual accounts/gMSA, explicit credentials, or application redesign. They have different credential exposure, directory control, and delegation scope. Never turn on broad delegation simply to clear an error.

JEA restricts who can connect and which commands/parameters/providers they can use. Define role capability files, session configuration, transcript location, virtual account/gMSA behavior, group mappings, and maintenance ownership. Test allowed and denied actions and whether the underlying service/resource permissions are truly least privilege.

### Configure SSH and remote desktop

For OpenSSH Server, install the supported capability, start/enable `sshd`, configure firewall, choose password versus public-key policy, protect host/private keys, restrict allowed users/groups, configure the default shell or PowerShell subsystem, and inspect OpenSSH event/file logs. Key possession authenticates a user; local Windows authorization still controls actions.

For RDP, require Network Level Authentication where compatible, restrict membership in Remote Desktop Users/Administrators, constrain network paths, use certificates, policy, lockout, MFA/gateway/Bastion where appropriate, and avoid broad internet exposure. Diagnose listener, firewall, route, NLA/authentication, rights, licensing/session, and desktop shell separately.

### Connect non-Azure servers through Azure Arc

Azure Arc-enabled servers project a non-Azure machine into Azure Resource Manager through the Connected Machine agent. Onboard interactively, at scale, or through supported cloud/connectivity tooling using least-privilege identities. Decide subscription/resource group/region/tags, private or public connectivity, proxy, service endpoints, Azure RBAC, policy scope, extensions, and update/configuration ownership.

Verify resource existence, agent local state, heartbeat/last connected time, extensions, managed identity, policy assignment/compliance, and workload health separately. Deleting the Azure resource does not uninstall every local component; offboarding must handle both control and guest state.

### Implement device configuration and extensions

Azure Policy machine configuration evaluates/audits or applies supported guest configuration through Arc/Azure VM components. Trace assignment → initiative/policy parameters → extension/agent → guest assignment → local evaluation/remediation → compliance. A compliant Azure resource can still run an unhealthy application, and a noncompliant resource is not always safely auto-remediated.

VM extensions deploy components such as Azure Monitor Agent, Defender-related agents, dependency components, scripts, or configuration onto Azure and Arc-enabled machines under supported scenarios. Inspect publisher/type/version, auto-upgrade settings, protected settings, managed identity, network/proxy, handler logs, sequence/version, and provisioning state. Avoid multiple tools racing to own the same setting.

### Manage updates and Automation runbooks

Azure Update Manager assesses update compliance and schedules/installs updates on supported Azure VMs and Arc-enabled servers. Define maintenance configuration, scope/dynamic scope, classifications, include/exclude rules, reboot behavior, timezone, maintenance window, pre/post work, and alerting. For clusters or stateful tiers, coordinate drain, dependency order, and health gates outside a naïve all-at-once schedule.

Azure Automation runbooks can use PowerShell or Python runtimes and hybrid runbook workers when execution must occur in a private/local environment. Design managed identity or approved credential assets, module/runtime pinning, webhook/input validation, logging, job concurrency, retry/idempotency, and rollback. A runbook that is safe once may be destructive on retry unless it tests current state.

**VERIFY CURRENT:** Azure Automation runtimes, modules, hybrid worker requirements, Update Manager features, Arc extensions, machine-configuration capabilities, and pricing evolve. Use current [Azure Arc-enabled servers](https://learn.microsoft.com/en-us/azure/azure-arc/servers/overview), [Azure Update Manager](https://learn.microsoft.com/en-us/azure/update-manager/overview), and [Azure Automation runbook](https://learn.microsoft.com/en-us/azure/automation/automation-runbook-types) documentation.

#### Hybrid management failure patterns

| Symptom | Likely layer | Evidence |
|---|---|---|
| WAC can list server but tool fails | target rights, WinRM/CIM/provider, double hop | WAC gateway log, target event, generated PowerShell |
| Second resource access denied | missing delegation/credential, not network | Kerberos ticket/delegation config and server-B auth event |
| Arc resource exists but offline | agent/service, identity/cert, DNS/proxy/outbound TLS | `azcmagent show/check`, local logs, Azure last connected |
| Policy assigned but no guest result | extension/agent/assignment scope | policy compliance reason, guest assignment, extension logs |
| Update scheduled but not installed | scope, classification, maintenance window, guest agent, reboot | maintenance run, assessment, Windows Update events |
| Runbook succeeds but target unchanged | execution location/identity/module/input/idempotency | job streams, hybrid worker log, target audit/effective state |

---

## 4. Manage virtual machines (10–15%)

### Configure Hyper-V guests and management paths

Enhanced Session Mode uses VMConnect with RDP capabilities to provide richer device/clipboard/display redirection for supported Windows guests. Basic session connects to the VM console path. Configure host and user policy plus guest support, and understand that Enhanced Session authentication/network behavior differs from direct network RDP.

| Management method | Path | Useful when |
|---|---|---|
| PowerShell remoting | Network to guest WinRM | Standard remote management across hosts |
| PowerShell Direct | Host VMBus to local Windows guest | Guest network is unavailable; host admin has VM/guest credentials |
| SSH Direct | Host-to-Linux-guest Hyper-V socket path using supported OpenSSH components | Linux guest network is unavailable or isolated |
| VMConnect | Console/enhanced-session path | Installation, boot, or interactive recovery |

**VERIFY CURRENT:** SSH Direct uses Hyper-V sockets and guest OpenSSH configuration rather than ordinary guest network reachability. Microsoft currently names it in the [AZ-802 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-802), but a current dedicated public product article was not discoverable during validation. Confirm the supported host, guest, OpenSSH, and configuration requirements before relying on it.

### Configure compute, memory, and integration services

Static memory assigns a fixed startup amount. Dynamic Memory uses startup, minimum, maximum, buffer, and priority to adapt supported guests. Plan enough startup memory for boot and recognize that guest-visible demand, host available memory, Smart Paging, NUMA, and application behavior affect results.

Configure virtual processors, reserve/limit/relative weight or CPU groups where applicable, NUMA exposure, and compatibility settings according to workload and supported migration paths. Oversubscription is a capacity/risk decision, not free compute.

Integration services provide time synchronization, heartbeat, shutdown, data exchange, backup/VSS, guest services, and other host-guest coordination. Enable only required services and verify version/guest support. Domain controllers have special time behavior; avoid allowing virtualization time to fight the AD hierarchy.

Nested virtualization exposes virtualization extensions to a guest so it can run Hyper-V or supported nested workloads. Validate processor/platform/VM-version requirements, MAC spoofing or NAT networking, memory settings, and performance/support constraints.

### Assign devices and partition GPUs

Discrete Device Assignment (DDA) passes a supported PCIe device directly to one VM. It requires hardware/platform support, device dismount from the host, location-path assignment, VM memory-mapped I/O configuration, compatible drivers, and operational acceptance that live migration/save/checkpoint features may be constrained.

GPU partitioning (GPU-P) divides supported GPUs among VMs. Plan supported Windows Server release, GPU/driver/hardware, homogeneous cluster configuration when highly available, partition counts, allocation, live migration behavior, and monitoring. A partition is not the same as DDA's exclusive whole-device assignment.

**VERIFY CURRENT:** GPU-P support, live migration, cluster prerequisites, supported GPUs/drivers, partitionability, and guest OS requirements change quickly. Use the current [GPU partitioning documentation](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/gpu-partitioning).

> **Related item:** Device performance and VM mobility trade against each other. Before selecting DDA, SR-IOV, GPU-P, or a synthetic device, decide whether the workload values maximum direct performance or flexible checkpoint/migration/HA operations more.

### Manage checkpoints, availability, disks, and adapters

Production checkpoints use guest backup technology to create a data-consistent checkpoint without preserving running memory; standard checkpoints capture VM/device memory state and are primarily a development/test tool. A checkpoint is not an independent backup. Merging/deleting a checkpoint consolidates differencing disks and needs time/capacity; never delete AVHDX files manually.

For high availability, configure the VM as a failover-cluster role on shared/clustered storage or an appropriate supported architecture. Validate cluster networks, CSV/storage, possible owners, VM configuration path, live migration, client reconnection, capacity after node failure, backup, and monitoring. Hyper-V Replica adds asynchronous secondary copies and recovery points; it does not replace clustering or backup.

Virtual disk decisions include VHDX versus legacy VHD, fixed/dynamic/differencing, generation, size/sector, controller, sharing, QoS, resize/compact/convert, and chain integrity. Fixed disks reserve capacity; dynamic disks grow but still require monitored physical capacity. Differencing disks depend on an immutable parent and intact chain.

Configure synthetic network adapters, virtual switch, VLAN, bandwidth/ACL/port features, MAC behavior, SR-IOV where supported, and guest IP/DNS. NIC teaming can exist on a Hyper-V host through supported switch-embedded or LBFO designs depending on release/scenario, and guest NIC teaming combines multiple virtual adapters. Do not mix architectures without checking current support.

### Configure Hyper-V switches and Replica

External switches bind to physical networking; internal switches connect host and guests; private switches connect guests only. Plan management OS sharing, teaming/SET, VLAN trunk/access, QoS, RDMA, SR-IOV, security extensions, and a recovery path before changing the host's only management adapter.

Hyper-V Replica asynchronously replicates selected VM disks to another host or cluster. Configure receiver authorization, Kerberos/HTTP or certificate/HTTPS authentication, firewall/listener, storage path, initial replication, frequency/history/application-consistent points, and monitoring. Know test, planned, and unplanned failover, reverse replication, and client/DNS redirection responsibilities.

### Manage Azure Windows VMs

#### Storage and capacity

Choose OS/data/temp disk placement, managed-disk type, capacity, IOPS/throughput, caching, bursting, encryption model, disk controller, LUN, and host limits. Temporary disk is not durable. Resizing a disk in Azure may still require guest partition/filesystem expansion.

Resize VMs based on CPU, memory, disk, network, accelerated networking, architecture, generation, GPU, and regional/zone capacity. Resizing commonly restarts the VM. VM Scale Sets manage a model and instances with orchestration, upgrade, health, scaling, and image decisions; instance drift from the model creates operational ambiguity.

#### Availability

Availability sets distribute VMs across fault/update domains within a datacenter design. Availability zones place resources in separate physical zones within a region. Scale sets can use zones and flexible/uniform orchestration according to scenario. None creates application replication, state consistency, or cross-region recovery by itself.

Design load balancing, health probes, multiple instances, application state, data replication, zone support, quotas, backup, and region recovery. A zonal VM is isolated to a zone, not automatically redundant across zones.

#### Secure management and networking

Just-in-time VM access in Defender for Cloud controls management-port exposure for an approved source and time window by changing applicable network controls. Azure Bastion provides managed browser/native connectivity without a public IP on each target under supported tiers/features. Both still require guest authentication/authorization and firewall/listener health.

Configure NIC, subnet, private/public IP, accelerated networking, NSG, route, DNS servers, load balancer/application gateway membership, IP forwarding, and multi-NIC behavior deliberately. Effective security combines subnet NSG, NIC NSG, platform routes, user-defined routes/NVAs, and guest firewall.

#### VM failure patterns

| Symptom | Likely layer | Evidence |
|---|---|---|
| PowerShell Direct works but network remoting fails | guest route/DNS/firewall/WinRM | guest network state and WinRM listener |
| Checkpoint merge consumes storage | differencing chain/capacity | VHDX parent chain, merge job, host free space |
| Live migration blocked after device assignment | DDA/GPU/CPU/network/storage compatibility | VM device state, cluster validation, support matrix |
| Azure VM reports Running but app fails | guest boot/service/network/auth/app | boot diagnostics, serial console, agent, transaction |
| VM resize unavailable | zone/region/SKU/cluster allocation constraint | size availability, deallocation requirement, quota/capacity |
| JIT approved but RDP still fails | route/NSG/guest firewall/listener/identity | effective rules, IP flow, listener, NLA/auth event |

#### Primary references

- [Hyper-V documentation](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/)
- [Manage Hyper-V virtual machines with Windows Admin Center](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/use/manage-virtual-machines)
- [Hyper-V checkpoints](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/checkpoints)
- [Hyper-V Replica](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/configure-replication-single-host)
- [Azure VM availability options](https://learn.microsoft.com/en-us/azure/virtual-machines/availability)
- [Azure Bastion overview](https://learn.microsoft.com/en-us/azure/bastion/bastion-overview)

---


## 5. Implement and manage on-premises and hybrid networking (10–15%)

### Design name resolution from authority outward

For any DNS answer, ask:

```text
client suffix/query -> selected resolver -> authoritative zone or recursion
-> record/alias -> address -> route/firewall -> listener -> identity
```

AD DS normally uses AD-integrated zones and secure dynamic updates. AD-integrated zones replicate through directory application partitions and support multimaster updates on DNS-hosting DCs. Choose replication scope—domain DNS servers, forest DNS servers, or a custom application partition—according to who must answer and update.

Create forward and reverse zones and use A/AAAA, PTR, CNAME, MX, SRV, TXT, NS, SOA, and other records for their intended protocol meaning. AD locator depends heavily on SRV records. A CNAME can redirect a name but does not automatically make Kerberos SPNs, certificates, SMB hardening, or applications accept that alias.

Distinguish:

- **forwarder:** sends unresolved recursive queries to another resolver;
- **conditional forwarder:** sends a particular DNS suffix to selected resolvers;
- **delegation:** authoritative parent records direct resolvers to child-zone name servers;
- **stub zone:** holds limited authoritative records to discover the current authoritative servers;
- **secondary zone:** read-only zone transfer copy outside AD-integrated multimaster behavior.

Configure recursion and forwarders with loop prevention and failure behavior. Conditional forwarders can be AD-integrated and replicated to chosen scope. Verify both directions in a cross-forest/hybrid scenario if applications and trusts require them.

### Resolve names across hybrid networks

Azure-provided DNS understands Azure resource names but cannot accept traditional inbound queries or host your AD zones as if it were a DC. Custom DNS settings on VNets/NICs direct guests to AD DNS or another resolver. Azure DNS Private Resolver provides managed inbound endpoints for queries entering Azure VNets and outbound endpoints plus rulesets for conditional forwarding from Azure to other DNS systems.

Plan address space, link/VPN/ExpressRoute routing, resolver inbound/outbound subnets, ruleset links, conditional forwarders on-premises, private DNS zone links, firewall UDP/TCP 53, and failure/redundancy. Private endpoint DNS needs the correct private zone and resolution path; simply creating an endpoint does not guarantee every on-premises client receives its private address.

Avoid circular forwarding:

```text
on-prem AD DNS -> Private Resolver inbound -> Azure ruleset outbound -> on-prem AD DNS
```

Define which server is authoritative for each suffix and which direction each conditional path travels. Test from representative clients with a specified DNS server.

**VERIFY CURRENT:** Private Resolver limits, regional availability, rules, DNS Private Resolver policy/virtual-network behavior, pricing, and integration patterns change. Use current [Azure DNS Private Resolver documentation](https://learn.microsoft.com/en-us/azure/dns/dns-private-resolver-overview).

### Use DNS policies and DNSSEC

DNS policies can control query resolution by criteria such as client subnet, server interface, time of day, FQDN, query type, or zone scope. Use them for split-brain responses, traffic management, filtering, or recursion control only with a documented rule order and test matrix. A policy can make two clients receive intentionally different answers; troubleshooting must include client subnet and server policy, not only zone contents.

DNSSEC signs DNS data so validating resolvers can detect forged/modified responses and build a chain of trust. It does not encrypt queries or hide names. Understand zone signing, key-signing/zone-signing keys, trust anchors/delegation signer records, rollover, validation, and operational recovery. Losing signing-key/rollover control can make valid names fail validation.

### Configure DHCP scopes, reservations, and options

Install and authorize DHCP servers in AD DS to reduce rogue service. Configure IPv4/IPv6 scopes, exclusions, pools, lease duration, reservations, scope/server/policy options, DNS update credentials, conflict detection, filters, and audit logging. Common options include router/default gateway, DNS servers, and DNS suffix; the actual value must match the subnet and resolver design.

A reservation maps a client identifier/MAC to a stable lease but remains part of DHCP. An exclusion removes addresses from dynamic allocation. A static address configured only on a device must also be excluded or outside the pool to prevent collision.

DHCP relay/IP helper forwards broadcasts from remote subnets. When one subnet works and another does not, inspect relay target, gateway/firewall/ACL, `giaddr`, scope state, available leases, policy, and return path before restarting DHCP.

### Implement DHCP high availability

Windows DHCP failover supports load-balance and hot-standby relationships for IPv4 scopes. Configure partner, shared secret, mode, load balance percentage or standby role, maximum client lead time, and state-switch interval. Replicate scopes and verify relationship state; operational configuration changes may need explicit replication.

Understand states such as Normal, Communication Interrupted, Partner Down, Potential Conflict, and Recover. Do not declare Partner Down casually: if the partner is still serving, conflicting leases can result. DHCP failover is not a replacement for redundant relay configuration, DNS, default gateway, or IPv6 design.

### Troubleshoot IP and DNS

Client evidence:

- `ipconfig /all`, route table, DHCP lease/server/options, APIPA address;
- `Resolve-DnsName` against the selected and authoritative servers;
- `Test-NetConnection`, `Get-NetTCPConnection`, ARP/neighbor table, packet capture;
- DNS client cache and suffix/search list;
- actual system clock and domain/site.

Server/network evidence:

- DHCP scope utilization, failover state, leases, filters, audit and server events;
- DNS zone/record/replication, policy, DNSSEC validation, forwarding, cache, server events;
- switch/VLAN, relay, VPN/ExpressRoute, route table, NSG/NVA/firewall, return path;
- application listener and authentication behavior after transport succeeds.

An IP connection that works while a name fails localizes toward DNS, but using an IP can change Kerberos, TLS certificate, SMB, and application behavior. Fix name resolution rather than institutionalizing the workaround.

> **Related item:** IP Address Management can inventory and coordinate DHCP/DNS/address spaces even though it is not named in the AZ-802 objective bullets. It is useful operational context, not a substitute for understanding the underlying services.

#### Primary references

- [Windows Server DNS overview](https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-top)
- [DNS policies overview](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview)
- [DNSSEC overview](https://learn.microsoft.com/en-us/windows-server/networking/dns/dnssec-overview)
- [Windows Server DHCP overview](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top)
- [DHCP failover](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-failover)

---

## 6. Manage storage and file services (15–20%)

### Model file access as layered authorization

For an SMB transaction, evaluate:

```text
client identity -> Kerberos/NTLM authentication
-> network reachability/firewall -> SMB server/share
-> share permission AND NTFS ACL -> file operation
-> audit/backup/snapshot/replication behavior
```

For Azure Files, add storage-account network access/private endpoint, identity-based authentication configuration, Azure RBAC share role, directory identity representation, and NTFS ACL. Data-plane rights and management-plane rights are different.

Use least privilege through groups, Access-Based Enumeration where appropriate, SMB encryption/signing policy based on threat model, and separate share and filesystem ownership. Effective network access is constrained by the more restrictive result of applicable share and NTFS permissions.

### Configure Azure Files

Choose SMB or NFS protocol, standard/premium or current provisioned model, redundancy, region, performance, quota, identity/authentication, encryption, networking, and backup according to workload. For Windows SMB identity, select the supported AD DS, Microsoft Entra Domain Services, or Entra Kerberos design and meet its client/identity requirements.

Avoid storage account keys for routine user access; they behave like broad secrets. Use private endpoints or restricted public-network rules where required, configure correct private DNS, grant Azure RBAC roles at the intended scope, and then apply NTFS permissions through an identity that can administer the root.

Troubleshoot in order: name resolves to intended endpoint, port 445/path is allowed, protocol/authentication is supported, identity obtains a ticket, RBAC share role permits data access, and NTFS permits the requested operation. Mount success with a key proves little about identity-based authorization.

**VERIFY CURRENT:** Azure Files pricing, provisioned v2 behavior, protocol/features, identity support, private endpoint DNS, redundancy, performance/scale, and backup change. Use the current [Azure Files planning guide](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-planning).

### Configure and monitor Azure File Sync

Azure File Sync uses an Azure file share as cloud endpoint and registered Windows Server paths as server endpoints. A Storage Sync Service, registered server, sync group, cloud endpoint, and server endpoint define topology. Cloud tiering keeps the namespace locally while recalling tiered content on demand.

Deployment sequence:

1. Verify OS/filesystem/topology/network/proxy and unsupported-file requirements.
2. Create Storage Sync Service and sync group/cloud endpoint.
3. Install current agent, register through an authorized identity, create server endpoint.
4. Choose cloud-tiering policy, volume free-space policy, initial-sync authority, and recall behavior.
5. Monitor server/endpoint health, sync sessions/errors, files not syncing, recall, tiering, and agent version.

Azure File Sync is synchronization, not backup. Deletion and corruption can synchronize. Protect the cloud share with Azure Files backup and test restore.

#### Migrate DFS or file shares to Azure Files/File Sync

Inventory namespaces, targets, DFS Replication topology/backlog, open files, ACLs, shares, data size/change rate, unsupported names/attributes, bandwidth, identity, and client dependencies. Decide whether clients will use Azure Files directly, a File Sync server endpoint, or an existing DFS Namespace referring to new targets.

Seed/copy through a supported method, preserve fidelity, complete delta synchronization, quiesce writers, cut over referrals/DNS/share paths, validate hashes/ACLs/application behavior, monitor sync, and retain rollback state. Do not run two uncontrolled replication engines over the same namespace.

### Configure Windows file shares, FSRM, and DFS

Set share path/name, caching/offline behavior, continuously available/access-based enumeration/encryption settings where supported, share permissions, NTFS ACL, audit, and firewall. Administrative shares and hidden `$` suffixes do not provide security by obscurity.

File Server Resource Manager provides quota, file-screening, storage-report, classification, and file-management tasks. Soft quotas report; hard quotas enforce. File screens block selected file groups but can be bypassed by content/extension tricks and are not antimalware. Test enforcement, notifications, event/report delivery, and application behavior.

DFS Namespaces provides a stable logical namespace and referrals to folder targets. DFS Replication provides multimaster replication for supported folder data. Namespace availability does not prove target availability or DFSR convergence. Configure sites/costs, referral ordering/cache, staging/conflict-deleted capacity, replication topology/schedule/bandwidth, and monitor backlog/events.

### Configure SMB over QUIC and SMB settings

SMB over QUIC carries SMB 3.x over QUIC/UDP 443 with TLS 1.3 for secure remote access without exposing TCP 445, under supported server/client/edition and certificate requirements. Configure a certificate whose subject/SAN matches the server name, trust, private key, server enablement, firewall, and client policy. It is still SMB: identity, share/NTFS permissions, signing/encryption, namespace, and server hardening remain.

**VERIFY CURRENT:** SMB over QUIC editions, client/server versions, access-control features, certificate rules, and management UI evolve. Follow the current [SMB over QUIC documentation](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-over-quic).

Manage SMB signing/encryption, dialect requirements, compression, multichannel, leasing/oplocks, guest access, NTLM/Kerberos behavior, client/server audit, and insecure legacy protocol removal. Enforcing a higher dialect/security setting can break old NAS/application dependencies; inventory and pilot first.

SMB Direct uses RDMA-capable adapters for low latency, high throughput, and low CPU use. SMB Multichannel can discover/use multiple paths; RDMA and multichannel often combine. Validate supported adapters/drivers/firmware, DCB/PFC where required by RoCE design, VLAN/QoS, RSS/RDMA state, and failover. A fast link with dropped/PFC-stalled traffic can perform worse than ordinary TCP.

### Configure disks, volumes, file systems, and Storage Spaces

Understand physical/virtual disk, partition style, basic/dynamic legacy disk, volume, mount point/drive letter, filesystem, share, and application layers. GPT supports modern large disks and UEFI boot scenarios; MBR has legacy limits. Before initializing, prove disk identity and ownership.

Use NTFS for broad compatibility and features; ReFS adds integrity, scale, block cloning/sparse VDL, and resiliency benefits for supported workloads but does not support every NTFS feature or boot scenario. Choose allocation unit, integrity streams, compression, deduplication, encryption, and workload support deliberately.

Storage Spaces pools eligible physical disks and creates virtual disks with simple, mirror, or parity resiliency plus columns/interleave/provisioning choices. Monitor physical disk, pool, virtual disk, volume, health, capacity, and repair jobs. Thin provisioning requires alerting because logical capacity can exceed physical capacity.

Storage Spaces Direct pools node-local drives across failover-cluster nodes. Validate Windows edition, symmetric certified hardware/firmware, network/RDMA, cluster validation, fault domains, resiliency, cache, free repair capacity, and workload. S2D is distributed storage; Cluster Shared Volumes and clustered roles are adjacent layers.

### Configure Storage Replica, deduplication, QoS, and iSCSI

Storage Replica performs block-level volume replication synchronously for zero data loss within supported latency or asynchronously for longer distances. It needs a separate log volume and supported source/destination volume geometry/filesystem/topology. Replication copies blocks, including corruption/deletion, and the destination is not a normal writable backup.

Data Deduplication identifies repeated chunks and stores references to optimized data. Configure supported workload/volume, usage type, schedule, minimum age, exclusions, garbage collection/scrubbing, and backup/application compatibility. Monitor savings and jobs; apparent free space depends on dedup metadata and integrity.

Storage QoS sets minimum/maximum IOPS or centralized policies in supported cluster scenarios to protect workloads from noisy neighbors. A minimum is a performance signal/goal under capacity, not a guarantee beyond hardware. Monitor latency, throughput, normalized IOPS, violations, and aggregate device capacity.

iSCSI presents block storage over IP. Configure target virtual disks and initiator IQN/IP mapping, portals, MPIO, CHAP/IPsec where required, dedicated/redundant networks, persistent sessions, and filesystem/cluster ownership. Never mount one noncluster-aware filesystem read-write from multiple hosts.

### Protect storage with BitLocker

BitLocker encrypts volumes using TPM, startup key/PIN, password, or recovery protectors according to role and policy. Decide OS/data/removable scope, algorithm, boot validation, auto-unlock, recovery escrow, delegated retrieval, and operational handling for firmware/boot changes.

Back up recovery information before enforcement and test authorized recovery. `manage-bde -status` or PowerShell shows conversion, protection, lock, method, and protector state. Suspending protection temporarily bypasses boot validation while preserving encryption; decrypting removes encryption. Treat recovery keys and directory backups containing them as sensitive.

> **Related item:** Azure Disk Encryption uses BitLocker inside Azure Windows VMs, but Microsoft has announced ADE retirement for September 15, 2028 and recommends encryption at host for new VMs. AZ-802 names BitLocker and encrypted-volume recovery, not ADE, but administrators may encounter ADE during transition. See [ADE retirement guidance](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/disk-encryption-windows).

#### Storage failure patterns

| Symptom | Likely layer | Evidence |
|---|---|---|
| Azure share reachable with key but not user | identity/RBAC/NTFS/Kerberos | ticket, role assignment, directory identity, effective ACL |
| File Sync shows persistent errors | unsupported file, agent, endpoint, conflict, network | health portal, sync event logs, files-not-syncing list |
| DFS namespace opens but file is stale | referral target/DFSR backlog/conflict | client referral cache, target state, DFSR backlog/events |
| SMB over QUIC fails while TCP SMB works | certificate/UDP 443/QUIC support/policy | cert name/trust/private key, firewall, SMB client/server logs |
| S2D remains degraded after node return | repair capacity/disk/network/job | health service, storage jobs, physical/virtual disk state |
| BitLocker recovery loops | boot measurement/protector/TPM/policy | recovery reason, protector state, TPM and BitLocker events |

#### Primary references

- [Azure Files documentation](https://learn.microsoft.com/en-us/azure/storage/files/)
- [Azure File Sync overview](https://learn.microsoft.com/en-us/azure/storage/file-sync/file-sync-introduction)
- [DFS overview](https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview)
- [Storage Spaces overview](https://learn.microsoft.com/en-us/windows-server/storage/storage-spaces/overview)
- [Storage Spaces Direct](https://learn.microsoft.com/en-us/windows-server/storage/storage-spaces/deploy-storage-spaces-direct)
- [Storage Replica overview](https://learn.microsoft.com/en-us/windows-server/storage/storage-replica/storage-replica-overview)
- [BitLocker overview](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/)

---

## 7. Secure Windows Server infrastructure (10–15%)

### Build layered protection

```text
boot/firmware -> OS baseline -> allowed code -> credential boundary
directory identity -> authentication protocol -> delegated authorization
network rule -> authenticated/protected connection -> application permission
data encryption -> key/recovery authorization -> audit/detection
```

Preventive controls reduce opportunity; detective controls identify suspicious or failed behavior; recovery controls limit lasting impact. No single Defender, firewall, encryption, or directory setting proves a secure server.

### Harden the operating system

Exploit Protection applies system and per-program mitigations. Pilot with workload/vendor compatibility, collect events, and make narrow exceptions instead of disabling all mitigations.

Application Control for Windows/App Control for Business—historically WDAC—controls which code can run based on signer, publisher, file attributes, reputation, managed installer, or hashes. Audit first, inventory scripts/drivers/installers/update paths, create base plus supplemental policies, explain unexpected code, then enforce in rings with signed update/recovery procedures. Hash rules are precise but brittle; publisher trust scales but broadens what is trusted.

Credential Guard uses virtualization-based security to isolate supported credential secrets. Verify hardware/firmware/virtualization/OS and protocol/application compatibility. It reduces reusable-secret theft but does not prevent phishing, token theft, delegated abuse, or credentials entered into a compromised remote system.

SmartScreen uses reputation to evaluate downloaded content and destinations; it is not an application allowlist. Configure for the server's interaction model and keep it as one layer.

Use Group Policy for supported OS/audit/firewall/Defender/user-rights/security-option settings. Windows Server 2025 OSConfig supplies role-aware `DomainController`, `MemberServer`, and `WorkgroupMember` security baseline scenarios with drift control. Microsoft states OSConfig baseline support does not extend to earlier Windows Server versions. Apply the right role, record OSConfig module/baseline version, test protocol/application behavior, verify compliance, and plan rollback.

**VERIFY CURRENT:** Baseline contents and OSConfig versions change. Use the [Windows Server 2025 OSConfig baseline guide](https://learn.microsoft.com/en-us/windows-server/security/osconfig/osconfig-how-to-configure-security-baselines).

### Implement Windows LAPS

Windows LAPS rotates and backs up managed local administrator passwords to AD DS or Entra ID for supported joined devices. For AD DS, prepare schema where required, grant devices self-update permission, delegate read/reset narrowly, configure policy, and verify rotation/retrieval. Decide password encryption/history, post-authentication reset actions, account selection, and DSRM password management.

Audit readers/resetters, protect directory backups, and test emergency retrieval during network/directory outage. Do not confuse built-in Windows LAPS with the older standalone LAPS product. Start with [Windows LAPS concepts](https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-concepts-overview).

### Configure Defender for Servers and Windows Firewall

Defender for Servers is a Defender for Cloud workload-protection plan for Azure and connected non-Azure servers. Distinguish resource visibility, plan scope, Arc/native connection, component/extension health, recommendation/policy evaluation, protection signal, alert, and response. Plans, agentless capabilities, entitlements, pricing, and prerequisites change; verify the current [Defender for Servers plans](https://learn.microsoft.com/en-us/azure/defender-for-cloud/plan-defender-for-servers-select-plan).

Keep Windows Firewall enabled on all profiles. Scope rules by direction, protocol, address, port, program/service, interface, profile, and authenticated identity where supported. Enable appropriately sized logging and document owner/expiry. Network security groups and Windows Firewall are independent layers for Azure VMs.

Connection security rules use IPsec to authenticate and optionally protect traffic. Isolation, authentication exemption, server-to-server, and tunnel rules solve different cases. Pilot request before require, model certificate or Kerberos bootstrap, and retain controlled exceptions. Firewall rules permit traffic; connection security rules authenticate/protect it.

### Secure AD DS accounts and authentication

Domain password policy controls length, history, age, complexity, and lockout; fine-grained password policies target users/global security groups when justified. Entra Password Protection extends banned-password intelligence to AD DS through DC agents and proxy services. Plan redundant proxies, registration, audit/enforce modes, monitoring, and writable-DC paths.

Protected Users applies strong restrictions to privileged accounts and can break legacy authentication/delegation/offline workflows. Pilot every administrative path. Harden DCs by minimizing roles/software and logon, isolating management, patching in rings, applying DC baselines, monitoring, securing backup, and separating privileged identities/workstations.

Built-in administrative groups can provide direct or indirect directory takeover. Keep standing membership minimal, alert on change, protect the built-in Administrator recovery account, understand nested group/user rights, and do not assume names such as Backup Operators imply low risk.

Delegate the smallest operation on the smallest OU/object scope to role groups. Separate account creation, reset, group membership, join, GPO, and resource operations as needed. Verify inheritance/effective permissions with representative nonprivileged identities.

Manage authentication protocols deliberately:

| Protocol/method | Strong fit | Common failure/risk |
|---|---|---|
| Kerberos | Domain authentication with mutual service identity/delegation | DNS, time, SPN, trust, encryption type, delegation |
| NTLM | Legacy/fallback scenarios | relay/hash exposure, weak service identity, audit and reduction needed |
| LDAP signing/channel binding/TLS | Directory queries and protected channel | legacy client incompatibility, certificates, policy |
| Certificate/smart-card authentication | Strong key-backed user/device/service authentication | PKI trust, mapping, revocation, renewal, recovery |
| Windows Hello for Business or other modern methods | Supported passwordless user scenarios | device registration, trust model, policy, recovery |

Audit NTLM use, identify source/target/account/application and Kerberos blocker, remediate, then deny in controlled scope. Do not disable estate-wide without testing cluster, backup, migration, service, trust, and outage workflows.

> **Related item:** Authentication proves an identity; authorization decides the operation. A trust or Kerberos ticket can succeed while share, NTFS, local right, Azure RBAC, or application permission denies access.

#### Security failure patterns

| Symptom | Likely layer | Evidence |
|---|---|---|
| App blocked after baseline | App Control, exploit mitigation, GPO/OSConfig, firewall | effective policy, Code Integrity/security/firewall events |
| LAPS password absent | schema/permissions/policy/join/replication | LAPS operational log, directory attribute, resultant policy |
| Defender plan enabled but no signal | onboarding/component/extension/policy scope | environment settings, Arc/extension health, test signal |
| Kerberos falls back to NTLM | DNS/SPN/trust/time/delegation/application | ticket request, SPN query, NTLM audit, auth events |
| Admin can authenticate but not manage | delegation/local rights/JEA/target ACL | token/group, endpoint role capability, effective permission |
| IPsec rollout blocks DC access | bootstrap/auth method/rule scope/firewall | security association, connection-security policy, Kerberos/cert path |

#### Primary references

- [App Control for Business](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/)
- [Credential Guard](https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/)
- [Entra Password Protection for AD DS](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-password-ban-bad-on-premises)
- [Windows Firewall documentation](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/)
- [Kerberos authentication overview](https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview)

---

## 8. Monitor and troubleshoot Windows Server environments (15–20%)

### Build evidence from a service question

```text
user transaction -> service indicator -> component signal
-> interval/retention -> baseline/threshold -> alert owner
-> diagnostic runbook -> repair -> validation
```

Metrics show numeric trends, logs record contextual events, traces connect request paths, and configuration/health data shows desired versus actual state. Alert only on actionable conditions with severity, owner, response, suppression/processing, and escalation. Monitor the monitoring system itself: missing heartbeat, failed action, disabled rule, full log, expired credential, or broken agent can turn silence into false health.

### Use Performance Monitor and Data Collector Sets

Performance Monitor shows real-time or recorded counters. A Data Collector Set schedules counters, traces, configuration, and alerts. Select evidence that tests a hypothesis:

| Resource | Useful signal | Caution |
|---|---|---|
| CPU | utilization by logical processor/process, queue, privileged/user time | total average can hide one saturated processor |
| Memory | available/committed bytes, paging, pool, process working set | low free memory can reflect useful cache; sustained hard paging is stronger |
| Disk | latency, IOPS, throughput, queue, capacity | thresholds depend on storage architecture and guest/host limits |
| Network | throughput, errors/discards, retransmission, connection state | low throughput can mean low demand or a blocked path |
| Service/process | state, CPU, memory, handles, threads | PID/instance changes require time/process correlation |

Choose sample interval and circular maximum size to capture the event without creating its own resource issue. Record baseline under comparable load. Use `perfmon /report`, `logman`, Reliability Monitor, Resource Monitor, and exported BLG/CSV reports appropriately. Microsoft's [Performance Monitor troubleshooting guide](https://learn.microsoft.com/en-us/troubleshoot/windows-server/support-tools/troubleshoot-issues-performance-monitor) provides current capture guidance.

### Use Windows Admin Center, System Insights, and event logs

Windows Admin Center exposes server/cluster events, performance, processes, services, storage, networking, updates, security, PowerShell, and Azure integrations. Protect the gateway and effective target permissions. Use the PowerShell it generates to understand actions rather than treating the UI as the source of truth.

System Insights runs local predictive capabilities on Windows Server 2019 and later for CPU, network, total storage, and volume capacity, with results in event logs and management through WAC/PowerShell. Configure each capability, gather history, and route useful events. Forecasts can be invalidated by seasonality or architecture/workload change.

Manage event-log size, overwrite/retention, channel enablement, audit policy, forwarding, access, and archival. Event ID is meaningful only with provider/channel/machine/time/activity/message. Preserve the relevant interval before it wraps and never clear logs as a generic repair.

### Configure Azure Monitor data collection and alerts

Azure Monitor Agent (AMA) plus data collection rules (DCRs) is the current collection architecture for supported Azure/Arc Windows servers. A DCR selects sources, data flows/transforms where supported, and destinations; an association connects it to machines/scope.

1. Define the operational/detection question and required event/counter.
2. Choose workspace region, RBAC, retention/table plan, and cost guardrails.
3. Deploy and verify AMA through supported policy/extension.
4. Create the DCR and association.
5. Generate a known signal and query heartbeat/target table.
6. Create an actionable metric, log search, or Activity Log alert.
7. Configure action group/processing and test delivery.

> **LEGACY/RETIRED:** The Log Analytics agent (MMA/OMS) retired August 31, 2024. Microsoft warns ingestion can stop after March 2, 2026. Use AMA/DCR for current designs and the [official migration guide](https://learn.microsoft.com/en-us/azure/azure-monitor/agents/azure-monitor-agent-migration) for remaining dependencies.

VM Insights provides curated performance views and supported process/dependency capabilities for Azure VMs and Arc servers. Distinguish VM power state, guest agent/extensions, AMA/DCR, data arrival, and application transaction.

**VERIFY CURRENT:** AMA/DCR schemas, transformations, VM Insights dependency architecture, table/pricing, retention, alert actions, and Arc support change. Start with [DCR overview](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview) and [VM Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/vm/vminsights-overview).

### Troubleshoot connectivity, DNS, Update, and time

Connectivity: prove source address, next hop/route, NSG/NVA/firewall, target listener, and return path using `Test-NetConnection`, `Get-NetTCPConnection`, `pktmon`/packet capture, firewall logs, and Azure Network Watcher tools. A TCP handshake does not prove authentication or application health.

Name resolution: query a specified resolver with `Resolve-DnsName`, inspect suffix, authoritative zone, record, TTL, forwarding/policy/DNSSEC, cache, and AD replication. For AD symptoms, verify locator SRV records and client site/subnet.

Windows Update: identify source—Microsoft/Windows Update, WSUS, Azure Update Manager, or other management—then policy, service, proxy/TLS, datastore/client events, component store, applicability, free space, and pending reboot. Preserve evidence before reset/repair.

Time: inspect `w32tm /query /status`, source/configuration, policy, service, UDP 123, virtualization integration, stratum/offset, and events. Domain members normally follow AD hierarchy; the forest-root PDC anchors to a reliable external source.

### Troubleshoot performance, extensions, encryption, and storage

For performance, correlate Azure/host and guest: VM/host size, burst credits, CPU/NUMA, memory pressure, virtual/physical disk limits and latency, caching, network limits, guest counters/processes, application latency, and time. Resizing can hide rather than fix a leak.

For Azure VM/Arc extensions, inspect provisioning state, publisher/type/handler version, sequence, protected settings, agent state, local logs, network/proxy/TLS, managed identity/RBAC, disk capacity, and extension conflicts. Follow the extension's supported remove/reinstall path only after preserving configuration and evidence.

For disk encryption, identify Storage Service Encryption, customer-managed disk key, encryption at host, ADE, or guest BitLocker. Then trace key state/version, vault/network/authorization, disk metadata, identity, extension/protector, and boot/recovery history. Never remove a key/protector while investigating.

For storage, separate disk, pool/virtual disk, volume/filesystem, share/protocol, replication/sync, network, and application. Check online/read-only state, capacity, health, errors, mount/LUN, ACL/locks, latency/throttling, redundancy, storage jobs, and logs. Do not initialize an unknown disk.

### Recover and troubleshoot AD DS

AD Recycle Bin restores deleted objects/attributes in a functioning directory when enabled; it cannot be disabled after enablement. Restore parents before children where needed, then validate memberships, linked attributes, ACLs, replication, synchronization, and application access.

Directory Services Restore Mode starts a DC without normal AD DS online for supported database/system-state recovery. Maintain protected, tested DSRM credentials beforehand. Choose nonauthoritative restore for a DC that should receive newer state or authoritative operations when selected recovered data must win, following official procedures.

Modern SYSVOL uses DFSR. Nonauthoritative sync rebuilds one copy from a healthy partner; authoritative sync establishes the selected trusted copy. Validate DFSR state/events, `SYSVOL`/`NETLOGON`, GPO AD and file versions, replication, and client policy.

For replication, capture source/destination/partition/last success/error and use `repadmin`, `dcdiag`, DNS, time/Kerberos, RPC/firewall, topology, database/disk, lingering-object, and DFSR evidence. Do not repeatedly force sync without cause.

For Kerberos/authentication, verify client/DC/service clocks, DNS, realm/domain/trust, user/computer secure channel, SPNs, encryption types, delegation, ticket cache, Protected Users, and service account. For secure-channel/computer trust errors, identify which account password/version and DC are involved; test with `Test-ComputerSecureChannel` or `nltest` as appropriate, repair deliberately, and do not casually remove/rejoin a server that hosts sensitive roles.

Follow the [AD forest recovery procedures](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-procedures) for catastrophic recovery. Recycle Bin, one DC repair, and forest recovery are different scopes.

#### Troubleshooting failure patterns

| Symptom | Avoid shortcut | Evidence-led response |
|---|---|---|
| No Monitor alerts | assume no issue | prove local signal, AMA, DCR association, table/query, rule, action delivery |
| Azure VM `Running` | assume guest healthy | boot diagnostics/serial, agent/extension, network, service, transaction |
| DNS fails | hard-code IP | locate resolver/authority/record/policy/cache; preserve Kerberos/TLS names |
| CPU high | resize immediately | correlate process, queue, host, duration, disk/network wait, baseline |
| AD replication error | force sync | identify partner/partition and DNS/time/RPC/topology cause |
| computer trust broken | remove/rejoin immediately | test secure channel, DC contacted, replication, machine account/password state |

#### Primary references

- [Manage servers with Windows Admin Center](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/use/manage-servers)
- [System Insights](https://learn.microsoft.com/en-us/windows-server/manage/system-insights/overview)
- [Azure Monitor Agent](https://learn.microsoft.com/en-us/azure/azure-monitor/agents/azure-monitor-agent-overview)
- [Azure Monitor alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview)
- [Troubleshoot Azure Windows VMs](https://learn.microsoft.com/en-us/troubleshoot/azure/virtual-machines/windows/welcome-virtual-machines-windows)
- [Windows Time Service tools](https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)

---

## 9. Integrated scenarios

### Scenario A — Consolidate the retiring two-exam path into one operating model

**Situation:** An organization operates AD DS, Hyper-V, SMB file services, Azure VMs, and Arc-enabled branch servers. Administrators previously divided knowledge between AZ-800 and AZ-801 teams, but the replacement exam and day-to-day work require end-to-end ownership.

1. Inventory directory, DNS/DHCP, management, virtualization, storage, security, monitoring, backup, and recovery dependencies.
2. Separate authoritative state from replicated, synchronized, cached, or telemetry state.
3. Establish privileged management tiers, protected recovery identities, JEA endpoints, and logged administrative paths.
4. Map AD sites/subnets and hybrid DNS before onboarding servers or moving workloads.
5. Standardize Hyper-V and Azure VM configurations while preserving platform-specific availability and storage behavior.
6. Connect eligible non-Azure servers to Arc, then assign policy, extensions, Update Manager, and DCRs independently.
7. Validate a user transaction from DNS and Kerberos through share/application authorization, not only resource health.
8. Exercise directory, server, file, and monitoring recovery with evidence and explicit rollback criteria.

The lesson is that hybrid administration is not a single agent or portal. It is a set of control and data paths whose failure boundaries must remain visible.

### Scenario B — Secure a low-trust branch with intermittent connectivity

**Requirements:** Local authentication and file access during WAN loss, limited physical trust, centrally governed changes, and useful cloud inventory.

1. Define the branch AD site/subnet and a site-link schedule/cost that matches the WAN.
2. Deploy an RODC with DNS; configure Password Replication Policy to allow only required branch users and deny privileged identities.
3. Prepopulate approved credentials and delegate local RODC administration without granting domain-wide privilege.
4. Configure a resilient DHCP design and verify relay, DNS, gateway, lease, and failover behavior.
5. Use a DFS Namespace and supported Azure File Sync/server-cache design, documenting which data can be recalled while disconnected.
6. Arc-enable eligible member servers with minimum RBAC and tightly controlled extensions; treat onboarding a DC as a separate Tier 0 risk decision.
7. Apply Windows LAPS, firewall rules, application control in audit-first deployment, and constrained JEA operations.
8. Test WAN loss, an uncached user, expired cached content, wrong DNS, failed update orchestration, and restoration of monitoring connectivity.

Availability during disconnection depends on what is local: cached credentials, DNS data, file content, management capability, and recovery material are separate decisions.

### Scenario C — Migrate a file workload without changing the user path

**Requirements:** Preserve the UNC namespace and ACLs, minimize downtime, support hybrid access, and retain a safe rollback.

1. Inventory paths, owners, ACLs, alternate streams, unsupported names/types, open-file behavior, change rate, latency, and throughput.
2. Select Azure Files protocol, provisioning/tier, redundancy, networking, identity source, and backup from workload requirements.
3. Create share-level RBAC and Windows ACL mappings; test the real application/service identity rather than an owner account.
4. Deploy File Sync endpoints, seed data with a supported ACL-preserving method, and monitor namespace and content convergence.
5. Keep DFS Namespace as the client abstraction and control referral order during a pilot.
6. Quiesce writes, perform final convergence, change referrals, and retain the previous target read-only under the rollback plan.
7. Validate file hashes, ACLs, locks, recall behavior, latency, backup/restore, monitoring, and the original client transaction.
8. Remove the old target or replication engine only after acceptance and retention approval.

DFS Namespace, DFS Replication, File Sync, Storage Replica, and backup operate at different layers. A successful namespace referral does not prove the selected copy is current or recoverable.

---

## 10. Hands-on labs

These are original practice exercises, not recalled exam questions or copies of paid-course labs. Use isolated disposable systems and an authorized Azure subscription. Record requirement, design, commands/configuration, expected result, failure injected, evidence, repair, validation, cost, and cleanup. Never rehearse destructive directory, encryption, or storage recovery against production.

### Lab 1 — AD DS topology, RODC, and service identity

1. Create a small forest with two sites/subnets, two writable DCs, and an RODC in an isolated branch network.
2. Configure DNS, global catalog placement, site links, and RODC Password Replication Policy.
3. Create test global/domain-local/universal groups and explain token/replication effects.
4. Configure a gMSA for a harmless test service on approved hosts and verify retrieval rights/SPN behavior.
5. Transfer one FSMO role normally and locate every role holder.
6. Break one safe DNS or replication dependency, diagnose it, repair it, and verify convergence.

**Evidence:** topology, `dcdiag`, `repadmin`, FSMO output, RODC cached/denied principals, group nesting, gMSA host authorization, client DC/site selection, and failure timeline.

### Lab 2 — Group Policy and hardened delegated administration

1. Build a narrow OU, users/computers, security group, and test GPO with documented precedence.
2. Add one Group Policy Preference with item-level targeting and verify its action semantics.
3. Diagnose effective policy using `gpresult`, event logs, link/order, inheritance, filtering, and SYSVOL/AD version evidence.
4. Create a JEA endpoint that exposes only a harmless status/restart function; enable transcripts.
5. Attempt allowed and denied operations and demonstrate the second-hop problem with a third resource.
6. Choose a supported delegation pattern and prove it does not expose reusable broad credentials.

**Evidence:** GPO reports, resultant policy, preference behavior, JEA role/session files, transcripts, identities on each hop, and rollback.

### Lab 3 — Arc, Update Manager, extension, and Automation lifecycle

1. Onboard a disposable non-Azure Windows Server to Azure Arc with minimum required permissions.
2. Inspect Connected Machine agent identity, status, version, local logs, and Azure resource metadata.
3. Apply one safe device configuration or policy, deploy one extension, and assess updates.
4. Run an idempotent Automation runbook with managed identity and least privilege.
5. Block one required connectivity path or stop an agent safely, then distinguish resource existence from stale connection, extension, policy, update, and workload state.
6. Restore service, prove each layer, remove the test assignment/extension, and offboard cleanly.

**Evidence:** RBAC, agent status/log, policy result, extension state/log, assessment, runbook job/output, failure/recovery timestamps, and cleanup.

### Lab 4 — Hyper-V configuration and management paths

1. Create a Generation 2 VM with VHDX, dynamic memory, production checkpoints, integration services, and an isolated switch.
2. Compare VMConnect Enhanced Session, PowerShell Direct, and SSH Direct requirements and identity boundaries.
3. Expand the VHDX and then the guest partition/filesystem; record both layers.
4. Create and remove a production checkpoint, observing chain/merge behavior and storage consumption.
5. Configure or design Hyper-V Replica to an isolated receiver and run a test failover if resources allow.
6. Document a supported nested-virtualization, discrete-device-assignment, or GPU-partitioning design and its host/guest/hardware requirements.

**Evidence:** exported host/VM configuration, switch/adapter state, management-channel results, disk before/after, checkpoint chain/merge, Replica health/test, and compatibility matrix.

### Lab 5 — Azure Windows VM administration without public management ports

1. Deploy a disposable Windows VM with a deliberate disk, size, availability, VNet/subnet, NSG, and identity design.
2. Manage it through Bastion or an approved private path; configure JIT only if its prerequisites and licensing fit the lab.
3. Attach and initialize a data disk, then expand it through Azure and guest layers.
4. Deploy one safe extension and inspect Azure provisioning state plus guest logs.
5. Resize the VM or model a VM Scale Set/availability design from stated failure and capacity requirements.
6. Inject one safe NSG, guest-firewall, DNS, or extension fault and prove the first failed layer.

**Evidence:** architecture diagram, effective routes/NSGs, guest listener/firewall, disk layers, extension logs, boot/serial evidence, original transaction, and cleanup/cost.

### Lab 6 — DNS, DHCP, and hybrid resolution

1. Configure an AD-integrated zone, reverse zone, records, aging/scavenging plan, and a conditional forwarder in an isolated network.
2. Configure a DHCP scope, options, reservation, exclusions, and failover relationship where the lab supports two servers.
3. Diagram an Azure DNS Private Resolver design with inbound/outbound endpoints, ruleset links, and on-premises forwarding.
4. Query an explicit resolver using `Resolve-DnsName` and record recursive versus authoritative responses and TTL.
5. Break one relay, forwarder, firewall, record, client suffix, or server-authorization dependency.
6. Diagnose from packet/query/lease/server evidence, repair once, and retest Kerberos/service location where applicable.

**Evidence:** zone/records, policies, leases/failover, forward path, packet/query output, SRV lookup, root cause, and corrected client transaction.

### Lab 7 — File services, File Sync, and layered authorization

1. Create a Windows SMB share with intentionally different share and NTFS permissions; test effective access for multiple identities.
2. Configure a small FSRM quota/file screen/report and observe active versus passive behavior.
3. If an Azure sandbox is available, create Azure Files SMB, configure supported identity access, assign minimum share RBAC, and apply directory/file ACLs.
4. Deploy Azure File Sync with conservative cloud tiering; copy a representative tree while preserving metadata and ACLs.
5. Place the target behind a DFS Namespace plan, then tier/recall a file and observe sync/recall evidence.
6. Restore a deleted file through an independent recovery mechanism and explain why synchronization or replication was insufficient.

**Evidence:** share configuration, effective token/access, FSRM events, Azure RBAC and ACLs, sync health, recall, namespace referral, content hash, and restore result.

### Lab 8 — Monitoring, troubleshooting, and AD recovery boundaries

1. Record a healthy PerfMon baseline, Data Collector Set, event-log policy, AD replication/DNS/time state, and original user transaction.
2. If available, configure AMA with a DCR and alert for one known event/counter on an Azure or Arc test server.
3. Inject one fault at a time: stopped listener, wrong DNS, time skew within a controlled lab, disconnected DCR association, full test volume, or deleted lab object.
4. State a hypothesis and collect evidence before changing anything.
5. Use WAC, event logs, counters, `Test-NetConnection`, `Resolve-DnsName`, `w32tm`, `dcdiag`, and `repadmin` as applicable.
6. Restore deleted parent/child objects with AD Recycle Bin and validate attributes, links, memberships, replication, and access.
7. Review—not improvise—the DSRM, SYSVOL, system-state, and forest-recovery decision boundaries.
8. Repair each fault separately and prove the original transaction plus monitoring delivery.

**Evidence:** baseline, signal/DCR/alert chain, timeline, commands/queries, rejected hypotheses, Recycle Bin result, repair, and recovery/runbook gaps.

The public [MicrosoftLearning AZ-802 lab repository](https://github.com/MicrosoftLearning/AZ-802-Windows-Server-Administrator-Associate) and [rendered lab instructions](https://microsoftlearning.github.io/AZ-802-Windows-Server-Administrator-Associate/) provide official-course exercises under the repository's stated MIT license. Check current prerequisites, tenant/subscription cost, and lab revision before use.

---

## 11. Knowledge checks

These original checks test reasoning from the public objectives. Answer from the dependency chain, then verify uncertain details in the linked current documentation.

### AD DS

1. **Why can an Azure-hosted DC be healthy while nearby clients select a distant DC?** The VM and AD replication can be healthy while AD site/subnet mapping is missing or wrong. DC Locator uses the client's mapped site and published locator records, so verify subnet objects, DNS SRV records, client site, and reachable DCs.
2. **When is an RODC useful, and what does Password Replication Policy control?** It provides local read-only directory/DNS and selected cached authentication at a site with weaker physical/security conditions or poor links. PRP determines whose credentials may or must not be cached; it is not a general authorization policy.
3. **Why transfer rather than seize an FSMO role during normal maintenance?** Transfer coordinates with the healthy owner. Seizure is a recovery action for permanent owner loss and requires preventing the former owner from returning incorrectly.
4. **What does a forest trust grant by itself?** An authentication route and potential name/identity reachability, not resource permission. Authorization, selective authentication, SID filtering, DNS, time, and application behavior remain separate.

### Hybrid management

5. **What is the PowerShell second-hop problem?** Credentials used from a client to Server B are not automatically delegated from B to resource C. Choose a constrained supported delegation/run-as pattern rather than exposing a reusable user secret.
6. **How does JEA differ from ordinary remoting?** JEA publishes an intentionally limited endpoint whose role capabilities define visible commands, parameters, providers, and execution identity, with transcription/logging. Transport security alone does not constrain administrator power.
7. **What does an Arc status of `Connected` prove?** A recent agent heartbeat/control-plane relationship. It does not prove a particular extension, policy, DCR, update, guest service, or business transaction is healthy.
8. **How do Machine Configuration, extensions, Update Manager, and Automation differ?** They respectively audit/enforce guest configuration, deliver a discrete capability/handler, assess/orchestrate patches, and execute general runbook logic. Each has its own assignment, identity, network, log, and success state.

### Virtual machines

9. **Why is a checkpoint not a backup?** It remains dependent on the VM's disk/checkpoint chain and storage, adds merge/capacity risk, and is not an independently retained recoverable copy.
10. **What is the management-boundary difference among PowerShell remoting, PowerShell Direct, and SSH Direct?** Normal remoting uses a reachable guest network/listener; PowerShell Direct uses the local Hyper-V host-to-Windows-guest VM boundary; SSH Direct tunnels SSH through the host to a supported guest without ordinary guest network reachability. Authentication and support requirements still apply.
11. **Why can an Azure VM show `Running` but be unusable?** That state is control-plane/compute evidence. Guest boot, agent/extensions, network, DNS, firewall/listener, authentication, storage, and application health can fail independently.
12. **When do availability sets/zones or a VM Scale Set still fail to provide application HA?** When the application keeps single-instance state, lacks healthy routing/probes, cannot replicate data, has a shared identity/DNS/storage dependency, or lacks capacity/failover logic.

### Networking

13. **How does DNS delegation differ from conditional forwarding?** Delegation publishes authoritative name servers for a child namespace. Conditional forwarding tells a recursive resolver where to send queries for a matching suffix.
14. **What do Azure DNS Private Resolver inbound and outbound paths solve?** Inbound endpoints let external networks query Azure private DNS through reachable private addresses; outbound endpoints plus rulesets direct Azure-originated suffix queries to selected DNS servers. Links, routes, firewalls, and authority still matter.
15. **What does DHCP failover not protect?** Incorrect options, a broken relay/VLAN/firewall, DNS update failure, every server-wide setting, IPv6 behavior, or a client/application that cannot reach or use its lease.
16. **Why is hard-coding an IP a poor DNS repair?** It bypasses discovery temporarily while breaking name-bound Kerberos/TLS, mobility, load balancing, lifecycle, and evidence. Find the resolver/authority/record/path/cache failure.

### Storage and file services

17. **Which two authorization gates normally govern identity-based Azure Files SMB access?** Share-level Azure RBAC (or configured default share permission) and Windows ACLs on the directory/file. The effective identity/token and network/authentication path must also be valid.
18. **How do DFS Namespace, DFS Replication, File Sync, and Storage Replica differ?** DFSN supplies logical paths/referrals; DFSR replicates supported folders between Windows servers; File Sync synchronizes Azure Files and server endpoints with optional tiering; Storage Replica copies volumes at block level.
19. **Why is Storage Replica not backup?** It can rapidly reproduce deletion, corruption, or malicious encryption and normally does not provide long independent retention/history. Keep tested protected recovery points.
20. **How do SMB Direct and iSCSI differ?** SMB Direct accelerates the SMB file protocol over RDMA. iSCSI exposes block devices over IP; the initiator owns a filesystem and uncoordinated multi-host access can corrupt it.

### Security

21. **Why deploy application control in audit mode first?** Audit records reveal legitimate executables, scripts, drivers, installers, and update behavior so policy can be corrected before enforcement causes an outage. Audit is a deployment phase, not the final protection state.
22. **Why can a Windows LAPS password fail to appear in AD DS?** Check supported OS/update, schema, applied policy, target directory, secure channel, device self-write permission, LAPS operational events, and AD replication. A retrieval delegation problem is a later, different gate.
23. **What changes when a user joins Protected Users?** Stronger restrictions reduce credential exposure and legacy authentication/delegation, but can break older workflows, offline access, or services. Pilot identities and preserve separate protected recovery access.
24. **How should Defender for Servers and Windows Firewall be related?** Defender supplies posture/workload-protection capabilities according to plan and connected-resource state; the host firewall enforces local network rules/profiles. Neither proves the other is configured or that an application transaction works.

### Monitoring and troubleshooting

25. **Why does an AMA extension plus DCR not prove useful monitoring?** The DCR must be associated with this resource and select the right signal/flow/destination; the local event must occur, agent must collect, data must arrive in the expected table, query must match, alert must evaluate, and action must deliver.
26. **Why keep a healthy Performance Monitor baseline?** Counters are workload- and architecture-dependent; comparison across a representative healthy period helps distinguish normal demand from queueing, resource exhaustion, or regression.
27. **When is AD Recycle Bin insufficient?** It needs a functioning directory and retained deleted-object state. It does not recover a lost/compromised forest, failed database/DC, missing SYSVOL, or recoverable state beyond retention; use the appropriate system-state/forest procedure.
28. **What should be verified before repairing a broken computer secure channel by remove/rejoin?** The DC contacted, DNS/time, AD replication, computer object/password versions, trust test result, local access, service/dependency impact, and a reversible supported repair. Remove/rejoin can destroy useful evidence and disrupt server roles.

---

## 12. Final review checklist

- [ ] I can place DCs, DNS, global catalogs, FSMO roles, RODCs, sites/subnets, trusts, and replication from failure and security requirements.
- [ ] I can choose group scope and a service-account type and diagnose token, SPN, Kerberos, password, and host-retrieval behavior.
- [ ] I can predict Group Policy link/precedence/filtering/loopback/replication behavior and prove resultant policy.
- [ ] I can choose WAC, PowerShell/JEA, SSH, RDP, PowerShell Direct, or SSH Direct by network, identity, privilege, and audit boundary.
- [ ] I can separate Arc resource, agent, extension, policy, update, Automation, monitoring, and workload state.
- [ ] I can configure Hyper-V VM compute, memory, integration, device, checkpoint, disk, switch, NIC, availability, and Replica behavior.
- [ ] I can reason about Azure VM disks, size, availability, scale, JIT/Bastion, network, agent, extension, and guest state independently.
- [ ] I can trace AD DNS, hybrid resolution, DNS policy/DNSSEC, DHCP scopes/options/reservations/failover, and client IP problems.
- [ ] I can configure Azure Files identity/share RBAC/ACLs and File Sync/cloud tiering/migration/monitoring.
- [ ] I can compare SMB/QUIC, DFS, FSRM, NTFS/ReFS, Storage Spaces/S2D, Storage Replica, deduplication, QoS, iSCSI, and BitLocker by layer.
- [ ] I can apply exploit protection, application control, Credential Guard, SmartScreen, OSConfig/GPO, LAPS, Defender, firewall, password, privileged-group, delegation, and protocol controls without treating them as interchangeable.
- [ ] I can build a signal-to-alert path and diagnose connectivity, DNS, Update, time, performance, extensions, encryption, storage, replication, SYSVOL, Kerberos, and secure-channel failures from evidence.
- [ ] I can explain Recycle Bin, DSRM/DC restore, SYSVOL recovery, and forest recovery as different scopes.
- [ ] I completed at least one identity, VM, network, storage, security, and monitoring failure-injection exercise.
- [ ] I rechecked the beta blueprint, training/practice availability, and AZ-800/AZ-801 retirement immediately before scheduling.

---

## Places to learn

This is **not a complete list**, and it is not meant to be consumed end to end. Pick the resources and formats that work for your experience, access, learning style, and weakest objectives. A strong plan is usually the official blueprint and documentation, one primary structured resource, hands-on practice, and a legitimate assessment used diagnostically—not every course from every vendor.

AZ-802 is in beta, so provider catalogs and coverage can lag or change. Estimated times describe content consumption or a reasonable practice session, not total preparation; add note-taking, labs, documentation lookup, spaced review, and remediation. Recheck duration, access, price, publication/update date, and blueprint alignment before purchase.

### Current AZ-802 resources

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official AZ-802 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-802) | Free; authoritative beta scope | 45–75 min to map; 10–15 min before each study cycle | Build the seven-domain checklist and detect beta changes |
| [Windows Server Administrator Associate page](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-administrator-associate/) | Free; exam delivery, beta, training/practice, and credential status | 15–30 min; recheck before scheduling | Confirm live exam rules and replacement path |
| [Microsoft AZ-802T00 course](https://learn.microsoft.com/en-us/training/courses/az-802t00) | Course page public; instructor-led access/pricing varies | **5 instructor-led days** plus review/labs | Microsoft's current structured course outline across all seven domains |
| [MicrosoftLearning AZ-802 labs](https://microsoftlearning.github.io/AZ-802-Windows-Server-Administrator-Associate/) | Free public instructions; infrastructure may cost | Estimate 18–30 hr including setup, evidence, troubleshooting, and cleanup | Guided implementation aligned to the new course |
| [MicrosoftLearning AZ-802 repository](https://github.com/MicrosoftLearning/AZ-802-Windows-Server-Administrator-Associate) | Free; repository states MIT license | 30–60 min to inspect releases/issues plus lab time above | Source, revision history, setup files, and issue context for official labs |
| [Microsoft practice-assessment catalog](https://learn.microsoft.com/en-us/credentials/certifications/practice-assessments-for-microsoft-certifications) | Free; **AZ-802 not available at verification time** | Recheck periodically; later allow 1–2 hr per attempt plus remediation | Use once released to expose weak domains, not memorize wording |
| [Udemy AZ-802 & AZ-800 hands-on course](https://www.udemy.com/course/az-800-course-administering-windows-server-hybrid-core-inf/) | Paid; John Christopher; page showed August 2026 update, 25h 38m, 193 lectures | 25h 38m video; plan 35–50 hr with labs and notes | Current commercial course explicitly retitled for AZ-802/AZ-800; map every section to the beta blueprint |
| [Udemy AZ-802 practice tests](https://www.udemy.com/course/az802-tests/) | Paid; Scott Duffy; page showed August 2026 update and four 25-question tests | About 2–4 hr for attempts; 5–10 hr with documentation remediation | Early third-party diagnostic practice; verify explanations against official docs |

### Selective legacy resources

AZ-800 and AZ-801 retire on September 30, 2026. Their material can still teach durable objectives that moved into AZ-802, but neither old path matches the consolidated blueprint. Use the AZ-802 objective map as a filter: omit old-only migration, clustering/DR, containers, hybrid identity synchronization, and other material unless it supports your wider job learning; add new AZ-802-specific coverage such as SSH Direct, GPU partitioning, current Windows Server 2025 security/storage, and its exact troubleshooting scope.

| Resource | Access | Estimated time | Reuse boundary |
|---|---|---:|---|
| [Microsoft AZ-800 training/course](https://learn.microsoft.com/en-us/training/courses/az-800t00) | Self-directed modules free; instructor-led access varies | 4 instructor-led days; selectively plan 15–30 hr | Reuse AD DS, Group Policy, hybrid server management, Hyper-V/Azure VM, DNS/DHCP, and file-service foundations |
| [Microsoft AZ-801 training/course](https://learn.microsoft.com/en-us/training/courses/az-801t00) | Self-directed modules free; instructor-led access varies | 4 instructor-led days; selectively plan 8–18 hr | Reuse host/AD security and monitoring/troubleshooting; much HA/DR/migration scope is outside AZ-802 |
| [Pluralsight AZ-800 path](https://www.pluralsight.com/paths/administering-windows-server-hybrid-core-infrastructure-az-800) | Paid; displayed six courses, two labs, practice exam | **17 hr** displayed; plan 22–35 hr with labs/current-doc checks | Broad overlap, but most original videos are older; select by AZ-802 objective |
| [Pluralsight AZ-801 path](https://www.pluralsight.com/paths/administering-windows-server-hybrid-advanced-services-az-801) | Paid; displayed six courses, one lab, practice exam | **18 hr** displayed; likely 5–10 hr relevant selection | Select security and monitoring only; do not treat its old practice exam as AZ-802 validation |
| [O'Reilly Exam Ref AZ-800](https://www.oreilly.com/library/view/exam-ref-az-800/9780137729333/cover.xhtml) | Paid subscription; Orin Thomas, 2022 | O'Reilly displayed about 9h 35m; selectively 6–12 hr | Durable identity, management, VM, network, and storage foundation; update terminology/features |
| [O'Reilly AZ-800 Exam Guide](https://www.oreilly.com/library/view/administering-windows-server/9781803239200/) | Paid subscription; Steve Miles, 2022 | O'Reilly displayed about 10h 42m; selectively 8–16 hr | Broader older foundation; reconcile Windows Server/Azure changes |
| [O'Reilly Exam Ref AZ-801](https://www.oreilly.com/library/view/exam-ref-az-801/9780137729524/) | Paid subscription; Orin Thomas, 2022 | O'Reilly displayed about 8h 16m; selectively 3–6 hr | Security and troubleshooting concepts only where they map to AZ-802 |
| [Whizlabs AZ-800](https://www.whizlabs.com/microsoft-azure-certification-az-800/) and [AZ-801](https://www.whizlabs.com/az-801-configuring-windows-server-hybrid-advanced-services/) | Paid; course/practice/lab packaging varies | Verify current duration; select 5–15 hr by mapped gap | No verified AZ-802 product found at validation; old assessments are not AZ-802 score predictors |
| [MeasureUp AZ-800](https://www.measureup.com/microsoft-practice-test-az-800-administering-windows-server-hybrid-core-infrastructure.html) and [AZ-801](https://www.measureup.com/microsoft-practice-test-az-801-configuring-windows-server-hybrid-advanced-services.html) | Paid; availability/pages may block automated validation | Estimate 4–7 hr per product including review | Use only mapped questions for concept practice; no verified AZ-802 product found at validation |

At verification time, the [O'Reilly certification-prep catalog](https://www.oreilly.com/products/certification-prep.html) exposed older AZ-800/AZ-801 resources but no verified AZ-802-specific title. Do not infer that an old exam title has been updated unless the product page says so.

### Supplemental experts and channels

| Resource | Access | Estimated time | Notes |
|---|---|---:|---|
| [John Savill Windows Server YouTube search](https://www.youtube.com/@NTFAQGuy/search?query=Windows%20Server) | Free | Select 4–12 hr by weak domain; many videos are 15–90 min | Strong architecture/context supplement, not a complete AZ-802 course |
| [John Savill public GitHub repositories](https://github.com/johnthebrit) | Free; licensing varies by repository/file | 1–3 hr to locate matching whiteboards/materials | Companion visuals exist for some content; link or reuse only under the material's actual license |
| [Microsoft Reactor YouTube channel](https://www.youtube.com/@MicrosoftReactor) | Free | Select 2–8 hr; sessions commonly 45–120 min | Topic sessions on Azure, security, infrastructure, and operations; verify date/version |
| [Microsoft Windows Server YouTube channel](https://www.youtube.com/@MicrosoftWindowsServer) | Free | Select 2–8 hr; typically 15–90 min per item | Product demonstrations and current Windows Server context rather than one exam course |

### Suggested selective plans

#### Experienced Windows Server administrator

1. Map every blueprint objective and mark only what you cannot explain/configure/troubleshoot: 2–3 hours.
2. Use the AZ-802T00 outline and current docs for Arc/Azure VM/Files/Monitor/Defender and Windows Server 2025 gaps: 15–25 hours.
3. Complete Labs 3, 5, 7, and 8 plus one weak local domain: 25–40 hours.
4. Use one course section or legitimate assessment diagnostically, then remediate from official docs: 8–15 hours.

**Planning range:** approximately 55–85 focused hours when AD DS, Hyper-V, DNS/DHCP, SMB/storage, PowerShell, and Windows troubleshooting are already routine.

#### Azure administrator with limited Windows Server depth

1. Learn Windows Server administration, TCP/IP/DNS, PowerShell, AD DS/Kerberos, Group Policy, Hyper-V, and SMB/storage foundations: 35–60 hours.
2. Complete the AZ-802T00 sequence or one mapped structured course: 35–50 hours with notes.
3. Complete all eight labs and repeat at least three with a new injected fault: 45–70 hours.
4. Use current documentation and later an AZ-802-specific assessment for targeted remediation: 10–20 hours.

**Planning range:** approximately 125–190 hours after basic Azure familiarity, depending on lab speed and prior networking/identity experience.

#### Beta-candidate final review

1. Recheck the official blueprint, credential page, beta delivery/result policy, and course/practice availability.
2. Rebuild the seven-domain objective map from memory and mark every item you have not configured or diagnosed.
3. Explain each **VERIFY CURRENT**, **LEGACY/RETIRED**, security boundary, and migration warning aloud.
4. Rerun one identity, VM/network, storage, and monitoring failure exercise using evidence before repair.
5. Treat third-party questions as discussion prompts, never as live-item predictions; report suspected dumps rather than using them.

---

### Currency and integrity note

This guide is an independent synthesis of public sources. It does not reproduce exam questions and is not an exam dump. AZ-802 is a beta exam: Microsoft can revise objectives, weights, exam delivery, result timing, training, practice availability, product names, supported versions, licensing, previews, limits, security defaults, agents/extensions, and retirement/replacement plans. Verify the official blueprint, credential page, course page, retirement page, and linked current product documentation before an exam or production decision.
