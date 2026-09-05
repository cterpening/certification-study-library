# Repository Health & Developer Experience Report — Certification Study Library

## Assessment identity

| Field | Value |
|---|---|
| Generated at (UTC) | 2026-09-05T18:14:35Z |
| Repository / commit | `certification-study-library` / `8c1ceaf01279ebc51058d77f91369bf6f24193f1` |
| Report mode | `snapshot` |
| Mode selection | Explicitly selected by the user |
| Assessment profile | `standard` — security, quality, governance, and operations |
| Adoption mode | `reference-only` |
| Collection status | `partial` |
| Repository facts | `ADLC_Docs/discovery/repository-facts.json` · contract `1.1.0` · SHA-256 `0589dff0039b2abaf5130b3c5a3c8d488653a57fcf8cb1c2f2e8a871964d3c40` |
| Finding set | `ADLC_Docs/findings/2026-09-05-repository-health.json` · contract `1.0.0` · SHA-256 `40d4db6e2eacd8c2215cbc27bedab74de9e6c27ccd93ee95c8587067da7b9ae4` |

## Decision summary

- Overall categorical rating: **at-risk**; Snapshot does not calculate an aggregate or numeric score.
- Overall confidence: **medium**. Local evidence is current and internally consistent, but remote GitHub governance, CI history, and deployed state were unavailable.
- Findings: **5 open** — 1 high, 3 medium, and 1 low.
- Highest-friction areas: content-assurance coverage, source-health data integrity, automation concentration, and duplicated CI maintenance.
- Most material evidence gap: remote branch protection, review requirements, workflow history, and repository settings were not assessed.
- Recommended next step: stop for findings review. Request a separately authorized remote-evidence pass only if GitHub governance or CI reliability must inform the decision.

The repository has strong structural foundations: 84 unit tests passed, the repository validator passed, the existing generated-site validator passed, dependencies are exactly pinned, maintenance workflows are defined, and the architecture and content-governance documentation is unusually explicit. The material concern is scale: independent AI audit covers 39 of 222 guides, freshness review covers 33, 10 audit findings remain open, and 61 discovered sources await review. A separate data-integrity defect allows duplicate source-health IDs to pass the main validator.

## Scope and budget

| Budget dimension | Approved plan | Actual use | Status / variance |
|---|---|---|---|
| Elapsed time | Snapshot target 10 minutes; ceiling 20 minutes | Evidence collection timestamps span 1 minute 33 seconds; end-to-end contract loading and rendering were not journaled | Collection within target; total not reliably measured |
| Primary repositories | 1 | 1 target repository | Within scope |
| Context repositories | Read-only accelerator context | 1 accelerator repository, reference-only | Within scope |
| Network | None | No web, provider API, connector, plugin, remote SCM, or scanner request | Within scope |
| Automated assessment runs | Ceiling 8 | 6 succeeded; one remote check recorded blocked and one strict build recorded skipped without execution | Within ceiling |
| External requests | 0 | 0 tool/provider requests; the active Codex inference boundary is recorded separately as egress | Within scope |

### Access and capabilities

| Capability / source | Required or optional | Approved | Available | Used | Notes |
|---|---|---:|---:|---:|---|
| Target local files | Required | Yes | Yes | Yes | Read-only except the four authorized assessment destinations |
| Local Git history | Required | Yes | Yes | Yes | Current branch, full HEAD, tags, and bounded history metadata |
| Existing non-mutating repository checks | Required | Yes | Yes | Yes | Unit tests and two existing validators |
| Accelerator files | Required context | Read-only | Yes | Yes | Prompt, contracts, validators, template, and persona generator referenced in place |
| Remote GitHub API/settings | Optional for partial Snapshot | No | Not assessed | No | Network and authentication explicitly prohibited |
| CI run history and artifacts | Optional for partial Snapshot | No | Not assessed | No | Local definitions only |
| Package installation or external scanners | Optional | No | Not used | No | Prohibited by user boundary |
| Target source/configuration changes | Not authorized | No | N/A | No | Only assessment outputs were written |

### Approved overrides

| Budget or boundary | Original | Approved change | Approver / reason |
|---|---|---|---|
| None | — | — | — |

## Data handling and egress

