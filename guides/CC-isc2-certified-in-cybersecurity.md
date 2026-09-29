---
exam_code: CC
vendor_id: isc2
official_blueprint: https://www.isc2.org/certifications/cc/cc-certification-exam-outline
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# ISC2 Certified in Cybersecurity (CC) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The September 1, 2026 outline, material claims, links, credential lifecycle and exam-integrity boundary were checked September 29, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#cc-coverage-record).

**Current baseline:** The September 1, 2026 CC outline is active. The CAT exam is two hours, 100–125 items, multiple-choice and advanced item types, with 700/1000 passing at Pearson VUE. It is available in English, Chinese, Japanese, German and Spanish, with appointment-window limits stated for Chinese.<br>
**Upcoming change:** No later revision or retirement announcement was present on the checked outline September 29, 2026.<br>
**Credential boundary:** CC requires no work experience. Passing the exam is still followed by the ISC2 certification/member process, Code of Ethics and maintenance requirements. Current member policy lists 45 CPEs over three years and a USD 50 annual maintenance fee for CC-only members; verify policy and fees before registering.<br>
**Freshness warning:** Material mapped to the pre-September outline can miss the new Security Governance domain, revised IAM/network-cloud/operations structure, metrics/testing and embedded AI-security guidance. Match every resource to the 2026 outline.

