# Independent AI guide audits

This workflow adds an adversarial semantic review layer to the library. It complements deterministic repository validation and the AI-assisted source-validation gate; it does not replace either one and never counts as human or community review.

## Non-negotiable boundaries

- The audit pass is **read-only**. It reports findings and does not edit guides, catalogs, snapshots, sources, or review evidence.
- Use a fresh-context agent when available. The agent should not rely on the conversation or assumptions that produced the guide.
- Bind every result to the exact official-objective snapshot SHA-256 and rubric version. A changed snapshot makes the previous result historical and the guide eligible for another audit.
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

## Ten required checks

Each result records `passed`, `failed`, `blocked`, or `not-applicable` plus concise evidence for every check.

1. **Official scope:** The guide names the correct credential/version and accurately represents every published domain or capability group.
2. **Objective coverage:** Coverage is substantive and findable; a heading or keyword alone is not sufficient.
3. **Material claim support:** Assessment and product-behavior claims are supported by the cited sources or current first-party documentation.
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

The default queue includes every guide that lacks a completed audit for its current blueprint hash and rubric version. Risk ordering is deterministic:

1. Changing, beta, retiring, or retired records.
2. Scheduled blueprint/lifecycle changes.
3. Broken, missing, or automation-blocked cited sources.
4. Visible `VERIFY CURRENT` markers and recent blueprint dates.
5. Vendor and natural exam-code order as stable tie breakers.

Use explicit exam codes for a curated pilot or repair-verification batch. Across the full library, prefer coherent provider batches with occasional cross-vendor samples to detect systemic template or catalog problems.

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

## Completed coverage

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

Across both waves, the catalog now contains completed results for 39 of 222 published guides: 23 pass, 14 require fixes, two are blocked, and 32 findings remain open. Coverage is snapshot- and rubric-specific rather than a permanent quality label.

## Completion and reporting

A completed batch must include exactly one result per selected exam, a summary matching the results and finding dispositions, a completion date, and an AI-audit disclosure. `closed_findings` counts resolved, accepted-risk, and dismissed findings; none of those dispositions may omit its rationale. Repository validation rejects stale hashes, wrong guide/vendor paths, duplicate codes or findings, inconsistent verdicts, incomplete checks, and incorrect summaries.

Report AI-audit coverage separately from source validation and human review. “Audited” means checked against this rubric at a particular snapshot; it is not a guarantee of correctness.
