# Certification inventory

The repository keeps discovery separate from full-guide publication, while the
site exposes both in its generated certification inventory. That page lists
every row in the seed catalog, links to the official listing, and marks whether
a complete guide is published.

- `config/certification-seeds.json` is the source-backed research inventory and
  drives the site's complete certification inventory.
- `CERTIFICATIONS.txt` is its generated, tab-separated Python query input.
- [Certification lifecycle and name history](CERTIFICATION-LIFECYCLE.md) shows
  recorded update/release dates, retirements, replacements and aliases.
- `config/exams.json` contains credentials with complete study guides and the
  metadata needed to publish and monitor those guides. The site's study guide
  catalog is limited to these entries.

An entry in the seed catalog means “research or enrich this credential.” Its
inventory row is visible on the site, but that does not mean a guide exists or
that its sources have been reviewed. Repository validation requires every
published guide to have a seed, while research-only seeds remain valid inventory
entries without a full guide.

[November 23, 2026 library refresh and per-certification evidence](research/2026-11-23-library-refresh.md)

## Current coverage baseline

The November intake adds guides for Microsoft's AB-330 and GitHub's GH-700,
plus an inventory entry for the upcoming MO-410 Outlook exam. **Announced**
means the issuer has named the exam and its availability has yet to be verified.
Both guides passed an independent AI review as drafts. Human review and live
exercises are pending. [Beta guides and announced exams](research/2026-11-20-microsoft-beta-certifications.md) · [Review evidence](research/2026-11-20-microsoft-beta-certifications-evidence.json)

The [IBM Bob v2 Developer Associate intake](research/2026-10-28-ibm-bob-certification-intake.md)
adds live exam C3000-006 / credential C9010800 as checked October 28, 2026.
It joins the existing six IBM guides; this targeted addition does not reverify
those older entries or the full IBM catalog. The guide maps all 52 public
objectives and preserves the official preparation PDF's unresolved general
marketplace-browser question. Product labs and independent human review remain pending.

The Azure and HashiCorp baseline was verified on August 31, 2026. The broader
Microsoft catalog expansion was rechecked on September 1, 2026 and is being
published one source-validated guide at a time.

The September Python Institute inventory covered ten exam versions. The November
inventory contains 13. PCEP-30-03 and PCAP-31-04 launched October 31, 2026,
and PCPP1-32-102 launched November 9. Candidates can still take the three
preceding versions through November 30, 2027. PCEA-30-01 is active on the
issuer's exam information page. [Python version transitions](research/2026-11-23-refresh-16.md) · [PCEA exam information](https://pythoninstitute.org/pcea)

The adjacent OpenEDG programming inventory adds the six active C++ Institute
C/C++ exams and four active JS Institute JavaScript/web-development exams shown
September 2, 2026. It records independently proctored certifications, not the
aligned learning platforms' course-completion certificates.

### Microsoft Azure

