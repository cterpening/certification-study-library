---
exam_code: SAP-C02
vendor_id: aws
official_blueprint: https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/solutions-architect-professional-02.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# SAP-C02 AWS Certified Solutions Architect - Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#sap-c02-coverage-record). The [official SAP-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/solutions-architect-professional-02.html) is authoritative.

**Current baseline:** Current four-domain SAP-C02 guide; 65 scored plus 10 unscored questions, with a separate unscored emerging-topic section<br>
**Upcoming blueprint change:** None announced on the official exam guide or certification page as of September 1, 2026.<br>
**Important freshness boundary:** AWS currently lists responsible and agentic-AI controls—Bedrock Guardrails, AgentCore Identity, and human-approval workflows—as possible **unscored pretest** topics, not as a fifth scored domain. The large non-exhaustive service list, product names, interfaces, quotas, pricing, Regions, service availability, and training catalogs are **VERIFY CURRENT**.<br>
**Official source:** [AWS Certified Solutions Architect - Professional exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/solutions-architect-professional-02.html)

## How to use this guide

SAP-C02 is not simply SAA-C03 with more services. It tests whether you can turn ambiguous enterprise requirements into an operable decision across accounts, applications, networks, identities, Regions, migrations, teams, and years of change. AWS targets candidates with two or more years designing and implementing AWS solutions who can advise across multiple applications and projects in a complex organization. Frontend mobile development, 12-factor methodology, and deep operating-system administration are listed outside the target role.

