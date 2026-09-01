---
exam_code: AZ-800
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-800
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: retirement-announced
upcoming_change_checked: 2026-08-31
---

# AZ-800 Administering Windows Server Hybrid Core Infrastructure Study Guide

> **RETIREMENT ANNOUNCED:** Microsoft will retire AZ-800 on **September 30, 2026, at 5:00 PM Central Standard Time**. AZ-801 retires at the same time. After that transition, [AZ-802](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-802) will remain the available exam path for the [Windows Server Administrator Associate certification](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-administrator-associate/). New learners should normally prepare for AZ-802; use this guide when you are already committed to taking AZ-800 before retirement or need the underlying infrastructure knowledge.

> **Independent AI-assisted resource — SOURCE-VALIDATED.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [source-validation record](../docs/SOURCE-VALIDATION.md). The [official AZ-800 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-800) is authoritative.

**Current baseline:** Skills measured as of January 21, 2026<br>
**Upcoming blueprint change:** No later blueprint revision is shown, but the exam itself has an announced retirement.<br>
**Certification lifecycle:** AZ-800 and AZ-801 retire September 30, 2026, at 5:00 PM Central Standard Time. Microsoft identifies AZ-802 as the remaining replacement path; passing one old exam does not imply automatic transition credit, so verify your credential status and scheduling plan on the official page.<br>
**Course lifecycle:** Microsoft course AZ-800T00-A also retires September 30, 2026 and is replaced by AZ-802T00-A.<br>
**Official sources:** [AZ-800 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-800) · [exam page](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-800/) · [retirement list](https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams) · [replacement credential](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-administrator-associate/)

## How to use this guide

Study AZ-800 as one hybrid operating system rather than separate on-premises and Azure lists. For every service, trace five paths:

```text
identity -> authentication -> authorization
name resolution -> route/firewall -> service endpoint
desired state -> management channel -> local execution
data owner -> namespace -> storage copy -> recovery copy
signal -> collection -> alert -> diagnosis -> repair
```

When a scenario fails, locate the first broken path. A user can authenticate but be denied by an ACL. A server can appear in Azure Arc while its workload continues normally during a management-plane outage. A private IP route can work while DNS returns the wrong address. A file can exist in Azure Files while a server endpoint has not finished syncing.

Use an isolated lab domain and an Azure sandbox. Domain controllers, VPN gateways, Bastion, public IPs, Azure VMs, Azure Files, Private Resolver, Update Manager, Automation, Monitor, Defender plans and log ingestion may cost money. Never experiment with trust, replication, delegation, DNS, DHCP, storage, encryption or service accounts in a production forest without authorization and recovery evidence.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, migration, security, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Administrator question |
|---|---:|---|
| Deploy and manage AD DS in on-premises and cloud environments | 30–35% | Can identities, domain services, replication, policy and hybrid synchronization remain correct across sites and clouds? |
| Manage Windows Servers and workloads in a hybrid environment | 10–15% | Can operators reach, constrain, configure, update and automate servers through appropriate management planes? |
| Manage virtual machines and containers | 15–20% | Can compute workloads run with the correct isolation, hardware, network, availability and lifecycle model? |
| Implement and manage on-premises and hybrid networking | 15–20% | Can clients resolve names, obtain addresses and reach private resources through resilient controlled paths? |
| Manage storage and file services | 15–20% | Can data be placed, authorized, synchronized, accelerated, protected and recovered without confusing the layers? |

---

# 1. Build the hybrid mental model

## Separate the planes

| Plane | Examples | Question to answer |
|---|---|---|
| Identity | AD DS, Microsoft Entra ID, Entra Domain Services | Which authority issues or validates this identity? |
| Management | Windows Admin Center, PowerShell, Azure Arc, Azure Policy | Which channel requests and executes the change? |
| Workload | AD DS, SMB, Hyper-V guest, Windows container | What must remain available even if management is unavailable? |
| Network | DNS, DHCP, routing, VPN, Private Resolver | How does a client discover and reach the correct endpoint? |
| Data | NTFS/ReFS, Azure Files, File Sync, Storage Replica | Which copy is authoritative, cached, replicated or recoverable? |
| Evidence | logs, agent status, replication state, metrics | What proves desired and actual state agree? |

Azure control-plane success does not prove guest success. An Azure VM can be `Running` while Windows is hung; an Arc resource can exist while its agent is disconnected; a policy assignment can exist while remediation has not completed.

## Distinguish the three directory services

| Service | Operated by | Primary use | Important boundary |
|---|---|---|---|
| AD DS | Your administrators | Domain join, Kerberos/NTLM, LDAP, Group Policy, trusts, traditional Windows workloads | You design and operate DCs, replication, DNS, backup and recovery |
| Microsoft Entra ID | Microsoft SaaS control plane | Cloud identity, OAuth/OIDC/SAML, Conditional Access, Azure/Microsoft 365 access | It is not a cloud-hosted replacement DC and does not expose normal AD DS administration |
| Microsoft Entra Domain Services | Microsoft-managed domain controllers | Managed domain join, LDAP, Kerberos/NTLM and GPO for Azure workloads | You do not hold domain/enterprise admin or manage DC lifecycle; object/password-hash flow has constraints |

A synchronized user can represent the same person in AD DS and Entra ID, but the directories remain different security authorities with different tokens, protocols and administrative surfaces.

### Join Windows Server to the correct directory

| Join state | What the server uses | Typical fit |
|---|---|---|
| AD DS domain joined | Your writable AD DS domain controllers, DNS, Kerberos/NTLM and domain GPO | Traditional and hybrid Windows Server workloads needing full AD DS capabilities |
| Entra Domain Services joined | Microsoft-managed domain controllers in the managed domain | Azure-hosted legacy workloads that need domain join/LDAP/Kerberos without self-managed DCs |
| Microsoft Entra joined | Entra device identity and modern cloud authentication/management capabilities supported for the Windows Server release/scenario | Cloud-first server scenarios that do not require traditional domain services |

Before joining, verify edition/version support, DNS points to the directory's resolvers, time is correct, the computer name/site/OU is intentional and the joining identity has only the required delegation. After joining, verify the computer object, secure channel, locator records, applied policy and intended administrative access. Leaving one directory and joining another changes identity and policy dependencies; it is not a cosmetic portal operation.

> **Related item:** Microsoft Entra Kerberos can let supported clients obtain Kerberos tickets for specific cloud resources such as Azure Files. That does not turn Entra ID into general-purpose AD DS.

## Use a dependency-first troubleshooting sequence

1. Confirm scope and time: affected identity, server, site, protocol and first/last known good time.
2. Verify local host health and clock before blaming the cloud or application.
3. Verify client address, gateway, route and firewall path.
4. Verify DNS suffix, queried server, answer, authority and cache.
5. Verify authentication protocol and ticket/token issuance.
6. Verify authorization at every applicable layer.
7. Verify management-agent, extension, sync or replication state.
8. Compare desired state, actual state and the logs from both endpoints.
9. Make one reversible change, record evidence and retest the original transaction.

Time is a hidden dependency for Kerberos, certificates, signed tokens, replication and logs. Establish reliable time sources and compare UTC timestamps before correlating events.

---

# 2. Deploy and manage AD DS (30–35%)

## Design and deploy domain controllers

Treat a domain controller as a security authority, DNS participant and replication partner—not simply a Windows VM. Before promotion decide:

- forest/domain and functional level constraints;
- site and subnet membership, expected replication links and closest clients;
- writable DC, global catalog and DNS roles;
- RODC suitability and password-replication policy;
- system-state backup, restore and forest-recovery responsibilities;
- physical/virtual security, privileged administration path and monitoring;
- Azure VM placement, availability and network dependencies when hosted in Azure.

Install the AD DS role, validate DNS and static addressing, promote with the intended new/existing forest or domain, verify SYSVOL/NETLOGON, replication, DNS registration and time, then test from a client. Do not clone, snapshot-restore or copy a DC as though it were an ordinary application server; use supported virtualization, backup and recovery procedures.

For Azure-hosted DCs:

- place AD DS database, logs and SYSVOL on an appropriate data disk rather than relying on a temporary disk;
- configure the virtual network DNS design deliberately and avoid creating circular DNS dependencies;
- map Azure region/zone placement to AD sites/subnets and actual network latency;
- protect management access without blocking replication, DNS, Kerberos, LDAP, RPC or time requirements;
- preserve multiple failure domains and a tested route to a writable DC.

**VERIFY CURRENT:** supported Windows Server versions, VM SKUs, accelerated networking, disk caching recommendations and availability-zone behavior can change. Confirm the current [AD DS in Azure guidance](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/identity/adds-extend-domain) before production design.

## Understand FSMO roles

| Role | Scope | Why the single owner matters |
|---|---|---|
| Schema master | Forest | Serializes schema updates |
| Domain naming master | Forest | Controls adding/removing domains and application partitions |
| RID master | Domain | Allocates RID pools used to create unique security identifiers |
| PDC emulator | Domain | Password-change priority, time hierarchy, lockout handling and legacy compatibility |
| Infrastructure master | Domain | Updates cross-domain object references under its operating rules |

