---
exam_code: NSE-7-SECURE-NETWORKING
vendor_id: fortinet
official_blueprint: https://training.fortinet.com/local/staticpage/view.php?page=secure_networking_architect_exam
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-10-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-10-28
---

# Fortinet NSE 7 in Secure Networking Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live certification and Secure Networking 7.6 Architect exam pages, current Fortinet documentation, and public program policies were checked October 28, 2026. Fortinet's pages remain authoritative.

**Current baseline:** Secure Networking 7.6 Architect: System configuration and SD-WAN setup 20–30%; Central management 15–25%; Security profiles 5–15%; Rules and routing 25–35%; Advanced IPsec 25–35%. The published ranges overlap and are not normalized point weights.<br>
**Exam contract:** 40–50 questions, 75 minutes, English and Japanese, Pearson VUE, pass/fail, using FortiGate 7.6, FortiManager 7.6, and FortiAnalyzer 7.6. Questions include multiple choice and drag-and-drop; verify the booking screen.<br>
**Delivery:** Since September 21, 2026, NSE 7 exams are available only at Pearson VUE-authorized test centers; OnVUE remote delivery ended. Check current local availability when scheduling.<br>
**Certification contract:** This guide covers the required **NSE 7 Secure Networking exam**, not the entire credential by itself. The credential also requires active NSE 4 FortiOS and either NSE 5 Secure Networking or NSE 6 Secure Networking, with the NSE 7 exam passed within two years of the last prerequisite exam. The credential is active for two years from the later qualifying exam.<br>
**Experience boundary:** Fortinet recommends three years each in networking and network security, plus two years of hands-on work with each of FortiGate, FortiManager, and FortiAnalyzer.<br>
**Upcoming change:** No replacement or retirement was announced September 2, 2026. This comprehensive exam was introduced with the July 15, 2026 program redesign; older FCSS/NSE 7 pages and course names can describe a different contract.<br>
**Integrity:** Use official sample questions only to understand form and scope. Reject recalled, leaked, “real exam,” guaranteed-match, or braindump material.

> **October 28, 2026 delivery check:** The current OnVUE notice limits the four NSE 7 exams to Pearson VUE-authorized test centers effective September 21, 2026. The blueprint and prerequisite rule were also rechecked against the live exam and track pages.

## How to use this guide

Treat every topic as a design-and-troubleshooting case. Draw control and data planes; identify ownership, dependencies, failure domains, configuration source, runtime state, evidence, rollback, and the effect on existing sessions. Practice reading routing tables, session flags, logs, packet captures, and configuration extracts before changing anything.

Use FortiOS 7.6, FortiManager 7.6, and FortiAnalyzer 7.6 in an owned or explicitly authorized lab. Exact behavior can vary by model, license, feature maturity, and maintenance release, so record versions and validate against the matching documentation.

> **About related items:** A `Related item:` callout adds architecture, operations, security, or lifecycle context that helps in real deployments. It is not claimed as a verbatim exam objective.

## Blueprint map

| Domain | Published range | Evidence of readiness |
|---|---:|---|
| System configuration and SD-WAN setup | 20–30% | Explain Security Fabric, HA/FGSP, VDOM/VLAN, and SD-WAN behavior with failure evidence |
| Central management | 15–25% | Deploy repeatable branches and overlays through governed FortiManager templates and ZTP |
| Security profiles | 5–15% | Select SSL/SSH inspection and layered profiles with performance and exception evidence |
| Rules and routing | 25–35% | Derive OSPF/BGP and SD-WAN forwarding from configuration and live state |
| Advanced IPsec | 25–35% | Design and troubleshoot IKEv2, dual-hub, multiregion, ADVPN, and large overlays |

## 1. System configuration and SD-WAN setup (20–30%)

### Build a trustworthy Security Fabric

Distinguish Fabric connectors, which join supported Fortinet products and share topology or security context, from external connectors that import dynamic cloud, identity, address, or threat information. For every connector, document authentication, scope, refresh interval, unavailable-source behavior, certificate trust, least privilege, logging, and stale-data removal. A green connector does not prove that the imported object is current or used by the intended policy.

