---
exam_code: MB-330
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-330
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# MB-330 Microsoft Dynamics 365 Supply Chain Management Functional Consultant Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide was checked against the June 20, 2025 official objective baseline and cited public sources on September 1, 2026. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#mb-330-coverage-record). The [official MB-330 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-330) is authoritative.

**Current baseline:** Skills measured as of June 20, 2025.<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 1, 2026.<br>
**Lifecycle:** The [Dynamics 365 Supply Chain Management Functional Consultant Associate credential](https://learn.microsoft.com/en-us/credentials/certifications/d365-functional-consultant-supply-chain-management/) is active. The exam is 100 minutes, offered in English and Japanese, has no announced retirement date, and offers a free Practice Assessment.<br>
**Freshness note:** The blueprint is more than a year old but remains Microsoft’s published authority. Recheck product documentation for Planning Optimization, Warehouse Management mobile app, Copilot and other fast-moving behavior.<br>
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

A product definition is shared; a **released product** makes it usable in a legal entity with company-specific settings. Product masters generate variants from product dimensions such as size, color, style or configuration. Define which combinations are valid, how variant IDs/names are generated and when release occurs. Product templates copy supported setup; audit the copied fields instead of assuming the new item is correct.

Product lifecycle states govern whether a product can be used in supported processes at stages such as draft, active or obsolete. Category hierarchies classify products for procurement, retail/sales or reporting according to hierarchy purpose. Attributes describe categorized products and can drive search or process information; they do not replace inventory dimensions.

A bill of materials defines components and quantities, while a BOM version adds site, dates, quantity range and approval/activation context. Even for MB-330 rather than manufacturing-depth MB-335, understand how a sales, planning or costing flow depends on a valid active BOM version.

> **Related item:** A product dimension creates a variant; a storage dimension identifies where inventory is held; a tracking dimension identifies batch/serial traceability; an attribute is descriptive. The names can look similar, but their transaction behavior differs.

### Configure inventory behavior

Storage, tracking and product dimension groups define which inventory dimensions are active and when they are physically/financially tracked. Item model groups define core inventory and costing behavior. Reservation hierarchies determine which dimensions are specified above and below the warehouse-reservation boundary; unit-sequence groups translate handling units such as each, case and pallet for warehouse work.

Choose these before transacting. Changing dimension or model-group behavior later can be constrained or require migration. Test receiving, reservation, picking, batch/serial capture, transfer and financial update. Default order settings define site/warehouse, lead time, order quantity and order-type defaults by sales, purchase and inventory context.

Bar codes and GTIN identify products/units for scan processes. Unit conversions must specify the correct from/to unit and product scope; rounding and catch-weight behavior can create fulfillment discrepancies. Warehouse product filter codes help constrain valid products during supported warehouse operations.

### Manage cost and commercial price

Costing versions hold planned or standard cost records with activation policy and dates. A standard-cost item uses active costs and posts variances when transaction cost differs. Separate calculation, pending cost, review and activation responsibilities. Inventory close and adjustment later settles/adjusts eligible inventory according to the item model.

Base purchase/sales prices, price groups and trade agreements solve different commercial pricing needs. Trade agreements can depend on customer/vendor, group, item, quantity, currency, unit and date; search order and concurrency matter. Test exact matches, overlapping agreements, conversion and expired records.

> **Related item:** Cost estimates inventory value and accounting; sales/purchase price controls commercial terms. Margin analysis connects them, but a trade-agreement change does not update the active standard cost.

---

## 2. Implement inventory, quality, and asset management

### Process and reconcile inventory

Inventory journals represent different movements: movement and adjustment change quantity/value with different offset logic; transfer journal moves dimensions without the richer shipment/receipt lifecycle of a transfer order; counting records observed quantity; item-arrival and output-order journals support inbound/outbound processing; BOM journal reports a simplified BOM consumption/production flow.

A transfer order provides ship and receive stages, in-transit visibility and delivery control. Select journal versus order from logistics and evidence requirements. Manual inventory blocking and batch-disposition codes can prevent reservation or issue of suspect stock. Explain exactly which processes each control blocks and how an authorized release occurs.

Inventory close settles issues to receipts and posts adjustments according to the item model; recalculation can update without closing the period. Define cut-off, sequence, negative inventory policy, exception review and reconciliation to the general ledger. ABC classification ranks items by a selected measure for differentiated control; it is an analysis input, not an automatic replenishment policy.

### Govern quality

Quality associations define when a quality order is created for a reference process and item/site/test group conditions. Test groups, tests, instruments, outcomes and acceptable quality level form the inspection contract. A quality order records results and validation; quarantine orders manage separated inventory processing. Nonconformance records describe a quality failure, related type/problem, correction and charges.

Design trigger timing carefully: before receipt, after registration or at another supported event changes what can proceed. Connect failed results to inventory blocking/disposition, vendor/customer action and evidence. Avoid duplicate quality orders when warehouse and procurement events overlap.

### Configure and operate asset maintenance

An asset type supplies defaults; an asset is the maintained equipment. Functional locations form the install/location hierarchy. Lifecycle models and states control valid transitions for assets, functional locations, requests and work orders. Work-order settings define types, jobs, stages, priorities and related behavior.

Maintenance requests capture reported need and can become work orders. Maintenance plans and rounds generate preventive work; reactive work starts from failure. Schedule work by worker, asset, tool and capacity, then register hours, items, expenses and counters as consumption. Asset loans track temporary replacement/loan flows. Reconcile maintenance execution to inventory consumption, cost and downtime evidence.

> **Related item:** Finance fixed assets track capitalization and depreciation; Supply Chain Asset Management operates equipment maintenance. An equipment record can relate to financial accounting, but the two asset models answer different questions.

---

## 3. Implement and manage supply chain processes

### Run procure-to-receive

Vendor master data, categories, procurement catalogs and policies determine what users can request and from whom. A purchase requisition expresses internal demand; an RFQ compares offers; a purchase agreement records committed terms; a purchase order authorizes specific supply. Configure workflow and change management around value, category, legal entity and exception risk.

Vendor collaboration exposes supported PO, confirmation, invoice or consignment processes to external contacts; constrain identity and vendor scope. Consignment inventory is vendor-owned until ownership change. Registration records arrival and product receipt physically updates the PO/inventory. Over/under delivery tolerances, delivery schedules and charges should express commercial policy, not conceal quantity errors.

Vendor rebates accrue/settle an agreement according to eligible purchases. Vendor returns need disposition, return document, physical shipment and financial correction. Trace every exception from request → order → receipt/return → invoice boundary even though invoice accounting is deeper MB-310 territory.

### Implement landed cost

Landed cost represents long inbound journeys through voyages, shipping containers, legs and goods-in-transit processing. Configure voyage statuses, journey templates, tracking control center, cost type codes, auto-cost rules, estimation and tolerances. Add PO or transfer lines to the correct voyage/container and preserve quantities and dates through departure, in-transit, arrival and put-away.

Estimated costs allocate according to configured basis; actual freight/duty invoices can create adjustments. Over/under delivery must resolve operational quantity and cost. Reconcile voyage/container → goods in transit → received inventory → allocated costs → vendor/freight invoice.

### Run order-to-delivery

Customer master, sales quotations and sales orders define demand. Sales agreements provide commitment terms; trade agreements provide prices/discounts. Reservations connect demand to inventory. Delivery schedules split a line across dates; sales returns reverse physical/financial flow with disposition. Sales groups and commissions assign commercial responsibility.

Intercompany orders create linked selling/buying-company documents; validate price, currency, dimensions, delivery and update sequence on both sides. Customer rebates accrue and settle eligible sales. ATP projects promise from supply/receipt timing, while CTP uses planning to consider capability/supply—confirm configuration and performance expectations. Product bundles sell a defined grouping while preserving supported component fulfillment behavior.

> **Related item:** Copilot can assist supported supply-chain decisions or summaries, but the blueprint’s scored domains remain process configuration and execution. Treat AI output as advice with source, permission, validation and fallback—not an inventory or planning system of record.

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

### Plan transportation and reconcile freight

Shipping carriers/groups, services, route plans/guides and rate/route engines provide transport choices. Load and shipment planning connects order demand with equipment, carrier, route and appointments. Dock appointment scheduling controls arrival/departure capacity.

Generate freight bills/invoices from the supported process and reconcile expected versus actual freight manually or automatically. Keep accessorial charges, tolerance, unmatched bills and dispute ownership visible. Transportation selects/moves a load; warehouse work physically picks/packs/ships it. Coordinate their state transitions without collapsing them.

> **Related item:** Inventory management tracks quantity by dimension; advanced warehouse management creates work and license-plate/location execution; transportation management plans carrier movement. The same order touches all three, but each owns different state.

---

## 5. Implement master planning

### Configure coverage and planning behavior

Coverage groups supply shared rules; item coverage overrides them by item and dimension. Understand requirement, period and min/max patterns, order modifiers, vendor/lead time and calendars. Master plans define horizon and included demand/supply. **Positive days** control how far future receipts can cover demand; **negative days** constrain using supply that arrives after demand. Time fences limit how far actions, firming, capacity or messages operate.

Action messages recommend advancing, postponing, increasing, decreasing or canceling supply. Delay calculates lateness through the supply chain. Safety margins add time at receipt/issue/reorder boundaries. Period templates group recommendations. Safety-stock journals help calculate/propose minimum levels from history; review seasonality and service policy before applying.

### Interpret and firm a plan

Run the intended plan, inspect messages, pegging, delays and net requirements, and compare results to the Supply Schedule view. Planned purchase and transfer orders are recommendations until reviewed/firmed. Define auto-firming scope narrowly and monitor exception volume.

When results look wrong, inspect on-hand/reservations, demand dates, coverage dimensions/groups, lead times/calendars, positive/negative days, time fences, order modifiers, BOM/version and planned-order status before overriding. Planning Optimization behavior changes over time; **VERIFY CURRENT** deployment, feature support and diagnostics in official docs.

> **Related item:** Forecast is anticipated demand, safety stock is a buffer target, and safety margin is time protection. Adding all three without understanding interaction can amplify supply and inventory.

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
3. **Quality:** Configure association/test group/order/quarantine/nonconformance; test pass, fail, partial sample, duplicate trigger and authorized disposition.
4. **Asset management:** Build functional location, asset/type/lifecycle, request/work order, preventive plan, scheduling/capacity/loan and consumption evidence.
5. **Procurement/landed cost/sales:** Run requisition/RFQ/agreement/PO/receipt/return, a voyage with cost variance, and quotation/order/reservation/delivery/return/intercompany paths.
6. **Warehouse/mobile:** Build layout/status, wave/work/location directives, replenishment/cross-dock/counting, labels/containerization and mobile menus/workers/detour; capture failure diagnostics.
7. **Transportation:** Configure carrier/service, route/rate, load/shipment and appointment; generate/reconcile a freight bill with tolerance exception.
8. **Planning:** Configure coverage, positive/negative days, margins/fences and plan; create demand, analyze pegging/messages/Supply Schedule, firm selected purchase/transfer orders and explain rejects.

## Knowledge checks

1. Why separate shared product from released product?
2. Which dimension groups create variants, storage identity and traceability?
3. How do reservation hierarchy and unit sequence affect warehouse execution?
4. When should lifecycle state prevent a transaction?
5. What makes a BOM version applicable?
6. Distinguish active standard cost, planned cost and trade-agreement price.
7. When choose transfer journal versus transfer order?
8. Which transactions are physical versus financial inventory updates?
9. What does inventory close settle and adjust?
10. Compare manual blocking and batch disposition.
11. How do quality association, order, quarantine and nonconformance differ?
12. Which event should trigger inspection and why?
13. Distinguish Finance fixed asset and SCM maintained asset.
14. How do request, plan, schedule, work order and consumption connect?
15. Compare requisition, RFQ, agreement and PO.
16. How is vendor-owned consignment converted to owned inventory?
17. Which controls govern over/under delivery and vendor returns?
18. Trace voyage, container, goods in transit and landed-cost allocation.
19. How do sales agreement and trade agreement differ?
20. What dependencies make intercompany orders fail asymmetrically?
21. Compare ATP and CTP.
22. Trace release, load, shipment, wave, work and mobile completion.
23. What do location directives and work templates each decide?
24. When do replenishment and cross-docking create different movements?
25. How should cycle counting coexist with open work?
26. What do license plate, GS1 label and container each identify?
27. What must a mobile detour preserve?
28. Which evidence diagnoses a short pick or duplicate scan?
29. How do route/rate engines and route guides differ?
30. What is matched during freight reconciliation?
31. Compare coverage group and item coverage.
32. How do positive days and negative days change supply matching?
33. Distinguish time fences and safety margins.
34. Why inspect pegging before firming?
35. When is auto-firming unsafe?
36. Which current product areas require a documentation freshness check?

---

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one primary route, build complete product-to-plan and order-to-warehouse journeys, and add another resource only for a measured gap.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MB-330 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-330) | Free | 1–2 hours to map the five domains |
| [Products and inventory](https://learn.microsoft.com/en-us/training/paths/configure-manage-products-inventory-dyn365-supply-chain-mgmt/) | Free | 7 hours 46 minutes listed; 15–24 hours with practice |
| [Procurement and vendors](https://learn.microsoft.com/en-us/training/paths/configure-manage-procurement-vendors-dyn365-supply-chain-mgmt/) | Free | 13 hours 41 minutes listed; select objectives and allow 20–32 hours with transactions |
| [Configure Asset Management](https://learn.microsoft.com/en-us/training/paths/configure-asset-management-dyn365-supply-chain-mgmt/) and [work with Asset Management](https://learn.microsoft.com/en-us/training/paths/work-asset-management-dyn365-supply-chain-mgmt/) | Free | 10 hours 45 minutes listed; 18–28 hours with maintenance flows |
| [Landed cost](https://learn.microsoft.com/en-us/training/paths/setup-work-landed-cost-dyn365-supply-chain-mgmt/) | Free | 2 hours 53 minutes listed; 6–10 hours with voyage/cost reconciliation |
| [Warehouse management](https://learn.microsoft.com/en-us/training/paths/configure-work-warehouse-management-dyn365-supply-chain-mgmt/) | Free | 5 hours 59 minutes listed; 15–25 hours with mobile work/failure tests |
| [Transportation management](https://learn.microsoft.com/en-us/training/paths/configure-work-transportation-mgmt-dyn365-supply-chain-mgmt/) | Free | 1 hour 43 minutes listed; 5–8 hours with load/freight practice |
| [Master planning](https://learn.microsoft.com/en-us/training/paths/master-planning-supply-chain-management/) | Free | 7 hours 20 minutes listed; 14–22 hours with planning diagnostics |
| [MB-330T00-A course](https://learn.microsoft.com/en-us/training/courses/mb-330t00) | Paid/provider-dependent | 5 days |
| [MicrosoftLearning MB-330 labs](https://github.com/MicrosoftLearning/MB-330-Microsoft-Dynamics-365-Supply-Chain-Management) | Free; MIT | 15–30 hours selected case studies; verify UI/current feature behavior |
| [Free MB-330 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/d365-functional-consultant-supply-chain-management/practice/assessment?assessment-type=practice&assessmentId=73&practice-assessment-type=certification) | Free | 45–90 minutes plus review |
| [Supply Chain Management documentation](https://learn.microsoft.com/en-us/dynamics365/supply-chain/) | Free | 15–40 hours selected implementation/troubleshooting |
| [Udemy advanced warehouse management Part 1](https://www.udemy.com/course/mb330-d365-fo-advance-warehouse-management-part1/) | Paid | Verify runtime; updated July 2024, so use for durable WMS practice and gap-check mobile/app changes |
| [MeasureUp MB-330 practice test](https://www.measureup.com/microsoft-practice-test-mb-330-microsoft-dynamics-365-supply-chain-management.html) | Paid; free demo | 2–4 hours diagnostic/review; verify its published update date and current five-domain mapping before use |
| [Microsoft Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner login required | Use the five-day course pattern for planning; signed-in event start/end times control |

The eight selected official paths total **50 hours 7 minutes** before independent labs; the full five-day syllabus contains additional manufacturing and adjacent modules, so select against the blueprint. Allow roughly **120–190 hours** for a new practitioner to complete a primary route, build the labs and remediate assessment gaps. No exact current MB-330 Pluralsight, O’Reilly or Whizlabs product was independently verified. Question-bank-only listings and “guaranteed pass” claims were excluded; reject recalled live content and unexplained bulk questions.

## Final readiness checklist

- [ ] I can configure/release products, dimensions, reservation/unit behavior, prices and costs and trace their effects.
- [ ] I can reconcile inventory journals/orders, close/adjustment, blocking, quality and asset-maintenance consumption.
- [ ] I can run procurement, landed-cost and sales/intercompany lifecycles with workflow and exception evidence.
- [ ] I can trace order release through shipment/load/wave/work/location/mobile/container/label and recovery.
- [ ] I can configure transport carriers/routes/rates/appointments and reconcile freight.
- [ ] I can configure coverage/plans/days/messages/fences/margins, diagnose results and firm appropriate supply.
- [ ] I completed all three scenarios and eight labs with failure-path evidence.
- [ ] I rechecked the current blueprint, lifecycle, Practice Assessment and fast-moving product docs before scheduling.

## Source notes

The June 20, 2025 Microsoft study guide is the objective authority. Microsoft Learn paths, product docs and MIT-licensed course labs support behavior but may include adjacent content or UI drift. Commercial assessment/training is optional and never defines scope. All questions here are original and conceptual; no exam dumps or recalled items were used.
