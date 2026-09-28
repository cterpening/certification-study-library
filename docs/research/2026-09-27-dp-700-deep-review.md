# DP-700 deep review — September 27, 2026

The complete [guide](../../guides/DP-700-implementing-data-engineering-solutions-microsoft-fabric.md)
was read and **54 published October objectives in ten groups** were mapped.
July 21 remains the accepted baseline. The October 19 terminology revision is
recorded separately, with historical snapshots and the effective-date recheck intact.

## Learning improvements

Four original worked examples teach key reconciliation despite matching counts,
CDF before/after interpretation, late-arrival time adjustment and queue versus
execution latency. The guide now has **ten labs and 44 answered checks**, with
clearer explanations of:

- Copy job reset, NULL watermarks, deletes, net CDC and preview SCD Type 2.
- CDF bootstrap, retained history and destination write contracts.
- OneLake grants/engine paths and source-specific mirroring security boundaries.
- Airflow pool lifecycle, networking and preview deployment limitations.
- Eventstream SQL time policies and shortcut acceleration limits.
- Monitoring history, missing diagnostics and scheduled notification coverage.
- V-Order defaults, VACUUM, cache evidence and runtime/table compatibility.

Eight synthetic arithmetic/set assertions passed locally. No Fabric, SQL, KQL,
Spark, streaming, Copy job, gateway or runtime workflow was executed. The labs
describe exercises for an appropriate test environment, not completed platform tests.

## Blog decision

Ye Xu's **Simplify data movement with Copy job: more control, more flexibility**,
Microsoft Fabric Updates Blog, May 26, 2026, supports a mode-switch/reload exercise.
Its public article text was reviewed via web search after direct retrieval of the
migrated page was blocked. Current product documentation governs reset behavior,
connector support and preview status. Screenshots and tenant steps were not tested.
The guide supplies the attributed link, estimated study time and exercise.

## Maintenance and evidence

An October 1 research checkpoint checks the planned late-September Runtime 2.0
default rollout; it is not a promised vendor cutover date. Existing ADBC checkpoints
already cover DP-700. Relevant recent Fabric release entries were checked against
linked product guidance; unrelated release entries were not exhaustively reviewed.

`ADLC_Docs/operations/2026-09-27-dp-700-deep-review.json` retains prior records,
guide/objective hashes, detailed objective mappings, source observations, findings,
blog decisions and validation results. The public Learn path module lists were
reviewed, but their earlier 27h49 duration total was not independently reverified.
Paid book/Udemy and migrated blog pages blocked direct retrieval. Public provider
metadata does not establish that paid content or assessments were completed.

Research and repair used the same AI context. Independent and human review remain
pending, as do platform lab execution and environment-specific rollout checks.
Publication uses unit tests, repository checks, strict site build, generated-site
validation and a diff check. The [Microsoft review tracker](../MICROSOFT-REVIEW-STATUS.md)
continues to show the remaining queue and unresolved blockers.
