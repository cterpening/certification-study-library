---
exam_code: EX267
vendor_id: red-hat
official_blueprint: https://www.redhat.com/en/services/training/ex267-red-hat-certified-developer-in-ai
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# EX267 Red Hat Certified Developer in AI Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 28, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ex267-coverage-record). The [official EX267 objectives](https://www.redhat.com/en/services/training/ex267-red-hat-certified-developer-in-ai) are authoritative.

**Current baseline:** Red Hat OpenShift AI 3.3 on Red Hat OpenShift Container Platform 4.20<br>
**Upcoming blueprint change:** None announced when checked September 28, 2026<br>
**Important freshness boundary:** OpenShift AI evolves quickly. Confirm the versions assigned in the Red Hat learning environment, and translate older 2.x or newer documentation to the 3.3/4.20 baseline before following it.<br>
**Assessment style:** Performance based; public objective groups are not weighted

## How to use this guide

EX267 tests whether you can create a repeatable path from a data-science project to a served, monitored AI application. It is not primarily a model-theory exam and it is not an OpenShift cluster-administration substitute. Work at the application and project boundary while understanding the platform objects your choices create.

Use one small system throughout preparation: a model selected from an approved catalog, a versioned notebook and training pipeline, an object-storage connection, a registry entry, a KServe deployment, evaluation evidence, and a small streaming or retrieval-augmented application. For every task, retain evidence:

1. inspect project permissions, quota, nodes, storage, connections, images, runtime, and current workload state;
2. make the smallest safe dashboard, YAML, notebook, SDK, or API change;
3. prove the artifact, model, endpoint, pipeline, metric, or application behaves as required;
4. test a denied, delayed, malformed, or resource-constrained path;
5. restart or recreate the relevant component and prove that declared state, data, and version relationships persist.

