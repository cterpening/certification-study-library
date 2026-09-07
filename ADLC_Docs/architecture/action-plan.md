# Action Plan — Certification Study Library

> Generated from inventory-only Phase 0 Discovery on 2026-09-05. This is an assessment plan, not an implementation plan or backlog.

## Current gate state

- Follow-up implementation: **approved by the repository owner on 2026-09-06** for
  the two new data-assurance defects and duplicate source-health cleanup. This later
  approval supersedes the assessment-only stop below for that bounded work only;
  use local tests/build checks and stage, commit and push each verified batch.
  See [implementation scope](../../docs/specs/data-assurance-remediation.md) and
  [verification record](../quality/2026-09-06-remediation-verification.md).
- Follow-up result: **seven concerns locally mitigated; two remain open**. All ten
  schemas are enforced, health identities are unique, and rubric-2 audit eligibility
  binds guide content. Outbound monitor requests and redirects now enforce the shared
  public-HTTPS boundary, and source-health report contracts no longer rely on production
  assertions. Validation and Pages now share one gate, external actions are commit-pinned,
  and Dependabot covers pip and Actions. Adapter registration is canonical and its complete
  25-adapter documentation is enforced against all 26 vendor assignments and implementations.
  Accessibility markup and four representative responsive renders now have retained automated
  evidence, while the human keyboard/assistive-technology matrix remains explicitly open.
  Verification: 116 tests, repository validation, strict site
  build and generated-link checks pass. Twenty-two rubric-2 results have been recorded across
  five later semantic-audit batches; after the Security+, Fortinet MSSP, and shared NSE 8
  evidence repairs, 15 guides remain bound to their current guide and objective versions, 204 guides are
  ready for audit preparation, and AZ-800/AZ-802 plus Fortinet MSSP remain source-gate
  blocked. Original assessment snapshots below retain
  their assessment-time state.
