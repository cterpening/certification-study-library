# AZ-104 deep review — September 28, 2026

The [AZ-104 guide](../../guides/AZ-104-microsoft-azure-administrator.md) was read
in full and mapped to **82 detailed objectives across 15 groups**. It now has
seven worked examples, ten labs and 48 explained original questions. Twenty-nine
offline assertions check permission sets, synthetic version states, capacity,
weighted rates, recovery timing, retention windows and catalog arithmetic.
One KQL example was reviewed but not run. No cloud, tenant, certificate, backup,
failover, SDK, Bicep or paid-content execution occurred. Human review is pending.

## Exam and catalog findings

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)
retains its April 17, 2026 baseline and 82 objectives. Accepted objective/status
hashes are unchanged, with no future announcement. The
[credential](https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/)
lists 100 minutes, ten languages and annual renewal. Assessment and sandbox links
were verified at the landing page only; no session, questions or results were read.
The [official course](https://learn.microsoft.com/en-us/training/courses/az-104t00)
lists four days and ten course languages. Its syllabus remained a loading widget;
study-hour budgets are editorial estimates.

The [Pluralsight path](https://www.pluralsight.com/paths/az-104-microsoft-azure-administrator-certification-prep)
now has six courses and eight labs. Course durations total 1,787 minutes (29h47),
and labs total 300 minutes: **34h47**, consistent with its rounded 35-hour header.
Identity/storage courses are dated September 9 and networking September 23.
One introductory paragraph still shows older domain weights even though a later
paragraph matches the current blueprint; official scope takes precedence.

Direct O'Reilly and Udemy retrievals were blocked. Indexed public pages show:

- [Exam Ref, second edition](https://www.oreilly.com/library/view/exam-ref-az-104/9780138345990/):
  Charles Pluta, July 2024, 391 pages, platform reading estimate 10h34. Contents
  were inspected; the book was not read.
- [ACI Learning video](https://www.oreilly.com/library/view/microsoft-azure-administrator/9781836206132/video1_1.html):
  ACI Learning/Adam Gordon, May 2024, 27h23. Selected chapter outlines include
  older Azure AD/Azure Disk Encryption and AKS material; learners need to filter
  against current implementation requirements. Paid lessons were not watched.
- [Scott Duffy's course](https://www.udemy.com/course/70533-azure/): June 2026,
  26 sections, 187 lectures, 18h2. Public metadata/selected outline are not evidence
  of paid lesson correctness or question originality.

[Whizlabs' exact product](https://www.whizlabs.com/microsoft-azure-certification-az-104/)
returned a title shell directly and in the indexed view. Earlier 107-video,
164-lab and 22-quiz counts were not reproduced and are marked unverified. Historical
launch articles and alternate-host counts were not substituted for the product.
The retained Savill video likewise exposed only a shell; its historical runtime
is labeled unverified.

The [MeasureUp assessment](https://www.measureup.com/assessment-az-104-microsoft-azure-administrator.html)
explicitly contains 30 questions from an associated practice test and **no
explanations or references**, with June 2026 metadata. The guide now distinguishes
that assessment from an explanation-based learning resource. No paid questions,
translated content or claimed exam realism were evaluated.

## Implementation changes

- **Identity and governance:** explain group-license processing and safe
  transitions, nesting differences from SSPR, current authentication-method
  management, role exclusions versus explicit denies and alternate key-access
  paths. A role name alone is not an effective-access result.
- **Storage:** add SMB share/ACL/client gates, replication prerequisites and
  destination restrictions, current-version recovery, and periodic lifecycle
  behavior. A simplified full-copy version example is not a billing estimate.
- **Deployment and compute:** distinguish omitted resources from omitted
  properties in incremental ARM deployment, qualify decompilation, correct the
  host-encryption description and explain registry ABAC roles. Add per-worker
  capacity reasoning and container sizing/restart/scaling checks.
- **App Service:** explain sticky identity/network dependencies, certificate
  binding and renewal boundaries, and app/database recovery differences. The
  current certificate reference specifies 198-day ASC validity/validation reuse;
  exported copies and ownership revalidation need their own process.
- **Networking:** scope private-subnet defaults to new VNet/API behavior after
  March 31, 2026, with existing-VNet and older-API exceptions. Explicit egress is
  separate from NSG permission. Retire Basic public-IP/load-balancer assumptions
  and new NSG flow-log labs; calculate subnet headroom.
- **Monitoring and recovery:** verify AMA/DCR ingestion, expose missing-machine
  coverage and request-weighted rates, and distinguish activity events from
  operations. Add measured RPO/RTO, isolated test failover, and fixed immutability
  versus retention, locking and underlying WORM availability.

Sources sit beside the claims in the guide. The evidence notes identify the
sections actually read; full command samples, every region/SKU matrix and all
linked procedures were not audited. Cloud labs remain unexecuted designs.

## Blog intake

[Routing options for VMs from private subnets](https://techcommunity.microsoft.com/blog/azurenetworkingblog/routing-options-for-vms-from-private-subnets/4271244),
Microsoft author `ulkeba`, October 20, 2024, was read through its introduction,
setup and first two scenarios. It informs an original path/evidence worksheet.
Its September 2025 deadline is outdated and explicitly superseded by current
API-scoped documentation. The remaining scenarios and Terraform repository were
not fully audited or executed.

[Industry-wide certificate changes](https://techcommunity.microsoft.com/blog/appsonazureblog/industry-wide-certificate-changes-impacting-azure-app-service-certificates/4477924),
Microsoft author `YutangLin`, December 15, 2025, has a visible February 17, 2026
update directing readers to current Learn guidance. The complete main article
informs an original certificate inventory worksheet. Its general 200-day limit
and broad “no action” summary do not replace current ASC implementation/export/
validation details. Public article bodies and author metadata were extracted from
embedded page JSON because the rendered main elements exposed title shells.

## Evidence and follow-ups

The operation receipt is `ADLC_Docs/operations/2026-09-28-az-104-deep-review.json`.
It preserves earlier records, objective mapping, source fetches, article-extraction
metadata, indexed catalog observations, applied findings and validation results.
The historical source review is retained; unchanged objective/status snapshots
are not rewritten.

October 12 events revisit network/storage/recovery support and App Service,
certificate and learning-catalog changes. A March 1, 2028 event precedes the
announced March 31 linked-database custom-backup retirement. The
[Microsoft review tracker](../MICROSOFT-REVIEW-STATUS.md) records completed reviews
and unresolved findings. Scheduled checks detect drift and queue work; they do
not perform an independent semantic review or execute these labs.
