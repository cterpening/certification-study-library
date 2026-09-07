# Independent AI guide audits

This workflow adds an adversarial semantic review layer to the library. It complements deterministic repository validation and the AI-assisted source-validation gate; it does not replace either one and never counts as human or community review.

## Non-negotiable boundaries

- The audit pass is **read-only**. It reports findings and does not edit guides, catalogs, snapshots, sources, or review evidence.
- Use a fresh-context agent when available. The agent should not rely on the conversation or assumptions that produced the guide.
- Bind every new result to the guide-content SHA-256, exact official-objective snapshot SHA-256 and rubric version. A changed guide, snapshot or rubric makes the previous result historical and the guide eligible for another audit.
- Use public sources only. Never seek or use recalled questions, dumps, confidential training, employer/customer information, or exam-session material.
- Do not change `review_status` to `community-reviewed`. An AI-audited guide remains human-review pending unless a qualifying contributor review is separately recorded.
- Keep batches small enough for close reading. The default is 10 guides and the hard operational recommendation is no more than 12.

## Audit inputs

For each guide, read all of the following rather than sampling isolated paragraphs:

1. The guide and its front matter.
2. The current official-objective snapshot and the official-status snapshot when that provider adapter emits one.
3. The current exam-catalog row and certification seed.
4. The latest source-validation record.
5. Every registered source cited by the guide and its source-health record.
6. Relevant current first-party documentation when a technical claim cannot be confirmed from the registered sources.

The batch preparer emits these paths and source identities. A source-health `ok` result proves reachability and captured metadata, not that the page supports a particular claim.

## Content binding and rubric versions

Rubric 2, active from September 6, 2026, keeps the same ten checks and adds required
`guide_content_sha256` evidence to every result. Copy the hash from the handoff manifest
only after confirming that the guide being read is still that version. The hash is
SHA-256 of the complete UTF-8 guide text after CRLF/CR newlines are normalized to LF;
all other text, whitespace and front matter are preserved. Platform-only newline
conversion does not force a new audit. Objective snapshots retain their raw-byte hashes.

If a guide changes during the audit, regenerate its manifest and review the changed
content before completing the result. Retain the hash of the actually reviewed content,
not a newly computed hash added later merely to make an old result look current.

Rubric-1 batches remain valid historical records without guide hashes. Do not backfill
them: the recorded evidence does not establish the precise guide content reviewed.
They no longer suppress the default audit queue. A historical guide-hash mismatch is
not a corrupt ledger; it means the current guide needs a new audit.

## Ten required checks

Each result records `passed`, `failed`, `blocked`, or `not-applicable` plus concise evidence for every check.

1. **Official scope:** The guide names the correct credential/version and accurately represents every published domain or capability group.
2. **Objective coverage:** Coverage is substantive and findable; a heading or keyword alone is not sufficient.
3. **Material claim support:** Assessment claims use the official contract. Product-behavior
   claims use current first-party documentation or evaluated, cited supplementary evidence whose
   non-vendor authority and confirmation gap are labeled next to the claim.
4. **Exam-contract integrity:** The guide does not invent weights, question counts, scores, prerequisites, delivery details, or lifecycle dates.
5. **Technical coherence:** Explanations, comparisons, failure modes, scenarios, and answer guidance are internally consistent and technically defensible.
6. **Volatility and lifecycle:** Preview, beta, changing, retiring, provider-inconsistent, regional, licensing, version, and UI-sensitive material is visibly bounded.
7. **Lab safety and feasibility:** Labs are authorized, reversible or recoverable, scoped, observable, and possible with the stated access model or substitute.
8. **Readiness-check quality:** Questions are original, aligned, unambiguous enough for study, and consistent with their answer guide.
9. **Review-evidence accuracy:** Objective mappings, source counts, health counts, dates, hashes, and review notes do not overstate what the repository proves.
10. **Duplication and contamination:** The guide has no irrelevant copied passages, vendor/product leakage, contradictory templates, or suspicious overlap with another guide.

## Findings and severity

Every finding names the exact check it affects. Every failed or blocked check needs at least one open finding with a precise location, evidence, recommendation, and disposition.

