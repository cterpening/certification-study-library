---
exam_code: NSE-7-CLOUD-SECURITY
vendor_id: fortinet
official_blueprint: https://training.fortinet.com/local/staticpage/view.php?page=public_cloud_security_architect_exam
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Fortinet NSE 7 in Cloud Security Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live Cloud Security certification and Public Cloud Security 7.6.4 Architect exam pages, current Fortinet product documentation, and public AWS/Azure guidance were checked September 2, 2026. Fortinet's live pages remain authoritative.

**Current baseline:** Public Cloud Security 7.6.4 Architect, using FortiOS 7.6 and FortiWeb 7.4. Published domains are Security solutions deployment; Automation tools; Cloud infrastructure monitoring; and Troubleshooting. Fortinet does **not** publish weights for these domains, so this guide does not invent them.<br>
**Exam contract:** 35–40 questions, 75 minutes, English, Pearson VUE, pass/fail. It includes design scenarios, configuration extracts, and troubleshooting captures.<br>
**Certification contract:** This guide covers the NSE 7 Public Cloud Security Architect exam, not the whole track credential in isolation. Fortinet's current high-level program table and renewal language indicate NSE 4 plus NSE 5 or NSE 6 Cloud Security plus this exam; one sentence on the track page says NSE 4 **or** NSE 5 **or** NSE 6. Because those official statements conflict, confirm the exact prerequisite rule with Fortinet before planning or booking. Qualifying exams must be completed within two years, and the awarded credential is active for two years.<br>
**Experience boundary:** Fortinet recommends two years with Fortinet security solutions, two years with AWS, and two years with Azure.<br>
**Upcoming change:** No retirement or dated replacement was announced September 2, 2026. The current exam is Public Cloud Security **7.6.4** Architect; older FCSS Public Cloud Security 7.2/7.6 pages are not the current credential contract.<br>
**Integrity:** Use official samples only for form/scope. Reject leaked, recalled, “real exam,” guaranteed-match, or braindump material.

## How to use this guide

Build every answer from the native cloud path: account/subscription, region/AZ, identity, DNS, route tables, gateways/load balancers, security controls, Fortinet insertion, state/symmetry, inspection, application, logging, and return. Separate the cloud provider control plane, Fortinet management plane, and packet/data plane.

Use owned or explicitly authorized AWS/Azure sandboxes, synthetic applications, dummy data, short-lived least-privilege identities, budget alerts, and teardown automation. Record provider region, Fortinet image/build/license, FortiWeb version, infrastructure-code version, and architecture assumptions.

> **About related items:** A `Related item:` callout adds operations, architecture, governance, or lifecycle context. It supports practical understanding but is not claimed as a published exam objective.

## Blueprint map

| Domain | Published weight | Evidence of readiness |
|---|---:|---|
| Security solutions deployment | Not published | Explain and validate IaaS/CaaS protection and cloud-native integration |
| Automation tools | Not published | Repeatable, reviewed Terraform/Ansible/Bicep/CloudFormation deployment and rollback |
| Cloud infrastructure monitoring | Not published | Correlated AWS/Azure/Fortinet telemetry with known-event and silence detection |
| Troubleshooting | Not published | Isolate AWS/Azure connectivity and SDN-connector failures from live evidence |

## 1. Security solutions deployment

### Protect IaaS with deliberate insertion

Start with north-south, east-west, internet egress, remote-access, hybrid, and management flows. Select centralized transit, distributed VPC/VNet, gateway/load-balancer insertion, or another supported topology from scale, statefulness, symmetry, latency, availability, blast radius, operations, and cost. Draw every route before deploying.

FortiGate-VM sizing includes CPU/memory, interfaces, sessions, new connections, inspected throughput, logging, license, and failure capacity. Cloud autoscaling can add instances, but stateful traffic, bootstrapping, configuration distribution, health checks, route updates, warm-up, and scale-in draining determine whether applications survive.

On AWS, reason across VPC/subnet route tables, Internet/NAT/Transit Gateways, Gateway Load Balancer endpoints, security groups, NACLs, ENIs, source/destination checking, IAM, Availability Zones, and DNS. On Azure, include VNets/subnets, UDRs, Virtual WAN or hubs, load balancers, NAT Gateway, NSGs, NIC/IP forwarding, managed identities, availability zones/sets, and DNS.