| Field | Decision / actual result |
|---|---|
| Handling mode | `approved-external` for the active Codex API inference boundary; generated artifacts remain local |
| Approved execution boundary | Target workspace plus the active OpenAI Codex API session invoked by the user for this assessment |
| Highest classification | Unknown; no repository data classification was supplied |
| Unknown-data action | No further external transfer; artifacts remain local drafts pending human review |
| Allowed assistants/tools/destinations | Active Codex session; local PowerShell, Git, ripgrep, Python, and accelerator validation/rendering scripts |
| External transfer permitted | Limited to the active Codex session by the user's explicit assessment request; service-region, retention/deletion, and approval-expiry details were unavailable locally |
| Redactions/exclusions | Absolute workstation paths, configured remote URL, author identities, commit-message contents, raw source URLs/excerpts, and token-match context were excluded from portable artifacts |
| Actual external egress | Selected repository metadata and file content were processed by the active OpenAI Codex API session. No connector, web request, remote SCM call, plugin, external scanner, or other destination was used. |

### Artifact retention and review

| Artifact class | Approved location | Owner | Period / governing policy | Expiry action | Review status / reviewer |
|---|---|---|---|---|---|
| Raw evidence | Existing target files and local Git history | Repository owner | Existing repository policy; no new raw-evidence copy created | Govern in place | Bounded automated review complete |
| Repository facts | `ADLC_Docs/discovery/repository-facts.json` | Assessment owner | Not supplied | Review and renew, archive, or delete before broader use | Schema and semantic validation passed; human review pending |
| Working report | `ADLC_Docs/quality/2026-09-05-repository-health.md` | Assessment owner | Not supplied | Review and renew or delete | Local draft; human review pending |
| Final report | No separate external deliverable created | Assessment owner | Not supplied | Do not distribute until approved | Not approved for egress |
| Tool logs/prompts | Active Codex session and local command session | User / service owner | Service policy not visible in local evidence | Apply account/service retention policy | Governance metadata incomplete |

## Evidence coverage

| Domain | Status | Facts assessed | Source classes | Freshness | Confidence | Missing or blocked evidence |
|---|---|---:|---|---|---|---|
| Stack | Complete | 5 | Repository files, inventory | Current | High | None for Snapshot stack identification |
| Build and test | Partial | 7 | Workflows, command output, README | Current | High | Current strict site-build result; repeated-run flakiness evidence |
| Dependencies | Partial | 5 | Manifest, update configuration, inventory | Current | High for declarations | Lockfile, pip update automation, SBOM, vulnerability and support-lifecycle evidence |
| CI | Partial | 7 | Local workflow definitions, blocked SCM source | Mixed | Medium | Enablement, required checks, run history/conclusions, remote artifacts |
| Ownership | Partial | 3 | Maintainer files, issue forms, blocked SCM source | Current | Medium | CODEOWNERS, path owners, remote owner-review enforcement |
| Branch model | Partial | 5 | Local Git history, blocked SCM source | Mixed | Medium | Remote default branch, protection, and review requirements |
| Release signals | Partial | 5 | Git tags, changelog, deployment definition, blocked SCM source | Mixed | Medium | Published releases, deployment history, promotion controls |
| Architecture artifacts | Partial | 3 | Architecture/runbook documents, inventory | Current | High | Formal ADR set and current system diagram |

## Operational change snapshot

| Field | Value |
|---|---|
| Correlation artifact / contract | Not assessed |
| Notice source / snapshot | Not assessed |
| Source retrieved / freshness | Not assessed |
| Notice / component coverage | No approved local normalized notice input existed |
| Candidate gate | No operational-change candidates generated |

No vendor notice collection or search was performed as a fallback.

## Repository facts

Only observed facts from the validated manifest are projected below. Inferred, unknown, and blocked items remain in the concern and limitation sections.

### Stack and dependencies

