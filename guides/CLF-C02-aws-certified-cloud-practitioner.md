---
exam_code: CLF-C02
vendor_id: aws
official_blueprint: https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# CLF-C02 AWS Certified Cloud Practitioner Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#clf-c02-coverage-record). The [official CLF-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html) is authoritative.

**Current baseline:** CLF-C02, four domains and 50 scored plus 15 unscored questions<br>
**Upcoming blueprint change:** None announced in the official exam-guide index or CLF-C02 pages as of September 1, 2026.<br>
**Official source:** [AWS Certified Cloud Practitioner exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)

## How to use this guide

CLF-C02 tests whether you can explain AWS value, responsibility, services, security, and economics at a foundational level. It does not expect you to code, troubleshoot production systems, or design detailed architectures. Learn the decision behind each service category, not a list of logos. For each contrast, state the requirement, the best fit, why a nearby option is weaker, and which responsibility stays with the customer.

The official certification page lists a 90-minute, 65-question exam delivered online or at Pearson VUE, priced at USD 100 before applicable regional pricing or taxes. The detailed guide identifies 50 scored and 15 unidentified unscored questions, a 700 minimum scaled score, and compensatory scoring across domains. Recheck the [current exam page](https://aws.amazon.com/certification/certified-cloud-practitioner/) before scheduling.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Cloud Concepts | 24% | Why use AWS, and how do cloud design, migration, and economics change decisions? |
| Security and Compliance | 30% | Who is responsible, how is access governed, and which controls supply evidence or protection? |
| Cloud Technology and Services | 34% | Which global-infrastructure component or service category fits the requirement? |
| Billing, Pricing, and Support | 12% | Which purchase model, cost tool, support resource, or partner channel fits? |

The percentages apply to scored content. The official guide says the task statements are representative rather than exhaustive; use the linked in-scope list as a boundary, not as a command to memorize every feature.

---

## 1. Cloud Concepts — 24%

The official [Cloud Concepts domain](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html) covers cloud value, Well-Architected principles, migration, and cloud economics.

### Value: agility, elasticity, reach, and availability

AWS exposes compute, storage, networking, data, security, and managed services through on-demand interfaces. That changes how an organization acquires and operates capacity:

| Concept | Meaning | Decision clue | Frequent mistake |
|---|---|---|---|
| Agility | Experiment and provision faster | A team must test an idea without a hardware purchase cycle | Treating speed as permission to skip governance |
| Elasticity | Capacity can expand and contract with demand | Traffic changes sharply and resources should follow it | Calling any large fixed deployment elastic |
| Scalability | A system can handle changed load by adding or resizing capacity | Growth is expected and the design must accommodate it | Assuming scaling automatically creates resilience |
| High availability | The workload resists a component or location failure | Service continuity matters during an instance or Availability Zone failure | Assuming one instance is highly available because AWS operates it |
| Global reach | Services can be deployed nearer users in multiple Regions | Latency, sovereignty, or disaster recovery drives geography | Assuming every service exists in every Region |
| Managed service | AWS operates more of the underlying platform | The team wants to focus on data or application behavior | Assuming AWS owns customer data, access, and configuration |

Cloud does not remove capacity, security, or financial planning. It replaces slow procurement with programmable choices. Those choices can be repeated, measured, and governed—but they can also create waste or exposure quickly.

### Well-Architected is a tradeoff framework

The [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html) organizes design reviews around six pillars: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

| Requirement | Relevant pillar question |
|---|---|
| Recover after a component failure | Reliability: are failure modes isolated and recovery tested? |
| Prevent long-lived administrator credentials | Security: how is identity risk reduced and access reviewed? |
| Reduce manual deployment mistakes | Operational excellence: can the change be automated, observed, and reversed? |
| Match compute to workload behavior | Performance efficiency: is the resource type and scaling model appropriate? |
| Remove idle resources | Cost optimization: is spending connected to value and ownership? |
| Reduce unnecessary resource use | Sustainability: can demand be met with fewer or better-utilized resources? |

The pillars are not independent scores. A multi-Region design might improve recovery while adding cost and operational complexity. A good decision records the requirement and accepted tradeoff.

> **Related item:** A service-level agreement describes a provider commitment under stated conditions; a workload service-level objective expresses the reliability target the team intends to meet. The application still needs redundancy, monitoring, and recovery appropriate to its objective.

### Migration is portfolio work, not copying servers

The [AWS Cloud Adoption Framework](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/welcome.html) connects transformation across business, people, governance, platform, security, and operations perspectives. A migration decision should include business outcome, dependencies, identity and network readiness, data movement, operating ownership, and a cutover/rollback plan.

| Strategy | Change level | Use when | Risk to test |
|---|---|---|---|
| Rehost | Move largely as-is | Speed matters and redesign can wait | Old inefficiency and operational assumptions move too |
| Replatform | Make bounded platform improvements | A managed database or runtime reduces operations without rewriting the application | Compatibility, performance, and rollback |
| Refactor | Redesign application components | Elasticity, resilience, or delivery speed justifies deeper change | Scope, data consistency, and organizational readiness |
| Repurchase | Replace with a commercial/SaaS product | A product meets the requirement better than maintaining custom software | Data migration, integration, and exit terms |
| Retain | Keep in the current environment for now | Latency, regulation, dependency, or timing blocks migration | Permanent deferral without an owner or review date |
| Retire | Decommission what no longer provides value | Usage and dependency evidence supports removal | Hidden consumers and retention obligations |

Migration Evaluator can help build a cost case; Application Discovery Service and Migration Hub support discovery/tracking; Application Migration Service supports server migration; DMS and Schema Conversion Tool support database moves. The foundational decision is still workload-specific.

### Cloud economics: cost follows configuration and consumption

Cloud can replace some capital expenditure with variable operating expense and can benefit from provider economies of scale. Savings are not automatic. An oversized always-on instance, unnecessary data transfer, forgotten snapshots, and unused public addresses can make a technically sound deployment financially poor.

Use this reasoning chain:

1. Identify the business unit of value: request, user, environment, transaction, or dataset.
2. Estimate demand and nonfunctional requirements.
3. Choose service and purchase models.
4. Tag or otherwise allocate ownership.
5. Measure actual cost and usage.
6. Right-size, schedule, delete, tier, or redesign.
7. Verify that optimization did not weaken security or reliability.

Licensing can be included with a service or brought under eligible BYOL terms. Rightsizing means matching provisioned capacity to measured demand, not merely choosing the cheapest resource.

> **Related item:** FinOps is a cross-functional operating practice for maximizing cloud business value. A budget or recommendation is useful only when an accountable owner can act on it and verify the result.

---

## 2. Security and Compliance — 30%

The official [Security and Compliance domain](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html) covers shared responsibility, governance/compliance, identity, and security resources.

### Shared responsibility changes by service

AWS is responsible for security **of** the cloud: facilities, physical hardware, and the infrastructure that operates AWS services. Customers are responsible for security **in** the cloud: data, identities, permissions, workload configuration, and every layer they control. The exact split changes with the service, as described by the [AWS shared responsibility model](https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/shared-responsibility-model.html).

| Layer or decision | EC2 | RDS | Lambda | Customer responsibility that remains |
|---|---|---|---|---|
| Physical facility and host | AWS | AWS | AWS | Select suitable Region/service and design required resilience |
| Guest operating system | Customer | AWS | AWS | EC2 patching/hardening; managed services abstract this layer |
| Database engine maintenance | Customer on self-managed DB | Mostly AWS-managed | Not applicable | Configure maintenance, access, backups, schema, and data appropriately |
| Application code/configuration | Customer | Customer | Customer | Secure code, dependencies, secrets, logging, and input handling |
| Identity and data | Customer | Customer | Customer | Classification, least privilege, encryption choices, retention, and recovery |

Managed does not mean responsibility-free. Moving from EC2 to RDS transfers engine and host tasks to AWS, but the customer still chooses network exposure, credentials, encryption, users, backups, and data behavior.

### Identity: prefer temporary, least-privilege access

Protect the root user, require MFA, avoid root access keys, and use it only for tasks that require it. Human users should normally federate through IAM Identity Center or another identity provider. Workloads should use IAM roles and temporary credentials instead of embedded long-lived access keys. AWS documents these controls in [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

| IAM object or capability | Purpose | Distinction |
|---|---|---|
| User | Long-term identity in one AWS account | Avoid as the default workforce pattern when federation is available |
| Group | Permission grouping for IAM users | A group cannot be assumed like a role |
| Role | Assumable identity with temporary credentials | Useful for workloads, federation, and cross-account access |
| Identity-based policy | Permissions attached to an identity | Says what that principal may do to which resources |
| Resource-based policy | Permissions attached to a resource | Can name allowed principals, including cross-account principals |
| Service control policy | Maximum permissions guardrail for organization accounts | Does not grant permissions by itself |
| Permission boundary | Maximum permissions for a user or role | Must intersect with granted permissions |

Effective access depends on applicable grants, boundaries, organization policies, resource policies, and explicit denies. Authentication proves identity; authorization decides allowed action.

### Governance, audit, monitoring, and compliance evidence

| Need | Service or resource | What it answers |
|---|---|---|
| API activity history | AWS CloudTrail | Who called which supported API, when, and from where? |
| Resource configuration history/rules | AWS Config | What configuration existed, and does it meet a rule? |
| Metrics, logs, dashboards, alarms | Amazon CloudWatch | What is the workload or service doing operationally? |
| Compliance reports and agreements | AWS Artifact | Which AWS audit artifact or agreement is available? |
| Security findings aggregation | AWS Security Hub | Which normalized security findings need prioritization? |
| Threat detection | Amazon GuardDuty | Which account, workload, or data-access signals look suspicious? |
| Vulnerability management | Amazon Inspector | Which supported workloads/images/packages show vulnerabilities or exposure? |
| DDoS protection | AWS Shield | Which managed DDoS protections apply? |
| Web request filtering | AWS WAF | Which HTTP/S requests should be allowed, blocked, or counted? |
| Multi-account governance | AWS Organizations and Control Tower | How are accounts grouped, governed, and baselined? |

Compliance is shared. AWS reports support the customer's evidence, but the customer must configure and operate its own controls for the applicable law, industry, contract, and data location.

### Protect data through layers

- Encrypt data in transit with suitable TLS and certificate management.
- Encrypt data at rest with service-managed or customer-managed keys as required.
- Use Secrets Manager or Systems Manager Parameter Store for supported secret/configuration patterns instead of hard-coding credentials.
- Restrict network and identity paths; encryption is not a replacement for access control.
- Enable logs, protect their integrity/retention, and route actionable findings to owners.
- Test backup and restoration. Replication and high availability do not prove recoverability from deletion or corruption.

> **Related item:** KMS manages cryptographic keys and cryptographic operations; Secrets Manager manages secret values and rotation workflows. A key protects data, while a secret is a credential or sensitive value an application must retrieve.

---

## 3. Cloud Technology and Services — 34%

The largest domain is the official [Cloud Technology and Services domain](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html). Start with the requirement, then choose a service category and operating model.

### Ways to deploy and operate

| Interface | Best fit | Control/evidence consideration |
|---|---|---|
| Management Console | Exploration and occasional human tasks | Easy to learn; manual steps are harder to reproduce |
| AWS CLI or SDK/API | Scripting and application integration | Requires credential, retry, error, and change control |
| CloudFormation or other IaC | Repeatable, reviewable infrastructure | Templates need versioning, testing, and drift awareness |
| Managed service console/API | Product-specific operations | Service configuration still needs least privilege and monitoring |

Prefer repeatable processes for environments that must be rebuilt, reviewed, or promoted. A one-time console action may fit exploration, but it is weak recovery evidence unless documented or automated.

### Global infrastructure

An AWS Region is a separate geographic area. An Availability Zone is one or more discrete data centers with independent infrastructure inside a Region. Edge locations place content or network capabilities nearer users. AWS describes the current structure in its [global infrastructure documentation](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html).

| Requirement | Typical scope |
|---|---|
| Resist one data-center/AZ failure | Deploy across multiple Availability Zones |
| Disaster recovery or data sovereignty across geography | Evaluate multiple Regions |
| Cache content close to users | Use edge services such as CloudFront |
| Lowest latency to an AWS Region over optimized paths | Consider Global Accelerator for supported network workloads |

**VERIFY CURRENT:** Region count, service availability, limits, and feature coverage change frequently. Check the current service and Region pages when the exact location matters.

### Compute: control versus abstraction

| Need | Service | Mental model | Customer operates |
|---|---|---|---|
| VM and OS control | Amazon EC2 | Resizable virtual machines | Guest OS, patches, runtime, app, scaling design |
| Run code on events without managing servers | AWS Lambda | Short-lived managed function executions | Code, dependencies, triggers, permissions, configuration |
| Managed container orchestration | Amazon ECS | AWS-native container control plane | Task/app definition and selected capacity model |
| Kubernetes API/ecosystem | Amazon EKS | Managed Kubernetes control plane | Kubernetes/workload configuration and selected nodes/capacity |
| Serverless container task capacity | AWS Fargate | Run ECS/EKS tasks without managing worker servers | Container/workload configuration and scaling rules |
| Simplified application platform | Elastic Beanstalk | Deploy application versions into managed environment patterns | Application and environment choices |

EC2 instance families trade compute, memory, storage, accelerators, and general-purpose balance. Auto Scaling changes capacity according to policy; Elastic Load Balancing distributes supported traffic across healthy targets. Review [EC2 concepts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html), [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), and the [AWS container decision guide](https://docs.aws.amazon.com/decision-guides/latest/containers-on-aws-how-to-choose/containers-on-aws-how-to-choose.html).

### Storage: object, block, and file

| Requirement | Service/type | Key idea |
|---|---|---|
| Durable objects accessed by key/API | Amazon S3 | Buckets, objects, policies, storage classes, lifecycle |
| Disk for an EC2 instance | Amazon EBS | Persistent block volume in an Availability Zone |
| Temporary host-attached disk | EC2 instance store | Data can be lost according to the instance lifecycle |
| Shared Linux file system | Amazon EFS | Managed elastic NFS file service |
| Managed specialized file systems | Amazon FSx family | Windows, Lustre, NetApp ONTAP, or OpenZFS use cases |
| Hybrid storage integration | AWS Storage Gateway | On-premises access patterns integrated with AWS storage |
| Centralized backup policies | AWS Backup | Policy-driven backup across supported services |

S3 storage classes balance access pattern, retrieval behavior, resilience design, and cost. Lifecycle rules move or expire objects; versioning and Object Lock address different protection needs. Use the [AWS storage decision guide](https://docs.aws.amazon.com/decision-guides/latest/storage-on-aws-how-to-choose/aws-storage-how-to-choose.html) to compare current options.

### Databases: choose data model and operating boundary

| Requirement | Typical AWS option | Distinction |
|---|---|---|
| Relational transactions and SQL | Amazon RDS or Aurora | Managed relational engine choices |
| Key-value/document at very large scale | DynamoDB | Managed NoSQL with access-pattern-driven design |
| In-memory cache/data store | ElastiCache | Reduce latency/load; not a relational system of record |
| Data warehouse analytics | Amazon Redshift | Columnar analytical workloads |
| Graph relationships | Amazon Neptune | Graph traversal and relationship use cases |
| Self-managed database requiring OS control | Database on EC2 | Customer owns more patching, resilience, backup, and tuning |

DMS moves or replicates supported data; Schema Conversion Tool helps convert schema/code between engine types. Migration tooling does not remove compatibility, cutover, validation, or rollback work. Compare current categories in the [AWS database decision guide](https://docs.aws.amazon.com/decision-guides/latest/databases-on-aws-how-to-choose/databases-on-aws-how-to-choose.html).

### Networking and content delivery

A VPC is a logically isolated network boundary in one Region. Subnets are Availability Zone scoped. Route tables decide where traffic is directed. Internet gateways connect supported public paths; NAT gateways allow supported outbound internet access from private subnets without accepting unsolicited inbound connections. Security groups are stateful resource-level virtual firewalls; network ACLs are stateless subnet-level controls. Review the [Amazon VPC guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).

| Need | Service |
|---|---|
| DNS registration and routing | Route 53 |
| Content caching at edge locations | CloudFront |
| Private service access without public routing | VPC endpoints / PrivateLink |
| Encrypted network tunnel | Site-to-Site VPN or Client VPN |
| Dedicated private connectivity | Direct Connect |
| Connect many VPCs/on-premises networks through a hub | Transit Gateway |
| Improve global application network path/availability | Global Accelerator |

### AI/ML, analytics, integration, and other categories

| Requirement | Service to recognize | Boundary |
|---|---|---|
| Build/train/deploy ML models | Amazon SageMaker AI | Full ML platform rather than one prebuilt API |
| Build generative AI applications with foundation models | Amazon Bedrock | Managed model access and GenAI capabilities |
| Conversational interface | Amazon Lex | Speech/text conversational bots |
| Query data in S3 with SQL | Amazon Athena | Serverless interactive query |
| Catalog/ETL/data integration | AWS Glue | Data integration and catalog services |
| Streaming-data family | Amazon Kinesis | Streaming rather than queued work dispatch |
| BI dashboards | Amazon QuickSight | Business intelligence and visualization |
| Event routing | Amazon EventBridge | Event bus/rules/pipes for event-driven integration |
| Queue and decoupling | Amazon SQS | Consumers pull buffered messages |
| Pub/sub notifications | Amazon SNS | Publishers fan out messages to subscribers |
| Workflow orchestration | AWS Step Functions | State-machine coordination |
| Email sending | Amazon SES | Application email service |
| Contact center | Amazon Connect | Managed customer-contact capabilities |

The name is less important than the interaction: queue versus topic, event routing versus workflow, dashboard versus query, and model platform versus conversational service.

---

## 4. Billing, Pricing, and Support — 12%

The [Billing, Pricing, and Support domain](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html) combines purchase models, cost tooling, support, and the AWS partner/marketplace ecosystem.

### Compute purchase models

| Model | Commitment/interruption | Use when | Do not confuse with |
|---|---|---|---|
| On-Demand | No long-term commitment | Short, uncertain, or new workloads | Cheapest for every steady workload |
| Savings Plans | Commit to eligible hourly spend for a term | Predictable eligible compute use | A capacity reservation |
| Reserved Instances | Term commitment/discount for eligible patterns | Predictable supported usage | A universal discount for all services |
| Spot Instances | Spare EC2 capacity; interruptible | Fault-tolerant, flexible workloads | Reliable capacity for an uncheckpointed singleton |
| Capacity Reservation | Reserve EC2 capacity in a location | Capacity assurance matters | Automatic discounted pricing |
| Dedicated Instance/Host | Dedicated physical isolation options | Licensing, compliance, or host visibility requires it | Normal shared-tenancy On-Demand |

**VERIFY CURRENT:** Discount rates, commitment terms, service eligibility, free offers, and transfer pricing change. Use current pricing pages and the calculator for actual decisions.

### Estimate, observe, allocate, and govern

| Tool | Time orientation | Best question |
|---|---|---|
| AWS Pricing Calculator | Planned | What might this design cost under explicit assumptions? |
| Cost Explorer | Historical and forecast | Where did cost and usage change? |
| AWS Budgets | Threshold/forecast alerting | When should owners be notified about cost or usage? |
| Cost and Usage Report / Data Exports | Detailed billing data | Which resource/account/tag/usage dimensions drove cost? |
| Cost allocation tags | Attribution metadata | Who or what owns this spend? |
| Compute Optimizer | Recommendation | Is supported compute over- or under-provisioned? |
| Trusted Advisor | Cross-category checks | Which cost, security, resilience, performance, or quota opportunities are visible? |

A budget normally alerts; it does not automatically stop services. Consolidated billing combines billing across organization accounts and can share eligible pricing benefits, while service control policies govern permission ceilings. Review the [AWS Cost Management guide](https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-costmanagement.html).

Data transfer must be evaluated by direction and location. Incoming transfer is often treated differently from outbound, inter-Region, or Availability Zone transfer. Do not generalize a single “data transfer is free” rule.

### Support and trusted resources

AWS provides documentation, whitepapers, Prescriptive Guidance, Knowledge Center articles, re:Post, Support Center cases under eligible plans, Health information, and account teams/solutions architects or Professional Services in appropriate engagements. Compare current entitlements on the [AWS Support plans page](https://aws.amazon.com/premiumsupport/plans/).

- AWS Health describes service/account events relevant to operations.
- Trusted Advisor provides checks and recommendations; feature availability depends on current plan and service.
- AWS Marketplace distributes third-party software/data/services and can centralize procurement and entitlement.
- The AWS Partner Network includes consulting and technology partners; a partner is not the same as AWS Support.
- Trust & Safety handles reports of abuse involving AWS resources; it is not an application help desk.

---

## 5. Integrated decision scenarios

### Scenario A: Seasonal public web application

A retailer needs a public website with unpredictable seasonal traffic, durable images, a transactional order database, low administrative overhead, and spending alerts.

1. Put static assets in S3 and consider CloudFront for edge caching.
2. Choose Lambda/API services or autoscaled compute according to runtime requirements; do not select EC2 merely because it is familiar.
3. Use a managed relational database when orders need relational transactions.
4. Distribute across Availability Zones where the availability requirement justifies it.
5. Use roles and least privilege; keep database secrets outside code.
6. Enable operational and API evidence with CloudWatch and CloudTrail.
7. Estimate with Pricing Calculator; tag ownership and configure a budget.

Failure clue: Auto Scaling can add instances, but a single-AZ database or hard-coded credentials still creates failure/security risk.

### Scenario B: Regulated analytics landing zone

An organization wants to analyze sensitive files while retaining compliance evidence and separating business units.

1. Classify data and choose an allowed Region before deployment.
2. Organize workloads into accounts with governed identity and organization guardrails.
3. Store objects in S3 with access, encryption, lifecycle, and recovery controls matched to policy.
4. Use Glue for catalog/integration and Athena or a warehouse for the query pattern.
5. Use CloudTrail for API evidence, Config for configuration history, CloudWatch for operations, and Artifact for AWS reports.
6. Allocate costs with account structure and approved tags.

Failure clue: AWS compliance reports do not prove that customer bucket policy, retention, identities, or analytical outputs are compliant.

### Scenario C: Branch-system migration

A company has a lightly used branch application on aging servers, a supported commercial database, and limited operations staff.

1. Discover dependency, latency, identity, licensing, and data requirements.
2. Compare rehost with EC2 against replatforming to a managed database/application service.
3. Use VPN for rapid encrypted connectivity or Direct Connect when dedicated connectivity requirements justify it.
4. Plan validation, cutover, rollback, monitoring, backups, and owner training.
5. Compare total operating cost, not just instance price.

Failure clue: Rehosting without right-sizing or operational redesign can reproduce on-premises waste and manual recovery in AWS.

---

## 6. Hands-on labs

Use a sandbox or an account approved for learning. Configure a budget before creating resources, avoid production data, and delete chargeable resources when finished. AWS interfaces, prices, and free offers change; verify them at the time of each lab.

### Lab 1: Secure the learning account and cost boundary

Review root-user protection, MFA, alternate contacts, role-based access, billing visibility, and a small budget alert. Record which tasks genuinely require root. Evidence: a redacted checklist and budget configuration—not credentials or account identifiers.

### Lab 2: Map a resilient regional design

Choose a Region and inspect its Availability Zones and service availability. Draw a two-AZ web design and a multi-Region disaster-recovery extension. Label which failure each layer handles and what replication/recovery still needs testing.

### Lab 3: Compare EC2 and Lambda responsibility

Launch a disposable EC2 workload and minimal Lambda function, or use guided labs. Compare provisioning, patching boundary, scaling, logs, identity, pricing unit, and cleanup. Do not conclude one is universally cheaper.

### Lab 4: Exercise S3 lifecycle and recovery controls

Create a test bucket, block unintended public access, upload synthetic files, inspect encryption/versioning choices, and create a lifecycle rule. Explain how lifecycle, storage class, versioning, replication, Object Lock, and AWS Backup differ. Delete test resources according to their controls.

### Lab 5: Trace identity and API evidence

Use a limited role for an allowed and denied read-only action. Inspect CloudTrail event history and explain principal, action, resource, time, source, result, and explicit-deny boundaries. Never weaken an organization policy merely to make the lab pass.

### Lab 6: Build a VPC decision diagram

Draw a VPC with public/private subnets across two Availability Zones, route tables, internet gateway, NAT path, security groups, and network ACLs. For a database, show why “private subnet” is insufficient without routes, access controls, credentials, and service configuration.

### Lab 7: Estimate and attribute cost

Use AWS Pricing Calculator for the seasonal-web scenario. Vary instance model, storage class, transfer, and database assumptions. Define tags for owner, environment, application, and cost center. State which tags support allocation and which governance mechanism ensures they exist.

### Lab 8: Create a support and incident evidence map

For an AWS disruption, vulnerable package, suspicious API call, high bill, and abusive external workload, choose the first evidence/resource: Health, Inspector, CloudTrail/GuardDuty, Cost Explorer/Support, or Trust & Safety. Record escalation ownership and a second verification source.

---

## 7. Knowledge checks and distinctions

1. A workload runs on EC2. Who patches the guest OS, and how does that change for Lambda?
2. Why do two instances in one Availability Zone not address an AZ failure?
3. When would multiple Regions be justified even if multi-AZ deployment exists?
4. Why is elasticity not identical to high availability?
5. Which Well-Architected pillars trade off when adding a warm DR Region?
6. Why might replatforming reduce operations more than rehosting?
7. A developer embeds an access key in private code. Which design is stronger?
8. Why does an SCP not grant an administrator role permission?
9. Which evidence belongs in CloudTrail versus CloudWatch versus Config?
10. Why does an Artifact report not prove workload compliance?
11. Choose Shield versus WAF for DDoS protection versus HTTP filtering.
12. Choose Secrets Manager versus KMS for a database password versus encryption key.
13. Why might RDS reduce responsibility without eliminating security work?
14. Choose EC2, Lambda, ECS/EKS, or Fargate for four control requirements.
15. Choose S3, EBS, instance store, EFS, or FSx from access patterns.
16. Why is S3 lifecycle transition not a backup strategy by itself?
17. Choose RDS/Aurora, DynamoDB, ElastiCache, Redshift, or Neptune from a data model.
18. Distinguish a security group from a network ACL.
19. Distinguish CloudFront from Global Accelerator and Route 53.
20. Choose SQS, SNS, EventBridge, or Step Functions for messaging/workflow needs.
21. Choose Athena, Glue, Kinesis, or QuickSight for analytics needs.
22. Why can Spot fit checkpointed batch but not a singleton uncheckpointed database?
23. Distinguish Savings Plans, Reserved Instances, and Capacity Reservations.
24. Why can consolidated billing help without merging account security boundaries?
25. Which question belongs to Pricing Calculator versus Cost Explorer?
26. Why does a budget alarm not guarantee resources stop?
27. What evidence makes cost allocation tags useful?
28. Choose Health, Trusted Advisor, Support Center, re:Post, or Trust & Safety.
29. What must be rechecked before relying on a service in a named Region?
30. Why perform labs when implementation is outside the exam scope?

| Contrast | Remember |
|---|---|
| Agility vs elasticity | Faster change versus demand-responsive capacity |
| Scalability vs high availability | Handle changed load versus remain available through failure |
| Region vs Availability Zone vs edge | Geographic area versus isolated location versus user-near presence |
| Multi-AZ vs multi-Region | Local failure isolation versus geographic recovery/latency/sovereignty |
| Security of vs in the cloud | AWS infrastructure responsibility versus customer workload responsibility |
| Authentication vs authorization | Prove identity versus permit action |
| IAM role vs user | Temporary assumable identity versus long-term account identity |
| CloudTrail vs CloudWatch vs Config | API activity versus telemetry versus configuration history |
| S3 vs EBS vs EFS | Object versus block versus shared file storage |
| RDS vs database on EC2 | Managed platform boundary versus customer-operated stack |
| SQS vs SNS vs EventBridge | Queue/buffer versus pub-sub fanout versus event routing |
| Pricing Calculator vs Cost Explorer | Planned estimate versus actual/forecast analysis |
| Savings Plan vs Capacity Reservation | Discount commitment versus capacity assurance |
| AWS Support vs APN partner | Vendor support entitlement versus solution/services ecosystem |

### Readiness checklist

- [ ] I can explain cloud value without promising automatic savings or reliability.
- [ ] I can apply all six Well-Architected pillars to a simple tradeoff.
- [ ] I can distinguish migration strategies and operational consequences.
- [ ] I can assign responsibilities across EC2, RDS, and Lambda.
- [ ] I can protect root access and choose federation, roles, and least privilege.
- [ ] I can distinguish CloudTrail, CloudWatch, Config, Artifact, GuardDuty, Inspector, Security Hub, Shield, and WAF.
- [ ] I can choose Regions, Availability Zones, and edge services by requirement.
- [ ] I can choose foundational compute, storage, database, networking, integration, AI/ML, and analytics services.
- [ ] I can distinguish pricing models and cost-management tools.
- [ ] I can choose the appropriate AWS support or partner resource.
- [ ] I completed at least three labs and can explain evidence and cleanup.
- [ ] I rechecked the official guide, in-scope services, pricing, Region availability, and every **VERIFY CURRENT** item.

### Primary references

- [Official CLF-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)
- [Cloud Concepts domain](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html)
- [Security and Compliance domain](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html)
- [Cloud Technology and Services domain](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain3.html)
- [Billing, Pricing, and Support domain](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain4.html)
- [CLF-C02 in-scope services](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/clf-02-in-scope-services.html)
- [AWS Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html)
- [AWS shared responsibility model](https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/shared-responsibility-model.html)
- [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [AWS global infrastructure](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html)
- [AWS Cost Management](https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-costmanagement.html)

---

## Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the formats that fit you and use the official blueprint to close only your gaps. Times are approximate consumption time at normal speed; labs, note-taking, assessment review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [AWS CLF-C02 exam page and four-step prep plan](https://aws.amazon.com/certification/certified-cloud-practitioner/) | Public page; Skill Builder account for learning | About 12–20 hours for selected official preparation plus labs | Start with the guide, then use question set, gap learning, labs, and official practice exam; some components require a Skill Builder subscription |
| [AWS Official Practice Question Set catalog](https://explore.skillbuilder.aws/learn/course/external/view/elearning/9153/aws-certification-official-practice-question-sets-english) | Skill Builder account; some prep may require subscription | 30 minutes plus 30–60 minutes review | Public catalog describes a repeatable 20-question CLF-C02 set with explanations; use the full official practice exam later if included in your plan |
| [AWS Cloud Quest: Cloud Practitioner](https://docs.cloudquest.skillbuilder.aws/coming-soon/index.html) | Free foundational role with Skill Builder account | About 8–15 hours estimated for selected assignments | Game-based reinforcement; use the current assignment list and watch for costs outside guided environments |
| [Pluralsight — AWS Certified Cloud Practitioner CLF-C02](https://www.pluralsight.com/paths/aws-certified-cloud-practitioner-clf-c02) | Subscription/trial; practice availability depends on plan | 18 hours plus six labs and practice review | Current five-course path with labs and listed practice exam; skip sections you can explain |
| [O'Reilly — AWS Certified Cloud Practitioner CLF-C02 Certification Guide, 2nd Edition](https://www.oreilly.com/library/view/aws-certified-cloud/9781835464298/) | Subscription or purchase | 15 hours 1 minute provider reading estimate plus labs | August 2026, 598-page scenario-driven reference; use selectively |
| [Udemy — Ultimate AWS Certified Cloud Practitioner CLF-C02 2026](https://www.udemy.com/course/aws-certified-cloud-practitioner-new/) | Purchase or subscription | 14 hours 35 minutes plus labs and practice review | Stéphane Maarek course shown updated August 2026 with a full practice exam; inspect previews/current outline |
| [Whizlabs — AWS Certified Cloud Practitioner CLF-C02](https://www.whizlabs.com/aws-certified-cloud-practitioner/) | Paid modules/subscription; trial items vary | 9+ video hours plus 50+ listed labs and practice review | Page shown updated May 2026; use explanations and public docs, never claims of real exam questions |
| [Tutorials Dojo — CLF-C02 video course](https://portal.tutorialsdojo.com/courses/aws-certified-cloud-practitioner-clf-c02-video-course/) | Paid; separate practice product | 11.2+ video hours, 10+ labs, and one practice exam | Current exam-focused course with labs, quizzes, flashcards, and 65-question assessment |
| [Tutorials Dojo — CLF-C02 practice exams](https://portal.tutorialsdojo.com/courses/aws-certified-cloud-practitioner-practice-exams/) | Paid; free sampler separately | About 8–14 hours for diagnostic, timed, review, and targeted modes | Review every rationale against AWS docs and avoid memorizing question banks |
| [freeCodeCamp — AWS Cloud Practitioner 2026 full course](https://www.youtube.com/watch?v=7HKot-brXFE) | Free | About 14 hours estimated from video length; add labs | Andrew Brown/ExamPro 2026 CLF-C02 video; verify services, prices, and interfaces in AWS docs |

No exact current MeasureUp CLF-C02 product was verified during the September 1 review. That absence is not a claim that the vendor will never add one; search the current catalog before purchasing a substitute. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md) for selection criteria and provider notes.
