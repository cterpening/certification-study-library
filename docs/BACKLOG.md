# Guide backlog

This file is the human-readable queue for study guides that have been selected
for production but are not yet published. It complements, rather than replaces,
the repository's machine-readable catalogs:

- `config/certification-seeds.json` is the source-backed research inventory.
- `config/exams.json` is the catalog of published guides.
- `CERTIFICATIONS.txt` is the generated query input for downstream scripts.
- [The roadmap](ROADMAP.md) defines the broader vendor scope and production
  sequence.

Before work begins on an item, recheck its official exam page, study guide,
skills baseline, beta status, and retirement or replacement announcements. A
checked item means its guide has been published and registered; it does not, by
itself, mean the guide has completed human practitioner review.

## Agreed delivery sequence

1. Produce the best public-source-safe OpenAI and Anthropic certification
   coverage possible for a partner-oriented audience. Clearly label gated
   resources and missing public objectives rather than filling gaps by
   inference.
2. Complete all seven current Databricks certification guides.
3. Pause for a portfolio, source-quality, and maintenance review before fixing
   the order of the larger expansion queue.

## Microsoft first-wave backlog

**Remaining:** 0 of 15 selected guides; reconciliation complete

**Last queue and lifecycle review:** September 1, 2026

The Microsoft guides are the current production block. Work through the groups
below before beginning the OpenAI, Anthropic, or Databricks blocks.

### Microsoft Fabric and data

- [x] **DP-700 — Implementing Data Engineering Solutions Using Microsoft
  Fabric** — [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-700)

### Security

- [x] **SC-401 — Administering Information Security in Microsoft 365** —
  [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401)

### Power Platform

- [x] **PL-300 — Microsoft Power BI Data Analyst** —
  [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-300)
- [x] **PL-400 — Microsoft Power Platform Developer** —
  [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400)
- [x] **AB-410 — Building Intelligent Applications** —
  [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-410)

### Business AI

- [x] **AB-730 — AI Business Professional** —
  [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-730)
- [x] **AB-731 — AI Transformation Leader** —
  [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-731)

### Dynamics 365 sales and service

- [x] **AB-210 — Accelerating Sales Pipelines with AI in Dynamics 365** —
  [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-210)
- [x] **AB-250 — Transforming Contact Center Experiences with AI in Dynamics
  365** — [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-250)
- [x] **MB-230 — Microsoft Dynamics 365 Customer Service Functional
  Consultant** — [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-230)

### Dynamics 365 finance, operations, and Business Central

- [x] **MB-310 — Microsoft Dynamics 365 Finance Functional Consultant** —
  [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-310)
- [x] **MB-330 — Microsoft Dynamics 365 Supply Chain Management Functional
  Consultant** — [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-330)
- [x] **MB-500 — Microsoft Dynamics 365: Finance and Operations Apps
  Developer** — [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-500)
- [x] **MB-800 — Microsoft Dynamics 365 Business Central Functional
  Consultant** — [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-800)
- [x] **MB-820 — Microsoft Dynamics 365 Business Central Developer** —
  [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-820)

Microsoft Office Specialist and Microsoft Certified Educator credentials are
intentionally deferred. None of the 15 queued exams was identified on
Microsoft's [scheduled credential-retirement
list](https://learn.microsoft.com/en-us/credentials/support/credential-retirement)
during the September 1, 2026 review; that status must still be checked again
before each guide is started.

The final September 1 reconciliation also checked Microsoft's [retired exam
list](https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams).
MB-335 and MB-700 are not missing current exams: both retired June 30, 2026,
along with PL-500 and PL-600. AZ-204 and MB-280 retired July 31; AZ-500 and
PL-200 retired August 31. They remain useful historical identities but are not
new current-study targets under the inventory rule. The earnable AZ-800,
AZ-801, and MS-102 retirements and their known transitions are already covered.

## Partner AI backlog