Know how to discover owners, transfer a healthy role and seize only when the previous owner will not return. After seizure, prevent the old owner from reappearing until it is properly cleaned/rebuilt. A role holder being offline is not automatically an emergency; the affected operation and outage duration determine urgency.

> **Related item:** The forest-root PDC emulator normally anchors the AD DS time hierarchy to a reliable external source. Other domain members follow the domain hierarchy; random independent time sources create authentication and diagnostic problems.

## Choose writable DC or RODC

An RODC holds read-only directory partitions and is useful where physical security or administrative trust is lower and local authentication must survive a WAN interruption. It is not merely a cheaper DC.

| Decision | Writable DC | RODC |
|---|---|---|
| Local directory writes | Yes | Forwarded to writable DC |
| Password caching | Normal | Controlled by password-replication policy |
| Compromise impact | Full writable authority risk | Cached credentials and local scope still matter; reduced, not zero |
| Branch administration | Requires careful delegation | Supports delegated local administration without domain-wide privilege |
| WAN dependency | Replication-dependent | Uncached authentication/write operations need a writable path |

Design the Password Replication Policy (PRP): explicitly allow only appropriate branch accounts, deny privileged accounts, prepopulate when planned offline authentication is needed and inspect which credentials were actually cached before decommission or incident response. Use administrator-role separation for branch maintenance.

## Design forests, domains and trusts

Prefer fewer forests and domains unless a real security, namespace, legal or autonomy boundary justifies more. Domains provide replication and administrative scopes, but a forest is the meaningful AD DS security boundary.

| Trust concept | Meaning |
|---|---|
| Direction | The trusting domain accepts authentication for identities from the trusted domain |
| Transitivity | Whether trust can extend through other trust relationships |
| Forest trust | Connects forest root domains and can be one-way/two-way with authentication scope controls |
| External trust | Connects specific domains, commonly for non-forest-wide or legacy relationships |
| Selective authentication | Requires explicit permission to authenticate to target computers/services |
| SID filtering | Reduces abuse of SID history across trust boundaries; do not disable casually |

Diagram access as `identity domain -> trust direction -> target computer -> local/resource permission`. Trust enables an authentication path; it does not grant resource authorization by itself.

## Map sites, subnets and replication

AD sites model network topology. A subnet object maps client addresses to a site; site links describe intersite replication connectivity, cost and schedule. Missing or wrong subnet mappings can send clients to distant DCs and make a healthy directory look slow.

Within a site, replication favors rapid change propagation. Between sites, the Knowledge Consistency Checker builds a topology influenced by site links, costs, schedules and bridge behavior. DNS application partitions have their own replication scopes.

Troubleshoot replication by asking:

1. Does DNS resolve the correct partner and locator records?
2. Is time close enough and authentication healthy?
3. Are RPC/firewall/routes available in both required directions?
4. Is the connection object/topology present and the naming context correct?
5. What do `repadmin /replsummary`, `repadmin /showrepl`, `dcdiag` and Directory Service/DFS Replication events say?
6. Is the problem transient latency, lingering state, USN/backup misuse or a SYSVOL-specific issue?

Do not use replication-forcing as a substitute for understanding the failure. Record source/destination, partition, last success, error code and topology before repair.

### Primary references

- [AD DS overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)
- [FSMO role placement and optimization](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/fsmo-placement-and-optimization-on-ad-dcs)
- [Active Directory replication concepts](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts)
- [AD DS deployment in Azure](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/identity/adds-extend-domain)

## Manage users, groups and service accounts

Separate identity lifecycle from access assignment:

```text
authoritative person/workload record
-> account created and placed in role groups
-> resource permission assigned to groups
-> use monitored and periodically reviewed
-> access removed promptly
-> account disabled/deleted under retention policy
```

Use role groups rather than direct user ACLs. In a multidomain design, understand group scope:

| Scope | Typical membership/use |
|---|---|
| Global | Accounts or global groups from the same domain; represents a business role |
| Domain local | Members from trusted domains; grants access to resources in its own domain |
| Universal | Forest-wide membership/use; membership changes replicate through the global catalog |

A durable pattern is accounts → global role groups → domain-local resource groups → permissions. Universal groups help across domains but create global-catalog replication considerations.

### Service-account choice

| Account | Use | Main operational issue |
|---|---|---|
| Built-in virtual/local service identity | One machine and supported service | Limited network identity/portability |
| sMSA | Managed password for a service on one host | Single-host placement |
| gMSA | Managed password/SPN for supported service across multiple hosts | KDS root key, host authorization and application support |
| Delegated managed service account (dMSA) | Windows Server 2025 migration from traditional accounts with stronger managed behavior | Newer OS/domain/application requirements |
| Traditional domain user | Only when workload cannot use a managed option | Password rotation, interactive use, SPNs and excessive rights |

For gMSA, create/validate the KDS root key, restrict the principals allowed to retrieve the managed password, grant only required logon rights and resource access, register correct SPNs and test from each allowed host. The managed password solves rotation; it does not automatically provide least privilege.

**VERIFY CURRENT:** dMSA requirements and application support are Windows Server 2025-era and can evolve. Use the current [service-account documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-managed-service-accounts/group-managed-service-accounts/group-managed-service-accounts-overview) for the deployed OS and functional level.

> **Related item:** Kerberos authenticates a service through an SPN associated with the service identity. Duplicate/missing SPNs can cause ticket failure or NTLM fallback even when the account password is correct.

## Implement hybrid identity

Microsoft Entra Connect Sync and Microsoft Entra Cloud Sync both provision directory objects, but they have different agent architecture and feature coverage. Microsoft states that Cloud Sync is the strategic replacement as it reaches functional parity; choose from current requirements rather than assuming all configurations are interchangeable.

| Concern | Connect Sync | Cloud Sync |
|---|---|---|
| Engine placement | Full sync engine on designated server(s) | Lightweight provisioning agents with cloud-managed configuration |
| Common fit | Complex/current Connect features and established deployments | Multi-forest, agent-based resilience and cloud-managed synchronization where supported |
| Resilience model | Active/staging design and operational ownership | Multiple agents can provide local availability |
| Migration | Requires planned scope/attribute/source-of-authority transition | Validate feature parity and pilot scope before cutover |

Synchronization is not authentication. Common sign-in methods include:

- **Password hash synchronization (PHS):** a derived hash representation is synchronized; Entra ID performs cloud authentication. Simple and resilient, and useful as a backup method.
- **Pass-through authentication (PTA):** agents validate passwords against on-premises AD DS; sign-in depends on healthy agents and DC reachability.
- **Federation:** Entra ID redirects authentication to a federation system; highest infrastructure/availability complexity and justified only by requirements.

Staged rollout lets selected groups test managed authentication while a federated domain remains in transition. Plan rollback, agent capacity, exclusions, Conditional Access and user communication. Verify actual sign-in logs rather than assuming a configuration switch changed every user's path.

For sync scope and object health, know source anchor/immutable identity concepts, UPN/routable domain requirements, attribute flow, filtering, accidental-delete protection, duplicate/conflict handling and soft/hard match risks. Do not edit synchronized cloud attributes without understanding source of authority.

### Entra Domain Services

Use Entra Domain Services when Azure workloads require domain join, LDAP, Kerberos/NTLM or GPO but you do not want to operate DC VMs. Expect a managed domain with delegated administrative capabilities, not enterprise/domain administrator ownership. Password hashes needed for NTLM/Kerberos must exist in the managed domain; existing cloud users can require a password change/synchronization path before those protocols work.

> **Related item:** Microsoft Entra Connect Health supplies health/usage signals for supported hybrid identity components. It complements product logs and monitoring; it does not replace server, agent, directory and sign-in troubleshooting.

Manage Connect Health as its own telemetry path: install the supported agent on each monitored Connect Sync/AD DS/AD FS server as applicable, provide its required outbound connectivity and least-privilege portal access, and respond to alerts, sync insights and object-level synchronization errors. Confirm data freshness before treating a green or red portal state as current. The [Connect Health for Sync documentation](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-health-sync) identifies current prerequisites, alert behavior and agent coverage.

### Primary references

