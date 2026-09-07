# Official-source freshness scans

Source freshness is a discovery gate for official material that is not already
represented in the library. It complements two narrower deterministic checks:

- the objective monitor detects changes on configured blueprint pages; and
- the source-health monitor checks reachability and public metadata for registered
  URLs.

Neither existing monitor can discover a newly published documentation page,
release note, retirement notice, renamed feature, or replacement source. A
freshness scan searches for those external deltas and records review work without
silently changing a guide.

## Operating boundary

- Scan public, first-party vendor sources only. Do not use recalled questions,
  dumps, confidential training, customer information, or authenticated material.
  The preparer enforces public access, authority classes 1–3, and an official
  source type; paid, partner-restricted, third-party, and expert resources are
  excluded even if their existing catalog rank is unusually high.
- Run read-only discovery before repair. The scanning agent reports evidence; a
  separate review decides whether to queue, apply, dismiss, or block a finding.
- Complete that review in the same work wave when the evidence supports a bounded guide note
  with reasonable confidence. A queue is a short decision boundary, not a parking place for
  verified concerns that can already help a learner.
- Prefer vendor-sized batches of 10 guides and never exceed 12.
- Treat search snippets as discovery hints, never as evidence. Open the canonical
  official page before recording a finding.
- Do not infer product behavior from an exam blueprint or course landing page.
- Do not mark a guide community reviewed. An AI freshness scan is not human review.

## Required search channels

For every selected guide, inspect all applicable channels:

1. The official credential page and current exam blueprint, including effective
   dates, beta status, replacements, and retirement announcements.
2. Official product documentation for each volatile or weakly supported objective.
3. Official release notes, roadmaps, changelogs, retirement notices, and product
   announcements.
4. The current `data/sources.json` and `data/source-candidates.json` entries for
   the exam so existing evidence is not rediscovered as new.
5. The guide's `VERIFY CURRENT` boundaries and unresolved audit findings, looking
   specifically for newer first-party evidence or contradictions.

Record the exact canonical URL, visible title, dated change when the vendor
publishes one, affected exams, catalog status, evidence, confidence, and a bounded
recommended action. If the official source does not publish a date, say so rather
than guessing.

## Five required checks

Each result records `passed`, `finding`, `blocked`, or `not-applicable`, plus
evidence notes for:

1. **Official blueprint and lifecycle:** scope, effective dates, beta/GA state,
   replacement, and retirement signals.
2. **Official product documentation:** newly published or materially revised
   implementation evidence for tested capabilities.
3. **Official release channels:** relevant release notes, roadmaps, changelogs,
   retirement notices, and announcements.
4. **Catalog comparison:** every reported URL is compared with approved sources,
   healthy redirect/canonical aliases, and queued candidates.
5. **Contradiction and gap review:** newer evidence is checked against guide claims,
   `VERIFY CURRENT` statements, and unresolved audit findings.

## Outcomes and dispositions

- **current:** no review-gated or blocked findings remain. Historical findings may
  be retained as `applied` or `no-action` with a resolution.
- **review-required:** one or more findings are queued for source or guide review.
- **blocked:** an applicable official channel could not be checked reliably.

A `queued` finding must point to a candidate in `data/source-candidates.json`. An
`applied` finding must point to an approved source in `data/sources.json` and state
what was changed. `no-action` preserves useful evidence that did not warrant a
catalog or guide change. `blocked` records the exact access or evidence limitation.

A blocked official channel does not end the research pass. Check vendor-owned code, examples,
training, and announcements, then maintained upstream material, named experts, and independent
implementation reports under the source-quality hierarchy. Add the strongest useful provisional
model to the guide with a dated **Corroborated — verify current** or **Unconfirmed — validation
needed** label, exact citations, the unresolved official-evidence gap, and a safe recheck path.
The official freshness result remains blocked until that channel is auditable, even though the
guide has been improved.

## Preparing a scan

The preparer packages current exam metadata, the guide-bound source baseline,
official catalog entry points, registered first-party sources, health states, and
queued candidates. Explicit exam codes are useful for a curated wave:

