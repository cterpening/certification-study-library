---
exam_code: DVA-C02
vendor_id: aws
official_blueprint: https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# DVA-C02 AWS Certified Developer - Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#dva-c02-coverage-record). The [official DVA-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02.html) is authoritative.

**Current baseline:** DVA-C02 version 2.1 skills, four scored domains, and a separately labeled emerging-topic/pretest section<br>
**Upcoming blueprint change:** None announced in the current guide, revisions page, or certification page as of September 1, 2026.<br>
**Important freshness boundary:** Version 2.1 added Amazon Q Developer, EventBridge patterns, third-party resilience, near-real-time Lambda transformation, specialized stores, fine-grained and cross-service authorization, masking/multi-tenancy, AppConfig, event-driven tests, health/readiness, caching, and performance analysis. AWS Copilot and CodeGuru were removed from the in-scope list, although one detailed testing example still names Copilot environments. Current AI-assisted development, AI security, test, CI/CD, error-analysis, and optimization topics are explicitly described by AWS as possible **unscored pretest** content.<br>
**Official source:** [AWS Certified Developer - Associate exam guide](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02.html)

## How to use this guide

DVA-C02 validates the ability to develop, test, deploy, secure, debug, and optimize AWS-hosted applications. The target candidate has at least one year building and maintaining applications with AWS, can program in a high-level language, uses APIs/CLI/SDKs, and works with existing CI/CD pipelines. Architecture design, pipeline design, IAM administration, server administration, and network design are explicitly outside the target role, but a developer must understand enough of each boundary to use existing platforms safely.