| Severity | Meaning |
|---|---|
| Critical | Unsafe instruction, exam-integrity breach, or content likely to cause severe harm |
| High | Wrong credential/scope or a major technical error affecting preparation or operations |
| Medium | Material omission, unsupported claim, stale behavior, or misleading exercise/answer |
| Low | Local ambiguity, minor evidence weakness, small inconsistency, or maintainability problem |
| Info | Useful observation that does not currently require a correction |

`open` means no repair decision has been recorded. `resolved` requires a later repair and verification note. `accepted-risk` requires an explicit rationale. `dismissed` requires evidence that the finding was invalid. The audit agent must not mark its own finding resolved during the read-only pass.

## Verdict rules

- **pass:** all applicable checks passed and there are no open findings.
- **pass-with-notes:** all applicable checks passed; only open `info` or `low` observations remain.
- **fix-required:** a check failed or an open `medium`, `high`, or `critical` finding exists.
- **blocked:** at least one required check could not be completed because authoritative evidence or access was unavailable.

Fixes happen in a separate change. Re-run deterministic validation and use a fresh audit pass to verify repairs. Never silently delete a finding.

## Batch strategy

The default queue includes every guide that lacks a completed, guide-bound audit for its current guide hash, blueprint hash and rubric version. Completion does not imply a passing verdict; use explicit exam codes to revisit unresolved findings even when the content is unchanged. Risk ordering is deterministic:

1. Changing, beta, retiring, or retired records.
2. Scheduled blueprint/lifecycle changes.
3. Broken, missing, or automation-blocked cited sources.
4. Visible `VERIFY CURRENT` markers and recent blueprint dates.
5. Vendor and natural exam-code order as stable tie breakers.

Use explicit exam codes for a curated pilot or repair-verification batch. Across the full library, prefer coherent provider batches with occasional cross-vendor samples to detect systemic template or catalog problems.

A current passed source-validation review remains a prerequisite for preparing a guide.
Default manifests list guides that do not meet that prerequisite in `blocked_items`,
with their paths and reasons, while continuing to prepare ready guides. Always inspect
both `items` and `blocked_items`; an empty `items` list is not proof of complete coverage
when blockers remain. Explicitly requesting a blocked guide fails without bypassing the gate.

Generate a default next batch:

```bash
python scripts/prepare_ai_audit_batch.py --batch-id audit-2026-09-04-01 --size 10
```

Generate an explicit pilot:

```bash
python scripts/prepare_ai_audit_batch.py \
  --batch-id pilot-2026-09-04 \
  --exam-code 1Z0-997-26 \
  --exam-code GOOGLE-PROFESSIONAL-AGENTIC-ARCHITECT
```

Use `--output <path>` when a durable handoff manifest is useful. Generated manifests are working material; only completed, scrutinized results belong in `data/ai-audits.json`.

## Historical completed coverage

### Pilot baseline

The September 4, 2026 fresh-context pilot audited five newly added Advanced OCI guides and five older higher-risk guides. It produced six passes, three fix-required verdicts, one blocked verdict, and eight open findings. The read-only pass made no guide or review repairs.

| Guide | Verdict | Open findings |
|---|---|---:|
| 1Z0-997-26 | Fix required | 1 |
| 1Z0-1084-26 | Pass | 0 |
| 1Z0-1109-26 | Pass | 0 |
| 1Z0-1124-26 | Pass | 0 |
| 1Z0-1111-26 | Pass | 0 |
| Google Professional Agentic Architect | Fix required | 3 |
| Fortinet Industry MSSP Security | Blocked | 2 |
| CISM | Pass | 0 |
| PCEA-30-01 | Pass | 0 |
| 200-301 CCNA | Fix required | 2 |