> **Related item: symmetric state.** A route can be individually correct while forward and return traffic reach different stateful firewalls. Show both directions and every translation or load-balancing decision.

### Protect applications and CaaS

FortiWeb protects supported web/API traffic through deployment modes appropriate to the application and platform. Map origin, DNS, TLS termination, certificates, load balancers/ingress, client identity, HTTP behavior, health probes, WAF policy, logs, and fail-open/fail-closed decisions. Tune with synthetic and representative traffic; do not train adaptive controls blindly on attacks or incomplete samples.

Container-as-a-Service protection begins with cluster/control-plane responsibility, nodes/workloads, ingress/egress, services, images/registries, identities/secrets, network policy, API paths, and runtime visibility. Fortinet integration does not replace cloud IAM, workload hardening, image governance, Kubernetes controls, or backup/recovery.

FortiCNAPP provides cloud posture/workload-related visibility and risk capabilities under current packaging. Validate account onboarding, least-privilege read or enforcement roles, asset coverage, regions, scan cadence, findings, suppression, ownership, remediation, and offboarding. Do not assume a dashboard finding proves exploitability or that “no findings” means full coverage.

### Integrate cloud-native tools

SDN connectors import dynamic cloud metadata into policy. Define cloud account/tenant, API identity, permissions, region/subscription scope, filters/tags, polling/freshness, object lifecycle, quotas, HA, and failure behavior. Test new, changed, deleted, duplicate-tag, permission-loss, throttling, and stale-cache cases.

Cloud-native logging, eventing, secrets, key management, monitoring, and deployment services should have explicit trust and data paths. Protect API identities and tokens; prefer workload identity/managed roles over embedded long-lived keys.

> **Related item: shared responsibility.** Cloud providers secure underlying services; customers still own identities, routes, images, policy, data, Fortinet configuration, logging, and proof that controls cover intended assets.

## 2. Automation tools

### Use infrastructure as code as a controlled system

Terraform calculates desired-state changes using providers and state. Protect remote state, lock concurrent operations, pin reviewed versions, constrain provider credentials, validate plans, separate environments, detect drift, and test destroy/rollback implications. Modules should expose necessary inputs without hiding routing, IAM, or security assumptions.

Ansible performs agentless configuration/orchestration through inventories, variables, modules, and playbooks. Make tasks idempotent, protect vault/secrets, scope devices/accounts, use check/diff modes where meaningful, serialize high-risk changes, and verify runtime outcomes. Infrastructure provisioning and appliance configuration have different rollback behavior.

### Use native templates appropriately

Azure Bicep compiles declarative Azure Resource Manager deployments; AWS CloudFormation manages AWS stacks. Understand parameters, outputs, dependencies, conditions, modules/nested stacks, change previews, deployment/stack failure, deletion policies, and drift. Provider-native tools can simplify platform integration but do not automatically validate Fortinet behavior.

Build a pipeline with linting/static checks, policy checks, secret scanning, plan/change-set review, ephemeral tests, canary deployment, post-deployment traffic and logging tests, approval, artifact provenance, and rollback. Never run unreviewed downloaded templates with privileged credentials.

> **Related item: immutable evidence.** Retain sanitized commit, tool/provider/module versions, plan/change set, approval, deployment output, tests, exception, and rollback result so the environment can be reconstructed and audited.

## 3. Cloud infrastructure monitoring

### Correlate AWS and Azure signals

On AWS, correlate CloudTrail control-plane activity, VPC Flow Logs, CloudWatch metrics/logs/alarms, load-balancer/TGW/GWLB health and logs, GuardDuty or other enabled findings, DNS, and Fortinet telemetry. On Azure, correlate Activity Log, resource/platform logs, Network Watcher/connection troubleshooting, NSG flow telemetry where currently supported, Azure Monitor, load-balancer health, route/effective-security views, and Fortinet logs.

Metrics show quantities, logs show events, traces follow transactions, and configuration/state inventories show intended/current topology. Time synchronization, account/region/subscription identity, resource tags, schema, sampling, retention, encryption, and access determine whether correlation is credible.

