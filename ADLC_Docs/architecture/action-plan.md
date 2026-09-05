# Action Plan — Certification Study Library

> Generated from inventory-only Phase 0 Discovery on 2026-09-05. This is an assessment plan, not an implementation plan or backlog.

## Current gate state

- Brownfield inventory: complete for the bounded local repository.
- Existing repository-health Snapshot: complete and validated, with five open findings.
- Assessment plan: **approved for the Bandit lane only** by the repository owner on 2026-09-05.
- Bandit 1.9.4 installation, the bounded local scan, validation, rendering, and the exact outputs below are authorized. Other assessments, project commands, remote evidence, backlog conversion, specification, implementation, deployment, and risk acceptance remain **not authorized**.

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

The sequence is deliberately wave-based. Approval of one wave does not approve later waves.

| Wave | Lanes | Purpose | Default operation budget |
|---|---|---|---|
| A — contract and assurance | Data/schema migration readiness; test maturity; AI system assurance; documentation readiness | Address the existing source-health integrity defect and the largest assurance/evidence gaps | Four Snapshot lanes; target 40 minutes, ceiling 80; no network; no project commands; maximum 8 local assessment tool runs per lane |
| B — maintainability and agentic workflow | Code quality; application-style conformance; agentic-delivery readiness; component change-risk map | Bound central-module, style-drift, human-gate, and change-risk concerns | Four Snapshot lanes with the same per-lane limits |
| C — security and supply chain | Security review; secret/key inventory; delivery supply-chain integrity; dependency modernization | Review public-boundary, workflow, action, and dependency evidence without scanners or lookups | Four Snapshot lanes; local static evidence only; remote/dependency state remains blocked |
| D — architecture, UX, and operations | Architecture quality; threat model; UX/accessibility; runbook readiness; release readiness | Complete system-boundary, accessibility-evidence, operating, and release views | Five Snapshot lanes; dynamic/browser and remote operations require separate approval |
| E — optional structural views | Component/import diagram | Produce a code-import view only after the generator's complete write set is reviewed and contained | One separately approved local command |

The Phase 0 inventory satisfies the immediate purpose of the catalog intake and architecture-diagram lanes. A separate report can still be requested, but is not proposed before the higher-value waves.

## Proposed applicable assessment lanes

Every output below is a **future proposed path** under the target root. None is authorized by this plan alone. Each report must first create and validate its JSON finding set, including an empty finding array when no actionable concern is found, before rendering Markdown.

