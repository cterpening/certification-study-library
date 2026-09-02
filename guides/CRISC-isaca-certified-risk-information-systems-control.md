---
exam_code: CRISC
vendor_id: isaca
official_blueprint: https://www.isaca.org/credentialing/crisc/crisc-exam-content-outline
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Certified in Risk and Information Systems Control (CRISC) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The effective-2025 outline, 2026 candidate guide, certification and maintenance rules, official preparation options, and selected independent resources were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#crisc-coverage-record).

**Current baseline:** Governance (26%); Risk Assessment (22%); Risk Response and Reporting (32%); Technology and Security (20%). ISACA identifies this outline as effective 2025.<br>
**Exam contract:** 150 multiple-choice questions in four hours through PSI test centers or remote proctoring. Registration is continuous, eligibility lasts six months, and the 2026 candidate guide lists US$575 member/US$760 nonmember pricing. Verify live identity, scheduling, language and retake rules.<br>
**Certification contract:** Anyone may sit the exam. To hold CRISC, pass within five years, pay the US$50 application fee, and document at least three years of qualifying professional experience across at least two of the four CRISC domains, gained within the ten years before application. Experience verification, ethics and continuing education apply; an exam pass alone is not the designation.<br>
**Maintenance:** At least 20 relevant CPE hours annually and 120 over three years, annual fee, ethics and audit cooperation. ISACA's revised CPE framework takes effect January 1, 2027.<br>
**Upcoming change:** No replacement outline or retirement was announced September 2, 2026. Recheck the live outline and candidate guide before scheduling.<br>
**Integrity:** ISACA's free quiz and QAE products are the official item-style sources. The 40 prompts below are original reasoning checks, not recalled or predicted questions.

## How to use this guide

Think in a loop: enterprise context and governance → scenario identification → analysis and prioritization → owned response and control design → monitored residual risk and reporting → reassessment when assumptions change. Keep the business objective, accountable risk owner, decision authority and evidence visible. CRISC is not a catalog of security products; technology and security knowledge supports risk decisions.

Use one realistic portfolio to practice the whole loop. Make every rating traceable to criteria, every treatment traceable to an owner, every control traceable to a risk and objective, and every dashboard traceable to validated data and action thresholds.

> **About related items:** A `Related item:` callout adds architecture, security, operations, governance, or lifecycle context. It makes the published objective more useful in real work but does not imply that the extra phrase appears verbatim in the official outline.

## Blueprint map

| Domain | Weight | Evidence to produce |
|---|---:|---|
| Governance | 26% | Enterprise-aligned risk governance, accountable roles, appetite/tolerance, policy and asset/resilience context |
| Risk Assessment | 22% | Complete scenarios, defensible analysis, BIA and maintained risk register |
| Risk Response and Reporting | 32% | Owned treatment/control plans, test evidence, KRIs/KCIs/KPIs and decision-ready reporting |
| Technology and Security | 20% | Architecture/lifecycle/resilience/security context translated into risk and control implications |

## 1. Governance (26%)

### Align risk with enterprise objectives

Governance evaluates stakeholder needs, establishes direction and monitors outcomes; management plans and executes within that direction. Understand enterprise strategy, goals, organization structure, roles, culture and ethics before designing a risk process. Risk management exists to improve decisions under uncertainty, not to produce a register.

Assign responsibilities. Governing bodies oversee. Executives set appetite and resources. Business/process owners own objectives and associated risk. Risk practitioners facilitate consistent identification, analysis, response and reporting. Control owners design/operate assigned controls. Assurance functions test independently. Use a RACI or similar model, but name one accountable decision owner.

Policies express required direction, standards define mandatory specifications, procedures implement, and guidelines advise. Exceptions need owner, risk assessment, compensating controls, approval, expiration and review. Legal, regulatory and contractual obligations inform criteria and response but should be interpreted by appropriate experts.

Business resilience joins continuity, disaster recovery, crisis management and supplier dependencies to protect prioritized outcomes. Asset management identifies owners, value/criticality, location, support state and lifecycle. An incomplete inventory creates both unknown risk and misleading metrics.

### Establish an integrated risk framework