| Fact ID | State | Predicate / value | Confidence | Evidence / source IDs | Source as-of UTC | Freshness |
|---|---|---|---|---|---|---|
| `stack.language.python` | observed | Automation uses Python; 8 scripts and 8 test files | High | `source.inventory` | 2026-09-05T12:50:07Z | Current |
| `stack.language.content` | observed | Markdown/JSON/YAML with small JavaScript/CSS assets; 222 guides | High | `source.inventory` | 2026-09-05T12:50:07Z | Current |
| `stack.runtime.python` | observed | CI definitions select Python 3.13 | High | `source.workflow-validation` | 2026-08-31T12:12:35Z | Current |
| `stack.framework.mkdocs-material` | observed | MkDocs Material 9.7.7 | High | `source.requirements` | 2026-09-05T11:44:35Z | Current |
| `dependency.direct.site` | observed | `jsonschema` 4.26.0, `mkdocs` 1.6.1, `mkdocs-material` 9.7.7; all exact pins | High | `source.requirements` | 2026-09-05T11:44:35Z | Current |
| `dependency.update-automation.local` | observed | Dependabot is configured for GitHub Actions only | High | `source.dependabot` | 2026-08-31T10:27:25Z | Current |

### Build and test

| Fact ID | State | Predicate / value | Confidence | Evidence / source IDs | Source as-of UTC | Freshness |
|---|---|---|---|---|---|---|
| `build.command.strict-site` | observed | Strict MkDocs build command is defined | High | `source.workflow-validation` | 2026-08-31T12:12:35Z | Current |
| `test.result.unit` | observed | 84 unit tests passed | High | `source.unit-tests` | Unknown; captured 2026-09-05T18:13:02Z | Current |
| `test.result.repository-validator` | observed | Repository validator passed | High | `source.repository-validator` | Unknown; captured 2026-09-05T18:13:02Z | Current |
| `test.result.generated-site-validator` | observed | Existing generated-site validation passed; strict build was not rerun | Medium | `source.site-validator` | Unknown; captured 2026-09-05T18:13:02Z | Current |

### Delivery, ownership, and releases

| Fact ID | State | Predicate / value | Confidence | Evidence / source IDs | Source as-of UTC | Freshness |
|---|---|---|---|---|---|---|
| `ci.definitions.local` | observed | Four GitHub Actions workflow definitions exist | High | `source.workflow-*` | 2026-08-31 through 2026-08-31 | Current |
| `ci.jobs.validation` | observed | Validation and Pages definitions repeat the same four-step verification suite | High | `source.workflow-validation`, `source.workflow-pages` | 2026-08-31T12:12:35Z | Current |
| `ci.artifact.source-health` | observed | Source-health artifact upload is configured | High | `source.workflow-source-health` | 2026-08-31T16:00:22Z | Current |
| `ownership.maintainer-sources` | observed | Contribution, security, and five structured issue-form sources exist | High | `source.maintainer-docs`, `source.inventory` | 2026-09-02T19:33:06Z | Current |
| `branch.current.local` | observed | Current local branch is `main` at the assessed commit | High | `source.git-head` | 2026-09-05T12:50:07Z | Current |
| `release.tags.local` | observed | Local tags `v0.1.0` and `v0.1.1` exist | High | `source.git-history` | 2026-09-05T12:50:07Z | Current |
| `release.deployment-definition.pages` | observed | A GitHub Pages deployment definition exists | High | `source.workflow-pages` | 2026-08-31T16:00:22Z | Current |

### Architecture artifacts

| Fact ID | State | Predicate / value | Confidence | Evidence / source IDs | Source as-of UTC | Freshness |
|---|---|---|---|---|---|---|
| `architecture.system-model.local` | observed | `docs/ARCHITECTURE.md` documents content, data, automation, and site boundaries | High | `source.architecture` | 2026-09-05T02:04:58Z | Current |
| `architecture.data-model.catalogs` | observed | 222 guides, 222 review records, 3,248 sources, 39 audit results, 33 freshness results, 61 queued candidates | High | `source.inventory`, `source.reviews`, `source.sources`, `source.ai-audits`, `source.source-freshness`, `source.source-candidates` | 2026-09-05T12:50:07Z | Current |
| `architecture.runbook.automation` | observed | `docs/AUTOMATION.md` documents maintenance workflows and boundaries | High | `source.automation-doc` | Unknown; captured 2026-09-05T18:13:02Z | Current |

## Dimension assessment

