# PCES-30-01 deep review — September 30, 2026

The [guide](../../guides/PCES-30-01-python-certified-entry-level-security-specialist.md) now maps all **45 detailed objectives**, grouped 10/12/13/10, and expands **17 answers**. Three exact original files pass **30 test methods and 21 observation checks in each normal/optimized mode**, using already installed CPython 3.13.14, pypdf 6.16.1 and Ruff 0.16.4. The result remains **reviewed with blockers**; twelve broader lab plans and independent human review are not complete.

## Scope and primary readings

The complete indexed [canonical English syllabus](https://pythoninstitute.org/pces-exam-syllabus), every detailed bullet and full MQC profile were read after direct retrieval and the automated monitor failed. The old snapshot summarizes 19 topic headings; it is retained as historical evidence while a separate 45-objective manual map supplies detail. No fresh automated hash success or full PDF reading is claimed. The MQC's grouping of psutil/cryptography/paramiko as standard libraries is corrected: these are third-party packages.

The complete [credential body and FAQ](https://pythoninstitute.org/pces) and [testing policy](https://pythoninstitute.org/pces-testing-policies) were read through indexed fallback. Active 30-01, seven-year validity and exam logistics remain consistent. Practice descriptions still say planned Q3/coming Q3–Q4; September 30 does not prove launch. PCAS's announced path is separate from PCES. The specific failed-retake rule says seven days, whereas generic footer prose also mentions passing. No account, booking, purchase, system test or protected questions were accessed.

Selected pinned Python 3.13 contracts support the actual examples; documents identify 3.13.15 while the interpreter is 3.13.14. Complete Fernet, Paramiko client and pypdf metadata/encryption bodies were read. Cryptography docs identify 51.0.0-dev1; pypdf docs 6.19.0 differ from runtime 6.16.1. Neither documentation version establishes an exam requirement. Exact reading ranges, complete versus partial boundaries and hash-verified Ruff reuse are recorded in operation evidence.

## Original executed behavior

`security_workbook.py`, `test_security_workbook.py` and `observations.py` are embedded exactly and matched by hash before execution. Four recorded runs treat warnings as errors; both observation JSON results are identical. Thirty methods include boundary/type/schema/duplicate/error tests, and 21 computed observations expose actual outcomes. Selected Ruff rules at 79 columns pass; this is not Pylint/Flake8 execution or a security audit.

One ephemeral listener binds only 127.0.0.1, accepts the workbook's own connection, exchanges four bytes and closes every socket. No ports or external hosts are scanned. A TLS client context is inspected for certificate and hostname requirements and loads existing trust anchors; it performs no handshake or trust-store change. Synthetic timestamp tests establish inclusive seven-day expiry boundaries, not a real certificate verdict.

The fixed short Python child receives shell-like text as one data argument under isolated mode, with no shell and a timeout. Actual argument round-trip and simulated timeout propagation are distinct evidence. An in-memory SQLite query binds values and rejects attack-shaped strings as nonmatching data. Original HTML/XML/JSON examples retain parser-specific meaning: JSON serialization still contains a closing-script sequence, so it is not safe script embedding by itself. No browser or untrusted XML input was executed.

Synthetic events at differing offsets normalize to 00:00/00:02/00:04 UTC. The exact five-minute inclusive window, three-failure threshold, duplicate replay, conflicting identity, future/old/success exclusions and host separation are tested. Original inputs remain unchanged; the report uses an HMAC subject token and controlled CSV fields. This is pseudonymization and a triage lead, not anonymity or attacker attribution. The deterministic fixture key is public test data.

The actual owned temporary file chain checks an original 25-byte payload, writes a backup, verifies a separate teaching manifest/key, restores to a new file and compares bytes while preserving the source. Modified bytes fail; replacing the adjacent plain SHA-256 still fails the original HMAC. The temporary tree is removed and its absence checked. This is one byte-recovery experiment, not application recovery, off-site resilience, RTO/RPO or real key management.

Filename allowlisting rejects traversal/drive/alternate-stream syntax before I/O, and a simulated resolved-path escape checks the guard. No real symlink/junction or race-free filesystem isolation is claimed. Failed/exceptional stages stop later callbacks and report only error type/stage, omitting a synthetic secret in the exception message. No persistent scheduler, service, alert or cleanup of existing user data was created.

The original one-page blank PDF demonstrates that removing document `/Info` leaves the XMP creator intact. No arbitrary document, text extraction, document sanitization, macro/hidden-content inspection, PDF incident report or encryption was performed. Both AES backends are absent; the guide warns against pypdf's implicit RC4 default. Installed pypdf is not silently equated with all named PyPDF2/python-docx/openpyxl objectives.

## Material content and catalog repairs

The previous [O'Reilly URL](https://www.oreilly.com/library/view/practical-python-security/9781098142155/) identifies **Kubernetes Best Practices, 2nd Edition**, not the listed “Practical Python Security.” The incorrect recommendation is removed and catalog identity corrected with provenance; no substitute title or paid interior is invented. Public PortSwigger Academy and Bandit landings were reviewed, with free-account/tool boundaries and author planning budgets. No individual external lab was attempted.

Selected current [NIST authenticator requirements](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/) distinguish password-verifier guidance and phishing resistance from legacy policy-setting names. Scoped Commission/HHS/California primary readings support study examples that separate recipient, jurisdiction, trigger and time window; they do not determine a real organization's legal obligations. No password or host policy was changed.

## Remaining limits

There are 35 direct source receipts: 27 successful, six errors and two blocked. Indexed fallback content review is separate from reachability. Source evidence identifies unreviewed manual sections, PDF and linked course/book/lab interiors. Current practice availability and passed-retake wording remain unresolved.

Cryptography, Paramiko, psutil, PyPDF2, python-docx, openpyxl, APScheduler, python-nmap, Pylint, Flake8, Bandit and AES backends are unavailable and were not installed. External TLS/SSH validation, process inventory, hardening, antivirus, scheduling/notifications, all twelve full lab plans and independent human content/accessibility review remain pending. The executed workbook is a bounded learning artifact, not readiness approval or a production security assessment.

## Validation

Exact-source extraction, four execution receipts, computed results, hashes, dependency inventory and selected lint are recorded in `ADLC_Docs/operations/2026-09-30-pces-30-01-deep-review.json`. Repository tests, strict site generation, repository/site/catalog consistency and whitespace checks are recorded after their gates complete.