- Brownfield inventory: complete for the bounded local repository.
- Existing repository-health Snapshot: complete and validated, with five open findings.
- Assessment plan: **approved for local assessment waves A–D** by the repository owner on 2026-09-06; prior Bandit approval and completed evidence are retained.
- Bandit lane: **complete and validated**. Bandit 1.9.4 scanned `scripts\` and `tests\`, producing 12 raw observations consolidated into four normalized findings: two open and two false-positive.
- Waves A–D are authorized within their recorded local static evidence limits. Project commands, remote evidence collection, backlog conversion, specification, implementation, deployment and risk acceptance remain outside this assessment approval. Stage, commit and push completed assessment batches using the user's standing instruction.

## Profiles to load

| Type | Profile | Accelerator path | Decision and reason |
|---|---|---|---|
| Stack | Python, partial | `docs/stack-profiles/python.md` | Use for language guidance, but repository standard-library, unittest, pip, and layout conventions have precedence |
| Stack/content | Markdown + JSON + YAML, discovery-derived | Repository policies and schemas | No exact accelerator stack profile; preserve guide/front-matter/schema conventions |
| Application | Content/static-site repository, discovery-derived | Closest canonical profile: `config/application-profiles/frontend-application.json` | Frontend accessibility/performance concerns apply, but component-driven UI and feature-first structure do not describe this repository |
| Cloud | None | — | No owned cloud workload or IaC found; vendor cloud topics in guides are content, not infrastructure evidence |
| Assessment mode/profile | Snapshot / standard | `config/tool-neutral/repository-report-modes.json`; `config/audit-report-catalog.json` | Continues the previously selected bounded mode and security/quality/governance/operations profile |

## Existing validated assessment input

| Artifact | Status | Use in later lanes |
|---|---|---|
| `ADLC_Docs/discovery/repository-facts.json` | Validated; 40 facts, 29 evidence sources, partial coverage | Reuse rather than recollecting unchanged local facts |
| `ADLC_Docs/findings/2026-09-05-repository-health.json` | Validated; 5 open findings | Preserve finding identities and avoid duplicate concerns |
| `ADLC_Docs/quality/2026-09-05-repository-health.md` | Rendered from validated facts/findings | Current local health synthesis |
| `ADLC_Docs/quality/repository-health-views/` | Validated three-view bundle | Findings review by executive, engineering, and developer readers |

## Proposed assessment sequence

The repository owner approved continuation of the local assessment plan on 2026-09-06. Execute waves A–D in order and record completion per wave. Wave E uses a documented static fallback after generator write-set review; blocked and deferred operations are unchanged.

| Wave | Lanes | Purpose | Default operation budget |
|---|---|---|---|
| A — contract and assurance | Data/schema migration readiness; test maturity; AI system assurance; documentation readiness | Address the existing source-health integrity defect and the largest assurance/evidence gaps | Four Snapshot lanes; target 40 minutes, ceiling 80; no network; no project commands; maximum 8 local assessment tool runs per lane |
| B — maintainability and agentic workflow | Code quality; application-style conformance; agentic-delivery readiness; component change-risk map | Bound central-module, style-drift, human-gate, and change-risk concerns | Four Snapshot lanes with the same per-lane limits |
| C — security and supply chain | Security review; secret/key inventory; delivery supply-chain integrity; dependency modernization | Review public-boundary, workflow, action, and dependency evidence without scanners or lookups | Four Snapshot lanes; local static evidence only; remote/dependency state remains blocked |
| D — architecture, UX, and operations | Architecture quality; threat model; UX/accessibility; runbook readiness; release readiness | Complete system-boundary, accessibility-evidence, operating, and release views | Five Snapshot lanes; dynamic/browser and remote operations require separate approval |
| E — optional structural views | Component/import diagram | Static import view completed after generator inspection; automated generator not executed | Local static inspection and the exact dated Markdown output only |

The Phase 0 inventory satisfies the immediate purpose of the catalog intake and architecture-diagram lanes. A separate report can still be requested, but is not proposed before the higher-value waves.

## Proposed applicable assessment lanes

The exact wave A–D paths below were approved for this continuation. Preserve the September 5 filenames and record the actual September 6 assessment date inside each artifact. Validate every JSON finding set before rendering Markdown; reuse canonical fingerprints for overlapping concerns.

| Priority | Lane / report ID | Prompt, tool, or evidence | Operation class | Proposed exact report and finding-set paths | Approval or blocker | Why |
|---:|---|---|---|---|---|---|
| 0 | `intake-audit` | Current Brownfield Phase 0 inventory | Local assistant review | Current `ADLC_Docs/architecture/` and `ADLC_Docs/discovery/` outputs; no extra file proposed | Satisfied for initial inventory; reviewer may request a separate intake format | Avoid duplicate inventory work |
| 1 | `data-schema-migration-readiness` | `prompts/data-schema-migration-readiness.md`; local schemas/catalog consumers | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\architecture\2026-09-05-data-schema-migration-readiness.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-data-schema-migration-readiness.json` | Wave A approved 2026-09-06 | Ten schemas and the duplicate-ID defect create immediate contract risk |
| 2 | `test-maturity-readiness` | `prompts/test-maturity-readiness.md`; existing tests/results | Local assistant static review; do not rerun commands unless explicitly added | `C:\src\certification-study-library\ADLC_Docs\quality\2026-09-05-test-maturity-readiness.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-test-maturity-readiness.json` | Wave A approved 2026-09-06 | Tests are extensive, but coverage/repeatability and the missing duplicate case need a coherent view |
| 3 | `ai-system-assurance` | `prompts/ai-system-assurance.md`; AI audit/freshness/source-review contracts | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\security\2026-09-05-ai-system-assurance.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-ai-system-assurance.json` | Wave A approved 2026-09-06 | The product is explicitly AI-assisted and has incomplete independent/human assurance coverage |
| 4 | `documentation-readiness` | `prompts/documentation-readiness.md`; local architecture/runbook/contributor docs | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\governance\2026-09-05-documentation-readiness.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-documentation-readiness.json` | Wave A approved 2026-09-06 | Documentation is strong but adapter and review evidence drift is visible |
| 5 | `quality-review` | `prompts/review.md`; Python, schemas, data, and tests | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\quality\2026-09-05-quality-review.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-quality-review.json` | Wave B approved 2026-09-06 | Central modules and data contracts warrant a focused maintainability review |
| 6 | `application-style-conformance` | `prompts/application-style-conformance.md`; current/target style artifacts | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\quality\2026-09-05-application-style-conformance.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-application-style-conformance.json` | Wave B approved 2026-09-06 | Brownfield convention precedence must be tested without normalizing style opportunistically |
| 7 | `agentic-delivery-readiness` | `prompts/agentic-delivery-readiness.md`; repository instructions and AI workflows | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\quality\2026-09-05-agentic-delivery-readiness.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-agentic-delivery-readiness.json` | Wave B approved 2026-09-06 | AI-assisted maintenance has explicit gates that should be assessed as a system |
| 8 | `component-change-risk-map` | `prompts/component-change-risk-map.md`; bounded local Git and code structure | Local Git/static review; no people scoring | `C:\src\certification-study-library\ADLC_Docs\quality\2026-09-05-component-change-risk-map.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-component-change-risk-map.json` | Wave B approved 2026-09-06 | Large central scripts and rapid provider growth may concentrate change risk |
| 9 | `security-review` | `prompts/security-review.md`; source retrieval, site allowlist, workflows, content boundary | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\security\2026-09-05-security-review.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-security-review.json` | Wave C approved 2026-09-06 | Public publication and network-capable maintenance scripts create security-relevant boundaries |
| 10 | `secret-key-inventory` | `prompts/secret-key-inventory.md`; bounded local tracked-file evidence | Local assistant static review; no secret-store or provider query | `C:\src\certification-study-library\ADLC_Docs\security\2026-09-05-secret-key-inventory.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-secret-key-inventory.json` | Wave C approved 2026-09-06 | Public repository intent makes secret-handling evidence important |
| 11 | `delivery-supply-chain-integrity` | `prompts/delivery-supply-chain-integrity.md`; requirements, action refs, workflows, facts | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\security\2026-09-05-delivery-supply-chain-integrity.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-delivery-supply-chain-integrity.json` | Wave C approved 2026-09-06; remote enforcement remains blocked | Existing findings identify mutable refs, duplicated CI, and missing pip updates |
| 12 | `dependency-modernization` | `prompts/dependency-modernization.md`; `requirements-site.txt` and local consumers | Local declarations only; no lifecycle/network lookup | `C:\src\certification-study-library\ADLC_Docs\quality\2026-09-05-dependency-modernization.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-dependency-modernization.json` | Wave C approved 2026-09-06; current-support claims remain blocked | Exact pins exist without lockfile, pip update automation, or approved lifecycle evidence |
| 13 | `architecture-quality-neutral` | `prompts/architecture-quality-neutral.md`; discovery architecture set | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\architecture\2026-09-05-architecture-quality-neutral.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-architecture-quality-neutral.json` | Wave D approved 2026-09-06 | Trust and publication boundaries can be assessed without cloud access |
| 14 | `threat-model-review` | `prompts/threat-model-review.md`; trust-boundary and data-flow evidence | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\security\2026-09-05-threat-model-review.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-threat-model-review.json` | Wave D approved 2026-09-06 | Source ingestion, generated content, workflow writes, and public output have explicit threat surfaces |
| 15 | `ux-accessibility-conformance` | `prompts/ux-accessibility-conformance.md`; local source/static evidence | Local static review only | `C:\src\certification-study-library\ADLC_Docs\quality\2026-09-05-ux-accessibility-conformance.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-ux-accessibility-conformance.json` | Wave D approved 2026-09-06; browser/assistive-technology execution separately gated | The existing accessibility finding is an evidence gap, not a conformance verdict |
| 16 | `runbook-readiness` | `prompts/runbook-readiness.md`; automation/publishing/source-review docs | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\operations\2026-09-05-runbook-readiness.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-runbook-readiness.json` | Wave D approved 2026-09-06 | Maintenance operations are documented but remote execution/recovery evidence is absent |
| 17 | `release-readiness-assembly` | `prompts/release-readiness-assembly.md`; existing facts, findings, tags, and changelog | Local artifact assembly | `C:\src\certification-study-library\ADLC_Docs\operations\2026-09-05-release-readiness-assembly.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-release-readiness-assembly.json` | Wave D approved 2026-09-06; published-release/deployment state remains blocked | Current evidence can support a bounded decision without re-scanning |
| 18 | `architecture-diagram` | Current `dependency-map.md`; optional `prompts/architecture-diagram.md` | Local assistant rendering | Current `C:\src\certification-study-library\ADLC_Docs\architecture\dependency-map.md`; no additional output proposed initially | Satisfied for discovery; separate catalog view requires new approval | Avoid duplicate diagrams before review |
| 19 | `component-diagram` | Static import inspection; `Invoke-RepoDiscovery.ps1` reviewed but not run | Read-only source inspection | `C:\src\certification-study-library\ADLC_Docs\architecture\2026-09-05-component-diagram.md`; finding set only if normalized concerns are produced | Static fallback completed; automated generator not executed | Static imports are simple enough that command value should be confirmed first |

