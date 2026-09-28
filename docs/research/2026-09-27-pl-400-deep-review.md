# PL-400 deep review — September 27, 2026

The complete guide and retained March 19 objective snapshot were read. All **88
published October replacement objectives in 15 groups** were mapped to guide
sections. The PL-400 study-guide URL now contains that future scope; this does not
replace the accepted March baseline before the transition. October registration
and final delivery dates remain explicit.

## Learning improvements

Sections 1–6 retain PL-400 preparation; Section 7 expands AB-400 transition work
for code apps, APIs and agent integration. Current documentation corrected or
sharpened several important boundaries:

- Personal pipelines cannot be extended; advanced requirements need a custom host.
- Connector import format and OAuth support depend on the particular route.
- Attribute presence is different from a changed business value, and database
  rollback cannot undo a completed external side effect.
- Full synchronization does not replay historical deletions, and elastic Upsert
  does not raise separate Create/Update events.
- Managed-identity version 2 uses certificate distinguished-name hashes.
- Background operations preserve plug-in timeouts and do not cancel running work.
- Code-app CSP, publication grants, flow types and environment variables have
  distinct boundaries; agent connector, client-library, MCP and A2A routes differ.

There are **four worked examples, ten labs and 44 answered checks**. Four synthetic
attribute/state-set assertions passed locally. No SDK, platform, Azure, tenant or
agent lab was executed.

## Blog decision

Suyash Kshirsagar's **Dataverse Skills: Your Coding Agent Now Speaks Dataverse**,
published April 1, 2026, was accepted for its tool-orchestration explanation.
The public article was read. The
[guide](../../guides/PL-400-microsoft-power-platform-developer.md) adds a synthetic
two-table review exercise and qualifies setup claims using current preview,
privilege, consent and client-allowlisting documentation. No plugin was installed,
video played or tenant demonstration executed.

Tiffany Treacy's September 17 Power Platform update was used as a release and
developer-documentation discovery channel. Relevant primary pages were followed;
its product-level announcements are not blanket GA evidence for every feature.

## Evidence and limits

`ADLC_Docs/operations/2026-09-27-pl-400-deep-review.json` preserves prior records,
guide hashes, objective positions/hashes and mappings, source observations,
findings, blog intake and validation. The objective count describes October scope;
the March snapshot and effective-date follow-up remain intact.

The Udemy page was automation-blocked. Public course metadata confirms five days
of instructor-led delivery, but the earlier 25-hour Learn-path total is historical.
Reachable catalog/practice shells do not demonstrate paid lesson access or an
assessment attempt. Preview, host, identity, licensing and deployment behavior must
still be tested in a suitable tenant. Research and repair used the same AI context;
independent and human review remain pending.

Publication uses the unit-test, repository, strict site-build, generated-site and
diff checks. See the [Microsoft review tracker](../MICROSOFT-REVIEW-STATUS.md) for
the remaining queue.
