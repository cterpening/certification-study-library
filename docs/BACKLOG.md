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
  2026 as a [limited-access certification reference](partner-ai/openai-ai-foundations.md).
  OpenAI Certified is now publicly documented as invite-only for eligible
  Enterprise/Edu workspaces, while the similarly named public Academy course
  issues a completion certificate rather than an OpenAI Certification. The
  reference remains outside the exam catalog until the public blueprint and
  assessment/lifecycle contract stabilize.
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
- [x] **Databricks Certified Data Engineer Professional** — [source-validated guide](../guides/DATABRICKS-DATA-ENGINEER-PROFESSIONAL-databricks-data-engineer-professional.md); July 3, 2026 detailed live-version PDF plus current ten-domain adapter
- [x] **Databricks Certified Machine Learning Associate** — [source-validated guide](../guides/DATABRICKS-MACHINE-LEARNING-ASSOCIATE-databricks-machine-learning-associate.md); March 1, 2025 live-version PDF with explicit current-terminology translation
- [x] **Databricks Certified Machine Learning Professional** — [source-validated guide](../guides/DATABRICKS-MACHINE-LEARNING-PROFESSIONAL-databricks-machine-learning-professional.md); September 30, 2025 live-version PDF with current bundle/monitoring translation
- [x] **Databricks Certified Generative AI Engineer Associate** — [source-validated guide](../guides/DATABRICKS-GENERATIVE-AI-ENGINEER-ASSOCIATE-databricks-generative-ai-engineer-associate.md); March 18, 2026 live-version PDF plus current six-domain adapter, with volatile agent/MCP/Apps/AI Search boundaries
- [x] **Databricks Certified Associate Developer for Apache Spark** — [source-validated guide](../guides/DATABRICKS-ASSOCIATE-DEVELOPER-APACHE-SPARK-databricks-associate-developer-apache-spark.md); October 30, 2025 live-version PDF plus current seven-domain adapter, explicitly separated from the retired Spark 3.0 exam

Completing this block triggers the planned portfolio checkpoint. Do not silently
promote the expansion candidates below into the active production queue before
that review.

## Active first-wave backlog

The maintainer selected this exact first wave after the Databricks checkpoint on
September 1, 2026. These 31 exam/version guides are now source-backed research
inventory. Build, validate, commit, and push them one at a time.

### AWS — 14 guides

