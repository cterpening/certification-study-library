# EX280 deep review — September 28, 2026

Same-context AI review; independent human review pending. Reviewed with a documented exam-version blocker. [Study guide](../../guides/EX280-red-hat-certified-system-administrator-openshift.md).

## Scope and version evidence

Read the complete live [exam page](https://www.redhat.com/en/services/training/red-hat-certified-openshift-administrator-exam): 55 tasks in nine groups (14/7/6/5/6/2/5/3/7). The objective and status monitor hashes are unchanged; accepted snapshots were not replaced. The [public version PDF](https://training-lms.redhat.com/public_content/redhat/training/Red%20Hat%20Certification%20Exam%20Objectives%20by%20Version.pdf) independently matches the EX280V422 list after whitespace/ligature normalization, with no remaining text differences. Its older lists are not substitutes for an assigned version. The audit retains the PDF byte hash and comparison evidence.

The page still has 4.22 in its headline and 4.18 in its delivery paragraph. The candidate's assigned version remains controlling. Multiple versions in use does not establish a future effective date, so the catalog's unsupported scheduled-change flag becomes none-announced. An October 5 library follow-up tracks the unresolved wording; it is not a vendor launch date.

## Changes and source reasoning

- Added an original Kustomize base/overlay exercise, generated configuration references and expected changes after a configuration edit, checked against the [Kustomize reference](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/).
- Separated environment, ordinary volume and subPath update behavior using the [ConfigMap reference](https://kubernetes.io/docs/concepts/configuration/configmap/).
- Added a NetworkPolicy fixture and source/port matrix; distinguish AND within a peer, OR across peers and additive allowances using the [upstream policy reference](https://kubernetes.io/docs/concepts/services-networking/network-policies/).
- Explained complementary direct-grant and RBAC evidence for [SCC access](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/managing-pod-security-policies), namespace-scoped grants and actual admission evidence.
- Qualified classic OLM and added [OLM v1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/extensions-overview) resource/console distinctions; clarified frontend/backend [route TLS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ingress_and_load_balancing/routes) checks.
- Answered all 40 knowledge checks. Rechecked official course versions: DO180 and DO280 both advertise 4.22. Qualified blocked OReilly/Udemy metadata and restored Places to learn as the final section.

## Blog intake

Przemysław Roguski's September 10 [network-policy verification article](https://www.redhat.com/en/blog/closing-loop-network-policy-intent-verified-reality) supports designing explicit permitted/denied flows and checking reconciliation at runtime. Accepted only that method; platform-specific ports, host-network generalizations, template claims and the article's agent workflow were not adopted. The earlier April 2018 microsegmentation article was unsuitable as a current implementation resource because its OpenShift 3.7 API/plugin examples are obsolete.

## Validation and limits

Executed 24 local checks: 15 assertions against actual kubectl v1.36.1 / Kustomize v5.8.1 rendering and nine limited NetworkPolicy reference-model cases. The base remains unchanged; the overlay selects the expected replicas, namespace, configuration, labels and ports; configuration content changes both the generated name and pod-template reference. The image is intentionally a non-runnable placeholder and no cluster API was contacted. YAML rendering is not schema admission or network enforcement.

No OpenShift, OAuth, SCC, network, TLS, Operator, quota or clean-replay lab was executed. Eight platform labs remain proposed. Repository validation, 175 unit tests, strict site build, generated-site validation, catalog consistency and diff checks are recorded in the operational receipt after execution. The PDF direct GET succeeded despite an initial general-checker block; both observations are retained. OReilly/Udemy access restrictions remain limitations, not evidence that their pages disappeared.
