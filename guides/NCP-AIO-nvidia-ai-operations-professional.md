---
exam_code: NCP-AIO
vendor_id: nvidia
official_blueprint: https://www.nvidia.com/en-us/learn/certification/ai-operations-professional/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# NVIDIA-Certified Professional: AI Operations (NCP-AIO) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live weighted blueprint, mixed knowledge/lab delivery contract, links and exam-integrity boundary were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#ncp-aio-coverage-record).

**Current baseline:** NCP-AIO is an active professional, English, remotely proctored exam with 30 multiple-choice questions and three integrated hands-on lab exercises inside one 120-minute session. It is pass/fail and listed at USD 500.<br>
**Upcoming change:** No revision or retirement announcement was present on the checked certification page September 2, 2026.<br>
**Prerequisite:** NVIDIA recommends two to three years operating data-center infrastructure with NVIDIA hardware and says candidates should be comfortable on live-cluster Linux CLI using Slurm, Kubernetes and Base Command Manager (BCM). This is experience guidance, not a prerequisite credential.<br>
**Validity:** NVIDIA says the credential is valid for two years and can be renewed by retaking the exam. Verify registration, lab environment and policy before purchase.

## How to use this guide

This is a performance-included exam. Reading can establish vocabulary, but readiness means completing normal administration and diagnosis under time pressure while preserving evidence. Practice an operator loop:

1. confirm scope, impact, authorization and desired state;
2. inspect the smallest useful layer and recent change;
3. form a falsifiable hypothesis;
4. run a safe check and compare to a known-good baseline;
5. apply the narrowest reversible correction if authorized;
6. verify workload and system outcomes, document, and roll back or escalate.

Build disposable or dedicated labs. Commands below are categories and examples, not a production runbook. Never patch firmware, synchronize images, change partitions, restart fabric/driver services, delete workloads or run load/diagnostic tools on shared systems without approved change, drain, backup and recovery procedures.

> **About related items:** A `Related item:` callout adds prerequisite, architectural or operational context. It supports the topic but does not assert that NVIDIA used the wording in the public blueprint.

## Blueprint map

| Topic area | Weight | Performance evidence |
|---|---:|---|
| Installation and Deployment | 31% | Inspect/configure BCM, categories/images, users, network, schedulers/Kubernetes, patches/firmware and reports; explain Mission Control, DOCA and Run:ai placement |
| Administration | 23% | Operate Slurm, Kubernetes, Run:ai and MIG against an AI data-center architecture with safe state verification |
| Workload Management | 23% | Deploy and observe training/inference from NGC; allocate resources among teams; diagnose scheduling, placement and runtime |
| Troubleshooting and Optimization | 23% | Isolate Docker, NVLink/NVSwitch Fabric Manager, BCM, Magnum IO, storage and NGC deployment faults; validate correction and performance |

## 1. Installation and Deployment — 31%

### 1.1 Establish desired state and control planes

An AI cluster contains several control planes. BCM provisions nodes, images, configuration, monitoring and workload-manager integration. Slurm schedules batch jobs. Kubernetes reconciles container workloads and cluster resources. Run:ai adds AI workload/resource orchestration on Kubernetes. BMCs provide out-of-band hardware control. DCGM observes/diagnoses GPUs. NVIDIA Mission Control is a broader AI-factory operations control plane/toolkit. Know which system is authoritative for each state before changing anything.

Start with inventory: rack/node role, BMC and host identity, CPU/GPU/DPU/NIC/HCA/storage, serial and GPU UUID, physical/logical fabric, firmware, OS/kernel, driver/CUDA/container runtime, BCM category/image, scheduler partition or Kubernetes labels/taints, owner and maintenance/support status. Desired state must be versioned and recoverable.

`Related item:` **Source of truth versus observer.** A dashboard may display state without owning it. Changing a generated host file directly can be overwritten by BCM or an operator. Trace the controller, desired configuration, reconciliation and evidence path.

### 1.2 BCM entities and Base View

