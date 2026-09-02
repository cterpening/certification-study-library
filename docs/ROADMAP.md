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
| Microsoft | 50 | 50 | 0 | Selected queue and September 1 live-catalog/lifecycle reconciliation complete. Excludes Microsoft Office Specialist and Microsoft Certified Educator. |
| HashiCorp | 4 | 4 | 0 | Complete current Terraform and Vault certification catalog. |
| Databricks | 7 | 7 | 0 | Complete current catalog: Data Analyst, both Data Engineer and Machine Learning levels, Generative AI Engineer, and Spark Developer. |
| AWS | 14 | 14 | 0 | Complete September 1 indexed exam/version set. ANS-C01 retires December 31 with no replacement announced; MLA-C02 is an English beta scheduled as ME1-C02 beginning September 29. Microcredentials are out of scope. |
| OpenAI | 0 guides / 1 limited-access reference | 1 conditional | 1 conditional | OpenAI Certified is documented but invite-only for eligible Enterprise/Edu workspaces. The dated AI Foundations map remains outside guide counts until OpenAI exposes a stable public blueprint and fuller assessment/lifecycle contract. The separate public Academy completion course is not the certification. |
| Anthropic | 0 guides / 1 partner-gated reference | 0 public / 1 partner | 0 public | Claude Certified Architect, Foundations is publicly named and a dated partner reference is published, but its blueprint remains in Partner Academy. Public Claude Academy courses are mapped as preparation, not certification scope. Do not reconstruct gated objectives. |
| Red Hat | 5 | 5 | 0 | Complete selected set: EX200, EX267, EX280, EX294, and EX378. |
| CompTIA | 7 | 7 | 0 | Complete selected set: Tech+, both A+ V15 components, Network+, Security+, Linux+, and Cloud+. |
| Linux Foundation | 5 | 5 | 0 | Selected first wave complete: LFCA, LFCS, CKA, CKAD, and CKS. The public catalog is much larger, so complete-catalog coverage is intentionally not a first-wave promise. |
| **Total** | **97** | **98** | **1 conditional** | No actionable first-wave guide remains; the only gap is the conditional OpenAI guide awaiting a stable public blueprint, fuller assessment contract, and broader availability. |