Enterprise risk management creates common context across strategic, operational, financial, compliance and technology risks. The three-lines model separates ownership, oversight and independent assurance. A risk profile summarizes the organization's material exposure. Appetite expresses the broad amount/type of risk the enterprise is willing to pursue or retain; tolerance defines acceptable variation around objectives.

Choose frameworks and methods appropriate to size, regulation, decision needs and maturity. Define taxonomy, scope, criteria, scales, aggregation, reporting, review cadence and escalation. Framework adoption is not evidence that risk is managed. Integrate the process into strategy, portfolio, procurement, architecture, SDLC, change, operations and incident management.

**Related item: positive risk.** Opportunity is uncertainty too. A well-designed process helps leaders take informed technology risk to gain value rather than only blocking change.

## 2. Risk Assessment (22%)

### Identify complete, relevant scenarios

A useful scenario names the objective or asset/process, threat/cause, vulnerability or condition, event and business impact. Gather from interviews/workshops, asset/data flows, architecture, incidents, threat intelligence, vulnerability findings, audits, suppliers, projects and external change. Threat modeling examines plausible actors, paths, trust boundaries and abuse; it complements rather than replaces enterprise assessment.

Distinguish asset value from threat capability and vulnerability severity. Validate inventory, ownership, exposure and existing controls. Emerging risk has greater uncertainty and may need scenarios, leading indicators and decision options instead of a false precise score. Record assumptions and data quality.

The BIA identifies critical processes, dependencies, impact over time, maximum tolerable disruption, recovery time and recovery point objectives. It informs operational and resilience scenarios but is not the entire risk assessment.

### Analyze, evaluate, and record risk

Define likelihood and impact criteria before scoring. Qualitative methods support shared prioritization; quantitative methods can estimate frequency and magnitude when data and assumptions are defensible. Scenario analysis, sensitivity, Monte Carlo or expected loss can clarify uncertainty; none removes judgment. Avoid multiplying ordinal labels as if they were precise currency.

Inherent risk is considered before controls; residual risk remains after their effect. “Current risk” terminology varies, so document the organization's definition. Evaluate against appetite/tolerance, regulatory limits and decision authority. Aggregate correlated exposures and concentration—several individually moderate supplier dependencies may create one severe outage path.

Maintain the risk register as a decision history: scenario, owner, assessment, criteria, controls, response, residual exposure, actions, review dates, indicators and acceptance/escalation. Deduplicate related entries and preserve relationships to assets, controls, incidents and issues.

**Related item: bow-tie analysis.** Map causes and preventive controls on one side, the event in the middle, and consequences with recovery controls on the other to reveal single points of failure.

## 3. Risk Response and Reporting (32%)

### Select and govern responses

Responses include avoid, mitigate/reduce, transfer/share and accept. Compare options by objective, risk reduction, cost, feasibility, timing, dependencies, secondary risk and reversibility. Transfer rarely removes accountability; exclusions, limits and supplier failure remain. Acceptance belongs to an authorized risk owner and should state scope, rationale, duration and review triggers.

Treatment plans name action, owner, resources, due date, interim controls and success evidence. Track issues, findings, exceptions and exemptions distinctly according to organizational definitions. An overdue action changes the current exposure and should trigger reassessment/escalation, not only status color.

Third-party and supply-chain risk spans criticality, due diligence, contracts, access/data, locations, subcontractors, continuous monitoring, incidents, resilience and exit. Map assurance reports to actual service scope, period, exceptions and complementary customer controls. Assess concentration and portability.

### Design, implement, and test controls

Controls may be preventive, detective, corrective, deterrent, compensating or recovery; manual or automated; entity-level or process-specific. Define objective, owner, trigger/frequency, population, implementation, evidence, dependencies and exception handling. Analyze whether the design addresses the scenario before testing operation.

Implementation includes configuration, process, skills, integration, communication, monitoring, support and rollback. Test design, implementation and operating effectiveness with representative population and period. Inquiry alone is weak; combine inspection, observation, analytics and reperformance. A control can operate consistently yet fail to reduce the intended risk.

### Monitor and report decisions

Collect, aggregate, analyze and validate data before reporting. KRIs indicate exposure; KCIs indicate control condition; KPIs indicate performance or outcome. Define formula, source, owner, frequency, threshold, target, interpretation and response. A metric without an action threshold is decoration.

