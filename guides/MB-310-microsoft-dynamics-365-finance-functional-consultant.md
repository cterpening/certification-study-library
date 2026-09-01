---
exam_code: MB-310
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-310
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# MB-310 Microsoft Dynamics 365 Finance Functional Consultant Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide was checked against the August 14, 2026 official objective baseline and cited public sources on September 1, 2026. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#mb-310-coverage-record). The [official MB-310 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-310) is authoritative.

**Current baseline:** Skills measured as of August 14, 2026.<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 1, 2026.<br>
**Lifecycle:** The [Dynamics 365 Finance Functional Consultant Associate credential](https://learn.microsoft.com/en-us/credentials/certifications/d365-functional-consultant-financials/) is active. The exam is 100 minutes, available in English and Japanese, has no announced retirement date, and offers a free Practice Assessment.<br>
**Scope change:** The August baseline removes cost management, substantially revises financial management, receivables, subscription billing, payables and fixed-asset transactions, and adds budget planning. Do not use an older course or practice test as the objective checklist.<br>
**Official source:** [MB-310 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-310)

## How to use this guide

Study Finance as connected accounting flows, not isolated setup pages. For each scenario, trace:

1. source document or journal and responsible persona;
2. master data, dimensions, currency, tax and posting-profile defaults;
3. validation, matching, approval, credit or budget control;
4. subledger entry, voucher, general-ledger accounts and posting layer;
5. settlement, revaluation, recognition, depreciation or close;
6. financial reporting, reconciliation and audit evidence;
7. correction, reversal and recovery from partial failure.

Use a nonproduction legal entity with synthetic customers, vendors and bank data. Record parameters, posting profiles, workflows, roles and batch jobs with the transactions they influence. The exam measures configuration and business outcomes; memorizing navigation is brittle.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Implement financial management | 35–40% | Can you design a controlled accounting foundation and operate journals, bank, close and tax processes? |
| Implement accounts receivable, credit, collections, and subscription billing | 15–20% | Can you control order-to-cash, customer risk, collection and recurring recognition? |
| Implement and manage accounts payable and expenses | 10–15% | Can you validate liabilities, execute payments and govern employee expense? |
| Implement budgeting | 10–15% | Can you distinguish budget entries, control and collaborative planning and configure each correctly? |
| Manage fixed assets | 10–15% | Can you configure books and depreciation and trace an asset through acquisition, transfer and disposal? |

---

## 1. Implement financial management

### Design the accounting foundation

The **chart of accounts** defines main accounts; financial dimensions add business-analysis segments such as department, cost center or region. Main-account categories support reporting and analysis, ledger-account aliases speed entry, and balance-control accounts can enforce a debit or credit balance expectation. Legal-entity overrides let a shared definition behave appropriately in a particular company.

An **account structure** defines valid combinations and required dimensions for a range of main accounts. An **advanced rule structure** adds dimensions only when a condition makes them relevant. Design from reporting and control requirements: forcing every dimension on every account creates unusable journals, while permissive structures produce postings that cannot be reconciled. Test valid, missing and invalid combinations as well as changes to an in-use structure.

Dimension default templates provide reusable defaults; derived dimensions calculate one dimension from another according to configured rules. Understand defaulting precedence across source documents, master records, headers, lines and account structures. A default is not proof that the accounting is correct. **Financial tags** add user-defined tracking values without expanding the financial-dimension structure; use them where the reporting and control requirement fits their behavior.

> **Related item:** Dimensions form part of a ledger account and are validated by account structures. Financial tags are supplemental transaction metadata. Choose by posting, validation, reporting and maintenance requirements rather than treating them as interchangeable labels.

### Configure ledgers, fiscal time and currency

The ledger ties a legal entity to its chart of accounts, fiscal calendar, accounting currency, reporting currency and balancing dimensions. Fiscal calendars define years and periods; opening or closing a period controls when modules and user groups can post. **Posting layers** separate current, operations, tax or custom reporting effects without creating another legal entity.

Currency design includes currencies, exchange-rate types and dated exchange rates. A transaction currency is translated into accounting currency and, when configured, reporting currency. Revaluation recognizes unrealized currency changes on open balances or ledger accounts; settlement or payment realizes the difference. Configure posting profiles/accounts and dates deliberately, then reconcile the revaluation voucher to the selected population.

Ledger allocation rules redistribute balances by fixed percentage, basis or supported allocation method. Define source, destination, basis, offset, schedule and traceability. An allocation should preserve totals and produce explainable dimensions. Intercompany accounting creates balanced due-to/due-from entries across legal entities; validate both companies, exchange rates, dimensions and period status.

### Implement controlled journals

A journal name carries defaults and controls such as journal type, voucher numbering and workflow. Voucher-number policy affects auditability: understand when numbering occurs, whether lines share a voucher and how continuous numbering behaves. Posting restriction rules and journal controls constrain who may post which accounts or dimensions. Periodic journals support recurring patterns; reversal configuration creates an intentional opposite entry at the chosen date.

For manual and Excel-assisted journals, trace template → draft/import → validation → workflow if used → posting → voucher → ledger inquiry. Excel improves volume entry but does not bypass account structures, permissions or validation. Batch posting improves throughput; it adds scheduling, contention, retry and monitoring responsibilities. A safe correction preserves audit history through reversal or supported correction rather than deleting evidence.

### Manage cash, banks and payments

Bank groups organize institutions; bank accounts hold currency, account identifiers, reconciliation, posting and payment settings. Payment methods define how customer or vendor payments are processed, while payment-format configuration produces or imports the bank-specific message. Protect account changes and payment-file generation with segregation of duties, workflow and out-of-band verification.

Manual reconciliation matches statement lines and Finance transactions directly. **Advanced bank reconciliation** imports statements, normalizes transaction codes and applies matching rules before exceptions are reviewed. Test one-to-one, one-to-many, fees, interest, duplicates, missing transactions and statement corrections. Bank foreign-currency revaluation updates eligible balances and posts the difference to configured accounts.

Cash-flow forecasting combines configured liquidity accounts, transaction sources and forecast rules into time-based projections. Automation can refresh forecasts, but completeness and timing assumptions still need review. Shared payment setup centralizes eligible payment activity across legal entities. Customer/vendor netting settles compatible receivable and payable amounts; preserve approvals, counterparty agreement and residual balances.

> **Related item:** Payment proposal selects obligations, payment journal authorizes accounting, payment format communicates with the bank, and reconciliation proves what cleared. These are distinct controls in one cash process.

### Perform close, consolidation and tax work

A financial close should be a scheduled, owned set of tasks with dependencies and evidence. Configure financial-period workspaces and close schedules; control period access by module and group. Reconcile subledgers to the general ledger before closing, run necessary accruals/revaluations/allocations, and use closing or year-end templates where supported. Ledger settlement matches related ledger transactions; it is not a substitute for correcting an erroneous voucher.

Consolidation combines legal entities under consistent account, currency and period rules; elimination removes intercompany effects. Decide between the supported online consolidation pattern and another reporting/consolidation architecture based on ownership, adjustments, translation, audit and scale. Validate that eliminations remove only reciprocal balances and that late subsidiaries and ownership changes have a defined process.

Sales-tax configuration connects sales tax codes, groups, item groups, settlement periods and authorities with posting groups. The intersection of party group, item group, jurisdiction and transaction determines tax behavior. Test taxable, exempt, reverse/adjusted and cross-border cases appropriate to the configuration. Settlement calculates the period liability and posts to authority accounts. Withholding tax has its own groups, codes and authorities; distinguish it from sales tax.

> **Related item:** Financial reporting consumes ledger and dimension structures but is not a repair layer. If a report needs extensive overrides to reconcile, investigate posting, dimensions, currency and close first.

---

## 2. Implement receivables, credit, collections, and subscription billing

### Run order-to-cash with explainable posting

Customer groups provide shared defaults; shared customers support cross-company use where configured. Posting profiles map customer transactions to summary and offset accounts. Payment methods, bank accounts and charges affect collection and settlement. For each free-text invoice, recurring invoice, sales-order invoice, credit memo, prepayment and intercompany invoice, explain the document state, tax, dimensions, due date, voucher, open transaction and settlement.

Customer payments may be entered/imported and settled against invoices; overpayments, underpayments, discounts and write-offs need explicit accounts and authority. Accounts-receivable foreign-currency revaluation adjusts eligible open balances. Billing classifications can separate supported invoice populations and processing. Protect customer bank details and changes to payment instructions as sensitive financial master data.

### Control credit and collections

Credit management combines limits, risk attributes, rules, holds and release authority. A sales order placed on credit hold needs a visible reason, reviewer and outcome; overriding a control must leave evidence. Aging-period definitions group open balances by due date, and aged-balance inquiries show exposure. They inform collection action but do not determine customer intent by themselves.

Collections use pools, activities and work queues to prioritize contact and resolution. Interest notes and collection letters apply configured policies; write-offs remove approved uncollectible balances to the proper account. Design for disputes, promises to pay, partial settlements, legal restrictions and vulnerable customers. Measure recovered value, dispute resolution and aged exposure, not just contact volume.

### Configure subscription billing and deferrals

A billing schedule defines recurring or milestone-based customer billing. Contract billing groups, item groups, frequency, dates, pricing, escalation and milestones determine generated sales documents. Holds and termination change future processing; preserve the commercial reason and effective date. Test mid-period starts, price updates, renewal, usage/milestone completion, cancellation and credit.

Revenue and expense deferrals separate invoice/posting timing from recognition timing. Configure deferral defaults and the items deferred by default, then generate recognition schedules. Charges may also be deferred. A schedule needs start/end convention, period allocation, account mapping and treatment for modification or termination. Reconcile source document → deferral schedule → periodic recognition entries → remaining balance.

> **Related item:** Subscription billing creates and manages recurring commercial documents; deferral controls when revenue or expense is recognized. A recurring invoice does not automatically prove compliance with an accounting recognition policy.

---

## 3. Implement payables and expenses

### Control procure-to-pay

Vendor groups, shared vendors, posting profiles, payment methods, charges and bank accounts supply defaults and accounting behavior. A vendor invoice may originate from a purchase order, invoice journal, recurring invoice, prepayment or intercompany flow. Trace each to liability, tax/charges, expense or inventory, due date, open transaction and settlement.

Invoice validation checks required data and policy. Invoice matching compares invoice price/quantity with purchase order and product receipt according to two-way or three-way rules and tolerance. A discrepancy needs workflow, documented approval or correction; changing tolerance merely to make an invoice pass weakens the control. Vendor invoice journals support invoices not tied to a PO but still require dimensions, tax, approval and duplicate controls.

Payment proposals select due items by criteria; payment journals make the accounting/payment set reviewable before file generation or posting. Centralized payments process eligible obligations across companies. Prepayments must later be applied to the correct invoice. Accounts-payable foreign-currency revaluation adjusts eligible open vendor balances. Secure vendor bank changes and separate vendor maintenance, invoice approval and payment release.

### Govern employee expenses

Expense categories connect business meaning, account, tax and policy. Configure per diem, mileage, intercompany expenses and treatment of personal spend according to the organization’s rules. Expense reports collect lines, receipts, project or dimension context and attestation; policies can warn or block based on amount, category, age or other supported conditions.

Test missing receipts, mixed currency, partial personal spend, delegate entry, policy exception, rejected/returned report and cross-company/project allocation. The final voucher should be reconcilable to the approved report, while sensitive receipt and personal information remains appropriately secured.

> **Related item:** Project Operations expense modules appear in the official MB-310T00 course syllabus, but the exam objective is the Finance expense process. Use adjacent course modules to understand integration boundaries, then map every study claim back to the current blueprint.

---

## 4. Implement budgeting

### Separate three budgeting capabilities

**Basic budgeting** records budget register entries against a budget model and code. Models organize versions; codes describe entry types and can control workflow. Allocation terms and transfer rules support distribution and controlled movement. Compare budget to actual at the same account/dimension and period grain.

**Budget control** checks funds availability on configured source documents and journals. Configure parameters, dimensions, rules, groups, calculation and over-budget permission. Test reservation/encumbrance behavior where relevant, thresholds, amendments, transfers, year boundaries, workflow and users allowed to exceed. A green check depends on the selected calculation and scope; it is not an unlimited-funds statement.

**Budget planning** is a collaborative proposal and approval process. Configure planning organization hierarchy, process, stages, scenarios, workflows, layouts/templates and allocations. Scenarios distinguish values such as prior actual, baseline, request and approved budget; stages define who acts when. Test promotion between stages, rejected/returned plans, allocation recalculation and transfer of the approved plan to budget entries.

> **Related item:** Basic budgeting stores approved amounts, budget control enforces availability, and budget planning develops proposals. They can integrate, but each solves a different governance problem.

---

## 5. Manage fixed assets

### Configure books and depreciation

Fixed-asset groups provide shared defaults and numbering; assets hold individual identity and attributes. A **book** represents a valuation/depreciation basis, such as corporate or tax, with acquisition, depreciation and disposal behavior. Derived books can create related transactions in another book. Posting profiles map asset transaction types to ledger accounts.

Configure service life, depreciation profile/convention, depreciation periods and supported methods. Map groups/assets to books deliberately. Before running depreciation, validate placed-in-service date, acquisition basis, residual value, remaining life and prior postings. A proposal selects expected transactions; review before posting and reconcile accumulated depreciation and net book value.

### Process the asset lifecycle

Assets can be acquired through a purchase order, fixed-asset journal, inventory or project process depending on the requirement. Trace source cost, capitalization date, dimensions and voucher into the correct asset/book. Fixed-asset budgets can feed budgeting; budget is authorization/planning, not an acquisition transaction.

Use journals or supported source documents to split, reclassify or transfer assets while preserving history and correct company/dimension/book balances. Disposal by sale can use a free-text invoice; disposal by scrap has no customer proceeds. Both must remove cost and accumulated depreciation and recognize the resulting gain or loss. Run depreciation across companies only with deliberate batch scope, security and monitoring.

> **Related item:** Asset leasing is relevant Finance knowledge and may affect accounting, but it is not an explicit domain in the August 14, 2026 MB-310 objectives. Cost management was removed from this baseline. Do not spend current exam-prep time on either until core gaps are closed.

---

## Integrated scenarios

### Scenario 1: multi-company month end

A group uses one chart of accounts with legal-entity overrides, account structures and reporting currency. During close, teams reconcile AR/AP and banks, post accruals and allocations, revalue open currency and ledger balances, settle related ledger entries, consolidate subsidiaries and post controlled eliminations. The close workspace records dependencies and evidence; a late subsidiary follows a documented reopen/adjust/reconsolidate path.

### Scenario 2: subscription customer under credit pressure

A customer has recurring and milestone schedules plus deferred revenue. Aging and risk rules place a new order on hold. Collections records the dispute and promise to pay; an authorized reviewer releases only the supported order. A later price change affects future billing, termination stops the schedule at the approved date, and recognition entries reconcile to the remaining deferral balance.

### Scenario 3: capital purchase under budget control

A department budget is developed through planning, approved into a budget model and enforced by budget control. A PO for equipment passes funds availability; product receipt and three-way-matched invoice establish the liability and acquisition flow. The asset/book is placed in service, depreciated, transferred to another cost center, then sold through a free-text invoice with gain/loss reconciled to the ledger.

---

## Hands-on labs

1. **Ledger design:** Build a COA/dimension/account-structure matrix with an advanced rule, defaults, a derived dimension and a financial-tag use case; test six valid/invalid entries.
2. **Journal and currency:** Configure a journal name, voucher policy, posting restriction, reversal and Excel template; post foreign-currency entries, revalue and reconcile the vouchers.
3. **Bank and close:** Configure/import a statement and matching rules; resolve exceptions, build a close schedule, allocate a balance and storyboard consolidation/elimination.
4. **Tax and receivables:** Configure a small tax intersection and posting profiles; create invoices, credit/prepayment/payment, revaluation and settlement, then inspect ledger effects.
5. **Credit and subscription:** Model risk/hold/release and collections activity; create a billing schedule and revenue/expense deferral with modification and termination cases.
6. **Payables and expenses:** Process PO and non-PO invoices, matching discrepancy, proposal/payment, prepayment and an expense report with policy exception.
7. **Budgeting:** Configure basic budget entry, transfer, funds-availability control and a planning process with hierarchy, stages, scenarios and allocation.
8. **Fixed assets:** Configure a group, two books and depreciation; acquire, split/transfer, run multi-period depreciation and dispose by sale or scrap with reconciliation.

## Knowledge checks

1. When should a requirement become a financial dimension rather than a financial tag?
2. How do account structures and advanced rules divide validation work?
3. Which sources and precedence can supply a default dimension?
4. Distinguish accounting, reporting and transaction currency.
5. What produces unrealized versus realized exchange differences?
6. When is a posting layer preferable to another legal entity?
7. Which journal-name and voucher controls support auditability?
8. Why does Excel entry not bypass journal validation?
9. What failure evidence must batch posting retain?
10. Distinguish bank statement import, matching, reconciliation and ledger posting.
11. How do payment proposal, journal, format and bank confirmation relate?
12. Which assumptions make cash-flow forecasts misleading?
13. What sequence makes a close repeatable and auditable?
14. Why reconcile subledgers before consolidation?
15. What does an elimination remove, and what should it preserve?
16. How do tax code, group, item group, period, authority and posting group interact?
17. How does a posting profile connect a customer/vendor transaction to the ledger?
18. What evidence supports a credit-hold release?
19. What is the difference between aging and a collections process?
20. How should a write-off remain authorized and traceable?
21. Distinguish recurring invoice and subscription billing schedule.
22. How does deferral separate billing from recognition?
23. What happens to recognition after a contract modification or termination?
24. Compare two-way and three-way invoice matching.
25. Why are vendor bank changes a high-risk control point?
26. How do centralized payments affect company and settlement boundaries?
27. Which expense-policy failures need a supported exception path?
28. Distinguish budget model, code, register entry and transfer rule.
29. Which calculation and scope choices control funds availability?
30. How do planning hierarchy, process, stage and scenario differ?
31. Distinguish asset, group, book and derived book.
32. How do depreciation profile and convention affect timing?
33. Which acquisition routes connect assets to source documents?
34. How should a transfer differ from a reclassification or split?
35. Which accounts change on disposal by sale versus scrap?
36. Which removed or adjacent topics should not displace August 2026 objectives?

---

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one primary route, build several source-document-to-ledger journeys, and add another resource only for a measured gap.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MB-310 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-310) | Free | 1–2 hours to map objectives and the August change log |
| [Configure financial management](https://learn.microsoft.com/en-us/training/paths/set-up-configure-financial-management-work-general-ledger/) | Free | 20 hours 23 minutes listed; 35–55 hours with transactions/reconciliation |
| [Manage accounts receivable](https://learn.microsoft.com/en-us/training/paths/implement-accounts-receivable-credit-collections-revenue-recognition/) | Free | 10 hours 12 minutes listed; select around removed cost-management material and allow 18–28 hours with practice |
| [Manage accounts payable](https://learn.microsoft.com/en-us/training/paths/implement-manage-accounts-payable-expenses/) | Free | 9 hours 56 minutes listed; 16–24 hours with matching/payment/expense practice |
| [Perform budgeting and forecasting](https://learn.microsoft.com/en-us/training/paths/manage-budgeting/) | Free | 3 hours 3 minutes listed; 8–12 hours with all three budgeting capabilities |
| [Administer fixed assets](https://learn.microsoft.com/en-us/training/paths/manage-fixed-assets/) | Free | 4 hours 56 minutes listed; 10–16 hours with lifecycle transactions |
| [MB-310T00-A course](https://learn.microsoft.com/en-us/training/courses/mb-310t00) | Paid/provider-dependent | 4 days |
| [Official MicrosoftLearning MB-310 labs](https://github.com/MicrosoftLearning/MB-310-Microsoft-Dynamics-365-Finance) | Free; MicrosoftLearning license applies | 10–20 hours selected labs; verify each lab against the current blueprint and tenant UI |
| [Free MB-310 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/d365-functional-consultant-financials/practice/assessment?assessment-type=practice&assessmentId=107&practice-assessment-type=certification) | Free | 45–90 minutes plus review |
| [Dynamics 365 Finance documentation](https://learn.microsoft.com/en-us/dynamics365/finance/) | Free | 15–35 hours selected implementation and troubleshooting references |
| [Pluralsight: Microsoft Dynamics 365 path](https://www.pluralsight.com/paths/microsoft-dynamics-365) | Subscription/trial | 4 hours listed; broad product primer, not current MB-310 coverage |
| [Udemy: Dynamics 365 Finance & Operations—Financials Part 1](https://www.udemy.com/course/d365-financeoperations-overview-and-financials-part-1/) | Paid | 4 hours 8 minutes; updated November 2024, useful for durable GL basics only |
| [MeasureUp MB-310 practice test](https://www.measureup.com/microsoft-practice-test-mb-310-microsoft-dynamics-365-finance.html) | Paid; free demo | 2–4 hours across diagnostic attempts and review; last updated February 2023 and includes objectives removed in 2026 |
| [Microsoft Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner login required | Use the four-day official-course pattern for planning; verify the signed-in event’s exact start/end time |

The five selected official paths total **48 hours 30 minutes** before labs. They mirror the current course syllabus but contain some adjacent/removed material, so select deliberately. Allow roughly **100–160 hours** for a new Finance practitioner to complete a primary route, build the labs and remediate the Practice Assessment. No exact current O’Reilly or Whizlabs MB-310 product was independently verified on September 1, 2026. Reject recalled live content, “valid questions,” pass guarantees and any practice source that cannot explain its authorship and update baseline.

## Final readiness checklist

- [ ] I can trace a source document or journal through defaults, validation, subledger, voucher, ledger, settlement and reporting.
- [ ] I can design COA/dimensions/account structures/tags without confusing reporting metadata and posting control.
- [ ] I can configure journals, currencies, revaluation, bank reconciliation, payments, close, consolidation and tax with failure/recovery evidence.
- [ ] I can operate receivables, credit, collections, subscription billing and deferral as connected but distinct controls.
- [ ] I can configure payables, invoice matching, payments, prepayments and expenses with segregation of duties.
- [ ] I can distinguish basic budgeting, budget control and budget planning and build one complete flow through each.
- [ ] I can configure asset groups/books/depreciation and reconcile acquisition, transfer, split and disposal.
- [ ] I completed scenarios and labs in a nonproduction environment and recorded expected vouchers and exceptions.
- [ ] I used older commercial material only after gap-checking it against the August 14, 2026 blueprint.
- [ ] I rechecked the official study guide, lifecycle and Practice Assessment before scheduling.

## Source notes

The August 14, 2026 official study guide is the objective authority. Microsoft Learn paths and product documentation support behavior but can include adjacent topics. MicrosoftLearning labs are linked for independent hands-on use under their repository terms, not copied here. Commercial resources are optional perspectives and were not treated as objective authority. All questions in this guide are original and conceptual; no exam dumps or recalled items were used.
