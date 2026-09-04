---
exam_code: 1Z0-1104-26
vendor_id: oracle
official_blueprint: https://mylearn.oracle.com/ou/learning-path/become-a-cloud-security-professional-2026/163254
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-04
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-04
---

# 1Z0-1104-26 Oracle Cloud Infrastructure Security Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide maps Oracle University's public 2026 learning-path scope checked September 4, 2026. It is unofficial and may contain errors. The [official OCI Security Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-a-cloud-security-professional-2026/163254) is authoritative.

**Assessment contract exposed by the current path:** Oracle Cloud Infrastructure Security Professional, exam 1Z0-1104-26, 90 minutes.<br>
**Published scope:** security principles; identity domains, IAM and workload principals; network and infrastructure security; WAF, TLS, Vault, encryption, secrets, and Data Safe; Cloud Guard, Security Zones, Vulnerability Scanning, Bastion, and Threat Intelligence; Audit, Logging, Events, Notifications, flow logs, Network Path Analyzer, automation, incident investigation, and forensics.<br>
**Source boundary:** the public path does not publish weights, question count, or passing score. **VERIFY CURRENT** in MyLearn before scheduling.

## How to use this guide

Analyze every control as asset and threat → trust boundary → preventive control → detective signal → response owner → recovery and retained evidence. Use only authorized tenancies and synthetic data for practice.

> **About related items:** A `Related item:` callout adds practical security-engineering context. It is supporting knowledge, not a claim that its wording appears in Oracle's published scope.

## Objective map

| Oracle-published skill group | Security question |
|---|---|
| OCI security foundations | Which responsibility, trust boundary, and layered principle applies? |
| Identity and access management | Who or what can perform which action, where, and under what condition? |
| Network and infrastructure security | Which paths are allowed, inspected, private, or explicitly denied? |
| Application and data security | How are applications, transport, keys, secrets, and sensitive data protected? |
| Cloud security posture | Which preventive or detective service finds and reduces material exposure? |
| Security operations | Which evidence supports triage, containment, remediation, recovery, and learning? |

## 1. Foundations and secure tenancy design

Apply shared responsibility, defense in depth, least privilege, segregation of duties, zero trust, and compartment isolation to concrete resources. Classify data and systems, identify owners, model threats, then select controls. A service feature is not a control until configured, monitored, and owned.

Separate production, security administration, logging, and recovery duties where risk warrants. Protect tenancy administrators and break-glass identities with strong authentication, limited use, alerts, and review.

## 2. Identity and access management

Design identity domains, federation, users, groups, administrator delegation, compartments, and policy inheritance. Parse policies by subject, verb, resource, scope, and condition. Use dynamic groups with instance principals and resource principals for workloads. Deny policies and tag-based access control add constraints but require careful interaction analysis.

Review credentials, tokens, keys, dormant users, group membership, and privileged activity. Test both allowed and denied paths. Avoid policy broadening as a first troubleshooting step.

## 3. Network and infrastructure security

Security lists and NSGs filter traffic; route tables and gateways create paths. Secure designs combine segmentation, minimal rules, private endpoints, Private Service Access, DRG controls, hybrid connectivity, Zero Trust Packet Routing, and OCI Network Firewall where inspection/policy is required.

Validate forward and return routes, DNS, stateful/stateless behavior, ports, sources, destinations, service endpoints, and logging. Bastion provides governed access to private resources; it does not justify permanent broad administration paths.

## 4. Application and data security

WAF policies apply protection rules, bot management, and rate limiting at application entry points. Certificates and load-balancer TLS termination require trusted chains, hostname coverage, protocol policy, and renewal ownership. Preserve end-to-end transport requirements when terminating or re-encrypting.

Vault manages keys and secrets; understand Oracle-managed versus customer-managed encryption, BYOK, HSM protection, and rotation. Data Safe supports database security assessment, activity auditing, discovery/masking, and user-risk work. Keep production data out of uncontrolled tests.

## 5. Posture and vulnerability management

Cloud Guard uses targets, detector recipes, problems, and responder recipes to surface and act on risky configurations/activity. Security Zones apply preventive recipes. Vulnerability Scanning assesses supported hosts and container images. Threat Intelligence enriches decisions; risk still needs asset and exposure context.

Prioritize findings by exploitability, privilege, exposure, sensitivity, and business impact. Validate automated responders in a limited scope and retain rollback and exception ownership.

## 6. Security operations and evidence

