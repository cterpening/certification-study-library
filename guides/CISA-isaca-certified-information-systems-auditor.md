---
exam_code: CISA
vendor_id: isaca
official_blueprint: https://www.isaca.org/credentialing/cisa/cisa-exam-content-outline
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# Certified Information Systems Auditor (CISA) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The September 29, 2026 [deep review](../docs/research/2026-09-29-cisa-deep-review.md) maps 60 subtopics and 43 supporting tasks, answers 40 original prompts and adds three worked scenarios plus 47 executed Python/SQLite checks. Eight broader activities remain proposed; organizational audit, production recovery and human review remain pending. See the [coverage record](../docs/SOURCE-VALIDATION.md#cisa-coverage-record).

**Current baseline:** Information Systems Auditing Process (18%); Governance and Management of IT (18%); Information Systems Acquisition, Development, and Implementation (12%); Information Systems Operations and Business Resilience (26%); Protection of Information Assets (26%). ISACA identifies this outline as effective August 2024.<br>
**Exam contract:** 150 multiple-choice questions in four hours, delivered at PSI test centers or by remote proctoring. Registration is continuous; eligibility lasts six months. The 2026 candidate guide lists US$575 for members and US$760 for nonmembers. Verify the live registration flow, appointment availability, identification, retake, language and price rules before purchase.<br>
**Certification contract:** Anyone may take the exam. To use the CISA designation, pass within the preceding five years, apply and pay the US$50 processing fee, and document qualifying information-systems audit, control or security experience gained within the ten years before application. The five-year experience requirement permits up to three years of waivers under the candidate guide; check the current application for eligible categories and evidence. Passing the exam alone does not make you CISA certified.<br>
**Maintenance:** ISACA currently requires at least 20 relevant CPE hours each year and 120 over three years, the annual maintenance fee, ethics, audit cooperation, and compliance with ISACA auditing standards. The [January 2027 change](https://www.isaca.org/credentialing/cpe-2027) preserves the three-year total, requires at least 90 hours aligned to the credential outline and permits up to 30 for other qualifying professional development. All 120 may still be aligned. This is a maintenance change, not a replacement exam outline.<br>
**Upcoming change:** No replacement CISA outline or retirement was announced on September 29, 2026. Technology and regulation examples change faster than the job-practice model, so recheck the official outline and candidate guide before scheduling.<br>
**Integrity:** Use ISACA's own free quiz and QAE products for official item style. The 40 prompts here are original retrieval and reasoning checks—not recalled, live, or predicted exam questions.

**VERIFY CURRENT — candidate details:** The [version 1.26 candidate guide](https://www.isaca.org/credentialing/-/media/fa494652c5f149289af38cef18328650.ashx) uses a 200–800 scaled score with 450 required to pass; 450/800 is not a raw passing percentage. It allows four attempts in a rolling 12 months, with waits of 30, then 90, then 90 days after failed attempts and a new fee each time. Rescheduling requires at least 48 hours. A single paid six-month eligibility extension is described, subject to its window and cancellation conditions. These public rules do not establish personal eligibility or an available appointment.

**VERIFY CURRENT — policy transition:** The [published CPE policy](https://www.isaca.org/-/media/files/isacadp/project/isaca/certification/general/cpe_policy.pdf), linked from the 2027 announcement, distinguishes activity limits and alignment. Its summary table's 30-hour column is not a cap on all aligned learning; the preceding rule explicitly permits 120 aligned hours. Current maintenance-page recordkeeping says 12 months after a three-year cycle, while the new policy says a minimum of three years. Keep the documents and relevant cycle together and resolve applicability with ISACA before discarding evidence. No account or CPE claim was changed here.

## How to use this guide

Start with the five-domain map and diagnose your gaps. Learn the audit decision sequence rather than memorizing isolated controls: understand the business objective, establish authority and scope, assess risk, choose suitable procedures and samples, obtain sufficient reliable evidence, evaluate design and operating effectiveness, communicate findings, and follow remediation without assuming management's responsibility.

For every topic, practice three views: what management should design, what operators should do, and what an independent auditor should verify. Use risk, authority, evidence quality and business relevance to explain your judgment. This is a study approach, not a claim to predict exam scoring or the intended answer to unseen items.

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

**CURRENT BLUEPRINT — standards and ethics:** The public [Code of Professional Ethics](https://www.isaca.org/code-of-professional-ethics) addresses objectivity, competence, confidentiality and disclosure of significant facts. ISACA [announced ITAF fifth edition on February 26, 2026](https://www.isaca.org/about-us/newsroom/press-releases/2026/isaca-launches-future-ready-it-audit-framework-update-to-strengthen-digital-trust), including an updated sampling companion. The [public listing](https://www.isaca.org/store2/product/WITAF-C?category=shop-all) offers a free package through checkout/MyISACA. This review inspected that listing, not the gated standards or companion text; it does not claim complete fifth-edition conformity. Keep mandatory standards distinct from recommended techniques.

### Execute procedures and evaluate evidence

Test design first: if a control, as described, cannot address the risk, transaction testing cannot rescue the design. Then test implementation and operating effectiveness over a representative period. Inquiry is useful but weak alone. Observation shows one moment. Inspection and reperformance usually provide stronger evidence. Evidence quality depends on sufficiency, relevance, reliability, authenticity and chain of custody—not file count.

Choose sampling to match the assertion. Statistical sampling permits quantified selection risk; nonstatistical sampling still requires a defensible method. Attribute sampling tests occurrence of a control or characteristic; variable sampling estimates amounts. Define population, sampling unit, expected error, tolerable error, confidence and treatment of exceptions before interpreting results. A convenience sample is rarely representative. Computer-assisted audit techniques and data analytics can examine full populations, but incomplete extraction, duplicate records, wrong joins, timestamps or misunderstood fields can produce confidently wrong conclusions.

Maintain workpapers so another competent auditor can understand objective, source, procedure, result, reviewer and conclusion. Protect sensitive evidence, preserve versions, record limitations and resolve contradictory evidence. A finding normally connects condition (what exists), criteria (what should exist), cause, effect/risk and recommendation. Validate facts with the process owner without surrendering auditor judgment.

**PRACTICAL DEPTH — turn criteria into procedures:** [NIST SP 800-53A revision 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final), section 2.4, links assessment objectives, objects and methods. Select suitable examination, interview and testing, with depth and breadth driven by assurance needs. Its catalog lists potential methods and evidence objects, not a requirement to perform every item. For a termination control, identify the authoritative departure time, actual target-system access and defined cutoff; interview the owner, inspect mappings and approvals, and test representative cases. The NIST assessment catalog is separate from the 800-53 control catalog. Their publication pages identify a 5.2.0 minor release; that is not a new CISA blueprint or a universal legal requirement.

The workbook intentionally constructs extracts with identical row counts and monetary totals but different payment identities. Reconcile keys, duplicates, relevant attributes, source scope and extraction logic as well as totals. A hash preserves a chosen artifact's identity; it does not authenticate its origin or prove that its content is truthful. ISACA's [June evidence-authenticity article](https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2026/the-audit-evidence-crisis-how-ai-deepfakes-are-rewriting-assurance-standards) reinforces independent corroboration; its anecdote and “zero trust” framing are author commentary, not a new exam rule.

**Sampling example:** In a known fictional population of 100 items containing 10 defects, a simple random sample of 20 without replacement has about a 9.51% chance of observing none: `C(90,20) / C(100,20)`. This calculation assumes the population defect count; real auditors usually do not know it. Zero observed exceptions cannot establish zero population defects. If different strata are sampled at different rates, pooling exceptions without weights can mislead: the workbook's raw 10% becomes a 4% population-weighted point estimate. Neither is a confidence bound or an approved sample plan.

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

**PRACTICAL DEPTH — release evidence:** The workbook checks a deliberately narrow rule: independent approval for the deployed artifact must precede deployment. A self-approval, approval for a different artifact and late approval fail that rule. A real audit must also verify identity provenance, scope, test evidence, deployment authorization and the organization's separately defined emergency-change process. A database row naming an approver is not proof that person approved it.

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

The selected BIA and recovery sections of [NIST SP 800-34 revision 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) distinguish system-resource recovery time, business tolerable downtime and the recoverable data point. Its 2010 technical examples are historical; they do not establish today's cloud design or regulatory duties. The workbook's chosen dependencies make the application available at minute 50 and business validation complete at minute 60. That meets a hypothetical 55-minute technology RTO yet misses a 58-minute business limit. A snapshot from minute 82 for an outage at minute 100 represents an 18-minute data gap, exceeding a chosen 15-minute RPO. These are modeled durations, not timings measured during the SQLite restore.

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

**PRACTICAL DEPTH — audit automated decisions:** ISACA's [September 11 agentic-workflow article](https://www.isaca.org/resources/news-and-trends/industry-news/2026/auditing-agentic-ai-workflows-how-to-control-test-when-the-system-decides-for-itself) proposes prompt/configuration review, authority tests, outcome analysis, model-change evidence and escalation checks. Extend those tests across requester identity, data access, tool actions and the policy version in force. Distribution analysis can complement transaction sampling; the article's broad suggestion to replace sampling is not a universal statistical rule. Its legal and ISO retention claims were not independently verified and are not adopted here. The workbook checks missing request evidence and a policy-version mismatch, not an AI model or legal compliance.

## Integrated scenarios

### Scenario 1 — Payroll SaaS assurance

The organization is replacing payroll with SaaS. Trace objectives through data classification, supplier due diligence, contract clauses, federation and privileged access, configuration/change controls, conversion reconciliation, UAT, logging, resilience, exit and postimplementation benefits. Identify which controls belong to the provider, customer or both. Design samples for user lifecycle and payroll changes, validate report scope, and report any inability to obtain sufficient evidence.

### Scenario 2 — Ransomware recovery claim

Management reports that recovery is “green” because backups complete nightly. Obtain the BIA, RTO/RPO, dependency map and incident history. Inspect immutability and privileged access, select backup jobs and exceptions, observe or reperform restores, recover an end-to-end business transaction, reconcile it, and compare measured results with objectives. Report replication, identity/key, supplier and communication gaps separately from backup success.

### Scenario 3 — Continuous-access audit

Build an authorized analytic for privileged access across HR, identity and target-system data. Validate population completeness, timestamps and join keys; define expected transfers and terminations; investigate exceptions; sample approvals and actual activity; protect workpapers; and have a reviewer reproduce the result. Escalate systemic feed gaps before presenting a false full-population conclusion.

### Worked results for the three scenarios

1. **Payroll SaaS:** First establish the criteria, provider/customer responsibilities, period and completeness of source payroll. In the workbook, substituting payment `p9` for `p3` preserves both three rows and 600 cents. Totals alone falsely reassure; identifier reconciliation exposes the missing and unexpected payment. Investigate cause before extrapolating loss or alleging fraud. For release assurance, only `c1` meets the chosen independent, artifact-specific prior-approval rule. Report the other evidence defects with management ownership, and keep supplier report coverage and customer controls separate.
2. **Ransomware recovery:** The local SQLite backup restores all three original payments, passes an integrity check, supports a subsequent update and continues enforcing the payment key. This is real evidence about that disposable database only. It does not test ransomware resistance, offsite independence, keys, provider recovery or production speed. The separate dependency model misses the business limit despite meeting the technology target, and its data gap misses the chosen RPO. Report each failed requirement and obtain a complete recovery exercise before concluding the service is resilient.
3. **Continuous access:** A join on user name alone yields six rows from four access events because Alex exists in two tenants; the qualified left join preserves four. Under the chosen immediate cutoff, only event `e2` is at or after tenant A Alex's termination. Tenant B Alex is distinct, pre-cutoff `e1` is outside this exception rule, and `e4` has no HR identity match. Keep `e4` as an unresolved population gap instead of silently dropping it. Validate feed coverage, effective times, approved exceptions and target-system evidence before a full-population conclusion.

## Executed offline audit workbook

All 47 assertions passed using Python's standard library and SQLite 3.50.4. Save the following as `cisa_audit_workbook.py` and run `python cisa_audit_workbook.py`. It uses three disposable in-memory databases, performs an actual backup/restore and closes them; it writes no files and contacts no service. Source rows, keys, rules and all recovery durations are fictional. The statistical calculations assume specified sampling designs and known fixture values; they are not a sample-size recommendation or certification of an audit conclusion. Hashing is not evidence authentication. No production audit, organizational approval, signed-in learning or human review was performed.

```python
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from math import comb
import json
import sqlite3

checks = []
def check(name, actual, expected):
    assert actual == expected, (name, actual, expected)
    checks.append(name)

source = [('p1', 100), ('p2', 200), ('p3', 300)]
substituted = [('p1', 100), ('p2', 200), ('p9', 300)]
check('row counts alone miss substitution', len(source), len(substituted))
check('amount totals alone miss substitution', sum(v for _, v in source), sum(v for _, v in substituted))
check('source identifiers missing from extract', sorted(set(dict(source)) - set(dict(substituted))), ['p3'])
check('unexpected extract identifiers', sorted(set(dict(substituted)) - set(dict(source))), ['p9'])
replayed = source + [source[1]]
check('duplicate identifier is visible', Counter(k for k, _ in replayed)['p2'], 2)
check('replay inflates total', sum(v for _, v in replayed), 800)

def fingerprint(rows):
    return sha256(json.dumps(sorted(rows), separators=(',', ':')).encode()).hexdigest()

check('order-independent fixture fingerprint', fingerprint(source[::-1]), fingerprint(source))
check('changed identity changes fingerprint', fingerprint(source) == fingerprint(substituted), False)
check('bad input can still have a stable hash', fingerprint(substituted), fingerprint(substituted))

population, defects, sample = 100, 10, 20
miss = Fraction(comb(population - defects, sample), comb(population, sample))
check('finite sample can miss known defects', 0 < miss < 1, True)
check('one random selection misses 90 of 100', Fraction(comb(90, 1), comb(100, 1)), Fraction(9, 10))
check('census cannot miss known defects', Fraction(comb(90, 100), comb(100, 100)), 0)
check('without replacement differs from independent draws', miss == Fraction(9, 10) ** sample, False)
check('more sampling reduces miss chance in this fixture', Fraction(comb(90, 30), comb(100, 30)) < miss, True)
check('zero exceptions does not prove zero population defects', miss > 0, True)
strata = [(20, 10, 2), (80, 10, 0)]
pooled = Fraction(sum(exceptions for _, _, exceptions in strata), sum(n for _, n, _ in strata))
weighted = sum(Fraction(size, 100) * Fraction(exceptions, n) for size, n, exceptions in strata)
check('oversampled raw exception rate', pooled, Fraction(1, 10))
check('stratum-weighted illustrative point estimate', weighted, Fraction(1, 25))
check('weighting changes the conclusion input', pooled != weighted, True)

db = sqlite3.connect(':memory:')
db.execute('PRAGMA foreign_keys=ON')
db.executescript('''
CREATE TABLE person(tenant TEXT, user_id TEXT, ended INTEGER, PRIMARY KEY(tenant,user_id));
CREATE TABLE access(event_id TEXT PRIMARY KEY, tenant TEXT, user_id TEXT, happened INTEGER);
CREATE TABLE payroll(payment_id TEXT PRIMARY KEY, cents INTEGER NOT NULL CHECK(cents >= 0));
CREATE TABLE release(change_id TEXT PRIMARY KEY, requestor TEXT, approver TEXT,
                     artifact TEXT, approved_artifact TEXT, approved_at INTEGER, deployed_at INTEGER);
''')
db.executemany('INSERT INTO person VALUES(?,?,?)', [('A','alex',120), ('B','alex',None), ('A','bea',None)])
db.executemany('INSERT INTO access VALUES(?,?,?,?)', [('e1','A','alex',119), ('e2','A','alex',120), ('e3','B','alex',130), ('e4','A','unknown',140)])
db.executemany('INSERT INTO payroll VALUES(?,?)', source)
db.executemany('INSERT INTO release VALUES(?,?,?,?,?,?,?)', [
    ('c1','maker','reviewer','v1','v1',100,110),
    ('c2','maker','maker','v1','v1',100,110),
    ('c3','maker','reviewer','v2','v1',100,110),
    ('c4','maker','reviewer','v1','v1',120,110)])
db.commit()
check('actual SQLite payroll control total', db.execute('SELECT count(*),sum(cents) FROM payroll').fetchone(), (3,600))
bad_join = db.execute('SELECT count(*) FROM access a JOIN person p ON a.user_id=p.user_id').fetchone()[0]
check('unqualified user join duplicates results', bad_join, 6)
good_join = db.execute('SELECT count(*) FROM access a LEFT JOIN person p ON a.tenant=p.tenant AND a.user_id=p.user_id').fetchone()[0]
check('qualified left join preserves every access', good_join, 4)
orphans = db.execute('SELECT a.event_id FROM access a LEFT JOIN person p ON a.tenant=p.tenant AND a.user_id=p.user_id WHERE p.user_id IS NULL').fetchall()
check('missing identity remains an evidence gap', orphans, [('e4',)])
exceptions = db.execute('SELECT a.event_id FROM access a JOIN person p ON a.tenant=p.tenant AND a.user_id=p.user_id WHERE p.ended IS NOT NULL AND a.happened >= p.ended').fetchall()
check('chosen termination rule includes exact cutoff', exceptions, [('e2',)])
check('other tenant is not falsely terminated', ('e3',) in exceptions, False)
check('pre-termination activity is not a violation of chosen rule', ('e1',) in exceptions, False)
qualified = db.execute('SELECT change_id FROM release WHERE requestor<>approver AND artifact=approved_artifact AND approved_at<=deployed_at').fetchall()
check('only complete chosen release evidence qualifies', qualified, [('c1',)])
check('self-approval isolated', db.execute('SELECT change_id FROM release WHERE requestor=approver').fetchall(), [('c2',)])
check('approval for another artifact isolated', db.execute('SELECT change_id FROM release WHERE artifact<>approved_artifact').fetchall(), [('c3',)])
check('late approval isolated', db.execute('SELECT change_id FROM release WHERE approved_at>deployed_at').fetchall(), [('c4',)])

snapshot = sqlite3.connect(':memory:')
db.backup(snapshot)
db.execute("DELETE FROM payroll WHERE payment_id='p3'")
db.commit()
check('simulated loss affects live disposable database', db.execute('SELECT sum(cents) FROM payroll').fetchone()[0], 300)
restored = sqlite3.connect(':memory:')
snapshot.backup(restored)
check('actual backup restore returns all three payments', restored.execute('SELECT * FROM payroll ORDER BY payment_id').fetchall(), source)
check('restored control total', restored.execute('SELECT sum(cents) FROM payroll').fetchone()[0], 600)
check('restored SQLite integrity', restored.execute('PRAGMA integrity_check').fetchone()[0], 'ok')
restored.execute("UPDATE payroll SET cents=cents+25 WHERE payment_id='p1'")
restored.commit()
check('business operation after restore', restored.execute("SELECT cents FROM payroll WHERE payment_id='p1'").fetchone()[0], 125)
check('backup remains unchanged by restored write', snapshot.execute("SELECT cents FROM payroll WHERE payment_id='p1'").fetchone()[0], 100)
try:
    restored.execute("INSERT INTO payroll VALUES('p1',999)")
except sqlite3.IntegrityError:
    restored.rollback()
    check('restored primary key still enforced', True, True)
else:
    raise AssertionError('duplicate payment accepted')
check('failed transaction preserves prior committed total', restored.execute('SELECT sum(cents) FROM payroll').fetchone()[0], 625)
for connection in (db, snapshot, restored):
    connection.close()

tasks = [('identity',10,()), ('dns',5,()), ('keys',5,('identity',)),
         ('database',20,('keys','dns')), ('application',15,('database','identity')),
         ('business_validation',10,('application',))]
finish = {}
for name, duration, predecessors in tasks:
    finish[name] = max((finish[p] for p in predecessors), default=0) + duration
check('parallel prerequisite is not added twice', finish['database'], 35)
check('technology available before business validation', finish['application'], 50)
check('chosen end-to-end ready time', finish['business_validation'], 60)
check('serial sum differs from critical path', sum(duration for _, duration, _ in tasks), 65)
check('meets chosen technology RTO of 55', finish['application'] <= 55, True)
check('misses chosen business MTD of 58', finish['business_validation'] <= 58, False)
check('synthetic recovery point gap', 100-82, 18)
check('gap fails chosen 15-minute RPO', 100-82 <= 15, False)
check('known runtime log gap prevents complete coverage claim', {'r1','r2','r3'} <= {'r1','r2'}, False)
check('policy version mismatch requires investigation', 'policy-v2' == 'policy-v1', False)

print(json.dumps(dict(passed=len(checks),checks=checks,sqlite_version=sqlite3.sqlite_version,
                     probability_miss_known_defects=float(miss),weighted_point_estimate=float(weighted),
                     recovery_finish_minutes=finish),indent=2))
```

## Eight practical labs

These eight broader activities are **proposed and unexecuted**. The smaller workbook above is the only executed local exercise; it does not complete the organizational reviews, peer review or end-to-end recovery below.

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

## Answer notes

These original explanations correspond to the 40 prompts above. They are study feedback, not exam items or predictions.

1. The approved audit charter establishes the function’s mandate, reporting position and access. Confirm that engagement scope and actual access are consistent with that authority.
2. Management implements and operates controls and accepts risk through authorized governance. Audit can advise and assess while disclosing impairments; owning the control undermines independent assurance over it.
3. Inherent risk describes exposure before the assessed controls; residual risk remains after them. Define the scenario, impact and assumptions instead of treating a score as an objective fact.
4. Escalate through the approved reporting line when restricted scope or missing evidence prevents a supported conclusion on material risk. State what was excluded and its effect, rather than issuing unsupported assurance.
5. An explanation can describe intent without showing implementation or consistent operation. Corroborate inquiry with suitable records, observation and testing over the relevant population and period.
6. Define objective, complete population, unit, period, selection method, expected and tolerable deviation, confidence and exception handling. A random selection from an incomplete extract still has a scope defect.
7. Attribute sampling concerns whether a characteristic/control occurred; variables approaches estimate amounts. Match the method to the assertion and distinguish sampling from nonsampling error.
8. No single count proves completeness. Reconcile source scope, unique keys, totals, relevant fields and extraction logic. The workbook’s substituted payment preserves counts and totals while failing identifier reconciliation.
9. Preserve objective, criteria, source/version, authority, exact procedure, selection, calculations, results, limitations, reviewer and conclusion. Another authorized auditor must be able to trace the reasoning.
10. Condition states the observed gap; criteria state the required state; cause explains why; effect identifies exposure; recommendation addresses the cause or intended outcome. Do not invent a cause before investigation.
11. Governance sets direction, accountabilities and oversight. Management plans and operates activities within that direction. Test decisions and reporting, not only organization-chart labels.
12. Trace approved enterprise goals to IT investments, risk decisions, service outcomes and accountable benefit owners. Compare intended value with measured delivery and explain deviations.
13. Policy states mandatory direction, a standard specifies required details, a procedure describes execution and a guideline advises. Check ownership, approval, versions, communication and exceptions.
14. Architecture is useful when it informs investment and design decisions, dependencies, standards, transition plans and exceptions. A diagram without ownership or actual use is weak operating evidence.
15. Check the covered legal entity/service, locations, period, criteria, exclusions, subservice arrangements, exceptions and customer responsibilities. A report for another service or period does not cover your use.
16. Examine notification timing, cooperation, evidence access, service/recovery commitments, subcontractors, data return/deletion and transition support. Applicability depends on actual requirements and legal review.
17. More closed tickets or completed training may coexist with recurrence, premature closure or poor behavior. Define denominator, severity, timeliness and business outcomes; inspect adverse incentives.
18. An authorized owner should document reason, affected scope, compensating controls, residual risk, expiry, monitoring and review. A silent or indefinite exception is not governed risk acceptance.
19. A business case needs baseline, alternatives, costs, benefits, assumptions, dependencies, risk and a benefit owner. Retain measurable acceptance criteria so the postimplementation review can compare outcomes.
20. Short iterations still need requirements, risk/control links, reviewed changes, tests, artifact identity and authorized promotion. Match the evidence to the delivery method without waiving accountability.
21. User acceptance testing addresses business fitness against agreed criteria. It complements unit, integration, security, performance and other appropriate testing rather than replacing them.
22. Reconcile source and target scope, identifiers, counts, amounts, field mappings, rejected records and business balances. Investigate differences and demonstrate rollback/recovery, not just a completed migration job.
23. Parallel running can support comparison and fallback when business criticality and reconciliation needs justify its cost and complexity. Assess synchronization and divergence risk; no cutover method is always preferable.
24. Assess whether business benefits, requirements, controls and operational readiness were achieved. Confirm ownership, support and lessons, and track unresolved defects or accepted risks after project closure.
25. Incident management restores an interrupted service; problem management addresses underlying causes and recurrence. The records should connect recurring incidents to investigated causes and controlled changes.
26. Change management authorizes and assesses changes; configuration management maintains trustworthy states and relationships; release management coordinates tested deployment. Trace an actual artifact through them.
27. A job status proves only that the job reported success. Recovery evidence includes accessible media/keys, restoration, integrity, dependencies, business validation and measured requirements under a defined scenario.
28. Business owners and accountable leadership derive tolerances and priorities through the BIA with technology input. IT designs and tests feasible recovery against those requirements.
29. Replication may faithfully propagate encrypted, deleted or corrupted data. Evaluate independent recovery points, protected administration, retention and tested restoration rather than assuming replicas are backups.
30. Include identity, keys, network/DNS, data, application, suppliers, communications, validation and backlog as relevant. Measure a defined end-to-end business outcome and reconcile data loss separately from downtime.
31. Compare entitlements and actual use with roles, approvals, job changes, departures and periodic review. Include privileged/service identities and effective dates; policy text alone is insufficient.
32. A scan identifies suspected weaknesses within its coverage. Validate exposure, exploitability, asset value, compensating controls and business impact before prioritizing risk.
33. A penetration test provides evidence of selected attack paths under defined scope, methods and timing. It cannot establish that all vulnerabilities or future attack paths are absent.
34. Check certificate issuance/identity validation, private-key protection, trust anchors, validity, revocation, renewal and compromise response. A strong cipher cannot repair an untrusted or misissued identity.
35. Identify provider, customer and shared responsibilities for the exact service. Obtain appropriate provider evidence and test the customer’s configuration, access, logging, data and recovery obligations.
36. Verify origin, collection completeness, synchronized time, protection, access, retention and transformations. A stable file hash does not by itself prove truthful contents or trustworthy acquisition.
37. Balance volatile-evidence loss against continuing harm using the authorized incident command and preservation plan. There is no blanket rule to postpone containment; record decisions and evidence handling.
38. Measure relevant reporting and behavior, scenario results, recurrence and response speed with defined denominators. Completion is an activity measure, and a simulation score alone can also mislead.
39. Verify provider/control scope, period, design, operating evidence, dependencies, exceptions and your required complementary controls. Responsibility for assessing applicability remains with the relying organization.
40. State the business risk and audit objective, confirm authority, identify the evidence gap and choose a proportionate procedure. Investigate conflicting evidence before recommending fixes or accepting unsupported reassurance.

## Places to learn

This is not a complete list, and it is not meant to be consumed end to end. Pick the format and chapters that close your measured gaps, practice the decision process, then return to the official outline. Durations are publisher-listed or practical estimates checked September 29, 2026; catalogs, prices and access change.

| Best use | Resource | Access | Estimated time |
|---|---|---|---:|
| Canonical five-domain map and final scope check | [ISACA CISA exam content outline](https://www.isaca.org/credentialing/cisa/cisa-exam-content-outline) | Public | 30–60 min |
| Delivery, policies, and detailed August 2024 outline | [ISACA certification exam candidate guide](https://www.isaca.org/credentialing/-/media/fa494652c5f149289af38cef18328650.ashx) | Public PDF | 60–90 min |
| Official self-paced instruction across 40+ modules with one year of access; public listing only, no lesson review | [ISACA CISA Online Review Course](https://www.isaca.org/training-and-events/online-training/online-review-courses) | Paid | 20–30 hr estimated |
| Explanation-led use of the 1,070-question pool and three timed practices | [ISACA CISA QAE Database](https://www.isaca.org/store2/product/CISA-QAE-C?category=shop-all) | Paid, six months | 25–45 hr estimated |
| Small official item-style sample, not a readiness score | [Free official CISA practice quiz](https://www.isaca.org/credentialing/cisa/cisa-practice-quiz) | Public/form | 15–25 min |
| Eleven-course path and practice exam aligned to the 2024 job practice | [Pluralsight CISA 2024 path](https://www.pluralsight.com/paths/cisar-certified-information-systems-auditorr-2024) | Paid/trial | 20 hr headline; listed courses total 19 hr 32 min |
| Selected explanations and demonstrations; recheck current policy and technology | [O'Reilly CISA video course](https://www.oreilly.com/videos/cisa-certified-information/9781836209119/) | Paid | Previously listed 26 hr 39 min; blocked and not reverified |
| Public Cybrary listing released June 4, 2026; five-domain table of contents read, lessons unreviewed | [LinkedIn Learning CISA Cert Prep](https://www.linkedin.com/learning/isaca-certified-information-systems-auditor-cisa-cert-prep-44731094) | Paid/trial | 7 hr 10 min |
| Public page blocked; prior description unverified; keep official outline/QAE authoritative | [Udemy Masterclass — CISA Exam (Updated 2026)](https://www.udemy.com/course/masterclass-cisa-exam/) | Paid | Previously listed 22 hr 50 min; blocked and not reverified |
| Outcome and governance criteria context | [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) | Public | 1–2 hr selected |
| Control and assessment context, not blueprint memorization | [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) | Public | 2–4 hr selected |
| Exam-versus-designation and application rules | [CISA certification requirements](https://www.isaca.org/credentialing/cisa/get-cisa-certified) | Public | 10–15 min |
| Current CPE, fee, audit and status duties | [CISA maintenance requirements](https://www.isaca.org/credentialing/cisa/maintain-cisa-certification) | Public | 15–20 min |
| Plan the January 2027 maintenance transition | [2027 CPE change](https://www.isaca.org/credentialing/cpe-2027) | Public | 10 min |
| Current standards package and sampling companion; package interior not reviewed | [ITAF fifth edition](https://www.isaca.org/store2/product/WITAF-C?category=shop-all) | Free listing; checkout/MyISACA for download | 3–6 hr selected study estimate |
| Select appropriate evidence objects, methods, depth and breadth | [NIST SP 800-53A revision 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) | Public | 1–2 hr selected sections estimate |
| BIA and recovery-method context; historical technical examples | [NIST SP 800-34 revision 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) | Public | 1–2 hr selected sections estimate |


Use only authorized practice material. Reject products advertised as dumps, recalled questions, “actual exam” files, exact-match simulations, or guaranteed passes.

**Resource review boundary:** Public listings are not course-quality or question-bank validation. The free quiz introduction, first item/explanation and start of the second were visible during a bounded page preview; the quiz was not completed or submitted and its wording is not reproduced. Paid QAE items, ITAF package contents, O’Reilly/Udemy interiors and video playback remain unreviewed.
