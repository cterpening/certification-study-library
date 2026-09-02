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

These are selected vendor targets. Exact codes, current titles, lifecycle
states, credential prerequisites, and public blueprint quality must be verified
before guide work begins; rows say when that inventory has been completed.

| Vendor | Provisional first set | Planned starting coverage |
|---|---:|---|
| Google Cloud | 8 | All eight selected guides are source validated, including [Professional Agentic Architect](../guides/GOOGLE-PROFESSIONAL-AGENTIC-ARCHITECT-professional-agentic-architect.md) as a two-part beta with registration opening September 3, 2026. Revalidate its windows, lab contract, tools and eventual GA transition frequently. |
| Cisco | 4 | Complete September 2, 2026: [100-150 CCST Networking](../guides/100-150-cisco-certified-support-technician-networking.md), [100-160 CCST Cybersecurity](../guides/100-160-cisco-certified-support-technician-cybersecurity.md), [200-301 CCNA](../guides/200-301-cisco-certified-network-associate.md), and [200-901 CCNA Automation](../guides/200-901-cisco-certified-network-associate-automation.md) are source validated. CCNA v1.1 stays live through February 2, 2027 with v2.0 separately mapped; CCNA Automation uses the detailed v1.1 scope while monitoring a lagging v1.0 landing-page label. |
| Snowflake | 4 | Complete September 2, 2026: retired [SOL-C01 SnowPro Associate: Platform](../guides/SOL-C01-snowpro-associate-platform.md), active [COF-C03 SnowPro Core](../guides/COF-C03-snowpro-core.md), [DEA-C02 Advanced Data Engineer](../guides/DEA-C02-snowpro-advanced-data-engineer.md), and [GES-C02 Specialty: Gen AI](../guides/GES-C02-snowpro-specialty-gen-ai.md) are source validated. GES-C01 retired July 20 and must not be used as current. |
| ISC2 | 4 | Complete September 2, 2026: [CC](../guides/CC-isc2-certified-in-cybersecurity.md), [SSCP](../guides/SSCP-isc2-systems-security-certified-practitioner.md), [CCSP](../guides/CCSP-isc2-certified-cloud-security-professional.md), and [CISSP](../guides/CISSP-isc2-certified-information-systems-security-professional.md) are source validated against their current outlines, with exam-versus-experience, Associate, endorsement, membership and CPE requirements explicit. |
| NVIDIA | 3 | Complete September 2, 2026: [NCA-GENL Generative AI LLMs](../guides/NCA-GENL-nvidia-generative-ai-llms-associate.md), [NCA-AIIO AI Infrastructure and Operations](../guides/NCA-AIIO-nvidia-ai-infrastructure-operations-associate.md), and [NCP-AIO AI Operations](../guides/NCP-AIO-nvidia-ai-operations-professional.md) are source validated. NCP-AIO preserves the 30-question plus three-integrated-lab contract and requires Linux CLI, Slurm, Kubernetes and Base Command Manager performance practice. |
| Salesforce | 4 | Complete September 2, 2026: [Platform Administrator](../guides/SALESFORCE-PLATFORM-ADMINISTRATOR-salesforce-certified-platform-administrator.md), [Platform App Builder](../guides/SALESFORCE-PLATFORM-APP-BUILDER-salesforce-certified-platform-app-builder.md), [Platform Developer](../guides/SALESFORCE-PLATFORM-DEVELOPER-salesforce-certified-platform-developer.md), and [Agentforce Specialist](../guides/SALESFORCE-AGENTFORCE-SPECIALIST-salesforce-certified-agentforce-specialist.md) are source validated. Agentforce tracks the Spring ’26 outline separately from weekly product and maintenance changes. |
| MongoDB | 3 | Complete September 2, 2026: [Associate Developer](../guides/MONGODB-ASSOCIATE-DEVELOPER-mongodb-associate-developer.md), [Associate Data Modeler](../guides/MONGODB-ASSOCIATE-DATA-MODELER-mongodb-associate-data-modeler.md), and [Associate Atlas Administrator](../guides/MONGODB-ASSOCIATE-ATLAS-ADMINISTRATOR-mongodb-associate-atlas-administrator.md) are published. Atlas Administrator maps all 13 public path skills but retains an enrolled detailed-objective reconciliation gate; no hidden weights are invented. The self-managed Associate Database Administrator is future breadth. |
| ServiceNow | 2 | Complete September 2, 2026: [Certified System Administrator](../guides/SERVICENOW-CSA-servicenow-certified-system-administrator.md) and [Certified Application Developer](../guides/SERVICENOW-CAD-servicenow-certified-application-developer.md) are source validated against KB0011554 and KB0011498. CAD preserves the mainline-versus-MeasureUp weighting discrepancy, and both list only official MeasureUp for exam-style practice. |

