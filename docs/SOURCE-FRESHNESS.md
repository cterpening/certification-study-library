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
4. Add unreviewed discoveries to the candidate inbox, or apply a fully reviewed
   source and content change in a separate repair step.
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
