# Microsoft refresh — first detailed batch, October 28, 2026

This continues the [initial monitoring and repair pass](2026-10-28-microsoft-refresh.md)
with complete-guide research for **AB-730, AB-900 and AI-200**. Three research agents
read all three guides, checked exam identity and current objectives, inspected selected
current product references, and evaluated specific learning resources. The coordinator
applied the shared changes. The [evidence ledger](../../ADLC_Docs/operations/2026-10-28-microsoft-wave1-deep-review.json)
records **121 detailed objective mappings**, source decisions, before/after bindings,
and review limits. This batch begins the detailed refresh; the other 52 Microsoft/MOS
guides are outside this batch, including the two archived Windows Server guides.

| Guide | Current English outline | Objectives | Research outcome |
|---|---|---:|---|
| [AB-730](../../guides/AB-730-ai-business-professional.md) | October 20, 2026 | 41 | Coverage reconciled; source gate blocked by documented product-source conflicts |
| [AB-900](../../guides/AB-900-microsoft-365-copilot-agent-administration-fundamentals.md) | October 14, 2026 | 53 | Sources/objectives checked; human and product execution pending |
| [AI-200](../../guides/AI-200-developing-ai-cloud-solutions-on-azure.md) | October 7, 2026 | 27 | Coverage reconciled; official weighting and Redis support conflicts remain blocked |

An accepted snapshot records the actual current official page. It does not resolve
contradictory statements on that page or prove a product works in a tenant. No new
full independent semantic-audit receipt, human review, course completion or live lab
execution is claimed. The separate final review and automated gate are recorded below
and in the ledger with their actual scope.

## AB-730

The four-domain October outline is now the guide's main objective map, rather than
a future supplement to July. Its weights are 25–30%, 20–25%, 20–25% and 20–25%.
Custom-agent construction remains useful related practice; it no longer stands in
for selecting and applying prebuilt agents, skills and supervised Cowork work.

Added a concrete multi-source renewal example, an agent-application example, context
engineering/model-effort guidance and a current-scope evidence worksheet. The guide
now has eleven proposed labs and 48 original answered checks. `Places to learn` is
the final public section. New exact Work IQ/prompt-foundation and Cowork modules have
explicit reading estimates and access limits; Pluralsight now lists three courses
totaling 4h26, still in production with older scope descriptions.

Current primary references establish several important boundaries:

- The dedicated federated-connector guide documents conditional write tools, while
  Researcher remains read-only. The general overview still says read-only; the
  discrepancy stays visible. Tool approval can persist beyond one invocation.
- Scheduled-prompt user help still names Optional connected experiences, while
  administrator guidance names Connected Experiences. Definitions, run history and
  runtime controls must be checked separately.
- Teams recap documents meeting memory in **Teams TAP preview**, subject to settings.
  It can support later answers without a saved transcript. Transcript deletion does
  not itself delete that separate generated artifact. The guide preserves the
  ordinary transcript-based route and the limited preview exception.
- Cowork model/access references disagree with the newer administration reference
  about Anthropic-control scope. No universal scope or fixed model inventory is
  asserted. Agent-history filtering still needs environment-specific verification.

These conflicts are bounded in the teaching but remain source-review blockers.
No sharing, action approval, message, meeting capture/deletion or schedule was run.

## AB-900

The October revision retains the three weights and 53 objectives, changing Enterprise
applications terminology. The refresh makes nine previously shallow treatments
explicit: organization/domain settings, SharePoint permission levels, authentication
choices, Identity Secure Score, audit-log selection, Compliance Manager improvement
actions, DLP alert triage, eDiscovery Content search and Copilot license assignment.

New examples distinguish app definitions from local service principals, including
the managed-identity exception; search from preservation; classification matches from
confirmed data loss; and entitlement from sign-in, agent and file permission. An
eighth tabletop/product worksheet and four more answers reinforce the distinctions.

The restricted-site example now limits its group-intersection model to the documented
internal-user case. External shared-channel participants are not evaluated against
resource-tenant restriction groups; channel/site permissions still govern them.
The BYO MCP preview statement now cites the dedicated support reference, retaining
its flow-specific client exclusions. Two exact three-module Learn paths replace a
vague learning link, and selected public course metadata is updated without implying
access to paid lessons or assessments.

