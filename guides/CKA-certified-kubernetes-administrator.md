---
exam_code: CKA
vendor_id: linux-foundation
official_blueprint: https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# CKA Certified Kubernetes Administrator Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 29, 2026. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#cka-coverage-record). The [official CKA page](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/) is authoritative.

**Current baseline:** Kubernetes v1.35 and the five weighted domains on the live CKA page<br>
**Lifecycle watch:** Kubernetes [v1.37 was released August 26, 2026](https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/), but the official exam page still names v1.35 as of September 29. Linux Foundation says exam alignment follows a new minor release by approximately 4–8 weeks, so recheck between September 23 and October 21 and immediately before practice or scheduling; this is a watch window, not an announced exam-version date.<br>
**Official delivery snapshot:** Online, remotely proctored, performance-based command-line exam; two hours; certification valid for two years; 12-month eligibility, one retake, and two 36-hour Killer.sh simulator activations listed<br>
**Prerequisite:** No formal certification prerequisite; practical readiness requires Linux, networking, containers, YAML, and repeated Kubernetes administration under time pressure

## How to use this guide

CKA evaluates working cluster state, not command recall. Practice every task with this loop:

1. confirm the `kubectl` context, namespace, target resource, requested end state, and time budget;
2. inspect live objects, events, logs, nodes, components, endpoints, routes, policies, and storage before editing;
3. choose an imperative command for a safe simple action or a declarative manifest for reviewable state;
4. make the smallest supported change, preserving an easy rollback or backup for risky control-plane work;
5. verify the direct object plus readiness, traffic, persistence, security, restart, and dependent behavior.