| Dimension | Rating / N/A | Confidence | Supporting fact/evidence IDs | Rationale | Missing evidence |
|---|---|---|---|---|---|
| Setup time | Healthy | High | `source.readme`, `source.requirements` | Setup and validation commands are discoverable; direct dependencies are exact pins | Clean-machine timing was not run |
| Local reproducibility | Watch | High | `test.result.unit`, `test.result.repository-validator`, `test.result.generated-site-validator` | Existing local checks pass, but the strict site build was not rerun and there is no lockfile | Fresh strict build and clean-environment evidence |
| Dev-container support | N/A | Medium | `source.inventory` | No dev container was found; the repository is a small Python-backed content/static-site toolchain | Confirm whether maintainers want a containerized contributor path |
| Build duration | Watch | Medium | `source.unit-tests`, `source.repository-validator`, `source.site-validator` | Observed local checks complete quickly, but current full-build and CI timings are unavailable | Strict build and CI duration history |
| Flaky tests | Not assessed | Not assessed | `source.scm-blocked` | One passing local execution cannot establish repeatability | Repeated runs or CI history |
| Ownership clarity | Watch | Medium | `ownership.maintainer-sources`, `ownership.codeowners.local` | Intake guidance is strong, but no local path ownership map was found | CODEOWNERS or equivalent and remote enforcement |
| Issue / PR hygiene | Watch | Low | `source.inventory`, `source.scm-blocked` | Five structured issue forms exist; no PR template was found and remote PR practice was unavailable | PR history, template/rulesets, review-time signals |
| Documentation findability | Watch | High | `source.architecture`, `source.automation-doc`, `source.adapter-doc` | Core docs are strong, but the adapter inventory has drifted from 9 documented to 26 routed keys | Documentation/registry reconciliation |
| Automation friction | At-risk | High | `ci.jobs.validation`, `dependency.update-automation.local` | Verification is duplicated across workflows and Python dependency updates are not configured | Remote run-cost and failure history |
| Cognitive load | At-risk | High | `source.validator-script`, `source.monitor-script`, `source.adapter-doc` | Two roughly 2,000-line modules centralize validation and provider routing; documentation already trails implementation | Maintainer qualitative feedback and change-failure history |
| Security posture | Watch | Medium | `source.secret-heuristic`, `source.requirements`, `source.scm-blocked` | No common secret signatures were detected and versions are pinned, but no external scan or remote security-setting evidence was authorized | Vulnerability, code-scanning, secrets-scanning, and repository-setting evidence |
| Content assurance | At-risk | High | `architecture.data-model.catalogs`, `source.ai-audits`, `source.source-freshness` | Independent assurance covers a minority of guides and 10 audit findings remain open | Completion of risk-ranked audit/freshness waves and human-review sample |
| Source-health integrity | At-risk | High | `source.source-health`, `source.validator-script` | Seven excess rows across six duplicate IDs are silently collapsed by the passing validator | Corrected ledger and duplicate-ID regression test |

## Inferred concerns

| Concern ID / inference | Reasoning | Confidence | Supporting fact/evidence IDs | Oldest source as-of UTC / freshness | Limitations / contrary evidence | Confirmation needed |
|---|---|---|---|---|---|---|
| `CON-01` — Library-wide semantic and freshness assurance is incomplete | 39 AI-audited and 33 freshness-scanned guides cannot support a library-wide assurance claim across 222 guides, especially with 10 open findings | High | `architecture.data-model.catalogs`, `source.ai-audits`, `source.source-freshness`, `source.source-candidates` | 2026-09-05 / current | All 222 guides have review records; 220 are marked source-validated; automated checks pass | Define acceptable independent and human-review coverage thresholds |
| `CON-02` — Source-health aggregates can be distorted | Duplicate ID rows increase row totals, while dictionary construction discards duplicates before coverage validation | High | `source.source-health`, `source.validator-script`, `test.result.repository-validator` | 2026-09-05 / current | Duplicate rows share matching content except timestamps; unique-ID latest statuses still reconcile to the source catalog | Decide snapshot-versus-history semantics and rerun after deduplication |
| `CON-03` — Provider growth is increasing change and review load | Provider routing and validation live in large modules, while adapter documentation covers only part of the registry | High | `source.monitor-script`, `source.validator-script`, `source.adapter-doc` | 2026-09-02 / current | The unit and repository checks pass, so this is maintainability exposure rather than demonstrated runtime failure | Review recent provider-change defects or maintainer feedback |
| `CON-04` — CI definitions may drift and dependency maintenance is incomplete | Two workflows duplicate verification; action refs are mutable major tags; update automation excludes pip | High | `ci.jobs.validation`, `dependency.update-automation.local`, `source.workflow-validation`, `source.workflow-pages` | 2026-08-31 / current | Exact Python pins improve repeatability; remote workflow health and enforcement are unknown | Inspect remote settings/history in a separately approved pass |
| `CON-05` — Accessibility readiness is not evidenced | Nine manual checks remain unchecked and local CI does not record equivalent interaction testing | High | `source.accessibility`, `source.workflow-validation` | 2026-09-01 / current | Unchecked boxes do not prove accessibility failures; testing may have occurred without being recorded | Execute and retain the documented test matrix |

