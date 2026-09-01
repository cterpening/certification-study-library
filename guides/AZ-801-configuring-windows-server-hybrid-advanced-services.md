---
exam_code: AZ-801
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-801
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: retirement-announced
upcoming_change_checked: 2026-08-31
---

# AZ-801 Configuring Windows Server Hybrid Advanced Services Study Guide

> **RETIREMENT ANNOUNCED:** Microsoft will retire AZ-801 on **September 30, 2026, at 5:00 PM Central Standard Time**. AZ-800 retires at the same time. After that transition, [AZ-802](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-802) will remain the available exam path for the [Windows Server Administrator Associate certification](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-administrator-associate/). New learners should normally prepare for AZ-802; use this guide when you are already committed to taking AZ-801 before retirement or need its advanced-services knowledge.

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#az-801-coverage-record). The [official AZ-801 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-801) is authoritative.

**Current baseline:** Skills measured as of October 6, 2025<br>
**Upcoming blueprint change:** No later skills-measured revision is shown, but the exam itself has an announced retirement.<br>
**Certification lifecycle:** AZ-800 and AZ-801 retire September 30, 2026, at 5:00 PM Central Standard Time. Microsoft identifies AZ-802 as the remaining replacement path; complete both old exams before retirement if you intend them to satisfy the old route, and verify your personal credential status on the official certification page.<br>
**Course lifecycle:** Microsoft course AZ-801T00-A also retires September 30, 2026 and is replaced by AZ-802T00-A.<br>
**Blueprint discrepancy:** The canonical study guide assigns **15–20%** to high availability and **15–20%** to monitoring/troubleshooting. At verification time, the separate exam page displayed **10–15%** and **20–25%** respectively. This guide uses the canonical study guide because it is the objective source monitored by this library; budget flexibly and recheck both pages before scheduling.<br>
**Official sources:** [AZ-801 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-801) · [exam page](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-801/) · [retirement list](https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams) · [replacement credential](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-administrator-associate/)

## How to use this guide

AZ-801 is about protecting and changing a hybrid Windows Server estate without losing its business service. For every scenario, write down six things:

```text
requirement -> dependency -> control -> evidence -> failure action -> recovery proof
```

The exam domains overlap deliberately. Encryption is a security control and a recovery dependency. A cluster can improve local availability but cannot replace backup. Replication can reduce recovery point loss but can replicate corruption. Monitoring is useful only when the collected signal leads to a tested response. Migration is complete only when the destination service, identity, security, observability, backup, and rollback obligations are satisfied.

Use isolated Windows Server labs and an authorized Azure sandbox. Vaults, replication, storage, log ingestion, Defender plans, public IPs, and running VMs can cost money. Never test directory recovery, cluster force-quorum, credential controls, encryption-key removal, disaster failover, or identity cutover in production merely to prepare for an exam.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, migration, security, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Canonical weight | Administrator question |
|---|---:|---|
| Secure Windows Server on-premises and hybrid infrastructures | 25–30% | Can each identity, host, network path, workload, and data copy resist, detect, and contain compromise? |
| Implement and manage Windows Server high availability | 15–20% | Can a clustered workload survive expected component and maintenance failures without corrupting state? |
| Implement disaster recovery | 10–15% | Can the organization recover the right data and service within agreed recovery objectives after a larger failure? |
| Migrate servers and workloads | 20–25% | Can administrators move identity, data, compute, and applications with measured compatibility, controlled cutover, and rollback? |
| Monitor and troubleshoot Windows Server environments | 15–20% | Can operators collect useful evidence, isolate the first broken dependency, repair safely, and prove recovery? |

---

## 1. Build the advanced-services mental model

### Distinguish availability, protection, recovery, and migration

| Capability | Primary purpose | Typical mechanism | What it does not prove |
|---|---|---|---|
| High availability | Keep a service running through a local component failure or planned maintenance | Failover cluster, redundant network/storage, live migration | Survival of region/site loss or logical corruption |
| Replication | Maintain a secondary state copy with low data lag | Hyper-V Replica, Azure Site Recovery, Storage Replica | A clean historical copy or successful application recovery |
| Backup | Preserve independent recovery points | Azure Backup, MARS, MABS, system-state backup | Immediate service continuity |
| Disaster recovery | Restore an agreed service after a major event | Recovery plan, alternate site/region, tested failover and failback | Prevention of the initiating incident |
| Migration | Move to a planned target | Storage Migration Service, Azure Migrate, workload-specific tools | Ongoing resilience after cutover |

Use four recovery terms precisely:

- **RTO** is the maximum acceptable time to restore the service.
- **RPO** is the maximum acceptable data loss measured in time.
- **Retention** determines which historical recovery points remain available.
- **Recovery consistency** describes whether the recovered state is crash-consistent, file-system-consistent, or application-consistent.

A five-minute replication interval does not automatically create a five-minute RPO: replication can be delayed, the usable point can be older, and application dependencies may not be mutually consistent. A 30-minute VM restore does not automatically create a 30-minute RTO: identity, DNS, routes, keys, application validation, and business approval also consume time.

> **Related item:** Business impact analysis supplies RTO, RPO, dependency priority, compliance, and data-location requirements. Technology selection should follow those requirements, not begin with a favorite Azure or Windows feature.

### Separate control plane, data plane, and recovery authority

| Plane | Examples | Failure question |
|---|---|---|
| Control/management | Azure Resource Manager, Windows Admin Center, Arc, cluster service | Can an administrator request and coordinate a change? |
| Workload/data | SMB, IIS, AD DS, a clustered role, VM disks | Can the business transaction still complete correctly? |
| Identity/security | AD DS, Entra ID, Key Vault, RBAC, certificates | Who can authorize normal and emergency actions? |
| Evidence | event logs, cluster logs, metrics, DCRs, replication and backup jobs | What shows desired state and actual state differ? |
| Recovery authority | vault roles, break-glass accounts, DSRM credentials, key access | Can responders recover if the normal authority is unavailable or compromised? |

Do not let one failure boundary contain both the protected system and every way to recover it. Protect vault access from production administrators where practical, keep required key and credential material recoverable, and test from an environment that resembles the failure you claim to survive.

### Use a common operational sequence

1. Define the protected service and its user-visible success transaction.
2. Inventory dependencies: identity, DNS, time, route, firewall, storage, certificates, keys, agents, extensions, management APIs, and external services.
3. Establish baseline evidence while healthy.
4. Make one controlled change or inject one safe failure.
5. Observe detection, automatic response, manual escalation, and user impact.
6. Recover or roll back through the documented path.
7. Prove data correctness and application behavior, not just green infrastructure status.
8. Preserve timelines, configuration, logs, and lessons for the next exercise.

---

## 2. Secure Windows Server on-premises and hybrid infrastructures (25–30%)

### Design defense in depth

Treat a server as several attack surfaces rather than one object:

```text
firmware/boot -> operating system -> credential boundary -> application
network identity -> allowed path -> authenticated protocol -> authorized operation
data encryption -> key authorization -> recovery authorization -> audit evidence
```

Preventive controls reduce opportunity, detective controls reveal activity, and recovery controls limit lasting impact. Application control without credential protection still exposes secrets to an allowed malicious process. Disk encryption without protected keys converts the key store into the real target. A firewall rule without logging can block an application and provide little evidence as to why.

### Secure the operating system

#### Exploit Protection

Exploit Protection applies system-wide and per-program mitigations such as Data Execution Prevention, Address Space Layout Randomization, Control Flow Guard, and attack-surface-specific controls. Begin with the application vendor's support statement and a captured baseline. Audit or pilot where the feature permits, deploy to a small ring, observe crashes and blocked behavior, then expand. Per-program overrides can differ from system defaults, so document both effective policy and source of policy.

Troubleshoot by correlating the exact executable, mitigation, event time, application build, and policy source. Disabling the entire protection set because one legacy executable fails removes unrelated safeguards; prefer a narrowly justified exception with an owner and expiry.

#### Windows Defender Application Control

Windows Defender Application Control (WDAC), also called App Control for Business in current documentation, controls which code is trusted to run. Design policy around signer, publisher, file attributes, reputation, managed installer, or explicit hashes according to the software lifecycle. A hash is precise but changes with every binary update. Publisher rules scale better but trust everything within their scope. Path rules are easier to bypass when users can write to the path.

Use an audit-first progression:

1. Inventory code that executes, including scripts, installers, drivers, plug-ins, management tools, and update processes.
2. Create a base policy and supplemental policies aligned to ownership boundaries.
3. Deploy in audit mode and collect code-integrity events.
4. Explain unexpected binaries instead of blindly allowing them.
5. Move a representative ring to enforcement and test boot, patch, recovery, and business workflows.
6. Prepare signed policy updates and a recovery path before broad enforcement.

WDAC answers “may this code run?” It is distinct from Defender Antivirus, which evaluates malicious content and behavior, and from AppLocker, whose capabilities and security guarantees differ.

#### Credential Guard and SmartScreen

Credential Guard uses virtualization-based security to isolate supported credential secrets from the normal operating system. Verify hardware, firmware, virtualization, OS edition, authentication, and application compatibility before enforcing it. It reduces theft of reusable secrets; it does not eliminate phishing, token theft, delegated abuse, or credentials entered into a compromised remote system.

Microsoft Defender SmartScreen evaluates downloaded files and web destinations using reputation and policy. Configure it to match server roles—an interactive jump host and a headless application server have different exposure—but do not treat reputation as an application allowlist.

#### Group Policy and OSConfig baselines

Group Policy can configure account, audit, user-rights, firewall, Defender, protocol, and security-option settings across AD DS scopes. Link GPOs to deliberate OUs, use security filtering and WMI filters sparingly, model precedence, test resultant set of policy, and separate emergency rollback from routine editing.

OSConfig provides role-aware Windows Server 2025 baselines and drift control. Apply the matching `DomainController`, `MemberServer`, or `WorkgroupMember` scenario, then verify compliance and test workload effects. The current documentation states that OSConfig baselines do not support Windows Server versions earlier than 2025; use supported mechanisms such as Group Policy or Azure Policy machine configuration for older releases. An installed OSConfig module carries a particular baseline version, so record the module and policy versions as evidence.

