# DP-800 deep review — September 27, 2026

The complete [guide](../../guides/DP-800-developing-ai-enabled-database-solutions.md)
was read and **73 published October objectives in eleven groups** were mapped.
The accepted March 12 baseline remains separate from October 19 preparation.
The live October change-mechanism objective still includes CES, correcting the
earlier removal note in the guide and maintenance schedule. Domain weights are
unchanged. The current credential lists ten languages and 120 minutes, and the
official course is three days.

## Learning changes

Five original worked examples explain RLS update protection, expired change
watermarks, stale embedding results, authorized retrieval recall and reciprocal
rank fusion. The guide now offers **ten labs and 44 answered checks**.

Corrections and additions cover:

- An AFTER UPDATE RLS block and trusted session-context initialization.
- DAB 2.0 authentication defaults, role inheritance, claim propagation, automatic
  entities, on-behalf-of identity and incompatible runtime caching.
- Change Tracking snapshot consistency, deletion recovery, SQL-trigger failure
  behavior and platform-specific CES migration requirements.
- Embedding-only external model objects, character-based chunking and conditional
  source/model version checks before publishing generated vectors.
- Exact/approximate query planning, current vector index support and recall measured
  over the same authorized population; filtered recall is distinct from disclosure.
- Fabric SQL feature and mirroring boundaries, plus REST permission/status handling.

Ten synthetic permission, retention, version, recall, ranking, overlap and duration
assertions passed. One illustrative JSON block parsed successfully. No SQL engine,
DAB schema/runtime, Azure/Fabric tenant, model, RLS, API or event-stream lab ran.
These checks do not establish live product behavior. The new labs identify what a
learner must verify in an isolated environment.

## Blog and course decisions

Two Microsoft SQL blog articles were read and linked with focused exercises:

- Pooja Kamath's August 17, 2026 vector-optimizer article supports a comparison of
  exact and approximate plans over the same filtered corpus. Current platform,
  index-version and region requirements control applicability.
- Jerry Nixon's April 8, 2026 SQL MCP Server article, as observed September 27,
  supports an entity/tool/role matrix. Permissive anonymous demonstration settings
  are qualified using current DAB 2.0 security documentation.

Neither article's videos, downloads or performance claims were independently
executed or benchmarked. Public Pluralsight listings now show six courses and
eight rounded path hours, including Lucian Lazar's September 21 AI course;
the six listed durations sum to 7h36. Rudi Bruchez's focused vector-index course
lists 1h19 and March 30, 2026. Paid lessons were not reviewed.

The official eleven-lab index, seven-session Reactor schedule and four sample
repository landing READMEs were inspected; videos and individual sample files
were not executed. Microsoft Learn path durations remain explicitly historical.
O'Reilly and Udemy blocked retrieval. Whizlabs and the official Practice Assessment
exposed only public shells; no signed-in assessment or quiz was reviewed.

## Release and documentation boundaries

The vector datatype page gives a 1998-dimension limit, while SQL Server 2025 release
notes describe float16 preview up to 3996. The guide preserves this disagreement,
uses the conservative shared bound and requires engine/build/base-type/driver
verification before relying on a higher limit. A research checkpoint is scheduled.

CES target naming differs across Azure SQL/Fabric and SQL Server/Managed Instance.
Existing AMQP groups have a documented April 2027 end month, not an established
exact day. Separate checkpoints cover target naming and migration preparation;
the guide includes pending-change draining and coordinated migration risks.

`ADLC_Docs/operations/2026-09-27-dp-800-deep-review.json` records prior catalog
data, guide/objective hashes, all objective mappings, source observations,
findings, blog decisions and publication checks. All 94 unique guide citations are
registered: 92 were reachable, two were access-blocked and none was missing/error.
Research and repair used the same AI context; independent and human review remain
pending. Publication requires unit tests, repository validation, a strict site
build, generated-site validation and a diff check. The
[Microsoft tracker](../MICROSOFT-REVIEW-STATUS.md) records the remaining program.