- [x] **AIB-C01 — AWS Certified AI Business Strategist** — [source-validated beta guide](../guides/AIB-C01-aws-certified-ai-business-strategist.md); initial September 1, 2026 four-domain blueprint, September 29 beta-delivery warning, business-decision frameworks, eight labs and launch-day learning-catalog boundary
- [x] **AIF-C01 — AWS Certified AI Practitioner** — [source-validated guide](../guides/AIF-C01-aws-certified-ai-practitioner.md); March 26, 2026 revision with explicit agentic AI, MCP, Amazon Quick, Kiro, Strands Agents and Bedrock AgentCore freshness boundary
- [x] **CLF-C02 — AWS Certified Cloud Practitioner** — [source-validated guide](../guides/CLF-C02-aws-certified-cloud-practitioner.md); current four-domain official guide, 65-question delivery contract, service-decision depth, eight labs and dated learning options
- [x] **SOA-C03 — AWS Certified CloudOps Engineer - Associate** — [source-validated guide](../guides/SOA-C03-aws-certified-cloudops-engineer-associate.md); current five-domain CloudOps baseline, explicit SOA-C02 gap boundary, operational evidence/remediation depth, three scenarios, eight labs and 40 original checks
- [x] **DEA-C01 — AWS Certified Data Engineer - Associate** — [source-validated guide](../guides/DEA-C01-aws-certified-data-engineer-associate.md); December 2025 version 1.1 baseline, explicit older-course gap map, three scenarios, eight labs and 40 original checks
- [x] **DVA-C02 — AWS Certified Developer - Associate** — [source-validated guide](../guides/DVA-C02-aws-certified-developer-associate.md); version 2.1 additions, scored-versus-emerging-topic boundary, three scenarios, eight labs and 40 original checks
- [x] **MLA-C01 — AWS Certified Machine Learning Engineer - Associate** — [source-validated retiring guide](../guides/MLA-C01-aws-certified-machine-learning-engineer-associate.md); complete traditional-ML/MLOps lifecycle, three scenarios, eight labs and 40 original checks, with the September 28 English cutoff and MLA-C02/ME1-C02 transition prominent
- [x] **MLA-C02 — AWS Certified Machine Learning Engineer - Associate (beta)** — [source-validated launch-day guide](../guides/MLA-C02-aws-certified-machine-learning-engineer-associate.md); complete September 1 blueprint and C01 delta, traditional ML plus FM/RAG/agent/LLMOps depth, three scenarios, eight labs and 42 original checks; scheduled as ME1-C02 beginning September 29
- [x] **SAA-C03 — AWS Certified Solutions Architect - Associate** — [source-validated guide](../guides/SAA-C03-aws-certified-solutions-architect-associate.md); current four-domain baseline, end-to-end architecture tradeoffs, three scenarios, eight labs and 42 original checks
- [x] **DOP-C02 — AWS Certified DevOps Engineer - Professional** — [source-validated guide](../guides/DOP-C02-aws-certified-devops-engineer-professional.md); six-domain automation/operations baseline, three scenarios, eight labs and 42 original checks
- [x] **AIP-C01 — AWS Certified Generative AI Developer - Professional** — [source-validated guide](../guides/AIP-C01-aws-certified-generative-ai-developer-professional.md); current post-beta five-domain baseline, governed production GenAI lifecycle, three scenarios, eight labs and 42 original checks
- [x] **SAP-C02 — AWS Certified Solutions Architect - Professional** — [source-validated guide](../guides/SAP-C02-aws-certified-solutions-architect-professional.md); current four-domain enterprise architecture baseline, separate unscored emerging-AI boundary, three scenarios, eight labs and 42 original checks
- [x] **ANS-C01 — AWS Certified Advanced Networking - Specialty** — [source-validated retiring guide](../guides/ANS-C01-aws-certified-advanced-networking-specialty.md); current packet-path/BGP/DNS/security baseline, three scenarios, eight labs and 42 original checks; last testing December 31, 2026 with no replacement announced
- [x] **SCS-C03 — AWS Certified Security - Specialty** — [source-validated guide](../guides/SCS-C03-aws-certified-security-specialty.md); current six-domain security baseline, explicit C02-to-C03 transition map, three scenarios, eight labs and 42 original checks

### Red Hat — 5 guides

- [x] **EX200 — Red Hat Certified System Administrator** — [source-validated guide](../guides/EX200-red-hat-certified-system-administrator.md); RHEL 10 public baseline, ten task groups, three scenarios, eight performance labs and 40 original checks
- [x] **EX267 — Red Hat Certified Developer in AI** — [source-validated guide](../guides/EX267-red-hat-certified-developer-in-ai.md); OpenShift AI 3.3 on OpenShift 4.20, 12 public task groups, three lifecycle scenarios, eight labs and 40 original checks
- [x] **EX280 — Red Hat Certified System Administrator in OpenShift** — [source-validated guide](../guides/EX280-red-hat-certified-system-administrator-openshift.md); live page's 4.22/4.18 conflict and multi-version assignment preserved, nine task groups, three scenarios, eight labs and 40 original checks
- [x] **EX294 — Red Hat Certified Advanced System Administrator in Ansible** — [source-validated guide](../guides/EX294-red-hat-certified-advanced-system-administrator-ansible.md); current most-recent-product objectives, explicit purchasable-version boundary, three scenarios, eight labs and 40 original checks
- [x] **EX378 — Red Hat Certified Specialist in Cloud-native Development** — [source-validated guide](../guides/EX378-red-hat-certified-specialist-cloud-native-development.md); Red Hat Build of Quarkus 3.8, 11 coding groups, three integrated microservice scenarios, eight labs and 40 original checks

### CompTIA — 7 guides