Use heat maps carefully: they communicate relative position but can hide uncertainty and aggregation. Scorecards and dashboards should show trends, appetite/tolerance, top changes, concentrations, overdue treatments, control failures and emerging risk. Tailor detail to boards, executives, owners and operators. Communicate assumptions, confidence and requested decision.

**Related item: risk velocity and persistence.** Similar likelihood/impact scenarios may demand different responses when one develops rapidly, lasts longer or is harder to detect.

## 4. Technology and Security (20%)

### Understand technology lifecycles as risk systems

Enterprise architecture connects business, data, application and technology states, principles and roadmaps. Evaluate trust boundaries, identities, data flows, dependencies, technical debt, interoperability and concentration. IT operations manage configuration, change, release, incidents, problems, capacity, availability, logging, backups and suppliers; weak operating evidence changes the claimed control effect.

Embed risk in project/portfolio and SDLC decisions. Requirements include security, privacy, resilience, logging and records. Architecture, code/dependency review, testing, environment separation, deployment authorization and rollback support controlled change. Agile and DevOps shorten feedback loops; they do not remove accountability. Track data from creation/acquisition through use, sharing, retention, archive and destruction.

Business continuity sustains processes; disaster recovery restores technology. RTO and RPO come from business impact. Test dependency-aware recovery including identity, keys, networks, data, applications, suppliers and reconciliation. Replication can reproduce corruption; backup success is not restore proof.

Assess emerging technologies by use case, data, architecture, supplier, control changes, skills, observability and exit. Do not equate unfamiliarity with unacceptable risk or marketing maturity with control assurance.

### Apply security and privacy concepts to risk

Confidentiality, integrity and availability describe protection objectives. Identity, least privilege, segmentation, encryption/key management, secure configuration, vulnerability management, monitoring, incident response and recovery combine in defense in depth. Select control strength from the scenario and business requirement.

Privacy concerns lawful/appropriate processing of personal data, transparency, purpose, minimization, rights, retention and transfers in addition to security. Awareness should be role- and risk-specific and measured by behavior/outcome, not completion alone.

**Related item: shared responsibility.** Cloud and SaaS providers operate some controls; customers retain configuration, identity, data, use and monitoring responsibilities. Inherited-control evidence must match service, region, period and customer obligations.

## Integrated scenarios

### Scenario 1 — Cloud analytics migration

Connect migration objectives to governance and appetite. Map sensitive data, identities, regions and supplier dependencies; write leakage, integrity, availability and lock-in scenarios; assess controls and concentration; compare redesign, phased migration, contractual transfer and acceptance; assign treatment owners; define KCIs/KRIs; and test end-to-end restore and exit.

### Scenario 2 — AI-assisted software delivery

Identify source-code leakage, insecure suggestion, dependency, license, prompt injection and over-automation scenarios. Define acceptable-use governance, data boundaries, review/testing, provenance, secrets, monitoring and incident handling. Measure escaped defects, override behavior and repository coverage rather than license count. Reassess as models, agents or suppliers change.

### Scenario 3 — Acquisition risk integration

Inventory critical processes, identities, data, networks, contracts and unsupported systems. Aggregate inherited risks, establish interim segmentation and privileged controls, prioritize by business transition, preserve accepted-risk authority, and report what must be decided before connectivity. Plan architecture convergence, control testing, continuity and supplier exits.

## Eight practical labs

1. **Governance model:** build a RACI for appetite, acceptance, control operation, issue remediation and assurance; resolve conflicting accountability.
2. **Risk taxonomy:** define five categories, likelihood/impact criteria, aggregation rule, tolerance and escalation with examples.
3. **Scenario workshop:** create eight cause-event-impact scenarios from a synthetic architecture and rank data quality/uncertainty.
4. **BIA and bow tie:** set business-owned recovery objectives, dependencies, causes, preventive controls, consequences and recovery controls.
5. **Response comparison:** evaluate avoid/mitigate/transfer/accept options with lifecycle cost, reduction, timing, secondary risk and evidence.
6. **Control test:** define objective/population/evidence, test design and operating effectiveness on synthetic records, and conclude on residual risk.
7. **Dashboard:** calculate one KRI, KCI and KPI from documented synthetic data; set thresholds, action owners and limitations.
8. **Tabletop/reassessment:** run an authorized supplier outage exercise, record decisions and update scenarios, control claims and treatment priorities.

