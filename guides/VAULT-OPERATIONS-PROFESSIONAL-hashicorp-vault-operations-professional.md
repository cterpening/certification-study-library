---
exam_code: VAULT-OPERATIONS-PROFESSIONAL
vendor_id: hashicorp
official_blueprint: https://developer.hashicorp.com/vault/tutorials/ops-pro-cert/ops-pro-review
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# HashiCorp Certified: Vault Operations Professional Study Guide

> **Independent AI-assisted resource — SOURCE-VALIDATED.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [source-validation record](../docs/SOURCE-VALIDATION.md). The [official Vault Operations Professional content list](https://developer.hashicorp.com/vault/tutorials/ops-pro-cert/ops-pro-review) is authoritative.

**Current baseline:** Vault Operations Professional objectives; verified August 31, 2026<br>
**Upcoming blueprint change:** No future update or retirement announcement was found in the official certification material as of August 31, 2026.<br>
**Official source:** [Vault Operations Professional exam content list](https://developer.hashicorp.com/vault/tutorials/ops-pro-cert/ops-pro-review)

HashiCorp does not display a short exam code for this credential. This library uses `VAULT-OPERATIONS-PROFESSIONAL` as a stable internal identifier.

## How to use this guide

This is a lab-based operations credential. The [official orientation](https://developer.hashicorp.com/vault/tutorials/ops-pro-cert/ops-pro-overview) expects Vault Associate knowledge, Linux and networking skill, PKI/TLS/PGP familiarity, container operations, and production Vault experience. The environment uses a Vault Enterprise binary and includes hands-on, hybrid, and multiple-choice tasks.

Study as an operator:

```text
requirement
   ↓
configure server + storage + seal + TLS
   ↓
initialize and establish controlled administration
   ↓
enable auth/engines/policies for clients
   ↓
monitor telemetry + audit + operational logs
   ↓
test HA, backup, replication, recovery, and scaling
   ↓
verify client delivery and access evidence
```

Choose a route:

- **Environment builder:** Work Domains 1–4 in order and repeat cluster builds from clean machines.
- **Security operator:** Focus on hardening, secure introduction, Kubernetes, HSM/seal wrap, policies, Sentinel, control groups, and namespaces.
- **Platform operator:** Focus on Integrated Storage, telemetry/audit/logging, HA, snapshots, replication, promotion, performance standbys, and path filters.
- **Exam rehearsal:** Complete timed Linux-terminal scenarios without personal aliases or external search. Verify health, state, configuration, and API behavior after every change.

The [Vault Associate (003) guide](VAULT-ASSOCIATE-003-hashicorp-vault-associate.md) repairs prerequisite gaps but does not replace production operating practice.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

HashiCorp publishes eight domains without percentage weights.

| Published domain | Weight | Guide coverage |
|---|---:|---|
| 1. Create a working Vault server configuration given a scenario | Not published | Engines, hardening, auto unseal, Raft, auth, initialization, root regeneration, rekey, and rotation |
| 2. Monitor a Vault environment | Not published | Telemetry, audit-device records, operational logs, and diagnostic workflow |
| 3. Employ the Vault security model | Not published | Secure client introduction and Kubernetes security boundaries |
| 4. Build fault-tolerant Vault environments | Not published | HA, snapshots, DR replication, failover, promotion, and recovery evidence |
| 5. Understand HSM integration | Not published | HSM auto unseal, key custody, PKCS#11 seal wrap, and failure dependencies |
| 6. Scale Vault for performance | Not published | Batch tokens, performance standbys, performance replication, and path filters |
| 7. Configure access control | Not published | Identity, ACL policies, Sentinel, control groups, and namespaces |
| 8. Configure Vault Agent | Not published | Auto-auth, token sinks, templates, renewal, and client-host security |

## Exam operating method

HashiCorp states that scenario labs are independent. Treat each as its own environment: inspect addresses, processes, configuration, environment variables, cluster membership, seal state, enabled mounts, and policies instead of carrying assumptions from another lab.

For each task:

1. Translate wording into an observable final state.
2. Inspect before editing.
3. Back up the relevant file or data when appropriate.
4. Make the smallest supported change.
5. Validate syntax and restart/reload implications.
6. Check command exit status and API response.
7. Verify from Vault's perspective and the client/system perspective.
8. Remove temporary tokens, files, and debug settings.

> **Related item:** A working CLI command can still produce an operationally unsafe cluster. Professional verification includes TLS, file permissions, process ownership, cluster membership, seal state, replication state, logs, and least-privilege access.

## 1. Create a working Vault server configuration

### Build the server from explicit boundaries

A production server configuration should make these decisions visible:

- listener addresses, TLS certificates/keys, and client/proxy expectations;
- `api_addr` used by clients and redirects;
- `cluster_addr` used for node-to-node communication;
- storage stanza and node identity;
- seal stanza and external key dependency;
- UI and telemetry settings where required;
- log level/format and operational integration;
- environment-specific paths and permissions.

Start from the [Vault configuration reference](https://developer.hashicorp.com/vault/docs/configuration), not a copied development example. Keep private keys and credentials out of the configuration file when a safer supported injection method exists.

### Enable auth methods and secrets engines deliberately

Mounting a plugin creates an API path and accessor. Select paths that express ownership, tune TTLs to the use case, and configure roles/policies before onboarding clients. Do not confuse enabling an engine with configuring its backend or proving that lease revocation works.

Operational validation includes:

```bash
vault status
vault secrets list -detailed
vault auth list -detailed
vault read sys/health
```

Use nonroot test tokens for positive and negative path checks.

### Production hardening

HashiCorp's [production hardening guidance](https://developer.hashicorp.com/vault/docs/concepts/production-hardening) spans operating system, memory, process, network, TLS, storage, audit, and administrative practice. Build a threat-driven checklist rather than treating hardening as one setting.

High-value controls include:

- dedicated nonroot process identity and restrictive file permissions;
- TLS for client and cluster traffic with verified names and trust chains;
- network exposure limited to required clients, peers, storage, seal, and monitoring systems;
- memory/swap/core-dump controls appropriate to the platform;
- protected audit devices with monitored delivery failures;
- minimal root-token use and controlled recovery procedures;
- timely, tested upgrades and backups;
- no secrets in arguments, history, world-readable files, or routine logs.

### Integrated Storage and HA

Integrated Storage uses Raft consensus. Configure each node with a unique `node_id`, shared cluster intent, and correct addresses, then join peers through supported retry/join methods. Quorum determines write availability. The [Raft storage reference](https://developer.hashicorp.com/vault/docs/configuration/storage/raft) covers current configuration and operational details.

Keep three concepts separate:

| Concept | Purpose |
|---|---|
| Integrated Storage | Persist Vault data and coordinate a Raft cluster |
| HA active/standby | One active node handles writes while standbys provide failover |
| Snapshot | Point-in-time backup artifact for recovery |

A healthy process is not proof of a healthy peer set. Check `vault operator raft list-peers`, health endpoints, leader state, and storage/log evidence.

### Initialization, unseal, rekey, and rotate

Initialization creates the barrier key material and initial root token; it is performed once per new storage cluster. Store shares/recovery keys and root token through approved custody processes, then revoke the initial root token after bootstrap.

Know the difference:

| Operation | Changes |
|---|---|
| Unseal | Makes the existing barrier key available so Vault can decrypt storage |
| Rekey | Changes Shamir unseal or recovery key shares/threshold |
| Rotate | Rotates the encryption key used by the barrier for new writes |
| Generate root | Creates a new root token through an authorized quorum workflow |

The [`operator generate-root`](https://developer.hashicorp.com/vault/docs/commands/operator/generate-root) workflow uses an OTP or PGP key and key-share/recovery authorization so no single operator should casually obtain a plaintext root token. Plan generation, custody, immediate use, audit, and revocation as one break-glass procedure.

### Auto unseal

Auto unseal delegates protection of the barrier key to a supported KMS/HSM/seal integration. It enables automatic restarts but creates an external service, network, credential, key, and policy dependency. Recovery keys support selected recovery operations; they do not manually unseal a cluster in the same way as Shamir shares.

**VERIFY CURRENT:** supported seal mechanisms, migration procedures, multi-seal behavior, and edition requirements change. Test seal migration and provider outages in an isolated environment before production use.

## 2. Monitor a Vault environment

### Three evidence streams

| Stream | Answers | Typical consumer |
|---|---|---|
| Telemetry metrics | Is the service healthy, saturated, slow, or approaching a limit? | Metrics platform and alerts |
| Audit-device records | Who requested which Vault operation and what was the result? | Security/SIEM investigation |
| Operational logs | What did the server process, storage, seal, plugin, or network layer report? | Operator diagnostics |

Do not substitute one for another. Audit logs are not performance metrics; operational logs are not a complete record of authenticated API requests.

### Telemetry

The [telemetry reference](https://developer.hashicorp.com/vault/docs/internals/telemetry) documents metric names, labels, sinks, and configuration. Build alerts around user-visible and recovery-relevant signals:

- sealed status and active-node availability;
- request latency, error rate, and saturation;
- Raft peer/quorum, leadership, and storage performance;
- token/lease activity and expiration/revocation pressure;
- audit-device health;
- replication lag/state;
- seal or external dependency errors;
- resource exhaustion and process restarts.

Metric names and editions are **VERIFY CURRENT**. Alert on a failure hypothesis rather than accumulating every metric without response guidance.

### Audit devices

Vault audit devices record API requests and responses with sensitive values generally HMAC-protected rather than stored as plaintext. Enable at least one reliable device and usually more than one independent destination where the risk model requires it. Vault can refuse requests when it cannot write to any enabled audit device, making audit availability part of service availability.

Protect audit logs: HMACs still reveal stable equality relationships and metadata can be sensitive. Restrict access, monitor ingestion, time synchronization, rotation, retention, and tamper evidence.

### Diagnostic sequence

1. Establish incident time, affected clients, and expected operation.
2. Check process and health endpoint.
3. Check seal, leader, peer, replication, and storage state.
4. Correlate request ID across client error, audit record, and operational log.
5. Classify authentication, authorization, path, lease, storage, network, TLS, or capacity failure.
6. Reproduce with the narrowest nonroot request.
7. Capture evidence before restarting or changing log levels.
8. Remove verbose logs and temporary access after resolution.

> **Related item:** Debug logs can contain request details, paths, identifiers, and sometimes sensitive data from integrations. Treat them as incident evidence with controlled access and retention.

## 3. Employ the Vault security model

### Secure client introduction

A new client needs a way to establish trust without already possessing an unconstrained Vault token. The [secure introduction tutorial](https://developer.hashicorp.com/vault/tutorials/app-integration/secure-introduction) frames this bootstrap problem.

Evaluate:

- what external system attests to the workload;
- how Vault verifies issuer, audience, signature, role, namespace, or platform metadata;
- how the first token or wrapped value reaches only the intended client;
- which policies and TTL apply;
- how replay and theft are constrained;
- how the client renews, reauthenticates, and handles denial/outage.

AppRole secret IDs, cloud identity documents, Kubernetes service-account tokens, and response wrapping solve different parts of the introduction problem. None removes the need for policy and lifecycle controls.

### Vault on Kubernetes

The [Kubernetes security considerations](https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-security-concerns) span pod scheduling, persistent storage, TLS, service accounts, network policy, auto-unseal credentials, host access, and secret delivery.

Threat boundaries include:

- Kubernetes administrators who can inspect workloads and Secrets;
- node/root access to process memory and files;
- pod service-account identity and token audiences;
- persistent-volume and snapshot access;
- load balancer and service routing to active/standby nodes;
- init/sidecar/operator copies of secrets;
- Helm values and manifests containing credentials.

Avoid treating a container image as a security boundary. Vault still requires hardened hosts/nodes, TLS, restricted service accounts, durable storage, and tested failure handling.

## 4. Build fault-tolerant Vault environments

### HA is local failover, not disaster recovery

Vault [HA mode](https://developer.hashicorp.com/vault/docs/concepts/ha) allows one active node and standby nodes sharing or replicating storage as supported. Standbys forward or redirect requests and can become active after failure. Client retry, DNS/load-balancer health, TLS identity, and leader election determine actual availability.

Test:

- active-node loss;
- standby promotion;
- peer loss without quorum loss;
- quorum loss and restoration;
- storage latency/failure;
- seal-service outage during restart;
- certificate expiry/rotation;
- snapshot restore in an isolated cluster.

### DR replication

Vault Enterprise DR replication maintains a recovery secondary. The secondary does not normally serve ordinary client traffic until promoted. A promotion requires recovery authorization and coordinated client routing. The [replication documentation](https://developer.hashicorp.com/vault/docs/enterprise/replication) distinguishes DR from performance replication.

A recovery plan must specify:

1. detection and authority to declare disaster;
2. latest confirmed replication state and expected data loss;
3. promotion/failover procedure and recovery credentials;
4. DNS/load-balancer/client configuration changes;
5. seal, TLS, plugin, and external dependency readiness;
6. verification of auth, policies, engines, and issued credentials;
7. failback or new-primary plan;
8. audit evidence and postincident repair.

Snapshots remain necessary for corruption, operator error, and recovery cases not solved by replicating current state.

## 5. Understand HSM integration

Vault Enterprise can integrate with an HSM for seal/key operations. The [HSM documentation](https://developer.hashicorp.com/vault/docs/enterprise/hsm) and [seal-wrap documentation](https://developer.hashicorp.com/vault/docs/enterprise/sealwrap) describe distinct protections.

| Capability | Purpose |
|---|---|
| HSM auto unseal | Protect barrier-unseal key material and automate unseal using HSM/PKCS#11 integration |
| Seal wrap | Add an HSM-backed encryption layer around supported sensitive values before storage |

Design HSM availability, partition/token credentials, slot/key labels, quorum/administration, backup, replacement, latency, and disaster recovery. A highly available Vault cluster can still be unable to restart if every node depends on an unavailable HSM path.

> **Related item:** FIPS validation, HSM certification, seal wrap, and end-to-end system compliance are different claims. Confirm the exact module, configuration, operational procedure, and compliance boundary.

## 6. Scale Vault for performance

### Batch tokens

Batch tokens reduce storage overhead for high-volume, short-lived use but have feature limitations. They cannot be renewed and do not behave like persisted service tokens. Choose them only when client reauthentication and the required engine/features fit their lifecycle.

### Performance standbys

Vault Enterprise [performance standby nodes](https://developer.hashicorp.com/vault/docs/enterprise/performance-standby) can serve eligible read-only traffic while forwarding requests that require the active node. They improve throughput and latency for supported workloads but do not make every endpoint local or eliminate the active node.

### Performance replication and path filters

Performance replication supports active clusters closer to clients. Cluster-local items and eventual propagation behavior matter. Path filters can constrain which secrets replicate to a secondary, supporting data-residency and blast-radius goals but adding configuration and troubleshooting complexity.

Ask:

- Is the required data replicated or cluster-local?
- Which cluster should issue or revoke this lease/token?
- Can the client tolerate replication delay?
- Does a path filter exclude a dependency such as an auth configuration or key?
- How are clients routed during cluster or network failure?

**VERIFY CURRENT:** feature availability, replicated paths, cluster-local behavior, scaling limits, and license requirements.

## 7. Configure access control

### Identity and ACL policies

Entities and groups connect external-auth aliases to a logical identity. ACL policies grant capabilities on API paths. Troubleshooting requires inspecting the auth mount accessor, alias, canonical entity, direct and inherited group membership, attached policies, namespace, token metadata, and exact request path.

Write policy from required API calls and test with `vault token capabilities`. `sudo` authorizes selected root-protected operations; it is not equivalent to a root token.

### Namespaces

Vault Enterprise [namespaces](https://developer.hashicorp.com/vault/docs/enterprise/namespaces) create isolated administrative and API-path scopes within one Vault deployment. Each namespace can contain auth methods, secrets engines, policies, identities, and child namespaces subject to product behavior.

Namespace boundaries do not create separate physical clusters, failure domains, storage systems, or seal dependencies. Choose namespaces for delegated multi-tenancy; choose separate clusters when stronger operational, regulatory, scaling, or failure isolation is required.

### Sentinel and control groups

Sentinel policies add policy-as-code checks beyond ACL path capabilities. Control groups can require additional authorization before a sensitive response is released. The [control-group documentation](https://developer.hashicorp.com/vault/docs/enterprise/control-groups) describes the request/authorization workflow.

| Control | Question |
|---|---|
| ACL policy | May this token perform this path operation? |
| Sentinel | Does broader request/context policy allow it? |
| Control group | Have required approvers authorized this specific request? |
| Namespace | In which delegated administrative scope does evaluation occur? |

Plan failure behavior and emergency access. An approval control without available approvers or a break-glass procedure can become an outage mechanism.

## 8. Configure Vault Agent

Vault Agent can authenticate, renew/manage tokens, proxy/cache requests, and render templates. The [auto-auth documentation](https://developer.hashicorp.com/vault/docs/agent-and-proxy/autoauth) and [template documentation](https://developer.hashicorp.com/vault/docs/agent-and-proxy/agent/template) are the primary references.

### Auto-auth and sinks

An auto-auth configuration has a method and one or more sinks. The method obtains a token using workload identity; a sink writes or delivers it. Secure the method credential, sink destination, file permissions, wrapping behavior, and process users.

### Templates

Templates retrieve data and render files or trigger commands according to configuration. Design:

- destination ownership and mode;
- atomic replacement behavior;
- renewal and re-render timing;
- application reload/restart signal;
- missing/denied secret behavior;
- command execution permissions and injection risk;
- cleanup on shutdown.

```text
workload identity → Agent auto-auth → Vault token
                                      ↓
                                template query
                                      ↓
                         protected rendered file
                                      ↓
                        application reload/consume
```

> **Related item:** Successful template rendering is not proof that the application consumed the new secret. Monitor the complete rotation chain through application reload and successful downstream use.

## Integrated operations playbook

Use this record for every design or incident:

| Dimension | Question |
|---|---|
| Service | Which nodes, leader, peers, storage, seal, and listeners are involved? |
| Identity | Which client, auth mount, entity/group, namespace, and token apply? |
| Authorization | Which ACL/Sentinel/control-group evaluations permit or deny the exact path? |
| Secret lifecycle | Which engine, role, lease, key version, renewal, and revocation path apply? |
| Availability | What happens on active, peer, storage, seal, network, or replication failure? |
| Evidence | Which telemetry, audit record, operational log, snapshot, and change record prove behavior? |
| Recovery | Who can rekey, generate root, promote DR, restore, reroute, and declare completion? |

## Hands-on labs

Use disposable personal environments and trial licensing only under HashiCorp's terms. Never practice destructive operations on an employer, customer, shared, or production Vault cluster without authorization.

### Lab 1: Build a three-node Raft cluster

Create three disposable Linux/container nodes with unique configuration, TLS, Integrated Storage, and retry join. Initialize once, join peers, unseal or use an approved test auto-unseal mechanism, and verify leader/peer health. Fail the active node and observe promotion. Rebuild from clean notes until repeatable.

### Lab 2: Bootstrap and remove root access

Initialize a disposable cluster, enable audit, create operator policies and auth, verify nonroot administration, then revoke the initial root token. Run a generate-root workflow with an OTP in the lab, perform one justified action, capture audit evidence, and immediately revoke the generated root token.

### Lab 3: Monitor one failed request end to end

Create a token missing one capability. Make the denied request and correlate client error, audit record, operational log, and relevant telemetry by time/request ID. Add the narrow capability, repeat, and document why the change is least privilege.

### Lab 4: Snapshot and isolated restore

Write disposable data, create an Integrated Storage snapshot, then restore it only into an isolated recovery cluster following current documentation. Verify seal compatibility, cluster identity, auth mounts, policies, engines, and data. Record RPO/RTO observations and destroy the lab.

### Lab 5: Replication tabletop or trial lab

Design DR and performance replication across two regions. Include enablement tokens, primary/secondary roles, TLS/networking, recovery keys, path filters, client routing, lag monitoring, promotion, failback, and snapshots. If using an Enterprise trial, execute only within its terms and clean up.

### Lab 6: Namespace and control-group design

Create a multi-tenant design for platform, payments, and analytics teams. Define namespace hierarchy, delegated administrators, auth mounts, identity groups, ACLs, Sentinel rules, a control-group approval, audit access, and cluster-level break-glass boundaries. Identify which requirement would force a separate cluster.

### Lab 7: Vault Agent delivery

On a disposable client host, configure auto-auth with a short-lived workload credential, a wrapped/protected file sink, and a template. Verify file permissions, renewal, re-render, application reload, denied-path behavior, Vault outage behavior, and cleanup.

### Lab 8: Timed incident drill

Introduce one failure—bad TLS name, sealed node, lost leader, wrong namespace, expired token, missing policy capability, audit-device failure, or broken Agent template. Give yourself 30 minutes to classify, correlate evidence, repair minimally, and verify recovery without root-token shortcuts.

## Knowledge checks

1. Which server addresses are client-facing and cluster-facing, and why must they be correct?
2. Why does enabling a secrets engine not prove it is production-ready?
3. How do Integrated Storage, HA, and snapshots solve different problems?
4. Contrast unseal, rekey, barrier-key rotation, and root-token generation.
5. What external dependency does auto unseal introduce?
6. Why can audit-device health affect Vault availability?
7. Which question belongs to telemetry, audit logs, and operational logs respectively?
8. How do you correlate a denied client request across evidence sources?
9. What is the secure-introduction problem?
10. Which Kubernetes actors can expose Vault-delivered secrets?
11. Why is HA not disaster recovery?
12. What must be verified after DR promotion beyond “the cluster is unsealed”?
13. How do HSM auto unseal and seal wrap differ?
14. Why can an HSM outage prevent restart of an otherwise healthy cluster?
15. When do batch-token limitations outweigh their scale advantage?
16. What traffic can performance standbys serve locally?
17. How can a replication path filter break an application unexpectedly?
18. Contrast ACL policies, Sentinel, control groups, and namespaces.
19. Why is a namespace not a separate failure domain?
20. What proves a Vault Agent rotation completed end to end?

## High-value distinctions

| Contrast | Remember |
|---|---|
| `api_addr` vs `cluster_addr` | Client/redirect address vs node-to-node address |
| Storage vs seal | Persist encrypted data vs protect barrier-unlock material |
| Unseal vs rekey vs rotate | Open barrier vs change shares vs change encryption key |
| Root generation vs normal auth | Quorum break-glass authority vs routine least-privilege access |
| Telemetry vs audit vs operational logs | Service measures vs API evidence vs process diagnostics |
| Healthy process vs healthy cluster | Running PID vs leader/quorum/storage/seal/client service |
| HA vs snapshot vs DR | Local failover vs point-in-time recovery vs remote promotable replica |
| DR vs performance replication | Recovery standby vs active distributed workload |
| Batch vs service token | Lightweight limited token vs full stored lifecycle |
| Performance standby vs DR secondary | Read-scaling/forwarding node vs disaster-recovery cluster |
| HSM auto unseal vs seal wrap | Unlock-key protection vs extra encryption of selected stored values |
| ACL vs Sentinel vs control group | Path capability vs contextual policy vs request approval |
| Namespace vs cluster | Logical delegated tenant vs separate operational failure boundary |
| Agent sink vs template | Token delivery vs rendered secret/config delivery |

## Readiness checklist

- [ ] I can build and validate a hardened Vault server configuration from a scenario.
- [ ] I can operate Integrated Storage, inspect peers, test HA, snapshot, and restore safely.
- [ ] I can initialize, unseal, rekey, rotate, and regenerate root while explaining custody boundaries.
- [ ] I can enable and configure auth methods and secrets engines without root-token dependence.
- [ ] I can correlate telemetry, audit records, operational logs, health, and client errors.
- [ ] I can design secure workload introduction and explain Kubernetes threats.
- [ ] I can distinguish and test HA, DR replication, performance replication, and path filters.
- [ ] I can explain HSM auto unseal and seal wrap dependencies.
- [ ] I can choose service/batch tokens and performance standbys by workload behavior.
- [ ] I can troubleshoot entities, groups, policies, Sentinel, control groups, and namespaces.
- [ ] I can configure Agent auto-auth, sinks, and templates with safe rotation behavior.
- [ ] I have repeated timed hands-on scenarios in an unfamiliar Linux environment.
- [ ] I checked current Vault/Enterprise behavior and the official blueprint.

## Primary references

- [Official Vault Operations Professional content list](https://developer.hashicorp.com/vault/tutorials/ops-pro-cert/ops-pro-review)
- [Official professional learning path](https://developer.hashicorp.com/vault/tutorials/ops-pro-cert/ops-pro-study)
- [Official exam orientation](https://developer.hashicorp.com/vault/tutorials/ops-pro-cert/ops-pro-overview)
- [Production hardening](https://developer.hashicorp.com/vault/docs/concepts/production-hardening)
- [Integrated Storage configuration](https://developer.hashicorp.com/vault/docs/configuration/storage/raft)
- [Vault telemetry](https://developer.hashicorp.com/vault/docs/internals/telemetry)
- [Vault replication](https://developer.hashicorp.com/vault/docs/enterprise/replication)
- [Vault Agent auto-auth](https://developer.hashicorp.com/vault/docs/agent-and-proxy/autoauth)

## Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the official material and hands-on scenarios that match your gaps. Times are approximate consumption time at normal speed; repeated cluster builds, failure injection, troubleshooting, and prerequisite repair add substantial time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [HashiCorp Vault Operations Professional learning path](https://developer.hashicorp.com/vault/tutorials/ops-pro-cert/ops-pro-study) | Free reading; full Enterprise exercises may require an authorized trial or licensed environment | About 30–50 hours for linked reading and hands-on repetition (library estimate; the page's seven-minute read time excludes linked work) | Authoritative scenario preparation across Raft, auth/engines, replication, Agent, and access control |
| [Professional exam content list](https://developer.hashicorp.com/vault/tutorials/ops-pro-cert/ops-pro-review) | Free | About 3–6 hours for an active documentation pass | Exact objective-to-documentation checklist; use it to select labs rather than passively rereading every link |
| [Professional exam orientation](https://developer.hashicorp.com/vault/tutorials/ops-pro-cert/ops-pro-overview) | Free | About 30–60 minutes including environment and prerequisite notes | First-party description of lab, hybrid, and multiple-choice tasks, Enterprise binary, trial option, and available documentation |
| [Vault Associate (003) guide](VAULT-ASSOCIATE-003-hashicorp-vault-associate.md) | Free | About 8–14 hours for targeted prerequisite repair | Review auth, policy, token, lease, engine, seal, storage, replication, and Agent fundamentals before operating scenarios |
| [HashiCorp Vault operations tutorials](https://developer.hashicorp.com/vault/tutorials) | Free; cloud, Kubernetes, HCP, and Enterprise labs can require accounts or licensing | About 2–6 hours per selected objective gap | Build focused practice for Raft, monitoring, DR/performance replication, HSM, namespaces, policies, and Agent |
| [Vault documentation and API reference](https://developer.hashicorp.com/vault/docs) | Free | About 8–16 hours for an objective-mapped reference pass, plus repeated lookup practice | Primary behavior reference and the style of material available during the exam; use current docs and mark version/edition changes |

No exact current third-party Vault Operations Professional course or commercial practice lab was included without a verifiable public objective mapping and runtime. That is an open catalog gap. A general Vault course can repair product gaps but should not be represented as performance-exam preparation unless it includes repeated cluster operations and failure recovery.
