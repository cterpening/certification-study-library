---
exam_code: NCP-AIO
vendor_id: nvidia
official_blueprint: https://www.nvidia.com/en-us/learn/certification/ai-operations-professional/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# NVIDIA-Certified Professional: AI Operations (NCP-AIO) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The canonical 31-topic blueprint, exam format and selected operations references were reviewed September 29, 2026. The local workbook passed 25 checks; eight infrastructure activities remain proposed. See the [deep-review report](../docs/research/2026-09-29-ncp-aio-deep-review.md). See the [coverage record](../docs/SOURCE-VALIDATION.md#ncp-aio-coverage-record).

**Current baseline:** NCP-AIO is an active professional, English, remotely proctored exam with 30 multiple-choice questions and three integrated hands-on lab exercises inside one 120-minute session. It is pass/fail and listed at USD 500.<br>
**Upcoming change:** No revision or retirement announcement was present on the checked certification page September 29, 2026.<br>
**Prerequisite:** NVIDIA recommends two to three years operating data-center infrastructure with NVIDIA hardware and says candidates should be comfortable on live-cluster Linux CLI using Slurm, Kubernetes and Base Command Manager (BCM). This is experience guidance, not a prerequisite credential.<br>
**Validity:** NVIDIA says the credential is valid for two years and can be renewed by retaking the exam. Verify registration, lab environment and policy before purchase.

