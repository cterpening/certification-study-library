# Certification discovery audit and monitor — September 17, 2026

## Scope and outcome

- Compared 26 registered vendors plus Google Education, OpenAI, and Anthropic.
- Configured 41 official sources: 37 weekly catalog scopes and four monthly announcement/status scopes.
- Initial accepted listing baseline: 35 sources, 686 observations. These are not 686 distinct certifications.
- Last full attempt: 34 usable sources, seven manual-review results, zero other fetch errors. OpenAI retains its earlier successful same-day observation despite a later 403.
- Full source-attempt evidence: `2026-09-17-certification-discovery.json`.
- Public findings and vendor ledger: `docs/research/2026-09-17-catalog-audit.md`.
- Updated OpenAI Academy credential labels/course overview and Anthropic public contract; no new guide publication or technical re-audit claimed.

## Activation

Workflow schedules are configured locally. Nothing in this work was committed, pushed, merged, or deployed. GitHub schedules activate after the workflow reaches the default branch with Actions enabled. The monthly run fetches known sources and emits a broader research checklist; it does not execute unauthenticated internet searches or complete blueprint reviews. No repository setting, account onboarding, or external notification was changed.

## Public Anthropic guide evidence

The partner catalog linked these public PDFs without authentication. All four identify version 1.0 effective July 2026. Exam questions and PDF contents were not copied into the repository. Registration eligibility remains partner-restricted.

| Exam | Downloaded filename | SHA-256 |
|---|---|---|
| CCAO-F | anthropic-associate-foundations.pdf | `ddb102d57f4ef82c62767b610e810d68c0320de9644f1c9f3e44a1399cdbacec` |
| CCDV-F | anthropic-developer-foundations.pdf | `8c52679323cb546790d7d663cbbb48ff42f76f813bbe97239dfde5c32c1c32bd` |
| CCAR-F | anthropic-architect-foundations.pdf | `9bac07c3e6671e55f6cd0232205340a370e8a13a97e8247237dcb71312bccfc2` |
| CCAR-P | anthropic-architect-professional.pdf | `19a111ae61a07066ebe26f7f2b87744f8266cfc0d47093a1d5bbf61e12dd4221` |

Resolve current downloads from https://anthropic-partners.skilljar.com/page/partner-certifications rather than assuming content remains unchanged at a versioned attachment URL.

## Verification

- 136 unit tests passed, including 12 discovery tests.
- Repository schemas/semantic validation passed.
- Strict MkDocs build passed.
- Workflow YAML and Bash syntax passed; third-party actions pinned to repository-standard commit SHAs.
- All 35 accepted baselines replayed unchanged; regex/URL policy checks and unique listing keys passed.
- Git diff whitespace checks passed with the repository's normal Windows line-ending configuration.
- Generated-site validation passed.

A fresh live comparison after accepting the baseline returned unchanged for HashiCorp, Databricks, and the AWS exam-guide index (three sources, zero errors).

## Follow-up: remaining seven catalog scopes

- Completed the scoped catalog reviews for GitHub, Microsoft, Cisco, MongoDB, ServiceNow, IBM and OpenAI Academy using public browser rendering and website feeds. Normalized evidence is in `2026-09-17-catalog-follow-up.json`; findings are in `docs/research/2026-09-17-catalog-follow-up.md`.
- GitHub: six certifications, all covered. Microsoft: all 74 results reconciled, including GitHub/MOS overlap. IBM: all 74 current Certification-filtered results reconciled. Cisco: both tables, 77 exam entries with career/partner/lab distinctions. MongoDB: four families. ServiceNow: all four role branches, preserving certification/suite/accreditation distinctions. OpenAI: all 14 courses rechecked.
- Added guarded GitHub/Microsoft public JSON extraction. Incomplete totals, pagination, duplicate identities, unexpected URLs and contract changes require manual review. Required-exam references detect transitions within an unchanged credential family.
- Follow-up automatic attempt: three usable sources, four manual reviews, zero errors. Accepted baseline now has 37 sources and 766 observations. Later replay returned unchanged for GitHub/Microsoft and HTTP 403 for OpenAI; its successful observation remains intact. Browser-only snapshots were not accepted as HTML baselines.
- Added PL-400 → AB-400 and DP-420 October notices and matching upcoming-change metadata. Registered and checked the new AB-400 reference URL (HTTP 200), updating PL-400 link evidence only. Historical objective snapshots, technical review dates and review hashes remain unchanged.
- 139 unit tests passed, including 15 discovery tests. Repository validation, strict MkDocs build, generated-site validation and normal Git whitespace checks passed. The generated site includes the follow-up report, 223 guides and 3368 registered sources.

These observations supersede the initial unresolved-catalog ledger, not the initial attempt's historical results. New certification guides and substantive replacement-blueprint mapping remain production work. All changes remain local.