Counts are a dated planning baseline, not evergreen vendor facts. Recheck the
official [AWS exam-guide index](https://docs.aws.amazon.com/aws-certification/latest/examguides/aws-certification-exam-guides.html),
[Databricks certification catalog](https://community.databricks.com/t5/certifications/ct-p/databricks-certifications),
[Red Hat certification paths](https://www.redhat.com/en/services/certifications),
[Linux Foundation catalog](https://training.linuxfoundation.org/certification-catalog/),
[OpenAI certification announcement](https://openai.com/index/openai-certificate-courses/),
and [Anthropic partner-program announcement](https://www.anthropic.com/news/services-track-partner-hub)
before adding or removing targets. CompTIA remains marked inventory-required
until its live catalog can be independently enumerated from an official source.

## Current production order

The Microsoft, partner-reference, and Databricks blocks are complete. Use this
next agreed sequence:

1. **AWS (complete):** maintain all 14 September 1 indexed exam/version guides;
   keep MLA-C01's September 28 retirement, MLA-C02's beta transition, and
   ANS-C01's December 31 retirement visible.
2. **Red Hat (complete):** maintain the five selected performance-based
   anchors and their explicit product-version baselines.
3. **CompTIA (complete):** maintain seven guides, treating A+ V15 Core 1 and Core 2 as
   independent exams that must be passed from the same version.
4. **Linux Foundation (complete):** maintain LFCA, LFCS, CKA, CKAD, and CKS,
   preserving the distinction between multiple-choice and performance-based
   assessments, rolling Kubernetes versions, and the previously-passed-CKA
   prerequisite for CKS.
5. **Checkpoint reached:** review value, source quality, accessibility,
   practitioner feedback, and weekly-maintenance cost before expanding again.

The selected Microsoft queue has **0 remaining exams**, and the September 1
live-catalog/lifecycle reconciliation is complete. MB-335, MB-700, PL-500, and
PL-600 retired June 30; AZ-204 and MB-280 retired July 31; AZ-500 and PL-200
retired August 31. They are not untracked current gaps. The ordered record is in
the [guide backlog](BACKLOG.md); Office Specialist and Educator credentials
remain deferred.

## Expansion candidates after the first-wave checkpoint

These targets are deliberately excluded from the 98-guide first-wave total
until their exact live catalogs and public-blueprint quality are inventoried.
They are recorded now so they are not lost, but the post-checkpoint order remains
a maintainer decision.

| Vendor | Provisional first set | Rationale and source boundary |
|---|---:|---|
| Google Cloud | 8 | All eight selected guides are source validated, including the published two-part Professional Agentic Architect beta. Revalidate that beta frequently through registration, assessment/lab windows and GA. |
| Cisco | 4 | Complete September 2, 2026: 100-150 CCST Networking, 100-160 CCST Cybersecurity, 200-301 CCNA, and 200-901 CCNA Automation are source validated. CCNA v1.1 remains current through February 2, 2027 with v2.0 separately mapped; CCNA Automation uses the detailed v1.1 PDF while monitoring a lagging v1.0 landing-page label. |
| Snowflake | 4 | Complete September 2, 2026: retired [SOL-C01 Associate: Platform](../guides/SOL-C01-snowpro-associate-platform.md), active [COF-C03 Core](../guides/COF-C03-snowpro-core.md), [DEA-C02 Advanced Data Engineer](../guides/DEA-C02-snowpro-advanced-data-engineer.md), and [GES-C02 Specialty: Gen AI](../guides/GES-C02-snowpro-specialty-gen-ai.md) are source validated. Do not carry retired COF-C02 or GES-C01 forward as current. |
| ISC2 | 4 | Complete September 2, 2026: [CC](../guides/CC-isc2-certified-in-cybersecurity.md), [SSCP](../guides/SSCP-isc2-systems-security-certified-practitioner.md), [CCSP](../guides/CCSP-isc2-certified-cloud-security-professional.md), and [CISSP](../guides/CISSP-isc2-certified-information-systems-security-professional.md) are source validated against their current outlines. Keep exam readiness separate from experience, Associate, endorsement, membership and CPE requirements. |
| NVIDIA | 3 | Complete September 2, 2026: [NCA-GENL Generative AI LLMs](../guides/NCA-GENL-nvidia-generative-ai-llms-associate.md), [NCA-AIIO AI Infrastructure and Operations](../guides/NCA-AIIO-nvidia-ai-infrastructure-operations-associate.md), and [NCP-AIO AI Operations](../guides/NCP-AIO-nvidia-ai-operations-professional.md) are source validated. NCP-AIO preserves the 30-question plus three-integrated-lab contract and requires Linux CLI, Slurm, Kubernetes and Base Command Manager performance practice. |
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

## Phase 4: Microsoft expansion (complete)

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

## Phase 5: Vendor-neutral pilot (complete)

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

- [x] Complete the remaining Microsoft backlog and lifecycle reconciliation.
- [x] Produce the strongest public-source-safe OpenAI certification coverage
  available, with partner access and blueprint gaps labeled.
- [x] Produce the strongest public-source-safe Anthropic partner-certification
  coverage available without copying gated content.
- [x] Inventory and publish all seven Databricks certifications; preserve the
  downloadable official exam-guide baselines and sample-question integrity
  boundary.
- [x] Complete the portfolio and maintenance checkpoint before choosing the
  next vendor sequence; the maintainer selected the AWS, Red Hat, CompTIA, and
  Linux Foundation first wave on September 1, 2026.

## Phase 7: First-wave inventory and provider patterns

- [x] Inventory all 14 AWS exam/version guides in the September 1 official
  index, then publish Cloud Practitioner as the AWS adapter and guide pattern.
- [x] Inventory the five Red Hat specialization anchors and current public
  product baselines, then publish RHCSA as the first Red Hat guide.
- [x] Complete the selected CompTIA inventory and adopt separate A+ Core 1 and
  Core 2 guides, then publish Tech+ as the foundational provider pattern.
- [x] Inventory LFCA, LFCS, CKA, CKAD, and CKS, then publish LFCS as the first
  Linux Foundation performance-based guide.
- [ ] Publish Google Cloud, Cisco, Snowflake, ISC2, NVIDIA, Salesforce,
  MongoDB, and ServiceNow after the completed current first wave. Google Cloud
  inventory is complete; Cloud Digital Leader, Generative AI Leader, and
  Associate Cloud Engineer, Professional Cloud Architect and Professional Data
  Engineer, Professional Cloud Security Engineer and Professional Machine
  Learning Engineer and the Professional Agentic Architect beta are source
  validated; the selected Google Cloud set is complete.
  Cisco's selected four-guide set is also complete.

## Phase 8: Balanced family expansion

- [x] Complete all 14 current AWS exam/version guides.
- [x] Complete the five Red Hat specialization anchors.
- [x] Complete the seven selected CompTIA foundation/core exam guides.
- [x] Complete LFCA, LFCS, CKA, CKAD, and CKS.
- [ ] Review first-wave value, usage, source quality, maintenance cost, and human
  feedback before expanding Red Hat or Linux Foundation toward their full
  catalogs.

## Work integration

The work repository remains downstream. It may add private content and reformat public guides through a private overlay or build step. Internal content, branding, and presentation rules never become dependencies of the public project.
