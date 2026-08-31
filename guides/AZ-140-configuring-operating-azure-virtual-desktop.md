---
exam_code: AZ-140
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-140
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# AZ-140 Configuring and Operating Microsoft Azure Virtual Desktop Study Guide

> **Independent AI-assisted resource — SOURCE-VALIDATED.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [source-validation record](../docs/SOURCE-VALIDATION.md). The [official AZ-140 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-140) is authoritative.

**Current baseline:** Skills measured as of July 20, 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of August 31, 2026.<br>
**Certification lifecycle:** Active; no retirement or replacement is announced on the [official credential page](https://learn.microsoft.com/en-us/credentials/certifications/azure-virtual-desktop-specialty/) as of August 31, 2026.<br>
**Official source:** [AZ-140 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-140)

## How to use this guide

Learn Azure Virtual Desktop (AVD) as a user connection and state-delivery system, not a collection of portal blades. For every scenario trace:

```text
user identity and license
-> client and workspace/feed discovery
-> Azure Virtual Desktop service authentication and policy
-> host-pool brokering and load balancing
-> session-host identity, health and capacity
-> RDP transport and redirection
-> profile/data/application attachment
-> monitoring evidence and recovery behavior
```

The Microsoft-managed control plane brokers access, while you still design and operate identity, session hosts, images, applications, profile storage, networking, security, monitoring and recovery. A healthy VM does not prove that the feed, broker, agent, authentication, transport, profile or application works.

Use a disposable subscription/tenant or an authorized lab. Session-host VMs, profile storage, Log Analytics, security products, Bastion, firewalls and backup can create cost. Estimate, constrain and remove lab resources deliberately.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Administrator question |
|---|---:|---|
| Plan and implement an Azure Virtual Desktop infrastructure | 40–45% | Can users reach an appropriately sized, licensed and healthy host through resilient network, storage and image designs? |
| Plan and implement identity and security | 15–20% | Are service access, Windows sign-in, administration, data movement and session-host protections independently correct? |
| Plan and implement user environments and apps | 20–25% | Do profiles, policies, clients, redirections and applications deliver a consistent least-privilege experience? |
| Monitor and maintain an Azure Virtual Desktop infrastructure | 10–15% | Can operators see the first failing layer, scale safely, update without drift and recover all required state? |

---

# 1. Architecture and troubleshooting model

## Know the resource relationships

| Resource | Purpose | Common mistake |
|---|---|---|
| Host pool | Collection and brokering configuration for compatible session hosts | Treating it as the VMs themselves |
| Session host | VM that runs user desktops/apps and AVD agents | Assuming “VM running” means “available for connections” |
| Application group | Publishes a full desktop or selected RemoteApps | Treating RemoteApp publication as application control/security |
| Workspace | User-visible grouping/feed of application groups | Assigning users only to the workspace and expecting entitlement |
| Scaling plan | Schedule/capacity policy associated with host pools | Confusing AVD Autoscale with generic Azure Monitor autoscale |
| Image/version | Repeatable OS and application baseline | Patching pooled hosts indefinitely and allowing drift |
| FSLogix container | Portable profile/Office state attached at sign-in | Ignoring storage identity, permissions, latency or container locks |

An application group belongs to a host pool and can be registered to a workspace. Users/groups receive application-group assignments. A session host registers to its intended host pool and reports heartbeat/health. Diagnose each relationship separately.

## Separate the connection layers

1. **Discovery:** Can the supported client subscribe to and display the assigned resources?
2. **Service authentication:** Does Microsoft Entra issue the required token under Conditional Access?
3. **Entitlement:** Is the user/group assigned to the application group and, for Entra-joined hosts, given required VM sign-in rights?
4. **Broker/agent:** Is a suitable session host available, registered and healthy?
5. **Windows sign-in:** Can the selected identity scenario authenticate to the host, preferably through Entra SSO where supported?
6. **Transport:** Which reverse-connect, Shortpath and Multipath paths were negotiated, with what latency/loss?
7. **User state/apps:** Did FSLogix attach, policies apply and the application launch?

Use correlation/activity IDs, Entra sign-in logs, host-pool/session-host status, event logs, client logs, FSLogix logs, network traces and Azure Monitor together. A generic “couldn’t connect” message may originate at any layer.

> **Related item:** AVD uses reverse connect; session hosts normally establish outbound connectivity to the service. Direct inbound RDP from the internet is neither the normal user path nor a substitute for a healthy broker/agent path.

---

# 2. Plan and implement AVD infrastructure (40–45%)

## Assess personas, workloads and capacity

Inventory:

- user locations, concurrency, work schedules and reconnect patterns;
- task, knowledge, power and GPU workload characteristics;
- applications, dependencies, plugins, drivers, update cadence and compatibility;
- display count/resolution, video, audio, conferencing, printing and peripheral needs;
- profile size/churn, OneDrive/Office cache and data-locality needs;
- sign-in-time, input-latency, session-density, recovery and security targets.

Use representative load tests. VM vCPU/memory is only part of density: storage latency, profile I/O, graphics encoding, network bandwidth, antivirus, application contention and per-user processes can set the practical limit. Plan spare capacity for maintenance, failures and demand spikes.

### Pooled versus personal host pools

| Choice | Best fit | Operational consequence |
|---|---|---|
| Pooled, multi-session | Standardized task/knowledge users and high density | Externalize user state, manage image consistency, load-balance sessions |
| Pooled, single-session | Standardized experience with stronger per-VM isolation | Lower density but retains nonpersistent operating model |
| Personal, direct assignment | Stable one-user-to-one-host mapping | VM lifecycle, backup and user-specific state matter more |
| Personal, automatic assignment | First eligible user claims an unassigned host | Assignment inventory and reclaim process are required |

Breadth-first distributes new sessions across available hosts for responsiveness; depth-first fills hosts toward a configured maximum so more hosts can remain stopped. Start VM on Connect can power on hosts for demand, but permissions, startup time and capacity still affect the first user.

## Choose OS, licensing and management scope

Choose a supported Windows 11/10 Enterprise multi-session or single-session image, or Windows Server where requirements and licensing support it. Validate application and agent compatibility, support lifecycle, language and security requirements. Microsoft 365 Apps and multi-session behavior need supported configuration.

AVD access eligibility and the Windows license applied to session hosts are separate from Azure compute cost. Windows client and Windows Server scenarios have different entitlement/RDS CAL requirements. External commercial access can use different licensing constructs.

**VERIFY CURRENT:** supported OS images, licensing eligibility, per-user access pricing, Microsoft 365 Apps support, RDS CAL requirements and Azure Hybrid Benefit before deployment.

Use management groups, subscriptions and resource groups to express policy, quota, billing, regional and lifecycle boundaries. Keep control-plane resources, session hosts, images, profile storage and shared monitoring aligned with ownership and recovery—not merely in one large resource group.

## Plan network capacity and paths

RDP adapts to content and network conditions. Estimate bandwidth from personas, display configuration, media/redirection and concurrency, then measure. Latency, jitter and packet loss are as important as throughput. Place session hosts and profile/app storage close enough for interactive and sign-in performance; trace application/data dependencies too.

The [AVD networking recommendations](https://learn.microsoft.com/en-us/azure/well-architected/azure-virtual-desktop/networking) emphasize regional proximity, RDP Shortpath, QoS in managed networks, accelerated networking where appropriate and synthetic path monitoring.

### Reverse connect, Shortpath and Multipath

- The service first establishes the brokered reverse-connect transport.
- [RDP Shortpath](https://learn.microsoft.com/en-us/azure/virtual-desktop/rdp-shortpath) attempts a more direct UDP transport for managed or public-network cases and falls back when it cannot establish it.
- QoS marking for managed Shortpath can prioritize latency-sensitive UDP only when the complete managed path honors DSCP; QoS does not create bandwidth.
- [RDP Multipath](https://learn.microsoft.com/en-us/azure/virtual-desktop/rdp-multipath) can maintain multiple transport paths and shift when a path degrades; Microsoft recommends Shortpath as the primary transport for maximum resilience benefits.

**VERIFY CURRENT:** client/OS support, rollout state, path/port prerequisites, policy names and preview/GA status for RDP Multipath and modern reconnect behavior.

Do not diagnose from “UDP allowed” alone. Confirm the negotiated transport in connection information/logs and measure the client-to-host path. Forced tunneling, proxies, TLS inspection, asymmetric routes and firewalls can impair service endpoints or transport.

## Plan Azure Private Link

[Private Link for AVD](https://learn.microsoft.com/en-us/azure/virtual-desktop/private-link-overview) controls private access to supported AVD control-plane resources; it does not make every dependency private and is distinct from private endpoints for Azure Files, App Attach storage or other services. Design private DNS, endpoint scope, client/on-premises connectivity, public-access settings and recovery access together.

> **Related item:** A private endpoint changes the DNS answer and route to a service. If some clients resolve public addresses while public access is disabled, authentication can succeed while resource discovery or connection fails.

## Plan profile and application storage

FSLogix containers are VHD/VHDX files opened across SMB in the user context. Choose storage by identity support, latency, IOPS, throughput, concurrent handles/users, capacity, zone/region availability, backup and cost.

| Option | Strength | Design concern |
|---|---|---|
| Azure Files | Managed SMB, broad AVD integration and multiple performance tiers | Identity/Kerberos, share/NTFS permissions, account/share limits and regional resilience |
| Azure NetApp Files | High-performance managed SMB volumes | Capacity pools, delegated networking, AD/Kerberos dependency, regional availability and cost |
| Self-managed file service | Custom control or legacy integration | You own clustering, patching, performance, backup and recovery |

Current [Azure Files AVD guidance](https://learn.microsoft.com/en-us/azure/storage/files/virtual-desktop-workloads) and [Azure NetApp Files FSLogix guidance](https://learn.microsoft.com/en-us/fslogix/how-to-configure-profile-container-netapp) contain explicit concurrency and identity constraints. Recheck them instead of copying sizing numbers.

Use separate shares/volumes or controlled sharding when scale requires it. Place App Attach packages on a supported SMB share in the required region/topology. Apply least-privilege share and NTFS permissions; storage keys are not a general end-user authentication design.

## Implement host pools and session hosts

Implementation sequence:

1. register required providers and establish identity, network, DNS and storage;
2. create host pool with type, preferred application-group type, load balancing, session limit and validation settings;
3. create desktop/RemoteApp application groups and workspace relationships;
4. assign groups using AVD RBAC/data-plane requirements;
5. deploy session hosts from a controlled image and join them to the selected identity system;
6. install/register current AVD agent and boot loader through the supported workflow;
7. validate health checks, policies, profile attach, apps and end-to-end connection;
8. enable diagnostics, scaling and update/recovery operations.

Automate with PowerShell, Azure CLI, ARM or Bicep as supported. Protect registration tokens, make identity join and extensions idempotent, and record versioned parameters. Validate portal-created resources against the same desired state.

Host-pool settings govern load balancing, session limits, validation environments, preferred app-group behavior, Start VM on Connect and RDP properties. Drain mode prevents new sessions but does not terminate existing sessions. Use it before update or removal.

## Create and manage images

Golden-image workflow:

```text
supported marketplace/base image
-> patch and install supported agents/apps
-> optimize and harden
-> validate multi-session behavior
-> generalize
-> publish immutable version to Azure Compute Gallery
-> canary host pool/session hosts
-> phased rollout and rollback
```

[Azure VM Image Builder custom image templates](https://learn.microsoft.com/en-us/azure/virtual-desktop/create-custom-image-templates) can automate build customization and distribution. Control its managed identity, staging resources, network access, versioning and logs. Azure Compute Gallery provides image definitions/versions and regional replication; replication completion is a deployment prerequisite, not an afterthought.

Avoid manual mutation of production pooled hosts. Patch the image, deploy replacement hosts, drain old hosts, validate and remove them. Personal desktops may use a different update/backup strategy because their VM state is user-specific.

### Infrastructure failure modes

| Symptom | Likely layer | Check first |
|---|---|---|
| Feed empty | Assignment/workspace discovery | Application-group assignment, workspace registration, client identity |
| No resources available | Broker/host pool capacity | Host availability, drain mode, session limit, agent heartbeat, assignment |
| Long sign-in | Profile/policy/application | FSLogix logs, SMB latency/permissions, GPO/Intune and login tasks |
| Choppy media | Transport/redirection/capacity | Negotiated path, RTT/loss/jitter, media optimization, CPU/GPU |
| Host created but unavailable | Join/agent/registration | Extension logs, DNS, time, outbound endpoints and token validity |

### Primary references

- [Azure Virtual Desktop prerequisites](https://learn.microsoft.com/en-us/azure/virtual-desktop/prerequisites)
- [RDP bandwidth requirements](https://learn.microsoft.com/en-us/azure/virtual-desktop/rdp-bandwidth)
- [RDP Shortpath](https://learn.microsoft.com/en-us/azure/virtual-desktop/rdp-shortpath)
- [Azure Files for virtual desktop workloads](https://learn.microsoft.com/en-us/azure/storage/files/virtual-desktop-workloads)
- [Create custom images with Azure VM Image Builder](https://learn.microsoft.com/en-us/azure/virtual-desktop/create-custom-image-templates)

---

# 3. Plan and implement identity and security (15–20%)

## Select the identity scenario

Microsoft Entra ID authenticates users to the AVD service. Session hosts can be joined to Microsoft Entra ID, AD DS or Microsoft Entra Domain Services under supported combinations. Users with hybrid scenarios need consistent synchronized identity attributes; cloud-only/external scenarios have feature and storage constraints.

| Join scenario | Useful when | Validate carefully |
|---|---|---|
| Microsoft Entra joined | Cloud-first management and supported modern authentication/apps | Client support, VM login roles, Intune, SSO, legacy app and SMB/Kerberos dependencies |
| AD DS joined/hybrid | Existing domain, Group Policy, Kerberos and legacy application dependencies | DC/DNS reachability, sync consistency, OU/GPO and regional recovery |
| Microsoft Entra Domain Services joined | Managed domain services without self-managed DCs | Supported trust/admin behavior, sync latency, DNS and service limitations |

The [AVD prerequisites](https://learn.microsoft.com/en-us/azure/virtual-desktop/prerequisites) table is the source of truth for supported user/session-host combinations. A user identity existing only in AD DS cannot access the AVD service because the user must be discoverable in Microsoft Entra ID.

## Separate authorization layers

- Azure RBAC on AVD resources controls administration.
- Application-group assignment entitles users to published desktops/apps.
- VM User Login/VM Administrator Login is relevant to Microsoft Entra-joined VM sign-in.
- Local groups, user-rights assignments, application ACLs and file permissions govern in-session access.
- FSLogix storage uses both share/data roles where applicable and NTFS permissions.

Use groups and least privilege. Built-in Desktop Virtualization roles separate contributor, reader, user-session and power-management duties. Avoid granting broad VM Contributor merely to let autoscale or Start VM on Connect operate; assign the documented role to the AVD service principal at the narrow required scope.

## Configure SSO and Conditional Access

[Microsoft Entra SSO](https://learn.microsoft.com/en-us/azure/virtual-desktop/configure-single-sign-on) uses an Entra token for Windows sign-in and enables passwordless/federated methods in supported scenarios. Configuration can include RDP authentication properties, a Kerberos server object for hybrid access and tenant consent.

Conditional Access evaluates AVD service/feed authentication and Windows Cloud Login for session-host SSO. Align policies, MFA and sign-in frequency so users do not receive duplicate prompts or get blocked by an inappropriate device condition. Test Windows App and every supported client type; inspect both sign-in records.

Smart cards and passwordless methods have join, client, certificate/Kerberos and redirection dependencies. “MFA succeeded” proves only that policy step, not host sign-in or resource access.

## Protect the session hosts and data paths

Apply layered controls:

- Defender for Cloud recommendations and regulatory posture;
- Microsoft Defender Antivirus policies, exclusions only where documented, tamper protection and scan scheduling;
- Microsoft Defender for Endpoint onboarding, detection/response and server/multi-session licensing;
- Intune or Group Policy security baselines;
- App Control for Business/AppLocker and Controlled Folder Access;
- Trusted Launch (Secure Boot, vTPM, boot integrity) or supported confidential VMs;
- NSGs, UDRs, Azure Firewall/NVA and documented service endpoints;
- no public inbound RDP; use Bastion or Defender for Cloud JIT for controlled administration;
- least-privilege clipboard, drive, printer, USB, camera, microphone and location redirection.

The current [AVD security recommendations](https://learn.microsoft.com/en-us/azure/virtual-desktop/security-recommendations) warn that RemoteApp is not a security boundary: users may launch other accessible executables unless application control prevents it. New-host-pool redirection defaults have changed over time; set and verify explicit policy.

Trusted Launch protects boot integrity and secrets with vTPM/VBS capabilities. Confidential VMs add hardware-based memory protection but introduce SKU, region, performance and feature considerations. Test profile, image, backup and application compatibility.

**VERIFY CURRENT:** Defender licensing/onboarding, supported security VM types, Intune multi-session policy support, redirection defaults and App Control terminology/behavior.

## Security troubleshooting sequence

1. Identify whether failure occurs at feed, service token, Windows Cloud Login, host sign-in or application/data access.
2. Correlate Entra sign-in logs for both AVD and Windows Cloud Login apps.
3. Review applicable Conditional Access policy results, not only the final error.
4. Verify application-group and VM/local rights independently.
5. Check session-host join state, time, certificates/Kerberos and network dependencies.
6. Use a narrowly scoped test account/policy exclusion only under controlled change; remove it afterward.

### Primary references

- [AVD supported identity prerequisites](https://learn.microsoft.com/en-us/azure/virtual-desktop/prerequisites)
- [Configure Microsoft Entra SSO](https://learn.microsoft.com/en-us/azure/virtual-desktop/configure-single-sign-on)
- [Conditional Access and MFA for AVD](https://learn.microsoft.com/en-us/azure/virtual-desktop/set-up-mfa)
- [Security recommendations for AVD](https://learn.microsoft.com/en-us/azure/virtual-desktop/security-recommendations)

---

# 4. Plan and implement user environments and apps (20–25%)

## Design FSLogix deliberately

Profile Container makes a user profile roam by attaching a VHD/VHDX at sign-in. ODFC Container can isolate selected Microsoft 365 cache data, though current design guidance may favor a single profile container depending on workload. Application Masking controls visibility based on rules; it is not equivalent to uninstalling or an application security boundary.

Key configuration areas:

- enablement and container type/format/size;
- `VHDLocations` or Cloud Cache `CCDLocations`;
- naming/matching and include/exclude groups;
- dynamic disk behavior and compaction;
- local-profile conflict behavior;
- retries, locks and concurrent/multi-session access;
- Office/OneDrive/Teams search and cache behavior;
- logging and redirections exclusions.

Cloud Cache writes to a local cache and multiple configured providers to add resilience, but it increases local-disk, network, synchronization and recovery complexity. A provider outage and a slow provider are different failure modes. Design for acceptable sign-out/flush and conflict behavior instead of assuming “two shares means HA.”

The [FSLogix documentation](https://learn.microsoft.com/en-us/fslogix/) and current storage-specific guides are authoritative. Test sign-in/sign-out, storage loss, locked/stale containers, full disks, concurrent access and recovery.

> **Related item:** A profile container is user state, not a complete data-management strategy. Redirect known folders to OneDrive where supported, keep business data in managed repositories and back up only the state that must be restored.

## Choose, deploy and troubleshoot clients

Client availability and features differ across Windows, web, macOS, iOS/iPadOS, Android/Chrome OS and thin-client platforms. Windows App is the current cross-service client direction, but exact feature support varies. Validate SSO, redirection, display, URI/feed discovery, update channel, proxy and Conditional Access for each client population.

Deploy clients with Intune, software distribution, app stores or managed images. Configure email discovery/feed subscription where required. Troubleshoot client version and logs before changing the host pool.

## Configure experience and RDP properties

RDP properties at the host pool interact with Group Policy/Intune and client capability. Control:

- clipboard by direction and data type;
- drives, printers, USB, cameras, microphones, location and smart cards;
- display/multimonitor, graphics encoding and dynamic resolution;
- audio/video redirection and multimedia optimization;
- session time limits for active, idle and disconnected sessions;
- authentication/SSO and transport settings.

Use the least data movement that satisfies the workflow. Universal Print can replace direct printer redirection for managed cloud printing. Multimedia redirection and Teams optimization move supported media work toward the client to improve scale and quality; verify that optimization is active rather than assuming installation succeeded.

## Deliver applications

| Method | Use when | Trade-off |
|---|---|---|
| Bake into image | Common, stable applications required by most hosts | Image grows; every update produces a new image lifecycle |
| Intune/configuration management | Managed staged installation after deployment | Convergence time and multi-session app support |
| App Attach | Dynamic package assignment without installing into image | Packaging, SMB availability/permissions, registration and app compatibility |
| RemoteApp | Publish selected app entry points | Not an execution security boundary |

Application groups publish full desktops or RemoteApps. Create a RemoteApp entry from an installed/attached executable, set display/icon/start behavior, register its application group to the correct workspace and assign groups. Avoid overlapping desktop/RemoteApp entitlement that produces confusing resource behavior.

[App Attach](https://learn.microsoft.com/en-us/azure/virtual-desktop/app-attach-setup) dynamically attaches supported application packages to user sessions. Package the app, place it on supported SMB storage, register it, assign it and test attach/registration/start/update/remove. As of the review, Microsoft documents Windows Server 2022/2025 support added in April 2026; verify OS, package, client and regional storage prerequisites.

## Microsoft 365 Apps, OneDrive, Teams and browsers

- Configure Microsoft 365 Apps with shared computer activation and supported update channel/architecture.
- Configure OneDrive per-machine and supported multi-session behavior; use Files On-Demand and known-folder strategy deliberately.
- Deploy the current Teams client and the required media-optimization components; validate optimization state, not only app launch.
- Set browser policies, profile/data behavior, extensions, updates and default associations through managed policy.
- Test search indexing, Outlook/Office caches and profile-container growth under representative workloads.

**VERIFY CURRENT:** Microsoft 365 Apps/Teams/OneDrive multi-session requirements, WebRTC/multimedia components, application package formats and App Attach OS support.

### User-environment failure modes

| Symptom | Likely cause | Evidence |
|---|---|---|
| Temporary/local profile | Container path, identity, permission, lock or attach failure | FSLogix operational logs, SMB access, registry/policy result |
| Slow first/each sign-in | Large profile, storage latency, policy/script or app registration | Phase timing, container I/O, policy results, event logs |
| App visible but fails | Package share/registration, dependency, ACL or app compatibility | App Attach state, event log, package and share access |
| Teams calls consume host CPU | Optimization absent/failed | Teams optimization status, client/component version, media logs |
| User can launch unlisted executable | RemoteApp misunderstood | Application control policy and filesystem/process rights |

### Primary references

- [FSLogix documentation](https://learn.microsoft.com/en-us/fslogix/)
- [Azure Files for AVD user profiles](https://learn.microsoft.com/en-us/azure/storage/files/virtual-desktop-workloads)
- [Add and manage App Attach applications](https://learn.microsoft.com/en-us/azure/virtual-desktop/app-attach-setup)
- [Customize host-pool RDP properties](https://learn.microsoft.com/en-us/azure/virtual-desktop/customize-rdp-properties)

---

# 5. Monitor and maintain AVD (10–15%)

## Build end-to-end observability

Configure diagnostic settings for host pools, workspaces/application groups where supported, scaling plans and relevant Azure resources. Install/configure Azure Monitor Agent and data collection for session-host guest telemetry. Use Log Analytics retention and access controls appropriate to operational and privacy requirements.

[Azure Virtual Desktop Insights](https://learn.microsoft.com/en-us/azure/virtual-desktop/insights) combines AVD diagnostics, session data, host performance and configuration into workbooks. Customize workbooks for business populations and failure layers, but retain source queries and alert rules outside a single personal workbook.

Monitor:

- feed/connection failures and round-trip/transport quality;
- host availability, agent health and registration;
- active/disconnected sessions, logon duration and input delay;
- CPU, memory, disk, network and process contention;
- FSLogix attach duration, size, capacity, locks and provider health;
- image/app version compliance and Defender status;
- scaling decisions, excluded hosts and capacity shortfalls.

## Autoscale and capacity

AVD scaling plans define ramp-up, peak, ramp-down and off-peak behavior, load-balancing choices, minimum host percentage/capacity thresholds and user-session actions. The AVD service principal needs the documented power-management RBAC. Associate only compatible host pools and account for time zone/day schedules.

Autoscale can start, drain and deallocate hosts according to policy; it does not correct an undersized host, broken agent, slow profile share or application memory leak. Monitor [Autoscale operations in Insights](https://learn.microsoft.com/en-us/azure/virtual-desktop/autoscale-monitor-operations-insights), including why actions were skipped or failed.

For personal pools, scaling behavior and Start VM on Connect differ from pooled capacity. Protect user work: notify or log off only under agreed policy, and distinguish disconnected from active sessions.

## Update strategy

Pooled immutable approach:

1. build a new image version from versioned inputs;
2. patch/security/app test automatically;
3. deploy canary hosts to validation/test population;
4. compare performance, profiles, apps and connection health;
5. deploy replacement capacity;
6. drain old hosts and handle remaining sessions;
7. remove old hosts while retaining a rollback image/version.

Personal hosts may require in-place Windows Update/Autopatch or another managed ring, plus VM backup if local state matters. Keep AVD agents, FSLogix, Defender, Teams/media components, browsers and apps in the compatibility matrix.

## Backup and disaster recovery

Classify state:

| State | Typical recovery approach |
|---|---|
| AVD definitions | IaC/exported configuration and version control |
| Pooled session hosts | Rebuild from replicated image version |
| Personal desktops | Azure Backup or supported VM recovery if stateful |
| FSLogix profiles | Storage-native snapshots/backup and tested item/container restore |
| Golden images | Azure Compute Gallery replication plus protected build source |
| Apps/packages | Versioned repository and replicated App Attach storage |
| Identity/policy/monitoring | Tenant/platform recovery and configuration-as-code |

For multi-region design, prebuild or automate host pools, identity/DNS/connectivity, images, profile/app storage and monitoring in the recovery region. Workspace/application-group publication and user routing must avoid duplicate or confusing assignments. FSLogix Cloud Cache can improve provider resilience but requires tested consistency/failover; it is not a universal cross-region solution.

The [AVD business continuity guidance](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/azure-virtual-desktop/eslz-business-continuity-and-disaster-recovery) treats profiles, images, application dependencies and control-plane resources separately. Define per-persona RPO/RTO and run connection plus business-workflow tests.

### Operational failure modes

| Symptom | First question | Evidence |
|---|---|---|
| Autoscale leaves hosts running | Capacity/session policy or failed power action? | Scaling-plan logs, sessions, exclusions, RBAC, power state |
| New image increases login time | Image/app/policy or profile regression? | Canary comparison, logon phases, FSLogix and process traces |
| DR hosts run but users cannot work | Which identity/profile/app/network dependency is absent? | Complete connection walk and business validation |
| Insights is empty | Diagnostics/agent/DCR/workspace permission or ingestion? | Diagnostic settings, agent heartbeat, tables, RBAC and time range |
| Restore succeeds but profile is inconsistent | Open container or wrong recovery point? | Container locks, snapshot time, FSLogix logs and user acceptance |

### Primary references

- [Enable Azure Virtual Desktop Insights](https://learn.microsoft.com/en-us/azure/virtual-desktop/insights)
- [Monitor Autoscale operations with Insights](https://learn.microsoft.com/en-us/azure/virtual-desktop/autoscale-monitor-operations-insights)
- [AVD business continuity and disaster recovery](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/azure-virtual-desktop/eslz-business-continuity-and-disaster-recovery)

---

# 6. Integrated scenarios

## Scenario A: Global pooled knowledge-worker desktop

Users in North America and Europe require Windows 11 multi-session, Microsoft 365 Apps, Teams and a consistent profile.

1. Segment personas and measure concurrent demand, displays/media, application and profile behavior.
2. Use regional host pools and images close to users; decide how workspaces and groups expose the right resources.
3. Select identity/join and Entra SSO; align Conditional Access for both AVD and Windows Cloud Login.
4. Size session hosts from load tests and select breadth/depth plus scaling schedules from business patterns.
5. Place FSLogix storage per region; design profile ownership/mobility rather than allowing simultaneous cross-region writes.
6. Enable Shortpath where supported, validate Multipath/transport and Teams optimization, then monitor RTT/loss/input delay.
7. Roll images through canary pools and keep versioned rollback.
8. Test regional loss, profile recovery and user communication.

The design error is “one global host pool because AVD is global.” The control plane can be global while interactive compute, profiles, apps and dependencies remain latency- and region-sensitive.

## Scenario B: Privileged contractor RemoteApps

External contractors require two line-of-business apps but must not move data to unmanaged endpoints.

1. Verify supported external-identity/client/licensing model.
2. Publish RemoteApps through a dedicated host pool/application group and least-privilege group assignment.
3. Apply Conditional Access, MFA and supported device/session controls.
4. Explicitly restrict clipboard types/direction, drives, printing and USB; consider watermarking/screen protection where supported.
5. Apply App Control because RemoteApp alone does not prevent other execution.
6. Segment session-host egress and application/data access with NSGs/firewall/UDRs.
7. Onboard Defender for Endpoint and monitor user/process/data-path evidence.
8. Test offboarding across Entra groups, AVD assignments, profiles and application authorization.

## Scenario C: Image rollout creates profile failures

New session hosts register and accept connections, but many users receive temporary profiles.

1. Stop rollout and keep old hosts available; put suspect hosts into drain mode.
2. Confirm affected image version, region, host and identity population.
3. Compare FSLogix version/configuration, share resolution, Kerberos ticket, share/NTFS access and container locks.
4. Inspect FSLogix operational logs and storage latency/availability.
5. Test a clean user and an affected container to separate base configuration from stale/locked state.
6. roll back or repair through a new image version; do not hand-edit the fleet.
7. Add the missing profile-attach test to canary validation.

---

# 7. Hands-on labs

Use small burstable/session-host VMs only where compatible and shut them down or remove them promptly. Architecture, policy and log-analysis labs can be completed without production-size infrastructure.

## Lab 1 — Persona and capacity workbook

Define three personas with concurrency, application, display/media, profile, security and availability needs. Estimate VM/session density and network/storage demand, then identify what must be load-tested.

**Evidence:** assumption table, formulas, selected host-pool types and rejected alternatives.

## Lab 2 — Automated host-pool deployment

Create a host pool, workspace, desktop application group and two session hosts using Bicep/PowerShell or CLI. Use groups for assignment, protect the registration token and verify resource relationships and health.

**Evidence:** versioned deployment, outputs, end-to-end connection and cleanup plan.

## Lab 3 — Transport and Private Link packet walk

Record discovery, authentication, reverse connect, Shortpath and negotiated transport for two client networks. Introduce a UDP block and observe fallback. Diagram how AVD Private Link and private DNS would change the path.

**Evidence:** connection-information screenshots/logs, RTT/loss comparison and DNS/path diagram.

## Lab 4 — Image lifecycle

Build a custom image template or documented equivalent, install one application, publish an Azure Compute Gallery version and deploy canary hosts. Patch the input and publish a second version; drain and replace the canary hosts.

**Evidence:** build inputs/logs, image versions, validation checklist and rollback proof.

## Lab 5 — Identity and security policy

Configure Entra SSO in a lab, AVD/VM RBAC groups and a report-only/test Conditional Access policy. Add explicit redirection restrictions and Defender/App Control design. Trace both service and Windows Cloud Login records.

**Evidence:** role matrix, policy results, sign-in chain and break-glass/exclusion cleanup.

## Lab 6 — FSLogix failure injection

Configure a profile container on a supported lab share. Measure sign-in, then test wrong NTFS permission, wrong path and an unavailable provider. Diagnose from FSLogix logs and restore normal profile attach.

**Evidence:** configuration, timings, log excerpts and recovery steps.

## Lab 7 — RemoteApp and App Attach

Publish an installed application as RemoteApp, then package/attach a supported test application through App Attach. Assign different groups and verify workspace visibility, attach, launch and removal. State why application control remains required.

**Evidence:** application-group/package state, assignments, user results and update plan.

## Lab 8 — Insights, autoscale and DR tabletop

Enable AVD Insights and diagnostics, create a scaling plan and query a scaling/connection event. Then tabletop loss of the primary region, restoring definitions, profiles, images and apps in dependency order.

**Evidence:** workbook/query, scaling action, RPO/RTO timeline, validation and failback gaps.

---

# 8. Knowledge checks

1. Why can a running session-host VM still be unavailable to users?
2. How do host pools, application groups and workspaces relate?
3. When is depth-first load balancing useful?
4. What does Start VM on Connect not guarantee?
5. Why must network planning include jitter and packet loss?
6. How does RDP Shortpath differ from reverse connect?
7. What problem does RDP Multipath address?
8. Why does QoS require an end-to-end managed path?
9. What does AVD Private Link not privatize automatically?
10. Why is profile storage usually placed close to session hosts?
11. What two permission layers commonly govern an Azure Files FSLogix share?
12. Why are pooled hosts good candidates for immutable replacement?
13. What role does Azure Compute Gallery play?
14. Why must AVD users exist in Microsoft Entra ID?
15. Which authorization is distinct from application-group assignment on Entra-joined hosts?
16. Why can Conditional Access produce two prompts in an SSO design?
17. Why is RemoteApp not an application security boundary?
18. What does FSLogix Cloud Cache add and cost?
19. How should a temporary-profile problem be diagnosed?
20. What proves Teams/media optimization is working?
21. Why is generic Azure Monitor autoscale not the same as an AVD scaling plan?
22. What state should be backed up for a pooled host pool?
23. What makes a multi-region AVD recovery test complete?
24. Which facts must be reverified before production use?

## Answers

1. The AVD agent may be unhealthy/unregistered, the host drained, capacity/session limits reached, identity failed or dependencies unavailable.
2. Session hosts register to a host pool; its application groups publish desktops/apps; a workspace exposes registered application groups as a feed.
3. To fill fewer hosts so unused capacity can remain stopped, within maximum-session and user-experience constraints.
4. That a suitable host starts quickly, permissions are correct, capacity exists, or profile/apps are healthy.
5. Interactive input, graphics and media quality can degrade despite sufficient aggregate bandwidth.
6. Reverse connect is the brokered fallback/service path; Shortpath negotiates a more direct UDP data path when supported.
7. Connection resilience/performance across multiple transport paths when one path degrades.
8. DSCP markings help only if every relevant network segment recognizes and queues them consistently.
9. Profile/app storage, identity, DNS, management and other Azure/application dependencies.
10. SMB latency and throughput directly affect profile attach, sign-in and user-state operations.
11. Azure share/data-plane role or share permission where applicable, plus NTFS ACLs.
12. User state is externalized, so versioned images can replace drifted hosts consistently.
13. It versions and distributes image definitions/versions, including regional replication.
14. Microsoft Entra authenticates and discovers users for the AVD service; AD-only identities are unsupported.
15. VM User Login/Administrator Login plus local Windows rights and resource/application permissions.
16. AVD service authentication and Windows Cloud Login SSO are separate app evaluations; mismatched policies/frequencies repeat authentication.
17. It publishes an entry point but does not prevent an authorized session from launching other accessible executables.
18. Multiple profile providers/local cache and resilience, at the cost of I/O, disk, network, synchronization and conflict complexity.
19. Correlate FSLogix logs with container path, identity/Kerberos, share/NTFS rights, availability/latency and locks.
20. Client/session diagnostic state and media logs show optimization; low host CPU alone is insufficient.
21. AVD scaling plans understand host-pool schedules, session thresholds, drain/logoff and load-balancing behavior.
22. IaC definitions, profiles, images/build inputs, app packages/configuration and any stateful personal desktops—not disposable pooled OS disks by default.
23. Users authenticate, discover resources, connect, attach correct state, run business apps, meet RPO/RTO and have a safe failback path.
24. OS/client/feature support, licensing, SKUs/regions, identity/storage constraints, RDP rollout, security defaults, limits, pricing and retirement/preview status.

---

# 9. Final review checklist

- [ ] I can trace discovery, service authentication, entitlement, brokering, host sign-in, transport and profile/app attach.
- [ ] I can compare personal/pooled and breadth/depth choices from persona and capacity evidence.
- [ ] I can explain reverse connect, Shortpath, Multipath, QoS and Private Link boundaries.
- [ ] I can design Azure Files or Azure NetApp Files profile storage with identity, permissions and recovery.
- [ ] I can automate host pools/session hosts and run an immutable image lifecycle.
- [ ] I can compare AD DS, Entra ID and Entra Domain Services identity scenarios.
- [ ] I can align AVD and Windows Cloud Login Conditional Access for SSO.
- [ ] I can protect hosts and data with Defender, application control, redirection and secure admin access.
- [ ] I can configure FSLogix, clients, experience policies, RemoteApps and App Attach.
- [ ] I can operate Insights, scaling plans, update rings and multi-region recovery.
- [ ] I completed at least one end-to-end deployment and one failure-injection lab.

---

# Places to learn

This is **not a complete list**, and it is not a recommendation to consume everything. Pick the resources and formats that fit you, and use the official July 20, 2026 objectives as the coverage checklist. Estimated times include reasonable note-taking or practice where stated and should be rechecked before purchase.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official AZ-140 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-140) | Free; authoritative scope and change log | 45–75 min initially; 10–15 min before exam |
| [Microsoft Learn AZ-140 course](https://learn.microsoft.com/en-us/training/courses/az-140t00) | Free self-paced paths; instructor-led delivery may be paid; official duration 4 days | 11 hr 57 min displayed path content; plan 24–38 hr with labs |
| [Microsoft free AZ-140 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/azure-virtual-desktop-specialty/?practice-assessment-type=certification) | Free with Microsoft Learn account | 45–90 min per attempt; plan 2–4 hr with remediation |
| [Microsoft Exam Readiness Zone AZ-140 series](https://learn.microsoft.com/en-us/shows/exam-readiness-zone/preparing-for-az-140-plan-and-implement-an-azure-virtual-desktop-infrastructure) | Free four-part 2024 objective review; supplemental to July 2026 changes | About 50 min video; plan 1.5–2.5 hr with blueprint reconciliation |
| [O'Reilly: Mastering Azure Virtual Desktop, Second Edition](https://www.oreilly.com/library/view/mastering-azure-virtual/9781835884140/) | Subscription/book; July 2024, 718 pages; strong implementation depth but pre-dates July 2026 topics | 14 hr 54 min displayed; plan 24–36 hr plus current-doc review |
| [O'Reilly: Securing Cloud PCs and Azure Virtual Desktop](https://www.oreilly.com/library/view/securing-cloud-pcs/9781835460252/) | Subscription/book; June 2024, 396 pages; focused security supplement | 8 hr 22 min displayed; plan 12–18 hr plus current-doc review |
| [Udemy: AZ-140 Azure Virtual Desktop (AVD)](https://www.udemy.com/course/az-140-avd-azure-virtual-desktop/) | Paid; Mahammad Kubaib; updated April 2026 | 23 hr 24 min video; plan 32–45 hr and reconcile July objectives |
| [MeasureUp AZ-140 practice test](https://www.measureup.com/microsoft-practice-test-az-140-configuring-and-operating-microsoft-azure-virtual-desktop.html) | Paid; around 150 questions displayed | Plan 4–7 hr across baseline, review and retest |

### Experienced Azure/desktop administrator route

1. Diff the July 2026 blueprint and complete the Microsoft Learn paths selectively.
2. Build Labs 2, 3, 5, 6 and 8 with evidence.
3. Read current identity, RDP Multipath, App Attach, FSLogix and security documentation.
4. Use practice assessments to target gaps, then repeat the failed scenario in a lab.

**Planning range:** 45–75 focused hours.

### Newer to desktop virtualization route

1. Learn Windows, AD DS/Entra, Group Policy/Intune, SMB/Kerberos, RDP and Azure VM/network/storage fundamentals.
2. Complete the Microsoft Learn course and all eight labs.
3. Use the O'Reilly implementation book selectively, reconciling every volatile topic with 2026 docs.
4. Add security and operations failure-injection practice before assessments.

**Planning range:** 90–140 hours after prerequisites.

---

## Currency and integrity note

This guide is an independent synthesis of public sources. It does not reproduce exam questions and is not an exam dump. Microsoft can change objectives, clients, RDP transport rollout, identity/storage support, images, licensing, security defaults, SKUs, limits, pricing and service behavior. Verify the official blueprint, credential page and linked product documentation before an exam or production decision.