## 40 readiness checks

1. How do governance and management differ?
2. Who owns a business risk?
3. What belongs to a control owner?
4. How do the three lines differ?
5. What makes risk appetite useful?
6. How does tolerance relate to objectives?
7. What makes a policy exception governable?
8. Why is an asset inventory a risk control?
9. Can you write a cause-event-impact scenario?
10. How do threat, vulnerability and control deficiency differ?
11. What does threat modeling add?
12. What does a BIA produce?
13. When is qualitative analysis appropriate?
14. Which assumptions make quantitative results fragile?
15. How do inherent and residual risk differ?
16. Why must correlated risk be aggregated?
17. What belongs in a risk register?
18. Which change triggers reassessment?
19. How do avoid, mitigate, transfer and accept differ?
20. Why does transfer not remove accountability?
21. Who may accept residual risk?
22. What makes a treatment plan measurable?
23. How do an issue, finding and exception differ?
24. Which third-party evidence limitations matter?
25. What defines an effective control design?
26. What proves operating effectiveness?
27. Why can an operating control still be ineffective?
28. When is a compensating control acceptable?
29. How do KRI, KCI and KPI differ?
30. What makes a threshold actionable?
31. What can a heat map conceal?
32. What should a board risk report request?
33. How does architecture expose concentration risk?
34. Why does Agile still need control evidence?
35. How does data lifecycle alter exposure?
36. Why is replication not recovery?
37. Who sets RTO and RPO?
38. How does privacy differ from security?
39. What customer controls remain in SaaS?
40. Can you recommend a business decision, not merely a product?

## Places to learn

This is not a complete list, and it is not meant to be consumed end to end. Pick the format and sections that close diagnosed gaps, then validate decisions against the effective-2025 official outline. Durations were publisher-listed or practically estimated September 2, 2026.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [CRISC exam content outline](https://www.isaca.org/credentialing/crisc/crisc-exam-content-outline) | Public | 30–60 min | Canonical weights, topics and supporting tasks |
| [ISACA certification exam candidate guide](https://www.isaca.org/credentialing/-/media/fa494652c5f149289af38cef18328650.ashx) | Public PDF | 60–90 min | Detailed effective-2025 scope and exam policy |
| [CRISC certification and preparation page](https://www.isaca.org/credentialing/crisc) | Public/paid routes | 20–30 min orientation; 20–40 hr official prep | Current registration, official course/manual and 600-question QAE route |
| [Free official CRISC practice quiz](https://www.isaca.org/credentialing/crisc/crisc-practice-quiz) | Public/form | 15–25 min | Small official item-style sample, not a readiness score |
| [Pluralsight CRISC path](https://www.pluralsight.com/paths/crisctm-certified-in-risk-and-information-systems-controltm) | Paid/trial | 5 hr | Six courses, labs and practice exam; 2025–26 releases |
| [O'Reilly/Packt CRISC — ACI Learning](https://www.oreilly.com/videos/crisc-certified-in/9781835886465/) | Paid | 16 hr 28 min | Detailed four-domain course with quizzes |
| [LinkedIn Learning CRISC Cert Prep](https://www.linkedin.com/learning/isaca-certified-in-risk-and-information-systems-control-crisc-cert-prep) | Paid/trial | 6 hr 3 min | Concise effective-outline overview released December 2025 |
| [Udemy Masterclass — CRISC Exam (Updated 2026)](https://www.udemy.com/course/masterclass-crisc-exam/) | Paid | About 19 hr | Supplemental explanation and practice; keep ISACA authoritative |
| [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) | Public | 1–2 hr selected | Governance, profiles and outcomes as related context |
| [CRISC certification requirements](https://www.isaca.org/credentialing/crisc/get-crisc-certified) | Public | 10–15 min | Exam-versus-designation and three-year experience rules |
| [CRISC maintenance requirements](https://www.isaca.org/credentialing/crisc/maintain-crisc-certification) and [2027 CPE change](https://www.isaca.org/credentialing/cpe-2027) | Public | 20–30 min | Current and scheduled renewal duties |

Reject dumps, recalled/“actual” questions, guaranteed-pass files, and practice sources that cannot explain their blueprint version.