BCM groups common node configuration into categories. Software images define bootable node OS/software state. Nodes inherit category settings with explicit exceptions. Base View is the graphical interface; `cmsh` is a common CLI administration interface. Use the assigned BCM version’s manual because objects and workflows change.

Be able to:

- identify unhealthy, down or mismatched nodes and compare a good peer;
- inspect category membership, image assignment, device/service state and telemetry;
- create or modify a category/image only in a lab or approved change;
- provision a node, follow the boot/provisioning path, and verify post-provision state;
- synchronize software images and distinguish image-build state from node runtime;
- install/configure workload-manager integration and verify controller/node services;
- produce usage, health, performance and issue reports with timestamps and scope.

A useful failure tree follows DHCP/PXE or boot source → management-network reachability → image/export/repository → disk/layout/install → first boot → services/config overlay → scheduler/orchestrator registration → GPU/fabric/storage validation. Do not leap to reimage before collecting evidence.

### 1.3 Users, roles and permissions

Implement identity lifecycle with named accounts, groups/projects, least-privilege administrative roles, scheduler associations/quotas and Kubernetes/Run:ai roles. Separate cluster administration from workload use. Federate where supported, protect service credentials, audit privilege, and remove access promptly.

Validate the effective path: identity exists → group/project membership is correct → home/data permissions work → Slurm account/QOS or Kubernetes namespace/RBAC/resource quota exists → container/registry access works → logs identify the actor. A successful login alone is not proof that authorization is correct.

### 1.4 Network, DPU and switch operations

Maintain separate understanding of management, BMC, storage and compute fabrics even if some share physical infrastructure. Verify address, route, DNS/NTP, link state/rate, MTU, bond, interface/driver/firmware and switch/port mapping. For InfiniBand or RoCE, include fabric manager/subnet manager, RDMA device, topology, congestion/error counters and collective tests.

BlueField DPUs run infrastructure services on DPU Arm cores and accelerate networking/security/storage in supported designs. Deploying DOCA Services requires matching DPU mode, firmware/BSP/DOCA and management/orchestration. Confirm the DPU versus host execution target, compatible image/chart, service status and data path. Never infer success only from a running pod/container.

`Related item:` **Time consistency.** NTP/time synchronization affects authentication, TLS, logs, distributed coordination and causal incident analysis. “The network works” is incomplete if clocks disagree.

### 1.5 Patches, firmware and image synchronization

Treat BIOS/BMC/GPU/NIC/DPU/switch firmware, OS/kernel, driver, CUDA, Fabric Manager, container runtime, BCM and scheduler/orchestrator as a compatibility set. Read release notes/support matrices and record current/target versions, dependencies and downgrade path.

Use a canary sequence: preserve configuration and evidence → drain workloads → verify redundancy/capacity → update management dependencies in supported order → update a representative node/category/image → reboot only when required → validate hardware discovery, services, GPU diagnostics, fabric/storage, scheduler, container and workload → expand in batches → retain rollback artifact. Image synchronization is not finished until a booted node and representative workload pass.

### 1.6 Install Slurm, Kubernetes and Run:ai

For Slurm, understand controller/database/compute daemon roles, authentication/time/DNS, node definitions, partitions, GRES/GPU resources, accounting and service state. A node can be reachable but unavailable to Slurm because definition, daemon, health or state differs.

For Kubernetes, understand control-plane and worker components, container runtime, CNI/CSI, GPU Operator/device plugin, labels/taints, namespaces/RBAC/quota and storage classes. BCM may install/initialize Kubernetes on NVIDIA hosts, but verify resulting nodes, system pods, advertised GPU resources, networking, storage and a disposable GPU workload.

Run:ai integrates with Kubernetes. Verify version/platform prerequisites, installation components, cluster connection, organizations/departments/projects, roles, quotas and a small workload before enabling production teams. Separate Run:ai policy from Kubernetes physical resource advertisement.

## 2. Administration — 23%

### 2.1 Slurm cluster administration

Operators should confidently use documented tools such as `sinfo`, `squeue`, `sacct`, `scontrol`, `sbatch`, `srun` and service/journal inspection in their lab version. Know what each answers:

