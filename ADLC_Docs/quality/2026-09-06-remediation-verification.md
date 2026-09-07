# Data-assurance remediation verification — September 6, 2026

The owner's follow-up approval authorizes the bounded implementation in
[the target-specific spec](../../docs/specs/data-assurance-remediation.md).
Original assessment snapshots and persona views remain unchanged historical evidence.
The accelerator is read-only; only target files are changed. No remote settings, CI
history, branch protections, external sources or dependency registries were inspected.

## Batch 1 — catalog contracts and duplicate health records

Implementation and local verification complete on Python 3.13.14.
Committed and pushed as `4d98b19`.

- Apply all ten schemas before semantic processing, including format checks; reject
  missing catalogs and invalid schemas with diagnostics.
- Add the 27 established source categories used by 117 records to the finite schema
  enum. Do not change source records or treat arbitrary categories as valid.
- Reject duplicate health IDs in validation, and duplicate input/baseline IDs in the
  monitor before fetching. Reject duplicate newly fetched results before writing.
- Remove seven older copies across six IDs: `aws-aif-c01-bedrock`,
  `aws-aif-c01-genai-lens`, `kubernetes-v1-35-docs` (two older copies),
  `snowflake-architecture`, `snowflake-practice-exams`, `snowflake-snowpro-policies`.
  All fields except `checked_at` match their retained newest observation. The snapshot
  now has 3,248 rows and 3,248 distinct IDs. No source was fetched or revalidated;
  discarded copies remain in Git history. `generated_on` remains September 5.

Verification passed: 93 unit tests (`python -m unittest discover -s tests -v`),
`python scripts/validate_repository.py`, `python scripts/prepare_site.py`,
`python -m mkdocs build --strict --config-file .site-build/mkdocs.yml`,
`python scripts/validate_site.py`, and `git diff --check`.
The site preparer regenerated only the ignored `.site-build` directory and MkDocs
regenerated `site`; both are recoverable build output. The strict build emitted
existing navigation info and the theme's upstream compatibility notice, not a failure.

Locally mitigated findings: `repository-health:source-health:duplicate-identifiers`
and `assessment:data-contracts:uneven-schema-enforcement`. This record supplements,
and does not rewrite, the original assessment dispositions.

## Batch 2 — guide-bound AI-audit eligibility

Implementation and local verification complete on Python 3.13.14.

- Hash the complete guide text, with universal newline normalization only, and bind
  default completion keys to exam code, blueprint hash, guide hash and rubric version.
- Require valid guide hashes in rubric-2 schema and semantic validation; advance the
  active rubric to 2 without rewriting any rubric-1 batch, finding or result.
- Preserve historical guide hashes even after later edits. Missing/invalid hashes and
  legacy rubric results cannot suppress current audit eligibility.
- Reject duplicate health rows in audit input indexing. Preserve explicit audit
  selection and the current passed source-validation prerequisite.
- The first real-data smoke test exposed a pre-existing default-queue abort on
  AZ-800's blocked review. Default manifests now retain AZ-800 and AZ-802 as explicit
  `blocked_items` while selecting from the 220 ready guides. Explicit blocked requests
  still fail; an all-blocked queue reports blockers rather than claiming coverage.

Verification passed: all 105 unit tests, repository validation, site preparation,
strict MkDocs build, generated-site validation and whitespace checks, using the same
commands as batch 1. Regressions exercise guide-only changes, unchanged text,
CRLF/CR/LF equivalence, whitespace edits, blueprint/rubric changes, explicit selection,
legacy/malformed bindings, schema and semantic enforcement, mixed/all-blocked queues,
and source-gate bypass rejection.

Read-only CLI smoke test:
`python scripts/prepare_ai_audit_batch.py --batch-id remediation-smoke-2026-09-06 --size 10`
returned rubric 2, ten items with valid guide hashes, and the two named source-gate
blockers. No manifest file or completed audit was written. Git comparison confirmed
all four historical batches and 39 results are unchanged; only the active top-level
rubric version changed in `data/ai-audits.json`.

