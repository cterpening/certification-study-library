# Roadmap

## Portfolio size and counting rule

Roadmap numbers count **planned study-guide targets**, not badges, learning
courses, product bundles, translated copies, renewal assessments, or Applied
Skills. When one credential requires more than one independently published exam,
each exam gets its own guide and counts separately. For example, the retiring
Windows Server Hybrid Administrator credential has separate AZ-800 and AZ-801
guides. CompTIA A+ will need a similar component-exam decision during inventory.

The first wave is deliberately smaller than several vendors' complete catalogs.
It gives the library meaningful cross-vendor coverage without promising dozens
of thin pages before the source adapters and human-review process have been
tested.

| Vendor | Published now | First-wave guide target | Remaining in first wave | Scope note |
|---|---:|---:|---:|---|
| GitHub | 5 | 5 | 0 | Complete current public certification family. |
| Microsoft | 44 | 50 | 6 | Selected current Microsoft catalog, excluding Microsoft Office Specialist and Microsoft Certified Educator; includes announced retirements while still earnable. |
| HashiCorp | 4 | 4 | 0 | Complete current Terraform and Vault certification catalog. |
| Databricks | 0 | 7 | 7 | All seven certifications currently listed by Databricks: Data Analyst Associate; Data Engineer Associate and Professional; Machine Learning Associate and Professional; Generative AI Engineer Associate; and Associate Developer for Apache Spark. |
| AWS | 0 | 12 | 12 | All 12 exams in the current official exam-guide index: 2 Foundational, 5 Associate, 3 Professional, and 2 Specialty. Microcredentials are out of scope. |
| OpenAI | 0 | 1 conditional | 1 conditional | AI Foundations is the only non-educator public certification candidate currently announced. Publish only after OpenAI exposes a stable public objective/assessment contract. The teacher course is deferred with other educator credentials. |
| Anthropic | 0 | 0 public / 1 watch | 0 | Claude Partner Certification exists inside the partner program, but no stable public exam blueprint was verified. Monitor and catalog public metadata; do not construct a public guide from gated material. |
| Red Hat | 0 | 5 | 5 | First wave: one anchor exam from each 2026 specialization—Enterprise Linux, Ansible, OpenShift, Cloud-native Applications, and AI. Inventory the much larger performance-based catalog before selecting exact versions. |
| CompTIA | 0 | 6 | 6 | First wave: Tech+, A+, Network+, Security+, Linux+, and Cloud+. Verify the live official catalog and component exam codes before publication. |
| Linux Foundation | 0 | 5 | 5 | First wave: LFCA, LFCS, CKA, CKAD, and CKS. The public catalog currently reports 77 certification product listings, so complete-catalog coverage is intentionally not a first-wave promise. |
| **Total** | **53** | **95** | **42** | Conditional/watch entries do not become publishable until their public source contract is sufficient. |

