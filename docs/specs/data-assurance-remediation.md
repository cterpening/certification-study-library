# Data-assurance remediation

Status: implementation approved by the repository owner on September 6, 2026.
This records the bounded follow-up to findings review, not a new backlog or ticket.

## Change and approach

All ten trusted catalogs must pass their declared schemas before semantic validation.
Missing catalogs, invalid schemas, malformed entries, unknown properties and duplicate
source-health IDs must fail with actionable diagnostics, without dictionary overwrite
or a shape-related traceback. Existing cross-reference, date and snapshot checks remain.

The source-type enum will explicitly include the 27 additional categories already used
by 117 registered records; it remains a finite allowlist. Recategorizing those records
would change established meaning and freshness baselines without new source evidence.
No arbitrary source category is accepted.

Retain the newest health observation for each duplicate ID, only after confirming all
other fields agree. Preserve the original observation dates and snapshot generation date.
Reject duplicate catalog/baseline inputs before the health monitor makes requests.

New AI-audit results will bind the guide text, objective snapshot and rubric version.
Rubric 2 requires a guide-content SHA-256. Hash UTF-8 guide text with universal newline
normalization (CRLF/CR to LF), preserving all other text including whitespace/front matter.
Guide-only edits must renew eligibility; unchanged bound results stay excluded by default.
Rubric-1 results remain historical and must never acquire guessed content hashes.

Smoke-test refinement: default preparation currently aborts on the existing blocked
source-validation records for AZ-800 and AZ-802. Keep the passed-review prerequisite,
but report these as `blocked_items` while preparing the 220 ready guides. An explicit
request for a blocked guide still fails. An all-blocked queue must report its blockers,
not imply that current audit coverage is complete. No source record is changed.

## Components and acceptance evidence

- Validator, source-health monitor and audit-batch preparer, with their unit tests.
- Source and audit schemas; health snapshot and active audit rubric version.
- AI-audit documentation, this spec and the remediation verification record.
- Tests cover each catalog's missing/unknown/wrong-type fields, malformed entries,
  duplicate observations and rejection before network access.
- Audit tests cover unchanged content, guide-only edits, blueprint/rubric changes,
  normalized newlines, explicit selection, legacy results and required new hashes.
- Run the complete unittest suite, repository validator, site preparation, strict
  MkDocs build and generated-site validation before each implementation commit.

## Non-functional requirements, risk and rollback

Repository-specific static-content profile: integrity via fail-closed contracts;
compatibility via unchanged CLI and preserved historical results; maintainability via
an explicit registry and regressions; portability via normalized guide hashes;
security/privacy via offline fixtures and no new dependencies or external source fetches.
The site smoke checks protect publication. Runtime availability and cloud requirements
are not applicable to this local maintenance change. No performance improvement is claimed.

Stricter checks can expose previously tolerated data. Review actual errors, never disable
validation to make the build pass. Increased audit eligibility is expected, not lost history.
Rollback uses a reviewed revert of the relevant batch commit; original duplicate observations
and prior schemas remain recoverable in Git. Do not reset unrelated user work.

## Out of scope

No guide rewrites, new audits, live source checks, dependency installs, remote settings,
CI changes, tickets, backlog conversion, human-review claims or finding risk acceptance.
The accelerator at `C:\src-IBM\AgenticDevelopment` remains strictly read-only and reference-only.

Finding fingerprints: `repository-health:source-health:duplicate-identifiers`,
`assessment:data-contracts:uneven-schema-enforcement`,
`assessment:ai-assurance:guide-content-not-bound`.