The live [certification page](https://aws.amazon.com/certification/certified-solutions-architect-professional/) lists 180 minutes, 75 multiple-choice or multiple-response questions, USD 300, and several languages. The detailed guide identifies 65 scored and 10 unidentified unscored questions, compensatory scoring, and a 750 minimum scaled score. Recheck delivery and pricing before scheduling.

Use one disciplined decision loop for every scenario:

1. Extract business outcomes, stakeholders, constraints, dependencies, regulatory boundaries, RTO/RPO, SLOs, growth, skills, budget, and deadlines.
2. Map trust, network, data, failure, deployment, ownership, and cost-allocation boundaries before selecting products.
3. Generate at least two viable architectures, including migration/operating model and not only target-state boxes.
4. Compare security, reliability, performance, cost, operational burden, reversibility, blast radius, and time to value.
5. State assumptions and select the option that satisfies all hard requirements with the simplest justified operating model.
6. Define measurable validation, rollout, rollback, recovery, observability, ownership, and improvement loops.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Domain | Weight | Central question |
|---|---:|---|
| 1. Design Solutions for Organizational Complexity | 26% | How should shared connectivity, security, resilience, accounts, governance, and cost visibility work across the organization? |
| 2. Design for New Solutions | 29% | Which complete architecture meets deployment, continuity, security, reliability, performance, and cost requirements? |
| 3. Continuous Improvement for Existing Solutions | 25% | What evidence identifies the highest-value operational, security, performance, reliability, and cost changes? |
| 4. Accelerate Workload Migration and Modernization | 20% | Which portfolio, wave, transfer, platform, data, and modernization decisions deliver safe business value? |

The domain pages provide the task detail: [Domain 1](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/solutions-architect-professional-02-domain1.html), [Domain 2](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/solutions-architect-professional-02-domain2.html), [Domain 3](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/solutions-architect-professional-02-domain3.html), and [Domain 4](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/solutions-architect-professional-02-domain4.html). Use the [non-exhaustive in-scope service list](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/sap-02-in-scope-services.html) for gap analysis, not as a memorization checklist.

## 1. Design Solutions for Organizational Complexity — 26%

### 1.1 Architect connectivity as a governed system

Begin with communication pairs, protocols, traffic direction, throughput/latency, address families, overlapping CIDRs, encryption, inspection, DNS, availability, failure ownership, and cost. Then choose a topology.

- **VPC peering** is direct and non-transitive. It can be simple for a small, stable set, but meshes scale poorly.
- **Transit Gateway** supplies a regional hub with route tables for segmentation. Cross-Region peering, inspection VPCs, AWS RAM sharing, and attachments introduce explicit routing and cost decisions.
- **Cloud WAN** can centralize policy and global network management when the organization needs that operating model; do not select it merely because the topology spans Regions.
- **PrivateLink** exposes a service to consumers without full network reachability. Compare service-oriented access with routed VPC connectivity.
- **Direct Connect** provides private connectivity but not encryption by itself. Design redundant locations/devices/connections as requirements demand; combine VPN or MACsec where the actual interface and threat model support it.
- **Site-to-Site VPN** gives encrypted tunnels over IP connectivity. It may be primary for suitable bandwidth/latency needs or a diverse backup to Direct Connect.
- **Route 53 Resolver endpoints/rules** solve hybrid DNS forwarding. Private hosted-zone association, split-horizon names, DNSSEC context, query logging, and failure behavior belong in the design.

For centralized inspection, trace every route: source subnet → attachment/route table → inspection appliance or Network Firewall → egress/target → return path. Stateful inspection requires symmetric routing. Use VPC Flow Logs, Transit Gateway Flow Logs, Route Analyzer/reachability tools, resolver query logs, and appliance metrics to test assumptions.

**Related item:** IP address management is an organizational capability. IPAM, non-overlapping allocation, IPv6 strategy, subnet growth reservations, ownership, and acquisition integration prevent a future network from becoming the migration blocker.

### 1.2 Prescribe security controls across accounts

Treat authentication, authorization, resource policy, network reachability, cryptography, detection, and response as separate layers.

- Federate workforce access through IAM Identity Center and the enterprise identity provider; use permission sets and short-lived roles rather than duplicating IAM users.
- Use workload roles and temporary credentials. For cross-account access, evaluate the identity policy, resource policy or role trust, permissions boundary, session policy, SCP/RCP context, and explicit denies.
- Organize preventive controls centrally through Organizations/Control Tower while delegating service administration where appropriate. SCPs bound permissions; they do not grant access.
- Centralize immutable/auditable CloudTrail, Config, access, network, application, and security findings with deliberately limited administrative paths.
- Select KMS keys, ACM/private CA, CloudHSM, Secrets Manager, and rotation patterns according to control, tenancy, availability, integration, and compliance—not “maximum security” as a slogan.
- Use WAF, Shield, Firewall Manager, Network Firewall, GuardDuty, Security Hub, Inspector, Macie, Access Analyzer, and Detective only where their evidence or enforcement role meets the threat model.

Map data classification to collection, allowed use, residency, encryption, access, masking/tokenization, retention, recovery, legal hold, deletion, and evidence. A replicated encrypted database is still noncompliant if the destination, key policy, or restore access violates the contract.

### 1.3 Design reliability and resilience from business impact

Availability, fault tolerance, backup, and disaster recovery are related but not interchangeable. Define RTO, RPO, maximum tolerable outage, dependency recovery order, minimum viable capacity, regional impairment assumptions, and recovery authority.

- **Backup/restore:** lowest steady-state footprint, generally longer recovery and more reconstruction/testing responsibility.
- **Pilot light:** persistent critical data/core components with remaining capacity activated during recovery.
- **Warm standby:** scaled-down but functional copy, faster recovery at higher ongoing cost.
- **Multi-site active/active:** lowest potential interruption for appropriate workloads, but demands conflict, consistency, routing, quota, dependency, and operational maturity decisions.

Align replication lag and backup frequency with RPO. Align detection, decision, infrastructure activation, data readiness, dependency order, traffic movement, verification, and communication with RTO. Cross-Region copies and immutable vault controls protect against different threats; neither proves recovery. Test restores and failback.

### 1.4 Design a multi-account environment

Accounts are isolation, quota, billing, ownership, and blast-radius boundaries. Build an OU/account taxonomy around security and operational intent—such as security, log archive, infrastructure, shared services, workloads, sandbox, and suspended—not around a brittle copy of the org chart.

- Establish an organization landing zone, identity federation, approved Regions, centralized logging, security aggregation, network/DNS foundations, backup, tagging, budgets, and account-vending lifecycle.
- Use SCPs and other organization policies for broad guardrails; use IAM/resource policies for grants. Test policies in a limited OU before broad deployment.
- Share supported resources with RAM where lifecycle and trust fit; otherwise expose services through APIs, events, PrivateLink, or replicated data rather than creating ownership ambiguity.
- Centralize standards and evidence while preserving application-team autonomy within guardrails. Define delegated administrators, break-glass access, exception expiry, and account closure/quarantine.

The [AWS multi-account strategy](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) is a pattern reference, not a mandatory account count.

### 1.5 Make cost visible and governable

Costs must map to an owner, outcome, environment, product, or tenant. Use account structure plus cost-allocation tags/categories, CUR/Data Exports, Cost Explorer, Budgets, Anomaly Detection, Compute Optimizer, Trusted Advisor, and service-specific telemetry.

Model total cost: resource, license, operations, support, data transfer, NAT/inspection, log ingestion/retention, backup, cross-Region replication, idle failover, migration overlap, and engineering time. Commitments such as Savings Plans or Reserved Instances fit stable eligible usage after rightsizing; they do not repair waste. Spot fits interruption-tolerant work with a fallback and checkpoint strategy.

**Related item:** Unit economics—cost per transaction, tenant, build, model inference, or GB processed—connect architecture to demand better than a falling monthly bill alone.

## 2. Design for New Solutions — 29%

### 2.1 Start from a deployment and ownership contract

Choose IaC boundaries, repositories, artifact provenance, environments/accounts, configuration/secrets, tests, approvals, deployment strategy, database compatibility, rollback/roll-forward, drift ownership, and audit evidence together.

- CloudFormation/CDK/SAM or other IaC should produce reviewable change and consistent promotion. StackSets distribute approved patterns across accounts/Regions; nested modules reduce duplication; neither removes lifecycle design.
- Build an artifact once, sign/scan it, and promote the same immutable identity. Rebuilding per environment weakens provenance.
- Select rolling, in-place, blue/green, canary, linear, or immutable deployment based on state, capacity, compatibility, observation window, rollback time, and cost.
- Separate infrastructure rollback from irreversible data change. Use expand/migrate/contract schemas, backward-compatible events/APIs, feature flags, and verified backups where appropriate.
- Prefer managed services when they meet requirements and materially reduce undifferentiated patching/provisioning work. Managed does not mean configuration-free or responsibility-free.

### 2.2 Design business continuity end to end

A healthy application tier is irrelevant if identity, DNS, keys, configuration, queues, data, certificates, quotas, or operator access cannot recover. Diagram dependencies and recovery order. Choose Multi-AZ for localized availability and multi-Region only when regional business requirements justify the consistency, routing, operational, and cost burden.

For data, distinguish synchronous availability from asynchronous DR and global distribution. Compare RDS/Aurora topology, DynamoDB global tables, S3 replication, EFS/FSx capabilities, OpenSearch, caches, streams, and self-managed replication based on consistency, writer model, conflict, lag, failover, restore, and failback—not brand familiarity.

Use Route 53 health/traffic policies, Global Accelerator, CloudFront, load balancers, and application health semantics appropriately. A DNS change has TTL/cache behavior; an accelerator or anycast endpoint has different routing behavior. Health should represent the service outcome, not only an instance process.

### 2.3 Place security at every trust transition

Define workforce, workload, customer, device, partner, and service identities. Minimize standing privilege and credential distribution. Segment public ingress, service-to-service paths, administration, egress, data access, and cross-account access.

For internet applications, combine DDoS posture, edge controls, TLS/certificate lifecycle, WAF rules, authenticated application authorization, least-privilege data access, logging, abuse/rate controls, vulnerability management, patching, and tested response. Private endpoints reduce internet exposure but do not replace authorization or data policy.

Use envelope encryption and service integrations correctly: KMS authorizes cryptographic use; application/service policies authorize data operations. Consider key ownership, separation of duties, multi-Region key behavior, grant/policy scope, rotation, deletion protection, availability, audit, and restore paths.

### 2.4 Design distributed reliability, not bigger instances

Identify hard dependencies and decide whether to remove, replicate, queue, cache, degrade, or fail fast. Use bounded retries with jitter, timeouts, idempotency, circuit breaking, backpressure, dead-letter handling, poison-message isolation, and reconciliation.

- SQS buffers work; SNS fans out; EventBridge routes events; Kinesis/MSK handle ordered stream use cases; Step Functions coordinate explicit workflows. Delivery, ordering, retention, replay, throughput, and consumer ownership decide among them.
- Scale on the metric closest to demand: queue age/depth, concurrency, request rate, target response time, stream lag, or custom work units. Check quotas and downstream capacity.
- Use cells/shards, bulkheads, tenant isolation, and failure-domain placement to bound blast radius at enterprise scale.
- Validate service SLAs only after composing dependencies. An architecture’s availability is not automatically the highest SLA on its diagram.

### 2.5 Select performance by access pattern

Quantify latency percentiles, throughput, concurrency, object size, request mix, consistency, data volume/growth, locality, durability, and burst behavior.

- Choose compute among instances, containers, functions, batch, and managed application platforms based on runtime/control, scaling unit, startup, scheduling, portability, operations, and economics.
- Choose storage among S3, EBS, EFS, FSx families, instance store, and gateways based on object/block/file semantics, sharing, protocol, performance, lifecycle, availability, and recovery.
- Choose purpose-built databases based on access pattern and transaction/query contract. RDS/Aurora, DynamoDB, ElastiCache, OpenSearch, Neptune, Timestream, DocumentDB, Redshift, and self-managed engines solve different problems.
- Use cache only with an ownership, invalidation, staleness, eviction, failure, and stampede plan. Use read replicas for supported read scaling, not to imply synchronous failover.
- Place CloudFront, Global Accelerator, transfer acceleration, edge compute, replicas, or partitioning only when measurements and geography support the choice.

### 2.6 Optimize cost without violating requirements

Model cost across normal, peak, recovery, and growth states. Include request and operation charges, inter-AZ/cross-Region/internet transfer, NAT gateways, load balancers, public IPv4, provisioned capacity, replication, cache, observability, backup, support, and people.

Rightsize first; schedule or autoscale variable nonproduction; apply lifecycle/tiering to data only when access and retrieval requirements fit; choose serverless or provisioned capacity based on usage shape; place processing near data; and use commitments for stable eligible baselines. A cheaper component can increase total cost through failure, data transfer, or operational toil.

## 3. Continuous Improvement for Existing Solutions — 25%

### 3.1 Establish an evidence-led improvement loop

Inventory workloads and owners, define SLOs/KPIs, map dependencies, centralize telemetry, identify risk/toil/cost, rank changes by impact and effort, test them, deploy safely, measure outcomes, and update standards. The [Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) supplies review lenses; it is not a one-time compliance score.

Improve operational excellence with useful logs/metrics/traces, correlation IDs, deployment/configuration events, actionable alarms, dashboards, runbooks, incident roles, automated bounded remediation, post-incident learning, game days, and tested rollback. Monitor the customer journey and dependency saturation, not only CPU.

### 3.2 Improve security from evidence and threat

Review unused access, external exposure, trust policies, credential age, secrets distribution, key policies, network paths, vulnerabilities, configuration drift, data classification, retention, backup integrity, and finding response.

Centralize findings without centralizing every remediation decision. Automate high-confidence, reversible containment; require approval for high-blast-radius actions; preserve evidence; route ownership; track exception expiry; and measure mean time to detect/contain/remediate.

**Related item:** A control that exists but is not observable, owned, tested, and enforced is architectural debt. Record control objective → implementation → evidence → responder → exception process.

### 3.3 Improve performance scientifically

Translate complaints into measurable workload KPIs and latency budgets. Correlate request traces with compute, storage, database, network, queue, cache, and external dependencies. Identify whether the system is CPU, memory, I/O, lock, connection, partition, quota, or dependency bound.

Form a hypothesis, reproduce with representative data/concurrency, change one relevant variable, compare percentiles and error rates, and assess cost/reliability effects. Candidate changes include indexes/query shape, connection pooling, partition keys, cache, replicas, batching, concurrency, instance/storage class, edge delivery, compression, asynchronous work, and purpose-built managed services.

### 3.4 Improve reliability through failure learning

Use growth trends, incident history, quota headroom, dependency maps, recovery tests, backup reports, replication lag, deployment failures, and operational readiness reviews. Remove single points of failure, add appropriate redundancy, bound failure domains, make operations idempotent, and verify that scaling does not overload downstream systems.

Test instance/AZ/dependency/Region failures according to the risk model. Measure detection plus recovery and data loss against RTO/RPO. Exercise restore, failover, failback, certificate/key availability, identity, DNS, quotas, and operator access.

### 3.5 Optimize cost continuously

Analyze CUR/Data Exports at account, tag/category, service, usage type, Region, purchase option, and unit-cost levels. Find idle resources, oversized capacity, unattached storage/IPs, stale snapshots, excess logs, inefficient transfers, duplicated data, and commitment coverage/utilization gaps.

Prioritize changes by verified savings, engineering effort, risk, reversibility, and opportunity cost. Alert on abnormal cost and forecast deviation, but assign an owner who can diagnose and act. Validate savings after change and ensure SLO/security/recovery were not degraded.

## 4. Accelerate Workload Migration and Modernization — 20%

### 4.1 Assess a portfolio before moving it

Create an application inventory with business owner, criticality, users, dependencies, data/classification, latency, licensing, infrastructure, utilization, lifecycle, recoverability, compliance, change freeze, and target outcome. Discovery tooling helps; workshops and dependency validation remain necessary.

Classify each workload using the 7 Rs: retire, retain, rehost, relocate, replatform, repurchase, or refactor/re-architect. Names vary slightly across methods; the decision matters. Do not force all applications into the same R. Use business value, risk, deadline, technical fit, skills, TCO, dependency cohesion, and modernization benefit.

Build waves around dependencies, landing-zone readiness, data transfer, network/identity/DNS, shared services, vendor constraints, business calendars, test capacity, cutover/rollback, and support. Start with representative learning waves, not necessarily the easiest or most critical workload.

### 4.2 Choose transfer and migration mechanisms

- **Application/server:** Application Migration Service supports block-level replication/rehost patterns; relocation or platform-native methods may fit VMware, containers, SaaS, or managed platforms.
- **Database:** DMS can move/replicate supported engines; Schema Conversion Tool and conversion approaches help heterogeneous migration. Validate unsupported objects, data types, CDC lag, consistency, performance, cutover, and rollback.
- **Online data:** DataSync, Transfer Family, Storage Gateway, S3 transfer features, and service-native replication solve distinct protocols, connectivity, acceleration, hybrid access, and ongoing synchronization needs.
- **Offline data:** Snow Family can fit volume/bandwidth/time/security constraints. Include appliance lead time, encryption, chain of custody, export/import workflow, and delta synchronization.
- **Connectivity:** Direct Connect, VPN, internet paths, Transit Gateway, DNS, and identity must be ready and capacity-tested before migration traffic competes with production.

Secure migration staging, replication agents, roles, keys, network paths, snapshots, logs, and temporary exceptions. Define validation totals/checksums, functional/performance tests, cutover authority, rollback point, delta handling, and decommission evidence.

### 4.3 Choose a target platform from constraints

Evaluate EC2, Elastic Beanstalk/App Runner, ECS/EKS/Fargate, Lambda, Batch, managed databases, and storage based on application/runtime compatibility, control, scaling, availability, portability, skills, licenses, compliance, patching, operational burden, and cost.

Rehost may meet a deadline but preserve operational debt. Replatform can remove some management without deep code change. Refactoring can improve scalability and delivery but raises transformation risk. Establish a two-step roadmap when “migrate now, modernize safely later” best meets the outcome—plus explicit debt, owner, and deadline.

### 4.4 Modernize around business and operational value

Good candidates have scaling bottlenecks, release coupling, expensive licenses, fragile recovery, high toil, end-of-life platforms, or valuable event/data reuse. Decompose by bounded capability and ownership, not arbitrary technical layers.

Use APIs, queues, events, workflows, containers, serverless, purpose-built databases, managed analytics, and GenAI only when they improve a measured constraint. Preserve idempotency, schema/version compatibility, data consistency, observability, security, failure handling, and rollback across old and new paths. Strangler patterns and change-data capture can reduce big-bang risk.

**Related item:** Decommissioning is part of migration. Remove obsolete servers, accounts, network routes, identities, licenses, DNS, replication, backups, and monitoring only after retention, rollback, financial, and audit requirements are met.

## Emerging topics — unscored pretest boundary

AWS currently says questions about evolving technologies may appear as unscored pretest content. The published items cover content filtering/regulatory controls for generative AI (for example, Bedrock Guardrails), access controls for generative/agentic applications (for example, AgentCore Identity), and human approval for AI operations (for example, Step Functions).

Study the architecture principle, not speculative product trivia: classify harmful or regulated outputs, constrain identity and tool authorization, validate action arguments, require approval for consequential/irreversible work, log traceable decisions, protect private context, and define safe failure. Do not let this small unscored section displace the four scored domains.

## Integrated scenarios

### Scenario 1: Global regulated enterprise landing zone

A newly combined enterprise has overlapping IP space, separate identity systems, Region restrictions, shared inspection, acquisition autonomy, and a six-hour recovery target. Design an OU/account model, federation transition, IPAM and connectivity segmentation, DNS/egress/inspection, centralized evidence, data/Region guardrails, exception lifecycle, cost allocation, and tested recovery. Explain which controls belong in SCP/RCP, IAM/resource policy, network, encryption, detective, and response layers.

### Scenario 2: Consumer platform expansion

A single-Region ordering system has synchronous dependencies, uneven peaks, slow releases, a stateful database, 99.95% service objective, two-hour RTO, fifteen-minute RPO, and global latency goals. Propose staged decoupling, caching/database/read topology, deployment/data compatibility, Multi-AZ and regional recovery, routing, observability, load/failure tests, quota plan, and cost model. State consistency and degraded-mode behavior.

### Scenario 3: Portfolio migration and modernization

A company must leave a data center in twelve months. Its portfolio includes commercial VMware software, a latency-sensitive factory app, a batch platform, a file share, a relational monolith, and unused systems. Build discovery, 7R dispositions, dependency-aware waves, landing-zone prerequisites, online/offline transfer decisions, DMS/MGN validation where appropriate, rollback/cutover evidence, two-step modernization candidates, and decommission controls.

## Practice labs

Use disposable accounts/resources, budgets, synthetic data, least privilege, and teardown evidence. Estimated times exclude prerequisite remediation.

### Lab 1: Multi-account decision record — 180–300 minutes

Create a diagram and ADR for OUs/accounts, identity, delegated administration, log archive, security aggregation, networking, shared services, backup, budgets, account vending, guardrails, exceptions, and closure. Test at least one SCP in a sandbox OU and document why it limits rather than grants.

### Lab 2: Hybrid routing and DNS proof — 180–300 minutes

Model two VPCs and simulated on-premises connectivity using Transit Gateway or an equivalent safe lab. Record route tables, security controls, DNS Resolver direction, expected/denied flows, return paths, logs, failure modes, and hourly/data-processing cost. Break a route and diagnose it from evidence.

### Lab 3: Resilience and recovery experiment — 240–360 minutes

Define RTO/RPO for a small application, create dependency/recovery-order diagrams, implement backup/replication appropriate to the lab, perform a restore or failover, measure each recovery phase, verify data, exercise failback, and reconcile results with objectives.

### Lab 4: Immutable delivery and data compatibility — 180–300 minutes

Build one artifact, capture provenance, promote it through two environments using IaC, deploy with canary or blue/green behavior, introduce a backward-compatible schema change, trigger rollback/roll-forward, and preserve change/test/metric evidence.

### Lab 5: Distributed failure controls — 180–300 minutes

Create an API-to-queue-to-worker flow. Add idempotency, bounded retry/jitter, timeout, DLQ, replay, correlation, queue-age scaling, and a reconciliation report. Inject throttling, duplicate delivery, poison input, worker loss, and downstream failure; explain the observed behavior.

### Lab 6: Performance and cost investigation — 180–300 minutes

Generate representative load, capture latency percentiles and dependency saturation, form and test two remediation hypotheses, then model resource, request, storage, NAT/data transfer, logging, backup, and recovery cost. Report unit cost and any reliability/security tradeoff.

### Lab 7: Migration wave plan — 180–300 minutes

Inventory five synthetic applications, map dependencies, assign evidence-backed 7R dispositions, build waves, select transfer/migration mechanisms, define landing-zone gates, data validation, cutover/rollback, hypercare, and decommission evidence. Challenge the plan with bandwidth and deadline changes.

### Lab 8: Well-Architected improvement backlog — 180–300 minutes

Review a disposable workload across all pillars. Turn observations into prioritized items with risk/outcome, evidence, owner, effort, dependency, rollback, acceptance metric, and due date. Implement one security, reliability, operational, performance, and cost improvement; measure the result.

## Knowledge checks

1. Why is a full-mesh peering plan risky as VPC count grows?
2. When is PrivateLink a better boundary than routed VPC connectivity?
3. Why can a stateful inspection path fail even when forward routes look correct?
4. What availability does Direct Connect alone guarantee, and what must the design add?
5. What policy layers should be checked for a denied cross-account request?
6. Why does an SCP not give a role permission?
7. How should an account taxonomy differ from an org chart?
8. What evidence makes an exception process governable?
9. How do RTO and RPO affect topology and replication?
10. Why is a cross-Region copy not proof of recoverability?
11. When is warm standby preferable to pilot light?
12. What does unit cost reveal that a monthly total may hide?
13. Why build an artifact once and promote it?
14. How does an irreversible database change alter rollback design?
15. What makes a deployment strategy appropriate rather than universally “best”?
16. Why must identity, DNS, keys, quotas, and operator access appear in a DR plan?
17. How do health semantics affect global traffic failover?
18. Why do private endpoints not replace authorization?
19. What determines whether SQS, SNS, EventBridge, Kinesis, or Step Functions fits?
20. Why should scaling use queue age or work units instead of CPU in some systems?
21. What controls retry amplification during dependency failure?
22. Why might a read replica not satisfy a failover requirement?
23. What must a cache invalidation and failure plan specify?
24. Which cost components commonly overturn a superficially cheap design?
25. How should commitment purchases follow rightsizing?
26. What turns a Well-Architected review into continuous improvement?
27. When should security remediation be automated versus approval-gated?
28. How do you test a performance hypothesis without confusing correlation and cause?
29. Which evidence exposes a downstream bottleneck hidden by healthy compute CPU?
30. Why test failback as well as failover?
31. What should a cost optimization acceptance test protect?
32. What portfolio facts are needed before assigning a migration R?
33. Why should migration waves follow dependencies rather than only business priority?
34. What must be validated during heterogeneous database migration?
35. When could offline transfer beat network transfer?
36. Why can “rehost now, modernize later” be sound, and what makes it dangerous?
37. What boundaries should guide monolith decomposition?
38. Why is decommissioning part of migration architecture?
39. How should GenAI guardrails relate to identity and tool authorization?
40. Why should an AI human-approval step be risk-based rather than universal?
41. Which parts of the current SAP-C02 guide are scored versus emerging pretest scope?
42. What evidence distinguishes a professional architecture recommendation from a product list?

### Answer guide

1. Connections, routes, policies, troubleshooting, and change coordination grow rapidly; a hub or service boundary may reduce complexity.
2. When consumers need private access to a specific service without broad network reachability or route exchange.
3. Return traffic may take an asymmetric path and miss the stateful appliance/session.
4. It supplies a connection construct, not an end-to-end availability guarantee; add diverse location/device/connection and appropriate encrypted backup according to requirements.
5. Identity/resource policies, role trust, boundaries, session policies, SCP/RCP context, KMS/service conditions, and explicit denies.
6. It is a maximum-permission guardrail; an identity or resource policy still must allow the operation.
7. Organize by stable security, isolation, lifecycle, ownership, quota, and policy intent rather than transient reporting structure.
8. Owner, business reason, scope, compensating controls, approval, evidence, expiry, and review/removal path.
9. RPO constrains backup/replication and consistency; RTO constrains detection, activation, data readiness, dependencies, routing, validation, and capacity.
10. Restore, dependencies, credentials/keys, integrity, application validation, routing, quotas, and operator procedures may still fail.
11. When faster recovery and a continuously functional scaled-down environment justify higher steady-state cost and operations.
12. Whether efficiency improves as demand changes and which product/tenant/workflow creates spend.
13. To preserve tested provenance and avoid environment-specific rebuild drift.
14. Use compatible expand/migrate/contract changes, backups, feature controls, and a roll-forward plan; binary rollback alone may be unsafe.
15. Required risk, state, compatibility, capacity, observation, rollback time, availability, and cost.
16. They are dependencies needed to authenticate, discover, decrypt, provision, route, and operate the recovered workload.
17. A shallow process check can route users to a service that cannot complete its critical transaction.
18. They change network exposure; IAM/resource/data authorization still controls operations.
19. Delivery, ordering, fan-out/routing, replay, throughput, workflow state, integration, and consumer ownership requirements.
20. CPU may not reflect backlog or concurrency; demand/outcome metrics align capacity with actual work and SLO risk.
21. Bounded exponential backoff with jitter, timeouts, retry budgets, circuit breaking, queue/backpressure, and idempotency.
22. It may be asynchronous, read-only, or require manual promotion/DNS changes and may not meet RPO/RTO.
23. Ownership, keys, TTL/invalidation, acceptable staleness, eviction, miss/stampede behavior, outage mode, and source protection.
24. Data transfer/NAT, requests, observability, backup/replication, idle recovery capacity, licenses/support, and operational labor.
25. Remove waste and measure stable eligible baseline first; then size commitments and track coverage/utilization.
26. Owners, evidence, prioritized actions, acceptance metrics, safe delivery, measured outcomes, and recurring review.
27. Automate high-confidence, reversible, bounded actions; gate consequential or ambiguous changes and preserve incident evidence.
28. Establish representative baseline, change one relevant variable, compare percentiles/errors and repeat while controlling workload.
29. Traces plus queue/connection/database/storage/network/dependency latency and saturation telemetry.
30. Recovery is incomplete if returning to normal operation causes data divergence, outage, or untested manual steps.
31. SLOs, security/compliance, recovery, performance, and operability while verifying actual savings/unit cost.
32. Owner, value, criticality, dependencies, data, usage, licensing, lifecycle, compliance, recoverability, deadline, skills, and TCO.
33. Splitting coupled systems or shared identity/data/network services can create outage, duplication, and cutover failure.
34. Schema/data-type/object compatibility, transformation, full-load/CDC accuracy and lag, performance, integrity, cutover, and rollback.
35. When volume and available bandwidth/window make shipment faster or more predictable, assuming logistics/security/delta needs fit.
36. It can meet a deadline with lower transformation risk; it is dangerous without explicit debt, owner, outcome, and modernization deadline.
37. Business capability, data/transaction consistency, change cadence, scaling/failure needs, team ownership, and interface contract.
38. Legacy cost, exposure, routes, identities, replication, licenses, and ambiguity persist until controlled retirement is evidenced.
39. Guardrails constrain content; identity, least-privilege tool permissions, argument validation, approval, and audit constrain actions.
40. Universal approval creates unusable workflows; use impact, reversibility, confidence, data sensitivity, and authority to set gates.
41. The four weighted domains are scored; the published responsible/agentic-AI items may appear as unidentified unscored pretest content.
42. Traceable requirements, alternatives, explicit tradeoffs/assumptions, complete lifecycle, measurable tests, cost, ownership, and recovery evidence.

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. Pick one current primary route, use references to close measured gaps, complete production-shaped labs, and treat legitimate practice as diagnosis—not as content to memorize.

| Resource | Access | Estimated time |
|---|---|---:|
| AWS four-step Skill Builder route | Public/free-account/subscription mix | 30–50 hours selected plus labs |
| Pluralsight SAP-C02 path | Paid/trial | 49 listed hours plus labs/review |
| O'Reilly 2024 Packt exam guide | Paid/trial | 12 hours listed plus exercises/current gap check |
| Udemy/Stéphane Maarek SAP-C02 | Paid | 16 hours 26 minutes plus 35–60 hours hands-on |
| Tutorials Dojo course/practice | Paid | 35–60 hours estimated |
| Whizlabs SAP-C02 route | Paid | 30–60 hours estimated after catalog inspection |

- **Official route:** [AWS certification page](https://aws.amazon.com/certification/certified-solutions-architect-professional/) and [SAP-C02 Skill Builder plan](https://skillbuilder.aws/category/exam-prep/solutions-architect-professional-SAP-C02) (**about 30–50 selected hours plus substantial labs/game days**). Access to Builder Labs, Jam, SimuLearn, and the official practice exam varies by entitlement.
- **Structured current path:** [Pluralsight SAP-C02](https://www.pluralsight.com/paths/aws-certified-solutions-architect-professional-sap-c02) (**49 listed hours**, 15 courses, three labs and practice exam). It mixes rolling 2025–2026 replacements with labeled legacy modules; select deliberately.
- **Book route:** [O'Reilly / Packt SAP-C02 Exam Guide](https://www.oreilly.com/library/view/aws-certified-solutions/9781801813136/) (**428 pages / 12 hours 1 minute listed**, March 2024). Strong domain structure; close newer service-name and unscored-emerging-topic gaps with official sources.
- **Video supplement:** [O'Reilly Pearson SAP-C02 video](https://www.oreilly.com/videos/aws-certified-solutions/9780138319205/) (**verify runtime after access**) or the older [Noah Gift 2023 route](https://www.oreilly.com/videos/aws-solutions-architect/10082022VIDEOPAIML/) (**use only selectively with a current gap check**).
- **Concise review:** [Udemy/Stéphane Maarek SAP-C02](https://www.udemy.com/course/aws-solutions-architect-professional/) (**16 hours 26 minutes**, 203 lectures, shown updated August 2026). The page explicitly says slides only/no hands-on; add substantial architecture work.
- **Course/practice route:** [Tutorials Dojo SAP-C02 video](https://portal.tutorialsdojo.com/courses/aws-certified-solutions-architect-professional-sap-c02-video-course/) plus [practice exams](https://portal.tutorialsdojo.com/courses/aws-certified-solutions-architect-professional-practice-exams/) (**about 35–60 hours estimated**; practice page lists randomized, six timed, six review, four domain modes, and flashcards).
- **Lab/practice alternative:** [Whizlabs SAP-C02](https://www.whizlabs.com/aws-solutions-architect-professional/) (**30–60 selected hours estimated**); inspect exact current course, sandbox, lab, and practice totals after access.

Suggested preparation: an experienced multi-account AWS architect may need **120–180 hours**; a learner still closing associate-level, networking, security, migration, and operations prerequisites may need **220–350 hours**.

---

## Source map and freshness notes

The root guide and four detailed domain pages define scored scope and the current unscored emerging-topic boundary. The certification page defines live delivery. The in-scope list is non-exhaustive and mutable. The Well-Architected and multi-account references supply architecture method; product documentation supplies behavior; learning providers support only their catalog claims.

- **VERIFY CURRENT:** service names/status, APIs, integrations, Regions, quotas, SLAs, pricing, purchase models, licensing, migration tooling, GenAI/AgentCore behavior, and training metadata.
- **Stable method:** requirement contract → boundaries/dependencies → alternatives → explicit tradeoffs → governed delivery/migration → measured recovery/operations → continuous improvement.
- **Freshness check:** explicitly separate four scored domains from unscored emerging topics and gap-check older material against the current official domain and service pages.

This guide uses no recalled exam questions or restricted content. The knowledge checks are original and test published concepts rather than reproducing vendor items.