- `sinfo`: partition and node availability/state;
- `squeue`: pending/running jobs and reason;
- `sacct`: completed/ongoing job accounting and exit/resource evidence;
- `scontrol`: detailed/controller state and authorized administrative updates;
- `sbatch`/`srun`: submit batch or launch steps with resource requests.

Interpret pending reasons, node `DRAIN/DOWN/IDLE/ALLOCATED` state, GRES mismatches, QOS/account limits, dependencies, reservation and priority. Restore a drained node only after root cause/correction and health validation. Do not cancel or requeue someone else’s job without incident/change authority.

`Related item:` **Requested versus allocated versus consumed.** Scheduler allocation may be correct while the application uses only one GPU, wrong CPU affinity or slow input. Correlate scheduler state with process/GPU/fabric/storage evidence.

### 2.2 Kubernetes administration

Use `kubectl get`, `describe`, `logs`, `events`, resource/metrics views and carefully scoped `exec` to follow desired state → scheduling → image pull → volume/network → container start → readiness → service. Diagnose `Pending`, `ImagePullBackOff`, `CrashLoopBackOff`, `OOMKilled`, failed mounts and missing extended resources from events before changing manifests.

For GPU work, confirm GPU Operator/component health, node labels, `allocatable` extended resources, requests/limits, MIG strategy/profile, tolerations/affinity, runtime class where used, and in-container GPU visibility. A host’s `nvidia-smi` success does not prove that the pod receives a device.

### 2.3 Run:ai administration

Model organizations/departments, projects, users/roles, quotas, over-quota policy, priority/preemption and node pools around business ownership. Run:ai can dynamically allocate fractional/shared capacity and queue work, but policy must preserve isolation and predictable high-priority service behavior.

Trace a pending workload through Run:ai queue/policy, Kubernetes scheduler/events, device advertisement, node state and image/storage dependencies. For utilization changes, compare useful throughput and latency—not just GPU percentage—and test preemption/checkpoint behavior.

### 2.4 Configure MIG

MIG partitions supported GPUs into isolated GPU instances with dedicated compute/memory resources and defined profiles. Before change, verify hardware/driver/support, active workloads, orchestrator strategy and persistence behavior. Drain, configure through the authoritative platform (for example GPU Operator/MIG Manager in Kubernetes), verify device/profile advertisement, schedule a test workload, then test reconfiguration/rollback.

Profile choice trades capacity fit and fragmentation. Several small instances can improve density for bounded inference, while full-GPU or different sharing may suit large training. MIG, vGPU and time slicing have different isolation, platform and licensing contracts.

### 2.5 Architecture for AI workload operations

Operational architecture includes compute topology, management/compute/storage fabrics, data and checkpoint tiers, schedulers/orchestrators, observability, identity/secrets, image/registry/supply chain, failure domains and support. Create a dependency graph. If DNS, NTP, registry, shared filesystem or scheduler controller is a hidden single point, GPU redundancy alone cannot meet availability.

## 3. Workload Management — 23%

### 3.1 Pull and deploy NGC containers safely

Choose an NGC artifact compatible with GPU architecture, driver and workload. Record immutable digest/version, publisher, license/entitlement and scan/approval. Authenticate without embedding tokens in scripts/images. Pull to an authorized registry/cache if policy requires. Confirm runtime GPU injection, mounts, ports, environment/secrets, user IDs and shared-memory/ulimit needs.

Diagnose the chain: registry DNS/TLS/auth → repository/tag/digest/entitlement → local disk/cache → container runtime → NVIDIA Container Toolkit/CDI → device permissions → driver/runtime compatibility → application/library/model. “Image pulled” only validates the first half.

### 3.2 Training with Slurm

A training submission should state partition/account/QOS, node/GPU/CPU/memory/time, container or environment, data/checkpoint paths, output/logs and distributed launcher. For multi-node work, verify consistent image/software, GPU visibility, NCCL/fabric interfaces/topology, rendezvous, DNS/time and storage.