## Assessment envelope for approved local waves

| Field | Proposed value |
|---|---|
| Accelerator root | `C:\src-IBM\AgenticDevelopment` — strictly read-only |
| Target root | `C:\src\certification-study-library` |
| Primary components | One content/static-site repository |
| Mode/profile | Snapshot / standard |
| Local tools | PowerShell 7.6.5, Git 2.55.0.windows.5, Python 3.13.14, ripgrep 15.2.0; assistant-native prompt review |
| Default evidence | Existing validated repository facts/findings plus current local files and Git history |
| Network/authentication | No assessment-provider requests or new authentication; user-authorized Git push to existing origin only |
| External/provider requests | 0 |
| Project commands | 0 unless a later approval names the exact command and writes |
| Package installation | Prohibited except for Bandit 1.9.4 and its dependencies in the approved lane below |
| External scanners | Prohibited except for the approved local Bandit 1.9.4 execution below |
| Per-lane time budget | Target 10 minutes; ceiling 20 minutes |
| Per-lane automated-tool ceiling | 8 local read-only assessment runs |
| Outputs | Only the exact report/finding paths approved for that wave under `ADLC_Docs/` |
| Data movement | Active Codex inference boundary only, except package metadata/download requests to PyPI for the approved Bandit install; no repository content is sent to PyPI |
| Handling limitation | Data classification, Codex service region/retention/deletion, and approval expiry require owner review |
| Stop | Validate finding JSON before Markdown, present findings, and stop before candidates/specification/implementation |

