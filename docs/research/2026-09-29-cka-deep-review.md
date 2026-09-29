# CKA deep review — September 29, 2026

Same-context AI review; independent human review pending. [Study guide](../../guides/CKA-certified-kubernetes-administrator.md).

## Exam scope and lifecycle

The [official CKA page](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/) still specifies Kubernetes **v1.35**. All 27 competencies were read and mapped in guide order: 8/5/6/3/5, weighted 25/15/20/10/30. The actual [CNCF v1.35 PDF](https://raw.githubusercontent.com/cncf/curriculum/master/CKA_Curriculum_v1.35.pdf) was downloaded and fully read: three pages, 169,029 bytes, with a hash receipt. Its outline matches the live page after typography/order normalization. A GitHub file-viewer shell was not treated as the PDF body.

The two-hour performance exam, two-year validity, 12-month eligibility, one retake and two 36-hour simulator activations remain listed. Simulator task counts are not generalized to the exam. Both monitor hashes are unchanged; accepted baselines were not rewritten. The August 26 v1.37 release remains a watch trigger under the approximate four-to-eight-week alignment policy. September 23–October 21 is not an announced exam transition, so the unsupported scheduled flag becomes none-announced while the watch text remains.

## Teaching and actual execution

An exact original Python/PyYAML example passed **22 local checks**, using checksum-verified Windows kubectl **v1.35.9** and bundled Kustomize **v5.7.1**. It generated a Deployment client-side, rendered base/overlay manifests, checked replicas/images/namespaces/selectors/ports, followed generated ConfigMap names and references through a content change, and verified stable rendering. Missing resources, duplicate resources and an invalid patch failed as intended. A wrong Service selector rendered successfully, demonstrating the limit of rendering checks. The example and execution receipt are hash-matched.

Temporary files and an isolated empty kubeconfig were removed. No existing cluster credentials were read, no image was pulled, no API request was made and no server admission or traffic was tested. Docker's Linux-engine named pipe was unavailable; the earlier native Linux runtime blocker remains deferred. No service was started or restarted. All eight complete cluster labs remain **proposed**.

Corrected readiness/EndpointSlice simplifications: unready addresses can remain listed, so conditions matter. Removed the implication that PDBs directly constrain Deployment rollouts; added separate rollout and eviction-budget rounding. Expanded additive/namespaced RBAC, ConfigMap consumption refresh, HPA metric errors, Gateway attachment versus backend permission, RWO versus RWOP, delayed binding with scheduler bypass, component skew and etcd revision/cache recovery. Numerical examples are explanations, not controller tests. There are 46 answered original checks and stronger success/failure criteria in the eight labs.

The guide links targeted **release-1.35 upstream documentation sources**, fetched and read after several rendered HTML pages timed out or failed. Original attempts are retained in the receipt. Current Gateway API and etcd 3.6 sources are explicitly version-sensitive operational references, not proof of exam component versions. The code exercise is local rendering; kubeadm/HA/recovery, RBAC/admission/operators, controllers, CNI/policy/DNS/Gateway and CSI/storage behavior still need live validation.

## Blog and catalog intake

Tabitha Sable's November 11, 2025 [ingress-nginx retirement notice](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/) was fully read. Retained its controller-retirement distinction; it does not retire the Ingress API or CKA objective. No migration was executed. The [v1.37 announcement](https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/) was used only for release-date watch; its full feature body was not reviewed or adopted into this guide.

[LFS258](https://training.linuxfoundation.org/training/kubernetes-fundamentals/) lists 35 hours, 17 chapters and hosted browser labs, with Helm/Kustomize, CRDs and Gateway API scope. Optional self-managed cloud labs may cost money. [Pluralsight](https://www.pluralsight.com/paths/certified-kubernetes-administrator) lists 15 courses, six labs and 30 hours, mixing older material with 2026 additions. [KodeKloud](https://kodekloud.com/courses/cka-certification-course-certified-kubernetes-administrator/) now lists 26.12 video hours, 17 modules and 306 lessons, an April 10 v1.35 lab update and separate September 2025 video update. O'Reilly and Udemy were blocked; earlier runtime claims are expressly unverified. Only public metadata was assessed. Added lab times are planning estimates, and Places to learn remains last.

## Validation

The operational receipt records repository tests, repository validation, strict site build, generated-site checks, catalog consistency and diff checks after execution. Review outcome remains **reviewed with blockers** because live cluster validation is incomplete; source freshness is current with the version watch and access limitations above.