Automation stitches connect a trigger to one or more actions. Trace the event producer, filters, execution identity, target, timeout, rate control, audit record, and rollback. Quarantine based on an IoC can reduce exposure quickly, but false positives and feedback loops can isolate critical systems. Test alert-only and simulation paths before automated containment.

SAML SSO in the Fabric depends on IdP metadata, certificates, entity identifiers, time, group/role mapping, and a recovery administrator. FortiNAC dynamic addressing and FortiNDR integration add confidence signals, but their freshness and failure modes remain part of the policy decision.

> **Related item: automation safety.** Treat response automation like production code: peer review, scoped credentials, idempotence, rate limits, canary rollout, observability, and a tested disable path.

### Select HA mechanisms from the failure model

FGCP clusters synchronize configuration and selected session state and can operate active-passive or active-active. Virtual clustering can distribute VDOM primaries. Validate heartbeat isolation, monitored interfaces, election priorities, override behavior, virtual MAC movement, session pickup, capacity during member loss, management access, and upgrade sequence.

FGSP synchronizes sessions between independent FortiGates without making them one configuration cluster. Know what session types and state are synchronized, what remains external, and how symmetric or intentionally asymmetric forwarding is achieved. IPsec-protected synchronization protects state in transit but adds key and path dependencies. VRRP supplies gateway redundancy, not FortiGate configuration or complete session synchronization.

### Segment with VLANs and VDOMs

VLANs create Layer 2 broadcast separation; VDOMs create administrative and routing/security domains. A virtual switch changes how member interfaces participate in switching. Inter-VDOM links and routes are explicit dependencies: derive source/destination VDOM, route tables, policies, NAT, resource allocation, logging, and management ownership.

Avoid treating segmentation names as controls. Prove isolation with denied traffic, management-plane tests, logging, and failure cases. Capacity, NP offload, session ownership, and asymmetric traffic can change under virtual clustering or multi-VDOM designs.

### Establish the SD-WAN substrate

An enterprise SD-WAN needs member links, zones, routes, performance SLAs, rules, overlays, logging, and an operational ownership model. Direct internet access changes inspection and egress assumptions at branches. Define which traffic may break out locally, which must use a hub or SASE service, how DNS and SaaS paths behave, and what happens when security services or telemetry are unavailable.

Member “up” is not application health. Use probes meaningful to the service, multiple targets where needed, realistic latency/jitter/loss thresholds, hysteresis, and a deliberate failback policy. Correlate widgets with SLA logs, route/session state, packet capture, and the application experience.

## 2. Central management (15–25%)

### Deploy branches reproducibly

Zero-touch provisioning is a chain of identity, entitlement, reachability, trust, serial/device assignment, blueprint/template selection, variables, install, validation, and acceptance. A CSV import or device blueprint is not merely inventory: incorrect metadata can deploy the wrong addressing, role, region, overlay, or policy at scale.

Define mandatory variables, formats, uniqueness constraints, secret handling, preflight validation, canary sites, and failed-bootstrap recovery. Preserve local emergency access without allowing unmanaged drift. A deployed device is not complete until management, time, DNS, routes, tunnels, policy, logging, and monitoring are verified.

### Govern FortiManager templates and overlay orchestration

Separate policy packages from device/system templates and understand template-group precedence. Metadata variables make a common design reusable, but unresolved or incorrectly scoped values can multiply error. Compare desired database state, installed configuration, device runtime state, and out-of-band changes before forcing synchronization.

For overlay orchestration, map hubs, spokes, regions, underlay links, IPsec templates, tunnel addressing, BGP design, route reflection, SD-WAN zones/rules, and FortiAnalyzer evidence. Plan migration from an existing topology in stages; avoid an all-at-once change that removes the management or return path.