Locally mitigated finding: `assessment:ai-assurance:guide-content-not-bound`.

## Current follow-up status and limitations

Three of the nine consolidated assessment concerns are locally mitigated by these
two batches. The original dated assessment JSONs/reports remain historical snapshots;
this record supplies implementation evidence rather than rewriting their earlier state.

Two concerns remain open: assurance coverage and missing manual accessibility evidence.
These changes are not a
new security scan, live source review, accessibility attestation or remote CI assessment.
No new independent or human audit has been performed: 39 historical rubric-1 results
remain, zero rubric-2 results exist, 220 guides are ready for audit preparation and two
remain source-gate blocked. Security-boundary remediation is the next bounded code pass;
independent guide audits should resume in small batches, without bypassing source gates.

## Batch 3 — outbound public-HTTPS enforcement

Implementation and local verification complete on Python 3.13.14.

- Add one shared URL policy for both network-capable monitors. Reject non-HTTPS schemes,
  embedded credentials, localhost, non-public literal IP addresses, and non-default HTTPS
  ports before calling the opener; validate every final redirect as well.
- Restrict objective-monitor redirects to the configured host or its `www` equivalent.
  Preserve cross-host redirect observation in source-health monitoring while still requiring
  the final destination to be public HTTPS.
- Preserve injected openers in source-health tests and close a response when redirect
  validation fails.
- Add negative tests proving unsafe initial URLs never reach the opener and unsafe or
  unapproved redirects fail closed.

