---
exam_code: CKA
vendor_id: linux-foundation
official_blueprint: https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-01
---

# CKA Certified Kubernetes Administrator Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#cka-coverage-record). The [official CKA page](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/) is authoritative.

**Current baseline:** Kubernetes v1.35 and the five weighted domains on the live CKA page<br>
**Lifecycle watch:** CNCF plans quarterly alignment to Kubernetes releases; the official exam page still names v1.35 as of September 1, 2026, so verify the version immediately before practice and scheduling<br>
**Official delivery snapshot:** Online, remotely proctored, performance-based command-line exam; two hours; certification valid for two years; 12-month eligibility, one retake, and two Killer.sh simulator attempts listed<br>
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

### Prepare and create kubeadm clusters

Prepare compatible Linux hosts: unique identity, supported kernel/network settings, time, resolvable addresses, disabled or correctly handled swap according to the selected Kubernetes/kubelet configuration, a CRI-compatible runtime, correct cgroup-driver alignment, required ports, trusted repositories/packages, and stable networking. Pin and record component versions. `kubeadm init` bootstraps a control plane; copy the generated kubeconfig for the intended administrator, install exactly one compatible CNI, and use the generated join data to add nodes. Validate Nodes, system Pods, CoreDNS, routes, taints, runtime, and a cross-node application—not just `Ready`.

Static control-plane Pods are defined by manifests watched by kubelet. Their logs may require `crictl` when the API is unavailable. Certificates, kubeconfigs, manifests, etcd data, runtime state and kubelet configuration have distinct locations and owners. Know where to look without changing all of them at once.

For high availability, separate the stable API endpoint/load balancer from control-plane nodes, use multiple control-plane/etcd members as designed, distribute failure domains, and test quorum-aware recovery. A load balancer that returns TCP success can still route to an unhealthy API server. Preserve etcd quorum; do not casually restore one member into a live inconsistent cluster.

> **Related item:** Availability is end-to-end: client DNS and load-balancer health, API servers, etcd quorum, controllers/scheduler, worker capacity, networking, DNS and storage all contribute different failure modes.

### Lifecycle, backup and upgrade

Inventory server/client/node versions, repositories, skew rules, add-ons, APIs, CRDs, webhooks, PDBs and capacity. Back up etcd with the correct endpoint, CA, certificate and key; verify snapshot status and protect the file. Also preserve external configuration, certificates, manifests, encryption configuration and application data as required—an etcd snapshot is not every backup.

For a kubeadm upgrade, read the exact target-version instructions. Upgrade one supported minor step at a time when required; start with a control-plane node, then additional control planes and workers. Cordon and drain with awareness of DaemonSets, local data, disruption budgets and replacement capacity. Upgrade kubeadm, run plan/apply or node phase as appropriate, then kubelet/kubectl; restart and verify components, Nodes, workloads, traffic and storage before continuing. Uncordon only after evidence is good.

Restore is a controlled state replacement: stop or isolate affected components, validate snapshot, restore to the intended data directory/configuration, update static Pod or service ownership if needed, restart, and validate members, API state and applications. Practice failed and successful restores on disposable clusters.

### Helm, Kustomize and operators

Helm renders and tracks chart releases. Inspect values and templates, install into the intended namespace, verify hooks/resources, upgrade with known values, inspect history and roll back deliberately. A release success does not prove workload readiness. Treat charts as code and inspect security-sensitive RBAC, webhooks, CRDs, images and host access.

Kustomize composes bases and overlays without a templating language. Use resources, patches, name/label transformers, images, ConfigMap/Secret generators and `kubectl kustomize`/`apply -k`; preview output and understand hash-suffixed generated names. Keep environment differences in overlays instead of copying whole manifests.

When installing an operator, separate CRDs, controller, webhooks, RBAC and custom resources. Verify controller readiness, leader election where used, admission reachability, reconciliation status and cleanup/finalizers. Version compatibility matters across Kubernetes, the operator and managed application.

## 2. Workloads and scheduling — 15%

### Controllers, configuration and self-healing

A Pod is the scheduling unit and shares network/storage namespaces among its containers. Prefer controllers: Deployment for replaceable stateless replicas and rolling releases; StatefulSet for stable identity/ordered behavior and per-Pod claims; DaemonSet for node-local agents; Job/CronJob for completion-oriented work. Inspect selectors and Pod-template labels carefully—immutable or mismatched selectors can orphan or misroute workloads.

ConfigMaps hold non-secret configuration; Secrets are encoded API objects, not encrypted merely because values are base64. Consume configuration as environment variables, arguments or mounted files, and know refresh semantics. Protect Secret access with RBAC and encryption-at-rest/secret-management controls outside this objective when required. Changing a ConfigMap does not guarantee an application reload; roll or signal the workload according to application behavior.