> **Related item: configuration supply chain.** Control who may change templates, variables, scripts, and imports. Version them, review diffs, test in a representative lab, canary, and retain a known-good install and rollback plan.

## 3. Security profiles (5–15%)

### Make TLS inspection an architecture decision

Certificate inspection uses handshake and certificate metadata; full inspection decrypts authorized traffic and re-encrypts it. Protecting outbound clients differs from protecting inbound servers. Full inspection requires a controlled CA lifecycle, endpoint trust deployment, cipher/protocol compatibility, privacy and legal review, resource sizing, bypass governance, and monitoring.

Use SNI checks and certificate validation carefully. Diagnose wrong names, incomplete/untrusted chains, expired certificates, pinning, mutual TLS, QUIC, unsupported ciphers, and time before adding an exception. HTTP/HTTPS code injection features need compatible inspection and must be tested for application impact.

### Combine profiles without losing the packet story

Web filtering, application control, IPS, and ISDB contribute different signals. Derive policy match, inspection mode, SSL visibility, selected profile, signature/category/database state, action, log, and performance. Scope IPS to protected technology and validate CVE-pattern behavior; an indiscriminate sensor can increase CPU use and false positives.

> **Related item: exception debt.** Every bypass needs owner, reason, affected data, compensating controls, expiry, monitoring, and retest. A permanent “temporary” decryption or IPS exception is an unmanaged attack path.

## 4. Rules and routing (25–35%)

### Control OSPF and BGP policy

For OSPF, explain adjacency prerequisites, area/type, network/interface activation, authentication, costs, DR behavior, ECMP, LSDB-to-route installation, filtering, and redistribution. OSPF over IPsec adds tunnel reachability, selectors/interfaces, MTU, and failure detection. Prove both adjacency and installed/usable routes.

For BGP, distinguish eBGP/iBGP, next hop, path attributes, best-path selection, multipath, loop prevention, neighbor groups, loopback sourcing, route reflectors, BFD, graceful restart, and convergence tradeoffs. Apply prefix lists, access lists, and route maps at the correct direction and stage. Redistribution needs explicit tagging/filtering to prevent loops and route leaks.

### Derive SD-WAN decisions

SD-WAN rule lookup and route lookup work together; neither replaces the other. Identify rule order, source/destination/application/Internet-service criteria, strategy, eligible members, SLA state, priority, selected route, and session. Local-out traffic has its own origin and selection considerations. Application steering may have a learning phase before classification stabilizes.

Static routes for zones, member routes, probe routes, policy routes, and dynamic routes can coexist. Trace a packet using current runtime state. Existing SNAT sessions can retain path state until reevaluation triggers; a routing change does not guarantee immediate movement.

> **Related item: convergence budget.** Define how quickly routing, SLA detection, tunnel recovery, policy, and applications must converge. Faster timers can increase instability or control-plane load; measure rather than assume.

## 5. Advanced IPsec (25–35%)

### Engineer reliable IKEv2 tunnels

Trace peer identity, authentication, IKE proposals, child-SA proposals/selectors, DPD, NAT traversal, lifetimes, rekey, PFS, routes, policies, MTU/MSS, fragmentation, offload, logs, and return path. IPsec interfaces without addresses and outbound NAT require deliberate design. OpenSSL can help inspect certificates and keys, but do not expose private material in evidence.

IPsec aggregates can provide redundancy or distribution only when member state, routing, session behavior, and peer design support it. Verify NPU flags and offload rather than assuming acceleration. FEC trades bandwidth and processing for loss recovery; test the application benefit.

### Scale dual-hub and multiregion overlays

Large overlays require an address/ASN/VRF plan, route-policy controls, hub capacity, route-reflection behavior, region preference, failure detection, self-healing, management scale, certificate/secret lifecycle, and observability. BGP per overlay and BGP on loopback have different session and reachability dependencies. MSSP designs add tenant isolation and delegated operations.

