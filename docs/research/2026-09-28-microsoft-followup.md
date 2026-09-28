# Microsoft portfolio follow-up — September 28, 2026

A fresh check covered **55 existing Microsoft guides**: 50 in the `microsoft` group and five Microsoft 365 Apps guides in `microsoft-office`. The previous completed deep-review pass covered the first group. All five Office guides have now completed detailed reviews and joined the same recurring review queue. Their individual receipts distinguish content review from unexecuted desktop labs and pending human review.

## Current evidence

The official credential catalog returned 74 listings without pagination loss. All 74 credential pages were fetched, and their lifecycle/change signals were inspected. The catalog's single title difference adds “Expert” to AB-100's credential name, which the repository already documents. An unmatched listing is not automatically a missing guide: these include aggregate MOS credentials, older Office versions, Educator, job-specific Excel and the separately classified GitHub vendor. No new Azure exam family appeared in this comparison.

Fresh objective/status candidates were collected for all 55 guides. **38 match their accepted snapshots exactly. The other 17 exactly match the future revisions already recorded in the prior deep-review receipts.** Those future revisions are not promoted early. The monitor writes into a separate candidate directory; its initial “changed” flags describe an empty candidate baseline, so this report uses explicit hashes against both accepted snapshots and prior research observations.

## Retirement and transition check

| Exam | Current notice | Result |
|---|---|---|
| AZ-800 and AZ-801 | September 30, 2026 exam retirement; AZ-802 remains the available path | Already documented; do not retire the replacement credential |
| MS-102 | November 30, 2026 exam and Administrator Expert credential retirement | Already documented; current notice takes precedence over older October announcements |
| PL-400 | Registration transition October 16; registered candidates can sit through October 30; AB-400 starts October 16 | Already documented; registration cutoff and final delivery date are distinct |
| Five Microsoft 365 Apps MOS exams | No retirement notice found on their credential pages or the central exam list | Current five-year credential-expiration context added during each detailed review |

Sources: [exam retirement list](https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams), [credential retirement policy](https://learn.microsoft.com/en-us/credentials/support/credential-retirement), [Windows Server credential](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-administrator-associate/), [Administrator Expert](https://learn.microsoft.com/en-us/credentials/certifications/m365-administrator-expert/), [Power Platform developer transition](https://learn.microsoft.com/en-us/credentials/certifications/power-platform-developer-associate/), and [expiration policy](https://learn.microsoft.com/en-us/credentials/support/credential-expiration-policy).

No additional retirement notice was found in this check. Courseware retirement, product support end, exam availability and an earned credential's expiration are separate facts. A missing catalog listing or blank “Retirement date” label alone is not evidence of retirement.

## Limits and follow-through

The evidence is recorded in `ADLC_Docs/operations/2026-09-28-microsoft-followup.json`. This is a fresh change/lifecycle scan, not a second full technical audit of the 50 recently reviewed guides. Their 14 unresolved evidence gaps remain visible. The MOS review reads the linked detailed PDF, task documentation and useful articles before updating learning material; the automatic page adapter currently sees only broad domains.

Each changed certification and its supporting documentation is validated, staged, committed and pushed separately. The [review tracker](../MICROSOFT-REVIEW-STATUS.md) records actual progress. No live Office, cloud or exam environment was executed during this scan.

## Completed Office reviews

| Guide | Detailed PDF tasks | Learning-content review |
|---|---:|---|
| [MO-110 Word Associate](2026-09-28-mo-110-deep-review.md) | 70 | Styles, document structure, references, graphics, inspection and collaboration |
| [MO-111 Word Expert](2026-09-28-mo-111-deep-review.md) | 47 | Fields, forms, templates, macros and mail-merge checks |
| [MO-210 Excel Associate](2026-09-28-mo-210-deep-review.md) | 65 | Named-function scope, reference copying, counts, arrays and table totals |
| [MO-211 Excel Expert](2026-09-28-mo-211-deep-review.md) | 48 | Criteria, lookups, payment/calendar models, stale values and Pivot aggregation |
| [MO-310 PowerPoint Associate](2026-09-28-mo-310-deep-review.md) | 73 | Navigation, masters, media preservation, animation and accessibility |

Together these reviews map 303 detailed tasks and add bounded article recommendations, original examples, proposed exercises and answered checks. The full 55-guide tracker now records **41 reviewed** and **14 reviewed with blockers**, with no untouched guides. This completes the requested content-review coverage of the current inventory; source conflicts, future effective dates, desktop/live labs and independent human review remain explicit follow-up work. Scheduled monitoring detects changes and prepares evidence for review; it does not silently rewrite learning content or accept a changed blueprint.