The existing AWS, Red Hat, CompTIA, and Linux Foundation targets remain in the
[roadmap](ROADMAP.md). Treat CNCF and Kubernetes credentials as a prominent
collection within the Linux Foundation provider rather than inventing a
separate certification vendor.

## Later inventory and pilot candidates

- [x] **Palo Alto Networks:** 17-title role-based portfolio inventoried and
  [Cybersecurity Apprentice](../guides/PANW-CYBERSECURITY-APPRENTICE-palo-alto-networks-cybersecurity-apprentice.md)
  published September 2, 2026 from the May 2026 seven-domain datasheet.
- [x] **Palo Alto Networks Certified Cybersecurity Practitioner:** 6-domain source-validated guide with
  applied scenarios, authorized labs, original checks, and a selective learning map.
- [x] **Palo Alto Networks Certified Cloud Security Professional:** 5-domain source-validated guide with
  applied scenarios, authorized labs, original checks, and a selective learning map.
- [x] **Palo Alto Networks Certified Network Security Professional:** 6-domain source-validated guide with
  applied scenarios, authorized labs, original checks, and a selective learning map.
- [x] **Palo Alto Networks Certified Security Operations Professional:** 5-domain source-validated guide with
  applied scenarios, authorized labs, original checks, and a selective learning map.
- [x] **Palo Alto Networks Certified Network Security Analyst:** 4-domain source-validated guide with applied scenarios, authorized labs, original checks, related-item context, and a selective learning map.
- [x] **Palo Alto Networks Certified XSIAM Analyst:** 6-domain source-validated guide with applied scenarios, authorized labs, original checks, related-item context, and a selective learning map.
- [x] **Palo Alto Networks Certified XDR Analyst:** 4-domain source-validated guide with applied scenarios, authorized labs, original checks, related-item context, and a selective learning map.
- [x] **Palo Alto Networks Certified Cloud Security Engineer:** 6-domain source-validated guide with applied scenarios, authorized labs, original checks, related-item context, and a selective learning map.
- [x] **Palo Alto Networks Certified Next-Generation Firewall Engineer:** 3-domain source-validated guide with applied scenarios, authorized labs, original checks, related-item context, and a selective learning map.
- [x] **Palo Alto Networks Certified SD-WAN Engineer:** 5-domain source-validated guide with applied scenarios, authorized labs, original checks, related-item context, and a selective learning map.
- [x] **Palo Alto Networks Certified Security Service Edge Engineer:** 5-domain source-validated guide with applied scenarios, authorized labs, original checks, related-item context, and a selective learning map.
- [x] **Palo Alto Networks Certified XDR Engineer:** 5-domain source-validated guide with applied scenarios, authorized labs, original checks, related-item context, and a selective learning map.
- [x] **Palo Alto Networks Certified XSIAM Engineer:** 4-domain source-validated guide with applied scenarios, authorized labs, original checks, related-item context, and a selective learning map.
- [x] **Palo Alto Networks Certified XSOAR Engineer:** 5-domain source-validated guide with applied scenarios, authorized labs, original checks, related-item context, and a selective learning map.
- [x] **Palo Alto Networks Certified Network Security Architect:** 10-domain source-validated guide with applied scenarios, authorized labs, original checks, related-item context, and a selective learning map.
- [x] **Palo Alto Networks Certified Security Operations Architect:** 3-domain source-validated guide with applied scenarios, authorized labs, original checks, related-item context, and a selective learning map.
- [x] **Fortinet:** 19-certification post-July 2026 NSE portfolio inventoried
  and [NSE 4 FortiOS](../guides/NSE-4-FORTIOS-fortinet-nse-4-fortios.md)
  published September 2, 2026 from the detailed FortiOS 7.6 Administrator page.
