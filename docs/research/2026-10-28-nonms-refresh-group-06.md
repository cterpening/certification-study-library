# Non-Microsoft certification refresh — Group 6

**Completed:** October 28, 2026
**Guides:** 10 (Oracle and GitHub)
**Queue:** Group 6 of 17 from the frozen 167-guide eligible non-Microsoft queue. **Remaining after this group: 107 guides, approximately 11 groups.**

## Work completed

- Rechecked the current official exam or learning-path pages, accepted objective material, credential status, lifecycle, and applicable product release channels for each guide.
- Refreshed current course and practice-assessment references and synchronized `docs/LEARNING-RESOURCES.md`.
- Added 17 public first-party sources covering Oracle credential naming, OCI release channels, AI Database 26ai, JDK 21, GitHub credentials and practice assessments, workflow lockfiles, secret protection, audit logs, and stacked pull requests.
- Captured nine changed Oracle objective/status snapshots as dated October 28 records and restored the former stable snapshot paths so older review receipts remain verifiable. The observed changes were public title/year removal for OCI credentials and expanded Java learning-path text; no exam objective bullets or GitHub objective snapshots changed.
- Removed a withdrawn GH-900 LinkedIn Learning path after its registered URL returned HTTP 404. Updated the GH-200 practice-assessment link and credential maintenance note; GH-500 current security preview and audit-log context; GH-900 assessment access and stacked pull requests context.

## Guide-specific updates

| Exam | New information added |
|---|---|
| 1Z0-1109-26 | OCI DevOps credential title is now yearless; the current learning path lists 35 hours and the exam 90 minutes. |
| 1Z0-1111-26 | OCI Observability title is yearless; path lists 9 hours and exam 90 minutes. OCI Monitoring API gained dual-stack endpoint context. |
| 1Z0-1124-26 | OCI Networking title is yearless; path lists 19 hours and exam 90 minutes. Added October NAT/DRG and September FastConnect updates; retained the source path’s 2025 copy inconsistency as a caveat. |
| 1Z0-171 | Added dated Oracle AI Database 26ai SQL examples such as `GROUP BY ALL`, direct joins in `UPDATE`/`DELETE`, `INSERT INTO SET`, and SQL `BOOLEAN`; these are product context, not asserted exam objectives. Current path lists 20 hours and exam 120 minutes. |
| 1Z0-182 | Clarified SQL Firewall’s Oracle Database Vault and licensing boundary. Current path lists 12 hours and exam 120 minutes. |
| 1Z0-830 | Current learning text was expanded. Added JDK 21.0.13 GA (October 24) and the JDK 21.0.13+ licensing pointer. Path lists 40 hours; exam 120 minutes. |
| 1Z0-997-26 | OCI Architect title is yearless; added dated Full Stack Disaster Recovery support for PostgreSQL and networking context. Path lists 26 hours and exam 90 minutes. |
| GH-200 | GitHub Actions workflow dependency lockfiles moved from October 14 public preview to general availability October 28 on GitHub Enterprise Cloud, Cloud with Data Residency, Team, and Free. Pinning does not establish dependency safety. Updated practice-assessment and credential-maintenance references. |
| GH-500 | Added the October 28 public preview for AI-detected secret push protection, its enablement prerequisites and AI-credit boundary, plus the November 12 secret-scanning audit-log `business` field change. Both are dated product context, separate from the July exam baseline. |
| GH-900 | Added stacked pull requests GA context and the current sign-in-required practice-assessment route. Removed the broken LinkedIn Learning listing. Fundamentals credential remains nonrenewing. |

Oracle University currently publishes yearless OCI credential names even where versioned 2026 exam codes and learning-path URLs remain. The Aug 10 program announcement says OCI credentials are valid for 24 months and professional learning paths require paid access. Oracle path descriptions and durations are recorded as shown; the odd 2025 networking sentence remains explicitly unresolved.

## Source health and review limits

The Group 6 source sweep checked **163 registered source URLs: 158 returned HTTP 200, five blocked automated fetching, and none were missing or errored**. Blocked pages were DataCamp GH-900, Oracle University’s certification update post, O’Reilly GH-200 and GH-900 listings, and Udemy GH-900. Oracle’s program announcement was directly reviewed through the public web reader; HTTP 403 is recorded as an automation-access limit, not a dead-page finding. The withdrawn LinkedIn GH-900 path was removed from the source catalog and group sweep after its 404.

Official practice-assessment launch pages require sign-in; assessment content was not opened. No Oracle paid course interior, vendor tenant, live API, or product lab was accessed. All refresh work is AI-assisted. The Group 6 audit is a same-context read-only audit, **not an independent or human review**.

## Selected first-party sources

- [OCI certification learning paths and exams: 2026 updates](https://blogs.oracle.com/oracleuniversity/oci-certification-learning-paths-and-exams-2026-updates-now-available)
- [OCI Networking release notes](https://docs.oracle.com/en-us/iaas/releasenotes/services/network/index.htm) and [Monitoring release notes](https://docs.oracle.com/en-us/iaas/releasenotes/services/monitoring/)
- [OCI release notes](https://docs.oracle.com/en-us/iaas/releasenotes/)
- [Oracle AI Database 26ai new features](https://docs.oracle.com/en/database/oracle/oracle-database/26/nfcoa/all-nfg.html)
- [JDK 21 release notes](https://www.oracle.com/java/technologies/javase/21all-relnotes.html) and [Oracle Java downloads/licensing](https://www.oracle.com/java/technologies/downloads/)
- [GitHub Actions workflow lockfiles GA](https://github.blog/changelog/2026-10-28-github-actions-workflow-lockfiles-are-generally-available/)
- [AI-detected secret push protection](https://github.blog/changelog/2026-10-28-push-protection-beyond-predefined-secret-patterns/) and [secret-scanning audit-log update](https://github.blog/changelog/2026-10-20-updates-to-github-secret-scanning/)
- [Stacked pull requests GA](https://github.blog/changelog/2026-10-06-stacked-pull-requests-generally-available/)
- [GH-200](https://learn.microsoft.com/en-us/credentials/certifications/github-actions/), [GH-500](https://learn.microsoft.com/en-us/credentials/certifications/github-advanced-security/), and [GH-900](https://learn.microsoft.com/en-us/credentials/certifications/github-foundations/) credential pages.

## Evidence

The [operations record](../../ADLC_Docs/operations/2026-10-28-nonms-refresh-group-06.json) binds guide hashes, objective/status snapshots, source-validation receipts, source health, and audit status. Structured source-freshness, audit, and deep-review receipts are recorded in `data/source-freshness.json`, `data/ai-audits.json`, and `data/deep-reviews.json`.
