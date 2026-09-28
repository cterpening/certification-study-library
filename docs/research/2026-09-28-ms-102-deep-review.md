# MS-102 deep review — September 28, 2026

The complete [guide](../../guides/MS-102-microsoft-365-administrator.md) was read
and all **54 objectives in 12 groups** individually mapped. The accepted April 28
snapshot is unchanged. November 30 remains the announced exam/credential
retirement; the credential lists four qualifying associate certifications.
The official course-retirement table names AB-650T00 as replacement training,
which does not establish a direct replacement expert credential.

## Learning changes

Five worked examples cover operation-specific recovery points and elapsed
recovery time, licensing membership versus successful assignment, Conditional
Access grant composition, email protection precedence and DLP precision/recall.
Two new labs bring the total to **ten**. All 36 existing questions now have an
answer key, with eight additional answered checks, for **44 answers**.
Ten offline arithmetic/decision/catalog checks passed, and one PowerShell
inventory block was syntax-parsed. No tenant, Graph call, directory migration,
sync upgrade, restore, paid service, DLP deployment or preview feature was run.

Operational additions distinguish September 30 Connect Sync enforcement from
the separate Connect Health agent requirements and normal version support.
They cover app/certificate ownership and scheduler-dependent rotation,
destination-first licensing migration, November 3 `memberOf` retirement,
legacy app-grant read-only behavior, Cloud Apps enforcement prerequisites,
Data Explorer permissions and Teams chat/file/tenant boundaries.

Backup treatment separates preview Full Workload Backup from custom policies,
including paused-policy precedence, daily discovery, static versus dynamic
membership, exclusions and removal. Retention reductions and moves to shorter
windows have a 30-day deletion grace period. The original-location granular
restore feature is documented now; older overview and April blog roadmap
wording is qualified by specific current instructions. Published restore
performance medians are not a tenant recovery-time commitment.

The passkey transition now explicitly identifies Global Administrators and
external users in the July 2027 exception, while internal guests stay in the
February cohort. A shared follow-up covers related guides. The retrieved
general Entra release feed stopped at June; specific product pages and the
September Microsoft blog supplied more recent evidence. Relevant current
Defender/Purview entries were checked without treating every preview as a new
exam objective. Six dated follow-ups cover these dependencies and retirement.

## Open documentation gap

[Backup policy configuration](https://learn.microsoft.com/en-us/microsoft-365/backup/backup-view-edit-policies?view=o365-worldwide)
supports a two-year recovery window, but the
[restore-frequency table](https://learn.microsoft.com/en-us/microsoft-365/backup/backup-restore-data?view=o365-worldwide)
documents only days 0–365. The guide does not extend that schedule into the
second year. This review is **reviewed with blockers**, with an October 1
checkpoint for authoritative clarification. The original September 1 passed
source review is retained unchanged as historical evidence; it does not resolve
this newly recorded gap.

## Resource and blog decisions

Nine Learn paths currently list 39 modules. Their earlier 28h45 runtime is
historical and was not exposed by this retrieval. Direct course metadata still
lists five days despite the credential page's empty training collection.
Pluralsight's five public listings total 7h44 and date from June–December 2025;
they do not prove April 2026 coverage. MeasureUp lists 123 questions and a
November 2025 update; its exam-alone credential claim is qualified by Microsoft's
associate prerequisite. Paid lessons and questions were not reviewed.

O'Reilly book/video and Udemy blocked retrieval, so their older metadata is
clearly historical. Video-channel and partner shells do not establish underlying
content, eligibility or schedules. The practice-assessment entry point did not
expose question content for review.

- [Microsoft 365 Backup granular restore now generally available](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-backup-granular-restore-now-generally-available/4515936),
  Microsoft author `diksha050`, April 29: main article read; accepted a
  file-versus-site recovery exercise, with current in-place behavior and
  operation-specific recovery-point limits supplied by product documentation.
- [What's new in Microsoft Entra: September 2026](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/what%E2%80%99s-new-in-microsoft-entra-september-2026/4545179),
  Yina Arenas, September 1: main article read; accepted a `memberOf` dependency
  and migration exercise corroborated by the official migration page. Adjacent
  previews are not assumed to be available in every tenant or added to the exam.

Linked demonstrations were not executed. Research, repair and local checks used
the same AI context; independent and human review remain pending. The evidence
ledger is `ADLC_Docs/operations/2026-09-28-ms-102-deep-review.json`, containing
prior records, objective mappings, source observations, hashes, findings and
local validation results.
