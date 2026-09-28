# MB-820 deep review — September 28, 2026

The entire guide was reviewed against 75 detailed objectives across 17 groups. It now contains six worked examples, ten proposed labs and 48 original answered checks. The guide's Python recipient model and 32 local assertions passed, including SQLite join/grain checks. No AL compilation, Business Central tenant, container, deployment, external API, webinar, paid-content or exam-assessment execution occurred. Independent human review remains pending.

## Scope and evidence

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-820) still uses June 10, 2025 with no newer announcement. The credential lists 100 minutes, seven languages and annual renewal, with no retirement displayed. The previous September 1 snapshot condensed the same objectives into 17 bullets. Its bytes and historical references are archived before restoring the canonical 75-objective text; the larger snapshot is not a new scope announcement.

The receipt `ADLC_Docs/operations/2026-09-28-mb-820-deep-review.json` records each objective hash and guide mapping, fetch evidence, prior records, article decisions, reading limitations and completed validation gates.

## Material corrections

- **Error capture is not rollback.** A Boolean-return try-method call catches an error without automatically reversing its writes. Boolean Codeunit.Run has a different commit contract. CommitBehavior governs explicit commits and does not suppress Codeunit.Run's implicit commit. The guide separates uncommitted local work, earlier commits and remote effects.
- **Transactional batching has a condition.** The specific batch documentation requires no intermediate AL COMMIT for one transaction. This qualifies the broader introductory wording in API tips. Inner outcomes and persisted records matter more than the outer envelope.
- **Sandbox read scale is unavailable.** Microsoft states that sandbox objects access the primary. ReadOnly is an intent, not guaranteed replica routing; Database Access Intent List overrides the request header, which overrides the object default. The lab now states what it can actually prove.
- **Current runtime controls matter.** HTTP permission, server-certificate validation, anti-SSRF and transport/status/payload outcomes are distinct. Partial-record loads and pass-by-value can defeat an optimization; hidden FlowField calculation depends on the visible-only feature state.
- **Upgrade and permissions require scope.** Upgrade tags need company, fresh-install and new-company handling; separate codeunit order is not guaranteed. Inherent permissions operate within the same extension and cannot be removed by ordinary administrator permission-set editing. IsHandled is corrected by name and minimized as Microsoft recommends.
- **Testing has environment limits.** Online production does not permit automated tests; bounded sandbox checks and larger container-based suites have different roles. The guide adds test-runner/handler evidence and distinguishes attempt metrics from eventual business outcomes.
- **Announced removals are specific.** The current platform register describes v29 Microsoft-page SOAP and on-premises data-only permission-set changes, then v30 Microsoft-page OData and PTE upload-surface changes. The guide does not claim that all SOAP/OData is already unavailable. Current SaaS PTE administration points to Admin Center/API.

The original examples cover a stable recipient-enforced operation ID, conflicting replay, cross-company identity, a 300-versus-150 report fan-out, commit-separated partial persistence, 140-record company migration coverage, payload reduction and 95% eventual versus 79.17% attempt success. They are simplified models, not measured service guarantees or AL runtime tests.

## Article and catalog decisions

[Stefano Demiliani's September 1 outbox article](https://demiliani.com/2026/09/01/why-your-business-central-job-queue-needs-idempotent-external-effects-when-integrating-external-systems/) supplies a useful remote-success/local-failure exercise. Its illustrative code was not compiled. The guide qualifies broad rollback, retry and DELETE-404 statements using the current transaction contract and resource identity; it does not claim a local flag provides exactly-once delivery.

[Steven Renders's March 17 API comparison](https://thinkaboutit.be/2026/03/api-pages-vs-api-queries-in-business-central-when-to-use-each/) was read in full and accepted for contract-selection prompts only. Its blanket SOAP/OData retirement and guaranteed-replica implications exceed the [primary deprecation register](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/upgrade/deprecated-features-platform) and [read-scale documentation](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/database-read-scale-out-overview). Those claims, universal query-first advice and unmeasured performance rules were not adopted. [Microsoft's roadmap-transition announcement](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/08/25/one-always-on-roadmap-dynamics-365-power-platform-and-dataverse-join-the-ai-at-work-roadmap/) supplies discovery context rather than proof of tenant availability.

Eight public Learn paths show 54 module placements (7/8/11/10/3/6/5/4). Overviews and all displayed module titles/descriptions were read; linked units were not. The old 50h07 subtotal is withdrawn because runtimes are absent. Some Dataverse, barcode and control-add-in material is adjacent to the objective list. The official course is now **Develop solutions with Dynamics 365 Business Central**, five days in English.

The MicrosoftLearning repository still has an INF99X sample-course README artifact; its root, README and MIT metadata were inspected, not individual labs or issues. AL-Go's README and template/scenario list were reviewed, not its full workflows or workshop. Indexed O'Reilly metadata identifies Dr. Gomathi S's November 2024 Apress book, 317 pages and a 3h48 reading estimate; direct fetch is blocked and no chapters were read.

The Plataan listing now shows October 13–14 and November 26–27, 2026. Its recommendation row was removed because its reference to real exam questions leaves the origin of its exercises unclear. This is a content-selection decision, not a finding that the provider misused exam material; no questions or sessions were accessed. Community-event, partner and assessment pages returned only shells. Other commercial catalogs were not comprehensively re-searched.

## Validation and follow-up

The actual local Python block was executed and exercised for same-ID replay, changed-content rejection, company separation and a new operation ID. SQLite verified the join fan-out and repaired aggregation. These checks are sequential and local; they do not provide durable or concurrent idempotency.

Repository, catalog, unit and strict-site gates are recorded after passing. Long product references were read in the sections identified in source notes, not every historical version, linked procedure or feature matrix. October 12 rechecks v29 and runtime documentation; March 15, 2027 revisits announced v30/PTE changes. The shared November 16 roadmap follow-up also applies. Live labs and independent human review remain outstanding.