Audit records API activity; Logging collects service/custom logs; Events matches state changes; Notifications routes messages. VCN Flow Logs and Network Path Analyzer help explain network behavior. Correlate timestamps, principals, source addresses, resource IDs, request IDs, configuration changes, and alerts.

Define triage, severity, containment authority, evidence preservation, communications, eradication, recovery, and lessons learned. Automation should be bounded, idempotent where possible, and fail safely.

> **Related item:** Retention is part of detection design. A perfect query cannot recover evidence that was never enabled, centralized, time-synchronized, or retained long enough.

## Integrated practice scenarios

1. **Exposed database path:** Investigate a Cloud Guard problem, validate route/NSG evidence, preserve logs, restrict access, rotate secrets, and confirm recovery.
2. **Compromised workload:** Trace an instance principal, Audit events, Vault use, network flows, and object access; contain without deleting evidence.
3. **Public application abuse:** Tune WAF rules and rate limits, protect TLS keys, correlate load-balancer/application logs, and handle false positives with expiry.

## Hands-on labs

1. Threat-model a three-tier OCI workload and map preventive, detective, responsive, and recovery controls.
2. Build least-privilege human and dynamic-group policies; test expected denials.
3. Trace and restrict a network path with routes, NSGs, flow evidence, and a private endpoint.
4. Configure a synthetic WAF policy and document safe rollout, false-positive, and rollback tests.
5. Create a Vault key/secret rotation plan and prove no secret appears in code, state, or logs.
6. Compare Cloud Guard, Security Zones, Vulnerability Scanning, Bastion, and Threat Intelligence for five findings.
7. Correlate Audit, Logging, Events, Notifications, and flow logs into an incident timeline.
8. Run a tabletop containment/recovery exercise and verify evidence retention and exception closure.

## Original readiness checks

1. Shared responsibility? 2. Defense in depth? 3. Least privilege evidence? 4. Segregation-of-duties example? 5. Policy inheritance risk? 6. Dynamic-group purpose? 7. Instance versus resource principal? 8. Deny-policy caution? 9. TBAC dependency? 10. Route versus NSG? 11. Private endpoint value? 12. ZPR intent? 13. Network Firewall role? 14. WAF versus NSG? 15. TLS termination concern? 16. BYOK meaning? 17. HSM value? 18. Data Safe purpose? 19. Cloud Guard versus Security Zones? 20. Detector versus responder recipe? 21. Vulnerability finding priority? 22. Audit versus flow log? 23. Evidence-preservation rule? 24. What makes automation safe? 25. What remains unpublished? 26. What proves readiness?

### Answer guide

1. Provider/customer duties vary by service. 2. Multiple independent layers. 3. Required action succeeds and broader action fails. 4. Different identities approve and execute sensitive change. 5. Parent grants may affect children. 6. Group resources by matching rules for policy. 7. Compute-instance identity versus supported service/resource identity. 8. Interactions can block required operations. 9. Correct, governed tags and conditions. 10. Path selection versus traffic permission. 11. Avoid public exposure. 12. Policy-directed packet routing based on trust attributes. 13. Central inspection and network policy. 14. HTTP application protection versus network traffic rules. 15. Certificate, protocol, backend encryption, and renewal ownership. 16. Bring your own key. 17. Strong protected key boundary. 18. Database security posture, auditing, discovery/masking, and user risk. 19. Detective response versus preventive enforcement. 20. Detection logic versus automated action. 21. Exploitability plus exposure, privilege, asset, and impact. 22. API/control activity versus network-flow metadata. 23. Preserve before destructive containment where possible. 24. Scoped, tested, observable, reversible, and owned. 25. Weights, count, and score. 26. Correct layered controls plus evidence-led incident decisions.

## Readiness checklist

- I can prove least privilege for human and workload identities with positive and negative tests.
- I trace network, application, data, and key trust boundaries end to end.
- I distinguish preventive controls, findings, telemetry, automation, and recovery.
- I can build an incident timeline without destroying or overclaiming evidence.

## Places to learn

This is a selective learning path, not a complete list of OCI security resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official OCI Security Professional learning path](https://mylearn.oracle.com/ou/learning-path/become-a-cloud-security-professional-2026/163254) | Oracle account/subscription may be required | **23+ hours** as published by Oracle University |
| [OCI IAM security guidance](https://docs.oracle.com/en-us/iaas/Content/Security/Reference/iam_security.htm) | Public | **8–12 hours** plus linked service guidance |
| Eight labs in this guide | Authorized OCI tenancy and synthetic data | **24–36 hours** plus two timed incidents |
