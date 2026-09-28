# AZ-700 deep review — September 28, 2026

The entire guide and all 136 detailed objectives were reviewed against the unchanged July 27, 2026 blueprint. The guide now includes six worked examples, ten labs, 48 answered checks and three blog exercises. Same-context AI source review is complete; independent human review and live labs remain pending.

## Scope and evidence

- Objective groups contain 10/7/10/7/9/9/13/7/11/10/9/6/4/10/7/7 bullets. Every bullet has a guide-section mapping in the receipt.
- Objective hash: `949dcb2d1b4bbde19b6f41b69fdf59cf33b52391d4b8010e2a46d6a0c94a98dd`; status hash: `b7617252bfa7efd19e346b0a81e2789ed70299d5b7fdb0ca18a47646d3cf9920`.
- The official credential remains active, with a 100-minute assessment, ten exam languages and annual renewal. The separate instructor course lists three days/eight languages.
- Detailed prior records, fetch outcomes, hashes, per-source reading boundaries, objective mappings, findings and local checks are in `ADLC_Docs/operations/2026-09-28-az-700-deep-review.json`.

## Material changes

The [NAT resource documentation](https://learn.microsoft.com/en-us/azure/nat-gateway/nat-gateway-resource) supports the SKU/protocol/capacity distinction. The original 120,000-connection exercise demonstrates why 64,512 ports per IP must not be confused with the 50,000 concurrent same-destination limit. Current [NAT overview limitations](https://learn.microsoft.com/en-us/azure/nat-gateway/nat-overview) control migration planning, including cases that interrupt existing traffic.

DNS additions separate endpoint direction, ruleset links, application routes, forwarding loops and the [Private Link-only NXDOMAIN fallback](https://learn.microsoft.com/en-us/azure/dns/private-dns-fallback). Endpoint policy guidance qualifies the ordinary route-selection example. Preview [PLS Direct Connect](https://learn.microsoft.com/en-us/azure/private-link/configure-private-link-service-direct-connect) is distinguished from conventional load-balancer-backed PLS, with restrictions and the October 15 billing start visible.

VPN additions distinguish [non-AZ consolidation](https://learn.microsoft.com/en-us/azure/vpn-gateway/gateway-sku-consolidation) from Basic gateway retirement claims and close the Always On device-tunnel requirements gap. ExpressRoute coverage now tests failure boundaries, degraded backup capacity, route preference and failback. Resiliency Guard stays explicitly preview; WAN routing intent is qualified by its route-table prerequisites and rollback requirements.

Application delivery additions explain backend TLS/probes, already-retired Application Gateway v1 and future Front Door classic migration. Security examples clarify admin Allow versus Always Allow, Firewall type order, application-rule SNAT and origin IP-plus-FDID restrictions. Existing flow-log retirement and agentless-preview cautions were retained and rechecked.

## Blog intake

All three extracted main articles were read, with author/date metadata preserved. Comments, media and linked deployments were not executed.

| Article | Accepted learning use | Qualification |
|---|---|---|
| [Private subnets by default](https://techcommunity.microsoft.com/blog/azurenetworkingblog/private-subnets-by-default-in-azure-virtual-networks-what-changed-and-how-to-use/4513778), Aimee Littleton, April 22, 2026 | Compare old/new VNet egress and plan dependencies/cutover. | Reject the stale Terraform exception and unconditional migration no-interruption statement; current product limitations govern. |
| [Landing-zone DNS](https://techcommunity.microsoft.com/blog/azurenetworkingblog/dns-best-practices-for-implementation-in-azure-landing-zones/4420567), Ashish Rana, June 12, 2025 | Compare centralized/distributed query paths and detect loops. | Zone links alone do not enforce firewall routing. Limit fallback to Private Link zones and avoid universal AD replication advice. |
| [StandardV2 ICMP](https://techcommunity.microsoft.com/blog/azurenetworkingblog/icmp-support-for-azure-standardv2-nat-gateway/4528374), Malaika Nazim, June 17, 2026 | Distinguish Echo reachability from HTTPS/application success. | SKU and ICMP-type restrictions remain; other filters and destination behavior still apply. |

## Learning catalog and objective coverage

The complete objective map is recorded per bullet rather than inferred from a course title. Existing IP, Monitor/Defender, hybrid connectivity, delivery, private access and security sections were retained and mapped; new material addresses concrete gaps and volatile behavior.

Pluralsight has six refreshed courses totaling 11h08 plus a 30-minute lab, and one 32h27 legacy course: seven courses total and 44h05 with the lab. The 44-hour header therefore should not be treated as all refreshed material. O’Reilly public browser metadata confirms Kirk Whetton’s July 2025 11h02 course and David Okeyode’s August 2023 524-page book/11h20 estimate. Udemy confirms March 2026, 13 sections, 368 lectures and 33h23. Direct retrieval of those three provider pages remains blocked. MeasureUp still advertises 118 questions/January 2025. Savill video runtime/image content and Whizlabs bundle details remain unverified. No paid content or assessment questions were consumed.

## Validation and follow-up

Thirty offline assertions check subnet growth, ordinary route ranking, SNAT capacity, backup demand and catalog sums. They use invented workload assumptions; they do not verify Azure performance or simulate its complete routing engine. Repository tests, metadata/learning-resource validation, strict site build, generated-site validation and whitespace checks are recorded after successful execution in the receipt.

Maintenance events cover October 5 VPN consolidation, October 12 PLS preview/billing, October 26 networking capabilities, March 1 Front Door classic migration and August 30, 2027 flow-log retirement preparation. Weekly automation detects/queues these changes; it does not replace a semantic deep review. Other pending exams remain visible in the [Microsoft review tracker](../MICROSOFT-REVIEW-STATUS.md).

No cloud resources, tenant policies, gateways, DNS settings, routes or firewall rules were changed. Large reference matrices and deployment scripts were reviewed only to the per-source boundaries recorded in the receipt. No unresolved evidence blocker remains for the applied claims.