- [x] **OpenAI — AI Foundations certification coverage.** Recheck the
  [official certification announcement](https://openai.com/index/openai-certificate-courses/)
  and any stable public assessment contract. If a complete public blueprint is
  still unavailable, publish a clearly labeled certification reference and
  learning map instead of inventing exam objectives. Published September 1,
  2026 as a [provisional partner reference](partner-ai/openai-ai-foundations.md);
  it remains outside the exam catalog until the public contract stabilizes.
- [x] **Anthropic — Claude Certified Architect, Foundations coverage.** Build the most
  useful partner-oriented, public-source-safe reference supported by the
  [partner-program announcement](https://www.anthropic.com/news/services-track-partner-hub),
  public Anthropic documentation, and publicly visible course metadata. Mark
  partner login requirements explicitly. Do not reproduce gated partner
  objectives or course material in the public repository; an authorized work
  mirror can add that material separately. Published September 1, 2026 as a
  [partner-gated certification reference](partner-ai/anthropic-claude-certified-architect-foundations.md)
  using the publicly verified name and solution-architect audience.

These two items may produce constrained reference pages rather than ordinary
exam-blueprint guides. That is preferable to implying that a private or
incomplete blueprint has been independently verified.

## Databricks backlog

Revalidate the [official Databricks certification
catalog](https://community.databricks.com/t5/certifications/ct-p/databricks-certifications)
and downloadable exam guides before registering the inventory.

- [x] **Databricks Certified Data Analyst Associate** — [source-validated guide](../guides/DATABRICKS-DATA-ANALYST-ASSOCIATE-databricks-data-analyst-associate.md); October 30, 2025 detailed PDF plus live nine-domain adapter
- [x] **Databricks Certified Data Engineer Associate** — [source-validated guide](../guides/DATABRICKS-DATA-ENGINEER-ASSOCIATE-databricks-data-engineer-associate.md); May 4, 2026 detailed PDF plus live weighted-page adapter
- [ ] **Databricks Certified Data Engineer Professional**
- [ ] **Databricks Certified Machine Learning Associate**
- [ ] **Databricks Certified Machine Learning Professional**
- [ ] **Databricks Certified Generative AI Engineer Associate**
- [ ] **Databricks Certified Associate Developer for Apache Spark**

Completing this block triggers the planned portfolio checkpoint. Do not silently
promote the expansion candidates below into the active production queue before
that review.

## Expansion queue after the Databricks checkpoint

These are selected vendor targets, not yet source-backed exam inventory. Exact
codes, current titles, lifecycle states, credential prerequisites, and public
blueprint quality must be verified before guide work begins.

| Vendor | Provisional first set | Planned starting coverage |
|---|---:|---|
| Google Cloud | 7 | Cloud Digital Leader; Generative AI Leader; Associate Cloud Engineer; Professional Cloud Architect, Data Engineer, Cloud Security Engineer, and Machine Learning Engineer. Keep Professional Agentic Architect on the beta watchlist. |
| Cisco | 4 | CCST Networking, CCST Cybersecurity, CCNA, and CCNA Automation. |
| Snowflake | 4 | SnowPro Associate: Platform, SnowPro Core, Advanced Data Engineer, and Specialty: Gen AI. |
| ISC2 | 4 | CC, SSCP, CCSP, and CISSP, with exam-versus-experience requirements kept explicit. |
| NVIDIA | 3 | Generative AI LLMs, AI Infrastructure, and AI Operations. |
| Salesforce | 4 | Administrator, Platform App Builder, Platform Developer I, and Agentforce Specialist. |
| MongoDB | 3 | Associate Developer, Associate Data Modeler, and Associate Atlas Administrator. |
| ServiceNow | 2 | Certified System Administrator and Certified Application Developer, subject to a public-source access check. |

The existing AWS, Red Hat, CompTIA, and Linux Foundation targets remain in the
[roadmap](ROADMAP.md). Treat CNCF and Kubernetes credentials as a prominent
collection within the Linux Foundation provider rather than inventing a
separate certification vendor.

## Later inventory and pilot candidates

- [ ] **Palo Alto Networks:** inventory the current portfolio and select one
  public-blueprint security pilot.
- [ ] **Fortinet:** inventory the post-July 2026 NSE program and select one
  foundational or professional pilot.
- [ ] **Splunk:** inventory current versus legacy certifications and select one
  platform or security-operations pilot.
- [ ] **ISACA:** inventory CISA, CISM, and CRISC, including professional
  experience and maintenance requirements.
- [ ] **Oracle:** inventory the live OCI, database, and Java certification
  catalogs before setting a guide count; avoid carrying year-versioned retired
  exams forward from old catalog pages.
