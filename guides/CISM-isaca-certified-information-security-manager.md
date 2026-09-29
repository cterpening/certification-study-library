---
exam_code: CISM
vendor_id: isaca
official_blueprint: https://www.isaca.org/credentialing/cism/cism-exam-content-outline
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-29
---

# Certified Information Security Manager (CISM) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Reviewed September 29, 2026. The current map covers 35 subtopics and 37 supporting tasks. Forty original prompts have answer notes; three scenarios have worked results; an offline workbook passes 47 checks. Eight broader activities remain proposed. See the [coverage record](../docs/SOURCE-VALIDATION.md#cism-coverage-record) and [research record](../docs/research/2026-09-29-cism-deep-review.md).

**CURRENT BLUEPRINT through November 2, 2026:** Governance 17%, Risk Management 20%, Information Security Program 33%, Incident Management 30%. The live outline and candidate guide's 2022 appendix agree. The four domain headings below use this current baseline.

**Scheduled November 3, 2026 change:** ISACA's [September 10 announcement](https://www.isaca.org/about-us/newsroom/press-releases/2026/isaca-updates-cism-exam-content-outline-factoring-in-todays-technologies-security-responsibilities) confirms the same domains with weights **18%, 20%, 33%, 29%**, more strategy/program-development emphasis, and new enterprise-architecture and information-security-architecture content areas. Updated preparation materials became available September 1. The exact future subtopic/task list remains unverified because the linked support article times out; the announcement is sufficient for these specific changes, not a complete replacement objective map.

