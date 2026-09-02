---
exam_code: CKS
vendor_id: linux-foundation
official_blueprint: https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-01
---

# CKS Certified Kubernetes Security Specialist Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#cks-coverage-record). The [official CKS page](https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/) is authoritative.

**Current baseline:** Kubernetes v1.35 and the six weighted domains on the live Linux Foundation CKS page: 15% / 15% / 10% / 20% / 20% / 20%<br>
**Source discrepancy:** The [CNCF CKS page](https://www.cncf.io/training/certification/cks/) still shows the earlier 10% / 15% / 15% first-three weights, and the public repository's latest named [CKS curriculum PDF is v1.34](https://github.com/cncf/curriculum/blob/master/CKS_Curriculum%20v1.34.pdf). This guide follows the live Linux Foundation v1.35 page and treats both CNCF artifacts as revalidation signals, not as authority to overwrite it.<br>
**Lifecycle watch:** The exam aligns to a recent Kubernetes minor release about 4–8 weeks after release; verify the live version, weights, competencies and curriculum file immediately before practice and scheduling<br>
**Official delivery snapshot:** Online, remotely proctored, performance-based command-line exam; two hours; certification valid for two years; 12-month eligibility, one retake, and two 36-hour Killer.sh simulator activations with 17 questions per attempt listed<br>
**Required prerequisite:** You must previously have passed CKA. The current Linux Foundation/CNCF wording says the CKA does **not** have to remain active.

## How to use this guide

CKS assumes CKA-level administration. Practice security as a layered, testable control system:

1. identify asset, trust boundary, identity, data, entry point and plausible abuse/failure;
2. collect the current configuration and a reproducible positive/negative test before changing it;
3. apply the narrowest supported preventive, detective or recovery control;
4. validate legitimate function plus the action that should now be denied or detected;
5. preserve evidence, restart/reboot/recreate where persistence matters, and document rollback/residual risk.

Use disposable Kubernetes v1.35 clusters and hosts that you own or are explicitly authorized to test. Keep recovery access before changing API server, kubelet, firewall, kernel policy, admission or audit configuration. Use the [versioned Kubernetes v1.35 documentation](https://v1-35.docs.kubernetes.io/docs/home/) and the official objective page as the scope baseline. Tool names in objectives are examples of capabilities; understand inputs, outputs, false positives, enforcement point and verification rather than memorizing one command. Never reproduce proprietary simulator tasks or recalled exam material.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Weighted objective map

| Domain | Weight | Security evidence |
|---|---:|---|
| 1. Cluster setup | 15% | Network isolation, CIS review, TLS Ingress, metadata/endpoint protection and binary integrity |
| 2. Cluster hardening | 15% | Least-privilege RBAC/ServiceAccounts/API access and security-driven upgrades |
| 3. System hardening | 10% | Minimal hosts, least-privilege IAM/network access, AppArmor and seccomp |
| 4. Minimize microservice vulnerabilities | 20% | Pod Security Standards, Secrets, tenancy/sandbox isolation and Pod-to-Pod encryption |
| 5. Supply chain security | 20% | Minimal images, SBOM/provenance, secured CI/artifacts, signatures/policy and static analysis |
| 6. Monitoring, logging and runtime security | 20% | Behavioral detection, attack investigation, immutable runtime and Kubernetes auditing |

## 1. Cluster setup — 15%

### Network isolation and secure cluster paths

Map control-plane, node, Pod, Service, ingress/egress, administration, registry, storage and cloud/provider paths before adding rules. Use host/network firewalls and security groups for node/control-plane exposure, and Kubernetes NetworkPolicy for supported Pod L3/L4 flows. Start with explicit management and component requirements; a careless default deny can break DNS, monitoring, admission, storage or the control plane.

NetworkPolicies are additive. A selected Pod is isolated for a direction, and both source egress and destination ingress can govern one connection. Define namespace/Pod selectors and ports precisely; test a permitted flow and a denied flow. Confirm the installed network plugin enforces policy. NetworkPolicy does not provide encryption or application authentication.

Restrict Kubernetes API and kubelet endpoints to necessary networks and identities. Do not expose dashboards, metrics, health, debug or unauthenticated read-only endpoints broadly. Protect node/cloud instance metadata through provider controls, workload identity, host routing/firewall, and Pod egress policy as applicable. The implementation is platform-specific, so prove the path rather than assuming an address is unreachable.

> **Related item:** Segmentation limits reachability; identity and encryption determine who is trusted and whether content is protected. A secure design normally needs all three.

### CIS benchmark review

CIS benchmarks provide a version/distribution-specific configuration baseline. Run an appropriate assessment such as kube-bench against the matching Kubernetes topology and benchmark. Read the control, automated/manual status, rationale and remediation. Inspect actual API server, controller manager, scheduler, etcd, CoreDNS and kubelet ownership—often static Pod manifests, kubelet config or service flags—before editing.

Treat findings as evidence, not an automatic patch list. A control may be not applicable, managed by a provider, or require a documented compensating control. Back up manifests/configuration, change one boundary, watch component/runtime logs and validate API, Nodes, DNS, workloads and audit behavior. Record pass/fail/not-applicable/exception with reason and re-run. A scanner green result does not prove end-to-end security.

### Ingress TLS and platform integrity

For Ingress TLS, identify the controller, class, host, Service/backend, certificate/key Secret, DNS and external path. Use a certificate whose subject names match the host, protect the private key, set correct Secret type/data, and verify handshake, chain, name and expiration from a client. Decide where TLS terminates and whether backend traffic also requires TLS/mTLS. Redirect behavior and cipher/protocol choices may be controller-specific.

Verify platform binaries/packages before deployment using the vendor/project's authenticated repository metadata, checksum and signature/provenance process. Obtain verification material over an independent trusted channel where appropriate. Confirm version and architecture; compare digest/signature before execution; preserve provenance. A matching checksum from the same compromised download location is weak evidence unless authenticity of the checksum is established.

Protect bootstrap tokens, CA keys, kubeconfigs, etcd data, encryption keys and join commands. Limit file permissions, exposure and lifetime, and remove obsolete bootstrap access.

## 2. Cluster hardening — 15%

### RBAC with escalation awareness

Inventory identities, group membership, ServiceAccounts, Role/ClusterRole rules and bindings. Use `kubectl auth can-i`, impersonation in authorized labs, and positive/negative API tests. Scope by API group, resource/subresource, verb, name and namespace. Avoid wildcards and broad cluster bindings.

Privilege is not limited to obvious `cluster-admin`: permission to read Secrets, create/patch workloads under powerful ServiceAccounts, bind/escalate roles, approve certificates, access nodes/proxy/exec/attach, mutate admission configuration or alter webhook workloads can become indirect escalation. Review aggregate roles and default/system roles before editing; some defaults are reconciled by the control plane.

Separate administrative, deployment and runtime identities. Short-lived credentials and audited elevation reduce standing access. Protect kubeconfigs/client keys and disable insecure/anonymous access unless a narrowly understood endpoint requires it. Validate that a denied identity remains denied after bindings, namespace changes and workload recreation.

### ServiceAccounts and API exposure

Assign explicit ServiceAccounts to workloads that call the API; bind only required rules. Avoid using the namespace default ServiceAccount as a shared privileged identity. Disable automatic token mounting when no API access is needed. Prefer projected, time-limited, audience-bound tokens over long-lived token Secrets. Rotate compromised identity material and validate dependents.

Restrict API server network access, authentication mechanisms, authorization mode, admission chain and audit policy. Anonymous authentication, service-account issuer/key settings, client CA, request headers and webhook dependencies require careful compatibility checks. Admission webhooks must have reachable Services/endpoints, correct TLS/CA bundle, narrow match rules, appropriate timeout and a deliberate failure policy; a broken fail-closed webhook can block recovery, while fail-open weakens enforcement.

Kubelet access should require authentication/authorization and use protected transport. Minimize direct node access and API server proxy-style paths. Remove unused dashboard/proxy exposure rather than relying on obscurity.

### Upgrade to remove known vulnerabilities

Inventory Kubernetes/control-plane/node/add-on/runtime versions, image digests, APIs, certificates and support/skew. Review official security advisories and release notes. Upgrade through supported minor steps using the documented kubeadm/provider process; preserve etcd and configuration backups, disruption capacity and recovery access. Upgrade control planes and nodes in the correct order, then validate components, Nodes, DNS, networking, storage, admission, policy and workloads.

Do not equate "latest" with "secure enough." A vulnerability may also require configuration, feature disablement, network restriction, credential rotation or workload mitigation. Conversely, an unsupported hurried upgrade can cause an outage. Document exposure, compensating controls, target, verification and residual risk.

> **Related item:** Patch management is a risk decision and operational change: advisory applicability, version skew, backup, rollout order, functional/security tests and rollback all belong together.

## 3. System hardening — 10%

### Reduce host and identity attack surface

Use a supported minimal node OS/image; inventory packages, services, sockets, users, groups, scheduled jobs, kernel modules and privileged files. Remove or disable only what is unnecessary and test kubelet, runtime, CNI, CSI, time, logging and recovery after changes. Read-only or immutable node designs can reduce drift, but still require a supported update/replacement pipeline.

Harden remote administration: limit source networks, use managed identities/keys, disable obsolete authentication, require accountable privilege elevation, log access, and maintain break-glass recovery. Least-privilege cloud IAM for nodes and control-plane integrations matters because a compromised workload/node may reach provider APIs. Prefer workload identity over shared node credentials where supported; restrict instance metadata accordingly.

Minimize external network access with host firewall/security groups/routes/proxies and egress controls, while preserving cluster dependencies. Enumerate required listeners with `ss` and map each to a process, identity and business need. A closed port on one interface does not prove another address family/interface is closed.

### AppArmor and seccomp

Seccomp filters Linux system calls. Start from a runtime-default profile; create a local/custom profile only from observed legitimate behavior and documented needs. Apply through current Kubernetes security context fields, verify it is loaded/enforced on the target node, test application success and a denied syscall behavior, and inspect runtime/kubelet/kernel evidence. `Unconfined` removes this layer.

AppArmor applies path/operation-oriented mandatory access profiles on supported Linux hosts. Confirm the profile is loaded on every eligible node, attach it using the current Kubernetes mechanism, and test complain/enforce behavior carefully. Examine kernel/audit logs for denials. Scheduling to a node without the required profile can break or weaken the workload; use node preparation/placement controls.

These tools complement non-root user, dropped capabilities, no privilege escalation, read-only root filesystem, SELinux where applicable and sandboxed runtimes. They are not interchangeable. Keep policies narrow enough to reduce risk and maintainable enough to deploy consistently.

> **Related item:** Host hardening must survive node replacement. Encode the approved image, packages, services, firewall, kernel policy and validation in the node build/provisioning pipeline instead of relying on one manual repair.

## 4. Minimize microservice vulnerabilities — 20%

### Pod Security Standards and workload security

Pod Security Standards define Privileged, Baseline and Restricted policy levels. Use Pod Security Admission labels for enforce, audit and warn with an explicit version, then test representative workloads. Move toward Restricted by running as non-root, using an allowed seccomp profile, preventing privilege escalation, dropping capabilities, avoiding privileged/host namespaces/host paths and constraining volume types as required. Understand allowed exceptions rather than broadly labeling every namespace privileged.

Admission rejection is preventive evidence; audit/warn support migration. Protect the namespaces/labels and admission configuration from unauthorized change. Controllers create Pods, so validate rendered workload templates, not only a one-off Pod. Third-party policy engines can express additional organization-specific controls, but their CRDs/controllers/webhooks/RBAC/TLS/failure modes add a security and availability boundary.

### Secrets

Kubernetes Secret data is base64-encoded, not inherently encrypted. Limit RBAC, avoid listing/watch when only a named read is needed, prefer short-lived external/workload identity where possible, enable/configure encryption at rest with a protected key/KMS process, and restrict etcd/backup access. Avoid command history, Git, logs, environment dumps and overly broad volume mounts.

Plan rotation: update source, make new material available, roll/reload dependents, verify, revoke old material and audit. Environment variables do not update in running containers; projected volumes and application reload behavior have separate timing. Deleting a Secret before dependents adopt a replacement can create an outage.

### Multi-tenancy and sandboxing

Namespaces are an administrative scope, not a complete security boundary. Combine namespace isolation with RBAC, quotas/limits, Pod Security Admission, NetworkPolicy, dedicated ServiceAccounts, secret separation, node placement/runtime isolation, admission controls and monitoring. Strong hostile multi-tenancy may require dedicated clusters or nodes based on threat model.

Sandboxed containers such as gVisor/Kata-style runtimes add a boundary through RuntimeClass and underlying node/runtime configuration. Verify the handler exists on eligible nodes, schedule deliberately, and test workload compatibility, observability and performance. Sandboxing does not remove the need for image, identity, network and policy controls.

### Pod-to-Pod encryption

NetworkPolicy does not encrypt. Pod-to-Pod encryption can be provided by a service mesh such as Istio with mTLS or a networking layer such as Cilium, depending on configuration. Identify identity issuance, trust domain, key/certificate rotation, policy mode and coverage—including excluded namespaces/host-network/egress paths. A dashboard "enabled" indicator is weaker than a positive encrypted connection plus a controlled plaintext/unauthorized failure test.

Migration from permissive to strict mTLS needs service compatibility and telemetry. Layer transport identity/encryption with application authorization; mTLS proves a workload identity at a layer, not business permission for every operation.

> **Related item:** Isolation strength follows the threat model. Namespace, process, container, sandboxed runtime, node and cluster boundaries protect against different adversaries and have different cost/compatibility tradeoffs.

## 5. Supply chain security — 20%

### Minimal images and build provenance

Reduce image footprint with trusted minimal bases, multi-stage builds, exact dependencies, no compilers/package managers/debug tools in runtime unless required, non-root execution and a clear patch/rebuild process. Minimal is not automatically vulnerability-free; scanning and lifecycle still matter. Avoid `latest`; record image digest.

Map source commit, dependencies, build definition, builder identity, test/scanner results, SBOM, signature/attestation and published digest. An SBOM inventories components; it does not prove absence of vulnerabilities or build integrity. Provenance describes where/how/by whom an artifact was produced. Protect CI tokens, runners, caches, build arguments, signing keys and artifact repository permissions.

Pin dependencies with appropriate lock/checksum mechanisms, review updates, and prevent untrusted pull-request code from accessing production secrets. Separate build from promotion: promote the same verified digest across environments instead of rebuilding mutable content.

### Registries, signatures and admission

Allow only approved registries/repositories and immutable artifact references through policy. Authenticate and encrypt registry access; limit push/delete/admin permissions; enable retention, audit and replication/recovery as needed. Mirror critical dependencies under governance.

Sign or attest artifacts with protected workload or keyless identity as designed, then verify issuer/identity, repository, digest, claim type and transparency/trust evidence—not merely that some signature exists. Admission can enforce signature, provenance, registry, tag/digest, vulnerability or configuration policies. Test a valid artifact and multiple invalid cases; plan fail-open/fail-closed behavior and recovery if verification dependencies fail.

### Static analysis and vulnerability decisions

Scan source/dependencies, Containerfiles/images and Kubernetes manifests. Tools such as Kubesec/KubeLinter-style analyzers flag risky configuration; image scanners correlate components with vulnerability feeds. Configure severity, fix availability, exploitability/context, age/SLA and exception workflow. Triage false positives and unreachable components without hiding real risk.

Scan at pull request/build, before promotion/admission and continuously because vulnerability data changes after release. A previously clean digest can gain a new finding; immutable images require rebuild/redeploy, not in-place patching. Preserve results tied to digest and policy version. Combine scan results with runtime exposure and compensating controls.

> **Related item:** Supply-chain assurance is a chain of custody. Any uncontrolled source, dependency, builder, credential, repository, promotion or admission link can invalidate confidence in the final image.

## 6. Monitoring, logging and runtime security — 20%

### Behavioral analytics and threat detection

Define expected processes, syscalls, file writes, network destinations, identities and API actions for workloads/nodes. Runtime tools such as Falco-style detectors observe events and apply rules; tune sources, rule conditions, priorities, output and exceptions. Generate only safe, authorized test events and confirm detection reaches the intended destination with useful context.

Detect across physical/virtual infrastructure, hosts, control plane, workloads, network, identity, data and supply chain. Correlate Kubernetes audit records, runtime events, container/application logs, node auth/system logs, network flows, admission/policy decisions and cloud/provider audit. Normalize timestamps and stable identities. Absence of one event source is a visibility gap, not proof of no attack.

Tune noisy rules with narrow, documented exceptions tied to workload identity/image/path/operation, not global disablement. Monitor the detector itself: DaemonSet coverage, permissions, rule version, queue/drop status, clock, output availability and tamper resistance.

### Investigation and attack phases

Triage alert validity and scope, preserve volatile evidence, establish timeline, identify initial access/execution/persistence/privilege escalation/defense evasion/credential access/discovery/lateral movement/collection/exfiltration/impact behaviors as supported by evidence, and determine affected identities/nodes/namespaces/images/data. Framework phase labels help organize hypotheses; they do not replace facts.

Contain proportionately: isolate a workload/node/identity or route while protecting evidence and service recovery. Rotate exposed credentials and replace compromised immutable components from trusted sources. Eradicate root cause, recover, monitor recurrence and document lessons/control changes. Do not run invasive commands on systems you do not own or without incident authority.

### Runtime immutability

Use read-only root filesystems, explicit writable volumes, non-root identity, dropped capabilities, no privilege escalation, seccomp/AppArmor, immutable image digests and controlled exec/ephemeral-container access. Prevent package installation or drift inside running containers; rebuild and redeploy from source. Validate that the application works with expected temp/cache/state paths and that an unauthorized write fails.

Immutable containers do not make nodes, volumes, Secrets or control-plane state immutable. Restrict who can patch workloads, exec/attach/port-forward, create debug containers or change admission/policy. Detect drift by comparing runtime process/files/network and deployed digest/configuration with expected state.

### Kubernetes audit logging

Audit policy chooses which API events and request/response detail to record by users, groups, verbs, resources, namespaces and stages. Levels include none, metadata, request and request-response; avoid capturing Secret bodies or other sensitive content unnecessarily. Configure audit policy and API server log/webhook output with correct file mounts/flags or supported managed-provider controls.

Validate with a known allowed and denied API request, then locate user, verb, resource, namespace, stage, response code, source and correlation fields. Protect log transport/storage from tampering and unauthorized reading; set rotation, retention, capacity and alerting. An audit policy that generates data but loses it to disk exhaustion or an unreachable webhook is not an effective control.

> **Related item:** Prevention reduces likelihood, detection reduces time-to-know, response limits impact, and recovery restores trust. CKS spans all four; no single scanner or policy is a security program.

## Integrated scenarios

### Scenario 1: Harden a new kubeadm cluster without losing recovery

Map API/kubelet/etcd/node/Pod/Ingress paths and preserve console, manifests and verified etcd/config backup. Run the matching CIS assessment and triage findings. Restrict firewall/API/kubelet, apply least-privilege RBAC/ServiceAccounts and default-deny policies, configure TLS Ingress, protect metadata and verify binaries. Change one control at a time, re-run the relevant check, and validate API, Nodes, DNS, workload traffic, audit and recovery. Record exceptions rather than blindly forcing every automated result.

### Scenario 2: Govern an application from source to runtime

Build a minimal non-root image from pinned dependencies, generate an SBOM, scan source/image/manifests, and publish a digest to an approved registry. Sign/attest it and configure admission to accept the correct identity/digest and reject an unsigned or disallowed artifact. Deploy under Restricted Pod Security, minimum ServiceAccount/RBAC, default-deny policy, Secret controls, read-only root, seccomp and mTLS. Prove function and negative controls, then rebuild/promote the same workflow after a new vulnerability finding.

### Scenario 3: Investigate suspicious activity safely

A runtime detector reports a shell/process and an unusual API access follows. Confirm sensor health and preserve the alert, Kubernetes audit event, Pod spec/image digest, current/previous logs, runtime processes, node/auth logs and network evidence. Build a time-normalized timeline, scope identity/workload/node impact, and contain through authorized network/identity/workload action. Rotate exposed credentials, replace from verified artifacts, correct admission/RBAC/runtime gaps, recover and watch for recurrence. Do not erase the only Pod before collecting volatile evidence.

## Hands-on labs

Use only disposable or explicitly authorized environments; snapshots and console access are strongly recommended.

1. **CIS-guided setup (3–5 hours):** run a matching benchmark, manually validate findings across API server/etcd/controller/scheduler/CoreDNS/kubelet, remediate selected safe items one at a time, and record pass/fail/not-applicable/exception evidence.
2. **Cluster access and segmentation (3–4 hours):** implement minimum RBAC/ServiceAccounts, disabled token automount where unused, API/kubelet/network exposure restrictions, default-deny policies, metadata protection and TLS Ingress. Prove allowed and denied paths.
3. **Host and kernel profiles (3–5 hours):** minimize services/ports/users on disposable nodes, apply runtime-default/custom seccomp and an AppArmor profile where supported, then test application success, denied action, node reboot and rescheduling coverage.
4. **Restricted workload and Secrets (2–4 hours):** enforce/audit/warn current Pod Security Standards, configure restrictive security context, encryption-at-rest lab or documented KMS equivalent, minimum Secret RBAC and a full rotation with dependent rollout/revocation.
5. **Isolation and mTLS (3–5 hours):** compare namespace-only, policy, sandbox RuntimeClass and dedicated placement boundaries. Configure Cilium- or Istio-style Pod-to-Pod encryption in a disposable environment and prove encrypted success plus unauthorized/plaintext failure as supported.
6. **Trusted supply chain (4–6 hours):** create a minimal image, SBOM, scans, digest, signature/attestation and approved-registry policy. Exercise accept/reject cases and rebuild/redeploy the same source after changing a dependency or policy threshold.
7. **Audit and runtime response (3–5 hours):** enable a safe audit policy, deploy a runtime detector, generate authorized test events, correlate at least four sources, investigate/contain/recover, and measure whether alerts/logs survive restart and rotation.
8. **Two-hour rehearsal (2.5–3 hours each):** create original defensive tasks in current official proportions. Use a fresh cluster, keep recovery access, track skipped tasks, validate positive/negative behavior and reserve 10–15 minutes for context, persistence and evidence review.

## Original knowledge checks

1. **Which first-three domain weights does this guide use?** The live Linux Foundation v1.35 weights: Cluster Setup 15%, Cluster Hardening 15%, System Hardening 10%.
2. **Does CKA have to remain active for CKS?** No; current official wording requires that CKA was passed previously.
3. **Why is NetworkPolicy not encryption?** It permits/denies L3/L4 flows but does not protect content cryptographically.
4. **How should a CIS failure be handled?** Validate applicability/ownership/risk, change safely, test and document remediation or exception.
5. **Why test cluster health after a benchmark remediation?** Component flag/config changes can secure one setting while breaking API, node, DNS or workload behavior.
6. **What must Ingress TLS validation include?** Host/name, chain, expiration, Secret/controller/backend path and actual client handshake.
7. **Why is a checksum alone sometimes weak?** If binary and checksum share a compromised source, neither establishes authenticity without signature/trusted channel.
8. **What does metadata protection prevent?** Unauthorized workloads reaching node/cloud identity or sensitive instance metadata endpoints.
9. **Why can Secret read be privilege escalation?** Secrets may contain service tokens, kubeconfigs or application/cloud credentials.
10. **What makes `bind`/`escalate` permissions sensitive?** They can grant or create roles beyond the caller's existing authority.
11. **Why disable ServiceAccount token automount?** A workload that does not call the API should not receive an unnecessary bearer token.
12. **Fail-open versus fail-closed webhook?** Availability versus enforcement tradeoff that must be explicitly designed and tested.
13. **Why upgrade after a security advisory?** To remove vulnerable code when applicable, while also applying any required configuration/credential/network mitigation.
14. **Why is an unsupported emergency upgrade risky?** Version skew and add-on/API incompatibility can create outage or weaken controls.
15. **What proves a port is unnecessary?** Mapping listener/process/interface/dependency/business need, not its unfamiliar name.
16. **Seccomp versus AppArmor?** Syscall filtering versus path/operation-oriented mandatory access control on supported Linux systems.
17. **Why must AppArmor profiles exist on every eligible node?** A rescheduled Pod otherwise fails or lacks the intended profile.
18. **What does Restricted Pod Security generally reduce?** Privilege, host access, privilege escalation, excess capabilities and unconfined syscall behavior.
19. **Why version Pod Security labels?** To make policy semantics predictable across cluster upgrades.
20. **Is namespace a complete tenant boundary?** No; combine access, policy, network, identity, resource, runtime/node and monitoring controls.
21. **Why is base64 not Secret encryption?** It is reversible representation without cryptographic confidentiality.
22. **Safe Secret rotation order?** Issue new, distribute/roll and verify, revoke old, then audit/clean up.
23. **What does RuntimeClass select?** A configured runtime handler and associated isolation behavior on prepared nodes.
24. **What must mTLS testing prove?** Correct identity/encrypted success, certificate rotation/coverage and expected unauthorized/plaintext failure.
25. **Why minimize runtime images?** Fewer packages/tools reduce attack surface, findings and post-compromise utility.
26. **What does an SBOM prove?** An inventory claim about components; not absence of vulnerabilities or artifact provenance by itself.
27. **Why promote by digest?** The exact verified artifact moves across environments without mutable-tag substitution or rebuild drift.
28. **What must signature verification constrain?** Trusted issuer/identity, artifact repository/digest and expected attestation claims.
29. **Why scan continuously after release?** Vulnerability intelligence changes even when the image digest does not.
30. **Why preserve scan policy version?** The same findings may produce different decisions under different thresholds/exceptions.
31. **What is a useful runtime baseline?** Expected processes, syscalls, file writes, network destinations, identities and API actions.
32. **Why monitor the detector?** Missing node coverage, dropped events or broken output can silently erase visibility.
33. **What should a narrow detection exception include?** Exact workload/image/operation context, owner, reason and review/expiry.
34. **Why correlate multiple telemetry sources?** Each source covers a different layer and can confirm identity, sequence and scope.
35. **Why preserve volatile evidence before deletion?** Process/network/container state and previous logs may disappear with the workload.
36. **What does read-only root not protect?** Writable volumes, Secrets, node/control-plane state or authorized workload replacement.
37. **Why restrict exec/debug permissions?** They permit runtime inspection/change that can bypass immutable-image intent.
38. **What are Kubernetes audit stages useful for?** Understanding request receipt, response start and completion/panic timing where recorded.
39. **Why avoid request bodies for Secrets in broad audit policy?** Audit storage could become another repository of sensitive material.
40. **What completes a security change?** Legitimate function, denied/detected negative case, persistence, evidence, rollback and residual-risk record.

## Places to learn

| Resource | Access | Estimated time |
|---|---|---:|
| [Official CKS page](https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/) and [CNCF CKS page](https://www.cncf.io/training/certification/cks/) | Public; exam paid | 3–5 hours mapping/discrepancy review, plus 8–14 selected simulator hours |
| [Public CNCF CKS v1.34 curriculum](https://github.com/cncf/curriculum/blob/master/CKS_Curriculum%20v1.34.pdf) | Public | 1–2 hours; gap-check every item against the live v1.35 page |
| [Kubernetes v1.35 documentation](https://v1-35.docs.kubernetes.io/docs/home/) | Public | 20–35 selected security reading/lab hours; use as a reference |
| [Linux Foundation Kubernetes Security Essentials (LFS260)](https://training.linuxfoundation.org/training/kubernetes-security-essentials-lfs260/) | Paid | 26–30 listed course hours plus 35–70 independent lab hours |
| [Pluralsight CKS path](https://www.pluralsight.com/paths/certified-kubernetes-security-specialist-cks) | Subscription/trial | 12 listed hours, seven courses, three refreshed 2026 labs and practice exam; add 35–70 lab hours |
| [KodeKloud CKS](https://kodekloud.com/courses/certified-kubernetes-security-specialist-cks/) | Subscription/free preview | 8.75 listed video hours plus browser labs/mock exams; public update history stops at v1.33, so allow 30–55 hours with gap work |
| [O'Reilly Certified Kubernetes Security Specialist](https://www.oreilly.com/videos/certified-kubernetes-security/9780138296537/) | Subscription/trial | 19 hours 38 minutes listed plus 35–70 lab hours; February 2025 |
| [Udemy Certified Kubernetes Security Specialist 2026](https://www.udemy.com/course/certified-kubernetes-security-specialist-certification/) | Paid; price varies | 19 hours 58 minutes listed plus independent labs; updated July 2026 |

This is not a complete list and is not meant to be consumed in full. Earn CKA first, choose one current structured security route, and use the live Linux Foundation v1.35 objectives as the source of truth while the CNCF page/PDF lag. Build every control in disposable infrastructure and verify both legitimate behavior and denial/detection. Check tools and course examples for current Pod Security Standards, admission APIs, seccomp/AppArmor fields, signatures/provenance, runtime detection and the 15/15/10 weights. Avoid recalled tasks and question dumps; this is a defensive performance exam.
