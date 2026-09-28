# AZ-140 deep review — September 28, 2026

The [AZ-140 guide](../../guides/AZ-140-configuring-operating-azure-virtual-desktop.md)
was read in full and mapped to **78 objectives in twelve groups**. It now has
seven worked examples, ten labs and 48 explained original checks. Thirty
offline assertions verify the calculations. No Azure, tenant, Arc, endpoint,
media, storage, update, backup/restore, failover or paid-content execution
occurred. Independent human review remains pending.

## Scope and lifecycle

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-140)
retains its July 20, 2026 baseline. Objective/status hashes are unchanged and no
future objective announcement is shown. The
[credential](https://learn.microsoft.com/en-us/credentials/certifications/azure-virtual-desktop-specialty/)
is active, with 100 minutes, seven languages and renewal. Practice Assessment
and sandbox links were verified at the landing page only.

The review separates four timelines:

| Item | Current primary evidence | Applied treatment |
|---|---|---|
| [AVD classic](https://learn.microsoft.com/en-us/azure/virtual-desktop/whats-new) | September 30, 2026 retirement blocks classic connections | Distinguish service generation from the active certification |
| [Windows Remote Desktop clients](https://learn.microsoft.com/en-us/previous-versions/remote-desktop-client/whats-new-windows) | Public-cloud MSI support ended March 27; government/21Vianet/classic extension ends September 28; Store app ended in 2025 | Inventory executable/distribution and move to supported Windows App |
| [Classic Teams](https://learn.microsoft.com/en-us/microsoftteams/teams-classic-client-end-of-availability) | VDI availability ended July 1, 2025 | Do not teach classic Teams as a supported fallback |
| [Windows-endpoint WebRTC optimization](https://techcommunity.microsoft.com/blog/microsoftteamsblog/the-next-chapter-of-microsoft-teams-in-virtualized-environments/4498259) | Support ends October 1, 2026; availability ends April 1, 2027, for the announced AVD/Windows 365/Citrix scope | Separate app installation from verified SlimCore and call/sharing evidence |

The [AVD Teams overview](https://learn.microsoft.com/en-us/azure/virtual-desktop/teams-on-avd)
conflates the classic-client and optimization deadlines and differs from the
[Teams VDI requirements](https://learn.microsoft.com/en-us/microsoftteams/vdi-2)
on some client minima. The guide explicitly uses the dedicated timelines and
requires a currently supported client distribution; it does not invent a
reconciled minimum version or claim Microsoft corrected its page.

## Applied technical changes

- **Management:** distinguish the creation-time
  [host-pool management choice](https://learn.microsoft.com/en-us/azure/virtual-desktop/host-pool-management-approaches)
  and service-managed configuration from external standard-pool tooling.
  [Host replacement](https://learn.microsoft.com/en-us/azure/virtual-desktop/session-host-update)
  needs surviving capacity, externalized state, monitoring and tested rollback.
- **Identity:** update the universal service-principal assumption for
  [managed identities](https://learn.microsoft.com/en-us/azure/virtual-desktop/configure-managed-identity),
  retaining App Attach's exception and feature-specific authorization.
- **Architecture:** add [Hybrid](https://learn.microsoft.com/en-us/azure/virtual-desktop/hybrid-overview)
  boundaries and its unsupported multi-session/power-management features.
  Clarify Multipath's client/cloud scope and separate private discovery, feed,
  host connection and storage endpoints.
- **Profiles:** apply current
  [Entra Kerberos requirements](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-identity-auth-hybrid-identities-enable)
  and the [profile procedure](https://learn.microsoft.com/en-us/fslogix/how-to-configure-profile-container-entra-id-hybrid),
  with scoped storage-app authentication exceptions. Record
  [FSLogix 26.08](https://learn.microsoft.com/en-us/fslogix/overview-release-notes)
  and its unchanged ticket lifetime, plus provider/cache recovery limits.
- **Applications and scale:** distinguish package/attach/registration/launch
  and service-principal storage access; separate
  [dynamic scaling](https://learn.microsoft.com/en-us/azure/virtual-desktop/autoscale-create-assign-scaling-plan)
  from power management, exclusions and personal-host hibernation constraints.
- **Servicing:** use the
  [OS/update-type matrix](https://learn.microsoft.com/en-us/azure/virtual-desktop/windows-update-management-methodologies-session-hosts)
  rather than carrying one monthly-update recommendation into every OS upgrade.
  All seven tables were inspected with cell boundaries preserved.

The worked examples cover maintenance capacity, network demand, sign-in I/O,
per-file handles, cache flush time, migration-evidence denominators and full
recovery timing. The numbers are original assumptions, not performance claims,
actual autoscale implementation or proof of recoverability.

## Learning resources and blog intake

The [Microsoft course](https://learn.microsoft.com/en-us/training/courses/az-140t00)
lists four days and four languages; its loading syllabus did not reproduce
the old self-paced runtime. Only the first
[readiness episode](https://learn.microsoft.com/en-us/shows/exam-readiness-zone/preparing-for-az-140-plan-and-implement-an-azure-virtual-desktop-infrastructure)
was inspected, with chapters through 18:16; the old series total is qualified.
The added [Pluralsight path](https://www.pluralsight.com/paths/configuring-and-operating-microsoft-azure-virtual-desktop-az-140-2023)
offers six Ned Bellavance courses dated 2023–2024. Their durations total
9 hr 14 min against a rounded nine-hour header; it is a structured foundation
requiring current-doc reconciliation.

Direct O'Reilly/Udemy access remains blocked. Indexed primary listings confirm
[Mastering AVD](https://www.oreilly.com/library/view/mastering-azure-virtual/9781835884140/)
(July 2024, 718 pages, 14 hr 54 min platform estimate),
[Securing Cloud PCs and AVD](https://www.oreilly.com/library/view/securing-cloud-pcs/9781835460252/B22033_Part_1.xhtml)
(June 2024, 396 pages, 8 hr 22 min), and
[Kubaib's course](https://www.udemy.com/course/az-140-avd-azure-virtual-desktop/)
(April 2026, 11 sections, 125 lectures, 23 hr 24 min).
[MeasureUp](https://www.measureup.com/microsoft-practice-test-az-140-configuring-and-operating-microsoft-azure-virtual-desktop.html)
lists 130 product questions and a December 2024 update; its generic FAQ says
about 150. Product-specific metadata replaces the guide's generic count.
No paid material, actual questions or completeness/originality audit was performed.

| Microsoft blog | Reading boundary | Original learner task |
|---|---|---|
| [Enhanced host management](https://techcommunity.microsoft.com/blog/azurevirtualdesktopblog/enhanced-host-pool-management-for-azure-virtual-desktop-is-now-generally-availab/4534612), NeoCai, July 9 | Main announcement and short setup outline; linked code not inspected | Management ownership and maintenance-capacity worksheet |
| [Hybrid GA](https://techcommunity.microsoft.com/blog/azurevirtualdesktopblog/microsoft-azure-virtual-desktop-hybrid-is-now-generally-available/4550523), Steve_Downs, September 1 | Architecture, ownership/licensing and deployment outline; promotional claims excluded | Supported-feature comparison and responsibility diagram |
| [Teams VDI transition](https://techcommunity.microsoft.com/blog/microsoftteamsblog/the-next-chapter-of-microsoft-teams-in-virtualized-environments/4498259), Fernando_Klurfan, March 2 | Timeline, scope and quickstart checklist; later pitfalls only partly read | Endpoint-scoped deadline and adoption-evidence worksheet |

Public embedded article bodies supplied content where rendered pages were
shells. The receipt records author/date metadata, extraction hashes and read
boundaries. Announcements were checked against implementation guidance;
marketing benefits were not adopted as measured results.

## Validation and follow-up

The receipt at `ADLC_Docs/operations/2026-09-28-az-140-deep-review.json` contains
objective mapping, source results, historical evidence, guide hashes, bounded
reading notes and actual gate results. Thirty assertions cover all numerical
examples, private endpoint counts and learning-time arithmetic. Unchanged
objective/status snapshots are preserved, alongside the earlier review record.

Repository tests, catalog consistency, repository validation, strict site
build, generated-site validation and whitespace checks gate publication.
Their completed outcomes are recorded in the receipt. Events schedule checks
for classic/client retirement on September 30, WebRTC support on October 1,
management/profile currency on October 12 and the later optimization
availability deadline on March 1, 2027. Automation detects and queues changes;
semantic review, lab execution and human judgment remain separate work.
