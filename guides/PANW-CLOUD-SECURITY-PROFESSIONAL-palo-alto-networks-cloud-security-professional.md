---
exam_code: PANW-CLOUD-SECURITY-PROFESSIONAL
vendor_id: palo-alto-networks
official_blueprint: https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/cloudsec-professional-datasheet.pdf
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Palo Alto Networks Certified Cloud Security Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live certification page, August 2025 datasheet, July 2025 certification handbook, Cortex Cloud documentation, public security standards, and selected learning sources were checked September 2, 2026. This does not guarantee that every explanation is error-free or remains current. The [official page](https://www.paloaltonetworks.com/services/education/palo-alto-networks-cloudsec-professional) and [datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/cloudsec-professional-datasheet.pdf) are authoritative.

**Current baseline:** SOC fundamentals 10%; Cortex fundamentals 15%; cloud posture 29%; cloud runtime 26%; application security 20%; August 2025 datasheet<br>
**Exam contract:** professional-level English Pearson VUE certification. Under the checked handbook, Palo Alto Networks exams use an 860 passing score on a 300–1000 scaled range and provisional results. The datasheet omits item count, base duration, and price; verify live registration.<br>
**Experience boundary:** working knowledge of cloud deployments/threats, operating systems, networking, SDLC, vulnerability, compliance, identity, and SOC processes. This is not a generic cloud-fundamentals exam; it asks how Cortex Cloud organizes posture, runtime, application, data, identity, and operations capabilities.<br>
**Validity and renewal:** two years under the July 2025 handbook, subject to current recertification pathway rules.<br>
**Upcoming change:** no retirement or dated replacement was found September 2, 2026. Cortex Cloud packaging and terminology are fast-moving; verify live product documentation throughout study.<br>
**Integrity:** actual exam content is confidential. This guide uses only the public blueprint, original questions, safe labs, and public documentation.

## How to use this guide

Build a single cloud application from source to production and attach each objective to it. For every finding, identify the resource/code/data/identity, collection method, evidence, exposure/path, owner, remediation location, runtime impact, exception, and verification. Do not treat a scan count as risk without context.

Study left to right and back again:

1. source, dependencies, IaC, secrets, and CI/CD;
2. deployed cloud/Kubernetes/AI/data/identity posture;
3. workload and web/API runtime behavior;
4. ingested evidence, incidents, dashboards, reports, and response;
5. remediation in code/config/runtime followed by regression validation.

Use a disposable cloud account/project with budget and teardown controls. Never scan infrastructure or repositories without ownership/authorization.

> **About related items:** A `Related item:` callout adds operational, architectural, governance, implementation, or lifecycle context. It makes the published objective more useful in real work but is not claimed as verbatim exam scope.

## Blueprint map

| Domain | Weight | Evidence of readiness |
|---|---:|---|
| 1. SOC Fundamentals | 10% | Prioritize and manage a cloud incident using defined roles, analytics, intelligence, and AI/ML evidence |
| 2. Cortex Fundamentals | 15% | Govern access/data, onboard sources/assets, interpret indicators, and create defensible dashboards/reports |
| 3. Cloud Posture Security | 29% | Correlate CSPM/KSPM/AI-SPM/DSPM/identity/vulnerability/compliance findings and remediation |
| 4. Cloud Runtime Security | 26% | Select CWP/CDR/WAAS coverage and manage agents without creating blind spots |
| 5. Application Security | 20% | Shift controls into ASPM, pipeline, SCA, IaC, secrets, and scan-management workflows |

## 1. Security Operations Center fundamentals — 10%

A cloud-focused SOC still needs defined monitoring/triage, investigation/response, hunting/detection, cloud/platform, data/automation, intelligence, and command roles. Cloud owners, developers, platform/SRE, IAM, data, privacy/legal, and vendor teams participate. A RACI and escalation matrix prevent the SOC from owning changes it cannot safely make.

Tools combine cloud/provider audit logs, identity, network, workload, Kubernetes, application/API, code/pipeline, data, threat intelligence, SIEM/XDR/SOAR, vulnerability, and posture evidence. Normalize account/project/subscription, region, resource, image, workload, user/workload identity, repository/build/deployment, and timestamps.

ML can classify/anomaly-detect/rank from learned data; AI is broader and includes generative/reasoning systems used for summarization, investigation assistance, and automation. Validate generated findings against raw evidence. Track drift, bias, evasion, privacy, prompt injection, hallucination, confidence, and action authorization.

Threat intelligence helps relate vulnerabilities, behavior, infrastructure, malware, campaigns, and mitigations to incidents. Judge relevance, timeliness, confidence, source, and handling. Categorize incidents by affected layer/use case; prioritize with exposure, exploitability, identity privilege, data sensitivity, runtime behavior, business criticality, scope, and confidence.

> **Related item:** Cloud containment can destroy volatile evidence or production state. Snapshot/preserve what policy requires, coordinate ownership, and choose reversible scope before terminating or redeploying resources.

## 2. Cortex fundamentals — 15%

### Access, entities, indicators, and data

Use users/roles for least privilege and separation across platform administration, cloud onboarding, application security, posture, SOC investigation, response, report, and data access. Govern SSO/MFA, service/API identities, role change/review, emergency access, and audit.

IP, domain, and URL indicators are observables, not proof. Record time, source, confidence, resolution/hosting history, relationships, first/last seen, and affected assets. Shared cloud/CDN infrastructure makes context critical.

Asset inventory should reconcile cloud APIs, Kubernetes, images, workloads, repositories, pipelines, data stores, identities, and agents. Ephemeral resources need event/API/orchestrator-based discovery. Log management covers onboarding, schema/parsing, time, entity normalization, retention/cost, privacy, integrity, and collection health.

Data protection constrains sensitive telemetry, source, secrets, customer data, snapshots, and exports. Rules encode detection/posture/policy logic and require owner, scope, inputs, severity, exceptions, version, tests, and response. Compliance maps controls/findings/evidence to frameworks; it does not guarantee operational security.

### Ingestion, dashboards, and reports

Data-source onboarding requires tenant/account authorization, cloud role permissions, APIs/log routes, network access, region, scope, rate/volume, encryption, validation, and offboarding. Use least-privilege read access unless enforcement needs more, and separate onboarding from response roles.

A dashboard supports current interactive decisions; a report distributes/snapshots defined results. Define audience, question, metrics/denominators, filter/time zone, freshness, exclusions, ownership, and drill-down. Show coverage gaps and expected-versus-seen resources so a low finding count cannot hide failed ingestion.

> **Related item:** A single normalized asset identity connects code, cloud configuration, runtime, data, and incident evidence. Duplicate/stale assets fragment risk and remediation ownership.

## 3. Cloud posture security — 29%

### Posture domains

CSPM discovers/evaluates cloud control-plane configuration, exposure, logging, encryption, network, and service posture. KSPM evaluates cluster/control-plane and workload configuration such as RBAC, admission, pod/security context, secrets, network policy, and exposed services. Findings depend on visibility and benchmark/profile versions.

AI-SPM inventories and evaluates AI services/models/datasets/pipelines/access/configuration and AI-specific risks. Distinguish model/API use, training/fine-tuning, retrieval, and agents. Map data provenance/sensitivity, prompt/output paths, model/supply chain, permissions/tools, monitoring, and lifecycle.

DSPM discovers/classifies sensitive data, maps location/access/exposure/movement, and prioritizes risk. It does not replace data ownership, retention, lawful use, key management, or application-level authorization.

Identity security/CIEM reasoning maps human and workload identities, effective permissions, trust/federation, keys/tokens, unused/excess privileges, escalation paths, and activity. Prioritize a public workload with sensitive data and excessive identity over independent low-context counts.

Vulnerability management inventories software/images/packages/assets, identifies vulnerabilities, considers fix/mitigation, and prioritizes by exploitability, exposure, reachability, privilege, runtime use, data/business context, and compensating controls. A CVSS score is input, not the whole decision.

### Agentless scanning, compliance, and modules

Agentless scanning uses cloud APIs/snapshots or equivalent out-of-band methods to inspect assets without an installed runtime agent. It improves broad inventory and vulnerability/configuration coverage with lower workload footprint, but may be periodic and lack process/runtime context. Govern snapshot/data permissions, regions, encryption, cleanup, and cost.

Unified compliance maps findings/evidence across standards/frameworks and reduces duplicate collection. Record control responsibility, scope, evidence freshness, exceptions, and remediation. One technical check can support several requirements but does not prove the full procedural control.

Posture Security Management Modules organize specialized posture capabilities/workflows in Cortex Cloud. Learn module purpose and how inventory/findings/policies/remediation connect across cloud, Kubernetes, AI, data, identity, vulnerability, and compliance; verify exact current names/licensing in [Cortex Cloud docs](https://docs.paloaltonetworks.com/resources/all-products-a-z).

> **Related item:** Risk correlation is valuable only when relationships are explainable. Preserve the path—exposure → vulnerable runtime → identity permission → sensitive data—so an owner can verify and break it.

## 4. Cloud runtime security — 26%

Cloud Workload Protection covers running hosts, VMs, containers/Kubernetes, serverless, images, and processes with capabilities varying by sensor/agent/agentless/integration. It can prevent/detect malicious behavior, enforce runtime policy, and supply investigation evidence. Identify where enforcement runs and how it behaves during platform/network failure.

Cloud Detection and Response ingests and analyzes cloud control-plane, identity, network, workload, Kubernetes, application, and other evidence to detect/investigate/respond to attacks. Build timelines across API calls, credentials, resources, processes, network, and data. Response can revoke credentials, isolate/quarantine resources, change policy, or orchestrate recovery according to integration and authority.

WAAS protects web applications and APIs against application-layer attacks/abuse through discovery, policy, inspection, and runtime controls depending on deployment. Inventory APIs, schemas, authentication, authorization, input, rate, bot, and data paths. API discovery is not proof that authorization and business logic are secure.

Vulnerability management bridges posture and runtime: confirm whether a package/image/workload is deployed, running/reachable, externally exposed, exploitable, privileged, and connected to sensitive data. Remediation may be dependency/code/image rebuild, configuration, isolation, virtual patching, or compensating control; verify the fixed artifact reaches runtime.

### Agent deployment and management

Define supported platform/architecture, image/container/Kubernetes/serverless method, package/registry, tenant, policy, permissions/capabilities, network/proxy, performance, update, tamper protection, health, logs, scaling/ephemeral coverage, response behavior, staged rollout, rollback, and removal. Avoid granting host/kernel/cloud permissions without documented need.

Measure coverage against authoritative expected assets, not only “agents seen.” Test safe telemetry/detection/response on a canary. Integrate agents/defenders with golden images, DaemonSets/admission/orchestration, or deployment pipelines as appropriate and prevent stale cloned identities.

> **Related item:** Runtime blocking can preserve service or cause an outage. Start with visibility/tuning where risk permits, define fail behavior, and stage prevention with application owners and rollback.

## 5. Application security — 20%

ASPM consolidates and prioritizes application-security findings/context across repositories, pipelines, dependencies, code/IaC/secrets, cloud/runtime, ownership, and policy. It should reduce duplicate findings and route fixes, not become another unactioned dashboard.

CI/CD posture management evaluates pipeline systems, identities, runners, repositories, branch protections, artifacts, integrations, secrets, and deployment permissions. Protect source-to-build provenance, isolated/ephemeral runners, least privilege, review/gates, signed/verifiable artifacts, and audit. A secure application scan cannot compensate for a compromised build pipeline.

SCA identifies open-source/package dependencies, versions, vulnerabilities, and license/supply-chain risk. Include transitive dependencies and runtime reachability, and remediate by update/replacement/removal/mitigation with tests. A lockfile improves reproducibility but does not guarantee integrity.

IaC security scans declarative infrastructure before deployment for exposure, encryption/logging, identity, network, and policy errors. Handle modules/providers, generated plans, variables, environment differences, state, and drift. Validate at runtime because code-to-deployed transformations and manual changes occur.

Secrets scanning finds credential-like material in working trees, history, artifacts, images, logs, and collaboration systems. A discovered secret must be revoked/rotated, dependent services updated, exposure/inappropriate use investigated, history/artifacts treated under policy, and prevention added. Deleting the current line is insufficient.

Scan management defines repositories/assets, tools/types, triggers/cadence, scope/exclusions, policies/gates, severity/prioritization, deduplication, owners/SLAs, exceptions, retest, data retention, and scanner health. Balance fast developer feedback with deeper scheduled or release testing.

Application-security use cases connect developer pull-request feedback, release policy, vulnerability prioritization, exposed IaC risk, secret response, dependency remediation, application inventory/ownership, cloud/runtime correlation, and compliance evidence.

> **Related item:** Fix location matters. Repair a reusable IaC module or base image instead of patching every derived deployment, then redeploy and verify drift is gone.

## Integrated scenarios

### Public container API

Trace repository, dependency, Dockerfile, Kubernetes IaC, pipeline identity/artifact, cluster posture, cloud IAM/data, agent/runtime process, and API requests. Correlate an exploitable package with external route, privileged pod, excessive role, and sensitive database; fix at source and verify new runtime state.

### Exposed cloud key

A scan finds a key in repository history. Validate whether it is real/active, revoke/rotate, update applications safely, inspect cloud audit/runtime/network/data evidence, scope affected resources, preserve evidence, remove leakage paths/artifacts, and add workload identity plus scanning/gates.

### AI retrieval application

Inventory model/API, prompts, retrieval data, vector store, service identities, tools/agents, code/dependencies/IaC, pipeline, cloud posture, runtime, logs, and users. Apply AI-SPM/DSPM/identity/app/runtime controls and test prompt injection, data leakage, excessive tool authority, poisoned data, and unsafe output handling.

## Hands-on labs

1. **Cloud/SOC ownership:** build an asset/data/identity/application RACI, incident categories/priorities, escalation thresholds, and AI-assisted-analysis validation checklist.
2. **Ingestion/asset graph:** ingest synthetic cloud/Kubernetes/code/runtime events, normalize identities/assets/time, introduce a source gap, and build a dashboard/report that exposes denominator/freshness.
3. **Posture matrix:** assess a disposable account and cluster for CSPM/KSPM/identity/vulnerability/compliance findings; build an explainable attack path and remediate the root template.
4. **AI/data posture:** classify synthetic data and an AI application, map model/data/identity/tool risks, and test policy without uploading sensitive material.
5. **Agentless versus agent:** compare snapshot/API findings with runtime sensor evidence, including timing, permissions, blind spots, cost, and cleanup.
6. **Runtime timeline:** simulate harmless process/API/network activity, correlate control-plane and workload evidence, investigate, and design a reversible response.
7. **WAAS/API:** deploy an intentionally simple local API, document inventory/authn/authz/schema/rate/data risks, add tests/controls, and validate both permitted and denied behavior.
8. **Application pipeline:** scan dependency/IaC/secret fixtures, secure the runner/identity/artifact path, triage findings, rotate a synthetic secret, rebuild/redeploy, and verify runtime remediation.

## Original readiness checks

1. Which roles outside the SOC are essential to cloud response?
2. How do AI and ML differ in SecOps?
3. What context should drive incident priority?
4. Why can cloud containment destroy evidence?
5. What belongs in Cortex role governance?
6. Why is an IP/domain/URL indicator not a verdict?
7. Which entity fields connect code, cloud, runtime, and incident evidence?
8. What must a data-source onboarding plan include?
9. How do dashboard and report purposes differ?
10. Why must collection health and denominators be visible?
11. How do CSPM and KSPM differ?
12. What should AI-SPM inventory/govern?
13. What does DSPM add beyond encryption?
14. What does cloud identity security analyze?
15. Why is CVSS insufficient for prioritization?
16. How does agentless scanning work broadly?
17. Which blind spot commonly remains with periodic agentless scanning?
18. What does unified compliance not prove?
19. What is an explainable cloud attack path?
20. How do CWP and CDR differ?
21. What does WAAS protect and what does API discovery not prove?
22. How does runtime context change vulnerability priority?
23. What must precede a runtime response action?
24. How should ephemeral agent coverage be measured?
25. Why stage runtime prevention?
26. What does ASPM consolidate?
27. Which CI/CD assets and identities need posture management?
28. What does SCA analyze beyond direct dependencies?
29. Why does a lockfile not guarantee supply-chain integrity?
30. Why must IaC findings be verified after deployment?
31. What must happen after finding an exposed secret?
32. What belongs in scan management?
33. How should the correct fix location be selected?
34. Which three blueprint domains make up 75% of weight?
35. What is Cortex Cloud's role across those domains?
36. What does scaled 860 not mean?
37. Why are base duration/count/price absent here?
38. How long is the credential valid under the checked handbook?
39. Why must product terminology be rechecked?
40. What must be verified immediately before scheduling?

## Answer key

1. Cloud/platform, development/SRE, IAM, data, application owners, privacy/legal, communications, and vendors as needed.
2. ML is learned statistical technique within the broader AI category.
3. Evidence confidence, exposure/exploitability, identity privilege, data, runtime, business criticality, scope, and impact.
4. Termination/redeployment can erase volatile state/logs unless preservation is planned.
5. Least privilege, separation, identity lifecycle/review, SSO/MFA, service/API access, emergency access, and audit.
6. Shared/reassigned/stale infrastructure and context require corroboration.
7. Cloud tenant/resource, image/workload, repository/build/deployment, user/workload identity, region, and time.
8. Authorization, scope, permissions, APIs/log routes, network/region, volume/cost, protection, validation, health, and offboarding.
9. Interactive current decisions versus distributable/scheduled evidence.
10. Low counts can otherwise hide missing data/assets.
11. Cloud-provider control-plane configuration versus Kubernetes cluster/workload posture.
12. Models/services/data/pipelines/access/configuration plus AI-specific lifecycle and agent/tool risks.
13. Discovery/classification, access/exposure/movement, ownership/retention context, and prioritization.
14. Effective permissions, trust, human/workload credentials, use, escalation paths, and excess/stale access.
15. Exposure, reachability, exploitability, runtime use, privilege, data/business context, and controls change actual risk.
16. Cloud APIs/snapshots or similar out-of-band inspection without workload agent installation.
17. Real-time process/activity context between scans.
18. That every procedural/operational control is fully effective.
19. An evidenced relationship such as public exposure → vulnerable workload → privileged identity → sensitive data.
20. Workload/runtime protection versus cross-source cloud detection, investigation, and response.
21. Web/API traffic and runtime risks; discovery alone does not validate object/function authorization or business logic.
22. Deployed/running/reachable/exposed/privileged status and data/attack-path relationships raise or lower urgency.
23. Target, evidence, authority, service impact, preservation, reversibility, and verification.
24. Compare authoritative expected assets to healthy correctly assigned reporting/protected assets over lifecycle.
25. Blocking can disrupt production and requires tuning, owner coordination, failure design, and rollback.
26. Application inventory/ownership and code/dependency/IaC/secret/pipeline/cloud/runtime findings/context/remediation.
27. Repositories, branches, runners, service identities, integrations, artifacts/registries, secrets, approvals, and deployments.
28. Transitive components, versions, vulnerability/license/provenance, and reachability/use.
29. It pins resolution but does not prove publisher/artifact/build integrity or absence of compromise.
30. Variables, plans, platform defaults, drift, generated resources, and manual changes can alter actual state.
31. Validate, revoke/rotate, update dependents, investigate use/exposure, handle history/artifacts, and prevent recurrence.
32. Assets/scopes, tools/triggers/cadence, policy/gates, severity/dedup, owners/SLAs, exceptions, retest, retention, and health.
33. Fix the earliest reusable source such as module/base image/dependency, then redeploy and verify.
34. Posture 29%, runtime 26%, and application security 20%.
35. Unify their inventory/findings/context/workflows with SOC ingestion, prioritization, investigation, and response.
36. It is not 86% raw correct; it is a scaled threshold across forms.
37. The current public datasheet/handbook omit them; registration is authoritative.
38. Two years, subject to current recertification rules.
39. Cortex Cloud modules, names, licensing, and interfaces evolve faster than the dated blueprint.
40. Active datasheet, current docs/path, registration details, handbook, access/version, and policies.

## Final readiness checklist

- [ ] I can assign cloud/SOC roles, prioritize incidents, and validate AI/ML/intelligence evidence.
- [ ] I govern Cortex users/roles, indicators, logs, assets, rules, compliance, data, ingestion, reports, and dashboards.
- [ ] I correlate CSPM, KSPM, AI-SPM, DSPM, agentless, identity, vulnerability, compliance, and module outputs.
- [ ] I distinguish CWP, CDR, WAAS, vulnerability context, runtime actions, and agent lifecycle.
- [ ] I connect ASPM, CI/CD posture, SCA, IaC, secrets, scan management, and developer remediation.
- [ ] I can explain one source-to-cloud-to-runtime-to-SOC asset/identity/data graph.
- [ ] I completed the three scenarios and eight labs in an authorized disposable environment with teardown.
- [ ] I can prove fixes in source/configuration and in redeployed runtime state.
- [ ] I reject leaked exam content and unauthorized scanning/data uploads.
- [ ] I rechecked the August 2025 datasheet, current Cortex Cloud docs, handbook, and registration before purchase.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Start with the blueprint and official path, then select standards, provider docs, and labs for measured gaps. Cloud/product interfaces change; record the tenant, module, provider, and date used.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Cloud Security Professional page](https://www.paloaltonetworks.com/services/education/palo-alto-networks-cloudsec-professional) | Public | 10–15 minutes | Current credential, datasheet, learning path, and registration |
| [August 2025 datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/cloudsec-professional-datasheet.pdf) | Public PDF | 45–75 minutes | Canonical five-domain scope and terminology |
| [Certification Handbook](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/ebooks/panw-certification-handbook.pdf) | Public PDF | 30–45 minutes | Scoring, ESL, results, retakes, validity, renewal, and integrity |
| [Official digital learning](https://learn.paloaltonetworks.com/learn) | Free account/login may be required | 30 minutes planning; modules vary | Follow the certification-page learning plan and record live durations |
| [Cortex Cloud documentation](https://docs.paloaltonetworks.com/resources/all-products-a-z) | Public | 25–45 hours selected topics/labs | Platform, application, posture, runtime, data, identity, SOC, onboarding, and agents |
| [AWS Security Learning Plan](https://explore.skillbuilder.aws/learn/learning_plan/view/91/security-learning-plan) | Free account; cloud-provider-specific | 10–20 hours selected fundamentals | AWS shared responsibility, IAM, logging, posture, workloads; not Cortex-specific |
| [Microsoft Learn: Implement network security controls in Azure](https://learn.microsoft.com/en-us/training/paths/implement-network-security-controls-azure/) | Free | About 3 hours plus labs | Current Azure network-security path; add identity, logging, and workload modules for broader coverage |
| [Google Cloud security learning](https://cloud.google.com/learn/training/security) | Free/paid paths | 8–20 hours selected content | GCP security and operations context; not Cortex-specific |
| [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) | Public | 8–15 hours selected safe labs | Web/API testing concepts for authorized applications |
| [NIST Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) | Public primary guidance | 3–5 hours | SDLC, supply-chain, build, vulnerability, and remediation practices |
| [Palo Alto Networks YouTube](https://www.youtube.com/@PaloAltoNetworks) | Free video | 4–10 hours selected current videos | Cortex Cloud visual overview/demos; verify current names and licensing |
| [O'Reilly Cloud Security Handbook](https://www.oreilly.com/library/view/cloud-security-handbook/9781119816287/) | Paid; vendor-neutral/broader | 15–25 hours selected chapters | Architecture, IAM, data, workloads, DevSecOps, monitoring, and response context |

No current official practice exam, MeasureUp product, or Whizlabs product explicitly aligned to this exact Cloud Security Professional blueprint was verified. Prefer authorized build-and-defend labs and current product documentation over unsourced question banks.