ADVPN creates on-demand shortcuts between spokes. Explain shortcut negotiation, route control, spoke/hub roles, timeout, delayed failback, dependent shortcuts, and how ADVPN 2.0 placeholders change orchestration. A shortcut that forms but has wrong routing, policy, MTU, or return path is not a working application path.

> **Related item: blast-radius testing.** Test spoke loss, one hub loss, one region loss, management loss, route leak, stale SLA, certificate expiry, and rollback. A dual-hub diagram is not proof of resilience.

## Integrated scenarios

### Global branch rollout

Design 300 branches across three regions. Specify blueprints, metadata, underlays, dual hubs, IPsec/ADVPN, BGP policy, SD-WAN rules/SLAs, DIA security, log routing, canary sequence, capacity, and rollback. Explain behavior for failed ZTP, bad variable, hub loss, brownout, route leak, and FortiManager outage.

### Asymmetric data-center service

Traffic may enter through one FortiGate and return through another. Compare FGCP, FGSP, VRRP, routing changes, session synchronization, inspection constraints, and external load-balancer behavior. Select a supported design and prove allowed, denied, member-failure, and stateful application cases.

### Encrypted SaaS degradation

Users report intermittent SaaS failures after full inspection and a routing change. Correlate certificate/SNI events, application learning, SD-WAN rule and SLA, route/session tables, SNAT, packet capture, IPS/web logs, and resource usage. Change one hypothesis at a time and preserve a safe rollback.

## Hands-on labs

Use only owned or explicitly authorized nonproduction systems. Sanitize captures and never store production secrets.

1. Build FGCP and compare a documented FGSP design; test member, heartbeat, monitored-link, and return-path failures.
2. Create VDOM/VLAN segmentation and an inter-VDOM service; prove default denial, intended flow, management isolation, and logs.
3. Build a Security Fabric automation stitch in alert-only mode, then a reversible quarantine action with rate controls.
4. Provision two branches through FortiManager variables/templates; inject an invalid value and document recovery.
5. Build OSPF and BGP routes with filtering/redistribution; create and remove a controlled route leak.
6. Configure two SD-WAN links, meaningful SLAs, application steering, local-out behavior, and controlled failback.
7. Deploy dual-hub IKEv2 overlays with BGP, then test MTU, proposal, route, hub, and region faults.
8. Add ADVPN shortcuts; prove shortcut creation, route use, timeout, failback, and behavior when a dependent shortcut fails.
9. Apply full inspection plus web/application/IPS controls to synthetic traffic; diagnose one trust and one false-positive case.
10. Perform a capstone from blank state and produce design, change, evidence, capacity, failure, rollback, and residual-risk records.

## Readiness checks and answers

These are original study prompts, not Fortinet exam questions.

