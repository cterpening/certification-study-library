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
| Microsoft | 35 | 50 | 15 | Selected current Microsoft catalog, excluding Microsoft Office Specialist and Microsoft Certified Educator; includes announced retirements while still earnable. |
| HashiCorp | 4 | 4 | 0 | Complete current Terraform and Vault certification catalog. |
| Databricks | 0 | 7 | 7 | All seven certifications currently listed by Databricks: Data Analyst Associate; Data Engineer Associate and Professional; Machine Learning Associate and Professional; Generative AI Engineer Associate; and Associate Developer for Apache Spark. |
| AWS | 0 | 12 | 12 | All 12 exams in the current official exam-guide index: 2 Foundational, 5 Associate, 3 Professional, and 2 Specialty. Microcredentials are out of scope. |
| OpenAI | 0 | 1 conditional | 1 conditional | AI Foundations is the only non-educator public certification candidate currently announced. Publish only after OpenAI exposes a stable public objective/assessment contract. The teacher course is deferred with other educator credentials. |
| Anthropic | 0 | 0 public / 1 watch | 0 | Claude Partner Certification exists inside the partner program, but no stable public exam blueprint was verified. Monitor and catalog public metadata; do not construct a public guide from gated material. |
| Red Hat | 0 | 5 | 5 | First wave: one anchor exam from each 2026 specialization—Enterprise Linux, Ansible, OpenShift, Cloud-native Applications, and AI. Inventory the much larger performance-based catalog before selecting exact versions. |
| CompTIA | 0 | 6 | 6 | First wave: Tech+, A+, Network+, Security+, Linux+, and Cloud+. Verify the live official catalog and component exam codes before publication. |
| Linux Foundation | 0 | 5 | 5 | First wave: LFCA, LFCS, CKA, CKAD, and CKS. The public catalog currently reports 77 certification product listings, so complete-catalog coverage is intentionally not a first-wave promise. |
| **Total** | **44** | **95** | **51** | Conditional/watch entries do not become publishable until their public source contract is sufficient. |

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

The previous sequence—finish every Microsoft guide, then start other
vendors—would leave the library Microsoft-heavy for too long. Use this order:

1. **Close the current Fabric pair:** publish DP-700 immediately after DP-600.
2. **Prove the third blueprint adapter:** publish Databricks Data Engineer
   Associate and document how its downloadable exam guide differs from
   Microsoft Learn and HashiCorp Developer.
3. **Finish the highest-value Microsoft professional cluster:** SC-401, PL-300,
   PL-400, and AB-410.
4. **Publish a cross-vendor anchor round:** AWS Cloud Practitioner, Red Hat
   RHCSA, CompTIA Security+, and Linux Foundation LFCS. Each must include the
   vendor-specific exam format; Red Hat and LFCS are performance based and must
   not be written like multiple-choice Microsoft exams.
5. **Return to Microsoft business AI:** AB-730 and AB-731, followed by AB-210
   and AB-250.
6. **Complete the selected Dynamics family:** MB-230, MB-310, MB-330, MB-500,
   MB-800, and MB-820.
7. **Expand in round-robin waves:** one coherent Databricks level/family, one
   AWS level/family, one Linux/Red Hat/CompTIA foundation, then one advanced
   guide. Revalidate existing guides between waves instead of allowing a whole
   vendor catalog to age before review.

The remaining selected Microsoft queue is therefore **15 exams**, not an open-
ended “all Microsoft” phase: DP-700, SC-401, AB-410, PL-300, PL-400, AB-730,
AB-731, AB-210, AB-250, MB-230, MB-310, MB-330, MB-500, MB-800, and MB-820.
Office Specialist and Educator credentials remain deferred.

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
- Use Databricks Data Engineer Associate as the next provider pilot to test a third blueprint format before defining a broader adapter interface.

## Phase 6: Cross-vendor anchors

- [ ] Inventory and publish Databricks Data Engineer Associate; preserve the
  downloadable official exam-guide baseline and sample-question integrity
  boundary.
- [ ] Inventory all 12 current AWS exams, then publish Cloud Practitioner as the
  AWS adapter and guide pattern.
- [ ] Inventory the five Red Hat specialization tracks and exact current exam
  versions, then publish RHCSA as the first performance-based Red Hat guide.
- [ ] Complete the live CompTIA catalog inventory and component-exam policy,
  then publish Security+ as the first CompTIA guide.
- [ ] Inventory the selected Linux Foundation first wave, then publish LFCS as
  the first Linux Foundation performance-based guide.
- [ ] Keep OpenAI AI Foundations conditional on a stable public certification
  objective/assessment contract; keep the Anthropic partner credential on the
  watchlist while its blueprint remains gated.

## Phase 7: Balanced family expansion

- [ ] Complete all seven selected Databricks guides.
- [ ] Complete all 12 current AWS certification-exam guides.
- [ ] Complete the five Red Hat specialization anchors.
- [ ] Complete the six selected CompTIA foundation/core guides.
- [ ] Complete LFCA, LFCS, CKA, CKAD, and CKS.
- [ ] Review first-wave value, usage, source quality, maintenance cost, and human
  feedback before expanding Red Hat or Linux Foundation toward their full
  catalogs.

## Work integration

The work repository remains downstream. It may add private content and reformat public guides through a private overlay or build step. Internal content, branding, and presentation rules never become dependencies of the public project.
