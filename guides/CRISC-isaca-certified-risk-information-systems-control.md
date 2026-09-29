---
exam_code: CRISC
vendor_id: isaca
official_blueprint: https://www.isaca.org/credentialing/crisc/crisc-exam-content-outline
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# Certified in Risk and Information Systems Control (CRISC) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Reviewed September 29, 2026. The guide maps 44 entries in the live domain lists and 24 supporting tasks, answers 40 original prompts, and adds three worked scenarios plus 52 executed offline checks. Eight broader activities remain proposed. See the [coverage record](../docs/SOURCE-VALIDATION.md#crisc-coverage-record) and [research record](../docs/research/2026-09-29-crisc-deep-review.md).

**CURRENT BLUEPRINT:** Governance 26%; Risk Assessment 22%; Risk Response and Reporting 32%; Technology and Security 20%. ISACA's [April 2025 announcement](https://www.isaca.org/about-us/newsroom/press-releases/2025/isaca-updates-cdpse-and-crisc-exams-to-reflect-latest-risk-and-privacy-priorities) dates this version to **November 3, 2025**, with materials from September 3, 2025. No later replacement or retirement appeared in the official sources examined on the review date. These are historical effective dates, not an upcoming 2026 cutover.

**Scope-count detail:** The live HTML lists 44 domain entries. The candidate PDF has 43 numbered subtopics because it uses **Technology Principles** as the domain 4A heading, while the HTML lists that phrase as an additional entry beneath a different heading. Both have the same weights and 24 supporting tasks. The map preserves every canonical HTML entry and teaches the heading concept; the count difference does not establish an added exam objective or a silent scope revision.

