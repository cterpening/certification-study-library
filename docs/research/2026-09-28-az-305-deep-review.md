# AZ-305 deep review — September 28, 2026

The [AZ-305 guide](../../guides/AZ-305-designing-microsoft-azure-infrastructure-solutions.md)
was read in full and mapped to **49 objectives in twelve groups**. It now has
seven worked examples, ten labs and 48 explained original checks. **38 offline
assertions passed:** 26 arithmetic/catalog checks and 12 assertions in one
published SQLite transaction/replay example. No Azure deployment, SDK
integration, migration, failover, restore or paid-content execution occurred.
Independent human review remains pending.

## Blueprint and certification

The [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305)
retains its April 17, 2026 baseline; objective and status hashes are unchanged,
with no upcoming objective announcement. The
[credential profile](https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/)
lists ten languages, renewal and Azure Administrator Associate as a prerequisite
for earning the Expert certification. This is not a prerequisite merely to sit
AZ-305. Exact exam duration was not verified. Practice Assessment and sandbox
links were reviewed at their public landing pages only.

The credential page displays a course-availability placeholder, but the
[standalone AZ-305 course](https://learn.microsoft.com/en-us/training/courses/az-305t00)
is available and lists four instructor days and eight languages. The guide
uses that direct course source and does not infer that official training is absent.

## Changes that affect design decisions

| Area | Primary evidence and applied change |
|---|---|
| Logging | Inspect the [Monitor Logs table-plan matrix](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-platform-logs) with cells preserved. Basic supports Simple Log Alerts; Auxiliary/Lake lacks alerts and workspace replication. Add query costs, eligibility and operational requirements to the decision. |
| Identity and keys | Separate [new-vault RBAC defaults and API retirement](https://learn.microsoft.com/en-us/azure/key-vault/general/access-control-default) from existing-vault access migration. Add [object backup](https://learn.microsoft.com/en-us/azure/key-vault/general/backup) scope, version constraints and same-subscription/geography restore. |
| Data and recovery | Explain [SQL failover-group](https://learn.microsoft.com/en-us/azure/azure-sql/database/failover-group-sql-db?view=azuresql) listeners and customer-managed recovery ownership. Connect [Cosmos partition](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview) choices to transaction boundaries and skew. |
| Failure analysis | [Region pairing](https://learn.microsoft.com/en-us/azure/reliability/regions-paired) is not automatic workload HA. Apply [failure mode analysis](https://learn.microsoft.com/en-us/azure/well-architected/reliability/failure-mode-analysis) to serving requests and performing recovery separately. |
| Messaging | Compare metadata-only [Geo-Disaster Recovery](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-geo-dr) with message/state [Geo-Replication](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-geo-replication). Distinguish mode, lag, promotion, authorization and preview limits. |
| Business effects | Apply the [idempotent-consumer](https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer) and [transactional-outbox](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos) boundaries. The original code demonstrates a consumer inbox and local atomic update, not a cloud exactly-once guarantee. |
| Compute and APIs | Separate [Functions HTTP deadlines](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale) from execution timeout. Compare the [APIM v2 matrix](https://learn.microsoft.com/en-us/azure/api-management/v2-service-tiers-overview) with [classic Premium multi-region](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-deploy-multi-region), including primary-region management dependencies. |
| Configuration | [App Configuration replicas](https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-geo-replication) are eventually consistent. Explain client failover and stale/default behavior instead of implying immediate global propagation. |
| Networking | Scope the [private-subnet default](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access) to new VNets and the relevant API versions. Add explicit egress and [Front Door migration](https://learn.microsoft.com/en-us/azure/frontdoor/migrate-tier) readiness, including postmigration DNS work. |

## Lifecycle follow-up

| Date | Scope and treatment |
|---|---|
| September 30, 2026 | [Service Bus](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-transfers-locks-settlement) older SDKs retire; SBMP becomes unusable after the deadline. These effects differ. [Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale) v3 on Linux Consumption stops running after this date. |
| February 27, 2027 | Key Vault control-plane APIs earlier than 2026-02-01 retire. API migration does not automatically change an existing vault's access model. |
| March 31, 2027 | Front Door classic and [Redis Enterprise/Enterprise Flash](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/retirement-faq) retire; remaining Enterprise caches are disabled starting April 1. |
| September 30, 2028 | Redis Basic/Standard/Premium retire, with disablement from October 1; Linux Consumption hosting also retires September 30. Distinguish hosting retirement from the earlier Functions runtime deadline. |

The maintenance event queue now includes September 30 and October 12 checks,
plus advance reviews on February 1 and March 1, 2027. These are source-review
triggers; they do not execute cloud migrations. Existing weekly monitoring and
age-based checks continue to cover later dates.

## Blog intake

All three rendered pages returned minimal article shells. Their publicly
embedded article bodies and author/date metadata were extracted and hashed in
the receipt. Reading was bounded as follows:

- [Fault types in Azure](https://techcommunity.microsoft.com/blog/azurearchitectureblog/proactive-reliability-series-%E2%80%94-article-1-fault-types-in-azure/4507006),
  Zoran Jovanovic, April 1, 2026: introduction, FMA/taxonomy and partial-regional
  discussion through the first Switzerland incident heading. Historical incident
  details were not verified. The author explicitly disclaims Microsoft
  endorsement; the registry records personal expert commentary. Adopt the
  fault-matrix exercise, not qualitative likelihood labels as probabilities.
- [APIM Premium v2 GA](https://techcommunity.microsoft.com/blog/integrationsonazureblog/announcing-the-general-availability-ga-of-the-premium-v2-tier-of-azure-api-manag/4471499),
  Sreekanth Thirthala, November 19, 2025: main announcement read. Use it to
  introduce separate gateway/backend network designs. Current product exclusions
  control; launch geography and broad marketing language are not current support
  guarantees.
- [Service Bus Geo-Replication GA](https://techcommunity.microsoft.com/blog/messagingonazureblog/announcing-general-availability-of-geo-replication-for-azure-service-bus-premium/4413164),
  Eldert Grootenboer, December 17, 2025: main announcement read. Add an
  acknowledgment, latency and promotion worksheet. Current documentation still
  marks partitioned-namespace support preview and excludes large messages.

## Learning resources

The public [Pluralsight path](https://www.pluralsight.com/paths/az-305-designing-microsoft-azure-infrastructure-solutions)
lists five courses totaling 13h 48m and three labs totaling 4h 15m: **18h 03m**
combined versus its rounded 18-hour heading. Courses date from 2024–2025;
the most recently listed lab is September 18, 2026. New lab metadata does not
establish that all video coverage is current.

Direct O'Reilly and Udemy retrieval remains blocked. Indexed O'Reilly provider
metadata confirms the [ACI/Adam Gordon course](https://www.oreilly.com/videos/designing-microsoft-azure/9781836200659/)
at May 2024 / 18h 46m, and the [Exam Ref](https://www.oreilly.com/library/view/exam-ref-az-305/9780137878758/)
at November 2022 / 192 pages / 5h 32m estimated reading time. The browser could
read the [Christopher Nett Udemy page](https://www.udemy.com/course/az-305-microsoft-azure-solutions-architect-expert-i/):
January 2026, 13 sections, 164 lectures and 16h 51m. A provider aggregator's
different AZ-305 course duration was not substituted for this exact product.

[MeasureUp](https://www.measureup.com/microsoft-practice-test-az-305-designing-microsoft-azure-infrastructure-solutions.html)
now lists **164 questions and a September 2026 update**, replacing the guide's
148-question / April 2024 metadata. Paid questions and explanations were not
opened. Whizlabs review was limited to public planning paragraphs. Savill's
video returned a shell, so its historical four-hour estimate is qualified;
the linked whiteboard image was not visually inspected. None of these public
catalog checks establishes complete coverage or paid-content correctness.

## Verification and remaining limits

The worked examples cover serial availability, skewed partition demand, queue
catch-up, cold-cache load, migration convergence, recovery critical paths and
transaction rollback/replay. The 12 code assertions run only in a local
in-memory SQLite database; they do not exercise concurrent workers, a broker,
external payment APIs or regional recovery. All capacity inputs are fictional.

Local repository validation, reviewed-resource consistency, all 174 unit tests,
strict site build, generated-site validation and whitespace checks passed.
The receipt at `ADLC_Docs/operations/2026-09-28-az-305-deep-review.json` preserves
the earlier review, objective hashes, 49 mappings, individual source boundaries,
blog body hashes and validation evidence. Retained references were fetched;
long product pages and every linked procedure were not exhaustively reread.

The review process detects source changes and queues work. It does not replace
semantic review, live labs or independent human review. Completion of this
guide does not mark the remaining Microsoft guides complete; the
[coverage tracker](../MICROSOFT-REVIEW-STATUS.md) records the remaining work.