The exact per-check evidence and finding dispositions are in the [machine-readable audit catalog](https://github.com/cterpening/certification-study-library/blob/main/data/ai-audits.json).

### GitHub and Microsoft/Azure wave

The September 4, 2026 follow-up audited every published GitHub guide plus 24 risk-selected Microsoft platform and Azure guides. The three fresh-context, read-only batches produced 17 passes, 11 fix-required verdicts, one blocked verdict, and 24 open findings.

| Batch | Guides | Pass | Fix required | Blocked | Open findings |
|---|---:|---:|---:|---:|---:|
| GitHub certification family | 5 | 1 | 4 | 0 | 6 |
| Microsoft platform | 12 | 8 | 4 | 0 | 9 |
| Microsoft Azure | 12 | 8 | 3 | 1 | 9 |
| **Follow-up total** | **29** | **17** | **11** | **1** | **24** |

### Repair revalidation

On September 5, the 11 fix-required guides and the blocked AZ-802 guide entered a separate repair pass, followed by cross-assigned fresh-context, read-only verification. The repair closed 22 of the 24 findings. GitHub and Microsoft platform repairs passed in full; AZ-700 and AI-103 passed after repair. One SSH Direct coverage finding remains open in each of AZ-800 and AZ-802 because the blueprints name the capability but Microsoft has not published the implementation contract needed for substantive teaching.

| Batch | Guides | Pass | Fix required | Blocked | Open findings | Closed findings |
|---|---:|---:|---:|---:|---:|---:|
| GitHub certification family | 5 | 5 | 0 | 0 | 0 | 6 |
| Microsoft platform | 12 | 12 | 0 | 0 | 0 | 9 |
| Microsoft Azure | 12 | 10 | 1 | 1 | 2 | 7 |
| **Follow-up current state** | **29** | **27** | **1** | **1** | **2** | **22** |

Across both historical waves, the catalog contains completed results for 39 of 222 published guides: 33 pass, four require fixes, two are blocked, ten findings remain open, and 22 findings are resolved. These rubric-1 results are not proof of current guide-content coverage and remain historical rather than being backfilled.

### Rubric-2 guide-bound coverage

On September 6, multiple rubric-2 batches bound complete-guide review to exact guide and objective hashes. The AWS lifecycle guides all passed. In the first cross-vendor batch, CISM and PCEP-30-02 passed while Terraform and NSE-8 required four repairs. Later diverse-provider batches verified those repairs, passed PCEA-30-01, both A+ cores, Cloud+, Network+, and Linux+, and closed five Google Agentic Architect and CCNA findings. Later verification passes repaired Security+ and shared-source-aligned NSE-8, closed three actionable Fortinet MSSP findings while retaining its objective-publication blocker, and passed expanded CKA and CKAD. Subsequent groups covered CKS, Red Hat, Splunk, Snowflake, Python Institute, expanded AB-100, the next risk-ranked Microsoft/Fortinet guides, a full-input JavaScript, MongoDB, Palo Alto, Salesforce, ServiceNow, and Snowflake batch, a full-input Splunk, CompTIA, Red Hat, and Microsoft batch, a full-input AWS, Microsoft, GitHub, and Databricks batch, a full-input Microsoft, Cisco, Fortinet, and Google Cloud batch, and a full-input ISACA, ISC2, NVIDIA, and Palo Alto batch. On September 7, the next full-input risk-ranked group covered Python AI, security and testing, Salesforce Agentforce and platform development, Splunk observability metrics, Databricks data engineering, LFCS, and Dynamics 365 Customer Service. A second September 7 group covered Dynamics 365 Finance and Business Central development, GitHub enterprise administration and Advanced Security, Vault operations, and five Oracle database, Java, architecture, and operations credentials. A third group covered seven additional Oracle Cloud credentials plus AB-250, Vault Associate, and IBM QRadar; it found an unsupported Oracle delivery-mode claim and the same overstatement in its rendered review evidence. A fourth group passed five more IBM credentials and all five current Microsoft Office Specialist Word, Excel, and PowerPoint guides. A fifth group reviewed eight Fortinet tracks plus NVIDIA AI Operations and Palo Alto Network Security Analyst; guide content passed, while nine guides received low-severity notes because shared cited sources lack exact supported-exam associations in the generated audit handoff. A sixth group passed Palo Alto Network Security Professional and Python Institute PCAD, while eight more Palo Alto engineering and architecture guides received the same low-severity shared-source association note. A seventh group passed the final three source-ready guides: Python Institute PCED, Snowflake Gen AI, and Linux Foundation LFCA. One repair-verification group then passed corrected Oracle Foundations, GitHub Enterprise Administration, and eight Fortinet guides, closing eleven findings. A final Palo Alto repair-verification group passed nine guides and closed all nine remaining shared-source association findings. After the living-guide source refresh invalidated 33 bindings, the first semantic-refresh batch rechecked ANS-C01, AZ-801, MS-102, MLA-C01, CISM, AIB-C01, MLA-C02, AI-500, AB-210, AB-650, AB-100, and AB-900; all twelve passed, including the new lifecycle and best-effort caveats. The second batch passed AZ-700, MD-102, PL-300, the three MongoDB guides, ServiceNow CAD and CSA, AB-620, PL-900, GH-300, and AI-103 while retaining explicit vendor-access limitations instead of promoting adjacent material to official scope. The final source-ready batch passed GH-200, AB-410, three Salesforce guides, GH-100, GH-500, Vault Operations Advanced, and Vault Associate; it verified the Salesforce source repairs and the Vault Professional-to-Advanced rename. The auditor disclosure is **same-context**, not fresh-context, so this is useful current semantic coverage but does not close the repository's independent-assurance finding or count as human review.

| Batch | Guides | Pass | Fix required | Blocked | Open findings | Independence |
|---|---:|---:|---:|---:|---:|---|
| AWS lifecycle and beta | 4 | 4 | 0 | 0 | 0 | Same context |
| Cross-vendor changing credentials | 4 | 2 | 2 | 0 | 4 | Same context |
| Diverse-provider verification and audit | 6 | 4 | 2 | 0 | 5 open / 4 closed | Same context |
| Google Agentic Architect and CCNA verification | 2 | 2 | 0 | 0 | 0 open / 5 closed | Same context |
| Fortinet MSSP and CompTIA risk batch | 6 | 4 | 1 | 1 | 8 open / 0 closed | Same context |
| Security+ and Fortinet verification | 3 | 2 | 0 | 1 | 1 open / 7 closed | Same context |
| CKA and CKAD verification | 2 | 2 | 0 | 0 | 0 open / 0 closed | Same context |
| CKS, Red Hat, Splunk, and Snowflake | 4 | 3 | 0 | 0 | 1 open / 0 closed | Same context |
| CKS lifecycle verification | 1 | 1 | 0 | 0 | 0 open / 1 closed | Same context |
| Python Institute, Splunk, and Red Hat | 6 | 5 | 1 | 0 | 2 open / 0 closed | Same context |
| PCPP-32-101 repair verification | 1 | 1 | 0 | 0 | 0 open / 2 closed | Same context |
| AB-100 post-expansion verification | 1 | 1 | 0 | 0 | 0 open / 0 closed | Same context |
| Risk-ranked Microsoft and Fortinet | 6 | 6 | 0 | 0 | 0 open / 0 closed | Same context |
| Risk-ranked Fortinet, Python, Microsoft, and AWS | 10 | 10 | 0 | 0 | 0 open / 0 closed | Same context |
| Risk-ranked Splunk, security, data, and Microsoft | 10 | 10 | 0 | 0 | 0 open / 0 closed | Same context |
| Risk-ranked AWS, Microsoft, GitHub, Red Hat, and C | 10 | 10 | 0 | 0 | 0 open / 0 closed | Same context |
| Risk-ranked MongoDB, ServiceNow, Splunk, Databricks, and Microsoft | 10 | 10 | 0 | 0 | 0 open / 0 closed | Same context |
| Risk-ranked AWS, Microsoft, GitHub, and HashiCorp | 10 | 10 | 0 | 0 | 0 open / 0 closed | Same context |
| Risk-ranked Microsoft, Google Cloud, Databricks, and AWS | 10 | 10 | 0 | 0 | 0 open / 0 closed | Same context |
| Risk-ranked Cisco, C/C++, Fortinet, ISACA, and ISC2 | 10 | 10 | 0 | 0 | 0 open / 0 closed | Same context |
| Risk-ranked JavaScript, MongoDB, Palo Alto, Salesforce, ServiceNow, and Snowflake | 10 | 10 | 0 | 0 | 0 open / 0 closed | Same context |
| Risk-ranked Splunk, CompTIA, Red Hat, and Microsoft | 10 | 10 | 0 | 0 | 0 open / 0 closed | Same context |
| Risk-ranked AWS, Microsoft, GitHub, and Databricks | 10 | 10 | 0 | 0 | 0 open / 0 closed | Same context |
| Risk-ranked Microsoft, Cisco, Fortinet, and Google Cloud | 10 | 10 | 0 | 0 | 0 open / 0 closed | Same context |
| Risk-ranked ISACA, ISC2, NVIDIA, and Palo Alto | 10 | 10 | 0 | 0 | 0 open / 0 closed | Same context |
| Risk-ranked Python, Salesforce, Splunk, Databricks, Linux, and Microsoft | 10 | 10 | 0 | 0 | 0 open / 0 closed | Same context |
| Risk-ranked Microsoft, GitHub, HashiCorp, and Oracle | 10 | 9 | 0 | 0 | 1 open / 0 closed | Same context |
| Risk-ranked Oracle, Microsoft, HashiCorp, and IBM | 10 | 9 | 1 | 0 | 2 open / 0 closed | Same context |
| Risk-ranked IBM and Microsoft Office | 10 | 10 | 0 | 0 | 0 open / 0 closed | Same context |
| Risk-ranked Fortinet, NVIDIA, and Palo Alto Networks | 10 | 1 | 0 | 0 | 9 open / 0 closed | Same context |
| Risk-ranked Palo Alto Networks and Python Institute | 10 | 2 | 0 | 0 | 8 open / 0 closed | Same context |
| Final source-ready Python, Snowflake, and Linux | 3 | 3 | 0 | 0 | 0 open / 0 closed | Same context |
| Oracle, GitHub, and Fortinet repair verification | 10 | 10 | 0 | 0 | 0 open / 11 closed | Same context |
| Palo Alto repair verification | 9 | 9 | 0 | 0 | 0 open / 9 closed | Same context |
| Living-guide semantic refresh 1 | 12 | 12 | 0 | 0 | 0 open / 0 closed | Same context |
| Living-guide semantic refresh 2 | 12 | 12 | 0 | 0 | 0 open / 0 closed | Same context |
| Living-guide semantic refresh 3 | 9 | 9 | 0 | 0 | 0 open / 0 closed | Same context |
| **Recorded rubric-2 results** | **281** | **253** | **7** | **2** | **41 open / 39 closed** | **Same context** |

The original Terraform, Google Professional Agentic Architect, CCNA, Security+, Fortinet MSSP, NSE-8, CKS, PCPP-32-101, AB-100, and Oracle Foundations results remain historical where their bound guides changed. Their repaired or expanded versions now have current results: Security+, NSE-8, CKA, CKAD, CKS, PCPP-32-101, AB-100, Oracle Foundations, GitHub Enterprise Administration, and the repaired Fortinet and Palo Alto guides pass, while MSSP remains blocked only by its unpublished objective blueprint. Current rubric-2 coverage is 219 guides and all 219 pass; no source-ready guide remains audit-due. AZ-800, AZ-802, and MSSP remain outside the default audit queue because they do not have a current passed source-validation review; MSSP's earlier blocked audit is now historical because its guide changed. A guide or objective change makes a completed result historical and returns that guide to the queue. Completed batches do not invalidate or erase earlier findings.

## Completion and reporting

A completed batch must include exactly one result per selected exam, a summary matching the results and finding dispositions, a completion date, and an AI-audit disclosure. New batches use rubric 2 and every result must include `guide_content_sha256`. `closed_findings` counts resolved, accepted-risk, and dismissed findings; none of those dispositions may omit its rationale. Repository validation rejects missing/malformed rubric-2 guide hashes, stale blueprint hashes, wrong guide/vendor paths, duplicate codes or findings, inconsistent verdicts, incomplete checks, and incorrect summaries.

Report AI-audit coverage separately from source validation and human review. “Audited” means checked against this rubric at a particular snapshot; it is not a guarantee of correctness.