Measure queue time, startup/data stage, samples/tokens per second, scaling efficiency, GPU/SM/tensor/memory/fabric activity, checkpoint duration and failures. A higher GPU allocation that yields worse scaling efficiency may be waste, not optimization.

### 3.3 Inference with Kubernetes

Use a Deployment or suitable controller for long-running replicated inference, a Job for bounded batch work, and Services/routes as required. Pin image/model versions, request GPUs or MIG resources, configure CPU/RAM and probes, mount or fetch the model safely, set rollout strategy and capture latency/throughput/error plus saturation signals.

Readiness should represent ability to serve, not just process existence. Test cold model load, overload/backpressure, pod/node failure and rollback. Autoscaling needs a meaningful signal and capacity/queue boundary; adding replicas cannot fix a shared storage/model-download or scarce-GPU bottleneck.

### 3.4 Workloads and allocation with Run:ai

For both training and inference, define project/owner, environment, command, compute/memory/GPU fraction or profile, data, priority and policy. Confirm queue and actual Kubernetes workload, then correlate allocation with outcome. Test fair sharing, guaranteed quota, over-quota borrowing, priority and preemption using disposable jobs.

Allocate resources among teams with explicit business priority, minimum guarantees, burst policy, charge/showback, checkpointability, service SLOs and exception review. Run:ai, Slurm and Kubernetes express these differently; do not assume a quota field has identical semantics.

`Related item:` **Preemption safety.** Reclaiming a GPU can lose work or break service unless the workload checkpoints, drains or has replicas. A fair policy without tested workload behavior is incomplete.

### 3.5 System-management tools in workload diagnosis

Start at service impact, then move downward. Correlate application response/job exit and logs with orchestrator events, scheduler allocation, container/process, GPU/DCGM, NVLink/PCIe/fabric, storage, host and facility signals. Compare time-aligned good and bad runs. Change one variable, repeat, and retain the evidence.

## 4. Troubleshooting and Optimization — 23%

### 4.1 A reusable fault-isolation matrix

| Symptom | First evidence | Common boundaries to test | Proof of recovery |
|---|---|---|---|
| Container cannot start/use GPU | Runtime error, host/container GPU visibility | image arch, runtime/CDI, device permission, driver/CUDA, resource allocation | same pinned image completes a minimal authorized workload |
| Job pending/fails | Slurm reason or K8s/Run:ai events; exit/log | quota/QOS, node/GRES/device, image/data, affinity, health | requested placement runs and accounting/status is clean |
| Multi-GPU slowdown/hang | per-rank log, NCCL/fabric/DCGM timeline | topology, interface, MTU, link errors/congestion, version, straggler | representative collective/workload meets baseline |
| Inference unhealthy/slow | readiness, request latency/errors, saturation | model/config, memory, batching/concurrency, CPU/data, network, backend compatibility | load test meets SLO without hidden errors |
| Node inconsistent after update | inventory/drift, services, diagnostics | category/image, kernel/driver/firmware, reboot, config reconciliation | node matches desired state and passes acceptance workload |

### 4.2 Troubleshoot Docker and NGC deployment

Separate daemon/runtime health, registry pull, image, mount/network, device injection and application. Inspect container state/exit/log, daemon journal, disk/inode, permissions, proxy/DNS/TLS and NVIDIA runtime configuration. Reproduce with a minimal approved container/digest. Do not “fix” by disabling TLS, using privileged mode broadly or copying credentials into an image.

NGC-specific failures can involve authentication/API key, organization/team entitlement, wrong repository/tag, rate/connectivity, image platform, disk capacity or compatibility. Preserve exact pull/run command with secrets redacted, image digest, runtime/driver versions and error.

### 4.3 Troubleshoot NVLink/NVSwitch Fabric Manager

Some NVSwitch systems require Fabric Manager compatible with the installed driver. Confirm topology/system requirement, package/version alignment, service state/journal and NVIDIA device/fabric health. A service restart can affect running multi-GPU workloads; drain/escalate per runbook.

