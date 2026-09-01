---
exam_code: SCS-C03
vendor_id: aws
official_blueprint: https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# SCS-C03 AWS Certified Security - Specialty Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#scs-c03-coverage-record). The [official SCS-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03.html) is authoritative.

**Current baseline:** SCS-C03 version 1.0; six domains; 50 scored plus 15 unscored questions<br>
**Upcoming blueprint change:** None announced when checked September 1, 2026<br>
**Important freshness boundary:** SCS-C03 replaced SCS-C02 on December 2, 2025. Older courses can still teach useful AWS security concepts, but must be gap-checked against AWS's official [C02-to-C03 comparison](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03-appendix-b.html).<br>
**Official source:** [AWS Certified Security - Specialty exam guide](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03.html)

## How to use this guide

SCS-C03 tests whether you can secure AWS workloads as a system: establish preventive controls, make activity observable, identify a meaningful signal, preserve evidence, contain the incident, recover safely, and prove that the environment still meets policy. Product recognition is not enough. For each scenario, identify the protected asset, threat actor or failure, trust boundary, preventive/detective/corrective controls, evidence source, response owner, and operational tradeoff.

The detailed exam guide targets the equivalent of **3–5 years securing cloud solutions**. The live certification page separately describes an experienced candidate as having five years of IT-security experience and at least two years securing AWS workloads. These descriptions are not identical; both point to a specialty exam that assumes hands-on AWS and security depth. There is no formal certification prerequisite.

The live page lists 170 minutes, 65 questions, USD 300, and delivery in English, Japanese, Korean, Portuguese (Brazil), Simplified Chinese, and Spanish (Latin America). The detailed guide identifies multiple-choice, multiple-response, ordering, and matching interactions; 50 scored and 15 unidentified unscored items; compensatory scoring; and a 750 minimum scaled score. Verify current delivery details before booking.

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

Use the official [Domain 1](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03-domain1.html), [Domain 2](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03-domain2.html), [Domain 3](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03-domain3.html), [Domain 4](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03-domain4.html), [Domain 5](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03-domain5.html), and [Domain 6](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03-domain6.html) task pages as the assessment contract. The [in-scope services list](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/scs-03-in-scope-services.html) is non-exhaustive and can change.

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

Amazon Detective can assist linked investigation; CloudTrail Lake, Security Lake, Logs Insights, Athena, OpenSearch, Config history, GuardDuty/Security Hub findings, IAM evidence, snapshots, and workload logs answer different questions. Preserve chain-of-custody and time correlation appropriate to organizational requirements.

**Related item:** Automated remediation should be idempotent, scoped, observable, retry-aware, protected from recursive triggers, and able to stop or roll back. A fast destructive action can erase evidence or cause a larger outage.

## 3. Infrastructure Security — 18%

### 3.1 Secure edge and application ingress

Map protocol and layer before choosing controls. CloudFront, Global Accelerator, Route 53, API Gateway, ALB/NLB, AWS WAF, Shield/Shield Advanced, Network Firewall, and third-party appliances act at different points. Use CloudFront origin access controls and restricted origins, current TLS/security policies, certificates, WAF managed/custom rules, rate-based controls, geolocation/IP/reputation signals, bot or application-specific protections where justified, and DDoS readiness/escalation.

WAF rule order, scope-down conditions, labels, oversize handling, forwarded IP source, exclusions, and count-before-block rollout matter. Evaluate third-party rule groups and OCSF-compatible security integrations rather than assuming marketplace content is inherently safe. Test normal, malicious, and false-positive paths and preserve WAF/edge logs.

### 3.2 Harden compute, containers, serverless, and GenAI workloads

Build trusted AMIs and container images through pipelines with source provenance, patching, vulnerability scanning, signing/attestation, configuration baselines, tests, promotion, and retirement. Systems Manager, EC2 Image Builder, Inspector, GuardDuty Runtime Monitoring, ECR scanning, Session Manager, IAM roles, IMDS controls, and service-native isolation contribute different controls. Prefer short-lived role credentials over embedded secrets and avoid broad instance/task/execution roles.

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

### 4.2 Evaluate authorization as an intersection and boundary system

Reason through identity policy, resource policy, role trust, session policy, permission boundary, Organizations SCP/RCP, VPC endpoint policy, KMS key policy/grants, service-specific ACL/control, and explicit denies. An SCP is a maximum permission boundary for member accounts, not a grant. Permission boundaries limit identity-based grants, and role trust controls who may assume a role, not what the resulting session may do.

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