| Priority | Lane / report ID | Prompt, tool, or evidence | Operation class | Proposed exact report and finding-set paths | Approval or blocker | Why |
|---:|---|---|---|---|---|---|
| 0 | `intake-audit` | Current Brownfield Phase 0 inventory | Local assistant review | Current `ADLC_Docs/architecture/` and `ADLC_Docs/discovery/` outputs; no extra file proposed | Satisfied for initial inventory; reviewer may request a separate intake format | Avoid duplicate inventory work |
| 1 | `data-schema-migration-readiness` | `prompts/data-schema-migration-readiness.md`; local schemas/catalog consumers | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\architecture\2026-09-05-data-schema-migration-readiness.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-data-schema-migration-readiness.json` | Wave A approval | Ten schemas and the duplicate-ID defect create immediate contract risk |
| 2 | `test-maturity-readiness` | `prompts/test-maturity-readiness.md`; existing tests/results | Local assistant static review; do not rerun commands unless explicitly added | `C:\src\certification-study-library\ADLC_Docs\quality\2026-09-05-test-maturity-readiness.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-test-maturity-readiness.json` | Wave A approval | Tests are extensive, but coverage/repeatability and the missing duplicate case need a coherent view |
| 3 | `ai-system-assurance` | `prompts/ai-system-assurance.md`; AI audit/freshness/source-review contracts | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\security\2026-09-05-ai-system-assurance.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-ai-system-assurance.json` | Wave A approval | The product is explicitly AI-assisted and has incomplete independent/human assurance coverage |
| 4 | `documentation-readiness` | `prompts/documentation-readiness.md`; local architecture/runbook/contributor docs | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\governance\2026-09-05-documentation-readiness.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-documentation-readiness.json` | Wave A approval | Documentation is strong but adapter and review evidence drift is visible |
| 5 | `quality-review` | `prompts/review.md`; Python, schemas, data, and tests | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\quality\2026-09-05-quality-review.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-quality-review.json` | Wave B approval | Central modules and data contracts warrant a focused maintainability review |
| 6 | `application-style-conformance` | `prompts/application-style-conformance.md`; current/target style artifacts | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\quality\2026-09-05-application-style-conformance.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-application-style-conformance.json` | Wave B approval | Brownfield convention precedence must be tested without normalizing style opportunistically |
| 7 | `agentic-delivery-readiness` | `prompts/agentic-delivery-readiness.md`; repository instructions and AI workflows | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\quality\2026-09-05-agentic-delivery-readiness.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-agentic-delivery-readiness.json` | Wave B approval | AI-assisted maintenance has explicit gates that should be assessed as a system |
| 8 | `component-change-risk-map` | `prompts/component-change-risk-map.md`; bounded local Git and code structure | Local Git/static review; no people scoring | `C:\src\certification-study-library\ADLC_Docs\quality\2026-09-05-component-change-risk-map.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-component-change-risk-map.json` | Wave B approval | Large central scripts and rapid provider growth may concentrate change risk |
| 9 | `security-review` | `prompts/security-review.md`; source retrieval, site allowlist, workflows, content boundary | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\security\2026-09-05-security-review.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-security-review.json` | Wave C approval | Public publication and network-capable maintenance scripts create security-relevant boundaries |
| 10 | `secret-key-inventory` | `prompts/secret-key-inventory.md`; bounded local tracked-file evidence | Local assistant static review; no secret-store or provider query | `C:\src\certification-study-library\ADLC_Docs\security\2026-09-05-secret-key-inventory.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-secret-key-inventory.json` | Wave C approval | Public repository intent makes secret-handling evidence important |
| 11 | `delivery-supply-chain-integrity` | `prompts/delivery-supply-chain-integrity.md`; requirements, action refs, workflows, facts | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\security\2026-09-05-delivery-supply-chain-integrity.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-delivery-supply-chain-integrity.json` | Wave C approval; remote enforcement remains blocked | Existing findings identify mutable refs, duplicated CI, and missing pip updates |
| 12 | `dependency-modernization` | `prompts/dependency-modernization.md`; `requirements-site.txt` and local consumers | Local declarations only; no lifecycle/network lookup | `C:\src\certification-study-library\ADLC_Docs\quality\2026-09-05-dependency-modernization.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-dependency-modernization.json` | Wave C approval; current-support claims remain blocked | Exact pins exist without lockfile, pip update automation, or approved lifecycle evidence |
| 13 | `architecture-quality-neutral` | `prompts/architecture-quality-neutral.md`; discovery architecture set | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\architecture\2026-09-05-architecture-quality-neutral.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-architecture-quality-neutral.json` | Wave D approval | Trust and publication boundaries can be assessed without cloud access |
| 14 | `threat-model-review` | `prompts/threat-model-review.md`; trust-boundary and data-flow evidence | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\security\2026-09-05-threat-model-review.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-threat-model-review.json` | Wave D approval | Source ingestion, generated content, workflow writes, and public output have explicit threat surfaces |
| 15 | `ux-accessibility-conformance` | `prompts/ux-accessibility-conformance.md`; local source/static evidence | Local static review only | `C:\src\certification-study-library\ADLC_Docs\quality\2026-09-05-ux-accessibility-conformance.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-ux-accessibility-conformance.json` | Wave D approval; browser/assistive-technology execution separately gated | The existing accessibility finding is an evidence gap, not a conformance verdict |
| 16 | `runbook-readiness` | `prompts/runbook-readiness.md`; automation/publishing/source-review docs | Local assistant static review | `C:\src\certification-study-library\ADLC_Docs\operations\2026-09-05-runbook-readiness.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-runbook-readiness.json` | Wave D approval | Maintenance operations are documented but remote execution/recovery evidence is absent |
| 17 | `release-readiness-assembly` | `prompts/release-readiness-assembly.md`; existing facts, findings, tags, and changelog | Local artifact assembly | `C:\src\certification-study-library\ADLC_Docs\operations\2026-09-05-release-readiness-assembly.md`; `C:\src\certification-study-library\ADLC_Docs\findings\2026-09-05-release-readiness-assembly.json` | Wave D approval; published-release/deployment state remains blocked | Current evidence can support a bounded decision without re-scanning |
| 18 | `architecture-diagram` | Current `dependency-map.md`; optional `prompts/architecture-diagram.md` | Local assistant rendering | Current `C:\src\certification-study-library\ADLC_Docs\architecture\dependency-map.md`; no additional output proposed initially | Satisfied for discovery; separate catalog view requires new approval | Avoid duplicate diagrams before review |
| 19 | `component-diagram` | Proposed `Invoke-RepoDiscovery.ps1` with explicit target and output | Existing local command with potential multi-file writes | `C:\src\certification-study-library\ADLC_Docs\architecture\2026-09-05-component-diagram.md`; finding set only if normalized concerns are produced | Wave E approval only after dry containment/write review | Static imports are simple enough that command value should be confirmed first |

## Assessment envelope for a future approved wave

| Field | Proposed value |
|---|---|
| Accelerator root | `C:\src-IBM\AgenticDevelopment` — strictly read-only |
| Target root | `C:\src\certification-study-library` |
| Primary components | One content/static-site repository |
| Mode/profile | Snapshot / standard |
| Local tools | PowerShell 7.6.5, Git 2.55.0.windows.5, Python 3.13.14, ripgrep 15.2.0; assistant-native prompt review |
| Default evidence | Existing validated repository facts/findings plus current local files and Git history |
| Network/authentication | None |
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

- **Status:** partially-approved — Bandit lane only
- **Decision reference:** `brownfield-discovery-v1`
- **Reviewer role / UTC time:** repository owner / 2026-09-05T19:05:40Z
- **Exact operations currently authorized:** completed inventory-only discovery, previously completed repository-health Snapshot, and the pinned/bounded Bandit lane documented above
- **Requested decision:** review the Bandit findings after execution; all other proposed waves remain gated
- **Important:** wave approval authorizes only the listed assessment reads and output paths. It does not authorize project changes, finding acceptance, backlog conversion, ticket creation, specification, implementation, deployment, or external access.

## Mandatory stop

After the approved Bandit lane is validated and rendered, stop for findings review. No other assessment lane, scanner, project command, remote query, backlog candidate, specification, source change, CI change, or implementation is authorized by this approval.
