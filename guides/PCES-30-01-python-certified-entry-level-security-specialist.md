---
exam_code: PCES-30-01
vendor_id: python-institute
official_blueprint: https://pythoninstitute.org/pces-exam-syllabus
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-30
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-30
---

# PCES-30-01 Certified Entry-Level Security Specialist with Python Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Deep-reviewed September 30, 2026; original local security exercises executed with explicit limits. The [official PCES syllabus](https://pythoninstitute.org/pces-exam-syllabus) is authoritative.

**Current baseline:** PCES-30-01, active; syllabus last updated August 21, 2025<br>
**Upcoming blueprint change:** none announced; the official page's PCES practice-test text still says planned/coming Q3–Q4 2026, so check actual availability rather than assuming the date means release<br>
**Official delivery snapshot:** 45 questions; 60 minutes plus NDA; 75%; select, input-based, scenario and analytical items; TestNow; English<br>
**Credential snapshot:** no formal prerequisite; PCEP-equivalent Python recommended; seven-year validity; USD 69 exam or USD 86 with retake when checked; seven-day wait after a failed attempt<br>

**VERIFY CURRENT:** The complete [credential page and FAQ](https://pythoninstitute.org/pces) still give planned Q3 or coming Q3/Q4 2026 practice availability; reaching September 30 does not prove release. Practice-related bundle prices are future listings. PCAS's announced Q4 path is a different credential, not a replacement PCES blueprint. The complete [PCES testing policy](https://pythoninstitute.org/pces-testing-policies), revised August 22, 2025, specifies seven days after failure; generic footer prose also mentions passing, which does not establish retake eligibility after a pass. Local partner rescheduling and global unredeemed-voucher procedures differ. No account, booking or system test occurred.

## How to use this guide

Practice only in systems you own or have explicit permission to assess. Build defensive scripts around local fixtures and loopback networks, document scope, minimize privileges, preserve logs, and never turn an educational scan into uncontrolled probing.

> **About related items:** A `Related item:` callout supplies adjacent operational context, not extra exam scope.

## Weighted objective map

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| Security essentials | 10 | 22% | Classify assets/threats/risks/impacts and communicate proportionate controls |
| IT systems security | 12 | 27% | Harden systems and explain network, identity, cloud and remote safeguards |
| Python security operations | 13 | 29% | Run authorized checks, monitor/correlate, report, schedule, verify backups and chain tasks |
| Secure Python development | 10 | 22% | Validate/encode, protect secrets/files/errors, use named libraries safely, and verify integrity |

The full canonical English syllabus and minimum-qualified-candidate profile were manually read after direct retrieval and the automated monitor timed out. They contain **45 detailed objectives**, grouped **10/12/13/10**, beneath the 19 topic headings summarized in the retained snapshot. The detailed mapping below is additional review evidence; the historical snapshot was not silently expanded or represented as a successful fresh hash observation. Full PDF reading remains pending.

## 1. Security essentials — 22%

Confidentiality limits disclosure, integrity protects correctness/completeness, and availability keeps authorized access reliable. Authenticity, accountability, and non-repudiation extend the model. Identify asset, threat, vulnerability, likelihood, and impact before calling something “high risk.” A control reduces likelihood or impact; residual risk remains.

Threats include malware, phishing/social engineering, credential attack, injection, exploitation, insider action, misconfiguration, and environmental failure. Use defense in depth: patching, least privilege, MFA, segmentation, backups, monitoring, filtering, and user/process safeguards.

Data loss destroys availability; theft harms confidentiality; unauthorized modification harms integrity. Consequences can be operational, financial, safety, legal, regulatory, contractual, and reputational. Incident communication should be timely, factual, need-to-know, and aligned with an escalation plan. Preserve evidence and distinguish observation from inference.

### Assets, consequences and escalation

| Detailed objective | Review focus |
|---|---|
| 1.1.1 | CIA and accountability |
| 1.2.1 | Threats and risk |
| 1.2.2 | Protective layers |
| 1.3.1 | Loss consequences |
| 1.3.2 | Theft consequences |
| 1.3.3 | Alteration consequences |
| 1.4.1 | Downtime consequences |
| 1.5.1 | Legal responsibilities |
| 1.6.1 | Clear reporting |
| 1.6.2 | Incident coordination |

For an original fictional clinic example, an unavailable appointment list delays care, a disclosed list exposes private associations, and an altered dosage record can create physical harm. A single ransomware incident can affect all three properties. Authenticating a sender does not prove their instruction is authorized; a log provides accountability only if identity, time and integrity are credible. Encryption cannot recover a deleted key, and a backup that shares the compromised credentials may share the same failure.

Classify malware by behavior: a virus attaches to a host artifact, a worm spreads, a trojan disguises a harmful purpose, and ransomware denies or threatens access to data. These categories can overlap. Phishing manipulates decisions; a denial-of-service attack exhausts availability. State the vulnerable condition and plausible impact before assigning severity, and record uncertainty instead of inventing a numeric probability.

| Study example | Scope and reporting distinction |
|---|---|
| [EU data protection obligations](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/obligations_en) | The Commission describes notifying the supervisory authority without undue delay and within 72 hours of awareness where the breach is likely to risk individuals' rights/freedoms; processors notify controllers. High risk can also require notifying individuals, subject to stated exceptions. This is not a universal incident deadline. |
| [HIPAA breach notification](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html) | HHS distinguishes covered entities/business associates and unsecured protected health information. Individual notice is without unreasonable delay and at most 60 days after discovery; notice to the Secretary has different rules for fewer than 500 people. Assess definitions, exceptions and recipients. |
| [California CCPA overview](https://oag.ca.gov/privacy/ccpa) | The Attorney General describes privacy rights and qualifying businesses. Consumer request-response periods are not interchangeable with breach-notification deadlines. Applicability and current notification duties need their own legal review. |

These are scoped study examples, not a decision that any real organization is covered or compliant. Legal, regulatory, contract and trade-secret duties can coexist; fines, civil claims or criminal exposure depend on the applicable rule and facts. An NDA does not replace an incident plan. Preserve the observed timeline and involve the designated privacy/legal owner early rather than waiting for a full root-cause narrative.

An original incident note should separate **observation** (three failed events on a lab host), **inference** (possible credential misuse), **unknowns** (clock accuracy and user activity), **action** (preserve records and triage), and **owner/next update**. Technical responders need timestamps, scope and reproducible evidence; managers need impact, decisions and timing. Assign an incident lead, evidence custodian, operations owner and communications/privacy contacts; rehearse escalation with synthetic exercises. The workbook's three-event threshold produces a lead, not a confirmed attacker.

## 2. IT systems security — 27%

Security is continuous because assets, threats, code, dependencies, people, and configurations change. Technical controls include updates, firewalls, encryption, endpoint protection, monitoring, and access control. Organizational controls include policy, training, separation of duties, supplier management, response plans, and audits.

Hardening inventories the system, removes/disables unnecessary software/services/accounts, applies secure configuration and patches, limits privileges, enables logging, and verifies against a baseline. Record exceptions and recheck drift.

Ports identify service endpoints; protocols define exchanges; services implement functions. Reduce exposure by binding only required interfaces, filtering traffic, encrypting transport, authenticating endpoints, and monitoring. A closed port is not proof the host is secure.

Authentication proves identity; authorization decides permitted actions. Strong unique passwords, secure storage, rate limiting, recovery controls, and MFA reduce credential risk. MFA requires independent factors: knowledge, possession, inherence—not merely two passwords.

Cloud/SaaS responsibility is shared: providers secure defined platform layers while customers still manage identities, data, configuration, devices, and use. Secure remote access with MFA, least privilege, managed devices, encrypted channels, timely updates, logs, and revocation.

### Controls and verification

| Detailed objective | Review focus |
|---|---|
| 2.1.1 | Continuous improvement |
| 2.1.2 | Technical safeguards |
| 2.1.3 | Organizational safeguards |
| 2.1.4 | Development review |
| 2.2.1 | Hardening sequence |
| 2.3.1 | Service exposure |
| 2.3.2 | Network configuration |
| 2.4.1 | Identity and permission |
| 2.4.2 | Password policy |
| 2.4.3 | Authentication factors |
| 2.5.1 | Cloud storage |
| 2.5.2 | Remote access |

A firewall filters according to rules; IDS detects and reports, while IPS can block inline traffic. A VPN protects a transport path but does not make a compromised endpoint trustworthy. Least privilege, approved devices, separation of production/test data, peer review and training address different failure paths. Review changes when requirements are formed, not only after deployment. Pseudonymized logs can remain linkable personal data; the workbook's keyed identifiers are explicitly not anonymous.

A useful hardening record has an owner, asset inventory, desired services, initial settings, proposed change, recovery path and verification result. Order changes so that management access and rollback remain available, then test intended and denied behavior. Revisit the baseline after changes and threat information; one universal calendar interval is not justified. No host settings were changed for this review.

HTTP and HTTPS carry web application traffic, SSH supports secure remote access, and conventional FTP is distinct from SFTP over SSH. A familiar port number does not authenticate a service or prove encryption. Inventory the actual bindings, remove unused exposure and segment systems by required communication. The workbook tests only its own loopback listener; it neither inventories this computer nor tests surrounding hosts.

Objective 2.4.2 names expiry/history/complexity settings. Know what these settings do, while distinguishing them from current deployment guidance. [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/) specifies at least 15 characters for single-factor passwords, permits a minimum of eight when used only within MFA, and recommends supporting at least 64. Its verifier guidance rejects arbitrary composition rules and routine forced changes without compromise evidence; blocklists, rate limits and password-manager support matter. This is NIST's scoped guidance, not a universal legal requirement or permission to change an organization's policy.

Two knowledge secrets remain one factor category. SMS and manually entered OTP can be relayed by phishing; possession of a hardware device alone does not establish phishing resistance. NIST identifies cryptographic binding to the legitimate verifier/session, with WebAuthn as an example. Recovery and enrollment controls also need protection. No credential or MFA setting was changed.

For cloud storage or SaaS, document who controls identity, sharing, configuration, backup/export and revocation under the actual service agreement. Provider responsibility does not remove customer duties. Test remote access with least privilege and managed-device requirements, including offboarding and a lost-device scenario; a successful VPN connection alone is insufficient evidence.

## 3. Python for security operations — 29%

Every assessment needs written authorization, targets, time window, techniques, data rules, and stop/escalation conditions. Use `socket`/`ssl` only against permitted endpoints; set timeouts and bound concurrency. A banner/version hint is evidence to investigate, not proof of vulnerability.

`psutil` can enumerate processes and system data. Establish a baseline and treat deviations as leads, not automatic malicious verdicts. `subprocess.run()` should receive an argument list, avoid `shell=True` with untrusted values, set timeout/check/capture policy, and run with least privilege.

Correlation aligns events by normalized timestamp, source, identity, host, and event meaning. Preserve original records and note clock/time-zone uncertainty. Reports in CSV/JSON/PDF should state scope, method, evidence, severity rationale, limitation, and remediation without exposing secrets unnecessarily.

Scheduled jobs need idempotence, lock/overlap handling, timeout, retry bounds, logging, alert routing, and failure visibility. A backup is not verified until a restore/integrity check demonstrates usability. Chain tasks only when failure/partial-success behavior is explicit.

> **Related item:** Detection engineering separates collection, normalization, rule logic, triage context, and response. This structure makes small scripts less likely to become opaque alert generators.

### Assessment, monitoring and recovery evidence

| Detailed objective | Review focus |
|---|---|
| 3.1.1 | Authorized port checks |
| 3.1.2 | Configuration weaknesses |
| 3.1.3 | Information gathering |
| 3.2.1 | Website certificates |
| 3.2.2 | Process monitoring |
| 3.2.3 | Controlled responses |
| 3.2.4 | OS command boundaries |
| 3.3.1 | Event correlation |
| 3.4.1 | Structured reporting |
| 3.4.2 | Actionable findings |
| 3.5.1 | Scheduling |
| 3.5.2 | Backup recovery |
| 3.5.3 | Task sequencing |

The original `owned_loopback` creates one ephemeral IPv4 listener on `127.0.0.1`, connects to that exact listener, exchanges four bytes and closes every socket. [socket's contracts](https://docs.python.org/3.13/library/socket.html) support bounded blocking calls and context cleanup. This is an executed connection exercise, not a scanner or vulnerability assessment. Written permission must additionally specify real targets, window, methods, collected data and stop conditions. Software banners, WHOIS data and version strings need corroboration; a backported fix can invalidate a version-only conclusion. No WHOIS query, credential trial or external scan occurred.

The [ssl reference](https://docs.python.org/3.13/library/ssl.html) distinguishes certificate-chain verification from hostname matching. The workbook inspects a `PROTOCOL_TLS_CLIENT` context with both requirements and loads default trust anchors, without a handshake. It deliberately avoids default-context environment key-log handling. The separate expiry function uses **synthetic explicit-offset timestamps**, classifying equality as expired and the next seven days inclusively as due soon. It does not extract a certificate, establish trust, check revocation or send an alert. Do not disable verification to make a failing connection appear healthy.

[psutil's public index](https://psutil.readthedocs.io/en/latest/) shows process and resource measurements; the package is absent here. A process name or high CPU sample alone cannot classify malware. Collect minimal authorized attributes, document sampling interval and baseline, and handle inaccessible or disappearing processes without treating missing data as a clean bill of health. Firewall, patch or antivirus state needs a platform-specific supported interface and an authorized response policy. Restarting a service automatically can amplify an incident or destroy evidence; no such response was run.

The fixed child exercise uses the current interpreter in isolated mode, a constant tiny program, one validated data argument, `shell=False`, capture/check policy and a five-second timeout. Shell-like characters round-trip unchanged. [subprocess documentation](https://docs.python.org/3.13/library/subprocess.html) also warns that Windows batch files may invoke a shell despite the requested setting; this example uses the Python executable, not a batch file. An argument list does not neutralize the called program's own option or language parser. Actual echo execution and a separately simulated timeout are distinct evidence.

The original correlation contract accepts at most 1,000 records with exact fields and controlled source/host/outcome values. [datetime parsing and conversion](https://docs.python.org/3.13/library/datetime.html) normalize explicit offsets; missing offsets are rejected. The inclusive fixed window ends at injected `now` and starts five minutes earlier. Replayed identical `(source,id)` events count once; conflicting identities fail. Three failures for one subject/host produce a triage row; successes, older/future events and other hosts do not silently contribute. This is a batch teaching rule, not a streaming detector or a conclusion about a real user.

The three fixture times normalize to 00:00, 00:02 and 00:04 UTC. The report preserves the original records, replaces the subject with a domain-separated HMAC identifier and records count, sources, first/last time and next action. A changed key changes the identifier and disrupts linkage. The public fixture key provides reproducibility, not privacy; a real key needs independent access control and lifecycle management. Clock skew, shared identities and missing logs remain uncertainty.

The JSON observation and [CSV report](https://docs.python.org/3.13/library/csv.html) contain controlled report fields. CSV quoting is not spreadsheet formula protection for arbitrary untrusted cells; this writer accepts only this controlled result schema. No PDF incident report or visualization was generated. Include scope, evidence, method, severity rationale, limits, owner and verifiable remediation in a real report; do not equate a count threshold with legal impact.

The executed chain writes an original 25-byte fixture to a backup, validates it with a separately held teaching manifest/key, restores to a new owned file, compares bytes and preserves the source. Tampering is rejected, including replacement of the unkeyed checksum. This proves one fixture's byte recovery, not application consistency, off-site resilience, restore permissions or RTO/RPO. A failed/exceptional stage stops later callbacks; errors expose only stage and exception type. No cleanup callback deletes source data.

Cron, Task Scheduler and APScheduler remain future integration exercises. Specify identity, working directory, overlap policy, bounded retries, failure recording and alert owner before scheduling. A timer firing does not prove the job completed. This review creates no persistent task, service or notification. The [temporary-directory contract](https://docs.python.org/3.13/library/tempfile.html) is used only for owned disposable fixtures, whose removal is checked.

## 4. Secure development and implementation — 22%

Linters/static analyzers find selected patterns without execution. Triage findings and combine them with tests, review, dependency scanning, and runtime controls. Validate input against type, length, range, format, allow-list, and cross-field rules; normalization occurs before validation where appropriate. Sanitizing data is context-specific and not a universal substitute for validation.

Output encoding must match the destination context: HTML text, attribute, URL, JavaScript, shell, and SQL have different rules. Use parameterized APIs rather than manual escaping.

Use context managers and restrictive permissions for files, avoid predictable unsafe temporary paths, log failures without secrets, and preserve exception cause while returning safe messages. Store secrets outside source/config committed to version control, restrict access, rotate/revoke, and never print them.

The `cryptography` library supplies modern primitives/recipes; keys, nonces, modes, authentication, and lifecycle matter. Encryption without integrity can permit undetected alteration, so prefer authenticated encryption. `paramiko` provides SSH/SFTP capabilities; validate host keys and do not blindly accept unknown hosts.

A cryptographic hash fingerprints bytes for integrity comparison, but an attacker who can replace both file and checksum defeats an unauthenticated checksum. Obtain expected digests through a trusted/authenticated channel; use signatures/MACs when authenticity is required.

### Validation, trust and document boundaries

| Detailed objective | Review focus |
|---|---|
| 4.1.1 | Static checks |
| 4.1.2 | Injection defenses |
| 4.1.3 | Output contexts |
| 4.1.4 | Files and errors |
| 4.1.5 | Secret configuration |
| 4.2.1 | Authenticated encryption |
| 4.2.2 | SSH/SFTP trust |
| 4.2.3 | Document protection |
| 4.3.1 | Hash choices |
| 4.3.2 | Trusted checksums |

The syllabus names Pylint and Flake8. Both are absent; existing [Ruff](https://docs.astral.sh/ruff/linter/) runs selected `E4,E7,E9,F,W,E501` rules at 79 columns. A clean result proves those checks passed, not a vulnerability audit or execution of the named tools. Review dependencies, trust boundaries and runtime behavior separately.

The original SQLite example binds data to a fixed query using `?` placeholders; attack-shaped strings return no rows, while `amber` and `blue` match their own rows. The database lives in memory and closes explicitly. [SQLite binding](https://docs.python.org/3.13/library/sqlite3.html) and [OWASP's SQL guidance](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) support keeping values separate from query structure. Identifiers and sort expressions require controlled choices; parameters do not establish row-level authorization.

The output example encodes one printable bounded string for **HTML text**, an **XML text node**, and a **standalone JSON value**. [html.escape](https://docs.python.org/3.13/library/html.html), [ElementTree serialization](https://docs.python.org/3.13/library/xml.etree.elementtree.html) and [json](https://docs.python.org/3.13/library/json.html) have distinct contracts. The observed JSON still contains a closing-script sequence, so do not paste it into executable HTML script content. [OWASP's context guidance](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) distinguishes HTML, attributes, JavaScript, CSS and URLs. No browser was executed and no general XML parser hardening is claimed; the tests parse only their own serialized fixture.

`read_fixture` permits only two exact filenames, resolves them under a trusted private root, checks a direct regular file and reads at most 1,025 bytes to enforce a 1,024-byte limit. Tests reject traversal, absolute/drive paths and alternate-stream syntax before I/O. The [pathlib reference](https://docs.python.org/3.13/library/pathlib.html) describes resolution of symlinks and parent components. A simulated escaped resolved path tests the guard; no real symlink/junction was created. Resolve-check-open still has a race if an attacker can mutate the directory. Protect directory ownership and use platform-appropriate handle-based controls where that threat applies; this helper is not a filesystem sandbox.

The public deterministic key is **test data**. Environment variables can separate configuration from source but are not automatically a secret vault; child processes, diagnostics and permissions still matter. Do not dump the environment, return raw tracebacks or log arbitrary exception messages. The chain test deliberately raises an exception containing a synthetic secret and verifies that the result omits it. It is not a complete logging, retention or secret-rotation system.

The complete [Fernet reference](https://cryptography.io/en/latest/fernet/) describes an authenticated symmetric recipe: key holders can read and create valid tokens, invalid tokens raise `InvalidToken`, optional TTL governs token age, and creation time is visible. Keep keys separate from ciphertext and plan recovery/rotation. `cryptography` is absent, so encryption/decryption, expiry and rotation are **not executed**. The docs currently identify a development version; no environment version or exam requirement is inferred. A plain SHA-256 digest is neither encryption nor a password-storage scheme.

The complete [Paramiko client reference](https://docs.paramiko.org/en/stable/api/client.html) describes known-host checks, default `RejectPolicy`, separate connection/authentication timeouts, explicit close and SFTP sessions. Before a future disposable-host lab, obtain the expected host key through a trusted route; automatic acceptance or warning-and-accept policies do not establish that trust. Remote command strings have different parsing boundaries from local argument lists. No SSH key, account, agent or host was accessed; `paramiko` is absent.

Objective 4.2.3 names PyPDF2, python-docx and openpyxl. Their PDF encryption/text, document comments/metadata and spreadsheet hidden-content/formula exercises remain pending because those packages are absent. Installed **pypdf 6.16.1** supports one narrow original experiment, not equivalence with all PyPDF2 objectives: removing `/Info` from a blank one-page PDF leaves the XMP creator intact. The complete [metadata documentation](https://pypdf.readthedocs.io/en/stable/user/metadata.html), currently 6.19.0, distinguishes these stores. Neither removal of a metadata field nor a successful parse proves absence of embedded actions, scripts, comments, hidden content, macros or sensitive text.

The [pypdf encryption page](https://pypdf.readthedocs.io/en/stable/user/encryption-decryption.html) warns that omitting the algorithm uses insecure RC4 and that AES needs an extra backend. Neither supported backend is installed here. No PDF encryption or decryption ran. A future exercise must explicitly select a supported AES algorithm, keep a strong synthetic password out of source/logs, verify correct and wrong-password behavior, inspect the actual file structure and transmit through an authenticated channel. No arbitrary document was opened or declared sanitized.

[hashlib](https://docs.python.org/3.13/library/hashlib.html) supports SHA-256 and documents collision weaknesses in older hashes; avoid MD4/MD5 for new security integrity designs. The original [HMAC](https://docs.python.org/3.13/library/hmac.html) exercise authenticates fixture bytes using a separate key and `compare_digest`. Replacing the data and its plain hash does not reproduce the original MAC. It provides no confidentiality, signature-based nonrepudiation or protection if the key is also compromised. A public download checksum still needs a separately authenticated source and version/filename association; none was downloaded or verified here.

The MQC profile calls `psutil`, `cryptography` and `paramiko` standard Python libraries. They are third-party packages; `socket`, `ssl`, `subprocess` and `hashlib` are standard-library modules. Do not assume the named packages exist because Python itself runs.

## Safe labs

1. Create an asset/threat/vulnerability/risk/control table for a local sample application.
2. Harden a disposable local VM/container and document baseline, change, verification, rollback, and residual risk.
3. Enumerate only loopback services with socket timeouts and a strict allow-list.
4. Use `psutil` to compare a local process snapshot to a fixture baseline without labeling deviations malicious.
5. Execute a fixed allow-listed command through `subprocess.run` safely and log result metadata.
6. Correlate synthetic JSON/CSV logs across time zones and preserve originals.
7. Generate a sanitized report with scope, evidence, uncertainty, severity, and action.
8. Schedule a local integrity check with overlap prevention and failure notification.
9. Validate/encode hostile fixture strings for two distinct output contexts.
10. Encrypt/decrypt test data with a documented authenticated recipe and separate key material.
11. Connect via Paramiko only to a disposable host whose key fingerprint you pre-recorded.
12. Verify a download fixture with a digest from a separately trusted manifest; demonstrate why co-located mutable hashes are weak.

The twelve lab plans above remain broader than the completed workbook. Local components cover the fixed child, correlation/reporting, encoding and integrity exercises; the loopback activity is one owned connection, not service enumeration. Hardening, process collection, scheduler/alerts, cryptography, SSH, document sanitization, independent review and full end-to-end readiness remain pending.

## Exact original executable workbook

Save the following three files together in a disposable directory. This recorded environment already had CPython 3.13.14, pypdf 6.16.1 and Ruff 0.16.4; no package was installed. The public tests require pypdf for their one metadata experiment. The review extracted these exact files and checked their hashes before running **30 test methods and 21 observation checks in each normal/optimized mode**, with warnings treated as errors. Both observation JSON results match.

```text
python -B -Werror -m unittest discover -s . -p test_security_workbook.py -v
python -B -Werror -O -m unittest discover -s . -p test_security_workbook.py -v
python -B -Werror observations.py
python -B -Werror -O observations.py
python -m ruff check security_workbook.py test_security_workbook.py observations.py --select E4,E7,E9,F,W,E501 --line-length 79
```

All inputs are synthetic. The only network interaction is with the example's own temporary loopback listener. One short child uses a fixed Python program; filesystem changes stay in an owned temporary directory; SQLite and PDF fixtures stay in memory. A simulated timeout and simulated resolved-path escape are labeled as such. There is no scan, real TLS/SSH validation, service change, scheduled task, notification or readiness approval.

### security_workbook.py

```python
"""Original finite PCES exercises. Synthetic data and owned resources only."""

import csv
import hashlib
import hmac
import html
import io
import json
import os
from pathlib import Path
import socket
import sqlite3
import ssl
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from xml.etree import ElementTree as ET


def text(value, limit=256):
    if type(value) is not str:
        raise TypeError("text required")
    if not 1 <= len(value) <= limit or not value.isprintable():
        raise ValueError("invalid text")
    return value


def key_bytes(key):
    if type(key) is not bytes or len(key) != 32:
        raise ValueError("32-byte key required")
    return key


def utc(value):
    result = datetime.fromisoformat(text(value, 64))
    if result.utcoffset() is None:
        raise ValueError("explicit time offset required")
    return result.astimezone(timezone.utc)


def expiry_status(now, expiry):
    remaining = (utc(expiry) - utc(now)).total_seconds()
    if remaining <= 0:
        return "expired"
    return "due-soon" if remaining <= 7 * 86400 else "outside-window"


def correlate(events, now, key):
    """Fixed five-minute inclusive window; a triage lead, not attribution."""
    key_bytes(key)
    if type(events) is not list or len(events) > 1000:
        raise ValueError("bounded event list required")
    end = utc(now)
    start = end - timedelta(minutes=5)
    seen, buckets = {}, {}
    required = {"id", "source", "subject", "host", "outcome", "time"}
    for event in events:
        if type(event) is not dict or set(event) != required:
            raise ValueError("unexpected event schema")
        for value in event.values():
            text(value)
        if event["source"] not in {"auth", "server", "firewall"}:
            raise ValueError("unknown source")
        if event["host"] not in {"lab-a", "lab-b"}:
            raise ValueError("unknown host")
        if event["outcome"] not in {"failed", "ok"}:
            raise ValueError("unknown outcome")
        moment = utc(event["time"])
        identity = (event["source"], event["id"])
        if identity in seen:
            if seen[identity] != event:
                raise ValueError("conflicting event identity")
            continue
        seen[identity] = event.copy()
        if event["outcome"] != "failed" or not start <= moment <= end:
            continue
        token = hmac.digest(
            key, b"PCES subject\0" + event["subject"].encode(), "sha256"
        ).hex()
        bucket = buckets.setdefault((token, event["host"]), [])
        bucket.append((moment, event["source"]))
    rows = []
    for (token, host), entries in sorted(buckets.items()):
        if len(entries) >= 3:
            rows.append(dict(
                subject_token=token, host=host, failures=len(entries),
                sources=",".join(sorted({source for _, source in entries})),
                first=min(t for t, _ in entries).isoformat(),
                last=max(t for t, _ in entries).isoformat(),
                decision="triage", action="check context and clock offsets",
            ))
    return rows


def csv_report(rows):
    """Only accepts the controlled output of correlate, not arbitrary cells."""
    stream = io.StringIO(newline="")
    fields = [
        "subject_token", "host", "failures", "sources", "first", "last",
        "decision", "action",
    ]
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


def encode_text(value):
    value = text(value)
    node = ET.Element("message")
    node.text = value
    return dict(
        html="<p>" + html.escape(value) + "</p>",
        xml=ET.tostring(node, encoding="unicode"),
        json=json.dumps({"message": value}, ensure_ascii=True),
    )


def lookup_label(value):
    value = text(value)
    connection = sqlite3.connect(":memory:")
    try:
        connection.execute("CREATE TABLE labels (name TEXT PRIMARY KEY)")
        connection.executemany(
            "INSERT INTO labels VALUES (?)", [("amber",), ("blue",)]
        )
        return connection.execute(
            "SELECT name FROM labels WHERE name = ?", (value,)
        ).fetchall()
    finally:
        connection.close()


def read_fixture(root, name):
    """Trusted private root. Resolve/check/open is NOT race-free isolation."""
    if type(name) is not str or name not in {"notes.txt", "report.json"}:
        raise ValueError("unapproved fixture")
    base = Path(root).resolve(strict=True)
    target = (base / name).resolve(strict=True)
    if not base.is_dir() or target.parent != base or not target.is_file():
        raise ValueError("fixture must be a direct regular file")
    with target.open("rb") as stream:
        data = stream.read(1025)
    if len(data) > 1024:
        raise ValueError("fixture too large")
    return data


def seal(data, key):
    key_bytes(key)
    if type(data) is not bytes or len(data) > 1024:
        raise ValueError("bounded bytes required")
    return dict(
        length=len(data), sha256=hashlib.sha256(data).hexdigest(),
        mac=hmac.digest(key, b"PCES backup\0" + data, "sha256").hex(),
    )


def verify_backup(data, manifest, key):
    expected = seal(data, key)
    if type(manifest) is not dict or set(manifest) != set(expected):
        return False
    if type(manifest["length"]) is not int:
        return False
    for name in ["sha256", "mac"]:
        value = manifest[name]
        if type(value) is not str or len(value) != 64:
            return False
        if any(c not in "0123456789abcdef" for c in value):
            return False
    return (
        manifest["length"] == expected["length"]
        and hmac.compare_digest(manifest["sha256"], expected["sha256"])
        and hmac.compare_digest(manifest["mac"], expected["mac"])
    )


def owned_loopback():
    """One connection to this function's own ephemeral listener; no scan."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.bind(("127.0.0.1", 0))
        listener.listen(1)
        listener.settimeout(2)
        address = listener.getsockname()
        with socket.create_connection(address, timeout=2) as client:
            accepted, peer = listener.accept()
            with accepted:
                accepted.settimeout(2)
                accepted.sendall(b"LAB\n")
                received = b""
                while len(received) < 4:
                    part = client.recv(4 - len(received))
                    if not part:
                        raise RuntimeError("unexpected end of stream")
                    received += part
                if peer[0] != "127.0.0.1":
                    raise RuntimeError("unexpected peer")
    return received.decode("ascii")


def tls_policy():
    # No default-context SSLKEYLOGFILE handling, handshake or trust-store edit.
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_default_certs()
    return dict(
        check_hostname=context.check_hostname,
        require_certificate=context.verify_mode == ssl.CERT_REQUIRED,
    )


def child_echo(value):
    value = text(value)
    # Fixed interpreter/program. Value is one data argument, never source.
    program = "import json,sys; print(json.dumps(sys.argv[1:]))"
    flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
    result = subprocess.run(
        [sys.executable, "-I", "-B", "-c", program, value],
        shell=False, timeout=5, check=True, capture_output=True,
        text=True, encoding="utf-8", creationflags=flags,
    )
    return json.loads(result.stdout)


def run_chain(stages):
    """Trusted injected callbacks; stop on exception or non-True result."""
    events = []
    for name, action in stages:
        try:
            result = action()
        except Exception as error:
            events.append(dict(stage=name, status="error",
                               error_type=type(error).__name__))
            break
        if result is not True:
            events.append(dict(stage=name, status="failed"))
            break
        events.append(dict(stage=name, status="passed"))
    return events


def pdf_metadata_probe():
    """One original blank PDF. Info removal alone leaves XMP creator data."""
    from pypdf import PdfReader, PdfWriter
    from pypdf.xmp import XmpInformation

    with io.BytesIO() as raw:
        writer = PdfWriter()
        try:
            writer.add_blank_page(width=72, height=72)
            writer.add_metadata({"/Author": "Synthetic author"})
            xmp = XmpInformation.create()
            xmp.dc_creator = ["Synthetic creator"]
            writer.xmp_metadata = xmp
            writer.metadata = None
            writer.write(raw)
        finally:
            writer.close()
        raw.seek(0)
        reader = PdfReader(raw)
        try:
            return dict(
                info_removed=reader.metadata is None,
                xmp_creator=reader.xmp_metadata.dc_creator,
                pages=len(reader.pages),
            )
        finally:
            reader.close()
```

### test_security_workbook.py

```python
"""Independent fixed expectations for original, synthetic PCES exercises."""

import copy
import csv
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from xml.etree import ElementTree as ET

import security_workbook as lab


KEY = bytes(range(32))  # Public deterministic fixture, never a real secret.
NOW = "2026-09-30T00:05:00+00:00"


def sample_events():
    return [dict(
        id=str(i), source=source, subject="=synthetic-user()", host="lab-a",
        outcome="failed", time=timestamp,
    ) for i, (source, timestamp) in enumerate([
        ("auth", "2026-09-29T20:00:00-04:00"),
        ("server", "2026-09-30T00:02:00Z"),
        ("firewall", "2026-09-30T01:04:00+01:00"),
    ])]


class SecurityTests(unittest.TestCase):
    def test_timestamp_offset_equivalence(self):
        self.assertEqual(lab.utc("2026-09-29T20:00:00-04:00").isoformat(),
                         "2026-09-30T00:00:00+00:00")

    def test_timestamp_rejects_missing_offset_and_bad_data(self):
        for value in ["2026-09-30", "wrong", "2026-09-30T00:00:00", ""]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                lab.utc(value)
        with self.assertRaises(TypeError):
            lab.utc(None)

    def test_expiry_exact_boundaries(self):
        now = "2026-09-30T00:00:00Z"
        for expiry, expected in [
            ("2026-09-29T23:59:59Z", "expired"),
            (now, "expired"),
            ("2026-09-30T00:00:01Z", "due-soon"),
            ("2026-10-07T00:00:00Z", "due-soon"),
            ("2026-10-07T00:00:01Z", "outside-window"),
        ]:
            with self.subTest(expiry=expiry):
                self.assertEqual(lab.expiry_status(now, expiry), expected)

    def test_correlation_preserves_input_and_exact_window(self):
        events = sample_events()
        before = copy.deepcopy(events)
        row, = lab.correlate(events, NOW, KEY)
        self.assertEqual(events, before)
        self.assertEqual(row["failures"], 3)
        self.assertEqual(row["sources"], "auth,firewall,server")
        self.assertEqual(row["first"], "2026-09-30T00:00:00+00:00")
        self.assertEqual(row["last"], "2026-09-30T00:04:00+00:00")
        self.assertEqual(row["decision"], "triage")
        self.assertNotIn("=synthetic-user()", json.dumps(row))

    def test_correlation_threshold_and_duplicate_replay(self):
        events = sample_events()
        self.assertEqual(lab.correlate(events[:2], NOW, KEY), [])
        self.assertEqual(lab.correlate(events + events, NOW, KEY),
                         lab.correlate(events, NOW, KEY))

    def test_correlation_rejects_conflicting_identity(self):
        events = sample_events()
        extra = dict(events[0], subject="different")
        with self.assertRaisesRegex(ValueError, "conflicting"):
            lab.correlate(events + [extra], NOW, KEY)

    def test_correlation_excludes_old_future_success_and_other_host(self):
        for change in [
            {"time": "2026-09-29T23:59:59Z"},
            {"time": "2026-09-30T00:05:01Z"},
            {"outcome": "ok"}, {"host": "lab-b"},
        ]:
            events = sample_events()
            events[0].update(change)
            with self.subTest(change=change):
                self.assertEqual(lab.correlate(events, NOW, KEY), [])
        events[0]["host"] = "lab-a"
        events[0]["time"] = NOW
        self.assertEqual(lab.correlate(events, NOW, KEY)[0]["failures"], 3)

    def test_correlation_rejects_schema_and_unbounded_inputs(self):
        for events in [None, [dict(sample_events()[0], secret="bad")],
                       sample_events() * 334]:
            with self.subTest(events_type=type(events).__name__):
                with self.assertRaises(ValueError):
                    lab.correlate(events, NOW, KEY)
        for field, value in [("source", "other"), ("host", "prod"),
                             ("outcome", "maybe"), ("subject", "a\nb")]:
            events = sample_events()
            events[0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                lab.correlate(events, NOW, KEY)

    def test_correlation_key_changes_linkability(self):
        events = sample_events()
        one = lab.correlate(events, NOW, KEY)[0]["subject_token"]
        two = lab.correlate(events, NOW, b"x" * 32)[0]["subject_token"]
        self.assertNotEqual(one, two)
        self.assertRegex(one, r"^[0-9a-f]{64}$")
        with self.assertRaises(ValueError):
            lab.correlate(events, NOW, b"short")

    def test_csv_report_is_controlled_and_roundtrips(self):
        rows = lab.correlate(sample_events(), NOW, KEY)
        encoded = lab.csv_report(rows)
        self.assertNotIn("=synthetic-user()", encoded)
        row, = list(csv.DictReader(io.StringIO(encoded)))
        self.assertEqual(row["failures"], "3")
        self.assertEqual(row["sources"], "auth,firewall,server")
        self.assertTrue(all(not value.startswith(("=", "+", "-", "@"))
                            for value in row.values()))
        self.assertEqual(len(lab.csv_report([]).splitlines()), 1)

    def test_encoding_has_context_specific_expected_values(self):
        value = '<script title="x">&\'</script>'
        result = lab.encode_text(value)
        self.assertEqual(result["html"],
                         '<p>&lt;script title=&quot;x&quot;&gt;'
                         '&amp;&#x27;&lt;/script&gt;</p>')
        self.assertEqual(ET.fromstring(result["xml"]).text, value)
        self.assertEqual(json.loads(result["json"]), {"message": value})
        # A JSON serializer can retain a closing-script sequence.
        self.assertIn("</script>", result["json"])

    def test_encoding_rejects_control_and_excess_length(self):
        for value in ["", "a\x00b", "a\nb", "x" * 257]:
            with self.subTest(value_length=len(value)):
                with self.assertRaises(ValueError):
                    lab.encode_text(value)

    def test_parameterized_lookup_preserves_query_intent(self):
        self.assertEqual(lab.lookup_label("amber"), [("amber",)])
        self.assertEqual(lab.lookup_label("' OR 1=1 --"), [])
        self.assertEqual(lab.lookup_label("x'; DROP TABLE labels; --"), [])
        self.assertEqual(lab.lookup_label("blue"), [("blue",)])

    def test_sql_rejects_invalid_type(self):
        with self.assertRaises(TypeError):
            lab.lookup_label(12)

    def test_fixture_valid_and_size_boundary(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as name:
            root = Path(name).resolve()
            target = root / "notes.txt"
            target.write_bytes(b"a" * 1024)
            self.assertEqual(lab.read_fixture(root, "notes.txt"), b"a" * 1024)
            target.write_bytes(b"a" * 1025)
            with self.assertRaisesRegex(ValueError, "too large"):
                lab.read_fixture(root, "notes.txt")
        self.assertFalse(root.exists())

    def test_fixture_rejects_path_syntax_before_io(self):
        with patch.object(lab.Path, "resolve") as resolve:
            for name in ["../notes.txt", "..\\notes.txt", "C:\\notes.txt",
                         "notes.txt:stream", "/notes.txt", "NOTES.TXT"]:
                with self.subTest(name=name), self.assertRaises(ValueError):
                    lab.read_fixture("unused", name)
            resolve.assert_not_called()

    def test_fixture_missing_or_directory(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as name:
            root = Path(name)
            with self.assertRaises(FileNotFoundError):
                lab.read_fixture(root, "notes.txt")
            (root / "notes.txt").mkdir()
            with self.assertRaises(ValueError):
                lab.read_fixture(root, "notes.txt")

    def test_fixture_simulated_resolved_parent_escape(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as name:
            outer = Path(name).resolve()
            root = outer / "owned"
            root.mkdir()
            outside = outer / "notes.txt"
            outside.write_bytes(b"outside selected root")
            with patch.object(lab.Path, "resolve",
                              side_effect=[root, outside]):
                with self.assertRaises(ValueError):
                    lab.read_fixture(root, "notes.txt")

    def test_backup_roundtrip_and_byte_tamper(self):
        data = b"configuration=v1\n"
        manifest = lab.seal(data, KEY)
        self.assertIs(lab.verify_backup(data, manifest, KEY), True)
        self.assertIs(lab.verify_backup(b"configuration=v2\n", manifest,
                                       KEY), False)
        self.assertIs(lab.verify_backup(data, manifest, b"x" * 32), False)

    def test_backup_replaced_unkeyed_hash_is_insufficient(self):
        first = lab.seal(b"one", KEY)
        forged = dict(first, sha256=lab.seal(b"two", KEY)["sha256"])
        self.assertEqual(forged["sha256"], lab.seal(b"two", KEY)["sha256"])
        self.assertIs(lab.verify_backup(b"two", forged, KEY), False)

    def test_backup_schema_length_and_digest_validation(self):
        manifest = lab.seal(b"x", KEY)
        for bad in [dict(manifest, length=True), dict(manifest, length=2),
                    dict(manifest, mac="g" * 64), dict(manifest, mac=None),
                    dict(manifest, extra=1), {}]:
            with self.subTest(keys=list(bad)):
                self.assertIs(lab.verify_backup(b"x", bad, KEY), False)

    def test_backup_rejects_invalid_key_or_payload(self):
        for data, key in [(b"x" * 1025, KEY), ("x", KEY), (b"x", b"bad")]:
            with self.subTest(data_type=type(data).__name__):
                with self.assertRaises(ValueError):
                    lab.seal(data, key)

    def test_owned_loopback_roundtrip(self):
        self.assertEqual(lab.owned_loopback(), "LAB\n")

    def test_tls_policy_without_handshake(self):
        self.assertEqual(lab.tls_policy(), dict(check_hostname=True,
                                               require_certificate=True))

    def test_child_keeps_shell_like_text_in_one_argument(self):
        value = 'x & echo FAKE; $(FAKE) "quoted" --flag'
        self.assertEqual(lab.child_echo(value), [value])

    def test_child_propagates_timeout_and_validates_first(self):
        error = subprocess.TimeoutExpired("synthetic", 5)
        with patch.object(lab.subprocess, "run", side_effect=error) as run:
            with self.assertRaises(subprocess.TimeoutExpired) as raised:
                lab.child_echo("example")
            self.assertIs(raised.exception, error)
            self.assertFalse(run.call_args.kwargs["shell"])
            self.assertEqual(run.call_args.kwargs["timeout"], 5)
            run.reset_mock()
            with self.assertRaises(ValueError):
                lab.child_echo("bad\ninput")
            run.assert_not_called()

    def test_chain_halts_before_later_side_effects(self):
        called = []

        def after():
            called.append("should not run")
            return True

        result = lab.run_chain([
            ("check", lambda: True), ("backup", lambda: False),
            ("cleanup", after), ("report", after),
        ])
        self.assertEqual(called, [])
        self.assertEqual(result, [dict(stage="check", status="passed"),
                                  dict(stage="backup", status="failed")])

    def test_chain_records_error_type_without_sensitive_message(self):
        def failed():
            raise RuntimeError("synthetic secret: do not log")

        result = lab.run_chain([("check", failed)])
        self.assertEqual(result, [dict(stage="check", status="error",
                                       error_type="RuntimeError")])
        self.assertNotIn("secret", json.dumps(result))

    def test_chain_requires_exact_success_and_preserves_order(self):
        self.assertEqual(lab.run_chain([("check", lambda: 1)]),
                         [dict(stage="check", status="failed")])
        self.assertEqual(lab.run_chain([]), [])
        result = lab.run_chain([(n, lambda: True) for n in ["a", "b"]])
        self.assertEqual(result, [dict(stage="a", status="passed"),
                                  dict(stage="b", status="passed")])

    def test_pdf_info_removal_leaves_xmp(self):
        self.assertEqual(lab.pdf_metadata_probe(), dict(
            info_removed=True, xmp_creator=["Synthetic creator"], pages=1,
        ))


if __name__ == "__main__":
    unittest.main()
```

### observations.py

```python
"""Original computed PCES observations; no external target or service."""

import hashlib
import json
from pathlib import Path
import tempfile

import security_workbook as lab
from test_security_workbook import KEY, NOW, sample_events


def main():
    checks = []

    def check(name, condition):
        if condition is not True:
            raise AssertionError(name)
        checks.append(name)

    events = sample_events()
    original = json.dumps(events, sort_keys=True)
    rows = lab.correlate(events, NOW, KEY)
    check("three failures across three sources", rows[0]["failures"] == 3)
    check("timezone normalization", rows[0]["first"] ==
          "2026-09-30T00:00:00+00:00")
    check("preserve original records", original ==
          json.dumps(events, sort_keys=True))
    check("duplicate replay not counted", rows ==
          lab.correlate(events + events, NOW, KEY))
    check("raw subject omitted", "=synthetic-user()" not in json.dumps(rows))
    csv = lab.csv_report(rows)
    check("CSV omits raw subject", "=synthetic-user()" not in csv)
    encoded = lab.encode_text('</script><b title="fixture">&</b>')
    check("HTML text encoded", "<script" not in encoded["html"] and
          "&lt;/script&gt;" in encoded["html"])
    check("JSON is not script embedding protection",
          "</script>" in encoded["json"])
    check("SQL attack-shaped value stays data",
          lab.lookup_label("' OR 1=1 --") == [])
    roundtrip = lab.owned_loopback()
    check("owned loopback", roundtrip == "LAB\n")
    tls = lab.tls_policy()
    check("TLS hostname requirement", tls["check_hostname"] is True)
    check("TLS certificate requirement", tls["require_certificate"] is True)
    child = lab.child_echo('fixture & $(fake) --flag "quoted"')
    check("fixed child argument roundtrip",
          child == ['fixture & $(fake) --flag "quoted"'])
    pdf = lab.pdf_metadata_probe()
    check("PDF Info removed", pdf["info_removed"] is True)
    check("PDF XMP creator survives", pdf["xmp_creator"] ==
          ["Synthetic creator"])

    with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as name:
        root = Path(name).resolve()
        check("owned temporary root", root.parent ==
              Path(__file__).resolve().parent)
        payload = b"mode=synthetic\nversion=1\n"
        (root / "notes.txt").write_bytes(payload)
        source = lab.read_fixture(root, "notes.txt")
        manifest = lab.seal(source, KEY)

        def backup():
            with (root / "backup.bin").open("xb") as stream:
                stream.write(source)
            return True

        def restore():
            data = (root / "backup.bin").read_bytes()
            if not lab.verify_backup(data, manifest, KEY):
                return False
            with (root / "restored.bin").open("xb") as stream:
                stream.write(data)
            return (root / "restored.bin").read_bytes() == payload

        stages = lab.run_chain([
            ("precheck", lambda: source == payload),
            ("backup", backup), ("restore", restore),
        ])
        check("actual write and restore chain", stages == [
            dict(stage="precheck", status="passed"),
            dict(stage="backup", status="passed"),
            dict(stage="restore", status="passed"),
        ])
        modified = payload.replace(b"=1", b"=2")
        plain_forgery = dict(manifest,
                             sha256=hashlib.sha256(modified).hexdigest())
        check("changed bytes rejected",
              lab.verify_backup(modified, manifest, KEY) is False)
        check("replaced plain hash rejected",
              lab.verify_backup(modified, plain_forgery, KEY) is False)
        check("original preserved", (root / "notes.txt").read_bytes() ==
              payload)
    check("temporary tree removed", root.exists() is False)

    result = dict(
        passed_checks=len(checks), checks=checks, correlation=rows,
        csv=csv, context_encodings=encoded, loopback=roundtrip,
        tls_policy=tls, child_arguments=child, pdf=pdf,
        restore_chain=stages, backup_manifest=manifest,
        limits=[
            "Public fixture key; not confidentiality or key management",
            "Pseudonymized identifiers, not anonymous records",
            "One owned loopback listener; no scan or TLS handshake",
            "TLS policy inspection; no remote certificate verification",
            "One blank PDF; no document sanitization or AES execution",
            "Private owned path; simulated escape test is not TOCTOU proof",
            "One byte fixture restored; not application recovery or RTO/RPO",
            "No scheduler, notification, service restart or package install",
        ],
    )
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
```

## Original knowledge checks

1. Contrast threat, vulnerability, likelihood, impact, and risk.
2. Map loss, theft, and modification to CIA effects.
3. Why is security a continuous process?
4. What is the first step in hardening?
5. Why is a closed port not proof of security?
6. Contrast authentication and authorization.
7. Why are two passwords not MFA?
8. What must written assessment authorization define?
9. Why is a version banner not a confirmed vulnerability?
10. What risks does `shell=True` create?
11. What fields support event correlation?
12. When is a backup verified?
13. Why must output encoding be context-specific?
14. What should an application log omit?
15. Why prefer authenticated encryption?
16. Why verify SSH host keys?
17. Why can a checksum next to a download be insufficient?

## Answers and reasoning

1. A threat is a possible harmful actor/event; a vulnerability is an exploitable weakness; likelihood and impact describe a scenario's exposure. Name the asset and evidence before assigning risk. A scary banner alone is not an assessment.
2. Loss commonly harms availability, theft confidentiality and alteration integrity. A ransomware event may combine all three and create safety, contractual and reputational consequences.
3. Assets, configuration, dependencies and threats change. Continuous inventory, review and verification detect drift; an earlier clean check remains evidence only for its scope and time.
4. Establish owner, scope, inventory and intended baseline. Preserve management access and rollback before sequencing changes; verify both allowed and denied behavior afterward.
5. Other interfaces, identities, application paths or misconfigurations remain. A timeout can also reflect filtering or connectivity, not proof of a secure host. Our loopback test assesses only its own listener.
6. Authentication establishes an identity claim; authorization evaluates a particular action/resource. Correct credentials do not grant every permission or prove an instruction is legitimate.
7. Two passwords share the knowledge factor. Independent factors reduce different risks, but manually entered OTP remains phishable; enrollment and recovery can undermine otherwise strong authentication.
8. Define owner permission, exact targets/window, allowed techniques, data handling, rate/impact limits and stop/escalation contacts. A learning site's public availability does not authorize probing unrelated infrastructure.
9. A banner can be stale, customized or hide backported fixes. Verify the relevant configuration and advisory applicability within authorized scope; do not jump from version text to exploitation.
10. A shell interprets metacharacters. Our fixed executable/program receives the hostile-looking string as one data argument. Batch files and the child's own parser have additional risks; `shell=False` is not a universal sanitizer.
11. Preserve source/id, original time, normalized time, subject/host and event meaning. Handle duplicate/conflicting events, missing clocks and uncertainty. Three failures in a window are a triage lead, not attribution.
12. A scoped restore must recover the required bytes and usable application state within recovery requirements. The workbook verifies only one 25-byte fixture, so application consistency and operational recovery remain unproven.
13. HTML, XML, JSON, SQL and shell parsers assign different meaning to text. The JSON example preserves a closing-script sequence. Use the destination's API and avoid embedding data into executable contexts.
14. Omit secrets and unnecessary personal data; restrict access and retention. The chain reports only error type/stage. HMAC identifiers are linkable pseudonyms, and the public fixture key protects no real identity.
15. Authenticated encryption detects unauthorized alteration while protecting content. Key compromise defeats both; Fernet's visible timestamp and memory needs also matter. This review executed HMAC integrity, not Fernet encryption.
16. A trusted expected host key helps establish the server identity. Automatically adding an unknown key does not prove it is the intended server. Credentials alone authenticate the client, not that server.
17. An attacker may replace both artifact and adjacent plain checksum. Obtain the expected value through independent trust or use an authenticated manifest; our altered fixture with a replaced hash still fails its original MAC.

## Readiness checklist

- [ ] I can evaluate CIA, threats, risk, impacts, controls, and incident communication.
- [ ] I can explain and verify hardening, network exposure, identity, SaaS/cloud, and remote access.
- [ ] I can perform only authorized Python checks with timeouts, least privilege, logging, and defensible conclusions.
- [ ] I can correlate/report/schedule tasks and prove backups restore.
- [ ] I can validate, encode, protect secrets/files/errors, and explain safe cryptography/SSH boundaries.
- [ ] I can distinguish integrity from authenticity and obtain expected hashes safely.
- [ ] I completed the labs only in isolated authorized environments.

## Source and freshness notes

- [Official PCES syllabus](https://pythoninstitute.org/pces-exam-syllabus) controls the objective map.
- [Official PCES page](https://pythoninstitute.org/pces) controls live status/delivery and contains practice-test timing that should be rechecked.
- Use current primary documentation for [Python](https://docs.python.org/3/), [psutil](https://psutil.readthedocs.io/en/latest/), [cryptography](https://cryptography.io/en/latest/), and [Paramiko](https://docs.paramiko.org/).

## Places to learn

This is **not a complete list** and is not intended to be consumed in full. All times below are **author planning budgets**, not measured course durations or claims of completion. Use one foundation and the relevant reference sections, then demonstrate outcomes in authorized labs.

| Resource | Access | Estimated time |
|---|---|---:|
| [PCES syllabus](https://pythoninstitute.org/pces-exam-syllabus) | Public canonical scope; full English objectives/MQC read, PDF pending | 2–4 selected hours |
| [Python documentation](https://docs.python.org/3/) | Public; index read and selected pinned 3.13 contracts used above, not every manual | 8–15 selected hours |
| [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) | Public; index plus selected SQL/XSS passages reviewed | 6–10 selected hours |
| [PortSwigger Web Security Academy](https://portswigger.net/web-security) | Public materials and free account for full lab/progress access; some labs need tools, with Community Edition advertised as a free option | 10–20 selected hours |
| [OverTheWire Bandit](https://overthewire.org/wargames/bandit/) | Public beginner level guidance; remote SSH game not attempted | 8–15 selected hours |
| Original workbook above | Three public original files; installed pypdf needed for metadata experiment | 2–4 hours to inspect, execute and explain |

The previous recommendation titled “Practical Python Security” was removed: its [O'Reilly URL](https://www.oreilly.com/library/view/practical-python-security/9781098142155/) identifies **Kubernetes Best Practices, 2nd Edition**. An ISBN-backed page does not validate the old title or relevance. No replacement title, subscription entitlement or book interior was inferred.

The complete public Academy landing and Bandit introduction were read, not the individual labs. No account, external SSH login, tool download, paid interior or protected exam content was accessed. Package APIs, access and practice availability need rechecking when a future lab is actually run. Missing cryptography/Paramiko/psutil/document/scheduler tools and independent human content/accessibility review remain explicit blockers to broader completion.