```bash
python scripts/prepare_source_freshness_scan.py \
  --batch-id freshness-2026-09-05-github-microsoft-azure \
  --exam-code GH-100 --exam-code GH-200 --exam-code GH-500 --exam-code GH-900 \
  --exam-code AB-100 --exam-code AB-650 --exam-code AB-900 --exam-code MD-102 \
  --exam-code AI-103 --exam-code AZ-700 --exam-code AZ-800 --exam-code AZ-802 \
  --output .site-build/freshness-2026-09-05.json
```

For recurring work, omit the exam codes. The default queue selects up to ten
guides whose current baseline has never been scanned or was last scanned at least
seven days ago, ordered by lifecycle and source-volatility risk. Use
`--min-age-days` to change the cadence and `--vendor-id` to constrain a provider.

The baseline hash covers the current guide, exam lifecycle metadata, and registered
authority-class 1–3 sources. A relevant guide or official-source catalog change
makes the prior result ineligible as the current baseline. Time still matters:
unchanged local inputs become due again because the external web can change.
Completed batch hashes are immutable historical evidence: a later local change
makes that baseline due again, but does not invalidate the earlier record. Blocked
or future-dated results never suppress recurrence.

## Review and completion

1. Run the deterministic objective monitor for the selected exam codes.
2. Give the generated manifest and this rubric to a fresh-context agent.
3. Verify every reported change against the opened first-party page.
4. Add genuinely undecided discoveries to the candidate inbox. Otherwise evaluate and promote
   useful sources, add the bounded concern or provisional explanation to the living guide, and
   record the applied source/content change during the same repair wave.
5. Record the completed results in `data/source-freshness.json`; never delete an
   earlier finding to make the summary pass.
6. Run repository tests, source checks appropriate to changed URLs, and generated
   site validation before merging.

Run volatile GitHub, Microsoft 365, Copilot, Power Platform, and Azure batches
weekly. A monthly cadence is usually sufficient for slower, stable providers,
with an immediate manual scan after an official exam or product announcement.

## Initial GitHub and Microsoft/Azure scan

The September 5, 2026 baseline ran three independent, fresh-context agents across
all five existing GitHub guides and the eight recently repaired Microsoft
platform/Azure guides. A deterministic live check also confirmed that all 13
configured objective and status snapshots were unchanged.

| Batch | Exams | Current | Review required | Queued guide/source impacts | Applied findings |
|---|---:|---:|---:|---:|---:|
| GitHub | 5 | 1 | 4 | 15 | 3 |
| Microsoft platform | 4 | 0 | 4 | 10 | 2 |
| Azure | 4 | 0 | 4 | 8 | 0 |
| **Total** | **13** | **1** | **12** | **33** | **5** |

The applied findings correct GH-300's retired `github.com` Spark experience,
Copilot CLI/app content-exclusion support, and public-preview Copilot approvals,
recognize a redirected Copilot Studio source's canonical harness overview,
and synchronize AB-650's current Microsoft 365 and AI Services display name. The
candidate inbox contains 23 unique first-party URLs for separate relevance and
content review. That count is lower than 33 because a single source can affect
multiple guides.

The scan also found the official GH-600 study guide. It is queued without an exam
mapping because adding a new certification, objective snapshot, and substantive
guide is an expansion decision rather than a source-refresh side effect. No public
Microsoft implementation documentation for SSH Direct was found, so the existing
AZ-800 and AZ-802 evidence boundaries remain in place.

A separate September 6 best-effort follow-up expanded beyond the official-source-only
freshness boundary and found Microsoft-owned code, Microsoft Press, upstream packaging,
and expert evidence for a provisional Hyper-V/VSOCK/OpenSSH model. Those exact URLs are
queued as candidates and summarized in [SSH Direct evidence and validation boundary](SSH-DIRECT-EVIDENCE.md).
This does not rewrite the September 5 scan result or unblock source validation.
The same follow-up now includes separately bounded Debian, Ubuntu, RHEL, CentOS Stream,
Fedora, SLES/openSUSE, and Oracle Linux observations. Cross-family evidence is useful for
forming and testing the technical model, but it is not a substitute for an exact
host/guest/version result or a vendor support statement.

## Repository-wide freshness expansion

On September 7, 2026, the risk-ordered queue contained 192 current guide baselines
without an eligible rubric result. Batch 04 reviewed the first 12 guides against live
first-party blueprint, product-documentation, release, and catalog evidence.