## Prioritized recommendations

Every recommendation is proposed only; this assessment does not authorize backlog creation or implementation.

| Recommendation ID | Status | Priority | Proposed action | Supporting concern/finding/fact IDs | Owner role | Expected value | Effort | Verification |
|---|---|---:|---|---|---|---|---|---|
| `REC-01` | `proposed` | 1 | Continue risk-ranked AI-audit and freshness batches, close the 10 open findings, and define a bounded human-review sample | `CON-01`, `repository-health:content-assurance:coverage-gap` | Content-assurance maintainer | Raises confidence in a 222-guide AI-assisted library without mislabeling unaudited content | Large, incremental | Ledgers reconcile to inventory; agreed coverage target met; findings explicitly dispositioned |
| `REC-02` | `proposed` | 2 | Deduplicate source-health data and fail validation on duplicate IDs | `CON-02`, `repository-health:source-health:duplicate-identifiers` | Repository automation maintainer | Restores trustworthy counts and prevents silent record overwrite | Small | Duplicate fixture fails; corrected ledger passes; row count equals unique source count |
| `REC-03` | `proposed` | 3 | Modularize validator/provider routing and validate adapter docs against one canonical registry | `CON-03`, `repository-health:maintainability:automation-concentration` | Repository automation maintainer | Reduces cognitive load and documentation drift as providers grow | Medium | Existing tests remain green; all 26 adapter keys are represented; drift test passes |
| `REC-04` | `proposed` | 4 | Reuse one CI validation definition, add pip dependency updates, and adopt a documented action-reference policy | `CON-04`, `repository-health:ci:duplicated-validation-and-partial-update-coverage` | Delivery maintainer | Reduces workflow drift and makes site dependency/action updates governed and visible | Medium | Validation and deployment share one definition; pip update job exists; action refs conform to policy |
| `REC-05` | `proposed` | 5 | Execute and retain the manual accessibility matrix, adding bounded automation only where repeatable | `CON-05`, `repository-health:accessibility:manual-evidence-unrecorded` | Site maintainer | Converts a well-designed checklist into reviewable release evidence | Small to medium | All nine areas have dated pass/finding/blocked records across representative pages |

## Strengths

- The current local checkout is clean at the assessed HEAD, with 253 commits and two release tags.
- Unit tests, repository consistency validation, and existing generated-site validation passed.
- The repository uses exact site-tool dependency pins and explicit Python 3.13 CI definitions.
- Source governance is substantive: 3,248 registered sources, 222 review records, schema-backed ledgers, fail-closed source monitoring, and explicit AI-assistance disclosure.
- Architecture, automation, source-quality, contribution, security-reporting, and structured issue-intake documentation are present and findable.
- No common private-key or token signatures were found in the bounded heuristic review; this is not a comprehensive scanner result.

## Risks if unchanged

- Unaudited or stale semantic content may persist across most of the published catalog even while structural validation remains green.
- Duplicate source-health records may misstate totals and remain invisible to the primary validator.
- Continued provider expansion may make two central automation modules harder to review safely and deepen adapter-documentation drift.
- Parallel workflow definitions and partial dependency-update coverage may diverge or delay important upgrades.
- Accessibility claims will remain difficult to substantiate without retained manual interaction evidence.

## Blocked, skipped, failed, stale, and not-applicable checks

