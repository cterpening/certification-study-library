---
exam_code: CISA
vendor_id: isaca
official_blueprint: https://www.isaca.org/credentialing/cisa/cisa-exam-content-outline
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Certified Information Systems Auditor (CISA) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The current ISACA job-practice outline, 2026 candidate guide, certification and maintenance requirements, official preparation products, and selected independent resources were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#cisa-coverage-record).

**Current baseline:** Information Systems Auditing Process (18%); Governance and Management of IT (18%); Information Systems Acquisition, Development, and Implementation (12%); Information Systems Operations and Business Resilience (26%); Protection of Information Assets (26%). ISACA identifies this outline as effective August 2024.<br>
**Exam contract:** 150 multiple-choice questions in four hours, delivered at PSI test centers or by remote proctoring. Registration is continuous; eligibility lasts six months. The 2026 candidate guide lists US$575 for members and US$760 for nonmembers. Verify the live registration flow, appointment availability, identification, retake, language and price rules before purchase.<br>
**Certification contract:** Anyone may take the exam. To use the CISA designation, pass within the preceding five years, apply and pay the US$50 processing fee, and document at least five years of qualifying information-systems audit, control or security experience gained within the ten years before application. Check the current application for any permitted waivers; do not assume that passing the exam alone makes you CISA certified.<br>
**Maintenance:** ISACA currently requires at least 20 relevant CPE hours each year and 120 over three years, the annual maintenance fee, ethics, audit cooperation, and compliance with ISACA auditing standards. A revised CPE framework takes effect January 1, 2027; verify the current policy when planning renewals.<br>
**Upcoming change:** No replacement CISA outline or retirement was announced on September 2, 2026. Technology and regulation examples change faster than the job-practice model, so recheck the official outline and candidate guide before scheduling.<br>
**Integrity:** Use ISACA's own free quiz and QAE products for official item style. The 40 prompts here are original retrieval and reasoning checks—not recalled, live, or predicted exam questions.

## How to use this guide

Start with the five-domain map and diagnose your gaps. Learn the audit decision sequence rather than memorizing isolated controls: understand the business objective, establish authority and scope, assess risk, choose suitable procedures and samples, obtain sufficient reliable evidence, evaluate design and operating effectiveness, communicate findings, and follow remediation without assuming management's responsibility.

For every topic, practice three views: what management should design, what operators should do, and what an independent auditor should verify. ISACA questions commonly reward the action that is most risk-based, appropriately authorized, evidence-led, and useful to the business—not necessarily the most technical response.

> **About related items:** A `Related item:` callout adds architecture, security, operations, governance, or lifecycle context. It makes the published objective more useful in real work but does not imply that the extra phrase appears verbatim in the official outline.

## Blueprint map

| Domain | Weight | Evidence to produce |
|---|---:|---|
| Information Systems Auditing Process | 18% | Risk-based audit plan, defensible procedure/sample, evidence trail, finding and follow-up record |
| Governance and Management of IT | 18% | Strategy/structure/control evaluation tied to enterprise objectives, risk and accountability |
| Acquisition, Development, and Implementation | 12% | Lifecycle assurance plan with requirements, controls, testing, migration and postimplementation evidence |
| Operations and Business Resilience | 26% | Operational control assessment plus tested continuity/recovery evidence |
| Protection of Information Assets | 26% | Layered identity, infrastructure, data and incident-control assessment |

## 1. Information Systems Auditing Process (18%)

### Establish authority, independence, and a risk-based plan

An audit charter establishes purpose, authority, responsibility, position and access. The audit universe identifies auditable entities; risk assessment helps select and prioritize engagements. An engagement letter or equivalent defines objective, scope, timing, responsibilities and reporting expectations. Preserve organizational and professional independence, disclose impairments, apply due professional care, and use competent staff. Management owns risk and controls; internal audit provides assurance and advice without quietly becoming the control owner.

Translate the business process into objectives, risks and controls. Understand inherent risk before controls and residual risk after them. Consider likelihood, impact, regulatory obligations, previous findings, material change, fraud, third parties and reliance on automated controls. Define materiality and tolerable error in context. An audit program converts scope into procedures, evidence needs, ownership and schedule; it should be adaptable when evidence changes the risk view.

Distinguish audit types and assurance objectives. Compliance work tests against criteria. Financial, operational, integrated, privacy, security, cloud, supplier and project audits ask different questions. A control self-assessment can improve ownership but is not independent assurance. Continuous auditing is an assurance approach; continuous monitoring is management's operating responsibility.