- [x] **Fortinet NSE 7 in Secure Networking:** 5-group public-scope guide with applied scenarios, authorized labs, original checks, related-item context, and timed learning resources.
- [x] **Fortinet NSE 7 in SASE:** 5-group public-scope guide with applied scenarios, authorized labs, original checks, related-item context, and timed learning resources.
- [x] **Fortinet NSE 7 in Cloud Security:** 4-group public-scope guide with applied scenarios, authorized labs, original checks, related-item context, and timed learning resources.
- [x] **Fortinet NSE 7 in Security Operations:** 4-group public-scope guide with applied scenarios, authorized labs, original checks, related-item context, and timed learning resources.
- [x] **Fortinet NSE 8 Cybersecurity Expert:** 16-group public-scope guide with applied scenarios, authorized labs, original checks, related-item context, and timed learning resources.
- [x] **Fortinet NSE 1 in Cybersecurity:** 10-group public-scope guide with applied scenarios, authorized labs, original checks, related-item context, and timed learning resources.
- [x] **Fortinet NSE 2 in Cybersecurity:** 9-group public-scope guide with applied scenarios, authorized labs, original checks, related-item context, and timed learning resources.
- [x] **Fortinet NSE 3 in Cybersecurity:** 20-group public-scope guide with applied scenarios, authorized labs, original checks, related-item context, and timed learning resources.
- [x] **Fortinet NSE 5 in Secure Networking:** 3-group public-scope guide with applied scenarios, authorized labs, original checks, related-item context, and timed learning resources.
- [x] **Fortinet NSE 5 in SASE:** 5-group public-scope guide with applied scenarios, authorized labs, original checks, related-item context, and timed learning resources.
- [x] **Fortinet NSE 5 in Cloud Security:** 3-group public-scope guide with applied scenarios, authorized labs, original checks, related-item context, and timed learning resources.
- [x] **Fortinet NSE 5 in Security Operations:** 4-group public-scope guide with applied scenarios, authorized labs, original checks, related-item context, and timed learning resources.
- [x] **Fortinet NSE 6 in Secure Networking:** 9-group public-scope guide with applied scenarios, authorized labs, original checks, related-item context, and timed learning resources.
- [x] **Fortinet NSE 6 in SASE:** 14-group public-scope guide with applied scenarios, authorized labs, original checks, related-item context, and timed learning resources.
- [x] **Fortinet NSE 6 in Cloud Security:** 12-group public-scope guide with applied scenarios, authorized labs, original checks, related-item context, and timed learning resources.
- [x] **Splunk inventory:** 14 tracks recorded—11 current and three Legacy.
  Cybersecurity Defense Architect is publicly schedulable and its live page no
  longer displays the earlier beta label; that status change is documented.
- [x] **Splunk pilot:** [Cybersecurity Defense Analyst (SPLK-5001)](../guides/SPLK-5001-splunk-certified-cybersecurity-defense-analyst.md)
  published from its six-domain public blueprint and named learning track.
- [x] **Splunk Core Certified User:** eight-domain source-validated guide,
  practical search-to-alert evidence path, and complete public learning map.
- [x] **Splunk Core Certified Power User:** ten-domain source-validated guide
  connecting SPL transformation and correlation to reusable knowledge objects.
- [x] **Splunk Core Certified Advanced Power User:** 22-domain source-validated guide with
  applied scenarios, safe labs, original checks, and a complete learning map.
- [x] **Splunk Cloud Certified Admin:** 13-domain source-validated guide with
  applied scenarios, safe labs, original checks, and a complete learning map.
- [x] **Splunk Enterprise Certified Admin:** 17-domain source-validated guide with
  applied scenarios, safe labs, original checks, and a complete learning map.
- [x] **Splunk Enterprise Certified Architect:** 20-domain source-validated guide with
  applied scenarios, safe labs, original checks, and a complete learning map.
- [x] **Splunk Core Certified Consultant:** 9-domain source-validated guide with
  applied scenarios, safe labs, original checks, and a complete learning map.
- [x] **Splunk O11y Cloud Certified Metrics User:** 8-domain source-validated guide with
  applied scenarios, safe labs, original checks, and a complete learning map.
