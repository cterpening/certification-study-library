# AB-650 deep review — September 28, 2026

The [AB-650 guide](../../guides/AB-650-ai-services-administrator-associate.md) was read
in full and mapped to all **58 detailed objectives across ten groups**. Six synthetic
worked examples, two additional labs (eleven total), 48 answered checks and a useful
Agent 365 blog exercise now develop administrative decisions and their evidence.

This is same-context AI research and repair. Twelve offline arithmetic, set and
policy-selection assertions passed. No tenant, mailbox, agent, billing policy,
provider opt-in, tool registration, network probe or restore was executed. Paid
question banks were not accessed. Independent human review remains pending.
The guide remains **review-required** because second-year Backup restore frequency
is not resolved by current official documentation.

## Exam and resource baseline

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-650)
retains the July 27, 2026 page date, with no separate skills-effective date or
announced replacement objective set. Both objective and status hashes are unchanged;
accepted snapshots were preserved. The [credential](https://learn.microsoft.com/en-us/credentials/certifications/ai-services-administrator-associate/)
and [exam page](https://learn.microsoft.com/en-us/credentials/certifications/exams/ab-650/)
still describe beta, English-only availability and no Practice Assessment. The exam
page exposes no current instructor-led course. No fixed duration or GA date was verified.

Three Learn paths expose **17 modules: 5 + 5 + 7**. Their former combined duration
of 23 hours 8 minutes is now marked historical because the fetched current pages
do not expose duration totals. The 35–55-hour study budget is an editorial estimate,
not a provider runtime. Videos, channel catalogs, repositories and signed-in partner
events were not treated as completed coursework.

Targeted searches found exact Udemy listings from
[Dean Ellerby](https://www.udemy.com/course/ab-650-practice-tests-administering-m365-ai-services/)
and [Hamdy Khaled](https://www.udemy.com/course/ab-650-practice-exams-300-qs-official-sources/).
Their public search descriptions advertise six tests/360 questions and five tests/300
questions respectively, August updates and documentation-linked explanations.
Both direct requests were access-blocked. These are catalog leads; content quality,
originality, current coverage, runtime and seller certification claims are unverified.
No exact current Pluralsight, O'Reilly, Whizlabs or MeasureUp offering was verified
in the bounded search; this is not evidence that none exists.

## Objective coverage

Every detailed bullet has a hashed mapping in the operation record.

| Group | Objectives | Reviewed teaching and additions |
|---|---:|---|
| Tenant configuration | 8 | Domains, profile, licensing, Backup setup/scope/recovery, network insights and health notifications |
| Workloads | 5 | Shared mailboxes, channel membership, Copilot meeting policy, SharePoint access/discovery |
| Entra identities | 7 | Users, guests, groups, PIM, administrative units, contacts and scoped bulk operations |
| Authentication/access | 5 | Methods, password protection, SSPR, troubleshooting and risk-policy migration |
| Defender | 4 | Threat policies, alert investigation, response and authorized simulations |
| Purview | 5 | DLP, classification/labels, retention, alerts and DSPM |
| Copilot | 9 | Readiness, oversharing, web/search/app controls, Cowork, AI providers and connectors |
| Agents | 8 | Identity lifecycle, access, ownership, settings, registry, requests, deployment and tools |
| Agent governance | 3 | Activity, sensitive content and protection-gap assessment |
| AI monitoring | 4 | Spending scopes, workload adoption, measurement and service health |

## Material updates

- **Recovery and operations:** distinguish full and granular restore points and
  permission outcomes; static versus dynamic scope; unsupported mailbox types;
  preview Full Workload Backup; and shortening-window deletion. Connect network
  location evidence to health notifications without inferring user entitlement.
- **Collaboration:** clarify shared-mailbox sign-in/licensing, shared-channel
  identity and residual file permissions, and meeting defaults versus enforced
  transcript requirements. Temporary audio processing does not imply no retained
  compliance evidence.
- **Identity:** preserve separate human-risk policies and the October 1 migration
  deadline. Distinguish delegated, agent-identity, agent-user and API-key access.
- **Cowork:** spending-policy scope grants access. Discovery, provider availability
  and asynchronous credit limits are separate controls. Policy precedence and
  carried consumption have their own worked example.
- **Agent administration:** correct broad-sharing assumptions, custom ZIP upload
  stages, publisher-specific block effects, owner management and firewall failure
  diagnostics. Explain the separate one-time template action for existing instances.
- **Protection:** explicit sharing and encrypted-file rights, generated-label limits,
  and narrower DLP interaction support complement broader audit visibility. Six
  examples require learners to calculate or reconcile evidence, not memorize a portal.
- **Tool support:** BYO MCP remains preview with named supported clients; republishing
  and deletion limitations affect the lifecycle exercise. Registration, approval,
  permission consent and successful invocation are separate evidence points.

The [September Copilot release notes](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes)
were reviewed for the latest September 23 entry, including license requests and
gradual rollout; the full historical release archive was not audited.
The [May Agent 365 announcement](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/)
supports product-level GA while individual integrations retain their own status.
Current product procedures determine the guide's implementation details.

## Blog intake

Alex Fleck's August 6, 2026 InsideTrack article,
[Implementing Agent 365: How we're governing and managing AI agents at Microsoft](https://www.microsoft.com/insidetrack/blog/implementing-agent-365-how-were-governing-and-managing-ai-agents-at-microsoft/),
was accepted for a bounded operations worksheet. Its public main article was read;
linked videos, internal systems and performance claims were not reproduced.

The exercise turns an inventory into explicit identity keys, owner/sponsor roles,
cross-team handoffs and dated actions. The original numerical example reconciles
duplicate rows, missing platform IDs and active-agent telemetry. Microsoft’s internal
scale figures are not used as a promised outcome. The article's historical Cowork
Frontier description is qualified by current work/school GA guidance.

## Contradictions and open evidence

1. **Backup frequency — open:** the [policy procedure](https://learn.microsoft.com/en-us/microsoft-365/backup/backup-view-edit-policies?view=o365-worldwide)
   and [September update](https://learn.microsoft.com/en-us/microsoft-365/backup/backup-whats-new?view=o365-worldwide)
   allow two-year recovery windows, but the [restore table](https://learn.microsoft.com/en-us/microsoft-365/backup/backup-restore-data?view=o365-worldwide)
   stops at 365 days and the overview describes 52 weeks. No second-year cadence is
   inferred. This is the same unresolved source gap already recorded for MS-102.
2. **Templates — reconciled by operation and date:** the July
   [template FAQ](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/policy-template)
   excludes already approved agents. September's [agent settings](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-settings?view=o365-worldwide)
   explicitly adds a one-time bulk action for existing identity-backed instances,
   excluding blueprints and AI teammates. Ordinary editing remains nonretroactive.
3. **Provider scope — reconciled by newer dedicated procedure:** the September 8
   [Cowork access page](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-access)
   says model settings are tenant-wide only. September 14
   [Cowork administration](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance)
   and September 18 [provider settings](https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor)
   explicitly support user/group scope. The guide uses the newer dedicated provider
   procedure and still separates provider availability from Cowork access.
4. **Granular restore — reconciled by current procedure:** the overview's
   coming-soon file-version wording is not used to deny the granular file/folder
   restore flow confirmed in the current restore procedure and September GA notice.

Follow-ups cover the October 1 risk-policy retirement, October 5 Backup frequency
gap, October 12 Cowork/template/tool documentation and October 15 beta/catalog status.
These events preserve unresolved evidence without continually displacing first reviews.

## Verification boundary

The twelve offline assertions check supplied recovery clocks, spending-policy
selection and carried consumption, template eligibility/backlog, simplified encrypted
file permission gates, inventory intersections, telemetry/adoption denominators,
synthetic cost per validated outcome and module/historical-runtime arithmetic.
They are not tenant integration tests or proof of product enforcement.

The operation ledger is
`ADLC_Docs/operations/2026-09-28-ab-650-deep-review.json`. It records fetch timestamps,
hashes, link health, the original source-validation record, objective mapping,
findings, blog limits and local validation results. The shared learning catalog and
Microsoft review tracker are updated from the completed guide and receipt.
