---
exam_code: CKAD
vendor_id: linux-foundation
official_blueprint: https://training.linuxfoundation.org/certification/certified-kubernetes-application-developer-ckad/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-01
---

# CKAD Certified Kubernetes Application Developer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ckad-coverage-record). The [official CKAD page](https://training.linuxfoundation.org/certification/certified-kubernetes-application-developer-ckad/) is authoritative.

**Current baseline:** Kubernetes v1.35 and the five weighted domains on the live CKAD page<br>
**Lifecycle watch:** The exam is aligned to a recent Kubernetes minor release about 4–8 weeks after release; the official page still names v1.35 as of September 1, 2026, so verify immediately before practice and scheduling<br>
**Official delivery snapshot:** Online, remotely proctored, performance-based command-line exam; two hours; certification valid for two years; 12-month eligibility, one retake, and two 36-hour Killer.sh simulator activations with 17 questions per attempt listed<br>
**Prerequisite:** No formal certification prerequisite; the official scope assumes working knowledge of OCI-compliant container images/runtimes, microservice architecture, and Kubernetes resource definitions

## How to use this guide

CKAD is application-centered. Practice each requirement as a deployable, observable, secure and reachable application rather than as isolated YAML:

1. confirm context, namespace, source image/code, resource owner, and requested end state;
2. select the right workload, configuration, identity, storage, rollout and network resources;
3. preview manifests and package output, apply the smallest coherent change, and watch reconciliation;
4. verify conditions, events, logs, probes, resources, endpoints and user behavior;
5. restart, roll forward/back, reschedule or recreate to prove the design survives normal lifecycle events.

