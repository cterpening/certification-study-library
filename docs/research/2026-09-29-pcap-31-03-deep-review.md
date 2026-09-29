# PCAP-31-03 deep review — September 29, 2026

The [study guide](../../guides/PCAP-31-03-python-certified-associate-python-programmer.md) now maps **21 numbered objectives** in groups 5/2/3/6/5 and improves all **27 original answer explanations**. The five weights remain 12/14/18/34/22, with 6/5/8/12/9 items. This same-context AI review retains human review as pending.

## Scope and source evidence

The public English [syllabus](https://pythoninstitute.org/pcap-exam-syllabus) was read completely through indexed web content after direct fetching, web opening and automated monitoring failed. Manual comparison supports retaining the existing snapshots; it is not a successful new automated hash comparison. The dated PDF was available only as an indexed cover/table excerpt. Its section raw totals and the HTML per-item wording do not support equal item weighting or an inferred count of correct answers needed to pass.

The full [English exam page](https://pythoninstitute.org/pcap) still marks 31-03 active and 31-04 in development with a Q3 2026 announcement. An announced quarter does not prove release. English five-year validity conflicts with indexed Japanese lifetime wording. The complete indexed TestNow policy specifies 15 days after a failed PCAP attempt, while a generic footer says seven days; selected Pearson policy excerpts support 15 days and no same-version passed retake. Practice redemption instructions differ between the credential page and public store. These remain explicit verification limits, not silently resolved facts. No account or booking flow was entered.

There are **31 registered sources**, with direct outcomes **{'ok': 23, 'error': 7, 'blocked': 1}**. Twenty-three HTTP successes do not mean full content review: Cisco returned a shell, and public product/path pages do not expose paid interiors. Each technical reading boundary is recorded. The unversioned Python index shows 3.14.7; selected pinned 3.13 documentation supports the actual existing CPython 3.13.14 runtime. No exam-required patch version or all-linked-chapters audit is claimed.

## Teaching and execution

Twelve exact public Python blocks were extracted, hashed and executed. They include the workbook, two introductory class examples, a real seven-file report package, Unicode catalog and ID sampler. The workbook passed **78 core checks**; **98 additional scenario/language checks** passed using temporary original modules and files. The latter count includes process/output checks and does not imply 98 separate learner labs.

The package verifies silent imports, qualified module/class names, import bindings, module identity, bytecode cache, explicit/default star exports, mutation versus rebinding, domain errors, row snapshots and polymorphism. It runs with `python -m reports`; bare-file invocation intentionally fails relative-import resolution. CSV output round-trips comma, quote, embedded newline, Unicode and empty fields through the actual writer/reader. Plain output is display text, not a reversible row format.

The catalog decodes captured raw bytes strictly, preserves case/normalization, rejects blank product rows, accepts empty input and an unterminated last line, and writes a binary checksum through exclusive creation. Tests cover malformed UTF-8, missing paths, existing output and buffer sizes that leave a short final chunk. The checksum describes the exact bytes read once; it does not authenticate them. Exclusive creation preserves prior output, but an operating-system write failure could leave a partial newly created file. No atomicity or failure-injection claim is made.

The sampler rejects duplicate/empty/non-string IDs and invalid sizes/seeds, preserves the input and global random state, and repeats within the tested runtime. It distinguishes sampled occurrences from unique values and avoids a cross-version sequence promise. Other checks cover factorial float rejection, all named platform calls, empty/cased/numeric string predicates, real `hasattr` behavior, optional instance dictionaries, cooperative diamond MRO, normal versus early `try` exit, re-raise traceback, optimized-away assertions, file closure and text EOF versus blank lines.

These are original programs and fixtures, not copied certification questions or course labs. No interpreter/package installation, live infrastructure deployment, interactive debugger session, OS permissions/disk-failure injection or cross-platform guarantee occurred. The catalog's `live-partial` label describes actual local original-code execution. Ten broader learner activities remain proposed.

## Learning content and remaining limits

The complete OpenEDG course landing lists **58 hours**, correcting the prior 40–50-hour estimate. Four modules include broader PIP/generator/library content and retained 31-02/31-03 alignment; course breadth does not change exam scope. The complete public Pluralsight path lists 16 courses, 21 labs and 53 hours, with substantial content beyond PCAP. Author-selected time budgets remain separate from these provider totals. Harvard's ten-week free course landing was read through web fallback; individual lecture/problem interiors were not reviewed.

The public practice product lists USD49, twelve-month redemption and five launches per test, with no official exam attempt included; no paid questions or answer explanations were accessed. Cisco shell and OReilly403 prevent current interior/duration verification. Source conflicts, inaccessible content, current booking/account details and human review keep the outcome **reviewed-with-blockers**.

The [operation record](https://github.com/cterpening/certification-study-library/blob/main/ADLC_Docs/operations/2026-09-29-pcap-31-03-deep-review.json) preserves mappings, selected-reading limits, exact source hashes, process receipts and the original boundary harness. Full unit, repository, catalog and strict generated-site gates are recorded after completion. No external message, enrollment, voucher or purchase occurred.