**Related item: the three-lines model.** Operational management owns and manages risk, oversight functions provide expertise and monitoring, and internal audit provides independent assurance. Names vary, but blurred accountability can make evidence appear stronger than it is.

### Execute procedures and evaluate evidence

Test design first: if a control, as described, cannot address the risk, transaction testing cannot rescue the design. Then test implementation and operating effectiveness over a representative period. Inquiry is useful but weak alone. Observation shows one moment. Inspection and reperformance usually provide stronger evidence. Evidence quality depends on sufficiency, relevance, reliability, authenticity and chain of custody—not file count.

Choose sampling to match the assertion. Statistical sampling permits quantified selection risk; nonstatistical sampling still requires a defensible method. Attribute sampling tests occurrence of a control or characteristic; variable sampling estimates amounts. Define population, sampling unit, expected error, tolerable error, confidence and treatment of exceptions before interpreting results. A convenience sample is rarely representative. Computer-assisted audit techniques and data analytics can examine full populations, but incomplete extraction, duplicate records, wrong joins, timestamps or misunderstood fields can produce confidently wrong conclusions.

Maintain workpapers so another competent auditor can understand objective, source, procedure, result, reviewer and conclusion. Protect sensitive evidence, preserve versions, record limitations and resolve contradictory evidence. A finding normally connects condition (what exists), criteria (what should exist), cause, effect/risk and recommendation. Validate facts with the process owner without surrendering auditor judgment.

### Report, follow up, and improve

Prioritize findings by business risk, not technical drama. The report should state objective, scope, period, approach, limitations, conclusions, findings, management response, owner and target date. Escalate scope limitations, evidence obstruction, significant control failure or accepted risk through the approved governance route. Recommendations should address causes and outcomes while allowing management to choose an appropriate implementation.

Follow-up verifies evidence of remediation and whether residual risk is now acceptable; a ticket marked closed is not proof. Track overdue actions and formally accepted exceptions. Quality assurance covers supervision, workpaper review, conformance, metrics, stakeholder feedback and improvement of the audit function itself.

**Related item: audit analytics engineering.** Treat extracts and tests like production data work: immutable inputs, documented transformations, validation totals, peer review, version-controlled logic and reproducible outputs.

## 2. Governance and Management of IT (18%)

### Connect enterprise direction to accountable IT decisions

Governance evaluates stakeholder needs and sets direction and oversight; management plans, builds, runs and monitors within that direction. Evaluate whether IT strategy traces to enterprise objectives, risk appetite and measurable value. Boards and executives need decision-quality reporting: outcomes, exposure, dependencies, trends and exceptions—not only activity counts.

Examine organization design, reporting lines, committees, decision rights, segregation of duties, skills, succession and performance. Policies state intent and mandatory direction; standards define required specifications; procedures describe execution; guidelines advise. Documents need owners, approval, versioning, communication, exceptions and review. Enterprise architecture should connect business, data, application and technology states with standards and roadmaps instead of becoming an unused diagram collection.

Enterprise risk management integrates technology risk into a common business portfolio. Privacy, data governance, records, legal, regulatory and contractual requirements should be assigned to owners and translated into controls. Classification considers sensitivity, criticality, ownership, handling, retention and disposal—not confidentiality alone.

### Assess resources, suppliers, performance, and quality

Resource management balances people, information, applications, infrastructure, facilities, budget and capacity. Portfolio governance should authorize work using value, risk, dependencies and resource constraints. Benefits need named owners and post-delivery measurement. Metrics should connect leading indicators, control performance and business outcomes; averages can hide severe exceptions.

Third-party governance begins before contract signature. Assess criticality, concentration, data flows, locations, subcontractors, security and resilience. Contracts should express service, security, privacy, audit, incident, continuity, change, data-return and exit requirements. Reports and certifications are inputs, not universal assurance; map their scope, period, control ownership, subservice organizations and exceptions to your actual use.

Quality management defines how products and services meet requirements. Quality assurance evaluates process; quality control detects defects in outputs. Independently assess whether service levels measure user-relevant outcomes and whether incentives encourage undesirable behavior.

**Related item: responsible technology governance.** Cloud, automation and AI do not remove accountability. Inventory services/models, assign owners, constrain data use, validate outputs, monitor drift and preserve an exit path.

## 3. Information Systems Acquisition, Development, and Implementation (12%)

### Govern the investment and delivery lifecycle