The September 28 review maps **43 tasks in twelve groups**. The EX267V33K section of the [official objectives-by-version PDF](https://training-lms.redhat.com/public_content/redhat/training/Red%20Hat%20Certification%20Exam%20Objectives%20by%20Version.pdf) contains 41 matching tasks but omits the main page's two resource-placement tasks. Retain selectors/tolerations and placement of workbenches/model servers: the main exam page is the canonical scope. This difference is recorded for follow-up; it is not evidence of a newly announced blueprint change.

Red Hat lists a final “Deploy and Store Models” group that refines capabilities already named under “Deploy and serve models.” This guide maps both groups explicitly to the same model-serving section and labs rather than inventing a separate weight.

## Objective map

| Official task group | What mastery looks like |
|---|---|
| Architecture and fundamentals | Explain the OpenShift/OpenShift AI boundary and place project components in an MLOps or GenAIOps lifecycle |
| Projects and workbenches | Control projects, permissions, images, versions, sizes, custom images, resources, and TensorBoard evidence |
| Data connections | Create least-privilege S3/database connections and prove artifact movement without exposing credentials |
| Resource allocation | Place workloads intentionally with selectors/tolerations and diagnose pending or starved work |
| Deploy and serve models | Choose serving mode, storage, runtime, protocol, resources, and scaling for predictive models or LLMs |
| Model Registry | Package, register, version, query, and deploy models with lineage intact |
| Model and hardware monitoring | Separate model-quality evidence from platform utilization, then act on both |
| Data science pipelines | Build reproducible Elyra/Kubeflow pipelines, artifacts, experiments, and runs |
| Optimize and evaluate | Select responsibly, compress/quantize where justified, and evaluate with repeatable benchmarks |
| Generative AI applications | Build bounded streaming, RAG, agentic, and guardrailed applications |
| Git and model development | Collaborate on notebooks/code and train, load, save, and export models reproducibly |
| Deploy and store models | Revalidate the serving interface, deployment settings, and S3/OCI/PVC storage choices above |

## 1. Architecture, projects, and lifecycle

OpenShift Container Platform supplies Kubernetes scheduling, namespaces/projects, identity, networking, storage, Operators, observability, and policy. OpenShift AI supplies the data-science dashboard and components for workbenches, pipelines, model registry, model serving, evaluation, and related AI workflows. Know which layer owns a failure: an invalid inference protocol is not fixed by adding a cluster role, while a pod blocked by quota or scheduling is not fixed by retraining the model.

MLOps connects source, data, environment, training, evaluation, approval, registration, deployment, monitoring, and feedback. GenAIOps extends that evidence chain to foundation models, prompts, retrieval indexes, evaluations, safety controls, tools, and runtime feedback. A data-science project is the collaboration and isolation boundary in which many of those components meet; it does not by itself prove data rights, model approval, or production readiness.

Create projects with purposeful membership and least privilege. Distinguish the user who experiments, the pipeline identity that reads data and writes artifacts, the registry client, and the serving identity. A broad project-admin grant may make a lab pass while hiding the authorization decision the task expects.

> **Related item:** Supply-chain provenance links Git commits, base images, packages, training data, model artifacts, evaluations, approvals, and deployments. It makes rollback and incident analysis possible even though “software bill of materials” is not a separate published objective.

## 2. Workbenches, images, and collaborative development

A workbench combines an image, image version, size/resource request, storage, environment variables or connections, and project permissions. Select the smallest supported image and size that satisfy the library, accelerator, and workload requirements. Treat image tags as mutable unless digest or release controls prove otherwise. A custom workbench image needs trusted packages, compatible drivers/runtime, a reproducible build, vulnerability review, and a supported notebook interface—not just a container that starts.

The [3.3 workbench guide](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/creating_a_workbench/index) distinguishes publishing a custom image as an `ImageStream` from creating a `Notebook` workload. Image annotations describe software; they do not install it or prove its behavior. Verify the built image, imported digest, visible tag, startup, arbitrary-user permissions and persistent mount separately. Cluster-wide image publication requires different authority from a project user selecting an available image.

Use Git for notebook and application collaboration. Keep large data and model binaries out of ordinary Git history; store code, environment declarations, pipeline definitions, small fixtures, and documentation in Git and maintain pointers/checksums for external artifacts. Clear output and credentials before committing. Prefer small modules and tests over hiding all logic in notebook cells.

TensorBoard can expose training loss, accuracy and other logged series, but the graph is only as reliable as the experiment metadata. Record the source revision, data/version reference, parameters, seed where meaningful, image, hardware, run ID, and artifact destination. Compare runs rather than selecting the most attractive final point without context.

> **Related item:** Reproducibility is stronger than repeatability. A repeated run in the same long-lived workbench can depend on cached state; a reproducible run rebuilds the environment and declared inputs.

## 3. Data connections and artifact boundaries

Connections describe how a workload reaches external storage or databases. For S3-compatible storage, understand endpoint, bucket, region/compatibility details, access key or workload identity, TLS trust, and object prefix. For databases, understand host/service, database/schema, user, secret, TLS, driver, network policy, and connection lifecycle. Keep secrets in connection/secret mechanisms and inject references; never print them in notebooks, pipeline output, Git, or model metadata.

The [3.3 S3 reference](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/working_with_data_in_an_s3-compatible_object_store/index) provides notebook data-transfer workflows. Treat the storage endpoint, bucket and prefix as distinct values. A connection secret reference is not authorization to every object; verify the workload identity and storage policy at the operation being performed. The [3.3 release notes](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/release_notes/index) deprecate `opendatahub.io/connection-type-ref` in favor of `opendatahub.io/connection-type-protocol` for new connection secrets; inspect the assigned environment before adapting old manifests.

Prove both directions independently: read the expected input and write a uniquely named artifact, then retrieve and checksum it from a clean process. Test a missing object, revoked credential, wrong endpoint, invalid certificate, and unauthorized prefix. “Connection created” is configuration evidence, not data-path evidence.

Choose storage by lifecycle. S3-compatible object storage suits durable, shareable model/data artifacts; an OCI artifact integrates packaging, digest, promotion, and registry controls; a PVC gives filesystem semantics and locality but creates access-mode, capacity, placement, backup, and portability considerations. Record who can mutate each artifact and how a deployment resolves an immutable version.

## 4. Resources, scheduling, and accelerator evidence

Resource requests influence scheduling and guarantees; limits bound use. A node selector constrains placement to labels. A toleration permits—but does not require—placement on a tainted node; it does not create the hardware resource or bypass a missing request. Diagnose a pending workload by reading events, node labels/taints, requested resources, quotas, affinity, storage topology, and available accelerator resources before changing anything.

The [3.3 hardware-profile reference](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/working_with_accelerators/index) and release notes identify Hardware Profiles as the current mechanism, replacing deprecated Accelerator Profiles and the legacy container-size selector. Inspect the resulting workload requests, limits, node selectors and tolerations; a selected profile name alone does not prove allocation. Seeing a physical accelerator with `lspci` is also insufficient: the platform must advertise usable allocatable resources.

| Observation | Next evidence to inspect |
|---|---|
| Toleration matches, selector does not | Required node labels still exclude that node |
| Labels match, accelerator request exceeds availability | Allocatable and already requested resources; toleration cannot manufacture capacity |
| Resources fit, PVC cannot attach in that topology | Volume access mode, binding and node/storage topology |
| Pod runs, latency remains unacceptable | Queueing, batch/concurrency, memory and request-level measurements |

Allocate expensive accelerators deliberately. Match runtime/model precision, memory, context length, concurrency, batch behavior, and performance goals to the hardware. Monitor GPU/CPU/memory utilization, throttling, queue depth, latency, errors, and saturation. Higher utilization is not automatically better if latency or reliability violates the service objective.

> **Related item:** Capacity planning joins platform telemetry with workload demand. A model-quality regression and a hardware-saturation incident may produce similar user complaints but require different evidence and fixes.

## 5. Model serving with KServe

Know the serving path: client, route/network controls, inference endpoint, serving resource, runtime, model loader/storage, and accelerator. KServe supplies Kubernetes-native model-serving concepts; OpenShift AI presents supported workflows and modes. The exam names Standard and Advanced modes, while the current [3.3 deployment guide](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/deploying_models/index) describes KServe RawDeployment and a wizard with Advanced settings. These words alone do not establish a one-to-one mapping to older deployment modes. The release notes require migration of Serverless/ModelMesh workloads before a 3.0 upgrade. Keep the public objective wording and inspect the assigned environment; do not equate Advanced with Knative/Serverless or assume scale-to-zero from a UI label. This terminology mapping remains an explicit review limitation.

The [3.3 serving-platform guide](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/configuring_your_model-serving_platform/index) separates runtime templates, workload configuration and deployment strategy. A rolling update can need temporary extra capacity; Recreate can free the old workload first but introduces downtime. Neither choice changes the model-quality acceptance criteria.

Use OpenVINO for supported predictive-model formats and vLLM for supported large-language-model serving. Configure a custom serving runtime only when a provided runtime does not meet the model/protocol need; define its container, supported formats, command/arguments, ports, resources, probes, security, and storage behavior. A running pod is insufficient. Invoke the endpoint with valid and invalid payloads, verify schema/protocol and response, observe latency/errors/resources, and recreate the deployment.

For model storage, preserve the directory structure expected by the loader. The deployment guide's OpenVINO example uses a numbered model-version directory; that is not a universal OCI requirement for every runtime. When building a modelcar, verify the selected base image supplies the tools required by its build/startup steps and that the eventual serving identity can read the files. A successful image push does not prove loading or inference.

Deployment settings should follow an explicit contract: immutable model reference, runtime and version, serving mode, protocol, resources/accelerator, replica/scaling policy, network exposure, authentication/authorization, timeouts, environment/secret references, and observability. Make rollback a model/runtime/configuration version change, not a manual repair to a live pod.

> **Related item:** An inference service has two versioned interfaces: its transport/schema contract and its statistical behavior. A backward-compatible JSON response can still be unsafe if the model or prompt changes its meaning.

## 6. Model Registry and lineage

The Model Registry records model identity, versions, artifacts, metadata, and lifecycle relationships. Package model artifacts as OCI artifacts when required and use immutable digests. Register a new version instead of silently overwriting an approved one. Metadata should make the version explainable: source revision, data reference, training run, framework/format, metrics/evaluation, owner, intended use, limitations, approval, and artifact checksum.

The [3.3 registry guide](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/working_with_model_registries/index) describes a metadata store, not automatic copying of model bytes. Its deployment-from-registry workflow currently limits URI-registered model deployment to **public OCI repositories**. Do not generalize that restriction to every direct-serving storage workflow or assume registry access supplies artifact-store credentials. The release notes identify `v1beta1` as the current registry API and deprecate `v1alpha1`; use the endpoint exposed by the assigned installation.

Practice dashboard and API workflows. Create and query a registered model, distinguish model identity from model version and artifact, select an exact version, and deploy from that record. Test duplicate names/versions, missing artifacts, unauthorized access, and a registry entry whose artifact digest no longer resolves. The registry is a catalog and governance anchor, not a substitute for the underlying artifact store or evaluation system.

## 7. Monitoring models and platform performance

Separate four evidence classes:

| Evidence | Question | Example response |
|---|---|---|
| Service health | Is inference available and within latency/error objectives? | scale, repair routing/runtime, or roll back |
| Resource health | Is CPU/GPU/memory/storage/network capacity adequate? | right-size, place, batch, limit, or add capacity |
| Data/model quality | Did inputs or outcomes drift or become biased? | investigate cohorts/data, retrain or constrain use |
| Business/safety outcome | Does the application remain useful and safe? | adjust retrieval/prompt/guardrails or suspend flow |

Use TrustyAI for supported bias, drift, evaluation, and guardrail workflows. A metric needs a defined population, reference, threshold, observation window, and response owner. Aggregate accuracy can conceal subgroup harm; drift can be harmless seasonal change or an early warning, not automatic proof of failure. Use OpenShift monitoring and Grafana to correlate model signals with resource and request signals.

The [3.3 monitoring guide](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/monitoring_your_ai_systems/index) requires the capture/configuration path to be working before TrustyAI metrics become meaningful. Record the model identifier, reference data tag, protected attribute, favorable outcome, compared groups and batch/window size. A fairness statistic is not a substitute for error rates or the task-specific consequences of an incorrect prediction. Test missing cohorts and small sample sizes as well as aggregate scores.

Never log raw sensitive prompts, retrieved documents, secrets, or regulated labels merely to improve observability. Design redaction, access, retention, sampling, and incident evidence before production.

## 8. Data science pipelines and experiments

Create a pipeline server and build components with clear inputs, outputs, images, resources, secrets, and artifact locations. Elyra can help author notebook-oriented flows; the Kubeflow Pipelines SDK defines reusable container components and pipelines. The compiled/uploaded definition—not the notebook UI—is the execution contract.

The [3.3 pipeline guide](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/working_with_ai_pipelines/index) documents Python 3.11+ and KFP SDK 2.14.3+ for compilation. A plain IR YAML is a serialized pipeline specification; a Kubernetes-native output wraps it in `Pipeline`/`PipelineVersion` resources. Select the form supported by the pipeline server and import method. Creating Kubernetes resources requires the matching CRDs and authority; compilation does not prove either. For custom pipeline containers on a FIPS cluster, the guide requires UBI 9 or RHEL 9 bases.

Elyra requires a supported JupyterLab workbench image with the extension; code-server, RStudio and Minimal Python are not interchangeable choices. Create the pipeline server before the workbench when relying on automatic runtime configuration. Verify the actual image package/extension list rather than inferring it from an old tutorial.

Use Kubernetes features intentionally: service accounts, secrets/configuration references, PVCs, resource requests/limits, node placement, and exit behavior. Components should be independently rerunnable, validate inputs, produce deterministic names or run-scoped outputs, and fail loudly. Cache only when the cache key captures every meaningful input. Treat a pipeline run as a graph of evidence, not a sequence of green icons.

Cache eligibility depends on declared inputs and task configuration. A mutable URL or image tag can keep the same string while its bytes change; pass an immutable version/digest and verify downloaded bytes, or disable caching where inputs cannot be represented reliably. `task.set_caching_options(False)` requests re-execution of that task; a server-wide disabled cache overrides task-level choices. Inspect actual cached/run status and retained artifacts when testing on the platform.

Use experiments to group comparable runs and compare parameters, inputs, metrics, artifacts, duration, resource use, and outcome. Promote only an exact evaluated artifact. Test resume/retry and ensure side effects are idempotent or deduplicated.

> **Related item:** Orchestration handles ordering and retries; data contracts handle meaning. A perfectly orchestrated pipeline can still train on mislabeled, stale, or unauthorized data.

## 9. Model selection, optimization, and evaluation

Select from the OpenShift AI catalog or Hugging Face using task fit, license, provenance, architecture, supported runtime, context/input limits, language/domain evidence, safety history, hardware need, and maintenance status. “Popular” is not an acceptance criterion. Record the exact revision and license terms; model code may require more trust than weights alone.

The [3.3 release notes](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/release_notes/index) list the **LLM Compressor integration as Developer Preview**. Its presence in exam objectives does not establish production support. Select a version-compatible practice image and keep this support status separate from the underlying optimization idea. The [model customization reference](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/customize_models_to_build_gen_ai_applications/index) provides adjacent training/data workflows; it does not make every current upstream recipe part of the assigned environment.

Compression and quantization with compatible LLM Compressor workflows can reduce memory, cost, or latency but may change quality and hardware compatibility. Establish a baseline, change one optimization dimension, measure task and subgroup quality plus throughput/latency/memory, and keep the unoptimized rollback artifact.

The [3.3 LM-Eval guide](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/evaluating_ai_systems/index) separates platform permission (`permitOnline` / `permitCodeExecution`) from per-job requests (`allowOnline` / `allowCodeExecution`). Both access categories are disabled by default, and downloading artifacts is a different decision from executing their code. Diagnose missing datasets/tokenizers and approved offline storage before broadly enabling either. Record task/template/data revisions and handle result samples as potentially sensitive.

Use LMEval with standard or justified custom benchmarks. Prevent train/test contamination, pin prompt/templates and dataset versions, choose metrics before comparison, and retain configuration and result artifacts. A benchmark improvement does not prove production safety; pair offline evaluation with application-level, adversarial, latency, cost, and human-review evidence.

## 10. Generative, retrieval, agentic, and guardrailed applications

A simple streaming application should preserve partial-response UX while handling cancellation, timeout, backpressure, authentication, errors, and final telemetry. For RAG, separate ingestion (extract, normalize, chunk, embed, authorize, index) from request time (authenticate, retrieve, filter/rerank, assemble context, generate, cite, evaluate). Enforce source-level permissions during retrieval; prompting the model not to reveal unauthorized material is not access control.

An agent combines a model with tools and a loop. Give each tool a narrow typed contract, least-privilege identity, validation, timeout, idempotency strategy, and audit record. Bound steps, time, tokens, spend, reachable resources, and data. Require human approval before consequential or irreversible actions and distinguish model text from trusted instructions.

The [3.3 guardrails guide](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/enabling_ai_safety_with_guardrails/index) separates detectors, Orchestrator service/TLS configuration and gateway pipeline presets. Detector identity, safe-label mapping and threshold are part of the evaluated contract. A reachable unguarded model endpoint is not evidence that the intended guardrail path ran. Test the gateway path with benign and prohibited synthetic inputs, detector unavailability, false positives and streamed-output boundaries. A blanket header-forwarding configuration can expose credentials to an unintended downstream service; restrict each configured destination and required headers.

Guardrails are defense in depth: validate input, constrain retrieval and tools, detect unsafe content, protect sensitive data, validate structured output, enforce business authorization outside the model, and monitor outcomes. Test direct and indirect prompt injection, data leakage, malformed tool arguments, denial-of-wallet, unavailable dependencies, and false positive/negative behavior.

> **Related item:** RAG changes the model's context; fine-tuning changes parameters; tools change what the application can do. Diagnose which layer caused the outcome before changing all three.

## Original pipeline artifact and evaluation example

This example scores **synthetic precomputed binary predictions**, not an LLM or a real customer population. Its illustrative thresholds are exercise inputs, not universal acceptance criteria. It makes the evaluated artifact, expected cohorts and decision explicit, while leaving deployment approval separate.

Save this as `pipeline_example.py`. Install the compatible KFP SDK in an isolated practice environment; the review used `kfp==2.14.3`. The `python:3.11` image string below is for this compilation exercise; no container was pulled or run. Before cluster execution, select an approved image, pin its digest and dependencies, and apply the UBI/RHEL 9 requirement where FIPS applies.

```python
from kfp import compiler, dsl
from kfp.compiler.compiler_utils import KubernetesManifestOptions


@dsl.component(base_image="python:3.11")
def prepare_rows(rows_json: str, dataset: dsl.Output[dsl.Dataset]) -> str:
    import hashlib
    import json
    from pathlib import Path

    rows = json.loads(rows_json)
    if not isinstance(rows, list) or not rows:
        raise ValueError("Expected a non-empty validation row list")
    seen = set()
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"id", "cohort", "label", "prediction"}:
            raise ValueError("Unexpected row schema")
        if not isinstance(row["id"], str) or not row["id"] or row["id"] in seen:
            raise ValueError("Row IDs must be non-empty and unique")
        if not isinstance(row["cohort"], str) or not row["cohort"]:
            raise ValueError("Missing cohort")
        if any(type(row[k]) is not int or row[k] not in (0, 1) for k in ("label", "prediction")):
            raise ValueError("Labels and predictions must be binary integers")
        seen.add(row["id"])
    raw = (json.dumps(sorted(rows, key=lambda r: r["id"]), sort_keys=True,
                      separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")
    target = Path(dataset.path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(raw)
    digest = hashlib.sha256(raw).hexdigest()
    dataset.metadata.update(sha256=digest, row_count=len(rows))
    return digest


@dsl.component(base_image="python:3.11")
def evaluate_rows(dataset: dsl.Input[dsl.Dataset], expected_sha256: str,
                  minimum_accuracy: float, minimum_cohort_accuracy: float,
                  minimum_cohort_count: int, expected_cohorts_json: str,
                  metrics: dsl.Output[dsl.Metrics],
                  report: dsl.Output[dsl.Artifact]) -> bool:
    import hashlib
    import json
    import math
    from collections import defaultdict
    from pathlib import Path

    for value in (minimum_accuracy, minimum_cohort_accuracy):
        if type(value) not in (int, float) or not math.isfinite(value) or not 0 <= value <= 1:
            raise ValueError("Accuracy thresholds must be finite and between zero and one")
    if type(minimum_cohort_count) is not int or minimum_cohort_count < 1:
        raise ValueError("Minimum cohort size must be a positive integer")
    expected = json.loads(expected_cohorts_json)
    if (not isinstance(expected, list) or not expected
            or any(not isinstance(v, str) or not v for v in expected)
            or len(set(expected)) != len(expected)):
        raise ValueError("Declare a non-empty unique cohort list")
    raw = Path(dataset.path).read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise ValueError("Validation artifact changed")
    rows = json.loads(raw)
    if not isinstance(rows, list) or not rows:
        raise ValueError("Empty validation artifact")
    by_cohort = defaultdict(list)
    for row in rows:
        by_cohort[row["cohort"]].append(row["label"] == row["prediction"])
    cohorts = {name: {"count": len(values), "accuracy": sum(values) / len(values)}
               for name, values in sorted(by_cohort.items())}
    accuracy = sum(row["label"] == row["prediction"] for row in rows) / len(rows)
    passed = set(cohorts) == set(expected) and accuracy >= minimum_accuracy and all(
        value["count"] >= minimum_cohort_count and value["accuracy"] >= minimum_cohort_accuracy
        for value in cohorts.values())
    metrics.log_metric("accuracy", accuracy)
    metrics.log_metric("minimum_cohort_accuracy", min(v["accuracy"] for v in cohorts.values()))
    metrics.log_metric("policy_passed", int(passed))
    result = {"dataset_sha256": expected_sha256, "row_count": len(rows),
              "accuracy": accuracy, "cohorts": cohorts, "policy_passed": passed,
              "missing_cohorts": sorted(set(expected) - set(cohorts)),
              "unexpected_cohorts": sorted(set(cohorts) - set(expected)),
              "requires_separate_approval": True}
    target = Path(report.path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    return passed


@dsl.pipeline(name="ex267-validation-evidence")
def validation_pipeline(rows_json: str, minimum_accuracy: float = 0.9,
                        minimum_cohort_accuracy: float = 0.8,
                        minimum_cohort_count: int = 2,
                        expected_cohorts_json: str = '["a","b"]'):
    prepared = prepare_rows(rows_json=rows_json)
    evaluated = evaluate_rows(
        dataset=prepared.outputs["dataset"], expected_sha256=prepared.outputs["Output"],
        minimum_accuracy=minimum_accuracy, minimum_cohort_accuracy=minimum_cohort_accuracy,
        minimum_cohort_count=minimum_cohort_count, expected_cohorts_json=expected_cohorts_json)
    prepared.set_caching_options(True)
    evaluated.set_caching_options(False)
    for task in (prepared, evaluated):
        task.set_cpu_request("100m").set_cpu_limit("1")
        task.set_memory_request("128Mi").set_memory_limit("512Mi")


if __name__ == "__main__":
    compiler.Compiler().compile(validation_pipeline, "validation-ir.yaml")
    compiler.Compiler().compile(
        validation_pipeline, "validation-kubernetes.yaml", kubernetes_manifest_format=True,
        kubernetes_manifest_options=KubernetesManifestOptions(
            pipeline_name="ex267-validation-evidence", pipeline_version_name="ex267-validation-v1",
            namespace="study-ai", include_pipeline_manifest=True))
```

Run `python pipeline_example.py` to produce `validation-ir.yaml` and `validation-kubernetes.yaml`. The first has top-level `components`, `deploymentSpec`, `pipelineInfo` and `root`; it is not directly a Kubernetes resource. The second contains a namespaced `Pipeline` and `PipelineVersion` with `spec.pipelineSpec`. The [compiler reference](https://www.kubeflow.org/docs/components/pipelines/user-guides/core-functions/compile-a-pipeline/) explains both forms and static artifact type checking.

The `Dataset` output and its SHA-256 parameter come from the same producer. The evaluator checks those exact bytes before scoring; the hash detects a changed artifact relative to the trusted expected digest, not malicious replacement of both bytes and digest. Production lineage additionally needs controlled identities, immutable artifact storage and authenticated provenance. The typed edge is a schema contract, not proof of data quality.

| Original local case | Expected decision/evidence |
|---|---|
| Both declared cohorts have enough correct examples | Policy passes; report still requires separate approval |
| 90 correct majority examples and 10 incorrect minority examples | Overall accuracy is 0.90, minority accuracy is 0; policy fails |
| Required cohort missing, even with perfect observed accuracy | Policy fails and names the missing cohort |
| Unexpected or undersized cohort | Policy fails the population/sample contract |
| Duplicate row ID, wrong field types, malformed thresholds | Reject invalid input |
| Data changes after expected digest was recorded | Refuse to score under the old digest |
| Dataset connected to a Model input | SDK rejects the incompatible typed edge |

**Actual local validation:** 39 checks passed with Python 3.13.14 and KFP 2.14.3. They executed the original component Python bodies using KFP artifact/metrics objects and compiled both output formats, including negative type checking and artifact/cohort failures. They did not run containers, a pipeline server, Kubernetes admission/scheduling, model inference, LM-Eval, GPUs, S3, registry or serving endpoints. The complete eight platform labs below remain proposed.

The evaluator is deliberately uncached. In the real workflow, change one dataset/model/policy version, inspect whether each task executes, and demonstrate that a failed policy result cannot be mistaken for approval. This example records a decision; it contains no deployment step.

## Integrated scenarios

### Scenario 1: Governed predictive service

A team trains a churn model from approved object storage. Build a project and least-privilege connection, version code and environment, pipeline preprocessing/training/evaluation, log TensorBoard evidence, package/register the approved artifact, deploy it with OpenVINO, validate endpoint semantics, then monitor resource use and drift. Revoke the data credential after training and prove inference still follows the intended artifact path.

### Scenario 2: Resource-constrained LLM service

An LLM deployment remains pending, then becomes slow under load. Trace selector, toleration, accelerator request, quota, storage and events. Deploy the exact model using vLLM, establish latency/throughput/memory baselines, quantize only after the quality baseline, and compare. Prove rollback to the registered unoptimized version and retain request/resource/evaluation evidence.

### Scenario 3: Guardrailed RAG assistant

Build an application that ingests authorized documents, creates a versioned vector index, retrieves only caller-permitted content, streams cited answers, and invokes one read-only tool. Evaluate retrieval and answer quality, add input/output guardrails and typed validation, test injection and tool failures, and correlate application traces with model-serving and hardware signals.

## Hands-on labs

1. **Project/workbench baseline:** create roles, a sized workbench and persistent storage; clone code, record image/version, restart, and prove permissions and files persist.
2. **Custom image and experiment:** build/import a pinned custom workbench image, run a small training job, emit TensorBoard metadata, and reproduce from a clean workbench.
3. **Connections and artifacts:** use least-privilege S3-compatible and database connections; read/write/checksum artifacts and test bad credentials/TLS/path.
4. **Placement diagnosis:** schedule CPU and accelerator-shaped workloads with selectors/tolerations; deliberately create and diagnose a pending pod without broadening access blindly.
5. **Serving and registry:** register two model versions, deploy exact OpenVINO and vLLM artifacts through appropriate modes/storage, test protocols and invalid input, then roll back.
6. **Pipeline evidence:** author a multi-component pipeline with the SDK or Elyra, pass artifacts, compare experiment runs, test caching and safe retry, and reproduce a chosen result.
7. **Evaluation and monitoring:** run a pinned standard or custom LMEval job, exercise TrustyAI drift/bias evidence, and correlate it with request and hardware dashboards.
8. **Capstone replay:** rebuild one scenario from Git and declared external artifacts, validate RAG or tool boundaries, restart/recreate every component, and produce an evidence/rollback packet.

Use a disposable authorized cluster and small models/datasets. GPU resources and hosted model calls can be scarce or costly; set quotas and budgets and remove lab resources when finished.

## Original knowledge checks

1. Which responsibilities belong to OpenShift versus OpenShift AI?
2. What artifacts extend an MLOps evidence chain into GenAIOps?
3. Why is a project-admin grant weak evidence of correct authorization?
4. Which workbench properties must be recorded to reproduce an experiment?
5. Why can a mutable image tag invalidate a comparison?
6. What belongs in Git, and what belongs in an artifact store?
7. What does TensorBoard show, and what provenance must accompany it?
8. How would you prove a connection beyond its dashboard status?
9. When is S3 preferable to OCI or PVC model storage?
10. What credential evidence must never enter notebook output?
11. How do requests, limits, selectors, and tolerations affect placement differently?
12. Which events would explain an accelerator workload remaining pending?
13. Why can high GPU utilization coexist with a poor service outcome?
14. Trace a request from route to model artifact and response.
15. What must a custom serving runtime declare and prove?
16. Why is a running inference pod insufficient acceptance evidence?
17. Which deployment settings must be versioned for rollback?
18. How do model identity, version, and artifact differ in the registry?
19. Which metadata connects a registry version to training and approval?
20. What failure occurs when registry metadata resolves to a missing artifact?
21. How do service, resource, model-quality, and business signals differ?
22. Why does drift not automatically prove model failure?
23. How can an aggregate metric conceal subgroup harm?
24. What observability data should be redacted or access-controlled?
25. What makes a pipeline component independently rerunnable?
26. When can pipeline caching return an invalid result?
27. How should a retry-safe component handle external side effects?
28. What makes two experiment runs legitimately comparable?
29. Which selection evidence matters beyond model popularity?
30. How would you detect benchmark contamination?
31. What quality and performance evidence should bracket quantization?
32. Why is an offline benchmark not production acceptance?
33. Separate RAG ingestion-time and request-time responsibilities.
34. Where must document authorization be enforced in RAG?
35. What controls bound an agent loop and its tools?
36. Which actions should require human approval?
37. Why are guardrails not a substitute for authorization?
38. How would you test indirect prompt injection safely?
39. Which persisted evidence proves the capstone can be recreated?
40. What must be checked when using a guide written for OpenShift AI 2.x?

## Answers and reasoning

1. OpenShift owns core cluster primitives; OpenShift AI composes supported AI workflows on them.
2. Model/prompt/index/tool versions, evaluations, safety controls, approvals, runtime feedback, and costs.
3. It bypasses least-privilege decisions and can hide the identity actually needed.
4. Source/data references, image and packages, resources, parameters, seed, run ID, metrics, and artifact destination.
5. The same name can resolve to different bits, destroying reproducibility and rollback confidence.
6. Version code/configuration/pipeline definitions and small fixtures; externally store large or sensitive data/models with immutable references.
7. Logged training series; it needs source, data, environment, parameter, run, and artifact context.
8. Read and write a unique artifact, retrieve/checksum it cleanly, and test failure paths.
9. For durable shareable objects; OCI favors digest-based packaging/promotion, while PVC favors filesystem/local access.
10. Secrets, tokens, full connection strings, sensitive records, and unredacted regulated data.
11. Requests drive scheduling, limits bound use, selectors require labels, and tolerations only permit tainted placement. In 3.3, inspect the workload produced by its Hardware Profile; the profile name does not prove that allocatable devices, quota and storage topology can satisfy it.
12. Events plus labels, taints, accelerator availability/request, quota, affinity, and storage topology.
13. Saturation can increase queues/errors/latency or run the wrong-quality workload efficiently.
14. Identify each network, serving-resource, runtime, loader/storage, process, protocol, and response boundary.
15. Image, formats, command, ports, protocol, resources, probes, security, and storage compatibility.
16. The model may not load correctly, protocol/authorization may fail, or output may be unusable.
17. Artifact digest, runtime/mode/protocol, resources, scaling, exposure, identity, config/secrets, and observability.
18. Identity groups the concept, version records a revision, and artifact points to the payload/location. Registry metadata does not make a mutable URI immutable or copy the payload; bind the evaluated version to its content digest and storage policy.
19. Source/data/run references, format, metrics, owner, intended use, limitations, approval, and checksum.
20. Discovery succeeds but reproducible deployment fails; treat it as a lineage/integrity incident.
21. They answer availability, capacity, statistical behavior, and actual usefulness/safety questions respectively.
22. It is a change signal whose materiality must be evaluated against outcomes and context.
23. Majority performance can mask a severe minority-cohort regression.
24. Prompts, retrieved text, labels, secrets, identifiers, tool arguments/results, and regulated data.
25. Declared inputs/outputs/image/resources, validation, durable artifacts, and deterministic or run-scoped side effects.
26. When declared inputs omit a meaningful version or the same URL/tag resolves to new bytes. Record immutable data/image references and the compiled task configuration; disable caching when hidden external state cannot be modeled safely.
27. Use idempotent writes, unique run keys, transactions, or explicit deduplication.
28. Pinned data/code/environment/parameters, comparable hardware/metrics, and retained artifacts.
29. Task evidence, license/provenance, runtime support, limits, domain/language fit, safety, resources, and maintenance.
30. Audit dataset lineage and overlap, isolate held-out data, and inspect suspiciously perfect or prompt-sensitive results.
31. Use the same pinned tasks and expected cohorts before/after optimization, with accuracy/safety, latency, throughput, memory, hardware and rollback artifacts. Verify enough examples exist per cohort and retain the 3.3 LLM Compressor Developer Preview limitation.
32. It does not test retrieval, tools, permissions, latency, cost, safety controls, or real user distribution.
33. Ingestion creates authorized indexed evidence; request time authenticates, filters/retrieves, prompts, generates, and cites.
34. In the retrieval/data layer before content becomes model context, with application authorization enforced afterward too.
35. Typed tools, least privilege, input/output validation, timeouts, idempotency, audit, and step/token/time/cost limits.
36. Irreversible, financially material, privileged, external-communication, or safety-critical changes.
37. A probabilistic filter cannot grant or deny deterministic business/data permissions.
38. Use synthetic authorized documents containing hostile instructions and verify they cannot expand tool/data authority.
39. Git revision, environment/image, data/model/index digests, pipeline/run configuration, metrics, approvals, deployment state, and rollback proof.
40. Map every objective to 3.3/4.20 names, APIs, modes, runtimes, storage, security and behavior. In particular, check Hardware Profiles, connection annotations, registry v1beta1, KFP output mode and retired Serverless/ModelMesh paths; keep the unresolved Standard/Advanced terminology visible.

## Version-gap checklist

Before using older 2.x or newer rolling material, verify against the official 3.3/4.20 environment:

- dashboard navigation, component/operator state, CRD/API versions, and terminology;
- Standard versus Advanced serving behavior, KServe topology, supported runtimes/protocols, and scaling;
- model storage, OCI packaging, registry API/metadata, and deployment-from-registry workflow;
- pipeline backend, Elyra/Kubeflow SDK syntax, caching, experiments, and artifact behavior;
- TrustyAI, LMEval, Guardrails Orchestrator, model catalog, and Hugging Face integration;
- accelerator profiles, node placement, monitoring metrics/dashboards, and permissions;
- workbench images, custom-image requirements, connection fields, and security defaults.

## Source and freshness notes

- The official exam page controls the name, version baseline, objectives, prerequisites, delivery language, and lifecycle state.
- Product documentation controls supported commands, APIs, modes, permissions, integrations, and operational behavior for 3.3/4.20.
- Training-provider runtimes, prices, schedules, revisions, catalogs, sandbox access, and course availability are volatile; verify before purchase.
- Model licenses, catalog entries, supported formats/runtimes, hardware profiles, limits, and security behavior are also volatile.
- This guide uses only public objectives and original practice prompts. It does not reproduce gated course labs or exam tasks.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Select the explanation, lab, reference, or assessment format that closes your own gaps; spend most preparation time performing and revalidating the public tasks.

| Resource | Access | Estimated time |
|---|---|---:|
| [Red Hat AI267 official course](https://www.redhat.com/en/services/training/ai267-developing-and-deploying-ai/ml-applications-on-red-hat-openshift-ai) | Paid; closest version-matched route | About 4–5 instructor-led days plus 30–60 hours of replay |
| [Red Hat AI067 technical overview](https://www.redhat.com/en/services/training/ai067-red-hat-ai-technical-overview) | Free account; broad orientation | About 3–6 hours |
| [OpenShift AI 3.3 documentation](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3) | Free official reference | 25–50 selected hours while labbing |
| [OpenShift Container Platform 4.20 documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20) | Free official prerequisite/reference | 10–25 selected hours for project, storage, scheduling, security, and monitoring gaps |
| [Red Hat Developer OpenShift AI learning hub](https://developers.redhat.com/learn/openshift-ai) | Free; mixed-version paths | 5–15 selected hours plus labs |
| [Introduction to OpenShift AI](https://developers.redhat.com/learn/openshift-ai/introduction-openshift-ai) | Free one-hour path; account/sandbox requirements | About 1–3 hours with repetition |
| [Scalable Kubernetes Infrastructure for AI Platforms](https://www.oreilly.com/library/view/scalable-kubernetes-infrastructure/9798341608191/) | O'Reilly subscription; Red Hat authors | 3–6 application hours estimated; current runtime unverified (page blocked) |
| [LLM on OpenShift AI Deployment Masterclass](https://www.udemy.com/course/llm-on-openshift-ai-deployment-masterclass/) | Paid marketplace course | 5–10 lab hours estimated; current runtime unverified (page blocked); check 3.3 workflow gaps |
| [Red Hat 3.3 training/certification update](https://www.redhat.com/en/blog/accelerate-and-upskill-red-hat-ai-training-and-certification) | Free lifecycle context | 10–20 minutes |

The paid O'Reilly and Udemy pages blocked automated rechecking on September 28; no lesson interiors or current runtime/date claims were verified.

- **Reusable components:** Ana Biazetti, Nelesh Singla and Matt Prahl’s June 3, 2026 [modular AI pipelines article](https://developers.redhat.com/articles/2026/06/03/build-modular-ai-pipelines-openshift-ai-and-reusable-components) supports focused component contracts, early input validation and small-data tests. Use it as an engineering method; a stability label does not by itself prove your security, FIPS, version or production requirements.
- **Focused 3.3 references:** pair [pipeline compilation/cache behavior](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/working_with_ai_pipelines/index), [model registry workflows](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/working_with_model_registries/index), [LM-Eval](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/evaluating_ai_systems/index) and [guardrails](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.3/html-single/enabling_ai_safety_with_guardrails/index) with the corresponding labs.

No exact current EX267 MeasureUp, Whizlabs, Pluralsight certification path, or independent practice exam was verified. Avoid recalled-task banks and “actual exam” claims. A performance exam is best served by original objective-mapped tasks, clean rebuilds, failure injection, and evidence review.