| # | Check | Concise answer |
|---:|---|---|
| 1 | Fabric connector versus external connector? | Fabric connectors integrate supported Fabric members/context; external connectors import outside dynamic data. Both need trust, scope, freshness, and failure handling. |
| 2 | Why can automated quarantine be dangerous? | A false or looping trigger can isolate critical systems at machine speed; scope, simulation, approvals, rate limits, and rollback bound risk. |
| 3 | What does FGCP provide that VRRP does not? | Cluster configuration/election and supported session synchronization; VRRP primarily supplies redundant gateway ownership. |
| 4 | What is FGSP's central tradeoff? | It shares supported session state between independent devices but does not make them one synchronized configuration cluster. |
| 5 | Why encrypt FGSP synchronization? | Session state can be sensitive; IPsec protects it in transit but adds tunnel/key/path dependencies. |
| 6 | VLAN versus VDOM? | VLAN is Layer 2 segmentation; VDOM is a separate administrative/routing/security domain. |
| 7 | What proves inter-VDOM isolation? | Explicit links/routes/policies, denied tests, management tests, and logs—not names or diagrams. |
| 8 | What makes an SLA probe meaningful? | It measures a relevant destination/path with thresholds and timing aligned to application experience. |
| 9 | Why is interface-up insufficient? | A carrier can stay up while loss, latency, DNS, routing, or the application is unusable. |
| 10 | What must a ZTP design validate? | Device identity, entitlement, reachability, template/variables, install, management, routes/tunnels, policy, logging, and recovery. |
| 11 | Why are metadata variables risky? | One wrong or unresolved value can create widespread addressing, role, routing, or policy errors. |
| 12 | Policy package versus system template? | Policy packages govern policy objects/rules; system templates govern device/platform settings, with scoped precedence. |
| 13 | Database state versus runtime state? | Manager intent/install state can differ from the device's live routes, sessions, health, and out-of-band changes. |
| 14 | Certificate versus full inspection? | Certificate inspection reads handshake metadata; full inspection decrypts authorized content and requires managed trust and governance. |
| 15 | First response to a TLS false positive? | Identify the exact trust/protocol/pinning/mTLS/SNI failure and affected policy before granting a narrow, expiring exception. |
| 16 | Why combine multiple security profiles? | They detect different signals; verify prerequisites, actions, logs, resource cost, and overlap. |
| 17 | What makes an OSPF neighbor useful? | Correct LSDB and route installation plus usable forwarding and return path—not adjacency alone. |
| 18 | Why tag redistribution? | To control re-entry and prevent route feedback loops or unintended propagation. |
| 19 | BFD versus graceful restart? | BFD detects path failure quickly; graceful restart preserves forwarding during a controlled control-plane restart. Their risks differ. |
| 20 | Why source BGP from loopbacks? | It decouples peering identity from one physical link, but requires reachable loopbacks and correct multihop/update-source design. |
| 21 | Does an SD-WAN rule replace routing? | No. A rule selects among eligible members; routes still establish reachability and participate in forwarding. |
| 22 | What affects preferred-member election? | Rule match/strategy, member/SLA eligibility, priority, route availability, application state, and session state. |
| 23 | Why might a route change not move traffic? | Existing sessions, especially SNAT state, can remain pinned until reevaluation or expiry. |
| 24 | Main IKEv2 troubleshooting split? | Separate IKE/authentication failure, child-SA/selectors failure, and established-tunnel data-plane failure. |
| 25 | MTU versus MSS? | MTU limits packet size on a path; TCP MSS advertises payload size to reduce fragmentation after tunnel overhead. |
| 26 | What does an NPU flag prove? | Runtime hardware-offload state for the session; configuration alone does not prove offload. |
| 27 | Why use FEC selectively? | It adds repair traffic/processing; only measured loss-sensitive application improvement justifies the cost. |
| 28 | BGP per overlay versus on loopback? | Per-overlay peers bind routing to tunnels; loopback peers can abstract transport but need recursive reachability and policy discipline. |
| 29 | What is ADVPN's value? | It creates on-demand spoke shortcuts to reduce hub tromboning while keeping hub-assisted discovery/control. |
| 30 | What can break an established shortcut? | Wrong route/policy/return path, MTU, SLA, selectors, timing, or dependent-shortcut behavior. |
| 31 | What is a convergence budget? | A measurable maximum for detection, route/tunnel/policy recovery, and usable application restoration. |
| 32 | What should a multiregion test include? | Hub/region/path/manager loss, route leaks, stale health, capacity, session effects, failback, and rollback. |
| 33 | Is passing this exam enough for the credential? | No; active NSE 4 and same-track NSE 5 or 6 requirements must also be met within the published timing rule. |
| 34 | What is the current exam baseline? | 40–50 questions, 75 minutes, English and Japanese; FortiGate/FortiManager/FortiAnalyzer 7.6. |
| 35 | How long is the credential active? | Two years from the NSE 7 exam or last prerequisite exam, whichever qualifying date is later. |
| 36 | What sources are forbidden? | Leaked, recalled, braindump, guaranteed-match, or other unauthorized exam content. |

## Final preparation

