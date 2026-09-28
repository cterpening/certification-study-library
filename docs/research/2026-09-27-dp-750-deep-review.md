# DP-750 deep review — September 27, 2026

The complete [guide](../../guides/DP-750-implementing-data-engineering-solutions-using-azure-databricks.md)
was read and **77 published October objectives in twelve groups** were mapped.
The accepted March 11 baseline remains separate from October 19 preparation:
bundle/CLI terminology changes, deletion vectors leave the clustering bullet,
and the four domain weights remain unchanged. The credential page now lists
ten languages, correcting the guide's English-only statement. The assessment
remains 120 minutes and the official course four days.

## Learning changes

Four original examples explain how a pipeline identity can persist a restricted
result, why file tracking does not guarantee unique business keys, how stable
sequence ordering handles late changes, and what warn/drop/fail quality actions
actually publish. The guide now provides **ten labs and 44 answered checks**.

Corrections and additions cover:

- Complete catalog/schema/volume paths and deterministic SQL ordering.
- Azure connector identity versus Databricks principal permissions.
- ABAC query, pipeline and sharing identities; dependency failures and Beta scope.
- Auto Loader schema/restart/rescue behavior, CDC modes and retained source state.
- Pipeline unit-test redirection, external IO, permissions and governance fidelity.
- Direct bundle deployment, omitted-field defaults and migration plan review.
- Continuous maintenance windows, restart exceptions and notification destinations.

Nine synthetic ordering/count/set assertions and one Python syntax parse passed
locally. No Spark/SQL engine, Azure/Databricks workspace, governance, sharing,
pipeline, bundle or CDF lab was executed. The SQL is illustrative and names its
setup and input assumptions; the new exercises require an isolated environment.

## Blog and course decisions

Two Databricks articles are linked in the guide with attribution and exercises:

- The May 13 ABAC/governed-tags/classification announcement by Adriana Ispas,
  Kristen Wilder, Jacqueline Li, Corey Sunwold, Menglei Sun and Viswesh Periyasamy.
  It supports a taxonomy and responsibility exercise; current Azure documentation
  qualifies its immediate-protection language with tag propagation delays.
- The February 10 Azure Lakeflow overview by Joanna Zouhour and Katie Cummiskey.
  It supports an ingestion/transformation/orchestration design exercise. Its
  customer performance and cost claims are not adopted as expected lab outcomes.

Both public article texts were read. Images, videos, linked downloads and customer
benchmarks were not independently validated. Pluralsight's public page supplies
the current observed 1h39 listing, dated July 23, 2025; its credential-passthrough
and mount topics need comparison with current governed-storage guidance.
Three O'Reilly pages and Udemy search blocked retrieval, so their earlier metadata
is labeled historical. No paid lessons or signed-in Practice Assessment were used.

## Release and documentation boundaries

Relevant September release entries were checked against detailed documentation.
Automatic CDF's GA announcement is distinguished from its planned regional rollout
through October. Direct-engine migration depends on the installed CLI and deployment
state. New research checkpoints cover both transitions.

Direct-view ABAC support remains uncertain: the metastore Beta page lists view
targets, while the general requirements page excludes policies directly on views.
The guide teaches the supported base-table/view session-user path, excludes
direct-view implementation instructions, and schedules an October 1 recheck.
Pipeline materialization and exemption guidance is route-specific and requires
integration tests. These limitations are preserved rather than treated as proven
support for every engine or identity.

`ADLC_Docs/operations/2026-09-27-dp-750-deep-review.json` records prior catalog data,
guide/objective hashes, all objective mappings, source observations, findings,
blog decisions and publication checks. A guessed deployment-state URL returned
404 during discovery and was rejected; the relevant section is on the verified
direct-engine page. All guide citations use registered sources.
The 72 unique guide links include 68 reachable sources, four access-blocked
sources and no missing/error results. Reachability does not prove lesson completion.

Research and repair used the same AI context. Independent and human review remain
pending. Publication requires unit tests, repository validation, a strict site
build, generated-site validation and a diff check. The
[Microsoft tracker](../MICROSOFT-REVIEW-STATUS.md) records the remaining program.