FortiGate/FortiWeb/FortiCNAPP monitoring should cover management/API health, interfaces, routes, neighbors, sessions, inspected traffic, security events, license/update state, resource use, SDN-connector freshness, HA/scale, and log delivery. Alert on telemetry silence and inventory gaps.

### Turn telemetry into service evidence

For every critical flow, define synthetic checks, expected route/enforcement path, allowed/denied controls, latency/error objectives, and a known event traceable across provider and Fortinet systems. Dashboards without owners, thresholds, runbooks, and paging are visualization—not operations.

> **Related item: cost observability.** Cloud firewalls, gateways, logs, cross-zone/region transfer, public IPs, and retained telemetry can create material cost. Monitor unit cost and anomalous change alongside security and availability.

## 4. Troubleshooting

### Isolate AWS connectivity problems

Check source/destination DNS and addresses, ENIs, subnet/VPC route tables, longest-prefix target, TGW/GWLB/endpoint state, security groups, NACLs, source/destination checking, firewall policy/NAT/session/route, load-balancer target health, return path, MTU, and application listener. Use Reachability Analyzer or provider-supported diagnostics where applicable, flow logs, packet capture, and FortiGate runtime evidence.

For GWLB/service insertion, verify endpoint location, route direction, GENEVE/supporting path, health, appliance mode/state symmetry, cross-zone assumptions, scale events, and return. Do not “fix” by opening all security groups or bypassing inspection.

### Isolate Azure connectivity problems

Check effective routes/NSGs at source and destination, UDR next hop, IP forwarding, load-balancer rules/probes, HA ports where applicable, NAT behavior, VNet peering or Virtual WAN propagation, firewall NIC/session/route/policy, DNS, return, MTU, and application. Network Watcher evidence should be correlated with the appliance and application.

Azure health probes and load-balancer behavior can select or remove appliances, but probe success may not test the inspected application path. Avoid unsupported routing through the same interface or topology assumptions; validate current reference architectures.

### Diagnose SDN connectors

Separate API authentication/authorization, endpoint/region reachability, certificate/time, quota/throttling, resource discovery/filter/tag, polling/freshness, object update, policy reference, and traffic match. Rotate credentials or change permissions safely and prove deletion removes stale dynamic objects.

> **Related item: hypothesis discipline.** Predict which provider, Fortinet, and application evidence a suspected cause would produce. Change one variable, observe, and restore; avoid stacking guesses into a larger outage.

## Integrated scenarios

### Dual-cloud application

An application spans AWS and Azure with internet and private east-west traffic. Produce account/subscription and region boundaries, routing both directions, FortiGate insertion, FortiWeb/API protection, DNS/TLS, identity, IaC ownership, logs, capacity, cross-cloud connectivity, failover, data handling, cost, and rollback.

### Autoscaling brownout

Latency rises during scale-out, but instances report healthy. Correlate load-balancer target registration, bootstrap completion, config/content readiness, route/SDN-connector convergence, session distribution, CPU/throughput, logging, and application metrics. Prevent traffic until an appliance is functionally ready.

### Stale tag-based policy

A workload changed tags but retains unexpected access. Trace cloud API permissions, scope/filter, polling, throttling, cache/object state, policy reference, active sessions, logs, deletion, and fail-safe behavior. Fix the source and validate lifecycle rather than manually editing one dynamic member.

## Hands-on labs

Use isolated accounts/subscriptions, budgets, dummy data, least privilege, and explicit teardown. Confirm billable resources are removed after each lab.

1. Draw and validate north-south/east-west FortiGate insertion in an AWS VPC sandbox.
2. Draw and validate a hub/spoke Azure VNet path with UDRs, load-balancer health, symmetry, and return.
3. Publish a synthetic web app behind FortiWeb; test TLS, allowed traffic, one harmless blocked pattern, logging, and rollback.
4. Onboard a limited test account to FortiCNAPP; verify scope, missing region, finding ownership, and clean removal.
5. Implement a tag-based SDN connector policy; test create/change/delete, permission loss, throttling simulation, and stale handling.
6. Deploy one topology through Terraform and one native Bicep or CloudFormation template; save plans/change sets and post-tests.
7. Apply a small idempotent Fortinet change with Ansible; run it twice and compare device runtime state.
8. Trace a known allow and deny event through cloud flow/control logs and Fortinet logs; alert on deliberate pipeline silence.
9. Inject AWS and Azure route, security-control, health-probe, return-path, and connector faults one at a time.
10. Tear down through reviewed automation and verify resources, roles, public addresses, logs, state, and secrets are handled correctly.