- Recheck the certification and exam pages for versions, domain ranges, delivery, languages, prerequisites, retake, renewal, and any successor.
- Rebuild one branch and one dual-hub overlay from blank state; diagnose failures using runtime evidence rather than GUI color.
- Practice short architecture answers that state requirements, dependencies, decision, failure behavior, evidence, and rollback.
- Review old FCSS or version-specific material only after mapping it to the current NSE 7 contract and 7.6 behavior.

## Key terms and phrases

**System configuration and SD-WAN setup (20–30%)**

| Term or phrase | Meaning |
|---|---|
| [Fabric connector](#build-a-trustworthy-security-fabric) | An integration through which supported Security Fabric components exchange topology or security context. |
| [Automation stitch](#build-a-trustworthy-security-fabric) | A FortiOS trigger linked to one or more actions, allowing a detected condition to initiate a defined response. |
| [External connector](#build-a-trustworthy-security-fabric) | A configured source of external context such as cloud inventory or a threat feed. Stale or failed updates can leave policy inputs inaccurate. |
| [Fortinet Security Fabric](#build-a-trustworthy-security-fabric) | Fortinet’s framework for integrating products so they can exchange context and coordinate visibility or policy-driven actions. |
| [Least privilege](#build-a-trustworthy-security-fabric) | Giving an identity only the permissions needed for its task, for as long as it needs them. |
| [Session synchronization](#select-ha-mechanisms-from-the-failure-model) | Sharing selected connection state with a peer so that it can continue eligible sessions after a failure. |
| [Active-passive](#select-ha-mechanisms-from-the-failure-model) | An HA arrangement in which a standby peer is available to take over service from the active peer. |
| [Asymmetric routing](#select-ha-mechanisms-from-the-failure-model) | A flow whose forward and return packets take different paths. Stateful inspection can fail if one direction misses the device holding the session. |
| [High availability (HA)](#select-ha-mechanisms-from-the-failure-model) | A deployment that lets a peer take over when a device fails. The peer still needs working network paths and a valid configuration. |
| [Session pickup](#select-ha-mechanisms-from-the-failure-model) | The transfer or reuse of supported connection state so that eligible sessions can continue across HA failover. |
| [FortiGate Clustering Protocol (FGCP)](#select-ha-mechanisms-from-the-failure-model) | The FortiGate mechanism for coordinating members of an HA cluster, including configuration synchronization and supported session handling. |
| [FortiGate Session Life Support Protocol (FGSP)](#select-ha-mechanisms-from-the-failure-model) | A mechanism for synchronizing supported session information between FortiGate peers in designs that handle traffic distribution separately. |
| [Virtual domain (VDOM)](#segment-with-vlans-and-vdoms) | A logical firewall instance that separates routing, policy and administration within a FortiGate. |
| [Layer 2](#segment-with-vlans-and-vdoms) | The data-link layer, where local delivery uses frames and link-layer addressing, such as Ethernet switching within a VLAN. |
| [Management plane](#segment-with-vlans-and-vdoms) | The interface and services through which administrators configure and monitor devices. Reachability here does not prove that user traffic is working. |
| [Virtual LAN (VLAN)](#segment-with-vlans-and-vdoms) | A logical Layer 2 network with its own broadcast scope. Communication with another VLAN ordinarily requires routing and a suitable policy. |
| [Direct internet access (DIA)](#establish-the-sd-wan-substrate) | An arrangement in which branch internet traffic exits locally instead of traveling through a central site first. |
| [Performance SLA](#establish-the-sd-wan-substrate) | A Fortinet SD-WAN health measurement that compares eligible links against targets such as delay, jitter or loss for steering decisions. |
| [SD-WAN member](#establish-the-sd-wan-substrate) | An interface or connection eligible for SD-WAN forwarding under its zone, route and steering policies. |
| [Software-defined WAN (SD-WAN)](#establish-the-sd-wan-substrate) | A way to steer traffic among network connections according to policy and measured link conditions. |

**Central management (15–25%)**

| Term or phrase | Meaning |
|---|---|
| [Underlay](#govern-fortimanager-templates-and-overlay-orchestration) | The network that provides basic connectivity between sites. An overlay tunnel still depends on that path. |
| [Metadata variable](#govern-fortimanager-templates-and-overlay-orchestration) | A site- or device-specific value substituted into a shared template, such as a branch interface address. |
| [FortiAnalyzer](#govern-fortimanager-templates-and-overlay-orchestration) | A platform for collecting and analyzing supported Fortinet telemetry, including searching logs, generating reports and handling security events. |
| [FortiManager](#govern-fortimanager-templates-and-overlay-orchestration) | A platform for centrally managing Fortinet device configurations and policy. A change staged in its database must reach the intended devices to affect traffic. |
| [Overlay](#govern-fortimanager-templates-and-overlay-orchestration) | A logical network formed over underlying links, commonly using tunnels between branches and hubs. |
| [Policy package](#govern-fortimanager-templates-and-overlay-orchestration) | A managed set of firewall policy rules and associated objects assigned to installation targets. Editing and installing are separate operations. |

**Security profiles (5–15%)**

| Term or phrase | Meaning |
|---|---|
| [Certificate authority (CA)](#make-tls-inspection-an-architecture-decision) | A trusted issuer that signs certificates linking subjects to public keys under a stated policy. |
| [Certificate inspection](#make-tls-inspection-an-architecture-decision) | Examining available TLS negotiation and certificate information without decrypting the application payload. |
| [Mutual TLS (mTLS)](#make-tls-inspection-an-architecture-decision) | TLS in which both peers present certificates and verify one another. Successful authentication still leaves authorization to policy. |
| [Application control](#combine-profiles-without-losing-the-packet-story) | A control that identifies the application using a connection and applies policy to it, even when several applications share a port. |
| [Packet](#combine-profiles-without-losing-the-packet-story) | A network-layer unit carrying a source and destination IP address. Routers use the destination and their forwarding tables to send it onward. |
| [Web filtering](#combine-profiles-without-losing-the-packet-story) | A control that allows or blocks web access according to a URL, category or other policy criterion. |

**Rules and routing (25–35%)**

| Term or phrase | Meaning |
|---|---|
| [Route redistribution](#control-ospf-and-bgp-policy) | Importing routes learned through one routing source into another. Filtering and route attributes control what is propagated. |
| [Border Gateway Protocol (BGP)](#control-ospf-and-bgp-policy) | A routing protocol that exchanges reachability between peers and uses policy and path attributes to select routes. |
| [Next hop](#control-ospf-and-bgp-policy) | The adjacent router or forwarding destination selected for the next stage of a packet’s path. |
| [Open Shortest Path First (OSPF)](#control-ospf-and-bgp-policy) | A link-state routing protocol in which routers exchange topology information and calculate paths using link costs. |
| [Equal-cost multipath (ECMP)](#control-ospf-and-bgp-policy) | Forwarding over multiple eligible paths with equal route preference and cost. The way traffic is distributed depends on the implementation. |
| [Application steering](#derive-sd-wan-decisions) | Selection of a WAN path using traffic classification, policy and the measured condition of eligible links. |
| [SD-WAN rule](#derive-sd-wan-decisions) | A policy that identifies a class of traffic and chooses among eligible links using its configured strategy. |
| [Source NAT (SNAT)](#derive-sd-wan-decisions) | Rewriting the source address of a packet, commonly so internal hosts can use a shared external address. |
| [Static route](#derive-sd-wan-decisions) | A route installed by configuration, specifying a prefix and next hop or interface. It changes only through configuration or an associated tracking mechanism. |

**Advanced IPsec (25–35%)**

| Term or phrase | Meaning |
|---|---|
| [Internet Key Exchange (IKE)](#engineer-reliable-ikev2-tunnels) | The protocol peers use to authenticate and negotiate the keys and settings for IPsec protection. |
| [Bandwidth](#engineer-reliable-ikev2-tunnels) | The nominal data-carrying capacity of a link, usually expressed in bits per second. It does not by itself establish delay or delivered throughput. |
| [Internet Protocol Security (IPsec)](#engineer-reliable-ikev2-tunnels) | A set of IP-layer protocols that protect traffic between negotiated peers, with defined security associations and traffic selectors. |
| [Security association lifetime](#engineer-reliable-ikev2-tunnels) | The interval after which protected traffic needs newly negotiated security association parameters or keys. Peer compatibility matters at renewal. |
| [Route reflection](#scale-dual-hub-and-multiregion-overlays) | A BGP mechanism that lets a designated router distribute routes among internal peers without a full mesh of peer sessions. |
| [Auto Discovery VPN (ADVPN)](#scale-dual-hub-and-multiregion-overlays) | A Fortinet overlay design that supports on-demand shortcut tunnels between eligible spokes, subject to routing and security association state. |
| [Observability](#scale-dual-hub-and-multiregion-overlays) | The ability to infer a system’s internal condition from its outputs, often by relating logs, metrics and traces to a particular request or failure. |
| [Tenant isolation](#scale-dual-hub-and-multiregion-overlays) | Separation of each customer’s identities, records, policies and actions so that one customer cannot access or affect another. |

**Worked examples and practice**

| Term or phrase | Meaning |
|---|---|
| [Load balancer](#asymmetric-data-center-service) | A component that sends eligible requests or connections to selected backends using health and distribution policy. |
| [Software as a service (SaaS)](#encrypted-saas-degradation) | An application operated by a provider and consumed as a service. The customer still governs tenant settings, access and use of its data. |

## Places to learn

This is not a complete list, and it is not a prescription to consume everything. Start with the official exam contract and choose only the documentation, course sections, and labs that close measured gaps. Times are publisher-listed where visible or clearly labeled estimates and can change.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Secure Networking Architect exam](https://training.fortinet.com/local/staticpage/view.php?page=secure_networking_architect_exam) | Public | 45–75 min | Current contract, exact tasks/ranges, versions, experience, and approved sample-question boundary |
| [NSE 7 Secure Networking certification](https://training.fortinet.com/local/staticpage/view.php?page=nse_7_secure_networking) | Public | 20–30 min | Prerequisite, timing, validity, renewal, and exam relationship |
| [Fortinet Training Institute library](https://training.fortinet.com/local/library/) | Free account; labs/ILT may cost | 20–40 min selection; courses vary | Find the current Enterprise Firewall, SD-WAN, FortiOS, FortiManager, and FortiAnalyzer courses named by the exam page |
| [SD-WAN Enterprise Administrator course outline](https://training.fortinet.com/local/staticpage/view.php?page=library_sd-wan-enterprise-administrator) | Account/enrollment; labs may cost | 6 hr lecture + 7 hr estimated labs | SD-WAN architecture and operations within the comprehensive exam; course outline only, not verified lesson coverage |
| [FortiOS 7.6 documentation](https://docs.fortinet.com/product/fortigate/7.6) | Public | 20–35 hr selected chapters/labs | HA, VDOM, Security Fabric, routing, SD-WAN, profiles, sessions, and IPsec authority |
| [FortiManager 7.6 documentation](https://docs.fortinet.com/product/fortimanager/7.6) | Public | 12–20 hr selected chapters/labs | ZTP, policy packages, templates, variables, VPN Manager, orchestration, install and troubleshooting |
| [FortiAnalyzer 7.6 documentation](https://docs.fortinet.com/product/fortianalyzer/7.6) | Public | 6–12 hr selected chapters/labs | SD-WAN/security logs, analytics, reports, event handling, and operational evidence |
| [Fortinet Training Institute policies](https://helpdesk.training.fortinet.com/support/solutions/73000238852) | Public | 30–60 min | Current delivery, retake, results, voucher, integrity, and renewal policy |
| [Fortinet YouTube](https://www.youtube.com/@Fortinet) | Free/YouTube | 3–8 hr selected current videos | Visual architecture and product demonstrations; reconcile version-sensitive steps with 7.6 docs |

