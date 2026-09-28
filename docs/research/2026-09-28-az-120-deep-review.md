# AZ-120 deep review — September 28, 2026

The [AZ-120 guide](../../guides/AZ-120-planning-administering-azure-sap-workloads.md)
was read in full and mapped to **78 detailed objectives in ten groups**. It now
includes seven worked examples, ten labs and 48 explained original checks.
Twenty-seven local assertions validate the synthetic calculations. The review
is complete with a scoped documentation blocker: Microsoft sources differ on
secondary-node backup operations. Independent human review remains pending.
No cloud, SAP, guest command, deployment, backup, restore, failover, preview
agent or commercial lesson was executed.

## Exam and learning catalogs

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-120)
retains the April 17, 2026 baseline, with unchanged objective and status hashes.
The [credential page](https://learn.microsoft.com/en-us/credentials/certifications/azure-for-sap-workloads-specialty/)
lists 100 minutes, seven exam languages and renewal; no retirement or replacement
is announced. An exam sandbox is offered, but no Microsoft Practice Assessment
was shown. The actual exam/sandbox was not entered.

The [official course](https://learn.microsoft.com/en-us/training/courses/az-120t00/)
lists three days and three course languages. Its loading syllabus did not
reproduce the guide's former 29-hour estimate, which is now qualified.
The four retained Pluralsight listings show June 5, 2026 and a combined
6 hr 46 min: [Big Picture](https://www.pluralsight.com/courses/sap-azure-big-picture)
1 hr 28 min, [Building and Deploying](https://www.pluralsight.com/courses/building-deploying-azure-sap-workloads)
2 hr 52 min, [Infrastructure](https://www.pluralsight.com/courses/azure-infrastructure-designing-implementing-sap-workloads-cert)
1 hr 14 min and [HA/DR](https://www.pluralsight.com/courses/azure-sap-workloads-designing-implementing-ha-disaster-recovery-cert)
1 hr 12 min. Update labels do not verify lesson coverage or SAP support currency.

Direct O'Reilly and Udemy access was blocked. An indexed
[O'Reilly listing](https://www.oreilly.com/library/view/sap-on-azure/9781838983987/Text/Index.xhtml)
confirms February 2020 and 242 pages; its former platform reading estimate
was not reverified. The indexed
[ReTeam Labs listing](https://www.udemy.com/course/microsoft-azure-for-sap-workloads-az-120-exam-preparation/)
was found, but its old duration/update fields remain unverified.
[MeasureUp](https://www.measureup.com/microsoft-practice-test-az-120-planning-and-administering-microsoft-azure-for-sap-workloads.html)
lists 115 items and a December 2021 release, with older HLI coverage and generic
FAQ counts/duration that differ from product-specific and official information.
The guide now identifies those limits. No paid content or actual questions
were inspected; no completeness or question-originality claim is made.

## Applied content changes

- **Storage:** distinguish mixed certified data/log types from corresponding
  HSR replica-volume symmetry; add a shared VM I/O budget and clarify
  [Premium SSD v2](https://learn.microsoft.com/en-us/azure/sap/workloads/hana-vm-premium-ssd-v2)
  versus [Write Accelerator](https://learn.microsoft.com/en-us/azure/virtual-machines/how-to-enable-write-accelerator)
  eligibility. Exact SAP certification, OS and SKU matrices still require verification.
- **Networking and fencing:** add a Linux
  [MANA readiness worksheet](https://learn.microsoft.com/en-us/azure/virtual-network/accelerated-networking-mana-linux),
  RISE gateway/ownership boundaries and OS-specific shared-disk/Azure-agent
  fencing considerations. Remove an unconditional cross-zone traffic-charge
  implication; current pricing depends on services and path.
- **Recovery:** distinguish current
  [instance-snapshot policy subtypes](https://learn.microsoft.com/en-us/azure/backup/sap-hana-database-instances-backup),
  preview HSR support, database backup prerequisites and separate log replay.
  Add a continuous-chain timeline and RPO/RTO calculations without presenting
  the unexecuted exercise as a successful restore.
- **Operations:** clarify that
  [VIS start/stop](https://learn.microsoft.com/en-us/azure/sap/center-sap-solutions/start-stop-sap-systems)
  changes SAP instance state while VMs stay allocated; HANA action scope and
  cluster prerequisites matter. Add provider/data/alert evidence for
  [Azure Monitor for SAP](https://learn.microsoft.com/en-us/azure/sap/monitor/providers).
- **Automation:** use the [SDAF 3.23 release](https://github.com/Azure/sap-automation/releases/tag/v3.23.0.0)
  to distinguish deployment success from configuration, HA and backup acceptance.
  Add planned-versus-executed test coverage and explicit critical-case gates.
- **Security integration:** record the
  [Sentinel SAP container connector](https://learn.microsoft.com/en-us/azure/sentinel/sap/deployment-overview)
  retirement on September 14 and image removal on October 14, 2026.
  Continued ingestion from an old container does not establish supported DR
  redeployment. This supplements operational learning without changing the blueprint.

## Unresolved source discrepancy

The [native HSR architecture](https://learn.microsoft.com/en-us/azure/backup/azure-backup-architecture-for-sap-hana-backup)
groups the nodes as one protected item and follows the primary, with a remedial
full backup when the log chain breaks. The
[HANA FAQ](https://learn.microsoft.com/en-us/azure/backup/sap-hana-faq-backup-azure-vm)
describes manually stopping protection on a secondary and resuming it after
promotion. Its protection-model scope is unclear. The guide keeps this
discrepancy visible and does not combine the operational recipes. Confirmation
of the exact supported model and transition is required before that lab can
be executed. A dated follow-up is recorded for October 5.

A support-matrix link in the HSR procedure led to SQL backup documentation.
That navigation target was not used as HANA support evidence. Broad storage
matrices and their footnotes also require product-specific reconciliation;
this review does not certify every listed configuration.

## Blog intake

| Primary article | Reviewed boundary | Added learning value |
|---|---|---|
| [Zone alignment](https://techcommunity.microsoft.com/blog/sapapplications/aligning-sap-application-servers-with-the-hana-primary-zone-on-azure-public-prev/4490925), sanoopt, April 28 | Main concepts, supported scope and active/passive behavior; public preview, nonproduction; Part 2/code not reviewed | Original capacity, latency and compute-state exercises |
| [Sapphire update](https://techcommunity.microsoft.com/blog/sapapplications/sap-on-azure-product-announcements-summary-%E2%80%93-sap-sapphire-2026/4517634), Hiren_Shah_Azure, May 11 | Selected SDAF/STAF section, cross-checked with the August release; wider AI/customer content not audited | Release-pinning and acceptance-evidence worksheet |
| [MANA and existing VM SKUs](https://techcommunity.microsoft.com/blog/sapapplications/mana-support-for-existing-vm-skuswhy-now-is-the-right-time-to-update-linux-on-yo/4524534), RalitzaDeltcheva, June 3 | Main public article; current Linux implementation checks; linked exception timelines not fully audited | Inventory, support-intersection and redeploy/rollback worksheet |

The Tech Community rendered pages were short shells. Public embedded article
bodies and author/date metadata were extracted; the receipt records their
hashes and the sections actually read. No linked installer, plugin or agent
was run. Blog suggestions do not override current product support guidance.

## Verification and follow-up

The machine-readable receipt is
`ADLC_Docs/operations/2026-09-28-az-120-deep-review.json`. It records per-objective
mapping, before/after guide hashes, source fetches, read boundaries, blog intake,
limitations and actual validation results. Historical review evidence is
preserved; unchanged objective/status snapshots are retained.

The 27 assertions check migration drain, shared I/O, surviving capacity,
headroom denominators, sequential latency, recovery windows, illustrative
compute cost, planned test coverage and catalog totals. None establishes
production support or measured SAP performance. Repository tests, consistency
validation, learning-catalog synchronization, strict site build, generated-site
validation and whitespace checks gate publication; their completed results
are recorded in the receipt.

Follow-ups cover the backup discrepancy on October 5, the connector-image
deadline on October 7, and driver/automation/preview/catalog currency on
October 12. Scheduled maintenance detects changes and queues work; it does
not replace semantic review, supported lab execution or human judgment.