**CURRENT BLUEPRINT:** Nineteen numbered objectives in five domains, effective September 1, 2026. The actual [eight-page English outline](https://edge.sitecorecloud.io/internationf173-xmc4e73-prodbc0f-9660/media/Project/ISC2/Main/Media/documents/exam-outlines/2026/EXAMS-CC_Exam_Outline-English-Revised-01-2026-Final.pdf) agrees with the detailed web domains; an old domain-name list still appears in the web introduction. The published rounded weights sum to 99.9%; retain them as printed rather than inventing corrected weights. The monitor's only change since the prior snapshot is a testing-center label, not new objectives.

**VERIFY CURRENT:** [ISC2 closed new One Million CC enrollments on May 20, 2026](https://www.isc2.org/landing/1mcc). Previously issued, unexpired codes may be used to schedule **and take** the exam by December 31, 2026; that date does not reactivate expired codes. Existing course access also must remain valid. The page lists the standard exam at USD 199, separate from the USD 50 CC-only annual fee. Verify your actual code, regional checkout and appointment before relying on an offer.

The [CAT policy](https://www.isc2.org/certifications/computerized-adaptive-testing) says finalized answers cannot be revisited and breaks consume exam time. Twenty-five pretest items are included in the minimum exam and cannot be distinguished by candidates. Exam length alone does not identify pass or fail, and 700/1000 is not a raw 70% answer target. The public outline's Chinese window text contains an impossible April 31 date; use actual booking availability rather than copying that calendar.

**PRACTICAL DEPTH:** The original workbook, scenarios and answers below teach control reasoning. They are not recalled exam items. Only the workbook was executed; infrastructure labs and independent human review remain pending.

## How to use this guide

Learn each term as part of a decision chain: asset or business process → threat and vulnerability → likelihood/impact → chosen control → implementation owner → observable evidence → response/recovery. CC tests foundational understanding, but “foundational” should not mean memorizing disconnected acronyms. Practice explaining why a control protects confidentiality, integrity or availability and what remains at risk.

Use only systems, accounts and labs you own or are authorized to test. Blue-team observation, configuration review, tabletop response and synthetic evidence are enough. Do not scan, phish, exploit or access another party's system without written authorization.

> **About related items:** A `Related item:` callout adds prerequisite, operational or adjacent context. It supports understanding but does not assert that ISC2 used that exact wording in the public CC outline.

## Domain map

| Current domain | Weight | Evidence of readiness |
|---|---:|---|
| 1. Security Principles | 24% | Explain CIA/AAA/privacy/non-repudiation, risk and governance hierarchy, control categories, due care/diligence and ethical escalation |
| 2. Security Governance | 17.3% | Connect GRC, BC/DR, awareness and metrics/KRIs to accountable decisions and tested resilience |
| 3. Identity and Access Management Concepts | 20% | Trace identity lifecycle and enforce least privilege, separation of duties and appropriate access-control models |
| 4. Networking and Cloud Security Concepts | 21.3% | Trace traffic through models, protocols and controls; explain segmentation, defense in depth, Zero Trust and shared cloud responsibility |
| 5. Security Operations and Incident Response | 17.3% | Handle data/assets, triage evidence, threat context, incident plans/exercises and authorized security testing |

---

## 1. Security Principles — 24%

### Protect the right property

Confidentiality limits disclosure to authorized subjects; integrity protects correctness, completeness and authorized change; availability keeps approved services/data usable when needed. Controls often affect more than one. Encryption can protect confidentiality and, with authenticated modes or signatures, support integrity/authenticity, but it does not ensure a service remains available. Backups support recovery only when protected, complete and tested.

Authentication establishes a claimed identity, authorization decides permitted access, and accounting records attributable activity. Non-repudiation supplies evidence strong enough that an action cannot credibly be denied, commonly through identity, digital signatures, protected audit trails and process controls. Privacy concerns the appropriate collection, use, sharing, retention and rights around personal data; security is necessary but not sufficient for privacy.

For AI systems, apply the same principles to models, training/retrieval data, prompts, tools, outputs and logs. Poisoned data threatens integrity; exposed prompts or training records threaten confidentiality/privacy; an uncontrolled agent action needs authentication, authorization and accounting. AI does not change the duty to follow policy and law.

### Reason about risk and controls

An asset has value; a threat can cause harm; a vulnerability is a weakness; a control changes likelihood or impact. Risk assessment identifies and analyzes risk against appetite/tolerance. Treatment options include avoid, mitigate, transfer/share and accept. Acceptance belongs to the authorized risk owner—not whoever found the issue or wants to close a ticket. Residual risk remains after controls; inherent risk is considered before them.

Administrative controls include policy, training and process; technical controls include identity, encryption and filtering; physical controls include locks, barriers, guards and environmental protection. Controls may also be preventive, detective, corrective, deterrent, compensating, recovery or directive. Classify by what the question asks: implementation form and security function are separate axes.

Defense in depth layers independent controls so one failure is not decisive. Least privilege grants only needed access for an appropriate time; separation of duties divides incompatible steps. Neither means “deny everyone.” Availability, usability, cost and business need still belong in the decision.

### Connect governance documents and conduct

Laws/regulations are externally imposed obligations; frameworks organize practices; policies state management intent; standards define mandatory requirements; procedures give repeatable steps; guidelines provide recommended discretion. A procedure should implement a policy/standard, and evidence should show it was followed. Know that ISO and CIS are examples in the outline, but study the purpose of a framework/control baseline rather than assuming one applies universally.

Due care is the reasonable protective action expected; due diligence is the continuing investigation, validation and attention that informs it. Follow the ISC2 Code of Ethics and organizational code, law and authorized process. Preserve evidence, avoid conflicts, escalate material risk and do not conceal a mistake. If obligations conflict, document and seek authorized legal/management guidance rather than improvising.

**Related item:** Risk appetite is the broad amount/type of risk an organization is willing to pursue or retain; tolerance defines acceptable variation or limits in a particular context.

---

## 2. Security Governance — 17.3%

### Plan GRC as an accountable system

Governance sets direction, decision rights and accountability. Risk management identifies/analyzes/treats/monitors uncertainty. Compliance demonstrates applicable obligations. A GRC tool can register risks, controls, evidence, exceptions and owners, but it does not create sound governance by itself.

Create a traceable chain from obligation/objective to policy/control, implementation owner, evidence, assessment result, exception, remediation and reporting. Record scope and date. Distinguish a missing control, a control that exists but is ineffective, and a control that works but lacks evidence. Key risk indicators warn about exposure; performance/control metrics show activity or effectiveness. A dashboard should name definition, source, time window, threshold, owner and action.

### Use a framework to organize evidence

[NIST CSF 2.0](https://www.nist.gov/cyberframework) is a source of risk-management outcomes and supporting guidance, not evidence that a control is implemented. Its six Functions are Govern, Identify, Protect, Detect, Respond and Recover. Map an owner, implementation, test, exception and improvement to the relevant outcome. For example, a maintained asset inventory helps identify scope; a recovery exercise supplies evidence that a critical dependency actually returns to service. Do not treat a completed checklist or attractive dashboard as certification of security.

The [August 6 ISC2 refresh article](https://www.isc2.org/Insights/2026/08/inside-the-updated-isc2-cc-exam) explains the new governance domain and the move of incident response into Domain 5. Older domain headings in a course require an explicit mapping, even when many underlying concepts remain useful. The September [AI guidance PDF](https://edge.sitecorecloud.io/internationf173-xmc4e73-prodbc0f-9660/media/Project/ISC2/Main/Media/exam-guidance/ISC2-Exam-Guidance.pdf), CC pages 3–5, adds practical context across all five domains: preserve model/configuration/data dependencies, manage bot identities and validate automated signals. It does not create a sixth domain or separate AI weight.

### Preserve business service through disruption

Business continuity keeps critical processes operating at an acceptable level; disaster recovery restores technology/data after disruption. A business impact analysis identifies critical processes, dependencies, impact over time and recovery priorities. Recovery time objective is the target duration to restore; recovery point objective is the acceptable data-loss window. Maximum tolerable downtime is a business limit, not automatically equal to RTO.

Redundancy reduces single points of failure across power, network, compute, storage, sites, people and suppliers, but replicated corruption or compromised credentials can also spread. Backups need protected copies, retention, restoration testing and accountable ownership. Hot/warm/cold recovery options trade readiness, cost and restoration effort. Plans must include communications, roles, alternate processes, dependencies and return-to-normal.

Exercise plans with walkthroughs/tabletops and technical recovery tests at authorized depth. A paper success does not prove data restores, identities work or dependencies start in order. Capture actual recovery time/point, missing contacts, failed dependencies and corrective actions.

A completed backup job and a structurally readable database can still contain wrong or maliciously changed data. Validate source/version, trusted checksums where applicable, record counts, business totals, required dependencies and permitted users before accepting recovery. Preserve a known recovery point separately from replication that can copy corruption. A hash comparison assumes the expected manifest is trustworthy; hashing alone does not authenticate an operator or establish chain of custody.

Measure recovery time from the defined disruption point to accepted service, including validation and dependencies. Measure potential data-loss age from disruption back to the usable recovery point. In the workbook's fictional timeline, 29 minutes meets a 30-minute RTO, but a 25-minute loss window fails a 15-minute RPO. Passing one objective does not pass both; distinguish exercise times from the actual local copy's runtime.

### Build awareness and measure it

Security awareness is continuous and role-based. Teach reporting, password/MFA behavior, data handling, social engineering/phishing and safe AI use. Executives, developers, administrators and general users face different decisions. Culture improves when reporting is easy and people are not punished for raising a concern in good faith.

Measure outcomes, not only course completion: report rate, time to report, repeat risky behavior, overdue remediation, restore success, privileged-access review exceptions or phishing susceptibility—with privacy and interpretation controls. A single metric can be gamed or misunderstood; use trends and complementary measures.

**Related item:** An incident-response plan handles security events; BC keeps priority business services running; DR restores technology. One event can invoke all three, but their objectives and owners differ.

---

## 3. Identity and Access Management Concepts — 20%

### Manage the whole identity lifecycle

Define roles and entitlement needs before provisioning. Joiner/mover/leaver processes create, change, review and remove access using an authoritative identity source and approvals. Temporary, third-party, service and emergency accounts need owners, expiration and review. Deprovision interactive access, sessions/tokens/keys, group memberships, devices and downstream accounts; disabling one directory account may not revoke every path.

Authentication factors are something you know, have or are; multifactor authentication uses different factor types. Strong authentication still needs secure enrollment, recovery, device/token protection and resistance to social engineering. Federation lets one identity authority support another service; single sign-on improves usability and central control but increases dependency on the identity provider.

Access reviews compare current business need to actual entitlements. Review privileged, toxic combinations, inactive/orphaned and exception access with accountable decisions. Logs show use but do not prove continued need. Bots and AI agents are workload identities and require the same owner, lifecycle, minimum scope, credential rotation and traceability.

### Distinguish strong authentication from a policy slogan

[NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) requires at least 15 characters for a centrally verified single-factor password, while permitting a minimum of eight when the password is only one part of MFA. It rejects mandatory character-mixture rules and calendar-driven password changes, while requiring change after evidence of compromise. It also calls for compromised/common-password blocking, rate limiting and password-manager support. These requirements describe this guidance's verifier context; they are not universal legislation or a rule for a device's local unlock PIN.

Two passwords still supply one factor type. OTP and manually entered out-of-band codes are not phishing-resistant under this reference: an impostor can relay them. Choose an appropriate authentication method with binding to the genuine verifier/session, and review enrollment and recovery as well as routine sign-in. No credentials or authentication settings were changed for this guide.

Removing a group is not proof that a mover lost direct grants. Disabling an account is not proof that every downstream token/session immediately stops working. Inventory independent authorization paths, token audience/lifetime and actual revocation support, then test the relevant application with an authorized identity. The local workbook deliberately models a stale downstream token to explain this distinction; it is not a real identity provider or JWT verifier.

### Apply logical access-control principles and models

Least privilege limits permissions; need-to-know limits information access; separation of duties prevents one identity from controlling incompatible stages. Privileged access should be separately administered, monitored and time-bounded where appropriate. Default deny and explicit grants reduce accidental exposure.

Discretionary access control lets an owner determine access. Mandatory access control uses centrally enforced labels/classifications and clearances. Role-based access control grants through job functions; rule-based control evaluates system rules/conditions; attribute-based access control evaluates subject, resource, action and environment attributes. Real systems combine models. Select by governance, scale, context, sensitivity and auditability.

Authorization must be enforced at every material resource, not only the user interface. Test positive access and negative denial. Protect access logs from unauthorized change, synchronize time, and investigate impossible travel or anomalous behavior as signals rather than automatic proof of compromise.

**Related item:** Zero Trust is not an access-control model in this list. It is an architecture/strategy that continually evaluates explicit trust signals, uses least privilege and assumes breach across identity, device, workload and resource paths.

---

## 4. Networking and Cloud Security Concepts — 21.3%

### Trace the path before naming the control

The OSI and TCP/IP models are troubleshooting abstractions. At a practical level, relate physical/link media and frames/MACs, network-layer IP/routing, transport-layer TCP/UDP/ports and application protocols. IPv4 and IPv6 identify interfaces; routers forward between networks; switches commonly forward within a LAN/VLAN; DNS resolves names; DHCP supplies configuration. A port identifies a service endpoint, not proof that the service is safe.

TCP is connection-oriented and provides ordered reliable delivery; UDP is connectionless with lower protocol overhead and application-dependent reliability. VPNs protect traffic across an untrusted path when correctly authenticated/configured. TLS protects supported application sessions. Never equate “encrypted” with authorized or benign.

Firewalls apply policy to traffic by address, port, protocol, state, application or other context depending on capability. IDS detects/alerts; IPS can block inline. Proxies mediate application connections. Segmentation limits communication and blast radius with zones, VLANs, firewalls or micro-segmentation. Validate rules from intended and forbidden paths.

Wireless and Bluetooth add radio exposure, association/authentication and configuration risks. Prefer current secure protocols, strong identity/key management, protected administration and monitoring. Embedded/ICS/IoT systems may have long lifecycles, safety/availability constraints, weak update mechanisms and vendor dependencies; inventory and isolate them rather than applying risky generic remediation.

### Layer architecture and Zero Trust

Defense in depth combines identity, endpoint, network, application/data and physical controls. A DMZ or screened zone separates internet-facing services from internal networks. Network access control evaluates devices/users before or during access. High availability and redundancy reduce single failures but require independent failure domains and testing.

Zero Trust removes implicit trust based on network location. Verify explicitly using identity, device/workload/resource and context; grant least privilege; assume breach; observe and reevaluate. Micro-segmentation can help enforce it, but buying one product does not create the architecture. [NIST SP 800-207](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) also rejects implicit trust based solely on device ownership. A successful authentication to one resource does not automatically authorize another; record the resource, action, policy and enforcement evidence.

### Understand cloud responsibility

Cloud characteristics include on-demand self-service, broad network access, resource pooling, rapid elasticity and measured service. SaaS supplies a managed application; PaaS supplies a managed application platform/runtime; IaaS supplies virtualized infrastructure. Public, private, hybrid and community describe deployment/ownership patterns. “Multi-cloud” describes use of multiple providers, not a separate service model.

Shared responsibility shifts with service and provider: the provider protects defined underlying facilities/services, while the customer retains responsibilities such as data, identities, configuration, workloads and use. Verify the specific service contract. Cloud elasticity can magnify misconfiguration and cost; centralized identity, logging, configuration guardrails and tested backup/recovery remain required.

**Related item:** Segmentation controls paths; encryption protects content in defined states; IAM controls subjects/actions. Strong architecture combines them instead of asking one to replace the others.

---

## 5. Security Operations and Incident Response — 17.3%

### Protect data and assets through their lifecycle

Classify data by sensitivity and obligation, label it, apply handling requirements and track creation/collection, use, storage, sharing, retention and destruction. Masking reduces exposed detail; sanitization makes media/data infeasible to recover at the required assurance. Symmetric cryptography uses a shared secret and is efficient for bulk data; asymmetric cryptography supports key exchange/signatures and other uses; hashing is one-way integrity support, not encryption. Use approved algorithms/key sizes and manage keys separately.

Maintain asset owner, purpose, classification, location, version/configuration, dependency, support and end-of-life status. Establish secure baselines and controlled changes. Unsupported/end-of-life assets create unpatchable risk; plan replacement, isolation or formally accepted compensating controls. Detect configuration drift and preserve change evidence.

### Distinguish sanitization and cryptographic purposes

Deleting a filename or formatting a volume is not proof of effective sanitization. [NIST SP 800-88 Revision 2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r2.pdf), September 2025, distinguishes clear, purge and destroy according to recovery resistance and possible reuse. The technique must fit the actual medium: degaussing an SSD does not sanitize flash storage. Cryptographic erase requires suitable encryption and key-handling preconditions; merely deleting one copy of a key is not blanket assurance for all copies and plaintext paths.

Verification checks what the operation did, including completion and errors. Validation decides whether those results sufficiently protect the target data and whether to accept, repeat or escalate. Document the asset, data scope, method/tool, result, reviewer and disposition. This guide performs no media wiping or destruction; the workbook's in-memory restore does not demonstrate sanitization.

The [NIST announcement of the first post-quantum standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) distinguishes ML-KEM (FIPS 203, key encapsulation) from ML-DSA and SLH-DSA (FIPS 204/205, signatures). Learn those purposes rather than treating every cryptographic algorithm as interchangeable encryption. An approved migration begins with an inventory of protocols, keys, data lifetime and vendor support, followed by compatibility testing. No cryptographic implementation or migration was executed here, and an old announcement's future roadmap is not current deployment evidence.

### Triage events with evidence and context

Logs record activity; monitoring evaluates it; correlation joins related signals. A SIEM centralizes/searches/correlates security data, while other tools may detect endpoint or network behavior. Normalize time and identity, protect log integrity/access/retention, and avoid collecting unnecessary sensitive content.

An event is observable activity; an alert flags a rule/model condition; an incident is an event or series that threatens policy/business and requires response. Triage validates signal, asset/user/data scope, threat, severity/priority and immediate escalation. Threat actors include insiders, criminals, nation states, activists and others with distinct motivations/capabilities. Threat intelligence should have source, relevance, confidence and freshness. Frameworks organize behavior; they do not prove attribution.

Follow the organization’s incident-response plan with defined preparation, detection/analysis, containment, eradication, recovery and improvement activities. These familiar activity names are not a claim that the older NIST Revision 2 model is still the latest publication. Preserve evidence and chain of custody, record times/actions/decision makers, communicate through authorized channels and do not destroy artifacts to restore faster. Short- and long-term containment trade business continuity against investigation and risk.

[NIST finalized SP 800-61 Revision 3 in April 2025](https://www.nist.gov/news-events/news/2025/04/nist-revises-sp-800-61-incident-response-recommendations-and-considerations), superseding Revision 2. The [current publication](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf) organizes incident-response recommendations through CSF 2.0: Govern/Identify/Protect support preparation and improvement; Detect/Respond/Recover address discovery, management and restoration. Teams can use a lifecycle model that fits their organization. Do not postpone every lesson until final closure or confuse a phase name with evidence that its work was done.

An alert's confidence score is not an incident finding. Validate asset criticality, identity, time, source and observed behavior, then escalate under the plan. In a labeled exercise, precision is confirmed relevant alerts divided by all alerts, while recall is detected relevant events divided by all relevant events. Neither is the same as total alert count. Deduplicate repeated event identities, define the labeling scope and report unknown labels or a zero denominator rather than inventing a perfect score.

### Test readiness safely

Tabletops exercise decisions/communications; simulations and technical recovery exercises test operation. Blue teams defend, red teams emulate an adversary under rules of engagement, and purple teaming emphasizes collaboration/learning. Vulnerability scanning identifies potential weaknesses; static analysis examines code/artifacts without executing; dynamic analysis tests running behavior; threat modeling identifies design risks. Physical assessments can test tailgating, impersonation or phishing only with explicit authorization and safety controls.

Testing requires scope, owner approval, rules, time, targets, allowed techniques, stop conditions, evidence handling, communication and remediation. A finding needs asset/context, evidence, risk and owner; a scan result is not automatically an exploitable incident.

**Related item:** AI can help correlate events and identify anomalies, but analysts must validate context, bias/error and authorization. Automated confidence is not incident proof.

---

## Executed local controls and recovery workbook

Save the following as `cc_workbook.py` and run `python cc_workbook.py`. The exact standard-library code passed **34 checks** with Python 3.13.14. It actually copies and restores SQLite databases in memory; IAM and alert examples are controlled models, and all timeline values are fictional.

The identity fixture exposes incompatible submit/approve duties, a direct grant surviving a group change, token audience/scope/expiry checks and a downstream token remaining usable after central disablement until explicit revocation. It assumes trusted identity/token inputs and does not validate signatures, authenticate anyone, change an OS account or emulate a provider’s actual token contract.

The database example preserves two rows totaling 300 fictional cents, adds later work and corrupts the live copy. A subsequent backup is structurally valid yet fails the trusted business manifest. Restoring the earlier backup recovers its exact two rows; later work is absent, and the corrupted source remains separate. These are real SQLite operations, not evidence of crash-safe, encrypted, offline, immutable or malware-free enterprise recovery. The trusted manifest and source point are fixtures; concurrent writes, operating-system failure, external dependencies and attackers were not tested.

```python
"""Original controlled IAM, SQLite restore and measurement study fixtures."""
import hashlib
import json
import sqlite3
from contextlib import ExitStack, closing
from datetime import datetime, timedelta
from decimal import Decimal
from fractions import Fraction

checks = 0


def check(actual, expected):
    global checks
    if actual != expected:
        raise AssertionError((actual, expected))
    checks += 1


role_permissions = {"reader": {"read"}, "approver": {"approve"}, "auditor": {"audit"}}
account = {"enabled": True, "roles": {"reader"}, "direct": set()}


def effective():
    return account["direct"].union(*(role_permissions[r] for r in account["roles"]))


def central_allows(action):
    return account["enabled"] and action in effective()


def downstream_allows(token, action, audience, minute, revoked):
    # A trusted fixture has already authenticated/validated this token.
    # This is NOT a JWT verifier or a complete real authorization implementation.
    return (token["id"] not in revoked and token["aud"] == audience
            and minute < token["expires"] and action in token["scope"])


check(central_allows("read"), True)
check(central_allows("approve"), False)
account["roles"].add("approver")
account["direct"].add("submit")
check({"submit", "approve"} <= effective(), True)  # Incompatible duties in this policy.
account["roles"] = {"auditor"}  # Moving the group does not remove direct grants.
check(effective(), {"audit", "submit"})
check(effective() - {"audit"}, {"submit"})
account["direct"].clear()
check(effective(), {"audit"})
token = {"id": "synthetic-1", "aud": "audit-app", "scope": {"audit"}, "expires": 30}
revoked = set()
check(downstream_allows(token, "audit", "audit-app", 10, revoked), True)
check(downstream_allows(token, "audit", "other-app", 10, revoked), False)
check(downstream_allows(token, "approve", "audit-app", 10, revoked), False)
check(downstream_allows(token, "audit", "audit-app", 30, revoked), False)
account["enabled"] = False
check(central_allows("audit"), False)
check(downstream_allows(token, "audit", "audit-app", 10, revoked), True)
revoked.add(token["id"])
check(downstream_allows(token, "audit", "audit-app", 10, revoked), False)


def rows(connection):
    return connection.execute("SELECT id,cents FROM ledger ORDER BY id").fetchall()


def digest(connection):
    return hashlib.sha256(json.dumps(rows(connection), separators=(",", ":")).encode()).hexdigest()


with ExitStack() as stack:
    live, good_backup, bad_backup, restored = [
        stack.enter_context(closing(sqlite3.connect(":memory:"))) for _ in range(4)
    ]
    live.execute("CREATE TABLE ledger(id INTEGER PRIMARY KEY, cents INTEGER NOT NULL)")
    live.executemany("INSERT INTO ledger VALUES(?,?)", [(1, 100), (2, 200)])
    live.commit()
    expected_digest = digest(live)  # Trusted manifest, captured before the corruption fixture.
    live.backup(good_backup)
    check(rows(good_backup), [(1, 100), (2, 200)])
    check(digest(good_backup), expected_digest)
    live.execute("INSERT INTO ledger VALUES(3,300)")  # Work after the protected recovery point.
    live.execute("UPDATE ledger SET cents=999 WHERE id=1")  # Controlled corruption, not malware.
    live.commit()
    live.backup(bad_backup)  # A successful backup can copy bad business data.
    check(len(rows(bad_backup)), 3)
    check(digest(bad_backup) == expected_digest, False)
    check(bad_backup.execute("PRAGMA integrity_check").fetchone()[0], "ok")
    good_backup.backup(restored)  # Actually execute SQLite's backup/restore API in memory.
    check(restored.execute("PRAGMA integrity_check").fetchone()[0], "ok")
    check(digest(restored), expected_digest)
    check(rows(restored), [(1, 100), (2, 200)])
    check(restored.execute("SELECT COUNT(*),SUM(cents) FROM ledger").fetchone(), (2, 300))
    check(restored.execute("SELECT COUNT(*) FROM ledger WHERE id=3").fetchone()[0], 0)
    check(live.execute("SELECT cents FROM ledger WHERE id=1").fetchone()[0], 999)

# Fictional timestamps, separate from the actual in-memory copy's runtime.
recovery_point = datetime.fromisoformat("2026-09-29T09:10:00+00:00")
disruption = datetime.fromisoformat("2026-09-29T09:35:00+00:00")
service_accepted = datetime.fromisoformat("2026-09-29T10:04:00+00:00")
loss_window = disruption - recovery_point
recovery_duration = service_accepted - disruption
check(loss_window, timedelta(minutes=25))
check(recovery_duration, timedelta(minutes=29))
check(loss_window <= timedelta(minutes=15), False)
check(recovery_duration <= timedelta(minutes=30), True)
check(loss_window <= timedelta(minutes=15) and recovery_duration <= timedelta(minutes=30), False)

# Labels and alerts use stable event identities, so a repeated alert is not a new event.
malicious = {"a", "b", "c", "d"}
alerts = set(["a", "c", "x", "y", "z", "a"])
true_positive = len(alerts & malicious)
false_positive = len(alerts - malicious)
false_negative = len(malicious - alerts)
check((true_positive, false_positive, false_negative), (2, 3, 2))
precision = Fraction(true_positive, len(alerts)) if alerts else None
recall = Fraction(true_positive, len(malicious)) if malicious else None
check(precision, Fraction(2, 5))
check(recall, Fraction(1, 2))
check(len(alerts), 5)
check(sum(map(Decimal, ["24", "17.3", "20", "21.3", "17.3"])), Decimal("99.9"))
print(json.dumps({"restored_rows": 2, "restored_cents": 300, "loss_window_minutes": 25,
                  "recovery_minutes": 29, "rto_met": True, "rpo_met": False,
                  "alert_precision": str(precision), "alert_recall": str(recall)}, sort_keys=True))
print(f"{checks} local checks passed")
```

Expected final evidence: two restored rows, 300 cents, fictional recovery time 29 minutes and loss window 25 minutes. RTO passes and RPO fails. Two true alerts, three false alerts and two missed labeled events give precision 2/5 and recall 1/2. These tiny invented samples are arithmetic demonstrations, not measured detector accuracy. All database state disappears when the script exits; no files, credentials, network service or cloud account are used.

## Integrated scenarios

### Scenario 1: A mover retains a payment privilege

An employee moves from payments to audit. The group changes, but a direct submit grant and an existing application token remain. Compare intended with effective permissions, flag incompatible duties, remove or expire each authorized access path and test denial in the downstream application. Keep the decision owner, time and evidence. An identity diagram or successful central disable is insufficient proof that every application enforced the change.

### Scenario 2: A backup restores but misses business recovery needs

A protected snapshot is from 09:10; disruption begins at 09:35; validated service returns at 10:04. With a 30-minute RTO and 15-minute RPO, restoration meets the time target but misses the data-loss target. Compare a corrupted recent copy with the older trusted snapshot, reconcile missing transactions and invoke the approved business continuity process. A tabletop timestamp is not a measured production restore.

### Scenario 3: An AI-assisted security dashboard overstates success

A dashboard counts repeated alerts as separate detections and declares high confidence on an anomalous login. Deduplicate event identity, check labels, distinguish precision from recall and examine the actual user/device/session context. Preserve the original evidence, route the decision to the incident owner and record review outcomes. A normal business trip, classifier drift or log delay can change interpretation; automation does not authorize containment on its own.

## Hands-on evidence labs

These eight labs are proposed work; only the workbook above was executed. Use synthetic data and an explicitly authorized local/test environment, define the evidence and cleanup beforehand, and avoid altering shared infrastructure.

1. **Risk and control register:** Describe five assets and threat/vulnerability paths, assign treatment and residual-risk authority, and separate technical/administrative/physical form from preventive/detective/recovery purpose. Include one failed control with a corrective owner and date.
2. **Governance and measurement:** Map an obligation through policy, standard, procedure, implementation and measured result. Produce an indicator with numerator, denominator, time window, owner and action; explain why training completion alone does not prove reduced risk. Relate evidence to CSF outcomes without claiming compliance certification.
3. **Recovery and continuity:** Use an authorized harmless dataset with a known snapshot, post-snapshot transactions and an intentionally altered copy. Restore separately, verify manifest/count/business totals and required dependencies, and measure actual accepted recovery time and usable point against targets. Retain the test evidence and clean up only your test copies.
4. **Identity lifecycle:** Inventory role, group, direct and downstream token access for synthetic joiner/mover/leaver cases. Demonstrate intended allowed/denied actions and a separation-of-duties conflict; record what revocation actually invalidates and when. Do not infer provider behavior from this guide's token fixture.
5. **Network and device path:** Draw DNS, DHCP, transport, TLS, VPN, firewall, VLAN and IoT paths in an authorized simulator or tabletop. Name the resource/action policy and two allowed/forbidden paths. Explain why encryption, trusted network location and company ownership do not grant application authority.
6. **Cloud and asset responsibility:** For one authorized SaaS/PaaS/IaaS example, identify the provider contract and owner for data, identity, patching, configuration, logs and recovery. Add one unsupported asset and an approved replacement/isolation plan. If disposal is proposed, specify medium-appropriate sanitization verification and validation; do not wipe a device as a paper exercise.
7. **Incident triage:** Analyze synthetic duplicate, delayed and ambiguous logs; retain original timestamps/source identity, correlate by event and calculate labeled precision/recall. Record escalation, containment authority and communications as a tabletop. Use the current NIST response guidance and document improvements throughout the exercise.
8. **AI and evidence review:** Inventory an assistant's data/model/configuration/tool dependencies, bot identity and permitted actions. Include drift, high-confidence wrong output and a restricted-data request; compare human-reviewed evidence with an automated score. Assemble versions, access tests, recovery decisions and a cleanup/rollback record.

## Readiness checks

These original answered study prompts are not exam questions. Explain each answer in a concrete scenario.

1. **Which CC outline is current here?** The September 1, 2026 outline with 19 numbered objectives in five domains.
2. **Why do the displayed weights total 99.9%?** The official values are rounded; retain the published values rather than redistributing the difference.
3. **Did the snapshot change add new scope?** No. Only the web testing-center label changed; the detailed objectives and weights did not.
4. **Is the old introductory domain list canonical over the detailed table?** No. The current detailed domains and linked September PDF agree; use those for mapping.
5. **Does CC require cybersecurity work experience?** No. The outline recommends basic IT knowledge but does not require work experience or a degree.
6. **Can a new participant still claim the One Million free enrollment?** No. New enrollments closed May 20, 2026; existing unexpired entitlements have separate conditions.
7. **Does December 31 reactivate an expired exam code?** No. The code must remain valid and both scheduling and taking the exam must meet the deadline.
8. **Is the exam fee the annual member fee?** No. The checked page lists a USD 199 exam separately from the USD 50 annual fee for CC-only members.
9. **Does 700/1000 mean a known raw 70% pass threshold?** No. Do not translate a scaled score into a raw answer percentage.
10. **Can a finalized CAT answer be revisited?** No. Finalized responses cannot be reviewed or changed; breaks also consume the examination time.
11. **Does a 100-item stopping point prove success?** No. CAT can stop at minimum length with either outcome; candidates cannot identify the pretest items.
12. **How do CIA and AAA differ?** CIA identifies confidentiality/integrity/availability properties; AAA identifies authentication, authorization and accounting functions.
13. **Does encryption guarantee availability?** No. Keys, dependencies, capacity and recovery can still fail; match the control to the property.
14. **Is privacy only preventing breaches?** No. Appropriate collection, purpose, use, retention and rights also matter.
15. **Who accepts residual risk?** The authorized risk owner under the organization’s governance process, not automatically the person finding the issue.
16. **Can one control have two classifications?** Yes. Technical/administrative/physical describes form, while preventive/detective/recovery describes function.
17. **How do due care and due diligence relate?** Reasonable protective action is informed by continuing investigation, assessment and review.
18. **What makes a governance metric actionable?** A defined scope, source, denominator, period, threshold, owner and decision; activity totals alone are insufficient.
19. **What are the six CSF 2.0 Functions?** Govern, Identify, Protect, Detect, Respond and Recover; mapping evidence to them is not proof of implemented security.
20. **How do BC and DR differ?** BC maintains priority business processes; DR restores technology/data, coordinated with incident response when necessary.
21. **Can replication copy corruption?** Yes. A fresh replicated copy can preserve bad data; retain and validate suitable recovery points.
22. **What does structural database integrity prove?** That the checked database structure is consistent under that check, not that its business values are correct.
23. **What does the workbook recover?** The earlier two-row, 300-cent snapshot; later transactions are absent and must be reconciled separately.
24. **Can RTO pass while RPO fails?** Yes. The fictional 29-minute recovery meets 30 minutes, while 25 minutes of potential loss exceeds 15 minutes.
25. **Is a hash manifest self-authenticating?** No. The expected manifest must be trusted; an attacker able to change both data and manifest can defeat a simple comparison.
26. **Does removing a group remove every permission?** No. Direct grants, other groups and downstream paths can remain.
27. **Does disabling one account revoke every token immediately?** Not necessarily. Check the application’s token/session lifetime and revocation enforcement.
28. **Why are two passwords not MFA?** Both are knowledge factors; MFA requires distinct factor types.
29. **What password length does the cited NIST verifier guidance use?** At least 15 characters for a single-factor password; it permits a minimum of 8 when used only as one part of MFA.
30. **Does that guidance require calendar password changes?** No. It rejects periodic changes and composition rules, while requiring changes after evidence of compromise and other verifier controls.
31. **Is a relayed OTP phishing-resistant?** No. Manual code entry does not bind the authentication to the genuine verifier/session under the cited guidance.
32. **What distinguishes least privilege from separation of duties?** Least privilege limits needed rights; separation of duties divides incompatible actions, such as submitting and approving the same payment.
33. **Does being on a company network create trust?** No. Evaluate resource access explicitly using relevant identity, device and policy evidence.
34. **Does authentication to one resource authorize another?** No. Each requested resource/action needs its own applicable authorization.
35. **Does a VPN make traffic benign?** No. It can protect a path but does not establish the safety or permission of the application activity.
36. **What customer cloud duties remain?** Data, identities and permitted use remain relevant; exact configuration, workload and recovery boundaries depend on the service contract.
37. **Can a high-availability pair replace backup testing?** No. It can share corruption, credentials or failure dependencies; recovery evidence is separate.
38. **How do clear, purge and destroy differ?** They differ in recovery resistance and media reuse; select a supported technique for the medium and data sensitivity.
39. **Can degaussing sanitize an SSD?** No. Flash storage does not become sanitized through magnetic degaussing.
40. **What separates sanitization verification and validation?** Verification checks operation outcomes; validation decides whether the outcome sufficiently protects the target data.
41. **Are ML-KEM and ML-DSA interchangeable?** No. ML-KEM establishes key material through encapsulation; ML-DSA is a signature algorithm.
42. **Which NIST incident-response revision is current in this review?** SP 800-61 Revision 3, finalized April 2025, supersedes Revision 2 and uses CSF 2.0 to organize recommendations.
43. **Must learning wait for incident closure?** No. Record and incorporate improvements while handling preparation, detection, response and recovery.
44. **Does an alert establish an incident?** No. Validate evidence, asset/user scope and consequences, then follow the authorized escalation process.
45. **What are precision and recall in the workbook?** Two true alerts out of five gives 2/5 precision; two detected out of four malicious labeled events gives 1/2 recall.
46. **Why deduplicate alerts?** Repeated records of one event should not inflate counts of independently detected events; preserve the originals as evidence.
47. **Does AI guidance create a new weighted CC domain?** No. It supplies context across the existing five domains, including bot identities, dependencies, drift and validated triage.
48. **What remains unproven by this guide?** Real identity/network/cloud/incident/forensic/sanitization behavior, production recovery, paid course quality and independent human review.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Choose a route after mapping the September 2026 objectives, then close gaps with current primary guidance and authorized exercises. Public sources were checked September 29, 2026. Study times below are our estimates unless stated otherwise; public metadata does not establish paid lesson quality or complete exam coverage.

| Resource | Access | Estimated time |
|---|---|---|
| [Current CC outline](https://www.isc2.org/certifications/cc/cc-certification-exam-outline) and [actual eight-page PDF](https://edge.sitecorecloud.io/internationf173-xmc4e73-prodbc0f-9660/media/Project/ISC2/Main/Media/documents/exam-outlines/2026/EXAMS-CC_Exam_Outline-English-Revised-01-2026-Final.pdf) — map all 19 numbered objectives, not the stale web introduction | Public | 2–4h mapping/review |
| [ISC2 self-study resources](https://www.isc2.org/certifications/cc/cc-self-study-resources) — official outline, flash cards, Study Hub and course links | Public listing; linked account/paid access varies | 1–2h selection; learning time varies |
| [Official adaptive course](https://www.isc2.org/training/online-self-paced/cc-online-self-paced) — current five-domain public outline; English course language is distinct from exam languages | Paid account; 90/180-day access starts at purchase; no lessons/assessments accessed | Adaptive duration varies; the earlier approximately 14h estimate was not reverified. Our proposed extra review/lab time: 15–25h |
| [Program closure and existing codes](https://www.isc2.org/landing/1mcc), [April 22 announcement](https://www.isc2.org/insights/2026/04/one-million-certified-cyber-conclusion) and [CAT policy](https://www.isc2.org/certifications/computerized-adaptive-testing) — verify eligibility, deadlines and delivery separately | Public; new free-program enrollments closed | 30–60m policy review |
| [Member policies](https://www.isc2.org/policies-procedures/member-policies) and [Code of Ethics](https://www.isc2.org/ethics) — CC requires 45 Group A CPEs over three years; 15 annually is suggested, not a separate annual minimum in that table | Public; CC-only AMF USD 50 annually, subject to policy | 45–90m plus ethical scenarios |
| [2026 refresh article](https://www.isc2.org/Insights/2026/08/inside-the-updated-isc2-cc-exam) and [AI guidance PDF](https://edge.sitecorecloud.io/internationf173-xmc4e73-prodbc0f-9660/media/Project/ISC2/Main/Media/exam-guidance/ISC2-Exam-Guidance.pdf) — read the CC section on printed pages 3–5 | Public; 29-page PDF, only introduction/CC section reviewed for this guide | 1–2h gap mapping |
| [NIST authentication](https://pages.nist.gov/800-63-4/sp800-63b.html), [Zero Trust](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf), [sanitization](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r2.pdf) and [incident response](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf) — selected current primary sections, practical depth beyond simple definitions | Public; not complete exam-prep courses or universal law | 6–10h selective reading plus proposed exercises |
| [O'Reilly/Sybex CC Study Guide, 2nd Edition](https://www.oreilly.com/library/view/cc-certified-in/9781394454907/) — returned HTTP 403; earlier August 2026 / 6h17m metadata and current alignment are unverified | Paid; no book/paid chapters reviewed | Current provider duration unverified |
| [O'Reilly CC 2026 video](https://www.oreilly.com/videos/cert-prep-isc2/00001ISC2CC2026/) — returned HTTP 403; earlier 4h56m duration/current scope unverified | Paid; no video or questions reviewed | Current provider duration unverified |
| [Mike Chapple Udemy course](https://www.udemy.com/course/isc2-certified-in-cybersecurity-cc-complete-course/) — returned HTTP 403; earlier August 2026 / 4h55m metadata unverified | Paid; no lessons reviewed | Current provider duration unverified |
| [Thor Pedersen Udemy course](https://www.udemy.com/course/certifiedincybersecurity/) — returned HTTP 403; earlier June 2026 revision/alignment unverified | Paid; no lessons reviewed | Current provider duration unverified |

The official adaptive course distinguishes its **Validation of Completion** from the CC credential. Its public completion rules use 75% on course assessments plus the other listed requirements; that is not an exam pass rule. Generic experience-requirement wording on the course page does not override the exam outline's explicit no-experience prerequisite. No purchase, enrollment, free voucher, examination item or paid assessment was accessed during this review.

Avoid recalled questions and guaranteed-pass promises. Use original explanations and evidence, reconcile exact current resource coverage and obtain independent review before relying on this unofficial guide.
