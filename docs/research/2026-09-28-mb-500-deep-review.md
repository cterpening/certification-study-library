# MB-500 deep review — September 28, 2026

The entire guide was reviewed against 89 detailed objectives across 21 groups. It now contains six worked examples, ten labs and 48 original answered checks. One SQLite example and 34 local assertions passed; no X++ compilation, tenant, migration, API or paid-content execution occurred. Independent human review remains pending.

## Objective and lifecycle evidence

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-500) still uses January 30, 2026 and announces no newer baseline. The credential lists 100 minutes, English/Japanese and annual renewal, with no retirement listed.

The previous repository snapshot summarized seven domains in 22 bullets. Its bytes and historical references are archived under September 1; the canonical snapshot now retains all 89 detailed objectives. The additional rows restore detail rather than document a newly announced scope change. The receipt `ADLC_Docs/operations/2026-09-28-mb-500-deep-review.json` maps each objective hash to guide sections and records fetches, reading boundaries, source decisions and validation.

## Corrections and learning content

- Separate the exam's **Batch OData API**, which requeues jobs, from OData entity `$batch` changesets and asynchronous data-management packages. Requeue success is not completed business work.
- Correct the implication that XDS protects entity integrations. DataServices/DataManagement permissions require their own design; supported table policies intersect and have documented exclusions.
- Explain the LCS freeze's scope, UDE's Sandbox type and single-developer purpose, and the one-way migration preview. Commerce is unsupported during preview even though the checker does not detect its usage. Current tooling instructions specify Visual Studio 2022.
- Teach same-scope update selection, outer transaction durability, CoC ordering limits and exception-preserving retry. The retry FAQ assigns ordinary failed runtime-child recovery to a static controller; SQL transient retries are a separate mechanism.
- Add atomic receipt/effect, changeset partial-commit, security intersection and query-count examples. Business-event control numbers are not sequential versions. Package execution requires status/error and successful-row reconciliation.
- Preserve required update logic before optimization; `doUpdate()` and set-based fallback are behavioral concerns, not just speed choices.

The retry page's dynamic-task paragraph is broader than its runtime restriction. The guide uses the explicit runtime note and controller FAQ, with an October 5 recheck. Similarly, the Batch OData page describes terminal states before later listing “started.” The guide teaches bounded terminal-failure recovery and does not claim that requeuing a running job is supported. Neither wording issue is used as a deployment recipe.

## Article and catalog decisions

[Lane Swenka's September 2023 UDE announcement](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2023/09/15/announcing-unified-trial-and-developer-environments-for-dynamics-365-finance-and-operations-apps/) supports an architecture worksheet. Its preview, trial, capacity and add-in examples remain historical. The [Microsoft UDE TechTalk article](https://learn.microsoft.com/en-us/dynamics365/guidance/techtalks/unified-developer-experience) adds local-tool/cloud-runtime context; the video was not watched. [Richard Riley's roadmap transition](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/08/25/one-always-on-roadmap-dynamics-365-power-platform-and-dataverse-join-the-ai-at-work-roadmap/) informs discovery and the planned November retirement follow-up, without implying automated feed ingestion.

The six Learn paths expose 35 module placements and 34 distinct modules (8/9/4/8/4/2); migration preparation appears twice. Public overviews and module descriptions were read, but linked units were not. The old 43h02 subtotal is withdrawn because current pages do not expose aggregate runtimes. LCS-era modules require current portal reconciliation. The renamed official course is five days in English.

Public indexed Udemy metadata retains Arezou Behnam, October 2024, eight sections, 34 lectures and 4h04. Indexed O'Reilly contributor metadata identifies a Packt book by Adrià Ariste Santacreu, January 2024, 274 pages and a 5h48 platform estimate. Direct fetches remain blocked. MeasureUp's public 119-question January 2022 catalog is older than the blueprint; no paid or demo questions were inspected. Partner/practice bodies were unavailable and Pluralsight/Whizlabs were not comprehensively searched again.

## Validation and follow-up

Local checks exercise the guide's actual SQLite block, duplicate and conflicting replay, rollback after a simulated failure, unknown-company rollback and origin/company separation. They also check the original ordering, set, arithmetic and catalog examples. These checks do not establish X++ runtime semantics, concurrent delivery, tenant security or measured performance.

Required repository, catalog and strict-site gates are recorded in the receipt after completion. Long product references were read in the identified sections, not every linked feature or regional matrix. October 26 revisits UDE/migration and catalog drift; November 16 revisits the planned roadmap retirement. Live labs and independent human review remain outstanding.