The scope is the official [Microsoft Learn certification catalog filtered to the
Azure product](https://learn.microsoft.com/en-us/credentials/browse/?credential_types=certification&products=azure).
The August 31 check also enumerated the live Microsoft Learn credentials API and
filtered its results to non-hidden entries whose `credential_types` contains
`certification` and whose `products` contains `azure`. Both views returned 24
certifications. The broader Azure study scope adds the current AZ-802 exam and
SC-100, which Microsoft does not tag with the Azure product. The query file
therefore contains 27 Azure-scope exam rows for 26 credentials; Microsoft
Certified: Windows Server Hybrid Administrator Associate requires both AZ-800
and AZ-801.

The rule deliberately includes cross-product certifications when Microsoft tags
them with Azure, including AB-900, AB-620, and the SC credentials. It then adds
current `AZ-*` exams that the product facet misses and SC-100 because it is the
expert cybersecurity architecture path over Azure security, identity, and
operations credentials. It excludes Applied Skills and retired credentials.
AB-100 and PL-900 are retained separately because this library already publishes
those guides. The November intake records AI-500 and AZ-802 as active.
[AI-500 study guide](../guides/AI-500-designing-implementing-multi-agent-ai-solutions.md)

### Microsoft beyond Azure

The September expansion selected entries from the official Microsoft Learn
certification catalog. Its scope excluded Applied Skills, Microsoft Office
Specialist and Microsoft Certified Educator. The November intake separately
added the announced MO-410 Outlook exam to the research inventory.

The September 1, 2026 final reconciliation closed the selected Microsoft phase
at 50 published exam guides. The official retirement indexes confirm that
MB-335, MB-700, PL-500, and PL-600 retired June 30; AZ-204 and MB-280 retired
July 31; and AZ-500 and PL-200 retired August 31. Those codes are not missing
current-study targets. Existing guides already cover the selected active,
beta, and still-earnable announced-retirement exams, including AZ-800/AZ-801,
AZ-802, SC-500 and MS-102. This is a curated current catalog, not a promise to
publish every historical Microsoft exam.

Microsoft lists November 30, 2026 as the retirement date for MS-102 and its
Administrator Expert credential. Partner Center identifies AB-650 for the
Modern Work designation path. AB-650 is an active associate credential.
[MS-102 guide](../guides/MS-102-microsoft-365-administrator.md) · [AB-650 guide](../guides/AB-650-ai-services-administrator-associate.md)

SC-401 is active. Its current English skills outline took effect October 28, 2026.
[SC-401 guide](../guides/SC-401-administering-information-security-microsoft-365.md)

### Lifecycle and replacement rule

- An already retired exam is not a current study target and is omitted from the
  generated query list unless an existing published guide or downstream history
  requires its identity to be preserved.
- An exam with an announced future retirement remains in scope. Its seed records
  `retirement-announced` and the exact `retirement_date`; its guide must show the
  date prominently.
- When the vendor names a replacement, the seed also records
  `replacement_exam_code` and `replacement_official_url`. A replacement code must
  exist in this inventory. Beta replacements remain labeled beta.
- A retiring guide explains that earned-credential and transition behavior must
  be verified with the vendor; it does not imply automatic conversion to the new
  credential.

AZ-800 and AZ-801 retired September 30, 2026. The library retains their guides
for historical reference. AZ-802 is the current exam for Windows Server Hybrid
Administrator Associate. [Microsoft's AZ-802 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-802)

[AZ-204](https://learn.microsoft.com/en-us/credentials/support/credential-retirement)
retired on July 31, 2026, and
[AZ-500](https://learn.microsoft.com/en-us/credentials/certifications/azure-security-engineer/)
retired on August 31, 2026. They are not new study targets. The current successor
paths are [AI-200](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-cloud-developer-associate/)
and [SC-500](https://learn.microsoft.com/en-us/credentials/certifications/cloud-and-ai-security-engineer-associate/),
respectively; these are new credentials rather than an assertion that an earned
retired credential converts automatically.

### HashiCorp

The November 23 inventory covers five HashiCorp credentials.

- Terraform Associate (004)
- Terraform Infrastructure Engineer Professional (002)
- Terraform Authoring and Operations Advanced
- Vault Associate (003)
- Vault Operations Advanced (repository key `VAULT-OPERATIONS-PROFESSIONAL`)

Infrastructure Engineer Professional is a multiple-choice exam based on Terraform
1.15. Authoring and Operations Advanced is the lab-based credential with AWS and
Azure delivery options. The inventory gives each assessment its own query key.
[HashiCorp catalog](https://developer.hashicorp.com/certifications) · [Assessment and version evidence](research/2026-11-23-refresh-21.md)

### Databricks

The scope is all seven credentials on the official [Databricks certification
catalog](https://www.databricks.com/learn/certification). All seven are
registered: Data Analyst Associate, both Data Engineer levels, both Machine
Learning levels, Generative AI Engineer Associate, and Associate Developer for
Apache Spark.
Databricks does not display short codes for them, so the uppercase identifiers
are stable library and downstream-query keys, not vendor-issued codes. The live
HTML certification page is the monitored weighted blueprint, while each linked
PDF is preserved as the detailed objective baseline. The adapter accepts both
“The exam covers” and “This exam covers,” the two heading variants encountered
so far. Apply that live-page-plus-linked-PDF rule during every revalidation.

### AWS

The September 1 AWS exam-guide index contained 14 current or announced exam
versions. The English MLA-C01 exam retired September 28. The issuer lists
continued Japanese, Korean and Simplified Chinese delivery during the transition
to MLA-C02. Its English beta began September 29. The English SAP-C03 standard
exam launched November 17. AWS announced December 1 for the DVA-C03 transition.
The inventory tracks each version and language window separately.
[AWS transition research](research/2026-11-23-refresh-04.md) · [SAP-C03 and DVA-C03 evidence](research/2026-11-23-refresh-21.md)

### Red Hat

The selected performance-based exams cover Enterprise Linux (EX200), Ansible
(EX294), OpenShift administration (EX280), cloud-native development (EX378)
and AI (EX267). Red Hat now specifies OpenShift 4.22 for both the EX280 exam
description and its tasks. EX267 uses OpenShift AI 3.3 on OpenShift 4.20.
[Red Hat exam and training evidence](research/2026-11-23-refresh-17.md)

### CompTIA

Published guides cover Tech+ V6 (FC0-U71), A+ V15 Core 1 and Core 2
(220-1201 and 220-1202), Network+ V9 (N10-009), Security+ V7 (SY0-701),
Linux+ V8 (XK0-006) and Cloud+ V4 (CV0-004). A+ requires both cores from
the same version.

The inventory also includes Security+ V8 (SY0-801), available in English
since November 17, 2026. V7 retires June 11, 2027 in English and August 13,
2027 in Japanese, Portuguese, Spanish and Thai.
[Security+ V7](https://www.comptia.org/en-us/certifications/security/v7/) · [Security+ V8](https://www.comptia.org/en-us/certifications/security/v8/)

### Linux Foundation and CNCF

The selected exams are LFCA, LFCS, CKA, CKAD and CKS. LFCA uses multiple-choice
questions. The other four are performance-based. On November 23, the issuer
listed Kubernetes v1.37 for CKA, CKAD and CKS. CKS requires a prior CKA pass,
which may have expired. [Exam environment and prerequisite evidence](research/2026-11-23-refresh-17.md)

### NVIDIA

The selected credentials are Generative AI LLMs (NCA-GENL), AI Infrastructure
and Operations (NCA-AIIO) and AI Operations (NCP-AIO). NCP-AIO publishes 19
tasks across four domains. Multiple-choice questions and three hands-on
challenges each contribute half of the overall score. [NVIDIA professional
exam evidence](research/2026-11-23-refresh-24.md)

### MongoDB

The selected expansion is Associate Developer, Associate Data Modeler, and
Associate Atlas Administrator. MongoDB publishes exact public exam contracts
and free learning-path outlines, while detailed study guides require free
enrollment. The self-managed Associate Database Administrator remains future
breadth. The current 13-hour Atlas Administrator path supersedes the 11.5-hour
v1 path flagged for replacement May 29, 2026.

### ServiceNow

The first ServiceNow expansion is limited to the two cross-platform mainline
credentials: Certified System Administrator (CSA) and Certified Application
Developer (CAD). Their current public ServiceNow University blueprint knowledge
articles are the canonical objective sources. Product-specific Certified
Implementation Specialist credentials, micro-certifications, accreditations,
and expert programs remain future breadth and must not be inferred from these
two guides. Mainline exam completion is distinct from annual maintenance exams
and the Certification Maintenance Program fee.

### Palo Alto Networks

The September 2, 2026 role-based portfolio has 17 current public titles: two
shared foundational credentials (Cybersecurity Apprentice and Cybersecurity
Practitioner); Network Security Professional, four network specialists, and
Network Security Architect; Security Operations Professional, five Cortex
analyst/engineer specialists, and Security Operations Architect; plus Cloud
Security Professional and Cloud Security Engineer. The same two foundational
credentials are displayed under multiple platform tabs but are counted once.
Cybersecurity Apprentice is the first guide pilot because its May 2026 public
datasheet exposes a complete seven-domain weighted blueprint. Legacy PCCET,
PCNSA, PCNSE, and other retired product-era exams are not current targets.

### Fortinet

The September 2, 2026 post-transition portfolio has 19 current certifications:
NSE 1, NSE 2, NSE 3, and NSE 4 FortiOS; Secure Networking, SASE, Cloud
Security, and Security Operations tracks at each of NSE 5, NSE 6, and NSE 7;
NSE 8 Cybersecurity Expert; and the MSSP Security and OT Security industry
certifications. This inventory counts certifications, not each versioned product
exam that can satisfy a track. NSE 4 FortiOS is the first guide pilot because
its public FortiOS 7.6 Administrator exam page publishes a complete weighted
topic table. FCF, FCA, FCP, FCSS, and FCX remain in certification histories but
were replaced as the current program labels on July 15, 2026.

### Splunk

The September 2, 2026 live catalog displays 14 tracks: 11 current platform,
observability, and cyber-defense certifications plus three tracks explicitly
labeled Legacy. The Legacy Enterprise Security Admin, ITSI Admin, and SOAR
Automation Developer credentials remain valid historical records but are no
longer refreshed; they carry a distinct `legacy` inventory state rather than
being mislabeled as retired or mixed into the current queue. Splunk Certified Cybersecurity Defense
Architect remains beta/change-sensitive until Splunk resolves the difference
between its normal-looking public registration page and the still-pending beta
results timeline. [Cybersecurity Defense Analyst](../guides/SPLK-5001-splunk-certified-cybersecurity-defense-analyst.md)
is the first published guide because Splunk provides both a six-domain weighted
test blueprint and a public track with named preparation resources.

## Updating the inventory

1. Recheck each `catalog_sources` URL and apply its written `selection` rule.
2. Add, change, retire, or remove entries in `config/certification-seeds.json`.
3. Preserve retired entries only when a published guide or downstream history
   still needs the identity, and mark the lifecycle state accurately. For every
   announced or completed retirement, record its date; when the vendor identifies
   a replacement, record and validate the replacement code and official URL.
   When a credential is renamed, keep its current `title` and add confirmed former
   names to `aliases`. Keep one row per vendor/exam code; an alias is not a new exam.
   AB-100 now retains the former name without “Expert” for LMS searches.
4. Update the source's `last_verified` date.
5. Regenerate and validate:

   ```bash
   python scripts/generate_certification_list.py
   python scripts/generate_certification_lifecycle.py
   python scripts/validate_repository.py
   ```

The JSON catalog retains official URLs, lifecycle state, provenance, and review
dates. The generated text file has four tab-separated columns: `vendor_id`,
`exam_code`, `title`, and `aliases`. The first three retain their previous order.
`aliases` is a JSON array of strings, or `[]` when none are recorded. Readers that
unpack exactly three columns must be updated; header-based readers can select the
fields they need. Query the current title and each alias separately, then merge
matches under the same vendor/exam identity. A matching old course name does not
prove alignment with the current blueprint. See the example in the [repository README](https://github.com/cterpening/certification-study-library/blob/main/README.md).

Lifecycle facts live in the same catalog. Set `lifecycle.checked_on` to the date
the cited evidence was checked. Each `blueprint_updates` entry needs an
`effective_on` date, a language code and a public `source_url`; preserve both
historical and announced dates. `initial_release`, when confirmed, needs `date`,
`stage` (`beta` or `general-availability`) and `source_url`. Use optional
`initial_release.scope` for a documented language or delivery limit. Do not infer
launch, rename or exam-update dates from a page timestamp or the library review date.
Unknown values stay absent. The lifecycle page lists confirmed dated events and
counts entries still needing date research by vendor. Record conflicts and
next-pass questions in `lifecycle.notes` rather than choosing an unsupported date;
cite the supporting public URLs in `lifecycle.source_urls`. The release date
belongs to the tracked exam version, not necessarily the credential's first launch.
Use `retirement_scope` for restrictions such as “English only” and
`retirement_source_url` for the specific announcement when available.

`lifecycle_as_of` is the page's dated comparison point. Advance it deliberately
when refreshing the view; it does not claim every credential was rechecked.
Repository validation catches stale generated query and lifecycle files.