CloudWatch Logs data-protection policies and SNS message data protection can audit or de-identify supported sensitive-data patterns. Macie discovers/classifies sensitive S3 data. Masking a log/message does not remove the original sensitive value from upstream producers or every destination; fix collection and access design as well.

**Related item:** Key rotation does not automatically re-encrypt all existing ciphertext. Envelope-encrypted data records which key version/material protected its data key; required re-encryption is a separate migration and validation decision.

## 6. Security Foundations and Governance — 14%

### 6.1 Govern accounts and central security services

Use AWS Organizations organizational units and accounts as isolation/delegation boundaries, with Control Tower for supported landing-zone controls and lifecycle. Separate security tooling, log archive, shared services, networking, production, nonproduction, and sandbox responsibilities based on risk. Design account vending, ownership, contacts, quotas, budgets, regions, baseline roles, logging, and decommissioning.

Organizations policies include SCPs, resource control policies, declarative policies, tag/backup policies, and AI-service opt-out policies with different semantics. Test inheritance and explicit denies. Delegate supported security services to appropriate accounts and aggregate findings/configuration without granting unnecessary workload administration.

Centralized root access for member accounts, root credential management, MFA, tightly controlled management-account root, and tested break-glass procedures reduce standing risk. Root is not an everyday administrator. Monitor every privileged path.

### 6.2 Make secure deployment repeatable

Represent guardrails and workload baselines as versioned IaC. Use CloudFormation/StackSets, CDK or another IaC tool with linting, policy-as-code such as CloudFormation Guard, least-privilege deployment roles, artifact integrity, change sets/plans, peer/automated checks, staged rollout, rollback, drift detection, and post-deployment validation. Central deployment must account for partial failures across accounts/Regions.

Tags support ownership, environment, classification, cost, and ABAC, but only when creation/mutation is governed. Firewall Manager centralizes supported policies. Service Catalog distributes approved products; RAM shares supported resources. Neither is a general substitute for authorization design.

### 6.3 Prove compliance with evidence

AWS Config rules/conformance packs evaluate configuration and can trigger notification/remediation. Security Hub standards consolidate supported controls/findings. Audit Manager helps collect and organize evidence; Artifact supplies AWS compliance reports/agreements. The Well-Architected Tool assesses architectures against guidance. These do not make an architecture compliant by themselves.

Map every control to requirement, scope, owner, implementation, evidence, frequency, exception/expiry, remediation, and reviewer. Separate continuous technical evidence from point-in-time documents and inherited AWS responsibility. Validate automated remediation in a canary scope, preserve evidence, and avoid oscillation or unauthorized changes.

**Related item:** Compliance is not equivalent to security. A control can pass while a threat path remains, and a secure design may still lack the evidence required by an auditor. Engineer both risk reduction and durable proof.

## Integrated scenarios

### Scenario 1: Multi-account exfiltration alert

A GuardDuty finding reports unusual reads from a sensitive S3 bucket followed by outbound transfer. Determine whether CloudTrail data events and identity/session context are complete; correlate GuardDuty, S3, VPC, DNS and application evidence; validate the affected objects/principal/time and whether Macie classification changes severity. Preserve central logs and relevant snapshots, constrain the session/role and egress without deleting evidence, inspect trust/resource/key/endpoint/Organizations policies, rotate exposed credentials, rebuild if integrity is uncertain, test recovery, and turn the root cause into bounded policy/detection/IaC improvements.

### Scenario 2: Organization-wide least privilege and audit

A regulated company needs workforce federation, workload roles, deny guardrails, protected logs, encryption, recoverable data, and monthly evidence across 200 accounts. Design OUs/accounts and delegated administrators; Identity Center permission sets and MFA; workload identity and cross-account trust; SCP/RCP/endpoint/key-policy boundaries; organization trails, Config, Security Hub and log archive; customer-managed keys and backup controls; StackSets/policy checks; exception expiry; Audit Manager evidence and ownership. Prove both required access and forbidden paths in a canary OU before broad rollout.

### Scenario 3: Prompt injection reaches an agent tool

A retrieval agent attempts an unauthorized action after processing hostile content. Preserve prompt/retrieval/tool/auth/audit traces with sensitive-data protections. Identify whether untrusted content was treated as instruction, retrieval crossed tenant/ACL boundaries, the tool role was too broad, or approval/validation failed. Revoke or constrain the action path, disable the affected tool/version, validate data impact, and recover through a tested prior release. Add input/content controls, authorization at retrieval and tool execution, structured tool schemas, least privilege, risk-based approvals, output validation, adversarial regression tests, monitoring, and a kill switch. A model-level guardrail alone is insufficient.