| Batch | Exams | Current | Review required | Blocked | Queued findings | Applied findings revalidated | No action |
|---|---:|---:|---:|---:|---:|---:|---:|
| 04 | 12 | 5 | 5 | 2 | 17 | 26 | 1 |
| 05 | 12 | 9 | 3 | 0 | 13 | 1 | 0 |
| 06 | 12 | 10 | 2 | 0 | 6 | 0 | 3 |
| 07 | 12 | 12 | 0 | 0 | 0 | 0 | 5 |
| 08 | 3 | 3 | 0 | 0 | 0 | 0 | 3 |
| 09 | 4 | 4 | 0 | 0 | 0 | 0 | 0 |
| 10 | 5 | 5 | 0 | 0 | 0 | 0 | 0 |
| 11 | 5 | 5 | 0 | 0 | 0 | 0 | 0 |
| 12 | 11 | 11 | 0 | 0 | 0 | 0 | 10 |
| 13 | 6 | 6 | 0 | 0 | 0 | 0 | 6 |
| 14 | 12 | 12 | 0 | 0 | 0 | 0 | 12 |
| 15 | 5 | 5 | 0 | 0 | 0 | 0 | 5 |
| 16 | 12 | 12 | 0 | 0 | 0 | 0 | 1 |
| 17 | 10 | 10 | 0 | 0 | 0 | 0 | 0 |
| 18 | 3 | 3 | 0 | 0 | 0 | 0 | 3 |
| 19 | 6 | 6 | 0 | 0 | 0 | 0 | 5 |
| 20 | 4 | 4 | 0 | 0 | 0 | 0 | 3 |
| 21 | 8 | 8 | 0 | 0 | 0 | 0 | 8 |
| 22 | 7 | 7 | 0 | 0 | 0 | 0 | 5 |
| 23 | 7 | 7 | 0 | 0 | 0 | 0 | 4 |
| 24 | 6 | 6 | 0 | 0 | 0 | 0 | 1 |
| 25 | 11 | 11 | 0 | 0 | 0 | 0 | 21 |
| 26 | 9 | 8 | 1 | 0 | 1 | 0 | 0 |
| 27 | 7 | 6 | 0 | 1 | 0 | 1 | 0 |
| 28 | 6 | 1 | 0 | 5 | 0 | 5 | 0 |
| 29 | 10 | 7 | 0 | 3 | 0 | 3 | 3 |

The two blocked results are CISM's announced November 2026 outline, which is not yet
publicly available in sufficient detail, and Fortinet's MSSP credential, whose official
page still says only `Coming soon!`. Blocked results intentionally remain due. The other
ten results reduce the current-baseline queue to 182 guides. The no-action finding closes
the freshness discrepancy for the CCNA credential page: its formerly conflicting price
and language claims are no longer visible, so the current exam page remains authoritative.

Batch 05 covers 12 Microsoft guides. All live objective and status snapshots were
unchanged. AB-100, AB-620, and PL-900 retain review-required outcomes for 13 exact
first-party candidates covering the AI at Work roadmap transition, current Copilot
Studio harness documentation, Agent 365 lifecycle evidence, Power Platform
deprecations, and Microsoft 365 Copilot release notes. The other nine guides are
current. This reduces the current-baseline queue to 170 guides.

Batch 06 covers 12 more Microsoft guides. AB-410 and PL-300 retain six shared
roadmap, harness, and deprecation candidates; the other ten results are current.
Three deterministic monitor alerts were manually resolved as no-action extraction
drift: PL-300 and AB-730 changed wrapping or audience prose without changing domains,
weights, or tasks, while AB-410's extractor omitted its audience preamble but retained
the same objective groups and bullets. The current-baseline queue is now 158 guides.

Batch 07 covers 12 more Microsoft guides and found no actionable freshness gap.
Five raw monitor alerts were resolved as no-action representation drift after manual
comparison. AB-731 and AB-250 gained expanded audience or skills-at-a-glance rendering;
MB-230, MB-330, and MB-500 expanded previously condensed objective text. Their published
skill dates, domains, weights, and assessed tasks remain substantively unchanged. The
current-baseline queue is now 146 guides.

Batch 08 closes the remaining Microsoft provider queue with MB-310, MB-800, and
MB-820. Each raw monitor alert is a condensed-snapshot versus expanded-live-text
difference; the published skill date, domain weights, and assessed tasks are unchanged.
All three results are current, reducing the current-baseline queue to 143 guides.

