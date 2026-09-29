# LFCA deep review — September 29, 2026

Same-context AI review; independent human review pending. [Study guide](../../guides/LFCA-linux-foundation-certified-it-associate.md).

## Scope and lifecycle

The [official exam page](https://training.linuxfoundation.org/certification/certified-it-associate/) and [2025 notice](https://training.linuxfoundation.org/lfca-program-changes-2025/) still publish 22 competencies, grouped 2/5/5/3/3/4 with weights 16/30/18/14/12/10. The September 16, 2025 baseline remains current, LFCA-JP remains retired and no replacement announcement was observed. Objective and status hashes are unchanged; no accepted snapshot was rewritten. The public outline is broad, so the guide labels original implementation depth without inventing detailed official command objectives.

The [language table](https://docs.linuxfoundation.org/tc-docs/certification/lf-handbook2/language) confirms English; the [multiple-choice FAQ](https://docs.linuxfoundation.org/tc-docs/certification/faq-mc) lists 90 minutes, 75% pass and two-year validity. Current exam-page prerequisites, retake and eligibility metadata were checked. No question count inferred or recalled assessment material accessed.

## Teaching and executed evidence

Added original Git and Bash examples with **35 passed local checks** using Git 2.55.0.windows.5, MSYS Bash 5.3.15 and Python 3.13.14. Both public code blocks match executed files. Git checks cover committed/staged/working snapshots, cached/ordinary diffs, unstaging, two conflict attempts with verified abort and reviewed resolution, tracked versus ignored synthetic logs, retained history and absence of remotes. Shell checks cover quoted paths, grouping, stream redirection order, pipeline failure propagation and grep no-match versus error. Owned temporary files and repositories were cleaned.

The [Git merge manual](https://git-scm.com/docs/git-merge) supports the clean-start/abort qualification. GNU-hosted Bash retrieval timed out; the [maintainer reference](https://tiswww.case.edu/php/chet/bash/bashref.html) supplied targeted current shell documentation, backed by actual installed-runtime execution. No global Git settings, remotes, credentials, network services or notifications were used by the examples.

Corrected [APT trust](https://manpages.debian.org/trixie/apt/apt-secure.8.en.html) to distinguish authenticated repository metadata/checksums from individual-package signatures or code review. Added [unlink permission](https://man7.org/linux/man-pages/man2/unlink.2.html), [systemctl activation](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html), container/VM kernel and data-control evidence distinctions. Native Linux runtime validation remains deferred from the prior WSL blocker. MSYS does not prove native permission, systemd, package or networking behavior.

Original project critical-path, cloud cost/failure-capacity, recovery and error-fraction examples state hypothetical inputs. Functional-analysis cases map actors, requirements, exceptions and acceptance evidence. The [2020 Scrum Guide](https://scrumguides.org/scrum-guide.html) supports the current accountabilities; [OSI](https://opensource.org/osd) and [SPDX](https://spdx.org/licenses/) support license rights versus source visibility and standardized identification. No legal compatibility conclusion is made. There are 46 answered checks, three integrated scenarios and eight expanded full labs with success/negative-case evidence; those full labs remain proposed.

## Catalog and limits

LFS200 lists 10–15 hours, an Ubuntu 20.04 VM and the old Supporting Applications and Developers chapter title. Pluralsight lists one A Cloud Guru course at 11h47 dated August 6, 2025, rounds the path to 12 hours and retains the same old final-domain wording. Both need explicit mapping to the current project-management competency. Canonical’s release table distinguishes Ubuntu 20.04 standard security maintenance ending May 2025 from separate extended coverage; no VM upgrade was performed.

Coursera LearnQuest lists four course durations of 16/17/14/12 hours, totaling 59, while its landing estimate is four weeks at ten hours per week. Qualified these as differing provider estimates. The actual one-page LF curriculum PDF was read: suggested 3–6 months, courses explicitly not required. Public free-resource descriptions were checked; paid lessons, provider labs and assessment questions were not accessed. Places to learn is final.

Repository validation, 176 unit tests, strict site build, generated-site validation, catalog consistency and diff checks are recorded after execution. Review outcome remains reviewed-with-blockers because native Linux validation is deferred; public scope and technical-source freshness is current using the available primary alternatives.
