---
exam_code: NCA-AIIO
vendor_id: nvidia
official_blueprint: https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# NVIDIA-Certified Associate: AI Infrastructure and Operations (NCA-AIIO) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** All 22 public objectives, the six-page study guide, delivery details and selected operations documentation were reviewed September 29, 2026. The local workbook passed 34 checks; eight infrastructure activities remain proposed. See the [deep-review report](../docs/research/2026-09-29-nca-aiio-deep-review.md). See the [coverage record](../docs/SOURCE-VALIDATION.md#nca-aiio-coverage-record).

**Current baseline:** NCA-AIIO is an active, English, remotely proctored associate exam with 50 questions in one hour. The certification page lists USD 125; the separate DGX learning-path card displayed USD 135 when checked. Treat the certification page as the exam authority and verify the Certiverse checkout total before purchase.<br>
**Upcoming change:** No revision or retirement announcement was present on the checked certification page September 29, 2026.<br>
**Prerequisite:** The certification page lists basic data-center knowledge. The linked study guide recommends a relevant degree and enterprise experience; it does not label these as mandatory admission requirements. Its training is explicitly optional.<br>
**Validity:** NVIDIA says the credential is valid for two years and can be renewed by retaking the exam. Recheck policy, price and supported delivery before registration.

**VERIFY CURRENT — exam policy:** NVIDIA reports pass/fail without a score. Its public FAQ specifies a 14-day retake wait, at most five attempts in a 12-month period beginning with the first exam purchase, and no breaks for remotely proctored exams. Check the individual booking, identity and accommodation requirements before registering; no booking or secure-browser installation was performed for this review. [Program policies](https://www.nvidia.com/en-us/learn/certification/).

## How to use this guide

Study the infrastructure as one evidence-bearing path: workload requirement → compute and memory behavior → server/GPU topology → network and storage movement → facility capacity → supported software stack → scheduler/orchestrator allocation → telemetry and diagnosis → safe change or escalation. Do not turn this into a catalog-name exercise. For each choice, explain the constraint it solves, the signal that validates it, and the failure it could introduce.

Use read-only inspection, simulators, documentation and hardware you are authorized to operate. Never run stress, reset, firmware, fabric or partitioning commands on shared/production equipment without approval, a maintenance plan and rollback.

> **About related items:** A `Related item:` callout adds prerequisite, architectural or operational context. It supports the topic but does not assert that NVIDIA used the wording in the public blueprint.

## Blueprint map

**CURRENT BLUEPRINT:** The website and [official study guide PDF](https://dam-cdn.nvd.orangelogic.com/AssetLink/x874j05hy3m3r2sor84kpvp70750m468.pdf) agree on eight knowledge topics, ten infrastructure topics and four operations topics. The PDF carries a January 2026 production mark; that mark alone does not establish an exam transition date. The monitored objective and lifecycle snapshots are unchanged.

| Topic area | Weight | Evidence to produce |
|---|---:|---|
| Essential AI Knowledge | 38% | Workload-to-stack map; AI/ML/DL and CPU/GPU reasoning; training/inference comparison; NVIDIA solution selection |
| AI Infrastructure | 40% | Compute, memory, topology, network, storage, power/cooling and on-premises/cloud decision record |
| AI Operations | 22% | Management, scheduling/orchestration, GPU-health telemetry and virtualization/partitioning operations runbook |

## 1. Essential AI Knowledge — 38%

### 1.1 AI, machine learning and deep learning

Artificial intelligence is the broad goal of systems performing tasks associated with intelligent behavior. Machine learning learns patterns from examples rather than encoding every rule. Deep learning uses layered neural networks and benefits from parallel tensor/matrix computation. Generative AI produces new content; it is one workload family, not a synonym for every AI system.

Supervised learning uses labeled examples, unsupervised learning discovers structure without target labels, and reinforcement learning learns from action/reward interaction. Training changes model parameters. Validation supports selection and tuning. Testing estimates behavior on held-out data. Inference applies a trained model to new input. Keep these stages separate because their infrastructure profiles differ.

### 1.2 Why GPUs accelerate AI

A CPU has a small number of sophisticated cores optimized for varied, latency-sensitive control flow. A GPU has many execution units designed for high-throughput parallel work. Neural-network training and inference contain large amounts of matrix/tensor arithmetic that can be divided across GPU resources. That does not make every workload GPU-bound: preprocessing, control-plane work, serialization, networking and storage can remain CPU or I/O constrained.

Know the roles, not transistor trivia:

- CUDA provides the programming platform and software interface for general-purpose NVIDIA GPU computing.
- CUDA cores perform general parallel arithmetic; Tensor Cores accelerate supported matrix operations used heavily in AI.
- GPU high-bandwidth memory holds model parameters, activations, optimizer state and working data. Capacity can be as important as raw compute.
- PCIe connects devices to the host; NVLink and NVSwitch provide higher-bandwidth GPU/CPU or GPU/GPU paths in supported topologies.
- NCCL provides topology-aware collective communication primitives such as all-reduce for multi-GPU work.
- GPUDirect technologies can reduce data-path copies and CPU involvement between GPUs, networks or storage on supported systems.

`Related item:` **Arithmetic intensity and bottlenecks.** A fast accelerator can wait on data. Ask whether the limiting resource is compute, device memory, interconnect, network, storage, CPU preprocessing or power/thermal headroom before recommending more GPUs.

### 1.3 Training and inference are different systems

Training usually emphasizes sustained throughput, large memory capacity, checkpoint durability and efficient collective communication over multiple GPUs/nodes. A failed long-running job can waste substantial time and compute. Inference often emphasizes request latency, concurrency, availability, predictable tail behavior and cost per useful response. Batch inference can resemble throughput-oriented training operations; interactive inference cannot.

Write a requirement sheet with model/data size, precision, batch/concurrency, latency or completion target, availability, privacy, locality, checkpoint/recovery point, growth and budget. Only then select hardware and topology. More GPUs help only if the work parallelizes and communication/data feeding keep them productive.

### 1.4 NVIDIA software and solution stack

Reason in layers:

1. **System and firmware:** DGX/HGX or certified systems, CPU, GPU, DPU, memory, local storage, NIC/HCA, BMC and fabric components.
2. **Operating system and driver:** supported Linux/DGX OS or cloud image, NVIDIA driver, Fabric Manager where required, and compatibility with the CUDA runtime.
3. **Acceleration libraries/frameworks:** CUDA plus workload libraries such as cuDNN and NCCL; optimized PyTorch/TensorFlow and other framework containers.
4. **Packaging/catalog:** NVIDIA Container Toolkit connects containers to GPUs; NGC distributes supported containers, models, Helm charts and artifacts.
5. **Optimization/serving:** TensorRT optimizes supported inference graphs; Triton Inference Server serves models with batching, concurrency and metrics; NIM packages supported inference microservices.
6. **Cluster operations:** Kubernetes and GPU Operator for cloud-native resource lifecycle; Slurm for queued batch/HPC scheduling; Base Command Manager for provisioning and managing AI/HPC clusters; DCGM and exporters for GPU telemetry/health.
7. **Enterprise/platform layer:** NVIDIA AI Enterprise supplies an enterprise-supported software suite; DGX, BasePOD and SuperPOD describe progressively broader validated system/platform patterns.

Do not claim that one named product is mandatory for every environment. Select by required support, scale, lifecycle ownership, workload shape and existing platform.

`Related item:` **Compatibility matrix.** Driver, CUDA runtime, framework/container, GPU architecture, operator and orchestration versions form a contract. “Latest” is not evidence of compatibility; record tested versions and consult current support matrices.

### 1.5 Use cases and adoption drivers

AI workloads span computer vision, natural-language processing, recommendations, forecasting, simulation, scientific computing, robotics and generative systems. Recent adoption reflects larger datasets/models, improved algorithms, accelerator performance, mature frameworks, cloud access and deployable pretrained models. Map each use case to an outcome and risk, not just a model: a diagnostic aid, safety controller and marketing assistant have different accuracy, latency, availability and governance requirements.

## 2. AI Infrastructure — 40%

### 2.1 Size from the workload

Start with the work rather than a preferred system. Estimate model plus runtime memory, training activations/optimizer state or inference key/value cache, batch/concurrency, data rate, checkpoint volume and communication. Choose precision and parallelism deliberately. Data, tensor, pipeline and expert parallelism distribute different parts of the work and impose different communication patterns.

Scaling has three boundaries:

- **Scale up:** faster/larger GPUs and stronger intra-node topology reduce coordination distance but have a ceiling.
- **Scale out:** more nodes add capacity but require a low-latency, high-bandwidth fabric, efficient collectives and operational consistency.
- **Share/partition:** MIG, vGPU, time slicing or scheduler allocation can improve utilization, but isolation, compatibility, performance predictability and licensing differ.

Capacity planning uses productive work, not installed accelerator count. Track queue time, job completion, useful tokens/samples, utilization, memory headroom, communication ratio, failures and energy/cost.

### 2.2 Node and cluster components

An accelerated node combines CPUs, system RAM, GPUs, local storage, power/cooling, management controller and network adapters. GPU locality matters: which GPUs share NVLink/NVSwitch paths, PCIe switches or CPU NUMA domains changes communication performance. At cluster level, separate logically:

- compute fabric for distributed workload traffic;
- storage/data path for datasets and checkpoints;
- management/in-band and out-of-band paths for provisioning and recovery;
- client/service network for user and inference access.

The physical design also needs racks, power distribution, cooling, structured cabling, service clearance, fire protection, physical security and supported environmental ranges. Facility capacity is part of architecture, not a late installation task.

`Related item:` **Failure domains.** A rack, top-of-rack switch, power feed, cooling loop or shared storage service can fail many nodes together. Availability estimates must model correlated failures, spares, replacement time and degraded-capacity operation.

### 2.3 Power and cooling

Use vendor system specifications and qualified designs for actual deployment. Conceptually distinguish nameplate capacity, expected draw, transient peaks and usable circuit/cooling headroom. Power effectiveness and heat removal constrain density. Air cooling may be suitable at one rack density while direct liquid cooling or different facility design is required at another.

Document utility/feed redundancy, UPS/generator intent, PDU capacity, voltage/current, rack density, airflow/liquid distribution, temperature/leak monitoring and emergency procedure. Do not extrapolate one server’s thermal design across a rack without engineering review.

### 2.4 Network and data movement

Ethernet is the common general-purpose data-center network and supports routed/switched management, storage and workload traffic. InfiniBand is widely used for low-latency, high-throughput HPC/AI fabrics. RoCE carries RDMA over a configured Ethernet fabric. RDMA lets supported endpoints access remote memory with less CPU/kernel involvement; GPUDirect RDMA can connect the network path more directly to GPU memory.

Know the purpose of:

- NIC versus HCA and their supported fabric/protocol;
- switches, leaf/spine topology, link aggregation and redundant paths;
- bandwidth, latency, jitter, oversubscription and congestion/loss behavior;
- MTU consistency, routing, addressing, DNS/NTP and management reachability;
- optics/cables/transceivers and end-to-end qualification;
- telemetry counters, errors, drops, retransmission and link health.

A DPU offloads and accelerates infrastructure functions such as networking, security and storage in supported architectures, helping isolate or free host CPU work. It is not a universal replacement for CPUs or switches.

`Related item:` **Collective communication.** Distributed training can synchronize frequently. An apparently healthy network can still be poorly matched to all-reduce patterns because of topology, congestion, rail mapping or a single degraded link.

### 2.5 Storage and data path

AI storage must supply datasets, write checkpoints and retain artifacts at the required concurrency. Consider capacity, aggregate and per-client throughput, metadata performance, small-versus-large files, caching/local NVMe, parallel/object/file access, durability, replication, backup and recovery. GPUDirect Storage can shorten supported GPU/storage paths, but end-to-end hardware/software compatibility is required.

Protect data provenance and permissions. High throughput does not justify copying sensitive training data into unmanaged scratch space. Measure stage-in time, accelerator starvation, checkpoint duration, restore time and data errors.

**PRACTICAL DEPTH — checkpoint budget:** In an original planning example, eight workers each write 40 GiB within 80 seconds. The aggregate payload target is 320 GiB / 80 s = 4 GiB/s, before protocol, metadata, contention and durability overhead. A nominal 4 GiB/s device specification provides no margin and does not demonstrate a successful concurrent checkpoint or restore. Measure the entire path and retain a recovery result. NVIDIA's [January 2023 storage article](https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing/) explains why capacity growth, throughput and maintenance availability need separate planning. Its general recommendations and examples are not current hardware sizing guarantees.

### 2.6 On-premises, cloud and hybrid

On-premises infrastructure can offer locality, control, predictable reserved capacity and deep topology choices but requires capital, facility lead time, lifecycle skills and spare capacity. Cloud can accelerate access, elasticity and geographic choice but introduces service quotas, egress/data-gravity, instance availability, shared-responsibility and ongoing-cost considerations. Colocation/managed and hybrid patterns split those tradeoffs.

Compare options against workload duration and variability, data location, regulation, latency, reservation/queue behavior, staff capability, refresh cycle, disaster recovery, support and full cost. Portability is not automatic: images, identity, networking, storage, scheduler, observability and data-transfer behavior all need design.

## 3. AI Operations — 22%

### 3.1 Provision and manage as a lifecycle

Maintain an inventory from facility/rack to system, BMC, NIC/HCA, GPU UUID, firmware, OS/kernel, driver, CUDA/container runtime and orchestration labels. Use supported, versioned images and configuration control. Validate burn-in and acceptance before production; preserve serials, topology, baseline diagnostics and support entitlement.

Changes need dependency checks, maintenance windows, workload drain, backups/config export, staged rollout, validation and rollback. Firmware, driver and operator upgrades are connected changes. A successful package install does not prove that CUDA applications, collectives, monitoring and schedulers still work.

**VERIFY CURRENT — release behavior:** The checked [GPU Operator release notes](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/release-notes.html) list 26.7.1. They describe an operand-startup fix that waits for driver validation, plus a known H100 issue when moving from driver 595.91.07 to 615.71.09 before subsequent MIG reconfiguration. Treat this as a reason to read the exact upgrade path and recovery procedure; it is not a recommendation to change this machine. The preceding 26.7.0 notes introduce a `GPUCluster`/DRA route that cannot coexist with `ClusterPolicy` in one cluster and has separate prerequisites. Do not transplant an older installation recipe into that route.

### 3.2 Scheduling and orchestration

Slurm schedules queued jobs across nodes and resources, fitting batch/HPC and training work. Kubernetes reconciles desired state for containerized services and jobs; the NVIDIA GPU Operator automates driver/toolkit/device-plugin/feature-discovery/MIG/DCGM components in supported clusters. Either can support multiple workload types; choose based on platform contract rather than slogans.

Resource requests must reflect GPUs or MIG devices, CPU, memory, storage, network/topology and time. Queues/partitions, quotas, priorities, preemption and reservations balance fairness with business priority. Node labels/taints or constraints can place work on compatible GPU/topology pools. Record why a workload is pending, evicted, preempted or underutilized.

`Related item:` **Gang scheduling and topology awareness.** A distributed job may need all workers at once and benefit from placement within a high-bandwidth locality. Allocating scattered or partial resources can waste capacity or cause timeout.

### 3.3 Monitor GPUs and systems

`nvidia-smi` is useful for local identification and read-only status. DCGM provides cluster-oriented observation, health, diagnostics and integration; DCGM Exporter exposes metrics to monitoring systems such as Prometheus. Base Command Manager or other management platforms add fleet provisioning and operations. Use current documentation for exact commands and field meanings.

Observe multiple layers:

- GPU presence, driver state, utilization and memory allocation;
- temperature, power, clocks and throttling reasons;
- ECC and other error/event counters, Xid events and health policy;
- PCIe/NVLink/fabric traffic and errors;
- CPU, RAM, disk, network, filesystem and BMC/facility health;
- scheduler queue, job failure/retry and productive throughput;
- inference latency/throughput/error and model-level quality where applicable.

High utilization is not automatically good, and low utilization is not automatically bad. Correlate telemetry with workload phase, baseline, topology and service outcome. A GPU can be busy doing inefficient work; a latency service can be healthy with deliberate headroom.

**PRACTICAL DEPTH — telemetry contract:** Identify the field ID, type, unit, entity, timestamp and collection status before interpreting a value. DCGM field 203 reports GPU utilization as an integer percentage; field 1613 reports a floating-point ratio. Thus 80 and 0.8 can describe the same observation. Memory field 252 reports MiB; 1627 reports bytes. They are distinct fields with different contracts. Check typed blank/unsupported values before arithmetic; an unavailable field is not evidence of zero activity. The local workbook models that boundary with explicit status values. [DCGM field definitions](https://docs.nvidia.com/datacenter/dcgm/latest/reference/field-identifiers.html).

The [Exporter reference](https://docs.nvidia.com/datacenter/dcgm/latest/reference/dcgm-exporter-metrics.html) distinguishes field metrics from exporter-owned counts. `DCGM_FI_DEV_XID_ERRORS` is a gauge representing an error code, so a numeric increase is not an incident count. Windowed Xid sample counts and cumulative observed records have different meanings; collection cadence, initialization and resets matter. Configuration does not guarantee runtime field support. Record exporter/DCGM versions together and distinguish physical GPU, MIG instance and workload labels before aggregating.

### 3.4 Diagnose and escalate safely

Use an evidence order: define impact and affected scope; check recent change and maintenance; inspect scheduler/service state; verify node/GPU visibility; compare health, thermal/power and error signals; inspect network/storage paths; reproduce only in an authorized safe way; drain/quarantine if needed; then collect the vendor support bundle.

Do not reset a GPU, restart a driver, change MIG mode or run intensive diagnostics simply because a command exists. These actions can terminate workloads or affect the node. Record timestamps, job/node/GPU IDs, versions, logs, topology, commands, results and recovery.

### 3.5 Virtualization and GPU sharing

GPU passthrough assigns a physical GPU to a VM with strong performance and simple workload visibility but coarse allocation. NVIDIA vGPU shares supported GPUs among VMs under a supported virtualization/licensing stack. MIG partitions supported GPUs into isolated GPU instances with dedicated compute and memory resources. Time slicing increases concurrency without MIG’s hardware partition characteristics.

Select using workload size, isolation, determinism, density, platform, live-migration/support needs and licensing. Validate that the GPU, driver, hypervisor/container platform and workload support the chosen mode. Partitioning improves utilization only when profiles match actual memory/compute needs and fragmentation is managed.

**PRACTICAL DEPTH — allocation is not capacity:** [Time-slicing documentation](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html) states that replicas do not provide MIG-style memory or fault isolation. Requesting multiple replicas does not promise proportional compute. The optional `failRequestsGreaterThanOne` admission rule can reject such requests, but it does not create a compute quota. DCGM Exporter cannot associate metrics with containers under the documented device-plugin time-slicing configuration. The Operator also does not automatically monitor changes to its time-slicing ConfigMap. Verify the documented update path and outcome in an authorized environment.

[MIG concepts](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/concepts.html) distinguish a GPU instance (GI) from its compute instances (CIs): CIs within the same GI share that GI's memory and engines. Counting the same GI memory once per CI invents capacity. Physical GPU totals, allocated GI capacity and logical replica counts are different accounting levels. Actual profiles and legal placement depend on the GPU and driver; the synthetic numbers below are not supported-profile specifications. [Deployment considerations](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/deployment-considerations.html) also distinguish GPU generations and disruptive mode changes. Use current matrices and the full procedure for an actual deployment.

## Executed local telemetry and capacity workbook

This original standard-library Python example parses synthetic JSON and checks normalization, stale/unknown values, entity scope and duplicate capacity. Run it as a normal Python script. It writes no files and calls no GPU, network, cluster or cloud service. `None` means the example cannot report a usable measurement. A real collector must translate DCGM's typed blank/error values first; this is neither a DCGM binding nor a Prometheus parser.

```python
import copy
import json
import math

# Original synthetic records, not a DCGM or Prometheus wire format.
# An upstream collector must first translate typed DCGM blank/error values.
CONTRACT = {
    203: ("gpu_utilization", "percent", 0.01, 100, {"GPU"}, int),
    1613: ("gpu_utilization", "ratio", 1, 1, {"GPU"}, float),
    252: ("memory_used", "MiB", 1048576, None, {"GPU", "GI", "CI"}, int),
    1627: ("memory_used", "bytes", 1, None, {"GPU", "GI", "CI"}, int),
}


def normalize(record, now=1000, max_age=30):
    if type(record["field_id"]) is not int:
        raise ValueError("field ID must be an integer")
    if record["field_id"] not in CONTRACT:
        raise ValueError("unknown field contract")
    name, unit, scale, ceiling, entities, kind = CONTRACT[record["field_id"]]
    if record["entity"] not in entities or not record["entity_id"]:
        raise ValueError("wrong entity scope or missing identity")
    if record["unit"] != unit:
        raise ValueError("unit does not match field ID")
    timestamp = record["timestamp"]
    if type(timestamp) is not int or timestamp > now:
        raise ValueError("invalid or future timestamp")
    status = record["status"]
    if status not in {"valid", "unsupported", "blank", "error"}:
        raise ValueError("unknown collection status")
    if status != "valid" or now - timestamp > max_age:
        return None
    value = record["value"]
    valid_type = type(value) is int if kind is int else type(value) in {int, float}
    if not valid_type or not math.isfinite(value) or value < 0:
        raise ValueError("invalid numeric value")
    if ceiling is not None and value > ceiling:
        raise ValueError("outside field range")
    return (name, record["entity"], record["entity_id"], value * scale)


def unique_capacity(rows):
    # Each row must represent one already identified physical GPU or one GI.
    # Caller keeps those two levels separate; never add a parent and its children.
    if len({row["level"] for row in rows}) > 1:
        raise ValueError("mixed accounting levels")
    capacities = {}
    for row in rows:
        level = row["level"]
        if level not in {"GPU", "GI"}:
            raise ValueError("unsupported accounting level")
        key = (row["gpu_uuid"], row.get("gi_id") if level == "GI" else None)
        memory = row["memory_mib"]
        if not key[0] or (level == "GI" and key[1] is None):
            raise ValueError("missing identity")
        if type(memory) is not int or memory <= 0:
            raise ValueError("invalid capacity")
        if key in capacities and capacities[key] != memory:
            raise ValueError("conflicting inventory for one entity")
        capacities[key] = memory
    return sum(capacities.values())


passed = 0


def check(condition):
    global passed
    assert condition
    passed += 1


def rejects(fn, value):
    try:
        fn(value)
    except ValueError:
        check(True)
    else:
        raise AssertionError("expected invalid fixture to be rejected")


raw = '''[
 {"field_id":203,"unit":"percent","entity":"GPU","entity_id":"GPU-A","timestamp":990,"status":"valid","value":80},
 {"field_id":1613,"unit":"ratio","entity":"GPU","entity_id":"GPU-A","timestamp":990,"status":"valid","value":0.8},
 {"field_id":252,"unit":"MiB","entity":"GI","entity_id":"GPU-A/GI-0","timestamp":990,"status":"valid","value":10},
 {"field_id":1627,"unit":"bytes","entity":"GI","entity_id":"GPU-A/GI-0","timestamp":990,"status":"valid","value":10485760}
]'''
samples = json.loads(raw)
check(normalize(samples[0]) == normalize(samples[1]))
check(normalize(samples[2]) == normalize(samples[3]))
base = samples[0]
check(normalize(dict(base, value=0))[-1] == 0)
check(normalize(dict(base, timestamp=970)) is not None)
check(normalize(dict(base, timestamp=969)) is None)
for status in ("unsupported", "blank", "error"):
    check(normalize(dict(base, status=status, value=9223372036854775794)) is None)
for changes in (
    {"unit": "ratio"}, {"field_id": 9999}, {"field_id": True},
    {"entity": "GI"}, {"entity_id": ""}, {"timestamp": 1001},
    {"timestamp": True}, {"status": "invented"}, {"value": True},
    {"value": -1}, {"value": 101}, {"value": 80.5},
):
    rejects(normalize, dict(base, **changes))
rejects(normalize, dict(samples[1], value=float("nan")))
rejects(normalize, dict(samples[1], value=float("inf")))
rejects(normalize, dict(samples[1], value=1.1))
check(normalize(dict(samples[1], value=1))[-1] == 1)

physical = [dict(level="GPU", gpu_uuid="GPU-A", memory_mib=65536,
                 replica=i) for i in range(8)]
check(unique_capacity(physical) == 65536)
check(sum(r["memory_mib"] for r in physical) == 524288)
instances = [dict(level="GI", gpu_uuid="GPU-A", gi_id=0,
                  ci_id=i, memory_mib=10240) for i in range(2)]
check(unique_capacity(instances) == 10240)
instances.append(dict(level="GI", gpu_uuid="GPU-A", gi_id=1,
                      ci_id=0, memory_mib=20480))
check(unique_capacity(instances) == 30720)
rejects(unique_capacity, physical + instances)
conflict = copy.deepcopy(physical)
conflict[1]["memory_mib"] = 131072
rejects(unique_capacity, conflict)
rejects(unique_capacity, [dict(instances[0], gi_id=None)])
rejects(unique_capacity, [dict(physical[0], memory_mib=True)])
rejects(unique_capacity, [dict(physical[0], level="CI")])
check(unique_capacity([]) == 0)

print(json.dumps(dict(normalized_utilization=normalize(samples[0])[-1],
                     normalized_memory_bytes=normalize(samples[2])[-1],
                     eight_replicas_physical_mib=unique_capacity(physical),
                     three_compute_instances_gi_mib=unique_capacity(instances),
                     checks=passed), sort_keys=True))
print(f"{passed} local telemetry and capacity checks passed")
```

The verified result is **34 checks passed**: utilization normalizes to 0.8 and 10 MiB to 10,485,760 bytes. Eight synthetic replicas still represent one 65,536 MiB physical GPU. Three CI records span two GIs totaling 30,720 MiB; the repeated first GI is counted once. An empty inventory returns zero only for a deliberately known empty list, not for failed discovery. The fixture trusts entity identity and collection status. It does not discover hardware, validate real MIG profiles, implement complete input validation, prove isolation or establish application performance.

## Integrated scenarios

### Scenario 1: Distributed training platform

A team needs multi-node training with large checkpoints. Translate model/data/precision and recovery objectives into per-node memory, GPU count and topology; choose a scale-out fabric and NCCL-aware validation; size parallel storage and checkpoint windows; select Slurm or another authorized scheduler; define queue fairness, topology placement, DCGM/fabric/storage telemetry and a failure-domain-aware restart test. The evidence pack includes requirement assumptions, topology/data-path diagram, compatibility matrix, collective baseline, checkpoint/restore result and rollback/escalation route.

### Scenario 2: Shared inference service

Several teams need low-latency inference but individual services underuse full GPUs. Compare full GPU, MIG, vGPU and time-slicing against memory, isolation and tail-latency needs. Build a Kubernetes design with supported GPU Operator components, placement, quota and health signals; validate batch/concurrency behavior and failure recovery. Do not call density a success if latency, errors or tenant isolation regress.

### Scenario 3: On-premises versus cloud expansion

Demand is growing faster than an existing facility. Compare facility power/cooling and procurement lead time with cloud quota, topology, storage/data movement and recurring cost. Include security/data-residency, skills, support and recovery. A justified hybrid plan may keep governed data and steady training capacity on premises while using approved cloud capacity for bursts—but only if identity, images, observability, data transfer and cost controls are tested.

Each scenario is original proposed practice. For the training case, include the checkpoint calculation and an actual restore criterion. For shared inference, explain why replica count and missing per-container telemetry cannot establish tenant isolation. For expansion, compare usable capacity after one failure with steady demand before assigning burst traffic.

## Hands-on evidence labs

These eight activities are **proposed**, with author-estimated study time. Only the separate local workbook above was executed. Use public documentation, a local simulator or authorized lab hardware. Label simulated evidence and distinguish it from measured hardware results.

1. **Workload-to-infrastructure map (3–5h):** define one training and one inference workload. Estimate memory, compute, data, latency/throughput, availability and recovery; select an infrastructure pattern and document rejected alternatives.
2. **Topology and data-path lab (3–5h):** diagram CPU/NUMA, PCIe, GPU/NVLink/NVSwitch, NIC/HCA and storage paths for a documented system. Mark likely bottlenecks and the counter/tool that would test each.
3. **Facility and capacity exercise (3–4h):** using published system specifications only, create a rack-level power/cooling/cabling/failure-domain checklist. Do not treat the exercise as a deployable electrical/mechanical design.
4. **Network/storage benchmark plan (4–6h):** define safe acceptance tests for bandwidth, latency, collective communication, storage throughput/metadata and checkpoint recovery. Specify baseline, load, success, isolation and rollback.
5. **Read-only GPU observation (3–5h):** in an authorized GPU environment, inventory versions/topology and observe workload utilization, memory, temperature, power and errors. Correlate signals to workload phases; make no disruptive changes.
6. **Scheduler/orchestrator reasoning (5–8h):** deploy a disposable Kubernetes GPU lab or model Slurm jobs. Demonstrate resource request, compatible placement, queue/pending diagnosis, failure and recovery. Capture manifests/config, events and lessons.
7. **Sharing decision (3–5h):** compare passthrough, vGPU, MIG and time slicing for three tenants. Create profile, isolation, fragmentation, licensing/support and reconfiguration criteria; optionally inspect MIG state on authorized supported hardware.
8. **Operational evidence pack (5–8h):** combine inventory, compatibility matrix, dashboard/alerts, change plan, drain/quarantine procedure, incident timeline, support bundle checklist and post-change validation for one scenario.

## Readiness checks

1. Can you distinguish AI, ML, deep learning, training and inference?
   **Answer:** AI is the broad field; ML learns patterns and deep learning uses multilayer neural models. Training updates parameters; inference applies them.
2. Why do GPUs accelerate tensor-heavy work, and when might they wait?
   **Answer:** Parallel arithmetic suits GPUs, but data loading, CPU work, memory capacity or communication can leave them waiting.
3. How do CPU, CUDA cores, Tensor Cores and GPU memory differ?
   **Answer:** The CPU handles varied control work; CUDA cores execute parallel arithmetic, Tensor Cores accelerate supported matrix operations, and device memory stores the working set.
4. What roles do PCIe, NVLink, NVSwitch, NCCL and GPUDirect play?
   **Answer:** PCIe links devices and hosts; NVLink/NVSwitch provide supported accelerator paths; NCCL implements collectives; GPUDirect shortens supported data paths.
5. How do training and interactive inference requirements differ?
   **Answer:** Training prioritizes useful throughput, synchronization and checkpoints; interactive inference also needs predictable tail latency and service availability.
6. Can you map a workload through all seven software/infrastructure layers?
   **Answer:** Trace hardware, OS/driver, libraries/frameworks, packaging, serving, cluster management and enterprise support; assign an owner and compatibility check to each.
7. What do CUDA, cuDNN, NGC, TensorRT, Triton and NIM each contribute?
   **Answer:** CUDA is the programming platform, cuDNN supports neural primitives, NGC distributes artifacts, TensorRT optimizes inference, Triton serves models, and NIM packages inference services.
8. When are DGX, HGX, BasePOD or SuperPOD patterns relevant?
   **Answer:** Use the documented system or platform pattern when its scale, validated topology and support contract match the requirement; a product name alone is not a design.
9. Why is a compatibility matrix more useful than “use latest”?
   **Answer:** Compatible supported versions form a dependency set. A newer individual component can break that set or change operational behavior.
10. What adoption drivers and AI use cases does the blueprint expect?
   **Answer:** Data, algorithms, accelerated compute and deployable tooling expand adoption; relate vision, language, recommendation and other workloads to measurable business needs.
11. Can you estimate memory, communication, storage and recovery needs?
   **Answer:** Include parameters, activations or cache, concurrency, data feeds, collective traffic, checkpoint volume and recovery targets; state assumptions before sizing.
12. How do scale-up, scale-out and sharing solve different constraints?
   **Answer:** Scale-up improves a node, scale-out distributes across nodes, and sharing divides access. Each has a different memory, communication or isolation limit.
13. Why is installed GPU count a weak capacity metric?
   **Answer:** Installed devices can be idle, fragmented, unhealthy or waiting on I/O. Count productive throughput and usable capacity under the required failure conditions.
14. How does NUMA/PCIe/GPU/NIC locality affect a workload?
   **Answer:** Crossing NUMA or slower interconnect boundaries adds movement and contention. Validate the actual CPU/GPU/NIC path under the intended workload.
15. What cluster paths should be separated or deliberately converged?
   **Answer:** Identify compute, storage, service and management paths; any convergence needs explicit capacity, isolation and recovery evidence.
16. Which correlated rack/fabric/power/storage failures matter?
   **Answer:** One rack, switch, feed, cooling loop or storage failure can affect many nodes; model correlated loss and recovery time.
17. How do nameplate, expected, transient and usable power differ?
   **Answer:** Nameplate is a rating, expected draw is workload-dependent, transient demand is brief, and usable capacity includes engineering limits and headroom.
18. When does cooling design constrain accelerator density?
   **Answer:** Density is constrained by heat removal, flow, environmental limits and redundancy. Use qualified facility design rather than a GPU-count estimate.
19. How do Ethernet, InfiniBand, RoCE, RDMA and GPUDirect relate?
   **Answer:** Ethernet and InfiniBand provide fabrics; RoCE carries RDMA on Ethernet; GPUDirect RDMA connects supported network and GPU memory paths.
20. Which bandwidth, latency, loss and congestion signals matter?
   **Answer:** Measure throughput, latency distributions, errors, drops and congestion alongside application phases; a healthy link light proves little.
21. What value can a DPU add, and what does it not replace?
   **Answer:** A DPU can offload supported network, security and storage functions. CPUs, switches and operational ownership still have roles.
22. Why can collective performance expose a hidden bad link?
   **Answer:** Synchronized workers expose the slowest path. Inspect topology and per-link evidence before assuming more aggregate bandwidth solves the problem.
23. Which storage characteristics matter beyond capacity?
   **Answer:** Throughput, metadata, concurrent checkpoint writes, latency, durability and restore behavior matter alongside storage capacity.
24. How do you protect governed data in staging and scratch paths?
   **Answer:** Apply identity, permissions, provenance, retention and cleanup to staged copies as well as source data; fast scratch space is not a governance exception.
25. Can you compare on-premises, cloud, managed and hybrid honestly?
   **Answer:** Compare locality, facility lead time, quotas, data transfer, skills, support, recovery and full cost against a specified workload.
26. What inventory/configuration data supports reproducible operations?
   **Answer:** Record serials and stable GPU identity, topology, versions, configuration, baseline measurements and change history.
27. Why are firmware, driver, CUDA and operator changes connected?
   **Answer:** The workload crosses all these layers; validate their supported combination and recovery path as a coordinated change.
28. How do Slurm scheduling and Kubernetes reconciliation differ?
   **Answer:** Slurm allocates queued batch jobs; Kubernetes reconciles containerized desired state. Both require deliberate resource and placement policies.
29. How does GPU Operator simplify—and constrain—cluster lifecycle?
   **Answer:** The Operator automates supported GPU components but introduces version, privilege, platform and upgrade constraints. Choose its supported installation route.
30. How do quota, priority, preemption and reservations affect fairness?
   **Answer:** Quota limits consumption, priority orders work, preemption interrupts it, and reservations hold capacity; evaluate starvation and business impact.
31. Why might a distributed job need gang/topology-aware placement?
   **Answer:** A distributed job may require simultaneous workers and fast locality; partial or scattered allocation can waste resources or stall it.
32. What can `nvidia-smi`, DCGM and DCGM Exporter tell you?
   **Answer:** They expose local status, managed GPU health/fields and exported metrics respectively; field support, units, identity and freshness still need verification.
33. Which GPU signals require workload and baseline context?
   **Answer:** Utilization, power, temperature, memory and errors need workload phase and baseline context. Unsupported or stale readings cannot be treated as healthy zeroes.
34. What is the safe evidence order for an incident?
   **Answer:** Establish impact, recent changes, placement, visibility and correlated evidence before escalating to controlled reproduction or disruptive recovery.
35. Which reset, diagnostic or partition actions can disrupt workloads?
   **Answer:** Resets, mode changes, driver restarts and stress diagnostics can stop work. Follow the exact authorized procedure and recovery plan.
36. How do passthrough, vGPU, MIG and time slicing differ?
   **Answer:** Passthrough allocates a physical GPU; vGPU uses a supported virtual stack; MIG partitions resources; time slicing shares execution without equivalent memory/fault isolation.
37. How can partition profiles create capacity fragmentation?
   **Answer:** Free capacity may be split across incompatible placements or profiles. CIs share parent GI memory, and replicas add no physical memory.
38. Can you defend all three scenario decisions with evidence?
   **Answer:** State the constraint, rejected alternative, validating signal and recovery criterion for each proposed scenario; design prose is not measured evidence.
39. Can you produce all eight labs without unauthorized change?
   **Answer:** Execute only the local workbook without hardware. Other activities need an authorized environment and must remain labeled proposed until performed.
40. Have you rechecked the live blueprint, policy and checkout price?
   **Answer:** Use the current canonical page and program policies; resolve the dated USD125 versus USD135 listing discrepancy at checkout. Do not infer a passing score.


### Check key

- **Ready:** You can connect workload, facility, compute, fabric, storage, software and operations decisions, then identify validation and recovery evidence.
- **Review:** You recognize product names but cannot trace a bottleneck, compatibility dependency or safe operational response.
- **Gap:** You guessed hardware sizing, equated utilization with outcome, or would run disruptive commands without authorization. Return to the requirement sheet and labs.

## Places to learn

This is not a complete list. Start with the official scope and choose resources for demonstrated gaps. Public metadata was checked September 29, 2026; course interiors and checkout were not accessed. Unless explicitly described as a listed runtime, times below are author estimates for selective study.

| Resource | Access | Estimated time |
|---|---|---|
| [Certification and blueprint](https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate/) | Public; canonical 22-topic scope and USD125 exam listing | 1–2h mapping |
| [Official study guide PDF](https://dam-cdn.nvd.orangelogic.com/AssetLink/x874j05hy3m3r2sor84kpvp70750m468.pdf) | Public; six pages, optional unit mapping and reading suggestions | 1–2h mapping |
| [Certification policies](https://www.nvidia.com/en-us/learn/certification/) | Public; booking, integrity, retake and renewal | 30–45m |
| [AI Infrastructure and Operations Fundamentals](https://www.nvidia.com/en-us/training/academy/course-detail/?id=course:15139841) | Paid/account route; public course shell lacks populated details. Canonical and learning-path pages still list the course | Listed 7h; add 12–20h proposed practice |
| [Academy route linked by the PDF](https://academy.nvidia.com/en/course/ai-infrastructure-operations-fundamentals/?cm=64727) | Redirects to a general training page; no course outline or lesson access confirmed there | Specific runtime unverified at this endpoint |
| [DGX Platform and Data Center learning path](https://www.nvidia.com/en-us/learn/learning-path/dgx-data-center/) | Public index; mixed paid routes. Fundamentals card lists USD50/7h; exam card still lists USD135 versus canonical USD125 | 1–2h selection; chosen course varies |
| [DGX documentation](https://docs.nvidia.com/dgx/) | Public portal; Mission Control, Base Command Manager, systems and platform references | 6–12h selected platform reading |
| [Storage scaling article](https://developer.nvidia.com/blog/tips-on-scaling-storage-for-ai-training-and-inferencing/) | Public, January 25, 2023; capacity/performance/availability planning, not a current sizing specification | 30–60m plus requirement sheet |
| [DCGM documentation](https://docs.nvidia.com/datacenter/dcgm/latest/contents.html) | Public entry point to monitoring and diagnostics | 2–4h orientation |
| [DCGM field identifiers](https://docs.nvidia.com/datacenter/dcgm/latest/reference/field-identifiers.html) | Public; inspect exact IDs, types, units and entity support | 2–3h selective reading and workbook |
| [DCGM Exporter metrics](https://docs.nvidia.com/datacenter/dcgm/latest/reference/dcgm-exporter-metrics.html) | Public; metric configuration, field/count distinctions and label boundaries | 2–3h |
| [GPU Operator overview](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/) | Public; lifecycle components and platform links | 2–4h |
| [GPU Operator release notes](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/release-notes.html) | Public; exact component and upgrade caveats are version-specific | 1–2h for assigned versions |
| [Time-slicing GPUs](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html) | Public; replica, isolation, telemetry and configuration limitations | 2–3h; cluster work optional |
| [MIG user guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/) | Public documentation entry point | 30m orientation |
| [MIG concepts](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/concepts.html) | Public; GI/CI boundaries and profile placement | 1–2h |
| [MIG deployment considerations](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/deployment-considerations.html) | Public; consult current GPU/platform prerequisites and full change procedure | 1–2h selective review |
| [Third-party NCA-AIIO prep course](https://www.udemy.com/course/nca-aiio-bootcamp/) | Paid; public fetch blocked with HTTP403. Earlier June2026/about7h claims and lesson quality were not reverified | Current runtime unverified |

Avoid recalled exam items, dumps and guaranteed-pass banks. These readiness prompts and scenarios are original teaching material. No paid questions, private lessons, accounts or infrastructure services were accessed for this review.