## Approved Bandit execution lane

| Field | Authorized value |
|---|---|
| Lane | `bandit-scan` |
| Approval | Repository owner approval in this session on 2026-09-05 |
| Tool/source | Bandit 1.9.4 from PyPI, pinned in `requirements-security.txt` |
| Installation boundary | Target-local ignored virtual environment at `C:\src\certification-study-library\.venv\`; no global installation and no accelerator writes |
| Installation commands | `python -m venv .venv`; `.\.venv\Scripts\python.exe -m pip install --disable-pip-version-check --requirement requirements-security.txt` |
| Scan command | `.\.venv\Scripts\bandit.exe -r scripts tests -f json -o ADLC_Docs\security\2026-09-05-bandit-raw.json` |
| Scan inputs | Tracked Python source below `scripts\` and `tests\` only |
| Authorized outputs | `C:\src\certification-study-library\requirements-security.txt`; `C:\src\certification-study-library\ADLC_Docs\security\2026-09-05-bandit-raw.json`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-bandit-scan.json`; `C:\src\certification-study-library\ADLC_Docs\security\2026-09-05-bandit.html`; approval/status updates to this plan and `ADLC_Docs\assessment-decisions.json` |
| Network/egress | PyPI package resolution and downloads only during installation; no repository content sent. Bandit scan and accelerator validation/rendering remain local |
| Budget | One environment creation, one installation, one recursive scan, one finding-set validation, and one HTML rendering/validation pass |
| Stop | Report scanner findings for review; do not remediate, generate backlog candidates/specifications, or change source/CI |

### Bandit execution outcome