| Check / evidence | State | Reason | Assessment impact | Fallback / owner / approval needed |
|---|---|---|---|---|
| GitHub settings, rulesets, protections, review requirements | Blocked | Network/authentication prohibited | Governance controls not assessed | Separately approve read-only SCM evidence |
| GitHub Actions history, conclusions, artifacts, duration | Blocked | Network prohibited | CI reliability, flakiness, and remote build duration not assessed | Separately approve read-only CI metadata |
| Published releases and deployment history | Blocked | Network prohibited | Local tags/definitions cannot prove release/deployment state | Separately approve read-only repository/release metadata |
| Strict MkDocs rebuild | Skipped | Would write generated files outside assessment allowlist | Existing site validator passed, but no current strict-build result | Authorize generated build output or run in approved disposable location |
| Dependency vulnerability/lifecycle scans | Skipped | Network, install, and external scanners prohibited | Dependency security/support posture remains partial | Approve named local/preinstalled or remote evidence source |
| Operational-change correlation | Not assessed | No approved local normalized notice input | No vendor lifecycle applicability conclusion | Supply an approved local normalized notice set |
| Dev-container support | N/A for this Snapshot | Content/static-site repository with short documented local setup | No containerized onboarding conclusion | Reassess if a standardized container workflow is desired |

### Permission gaps

| Source / capability | Missing permission or access | Observed UTC | Assessment impact | Fallback used | Owner / approval needed |
|---|---|---|---|---|---|
| GitHub repository settings | Network and authenticated read access | 2026-09-05T18:13:02Z | Default branch, protection, rulesets, and review requirements not assessed | Local Git and checked-in files | Repository owner; separate read-only approval |
| GitHub Actions | Network and authenticated read access | 2026-09-05T18:13:02Z | Enablement, history, conclusions, artifacts, duration, and flakiness not assessed | Existing local checks and workflow definitions | Repository owner; separate read-only approval |
| GitHub releases/metadata | Network and authenticated read access | 2026-09-05T18:13:02Z | Published-release and deployed-state health not assessed | Local tags, changelog, deployment definition | Repository owner; separate read-only approval |
| OpenAI Codex service governance metadata | Service region, retention/deletion behavior, and approval expiry were unavailable locally | 2026-09-05T18:13:02Z | Full assistant-processing boundary cannot be demonstrated from repository evidence | Exact actual-egress statement; local draft retention | User/service owner; review account and service policy |

### Collection errors

None recorded.

## Evidence appendix