Batch 09 covers CKAD, CKS, LFCA, and LFCS. All live objective and status checks
are unchanged. CKAD and CKS remain on Kubernetes v1.35, while the already registered
v1.37 release watch and Ingress NGINX controller-retirement boundary remain correctly
bounded. All four results are current, reducing the queue to 139 guides.

Batch 10 covers the five remaining CompTIA baselines: Cloud+, Network+,
Security+, Linux+, and Tech+. Their live exam versions, weighted domains, delivery
contracts, and published or estimated retirement watches are unchanged. All five
results are current, reducing the queue to 134 guides.

Batch 11 covers all five Red Hat guides. Their live objectives and product-version
contracts are unchanged: RHEL 10 for EX200, OpenShift 4.22 for EX280, OpenShift AI
3.3 with OpenShift 4.20 for EX267, Quarkus 3.8 for EX378, and the current purchasable
version boundary for EX294. EX280 still requires checking the assigned LMS version.
All five results are current, reducing the queue to 129 guides.

Batch 12 covers 11 Fortinet guides and excludes the same-day MSSP blocker. Ten
monitor alerts were resolved as no-action composite-extraction differences: the
entry guides combine credential and course evidence, solution tracks combine several
exam pages, and the SASE page lists its retiring 7.6 block before its current version
26 block. Manual review also confirmed that the announced FortiMail WorkSpace,
FortiVoice, FortiAnalyzer, FortiRecon, and FortiDeceptor pages still say `Coming soon!`.
The guides already preserve those gaps. All 11 results are current, reducing the queue
to 118 guides.

Batch 13 closes the six remaining publishable Fortinet tracks. Manual comparison
confirmed their live versions, delivery contracts, domains, and tasks; the monitor
hashes differ because its reduced extraction omits snapshot detail, and NSE 6 SASE
uses a composite three-exam snapshot. All six alerts are recorded as no-action
representation findings. The results are current, reducing the queue to 112 guides.

Batch 14 covers 12 Palo Alto Networks guides. The deterministic monitor cannot
parse the official PDF datasheets, and the concise Apprentice HTML objective falls
below its length threshold. Browser-visible first-party evidence still exposes the
expected credential identities, roles, and weighted blueprints; current source-health
records remain healthy and no lifecycle delta or contradiction was found. The 12
format-limit alerts are no-action findings. All results are current, reducing the queue
to 100 guides.

Batch 15 closes the remaining five Palo Alto Networks guides. Their current
first-party PDF datasheets remain browser-readable and aligned with the guide-bound
roles and weighted blueprints, while the HTML-oriented monitor reports format errors.
Those five errors are recorded as no-action format-limit findings. All results are
current, reducing the queue to 95 guides.

Batch 16 covers all 12 Oracle guides. Eleven extracted objective and status pairs
are unchanged. Java 1Z0-830 adds introductory, audience, and closing preparation
prose while preserving its Java SE 21 objectives, exam code, and 120-minute contract;
that alert is a no-action content-boundary finding. All results are current, reducing
the queue to 83 guides.

Batch 17 covers the ten remaining AWS baselines. Every live AWS exam guide matches
the committed credential identity, objective domains, weights, and status snapshot.
No replacement, retirement, contradictory service boundary, or uncataloged first-party
source was identified. All ten results are current. A complete baseline-hash recount
after this batch found 85 guides still due, not 73: the earlier running subtraction
did not account for 12 baselines invalidated by intervening guide or source-catalog
changes.

Batch 18 covers Cisco 100-150, 100-160, and 200-901. The two CCST objective hashes
are unchanged; their alerts only initialize previously absent delivery-status hashes.
The CCNAAUTO landing-page extraction changed with Cisco's credential rename, but the
guide already uses the detailed official v1.1 blueprint and records the landing page's
v1.0 label as a first-party discrepancy. All three alerts are no-action findings and
all results are current, reducing the recomputed queue to 82 guides.

Batch 19 covers all six C and C++ Institute guides. CPE-20-01 is unchanged. Five
other live pages expose expanded instructional wording where the committed snapshots
use concise paraphrases, while preserving the same active exam codes, July 2025
alignment dates, block weights, topic order, and numbered objectives. Manual
objective-by-objective comparison found no scope or lifecycle delta, so those alerts
are no-action representation findings. All six results are current, reducing the
queue to 76 guides.