Build disposable v1.35 clusters with `kubeadm`, `kind`, or another conformant lab. Use the [versioned Kubernetes v1.35 documentation](https://v1-35.docs.kubernetes.io/docs/home/) while learning, then check the current exam-documentation policy in the official candidate resources. Type and explain commands; do not paste unknown snippets. Time mixed task sets only after you can diagnose them untimed. Never reproduce proprietary simulator tasks or recalled exam material.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Weighted objective map

| Domain | Weight | Performance evidence |
|---|---:|---|
| 1. Cluster architecture, installation and configuration | 25% | Govern access; build, upgrade and recover kubeadm/HA clusters; install extensions, packages and operators |
| 2. Workloads and scheduling | 15% | Configure, place, scale, update, roll back and self-heal workloads |
| 3. Services and networking | 20% | Trace Pod traffic; configure Services, policies, DNS, Ingress and Gateway API routes |
| 4. Storage | 10% | Match StorageClasses, provisioning, volumes, access modes, reclaim policy, PVs and PVCs |
| 5. Troubleshooting | 30% | Localize and repair node, component, resource, stream, Service and network failures |

## 1. Cluster architecture, installation and configuration — 25%

### Architecture, interfaces and API resources

The API server is the front door to desired and observed cluster state. etcd stores that state; the scheduler binds unscheduled Pods to feasible nodes; controllers reconcile actual state toward declared state. On workers, kubelet reconciles Pod specifications through the Container Runtime Interface (CRI), while a network implementation satisfies the Container Network Interface (CNI). Storage drivers use the Container Storage Interface (CSI). Learn ownership: changing a Deployment-managed Pod is temporary; changing the Deployment template changes the controller's desired state.

Use discovery before assumptions: `kubectl api-resources`, `api-versions`, `explain`, `get -o yaml`, labels, owner references, finalizers, conditions, events, and relevant node/control-plane files. Namespaced and cluster-scoped resources have different boundaries. A CustomResourceDefinition extends the API schema; a custom resource is an instance; an operator adds a controller that reconciles those resources. Inspect CRD versions, scope, schema, status, controller deployment, RBAC, logs and events before deciding that an operator is healthy.

CRI, CNI and CSI are contracts, not interchangeable products. Diagnose at the boundary: kubelet-to-runtime for image/container/sandbox failures, runtime-to-CNI for Pod network setup, and workload-to-CSI/storage backend for mount or attach failures. A healthy API object does not prove its provider-side dependency is healthy.

> **Related item:** Reconciliation explains much of Kubernetes administration: identify the resource that owns desired state, change that owner, and observe its controller converge instead of repeatedly patching symptoms.

### RBAC and administrative access

Authentication establishes identity; authorization decides whether the identity may perform a verb on a resource; admission can accept, reject, or mutate a request. RBAC combines Role/ClusterRole rules with RoleBinding/ClusterRoleBinding subjects. `Role` is namespaced; `ClusterRole` can express cluster-scoped rules and can also be bound into one namespace. A binding grants rules—it does not copy or edit the referenced role.

Use `kubectl auth can-i --as ... --namespace ...`, SelfSubject-style checks, and actual positive/negative operations. Grant exact API groups, resources, subresources, verbs, resource names, and namespaces. Avoid wildcard escalation. Remember that reading Secrets, creating Pods with powerful service accounts, creating role bindings, or accessing node/proxy-like subresources can create indirect privilege.

Kubeconfig holds clusters, users/credentials, contexts, and current context. Validate server, CA/trust, identity, context and namespace separately. Protect client keys and bearer tokens. ServiceAccount identity is for workloads; bind only what the workload needs and understand projected, time-limited tokens rather than assuming a permanent Secret token.

**PRACTICAL DEPTH — binding scope:** RBAC grants are additive; a second restrictive Role does not deny an existing grant. A RoleBinding to a ClusterRole grants its applicable namespaced permissions only in the binding namespace; it cannot grant cluster-scoped access. `roleRef` is immutable, so changing the referenced role requires replacement (or a suitable reconciliation operation), not an ordinary in-place edit. Test another namespace and a forbidden verb as well as the intended operation. See [the v1.35 RBAC source](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/reference/access-authn-authz/rbac.md).

### Prepare and create kubeadm clusters

Prepare compatible Linux hosts: unique identity, supported kernel/network settings, time, resolvable addresses, disabled or correctly handled swap according to the selected Kubernetes/kubelet configuration, a CRI-compatible runtime, correct cgroup-driver alignment, required ports, trusted repositories/packages, and stable networking. Pin and record component versions. `kubeadm init` bootstraps a control plane; copy the generated kubeconfig for the intended administrator, install exactly one compatible CNI, and use the generated join data to add nodes. Validate Nodes, system Pods, CoreDNS, routes, taints, runtime, and a cross-node application—not just `Ready`.

Static control-plane Pods are defined by manifests watched by kubelet. Their logs may require `crictl` when the API is unavailable. Certificates, kubeconfigs, manifests, etcd data, runtime state and kubelet configuration have distinct locations and owners. Know where to look without changing all of them at once.

For high availability, separate the stable API endpoint/load balancer from control-plane nodes, use multiple control-plane/etcd members as designed, distribute failure domains, and test quorum-aware recovery. A load balancer that returns TCP success can still route to an unhealthy API server. Preserve etcd quorum; do not casually restore one member into a live inconsistent cluster.

> **Related item:** Availability is end-to-end: client DNS and load-balancer health, API servers, etcd quorum, controllers/scheduler, worker capacity, networking, DNS and storage all contribute different failure modes.

### Lifecycle, backup and upgrade

Inventory server/client/node versions, repositories, skew rules, add-ons, APIs, CRDs, webhooks, PDBs and capacity. Back up etcd with the correct endpoint, CA, certificate and key; verify snapshot status and protect the file. Also preserve external configuration, certificates, manifests, encryption configuration and application data as required—an etcd snapshot is not every backup.

For a kubeadm upgrade, read the exact target-version instructions. Skipping minor versions with kubeadm is unsupported; start with a control-plane node, then additional control planes and workers. Cordon and drain with awareness of DaemonSets, local data, disruption budgets and replacement capacity. Upgrade kubeadm, run plan/apply or node phase as appropriate, then kubelet/kubectl; restart and verify components, Nodes, workloads, traffic and storage before continuing. Uncordon only after evidence is good.

Restore is a controlled state replacement: stop or isolate affected components, validate snapshot, restore to the intended data directory/configuration, update static Pod or service ownership if needed, restart, and validate members, API state and applications. Practice failed and successful restores on disposable clusters.

**VERIFY CURRENT — component compatibility:** [Version skew](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/releases/version-skew-policy.md) allows kubectl one minor older or newer than the API server; mixed-version HA API servers narrow that intersection. A kubelet must not be newer than its API server and, for modern releases, may be up to three minors older within the documented policy. This does not authorize skipping kubeadm upgrade steps or ignoring add-on compatibility. The [kubeadm upgrade procedure](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade.md) requires draining before a minor kubelet upgrade, including control-plane hosts that run critical workloads.

**PRACTICAL DEPTH — recovery revisions:** Restoring old etcd data can move revisions behind what Kubernetes clients previously observed. The [etcd 3.6 recovery documentation](https://raw.githubusercontent.com/etcd-io/website/main/content/en/docs/v3.6/op-guide/recovery.md) recommends revision bumping with marking compacted for Kubernetes watch/cache recovery. Select flags and a sufficient revision increment from the installed etcd version and recovery plan; do not copy a large example constant as a universal answer. A restored cluster has new logical identities and must be recovered consistently. This reference does not establish which etcd version an exam cluster uses; no restore was executed here.

### Helm, Kustomize and operators

Helm renders and tracks chart releases. Inspect values and templates, install into the intended namespace, verify hooks/resources, upgrade with known values, inspect history and roll back deliberately. A release success does not prove workload readiness. Treat charts as code and inspect security-sensitive RBAC, webhooks, CRDs, images and host access.

Kustomize composes bases and overlays without a templating language. Use resources, patches, name/label transformers, images, ConfigMap/Secret generators and `kubectl kustomize`/`apply -k`; preview output and understand hash-suffixed generated names. Keep environment differences in overlays instead of copying whole manifests.

When installing an operator, separate CRDs, controller, webhooks, RBAC and custom resources. Verify controller readiness, leader election where used, admission reachability, reconciliation status and cleanup/finalizers. Version compatibility matters across Kubernetes, the operator and managed application.

### Offline exercise: render, inspect, break and repair

This original Python exercise uses PyYAML and an explicitly selected kubectl executable. Save it as `cka_render_practice.py` and run `python cka_render_practice.py /path/to/kubectl` (on Windows, quote the full executable path). It creates temporary base/overlay files, uses client-side Deployment generation, renders Kustomize locally, then removes its files. The namespace is a rendered field; no namespace is created. The intentionally nonexistent image is never pulled. It isolates kubeconfig from your normal contexts and makes no API request.

Predict the three output kinds, replica counts, image, selector and generated ConfigMap reference before running. Changing generator content changes the hash-suffixed ConfigMap name and Pod-template reference. A missing file, duplicate resource and invalid patch fail rendering; a wrong Service selector still renders. That last case explains why rendering success cannot establish Service traffic. See [the v1.35 Kustomize source](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/tasks/manage-kubernetes-objects/kustomization.md).

```python
"""Offline CKA rendering exercise. Requires Python, PyYAML and a kubectl path."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import yaml


def exercise(kubectl, parent=None):
    checks = []
    def check(label, condition):
        if not condition:
            raise AssertionError(label)
        checks.append(label)

    with tempfile.TemporaryDirectory(prefix="cka-render-", dir=parent) as temporary:
        root = Path(temporary)
        base = root / "base"
        overlay = root / "practice"
        base.mkdir()
        overlay.mkdir()
        kubeconfig = root / "empty-kubeconfig.yaml"
        kubeconfig.write_text("apiVersion: v1\nkind: Config\nclusters: []\nusers: []\ncontexts: []\ncurrent-context: ''\n", encoding="utf-8")
        env = dict(os.environ, KUBECONFIG=str(kubeconfig))
        def run(*args, success=True):
            result = subprocess.run([str(kubectl), *args], env=env,
                                    capture_output=True, text=True, timeout=20)
            if success and result.returncode:
                raise RuntimeError(result.stderr)
            return result

        version = json.loads(run("version", "--client", "-o", "json").stdout)
        deployment = yaml.safe_load(run("create", "deployment", "catalog",
            "--image=example.invalid/catalog:v1", "--replicas=2",
            "--dry-run=client", "-o", "yaml").stdout)
        deployment.pop("status", None)
        deployment["metadata"].pop("creationTimestamp", None)
        deployment["spec"]["template"]["metadata"].pop("creationTimestamp", None)
        container = deployment["spec"]["template"]["spec"]["containers"][0]
        container["envFrom"] = [{"configMapRef": {"name": "catalog-settings"}}]
        container["ports"] = [{"name": "http", "containerPort": 8080}]
        container["resources"] = {"requests": {"cpu": "100m", "memory": "64Mi"}}
        service = {"apiVersion": "v1", "kind": "Service", "metadata": {"name": "catalog"},
                   "spec": {"selector": {"app": "catalog"},
                            "ports": [{"port": 80, "targetPort": "http"}]}}
        (base / "objects.yaml").write_text(yaml.safe_dump_all([deployment, service]), encoding="utf-8")
        (base / "settings.env").write_text("MODE=training\n", encoding="utf-8")
        config = {"apiVersion": "kustomize.config.k8s.io/v1beta1", "kind": "Kustomization",
                  "resources": ["objects.yaml"],
                  "configMapGenerator": [{"name": "catalog-settings", "envs": ["settings.env"]}]}
        (base / "kustomization.yaml").write_text(yaml.safe_dump(config), encoding="utf-8")
        practice = {"apiVersion": config["apiVersion"], "kind": "Kustomization",
                    "resources": ["../base"], "namespace": "cka-practice", "namePrefix": "lab-",
                    "replicas": [{"name": "catalog", "count": 3}],
                    "images": [{"name": "example.invalid/catalog", "newTag": "v2"}]}
        overlay_file = overlay / "kustomization.yaml"
        def save_overlay():
            overlay_file.write_text(yaml.safe_dump(practice), encoding="utf-8")
        def render(path):
            return list(yaml.safe_load_all(run("kustomize", str(path)).stdout))
        def objects(items):
            return {item["kind"]: item for item in items}
        save_overlay()
        initial = objects(render(base))
        rendered = objects(render(overlay))
        check("three rendered kinds", set(rendered) == {"Deployment", "Service", "ConfigMap"})
        check("base retains two replicas", initial["Deployment"]["spec"]["replicas"] == 2)
        check("overlay has three replicas", rendered["Deployment"]["spec"]["replicas"] == 3)
        check("namespace applied to every object", all(o["metadata"]["namespace"] == "cka-practice" for o in rendered.values()))
        check("name prefix applied", all(o["metadata"]["name"].startswith("lab-") for o in rendered.values()))
        pod = rendered["Deployment"]["spec"]["template"]
        check("image tag transformed", pod["spec"]["containers"][0]["image"] == "example.invalid/catalog:v2")
        check("service selector matches pod labels", all(pod["metadata"]["labels"].get(k) == v for k, v in rendered["Service"]["spec"]["selector"].items()))
        check("named target port resolves in manifest", rendered["Service"]["spec"]["ports"][0]["targetPort"] == pod["spec"]["containers"][0]["ports"][0]["name"])
        config_name = rendered["ConfigMap"]["metadata"]["name"]
        check("config generator adds suffix", config_name.startswith("lab-catalog-settings-") and config_name != "lab-catalog-settings-")
        check("config reference rewritten", pod["spec"]["containers"][0]["envFrom"][0]["configMapRef"]["name"] == config_name)
        check("initial configuration value", rendered["ConfigMap"]["data"]["MODE"] == "training")
        check("repeat render stable", objects(render(overlay)) == rendered)
        (base / "settings.env").write_text("MODE=diagnostic\n", encoding="utf-8")
        changed = objects(render(overlay))
        new_name = changed["ConfigMap"]["metadata"]["name"]
        new_pod = changed["Deployment"]["spec"]["template"]
        check("content change changes config name", new_name != config_name)
        check("new reference follows content change", new_pod["spec"]["containers"][0]["envFrom"][0]["configMapRef"]["name"] == new_name)
        check("pod template changes", new_pod != pod)
        check("base image stays unchanged", objects(render(base))["Deployment"]["spec"]["template"]["spec"]["containers"][0]["image"] == "example.invalid/catalog:v1")
        practice["resources"].append("missing.yaml")
        save_overlay()
        rejected = run("kustomize", str(overlay), success=False)
        check("missing resource rejected", rejected.returncode != 0 and "missing.yaml" in rejected.stderr)
        practice["resources"].pop()
        practice["resources"].append("../base")
        save_overlay()
        rejected = run("kustomize", str(overlay), success=False)
        check("duplicate resources rejected", rejected.returncode != 0 and "already registered id" in rejected.stderr)
        practice["resources"].pop()
        practice["patches"] = [{"target": {"kind": "Deployment", "name": "catalog"},
                               "patch": '- op: replace\n  path: /spec/missing/value\n  value: bad\n'}]
        save_overlay()
        rejected = run("kustomize", str(overlay), success=False)
        check("invalid patch path rejected", rejected.returncode != 0 and "missing" in rejected.stderr)
        practice.pop("patches")
        save_overlay()
        check("repair restores expected output", objects(render(overlay)) == changed)
        # Rendering permits mistakes that only later validation/behavior can expose.
        service["spec"]["selector"] = {"app": "wrong"}
        (base / "objects.yaml").write_text(yaml.safe_dump_all([deployment, service]), encoding="utf-8")
        broken = objects(render(overlay))
        check("rendering alone does not reject wrong selector", broken["Service"]["spec"]["selector"] != broken["Deployment"]["spec"]["template"]["metadata"]["labels"])
        result = {"passed": len(checks), "checks": checks, "client_version": version,
                  "boundary": "Client generation and local rendering only; no API requests, image pulls, admission, Pods, CNI, CSI, controllers or live traffic validated."}
    check("owned temporary files removed", not root.exists())
    result.update(passed=len(checks), checks=checks, cleanup_verified=True)
    return result


if __name__ == "__main__":
    print(json.dumps(exercise(Path(sys.argv[1]).resolve()), indent=2))
```

**Executed September 29:** 22 checks passed using checksum-verified Windows kubectl **v1.35.9** and its bundled Kustomize **v5.7.1**, with cleanup verified. The [official installation instructions](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/tasks/tools/install-kubectl-windows.md) explain binary checksum and client-version verification. This validates client generation/rendering and the listed negative cases. It does not test an API server, CRDs, admission, controller reconciliation, Pods, CNI, CSI, DNS or traffic.

For a later authorized cluster lab, [server dry-run](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/reference/using-api/api-concepts.md) adds server validation, defaulting, authorization and compatible admission processing without persisting the change. It requires the same authorization as a real request. Even server dry-run does not schedule a Pod, pull its image or prove readiness; complete the appropriate live lab and traffic checks.

## 2. Workloads and scheduling — 15%

### Controllers, configuration and self-healing

A Pod is the scheduling unit and shares network/storage namespaces among its containers. Prefer controllers: Deployment for replaceable stateless replicas and rolling releases; StatefulSet for stable identity/ordered behavior and per-Pod claims; DaemonSet for node-local agents; Job/CronJob for completion-oriented work. Inspect selectors and Pod-template labels carefully—immutable or mismatched selectors can orphan or misroute workloads.

ConfigMaps hold non-secret configuration; Secrets are encoded API objects, not encrypted merely because values are base64. Consume configuration as environment variables, arguments or mounted files, and know refresh semantics. Protect Secret access with RBAC and encryption-at-rest/secret-management controls outside this objective when required. Changing a ConfigMap does not guarantee an application reload; roll or signal the workload according to application behavior.

Readiness normally controls whether a Pod is eligible for Service traffic; liveness triggers container restart; startup prevents premature liveness/readiness evaluation during initialization. Set probes against meaningful behavior and choose delay, period, timeout, thresholds and endpoints deliberately. A liveness probe that depends on a remote downstream can amplify an outage.

Requests influence scheduling and are the denominator for utilization-based autoscaling; limits constrain runtime resources. CPU throttling and memory OOM behavior differ. Inspect Pod QoS, node allocatable state, usage and eviction signals. Horizontal Pod Autoscaler needs a usable metric path and scalable workload; increasing replicas cannot fix a shared dependency or no remaining capacity.

**Configuration refresh:** A mounted ConfigMap projection updates eventually, subject to kubelet synchronization and cache propagation; the application must still reload the changed file. Environment variables require a Pod restart to change, and a ConfigMap mounted with `subPath` does not receive these updates. Compare the API value, mounted bytes and effective application setting separately. See [v1.35 ConfigMap behavior](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/concepts/configuration/configmap.md).

**Autoscaling reasoning:** For four replicas averaging 75% CPU utilization against a 60% target, the basic ratio gives `ceil(4 × 75 / 60) = 5`. Utilization uses requests, not CPU limits. This is a first estimate: missing metrics, readiness, tolerance, bounds, stabilization and scaling policies can change the action. If a second metric cannot be fetched, an otherwise suggested scale-down is skipped; a valid metric can still justify scale-up. Inspect metric availability and HPA conditions before changing capacity. See [the v1.35 HPA algorithm](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale.md).

### Updates, rollback, admission and placement

For rolling updates, understand desired/current/available replicas, `maxSurge`, `maxUnavailable`, readiness, progress deadline, revision history and image pull behavior. Watch rollout, inspect the ReplicaSets and Pods, test traffic, and use rollback only after understanding configuration/data compatibility. A rollback of a Deployment does not roll back a database schema or external dependency.

Scheduling filters and scores feasible nodes. Use node selectors/affinity for placement, anti-affinity or topology spread for distribution, taints to repel and tolerations to permit, resource requests for capacity, and Pod affinity/anti-affinity for co-location/separation. Toleration does not force placement; affinity can. Hard requirements can leave Pods Pending; soft preferences allow degraded placement.

Admission occurs after authentication/authorization and before persistence. Built-in admission, policy/webhook controls, quotas and limit ranges can reject or mutate a Pod even when RBAC allows creation. Use Events and the API error. For a webhook problem, inspect service/endpoints/TLS/CA bundle, failure policy, match rules and controller availability before disabling policy.

> **Related item:** Desired replicas, schedulability, startup, readiness, Service endpoint membership and real user success are separate gates. Verify each one instead of using `Running` as a health verdict.

**Rollout versus maintenance budgets:** With seven desired replicas, `maxUnavailable: 30%` permits `floor(2.1) = 2` unavailable during a Deployment rollout, while `maxSurge: 30%` permits `ceil(2.1) = 3` extra. Terminating Pods can still consume resources beyond the apparent desired-plus-surge allowance until their grace period ends. Check capacity for termination overlap. See [Deployment rollout behavior](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/concepts/workloads/controllers/deployment.md).

A PDB protects against cooperating voluntary eviction, such as drain through the Eviction API. It does not constrain a Deployment/StatefulSet rolling update, prevent node failure, or protect against direct Pod deletion. Unavailable rollout Pods still count against its budget. Unlike Deployment `maxUnavailable`, both PDB percentage fields round up: seven replicas and `maxUnavailable: 30%` allow three unavailable. Check current health and `disruptionsAllowed`; do not use that number as a universal permission to kill Pods. The default unhealthy-Pod eviction policy can block a drain; evaluate `AlwaysAllow` against the recovery requirements. Sources: [disruption boundaries](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/concepts/workloads/pods/disruptions.md) and [PDB rounding and eviction policy](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/tasks/run-application/configure-pdb.md).

## 3. Services and networking — 20%

### Packet path, Services and endpoints

Each Pod receives an address; Pods should communicate without address translation inside the cluster model, while the CNI implements routing/encapsulation and NetworkPolicy enforcement capabilities. Trace a request in order: client name resolution → Service virtual name/IP/port → EndpointSlice-selected ready backend → Pod IP/targetPort → listener/process → response and return path. Compare this with direct Pod-IP and local-container tests.

Service selectors build EndpointSlices from matching Pods. Confirm labels, namespace, readiness and port name/number/protocol. `ClusterIP` is internal virtual access; `NodePort` exposes a port on nodes; `LoadBalancer` asks an integration to provision external access. Headless Services omit the virtual IP for discovery use cases. `externalTrafficPolicy`, session affinity, health checks and provider implementations affect path and source-IP behavior; do not assume cloud-specific behavior on a vendor-neutral exam.

Use `kubectl get svc,endpointslices,pods -o wide`, DNS queries from a disposable Pod, `curl`/`wget`/`nc` where installed, `ss` inside the relevant container/node, and CNI/kube-proxy or replacement data-plane evidence. Avoid random restarts before locating the failed boundary.

### NetworkPolicy, DNS, Ingress and Gateway API

NetworkPolicy selects Pods and defines allowed ingress/egress by peers and ports. Once a Pod is selected for a direction, traffic in that direction is restricted to the union of allowed rules; policies are additive. Both source egress and destination ingress may need to allow a connection. Empty selectors, namespaces, IP blocks, DNS egress and plugin support are common traps. Test an allowed and denied path from realistic identities.

CoreDNS normally serves cluster names through a Service. Diagnose Pod resolver configuration, search domains/`ndots`, CoreDNS Pods, Service and EndpointSlice, ConfigMap, logs, upstream reachability and NetworkPolicy. Directly querying CoreDNS separates name-service reachability from search-name behavior. DNS failure can look like application or Service failure.

Ingress resources require an Ingress controller; the resource alone does nothing. Match controller class, host/path/path type, backend Service/port, controller logs, address and TLS Secret. Gateway API separates infrastructure and route concerns through GatewayClass, Gateway, listeners and route resources such as HTTPRoute. Inspect `Accepted`, `Programmed`, `ResolvedRefs` and parent status; verify allowed route attachment and cross-namespace references. The official v1.35 CKA objectives explicitly include both Ingress and Gateway API, so practice both rather than treating one as a synonym for the other.

Do not confuse the stable Kubernetes Ingress API with one implementation. The Kubernetes project [retired the community ingress-nginx controller in March 2026](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/), ending releases, bug fixes, and security updates for that controller; the Ingress API itself and the exam objective were not retired. In a provided exam environment, use the installed controller and stated task contract. For production design, inventory controller ownership and version, migrate to a maintained implementation, validate class/annotations/TLS/traffic, and keep rollback rather than deleting Ingress resources by assumption.

> **Related item:** Network objects express intent, while CNI, Service data plane, DNS, ingress/gateway controller and external load balancer implement different segments. Healthy YAML cannot substitute for segment-by-segment traffic evidence.

**PRACTICAL DEPTH — read EndpointSlice conditions:** A selector-based Service can have a Slice containing unready Pod addresses. Inspect each endpoint's `ready`, `serving` and `terminating`, not just whether an address exists. Normally `ready` means serving and not terminating; `publishNotReadyAddresses` changes this interpretation. Some proxies may use serving-but-terminating endpoints if all available endpoints are terminating. An empty set and a populated set with no usable backends need different investigations. See [v1.35 EndpointSlice conditions](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/concepts/services-networking/endpoint-slices.md).

**Policy indentation changes permission:** For a policy in namespace `shop`, one peer containing both `namespaceSelector: team=blue` and `podSelector: role=client` means client Pods in blue-team namespaces. Two separate peers mean all Pods in blue-team namespaces **or** client Pods in `shop`. A pod selector without a namespace selector is local to the policy namespace. Other policies can add permissions, and an isolated source's egress plus an isolated destination's ingress must both permit the connection. Prove rejected paths as well as allowed paths using a policy-capable plugin. See [NetworkPolicy selector semantics](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/concepts/services-networking/network-policies.md).

**Two cross-namespace Gateway checks:** A Route in `shop` attaching to a Gateway in `infra` needs its parent reference and the listener's permitted route kinds/namespaces to agree. A Route forwarding to a Service in `payments` has a different boundary: a ReferenceGrant in the backend's namespace authorizes that cross-namespace reference. One does not substitute for the other. Match the API versions and features supported by the installed Gateway API CRDs/controller, then check attachment, references and real traffic. Sources: [route attachment](https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/main/site/content/en/guides/user-guides/multiple-ns.md) and [ReferenceGrant](https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/main/site/content/en/reference/api-types/referencegrant.md).

## 4. Storage — 10%

### Volumes, PVs, PVCs and dynamic provisioning

An ephemeral Pod volume follows the Pod; persistent storage is modeled through PersistentVolume (supply), PersistentVolumeClaim (request), StorageClass (provisioning policy) and CSI/backend implementation. A workload mounts a claim, not an arbitrary StorageClass. Trace claim phase, selected class, requested capacity/access mode/volume mode, binding, provisioner events, PV claim reference, CSI controller/node behavior, attachment, mount and application permissions.

Access modes express capabilities used for matching and attachment; they do not automatically provide application-level locking. Filesystem versus block volume modes change consumption. StorageClass fields can include provisioner, parameters, reclaim policy, volume binding mode and expansion. `WaitForFirstConsumer` lets topology-aware provisioning consider the scheduled Pod; immediate provisioning may select topology before placement. A default class is an admission convenience, not a universal backend guarantee.

Reclaim policy governs what happens to dynamically provisioned or released backing storage after claim deletion: delete or retain requires different recovery/cleanup. Deleting a PVC can be destructive. Understand finalizers, protection, StatefulSet claim retention behavior, snapshots/backups, and application-consistent recovery. A PV in `Released` is not automatically safe to rebind without handling data and claim-reference state.

For Pending claims, compare requested attributes with available PVs/classes and provisioner logs/events. For mount failures, inspect node/plugin registration, topology, access conflict, device/filesystem, credentials, permissions/security context and backend health. Validate with a write/read, Pod recreation and—when the design permits—rescheduling to another node.

> **Related item:** Kubernetes persistence protects attachment to storage, not automatically the correctness, backup, replication, transaction consistency or disaster recovery of data inside it.

**Access and binding traps:** `ReadWriteOnce` is a single-node mode and can permit multiple Pods on that node. `ReadWriteOncePod` constrains access to one Pod cluster-wide and requires compatible CSI support. Neither an RWO assumption nor an access-mode label substitutes for application consistency or read-only enforcement. See [PV access-mode semantics](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/concepts/storage/persistent-volumes.md).

With a compatible `WaitForFirstConsumer` StorageClass, a Pending PVC can be expected until there is a schedulable consumer. Setting a Pod's `nodeName` bypasses the scheduler and can leave this delayed-binding claim Pending; use the appropriate scheduling constraints instead. Dynamically provisioned PVs inherit their class's reclaim policy, whereas manually created PVs keep their own configured policy. Check the actual PV before deleting a disposable claim. See [StorageClass binding and reclaim behavior](https://raw.githubusercontent.com/kubernetes/website/release-1.35/content/en/docs/concepts/storage/storage-classes.md).

## 5. Troubleshooting — 30%

### A disciplined evidence ladder

Start broad, then narrow without destroying evidence:

1. scope: one request, Pod, node, namespace, application or whole cluster;
2. recent change: image, manifest, policy, certificate, version, node, CNI/CSI, DNS or external dependency;
3. API state: desired versus current, conditions, Events, owner and generation;
4. workload: scheduling, init, image pull, container state/restarts, probes, logs and previous logs;
5. service path: listener, selector, endpoint, DNS, policy, route/controller and return path;
6. node/component: pressure, kubelet, runtime, certificates, static Pods, API/etcd/controllers/scheduler, CNI and CSI;
7. fix the controlling cause, then verify direct behavior, dependent behavior, restart/reschedule and monitoring.

Use `kubectl get/describe/logs --previous/events/top`, JSONPath or custom columns, `auth can-i`, `rollout`, `debug` where supported, and node tools such as `systemctl`, `journalctl`, `crictl`, `ss`, `ip`, `df`, `mount`, `free` and certificate inspection. `kubectl top` depends on metrics availability. Container stdout/stderr is a stream; central retention and correlation are separate system concerns.

### Workload and scheduling failures

`Pending` suggests scheduling, admission, PVC or image-related setup evidence; read conditions and Events. `ImagePullBackOff` requires image name/tag/digest, registry reachability, credentials, policy and runtime evidence. `CrashLoopBackOff` is a restart delay, not a cause—inspect current/previous logs, command/args, configuration, mounts, permissions, dependencies and exit code. `CreateContainerConfigError`, init-container failures, OOM kills and probe failures each point to different boundaries.

For a stalled rollout, compare Deployment/ReplicaSet generations, new Pod states, readiness, capacity, quotas, selectors, image and application compatibility. Pause destructive actions; a rollout restart may hide the first failure and does not correct bad desired state.

### Node and control-plane failures

A NotReady node requires conditions, taints, leases/heartbeats, capacity/pressure and kubelet/runtime/network evidence. Check time, disk/inodes, memory, PID pressure, certificates, kubelet configuration and dependencies. Drain before planned maintenance when capacity and disruption rules allow; distinguish cordon, drain and deletion.

If the API is unavailable, move below `kubectl`: endpoint/load balancer, host reachability, static Pod manifests, kubelet, runtime containers/logs, certificates, ports and etcd health/quorum. A malformed manifest can cause kubelet to repeatedly recreate a broken component. Back up before editing control-plane state. If scheduler/controller manager fail while API/etcd work, existing workloads may run while new scheduling or reconciliation stalls; inspect their static Pods, flags, kubeconfigs, leader election and logs.

### Service and storage failures

For a Service failure, compare direct local process, Pod IP, EndpointSlice, Service name/IP, then ingress/gateway/external route. For empty EndpointSlices, check namespace, selector/labels and Pod existence; for listed addresses, inspect readiness/serving/termination conditions; connection refused differs from timeout; DNS `NXDOMAIN` differs from no DNS response. Evaluate NetworkPolicy in both directions and remember external/provider behavior is implementation-specific.

For storage, distinguish PVC Pending, attachment failure, mount failure, permission failure, full/read-only filesystem and application consistency. Events often name the CSI stage. Protect data before delete/recreate experiments and confirm reclaim behavior. A replacement Pod on the same node is not proof of cross-node recoverability.

> **Related item:** Fast troubleshooting is not fast guessing. A short, repeatable evidence ladder reduces changes, preserves the original signal and makes verification part of the repair.

## Integrated scenarios

### Scenario 1: A release is healthy by replica count but users receive errors

The Deployment shows desired replicas, but the Gateway route intermittently returns 503. Confirm context/namespace and reproduce. Inspect rollout generation, Pod readiness/restarts/logs, Service selector and EndpointSlices. If only old Pods are usable backends, compare new labels and endpoint readiness/serving/termination conditions. If endpoints are healthy, inspect HTTPRoute parent status, backend references, Gateway/controller logs and policies. Correct the owner—template labels/probe/route—not an individual Pod. Verify direct Pod, Service DNS, Service IP and Gateway path, then roll another replica and confirm monitoring.

### Scenario 2: Upgrade one control plane without losing service

Inventory versions/skew, HA endpoint, etcd members/health, add-ons and deprecated APIs. Take and verify an etcd snapshot plus required configuration backups. Confirm workload capacity and disruption constraints. Upgrade kubeadm and run the supported plan/apply sequence on one control plane; then kubelet/kubectl and service restart. Validate API, etcd, controllers, scheduler, Nodes, DNS, workloads, traffic and storage before the next node. Record rollback/recovery triggers; never improvise an unsupported downgrade into a live quorum.

### Scenario 3: A stateful workload cannot recover on a replacement node

Inspect Pod scheduling Events, PVC/PV/StorageClass, access/volume modes, topology, attachment and CSI controller/node logs. Determine whether the old attachment, node affinity, missing plugin, permissions or backend causes the failure. Protect data; do not delete the claim blindly. Apply the smallest safe fix, wait for attach/mount, validate application data, restart the Pod and test another supported reschedule. Confirm backup and reclaim policy separately from restored availability.

## Hands-on labs

Use disposable infrastructure and only systems you own or are authorized to change. **All eight complete cluster labs below remain proposed:** Docker's Linux-engine endpoint was unavailable during this review, and native Linux runtime validation is deferred. Only the separate offline rendering exercise was executed.

1. **Build and prove a kubeadm cluster (3–5 hours):** create a control plane and worker with v1.35-compatible components, CRI and CNI. Capture component ownership, join evidence, cross-node traffic and DNS. Reboot both nodes and validate again.
2. **RBAC and operator boundary (2–3 hours):** create a namespaced service account with minimum read/write scope, prove allowed/denied operations, then install a small operator/CRD in a lab. Trace CR to controller, status, RBAC, events and finalizer cleanup. Prove that the namespaced binding grants no access in a second namespace and that an additional restrictive role cannot negate an existing grant.
3. **Safe lifecycle rehearsal (3–5 hours):** take/verify etcd backup, cordon/drain, perform a supported single-minor kubeadm upgrade in a disposable cluster, validate every component, and restore a separate clone from snapshot. Record quorum, revision/cache recovery and application-data evidence; demonstrate a budget-blocked drain without bypassing it.
4. **Release and scheduling matrix (2–3 hours):** deploy an app with requests/limits, three probes, ConfigMap/Secret, affinity, taint/toleration, topology spread and HPA. Cause Pending, failed readiness and bad rollout states; repair and roll back. Compare projected-file, environment and subPath configuration refresh. Explain the seven-replica rollout/PDB rounding difference with observed status.
5. **Service path and policy (2–4 hours):** trace Pod → EndpointSlice → ClusterIP → DNS. Add default-deny and explicit ingress/egress including DNS. Prove allowed and denied paths, then expose the app through Ingress and Gateway API/HTTPRoute. Contrast same-peer AND with separate-peer OR selectors, inspect unready EndpointSlice entries, and independently break/repair route attachment and backend-reference permission.
6. **Storage lifecycle (2–3 hours):** compare immediate and delayed binding where supported; create claims with different modes/policies, mount/write/recreate/reschedule, expand if supported, and observe retain/delete behavior using nonvaluable data. Contrast RWO with supported RWOP and diagnose a delayed-binding claim whose consumer bypasses the scheduler.
7. **Mixed break/fix (3–5 hours):** seed at least eight faults across labels, probes, image, quota, scheduler constraint, CoreDNS/Service, kubelet/runtime and CSI/mount. Diagnose using a fixed evidence ladder and keep a cause/evidence/fix/verification log.
8. **Two-hour rehearsal (2.5–3 hours each):** assemble original tasks covering all domains in official proportions. Use a fresh cluster, track skips/returns, validate every result, and spend the final 10–15 minutes on context, namespace and end-state checks. Repeat until accurate rather than memorized.

## Original knowledge checks

1. **Why change a Deployment rather than one of its Pods?** The controller owns desired Pod state and will replace a divergent Pod from its template.
2. **What distinct roles do CRI, CNI and CSI serve?** Container runtime, Pod networking and storage integration contracts.
3. **What does a CRD add?** A new API resource schema; an operator/controller is still needed for reconciliation behavior.
4. **Role versus ClusterRole?** Role is namespaced; ClusterRole can express cluster-scoped rules or reusable namespaced rules.
5. **Does a RoleBinding copy a role?** No; it grants subjects the referenced role's rules in the binding's namespace.
6. **How should RBAC be proven?** With `auth can-i` and positive/negative operations for the intended identity, verb, resource and namespace.
7. **Why validate a kubeadm cluster with cross-node traffic?** Node Ready alone does not prove CNI routing, DNS, Service path or application reachability.
8. **Why is an etcd snapshot not a complete disaster-recovery plan?** External configuration, certificates, manifests, application data and provider state may exist outside etcd.
9. **What should happen before a worker upgrade?** Check skew/instructions/capacity and disruption, cordon/drain safely, then upgrade components and validate before uncordoning.
10. **Why preserve etcd quorum?** Losing quorum prevents consistent writes and can make control-plane recovery materially harder.
11. **Helm success versus workload success?** Release rendering/application may succeed while Pods, traffic or dependencies remain unhealthy.
12. **Why preview Kustomize output?** Transformers and patches can produce names, selectors, images or configuration different from intent.
13. **What owns operator behavior?** Its controller reconciliation, supported by CRDs, RBAC, webhooks and managed custom resources.
14. **Readiness versus liveness?** Readiness normally removes a Pod from eligible Service backends while its address can remain in an EndpointSlice; liveness failure can trigger container restart.
15. **When is a startup probe useful?** To protect a slow-starting application from premature liveness/readiness judgments.
16. **Why can an HPA fail to help?** Metrics, requests, capacity, scalable target or a shared bottleneck may be missing.
17. **What does a toleration guarantee?** Permission to schedule despite a matching taint, not placement on that node.
18. **Hard versus preferred affinity?** Hard rules filter nodes and can leave Pods Pending; preferences influence scoring.
19. **Why can a rollback be incomplete?** It restores workload template revision, not external data/schema/configuration changes.
20. **Where do admission failures appear?** In the API response and often Events; RBAC permission alone does not bypass admission.
21. **What creates Service endpoints?** For selector-based Services, the EndpointSlice controller represents matching Pods; listed addresses can be unready, so inspect conditions as well as selector matching.
22. **First checks for empty EndpointSlices?** Namespace, selector/labels and Pod existence; distinguish no listed addresses from addresses present with unready/terminating conditions.
23. **Why test Pod IP, Service and route separately?** They isolate application, Service data plane and ingress/gateway segments.
24. **How do NetworkPolicies combine?** Additively; allowed traffic is the union, and both egress and ingress may govern a flow.
25. **What must implement NetworkPolicy?** A network plugin/data plane with policy support.
26. **Why can DNS fail under default-deny egress?** DNS queries to the resolver were not explicitly allowed.
27. **Does an Ingress resource route traffic alone?** No; a compatible Ingress controller must reconcile it.
28. **Useful Gateway API status conditions?** Accepted, Programmed and ResolvedRefs, plus parent/listener attachment evidence.
29. **PVC versus PV?** A PVC requests storage; a PV represents supplied storage bound to a claim.
30. **Why use WaitForFirstConsumer?** To defer topology-aware provisioning until workload placement is known.
31. **Does ReadWriteMany provide application locking?** No; access capability is not transaction or concurrency control.
32. **What can Retain reclaim policy require?** Explicit data handling, cleanup and deliberate PV reuse after claim deletion.
33. **Why test storage after Pod recreation?** To prove data is outside the replaced container/Pod lifecycle.
34. **Why is CrashLoopBackOff not a diagnosis?** It is restart backoff; logs, exit state, configuration and dependencies reveal cause.
35. **What should be read for a Pending Pod?** Scheduling/admission conditions and Events, then PVC/resource/constraint evidence.
36. **Why use previous container logs?** The current restart may not contain the failure output from the terminated instance.
37. **What does NotReady require beyond `kubectl`?** Node conditions plus kubelet, runtime, network, pressure, certificate and host evidence.
38. **If the API is down, where next?** Load-balancer/host path, kubelet, runtime/static control-plane containers, ports, certificates and etcd.
39. **Connection refused versus timeout?** Refused often reaches a host with no listener; timeout more often suggests drop/path/unresponsive behavior, though evidence must confirm.
40. **Why not delete a stuck PVC first?** Reclaim and backend behavior may destroy or strand data before the real attach/mount cause is known.
41. **Does the Kubernetes v1.37 release move CKA off v1.35 automatically?** No; the live exam page and curriculum remain authoritative, and the 4–8-week policy creates a recheck window rather than a guaranteed switch date.
42. **Did ingress-nginx retirement remove the Ingress API objective?** No; it retired one community controller, so distinguish API intent from the installed implementation and use a maintained controller for production.

43. **Does a PDB stop a Deployment rollout from making Pods unavailable?** No; rollout strategy governs that update. Resulting unavailability still affects voluntary-eviction budget calculations.
44. **Does a cross-namespace Gateway attachment grant backend access elsewhere?** No; listener attachment and ReferenceGrant authorization are separate relationships.
45. **Does RWO enforce exactly one Pod?** No; it is a single-node mode. Supported RWOP provides the single-Pod constraint.
46. **What did the offline rendering checks establish?** Client generation, transformations, reference rewriting and selected failures; no server admission, running cluster or traffic behavior.

## Places to learn

| Resource | Access | Estimated time |
|---|---|---:|
| [Official CKA page](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/) and [public CNCF v1.35 curriculum](https://github.com/cncf/curriculum/blob/master/CKA_Curriculum_v1.35.pdf) | Public; exam paid | 3–5 hours mapping/review, plus 8–14 selected simulator hours |
| [Kubernetes v1.35 documentation](https://v1-35.docs.kubernetes.io/docs/home/) | Public | 20–35 selected reading/lab hours; use as reference, not a cover-to-cover course |
| [Kubernetes v1.37 release](https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/) | Public release watch; use only to trigger the exam-version recheck | 20–40 minutes |
| [Ingress NGINX retirement notice](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/) | Public operational warning; distinguishes the controller from the stable Ingress API | 15–25 minutes |
| [Linux Foundation Kubernetes Fundamentals (LFS258)](https://training.linuxfoundation.org/training/kubernetes-fundamentals/) | Paid | 35 listed course hours, 17 chapters and hosted browser labs; add 35–70 independent lab hours |
| [Pluralsight CKA path](https://www.pluralsight.com/paths/certified-kubernetes-administrator) | Subscription/trial | 30 listed hours, 15 courses, 6 labs and practice exam; add 30–60 lab hours |
| [KodeKloud CKA](https://kodekloud.com/courses/cka-certification-course-certified-kubernetes-administrator/) | Subscription/free preview | 26.12 listed video hours (17 modules, 306 lessons; lab update April 10, 2026 names v1.35) plus browser labs and mock exams; allow 45–75 hours total |
| [O'Reilly CKA in-depth guidance and practice](https://www.oreilly.com/videos/certified-kubernetes-administrator/0642572014448/) | Subscription/trial | Earlier listing: 8 hours 7 minutes; blocked during this review, not reverified; add 20–40 proposed lab hours |
| [Udemy/KodeKloud CKA with Practice Tests](https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/) | Paid; price varies | Earlier listing: 25 hours 57 minutes; blocked during this review, not reverified; allow 45–75 proposed total hours |

LFS258 now advertises hosted browser labs; optional self-managed cloud infrastructure may still cost money. Its outline explicitly includes Helm/Kustomize and CRDs, and its overview includes Gateway API. Pluralsight mixes older courses with 2026 additions; path totals alone do not establish every lesson's v1.35 alignment. KodeKloud lists Gateway API, Helm and Kustomize, with a separate September 2025 video update. Public metadata was reviewed; paid lessons, mock questions and provider labs were not accessed. All added independent practice times are planning estimates.

This is not a complete list and is not meant to be consumed in full. Choose one current structured route, use the official v1.35 objectives and documentation as the source of truth, build and break disposable clusters, and use the included simulator late for diagnosis. Check every course against the live CKA version, especially when it still teaches older Ingress-only, pre-Gateway API, pre-current-admission, or outdated kubeadm behavior. Avoid recalled tasks and question dumps; this is a performance exam.