- [Microsoft Entra Connect Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-whatis)
- [Microsoft Entra Cloud Sync overview](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-cloud-sync)
- [Staged rollout](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-staged-rollout)
- [Microsoft Entra Domain Services overview](https://learn.microsoft.com/en-us/entra/identity/domain-services/overview)

## Implement Group Policy and Preferences

A Group Policy Object contains computer/user configuration. It applies through site, domain and OU links, subject to inheritance, enforcement, block inheritance, security filtering, WMI filtering and loopback processing. Within the normal LSDOU sequence, later applicable settings generally win when they conflict, but settings can merge and enforcement changes precedence behavior.

Operational method:

1. Define a narrow outcome and target group/computers.
2. Create a dedicated GPO; avoid turning Default Domain Policy into a general settings bucket.
3. Link at the smallest stable OU/site/domain scope.
4. Use security filtering for authorization to apply, not as an undocumented exception maze.
5. Pilot, use `gpresult`/Resultant Set of Policy and inspect GroupPolicy operational events.
6. Separate configuration failure from replication, SYSVOL, DNS and client-side-extension failure.
7. Document rollback and ownership.

Group Policy Preferences configure items such as files, registry, drives, local users/groups and scheduled tasks with item-level targeting. Preferences are not an enforcement/security boundary by default and can tattoo state when settings no longer apply, depending on action and option. Never place passwords in Group Policy Preferences; historical `cpassword` material is recoverable and should be remediated.

For Entra Domain Services, use the delegated management model and its supported administrative VMs/tools and GPO scopes. You do not manage the managed DCs directly.

> **Related item:** Central Store ADMX templates affect the administrative editing experience and available policy definitions; they do not automatically change client behavior. Client OS/version support determines whether a setting is understood.

### Failure patterns

| Symptom | Likely layer | Evidence/action |
|---|---|---|
| New user exists on-prem but not in cloud | Sync scope/agent/export/conflict | Synchronization Service/provisioning logs and object error |
| User exists but cloud sign-in fails | Authentication method/UPN/Conditional Access | Entra sign-in logs plus agent/DC evidence |
| User can sign in but share denies access | Group token/share RBAC/ACL | Effective groups, Kerberos ticket, RBAC and NTFS ACL |
| Client uses distant DC | Missing/wrong subnet-site mapping | `nltest /dsgetsite`, locator DNS and subnet objects |
| GPO appears linked but not applied | Scope/filter/replication/client extension | `gpresult /h`, event log, SYSVOL and AD replication |
| RODC branch users fail while WAN is down | Credentials not cached/PRP denied | PRP resultant policy and cached-account list |

---

# 3. Manage Windows Servers in a hybrid environment (10–15%)

## Choose the remote-management channel

| Channel | Strength | Boundary to remember |
|---|---|---|
| Windows Admin Center | Browser-based server/cluster management and Azure integration | Gateway identity, delegation and target connectivity still matter |
| PowerShell remoting | Repeatable automation and fan-out | WinRM/SSH transport, authentication and second-hop behavior |
| JEA endpoint | Role-capability-constrained PowerShell | Endpoint design, transcript/logging and escape-path testing |
| SSH | Cross-platform shell/remoting | Host keys, authorized keys and shell/PowerShell subsystem configuration |
| RDP | Full interactive desktop | Broad session capability; restrict through JIT/Bastion/network controls |
| Azure portal/Arc | Azure RBAC, policy, extensions and services over an agent | Cloud resource state is not guest/workload state |

Install Windows Admin Center as a local client or gateway based on who must reach it and what targets it manages. Secure the gateway certificate, access groups, outbound Azure integration and delegation. In Azure, understand whether the experience uses a VM extension or Arc-backed path and what ports/identity it requires.

For SSH, install/enable the supported OpenSSH components, protect host keys, prefer managed public-key authentication where requirements allow, constrain administrators and verify the configured shell or PowerShell subsystem. For Remote Desktop Protocol (RDP), enable only where required, require Network Level Authentication under normal supported conditions, restrict the local Remote Desktop Users/administrator rights, protect the route with firewall/JIT/VPN/Bastion controls and audit sessions. RDP and SSH both provide a transport plus an authenticated session; neither grants permission to every operation inside the server.

## PowerShell remoting, second hop and JEA

The second-hop problem is: client connects to Server B, then code on B needs to access Server C using the caller's identity. Default remoting does not freely delegate that credential.

| Method | Benefit | Risk/constraint |
|---|---|---|
| Resource-based Kerberos constrained delegation | Target-controlled constrained delegation without storing caller password | Kerberos/domain/configuration requirements; WinRM limitations must be checked |
| CredSSP | Straightforward credential delegation | Credentials are exposed to the intermediate server; use only when it is trusted and justified |
| JEA virtual account | Constrained commands, often accesses local/network resources as managed machine identity | Endpoint must be carefully authored on each intermediate server |
| RunAs session configuration | Predictable service identity | Stored/managed credential and shared identity reduce caller attribution |
| Pass explicit credentials | Works for selected command | Secret handling and logging/exposure risk |
| Unconstrained delegation | Broad delegation | Unsafe; do not use as a production shortcut |

Choose the least powerful method that satisfies the transaction. Prove which identity reaches Server C and capture logs at all hops.

JEA combines a session configuration with role capability files. Define allowed cmdlets/functions/providers, constrain parameters, use virtual accounts or gMSA when appropriate and enable transcripts. Test obvious escape routes: arbitrary scripts, aliases, providers, `Invoke-Expression`, native binaries, output-object methods and writable module paths.

### Primary references

- [Windows Admin Center overview](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/overview)
- [PowerShell remoting second hop](https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/ps-remoting-second-hop)
- [Just Enough Administration overview](https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/jea/overview)

## Connect and manage servers with Azure Arc

Azure Arc-enabled servers projects a non-Azure machine into Azure as a resource. The Connected Machine agent provides identity, heartbeat, machine configuration and extension-management components. Azure becomes the management source for those agent actions, but the application workload continues on its host.

Plan onboarding:

- supported OS and agent version;
- resource group, region, tags and Azure Policy/RBAC hierarchy;
- outbound endpoints, proxy/private link and TLS inspection constraints;
- interactive, service-principal or at-scale onboarding identity;
- extension allow/block lists and local agent security controls;
- duplicate/cloned machine prevention and offboarding/incident procedure.

Agent states are diagnostic signals:

- `Connected` means expected heartbeat, not that every extension/workload is healthy;
- `Disconnected` can mean host outage, network block or stopped/broken agent;
- an extended disconnect can cause the resource identity to expire and require reconnection;
- extension status needs its own handler logs and dependency checks.

The [current agent overview](https://learn.microsoft.com/en-us/azure/azure-arc/servers/agent-overview) says supported agents must remain within the one-year support window and documents heartbeat/identity behavior. Treat exact versions and intervals as **VERIFY CURRENT**.

> **Related item:** Azure Arc has two permission boundaries: Azure RBAC/policy controls requested cloud operations, and local agent controls can further restrict what a compromised or overprivileged cloud identity may cause on sensitive servers such as DCs.

## Apply configuration, updates and automation

| Capability | Purpose | Do not confuse with |
|---|---|---|
| Azure Machine Configuration | Audit/enforce guest OS settings through policy/assignments | Azure resource-property policy alone |
| VM extensions | Deploy a specific agent/script/capability through the VM/Arc agent | General package management or application deployment platform |
| Azure Update Manager | Assess, schedule and orchestrate OS updates for supported Azure/Arc machines | Application dependency-aware release orchestration |
| Azure Automation runbook | Execute PowerShell/Python/process automation under an identity | A guarantee that target connectivity, idempotency or rollback exists |

For Machine Configuration, define assignment scope, audit versus enforcement, managed identity/remediation requirements, content trust and excluded systems. For extensions, control publishers/types/versions, automatic upgrade behavior and failure logs.

For updates, distinguish assessment from installation; configure maintenance windows, classifications, reboot behavior, dynamic scope, pre/post actions and reporting. Pilot rings should reflect business services and failure domains rather than random server counts. Domain controllers, clusters and multi-tier applications need workload-aware sequencing.

For runbooks, use managed identity where supported, least-privilege Azure/local permissions, Hybrid Runbook Worker only when target access requires it, encrypted variables/Key Vault for unavoidable secrets, idempotent steps, timeouts/retries and durable job output. A successful job means the script exited successfully—not necessarily that the intended service outcome is healthy.

### Primary references

- [Azure Arc-enabled servers overview](https://learn.microsoft.com/en-us/azure/azure-arc/servers/overview)
- [Azure Arc security overview](https://learn.microsoft.com/en-us/azure/azure-arc/servers/security-overview)
- [Azure Machine Configuration overview](https://learn.microsoft.com/en-us/azure/governance/machine-configuration/overview)
- [Azure Update Manager overview](https://learn.microsoft.com/en-us/azure/update-manager/overview)
- [Azure Automation runbook execution](https://learn.microsoft.com/en-us/azure/automation/automation-runbook-execution)

---

# 4. Manage virtual machines and containers (15–20%)

## Configure Hyper-V hosts and guests

Hyper-V decisions form four layers:

1. host hardware/firmware, OS edition/version, drivers and capacity;
2. virtual compute, memory, storage, devices and switches;
3. guest OS integration, security, checkpoints and management channel;
4. availability, migration, backup and failure-domain design.

### Memory, processor and integration

Static memory fixes startup/assigned memory. Dynamic Memory uses startup, minimum, maximum, buffer and weight to adjust supported guests. Size for peak/guaranteed workload needs and host pressure; maximum is not a capacity plan. Processor compatibility can aid migration across supported CPU generations, while resource controls/weights affect contention rather than creating physical CPU.

Hyper-V CPU controls exist at different scopes. Per-VM reserve, limit and relative weight shape virtual-processor access under supported schedulers. VM resource groups and CPU groups can aggregate/allocate processor capacity for sets of VMs or host processes. The classic, core and root [hypervisor scheduler types](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/manage/manage-hyper-v-scheduler-types) make different isolation, simultaneous-multithreading and ownership tradeoffs; changing scheduler type is a host-wide, restart-sensitive design choice, not routine tuning. Measure workload behavior and confirm the Windows Server release/default before changing it.

Integration services enable host–guest functions such as time synchronization, heartbeat, shutdown, data exchange, backup and guest services. Their value and desired state depend on the workload; for example, domain-controller time behavior requires deliberate design.

Enhanced Session Mode provides richer VMConnect redirection through an RDP-based path. PowerShell Direct manages a Windows guest from its Hyper-V host without relying on guest networking, but still requires guest credentials and a trusted host boundary. SSH Direct provides an analogous host-to-Linux-guest management option under its requirements.

### Device assignment and nested virtualization

- **Discrete Device Assignment (DDA):** gives a supported physical PCIe device exclusively to one VM; strongest direct performance, reduced mobility and hardware/driver/security requirements.
- **GPU partitioning:** shares a supported GPU in hardware-backed partitions; Windows Server 2025 introduced important capabilities including supported live-migration scenarios.
- **Nested virtualization:** exposes virtualization extensions to a guest so it can run Hyper-V/WSL2 or Hyper-V-isolated containers; adds performance and compatibility constraints.

**VERIFY CURRENT:** GPU model/driver/CPU, clustering, live migration, OS edition and nested-virtualization support are hardware- and release-sensitive. Use the current [Hyper-V feature documentation](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/features-terminology).

## Manage virtual disks, checkpoints and availability

| Item | Choice | Consequence |
|---|---|---|
| VHD vs VHDX | Prefer VHDX for modern resilience/capacity unless compatibility requires VHD | Format conversion is separate from disk type change |
| Fixed vs dynamic | Predictable allocation/performance vs space-efficient growth | Dynamic disks still require backing-store capacity monitoring |
| Differencing disk | Child changes reference parent | Parent integrity and chain management are critical; not routine backup |
| Production checkpoint | Uses in-guest backup technology for application-consistent state | Preferred for production workloads where supported |
| Standard checkpoint | Saves VM memory/device state | Can be unsuitable for distributed/transactional production systems |

A checkpoint is not a backup: it depends on the VM/storage lineage, increases differencing I/O and is not an independent recovery copy. Merge/delete it through Hyper-V tools and verify free space.

High availability can involve failover clustering, Cluster Shared Volumes, live migration and Hyper-V Replica, but these solve different failures:

- clustering restarts/fails over a VM after node failure using shared/resilient infrastructure;
- live migration moves a running VM for planned maintenance/load management;
- storage migration moves VM storage;
- Hyper-V Replica maintains asynchronous copies for site/server recovery and requires planned/test/failover operations;
- backup provides point-in-time recovery and retention.

NIC teaming can provide host network redundancy/aggregation under supported modes. Hyper-V virtual switch types are external, internal and private. Map management, cluster, live migration, storage, replication and guest traffic to required isolation/bandwidth without assuming a VLAN alone is a security boundary.

> **Related item:** Shielded VMs and guarded fabrics protect sensitive Generation 2 VMs from compromised fabric administrators through attestation and key protection. Requirements and deployment guidance are version-sensitive; learn the security goal and verify current support before choosing the architecture.

Moving a secure or shielded VM requires the destination host/fabric to be authorized to unlock it. A destination guarded host must attest successfully to an HGS trusted by the VM's shielding data; cross-fabric movement requires planned guardian/key authorization and protected transfer of the VM files. Ordinary live-migration connectivity is not sufficient if the destination cannot obtain key protection. Preserve owner/recovery keys and test the secondary fabric before an outage.

### Primary references

- [Hyper-V overview](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/overview)
- [Hyper-V checkpoints](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/checkpoints)
- [Nested virtualization](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/nested-virtualization)
- [Guarded fabric and shielded VMs](https://learn.microsoft.com/en-us/windows-server/security/guarded-fabric-shielded-vm/guarded-fabric-and-shielded-vms)

## Manage Windows containers

A container image is an immutable layered package; a running container adds an ephemeral writable layer. Persist required data outside that writable layer. Rebuild and redeploy patched base images rather than treating containers like long-lived manually patched servers.

| Isolation | Kernel relationship | Use |
|---|---|---|
| Process isolation | Containers share host kernel | Higher density when host/image compatibility permits |
| Hyper-V isolation | Each container receives a minimal utility VM/kernel boundary | Stronger isolation and broader supported host/image combinations, with overhead |

Windows host and base-image build compatibility is more restrictive than typical Linux container expectations. Validate the exact host, image build and isolation combination using the [current compatibility matrix](https://learn.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/version-compatibility). Patch both hosts and images.

Use a repeatable container lifecycle:

1. Prepare Windows Server as a container host by installing supported container features/runtime and validating virtualization/network prerequisites.
2. If Linux containers are required, configure Windows Subsystem for Linux/WSL 2 or the supported Linux-node/VM architecture; do not mix kernels conceptually.
3. Create a Windows Server container image from a pinned compatible base image and declarative Dockerfile/build definition.
4. Manage container images by tag and immutable digest in an authorized registry; scan, patch and retire old base layers.
5. Create and manage container instances with explicit isolation, identity, resource, volume, port, restart and logging settings.
6. Inspect actual process/health/network state and replace failed or outdated instances from the trusted image.

Common network drivers include NAT for local outbound connectivity, transparent/l2bridge for network-integrated scenarios and overlay for supported orchestration. Diagnose from container namespace outward: endpoint/IP, HNS network, virtual switch, host route/firewall, physical/overlay network, DNS and service publishing.

For Linux containers on Windows, understand whether the implementation uses WSL 2, a Linux VM or orchestration nodes. A Linux container requires a Linux kernel; Windows does not execute it as a Windows process-isolated container.

AKS on Windows Server/AKS hybrid offerings, supported Kubernetes versions and lifecycle have changed over time. **VERIFY CURRENT:** confirm the supported on-premises Azure Kubernetes product, host OS, node-image and support lifecycle before lab or production selection. The objective names the capability; older training may describe a superseded product name.

### Primary references

- [Windows container version compatibility](https://learn.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/version-compatibility)
- [Windows container networking](https://learn.microsoft.com/en-us/virtualization/windowscontainers/container-networking/architecture)
- [Windows containers documentation](https://learn.microsoft.com/en-us/virtualization/windowscontainers/)

## Manage Windows Server VMs in Azure

Separate Azure infrastructure from guest configuration:

| Need | Azure control | Guest control |
|---|---|---|
| Compute capacity | VM size, scale set capacity | processes/services, CPU/memory behavior |
| Storage | disk SKU/size/caching, host encryption | partition, volume, filesystem, BitLocker/application layout |
| Availability | zones, availability set, scale set/orchestration | workload clustering/replication and application health |
| Network | NIC, subnet, NSG, route, load balancer | Windows Firewall, listener, DNS client and application binding |
| Admin access | Bastion, JIT, RBAC | RDP/SSH/WinRM configuration and local authorization |

Resize requires a supported target size and may restart/deallocate the VM. Managed disks can be resized under documented constraints; guest partition/filesystem expansion is a separate step. Availability sets distribute fault/update domains within their scope; availability zones separate datacenter zones in a region. Neither substitutes for application-aware redundancy, backup or cross-region recovery.

VM Scale Sets manage fleets from a model, but stateful Windows Server roles require careful identity, data and upgrade design. Do not scale a DC, file server or arbitrary stateful workload like a stateless web tier without workload-specific architecture.

JIT access uses Defender for Cloud workflow to temporarily open management ports under policy. Bastion provides managed browser/native RDP/SSH connectivity without requiring each VM to expose a public IP. They reduce exposure but do not replace strong identity, endpoint security, patching or session authorization.

Troubleshoot Azure VM network access in order: NIC/private/public IP, subnet, effective routes, NSG effective rules, load balancer/NAT/Bastion path, guest firewall, listener and name resolution. Use boot diagnostics/serial console/run command only under controlled permissions when the normal path fails.

### Primary references

- [Azure VM availability options](https://learn.microsoft.com/en-us/azure/virtual-machines/availability)
- [Azure Bastion overview](https://learn.microsoft.com/en-us/azure/bastion/bastion-overview)
- [Just-in-time VM access](https://learn.microsoft.com/en-us/azure/defender-for-cloud/just-in-time-access-overview)

---

# 5. Implement on-premises and hybrid networking (15–20%)

## Design name resolution

DNS correctness is more than “a name resolves.” Record:

- queried FQDN and suffix-search behavior;
- recursive DNS server used by the client;
- authoritative zone and record owner;
- returned address and TTL/cache source;
- forwarder/delegation/private-zone path;
- reachability from the returned address to the service.

AD-integrated zones store zone data in directory application partitions and use AD replication/security. Choose replication scope intentionally. Dynamic updates should be secure for domain data. Understand A/AAAA, PTR, CNAME, MX, SRV and SOA/NS records; AD locator behavior relies heavily on SRV records.

| Mechanism | Question it answers |
|---|---|
| Delegation | Which authoritative child DNS servers own this subdomain? |
| Forwarder | Where should unresolved queries generally go? |
| Conditional forwarder | Where should queries for this suffix go? |
| Stub zone | Which authoritative servers currently serve another zone? |
| Secondary zone | Do I need a read-only transferred copy of zone data? |
| Private DNS zone link | Which Azure VNets can resolve/use this private namespace? |

DNS policies can vary responses by criteria such as client subnet, time or query context for split-brain, filtering or traffic management. DNSSEC provides origin authentication and integrity for signed DNS data; it does not encrypt queries or prove the destination application is trustworthy. Plan trust anchors, signing/rollover and validation.

## Build hybrid DNS with Azure Private Resolver

Azure DNS Private Resolver avoids maintaining custom DNS forwarder VMs for supported hybrid recursion:

- **inbound endpoint:** on-premises DNS forwards Azure/private-zone queries to an IP in Azure;
- **outbound endpoint:** Azure-originated queries follow a forwarding ruleset toward on-premises/other DNS servers;
- **ruleset and VNet links:** associate suffix rules with the VNets whose queries should use them.

On-premises-to-Azure resolution still needs VPN or ExpressRoute reachability to the inbound endpoint. Inbound and outbound endpoints require dedicated delegated subnets under current rules. Longest matching suffix wins among forwarding rules.

Private endpoint DNS requires the correct `privatelink` zone and links. A connectivity failure that appears after enabling a private endpoint is often a name-resolution design error: the public service name must resolve to the private endpoint address from intended clients.

Keep public hosting separate from private recursion. [Azure Public DNS](https://learn.microsoft.com/en-us/azure/dns/public-dns-overview) hosts authoritative internet zones and records after the parent/registrar delegates the domain to Azure name servers; it is not a recursive resolver for AD DS clients. Azure Private DNS hosts VNet-linked private namespaces, while Private Resolver carries selected recursive queries across hybrid boundaries. Windows DNS can conditionally forward Azure private suffixes and separately host or delegate public names—do not copy private addresses into a public zone to simulate integration.

### Primary references

- [Windows Server DNS overview](https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-top)
- [DNS forwarding](https://learn.microsoft.com/en-us/windows-server/networking/dns/forwarding)
- [Azure DNS Private Resolver overview](https://learn.microsoft.com/en-us/azure/dns/dns-private-resolver-overview)
- [Azure Private DNS overview](https://learn.microsoft.com/en-us/azure/dns/private-dns-overview)

## Manage DHCP and IPAM

DHCP uses a discover–offer–request–ack exchange for new leases and renewal timers for existing leases. A scope defines the network range, exclusions, lease duration and options; a reservation maps a client identifier/MAC to a predictable address. Options can be set at server, scope, reservation or policy levels with precedence/selection implications.

Use DHCP relay/IP helper when clients and servers are separated by routers. Authorize legitimate domain DHCP servers and detect rogue offers. Troubleshoot from the client packet path: link/VLAN, relay, server binding, authorized state, scope activation/free addresses, policies, reservations and option values.

DHCP failover replicates lease state between two supported servers:

| Mode | Behavior | Fit |
|---|---|---|
| Load balance | Both serve clients under configured distribution | Sites with both servers reachable |
| Hot standby | One active, partner reserves capacity for failure | Hub/branch or asymmetric capacity |

Know maximum client lead time, state transitions and planned partner-down decisions. Failover covers DHCPv4 scope lease service under its documented constraints; it is not a backup of every server setting and does not solve a broken relay/network path.

IPAM discovers, inventories and manages IP/DNS/DHCP data and delegated workflows. Configure server discovery/management access and data collection. It helps expose overlap, utilization and configuration state; it does not replace DHCP/DNS authoritative services.

### Primary references

- [DHCP overview](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top)
- [DHCP failover](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-failover)
- [IPAM overview](https://learn.microsoft.com/en-us/windows-server/networking/technologies/ipam/ipam-top)

## Choose remote-access and application-publication paths

| Capability | Best-fit question | Boundary |
|---|---|---|
| RRAS VPN/site-to-site | Do networks or remote clients need routed IP connectivity? | Broad network path; authentication does not authorize every resource |
| Network Policy Server | What RADIUS authentication/authorization/accounting policy applies? | Policy server, not the tunnel or application itself |
| Web Application Proxy | Do I need reverse proxy/preauthentication for supported web/federation scenarios? | Application HTTP(S), not general network access |
| Microsoft Entra Application Proxy | Can an outbound connector publish an on-premises web app with Entra preauthentication? | Web application access, not arbitrary private network protocols |
| Microsoft Entra Private Access | Do users need identity-aware access to private apps/resources beyond a single web proxy? | Global Secure Access licensing/client/connectors and current protocol support |
| Azure Relay | Can an application establish outbound relay connections without opening inbound firewall ports? | Application messaging/hybrid connection pattern, not general routing |
| Azure Network Adapter in WAC | Does a server need a guided point-to-site Azure connection? | Operational convenience with Azure network prerequisites |
| Azure Extended Network | Must selected IP addresses extend across an Azure Local migration boundary? | Specialized L2/IP-preservation scenario, not general hybrid design |

Do not select by product name alone. Define user/device identity, protocols/ports, resource scope, client software, inbound/outbound firewall posture, DNS, high availability, inspection/logging and conditional-access requirements.

For a site-to-site VPN, define local/remote address spaces, tunnel/authentication protocol, certificates or pre-shared-key lifecycle, routing, NAT interaction, redundant endpoints and failover detection. RRAS can terminate the Windows Server side; an Azure VPN Gateway or other peer terminates the remote side. A tunnel-up state proves security-association establishment, not that routes, DNS, firewall rules or the application transaction are correct.

NPS evaluates connection request and network policy based on conditions, constraints and settings. RADIUS clients are access devices such as VPN servers/APs, not end users. Protect shared secrets/certificates, define policy order and inspect NPS accounting/security logs.

**VERIFY CURRENT:** Entra Private Access, Global Secure Access licensing, connector capacity/protocol coverage, Azure Network Adapter and Azure Extended Network support evolve. Recheck official documentation before selecting or implementing them.

### Primary references

- [Remote Access overview](https://learn.microsoft.com/en-us/windows-server/remote/remote-access/remote-access)
- [Network Policy Server](https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-top)
- [Microsoft Entra Application Proxy overview](https://learn.microsoft.com/en-us/entra/identity/app-proxy/overview-what-is-app-proxy)
- [Microsoft Entra Private Access overview](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-private-access)
- [Azure Relay overview](https://learn.microsoft.com/en-us/azure/azure-relay/relay-what-is-it)

### Failure patterns

| Symptom | Likely distinction | First evidence |
|---|---|---|
| IP works, hostname fails | DNS rather than route | `Resolve-DnsName`, queried server/answer/authority |
| Azure VM resolves public endpoint after Private Link | Missing/wrong private zone link/forwarding | effective DNS server and private-zone record/link |
| New clients get APIPA | DHCP/relay/scope path | packet capture, relay, authorization and free leases |
| Reservation gets another address | wrong client identifier/scope/policy or old lease | client ID/MAC and server lease/audit log |
| VPN connects but share fails | resource DNS/route/firewall/auth/ACL | trace each layer after tunnel establishment |
| App Proxy page opens but SSO fails | backend auth/delegation/SPN | connector, preauthentication and backend logs |

---

# 6. Manage storage and file services (15–20%)

## Model file access as layered authorization

For a Windows file server, effective access is shaped by share permission and NTFS ACL, plus identity/group token, claims and policy. For Azure Files over SMB, add identity source and Azure share-level RBAC/default share permission.

```text
identity can obtain Kerberos ticket
AND network can reach SMB endpoint
AND share-level authorization permits action
AND file/directory ACL permits action
= allowed operation
```

The most restrictive applicable share/ACL permission wins. A successful mount does not prove access to every directory. Avoid broad deny entries and direct user ACLs; use groups, inheritance and least privilege, and verify the actual token/effective access.

## Configure Azure Files

Azure Files provides managed SMB and NFS shares, but identity-based Windows authorization in this objective centers on SMB. Current SMB identity sources include AD DS, Entra Domain Services and Microsoft Entra Kerberos for supported scenarios. Select based on client join state, user origin, domain-controller reachability and application protocol requirements.

Azure Files authorization has two layers:

1. share-level access using Azure RBAC roles or a configured default share permission;
2. Windows ACLs at root, directory and file level.

Storage account keys are broad shared secrets and do not identify an individual user; prefer identity-based access. Preserve ACLs during migration with a supported tool/mode and verify owner, inheritance, timestamps, alternate streams and locked-file behavior required by the workload.

Choose share tier/provisioning, redundancy, capacity, transaction characteristics, networking and backup from workload requirements. **VERIFY CURRENT:** share limits, pricing, provisioned models, protocol/identity support and redundancy-region combinations change.

### Primary references

- [Plan an Azure Files deployment](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-planning)
- [Azure Files identity-based authentication](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-active-directory-overview)
- [Azure Files authorization and access control](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-authorization-overview)

## Design Azure File Sync

Azure File Sync synchronizes an Azure file share (cloud endpoint) with one or more Windows Server paths (server endpoints) in a sync group. Cloud tiering can retain namespace/recall pointers locally while less-active file content resides in Azure.

| Object | Meaning |
|---|---|
| Storage Sync Service | Regional management resource for registered servers/sync groups |
| Registered server | Windows Server associated with one Storage Sync Service |
| Sync group | Defines the synchronization relationship |
| Cloud endpoint | One Azure file share; authoritative cloud member of the sync group |
| Server endpoint | A specific path/volume on a registered Windows Server |

Plan topology before copying data. Avoid unsupported overlapping endpoints and understand namespace/data convergence when multiple endpoints change the same file. Antivirus, backup, reparse points, VSS, DFS namespaces and clustered file server configurations need specific guidance.

Cloud tiering combines volume free-space policy and optional date policy. A tiered file still appears in the namespace; opening it recalls content and can create latency/egress. Size the local cache for the active working set and monitor recall success, throughput, cache hit behavior, pending files and server/storage health.

For DFS migration, preserve the user-facing DFS Namespace while replacing folder targets with File Sync-backed servers as appropriate. DFS Replication and File Sync are separate replication engines; do not point both at the same content and hope they coordinate. Sequence seeding, ACL copy, namespace target changes, referral/cache behavior, cutover and rollback.

### Primary references

- [Plan Azure File Sync](https://learn.microsoft.com/en-us/azure/storage/file-sync/file-sync-planning)
- [Choose cloud-tiering policies](https://learn.microsoft.com/en-us/azure/storage/file-sync/file-sync-choose-cloud-tiering-policies)
- [Monitor Azure File Sync](https://learn.microsoft.com/en-us/azure/storage/file-sync/file-sync-monitoring)

## Configure Windows Server shares, FSRM and DFS

SMB share design includes path, share name, availability, access-based enumeration, offline caching, encryption, continuously available behavior and share/NTFS permissions. Use SMB signing/encryption based on threat/path and current defaults; measure performance rather than disabling protection reflexively.

File Server Resource Manager provides:

- quotas: hard stops or soft monitoring thresholds;
- file screens: active blocking or passive reporting by file groups;
- storage reports and classification/management tasks.

FSRM policy helps govern a volume but is not data-loss prevention, malware scanning or a substitute for permissions. Test applications that use temporary extensions or large transactional files before enforcement.

BranchCache reduces WAN traffic by caching content retrieved from an authorized content server. Distributed mode shares cached content among supported clients on one branch subnet; hosted mode centralizes it on one or more branch servers and better fits multi-subnet branches. For SMB, install BranchCache for Network Files on the content server, enable hash publication and configure client mode through policy. Clients must still authenticate and be authorized by the original source before they receive content information; [BranchCache](https://learn.microsoft.com/en-us/windows-server/networking/branchcache/branchcache) accelerates access but does not replace ACLs, DFS, synchronization, offline availability or backup.

DFS Namespaces gives clients a logical UNC namespace with referrals to folder targets. DFS Replication replicates eligible folders between servers. Namespace availability and content replication are distinct. Design referral ordering/site awareness, target health, staging/conflict space and backup. Do not use DFSR for workloads it does not support, such as live database files.

## Compare SMB transport and performance features

| Feature | Purpose | Requirement/boundary |
|---|---|---|
| SMB Multichannel | Multiple connections/interfaces for resilience and throughput | Compatible client/server NIC paths |
| SMB Direct | RDMA for low latency/high throughput/low CPU | RDMA-capable adapters and correct fabric configuration |
| SMB encryption | Confidentiality/integrity of SMB data | CPU/performance/version considerations; can coexist with newer RDMA support |
| SMB signing | Integrity/authenticity against tampering | Current defaults and performance are version-sensitive |
| SMB compression | Reduce transferred bytes for compressible data | Not equivalent to storage compression; interaction with RDMA/features matters |
| SMB over QUIC | SMB 3.1.1 over QUIC/TLS 1.3 for secure access over untrusted networks | Server/client edition/version and certificates |

SMB over QUIC is available in Windows Server 2025 editions and Windows Server 2022 Datacenter: Azure Edition under current documentation. It replaces TCP transport for this session; it does not bypass SMB authentication or ACLs. Certificate identity, client trust, port/firewall and revocation/lifecycle are operational dependencies.

**VERIFY CURRENT:** SMB signing defaults, QUIC editions, client access control, cipher behavior and feature interactions vary by Windows release. Use the current [SMB feature matrix](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-feature-descriptions).

## Configure disks, volumes and filesystems

| Layer | Examples | Failure question |
|---|---|---|
| Physical/virtual disk | local disk, SAN LUN, Azure managed disk, VHDX | Is media/path healthy and visible? |
| Pool/virtual disk | Storage Spaces | Is resiliency/capacity/health intact? |
| Partition/volume | GPT, basic/dynamic volume | Is the volume online and correctly sized? |
| Filesystem | NTFS, ReFS | Is metadata healthy and feature-compatible? |
| Share/application | SMB, CSV, database path | Is access/workload configuration correct? |

Use GPT for modern large disks and UEFI scenarios. Extending the cloud disk/LUN does not automatically extend a partition/volume/filesystem. Keep evidence at each layer before destructive repair.

NTFS has the broadest Windows feature/application compatibility. ReFS emphasizes integrity, availability and virtualization/storage scenarios, but does not support every NTFS feature. Select from workload and current feature matrix, not the name “resilient.”

Storage Spaces pools physical disks and creates virtual disks with simple, mirror or parity resiliency. Columns, interleave, tiers, enclosure awareness and repair capacity affect performance/resilience. Storage Spaces Direct aggregates local disks across clustered nodes for software-defined storage; it adds clustering, network and validated-hardware requirements and is not simply a larger standalone pool.

## Replication, deduplication, QoS and iSCSI

- **Storage Replica:** block-level, crash-consistent volume replication between servers/clusters; synchronous mode targets low-latency zero-data-loss scenarios, asynchronous mode tolerates distance with possible data loss. Replication is not backup because deletion/corruption can replicate.
- **Data Deduplication:** optimizes repeated chunks according to workload policy/schedule; monitor savings, jobs and compatibility. It is not general compression and can add restore/processing dependencies.
- **Storage QoS:** defines/monitors I/O performance policy to control noisy-neighbor behavior in supported Hyper-V/storage designs; verify policy scope and measured IOPS/latency.
- **iSCSI:** carries SCSI block commands over IP between initiator and target. Design isolated/redundant network paths, MPIO, authentication and filesystem ownership. Sharing a block LUN between uncoordinated hosts corrupts data.

SMB Direct operates at file protocol level over RDMA; iSCSI exposes block storage over IP. Storage Replica protects volumes; DFSR/File Sync operate at file/namespace layers. Selecting the wrong layer produces subtle recovery and consistency failures.

### Primary references

- [SMB features](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-feature-descriptions)
- [SMB over QUIC](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-over-quic)
- [Storage Spaces overview](https://learn.microsoft.com/en-us/windows-server/storage/storage-spaces/overview)
- [Storage Replica overview](https://learn.microsoft.com/en-us/windows-server/storage/storage-replica/storage-replica-overview)
- [Data Deduplication overview](https://learn.microsoft.com/en-us/windows-server/storage/data-deduplication/overview)

### Failure patterns

| Symptom | Likely layer | Evidence/action |
|---|---|---|
| Azure share mounts but folder is denied | Windows ACL after share-level gate | effective RBAC and ACL/token |
| User gets access with storage key | Shared key bypasses identity attribution model | remove key usage; configure identity and both permission layers |
| File Sync namespace exists but open is slow/fails | Tiered recall/network/agent/cloud endpoint | recall and sync health metrics, agent/event logs |
| DFS path resolves but file is stale | Namespace referral succeeded; content replication did not | target selected and DFSR/File Sync backlog/state |
| Replica is healthy but deleted file is gone everywhere | Replication copied the deletion | restore from independent backup/version/snapshot |
| RDMA expected but CPU/latency high | SMB Direct path/configuration not active | SMB connection/multichannel counters and NIC/RDMA state |

---

# 7. Integrated scenarios

## Scenario A — Secure branch office with intermittent WAN

**Requirements:** local logon/file access during WAN loss, low-trust physical site, centralized administration and cloud inventory.

1. Map branch subnet to an AD site and configure site-link schedule/cost.
2. Deploy an RODC/DNS with PRP allowing only required branch identities and denying privileged accounts.
3. Prepopulate appropriate credentials; delegate local RODC administration without domain-wide privilege.
4. Use DHCP failover appropriate to link topology and verify relay/DNS options.
5. Present data through a DFS Namespace and a supported File Sync/server-cache design; document what continues offline.
6. Arc-enable non-DC servers with restricted extensions/RBAC; treat Tier 0 onboarding as a separate risk decision.
7. Use JEA for routine constrained tasks and a documented emergency access path.
8. Test WAN failure, uncached account, stale DNS, file recall dependency and recovery—not just normal operation.

## Scenario B — Azure-hosted application using hybrid identity and files

**Requirements:** legacy Kerberos application on Azure VMs, private file access, no public management ports.

1. Decide whether self-managed AD DS in Azure or Entra Domain Services meets administrative/application needs.
2. Design DNS forward and reverse paths with Private Resolver and correct private-zone links.
3. Choose Azure Files SMB identity source; synchronize identities if granular share RBAC requires it.
4. Assign minimum share-level role and NTFS ACL; test the application's service identity and SPN/ticket.
5. Use Bastion/JIT or Arc/WAC/PowerShell for management with role separation.
6. Place redundant application instances across appropriate failure domains and keep state out of local ephemeral paths.
7. Monitor guest, identity, DNS, file and Azure control-plane signals separately.
8. Test loss of on-premises connectivity, DC/DNS failure, expired ticket, denied ACL and storage throttling.

## Scenario C — File-server migration with stable user paths

**Requirements:** preserve UNC namespace and ACLs, minimize downtime, retain rollback.

1. Inventory files, owners, ACLs, unsupported names/types, open-file patterns, throughput and change rate.
2. Choose Azure Files tier/redundancy/network/identity and File Sync topology from data/access needs.
3. Deploy cloud and server endpoints; seed/copy with a supported ACL-preserving process.
4. Monitor initial upload/convergence before enabling aggressive cloud tiering.
5. Add new DFS Namespace target, control referrals and pilot real user/application transactions.
6. Quiesce changes, perform final convergence and move referrals; retain old target read-only for rollback under policy.
7. Validate identity, share RBAC, ACL, namespace, file content/hash, recall latency, backup and restore.
8. Remove old DFSR/target configuration only after evidence and retention approval.

---

# 8. Hands-on labs

## Lab 1 — AD DS topology and RODC branch

Create an isolated forest with two sites/subnets, writable DCs and an RODC. Configure PRP, prepopulate one branch identity, deny a privileged identity, move FSMO roles normally and inspect replication/site locator behavior. Simulate WAN loss.

**Evidence:** topology diagram, FSMO output, PRP/cached-account report, `repadmin`/`dcdiag`, client site/DC selection and failure observations.

## Lab 2 — Hybrid identity decision and staged pilot

Build a lab comparison for Connect Sync and Cloud Sync from current requirements. If a tenant is available, synchronize a tightly scoped test OU, select PHS/PTA as appropriate, inspect provisioning/sign-in logs and design a staged-rollout/rollback runbook. Do not synchronize real identities.

**Evidence:** source-of-authority map, scope/filter, agent health, test-object attributes, authentication-path proof and rollback steps.

## Lab 3 — Group Policy and constrained administration

Create a narrow computer GPO and a preference with item-level targeting. Diagnose it with `gpresult`. Build a JEA endpoint allowing only a harmless service-status/restart function, enable transcripts and attempt prohibited commands. Demonstrate a second-hop need and choose a secure solution.

**Evidence:** GPO scope/result, event log, JEA role/session files, allowed/denied transcript and identity used at the second resource.

## Lab 4 — Azure Arc management lifecycle

Onboard a disposable Windows Server to Azure Arc, tag it, assign audit configuration, deploy one safe extension, assess updates and run an idempotent Automation task. Block connectivity or stop the agent, diagnose state/logs, restore it and offboard cleanly.

**Evidence:** resource/RBAC, agent version/status, policy result, extension log, update assessment, runbook output and disconnect/recovery timeline.

## Lab 5 — Hyper-V VM lifecycle

Create a Generation 2 VM with VHDX, dynamic memory, production checkpoints and an isolated virtual switch. Use PowerShell Direct, resize/expand its disk correctly, compare checkpoint behavior and document a nested-virtualization or device-assignment plan without requiring specialized hardware.

**Evidence:** host/VM configuration export, disk-layer before/after, checkpoint merge proof, management-channel result and availability/recovery design.

## Lab 6 — Windows container compatibility and network

Build a simple Windows container image pinned to a compatible base image, run it with the supported isolation mode, publish a port, persist data outside the writable layer and inspect HNS/network path. Patch by rebuilding rather than editing the running container.

**Evidence:** Dockerfile, host/image build comparison, image digest, isolation/network state, external data proof and rebuilt version.

## Lab 7 — Hybrid DNS and DHCP failure injection

Implement AD-integrated DNS, a conditional forwarder, DHCP scope/reservation/failover and an IPAM inventory in an isolated network. Diagram Private Resolver inbound/outbound endpoints. Break one relay or forwarder path and diagnose from client packet/query evidence.

**Evidence:** zone/records, forwarding path, lease/failover state, IPAM discovery, packet/query trace and corrected root cause.

## Lab 8 — Azure Files and File Sync migration

Create a test SMB share and identity-based access if your sandbox supports it. Apply share-level RBAC and distinct NTFS ACLs, deploy File Sync, enable conservative cloud tiering, copy a test tree with ACLs and expose it through a DFS Namespace plan. Test a tiered recall and restore one file from an independent recovery mechanism.

**Evidence:** identity source, RBAC/ACL effective-access results, sync health, recall metrics, namespace/cutover plan and restore proof.

---

# 9. Knowledge checks

1. Why can a synchronized user authenticate to Entra ID but still fail against an AD DS-protected SMB share?
2. What is the meaningful security boundary in AD DS: domain or forest?
3. When is an RODC useful, and what does its PRP control?
4. Why should an FSMO role be seized only when the old owner will not return?
5. How can a missing AD subnet object affect users when replication is healthy?
6. What access does a trust relationship grant by itself?
7. Why does a gMSA reduce but not eliminate service-account risk?
8. How does synchronization differ from PHS, PTA and federation?
9. What does staged rollout test?
10. Why can a linked GPO still not apply?
11. What is the PowerShell second-hop problem?
12. How does JEA differ from ordinary PowerShell remoting?
13. What does an Arc `Connected` state prove—and not prove?
14. How do Machine Configuration, extensions, Update Manager and runbooks differ?
15. Why is a Hyper-V checkpoint not a backup?
16. When would Hyper-V isolation help a Windows container?
17. Why must Windows container host and base-image versions be checked together?
18. How do availability zones differ from workload high availability?
19. What is the difference between DNS delegation and conditional forwarding?
20. What are Private Resolver inbound and outbound endpoints for?
21. What does DHCP failover not protect?
22. How does Application Proxy differ from a VPN or Entra Private Access?
23. Which two authorization layers usually govern identity-based Azure Files SMB access?
24. How do File Sync, DFS Namespace, DFS Replication and Storage Replica solve different problems?

## Answers

1. Sync links/provisions identities; the SMB path still needs the correct Kerberos authority/ticket, network path, group token, share permission and ACL.
2. The forest; domains are major replication/administrative scopes but do not isolate a hostile forest administrator.
3. A lower-trust or disconnected site needing local read/authentication service; PRP decides which account credentials may or may not cache there.
4. Returning the former holder after seizure can create conflicting authority/unsafe state; transfer healthy roles and seize only after a permanent-loss decision.
5. The client can select a distant site/DC, increasing latency and WAN dependency even though DC-to-DC replication succeeds.
6. An authentication route; the target resource still requires authorization, and selective authentication may add a computer-level gate.
7. Windows rotates/retrieves its password and supports multi-host service identity, but host retrieval rights, SPNs and resource privilege still require control.
8. Sync provisions object/attribute state; PHS, PTA and federation decide where/how password authentication is validated.
9. Whether selected users can use a managed authentication method during a controlled transition, with logs and rollback before domain-wide cutover.
10. Link precedence, inheritance, security/WMI filtering, loopback, replication/SYSVOL or client-side processing can exclude/fail it.
11. Credentials used from client to Server B are not automatically delegated from B to resource C.
12. JEA exposes an intentionally constrained endpoint/role capability instead of the caller's normal broad shell.
13. It proves recent agent heartbeat; it does not prove extensions, policy, OS, application or workload transactions are healthy.
14. Guest desired-state audit/enforcement, discrete agent-delivered capability, patch assessment/orchestration and general automation execution, respectively.
15. It depends on the VM/disk chain, adds runtime I/O/space needs and is not an independently retained recovery copy.
16. When a stronger per-container kernel boundary or a supported host/image compatibility combination is required, accepting extra overhead.
17. Process isolation shares the host kernel and Windows support depends on build compatibility; Hyper-V isolation changes but does not erase requirements.
18. Zones separate Azure infrastructure failure domains; the application must still replicate state, route healthily and fail over correctly.
19. Delegation identifies authoritative servers for a child namespace; conditional forwarding sends matching suffix queries to chosen recursive DNS servers.
20. Inbound accepts queries into Azure resolution; outbound applies rules for Azure-originated queries toward other DNS servers.
21. Every server setting, DNS/network/relay path, IPv6 service, backup or an application that cannot reach DHCP.
22. App Proxy publishes supported web apps through outbound connectors; VPN provides routed network access, while Private Access targets broader identity-aware private application access.
23. Azure share-level RBAC/default permission and Windows directory/file ACLs; the most restrictive applicable access controls the operation.
24. File Sync synchronizes Azure Files/server endpoints and can tier; DFSN supplies a stable namespace/referrals; DFSR replicates supported files; Storage Replica copies volumes at block level.

---

# 10. Final review checklist

- [ ] I can distinguish AD DS, Entra ID and Entra Domain Services and trace a hybrid identity transaction.
- [ ] I can deploy/verify DCs, FSMO, RODC PRP, sites/subnets, trusts and replication.
- [ ] I can choose group scope and a managed service-account type and troubleshoot SPN/Kerberos implications.
- [ ] I can compare Connect Sync/Cloud Sync and PHS/PTA/federation/staged rollout.
- [ ] I can design, apply and diagnose Group Policy and Preferences.
- [ ] I can select WAC, PowerShell/JEA/SSH/RDP or Azure management with correct delegation.
- [ ] I can onboard and secure Arc, then separate agent, extension, policy, update and runbook state.
- [ ] I can configure Hyper-V memory/devices/disks/switches/checkpoints and explain its availability options.
- [ ] I can select Windows container isolation, version and network behavior and rebuild images safely.
- [ ] I can operate Azure VM disk/capacity/availability/admin/network layers without confusing guest state.
- [ ] I can implement AD-integrated/hybrid DNS and diagnose the exact query path.
- [ ] I can implement DHCP scopes/reservations/failover and use IPAM as management evidence.
- [ ] I can choose among VPN/NPS, WAP, App Proxy, Private Access, Relay and specialized Azure connectivity.
- [ ] I can configure Azure Files identity, share RBAC and ACLs as separate authorization gates.
- [ ] I can design File Sync/cloud tiering and migrate a DFS/file-server namespace with rollback.
- [ ] I can compare SMB Multichannel/Direct/encryption/compression/QUIC.
- [ ] I can choose Storage Spaces/S2D, Storage Replica, deduplication, QoS, NTFS/ReFS and iSCSI by layer.
- [ ] I completed at least one identity, one networking and one data-path failure-injection lab.
- [ ] I verified my exam date against the September 30, 2026 retirement and considered AZ-802.

---

# Places to learn

This is **not a complete list**, and it is not a recommendation to consume everything. Pick the resources and formats that fit you. Because AZ-800 retires September 30, 2026, compare the time remaining with the broader value of studying AZ-802. Use the official January 21, 2026 objectives as the AZ-800 coverage checklist. Estimated times include reasonable note-taking or practice where stated and should be rechecked before purchase. Older material can teach durable Windows Server concepts, but reconcile product names, versions and deprecated capabilities with current documentation.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official AZ-800 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-800) | Free; authoritative AZ-800 scope and retirement notice | 45–75 min initially; 10–15 min before exam |
| [AZ-802 replacement blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-802) | Free; compare before committing to the retiring two-exam route | 60–90 min for a scope diff |
| [Microsoft Learn AZ-800 exam/training collection](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-800/) | Free self-paced paths; official instructor-led AZ-800T00 duration is 4 days | Plan 35–55 hr self-paced with labs, or 4 instructor-led days plus review |
| [Microsoft free AZ-800 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-800/practice/assessment?assessment-type=practice&assessmentId=67) | Free; use explanations for remediation, not question memorization | 45–90 min per attempt; plan 3–5 hr with remediation |
| [Official MicrosoftLearning AZ-800 lab instructions](https://microsoftlearning.github.io/AZ-800-Administering-Windows-Server-Hybrid-Core-Infrastructure/) | Free public hands-on course labs; Azure/VM costs may apply | Plan 15–25 hr including setup, evidence and cleanup |
| [Microsoft Exam Readiness Zone AZ-800](https://learn.microsoft.com/en-us/shows/exam-readiness-zone/?terms=AZ-800) | Free objective-review videos; reconcile recording age with January 2026 scope | About 2–3 hr video; plan 3–5 hr with notes/diffs |
| [Pluralsight AZ-800 path](https://www.pluralsight.com/paths/administering-windows-server-hybrid-core-infrastructure-az-800) | Paid; six courses, two labs, 17 displayed hours and practice exam; much course content originated in 2021–2022 | 17 hr media; plan 25–35 hr with labs and 2026 reconciliation |
| [O'Reilly Exam Ref AZ-800](https://www.oreilly.com/library/view/exam-ref-az-800/9780137729333/cover.xhtml) | Paid/subscription; Orin Thomas, August 2022, 304 pages | O'Reilly displayed about 9 hr 35 min; plan 14–20 hr with notes/current-doc checks |
| [O'Reilly Administering Windows Server Hybrid Core Infrastructure AZ-800 Exam Guide](https://www.oreilly.com/library/view/administering-windows-server/9781803239200/) | Paid/subscription; Steve Miles, December 2022, 502 pages | O'Reilly displayed about 10 hr 42 min; plan 18–28 hr with exercises/current-doc checks |
| [O'Reilly AZ-800 video course](https://www.oreilly.com/library/view/az-800-administering-windows/9781836208730/) | Paid/subscription; ACI Learning/Packt, May 2024; verify edition and duration | Estimate 8–14 hr viewing; plan 12–20 hr with labs |
| [Udemy AZ-802 & AZ-800 hands-on course](https://www.udemy.com/course/az-800-course-administering-windows-server-hybrid-core-inf/) | Paid; John Christopher; page showed August 2026 update, 25 hr 38 min and 193 lectures | Plan 35–50 hr with labs and blueprint comparison |
| [Whizlabs AZ-800 training and practice](https://www.whizlabs.com/microsoft-azure-certification-az-800/) | Paid; course/practice/lab packaging and duration can change | Verify current duration; plan 15–30 hr plus targeted remediation |
| [MeasureUp AZ-800 practice test](https://www.measureup.com/microsoft-practice-test-az-800-administering-windows-server-hybrid-core-infrastructure.html) | Paid; page access was blocked during validation, so verify availability, question count and January 2026 alignment before purchase | Plan 4–7 hr across baseline, review and retest |
| [John Savill Windows Server/Hybrid search](https://www.youtube.com/@NTFAQGuy/search?query=Windows%20Server) and [public whiteboards/materials](https://github.com/johnthebrit) | Free supplemental explanations; select AD, Arc, Azure VM, networking and storage topics rather than expecting an AZ-800 course | Select 4–12 hr by weak domain; add hands-on practice |

### Experienced Windows Server administrator route

1. Decide AZ-800 versus AZ-802 from the retirement date and credential page.
2. Diff the January 2026 blueprint against your production experience; do not assume on-premises depth covers Azure identity, Arc, Files or Private Resolver.
3. Complete Labs 2, 4, 6 and 8, then inject one identity, DNS and sync failure.
4. Use practice assessment results to select current Microsoft documentation, not to memorize answer wording.

**Planning range:** 55–85 focused hours if you already operate AD DS, Hyper-V, DNS/DHCP and Windows file services.

### Newer to Windows Server route

1. Start with Windows Server, TCP/IP/subnetting/DNS, PowerShell, Azure fundamentals and identity concepts.
2. Complete the official learning paths and all eight labs in this guide.
3. Use one structured course/book, not every vendor; add focused docs where your evidence is weak.
4. Rebuild one small hybrid environment twice and troubleshoot it from client to identity/network/data path.

**Planning range:** 120–180 hours after foundational operating-system, networking and Azure study. Given AZ-800 retirement, AZ-802 will usually be the more practical certification target.

---

## Currency and integrity note

This guide is an independent synthesis of public sources. It does not reproduce exam questions and is not an exam dump. Microsoft can change objectives, exam availability, replacement paths, Windows/Azure product names, OS editions, licensing, previews, limits, identity methods, Arc agents/extensions, Kubernetes offerings, SMB defaults, storage tiers and service retirements. Verify the official AZ-800 retirement notice, AZ-802 blueprint, credential page and linked product documentation before an exam or production decision.
