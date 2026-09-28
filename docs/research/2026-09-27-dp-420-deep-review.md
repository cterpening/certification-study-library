# DP-420 deep review — September 27, 2026

The whole guide was read and **all 56 published October 6 objectives in 12 groups**
were mapped to existing foundations and expanded transition teaching. The accepted
July 21 objective/status snapshots remain unchanged. The live English blueprint now
shows October scope, while the credential page retains the current exam description
and announces the future name/level change. The observed hash difference is expected;
it must not silently replace the baseline before the effective date.

## Learning improvements

- Expand October preparation for retrieval, grounding, durable memory, Agent Kit,
  masking, container copy, Fleet capacity/analytics and Fabric operational endpoints.
- Separate tenant authorization, partition routing and vector-index sharding; add
  colliding-thread and forged-scope tests plus current vector/HPK support limits.
- Correct latest-version change-feed bootstrap, TTL query visibility and physical
  deletion, same-SDK continuation-token behavior and backlog recovery arithmetic.
- Add current per-partition failover eligibility and exclusions; preserve backup,
  analytical-store and new-project Synapse Link boundaries.
- Distinguish July's C#/Java audience from October's C#/Python profile and qualify
  older course/practice alignment.

Four worked examples cover tenant isolation, retrieval recall, masking exposure and
net backlog drain. Two new labs bring the guide to **ten labs**. All 30 existing
questions now have answer checkpoints, with six new October scenarios: **36 answers**
in total. Executed cloud evidence is explicitly separate from a design worksheet.

## Blog decisions

Two public Microsoft articles were read and accepted with limits in the
[guide](../../guides/DP-420-designing-and-implementing-cloud-native-applications-using-microsoft-azure-cosmos-db.md):

- Sajeetharan Sinnathurai's **Introducing the Azure Cosmos DB Agent Kit**, January
  22, 2026: useful review workflow, but the constructor sample has an unmatched brace
  and a tenant/year key does not guarantee freedom from hot partitions. Current
  repository/release guidance governs installation and SDK details.
- James Codella, Shivam Atri and Haiyang Xu's **Sharded DiskANN for multitenant vector
  search**, April 24, 2025: useful partition/index distinction and comparative
  measurement method. Benchmark gains are workload-specific and some query examples
  reverse the `WHERE`/`ORDER BY` clause order. No sample or benchmark was copied as an
  executable recipe.

The guide provides attribution, reading estimates, original exercises and links to
current implementation guidance. Neither article was treated as exam content or as
proof of successful execution.

## Evidence and remaining limits

`ADLC_Docs/operations/2026-09-27-dp-420-deep-review.json` records prior catalog state,
before/after guide hashes, all 56 objective positions/hashes and section mappings,
source observations, blog decisions and validation. This count is the **upcoming
October version**, not a relabeling of the July objective inventory. Recheck activation
and naming on October 6 through the existing maintenance follow-up.

Four synthetic recall/backlog arithmetic assertions were checked offline. No Azure,
Fabric, emulator, retrieval benchmark, Agent Kit or infrastructure lab was executed.
Three paid catalog pages were blocked; a reachable catalog does not establish lesson
access or October assessment alignment. Feature/SDK/region constraints remain in the
guide, including vector/HPK guidance and preview copy jobs.

Research and repair used the same AI context; independent and human review remain
pending. The shared gate covers unit tests, repository validation, strict site build,
generated-site checks and diff checks. The
[Microsoft review tracker](../MICROSOFT-REVIEW-STATUS.md) records remaining certifications.
