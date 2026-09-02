---
exam_code: CISM
vendor_id: isaca
official_blueprint: https://www.isaca.org/credentialing/cism/cism-exam-content-outline
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-02
---

# Certified Information Security Manager (CISM) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The current and scheduled-change statements, 2026 candidate guide, certification and maintenance requirements, official preparation products, and selected independent sources were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#cism-coverage-record).

**Current baseline through November 2, 2026:** Information Security Governance (17%); Information Security Risk Management (20%); Information Security Program (33%); Incident Management (30%). The candidate guide identifies this job practice as effective 2022.<br>
**Scheduled change:** ISACA says a new CISM Exam Content Outline takes effect **November 3, 2026**, with updated preparation material available in September. The public outline checked September 2 still displayed the 2022 domains and weights and did not expose replacement weights. Do not infer them. Schedule against the version you intend to take, and re-download the outline before buying materials.<br>
**Exam contract:** 150 multiple-choice questions in four hours through PSI test centers or remote proctoring. Registration is continuous, eligibility lasts six months, and the candidate guide lists US$575 member/US$760 nonmember pricing. Verify live policies, identity, appointment and retake rules.<br>
**Certification contract:** Anyone may sit the exam. The designation requires a pass within five years, US$50 application, verified five or more years of professional information-security management experience across at least three of the four job-practice domains, gained within the ten years before application, plus ethics and maintenance obligations. Passing alone is not CISM certification.<br>
**Maintenance:** At least 20 relevant CPE hours annually and 120 over three years, annual fee, ethics and audit cooperation. ISACA's revised CPE framework begins January 1, 2027.<br>
**Integrity:** Use the official free quiz and QAE product for ISACA item style. The checks here are original management-reasoning prompts, not representations of live questions.

## How to use this guide

Study from enterprise objectives outward. A CISM-level answer assigns accountability correctly, frames information-security risk in business terms, recommends an appropriately governed program, communicates to the right decision maker, and prepares the enterprise to manage incidents. Avoid the reflex that the newest technical control is always best. Ask first: who owns this decision, what outcome and risk appetite apply, what evidence exists, and what sequence protects value?

Create one portfolio scenario and carry it through all four domains: governance charters the direction, risk analysis prioritizes action, the program implements and measures capabilities, and incident management exercises and improves them.

> **About related items:** A `Related item:` callout adds architecture, security, operations, governance, or lifecycle context. It makes the published objective more useful in real work but does not imply that the extra phrase appears verbatim in the official outline.

## Blueprint map

| Domain | Weight | Evidence to produce |
|---|---:|---|
| Information Security Governance | 17% | Board-aligned strategy, governance model, policy hierarchy, business case and decision reporting |
| Information Security Risk Management | 20% | Repeatable assessment, owned response, residual-risk decision and monitoring route |
| Information Security Program | 33% | Prioritized roadmap, resources, control lifecycle, third-party integration and outcome metrics |
| Incident Management | 30% | Tested readiness, classification/escalation, coordinated response, recovery and improvement evidence |

## 1. Information Security Governance (17%)

### Establish enterprise accountability

Corporate governance sets enterprise direction and accountability; information-security governance ensures security supports it. The board or equivalent governing body retains oversight. Executive management allocates authority and resources. Business/process and information owners accept or escalate risk. The security manager advises, coordinates and reports; control operators execute; assurance functions independently evaluate. A steering committee can coordinate priorities but must not obscure accountable owners.

Understand culture, ethics, legal/regulatory/contractual obligations and organizational structure. Culture shapes whether people escalate problems, work around controls or treat security as an enabler. Identify jurisdictions, contracts, industry requirements, privacy duties and records obligations, then assign interpretation to competent legal/compliance owners. Security translates requirements into policies and controls; it should not invent legal conclusions.

A governance framework defines decision rights, roles, policy authority, oversight, reporting and escalation. Policies express mandatory direction; standards define required specifications; procedures implement them; guidelines advise. Exceptions require documented scope, reason, compensating controls, owner, approval, expiration and review.

**Related item: risk ownership.** The security function can explain exposure and recommend treatment, but the accountable business owner accepts residual business risk within delegated authority. Material exceptions above tolerance escalate rather than disappear into a security backlog.

### Build an aligned strategy and business case

Derive security vision, objectives and principles from enterprise mission, strategy, risk appetite, architecture, obligations and current capability. Assess people, process, technology and third parties. Define target capability and a prioritized roadmap with dependencies, resources, measures and review triggers. A strategy should be stable enough to guide decisions but adaptable to acquisitions, regulation, threats and technology.

