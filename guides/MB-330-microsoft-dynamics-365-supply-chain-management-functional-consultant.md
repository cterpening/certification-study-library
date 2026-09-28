---
exam_code: MB-330
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-330
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-27
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-27
---

# MB-330 Microsoft Dynamics 365 Supply Chain Management Functional Consultant Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide was checked against the June 20, 2025 official objective baseline and cited public sources on September 27, 2026; all 101 October objectives were separately mapped without accepting the future baseline early. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#mb-330-coverage-record). The [official MB-330 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-330) is authoritative.

**Current baseline:** Skills measured as of June 20, 2025.<br>
**Upcoming blueprint change (checked September 27, 2026):** The English blueprint changes October 21, 2026. Minor revisions cover inventory activities, landed costs, sales features, warehouse processes and master-plan execution. Domain weights are unchanged. The revised plan-management objective explicitly names Planning Optimization. Use the [official change log](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-330) for the revised wording; the map below preserves the June baseline.<br>
**Lifecycle:** The [Dynamics 365 Supply Chain Management Functional Consultant Associate credential](https://learn.microsoft.com/en-us/credentials/certifications/d365-functional-consultant-supply-chain-management/) is active. The exam is 100 minutes, offered in English and Japanese, has no announced retirement date, and offers a free Practice Assessment.<br>
**Freshness note:** The guide retains the June 2025 baseline for appointments before the October revision. Recheck product documentation for Planning Optimization, Warehouse Management mobile app, Copilot and other fast-moving behavior.<br>
**Official source:** [MB-330 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-330)

## How to use this guide

For each requirement, trace one complete flow:

1. product/released-product, variant, dimensions, units and commercial/cost defaults;
2. source demand or supply document and reservation/availability state;
3. inventory transactions, physical update, financial update and costing;
4. quality, warehouse, transportation or asset-maintenance execution;
5. planning inputs, planned action and firmed supply;
6. exception, workflow/approval, telemetry and recovery;
7. downstream order, inventory, cost and customer/vendor evidence.

Build with synthetic data in a nonproduction environment. Draw inventory transaction state and warehouse work state separately; many errors come from assuming an order line, reservation, work line and on-hand quantity are the same thing.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Implement product information management | 25–30% | Can you create a reusable product model whose identity, dimensions, units, cost and trade behavior remain valid after release? |
| Implement inventory and asset management | 20–25% | Can you maintain accurate on-hand/cost/quality state and operate equipment maintenance? |
| Implement and manage supply chain processes | 15–20% | Can you run controlled procurement, landed-cost and sales lifecycles? |
| Implement warehouse management and transportation management | 20–25% | Can you translate physical flows into locations, waves, work, mobile steps, loads, routes and freight settlement? |
| Implement master planning | 10–15% | Can you configure coverage and interpret/firm supply recommendations without creating instability? |

---

## 1. Implement product information management

### Model products and variants

A product definition is shared; a **released product** makes it usable in a legal entity with company-specific settings. Product masters generate variants from color, configuration, size, style and, where enabled, version dimensions. Define which combinations are valid, how variant IDs/names are generated and when release occurs. Product templates copy supported setup; audit the copied fields instead of assuming the new item is correct.

Product lifecycle states govern whether a product can be used in supported processes at stages such as draft, active or obsolete. Category hierarchies classify products for procurement, retail/sales or reporting according to hierarchy purpose. Attributes describe categorized products and can drive search or process information; they do not replace inventory dimensions.

A bill of materials defines components and quantities, while a BOM version adds site, dates, quantity range and approval/activation context. Even for MB-330 rather than manufacturing-depth MB-335, understand how a sales, planning or costing flow depends on a valid active BOM version.

> **Related item:** A product dimension creates a variant; a storage dimension identifies where inventory is held; a tracking dimension identifies batch/serial traceability; an attribute is descriptive. The names can look similar, but their transaction behavior differs.

### Configure inventory behavior

Storage, tracking and product dimension groups define which inventory dimensions are active and when they are physically/financially tracked. Item model groups define core inventory and costing behavior. Reservation hierarchies determine which dimensions are specified above and below the Location level of the reservation hierarchy; unit-sequence groups translate handling units such as each, case and pallet for warehouse work.

Choose these before transacting. Changing dimension or model-group behavior later can be constrained or require migration. Test receiving, reservation, picking, batch/serial capture, transfer and financial update. Default order settings define site/warehouse, lead time, order quantity and order-type defaults by sales, purchase and inventory context.

Bar codes and GTIN identify products/units for scan processes. Unit conversions must specify the correct from/to unit and product scope; rounding and catch-weight behavior can create fulfillment discrepancies. Warehouse product filter codes help constrain valid products during supported warehouse operations.

### Check identity, reservation and units together

The [version dimension](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-dimensions) requires appropriate configuration and has unsupported integration scenarios; do not assume every dimension is interchangeable in every process. A [lifecycle state](https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-lifecycle) with **Is active for planning = No** excludes the item from master planning and BOM-level calculations. Other transaction restrictions depend on the configured process policies. An obsolete label alone does not prove every transaction is blocked.

With [flexible warehouse reservation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/flexible-warehouse-level-dimension-reservation), dimensions above Location normally bind demand; the warehouse selects dimensions at or below it. A batch-below hierarchy normally leaves batch selection to warehouse work, but **Allow reservation on demand order** can enable batch or license-plate reservation on the order. This is not a universal switch for location or serial number. When that exception reserves a batch on demand, picking allocation bypasses location directives for the committed dimensions; the batch cannot simply be changed during a picking exception. Inspect existing reservations and open work before changing setup.

A WMS-enabled product needs a [unit sequence group](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/unit-measure-stocking-policies); its smallest unit must match the inventory unit, and multiple units require conversions. Variant-specific conversions require their own setup. Verify purchase, sales, inventory and scanned units independently.

**Worked example — cases versus each:** A PO buys three cases of 12 each at $48 per case. Receipt quantity is 36 each; commercial value is $144, equivalent to $4 per each before charges. Applying $48 to each produces $1,728. Record GTIN, scanned unit, conversion and price unit before blaming the cost model. A scanner reading the right item with the wrong packaging unit can still create the wrong receipt.

### Manage cost and commercial price

Costing versions hold planned or standard cost records with activation policy and dates. A standard-cost item uses active costs and posts variances when transaction cost differs. Separate calculation, pending cost, review and activation responsibilities. Inventory close and adjustment later settles/adjusts eligible inventory according to the item model.

Base purchase/sales prices, price groups and trade agreements solve different commercial pricing needs. Trade agreements can depend on customer/vendor, group, item, quantity, currency, unit and date; search order and concurrency matter. Test exact matches, overlapping agreements, conversion and expired records.

> **Related item:** Cost estimates inventory value and accounting; sales/purchase price controls commercial terms. Margin analysis connects them, but a trade-agreement change does not update the active standard cost.

---

## 2. Implement inventory, quality, and asset management

### Process and reconcile inventory

Inventory journals represent different movements: movement and adjustment change quantity/value with different offset logic; transfer journal moves dimensions without the richer shipment/receipt lifecycle of a transfer order; counting records observed quantity; item-arrival journals support inbound processing; BOM journal reports a simplified BOM consumption/production flow.

A transfer order provides ship and receive stages, in-transit visibility and delivery control. Select journal versus order from logistics and evidence requirements. Manual inventory blocking and batch-disposition codes can prevent reservation or issue of suspect stock. Explain exactly which processes each control blocks and how an authorized release occurs.

Inventory close settles issues to receipts and posts adjustments according to the item model; recalculation can update without closing the period. Define cut-off, sequence, negative inventory policy, exception review and reconciliation to the general ledger. ABC classification ranks items by a selected measure for differentiated control; it is an analysis input, not an automatic replenishment policy.

The October journal bullet no longer lists output journals. Retain older-baseline study notes as historical context, and practice the explicitly listed BOM, arrival, transfer, movement, adjustment and counting journals.

For periodic costing, [inventory close](https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/inventory-close) settles issues against receipts and can adjust their value. Recalculation can adjust value without settling transactions or closing the period. Review financial receipt completeness first; adjustments use the original posting accounts even if account setup has since changed. Reverse the latest close first when reopening multiple periods. The [costing FAQ](https://learn.microsoft.com/en-us/dynamics365/supply-chain/cost-management/inventory-costing-faq) distinguishes periodic valuation from standard-cost and moving-average behavior: do not promise the same settlement effect for every model.

### Govern quality

Quality associations define when a quality order is created for a reference process and item/site/test group conditions. Test groups, tests, instruments, outcomes and acceptable quality level form the inspection contract. A quality order records results and validation; quarantine orders manage separated inventory processing. Nonconformance records describe a quality failure, related type/problem, correction and charges.

Design trigger timing carefully: before receipt, after registration or at another supported event changes what can proceed. Connect failed results to inventory blocking/disposition, vendor/customer action and evidence. Avoid duplicate quality orders when warehouse and procurement events overlap.

### Separate the inspected quantity from the blocked quantity

[Inventory blocking](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-blocking) and [quality orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quality-orders) need separate evidence. For a manually created quality order, the quality-order quantity controls the block; sampling controls inspection. Automatic quality associations can use item sampling to determine the block, and supported **Full blocking** can block the complete source line. Combining status blocking and quality blocking can create overlapping exclusions and misleading expected receipts; inspect the transaction records before layering controls.

**Worked example — a 100-unit receipt:** Inspecting 10% means testing 10 units. In a supported basic quality association with Full blocking, all 100 units can be held. A manual quality order for 10 units blocks 10, even if the business intended to hold the whole receipt. Neither calculation establishes the warehouse configuration: prove which quantity can be reserved and shipped before validation and after pass/fail.

[Quality management for warehouse processes](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quality-management-for-warehouses-processes) creates sampling work into the quality location and can create quality-order work out after validation. The WMS-specific quality-association type does **not** support Full blocking. Design and test the required inventory-status/location controls if the business requires a complete receipt hold; moving a sample does not hold the remainder. Purchase registration via the mobile flow and registration through the web client/item-arrival journal have different work behavior: the latter can create quality orders without quality-item-sampling work. Inspect event, warehouse type and test group when diagnosing duplicates.

[Quarantine orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quarantine-orders) are a separate flow. For WMS-enabled warehouses, their supported processing is limited to sales returns. Do not prescribe the basic quarantine-order purchase flow for every advanced warehouse. In the basic flow, reporting a quarantine order as finished releases the inventory, while ending it performs the return movement; these are different states.

### Configure and operate asset maintenance

An asset type supplies defaults; an asset is the maintained equipment. Functional locations form the install/location hierarchy. Lifecycle models and states control valid transitions for assets, functional locations, requests and work orders. Work-order settings define types, jobs, stages, priorities and related behavior.

Maintenance requests capture reported need and can become work orders. Maintenance plans and rounds generate preventive work; reactive work starts from failure. Schedule work by worker, asset, tool and capacity, then register hours, items, expenses and counters as consumption. Asset loans track temporary replacement/loan flows. Reconcile maintenance execution to inventory consumption, cost and downtime evidence.

> **Related item:** Finance fixed assets track capitalization and depreciation; Supply Chain Asset Management operates equipment maintenance. An equipment record can relate to financial accounting, but the two asset models answer different questions.

A [work order](https://learn.microsoft.com/en-us/dynamics365/supply-chain/asset-management/overview/objects-and-work-orders) can contain jobs for multiple assets. A maintenance-calendar entry is not itself an executed work order. Automatic work-order generation from a [maintenance plan](https://learn.microsoft.com/en-us/dynamics365/supply-chain/asset-management/preventive-and-reactive-maintenance/schedule-maintenance-plans) requires both the plan-line auto-create setting and the scheduling dialog's **Auto create if specified on the line** setting. Capture generated entries, jobs and consumed inventory separately. Changing the asset-type/manufacturer/model criteria of a functional-location maintenance plan removes its related schedule entries; reschedule and review the new scope. Updating asset-type defaults does not automatically update every existing asset.

---

## 3. Implement and manage supply chain processes

### Run procure-to-receive

Vendor master data, categories, procurement catalogs and policies determine what users can request and from whom. A purchase requisition expresses internal demand; an RFQ compares offers; a purchase agreement records committed terms; a purchase order authorizes specific supply. Configure workflow and change management around value, category, legal entity and exception risk.

Vendor collaboration exposes supported PO, confirmation, invoice or consignment processes to external contacts; constrain identity and vendor scope. Consignment inventory is vendor-owned until ownership change. Registration records arrival and product receipt physically updates the PO/inventory. Over/under delivery tolerances, delivery schedules and charges should express commercial policy, not conceal quantity errors.

Vendor rebates accrue/settle an agreement according to eligible purchases. Vendor returns need disposition, return document, physical shipment and financial correction. Trace every exception from request → order → receipt/return → invoice boundary even though invoice accounting is deeper MB-310 territory.

For [consignment](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/consignment), a receipt establishes physical possession without transferring ownership or posting a general-ledger receipt. Enable and inspect the Owner tracking dimension. Posting the ownership-change journal creates the vendor issue and company receipt with a purchase order whose origin is Consignment; invoice that generated PO. Drafting the journal or moving vendor stock between locations does not establish company ownership.

### Implement landed cost

Landed cost represents long inbound journeys through voyages, shipping containers, legs and goods-in-transit processing. Configure voyage statuses, journey templates, tracking control center, cost type codes, auto-cost rules, estimation and tolerances. Add PO or transfer lines to the correct voyage/container and preserve quantities and dates through departure, in-transit, arrival and put-away.

Estimated costs allocate according to configured basis; actual freight/duty invoices can create adjustments. Over/under delivery must resolve operational quantity and cost. Reconcile voyage/container → goods in transit → received inventory → allocated costs → vendor/freight invoice.

The [landed-cost overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/landed-cost-overview) distinguishes purchase voyages from transfers. Transfer-order voyages require goods-in-transit processing to be disabled; their estimated-cost posting occurs when the transfer ships. In the purchase [goods-in-transit flow](https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/in-transit-processing), invoicing can establish ownership before arrival. The goods-in-transit and underdelivery warehouses must be non-WMS even when the destination uses WMS. Goods in transit are not pickable on-hand at the destination; use the dedicated receipt flow rather than a normal PO product receipt when GIT terms apply.

**Worked example — allocation basis:** A container carries item A weighing 200 kg and item B weighing 100 kg. Allocating $600 freight by weight assigns $400 to A and $200 to B. A quantity or value basis can produce a different result. Record the configured basis, units, estimated cost and actual invoice separately; a correct arithmetic total does not prove the allocation policy is correct.

For [landed-cost over/under delivery](https://learn.microsoft.com/en-us/dynamics365/supply-chain/landed-cost/over-under-transactions), the original purchase order is already invoiced. Preserve its quantity and resolve the difference through the configured tolerance and adjustment flow. Amount tolerance is evaluated at PO level before percentage tolerance at line level; outcomes can involve an inventory adjustment, another PO, a negative PO/credit, or manual resolution. Record the branch taken instead of editing the original receipt to hide the variance.

### Run order-to-delivery

Customer master, sales quotations and sales orders define demand. Sales agreements provide commitment terms; trade agreements provide prices/discounts. Reservations connect demand to inventory. Delivery schedules split a line across dates; sales returns reverse physical/financial flow with disposition. Sales groups and commissions assign commercial responsibility.

Intercompany orders create linked selling/buying-company documents; validate price, currency, dimensions, delivery and update sequence on both sides. Customer rebates accrue and settle eligible sales. ATP projects promise from supply/receipt timing, while CTP uses planning to consider capability/supply—confirm configuration and performance expectations. Product bundles sell a defined grouping while preserving supported component fulfillment behavior.

> **Related item:** Copilot can assist supported supply-chain decisions or summaries, but the blueprint’s scored domains remain process configuration and execution. Treat AI output as advice with source, permission, validation and fallback—not an inventory or planning system of record.

With [product bundles](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/product-bundles-setup), the customer sees the parent on confirmation/invoice while internal picking and packing use the exploded components. Configure the BOM and component base prices for revenue allocation; even a service-type component must have Stocked product enabled for this feature. Check the version-dependent bundle journals and the incompatibility with Revenue recognition before adopting the pattern.

---

## 4. Implement warehouse and transportation management

### Build the warehouse-control stack

Sites and warehouses establish inventory scope; zones, location types, formats and profiles describe physical layout and location capabilities. Inventory status separates usable, blocked or process-specific stock without changing product identity. Packing dimensions support container/pack calculations.

A **location directive** answers where to pick or put. A **work template** defines the sequence of work lines such as pick/put. A **wave template** groups released demand and invokes methods that create work, replenishment, containerization or labels. A **load** groups shipment work for transportation/warehouse execution. Debug in that order: order/release → shipment/load/wave → allocation → work template → location directive → work → mobile execution.

Work policies can suppress work creation for supported operations; work breaks divide work under conditions. Replenishment moves stock into picking locations based on demand or minimum/maximum patterns. Cross-docking directs inbound supply toward outbound demand. Cycle-count plans and threshold/manual work validate on-hand while warehouse activity continues.

Labels can identify product, wave, GS1 data segments or license plates. Design data source, format, printer routing, reprint and uniqueness. Containerization and packaging configuration groups items into containers subject to capacity and compatibility; test rounding, mixed items and partial shipments.

### Configure the mobile execution contract

Mobile-device menu items define tasks and work-creation behavior; menus expose them to workers. Display settings and step instructions reduce error. **Detours** let a worker temporarily perform another supported task and return to the original flow. Install/register the Warehouse Management mobile app according to current deployment guidance, then create warehouse workers, credentials, default warehouse and menu assignments with least privilege.

Test scanning, GS1 parsing, wrong item/location/license plate, short pick, damaged stock, offline/network interruption, duplicate submit and session recovery. A clean desktop transaction is not evidence the handheld flow works on the warehouse floor.

### Keep mobile identity and software support current

Use current [installation and connection guidance](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/install-configure-warehouse-management-app) and the [user-based authentication FAQ](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/warehouse-app-user-based-auth-faq). Microsoft recommends the interactive username/password authentication option; it is not an instruction to embed passwords in connection JSON. Microsoft-managed app registration can avoid a custom registration in the supported flow. Service-based authentication for this mobile app is deprecated. Device-code flow remains available for existing deployments but is not the recommended default; do not weaken tenant security to make an older tutorial work.

Broker authentication is optional for ordinary sign-in but required for the documented device-based Conditional Access/SSO scenarios, with supported app versions. An Entra sign-in and a warehouse worker are separate identities. **Log off** clears the server-side worker session; **Sign out** clears the Entra authentication but can leave the prior worker's server-side screen state. Test both during a shared-device handoff. The installation guide currently says Entra Shared Device Mode is unsupported; a physically shared handheld is not evidence that this identity feature is supported.

The [mobile release notes](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/warehouse-app-whats-new) list 4.1.6.0 on September 2, 2026, including a fix for spinner quantities above 20 resetting to zero. Version 4.1.5.0 fixed a timeout/gateway retry issue that could send a request twice and complete work twice. Test the installed build, entered quantity, request result and completed work before retrying after a lost response. Use disposable work in a sandbox; do not reproduce duplicates against live shipments.

The [support policy](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/warehouse-app-support-info-v3) says V3 support ended in May 2026. V4 and later releases adopt a rolling 12-month support window **starting May 1, 2027**, measured from Microsoft's defined publication date, not the later app-store arrival date. Older clients continuing to connect does not establish support eligibility. Keep a device/build/publication-date inventory, pilot scanner and identity tests, and deploy supported updates through the organization's device-management process.

### Plan transportation and reconcile freight

Shipping carriers/groups, services, route plans/guides and rate/route engines provide transport choices. Load and shipment planning connects order demand with equipment, carrier, route and appointments. Dock appointment scheduling controls arrival/departure capacity.

Generate freight bills/invoices from the supported process and reconcile expected versus actual freight manually or automatically. Keep accessorial charges, tolerance, unmatched bills and dispute ownership visible. Transportation selects/moves a load; warehouse work physically picks/packs/ships it. Coordinate their state transitions without collapsing them.

> **Related item:** Inventory management tracks quantity by dimension; advanced warehouse management creates work and license-plate/location execution; transportation management plans carrier movement. The same order touches all three, but each owns different state.

For [freight reconciliation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/transportation/reconcile-freight-transportation-management), match estimated freight-bill lines from the load with actual carrier-invoice lines. Account for discrepancies with configured reasons and posting accounts before approval and journal creation. A successful carrier-rate calculation does not prove that the carrier invoice matches or that every variance has an owner.

---

## 5. Implement master planning

### Configure coverage and planning behavior

Coverage groups supply shared rules; item coverage overrides them by item and dimension. Understand requirement, period and min/max patterns, order modifiers, vendor/lead time and calendars. Master plans define horizon and included demand/supply. **Positive days** control the interval in which existing supply can cover later demand; **negative days** contribute to tolerance for supply arriving after demand. Time fences limit how far actions, firming, capacity or messages operate.

Action messages recommend advancing, postponing, increasing, decreasing or canceling supply. Delay calculates lateness through the supply chain. Safety margins add time at receipt/issue/reorder boundaries. Period templates group recommendations. Safety-stock journals help calculate/propose minimum levels from history; review seasonality and service policy before applying.

### Interpret and firm a plan

Run the intended plan, inspect messages, pegging, delays and net requirements, and compare results to the Supply Schedule view. Planned purchase and transfer orders are recommendations until reviewed/firmed. Define auto-firming scope narrowly and monitor exception volume.

When results look wrong, inspect on-hand/reservations, demand dates, coverage dimensions/groups, lead times/calendars, positive/negative days, time fences, order modifiers, BOM/version and planned-order status before overriding. Use the documented Planning Optimization behavior and inspect the actual plan run, feature settings and diagnostics.

> **Related item:** Forecast is anticipated demand, safety stock is a buffer target, and safety margin is time protection. Adding all three without understanding interaction can amplify supply and inventory.

### Use Planning Optimization rules explicitly

The [legacy built-in engine is deprecated](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/new-master-planning-engine); Planning Optimization is required for new cloud deployments. The documentation does not give a full-removal date. Run [fit analysis](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planning-optimization-fit-analysis) for each legal entity and review documented differences even when no issues are reported: the analysis cannot detect every incompatibility. Auto-firming runs as a separate batch after planning and uses planned-order start/order date, not the requirement end date.

With [master-plan parameters](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/master-plans), a plan override takes precedence over inherited coverage settings. An override enabled with zero can disable a time fence rather than inherit it. Under the documented ordinary Planning Optimization positive-day behavior, zero positive days causes new supply rather than reuse of existing supply; do not use zero as a shortcut for unlimited matching. [Dynamic positive days](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/dynamic-positive-days) has a separate shared planning parameter: feature availability or default enablement does not prove the parameter is enabled. Within lead time it favors existing supply; outside lead time it can still reuse supply that falls within the positive-day interval.

For [Planning Optimization delay tolerance](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/delay-tolerance), negative days are calendar days and the engine always applies the dynamic calculation. The legacy **Use dynamic negative days** parameter does not change this behavior. Effective tolerance is `max(earliest replenishment date, demand due date) - demand due date + negative days`, with master-plan override, item coverage and coverage group precedence.

**Worked example — late receipt or new supply:** Use simple day numbers with no calendar exclusions or competing requirements. Today is day 0, earliest replenishment is day 6, demand is due day 2 and negative days is 2. Tolerance is `max(6, 2) - 2 + 2 = 6` days. Existing supply on day 8 is six days late and fits; day 9 is seven days late and does not. Inspect pegging and proposed supply in the actual plan; the arithmetic alone does not validate all plan settings.

### Protect confirmed promises without freezing everything

Two documented features require **10.0.48 build 10.0.2645.33 or later**, Planning Optimization and their feature settings:

- [CTP confirmed-date handling for line changes](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/optimize-confirmed-dates-for-ctp-line-changes) accounts for transportation changes such as delivery mode, warehouse or address. Verify the applicable CTP mode, dates and shipping constraints. Some dates in the article's example are inconsistent, so reproduce the behavior with a coherent test calendar rather than copying those dates.
- [Keep supply for confirmed demand](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/keep-supply-for-confirmed-demand) preserves eligible planned supply and pegging for open demand with a confirmed ship date. It is controlled per plan or run; inspect the effective flag in plan history. A later change of delivery-date control does not erase an existing confirmed date. Preserving planned supply is distinct from preserving received on-hand outside positive days, which needs **Keep received supply outside positive days** in coverage settings as well.

Preservation can reduce churn but retain excess shared supply when other demand is canceled. Review costs, capacity, excess quantity and messages; approved planned orders and freezing fences use different preservation criteria. Do not treat a confirmed date as permission to ignore a real shortage.

---

## Integrated scenarios

### Scenario 1: regulated inbound product

A variant product uses batch tracking, unit sequence and reservation hierarchy. A PO line joins a landed-cost voyage and arrives by container. Mobile receiving captures GTIN/batch/license plate; a quality association creates inspection and blocks failed inventory. Passing stock is put away by location directive/work, allocated cost is reconciled, and planning sees the usable receipt rather than the quarantined quantity.

### Scenario 2: customer order through advanced warehouse

A sales agreement and trade agreement price an order with delivery schedule. ATP/CTP informs promise date. Release creates shipment/load and wave; replenishment feeds pick faces, work templates/location directives create pick/put, mobile workers handle a short pick, container/GS1 labels print, carrier/rate/route is selected, dock appointment is honored and freight is reconciled.

### Scenario 3: equipment failure affects planning

A maintenance request becomes a reactive work order on an asset at a functional location. Scheduling checks worker/asset capacity and consumes a spare part. The inventory reduction and downtime change supply expectations; the planner analyzes delay/action messages, firms an approved transfer/purchase recommendation, and records recovery evidence without hiding the root cause with manual on-hand adjustment.

---

## Hands-on labs

1. **Product foundation:** Create/release a master and variants, lifecycle state, category/attribute, BOM/version, dimension/model groups, reservation hierarchy, unit sequence, conversions, defaults and GTIN.
2. **Cost and inventory:** Configure a cost version and trade agreement; process six journal types and a transfer order, block/release a batch, run ABC and storyboard close/reconciliation.
3. **Quality:** Configure association/test group/order/nonconformance and the appropriate basic or WMS quality flow; test pass, fail, partial sample, duplicate trigger and authorized disposition.
4. **Asset management:** Build functional location, asset/type/lifecycle, request/work order, preventive plan, scheduling/capacity/loan and consumption evidence.
5. **Procurement/landed cost/sales:** Run requisition/RFQ/agreement/PO/receipt/return, a voyage with cost variance, and quotation/order/reservation/delivery/return/intercompany paths.
6. **Warehouse/mobile:** Build layout/status, wave/work/location directives, replenishment/cross-dock/counting, labels/containerization and mobile menus/workers/detour; capture failure diagnostics.
7. **Transportation:** Configure carrier/service, route/rate, load/shipment and appointment; generate/reconcile a freight bill with tolerance exception.
8. **Planning:** Configure coverage, positive/negative days, margins/fences and plan; create demand, analyze pegging/messages/Supply Schedule, firm selected purchase/transfer orders and explain rejects.

9. **Receipt hold and handheld recovery:** Receive a disposable 100-unit order with a 10-unit sample. Compare manually created quality orders, basic Full blocking and WMS sampling work. Prove which stock can reserve/ship, validate pass/fail, and inspect release work. Test worker logoff/Entra sign-out and a controlled lost-response recovery; check server work before retrying. Record build and feature settings.
10. **Planning and cost evidence:** Reproduce the day-8/day-9 delay example, compare positive-day settings, and inspect the actual keep-supply flag and received-stock behavior. Reconcile the $600 allocation on a purchase voyage, then explain why a transfer voyage cannot use the same GIT-enabled configuration. Test both maintenance-plan auto-create controls and compare calendar entries with created work orders.

These ten labs require an appropriate nonproduction environment and permissions. If a feature/build/license is unavailable, record the gap and complete the paper trace without claiming execution. This review checked only synthetic arithmetic; no Dynamics environment, mobile app or business transaction was run.

## Knowledge checks with answers

1. **Why separate shared product from released product?** Shared identity is reused across companies; released-product settings determine company-specific transactions.

2. **Which dimension groups create variants, storage identity and traceability?** Product dimensions identify variants, storage dimensions identify inventory location/state, and tracking dimensions identify batch, serial or ownership where configured.

3. **How do reservation hierarchy and unit sequence affect warehouse execution?** The Location boundary determines demand versus warehouse allocation. Unit sequences and conversions determine handling quantities and license-plate behavior.

4. **When should lifecycle state prevent a transaction?** Use configured process policies for the intended restriction; Is active for planning independently controls master-planning/BOM inclusion.

5. **What makes a BOM version applicable?** Check product, site, effective dates, quantity range, approval and activation.

6. **Distinguish active standard cost, planned cost and trade-agreement price.** Active standard cost values the item; planned cost supports estimation; a trade agreement sets commercial price/discount conditions.

7. **When choose transfer journal versus transfer order?** Use a journal for an immediate supported dimension transfer; use an order for shipment, in-transit and receipt stages.

8. **Which transactions are physical versus financial inventory updates?** Registration and physical receipt differ; financial posting such as invoicing establishes financial update. Follow each transaction type and its posting profile.

9. **What does inventory close settle and adjust?** For periodic costing, it settles issues against receipts and adjusts eligible value. Recalculation adjusts without settlement; other valuation models differ.

10. **Compare manual blocking and batch disposition.** Manual blocking targets an inventory quantity/dimensions; batch disposition supplies availability rules for a batch. Inspect each affected process.

11. **How do quality association, order, quarantine and nonconformance differ?** Association triggers inspection, quality order records tests/validation, quarantine manages a separate isolation flow, and nonconformance records failure/correction.

12. **Which event should trigger inspection and why?** Choose a supported reference/event consistent with whether receipt, reservation or shipment must wait; web and mobile registration can create different work.

13. **Distinguish Finance fixed asset and SCM maintained asset.** A Finance fixed asset concerns capitalization/depreciation; an SCM asset concerns maintenance, jobs, failures and consumption.

14. **How do request, plan, schedule, work order and consumption connect?** Requests capture need; plans generate calendar entries; scheduling creates/orders work subject to settings/capacity; execution registers consumption.

15. **Compare requisition, RFQ, agreement and PO.** Requisition expresses internal demand, RFQ seeks offers, agreement records commitments, and PO orders specific supply.

16. **How is vendor-owned consignment converted to owned inventory?** Post an ownership-change journal; inspect vendor/company inventory transactions and the generated Consignment-origin PO before invoice.

17. **Which controls govern over/under delivery and vendor returns?** Apply the appropriate order or landed-cost tolerances, approval, return disposition and physical/financial correction. Keep the real variance visible.

18. **Trace voyage, container, goods in transit and landed-cost allocation.** Trace voyage and container through journey legs, ownership/GIT and destination receipt, then compare estimated allocation with actual invoices.

19. **How do sales agreement and trade agreement differ?** A sales agreement records a commitment; a trade agreement supplies price or discount rules.

20. **What dependencies make intercompany orders fail asymmetrically?** Company-specific customer/vendor/item setup, dimensions, currencies, prices and update order can succeed on one side and fail on the other.

21. **Compare ATP and CTP.** ATP considers availability over time; CTP invokes configured planning capability/supply logic. Confirm engine, mode, dates and feature prerequisites.

22. **Trace release, load, shipment, wave, work and mobile completion.** Inspect linked order, shipment/load, wave processing, allocation, work and mobile completion records; a completed screen is not proof of every downstream state.

23. **What do location directives and work templates each decide?** Location directives choose locations; work templates define the work sequence. Demand-specific reservations can constrain or bypass normal allocation.

24. **When do replenishment and cross-docking create different movements?** Replenishment feeds picking stock; cross-docking directs incoming stock toward matching outbound demand under configured rules.

25. **How should cycle counting coexist with open work?** Inspect open work and count policies, preserve quantity/dimension evidence, and resolve differences without silently invalidating picks.

26. **What do license plate, GS1 label and container each identify?** A license plate identifies a handling unit; GS1 segments encode identifiers/data; a container groups goods for packing/shipping.

27. **What must a mobile detour preserve?** Preserve the original work context and return path; verify transferred data and worker authorization.

28. **Which evidence diagnoses a short pick or duplicate scan?** Compare scanned item/unit/location/license plate, request timing and server work status before retrying or adjusting quantity.

29. **How do route/rate engines and route guides differ?** Engines calculate or retrieve rates/routes; configured route plans/guides constrain the intended journey and service.

30. **What is matched during freight reconciliation?** Estimated freight-bill lines are matched with actual carrier-invoice lines; reasons and accounts explain discrepancies before posting.

31. **Compare coverage group and item coverage.** Coverage groups provide shared rules; item coverage specializes item/dimension behavior, with master-plan overrides where configured.

32. **How do positive days and negative days change supply matching?** Positive days govern reuse of existing supply for later demand; negative days contribute to dynamic lateness tolerance. Planning Optimization is engine-specific.

33. **Distinguish time fences and safety margins.** Time fences bound planning behaviors/horizons; safety margins add time at process boundaries.

34. **Why inspect pegging before firming?** Pegging identifies which demand the supply covers, making duplicates, shortages and preserved excess visible before committing supply.

35. **When is auto-firming unsafe?** When inputs, lead times, coverage, dates, approvals or exception handling are unreliable, automatic commitments propagate those errors.

36. **Which current product areas require a documentation freshness check?** Check Planning Optimization/CTP, WMS app authentication/build/support, warehouse quality/reservation behavior and any preview or Copilot feature.

37. **What quantity and value follow from three cases of 12 at $48 per case?** Three cases contain 36 each; at $48 per case the order is $144, not $1,728.

38. **Does testing 10 units prove the whole 100-unit receipt is blocked?** A 10-unit sample does not prove a 100-unit hold. Basic Full blocking and WMS sampling have different support and transaction behavior.

39. **Can WMS quality associations use Full blocking?** The WMS-specific quality-association type does not support Full blocking; design and prove the required receipt hold with supported controls.

40. **Why test both worker logoff and Entra sign-out?** Log off clears the worker session, while Entra Sign out handles authentication; test both for handoff and do not assume Shared Device Mode support.

41. **Does supply on day 8 meet the worked delay tolerance, and what about day 9?** Six days is the computed tolerance: day 8 fits demand due day 2, while day 9 exceeds it under the stated assumptions.

42. **Does keeping confirmed supply automatically preserve all received on-hand?** Preserving confirmed planned supply and retaining received stock outside positive days need different controls; inspect the effective run and coverage settings.

43. **How should $600 freight be allocated across 200 kg and 100 kg?** For weight-based allocation, A receives $400 and B $200; independently verify policy, units and invoice variance.

44. **Which two settings generate work orders from the maintenance plan?** Both the plan-line auto-create setting and the scheduling dialog option must allow work-order creation; a calendar entry alone is insufficient.

---

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one primary route, build complete product-to-plan and order-to-warehouse journeys, and add another resource only for a measured gap.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MB-330 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-330) | Free | 1–2 hours to map the five domains |
| [Products and inventory](https://learn.microsoft.com/en-us/training/paths/configure-manage-products-inventory-dyn365-supply-chain-mgmt/) | Free | 7 hours 46 minutes in the September 1 listing (historical); 15–24 hours with practice |
| [Procurement and vendors](https://learn.microsoft.com/en-us/training/paths/configure-manage-procurement-vendors-dyn365-supply-chain-mgmt/) | Free | 13 hours 41 minutes in the September 1 listing (historical); select objectives and allow 20–32 hours with transactions |
| [Configure Asset Management](https://learn.microsoft.com/en-us/training/paths/configure-asset-management-dyn365-supply-chain-mgmt/) and [work with Asset Management](https://learn.microsoft.com/en-us/training/paths/work-asset-management-dyn365-supply-chain-mgmt/) | Free | 10 hours 45 minutes in the September 1 listing (historical); 18–28 hours with maintenance flows |
| [Landed cost](https://learn.microsoft.com/en-us/training/paths/setup-work-landed-cost-dyn365-supply-chain-mgmt/) | Free | 2 hours 53 minutes in the September 1 listing (historical); 6–10 hours with voyage/cost reconciliation |
| [Warehouse management](https://learn.microsoft.com/en-us/training/paths/configure-work-warehouse-management-dyn365-supply-chain-mgmt/) | Free | 5 hours 59 minutes in the September 1 listing (historical); 15–25 hours with mobile work/failure tests |
| [Transportation management](https://learn.microsoft.com/en-us/training/paths/configure-work-transportation-mgmt-dyn365-supply-chain-mgmt/) | Free | 1 hour 43 minutes in the September 1 listing (historical); 5–8 hours with load/freight practice |
| [Master planning](https://learn.microsoft.com/en-us/training/paths/master-planning-supply-chain-management/) | Free | 7 hours 20 minutes in the September 1 listing (historical); 14–22 hours with planning diagnostics |
| [MB-330T00-A Conceptualize Supply Chain Management course](https://learn.microsoft.com/en-us/training/courses/mb-330t00) | Paid/provider-dependent | 5 days |
| [MicrosoftLearning MB-330 labs](https://github.com/MicrosoftLearning/MB-330-Microsoft-Dynamics-365-Supply-Chain-Management) | Free; MIT | 15–30 hours suggested practice; repository README reviewed, individual handouts not reviewed or run |
| [Free MB-330 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/d365-functional-consultant-supply-chain-management/practice/assessment?assessment-type=practice&assessmentId=73&practice-assessment-type=certification) | Free | 45–90 minutes suggested allocation; signed-in questions not reviewed |
| [Supply Chain Management documentation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/) | Free | 15–40 hours selected implementation/troubleshooting |
| [Udemy advanced warehouse management Part 1](https://www.udemy.com/course/mb330-d365-fo-advance-warehouse-management-part1/) | Paid | Current retrieval blocked; July 2024 update was an earlier observation. Check current runtime, app build and coverage before purchase |
| [MeasureUp MB-330 practice test](https://www.measureup.com/microsoft-practice-test-mb-330-microsoft-dynamics-365-supply-chain-management.html) | Paid; free demo | Public listing: 154 questions, last updated March 2023; obsolete MB-300 prerequisite statement and unverified October coverage. No paid questions reviewed |
| [Microsoft Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner login required | Use the five-day course pattern for planning; signed-in event start/end times control |

The September 1 durations sum to **50 hours 7 minutes** across eight paths; this review checked landing pages, not every module or a current total. Treat these timings as historical planning observations, not freshly verified runtimes; the full five-day syllabus contains additional manufacturing and adjacent modules, so select against the blueprint. Allow roughly **120–190 hours** for a new practitioner to complete a primary route, build the labs and remediate assessment gaps. No exact current MB-330 Pluralsight, O’Reilly or Whizlabs product was independently verified. Question-bank-only listings and “guaranteed pass” claims were excluded; reject recalled live content and unexplained bulk questions.

### Useful blog reading with a task

- **Sameer Verma, September 23, 2026 — [new Dynamics 365 ERP capabilities](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/09/23/build-the-future-of-agentic-erp-with-new-microsoft-dynamics-365-capabilities/).** Read the SCM section to connect a supplier-proposed PO delay with downstream sales, production, transfers and projected inventory. Create a table of affected demand, evidence, proposed response and approving owner. Procurement impact analysis and Supplier Engagement are described as public previews; dynamic item placement is forthcoming. Use the exercise without requiring an agent deployment. The broader roadmap includes future capabilities through March 2027 and does not redefine MB-330 objectives. Allow 30–45 minutes for reading and a paper trace.
- **Michael Fruergaard Pontoppidan and Denis Conway, February 16, 2024 — [warehouse mobile interaction improvements](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2024/02/16/optimizing-warehouse-management-unveiling-the-power-of-d365-warehouse-mobile-app-version-2-1-23/).** Use this historical article to design a scanner, text-size, back-navigation and shift-handoff test matrix. Cross-check its authentication advice and app version against the current FAQ, release notes and support policy above; do not deploy 2.1.23 or restore device-code flow merely because the article describes it. Allow 30–45 minutes for analysis, plus environment-dependent test time.

Only the relevant public article text was reviewed; linked videos, claimed customer benefits and preview deployment were not tested. Add a blog when it teaches a specific decision, failure case or exercise backed by current product documentation, rather than adding another general link.

## Final readiness checklist

- [ ] I can configure/release products, dimensions, reservation/unit behavior, prices and costs and trace their effects.
- [ ] I can reconcile inventory journals/orders, close/adjustment, blocking, quality and asset-maintenance consumption.
- [ ] I can run procurement, landed-cost and sales/intercompany lifecycles with workflow and exception evidence.
- [ ] I can trace order release through shipment/load/wave/work/location/mobile/container/label and recovery.
- [ ] I can configure transport carriers/routes/rates/appointments and reconcile freight.
- [ ] I can configure coverage/plans/days/messages/fences/margins, diagnose results and firm appropriate supply.
- [ ] I completed all three scenarios and ten labs with failure-path evidence.
- [ ] I rechecked the current blueprint, lifecycle, Practice Assessment and fast-moving product docs before scheduling.

## Source notes

The accepted June 20, 2025 baseline remains the reference for earlier appointments; all 101 published October 21 objectives were separately mapped in the [deep-review record](../docs/research/2026-09-27-mb-330-deep-review.md). Microsoft Learn paths, product docs and MIT-licensed course labs support behavior but may include adjacent content or UI drift. Commercial assessment/training is optional and never defines scope. All questions here are original and conceptual; no exam dumps or recalled items were used.
