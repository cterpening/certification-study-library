---
exam_code: MB-800
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-800
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# MB-800 Microsoft Dynamics 365 Business Central Functional Consultant Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Checked against the June 30, 2026 official objective baseline and cited public sources on September 28, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#mb-800-coverage-record). The [official MB-800 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-800) is authoritative.

**Current baseline:** Skills measured as of June 30, 2026.<br>
**Upcoming blueprint change:** None announced as of September 28, 2026.<br>
**Lifecycle:** The [Business Central Functional Consultant Associate credential](https://learn.microsoft.com/en-us/credentials/certifications/d365-business-central-functional-consultant-associate/) is active, renews every 12 months, and has no announced retirement. The exam is 100 minutes, is offered in eight languages, and has a free Practice Assessment.<br>
**Recent blueprint change:** The June 2026 update removed the standalone integration objective, added Copilot and agent setup, substantially revised core setup/basic operations, increased operations weighting, and added inventory transactions. Older courses remain useful only after this gap check.<br>
**Official source:** [MB-800 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-800)

The [September deep-review report](../docs/research/2026-09-28-mb-800-deep-review.md) maps all **123 detailed objectives**, explains source corrections and records the limits of this review. The June baseline is unchanged; the older condensed snapshot has been archived.

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

**Check combined permissions.** For multiple permission sets granting access to the same table, Business Central uses the least restrictive security filter. Adding a filtered permission set does not narrow another broader grant. Test every applicable assignment in the intended company, including unfiltered grants. Security filters do not support `*` or `?` wildcards; supported expressions and length limits differ from an ordinary page filter. See [security-filter behavior](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/security/security-filters) and worked example 1.

### Configure core functionality

Number series provide controlled identifiers for master data, documents and journals. Define automatic/manual numbering, relationships, dates and collision behavior. Report selection and layouts determine which report runs and how output renders; distinguish Word, RDLC and Excel layouts, defaults, custom copies and per-customer/vendor requirements. Test data, localization, email/print output and upgrades.

Job queues schedule background tasks. Specify category, recurrence, earliest start, concurrency, retry, failure notification and owner. A job that is “ready” is not necessarily completing. Inspect entries and logs, reproduce failures and verify idempotency before rerunning.

Enable Copilot and built-in agent capabilities only after validating geography, licensing, privacy, permissions and business ownership. Treat AI suggestions as proposed actions: identify input/grounding, user confirmation, downstream record change, exception path and audit evidence. Do not grant broader permissions merely to make an agent work.

**Queue states need evidence.** Earliest Start Date/Time is scheduling eligibility, not a completion guarantee. Entries in one category can wait for the running entry. Putting an entry On Hold prevents a future start; it does not stop a run already in progress. Inspect log entries and the affected documents before retrying. See [job-queue scheduling and states](https://learn.microsoft.com/en-us/dynamics365/business-central/admin-job-queues-schedule-tasks).

**Agent setup changes the control boundary.** Current [Payables Agent setup](https://learn.microsoft.com/en-us/dynamics365/business-central/payables-agent-setup) lists the capability as generally available; an older preview sentence in the overview is not the current activation guide. Availability still depends on the supported country/region, language, permissions and environment billing. Its production-only trial automatically becomes billable processing after 50 invoices; do not assume a sandbox exercise is covered by that trial. Credit exhaustion pauses invoice processing while the scheduled task can remain active, and replenishment can resume a backlog.

Separate email review, draft review, vendor approval and posting. Finalizing a purchase draft creates an unposted purchase invoice. An agent-created vendor starts blocked; the agent does not provide vendor-approval workflows. The [Payables Agent overview](https://learn.microsoft.com/en-us/dynamics365/business-central/payables-agent) documents PDF and daily-processing limits—include malformed attachments and exceptions in acceptance tests.

[Known-sender policies](https://learn.microsoft.com/en-us/dynamics365/business-central/payables-agent-known-senders) apply when email review is Manage per sender and no monitored subfolder is configured. Always/Never settings override sender policy; a monitored subfolder bypasses these email-review controls. Do not interpret Approve as permission to post every invoice. Test authenticated internal senders separately using the setup document's rules, and treat mailbox folder routing as a business control.

The [Sales Order Agent](https://learn.microsoft.com/en-us/dynamics365/business-central/sales-order-agent) creates a quote first even when configured to proceed directly to an order. A quote does not reserve stock. Sender email identifies the contact; a forwarded message is matched using the forwarder's address, so a name in the body is insufficient. Use the supported one-time contact association for a forwarded request after verifying it. Review outgoing communications and the task timeline through [agent supervision](https://learn.microsoft.com/en-us/dynamics365/business-central/supervise-agent-tasks); document creation is not shipment, invoicing or cash settlement.

### Set up dimensions

Dimensions classify entries for management reporting without multiplying G/L accounts. Define stable dimension/value codes and ownership. Global dimensions are highly integrated and costly to change; shortcut dimensions simplify entry but do not change the underlying dimension-set model. Default dimensions on G/L accounts, customers, vendors, items and other master data can enforce values or block combinations.

Default-dimension priorities resolve competing defaults. Dimension combinations can block a complete pair or selected values. Test documents containing multiple sources because headers, lines and account types may contribute different defaults. Use the Dimension Correction Tool for supported posted-entry corrections with approval and audit evidence; it does not rewrite every operational fact or replace preventive validation.

**Posted dimension correction has a defined scope.** The [Dimension Correction Tool](https://learn.microsoft.com/en-us/dynamics365/business-central/finance-troubleshooting-correcting-dimensions) changes G/L entries, not the dimensions on their customer, vendor or item subledger entries. Select and validate the intended entry set, check the required permission, retain the correction history, and decide whether to update analysis views. Cost-accounting synchronization needs separate attention. Reports based on different ledgers can therefore show different dimension allocations after a valid correction.

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

For expected item cost, **Inventory Account (Interim)** belongs in Inventory Posting Setup, selected by location and inventory posting group. **Invt. Accrual Acc. (Interim)** belongs in General Posting Setup, selected by general business/product groups. Do not swap these matrices. Expected cost is an estimate before invoicing and uses interim accounts when configured; the invoice clears the corresponding interim amount and records actual cost. See [expected-cost posting](https://learn.microsoft.com/en-us/dynamics365/business-central/design-details-expected-cost-posting) and [posting-group responsibilities](https://learn.microsoft.com/en-us/dynamics365/business-central/finance-posting-groups).

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

Keep three controls separate: **Automatic Cost Adjustment** forwards cost changes to related item value entries; **Automatic Cost Posting** transfers value to G/L; **Expected Cost Posting to G/L** controls interim estimates. Choose scheduling from transaction volume and acceptable latency using [Inventory Setup](https://learn.microsoft.com/en-us/dynamics365/business-central/inventory-how-setup-general). A later invoice can change COGS for an earlier shipment through [cost adjustment](https://learn.microsoft.com/en-us/dynamics365/business-central/design-details-cost-adjustment) without changing quantity. Before manual [Post Inventory Cost to G/L](https://learn.microsoft.com/en-us/dynamics365/business-central/finance-how-to-post-inventory-costs-to-the-general-ledger), adjust costs, inspect the test report and resolve skipped entries. A test report with Post cleared does not update G/L.

### Customer and vendor master data

Customer configuration includes ship-to addresses, location, shipping agent/service, lead time and sales defaults. Vendor configuration includes order addresses, location, lead time and purchasing defaults. Separate legal/pay-to or bill-to identity from operational ship-to/order addresses. Templates speed entry but need controlled ownership because defaults affect tax, currency, posting and fulfillment.

### Prices and discounts

Purchase and sales price logic selects among item/resource, vendor/customer or groups, currency, unit of measure, quantity and effective dates. Line discounts apply to eligible lines; invoice discounts use document totals and eligibility. Determine whether price, line discount and invoice discount can combine, and preview the result at boundaries such as quantity, date, currency and UOM.

Current [price-list setup](https://learn.microsoft.com/en-us/dynamics365/business-central/sales-how-record-sales-price-discount-payment-agreements) distinguishes Draft from Active lists; draft lists do not participate in price calculation.

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

**Choose correction by state.** Use [Undo Receipt/Shipment](https://learn.microsoft.com/en-us/dynamics365/business-central/finance-how-reverse-journal-posting) before the quantities are invoiced and when the transaction is eligible. Reverse Transaction is a separate general-journal mechanism; it is not a universal posted-document delete, and the documented additional-reporting-currency limitation requires a different correction process. An unpaid invoice may support Cancel/Correct subject to its origin and shipment state. A partially or fully paid [sales invoice](https://learn.microsoft.com/en-us/dynamics365/business-central/sales-how-correct-cancel-sales-invoice) needs a credit/return path; a paid purchase invoice or one based on combined purchase receipts needs the [purchase credit/return path](https://learn.microsoft.com/en-us/dynamics365/business-central/purchasing-how-correct-cancel-unpaid-purchase-invoices). Correct related prepayments as necessary, and inspect application/unapplication rather than discarding the receipt history. For returned inventory, [exact cost reversing](https://learn.microsoft.com/en-us/dynamics365/business-central/sales-how-process-sales-returns-cancellations) links to the original item entry, preserving its original cost.

**Over-receipt is not an invoice agreement.** An [over-receipt code](https://learn.microsoft.com/en-us/dynamics365/business-central/purchasing-how-record-purchases) defines quantity tolerance and can require approval. Receiving extra units does not settle their financial treatment with the vendor. Work through the quantity and invoice decisions separately in example 3.

### Financial documents, journals and payments

Process purchase/sales invoices and credit memos with correct application and reason. A posted correction must reverse both business and ledger effects. Prepayments create invoices/payments before final fulfillment and must be applied through the final document lifecycle.

Payment and cash-receipt journals post cash and apply entries. Payment Registration offers an invoice-centric receipt experience. Application connects an open payment/credit to invoices; unapplication restores open detailed-ledger effects without deleting history. Reverse posted journals only when supported and understand what dependent entries prevent reversal.

Bank reconciliation matches statement lines to bank-account ledger entries, explains differences and posts adjustments. A successful import is not reconciliation. Recurring journals and G/L allocations automate repeated/distributed postings but still need period, dimension, amount and reversal controls. Exchange-rate adjustment revalues open foreign-currency entries; distinguish realized and unrealized gains/losses. Dimension Correction changes supported posted dimensions under audit. G/L currency revaluation has different scope from customer/vendor/bank adjustments.

**Revaluation and closing controls.** [G/L account revaluation](https://learn.microsoft.com/en-us/dynamics365/business-central/finance-revalue-account-balances) adjusts accumulated source-currency balances by G/L account, currency and dimension combination through a reviewable journal. It preserves source-currency amounts while changing LCY valuation. Do not revalue control-account balances already adjusted through customer, vendor or bank processes. Source-currency tracking does not itself enable revaluation. Closing accounting periods marks the year closed irreversibly but still permits prior-year entries if posting ranges allow them; repeat the income-statement closing process after such entries. See [closing accounting periods](https://learn.microsoft.com/en-us/dynamics365/business-central/year-close-account-periods).

For [bank reconciliation](https://learn.microsoft.com/en-us/dynamics365/business-central/bank-how-reconcile-bank-accounts-separately), distinguish imported statement lines, matched bank-ledger entries, outstanding timing items and missing postings. A bank fee missing from the ledger needs a posting, not a forced match. The [Copilot reconciliation assist (preview)](https://learn.microsoft.com/en-us/dynamics365/business-central/bank-reconciliation-with-copilot) supplements ordinary automatch and proposes additional matches/accounts; review those proposals before posting. Localization and current operational limits matter.

### Fixed-asset and inventory operations

Post fixed-asset acquisition, depreciation and disposal with the intended depreciation book, dates and integration. Reconcile FA ledger entries to G/L and explain gain/loss on disposal.

Inventory receipts and shipments adjust quantity outside normal sales/purchase flows when appropriate. Transfers move quantity between locations and may use in-transit state. Physical inventory counts compare expected and observed quantity; post only reviewed differences. Reclassification changes dimensions such as location/bin/variant without representing purchase or sale. Cost adjustment updates value assignment and can create later value/G/L postings.

> **Related item:** Quantity and value are related but not identical timelines. An item ledger entry carries quantity; value entries can arrive or adjust later, so operational availability can be correct while cost remains provisional.

---

## Worked examples

These original examples omit tax, charges and currency rounding unless stated. They are calculation and control exercises, not executed tenant transactions.

### 1. A second permission set broadens access

For the same table and company, permission set A permits department EAST, while B permits WEST. The user's combined access can include both departments. Adding an unfiltered grant can expose every department. Replacing A with a narrower filter does not repair B. Produce an assignment matrix and test EAST, WEST and a third department through each required access path.

### 2. Quantity is final before cost is final

Receive 10 FIFO units at expected cost 50 each: expected value is 500. Ship and invoice four before the purchase invoice; their provisional cost is 200. The vendor invoice later prices all ten at 55, with no other cost layers or charges. After adjustment, COGS is 220 and six units remain valued at 330. The 50 increase splits into 20 for sold units and 30 for remaining stock. Quantity remains six. Reconcile these value entries to G/L after cost posting; do not count clearing of the original interim value as another purchase cost.

### 3. Receiving extra stock and correcting a paid sale

Order 100 units with a 5% over-receipt tolerance: the limit is 105. A receipt of 104 is within tolerance; 106 exceeds it. Four additional units at an agreed 20 each represent 80 of extra invoice value, but that agreement and invoice still need to be recorded.

Separately, a sales invoice of 1,000 has a payment of 300 applied: 700 remains. The customer returns the entire purchase. Use a credit/return and review the existing application and reimbursement; the Cancel action is not the paid-invoice solution. The original sale, receipt and credit must remain traceable. Do not simply treat the remaining 700 as the full credit value.

### 4. Reconcile timing differences and a missing bank fee

The bank statement ends at 9,700. Add a 500 deposit in transit and subtract a 200 outstanding payment: adjusted statement balance is 10,000. The book balance is 10,050 because a 50 bank fee already on the statement is absent from the books. Post the fee to bring books to 10,000, then verify the outstanding items. Matching unrelated 50 entries would hide the error.

### 5. Pricing, deferral and allocation boundaries

Assume one eligible line of ten units at 100, a 10% line discount and an additional 5% invoice discount on that net line: 1,000 − 100 = 900; then 900 − 45 = 855. The effective discount is 14.5%, not 15%. Confirm eligibility, active price-list status, UOM, dates and rounding before using this result.

A separate 12,000 annual service expense, under an equal-month schedule of twelve full periods, recognizes 1,000 per month. After three periods, 3,000 is recognized and 9,000 deferred. An independent 6,000 overhead allocation split 25%/75% produces 1,500/4,500. Verify the posting dates, dimensions and allocation basis as well as the sum.

### 6. Foreign-currency balance and dimension corrections

A directly maintained G/L asset has EUR 2,000, originally valued at USD 1.10 per EUR: USD 2,200. At 1.15, target LCY value is 2,300, so the adjustment is +100 under these assumptions. At 1.12, target value is 2,240; the subsequent adjustment is −60, not another +40 on top of 2,300. The source balance remains EUR 2,000. Use the journal and configured gain/loss treatment; do not duplicate an AR/AP/bank adjustment.

If a posted 1,000 expense moves from department A to B through G/L dimension correction, total expense remains 1,000. The corresponding subledger dimension can still be A. Reconcile by entry and reporting source before concluding that one report is wrong.

### 7. Sender policy and document state

Prepare four paper cases: Manage per sender with Approve; Manage per sender with Ask; Always with Approve; and a monitored subfolder with Reject. The first can skip email review, the next two require review, and the subfolder case does not use the sender policy. Add a separate authenticated-internal-sender case using the setup rules. For every case, independently identify draft review, vendor approval and posting requirements. A green task icon does not prove a posted, correct invoice.

## Integrated scenarios

### Scenario 1: controlled company migration

A new distribution company defines fiscal calendar, local currency, posting ranges, number series, account categories, dimensions and posting matrices before loading masters. Configuration packages load setup and records in dependency order; opening journals establish G/L, customer, vendor and item balances. Security groups separate setup, transaction and approval work. Reconciliation proves subledgers, inventory value and bank openings, while audit records and signed totals form cutover evidence.

### Scenario 2: order-to-cash with price and exception control

A customer, ship-to address, location, item/SKU, UOM, price and discount determine the quote. Approval handles a threshold exception. The quote becomes an order; availability informs the promised date; shipment and invoice occur separately. Posting creates item/value, customer/detailed-customer and G/L entries. A partial payment is registered/applied, a returned unit uses a credit path, and reports reconcile revenue, receivable, inventory and COGS.

### Scenario 3: procure-to-pay and close

A blanket purchase agreement provides planned quantity, while orders use vendor prices and over-receipt policy. Receipts and invoices are combined correctly, a deferral spreads a service charge, and the payment proposal uses approved bank information. Bank reconciliation verifies settlement. Period close includes recurring allocations, exchange adjustment, depreciation, inventory-cost adjustment and dimension/report review; job-queue failures are resolved before sign-off.

---

## Hands-on labs

Use an isolated test company with synthetic data. These are proposed tenant labs; this review executed only offline calculations.

1. **Cutover:** Import dependent setup and masters, inject one missing dependency, then reconcile opening journals and every reject. Keep a before/after control-total sheet.
2. **Security:** Test EAST/WEST and an unfiltered grant with a nonadministrator across company and access paths. Record both permitted and denied records.
3. **Core and dimensions:** Configure numbering/layouts, default priorities and blocked combinations. Correct a posted G/L dimension and compare the unchanged subledger and refreshed analysis view.
4. **Workflow and queue:** Run approve/reject/delegate and queue success/failure cases. Show why On Hold during execution is not cancellation and verify recovery does not duplicate effects.
5. **Financial setup:** Configure chart/categories, general/specific/inventory posting matrices, currency and deferral. Predict accounts before posting and compare actual entries.
6. **Trade:** Test UOM, SKU/location, active/draft prices and date/quantity discount boundaries. Explain every price and calculate the expected total.
7. **Documents and payments:** Process quote/order/partial fulfillment/invoice/prepayment and paid-invoice credit paths, including combined receipts. Trace application and unapplication without deleting history.
8. **Inventory and bank:** Reproduce examples 2–4, run adjustment before manual cost posting, resolve skipped entries and distinguish outstanding bank items from missing fees.
9. **Assets and close:** Acquire, depreciate and dispose of an asset; reconcile FA/G/L and a direct G/L currency balance. In a disposable company, document the irreversible year-close state and later prior-year entry behavior.
10. **Agents:** Begin with a paper control matrix for sender settings, subfolders, forwarded contacts, blocked vendors, invoice drafts and credit exhaustion. If an authorized test environment is available, record the actual setting/version and task evidence. Do not enable the production-only automatically billable trial as a sandbox shortcut.

## Knowledge checks with answers

1. **When use a clean company?** When a controlled implementation needs its own setup and opening state; demo data is for evaluation and practice.

2. **Worksheet, package or template?** A worksheet organizes setup tasks; a package imports/applies selected tables and fields; a template supplies repeatable record defaults.

3. **What accepts a migration?** Reconciled counts, rejects, opening balances and subledger/control totals, with business sign-off.

4. **Does a profile secure data?** No. It shapes the workspace; permissions and security filters govern access.

5. **What happens when table filters overlap?** The least restrictive combined permission applies; a narrow set cannot cancel another broad grant.

6. **Which security tests matter?** The target company/user and required pages, reports, Excel, APIs and background operations, including negative cases.

7. **What does a number-series relationship provide?** A controlled alternative series; still test date, manual-number and collision rules.

8. **Does Ready prove successful work?** No. Inspect job logs and resulting business records.

9. **Does On Hold stop a running job?** No. It prevents a future start; running work has a separate lifecycle.

10. **What activates agent use responsibly?** Supported environment/language, permission and mailbox setup, billing, review owners and exception tests.

11. **Does finalizing a Payables draft post it?** No. It creates a purchase invoice awaiting the applicable approval/posting process.

12. **Do sender policies always apply?** No. Always/Never and monitored-subfolder behavior can override or bypass them.

13. **Why review agent-created vendors?** They begin blocked; vendor approval and bank validation remain separate responsibilities.

14. **Does a Sales Order Agent quote reserve stock?** No. Its initial quote has no reservation/planning effect; an order is a later state.

15. **How is forwarded sales email identified?** By the forwarder’s sender address; use a verified one-time contact association when appropriate.

16. **How do default dimensions interact?** Defaults come from records/account types and priorities; blocked combinations can still reject the result.

17. **What does dimension correction leave unchanged?** Related subledger dimensions; also check analysis-view and cost-accounting follow-up.

18. **Why distinguish workflow from notification?** Workflow governs the business transition; a notification only communicates it.

19. **How do account categories and dimensions differ?** Categories organize account/report structure; dimensions classify transactions along management axes.

20. **Where is Inventory Account (Interim) configured?** Inventory Posting Setup by location and inventory posting group.

21. **Where is Invt. Accrual Acc. (Interim) configured?** General Posting Setup by general business and product posting groups.

22. **Why inspect multiple posting groups?** They allow different accounting treatments but also add choices that can route a balanced posting incorrectly.

23. **Template, batch and journal line?** Purpose/default structure, grouped work/numbering, and individual transactions respectively.

24. **What do detailed ledger entries explain?** Applications, unapplications, discounts, tolerances and exchange effects on remaining customer/vendor amounts.

25. **How do FA books and posting groups differ?** Books define depreciation/valuation treatment; posting groups select the G/L accounts.

26. **How do item, value and G/L entries relate?** Quantity, valuation and financial accounting are linked but may update at different times.

27. **What does a SKU add?** Item/location/variant-specific planning and replenishment settings.

28. **Which master-data addresses matter?** Bill-to/pay-to identity and ship-to/order addresses have distinct financial and operational roles.

29. **Does a draft price list apply?** No. Activate it and verify eligibility/date/quantity/UOM/currency conditions.

30. **Do 10% and then 5% discounts equal 15%?** No. With both applicable sequentially, the effective discount is 14.5%.

31. **How do design, customization and personalization differ?** Application development, a shared profile experience, and one user’s preferences.

32. **Why use page inspection?** To identify page/table/extension context for diagnosis without assuming edit rights.

33. **Edit in Excel versus Open in Excel?** Supported publish-back editing versus an export-oriented experience; validate permissions and errors.

34. **What gives analysis mode meaning?** Its company, filters, fields, grouping and reporting grain.

35. **Why separate receipt/shipment from invoice?** Physical quantity and financial valuation can reach completion at different times.

36. **Does tolerated over-receipt settle the vendor invoice?** No. Agree and record its financial treatment separately.

37. **Blanket order versus recurring lines?** A longer-term quantity agreement versus reusable document-line defaults.

38. **When can Undo Receipt/Shipment apply?** Before invoicing and subject to supported transaction conditions.

39. **How correct a partially paid sale?** Use a credit/return and review applications/refund; Cancel/Correct on the paid invoice is not the route.

40. **Which purchase invoices need a credit path?** Paid invoices and invoices based on combined receipts are documented examples.

41. **Why link a return to the original item entry?** Exact cost reversing preserves the cost of the original sale.

42. **What must a prepayment correction include?** Its own corrective lifecycle plus correct application in the final order/invoice process.

43. **Does unapplication delete payment history?** No. It changes application effects through detailed entries while preserving the posting trail.

44. **How distinguish a timing item from a missing fee?** A timing item already exists in one system and is outstanding in the other; the fee needs the missing ledger posting.

45. **What must precede manual inventory cost posting?** Current adjusted value entries, a checked test report and resolved skipped-entry causes.

46. **Which balances belong in G/L currency revaluation?** Eligible directly maintained source-currency balances, excluding balances already handled by customer/vendor/bank adjustment.

47. **Does closing accounting periods prevent every backdated entry?** No. Posting ranges still matter; later prior-year entries require another income-statement close.

48. **How prove asset and inventory close?** Reconcile acquisition/depreciation/disposal and gain/loss, counts/transfers/reclassification, adjusted costs and G/L totals with consistent filters.

---

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one primary route, build one company from setup through close, and add a second resource only for a measured gap.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MB-800 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-800) | Free | 1–2 hours to map four domains and June change log |
| [Set up Business Central](https://learn.microsoft.com/en-us/training/paths/set-up-business-central/) | Free | 5 modules; runtime not shown; 12–20 hours with setup/migration/security labs |
| [Configure financials](https://learn.microsoft.com/en-us/training/paths/configure-financials-business-central/) | Free | 15 modules; runtime not shown; 25–40 hours with posting/reconciliation practice |
| [Configure sales and purchasing](https://learn.microsoft.com/en-us/training/paths/configure-sales-purchasing-business-central/) | Free | 7 modules; runtime not shown; 12–20 hours with price/inventory setup |
| [Process sales and purchasing](https://learn.microsoft.com/en-us/training/paths/process-sales-purchasing-business-central/) | Free | 12 modules; runtime not shown; 25–40 hours with full document lifecycles |
| [Process financial operations](https://learn.microsoft.com/en-us/training/paths/process-financial-operations-business-central/) | Free | 9 modules; runtime not shown; 18–30 hours with close/correction/reconciliation |
| [MB-800T00-A: Manage business solutions with Microsoft Dynamics 365 Business Central](https://learn.microsoft.com/en-us/training/courses/mb-800t00) | Paid/provider-dependent | 5 days; English |
| [MicrosoftLearning MB-800 labs](https://github.com/MicrosoftLearning/MB-800-Business-Central-Functional-Consultant) | Free; MIT | 15–30 hours selected; review open issues and current tenant/localization differences |
| [Free MB-800 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/d365-business-central-functional-consultant-associate/practice/assessment?assessment-type=practice&assessmentId=109&practice-assessment-type=certification) | Free | 45–90 minutes plus remediation |
| [Business Central documentation](https://learn.microsoft.com/en-us/dynamics365/business-central/) | Free | 20–50 hours selected implementation/reference reading |
| [O’Reilly: Business Central Essentials](https://www.oreilly.com/library/view/microsoft-dynamics-365/9798868822292/) | Subscription/trial | 186-page Apress book by Dr. Gomathi S, January 2026; 2h38 platform reading estimate, not video runtime; broad primer |
| [Udemy MB-800 by Dr. Gomathi Srinivasan](https://www.udemy.com/course/mb-800-dynamics-365-bc-functional-consultant-exam-training/) | Paid | 14 sections, 36 lectures, 18h43; public listing updated February 2026, gap-check against June inventory/agent changes |
| [MeasureUp MB-800 practice test](https://www.measureup.com/microsoft-practice-test-mb-800-microsoft-dynamics-365-business-central-functional-consultant.html) | Paid; free demo | 2–5 hours; 132 questions, last updated January 2026, so map against June changes first |
| [Microsoft Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner login required | Use the five-day course pattern for planning; signed-in event start/end times control |

The five official paths show **48 module placements** (5/15/7/12/9); the current public pages do not show runtime. The earlier 43h40 total is withdrawn. Linked units were not exhaustively read; budgeted asset and integration material can be adjacent to the detailed exam bullets. Allow roughly **100–170 hours** for a learner without current Business Central implementation experience to configure, transact, reconcile, correct and remediate. No exact current Pluralsight or Whizlabs MB-800 product was independently verified. Question-bank-only, recalled-content and guaranteed-pass listings were excluded.

## Useful articles and current documentation

- [Sumit Singh: Inventory Setup in Business Central](https://community.dynamics.com/blogs/post/?postid=7989aea7-627b-f011-b4cc-7c1e5248819c) provides prompts for an inventory-reconciliation worksheet. **Use it selectively:** its placement of Inventory Account (Interim) conflicts with the official setup documented above. Do not copy its account map or generic configuration defaults. Publication date was not independently established.
- [Mike Morton: Sales Order Agent public-preview introduction](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2025/04/03/sales-order-agent-in-microsoft-dynamics-365-business-central-now-in-public-preview/) (April 3, 2025) helps trace a request through review and document creation. Its preview status and defaults are historical; current setup/supervision docs govern the lab. The embedded video was not watched.
- [Richard Riley: the AI at Work roadmap transition](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/08/25/one-always-on-roadmap-dynamics-365-power-platform-and-dataverse-join-the-ai-at-work-roadmap/) (August 25, 2026) explains the September move of new release disclosures and planned November 15 Release Planner retirement. Use roadmap discoveries to select a current-documentation check; an announced feature is not evidence that it is enabled in your company.

For each article, write one requirement, one predicted ledger/document state, one negative case and the evidence that would prove the result. This makes optional reading useful without treating a blog as the exam blueprint.

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