A business case connects an initiative to business outcome, options, total lifecycle cost, benefit, risk reduction, dependencies, assumptions and accountable owner. Quantitative estimates are useful when inputs are transparent; false precision is not. Present alternatives—including accepting or transferring risk—and the consequence of deferral.

Communicate differently by audience. Boards need business exposure, decision, trend and confidence. Executives need cross-functional dependencies and resources. Operators need actionable requirements. Metrics should show outcomes and exceptions, not only volume. A rising incident count may reflect worse attacks, better detection or reporting change; explain the denominator and context.

**Related item: AI and emerging-technology governance.** Inventory systems and models, classify data/use cases, assign owners, constrain acceptable use, evaluate suppliers, test outputs, monitor drift/abuse and maintain human authority over material decisions.

## 2. Information Security Risk Management (20%)

### Identify and assess meaningful scenarios

Risk is uncertainty affecting objectives. Build scenarios that name asset/process, threat, vulnerability or exposure, event and business impact. Distinguish threats from vulnerabilities, and control deficiencies from realized incidents. Use business impact analysis, threat intelligence, architecture, incidents, audit findings, supplier information and vulnerability data without mistaking any single feed for a complete risk assessment.

Define scope, context, criteria and assumptions. Risk appetite is the broad amount/type of risk the enterprise is willing to pursue or retain; tolerance sets acceptable variation around objectives. Inherent risk is before considered controls; residual risk remains afterward. Likelihood and impact may be qualitative, quantitative or hybrid. Consistency, traceability and decision usefulness matter more than decorative numbers.

Prioritize vulnerabilities by exploitability, exposure, asset criticality, existing controls and impact—not score alone. Emerging risk requires horizon scanning and explicit uncertainty. Bias, stale inventories and optimistic control claims should be challenged. Validate who supplied inputs and when they remain valid.

### Choose, own and monitor response

Responses include avoid, mitigate/reduce, transfer/share and accept. A treatment plan needs owner, action, resources, target, interim exposure and success criteria. Control owners operate controls; risk owners decide whether residual exposure is acceptable. Acceptance must sit within delegated authority and expire or be reviewed when assumptions change.

Select controls using requirements, risk reduction, feasibility, cost, usability, dependencies and control interaction. Preventive, detective, corrective, deterrent, compensating and recovery controls form a system. A compensating control should meet the original objective sufficiently, not simply exist nearby.

Maintain a risk register with scenario, owner, assessment, controls, response, residual risk, status, review trigger and decision history. Key risk indicators warn about exposure; key control indicators show control health; key performance indicators show execution or outcome. Thresholds need owners and action. Report trends, concentrations and out-of-tolerance decisions with uncertainty visible.

**Related item: aggregation and concentration.** Individually acceptable supplier, identity or regional risks can combine into material enterprise exposure. Model shared dependencies and correlated failure.

## 3. Information Security Program (33%)

### Translate strategy into a managed capability portfolio

The program turns strategy into coordinated people, processes, technologies and services. Define charter, scope, governance, roadmap, architecture, budget, skills, sourcing, dependencies, milestones and measures. Prioritize foundational capabilities—asset, identity, configuration, vulnerability, logging, incident and recovery—based on risk rather than buying disconnected tools.

Identify information assets and assign business owners. Classification drives access, handling, encryption, sharing, retention, backup and disposal. Include structured/unstructured data, secrets, logs, models, source code and derived data. Repositories and copies often outlive the authoritative record.

Use frameworks and standards as organizing references, not claims of automatic compliance. Map obligations and risks to control objectives, then to implementable standards and procedures. Architecture should expose trust boundaries, identities, data flows, dependencies and control locations. Record design decisions and exceptions.

Program metrics should connect investment to capability and business outcome. Track coverage, effectiveness, timeliness, exception aging, loss/near miss and recovery evidence. A dashboard needs definitions, data lineage, thresholds, owners and narrative. Benchmarking can prompt questions but does not set the organization's appetite.

### Manage the full control lifecycle

Design and select controls for the scenario and operating environment. Integrate them into HR lifecycle, procurement, architecture, SDLC/DevSecOps, change, IT service management, cloud operations and data governance. Define control objective, owner, frequency/trigger, population, evidence, exceptions and dependencies. Test design before operating effectiveness.

Implementation requires business change: procedures, roles, training, integration, data quality, monitoring, support and rollback. Pilot high-impact controls, measure unintended consequences and manage technical debt. Control testing should combine configuration, population, activity, exceptions and outcomes; assurance independence should match the decision.

Awareness and training are role- and risk-based. Executives, developers, administrators, finance and incident responders need different behaviors. Measure simulation/reporting, secure choices, coaching and trend—not completion alone. Communications explain why, required action and escalation route.