Distinguish intra-node NVLink/NVSwitch problems from inter-node InfiniBand/Ethernet problems. Use topology, link/error state and an approved collective or GPU peer test. A distributed hang can come from one rank, storage or rendezvous as well as fabric.

### 4.4 Troubleshoot BCM

Classify the issue: management daemon/database/license/GUI, provisioning/boot, category/image drift, monitoring, user/auth, scheduler integration, network or node service. Compare BCM desired state, node runtime and a healthy peer. Inspect alerts/events/logs, device state, image synchronization and dependency services before forcing state.

For node outage, confirm BMC/power, management link, boot/provision path, OS reachability, BCM agent/services, scheduler/orchestrator registration, GPU/fabric/storage and representative workload. Document any manual override and return ownership to BCM reconciliation.

### 4.5 Troubleshoot Magnum IO and storage

Magnum IO spans data movement technologies such as NCCL, GPUDirect RDMA and GPUDirect Storage. Identify the actual component/path; “Magnum IO issue” is too broad. Validate support/versions, topology, device/interface selection, permissions, filesystem/mount and measured link/storage behavior. Compare a component benchmark to end-to-end workload to locate the bottleneck.

For storage, check capacity/inodes, mount/metadata service, client errors/timeouts, network, permissions, per-client and aggregate throughput, metadata/small-file behavior, cache, striping/layout where applicable, and checkpoint concurrency. Avoid benchmarking against production data or clearing caches without approval. Recovery must restore workload correctness and the expected throughput envelope.

### 4.6 Optimize without hiding risk

Define the outcome: completion time, latency percentile, throughput, queue time, availability or cost/energy. Capture baseline with repeatable input and versions. Form one hypothesis, change one controlled factor, measure multiple runs, check errors/quality, then retain or roll back. Possible levers include batch/concurrency, precision, GPU/profile/placement, CPU/NUMA affinity, data loader, local cache, parallelism, NCCL topology/interface, storage layout and scheduler policy.

Optimization that disables checks, consumes all headroom, breaks isolation, changes numerical/AI quality or cannot survive failure is not production improvement.

## Integrated scenarios

### Scenario 1: Post-update nodes cannot join workloads

After a BCM image/driver update, several nodes appear healthy in Base View but Slurm marks them unavailable and GPU containers fail. Preserve versions and change scope; compare category/image and booted runtime to a good node; check daemon/GRES definition, driver/toolkit/device visibility and Fabric Manager compatibility; run safe acceptance diagnostics and a minimal NGC workload. Correct the desired image/category, validate, return one canary node, then roll out. Do not resume nodes solely because their power state is green.

### Scenario 2: Kubernetes inference misses latency SLO

Pods are ready and GPU utilization is high, but tail latency regresses after teams share the cluster. Correlate request, queue, pod, allocation, DCGM, CPU, memory, network and model-load signals. Verify Run:ai policy and GPU/MIG profile, placement and interference; compare full-GPU versus supported partition/batch/concurrency variants. Retain the configuration that meets quality, latency and isolation with headroom; document rollback and capacity trigger.

### Scenario 3: Multi-node training intermittently hangs

One Slurm job hangs during collectives and later checkpoint writes. Use per-rank logs, job allocation/topology, DCGM, NVLink/fabric counters, storage client/server and system journals on a common timeline. Reproduce with approved component tests in drained nodes. Isolate a degraded link, node, rank or storage boundary; quarantine and escalate rather than masking the fault with unlimited retries. Prove recovery with collective and end-to-end baselines plus checkpoint restore.

## Hands-on performance labs

Use a disposable training environment or systems specifically authorized for practice. Time each lab, keep a command/evidence journal, and reset to a known state.

