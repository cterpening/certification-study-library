# PL-300 deep review — September 27, 2026

The complete [guide](../../guides/PL-300-microsoft-power-bi-data-analyst.md) was read
and **78 objectives in eleven groups** were mapped. April 20 remains the effective
date, with unchanged weights and detailed objectives. The fetched page reformats
the audience profile and line wrapping. That editorial snapshot was accepted only
after comparison; the evidence retains its previous text and both hashes. Older
audits now reference a byte-identical archived snapshot. Their original hashes,
dates, checks, findings and verdicts remain unchanged; the current guide review
references the accepted snapshot. The process is documented in
[Automation](../AUTOMATION.md#review-checklist-for-an-objective-change-pr).
The original September 1 source review is retained with its original link counts.
The validator now selects the source review applicable to an audit's date, with
regression coverage for superseded baselines, blocked reviews and altered bytes.

## Learning improvements

Four original worked examples explain filter replacement versus intersection,
overlapping distinct-count totals, previous visible year versus prior calendar
year, and additive RLS roles. The guide now has **ten labs and 44 answered checks**.
It also clarifies:

- Deterministic Power Query deduplication and buffering trade-offs.
- Ordinary Import columns versus user-context evaluation and Direct Lake preview.
- Direct Lake variants, framing, ADBC connection routes and relationship security.
- Visual-calculation export, alert and model-reuse limitations.
- Copilot capacity/surface requirements and hidden-bookmark scope.
- Page refresh, data/schema refresh, file synchronization and schedule failures.
- Actual-consumer RLS tests, hidden presentation and label-protected export routes.

Eight synthetic arithmetic/set assertions passed locally. No Power BI, DAX/M engine,
gateway, Copilot, security, export or notification lab was executed. The examples
give expected outcomes to verify in a suitable test environment.

## Blog and release decisions

Marco Russo and Alberto Ferrari's SQLBI article **Analyzing the performance impact
of visual calculations**, July 27, 2026, supports a measured comparison at different
visual grains. The public article was read; downloadable models, paid material,
screenshots and benchmark results were not independently executed.

The Microsoft Power BI Team's September **Q&A retirement timeline update** explicitly
extends retirement from December 2026 to February 2027. Public article text was
reviewed through web search after direct retrieval was blocked. Updated Learn
limitations agree; an older visual page retains December wording. The guide records
the extension and the capacity, embedded and sovereign-cloud limits of alternatives.

The current observed Power BI monthly summary is August 2026. Relevant entries
include calculated columns, refresh controls, themes, bookmarks and the October
old-file-picker transition. This review does not invent a September release.
The guide supplies the attributed blog links and learning exercises.

## Maintenance and evidence

New research checkpoints cover October's old OneDrive/SharePoint Desktop save/share
transition and the extended February Q&A retirement. Their dates are recheck dates,
not invented vendor cutover days. Existing ADBC checkpoints remain applicable.

A bounded DP-600 follow-up qualifies its ordinary Import calculated-column advice
and answer. Its report, source association, guide hash and review evidence were
updated so that the shared correction remains traceable.

`ADLC_Docs/operations/2026-09-27-pl-300-deep-review.json` records prior catalog data,
guide/objective hashes, the accepted editorial snapshot, all objective mappings,
source observations, findings and validation. The earlier Learn duration total
was not independently reverified. Coursera's current overview estimates about
40 hours; the displayed module estimates sum to 37. Public provider metadata and
the Microsoft lab repository README do not establish course or lab completion.

An O'Reilly page, two Udemy pages and the retirement blog blocked direct retrieval.
Automatic-page-refresh setup text remains narrower than its mode matrix; actual
mode, capacity and connection behavior requires environment testing. Research and
repair used the same AI context; independent and human review remain pending.

Publication uses unit tests, repository checks, strict site build, generated-site
validation and a diff check. The [Microsoft review tracker](../MICROSOFT-REVIEW-STATUS.md)
keeps the remaining work visible.
