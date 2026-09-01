---
exam_code: SAA-C03
vendor_id: aws
official_blueprint: https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# SAA-C03 AWS Certified Solutions Architect - Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#saa-c03-coverage-record). The [official SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html) is authoritative.

**Current baseline:** Current four-domain SAA-C03 AWS Certified Solutions Architect - Associate guide; 50 scored plus 15 unscored questions<br>
**Upcoming blueprint change:** None announced on the official exam guide or certification page as of September 1, 2026.<br>
**Important freshness boundary:** AWS can change services without changing the exam code. Treat feature availability, quotas, pricing, instance families, named products, console paths, and learning-product metadata as **VERIFY CURRENT**. The official service list is non-exhaustive; it is a scope aid, not a checklist to memorize.<br>
**Official source:** [AWS Certified Solutions Architect - Associate exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html)

## How to use this guide

SAA-C03 tests architecture judgment. A plausible service is not automatically the best answer: the design must satisfy the stated security, resilience, performance, operational-effort, and cost constraints together. AWS targets candidates with at least one year of hands-on experience designing cloud solutions. No deep coding is required, but you should be able to reason about protocols, data access, failure, scaling, identity, and application behavior.

The certification page lists a 130-minute, 65-question, USD 150 exam delivered online or at Pearson VUE. The detailed guide says 50 questions affect the score, 15 unidentified questions are unscored, question types are multiple choice and multiple response, and the minimum scaled score is 720. Recheck the [live certification page](https://aws.amazon.com/certification/certified-solutions-architect-associate/) before scheduling; delivery, language, price, and policy details are **VERIFY CURRENT**.

Use one consistent decision sequence:

1. Extract hard requirements: users, data, traffic, latency, availability, RTO/RPO, compliance, integration, geography, skills, and budget.
2. Identify the failure and trust boundaries: account, Region, Availability Zone, subnet, identity, service, component, dependency, and data copy.
3. Choose the simplest managed design that meets the requirements; do not add distributed-system complexity without a requirement.
4. Walk the request and data paths end to end, including DNS, edge, network, identity, compute, storage, database, encryption, observability, and recovery.
5. Test tradeoffs and failure modes. State what scales, what fails, what is retried, what is duplicated, and what is restored.
6. Validate cost drivers and operational ownership rather than selecting a service from one attractive feature.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Design Secure Architectures | 30% | Who or what may reach each resource and data item, through which trusted path and controls? |
| Design Resilient Architectures | 26% | How does the solution scale, isolate failure, preserve work, and recover to a defined objective? |
| Design High-Performing Architectures | 24% | Which compute, storage, database, network, and ingestion pattern meets the workload shape efficiently? |
| Design Cost-Optimized Architectures | 20% | Which design meets the requirements at the lowest responsible total cost? |

Security has the largest standalone weight, but most scenarios span domains. Build architecture comparisons around requirements and constraints rather than isolated service definitions.

---

## 1. Design Secure Architectures — 30%

The official [Domain 1 page](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain1.html) covers secure access, secure workloads and applications, and data-security controls.

### Design identity before permissions

Start with workforce, workload, customer, and service identities. Prefer temporary credentials and roles over long-lived access keys. Use IAM Identity Center and federation for workforce access where appropriate; use roles for AWS workloads and cross-account access; use Cognito when customer/application identity fits. Protect the root user, require MFA, and centralize account governance.

Authorization is evaluated across identity policies, resource policies, permissions boundaries, session policies, service control policies, resource control policies where applicable, and explicit denies. An SCP limits the maximum permissions in member accounts; it does not grant a permission. A role trust policy controls who can assume the role; its permissions policies control what an assumed session may do. Review the [IAM policy-evaluation model](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) until you can predict an allow or deny from the complete policy set.

For multi-account design, separate workloads and environments to contain blast radius, billing, quotas, and administration. AWS Organizations groups accounts and applies governance; Control Tower helps establish and govern a landing zone. Cross-account access should identify trusted principals, permitted actions/resources, conditions, session duration, external ID where relevant, and audit evidence. Avoid duplicating permanent IAM users across accounts.

**Related item:** Authentication proves or establishes an identity; authorization decides what that identity may do. Federation changes how a session is obtained, not the need for least privilege.

### Build defense in depth around the request path

Map traffic from client to endpoint to application to data:

- Public workloads commonly use Route 53, CloudFront, WAF/Shield, an internet-facing load balancer or API Gateway, private compute, and protected data stores. Not every layer is required; select from protocol, caching, threat, latency, and availability needs.
- Public subnets have a route to an internet gateway; a resource is not public merely because its subnet is. It also needs a public address or public-facing endpoint and controls permitting traffic.
- Private workloads can reach supported AWS services through gateway or interface VPC endpoints, avoiding a public internet path. Endpoint policy, private DNS, security groups, IAM/resource policy, and KMS policy can all matter.
- NAT gateways provide outbound IPv4 translation for private resources; they do not accept unsolicited inbound sessions. Consider zonal placement, routes, availability, data-processing charges, and alternative endpoints.
- Security groups are stateful resource-level controls; network ACLs are stateless subnet-level controls. Route tables select paths but do not grant application authorization.

Use WAF for supported web-request filtering, Shield for DDoS protection tiers, Network Firewall for managed VPC network filtering, and security groups/NACLs for network boundaries. GuardDuty detects suspicious activity; Inspector assesses supported workload vulnerabilities and exposure; Macie helps discover and protect sensitive S3 data; Security Hub aggregates and normalizes findings. A detection service does not automatically prevent or remediate every event.

Store secrets in Secrets Manager or Parameter Store according to rotation, integration, sensitivity, hierarchy, and cost requirements. Do not put credentials in AMIs, container images, code, user data, environment files, or public repositories. Grant the workload identity access at runtime and record use.

### Protect data throughout its lifecycle

Classify data, identify owner and residency/retention obligations, and control create, read, write, share, replicate, archive, restore, and delete operations. Distinguish:

- encryption at rest from TLS in transit;
- service-owned or AWS-managed keys from customer-managed KMS keys;
- a KMS key policy from IAM permission and grants;
- encryption from access control, immutability, backup, and deletion protection;
- durability from availability and recoverability.

Customer-managed KMS keys add control over policy, rotation options, grants, disablement, deletion scheduling, and audit, but also add cost and the risk of making data unavailable. Cross-account and cross-Region designs must ensure that recovery principals can use the correct key. Envelope encryption protects data with a data key and protects that key under a KMS key. ACM manages supported public/private certificate workflows; confirm service integration and renewal conditions.

S3 design can combine Block Public Access, bucket/IAM policies, access points, encryption, versioning, lifecycle, replication, Object Lock, logging, and ownership controls. A presigned URL delegates time-limited access under the signer’s effective permissions; it is not a public bucket. For databases and storage, verify encryption behavior for snapshots, replicas, backups, copies, and restored resources.

**Related item:** Least privilege is a lifecycle, not a one-time small policy. Start narrow, observe legitimate use, refine with access analysis, review exceptions, and remove unused access.

---

## 2. Design Resilient Architectures — 26%

The official [Domain 2 page](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain2.html) covers scalable/loosely coupled and highly available or fault-tolerant architectures. Use the [Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) to connect foundations, architecture, change, and failure management.

### Separate state and decouple work

Stateless compute can be replaced or scaled horizontally because durable session and business state live elsewhere. Do not mistake an EC2 instance for stateless merely because an Auto Scaling group launches it. Externalize session state, durable files, work progress, and configuration as requirements allow.

Decoupling prevents one component’s speed or failure from immediately controlling another:

- SQS buffers point-to-point work. Standard queues prioritize throughput and at-least-once delivery; FIFO queues add ordered message groups and deduplication constraints. Consumers need visibility-timeout, retry, idempotency, poison-message, dead-letter, scaling, and backlog-age design.
- SNS publishes to multiple subscribers. EventBridge routes events by pattern and can transform or connect many AWS/SaaS targets. Choose from event contract, ordering, throughput, filtering, replay/archive needs, subscriber count, and integrations.
- Kinesis Data Streams fits ordered high-throughput streaming where consumers process shard-partitioned records and replay within retention. Amazon MSK fits managed Apache Kafka compatibility and ecosystem needs.
- Step Functions coordinates multi-step workflows with state, retries, branching, timeout, and error handling. It does not replace every message bus or high-throughput stream.

Assume events can be duplicated, delayed, retried, or delivered out of order unless the exact service contract proves otherwise. Make consumers idempotent using business keys, conditional writes, deduplication, and explicit state transitions. Set a queue visibility timeout long enough for normal processing and extend it carefully for variable work; an expired in-flight message can be delivered again.

**Related item:** A dead-letter queue isolates repeatedly failed messages; it does not explain, repair, replay safely, or guarantee retention. Own the redrive and reconciliation process.

### Scale the constrained layer

Elastic Load Balancing distributes traffic to healthy targets; EC2 Auto Scaling adjusts instance count. Choose target tracking for a proportional load signal, step scaling for threshold bands, scheduled scaling for known events, and predictive options only when history supports forecast. Include warmup, cooldown, health-check grace, minimum/maximum capacity, subnet IP space, quotas, and downstream capacity.

Serverless and managed services remove server-capacity tasks but retain concurrency, quotas, throttling, timeout, payload, connection, cold-start, partition, and downstream limits. Protect a database from a sudden Lambda concurrency burst with reserved concurrency, queues, connection management such as RDS Proxy, or an architecture suited to the workload.

Caching reduces repeated latency and origin load but introduces freshness and consistency decisions. CloudFront caches at edge locations; ElastiCache provides application data caching; DynamoDB Accelerator is a DynamoDB-compatible in-memory cache for suitable access patterns. Define the cache key, TTL, invalidation, miss behavior, failure mode, encryption, and sensitive-data rules.

### Design for defined failures

Availability Zones are isolated locations within a Region. A Multi-AZ architecture must distribute every critical layer and have routing, capacity, data, and automation that work after a zone failure. An Application Load Balancer across subnets and an Auto Scaling group across zones help only if targets are healthy and dependencies are also resilient.

For relational databases, distinguish:

- RDS Multi-AZ deployment or Aurora replicas/failover for availability;
- read replicas for read scaling and possible promotion, with engine/topology-specific lag and failover behavior;
- automated backups and point-in-time recovery for recovery points;
- cross-Region replicas, snapshots, or global patterns for regional recovery needs.

DynamoDB offers managed partitioning and availability, with on-demand/provisioned capacity and global tables for multi-Region use cases. Understand partition-key distribution, hot keys, read consistency, conditional writes, transactions, indexes, TTL, streams, backup/PITR, and global conflict semantics at the decision level.

Route 53 routing policies solve different traffic goals: simple, weighted, latency, failover, geolocation, geoproximity, and multivalue. Health checks, record type, alias behavior, TTL, resolver/client caching, and endpoint health affect observed failover. Global Accelerator provides static anycast IP entry and health-aware regional routing for TCP/UDP; CloudFront adds CDN caching and edge processing for supported workloads.

### Make recovery measurable

RPO is the maximum acceptable data-loss interval; RTO is the maximum acceptable restoration time. Turn them into replication/backup frequency, architecture, protected artifacts and keys, runbooks, staff roles, tests, and budget.

| Strategy | Readiness | Relative cost | Main proof required |
|---|---|---:|---|
| Backup and restore | Rebuild and restore after event | Lowest | Protected usable backups, current IaC, dependency map, measured restore |
| Pilot light | Critical data/core active | Low–medium | Automated scale-out and frequent end-to-end tests |
| Warm standby | Reduced functional copy active | Medium–high | Replication, traffic shift, capacity expansion, consistency |
| Multi-site active/active | Multiple sites serve | Highest | Conflict model, isolation, routing, observability, capacity, game days |

Backups are only useful if they are complete, retained, decryptable, protected from the same failure, and restored within the objective. Test an application recovery, not merely a database restore. Include DNS, certificates, secrets, keys, identities, networks, images, dependencies, quotas, and external integrations.

**Related item:** High availability reduces interruption during expected component failure; disaster recovery restores after a larger event. Neither automatically supplies data correctness or business continuity.

---

## 3. Design High-Performing Architectures — 24%

The official [Domain 3 page](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain3.html) covers high-performing storage, compute, databases, networking, and ingestion/transformation. Performance is workload-specific: define latency percentile, throughput, concurrency, data volume, access pattern, growth, consistency, and recovery before choosing.

### Match compute to execution shape

| Option | Strong fit | Architecture responsibilities |
|---|---|---|
| EC2 | OS/runtime control, sustained or specialized workloads | Image, patching, scaling, placement, storage, networking, recovery |
| ECS/Fargate | Containerized services/tasks; less orchestration overhead with Fargate | Image, task/service design, scaling, networking, observability |
| EKS | Kubernetes API/ecosystem is a requirement | Cluster/workload operations, upgrades, add-ons, networking, scaling |
| Lambda | Event-driven, short-lived, bursty functions | Timeout, memory/CPU, concurrency, retries, idempotency, packaging, downstream limits |
| Batch | Queued batch jobs with managed scheduling/capacity | Job definition, dependency, retry, compute environment, data movement |

For EC2, compare instance family/generation, architecture, vCPU/memory, local or EBS storage, network/EBS bandwidth, accelerators, licensing, placement, and purchase model. Vertical scaling changes size; horizontal scaling adds units and generally needs distributed/stateless design. Placement groups trade placement behavior for latency, throughput, or failure-spread goals.

For containers, Fargate trades host management for task-level constraints and pricing; EC2 capacity offers host control and potentially different economics. ECS and EKS are orchestration choices, not substitutes for application design. For Lambda, memory also affects CPU allocation; measure duration and end-to-end latency rather than minimizing memory blindly.

### Choose storage from access semantics

- **S3** is object storage for keys/objects accessed through APIs. It is not a block device or general POSIX file system. Select storage class and lifecycle from access frequency, retrieval time/cost, minimum duration/size, resilience, and retention. Multipart upload and Transfer Acceleration help specific transfer patterns; measure benefit.
- **EBS** provides block volumes for EC2. Compare SSD/HDD volume types, IOPS/throughput, latency, size, durability, multi-attach constraints, snapshots, encryption, and instance bandwidth. The instance can be the bottleneck even when a volume is provisioned higher.
- **EFS** provides managed elastic NFS file storage for shared Linux-oriented access. Consider performance/throughput modes, access points, lifecycle/storage classes, mount targets, and cross-AZ traffic.
- **FSx** families serve workload-specific file systems such as Windows, Lustre, NetApp ONTAP, and OpenZFS. Select from protocol, semantics, performance profile, integration, administration, and cost—not from the generic word “file.”
- **Storage Gateway, DataSync, Transfer Family, and Snow Family** solve different hybrid transfer/access, protocol, migration, and offline-volume needs. Identify direction, size, change rate, network, deadline, protocol, and continuing-access requirement.

### Choose a database from the data model and access path

Start with relationship/transaction requirements, query shapes, indexes, consistency, scale, latency, availability, operational ownership, and portability.

| Need | Likely family | Important discriminator |
|---|---|---|
| Relational transactions and SQL | RDS or Aurora | Engine compatibility, failover, replicas, connections, I/O and scaling |
| Key-value/document at massive managed scale | DynamoDB | Partition/access-key design, capacity, indexes, consistency, hot keys |
| In-memory cache | ElastiCache or MemoryDB according to durability/compatibility needs | Data purpose, persistence, topology, eviction and failover |
| Data warehouse/analytics SQL | Redshift | Columnar analytical workload, distribution, ingestion, concurrency |
| Search/log analytics | OpenSearch Service | Index/search model, shard design, ingestion, retention |
| Graph relationships | Neptune | Traversal/graph query requirement |
| Document API/model | DocumentDB where compatibility fits | Compatibility boundary, query pattern, scaling, migration |
| Time series | Timestream | Time-oriented ingestion, retention, query pattern |

Aurora is not simply “always faster RDS.” Verify engine compatibility, I/O pattern, topology, failover, serverless/provisioned behavior, migration, and cost. Read replicas do not replace caching or query/index optimization. RDS Proxy manages suitable connection pools and failover behavior; it does not repair inefficient SQL.

### Design the network and data path

Use the [Amazon VPC guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) for component behavior. Choose CIDR ranges with growth and connectivity in mind; route by longest-prefix match; distinguish internet, NAT, transit gateway, peering, PrivateLink/endpoints, VPN, and Direct Connect use cases.

VPC peering is non-transitive. Transit Gateway provides hub-and-spoke connectivity and route-domain options. PrivateLink publishes supported services privately without general network transitivity. Site-to-Site VPN uses encrypted internet paths; Direct Connect provides dedicated connectivity but encryption and resilient connections require deliberate design. Hybrid designs need return routes, DNS resolution, BGP/static routing, failure detection, bandwidth, latency, and redundant facilities/devices/paths as required.

Select an Application Load Balancer for HTTP/HTTPS layer-7 routing, Network Load Balancer for very high-performance layer-4 TCP/UDP/TLS and static-IP-related needs, and Gateway Load Balancer for supported virtual network appliances. Confirm cross-zone behavior, health checks, session handling, TLS, source IP, target type, and cost.

For data ingestion, compare batch versus streaming, push versus pull, ordering, fan-out, replay, schema, transformation, delivery guarantee, peak throughput, backpressure, retention, destination, and operations. Kinesis, MSK, Firehose, SQS, EventBridge, Glue, DMS, DataSync, and transfer services overlap only superficially.

**Related item:** Performance efficiency is not maximum provisioned capacity. It is meeting measurable requirements while adapting resources and avoiding unnecessary work.

---

## 4. Design Cost-Optimized Architectures — 20%

The official [Domain 4 page](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain4.html) covers cost-optimized storage, compute, databases, and networking. Use the [Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) to connect financial ownership, demand, resource use, supply, and long-term optimization.

### Model total cost, not one price line

Estimate usage by environment and workload period. Include compute time, storage capacity and class, requests/operations, IOPS/throughput, data transfer, NAT/endpoints/transit/load balancing, backups/snapshots/logs, support/licensing, idle failover capacity, and operational labor. Pricing and free-tier terms are **VERIFY CURRENT**; use the [AWS Pricing Calculator](https://calculator.aws/) for a current estimate, then compare with measured bills and Cost Explorer data.

Tag and account-separate costs according to ownership. Budgets notify against thresholds or forecasts; they do not automatically make an architecture efficient. Cost Explorer analyzes cost and usage; Cost and Usage Reports provide detailed records; Cost Anomaly Detection flags unusual patterns; Compute Optimizer and rightsizing recommendations provide evidence to review, not commands to apply blindly.

### Match commitment and interruption tolerance

- On-Demand capacity provides flexibility without a long commitment.
- Savings Plans trade a usage commitment for discounts under current plan rules. Compute and EC2 Instance Savings Plans differ in flexibility.
- Reserved Instances remain relevant for supported services and EC2-specific attributes/benefits; do not treat every reservation as a capacity guarantee.
- Spot uses spare capacity at steep discounts but can be interrupted. Use diversified capacity, checkpointing, queues, retries, and fault-tolerant workers.
- Dedicated Hosts/Instances address isolation, compliance, or licensing cases and usually cost more.

Right-size from CPU, memory, network, storage, accelerator, latency, and peak/seasonal measurements. Schedule nonproduction shutdown, remove idle resources, modernize where benefit exceeds migration cost, and use autoscaling. Graviton or newer generations can improve price/performance only after compatibility and workload validation.

### Find hidden storage and network costs

Apply S3 lifecycle only after modeling object age, access distribution, minimum storage duration, retrieval fees/time, transitions, request volume, replication, and deletion requirements. Intelligent-Tiering helps uncertain/changing access patterns but has monitoring/automation charges and tier behavior to understand. Delete unattached volumes, obsolete snapshots, old AMIs, incomplete multipart uploads, expired logs, and redundant copies according to policy.

Database cost includes instance/capacity, storage, I/O, backup, replicas, data transfer, licensing, proxy/cache, and operations. Consolidation can reduce cost but increase blast radius and noisy-neighbor risk. Serverless can fit variable or intermittent workloads; provisioned resources and commitments can fit stable utilization. Select only after workload modeling.

Network cost surprises often come from internet egress, NAT processing, cross-AZ traffic, cross-Region replication, transit gateway processing, load balancers, interface endpoints, inspection hops, and chatty architectures. A gateway endpoint for S3/DynamoDB can avoid NAT processing for supported traffic; interface endpoints add hourly and data-processing charges but may be justified by security and path requirements. Place tightly coupled components intentionally without destroying failure isolation.

**Related item:** The cheapest component is not always the cheapest system. A design that misses RTO, leaks data, requires excessive labor, or cannot scale transfers cost into risk and operations.

---

## Integrated scenarios

### Scenario 1: Public retail checkout

A global retailer needs low-latency browsing, a relational checkout, burst handling, and no lost orders. Put static/cacheable content behind CloudFront, protect supported HTTP requests with WAF, distribute dynamic traffic to healthy Multi-AZ compute, and keep application tiers private. Use least-privilege roles and managed secrets. Isolate checkout submission from fulfillment with a durable queue and idempotency key; alarm on queue age, failures, latency, and database saturation. Select Multi-AZ relational availability, backup/PITR, and read scaling from transaction and RTO/RPO needs. Load-test failover and bursts, then model CDN, NAT, cross-AZ, database I/O, and idle capacity costs.

### Scenario 2: Regulated hybrid document platform

An enterprise must ingest private on-premises documents, retain immutable records, search metadata, and recover regionally. Classify data and map residency. Use redundant VPN or Direct Connect design according to bandwidth/SLA needs, private DNS, endpoints, scoped roles, KMS keys with tested recovery access, and S3 controls including versioning/retention/Object Lock where governance requires. Choose DataSync, Transfer Family, or application/API ingestion from protocol and change rate. Index only permitted metadata/content, separate search authorization from storage access, replicate/copy according to RPO, and rehearse an application-level recovery with keys, identity, network, certificates, and audit evidence.

### Scenario 3: Spiky media-processing pipeline

Uploads arrive unpredictably and each job creates thumbnails and metadata. Store originals durably in S3, emit work to a queue, and use Lambda, containers, or Batch based on runtime, package, accelerator, duration, concurrency, and cost. Make workers idempotent, keep status in an appropriate data store, isolate poison jobs in a DLQ, and use reserved concurrency or queue-based scaling to protect dependencies. Apply lifecycle to originals/derivatives from retention and retrieval needs. Test duplicates, partial output, retry, a zone failure, backlog recovery, and a tenfold spike. Compare serverless per-use cost with provisioned/container capacity at steady state.

---

## Practice labs

Use an AWS Builder Lab, organization-approved sandbox, or disposable personal training account. Set a budget/alarm, avoid production data, use least privilege, record resources, and remove billable resources after validation. Current prices and free-tier coverage are **VERIFY CURRENT**.

### Lab 1: Requirement-to-architecture decision record — 60–90 minutes

Choose a small workload and write user, data, traffic, latency, availability, RTO/RPO, security, integration, operational, and cost requirements. Compare two designs across every dimension. Record assumptions, decision, rejected alternative, failure modes, and validation evidence.

### Lab 2: Multi-account IAM reasoning — 90–150 minutes

In policy simulator/sandbox or with supplied JSON, model a cross-account role, trust policy, identity/resource policy, permissions boundary, condition, KMS policy, and an organization-level explicit deny. Predict each outcome before testing. Remove all long-lived credentials.

### Lab 3: Secure three-tier request path — 120–210 minutes

Deploy a minimal two-AZ VPC from IaC or use a guided lab. Place load-balancer and private application targets appropriately, create least-privilege security groups, add a private service endpoint, enable relevant logs, and trace DNS-to-data flow. Break route, security, health, and identity layers one at a time; restore and clean up.

### Lab 4: Queue resilience and idempotency — 120–180 minutes

Connect a producer, SQS queue, DLQ, and disposable consumer. Test duplicate delivery, visibility-timeout expiry, poison message, retry, backlog scaling, and safe redrive. Prove that a business operation happens once even when delivery repeats.

### Lab 5: Storage and database decision lab — 90–150 minutes

Given five workload cards, choose S3/EBS/EFS/FSx and RDS/Aurora/DynamoDB/cache/analytics/search options. Define access pattern, consistency, latency, availability, backup, encryption, scale, and cost. Validate at least two choices with a small benchmark or guided lab.

### Lab 6: Multi-AZ failure and recovery drill — 150–240 minutes

Use a disposable load-balanced workload and supported data tier. Simulate a target/AZ-layer failure, observe health/routing, and measure service impact. Restore a backup or point in time to a new target, validate application data, and compare achieved RTO/RPO with the requirement.

### Lab 7: Performance and cost experiment — 120–180 minutes

Run the same representative workload against two compute/storage/cache configurations. Capture p50/p95 latency, throughput, error rate, utilization, scale time, and estimated cost. Explain which requirement changes would reverse the decision. Remove resources.

### Lab 8: Integrated architecture review — 120–180 minutes

Draw one end-to-end scenario with trust, network, failure, data, scaling, observability, and cost boundaries. Have a peer introduce three changed requirements. Revise the architecture, identify new failure/cost modes, and produce a short Well-Architected improvement backlog with evidence and owners.

---

## Knowledge checks

1. First architecture step? **Extract hard requirements and constraints before choosing services.**
2. Does an SCP grant access? **No; it limits maximum available permissions in affected accounts.**
3. Role trust policy versus permissions policy? **Trust controls who may assume; permissions control what the assumed session may do.**
4. What wins policy evaluation? **An applicable explicit deny.**
5. Why prefer roles to access keys? **Roles provide scoped temporary credentials and reduce long-lived-secret risk.**
6. Public subnet means public instance? **No; route, address/endpoint, and security controls must also permit connectivity.**
7. Security group versus NACL? **Stateful resource control versus stateless subnet control.**
8. NAT gateway purpose? **Outbound IPv4 translation for private resources, not unsolicited inbound publishing.**
9. Endpoint policy enough for access? **No; identity, resource, key, and other applicable policies still matter.**
10. Encryption versus authorization? **Encryption protects data cryptographically; authorization controls permitted actions. Both are needed.**
11. Why can a customer-managed key increase risk? **Misconfigured, disabled, deleted, or unavailable key access can make data unusable.**
12. Presigned S3 URL meaning? **Time-limited delegated access using the signer’s effective permissions, not a public bucket.**
13. Stateless compute requirement? **Durable sessions, files, progress, and configuration must not depend on one replaceable instance.**
14. SQS versus SNS? **Queue buffered work to consumers versus publish/subscribe fan-out.**
15. Standard SQS delivery assumption? **At-least-once; consumers must tolerate duplicates.**
16. What does a DLQ solve? **It isolates repeatedly failed messages; investigation, repair, and safe redrive remain your job.**
17. Why scale on queue age? **It represents customer delay better than worker CPU for many backlog workloads.**
18. RDS Multi-AZ versus read replica? **Availability/failover versus primarily read scaling, with topology-specific recovery options.**
19. RPO versus RTO? **Maximum acceptable data loss versus maximum acceptable restoration time.**
20. Does a backup prove recovery? **No; restore data, dependencies, keys, and application within measured objectives.**
21. Route 53 failover delay factor? **TTL plus resolver/client caching and health-evaluation behavior.**
22. CloudFront versus Global Accelerator? **CDN caching/edge features versus global TCP/UDP traffic routing with static anycast IPs.**
23. EC2 versus Lambda decision? **Control/runtime/workload duration and shape versus event-driven managed execution constraints.**
24. Fargate versus ECS? **Fargate is a serverless compute capacity option; ECS is a container orchestrator that can use it.**
25. EBS versus EFS? **Block storage attached to compute versus shared managed NFS file storage.**
26. S3 a file system? **No; it is object storage with API/object semantics.**
27. Volume IOPS higher than instance capability? **The instance path can cap observed performance.**
28. Aurora always the best relational option? **No; choose from compatibility, workload, topology, operation, migration, and cost.**
29. DynamoDB hot partition cause? **Poorly distributed partition-key access can concentrate traffic.**
30. Does RDS Proxy fix inefficient SQL? **No; it manages supported connection patterns and failover behavior.**
31. VPC peering transitive? **No.**
32. PrivateLink versus Transit Gateway? **Private service exposure without general transitivity versus routed network connectivity among attachments.**
33. VPN versus Direct Connect? **Encrypted internet connectivity versus dedicated connectivity; resilience/encryption still require design.**
34. ALB versus NLB? **Layer-7 HTTP routing versus high-performance layer-4 TCP/UDP/TLS use cases.**
35. Batch versus streaming first question? **Required latency and whether records must be processed continuously or in bounded sets.**
36. Savings Plan core tradeoff? **Lower eligible usage cost in exchange for a time-based spend commitment under current rules.**
37. Spot requirement? **Design for interruption with diversification, checkpointing, queues, retries, or disposable work.**
38. S3 lifecycle risk? **Transitions can add request, retrieval, duration, and latency costs that outweigh storage savings.**
39. Common hidden network costs? **NAT, cross-AZ/Region transfer, internet egress, transit, load balancers, endpoints, and inspection.**
40. Cheapest component equals cheapest architecture? **No; include reliability, security, performance, operations, migration, and failure cost.**
41. What makes a scenario answer “best”? **It meets every explicit requirement with the simplest justified tradeoffs, not merely a valid service.**
42. Why benchmark? **Service labels and averages cannot prove workload-specific latency, throughput, scale behavior, or cost.**

---

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. Choose one primary explanation route, do substantial hands-on design/failure work, then use legitimate practice results to select remediation. Prefer current SAA-C03 material and validate changing service behavior in first-party documentation.

| Resource | Access | Estimated time |
|---|---|---:|
| Official guide and AWS four-step plan | Public/free-account/subscription mix | 20–35 hours selected study |
| Hands-on architecture and failure practice | Sandbox or subscription | 30–50 hours |
| Pluralsight SAA-C03 path | Paid | 45–65 hours selected; 97-hour full catalog |
| O'Reilly/Pearson SAA-C03 Cert Guide | Paid | 19 hours 41 minutes plus labs |
| Udemy/Stéphane Maarek current course | Paid | 27 hours 13 minutes plus labs/review |
| Tutorials Dojo video and practice route | Paid | 24–38 hours estimated |
| Whizlabs course/lab/practice route | Paid | 45–80 hours selected |
| freeCodeCamp/Andrew Brown full course | Public/free | About 50 hours plus gap check/labs |

- **Official route:** [AWS certification page and four-step plan](https://aws.amazon.com/certification/certified-solutions-architect-associate/) plus [SAA-C03 Skill Builder exam prep](https://skillbuilder.aws/category/exam-prep/solutions-architect-associate-SAA-C03) (**about 20–35 hours selected**, plus labs). Use the official question set, domain refresh, Builder Labs/Cloud Quest/Jam/SimuLearn options, and official practice exam according to entitlement.
- **Broad modular route:** [Pluralsight SAA-C03 path](https://www.pluralsight.com/paths/aws-certified-solutions-architect-associate-saa-c03) (**97 listed hours**, 12 courses, six labs, and a practice exam). Choose the modernized domain modules and targeted remediation rather than automatically watching both modern and legacy series.
- **Detailed reference:** [O'Reilly/Pearson SAA-C03 Cert Guide, 2nd Edition](https://www.oreilly.com/library/view/aws-certified-solutions/9780137941483/) (**19 hours 41 minutes / 832 pages**, plus companion practice and labs; June 2023, so verify evolving services).
- **Current long-form course:** [Udemy/Stéphane Maarek SAA-C03](https://www.udemy.com/course/aws-certified-solutions-architect-associate-saa-c03/) (**27 hours 13 minutes plus labs/practice**; shown updated July 2026).
- **Course and practice route:** [Tutorials Dojo SAA-C03 video course](https://portal.tutorialsdojo.com/courses/aws-certified-solutions-architect-associate-exam-video-course/) (**14+ video hours, 10+ listed labs, and one practice exam**) plus its [practice exams](https://portal.tutorialsdojo.com/courses/aws-certified-solutions-architect-associate-practice-exams/) (**about 10–18 hours across diagnostic, timed, review, domain, and topic modes**). The publisher explicitly rejects exam dumps; still verify rationales against current AWS documentation.
- **Large lab/practice bundle:** [Whizlabs SAA-C03](https://www.whizlabs.com/aws-solutions-architect-associate/) (**30+ video hours, 110+ listed labs, and 17 quizzes; plan roughly 45–80 selected hours**, not every item). Inspect live access and counts before purchase.
- **Free long-form alternative:** [freeCodeCamp/Andrew Brown SAA-C03](https://www.youtube.com/watch?v=c3Cn4xYfxJY) (**about 50 hours plus labs**; published 2024). Use it for fundamentals and perform a current-objective/service gap check before relying on it.
- **Practice boundary:** no exact current MeasureUp SAA-C03 product was independently verified on September 1, 2026. Start with AWS’s official assessment route and use third-party banks for diagnosis and rationale review—not recalled-question hunting.

Suggested preparation: an experienced AWS builder may need **60–90 hours**; someone new to architecture may need **100–160 hours**, including prerequisites. Spend roughly one-quarter on structured scope, one-half on architecture/labs/failure drills, and the remainder on scenarios, practice, and targeted remediation.

---

## Source map and freshness notes

The official root and four domain pages define the assessment contract. The certification page defines live delivery, and the [in-scope service list](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html) is a non-exhaustive boundary. AWS service documentation supports current behavior; learning vendors support only their catalog claims.

- **VERIFY CURRENT:** service features, regions, quotas, endpoints, pricing, purchase models, instance families, console flows, free-tier terms, and training metadata.
- **VERIFY CURRENT:** encryption, replication, failover, consistency, backup, routing, cache, and recovery behavior before production use.
- **Stable reasoning pattern:** requirements → trust/failure boundaries → simplest qualifying design → end-to-end path → tradeoff/failure test → cost and operational validation.

This guide uses no recalled exam questions or restricted content. The knowledge checks are original and test published concepts rather than reproducing vendor items.