Evaluate the business case for problem, options, costs, benefits, risk, assumptions, dependencies and measurable ownership. Feasibility covers technical, economic, legal, operational and schedule concerns. Project governance needs sponsor, accountable owner, scope, milestones, risk/issues, quality, change control and benefit tracking. Agile changes the delivery cadence, not the need for authorization, traceability, security or evidence.

Requirements should be testable and trace to business and control objectives. Embed privacy, security, availability, audit logging, accessibility, records and segregation of duties early. For acquired or SaaS solutions, assess configuration responsibility, integration, data portability, vendor viability, customization debt and exit. For internally developed systems, review repositories, branching, peer review, dependency management, build integrity, secrets, environments and deployment approvals.

### Test, migrate, release, and verify outcomes

Separate unit, integration, system, performance, security, usability, regression and user-acceptance purposes. Test data and environments need protection and representativeness. Defects need severity, ownership, retest and accepted-risk evidence. User acceptance confirms business fitness; it does not replace technical or security testing.

Configuration, change and release management maintain authorized, tested, traceable baselines. Emergency changes need expedited authorization plus retrospective review. Data conversion should include mapping, cleansing, reconciliation totals, exception handling, ownership and rollback. Parallel, phased, pilot and direct cutover strategies trade speed, cost and recoverability differently.

A postimplementation review asks whether requirements, controls, performance, cost and benefits were achieved and whether lessons are acted on. It is not merely project closure. Confirm operational ownership, documentation, training, support, monitoring and decommissioning of replaced components.

**Related item: software supply-chain assurance.** Build provenance, signed artifacts, dependency inventories, isolated pipelines and promotion evidence extend traditional change control into modern delivery.

## 4. Information Systems Operations and Business Resilience (26%)

### Assure reliable operations

Understand how compute, networks, operating systems, databases, middleware, storage, virtualization, cloud and end-user computing support the service. Asset records need owner, location, classification, support state and disposal evidence. Shadow IT creates ungoverned data, identity, continuity and supplier risk; discovery should lead to proportionate governance, not automatic shutdown.

Evaluate job scheduling, interfaces and automation for completeness, ordering, restart, exception and reconciliation. Availability and capacity planning use workload, dependency, threshold and growth evidence. Incident management restores service; problem management seeks root cause; change controls risk in modifications; configuration management maintains relationships and baselines; release management packages deployment. Similar terms must not be collapsed.

Logs need synchronized time, protected collection, retention, access and review. Service-level agreements define customer/provider commitments; operational-level agreements and underpinning supplier contracts support them. Database controls cover authorization, schema and change, integrity, backup, encryption, monitoring and privileged activity.

**Related item: observability versus assurance.** A green dashboard proves only that its selected signals met thresholds. Audit monitoring coverage, blind spots, alert routing, synthetic tests and recovery evidence.

### Connect business impact to continuity and recovery

The business impact analysis identifies critical processes, dependencies, maximum tolerable disruption and recovery priorities. Recovery time objective is the target time to restore; recovery point objective is tolerable data-loss time. These are business requirements, not values invented by IT. Maximum tolerable downtime constrains strategy; work-recovery time accounts for validation and backlog after technology returns.

Business continuity sustains prioritized operations; disaster recovery restores technology. Strategies may include alternate work methods, redundant regions/sites, manual procedures, suppliers, communications and crisis governance. Cold, warm and hot arrangements differ in readiness and cost; cloud multi-zone design is not automatically multi-region recovery.

Backups require scope, frequency, retention, isolation, encryption, access, integrity and restore testing. Replication can copy corruption or ransomware. A successful backup job is not a proven recovery. Test plans through walkthroughs, tabletop exercises, simulations, component tests and appropriately governed full exercises. Record objectives, assumptions, participants, evidence, gaps and remediation.

**Related item: dependency-aware recovery.** Restore identity, keys, DNS, networks, data and applications in the order needed for an end-to-end business transaction, then reconcile data and resume normal processing.

## 5. Protection of Information Assets (26%)

### Evaluate the layered control system

Start with policy, risk and asset/data classification. Physical and environmental controls address site access, surveillance, power, fire, water, temperature and media. Identity controls span joiner/mover/leaver lifecycle, authentication, federation, authorization, privileged access, service identities, recertification and monitoring. Least privilege and segregation of duties require actual entitlement and activity evidence, not policy text.

Network and endpoint security combine architecture, segmentation, secure configuration, patching, malware defenses, encryption, monitoring and controlled administration. Understand preventive, detective, corrective, deterrent, compensating and recovery roles. Data-loss prevention detects/enforces defined handling patterns but needs accurate classification and exception governance. Cryptography choices depend on confidentiality, integrity, authenticity, nonrepudiation, key lifecycle and performance. PKI joins identities, certificates, trust chains, revocation and protected private keys.