## Readiness checks and answers

These are original prompts, not Fortinet exam questions.

| # | Check | Concise answer |
|---:|---|---|
| 1 | First cloud-firewall design artifact? | A bidirectional flow and route diagram with trust, translation, inspection, ownership, and failure points. |
| 2 | Why does symmetry matter? | Stateful devices must see the required directions/session state; asymmetric paths can drop or bypass inspection. |
| 3 | What drives FortiGate sizing? | Inspected throughput, sessions/connections, interfaces, logging, features, license, and capacity during failure/scale. |
| 4 | Does autoscaling guarantee resilience? | No; health, bootstrap/config readiness, state, routing, warm-up, draining, and failure capacity must work. |
| 5 | AWS route essentials? | Both-direction longest-prefix routes through the intended IGW/NAT/TGW/GWLB/endpoint/ENI path. |
| 6 | Azure route essentials? | Effective routes and UDR propagation/next hop, IP forwarding, load-balancer behavior, and both-direction return. |
| 7 | Security group versus NACL? | Security groups are stateful resource controls; NACLs are stateless subnet controls. Both can affect the path. |
| 8 | NSG role? | Azure stateful subnet/NIC filtering whose effective rules must be evaluated with routes and appliance policy. |
| 9 | What must WAF placement include? | DNS, TLS termination, client identity, load balancer/ingress, origin, health, policy, logging, and failure mode. |
| 10 | Does CNAPP replace native controls? | No; it adds posture/workload visibility and workflows while IAM, hardening, network and platform controls remain. |
| 11 | What proves CNAPP coverage? | Accounts/regions/assets, permissions, scan freshness, inventory reconciliation, findings, and missing-sensor alerts. |
| 12 | Main SDN connector risk? | Stale or incorrectly scoped cloud metadata can grant or remove access unexpectedly. |
| 13 | Best connector credential? | A least-privilege workload identity/role where supported, with rotation and audited scope. |
| 14 | Terraform state risk? | It can contain sensitive infrastructure data and coordinates changes; encrypt, restrict, lock, back up, and separate it. |
| 15 | Why review a plan? | It exposes intended create/change/delete operations before privileged mutation. |
| 16 | What makes Ansible safe to rerun? | Idempotent tasks, controlled inventory/variables, scoped credentials, check/diff, and outcome verification. |
| 17 | Bicep's role? | Declarative Azure resource deployment through ARM, with parameters/modules/dependencies and deployment history. |
| 18 | CloudFormation's role? | Declarative AWS stack lifecycle with parameters, change sets, dependencies, rollback, and drift considerations. |
| 19 | Does IaC prove the application path? | No; post-deployment traffic, policy, logging, failure, and rollback tests are still required. |
| 20 | Metrics versus logs? | Metrics aggregate quantities; logs record events/context. Both need configuration and topology context. |
| 21 | What is a known-event test? | Generate a harmless identifiable event and prove collection, parsing, correlation, search, alert, and retention. |
| 22 | Why alert on silence? | Missing telemetry can hide failure, coverage gaps, time/schema problems, or attack activity. |
| 23 | AWS troubleshooting order? | DNS/address, routes/gateways/endpoints, SG/NACL, load balancer, firewall session/policy/NAT, return, app. |
| 24 | Azure troubleshooting order? | DNS/address, effective route/NSG/UDR, forwarding/load balancer, firewall state, return, app. |
| 25 | What makes a health probe incomplete? | It may test only one listener or interface, not configuration readiness, inspection, routes, or the real app. |
| 26 | How troubleshoot connector emptiness? | Check identity/permissions, endpoint/region, filters/tags, quota, polling, object state, and policy reference. |
| 27 | Why not open all cloud controls temporarily? | It destroys diagnostic isolation and can create an exposed path; use narrow, timed, logged tests. |
| 28 | What is cloud shared responsibility? | Provider secures underlying cloud; customer owns configuration, identity, workloads/data, controls, and validation. |
| 29 | What is cost evidence? | Usage and unit-cost data for appliances, gateways, transfer, logs, IPs, and retained telemetry. |
| 30 | How handle secrets in evidence? | Redact values, protect artifacts, use references/managed stores, and rotate exposed credentials. |
| 31 | Does the blueprint publish domain weights? | No; do not invent them. |
| 32 | Current exam baseline? | 35–40 questions, 75 minutes, English; FortiOS 7.6 and FortiWeb 7.4. |
| 33 | Is the credential prerequisite wording fully consistent? | No; current official pages conflict, so verify directly with Fortinet before booking. |
| 34 | Why avoid old FCSS guides as contract authority? | They describe previous program identities/versions and may teach a retired credential path. |
| 35 | What should every fault exercise include? | Predicted evidence, one isolated fault, safe rollback, restored validation, and sanitized record. |
| 36 | Forbidden study content? | Leaked, recalled, braindump, guaranteed-match, or otherwise unauthorized questions. |