1. **BCM state and report lab (6–10h):** navigate Base View and documented CLI; inventory nodes/categories/images/services; compare a healthy and intentionally misconfigured lab node; produce a health/usage/issue report and correction plan.
2. **Provision/update canary lab (8–12h):** clone or build an approved lab image/category, provision a node, stage a safe package/config change, drain/update/reboot/validate and roll back. Capture each control-plane and workload proof.
3. **Slurm operations lab (8–12h):** configure or use a small lab cluster; submit CPU/GPU jobs, accounts/QOS/partition/resource requests; diagnose pending/failure; drain/correct/resume a node; inspect accounting and distributed-job evidence.
4. **Kubernetes GPU lab (8–12h):** verify GPU Operator/device advertisement; deploy a pinned NGC-derived training Job and inference Deployment; use requests, labels/taints, probes, storage and events; break one safe dependency, diagnose and restore.
5. **Run:ai policy lab (6–10h):** in an authorized environment, model teams/projects/roles/quotas and priorities; run contention, over-quota and preemption/checkpoint cases; reconcile Run:ai, Kubernetes and outcome evidence.
6. **MIG allocation lab (5–8h):** on supported dedicated hardware, drain, enable/configure through the authoritative manager, verify profiles/resources, schedule workloads, observe isolation/fragmentation, and restore baseline. If unavailable, build an exact runbook and analyze sanitized outputs.
7. **Fault-isolation circuit (10–16h):** rotate through Docker/NGC auth or runtime, scheduler allocation, Fabric Manager/version, fabric/collective and storage symptoms. For each: impact, hypothesis, safest discriminating command, correction, verification, rollback and escalation artifact.
8. **Integrated timed simulation (6–10h):** complete three original tasks—a BCM/Slurm administration change, Kubernetes/NGC deployment, and cross-layer performance fault—within 120 minutes, including verification and notes. Review command fluency, wrong turns and risk, then repeat with new failures.

## Readiness checks

1. Can you name the authoritative control plane for each cluster state?
2. Can you inventory hardware through firmware, image and workload ownership?
3. How do BCM categories, software images, nodes and exceptions relate?
4. Can you trace a failed provision without immediately reimaging?
5. What must a Base View health/performance report prove?
6. How do user, project, scheduler and Kubernetes permissions connect?
7. Can you verify effective access without granting broad privilege?
8. Which management, BMC, compute and storage paths must be checked?
9. How do host and DPU Arm execution targets differ?
10. What dependency evidence precedes firmware or driver changes?
11. Can you execute a canary, validation, batch rollout and rollback?
12. What must be verified after installing Slurm through BCM?
13. What must be verified after initializing Kubernetes through BCM?
14. What must be verified after installing Run:ai?
15. Can you interpret `sinfo`, `squeue`, `sacct` and `scontrol` evidence?
16. Why is a job pending, and which layer owns the reason?
17. When is it safe to return a drained Slurm node?
18. Can you diagnose common Kubernetes pod states from events first?
19. How do GPU Operator, device plugin and resource requests connect?
20. Can you trace a Run:ai workload through Kubernetes to the device?
21. How do quota, borrowing, priority and preemption affect teams?
22. What are the support, drain and profile steps for MIG change?
23. How do MIG, vGPU, passthrough and time slicing differ?
24. Can you identify hidden architecture single points of failure?
25. Can you select and pin an authorized NGC artifact and digest?
26. How do registry, runtime, device and application failures differ?
27. Can you submit a reproducible single- and multi-node Slurm job?
28. Which signals prove distributed training scales productively?
29. Can you deploy inference with meaningful readiness and rollback?
30. Why might autoscaling fail to solve latency?
31. Can you allocate resources with an explicit business policy?
32. How do Slurm, Kubernetes and Run:ai quota semantics differ?
33. Can you correlate app, scheduler, container, GPU, fabric and storage time?
34. What is the smallest discriminating check for a Docker failure?
35. What evidence distinguishes NGC auth, tag and compatibility failure?
36. When is Fabric Manager required, and why is restart risky?
37. Can you separate intra-node NVLink from inter-node fabric issues?
38. How do you compare BCM desired state with node runtime?
39. Which Magnum IO component and path is actually involved?
40. Can you diagnose storage capacity, metadata and throughput separately?
41. What makes a benchmark safe, representative and reproducible?
42. Can you define outcome, baseline, hypothesis and rollback for tuning?
43. Why can high utilization still represent poor performance?
44. Can you complete each scenario without risky shortcut commands?
45. Can you produce all eight evidence packs in a resettable lab?
46. Can you complete three fresh tasks inside the 120-minute budget?
47. Do your notes preserve exact IDs, versions, times, commands and results?
48. Have you rechecked the live blueprint, lab contract and exam policy?