Readiness controls whether endpoints receive traffic; liveness triggers container restart; startup prevents premature liveness/readiness evaluation during initialization. Set probes against meaningful behavior and choose delay, period, timeout, thresholds and endpoints deliberately. A liveness probe that depends on a remote downstream can amplify an outage.

Requests influence scheduling and are the denominator for utilization-based autoscaling; limits constrain runtime resources. CPU throttling and memory OOM behavior differ. Inspect Pod QoS, node allocatable state, usage and eviction signals. Horizontal Pod Autoscaler needs a usable metric path and scalable workload; increasing replicas cannot fix a shared dependency or no remaining capacity.

### Updates, rollback, admission and placement

For rolling updates, understand desired/current/available replicas, `maxSurge`, `maxUnavailable`, readiness, progress deadline, revision history and image pull behavior. Watch rollout, inspect the ReplicaSets and Pods, test traffic, and use rollback only after understanding configuration/data compatibility. A rollback of a Deployment does not roll back a database schema or external dependency.

Scheduling filters and scores feasible nodes. Use node selectors/affinity for placement, anti-affinity or topology spread for distribution, taints to repel and tolerations to permit, resource requests for capacity, and Pod affinity/anti-affinity for co-location/separation. Toleration does not force placement; affinity can. Hard requirements can leave Pods Pending; soft preferences allow degraded placement.

Admission occurs after authentication/authorization and before persistence. Built-in admission, policy/webhook controls, quotas and limit ranges can reject or mutate a Pod even when RBAC allows creation. Use Events and the API error. For a webhook problem, inspect service/endpoints/TLS/CA bundle, failure policy, match rules and controller availability before disabling policy.

> **Related item:** Desired replicas, schedulability, startup, readiness, Service endpoint membership and real user success are separate gates. Verify each one instead of using `Running` as a health verdict.

## 3. Services and networking — 20%

### Packet path, Services and endpoints

Each Pod receives an address; Pods should communicate without address translation inside the cluster model, while the CNI implements routing/encapsulation and NetworkPolicy enforcement capabilities. Trace a request in order: client name resolution → Service virtual name/IP/port → EndpointSlice-selected ready backend → Pod IP/targetPort → listener/process → response and return path. Compare this with direct Pod-IP and local-container tests.

Service selectors build EndpointSlices from matching Pods. Confirm labels, namespace, readiness and port name/number/protocol. `ClusterIP` is internal virtual access; `NodePort` exposes a port on nodes; `LoadBalancer` asks an integration to provision external access. Headless Services omit the virtual IP for discovery use cases. `externalTrafficPolicy`, session affinity, health checks and provider implementations affect path and source-IP behavior; do not assume cloud-specific behavior on a vendor-neutral exam.

Use `kubectl get svc,endpointslices,pods -o wide`, DNS queries from a disposable Pod, `curl`/`wget`/`nc` where installed, `ss` inside the relevant container/node, and CNI/kube-proxy or replacement data-plane evidence. Avoid random restarts before locating the failed boundary.

### NetworkPolicy, DNS, Ingress and Gateway API

NetworkPolicy selects Pods and defines allowed ingress/egress by peers and ports. Once a Pod is selected for a direction, traffic in that direction is restricted to the union of allowed rules; policies are additive. Both source egress and destination ingress may need to allow a connection. Empty selectors, namespaces, IP blocks, DNS egress and plugin support are common traps. Test an allowed and denied path from realistic identities.

CoreDNS normally serves cluster names through a Service. Diagnose Pod resolver configuration, search domains/`ndots`, CoreDNS Pods, Service and EndpointSlice, ConfigMap, logs, upstream reachability and NetworkPolicy. Directly querying CoreDNS separates name-service reachability from search-name behavior. DNS failure can look like application or Service failure.

Ingress resources require an Ingress controller; the resource alone does nothing. Match controller class, host/path/path type, backend Service/port, controller logs, address and TLS Secret. Gateway API separates infrastructure and route concerns through GatewayClass, Gateway, listeners and route resources such as HTTPRoute. Inspect `Accepted`, `Programmed`, `ResolvedRefs` and parent status; verify allowed route attachment and cross-namespace references. The official v1.35 CKA objectives explicitly include both Ingress and Gateway API, so practice both rather than treating one as a synonym for the other.

> **Related item:** Network objects express intent, while CNI, Service data plane, DNS, ingress/gateway controller and external load balancer implement different segments. Healthy YAML cannot substitute for segment-by-segment traffic evidence.

## 4. Storage — 10%

### Volumes, PVs, PVCs and dynamic provisioning