**Exam versus designation:** Anyone may sit the 150-question, four-hour exam. The candidate guide lists a scaled 200–800 range with 450 passing; 450/800 is not a raw-percent passing rule. Public fees are US$575 member/US$760 nonmember, with six-month eligibility. Designation requires three years of qualifying experience across at least two domains, gained within the ten years before application; **CRISC has no experience waivers or substitutions** in the candidate guide. Apply within five years of passing, obtain experience verification and pay the US$50 application fee. Personal eligibility was not assessed. [Candidate guide](https://www.isaca.org/credentialing/-/media/fa494652c5f149289af38cef18328650.ashx), [requirements](https://www.isaca.org/credentialing/crisc/get-crisc-certified).

**VERIFY CURRENT — scheduling and maintenance:** Retake rules permit four attempts in a rolling 12 months, with 30 days after the first failure and 90 after later failures. Reschedule at least 48 hours ahead; appointment availability and eligibility extension rules are separate. Current maintenance requires 20 CPE annually, 120 over three years and annual fees of US$45 member/US$85 nonmember. From January 1, 2027, the revised framework requires at least 90 aligned hours and allows up to 30 other qualifying professional-development hours; all 120 may align. Individual caps and records still matter. The current webpage's 12-month retention after a cycle differs from the linked new policy's minimum three years; verify the applicable transition before making a personal recordkeeping decision. [Maintenance](https://www.isaca.org/credentialing/crisc/maintain-crisc-certification), [2027 changes](https://www.isaca.org/credentialing/cpe-2027).

**Resource verification:** The current certification landing advertises **833 QAE items and six-month access**, correcting this guide's earlier 600-item figure. The individual course, QAE and manual store routes rendered application shells, so exact product editions, interiors and course duration remain unverified. Public Pluralsight course durations total 5 hours 19 minutes beneath a rounded five-hour headline; LinkedIn/Cybrary lists 6 hours 3 minutes. Paid content was not reviewed. [Official preparation page](https://www.isaca.org/credentialing/crisc).

**Integrity and execution:** Original prompts and examples are not recalled or predicted questions. The free quiz was fetched but its items were not reviewed or submitted. Execution used synthetic data, a local public schema copy, an existing Python/jsonschema installation and a seeded simulation. No account, purchase, organizational control, infrastructure or approval was exercised.

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

### Make escalation a decision process

State the business objective, decision maker, delegated limit, evidence requirements, expiry and review trigger. Separate the person accountable for risk from the operator of a control, the owner of a remediation action and the independent assessor. A process can assign multiple roles to one person only where conflicts and assurance needs are addressed; a RACI should not hide ownership in a committee name. Report significant contrary evidence rather than smoothing it out of the dashboard. [ISACA ethics](https://www.isaca.org/code-of-professional-ethics) supports objectivity, due care, competence and disclosure of material facts.

**PRACTICAL DEPTH:** A treatment backlog does not itself constitute authorized risk acceptance. If a mitigation slips, state the exposure during the delay, interim controls, changed assumptions and decision needed. [NIST IR 8286B](https://csrc.nist.gov/pubs/ir/8286/b/upd1/final) discusses implicit acceptance and the need to record and monitor deferred responses. Escalation thresholds, senior decision authority and organization-specific obligations still apply. The document's federal examples are not universal legal procedures.

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

### Check what the numbers mean

Choose methods based on the decision and evidence available. [NIST IR 8286A Rev. 1](https://csrc.nist.gov/pubs/ir/8286/a/r1/final) discusses estimation, bias, event trees and simulation. Seek independent initial estimates before group discussion, challenge optimism and recent-event bias, and record assumptions that would change the recommendation. A model does not supply empirical support for its own inputs.

An event tree uses conditional probabilities at each branch. In the workbook's fictional annual scenario, an initiating event has probability 0.2; the first control fails with probability 0.3 given that event; the second fails with probability 0.4 given that earlier failure. The resulting loss probability is 0.024 and modeled expected loss is US$24,000 for a US$1 million consequence. The four mutually exclusive leaves sum to one. Multiplying unrelated marginal control-failure rates would not establish the same result; investigate common causes and define the conditioning clearly.

For a different example, conditional loss magnitude follows an explicitly chosen triangular distribution with minimum US$20,000, mode US$40,000 and maximum US$100,000. Its mean is approximately US$53,333 and its probability of exceeding US$60,000 is one-third. A 100,000-draw seeded simulation actually ran and produced approximately US$53,287 and 33.159%, respectively. These are results of the chosen model, not measured enterprise loss probabilities. More draws reduce numerical sampling variation; they cannot repair an unrealistic distribution or missing scenarios. A differently weighted three-point mean, about US$46,667 here, represents different assumptions.

Do not label every range a confidence interval. A model's loss percentiles, a sensitivity range across assumptions and a confidence interval for a population mean answer different questions. The [NIST statistics handbook](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm) describes confidence for the mean as a property of an interval-producing method across repeated samples. The IR 8286A three-point passage has arithmetic and interval-interpretation inconsistencies, so its numerical confidence example is not adopted here. The workbook instead compares its simulation with an explicitly specified distribution and analytic result.

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

### Separate a valid register from a supported decision

The [NIST risk-register JSON schema](https://csrc.nist.gov/files/pubs/ir/8286/r1/final/docs/risk_register_schema.json) checks required fields, basic types and allowed response values. Its likelihood field is a **percentage**, so 25 means 25%, not 0.25%. The published schema does not set numerical bounds, require a nonempty owner, check an exposure equation or constrain status to an organizational vocabulary. The workbook actually validates records against that unmodified schema: missing fields, invalid types and duplicate response values fail, while a 120% likelihood, empty owner and inconsistent exposure can pass structural validation. Separate exercise rules flag those gaps.

Those extra rules are deliberately narrow. The example equation assumes one loss scenario, one time horizon and probability multiplied by conditional loss magnitude. It is not a universal formula for repeated-event frequency models, positive opportunities, distributions or qualitative scales. Even a complete, arithmetically consistent record needs source evidence, freshness, units, uncertainty, decision authority and links to the detailed assessment. A status of `planned` does not prove that treatment is implemented or effective. [NIST IR 8286 Rev. 1](https://csrc.nist.gov/pubs/ir/8286/r1/final) explains how a concise register relates to a detailed risk record and enterprise reporting.

### Compare feasible treatment portfolios

Compare costs and benefits on a consistent time basis, include dependencies, and avoid double counting overlapping effects. The workbook enumerates all 16 subsets of four fictional actions with annual costs and projected additive benefits, in thousands of dollars. With a US$65,000 budget, inventory plus identity gives the largest modeled benefit, US$120,000 for US$60,000 cost. Identity and logging both require inventory; selecting them without that prerequisite is infeasible. Duplicate and unknown actions are rejected.

If leadership requires a recovery capability in this planning period, the feasible choice changes to inventory plus recovery: US$65,000 cost and US$115,000 projected benefit. The arithmetic does not decide whether that requirement is appropriate, whether the benefits are credible, or whether the eventual implementation meets it. Document obligations, nonfinancial effects, delivery capacity, interactions and residual exposure, then obtain the authorized decision. [NIST IR 8286B](https://csrc.nist.gov/pubs/ir/8286/b/upd1/final) distinguishes prioritization criteria and optimization approaches; it does not prescribe choosing the highest calculated value in every case.

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

### Follow evidence across changing technology

For a cloud migration or acquisition, trace business process → information → application → identity/network/provider dependencies → control owner → evidence. A service-level commitment for one component does not establish the business's recovery capability. Define how customer configuration, supplier assurance and tests of the complete dependency chain support the control claim. Track the version, scope and period of each artifact; an old architecture diagram cannot prove the current boundary.

For AI-assisted delivery, evaluate the actual workflow: which data may leave, which identities can propose or approve changes, whether tests and reviews cover the relevant repositories, how changes are attributable, and how an unsafe result is contained. Completion counts, licenses and a syntactically valid risk record are inputs rather than outcome evidence. Reassess when models, permissions, providers or data purposes change. These are practical applications of architecture, SDLC, privacy and emerging-technology topics, not claims that a named tool is required by CRISC.

## Integrated scenarios

### Scenario 1 — Cloud analytics migration

Connect migration objectives to governance and appetite. Map sensitive data, identities, regions and supplier dependencies; write leakage, integrity, availability and lock-in scenarios; assess controls and concentration; compare redesign, phased migration, contractual transfer and acceptance; assign treatment owners; define KCIs/KRIs; and test end-to-end restore and exit.

### Scenario 2 — AI-assisted software delivery

Identify source-code leakage, insecure suggestion, dependency, license, prompt injection and over-automation scenarios. Define acceptable-use governance, data boundaries, review/testing, provenance, secrets, monitoring and incident handling. Measure escaped defects, override behavior and repository coverage rather than license count. Reassess as models, agents or suppliers change.

### Scenario 3 — Acquisition risk integration

Inventory critical processes, identities, data, networks, contracts and unsupported systems. Aggregate inherited risks, establish interim segmentation and privileged controls, prioritize by business transition, preserve accepted-risk authority, and report what must be decided before connectivity. Plan architecture convergence, control testing, continuity and supplier exits.

## Worked results for the three scenarios

1. **Cloud analytics migration:** Identify the business owner, data categories and supplier/identity dependencies before selecting controls. Use the four-leaf event tree to make conditioning explicit, but request evidence for its 20%/30%/40% assumptions before treating US$24,000 as an enterprise estimate. In the separate conditional-magnitude example, the modeled one-third probability of exceeding US$60,000 may matter more to tolerance than the mean alone. Preserve source/period and unknowns in the detailed record. Recommend phased migration only with approved boundaries, verified control evidence and a tested recovery/exit path; no migration or restore was executed.
2. **AI-assisted delivery:** A register that passes JSON validation can still name no accountable owner or claim a 120% likelihood. Resolve those data defects before reporting. Record the data boundary, contributor/reviewer/approver roles, code and dependency checks, privileged actions, incident route and measured population. A `planned` review control is not operating evidence. Use role-relevant tests and representative change records to assess the design and operation; no AI model or software-delivery control was tested here.
3. **Acquisition integration:** Inventory ownership and control dependencies before connecting environments. Under the fictional annual budget, inventory plus identity has the largest projected additive benefit. If recovery is mandatory for the integration milestone, choose the feasible inventory-plus-recovery plan in the model and explicitly escalate the identity gap, interim exposure and funding/sequence decision. Do not treat the unselected item as silently accepted, or the selected item as already effective. Preserve separate business units' periods, currencies and assumptions when combining risks.

## Executed offline risk workbook

The code below passed **52 checks**, including validation against the complete public schema, a 100,000-draw seeded simulation and enumeration of all 16 treatment subsets. It requires Python and `jsonschema`; version 4.26.0 was already present in the review environment. Save the [public JSON schema](https://csrc.nist.gov/files/pubs/ir/8286/r1/final/docs/risk_register_schema.json) locally and pass its path as the first argument when running a saved copy of this script. No network request occurs in the script. The run records the schema hash so later changes are distinguishable.

All probabilities, costs, benefits, mandatory choices and extra decision rules are fictional. Numerical checks do not establish empirical risk, real control effectiveness or authorization. The eight broader activities below were not executed.

```python
"""Offline fictional risk models. Pass a local copy of the linked NIST JSON schema."""
from fractions import Fraction as F
import hashlib
from importlib.metadata import version
from itertools import combinations
import json
from pathlib import Path
import random
from statistics import mean
import sys
from jsonschema import Draft202012Validator

checks = []


def check(name, actual, expected):
    if actual != expected:
        raise AssertionError((name, actual, expected))
    checks.append(name)


schema_bytes = Path(sys.argv[1]).read_bytes()
schema = json.loads(schema_bytes)
Draft202012Validator.check_schema(schema)
validator = Draft202012Validator(schema)
record = dict(riskId='R-1', riskDescription='Stolen supplier token discloses records',
              riskCategory='Information disclosure', riskLikelihood=25,
              riskImpact=200_000, exposureRating=50_000,
              riskResponseType=['Mitigate'], riskResponseCost=10_000,
              riskResponseDescription='Restrict token privileges and test access boundaries',
              riskOwnerPointOfContact='Customer service owner', status='planned')
check('complete synthetic record has valid structure', validator.is_valid(record), True)
check('missing identity rejected', validator.is_valid({k: v for k, v in record.items() if k != 'riskId'}), False)
check('percentage text rejected', validator.is_valid(dict(record, riskLikelihood='25%')), False)
check('empty response list rejected', validator.is_valid(dict(record, riskResponseType=[])), False)
check('duplicate response rejected', validator.is_valid(dict(record, riskResponseType=['Mitigate', 'Mitigate'])), False)
check('unknown response rejected', validator.is_valid(dict(record, riskResponseType=['Ignore'])), False)
check('array instead of record rejected', validator.is_valid([record]), False)


def decision_data_errors(row):
    """Chosen exercise rules, additional to the unmodified NIST schema."""
    errors = []
    if not row['riskId'].strip():
        errors.append('empty risk ID')
    if not row['riskOwnerPointOfContact'].strip():
        errors.append('empty owner')
    if not 0 <= row['riskLikelihood'] <= 100:
        errors.append('likelihood outside percentage range')
    if row['riskImpact'] < 0 or row['riskResponseCost'] < 0:
        errors.append('negative cost or impact in loss-only model')
    expected = F(row['riskLikelihood']) * row['riskImpact'] / 100
    if F(row['exposureRating']) != expected:
        errors.append('inconsistent illustrative expected loss')
    if row['status'] not in {'assessed', 'planned', 'implemented', 'accepted'}:
        errors.append('unknown local status')
    return errors


check('valid record passes chosen extra rules', decision_data_errors(record), [])
bad_rows = [
    ('blank owner', dict(record, riskOwnerPointOfContact=''), 'empty owner'),
    ('blank risk ID', dict(record, riskId=''), 'empty risk ID'),
    ('percentage above 100', dict(record, riskLikelihood=120), 'likelihood outside percentage range'),
    ('negative percentage', dict(record, riskLikelihood=-1), 'likelihood outside percentage range'),
    ('wrong exposure', dict(record, exposureRating=1), 'inconsistent illustrative expected loss'),
    ('unknown status', dict(record, status='banana'), 'unknown local status'),
    ('negative response cost', dict(record, riskResponseCost=-1), 'negative cost or impact in loss-only model'),
]
for name, row, expected_error in bad_rows:
    check(name + ' passes structural schema', validator.is_valid(row), True)
    check(name + ' fails extra decision rule', expected_error in decision_data_errors(row), True)
check('local extension permitted structurally', validator.is_valid(dict(record, assessmentPeriod='one year')), True)
check('planned remains planned', record['status'], 'planned')
check('schema validation does not mutate source record', record['exposureRating'], 50_000)

event = F(1, 5)
first_fails_given_event = F(3, 10)
second_fails_given_first = F(2, 5)
leaves = {
    'no initiating event': 1 - event,
    'first control stops event': event * (1 - first_fails_given_event),
    'second control stops event': event * first_fails_given_event * (1 - second_fails_given_first),
    'loss event': event * first_fails_given_event * second_fails_given_first,
}
check('event tree conserves probability', sum(leaves.values()), 1)
check('all leaf probabilities valid', all(0 <= p <= 1 for p in leaves.values()), True)
check('conditional loss probability', leaves['loss event'], F(3, 125))
check('illustrative expected loss', leaves['loss event'] * 1_000_000, 24_000)
check('second-stage success leaf', leaves['second control stops event'], F(9, 250))
check('first-stage success leaf', leaves['first control stops event'], F(7, 50))

low, mode, high = 20, 40, 100  # Thousands of dollars, conditional on a loss.
triangular_mean = F(low + mode + high, 3)
triangular_variance = F(low**2 + mode**2 + high**2 - low*mode - low*high - mode*high, 18)
check('triangular mean', triangular_mean, F(160, 3))
check('triangular variance', triangular_variance, F(2600, 9))
check('weighted three-point mean differs', F(low + 4*mode + high, 6), F(140, 3))


def triangular_cdf(x):
    if x <= low:
        return F(0)
    if x >= high:
        return F(1)
    if x <= mode:
        return F((x-low)**2, (high-low)*(mode-low))
    return 1 - F((high-x)**2, (high-low)*(high-mode))


check('lower support CDF', triangular_cdf(low), 0)
check('upper support CDF', triangular_cdf(high), 1)
check('mode CDF', triangular_cdf(mode), F(1, 4))
check('exceedance of 60', 1 - triangular_cdf(60), F(1, 3))
rng = random.Random(20260929)
samples = [rng.triangular(low, high, mode) for _ in range(100_000)]
simulated_mean = mean(samples)
simulated_exceedance = sum(x > 60 for x in samples) / len(samples)
check('actual simulation sample count', len(samples), 100_000)
check('simulation stays in chosen support', all(low <= x <= high for x in samples), True)
check('simulation mean agrees within 0.3 thousand', abs(simulated_mean - float(triangular_mean)) < 0.3, True)
check('simulation exceedance agrees within 0.01', abs(simulated_exceedance - 1/3) < 0.01, True)

# Costs and projected benefits are annual, in thousands, additive by assumption.
actions = {
    'inventory': dict(cost=20, benefit=20, requires=set()),
    'identity': dict(cost=40, benefit=100, requires={'inventory'}),
    'recovery': dict(cost=45, benefit=95, requires=set()),
    'logging': dict(cost=15, benefit=25, requires={'inventory'}),
}
budget = 65


def portfolio(names, mandatory=frozenset()):
    selected = set(names)
    if len(selected) != len(names) or not selected <= actions.keys():
        return None
    cost = sum(actions[n]['cost'] for n in selected)
    if cost > budget or not mandatory <= selected:
        return None
    if any(not actions[n]['requires'] <= selected for n in selected):
        return None
    return cost, sum(actions[n]['benefit'] for n in selected)


choices = [tuple(c) for size in range(5) for c in combinations(actions, size)]
check('all four-action subsets considered', len(choices), 16)
check('identity without prerequisite rejected', portfolio(('identity',)), None)
check('duplicate action rejected', portfolio(('inventory', 'inventory')), None)
check('unknown action rejected', portfolio(('magic',)), None)
check('over-budget portfolio rejected', portfolio(tuple(actions)), None)
feasible = [(names, portfolio(names)) for names in choices if portfolio(names) is not None]
best_names, best_values = max(feasible, key=lambda item: item[1][1])
check('largest projected additive benefit', set(best_names), {'inventory', 'identity'})
check('best portfolio annual cost and benefit', best_values, (60, 120))
mandatory = frozenset({'recovery'})
constrained = [(names, portfolio(names, mandatory)) for names in choices if portfolio(names, mandatory) is not None]
required_names, required_values = max(constrained, key=lambda item: item[1][1])
check('mandatory recovery changes portfolio', set(required_names), {'inventory', 'recovery'})
check('constrained annual cost and benefit', required_values, (65, 115))
check('old optimum violates required outcome', portfolio(best_names, mandatory), None)

print(json.dumps(dict(
    passed=len(checks), checks=checks, jsonschema_version=version('jsonschema'),
    schema_sha256=hashlib.sha256(schema_bytes).hexdigest(),
    results=dict(loss_event_probability=float(leaves['loss event']),
                 triangular_mean=float(triangular_mean), simulated_mean=simulated_mean,
                 simulated_exceedance=simulated_exceedance,
                 unconstrained_portfolio=list(best_names), constrained_portfolio=list(required_names)),
    boundary='Actual offline schema validation, seeded simulation and enumeration. Inputs and decision rules are fictional; no empirical risk estimate, organizational control test or real approval.'
), indent=2))
```

## Eight practical labs

**Proposed activities, not executed in this review.** Use synthetic records and an authorized environment. Keep scope, evidence and limitations with each conclusion.


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

## Answer notes

These explain the original prompts; they are not an official answer key or a prediction of exam items.

1. Governance evaluates needs, directs and oversees; management plans and executes within that direction and reports outcomes.
2. The accountable business/process risk owner owns exposure to the objective; a risk practitioner facilitates analysis and reporting.
3. The control owner maintains design, implementation, operation, evidence, exceptions and improvement for an assigned safeguard.
4. Management's operational and risk/compliance roles own and oversee activity; internal audit provides independent assurance. Define actual responsibilities and conflicts rather than relying on a diagram alone.
5. Connect appetite to enterprise objectives and actionable decisions, with tolerances, delegated authority, reporting and reassessment.
6. Tolerance makes boundaries usable for particular objectives. Define the measure, period, acceptable variation and action if it is exceeded.
7. State scope, rationale, controls, owner, assessment, authorized approval, expiry and triggers; unresolved exceptions cannot disappear from reporting.
8. Inventory establishes the population, ownership and dependencies. Missing or stale assets can conceal exposure and distort control coverage.
9. Example: a stolen supplier support token accesses analytics records and causes disclosure. Name the conditions, assets and impact assumptions needed to assess it.
10. A threat can cause harm, a vulnerability is a susceptible condition, and a control deficiency is a weakness against an intended control objective; relate them within a scenario.
11. It traces plausible actors, abuse paths and trust boundaries against a specific architecture, complementing enterprise-level scenario identification.
12. The BIA identifies critical processes, impacts over time, dependencies, recovery priorities and business-owned recovery objectives.
13. Use qualitative analysis when it supports the decision and available evidence, with consistent criteria and explicit uncertainty; do not present ordinal scores as currency.
14. Fragile assumptions include time horizon, conditional probabilities, dependence, distribution shape, loss scope, double counting, data quality and control effectiveness.
15. Inherent risk excludes the chosen controls; residual risk remains after response. Define current operating and projected target exposure explicitly rather than mixing them.
16. Common dependencies can cause simultaneous losses or defeat several controls. Normalize assumptions and joint impacts without adding ordinal scores or duplicating one business loss.
17. Keep scenario, owner, criteria, evidence, current assessment, response, residual/target distinction, actions, indicators, decisions and review dates, with a linked detailed record.
18. Changes to threats, architecture, data use, suppliers, ownership, obligations, incidents, evidence or treatment delivery can invalidate the assessment.
19. Avoid stops the risk-generating activity, mitigate changes likelihood/impact, transfer/share reallocates some consequences or duties, and accept retains risk under authority and monitoring.
20. Contracts or insurance may cover limited losses; exclusions, provider failure, residual obligations, reputation and enterprise accountability remain.
21. A designated risk owner with sufficient delegated authority accepts it, subject to constraints and escalation. A tool or analyst does not acquire authority by calculating a score.
22. Specify action, owner, resources, due date, interim exposure, dependency, acceptance criterion and evidence of completion/effectiveness.
23. Define the organization's vocabulary: a finding is an assessed observation, an issue needs resolution, and an exception is an approved departure with conditions. Names alone do not establish approval.
24. Check service, period, report type, scope, exceptions, subservice treatment and customer controls; a current report is an input rather than complete assurance.
25. Show how the design addresses the scenario/control objective for the intended population, including dependencies and failure handling.
26. Examine relevant configuration and execution evidence across the needed population and period, investigate exceptions and reperform appropriate procedures.
27. The wrong control can operate perfectly, or a dependency can fail. Link operation to the actual risk-reduction objective and test that relationship.
28. Demonstrate that it meets the original objective adequately within approved constraints; document residual gaps, authority and reassessment.
29. A KRI signals exposure, a KCI signals control condition, and a KPI measures performance/outcome. Classification depends on the decision and definition, not merely the label.
30. Specify population, formula, window, owner, evidence freshness and the action/escalation when a boundary is reached.
31. Heat maps can hide unequal scales, uncertainty, movement within a cell, shared causes, consequence tails and aggregation errors.
32. Request a concrete decision about exposure, appetite, resources or priorities, with alternatives, uncertainty, owner and consequence of delay.
33. Map shared identities, regions, suppliers, networks and data paths across services; two contracts may still depend on the same failure point.
34. Short delivery cycles still need traceable requirements, review, testing, authorized deployment and rollback evidence appropriate to risk.
35. Creation, copies, sharing, retention and disposal change who can access data and what persists. Include derived data, backups and logs in the scenario.
36. Replication can copy corruption or malicious changes. Recovery needs trustworthy inputs, dependencies, restoration and business validation.
37. Business owners establish objectives from impacts and obligations, with technical feasibility input. A vendor's default setting does not set enterprise tolerance.
38. Privacy includes appropriate purposes, transparency, minimization, rights and lifecycle obligations as well as protecting personal data; applicable requirements need competent interpretation.
39. Responsibilities depend on the service and contract, but customers commonly retain identity, configuration, data handling, authorized use and monitoring of their obligations.
40. State the business outcome, feasible options, evidence, cost/uncertainty, residual exposure and authorized decision. A product purchase alone does not establish a managed response.

## Places to learn

This is not a complete list. Choose sections that close your measured gaps. The effective-November-2025 official outline controls scope; related standards and practical exercises do not add exam requirements. Estimates are study budgets unless a publisher duration is explicitly stated.

| Best use and reading boundary | Resource | Access | Estimated time |
|---|---|---|---:|
| Canonical current lists, weights and supporting tasks | [CRISC exam outline](https://www.isaca.org/credentialing/crisc/crisc-exam-content-outline) | Public | 30–60 min |
| Exam policy and detailed appendix; selected pages read | [Candidate guide](https://www.isaca.org/credentialing/-/media/fa494652c5f149289af38cef18328650.ashx) | Public PDF | 60–90 min |
| Dates and changes for the current 2025 version | [ISACA update announcement](https://www.isaca.org/about-us/newsroom/press-releases/2025/isaca-updates-cdpse-and-crisc-exams-to-reflect-latest-risk-and-privacy-priorities) | Public | 10–15 min |
| Current 833-item/six-month QAE claim and official preparation routes; individual store descriptions remain unread | [Certification/preparation page](https://www.isaca.org/credentialing/crisc) | Public/paid | 20–30 min orientation; 20–40 hr prep budget |
| Ten-item style sample advertised; items and submission unreviewed | [Free CRISC quiz](https://www.isaca.org/credentialing/crisc/crisc-practice-quiz) | Public/form | 15–25 min |
| Six public course listings; domain courses 2025–26, exam-preparation course April 2026, lab introduction 2021; paid content unreviewed | [Pluralsight CRISC path](https://www.pluralsight.com/paths/crisctm-certified-in-risk-and-information-systems-controltm) | Paid/trial | 5 hr headline; listed videos total 5 hr 19 min |
| Access returned 403; prior duration/interior not reverified | [O'Reilly/Packt — ACI Learning](https://www.oreilly.com/videos/crisc-certified-in/9781835886465/) | Paid | Prior 16 hr 28 min; verify live |
| Public Cybrary listing/TOC, beginner, December 11, 2025; lessons unreviewed | [LinkedIn Learning CRISC Cert Prep](https://www.linkedin.com/learning/isaca-certified-in-risk-and-information-systems-control-crisc-cert-prep) | Paid/trial | 6 hr 3 min stated |
| Access returned 403; exact revision, duration and content unverified | [Udemy — Hemang Doshi](https://www.udemy.com/course/masterclass-crisc-exam/) | Paid | Prior about 19 hr; verify live |
| Governance/outcome context; full framework PDF not reviewed here | [NIST CSF 2.0](https://www.nist.gov/cyberframework) | Public | 1–2 hr selected |
| Registers, detailed records and enterprise reporting; selected pages read | [NIST IR 8286 Rev. 1](https://csrc.nist.gov/pubs/ir/8286/r1/final) | Public | 2–4 hr selected |
| Bias, estimation and analysis; selected pages, with confidence-example limitations noted | [NIST IR 8286A Rev. 1](https://csrc.nist.gov/pubs/ir/8286/a/r1/final) | Public | 3–5 hr selected |
| Prioritization, response costs/authority and deferred treatment; selected pages read | [NIST IR 8286B Update 1](https://csrc.nist.gov/pubs/ir/8286/b/upd1/final) | Public | 2–4 hr selected |
| Structure for the offline validation exercise; business criteria still required | [NIST risk-register schema](https://csrc.nist.gov/files/pubs/ir/8286/r1/final/docs/risk_register_schema.json) | Public JSON | 30–60 min |
| Clarifies confidence intervals for the mean; optional statistical depth | [NIST statistics handbook](https://www.itl.nist.gov/div898/handbook/eda/section3/eda352.htm) | Public | 20–40 min |
| Experience/application versus exam eligibility | [Certification requirements](https://www.isaca.org/credentialing/crisc/get-crisc-certified) | Public | 10–15 min |
| Current renewal obligations and separate January 2027 transition | [Maintenance](https://www.isaca.org/credentialing/crisc/maintain-crisc-certification) and [2027 CPE changes](https://www.isaca.org/credentialing/cpe-2027) | Public | 20–30 min |
| Objectivity, competence, confidentiality and material facts | [ISACA ethics](https://www.isaca.org/code-of-professional-ethics) | Public | 10–15 min |

Reject dumps, recalled or “actual” questions and guaranteed-pass products. A large question pool, polished dashboard or valid JSON record does not replace evidence and reasoned decisions.