| Evidence ID | Class | Locator / governed ID | Captured / as-of UTC | Freshness | Access | Collector/version |
|---|---|---|---|---|---|---|
| `source.git-head` | Git history | `git:HEAD` | 18:13:02Z / 12:50:07Z | Current | Available | Git 2.55.0.windows.5 |
| `source.git-history` | Git history | `git:local-history` | 18:13:02Z / 12:50:07Z | Current | Available | Git 2.55.0.windows.5 |
| `source.inventory` | Command output | `git ls-files` and bounded inventory | 18:13:02Z / 12:50:07Z | Current | Available | Repository-health prompt |
| `source.readme` | Repository file | `README.md` | 18:13:02Z / 11:44:35Z | Current | Available | Repository-health prompt |
| `source.requirements` | Repository file | `requirements-site.txt` | 18:13:02Z / 11:44:35Z | Current | Available | Repository-health prompt |
| `source.workflow-validation` | Repository file | `.github/workflows/validate-repository.yml` | 18:13:02Z / 2026-08-31T12:12:35Z | Current | Available | Repository-health prompt |
| `source.workflow-pages` | Repository file | `.github/workflows/deploy-pages.yml` | 18:13:02Z / 2026-08-31T16:00:22Z | Current | Available | Repository-health prompt |
| `source.workflow-source-health` | Repository file | `.github/workflows/check-source-health.yml` | 18:13:02Z / 2026-08-31T16:00:22Z | Current | Available | Repository-health prompt |
| `source.workflow-objectives` | Repository file | `.github/workflows/check-certification-objectives.yml` | 18:13:02Z / 2026-08-31T10:27:25Z | Current | Available | Repository-health prompt |
| `source.dependabot` | Repository file | `.github/dependabot.yml` | 18:13:02Z / 2026-08-31T10:27:25Z | Current | Available | Repository-health prompt |
| `source.reviews` | Repository file | `data/reviews.json` | 18:13:02Z / 12:50:07Z | Current | Available | Repository-health prompt |
| `source.sources` | Repository file | `data/sources.json` | 18:13:02Z / 12:50:07Z | Current | Available | Repository-health prompt |
| `source.source-health` | Repository file | `data/source-health.json` | 18:13:02Z / 11:44:35Z | Current | Available | Repository-health prompt |
| `source.ai-audits` | Repository file | `data/ai-audits.json` | 18:13:02Z / 12:50:07Z | Current | Available | Repository-health prompt |
| `source.source-freshness` | Repository file | `data/source-freshness.json` | 18:13:02Z / 12:50:07Z | Current | Available | Repository-health prompt |
| `source.source-candidates` | Repository file | `data/source-candidates.json` | 18:13:02Z / 12:50:07Z | Current | Available | Repository-health prompt |
| `source.validator-script` | Repository file | `scripts/validate_repository.py` | 18:13:02Z / 11:44:35Z | Current | Available | Repository-health prompt |
| `source.monitor-script` | Repository file | `scripts/check_official_study_guides.py` | 18:13:02Z / 12:50:07Z | Current | Available | Repository-health prompt |
| `source.adapter-doc` | Repository file | `adapters/README.md` | 18:13:02Z / 2026-09-02T17:09:46Z | Current | Available | Repository-health prompt |
| `source.architecture` | Architecture document | `docs/ARCHITECTURE.md` | 18:13:02Z / 02:04:58Z | Current | Available | Repository-health prompt |
| `source.automation-doc` | Architecture document | `docs/AUTOMATION.md` | 18:13:02Z / unknown | Current | Available | Repository-health prompt |
| `source.accessibility` | Repository file | `docs/ACCESSIBILITY.md` | 18:13:02Z / 2026-09-01T11:01:03Z | Current | Available | Repository-health prompt |
| `source.changelog` | Repository file | `CHANGELOG.md` | 18:13:02Z / 11:44:35Z | Current | Available | Repository-health prompt |
| `source.maintainer-docs` | Repository file | `CONTRIBUTING.md` and `SECURITY.md` | 18:13:02Z / 2026-09-02T19:33:06Z | Current | Available | Repository-health prompt |
| `source.unit-tests` | Command output | Python unittest command | 18:13:02Z / unknown | Current | Available | Python 3.13.14 |
| `source.repository-validator` | Command output | Repository validator command | 18:13:02Z / unknown | Current | Available | Repository validator |
| `source.site-validator` | Command output | Site validator command | 18:13:02Z / unknown | Current | Available | Site validator |
| `source.secret-heuristic` | Command output | Bounded filename/token-signature review | 18:13:02Z / unknown | Current | Available | Repository-health prompt |
| `source.scm-blocked` | SCM metadata | `github:remote` | 18:13:02Z / unknown | Unknown | Blocked | Repository-health prompt |

## Persona view bundle

| Field | Value |
|---|---|
| View-set manifest / contract | `ADLC_Docs/quality/repository-health-views/repository-health-view-set.json` · contract `1.0.0` · SHA-256 `1896c7f207adc7fe05e2cafcd2d5f94a1378755b69719a4ec85e9db27fc158be` |
| Canonical finding-set SHA-256 | `40d4db6e2eacd8c2215cbc27bedab74de9e6c27ccd93ee95c8587067da7b9ae4` |
| Persona contract SHA-256 | `bf498800eb5209f4151fed3a72e4261665556595c6915407b3c1c4a6a668cb1e` |
| Executive summary | `repository-health-views/executive-summary.md` · 5 displayed, 0 omitted |
| Engineering-lead action plan | `repository-health-views/engineering-lead-action-plan.md` · all 5 findings |
| Developer evidence appendix | `repository-health-views/developer-evidence-appendix.md` · all 5 findings |
| Bundle validation | Passed after generation |
| Review / sharing state | Local drafts; human findings and data-handling review pending; no sharing authorized |

## Completion statement

- Mode deliverables satisfied: **yes** — repository facts, canonical finding set, primary report, and three persona views were produced at the authorized paths.
- Evidence threshold satisfied: **yes for an explicitly partial Snapshot** — local evidence is sufficient for the bounded findings, while remote claims remain blocked/not assessed.
- Budget stop condition reached: **scope stop reached; time ceiling not known to have been reached**.
- Recommended disposition: **stop for findings review**.
- Additional evidence that would change the result: separately approved read-only GitHub settings/CI/release evidence; an authorized strict site build; repeated test history; completed accessibility records; and agreed content-assurance coverage targets.
- Generated-artifact privacy review: machine validation and minimization review completed; named human review remains pending.
- No backlog candidates, specifications, tickets, source changes, or implementation changes were generated.