The source gate passes for this bounded public-source review. Tenant execution,
license propagation, role/access tests, billing, eDiscovery and MCP remain unexecuted;
human review is pending. Product-specific preview and rollout limits remain explicit.

## AI-200

The current outline adds explicit October date/audience framing but retains the
27 detailed implementation tasks. Its summary assigns data services **30–35%**, while
the detailed domain heading still says **25–30%**. Both remain visible in the objective
map and teaching; no percentage is silently selected or averaged.

The Redis creation guide still prohibits post-creation clustering changes, while
the versioned update API permits a `NoCluster` exception. That does not allow adding
a missing RediSearch module after creation. The support discrepancy remains open;
the guide does not prescribe destructive conversion as its resolution.

Added replica/approximate-index reproducibility guidance for Cosmos DiskANN and a
current OpenTelemetry distribution note. Existing trace versus metric, authorization
versus recall, and replay/settlement boundaries remain. Runtime/protocol deadlines
that have passed are dated accordingly. There are ten proposed labs and 50 answered
checks; the earlier review's offline tests are historical, not new Azure execution.

Learning routes now name exact Cosmos, PostgreSQL and selected Redis paths, focused
Redis vector/cache references and an MIT-licensed PostgreSQL RAG repository. Time
budgets are marked editorial where a directly verified total is unavailable. Repository
reading does not establish deployed security, dependency compatibility or load results.
The earlier October 1 O'Reilly event listing is historical; delivery/recording access
is unverified. Updated public Udemy metadata does not evaluate paid content.

## Snapshot preservation and evidence boundaries

All three current English objective/status snapshots were fetched into an isolated
candidate directory and compared with the accepted versions. After objective mapping
and teaching repairs, current versions were accepted. Exact prior objective bytes are
stored in `data/objective-snapshots/archive/`, named with their original SHA-256.
Historical source-validation and AI-audit records migrate only their snapshot paths
to those archives. Their dates, hashes, outcomes, checks, link counts and findings
remain unchanged; older guide hashes remain historical. Archive files preserve exact
bytes across Git checkouts.

The sequential live check covered 158 initially cited sources; 152 were reachable,
six automation-blocked, and none missing/error. Twenty-one newly registered exact
sources and five reused sources newly cited by this batch were checked separately;
all 26 returned HTTP 200. These scopes overlap the final guide inventory and are not
a whole-library or all-55 result. The final guide inventory has **177 distinct sources:
171 reachable, six automation-blocked, none missing/error**. Per-guide counts are in
the ledger. Browser
access to selected commercial landing bodies does not erase automation blocks or
establish lesson/question access.

Technical research includes 71 opened source observations and rechecks of 41 older
findings. Large references were inspected in named sections; three references were
metadata-only and are labeled as such. Learning research evaluated 25 specific
resources and promoted ten learning/technical routes within the 21 new source total.
Neither search was exhaustive. Only public sources and original synthesis were used.

## Verification and continuation

A separate fresh-context reviewer read all three final guides and all 121 mappings,
verified their spans and hashes, checked source associations and historical preservation,
and independently opened 33 selected primary/learning sources. No new actionable finding
or material repair was required. The result is **pass with scope limitations** for
this bounded review; AB-730 and AI-200 source blockers remain. It is not a complete
independent semantic audit, human review or product execution.

All **193 tests**, repository validation and the shared learning-resource drift check
passed. A fresh post-acceptance official monitor reports all three snapshots unchanged,
with zero extraction errors or manual-review results. Final website checks use the
assembled report and evidence; execution outputs are retained with this wave's artifacts.

Three detailed research receipts are recorded: one reviewed and two reviewed with
blockers. **Fifty other active Microsoft/MOS guides remain eligible**; two retired
Windows Server guides remain archived. Continue with the
[Microsoft review queue](../MICROSOFT-REVIEW-STATUS.md) in small packets; future-dated
English outlines and localized exam scope remain separate. No commit, remote publication
or deployment result is included in this local batch's completion claim.