Batch 20 covers all four JS Institute guides. JSE-40-01 is unchanged. The other
three live pages now label their detailed objective section `Exam Syllabus Contents`,
while the HTML adapter still expects the former `Exam Scope` heading. Manual extraction
confirmed the active codes, block weights, objective counts, and detailed topics match
the normalized guide snapshots. The three errors are no-action adapter-limit findings;
all four results are current, reducing the queue to 72 guides.

Batch 21 covers the eight remaining Python Institute guides. Six live pages expose
full provider wording where committed snapshots use normalized paraphrases; their
codes, status, update dates, block weights, item counts, and topics remain aligned.
PCET-30-01 and PCAT-31-01 remain browser-readable, but their pages no longer expose
the download marker used as the monitor's end boundary. Manual extraction found no
content delta. The PCAP, PCPP1, and PCAT successor watches remain disclosed in their
guides with no newer effective scope. All eight alerts are no-action findings and all
results are current, reducing the queue to 64 guides.

Batch 22 covers the seven remaining Google Cloud guides. Cloud Digital Leader and
Generative AI Leader are unchanged. The other five objective hashes are also unchanged;
their alerts initialize previously absent delivery-status snapshots. Existing branding
notices for Associate Cloud Engineer, Professional Cloud Architect, and Professional
Machine Learning Engineer are already explicitly disclosed in the guides, including
the Gemini Enterprise transition where applicable. The five alerts are no-action
baseline findings. All seven results are current, reducing the queue to 57 guides.

Batch 23 covers all seven Databricks guides. Five objective/status pairs are unchanged.
The Generative AI Engineer alert is only hyphen-to-en-dash typography plus status
initialization, and the Apache Spark Associate alert only initializes status. A blocked
historical Spark 3.0 community notice and a blocked supporting MLflow Optuna tutorial
are recorded separately; accessible current blueprints and adjacent official product
documentation still support both assessments. These four items are no-action findings.
All seven results are current, reducing the queue to 50 guides.

Batch 24 covers all six IBM guides. Five objective/status pairs are unchanged.
C1000-185 differs by one trailing space after its title; every status, delivery,
weighted-section, and objective line remains identical. That alert is a no-action
whitespace finding. All six results are current, reducing the queue to 44 guides.

Batch 25 covers all 11 Splunk guides. SPLK-5001's live HTML objective and status
snapshots are unchanged. The other ten official blueprints are PDFs that the HTML
monitor cannot parse; local extraction with the already-installed PDF reader confirmed
every live weighted-domain sequence exactly matches its committed snapshot. Each guide
also has one or more supporting Splunk Help or community URLs that block automated
health access. The ten format limits and 11 grouped supporting-access limits are
recorded as 21 no-action findings, while accessible blueprint and credential evidence
supports every assessment. All 11 results are current, reducing the queue to 33 guides.

Batch 26 covers GH-100, three HashiCorp guides, and five Microsoft Office guides.
Eight objective/status pairs are unchanged. The Vault Operations page is readable and
its 130 objective lines are unchanged, but HashiCorp now labels the credential Vault
Operations Advanced instead of Vault Operations Professional. That real title conflict
is queued against the official certification catalog for separate metadata, guide, and
adapter review; it was not silently repaired during discovery. Eight results are current
and one is review-required, reducing the rubric queue to 24 guides.

Batch 27 covers four ISC2 and three ISACA guides. The four ISC2 outlines and the
CISA and CRISC outlines are unchanged. CISM's current four-domain outline is also
unchanged and still announces a November 3, 2026 update, but its official update URL
continues to return only a JavaScript application shell without auditable future
domains, weights, or objectives. That known limitation remains blocked rather than
being guessed. Six results are current, reducing the queue to 18; CISM remains due.

Batch 28 covers four Salesforce and two ServiceNow guides. The Salesforce Platform
Administrator Trailhead objective and maintenance snapshots are unchanged. The other
three Salesforce Help pages return only `Loading` and a CSS error, while both ServiceNow
pages return only a title plus `Loading...` to the deterministic and available browser
checks. HTTP success alone is insufficient to claim their weighted blueprints are
unchanged, so all five are explicitly blocked. One result is current, reducing the
queue to 17; the five blocked results intentionally remain due.

