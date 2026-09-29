# CKAD deep review — September 29, 2026

Same-context AI review; independent human review pending. [Study guide](../../guides/CKAD-certified-kubernetes-application-developer.md).

## Scope and lifecycle

The [official CKAD page](https://training.linuxfoundation.org/certification/certified-kubernetes-application-developer-ckad/) still names Kubernetes **v1.35**. Read all 24 competencies and the actual [CNCF PDF](https://raw.githubusercontent.com/cncf/curriculum/master/CKAD_Curriculum_v1.35.pdf): three pages, 149,864 bytes, with SHA receipt. Layout extraction confirms Kustomize belongs in deployment; groups are 4/4/5/8/3, weighted 20/20/15/25/20. Typography and within-domain ordering differ slightly from the live page. The GitHub viewer shell was not mistaken for PDF contents.

Both monitored hashes remain unchanged. No accepted baseline was rewritten. The two-hour performance exam, two-year validity, 12-month eligibility, one retake and two 36-hour simulator activations remain listed. Simulator question counts are not real-exam counts. Kubernetes v1.37's release only triggers the approximate September 23–October 21 alignment watch; no exam switch date was announced. The unsupported scheduled flag becomes none-announced without removing the watch.

## Teaching and execution

Published seven exact original chart files and executed **27 checks** with checksum-verified [Helm 3.22.0](https://github.com/helm/helm/releases/tag/v3.22.0). Default/file/set precedence, nested merging, zero/string values, names/namespaces/references, checksum changes, release isolation and informational appVersion behaved as expected. Schema errors, an empty required repository and an incompatible declared Kubernetes range were rejected: six intended failures. A mismatched Service selector passed rendering and strict lint; repairing it restored the expected manifests. All public files are hash-matched to the executed inputs.

The exercise used an isolated empty kubeconfig and temporary Helm configuration/cache/data/plugin paths. All owned temporary files were removed. No install, upgrade, rollback, chart dependency, registry, image pull, template network lookup or API operation ran. A supplied Kubernetes version tests local capabilities/range handling, not real server compatibility. The synthetic image was never executed. Docker's Linux engine and native Linux runtime remain unavailable from the preceding probe; no services were started or restarted. All eight complete cluster labs remain **proposed**.

Corrected regular-init/native-sidecar lifecycle and shared-Pod startup/termination simplifications. Added Deployment minReadySeconds and the absence of automatic rollback on a progress deadline. Expanded Job/CronJob duplicate-work boundaries, schema migration examples, quota rejection versus RBAC, effective request defaults, token-mount precedence, ConfigMap/Secret refresh, security/volume scope and EndpointSlice conditions. There are 46 answered original checks and stronger lab acceptance criteria. Numerical cases are explanations; no Kubernetes controller was simulated or tested.

## Release and catalog evidence

George Jenkins's full [June 2 Helm support announcement](https://helm.sh/blog/helm-v3-end-of-life/) extends Helm 3 security fixes through February 10, 2027 and identifies its final limited September 2026 minor release. Accepted the dated tooling boundary, without inferring CKAD's assigned Helm version or testing Helm 4 migration. The previously read ingress-nginx retirement notice remains a controller-specific distinction; the Ingress API/objective remains in scope. The v1.37 release post remains a date-only watch, not a source of new CKAD requirements.

[LFD259](https://training.linuxfoundation.org/training/kubernetes-for-developers/) lists 35 hours and eight chapters, still requiring Linux plus cloud/VirtualBox access; hosted labs from another LF course were not assumed. [Pluralsight](https://www.pluralsight.com/paths/certified-kubernetes-application-developer-ckad-2023) now lists five courses, four labs and 10 hours, including a September 9, 2026 deployment course. There is no separately titled networking course in the visible list, so the guide asks learners to check coverage across the path. [KodeKloud](https://kodekloud.com/courses/certified-kubernetes-application-developer-ckad/) lists 14.75 video hours, 13 modules and 188 lessons; the visible update history still says v1.33 in progress in May 2025, and Kustomize has no visible outline title. These are public metadata gaps, not findings about paid lesson contents or current lab runtime. O'Reilly and Udemy were blocked; inherited durations/dates are explicitly unverified. Practice estimates are planning allowances and Places to learn remains last.

## Validation

The operational receipt records repository tests, repository validation, strict site generation, generated-site checks, catalog consistency and diff checks after execution. Source freshness is current with the stated limits; the review is **reviewed with blockers** because complete image/cluster behavior still needs live validation.