The live page lists a 130-minute, 65-question, USD 150 exam. The detailed guide identifies 50 scored and 15 unidentified unscored multiple-choice/multiple-response items and a 720 minimum scaled score. Recheck the [certification page](https://aws.amazon.com/certification/certified-developer-associate/) for current price, languages, delivery, and validity before scheduling.

For every scenario, ask:

1. What is the request/event contract, identity, state, consistency, latency, and failure boundary?
2. Which AWS API, SDK behavior, service integration, or data access pattern fits?
3. How do retries, duplicates, timeouts, ordering, quotas, and partial failures change the code?
4. Where are configuration, secrets, tenant context, and permissions enforced?
5. How is the artifact tested, promoted, deployed, observed, rolled back, and optimized?

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the objective easier to reason about. It is supporting knowledge, not a claim that the item appears verbatim in the official outline.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Development with AWS Services | 32% | How should application code use events, compute, APIs, messages, streams, and stores resiliently? |
| Security | 26% | How are identities, permissions, encryption, secrets, tenants, and sensitive data handled in code? |
| Deployment | 24% | How are artifacts, environments, tests, IaC, strategies, promotion, and rollback implemented? |
| Troubleshooting and Optimization | 18% | Which telemetry isolates a fault or bottleneck, and which change improves it safely? |

---

## 1. Development with AWS Services — 32%

The official [Domain 1 page](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02-domain1.html) covers application patterns, APIs/SDKs, messaging, streams, Lambda, EventBridge, resilience, DynamoDB, caching, and specialized stores.

### Choose the interaction pattern

| Pattern | Use when | Developer obligations |
|---|---|---|
| Synchronous request/response | Caller needs an immediate answer | Validate input, authenticate, bound timeouts, map errors, protect dependencies, make retry semantics clear |
| Queue-based asynchronous work | Work can wait and consumers should be decoupled | Idempotency, visibility timeout, retry/backoff, DLQ/redrive, poison-message handling, backlog monitoring |
| Publish/subscribe fan-out | Multiple independent consumers need the same event | Filter/routing contracts, per-consumer failure isolation, delivery/replay expectations |
| Event bus | Producers publish business/service events without knowing targets | Stable schemas, event source/detail, filtering, archive/replay where used, target permissions and failures |
| Stream | Ordered records and replayable continuous processing matter | Partition key, retention, consumer checkpoint, late/duplicate records, hot partitions, scaling |
| Orchestrated workflow | Central state and step-by-step control are required | Retries, catches, timeouts, compensation, state size, idempotent activities, audit |
| Choreography | Services react independently to events | Loop prevention, ownership, emergent dependencies, traceability, versioned contracts |

Use SQS to buffer and decouple work; standard queues favor scale with at-least-once delivery and best-effort ordering, while FIFO queues add ordering/deduplication semantics within their current constraints. SNS fans messages to subscribers. EventBridge matches and routes events. Step Functions owns workflow state. Kinesis serves ordered, retained streams. An API Gateway API exposes governed HTTP/WebSocket interfaces. These services can be combined, but each additional hop needs an identity, error path, metric, and replay story.

Resilient client code sets connection/request timeouts, retries only appropriate failures, uses exponential backoff with jitter, honors throttling, and avoids retry storms. A circuit breaker stops repeatedly calling a failing dependency and probes recovery. Bulkheads isolate capacity. Idempotency keys let the same logical request be recognized. Do not retry a non-idempotent operation blindly.

AWS SDKs implement signing, serialization, endpoints, credential-provider chains, retries, and pagination, but defaults vary by language/version. Reuse clients/connections when safe, consume paginated APIs fully, and use waiters only for the state they actually observe. Treat service quotas and throttling as normal distributed-system behavior.

**Related item:** “Serverless” removes server management, not application responsibility. You still own data contracts, permissions, concurrency, cost, failure handling, observability, and correctness.

### Develop and tune Lambda functions

Lambda configuration includes runtime, handler, memory, architecture where supported, timeout, ephemeral storage, environment variables, layers/extensions, reserved/provisioned concurrency, event sources, destinations, and VPC networking. Review the current [Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html) rather than memorizing limits.

An execution environment can be reused. Initialize SDK clients and static dependencies outside the handler to reduce repeated setup, but never store request-specific secrets or tenant state in reusable global data. Package only required dependencies. Layers share suitable code, while container images support larger/custom packaging under current limits. Memory also changes available CPU; profile duration and cost rather than assuming the smallest setting is cheapest.

Invocation modes have different error paths:

- synchronous callers receive a response/error and decide whether to retry;
- asynchronous invocation has service-managed retry and destination/DLQ options;
- event source mappings poll streams/queues, batch records, checkpoint progress, and have source-specific retry/partial-batch behavior.

For SQS, align visibility timeout with processing and retries; delete only successfully processed messages. For streams, record ordering and batch checkpoint behavior mean one bad record can impede a shard unless partial-batch/failure handling is designed. Reserved concurrency bounds a function and protects downstream systems; provisioned concurrency reduces cold-start latency for selected workloads. VPC attachment enables private-resource access but requires appropriate subnets, security, routes/endpoints/NAT, IAM, DNS, and connection management.

Near-real-time transformation requires schema validation, poison-record isolation, idempotent output, backpressure awareness, and lag monitoring. A function returning success is not proof that all records produced correct business results.

### Build APIs and event contracts

API Gateway stages, deployments, routes/resources, methods, integrations, transformations, validation, status mapping, throttling, authorizers, custom domains, and logging form an API release boundary. HTTP APIs and REST APIs differ in features and price; select from required capabilities, not recency. Validate at the edge and again at trust boundaries. Return stable error bodies and correlation IDs without exposing internal exceptions.

EventBridge events should carry a stable source, detail type, versioned detail schema, immutable event ID, occurrence time, and business key. Consumers must tolerate added fields, duplicates, delay, and reordering unless stronger guarantees are explicitly implemented. Use the [EventBridge user guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) for current buses, rules, targets, schemas, archives, and pipes.

### Use data stores from access patterns

[DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) models data around known operations. A high-cardinality partition key distributes load; a sort key enables grouped/range queries. A query uses key conditions; a scan reads broadly and is rarely the default for request paths. Global secondary indexes enable different access patterns and carry capacity/storage/consistency implications. Conditional writes and transactions protect invariants; optimistic locking uses a version condition. Eventually consistent reads can be stale; strongly consistent reads apply only where supported and cost/capacity differs.

Serialization must preserve type, precision, timestamps, enums, nulls, and compatibility across versions. Store an explicit schema/version when evolution matters. TTL supports asynchronous expiry and stream-based follow-up patterns, not exact-time deletion.

Use ElastiCache/MemoryDB or application caches when repeated access and latency justify complexity. Define key, value, TTL, invalidation, consistency, stampede protection, failure fallback, and tenant isolation. CloudFront caches HTTP content based on the configured cache key; including or excluding headers, cookies, or query strings changes correctness and hit rate.

Specialized stores exist for distinct access patterns: OpenSearch for search/analytics/vector cases, RDS/Aurora for relational transactions, S3 for objects, Neptune for graphs, and others listed in current scope. The developer role uses an existing design; it still must choose correct API and consistency behavior.

### Use Amazon Q Developer safely

Amazon Q Developer can assist with code, explanation, refactoring, testing, reviews, and related development tasks. Exact features, plans, supported environments, data handling, and release stages are **VERIFY CURRENT**. Treat output as untrusted proposed code: understand it, review dependencies/licenses, test success and failure paths, scan for security issues, check least privilege, and avoid submitting sensitive data contrary to policy.

---

## 2. Security — 26%

The official [Domain 2 page](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02-domain2.html) covers federation, tokens, roles, fine-grained authorization, cross-service authentication, encryption, certificates, secrets, masking, and multi-tenant access.

### Authenticate and authorize deliberately

Authentication answers who; authorization answers what that identity may do. IAM roles supply temporary AWS credentials to workloads through STS. Never embed access keys in code. SDK credential-provider chains can source environment, shared config, container/instance roles, web identity, or other supported providers; understand which provider wins in the deployment environment.

Amazon Cognito user pools provide user directories and token issuance; identity pools exchange supported identities for temporary AWS credentials. OAuth/OIDC bearer tokens have issuer, audience/client, expiry, scopes/claims, signature, and key-rotation considerations. Validate tokens in a trusted component—do not merely base64-decode them. API Gateway/Lambda authorizers or application middleware can enforce access, but business-resource authorization still belongs at the resource/action boundary.

IAM evaluation combines identity/resource policies with boundaries, sessions, organization controls, and explicit deny. Cross-service calls may use the caller identity, a service role, resource policy, or service-linked role. The application must know which principal actually calls the next service.

Fine-grained application authorization should bind the authenticated subject, tenant, resource owner, action, and context. A route like `/tenant/{tenantId}` is not secure because it contains a tenant ID; the code must derive/validate authorized tenant context. Prevent cross-tenant object keys, cache keys, indexes, logs, exports, background jobs, and admin paths.

**Related item:** Authentication is not tenant isolation. A valid user from Tenant A is still an attacker if the application accepts Tenant B’s identifier without an authorization decision.

### Encrypt data with usable key controls

TLS protects data in transit when endpoints/certificate validation are correctly configured. At rest, services can use AWS-owned, AWS-managed, or customer-managed KMS keys depending on service and control needs. Client-side encryption encrypts before data reaches the service and shifts key/envelope/metadata responsibility to the application. Server-side encryption lets the service encrypt after receipt.

KMS commonly uses envelope encryption: a data key encrypts data, and the encrypted data key is stored alongside ciphertext; the KMS key protects the data key. Encryption context can bind cryptographic use and policy conditions but is not secret. Cross-account use requires aligned IAM and key policy/grants plus supported service/region behavior. Rotation does not automatically rewrite old ciphertext. See the [KMS concepts](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) for current behavior.

ACM manages supported public/private certificates for integrated services; AWS Private CA issues private certificates under your PKI controls. For local development SSH keys/certificates, protect private keys and avoid reusing production trust. Know the objective at the level of generation, storage, rotation, distribution, trust, and revocation—not certificate-authority administration.

### Keep sensitive data out of code and telemetry

[Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) stores and retrieves secrets and supports rotation patterns; Systems Manager Parameter Store can hold configuration and secure strings. Cache retrieved secrets only for a bounded time and handle rotation. Environment-variable encryption helps at rest, but decrypted values are available to the function/process; restrict configuration access and never log them.

Classify PII/PHI and other sensitive data before deciding storage, logging, masking, retention, or transmission. Sanitize input to prevent injection and normalize unsafe output. Masking hides part/all of a value for a context; tokenization substitutes a controlled token; hashing is not encryption; redaction removes data from an output. Logs, traces, exceptions, URLs, headers, events, and dead-letter messages are common leakage paths.

For multi-tenancy, compare pooled, siloed, and bridge patterns. Regardless of storage model, propagate verified tenant context, scope every query/key/index, isolate caches and async messages, test negative access, constrain admin operations, and record tenant-aware audits. Encryption per tenant may improve separation but increases key and operational complexity.

---

## 3. Deployment — 24%

The official [Domain 3 page](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02-domain3.html) covers artifacts, configuration, tests, event-driven testing, IaC, environment management, CI/CD use, versioning, strategies, and rollback.

### Build immutable, reproducible artifacts

An artifact should identify source commit, dependency lock/versions, build instructions, architecture/runtime, configuration expectations, SBOM/provenance where required, test results, and checksum/digest. Do not rebuild a different artifact for each environment; promote the same tested artifact and inject controlled configuration.

Lambda zip packages include handler and dependencies with size/runtime constraints. Container-image functions use an image in ECR and an immutable digest should identify the release. SAM packages serverless resources/functions/APIs/events and transforms a template for CloudFormation; consult [AWS SAM concepts](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html). CloudFormation describes stacks, dependencies, outputs, change sets, rollback, and drift.

AppConfig can validate and progressively deploy application configuration independently of code. Separate secrets from non-secret configuration. Define environment, version, validator, deployment strategy, rollback signal, and retrieval/caching behavior. A feature flag needs owner, expiry/removal, default, failure behavior, and observability—not permanent branches everywhere.

### Test contracts and failures

Use unit tests for local logic and mocked boundaries, but do not let mocks invent AWS behavior. Integration tests validate real service contracts, IAM, serialization, retries, timeouts, and configuration. End-to-end tests validate representative user flows in a controlled environment. Contract tests help producers/consumers evolve independently.

Event-driven tests need duplicate, out-of-order, delayed, malformed, oversized, unauthorized, throttled, poison, partial-batch, and replay cases. Assert both state and emitted side effects. Use deterministic event fixtures and unique run IDs. Test DLQ/redrive and prove a retry does not duplicate the business outcome.

Amazon Q Developer may generate tests, but reviewers must verify assertions, independence, edge cases, negative authorization, realistic mocks, and whether a test can fail for the right reason.

### Use an existing pipeline safely

CodePipeline orchestrates stages/actions; CodeBuild runs builds/tests; CodeDeploy deploys to supported compute; ECR stores images; CloudFormation/SAM provisions resources; third-party repositories and actions can participate. CodeCommit is no longer in the DVA-C02 in-scope list—do not center current study on it.

Understand deployment strategies:

| Strategy | Behavior | Main risk/control |
|---|---|---|
| All at once | Replace all capacity quickly | Fast, highest immediate blast radius; needs strong rollback |
| Rolling | Replace batches | Mixed versions and reduced capacity/compatibility |
| Canary | Send a small portion to new version, then expand | Needs representative traffic, alarms, bake time, automated stop |
| Linear | Shift traffic in fixed increments | Slower exposure with measurable checkpoints |
| Blue/green | Create parallel environment and switch traffic | Extra cost/capacity; database/config compatibility remains |

Lambda versions are immutable snapshots of code/config; aliases point to versions and can split traffic. API Gateway stages/deployments expose environment/release boundaries. Container tags are mutable unless policy prevents it; prefer digests for exact promotion. Labels/branches organize source, but the deployable identity must resolve to an immutable artifact.

Rollback is more than shifting traffic. Database/schema changes, messages already emitted, external calls, and cache/config changes may be irreversible. Use expand/contract schemas, backward-compatible events, feature flags, versioned APIs, and compensating actions. Deployment alarms should cover customer and dependency outcomes, not only host health.

**Related item:** Continuous delivery means every change is releasable through automation; continuous deployment releases qualifying changes automatically. Both require controls, and neither means skipping human governance where risk demands it.

---

## 4. Troubleshooting and Optimization — 18%

The official [Domain 4 page](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02-domain4.html) covers debugging, metrics/logs/traces, structured logging, custom metrics, health/readiness, integration faults, concurrency, caching, profiling, and resource optimization.

### Instrument an evidence chain

| Signal | Answers | Developer practice |
|---|---|---|
| Structured log | What application event/state/error occurred? | Emit timestamp, level, service/version, correlation/trace/request ID, safe fields, outcome; never secrets |
| Metric | How much/often and is it breaching a threshold? | Measure rate, errors, duration, saturation/backlog and business outcomes; control cardinality |
| Trace | Where did a distributed request spend time or fail? | Propagate context, annotate useful dimensions, sample intentionally, protect sensitive data |
| Health check | Can this instance serve its intended traffic? | Separate liveness from readiness; test dependencies only when that reflects serving ability |
| Deployment/build log | Why did packaging, permissions, tests, IaC, or rollout fail? | Correlate build/artifact/deployment/environment IDs |
| Audit record | Who changed or called an AWS API? | Use CloudTrail with application evidence; recognize coverage differences |

CloudWatch Logs Insights queries structured fields more reliably than parsing free text. Embedded Metric Format can produce metrics from structured log events, but uncontrolled dimensions create high-cardinality cost/noise. X-Ray and OpenTelemetry-compatible tracing connect service segments and downstream calls under current integrations.

Start root-cause work with expected vs actual, scope, timeline, last known good, and recent change. Follow request ID from edge through function/container, message/event, dependency, data write, and response. Distinguish application exception, IAM/KMS denial, DNS/network path, timeout, throttling/quota, serialization/schema, stale configuration, deployment mismatch, and downstream unavailability. Change one hypothesis at a time and preserve evidence.

### Optimize measured constraints

- **Concurrency:** determine arrival rate, service time, parallelism, quotas, reserved/provisioned settings, event-source scaling, and downstream capacity. More concurrency can amplify a database or API failure.
- **Lambda:** tune memory/CPU and initialization, connection reuse, dependency size, architecture, timeout, batch size/window, concurrency, and ephemeral storage from measured profiles.
- **DynamoDB:** use keyed queries, balanced partitions, suitable capacity mode, efficient items/indexes, batch APIs, conditional writes, caching, and retry/backoff. Avoid scans on latency paths.
- **Messaging:** SNS subscription filter policies reduce irrelevant delivery; batching lowers API calls but changes latency/failure units. Size visibility timeouts and DLQ redrive from measured processing.
- **HTTP/cache:** define cache key from method/path/query/header/cookie/authorization semantics. Excluding a varying value can leak/wrongly share content; including everything destroys hit rate.
- **Application cache:** define invalidation, TTL, consistency, memory/eviction, tenant/key isolation, stampede protection, and fallback.
- **SDK/API:** reuse connections, paginate correctly, batch where supported, bound retries, and profile serialization/network waits.

Optimization is a controlled experiment: baseline a customer-relevant metric and cost, change one constraint, load-test representative traffic, compare tail latency/error/cost, inspect downstream effects, then keep or revert.

### Treat AI-assisted troubleshooting as advisory

The live guide’s emerging topics include AI-generated error explanations and optimization suggestions. Those are possible unscored pretest topics, not an excuse to surrender diagnosis. Provide sanitized evidence, verify the suggested causal chain, test in a safe environment, inspect permissions/dependencies, and preserve human accountability.

---

## Integrated scenarios

### Scenario 1: Resilient order API

API Gateway validates and authenticates a request, then Lambda creates an order with a client-provided idempotency key. DynamoDB uses a conditional write to prevent duplicate creation. The function publishes an order-created event to EventBridge; independent targets enqueue fulfillment and analytics work. Each consumer records event ID, handles duplicates, uses bounded retries, and sends poison work to a DLQ with an owned redrive runbook.

Tenant context comes from validated identity claims and is included in every key/authorization decision—not trusted from the route alone. Logs contain correlation/order/tenant-safe identifiers, never tokens or payment data.

### Scenario 2: Safe serverless release

One immutable SAM artifact and template move from test to production. Unit/contract tests run first, then integration tests exercise real API/event/DynamoDB behavior with a unique run ID. AppConfig holds a disabled feature flag. A Lambda alias shifts a canary share to the new version while alarms watch error rate, duration, throttles, DLQ depth, and order success. A failure shifts traffic back and disables the flag; the schema remains backward compatible.

The rollback plan accounts for events emitted during the canary. The team does not rebuild “the same” code after production approval.

### Scenario 3: Latency and duplicate incident

P99 latency rises and a downstream partner reports duplicates. Trace data shows slow partner calls; logs show SDK retries; metrics show Lambda concurrency growing and partner throttling. The request path lacks idempotency and has excessive timeout/retry settings. Stabilize by bounding concurrency and retries, enabling an appropriate circuit breaker/fallback, and adding idempotency at the business boundary. Verify reduced tail latency and no duplicate outcome under failure injection.

Do not merely increase Lambda timeout or concurrency; that would hold resources longer and intensify pressure on the failing partner.

---

## Hands-on labs

Use a sandbox account, least privilege, budgets, synthetic data, and cleanup. Features, limits, and cost are **VERIFY CURRENT**.

### Lab 1: SDK resilience

Build a small SDK client that paginates, applies bounded retry/backoff, distinguishes throttling from validation errors, and attaches a correlation ID. Inject timeouts and throttles. Deliverable: tests and a retry/idempotency rationale.

### Lab 2: Event-driven order flow

Implement API/event → Lambda → DynamoDB → EventBridge/SQS with synthetic data. Add a conditional idempotent write, consumer deduplication, DLQ, and correlation IDs. Replay events and prove totals stay stable.

### Lab 3: Lambda tuning

Run a CPU- and I/O-mixed function at several memory/concurrency/batch settings. Measure initialization, duration, error, throttling, downstream calls, and estimated cost. Deliverable: evidence-backed configuration, not “smallest memory.”

### Lab 4: Tenant authorization

Create two synthetic tenants and API paths to shared data. Derive tenant context from validated claims, scope keys/queries/cache, and add negative tests for cross-tenant IDs, async messages, and admin paths. Deliverable: authorization matrix and denied evidence.

### Lab 5: Secrets and encryption

Retrieve a rotating test secret through a workload role; encrypt data with KMS and an encryption context; attempt an unauthorized tenant/account context. Ensure logs contain no secret/plaintext. Deliverable: policy/key evaluation and rotation/caching behavior.

### Lab 6: Artifact, IaC, and event tests

Package the app with SAM, pin dependencies, record artifact digest/commit, and deploy to a disposable stage. Test duplicates, malformed events, partial failures, and rollback. Deliverable: provenance, test results, and clean deletion.

### Lab 7: Canary and configuration rollback

Use versions/alias traffic shifting or simulate the exact workflow. Deploy a deliberately slow release behind AppConfig, observe alarms, stop the canary, shift back, and disable the feature. Deliverable: timeline and evidence that data/events remained compatible.

### Lab 8: Observability game day

Inject four failures separately: IAM deny, malformed payload, downstream timeout, and hot/inefficient access. Diagnose with structured logs, metrics, traces, deployment/audit evidence, and request IDs. Deliverable: four evidence chains and one measured optimization.

---

## Original knowledge checks

These prompts are independent and do not reproduce live or vendor questions.

1. When does asynchronous messaging improve resilience, and what new failure states does it add?
2. Why must an SQS consumer be idempotent even if processing usually succeeds once?
3. How should visibility timeout relate to processing duration and retry behavior?
4. When is EventBridge preferable to direct SNS or SQS integration?
5. What is the difference between orchestration and choreography?
6. Why can indiscriminate retries worsen an outage?
7. Which conditions make a circuit breaker useful?
8. Where should an SDK client obtain credentials in Lambda or a container?
9. What can go wrong if code ignores paginated API responses?
10. Why is global request state unsafe in a reused Lambda environment?
11. How do reserved and provisioned concurrency solve different problems?
12. How can one poison stream record block progress, and what must recovery preserve?
13. Why is DynamoDB `Query` generally different from `Scan` for a request path?
14. How does partition-key cardinality affect DynamoDB behavior?
15. When does eventually consistent reading create an application bug?
16. What must a cache key include to prevent cross-user or cross-tenant leakage?
17. Why is generated code from Amazon Q Developer still untrusted input to the review process?
18. What token properties must an API validate beyond signature?
19. Why is a tenant ID in a URL not an authorization decision?
20. Which identity actually calls a downstream AWS service in a cross-service flow?
21. Why can IAM permission still fail when KMS-encrypted data is accessed?
22. What is the difference between client-side and server-side encryption responsibility?
23. Why does KMS rotation not automatically re-encrypt old application ciphertext?
24. When is an environment variable an inadequate secret-management design?
25. How do masking, redaction, tokenization, hashing, and encryption differ?
26. What negative test best detects a multi-tenant data-access defect?
27. Why should the same artifact be promoted across environments?
28. What evidence makes an artifact reproducible and traceable?
29. Why can mocks give false confidence about an AWS integration?
30. Which event-driven failure cases should an automated test cover?
31. How do Lambda versions and aliases support a canary?
32. Why can a successful traffic rollback leave data inconsistent?
33. What compatibility property enables safe blue/green or canary deployment?
34. How do liveness and readiness checks differ?
35. Why are high-cardinality metric dimensions dangerous?
36. Which evidence distinguishes application timeout from IAM denial?
37. Why can increasing concurrency make latency or errors worse?
38. How should a subscription filter improve both cost and correctness?
39. What experiment proves a memory/caching change is an optimization?
40. How should AI-generated troubleshooting advice be verified before action?

---

## Readiness checklist

- [ ] I can map all four scored domains and distinguish the emerging unscored pretest section.
- [ ] I can choose synchronous, queue, fan-out, bus, stream, orchestration, and choreography patterns.
- [ ] I can implement bounded retries, backoff/jitter, circuit breaking, idempotency, and DLQ/redrive.
- [ ] I can configure/test Lambda invocation, events, VPC access, concurrency, packaging, and performance.
- [ ] I can use APIs/SDKs safely, including credentials, pagination, errors, and throttling.
- [ ] I can model DynamoDB keys/indexes/consistency and design safe caches.
- [ ] I can validate tokens, assume roles, evaluate permissions, and enforce resource/tenant authorization.
- [ ] I can apply KMS, certificates, secrets, masking, sanitization, and log-data protection.
- [ ] I can package immutable artifacts, update SAM/CloudFormation, and separate configuration/secrets.
- [ ] I can test event failures and use an existing CI/CD workflow with safe promotion and rollback.
- [ ] I can compare all-at-once, rolling, canary, linear, and blue/green releases.
- [ ] I can correlate structured logs, metrics, traces, health, deployment logs, and audit records.
- [ ] I can optimize concurrency, Lambda, DynamoDB, messages, HTTP/application caches, and SDK use from measurements.
- [ ] I have gap-checked older training against version 2.1 additions/removals and the current emerging-topic section.
- [ ] I reject dumps and recalled/“actual” questions.

---

## Places to learn

This is **not a complete list** and is not meant to be consumed in full. Choose one structured route, build the labs, use official documentation to close version 2.1 and emerging-topic gaps, and add one ethical practice source. Times combine provider-listed duration with labeled library estimates. Access and metadata are **VERIFY CURRENT**.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official guide, domains, service scope, and version 2.1 revisions](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02.html) | Free | 3–5 hours mapping and gap analysis |
| [AWS Skill Builder DVA-C02 exam prep](https://skillbuilder.aws/category/exam-prep/developer-associate-DVA-C02) | Free account plus subscription options | 15–30 hours selected review, practice, labs, pretest and official practice exam; exact entitlement varies |
| [Pluralsight DVA-C02 path](https://www.pluralsight.com/paths/aws-certified-developer-associate-dva-c01) | Subscription/trial terms vary | 34 listed hours, 12 courses, five labs, and practice exam; add version 2.1/emerging-topic gap work |
| [O'Reilly/Sybex AWS Certified Developer Study Guide, 2nd ed.](https://www.oreilly.com/library/view/aws-certified-developer/9781394274802/) | Subscription/book | 20 hours 39 minutes / 800 pages plus labs; January 2025, gap-check current emerging topics |
| [O'Reilly DVA-C02 in-depth course](https://www.oreilly.com/videos/aws-certified-developer/0642572115197/) | Subscription | 3 hours 15 minutes plus 10–20 hours labs; compact June 2025 review, not standalone hands-on depth |
| [Udemy — Neal Davis DVA-C02](https://www.udemy.com/course/aws-certified-developer-associate-exam-training/) | Paid; sales/subscription vary | 17 hours 12 minutes video plus labs/review; updated August 2026 when checked |
| [Udemy — Stéphane Maarek DVA-C02](https://www.udemy.com/course/aws-certified-developer-associate-dva-c01/) | Paid; sales/subscription vary | Plan 20–35 hours with labs/practice; updated August 2026, verify live runtime and new boundaries |
| [Tutorials Dojo DVA-C02 video](https://portal.tutorialsdojo.com/courses/aws-certified-developer-associate-video-course/) | Paid | 11+ video hours, 10+ labs, 14 quizzes and one simulator; add 8–16 hours practice |
| [Tutorials Dojo DVA-C02 practice](https://portal.tutorialsdojo.com/courses/aws-certified-developer-associate-practice-exams/) | Paid | 17 quizzes across randomized, timed, review and domain modes; plan 10–18 hours with rationale review |
| [Whizlabs DVA-C02](https://www.whizlabs.com/aws-developer-associate/) | Paid/free sample | Plan 20–40 hours selectively; exact live video, lab, practice and sandbox counts require page/account verification |

No exact current MeasureUp DVA-C02 product was independently verified. Reject content advertising leaked/recalled/actual items, and do not copy vendor questions into notes. A useful practice assessment explains all options and links current documentation.

### A practical 6–8 week route

- **Week 1:** Official map, one language/SDK, IAM/KMS, HTTP/events, unit testing.
- **Weeks 2–3:** API Gateway, Lambda, SQS/SNS/EventBridge/Kinesis, DynamoDB/cache; Labs 1–3.
- **Week 4:** Cognito/tokens, roles, secrets, encryption, tenants; Labs 4–5.
- **Week 5:** SAM/CloudFormation, artifacts, AppConfig, integration/event tests; Lab 6.
- **Week 6:** strategies, versions/aliases, pipeline use, rollback; Lab 7.
- **Weeks 7–8:** observability game day, measured tuning, practice/remediation, and current emerging-topic review.

---

## Source map and maintenance boundary

Primary scope/status:

- [Official DVA-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02.html)
- [Domain 1: Development with AWS Services](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02-domain1.html)
- [Domain 2: Security](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02-domain2.html)
- [Domain 3: Deployment](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02-domain3.html)
- [Domain 4: Troubleshooting and Optimization](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02-domain4.html)
- [Technologies and concepts](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/dva-technologies-concepts.html)
- [In-scope AWS services](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/dva-02-in-scope-services.html)
- [Version 2.1 revisions](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/dva-02-revisions.html)
- [Live certification page](https://aws.amazon.com/certification/certified-developer-associate/)

Implementation depth:

- [Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
- [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
- [IAM policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
- [KMS concepts](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
- [Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
- [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)

The weekly monitor should track the canonical guide and status, while source health checks every cited URL. The guide’s emerging topics, exact service list, product features, limits, runtimes, prices, exam delivery, and learning metadata are volatile. A human must interpret changes before content is rewritten.

## Exam-integrity boundary

This guide is an original synthesis of public objectives and documentation. It contains no recalled exam questions, leaked content, copied vendor banks, or paid-course reproductions. Use legitimate practice to find weak decisions; verify every technical rationale in current first-party documentation.
