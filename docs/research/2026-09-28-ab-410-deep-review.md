# AB-410 deep review — September 28, 2026

The [AB-410 guide](../../guides/AB-410-building-intelligent-applications.md) was read
in full and mapped to **48 detailed objectives across seven groups**. It now has
six worked examples, ten labs, 48 answered checks and two focused Power Platform
blog exercises. Eighteen offline assertions passed. SAP prompt-knowledge support
remains an unresolved documentation gap.

This is same-context AI research and repair; independent human review is pending.
No tenant, app, Power Fx runtime, Dataverse write, flow, approval, model, agent,
deployment, billing or paid lesson was executed. The offline models do not prove
concurrency safety, query delegation, service timing, model quality or authorization.

## Exam and learning baseline

The [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-410)
retains its May 15, 2026 page date without a separate skills-effective date or
announced revision. All **48 detailed objectives match the prior snapshot** after
whitespace normalization. The old snapshot abridged the audience section; the
current accepted snapshot restores the complete source text and canonical heading
and wrapping format. This is not evidence of a newly announced exam revision.

Original objective/status bytes are archived under
`data/objective-snapshots/ab-410-2026-09-01-official-objectives.txt` and the corresponding
status JSON. Historical review/audit references locate those archived bytes;
their original dates, hashes, outcomes and substantive evidence remain unchanged.

The [credential](https://learn.microsoft.com/en-us/credentials/certifications/intelligent-applications-builder-associate/)
still lists an active English, 120-minute exam and no Practice Assessment. The
[course](https://learn.microsoft.com/en-us/training/courses/ab-410t00) lists three days
and thirteen languages. Its four learning paths expose **17 modules: 3 + 3 + 7 + 4**.
Their earlier 15h26 total is historical; current fetched outlines do not expose
those runtimes. The guide's 40–70-hour build-and-study budget is editorial.

The indexed public [Udemy page](https://www.udemy.com/course/pl-100-microsoft-power-platform-app-maker-ms/)
shows Phillip Burton, a September update, 38 sections, 213 lectures and **21h09**
total. Its description still says approximately 7h30 of AB-410 and promises removal
of old PL-200 content from September 1. That inconsistency prevents treating the
total as verified exam-only instruction. Direct automated access was blocked;
the indexed public outline was available. Paid lessons and removal were unverified.
Whizlabs and the partner/video pages returned content shells. Bounded exact-exam
searches of Pluralsight, O'Reilly and MeasureUp found no offering; this is not
proof of absence from the entire market.

## Objective coverage

Every bullet has a hashed mapping in the operation record.

| Group | Count | Teaching and evidence |
|---|---:|---|
| AI-enabled solution design | 5 | Requirements, built-ins, extensions, environments and ALM |
| Dataverse data models | 10 | Tables, columns, relationships, prompts, summaries, forms/views and access |
| Model-driven apps | 7 | Composition, generated pages, access, charts and dashboards |
| Canvas apps | 8 | Data, usability, automation, reuse, state, errors, monitoring and agents |
| Cloud flows | 6 | Triggers, connectors, approvals, actions, control and troubleshooting |
| Prompts and models | 8 | Contracts, apps/flows, knowledge, settings, inputs and model use |
| Business/process logic | 4 | Rules, process flows, derived columns and surface selection |

## Material corrections and additions

- **Freshness:** add prompt-column state interpretation and distinguish stored
  output from a new successful generation. Explain summary scope, language,
  solution transport and Dynamics-specific table exceptions; correct the case
  scenario accordingly.
- **Release and access:** distinguish pipeline artifacts from data recovery,
  generated-page dependencies from editing history, authoring routes from regional
  limits, and bound record IDs from authorization. Test protected columns with
  nonadministrator personas and consider derived-output disclosure.
- **App correctness:** add incomplete-prefix examples, typed reuse and explicit
  error paths. A successful local query or type check does not establish complete
  data or valid business meaning; an error handler does not roll back prior effects.
- **Automation:** clarify update-column inclusion, action identities and operation
  keys. Separate interactive response deadlines from persisted business requests
  and long approvals.
- **AI implementation:** qualify older model references using current settings,
  distinguish per-call context from total interaction use, and explain saved JSON
  contracts, bounded knowledge and calibrated outcome measures.
- **Licensing and business logic:** preserve active-contract credit entitlements
  through their documented term, separate context-specific consumption, and add
  formula/rule/rollup timing and access boundaries.

Current implementation sources are linked beside the changed guide explanations.
Long references were reviewed in the sections identified by individual source
notes; retrieval was not treated as a complete audit of all linked procedures.

## Unresolved evidence gap

The [prompt-knowledge article](https://learn.microsoft.com/en-us/ai-builder/use-your-own-prompt-data)
names SAP in its connector instructions but omits it from the explicit support
limitations. This review does not infer SAP support or exclusion from either
sentence alone. The guide keeps that path unverified and schedules clarification.
Other context, retrieval and relationship limits remain useful and documented.

## Blog intake

Both accepted readings are bounded sections of long vendor roundups, not full
article or linked-tool audits.

- [Tiffany Treacy, September 17](https://www.microsoft.com/en-us/power-platform/blog/power-apps/whats-new-in-power-platform-september-2026-feature-update/):
  the model app-builder, form-embedding and preview connector sections support an
  original 45–75-minute persona/artifact/binding review worksheet. No external
  coding tool, app creation or deployment was executed.
- [Tiffany Treacy, May 14](https://www.microsoft.com/en-us/power-platform/blog/2026/05/14/whats-new-in-power-platform-may-2026-feature-update/):
  the UDT section supports an original 30–60-minute type-versus-business-validation
  worksheet, checked against current App.Formulas guidance. No Power Fx runtime
  or linked code was executed.

These exercises supplement the blueprint; neither publication nor a GA headline
establishes support for every associated preview feature or a particular tenant.

## Verification and follow-up

Eighteen assertions cover prompt statuses, prefix recall, operation keys,
response/approval deadlines, outcome denominators, review workload, stale totals
and catalog arithmetic. They use synthetic values and do not simulate the actual
Power Platform implementation. Labs remain learner exercises.

Three events recheck October 5 SAP support, October 12 feature/catalog boundaries
and November 1 credit transition. The shared learning catalog is synchronized
from the guide. Exact citation/fetch counts and executed repository/unit/site
checks are recorded in `ADLC_Docs/operations/2026-09-28-ab-410-deep-review.json`.
HTTP reachability, indexed visibility, full content access and semantic review
are recorded as distinct evidence.

All **48** guide citations are registered: **47** returned reachable HTTP responses,
one direct commercial fetch was blocked, and none were classified missing/error.
The Whizlabs, partner and video shells remain content-access limitations despite
their successful HTTP responses.