An ephemeral Pod volume follows the Pod; persistent storage is modeled through PersistentVolume (supply), PersistentVolumeClaim (request), StorageClass (provisioning policy) and CSI/backend implementation. A workload mounts a claim, not an arbitrary StorageClass. Trace claim phase, selected class, requested capacity/access mode/volume mode, binding, provisioner events, PV claim reference, CSI controller/node behavior, attachment, mount and application permissions.

Access modes express capabilities used for matching and attachment; they do not automatically provide application-level locking. Filesystem versus block volume modes change consumption. StorageClass fields can include provisioner, parameters, reclaim policy, volume binding mode and expansion. `WaitForFirstConsumer` lets topology-aware provisioning consider the scheduled Pod; immediate provisioning may select topology before placement. A default class is an admission convenience, not a universal backend guarantee.

Reclaim policy governs what happens to dynamically provisioned or released backing storage after claim deletion: delete or retain requires different recovery/cleanup. Deleting a PVC can be destructive. Understand finalizers, protection, StatefulSet claim retention behavior, snapshots/backups, and application-consistent recovery. A PV in `Released` is not automatically safe to rebind without handling data and claim-reference state.

For Pending claims, compare requested attributes with available PVs/classes and provisioner logs/events. For mount failures, inspect node/plugin registration, topology, access conflict, device/filesystem, credentials, permissions/security context and backend health. Validate with a write/read, Pod recreation and—when the design permits—rescheduling to another node.

> **Related item:** Kubernetes persistence protects attachment to storage, not automatically the correctness, backup, replication, transaction consistency or disaster recovery of data inside it.

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

For a stalled rollout, compare Deployment/ReplicaSet generations, new Pod states, readiness, capacity, quotas, PDBs, selectors, image and application compatibility. Pause destructive actions; a rollout restart may hide the first failure and does not correct bad desired state.

### Node and control-plane failures

A NotReady node requires conditions, taints, leases/heartbeats, capacity/pressure and kubelet/runtime/network evidence. Check time, disk/inodes, memory, PID pressure, certificates, kubelet configuration and dependencies. Drain before planned maintenance when capacity and disruption rules allow; distinguish cordon, drain and deletion.

If the API is unavailable, move below `kubectl`: endpoint/load balancer, host reachability, static Pod manifests, kubelet, runtime containers/logs, certificates, ports and etcd health/quorum. A malformed manifest can cause kubelet to repeatedly recreate a broken component. Back up before editing control-plane state. If scheduler/controller manager fail while API/etcd work, existing workloads may run while new scheduling or reconciliation stalls; inspect their static Pods, flags, kubeconfigs, leader election and logs.

### Service and storage failures

For a Service failure, compare direct local process, Pod IP, EndpointSlice, Service name/IP, then ingress/gateway/external route. Empty endpoints usually point to selectors/readiness; connection refused differs from timeout; DNS `NXDOMAIN` differs from no DNS response. Evaluate NetworkPolicy in both directions and remember external/provider behavior is implementation-specific.

For storage, distinguish PVC Pending, attachment failure, mount failure, permission failure, full/read-only filesystem and application consistency. Events often name the CSI stage. Protect data before delete/recreate experiments and confirm reclaim behavior. A replacement Pod on the same node is not proof of cross-node recoverability.

> **Related item:** Fast troubleshooting is not fast guessing. A short, repeatable evidence ladder reduces changes, preserves the original signal and makes verification part of the repair.

## Integrated scenarios

### Scenario 1: A release is healthy by replica count but users receive errors

The Deployment shows desired replicas, but the Gateway route intermittently returns 503. Confirm context/namespace and reproduce. Inspect rollout generation, Pod readiness/restarts/logs, Service selector and EndpointSlices. If only old Pods are endpoints, compare new labels and readiness. If endpoints are healthy, inspect HTTPRoute parent status, backend references, Gateway/controller logs and policies. Correct the owner—template labels/probe/route—not an individual Pod. Verify direct Pod, Service DNS, Service IP and Gateway path, then roll another replica and confirm monitoring.

### Scenario 2: Upgrade one control plane without losing service

Inventory versions/skew, HA endpoint, etcd members/health, add-ons and deprecated APIs. Take and verify an etcd snapshot plus required configuration backups. Confirm workload capacity and disruption constraints. Upgrade kubeadm and run the supported plan/apply sequence on one control plane; then kubelet/kubectl and service restart. Validate API, etcd, controllers, scheduler, Nodes, DNS, workloads, traffic and storage before the next node. Record rollback/recovery triggers; never improvise an unsupported downgrade into a live quorum.

### Scenario 3: A stateful workload cannot recover on a replacement node

