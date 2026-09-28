---
exam_code: SCS-C03
vendor_id: aws
official_blueprint: https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-28
---

# SCS-C03 AWS Certified Security - Specialty Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were reviewed on September 28, 2026, including all 70 detailed skills. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#scs-c03-coverage-record). The [official SCS-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03.html) is authoritative.

**Current baseline:** SCS-C03 version 1.0, published March 26, 2026; six domains; 50 scored plus 15 unscored questions<br>
**Upcoming delivery change:** Simplified Chinese, Spanish (Latin America) and Portuguese (Brazil) delivery retires after December 31, 2026. This does not retire the overall SCS-C03 certification. Checked September 28, 2026; see the [deep-review report](../docs/research/2026-09-28-scs-c03-deep-review.md)<br>
**Important freshness boundary:** SCS-C03 replaced SCS-C02 on December 2, 2025. Older courses can still teach useful AWS security concepts, but must be gap-checked against AWS's official [C02-to-C03 comparison](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03-appendix-b.html).<br>
**Official source:** [AWS Certified Security - Specialty exam guide](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03.html)

## How to use this guide

SCS-C03 tests whether you can secure AWS workloads as a system: establish preventive controls, make activity observable, identify a meaningful signal, preserve evidence, contain the incident, recover safely, and prove that the environment still meets policy. Product recognition is not enough. For each scenario, identify the protected asset, threat actor or failure, trust boundary, preventive/detective/corrective controls, evidence source, response owner, and operational tradeoff.

The detailed exam guide targets the equivalent of **3–5 years securing cloud solutions**. The live certification page separately describes an experienced candidate as having five years of IT-security experience and at least two years securing AWS workloads. These descriptions are not identical; both point to a specialty exam that assumes hands-on AWS and security depth. There is no formal certification prerequisite.

The live page lists 170 minutes, 65 questions, USD 300, and delivery in English, Japanese, Korean, Portuguese (Brazil), Simplified Chinese, and Spanish (Latin America). The detailed guide identifies multiple-choice, multiple-response, ordering, and matching interactions; 50 scored and 15 unidentified unscored items; compensatory scoring; and a 750 minimum scaled score. The credential page summarizes only multiple-choice/multiple-response formats, while the detailed blueprint also lists ordering/matching. Preserve this source discrepancy and prepare from the fuller blueprint; verify delivery before booking.

Use this loop for every topic:

1. state the asset, business/compliance requirement, data classification, actors, accounts, Regions, and trust boundaries;
2. select identity, network, workload, data, and organization-level preventive controls;
3. define logs, findings, metrics, aggregation, retention, integrity, access, and alert ownership before an incident;
4. distinguish preparation, detection, validation, containment, eradication, recovery, and lessons learned;
5. test policy evaluation, failure modes, quotas, cost, deployment/rollback, and evidence collection in a safe lab;
6. explain why the rejected alternatives fail the exact requirement.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Domain | Weight | Central question |
|---|---:|---|
| 1. Detection | 16% | How will activity be collected, normalized, analyzed, surfaced, and troubleshot across accounts? |
| 2. Incident Response | 14% | How will the organization prepare, investigate, preserve evidence, contain, recover, and improve? |
| 3. Infrastructure Security | 18% | Which edge, compute, application, GenAI, and network controls reduce workload exposure? |
| 4. Identity and Access Management | 20% | How are humans and workloads authenticated and authorized at least privilege, and why did access succeed or fail? |
| 5. Data Protection | 18% | How are data, credentials, keys, certificates, integrity, retention, backup, and transport protected? |
| 6. Security Foundations and Governance | 14% | How are accounts, guardrails, secure deployments, central services, and audit evidence governed at scale? |

Use the official [Domain 1](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03-domain1.html), [Domain 2](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03-domain2.html), [Domain 3](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03-domain3.html), [Domain 4](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03-domain4.html), [Domain 5](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03-domain5.html), and [Domain 6](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03-domain6.html) task pages as the assessment contract. The [in-scope services list](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/scs-02-in-scope-services.html) is non-exhaustive and can change.

## 1. Detection — 16%

### 1.1 Design monitoring and alerting around decisions

Start with required outcomes: detect unauthorized access, public exposure, malware, exfiltration, control drift, vulnerable workloads, abnormal API behavior, suspicious network/DNS activity, or an unavailable security control. Define severity, owner, response time, enrichment, suppression, escalation, and evidence retention. A dashboard without an operational decision and owner is presentation, not detection engineering.

- **CloudTrail** records supported account activity and API events. Use organization trails, multi-Region coverage, validation, centralized protected destinations, and appropriate management/data/Insights events.
- **CloudWatch** supplies metrics, alarms, logs, queries, dashboards, subscriptions, and agent-collected OS/application telemetry. A metric alarm and a log-derived finding solve different problems.
- **AWS Config** evaluates configuration state and change against rules/conformance packs; it is not a packet or application-event detector.
- **GuardDuty** produces managed threat findings from multiple telemetry sources. **Inspector** assesses supported workloads/images/code for vulnerabilities and exposure. **Macie** discovers sensitive data and risky S3 posture.
- **Security Hub** aggregates, normalizes, correlates, and prioritizes supported findings and standards. **Security Lake** centralizes supported security data in OCSF-compatible form for analytics and integrations.

