---
exam_code: CKS
vendor_id: linux-foundation
official_blueprint: https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# CKS Certified Kubernetes Security Specialist Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 29, 2026. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#cks-coverage-record). The [official CKS page](https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/) is authoritative.

**Current baseline:** Kubernetes v1.35 and the six weighted domains on the live Linux Foundation CKS page: 15% / 15% / 10% / 20% / 20% / 20%<br>
**Source discrepancy:** The [CNCF CKS page](https://www.cncf.io/training/certification/cks/) still shows the earlier 10% / 15% / 15% first-three weights, and the public repository's latest named [CKS curriculum PDF is v1.34](https://github.com/cncf/curriculum/blob/master/CKS_Curriculum%20v1.34.pdf). The actual three-page PDF was read on September 29: despite its filename, its 26 competencies and weights match the live Linux Foundation outline, apart from minor wording/case differences. The overview page remains inconsistent; the live exam page governs.<br>
**Lifecycle watch:** Kubernetes [v1.37 was released August 26, 2026](https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/), while the live CKS page still names v1.35 on September 29. Linux Foundation says alignment follows by approximately 4–8 weeks, so recheck between September 23 and October 21 and immediately before practice or scheduling; this is a watch window, not an announced switch date.<br>
**Official delivery snapshot:** Online, remotely proctored, performance-based command-line exam; two hours; certification valid for two years; 12-month eligibility, one retake, and two 36-hour Killer.sh simulator activations; the public certification page now lists 17 simulator questions per attempt as of September 29, 2026 (separate from the live exam)<br>
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

**PRACTICAL DEPTH — peer scope:** A single NetworkPolicy peer containing both Pod and namespace selectors means selected Pods in selected namespaces. Separate peer entries allow either set; a Pod selector alone is local to the policy namespace. Other policies can add permissions. Test the same client label in both permitted and unpermitted namespaces and inspect all selecting policies. For node/host-network, NAT and external paths, validate the plugin's actual behavior rather than treating a manifest as a packet trace. See [the v1.35 NetworkPolicy source](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/concepts/services-networking/network-policies.md).

### CIS benchmark review

CIS benchmarks provide a version/distribution-specific configuration baseline. Run an appropriate assessment such as kube-bench against the matching Kubernetes topology and benchmark. Read the control, automated/manual status, rationale and remediation. Inspect actual API server, controller manager, scheduler, etcd, CoreDNS and kubelet ownership—often static Pod manifests, kubelet config or service flags—before editing.

Treat findings as evidence, not an automatic patch list. A control may be not applicable, managed by a provider, or require a documented compensating control. Back up manifests/configuration, change one boundary, watch component/runtime logs and validate API, Nodes, DNS, workloads and audit behavior. Record pass/fail/not-applicable/exception with reason and re-run. A scanner green result does not prove end-to-end security.

### Ingress TLS and platform integrity

For Ingress TLS, identify the controller, class, host, Service/backend, certificate/key Secret, DNS and external path. Use a certificate whose subject names match the host, protect the private key, set correct Secret type/data, and verify handshake, chain, name and expiration from a client. Decide where TLS terminates and whether backend traffic also requires TLS/mTLS. Redirect behavior and cipher/protocol choices may be controller-specific.

The Kubernetes project [retired the community ingress-nginx controller in March 2026](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/), not the stable Kubernetes Ingress API or the current CKS Ingress TLS objective. In a provided exam environment, follow the installed controller and task contract. For production practice, select a maintained implementation and validate IngressClass, controller-specific annotations, TLS, routing, observability, cutover and rollback; do not translate one controller's retirement into a claim that Ingress resources no longer work.

Verify platform binaries/packages before deployment using the vendor/project's authenticated repository metadata, checksum and signature/provenance process. Obtain verification material over an independent trusted channel where appropriate. Confirm version and architecture; compare digest/signature before execution; preserve provenance. A matching checksum from the same compromised download location is weak evidence unless authenticity of the checksum is established.

Protect bootstrap tokens, CA keys, kubeconfigs, etcd data, encryption keys and join commands. Limit file permissions, exposure and lifetime, and remove obsolete bootstrap access.

## 2. Cluster hardening — 15%

### RBAC with escalation awareness

Inventory identities, group membership, ServiceAccounts, Role/ClusterRole rules and bindings. Use `kubectl auth can-i`, impersonation in authorized labs, and positive/negative API tests. Scope by API group, resource/subresource, verb, name and namespace. Avoid wildcards and broad cluster bindings.

Privilege is not limited to obvious `cluster-admin`: permission to read Secrets, create/patch workloads under powerful ServiceAccounts, bind/escalate roles, approve certificates, access nodes/proxy/exec/attach, mutate admission configuration or alter webhook workloads can become indirect escalation. Review aggregate roles and default/system roles before editing; some defaults are reconciled by the control plane.

Separate administrative, deployment and runtime identities. Short-lived credentials and audited elevation reduce standing access. Protect kubeconfigs/client keys and disable insecure/anonymous access unless a narrowly understood endpoint requires it. Validate that a denied identity remains denied after bindings, namespace changes and workload recreation.

**Named reads and delegation:** `resourceNames` can restrict named reads, but top-level `create` and `deletecollection` cannot be confined this way. Restricted list/watch clients must supply a matching `metadata.name` field selector. Also separate ordinary permission to edit Roles/Bindings from permission to grant more access: role escalation and binding restrictions apply unless the caller already has the permissions or has the relevant `escalate`/`bind` authority. Review these explicitly; a role-editor label alone does not describe effective privilege. See [RBAC restrictions](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/reference/access-authn-authz/rbac.md).

### ServiceAccounts and API exposure

Assign explicit ServiceAccounts to workloads that call the API; bind only required rules. Avoid using the namespace default ServiceAccount as a shared privileged identity. Disable automatic token mounting when no API access is needed. Prefer projected, time-limited, audience-bound tokens over long-lived token Secrets. Rotate compromised identity material and validate dependents.

Restrict API server network access, authentication mechanisms, authorization mode, admission chain and audit policy. Anonymous authentication, service-account issuer/key settings, client CA, request headers and webhook dependencies require careful compatibility checks. Admission webhooks must have reachable Services/endpoints, correct TLS/CA bundle, narrow match rules, appropriate timeout and a deliberate failure policy; a broken fail-closed webhook can block recovery, while fail-open weakens enforcement.

Kubelet access should require authentication/authorization and use protected transport. Minimize direct node access and API server proxy-style paths. Remove unused dashboard/proxy exposure rather than relying on obscurity.

**Token and webhook checks:** Pod-level `automountServiceAccountToken` overrides the ServiceAccount setting. Turning off automatic mounting does not revoke RBAC or prevent a deliberately configured projection; inspect actual Pod identity and required audience. Sources: [ServiceAccount behavior](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/tasks/configure-pod-container/configure-service-account.md) and [Secret handling](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/concepts/configuration/secret.md).

A webhook's `failurePolicy: Ignore` allows a request to continue when the webhook call errors or times out; it does not override an explicit admission denial. `Fail` rejects call failures. A dry-run-compatible webhook must suppress side effects on dry-run requests, and a successful admission response still does not guarantee the object was eventually persisted. Test policy decisions separately from TLS/timeout/reachability failures and preserve a documented recovery route. See [admission webhook behavior](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/reference/access-authn-authz/extensible-admission-controllers.md).

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

**Requested versus effective kernel policy:** An unspecified seccomp field normally leaves a container Unconfined unless the kubelet's seccomp-default setting supplies RuntimeDefault. That defaulting does not write a seccomp field into the Pod object; inspect runtime evidence. Privileged containers run Unconfined even when a seccomp profile is requested. RuntimeDefault profiles can differ by runtime/version. See [seccomp defaulting and runtime checks](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/tutorials/security/seccomp.md).

An explicitly requested AppArmor Localhost profile must be loaded on the target node. API object creation can succeed while kubelet refuses to run the Pod because a profile is unavailable. Check node support, loaded profile and process confinement, then repeat on another eligible node. A successful API create is not proof of host enforcement. See [AppArmor prerequisites and profile selection](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/tutorials/security/apparmor.md).

## 4. Minimize microservice vulnerabilities — 20%

### Pod Security Standards and workload security

Pod Security Standards define Privileged, Baseline and Restricted policy levels. Use Pod Security Admission labels for enforce, audit and warn with an explicit version, then test representative workloads. Move toward Restricted by running as non-root, using an allowed seccomp profile, preventing privilege escalation, dropping capabilities, avoiding privileged/host namespaces/host paths and constraining volume types as required. Understand allowed exceptions rather than broadly labeling every namespace privileged.

Admission rejection is preventive evidence; audit/warn support migration. Protect the namespaces/labels and admission configuration from unauthorized change. Controllers create Pods, so validate rendered workload templates, not only a one-off Pod. Third-party policy engines can express additional organization-specific controls, but their CRDs/controllers/webhooks/RBAC/TLS/failure modes add a security and availability boundary.

**Admission is not retroactive repair:** Enforce mode applies to resulting Pods, while warn/audit also evaluate workload templates. A Deployment can therefore exist while its controller's Pods are denied; read ReplicaSet Events. Changing an enforce label checks existing Pods and returns warnings about violations—it does not repair their specifications. Exempt namespaces, users or RuntimeClasses skip all three modes, so review exemptions and the controller identity as well as labels. Sources: [Pod Security Admission](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/concepts/security/pod-security-admission.md) and [namespace-label evaluation](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/tasks/configure-pod-container/enforce-standards-namespace-labels.md).

**CURRENT BLUEPRINT / PRACTICAL DEPTH:** Pin the policy version and inspect all app, init and ephemeral containers. For Linux Restricted policy, an allowed seccomp profile must be explicit at the Pod or relevant container levels, privilege escalation must be disabled, and capabilities must drop `ALL` with only `NET_BIND_SERVICE` permitted to be added. Version 1.34+ also restricts host fields in probes/lifecycle hooks under Baseline, inherited by Restricted. Admission tests, actual process privileges and application behavior answer separate questions. See [the v1.35 Pod Security Standards](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/concepts/security/pod-security-standards.md).

### Secrets

Kubernetes Secret data is base64-encoded, not inherently encrypted. Limit RBAC, avoid listing/watch when only a named read is needed, prefer short-lived external/workload identity where possible, enable/configure encryption at rest with a protected key/KMS process, and restrict etcd/backup access. Avoid command history, Git, logs, environment dumps and overly broad volume mounts.

Plan rotation: update source, make new material available, roll/reload dependents, verify, revoke old material and audit. Environment variables do not update in running containers; projected volumes and application reload behavior have separate timing. Deleting a Secret before dependents adopt a replacement can create an outage.

**At-rest migration and rotation:** The first encryption provider, and its first key, writes new data; reading tries matching providers/keys in order. An `identity` provider first means new writes lack confidentiality protection. Merely enabling encryption does not rewrite old records. Keep compatible configuration across API servers, verify migration through controlled storage evidence, and retain old decryption material until all required data and backups can be recovered with the intended keys. A normal Secret API read returns decoded usable data after decryption and cannot by itself prove storage encryption. Do not remove a key merely because new Secret creation works. See [encryption-at-rest configuration and rotation](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/tasks/administer-cluster/encrypt-data.md).

For runtime volume access, container security settings override overlapping Pod settings; filesystem groups and driver support govern mounted data separately from root-filesystem write protection. Validate actual ownership and paths rather than granting broad privilege to fix every mount failure. See [effective security contexts](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/tasks/configure-pod-container/security-context.md).

### Multi-tenancy and sandboxing

Namespaces are an administrative scope, not a complete security boundary. Combine namespace isolation with RBAC, quotas/limits, Pod Security Admission, NetworkPolicy, dedicated ServiceAccounts, secret separation, node placement/runtime isolation, admission controls and monitoring. Strong hostile multi-tenancy may require dedicated clusters or nodes based on threat model.

Sandboxed containers such as gVisor/Kata-style runtimes add a boundary through RuntimeClass and underlying node/runtime configuration. Verify the handler exists on eligible nodes, schedule deliberately, and test workload compatibility, observability and performance. Sandboxing does not remove the need for image, identity, network and policy controls.

### Pod-to-Pod encryption

NetworkPolicy does not encrypt. Pod-to-Pod encryption can be provided by a service mesh such as Istio with mTLS or a networking layer such as Cilium, depending on configuration. Identify identity issuance, trust domain, key/certificate rotation, policy mode and coverage—including excluded namespaces/host-network/egress paths. A dashboard "enabled" indicator is weaker than a positive encrypted connection plus a controlled plaintext/unauthorized failure test.

Migration from permissive to strict mTLS needs service compatibility and telemetry. Layer transport identity/encryption with application authorization; mTLS proves a workload identity at a layer, not business permission for every operation.

> **Related item:** Isolation strength follows the threat model. Namespace, process, container, sandboxed runtime, node and cluster boundaries protect against different adversaries and have different cost/compatibility tradeoffs.

**Encryption coverage exercise:** In Istio sidecar mode, `PERMISSIVE` admits both plaintext and mTLS, while `STRICT` requires mTLS. A port-level exception uses the workload port, not the Service port. Authentication/encryption and authorization remain separate; an `AUDIT` authorization action also needs a supporting audit plugin and does not deny requests. Account for sidecar versus ambient behavior and installed version. Sources: [PeerAuthentication](https://istio.io/latest/docs/reference/config/security/peer_authentication/) and [AuthorizationPolicy](https://istio.io/latest/docs/reference/config/security/authorization-policy/).

Cilium WireGuard does not encrypt packets whose source and destination are on the same node. Node encryption has additional configuration and exclusions, including the default control-plane-node opt-out; this is distinct from Cilium-managed cross-node Pod traffic. Build a coverage matrix for same-node, cross-node, host, control-plane and external paths, and verify the implementation's actual encrypted segments. See [Cilium WireGuard coverage](https://docs.cilium.io/en/stable/security/network/encryption-wireguard/). These are proposed cluster checks; no mesh or network encryption was configured here.

## 5. Supply chain security — 20%

### Minimal images and build provenance

Reduce image footprint with trusted minimal bases, multi-stage builds, exact dependencies, no compilers/package managers/debug tools in runtime unless required, non-root execution and a clear patch/rebuild process. Minimal is not automatically vulnerability-free; scanning and lifecycle still matter. Avoid `latest`; record image digest.

Map source commit, dependencies, build definition, builder identity, test/scanner results, SBOM, signature/attestation and published digest. An SBOM inventories components; it does not prove absence of vulnerabilities or build integrity. Provenance describes where/how/by whom an artifact was produced. Protect CI tokens, runners, caches, build arguments, signing keys and artifact repository permissions.

Pin dependencies with appropriate lock/checksum mechanisms, review updates, and prevent untrusted pull-request code from accessing production secrets. Separate build from promotion: promote the same verified digest across environments instead of rebuilding mutable content.

### Registries, signatures and admission

Allow only approved registries/repositories and immutable artifact references through policy. Authenticate and encrypt registry access; limit push/delete/admin permissions; enable retention, audit and replication/recovery as needed. Mirror critical dependencies under governance.

Sign or attest artifacts with protected workload or keyless identity as designed, then verify issuer/identity, repository, digest, claim type and transparency/trust evidence—not merely that some signature exists. Admission can enforce signature, provenance, registry, tag/digest, vulnerability or configuration policies. Test a valid artifact and multiple invalid cases; plan fail-open/fail-closed behavior and recovery if verification dependencies fail.

### Offline exercise: signature, artifact and approval are separate

Save the following original script as `cks_signature_practice.py` and run `python cks_signature_practice.py /path/to/openssl`. On Windows, quote the executable path. It generates temporary EC P-256 keys, signs a small synthetic statement with SHA-256, verifies the exact signed bytes and checks selected claims plus the artifact digest. Its schema is invented for teaching; it is not an OCI image, SBOM, SLSA or DSSE implementation. No registry or cluster is involved. Sources for the cryptographic operations: [OpenSSL key generation](https://docs.openssl.org/3.5/man1/openssl-genpkey/) and [detached signing and verification](https://docs.openssl.org/3.5/man1/openssl-dgst/).

```python
"""Original offline signature/claim exercise; Python and OpenSSL 3.5 required."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


def exercise(openssl, parent=None):
    checks = []
    def check(label, condition):
        if not condition:
            raise AssertionError(label)
        checks.append(label)
    env = {k: v for k, v in os.environ.items() if not k.startswith("OPENSSL_")}
    # A new child-process configuration; the user's global configuration is untouched.
    env["OPENSSL_CONF"] = "/dev/null" if os.name != "nt" or "Git" in str(openssl) else "NUL"
    with tempfile.TemporaryDirectory(prefix="cks-signature-", dir=parent) as temporary:
        root = Path(temporary).resolve()
        if not root.is_relative_to(Path(parent or tempfile.gettempdir()).resolve()):
            raise RuntimeError("Temporary path is outside its intended parent")
        def run(*args, success=True):
            result = subprocess.run([str(openssl), *args], cwd=root, env=env,
                                    capture_output=True, text=True, timeout=20)
            if success and result.returncode:
                raise RuntimeError(result.stderr)
            return result
        version = run("version").stdout.strip()
        for name in ("trusted", "other"):
            run("genpkey", "-algorithm", "EC", "-pkeyopt", "ec_paramgen_curve:P-256",
                "-out", name + ".pem")
            run("pkey", "-in", name + ".pem", "-pubout", "-out", name + ".pub")
        artifact = root / "artifact.bin"
        # This is a synthetic byte payload, not an OCI image or real SBOM.
        artifact.write_bytes(b"original training payload\n")
        original_bytes = artifact.read_bytes()
        statement = root / "statement.json"
        signature = root / "statement.sig"
        manifest = {
            "schema": "training-provenance/v1",
            "subject": {"name": "registry.example.invalid/practice/app",
                        "sha256": hashlib.sha256(original_bytes).hexdigest()},
            "builder": "practice-builder",
            "release": "r1"
        }
        def sign_bytes(payload):
            statement.write_bytes(payload)
            run("dgst", "-sha256", "-sign", "trusted.pem", "-out", signature.name, statement.name)
        def sign(value):
            sign_bytes(json.dumps(value, sort_keys=True, separators=(",", ":")).encode())
        def signature_valid(public_key="trusted.pub"):
            return run("dgst", "-sha256", "-verify", public_key,
                       "-signature", signature.name, statement.name, success=False).returncode == 0
        def assess(public_key="trusted.pub", expected_release="r1"):
            # The trusted key is supplied independently, never selected by an untrusted claim.
            if not signature_valid(public_key):
                return "signature-rejected"
            try:
                claim = json.loads(statement.read_bytes())
                approved = (claim["schema"] == "training-provenance/v1"
                            and claim["subject"]["name"] == "registry.example.invalid/practice/app"
                            and claim["builder"] == "practice-builder"
                            and claim["release"] == expected_release)
                if not approved:
                    return "claim-rejected"
                if claim["subject"]["sha256"] != hashlib.sha256(artifact.read_bytes()).hexdigest():
                    return "digest-rejected"
            except (ValueError, KeyError, TypeError):
                return "claim-rejected"
            return "accepted-for-this-exercise"
        sign(manifest)
        original_statement = statement.read_bytes()
        original_signature = signature.read_bytes()
        check("expected signature verifies", signature_valid())
        check("expected claims and artifact accepted", assess() == "accepted-for-this-exercise")
        check("different trusted key rejected", assess("other.pub") == "signature-rejected")
        check("valid old release rejected by new release requirement", assess(expected_release="r2") == "claim-rejected")
        artifact.write_bytes(original_bytes + b"changed\n")
        check("statement signature alone does not inspect artifact", signature_valid())
        check("changed artifact fails signed digest binding", assess() == "digest-rejected")
        artifact.write_bytes(original_bytes)
        statement.write_bytes(original_statement + b"\n")
        check("even whitespace changes signed bytes", assess() == "signature-rejected")
        statement.write_bytes(original_statement)
        signature.write_bytes(b"invalid signature")
        check("damaged signature rejected", assess() == "signature-rejected")
        signature.write_bytes(original_signature)
        check("restored bytes and signature accepted", assess() == "accepted-for-this-exercise")
        for field, value in (("builder", "unapproved-builder"), ("schema", "unknown/v1"), ("release", "old")):
            altered = dict(manifest, **{field: value})
            sign(altered)
            check("valid signature on unapproved " + field, signature_valid() and assess() == "claim-rejected")
        altered = dict(manifest, subject=dict(manifest["subject"], name="registry.example.invalid/other/app"))
        sign(altered)
        check("valid signature on wrong repository claim rejected", signature_valid() and assess() == "claim-rejected")
        sign_bytes(b"not JSON")
        check("signed malformed claim rejected", signature_valid() and assess() == "claim-rejected")
        sign({"schema": "training-provenance/v1"})
        check("signed incomplete claim rejected", signature_valid() and assess() == "claim-rejected")
        sign(manifest)
        check("repaired original claim accepted", assess() == "accepted-for-this-exercise")
    check("owned temporary keys and payloads removed", not root.exists())
    return {"passed": len(checks), "checks": checks, "openssl": version,
            "cleanup_verified": True,
            "boundary": "Synthetic detached signatures and deliberately narrow claim checks only; no publisher identity proof, standard attestation, transparency log, registry, image scan, admission or live cluster."}


if __name__ == "__main__":
    print(json.dumps(exercise(Path(sys.argv[1]).resolve()), indent=2))
```

**Executed September 29:** 17 checks passed with Git for Windows OpenSSL **3.5.7**, including wrong-key, changed-artifact, changed-statement, damaged-signature, wrong-release/repository/builder/schema and malformed/incomplete-claim cases. Temporary keys and data were removed. The trusted verification key is an explicit exercise assumption; generating a key locally does not prove a publisher's identity. A valid signature can accompany an unapproved claim, and a valid signed statement can refer to bytes different from the artifact supplied for deployment. The script does not verify keyless identity, transparency records, standard attestations, vulnerability status, SBOM completeness or admission policy. A production verifier must define those trust and policy requirements separately.

### Static analysis and vulnerability decisions

Scan source/dependencies, Containerfiles/images and Kubernetes manifests. Tools such as Kubesec/KubeLinter-style analyzers flag risky configuration; image scanners correlate components with vulnerability feeds. Configure severity, fix availability, exploitability/context, age/SLA and exception workflow. Triage false positives and unreachable components without hiding real risk.

Scan at pull request/build, before promotion/admission and continuously because vulnerability data changes after release. A previously clean digest can gain a new finding; immutable images require rebuild/redeploy, not in-place patching. Preserve results tied to digest and policy version. Combine scan results with runtime exposure and compensating controls.

> **Related item:** Supply-chain assurance is a chain of custody. Any uncontrolled source, dependency, builder, credential, repository, promotion or admission link can invalidate confidence in the final image.

## 6. Monitoring, logging and runtime security — 20%

### Behavioral analytics and threat detection

Define expected processes, syscalls, file writes, network destinations, identities and API actions for workloads/nodes. Runtime tools such as Falco-style detectors observe events and apply rules; tune sources, rule conditions, priorities, output and exceptions. Generate only safe, authorized test events and confirm detection reaches the intended destination with useful context.

Detect across physical/virtual infrastructure, hosts, control plane, workloads, network, identity, data and supply chain. Correlate Kubernetes audit records, runtime events, container/application logs, node auth/system logs, network flows, admission/policy decisions and cloud/provider audit. Normalize timestamps and stable identities. Absence of one event source is a visibility gap, not proof of no attack.

Tune noisy rules with narrow, documented exceptions tied to workload identity/image/path/operation, not global disablement. Monitor the detector itself: DaemonSet coverage, permissions, rule version, queue/drop status, clock, output availability and tamper resistance.

**Rule quality and sensor quality:** Falco rule priority expresses severity; it is not a mechanism for overriding other rules. A process-name condition without an event-type restriction can match many syscalls and create repeated noise. Use fields supported by the selected event source, constrain the intended event, and verify output delivery and dropped-event/coverage evidence. Missing output fields can appear as unavailable rather than proving the underlying event did not happen. See [Falco rule elements](https://falco.org/docs/concepts/rules/basic-elements/). No Falco sensor or runtime event was exercised in this review.

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

### Offline exercise: audit-rule order

The [audit documentation](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/tasks/debug/debug-cluster/audit.md) and [v1.35 policy API types](https://raw.githubusercontent.com/kubernetes/apiserver/release-1.35/pkg/apis/audit/v1/types.go) specify first-match rule selection; no match means no event. Global and rule-specific omitted stages are combined. Put sensitive-resource rules before broad body-logging rules. Metadata omits request/response bodies, but still requires protected log storage.

Save this original model as `cks_audit_practice.py` and run it with Python. Its `POLICY` deliberately keeps Secret accesses at Metadata, records bodies only for selected ConfigMap writes in a synthetic namespace, and uses Metadata as its fallback. The model rejects unsupported selectors and covers only the stated exact resource/group/namespace/verb/stage subset. It is neither a full API schema validator nor Kubernetes audit execution.

```python
"""A small audit-policy reasoning model, not a Kubernetes evaluator."""
import copy

POLICY = {
    "apiVersion": "audit.k8s.io/v1", "kind": "Policy",
    "omitStages": ["RequestReceived"],
    "rules": [
        {"level": "Metadata", "resources": [{"group": "", "resources": ["secrets"]}]},
        {"level": "RequestResponse", "verbs": ["create", "update", "patch"],
         "namespaces": ["practice"],
         "resources": [{"group": "", "resources": ["configmaps"]}],
         "omitStages": ["ResponseStarted"]},
        {"level": "Metadata"}
    ]
}


def audit_level(policy, event):
    # Explicitly reject unsupported selectors instead of silently ignoring them.
    if set(policy) - {"apiVersion", "kind", "omitStages", "rules"}:
        raise ValueError("Unsupported policy field")
    if not policy.get("rules"):
        raise ValueError("This model requires at least one rule")
    for rule in policy["rules"]:
        if set(rule) - {"level", "verbs", "namespaces", "resources", "omitStages"}:
            raise ValueError("Unsupported rule selector")
        if rule["level"] not in {"None", "Metadata", "Request", "RequestResponse"}:
            raise ValueError("Unknown audit level")
        for group in rule.get("resources", []):
            if set(group) - {"group", "resources"}:
                raise ValueError("Unsupported resource selector")
            if any("*" in name or "/" in name for name in group.get("resources", [])):
                raise ValueError("This model uses only exact main-resource names")
    if "/" in event["resource"]:
        raise ValueError("Subresource events are outside this exercise")
    for rule in policy["rules"]:
        if rule.get("verbs") and event["verb"] not in rule["verbs"]:
            continue
        if rule.get("namespaces") and event["namespace"] not in rule["namespaces"]:
            continue
        groups = rule.get("resources", [])
        if groups and not any(event["group"] == g.get("group", "") and
                              (not g.get("resources") or event["resource"] in g["resources"])
                              for g in groups):
            continue
        omitted = set(policy.get("omitStages", [])) | set(rule.get("omitStages", []))
        return "None" if event["stage"] in omitted else rule["level"]
    return "None"


def exercise():
    checks = []
    def check(label, condition):
        if not condition:
            raise AssertionError(label)
        checks.append(label)
    secret = {"group": "", "resource": "secrets", "namespace": "practice",
              "verb": "get", "stage": "ResponseComplete"}
    config = dict(secret, resource="configmaps", verb="update")
    check("Secret reads retain metadata", audit_level(POLICY, secret) == "Metadata")
    check("Secret lists also retain metadata", audit_level(POLICY, dict(secret, verb="list")) == "Metadata")
    check("selected ConfigMap writes include bodies", audit_level(POLICY, config) == "RequestResponse")
    check("read verb uses metadata fallback", audit_level(POLICY, dict(config, verb="get")) == "Metadata")
    check("different namespace uses metadata fallback", audit_level(POLICY, dict(config, namespace="other")) == "Metadata")
    check("different API group uses fallback", audit_level(POLICY, dict(config, group="example.invalid")) == "Metadata")
    check("global omitted stage suppresses event", audit_level(POLICY, dict(config, stage="RequestReceived")) == "None")
    check("rule omitted stage suppresses without fallthrough", audit_level(POLICY, dict(config, stage="ResponseStarted")) == "None")
    narrower = copy.deepcopy(POLICY)
    narrower["rules"] = narrower["rules"][:2]
    check("no matching rule means no event", audit_level(narrower, dict(config, resource="pods")) == "None")
    unsafe = copy.deepcopy(POLICY)
    unsafe["rules"].insert(0, {"level": "RequestResponse"})
    check("early broad rule defeats later Secret protection", audit_level(unsafe, secret) == "RequestResponse")
    reordered = copy.deepcopy(POLICY)
    reordered["rules"] = [reordered["rules"][-1], *reordered["rules"][:-1]]
    check("early metadata fallback hides intended detailed write", audit_level(reordered, config) == "Metadata")
    unsupported = copy.deepcopy(POLICY)
    unsupported["rules"][0]["users"] = ["example"]
    try:
        audit_level(unsupported, secret)
    except ValueError:
        check("unsupported user selector rejected explicitly", True)
    else:
        raise AssertionError("Unsupported selector was ignored")
    return {"passed": len(checks), "checks": checks,
            "boundary": "Restricted reasoning model: exact resource/group/namespace/verb matching and stage omission only; no API server audit event or backend emission tested."}


if __name__ == "__main__":
    print(exercise())
```

**Executed September 29:** 12 model checks passed. Moving a broad RequestResponse rule first defeats the later Secret-specific rule; moving Metadata first hides intended detailed writes. An omitted stage on the first matching rule suppresses the event rather than falling through. This exercise predicts policy decisions only. It did not emit an API audit record, test log rotation/webhooks, inspect real Secrets or prove an audit backend works. In the live lab, use synthetic data and check the emitted level, stage, identity, response status and absence of prohibited bodies.

## Integrated scenarios

### Scenario 1: Harden a new kubeadm cluster without losing recovery

Map API/kubelet/etcd/node/Pod/Ingress paths and preserve console, manifests and verified etcd/config backup. Run the matching CIS assessment and triage findings. Restrict firewall/API/kubelet, apply least-privilege RBAC/ServiceAccounts and default-deny policies, configure TLS Ingress, protect metadata and verify binaries. Change one control at a time, re-run the relevant check, and validate API, Nodes, DNS, workload traffic, audit and recovery. Record exceptions rather than blindly forcing every automated result.

### Scenario 2: Govern an application from source to runtime

Build a minimal non-root image from pinned dependencies, generate an SBOM, scan source/image/manifests, and publish a digest to an approved registry. Sign/attest it and configure admission to accept the correct identity/digest and reject an unsigned or disallowed artifact. Deploy under Restricted Pod Security, minimum ServiceAccount/RBAC, default-deny policy, Secret controls, read-only root, seccomp and mTLS. Prove function and negative controls, then rebuild/promote the same workflow after a new vulnerability finding.

### Scenario 3: Investigate suspicious activity safely

A runtime detector reports a shell/process and an unusual API access follows. Confirm sensor health and preserve the alert, Kubernetes audit event, Pod spec/image digest, current/previous logs, runtime processes, node/auth logs and network evidence. Build a time-normalized timeline, scope identity/workload/node impact, and contain through authorized network/identity/workload action. Rotate exposed credentials, replace from verified artifacts, correct admission/RBAC/runtime gaps, recover and watch for recurrence. Do not erase the only Pod before collecting volatile evidence.

## Hands-on labs

Use only disposable or explicitly authorized environments; snapshots and console access are strongly recommended. **All eight complete cluster labs remain proposed.** The local Docker Linux engine was unavailable and native Linux execution remains deferred. The separate local exercises executed 17 cryptographic/claim checks and 12 audit-model checks; they do not establish cluster enforcement.

1. **CIS-guided setup (3–5 hours):** run a matching benchmark, manually validate findings across API server/etcd/controller/scheduler/CoreDNS/kubelet, remediate selected safe items one at a time, and record pass/fail/not-applicable/exception evidence.
2. **Cluster access and segmentation (3–4 hours):** implement minimum RBAC/ServiceAccounts, disabled token automount where unused, API/kubelet/network exposure restrictions, default-deny policies, metadata protection and TLS Ingress. Prove allowed and denied paths, named read/list behavior and explicit webhook denial versus webhook-call failure.
3. **Host and kernel profiles (3–5 hours):** minimize services/ports/users on disposable nodes, apply runtime-default/custom seccomp and an AppArmor profile where supported, then test application success, denied action, node reboot and rescheduling coverage. Compare API creation with kubelet admission, explicit profiles with runtime defaults, and every eligible node.
4. **Restricted workload and Secrets (2–4 hours):** enforce/audit/warn current Pod Security Standards, configure restrictive security context, encryption-at-rest lab or documented KMS equivalent, minimum Secret RBAC and a full rotation with dependent rollout/revocation. Distinguish template warnings from Pod enforcement and new encrypted writes from migration of existing records.
5. **Isolation and mTLS (3–5 hours):** compare namespace-only, policy, sandbox RuntimeClass and dedicated placement boundaries. Configure Cilium- or Istio-style Pod-to-Pod encryption in a disposable environment and prove encrypted success plus unauthorized/plaintext failure as supported.
6. **Trusted supply chain (4–6 hours):** create a minimal image, SBOM, scans, digest, signature/attestation and approved-registry policy. Exercise signature, trusted identity, digest and policy accept/reject cases separately, then rebuild/redeploy the same source after changing a dependency or policy threshold.
7. **Audit and runtime response (3–5 hours):** enable a safe audit policy, deploy a runtime detector, generate authorized test events, correlate at least four sources, investigate/contain/recover, and measure whether alerts/logs survive restart and rotation. Prove rule order protects synthetic Secret bodies and check event-source coverage/output loss independently.
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
17. **Why must AppArmor profiles exist on every eligible node?** Kubelet can refuse to run a Pod whose explicitly requested profile is missing, even though the API object was created.
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
41. **Does Kubernetes v1.37 automatically become the CKS exam version?** No; use the live exam page and curriculum, and treat the 4–8-week policy only as a recheck window.
42. **What exactly did the ingress-nginx retirement remove?** One community controller's maintained releases, bug fixes and security fixes—not the stable Ingress API or the current CKS objective.

43. **Can a valid signature still fail deployment approval?** Yes; trusted signer, expected claims, matching artifact digest and release policy are separate checks.
44. **What if a broad RequestResponse audit rule comes before a Secret Metadata rule?** The first matching rule wins, so Secret request/response bodies may be logged.
45. **Does enabling at-rest encryption rewrite every existing Secret?** No; existing stored data must be migrated and verified before retiring old recovery keys.
46. **Can a Deployment exist in an enforcing namespace while its Pods are denied?** Yes; enforce acts on resulting Pods, while audit/warn also check workload templates.

## Places to learn

| Resource | Access | Estimated time |
|---|---|---:|
| [Official CKS page](https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/) and [CNCF CKS page](https://www.cncf.io/training/certification/cks/) | Public; exam paid | 3–5 hours mapping/discrepancy review, plus 8–14 selected simulator hours |
| [Public CNCF CKS v1.34 curriculum](https://github.com/cncf/curriculum/blob/master/CKS_Curriculum%20v1.34.pdf) | Public | 1–2 hours; actual outline and weights match the live v1.35 page despite the older filename |
| [Kubernetes v1.35 documentation](https://v1-35.docs.kubernetes.io/docs/home/) | Public | 20–35 selected security reading/lab hours; use as a reference |
| [Kubernetes v1.37 release](https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/) | Public release watch; use only to trigger the exam-version recheck | 20–40 minutes |
| [Ingress NGINX retirement notice](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/) | Public operational warning; distinguishes the controller from the Ingress API | 15–25 minutes |
| [Linux Foundation Kubernetes Security Essentials (LFS260)](https://training.linuxfoundation.org/training/kubernetes-security-essentials-lfs260/) | Paid | 26–30 listed course hours, nine chapters; Linux plus cloud/VirtualBox labs; add 35–70 independent lab hours |
| [Pluralsight CKS path](https://www.pluralsight.com/paths/certified-kubernetes-security-specialist-cks) | Subscription/trial | 12 listed hours, seven courses, three refreshed 2026 labs and practice exam; add 35–70 lab hours |
| [KodeKloud CKS](https://kodekloud.com/courses/certified-kubernetes-security-specialist-cks/) | Subscription/free preview | 8.75 listed video hours, eight modules/150 lessons; public history still says v1.33 in progress in May 2025; allow 30–55 hours with gap work |
| [O'Reilly Certified Kubernetes Security Specialist](https://www.oreilly.com/videos/certified-kubernetes-security/9780138296537/) | Subscription/trial | Earlier listing: 19 hours 38 minutes, February 2025; blocked now and not reverified; add 35–70 proposed lab hours |
| [Udemy Certified Kubernetes Security Specialist 2026](https://www.udemy.com/course/certified-kubernetes-security-specialist-certification/) | Paid; price varies | Earlier listing: 19 hours 58 minutes, July 2026 update; blocked now and not reverified; add independent labs |

Pluralsight mixes a 2022 introduction, 2025 courses and 2026 cluster courses/labs; a refreshed lab does not date every lesson. KodeKloud's public outline still lists optional Pod Security Policies and does not visibly name SBOM/signature lessons; check modern Pod Security Admission and supply-chain coverage against the official objectives. This does not establish what is inside paid lessons or the actual current lab runtime. LFS260 requires self-managed lab access and possible cloud charges. Public metadata only was reviewed; no paid lessons, mock questions or provider labs were accessed. Added independent study times are planning estimates.

This is not a complete list and is not meant to be consumed in full. Earn CKA first, choose one current structured security route, and use the live Linux Foundation v1.35 objectives as the source of truth while the CNCF overview weights remain inconsistent and the PDF retains its older filename. Build every control in disposable infrastructure and verify both legitimate behavior and denial/detection. Check tools and course examples for current Pod Security Standards, admission APIs, seccomp/AppArmor fields, signatures/provenance, runtime detection and the 15/15/10 weights. Avoid recalled tasks and question dumps; this is a defensive performance exam.
