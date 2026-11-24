---
exam_code: AB-330
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-330
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: ai-generated-draft
last_verified: 2026-11-20
upcoming_change_status: none-announced
upcoming_change_checked: 2026-11-20
---

# AB-330 Supply Chain Management AI Consultant Associate

> **Independent AI-assisted resource.** Beta study guide, checked November 20, 2026. Human review and live Dynamics 365 exercises are pending. Microsoft's [AB-330 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-330) is authoritative.

AB-330 is for functional consultants who turn supply chain requirements into Dynamics 365 configurations. Start with purchasing, warehousing and sales. Together they carry the largest weights. Practice following one order through all three so you can explain which team owns the next decision.

**VERIFY CURRENT.** Microsoft opened the beta in October and expects general availability in January 2027. The credential page lists English, 100 minutes, a passing score of 700 and Pearson VUE scheduling. Beta results are delayed. Microsoft lists no practice assessment on the credential page. MB-330 and its separate Functional Consultant Associate credential retire February 1, 2027. [Credential and booking](https://learn.microsoft.com/en-us/credentials/certifications/supply-chain-management-ai-consultant-associate/) · [Microsoft launch and transition notice](https://techcommunity.microsoft.com/blog/skills-hub-blog/new-microsoft-certified-supply-chain-management-ai-consultant-associate/4564533)

## Objective map

Microsoft's English outline was updated October 15, 2026. It lists six business processes and supplies no separate skills-effective date. AI-enabled capabilities appear in the audience description. The six process areas below carry the published weights. [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-330)

| Process | Weight | Decision to practice |
|---|---:|---|
| Design to retire | 5–10% | Release a product to the right company. Choose its dimensions, lifecycle state, cost and applicable bill of materials or formula. |
| Forecast to plan | 1–5% | Turn demand into planned supply. Check coverage, calendars and time fences before firming an order. |
| Inventory to deliver | 20–25% | Decide where goods should move, which work the warehouse should create and what to do with stock under inspection. |
| Order to cash | 20–25% | Price a sales order, promise a date, reserve supply and trace a return or intercompany dependency. |
| Plan to produce | 1–5% | Schedule resources, record material and time consumption, report finished output and close the order. |
| Source to pay | 30–35% | Select the purchasing document, approval route, supplier agreement and receipt evidence appropriate to the request. |

> **About related items:** A **Related item:** adds practical context beyond the wording of an objective.

## From purchase request to supplier delivery

A factory needs 120 replacement bearings. Its usual supplier has a price agreement, but can ship only 80 this week. Before changing the sales promise, trace what each purchasing document establishes. A requisition records the internal need. An RFQ lets buyers compare offers. A purchase agreement records terms for purchases over time. A purchase order specifies the quantities and delivery terms for this transaction. Select the documents that the scenario actually needs. Check purchasing policy, approval authority and delivery tolerances before accepting a split shipment. [Microsoft procurement process](https://learn.microsoft.com/en-us/dynamics365/guidance/business-processes/source-to-pay-procure-materials-services-overview)

Suppose the warehouse posts a receipt for the first 80. Inspect both the document history and remaining quantity. The latest posted document can be a product receipt while the order quantity status remains open. Capture the vendor confirmation for the last 40 and distinguish it from an actual second receipt. For a return, identify the original receipt, the quantity being returned and the vendor return document. [Purchase order types and statuses](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/purchase-order-overview)

## From product design to a customer promise

For a new assembly, identify which product variant the company released and which BOM or formula version applies. A BOM identifies components. A formula can also account for co-products and by-products. Check the version's applicability before trusting an explosion or a cost calculation. For a make-to-order item, a valid component list still leaves the question of when the work centre can run the order. [Bills of materials and formulas](https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/bill-of-material-bom)

Read a planned purchase or production order as a proposed response to demand. Inspect the item, site, dates and existing supply before firming. For a customer's delivery date, ATP uses availability information. CTP also considers materials, capacity and lead times. If the production line is fully booked, ask which method produced the quoted date and which calendars it used. Trace the customer, price, reservation and confirmed date back to the sales order. [Planned order firming](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/planned-order-firming) · [Delivery date calculations](https://learn.microsoft.com/en-us/dynamics365/supply-chain/master-planning/planning-optimization/calculate-delivery-dates-using-ctp)

## From stock arrival to finished goods

A work template defines the warehouse tasks. A location directive selects an eligible pick or put location for the relevant work line. When put-away fails, first check whether work was created. If it exists, inspect the warehouse, line criteria and eligible locations. For an inspection failure, identify the quality order and its test results, then verify inventory blocking before offering the stock for shipment. [Warehouse work and location directives](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/control-warehouse-location-directives) · [Quality orders](https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/quality-orders)

On the production order, compare scheduled inputs with what the floor actually consumed. Picking list journals record material consumption. Route or job card journals record operations and time. Reporting as finished records output. Ending the order has separate costing implications. Capture each event before explaining a difference between estimated cost, actual consumption and finished inventory. [Production order lifecycle](https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/production-process-overview)

## Decisions to rehearse across the six processes

Use these changes to the bearing order to test a different part of the outline each time. For each one, name the first record you would inspect and the evidence that would allow the order to proceed.

| Change in the scenario | Decision and evidence |
|---|---|
| A second company will stock the bearing | Choose the product dimensions and tracking requirements, release the variant to that company, and check its lifecycle state and active cost. Verify that the applicable BOM version, dates and unit of measure match the intended item. |
| The plan repeatedly proposes a new purchase one day before an existing receipt | Check the forecast model, working calendar, item coverage, time fences and safety margin. Compare the pegged demand and available supply before accepting an action message, changing planning policy or firming the proposal. |
| The carrier arrives with only part of the inbound load | Compare load lines with physically registered quantities and the posted product receipt. For outbound work, trace the reservation, wave, pick, put and shipment confirmation. Look for the first missing event before changing the load. [Inbound load handling](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/inbound-load-handling) |
| A bin contains fewer bearings than on-hand inventory shows | Use cycle counting work to record the physical quantity and review the difference. A transfer order records stock traveling between warehouses. A count discrepancy alone supplies no evidence of a transfer. Check owner, status and blocking before releasing stock. [Cycle counting](https://learn.microsoft.com/en-us/dynamics365/supply-chain/warehousing/cycle-counting) |
| Another legal entity sells the assembly to the customer | Check customer delivery terms, price and reservation on the external order. For the internal leg, verify that the buying company's vendor and selling company's customer point to the correct counterpart, then trace the linked purchase and sales orders. [Intercompany trading setup](https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/intercompany-set-up-vendors-customers-items) |
| A production resource is unavailable | Check the route, resource capability, calendar and capacity assumptions. Compare the operations schedule with detailed job assignments. Before release, check component reservations. During execution, record consumption, output or scrap against the correct job and reconcile before ending the order. [Production lifecycle](https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/production-process-overview) |
| The supplier proposes a new price and delivery date | Verify the vendor account, category policy, purchase agreement, delivery tolerance and approval workflow. Give the supplier access to the appropriate collaboration records. Compare its response with the approved PO and record the buyer's decision before accepting a change. [Vendor collaboration](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/vendor-collaboration-work-external-vendors) |

## Practice and readiness

> **Related item:** The supplier communications capability in the Procurement Agent can help purchasers review proposed changes to purchase orders. For a delayed delivery, compare the proposed date and quantity with the vendor's message and the customer's demand before accepting the change. **VERIFY CURRENT.** Microsoft describes the agent as a production-ready preview. Check availability and setup in your environment. [Microsoft's Procurement Agent overview](https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/procurement-agent-overview)

On paper, draw the 120-bearing order as a timeline. Add an inspection hold on 10 of the 80 received, an outstanding delivery of 40 and a customer request for 90. Assume one bearing per unit, no other stock and all other components available. Mark each number as ordered, received, eligible or still expected. Name the screen or document you would inspect before committing to a shipment.

**Answer check.** At most 70 bearings from the first delivery are eligible under those assumptions. A buyer can confirm the supplier's next delivery, a quality owner can disposition the held stock, and a planner can check component and production capacity. Explain which new evidence would change the promised date. Treat an AI-generated summary as a proposal to verify against those records before changing the order.

## Places to learn

This is a starting sequence, not a complete list. Times below are editorial estimates for the selected reading or exercise. Hands-on configuration requires access to a suitable Dynamics 365 environment.

| Resource | Access | Estimated time |
|---|---|---|
| [AB-330 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-330) | Public outline | 20–30 minutes to mark each process and list the documents you already know. |
| [Configure and manage procurement and vendors](https://learn.microsoft.com/en-us/training/paths/configure-manage-procurement-vendors-dyn365-supply-chain-mgmt/) | Public Microsoft Learn path | Microsoft lists 13 hr 41 min for all seven modules. Allow about 30–45 minutes for selected purchasing lessons and the split-delivery exercise. |
| [Master planning in Dynamics 365](https://learn.microsoft.com/en-us/training/paths/master-planning-supply-chain-management/) | Public Microsoft Learn path | Microsoft lists 7 hr 20 min for the full path. Allow about 20–40 minutes to trace one demand, a planned order and a firming decision. |
