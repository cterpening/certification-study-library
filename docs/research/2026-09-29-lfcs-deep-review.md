# LFCS deep review — September 29, 2026

Same-context AI review; independent human review pending. [Study guide](../../guides/LFCS-linux-foundation-certified-system-administrator.md).

## Scope and lifecycle

The [official LFCS page](https://training.linuxfoundation.org/certification/linux-foundation-certified-sysadmin-lfcs/) retains 34 public competencies in groups 8/8/7/6/5 with weights 25/25/20/20/10. Reviewed the full current outline and distribution-independent performance assessment metadata. The exam remains two hours with no formal prerequisite, two-year credential validity, 12-month eligibility, one retake and two included 36-hour simulator activations. No new replacement announcement was observed. Both monitored hashes are unchanged and no accepted baseline was rewritten; simulator task counts are not generalized to the real exam.

## Teaching and execution

Corrected the [systemd service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) active-state simplification and added an explicitly proposed Linux oneshot exercise. [Timer](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html) catch-up/overlap behavior, effective process constraints, and libvirt live/defined/autostart state now have separate evidence. No unit, timer, VM or native Linux subsystem was configured.

Two exact original code blocks and a harness passed **38 checks**: Git for Windows OpenSSL 3.5.7, Python 3.13.14 with its separate OpenSSL 3.0.21 library, and MSYS Bash. Synthetic CA/CSR/leaf generation, CSR checking, public-key pairing, explicit trust/name/purpose validation, PEM/DER conversion, expiry windows and reference-time tests ran. Negative cases rejected wrong hostname, incompatible client purpose, future expiry/past validity, signature corruption, mismatched key and a conflicting SAN despite matching CN. These checks follow targeted [OpenSSL verification options](https://docs.openssl.org/3.5/man1/openssl-verification-options/).

The [Python TLS](https://docs.python.org/3.13/library/ssl.html) exercise made six real loopback attempts across harness and standalone execution: two successful ping/pong exchanges and four intended name/trust rejections with no application payload. Workers stopped, listeners closed and all owned files, certificates and keys were cleaned. Trust was confined to newly created SSL contexts; no system/browser trust, DNS, host clock, global configuration, credentials or external service changed. This is a synthetic TLS protocol, not HTTP, a reverse proxy, mutual TLS or production PKI. No intermediate chain or revocation policy was tested.

Expanded filesystem growth/shrink ordering and version boundaries. The [current upstream XFS manual](https://man7.org/linux/man-pages/man8/xfs_growfs.8.html) includes limited last-allocation-group shrinking, so neither a blanket historical prohibition nor broad present support is inferred. Installed kernel/xfsprogs, geometry and distribution support remain verification requirements. No storage resize was performed. Original extent/capacity/throughput, simple-route and ACL-bit calculations are labeled restricted models.

SSH test-mode versus actual login, SELinux expected-label repair, NBD file/block semantics, ACL matching/mask behavior and SSSD identity/authentication evidence were strengthened using targeted primary references. The guide has 46 answered checks, three integrated scenarios and eight full labs with acceptance and negative cases. The existing native Linux runtime blocker remains deferred; all eight complete Linux labs are proposed, and Windows/MSYS results do not claim native Linux administration coverage.

## Resource comparison and validation

LFS207 lists 50–60 hours and a 34-chapter cross-distribution outline. Pluralsight now lists 40 hours, 12 courses and three July 2026 labs; two courses have September 2026 updates but the summary retains older six-domain labels. KodeKloud lists 11.25 video hours, eight modules/103 lessons and two mock-exam titles, with a mislabeled networking section; those are public metadata only. Its lab-hour range is an original planning estimate. O’Reilly blocked rechecking, so earlier 11h57/June 2025 claims remain unverified. The actual one-page LF curriculum PDF was read and says the suggested 3–6 month route is not a mandatory prerequisite.

Paid interiors, provider labs, simulator tasks and assessment contents were not accessed. Places to learn is final. Repository validation, 176 unit tests, strict build, generated-site checks, catalog consistency and diff checks are recorded after execution. Outcome is reviewed-with-blockers because native Linux execution remains deferred; scope and public-source freshness are current.
