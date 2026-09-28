# AZ-400 deep review — September 28, 2026

The [AZ-400 guide](../../guides/AZ-400-designing-implementing-microsoft-devops-solutions.md)
was read in full and mapped to **86 objectives in sixteen groups**. It now
contains seven worked examples, ten labs and 48 explained original checks.
**47 offline assertions passed:** 35 arithmetic/catalog checks and 12 in the
published Python release-decision example. The KQL example was reviewed and
corrected for sampling; it was not run against a workspace. No cloud pipeline,
identity change, deployment, security scan or paid-content execution occurred.
Independent human review remains pending.

## Scope and credential

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400)
retains the July 27, 2026 baseline. Objective and status hashes are unchanged;
no upcoming change is announced. The
[credential profile](https://learn.microsoft.com/en-us/credentials/certifications/devops-engineer/)
lists ten languages, renewal and Azure Administrator Associate or Azure
Developer Associate as certification prerequisites. The
[AZ-204 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-204)
confirms its July 31 retirement. No automatic substitution of a new developer
credential is inferred; AZ-104 remains the active administrator route.
Exact AZ-400 exam duration was not verified.

The standalone [Microsoft Learn course](https://learn.microsoft.com/en-us/training/courses/az-400t00)
lists four instructor days and eight languages. Its existence takes precedence
over the profile's empty training placeholder. The free Practice Assessment
was checked only at the public landing page; no actual questions or results
were accessed.

## Applied changes

| Area | Evidence and resulting lesson |
|---|---|
| Source and integration | A [merge queue](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue) requires checks on its merge-group commit. [Azure DevOps public projects](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/public-projects-retirement?view=azure-devops) convert in 2027, affecting anonymous links and feed consumers; exact dates come through product banners. |
| Teams communication | Use the latest [connector retirement update](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/) and distinguish legacy connectors from native apps/Workflows. MessageCard action buttons need a different payload/response design. |
| Packages and provenance | [Feed/view access](https://learn.microsoft.com/en-us/azure/devops/artifacts/feeds/feed-permissions?view=azure-devops) must be reviewed separately. [Promotion](https://learn.microsoft.com/en-us/azure/devops/artifacts/feeds/views?view=azure-devops) does not support demotion. [Attestations](https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations) must be verified for the artifact consumed; their existence does not prove application correctness. |
| Workflow trust | Apply [secure-use guidance](https://docs.github.com/en/actions/reference/security/secure-use) to privileged events, untrusted code/artifacts, full-SHA pins and script input. [Execution policies](https://docs.github.com/en/actions/how-tos/administer/control-workflow-execution) and [cache modes](https://github.blog/changelog/2026-09-10-control-github-actions-cache-access-with-cache-mode/) add independent controls, with plan and caller/callee boundaries. |
| YAML and resource gates | [Conditions](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/conditions?view=azure-devops) replace default success behavior; [variable evaluation](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops) depends on stage of execution. [Checks](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/approvals?view=azure-devops) remain resource-owner controls; pending approvers and lock behavior need deliberate handling. |
| IaC | [Bicep what-if](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/deploy-what-if) validation levels differ and unresolved resources/modules may be excluded. Read diagnostics rather than treating an empty diff as complete validation. |
| Identity | The [new DevOps connection](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/add-devops-entra-service-connection?view=azure-devops) targets DevOps resources. [Application identities](https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/service-principal-managed-identity?view=azure-devops) need organization membership, licensed access and DevOps permissions; Entra permissions alone are insufficient. |
| Code scanning | [Current CodeQL setup guidance](https://learn.microsoft.com/en-us/azure/devops/repos/security/github-advanced-security-code-scanning?view=azure-devops), together with [sprint 276 GA](https://learn.microsoft.com/en-us/azure/devops/release-notes/2026/sprint-276-update), distinguishes default-branch/no-custom-build setup from advanced setup. Do not apply historical April preview-delay wording to current availability. |
| Observability | [Classic sampling](https://learn.microsoft.com/en-us/azure/azure-monitor/app/sampling-classic-api) requires weights for estimated totals. [OpenTelemetry sampling](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-sampling) differs by language/version; appropriate unsampled metrics support release decisions. The retained-row percentile is explicitly labeled. |

## Current release and lifecycle boundaries

- [Node 20 removal](https://github.blog/changelog/2026-09-23-node-20-is-no-longer-available-in-github-actions/),
  September 23: JavaScript actions use Node 24 and the temporary insecure
  opt-out has ended on github.com and GitHub with Data Residency. Application
  runtime selection is a separate concern.
- [Actions retention expansion](https://github.blog/changelog/2026-08-27-actions-retention-will-cover-checks-workflow-runs-and-statuses/),
  October 1: checks, run and status records follow configured retention.
  Archive evidence before expiry. [Azure Pipelines retention](https://learn.microsoft.com/en-us/azure/devops/pipelines/policies/retention?view=azure-devops)
  has its own project/build, classic-release and test boundaries.
- [Workflow execution protection GA](https://github.blog/changelog/2026-09-17-workflow-execution-protections-in-github-actions-generally-available/)
  schedules November 2 enforcement of the default `pull_request_target` block
  for affected public repositories. Private/internal repositories are outside
  that default rollout; the product documentation controls plan availability.
- [Reusable workflow job context](https://github.blog/changelog/2026-09-03-github-actions-early-september-2026-updates/)
  distinguishes the workflow defining the job from its caller. The new job
  properties are not available on GitHub Enterprise Server.
- [Azure DevOps issuer retirement](https://devblogs.microsoft.com/devops/retirement-of-azure-devops-issuer-in-workload-identity-federation-service-connections/)
  on July 1, 2027 has explicit public-cloud/single-tenant/managed-identity scope.
  Do not invent the same deadline for excluded clouds or multi-tenant apps.
  Azure Automation State Configuration's September 30, 2027 retirement remains
  documented separately from the issuer change.

Follow-up events now cover October 1 retention, October 12 capabilities/catalogs,
October 19 preparation for the November policy rollout, December 1 public-project
timing and June 1, 2027 issuer migration readiness. They queue reviews; no
organization policies or infrastructure are changed by those reminders.

## Blog intake and critique

| Article | Reading boundary | Adopted exercise |
|---|---|---|
| [PAT-free service connection](https://devblogs.microsoft.com/devops/you-can-now-use-the-azure-devops-service-connection-instead-of-a-pat-or-build-session-token/) — Eric van Wijk, August 6, 2026 | Introduction/prerequisites, tenant boundary and selected repository/feed/REST/CLI examples; later complete script not audited | Map all identity, membership, access-level, permission and connection controls. Preserve the preview-labeled launch/rollout boundary. |
| [Issuer retirement](https://devblogs.microsoft.com/devops/retirement-of-azure-devops-issuer-in-workload-identity-federation-service-connections/) — Eric van Wijk, June 22, 2026 | Main announcement, scope, timeline, conversion and FAQ; linked scripts not executed | Identify affected connections, validate new trust and preserve pipeline references during conversion. |
| [Dev-to-prod promotion](https://devblogs.microsoft.com/devops/azure-developer-cli-from-dev-to-prod-with-azure-devops-pipelines/) — PuiChee and Kristen, August 13, 2025 | Introduction/artifact rationale and selected stage/package/deployment/validation snippets; linked repository not audited | Preserve the same package across stages, then replace the TODO/sleep validation placeholder with actual gates, protected deployment resources and rollback evidence. |

The last article is useful precisely because its demonstration needs review.
A task that waits and prints success supplies no health, security or correctness
evidence. The guide does not reproduce its full pipeline or label it ready for
production. The local gate exercise rejects bad/missing/stale/wrong-version
observations, but still assumes an authenticated and correctly aggregated
telemetry source supplied by the real delivery system.

## Catalog corrections

- [Pluralsight](https://www.pluralsight.com/paths/az-400-designing-and-implementing-microsoft-devops-solutions):
  six courses and three labs total **35h 36m**, matching a rounded 36-hour header.
  That includes a 15h 22m legacy 2023 course overlapping five 2024–2025 domain
  courses. The five domain courses plus three April 2026 labs total **20h 14m**.
  The guide helps learners avoid duplicating the entire legacy course.
- [O'Reilly/Tim Warner](https://www.oreilly.com/live-events/exam-az-400-microsoft-azure-devops-solutions-crash-course/0636920382614/):
  public two-day agenda totals six hours including breaks. The page contains
  AZ-500/Security Engineer and obsolete exam-name errors. Current booking date
  and paid delivery were not verified; it is an older catalog option, not
  evidence of correct current prerequisite guidance.
- [Udemy/Alan Rodrigues](https://www.udemy.com/course/azure100/): direct retrieval
  blocked; browser provider metadata confirms September 2025, ten sections,
  258 lectures and 20h 46m. Paid content remains unaudited.
- [MeasureUp](https://www.measureup.com/microsoft-practice-test-az-400-designing-and-implementing-microsoft-devops-solutions.html):
  139 questions and August 2024 update remain unchanged. The current objective
  baseline is newer; no paid question/coverage validation is claimed.
- [Reactor](https://developer.microsoft.com/en-us/reactor/series/s-1625/):
  **twelve distinct one-hour sessions**, January 27–April 21, 2026, replacing
  the old six-session estimate. The HTML duplicates its event list; 24 rendered
  rows were deduplicated. Scheduled time is not a verified recording runtime.
- Whizlabs and Savill returned shells; specific bundle and playlist-runtime
  claims are qualified. The Readiness Zone series introduction was accessible,
  but its selected AZ-400 episode runtimes were not verified. The Azure DevOps
  Labs landing index was partly read; no hosted lab was executed.

## Validation and limits

The exercises cover pipeline critical paths, runner utilization, canary cohorts,
flaky-test retries, evidence intersections, sampling and error-budget burn.
The Python example validates only a local decision predicate; it does not
authenticate telemetry, attest packages, run a deployment or establish
statistical significance. All numerical inputs are fictional.

Repository validation, reviewed-resource consistency, all 174 unit tests,
strict site build, generated-site validation and whitespace checks passed.
The receipt at `ADLC_Docs/operations/2026-09-28-az-400-deep-review.json` preserves
the previous review, unchanged blueprint hashes, all 86 objective mappings,
source read boundaries, catalog evidence and local validation.

Retained references were fetched; long documents, full licensing matrices,
every linked script and all provider lessons were not exhaustively audited.
This is a same-context source/content review. The
[Microsoft review tracker](../MICROSOFT-REVIEW-STATUS.md) distinguishes completed
review work, unresolved blockers and guides still awaiting deep review.