- [x] **Splunk Certified Cybersecurity Defense Engineer:** 5-domain source-validated guide with
  applied scenarios, safe labs, original checks, and a complete learning map.
- [x] **Splunk Certified Cybersecurity Defense Architect:** 8-domain source-validated guide with
  applied scenarios, safe labs, original checks, and a complete learning map.
- [x] **ISACA inventory:** CISA, CISM, and CRISC recorded September 2, 2026.
  Publish each guide with the exam-versus-certification experience and
  maintenance contract explicit. CISM changes outline November 3, 2026; do
  not infer the replacement weights before ISACA publishes them.
- [x] **CISA — Certified Information Systems Auditor:** source-validated
  five-domain guide with exam-versus-designation, audit evidence, three
  scenarios, eight labs, and 40 checks.
- [x] **CISM — Certified Information Security Manager:** source-validated
  current-outline guide with a prominent November 3, 2026 transition boundary.
- [x] **CRISC — Certified in Risk and Information Systems Control:**
  source-validated effective-2025 guide. The selected ISACA family is complete.
- [ ] **Oracle:** inventory the live OCI, database, and Java certification
  catalogs before setting a guide count; avoid carrying year-versioned retired
  exams forward from old catalog pages.
- [x] **Python Institute/OpenEDG inventory:** ten current exam versions recorded
  September 2, 2026 across programming, data, testing, security, automation,
  and AI. PCEA-30-01 remains explicitly beta/small-market-trial; ten announced
  or in-development exam versions and tracks remain watch items, not current
  certification rows.
- [x] **Python Institute/OpenEDG pilot:** PCEP-30-02 published from its detailed
  public syllabus, with the announced PCEP-30-03 Q3 2026 transition separated
  from the currently active exam. Treat course badges and completion
  certificates as learning resources rather than certifications. PCAP-31-03 is
  now also published, with PCAP-31-04 retained as a separate transition watch;
  PCPP-32-101 completes the current general-purpose programming ladder while
  the in-development PCPP-32-102 remains a separate watch item. PCED-30-02 now
  starts the Python Institute data-science specialization and PCAD-31-02 now
  completes its currently available associate step; both guides explicitly
  separate their retired predecessors and keep PCPD as in-development.
  PCET-30-01 now starts the testing specialization while preserving the
  provider's 30-01/30-02 syllabus-text inconsistency as a verification warning;
  PCAT-31-01 completes the currently available associate step while keeping
  in-development PCAT-31-02 separate. PCES-30-01 now adds the active security
  entry point, with practice-test and PCAS release language kept as dated watch
  items rather than assumed availability. PCEA-30-01 now covers automation but
  remains explicitly labeled beta because its credential page and syllabus
  disagree on lifecycle status. PCEI-30-01 completes the current entry-level
  specialty set and flags its mislabeled objective plus unreconciled 2026
  practice-test/PCAI announcements.
- [x] **C++ and JS Institute inventories:** six active C/C++ exams and four
  active JavaScript/web-development exams recorded September 2, 2026, with
  retired versions and course-completion certificates excluded.
- [x] **Adjacent programming pilots:** CPE-20-01 is published from its weighted
  four-block public syllabus and JSE-40-01 from its six-block public scope.
  CLE-10-01 now extends the C/C++ family with a source-validated eight-block
  entry-level C guide, and JSA-41-01 adds all 40 weighted associate JavaScript
  objectives with runnable object, class, built-in and asynchronous practice.
  WDE-40-01 is now published from its five-block HTML, form, CSS, modern-platform
  and accessibility syllabus; WDA-41-01 completes the active JS Institute
  portfolio with responsive layout, accessibility, performance and production
  quality practice. CLA-11-03 advances the C ladder with weighted multi-file,
  storage, pointer, preprocessor and stream-I/O coverage; CLP-12-01 completes the
  C track with version-aware systems, concurrency, numeric and socket practice.
  CPA-21-02 advances the C++ ladder with a source-validated object-oriented,
  exception, ownership and polymorphism guide; CPP-22-02 completes the active
  C++ ladder while explicitly preserving its source page's count/weight and
  aligned-course version discrepancies.
  After the Oracle catalog is reconciled, use
  current Oracle Java as the first Java pilot. Do not treat course-completion
  badges as certifications.