## Hands-on labs

Use a sandbox account or authorized organization, apply budgets, avoid real sensitive data, and remove billable resources after each lab.

1. **Organization logging model:** diagram an organization trail and protected log-archive destination; implement a safe subset, test delivery, query an event, deny a simulated workload-admin deletion path, and alert on trail change.
2. **Detection pipeline:** create benign test activity, route a supported signal through EventBridge/Security Hub or CloudWatch, enrich it, open a mock incident, suppress a documented duplicate, and test missing-source monitoring.
3. **Evidence-preserving response:** write and rehearse a runbook for a compromised EC2 role: validate, preserve metadata/snapshot/logs, quarantine, revoke sessions where appropriate, rebuild, restore, observe, and document every action.
4. **Policy evaluation lab:** construct cross-account role/resource access with a permission boundary and an explicit Organizations/endpoint/key-policy constraint. Predict results, test allowed and denied operations, and explain each decision from evidence.
5. **Network control trace:** deploy a small private workload behind a supported entry point. Trace a request through routes, SG/NACL, WAF/firewall/endpoint policy and return path; generate one safe deny and correlate logs.
6. **Key and secret lifecycle:** create a customer-managed KMS key and test envelope-encrypted service access, key-policy failure, rotation/lifecycle assumptions, a Secrets Manager rotation design, and recovery/rollback. Never import valuable production material.
7. **Immutable recovery:** protect test objects/backups using versioning/retention or vault controls, simulate accidental change, restore to an isolated destination, validate integrity and permissions, and record measured RPO/RTO.
8. **Governed deployment:** deploy a small baseline with IaC, lint/policy-check it, canary a change, create drift, detect/remediate safely, roll back, and collect Config/Security Hub/audit evidence plus an approved exception with expiry.

## Original knowledge checks

1. Why is an organization trail plus protected destination stronger than separate unmanaged account trails?
2. When would Security Lake add value beyond Security Hub?
3. Why can a healthy dashboard still hide a telemetry-delivery failure?
4. Which evidence distinguishes an API authorization failure from a network failure?
5. What does a VPC Flow Logs `ACCEPT` record not prove?
6. How would you detect that a required data-event selector stopped covering a bucket?
7. Why normalize events to OCSF, and what problems remain after normalization?
8. What should an alert owner know before the alert fires?
9. Why should containment usually preserve evidence?
10. How do containment, eradication, and recovery differ?
11. What makes an automated remediation safe to retry?
12. Which preparation step prevents responders from depending on a compromised identity plane?
13. What must a tested incident runbook measure besides technical recovery?
14. How do you validate the scope and impact of a managed finding?
15. When should CloudFront/WAF be preferred to a network-layer control?
16. Why deploy a new WAF rule in count mode first?
17. What control prevents a model from using its own output as authorization?
18. How do image provenance and runtime monitoring complement vulnerability scanning?
19. Why can a private subnet still exfiltrate data?
20. What causes asymmetric inspection, and what evidence would confirm it?
21. How do SGs, NACLs, WAF, Network Firewall, and IAM policies differ?
22. Why is broadening several controls at once poor troubleshooting?
23. How do authentication and authorization differ in a federated role session?
24. Why does an SCP not grant access?
25. How do a permission boundary and a session policy constrain a role session?
26. Which controls participate in a cross-account KMS decrypt decision?
27. What governance makes ABAC trustworthy?
28. How would Access Analyzer and CloudTrail contribute different evidence?
29. When is a presigned URL the wrong delegation mechanism?
30. Why can a trust-policy fix still leave an assume-role attempt failing?
31. How do client-side and server-side encryption change trust and key-handling responsibility?
32. Why is encryption not an integrity or retention control by itself?
33. What operational risk does imported KMS key material introduce?
34. What does multi-Region KMS key replication not replicate automatically?
35. Why does key rotation not re-encrypt every stored object?
36. How do Secrets Manager rotation and KMS key rotation differ?
37. Why must an immutable backup be restored and validated?
38. How can log masking still leave sensitive data exposed?
39. How do an SCP, RCP, Config rule, and Control Tower control differ?
40. What makes a central StackSet deployment safe across hundreds of accounts?
41. Why are Artifact reports and Audit Manager evidence not the same thing?
42. What exact SCS-C03 gaps must an SCS-C02 course be checked for?

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
| AWS Skill Builder official question set and exam-prep plan | Free account; some subscription items | 30 minutes for 20-question set; 15–35 selected hours estimated for plan |
| Pluralsight SCS-C03 current modules | Paid/trial | 2 hours 16 minutes for verified Detection module; 12–22 hours estimated as remaining domains publish |
| Udemy / Stéphane Maarek SCS-C03 | Paid | 16 hours 57 minutes video plus 15–30 hours labs/review |
| Udemy / Neal Davis SCS-C03 | Paid | 11 hours 41 minutes video plus 15–30 hours exercises/review |
| Tutorials Dojo SCS-C03 study path and practice exams | Public guide; paid practice | 1–2 hours guide; 10–18 hours attempts and rationale review estimated |
| Whizlabs SCS-C03 labs/course/practice | Paid | About 12 hours for ten highlighted projects; 25–50 selected hours estimated total |