Cloud and virtualization require a shared-responsibility map for identity, configuration, data, workloads, logs, continuity and provider dependencies. Mobile, wireless and IoT add device identity, constrained patching, unsafe defaults, physical exposure and lifecycle concerns. Validate secure baselines, exceptions and drift across the real population.

### Assess security monitoring and incident handling

Threat and vulnerability management distinguish threat intelligence, discovery, validation, prioritization, remediation and accepted risk. Scanning cannot prove exploitability or business impact by itself. Penetration tests demonstrate selected attack paths under scope; they do not certify the absence of vulnerabilities. Control testing should combine configuration, activity, exception and outcome evidence.

Security monitoring needs relevant sources, parsing, time, protected retention, use cases, tuning, ownership and response. Incident response prepares roles, classification, evidence, communications, legal/privacy involvement, containment, eradication, recovery and lessons learned. Preserve chain of custody and forensic soundness when investigation may support legal or disciplinary action. Premature remediation can destroy evidence; delayed containment can increase harm—follow the authorized incident structure.

Awareness should be role- and risk-specific, reinforced, measured and improved. Completion rate is not behavior change. Report control gaps with business impact and accountable action rather than substituting fear for evidence.

**Related item: control inheritance.** A provider, platform or shared service may operate a control, but the consuming organization still must verify scope, configure its portion and monitor exceptions.

## Integrated scenarios

### Scenario 1 — Payroll SaaS assurance

The organization is replacing payroll with SaaS. Trace objectives through data classification, supplier due diligence, contract clauses, federation and privileged access, configuration/change controls, conversion reconciliation, UAT, logging, resilience, exit and postimplementation benefits. Identify which controls belong to the provider, customer or both. Design samples for user lifecycle and payroll changes, validate report scope, and report any inability to obtain sufficient evidence.

### Scenario 2 — Ransomware recovery claim

Management reports that recovery is “green” because backups complete nightly. Obtain the BIA, RTO/RPO, dependency map and incident history. Inspect immutability and privileged access, select backup jobs and exceptions, observe or reperform restores, recover an end-to-end business transaction, reconcile it, and compare measured results with objectives. Report replication, identity/key, supplier and communication gaps separately from backup success.

### Scenario 3 — Continuous-access audit

Build an authorized analytic for privileged access across HR, identity and target-system data. Validate population completeness, timestamps and join keys; define expected transfers and terminations; investigate exceptions; sample approvals and actual activity; protect workpapers; and have a reviewer reproduce the result. Escalate systemic feed gaps before presenting a false full-population conclusion.

## Eight practical labs

1. **Audit charter and universe:** draft a one-page charter and rank ten auditable entities by explicit impact, change, control and evidence factors. Record assumptions and independence threats.
2. **Procedure and sample:** define one control objective, population, procedure, sampling unit, sample method, tolerable exception and conclusion rule. Use synthetic records.
3. **Reproducible analytics:** create a small synthetic user/access/change dataset, reconcile row/control totals, test one exception rule, preserve immutable input and have another person or fresh environment rerun it.
4. **Supplier assurance:** map a public assurance report or fictional provider evidence pack to five customer requirements; identify scope, period, exceptions, complementary controls and gaps.
5. **Release traceability:** in a sandbox repository, connect requirement → risk/control → change → review → test → artifact → deployment approval → rollback evidence.
6. **Operations walk-through:** diagram one service from identity and DNS through application and database. Add owners, monitoring, failure modes, incident/problem/change/configuration handoffs and supplier dependencies.
7. **Restore proof:** back up a disposable application and data set, simulate loss, restore in dependency order, measure RTO/RPO, validate a transaction and record lessons. Never disrupt a production service.
8. **Security-control assessment:** assess a nonproduction identity or endpoint baseline using design, configuration, population, exception, activity and monitoring evidence; write one five-part finding.

## 40 readiness checks