**Exam and designation are separate:** 150 questions in four hours; a scaled 450 on a 200–800 scale passes, not a raw 56.25% score. The public candidate guide lists US$575 member/US$760 nonmember fees and six-month eligibility. Anyone may sit. The designation requires timely application, verified qualifying management experience, ethics and maintenance; the standard experience route is five years across at least three domains within the ten years before application. Apply within five years of passing; the application fee is US$50. The candidate guide lists a maximum two-year CISM experience waiver, but eligible categories and personal evidence require verification. A passed exam alone does not confer CISM. [Candidate guide](https://www.isaca.org/credentialing/-/media/fa494652c5f149289af38cef18328650.ashx), [certification requirements](https://www.isaca.org/credentialing/cism/get-cism-certified).

**VERIFY CURRENT — scheduling:** The candidate guide permits four attempts in a rolling 12 months, with 30 days after the first failure and 90 days after each later failure. Rescheduling requires at least 48 hours. A single six-month eligibility extension has separate conditions and a US$75 fee. These are not guarantees of appointments, accommodations or personal eligibility; check the live rules before booking.

**Maintenance:** Current requirements include 20 CPE annually, 120 per three-year cycle and annual fees of US$45 member/US$85 nonmember. From January 1, 2027, the revised framework requires at least 90 aligned hours and permits up to 30 other qualifying professional-development hours; all 120 can align. Individual activity caps and evidence rules still apply. The current maintenance page says to retain evidence for 12 months after the cycle, while the linked new policy specifies a minimum three years. Verify the applicable cycle and transition before deciding what to retain; no personal CPE assessment was performed. [Maintenance](https://www.isaca.org/credentialing/cism/maintain-cism-certification), [2027 policy announcement](https://www.isaca.org/credentialing/cpe-2027).

**Resource boundary:** The public certification page still advertises a 1,047-item QAE pool. The rendered course listing advertises about 16 hours, six-month access and 20 CPE, while retaining an old-material warning and linking a recommendation labeled 17th edition. The current QAE/manual and recommended-course routes rendered only shells. Do not assume that a generic link, edition label or question count establishes November alignment or an automatic upgrade. Verify the exact product before purchase; paid lessons and questions were not reviewed.

**Integrity:** These are original management-reasoning exercises, not recalled exam questions. The free quiz was fetched but its items were not reviewed or submitted. No account, checkout, purchase or live organizational action occurred.

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

### Version selection and architecture bridge

| Exam date | Governance | Risk | Program | Incident | Coverage boundary |
|---|---:|---:|---:|---:|---|
| Through November 2, 2026 | 17% | 20% | 33% | 30% | Current 35 subtopics and 37 tasks mapped |
| From November 3, 2026 | 18% | 20% | 33% | 29% | Announcement verified; complete future task mapping pending |

**PRACTICAL DEPTH:** Enterprise architecture connects business capabilities to processes, information, applications, infrastructure and suppliers. Information security architecture places security objectives, trust boundaries, identities, protective/detective controls and assurance evidence into those relationships. Draw both for a customer-service launch: which business capability depends on which information flow, who owns the data, which provider may act, what could cross a boundary, and how the business continues if the provider or identity service fails. A diagram is useful only when its assumptions, owners and exceptions are maintained. This bridge teaches the announced areas without inventing their future exam subtopics.

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

### Make authority and uncertainty explicit

A residual-risk decision should identify the scenario, affected business objective, assessed range, evidence date, operating controls, obligations, accountable owner and authority limit. Record start/expiry, review triggers, treatment milestones and what happens if the decision lapses. An approval is evidence of a decision, not proof that controls work or that a legal obligation can be waived. The security manager can recommend, but a title alone does not grant business-risk acceptance authority. ISACA's [ethics requirements](https://www.isaca.org/code-of-professional-ethics) support objective reporting, competence, due care and disclosure of significant facts.

In the workbook's fictional annual-loss scenario, the current point estimate is US$200,000. A response projects US$80,000 of residual loss plus US$60,000 annual cost, yielding a modeled US$60,000 improvement. But alternative probability assumptions produce US$90,000–310,000 total exposure plus cost. This sensitivity interval is not a confidence interval. Present the assumptions, uncertainty, nonfinancial impacts, mandatory obligations and implementation evidence before recommending an option; a favorable point estimate cannot authorize itself.

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

### Normalize risk before combining it

[NIST IR 8286 Rev. 1](https://csrc.nist.gov/pubs/ir/8286/r1/final) provides practical guidance for connecting cybersecurity registers and enterprise decisions. Use a short register linked to a detailed record of assumptions, analysis, owners, dates and response history. Distinguish **inherent** exposure before the chosen controls, **current** exposure with controls operating now, **target** exposure projected after a response, and **residual** exposure evaluated after it. Define these terms in your register; a projected target must not silently replace the current assessment. Framework wording varies, so normalization includes meaning, time horizon, units, impact categories and scoring method.

Two suppliers each have a fictional 5% annual outage probability. If independent, both fail with probability 0.25%; if their outages are entirely caused by the same dependency, both fail with probability 5%. With additive losses of US$2 million and US$3 million and unchanged marginal probabilities, expected combined loss remains US$250,000 in either model. Dependence changes the joint-loss distribution and simultaneous-recovery demand; it does not automatically increase the sum of expected additive losses. Double counting a shared business loss or adding ordinal risk scores produces a different error. Investigate concentration, common identity/region/network providers, conditional effects and recovery capacity before approving the portfolio.

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

### Measure the population and the decision

Define a metric's population, numerator, time window, exclusions, evidence freshness and accountable action owner before publishing it. In the workbook, 100 in-scope assets include 90 enrolled, 80 with current telemetry and 75 with verified control evidence. A reporter-only dashboard shows 75/80 = 93.75%; enterprise coverage is 75/100 = 75%. Twenty assets lack current telemetry. They remain unknown until investigated; omitting them does not establish healthy controls. Enrollment and telemetry each contain an unrelated ID that must be reconciled rather than counted. Expanding inventory to 120 assets makes coverage 62.5% with unchanged verified assets; explain scope growth before calling it control deterioration.

Similarly, only two of five fictional suppliers have current, relevant assurance. A stale report, absent report and report covering another service are three distinct gaps. Even a current report is an input: inspect service scope, period, exceptions, subservice treatment and customer responsibilities, then test the controls your organization operates. A 40% evidence-coverage result is not a statement that the other 60% are compromised or that the two reports prove complete security.

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

### Response is part of ongoing risk management

The current [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) organizes incident-response recommendations around CSF 2.0. Govern, Identify and Protect support readiness; Detect, Respond and Recover cover incident activity, with improvement feeding all functions as lessons emerge. This is practical context, not an alternative CISM outline. Do not wait until the entire incident ends to fix an urgent, understood weakness. Provider contracts must establish information flows and authority to contain, restore or share information; outsourcing tasks does not eliminate enterprise accountability.

Set criteria for human decisions and explicitly preauthorized actions before an incident. In the fictional timeline, detection occurs at minute 5, triage at 8, a decision request at 10, approval at 28 and containment at 32. Eighteen minutes were spent awaiting the decision; the four-minute action execution is a different measure. Review alternate approvers, required evidence, escalation and safe preauthorization. Do not remove necessary oversight merely to improve a timer.

Recovery requires trusted restoration inputs, appropriate sequencing, checks of restored assets, validation with owners and monitoring. Evidence handling must fit the incident and applicable rules; formal forensic chain of custody is not automatically required for every routine event. Preserve provenance and integrity, and ask the designated legal/privacy functions about obligations. No universal notification deadline or legal determination is supplied here.

## Integrated scenarios

### Scenario 1 — GenAI customer-service launch

Govern the use case and accountable owners; classify prompts, retrieval data and outputs; identify privacy, leakage, injection, quality, supplier and continuity scenarios; choose controls and residual-risk authority; fund evaluation, identity, logging and incident capabilities; and define shutdown/fallback decisions. Report outcome and uncertainty to executives without reducing the program to a model-security tool.

### Scenario 2 — Critical supplier ransomware

Start from contractual and concentration risk, dependency maps and BIA. Exercise notification, evidence sharing, alternative processing, privileged access revocation, data recovery and communications. Distinguish the supplier's recovery assertion from the enterprise's end-to-end business recovery evidence. Reassess residual risk and exit options after the postincident review.

### Scenario 3 — Privileged-access program

Build the business case from high-impact scenarios. Assign identity, HR, application and risk owners; inventory accounts; define joiner/mover/leaver, approval, vaulting, session monitoring, emergency access and recertification; integrate with cloud and suppliers; test the population; track exceptions and business friction; and define response when a privileged identity is compromised.

## Worked results for the three scenarios

1. **GenAI launch:** Name the customer-service business owner, data owner and security/control owners. Map retrieval, model provider, logging and human escalation boundaries. Recommend a constrained pilot with approved data, least privilege, adversarial evaluation, output review and a tested human fallback. Use the US$200,000 versus US$140,000 point-estimate comparison only alongside its US$90,000–310,000 sensitivity range and unquantified impacts. Require a dated decision within delegated authority; changed data use or a new provider reopens the assessment. No model or privacy-compliance test was executed.
2. **Supplier ransomware:** Establish facts, contractual contacts, enterprise exposure and continuity authority. Treat two vendors sharing an identity provider as a common dependency. The joint-outage model changes from 0.25% to 5%; choosing a second vendor alone does not establish independence. In the modeled recovery, containment at minute 32 precedes identity readiness at 44 and data readiness at 40. Parallel prerequisites permit application readiness at 59, followed by business validation at 69. A 60-minute business RTO is missed even though the application is up before it. A recovery point 20 minutes before disruption misses a 15-minute RPO. These are chosen durations, not measured recovery results; escalate the gap and fund/test a workable alternative.
3. **Privileged-access program:** Reconcile account/asset populations and classify missing evidence before reporting success. The fictional coverage is 75%, not the reporter-only 93.75%. Assign owners to unenrolled assets, silent agents and unverified controls; investigate unmatched IDs separately. Sequence inventory and identity ownership before privileged workflows, telemetry and advanced analytics. Keep emergency access monitored and expiring; measure task success and business friction as well as enrollment. After expanding scope, distinguish the denominator change from actual deterioration. No real account or endpoint was modified.

## Executed offline management workbook

This Python standard-library example passed **47 checks** with fictional inputs. It tests arithmetic, population reconciliation, chosen authority rules and a dependency timeline. It does not infer real probabilities, accept risk, verify suppliers, operate an incident or restore a service. The authority ceilings and exclusive expiry convention are explicit exercise rules, not ISACA requirements. The wider eight activities below remain proposed.

```python
"""Original, offline management examples using fictional inputs and chosen rules."""
from datetime import date
from fractions import Fraction as F
import json

checks = []


def check(name, actual, expected):
    if actual != expected:
        raise AssertionError((name, actual, expected))
    checks.append(name)


def probability(value):
    if not 0 <= value <= 1:
        raise ValueError('Probability must be between zero and one')
    return value


p = probability(F(5, 100))
independent_both = p * p
common_both = p
check('independent joint outage', independent_both, F(1, 400))
check('shared cause joint outage', common_both, F(1, 20))
check('joint exposure multiplier', common_both / independent_both, 20)
check('independent any outage', 2 * p - independent_both, F(39, 400))
check('shared cause any outage', 2 * p - common_both, p)
loss_a, loss_b = 2_000_000, 3_000_000
expected_total = p * loss_a + p * loss_b
check('additive expected loss', expected_total, 250_000)
check('common cause expected loss', p * (loss_a + loss_b), expected_total)
try:
    probability(F(3))
except ValueError:
    check('ordinal score rejected as probability', True, True)
else:
    raise AssertionError('An ordinal score is not a probability')

before = F(20, 100) * 1_000_000
after = F(8, 100) * 1_000_000
annual_cost = 60_000
check('modeled current annual loss', before, 200_000)
check('modeled target annual loss', after, 80_000)
check('modeled total with response', after + annual_cost, 140_000)
check('point estimate improvement', before - after - annual_cost, 60_000)
check('optimistic response total', F(3, 100) * 1_000_000 + annual_cost, 90_000)
check('pessimistic response total', F(25, 100) * 1_000_000 + annual_cost, 310_000)

today = date(2026, 9, 29)
authority = {'operations-owner': 500_000, 'enterprise-risk-council': 5_000_000}
base = dict(owner='operations-owner', loss_upper=400_000,
            starts=date(2026, 9, 1), expires=date(2026, 10, 1),
            assumptions_current=True, legal_review_complete=True)


def acceptance_reason(record):
    if not record['legal_review_complete']:
        return 'obligation review needed'
    if not record['starts'] <= today < record['expires']:
        return 'outside decision period'
    if not record['assumptions_current']:
        return 'reassess changed assumptions'
    if record['owner'] not in authority:
        return 'no delegated authority'
    if record['loss_upper'] > authority[record['owner']]:
        return 'escalate beyond delegation'
    return 'within fictional decision rules'


check('valid recorded decision', acceptance_reason(base), 'within fictional decision rules')
check('expiry is exclusive', acceptance_reason(dict(base, expires=today)), 'outside decision period')
check('future approval ineffective', acceptance_reason(dict(base, starts=date(2026, 10, 1))), 'outside decision period')
check('security adviser lacks delegation', acceptance_reason(dict(base, owner='security-manager')), 'no delegated authority')
check('upper estimate exceeds authority', acceptance_reason(dict(base, loss_upper=500_001)), 'escalate beyond delegation')
check('boundary estimate allowed', acceptance_reason(dict(base, loss_upper=500_000)), 'within fictional decision rules')
check('new supplier forces reassessment', acceptance_reason(dict(base, assumptions_current=False)), 'reassess changed assumptions')
check('money does not settle obligations', acceptance_reason(dict(base, legal_review_complete=False)), 'obligation review needed')

inventory = set(range(1, 101))
enrolled = set(range(1, 91)) | {999}
reporting = set(range(1, 81)) | {1000}
verified = set(range(1, 76))
check('inventory population', len(inventory), 100)
check('unmatched enrollment', enrolled - inventory, {999})
check('unmatched telemetry', reporting - inventory, {1000})
check('valid enrollment', len(enrolled & inventory), 90)
check('valid reporting', len(reporting & inventory), 80)
check('missing current telemetry', len(inventory - reporting), 20)
check('verified population coverage', F(len(verified & inventory), len(inventory)), F(3, 4))
check('reporter-only result', F(len(verified), len(reporting & inventory)), F(15, 16))
expanded_inventory = inventory | set(range(101, 121))
check('expanded population coverage', F(len(verified), len(expanded_inventory)), F(5, 8))

suppliers = {'A': 'current', 'B': 'stale', 'C': None, 'D': 'current', 'E': 'out-of-scope'}
check('current assurance population', sum(v == 'current' for v in suppliers.values()), 2)
check('assurance fraction', F(sum(v == 'current' for v in suppliers.values()), len(suppliers)), F(2, 5))
check('missing evidence retained', [k for k, v in suppliers.items() if v is None], ['C'])
check('stale is not current', suppliers['B'] == 'current', False)
check('wrong scope is not current', suppliers['E'] == 'current', False)

timeline = {'incident': 0, 'detected': 5, 'triaged': 8, 'requested': 10, 'approved': 28, 'contained': 32}
check('request-to-decision wait', timeline['approved'] - timeline['requested'], 18)
check('decision-to-action time', timeline['contained'] - timeline['approved'], 4)
check('detection-to-containment', timeline['contained'] - timeline['detected'], 27)
identity_ready = timeline['contained'] + 12
data_ready = timeline['contained'] + 8
app_ready = max(identity_ready, data_ready) + 15
business_ready = app_ready + 10
check('identity readiness', identity_ready, 44)
check('data readiness', data_ready, 40)
check('application readiness', app_ready, 59)
check('business readiness', business_ready, 69)
check('application within chosen target', app_ready <= 60, True)
check('business misses chosen RTO', business_ready <= 60, False)
check('recovery point gap', timeline['incident'] - (-20), 20)
check('chosen RPO missed', 20 <= 15, False)

print(json.dumps(dict(
    passed=len(checks), checks=checks,
    results=dict(joint_independent=float(independent_both), joint_common=float(common_both),
                 expected_combined_loss=int(expected_total), target_plus_cost=int(after + annual_cost),
                 verified_coverage=0.75, reporter_only_coverage=0.9375,
                 supplier_current_fraction=0.4, approval_wait_minutes=18,
                 app_ready_minute=app_ready, business_ready_minute=business_ready),
    boundary='Arithmetic and fictional decision rules executed locally. No real risk acceptance, organizational assessment, incident, supplier validation or restore.'
), indent=2))
```

## Eight practical labs

**Proposed activities, not executed in this review.** Use synthetic data and an authorized disposable environment for operational work. Keep the management decision and its evidence separate from merely completing a worksheet.


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

## Answer notes

These explain the original prompts; they are not an official answer key or a prediction of exam items.

1. The accountable business/risk owner accepts residual risk within delegated authority; security advises and escalates beyond that authority.
2. The governing body retains oversight, direction and accountability for the risk/governance framework; management executes delegated responsibilities.
3. Policy sets mandatory direction; a standard specifies required detail; a procedure gives steps; a guideline offers advice. Publish the applicable authority and exception process.
4. An exception has scope, reason, compensating controls, owner, authorized approval, expiry, review triggers and an action if conditions change.
5. Enterprise objectives, obligations, appetite, architecture, threat context, current capability, culture and resources drive the strategy.
6. State the business outcome, options, lifecycle cost, benefits, risk/uncertainty, dependencies, ownership, decision and consequence of delay.
7. Tool count measures inventory, not reduced exposure or dependable business capability. Explain coverage, effectiveness and consequences instead.
8. State assumptions, evidence age, ranges, missing data and how the decision changes under plausible alternatives; do not disguise unknowns as zero risk.
9. A threat can cause harm; a vulnerability is a susceptible condition that may enable it. Neither alone establishes a complete business-risk scenario.
10. Example: an attacker steals a supplier support token, accesses customer records and causes disclosure and service interruption. Identify assets, conditions and impact assumptions.
11. Appetite sets broad willingness to take risk; tolerance makes boundaries usable for particular objectives. Define their meaning consistently within the organization.
12. Inherent exposure excludes the controls under consideration; residual exposure remains after a response. Keep current operating exposure and projected target exposure distinct.
13. Technical severity omits business criticality, exposure, exploitability, compensating controls, dependencies and consequences.
14. Escalate when exposure exceeds delegated limits, assumptions change, authority expires or obligations need resolution. Acceptance cannot waive every requirement.
15. The risk owner is accountable for the exposure, the control owner operates a safeguard, and the action owner delivers a treatment task; one person may have multiple clearly stated roles.
16. Define the signal, threshold, population, window, evidence quality, owner and decision/action it triggers. A colored dashboard alone is not a response.
17. Shared causes can defeat multiple safeguards simultaneously. Normalize and investigate joint impacts without double counting losses or simply adding ordinal scores.
18. New data use, provider, threat, acquisition, incident, control failure, expiry or material obligation can invalidate the earlier assessment.
19. A program sustains coordinated capabilities and outcomes; a project delivers a bounded change that may contribute to the program.
20. Use risk to sequence authoritative inventory, ownership, identity, configuration, telemetry, response and recovery; no universal shopping list replaces assessment.
21. The accountable information/business owner decides classification with security/privacy guidance; custodians implement handling requirements.
22. Classification informs access, sharing, storage, encryption, logging, retention, recovery and disposal across originals, copies and derived data.
23. Show how the control's design meets its objective for the actual threats, population and dependencies; a policy sentence or purchased product is insufficient.
24. Obtain relevant evidence over the required population and period, investigate exceptions and verify corrective action. A configured control is not necessarily an operating control.
25. Trace the business objective to risk, capability, control evidence and outcome; disclose numerator, denominator, time window and scope changes.
26. Attendance shows exposure to training. Observe role-relevant behavior, reporting, errors, coaching and trends without assuming any single simulation proves competence.
27. Check scope, period, exceptions, subservice treatment, assurance type and customer responsibilities. Current documentation remains only part of assurance.
28. Assess shared providers, jurisdictions, privileged dependencies, subcontractor changes, portability, termination rights and a tested continuity/exit route.
29. BIA identifies impacts and priorities; BCP sustains business; DRP restores technology; incident response coordinates detection, investigation, containment and recovery of the incident.
30. Follow documented delegated authority with alternates and escalation. A security tool's severity label does not itself declare an enterprise crisis.
31. Consider affected services/data, scope, operational and safety impact, urgency, confidence and applicable obligations; reassess as facts change.
32. Weigh evidence needs with safety, ongoing harm and continuity under approved procedures. Preservation does not justify unlimited delay of containment.
33. Containment limits spread, eradication removes causes/persistence, and recovery restores trusted operations with validation. Activities may overlap or iterate.
34. Verify restoration inputs, identity/keys, restored assets, root-cause treatment, dependencies, monitoring and business-owner validation before the relevant reconnection decision.
35. Use qualified review for breach notices, regulator/customer statements, evidence disclosure and other legally sensitive communications; apply actual jurisdictions and contracts.
36. Record time, known facts, uncertainty, options, decision, authority, rationale, action owner, evidence reference and revisit trigger; protect the record.
37. A tabletop exercises discussion and decisions; a technical recovery test executes restoration and validates operation. Each has different evidence and limits.
38. Assign an owner, due date and measurable criterion, implement the change, retest effectiveness and update plans/risk. Closing a ticket is insufficient.
39. Incorrect scope, weak confidence, excess privileges or unavailable override can spread disruption. Limit authority, monitor outcomes and test failure/rollback paths.
40. Identify the authorized outcome and constraints, then perform or invoke the appropriate action. Do not add approval delay to an action already safely preauthorized by the incident plan.

## Places to learn

This is not a complete list. Choose resources for your measured gaps and intended exam date. Estimates are study budgets unless an observed duration is explicitly labeled. Older courses can teach transferable concepts; they do not establish complete November alignment.

| Best use and version boundary | Resource | Access | Estimated time |
|---|---|---|---:|
| Current 35 subtopics and 37 tasks; recheck before scheduling | [Official outline](https://www.isaca.org/credentialing/cism/cism-exam-content-outline) | Public | 30–60 min |
| Confirmed November date, weights and architecture additions; not the complete future tasks | [September 10 update](https://www.isaca.org/about-us/newsroom/press-releases/2026/isaca-updates-cism-exam-content-outline-factoring-in-todays-technologies-security-responsibilities) | Public | 10–15 min |
| Detailed future explanation remains blocked in this review | [2026 job-practice FAQ](https://support.isaca.org/s/article/Certification-CISM-Job-Practice-Update-2026) | Public route; timed out | Verify availability |
| Policies and 2022 CISM appendix; selected pages read | [Candidate guide](https://www.isaca.org/credentialing/-/media/fa494652c5f149289af38cef18328650.ashx) | Public PDF | 60–90 min |
| Public listing retains old-material warning; verify the exact version and access | [Online review course](https://www.isaca.org/store2/product/CISM-ORC-C) | Paid; public description read | About 16 hr stated; 20–30 hr study budget |
| Current manual route returned a shell; exact edition/interior not verified | [Review manual](https://www.isaca.org/store2/product/CISM-RM-C) | Paid | 20–35 hr study budget |
| Landing page advertises 1,047 items/six months; current product route unreadable, so verify November alignment and pool | [Certification and QAE route](https://www.isaca.org/credentialing/cism) | Public/paid | 25–45 hr study budget |
| Ten-item style sample advertised; item contents/submission not reviewed | [Official free quiz](https://www.isaca.org/credentialing/cism/cism-practice-quiz) | Public/form | 15–25 min |
| Supplementary explanations; access returned 403 and prior duration was not reverified | [O'Reilly — Peter H. Gregory](https://www.oreilly.com/videos/certified-information-security/0642572021955/) | Paid | Prior 8 hr 2 min; verify live |
| Supplementary explanations; access returned 403 and prior duration was not reverified | [O'Reilly/Packt — ACI Learning](https://www.oreilly.com/videos/certified-information-security/9781835881309/) | Paid | Prior 13 hr 49 min; verify live |
| Public Cybrary listing/TOC, May 20, 2025; no November alignment or lesson-quality verification | [LinkedIn Learning CISM Cert Prep](https://www.linkedin.com/learning/isaca-certified-information-security-manager-cism-cert-prep) | Paid/trial | 9 hr 22 min stated |
| Access blocked; exact revision, duration and lessons unverified | [Udemy — Hemang Doshi](https://www.udemy.com/course/hemang-doshi-cism/) | Paid | Verify live duration |
| Governance and outcomes; related practice, not exam scope | [NIST CSF 2.0](https://www.nist.gov/cyberframework) | Public | 1–2 hr selected |
| Risk-register meaning, ownership and enterprise reporting; selected PDF pages read | [NIST IR 8286 Rev. 1](https://csrc.nist.gov/pubs/ir/8286/r1/final) | Public | 3–6 hr selected |
| Readiness, response authority, evidence and recovery; selected PDF pages read | [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | Public | 3–5 hr selected |
| Experience/application versus sitting the exam; no personal eligibility decision | [Certification requirements](https://www.isaca.org/credentialing/cism/get-cism-certified) | Public | 10–15 min |
| Current obligations and dated transition; personal cycle remains unverified | [Maintenance](https://www.isaca.org/credentialing/cism/maintain-cism-certification) and [2027 CPE policy](https://www.isaca.org/credentialing/cpe-2027) | Public | 20–30 min |
| Objectivity, competence, significant facts and confidentiality | [ISACA ethics](https://www.isaca.org/code-of-professional-ethics) | Public | 10–15 min |

Reject dumps, recalled or “actual” questions and guaranteed-pass products. Match materials to the date-specific official scope; neither a marketing title nor a large question pool proves complete coverage.
