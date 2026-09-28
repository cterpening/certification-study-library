# AI-200 deep review — September 28, 2026

The [AI-200 guide](../../guides/AI-200-developing-ai-cloud-solutions-on-azure.md)
was read in full and mapped to **27 detailed objectives in nine groups**. It now
contains six worked examples, ten labs and explanations for 48 original knowledge
checks. Twenty-six offline assertions check capacity, replay/version state,
filtered recall, rotation timing, sampling and catalog arithmetic. Five Python
blocks compile; the local sequential reducer was executed, and the AKS YAML was
parsed. These checks do not execute Azure SDKs or validate deployed behavior.

This is same-context AI research and repair. Independent human review remains
pending. No tenant, database, broker, cache, model, credential, container build,
deployment, SQL, KQL, load test or paid course was exercised. The Managed Redis
conversion documentation conflict below remains a narrow open blocker.

## Exam and learning catalog

The [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200)
still has its May 5, 2026 page date, no separate skills-effective date and no
announced revision. All 27 objectives and accepted snapshot hashes are unchanged.
The [credential page](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-cloud-developer-associate/)
lists an active 120-minute assessment in 13 languages and no Practice Assessment.
The [course](https://learn.microsoft.com/en-us/training/courses/ai-200t00)
lists five days and 12 languages; Russian appears in the exam list but not the
course list. Its extracted syllabus remained a loading shell. The prior nine-path,
32h4 total was not reproduced and is no longer presented as current.

The [O'Reilly event](https://www.oreilly.com/live-events/azure-ai-cloud-developer-associate-ai-200-crash-course/0642572385149/0642572385132/)
lists Reza Salehi, October 1, 2026 and an embedded 12:00–16:00 UTC event window.
Its public agenda adds to 240 minutes before the separately listed breaks;
the provider labels times approximate. Delivery, attendance and recording remain
unverified because the event is future.

Direct Udemy retrieval was blocked. Indexed public outlines show:

| Listing | Update | Public outline |
|---|---|---|
| [Luke Ginn](https://www.udemy.com/course/ai-200-azure-ai-cloud-developer-associate-complete-course/) | August 2026 | 13 sections, 55 lectures, 21h19; some walkthroughs still forthcoming |
| [Kuljot Singh Bakshi](https://www.udemy.com/course/azure-ai-cloud-developer/) | June 2026 | 15 sections, 135 lectures, 18h5 |
| [Scott Duffy course](https://www.udemy.com/course/ai200-azure/) | May 2026 | 11 sections, 29 lectures, 3h54 |
| [Scott Duffy practice](https://www.udemy.com/course/ai200-tests/) | August 2026 | Four 25-question sets; claimed August 28 exam update not corroborated by Microsoft's baseline |

These observations establish catalog metadata, not content quality, completeness,
question originality or exam difficulty. The [Whizlabs catalog page](https://www.whizlabs.com/microsoft-azure-ai-cloud-developer-associate/)
now exists, correcting the old missing-product note; retrieval exposed only its
title. Counts, duration and paid content remain unverified. Bounded Pluralsight
and MeasureUp searches did not identify dedicated current offerings; absence from
that search is not proof of absence. Reactor, Azure-Samples and broad architecture
references remain discovery/context resources, not audited end-to-end courses.

## Corrections and learning additions

- **Containers and identity:** distinguish ACR RBAC/ABAC repository roles,
  catalog-listing scope and task source identity. Explain sidecar versus legacy
  App Service settings. Correct the required AKS workload-identity pod label and
  state its ServiceAccount/federation prerequisites. Separate ingress traffic
  routing from independent background consumers and aggregate connection demand.
- **Data and replay:** add Cosmos vector dimensions/index thresholds and current
  policy-change boundaries. Separate .NET/Java processor, Python managed trigger
  and Python pull reader. Explain latest-version deletion limits and explicit
  Functions retry policies. Add a local version/tombstone reducer, authorized
  recall calculation and pgvector iterative-scan version boundary.
- **Redis and messaging:** remove an unsupported old customer-cutoff date while
  retaining verified retirement dates. Add RediSearch clustering/module/eviction
  requirements. Separate durable work from Service Bus settlement failure, scope
  deduplication by tier/window/partition, and explain the implicit DLQ using its
  dedicated reference. The general locks article's enablement wording must not
  be read as a requirement to create that subqueue.
- **Operations:** distinguish the September 2026 Linux Functions v3/SBMP/legacy
  SDK milestones from later plan retirement. Scope Event Grid retry details to
  Basic push destinations. Add secret-reference refresh/pinning, explicit Python
  App Configuration refresh and sampling-aware telemetry interpretation.
- **Exercises:** add six worked examples, two offline artifact labs and all
  48 answer explanations. Keep cloud execution separate from static syntax and
  synthetic arithmetic. The sequential reducer does not establish concurrent
  atomicity or exactly-once external effects.

The guide places primary references beside each applied claim. Only the named
sections of long references were audited; retained broad pages were refreshed
without exhaustive rereading. Source-specific notes in the registry and operation
receipt document that boundary.

## Redis documentation conflict

The [creation guide](https://learn.microsoft.com/en-us/azure/redis/quickstart-create-managed-redis)
says clustering policy cannot change after creation. The
[database update contract](https://learn.microsoft.com/en-us/rest/api/redis/redisenterprisecache/databases/update?view=rest-redis-redisenterprisecache-2025-07-01)
permits an update when the existing policy is `NoCluster`; OSS/Enterprise policy
changes require database deletion. The [architecture guidance](https://learn.microsoft.com/en-us/azure/redis/architecture)
also describes size and geo-replication constraints. This review does not infer a
universally supported in-place migration from those conflicting instructions.
The guide teaches choosing the required policy/module at creation and confirming
an exact existing-database conversion path. No database changes were attempted.

This unresolved support question keeps the freshness outcome blocked and the
program outcome `reviewed-with-blockers`; it does not prevent publishing the
verified corrections. An October 5 follow-up is registered.

## Blog intake

[Sanket Achari's September 15 Microsoft engineering article](https://devblogs.microsoft.com/powerplatform/azure-managed-redis-migration/)
was read through its main content. The guide adds an original worksheet for L1
lookup order, reconnect/authentication behavior, warming scope and rollback.
Reported savings and linked .NET code were not reproduced or generalized to
Python. A Container Apps TCP blue-green blog candidate exposed only a shell and
was not accepted as a reviewed learning source.

## Maintenance and validation

The existing weekly/manual workflow checks sources, objective hashes and dated
events, then prepares the next review queue. It does not independently perform
this semantic review or execute learner infrastructure. AI-200 adds follow-ups
for September 30 runtime/protocol deadlines, October 1 course/catalog evidence and
October 5 Redis conversion support. The current learning catalog is synchronized
from the guide; prior review dates/hashes/outcomes are preserved as historical
records. The accepted objective/status snapshots need no replacement.

The operation receipt is
`ADLC_Docs/operations/2026-09-28-ai-200-deep-review.json`. It records all 27
objective mappings, source observations, findings, offline checks and the actual
repository/site validation result. HTTP reachability alone is not evidence that
paid lessons, video content or an entire linked reference were reviewed.
