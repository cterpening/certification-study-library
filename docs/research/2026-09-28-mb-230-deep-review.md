# MB-230 deep review — September 28, 2026

The entire guide and all 50 detailed objectives were reviewed. The update adds six worked examples, ten labs and 48 answered checks, including answers to all 36 existing questions. Two useful blog tasks supplement the official material. Independent human review and live tenant labs remain pending.

## Objective and lifecycle evidence

The March 11, 2026 baseline is unchanged in meaning. The ten groups contain 4/5/4/5/6/8/2/4/9/3 objectives. Forty-eight bullets exactly match the prior snapshot; two had been paraphrased locally: “including by using AI” had lost “by using,” and “key performance indicators (KPIs)” had been shortened to “KPIs.” The old snapshot also summarized the audience and included local capture text. The new snapshot restores the complete canonical extraction rather than announcing an exam revision.

The prior objective and status files are preserved under dated September 1 filenames, and historical audit/review references retain their hashes. The objective hash changes from `02105f2bbafe2b5a53a2f55604a18cdd0af2d68c842cc5d285ac8abc41a52e7e` to `e5925c65c9de7fad2e0d1d921564490a83ce02092b95ad95382775abd6352b38`; status normalization changes from `a3ac151557316ac10fc8709a8bb476343735f7db03afb695d7a6ad9dd10b13b2` to `4cf37ffbb9684b28047947f6cc9464d0e6c5ecef7e09d2dacd47be0e087c9c57`.

The [credential](https://learn.microsoft.com/en-us/credentials/certifications/d365-functional-consultant-customer-service-v3/) remains active, with 100 minutes, seven languages and annual renewal. Its older update banner remains a discrepancy; the [study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-230) controls the objective baseline. Detailed mappings, prior records, comparison/overlap evidence and validation are in `ADLC_Docs/operations/2026-09-28-mb-230-deep-review.json`.

## Repairs and learning value

The SLA scenario no longer promises one runtime KPI-instance ID throughout a case. [Pause/resume guidance](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/set-pause-conditions-sla) specifies successor instances and override precedence. The original holiday/pause calculation separates business time from wall time. [Schedule guidance](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/change-schedules) also prevents treating a calendar edit as immediate recalculation of every active deadline.

Capacity guidance now acknowledges manual overrides, custom limits below existing workload and end-of-day resets with open work remaining. A routing example distinguishes three cases from five work-item records after reassignment. Current telemetry and analytics replace reliance on the legacy diagnostics setup; specific [retirement notices](https://learn.microsoft.com/en-us/dynamics365/customer-service/implement/deprecations-customer-service) also correct older suggestion-feature guidance.

[Knowledge setup](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/set-up-knowledge-management-embedded-knowledge-search) supplies the environment/table access boundary. Search filters and draft/internal labels are not presented as authorization. Federated and ingested providers are distinguished, including static sitemap requirements and copy freshness. Teams guidance separates meeting handoff, the continuing voice call and recording storage.

Agent configuration distinguishes automation levels, triggers, identity, mailbox and consumption prerequisites. [Current case-resolution setup](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/set-up-case-resolution-agent) labels simulation/shadow evaluation as preview and metered. The guide follows the explicit confirmation setting rather than interpreting less precise runtime-table sending language as permission to bypass it. An inconsistent status example on the follow-up page was not copied.

Macro exercises distinguish the anchor case from a selected account tab and make partial replay visible. Survey guidance separates the regarding record, Contact association, generic links, saved variables and per-invitation response limits. Original examples explain evaluation denominators, invitation idempotency and response bias without sending messages or using customer data.

## Blog decisions

| Article | Accepted learning task | Qualification |
|---|---|---|
| [Shadow Mode](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/07/09/shadow-mode-case-management-agent/), Madhuri Somara, Peter Bian and Saurabh Gupta, July 9, 2026 | Compare proposed actions with adjudicated outcomes and action severity. | Product documentation retains preview/metered boundaries; the production-oriented blog is not a support guarantee or proof of executed actions. |
| [Service Agent changes](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/07/15/service-agent-microsoft-365-copilot-customer-service/), Saurabh Gupta and Rushil Vora, July 15, 2026 | Distinguish answers, drafts and actions across application contexts. | Optional context; exact tool counts, future roadmap and broad licensing claims are not new exam objectives. |

Both main articles were read; linked media and tenant procedures were not executed.

## Learning catalogs

The seven official paths have refreshed titles/descriptions and contain 29 module placements but only 25 distinct modules. The SLA/entitlement, case-management and Customer Voice overlaps are documented in the receipt. Current public pages do not expose the prior durations, so the old 29h02 sum was withdrawn. Practice-hour ranges are planning estimates, not provider runtimes.

The official course remains four days in English. Pluralsight lists Vovwe Enyoyi, May 6, 2026, 47 minutes and an extension-focused outline. A browser-indexed Udemy copy, crawled about two months earlier, lists June 2026, 15 sections, 23 lectures and 3h38; this conflicts with the prior August/4h16 observation. Direct access remains blocked, so the new observation is not presented as a confirmed live catalog rollback. The partner page is a login shell and the assessment endpoint returned no substantive text. No paid content or assessment questions were accessed.

## Validation and follow-up

Thirty-one local assertions passed for the original calendar, capacity, routing counts, evaluation/survey arithmetic, invitation keys and catalog overlap. They do not test Dynamics runtime behavior, delivery, concurrency, prices or tenant support. Repository tests, metadata/catalog checks, strict site build, generated-site validation and whitespace checks are recorded in the receipt after success.

October 26 follow-ups cover agent preview/confirmation wording, lifecycle metadata and learning catalogs. Weekly automation detects changes and queues reviews; it does not perform the semantic review. The [Microsoft review tracker](../MICROSOFT-REVIEW-STATUS.md) retains the remaining backlog.

Long product pages were read selectively; complete role, source, region and channel matrices were not exhaustively audited. No cloud configuration, telemetry export, flow, survey, email, Teams meeting or agent execution occurred. The applied guidance has no unresolved source blocker; documented runtime/preview limitations still require validation before a real deployment.