| Checkpoint | Result |
|---|---|
| Installation | Bandit 1.9.4 installed successfully in the ignored target-local `.venv\`; package requests were limited to PyPI |
| Scan | Complete across `scripts\` and `tests\`; 7,839 lines, 12 raw observations, no skipped tests, and no scanner errors |
| Raw severity | 3 medium and 9 low; 9 high-confidence and 3 medium-confidence observations |
| Triage | Four normalized findings: two open source-code concerns and two test-only false-positive groups |
| Validation | `ADLC_Docs\findings\2026-09-05-bandit-scan.json` passed `Validate-FindingSet.ps1` |
| Rendering | `ADLC_Docs\security\2026-09-05-bandit.html` was rendered only after finding-set validation |
| Next gate | Findings review; remediation and recurring CI integration are not authorized |

## Continuation progress — 2026-09-06

| Wave | State | Result |
|---|---|---|
| A | Complete; findings review pending | Four validated finding sets and reports; five distinct concerns, including two newly identified issues |
| B | Complete; findings review pending | Four validated finding sets and reports; existing concerns reused; five style rules blocked by insufficient evidence |
| C | Complete; findings review pending | Four validated partial reports; Bandit reused; remote lifecycle, secrets and protection evidence unavailable |
| D | Complete; findings review pending | Five validated partial reports; release sign-off needs a named candidate and current verification |
| E | Complete as labeled static fallback | Manual import view; generator write set exceeds the exact one-file output contract, so it was not invoked |

The new findings concern uneven schema enforcement and missing guide-content binding in AI-audit eligibility. Prior repository-health and Bandit records are preserved; repeated fingerprints represent shared concerns, not additional unique issues.

### Findings review index

Seventeen assessment lanes now have validated JSON finding sets and tailored Markdown reports; one additional static component/import view completes the approved local plan. Every lane remains explicit about missing runtime/provider evidence. Historical repository-health, Bandit and persona artifacts were preserved.

The [release-readiness assembly](../operations/2026-09-05-release-readiness-assembly.md) gathers all **nine distinct open findings**: **one high, six medium and two low**. The two historical Bandit false-positive groups remain separate. Assessment completion does not mean remediation, accepted risk or release approval.

| Concern | Severity | Canonical finding / review context |
|---|---|---|
| Independent assurance coverage | High | `repository-health:content-assurance:coverage-gap`; [AI assurance](../security/2026-09-05-ai-system-assurance.md) |
| Duplicate source-health identifiers | Medium | `repository-health:source-health:duplicate-identifiers`; [data/schema readiness](2026-09-05-data-schema-migration-readiness.md) |
| Automation concentration and adapter drift | Medium | `repository-health:maintainability:automation-concentration`; [component risk](../quality/2026-09-05-component-change-risk-map.md) |
| Duplicated CI and incomplete dependency updates | Medium | `repository-health:ci:duplicated-validation-and-partial-update-coverage`; [supply chain](../security/2026-09-05-delivery-supply-chain-integrity.md) |
| Uneven schema enforcement — new | Medium | `assessment:data-contracts:uneven-schema-enforcement`; [data/schema readiness](2026-09-05-data-schema-migration-readiness.md) |
| Audit eligibility does not bind guide content — new | Medium | `assessment:ai-assurance:guide-content-not-bound`; [AI assurance](../security/2026-09-05-ai-system-assurance.md) |
| Outbound URL validation | Medium | `bandit:B310:scripts-check-official-study-guides:urlopen`; [static security](../security/2026-09-05-security-review.md) |
| Production assertions | Low | `bandit:B101:scripts-check-source-health:assert`; [static security](../security/2026-09-05-security-review.md) |
| Manual accessibility evidence | Low | `repository-health:accessibility:manual-evidence-unrecorded`; [accessibility](../quality/2026-09-05-ux-accessibility-conformance.md) |

The highest-value review order is catalog identity/schema enforcement, guide-content audit binding, existing content-assurance findings, outbound retrieval controls, then delivery/accessibility evidence. These are assessment recommendations only; no backlog candidates, specifications, fixes, tickets or waivers were created.

### Completed batch commits

Final verification: all 19 finding sets (17 new plus the two historical sets), the repository-facts manifest, and the three-view historical persona bundle passed accelerator validators. Local links and unresolved placeholders were checked across the 17 new reports, this index, and the static component view. All 46 decisions reconcile: 21 applicable, 2 blocked, 7 deferred and 16 not applicable. Only ADLC_Docs artifacts changed in this continuation; accelerator revision 82d4bca and its clean worktree were preserved. No project tests, builds or scanners were rerun.

- Wave A: `b555707` — data contracts and content assurance.
- Wave B: `3e79e84` — maintainability and agentic delivery readiness.
- Wave C: `9ebfda5` — static security and delivery supply chain.
- Wave D: `ecdccf4` — architecture and operational release readiness.
- Wave E and final index: included in this document's completion commit; identify it from Git history.

## Blocked lanes

| Lane | Blocker | Manual fallback | What would authorize it |
|---|---|---|---|
| `code-duplication` | Catalog tool is npx jscpd; tooling/install/network side effects are prohibited | Bounded manual structure review, explicitly not called a scanner result | Approve runtime, exact version/source, command, target paths, network, and writes |
| `github-delivery-health` | Remote settings, protections, PR flow, run history, and Pages evidence require network/authentication | Retain the partial local repository-health evidence | Approve endpoint, read-only identity, fields, request limit, egress/retention, and output paths |

## Deferred lanes

| Lane | Reason to defer | Evidence needed to reconsider |
|---|---|---|
| `dr-bcp-assessment` | No continuity objectives or remote recovery evidence | Owner-approved RPO/RTO and service/recovery records |
| `compliance-mapping` | No accountable framework applicability decision | Confirmed legal/regulatory/contractual requirement |
| `maturity-assessment` | Broader than the immediate evidence decisions | Review higher-priority findings and define desired decision |
| `privacy-data-classification` | Classification and retention ownership not supplied | Named data owner and handling/retention decisions |
| `observability-slo-privacy` | No deployed telemetry/SLO/alert evidence | Approved Pages/Actions/monitoring evidence and service objectives |
| `performance-capacity-efficiency` | Strict build and CI performance history unavailable | Authorized clean build plus CI duration/capacity evidence |
| `resilience-recovery-evidence` | No restore exercise or remote service recovery evidence | Recovery objectives and tested restore/rollback records |

## Not-applicable lanes

The following 16 catalog reports are currently not applicable based on bounded local evidence: `waf-review`, `naming-audit`, `cost-estimate`, `rbac-access-matrix`, `network-topology`, `deployment-order`, `drift-report`, `tag-compliance`, `shared-responsibility`, `npm-audit`, `license-check`, `checkov-terraform`, `checkov-docker`, `checkov-kubernetes`, `tf-quality`, and `api-event-contracts`.

Cloud and certification terminology inside study guides is not used to infer deployed cloud, network, API, container, or IaC components.

## Skills to invoke

None during discovery. Future lanes should use the named canonical prompts directly from the read-only accelerator. No skill, prompt, assistant wiring, or configuration will be copied into the target.

## Compliance frameworks

No external regulatory framework is selected. The repository's own public-source, copyright/exam-integrity, AI-disclosure, and private-data exclusion policies are observed governance requirements. GDPR, PCI DSS, HIPAA, SOC 2, NIST, and similar applicability remains unknown unless an accountable owner supplies a requirement and data-flow evidence.

## Evidence gaps and blockers

- [ ] Remote GitHub default branch, protections, rulesets, required checks, owner review, workflow history, Pages settings, releases, and deployment state — impact: delivery governance and reliability remain unassessed.
- [ ] Data classification, assessment retention period, expiry action, and named human reviewer — impact: generated artifacts remain local drafts.
- [ ] Clean build, repeated test, coverage, mutation, lint, formatting, and type-check evidence — impact: engineering-quality conclusions remain bounded.
- [ ] Dependency lifecycle, vulnerability, transitive-lock, license, and SBOM evidence — impact: supply-chain posture remains partial.
- [ ] Browser and assistive-technology results — impact: accessibility conformance cannot be concluded.
- [ ] Path-level ownership and contributor/PR history — impact: ownership continuity and collaboration health remain partial.

## Provisional themes

These themes are not findings beyond the existing validated finding set, backlog items, or specifications:

1. Protect catalog identity and schema compatibility as the library grows.
2. Expand risk-ranked independent and human assurance without conflating review layers.
3. Reduce automation concentration while preserving CLI behavior and fail-closed semantics.
4. Consolidate delivery validation and govern dependency/action updates.
5. Convert accessibility and remote delivery expectations into retained evidence.

## Assessment-plan decision

- **Status:** assessments-complete-with-limitations — findings review pending
- **Decision reference:** `brownfield-discovery-v1`
- **Reviewer role / recorded UTC time:** repository owner / 2026-09-06T17:15:20Z; prior Bandit approval 2026-09-05 retained
- **Exact operations completed:** local static assessment waves A–D, the Wave E static import fallback, declared JSON/report paths, assessment status updates, contract validation, and stage/commit/push after each batch
- **Requested decision after completion:** review consolidated assessment findings and Bandit triage; candidate generation and implementation are separate work
- **Important:** wave approval authorizes only the listed assessment reads and output paths. It does not authorize project changes, finding acceptance, backlog conversion, ticket creation, specification, implementation, deployment, or external access.

## Mandatory stop — completed assessment phase

The approved local waves are validated and rendered; stop here for consolidated findings review. Preserve explicit limitations for remote/runtime evidence and any conditional generator. Do not generate backlog candidates or specifications, remediate findings, or change source or CI.
