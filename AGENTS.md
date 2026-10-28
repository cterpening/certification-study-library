# Repository instructions

This is an independent, AI-assisted certification study library. Read
`CONTRIBUTING.md`, `docs/CONTENT-POLICY.md` and `docs/SOURCE-QUALITY.md` before
substantive content changes. Follow `docs/GUIDE-QUALITY-STANDARD.md` for guides.

## Subagents for substantial refreshes

For a multi-guide or research-heavy certification refresh, use a coordinating
agent and up to three research subagents, within the available concurrency limit:

1. Exam researcher: official objectives, credential identity, prerequisites,
   delivery status, replacements and retirement evidence.
2. Technical researcher: product documentation, release channels, volatile
   behavior, contradictions and unresolved guide findings.
3. Learning-resource researcher: specific tutorials, workshops, repositories,
   courses and videos, with access, scope, time estimates and source limitations.

Research subagents inspect sources and report proposed changes. They must not
edit shared guides, catalogs, accepted snapshots or review ledgers. Give each
worker an explicit scope and an exclusive scratch output path. Return exact
opened URLs, observations, affected exams, source/candidate matches, confidence,
unresolved questions and a bounded recommendation. These instructions describe
their assigned behavior, not a separate filesystem sandbox.

The coordinator reconciles findings, owns shared-file edits, preserves earlier
work, and runs validation. Keep the existing automated maintenance checks
sequential; do not launch duplicate whole-library collectors. Use coherent
research batches of about ten guides, never more than twelve per packet.

After applying changes, delegate a separate read-only review to a fresh-context
agent. Supply the current diff, complete affected guides, exact objective and
guide hashes, source evidence and applicable rubric. Do not give the reviewer
the editing conversation as its evidence. Resolve material findings and recheck
the affected work. Record same-context and fresh-context review accurately;
neither is human review or live product/lab execution.

For small link corrections or work that does not divide usefully, a single agent
is sufficient. If delegation is unavailable, record that limitation and complete
the authorized work without claiming independent review.

See `docs/AUTOMATION.md` (Subagent refresh workflow),
`docs/SOURCE-FRESHNESS.md`, and `docs/AI-AUDIT.md` for evidence and completion rules.

## Verification

Use the checks in `CONTRIBUTING.md`. Never equate reachability with technical
verification or advance full-review dates after an automated match. Preserve
dated records and accept changed objective baselines only with reviewed content.
Generate `CERTIFICATIONS.txt`, lifecycle pages, review status and shared learning
resources with their existing scripts. Do not hand-edit `.site-build/` or `site/`.
