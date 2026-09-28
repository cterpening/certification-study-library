# MB-800 deep review — September 28, 2026

The entire guide was reviewed against 123 detailed objectives across 22 groups. Seven worked examples, ten proposed labs and 48 original answered checks now connect setup to document state, ledger effects and exception handling. All 34 local calculation assertions passed. No tenant transactions, agent activation, email, payment, paid-content or assessment execution occurred; independent human review remains pending.

## Objective and lifecycle evidence

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-800) retains the June 30, 2026 baseline with no newer announcement. The credential lists 100 minutes, eight languages and annual renewal, with no retirement displayed. The previous snapshot condensed the same scope into 22 bullets. Its September 1 bytes and historical references are preserved before accepting the canonical 123-objective extraction; this is restoration of detail, not a newly announced exam expansion.

The receipt `ADLC_Docs/operations/2026-09-28-mb-800-deep-review.json` records objective-to-section mappings, source fetches, article decisions, previous records, calculation boundaries and completed validation gates.

## Corrections and learning additions

- Combined security-filter permissions are least restrictive. A narrow permission set does not revoke a broader grant; the guide adds an assignment-union example and negative tests.
- Inventory Account (Interim) belongs to Inventory Posting Setup; Invt. Accrual Acc. (Interim) belongs to General Posting Setup. Adjustment, actual G/L posting and expected-cost posting are separate controls. The original FIFO example reconciles 550 of final cost into 220 COGS and 330 remaining inventory.
- Invoice correction depends on payment, shipment and source-document state. Paid sales require a credit/return path; combined purchase receipts also affect correction eligibility. Quantity tolerance does not resolve an over-receipt's invoice agreement.
- G/L dimension correction does not rewrite subledger dimensions. G/L currency revaluation is for eligible directly maintained source-currency balances, not duplicate revaluation of customer/vendor/bank control balances. Period closing is irreversible but does not replace posting-date controls.
- Bank reconciliation distinguishes timing differences from a missing fee. Discounts, deferrals, allocations and exchange-rate examples provide explicit assumptions and expected totals.
- Current Payables setup controls take precedence over an older preview sentence in its overview. Sender policies depend on email-review settings and subfolder configuration; authenticated internal senders have additional setup rules. Draft finalization, vendor approval and invoice posting remain distinct.
- Production-only Payables trial processing automatically becomes billable after 50 invoices. Credit exhaustion can pause processing while the task remains active, with backlog resumption later. The labs do not treat this trial as free sandbox infrastructure.
- Sales Order Agent starts with a quote, which does not reserve inventory. Forwarded email uses the forwarder's address for contact lookup. Queue On Hold prevents a future start rather than canceling a running task. Bank Copilot's preview status and proposal-review boundary remain explicit.

## Blog decisions

[Sumit Singh's inventory setup tutorial](https://community.dynamics.com/blogs/post/?postid=7989aea7-627b-f011-b4cc-7c1e5248819c) was read in full and accepted only for reconciliation prompts. Its interim-account placement conflicts with [Microsoft's expected-cost setup](https://learn.microsoft.com/en-us/dynamics365/business-central/design-details-expected-cost-posting). The inaccurate account mapping and generic defaults were rejected. It is independently authored community material, not a Microsoft endorsement; its publication date was not established.

[Mike Morton's April 3, 2025 Sales Order Agent introduction](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2025/04/03/sales-order-agent-in-microsoft-dynamics-365-business-central-now-in-public-preview/) supports a request/review/document-state worksheet. Preview status and defaults are historical; current product setup governs the exercise. The embedded video was not watched. [Richard Riley's August roadmap-transition announcement](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/08/25/one-always-on-roadmap-dynamics-365-power-platform-and-dataverse-join-the-ai-at-work-roadmap/) informs release discovery and the planned November 15 retirement follow-up. It does not establish that a roadmap feature is deployed in a tenant.

## Catalog and reading boundaries

The five Learn paths expose 48 module placements, respectively 5/15/7/12/9. Their complete public overviews and module descriptions were read; linked units were not. Current pages do not expose runtime, so the older 43h40 total is withdrawn. Some asset-budget and integration material is adjacent to the exam's detailed bullets. The official course is now titled **Manage business solutions with Microsoft Dynamics 365 Business Central**, five days in English. The public lab repository's root, README and license were inspected; individual labs, open issues and release history were not audited.

Public indexed O'Reilly metadata identifies Dr. Gomathi S's January 2026 Apress book, 186 pages, with a 2h38 platform reading estimate. This is not a video runtime. Public indexed Udemy metadata retains Dr. Gomathi Srinivasan, February 2026, 14 sections, 36 lectures and 18h43. Both direct fetches were blocked; indexed observations are separately recorded. MeasureUp lists 132 questions and January 2026, requiring a gap check against June scope. No paid lessons, chapters or practice questions were accessed. Partner/assessment shells did not expose substantive content; Pluralsight and Whizlabs were not comprehensively searched again.

Long product references were read in the sections identified in source notes, not every linked procedure or localization/permission/version matrix. Local calculations use simplified assumptions and do not establish platform accounting, concurrency, security or AI accuracy.

## Follow-up

October 26 revisits agent setup and overview consistency, sender policies, trial/credit behavior, bank Copilot status and catalog drift. November 16 rechecks the planned release-roadmap transition. Repository, catalog, unit and strict-site checks are recorded in the receipt after they pass. Live labs and independent human review remain outstanding.