- [x] **FC0-U71 — CompTIA Tech+ V6** — [source-validated guide](../guides/FC0-U71-comptia-tech-plus.md); six weighted domains, three cross-domain scenarios, eight safe labs, 40 original checks, and explicit FC0-U71/FC0-U71-CE lifecycle wording
- [x] **220-1201 — CompTIA A+ Core 1 V15** — [source-validated guide](../guides/220-1201-comptia-a-plus-core-1.md); five weighted domains, same-version and estimated-2028 boundaries, three support scenarios, eight labs and 40 original checks
- [x] **220-1202 — CompTIA A+ Core 2 V15** — [source-validated guide](../guides/220-1202-comptia-a-plus-core-2.md); four weighted domains, same-version and estimated-2028 boundaries, three support scenarios, eight labs and 40 original checks
- [x] **N10-009 — CompTIA Network+ V9** — [source-validated guide](../guides/N10-009-comptia-network-plus.md); five weighted domains, packet-walk model, three operational scenarios, eight authorized labs, 42 original checks, and an explicit N10-008 gap checklist
- [x] **SY0-701 — CompTIA Security+ V7** — [source-validated guide](../guides/SY0-701-comptia-security-plus.md); five weighted domains, three governance-to-operations scenarios, eight isolated/authorized labs, 42 original checks, urgent estimated-2026 lifecycle warning, and an explicit SY0-601 gap checklist
- [x] **XK0-006 — CompTIA Linux+ V8** — [source-validated guide](../guides/XK0-006-comptia-linux-plus.md); five weighted domains, cross-distribution runtime/persistence model, three administration scenarios, eight break/fix labs, 42 original checks, and an explicit XK0-005 gap checklist
- [x] **CV0-004 — CompTIA Cloud+ V4** — [source-validated guide](../guides/CV0-004-comptia-cloud-plus.md); six weighted domains, provider-neutral requirement-to-operation model, three cloud scenarios, eight safe labs, 42 original checks, and an explicit CV0-003 gap checklist

A+ requires both component exams from the same version. The two independently
published objective maps therefore receive separate guides even though they
lead to one credential.

### Linux Foundation and CNCF — 5 guides

- [x] **LFCA — Linux Foundation Certified IT Associate** — [source-validated guide](../guides/LFCA-linux-foundation-certified-it-associate.md); September 16, 2025 six-domain baseline, three integrated scenarios, eight labs, 40 original checks, and explicit retired LFCA-JP/old-project-domain boundaries
- [x] **LFCS — Linux Foundation Certified System Administrator** — [source-validated guide](../guides/LFCS-linux-foundation-certified-system-administrator.md); five weighted performance domains, three integrated operations scenarios, eight timed labs, 40 original checks and distribution-independent persistence/recovery discipline
- [x] **CKA — Certified Kubernetes Administrator** — [source-validated guide](../guides/CKA-certified-kubernetes-administrator.md); Kubernetes 1.35 baseline, five weighted performance domains, three integrated scenarios, eight labs, 40 original checks and explicit quarterly version watch
- [x] **CKAD — Certified Kubernetes Application Developer** — [source-validated guide](../guides/CKAD-certified-kubernetes-application-developer.md); Kubernetes 1.35 baseline, five weighted performance domains, three integrated application scenarios, eight labs, 40 original checks and explicit quarterly version watch
- [x] **CKS — Certified Kubernetes Security Specialist** — [source-validated guide](../guides/CKS-certified-kubernetes-security-specialist.md); Kubernetes 1.35 live-page baseline, six defensive performance domains, three integrated security scenarios, eight labs, 40 original checks, prior CKA pass prerequisite (active status not required), and explicit CNCF page/PDF discrepancy watch

## Expansion queue after the first-wave checkpoint

These are selected vendor targets, not yet source-backed exam inventory. Exact
codes, current titles, lifecycle states, credential prerequisites, and public
blueprint quality must be verified before guide work begins.

| Vendor | Provisional first set | Planned starting coverage |
|---|---:|---|
| Google Cloud | 8 | [Cloud Digital Leader](../guides/GOOGLE-CLOUD-DIGITAL-LEADER-cloud-digital-leader.md), [Generative AI Leader](../guides/GOOGLE-GENERATIVE-AI-LEADER-generative-ai-leader.md), and [Associate Cloud Engineer](../guides/GOOGLE-ASSOCIATE-CLOUD-ENGINEER-associate-cloud-engineer.md) are source validated; Professional Cloud Architect, Data Engineer, Cloud Security Engineer, and Machine Learning Engineer remain. Professional Agentic Architect is a published beta target with registration opening September 3, 2026. |
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
