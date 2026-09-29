---
exam_code: GOOGLE-PROFESSIONAL-CLOUD-ARCHITECT
vendor_id: google-cloud
official_blueprint: https://cloud.google.com/learn/certification/cloud-architect
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# Google Cloud Professional Cloud Architect Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 29, 2026. Human review is still pending. See the [coverage record](../docs/SOURCE-VALIDATION.md#google-professional-cloud-architect-coverage-record). The [official certification page](https://cloud.google.com/learn/certification/cloud-architect) and [detailed exam guide](https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf) are authoritative.

**Current baseline:** Six domains weighted approximately 25%, 17.5%, 17.5%, 15%, 12.5%, and 12.5%; actual seven-page guide and all four case-study PDFs read September 29, 2026; 101 mapped statements (96 bullets plus five standalone objectives) under 22 numbered objectives<br>
**Published change notice:** Google says the exam was updated for recent branding changes and directs candidates to the exam guide for current product names. No future effective date is announced.<br>
**Official source:** [Certification page](https://cloud.google.com/learn/certification/cloud-architect) · [exam guide](https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf) · [Architecture Center](https://cloud.google.com/architecture)

## How to use this guide

PCA is an architecture judgment exam. For each requirement, identify the business outcome, constraints, workload and data shape, users and trust boundaries, required service levels, change/migration path, shared responsibility, cost model, evidence, and exit/rollback. Then choose the simplest design that satisfies those facts. A technically possible choice can still be wrong because it adds operations, violates sovereignty, misses recovery, or cannot be adopted.

The standard exam is two hours, USD 200 before applicable tax or regional differences, 50–60 multiple-choice and multiple-select questions, available in English and Japanese, online or onsite, and valid for two years. Google lists no prerequisite and recommends three or more years of industry experience including at least one year designing and managing Google Cloud solutions. **VERIFY CURRENT:** The standard exam uses two cases, with case questions comprising 20–30% of the exam. The one-hour renewal exam costs USD 100 before tax, contains 25 questions in English/Japanese and grants two-year validity; one generative-AI case accounts for 90–100% of that exam. Its separate guide lists two available cases. A designated Google Skills course/badge renewal route grants one-year validity, requires linked accounts and eligible completion within the final active year. This guide maps the standard blueprint and its four cases; it does not substitute for the renewal guide. Verify the [live page](https://cloud.google.com/learn/certification/cloud-architect) and your eligibility before scheduling.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context. It improves the decision model; it is not a claim that the item appears verbatim in the published objectives.

## Objective map

| Published domain | Weight | Architecture outcome |
|---|---:|---|
| Designing and planning a cloud solution architecture | ~25% | Trace business and technical requirements to a defensible target and migration plan |
| Managing and provisioning cloud solution infrastructure | ~17.5% | Translate the target into governed network, compute, data, AI and platform configuration |
| Designing for security and compliance | ~17.5% | Build identity, data, software, AI and compliance controls into the architecture |
| Analyzing and optimizing technical and business processes | ~15% | Make delivery, recovery, cost, skills, change and decisions repeatable |
| Managing implementation | ~12.5% | Guide teams through tested deployment, migration, APIs, automation and programmatic operation |
| Ensuring solution and operations excellence | ~12.5% | Operate through observability, releases, support, quality, resilience and continuous improvement |

The [Well-Architected Framework](https://cloud.google.com/architecture/framework) is a cross-cutting baseline: operational excellence, security, reliability, cost optimization, performance optimization, and sustainability. Never optimize one pillar without stating the effect on the others.

---

## 1. Designing and planning — about 25%

### Begin with an architecture contract

Functional requirements describe behavior; non-functional requirements constrain quality such as availability, latency, recovery, security, scalability, auditability, portability, sustainability, and cost. Convert vague terms into measurable targets and workloads: users/regions, requests or events, data volume/growth, read/write mix, consistency, peak/steady behavior, dependencies, RTO/RPO, deployment frequency, and regulatory location.

Record each decision as context → options → choice → tradeoff → owner → validation → revisit trigger. KPIs and ROI connect technical work to business outcomes; SLIs/SLOs and cost/performance/security measures show whether the solution works in production. Observability, recovery, compliance, and operational ownership are requirements, not decorations added after deployment.

Disposition each workload: retain, retire/deprecate, rehost, relocate, replatform, refactor, repurchase/buy, or build. Prefer managed services when their functional, control, locality, cost, portability and operational contracts fit. “Cloud first” means considering cloud-native value early, not forcing migration when constraints do not support it.

### Design reliability and continuity from failure modes

Map component, zone, region, identity, network, dependency, data corruption, operator, deployment, capacity, and provider failures. High availability maintains service through likely faults; disaster recovery restores after a major disruption. Backups are data copies, not a complete DR plan. Define RTO, RPO, failover/failback, data consistency, dependency recovery order, degraded mode, communication, and test evidence.

Zonal, regional and multi-region designs have different blast radius, latency, data, cost and operational consequences. Managed multi-zone service does not prove application resilience if a global configuration, identity, pipeline, DNS, third-party dependency, or corrupt write remains a single failure path.

Make the recovery dependency graph explicit. Detection, declaration, identity/key access, networking, data recovery, application restart and business validation all consume time; some tasks can run in parallel while others depend on them. Google's [DR planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide) includes recovery access, deployment artifacts, capacity and realistic tests. An isolated 30-minute database restore is not a measured 30-minute business recovery. The worksheet below calculates a fictional 68-minute critical path despite parallel network/identity work; neither an RTO target nor an availability percentage proves that time will be achieved.

For example, [Cloud SQL PostgreSQL regional HA](https://docs.cloud.google.com/sql/docs/postgres/intro-to-cloud-sql-disaster-recovery) does not itself survive loss of its whole region. Cross-region replication is asynchronous, so promotion can lose unreplicated committed writes. A complete recovery includes client redirection, preventing writes to the old primary, validation and restoring protection around the new primary. [Promotion documentation](https://docs.cloud.google.com/sql/docs/postgres/replication/cross-region-replicas) separates ordinary intentional promotion from edition-specific advanced DR. A controlled switchover after catch-up can avoid data loss; an outage failover with replication lag is a different condition. Confirm engine, edition, topology and procedure before promising an RPO.

Scalability is ability to meet growth; elasticity adjusts resources with demand. Load test realistic traffic and dependency limits. Performance design includes latency budget, throughput, concurrency, locality, caching, storage/query layout, accelerator utilization, and price-performance. Gemini Cloud Assist may surface recommendations, but architecture authority remains with accountable humans and tested evidence.

### Choose platform components by contract

Compute Engine fits guest/OS control and legacy or specialized workloads. Managed instance groups add templates, autoscaling and autohealing. GKE fits Kubernetes APIs/ecosystem and portable container orchestration; Autopilot reduces node operations while Standard exposes them. Cloud Run fits stateless request/event containers with managed scaling. Cloud Run functions fits event/function packaging. Spot capacity fits interruptible work. GPUs/TPUs fit evaluated accelerator workloads with quota, topology, capacity and fallback plans.

For data, choose by model, query/access pattern, consistency/transactions, scale, locality, latency, availability, recovery, ecosystem, operations and cost—not by a memorized service hierarchy. Typical choices include Cloud Storage/Filestore for objects/files; Cloud SQL/AlloyDB for managed relational compatibility; Spanner for scalable relational/global consistency; Firestore for documents; Bigtable for wide-column throughput; BigQuery for analytics; Pub/Sub for messaging; Dataflow for batch/stream processing; and Memorystore for cache.

Network design covers VPC/subnets, Shared VPC, peering, routes, Cloud NAT/DNS, firewall/Cloud NGFW policies, Private Service Connect, load balancing, hybrid/multicloud VPN or Interconnect, service networking, GKE networking, address capacity, observability and ownership. Prefer private and least-privilege paths, but do not confuse private addressing with authorization or encryption.

AI architecture starts with task and consequence. Select application/API/model/platform/agent/accelerator layers; permitted data; grounding, customization and evaluation; human authority; tool identity and limits; monitoring and rollback. Current scope names Gemini models/LLMs, Model Garden, Agent Builder, Gemini Enterprise Agent Platform and AI Hypercomputer. Verify release stage and region because this surface changes rapidly.

### Migration is a program, not a copy operation

Discovery captures inventory, dependency, usage, data, licenses, risk, owner, cost and readiness. Use Migration Center and other assessment/migration tooling where suitable, then define waves, landing-zone prerequisites, connectivity, data transfer/synchronization, test, cutover, rollback, decommission and success evidence. Diagrams must show boundaries, flows, identities, protocols, failure domains, data stores, observability and external dependencies.

Data migration considers volume, bandwidth, change rate, allowable downtime, consistency, validation, encryption, residency and rollback. License implications can alter the target’s feasibility. A pilot can supply evidence for the migration mechanism; it does not establish full-estate capacity or organizational readiness. Measure the rate at which changes arrive as well as effective transfer/replay throughput. In a deliberately simplified example, a 900 GiB backlog draining at 100 MiB/s while 80 MiB/s of new work arrives takes 12.8 hours, not the 2.56-hour no-new-write estimate. If arrivals equal or exceed throughput, it does not converge. Compression, retries, apply bottlenecks and uneven writes require measurement. Define write fencing, reconciliation, cutover acceptance and a rollback data path: routing clients back to an old database after new writes is not data rollback.

> **Related item:** A landing zone is a repeatable governed foundation—hierarchy, identity, policy, network, logging, billing, security and automation—from which workload environments are provisioned.

---

## 2. Managing and provisioning infrastructure — about 17.5%

### Provision networks, storage and compute as products

Central platform teams should expose opinionated, versioned, supportable patterns without becoming a bottleneck. Shared VPC and hierarchical firewall policy can centralize network guardrails while service projects retain workload ownership. Hybrid connectivity needs redundant devices/links, dynamic routing choices, route/firewall/DNS design, encryption, capacity monitoring, failure testing and documented ownership. Multicloud adds identity, data, observability, egress and cross-provider failure contracts; it does not automatically improve resilience.

Storage configuration implements location, capacity/performance, access, encryption/key model, transfer, retention/lifecycle, versioning, backup/replication and growth forecasts. Data protection must cover accidental deletion/corruption and malicious action, not only infrastructure failure. Separate production administration from backup/key authority where the risk requires it.

Compute configuration covers immutable templates/images, service identity, network, capacity/scaling, placement, patching, configuration management, orchestration, health and release. Standard versus Spot is a workload resilience decision. VMware Engine can support VMware estate relocation/integration, but assess cost, network, licensing, modernization path and operational ownership rather than treating it as an endpoint by default.

Terraform or another IaC mechanism should be modular, reviewed, policy-checked, tested and promoted through environments. Protect state and pipeline identity, review destroy actions, detect drift, and verify deployed behavior. A service catalog can wrap these patterns with approved parameters and ownership.

**Private connectivity has a direction and a service boundary.** [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) endpoints let consumers initiate access to producer services; backends add a consumer load balancer, while interfaces allow producer-initiated access into consumer networks. Interfaces can reach connected networks, so inspect the resulting paths. This is not interchangeable with unrestricted VPC peering. Record the selected feature, supported service/region, DNS, acceptance and application identity controls.

### Provision AI/ML and agents as governed systems

The current guide calls for Agent Platform Pipelines, data integration, AI Hypercomputer, GPU/TPU training and serving, consumption-model optimization, Google AI APIs, Gemini Enterprise agents/NotebookLM and Model Garden integration. Names are volatile; the durable architecture is:

data/rights → preparation/features or retrieval → model/API choice → training/customization → registry/version → evaluation → deployment/serving → monitoring → feedback/retraining or retirement.

AI Hypercomputer combines accelerator, network/storage/system design and software. Select by model/framework, training versus inference, scale/topology, utilization, latency/throughput, capacity, price, sustainability and operational skill. For agents, bind tools to narrow workload/end-user identity, validate arguments, restrict destinations/actions, require approval for consequential changes, log decisions/actions, design idempotency and reversal, and continuously evaluate safety and task success.

Specialized Search, Conversation, Vision, Image, Video and Audio APIs may give a narrower managed contract than a general model. Model Garden expands choice but adds license, provenance, model risk, data, evaluation and lifecycle decisions. NotebookLM/Gemini Enterprise labels do not by themselves establish an enterprise API or data contract. Distinguish the employee app, developer platform, model endpoint and notebook account. [Agent Platform retention documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention) separates training restrictions from enabled logs, grounding, state and other retention. [Search identity configuration](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider) makes identity mapping and ingestion/federation choices part of access design; provider changes do not automatically update existing stores. Test revoked access before retrieval context is constructed and before an action executes. Use Model Garden for discovery and [Model Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction) for applicable owned model/version lifecycle; do not treat a catalog listing as a deployed, evaluated endpoint.

> **Related item:** MLOps/LLMOps extends DevOps with data, feature/retrieval, prompt, model, evaluation and monitoring artifacts. A deployment pipeline alone does not control model behavior.

---

## 3. Security and compliance — about 17.5%

### Identity-first, layered design

Use organization/folder/project boundaries, organization policy, group-based human roles, purpose-specific workload identities, short-lived credentials and federation. Basic roles are too broad for routine use. Separate duty among platform, security, application, data, billing, key and audit roles. Privileged access should be approved, time-bound where possible, logged, reviewed and recoverable.

Service-account impersonation, Workload Identity Federation and Workload Identity Federation for GKE reduce long-lived keys. Identity-Aware Proxy can mediate context-aware access to applications and administrative paths. Chrome Enterprise Premium/context-aware access can add device and context signals. These controls complement application authorization. Diagnose the actual credential path: [ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials) is distinct from CLI authentication. In GKE, [direct workload IAM and optional service-account impersonation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) differ from node image-pull identity; matching principals across clusters in a shared project pool can share permissions. Define trust boundaries rather than relying only on namespace names.

Protect data through classification, minimization, authorized location/flow, IAM, VPC Service Controls for data-exfiltration boundaries, encryption, secrets, retention/deletion, logging and recovery. Google-managed encryption is default; CMEK through Cloud KMS adds customer-controlled key lifecycle plus new availability, permission, rotation, disablement/destruction and separation-of-duty risks. [KMS rotation](https://docs.cloud.google.com/kms/docs/key-rotation) creates a new key version; it does not itself rewrite all ciphertext or delete the old version. [CMEK integrations](https://docs.cloud.google.com/kms/docs/cmek-rotation) vary: a resource may rewrap existing data keys, use the new version only for new data, or keep the originally configured version. Check the exact resource and old backup dependencies before retiring a version; a schedule alone is not recovery evidence. Secret Manager manages secret versions/access; do not store secrets in images, source, Terraform variables/state or ordinary environment files without a controlled mechanism.

Software supply-chain design covers trusted source, review, dependency/SBOM, build isolation, short-lived pipeline identity, artifact scanning/signing/provenance, protected registry, policy-based admission, runtime hardening, vulnerability response and rollback. Separate [provenance, scanning and admission](https://docs.cloud.google.com/software-supply-chain-security/docs/overview). A signed attestation binds a claim about a particular artifact/process to a trusted signer; it does not independently prove all vulnerabilities are absent. Define which signer and digest are accepted, how scan age/severity exceptions are handled, where policy enforces admission and how emergency bypass is audited. Reassess running artifacts as new vulnerabilities appear. Penetration/security testing must be authorized and scoped.

AI security includes prompt injection, poisoned or unauthorized data, sensitive-data disclosure, insecure tool/action use, model/supply-chain risk, excessive agency, denial/cost abuse and unsafe output. Use Sensitive Data Protection, Model Armor where its current contract fits, grounding permission filters, input/output controls, deterministic authorization, sandbox/allowlists, evaluation/red teaming, monitoring, human escalation and stop controls. No single filter makes an agent secure. [Model Armor](https://docs.cloud.google.com/model-armor/overview) detection, refusal and enforcement in the calling application are distinct; [integration/modality coverage](https://docs.cloud.google.com/model-armor/integrations) must match the actual request path. In a media pipeline, verifying a text prompt filter is not evidence that every audio/video asset was inspected. Confirm the current integration's supported payload types and route rejected or unassessed material to the chosen review process.

### Turn compliance obligations into controls and evidence

Legal, regulatory, contractual and industry requirements determine permitted data, purpose, consent, residency/sovereignty, retention/deletion, access, encryption/key ownership, supplier terms, incident reporting and audit evidence. A service certification such as SOC 2 is useful assurance evidence, not automatic compliance for the customer workload.

Build a requirement-to-control-to-owner-to-evidence matrix. Evidence may include policy configuration, effective access, key logs, deployment provenance, data lineage, audit logs, test results, retention execution, incident records and approved exceptions. Confirm shared responsibility, current product/regional compliance, and contract terms with qualified organizational experts.

> **Related item:** VPC Service Controls reduce specified data-exfiltration paths around supported services. They are not a replacement for IAM, encryption, application authorization, network policy or classification.

---

[VPC Service Controls dry run](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode) evaluates and logs potential violations without applying those dry-run denials. An existing enforced perimeter still enforces its own rules. A clean test log is meaningful only for the methods, identities and paths actually exercised; dry run is not deployed protection, and absent traffic is not a successful exfiltration test. Validate required ingress/egress and negative cases before controlled enforcement.

## 4. Optimize technical and business processes — about 15%

### Technical process

A reliable SDLC defines source control, review, tests, security checks, artifact provenance, environment promotion, release strategy, migrations, observability, approval, rollback and learning. CI validates/integrates change; delivery/deployment promotes it under defined control. Unit tests isolate logic; integration tests verify component contracts; load tests prove capacity behavior; chaos experiments test resilience hypotheses with bounded blast radius.

Troubleshooting should be evidence-led: define symptom/impact/time, identify recent changes, compare healthy/unhealthy paths, inspect metrics/logs/traces/configuration, form and test hypotheses, stabilize, correct root cause, verify user outcome and record prevention. A root-cause label without contributing control/process analysis is incomplete.

Disaster recovery is a recurring process: inventory/dependency, backup/replication, runbook/automation, access, communication, exercise, measured RTO/RPO, remediation. A service catalog makes supported patterns discoverable and provisionable; product owners maintain versions, constraints, SLOs, support and retirement.

### Business process

Map stakeholder influence, decision rights and success criteria. Use architecture decision records and explicit escalation for unresolved risk. Change management includes sponsorship, communication, training, role/process redesign, champions, adoption telemetry, support and feedback—not merely a release announcement.

Assess skills and operating-model gaps early. Build/buy/partner and central/federated ownership choices affect time, risk, differentiation and long-term cost. Customer success measures realized outcomes after deployment. FinOps connects visibility, allocation, optimization and governance; compare CapEx/OpEx and total cost including people, migration, network egress, support, licenses, risk and decommissioning.

Business continuity includes people, facilities, suppliers, identity, communications and manual/degraded procedures in addition to technical recovery.

---

## 5. Managing implementation — about 12.5%

Guide teams with reference architectures, paved paths, acceptance criteria, threat/data reviews, test strategy, dependency contracts, deployment/recovery runbooks and production-readiness reviews. Preserve team accountability: an architect advises and verifies; operations and product owners need clear authority.

Migration implementation uses rehearsal, data validation, coexistence/synchronization, cutover criteria, freeze/change control, rollback and decommission evidence. Application and infrastructure releases should be independently reversible where practical. Schema/API compatibility matters during rolling or canary deployment.

Apigee fits governed API-product management: proxy/policy, authentication/authorization, quotas/rate limits, analytics, developer/app lifecycle and versioning. Google API best practices include resource-oriented design where relevant, consistent errors, idempotency/retries, pagination, long-running operations, compatibility, quotas and secure credentials. Prefer supported client libraries/SDKs over handwritten protocol handling.

Cloud Shell Terminal/Editor and Cloud Code provide managed development/administration surfaces. `gcloud`, `gsutil`, and `bq` automate platform, storage and analytics tasks; use supported current commands and explicit project/account/region. Emulators for services such as Bigtable, Spanner, Pub/Sub and Firestore improve fast isolated testing but do not reproduce every production IAM, quota, scale, network or failure behavior.

Terraform plans must be reviewed and promoted by controlled identities. Gemini Cloud Assist can explain, generate or troubleshoot; validate its commands and architecture changes against current docs and real state.

---

## 6. Solution and operations excellence — about 12.5%

Operational excellence means clear ownership, documented/automated repeatable work, measured outcomes, controlled change, incident learning and continual improvement. Build golden signals and workload-specific SLIs, SLOs and error budgets. Logs explain events, metrics quantify behavior, traces connect requests, and profiles/benchmarks expose resource/code performance. Route alerts only when an owner can act; link runbooks and test notification paths.

Release strategies—rolling, blue-green, canary, traffic splitting and feature flags—trade speed, capacity, complexity and rollback. Separate deploy from release when useful. Observe user and dependency behavior, security and cost during promotion. A rollback must account for schema/data/API compatibility. Database expand/migrate/contract phases and old/new-client coexistence need explicit acceptance evidence. A healthy new binary cannot prove a safe rollback after destructive schema or business-data changes.

Quantify error-budget consumption using an explicitly defined population and window. For an illustrative request SLO of 99.9%, a 2% bad-request fraction is a 20× burn rate: `0.02 / (1 - 0.999)`. For a separate time-based 30-day illustration, 99.9% permits 43.2 minutes of unavailability; that is not automatically the allowed duration of one incident or an RTO. [Google SRE's alerting chapter](https://sre.google/workbook/alerting-on-slos/) explains long/short-window confirmation and low-traffic pitfalls. Its low-traffic example labels one failure among ten requests as 1,000×, but the published formula gives **100×**; the worksheet checks the arithmetic. Choose thresholds and paging policy for the service, and keep synthetic checks from hiding real-user failures.

Support requires severity/impact definitions, on-call/escalation, dependency/vendor paths, status communication, evidence preservation, recovery authority and post-incident learning. Quality controls include tests, policy gates, data validation, SLO/error-budget review, vulnerability/configuration checks, cost/performance regression and manual approval where consequence warrants it.

Reliability validation uses realistic load, failure injection/chaos, recovery exercises and authorized penetration testing. State the hypothesis, blast radius, abort condition, monitoring and recovery before an experiment. Production is not the first time failover, restore, scaling or incident roles should be exercised.

---

## Working with the official case studies

Google identifies four fictitious cases in the current guide: [Altostrat Media](https://services.google.com/fh/files/misc/v6.1_pca_altostrat_media_case_study_english.pdf), [Cymbal Retail](https://services.google.com/fh/files/misc/v6.1_pca_cymbal_retail_case_study_english.pdf), [EHR Healthcare](https://services.google.com/fh/files/misc/v6.1_pca_ehr_healthcare_case_study_english.pdf), and [KnightMotives Automotive](https://services.google.com/fh/files/misc/v6.1_pca_knightmotives_automotive_case_study_english.pdf). For each, create one page with:

1. business model, desired outcomes and KPIs;
2. current estate, teams, constraints and pain;
3. explicit business and technical requirements;
4. data classes, identities, geographies and trust boundaries;
5. target service choices with rejected alternatives and tradeoffs;
6. migration waves, coexistence, cutover, rollback and decommission;
7. availability, RTO/RPO, degraded operation and test plan;
8. security/compliance controls and evidence;
9. cost, skills/adoption and ownership;
10. observability, SLOs, release, support and improvement triggers.

Do not memorize a single “answer architecture.” A changed requirement should change the design. The actual PDFs above were read in full (3/4/2/3 pages). The table distinguishes published facts from original design hypotheses and proposed verification:

| Case and published constraint | Design hypothesis to compare | Evidence or question that could change it |
|---|---|---|
| **Altostrat Media:** already uses GKE, Cloud Storage, BigQuery and event functions; some ingestion/archive remains on premises. Reliability and cost lead the priorities, alongside summarization, metadata, moderation and explainability. | Evolve the existing pipeline in stages, preserve hybrid ingestion, version derived metadata and evaluate each media type before publication. | Measure ingest/reprocessing latency and failed-asset handling; test whether selected moderation covers the actual media. Determine rights, retention and quality thresholds rather than assuming them. |
| **Cymbal Retail:** heterogeneous data and file/batch integration; generated attributes/images; explicit associate approval/rejection/editing **before** catalog updates. | Separate candidate generation from approved publication, bind review to the exact candidate and current source version, and keep authoritative stock/price outside unconstrained generation. | Reject stale or edited approvals; compare attribute correctness by category and conversion against returns/corrections. Clarify reconciliation and approval ownership. |
| **EHR Healthcare:** an expiring colocation lease, containerized apps, Active Directory, ignored email alerts, minimum 99.9% customer-facing availability; existing insurance interfaces are **not planned to move now**. | Migrate suitable application waves while retaining those interfaces over tested hybrid connectivity; preserve identity and improve actionable monitoring. | Derive the SLI/window and RTO/RPO with stakeholders; test dependency/identity failure and restore before lease exit. Do not invent an RTO from the availability figure or prescribe immediate migration of retained systems. |
| **KnightMotives Automotive:** five-year experience modernization, fragmented vehicle software, rural/plant connectivity problems, legacy core systems and no dealer budget for new equipment. | Phase hybrid modernization, design degraded-connectivity behavior and dealer tools compatible with available equipment, and evaluate vehicle hardware changes separately. | Test disconnected/resynchronization behavior and rollback; validate data-use rights and staged simulation evidence. The fictional executive's safety assertion is not independent proof of autonomous-driving safety or regulatory approval. |

None of these hypotheses is an official answer key. The cases do not supply every threshold, topology, contract or budget; record missing facts as assumptions to verify.

## Integrated practice scenarios

### 1. Global retail modernization

A retailer needs low-latency browsing, transactional orders, global analytics and burst handling. Separate static/object delivery, stateless compute, transactional database, asynchronous fulfillment and analytical pipeline. Choose regional versus global data architecture from consistency, locality, sovereignty and recovery facts. Add identity, inventory/event idempotency, SLOs, canary release, cost allocation, failure testing and a phased migration from the legacy system.

### 2. Regulated document agent

Employees ask an agent questions over controlled records and may initiate bounded workflows. Enforce end-user permissions at retrieval/action time; classify/minimize data; choose authorized model/region; ground and cite; validate tool arguments; use short-lived identity, transaction limits and approval; log evidence; evaluate retrieval, faithfulness, safety and task success; retain/erase according to policy; provide abstention, escalation, shutdown and rollback.

### 3. Hybrid platform consolidation

Business units need shared networking/security but independent delivery. Use landing-zone hierarchy, policies, Shared VPC/service projects, redundant hybrid connectivity, centralized DNS/logging/billing, federated identities and modular IaC/service catalog. Define delegated roles, quota/capacity, change ownership, DR and platform SLOs. Migrate by dependency-aware waves and measure adoption and decommissioned cost. Trace producer/consumer direction for each Private Service Connect path, test credentials in the recovery environment, and preserve the interfaces explicitly retained by the business.

## Hands-on evidence path

These eight cloud exercises are **proposed, not executed in this review**. Use an authorized disposable scope and synthetic data, record owner/cost/cleanup, and preserve observed results separately from expectations.

| Exercise | Acceptance evidence | Failure/recovery case |
|---|---|---|
| 1. Architecture contract | Trace one case's facts to quantified targets, constraints, alternatives and decision owners | Change a constraint and explain the revised design; mark invented thresholds explicitly |
| 2. Landing-zone slice | Show effective hierarchy/IAM/network/logging/billing configuration and named administration/recovery roles | Wrong identity and denied service path must fail for the intended reason; recover access without broadening unrelated roles |
| 3. Compute comparison | Deploy the same small service on chosen candidates and compare operational work, latency, identity, cost and rollback | Measure dependency connections under scale/rollout; a maximum-instance setting alone is not a hard budget |
| 4. Data and migration | Trace source changes, replay, business keys, reconciliation and a measured catch-up curve | Stop/restart transfer, inject duplicates, fence writes and test rollback after target writes |
| 5. Hybrid network | Document redundant paths, PSC feature/direction, DNS, routes and firewall layers | Lose a link or name-resolution path; show remaining capacity and client behavior, not merely a topology diagram |
| 6. Governed content/agent | Evaluate synthetic retrieval and tool actions; bind human review to the exact proposed content/version | Revoke access, alter content after approval and inject untrusted instructions; confirm actual enforcement and escalation |
| 7. Delivery/IaC | Review immutable artifact digest, signer/process evidence, current scans, admission and controlled plan/apply | Reject wrong digest/signer or stale evidence under the stated policy; exercise compatible application/schema rollback |
| 8. Recovery and operations | Measure user-visible recovery, recovered data point, identity/key access, paging and restored redundancy | Test unavailable primary, old-primary fencing, missing key/permissions and failback; use disposable keys and avoid irreversible destruction |

### Offline architecture worksheet — executed

Save the following as `pca_architecture_workbook.py` and run `python pca_architecture_workbook.py`. The exact standard-library code passed **32 checks** on September 29, 2026. It sends no requests and changes no infrastructure.

The deterministic recovery graph assumes unlimited parallel workers and invented task durations; its result is planning arithmetic, not measured RTO. Backlog arithmetic assumes steady effective rates and no additional transfer/apply overhead. Burn rate uses a stated request population; the separate time budget assumes a 30-day time-based SLO. The approval model assumes trusted reviewer identities and approval records; hashing binds content but does not authenticate a reviewer, prove content correctness, or provide an atomic publication transaction. A real workflow must revalidate and commit atomically under its actual authorization and concurrency rules.

```python
"""Offline planning models; no cloud, vehicle, medical record or model call."""
from decimal import Decimal, InvalidOperation
import hashlib
import json


def number(value):
    if isinstance(value, bool):
        raise ValueError("Boolean is not a measured quantity")
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError("Invalid quantity") from exc
    if not result.is_finite() or result < 0:
        raise ValueError("Use a finite nonnegative quantity")
    return result


def recovery_schedule(tasks):
    # Unlimited parallel workers and deterministic durations; not a measured RTO.
    if not tasks:
        raise ValueError("Recovery plan is empty")
    normalized = {name: (number(duration), tuple(deps))
                  for name, (duration, deps) in tasks.items()}
    if any(dep not in tasks for _, deps in normalized.values() for dep in deps):
        raise ValueError("Missing prerequisite")
    finishes = {}
    while len(finishes) < len(tasks):
        ready = [name for name, (_, deps) in normalized.items()
                 if name not in finishes and all(dep in finishes for dep in deps)]
        if not ready:
            raise ValueError("Dependency cycle")
        for name in ready:
            duration, deps = normalized[name]
            finishes[name] = max((finishes[d] for d in deps), default=Decimal(0)) + duration
    return finishes


def catchup_seconds(backlog_mib, transfer_mib_s, writes_mib_s):
    backlog, transfer, writes = map(number, (backlog_mib, transfer_mib_s, writes_mib_s))
    if transfer <= writes:
        return None  # no converging positive net drain under these assumptions
    return backlog / (transfer - writes)


def burn_rate(bad, total, slo):
    bad, total, slo = map(number, (bad, total, slo))
    if total == 0 or bad > total or not 0 < slo < 1:
        raise ValueError("Missing/invalid event evidence or SLO")
    return (bad / total) / (1 - slo)


def fingerprint(candidate):
    payload = json.dumps(candidate, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


def may_publish(candidate, approval, current_version, trusted_reviewers):
    # Trusted records/identity are assumed. This is not authentication or a signature.
    return (approval.get("reviewer") in trusted_reviewers
            and approval.get("decision") == "approve"
            and approval.get("candidate_sha256") == fingerprint(candidate)
            and candidate.get("base_version") == current_version
            and approval.get("base_version") == current_version)


def run():
    passed = 0

    def check(condition):
        nonlocal passed
        if not condition:
            raise AssertionError("Planning check failed")
        passed += 1

    def rejects(function, *args):
        try:
            function(*args)
        except ValueError:
            check(True)
        else:
            raise AssertionError("Expected rejection was not observed")

    tasks = {"detect": (10, []), "declare": (5, ["detect"]),
             "network": (10, ["declare"]), "identity": (8, ["declare"]),
             "database": (30, ["network", "identity"]),
             "application": (8, ["database"]), "validate": (5, ["application"])}
    result = recovery_schedule(tasks)
    check(result["validate"] == 68)
    check(sum(number(t[0]) for t in tasks.values()) == 76)
    check(result["validate"] > 60)  # invented recovery objective
    quicker = dict(tasks, database=(15, ["network", "identity"]))
    check(recovery_schedule(quicker)["validate"] == 53)
    rejects(recovery_schedule, {})
    rejects(recovery_schedule, {"a": (1, ["missing"])})
    rejects(recovery_schedule, {"a": (1, ["b"]), "b": (1, ["a"])})
    rejects(recovery_schedule, {"a": (-1, [])})
    rejects(recovery_schedule, {"a": ("NaN", [])})
    check(catchup_seconds(900 * 1024, 100, 80) == 46080)
    check(catchup_seconds(900 * 1024, 100, 0) == 9216)
    check(catchup_seconds(900 * 1024, 100, 100) is None)
    check(catchup_seconds(900 * 1024, 100, 120) is None)
    check(catchup_seconds(0, 100, 80) == 0)
    rejects(catchup_seconds, -1, 100, 80)
    rejects(catchup_seconds, 1, True, 0)
    check(burn_rate(200, 10000, ".999") == 20)
    check(burn_rate(1, 10, ".999") == 100)
    check(Decimal(30 * 24 * 60) * (1 - Decimal(".999")) == Decimal("43.2"))
    rejects(burn_rate, 0, 0, ".999")
    rejects(burn_rate, 11, 10, ".999")
    rejects(burn_rate, 0, 10, 1)
    candidate = {"id": "sku-7", "base_version": 4,
                 "attributes": {"color": "blue", "material": "cotton"}}
    approval = {"reviewer": "reviewer-1", "decision": "approve",
                "candidate_sha256": fingerprint(candidate), "base_version": 4}
    trusted = {"reviewer-1"}
    check(may_publish(candidate, approval, 4, trusted))
    check(not may_publish(candidate, approval, 5, trusted))
    changed = dict(candidate, attributes={"color": "red", "material": "cotton"})
    check(not may_publish(changed, approval, 4, trusted))
    check(not may_publish(candidate, dict(approval, decision="reject"), 4, trusted))
    check(not may_publish(candidate, {}, 4, trusted))
    check(not may_publish(candidate, dict(approval, reviewer="outsider"), 4, trusted))
    check(not may_publish(candidate, approval, 4, set()))
    check(not may_publish(candidate, dict(approval, base_version=3), 4, trusted))
    reordered = {"attributes": candidate["attributes"], "base_version": 4, "id": "sku-7"}
    check(fingerprint(reordered) == fingerprint(candidate))
    revised_approval = dict(approval, candidate_sha256=fingerprint(changed))
    check(may_publish(changed, revised_approval, 4, trusted))
    print(f"{passed} offline architecture checks passed; no service deployed or content published")
    return passed


if __name__ == "__main__":
    run()
```

The quicker recovery scenario changes only the database task and yields 53 minutes instead of 68. Explain what real evidence would justify that estimate and what happens when identity or capacity is unavailable. The final approval test requires a new hash binding for changed content; it is not evidence that a human actually reviewed that content.

## Original readiness checks

1. What makes a non-functional requirement usable? 2. Why can a multi-region product still leave a single failure path? 3. Distinguish RTO and RPO. 4. When is Cloud Run a better starting point than GKE? 5. When is replatform preferable to refactor? 6. Why is private connectivity not authorization? 7. What facts drive database choice? 8. What must a migration wave include besides resource creation? 9. Why can a pilot give false confidence? 10. What does Shared VPC separate? 11. Why is Spot unsuitable for some workloads? 12. What additional risk comes with CMEK? 13. What does VPC Service Controls address? 14. Why are service-account keys discouraged? 15. Name four agent tool controls. 16. What must be checked when using Model Garden? 17. What is AI Hypercomputer: product label or architecture concern? 18. What evidence supports compliance? 19. How does an SLO differ from an alert? 20. What is an error budget used for? 21. What does a canary reduce? 22. Why can rollback fail after a schema change? 23. What does an emulator not prove? 24. Why review Terraform plan? 25. What belongs in API governance? 26. What is a service catalog’s operational obligation? 27. Why include decommission in migration? 28. What does FinOps add beyond cost cutting? 29. Why assess skills before target design is final? 30. What is the role of an architecture decision record? 31. What should precede chaos testing? 32. Why is backup success insufficient evidence? 33. How should you use Gemini Cloud Assist? 34. What are the six Well-Architected pillars named by the current guide? 35. Why study each official case as facts rather than a fixed design? 36. What makes an architecture recommendation defensible?

37. Why is regional database HA insufficient for every region-loss requirement?
38. How does a planned switchover differ from a replica failover with lag?
39. Why include identity and business validation in the recovery path?
40. What happens when incoming change rate equals migration throughput?
41. Does a dry-run perimeter enforce its proposed denials?
42. Does KMS rotation make every old key version unnecessary?
43. Which PSC feature allows producer-initiated connections into a consumer network?
44. Does a signed build attestation prove there are no vulnerabilities?
45. Why must Cymbal's approval identify an exact content version?
46. Should EHR's retained insurance interfaces be migrated immediately to satisfy the case?
47. At a 99.9% request SLO, what is the burn rate for one failed request out of ten?
48. Does a fictional automotive executive's safety statement establish verified safety performance?

## Answer key

1. A measure, target, scope/time window and owner. 2. Identity, configuration, deployment, DNS, dependency or corrupt data may remain global failure paths. 3. Recovery time versus acceptable data-loss interval. 4. Stateless request/event container, managed scaling, little Kubernetes need. 5. When a managed platform improvement meets requirements without refactor cost/risk. 6. It changes reachability, not identity/application permission. 7. Model, access/query, consistency, scale, locality, availability/recovery, ecosystem, operations and cost. 8. Dependency, data sync/validation, tests, cutover, rollback, ownership and success/decommission. 9. It may not exercise full scale, dependency, data or organizational behavior. 10. Central network ownership from service-project workload ownership. 11. Interruption may violate state/latency/availability. 12. Key permission, lifecycle and availability become customer failure modes. 13. Data-exfiltration boundaries around supported services. 14. They are long-lived bearer secrets. 15. Narrow identity, allowlists, argument validation, policy/limits, approval, audit, idempotency/reversal. 16. License, provenance, data terms, evaluation, security, region/stage and lifecycle. 17. Both: a Google system offering and a workload-specific accelerator/network/storage/software design decision. 18. A mapped control with owner and current verifiable artifacts. 19. SLO is a target; an alert signals actionable risk/violation. 20. Balancing reliability and change using tolerated unreliability. 21. Exposure/blast radius of a bad release. 22. Old code/data contracts may no longer be compatible. 23. Production IAM, quota, scale, networking and failure behavior. 24. Identify create/change/destroy, drift, policy, cost and dependency impact. 25. Identity, lifecycle/versioning, compatibility, quota/rate, policy, analytics, developer/product ownership and reliability. 26. Version, constraint, SLO, support, security and retirement ownership. 27. To realize savings, remove risk/data and prevent dual-operation indefinitely. 28. Allocation, accountability, forecasting, value and recurring governance. 29. Feasibility, operating model, time, buy/build and risk depend on them. 30. Preserve context, alternatives, choice, tradeoff and revisit trigger. 31. Hypothesis, authorization, blast radius, observability, abort and recovery. 32. Restore may be incomplete, unauthorized, too slow or untested with dependencies. 33. As proposed assistance verified against current docs, state, policy, security, cost and tests. 34. Operational excellence, security, reliability, cost optimization, performance optimization, sustainability. 35. Requirements determine choices and can change. 36. Traceable facts, compared options/tradeoffs, ownership, validation evidence and revisit conditions.

37. Regional HA protects specified zonal failures; regional loss needs a separate data/client/recovery design.
38. Planned switchover can wait for catch-up under the supported configuration; asynchronous outage failover may lose unreplicated writes.
39. A restored database is unusable if operators, keys, network or application dependencies cannot support a valid business request.
40. The modeled backlog never drains; increase effective capacity, reduce writes or plan controlled downtime and validate the result.
41. No. It logs potential violations; an existing enforced configuration continues to enforce separately.
42. No. Resource-specific rewrapping behavior and older data/backups can preserve dependencies on earlier versions.
43. A Private Service Connect interface; inspect its reachable networks and authorization as well as connection direction.
44. No. It proves a signed claim under the trusted process; scan scope, age, policy and later vulnerabilities remain separate evidence.
45. Otherwise a later edit or stale source can bypass the intended human review; binding must be checked at the publication transaction.
46. No. The case explicitly retains those systems for now, so design their hybrid integration and later migration boundary.
47. 100×: `(1/10)/(1-0.999)`. A sparse sample still needs a deliberate alerting policy.
48. No. Treat it as a case statement and require independently assessed validation and applicable approval evidence for a real design.

## Source and freshness notes

- The live page and actual PDFs were read: seven exam pages and 12 case-study pages (Altostrat 3, Cymbal 4, EHR 2, KnightMotives 3). Standard scope is mapped through 101 statements: 96 bullets plus 5 standalone objectives under 22 numbered objectives. The detailed PDF exposes no visible publication date, so verification date is recorded rather than invented.
- The live objective monitor intentionally snapshots the six high-level capability lines; the detailed PDF is separately registered and manually mapped.
- The objective hash is unchanged. A previously absent lifecycle baseline was initialized after explicit standard/renewal review; before/accepted/post receipts distinguish initialization from an exam change. Renewal case-study PDFs were not separately reviewed.
- The [April 22, 2026 Google announcement](https://cloud.google.com/blog/products/ai-machine-learning/the-new-gemini-enterprise-one-platform-for-agent-development) supplies app/platform naming context only. Source passages on retention, identity, Model Registry, Model Armor and GKE reuse documented same-session reading with current healthy fetches.
- Only the exact 32-check local worksheet executed. Eight cloud labs remain proposed; no live IAM, database, migration, perimeter, model, signing pipeline, vehicle or clinical system was tested. The prior ACE check found no `gcloud` on PATH; no credentials or paid content were accessed. Independent human review remains pending.
- Product names, model/API capabilities, release stages, regions, quotas, prices, compliance contracts, case studies, renewal/delivery details and learning catalogs are volatile. Verify first-party sources during study and before scheduling.
- This guide is original synthesis from public sources. It uses no recalled exam item, exam dump, proprietary bank or copied course material.

> **Related items remain contextual:** The official guide defines scope; related explanations connect it to sound architecture and operation.

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. Pick a coherent route, use the blueprint/case studies as the checklist, and select labs/readings for weak decisions. Public metadata was checked September 29, 2026; paid lessons/labs were not accessed. Separate visible content totals from schedule estimates, then add practice, design, troubleshooting and review time.

| Resource | Access | Estimated time | Best use / currency note |
|---|---|---:|---|
| [Official exam guide](https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf) | Public | 1–2h initially, then weekly | Scope and current product-name authority |
| [Four official case studies](https://cloud.google.com/learn/certification/cloud-architect) | Public | 4–8h initial analysis; revisit | Requirement-driven judgment; follow the case links on the page/PDF |
| [Google Skills PCA path](https://www.skills.google/paths/12) | Account; labs may need credits/entitlement | 24 activities; current activity durations not exposed | Public page gives relative update age of four months; earlier 172h15m and 72h badge claims were not reverified. Select by objective gaps |
| [Official sample questions](https://docs.google.com/forms/d/e/1FAIpQLSf54f7FbtSJcXUY6-DUHfBG31jZ3pujgb8-a5io_9biJsNpqg/viewform?usp=sf_link) | Public | 30–60m plus review | Calibrate official question style; not a score predictor |
| [Preparing for Google Cloud Certification: Cloud Architect](https://www.coursera.org/professional-certificates/gcp-cloud-architect) | Paid/subscription; audit terms vary | Seven course cards total 48h; landing 4 weeks at 10h/week; FAQ 1.5 months at 5h/week | Google-authored infrastructure/design/GKE route plus Gemini Notebook study preparation. Conflicting schedule estimates and old/new branding need review; paid teaching was not inspected |
| [Google Cloud Certified Professional Cloud Architect Study Guide, 2nd ed.](https://www.oreilly.com/library/view/google-cloud-certified/9781119821002/) | Paid O’Reilly | Planning allowance 12–18h reading plus exercises; current metadata blocked | Prior record says 2022/352 pages, not reverified. Use current AI/agent/case gaps; no paid book content read |
| [Whizlabs Professional Cloud Architect](https://www.whizlabs.com/google-cloud-certified-professional-cloud-architect/) | Paid; limited free material may vary | Full current catalog not exposed; verify before purchase | Direct fetch returned a title-only shell, so course/lab quantities and current objective alignment were not verified |
| [Well-Architected Framework](https://cloud.google.com/architecture/framework) and [Architecture Center](https://cloud.google.com/architecture) | Public | 12–30h targeted reading | Production tradeoffs and all six cross-cutting pillars |

A current [Pluralsight PCA path](https://www.pluralsight.com/paths/google-certified-professional-cloud-architect-by-pluralsight) is verified: seven Victor Dantas courses total **7h17m**, with one 30-minute regional-MIG lab, **7h47m** altogether versus the rounded eight-hour header. Core course dates span July–December 2025; the lab is August 6, 2026. Compare current AI/agent/case objectives explicitly; public titles and dates do not establish complete paid-lesson coverage. No verified MeasureUp PCA item is added.

### Current-version gap checklist

When a resource predates the current guide, independently close: Gemini Enterprise Agent Platform, Agent Platform Pipelines/data integration, Agent Builder and Model Garden; Gemini Enterprise agents and NotebookLM; Gemini Cloud Assist; AI Hypercomputer and GPU/TPU consumption; Model Armor/Sensitive Data Protection and secure AI; current Cloud Run functions branding; current Well-Architected sustainability pillar; Migration Center; Chrome Enterprise Premium/context-aware access; software supply chain; and all four V6.1 official case studies.