Counts are a dated planning baseline, not evergreen vendor facts. Recheck the
official [AWS exam-guide index](https://docs.aws.amazon.com/aws-certification/latest/examguides/aws-certification-exam-guides.html),
[Databricks certification catalog](https://community.databricks.com/t5/certifications/ct-p/databricks-certifications),
[Red Hat certification paths](https://www.redhat.com/en/services/certifications),
[Linux Foundation catalog](https://training.linuxfoundation.org/certification-catalog/),
[OpenAI certification announcement](https://openai.com/index/openai-certificate-courses/),
and [Anthropic partner-program announcement](https://www.anthropic.com/news/services-track-partner-hub)
before adding or removing targets. CompTIA remains marked inventory-required
until its live catalog can be independently enumerated from an official source.

## Recommended production order

Use this agreed sequence:

1. **Finish Microsoft:** complete the remaining 6 guides in the ordered
   [backlog](BACKLOG.md#microsoft-first-wave-backlog), including lifecycle
   revalidation immediately before each guide.
2. **Cover OpenAI for a partner audience:** use the strongest public sources
   available and identify partner-restricted learning explicitly. Publish a
   normal exam guide only when a stable public objective contract supports it;
   otherwise publish an honest certification reference and learning map.
3. **Cover Anthropic for a partner audience:** follow the same public/private
   boundary. Publicly visible partner metadata may be cataloged, but gated
   partner objectives and course content belong only in an authorized downstream
   overlay.
4. **Complete Databricks:** inventory and publish all seven current
   certifications. Use Data Engineer Associate to prove the third objective
   adapter before applying it across the remaining six guides.
5. **Stop for a checkpoint:** review portfolio balance, usage, source quality,
   adapter behavior, and weekly-maintenance cost with the maintainer before
   choosing the next production order.

The remaining selected Microsoft queue is therefore **6 exams**, not an open-
ended “all Microsoft” phase. The ordered, checkable list is maintained in the
[guide backlog](BACKLOG.md). Office Specialist and Educator credentials remain
deferred.

## Expansion candidates after the Databricks checkpoint

These targets are deliberately excluded from the 95-guide first-wave total
until their exact live catalogs and public-blueprint quality are inventoried.
They are recorded now so they are not lost, but the post-checkpoint order remains
a maintainer decision.

| Vendor | Provisional first set | Rationale and source boundary |
|---|---:|---|
| Google Cloud | 7 | Add the two current foundational credentials plus associate/professional anchors across cloud, architecture, data, security, and ML. Google publishes exam guides and a dedicated learning path for each certification. Keep Professional Agentic Architect on the beta watchlist. |
| Cisco | 4 | Start with CCST Networking, CCST Cybersecurity, CCNA, and CCNA Automation. Cisco publishes exam topics and substantial official lab/training options. |
| Snowflake | 4 | Start with SnowPro Associate: Platform, Core, Advanced Data Engineer, and Specialty: Gen AI to complement Fabric and Databricks. |
| ISC2 | 4 | Start with CC, SSCP, CCSP, and CISSP. Separate exam readiness from the work-experience and endorsement requirements for earning each credential. |
| NVIDIA | 3 | Start with Generative AI LLMs, AI Infrastructure, and AI Operations where weighted public blueprints and mapped training are available. |
| Salesforce | 4 | Start with Administrator, Platform App Builder, Platform Developer I, and Agentforce Specialist; account for Salesforce's frequent release and maintenance cycle. |
| MongoDB | 3 | Start with Associate Developer, Associate Data Modeler, and Associate Atlas Administrator, supported by free official learning paths. |
| ServiceNow | 2 | Pilot Certified System Administrator and Certified Application Developer only after confirming that enough objective and product material is publicly accessible. |

Recheck the official [Google Cloud](https://cloud.google.com/learn/certification),
[Cisco](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/index.html),
[Snowflake](https://learn.snowflake.com/en/certifications/),
[ISC2](https://www.isc2.org/certifications),
[NVIDIA](https://www.nvidia.com/en-us/learn/certification/),
[Salesforce](https://trailhead.salesforce.com/en/credentials),
[MongoDB](https://learn.mongodb.com/pages/certification-program), and
[ServiceNow](https://www.servicenow.com/university/training-and-certification.html)
catalogs during formal inventory.

Later pilots are Palo Alto Networks, Fortinet, Splunk, and the CISA/CISM/CRISC
ISACA family. Oracle remains inventory-required because its OCI, database, and
Java catalogs are broad and version-sensitive. Kubernetes and CNCF credentials
remain under the Linux Foundation provider, with their own visible collection.
See the [backlog](BACKLOG.md#later-inventory-and-pilot-candidates) for the
checkable list.

## Phase 1: GitHub reference implementation

- Seed the five GitHub certification guides.
- Register the exams, vendors, canonical blueprints, and review state.
- Monitor Microsoft Learn objective changes.
- Validate guide paths, metadata, Markdown structure, and local links.
- Keep all guides explicitly marked as independent AI-generated drafts until reviewed.

## Phase 2: Source and coverage review

- Register the individual public sources already cited by the seed guides.
- Map published objectives to guide sections and supporting sources.
- Normalize guide structure and depth using `docs/GUIDE-QUALITY-STANDARD.md`; continue closing objective-level gaps independently of raw page length.
- Review material claims and promote guides independently to **SOURCE-VALIDATED**.
- [x] Establish machine-readable review evidence and promote GH-900 and GH-300 after source validation.
- [x] Deepen and source-validate all five GitHub certification guides.
- [x] Add structured correction/source forms and weekly source-health monitoring.
- Add alternative learning formats where they materially help, such as concise reviews, diagrams, and labs.
- Record known gaps without ranking one learning style as universally best.

## Phase 3: Public site

- [x] Add a searchable static-site configuration.
- [x] Generate navigation and guide cards from the exam catalog.
- [x] Group every generated guide listing by beginner, intermediate/specialty,
  and expert/professional level, then sort naturally by exam code within each
  group.
- [x] Show provenance, freshness, review state, and **VERIFY CURRENT** warnings prominently.
- [x] Add a strict site build and generated-link validation.
- [ ] Complete keyboard, contrast, mobile, screen-reader, and print review.
- [x] Add and approve the GitHub Pages deployment workflow.
- [x] Normalize guide headings, constrain the visible table of contents to major sections, simplify provider navigation, and add a homepage skip target.
- [x] Clarify the sources-and-objectives quality gate and publish a maintainer/About page.
- Obtain complete external practitioner reviews of GH-300, AZ-104, and Terraform Associate (004) before labeling any of them community reviewed.
- Submit the public sitemap to Google Search Console and Bing Webmaster Tools after account-level site verification.

## Phase 4: Microsoft expansion (in progress)

- [x] Inventory every current certification in Microsoft Learn's Azure product facet, preserving one enrichment row per required exam.
- Add a weekly discovery check that reports additions, removals, code changes, and lifecycle changes in the Azure and HashiCorp catalogs without editing the inventory automatically.
- [x] Build and source-validate the selected Azure guides from the research inventory; inventory presence is not publication.
- [x] Deepen and source-validate AI-103 and AB-100 as engineering- and architecture-exam patterns.
- [x] Cover all active Microsoft 900/901 Fundamentals exams as of August 31, 2026: AZ-900, DP-900, PL-900, SC-900, AB-900, and AI-901.
- [x] Complete source validation of the Microsoft first drafts.
- Complete practitioner review of the Microsoft guides.
- [x] Establish the Azure fundamentals depth and source-validation pattern with AZ-900.
- [x] Deepen and source-validate DP-900 against the July 21, 2026 objective baseline.
- [x] Deepen and source-validate AI-901 as the active replacement for retired AI-900.
- [x] Deepen and source-validate SC-900 against the July 28, 2026 objective baseline.
- [x] Deepen and source-validate PL-900 against the July 24, 2026 objective baseline.
- [x] Deepen and source-validate AB-900 against the July 22, 2026 objective baseline.
- Revisit breadth only when Microsoft publishes or retires a 900/901 credential; AI-900 retired June 30, 2026 and is replaced here by AI-901.
- [x] Add a genuinely different blueprint platform before generalizing discovery adapters, using HashiCorp Terraform Associate (004) as the pilot.
- [x] Extract the first shared objective-monitor boundary from demonstrated Microsoft Learn and HashiCorp Developer differences.

## Phase 5: Vendor-neutral pilot (in progress)

- [x] Inventory all four current HashiCorp certifications: Terraform Associate (004), Terraform Authoring and Operations Professional, Vault Associate (003), and Vault Operations Professional.
- [x] Build and source-validate the remaining Terraform and Vault guides one at a time.
- [x] Generate provider navigation, cards, catalogs, and labels from `data/vendors.json` rather than fixed GitHub/Microsoft lists.
- [x] Add HashiCorp Terraform Associate (004) as the first non-Microsoft-platform guide.
- [x] Support provider-published objective maps that do not include percentage weights.
- [x] Add and test a HashiCorp Developer objective adapter alongside the Microsoft Learn adapter.
- [x] Complete source validation of the Terraform Associate draft.
- Complete practitioner review of the Terraform Associate guide.
- After the partner AI block, use Databricks Data Engineer Associate as the next provider pilot to test a third blueprint format before defining a broader adapter interface.

## Phase 6: Partner AI and Databricks checkpoint

- [ ] Complete the remaining Microsoft backlog.
- [ ] Produce the strongest public-source-safe OpenAI certification coverage
  available, with partner access and blueprint gaps labeled.
- [ ] Produce the strongest public-source-safe Anthropic partner-certification
  coverage available without copying gated content.
- [ ] Inventory and publish all seven Databricks certifications; preserve the
  downloadable official exam-guide baselines and sample-question integrity
  boundary.
- [ ] Complete the portfolio and maintenance checkpoint before choosing the
  next vendor sequence.

## Phase 7: Cross-vendor anchors after checkpoint

- [ ] Inventory Google Cloud and select the exact seven-guide first set; keep
  the announced Agentic Architect beta separate until its contract stabilizes.
- [ ] Inventory Cisco, Snowflake, ISC2, NVIDIA, Salesforce, MongoDB, and
  ServiceNow before promoting their provisional anchors into the source-backed
  certification inventory.
- [ ] Inventory all 12 current AWS exams, then publish Cloud Practitioner as the
  AWS adapter and guide pattern.
- [ ] Inventory the five Red Hat specialization tracks and exact current exam
  versions, then publish RHCSA as the first performance-based Red Hat guide.
- [ ] Complete the live CompTIA catalog inventory and component-exam policy,
  then publish Security+ as the first CompTIA guide.
- [ ] Inventory the selected Linux Foundation first wave, then publish LFCS as
  the first Linux Foundation performance-based guide.

## Phase 8: Balanced family expansion

- [ ] Complete all 12 current AWS certification-exam guides.
- [ ] Complete the five Red Hat specialization anchors.
- [ ] Complete the six selected CompTIA foundation/core guides.
- [ ] Complete LFCA, LFCS, CKA, CKAD, and CKS.
- [ ] Review first-wave value, usage, source quality, maintenance cost, and human
  feedback before expanding Red Hat or Linux Foundation toward their full
  catalogs.

## Work integration

The work repository remains downstream. It may add private content and reformat public guides through a private overlay or build step. Internal content, branding, and presentation rules never become dependencies of the public project.