Decide which accounts own collection, security administration, analytics, and response. Use Organizations and delegated administration where supported. Protect the logging account and destination from workload administrators, enforce retention, encrypt appropriately, monitor delivery failure, and control who can query sensitive logs.

**Related item:** OCSF is a shared event schema, not a detector. Normalization makes multi-source analysis easier, but field mapping, timestamp quality, source completeness, enrichment, and detection logic still determine whether an investigation succeeds.

[GuardDuty Custom Detection Rules](https://docs.aws.amazon.com/guardduty/latest/ug/custom-detection-rules.html) are AWS-maintained rules enabled for particular accounts, rather than arbitrary user-written detector code. Live mode produces findings; dry run emits metrics on matches, creates no findings and expires after 14 days. No match means no dry-run metrics. The [September 18 history update](https://docs.aws.amazon.com/guardduty/latest/ug/doc-history.html) also warns that a rule depending on a redacted CloudTrail field will not match. Verify association, mode, source coverage and required fields before interpreting silence as safety.

[GuardDuty AI Protection](https://docs.aws.amazon.com/guardduty/latest/ug/ai-protection.html) detects supported anomalous invocation and cost-harvesting activity. Its direct prompt-injection detection requires Bedrock Guardrails and supported Bedrock/Region coverage. This detection layer does not replace tool authorization or guarantee protection against all indirect injection. Check the enabled protection plans and available evidence for each workload.

### 1.2 Build a trustworthy logging pipeline

For every source, document producer → configuration → permission → transport/subscription → destination → partition/index → query/detection → alert/ticket. Include CloudTrail, CloudWatch Logs, VPC and Transit Gateway Flow Logs, Route 53 Resolver query logs, load balancer/CloudFront/WAF logs, S3 access, database audit, Kubernetes/control-plane, OS/application, and security-service findings where required.

Choose a query layer deliberately: CloudWatch Logs Insights for operational log queries, Athena for data in S3, OpenSearch for indexed search/visualization, Security Lake for normalized lake workflows, or a third-party SIEM integration. Use Kinesis Data Firehose, Lambda, EventBridge, subscriptions, or supported native integrations only when their delivery, retry, ordering, transformation, security, and cost behavior fit.

Troubleshoot missing evidence from both ends. Confirm the event occurred, logging is enabled in the correct account/Region, resource/data-event selector matches, service-linked/delivery roles and destination policies allow writes, encryption keys allow the service path, filters are not excluding records, and queries use the correct time/partition/schema. Alert on logging-control changes and delivery gaps.

**Related item:** VPC Flow Logs contain flow metadata, not payloads, and an `ACCEPT` result does not prove the application responded. Correlate interface/time/tuple with load-balancer, WAF, DNS, host, application, and identity evidence.

## 2. Incident Response — 14%

### 2.1 Prepare and test before the alert

Create incident plans and service-specific runbooks with severity, roles, communications, legal/privacy escalation, evidence handling, credential access, isolation options, recovery criteria, and post-incident actions. Establish a security incident account or clean-room pattern, pre-provision forensic tools, define cross-account roles, and keep break-glass access independent, monitored, tested, and tightly controlled.

Use Systems Manager Automation/OpsCenter, Step Functions, Lambda, EventBridge, Security Hub custom actions or the AWS Automated Security Response patterns to orchestrate bounded actions. Human approval is appropriate when business impact or evidence risk is high. Test runbooks with simulations, AWS Fault Injection Service where safe, and Resilience Hub/other exercises; measure detection, validation, containment, recovery, and communication time.

### 2.2 Respond without destroying the evidence

Triage is not immediately deleting the compromised resource. Validate the finding, determine affected principal/resource/account/Region/time, identify scope and blast radius, preserve relevant logs/configuration/snapshots or disk artifacts, and record every responder action. Isolate with reversible controls where possible: quarantine security groups, revoke or constrain sessions/credentials, deny an abused path, remove a target from service, or move traffic to a known-good environment.

Containment stops continued harm; eradication removes the cause; recovery restores a verified service. Rotate credentials based on actual exposure and dependencies, rebuild from trusted artifacts, validate data/configuration integrity, restore monitoring, test required and forbidden behavior, and watch for recurrence. Root-cause analysis should connect initial access, control failure, attacker/action path, detection gap, and systemic correction.

Amazon Detective can assist linked investigation; CloudTrail Lake, Security Lake, Logs Insights, Athena, OpenSearch, Config history, GuardDuty/Security Hub findings, IAM evidence, snapshots, and workload logs answer different questions. Preserve chain-of-custody and time correlation appropriate to organizational requirements. [CloudTrail Lake closed to new customers May 31, 2026](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html), with existing-account/organization eligibility distinctions. CloudTrail trails remain supported; use trails plus an appropriate query path for a new-account lab.

Changing a [security-group rule does not immediately interrupt tracked connections](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html). A quarantine plan must verify existing sessions and every egress path. A scoped stateless network ACL can interrupt traffic but affects the subnet and return paths; choose a tested containment method with an explicit blast radius and responder access.

The [April 8 forensic-artifact article](https://aws.amazon.com/blogs/security/a-framework-for-securely-collecting-forensic-artifacts-into-s3-buckets/) is useful for its collection/storage design: separate evidence account, case-specific upload prefix, short-lived scoped credentials, protected encryption, data-event auditing and retention. A hash detects changed bytes relative to a trusted recorded digest; it does not establish who collected them or their original truth. Keep collector, time, source, transfer and access records. The article's deployment/code was not executed here; its KMS example needs adjustment when S3 Bucket Keys are used.

**Related item:** Automated remediation should be idempotent, scoped, observable, retry-aware, protected from recursive triggers, and able to stop or roll back. A fast destructive action can erase evidence or cause a larger outage.

## 3. Infrastructure Security — 18%

### 3.1 Secure edge and application ingress

Map protocol and layer before choosing controls. CloudFront, Global Accelerator, Route 53, API Gateway, ALB/NLB, AWS WAF, Shield/Shield Advanced, Network Firewall, and third-party appliances act at different points. Use CloudFront origin access controls and restricted origins, current TLS/security policies, certificates, WAF managed/custom rules, rate-based controls, geolocation/IP/reputation signals, bot or application-specific protections where justified, and DDoS readiness/escalation.

WAF rule order, scope-down conditions, labels, oversize handling, forwarded IP source, exclusions, and count-before-block rollout matter. Evaluate third-party rule groups and OCSF-compatible security integrations rather than assuming marketplace content is inherently safe. Test normal, malicious, and false-positive paths and preserve WAF/edge logs.

[S3 CORS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cors.html) controls browser cross-origin behavior. It does not grant S3 permission; bucket/IAM policies and other applicable controls still apply. An allowed origin is not authentication, and a non-browser caller does not become authorized or unauthorized merely through a CORS setting. For IoT endpoints, separately map device certificate identity, topic/action permissions and lifecycle; do not substitute web CORS for device authorization.

### 3.2 Harden compute, containers, serverless, and GenAI workloads

Build trusted AMIs and container images through pipelines with source provenance, patching, vulnerability scanning, signing/attestation, configuration baselines, tests, promotion, and retirement. Systems Manager, EC2 Image Builder, Inspector, GuardDuty Runtime Monitoring, ECR scanning, Session Manager, IAM roles, IMDS controls, and service-native isolation contribute different controls. Prefer short-lived role credentials over embedded secrets and avoid broad instance/task/execution roles.

Task 3.2.6 still names CodeGuru Security, but its [CLI reference records November 20, 2025 end of support](https://docs.aws.amazon.com/cli/latest/reference/codeguru-security/). Retain the pipeline-vulnerability-detection concept and use a currently supported scanner in a new lab.

For Lambda and managed services, minimize execution roles, dependencies, network reachability, environment secrets, concurrency/blast radius, and untrusted input. For EKS/ECS, distinguish AWS IAM, Kubernetes RBAC, workload identity, node role, security groups/network policy, admission/policy, image/runtime controls, and cluster/audit logs.

For generative-AI applications, define trusted data/tool boundaries, input/output filtering, prompt-injection defenses, retrieval authorization, action approval, least-privilege tool roles, tenant isolation, sensitive-data handling, model/provider controls, logging, evaluation, and kill switches. Apply relevant OWASP LLM risk thinking, but map each threat to the actual AWS architecture and business impact.

**Related item:** A model guardrail is one layer, not an authorization system. The application must re-establish identity and policy at retrieval and tool-execution boundaries; never let model text confer permission.

### 3.3 Design and troubleshoot network security controls

Security groups are stateful resource/ENI controls; network ACLs are stateless subnet controls; route tables select next hops; endpoint policies restrict supported endpoint use; resource/identity policies authorize APIs; WAF examines supported Layer-7 requests; Network Firewall and appliances inspect supported routed traffic. Trace both forward and return paths before changing a rule.

Use public/private subnets, egress control, NAT/egress-only gateways, VPC endpoints/PrivateLink, Transit Gateway segmentation, inspection VPCs, Firewall Manager, DNS Firewall, Verified Access, VPN/Direct Connect encryption patterns, and service-to-service private connectivity according to requirements. Avoid broad `0.0.0.0/0`, unrestricted east-west paths, unintended transitive routing, asymmetric appliance paths, and bypass routes.

Troubleshoot with route tables, security groups, NACLs, endpoint/resource policies, network/firewall/WAF logs, Flow Logs, Reachability Analyzer and Network Access Analyzer. Start from source, destination, direction, protocol/ports, expected next hops, identity, DNS, and return path. Do not weaken several controls at once to make a symptom disappear.

## 4. Identity and Access Management — 20%

### 4.1 Authenticate humans and workloads

Centralize workforce access through IAM Identity Center/federated identity where appropriate, require strong MFA, use permission sets and short sessions, and monitor privileged changes. Cognito supports application user identity patterns; Directory Service integrates directory use cases; IAM Roles Anywhere issues temporary AWS credentials to authenticated external workloads; STS and role assumption underpin temporary access. S3 presigned URLs delegate time-limited operation capability and must be scoped and protected like credentials.

For each authentication failure, identify issuer/IdP, subject, audience, signature/certificate, federation assertion or token, trust policy, role/permission set, session duration, clock, device/context condition, and CloudTrail/Identity Center/Cognito evidence. Authentication proves an identity; it does not by itself authorize the requested resource operation.

The [June 24 sign-in policy article](https://aws.amazon.com/blogs/security/restrict-aws-management-console-access-to-expected-networks-with-sign-in-resource-based-policies-and-rcps/) adds useful console-access practice: define allowed networks and tested break-glass access, review generated permission statements, enable enforcement deliberately, then verify allowed/denied sign-ins in CloudTrail. Creating statements alone does not enable enforcement. These controls address sign-in/console access; broader API/data controls remain necessary. The example commands were not executed for this review.

### 4.2 Evaluate authorization with principal and policy context

Reason through identity policy, resource policy, role trust, session policy, permission boundary, Organizations SCP/RCP, VPC endpoint policy, KMS key policy/grants, service-specific ACL/control, and explicit denies. An SCP is a maximum permission boundary for member accounts, not a grant. Permission boundaries limit identity-based grants, and role trust controls who may assume a role, not what the resulting session may do.

Avoid a universal “all policies intersect” shortcut. Under [same-account evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic_policy-eval-denyallow.html), a resource policy granting directly to a role-session ARN can grant access despite an implicit deny in identity, boundary or session policies. A grant to the role ARN has different limits. Applicable explicit denies still win; Organizations and service-specific rules still matter. Inspect the exact principal and request context before explaining a result.

[Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html) externalizes authorization for your application's principals/actions/resources using Cedar. Your application authenticates the caller and enforces the returned decision. It does not replace IAM authorization to the underlying AWS service.

Use RBAC for stable job functions and ABAC for scalable attributes/tags, with governance over tag issuance and mutation. Apply conditions such as organization, resource/request/principal tags, source network/endpoint, MFA, requested Region, TLS, service-mediated calls, or confused-deputy protections where supported. Use resource policies and roles deliberately for cross-account access.

IAM Access Analyzer can identify external/internal access findings and generate policy suggestions from observed activity; Policy Simulator helps evaluate supported policy behavior. Neither replaces verifying the actual principal, session context, resource policy, Organizations boundaries, service control, and CloudTrail error.

**Related item:** KMS authorization is intentionally distinct. Key policy, IAM permissions, grants, encryption context, region/key state, and the calling service/principal can all matter; “the role has `kms:Decrypt`” is not a complete proof.

## 5. Data Protection — 18%

### 5.1 Protect data in transit and private paths

Require modern TLS through supported service and load-balancer policies, redirect or reject plaintext, manage certificates and renewal, and validate hostname/trust/client-auth requirements. Use PrivateLink/VPC endpoints, Client VPN, Verified Access, private APIs/endpoints, or appropriate hybrid connectivity to reduce public exposure—but remember that private connectivity does not replace identity authorization or encryption requirements.

SCS-C03 explicitly adds inter-resource encryption examples such as EMR and EKS inter-node paths, SageMaker AI, and Nitro-based encryption. Identify which hop is encrypted by default, configurable, unsupported, or dependent on workload protocol/current instance type. Verify current service documentation rather than generalizing one service's behavior.

### 5.2 Choose at-rest encryption, integrity, retention, and recovery controls

Compare service-managed keys, AWS managed KMS keys, customer managed KMS keys, CloudHSM/custom key stores, external key stores, server-side encryption, and client-side encryption against key control, separation of duties, availability, latency, cost, import/residency, audit, and deletion/recovery requirements. Envelope encryption protects data keys with a key-encryption key; encryption context can bind cryptographic operations to context and policy.

Integrity/immutability is different from confidentiality. S3 Versioning, Object Lock retention/legal hold, Glacier Vault Lock, checksums/signatures, code signing, backup vault lock, protected cross-account copies, and restore tests meet different needs. Lifecycle rules manage transition/expiration; they are not backups. Design RPO/RTO, vault ownership, KMS dependencies, ransomware isolation, replication, and regular recovery verification.

### 5.3 Manage keys, secrets, certificates, and sensitive data

Use Secrets Manager for managed secret lifecycle/rotation patterns and Parameter Store for appropriate configuration/secret use cases; choose based on required features and integrate applications through least-privilege roles and caching without logging secret values. Rotate safely with overlapping validity and rollback, and distinguish secret rotation from KMS key rotation or certificate renewal.

AWS-generated KMS key material and imported key material have different availability, durability, rotation, expiration, and operational responsibilities. External key stores and CloudHSM shift control and failure dependencies. Understand aliases versus key IDs/ARNs, multi-Region primary/replica keys, grants, key states, deletion waiting periods, and Private CA hierarchy/issuance/revocation. Test loss and recovery assumptions.

[KMS rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) supports on-demand rotation for symmetric encryption keys with imported material, including multi-Region keys. For imported multi-Region material, import the same new material into the primary and each replica before initiating rotation on the primary; AWS does not copy the imported key material between Regions. The [import procedure](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-import-key-material.html) states that deletion/expiry of any associated material makes the key `PendingImport` and unusable for cryptographic operations. Retain protected recovery copies and test dependencies. This differs from rotating a secret and does not re-encrypt stored application data.

CloudWatch Logs data-protection policies and SNS message data protection can audit or de-identify supported sensitive-data patterns. Macie discovers/classifies sensitive S3 data. Masking a log/message does not remove the original sensitive value from upstream producers or every destination; fix collection and access design as well.

**Related item:** Key rotation does not automatically re-encrypt all existing ciphertext. Envelope-encrypted data records which key version/material protected its data key; required re-encryption is a separate migration and validation decision.

## 6. Security Foundations and Governance — 14%

### 6.1 Govern accounts and central security services

Use AWS Organizations organizational units and accounts as isolation/delegation boundaries, with Control Tower for supported landing-zone controls and lifecycle. Separate security tooling, log archive, shared services, networking, production, nonproduction, and sandbox responsibilities based on risk. Design account vending, ownership, contacts, quotas, budgets, regions, baseline roles, logging, and decommissioning.

Organizations policies include SCPs, resource control policies, declarative policies, tag/backup policies, and AI-service opt-out policies with different semantics. Test inheritance and explicit denies. [RCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) constrain supported resources in member accounts, including access by external principals; SCPs constrain covered member-account principals. Neither grants permission. RCPs do not protect management-account resources or restrict service-linked-role calls, and service/action exceptions apply. Check support for the exact operation before relying on an organization-wide statement. Delegate supported security services to appropriate accounts and aggregate findings/configuration without granting unnecessary workload administration.

Centralized root access for member accounts, root credential management, MFA, tightly controlled management-account root, and tested break-glass procedures reduce standing risk. Root is not an everyday administrator. Monitor every privileged path.

### 6.2 Make secure deployment repeatable

Represent guardrails and workload baselines as versioned IaC. Use CloudFormation/StackSets, CDK or another IaC tool with linting, policy-as-code such as CloudFormation Guard, least-privilege deployment roles, artifact integrity, change sets/plans, peer/automated checks, staged rollout, rollback, drift detection, and post-deployment validation. Central deployment must account for partial failures across accounts/Regions.

Tags support ownership, environment, classification, cost, and ABAC, but only when creation/mutation is governed. Firewall Manager centralizes supported policies. Service Catalog distributes approved products; RAM shares supported resources. Neither is a general substitute for authorization design.

### 6.3 Prove compliance with evidence

AWS Config rules/conformance packs evaluate configuration and can trigger notification/remediation. Security Hub standards consolidate supported controls/findings. Audit Manager helps collect and organize evidence; Artifact supplies AWS compliance reports/agreements. The Well-Architected Tool assesses architectures against guidance. These do not make an architecture compliant by themselves. [Audit Manager restricted new setup from April 30, 2026](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html) and is in maintenance; existing account/organization/Region configuration affects eligibility. Use available evidence-collection mechanisms for new labs rather than assuming enrollment is possible.

Map every control to requirement, scope, owner, implementation, evidence, frequency, exception/expiry, remediation, and reviewer. Separate continuous technical evidence from point-in-time documents and inherited AWS responsibility. Validate automated remediation in a canary scope, preserve evidence, and avoid oscillation or unauthorized changes.

**Related item:** Compliance is not equivalent to security. A control can pass while a threat path remains, and a secure design may still lack the evidence required by an auditor. Engineer both risk reduction and durable proof.

## Integrated scenarios

### Scenario 1: Multi-account exfiltration alert

A GuardDuty finding reports unusual reads from a sensitive S3 bucket followed by outbound transfer. Determine whether CloudTrail data events and identity/session context are complete; correlate GuardDuty, S3, VPC, DNS and application evidence; validate the affected objects/principal/time and whether Macie classification changes severity. Preserve central logs and relevant snapshots, constrain the session/role and egress without deleting evidence, inspect trust/resource/key/endpoint/Organizations policies, rotate exposed credentials, rebuild if integrity is uncertain, test recovery, and turn the root cause into bounded policy/detection/IaC improvements.

### Scenario 2: Organization-wide least privilege and audit

A regulated company needs workforce federation, workload roles, deny guardrails, protected logs, encryption, recoverable data, and monthly evidence across 200 accounts. Design OUs/accounts and delegated administrators; Identity Center permission sets and MFA; workload identity and cross-account trust; SCP/RCP/endpoint/key-policy boundaries; organization trails, Config, Security Hub and log archive; customer-managed keys and backup controls; StackSets/policy checks; exception expiry; eligible evidence-collection tooling and clear ownership. Prove both required access and forbidden paths in a canary OU before broad rollout.

### Scenario 3: Prompt injection reaches an agent tool

A retrieval agent attempts an unauthorized action after processing hostile content. Preserve prompt/retrieval/tool/auth/audit traces with sensitive-data protections. Identify whether untrusted content was treated as instruction, retrieval crossed tenant/ACL boundaries, the tool role was too broad, or approval/validation failed. Revoke or constrain the action path, disable the affected tool/version, validate data impact, and recover through a tested prior release. Add input/content controls, authorization at retrieval and tool execution, structured tool schemas, least privilege, risk-based approvals, output validation, adversarial regression tests, monitoring, and a kill switch. A model-level guardrail alone is insufficient.

## Worked security decisions

These original scenarios use synthetic records. Eight local arithmetic/hash assertions passed; no AWS policy simulation, attack, containment or cloud lab was executed.

1. **Choose the correct permission explanation:** A same-account resource policy grants a supported operation directly to a role-session ARN. The identity policy merely omits it. That omission alone is not an explicit deny and need not block the resource grant. Change the principal to the role ARN, or introduce an applicable explicit deny, and the evaluation can change. Record all service/Organizations constraints before predicting access.
2. **Measure response stages:** An event occurs at 10:00, is detected at 10:04, contained at 10:11 and service is verified at 10:26. Detection took four minutes; detection-to-containment took seven; total restoration took 26. A 20-minute recovery target fails even if the automated containment action itself was fast.
3. **Check artifact integrity:** Record a SHA-256 digest of synthetic evidence, copy it, then alter one byte in a second copy. The exact copy has the same digest; the altered copy differs. Store the original digest in a separately protected record with collector/source/time. An attacker able to replace both file and reference digest defeats this comparison as proof of custody.
4. **Interpret a rule experiment:** A dry-run detector matches 12 of 1,000 known test events, or 1.2%. That is a match rate, not accuracy; correctness needs labels for expected matches and misses. Zero live findings are expected in dry run. Verify the 14-day window and required fields before diagnosing missing metrics.
5. **Retain usable encrypted evidence:** An immutable evidence object still depends on an available decryption path. An imported multi-Region KMS key does not become recoverable just because replicas exist; required material, policy and key state must work in the recovery Region. A rotated key does not repair an exposed data key or re-encrypt old evidence automatically.

## Hands-on labs

The eight labs remain proposed. This review ran only the synthetic checks described above. Use a sandbox account or authorized organization, apply budgets, avoid real sensitive data, and remove billable resources after each lab.

1. **Organization logging model:** diagram an organization trail and protected log-archive destination; implement a safe subset, test delivery, query an event, deny a simulated workload-admin deletion path, and alert on trail change.
2. **Detection pipeline:** create benign test activity, route a supported signal through EventBridge/Security Hub or CloudWatch, enrich it, open a mock incident, suppress a documented duplicate, and test missing-source monitoring.
3. **Evidence-preserving response:** write and rehearse a runbook for a compromised EC2 role: validate, preserve metadata/snapshot/logs, quarantine, revoke sessions where appropriate, rebuild, restore, observe, and document every action.
4. **Policy evaluation lab:** construct cross-account role/resource access with a permission boundary and an explicit Organizations/endpoint/key-policy constraint. Predict results, test allowed and denied operations, and explain each decision from evidence.
5. **Network control trace:** deploy a small private workload behind a supported entry point. Trace a request through routes, SG/NACL, WAF/firewall/endpoint policy and return path; generate one safe deny and correlate logs.
6. **Key and secret lifecycle:** create a customer-managed KMS key and test envelope-encrypted service access, key-policy failure, rotation/lifecycle assumptions, a Secrets Manager rotation design, and recovery/rollback. Never import valuable production material.
7. **Immutable recovery:** protect test objects/backups using versioning/retention or vault controls, simulate accidental change, restore to an isolated destination, validate integrity and permissions, and record measured RPO/RTO.
8. **Governed deployment:** deploy a small baseline with IaC, lint/policy-check it, canary a change, create drift, detect/remediate safely, roll back, and collect Config/Security Hub/audit evidence plus an approved exception with expiry.

## Original knowledge checks

1. Why is an organization trail plus protected destination stronger than separate unmanaged account trails? **Central policy and a separately protected destination reduce inconsistent coverage and workload-admin deletion risk; verify every account/Region and delivery path.**
2. When would Security Lake add value beyond Security Hub? **Security Lake stores normalized security telemetry for analytics; Security Hub supplies findings and posture context. Choose from the investigation/query need.**
3. Why can a healthy dashboard still hide a telemetry-delivery failure? **A dashboard can display old or partial data. Monitor source coverage, delivery freshness, query time range and failures independently.**
4. Which evidence distinguishes an API authorization failure from a network failure? **A service authorization error with principal/action context points to policy evaluation; DNS/routes/connection logs and Flow Logs help isolate transport. A missing event alone proves neither.**
5. What does a VPC Flow Logs `ACCEPT` record not prove? **It does not prove an application response, valid authorization, useful payload or successful transaction.**
6. How would you detect that a required data-event selector stopped covering a bucket? **Generate an authorized benign object operation, confirm selector configuration and expected delivery, and alert on selector/control changes or missing evidence.**
7. Why normalize events to OCSF, and what problems remain after normalization? **It eases multi-source correlation; completeness, mapping, timestamps, identity context and detection logic still need validation.**
8. What should an alert owner know before the alert fires? **Signal meaning, affected scope, severity, owner, evidence, response target, runbook, escalation and stop conditions.**
9. Why should containment usually preserve evidence? **Evidence is needed to determine scope, cause and recovery integrity; destructive containment can erase it.**
10. How do containment, eradication, and recovery differ? **Containment limits continued harm; eradication removes the cause; recovery restores and verifies required service.**
11. What makes an automated remediation safe to retry? **Stable operation identity, preconditions, idempotent action, bounded retries, durable outcome, verification and stop/escalation.**
12. Which preparation step prevents responders from depending on a compromised identity plane? **Prearranged protected responder identities, cross-account access and tested break-glass paths independent of the affected system.**
13. What must a tested incident runbook measure besides technical recovery? **Detection, validation, containment, communications, evidence preservation, data correctness and authorized access as well as restoration time.**
14. How do you validate the scope and impact of a managed finding? **Correlate the finding with source events, actual principal/resource/time, permissions, data classification and affected dependencies.**
15. When should CloudFront/WAF be preferred to a network-layer control? **For supported HTTP/application threats, content delivery/origin protection and Layer-7 inspection; still secure the network and origin path.**
16. Why deploy a new WAF rule in count mode first? **Measure expected matches and false positives before blocking real users; count mode itself does not block attacks.**
17. What control prevents a model from using its own output as authorization? **Independent deterministic authorization at the tool and data boundaries, with scoped identity, validated parameters and required approval.**
18. How do image provenance and runtime monitoring complement vulnerability scanning? **Provenance identifies trusted build inputs; scanning detects known issues; runtime monitoring observes behavior after deployment.**
19. Why can a private subnet still exfiltrate data? **It can have NAT, endpoints, peer/hybrid routes or permitted service APIs that reach an unauthorized destination.**
20. What causes asymmetric inspection, and what evidence would confirm it? **Forward and return paths traverse different inspection state; correlate routes, appliance placement and directional flow/firewall evidence.**
21. How do SGs, NACLs, WAF, Network Firewall, and IAM policies differ? **SGs are stateful resource controls, NACLs stateless subnet controls, WAF supported Layer-7 inspection, Network Firewall routed inspection, and IAM API authorization.**
22. Why is broadening several controls at once poor troubleshooting? **It increases exposure and removes the evidence needed to identify which layer caused the failure.**
23. How do authentication and authorization differ in a federated role session? **Authentication validates the identity/session; authorization evaluates whether that principal may perform this operation on this resource.**
24. Why does an SCP not grant access? **It sets a maximum for covered principals; an applicable permission grant is still required.**
25. How do a permission boundary and a session policy constrain a role session? **They limit relevant grants under IAM evaluation rules, but same-account resource grants to session principals have exceptions; applicable explicit denies still apply.**
26. Which controls participate in a cross-account KMS decrypt decision? **Caller identity/session permissions, key policy or grants, applicable organization/endpoint controls, encryption context and key state/Region.**
27. What governance makes ABAC trustworthy? **Trusted attribute sources, restricted tag creation/mutation, correct propagation and tests for missing or forged tags.**
28. How would Access Analyzer and CloudTrail contribute different evidence? **Analyzer reasons about supported access/policy relationships; CloudTrail records observed calls and context. Neither alone proves every possible path.**
29. When is a presigned URL the wrong delegation mechanism? **When the recipient must have independently revocable identity-bound authorization or the bearer URL could expose excessive scope/duration.**
30. Why can a trust-policy fix still leave an assume-role attempt failing? **The caller can still lack assume-role permission or fail MFA/external-ID/session/organization conditions or other applicable denies.**
31. How do client-side and server-side encryption change trust and key-handling responsibility? **Client-side encryption places encryption and key handling before service upload; server-side encryption delegates the service encryption path while retaining customer policy duties.**
32. Why is encryption not an integrity or retention control by itself? **Encrypted data can still be altered, deleted or retained incorrectly by an authorized path; use distinct integrity, retention and recovery controls.**
33. What operational risk does imported KMS key material introduce? **The customer must preserve and import required material; expiration/deletion can make the key unusable and disrupt dependent workloads.**
34. What does multi-Region KMS key replication not replicate automatically? **It does not replicate data, aliases, policies or every regional setting; imported key material must be imported in each related Region.**
35. Why does key rotation not re-encrypt every stored object? **Rotation changes the material used for new KMS operations; existing encrypted data/data keys need a separate re-encryption plan if required.**
36. How do Secrets Manager rotation and KMS key rotation differ? **Secret rotation changes credentials used by an application; KMS rotation changes cryptographic key material. Both need dependency-aware validation.**
37. Why must an immutable backup be restored and validated? **Immutability alone does not prove usable keys, permissions, complete data, clean workload state or achieved RPO/RTO.**
38. How can log masking still leave sensitive data exposed? **Original data can remain upstream, in another destination or available to an authorized unmask operation; minimize collection and control access.**
39. How do an SCP, RCP, Config rule, and Control Tower control differ? **SCPs constrain covered principals; RCPs constrain supported resources; Config detects configuration state; Control Tower manages supported preventive/detective/proactive controls.**
40. What makes a central StackSet deployment safe across hundreds of accounts? **Scoped deployment roles, tested templates, canary waves, concurrency/failure limits, rollback, partial-result handling and per-account verification.**
41. Why are Artifact reports and Audit Manager evidence not the same thing? **Artifact supplies AWS reports/agreements; Audit Manager organizes customer assessment evidence where eligible. Each covers a different responsibility.**
42. What exact SCS-C03 gaps must an SCS-C02 course be checked for? **Current domain weights, finding validation, OCSF/third-party edge integrations, GenAI protection, inter-resource encryption, imported key behavior, masking and regional key/certificate patterns.**

Use misses to select the next lab or official task page. Do not memorize these as vendor questions; they are original prompts for explaining the published concepts.

## C02-to-C03 transition checklist

AWS began SCS-C03 delivery December 2, 2025. Before using SCS-C02 material, confirm that it covers or is supplemented for:

- the separate Detection and Incident Response domains and current six-domain weights;
- validation of security findings for scope and impact;
- OCSF integrations and third-party WAF rule groups;
- generative-AI application protections and OWASP LLM risks;
- inter-resource encryption examples for EMR, EKS, SageMaker AI, and Nitro;
- AWS-generated versus imported KMS key material, including operational implications;
- CloudWatch Logs and SNS sensitive-data masking/data-protection controls;
- single- and multi-Region key/certificate patterns including Private CA;
- current ordering and matching interaction types;
- current services, Organizations policy types, root-access features, quotas, Regions, and product terminology.

The comparison also lists removals and recategorizations. Do not over-index on deleted C02 detail merely because an older course spends time on it; foundational TCP/IP, TLS, policy structure, and host hardening can remain useful prerequisite knowledge even when no longer named as task detail.

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. Choose one coherent current path, use first-party documentation to close objective gaps, build the labs, and add one explanation-led practice source. Durations are provider-listed where available and otherwise labeled estimates; verify price, access, runtime, and SCS-C03 alignment before enrolling.

| Resource | Access | Estimated time |
|---|---|---:|
| AWS exam guide, six domain pages, services and comparison | Public | 4–8 hours mapping/review |
| AWS Skill Builder official question set and exam-prep plan | Free account; some subscription items | Allow 1 hour for questions/review; 15–35 selected hours estimated for plan |
| Pluralsight SCS-C03 current modules | Paid/trial | 2 hours 16 minutes for verified Detection module; 12–22 hours estimated as remaining domains publish |
| Udemy / Stéphane Maarek SCS-C03 | Paid | Plan 35–55 hours with labs/review |
| Udemy / Neal Davis SCS-C03 | Paid | Plan 30–50 hours with exercises/review |
| Tutorials Dojo SCS-C03 study path and practice exams | Public guide; paid practice | 1–2 hours guide; 10–18 hours attempts and rationale review estimated |
| Whizlabs SCS-C03 labs/course/practice | Paid | About 12 hours for ten highlighted projects; 25–50 selected hours estimated total |

- **Official scope and practice:** Start with the [SCS-C03 guide](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03.html), [AWS live certification page](https://aws.amazon.com/certification/certified-security-specialty/), and [official 20-question set](https://explore.skillbuilder.aws/learn/course/external/view/elearning/9153/aws-certification-official-practice-question-sets-english). The public page returned only a Skill Builder shell in this review; current count/runtime was not reverified. Allow about an hour for selected questions and explanations. Some full pretest/practice-plan items require Skill Builder subscription.
- **Current modular route:** [Pluralsight SCS-C03 Detection](https://www.pluralsight.com/courses/aws-scs-c03-detection) is **2 hours 16 minutes** and was updated July 2026. At this check, a complete stable six-domain path was not independently visible; add only published current modules and map them to the blueprint.
- **Detailed course:** [Udemy / Stéphane Maarek SCS-C03](https://www.udemy.com/course/ultimate-aws-certified-security-specialty/) is a **35–55-hour planning route including labs/review**. Public content was blocked; runtime, lecture count, update date and current C03 lesson alignment were not reverified. Use the transition checklist.
- **Lab-oriented alternative:** [Udemy / Neal Davis SCS-C03](https://www.udemy.com/course/aws-certified-security-specialty-course/) is a **30–50-hour planning route including exercises/review**. Public content was blocked; runtime, count, test entitlement and update date were not reverified.
- **Study/practice route:** [Tutorials Dojo SCS-C03 study path](https://tutorialsdojo.com/aws-certified-security-specialty-scs-c03-exam-guide-study-path/) links current preparation and its premium practice set; the [free sampler](https://portal.tutorialsdojo.com/courses/free-aws-certified-security-specialty-practice-exams-sampler/) contains 20 questions in timed/review modes. The public path retains older compliance references; verify current issuer guidance before using those. Verify current C03 revision inside the purchased product because its catalog transitioned from C02 during late 2025.
- **Hands-on route:** [Whizlabs' ten SCS-C03 security projects](https://www.whizlabs.com/blog/aws-security-projects-scs-c03/) reports **about 12 hours** of lab work across Macie/KMS, detection, WAF, automation, and other domains; pair selected labs with its course/practice product only after confirming current totals and blueprint alignment.
- **Broad reference route:** Use the [AWS Security Documentation](https://docs.aws.amazon.com/security/) and service security chapters to resolve implementation gaps (**20–40 selected hours**, not end-to-end reading). Prefer current service documentation to memorized feature lists.

No exact current SCS-C03 O'Reilly book/course, MeasureUp product, or stable complete Pluralsight path was independently verified in this review. Do not substitute search results or recalled-question products for a product page with a visible current blueprint. A realistic plan is **120–180 hours** for an experienced AWS security engineer and **220–350 hours** if IAM/KMS, networking, logging, incident response, and multi-account governance are still developing.

---

## Source map and freshness notes

The root guide, six domain pages, in-scope list, and C02/C03 comparison define the assessment contract. The live certification page defines current price, delivery, language, and experience-summary metadata. Third-party courses are learning choices, not scope authorities.

- **VERIFY CURRENT:** exam delivery, blueprint revisions, in-scope services, service features/names, Organizations policy/root-access behavior, IAM/KMS evaluation details, supported Regions, quotas, pricing, training totals, and subscription access.
- **Stable decision pattern:** requirement/threat → trust and data boundary → least-privilege preventive controls → protected complete telemetry → validated finding → evidence-preserving containment → trusted recovery → control and detection improvement.
- **SCS-C02 material:** use for durable concepts only after closing every item in the transition checklist.

This guide uses no recalled exam questions or restricted content. The knowledge checks are original and test published concepts rather than reproducing vendor items.