The 44 focused monitor tests passed. A local Bandit 1.9.4 rescan of `scripts\`, excluding
the separately open B101 rule, returned no findings; the single urllib call carries a
targeted B310 suppression immediately after the explicit policy guard. The original raw
September 5 scanner artifact remains unchanged historical evidence.

Locally mitigated finding: `bandit:B310:scripts-check-official-study-guides:urlopen`.

## Batch 4 — durable source-health report contracts

Implementation and local verification complete on Python 3.13.14.

- Replace both production assertions in `check_source_health.py` with explicit mapping
  checks and precise `ValueError` diagnostics. The checks remain active under Python's
  optimized execution mode.
- Use guarded access for the report summary and findings so missing or wrong-shaped
  internal results fail at the reporting boundary.
- Add negative tests for both malformed structures.

The focused source-health tests and all 110 repository tests passed. Bandit 1.9.4 then scanned all production scripts
with no skipped rule and returned no findings. The test-loader assertions remain the
previously triaged non-production false-positive group; the historical scanner artifact
is unchanged.

Locally mitigated finding: `bandit:B101:scripts-check-source-health:assert`.

## Batch 5 — shared delivery gate and dependency governance

Implementation and local verification complete on Python 3.13.14.

- Replace the duplicated validation and Pages command sequences with one repository-local
  composite action. Workflow-specific triggers, permissions, Pages configuration, artifact
  upload, and deployment remain in their owning workflows.
- Add explicit Python setup and pinned dependency installation to the scheduled objective
  monitor so its full test-suite invocation is reproducible on a fresh runner.
- Pin every external action reference in all four workflows and the composite action to the
  exact commit behind its existing major tag. The tag-to-commit values were checked with
  read-only `git ls-remote` queries immediately before editing.
- Add weekly pip coverage to Dependabot alongside GitHub Actions, with Python updates grouped
  for one coherent compatibility review.
- Add three local contract tests that reject duplicated gate commands, mutable external action
  references, or loss of either dependency ecosystem.

All six workflow/action/dependency YAML files parsed locally. The three focused workflow tests
and repository validation passed. Remote Actions execution, branch protections, Dependabot
behavior, and Pages deployment remain provider-state evidence to confirm after push.

Locally mitigated finding:
`repository-health:ci:duplicated-validation-and-partial-update-coverage`.

## Batch 6 — canonical objective-adapter registry

Implementation and focused local verification complete on Python 3.13.14.

- Extract provider registration metadata and its consistency rules from the central validator
  and monitor into `scripts/objective_adapter_registry.py`.
- Require the monitor's implementation map to exactly equal the canonical registry at import
  time; missing and unregistered implementations now fail closed before any network request.
- Require all vendor assignments to use the canonical registry, require every registered
  adapter to have a vendor assignment, and validate the generated documentation block during
  normal repository validation.
- Replace the nine-entry documentation subset and obsolete “both” wording with the complete
  25-adapter inventory covering all 26 vendor catalog entries.
- Add focused regression tests for implementation mismatch and documentation/catalog drift.

The 64 focused adapter, monitor, and repository-validation tests passed, as did repository
validation. The historical finding snapshots remain unchanged.

Locally mitigated finding:
`repository-health:maintainability:automation-concentration`.

## Batch 7 — retained accessibility baseline

Automated and browser evidence is recorded in
`ADLC_Docs/quality/2026-09-06-accessibility-evidence.md`.

- Expand the generated-site validator from H1/skip-link coverage to document language and title,
  main landmarks, working skip targets, unique IDs, image alternatives, enabled form-control and
  button names, and table headers.
- Add a focused regression fixture that independently breaks each new structural rule.
- Validate all 290 generated HTML pages successfully.
- Use Microsoft Edge 152.0.4191.66 and browser device emulation to render the homepage, catalog,
  a short guide, and a long guide at 320, 768, 1024, and 1440 CSS pixels across light/dark
  preferences. All four reported exact requested widths, one main landmark, one H1, and no
  document-level horizontal overflow.

This is a **partial mitigation**, not closure of
`repository-health:accessibility:manual-evidence-gap`. NVDA was unavailable, and no human
keyboard, screen-reader, zoom, contrast, print, or reduced-motion session was performed. The
retained record labels every missing check explicitly rather than inferring conformance from
static or headless evidence.

### Best-effort evidence follow-up — SSH Direct

At the owner's direction, a September 6 network-enabled research pass expanded beyond
the earlier official-source-only scan. Twenty exact sources are now in the candidate
inbox: the initial seven plus thirteen distribution and upstream follow-up sources. A public
evidence/confidence/validation matrix was added at
`docs/SSH-DIRECT-EVIDENCE.md`. The AZ-800 and AZ-802 guides now explain the provisional
Hyper-V/VSOCK/OpenSSH model and a safe versioned validation plan. No candidate was
promoted, no lab was run, and neither blocked review nor historical audit result was
changed. The source gap is better bounded but remains open pending candidate review and
reproduction on a current supported host/guest combination or stronger Microsoft guidance.

The expanded page separates observations for Debian, Ubuntu, RHEL, CentOS Stream, Fedora,
SLES/openSUSE, and Oracle Linux into kernel transport, SSH/socket packaging, security
policy, and verified end-to-end behavior. The general source policy now states that
repository research and validation are always best effort: provide the strongest bounded
useful answer, document discrepancies and unavailable evidence, and retain the gap until
stronger evidence or reproducible validation resolves it. No distribution was marked
supported and no runtime result was inferred from component availability.

## Batch 8 — first guide-bound semantic audit

A same-context, read-only rubric-2 pass scrutinized complete current copies of four
risk-selected AWS guides: ANS-C01, MLA-C01, AIB-C01, and MLA-C02. Each result is bound to
the normalized guide-content SHA-256 and raw objective-snapshot SHA-256. The review checked
all ten required dimensions, including lifecycle contradictions, beta-versus-standard exam
contracts, lab safety, readiness prompts, review counts, and cross-guide contamination.

All four passed. ANS-C01 preserves AWS's current December 31 retirement date alongside the
older August 25 evidence; MLA-C01 and MLA-C02 distinguish the credential version from the
ME1-C02 beta appointment code; AIB-C01 separates strategic AWS awareness from the official
no-service-knowledge assessment boundary. The machine-readable evidence is in
`data/ai-audits.json`, and `docs/AI-AUDIT.md` records the resulting coverage.

This improves current semantic-assurance coverage but is **not** an independent review:
the auditor is explicitly recorded as `same-context`, and no human review occurred. The
high-severity independent-assurance concern therefore remains open. Four of 222 guides now
have current rubric-2 bindings; 216 more are preparation-ready and AZ-800/AZ-802 remain
source-gate blocked.

## Batch 9 — cross-vendor changing-credential audit

A second same-context, read-only rubric-2 pass reviewed CISM, PCEP-30-02, Terraform
Authoring and Operations Professional, and Fortinet NSE 8 against complete guides,
objective and status snapshots, catalog and seed rows, source-validation records,
registered source health, and current first-party evidence. CISM and PCEP-30-02 passed
all ten checks.

Terraform requires two repairs. HashiCorp's live catalog and learning collection now use
the **Terraform Authoring and Operations Advanced** title and `adv-*` canonical pages,
while the repository still presents Professional as current. The guide also incorrectly
says a refresh-only plan updates state; `plan -refresh-only` only proposes reconciliation,
and `apply -refresh-only` persists an accepted update.

NSE 8 also requires two repairs. Its high-level credential contract and safe lab model
are accurate, but the three elective sections mostly enumerate capabilities instead of
teaching the design, configuration, validation, troubleshooting, and failure-path depth
Fortinet says its practical exams assess. Separately, five cited shared Fortinet source
records omit NSE-8 from `supported_exams`, so the audit handoff exposes only ten of the
guide's 15 registered URLs even though the source-validation record correctly accounts
for all 15.

The exact evidence and four open findings are recorded in `data/ai-audits.json`. This
audit made no guide, catalog, snapshot, source, or review repair. Eight of 222 guides now
have current rubric-2 bindings: six pass and two require fixes. Of the remaining 214,
212 are preparation-ready and AZ-800/AZ-802 remain source-gate blocked. The same-context
disclosure remains explicit, so the independent-assurance concern is still open.

## Batch 10 — Terraform Advanced identity and state-semantics repair

The Terraform finding repair is complete. Public titles, the guide contract, certification
seed, inventory, and roadmap now use **Terraform Authoring and Operations Advanced** while
the existing long exam code, guide filename, source ids, review anchor, and objective
snapshot filenames remain as labeled stable identifiers. HashiCorp's rename announcement
is registered and cited: existing Professional holders transition automatically, and exam
content and lab-based format are unchanged.

Four redirected `pro-*` source records now use their canonical `adv-*` URLs. The rename
announcement and HCP Terraform changelog were promoted from the candidate inbox, giving
the guide 21 registered first-party links. All six changed or new pages returned HTTP 200
through the repository's public-HTTPS policy on September 6, and their health metadata is
retained. The corresponding freshness findings are marked applied with resolution evidence.

The guide now correctly explains that `terraform plan -refresh-only` previews proposed
state reconciliation and that `terraform apply -refresh-only` persists an accepted update.
The official-objective monitor regenerated the Advanced-titled snapshot and found no domain
or format delta. Repository validation reconciles its new hash and the refreshed source
review.

The original AI-audit finding remains open until a later semantic verification pass. Because
the guide and title-only snapshot changed, its September 6 audit result is historical and
the current rubric-2 binding count is seven; the guide has returned to the ready queue.

## Batch 11 — Fortinet NSE 8 elective-depth and source-association repair

The NSE 8 finding repair is complete. The Secure Networking, Application Security, and
Security Operations elective sections now turn each published domain into bounded design,
configuration, validation, troubleshooting, and failure-path guidance. The expanded guide
retains ten safe labs and now includes 52 original readiness checks. Unpublished or volatile
product placement, licensing, provider, protocol, and configuration details remain marked
**VERIFY CURRENT** rather than inferred.

Five shared Fortinet catalog records now associate their cited URLs with NSE-8. Current
FortiSandbox 5.2 documentation was promoted from the candidate inbox, cited as the
version-matched Application Security source, and returned HTTP 200 through the repository's
public-HTTPS policy on September 6. The refreshed source-validation record accounts for all
16 registered and reachable guide URLs. The consolidated official-objective snapshot is
unchanged because the reviewed Core and three elective contracts showed no objective delta.

The original two AI-audit findings remain open until a later semantic verification pass.
Because the guide changed, its September 6 result is historical; current rubric-2 coverage
is six guides. The default queue is 216 guides: 214 are preparation-ready and AZ-800/AZ-802
remain source-gate blocked.

## Batch 12 — diverse-provider semantic audit

A six-guide same-context, read-only rubric-2 batch moved the content-assurance wave beyond
Microsoft and GitHub. Terraform Advanced and Fortinet NSE 8 passed all ten checks and close
their four prior findings. PCEA-30-01 and CompTIA A+ Core 1 also passed. Google Professional
Agentic Architect and Cisco CCNA remain fix-required with five open findings.

Google's official page now says beta registration is open through September 30, and its FAQ
publishes the exam, result, practical-lab, and projected-GA windows. The guide still describes
registration as not open and does not substantively cover several explicitly in-scope data,
model-catalog, logging, monitoring, and tracing products. The source review overstates that
product coverage. CCNA still lacks current v1.1 depth for Layer 3 LACP EtherChannel,
security-program awareness/training/physical controls, and representative REST authentication
types; its source-review lab mappings remain materially inaccurate.

The machine-readable findings are retained in `data/ai-audits.json`. This batch is useful
same-context scrutiny, not independent or human assurance. Fourteen rubric-2 results have now
been recorded; 12 distinct guides have current bindings, 208 more are preparation-ready, and
AZ-800/AZ-802 remain source-gate blocked.

## Batch 13 — Google Agentic Architect and CCNA content repair

The five diverse-audit findings are repaired. The Google guide now records the open beta's
registration, multiple-choice, result, qualifying-lab, and projected-GA windows, retaining
**VERIFY CURRENT** around every scheduled milestone. It maps the blueprint-era Agent Designer
name to current Gemini Enterprise Workflow Builder and adds applied selection, control,
failure, and evidence boundaries for Cloud Storage, BigQuery, Cloud SQL, Firestore,
Memorystore for Redis, Model Garden, Cloud Logging, Monitoring, and Trace. Its evidence path
and readiness set now contain 42 original checks.

The CCNA guide now distinguishes Layer 2 from routed Layer 3 LACP EtherChannel and adds
configuration, state, member-failure, restoration, and simulator-substitute evidence. It
also distinguishes awareness, training, exercises, and physical controls, and compares
Basic, Bearer, API-key, and OAuth REST authentication without generalizing one Cisco API's
contract to all products. Source-review lab mappings now match labs 1–8.

Two Google lifecycle sources, seven direct Google product references, and three Cisco
references were registered and cited. All 12 returned HTTP 200 through the public-HTTPS
checker on September 6. Six queued freshness findings are marked applied; the separate
undated Cisco credential-page logistics conflict remains queued and visible. Google now
has 16/16 reachable cited URLs; CCNA has 13 cited URLs, with 11 reachable and two commercial
pages automation-blocked.

The five AI-audit findings remain open until a later semantic verification pass. Because
both guides changed, their audit results are historical; current rubric-2 coverage is ten
guides, 210 more are preparation-ready, and AZ-800/AZ-802 remain source-gate blocked.

## Batch 14 — Google Agentic Architect and CCNA semantic verification

A separate same-context, read-only rubric-2 pass checked the committed repaired guides
against their exact guide and objective hashes. Both guides pass all ten checks. The three
Google findings and two CCNA findings are now resolved with retained before/after evidence;
the original fix-required records remain historical rather than being overwritten.

The Google handoff contains all 16 registered sources with no blocker. The CCNA handoff
contains all 13 registered sources; its two existing commercial-page automation blocks are
visible and do not support the repaired claims. The undated Cisco credential-page logistics
conflict also remains queued for later reconciliation. This is AI same-context assurance,
not an independent or human review.

Sixteen rubric-2 results are now recorded. Twelve distinct guides have current passing
bindings, 208 more guides meet the audit-preparation prerequisite, and AZ-800/AZ-802 remain
source-gate blocked.

## Batch 15 — risk-ranked Fortinet MSSP and CompTIA audit

The next six preparation-ready non-Microsoft/GitHub guides received same-context, read-only
rubric-2 review. A+ Core 2, Cloud+, Network+, and Linux+ pass all ten checks. A live official
monitor check found their exam/objective contracts unchanged on September 6.

Security+ is fix-required because CompTIA replaced its estimated-2026 retirement statement
with exact dates: June 11, 2027 for English and August 13, 2027 for Japanese, Portuguese,
Spanish, and Thai. The guide, readiness answer, objective/status snapshots, and review still
contain the stale estimate.

Fortinet MSSP remains blocked for exam-alignment because the canonical page still publishes
no objectives or qualifying exam. Its transferable foundation remains useful and safe, but
three repairable issues were also confirmed: partial program-level contract evidence is not
reflected, the review invents one published scope group, and only four of ten cited sources
are associated in the guide-bound audit handoff. Eight traceable findings are open across
the batch; four Security+ records point to the same retirement change across its guide,
readiness, lifecycle, and review-evidence surfaces.

Twenty-two rubric-2 results are now recorded. Eighteen distinct guides have current bindings:
16 pass, one requires repair, and one is blocked. Another 202 guides meet the preparation
prerequisite; AZ-800/AZ-802 remain source-gate blocked.

## Batch 16 — Security+ lifecycle and Fortinet evidence repair

Security+ now uses CompTIA's exact language-specific 2027 retirement dates throughout the
guide, readiness answer, source record, objective/status snapshots, exam catalog, and
source-validation record. No successor identity or objectives are inferred. The live official
page returned HTTP 200 and the monitor produced the new objective/status hashes.

Fortinet MSSP now records the useful partial credential contract from two first-party program
pages: credential purpose, active NSE 4/5-or-6/7 prerequisites, one proctored MSSP exam,
two-year validity, and the bounded renewal route. The guide still makes no exam-coverage claim.
It adds the versioned FortiGate 7.6 MSSP SD-WAN reference as foundation only. All three promoted
sources returned HTTP 200. Six previously omitted cited-source associations were repaired, so
the guide's 13 links are registered and reachable. Its source-validation record is now honestly
blocked with zero published objective groups rather than calling publication state an objective.

The same three program/catalog/SD-WAN sources also apply to NSE 8. Its guide now records the
standard 200-point renewal route, cites credential-level pathway context, and uses the versioned
MSSP SD-WAN document only as bounded implementation evidence rather than practical-exam scope.
The source-validation record now accounts for all 19 cited links and 53 original checks.

Seven actionable AI-audit findings are repaired; the separate unpublished-objectives finding
remains open until Fortinet releases a blueprint. Because all three guide/evidence snapshots changed,
their audit results are historical pending semantic verification. Fifteen guides retain current
passing bindings; 204 more are preparation-ready, while AZ-800, AZ-802, and Fortinet MSSP are
source-gate blocked.

## Batch 17 — Security+ and Fortinet post-repair verification

A separate same-context, read-only rubric-2 review checked the three committed repaired
guides and their evidence bindings. Security+ passes all ten checks with exact retirement
dates, current snapshots, and an explicit unconfirmed-successor boundary. NSE 8 passes all
ten checks with its standard renewal route and shared program/SD-WAN sources kept separate
from the practical blueprint.

Fortinet MSSP closes the three repairable contract and review/source-metadata findings. It
remains blocked only because Fortinet still publishes no exam objectives, weights, version,
or scheduling contract. That is a useful retained gap rather than an inferred scope. The
batch closes seven findings and keeps one publication finding open.

Twenty-five rubric-2 results are now recorded. Eighteen distinct guides have current bindings:
17 pass and Fortinet MSSP is blocked. Another 202 unaudited guides meet the preparation
prerequisite; AZ-800 and AZ-802 are the unaudited source-gate blockers. MSSP remains listed
by the source gate because its review is blocked, while its current audit captures that state.