**VERIFY CURRENT — conflicting official preparation material:** The [linked seven-page study guide](https://dam-cdn.nvd.orangelogic.com/AssetLink/ub08c12vdc5l53ksln5d4dlpt3346464.pdf) differs from the canonical webpage: its four main sections use 28/20/32/20 weights and 19 numbered topics, including Fleet Command. Its contents also shows a fifth 10% entry without a corresponding body section, producing a 110% contents total. Use the webpage's **31/23/23/23** blueprint below; do not merge the lists or infer a transition date from the PDF's FEB26 mark. The PDF describes section scoring and a performance report that the canonical page does not confirm; the [program FAQ](https://www.nvidia.com/en-us/learn/certification/) says pass/fail without a score. Those details need vendor clarification before relying on them for exam planning.

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

**CURRENT BLUEPRINT:** The canonical page contains 13 installation/deployment, five administration, seven workload-management and six troubleshooting topics. Its monitored objective and lifecycle snapshots are unchanged. The PDF discrepancy is recorded separately.

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

**PRACTICAL DEPTH — BCM configuration ownership:** In the [BCM 11 administrator manual](https://docs.nvidia.com/base-command-manager/manuals/11/admin-manual.pdf), a regular node belongs to exactly one category, while convenience groups can overlap. Categories and software images need not correspond one-to-one. Non-Boolean node settings can override category defaults; the documented Boolean settings use category/node OR semantics, so a node-level false does not override a category-level true. Roles also have priorities: category 250, default overlay 500 and node 750, with configurable overlay priority. Inspect the effective value rather than assuming every setting follows simple inheritance.

The same manual distinguishes `CLOSED` in BCM from scheduler drain: a closed node can still run jobs. `imageupdate` defaults to a dry run and provides synchronization logs; review the exclude list, provisioner freshness and expected service behavior before any authorized write. Copying files does not prove running processes picked up new libraries or configuration.

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

**VERIFY CURRENT — release-specific acceptance:** [BCM 11.34.0 release notes](https://docs.nvidia.com/base-command-manager/bcm-11-release-notes/bcm11-34-0.html), dated September 11, 2026, include fixes for image updates deleting a Slurm pre-job prolog/DCGM enablement link and for Kubernetes drain reporting. They also change Container Toolkit ownership in the Kubernetes setup path and add Slurm 26.05 support. Build canary checks around the affected scheduler hooks, monitoring and runtime, rather than treating a package version or green management status as acceptance. These are selected documented changes, not instructions to upgrade an existing cluster.

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

**PRACTICAL DEPTH — Slurm evidence:** The current [GRES documentation](https://slurm.schedmd.com/gres.html) is for Slurm 26.05. A configured resource count larger than discovery can drain a node. `AutoDetect=nvidia` avoids the NVML library dependency but does not detect MIGs or NVLinks; do not substitute it blindly for `nvml`. Slurm expects MIG devices to be pre-partitioned and does not dynamically partition them. The documented MIG accounting path lacks `gpumem`/`gpuutil`; absence does not prove idle capacity.

[Job exit-code documentation](https://slurm.schedmd.com/job_exit_code.html) separates batch-script, step and derived results. A script can exit zero after a central task failed. A colon suffix records a terminating signal, so `0:9` is not successful completion. Derived results can be annotated later; retain original job/step output and application artifacts when making an incident conclusion.

### 2.2 Kubernetes administration

Use `kubectl get`, `describe`, `logs`, `events`, resource/metrics views and carefully scoped `exec` to follow desired state → scheduling → image pull → volume/network → container start → readiness → service. Diagnose `Pending`, `ImagePullBackOff`, `CrashLoopBackOff`, `OOMKilled`, failed mounts and missing extended resources from events before changing manifests.

For GPU work, confirm GPU Operator/component health, node labels, `allocatable` extended resources, requests/limits, MIG strategy/profile, tolerations/affinity, runtime class where used, and in-container GPU visibility. A host’s `nvidia-smi` success does not prove that the pod receives a device.

### 2.3 Run:ai administration

Model organizations/departments, projects, users/roles, quotas, over-quota policy, priority/preemption and node pools around business ownership. Run:ai can dynamically allocate fractional/shared capacity and queue work, but policy must preserve isolation and predictable high-priority service behavior.

Trace a pending workload through Run:ai queue/policy, Kubernetes scheduler/events, device advertisement, node state and image/storage dependencies. For utilization changes, compare useful throughput and latency—not just GPU percentage—and test preemption/checkpoint behavior.

**PRACTICAL DEPTH — entitlement and placement:** The [self-hosted scheduler concepts](https://run-ai-docs.nvidia.com/self-hosted/platform-management/runai-scheduler/scheduling/concepts-and-principles) define quotas per project/department and node pool. Non-preemptible workloads must fit deserved quota; over-quota use is for preemptible work. A project's remaining quota cannot bypass an exhausted department boundary. Quota can also exceed physically usable capacity, and fragmentation or topology can prevent placement. Project/department rank and workload priority govern different comparisons. Pin the platform version and verify its policy instead of translating a Kubernetes quota or Slurm limit by name alone.

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

**PRACTICAL DEPTH — rollout capacity:** For an original two-replica service using one GPU per replica, `maxSurge: 1` and `maxUnavailable: 0` preserve two available replicas while requesting room for a third. With two GPUs already allocated and a namespace GPU quota of two, that surge lacks both quota and physical headroom. Raising quota does not add hardware. Allowing one unavailable replica reduces the availability requirement and needs an explicit SLO decision; terminating pods may retain resources during shutdown.

The [Deployment reference](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) rounds surge percentages up and unavailable percentages down. A progress deadline reports a stalled rollout; it does not automatically roll back. [ResourceQuota](https://kubernetes.io/docs/concepts/policy/resource-quotas/) can allow the Deployment object while rejecting its new Pods. Quota is an admission boundary, not a capacity reservation. [GPU scheduling](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/) requires equal GPU request/limit values when both are supplied; a limit alone supplies the request default.

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

**VERIFY CURRENT — preserve isolation while diagnosing:** The [Container Toolkit troubleshooting guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/troubleshooting.html) documents legacy-hook GPU-access loss following some container/cgroup updates, including certain `systemd` reload cases, and distinguishes CDI-based device injection. It also notes that a missing group-name warning can be cosmetic: permissions use the numeric group ID. Disabling supplementary device groups can remove access, and disabling SELinux labels removes separation. Identify the injection mode and actual failure before changing either. No runtime, driver, security policy or container was changed in this review.

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

## Executed local rendering and accounting workbook

This original example uses Python, PyYAML and an existing `kubectl` executable. The verified run used Python 3.13.14, PyYAML 6.0.3, kubectl 1.35.9 and embedded Kustomize 5.7.1. Save the code as `ncp_aio_workbook.py`, then supply your existing executable path and a disposable workspace directory:

```text
python ncp_aio_workbook.py /path/to/kubectl /path/to/workspace
```

The script creates and removes its own temporary files inside that workspace, supplies an empty kubeconfig, and only calls client version reporting and [local Kustomize rendering](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/). No API operation, image pull, cluster, Slurm service or GPU is involved. The deliberately nonexistent image and zero-filled digest are placeholders; do not apply the generated objects. The rendered documents illustrate accounting boundaries, not a deployable inference service.

```python
import copy
import csv
import io
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import yaml


def rollout_budget(deployment, quota, physical_free):
    spec = deployment["spec"]
    container = spec["template"]["spec"]["containers"][0]
    resources = container["resources"]
    gpu = resources["limits"]["nvidia.com/gpu"]
    request = resources.get("requests", {}).get("nvidia.com/gpu", gpu)
    if type(gpu) is not int or gpu <= 0 or request != gpu:
        raise ValueError("fixture requires equal positive integer GPU request/limit")
    replicas = spec["replicas"]
    update = spec["strategy"]["rollingUpdate"]

    def count(value, up):
        if isinstance(value, str) and value.endswith("%"):
            raw = replicas * int(value[:-1]) / 100
            return math.ceil(raw) if up else math.floor(raw)
        return int(value)

    surge = count(update["maxSurge"], True)
    unavailable = count(update["maxUnavailable"], False)
    if surge == unavailable == 0:
        raise ValueError("both rollout allowances are zero")
    steady = replicas * gpu
    ceiling = int(quota["spec"]["hard"]["requests.nvidia.com/gpu"])
    return dict(steady_gpu=steady, surge_gpu=surge * gpu,
                quota_room=ceiling - steady,
                physical_free=physical_free,
                minimum_available=max(0, replicas - unavailable),
                full_surge_fits=(ceiling - steady >= surge * gpu
                                 and physical_free >= surge * gpu))


def accounting_outcome(row, output_verified):
    values = [row["ExitCode"], row["DerivedExitCode"]]
    if any(not value for value in values):
        return "incomplete evidence"
    codes = [tuple(map(int, value.split(":"))) for value in values]
    if any(len(code) != 2 or any(v < 0 for v in code) for code in codes):
        raise ValueError("invalid synthetic exit record")
    if row["State"] != "COMPLETED" or any(code != (0, 0) for code in codes):
        return "investigate job and steps"
    return "verified fixture output" if output_verified else "verify application output"


def run(kubectl, workspace):
    workspace = Path(workspace).resolve(strict=True)
    kubectl = Path(kubectl).resolve(strict=True)
    checks = []

    def check(label, condition):
        if not condition:
            raise AssertionError(label)
        checks.append(label)

    with tempfile.TemporaryDirectory(prefix="ncp-aio-", dir=workspace) as temporary:
        root = Path(temporary).resolve(strict=True)
        assert root.parent == workspace  # Verify cleanup stays in the named workspace.
        config = root / "empty-kubeconfig.yaml"
        config.write_text("apiVersion: v1\nkind: Config\nclusters: []\nusers: []\ncontexts: []\n", encoding="utf-8")
        env = dict(os.environ, KUBECONFIG=str(config))

        def invoke(*args):
            result = subprocess.run([str(kubectl), *args], env=env,
                                    capture_output=True, text=True, timeout=20)
            if result.returncode:
                raise RuntimeError(result.stderr)
            return result.stdout

        version = json.loads(invoke("version", "--client", "-o", "json"))
        deployment = dict(apiVersion="apps/v1", kind="Deployment",
            metadata=dict(name="inference"), spec=dict(replicas=2,
                selector=dict(matchLabels=dict(app="inference")),
                strategy=dict(type="RollingUpdate", rollingUpdate=dict(maxSurge=1, maxUnavailable=0)),
                template=dict(metadata=dict(labels=dict(app="inference")),
                    spec=dict(containers=[dict(name="server",
                        image="registry.invalid/study/inference@sha256:" + "0" * 64,
                        resources=dict(limits={"nvidia.com/gpu": 1},
                                       requests={"nvidia.com/gpu": 1}))]))))
        quota = dict(apiVersion="v1", kind="ResourceQuota", metadata=dict(name="gpu-budget"),
                     spec=dict(hard={"requests.nvidia.com/gpu": "2"}))
        for name, value in [("deployment.json", deployment), ("quota.json", quota),
                            ("kustomization.yaml", dict(apiVersion="kustomize.config.k8s.io/v1beta1",
                                kind="Kustomization", namespace="ncp-aio-practice",
                                resources=["deployment.json", "quota.json"]))]:
            (root / name).write_text(json.dumps(value), encoding="utf-8")
        rendered = invoke("kustomize", str(root))
        objects = {v["kind"]: v for v in yaml.safe_load_all(rendered)}
        check("two rendered objects", set(objects) == {"Deployment", "ResourceQuota"})
        check("namespace transform", all(v["metadata"]["namespace"] == "ncp-aio-practice" for v in objects.values()))
        d, q = objects["Deployment"], objects["ResourceQuota"]
        check("selector preserved", d["spec"]["selector"]["matchLabels"] == d["spec"]["template"]["metadata"]["labels"])
        check("placeholder digest preserved", d["spec"]["template"]["spec"]["containers"][0]["image"].endswith("0" * 64))
        check("deterministic rendering", rendered == invoke("kustomize", str(root)))
        budget = rollout_budget(d, q, physical_free=0)
        check("steady state fits", budget["steady_gpu"] == 2)
        check("surge needs another GPU", budget["surge_gpu"] == 1)
        check("quota exhausted", budget["quota_room"] == 0)
        check("physical capacity exhausted", not budget["full_surge_fits"])
        check("two available required", budget["minimum_available"] == 2)
        room = copy.deepcopy(q)
        room["spec"]["hard"]["requests.nvidia.com/gpu"] = "3"
        check("quota alone does not add hardware", not rollout_budget(d, room, 0)["full_surge_fits"])
        check("hardware alone does not raise quota", not rollout_budget(d, q, 1)["full_surge_fits"])
        check("both allow full surge budget", rollout_budget(d, room, 1)["full_surge_fits"])
        constrained = copy.deepcopy(d)
        constrained["spec"]["strategy"]["rollingUpdate"] = dict(maxSurge=0, maxUnavailable=1)
        check("alternative permits reduced availability", rollout_budget(constrained, q, 0)["minimum_available"] == 1)
        percent = copy.deepcopy(d)
        percent["spec"]["replicas"] = 3
        percent["spec"]["strategy"]["rollingUpdate"] = dict(maxSurge="25%", maxUnavailable="25%")
        check("surge rounds up", rollout_budget(percent, room, 1)["surge_gpu"] == 1)
        check("unavailable rounds down", rollout_budget(percent, room, 1)["minimum_available"] == 3)
        no_requests = copy.deepcopy(d)
        del no_requests["spec"]["template"]["spec"]["containers"][0]["resources"]["requests"]
        check("limits supply request default", rollout_budget(no_requests, q, 0)["steady_gpu"] == 2)
        mismatch = copy.deepcopy(d)
        mismatch["spec"]["template"]["spec"]["containers"][0]["resources"]["requests"]["nvidia.com/gpu"] = 2
        try:
            rollout_budget(mismatch, q, 0)
        except ValueError:
            check("mismatched request rejected", True)
        else:
            raise AssertionError("mismatched request accepted")
    check("temporary directory removed", not root.exists())
    rows = list(csv.DictReader(io.StringIO(
        "JobID|State|ExitCode|DerivedExitCode\n"
        "81|COMPLETED|0:0|0:0\n"
        "82|COMPLETED|0:0|2:0\n"
        "83|FAILED|0:9|0:9\n"
        "84|COMPLETED|0:0|\n"), delimiter="|"))
    check("CSV parsed", len(rows) == 4)
    check("zero exit still needs output", accounting_outcome(rows[0], False) == "verify application output")
    check("output verified separately", accounting_outcome(rows[0], True) == "verified fixture output")
    check("step failure survives script zero", accounting_outcome(rows[1], True) == "investigate job and steps")
    check("signal failure retained", accounting_outcome(rows[2], True) == "investigate job and steps")
    check("missing accounting unknown", accounting_outcome(rows[3], True) == "incomplete evidence")
    return dict(passed=len(checks), checks=checks, client_version=version["clientVersion"]["gitVersion"],
                kustomize_version=version.get("kustomizeVersion"), pyyaml_version=yaml.__version__,
                initial_rollout_budget=budget, temporary_cleanup=True)


if __name__ == "__main__":
    result = run(sys.argv[1], sys.argv[2])
    print(json.dumps(result, sort_keys=True))
    print(f"{result['passed']} local rendering and accounting checks passed")
```

The verified output is **25 checks passed**, including cleanup. Rendering preserves the request, quota, selector and namespace, but performs no server admission or scheduling validation. The budget function assumes two already allocated replicas, one ordinary container, whole GPUs and a supplied count of eligible unused devices; it omits node placement, init containers, other namespace usage, failures and termination delays. Its `full_surge_fits` result is a budget calculation, not a promise of rollout progress. Synthetic accounting rows and an explicit output-verification flag illustrate separate evidence; they are not a live Slurm query or a complete accounting parser.

## Integrated scenarios

### Scenario 1: Post-update nodes cannot join workloads

After a BCM image/driver update, several nodes appear healthy in Base View but Slurm marks them unavailable and GPU containers fail. Preserve versions and change scope; compare category/image and booted runtime to a good node; check daemon/GRES definition, driver/toolkit/device visibility and Fabric Manager compatibility; run safe acceptance diagnostics and a minimal NGC workload. Correct the desired image/category, validate, return one canary node, then roll out. Do not resume nodes solely because their power state is green.

### Scenario 2: Kubernetes inference misses latency SLO

Pods are ready and GPU utilization is high, but tail latency regresses after teams share the cluster. Correlate request, queue, pod, allocation, DCGM, CPU, memory, network and model-load signals. Verify Run:ai policy and GPU/MIG profile, placement and interference; compare full-GPU versus supported partition/batch/concurrency variants. Retain the configuration that meets quality, latency and isolation with headroom; document rollback and capacity trigger.

### Scenario 3: Multi-node training intermittently hangs

One Slurm job hangs during collectives and later checkpoint writes. Use per-rank logs, job allocation/topology, DCGM, NVLink/fabric counters, storage client/server and system journals on a common timeline. Reproduce with approved component tests in drained nodes. Isolate a degraded link, node, rank or storage boundary; quarantine and escalate rather than masking the fault with unlimited retries. Prove recovery with collective and end-to-end baselines plus checkpoint restore.

## Hands-on performance labs

These eight activities are **proposed**, with author-estimated study time. Only the separate local workbook above was executed. Use a disposable training environment or systems specifically authorized for practice. Time each activity, preserve command/output evidence, and reset to a known state.

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
   **Answer:** Identify BCM desired configuration, scheduler allocation, Kubernetes reconciliation and each runtime observer separately before changing state.
2. Can you inventory hardware through firmware, image and workload ownership?
   **Answer:** Record stable node/GPU identity, topology, firmware, image/driver/runtime versions, resource pools and business owners.
3. How do BCM categories, software images, nodes and exceptions relate?
   **Answer:** A regular node has one category; images can serve multiple categories, node settings can differ, and Boolean/role-priority rules require separate interpretation.
4. Can you trace a failed provision without immediately reimaging?
   **Answer:** Trace management reachability, boot source, image availability, disk/network setup and registration; preserve installer logs before a destructive reprovision.
5. What must a Base View health/performance report prove?
   **Answer:** A report needs timestamped identity, expected state, workload impact, supporting signals and unresolved discrepancies, not just a green status.
6. How do user, project, scheduler and Kubernetes permissions connect?
   **Answer:** Trace authenticated identity through groups, project/RBAC, scheduler account/QOS and storage/registry permissions; each boundary has its own policy.
7. Can you verify effective access without granting broad privilege?
   **Answer:** Use scoped read-only access checks and an authorized minimal workload; successful login alone does not prove resource or data authorization.
8. Which management, BMC, compute and storage paths must be checked?
   **Answer:** Check logical management, out-of-band, compute and storage paths, including DNS/time, addresses, topology and failure domains.
9. How do host and DPU Arm execution targets differ?
   **Answer:** DPU Arm services execute on a different processor/runtime target; match mode, firmware, DOCA stack and artifact architecture.
10. What dependency evidence precedes firmware or driver changes?
   **Answer:** Record a supported current/target dependency set, workload impact, recovery artifact and acceptance conditions before a change.
11. Can you execute a canary, validation, batch rollout and rollback?
   **Answer:** Use a representative authorized node, preserve baseline, verify workload recovery, expand in bounded batches and stop or roll back on failures.
12. What must be verified after installing Slurm through BCM?
   **Answer:** Verify controller/compute/accounting daemons, authentication, node/GRES definitions, allocation and a small job with accounting output.
13. What must be verified after initializing Kubernetes through BCM?
   **Answer:** Verify control plane, workers, CNI/CSI, device advertisement, policy and a representative workload; installation completion is insufficient.
14. What must be verified after installing Run:ai?
   **Answer:** Verify the exact platform version, cluster connection, roles, projects, quota boundaries and an authorized workload; distinguish policy from hardware.
15. Can you interpret `sinfo`, `squeue`, `sacct` and `scontrol` evidence?
   **Answer:** Use partition/node state, queue reasons, job/step accounting and detailed controller state together; batch zero exit can hide failed steps.
16. Why is a job pending, and which layer owns the reason?
   **Answer:** Locate the reason in policy, resources, placement, node health or runtime; one observed reason need not describe every outstanding constraint.
17. When is it safe to return a drained Slurm node?
   **Answer:** After the root cause is corrected and health plus workload acceptance passes under authorized recovery; BCM closed state is not scheduler drain.
18. Can you diagnose common Kubernetes pod states from events first?
   **Answer:** Follow scheduling, image retrieval, mount/network, process start and readiness events to find the first failed dependency.
19. How do GPU Operator, device plugin and resource requests connect?
   **Answer:** The driver and device plugin make supported resources available; Pods request them through documented matching request/limit semantics.
20. Can you trace a Run:ai workload through Kubernetes to the device?
   **Answer:** Join workload/project, pod UID, placement and device identity with a common timeline rather than comparing unrelated dashboards.
21. How do quota, borrowing, priority and preemption affect teams?
   **Answer:** Quota defines policy boundaries, borrowing uses eligible spare resources, rank/priority affect ordering and preemption requires checkpoint or service recovery.
22. What are the support, drain and profile steps for MIG change?
   **Answer:** Confirm exact supported GPU/driver/profile, drain work, use the authoritative manager and validate advertisement and workloads before return to service.
23. How do MIG, vGPU, passthrough and time slicing differ?
   **Answer:** MIG partitions supported hardware, vGPU uses its virtual stack, passthrough assigns hardware and time slicing shares execution with different isolation.
24. Can you identify hidden architecture single points of failure?
   **Answer:** Map dependencies such as DNS, time, registry, shared storage and controllers; redundant GPUs do not remove these failure domains.
25. Can you select and pin an authorized NGC artifact and digest?
   **Answer:** Choose a supported entitled artifact, verify provenance and record an immutable digest with the tested environment; never copy tokens into examples.
26. How do registry, runtime, device and application failures differ?
   **Answer:** Separate retrieval/authentication from container runtime/device setup and then model/application behavior. A successful pull proves no GPU access.
27. Can you submit a reproducible single- and multi-node Slurm job?
   **Answer:** State versions, resources, placement, launcher, data/checkpoint paths and output; verify every participating rank and retain job/step evidence.
28. Which signals prove distributed training scales productively?
   **Answer:** Compare useful throughput, completion time, communication, checkpoints and failures across repeatable baselines, not only allocated GPU count.
29. Can you deploy inference with meaningful readiness and rollback?
   **Answer:** Tie readiness to serving ability, include cold loading and failure recovery, and preserve model/image/configuration rollback artifacts.
30. Why might autoscaling fail to solve latency?
   **Answer:** Quota, compatible GPUs, shared storage, queueing or loading can remain the bottleneck; extra desired replicas do not create capacity.
31. Can you allocate resources with an explicit business policy?
   **Answer:** Define owners, guaranteed and burst policy, preemptibility, service targets, accounting and exceptions before tuning placement.
32. How do Slurm, Kubernetes and Run:ai quota semantics differ?
   **Answer:** Kubernetes quota constrains namespace admission; Slurm and Run:ai add different scheduler/account and hierarchical policy semantics. None alone proves usable capacity.
33. Can you correlate app, scheduler, container, GPU, fabric and storage time?
   **Answer:** Use synchronized clocks and stable workload/node/device IDs; separate observation time from event time and preserve missing evidence.
34. What is the smallest discriminating check for a Docker failure?
   **Answer:** Locate the failing stage using the exact error and pinned environment; inspect permission, mount, injection and runtime state before broad changes.
35. What evidence distinguishes NGC auth, tag and compatibility failure?
   **Answer:** Keep redacted pull errors, repository/digest, entitlement and runtime/driver facts; distinguish an unavailable artifact from an incompatible successful pull.
36. When is Fabric Manager required, and why is restart risky?
   **Answer:** Consult the exact NVSwitch system and driver requirements; changing its management service can disrupt communication for running work.
37. Can you separate intra-node NVLink from inter-node fabric issues?
   **Answer:** Use local GPU/NVSwitch topology separately from network interfaces and inter-node fabric; collectives can also fail from a rank or storage dependency.
38. How do you compare BCM desired state with node runtime?
   **Answer:** Compare category/image, overrides and role priorities with the booted node, effective services and workload result; reconcile at the owning control plane.
39. Which Magnum IO component and path is actually involved?
   **Answer:** Name NCCL, GPUDirect RDMA, GPUDirect Storage or another specific component and trace the actual data path and compatibility.
40. Can you diagnose storage capacity, metadata and throughput separately?
   **Answer:** Capacity/inodes, metadata operations and sustained throughput are distinct constraints; verify checkpoint correctness and restore, not just write speed.
41. What makes a benchmark safe, representative and reproducible?
   **Answer:** Use authorized isolated data/load, fixed versions and inputs, known measurement limits, repeated runs and cleanup/recovery criteria.
42. Can you define outcome, baseline, hypothesis and rollback for tuning?
   **Answer:** Specify a measurable objective and baseline, change one justified factor and retain errors/quality plus rollback evidence.
43. Why can high utilization still represent poor performance?
   **Answer:** Busy devices can repeat failed work, wait inefficiently or serve poor tail latency. Measure useful service or job outcomes.
44. Can you complete each scenario without risky shortcut commands?
   **Answer:** Write the discriminating check, authorized correction and recovery proof first; do not substitute resets or broad privilege for diagnosis.
45. Can you produce all eight evidence packs in a resettable lab?
   **Answer:** The workbook is local evidence only. All eight infrastructure packs need an authorized resettable environment and remain unexecuted here.
46. Can you complete three fresh tasks inside the 120-minute budget?
   **Answer:** Practice three original tasks with verification inside a shared time budget; this is not proof of access to or replication of the vendor lab.
47. Do your notes preserve exact IDs, versions, times, commands and results?
   **Answer:** Record IDs, versions, timestamps, sanitized commands, observed output and interpretation separately so another operator can reproduce the reasoning.
48. Have you rechecked the live blueprint, lab contract and exam policy?
   **Answer:** Use the canonical current page and disclose the conflicting PDF and training listings. Obtain vendor clarification rather than assuming the conflicting weights or score-report details.


### Check key

- **Ready:** You can administer and diagnose BCM, Slurm, Kubernetes, Run:ai, containers, GPU/fabric and storage in a resettable lab, with verification and rollback.
- **Review:** You know commands and product names but cannot choose the safest evidence path or complete tasks inside the time budget.
- **Gap:** You would experiment on production, force state without root cause, or treat a green dashboard/high utilization as proof. Return to the labs and operator loop.

## Places to learn

This is not a complete list. Select public references for the specific platform and weak areas in your practice. Metadata was checked September 29, 2026; paid interiors, lab access and checkout were not tested. Times are author estimates except explicitly listed vendor runtimes.

| Resource | Access | Estimated time |
|---|---|---|
| [NCP-AIO certification and blueprint](https://www.nvidia.com/en-us/learn/certification/ai-operations-professional/) | Public canonical scope; 30 questions plus three labs in 120m, USD 500 | 2–4h mapping |
| [Linked exam study guide](https://dam-cdn.nvd.orangelogic.com/AssetLink/ub08c12vdc5l53ksln5d4dlpt3346464.pdf) | Public 7-page PDF; conflicts with canonical weights/scope and has an extraneous contents entry | 1–2h comparison; do not use as replacement blueprint |
| [Certification policies](https://www.nvidia.com/en-us/learn/certification/) | Public; pass/fail, retake, renewal and remote procedures | 30–45m |
| [Earlier professional workshop outline URL](https://academy.nvidia.com/en/wp-content/uploads/2026/01/AI-Operations-Outline-2026.pdf) | Now redirects to generic Academy HTML; earlier four 5h sessions not reverified | Current outline runtime unverified |
| [DGX learning path](https://www.nvidia.com/en-us/learn/learning-path/dgx-data-center/) | Public mixed-access index; professional course card lists USD 3000/24h. Exam card lists USD 400/1.5h versus canonical USD 500/2h | Listed 24h workshop; additional practice varies |
| [AI Infrastructure and Operations Fundamentals](https://www.nvidia.com/en-us/training/academy/course-detail/?id=course:15139841) | Paid/account course shell; 7h remains listed on canonical/path pages, not verified lesson access | Listed 7h; associate refresher only |
| [BCM documentation portal](https://docs.nvidia.com/base-command-manager/) | Public; select major version and manual | 1–2h selection |
| [BCM 11 administrator manual](https://docs.nvidia.com/base-command-manager/manuals/11/admin-manual.pdf) | Public 1094-page PDF; selected concepts and running-node update sections reviewed | 12–24h selected reading plus proposed lab |
| [BCM 11 release index](https://docs.nvidia.com/base-command-manager/bcm-11-release-notes) | Public version navigation | 30m |
| [BCM 11.34.0 changes](https://docs.nvidia.com/base-command-manager/bcm-11-release-notes/bcm11-34-0.html) | Public September 11, 2026 release; selected operations changes reviewed | 1–2h relevant-version review |
| [Slurm documentation](https://slurm.schedmd.com/documentation.html) | Public; current index 26.05, choose installed version | 8–16h selected reading |
| [Slurm GRES](https://slurm.schedmd.com/gres.html) | Public; discovery, allocation, accounting and pre-partitioned MIG | 2–4h selected sections |
| [Slurm exit codes](https://slurm.schedmd.com/job_exit_code.html) | Public; script/step/signal/derived evidence | 1–2h plus workbook |
| [Kubernetes resource-management index](https://kubernetes.io/docs/concepts/resource-management/) | Public navigation; new DRA routes do not replace all legacy resource guidance | 30–60m |
| [GPU scheduling](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/) | Public device-plugin resource semantics | 1–2h |
| [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) | Public; rollout allowances, progress and termination behavior | 2–3h selected sections |
| [Resource quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/) | Public; namespace admission and extended-resource limits | 1–2h selected sections |
| [Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/) | Public; local composition/patching distinct from cluster apply | 1–2h plus workbook |
| [Run:ai documentation](https://docs.nvidia.com/run-ai/index.html) | Public split between SaaS and self-hosted routes | 30m |
| [Self-hosted Run:ai](https://docs.nvidia.com/run-ai/self-hosted/index.html) | Public index; align with deployed version | 1–2h selection |
| [Run:ai scheduling concepts](https://run-ai-docs.nvidia.com/self-hosted/platform-management/runai-scheduler/scheduling/concepts-and-principles) | Public; hierarchical quota, rank, preemption and placement | 2–4h |
| [DCGM documentation](https://docs.nvidia.com/datacenter/dcgm/latest/contents.html) | Public entry point; match fields and diagnostics to supported environment | 4–8h selected reading |
| [Container Toolkit troubleshooting](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/troubleshooting.html) | Public; injection mode, cgroups, permissions and security tradeoffs | 2–4h |
| [Triton documentation portal](https://docs.nvidia.com/deeplearning/triton-inference-server/index.html) | Public latest/archive links; portal also contains old release prose, so verify the selected artifact/version | 4–8h selected reading |

Original tasks should require evidence, correction, verification and recovery. Memorized answers do not establish Linux or cluster fluency. Avoid recalled exam items, dumps and guaranteed-pass material.
