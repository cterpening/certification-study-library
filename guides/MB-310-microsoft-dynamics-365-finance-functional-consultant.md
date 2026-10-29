---
exam_code: MB-310
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-310
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-10-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-10-28
---

# MB-310 Microsoft Dynamics 365 Finance Functional Consultant Study Guide

> **Independent AI-assisted resource — HUMAN REVIEW PENDING.** The October 28, 2026 team refresh reconciles this complete guide and detailed objectives with current public exam, product and learning evidence. See the [current group report](../docs/research/2026-10-28-microsoft-refresh-group-04.md#mb-310) and [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#mb-310-coverage-record). Source limits and unexecuted exercises remain explicit. This is not human review or live product validation. The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-310) is authoritative.

**Current baseline:** Skills measured as of August 14, 2026.<br>
**Upcoming blueprint change:** None announced on the official study guide as checked October 28, 2026. Current detailed objective text is unchanged.<br>
**Lifecycle:** The [Dynamics 365 Finance Functional Consultant Associate credential](https://learn.microsoft.com/en-us/credentials/certifications/d365-functional-consultant-financials/) is active. The exam is 100 minutes, available in English and Japanese, lists no retirement date, and links a free Practice Assessment. Renewal is every 12 months; the direct assessment endpoint exposed no question content during this review.<br>
**Scope change:** The August baseline removes cost management, substantially revises financial management, receivables, subscription billing, payables and fixed-asset transactions, and adds budget planning. Do not use an older course or practice test as the objective checklist.<br>
**Official source:** [MB-310 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-310)

**September deep review:** All 96 published objectives are mapped in the [review report](../docs/research/2026-09-28-mb-310-deep-review.md). The earlier repository snapshot condensed them into 89 bullets; the complete extraction restores detail without implying a new exam announcement. The previous snapshot remains archived.

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

Use the current [financial-tag documentation](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-tag): a legal entity can define up to 20 tags. Ordinary List/Custom list choices do not enforce membership; **Fixed list/Fixed custom list**, available from 10.0.44, validate entered values against the list. This does not turn a tag into an account-structure dimension. Procurement support requires 10.0.49 or later and the purchase-order-invoicing tag feature. Check version and feature state before following an older journal-only tutorial.

The September 11, 2026 [financial-dimension service deprecation](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-dimensions) concerns an optional optimization for certain large DMF general-journal imports. Financial dimensions remain core accounting structures. The old service excludes Customer/Vendor/Bank account types and derived-dimension scenarios; do not interpret its deprecation as instructions to remove dimensions.

#### Turn a shortcut into a controlled account combination

For a synthetic maintenance expense, define an alias against the correct account structure and company, specify its main-account/dimension combination and choose which dimension receives initial focus. Enter the alias in a test journal and inspect the expanded segments before validating. An alias accelerates entry; it does not bypass account-structure rules or establish a user's posting permission. Compare this with a main-account category used for reporting and a balance expectation used for validation. See [ledger-account alias setup](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/set-up-ledger-account-alias). Change one dimension to an invalid value and retain the expected rejection as evidence.

### Configure ledgers, fiscal time and currency

The ledger ties a legal entity to its chart of accounts, fiscal calendar, accounting currency, reporting currency and balancing dimensions. Fiscal calendars define years and periods; opening or closing a period controls when modules and user groups can post. **Posting layers** separate current, operations, tax or custom reporting effects without creating another legal entity.

Currency design includes currencies, exchange-rate types and dated exchange rates. A transaction currency is translated into accounting currency and, when configured, reporting currency. Revaluation recognizes unrealized currency changes on open balances or ledger accounts; settlement or payment realizes the difference. Configure posting profiles/accounts and dates deliberately, then reconcile the revaluation voucher to the selected population.

Ledger allocation rules redistribute balances by fixed percentage, basis or supported allocation method. Define source, destination, basis, offset, schedule and traceability. An allocation should preserve totals and produce explainable dimensions. Intercompany accounting creates balanced due-to/due-from entries across legal entities; validate both companies, exchange rates, dimensions and period status.

In [GL revaluation](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/foreign-currency-revaluation-general-ledger), exclude AR/AP/bank main accounts when their modules perform revaluation, avoiding a second adjustment to the same exposure. GL posts the difference from the existing revalued balance; AR/AP reverse the previous open-transaction revaluation and calculate a replacement. GL's postable preview cannot run in batch; AR/AP simulation is a report. Keep the balance-selection date range separate from the exchange-rate date.

### Implement controlled journals

A journal name carries defaults and controls such as journal type, voucher numbering and workflow. Voucher-number policy affects auditability: understand when numbering occurs, whether lines share a voucher and how continuous numbering behaves. Posting restriction rules and journal controls constrain who may post which accounts or dimensions. Periodic journals support recurring patterns; reversal configuration creates an intentional opposite entry at the chosen date.

For manual and Excel-assisted journals, trace template → draft/import → validation → workflow if used → posting → voucher → ledger inquiry. Excel improves volume entry but does not bypass account structures, permissions or validation. Batch posting improves throughput; it adds scheduling, contention, retry and monitoring responsibilities. A safe correction preserves audit history through reversal or supported correction rather than deleting evidence.

#### Retrieve a recurring entry, then validate the actual journal

For a monthly 600 expense, create a periodic-journal line with account/offset/dimensions, next date, a one-month interval and the correct last retrieval date. Retrieve it into a general journal using a deliberate cutoff; inspect how many occurrences were generated before approving/posting. A cutoff spanning several due dates can create the line several times. Retain the periodic definition and the generated journal/voucher separately. See [periodic-journal retrieval](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/post-periodic-journals).

For an Excel journal template, choose an entity/template supporting the account types, retain journal/company keys and mandatory fields, then add the needed dimensions through the supported entity/designer configuration. Refresh the journal context, enter synthetic lines, publish and inspect validation errors in Finance before posting. Publishing is not posting. A custom workbook's presence on disk does not make it a journal-menu template: promotion has a registration/resource path and journal-type/account-type filtering. See [journal template support](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/open-lines-excel-journals-documents) and [custom template promotion](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/user-interface/add-templates-open-lines-excel-menu). Test an unsupported offset type and an invalid dimension rather than weakening validation. Developer registration is implementation context; the functional objective is to create/modify a usable, correctly bound template.

### Manage cash, banks and payments

Bank groups organize institutions; bank accounts hold currency, account identifiers, reconciliation, posting and payment settings. Payment methods define how customer or vendor payments are processed, while payment-format configuration produces or imports the bank-specific message. Protect account changes and payment-file generation with segregation of duties, workflow and out-of-band verification.

Manual reconciliation matches statement lines and Finance transactions directly. **Advanced bank reconciliation** imports statements, normalizes transaction codes and applies matching rules before exceptions are reviewed. Test one-to-one, one-to-many, fees, interest, duplicates, missing transactions and statement corrections. Bank foreign-currency revaluation updates eligible balances and posts the difference to configured accounts.

Cash-flow forecasting combines configured liquidity accounts, transaction sources and forecast rules into time-based projections. Automation can refresh forecasts, but completeness and timing assumptions still need review. Shared payment setup centralizes eligible payment activity across legal entities. Customer/vendor netting settles compatible receivable and payable amounts; preserve approvals, counterparty agreement and residual balances.

> **Related item:** Payment proposal selects obligations, payment journal authorizes accounting, payment format communicates with the bank, and reconciliation proves what cleared. These are distinct controls in one cash process.

[Bank matching rules](https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/set-up-bank-reconciliation-matching-rules) can select the first eligible document by default. Enable the manual-review parameter for ambiguous matches on amount and use references/date criteria. The [advanced reconciliation procedure](https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/reconcile-bank-statements-advanced-bank-reconciliation) distinguishes the Modern bank reconciliation feature; record its state instead of mixing both workflows. Importing a multi-account file can succeed for some accounts and fail for others, so inspect per-account results before retrying.

[Customer/vendor netting](https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/net-customer-and-vendor-balances) requires an active agreement, a suitable journal name and a bridging account. Net eligible open transactions **before creating payment journals**; transactions already included in a payment journal are outside that netting flow. A reversal both unsets settlement and reverses the netting journal. Intercompany netting has its own enablement and company setup; it is not implied by two accounts sharing a name.

#### Schedule forecast data and configure cross-company settlement

For forecasting, identify liquidity accounts first, then select source areas and timing assumptions on Cash flow forecast setup. Calculate a baseline and inspect its last-run date. If using cash-flow process automation, resolve competing legacy batch schedules, create the supported schedule **for each company**, and inspect pending/completed runs. Refresh the relevant analytical measurement as required; a calculation timestamp and report timestamp can differ. Test an omitted bank account and an unpaid invoice with an unrealistic expected date. See [cash-flow setup and automation](https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/cash-flow-forecasting).

For shared payments, configure a hierarchy with purpose **Centralized payments**, intercompany due-to/due-from accounts and the chosen company treatment for discounts/realized currency differences. Corresponding customer/vendor accounts need the same address-book identity; payment-method and posting-profile **IDs** must match across the involved entities, although their account settings can differ. Any included entity can pay for another; this is not restricted to a parent paying children. See [centralized-payment setup](https://learn.microsoft.com/en-us/dynamics365/finance/cash-bank-management/set-up-centralized-payments). In an original test, pay a 900 invoice in company B from company A, then reconcile B's settled liability, A's cash and reciprocal balances. Test a missing party mapping and a mismatched payment-method ID before generating a bank file.

### Perform close, consolidation and tax work

A financial close should be a scheduled, owned set of tasks with dependencies and evidence. Configure financial-period workspaces and close schedules; control period access by module and group. Reconcile subledgers to the general ledger before closing, run necessary accruals/revaluations/allocations, and use closing or year-end templates where supported. Ledger settlement matches related ledger transactions; it is not a substitute for correcting an erroneous voucher.

Consolidation combines legal entities under consistent account, currency and period rules; elimination removes intercompany effects. Decide between the supported online consolidation pattern and another reporting/consolidation architecture based on ownership, adjustments, translation, audit and scale. Validate that eliminations remove only reciprocal balances and that late subsidiaries and ownership changes have a defined process.

Sales-tax configuration connects sales tax codes, groups, item groups, settlement periods and authorities with posting groups. The intersection of party group, item group, jurisdiction and transaction determines tax behavior. Test taxable, exempt, reverse/adjusted and cross-border cases appropriate to the configuration. Settlement calculates the period liability and posts to authority accounts. Withholding tax has its own groups, codes and authorities; distinguish it from sales tax.

> **Related item:** Financial reporting consumes ledger and dimension structures but is not a repair layer. If a report needs extensive overrides to reconcile, investigate posting, dimensions, currency and close first.

---

For [ledger settlements](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/ledger-settlements), realized currency differences require the relevant feature/account settings. Microsoft recommends leaving that calculation off for AR/AP summary accounts whose subledgers already realize differences. Do not mark earlier unrealized revaluation entries for settlement; rerun GL revaluation afterward to resolve them. For [consolidation currency translation](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-consolidations-currency-translation), distinguish initial translation from subsequent revaluation and document which company's currency settings apply.

---

#### Configure the consolidation company before running it

Create the target legal entity with the financial-consolidation designation, configure its chart, fiscal calendar, accounting/reporting currencies, rate type and exchange rates, then prepare subsidiary account mapping. Choose an elimination company/control design deliberately. A consolidation entity is not a daily operational company. In a synthetic two-subsidiary run, record source dates, account mapping, translation accounts and consolidation history; reconcile source balances before eliminating reciprocals. See [consolidation-company preparation](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/prepare-company-for-consolidation). **VERIFY CURRENT:** Consolidate online template and preview behavior; a source balance change requires a deliberate rerun/review, not an unexplained plug.

#### Work a tax intersection through settlement

Set up tax main accounts/posting group, authority and settlement period before linking a code to the period and posting group. Put the appropriate codes in the party sales-tax group and item sales-tax group, then test their intersection on a document. For an invented exclusive-price line of 800, a common 5% code produces 40; an additional code present in only one group does not apply merely because it exists. Review the transaction's calculated tax and any supported documented adjustment, including the configured exemption treatment. See [sales-tax components and calculation](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/indirect-taxes-overview).

For settlement, select the settlement period/date interval and correct original/correction processing, review the calculated liability, then run Settle and post sales tax and reconcile the clearing/settlement account. A later tax payment is a separate cash transaction. Test a late invoice after the original settlement and use the documented correction process rather than settling the original interval twice. See [sales-tax settlement procedure](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/tasks/create-sales-tax-payment).

Withholding has its own setup. For the **global withholding** mechanism, configure authority, settlement period, ledger posting group/accounts, codes, party groups and item withholding groups before testing the applicable threshold and transaction. Do not assume ordinary vendor-payment withholding and global/localized withholding share every field or calculation trigger. See [global-withholding setup](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/set-up-global-withholding-tax). For an original paper test, an explicitly applicable 2% withholding on a 1,000 base gives 20 withheld and 980 paid; confirm the actual jurisdiction, taxable base, recognition event and payable/withholding vouchers in an authorized sandbox. This arithmetic does not establish a real tax rate or policy. **VERIFY CURRENT:** localization, tax-engine selection, account requirements, rounding and feature state.

## 2. Implement receivables, credit, collections, and subscription billing

### Run order-to-cash with explainable posting

Customer groups provide shared defaults; shared customers support cross-company use where configured. Posting profiles map customer transactions to summary and offset accounts. Payment methods, bank accounts and charges affect collection and settlement. For each free-text invoice, recurring invoice, sales-order invoice, credit memo, prepayment and intercompany invoice, explain the document state, tax, dimensions, due date, voucher, open transaction and settlement.

Customer payments may be entered/imported and settled against invoices; overpayments, underpayments, discounts and write-offs need explicit accounts and authority. Accounts-receivable foreign-currency revaluation adjusts eligible open balances. Billing classifications can separate supported invoice populations and processing. Protect customer bank details and changes to payment instructions as sensitive financial master data.

### Control credit and collections

Credit management combines limits, risk attributes, rules, holds and release authority. A sales order placed on credit hold needs a visible reason, reviewer and outcome; overriding a control must leave evidence. Aging-period definitions group open balances by due date, and aged-balance inquiries show exposure. They inform collection action but do not determine customer intent by themselves.

Collections use pools, activities and work queues to prioritize contact and resolution. Interest notes and collection letters apply configured policies; write-offs remove approved uncollectible balances to the proper account. Design for disputes, promises to pay, partial settlements, legal restrictions and vulnerable customers. Measure recovered value, dispute resolution and aged exposure, not just contact volume.

#### Generate recurring invoices and process collection evidence

Create a free-text invoice template containing the service/revenue account, amount, tax/charges, terms and dimensions; assign it to the customer with start/end, frequency and any maximum amount. Generate for a chosen invoice date, inspect the recurrence ID and individual documents, submit workflow when required, validate and post. A generated recurrence group is not a posted receivable. Test a customer with two schedules and a failed document; reconcile already-posted members before regenerating. See [recurring free-text invoice setup](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/set-up-process-recurring-invoices).

For a prepayment scenario, configure the prepayment posting account/feature and applicable parameters, create/confirm the proposal and post the deposit invoice, then settle it through the customer payment journal. Select the received prepayment for application to the final sales invoice and verify synchronous settlement or successful background application under the configured option. For a 5,000 sale with an agreed 1,000 deposit, reconcile a 4,000 remaining receivable, then test reversal/credit. See [customer prepayment setup and application](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/customer-prepayment-invoice). **VERIFY CURRENT:** line-level versus header-level prepayment and settlement feature/parameter state. A payment journal marked as a prepayment is not automatically the same contract as a sales-order prepayment invoice.

Billing classification has public-sector applicability: create the classification with terms, associate existing billing codes and explicitly decide interest/collection-letter settings; the documented defaults suppress those activities for that classification. Apply it to an appropriate free-text invoice and verify grouping and due date. See [billing classification setup](https://learn.microsoft.com/en-us/dynamics365/finance/public-sector/tasks/create-billing-classification-public-sector). Do not treat it as a universal customer-payment category.

For letters, assign the collection sequence and permission on the customer posting profile, generate the selected transaction/date/customer population, review the created letter, then print/post under the intended process. Customer-level versus transaction-level handling changes how letters group and advance. See [collection-letter processing](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/tasks/process-collection-letters). For interest, assign the interest code to the applicable posting profile, select the calculation population/date range, review created notes and post with the intended per-transaction versus grouped posting behavior. See [interest-note processing](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/tasks/process-interest). In both cases, test a payment or credit arriving before posting; stale selection must not produce an unjustified demand. Retain source open items, calculation parameters, note/letter ID and voucher.

### Configure subscription billing and deferrals

A billing schedule defines recurring or milestone-based customer billing. Contract billing groups, item groups, frequency, dates, pricing, escalation and milestones determine generated sales documents. Holds and termination change future processing; preserve the commercial reason and effective date. Test mid-period starts, price updates, renewal, usage/milestone completion, cancellation and credit.

Revenue and expense deferrals separate invoice/posting timing from recognition timing. Configure deferral defaults and the items deferred by default, then generate recognition schedules. Charges may also be deferred. A schedule needs start/end convention, period allocation, account mapping and treatment for modification or termination. Reconcile source document → deferral schedule → periodic recognition entries → remaining balance.

> **Related item:** Subscription billing creates and manages recurring commercial documents; deferral controls when revenue or expense is recognized. A recurring invoice does not automatically prove compliance with an accounting recognition policy.

---

Check the [deferral parameters](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/sb-deferrals): Equal per period gives equal full-period amounts but prorates partial periods; turning it off allocates using days. Posting method and reversal settings also affect credit/termination behavior. In [recognition processing](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/sb-deferrals-schedules), the cutoff includes schedule lines whose end date is on or before it. Creating a recognition journal is not evidence of posting when automatic posting is off. Once lines are recognized, schedule modification must handle their history through the supported catch-up/reversal behavior.

For a straight-line schedule, recognition history changes the available repair: with no recognized or externally posted lines, the whole schedule, including its start date, can be modified. With history, use the documented recalculation, catch-up or reversal behavior and preview the result. An event-based schedule has different restrictions, including immutable template/allocation choices once history exists. The [schedule modification rules](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-receivable/sb-deferrals-schedules) are a better diagnostic than assuming every schedule remains freely editable.

---

## 3. Implement payables and expenses

### Control procure-to-pay

Vendor groups, shared vendors, posting profiles, payment methods, charges and bank accounts supply defaults and accounting behavior. A vendor invoice may originate from a purchase order, invoice journal, recurring invoice, prepayment or intercompany flow. Trace each to liability, tax/charges, expense or inventory, due date, open transaction and settlement.

Invoice validation checks required data and policy. Invoice matching compares invoice price/quantity with purchase order and product receipt according to two-way or three-way rules and tolerance. A discrepancy needs workflow, documented approval or correction; changing tolerance merely to make an invoice pass weakens the control. Vendor invoice journals support invoices not tied to a PO but still require dimensions, tax, approval and duplicate controls.

Payment proposals select due items by criteria; payment journals make the accounting/payment set reviewable before file generation or posting. Centralized payments process eligible obligations across companies. Prepayments must later be applied to the correct invoice. Accounts-payable foreign-currency revaluation adjusts eligible open vendor balances. Secure vendor bank changes and separate vendor maintenance, invoice approval and payment release.

[Invoice matching](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/accounts-payable-invoice-matching) separates net unit price, price totals and receipt quantity. Both two-way and three-way matching compare price; three-way also compares invoiced quantity with the **selected product receipts**, not simply the PO's ordered quantity. Charges and discounts affect net unit price. For price-total tolerance, percentage comparison uses transaction currency and amount comparison uses accounting currency; partial invoicing defers that price-total validation until the last invoice for the line.

### Govern employee expenses

Expense categories connect business meaning, account, tax and policy. Configure per diem, mileage, intercompany expenses and treatment of personal spend according to the organization’s rules. Expense reports collect lines, receipts, project or dimension context and attestation; policies can warn or block based on amount, category, age or other supported conditions.

Test missing receipts, mixed currency, partial personal spend, delegate entry, policy exception, rejected/returned report and cross-company/project allocation. The final voucher should be reconcilable to the approved report, while sensitive receipt and personal information remains appropriately secured.

> **Related item:** Project Operations expense modules appear in the official MB-310T00 course syllabus, but the exam objective is the Finance expense process. Use adjacent course modules to understand integration boundaries, then map every study claim back to the current blueprint.

---

#### Build recurring payables and an expense-control worksheet

With the recurring-invoice feature enabled, save a suitable pending vendor invoice as a template, including distributions, tax, charges and dimensions. Assign it to the vendor with dates/frequency/limits, generate the selected recurrence and inspect each pending invoice. Submit workflow before posting when required. A recurrence ID groups generated documents; it does not prove all posted. See [recurring vendor invoice workflow](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/recurring-invoice). For a monthly 250 maintenance service, test an intentionally changed vendor tax/default account and a failed invoice before allowing the next run.

Expense categories require a shared category, expense type, default payment method, main account, item-tax group and any itemization/subcategory decisions. Configure those first, then create an original report containing mileage, a location/date-based per diem, a personal portion and an intercompany line. See [expense-category setup](https://learn.microsoft.com/en-us/dynamics365/project-operations/expense/set-up-expense-categories).

For mileage, configure the rate/tiers and test quantities immediately below/at/above a tier boundary and the fiscal-versus-calendar accumulation setting. For per diem, confirm the intended interface/feature, travel dates/location and included-meal reduction method before calculating. See [mileage tier configuration](https://learn.microsoft.com/en-us/dynamics365/project-operations/expense/set-up-mileage) and [per-diem entry prerequisites](https://learn.microsoft.com/en-us/dynamics365/project-operations/expense/mobile-app-manage-perdiem). An invented 80-distance-unit trip at a single 0.50 rate is 40, but it is not a published reimbursement rate.

Enable **Allow intercompany expense lines** before entering a line for work performed for a borrowing company. Configure project-intercompany default categories where applicable, and explicitly select the supported source/destination tax treatment before reconciling both entities. See [intercompany expense configuration](https://learn.microsoft.com/en-us/dynamics365/project-operations/prod-exp/intercompany-expense). For corporate-card personal spend, select Paid by employee or Paid by company in Expense management parameters: the latter pays the card bill and debits the worker account. A 100 card line split into 75 business and 25 personal must preserve that 25 recovery/employee obligation under the chosen method. See [personal expense treatment](https://learn.microsoft.com/en-us/dynamics365/project-operations/expense/personal-expenses-expense-report). These references are under Project Operations Integrated with ERP; verify the Finance-integrated deployment rather than using older Project Service instructions. **VERIFY CURRENT:** deployment, feature state, currency, policy and statutory requirements. No expense report was submitted here.

## 4. Implement budgeting

### Separate three budgeting capabilities

**Basic budgeting** records budget register entries against a budget model and code. Models organize versions; codes describe entry types and can control workflow. Allocation terms and transfer rules support distribution and controlled movement. Compare budget to actual at the same account/dimension and period grain.

**Budget control** checks funds availability on configured source documents and journals. Configure parameters, dimensions, rules, groups, calculation and over-budget permission. Test reservation/encumbrance behavior where relevant, thresholds, amendments, transfers, year boundaries, workflow and users allowed to exceed. A green check depends on the selected calculation and scope; it is not an unlimited-funds statement.

**Budget planning** is a collaborative proposal and approval process. Configure planning organization hierarchy, process, stages, scenarios, workflows, layouts/templates and allocations. Scenarios distinguish values such as prior actual, baseline, request and approved budget; stages define who acts when. Test promotion between stages, rejected/returned plans, allocation recalculation and transfer of the approved plan to budget entries.

> **Related item:** Basic budgeting stores approved amounts, budget control enforces availability, and budget planning develops proposals. They can integrate, but each solves a different governance problem.

---

The [budget-control setup](https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/budget-control-overview-configuration) has two distinct requirements: activate the configuration and **turn budget control on**. An Active configuration with control off does not enforce a manual budget check either. Plan initial balances and activation at the beginning of a cycle; transactions posted while control is off do not populate its tracking history. Align document selection with the available-funds formula and examine how reservations are relieved downstream.

Version 10.0.49 adds an optional automatic accounting-date advancement feature for budget-controlled PR/PO workflows whose original period closes. It does not automatically cross into a new fiscal year. A [budget-control statistics report](https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/budget-control-statistics-and-budget-analysis-report) and budget analysis report can differ in draft/reservation scope and exchange rates; reconcile those settings before calling a difference an error.

---

#### A budget entry becomes usable through its lifecycle

Prepare Budgeting dimensions, model, code, number sequence and rates; attach any workflow to the code and configure budget control before loading its starting amounts. Create the register header with model/code and lines with date, account structure, dimension values, amount/type and currency. Submit/complete the required workflow and **Update budget balances**; a saved draft does not establish available budget. See [budget-register entry lifecycle](https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/budget-register-entries).

For an original transfer, move 1,200 from department A to B with a Transfer budget code: A −1,200, B +1,200. Confirm both dimensions and dates, workflow and transfer rules, then reconcile model totals and budget-versus-actual at the same grain. Allocation creates reversal and destination entries; inspect them before updating balances. An overall zero transfer can still be wrong when it moves money from an unauthorized source.

## 5. Manage fixed assets

### Configure books and depreciation

Fixed-asset groups provide shared defaults and numbering; assets hold individual identity and attributes. A **book** represents a valuation/depreciation basis, such as corporate or tax, with acquisition, depreciation and disposal behavior. Derived books can create related transactions in another book. Posting profiles map asset transaction types to ledger accounts.

Configure service life, depreciation profile/convention, depreciation periods and supported methods. Map groups/assets to books deliberately. Before running depreciation, validate placed-in-service date, acquisition basis, residual value, remaining life and prior postings. A proposal selects expected transactions; review before posting and reconcile accumulated depreciation and net book value.

[Derived books](https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/derived-books) copy selected transaction types from a primary book; acquisition is a common choice. [Derived depreciation](https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/post-derived-value-models) copies the primary amount rather than recalculating a different tax method. Use independently calculated depreciation where methods differ. A copied acquisition is not a second supplier liability: customer/vendor/tax accounts update once through the primary transaction, while the derived asset entries use their configured accounts and posting layers.

### Process the asset lifecycle

Assets can be acquired through a purchase order, fixed-asset journal, inventory or project process depending on the requirement. Trace source cost, capitalization date, dimensions and voucher into the correct asset/book. Fixed-asset budgets can feed budgeting; budget is authorization/planning, not an acquisition transaction.

Use journals or supported source documents to split, reclassify or transfer assets while preserving history and correct company/dimension/book balances. Disposal by sale can use a free-text invoice; disposal by scrap has no customer proceeds. Both must remove cost and accumulated depreciation and recognize the resulting gain or loss. Run depreciation across companies only with deliberate batch scope, security and monitoring.

> **Related item:** Asset leasing is relevant Finance knowledge and may affect accounting, but it is not an explicit domain in the August 14, 2026 MB-310 objectives. Cost management was removed from this baseline. Do not spend current exam-prep time on either until core gaps are closed.

---

#### Keep asset budgets and actual asset value separate

Create a **Fixed asset budget journal** with the appropriate journal name/model, transaction type, date, asset/book and amount. Inspect the posting-profile defaults. Choose asset-budget-only transfer or asset-and-ledger-budget transfer according to the requirement, and reconcile the destination budget entries. The Delete existing entries option replaces existing budget records; inspect scope and retain a before/after export before using it. See [asset budgeting workflow](https://learn.microsoft.com/en-us/training/modules/manage-fixed-assets-finance/asset-budgeting). A 30,000 planned acquisition must remain a budget until an actual acquisition is posted; transferring it to budgeting does not create a supplier liability or depreciable asset balance.

For a split, create the destination asset/book, invoke the source book's split function with date, percentage and journal, then review/post the generated adjustments. A 25% split of an assumed 20,000 acquisition basis moves 5,000 to the new asset and leaves 15,000 on the original under this simple model; reconcile associated history and accumulated depreciation under the actual book rules. See [asset split and journal review](https://learn.microsoft.com/en-us/dynamics365/finance/fixed-assets/tasks/split-fixed-asset). A department transfer changes the supported ownership/dimension context; reclassification changes group/classification and can affect accounts/defaults. Neither should be substituted for a split merely to move a percentage of value. Test book status, dates and voucher rules before posting. **VERIFY CURRENT:** cross-company split/transfer is a separate preview capability with additional mappings and must not be assumed from the ordinary within-company example.

## Integrated scenarios

### Scenario 1: multi-company month end

A group uses one chart of accounts with legal-entity overrides, account structures and reporting currency. During close, teams reconcile AR/AP and banks, post accruals and allocations, revalue open currency and ledger balances, settle related ledger entries, consolidate subsidiaries and post controlled eliminations. The close workspace records dependencies and evidence; a late subsidiary follows a documented reopen/adjust/reconsolidate path.

### Scenario 2: subscription customer under credit pressure

A customer has recurring and milestone schedules plus deferred revenue. Aging and risk rules place a new order on hold. Collections records the dispute and promise to pay; an authorized reviewer releases only the supported order. A later price change affects future billing, termination stops the schedule at the approved date, and recognition entries reconcile to the remaining deferral balance.

### Scenario 3: capital purchase under budget control

A department budget is developed through planning, approved into a budget model and enforced by budget control. A PO for equipment passes funds availability; product receipt and three-way-matched invoice establish the liability and acquisition flow. The asset/book is placed in service, depreciated, transferred to another cost center, then sold through a free-text invoice with gain/loss reconciled to the ledger.

---

## Worked examples

These are original, simplified learning calculations, not local tax or accounting-policy advice. Assume one accounting currency and no tax, discounts or exchange rounding unless stated. Arithmetic was checked locally; Dynamics posting was not executed.

### 1. Allocate a shared service cost

Allocate 18,000 using headcounts of 12, 18 and 30. Total headcount is 60, so allocations are 3,600, 5,400 and 9,000. The destination debits total 18,000 and the source credit is 18,000: company profit does not change from this internal redistribution. Record basis date, departments and posting layer. Re-running the same allocation without controlling the source population can redistribute twice; balanced vouchers alone do not prove a correct run.

### 2. Revalue the remaining exposure once

A standalone GL monetary asset holds EUR 2,000 at USD 1.10/EUR, a USD 2,200 balance. At 1.15 its target is 2,300: unrealized gain 100. At the next valuation rate of 1.12, its target is 2,240: post a 60 loss relative to 2,300, leaving cumulative unrealized gain 40. Posting another 40 gain instead would overstate the balance by 100. An open customer invoice belongs in AR revaluation; do not also select its summary account in the GL run. This example omits settlement and reporting-currency entries deliberately.

### 3. A correct price can still fail three-way matching

Order 100 units at 50 each, receive 60, and select that receipt for an invoice for 80 units at 50, with no charges or discounts. Price agrees; quantity exceeds the selected receipt by 20. Two-way price matching alone does not detect that receipt mismatch. If instead 60 units are invoiced at 51, the price increase is 2%; compare it to the configured tolerance separately from the now-matching quantity. An approved invoice exception is a controlled decision, not evidence that the missing goods arrived.

### 4. Net first, then pay the residual

For an eligible customer/vendor pair in one company and currency, selected receivables total 12,000 and selected payables total 7,500. Net 7,500, leaving a customer receivable of 4,500 and no selected payable. The bridging account must reconcile. If the payable is already marked in a payment journal, stop and inspect the marking; do not assume a second netting run will safely repair the payment. Reversal must reopen the settled invoices and reverse the netting posting, preserving the audit trail.

### 5. Deferral schedule versus posted recognition

Bill 12,000 for January 1–December 31 with monthly full periods and Equal per period enabled. Each period is 1,000; after three **posted** recognitions, cumulative revenue is 3,000 and the remaining deferred balance is 9,000. A March 30 cutoff excludes a line ending March 31; March 31 includes it. A draft recognition journal has not reduced the posted deferral balance. Changing to day-based allocation or a partial first month invalidates the equal-1,000 assumption.

### 6. A PO reservation becomes an actual expense

Choose a teaching formula: revised budget minus posted actuals minus outstanding PO encumbrances. Start with 100,000 budget, 20,000 actuals and 30,000 encumbrances: 50,000 available. Invoice 10,000 of the reserved PO: actuals rise to 30,000 and the remaining encumbrance falls to 20,000, so availability remains 50,000. Keeping the original 30,000 reservation would double-count 10,000. A new 55,000 request exceeds availability by 5,000; configured permissions and thresholds determine the result. Check document, period and dimension scope before comparing reports.

### 7. Two asset books do not imply two identical depreciation policies

Acquire equipment for 24,000 with no residual value. For this full-year illustration, a 48-month straight-line corporate book gives 500/month and 6,000/year; an independently calculated 24-month tax book gives 1,000/month and 12,000/year. Derive acquisition if appropriate, but copying corporate depreciation would understate this example's tax-book depreciation by 6,000 after a year. After 12 corporate periods, book value is 18,000. A sale for 19,000 produces gain 1,000; scrap with no proceeds produces loss 18,000. Reconcile removal of 24,000 cost and 6,000 accumulated depreciation in either case. Real tax methods/conventions require the applicable policy.

### 8. Eliminate balances without hiding a mismatch

Company A records an intercompany receivable of 40,000; Company B records a payable of 39,500 in the same reporting currency. The unexplained 500 difference needs investigation—timing, missing document, conversion or an error. After correction to equal 40,000, an elimination removes 40,000 of both reciprocal balances from consolidated reporting while retaining each company's source history. A balancing plug that hides the 500 does not establish a valid reconciliation.

## Useful articles and a release-reading habit

- **[Financial tags and reporting](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2023/04/26/financial-tags-flexible-reporting-and-analytics-capabilities-without-the-overhead-of-dimensions/)** — Kristi Slininger, April 26, 2023. Useful design rationale: compare a reusable cost-center dimension with a high-cardinality purchase reference. Write down posting-control, reporting and retention needs before choosing. Its first-release support and future plans are historical; current tag documentation supplies validation and supported-document details.
- **[Agentic ERP capabilities](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/09/23/build-the-future-of-agentic-erp-with-new-microsoft-dynamics-365-capabilities/)** — Sameer Verma, September 23, 2026. Read the Finance section as a mixture of available and planned capabilities through March 2027. Build an exception-review worksheet for an invoice/reconciliation suggestion: evidence, entity, amount, approver and reversal. Do not infer that every announced journal or agent capability is generally available or an MB-310 objective.
- **[Always-on roadmap transition](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/08/25/one-always-on-roadmap-dynamics-365-power-platform-and-dataverse-join-the-ai-at-work-roadmap/)** — Richard Riley, August 25, 2026. New disclosures move to the [AI at Work roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap) from September; [Learn release plans](https://learn.microsoft.com/en-us/dynamics365/release-plans/) remain historical. The announced Release Planner retirement is November 15. Track feature ID, product, status, estimate, region and a confirming product-document link. A roadmap estimate alone does not prove tenant availability.

## Hands-on labs

1. **Ledger design:** Build a COA/dimension/account-structure matrix with an advanced rule, defaults, a derived dimension and a financial-tag use case; test six valid/invalid entries.
2. **Journal and currency:** Configure a journal name, voucher policy, posting restriction, reversal and Excel template; post foreign-currency entries, revalue and reconcile the vouchers.
3. **Bank and close:** Configure/import a statement and matching rules; resolve exceptions, build a close schedule, allocate a balance and storyboard consolidation/elimination.
4. **Tax and receivables:** Configure a small tax intersection and posting profiles; create invoices, credit/prepayment/payment, revaluation and settlement, then inspect ledger effects.
5. **Credit and subscription:** Model risk/hold/release and collections activity; create a billing schedule and revenue/expense deferral with modification and termination cases.
6. **Payables and expenses:** Process PO and non-PO invoices, matching discrepancy, proposal/payment, prepayment and an expense report with policy exception.
7. **Budgeting:** Configure basic budget entry, transfer, funds-availability control and a planning process with hierarchy, stages, scenarios and allocation.
8. **Fixed assets:** Configure a group, two books and depreciation; acquire, split/transfer, run multi-period depreciation and dispose by sale or scrap with reconciliation.

9. **Ambiguous bank match and netting:** Create two synthetic bank entries of the same amount with different references; test automatic versus manual-review matching. For a separate eligible customer/vendor pair, trace netting, residual payment and reversal. Record marked-transaction exclusions.
10. **Reconciliation workbook:** Reproduce the eight examples, attach expected debit/credit totals and explain each failure. Then validate one example in a disposable Finance environment, recording version, feature state, entity, dates, document IDs and vouchers. Local arithmetic is preparation for that test, not a substitute for it.

For every lab retain expected/actual outcomes, a negative case and correction evidence. These labs have not been executed in a tenant by this review.

## Knowledge checks with explained answers

Original learning prompts; no recalled exam items. Try each before opening its answer.

1. **When should a requirement become a financial dimension rather than a financial tag?** Use a dimension for account-structure and ledger reporting needs; use a tag for suitable transaction detail. Fixed-list tags can validate entries, so “tags never validate” is outdated.
2. **How do account structures and advanced rules divide validation work?** The account structure defines base segments/combinations; advanced rules add conditional requirements. Test both together.
3. **Which sources and precedence can supply a default dimension?** Master records, documents and templates can supply defaults; derived dimensions supply dependent values. Trace the actual entry path and override rules, then validate the final combination.
4. **Distinguish accounting, reporting and transaction currency.** Transaction currency denominates the document; accounting currency is the company ledger basis; reporting currency is an additional configured reporting basis.
5. **What produces unrealized versus realized exchange differences?** Revaluation adjusts an open exposure without settlement; realized differences arise under settlement/payment rules. Avoid duplicate subledger and GL calculation.
6. **When is a posting layer preferable to another legal entity?** A posting layer separates reporting effects within one company. A distinct legal entity represents a separate company and its operational obligations.
7. **Which journal-name and voucher controls support auditability?** Journal type/defaults, voucher numbering, account restrictions, approval and posting rights together preserve a traceable authorized entry.
8. **Why does Excel entry not bypass journal validation?** Publishing/importing spreadsheet rows creates data subject to Finance permissions, validation and posting controls; it is not a separate accounting engine.
9. **What failure evidence must batch posting retain?** Keep selected scope, run ID, posted vouchers, rejected records and errors. Retry only the remaining work after checking for already-posted entries.
10. **Distinguish bank statement import, matching, reconciliation and ledger posting.** Import loads evidence, matching proposes associations, reconciliation verifies the account, and posting records permitted new accounting. Inspect each outcome separately.
11. **How do payment proposal, journal, format and bank confirmation relate?** Proposal selects items; journal forms the payment accounting set; format creates the bank message; confirmation/reconciliation establishes what cleared.
12. **Which assumptions make cash-flow forecasts misleading?** Missing sources, optimistic collection dates, stale refreshes, wrong liquidity accounts and unmodeled timing can make a mathematically correct forecast unreliable.
13. **What sequence makes a close repeatable and auditable?** Order dependencies, assign owners, reconcile subledgers, post adjustments, validate reports and control period access. Retain reopen and rerun evidence.
14. **Why reconcile subledgers before consolidation?** Consolidation cannot repair an unexplained source mismatch; reconcile company balances before translating and eliminating them.
15. **What does an elimination remove, and what should it preserve?** Remove reciprocal intercompany effects at group level while preserving company source transactions and evidence of each elimination.
16. **How do tax code, group, item group, period, authority and posting group interact?** Groups determine applicable codes; codes define calculation; posting groups route ledger entries; settlement periods and authorities organize reporting/payment. Validate local rules.
17. **How does a posting profile connect a customer/vendor transaction to the ledger?** The configured profile maps the customer/vendor transaction to the relevant control and related accounts; reconcile it to the subledger.
18. **What evidence supports a credit-hold release?** Keep hold reason, exposure, supporting facts, authorized approver and the limited release scope; a release is not a general credit-policy waiver.
19. **What is the difference between aging and a collections process?** Aging classifies balances at a date. Collections coordinates follow-up, dispute resolution and recovery using those balances and context.
20. **How should a write-off remain authorized and traceable?** Apply documented approval and configured write-off accounts; retain invoice, settlement and reason history rather than deleting the debt.
21. **Distinguish recurring invoice and subscription billing schedule.** A recurring invoice repeats document creation; a subscription schedule additionally models contract timing, pricing, holds and termination.
22. **How does deferral separate billing from recognition?** Billing creates the receivable/payable document; the deferral schedule and posted recognition move the amount into the relevant period.
23. **What happens to recognition after a contract modification or termination?** Reconcile recognized history, future schedule and credits under the actual modification/reversal settings. Terminating billing does not by itself prove correct accounting.
24. **Compare two-way and three-way invoice matching.** Both compare price to the PO; three-way also compares invoice quantity to selected receipts. Total-price and charge checks are separate settings.
25. **Why are vendor bank changes a high-risk control point?** A changed bank account can redirect an otherwise valid payment. Separate maintenance from release and verify the change independently.
26. **How do centralized payments affect company and settlement boundaries?** Trace payment company, invoice company, settlement and intercompany accounts; centralized payment does not collapse the legal entities.
27. **Which expense-policy failures need a supported exception path?** Missing receipts, personal spend, mileage limits and late submissions need a documented return/approval route with posting and privacy evidence.
28. **Distinguish budget model, code, register entry and transfer rule.** Model organizes the budget; code describes entry type/workflow; register entry changes budget amounts; transfer rules constrain movement.
29. **Which calculation and scope choices control funds availability?** The formula, periods, dimensions, document filters, reservation handling and override permissions determine the result; active rules also require control turned on.
30. **How do planning hierarchy, process, stage and scenario differ?** Hierarchy organizes responsibility, process orchestrates planning, stage controls progress, and scenario labels the values such as request versus approved.
31. **Distinguish asset, group, book and derived book.** Asset is the item, group supplies defaults, book is a valuation basis, and a derived book receives selected transactions from a primary book.
32. **How do depreciation profile and convention affect timing?** Profile chooses the method while dates/convention determine eligible periods and prorating; use the actual book settings before predicting a proposal.
33. **Which acquisition routes connect assets to source documents?** PO, asset journal, inventory and project routes retain different source trails. Verify the correct book, cost, capitalization and voucher.
34. **How should a transfer differ from a reclassification or split?** Transfer changes supported ownership/dimension context, reclassification changes classification, and split distributes value/history; reconcile before and after.
35. **Which accounts change on disposal by sale versus scrap?** Both remove cost and accumulated depreciation. Sale also records proceeds and gain/loss; scrap has no sale proceeds.
36. **Which removed or adjacent topics should not displace August 2026 objectives?** Cost management was removed; asset leasing and wider agent announcements are adjacent. Prioritize the published August 14 objectives.
37. **Does a tag always accept arbitrary text?** No. Normal list types do, but Fixed list/Fixed custom list validate membership from version 10.0.44.
38. **Did Microsoft deprecate financial dimensions themselves?** No. The September notice concerns the optional financial-dimension import service.
39. **Why can a balanced allocation still be wrong?** Wrong source scope, basis date or repeated processing can preserve totals while misallocating cost.
40. **Why is the second GL revaluation adjustment minus 60 in example 2?** The current balance is 2,300 and target is 2,240; use their difference, not the cumulative 40 gain from original cost.
41. **Why is an amount-only bank match weak evidence?** Two documents may share an amount; inspect references and require manual review of ambiguity.
42. **When should netting precede payment work?** Run it before payment journal creation; already-included transactions are excluded from the documented netting flow.
43. **Does a recognition journal prove revenue posted?** Only after successful posting; auto-post can be disabled. Check schedule line and voucher status.
44. **Can activating budget rules alone block an overspend?** No. Budget control must also be turned on and the document/dimensions must be in scope.
45. **Why does availability stay 50,000 when the PO is partly invoiced?** Actual expense increases 10,000 while the outstanding reservation is relieved by the same amount.
46. **Can derived depreciation calculate a different tax method?** No. It copies the primary amount; use separate depreciation computation when methods differ.
47. **Can a 500 intercompany mismatch be eliminated without investigation?** A plug can hide it, but does not reconcile it. Establish and correct the cause first.
48. **Does a March 2027 roadmap horizon establish present availability?** No. Confirm the individual feature status, product documentation and tenant rollout before designing a lab around it.

---

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

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one primary route, build several source-document-to-ledger journeys, and add another resource only for a measured gap.

### Focused reading and evidence route

Select MicrosoftLearning’s [voucher breakdown lab](https://microsoftlearning.github.io/MB-310-Microsoft-Dynamics-365-Finance/Instructions/Labs/LP3%20Lab%20-%20Breakdown%20of%20voucher.html) for payables-to-ledger reasoning. Allow about 60–90 minutes for reading and an original worksheet that predicts taxable bases, tax by line, offset accounts, balanced totals and the evidence needed before and after posting; this editorial range includes one deliberately wrong tax-group mapping and its correction. The February 10, 2026 change record is visible, but the walkthrough assumes USMF demo records and older dates. Reconcile those prerequisites with your sandbox and current Finance documentation. Exclude its expired-certificate bypass workaround. The public textual procedure was read, not executed; screenshots, journal postings and tax compliance outcomes were not independently verified.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MB-310 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-310) | Free | 1–2 hours to map objectives and the August change log |
| [Configure financial management](https://learn.microsoft.com/en-us/training/paths/set-up-configure-financial-management-work-general-ledger/) | Free | 16 modules; allow 35–55 hours with transactions/reconciliation (editor estimate) |
| [Manage accounts receivable](https://learn.microsoft.com/en-us/training/paths/implement-accounts-receivable-credit-collections-revenue-recognition/) | Free | 8 modules, including removed cost-management material; allow 18–28 hours with selected practice (editor estimate) |
| [Manage accounts payable](https://learn.microsoft.com/en-us/training/paths/implement-manage-accounts-payable-expenses/) | Free | 6 modules including OCR and Project Operations expenses; allow 16–24 hours with selected practice (editor estimate) |
| [Perform budgeting and forecasting](https://learn.microsoft.com/en-us/training/paths/manage-budgeting/) | Free | 3 modules; allow 8–12 hours with all three budgeting capabilities (editor estimate) |
| [Administer fixed assets and inventory](https://learn.microsoft.com/en-us/training/paths/manage-fixed-assets/) | Free | 4 modules; allow 10–16 hours with lifecycle transactions (editor estimate) |
| [MB-310T00-A: Manage Financial Operations with Dynamics 365 Finance](https://learn.microsoft.com/en-us/training/courses/mb-310t00) | Paid/provider-dependent | 4 days; English |
| [Official MicrosoftLearning MB-310 labs](https://github.com/MicrosoftLearning/MB-310-Microsoft-Dynamics-365-Finance) | Free; MicrosoftLearning license applies | 10–20 hours selected labs; verify each lab against the current blueprint and tenant UI |
| [Free MB-310 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/d365-functional-consultant-financials/practice/assessment?assessment-type=practice&assessmentId=107&practice-assessment-type=certification) | Free | 45–90 minutes plus review |
| [Dynamics 365 Finance documentation](https://learn.microsoft.com/en-us/dynamics365/finance/) | Free | 15–35 hours selected implementation and troubleshooting references |
| [Pluralsight: Microsoft Dynamics 365 path](https://www.pluralsight.com/paths/microsoft-dynamics-365) | Subscription/trial | 6 published courses, 5 hours rounded (5h03 from components); broad product primer, Finance/Project Operations course still listed as coming soon |
| [Udemy: Dynamics 365 Finance & Operations—Financials Part 1](https://www.udemy.com/course/d365-financeoperations-overview-and-financials-part-1/) | Paid | 4h08, 10 sections/24 lectures; November 2024 update confirmed in public indexed metadata, direct fetch blocked; foundation only |
| [MeasureUp MB-310 practice test](https://www.measureup.com/microsoft-practice-test-mb-310-microsoft-dynamics-365-finance.html) | Paid; free demo | 103 questions listed; February 2023 update, older objectives. Allow 2–4 hours with review (editor estimate); no paid questions inspected |
| [Microsoft Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner login required | Use the four-day official-course pattern for planning; verify the signed-in event’s exact start/end time |

The five paths list **37 distinct modules** (16 + 8 + 6 + 3 + 4). Their current public pages do not expose a total runtime, so the earlier 48h30 sum is withdrawn. Cost management remains in the receivables path; expense modules reference Project Operations. Use the current blueprint to select content. The table's study-hour ranges are editorial estimates, not provider runtimes. Allow roughly **100–160 hours** for a new Finance practitioner to complete a primary route, build the labs and remediate the Practice Assessment. No exact O’Reilly or Whizlabs MB-310 product was established in the earlier catalog review; those providers were not comprehensively searched again here. Partner events require signed-in verification and the direct Practice Assessment fetch returned no substantive body. Reject recalled live content, “valid questions,” pass guarantees and any practice source that cannot explain its authorship and update baseline.
