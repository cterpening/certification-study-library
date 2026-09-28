# DP-600 deep review — September 27, 2026

The complete guide was read and **41 published October objectives in seven groups**
were mapped. July 21 remains the accepted baseline. The live page contains the
October 19 capitalization change; historical snapshots and follow-up are preserved.

## Learning improvements

Four worked examples teach additive OneLake grants, duplicate-dimension join totals,
Direct Lake framing and weighted percentage totals. The guide now clearly separates
OneLake's no-fallback behavior from SQL-based Direct Lake, and explains:

- Supported engine/identity paths and sensitive model metadata.
- Unenforced Warehouse keys and transformation quality checks.
- Eventhouse batching/backfill/retention versus Import-model Delta exports.
- Active relationship requirements for RLS and incremental-refresh deletion limits.
- September result-set cache evidence and cloud/gateway ADBC differences.

There are **ten labs and 44 answered checks**. Six synthetic arithmetic/set assertions
passed locally. No Fabric tenant, Power BI engine, SQL/KQL engine or driver lab was
executed. Three ADBC research checkpoints were added for the planned October 2026,
early-Q1 2027 and spring-2027 milestones; their review dates are not claimed vendor
cutover dates.

## Blog decisions

The guide adds two qualified readings:

- DataZoe's April 21, 2025 **Deep dive into Direct Lake on OneLake**, in Microsoft's
  Power BI Updates Blog, for live model/report editing and architecture. Substantial
  available public text was reviewed via web search; direct automated retrieval of
  the migrated page was blocked. Initial-preview and early-access restrictions are
  reconciled with current documentation.
- Chris Webb's April 5, 2026 **Role-playing dimensions revisited**, for design and
  version-specific investigation. The public article/discussion includes an April 9
  author acknowledgment of a web-editor bug. It is not presented as a verified
  deployment recipe.

Neither article's screenshots nor tenant/model procedures were independently
validated. Attribution, estimated reading time and original exercises appear in
the [guide](../../guides/DP-600-implementing-analytics-solutions-microsoft-fabric.md).

## Evidence and limits

`ADLC_Docs/operations/2026-09-27-dp-600-deep-review.json` records prior catalog data,
guide hashes, objective hashes/positions and mappings, source observations, blog
decisions, findings and validation. The objective count describes the live October
version, not a newly accepted July snapshot.

Two paid books and the migrated Microsoft blog blocked direct retrieval. Public
Learn path/module pages did not independently reverify the earlier 23-hour-20-minute
duration total. No assessment, paid lesson or tenant workflow was completed.
Preview, engine, identity, rollout and workaround limits remain explicit. Review
and repair used the same AI context; independent and human review remain pending.

Publication uses unit-test, repository, strict site-build, generated-site and diff
checks. The [Microsoft review tracker](../MICROSOFT-REVIEW-STATUS.md) keeps the
remaining queue visible.

## PL-300 follow-up

The subsequent PL-300 review clarified section 3 and answer 29: stored refresh-time
columns describe the ordinary Import case. Other storage modes and user-context
columns can evaluate at query time. The current [calculated-column documentation](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-calculated-columns)
was associated with DP-600, and the evidence preserves the guide hashes before and
after this bounded correction. No engine execution was added; the publication gates
cover the correction with the PL-300 change.