Third- and fourth-party management covers criticality, due diligence, contracts, access/data, continuous monitoring, incidents, resilience, subcontractors, changes and exit. Assurance reports must be mapped to scope, period, exceptions and complementary customer controls. Concentration and portability belong in the portfolio view.

**Related item: security product versus security program.** Technology is useful only when requirements, identity/data integration, ownership, tuning, response, recovery and evidence make it an operating capability.

## 4. Incident Management (30%)

### Prepare coordinated enterprise response

An incident response plan defines authority, roles, classification, escalation, communications, evidence, external coordination and integration with crisis management, business continuity and disaster recovery. The BIA establishes critical services, dependencies, maximum disruption, RTO and RPO. BCP sustains business operations; DRP restores technology. These plans overlap but are not interchangeable.

Classify incidents using type, severity, scope, business impact, data, legal/privacy obligations and urgency. Define who can declare an incident/crisis, isolate systems, invoke continuity, notify parties and accept restoration risk. Contact lists, alternates and out-of-band communications need protection and testing.

Organize and train the response team. Include security operations, IT, cloud, identity, forensics, business, legal, privacy, HR, communications, suppliers and executives as appropriate. Retainers and evidence access should be ready before an emergency. Conduct walkthroughs, table tops, simulations and technical recovery tests with objectives and corrective actions.

**Related item: decision latency.** Measure not only detection and restoration but how long it takes to reach the authorized person with sufficient evidence to decide containment, notification or continuity activation.

### Operate, recover, and learn

Detection starts from trustworthy telemetry, baselines, intelligence and reporting channels. Triage validates signal, scope and potential impact. Investigation maintains a timeline, hypotheses, contrary evidence, chain of custody and legal constraints. Synchronize time and preserve volatile evidence when appropriate.

Containment limits harm while considering evidence, safety and business continuity. Eradication removes cause and persistence. Recovery restores trusted service, validates data and monitoring, increases exposure deliberately and watches for recurrence. Do not restore from an unverified backup or reconnect systems before identity, keys and root cause are controlled.

Communications need a preapproved plan, facts, audience, owner, timing and legal/privacy review. Avoid speculation and inconsistent channels. Regulators, customers, law enforcement, insurers and suppliers may have distinct triggers. Preserve a decision log.

Postincident review examines causes, control and process performance, decision quality, communications, business impact and recovery. Assign actions, owners and dates; retest them. Feed lessons into risk scenarios, architecture, training, suppliers, metrics and exercises. Blaming an individual hides systemic improvement opportunities.

**Related item: safe automation.** Automate enrichment and reversible containment with confidence thresholds, authorization, audit trails, failure handling and manual override. Fast uncontrolled action can widen an incident.

## Integrated scenarios

### Scenario 1 — GenAI customer-service launch

Govern the use case and accountable owners; classify prompts, retrieval data and outputs; identify privacy, leakage, injection, quality, supplier and continuity scenarios; choose controls and residual-risk authority; fund evaluation, identity, logging and incident capabilities; and define shutdown/fallback decisions. Report outcome and uncertainty to executives without reducing the program to a model-security tool.

### Scenario 2 — Critical supplier ransomware

Start from contractual and concentration risk, dependency maps and BIA. Exercise notification, evidence sharing, alternative processing, privileged access revocation, data recovery and communications. Distinguish the supplier's recovery assertion from the enterprise's end-to-end business recovery evidence. Reassess residual risk and exit options after the postincident review.

### Scenario 3 — Privileged-access program

Build the business case from high-impact scenarios. Assign identity, HR, application and risk owners; inventory accounts; define joiner/mover/leaver, approval, vaulting, session monitoring, emergency access and recertification; integrate with cloud and suppliers; test the population; track exceptions and business friction; and define response when a privileged identity is compromised.

## Eight practical labs

1. **Governance RACI:** for a fictional organization, assign board, executive, risk owner, data owner, security manager, control owner and assurance responsibilities for five decisions.
2. **Security strategy:** produce current state, target outcomes, three initiatives, dependencies, measures and an executive decision request tied to one business objective.
3. **Risk scenario:** write five cause-event-impact scenarios; score with explicit criteria, record uncertainty and name residual-risk authority.
4. **Control selection:** compare three response options using risk reduction, cost, feasibility, user impact, dependencies, evidence and exit; recommend without hiding assumptions.
5. **Program roadmap:** sequence asset, identity, logging, vulnerability, supplier and incident capabilities across four quarters with owners and outcome metrics.
6. **Supplier assurance:** map a fictional provider pack to contract, report scope, customer controls, concentration, incident and exit requirements; document gaps.
7. **Tabletop:** run an authorized 60-minute lost-token or ransomware exercise. Record decisions, timestamps, escalations, communications and action owners.
8. **Recovery evidence:** restore a disposable service and data set, rotate credentials, validate a business transaction and monitoring, measure targets and update the risk register.

