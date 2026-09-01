---
exam_code: DOP-C02
vendor_id: aws
official_blueprint: https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# DOP-C02 AWS Certified DevOps Engineer - Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#dop-c02-coverage-record). The [official DOP-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02.html) is authoritative.

**Current baseline:** Current six-domain DOP-C02 AWS Certified DevOps Engineer - Professional guide; 65 scored plus 10 unscored questions<br>
**Upcoming blueprint change:** None announced on the official exam guide or certification page as of September 1, 2026.<br>
**Important freshness boundary:** DOP-C02 remains current, but AWS delivery, observability, governance, container, and security services evolve inside an unchanged exam code. Validate features, regions, quotas, integrations, pricing, and learning metadata. Do not confuse older DOP-C01 domains or legacy service workflows with the current contract.<br>
**Official source:** [AWS Certified DevOps Engineer - Professional exam guide](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02.html)

## How to use this guide

DOP-C02 is an automation and systems-ownership exam. The best design does more than deploy: it creates a controlled path from reviewed source to immutable evidence, manages infrastructure and configuration across accounts, responds safely to failure, and proves security and compliance continuously. AWS targets candidates with two or more years provisioning, operating, and managing AWS environments plus SDLC and programming or scripting experience.

The certification page lists a 180-minute, 75-question, USD 300 exam delivered online or at Pearson VUE. The detailed guide identifies 65 scored and 10 unidentified unscored multiple-choice or multiple-response items and a 750 minimum scaled score. Recheck the [live certification page](https://aws.amazon.com/certification/certified-devops-engineer-professional/) before scheduling; delivery, language, price, and policy are **VERIFY CURRENT**.

Use one operating loop across all domains:

1. Define desired state, deployment unit, owners, environments, account/Region boundaries, service objectives, and risk.
2. Make source, dependencies, artifacts, configuration, infrastructure, policies, and runbooks versioned and reproducible.
3. Build the smallest safe pipeline with early tests, least-privilege identities, traceable approvals, immutable promotion, and explicit rollback.
4. Observe customer outcomes, workload health, deployments, security signals, configuration, and audit activity centrally.
5. Detect, contain, diagnose, remediate, verify, communicate, and learn from events; automate only bounded decisions.
6. Feed evidence back into templates, tests, guardrails, capacity, recovery, and delivery policy.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| SDLC Automation | 22% | How does reviewed source become a tested, trusted artifact and a safe deployment? |
| Configuration Management and IaC | 17% | How is desired state defined, reused, governed, deployed, reconciled, and retired at scale? |
| Resilient Cloud Solutions | 15% | How do capacity, failure, backup, and recovery become tested automated behavior? |
| Monitoring and Logging | 15% | Which telemetry proves customer/system state and enables diagnosis across accounts? |
| Incident and Event Response | 14% | How are events routed into bounded, auditable action and verified recovery? |
| Security and Compliance | 17% | How are identity, data, findings, policy, and compliance enforced continuously in delivery and operations? |

SDLC automation is the largest domain, but professional scenarios join several domains. A release pipeline without observability, recovery, and security is incomplete.

---

## 1. SDLC Automation — 22%

The official [Domain 1 page](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain1.html) covers CI/CD pipelines, automated testing, artifact management, and deployment strategies across instances, containers, and serverless environments.

### Design a promotion system, not a sequence of buttons

A trustworthy pipeline records source revision, dependency lock, build environment, commands, tests, scan results, artifact digest, configuration/infrastructure version, approvals, identity, target, deployment result, and rollback evidence. Build an artifact once and promote the same immutable bytes or image digest through environments. Rebuilding “the same” source for production can change dependencies or tooling and destroys provenance.

CodePipeline can orchestrate stages and actions; CodeBuild supplies managed builds/tests; CodeDeploy manages supported instance, ECS, and Lambda deployment patterns; CodeArtifact stores supported packages; ECR stores container images; S3 can hold pipeline artifacts. Third-party repositories and delivery tools can participate. Choose from organizational integration, runner isolation, cross-account role model, artifact provenance, target platform, deployment control, and supportability—not from an assumption that every pipeline must use every Code service.

For multi-account delivery, keep the pipeline/tooling account separate where appropriate, store artifacts under controlled policy/encryption, assume narrowly scoped deployment roles in targets, and let target-side resource policies/key policies trust only required principals. Avoid copying permanent credentials to runners. Record source and destination accounts/Regions and test cross-account KMS/S3/ECR access before production.

Protect secrets with Secrets Manager or Parameter Store as appropriate. Expose them only to the action that needs them, prevent log/command/history leakage, rotate, audit retrieval, and revoke compromised material. A pipeline secret variable is still a secret with an access and output path.

### Put the right test at the earliest reliable gate

- **Static/unit tests:** fast feedback on code, templates, policy, formatting, dependency, and local behavior.
- **Integration/contract tests:** prove service, schema, permissions, API, message, and dependency interactions.
- **Security tests:** scan dependencies, source, images, IaC, permissions, and reachable workloads; define blocking policy and exception evidence.
- **Performance/load tests:** validate latency, throughput, scale, throttling, and downstream capacity in a representative environment.
- **Acceptance/synthetic tests:** prove user/business behavior through the deployed path.
- **Resilience tests:** inject bounded failure and prove alarm, containment, recovery, and rollback.

Use exit codes plus machine-readable results, but do not treat process success as customer success. Define promotion gates, thresholds, waivers, owners, and expiry. Run destructive or high-load tests only in isolated authorized environments.

**Related item:** Continuous delivery keeps each change deployable; continuous deployment automatically releases qualifying changes. Both require reliable gates, but their approval and risk policies differ.

### Secure and govern artifacts

An artifact is a deployment input: package, archive, image, AMI, Lambda bundle, template, chart, or manifest. Create it in a controlled build, pin dependencies/base images, scan, sign or attest where required, encrypt, prevent overwrite, record digest/provenance, promote immutably, and expire safely. Restrict repository push/delete rights more tightly than pull rights.

EC2 Image Builder can create/test/distribute AMIs and container images through pipelines. ECR supports image scanning and lifecycle controls. CodeArtifact domains/repositories manage supported package formats and upstream connections. Confirm whether a finding blocks build, promotion, or deployment; define risk acceptance and emergency repair.

### Select deployment strategy by failure economics

| Strategy | Benefit | Main risk/control |
|---|---|---|
| In-place / rolling | Lower duplicate capacity | Mixed versions, reduced capacity, slower rollback; control batch and health |
| Immutable | Replaces hosts/tasks from a new artifact | Extra capacity and longer provisioning; validate image and state externalization |
| Blue/green | Isolated new environment and fast traffic switch | Duplicate cost plus data/schema compatibility; own routing and rollback |
| Canary / linear | Limits initial exposure and gathers evidence | Requires representative traffic, alarms, bake time, gates, and automatic stop |
| All-at-once | Fast and cheap for tolerant workloads | Largest blast radius and interruption risk |

EC2/Auto Scaling, ECS, EKS, Lambda, and Elastic Beanstalk have different deployment primitives. Define pre/post hooks, health/acceptance signals, maximum unavailable, traffic increments, bake time, alarm set, timeout, database compatibility, and rollback trigger. Lambda aliases and CodeDeploy can shift versions; ECS blue/green uses task sets/traffic routing; Kubernetes adds rollout/controller/readiness behavior that must be observed separately.

Database and event-schema changes should be backward/forward compatible across the overlap window. Use expand/migrate/contract where appropriate: add compatible structures, deploy code that supports both states, migrate/verify, then remove old structures later. A compute rollback cannot undo a destructive schema change.

---

## 2. Configuration Management and IaC — 17%

The official [Domain 2 page](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain2.html) covers reusable lifecycle-managed infrastructure, automated account onboarding/governance, and complex large-scale automation.

### Treat desired state as a product

CloudFormation templates define AWS resources and stacks. Know parameters, mappings/conditions, references, outputs/exports, dynamic references, change sets, stack policy, termination protection, rollback, creation/update/deletion policies, custom resources, nested stacks, modules, hooks, drift detection, and StackSets. The [CloudFormation guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) is the current behavior source.

The CDK defines constructs in supported languages and synthesizes CloudFormation; it does not bypass CloudFormation lifecycle or permissions. SAM specializes serverless definitions and workflows. Terraform can manage AWS but brings its own state, locking, provider/module, import, drift, plan/apply, and recovery responsibilities. Do not let two systems unknowingly own the same property.

Reusable components need a published contract: inputs, outputs, defaults, supported versions, security/compliance controls, dependencies, ownership, compatibility, examples, tests, upgrade path, and deprecation. Pin versions and promote changes; a mutable central module can surprise every consumer.

Use change sets or equivalent plans to inspect create/update/replace/delete behavior. Test in representative nonproduction accounts, deploy in waves, set failure tolerance/concurrency, observe, and stop on evidence. Preserve service error and stack-event context when rollback fails.

**Related item:** Git proves intended source history; a pipeline proves promotion; CloudFormation records stack operations; CloudTrail records API activity; Config records resource configuration/compliance. None alone is a full audit trail.

### Separate infrastructure, configuration, and secrets

Infrastructure defines durable cloud resources and relationships. Configuration defines environment/workload behavior. Secrets are sensitive runtime inputs. The boundaries overlap, but storing all three in a template or image usually creates unnecessary coupling and exposure.

Systems Manager supports parameter/configuration, inventory, Patch Manager, State Manager, Run Command, Automation, Session Manager, OpsCenter, and related operational capabilities according to current features. Use tags/resource groups, maintenance windows, rate/error controls, approvals, association compliance, and least-privilege roles. Run Command is powerful remote execution; restrict targets, documents, parameters, outputs, concurrency, and audit access.

Use launch templates, AMIs/images, user data, bootstrap, configuration agents, containers, and SSM according to immutability and runtime needs. Prefer immutable replacement for foundational change where possible; use controlled configuration management for settings that legitimately change in place. Detect/reconcile drift or deliberately import/update the desired state—do not silently accept unmanaged mutations.

### Automate multi-account foundations

AWS Organizations provides account hierarchy and policy governance; Control Tower establishes/governs a landing zone; Organizations APIs/account factory workflows, CloudFormation StackSets, RAM, IAM Identity Center, Config aggregators, CloudTrail organization trails, Security Hub/GuardDuty delegated administration, and centralized logging can support account onboarding.

An onboarding workflow should establish identity/federation, break-glass, organization placement, SCPs, budgets/tags, networks/DNS, logging, configuration/security services, baseline roles, key/secrets rules, backup, quotas, and ownership. Make it idempotent and resumable. Detect partial success: an account created without logs/security guardrails is not “onboarded.”

Separate preventive controls (block), detective controls (find), and responsive/corrective controls (act). Test policy impact in safe organizational units before broad rollout. SCP explicit deny can break automation even when a role policy allows it; delegated administrators and service-linked roles need lifecycle planning.

### Engineer large-scale automation safely

For Automation runbooks, Lambda, Step Functions, EventBridge, scripts, and custom resources, define input validation, idempotency, state/checkpoint, retries/backoff/jitter, timeout, rate/concurrency, quota, partial failure, rollback/compensation, output, audit, and escalation. Test 1, then a small wave, then broader scope. A loop across all accounts/Regions without rate and stop controls is a blast-radius mechanism.

---

## 3. Resilient Cloud Solutions — 15%

The official [Domain 3 page](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain3.html) covers highly available/scalable systems, automated recovery, and backups/restores.

### Turn resilience into automated policy

Define availability target, traffic shape, dependency graph, failure modes, RTO/RPO, capacity margin, and data correctness. Multi-AZ placement is useful only when routing, capacity, state, dependencies, and deployment all survive a zone loss. Multi-Region adds data-consistency, routing, identity/key, quota, artifact, observability, and operating complexity.

Auto Scaling policies should use workload-correlated metrics and include min/max/desired, warmup, cooldown, lifecycle hooks, health checks, quotas, subnet space, placement, mixed instances/Spot behavior, and downstream limits. Use queues to absorb bursts and isolate producers/consumers; scale on backlog age/depth where appropriate. Make consumers idempotent and own DLQ redrive.

Use ELB and Route 53 health/routing, CloudFront or Global Accelerator where their edge/path behavior fits, and database/storage availability patterns appropriate to state. Failure drills must include partial dependency degradation, not merely stopped instances.

### Automate recovery without hiding failure

EventBridge, CloudWatch alarms, Auto Scaling, Systems Manager Automation, Lambda, Step Functions, health checks, and service-native recovery can detect and remediate. A safe closed loop:

1. detects a specific condition with enough context;
2. checks preconditions and scope;
3. runs a bounded, idempotent action under least privilege;
4. captures evidence;
5. verifies customer/system recovery;
6. stops/escalates on non-recovery or repeated action.

Avoid “restart until green” automation that destroys evidence or amplifies faults. Define circuit breakers and human approval for high-impact actions.

### Prove backup and disaster recovery

AWS Backup can centralize supported-resource policies, vaults, copies, lifecycle, monitoring, and restore testing. Service-native snapshots/PITR, S3 versioning/replication/Object Lock, AMIs/images, and data replication have different semantics. Protect backups from the same account, credentials, Region, key loss, and deletion authority when requirements demand.

Map backup-and-restore, pilot-light, warm-standby, and active/active strategies to business RTO/RPO and cost. Keep IaC, artifacts, roles, keys, secrets, certificates, DNS, dependencies, quotas, and runbooks recoverable. Restore into isolation, validate data and application behavior, measure achieved objectives, and feed failures into automation.

**Related item:** Self-healing restores intended service for known failure modes. It does not eliminate incident review or prove that restored behavior and data are correct.

---

## 4. Monitoring and Logging — 15%

The official [Domain 4 page](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain4.html) covers collection/aggregation, metric/log auditing, automated monitoring/event management, and analysis/troubleshooting.

### Build telemetry around questions

| Signal | Question | Typical source |
|---|---|---|
| Business/SLO metric | Are users receiving the promised outcome? | Custom metrics, synthetic/canary results, application events |
| Resource/service metric | Is a component saturated, throttled, failing, or scaling? | CloudWatch/service/container metrics |
| Log | What detailed event/error occurred? | CloudWatch Logs, application/service/access/flow logs |
| Trace | Where did a distributed request spend time or fail? | X-Ray/OpenTelemetry-compatible telemetry |
| Deployment event | What changed and with which artifact/result? | Pipeline/deployment system and EventBridge |
| Audit/configuration | Who changed what; what state existed? | CloudTrail, Config, IaC history |
| Security finding | What risk or suspicious behavior was detected? | GuardDuty, Inspector, Security Hub, Macie and sources |

[CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) covers metrics, alarms, dashboards, logs and related observability. Instrument at request/queue/dependency boundaries, use correlation IDs, structure logs, control cardinality and sensitive fields, synchronize time, define retention, and test telemetry loss. Missing telemetry is not proof of health.

Centralize cross-account/Region logs under protected write paths and restricted read/delete access. Organization trails and Config aggregation support governance, while application/service logs require deliberate delivery. Validate destination policy, KMS permissions, partitions/prefixes, retry/failure, integrity/retention, query access, and cost. Separate production evidence from a compromised workload/account where required.

### Make alarms and dashboards actionable

Choose metric/statistic/percentile, dimensions, period, evaluation window, datapoints-to-alarm, threshold/anomaly model, missing-data behavior, and action. Composite alarms reduce noise or express dependencies. Alarm on customer symptoms and leading resource signals; include owner, severity, runbook, context, and response target.

Dashboards should connect SLO/outcome, traffic, errors, latency, saturation, dependency, deployment, capacity, security, and cost. High average health can hide tail latency or one tenant/zone. Use percentile/distribution and dimension breakdowns responsibly.

CloudWatch Logs Insights and metric filters can query/derive signals; Contributor Insights identifies high-cardinality contributors; X-Ray/service maps/traces isolate distributed latency; VPC Flow Logs and load-balancer/WAF logs answer network/request questions. Select the minimum evidence that distinguishes hypotheses.

### Automate event routing without losing events

EventBridge routes matching events to targets; SNS fans notifications to subscribers; SQS buffers work; alarms act on metric state. Design permissions, input transformation, retries, DLQs, archives/replay where supported, ordering/duplicates, idempotency, and observability. A matched event is not proof that the target completed.

**Related item:** Monitoring reports known conditions; observability lets operators infer internal state from outputs, including failures not predicted as named alarms.

---

## 5. Incident and Event Response — 14%

The official [Domain 5 page](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain5.html) covers event sources, processing, automated response, and troubleshooting.

### Establish an evidence-preserving response flow

1. Detect and validate the signal; reject duplicates/noise without discarding useful evidence.
2. Declare severity, owner/commander, scope, customer impact, communication cadence, and timeline.
3. Contain the blast radius with reversible least-privilege action.
4. Diagnose from telemetry, deployment/config/audit history, topology, health, and hypotheses.
5. Remediate, rollback, fail over, restore, or mitigate; record commands and approvals.
6. Verify customer outcome, data correctness, backlog recovery, security posture, and monitoring.
7. Preserve evidence and write blameless learning actions with owners and due dates.

Systems Manager OpsCenter/Incident Manager capabilities, Automation, Lambda, Step Functions, EventBridge, SNS, SQS, Chatbot/chat integrations, and ticketing tools can coordinate response according to current features. Automate enrichment first—resource/account/Region, owner, recent change, metrics/logs, dependencies, and runbook—before automating destructive remediation.

### Troubleshoot by causal layer

- **Pipeline:** trigger/filter, source revision, action role, artifact/key access, environment variable/secret, network path, quota, action timeout, output, and downstream stage.
- **Deployment:** platform agent/controller, target registration/health, hook, package/image, runtime configuration, IAM, capacity, subnet/IP, dependency, database/schema, and alarm rollback.
- **IaC:** template/plan, change replacement, permission, quota/Region, dependency, name collision, custom resource, stack event, rollback, and drift.
- **Application:** SLO, request/trace/log, dependency, throttling, queue/backlog, connection, data/schema, cache, and resource saturation.
- **Network:** DNS, address/port, route/return route, SG/NACL/firewall/endpoint, load balancer/target, hybrid state, and application listener.
- **Security/compliance:** principal/session, complete policy evaluation, key/resource policy, finding source, configuration history, CloudTrail, scope, and containment.

Change one variable at a time when possible. Preserve failing events/logs before retry/delete. Broadening permissions or opening networks can hide the root cause and create an incident.

### Design runbooks and game days

A runbook states trigger, scope, prerequisites, roles, evidence, commands/automation, decision points, stop conditions, verification, rollback, escalation, communication, and cleanup. Test it with realistic permissions and dependencies. Version and review runbooks alongside the systems they operate.

Game days safely inject faults to validate detection, response, recovery, and learning. Define hypothesis, blast radius, abort condition, observers, metrics, communication, rollback, and evidence. Vary deployment, dependency, zone, permission, capacity, telemetry, and backup failure—not only instance termination.

**Related item:** Mean time to recovery can improve while recurrence remains high. Track detection, acknowledgment, containment, restoration, change failure, and repeat-incident evidence separately.

---

## 6. Security and Compliance — 17%

The official [Domain 6 page](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02-domain6.html) covers identity/access at scale, security-control automation, data protection, and automated compliance validation.

### Make pipeline identity short-lived and scoped

Use roles and temporary credentials for builds/deployments. Separate human, pipeline, service, and emergency identities. A build role needs only its build inputs/outputs and test actions; a deploy role needs only target changes. Cross-account trust should restrict principal, source context/conditions, session, and artifact/key access. Use permissions boundaries/SCPs to constrain delegated automation without assuming they grant access.

Review the [IAM evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html), Access Analyzer findings, last-accessed/activity evidence, CloudTrail, and policy simulation. Prevent privilege escalation through role passing, policy changes, CloudFormation service roles, build scripts, custom resources, or writable artifacts/templates.

Protect source branches, reviews, pipeline definition, build image/runner, dependencies, artifacts, provenance, deployment roles, and target configuration. A signed artifact is insufficient if an attacker can replace the pipeline definition or signing identity.

### Automate layered controls

Preventive: SCPs, permissions boundaries, resource policies, network controls, encryption requirements, protected branches, pipeline gates, CloudFormation hooks, and service control features. Detective: Config rules/conformance packs, CloudTrail, GuardDuty, Inspector, Macie, Security Hub controls, IAM Access Analyzer, logs, and scanning. Responsive: EventBridge-driven triage, Systems Manager/Lambda/Step Functions remediation, isolation, ticketing, notification, and evidence preservation.

Centralize delegated security administration carefully. Aggregate findings with account/Region/resource/control context, deduplicate, enrich ownership, prioritize exploitability/impact, suppress only with reason/expiry, remediate, and verify at the source. Security Hub aggregation is not itself remediation; Config compliance is not proof of runtime security.

### Protect data and evidence

Encrypt artifacts, logs, backups, parameters/secrets, queues/topics, data stores, and cross-account transfers according to classification. Design KMS key policy, grants, aliases, rotation/deletion, separation of key and data administrators, multi-Region or cross-account access, and recovery. Encrypt in transit with managed certificates where suitable; validate endpoint and renewal behavior.

Do not log secrets, tokens, personal data, or sensitive payloads without an explicit protected need. Apply retention and deletion policy, Object Lock/immutability where required, separate evidence access, and test retrieval during investigation/recovery.

### Make compliance continuous and auditable

Translate requirements into preventive/detective controls, evidence sources, frequency, owner, exception process, remediation target, and retention. Config evaluates supported resource configuration; Audit Manager helps collect organized evidence; CloudTrail records activity; Artifact provides AWS compliance reports; Security Hub evaluates controls/findings. No one service proves full compliance.

Use policy-as-code/template scanning before deployment, hooks/guardrails during provisioning, Config/security detection after deployment, and automated remediation within safe bounds. Exceptions need business owner, scope, compensating control, approval, expiration, and periodic review.

**Related item:** Compliance automation should produce explainable evidence. A green dashboard without control definition, scope, timestamps, exceptions, and source records is not an audit trail.

---

## Integrated scenarios

### Scenario 1: Multi-account container release platform

A platform team must deploy one container service to dev, test, and production accounts. Build once in an isolated account, record source/dependency/build/scan provenance, publish an immutable ECR digest, and promote it through cross-account roles. Validate IaC and policy, run unit/integration/security/performance tests, then canary the new task set behind measured alarms. Keep database change backward-compatible. Stop and roll back automatically on customer-error/latency signals, not pipeline status alone. Centralize deployment, audit, application, and security evidence and rehearse compromised-artifact revocation.

### Scenario 2: Organization-wide configuration drift

A security baseline is missing in newly created accounts and operators have made manual changes. Compare account factory/Control Tower workflow, StackSet deployments, SCP/Config coverage, CloudTrail history, and delegated administrators. Quarantine the failure to onboarding state, fix idempotency and partial-success detection, deploy in waves with failure tolerance, reconcile drift through desired state, and preserve approved exceptions. Verify every account/Region and add a conformance plus response loop that cannot recursively break access.

### Scenario 3: Deployment causes regional order backlog

A canary passes health checks but queue age and order latency rise. Freeze promotion, correlate artifact/config/schema revision with traces, consumer logs, queue metrics, throttling, database connections, and downstream quotas. Roll back or reduce traffic if the old version is data-compatible; otherwise use a targeted mitigation. Preserve messages and idempotency. Verify customer latency, backlog drain, data correctness, and security—not just task health. Add a queue-age gate, representative load/contract test, and game-day scenario.

---

## Practice labs

Use an AWS Builder Lab, organization-approved sandbox, or disposable personal training accounts. Set budgets, avoid production data, use least privilege, record resources, and remove billable resources. Current prices and free-tier coverage are **VERIFY CURRENT**.

### Lab 1: Build-once promotion pipeline — 150–240 minutes

Create a small application pipeline from source to immutable artifact. Record digest/provenance, run unit/integration/security checks, promote the same artifact to two disposable environments through separate roles, and prove that production does not rebuild source.

### Lab 2: Canary with evidence-driven rollback — 150–240 minutes

Deploy a Lambda alias, ECS task set, or guided equivalent with traffic steps, bake time, customer-facing metric, alarm, and rollback. Inject a reversible defect that passes basic liveness but fails an acceptance/SLO test. Capture events and cleanup.

### Lab 3: Reusable IaC and drift lifecycle — 150–240 minutes

Build a versioned reusable CloudFormation/CDK/SAM component with inputs, outputs, policies, tests, change-set review, deletion/replacement controls, and documentation. Create controlled drift, detect it, reconcile through source, and test a failed rollback safely.

### Lab 4: Multi-account onboarding design — 120–180 minutes

Using sandbox accounts or a document-based simulation, map organization placement, identity, SCPs, logging, Config/security aggregation, network/DNS, budget, backup, keys, ownership, and partial-failure states. Implement/test one StackSet or equivalent wave with concurrency/error controls.

### Lab 5: Central observability and SLO — 120–210 minutes

Instrument a request/queue flow with structured logs, metrics, traces/correlation, deployment events, and audit/config evidence. Create an SLO dashboard and actionable alarms. Break telemetry and prove that missing data is detected separately from workload health.

### Lab 6: Bounded auto-remediation — 120–180 minutes

Route a specific EventBridge/alarm condition to Systems Manager Automation, Lambda, or Step Functions. Add validation, idempotency, concurrency/error limit, audit, verification, manual stop, and escalation. Test repeated/failed delivery without repeated harmful action.

### Lab 7: Backup and regional recovery game day — 180–300 minutes

Protect a small stateful workload and its IaC/artifacts/keys/secrets. Restore into isolation or a second Region/account where authorized, measure RPO/RTO, validate application/data, and document DNS/identity/quota dependencies and failed assumptions.

### Lab 8: Continuous compliance pipeline — 150–240 minutes

Create one policy-as-code pre-deploy check, one preventive provisioning control, one Config/security detection, and one bounded remediation/exception path. Generate evidence showing control, scope, time, result, owner, exception expiry, and verified remediation.

---

## Knowledge checks

1. Build once means? **Promote the same immutable artifact/digest rather than rebuilding source per environment.**
2. Why record provenance? **To trace artifact to source, dependencies, build, tests, identity, and approval.**
3. CodePipeline versus CodeBuild? **Pipeline orchestrates stages/actions; CodeBuild runs managed builds/tests.**
4. First cross-account requirement? **Narrow role trust/permissions plus artifact and KMS/resource-policy access.**
5. Continuous delivery versus deployment? **Deployable changes versus automatic release of qualifying changes.**
6. Unit test versus integration test? **Isolated behavior versus interaction between real components/contracts.**
7. Process exit zero proves customer health? **No; use acceptance/SLO signals through the deployed path.**
8. Artifact repository write permission risk? **It can replace trusted deployment inputs; restrict and audit push/delete.**
9. Rolling versus blue/green? **Rolling changes batches in place; blue/green uses separate environments and traffic switch.**
10. Canary needs what beyond traffic split? **Representative signal, step/bake policy, alarm, stop and rollback.**
11. Why expand/migrate/contract schema? **To preserve compatibility across mixed versions and safe rollback.**
12. CDK ultimately deploys through? **Synthesized CloudFormation templates/assets and CloudFormation lifecycle.**
13. Change set purpose? **Preview create/update/replace/delete effects before execution.**
14. Drift detection repairs drift? **No; it reports supported differences for deliberate reconciliation.**
15. Risk of mutable modules? **Consumers can change without an explicit versioned upgrade.**
16. IaC and runtime configuration identical? **No; separate durable resources, changing configuration, and secrets deliberately.**
17. StackSets role? **Deploy stack instances across selected accounts/Regions with rollout controls.**
18. SCP grant permissions? **No; it constrains maximum permissions.**
19. Account onboarding completion proof? **Every baseline control is verified; account creation alone is partial success.**
20. Safe bulk automation controls? **Idempotency, validation, waves, concurrency/error limits, stop, audit, and verification.**
21. Multi-AZ means resilient automatically? **No; every critical layer, route, capacity, state, and dependency must survive.**
22. Queue scaling signal often better than CPU? **Backlog age/depth reflects waiting work and customer delay.**
23. What completes self-healing? **Post-action verification and escalation if recovery did not occur.**
24. Backup success equals recovery proof? **No; restore complete application/data/keys/dependencies within RTO/RPO.**
25. Pilot light versus warm standby? **Critical core versus reduced functional copy already running.**
26. Metric versus log versus trace? **Numeric trend, detailed event, and distributed request path.**
27. CloudTrail versus Config? **API/account activity versus resource configuration/compliance history.**
28. Composite alarm purpose? **Combine alarm states/reduce noise, not improve weak input signals.**
29. Missing telemetry means healthy? **No; collection/permission/network/region/config can fail.**
30. Event matched means remediation succeeded? **No; observe target delivery, action, and verification.**
31. First incident step after alert? **Validate signal, impact, scope, severity, owner, and recent change.**
32. Why preserve failing stack/deployment events? **Retries/deletion can erase causal evidence.**
33. Opening all network access valid troubleshooting? **No; it creates exposure and hides the failing layer.**
34. Good runbook stop condition? **A defined risk, non-recovery, repeated action, or evidence threshold requiring escalation.**
35. Game day prerequisite? **Hypothesis, bounded blast radius, abort/rollback, observers, metrics, and authorization.**
36. Pipeline role should be administrator? **No; separate narrowly scoped build and deployment actions.**
37. Signed artifact alone secures supply chain? **No; protect source, pipeline, builder, dependencies, signing identity, and target.**
38. Preventive versus detective control? **Blocks disallowed action versus finds noncompliance or risk.**
39. Security Hub fixes source findings? **Not by itself; aggregate/prioritize, remediate, and verify at source.**
40. KMS key policy operational risk? **It can deny builds, logs, artifacts, backups, or recovery despite other IAM allows.**
41. Config proves full compliance? **No; it evaluates supported configuration against defined rules, one evidence source.**
42. What makes compliance evidence useful? **Defined control/scope, timestamped source result, owner, exception, remediation, and retention.**

---

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. Choose one current primary route, then spend more time building and failing enterprise-style delivery/operations systems than watching overlapping videos. Use legitimate practice to locate gaps; reject recalled-question or “actual item” claims.

| Resource | Access | Estimated time |
|---|---|---:|
| Official guide and AWS four-step plan | Public/free-account/subscription mix | 25–40 hours selected study |
| Hands-on delivery, operations, and game days | Sandbox/authorized accounts | 40–70 hours |
| Pluralsight DOP-C02 path | Paid | 35 hours plus labs/practice |
| Udemy/Stéphane Maarek current course | Paid | 17 hours 3 minutes plus extensive labs |
| Tutorials Dojo video/practice route | Paid | 30–45 hours estimated |
| Whizlabs course/lab/practice route | Paid | 25–50 hours estimated |

- **Official route:** [AWS certification page and four-step plan](https://aws.amazon.com/certification/certified-devops-engineer-professional/) plus [DOP-C02 Skill Builder exam prep](https://skillbuilder.aws/category/exam-prep/devops-engineer-professional-DOP-C02) (**about 25–40 hours selected**, plus labs/game days). Use official questions, domain refresh, Builder Labs/Jam/SimuLearn choices, and official practice exam according to entitlement.
- **Structured domain route:** [Pluralsight DOP-C02 path](https://www.pluralsight.com/paths/aws-certified-devops-engineer-professional) (**35 listed hours**, eight courses and practice exam; modules range from 2024 to August 2026, so check legacy named services/workflows).
- **Current compact course:** [Udemy/Stéphane Maarek DOP-C02](https://www.udemy.com/course/aws-certified-devops-engineer-professional-hands-on/) (**17 hours 3 minutes**, plus hands-on repetition; shown updated August 2026). Its compact runtime assumes associate-level foundation and real AWS experience.
- **Course/practice route:** [Tutorials Dojo DOP-C02 video course](https://portal.tutorialsdojo.com/courses/aws-certified-devops-engineer-professional-dop-c02-video-course/) (**21.2+ video hours, 10+ listed labs, 13 quizzes, and one practice test**) plus [practice exams](https://portal.tutorialsdojo.com/courses/aws-certified-devops-engineer-professional-practice-exams/) (**about 10–18 hours** across randomized, timed, review, and six domain sets). Note that its video page still labels the included full test as 65 questions even though the live exam has 75 total; verify practice format.
- **Lab/practice alternative:** [Whizlabs DOP-C02](https://www.whizlabs.com/aws-devops-certification-training/) (**about 25–50 hours selected estimated**); the current product resolves, but stable public counts/runtime were not exposed in the review response. Inspect live coverage, labs, sandbox, and practice sets before purchase.
- **O'Reilly boundary:** no exact current DOP-C02-specific O'Reilly book/video with stable public metadata was independently verified on September 1, 2026. Use its AWS/DevOps library only after mapping chapters to the six official domains.
- **Practice boundary:** no exact current MeasureUp DOP-C02 product was independently verified. Start with official AWS assessment, then choose a legitimate explanation-rich bank rather than large untraceable question collections.

Suggested preparation: someone already owning mature AWS delivery and operations may need **80–120 hours**; a candidate bridging from associate-level knowledge may need **140–220 hours**, including prerequisites and game days.

---

## Source map and freshness notes

The official root and six domain pages define scope; the certification page defines live delivery; the [in-scope services page](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/dop-02-in-scope-services.html) is a non-exhaustive gap aid. Product documentation supports behavior, while learning vendors support only their catalog claims.

- **VERIFY CURRENT:** Code service/source availability, container/serverless delivery features, Systems Manager/Control Tower capabilities, observability/security integrations, regions, quotas, price, and training metadata.
- **VERIFY CURRENT:** deployment rollback, CloudFormation/CDK/SAM behavior, organization policy/control coverage, backup support, delegated administration, and incident tooling before production use.
- **Stable operating pattern:** desired state → versioned inputs → gated immutable promotion → observability → bounded response → verified recovery → feedback into controls.

This guide uses no recalled exam questions or restricted content. The knowledge checks are original and test published concepts rather than reproducing vendor items.