Batch 29 covers four Snowflake, three MongoDB, and three NVIDIA guides. NVIDIA's
three objective/status pairs are unchanged. Three active Snowflake objective hashes
are unchanged and only initialize status; retired SOL-C01 remains correctly bound to
its registered retirement and COF-C03 replacement evidence. The three MongoDB
University study-guide and credential URLs resolve only to a generic client-rendered
course shell, so current weighted scope cannot be re-audited and those results are
blocked. Seven results are current, reducing the queue to 10; the three MongoDB
results intentionally remain due.

The September 7 closeout recomputed every baseline hash rather than relying on the
running subtraction. Before remediation, all 222 guides had a rubric result for their
current local baseline: 188 current, 24 review-required, 10 blocked, and zero missing.

Batch 30 revisits the four AWS review-required guides under the living-guide rule.
Nine official candidates were promoted and health checked. Ten per-guide findings
were applied across AIB-C01, ANS-C01, MLA-C01, and MLA-C02: exact AI Business
Strategist scope/exclusion appendices; Transit Gateway policy-based routing and its
Reachability Analyzer boundary; the MLA-C01/C02 January 14, 2027 transition; and
SageMaker monitoring availability changes. Each guide now separates confirmed facts,
useful adjacent product context, and the concern that still needs rechecking. All four
results are current, leaving 192 current, 20 review-required, 10 blocked, and zero
missing on the post-batch baseline. The blocked results remain visible even when
supplementary evidence improves their guides.

Batch 31 applies the same rule to GitHub. Seven official changelog sources were
promoted and health checked, and 13 per-guide findings were applied across GH-100,
GH-200, GH-300, and GH-500. The guides now cover the September runner and Node
deadlines, expanded Actions retention, reusable-workflow identity and least-privilege
permissions, Copilot policy/retention/billing and model changes, and CodeQL 2.26.4.
Each note distinguishes durable governance or security lessons from volatile release
details and from the unchanged exam blueprints. The three review-required guides are
now current, leaving 195 current, 17 review-required, 10 blocked, and zero missing.

Batch 32 resolves HashiCorp's Vault Operations credential rename. The official
catalog, exam-content page, learning path, and orientation now consistently say Vault
Operations Advanced; a validated comparison found all 130 objective lines unchanged
apart from the title. Display metadata and canonical URLs now use Advanced, while the
stable internal `VAULT-OPERATIONS-PROFESSIONAL` identifier is retained and explicitly
documented because HashiCorp has not published an unambiguous replacement exam code.
The result is current, leaving 196 current, 16 review-required, 10 blocked, and zero
missing.

Batch 33 reviews 12 Microsoft platform, Azure AI, endpoint, administration, and Power
Platform guides under the living-guide rule. Seventeen queued first-party sources were
promoted and health checked, including the AI at Work transition, Copilot and product
release feeds, Agent 365 GA, Power Platform and Dynamics deprecations, Intune changes,
Entra/Defender/Purview feeds, Content Understanding changes, and AI-500 lifecycle and
migration evidence. Each guide now records the concern and distinguishes blueprint
scope from roadmap estimates, preview/GA state, staged rollout, retired behavior, and
independent learning aids. AB-620's obsolete two-experience table was replaced with
the current three-harness model. All 12 results are current, leaving 208 current, four
review-required, 10 blocked, and zero missing.

Batch 34 reviews the four remaining Azure and Windows Server freshness results. Twenty-seven
first-party, distribution, upstream, book, expert, and community sources were registered and
health checked. AZ-700 now distinguishes current virtual network flow logs from retiring NSG
flow logs and labels agentless Connection troubleshoot preview. AZ-801 separates unaffected
VM Insights performance monitoring from the retiring Map and Dependency Agent. AZ-800 and
AZ-802 teach a cited provisional SSH Direct model across Debian/Ubuntu, Red Hat-family,
SUSE/openSUSE, Oracle Linux, systemd, and libvirt while retaining the missing Microsoft
end-to-end contract and compatibility matrix as a human-review concern. All four freshness
results are current, leaving 212 current, zero review-required, 10 blocked, and zero missing.