Inspect Pod scheduling Events, PVC/PV/StorageClass, access/volume modes, topology, attachment and CSI controller/node logs. Determine whether the old attachment, node affinity, missing plugin, permissions or backend causes the failure. Protect data; do not delete the claim blindly. Apply the smallest safe fix, wait for attach/mount, validate application data, restart the Pod and test another supported reschedule. Confirm backup and reclaim policy separately from restored availability.

## Hands-on labs

Use disposable infrastructure and only systems you own or are authorized to change.

1. **Build and prove a kubeadm cluster (3–5 hours):** create a control plane and worker with v1.35-compatible components, CRI and CNI. Capture component ownership, join evidence, cross-node traffic and DNS. Reboot both nodes and validate again.
2. **RBAC and operator boundary (2–3 hours):** create a namespaced service account with minimum read/write scope, prove allowed/denied operations, then install a small operator/CRD in a lab. Trace CR to controller, status, RBAC, events and finalizer cleanup.
3. **Safe lifecycle rehearsal (3–5 hours):** take/verify etcd backup, cordon/drain, perform a supported single-minor kubeadm upgrade in a disposable cluster, validate every component, and restore a separate clone from snapshot.
4. **Release and scheduling matrix (2–3 hours):** deploy an app with requests/limits, three probes, ConfigMap/Secret, affinity, taint/toleration, topology spread and HPA. Cause Pending, failed readiness and bad rollout states; repair and roll back.
5. **Service path and policy (2–4 hours):** trace Pod → EndpointSlice → ClusterIP → DNS. Add default-deny and explicit ingress/egress including DNS. Prove allowed and denied paths, then expose the app through Ingress and Gateway API/HTTPRoute.
6. **Storage lifecycle (2–3 hours):** compare immediate and delayed binding where supported; create claims with different modes/policies, mount/write/recreate/reschedule, expand if supported, and observe retain/delete behavior using nonvaluable data.
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
14. **Readiness versus liveness?** Readiness removes traffic endpoints; liveness restarts a container.
15. **When is a startup probe useful?** To protect a slow-starting application from premature liveness/readiness judgments.
16. **Why can an HPA fail to help?** Metrics, requests, capacity, scalable target or a shared bottleneck may be missing.
17. **What does a toleration guarantee?** Permission to schedule despite a matching taint, not placement on that node.
18. **Hard versus preferred affinity?** Hard rules filter nodes and can leave Pods Pending; preferences influence scoring.
19. **Why can a rollback be incomplete?** It restores workload template revision, not external data/schema/configuration changes.
20. **Where do admission failures appear?** In the API response and often Events; RBAC permission alone does not bypass admission.
21. **What creates Service endpoints?** Matching, ready Pods represented through EndpointSlices, subject to Service selectors/readiness.
22. **First checks for empty EndpointSlices?** Namespace, selector/labels, Pod existence and readiness.
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

## Places to learn

| Resource | Access | Estimated time |
|---|---|---:|
| [Official CKA page](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/) and [public CNCF v1.35 curriculum](https://github.com/cncf/curriculum/blob/master/CKA_Curriculum_v1.35.pdf) | Public; exam paid | 3–5 hours mapping/review, plus 8–14 selected simulator hours |
| [Kubernetes v1.35 documentation](https://v1-35.docs.kubernetes.io/docs/home/) | Public | 20–35 selected reading/lab hours; use as reference, not a cover-to-cover course |
| [Linux Foundation Kubernetes Fundamentals (LFS258)](https://training.linuxfoundation.org/training/kubernetes-fundamentals/) | Paid | 35 listed course hours plus 35–70 independent lab hours |
| [Pluralsight CKA path](https://www.pluralsight.com/paths/certified-kubernetes-administrator) | Subscription/trial | 30 listed hours, 15 courses, 6 labs and practice exam; add 30–60 lab hours |
| [KodeKloud CKA](https://kodekloud.com/courses/cka-certification-course-certified-kubernetes-administrator/) | Subscription/free preview | 24.98 listed video hours plus browser labs and mock exams; allow 45–75 hours total |
| [O'Reilly CKA in-depth guidance and practice](https://www.oreilly.com/videos/certified-kubernetes-administrator/0642572014448/) | Subscription/trial | 8 hours 7 minutes listed plus 20–40 lab hours |
| [Udemy/KodeKloud CKA with Practice Tests](https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/) | Paid; price varies | 25 hours 57 minutes listed plus browser labs; allow 45–75 hours total |

This is not a complete list and is not meant to be consumed in full. Choose one current structured route, use the official v1.35 objectives and documentation as the source of truth, build and break disposable clusters, and use the included simulator late for diagnosis. Check every course against the live CKA version, especially when it still teaches older Ingress-only, pre-Gateway API, pre-current-admission, or outdated kubeadm behavior. Avoid recalled tasks and question dumps; this is a performance exam.
