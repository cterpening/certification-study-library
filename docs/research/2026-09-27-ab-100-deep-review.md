# AB-100 deep review — September 27, 2026

The [AB-100 guide](../../guides/AB-100-agentic-ai-business-solutions-architect.md)
was read in full and compared with all **74 detailed objectives in ten objective
groups**. The pass researched implementation gaps, reviewed the original exercises
and questions, and applied supported corrections. It adds **11 official sources**,
associates four existing sources with AB-100, and gives each of the 17 knowledge
checks an answer checkpoint. There are now 12 architecture exercises.

This is an AI research and repair pass in the same conversation context, not an
independent audit or human review. No tenant deployment, paid course interior,
partner-only training, or account-only assessment was tested. The guide's review
date describes this documented scope, not a guarantee that every product feature
was executed or every recommendation was independently validated.

## Exam and credential evidence

The [public blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-100)
now displays the October 14, 2026 English outline. Compared with the accepted July
22 snapshot, the differences are the effective-date heading, two additions of
“Microsoft” before Foundry Tools, and capitalization of “Service” in one ALM
objective. The detailed objective count, groups, and three domain weights are
unchanged. The saved July snapshot remains the historical baseline; the October
candidate was compared without silently replacing it before its effective date.

The [credential page](https://learn.microsoft.com/en-us/credentials/certifications/agentic-ai-business-solutions-architect/)
lists the Expert credential and an associate prerequisite. The [exam page](https://learn.microsoft.com/en-us/credentials/certifications/exams/ab-100/)
also lists MB-280 and PL-200, which are absent from the credential page. Both pages
contain an unrelated information-protection summary. The guide now warns about
these discrepancies, uses the dedicated blueprint for scope, and directs learners
to confirm ambiguous prerequisites with Microsoft. This conflict is retained as
a blocked freshness finding rather than selecting an unsupported answer.

The public [three-day course](https://learn.microsoft.com/en-us/training/courses/ab-100t00)
and [11-module learning path](https://learn.microsoft.com/en-us/training/paths/architect-agentic-ai-business-solutions/)
were readable. The path is now titled *Architect AI solutions for business
productivity*. The credential page's empty training widget does not establish
that these resources are unavailable.

## Coverage and repairs

| Objective group, paraphrased | Bullets reviewed | Guide locations and result |
|---|---:|---|
| Requirements and grounding | 3 | Parts 1–2: process suitability, data readiness, ownership, and reusable data contracts retained. |
| Enterprise strategy | 13 | Parts 3–5 and 7: CAF, CoE, portfolio, prompts, model customization, cross-platform design; runtime boundaries clarified. |
| Cost and value | 4 | Part 4: added a worked ROI/sensitivity example and a concrete managed-router decision and evaluation process. |
| Agent design | 16 | Parts 2, 5–7: added Foundry capability selection, event-trigger identity, and agent-feed privacy/approval distinctions. |
| Extensibility | 7 | Parts 3, 5–6 and 9: expanded MCP transport/authentication and computer-use identity, supervision, and administration. |
| Prebuilt apps and agents | 7 | Part 7: reviewed workload boundaries, finance-and-operations virtual knowledge and in-app help; retained current-verification limits. |
| Monitoring and tuning | 5 | Part 8: retained layered telemetry, outcome measures, feedback triage, and diagnosis by component. |
| Testing | 5 | Part 8: added native Copilot Studio evaluation constraints and a strategy for generating and independently checking synthetic test cases. |
| ALM | 6 | Part 9: separated standard-harness solution ALM from other runtimes and explained both Foundry publishing models. |
| Security and governance | 8 | Part 10: replaced a mismatched governance citation, retained authorization and threat-model controls, and strengthened exercise checks. |

The per-objective ledger identifies each bullet by position and normalized hash,
with a guide-section mapping. It does not reproduce a vendor question bank.

## Material implementation findings

- **Copilot Studio runtimes:** The [harness overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview)
  distinguishes three runtimes. Topic/solution guidance must be scoped to the
  standard harness; the GitHub Copilot harness name does not establish a GitHub
  service data boundary. The guide no longer implies one uniform deployment model.
- **Autonomous identity:** [Event-trigger documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-triggers-about)
  specifies maker credentials and the authentication requirements for autonomous
  actions. The guide now distinguishes that path from interactive user access.
- **Routing:** The [model-router concepts](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-router)
  and [implementation guide](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/model-router)
  support explicit eligible-model selection, evaluation, and configuration tracking.
  A fixed router version name alone is insufficient evidence of a frozen model pool.
- **Foundry ALM:** The [development lifecycle](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/development-lifecycle),
  [identity reference](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity),
  and [publishing migration guide](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/migrate-agent-applications)
  describe different resource generations. The guide now differentiates legacy
  application identities from identities created with new agent objects. Migration
  requires checking permissions and endpoint consumers; no retirement date was invented.
- **Agent feed:** The [implementation page](https://learn.microsoft.com/en-us/power-apps/user/supervise-agents-with-agent-feed)
  documents preview status, broad visibility for users with Agent Task table access,
  and different task semantics. An informational completed task is not evidence of
  prior approval. The guide and new exercise explicitly reject a confidential
  per-user approval design based only on this feed.
- **Generated pages:** [Current guidance](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/generative-page-external-tools)
  labels connector and custom-API data paths as preview. Their status is now
  distinguished from page creation itself.
- **MCP and computer use:** The [MCP connection guide](https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent),
  [computer-use configuration](https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use),
  and [administrator controls](https://learn.microsoft.com/en-us/microsoft-copilot-studio/administer-computer-use)
  anchor concrete transport, credential, reviewer-access, and disable boundaries.
- **Testing and governance:** [Native agent evaluations](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-intro)
  have cloud and target limitations. The previous governance citation pointed at a
  testing page; it is now paired with the actual [security and governance overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance).

## Access and verification limits

The live health check covered **73 registered AB-100 source URLs**: **68 returned
healthy HTTP/metadata responses, five were blocked, and none were missing or errored**.
The updated guide cites 67 distinct external URLs. HTTP success is weaker than
readable evidence: the Whizlabs listing, partner training page, practice-assessment
application, and YouTube page did not expose enough content for a new syllabus or
runtime verification. Two additional YouTube channel references in the registered
catalog also returned minimal shells.

The five blocked requests were the OpenAI supplementary guide, two O'Reilly
resources, and two Udemy resources. These were not used to establish new Microsoft
behavior. Commercial duration and question/lab counts are explicitly historical
observations, not newly verified recommendations. The O'Reilly crash-course and
MeasureUp public descriptions were readable; their marketing claims do not establish
exam coverage or readiness. Two Microsoft blog duration-signal differences appear
in the health report and were not treated as exam or product revisions.

All exercises were reviewed for design coherence, synthetic inputs, access needs,
and recovery boundaries. None was executed against a tenant. The ROI arithmetic
is a synthetic worked example, not vendor pricing or a business forecast. The
answer checkpoints are original explanations of this guide's own questions.

## Evidence and follow-through

`ADLC_Docs/operations/2026-09-27-ab-100-deep-review.json` records the guide hashes,
prior review record, blueprint hashes, 74 objective mappings, source-fetch metadata,
health observations, findings, and validation scope. Local source bodies and
candidate differences stay under the ignored
`.maintenance/ab-100-deep-review-2026-09-27/` directory; they are not published.

`data/source-freshness.json` retains the prerequisite conflict as blocked. Recheck
the English blueprint on October 14 before accepting its new baseline, confirm
ambiguous prerequisite eligibility through Microsoft, and execute the relevant
exercises in a disposable licensed environment before claiming hands-on validation.

## Blog discovery follow-up

A separate September 27 pass searched for useful implementation blogs after the
deep review above. Searches combined AB-100 with architecture, Copilot Studio,
evaluation, autonomous triggers, and ALM, then followed exact article links from
the Microsoft Copilot Studio CAT blog. Named practitioner leads and Microsoft
announcement posts were also considered. This was a bounded discovery pass, not
an exhaustive blog search or a renewed full objective audit.

The guide's **Selected implementation blogs** table adds five public articles:

| Accepted article | Author | Published | Updated | Objective fit |
|---|---|---|---|---|
| [MCP Servers or Connectors?](https://microsoft.github.io/mcscatblog/posts/compare-mcp-servers-pp-connectors/) | Jay Padimiti | 2026-02-13 | 2026-08-02 | Design: integration tradeoffs |
| [ALM: The Foundation](https://microsoft.github.io/mcscatblog/posts/alm-copilot-studio-agents-foundation/) | James Papadimitriou | 2026-06-03 | 2026-08-02 | Deploy: environments and promotion |
| [Quality Gates in Azure DevOps](https://microsoft.github.io/mcscatblog/posts/copilot-studio-eval-gate-azure-devops/) | Adi Leibowitz | 2026-04-19 | 2026-08-02 | Deploy: evaluation automation |
| [Copilot Credit Consumption](https://microsoft.github.io/mcscatblog/posts/copilot-credit-consumption-api/) | Petros Feleskouras | 2026-08-25 | 2026-08-26 | Plan/deploy: cost and monitoring |
| [Review Before Release](https://microsoft.github.io/mcscatblog/posts/agent-review-tool/) | Ramakrishnan Raman | 2026-08-18 | Not separately shown | Deploy: configuration review |

All five are Microsoft-hosted, named-author technical blog articles, registered
as Tier 5 expert resources because they are used for examples. Each links to
first-party evidence and adds a concrete reading artifact. The guide records
runtime, preview, authentication, and sample-support limits beside the resources.
Author attribution and source links are retained; each article displayed a
CC BY 4.0 notice. No code, illustrations, or substantial excerpts were copied.
No dumps, recalled questions, or guaranteed-pass claims were found in these
reviewed articles.

**Correction retained with the recommendation:** The evaluation post's statement
about Power Platform pipelines conflicts with Microsoft's newer
[test-and-deploy guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/kit-automate-test-deploy),
updated August 11. Part 8 now states the documented alternative explicitly.
The Agent Review article and current documentation describe different scoring
details; the guide recommends a review method without adopting either formula
or treating the blog's preview label as a current GA determination.

Other leads were not added:

- [Mariano Gomez's ALM account](https://www.theworkbench.blog/2026/08/copilot-studio-real-alm-for-agents-and.html)
  contains useful first-person recovery lessons and cites official documentation.
  Its author also identifies unsupported record shapes and a single-environment
  proof of concept. The accepted ALM post is a better introductory reading;
  this implementation was not reproduced or promoted as production guidance.
- [Ivy Fiecas-Borjal's ALM article](https://ifiecas.com/2026/04/25/alm-best-practices-for-copilot-studio-agents-and-why-its-different/)
  appeared in discovery but a later open returned 404. Full-content review was
  incomplete, so it was not added; this does not establish permanent removal.
- Broad launch announcements, existing cross-vendor references, and exam-oriented
  search results without additional implementation value did not justify more
  guide links. Suspected dump results were excluded from consideration.

Five blog URLs and six corroborating Microsoft documentation URLs were added to
the source catalog and fetched successfully with readable bodies. Their health
observations are registered, making them part of the existing weekly monitor.
The guide now cites **78 unique URLs: 73 reachable and five access-blocked**.
The earlier 67-link guide counts and 73-source live run above describe the deep
review before this follow-up. Original evidence hashes and the blocked
prerequisite finding remain unchanged. This pass does not reset the full
freshness baseline or establish hands-on validation. Local article bodies and
fetch metadata are under `.maintenance/ab-100-blogs-2026-09-27/` and are not
published. Acceptance metadata and observations are retained in the source
catalog, source-health baseline, and current AB-100 review record.

## Learning-content follow-up

The next September 27 pass turned the selected reading into original teaching
material inside the guide. A fictional service-case assistant connects five
worked examples: consumption per accepted outcome, connector/MCP selection,
evaluation completeness, configuration findings, and environment promotion.
Each example supplies a decision, failure case, and evidence to inspect. The
opening study route links directly to them.

Exercise 13 combines the examples into a paper-based workshop with calculations
and an answer guide. Five additional knowledge checks have answer checkpoints,
bringing the current guide to **13 exercises and 22 knowledge checks**. Earlier
counts in this report describe the earlier review phase. The examples, tool
names, records, numerical inputs, and predicted results are synthetic; no tenant
execution or vendor billing estimate is claimed.

The technical anchors were reread in current Microsoft documentation for ALM,
solutions, evaluation automation, connector policies, usage reporting, and Agent
Review Tool. Existing registered citations were reused. The guide still cites
78 unique external URLs, and the earlier source-health observations retain their
original timestamps. This teaching pass does not renew the full freshness
baseline or resolve the official prerequisite discrepancy.

The consumption calculations, incomplete-run percentages, question/answer
alignment, scenario permissions, and internal navigation were checked. An
implementation record with before/after guide hashes and validation results is
stored at `ADLC_Docs/operations/2026-09-27-ab-100-learning-content.json`.

## September 28 scheduled prerequisite recheck

The public [exam page](https://learn.microsoft.com/en-us/credentials/certifications/exams/ab-100/) still includes MB-280 and PL-200, and the [credential page](https://learn.microsoft.com/en-us/credentials/certifications/agentic-ai-business-solutions-architect/) still omits both. The existing guide caveat remains necessary. This bounded recheck leaves the blocker open and schedules another check for October 5; it does not reset the September 27 full-review date or establish prerequisite eligibility. Fetch timestamps, response hashes and the extracted lists are recorded in `ADLC_Docs/operations/2026-09-28-ab-100-prerequisite-followup.json`. No live lab or account-specific eligibility check was performed.