### Check key

- **Ready:** You can administer and diagnose BCM, Slurm, Kubernetes, Run:ai, containers, GPU/fabric and storage in a resettable lab, with verification and rollback.
- **Review:** You know commands and product names but cannot choose the safest evidence path or complete tasks inside the time budget.
- **Gap:** You would experiment on production, force state without root cause, or treat a green dashboard/high utilization as proof. Return to the labs and operator loop.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Use the live blueprint and one primary hands-on route, then select exact product documentation for the versions in your lab. Access, durations, prices and revisions were checked September 2, 2026 and can change.

| Resource | Access | Estimated time | Best use and freshness boundary |
|---|---|---:|---|
| [NCP-AIO certification and blueprint](https://www.nvidia.com/en-us/learn/certification/ai-operations-professional/) | Public | 4–6h mapping + repeated review | Canonical 31/23/23/23 scope, 30-question/three-lab/120-minute contract, USD 500 price and experience guidance. |
| [AI Operations Professional training outline](https://academy.nvidia.com/en/wp-content/uploads/2026/01/AI-Operations-Outline-2026.pdf) | Public outline / paid workshop | 20h outline schedule + 25–50h practice | Official recommended multi-day hands-on route. The outline says four five-hour sessions while the DGX learning-path card showed 24 hours/USD 3,000; verify the scheduled offering. |
| [AI Infrastructure and Operations Fundamentals](https://www.nvidia.com/en-us/training/academy/course-detail/?id=course:15139841) | Paid/account | 7h + 8–12h gaps | Official associate-level prerequisite refresher for compute, networking, storage and orchestration; insufficient alone for the professional labs. |
| [NVIDIA Base Command Manager documentation](https://docs.nvidia.com/base-command-manager/) | Public | 20–40h selective + lab | Versioned administrator, containerization, cloudbursting, installation and user manuals. Use the exact BCM major version assigned to the lab. |
| [Slurm documentation](https://slurm.schedmd.com/documentation.html) | Public | 12–24h + repeated lab | Canonical scheduler/admin/command semantics; match the lab release and local policy/plugins. |
| [Kubernetes resource and workload documentation](https://kubernetes.io/docs/concepts/resource-management/) | Public | 12–24h + repeated lab | Resource, device-plugin, scheduling and workload foundations; combine with the cluster’s supported Kubernetes/GPU Operator matrix. |
| [NVIDIA Run:ai documentation](https://docs.nvidia.com/run-ai/index.html) | Public | 8–16h + authorized lab | Install/monitor, organizations/resources, workloads and API routes; distinguish SaaS current behavior from a versioned self-hosted deployment. |
| [NVIDIA DCGM documentation](https://docs.nvidia.com/datacenter/dcgm/latest/contents.html) | Public | 6–12h + lab | GPU observation, diagnostics, fields, job statistics and exporter evidence; privileged diagnostics require an approved window. |
| [NVIDIA Container Toolkit troubleshooting](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/troubleshooting.html) | Public | 4–8h + fault lab | Current Docker/runtime/CDI troubleshooting and evidence collection; do not copy destructive cleanup from an unrelated version. |
| [NVIDIA Triton Inference Server documentation](https://docs.nvidia.com/deeplearning/triton-inference-server/index.html) | Public | 8–16h + deployment lab | Pinned NGC container, model repository, readiness, client, performance and debugging practice; monthly releases require version control. |

Commercial practice-only banks located during research did not reproduce the official 30-question plus three-lab structure and cannot establish CLI readiness. Avoid “real questions,” recalled items, dumps and guaranteed-pass content. Build original tasks from public objectives, then explain the evidence, correction, verification and rollback.