1. What document authorizes internal audit and its access?
2. Why must management, rather than audit, own a control?
3. How do inherent and residual risk differ?
4. When is a scope limitation significant enough to escalate?
5. Why is inquiry alone usually insufficient evidence?
6. What must be known before selecting an audit sample?
7. How do attribute and variable sampling differ?
8. Which validation proves a data extract represents the source population?
9. What makes a workpaper reproducible?
10. Can you write condition, criteria, cause, effect and recommendation separately?
11. How does governance differ from management?
12. Which evidence shows IT strategy supports enterprise objectives?
13. How do policy, standard, procedure and guideline differ?
14. What makes an enterprise architecture operationally useful?
15. Which supplier-report limitations matter to your exact service?
16. What contract terms support incident response and exit?
17. Why can an activity metric misstate business value?
18. How should accepted risk and policy exceptions be governed?
19. What makes a business case auditable after implementation?
20. Why does Agile not remove control traceability?
21. Which test type demonstrates business fitness?
22. What evidence supports complete data conversion?
23. When is parallel cutover preferable to direct cutover?
24. What does a postimplementation review test beyond project closure?
25. How do incident and problem management differ?
26. How do change, configuration and release management interact?
27. Why is a successful backup job not recovery evidence?
28. Who should set RTO and RPO, and from what analysis?
29. How can replication weaken ransomware recovery?
30. What must an end-to-end recovery test include?
31. Which evidence proves least privilege operates in practice?
32. Why is a vulnerability scan not a risk conclusion?
33. What assurance does a penetration test provide—and not provide?
34. Which PKI controls protect trust beyond encryption algorithms?
35. How does shared responsibility change a cloud audit procedure?
36. What makes security log evidence reliable?
37. When should evidence preservation precede containment?
38. How would you measure awareness beyond completion?
39. What must be true before relying on an inherited control?
40. Can you choose the next audit action from risk, authority and evidence rather than technical preference?

## Places to learn

This is not a complete list, and it is not meant to be consumed end to end. Pick the format and chapters that close your measured gaps, practice the decision process, then return to the official outline. Durations are publisher-listed or practical estimates checked September 2, 2026; catalogs, prices and access change.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [ISACA CISA exam content outline](https://www.isaca.org/credentialing/cisa/cisa-exam-content-outline) | Public | 30–60 min | Canonical five-domain map and final scope check |
| [ISACA certification exam candidate guide](https://www.isaca.org/credentialing/-/media/fa494652c5f149289af38cef18328650.ashx) | Public PDF | 60–90 min | Delivery, policies, and detailed August 2024 outline |
| [ISACA CISA Online Review Course](https://www.isaca.org/training-and-events/online-training/online-review-courses) | Paid | 20–30 hr estimated | Official self-paced instruction across 40+ modules; ISACA does not state one seat time |
| [ISACA CISA QAE Database](https://www.isaca.org/store/items/xmxca1712m) | Paid, six months | 25–45 hr estimated | Explanation-led use of the 1,070-question pool and three timed practices |
| [Free official CISA practice quiz](https://www.isaca.org/credentialing/cisa/cisa-practice-quiz) | Public/form | 15–25 min | Small official item-style sample, not a readiness score |
| [Pluralsight CISA 2024 path](https://www.pluralsight.com/paths/cisar-certified-information-systems-auditorr-2024) | Paid/trial | 20 hr | Eleven-course path and practice exam aligned to the 2024 job practice |
| [O'Reilly CISA video course](https://www.oreilly.com/videos/cisa-certified-information/9781836209119/) | Paid | 26 hr 39 min | Selected explanations and demonstrations; recheck current policy and technology |
| [LinkedIn Learning CISA Cert Prep](https://www.linkedin.com/learning/isaca-certified-information-systems-auditor-cisa-cert-prep-44731094) | Paid/trial | 7 hr 10 min | Concise June 2026 pass across all five domains |
| [Udemy Masterclass — CISA Exam (Updated 2026)](https://www.udemy.com/course/masterclass-cisa-exam/) | Paid | 22 hr 50 min | Accessible domain instruction; keep official outline/QAE authoritative |
| [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) | Public | 1–2 hr selected | Outcome and governance criteria context |
| [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) | Public | 2–4 hr selected | Control and assessment context, not blueprint memorization |
| [CISA certification requirements](https://www.isaca.org/credentialing/cisa/get-cisa-certified) | Public | 10–15 min | Exam-versus-designation and application rules |
| [CISA maintenance requirements](https://www.isaca.org/credentialing/cisa/maintain-cisa-certification) | Public | 15–20 min | Current CPE, fee, audit and status duties |
| [2027 CPE change](https://www.isaca.org/credentialing/cpe-2027) | Public | 10 min | Plan the January 2027 maintenance transition |

Use only authorized practice material. Reject products advertised as dumps, recalled questions, “actual exam” files, exact-match simulations, or guaranteed passes.