- **Official scope and practice:** Start with the [SCS-C03 guide](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03.html), [AWS live certification page](https://aws.amazon.com/certification/certified-security-specialty/), and [official 20-question set](https://explore.skillbuilder.aws/learn/course/external/view/elearning/9153/aws-certification-official-practice-question-sets-english). The question set is listed as 30 minutes on some catalog surfaces and 55 minutes on the current result; allow about an hour including explanations. Some full pretest/practice-plan items require Skill Builder subscription.
- **Current modular route:** [Pluralsight SCS-C03 Detection](https://www.pluralsight.com/courses/aws-scs-c03-detection) is **2 hours 16 minutes** and was updated July 2026. At this check, a complete stable six-domain path was not independently visible; add only published current modules and map them to the blueprint.
- **Detailed course:** [Udemy / Stéphane Maarek SCS-C03](https://www.udemy.com/course/ultimate-aws-certified-security-specialty/) is **16 hours 57 minutes**, 279 lectures, shown updated August 2026. Its title, introduction, description, and domain structure say C03, but one stale “what you'll learn” line still says C02; use the transition checklist.
- **Lab-oriented alternative:** [Udemy / Neal Davis SCS-C03](https://www.udemy.com/course/aws-certified-security-specialty-course/) is **11 hours 41 minutes**, 129 lectures, includes practical exercises and one practice exam, and was shown updated August 2026.
- **Study/practice route:** [Tutorials Dojo SCS-C03 study path](https://tutorialsdojo.com/aws-certified-security-specialty-scs-c03-exam-guide-study-path/) links current preparation and its premium practice set; the [free sampler](https://portal.tutorialsdojo.com/courses/free-aws-certified-security-specialty-practice-exams-sampler/) contains 20 questions in timed/review modes. Verify current C03 revision inside the purchased product because its catalog transitioned from C02 during late 2025.
- **Hands-on route:** [Whizlabs' ten SCS-C03 security projects](https://www.whizlabs.com/blog/aws-security-projects-scs-c03/) reports **about 12 hours** of lab work across Macie/KMS, detection, WAF, automation, and other domains; pair selected labs with its course/practice product only after confirming current totals and blueprint alignment.
- **Broad reference route:** Use the [AWS Security Documentation](https://docs.aws.amazon.com/security/) and service security chapters to resolve implementation gaps (**20–40 selected hours**, not end-to-end reading). Prefer current service documentation to memorized feature lists.

No exact current SCS-C03 O'Reilly book/course, MeasureUp product, or stable complete Pluralsight path was independently verified September 1. Do not substitute search results or recalled-question products for a product page with a visible current blueprint. A realistic plan is **120–180 hours** for an experienced AWS security engineer and **220–350 hours** if IAM/KMS, networking, logging, incident response, and multi-account governance are still developing.

---

## Source map and freshness notes

The root guide, six domain pages, in-scope list, and C02/C03 comparison define the assessment contract. The live certification page defines current price, delivery, language, and experience-summary metadata. Third-party courses are learning choices, not scope authorities.

- **VERIFY CURRENT:** exam delivery, blueprint revisions, in-scope services, service features/names, Organizations policy/root-access behavior, IAM/KMS evaluation details, supported Regions, quotas, pricing, training totals, and subscription access.
- **Stable decision pattern:** requirement/threat → trust and data boundary → least-privilege preventive controls → protected complete telemetry → validated finding → evidence-preserving containment → trusted recovery → control and detection improvement.
- **SCS-C02 material:** use for durable concepts only after closing every item in the transition checklist.

This guide uses no recalled exam questions or restricted content. The knowledge checks are original and test published concepts rather than reproducing vendor items.