**VERIFY CURRENT:** Baseline contents and OSConfig module versions evolve. Recheck [Windows Server 2025 OSConfig baseline guidance](https://learn.microsoft.com/en-us/windows-server/security/osconfig/osconfig-how-to-configure-security-baselines) and test protocol, RDP, SMB, service, and application behavior before production enforcement.

> **Related item:** A baseline is a controlled starting point, not proof of security. Exceptions need a business reason, compensating controls, owner, review date, and evidence that the effective configuration matches the approved state.

#### Windows LAPS

Windows LAPS rotates and backs up a managed local administrator password to Windows Server AD or Microsoft Entra ID for supported joined devices. For AD DS, prepare the schema where required, grant managed devices permission to update their own password attributes, delegate read/reset permissions narrowly, configure policy, and verify both rotation and authorized retrieval. Password encryption, history, post-authentication actions, and DSRM password management are policy decisions.

The protection is more than rotation. Audit who can read or reset the secret, avoid broad replication or delegated-read exposure, protect directory backups, and test emergency retrieval during a directory or network outage. Windows LAPS can manage DSRM credentials on domain controllers; that can materially improve forest-recovery readiness when governed carefully.

Use [Windows LAPS concepts](https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-concepts-overview) for the deployed Windows versions. Do not confuse built-in Windows LAPS with the older standalone Microsoft LAPS product.

### Secure hybrid Active Directory

#### Password policy and Entra Password Protection

Domain password policy covers length, age, history, complexity, and lockout. Fine-grained password policies can target users and global security groups when different requirements are justified. Determine the resultant policy rather than assuming an OU-linked GPO changes domain-account password rules.

Microsoft Entra Password Protection extends global and custom banned-password intelligence to AD DS through proxy services and agents on writable domain controllers. Plan redundant proxies, registration, connectivity, audit mode, enforcement, monitoring, and agent lifecycle. RODCs do not process password changes locally; understand the writable-DC path. A successful deployment should prove that expected password changes are allowed, banned variants are rejected, proxy/agent health is visible, and an outage has understood behavior.

#### Protected Users and authentication policy silos

The Protected Users group applies strong restrictions to privileged accounts, including changes to credential caching and authentication behavior. Those restrictions can break legacy protocols, delegation, offline sign-in, or older applications. Add candidates in a test ring and verify every administrative workflow before broad use.

Authentication policies define conditions and ticket lifetimes for accounts; authentication policy silos bind protected user, computer, and service accounts to an allowed relationship. Audit before enforcement, make the service dependency graph explicit, and preserve an independent recovery identity. A silo is not a replacement for tiered administration or removal of unnecessary privilege.

#### RODC account security

An RODC reduces risk at a less-trusted site by holding a read-only directory and caching only passwords allowed by its Password Replication Policy (PRP). Explicitly deny privileged accounts, allow only appropriate branch identities, prepopulate credentials needed during expected WAN outages, and review the revealed list. If an RODC is stolen, reset the credentials that were actually cached and treat its local delegated administrator and physical environment as incident scope.

#### Harden domain controllers and administrative groups

Domain controllers are identity infrastructure, not general-purpose application servers. Reduce installed roles and software, limit interactive and network logon, isolate management paths, patch through controlled rings, apply DC-specific baselines, secure backups, monitor directory and security events, and use separate privileged identities and hardened admin workstations.

Built-in groups such as Enterprise Admins, Domain Admins, Schema Admins, Administrators, Account Operators, Server Operators, Backup Operators, and Print Operators have powerful direct or indirect capabilities. Keep standing membership minimal, understand nested membership and user rights, protect the built-in Administrator recovery account, and alert on membership or privilege changes. A group that sounds operationally narrow can still enable code execution or backup-based data access on a DC.

Configure user-account security options intentionally: account flags, delegation settings, Kerberos encryption support, smart-card requirements, authentication scope, allowed logon, and service-account constraints affect both security and compatibility. Never apply “account is sensitive and cannot be delegated” or equivalent controls without checking required delegation paths.

#### Delegate without transferring the directory

Delegate the smallest set of operations over the smallest OU/object scope to role groups, not individual users. Use the Delegation of Control Wizard or explicit ACL tooling, document inheritance, and test with a nonprivileged representative account. Separate create/delete, reset-password, attribute-write, group-membership, GPO-link, and computer-join duties when risk requires it.

Avoid placing ordinary operators in domain-wide built-in administrator groups. Periodically verify effective permissions and unexpected inherited ACEs. Delegation is an authorization design; organizational-unit ownership alone does not automatically establish a security boundary.

#### Defender for Identity

Microsoft Defender for Identity sensors collect relevant identity signals from domain controllers and supported identity infrastructure and send selected data to its cloud analytics service. Plan sensor capacity, connectivity, directory-service accounts and permissions where required, coverage for every forest/domain/site, health alerts, role separation, and integration with Microsoft Defender XDR.

Use posture assessments to reduce exposure, alerts to investigate suspicious behavior, and entity context to correlate accounts and devices. Sensor deployment does not harden a domain controller by itself. A sensor gap, directory misconfiguration, time problem, or missing event setting can create blind spots while the portal still exists. Start with the current [Defender for Identity architecture](https://learn.microsoft.com/en-us/defender-for-identity/architecture).

#### Audit and reduce NTLM

NTLM remains a compatibility path for scenarios that cannot use Kerberos, but it lacks Kerberos capabilities and expands relay and credential-theft risk. Do not disable it estate-wide without evidence.

1. Enable NTLM auditing on domain controllers and affected servers.
2. Collect enough normal and peak-period evidence.
3. Identify source, target, account, application, name-resolution, SPN, trust, and protocol cause.
4. Fix Kerberos blockers or modernize the application.
5. Add narrowly documented exceptions if unavoidable.
6. Deny in increasing scope and monitor failure.
7. Retest administrative, cluster, backup, restore, migration, and outage workflows.

An IP address, missing/duplicate SPN, untrusted domain path, or broken DNS can force fallback even when both endpoints support Kerberos. Treat NTLM use as a symptom to explain.

### Use Azure security services

#### Ingest Windows Server data into Microsoft Sentinel

Current collection should use Azure Monitor Agent (AMA) and data collection rules (DCRs) for supported sources. A DCR specifies what is collected, transformed where supported, and delivered to which destination. Onboard non-Azure servers through Azure Arc when the chosen connector requires it, deploy AMA, associate the DCR, and validate records in the expected tables before trusting analytics rules.

Design from detection requirement backward:

```text
threat/use case -> required event -> audit policy -> local event exists
-> agent/DCR association -> workspace table -> analytics rule -> incident/response
```

Collecting every event increases cost and noise; collecting too little makes detection impossible. Test latency, parsing, computer identity, duplicate collection, retention, access, and an agent-disconnected alert.

> **LEGACY/RETIRED:** The Log Analytics agent—also called MMA or OMS—retired on August 31, 2024. Microsoft warns that ingestion can stop after March 2, 2026. Use AMA and DCRs for current designs and migrate remaining legacy dependencies using the [official agent migration guidance](https://learn.microsoft.com/en-us/azure/azure-monitor/agents/azure-monitor-agent-migration).

#### Defender for Cloud and Defender for Servers

Defender for Cloud provides security-posture management and workload-protection views. Defender for Servers plans add server-focused protections whose exact features, prerequisites, pricing, agentless capabilities, and plan differences can change. Establish the scope at management group, subscription, or connector; onboard Azure and Arc-enabled machines; configure environment settings and required components; remediate recommendations by risk; and route alerts to an owned response process.

Separate these states:

- resource visible in Azure;
- server connected through Arc or native Azure resource model;
- Defender plan enabled at the intended scope;
- required component or extension healthy;
- policy/recommendation evaluated;
- protection signal successfully tested;
- alert investigated and closed with evidence.

**VERIFY CURRENT:** Confirm current Defender for Servers plan entitlements, pricing, prerequisites, agentless coverage, data residency, and supported clouds on [Microsoft Defender for Servers](https://learn.microsoft.com/en-us/azure/defender-for-cloud/plan-defender-for-servers-select-plan) before design or purchase.

### Secure Windows Server networking

#### Windows Defender Firewall

Keep the firewall enabled for Domain, Private, and Public profiles. Scope rules by direction, protocol, local/remote address, port, program/service, interface, profile, and authorized identity where supported. Prefer rules tied to the actual service instead of broad port openings. Group rules, record ownership, enable logging sized for investigation, and verify the effective profile and policy source.

For a blocked transaction, prove DNS answer, route, listening socket, local and network firewalls, authentication, and application result. A successful TCP connection proves only transport reachability, not authorization or application health.

#### Domain isolation and connection security rules

Connection security rules use IPsec to authenticate and optionally protect traffic between hosts. Domain isolation can require authenticated connections for managed computers while defining boundaries or exemptions for systems that cannot participate. Rule types include isolation, authentication exemption, server-to-server, and tunnel scenarios.

Plan certificate or Kerberos authentication, profile and endpoint scope, encryption/integrity requirements, trusted intermediaries, domain-controller reachability, bootstrap behavior, and exemption governance. Pilot in request mode before require mode. Firewall rules authorize traffic; connection security rules authenticate/protect the connection. Both can apply to the same flow.

#### Azure network security groups

An NSG filters traffic at a subnet or network interface using priority, source, destination, protocol, and port. Rules are stateful. Effective security rules combine applicable subnet and NIC associations, and platform defaults remain unless overridden by higher-priority custom rules.

Use service tags and application security groups where they accurately express intent. Do not expose RDP broadly; prefer a controlled management path such as Bastion, VPN/ExpressRoute, or a secured jump tier. Diagnose with effective rules, IP flow verify, next hop, packet capture, guest firewall, and listener/application evidence.

An NSG is not a guest firewall replacement. The NSG protects the Azure network boundary; Windows Defender Firewall can enforce host/service and authenticated-identity context.

### Secure Windows Server storage

#### BitLocker and key recovery

BitLocker encrypts Windows volumes and can use TPM-based, startup-key, PIN, password, or recovery protectors according to platform and policy. Decide which volumes, algorithms, boot validation, recovery escrow, removable-media policy, and administrative roles are required. Back up recovery material to an approved directory or management system and test retrieval before enforcement.

Record `manage-bde -status`, protector state, encryption percentage, TPM state, recovery-object presence, and policy source. Suspending protection preserves key material while temporarily bypassing normal boot validation; decrypting removes encryption and takes much longer. Know which operation a firmware or boot change requires.

#### Azure managed-disk encryption choices

Azure Storage encrypts managed disks at rest by default using platform-managed keys or customer-managed keys through a disk encryption set. Encryption at host extends encryption to host-side caches, temporary disks, and data flow from compute to Storage. Confidential VM options address additional threat models. Azure Disk Encryption (ADE) is an older guest-level mechanism that uses BitLocker for Windows and an extension plus Key Vault integration.

> **RETIREMENT ANNOUNCED — Azure Disk Encryption:** ADE remains explicitly named in the October 2025 AZ-801 blueprint, but Microsoft will retire it on **September 15, 2028**. Microsoft recommends encryption at host for new VMs, or supported Confidential VM designs for confidential-computing needs. ADE-enabled workloads, including recoverable copies, must migrate before retirement; the official guidance says migration is not an in-place conversion. See [ADE retirement guidance](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/disk-encryption-windows) and [migration guidance](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-migrate).

For the exam, still understand how ADE uses BitLocker, the extension, Key Vault secrets/keys, key-encryption keys, VM identity and network access. For new production architecture, follow the announced replacement direction.

#### Manage and recover encrypted volumes and keys

Draw the complete authorization path:

```text
operator/automation identity -> Azure RBAC/control action
VM/extension identity -> Key Vault data action
disk or volume metadata -> key version -> key enabled and reachable
backup recovery point -> restored disk -> target key/identity/network context
```

Soft delete and purge protection reduce accidental or malicious key destruction, but recovery still depends on correct permissions, subscription/tenant context, network rules, and retained key versions. Rotate keys through a supported procedure and test restore from both recent and older recovery points. Never delete a key, secret, disk encryption set, protector, or vault access path merely because a portal reports encryption as enabled.

Encrypted-VM recovery can have restrictions that differ by encryption model and recovery tier. Recheck the current [encrypted Azure VM restore documentation](https://learn.microsoft.com/en-us/azure/backup/restore-azure-encrypted-virtual-machines) before relying on a runbook.

#### Security failure patterns

| Symptom | Likely layer | First evidence |
|---|---|---|
| Expected app blocked after hardening | WDAC, Exploit Protection, baseline, firewall | Code Integrity/exploit/firewall events and effective policy |
| LAPS password absent or stale | schema/permissions, join state, policy processing | LAPS operational log, directory attribute, resultant policy |
| Defender for Identity blind spot | sensor/connectivity/configuration/capacity | sensor health, service/event logs, portal health alert |
| Sentinel table has no server events | local audit, AMA, DCR, association, workspace | local event, agent state, DCR association, heartbeat/table query |
| Kerberos falls back to NTLM | DNS/SPN/trust/delegation/application | ticket request, SPN query, NTLM operational events |
| ADE VM cannot unlock after reboot | extension, Key Vault, key version, identity/network | extension status, serial/boot diagnostics, Key Vault access logs |

#### Primary references

- [App Control for Business and WDAC](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/)
- [Credential Guard overview](https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/)
- [Microsoft Entra Password Protection for AD DS](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-password-ban-bad-on-premises)
- [Windows Defender Firewall with Advanced Security](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/)
- [Microsoft Sentinel Windows security-event connector using AMA](https://learn.microsoft.com/en-us/azure/sentinel/data-connectors/windows-security-events-via-ama)
- [Managed disk encryption overview](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview)

---

## 3. Implement and manage Windows Server high availability (15–20%)

### Design for a specific failure set

A failover cluster is a set of independent nodes that maintain membership and coordinate clustered roles. It does not make every application cluster-aware. Before deployment, identify supported application behavior, shared state, client reconnection, node count, failure domains, storage, network paths, quorum, patching, backup, monitoring, and capacity after the largest planned failure.

N+1 capacity means the surviving nodes can run the workload after one node fails. A stretched two-site design needs a more explicit calculation: can either site run the required roles, and does the storage/data design make that state safe? A cluster that stays online but overloads its survivors has not met availability requirements.

### Create and validate a failover cluster

Prepare consistent supported Windows versions, editions, updates, drivers, firmware, roles, network names, domain or workgroup authentication model, storage visibility, and DNS. Run all relevant cluster validation tests and resolve failures before production. Validation evidence matters again after hardware, driver, storage, or topology changes.

Domain-joined clusters commonly use a cluster name object with permissions to create virtual computer objects. Prestage objects when directory permissions or change controls require it. Workgroup clusters support selected scenarios but change authentication, management, naming, and workload constraints; verify support for the intended clustered role rather than assuming domainless membership is equivalent.

Create the cluster, configure quorum, add storage/Cluster Shared Volumes as needed, create clustered roles, define preferred owners and failover/failback behavior, then test planned moves and controlled failures. Check that clients reconnect and the application validates data after failover.

Use the current [Failover Clustering overview](https://learn.microsoft.com/en-us/windows-server/failover-clustering/failover-clustering-overview) and hardware/storage requirements for the deployed Windows Server version.

### Understand quorum

Quorum protects consistency by allowing only the partition with a majority of current votes to keep the cluster running. It does not select which application data is newest, add workload capacity, or store a backup.

| Witness | Appropriate when | Critical dependency |
|---|---|---|
| Cloud witness | Nodes/sites can reach Azure Blob Storage and no suitable third location exists | outbound connectivity, storage account configuration, credential lifecycle |
| File-share witness | An independent SMB location is reachable by all nodes | file-server/site independence and permissions |
| Disk witness | Supported shared storage is visible to all nodes | shared-storage availability; not supported with S2D |
| No witness | The voting design does not benefit from one | enough surviving node votes |

Modern clusters use dynamic quorum and dynamic witness to adjust votes, but cannot create a majority from a simultaneous partition that lacks enough surviving voters. Place the witness in an independent failure domain, model each site/network failure, and inspect `Get-ClusterQuorum`, `Get-ClusterNode`, `NodeWeight`, and `DynamicWeight` rather than memorizing a static odd/even shortcut. The [quorum witness documentation](https://learn.microsoft.com/en-us/windows-server/failover-clustering/what-is-quorum-witness) explains the majority and split-brain purpose.

Force quorum is an emergency recovery action that can create divergent cluster state if another partition is active. Use only with confirmed topology, authority, and recovery procedure.

> **Related item:** Quorum answers “which partition may run the cluster?” Storage replication answers “which data copy is usable?” DNS/load balancing answers “where will clients connect?” Treat them as separate decisions.

### Configure cluster networks and Network ATC

Inventory management, cluster/heartbeat, live migration, storage, replication, and client traffic. Some networks can converge safely with QoS and adequate bandwidth; others require isolation for security, latency, or supportability. Avoid a single switch, adapter, subnet, route, or name-resolution dependency that defeats node redundancy.

Network ATC applies intent-based host networking configuration consistently across supported clustered nodes. Define the adapters and intent—management, compute, or storage—then validate converged virtual switches, RDMA, Data Center Bridging, VLANs, QoS, and IP configuration as applicable. Use global overrides only when needed and record them. Hardware symmetry and supported drivers/firmware remain essential; intent cannot make incompatible adapters equivalent.

**VERIFY CURRENT:** Network ATC capabilities and supported Windows Server/Azure Local scenarios change. Confirm the current [Network ATC documentation](https://learn.microsoft.com/en-us/windows-server/networking/network-atc/manage-network-atc) for the actual release.

### Configure clustered storage and workload behavior

Traditional shared storage presents supported disks or LUNs to cluster nodes; ownership coordinates access. Cluster Shared Volumes provide a consistent namespace such as `C:\ClusterStorage` and enable simultaneous coordinated access for supported roles. Storage Spaces Direct aggregates eligible local drives across cluster nodes into a software-defined pool.

Do not confuse:

- **CSV**: a cluster access/namespace mechanism for supported shared cluster disks;
- **S2D**: a distributed storage system built from node-local drives;
- **Storage Replica**: block-level replication between volumes/sites;
- **Scale-Out File Server**: an active-active clustered file-server role for application data over SMB;
- **general-use file server**: client file sharing with different workload behavior.

Configure clustered-role dependencies, possible/preferred owners, restart thresholds, failover period, anti-affinity or placement, health checks, and failback policy to match workload behavior. A resource online state is necessary, but the user transaction is the final health test.

#### Scale-Out File Server

Scale-Out File Server (SOFS) exposes continuously available SMB shares for application workloads such as Hyper-V or SQL Server when supported. Clients can connect through multiple cluster nodes, and SMB features coordinate transparent failover. Configure the SOFS role, storage/CSV, continuously available shares, permissions, DNS, networking, and application identities. Test node loss while observing the client workload.

Do not choose SOFS automatically for ordinary information-worker file shares. Match the clustered file-server role to workload and feature support.

#### Floating IP address in Azure

An Azure-hosted failover cluster often needs an internal load balancer, health probe, load-balancing rule, and backend membership so clients can reach the active clustered role. Floating IP/direct server return changes how the frontend address is delivered to the guest. The cluster IP resource may use probe-aware parameters instead of owning the frontend address as an on-premises cluster would.

Verify the workload's Azure cluster support, load-balancer SKU, frontend/probe/port, subnet, guest firewall, and client connection method. A healthy load-balancer probe proves reachability to the probe endpoint, not application correctness.

### Build stretch clusters deliberately

A stretch cluster places nodes across sites or Azure regions and typically combines site awareness, suitable network latency/bandwidth, quorum in a third failure domain, and replicated storage. Define preferred site, storage replication direction, RPO, automatic versus manual cross-site failover, and how applications, IP addresses, DNS, load balancers, and clients follow the role.

For an S2D campus cluster, failure-domain awareness and networking are as important as drive count. Validate supported distances/latency, symmetric hardware, RDMA/DCB configuration where used, storage resiliency, repair capacity, and witness access. Do not extrapolate a campus design to arbitrary inter-region latency.

### Configure and operate Storage Spaces Direct

S2D pools eligible local drives, creates software-defined storage, and exposes virtual disks/volumes to the cluster. Deployment sequence:

1. Verify edition, hardware, drive, firmware, network, node, and cluster requirements.
2. Update nodes and run cluster validation including storage and S2D tests.
3. Configure host networking and fault domains.
4. Enable S2D and inspect the pool, physical-disk health, storage jobs, cache, and capacity.
5. Create volumes with the intended resiliency and size.
6. Validate repair, node drain, restart, and workload behavior.

Resiliency consumes raw capacity, and repair operations need free capacity. Plan for the node/drive failures and maintenance concurrency you promise to survive. Monitor physical disks, virtual disks, storage pool, health service, CSV state, latency, and repair jobs.

When upgrading a node, confirm the supported rolling-upgrade path, pause/drain it, verify roles and storage jobs have settled, apply OS/firmware/driver changes, restart, validate, resume, and proceed one node at a time. Never start the next node merely because the previous node responds to ping.

The [S2D deployment guide](https://learn.microsoft.com/en-us/windows-server/storage/storage-spaces/deploy-storage-spaces-direct) is version-sensitive and should control production prerequisites.

### Manage clusters and updates

#### Move and recover workloads

Use planned moves to drain a node before maintenance. A failover is the cluster's response to failure or an administrator's move of a role; a failback moves it toward preferred ownership according to policy. For stateful applications, validate storage consistency and application recovery after every move.

When a node fails:

1. Preserve cluster and system evidence before rebooting repeatedly.
2. Determine whether the failure is node, network, storage, quorum, directory/DNS, or workload-specific.
3. Confirm the remaining cluster has quorum and enough capacity.
4. Repair or rebuild the failed node through a supported process.
5. Validate version, patch, driver, network, storage, and cluster configuration before resume.
6. Observe rebalance/repair and test a controlled move.

#### Cluster-Aware Updating

Cluster-Aware Updating (CAU) orchestrates a sequence: pause/drain a node, update and restart it, validate/resume it, then continue to the next node. It can run in self-updating mode through a clustered role or remote-updating mode from a coordinator. Profiles control behavior, and plug-ins identify update sources/types.

Before a run, validate cluster health, available capacity, workload mobility, storage health, update source, maintenance window, and rollback. After each node, require a health gate. CAU reduces disruption but does not make every clustered workload continuously available; client reconnect and application behavior still matter. See [Cluster-Aware Updating](https://learn.microsoft.com/en-us/windows-server/failover-clustering/cluster-aware-updating).

Windows Admin Center can create, monitor, update, and troubleshoot supported clusters. Use its views alongside Failover Cluster Manager, PowerShell, event logs, cluster validation reports, health service data, and generated cluster logs. A management UI is not itself the source of cluster availability.

#### HA failure patterns

| Symptom | Likely layer | Useful evidence |
|---|---|---|
| Cluster name fails to come online | AD object/DNS/IP/load balancer | cluster resource parameters, CNO/VCO ACL, DNS, probe |
| Nodes divide and roles stop | quorum/network partition | quorum config, node votes, cluster log, network loss timeline |
| CSV redirects or pauses | storage path/coordination | CSV state, storage events, path health, latency |
| S2D repair never settles | failed drive/node, insufficient capacity, network | health service, storage jobs, pool/physical disk state |
| CAU stops after first node | validation, coordinator, update source, role drain | CAU report/events, node state, pending reboot, workload blockers |
| Role online but clients fail | DNS/LB/firewall/app/authentication | client transaction, name resolution, probe, listener, app log |

#### Primary references

- [Failover Clustering documentation](https://learn.microsoft.com/en-us/windows-server/failover-clustering/failover-clustering-overview)
- [Deploy a quorum witness](https://learn.microsoft.com/en-us/windows-server/failover-clustering/deploy-quorum-witness)
- [Cluster and pool quorum](https://learn.microsoft.com/en-us/windows-server/storage/storage-spaces/quorum)
- [Failover clustering hardware and storage requirements](https://learn.microsoft.com/en-us/windows-server/failover-clustering/clustering-requirements)
- [Scale-Out File Server overview](https://learn.microsoft.com/en-us/windows-server/failover-clustering/sofs-overview)
- [Windows Admin Center cluster management](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/use/manage-failover-clusters)

---


## 4. Implement disaster recovery (10–15%)

### Start with recoverability, not job success

A successful backup job proves that a tool wrote something. A recovery test proves that the copy, metadata, permissions, keys, network, target capacity, and runbook can restore the required service. Define a recovery catalog for each workload:

| Decision | Questions |
|---|---|
| Protected unit | File, folder, volume, system state, VM, application database, or multi-VM service? |
| Recovery objective | Required RPO, RTO, retention, consistency, and recovery location? |
| Threat model | Deletion, corruption, ransomware, host loss, site loss, region loss, or identity compromise? |
| Independence | Can a compromised production identity delete or encrypt every recovery copy? |
| Dependencies | Which keys, credentials, DNS, network, licenses, agents, extensions, or installers are required? |
| Evidence | Which restore was tested, when, by whom, to what target, and against which business transaction? |

Use separate protection and recovery roles, multifactor authentication, soft delete, immutability where supported, alerting on destructive operations, and an emergency access procedure. Keep a copy of critical runbooks and recovery contacts outside the failed system.

### Choose the correct Azure Backup mechanism

| Mechanism | Typical protected source | Operational model |
|---|---|---|
| Microsoft Azure Recovery Services (MARS) agent | Files, folders, and system state on individual Windows machines | Agent sends protected data to a Recovery Services vault; no application-aware VM image |
| Microsoft Azure Backup Server (MABS) | On-premises Windows workloads, Hyper-V/VMware VMs, and supported applications | Dedicated server, local disk recovery tier, and Azure vault registration |
| Azure VM backup extension | Entire supported Azure VM | Azure orchestrates snapshots and vault-tier recovery points through a VM extension |
| Workload-aware Azure Backup | Supported SQL Server/SAP HANA in Azure VM and other supported data sources | Workload-specific discovery, policy, and recovery |

Do not refer to a generic “built-in backup agent” without identifying the actual mechanism. The AZ-801 phrase for Azure VM backup refers to the Azure VM backup architecture and extension; MARS is the direct file/folder/system-state agent; MABS has its own server, agents, protection groups, and local storage.

The [Azure Backup overview](https://learn.microsoft.com/en-us/azure/backup/backup-overview) and [support matrix](https://learn.microsoft.com/en-us/azure/backup/backup-support-matrix) are authoritative for current workload and vault support.

#### Back up files and folders with MARS

Create a Recovery Services vault in the intended subscription/region, configure vault security and storage redundancy before protection where settings have one-way constraints, download current vault credentials and the MARS agent, install/register the server, supply an encryption passphrase that the organization can recover, and create a schedule/retention policy.

MARS backups are incremental after the initial transfer. A recovery requires the registered server or an alternate registered server, vault access, and the encryption passphrase. Test original-location and alternate-location restore, overwrite behavior, permissions, and a representative large file. If the protected server is destroyed, the passphrase must not be destroyed with it.

**VERIFY CURRENT:** MARS versions, TLS requirements, workload/volume support, offline seeding options, vault limits, and retention capabilities change. Recheck the [MARS support matrix](https://learn.microsoft.com/en-us/azure/backup/backup-support-matrix-mars-agent) for production.

#### Deploy and manage MABS

MABS is a dedicated protection server derived from Data Protection Manager. It uses protection groups to select data sources and define short-term disk and online protection. Plan supported server OS, database placement, storage pool, capacity, network, agent deployment, consistency checks, vault registration, passphrase custody, update cadence, and backup of the MABS database itself.

Microsoft's current MABS v4 installation guidance says the server must be domain joined and cannot be a domain controller, cluster node, Server Core installation, or a host for several conflicting workloads. That is a version-sensitive production constraint, not an eternal exam fact. Always verify the current [MABS installation and upgrade guide](https://learn.microsoft.com/en-us/azure/backup/backup-azure-microsoft-azure-backup).

For recovery, choose the protected data source and recovery point, select original/alternate location and security behavior, run the job, then validate application or file integrity. Protect the MABS database and document how to rebuild a lost MABS server; losing the catalog can turn intact storage into a difficult recovery exercise.

#### Configure vaults and policies

A Recovery Services vault is the management and recovery-point container used by Azure VM, MARS, MABS/DPM, and supported application backups. Configure:

- subscription, resource group, region, and redundancy aligned with recovery requirements;
- RBAC and separation of backup operator, restore operator, and security administrator;
- soft delete, immutability, Resource Guard or multi-user authorization where applicable;
- public/private network access and required service connectivity;
- backup policies for schedule, instant-restore snapshot retention, daily/weekly/monthly/yearly retention, and time zone;
- alerting, reports, diagnostic settings, and a periodic restore-test calendar.

Changing a policy does not necessarily rewrite the lifecycle of all existing recovery points in the intuitive way. Inspect current policy and recovery-point behavior before promising retention.

### Protect and recover Azure VMs

Enable backup at the VM, policy, vault, or governed-at-scale level. Confirm the VM is in a supported region/subscription relationship, the guest/VM agent and extension are healthy, network and encryption prerequisites are met, and application-consistent processing works where required. Azure Backup creates snapshot-tier recovery points for faster restore and transfers points to the vault according to policy.

Choose a restore operation based on the failure:

| Restore choice | Use when | Validate afterward |
|---|---|---|
| Create a new VM | Need an isolated or parallel recovered machine | target network, identity, DNS, extensions, security, app data |
| Restore disks | Need control over VM creation or disk inspection | template/config, zones, encryption, NICs, boot and data order |
| Replace existing disks | Supported and the original VM shell/config should remain | VM state, disk mapping, current support restrictions |
| File recovery | Need selected files from a recovery point | mount/access process, ACLs, malware scan, cleanup |
| Cross-region/cross-subscription restore | The normal scope is unavailable or isolation is required | feature enablement, paired/target region, RBAC, policy and network |

Instant Restore uses snapshot-tier points to reduce restore time. Snapshot availability and retention are policy-dependent and can incur storage cost. A snapshot-tier restore can have different limitations from a vault-tier restore, especially for encryption and special VM types. Start with [Instant Restore](https://learn.microsoft.com/en-us/azure/backup/backup-instant-restore-capability) and the current [Azure VM restore guide](https://learn.microsoft.com/en-us/azure/backup/backup-azure-arm-restore-vms).

For an encrypted VM, preserve the relationship among recovery-point metadata, encryption model, disk encryption set or Key Vault, key versions, identities, and target permissions. An infrastructure restore that cannot access the necessary key is not a recoverable service. ADE-specific restore restrictions will become increasingly important as ADE approaches retirement.

> **Related item:** Backups of domain controllers require directory-aware recovery decisions. Restoring an old DC as an ordinary isolated VM can create replication and security consequences. Follow supported AD DS backup/restore and forest-recovery procedures.

### Implement Azure Site Recovery

Azure Site Recovery (ASR) orchestrates replication, failover, and failback for supported Azure VMs and on-premises machines. It is not the same as Azure Backup: ASR prioritizes a recent runnable replica and coordinated recovery; Backup prioritizes retained recovery points.

#### Design the replication path

For each protected VM, decide:

- source and target region/site, subscription, resource group, and vault;
- target virtual network/subnet, IP behavior, DNS, NSGs, routes, load balancers, and private endpoints;
- target compute size, availability configuration, disk type, encryption, capacity, and quotas;
- crash-consistent versus application-consistent recovery points and retention;
- change rate, bandwidth, initial replication, cache/storage accounts, and supported limits;
- mobility/replication agents or extensions and their update process;
- dependency grouping, boot order, scripts/manual actions, and application validation;
- test-failover isolation, cleanup, planned/unplanned failover, commit, reprotect, and failback.

A replication policy controls recovery-point retention and app-consistent snapshot frequency for the applicable ASR scenario. Higher retention and application-consistent frequency can affect storage, processing, and workload performance. Use current workload requirements rather than default values.

#### Configure network mapping

Network mapping associates source networks with recovery networks so replicas attach to the intended target after failover. Mapping does not recreate every dependent network service. Ensure target subnets, address ranges, DNS, routing, security controls, gateways, private connectivity, name-resolution changes, and application endpoints are ready.

Test failover into an isolated network that can reach required validation services without colliding with production addresses or accepting real transactions. A successful VM boot in a test VNet does not prove users can find or authenticate to the service after a real site failover.

#### Use recovery plans

A recovery plan groups replicated machines, orders startup groups, and can include automation or manual steps. Model application tiers such as identity/DNS, database, middleware, web, and external publication. Parallelize only independent actions. Add explicit health gates and owner approvals rather than fixed sleep periods wherever possible.

Run test failover regularly, validate the business transaction and data, record actual RTO/RPO, and clean up test resources. Planned failover is appropriate when the source is available and data can be synchronized deliberately. Unplanned failover accepts that the source may be unavailable and requires selection of the safest usable recovery point. Commit finalizes the selected point; reprotect reverses or establishes replication for the post-failover direction.

Use the [Azure-to-Azure ASR architecture](https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-architecture) and [enable-replication tutorial](https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-enable-replication) for current implementation details.

### Protect VMs with Hyper-V Replica

Hyper-V Replica asynchronously copies a VM from a primary Hyper-V host or cluster to a replica host or cluster. Configure the receiving replica server/cluster first, choose Kerberos over HTTP or certificate authentication over HTTPS as requirements dictate, authorize primary servers and storage locations, and configure firewall/listeners and certificate trust.

Enable replication per VM, select disks, initial replication method/time, frequency supported by the deployed version, recovery history, and application-consistent points. Monitor replication health and perform planned test failovers. Configure reverse replication if the design requires failback.

| Operation | Source expectation | Purpose |
|---|---|---|
| Test failover | Primary continues running | Start an isolated test VM from a selected recovery point |
| Planned failover | Primary available and shut down cleanly | Synchronize final changes and move with minimal data loss |
| Unplanned failover | Primary unavailable | Start replica from the best usable point; data loss may occur |

Hyper-V Replica does not automatically provide client redirection, application-tier orchestration, independent historical backup, or infinite retention. Start with [Configure Hyper-V Replica](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/configure-replication-single-host) and test the complete service path.

### DR failure patterns

| Symptom | Likely layer | First evidence |
|---|---|---|
| Backup job succeeds but restore fails | key/passphrase, unsupported target, corrupt/incomplete dependency | recovery-point type, job detail, vault/key permissions, support matrix |
| Azure VM snapshot stalls | VM agent/extension, VSS/application writer, network | extension state, VSS writers/events, backup job subtask |
| ASR replica unhealthy | change rate, agent/extension, cache/storage, connectivity | replicated-item health, agent logs, churn and network metrics |
| Failover VMs boot but app is unavailable | DNS/network mapping, dependency order, secrets, data consistency | recovery plan output, target routing/DNS, app/database logs |
| Hyper-V Replica cannot authenticate | certificate/Kerberos, listener, firewall, authorization | replication authorization, cert name/EKU/trust, Hyper-V VMMS logs |
| Restored encrypted disk will not unlock | missing/wrong key version, identity, network or ADE metadata | Key Vault audit, disk encryption metadata, restore tier/job details |

#### Primary references

- [Azure Backup documentation](https://learn.microsoft.com/en-us/azure/backup/)
- [Back up file data with MABS](https://learn.microsoft.com/en-us/azure/backup/back-up-file-data)
- [Azure Site Recovery documentation](https://learn.microsoft.com/en-us/azure/site-recovery/)
- [ASR recovery plans](https://learn.microsoft.com/en-us/azure/site-recovery/recovery-plan-overview)
- [Hyper-V Replica overview](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/manage/set-up-hyper-v-replica)

---

## 5. Migrate servers and workloads (20–25%)

### Use one migration lifecycle

Every migration should pass through measurable stages:

```text
discover -> assess -> design target -> remediate -> replicate/copy
-> test -> freeze/delta sync -> cut over -> validate -> observe
-> decommission after rollback window
```

Create an inventory of owners, usage, dependencies, data size/change rate, security, identity, certificates, DNS, IPs, ports, service accounts, scheduled tasks, backup, monitoring, licensing, support, and recovery objectives. Define acceptance tests and rollback triggers before migration. “Server started” is not an application acceptance test.

Choose among common strategies:

| Strategy | Meaning | Typical trade-off |
|---|---|---|
| Rehost | Move with minimal workload change | Faster but preserves technical debt |
| Replatform | Move to a managed or different hosting platform with moderate changes | More remediation; less infrastructure ownership |
| Refactor/rearchitect | Change application design/code | Highest change and potential long-term benefit |
| Rebuild | Deploy clean current OS/application and move state/config | Avoids carrying old OS state; requires good configuration knowledge |
| In-place upgrade | Upgrade the existing OS installation | Preserves state but also accumulated risk and rollback complexity |
| Retire/retain | Remove unused workload or defer it deliberately | Requires owner and dependency evidence |

### Migrate storage with Storage Migration Service

Storage Migration Service (SMS) orchestrates **inventory**, **transfer**, and optional **cutover** through Windows Admin Center. It can inventory supported Windows, Linux/Samba, and NetApp CIFS sources and transfer files, shares, and security configuration to supported Windows Server destinations or Azure VMs. During cutover, the destination can assume the source computer name and IP identity; the source receives a different identity and retains its data.

#### Inventory

Deploy a supported orchestrator, ensure administrative credentials and firewall connectivity, create a job, and inventory source servers. Review volumes, shares, files, local users/groups where supported, SMB settings, paths, exclusions, unsupported data, permissions, and transfer estimates. Clean up obsolete or prohibited content only through an approved data-owner process.

#### Transfer

Prepare or let Windows Admin Center create a supported destination, map source volumes to destination volumes, choose included shares/data and applicable Azure File Sync behavior, then perform transfer. Validate byte/file counts, errors, share definitions, NTFS and share permissions, local identity translation, and application-specific open-file behavior. Repeat transfer to reduce the final delta.

#### Cut over

Schedule a change window, stop writes or quiesce dependent applications, run the final transfer, supply target/source post-cutover network settings, and initiate cutover. Validate AD computer object and secure channel, DNS registrations and TTL/cache behavior, certificates, SPNs, shares, ACLs, client access, backup, monitoring, and application transactions.

Keep the renamed source isolated and recoverable during a defined rollback window. The service does not erase its original files. Reusing the original name/IP can expose stale certificates or external dependencies, so inventory identity beyond Windows naming.

The official [Storage Migration Service overview](https://learn.microsoft.com/en-us/windows-server/storage/storage-migration-service/overview) and [migration procedure](https://learn.microsoft.com/en-us/windows-server/storage/storage-migration-service/migrate-data) document supported sources, destinations, Azure VM creation, and cutover behavior.

#### Migrate to Azure file shares

SMS does not directly use Azure Files as a plain destination. A supported pattern can migrate to a Windows Server or cluster running Azure File Sync with cloud tiering when current prerequisites are met. For direct at-scale file transfer into Azure Storage, consider the source/target capabilities of Azure Storage Mover, AzCopy, Data Box, or a supported partner tool.

Preserve SMB identities and ACLs, directory authentication method, share names, namespace, file attributes, timestamps, locks, unsupported characters, capacity, transaction rate, and client protocol requirements. Decide whether users connect directly to Azure Files or through a Windows Server/Azure File Sync namespace; those are different architectures.

> **Related item:** Data transfer and namespace cutover are separate. DFS Namespaces or stable application configuration can reduce client-visible changes, but replication health and referrals must still be validated.

### Migrate servers with Azure Migrate

Azure Migrate is the hub for discovery, assessment, business-case analysis, dependency visibility, and migration of supported server/application estates. The Azure Migrate appliance discovers source metadata and performance data; migration may be agentless at the virtualization host layer or agent-based through replication components depending on source and constraints.

#### Deploy the appliance

Create an Azure Migrate project in the intended geography, prepare least-privilege Azure and source credentials, generate a project key, deploy the correct appliance package for VMware, Hyper-V, or physical/other sources, register it, add discovery credentials/sources, and verify continuous discovery.

Protect the appliance because it holds privileged discovery capability. Ensure time, DNS, outbound URLs, proxy, source management interfaces, and credential scope are correct. An appliance that appears registered but cannot reach its source provides incomplete assessment data.

#### Assess before sizing

Group machines by application dependency, select assessment type and target assumptions, and choose sizing based on performance history or as-on-premises configuration. Review readiness, conditional readiness, blockers, target size/storage, availability, cost assumptions, utilization percentile, comfort factor, and dependency completeness. Capture peak/business-cycle performance; a short quiet sample can undersize production.

An assessment is a decision input, not a migration guarantee. Validate guest OS support, boot type, disk count/size, encryption, networking, licenses, extensions, authentication, database/app support, and target-region capacity.

#### Replicate, test, and cut over VMs

Use the method appropriate to the source fabric. Microsoft's current overview recommends agentless migration for most supported VMware and Hyper-V scenarios; physical servers and nontraditional virtualization use the physical/agent-based path. Architecture and terminology evolve, so follow the [current migration-method comparison](https://learn.microsoft.com/en-us/azure/migrate/server-migrate-overview).

Configure target subscription, resource group, VNet/subnet, VM size, disk types, availability, security type, license benefit, and replication options. Start replication, monitor health and lag, run a test migration in an isolated VNet, remediate, then schedule final cutover. Stop application writes/source VM as required, synchronize, migrate, validate, enable operational controls, and stop replication only after acceptance and rollback decisions.

Physical-server migration uses a replication appliance and Mobility service and is also the fallback for unsupported host-level agentless paths. Do not install unrelated appliance roles together when Microsoft explicitly separates them. See [migrate physical servers](https://learn.microsoft.com/en-us/azure/migrate/tutorial-migrate-physical-virtual-machines).

### Migrate Windows Server workloads to a current version

#### Choose clean migration or in-place upgrade

An in-place upgrade retains applications, settings, and data on the same installation. It can be appropriate for a supported upgrade path with verified hardware, application compatibility, free space, backup, and rollback. A clean deployment plus workload migration creates a stronger boundary and is often preferable for old, compromised, poorly understood, or materially redesigned servers.

Before either path:

- inventory roles, features, applications, drivers, agents, services, tasks, certificates, firewall rules, local identities, ports, data, and dependencies;
- verify supported source-to-target upgrade paths and licensing;
- remediate deprecated features and incompatible applications;
- capture configuration and tested recoverable backups;
- create an application-specific validation and rollback plan;
- update monitoring, security baselines, backup, and documentation at the destination.

**VERIFY CURRENT:** Windows Server upgrade paths and role/application support depend on release and installation option. Use the current [Windows Server upgrade overview](https://learn.microsoft.com/en-us/windows-server/get-started/upgrade-overview) rather than assuming every version can skip directly to Windows Server 2025.

#### IIS

For a server-to-server IIS migration, capture sites, bindings, certificates/private keys, application pools and identities, authentication, modules, handlers, MIME types, configuration encryption, content, shared configuration, .NET/runtime dependencies, scheduled jobs, DNS, and external data services. Use supported Web Deploy, configuration export/import, or application deployment tooling; test on the target before switching DNS or load balancer membership.

For Azure modernization, Azure Migrate can discover and assess ASP.NET web apps at scale. App Service Migration Assistant and current scripts/tools can assess and migrate supported IIS applications to Azure App Service. Read readiness blockers carefully: Windows authentication, COM, GAC assemblies, local filesystem writes, machine-level configuration, unsupported frameworks, and network dependencies can require redesign.

Containerizing an IIS workload packages application runtime and dependencies into an image, but does not make mutable local state, machine identity, domain dependencies, or unsupported components disappear. Externalize state, run as a constrained identity, patch/rebuild images, and design container networking, registry, orchestration, secrets, and logging.

Start with [Azure Migrate application and code assessment](https://learn.microsoft.com/en-us/azure/migrate/appcat/overview) and [App Service .NET migration cases](https://learn.microsoft.com/en-us/azure/app-service/app-service-asp-net-migration).

#### Hyper-V hosts

Inventory VMs, virtual switches/VLANs, SET or teaming, storage/CSV paths, checkpoints, replication, cluster roles, virtual hardware versions, host resource reservations, GPU/device assignment, backup integrations, and management agents. Choose rolling cluster upgrade when supported, evacuate and rebuild a standalone host, or deploy a new cluster and live/cold migrate VMs.

Verify target CPU/vendor compatibility for live migration, authentication/delegation, network names and VLANs, storage access, integration services, and VM configuration-version consequences. Upgrade a VM configuration version only when older hosts no longer need to run it and the feature/support trade-off is accepted.

#### Remote Desktop Services

Map RD Connection Broker, Web Access, Gateway, Licensing, Session Host, certificates, DNS, collections, RemoteApps, profiles/FSLogix or user profile disks, GPO, databases, MFA/NPS integration, and client feeds. Build supported new infrastructure, add/replace hosts in controlled batches, drain sessions, test brokering and reconnect, then remove old roles. Preserve license-server activation and CAL requirements through authorized procedures.

#### DHCP

Export scopes, leases, reservations, options, policies, filters, credentials, audit configuration, failover relationships, and server settings. Install/authorize the target, import configuration, re-establish or migrate failover deliberately, update DHCP relay/IP helper addresses and monitoring, then stop/deauthorize the old server. Test lease renewal from representative subnets and option delivery—not merely scope presence.

#### Print servers

Inventory queues, ports, drivers, processors, forms, permissions, defaults, deployment GPOs, architecture, and signed-driver support. Use Print Management migration tooling where supported, but review old or package-unaware drivers before importing them. Test rendering and finishing from representative clients, update deployment references, and monitor spooler/security behavior.

### Migrate IIS to Azure targets

Choose among:

| Target | Best fit | Main redesign questions |
|---|---|---|
| Azure VM running IIS | Need high compatibility/control | OS ownership, availability, patching, backup, network/security |
| Azure App Service | Supported web app can use managed platform | authentication, runtime, local state, certificates, scale, networking |
| Windows container | Application benefits from image portability and supported container runtime | base-image lifecycle, state, identity, orchestration, observability |

Run assessment, remediate blockers, create a nonproduction target, migrate content/configuration, connect private dependencies, load/performance test, establish deployment and rollback, then use staged traffic or a controlled DNS/load-balancer switch. After cutover, enable backup where appropriate, monitoring, Defender, certificate renewal, autoscale, and cost controls.

### Migrate an AD forest to Windows Server 2025

First determine whether the requirement is an **in-place forest upgrade**—introduce newer DCs into the same forest—or a **forest restructure**—move identities/resources to a different forest/domain design. They have different identities, SIDs, trusts, namespaces, and rollback boundaries.

#### Upgrade an existing forest

1. Assess forest/domain health: replication, DNS, SYSVOL, time, trusts, backups, lingering objects, and application/DC dependencies.
2. Verify schema/application/agent/OS compatibility and supported functional levels.
3. Back up multiple writable DCs per domain and test forest-recovery procedures.
4. Introduce Windows Server 2025 DCs gradually, place DNS/GC appropriately, and validate replication/authentication.
5. Transfer FSMO roles through a planned change.
6. demote and remove old DCs cleanly, then clean metadata/DNS only where necessary.
7. Raise domain and forest functional levels only after every dependency and rollback implication is accepted.

Functional level enables directory capabilities and establishes a minimum DC version; it does not upgrade member servers or client operating systems. Raising it is a separate decision from adding a newer DC.

#### Restructure or build a new forest

Design target forest/domain/OU/GPO, namespace, DNS, trusts, identity matching, privileged access, application dependencies, SIDHistory policy, password migration, service accounts/SPNs, devices, profiles, resources, and coexistence. Establish a trust where appropriate, migrate in controlled waves, translate resource security, validate access, and remove coexistence paths after acceptance.

Sequence users, groups, service accounts, computers, and resources according to dependencies. A migrated user with no access to an unmigrated application is not a successful migration; neither is an application that works only because unrestricted SIDHistory or a broad trust remains forever.

#### ADMT: know the objective and the current limitation

The blueprint explicitly names Active Directory Migration Tool (ADMT) for users, groups, and GPO-related migration context. Understand its conceptual roles: source/target domains and trust, migration accounts, database, Password Export Server for password migration when used, SIDHistory, security translation, service/user/group/computer sequencing, and test/rollback.

> **LEGACY/DEPRECATED:** Microsoft states that ADMT 3.2 has not been updated to support Windows Server 2012 R2 through 2022 or modern Windows clients, its codebase is deprecated, and support is best effort. The page does not establish Windows Server 2025 support. Therefore, learn ADMT because the October 2025 blueprint names it, but do not present it as a fully supported modern production migration solution. Assess current Microsoft/partner migration options and obtain vendor support for the actual target. See the [ADMT support policy](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/support-policy-and-known-issues-for-admt).

GPO migration additionally requires backup/import or copy, Migration Table mapping of users/groups/UNC paths where applicable, WMI filter and script review, link/security filtering recreation, central-store/template compatibility, and resultant-policy testing. ADMT does not make every GPO/application dependency portable.

> **Related item:** SIDHistory can preserve access during coexistence, but it increases trust and token risk. Govern who can write it, retain SID filtering where required, monitor its use, translate ACLs to target SIDs, and remove it when coexistence ends.

### Migration failure patterns

| Symptom | Likely layer | First evidence |
|---|---|---|
| Files arrived but users are denied | share/NTFS ACL, identity translation, SID/trust | effective access, owner/SID, share plus NTFS permission |
| SMS cutover completes but name fails | DNS/AD replication, IP, certificate/SPN | DNS record/cache, computer object, secure channel, certificate names |
| Azure Migrate assessment is incomplete | appliance discovery/credentials/network/sample window | appliance health, discovered inventory, credential errors, history duration |
| Test-migrated VM boots but application fails | dependency, identity, DNS, secret, firewall, license | acceptance transaction and application logs |
| IIS works locally but not through production path | binding/certificate/DNS/LB/authentication | binding, certificate chain/name, proxy headers, client trace |
| New DC exists but clients use old/unhealthy path | site/subnet/DNS/replication | locator DNS, client site, `repadmin`, `dcdiag`, event logs |

#### Primary references

- [Azure Migrate documentation](https://learn.microsoft.com/en-us/azure/migrate/)
- [Azure Migrate appliance](https://learn.microsoft.com/en-us/azure/migrate/migrate-appliance)
- [Windows Server migration and upgrade](https://learn.microsoft.com/en-us/windows-server/get-started/upgrade-overview)
- [Storage Migration Service cutover](https://learn.microsoft.com/en-us/windows-server/storage/storage-migration-service/cutover)
- [Azure Storage Mover overview](https://learn.microsoft.com/en-us/azure/storage-mover/service-overview)
- [AD DS functional levels](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels)

---

## 6. Monitor and troubleshoot Windows Server environments (15–20%)

### Build monitoring from a question

Do not begin with “collect all counters.” Start with a service-level question and build an evidence chain:

```text
user transaction -> service-level indicator -> component signal
-> collection interval/retention -> baseline/threshold -> alert owner
-> diagnostic runbook -> repair -> validation
```

Use metrics for numeric trends, logs for discrete contextual records, traces for request paths, and configuration/health state for desired-versus-actual comparisons. Correlate in UTC and preserve the affected machine, user, operation, and correlation identifiers. An alert without an owner, priority, suppression model, and response action is noise.

### Use Performance Monitor and Data Collector Sets

Performance Monitor displays real-time or recorded counters. A Data Collector Set (DCS) schedules performance counters, event traces, configuration information, and alerts into reusable collection. Select counters that test a hypothesis and include denominators/context:

| Resource | Example evidence | Interpretation caution |
|---|---|---|
| CPU | Processor/Processor Information utilization, queue, privileged/user time | One busy logical CPU can hide behind a low total; virtualization adds host context |
| Memory | available bytes, committed bytes, paging, pool usage | Low free memory can be normal caching; sustained hard paging is stronger evidence |
| Disk | latency, IOPS, throughput, queue, free capacity | Queue thresholds depend on storage architecture; separate guest and platform evidence |
| Network | bytes, errors/discards, retransmission and connection state | A low throughput number can mean no demand or a blocked path |
| Process/service | per-process CPU, working set, handles, threads | Instance names/PIDs change; correlate with service and time |

Choose a sampling interval fast enough to capture the event but slow enough to control overhead and file size. Use circular logs for bounded long-running capture, record counter paths and machine time, reproduce when safe, and compare with a healthy baseline. `perfmon /report` runs a system diagnostics DCS; `logman` can create and manage sets from the command line. See Microsoft's [Performance Monitor troubleshooting guide](https://learn.microsoft.com/en-us/troubleshoot/windows-server/support-tools/troubleshoot-issues-performance-monitor).

Average utilization can conceal short saturation. Compare average, minimum, maximum, percentile where tooling permits, and user-visible latency over the same interval.

### Monitor with Windows Admin Center and System Insights

Windows Admin Center provides per-server and cluster views for events, performance, services, storage, networking, updates, Azure integrations, and PowerShell. Configure appropriate gateway/user authorization; a gateway operator's effective rights on a managed node determine what actions are possible. Use tags and connection inventory to organize scope.

System Insights runs local predictive capabilities on Windows Server 2019 and later. Built-in capabilities forecast CPU, network, total storage, and individual volume consumption, and publish results to event logs. Enable/configure the capabilities, allow enough history, review forecast status/reason, and route relevant event results to enterprise monitoring. A forecast is not a capacity promise; maintenance, seasonality, sudden growth, and application changes can invalidate it. Start with the [System Insights overview](https://learn.microsoft.com/en-us/windows-server/manage/system-insights/overview).

### Manage event logs as evidence

Configure log size, retention/overwrite policy, channel enablement, audit policy, forwarding, collection, and access according to investigation and compliance requirements. Important sources include System, Application, Security, Setup, Directory Service, DNS Server, DFS Replication, FailoverClustering, Hyper-V, BitLocker, CodeIntegrity, LAPS, Azure Connected Machine Agent, Azure VM Agent, and workload-specific operational channels.

Use event ID together with provider, channel, level, machine, timestamp, activity/correlation ID, and message fields. Event IDs are not globally unique. Filter and export the relevant time window before logs wrap; do not clear logs as a troubleshooting step. Windows Event Forwarding can centralize selected events on-premises, while AMA/DCR can send supported data to Azure Monitor.

### Configure Azure Monitor data collection and alerts

A data collection rule defines supported data sources, transformations/data flows where applicable, and destinations; a data collection rule association connects the rule to resources. For Azure and Arc-enabled Windows servers:

1. Define the operational/detection question and required Windows events or performance counters.
2. Create/select the Log Analytics workspace with deliberate region, retention, RBAC, and cost controls.
3. Install and verify Azure Monitor Agent through supported deployment.
4. Create a DCR with only required data, sampling, and destination.
5. Associate it to the intended machines or scope through supported policy.
6. Query heartbeat and target tables; generate a known event/load and verify arrival.
7. Alert on actionable conditions including loss of collection where appropriate.

Azure Monitor metric alerts evaluate numeric platform or custom metrics. Log search alerts evaluate a query result. Activity Log alerts detect control-plane events. Alerts use action groups for email, SMS, push, voice, webhook, ITSM, Automation, Functions, Logic Apps, or other supported actions. Configure evaluation window/frequency, threshold, dimensions, severity, suppression/processing rules, and ownership; then fire a safe synthetic test.

**VERIFY CURRENT:** DCR data-source schemas, transformations, AMA support, table plans, ingestion/retention pricing, alert features, and Arc requirements change. Use [Azure Monitor Agent overview](https://learn.microsoft.com/en-us/azure/azure-monitor/agents/azure-monitor-agent-overview) and [DCR documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview) for current design.

#### VM Insights

VM Insights provides curated performance views for Azure VMs and Arc-enabled servers and can provide process/dependency mapping under current prerequisites. Enable the necessary agents/DCRs/workspace configuration, verify data collection, and use workbooks/maps with platform metrics and guest logs. Distinguish:

- Azure resource is running;
- VM agent and extensions are healthy;
- AMA is connected and associated with the intended DCR;
- guest performance data arrives;
- application transaction is successful.

Each is a separate state. Use the current [VM Insights overview](https://learn.microsoft.com/en-us/azure/azure-monitor/vm/vminsights-overview) because agent and dependency-map architecture has changed over time.

> **Related item:** Monitoring the monitoring system is essential. Alert on missing heartbeats, disabled rules, failed action delivery, expired credentials/certificates, full log volumes, and ingestion gaps so silence does not masquerade as health.

### Use a layered troubleshooting ladder

1. Define the failed transaction, scope, exact error, and first/last known-good time.
2. Confirm recent change, maintenance, security incident, or dependency outage.
3. Check local host state: clock, CPU, memory, disk, boot, service, event logs.
4. Check name resolution: suffix, queried server, answer, authority, cache, registration.
5. Check network: source address, route/next hop, NSG/NVA/firewall, listener, return path.
6. Check authentication: identity authority, trust, ticket/token, SPN, certificate, time.
7. Check authorization: Azure RBAC, local rights, share/NTFS, application/database permission.
8. Check management components: agent, extension, DCR, policy, cluster/replication/backup job.
9. Compare with a healthy peer and baseline.
10. Make one reversible repair, rerun the original transaction, and document evidence.

### Troubleshoot connectivity and name resolution

For connectivity, use `ipconfig /all`, `Get-NetIPConfiguration`, routing tables, `Test-NetConnection`, `Get-NetTCPConnection`, firewall logs, `pktmon`, packet capture, Azure Network Watcher connection troubleshoot/IP flow verify/next hop, NSG effective rules, and NVA/load-balancer health. Confirm both forward and return paths. A route on the client does not prove the server has a return route.

For DNS, use `Resolve-DnsName` or `nslookup` against a specified server, inspect suffix/search behavior, record type, TTL, authoritative answer, conditional forwarder, delegation, zone replication scope, and client/server cache. Verify AD locator SRV records and site/subnet mappings for directory symptoms. An application connecting by IP while failing by name indicates a name or identity issue, but connecting by IP can also force NTLM or break certificates.

### Troubleshoot Windows Update and Time Service

For Windows Update, identify the management source—Windows Update, Microsoft Update, WSUS, Azure Update Manager, or other enterprise tooling—then inspect policy, service state, connectivity/proxy, datastore/client logs, pending reboot, servicing stack/component store, disk space, and applicable update. Use supported reset/repair procedures only after preserving evidence. In a cluster, coordinate node drains and health gates rather than updating all nodes together.

For Windows Time, identify domain hierarchy or configured NTP source with `w32tm /query /status`, `/source`, `/configuration`, and `/monitor`. Domain members normally follow the AD hierarchy; the forest-root PDC emulator anchors it to a reliable external source. Check service, policy, UDP 123 path, virtualization time integration, stratum, offset, and event logs. Large clock skew affects Kerberos, certificates, replication, logs, clusters, and signed cloud tokens.

### Troubleshoot Azure VM deployment and boot

Deployment failure can arise before a guest exists: policy denial, quota, capacity, SKU/zone unavailability, invalid template, dependency order, RBAC, provider registration, naming, network, disk/image, encryption, or extension errors. Read the nested Azure deployment operation and error code rather than retrying the top-level message.

For boot failure:

- inspect resource health, Boot Diagnostics screenshot and serial log;
- use Azure Serial Console when supported and configured;
- check OS disk attachment/LUN, boot configuration, filesystem, drivers, update history, encryption and free space;
- use VM repair commands or attach a copy/restored OS disk to a repair VM under a documented process;
- preserve evidence and avoid making simultaneous unknown changes.

After repair, validate guest boot, agent heartbeat, network identity, extensions, domain trust, application, monitoring, and backup. A portal `Running` power state is not guest health.

### Troubleshoot performance, extensions, encryption, and storage

Performance diagnosis needs both Azure and guest layers. Check VM size/vCPU/memory, host or resource health, CPU credits for burstable SKUs, disk IOPS/throughput/latency/queue, caching, network limits, accelerated networking, guest counters, top processes, application latency, and workload timing. Resizing may hide a leak without fixing it.

For Azure VM or Arc extensions, inspect provisioning state, handler version, sequence number, protected settings, guest/Arc agent state, local extension logs, network/proxy/TLS, managed identity/RBAC, disk space, and conflicts with other extensions. Remove/reinstall only when the extension's supported troubleshooting path calls for it and configuration is preserved.

For disk encryption, identify the model first: Storage Service Encryption, customer-managed keys/disk encryption set, encryption at host, ADE, or guest BitLocker independent of ADE. Then trace key state/version, Key Vault or managed HSM network and RBAC/access policy, identity, extension status, disk metadata, BitLocker protectors, reboot timing, and backup/restore history.

For storage, separate filesystem/volume, virtual disk/Storage Spaces, Azure managed disk, SMB share, storage account, and application layers. Check capacity, health, read-only/offline state, filesystem errors, mount points/drive letters, permissions, locks, latency, throttling, redundancy/replication, storage jobs, network, and service logs. Never initialize or format an unknown disk during diagnosis.

### Troubleshoot and recover Active Directory

#### Restore deleted objects with AD Recycle Bin

AD Recycle Bin preserves deleted-object attributes for recovery when enabled. It cannot be disabled after enablement. Identify the deleted object and its parent, restore parent objects before children as needed, restore with Active Directory Administrative Center or PowerShell, then validate memberships, permissions, linked attributes, replication, and application access. Recycle Bin is not a substitute for system-state backup or forest recovery.

#### Use DSRM for database recovery

Directory Services Restore Mode starts a domain controller without normal AD DS online so system-state/authoritative recovery operations can occur. Maintain a known, protected DSRM credential before disaster; Windows LAPS can support DSRM password management in suitable designs. Decide whether recovery is nonauthoritative—restored data then receives newer replication—or marks selected data authoritative so it propagates as the winning version.

Do not improvise a forest recovery on a connected production network. Follow a rehearsed isolation and recovery sequence, restore at least one trusted writable DC in each domain as required, seize roles where directed, reset sensitive credentials, clean metadata, and reintroduce/rebuild other DCs through the supported plan. The [AD forest recovery procedures](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-procedures) are the operational authority.

#### Recover SYSVOL

Modern SYSVOL uses DFS Replication. A nonauthoritative synchronization rebuilds one DC's SYSVOL from a healthy partner; an authoritative synchronization declares the selected copy primary for recovery. Confirm whether AD database and SYSVOL are both affected, select the trusted source, isolate as the procedure requires, and validate `SYSVOL`/`NETLOGON` shares, DFSR events/state, GPO files, AD GPO objects, replication, and client policy.

#### Troubleshoot AD replication and on-premises AD

Use `repadmin /replsummary`, `repadmin /showrepl`, `dcdiag`, directory/DNS/DFSR events, sites/subnets, connection objects, and naming-context status. Common causes include DNS, time/Kerberos, RPC/firewall, network loss, lingering objects, USN/restore misuse, topology, permissions, or a failed DC. Capture source, destination, partition, last success, consecutive failures, and error code.

For general AD symptoms, verify client site, DC locator, DNS registration, secure channel, account lockout/password policy, SPNs, group membership/token refresh, trust, FSMO availability for the affected operation, database/disk health, and replication convergence. Do not force replication or seize roles until the failure mechanism and returning-node plan are understood.

#### Troubleshoot hybrid authentication and synchronization

Trace the identity lifecycle:

```text
AD source object -> scope/filter -> sync/provisioning engine
-> metaverse/cloud object -> authentication method -> token
-> Conditional Access/resource authorization
```

Check duplicate/invalid attributes, UPN/domain verification, source anchor, filtering, connector space/export errors, staging/active server, agent/service account, password-hash or pass-through agent health, federation endpoints/certificates where used, Seamless SSO, password writeback, and Entra sign-in/provisioning logs. A synchronized object does not prove authentication succeeded, and successful authentication does not prove application authorization.

#### Monitoring and troubleshooting failure patterns

| Symptom | Avoid the shortcut | Better approach |
|---|---|---|
| CPU alert fires | Resize immediately | correlate queue, process, workload, host, duration, and baseline |
| No Sentinel alerts | Assume no threats | prove local events, AMA/DCR flow, query/rule schedule, and alert action |
| VM shows Running | Assume OS is healthy | inspect boot/serial/agent/app transaction |
| DNS name fails | Hard-code an IP | locate resolver/delegation/record/cache error and preserve identity behavior |
| Replication error | Force sync repeatedly | identify partner, partition, DNS/time/RPC/topology cause |
| Deleted user restored | Declare recovery complete | validate parent, groups, ACLs, replication, sync, and application access |

#### Primary references

- [Windows Server management documentation](https://learn.microsoft.com/en-us/windows-server/administration/manage-windows-server)
- [Manage servers with Windows Admin Center](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/use/manage-servers)
- [Azure Monitor alerts overview](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview)
- [Troubleshoot Azure Windows VMs](https://learn.microsoft.com/en-us/troubleshoot/azure/virtual-machines/windows/welcome-virtual-machines-windows)
- [Windows Time Service tools and settings](https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)
- [AD forest recovery: determine how to recover](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-determine-how-to-recover)

---

## 7. Integrated scenarios

### Scenario A: Secure and recover a hybrid file service

A regulated organization runs a two-node SOFS/S2D workload and an Azure-hosted management tier. It requires local node maintenance without outage, recovery after site loss, protected administrative credentials, and auditable security events.

Design response:

1. Convert business requirements into node/site failure set, RTO/RPO, retention, and evidence requirements.
2. Validate symmetric supported S2D hardware/networking, configure quorum witness in an independent failure domain, and prove node drain/failure.
3. Apply role-appropriate server baselines, Windows LAPS, constrained administration, Defender for Identity coverage for DCs, host firewall rules, and protected backup roles.
4. Use MABS or the workload-appropriate backup mechanism for retained independent recovery points; protect the catalog/passphrase and test alternate recovery.
5. If using replication for site recovery, map application-consistent behavior and client redirection separately from backup.
6. Collect selected security/system/cluster/storage events with AMA/DCR and alert on storage degradation, backup failure, agent silence, and privileged change.
7. Run a combined exercise: lose a cluster node, restore a deleted file, and prove the original SMB business transaction and audit trail.

The key insight is that SOFS/S2D availability, backup retention, site recovery, key/credential recovery, and monitoring are five controls—not one “high availability” product.

### Scenario B: Migrate a legacy three-tier application to Azure

An application uses two IIS servers, a database server, AD service accounts, SMB content, static IP references, and a hardware-bound license. The organization wants Azure, but the support team initially asks for a lift-and-shift.

Design response:

1. Discover with Azure Migrate and an application dependency inventory; capture peak performance and owner-validated transactions.
2. Assess rehost versus App Service/container replatforming. Hardware-bound licensing and local filesystem writes are explicit blockers to resolve, not surprises for cutover night.
3. Design identity, DNS, network, certificate, secret, database consistency, load balancer, availability, backup, and monitoring targets.
4. Use Azure Migrate for supported VM movement or workload-specific tooling for replatforming; migrate SMB data with an appropriate service and preserve ACL identity.
5. Test migration in an isolated network, validate every tier and security control, measure RTO/RPO, and load test.
6. Freeze writes, perform final synchronization, cut over traffic, validate, and observe through a defined rollback window.
7. Decommission only after business acceptance, backup/restore proof, monitoring, support, licensing, and security evidence are complete.

The key insight is that migration method follows workload constraints. Azure Migrate can move servers, but it cannot silently repair application architecture or license terms.

### Scenario C: Recover a compromised identity and server estate

Attackers gained domain privilege, deleted selected objects, tampered with GPOs, and encrypted application servers. Some backups exist, but production identities controlled the vault.

Design response:

1. Invoke incident command and establish whether the identity authority and recovery control plane are trustworthy.
2. Isolate affected networks and preserve Defender, Sentinel, DC, authentication, vault, and key evidence.
3. Select a trusted recovery point based on compromise timeline—not simply the newest copy.
4. Recover the forest using the supported isolated procedure, DSRM credentials, system-state/full-server backups, authoritative decisions, credential resets, and clean reintroduction.
5. Restore workloads into a controlled clean network, using protected keys and independent recovery identities.
6. Validate directory replication, DNS/time, privileged groups, GPO/SYSVOL, hybrid sync, applications, and monitoring before reconnecting users.
7. Remove persistence, rotate secrets/keys, re-establish backup immutability and role separation, and retain evidence.

The key insight is that normal availability automation can spread compromised state. Cyber recovery prioritizes a trusted state and authority boundary over the fastest possible restart.

---

## 8. Hands-on labs

These labs are independent practice activities, not reproduced exam or paid-course material. Keep an evidence journal with requirement, diagram, commands/configuration, screenshots or exported state, observed failure, repair, and cleanup. Use disposable resources and estimate Azure cost before deployment.

### Lab 1: Harden a server and prove effective policy

**Goal:** Apply several host controls without losing the ability to explain their effect.

1. Build an isolated domain with one management client and one current Windows Server member.
2. Capture effective firewall, audit, SmartScreen, BitLocker, local administrator, and application-execution state.
3. Configure Windows LAPS to back up a managed password to the lab AD DS; delegate retrieval to a dedicated group.
4. Create a small WDAC policy in audit mode, run approved and deliberately unsigned test binaries, and review Code Integrity events.
5. Apply a narrowly scoped Group Policy security setting; if the server is Windows Server 2025, compare an OSConfig baseline in a separate snapshot/clone.
6. Turn on firewall logging and create a service-specific allow rule plus a safe blocked-connection test.
7. Retrieve and rotate the LAPS password with authorized and unauthorized identities.
8. Roll back policy and prove the intended original management/application transaction.

**Evidence:** resultant policy, LAPS directory permissions and events, WDAC audit records, firewall effective rules/log, BitLocker status, baseline version, and rollback result.

**Questions:** Which controls prevented, detected, and recovered? Which exception was truly necessary? Which policy source won?

### Lab 2: Build and fail a two-node cluster

**Goal:** Explain membership, quorum, clustered role, client path, and failure separately.

1. Create two supported nested-lab servers with multiple networks if your platform allows it; do not use an unsupported lab as evidence for production design.
2. Install Failover Clustering, run validation, and preserve the report.
3. Create a domain-joined or workgroup cluster according to your learning target.
4. Configure an appropriate witness and inspect dynamic votes.
5. Add a simple clustered role and storage appropriate to the lab; record preferred owners, dependencies, and failover policy.
6. Perform a planned move, stop a noncritical network path, and simulate one node failure.
7. Observe cluster events, generated cluster log, client behavior, role ownership, and quorum.
8. Recover the node and prove a controlled move back.

**Evidence:** validation report, network roles, quorum/votes before and after failure, resource dependencies, event timeline, and client transaction.

**Questions:** Which partition could form a majority? Did the role being online prove client access? What capacity remained after failure?

### Lab 3: Explore S2D and cluster updating safely

**Goal:** Connect disk health, storage pool, volume resiliency, node maintenance, and workload availability.

1. Use Microsoft's supported evaluation pattern for S2D in nested VMs only if your hardware/platform supports it.
2. Verify drive eligibility, cluster validation, fault domains, and network configuration.
3. Enable S2D; inspect pool, physical disks, virtual disks, volumes, health service, and storage jobs.
4. Place a nonproduction workload on a volume and collect latency/throughput baseline.
5. Pause/drain one node and observe ownership, storage health, and workload behavior.
6. Run a CAU readiness scan or a controlled manual update sequence; do not update multiple nodes together.
7. Resume the node and wait for all repair/storage jobs and health state to settle.
8. Document the raw-to-usable-capacity and failure-tolerance trade-off.

**Evidence:** physical/virtual disk state, pool capacity, storage jobs, node status, workload transaction, CAU report/readiness, and recovery time.

**Questions:** How much free repair capacity existed? Which signals prevented moving to the next node? What did quorum not protect?

### Lab 4: Back up and restore a Windows workload

**Goal:** Prove that policy, recovery point, credentials/keys, and restored transaction work together.

1. Create an approved Recovery Services vault and configure security, RBAC, redundancy, and alerts before protection.
2. Protect either a disposable Azure VM or an isolated Windows file/folder workload with the correct Azure Backup mechanism.
3. Create data with known content, ACLs, timestamps, and an application-consistent marker if appropriate.
4. Run/observe backup and identify snapshot-tier versus vault-tier state where applicable.
5. Delete or corrupt only the lab data.
6. Restore to an alternate location or new VM, using an isolated network.
7. Validate content hash, ACLs, application behavior, identity/network configuration, agent/extension, and monitoring.
8. Record actual RTO and recovery point age; clean up protected items and vault only through the safe documented sequence.

**Evidence:** policy, job detail, recovery-point type/time, restore selection, key/passphrase custody statement, hashes/ACLs, validation, and cost/cleanup.

**Questions:** What was the real RPO? Which single missing secret would have blocked recovery? Did job success prove service recovery?

### Lab 5: Test replication and recovery orchestration

**Goal:** Compare replicated availability with retained backup.

Choose either Hyper-V Replica in an isolated local lab or ASR in an authorized Azure lab.

1. Define source, target, RTO/RPO, test network, application transaction, and cleanup.
2. Configure receiver/vault, authentication or agent/extension, network mapping, replication policy, and target resources.
3. Enable replication and observe initial synchronization plus health.
4. Create a known data change and calculate replication/recovery-point lag.
5. Perform a test failover into an isolated network; never connect a duplicate identity to production.
6. Validate boot, data point, DNS/network, authentication, and application behavior.
7. For ASR, add a small recovery plan with dependency order and a manual validation gate. For Hyper-V Replica, compare test and planned failover behavior.
8. Clean up the test, verify replication remains healthy, and compare the result with backup retention.

**Evidence:** topology, policy, health, selected recovery point, test output, transaction, actual RTO/RPO, and cleanup.

**Questions:** Which corruption would replication copy? Who redirects clients? What would failback/reprotect require?

### Lab 6: Run a Storage Migration Service pilot

**Goal:** Migrate data, configuration, and server identity through separate verified phases.

1. Build a source file server with representative shares, nested ACLs, local identities where relevant, open files, and a DNS name; build a supported destination and orchestrator.
2. Inventory through SMS and classify warnings/exclusions.
3. Map volumes and transfer selected data.
4. Compare file counts/hashes, shares, NTFS/share permissions, owners, and unsupported items.
5. Run another transfer to measure delta behavior.
6. In an isolated lab, execute cutover and observe source/destination names, addresses, AD objects, DNS, certificates, and restarts.
7. Test representative clients and applications, backup, monitoring, and rollback decision criteria.
8. Keep the renamed source during a simulated observation window; then document a safe decommission sequence.

**Evidence:** inventory, transfer errors, integrity/ACL comparison, cutover timeline, DNS/identity changes, client test, and rollback plan.

**Questions:** Which state did SMS migrate? Which dependency did it not discover? Why can a certificate fail after a successful name cutover?

### Lab 7: Discover and test-migrate with Azure Migrate

**Goal:** Turn discovery evidence into a defensible target and cutover plan.

1. Create an Azure Migrate project and deploy the correct appliance for an isolated Hyper-V, VMware, or physical-style source lab.
2. Use least-privilege discovery credentials and verify appliance time, DNS, outbound access, registration, and source reachability.
3. Allow enough collection to observe workload behavior; inspect discovered configuration and dependencies.
4. Create two assessments with different sizing assumptions and compare readiness, target, cost, and confidence.
5. Remediate one blocker or conditional-readiness item.
6. Configure replication/migration target settings and perform a test migration to an isolated VNet.
7. Validate boot, guest/agent health, DNS/network, identity, application, monitoring, security, and backup.
8. Write—but do not execute unless authorized—the freeze, final synchronization, cutover, acceptance, rollback, and decommission plan.

**Evidence:** appliance health, inventory completeness, assessment assumptions/results, remediation, test target, transaction, and runbook.

**Questions:** What evidence supports the VM size? Which source required agentless versus agent-based migration? What remains outside Azure Migrate?

### Lab 8: Diagnose a multi-layer incident and recover AD safely

**Goal:** Use evidence rather than random repair.

1. Establish a small lab domain with two DCs, one member server, known DNS/time/replication health, Recycle Bin enabled, and recoverable system-state/full-server protection.
2. Configure a Performance Monitor DCS, selected event forwarding or AMA/DCR in an approved sandbox, and an alert for an actionable signal.
3. Introduce one safe fault at a time: wrong client DNS, stopped time service, blocked test port, disconnected monitoring association, or deleted lab OU/user.
4. Record symptom, scope, timestamps, hypothesis, and evidence before repair.
5. Use `Resolve-DnsName`, `Test-NetConnection`, `w32tm`, `repadmin`, `dcdiag`, event logs, DCR/heartbeat queries, and Performance Monitor as appropriate.
6. Restore deleted parent/child objects from Recycle Bin and validate attributes, memberships, replication, and application access.
7. Review—but do not improvise—the DSRM, system-state, SYSVOL, and forest-recovery steps; confirm required credentials/backups are independently available.
8. Repair each injected fault one at a time and rerun the original transaction.

**Evidence:** healthy baseline, fault timeline, collected signals, false leads rejected, change made, original transaction, and updated runbook.

**Questions:** Which tool localized the first broken dependency? Would monitoring have detected its own failure? When would Recycle Bin be insufficient?

The public [MicrosoftLearning AZ-801 lab instructions](https://microsoftlearning.github.io/AZ-801-Configuring-Windows-Server-Hybrid-Advanced-Services/) provide additional official-course exercises. Reconcile their product versions and steps with the October 2025 blueprint and current documentation before use.

---

## 9. Knowledge checks

These are original learning checks written from the public objectives. They are not recalled exam questions and do not predict the live exam.

### Security

1. **A legacy application crashes only after an exploit mitigation is enforced. What is the safest next step?** Identify the executable and exact mitigation from events/effective policy, reproduce in a representative ring, and create the narrowest time-bounded exception only when vendor remediation is unavailable. Disabling Exploit Protection broadly removes unrelated defenses.

2. **Why should WDAC normally begin in audit mode?** Audit data reveals legitimate binaries, scripts, drivers, installers, and update paths before enforcement. It lets administrators explain and correct policy gaps without creating a widespread outage.

3. **A LAPS-managed password never appears in AD DS. Which chain should be checked?** OS support and update level, schema preparation, device join/secure channel, applied policy, device permission to update its own attributes, LAPS operational events, and directory replication. Delegated read permission affects retrieval, not the device's ability to store the password.

4. **Why is adding all administrators to Protected Users risky without a pilot?** Its authentication and credential-caching restrictions can break legacy protocols, delegation, offline use, and some service/administration paths. Test each workflow and preserve a separate protected recovery path.

5. **Sentinel has a DCR and AMA installed, but no security events arrive. What should be proven in order?** The local audit event exists, AMA is healthy, the DCR includes the channel/event, the DCR is associated with this machine, the destination/workspace is correct, and records arrive in the expected table. An analytics rule cannot match data that was never collected.

6. **Why is ADE no longer the default recommendation for a new Azure VM?** Microsoft has announced ADE retirement for September 15, 2028 and recommends encryption at host for new VMs, with Confidential VM options for applicable threat models. AZ-801 still names ADE, so understand its architecture and migration implications.

### High availability

7. **What does cluster quorum protect?** It prevents multiple partitions from independently running the cluster without a majority, reducing split-brain risk. It does not back up data, guarantee application consistency, or provide extra compute capacity.

8. **Why place a cloud/file-share witness outside the clustered sites?** The witness must serve as an independent deciding vote during a site/network partition. A witness that fails with one site may not improve the failure set it was meant to solve.

9. **How do CSV, S2D, and SOFS differ?** CSV is a coordinated cluster namespace/access mechanism for cluster storage; S2D pools node-local drives into distributed storage; SOFS is a clustered SMB role for supported application data. They can work together but solve different layers.

10. **What must happen before CAU advances to the next node?** The updated node should restart, rejoin, pass health checks, resume, and leave roles/storage/repair in an acceptable state while survivors retain capacity. A ping response is not enough.

11. **An Azure cluster's load-balancer probe is healthy but clients fail. What remains to check?** Frontend/rule/backend membership, application port/listener, floating-IP guest configuration, NSG and guest firewall, DNS, authentication, application health, and return path. The probe validates only its configured endpoint.

### Disaster recovery

12. **When is MARS more appropriate than MABS?** MARS fits direct file, folder, and system-state backup from individual Windows machines to a Recovery Services vault. MABS is a dedicated multi-workload protection server with local disk recovery and application/VM coverage.

13. **Why can a successful Azure VM backup still fail the recovery objective?** The restore may lack target quota/network/identity, keys, application consistency, dependency order, current runbook, or enough time. Only a tested service recovery measures actual RTO and usable RPO.

14. **How does ASR differ from Azure Backup?** ASR maintains and orchestrates a recent runnable replica for failover/failback. Backup keeps independent historical recovery points. Replication can copy logical corruption; backup normally has longer point-in-time choices.

15. **Which failover type should be used to test Hyper-V Replica without stopping the primary VM?** Test failover, using an isolated network and a selected recovery point. Planned failover is for an intentional move with the primary available; unplanned failover handles primary loss.

16. **Why must an encrypted-VM recovery plan include key operations?** Disk data is useless without the correct enabled/reachable key or secret, identities, permissions, network path, and encryption metadata. Restores can also have encryption-model-specific limitations.

### Migration

17. **What are the three SMS phases?** Inventory, transfer, and optional cutover. Cutover can move the source name and IP identity to the destination; it does not erase the source data.

18. **Why should Azure Migrate collect performance across a representative period?** Target sizing and cost based on a quiet or short sample can miss peak and business-cycle demand. The assessment's percentile, history, and comfort assumptions must be explicit.

19. **When might clean migration be preferable to in-place upgrade?** When the source is old, unsupported, compromised, poorly understood, hardware-constrained, or needs major redesign. A clean target avoids carrying all accumulated OS state but requires complete workload/configuration migration.

20. **Why is ADMT in the guide even though its codebase is deprecated?** The October 2025 official blueprint explicitly names it. Candidates need the concepts, while production planners must heed Microsoft's unsupported-modern-OS/best-effort policy and choose a currently supported migration approach.

### Monitoring and troubleshooting

21. **Why record a healthy Performance Monitor baseline?** Many counter values have no universal “bad” threshold. A comparable healthy period lets operators distinguish normal workload behavior from resource saturation or a regression.

22. **A VM is `Running` but unreachable. What layers should be separated?** Azure control-plane/power state, route/NSG/load balancer, guest boot, VM agent/extensions, guest firewall/listener, DNS, authentication/authorization, and application transaction.

23. **What is the difference between restoring an AD object from Recycle Bin and a forest recovery?** Recycle Bin restores selected deleted objects into a functioning directory. Forest recovery rebuilds trusted directory authority after catastrophic or compromise-level failure using isolated DC/system-state procedures.

24. **A hybrid user is present in Entra ID but cannot sign in to an app. Why is “sync works” insufficient?** Object provisioning, authentication method/agent/federation, token issuance, Conditional Access, and application authorization are separate stages. Trace the user through each stage and its logs.

### Readiness prompts

You are ready to move from broad review to targeted remediation when you can do all of the following without relying on product-name recognition:

- choose among preventive host controls and explain policy source, evidence, compatibility, and rollback;
- trace directory privilege, authentication, NTLM fallback, Defender for Identity, Sentinel, and Defender for Servers boundaries;
- design node, site, witness, storage, network, workload, update, and client behavior for a cluster;
- derive backup, replication, failover, recovery point, key, and restore-test decisions from RTO/RPO;
- choose an SMS, Azure Migrate, workload-specific, forest-upgrade, or restructure path and define acceptance/rollback;
- construct a DCR/alert and diagnose connectivity, update, time, boot, performance, extension, encryption, storage, and AD failures from evidence;
- explain every **VERIFY CURRENT**, **LEGACY/RETIRED**, and retirement notice in this guide.

---

## Places to learn

This is **not a complete list**, and it is not meant to be consumed end to end. Pick the combination that fits your experience, access, learning style, available time, and weak objectives. A productive plan is often one primary course or book, the official blueprint/documentation, hands-on labs, and one legitimate practice assessment used diagnostically.

Time estimates below describe content consumption, not total preparation. Add lab time, note-taking, documentation lookup, spaced review, and remediation. Provider catalogs, access, schedules, prices, durations, and blueprint alignment can change; verify them before purchase. Older material can still teach durable Windows concepts, but reconcile it with the October 2025 baseline, Windows Server 2025 additions, retired agents, ADE's announced retirement, and the AZ-801 exam retirement.

### Microsoft resources

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official AZ-801 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-801) | Free | 30–60 min to map; revisit weekly | Authoritative scope, weights, objective checklist, retirement status |
| [AZ-801T00 self-directed learning and course](https://learn.microsoft.com/en-us/training/courses/az-801t00) | Self-directed modules free; instructor-led varies | Microsoft lists 4 instructor-led days; estimate 30–45 hours self-paced with exercises | Structured first pass across all five domains |
| [MicrosoftLearning AZ-801 labs](https://microsoftlearning.github.io/AZ-801-Configuring-Windows-Server-Hybrid-Advanced-Services/) | Public; infrastructure may cost | Estimate 12–20 hours for seven labs plus setup/cleanup | Guided implementation and troubleshooting practice |
| [Microsoft Learn practice assessments](https://learn.microsoft.com/en-us/credentials/certifications/practice-assessments-for-microsoft-certifications) | Free; sign-in may be required | 1–2 hours per attempt plus remediation | Baseline and later diagnostic assessment; Microsoft lists AZ-801 as available |
| [Exam Readiness Zone AZ-801 search](https://learn.microsoft.com/en-us/shows/exam-readiness-zone/?terms=AZ-801) | Free | Estimate 2–4 hours, depending on available sessions | Objective review; confirm recording date against current baseline |

### Courses, books, and practice providers

| Resource | Access | Estimated time | Notes |
|---|---|---:|---|
| [Pluralsight AZ-801 path](https://www.pluralsight.com/paths/administering-windows-server-hybrid-advanced-services-az-801) | Paid/trial varies | **18 hours** displayed, including six courses and one lab | Tim Warner path plus practice exam; most videos are 2021–2023, while the lab was updated in July 2026, so reconcile older terminology |
| [O'Reilly/Packt: Configuring Windows Server Hybrid Advanced Services Exam Ref AZ-801](https://www.oreilly.com/library/view/configuring-windows-server/9781804615096/) | Paid subscription | **13h 31m** displayed; 602 pages | Chris Gill, April 2023; broad coverage but predates the Windows Server 2025/October 2025 objective revision |
| [O'Reilly/Microsoft Press: Exam Ref AZ-801](https://www.oreilly.com/library/view/exam-ref-az-801/9780137729524/) | Paid subscription | **8h 16m** displayed; 288 pages | Orin Thomas, October 2022; concise older-baseline reference |
| [O'Reilly live-event page: Tim Warner AZ-801 Crash Course](https://www.oreilly.com/live-events/exam-az-801-configuring-windows-server-hybrid-advanced-services-crash-course/0636920065018/) | Paid subscription; schedule/archive availability varies | **6 hours** in the published agenda | Compact objective review; verify whether a current event or recording is available and reconcile Windows Server 2022-era content |
| [Udemy AZ-801 by John Christopher](https://www.udemy.com/course/az-801-configuring-windows-server-hybrid-advanced-services-i/) | Paid; sale pricing varies | **15h 29m**, 133 lectures displayed | Updated August 2026 with demonstrations/simulations; independently verify objective and lifecycle claims |
| [Whizlabs AZ-801](https://www.whizlabs.com/az-801-configuring-windows-server-hybrid-advanced-services/) | Paid | 3 quizzes/110 questions; estimate 3–5 hours plus review | Practice-focused; provider wording includes stale credential terminology, so use the official blueprint for authority |
| [MeasureUp AZ-801 practice test](https://www.measureup.com/microsoft-practice-test-az-801-configuring-windows-server-hybrid-advanced-services.html) | Paid | 120 questions displayed; estimate 4–7 hours across timed/certification and practice/remediation modes | Released in 2022 and contains older objective/product wording; reconcile explanations with the October 2025 baseline |

Practice products should be used to expose weak domains and reasoning errors, not to memorize items. Avoid any provider offering recalled live questions, dumps, VCE files, or a passing guarantee based on leaked content.

### Supplemental experts and channels

| Resource | Access | Estimated time | Notes |
|---|---|---:|---|
| [John Savill Windows Server YouTube search](https://www.youtube.com/@NTFAQGuy/search?query=Windows%20Server) | Free | Pick by gap; typically 15–90 min per selected video | Strong supplemental Azure/Windows architecture explanations, not a complete AZ-801 course |
| [John Savill public GitHub repositories](https://github.com/johnthebrit) | Free | 1–3 hours to locate and review relevant whiteboards/materials | Companion visuals vary by video/series; respect the license of each repository/file before reuse |
| [Microsoft Reactor YouTube channel](https://www.youtube.com/@MicrosoftReactor) | Free | Pick by topic; typically 1–2 hours per session | Useful Microsoft/community technical sessions; verify date, product version, and objective relevance |
| [Microsoft Windows Server YouTube channel](https://www.youtube.com/@MicrosoftWindowsServer) | Free | Pick by gap; 30–90 min per selected session | Product demonstrations and feature context rather than a single exam path |

### Suggested selective plans

#### Experienced Windows Server administrator, limited Azure experience

1. Map the official blueprint and take the free practice assessment: 2–3 hours.
2. Complete Microsoft Learn sections for Defender/Sentinel, Azure Backup/ASR, Azure Migrate, Arc/Monitor, and Azure VM troubleshooting: 15–25 hours.
3. Complete labs 4, 5, and 7 plus weak-domain official labs: 15–25 hours.
4. Use a targeted Pluralsight, O'Reilly, Udemy, or expert-video section for remaining gaps: 5–12 hours.

#### Azure administrator, limited Windows Server depth

1. Review AZ-800 prerequisites for AD DS, DNS, Group Policy, Hyper-V, SMB/storage, and Windows administration: 15–30 hours depending on experience.
2. Use a complete AZ-801 course/book selectively around clustering, S2D, LAPS/AD security, workload migration, and forest recovery: 15–25 hours.
3. Complete labs 1–3, 6, and 8: 25–40 hours.
4. Use practice assessments to drive another 8–15 hours of documentation and lab remediation.

#### Final review before the retirement date

1. Recheck the official study guide, exam page, retirement page, and AZ-802 replacement route.
2. Rebuild the five-domain objective map from memory and mark weak subobjectives.
3. Revisit the lifecycle distinctions: AMA versus MMA, encryption at host versus ADE, and ADMT objective versus modern support state.
4. Rerun two failure/recovery labs and explain the evidence aloud.
5. Use one legitimate practice assessment, investigate every uncertain answer, and stop memorizing question wording.

Schedule conservatively: Microsoft gives an exact **September 30, 2026, 5:00 PM Central Standard Time** retirement. Availability of test centers, online slots, rescheduling, accommodations, results, and prerequisite exam completion can add lead time. If that path is no longer realistic, use [AZ-802](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-802) rather than rushing an expiring exam.
