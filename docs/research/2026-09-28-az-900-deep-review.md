# AZ-900 deep review — September 28, 2026

The entire guide and all 57 detailed objectives were reviewed against the unchanged July 20, 2026 blueprint. The guide now has six worked examples, seven labs and 30 answered checks, including answers to its seven existing questions. Three blog exercises were added and one unsuitable automation article was rejected. Independent human review and live Azure labs remain pending.

## Scope and evidence

The eleven objective groups contain 7/4/4/7/6/6/8/4/3/5/3 bullets. Each has a section mapping in `ADLC_Docs/operations/2026-09-28-az-900-deep-review.json`, alongside prior records, source fetches, reading boundaries and validation results. The objective hash remains `8b4c89d325b3ce339eb881aa2dc4b251888e6d7a07d6351d81bcc2123b1c4449`; status hash remains `0f30a5d589be04e1a7b6ed102fa537494796db50e4160607f8e49199d1c2eb0a`.

The [credential](https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/) is active with a 45-minute assessment and 13 languages. Fundamentals certifications do not expire under the [expiration policy](https://learn.microsoft.com/en-us/credentials/support/certification-expiration-policy). The one-day, 13-language AZ-900T00 course is now named Introduction to Cloud Infrastructure; training completion is distinct from earning the credential.

## Changes that help learners

The current [shared-responsibility matrix](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility) was inspected with table cells preserved. Application responsibility is shared for SaaS/PaaS; customer data, identity and configuration duties remain. The compact guide table was corrected accordingly.

Billing examples now separate allocated/stopped/deallocated VM state, retained-resource charges, actual cost versus forecast, alert delay, offer-specific spending limits and shared-cost allocation. The [savings-plan overview](https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/savings-plan-compute-overview) now describes compute and database offers, so the guide's compute-only wording was replaced. Billing commitments are distinguished from capacity guarantees and resource operations.

Storage coverage distinguishes service/data shape, account type, tier and redundancy. The [tier reference](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview) supports ordinary charging-duration versus retention-lock and archive-versus-online distinctions. The specialized [smart-tier reference](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-smart) controls current eligibility, default/inherited behavior, access clocks and sovereign-preview status. Its online-only behavior and billing model are not conflated with ordinary manual tiering. The example uses a 1 MiB object and avoids the documentation's exact 128 KiB boundary ambiguity.

Other additions explain nonpaired regions, External ID workforce/customer-app separation, resource tags versus inherited cost-record tags, remediation tasks/identity, management locks versus data-plane protection, Cloud Shell context/cost, and public status versus personalized health. These fill practical gaps without expanding the official objective list.

## Blog decisions

| Source | Decision and learning value | Boundaries |
|---|---|---|
| [Forecasted cost alerts](https://azure.microsoft.com/en-us/blog/prevent-exceeding-azure-budget-with-forecasted-cost-alerts/), Adam Wise, March 15, 2021 | Accept: actual/forecast threshold exercise. | Older explanation; current budget timing/scope controls. Alerts are not a hard spending cap. |
| [Smart tier GA](https://azure.microsoft.com/en-us/blog/optimize-object-storage-costs-automatically-with-smart-tier-now-generally-available/), Aung Oo, April 14, 2026 | Accept: online access-clock exercise and comparison with archive. | Current product eligibility controls; customer savings percentages are not forecasts for other workloads. |
| [Observability Agent billing](https://techcommunity.microsoft.com/blog/azureobservabilityblog/understanding-billing-for-the-azure-copilot-observability-agent/4537780), Noa Kuperberg, July 16, 2026 | Accept: optional consumption-unit and additive monitoring-cost example. | No new exam objective. Future caps and advanced correlation-billing/per-operation ambiguities are not adopted. |
| [FinOps-ready landing zone](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/building-a-finops-ready-azure-landing-zone-infrastructure-foundations-for-cost-o/4411706), javedeqbal, May 8, 2025 | Reject for this beginner guide. | Abbreviated inputs, an expired budget end date and a generic diagnostic-setting snippet do not supply a tested cost-export deployment. No code copied or executed. |

All four main article texts were read. TechCommunity body extraction and metadata were preserved; comments, linked media and cloud scripts were not executed. Current [agent billing documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-billing) supports the bounded consumption-unit lesson, not an assertion that every advanced billing statement has been reconciled.

## Catalog comparison

Pluralsight lists five courses totaling 18h56 and four 30-minute labs, yielding 20h56 rounded to 21 hours; the prior row incorrectly added labs on top. Course dates span 2024–2026 and the latest lab is September 21. O’Reilly browser metadata confirms KodeKloud/Rithin Skaria, August 2025, 6h27. Udemy now lists September 2026, 15 sections, 148 lectures and 8h17. Direct O’Reilly/Udemy retrieval remains blocked; public metadata does not verify lesson accuracy or completeness.

LinkedIn remains 4h11/September 5, 2024. Coursera's four course estimates total 63 hours, distinct from its three-month/10-hour-week pace. MeasureUp lists 159 questions and June 2026; its domain counts sum to 159. Partner, Whizlabs, direct assessment and generic O’Reilly practice pages returned shells or no substantive text. Entitlements/launch details and Savill media/runtime remain unverified. No paid content or assessment questions were consumed.

## Validation and follow-up

Thirty-five local assertions check invented VM costs, a classroom projection, shared allocation, storage charging/access clocks, availability arithmetic and provider catalog sums. These are not Azure price quotes, the Azure forecast algorithm, service performance measurements or SLA eligibility determinations. Repository tests, metadata/learning-resource checks, strict site build, generated-site validation and whitespace checks are recorded in the receipt after success.

October 26 follow-ups cover storage/billing eligibility and course/catalog changes. Weekly automation detects and queues review work; it does not perform the semantic review itself. The [Microsoft review tracker](../MICROSOFT-REVIEW-STATUS.md) retains the remaining exam backlog.

No cloud deployment, tenant configuration, financial commitment, notification, storage mutation or agent investigation was performed. Full feature/region/offer matrices were not exhaustively audited. There is no unresolved blocker for the bounded claims applied to this fundamentals guide; advanced ambiguities deliberately excluded are identified above.
