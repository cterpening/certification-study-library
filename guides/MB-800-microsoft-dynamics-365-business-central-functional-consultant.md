---
exam_code: MB-800
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-800
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# MB-800 Microsoft Dynamics 365 Business Central Functional Consultant Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Checked against the June 30, 2026 official objective baseline and cited public sources on September 1, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#mb-800-coverage-record). The [official MB-800 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-800) is authoritative.

**Current baseline:** Skills measured as of June 30, 2026.<br>
**Upcoming blueprint change:** None announced as of September 1, 2026.<br>
**Lifecycle:** The [Business Central Functional Consultant Associate credential](https://learn.microsoft.com/en-us/credentials/certifications/d365-business-central-functional-consultant-associate/) is active, renews every 12 months, and has no announced retirement. The exam is 100 minutes, is offered in eight languages, and has a free Practice Assessment.<br>
**Recent blueprint change:** The June 2026 update removed the standalone integration objective, added Copilot and agent setup, substantially revised core setup/basic operations, increased operations weighting, and added inventory transactions. Older courses remain useful only after this gap check.<br>
**Official source:** [MB-800 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-800)

## How to use this guide

Study each business process as a traceable control chain:

1. requirement, company and role;
2. master data and setup that drive behavior;
3. source document or journal and its state changes;
4. posting groups, dimensions, number series and approvals;
5. ledger entries and general-ledger impact;
6. exception, correction or reversal path;
7. report, reconciliation and audit evidence.

Use a disposable Business Central sandbox or trial. Repeat transactions from setup through posting and correction; screenshots alone do not prove that you understand the accounting and inventory effects.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Domain | Weight | Central question |
|---|---:|---|
| Set up Business Central | 20–25% | Can you create a governed company, migrate data, secure it, automate work and configure core behavior? |
| Configure financials | 30–35% | Can you turn accounting policy into accounts, posting groups, dimensions, journals, receivables, payables and assets? |
| Configure sales and purchasing | 10–15% | Can you configure item, customer, vendor, price, discount and location behavior correctly? |
| Perform Business Central operations | 30–35% | Can you execute, trace, reconcile, correct and explain everyday financial, trade, asset and inventory transactions? |

---

## 1. Set up Business Central

### Create a company and move data

Choose the company-creation option according to purpose: production-like setup, evaluation/demo data, or a clean company. Assisted Setup guides common tasks; it does not replace a signed configuration workbook. Record localization, base currency, fiscal year, posting ranges, number series, dimensions, taxes, inventory costing and opening-balance decisions before importing dependent records.

A configuration worksheet organizes tables and setup tasks. A configuration package selects fields, validates relationships, imports/export data and applies package records. Templates provide defaults for repeatable master-data creation. Sequence imports—setup and dimensions before customers/vendors/items, then opening entries—and reconcile counts, balances and rejected rows. A green import status is not financial acceptance.

Opening balances normally enter through journals so the system produces traceable entries. Decide cutover date, open versus historical transactions, customer/vendor/item detail, document application and control-account reconciliation. Rehearse, correct source data, reload, and obtain business sign-off.

> **Related item:** Migration establishes a starting state; master-data synchronization maintains selected facts afterward. A configuration package is not a permanent integration architecture.

### Manage users and security

Synchronize or create users as supported, then separate the concepts:

- a profile/role center shapes the workspace;
- a permission set grants object/data capabilities;
- a security group makes assignments manageable at scale;
- a security filter restricts which records an entitlement can reach;
- user setup can impose business constraints such as posting dates.

Start with standard permission sets, compose least-privilege access through groups, and add custom permission sets only for a documented gap. Test with the target user, not an administrator. Cover direct pages, Edit in Excel, reports, APIs and background jobs. Audit setup and sensitive record changes, protect audit access and define retention/review ownership.

> **Related item:** Personalization hides or rearranges controls; it never revokes permission. Profiles improve usability, while permission sets and filters enforce authorization.

### Configure core functionality

Number series provide controlled identifiers for master data, documents and journals. Define automatic/manual numbering, relationships, dates and collision behavior. Report selection and layouts determine which report runs and how output renders; distinguish Word, RDLC and Excel layouts, defaults, custom copies and per-customer/vendor requirements. Test data, localization, email/print output and upgrades.

Job queues schedule background tasks. Specify category, recurrence, earliest start, concurrency, retry, failure notification and owner. A job that is “ready” is not necessarily completing. Inspect entries and logs, reproduce failures and verify idempotency before rerunning.

Enable Copilot and built-in agent capabilities only after validating geography, licensing, privacy, permissions and business ownership. Treat AI suggestions as proposed actions: identify input/grounding, user confirmation, downstream record change, exception path and audit evidence. Do not grant broader permissions merely to make an agent work.

### Set up dimensions

Dimensions classify entries for management reporting without multiplying G/L accounts. Define stable dimension/value codes and ownership. Global dimensions are highly integrated and costly to change; shortcut dimensions simplify entry but do not change the underlying dimension-set model. Default dimensions on G/L accounts, customers, vendors, items and other master data can enforce values or block combinations.

Default-dimension priorities resolve competing defaults. Dimension combinations can block a complete pair or selected values. Test documents containing multiple sources because headers, lines and account types may contribute different defaults. Use the Dimension Correction Tool for supported posted-entry corrections with approval and audit evidence; it does not rewrite every operational fact or replace preventive validation.

### Manage approvals with workflows

A native workflow connects an event, conditions, responses and steps. Configure approval users, limits, substitutes/delegation, workflow user groups, notifications and escalation. Decide whether approval follows amount, dimension, responsibility center or another condition. Test submit, approve, reject, delegate, cancel, resubmit, overdue and unavailable-approver paths.

Power Automate can orchestrate adjacent cross-system work, but the native workflow should own the Business Central transaction state when that is the durable system rule. Monitor flow connections separately from Business Central workflow entries.

> **Related item:** A workflow controls a business-state transition; a job queue schedules background execution; a notification communicates an event. Combining them without distinct ownership makes failures hard to diagnose.

---

## 2. Configure financials

### Financial policy and chart of accounts

General Ledger Setup controls foundational accounting behavior such as local/reporting currency conventions, posting dates and other shared rules. Accounting periods define the fiscal calendar; permitted posting ranges exist at company and user levels. Payment terms calculate due dates/discounts, payment methods describe settlement behavior, and deferral templates spread revenue or expense according to a schedule. Currency setup requires codes, exchange rates, rounding and gain/loss accounts plus an update/revaluation process.

The chart of accounts should express statutory and management reporting without encoding every department or project as a separate account. G/L account type, direct-posting setting, posting restrictions and account category/subcategory all affect use and reporting. Financial reports combine row definitions/accounts/categories with column definitions, periods, dimensions and calculations. G/L allocations distribute amounts using fixed, percentage or variable bases; test rounding and reversal behavior.

> **Related item:** The chart of accounts classifies the economic nature of a posting; dimensions classify who, where, why or which initiative. Keeping these axes separate makes reporting more maintainable.

### Posting groups: predict the ledger before posting

Posting groups translate business context into G/L accounts. Specific posting groups classify entities or items—for example customer, vendor, bank and inventory posting groups. General business and product posting groups meet in General Posting Setup to choose sales, purchases, cost and related accounts. Inventory Posting Setup combines inventory posting group and location to select inventory accounts.

Multiple posting groups can support a master record that legitimately posts under more than one accounting treatment, but they increase user choice and control risk. For any document line, predict every account before posting: receivable/payable, revenue/purchase, inventory/interim, COGS, tax/VAT, discount and rounding as applicable. Then post and reconcile the actual G/L entries.

> **Related item:** Posting setup is a routing matrix. A correct source document with a wrong posting-group combination can still produce a balanced but economically wrong ledger.

### Journals and bank accounts

Journal templates define journal purpose/behavior; batches divide work, permissions and number series; lines hold the transactions. Recurring journals add recurrence method/frequency and allocation behavior. Configure bank cards, currency, posting group, account details and import/reconciliation capabilities. Separate preparation, approval and posting where the control model requires it.

Test balancing account versus separate balancing lines, dimensions, document/external document numbers, tax, currency and reversal. Preview posting when available. After posting, follow the register and entries rather than assuming that the journal page preserves the evidence.

### Payables and receivables

Vendor setup combines address, currency, language, payment terms/method, bank information, posting group and purchasing defaults. Purchases & Payables Setup controls shared document/number/posting behavior; payment journals propose and execute vendor settlements. Trace vendor → vendor ledger entry → detailed vendor ledger entry → G/L entry. The detailed entry explains applications, discounts, tolerances and currency effects that change remaining amounts.

Customer setup uses analogous sales, payment, shipping and receivables controls. Sales & Receivables Setup governs documents and posting. Cash receipt journals and Payment Registration capture receipts through different working experiences. Trace customer → customer ledger → detailed ledger → G/L, including partial application, unapplication, discount and tolerance.

Bank details and payment exports are sensitive. Apply least privilege, approval and change audit; validate files and bank responses rather than treating generation as payment completion.

### Fixed assets

Fixed Asset Setup, classes/subclasses, locations and posting groups define structure. Depreciation books hold accounting or tax treatments. A fixed asset may be a main asset with components, but component behavior and disposal/acquisition must be tested explicitly. Understand straight-line, declining-balance and other supported depreciation methods conceptually: basis, dates, conventions, residual value and posting integration determine results.

> **Related item:** A fixed-asset card identifies the asset; a depreciation book defines a valuation/depreciation view; the FA posting group routes transactions to G/L. One physical asset can require more than one accounting book.

---

## 3. Configure sales and purchasing

### Inventory and item structure

Inventory Setup establishes shared behavior. Item categories and attributes support classification/search; base and alternate units of measure require accurate conversions; variants distinguish versions of an item. Locations represent physical or logical inventory points. Stockkeeping units override planning and replenishment settings for an item/location/variant combination.

Know the entry chain: an item transaction creates item ledger entries for quantity, value entries for cost/value changes, and—through expected/actual cost posting and setup—G/L entries. Costing method changes how outbound cost is assigned; Standard, FIFO, Average, Specific and other supported behavior should be understood through transactions rather than definitions. Run and explain Adjust Cost–Item Entries and the relevant G/L posting process.

### Customer and vendor master data

Customer configuration includes ship-to addresses, location, shipping agent/service, lead time and sales defaults. Vendor configuration includes order addresses, location, lead time and purchasing defaults. Separate legal/pay-to or bill-to identity from operational ship-to/order addresses. Templates speed entry but need controlled ownership because defaults affect tax, currency, posting and fulfillment.

### Prices and discounts

Purchase and sales price logic selects among item/resource, vendor/customer or groups, currency, unit of measure, quantity and effective dates. Line discounts apply to eligible lines; invoice discounts use document totals and eligibility. Determine whether price, line discount and invoice discount can combine, and preview the result at boundaries such as quantity, date, currency and UOM.

Avoid memorizing screen positions. For each rule, state the eligible party/item, unit/currency, date range, quantity break, precedence and stacking behavior, then prove it on a quote/order.

> **Related item:** Pricing chooses a unit amount; a line discount changes a line; an invoice discount responds to eligible document total. They are separate calculations and may post differently.

---

## 4. Perform Business Central operations

### Navigate, personalize and analyze

Designing changes the application through development, customization changes a profile for users, and personalization changes one user's experience. Know who owns each layer and how to clear/disable it. Apply filters, filter panes and saved views deliberately; preserve context when opening related entries. Page inspection exposes page/table/extension details for diagnosis without granting permission to change them.

Edit in Excel publishes supported edits back through a connector; Open in Excel is export-oriented. Validate keys, allowed edits, permissions and error feedback. Data analysis mode groups, pivots and summarizes list data without requiring a separate report, but the selected fields, filters and company context still define meaning.

### Purchase and sales documents

A purchase quote can become an order. A purchase order supports receipt and invoice as separate quantities/states; over-receipt requires configuration and policy. Reverse a receipt only through supported correction behavior and understand downstream dependencies. Multiple receipts can be combined into one invoice. Blanket orders express longer-term agreement; recurring purchase lines provide reusable defaults; deferrals spread recognized value.

A sales quote can become an order or invoice. Before committing, inspect item availability and dates. Sales orders support shipment then invoicing; reverse shipments through the supported path. Combine shipments, use recurring lines, blanket orders, deferrals and prepayments only when their lifecycle fits the requirement.

For both directions, release freezes a document for downstream processing; reopen permits editing. Compare delete, cancel, credit memo, corrective credit memo and reversal according to whether the document is unposted, partly processed or fully posted. Preserve the audit chain rather than editing history.

### Financial documents, journals and payments

Process purchase/sales invoices and credit memos with correct application and reason. A posted correction must reverse both business and ledger effects. Prepayments create invoices/payments before final fulfillment and must be applied through the final document lifecycle.

Payment and cash-receipt journals post cash and apply entries. Payment Registration offers an invoice-centric receipt experience. Application connects an open payment/credit to invoices; unapplication restores open detailed-ledger effects without deleting history. Reverse posted journals only when supported and understand what dependent entries prevent reversal.

Bank reconciliation matches statement lines to bank-account ledger entries, explains differences and posts adjustments. A successful import is not reconciliation. Recurring journals and G/L allocations automate repeated/distributed postings but still need period, dimension, amount and reversal controls. Exchange-rate adjustment revalues open foreign-currency entries; distinguish realized and unrealized gains/losses. Dimension Correction changes supported posted dimensions under audit. G/L currency revaluation has different scope from customer/vendor/bank adjustments.

### Fixed-asset and inventory operations

Post fixed-asset acquisition, depreciation and disposal with the intended depreciation book, dates and integration. Reconcile FA ledger entries to G/L and explain gain/loss on disposal.

Inventory receipts and shipments adjust quantity outside normal sales/purchase flows when appropriate. Transfers move quantity between locations and may use in-transit state. Physical inventory counts compare expected and observed quantity; post only reviewed differences. Reclassification changes dimensions such as location/bin/variant without representing purchase or sale. Cost adjustment updates value assignment and can create later value/G/L postings.

> **Related item:** Quantity and value are related but not identical timelines. An item ledger entry carries quantity; value entries can arrive or adjust later, so operational availability can be correct while cost remains provisional.

---

## Integrated scenarios

### Scenario 1: controlled company migration

A new distribution company defines fiscal calendar, local currency, posting ranges, number series, account categories, dimensions and posting matrices before loading masters. Configuration packages load setup and records in dependency order; opening journals establish G/L, customer, vendor and item balances. Security groups separate setup, transaction and approval work. Reconciliation proves subledgers, inventory value and bank openings, while audit records and signed totals form cutover evidence.

### Scenario 2: order-to-cash with price and exception control

A customer, ship-to address, location, item/SKU, UOM, price and discount determine the quote. Approval handles a threshold exception. The quote becomes an order; availability informs the promised date; shipment and invoice occur separately. Posting creates item/value, customer/detailed-customer and G/L entries. A partial payment is registered/applied, a returned unit uses a credit path, and reports reconcile revenue, receivable, inventory and COGS.

### Scenario 3: procure-to-pay and close

A blanket purchase agreement provides planned quantity, while orders use vendor prices and over-receipt policy. Receipts and invoices are combined correctly, a deferral spreads a service charge, and the payment proposal uses approved bank information. Bank reconciliation verifies settlement. Period close includes recurring allocations, exchange adjustment, depreciation, inventory-cost adjustment and dimension/report review; job-queue failures are resolved before sign-off.

---

## Hands-on labs

1. **Company/cutover:** Create a company and configuration workbook/package; load representative masters and opening journals, deliberately fail one dependency, remediate and reconcile.
2. **Security/automation:** Create profiles, security-group/permission assignments, a filter, audit review, workflow approval and job queue; test with least privilege and forced failures.
3. **Dimensions/core:** Configure number series, layouts, global/shortcut/default dimensions, priorities and blocked combinations; correct one supported posted dimension with evidence.
4. **Financial setup:** Build a small chart, categories, G/L/general/specific/inventory posting matrices, currencies, deferral and journal structures; predict and verify postings.
5. **Receivables/payables/assets:** Create customer/vendor/bank/fixed asset; invoice, apply/unapply, reconcile, depreciate and dispose while tracing detailed ledgers to G/L.
6. **Trade setup:** Configure item/category/attributes/UOM/variant, locations/SKUs, customer/vendor defaults, price and three discount boundaries; test costing effects.
7. **Document lifecycles:** Run quote/order/receipt-or-shipment/invoice/prepayment/credit/correction for both purchase and sales, including blanket/recurring/combined documents.
8. **Inventory/close:** Transfer, count, reclassify, receive/ship and adjust cost; run currency, recurring allocation, reconciliation and close checks, then produce an evidence pack.

## Knowledge checks

1. When should you create a clean company rather than one with demo/setup data?
2. How do configuration worksheets, packages and templates differ?
3. What makes opening-balance migration financially accepted?
4. How do profile, permission set, security group and security filter differ?
5. Which non-page access paths must security testing cover?
6. How do number-series relationships support controlled alternatives?
7. What proves that a job queue is healthy rather than merely enabled?
8. Which controls should surround Copilot or agent-proposed actions?
9. Why are global dimensions more consequential than ordinary shortcut dimensions?
10. How do default-dimension priorities and blocked combinations interact?
11. When should native workflow own state rather than Power Automate?
12. How do chart-of-account structure and dimensions divide reporting responsibility?
13. What drives a deferral schedule and its postings?
14. How do general and specific posting groups combine?
15. Why can a balanced posting still be economically wrong?
16. How do journal template, batch and line differ?
17. What do detailed customer/vendor ledger entries explain?
18. Which controls protect vendor bank-detail changes?
19. How do depreciation book and FA posting group differ?
20. Trace an item transaction through item ledger, value and G/L entries.
21. How do costing methods change outbound cost behavior?
22. When is a SKU needed in addition to an item card?
23. How are prices, line discounts and invoice discounts selected?
24. Compare design, profile customization and personalization.
25. How do Edit in Excel and Open in Excel differ?
26. What evidence gives data-analysis-mode output meaning?
27. Why are receipt/shipment and invoice separate states?
28. When use a blanket order versus recurring lines?
29. How do release and reopen affect a document?
30. When use reversal, credit memo or corrective document?
31. How do application and unapplication preserve history?
32. What turns a bank-statement import into a reconciliation?
33. How do currency adjustment and G/L currency revaluation differ?
34. How do acquisition, depreciation and disposal affect FA/G/L entries?
35. Compare transfer, count and reclassification inventory journals.
36. Why can quantity be final while cost is still changing?

---

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one primary route, build one company from setup through close, and add a second resource only for a measured gap.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MB-800 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-800) | Free | 1–2 hours to map four domains and June change log |
| [Set up Business Central](https://learn.microsoft.com/en-us/training/paths/set-up-business-central/) | Free | 5 hours 42 minutes listed; 12–20 hours with setup/migration/security labs |
| [Configure financials](https://learn.microsoft.com/en-us/training/paths/configure-financials-business-central/) | Free | 11 hours 6 minutes listed; 25–40 hours with posting/reconciliation practice |
| [Configure sales and purchasing](https://learn.microsoft.com/en-us/training/paths/configure-sales-purchasing-business-central/) | Free | 6 hours 15 minutes listed; 12–20 hours with price/inventory setup |
| [Process sales and purchasing](https://learn.microsoft.com/en-us/training/paths/process-sales-purchasing-business-central/) | Free | 12 hours 49 minutes listed; 25–40 hours with full document lifecycles |
| [Process financial operations](https://learn.microsoft.com/en-us/training/paths/process-financial-operations-business-central/) | Free | 7 hours 48 minutes listed; 18–30 hours with close/correction/reconciliation |
| [MB-800T00-A course](https://learn.microsoft.com/en-us/training/courses/mb-800t00) | Paid/provider-dependent | 5 days |
| [MicrosoftLearning MB-800 labs](https://github.com/MicrosoftLearning/MB-800-Business-Central-Functional-Consultant) | Free; MIT | 15–30 hours selected; review open issues and current tenant/localization differences |
| [Free MB-800 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/d365-business-central-functional-consultant-associate/practice/assessment?assessment-type=practice&assessmentId=109&practice-assessment-type=certification) | Free | 45–90 minutes plus remediation |
| [Business Central documentation](https://learn.microsoft.com/en-us/dynamics365/business-central/) | Free | 20–50 hours selected implementation/reference reading |
| [O’Reilly: Business Central Essentials](https://www.oreilly.com/library/view/microsoft-dynamics-365/9798868822292/) | Subscription/trial | 2 hours 38 minutes; January 2026 broad primer with case study, not complete blueprint depth |
| [Udemy MB-800 by Dr. Gomathi Srinivasan](https://www.udemy.com/course/mb-800-dynamics-365-bc-functional-consultant-exam-training/) | Paid | 18 hours 43 minutes; updated February 2026, gap-check against June inventory/agent changes |
| [MeasureUp MB-800 practice test](https://www.measureup.com/microsoft-practice-test-mb-800-microsoft-dynamics-365-business-central-functional-consultant.html) | Paid; free demo | 2–5 hours; 132 questions, last updated January 2026, so map against June changes first |
| [Microsoft Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner login required | Use the five-day course pattern for planning; signed-in event start/end times control |

The five official paths total **43 hours 40 minutes** before labs. Allow roughly **100–170 hours** for a learner without current Business Central implementation experience to configure, transact, reconcile, correct and remediate. No exact current Pluralsight or Whizlabs MB-800 product was independently verified. Question-bank-only, recalled-content and guaranteed-pass listings were excluded.

## Final readiness checklist

- [ ] I can create, migrate, secure and audit a company and reconcile its opening state.
- [ ] I can configure number series, layouts, queues, dimensions, workflows and governed AI capabilities.
- [ ] I can predict postings from chart, journals and every relevant posting-group matrix.
- [ ] I can configure and trace receivables, payables, bank and fixed-asset entries to G/L.
- [ ] I can configure items, locations/SKUs, customers/vendors, prices and discounts.
- [ ] I can execute purchase/sales/prepayment/correction lifecycles and explain every state.
- [ ] I can reconcile journals, payments, bank, currency, fixed assets, inventory quantity/cost and close evidence.
- [ ] I rechecked the official blueprint, lifecycle, languages, assessment and June 2026 changes before scheduling.

## Source notes

The June 30, 2026 study guide defines exam scope. Microsoft Learn, product documentation and public course labs support behavior but may include adjacent features or localization-dependent steps. Commercial sources are optional supplements and never define the objective contract. All scenarios, labs and checks here are original; no dumps or recalled questions were used.