Build a small service repeatedly on disposable Kubernetes v1.35 clusters. Keep source, Containerfile/Dockerfile, manifests, Kustomize overlays and Helm values in version control. Use the [versioned Kubernetes v1.35 documentation](https://v1-35.docs.kubernetes.io/docs/home/) to understand APIs and examples. Learn fast discovery with `kubectl explain`, API resource discovery, dry run, output formats and focused documentation search. Do not reproduce proprietary simulator tasks or recalled exam material.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Weighted objective map

| Domain | Weight | Performance evidence |
|---|---:|---|
| 1. Application design and build | 20% | Build images; select workloads; compose multi-container Pods; use ephemeral and persistent volumes |
| 2. Application deployment | 20% | Implement rolling, blue/green and canary strategies; deploy and change Helm/Kustomize packages |
| 3. Application observability and maintenance | 15% | Handle API deprecation; implement probes; monitor, log and debug applications |
| 4. Application environment, configuration and security | 25% | Use extensions, access/admission, resources/quotas, configuration, Secrets, identities and security contexts |
| 5. Services and networking | 20% | Configure and troubleshoot Services, NetworkPolicies and Ingress exposure |

## 1. Application design and build — 20%

### Images and executable contracts

A container image packages a filesystem and configuration; the runtime creates a container from it. Define a small, reproducible build context, use a trusted version-pinned base, order layers for caching, avoid build secrets in layers, install only needed dependencies, use a non-root user where possible, and set clear entrypoint/command behavior. OCI image tags are mutable names; a digest pins content. Record source-to-image provenance and scan/sign according to organizational policy.

Understand how image `ENTRYPOINT`/`CMD` relate to Kubernetes `command`/`args`: Kubernetes `command` overrides the image entrypoint and `args` overrides its default command arguments. Test signals and graceful termination. An application should handle `SIGTERM`, stop accepting new work, finish or checkpoint appropriately, and exit before its termination grace period. Writing application data only into the writable container layer loses it on replacement.

Build and run locally, inspect metadata, push only to an authorized registry, then deploy by immutable reference when possible. Diagnose `ImagePullBackOff` through name, tag/digest, platform architecture, registry reachability/trust, pull secret, policy and runtime Events—not by repeatedly deleting the Pod.

> **Related item:** A Kubernetes manifest cannot repair a poor container contract. Deterministic startup, signal handling, non-root compatibility, logs to streams and externalized state make orchestration reliable.

### Choose the workload owner

A bare Pod is useful for diagnosis but offers limited lifecycle management. Choose the controller whose reconciliation matches the application:

- Deployment for replaceable stateless replicas, revisions and rolling updates;
- StatefulSet for stable identity, ordering and claim templates;
- DaemonSet for one eligible Pod per node, often an agent;
- Job for finite successful completion and parallelism;
- CronJob for scheduled Jobs, with concurrency, deadline and history controls.

Selectors and Pod-template labels connect controller intent to Pods. A selector mismatch can prevent creation, orphan objects or route traffic incorrectly. Inspect owner references. Changing a controller-managed Pod is not durable because the owner recreates it from the template.

Jobs require idempotence and explicit completion/failure behavior. Set restart policy, backoff, completions/parallelism and deadline as needed. Cron schedule, timezone support, suspend, starting deadline and concurrency policy influence duplicate or missed execution. Kubernetes scheduling is not exactly-once business processing; design the application for retries and deduplication.

### Multi-container patterns

Containers in one Pod share the network namespace and can share volumes. They are scheduled, started and terminated as one unit. Use an init container for ordered setup that must succeed before app containers start. A sidecar continuously supports the primary container—for example proxying, synchronizing or processing output—when shared lifecycle is appropriate. Adapter and ambassador are design labels for transforming output or mediating external access; implement the actual containers, ports, volumes and readiness behavior rather than memorizing labels.

Avoid combining unrelated services simply because localhost is convenient. Resource requests/limits and security contexts apply per container and/or Pod. `kubectl logs` needs a container selection in multi-container Pods; `exec` and probes also target a container. If an init container cannot finish, the application never starts; inspect its status, logs, mounts, identity and dependency.

### Ephemeral and persistent volumes

Use `emptyDir` for Pod-lifetime scratch/shared data, ConfigMap/Secret/projected volumes for configuration or identity material, and PVCs for data that must outlive a Pod. Know that `emptyDir` survives individual container restarts but not Pod replacement. Mount paths can hide image files underneath; `subPath` changes mount behavior and configuration refresh expectations.

For a PVC, match storage class, capacity, access mode and volume mode. The application still owns filesystem permissions, data layout, locking, backup and consistency. Validate by writing data, recreating the Pod, and reading it again. For StatefulSets, volumeClaimTemplates create per-Pod claims; scaling down or deleting the controller does not necessarily delete claims, which protects data but needs lifecycle planning.

## 2. Application deployment — 20%

### Rolling updates and safe rollback

A Deployment rollout changes the Pod template, creates a new ReplicaSet and moves capacity according to `maxSurge` and `maxUnavailable`. Readiness determines whether a replica counts as available. Choose settings based on spare capacity, minimum service, startup time and downstream load. Observe `rollout status`, Deployment conditions, ReplicaSets, Pod readiness/restarts, endpoints and actual traffic.

Record a change cause through source/commit/release metadata rather than relying on memory. Pause/resume only when you understand the intermediate state. Rollback restores a previous Pod template revision; it does not revert a database migration, external configuration, message schema or data. Prefer backward/forward-compatible application changes and a tested roll-forward option.

### Blue/green and canary with Kubernetes primitives

Blue/green keeps old and new application sets available, validates green, then switches a stable Service selector or route/backend. Ensure label design prevents accidental mixed endpoints. Test configuration, data compatibility, warm-up and rollback before switching. After the cutover, retain blue only as long as needed and monitor both correctness and resource cost.

A basic canary runs a small new-version replica set beside the stable set behind compatible routing. With one Service and matching labels, traffic split follows ready endpoints approximately, not a contractual percentage. More controlled weighting may require ingress/gateway/service-mesh capabilities outside the basic primitive. Define metrics, observation window, abort criteria and promotion steps. Keep session state and schema compatibility in mind.

Deployment strategies are end-to-end: manifests create replicas, probes gate endpoints, Services/routes deliver traffic, telemetry evaluates behavior, and release/data controls determine rollback safety.

> **Related item:** Kubernetes provides rollout primitives, while the release strategy also needs observability, compatibility, decision thresholds, ownership and a recovery path.

### Helm packages

Helm renders templates with chart defaults and supplied values, applies resources, and records a release. Inspect chart metadata, dependencies, values schema, templates, hooks, CRDs, RBAC, images and security-sensitive host access. Use `helm template` or dry-run-style inspection before install. Set the intended namespace and release name explicitly.

After install/upgrade, check release status/history and Kubernetes resources; a successful Helm operation is not proof of application readiness. Preserve the values used. During rollback, verify that the chart revision, application/data compatibility and any hooks behave as intended. Uninstall semantics can leave CRDs, PVCs or hook-created resources; inspect instead of assuming a clean slate.

### Kustomize composition

Kustomize composes bases and overlays using resources, patches, name/label transformers, image changes and ConfigMap/Secret generators. Keep common application structure in a base and environment-specific differences in small overlays. Preview with `kubectl kustomize`; confirm names, namespaces, selectors, references, images and generated hashes before `apply -k`.

Generators can create hash-suffixed names that trigger a workload rollout when configuration changes. Understand references and do not hand-edit rendered output as the source. Avoid copying a full base per environment because drift becomes invisible. Use source review and a rendered-manifest diff for deployment evidence.

## 3. Application observability and maintenance — 15%

### Probes and health semantics

Startup probe protects slow initialization; while it has not succeeded, liveness and readiness do not run. Readiness removes a Pod from Service endpoints without restarting it. Liveness restarts a failed container. Select HTTP, TCP, gRPC or command checks that match meaningful local behavior; configure path/port, delay, period, timeout and thresholds around real startup/recovery times.

Do not make liveness depend on every remote dependency: a shared outage could restart every replica and erase useful evidence. Readiness may include dependencies needed to serve traffic, but balance it against cascading removal. A probe endpoint should be lightweight, authorized appropriately, and distinguish initialization, health and ability to serve.

### CLI monitoring, logs and events

Start with desired/current state and conditions: `get`, `describe`, Events sorted by time, owner resources and generation. `kubectl top` provides current usage only when metrics infrastructure exists. Compare usage with requests/limits, throttling, OOM state, node pressure and application latency; one sample is not a trend.

Containers should write operational logs to stdout/stderr. Use `logs`, `--previous`, container selection, timestamps and label selectors as supported. Stream logs are not durable centralized logging; correlation, retention and query are related production capabilities. Capture identifiers and time boundaries. Events are concise and expiring; they complement rather than replace component/application logs.

Use `exec` only when the image includes the needed tools and policy permits. `kubectl debug`/ephemeral-container or a diagnostic Pod can provide tools without changing the application image, depending on cluster policy and version. Preserve evidence before restarting.

### API deprecations

Kubernetes APIs move through versions and can be deprecated before removal. Inspect manifest `apiVersion`/`kind`, discover served/preferred APIs, read versioned deprecation guides and migrate schemas/controllers before a cluster upgrade. A resource stored under one version may be served under another; conversion and behavior still matter. CRDs have their own served/storage versions and conversion strategy.

Validate rendered Helm/Kustomize output, not only source templates. Search all manifests and generated resources, use server-side dry run against the target cluster where appropriate, update clients/controllers/webhooks, and exercise create/update/read/delete plus application behavior. Do not blindly change the `apiVersion` string when fields or semantics changed.

> **Related item:** An API migration is a compatibility change across manifests, rendered packages, controllers, stored objects and application behavior—not a text replacement exercise.

### Debugging workflow

Use a consistent ladder:

1. reproduce and scope the symptom;
2. confirm context, namespace, object and owner;
3. inspect conditions, Events, container/init states and recent changes;
4. inspect current and previous logs, configuration, identity, mounts, resources and probes;
5. trace Service/endpoints/DNS/policy/Ingress if traffic is involved;
6. correct the controlling resource and watch reconciliation;
7. verify function, restart/replacement, traffic and monitoring.

`Pending` may reflect scheduling, quota, PVC or admission. `ImagePullBackOff` reflects a failed pull with delayed retries. `CrashLoopBackOff` is a restart delay, not the cause. `CreateContainerConfigError`, init failures, OOM kills and probe failures each have different evidence. Avoid deleting the only failing Pod before capturing `describe`, Events and previous logs.

## 4. Application environment, configuration and security — 25%

### Extensions, authentication, authorization and admission

Discover built-in and extended resources with `api-resources`, `api-versions`, `explain` and CRD inspection. A CRD defines an API; an operator/controller reconciles its custom resources. Before using one, confirm scope, versions/schema, required fields, status/conditions, controller health, RBAC and admission webhooks. Do not guess a custom resource's schema from its name.

Authentication identifies a user or ServiceAccount; authorization determines allowed operations; admission validates or mutates an otherwise authenticated/authorized request. An API error may identify any of these boundaries. Use `kubectl auth can-i` for intended identity/action/namespace, then an actual positive/negative operation. Admission can enforce policy, defaults, quotas or custom validation.

Application developers should request the minimum RBAC from administrators and design around namespace boundaries. Reading Secrets, creating Pods under privileged service accounts or binding roles can provide indirect power. Never embed cluster-admin credentials in an image or ConfigMap.

### Requests, limits and quotas

Requests drive scheduling and influence QoS/autoscaling; limits constrain runtime. CPU limit pressure generally throttles, while exceeding memory limit can produce OOM termination. Set resources per container based on measured behavior, including sidecars/init peaks. Pod overhead, node allocatable capacity and namespace policies also affect placement.

LimitRange can set/default/validate per-object resource values; ResourceQuota caps aggregate namespace consumption and object counts. A Pod can be rejected by quota even when a node has capacity. Inspect the API error, quota used/hard values and LimitRange. Define application concurrency and backpressure: adding a limit without load behavior can turn saturation into failures.

Horizontal scaling requires an eligible controller, metrics and requests for utilization-based behavior; quota/capacity may block replicas. Scaling replicas does not solve serialized work, shared storage, a single downstream bottleneck or unsafe application state.

### ConfigMaps, Secrets and ServiceAccounts

ConfigMaps decouple non-sensitive configuration; Secrets are intended for sensitive values but base64 is encoding, not encryption. Create them without leaking values into shell history, logs or source. Consume selected keys or entire sets as environment variables or files. Environment values are fixed at container start; mounted projected configuration may update with delay, while `subPath` has different refresh behavior. The application must reload or be rolled deliberately.

Use immutable or versioned configuration when predictability matters. Validate missing/invalid keys and fail safely. Keep configuration ownership clear across image defaults, command arguments, environment and mounted files.

A ServiceAccount supplies workload identity. Assign one explicitly when permissions are needed, bind minimum roles, and understand projected time-limited tokens. Disable or avoid token mounting when the application does not call the API. Test allowed and denied API calls from that identity. External workload identity integrations are implementation-specific; the durable principle is short-lived, audience-bound, least-privilege identity.

### Application security contexts and capabilities

Pod/container `securityContext` can set user/group IDs, non-root enforcement, filesystem groups, privilege escalation, Linux capabilities, read-only root filesystem and seccomp behavior. Start from non-root, no privilege escalation, drop all capabilities, read-only root and a runtime-default seccomp profile, then add only documented needs. Image file ownership and writable paths must support the chosen user/group.

Linux capabilities divide root-like powers; adding one should be a specific exception, not a shortcut. Privileged mode and host namespaces/paths materially cross isolation boundaries. A read-only root filesystem requires explicit writable ephemeral/persistent mounts for caches, temp files or logs. Validate both application success and a negative action that should fail.

Secrets, RBAC, NetworkPolicy and security context address different layers. None alone secures the application. Image trust/scanning, admission policy, node/runtime hardening and external secret systems are related production controls even when not directly configured in an application task.

> **Related item:** Least privilege is a working contract across image user/files, runtime capabilities, volumes, ServiceAccount/RBAC, configuration/Secrets and network paths. Validate the application under the restriction rather than adding broad exceptions.

## 5. Services and networking — 20%

### Services and application access

A Service selects Pods and exposes a stable virtual name/address and port; EndpointSlices hold eligible backends. Trace traffic: client DNS → Service name/IP/port → ready EndpointSlice address/targetPort → container listener → response. Confirm namespace, selector labels, Pod readiness, named ports and protocol. A Service with no endpoints often has selector/readiness mismatch, not a broken Service implementation.

ClusterIP exposes inside the cluster; NodePort adds a node-level port; LoadBalancer asks an integration for external provisioning. CKAD emphasizes application access, so remain provider-neutral. Port-forward is a diagnostic tunnel, not production exposure. A headless Service supports direct endpoint discovery and is often paired with StatefulSets.

For failure isolation, test localhost/container listener, Pod IP, Service DNS/name and Service IP in sequence. Connection refused, timeout and name-resolution errors provide different clues. Use a small diagnostic Pod when the application image has no tools.

### NetworkPolicy

NetworkPolicy selects Pods and allows ingress/egress by Pod/namespace selector, IP block and port. Once a Pod is selected for a direction, only the union of allowed rules in that direction passes; policies are additive. Source egress and destination ingress may both need permission. An empty `podSelector` selects all Pods in the policy namespace; an empty rule peer can have broad meaning depending on structure, so preview carefully.

Start with default deny in a lab, then add named flows: frontend to API, API to database, and required DNS egress. Test an allowed and denied path. Policy enforcement requires a supporting network plugin. NetworkPolicy is layer 3/4 intent; it does not by itself provide application authentication, TLS or HTTP authorization.

### Ingress

Ingress rules map host/path to Services but require an installed compatible Ingress controller. Set and verify IngressClass, host, path and path type, backend Service/port, address and TLS Secret. Inspect controller logs/events and backend endpoints. Test with correct Host header/DNS and TLS name. Controller-specific annotations are not portable Kubernetes API behavior; identify them explicitly if used.

The current CKAD objectives name Ingress, not Gateway API. Gateway API is useful adjacent knowledge and appears in the CKA v1.35 scope, but do not substitute it for practicing Ingress. External DNS and load balancer provisioning are separate integrations.

> **Related item:** Application reachability is a chain. A healthy Pod does not prove selector, endpoint readiness, Service ports, policy, DNS, Ingress controller or TLS configuration.

## Integrated scenarios

### Scenario 1: Release a secure API without downtime

Build a non-root image that handles termination and writes logs to streams. Deploy it with requests/limits, startup/readiness/liveness probes, ConfigMap, Secret and minimum ServiceAccount. Apply restrictive security context. Use a Deployment rolling strategy and Service. Start a new version compatible with current configuration/data, watch ReplicaSets/endpoints/traffic, and verify both success and denied API/network actions. If signals regress, roll back the workload and state explicitly what external changes are not rolled back.

### Scenario 2: Canary through package overlays

Render a Helm chart or Kustomize base/overlay for stable and canary Deployments with deliberate labels. Run a small canary beside stable behind one Service or two controlled routes. Verify image, configuration, probes, resources and endpoint mixture. Define promotion/abort evidence from logs, failures and latency. Promote by reviewed source change, render/diff/apply, and remove or scale down canary only after verification. Record the v1.35 API versions used.

### Scenario 3: An application is Running but unreachable and loses work

Trace container listener, readiness, Pod labels, EndpointSlices, Service port/targetPort, DNS, NetworkPolicy and Ingress. Separately inspect its `emptyDir` use and determine whether the work must survive Pod replacement; if yes, select a PVC and application-safe persistence design. Correct the owner resources, prove allowed/denied traffic, write data, recreate/reschedule the Pod and verify recovery. Do not treat restored traffic as proof of persistence.

## Hands-on labs

Use only disposable or explicitly authorized environments.

1. **Image-to-Pod contract (2–3 hours):** build a small application image with non-root user, signal handling and stream logs. Override command/args, break an image reference and permissions, diagnose, then pin a working digest.
2. **Controller and multi-container design (2–3 hours):** implement Deployment, Job and CronJob variants; add init and sidecar containers with shared `emptyDir`. Prove ordering, logs, restart behavior and idempotent retry.
3. **Volume survival (1.5–2.5 hours):** compare container filesystem, `emptyDir`, projected ConfigMap/Secret and PVC. Restart containers, replace/reschedule Pods and document exactly what survives.
4. **Three release strategies (3–4 hours):** perform rolling update/rollback, blue/green Service switch and a basic canary. Define availability/compatibility/telemetry evidence and deliberately seed a bad readiness probe.
5. **Helm and Kustomize (2–4 hours):** package the same app with a Helm chart and with base/overlays. Render, diff, install/apply, change image/configuration, roll back, and inspect leftover PVC/CRD/hook behavior.
6. **Observability and API maintenance (2–3 hours):** seed startup, probe, image, resource and configuration faults. Use Events, current/previous logs, top/debug where available, then migrate a deprecated practice manifest using target-version docs and server-side validation.
7. **Least-privilege application (2–4 hours):** combine quota/LimitRange, ConfigMap/Secret, minimum ServiceAccount/RBAC, restrictive security context and default-deny policies. Prove positive and negative application/API/network behavior.
8. **Two-hour rehearsal (2.5–3 hours each):** create original tasks in official proportions across build/design, release, observability, configuration/security and networking. Use fresh namespaces, track skipped tasks, and reserve 10–15 minutes for context, namespace and end-state validation.

## Original knowledge checks

1. **How do Kubernetes `command` and `args` relate to an image?** They override the image entrypoint and default command arguments respectively.
2. **Why handle SIGTERM?** It enables graceful removal from service and clean shutdown before forced termination.
3. **Why prefer a digest for a controlled release?** It identifies immutable image content rather than a movable tag.
4. **Deployment versus Job?** Deployment maintains replaceable replicas; Job drives finite successful completion.
5. **What must a retryable Job consider?** Idempotence, backoff, completion, deadline and duplicate work.
6. **What does an init container guarantee?** It must complete successfully in sequence before regular app containers start.
7. **When is a sidecar appropriate?** When a continuous supporting process genuinely shares the Pod's lifecycle/network/volumes.
8. **What survives a container restart but not Pod replacement?** `emptyDir` and other Pod-lifetime ephemeral data.
9. **Why can `subPath` surprise configuration users?** It has different projected-volume update behavior and mounts only a selected path.
10. **What owns a controller-managed Pod?** Its workload controller and Pod template, visible through owner references.
11. **What gates availability during a rolling update?** Ready replicas, strategy limits, capacity, probe behavior and dependencies.
12. **What does Deployment rollback not restore?** External schemas, data, configuration systems or irreversible side effects.
13. **How does blue/green switch traffic with basic primitives?** A stable Service selector or route changes from validated old to new labels/backends.
14. **Is a one-Service canary an exact weighted split?** No; endpoint selection is approximate and implementation/traffic dependent.
15. **Why render Helm before install?** To inspect actual resources, RBAC, hooks, images, CRDs and values-derived behavior.
16. **What is Helm release success missing?** Proof of workload readiness, traffic, data and dependent service behavior.
17. **Why use Kustomize overlays?** To keep shared source centralized and environment differences small and reviewable.
18. **What can a ConfigMap generator hash do?** Change the generated name/reference and trigger a workload rollout.
19. **Readiness versus liveness?** Readiness removes traffic eligibility; liveness restarts the container.
20. **Purpose of startup probe?** Delay other probes until slow initialization succeeds or definitively fails.
21. **Why avoid remote dependencies in liveness?** A dependency outage could restart all replicas and amplify failure.
22. **What does `kubectl top` require?** A working metrics provider and it shows samples, not historical trends.
23. **Why use `logs --previous`?** To inspect output from the prior terminated container in a restart loop.
24. **What must an API-version migration include?** Schema/semantic review, rendered resources, controllers/webhooks, stored objects and behavioral testing.
25. **Why is CrashLoopBackOff not the root cause?** It only reports delayed repeated restarts; exit state/logs/configuration reveal cause.
26. **What is the difference among authentication, authorization and admission?** Identity, permission and request validation/mutation.
27. **What does a CRD provide versus an operator?** API schema/storage versus reconciliation behavior.
28. **CPU versus memory limit pressure?** CPU is normally throttled; memory overage can cause OOM termination.
29. **How can quota block a schedulable Pod?** Namespace aggregate/object limits are enforced before node placement.
30. **Why are base64 Secret values not encrypted?** Base64 is reversible encoding; encryption/access controls are separate.
31. **Do environment variables update when ConfigMap changes?** No; a new container start is required.
32. **Why use an explicit ServiceAccount?** To give the workload a clear, minimum identity rather than accidental default access.
33. **What does `allowPrivilegeEscalation: false` constrain?** A process gaining more privileges than its parent through mechanisms such as setuid.
34. **Why drop capabilities?** To remove granular kernel powers the process does not need.
35. **What builds Service endpoints?** Ready Pods matching the selector, represented through EndpointSlices.
36. **First checks when a Service has no endpoints?** Namespace, selector/labels, Pod existence and readiness.
37. **How do NetworkPolicies combine?** Additively, with both source egress and destination ingress potentially governing a flow.
38. **Does NetworkPolicy encrypt traffic?** No; it permits/denies L3/L4 flows and needs separate TLS/application controls.
39. **What makes Ingress work?** A compatible controller plus correct class, rules, Service/endpoints and optional TLS.
40. **Why test localhost, Pod IP, Service and Ingress separately?** Each isolates a different segment of the application traffic chain.

## Places to learn

| Resource | Access | Estimated time |
|---|---|---:|
| [Official CKAD page](https://training.linuxfoundation.org/certification/certified-kubernetes-application-developer-ckad/) and [public CNCF v1.35 curriculum](https://github.com/cncf/curriculum/blob/master/CKAD_Curriculum_v1.35.pdf) | Public; exam paid | 3–5 hours mapping/review, plus 8–14 selected simulator hours |
| [Kubernetes v1.35 documentation](https://v1-35.docs.kubernetes.io/docs/home/) | Public | 18–30 selected reading/lab hours; use as a reference |
| [Linux Foundation Kubernetes for Developers (LFD259)](https://training.linuxfoundation.org/training/kubernetes-for-developers/) | Paid | 35 listed course hours plus 30–60 independent lab hours |
| [Pluralsight CKAD path](https://www.pluralsight.com/paths/certified-kubernetes-application-developer-ckad-2023) | Subscription/trial | 13 listed hours, six courses, four labs and practice exam; add 25–50 lab hours |
| [KodeKloud CKAD](https://kodekloud.com/courses/certified-kubernetes-application-developer-ckad/) | Subscription/free preview | 14.75 listed video hours plus browser labs and mock exams; allow 35–60 hours total |
| [O'Reilly CKAD Prep Course](https://www.oreilly.com/videos/certified-kubernetes-application/0642572045296/) | Subscription/trial | 8 hours 3 minutes listed plus 20–40 lab hours; May 2024, so gap-check v1.35 |
| [Udemy/KodeKloud CKAD with Tests](https://www.udemy.com/course/certified-kubernetes-application-developer/) | Paid; price varies | 16 hours 34 minutes listed plus browser labs; allow 35–60 hours total |

This is not a complete list and is not meant to be consumed in full. Choose one current route, build one application through every domain, and use official v1.35 objectives/documentation as the gap checklist. The Udemy and KodeKloud entries are the same course family, so choose one access route. Verify older material for current API versions, security contexts, admission, multi-container behavior and release tooling. Avoid recalled tasks and question dumps; this is a performance exam.
