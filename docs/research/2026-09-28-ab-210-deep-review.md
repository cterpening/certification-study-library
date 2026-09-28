# AB-210 deep review — September 28, 2026

The complete [AB-210 guide](../../guides/AB-210-accelerating-sales-pipelines-ai-dynamics-365.md)
was read and mapped to **46 detailed objectives in twelve groups**. This pass adds
six worked examples, two labs (ten total), 44 answer checkpoints and two qualified
blog exercises. It corrects the transition citation and develops pricing, assignment,
scoring, agent handoff, capacity, knowledge, retirement, research and channel decisions.

This is same-context AI research and repair. Twelve offline assertions passed;
no Dynamics environment, paid content, agent, mailbox, email/SMS, phone call,
mobile application, predictive model or platform pricing engine was exercised.
Independent human review remains pending. The guide remains **review-required**
because two official documentation contradictions could not be resolved.

## Exam, lifecycle and resources

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-210)
still has the June 18, 2026 page date, without a separate skills-effective date.
Objective and status extraction are unchanged; accepted snapshots were preserved.
The [credential page](https://learn.microsoft.com/en-us/credentials/certifications/d365-sales-ai-consultant-associate/)
still describes a beta exam, 120 minutes, seven languages, delayed beta scoring and
no available Practice Assessment. No GA date was inferred.

The guide previously cited August Partner Center announcements for the MB-280
replacement. The fetched August page describes different certifications. The
[July skilling announcement](https://learn.microsoft.com/en-us/partner-center/announcements/2026-july)
supports the MB-280-to-AB-210 mapping, so the guide now links there. An unsupported
course-component replacement assertion was removed.

Four current Learn paths expose **13 modules: 3 + 3 + 4 + 3**. Their former total of
12 hours 3 minutes is retained as historical because the retrieved path pages do
not expose those durations. The course lists three days and seven languages.
Both previously cited Udemy listings were access-blocked; current content,
duration, assessment originality and completeness were not verified. The partner
hub returned a shell. Targeted searches did not verify an exact new Pluralsight,
O'Reilly, MeasureUp or Whizlabs AB-210 offering; this is not a claim that none exists.

## Objective coverage

Each detailed bullet has a hashed mapping in the operation record. The groups are:

| Group | Objectives | Teaching reviewed or expanded |
|---|---:|---|
| Configure Sales | 7 | Environment, mailbox, process, timeline, import, security and collaboration |
| Product catalog | 2 | Families, units, currency, pricing and privilege inheritance |
| AI-first strategy | 4 | Workflow outcomes, Dataverse model, analytics and plan differences |
| Agent prerequisites | 2 | Identity/settings, capacity and current meter boundaries |
| Intelligence and insights | 8 | Sequences, assignment, conversations, scoring, relationships, summaries, forecasts and goals |
| Lead generation/nurturing | 2 | Qualification experience and eligible predictive-model history |
| Qualification Agent | 4 | Modes, setup, handoff evidence and monitoring |
| Opportunity management | 4 | Commercial data, pipeline, agent scope and configuration |
| Close Agent | 4 | Historical setup, run evidence, escalation and retiring-product continuity |
| Research Agent | 3 | Questions, reader access, source context and reconciliation |
| Supporting services | 3 | Mobile, Teams dialer and SMS integration boundaries |
| Power Platform extension | 3 | Flows, embedded apps/controls, Power BI, identity and ALM |

## Learning additions and repairs

The six synthetic examples make learners calculate or distinguish:

1. A 25% markup versus 25% margin on a cost of 80, with explicit rounding assumptions.
2. Entity-scoped seller capacity and the first matching assignment rule.
3. Filtered training eligibility: a raw qualified count of 44 becomes 39 after exclusions.
4. The intersection of selected handoff criteria, distinct from research-only completion.
5. Initial research, repeated refresh and another agent's shared consumption against a reserve.
6. A supplied currency conversion and source-row reconciliation for uploaded research data.

Current procedures now anchor these decisions. In particular, the guide separates
agent handoff, CRM qualification and booked revenue; controlled test inboxes from
public company research; operational views from governed analytics; provider sending
from SMS callback verification; and legacy dialer removal from Teams dialer support.
No synthetic assumption is presented as a Microsoft rate, live exchange rate or
observed tenant outcome.

The [Sales retirement ledger](https://learn.microsoft.com/en-us/dynamics365/sales/deprecations-sales)
is applied to older collaboration and intelligence exercises. Close Agent remains in
the exam objectives while its new-instance cutoff is September 30 and existing-instance
removal is October 30. The [Sales Development activation procedure](https://learn.microsoft.com/en-us/dynamics365/sales/sales-dev-agent/activate-agent)
has separate preview, license, identity and Frontier requirements. The guide keeps
historical Close setup as a tabletop exercise and asks for an explicit continuity plan;
the replacement name alone does not establish production readiness or automatic migration.

## Useful blog intake

- **Julie Strauss, December 11, 2025:** the public [Sales Qualification benchmark article](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2025/12/11/dynamics-365-sets-the-bar-for-agentic-sales-qualification-on-new-benchmark/)
  supplies an evaluation exercise. Its commercial results were not reproduced or
  treated as promised lift; current product procedures qualify older mode descriptions.
- **Paramita Chatterjee, January 28, 2026:** the public [data-entry and exploration article](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/01/28/agentic-ai-transforming-dynamics-365-sales/)
  supplies an acceptance/reconciliation exercise. Current form-fill documentation
  qualifies the historical UI, product-specific status and protected-input limits.

The main articles were read. Linked benchmark implementation, videos, paid course
interiors and demonstrations were not executed. Existing commercial candidates were
not promoted to verified recommendations based on search snippets or question counts.

## Unresolved evidence

The [knowledge-source page](https://learn.microsoft.com/en-us/dynamics365/sales/configure-sqa-knowledge-source)
both denies Opportunity Agent custom-field support and describes configuring it in
the same section. The guide leaves that capability unverified for a required design.
Separately documented Qualification Agent custom criteria remain distinguished.

The [Close setup page](https://learn.microsoft.com/en-us/dynamics365/sales/configure-sales-close-agent)
says deactivation lets existing orchestrations continue. The [management page](https://learn.microsoft.com/en-us/dynamics365/sales/manage-sales-close-agent)
says in-process records will not be processed after stopping. This is not resolved by
borrowing Qualification Agent's separate shutdown behavior. The guide requires actual
pending-run/outbound verification before relying on containment.

Six maintenance events cover September 30 creation cutoff, October 23 removal
readiness, October 5 checks for each contradiction and Qualification Agent rollout,
and October 15 beta/blueprint status. Month-only historical release-plan dates do not
prove tenant availability. Neither unresolved item is marked as a clean validation pass.

## Evidence and validation

The guide has 46 registered external citations: 44 reachable, two access-blocked,
and none missing/error. This pass adds 29 source records and associates the existing
July partner announcement with AB-210. Twenty supported findings were applied;
two contradictions remain blocked. A reachable page alone is not a content review.

`ADLC_Docs/operations/2026-09-28-ab-210-deep-review.json` records per-objective mappings,
previous records, actual fetch results/timestamps/hashes, findings, accepted article
scope, limits and the local validation results. Source/catalog metadata, link health,
freshness findings, review records, progress and dated events accompany the guide.
The September 1 passed source review is preserved as historical evidence; the new
September 28 source review is blocked by the two unresolved vendor contradictions.

The publication gate is unit tests, repository validation, strict site build, generated
site validation and diff checking. Completion of those checks validates the repository
and publication, not live Sales functionality. The deep-review receipt records completed
research with blockers and keeps the remaining initial reviews eligible in the queue.
