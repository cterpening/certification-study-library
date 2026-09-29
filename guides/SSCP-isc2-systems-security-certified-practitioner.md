---
exam_code: SSCP
vendor_id: isc2
official_blueprint: https://www.isc2.org/certifications/sscp/sscp-certification-exam-outline
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# ISC2 Systems Security Certified Practitioner (SSCP) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The October 1, 2025 outline, claims, links, credential contract and exam-integrity boundary were checked September 29, 2026. This review maps all 36 numbered objectives and executes 11 local TLS cases; independent human review and infrastructure labs remain pending. See the [coverage record](../docs/SOURCE-VALIDATION.md#sscp-coverage-record).

**Current baseline:** The October 1, 2025 SSCP outline is active. The CAT exam is two hours with 100–125 multiple-choice/advanced items, 700/1000 passing, and English, Japanese and Spanish delivery at Pearson testing centers. The public outline now shortens the testing-center label; the dated PDF retains “Pearson VUE.” This is not an objective change.<br>
**Upcoming change:** No later revision or retirement announcement was present on the checked outline September 29, 2026.<br>
**Exam versus certification:** ISC2 requires one year of full-time experience in at least one current SSCP domain; an applicable post-secondary degree can satisfy up to one year, and part-time work/internships may count under current rules. A passer without qualifying experience can become an Associate of ISC2 and has two years to earn it. Verify endorsement/application details.<br>
**Maintenance — VERIFY CURRENT:** SSCP requires 60 CPEs over three years: at least 45 Group A, with the remaining 15 Group A or B. The suggested annual total is 20, distinct from the required cycle total. The member AMF is USD 135; Associates have an annual 15 Group A requirement and USD 50 AMF. Check the [member policies](https://www.isc2.org/policies-procedures/member-policies) for the applicable category and cycle.

**CURRENT BLUEPRINT:** Use the [canonical web outline](https://www.isc2.org/certifications/sscp/sscp-certification-exam-outline) for mapping. The [October 2025 PDF](https://edge.sitecorecloud.io/internationf173-xmc4e73-prodbc0f-9660/media/Project/ISC2/Main/Media/documents/exam-outlines/MAR-EXAMS-SSCP-Exam_Outline-English---10012025---FINAL.pdf) confirms the seven weights but has presentation differences: its 7.3 heading says EDR above mobile-device bullets, whereas the web heading explicitly says mobile-device management. Study both endpoint detection and mobile operations; do not drop mobile scope. Web objective 6.7 is numbered without the hyphen used by other headings and still counts.

**VERIFY CURRENT:** [Experience rules](https://www.isc2.org/certifications/sscp/sscp-experience-requirements) describe qualifying work, degrees and internships; a course certificate does not establish personal eligibility. Under the [CAT policy](https://www.isc2.org/certifications/computerized-adaptive-testing), you cannot return to an answered item, breaks consume exam time, and pretest items are not identified. Neither a stopping point nor a course percentage establishes the exam result; 700/1000 is a scaled passing score.

## How to use this guide

SSCP is an operator credential. For each control, practice the complete loop: approved requirement → baseline/configuration → safe change → positive and negative validation → centralized evidence → alert/triage → repair/recovery → documented review. Use disposable local/cloud labs and synthetic data. Never scan, exploit, intercept or modify systems without explicit authorization and rules of engagement.

> **About related items:** A `Related item:` callout adds prerequisite, architectural or operational context. It supports the topic but does not assert that ISC2 used the wording in the public outline.

## Domain map

| Domain | Weight | Operator evidence |
|---|---:|---|
| 1. Security Concepts and Practices | 16% | Policy-to-control record, owned asset/configuration baseline, approved change, awareness/physical coordination and ethical evidence |
| 2. Access Controls | 15% | Identity lifecycle, authentication/federation/trust, entitlement decision, access review, denial and attributable logs |
| 3. Risk Identification, Monitoring and Analysis | 15% | Scoped assessment, contextual vulnerability/risk record, platform telemetry, correlation, threshold, escalation and remediation validation |
| 4. Incident Response and Recovery | 14% | Evidence-preserving response, forensic support, communications, clean recovery and BCP/DR measurement |
| 5. Cryptography | 9% | Approved algorithm/protocol/key lifecycle, certificate validation and failure/rotation/revocation evidence |
| 6. Network and Communications Security | 16% | Packet/control path, segmented policy, device/service configuration, monitoring and safe troubleshooting |
| 7. Systems and Application Security | 15% | Hardened endpoint/mobile/cloud/virtual baseline, malware/activity response, patch/change and recovery evidence |

---

## 1. Security Concepts and Practices — 16%

Apply the ISC2 and organizational codes of ethics when handling access, evidence, disclosure, competence and public trust. A technically possible action is not necessarily authorized or ethical. Stop when scope is unclear, preserve evidence, report conflicts and escalate material risk through approved channels.

Confidentiality, integrity and availability connect to accountability, authenticity, non-repudiation, privacy, least privilege and separation of duties. Map a threat/vulnerability to risk before selecting administrative, technical and physical controls. Classify controls by function—preventive, detective, corrective, deterrent, recovery, compensating or directive—and show what evidence demonstrates operation.

Document control owner, purpose, scope, dependency, configuration, test, exception and review date. Functional evidence is more than “enabled”: validate desired activity and denied/misuse paths, telemetry and failure behavior. Asset management covers procurement/onboarding, ownership/classification, inventory/configuration, use/change, maintenance and secure retirement/disposal for hardware, software and data. Include cloud resources, identities, certificates, containers and AI models/services.

Change management requires request, risk/impact, dependencies, approval, tested implementation, validation, communication, rollback and record update. Emergency change shortens the path but does not erase authorization or retrospective review. Configuration management establishes known baselines and detects drift.

Awareness is role- and threat-specific: phishing/social engineering, password/MFA, data/AI handling, reporting and exercises. Measure behavior and report time, not only attendance. Coordinate physical access, badges/visitors, device/media restrictions, environmental monitoring and safety with facilities; do not defeat a physical control to make IT administration easier.

**Related item:** Policies state management intent; standards define mandatory requirements; procedures explain execution; guidelines advise. Control evidence should trace back through this hierarchy.

---

### From control statement to operating evidence

**PRACTICAL DEPTH:** For a certificate renewal, record the service and owner, approved trust anchors, required DNS names/usage, current serial/expiry, key custodian, rollback conditions and monitor. Test the replacement on a disposable service before changing the active binding. Retain rejection evidence for the old revoked certificate as well as success for the new one. An emergency change still needs authority, a record and subsequent review.

For retirement, classify the medium and intended reuse before selecting clear, purge or destroy. NIST distinguishes checking that the sanitization operation completed from deciding that its result adequately addresses the data risk. Cryptographic erase depends on the scope and protection of keys, key copies and earlier plaintext; deleting a filename or disabling one account does not establish it. The [September 2025 sanitization revision](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r2.pdf) informs this explanation; this guide does not perform media sanitization.

## 2. Access Controls — 15%

Identification names an entity; authentication verifies it; authorization applies permissions; accounting records activity. Use MFA with independent factor types and protect enrollment, recovery, tokens and sessions. Compare passwords, hardware/software tokens, certificates, biometrics, one-time codes and passwordless methods by threat, assurance, usability and lifecycle—not novelty.

Federation establishes cross-domain identity trust; SSO reuses an authenticated session across services. Protocols such as SAML, OAuth and OpenID Connect serve different authentication/authorization delegation purposes. Validate issuer/audience, signing/encryption, redirect/replay/session behavior and claim-to-role mapping. A trusted identity provider compromise or bad claim mapping can expand blast radius.

Manage joiner/mover/leaver plus contractors, service/workload, privileged, shared and emergency accounts. Establish owner, source, approval, role/attribute, expiration, credential rotation and review. Deprovision active sessions, tokens/keys, groups, devices and downstream/federated accounts. Use privileged-access controls and just-in-time/time-bounded elevation when supported.

Apply DAC, MAC, RBAC, rule- and attribute-based models appropriately. Least privilege, need-to-know, separation of duties, default deny and periodic recertification limit excess access. Detect orphaned/dormant accounts and toxic combinations. Validate from both permitted and prohibited users; protect access logs and time sources.

**Related item:** Zero Trust continually evaluates identity, device/workload, resource and context and assumes breach. Federation, network location or a successful login alone should not create permanent implicit trust.

---

### Authentication does not finish the access decision

For a fictional payroll operator moving to support, remove inherited payroll groups, direct grants, temporary elevation and downstream entitlements; invalidate relevant sessions or credentials through the supported lifecycle. Test that payroll reads are denied and support work still succeeds. Record the evaluated subject, action, resource, policy version and result without retaining tokens. One successful login cannot prove authorization or complete deprovisioning.

**PRACTICAL DEPTH:** NIST's current centrally verified password guidance distinguishes at least 15 characters for a single-factor password from at least eight when the password is used only as part of MFA. It rejects mandatory composition rules and routine calendar changes absent evidence of compromise, while requiring compromised-password checks and rate limiting. Local activation PINs have a different scope. Manually relayed OTPs are not phishing resistant merely because they add a second factor. These are scoped [SP 800-63B-4 verifier requirements](https://pages.nist.gov/800-63-4/sp800-63b.html), not a universal rule for every local secret.

[NIST Zero Trust principles](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) do not grant implicit trust from location or device ownership. An authenticated AI agent still needs a constrained resource/action scope and an accountable owner. MAC-address recognition alone is weak device evidence because an address can be imitated.

## 3. Risk Identification, Monitoring and Analysis — 15%

Maintain asset/business context, threat, vulnerability, likelihood, impact, existing control, inherent/residual risk, treatment, owner and due date. Quantitative approaches estimate loss/frequency; qualitative approaches use defined ratings. Neither removes uncertainty. Risk appetite/tolerance comes from authorized leadership; operators surface evidence and implement treatment.

Identify applicable jurisdiction, privacy, contractual, licensing, retention, notification and third-party requirements with legal/compliance input. Data location, cloud provider and user/customer geography can change obligations. Preserve minimum necessary evidence and approved chain of custody.

Security assessments include architecture/configuration review, control testing, vulnerability scanning, code/dependency analysis, penetration tests and audits at authorized scope. A scanner finding needs asset/version/reachability/exposure/control context and validation; CVSS is input, not business priority. Remediate, mitigate, accept, transfer or avoid under ownership, then rescan/retest and close with evidence. Do not test production exploitability merely to raise confidence.

Operate telemetry from endpoint, identity, network, DNS, cloud, application, database and physical systems. Normalize time/identity/asset context; protect collection, transport, access, retention and integrity. SIEM aggregates/searches/correlates; EDR observes/responds at endpoints; IDS/IPS and network analytics observe/control paths; DLP identifies/controls sensitive movement. Health monitoring must distinguish “sensor quiet” from “environment safe.”

Analyze baseline/deviation, rule/signature, behavior, threat-intelligence enrichment and multi-source correlation. Tune false positives without suppressing true attack paths. Define severity/priority, threshold, owner, runbook and escalation; retain query/event IDs. AI-assisted detection can rank or correlate but requires quality/drift/bias monitoring and human validation.

**Related item:** A risk register is forward-looking governance; vulnerability management handles weaknesses; detection engineering creates observable signals; incident response acts when evidence crosses a response threshold.

---

### Correlation and risk decisions need denominators

In an original example, five distinct alerts contain two true positives and three false positives; two additional malicious cases produced no alert. Precision is 2/5 and recall is 2/4. Duplicate events must not inflate these counts. The numbers describe this labeled example, not a production detector; a quiet collector could hide the missed cases. Verify ingestion delay, dropped-event counters, synchronized time and a permitted test signal before concluding the rule works.

Risk treatment should name an authorized owner, rationale, compensating controls, review date and expiration. The dated PDF includes “ignore” among examples; that is not an instruction to silently leave risk unmanaged. Do not infer that high CVSS always outranks a lower-scored exposed asset with greater business impact. A model's changed output distribution is a reason to investigate; drift alone is not proof of hostile compromise.

## 4. Incident Response and Recovery — 14%

Prepare policies, roles, severity, contacts, authority, tooling, logging, evidence storage, communications and playbooks. Detection/analysis validates what occurred, affected identities/assets/data, time and business impact. Containment limits harm with reversible short-term actions and durable long-term measures. Eradication removes cause/persistence; recovery restores clean service and heightened monitoring; lessons learned fixes control and plan gaps.

Record who did what, when, where and why. Preserve original evidence, hashes where appropriate, acquisition method, secure storage and every transfer. Volatile evidence may disappear quickly; follow authorized forensic procedure and order of volatility. Do not power off, image, interrogate or disclose a system outside authority. Separate facts, hypotheses and conclusions.

Support forensic acquisition/analysis across host, memory, network, mobile, cloud and logs while maintaining legal/HR/privacy coordination. Time synchronization and contextual identity/asset records are essential. Communicate by need-to-know through approved out-of-band channels if normal channels may be compromised.

BC keeps critical processes operating; DR restores technology/data. Use BIA, maximum tolerable downtime, RTO and RPO to prioritize. Test alternate process/site, dependency order, identity/DNS/network, immutable/offline backups and restoration. Validate integrity and security before returning service; monitor for recurrence. Exercises range from checklist/walkthrough/tabletop to simulation and technical failover/restoration.

**Related item:** Containment can destroy availability or evidence. Choose the least harmful action that satisfies authority and risk, document the tradeoff and preserve a path to recovery.

---

### Current response guidance and recovery acceptance

The [April 2025 NIST announcement](https://www.nist.gov/news-events/news/2025/04/nist-revises-sp-800-61-incident-response-recommendations-and-considerations) identifies SP 800-61 Revision 3 as the replacement for Revision 2. Its [executive summary](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf) relates preparation and improvement to Govern, Identify and Protect, with response work in Detect, Respond and Recover. The familiar activities in the SSCP outline remain useful; do not label an old four-phase diagram as the only current NIST model.

An original restore scenario has an outage at 10:00, the latest usable data at 09:35, and validated service at 10:29. Against RTO 30 minutes and RPO 15 minutes, the 29-minute restoration meets RTO but the 25-minute data gap misses RPO. A readable backup and completed copy do not prove business completeness, absence of persistence or restored identity/DNS/key dependencies. Preserve custody records alongside hashes: a hash comparison cannot explain who obtained the original evidence or every transfer.

## 5. Cryptography — 9%

Select cryptography for confidentiality, integrity, authenticity, non-repudiation and data sensitivity/obligation. Symmetric encryption is efficient for bulk data but requires shared-key protection. Asymmetric cryptography enables key exchange/signatures and other cases but costs more. Hashes support integrity/password constructions and are not encryption; salts defeat precomputed password hashes; HMAC combines secret and hash for integrity/authentication.

Use approved algorithms, modes and key lengths; do not design custom crypto. Account for entropy/random generation and future quantum risk through inventory and crypto-agility, not unsupported “quantum-safe” claims. Encrypt data at rest, in transit and, where needed, in use with clear trust boundaries. TLS, IPsec/VPN, SSH, secure mail/file and Wi-Fi protocols have different layers and purposes.

PKI connects certificate subjects, public keys, issuers/CAs, registration/validation, chains, trust stores, validity, name/usage constraints and revocation/status. Validate the entire chain, hostname/identity, time and intended usage. Manage keys through generation, storage, distribution, rotation, backup/recovery where allowed, revocation, expiration and destruction. Protect CA/HSM/admin roles and log sensitive operations.

**Related item:** Encryption without authentication can permit tampering; signatures without protected private keys do not establish trustworthy origin; a valid certificate does not make application content safe.

---

### Separate the certificate checks

| Check | Failure to explain | Evidence to retain |
|---|---|---|
| Trust and chain constraints | A self-created CA is not automatically trusted | Explicit trust store, issuer/path and constraint result |
| Name and intended use | A trusted certificate can identify the wrong host or be client-only | Requested identity, SAN, EKU and rejection |
| Time | A certificate may be expired or not yet active | Validation clock and validity interval |
| Revocation | A loaded CRL can be ignored if checking is disabled | Enforced policy, issuer, current CRL and tested revoked serial |
| Rotation | Issuing a new certificate does not invalidate the old one | New binding success plus separately enforced old-certificate rejection |

[Python's SSL documentation](https://docs.python.org/3.13/library/ssl.html) distinguishes certificate requirements, hostname checking and explicit CRL flags. The example below uses actual TLS validation with a private disposable trust anchor. It checks a directly issued leaf; it does not implement OCSP, automatically retrieve CRLs or test an intermediate-chain revocation policy.

HMAC uses a shared secret: either holder may produce the tag, so it cannot by itself provide public proof that only one holder signed. A digital signature likewise does not prove that a model's signed statement is true; trustworthy key custody and provenance are separate from semantic correctness. [NIST's first three finalized post-quantum standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) distinguish ML-KEM key encapsulation from ML-DSA and SLH-DSA signatures. Inventory dependencies and use approved implementations; this guide does not implement post-quantum migration.

## 6. Network and Communications Security — 16%

Trace user/workload → name resolution → route → transport → proxy/firewall/load balancer → service and return path. Relate OSI/TCP-IP layers, IPv4/IPv6, subnet/VLAN, switching/routing, TCP/UDP, ports, DNS/DHCP/NTP and application protocols. Capture read-only state and authorized packet/log evidence before changing configuration.

Recognize DDoS, on-path interception, spoofing, DNS poisoning, scanning, route/ARP manipulation, wireless attacks and protocol abuse by prerequisite, observable effect and defensive layer. Do not memorize attack names without detection/containment. Apply segmentation/DMZ/micro-segmentation, NAC, firewalls, proxies, IDS/IPS, VPN, DNS/email/web controls and secure management planes under least privilege and change control.

Harden routers, switches, firewalls and appliances: supported software, secure admin protocols, centralized AAA, role separation, configuration backup, NTP, logs/telemetry, unused-service/port shutdown, routing/control protection and reviewed rules. A rule needs business owner, source/destination/service/action, time/expiry and validation. Diagnose by layer and roll back if impact exceeds plan.

Secure wireless with current authentication/encryption, protected management, separate guest/IoT paths, RF/rogue monitoring and controlled provisioning. Treat Bluetooth/NFC/cellular/satellite and IoT/OT by range, pairing/identity, update, safety/availability and monitoring constraints.

**Related item:** Network segmentation limits paths and blast radius; identity limits subjects/actions; encryption protects content. None replaces endpoint/application security or monitoring.

---

### A complete packet path includes management and return traffic

**PRACTICAL DEPTH:** For a guest-to-application rule, record source zone/identity, destination service and port, direction, action, owner and expiry. Validate the permitted request and a prohibited administrative connection; inspect return routing and stateful policy before broadening access. Passive IDS sees traffic only where it is delivered; inline IPS can affect availability when it fails. A WAF's application inspection is not a substitute for network segmentation or endpoint authorization.

Compare NAC admission, RADIUS authentication/accounting, TACACS+ device administration and 802.1X port-based access in the context of the deployed design. Inventory IoT firmware, owner, update support and EOL; isolate an unpatchable device under an approved exception rather than leaving it on an unrestricted user network. Wireless guest isolation must include the routed path, not just a separate SSID. Apply maintenance and safety constraints before any OT change.

## 7. Systems and Application Security — 15%

Analyze malicious code/activity—virus, worm, Trojan, ransomware, rootkit, backdoor, bot, script/macro/fileless behavior—by execution vector, persistence, privilege, command/control, impact and observable artifacts. Use layered prevention, application control, EDR/anti-malware, patching, least privilege, segmentation, backups and user reporting. Quarantine/contain under an incident plan; do not delete evidence first.

Build endpoint baselines for firmware/boot, OS support/patch, accounts/services, host firewall, storage encryption, application control, anti-malware/EDR, logging, backup, device/media controls and secure configuration. Manage vulnerability/change cycles and exceptions. Servers, desktops, kiosks and specialized/legacy systems need different availability and application constraints.

Mobile device management/unified endpoint management handles enrollment, inventory, policy, encryption, lock, application/work profile, update, compliance, remote action and retirement. Compare corporate-owned, BYOD and other ownership models by privacy, support and control. Protect loss/theft, insecure apps/networks, rooting/jailbreak and backup/cloud synchronization.

For cloud, map SaaS/PaaS/IaaS shared responsibility; secure tenant hierarchy, IAM/federation, network, data/key/secrets, compute/container/serverless configuration, logging/posture, image/dependency supply chain, backup and incident evidence. Do not assume provider certification secures customer configuration.

Virtualization separates guests through a hypervisor but adds management plane, image/snapshot, virtual network/storage, sprawl and escape risks. Containers share host kernel and need trusted minimal images, registry/provenance, runtime identity, secrets, network policy, resource limits and scanning. Test resilience and restore of configurations/data, not just instance restart.

Application security includes secure requirements/design/threat modeling, reviewed code/dependencies, SAST/DAST and controlled testing, input validation, parameterized queries, output encoding, session/authz, secrets, logging and release/rollback. Treat AI models/prompts/tools as application assets with data leakage, poisoning, injection and excessive-agency risks.

**Related item:** A golden image accelerates recovery only if its provenance, patches, secrets, configuration and deployment automation remain governed and tested.

---

### AI context belongs within the seven existing domains

The [September 2026 ISC2 AI guidance](https://edge.sitecorecloud.io/internationf173-xmc4e73-prodbc0f-9660/media/Project/ISC2/Main/Media/exam-guidance/ISC2-Exam-Guidance.pdf), SSCP pages 6–8, maps AI to existing operations: approved model changes, scoped service identities, monitored endpoints and risk reporting, evidence-preserving triage, protected keys/data, segmented traffic and maintained application dependencies. It does not publish an eighth domain or new weight.

For an AI-assisted incident workflow, version the model and detection rule, keep a human escalation path, and constrain automated containment to approved actions. Backup models, configuration, required data and recovery dependencies together. Protect supply-chain inputs and API identities. A signed output or alert score is evidence to assess, not automatic proof of factual accuracy or malicious activity.

## Integrated scenarios

### Scenario 1: Joiner-to-leaver operations

A fictional support administrator retains a direct payroll grant after a group change. **Reasoning:** removing the old group is insufficient; enumerate effective grants and sessions, authorize the correction, test both payroll denial and support access, and preserve attributable results. A dashboard showing “disabled” does not establish that every independent token or service credential stopped working.

### Scenario 2: Endpoint ransomware incident

A synthetic endpoint alert accompanies unusual file writes, but the collector also has a 20-minute gap. **Reasoning:** preserve endpoint/identity/network evidence, confirm collector health, assess scope, and contain under the response plan. A clean alert dashboard cannot establish that the host is clean. Verify the restored service, data checkpoint and recurrence monitoring against separate RTO/RPO targets.

### Scenario 3: Hybrid service certificate rotation

A new server certificate works, but an older compromised certificate is still trusted. **Reasoning:** renewal and revocation are separate operations. Check the active binding and name/usage, publish current status through the supported mechanism, configure enforcement and test the old serial's rejection. A CRL sitting in a directory proves neither loading nor enforcement; a stale CRL should not silently become current evidence.

## Executed local TLS workbook

**PRACTICAL DEPTH — execution boundary:** This original Python example creates synthetic EC keys, certificates and CRLs, then performs real client/server TLS handshakes and encrypted request/response exchange through memory buffers. No socket is opened and no system trust store is modified. Only a newly created directory under the current working directory holds temporary certificates and an encrypted disposable server key; it is checked and removed on completion. This is a learning fixture, not a CA or server deployment recipe.

It was executed with Python 3.13.14, cryptography 50.0.1 and the Python SSL module's OpenSSL 3.0.21. Use an approved disposable Python environment with the dependency available; the review used an existing environment and installed nothing. Save the block as `sscp_tls.py` in a writable practice directory and run `python sscp_tls.py`. The numeric verification codes document that tested OpenSSL environment and may need review on a different implementation.

| Case | Observed result |
|---|---|
| Trusted issuer, correct hostname, current time and server usage | Handshake and two-way application payload succeed |
| Wrong hostname / untrusted issuer / expired / not-yet-valid / client-only usage | Certificate verification rejects each condition |
| Revocation list loaded, checking disabled | Revoked leaf still succeeds |
| Revoked leaf, checking enabled, current CRL | Rejected |
| Checking enabled, missing CRL / stale CRL | Rejected in each case |
| New leaf, same CA, current CRL revoking only old serial | Succeeds |

The source patterns are documented in the [X.509 tutorial](https://cryptography.io/en/50.0.1/x509/tutorial/), [certificate and CRL reference](https://cryptography.io/en/50.0.1/x509/reference/), and [EC key documentation](https://cryptography.io/en/50.0.1/hazmat/primitives/asymmetric/ec/). Contexts are explicit to avoid loading system trust or enabling environment-driven TLS key logging.

```python
"""Disposable PKI fixtures and real TLS handshakes over memory buffers."""
import json
import os
import ssl
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
import cryptography
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.x509.oid import ExtendedKeyUsageOID, NameOID

now = datetime.now(timezone.utc)
pem = serialization.Encoding.PEM
root_key = ec.generate_private_key(ec.SECP256R1())
root_name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "Disposable SSCP CA")])

def usage(ca=False):
    return x509.KeyUsage(True, False, False, False, False, ca, ca, False, False)

root = (x509.CertificateBuilder().subject_name(root_name).issuer_name(root_name)
        .public_key(root_key.public_key()).serial_number(x509.random_serial_number())
        .not_valid_before(now - timedelta(days=10)).not_valid_after(now + timedelta(days=10))
        .add_extension(x509.BasicConstraints(ca=True, path_length=0), critical=True)
        .add_extension(usage(ca=True), critical=True)
        .add_extension(x509.SubjectKeyIdentifier.from_public_key(root_key.public_key()), False)
        .sign(root_key, hashes.SHA256()))

def issue(start=-1, end=1, purpose=ExtendedKeyUsageOID.SERVER_AUTH):
    key = ec.generate_private_key(ec.SECP256R1())
    cert = (x509.CertificateBuilder().subject_name(x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, "localhost")]))
            .issuer_name(root_name).public_key(key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(now + timedelta(days=start))
            .not_valid_after(now + timedelta(days=end))
            .add_extension(x509.BasicConstraints(ca=False, path_length=None), True)
            .add_extension(usage(), True)
            .add_extension(x509.SubjectAlternativeName([x509.DNSName("localhost")]), False)
            .add_extension(x509.ExtendedKeyUsage([purpose]), False)
            .add_extension(x509.SubjectKeyIdentifier.from_public_key(key.public_key()), False)
            .add_extension(x509.AuthorityKeyIdentifier.from_issuer_public_key(root_key.public_key()), False)
            .sign(root_key, hashes.SHA256()))
    return key, cert

valid = issue()
rotated = issue()
expired = issue(start=-3, end=-2)
future = issue(start=2, end=3)
client_only = issue(purpose=ExtendedKeyUsageOID.CLIENT_AUTH)

def make_crl(stale=False):
    revoked = (x509.RevokedCertificateBuilder().serial_number(valid[1].serial_number)
               .revocation_date(now - timedelta(minutes=1)).build())
    return (x509.CertificateRevocationListBuilder().issuer_name(root_name)
            .last_update(now - timedelta(days=2 if stale else 1))
            .next_update(now + timedelta(days=-1 if stale else 1))
            .add_extension(x509.AuthorityKeyIdentifier.from_issuer_public_key(root_key.public_key()), False)
            .add_revoked_certificate(revoked).sign(root_key, hashes.SHA256()))

def exchange(client_context, server_context, hostname):
    ci, co, si, so = (ssl.MemoryBIO() for _ in range(4))
    client = client_context.wrap_bio(ci, co, server_hostname=hostname)
    server = server_context.wrap_bio(si, so, server_side=True)

    def pump():
        for outgoing, incoming in ((co, si), (so, ci)):
            if outgoing.pending:
                incoming.write(outgoing.read())

    done = [False, False]
    for _ in range(30):
        for i, peer in enumerate((client, server)):
            if not done[i]:
                try:
                    peer.do_handshake()
                    done[i] = True
                except ssl.SSLWantReadError:
                    pass
            pump()
        if all(done):
            break
    else:
        raise RuntimeError("TLS handshake did not converge")
    client.write(b"synthetic request")
    pump()
    assert server.read(1024) == b"synthetic request"
    server.write(b"synthetic response")
    pump()
    assert client.read(1024) == b"synthetic response"
    return client.version(), client.getpeercert(binary_form=True)

results = []
workspace = Path.cwd().resolve()
temporary = tempfile.TemporaryDirectory(prefix="sscp-tls-", dir=workspace)
folder = Path(temporary.name).resolve()
assert folder.parent == workspace and folder.name.startswith("sscp-tls-")
try:
    password = os.urandom(32).hex().encode("ascii")
    bundles = {}
    for name, crl in (("root", None), ("current", make_crl()), ("stale", make_crl(True))):
        bundles[name] = folder / (name + ".pem")
        bundles[name].write_bytes(root.public_bytes(pem) + (crl.public_bytes(pem) if crl else b""))

    def probe(name, pair, expected=0, hostname="localhost", trust=True, crl=False, bundle="root"):
        key, cert = pair
        cert_file, key_file = folder / "server.pem", folder / "server-key.pem"
        cert_file.write_bytes(cert.public_bytes(pem))
        key_file.write_bytes(key.private_bytes(pem, serialization.PrivateFormat.PKCS8,
                                             serialization.BestAvailableEncryption(password)))
        server = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        server.minimum_version = ssl.TLSVersion.TLSv1_2
        server.load_cert_chain(cert_file, key_file, password=lambda: password)
        # Explicit context avoids system trust and environment-triggered key logging.
        client = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        client.minimum_version = ssl.TLSVersion.TLSv1_2
        client.verify_flags |= ssl.VERIFY_X509_STRICT
        assert client.verify_mode == ssl.CERT_REQUIRED and client.check_hostname
        if trust:
            client.load_verify_locations(cafile=bundles[bundle])
        if crl:
            client.verify_flags |= ssl.VERIFY_CRL_CHECK_LEAF
        try:
            version, peer = exchange(client, server, hostname)
        except ssl.SSLCertVerificationError as error:
            assert expected != 0 and error.verify_code == expected, (name, error.verify_code, expected)
            results.append({"case": name, "verify_code": error.verify_code})
        else:
            assert expected == 0, (name, "unexpected acceptance")
            assert peer == cert.public_bytes(serialization.Encoding.DER)
            assert version in ("TLSv1.2", "TLSv1.3")
            results.append({"case": name, "verify_code": 0, "protocol": version})

    probe("trusted name, time and server usage", valid)
    probe("wrong hostname", valid, 62, hostname="wrong.invalid")
    probe("untrusted issuer", valid, 20, trust=False)
    probe("expired leaf", expired, 10)
    probe("not-yet-valid leaf", future, 9)
    probe("client-only usage", client_only, 26)
    probe("loaded CRL without enforcement", valid, bundle="current")
    probe("revoked leaf with enforcement", valid, 23, crl=True, bundle="current")
    probe("enforcement without CRL", rotated, 3, crl=True)
    probe("rotated leaf with current CRL", rotated, crl=True, bundle="current")
    probe("rotated leaf with stale CRL", rotated, 12, crl=True, bundle="stale")
finally:
    # Only this newly created, verified child directory is removed.
    assert folder.resolve().parent == workspace and folder.name.startswith("sscp-tls-")
    temporary.cleanup()

assert not folder.exists()
print(json.dumps({"tls_cases": results, "temporary_files_removed": True,
                  "openssl": ssl.OPENSSL_VERSION, "cryptography": cryptography.__version__}))
print("11 TLS cases passed; temporary files removed")
```

Expected final line: `11 TLS cases passed; temporary files removed`. The three accepted cases also validate the peer certificate bytes and application payloads. These checks do not prove network reachability, browser behavior, mutual TLS, online status retrieval, CA governance, hardware-backed key storage, application authorization, session invalidation or production readiness. Deleting temporary files is cleanup, not certified media sanitization.

## Hands-on evidence labs

The following eight infrastructure activities remain **proposed**, separate from the executed in-memory TLS workbook. Use owned disposable systems, synthetic data, written scope and cleanup records.

1. **Control and asset baseline:** Inventory one disposable host, data classification and owner. Link three controls to a policy, capture the initial baseline, make an approved change and deliberately detect a harmless drift. Pass when allowed/denied behavior and rollback evidence match the recorded requirement; remove the disposable assets afterward.
2. **Identity and trust:** Create two synthetic roles with permitted and forbidden actions. Exercise join, move and leave, including a direct grant and an active session. Pass when effective access matches approval and the old entitlement fails after the supported revocation operation; delete test identities and credentials.
3. **Risk and vulnerability:** Assess only a listed local target under agreed rules. Record finding, evidence, asset impact, uncertainty, owner and treatment. Apply a reversible fix and retest the same condition; do not equate a scanner's disappearance with complete remediation without explaining the evidence.
4. **Monitoring:** Ingest synthetic host and identity records with synchronized timestamps. Test one allowed signal, one malicious fixture, duplicate delivery and a missing collector heartbeat. Record precision/recall on labeled cases and ingestion health separately. Remove test forwarding and restore the previous configuration.
5. **Incident and forensic support:** Work from provided synthetic evidence copies. Hash acquisition and working copies, record custody, mark facts versus hypotheses and tabletop containment authority. Restore a disposable dataset and calculate both recovery duration and data gap; preserve a sanitized timeline and clean up copies under the retention plan.
6. **PKI and TLS deployment:** Extend the executed workbook to an owned isolated service only if authorized. Test correct and wrong names, expiry, usage, old-serial revocation and new binding. Record actual client policy, CRL/status freshness and failure behavior. Remove temporary trust anchors and keys through documented cleanup; do not install them in shared stores.
7. **Network, endpoint and mobile controls:** Design a guest/IoT/service separation and validate permitted traffic plus blocked administration. Document device support/EOL and a mobile ownership/privacy policy; distinguish virtual-machine isolation from shared-kernel containers. Test a configuration restore and remove temporary rules/resources.
8. **Operator evidence pack:** Link asset, risk, approval, access, scan, alert, incident and restore records by stable identifiers. Have a reviewer trace one denied action and one recovery result to the relevant policy. List exceptions, expiry, unresolved evidence and cleanup rather than reporting a blanket pass.

## Readiness checks

These are original teaching prompts, not recalled or predicted exam items. Cover the answer, reason through an example, then compare the evidence you would produce.

1. **Authority conflicts with a technically available action. What comes first?** Confirm scope, protect evidence and use approved escalation. Technical access alone does not grant authority; apply the ISC2 and organizational ethics obligations.
2. **How do CIA and accountability change a control design?** Identify the asset and harm: restrict sensitive reads, detect unauthorized changes, preserve required service and attribute actions to a controlled identity.
3. **How do control form and function differ?** Administrative, physical and technical describe implementation; preventive, detective, corrective and other functions describe what the control does. One implementation can serve several functions.
4. **What proves a control operates?** A dated configuration tied to a requirement, permitted and denied tests, telemetry, owner, failure behavior and recorded review. A checked enable box is insufficient.
5. **What belongs in an asset lifecycle?** Planning/acquisition, ownership and inventory, assessment, operation/change, maintenance/EOL, retention and approved disposal of hardware, software and data.
6. **What remains necessary during an emergency change?** Authority, impact assessment, a recorded action, validation and recovery options; expedited approval still needs retrospective review.
7. **How can awareness measurement improve?** Measure safe reporting and response behavior on approved simulations, including time and errors; attendance alone does not show behavior changed.
8. **What physical dependencies need coordination?** Visitor/badge controls, device/media restrictions, power/environment, safe access and facility response responsibilities.
9. **How do the four identity operations connect?** Identification claims a subject, authentication verifies it, authorization evaluates the action/resource, and accounting records the result.
10. **Why are SSO and federation different?** SSO reduces repeated sign-ins; federation establishes identity trust across boundaries. Their configurations and trust failures must be evaluated separately.
11. **What should a federated application validate?** The intended protocol, issuer, audience, signatures and freshness plus redirect/session protections and controlled claim-to-permission mapping.
12. **Is removing a group enough to deprovision?** No. Inspect direct and inherited rights, elevation, sessions, tokens/keys and downstream identities, then test denied access.
13. **How do RBAC and ABAC differ from least privilege?** RBAC and ABAC express decisions through roles or attributes. Least privilege is the design objective of restricting effective access to necessary scope and duration.
14. **Who accepts a residual risk?** The authorized risk owner within organizational policy; record rationale, remaining impact, controls, expiration and review. Operators provide evidence and execute treatment.
15. **How do jurisdiction and contracts affect evidence?** They can constrain location, collection, access, retention and disclosure. Work with the responsible legal/privacy functions and preserve only approved evidence.
16. **How do scanning, penetration testing and audit differ?** Scanning identifies candidate weaknesses, penetration testing validates selected attack paths under explicit scope, and audit assesses evidence against criteria. None automatically covers all risk.
17. **How is a vulnerability closed defensibly?** Validate applicability and exposure, prioritize with business context, implement approved treatment and retest the relevant condition with dated evidence.
18. **How do SIEM, EDR, IDS/IPS and DLP differ?** They emphasize cross-source analysis, endpoint activity/response, network detection or prevention, and sensitive-data movement respectively; verify their actual coverage and dependencies.
19. **How can a quiet sensor mislead?** A broken collector also produces no alerts. Check heartbeat, delivery delay, dropped events, time and a permitted test signal.
20. **What makes an alert actionable?** Identifiable subject/asset, useful evidence, severity and confidence context, owner, response authority, runbook and escalation path; tune against labeled false and missed cases.
21. **What connects response phases?** Preparation establishes authority and capability; analysis determines scope; containment limits harm; eradication removes cause; recovery validates service; lessons drive improvement.
22. **Does a matching hash prove custody?** It supports unchanged bytes relative to the compared value. Origin, acquisition method, authorized handlers and transfers need their own records.
23. **How do BIA, BC and DR relate?** BIA identifies critical impact and priorities; business continuity maintains essential processes; disaster recovery restores technology and data under those priorities.
24. **What makes a restore acceptable?** Authorized service and data validation, required dependency recovery, absence of known persistence, measured RTO/RPO, monitoring and documented acceptance.
25. **When do hash, salt and HMAC fit?** Hashing supports integrity constructions, salts make password hashes distinct against precomputation, and HMAC authenticates with a shared secret; none is reversible encryption.
26. **What makes a protocol choice defensible?** A current approved algorithm and implementation, appropriate keys/parameters, correct peer validation, protected key lifecycle and evidence of positive and negative behavior.
27. **Does trusting a CA finish certificate validation?** No. Check the path and constraints, intended name and use, validity and the configured revocation/status policy.
28. **What belongs in key lifecycle management?** Authorized generation, custody/storage, distribution/use, rotation, backup or escrow where permitted, revocation, recovery and appropriate destruction with records.
29. **How should a failed service connection be traced?** Check identity/name resolution, address/route, transport, middleboxes, TLS and application result plus return path. Change the layer supported by evidence.
30. **How should an attack name be studied?** Explain its prerequisites, observable artifacts, affected layer and suitable prevention/detection/response; memorizing a label does not establish coverage.
31. **What makes a firewall rule governed?** Business owner, precise source/destination/service/direction/action, approval, expiration, logging, allowed/denied tests and rollback.
32. **What protects an appliance management plane?** Restricted administration paths, supported firmware, strong administrator identity, least privilege, secure protocols, configuration backup and attributable logs.
33. **Why treat IoT EOL explicitly?** An unsupported device may not receive fixes. Inventory its owner and exposure, isolate it, monitor, plan replacement and document time-limited exceptions.
34. **What distinguishes malware behavior from an alert name?** Actual execution, persistence, privilege, communication and impact artifacts. Validate context before containment and preserve evidence.
35. **How do endpoint and mobile baselines differ?** Both need supported software, controlled identity, encryption and telemetry; mobile ownership introduces enrollment, work/personal separation, privacy and authorized remote-action boundaries.
36. **Does SaaS remove customer security work?** No. The provider operates more of the stack, but customer identity, configuration, data handling and contractual responsibilities still need explicit allocation.
37. **Why distinguish VMs from containers?** A VM has a guest operating-system boundary through a hypervisor; containers generally share a host kernel. Both require maintained management, images, identities, storage and recovery.
38. **What should gate an application release?** Approved requirements, threat/dependency review, appropriate testing, authorization/session/input protections, secrets handling, evidence, rollback and monitored deployment.
39. **How can all seven domains meet in one change?** Certificate rotation combines policy/change, operator access, risk/monitoring, recovery, PKI, network service paths and host/application configuration.
40. **How should a course be reconciled with scope?** Map each current numbered objective to teaching and practical evidence; resolve gaps with current primary sources instead of trusting a title or revision date.
41. **Why did a loaded CRL still allow the old certificate?** The client did not enable CRL checking. Loading data and enforcing a validation policy are separate steps.
42. **Why did a rotated certificate fail with a stale CRL?** The leaf was new, but the required status evidence was no longer current. Renew status evidence through the approved process rather than disabling checks.
43. **Does renewal automatically revoke an earlier certificate?** No. Issuance/binding and revocation enforcement are separate. Test both new-certificate success and old-certificate rejection.
44. **What does the executed workbook establish?** Eleven actual TLS outcomes in memory with synthetic certificates and CRLs, accepted-case payload exchange and temporary cleanup; it does not test a deployed network or application authorization.
45. **Can a signed AI output prove its factual accuracy?** No. A signature can support origin and integrity under its key/trust assumptions. Evidence for the statement and control of the signing key remain separate.
46. **What do ML-KEM, ML-DSA and SLH-DSA do?** ML-KEM establishes shared key material through key encapsulation; the other two are signature standards. These roles are not interchangeable.
47. **Is a 70% course assessment result the SSCP passing score?** No. The adaptive course completion requirements are separate from the CAT exam’s scaled 700/1000 passing score and from certification experience requirements.
48. **Does completing this guide establish certification readiness?** No. Use objective mapping, independent review and demonstrated operation/failure/recovery evidence; complete the official experience/application process separately.

## Places to learn

This is not a complete list. Choose a route, map it against the current outline, and use targeted references and practical work for gaps. Catalog observations below were checked September 29, 2026; paid lessons, books and question banks were not accessed. Estimates labeled planning are this guide's suggestions, not provider runtimes or guarantees.

| Resource | Access | Estimated time |
|---|---|---|
| [Current SSCP outline](https://www.isc2.org/certifications/sscp/sscp-certification-exam-outline) — canonical 36-objective map and seven weights | Public | Planning: 3–6h mapping and review |
| [ISC2 self-study resources](https://www.isc2.org/certifications/sscp/sscp-self-study-resources) — official links to outline, adaptive training and study aids | Public hub; some destinations require account/payment | Planning: 1–2h selecting resources; study varies |
| [Official adaptive training](https://www.isc2.org/training/online-self-paced/sscp-online-self-paced) — public seven-domain description; English course; included textbook/questions are catalog claims only | Paid/account; 90/180-day access begins at purchase | No fixed public runtime verified; earlier 35–50h was a planning estimate |
| [Pluralsight SSCP path](https://www.pluralsight.com/paths/sscpr-systems-security-certified-practitioner-certification) — eight public course cards dated September–October 2024; conflicting September 2024/November 2021 outline labels require current gap mapping | Paid/trial; public catalog only reviewed | Header 14h; eight listed cards total 13h36m; planning: add 25–40h practical work |
| [LinkedIn Learning/Cybrary SSCP Cert Prep](https://www.linkedin.com/learning/isc2-systems-security-certified-practitioner-sscp-cert-prep) — August 26, 2025 public listing, seven domains and nine quizzes; current detailed alignment not established | Paid/trial; public contents only reviewed | Header 6h; 30 listed clips total 6h00m59s; planning: add 20–35h practical work |
| [O'Reilly/Sybex SSCP study guide, 3rd edition](https://www.oreilly.com/library/view/isc-2-sscp-systems/9781119854982/) — current access blocked; earlier 2022/alignment metadata unverified in this review | Paid/trial or book; public request returned HTTP 403 | Earlier 29h16m estimate not reverified; inspect a legitimate preview before planning |
| [Udemy SSCP Masterclass](https://www.udemy.com/course/sscp-training-english-isc2/) — current access blocked; earlier August 2026 revision/alignment unverified | Paid; public request returned HTTP 403 | Earlier 27h15m not reverified |
| [ISC2 member policies](https://www.isc2.org/policies-procedures/member-policies) — distinguish member versus Associate obligations | Public | Planning: 45–90m on applicable requirements |
| [ISC2 Code of Ethics](https://www.isc2.org/ethics) — apply the canons to authority, competence, disclosure and public trust | Public | Planning: 30–60m plus original scenarios |

**VERIFY CURRENT:** Adaptive training requires at least 70% on domain and final assessments plus its acknowledgement/evaluation requirements for a Validation of Completion. That document is not the SSCP credential. Course access, exam entitlements and personal experience are separate; verify the selected offer before purchase. Public catalog metadata cannot establish teaching quality, question legitimacy or complete October 2025 alignment.

Avoid recalled questions, “actual exam” banks and guaranteed passing. Use original practice with explained answers and current primary sources. The [dated deep-review report](../docs/research/2026-09-29-sscp-deep-review.md) records the executed work, source limitations and pending human review.