## 40 readiness checks

1. Who owns information-security risk acceptance?
2. What security governance decision remains with the board?
3. How do policy, standard, procedure and guideline differ?
4. What makes an exception governable?
5. Which inputs should drive security strategy?
6. What belongs in a security business case?
7. Why is tool count a weak board metric?
8. How should security communicate uncertainty?
9. What separates a threat from a vulnerability?
10. Can you write a cause-event-impact risk scenario?
11. How do appetite and tolerance differ?
12. How do inherent and residual risk differ?
13. Why is a vulnerability score not a risk rating?
14. When should risk be escalated rather than accepted?
15. How do risk, control and action ownership differ?
16. What makes a KRI actionable?
17. Why must correlated dependencies be aggregated?
18. Which trigger forces risk reassessment?
19. How does a program differ from a project?
20. Which capabilities should precede advanced tools?
21. Who owns information classification?
22. How does classification change lifecycle controls?
23. What proves a control is designed effectively?
24. What proves it operates effectively?
25. How should program metrics trace to outcomes?
26. Why is training completion not behavior evidence?
27. Which supplier-report limitations matter?
28. What fourth-party and exit risks should be assessed?
29. How do BIA, BCP, DRP and incident response differ?
30. Who may declare an incident or crisis?
31. Which facts drive incident severity?
32. When should evidence preservation affect containment?
33. How do containment, eradication and recovery differ?
34. What must be trusted before reconnecting a restored system?
35. Which communications need legal or privacy review?
36. What belongs in an incident decision log?
37. How does a tabletop differ from a recovery test?
38. What makes a postincident action complete?
39. How can automation worsen incident impact?
40. Can you choose the management action before the technical action?

## Places to learn

This is not a complete list, and it is not meant to be consumed end to end. Pick the resource and chapters that close your measured gaps. **Version check:** anything built for the 2022 outline applies only through November 2, 2026 unless its publisher explicitly updates it for the November 3 outline.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Current CISM exam content outline](https://www.isaca.org/credentialing/cism/cism-exam-content-outline) | Public | 30–60 min | Canonical current scope and scheduled-change notice |
| [ISACA certification exam candidate guide](https://www.isaca.org/credentialing/-/media/fa494652c5f149289af38cef18328650.ashx) | Public PDF | 60–90 min | Exam policy and detailed 2022 task baseline |
| [ISACA online review courses](https://www.isaca.org/training-and-events/online-training/online-review-courses) | Paid | 20–30 hr estimated | Official structured learning; verify that purchased material matches the intended test date |
| [CISM Review Manual, 16th Edition](https://www.isaca.org/store2/product/EPUBCM16ED-2024) | Paid | 20–35 hr estimated | Current-outline definitions, tasks and references; ISACA warns it will not grant later-version access |
| [CISM certification page and QAE route](https://www.isaca.org/credentialing/cism) | Public/paid | 25–45 hr estimated for QAE | Official 1,047-question database route and exam/registration context |
| [Free official CISM practice quiz](https://www.isaca.org/credentialing/cism/cism-practice-quiz) | Public/form | 15–25 min | Ten-question official style sample, not a readiness score |
| [O'Reilly CISM Course — Peter H. Gregory](https://www.oreilly.com/videos/certified-information-security/0642572021955/) | Paid | 8 hr 2 min | Concise January 2025 management-oriented course |
| [O'Reilly/Packt CISM — ACI Learning](https://www.oreilly.com/videos/certified-information-security/9781835881309/) | Paid | 13 hr 49 min | More expansive 2022-outline explanations and quizzes |
| [LinkedIn Learning CISM Cert Prep](https://www.linkedin.com/learning/isaca-certified-information-security-manager-cism-cert-prep) | Paid/trial | 9 hr 22 min | Advanced four-domain course released May 2025 |
| [Udemy Masterclass — CISM Exam](https://www.udemy.com/course/hemang-doshi-cism/) | Paid | Verify live duration | Supplementary 2022-outline instruction; do not use for a post-November exam until explicitly updated |
| [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) | Public | 1–2 hr selected | Governance, outcomes and profiles as related context |
| [CISM certification requirements](https://www.isaca.org/credentialing/cism/get-cism-certified) | Public | 10–15 min | Exam-versus-designation and experience rules |
| [CISM maintenance requirements](https://www.isaca.org/credentialing/cism/maintain-cism-certification) and [2027 CPE change](https://www.isaca.org/credentialing/cpe-2027) | Public | 20–30 min | Current and scheduled maintenance obligations |

Reject dumps, recalled or “actual” questions, guaranteed-pass products, and content that claims the unpublished November weights.