## Final preparation

- Recheck both the exam and track pages and resolve the prerequisite wording with Fortinet support before scheduling.
- Build one AWS and one Azure packet story from source to return, including native and Fortinet evidence.
- Re-run IaC from clean state, review the proposed changes, prove application/security outcomes, and tear down safely.
- Practice diagnosing route, health, IAM/API, SDN-connector, state/symmetry, and application failures without broad bypasses.

## Places to learn

This is not a complete list, and it is not a prescription to consume everything. Start with the official exam contract; then select only current documentation, cloud guidance, and labs that close measured gaps. Times are publisher-listed where visible or clearly labeled estimates.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Public Cloud Security Architect exam](https://training.fortinet.com/local/staticpage/view.php?page=public_cloud_security_architect_exam) | Public | 30–50 min | Current contract, exact unweighted objectives, products, experience, and official resources |
| [NSE 7 in Cloud Security](https://training.fortinet.com/local/staticpage/view.php?page=nse_7_cloud_security) | Public | 20–30 min | Track purpose, prerequisite language, validity, and recertification; verify noted inconsistency |
| [Fortinet Training Institute library](https://training.fortinet.com/local/library/?category=Certification%3ANSE_7+-+Cloud+Security) | Free account; labs/ILT may cost | 20–40 min selection; course varies | Locate current Public Cloud Security 7.6.4 Architect course and lab, avoiding older versions |
| [FortiGate Public Cloud documentation](https://docs.fortinet.com/product/fortigate-public-cloud) | Public | 20–35 hr selected AWS/Azure chapters/labs | Current reference architectures, deployment, routing, HA, automation, SDN connectors, and troubleshooting |
| [FortiWeb 7.4 documentation](https://docs.fortinet.com/product/fortiweb/7.4) | Public | 8–16 hr selected reading/labs | Web/API protection, deployment modes, certificates, policies, logging, HA, and troubleshooting |
| [FortiCNAPP documentation](https://docs.fortinet.com/product/forticnapp) | Public | 5–10 hr selected reading/labs | Account onboarding, inventory, posture/workload risks, permissions, findings, and operations |
| [AWS Well-Architected security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) | Public | 4–8 hr selected reading | Primary AWS design principles and shared-responsibility context |
| [Azure Architecture Center: security](https://learn.microsoft.com/en-us/azure/architecture/security/security-get-started) | Public | 4–8 hr selected reading | Primary Azure architecture patterns, identity, network, monitoring, and governance context |
| [Terraform documentation](https://developer.hashicorp.com/terraform/docs) | Public | 6–12 hr selected tutorials/labs | State, providers, modules, plans, lifecycle, automation, and safe workflow |
| [Ansible documentation](https://docs.ansible.com/ansible/latest/) | Public | 4–10 hr selected tutorials/labs | Inventory, variables, modules, playbooks, vault, idempotence, and validation |
| [Fortinet Training Institute policies](https://helpdesk.training.fortinet.com/support/solutions/73000238852) | Public | 30–60 min | Delivery, retake, result, voucher, integrity, and renewal policy |
