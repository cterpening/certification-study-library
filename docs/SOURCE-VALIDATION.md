# Sources-and-objectives validation records

These records document an AI-assisted quality gate: objective coverage, citations, volatility labels, link evidence, and exam-integrity checks. They do **not** claim that an independent person has reviewed every explanation or technical judgment. A guide is labeled **Community reviewed** only after a complete contributor review is recorded separately.

The internal `source-validated` state powers the repository workflow. On the public site it is deliberately displayed as **Sources + objectives checked — human review pending**. The guide was checked against the current official objective snapshot, its material explanations have supporting public sources, volatile details are marked **VERIFY CURRENT**, repository and external links validate, and the content passes the project's exam-integrity policy.

The machine-readable evidence is in [`data/reviews.json`](https://github.com/cterpening/certification-study-library/blob/main/data/reviews.json). Repository validation recomputes blueprint hashes, exact source registration, and source-health counts so a stale review record fails the build. A separate human contributor review is still required before a guide can become **COMMUNITY REVIEWED**.

## AI-agent validation workflow

An AI agent may perform the sources-and-objectives gate so the library can scale beyond what one maintainer can manually inspect. For each guide, the agent must:

1. capture the current official objective or syllabus text in a dated repository snapshot;
2. map every published objective group to specific guide sections, scenarios, and labs;
3. trace material technical claims to registered public sources, preferring the vendor blueprint and primary documentation;
4. label volatile product, delivery, pricing, availability, and lifecycle details **VERIFY CURRENT**;
5. run repository, link-health, and site validation and record the exact snapshot hash and link results; and
6. confirm that the guide contains original study material and no recalled, leaked, or copied assessment content.

Passing this workflow changes the public label to **Sources + objectives checked — human review pending**. It never produces **Community reviewed**, and it never represents vendor approval, practitioner endorsement, or a guarantee of correctness. Readers should report questionable material and use the current official blueprint as the final authority.

## Current guides that passed this gate

| Exam | Reviewed | Blueprint snapshot | External-link evidence | Result |
|---|---|---|---|---|
| GH-900 | August 31, 2026 | January 2026 objectives; unchanged during review | 69 registered links: 66 reachable, 3 access-blocked, 0 missing/error | Passed |
| GH-300 | August 31, 2026 | August 7, 2026 objectives; unchanged during review | 55 registered links: 53 reachable, 2 access-blocked, 0 missing/error | Passed |
| GH-200 | August 31, 2026 | January 2026 objectives; unchanged during review | 39 registered links: 38 reachable, 1 access-blocked, 0 missing/error | Passed |
| GH-500 | August 31, 2026 | July 2026 objectives; unchanged during review | 21 registered links: 21 reachable, 0 access-blocked, 0 missing/error | Passed |
| GH-100 | August 31, 2026 | July 2026 objectives; unchanged during review | 30 registered links: 30 reachable, 0 access-blocked, 0 missing/error | Passed |
| AI-103 | August 31, 2026 | April 16, 2026 objectives; unchanged during review | 40 registered links: 39 reachable, 1 access-blocked, 0 missing/error | Passed |
| AB-100 | August 31, 2026 | July 22, 2026 objectives; unchanged during review | 28 registered links: 24 reachable, 4 access-blocked, 0 missing/error | Passed |
| AZ-900 | August 31, 2026 | July 20, 2026 objectives; unchanged during review | 49 registered links: 48 reachable, 1 access-blocked, 0 missing/error | Passed |
| DP-900 | August 31, 2026 | July 21, 2026 objectives; unchanged during review | 39 registered links: 38 reachable, 1 access-blocked, 0 missing/error | Passed |
| PL-900 | August 31, 2026 | July 24, 2026 objectives; unchanged during review | 41 registered links: 39 reachable, 2 access-blocked, 0 missing/error | Passed |
| SC-900 | August 31, 2026 | July 28, 2026 objectives; unchanged during review | 49 registered links: 47 reachable, 2 access-blocked, 0 missing/error | Passed |
| AB-900 | August 31, 2026 | July 22, 2026 objectives; unchanged during review | 34 registered links: 31 reachable, 3 access-blocked, 0 missing/error | Passed |
| AI-901 | August 31, 2026 | April 15, 2026 objectives; unchanged during review | 26 registered links: 23 reachable, 3 access-blocked, 0 missing/error | Passed |
| Terraform Associate (004) | August 31, 2026 | Terraform 1.12 objectives; unchanged during review | 33 registered links: 31 reachable, 2 access-blocked, 0 missing/error | Passed |
| Terraform Authoring and Operations Professional | August 31, 2026 | Six-domain AWS-provider objective map; Azure-provider version announced for late 2026 | 19 registered links: 19 reachable, 0 access-blocked, 0 missing/error | Passed |
| Vault Associate (003) | August 31, 2026 | Vault 1.16, nine-domain objectives | 19 registered links: 19 reachable, 0 access-blocked, 0 missing/error | Passed |
| Vault Operations Professional | August 31, 2026 | Eight-domain Enterprise-aware lab objectives | 21 registered links: 21 reachable, 0 access-blocked, 0 missing/error | Passed |
| AZ-104 | August 31, 2026 | April 17, 2026 objectives; unchanged during review | 25 registered links: 22 reachable, 3 access-blocked, 0 missing/error | Passed |
| AZ-305 | August 31, 2026 | April 17, 2026 objectives; unchanged during review | 29 registered links: 26 reachable, 3 access-blocked, 0 missing/error | Passed |
| AZ-700 | August 31, 2026 | July 27, 2026 objectives; unchanged during review | 26 registered links: 23 reachable, 3 access-blocked, 0 missing/error | Passed |
| AZ-120 | August 31, 2026 | April 17, 2026 objectives; unchanged during review | 27 registered links: 25 reachable, 2 access-blocked, 0 missing/error | Passed |
| AZ-140 | August 31, 2026 | July 20, 2026 objectives; unchanged during review | 27 registered links: 24 reachable, 3 access-blocked, 0 missing/error | Passed |
| SC-200 | September 1, 2026 | July 28, 2026 objectives; unchanged during review | 48 registered links: 46 reachable, 2 access-blocked, 0 missing/error | Passed |
| PL-300 | September 1, 2026 | April 20, 2026 objectives; unchanged during review | 25 registered links: 22 reachable, 3 access-blocked, 0 missing/error | Passed |
| PL-400 | September 1, 2026 | March 19, 2026 objectives; unchanged during review | 19 registered links: 18 reachable, 1 access-blocked, 0 missing/error | Passed |
| AB-410 | September 1, 2026 | Official guide last updated May 15, 2026; no separate effective date; unchanged during review | 18 registered links: 17 reachable, 1 access-blocked, 0 missing/error | Passed |
| AB-730 | September 1, 2026 | July 22, 2026 objectives; unchanged during review | 11 registered links: 10 reachable, 1 access-blocked, 0 missing/error | Passed |
| AB-731 | September 1, 2026 | July 22, 2026 objectives; unchanged during review | 12 registered links: 10 reachable, 2 access-blocked, 0 missing/error | Passed |
| AB-210 | September 1, 2026 | Official guide last updated June 18, 2026; beta; no separate effective date | 12 registered links: 10 reachable, 2 access-blocked, 0 missing/error | Passed |
| AB-250 | September 1, 2026 | Official guide last updated May 15, 2026; no separate effective date | 11 registered links: 11 reachable, 0 missing/error | Passed |
| MB-230 | September 1, 2026 | March 11, 2026 objectives; credential surfaces contain stale update text | 15 registered links: 14 reachable, 1 access-blocked, 0 missing/error | Passed |
| Databricks Data Analyst Associate | September 1, 2026 | October 30, 2025 detailed PDF plus current live nine-domain weights | 27 registered links: 26 reachable, 1 access-blocked, 0 missing/error | Passed |
| Databricks Data Engineer Associate | September 1, 2026 | May 4, 2026 detailed PDF plus current live seven-domain weights | 28 registered links: 27 reachable, 1 access-blocked, 0 missing/error | Passed |
| Databricks Data Engineer Professional | September 1, 2026 | July 3, 2026 detailed live-version PDF plus current ten-domain weights | 30 registered links: 28 reachable, 2 access-blocked, 0 missing/error | Passed |
| Databricks Machine Learning Associate | September 1, 2026 | March 1, 2025 detailed live-version PDF plus current four-domain weights | 16 registered links: 15 reachable, 1 access-blocked, 0 missing/error | Passed |
| Databricks Machine Learning Professional | September 1, 2026 | September 30, 2025 detailed live-version PDF plus current three-domain weights | 17 registered links: 15 reachable, 2 access-blocked, 0 missing/error | Passed |
| Databricks Generative AI Engineer Associate | September 1, 2026 | March 18, 2026 detailed live-version PDF plus current six-domain weights | 12 registered links: 9 reachable, 3 access-blocked, 0 missing/error | Passed |
| Databricks Associate Developer for Apache Spark | September 1, 2026 | October 30, 2025 detailed live-version PDF plus current seven-domain weights | 11 registered links: 7 reachable, 4 access-blocked, 0 missing/error | Passed |
| CLF-C02 | September 1, 2026 | Current four-domain AWS guide and in-scope service list | 29 registered links: 25 reachable, 4 access-blocked, 0 missing/error | Passed |
| AIF-C01 | September 1, 2026 | Revision 1.0 dated March 26, 2026 plus current five-domain pages | 25 registered links: 23 reachable, 2 access-blocked, 0 missing/error | Passed |

Access-blocked course pages returned HTTP 403 to the automated client. An access-controlled response is recorded separately from a missing or failing page and does not establish that the resource is unavailable to a browser or subscriber.

## MB-230 coverage record

| Official objective group | Guide coverage |
|---|---|
| Manage cases in Customer Service | Section 1, all integrated scenarios, and Labs 1–5 |
| Configure representative experience and routing | Section 2, all integrated scenarios, and Labs 6–7 |
| Extend Customer Service | Section 3, warranty-support scenario, and Lab 8 |

The review maps every March 11, 2026 subobjective to a case/data/security state, knowledge/collaboration/AI contract, SLA clock/action, routing stage, representative experience, extension/feedback decision, evidence, failure or recovery path. Three scenarios, eight labs and 36 original checks cover automatic record rules and monitoring; resolution/parent-child/merge; roles and timeline; knowledge tables/lifecycle/translations/internal/external search/AI authoring; Teams chat/call/suggested contacts; filtered Ask a Question, summaries, Draft a Response, Case Management Agent and plug-in/tool controls; SLA settings/application/items/KPIs/instances/timers and reliable Power Automate actions; workstreams/users/capacity/classification/assignment/basic/skills/skill-finder/queues/record routing/diagnostics; scripts/slugs/macros; session/application-tab templates, experience profiles and Inbox; Dataverse tables/columns/relationships/forms/views/apps/search/templates/notifications; and Customer Voice trigger/personalization/correlation/governance. All 15 cited URLs are cataloged: 14 were reachable and Udemy was automation-blocked; none was missing or broken. The guide records the active 100-minute seven-language exam, no retirement date, free Practice Assessment, 29 hours 2 minutes of selected official paths, four-day course, current Pluralsight/Udemy supplements, partner-restricted learning and no exact verified O'Reilly, MeasureUp or Whizlabs product. It explicitly resolves the stale October 2025/future-tense credential-page text in favor of the dated official study guide. Blueprint SHA-256: `02105f2bbafe2b5a53a2f55604a18cdd0af2d68c842cc5d285ac8abc41a52e7e`.

## AB-250 coverage record

| Official objective group | Guide coverage |
|---|---|
| Deploy Dynamics 365 Contact Center | Section 1, all integrated scenarios, and Lab 1 |
| Implement channels | Section 2, all integrated scenarios, and Labs 2–3 and 8 |
| Configure agents and AI capabilities | Section 3, digital and voice scenarios, and Labs 3 and 5 |
| Configure work distribution | Section 4, all integrated scenarios, and Lab 4 |
| Configure the Dynamics 365 Contact Center representative experience | Section 5, all integrated scenarios, and Lab 6 |
| Manage analytics for the Dynamics 365 Contact Center | Section 6, all integrated scenarios, and Labs 7–8 |

The review maps every subobjective on the official May 15, 2026 guide to a deployment, channel/journey, identity/data/compliance boundary, agent/Copilot contract, work-distribution decision, representative/supervisor experience, operational metric, evidence, failure or recovery path. Three scenarios, eight labs and 36 original checks cover standalone/embedded/third-party CCaaS, connectors, simulation/Health/transformation agents, Agent hub/solutions/ALM/users/roles/capacity, chat/digital/SDK/API/translation, voice/IVR/numbers/calling/recording/CCaaS API, context/customer identification/transfer/masking/messages/timeline/Channel Integration Framework/attachments, proactive campaigns/dialing/WFM, Copilot/knowledge/plugins/smart assist, voice orchestration/DTMF/NLU/speech/SIP/multilingual, queues/overflow/assignment/routing/diagnostics, profiles/templates/inbox/scripts/macros/APIs/knowledge agent, supervisors/quality, Power BI and Application Insights. All 11 cited URLs were reachable. The guide records the active 120-minute English exam, no official Practice Assessment, 11 hours 40 minutes of official paths, three-day course, LinkedIn Learning with adjacent-content/runtime caveats, MB-240 non-direct partner transition, and no exact verified Pluralsight, O'Reilly, MeasureUp or Whizlabs product. Volatile telephony, provider, SDK/API, agent, licensing, capacity, proactive-engagement and regional details are marked **VERIFY CURRENT**. Blueprint SHA-256: `465a6902bed4ff612be45f9c72b3e11644c6e42108331debab23b62a37bb5fa5`.

## AB-210 coverage record

| Official objective group | Guide coverage |
|---|---|
| Configure Dynamics 365 Sales core features for AI | Section 1, all integrated scenarios, and Labs 1–3 |
| Optimize AI-driven sales | Section 2, all integrated scenarios, and Labs 4 and 7 |
| Qualify and prioritize leads by using AI | Section 3, inbound-qualification scenario, and Lab 5 |
| Develop deals by using intelligent opportunity research | Section 4, stalled-opportunities scenario, and Labs 6–7 |
| Extend and enhance Sales | Section 5, mobile-seller scenario, and Lab 8 |

The review maps every subobjective on the official June 18, 2026 guide to a lead-to-cash record/process, configuration choice, data/security/collaboration boundary, intelligence or agent contract, capacity and monitoring control, channel or extension decision, evidence, failure or recovery path. Three integrated scenarios, eight labs and 36 original checks cover deployment, mailboxes, business process flows/timeline, import/export, Dataverse security, Microsoft 365 collaboration, product/price/currency, AI-first data/reporting/plan choices, agent prerequisites/capacity, accelerator/assignment, conversational/predictive/relationship/Copilot/forecast/goal features, lead scoring, Qualification Agent modes/actions/monitoring, opportunity products/pipeline, Opportunity/Close/Research agents and research canvas, mobile/calling/SMS, flows, embedded Power Apps and Power BI. All 12 cited URLs are cataloged: ten were reachable and two Udemy pages were automation-blocked; none was missing or broken. The guide records the 120-minute English beta exam, delayed beta results, unavailable Practice Assessment, 12 hours 3 minutes of official paths, three-day course, current Udemy choices, MB-280 partner transition, and no exact verified Pluralsight, O'Reilly, MeasureUp or Whizlabs product. Volatile plan/licensing, agent, capacity/credit, mobile, calling and SMS details are marked **VERIFY CURRENT**. Blueprint SHA-256: `145a2a8c25fcf37ca19346a612706ce46838b4c0328d703b0bd53512ce9b5cf3`.

## AB-731 coverage record

| Official objective group | Guide coverage |
|---|---|
| Identify the business value of generative AI solutions | Section 1, all integrated scenarios, and Labs 1–3 and 5 |
| Identify benefits, capabilities, and opportunities for Microsoft’s AI apps and services | Section 2, all integrated scenarios, and Labs 4–5 |
| Identify an implementation and adoption strategy for Microsoft’s AI apps and services | Section 3, all integrated scenarios, and Labs 6–8 |

The review maps every July 22, 2026 subobjective to a business outcome, AI/ML/automation choice, model/adaptation decision, grounding/data/security contract, Microsoft capability, build/buy/extend boundary, responsible-AI control, operating owner, adoption mechanism, economic model or pilot decision. Three integrated scenarios, eight labs and 36 original checks cover generation versus ML and automation; pretrained and fine-tuned models; prompting, RAG, data readiness, ML lifecycle and secure AI; tokens, ROI and opportunity scoring; Copilot Chat/apps, Researcher, Analyst, Copilot Studio and Graph; Microsoft Foundry, Foundry Tools, Vision and Azure AI Search; model choice; responsible-AI principles; AI council, adoption team, champions and workload owners; adoption barriers; licensing/consumption models; and outcome, quality, adoption, risk and cost evidence. All 12 cited URLs are cataloged: ten were reachable and two Udemy pages were automation-blocked; none was missing or broken. The guide records the active 45-minute exam, 4 hours 44 minutes of official learning, one-day course, free Practice Assessment, official prep session, current Pluralsight and Udemy choices, partner learning, current-versus-older Foundry terminology, and no independently verified exact O'Reilly, MeasureUp or Whizlabs product. Volatile product, licensing, consumption and availability details are marked **VERIFY CURRENT**. No upcoming blueprint change or retirement was announced. Blueprint SHA-256: `ac86a35a21c860a8739b3d37f09e90288270e7343af24bf5dcc67729685c48c2`.

## AB-730 coverage record

| Official objective group | Guide coverage |
|---|---|
| Understand generative AI fundamentals | Section 1, all integrated scenarios, and Labs 1–2 |
| Manage prompts and conversations by using AI | Section 2, all integrated scenarios, and Labs 3–6 |
| Draft and analyze business content by using AI | Section 3, executive-status and proposal scenarios, and Labs 7–8 |

The review maps every July 22, 2026 subobjective to an outcome, experience/context choice, prompt/source contract, permission/protection boundary, responsible-AI risk, verification step, reuse/collaboration decision, evidence, or human approval. Three integrated scenarios, eight independent labs, and 36 original checks cover work/web/app context and Graph permissions; chat versus agents; Agent Store and custom agents; Researcher, Analyst, Pages and Notebooks; fabrication, prompt injection, over-reliance, sensitive data and data-protection restrictions; goal/context/source/expectation prompts; reference selection, iteration, save/schedule/share; chat find/delete/rename and notebook curation; agent templates/knowledge/instructions/capabilities/suggested prompts/sharing; new and source-derived documents, management summaries, cross-app workflows; meetings, collaboration, memory and instructions. All 11 cited URLs are cataloged: 10 were reachable and Udemy was automation-blocked; none was missing or broken. The guide records the active 45-minute exam, 4 hours 31 minutes of official learning, one-day course, free Practice Assessment, official prep video, current developing Pluralsight path, O'Reilly live course, MeasureUp and Udemy assessments, partner learning, and the absence of a verified exact Whizlabs product. Fast-moving Copilot, agent, Researcher/Analyst, Pages/Notebooks, memory, prompt-management, licensing and sharing behavior is marked **VERIFY CURRENT**. No upcoming blueprint change or retirement was announced. Blueprint SHA-256: `5387c1978cda745a51ab645fb402bb8080729bcf6461c63a1eac464492e71a55`.

## AB-410 coverage record

| Official objective group | Guide coverage |
|---|---|
| Create a foundation for intelligent applications | Section 1, all integrated scenarios, and Labs 1–3 |
| Create intelligent applications | Section 2, all integrated scenarios, and Labs 4–5 and 8 |
| Build business application logic and automation | Section 3, all integrated scenarios, and Labs 6–7 |

The review maps every May 15, 2026 subobjective to a business outcome, component choice, data/security/identity boundary, app interaction, automation or AI contract, evidence, failure, or recovery decision. Three integrated scenarios, eight independent labs, and 36 original checks cover requirement-to-component mapping; built-in agents and extensibility; environment types; solutions and ALM; Dataverse tables/properties/columns/relationships, prompt columns, row summaries, forms, views and security; model-driven forms/views/generative pages/access/charts/dashboards; responsive and accessible canvas apps; named formulas, UDFs, components, variables, collections, errors and Monitor; app-triggered flows and embedded agents; flow triggers/connectors/approvals/actions/conditions/loops/failure handling/idempotency; AI Hub prompts, knowledge, settings and app/flow consumption; AI models, validation and human review; and business rules, business process flows, calculated/formula/rollup columns. All 18 cited URLs are cataloged: 17 were reachable and the Udemy page was automation-blocked; none was missing or broken. The guide records the active credential, 120-minute English exam, 15 hours 26 minutes of current Learn paths, three-day course, unavailable official Practice Assessment, current Udemy and Whizlabs options, partner-restricted learning, and unverified exact Pluralsight/O'Reilly/MeasureUp offerings. Volatile agent, Copilot, prompt/model, capacity, region, license and governance behavior is marked **VERIFY CURRENT**. No upcoming blueprint change or retirement was announced. Blueprint SHA-256: `159e34e3c4e43d8825e43cd279f58fe37eab1457992433204c216015fe1424d6`.

## PL-400 coverage record

| Official objective group | Guide coverage |
|---|---|
| Create a technical design | Section 1, all integrated scenarios, and Lab 1 |
| Build Power Platform solutions | Section 2, all integrated scenarios, and Lab 2 |
| Implement Power Apps improvements | Section 3, regulated-case and partner-service scenarios, and Lab 3 |
| Extend the user experience | Section 4, regulated-case scenario, and Labs 4–5 |
| Extend the platform | Section 5, all integrated scenarios, and Labs 6–7 |
| Develop integrations | Section 6, partner-service and synchronization scenarios, and Lab 8 |

The review maps every March 19, 2026 subobjective to an extension choice, data/identity/security/transaction boundary, lifecycle control, implementation contract, evidence, failure, or recovery decision. Three integrated scenarios, eight independent labs, and 36 original checks cover out-of-box versus code; standard, virtual, and elastic tables; preview Power Fx functions; DLP and Dataverse security; solutions, layers, dependencies, configuration and CI/CD; advanced Power Fx, delegation and Monitor; Client API, commands, custom pages and PCF; plug-in stages, execution context, images, custom APIs and business events; connectors, platform APIs, Functions and flows; events, change tracking, alternate keys, Upsert and reconciliation. All 19 cited URLs are cataloged: 18 were reachable and Udemy returned an automation-blocked HTTP 403; none was missing or broken. The guide verifies the active credential, records a stale pre-update notice on its credential page, estimates about 25 listed hours across the current official self-paced paths, and records the five-day course, MIT official labs, free Practice Assessment, current vendor choices, and explicit freshness gaps in 2022–2024 material. No upcoming blueprint change or retirement was announced. Blueprint SHA-256: `4867995d075161ae07190d54a25c84872deb9efc388a7629743ee6bc49b8f468`.

## AZ-140 coverage record

| Published objective group | Guide coverage |
|---|---|
| Plan and implement an Azure Virtual Desktop infrastructure | Sections 1–2, global pooled scenario, and Labs 1–4 |
| Plan and implement identity and security | Section 3, contractor scenario, and Lab 5 |
| Plan and implement user environments and apps | Section 4, image/profile failure scenario, and Labs 6–7 |
| Monitor and maintain an Azure Virtual Desktop infrastructure | Section 5, integrated scenarios, and Lab 8 |

The guide maps every July 20, 2026 objective bullet to an end-to-end connection and state-delivery model, implementation decisions, failure modes, three cross-domain scenarios, eight independent labs, and 24 original knowledge checks. It includes the July-era RDP Multipath, identity/SSO, App Attach, security, Autoscale and recovery concepts and cites 27 exact registered sources: 24 were reachable, while two O'Reilly pages and one Udemy page returned HTTP 403 to the automated checker. The active credential has no announced retirement or blueprint change. The official objective snapshot SHA-256 is `d40f010042124a6e28c81a7f783b6127e3b7ebf7bb99d9b3ddfccdd40dcede84`.

## AZ-120 coverage record

| Published objective group | Guide coverage |
|---|---|
| Migrate SAP workloads to Azure | Sections 1–2, ECC and RISE scenarios, and Labs 1–2 |
| Design and implement an infrastructure to support SAP workloads on Azure | Section 3, ECC scenario, and Labs 3–5 |
| Design and implement high availability and disaster recovery (HADR) | Section 4, region-loss scenario, and Labs 6–7 |
| Maintain SAP workloads on Azure | Section 5, integrated scenarios, and Lab 8 |

The guide maps every April 17, 2026 objective bullet to an end-to-end SAP landscape decision model, supportability and sizing controls, failure modes, three cross-domain scenarios, eight independent labs, and 24 original knowledge checks. It cites 27 exact registered sources: 25 were reachable, while one O'Reilly page and one Udemy page returned HTTP 403 to the automated checker. The active credential has no announced retirement or blueprint change. The official objective snapshot SHA-256 is `9ef2824a901a8ba33075de4315d56f6bd0c7e9b5887028f27c16e6645e6eb3ff`.

## AZ-700 coverage record

| Published objective group | Guide coverage |
|---|---|
| Design and implement core networking infrastructure | Sections 1–2, hub-and-spoke scenario, and Labs 1–3 and 7 |
| Design, implement, and manage connectivity services | Section 3, hub-and-spoke scenario, and Lab 4 |
| Design and implement application delivery services | Section 4, global web scenario, and Lab 5 |
| Design and implement private access to Azure services | Section 5, hub-and-spoke scenario, and Lab 6 |
| Design and implement Azure network security services | Section 6, integrated scenarios, and Labs 7–8 |

The guide maps every July 27, 2026 objective bullet to a bidirectional packet-walk method, service and control comparisons, failure modes, two cross-domain scenarios, eight independent labs, and 24 original knowledge checks. It cites 26 exact registered sources: 23 were reachable, while two O'Reilly pages and one Udemy page returned HTTP 403 to the automated checker. The official objective snapshot SHA-256 is `949dcb2d1b4bbde19b6f41b69fdf59cf33b52391d4b8010e2a46d6a0c94a98dd`.

## AZ-305 coverage record

| Published objective group | Guide coverage |
|---|---|
| Design identity, governance, and monitoring solutions | Section 2, regulated application scenario, and Labs 1–2 |
| Design data storage solutions | Section 3, integrated scenarios, and Labs 3–4 |
| Design business continuity solutions | Section 4, regulated application scenario, and Lab 5 |
| Design infrastructure solutions | Section 5, migration scenario, and Labs 6–8 |

The guide maps every April 17, 2026 objective bullet to an architecture decision method, constraint and trade-off tables, failure modes, two cross-domain scenarios, eight independent design labs, and 24 original knowledge checks. It cites 29 exact registered sources: 26 were reachable, while two O'Reilly pages and one Udemy page returned HTTP 403 to the automated checker. The official objective snapshot SHA-256 is `7e5e8671b6ba67938e71f71261f92e0d9798f27ec94f79c75e3ea6310f917df2`.

## AZ-104 coverage record

| Published objective group | Guide coverage |
|---|---|
| Manage Azure identities and governance | Section 2, integrated scenarios, and Lab 1 |
| Implement and manage storage | Section 3, private web application scenario, and Lab 2 |
| Deploy and manage Azure compute resources | Section 4, private web application scenario, and Labs 3–5 |
| Implement and manage virtual networking | Section 5, VM connectivity scenario, and Labs 6–7 |
| Monitor and maintain Azure resources | Section 6, integrated scenarios, and Lab 8 |

The guide maps every published bullet to administrator responsibility boundaries, operational decision tables, common failure modes, two cross-domain troubleshooting scenarios, eight independent labs, and 20 original knowledge checks. It cites 25 exact registered sources: 22 were reachable, while two O'Reilly pages and one Udemy page returned HTTP 403 to the automated checker. The official objective snapshot SHA-256 is `7d2330fbafdd4981b54e6aa8f9ba371f0bbad1edf521fa8d2fa591e2bf8d2ae1`.

## GH-900 coverage record

| Published objective group | Guide coverage |
|---|---|
| Understand Git and GitHub basics | Parts 1–5, 7, and 10 |
| Work with GitHub repositories | Parts 4–6 and 13–15 |
| Collaborate using GitHub | Parts 7–8 |
| Apply modern development practices | Parts 9–11 |
| Manage projects with GitHub | Parts 8 and 12 |
| Understand privacy, security, and administration | Parts 5 and 13–15 |
| Explore the GitHub community | Parts 7 and 16 |

The review removed a duplicated GH-300-specific chapter from the GH-900 guide, retained a concise related-guide handoff, and added primary-reference blocks near each substantive part. The official blueprint snapshot SHA-256 is `bd1c323a21723f8479a7b79ec41a576044ebe6afbc5bf57715acf431fe90828b`.

## GH-300 coverage record

| Published objective group | Guide coverage |
|---|---|
| Use GitHub Copilot responsibly | Part 0, Parts 4–5, and Labs 3–5 |
| Use GitHub Copilot features | Parts 2–4, Part 6, and Labs 2–5 |
| Understand GitHub Copilot data and architecture | Part 0 and Parts 4–5 |
| Apply prompt engineering and context crafting | Part 0, Parts 3–4, and Labs 3 and 5 |
| Improve developer productivity with GitHub Copilot | Part 0, Parts 3–4, and Labs 1–3 |
| Configure privacy, content exclusions, and safeguards | Parts 5–6 and Lab 4 |

The review added first-party citations beside the responsible-AI principles, service-flow explanation, prompt-engineering model, productivity guidance, refactoring practice, and test-generation practice. The official blueprint snapshot SHA-256 is `2043edf29c68926236ec3a6e417058609e4e6cfec55e1e201e48e57c1b4fff9b`.

## GH-200 coverage record

| Published objective group | Guide coverage |
|---|---|
| Author and manage workflows | Parts 1–4, Part 10, and Labs 1–3 |
| Consume and troubleshoot workflows | Parts 4–5, troubleshooting by failure phase, and Labs 1–3 |
| Author and maintain actions | Part 6, custom-action engineering, and Lab 5 |
| Manage GitHub Actions for the enterprise | Part 7, enterprise governance and runner operations, and Lab 6 |
| Secure and optimize automation | Parts 8–10 and Labs 4–6 |

The review added official citations and decision guidance for editor validation, workflow badges, retention and REST administration, workflow templates, immutable releases, IP allow lists, hosted-runner image dependencies, and encrypted-secret APIs. The official blueprint snapshot SHA-256 is `b41c6a6832e14bf4b6c222d0b6162cff81e9ef4683480f89e89b3e0406fdf941`.

## GH-500 coverage record

| Published objective group | Guide coverage |
|---|---|
| Describe GitHub Security suites, features, and ecosystem | Parts 1–2 and security suites/architecture deep dive |
| Configure and use Secret Protection | Part 3, Secret Protection deep dive, and Lab 1 |
| Configure and use supply chain security | Part 4, supply-chain deep dive, and Labs 2–3 |
| Configure and use Code Security | Part 5, CodeQL deep dive, and Lab 4 |
| Security operations: best practices, prioritization, and remediation | Part 6, security operations at scale, and Lab 5 |
| GitHub Security suites administration | Part 7, administration/governance deep dive, and Lab 6 |

The review added direct primary sourcing beside all three security suites and an explicit model separating repository visibility, entitlement, deployment, policy, configuration, and operational health. The official blueprint snapshot SHA-256 is `a935dc15cfa929c01d402424f0edc39bb018b4c600ce734bd7cf10e1446ae102`.

## GH-100 coverage record

| Published objective group | Guide coverage |
|---|---|
| Manage GitHub identities and access | Parts 2–3, identity/access deep dive, identity drills, and Lab 3 |
| Administer GitHub Enterprise environment | Parts 1 and 8, administration playbooks/drills, and Lab 1 |
| Implement secure software development and compliance | Parts 4–6, secure-development administration, and Labs 2, 5, and 6 |
| Manage GitHub Actions | Part 7, Actions governance/networking, and Lab 4 |
| Monitor and optimize GitHub usage | Parts 8–12 and Lab 6 |

The review added direct primary sources beside identity models, SAML, SCIM, team synchronization, delegated roles, rulesets, audit evidence, GitHub Apps, Actions administration, support bundles, and license usage. It also corrected an obsolete SAML documentation path. The official blueprint snapshot SHA-256 is `9e671c9dd3ce7ac8914e989a0090422d6f0490fe19f3c9b11de73010453d44b6`.

## AI-103 coverage record

| Published objective group | Guide coverage |
|---|---|
| Plan and manage an Azure AI solution | Parts 1–3, implementation/operations playbooks in Parts 9–10, and Labs 1 and 4 |
| Implement generative AI and agentic solutions | Parts 4–5, implementation/operations playbooks in Parts 9–10, and Labs 2–4 |
| Implement computer vision solutions | Part 6, multimodal implementation in Part 9, and Lab 5 |
| Implement text analysis solutions | Part 7 and speech/translation operations in Part 9 |
| Implement information extraction solutions | Part 8, retrieval/Content Understanding implementation in Part 9, and Lab 6 |

The review retained the guide's architecture and production-operations depth while adding primary Microsoft citations at the decisions they support. A second-pass Foundry-generation audit replaced legacy URL aliases and a classic-only tracing page with canonical current sources, added Microsoft's official classic-to-current terminology crosswalk, and explicitly labeled confirmed classic or generation-uncertain training. The guide separates durable platform concepts from volatile Foundry naming, project types, models, deployment types, role names, quotas, SDKs, analyzer modes, preview features, regions, and licensing. The official blueprint snapshot SHA-256 is `3fbf0ebd6b3d5e591d7354de47f8d87baaea121330a209e9104045447ac70f63`.

## AB-100 coverage record

| Published objective group | Guide coverage |
|---|---|
| Plan AI-powered business solutions | Parts 1–4 and Architecture Exercises 1, 4, and 5 |
| Design AI-powered business solutions | Parts 5–7 and Architecture Exercises 1–3 and 5 |
| Deploy AI-powered business solutions | Parts 8–10 and Architecture Exercise 6 |

The review retained the guide's business-process, portfolio, value, platform, operations, ALM, security, and governance depth while adding direct primary sources at those decisions. It also added a cross-platform responsibility decomposition and worked service-case boundary so channel, orchestration, knowledge, action identity, system of record, failure, and audit concerns remain explicit. The official blueprint snapshot SHA-256 is `3736af21c41a6a8c785e5461d4ba25424a9e6b2205a3c10ae1d18589e16a61e2`.

## AZ-900 coverage record

| Published objective group | Guide coverage |
|---|---|
| Describe cloud concepts | Part 1, responsibility/benefit decision guide, and Labs 2 and 5 |
| Describe Azure architecture and services | Parts 2–3, placement/compute/network/storage/identity decision guides, and Labs 2–4 |
| Describe Azure management and governance | Part 4, governance/deployment/monitoring decision guides, and Labs 1 and 5 |

The review expanded every domain from service recognition into requirement, responsibility, scope, service choice, failure boundary, governance, and evidence decisions. It also corrected an obsolete Microsoft FinOps link during source-health review. The official blueprint snapshot SHA-256 is `8b4c89d325b3ce339eb881aa2dc4b251888e6d7a07d6351d81bcc2123b1c4449`.

## DP-900 coverage record

| Published objective group | Guide coverage |
|---|---|
| Describe core data concepts | Part 1, objective-to-scenario drill, and Labs 1 and 4 |
| Identify considerations for relational data on Azure | Part 2, objective-to-scenario drill, and Lab 2 |
| Describe considerations for working with non-relational data on Azure | Part 3, objective-to-scenario drill, and Labs 1 and 3 |
| Describe an analytics workload on Azure | Part 4, objective-to-scenario drill, and Labs 4 and 5 |

The review expanded the guide from service definitions into a repeatable requirement-to-design method, including a multi-store order and analytics scenario. It added direct Microsoft sourcing for SQL management boundaries, Cosmos DB partitioning/request units/consistency, analytical pipeline responsibilities, batch and streaming distinctions, Fabric and Databricks boundaries, and Power BI semantic modeling. The official blueprint snapshot SHA-256 is `7cef780d1a9e8e88b587fba89acb994985c4aedbd491710e814686ce5dc6559f`.

## PL-900 coverage record

| Published objective group | Guide coverage |
|---|---|
| Describe the business value of Microsoft Power Platform | Parts 1–2, objective-to-scenario drill, and integrated scenario |
| Manage the Microsoft Power Platform environment | Parts 2–3, objective-to-scenario drill, and end-to-end lab |
| Demonstrate the capabilities of Power Apps | Part 4, objective-to-scenario drill, and end-to-end lab |
| Demonstrate the capabilities of Power Automate | Part 5, objective-to-scenario drill, and end-to-end lab |
| Describe features and capabilities of agents in Microsoft Copilot Studio | Part 6, objective-to-scenario drill, and end-to-end lab |

The review expanded the guide into a requirement-to-solution method covering outcome, system of record, experience, process, trust boundary, and lifecycle evidence. It added Dataverse-versus-database and identity/connection paths, environment and release reasoning, canvas and flow execution paths, agent-turn diagnostics, an Agent 365 boundary, an objective drill, and an integrated employee-request design. July 2026 plans, code apps, vibe, Copilot-assisted automation, agent flows, evaluations, and Agent 365 details remain explicitly volatile. The official blueprint snapshot SHA-256 is `959c63326efa3e74735cd2abc1cb28246d816506296b218428802240f9f99bd0`.

## SC-900 coverage record

| Published objective group | Guide coverage |
|---|---|
| Describe the concepts of security, compliance, and identity | Part 1, objective-to-scenario drill, and Labs 3–4 |
| Describe the capabilities of Microsoft Entra | Part 2, objective-to-scenario drill, and Labs 1–2 |
| Describe the capabilities of Microsoft security solutions | Parts 3–4, objective-to-scenario drill, and Labs 3 and 5 |
| Describe the capabilities of Microsoft compliance solutions | Part 5, objective-to-scenario drill, and Labs 4–5 |

The review expanded the control-map premise into repeatable asset, actor, threat/obligation, preventive-control, signal/evidence, decision, and response reasoning. It added worked identity-request, inbound-application, security-signal, and document-lifecycle flows; an integrated compromised-administrator scenario; direct Microsoft sources beside material claims; and explicit volatility treatment for Entra Agent ID and changing service plans, licensing, portal surfaces, and coverage. The official blueprint snapshot SHA-256 is `e2869853685f48f936c2833bda16c5065a629346c7f5d1c9cd5aa91f9d1a3b91`.

## AB-900 coverage record

| Published objective group | Guide coverage |
|---|---|
| Identify the core features and objects of Microsoft 365 services | Parts 1–3, objective-to-scenario drill, and Labs 1–2 |
| Understand data protection and governance tasks for Microsoft 365 and Copilot | Parts 4–5, objective-to-scenario drill, and Labs 3–4 |
| Perform basic administrative tasks for Copilot and agents | Part 6, objective-to-scenario drill, and Lab 5 |

The review corrected the objective labels to the published wording and expanded the guide into a repeatable object, entitlement, identity, authorization, protection, admin-surface, and evidence method. It added collaboration-object tracing, sign-in gates, application-object boundaries, a governed-document path, Copilot grounding/data-protection flow, oversharing remediation, licensing/pay-as-you-go and measurement chains, Agent 365/Power Platform administration boundaries, an objective drill, and an HR-agent incident scenario. Fast-changing Copilot, Purview DSPM, SharePoint Advanced Management, billing, Researcher/Analyst, prompt, registry, approval, tool, license, and admin-surface details remain explicitly volatile. The official blueprint snapshot SHA-256 is `8e38035a94d260856ff5c08899492597046213510e057128edd89d775d363b90`.

## AI-901 coverage record

| Published objective group | Guide coverage |
|---|---|
| Identify AI concepts and capabilities | Parts 1–2, objective-to-scenario drill, and Labs 1 and 5 |
| Implement AI solutions by using Microsoft Foundry | Parts 3–8 and Labs 1–6 |

The review corrected the objective-map labels to the published wording and expanded the draft from concept recognition into a repeatable input/output/workload decision method. It added a Foundry component map, portal-to-client sequence, applied responsible-AI controls, agent-turn diagnostics, modality-specific implementation decisions, Content Understanding evidence stages, and an integrated help-assistant scenario. The official blueprint snapshot SHA-256 is `8b1c05a7a2258d69e43d47d75c0adeae2a5a7660e12e4d46627014d1ff9bedd1`.

## TERRAFORM-ASSOCIATE-004 coverage record

| Published objective group | Guide coverage |
|---|---|
| Infrastructure as Code (IaC) with Terraform | Domain 1 and Labs 1–2 |
| Terraform fundamentals | Domain 2 and Labs 1–2 |
| Core Terraform workflow | Domain 3 and Labs 1–2 |
| Terraform configuration | Domain 4 and Labs 1–5 |
| Terraform modules | Domain 5 and Lab 3 |
| Terraform state management | Domain 6 and Labs 4–5 |
| Maintain infrastructure with Terraform | Domain 7 and Labs 4–5 |
| HCP Terraform | Domain 8 and Lab 6 |

The review checked all 38 published subobjectives without inventing percentage weights, retained explicit **VERIFY CURRENT** treatment for volatile HCP Terraform service details, and verified that the 004-specific lifecycle, custom-condition, ephemeral/write-only, and workspace/project additions are visible. The official blueprint snapshot SHA-256 is `41390d0d2fbb8b1cfbfb7349ada41f4cf13dc65815827b802ad082fd2c1bf53b`.

## TERRAFORM-AUTHORING-OPERATIONS-PROFESSIONAL coverage record

| Published objective group | Guide coverage |
|---|---|
| Manage resource lifecycle | Domain 1, integrated professional playbook, and Labs 1–2 |
| Develop and troubleshoot dynamic configuration | Domain 2 and Labs 2–3 |
| Develop collaborative Terraform workflows | Domain 3 and Lab 4 |
| Create, maintain, and use Terraform modules | Domain 4 and Labs 2–3 |
| Configure and use Terraform providers | Domain 5 and Lab 5 |
| Collaborate on infrastructure as code using HCP Terraform | Domain 6 and Lab 6 |

The review mapped all six unweighted domains and their subobjectives to lifecycle, dynamic HCL, collaborative state/automation, module, provider, and HCP Terraform explanations. Seven labs emphasize address-preserving change, verification, failure classification, and unfamiliar-environment execution rather than command recognition. All 19 cited links are reachable first-party sources. The current AWS-provider exam version and HashiCorp's announced late-2026 Azure-provider version are separated explicitly. The official blueprint snapshot SHA-256 is `88a65ae987088cf298443a82308251ad72752622488feeaa9f8150436ac55289`.

## VAULT-ASSOCIATE-003 coverage record

| Published objective group | Guide coverage |
|---|---|
| Authentication methods | Domain 1 and Lab 1 |
| Vault policies | Domain 2 and Lab 1 |
| Vault tokens | Domain 3 and Lab 2 |
| Vault leases | Domain 4 and Lab 3 |
| Secrets engines | Domain 5 and Lab 3 |
| Encryption as a Service | Domain 6 and Lab 4 |
| Vault architecture fundamentals | Domain 7 and Lab 5 |
| Vault deployment architecture | Domain 8 and Lab 5 |
| Access management architecture | Domain 9 and Lab 6 |

The review mapped all nine unweighted domains and their subobjectives to one identity-to-secret lifecycle: external identity, auth mount, entity/group, policy, token, engine, lease/key, delivery, and revocation evidence. Six labs test policy denial, token lineage, static/dynamic lifecycle, transit rotation, deployment recovery, and workload delivery. All 19 cited links are reachable first-party sources. The guide preserves the official Vault 1.16 baseline and labels current release, edition, HCP, limit, and interface details as volatile. The official blueprint snapshot SHA-256 is `2322b0085fb020f4cd83226d6c3e660412ae71e6de790e3e5716e17504818f0a`.

## VAULT-OPERATIONS-PROFESSIONAL coverage record

| Published objective group | Guide coverage |
|---|---|
| Create a working Vault server configuration given a scenario | Domain 1 and Labs 1–2 |
| Monitor a Vault environment | Domain 2 and Labs 3 and 8 |
| Employ the Vault security model | Domain 3 and Labs 6–7 |
| Build fault-tolerant Vault environments | Domain 4 and Labs 1, 4, and 5 |
| Understand the hardware security module integration | Domain 5 and Lab 5 |
| Scale Vault for performance | Domain 6 and Lab 5 |
| Configure access control | Domain 7 and Lab 6 |
| Configure Vault Agent | Domain 8 and Lab 7 |

The review mapped all eight unweighted Enterprise-aware domains to explicit server, evidence, security, availability, HSM, scaling, access, and workload-delivery operating models. Eight labs cover cluster construction, root removal, evidence correlation, isolated restore, replication, tenancy/approval, Agent rotation, and timed incident response. All 21 cited links are reachable first-party sources. Edition, licensing, seal, replication, metric, namespace, HCP, and exam-environment behavior remains marked **VERIFY CURRENT**. The official blueprint snapshot SHA-256 is `9144a3107d050f893b0c845664fbe4ca07e8edff7f4830f8dc89fefea3d291d6`.

## AZ-400 coverage record

| Published objective group | Guide coverage |
|---|---|
| Design and implement processes and communications | Sections 1–2, hybrid delivery scenario, and Lab 1 |
| Design and implement a source control strategy | Section 3, hybrid delivery scenario, and Lab 2 |
| Design and implement build and release pipelines | Section 4, integrated scenarios, and Labs 3–6 |
| Develop a security and compliance plan | Section 5, compromised-runner scenario, and Lab 7 |
| Implement an instrumentation strategy | Section 6, integrated scenarios, and Lab 8 |

The review maps every July 27, 2026 subobjective to a work-to-production evidence model spanning both GitHub and Azure DevOps. It includes package provenance, layered tests, runner/agent trust, reusable multi-stage YAML, progressive delivery, database compatibility, IaC/self-service, identity federation, security scanning, OpenTelemetry, KQL, and pipeline/runtime metrics. Eight labs and three integrated scenarios emphasize failure isolation and recovery. All 40 cited URLs are cataloged: 39 were reachable and Udemy returned access-blocked HTTP 403. The guide records Azure Automation State Configuration's September 30, 2027 retirement and the applicable legacy Azure DevOps WIF issuer's July 1, 2027 retirement with current transition guidance. The official blueprint snapshot SHA-256 is `2daece89f2a2ef131293e7299b41532985afbe955aed913bb86dc42bb8650460`.

## AZ-800 coverage record

| Published objective group | Guide coverage |
|---|---|
| Deploy and manage AD DS in on-premises and cloud environments | Sections 1–2, branch and Azure application scenarios, and Labs 1–3 |
| Manage Windows Servers and workloads in a hybrid environment | Section 3, all integrated scenarios, and Labs 3–4 |
| Manage virtual machines and containers | Section 4, Azure application scenario, and Labs 5–6 |
| Implement and manage an on-premises and hybrid networking infrastructure | Section 5, branch and Azure application scenarios, and Lab 7 |
| Manage storage and file services | Section 6, file-server migration scenario, and Lab 8 |

The review maps every January 21, 2026 subobjective to a hybrid identity, management, compute, network, or data path with explicit decision points and failure evidence. It includes AD DS topology and recovery implications, hybrid synchronization and authentication, constrained administration, Azure Arc, Hyper-V and Windows containers, Azure VM infrastructure, DNS/DHCP and private access, Azure Files/File Sync, SMB, DFS, and block/file storage distinctions. Three integrated scenarios, eight labs, and 24 original knowledge checks emphasize diagnosis and recovery. All 73 cited URLs are cataloged: 69 were reachable, while three O'Reilly pages and one Udemy page were access-blocked; none was missing or broken. The guide prominently records AZ-800 and AZ-801 retirement on September 30, 2026 at 5:00 PM Central Standard Time and points to AZ-802 as Microsoft's remaining replacement path. The official blueprint snapshot SHA-256 is `03c6f4e0c73f383ada8c4ddf43a91fa28ec513a732b40abae0a38b1b6ac4f7bc`.

## AZ-801 coverage record

| Published objective group | Guide coverage |
|---|---|
| Secure Windows Server on-premises and hybrid infrastructures | Sections 1–2, secure file-service and cyber-recovery scenarios, and Lab 1 |
| Implement and manage Windows Server high availability | Section 3, secure file-service scenario, and Labs 2–3 |
| Implement disaster recovery | Section 4, secure file-service and cyber-recovery scenarios, and Labs 4–5 |
| Migrate servers and workloads | Section 5, legacy application migration scenario, and Labs 6–7 |
| Monitor and troubleshoot Windows Server environments | Section 6, all integrated scenarios, and Lab 8 |

The review maps every October 6, 2025 subobjective to requirement, dependency, control, evidence, failure action, and recovery proof. Three integrated scenarios, eight labs, and 24 original knowledge checks cover security, clustering/S2D, backup/replication, server/workload/forest migration, monitoring, and layered troubleshooting. All 83 cited URLs are cataloged: 80 were reachable, while two O'Reilly books and one Udemy page were access-blocked; none was missing or broken. The guide distinguishes current AMA/DCR from retired MMA/OMS, records ADMT's deprecated support state, and marks Azure Disk Encryption's September 15, 2028 retirement and encryption-at-host direction. It prominently records AZ-801 retirement on September 30, 2026 at 5:00 PM Central Standard Time, links AZ-802, and discloses the canonical-study-guide versus exam-page weight discrepancy. The official blueprint snapshot SHA-256 is `c279fe648d4e3a6c67df9e119c95335e042937b93b83ffbf6a07d7f0ce51a76f`.

## AZ-802 coverage record

| Official objective group | Guide coverage |
|---|---|
| Deploy and manage Active Directory Domain Services (AD DS) | Sections 1–2, integrated scenarios, and Labs 1–2 and 8 |
| Manage Windows Server instances and workloads in a hybrid environment | Section 3, branch scenario, and Labs 2–3 |
| Manage virtual machines | Section 4, consolidated operating scenario, and Labs 4–5 |
| Implement and manage an on-premises and hybrid networking infrastructure | Section 5, branch scenario, and Labs 5–6 |
| Manage storage and file services | Section 6, file-workload migration scenario, and Lab 7 |
| Secure Windows Server infrastructure | Section 7, all integrated scenarios, and Labs 1–3 and 5–8 |
| Monitor and troubleshoot Windows Server environments | Section 8, all integrated scenarios, and Labs 3–8 |

The review maps every published AZ-802 beta subobjective from the official page last updated July 6, 2026 to an operating dependency, decision, implementation boundary, failure signal, or recovery proof. Three integrated scenarios, eight labs, and 28 original knowledge checks reinforce AD DS and Group Policy, hybrid management and Azure Arc, Hyper-V/Azure VMs, DNS/DHCP, Azure Files/File Sync and Windows storage, layered security, AMA/DCR monitoring, and evidence-led troubleshooting. All 77 cited URLs are cataloged: 72 were reachable and five commercial-provider pages were access-blocked; none was missing or broken. The guide prominently identifies beta volatility, the absence of a separate published skills-effective date and Practice Assessment, the live five-day AZ-802T00 course, the credential-page training discrepancy, and the September 30, 2026 replacement transition from AZ-800/AZ-801. A dedicated public SSH Direct product article was not discoverable, so the guide anchors that objective to the official blueprint and labels its implementation details **VERIFY CURRENT**. The official blueprint snapshot SHA-256 is `ec584efe0ea08ae5ad6bbcef992c1b4a4e6b18826193ece06a76114757c8f65d`.

## DP-300 coverage record

| Official objective group | Guide coverage |
|---|---|
| Plan and implement data platform resources | Sections 1–2, migration scenario, and Labs 1–2 |
| Implement a secure environment | Section 3, migration and recovery scenarios, and Lab 3 |
| Monitor, configure, and optimize database resources | Section 4, performance scenario, and Labs 4–5 |
| Configure and manage automation of tasks | Section 5, all integrated scenarios, and Lab 6 |
| Plan and configure a high availability and disaster recovery (HA/DR) environment | Section 6, migration and recovery scenarios, and Labs 7–8 |

The review maps every April 24, 2026 subobjective to a platform decision, configuration boundary, signal, failure action, or recovery proof. Three integrated scenarios, eight labs, and 28 original knowledge checks cover Azure SQL Database, Managed Instance, SQL Server VMs/hybrid SQL, Fabric SQL, both Arc SQL models, deployment and migration, layered security, database watcher and engine tuning, automation, and platform-specific backup/HA/DR. All 65 cited URLs are cataloged: 62 were reachable and three O'Reilly/Udemy pages were access-blocked; none was missing or broken. The guide explicitly labels Azure Data Studio retired on February 28, 2026 and uses supported current migration paths. No upcoming blueprint change or retirement was announced. The official blueprint snapshot SHA-256 is `08cba3368c07be28f4abeea90be94256a0cd0fc247ed53f2561fd340c0df3e4b`.

## DP-420 coverage record

| Official objective group | Guide coverage |
|---|---|
| Design and implement data models | Sections 1–2, all integrated scenarios, and Labs 1–3 |
| Design and implement data distribution | Section 3, global-commerce scenario, and Lab 4 |
| Integrate an Azure Cosmos DB solution | Section 4, all integrated scenarios, and Labs 5–6 |
| Optimize an Azure Cosmos DB solution | Section 5, commerce and IoT scenarios, and Labs 1–5 |
| Maintain an Azure Cosmos DB solution | Section 6, all integrated scenarios, and Labs 6–8 |

The review maps every July 21, 2026 subobjective to an access-pattern decision, implementation boundary, measurable signal, failure action, or recovery proof. Three integrated scenarios, eight labs, and 30 original knowledge checks cover document modeling and schema versioning, natural/synthetic/hierarchical partitioning, throughput, current SDK/query/transaction/server-side patterns, regions/consistency/conflicts, Fabric mirroring and transitional Synapse analytical paths, replay-safe change feed, indexing/cache optimization, observability, backup/PITR, layered security, data movement, and IaC. All 76 cited URLs are cataloged: 73 were reachable and three O'Reilly/Udemy pages were access-blocked; none was missing or broken. The guide prominently records that Synapse Link is no longer supported for new projects while retaining its still-published exam objectives for existing deployments, and points new analytical designs to Fabric mirroring. It labels current limits, preview backup tiers, pricing, vendor alignment, and evolving integrations for re-verification. No upcoming blueprint change or exam retirement was announced. The official blueprint snapshot SHA-256 is `7966ceca9589ef574018cacb35f5bcd02a55b148a34107310b5e7c9e1e52de7a`.

## DP-750 coverage record

| Official objective group | Guide coverage |
|---|---|
| Set up and configure an Azure Databricks environment | Sections 1–2, all integrated scenarios, and Labs 1–2 |
| Secure and govern Unity Catalog objects | Section 3, governed sales and external-sharing scenarios, and Labs 2–3 |
| Prepare and process data | Section 4, all integrated scenarios, and Labs 4–6 |
| Deploy and maintain data pipelines and workloads | Section 5, all integrated scenarios, and Labs 5–8 |

The review maps every March 11, 2026 subobjective to an environment, governance, ingestion, processing, delivery, evidence, failure, or recovery decision. Three integrated scenarios, eight labs, and 36 original knowledge checks cover compute and libraries, Unity Catalog objects and permissions, ABAC/filters/masks, identity and secrets, lineage/audit/sharing, modeling and layout, batch/stream/CDC ingestion, quality, jobs, Git/testing/bundles, Spark troubleshooting, Delta maintenance, cost, and Azure monitoring. All 52 cited URLs are cataloged: 48 were reachable and four O'Reilly/Udemy pages were access-blocked; none was missing or broken. The guide explicitly reconciles current Lakeflow Spark Declarative Pipelines and Declarative Automation Bundles names with legacy DLT and published Asset Bundles wording. It labels runtime support, serverless availability, preview boundaries, limits, pricing, commercial alignment, and changing product names for re-verification. No upcoming blueprint change or exam retirement was announced. The official blueprint snapshot SHA-256 is `eba786118a9e5129571b0a9505b8849bd82f3cdf84e2da759d735f354f27fb84`.

## DP-800 coverage record

| Official objective group | Guide coverage |
|---|---|
| Design and develop database solutions | Sections 1–2, all integrated scenarios, and Labs 1–2 |
| Secure, optimize, and deploy database solutions | Section 3, all integrated scenarios, and Labs 3–7 |
| Implement AI capabilities in database solutions | Section 4, tenant-safe RAG scenario, and Labs 7–8 |

The review maps every March 12, 2026 subobjective to a requirement, platform decision, implementation boundary, evidence artifact, failure action, or recovery path. Three integrated scenarios, eight labs, and 36 original knowledge checks cover relational/JSON/specialized design, modern T-SQL, AI-assisted tools and MCP, layered security, concurrency, plans and Query Store, database projects and deployment controls, Data API builder, monitoring, change processing, external models, embedding lifecycle, ENN/ANN/vector indexes, hybrid retrieval, RRF, and secure grounded generation. All 86 cited URLs are cataloged: 84 were reachable, while O'Reilly and Udemy returned access-blocked HTTP 403; none was missing or broken. The guide labels fast-changing platform, compatibility, JSON/regex/fuzzy/vector and preview boundaries, uses current Microsoft Foundry naming while identifying older names, and records the August 15, 2026 CES Event Hubs AMQP-to-Kafka transition. No upcoming blueprint change or exam retirement was announced. The official blueprint snapshot SHA-256 is `5302e42b10e2f414caa1fba1ef4e641ecfb85b44d87bb39635b5caea2ac79e7f`.

## AI-200 coverage record

| Official objective group | Guide coverage |
|---|---|
| Develop containerized solutions on Azure | Sections 1–2, all integrated scenarios, and Labs 1–3 |
| Develop AI solutions by using Azure data management services | Section 3, all integrated scenarios, and Labs 4–6 |
| Connect to and consume Azure services | Section 4, ingestion and AKS scenarios, and Lab 7 |
| Secure, monitor, troubleshoot Azure solutions | Section 5, all integrated scenarios, and Lab 8 |

The review maps every subobjective on the official page last updated May 5, 2026 to a production dependency, implementation boundary, evidence artifact, failure action, or recovery path. Three integrated scenarios, eight labs, and 36 original knowledge checks cover ACR/Tasks, App Service, Container Apps revisions/KEDA, AKS manifests and troubleshooting, Cosmos SDK/RU/vector/change feed, PostgreSQL/pgvector and resource/connection tuning, Managed Redis cache/vector behavior, Service Bus settlement/DLQ, Event Grid filters/retry, Functions, Key Vault rotation, App Configuration, OpenTelemetry and KQL. All 55 cited URLs are cataloged: 51 were reachable and four Udemy pages were automation-blocked; none was missing or broken. The guide records that no Microsoft Practice Assessment was available, the exact Azure Cache for Redis retirement transition, and current platform/vector/SDK volatility. No upcoming exam blueprint change or retirement was announced. The official blueprint snapshot SHA-256 is `3dc5dfbae796cc5345c92061d04d0e671d5ebc7252ac057038ca61b8b8a6e464`.

## AI-300 coverage record

| Official objective group | Guide coverage |
|---|---|
| Design and implement an MLOps infrastructure | Section 1, all scenarios, Labs 1–2 |
| Implement machine learning model lifecycle and operations | Section 2, regulated-model scenario, Labs 3–5 |
| Design and implement a GenAIOps infrastructure | Section 3, GenAI scenarios, Lab 6 |
| Implement generative AI quality assurance and observability | Section 4, GenAI scenarios, Lab 7 |
| Optimize generative AI systems and model performance | Section 5, RAG/fine-tuning scenarios, Lab 8 |

The review maps every subobjective on the official page last updated March 5, 2026 to infrastructure, reproducibility, lifecycle, deployment, monitoring, evaluation or optimization evidence. Three scenarios, eight labs and 36 original checks cover workspace assets and registries, identity/private networking, Bicep/CLI/GitHub OIDC, MLflow/AutoML/sweeps/distributed training, feature specifications, responsible registration, online/batch rollout, drift/retraining, Foundry/model/PTU/prompt delivery, quality/safety/tracing/cost, RAG tuning/A-B tests and governed fine-tuning/synthetic data. All 41 URLs are cataloged: 39 reachable and two Udemy pages automation-blocked; none broken. No upcoming exam change or retirement was announced. Blueprint SHA-256: `79d7fabcf253e7ac5f5f7629397075867d22c48045c2483c9d03e1b217215f41`.

## AI-500 coverage record

| Official objective group | Guide coverage |
|---|---|
| Architect multi-agent solutions | Sections 1–2, all integrated scenarios, Labs 1–3 |
| Develop multi-agent solutions in Azure | Sections 3–5, all integrated scenarios, Labs 2–5 |
| Evaluate, optimize, and monitor multi-agent solutions | Section 6, all integrated scenarios, Labs 5–7 |
| Secure, govern, and deploy multi-agent solutions | Section 7, all integrated scenarios, Labs 3 and 6–8 |

The review maps every subobjective on the official page last updated July 16, 2026 to an architecture, implementation, evaluation, operating, security, governance, or release decision. Three integrated scenarios, eight independent labs, and 36 original checks cover agent boundaries and topology; Agent Framework, HITL, MCP and A2A; identity, OBO, memory and RAG; prompts, context, fine-tuning, tools and middleware; layered evaluation, continuity failures, tracing, SLOs and cost; and guardrails, red teaming, environment promotion and controlled rollout. All 32 cited URLs are cataloged: 30 were reachable and O'Reilly and Udemy returned access-blocked HTTP 403; none was missing or broken. The guide distinguishes current Microsoft Foundry from classic material, marks preview/volatile behavior, records the beta exam and AI-103 credential prerequisite, separates the live beta from AI-500T00's September 30 availability, and records the absence of an official Practice Assessment and exact paths from several commercial providers. No upcoming blueprint change or retirement was announced. Blueprint SHA-256: `498ed5ca3e5f1ac958dedea4b84cb33a34a8ff0f5aa239540fd7283bc41360e8`.

## AB-620 coverage record

| Official objective group | Guide coverage |
|---|---|
| Plan and configure agent solutions | Sections 1–3, all integrated scenarios, Labs 1–3 |
| Integrate and extend agents in Copilot Studio | Sections 4–5, all integrated scenarios, Labs 4–6 |
| Test and manage agents | Sections 6–7, all integrated scenarios, Labs 7–8 |

The review maps every subobjective on the official page last updated April 21, 2026 to an agent object, integration boundary, identity/governance decision, test, signal, or recovery path. Three integrated scenarios, eight independent labs, and 36 original checks cover classic-versus-new Copilot Studio; architecture, audiences, channels, identity and governance; agent flows/HITL, topics, Power Fx, Adaptive Cards, prompts, generative answers and variables; enterprise knowledge, Azure AI Search, connectors, REST, MCP and computer use; child, connected, Foundry, Fabric and A2A agents; evaluation and Application Insights; and solutions, environment variables and pipelines. All 31 cited URLs are cataloged: 29 were reachable and two Udemy pages returned access-blocked HTTP 403; none was missing or broken. The guide records that the active credential no longer carries a beta label, that official objective paths are classic-experience based while the new experience remains preview with no conversion path, that the three self-paced paths are live while the three-day course is dated September 18, and that no official Practice Assessment or exact resource from several commercial providers was verified. No upcoming blueprint change or retirement was announced. Blueprint SHA-256: `8b9f6ca0601cf631a000763ce7a0cca802a0177c66d7a4e3cc29d84d52188dfc`.

## SC-100 coverage record

| Official objective group | Guide coverage |
|---|---|
| Design solutions that align with security best practices and priorities | Section 1, all integrated scenarios, Labs 1–2 |
| Design security operations, identity, and compliance capabilities | Section 2, all integrated scenarios, Labs 3–6 |
| Design security solutions for infrastructure | Section 3, all integrated scenarios, Labs 3 and 6–7 |
| Design security solutions for applications and data | Section 4, AI/Copilot and web/API scenarios, Labs 2 and 7–8 |

The review maps every July 28, 2026 subobjective to a strategy, control boundary, implementation choice, evidence artifact, failure condition, or recovery action. Three integrated scenarios, eight independent labs, and 36 original checks cover ransomware/BCDR and privileged recovery; MCRA, MCSB, Zero Trust, CAF, WAF, landing zones, secure AI and DevSecOps; XDR/SIEM/SOAR and ATT&CK; human, external, workload and agent identity; enterprise privileged access and compliance; multicloud CSPM/CWPP, Azure Arc, EASM and Exposure Management; endpoints, OT/IoT, cloud service models and SSE; Microsoft 365/Copilot; and application, API, WAF, encryption and data security. All 36 cited URLs are cataloged: 34 were reachable and two O'Reilly pages returned access-blocked HTTP 403; none was missing or broken. The guide marks 2022–2025 secondary resources as older foundations, verifies the active exam and current prerequisite credentials, records a free Microsoft Practice Assessment and 20 hours 58 minutes of current Microsoft Learn paths, and labels agent, AI, SSE, Exposure Management, and Copilot volatility. No upcoming blueprint change or retirement was announced. Blueprint SHA-256: `342b0f01a93d8047a5dbc4ecc9d9529b94191d6cab60c99af7307251aaee6099`.

## SC-200 coverage record

| Official objective group | Guide coverage |
|---|---|
| Manage a security operations environment | Section 1, all integrated scenarios, Labs 1–4 |
| Respond to security incidents | Section 2, all integrated scenarios, Labs 5–7 |
| Perform threat hunting | Section 3, long-horizon scenario, Labs 4 and 8 |

The review maps every July 28, 2026 subobjective to a configuration boundary, operating decision, query or investigation path, evidence artifact, failure action, or recovery proof. Three integrated scenarios, eight independent labs, and 36 original checks cover Defender XDR notifications/tuning, Endpoint settings/ASR/device groups/custom data collection, AIR and attack disruption, Sentinel automation, roles, tiers/retention, workbooks and SOC optimization, multisource AMA/DCR/WEF/Syslog/CEF ingestion, diagnostics, indicators/custom tables, Defender and Sentinel detection engineering, cross-domain response, Endpoint actions, Purview/Audit/eDiscovery/Graph evidence, KQL, Advanced Hunting, threat analytics, Sentinel Graph, data-lake jobs/summaries, notebooks, Security Copilot, agentic investigation, and Sentinel MCP. All 48 cited URLs are cataloged: 46 were reachable and the O'Reilly and Udemy pages returned access-blocked HTTP 403; none was missing or broken. The guide marks older secondary resources as foundations, verifies the active credential and free Practice Assessment, records 43 hours 12 minutes of current Microsoft Learn paths, and calls out the March 31, 2027 Sentinel Azure-portal support end. No upcoming blueprint change or exam retirement was announced. Blueprint SHA-256: `c64e8b14b67c6cd01b9ec4df39441c9d83971c5e2db87010561edbb07eda656e`.

## SC-300 coverage record

| Official objective group | Guide coverage |
|---|---|
| Implement and manage user identities | Section 1, hybrid and partner scenarios, and Labs 1–3 |
| Implement authentication and access management | Section 2, all integrated scenarios, and Labs 4–5 |
| Plan and implement workload identities | Section 3, SaaS and workload scenarios, and Labs 6–7 |
| Plan and automate identity governance | Section 4, all integrated scenarios, and Lab 8 |

The review maps every April 27, 2026 subobjective to an identity lifecycle, delegation decision, authentication/authorization boundary, configuration dependency, evidence artifact, failure action, or recovery path. Three integrated scenarios, eight labs, and 36 original checks cover tenant roles/AUs/settings; workforce, device, license and custom-attribute lifecycle; external/cross-tenant and hybrid identity; strong authentication, TAP, passkeys, SSPR and Windows Hello; Conditional Access, risk and Global Secure Access; managed/application identities; enterprise apps, App Proxy and consent; Defender for Cloud Apps; entitlement, access reviews, PIM and emergency access; and logs, KQL, workbooks and Identity Secure Score. All 45 cited URLs are cataloged: 43 were reachable and two O'Reilly book pages were access-blocked; none was missing or broken. The guide verifies the active exam, free Practice Assessment and 15 hours 11 minutes of current Learn paths, labels older resources by current gaps, marks fast-changing Cloud Sync, registration, GSA and MDCA behavior **VERIFY CURRENT**, and discloses Microsoft's own conflicting authentication-domain weight. No upcoming blueprint change or retirement was announced. Blueprint SHA-256: `242f9f0cedd16af9ee78aa8d389ab62fcba2a925f7b86070d44f94d5f98c624b`.

## SC-500 coverage record

| Official objective group | Guide coverage |
|---|---|
| Manage identity, access, and governance | Section 1, all integrated scenarios, and Labs 1–3 |
| Secure storage, databases, and networking | Section 2, all integrated scenarios, and Labs 4–5 |
| Secure compute | Section 3, AI/platform/hybrid scenarios, and Labs 6–8 |
| Manage and monitor security posture | Section 4, all integrated scenarios, and Labs 3 and 7–8 |

The review maps every objective on the official page last updated May 13, 2026 to an identity, authorization, data, network, compute, posture, monitoring, evidence, failure, or recovery decision. Three integrated scenarios, eight independent labs, and 36 original checks cover PIM, Conditional Access, app/workload identity, Key Vault, Policy/compliance/RBAC/Backup/IaC, Storage/SQL/networking, SharePoint and Copilot data, Copilot Studio protection, Entra Agent ID, AI Gateway, Defender for AI Services, Foundry guardrails, Data and AI dashboard, VMs/Arc, containers/application platforms, Defender posture/multicloud/EASM, Sentinel collection/automation/retention/Purview, and Security Copilot. All 51 cited URLs are cataloged: 49 were reachable, while the O'Reilly legacy video and one Udemy course were access-blocked; none was missing or broken. The guide verifies the active 120-minute exam, absent Practice Assessment, August 31, 2026 AZ-500 retirement, 30 hours 8 minutes of current Microsoft Learn paths, and MIT-licensed Tim Warner companion. It labels AZ-500-only resources as incomplete foundations and marks AI, Agent ID, Gateway, Defender-plan, disk-encryption, Sentinel-portal, and Security Copilot volatility **VERIFY CURRENT**. No upcoming blueprint change or SC-500 retirement was announced. The official blueprint snapshot SHA-256 is `9f832db799678f547b3272c902e5529c77077e2cd4272326cf8ad94ef50cf7c6`.

## MS-102 coverage record

| Official objective group | Guide coverage |
|---|---|
| Deploy and manage a Microsoft 365 tenant | Section 1, all integrated scenarios, and Labs 1–4 |
| Implement and manage Microsoft Entra identity and access | Section 2, hybrid identity scenarios, and Labs 5–6 |
| Manage security and threats by using Microsoft Defender XDR | Section 3, all integrated scenarios, and Lab 7 |
| Manage compliance by using Microsoft Purview | Section 4, data-exfiltration scenario, and Lab 8 |

The review maps every April 28, 2026 subobjective to a tenant, identity, security, compliance, operating, evidence, failure, or recovery decision. Three integrated scenarios, eight independent labs, and 36 original checks cover domains/DNS, health/network/update/usage/Backup, identities/groups/licenses/Graph, cross-workload roles/AUs/PIM, Connect Sync and Cloud Sync, authentication/SSPR/Password Protection/risk/Conditional Access, Exposure Management/Secure Score/XDR, Defender for Office 365/Endpoint/Cloud Apps, and Purview classification/labels/retention/explorers/workload and endpoint DLP. All 56 cited URLs are cataloged: 53 were reachable and two O'Reilly pages plus the Udemy page were automation-blocked; none was missing or broken. The guide records the November 30, 2026 exam and certification retirement, absence of an officially named direct replacement, free Practice Assessment, 28 hours 45 minutes of current Learn paths, five-day course, and freshness gaps in older resources. Blueprint SHA-256: `97ce6b34e98fb43947409e8b7997f3de72e6cae7a62102dfdea849bfb177c92a`.

## AB-650 coverage record

| Official objective group | Guide coverage |
|---|---|
| Configure and manage Microsoft 365 tenants and workloads | Section 1, all integrated scenarios, and Labs 1–2 |
| Govern and secure Microsoft 365 tenants and workloads | Section 2, all integrated scenarios, and Labs 3–6 |
| Manage and secure AI services in Microsoft 365 | Section 3, all integrated scenarios, and Labs 2, 6–8 |

The review maps every subobjective on the beta blueprint page last updated July 27, 2026 to a tenant, workload, entitlement, identity, authorization, data, agent/tool, security, operational, evidence, failure, or recovery decision. Three integrated scenarios, eight independent labs, and 36 original checks cover tenant settings/domains/licenses/Backup/health; Exchange, Teams, SharePoint, OneDrive, Search, Advanced Management and connectors; workforce/external identity, roles/PIM/AUs, authentication/risk/Conditional Access; Defender for Office 365 and attack simulation; Purview labels/retention/DLP/DSPM; Copilot readiness/search/web/Cowork/tenant settings; agent identities/access packages/lifecycle/registry; MCP servers/connectors/plugins/skills; Agent 365 protection/compliance; and cost, usage, adoption and service health. All 22 cited URLs were reachable. The guide records the beta status, absence of a separate skills effective date, unavailable Practice Assessment, 23 hours 8 minutes of current Learn paths, and the lack of independently verified exam-specific Pluralsight, O'Reilly, Udemy, Whizlabs or MeasureUp offerings. Fast-moving AI, Agent 365, Copilot and portal behavior is marked **VERIFY CURRENT**. Blueprint SHA-256: `e70d10682f078cb6887f7dde679f56661e63dfeabb221779f6b0ff4ab08bdf1a`.

## MD-102 coverage record

| Official objective group | Guide coverage |
|---|---|
| Prepare infrastructure for devices | Section 1, all integrated scenarios, and Labs 1–2 |
| Manage and maintain devices | Section 2, Autopilot scenario, and Labs 3–4 |
| Protect devices | Section 3, agent recommendation scenario, and Lab 5 |
| Manage and secure applications | Section 4, BYOD/Autopilot scenarios, and Labs 6–7 |
| Optimize endpoint operations by using automation, monitoring, and reporting | Section 5, all integrated scenarios, and Lab 8 |

The review maps every July 24, 2026 subobjective to a device identity, enrollment, targeting, policy, application, access, operating, evidence, failure, or recovery decision. Three integrated scenarios, eight independent labs, and 36 original checks cover Entra registered/joined/hybrid devices; Windows/Android/Apple/macOS enrollment; RBAC/scope tags/multi-admin approval; compliance/Conditional Access/Hello/LAPS/local groups; Autopilot/device preparation/Windows 365/Backup; cross-platform profiles/filters; EPM/Enterprise App Management/Remote Help/Cloud PKI/Tunnel/Advanced Analytics; remote actions and KQL; endpoint security/Defender/App Control and cross-platform updates; app packaging/Microsoft 365 Apps/MAM; Graph/PowerShell/custom compliance; Security Copilot agents; and analytics/remediations/reporting/alerts. All 37 cited URLs are cataloged: 34 were reachable and the O'Reilly page plus two Udemy pages were automation-blocked; none was missing or broken. The guide records 29 hours 46 minutes of current Learn paths, the five-day course, free Practice Assessment, and July 2026 gaps in older resources. Fast-moving Autopilot, Intune Suite, agents, Hotpatch and Microsoft 365 Apps controls are marked **VERIFY CURRENT**. Blueprint SHA-256: `ba90e464c3a81deac207962ffe32e88c3ac6b0d966c33ba77572bb3d83910009`.

## MS-700 coverage record

| Official objective group | Guide coverage |
|---|---|
| Configure and manage a Teams environment | Section 1, all integrated scenarios, and Labs 1–4 |
| Manage teams, channels, chats, and apps | Section 2, shared-channel/app scenarios, and Lab 5 |
| Manage meetings and calling | Section 3, town-hall scenario, and Labs 6–7 |
| Monitor, report on, and troubleshoot Teams | Section 4, all integrated scenarios, and Lab 8 |

The review maps every July 29, 2026 subobjective to a Teams/Microsoft 365 object, entitlement, role, identity, policy, media/network, data, application, call flow, evidence, failure, or recovery decision. Three integrated scenarios, eight independent labs, and 36 original checks cover network capacity/ports/QoS/readiness; roles, Defender/Purview/Conditional Access; group/team/data lifecycle and policy assignment; external access/guests/shared channels/B2B direct connect/MTO; Teams Rooms/devices/VDI; teams/templates/frontline/channels/messaging/apps; meetings/appointments/webinars/town halls/Copilot; Teams Phone numbers/resource accounts/auto attendants/queues; usage/alerts/CQD/Call Analytics; and client/sign-in/media/meeting/AI troubleshooting. All 21 cited URLs are cataloged: 17 were reachable and two O'Reilly plus two Udemy pages were automation-blocked; none was missing or broken. The guide records 19 hours 1 minute of Learn paths, the four-day course, free Practice Assessment, and freshness gaps in commercial resources. MTO, Copilot/AI, meeting controls, device, VDI and troubleshooting behavior is marked **VERIFY CURRENT**. Blueprint SHA-256: `7b8312756006b9ee0f6b8e5fdb134797ef97c6ed27f664d0f518b8007cd03061`.

## MS-721 coverage record

| Official objective group | Guide coverage |
|---|---|
| Plan and design collaboration communications systems | Section 1, all integrated scenarios, and Labs 1–2 |
| Configure and manage Teams meetings, webinars, and town halls | Section 2, town-hall scenario, and Labs 3–4 |
| Implement and configure Teams Phone | Section 3, phone-migration scenario, and Labs 4–6 |
| Configure and manage Teams Rooms and devices | Section 4, Rooms sign-in scenario, and Labs 7–8 |

The review maps every April 28, 2026 subobjective to a meeting/event, identity, entitlement, number, policy, PSTN/carrier/SBC, network/media, device/room, evidence, failure, or recovery decision. Three integrated scenarios, eight independent labs, and 36 original checks cover meeting types/policies/templates/Premium/Copilot; Audio Conferencing; webinars, town halls and eCDN; Calling Plans, Operator Connect, Teams Phone Mobile, Direct Routing, Shared Calling and SMS; number lifecycle; SBC/SBA/LBR/LMO, compliance recording, contact centers and Queues app; network/QoS/CQD; voice-user policies; auto attendants and queues; emergency calling; Direct Routing implementation/troubleshooting; Rooms resource accounts/Conditional Access/enrollment; Windows, Android and SIP devices; BYOD/bookable desks; and device operations. All 19 cited URLs are cataloged: 18 were reachable and the O'Reilly page was automation-blocked; none was missing or broken. The guide records 14 hours 43 minutes of current Learn paths, the five-day course, free Practice Assessment, and April 2026 gaps in older commercial resources. Fast-moving Teams Premium, Copilot, Queues app, Android/MDEP, device and licensing behavior is marked **VERIFY CURRENT**. Blueprint SHA-256: `5167d7ad28df0c595db0836af19c921bc647da376dd96d029dbdf9f60555c5b0`.

## DP-600 coverage record

| Official objective group | Guide coverage |
|---|---|
| Maintain a data analytics solution | Section 1, all integrated scenarios, and Labs 1–2 |
| Prepare data | Section 2, all integrated scenarios, and Labs 3–5 |
| Implement and manage semantic models | Section 3, sales/performance scenarios, and Labs 6–8 |

The review maps every July 21, 2026 subobjective to a store, grain, transformation, query, identity/access layer, governance artifact, semantic-model behavior, lifecycle mechanism, performance signal, evidence, failure, or recovery decision. Three integrated scenarios, eight independent labs, and 36 original checks cover workspace/item/RLS/CLS/OLS/file controls; sensitivity labels and endorsement; Git, PBIP, templates, PBIDS, shared models, deployment, XMLA and impact analysis; lakehouse, warehouse, eventhouse, OneLake, catalog and Real-Time hub; Dataflows, notebooks, T-SQL, star schemas and quality; SQL, KQL and DAX; storage modes, relationships, calculations, large models, Direct Lake and incremental refresh; performance; and AI-ready semantics/Fabric IQ. All 16 cited URLs are cataloged: 14 were reachable and two O'Reilly pages were automation-blocked; none was missing or broken. The guide records 23 hours 20 minutes of current Learn paths, the four-day course, free Practice Assessment, and July 2026 gaps in older commercial resources. Fast-moving Direct Lake, OneLake security/integration, catalog, endorsement, Fabric IQ and data-agent behavior is marked **VERIFY CURRENT**. Blueprint SHA-256: `2b7d8452085a3503eaa3c72d3b5afd25ccb6dd2b42177e876d4c5d373051e3ec`.

## DP-700 coverage record

| Official objective group | Guide coverage |
|---|---|
| Implement and manage an analytics solution | Section 1, all integrated scenarios, and Labs 1–3 |
| Ingest and transform data | Section 2, all integrated scenarios, and Labs 4–6 |
| Monitor and optimize an analytics solution | Section 3, nightly-load scenario, and Labs 7–8 |

The review maps every July 21, 2026 subobjective to a configuration, identity/access layer, lifecycle mechanism, store, movement/transformation engine, grain/load contract, monitoring signal, failure boundary, optimization hypothesis, evidence, or recovery decision. Three integrated scenarios, eight independent labs, and 36 original checks cover Spark, domain, OneLake and Airflow settings; Git, database projects and deployment; layered access, masking, labels, endorsement and audit; Dataflow, pipeline and notebook orchestration; full, incremental, dimensional and streaming loads; lakehouse, warehouse, Eventhouse, shortcuts and mirroring; PySpark, SQL, KQL and data quality; Eventstream, Structured Streaming, windows and query acceleration; monitoring, alerts and every named error class; and lakehouse, pipeline, warehouse, Eventhouse, Eventstream, Spark and query optimization. All 27 cited URLs are cataloged: 26 were reachable and the O'Reilly early-release book was automation-blocked; none was missing or broken. The guide records 27 hours 49 minutes of current Learn paths, the four-day course, free Practice Assessment, an eight-hour O'Reilly bootcamp agenda, current commercial assessments, and explicit freshness/early-release caveats. Fast-moving Airflow, OneLake security, mirroring, query acceleration, Git/database-project and monitoring behavior is marked **VERIFY CURRENT**. Blueprint SHA-256: `b250753e6f60be9e2a9625e9849d575999dc56fc6afe43788a85ce43db5e25a8`.

## SC-401 coverage record

| Official objective group | Guide coverage |
|---|---|
| Implement information protection | Section 1, all integrated scenarios, and Labs 1–4 |
| Implement data loss prevention and retention | Section 2, all integrated scenarios, and Labs 5–7 |
| Manage risks, alerts, and activities | Section 3, all integrated scenarios, and Labs 2, 5, and 8 |

The review maps every July 28, 2026 subobjective to a data requirement, classifier, label, user/device/location context, preventive/detective control, priority, evidence, exception, failure, investigation, or recovery decision. Three integrated scenarios, eight independent labs, and 36 original checks cover built-in/custom SITs, fingerprinting, EDM, trainable classifiers, OCR and explorers; item/container labels, protection, publishing, auto-labeling and Cloud Apps; client/scanner and email encryption; unified and Endpoint DLP, Adaptive Protection, precedence and just-in-time protection; retention labels/policies, adaptive scopes, Policy lookup, disposition and recovery; Insider Risk roles/connectors/Defender/signals/templates/policies/forensic evidence/risk levels/cases/notices; Audit, Activity Explorer, DLP/insider/XDR/Cloud Apps alerts and eDiscovery; and Microsoft/third-party AI protection with current-versus-classic DSPM terminology. All 24 cited URLs are cataloged: 23 were reachable and the Udemy page was automation-blocked; none was missing or broken. The guide records 20 hours 45 minutes of current Learn paths, the four-day course, free Practice Assessment, current MeasureUp metadata, and July 2026 gaps in older or unverified provider content. Fast-moving OCR, label/workload, Endpoint DLP, Adaptive Protection, AI, and DSPM behavior is marked **VERIFY CURRENT**. No upcoming blueprint change or retirement was announced. Blueprint SHA-256: `5ca7d97c4a3ab4854779d477e20c4c2f6fc0b3ddeb987c6b63b8211127f51e85`.

## PL-300 coverage record

| Official objective group | Guide coverage |
|---|---|
| Prepare the data | Section 1, all integrated scenarios, and Labs 1–2 |
| Model the data | Section 2, all integrated scenarios, and Labs 3–4 and 8 |
| Visualize and analyze the data | Section 3, all integrated scenarios, and Labs 5–6 |
| Manage and secure Power BI | Section 4, regional-sales and operations scenarios, and Labs 7–8 |

The review maps every April 20, 2026 subobjective to a business requirement, grain, source/credential/privacy/gateway boundary, storage mode, quality/transformation/load rule, model relationship/calculation context, visual/interaction/accessibility decision, distribution/security/refresh control, evidence, failure, or recovery decision. Three integrated scenarios, eight independent labs, and 36 original checks cover shared models; Import, DirectQuery and Direct Lake; profiling and errors; Power Query folding/reference/duplicate/merge/append; fact/dimension keys; star schemas, date roles and relationships; DAX contexts, time/semi-additive measures, calculation groups and visual calculations; Performance Analyzer and DAX query view; visual selection, Copilot, paginated/mobile/accessibility and analysis; workspaces, apps, dashboards, distribution and endorsement; gateways and refresh; roles, item/model permissions, RLS and labels. All 25 cited URLs are cataloged: 22 were reachable and O'Reilly plus two Udemy pages were automation-blocked; none was missing or broken. The guide records 19 hours 52 minutes of current Learn paths, the three-day course, MIT official labs, free Practice Assessment, and current Reactor, Pluralsight, O'Reilly, Udemy, Coursera, Whizlabs and MeasureUp choices with explicit April 2026 freshness gaps. Fast-moving Direct Lake, Copilot, visual-calculation, workspace/app, licensing and label behavior is marked **VERIFY CURRENT**. No upcoming blueprint change or retirement was announced. Blueprint SHA-256: `4f6959b470d83a2a3095e739cb03912f957a60f07cd5108e70ddcf152ccd29ee`.

## MB-310 coverage record

| Official objective group | Guide coverage |
|---|---|
| Implement financial management | Section 1, all integrated scenarios, and Labs 1–4 |
| Implement accounts receivable, credit, collections, and subscription billing | Section 2, subscription-customer scenario, and Labs 4–5 |
| Implement and manage accounts payable and expenses | Section 3, capital-purchase scenario, and Lab 6 |
| Implement budgeting | Section 4, capital-purchase scenario, and Lab 7 |
| Manage fixed assets | Section 5, capital-purchase scenario, and Lab 8 |

The review maps every August 14, 2026 subobjective to an accounting object, configuration, source document, subledger/voucher/ledger effect, control, reconciliation, evidence, failure, or recovery decision. Three integrated scenarios, eight independent labs, and 36 original checks cover chart/dimensions/structures/tags/defaulting; ledgers/currencies/revaluation/layers/allocations; journals/Excel/batch/reversal/intercompany; cash/bank/payment/reconciliation/forecast/netting; close/consolidation/elimination/settlement/tax; AR/credit/collections/subscription billing/deferrals; AP/matching/payments/expenses; all three budgeting capabilities; and fixed-asset books/depreciation/acquisition/transfer/disposal. All 15 cited URLs are cataloged: 14 were reachable and the Udemy page was automation-blocked; none was missing or broken. The guide records 48 hours 30 minutes of selected official paths, the four-day course, official public labs, free Practice Assessment, and explicit August 2026 gaps in older commercial resources. Cost management is marked removed and asset leasing adjacent. Blueprint SHA-256: `f843902addfd9a29b5d0cfa9ae537ecc5a2afef4ca2b402013f08ed26d5e94d7`.

## MB-330 coverage record

| Official objective group | Guide coverage |
|---|---|
| Implement product information management | Section 1, all integrated scenarios, and Labs 1–2 |
| Implement inventory and asset management | Section 2, regulated-inbound and equipment-failure scenarios, and Labs 2–4 |
| Implement and manage supply chain processes | Section 3, regulated-inbound and customer-order scenarios, and Lab 5 |
| Implement warehouse management and transportation management | Section 4, regulated-inbound and customer-order scenarios, and Labs 6–7 |
| Implement master planning | Section 5, equipment-failure scenario, and Lab 8 |

The review maps every June 20, 2025 subobjective to a product, inventory, order, quality, asset, warehouse, mobile, transport, or planning object/state, configuration, evidence, failure, and recovery decision. Three integrated scenarios, eight independent labs, and 36 original checks cover product release/variants/dimensions/BOM/categories/attributes/cost/price; journals/orders/close/blocking/reports; quality; maintained assets; procurement, landed cost, sales/intercompany; warehouse layout/status/waves/work/directives/replenishment/counting/mobile/labels/containerization/cross-dock; transportation/routing/freight; and planning coverage/days/messages/fences/margins/firming. All 17 cited URLs are cataloged: 16 were reachable and the Udemy page was automation-blocked; none was missing or broken. The guide records 50 hours 7 minutes of selected official paths, the five-day course, MIT public labs, free Practice Assessment, and freshness boundaries for the year-old blueprint. Blueprint SHA-256: `d2256ab65b1fb5846cf0bcd68e769a0ce0cf7e64ad9ccfc709d5f9ba7866427a`.

## MB-500 coverage record

| Official objective group | Guide coverage |
|---|---|
| Plan the architecture and solution design | Section 1, all scenarios, and Lab 1 |
| Apply developer tools | Section 2, governed-extension scenario, and Lab 2 |
| Design and develop AOT elements | Section 3, governed-extension scenario, and Labs 3–4 |
| Develop and test code | Section 4, governed-extension scenario, and Labs 4–5 |
| Implement reporting | Section 5, executive-reporting scenario, and Lab 6 |
| Integrate and manage data solutions | Section 6, external-fulfillment scenario, and Lab 7 |
| Implement security and optimize performance | Section 7, all scenarios, and Lab 8 |

The review maps every January 30, 2026 subobjective to an architecture/environment, metadata, code, data, report, integration, or security artifact, lifecycle gate, automated test, performance signal, evidence, failure, or recovery decision. Three integrated scenarios, eight independent labs, and 36 original checks cover cloud/on-prem/ecosystem, UDE/PPAC/LCS/Implementation portal ALM, Visual Studio/Azure DevOps/CI/CD, AOT UI/data/classes and upgrade-safe extensibility, X++/queries/frameworks/testing, five reporting surfaces, APIs/entities/jobs/events/Power Platform/Key Vault, roles/XDS and trace-driven tuning. All 16 cited URLs are cataloged: 14 were reachable and O'Reilly/Udemy were automation-blocked; none was missing or broken. The guide records 43 hours 2 minutes of timed official paths plus reporting, the five-day course, MIT labs, free Practice Assessment and older-resource gaps. Blueprint SHA-256: `78eafb1665f8e4fb52988e1542e3d9bad30b1148ca533c6178e051668602c4ee`.

## MB-800 coverage record

| Official objective group | Guide coverage |
|---|---|
| Set up Business Central | Section 1, controlled-migration scenario, and Labs 1–3 |
| Configure financials | Section 2, migration and procure-to-pay scenarios, and Labs 4–5 and 8 |
| Configure sales and purchasing | Section 3, order-to-cash and procure-to-pay scenarios, and Lab 6 |
| Perform Business Central operations | Section 4, all scenarios, and Labs 5 and 7–8 |

The review maps every June 30, 2026 subobjective to a company/setup/master record, permission/control, business document, state transition, posting matrix, ledger entry, correction, reconciliation or evidence decision. Three integrated scenarios, eight independent labs and 36 original checks cover company migration, profiles/permission sets/security groups/filters/audit, number series/layouts/job queues/Copilot/agents, dimensions and approvals, G/L/chart/posting groups/journals/currency, receivables/payables/assets, inventory/items/SKUs/costing, prices/discounts, purchase/sales/prepayment/correction lifecycles, journals/payments/bank, fixed assets and inventory operations. All 15 cited URLs are cataloged: 13 were reachable and O'Reilly/Udemy were automation-blocked; none was missing or broken. The guide records 43 hours 40 minutes of official paths, the five-day course, MIT labs, free Practice Assessment, current commercial supplements and June-change freshness boundaries. Blueprint SHA-256: `29f5557d525b445ac9b0c44e81dd0298fba788ae62e53fa44e4a50eaeb7c7fff`.

## MB-820 coverage record

| Official objective group | Guide coverage |
|---|---|
| Describe Business Central | Section 1, compliance-extension scenario, and Lab 1 |
| Install, develop, and deploy for Business Central | Section 2, compliance-extension scenario, and Lab 2 |
| Develop by using AL objects | Section 3, all scenarios, and Labs 3–5 |
| Develop by using AL | Section 4, compliance/document scenarios, and Labs 5–6 |
| Work with development tools | Section 5, all scenarios, and Lab 7 |
| Integrate Business Central with other applications | Section 6, fulfillment-integration scenario, and Lab 8 |

The review maps every June 10, 2025 subobjective to an architecture/app/lifecycle boundary, AL project/configuration, object, procedure, Business Central data pattern, permission, test, telemetry/performance signal or HTTP/API contract. Three integrated scenarios, eight independent labs and 36 original checks cover online/on-prem, System/Base/extensions/AppSource, environment/dependency/debug/package/install/upgrade/language, tables/pages/enums/reports/XMLports/codeunits/interfaces/permissions/queries, UI/onboarding, standard master/document/ledger patterns, safe AL data/file/error behavior, Test Toolkit/custom tests, telemetry and resilient REST/JSON/API/action/Read Scale-Out integration. All 18 cited URLs are cataloged: 17 were reachable and O'Reilly was automation-blocked; none was missing or broken. The guide records 50 hours 7 minutes of selected official paths, the five-day course, MIT labs, free Practice Assessment, vetted live/commercial options and explicit older-blueprint freshness boundaries. Blueprint SHA-256: `dc84f7d5fecf0b048cb596c8401e0e8ce9f6a02ed481e05c1fda72938af76edf`.

## Databricks Machine Learning Professional coverage record

| Official objective group | Guide coverage |
|---|---|
| Model Development | Section 1, all integrated scenarios, and Labs 1–4 |
| ML Ops | Section 2, drift-retraining scenario, and Labs 5–7 |
| Model Deployment | Section 3, real-time/drift scenarios, and Lab 8 |

The review reconciles the detailed September 30, 2025 live-version PDF with the current three-domain page and uses current live delivery metadata where the PDF differs. Three scenarios, eight labs and 32 original checks cover Spark versus single-node; vertical/horizontal/model/data/trial/group parallelism; Ray and Optuna; nested MLflow and custom PyFunc; point-in-time, online and on-demand features; deploy-code lifecycle mapping; bundle environments; unit/integration gates; governed automated retraining; snapshot/time-series/inference monitoring; drift, slices, custom metrics, endpoint health and alerts; plus blue-green/canary/shadow rollout and custom-model REST/SDK serving. All 17 guide URLs are cataloged: 15 were reachable and the MLflow Optuna/O'Reilly pages were automation-blocked; none was missing or broken. DAB and Lakehouse Monitoring terminology is preserved as published and translated to current names; vendor sample questions are linked rather than reproduced. Blueprint SHA-256: `90c1a98f80cb5fb4bf172563055256b49ba45f967caa4bbe4a0d5a9b88d124f7`.

## Databricks Machine Learning Associate coverage record

| Official objective group | Guide coverage |
|---|---|
| Databricks Machine Learning | Section 1, all integrated scenarios, and Labs 3–4 and 6 |
| ML Workflows | Section 2, churn-model scenario, and Labs 1–2 |
| Model Development | Section 3, churn/fraud scenarios, and Labs 4–5 |
| Model Deployment | Section 4, fraud/streaming scenarios, and Labs 7–8 |

The review reconciles the detailed March 1, 2025 live-version PDF with the current four-domain page. It explicitly maps the live **ML Workflows** label to the PDF's **Data Processing** objectives and uses current live delivery metadata where the older PDF differs. Three scenarios, eight labs and 32 original checks cover MLOps/runtime/AutoML; Unity Catalog feature tables and MLflow tracking/registry; profiling/outliers/imputation/encoding/log transforms; algorithm/pipeline/imbalance/tuning/CV/metrics/bias-variance; and batch/stream/real-time deployment with canary evidence. All 16 guide URLs are cataloged: 15 were reachable and Udemy search was automation-blocked; none was missing or broken. Aged Delta Live Tables, workspace registry, Hyperopt and serving terminology is preserved as published and translated through current documentation; original vendor sample questions are linked rather than reproduced. Blueprint SHA-256: `2b414caebf75aedc46dc20a956d95c12d8f8b46213655d78768a1a7da9d56346`.

## Databricks Data Engineer Professional coverage record

| Official objective group | Guide coverage |
|---|---|
| Developing Code for Data Processing using Python and SQL | Section 1, all integrated scenarios, and Labs 1–3 and 8 |
| Data Ingestion & Acquisition | Section 2, regulated-events scenario, and Lab 2 |
| Data Transformation, Cleansing, and Quality | Section 3, regulated-events scenario, and Lab 3 |
| Data Sharing and Federation | Section 4, shared-supply-data scenario, and Lab 4 |
| Monitoring and Alerting | Section 5, failing-pipeline scenario, and Lab 5 |
| Cost & Performance Optimisation | Section 6, failing-pipeline scenario, and Lab 6 |
| Ensuring Data Security and Compliance | Section 7, regulated-events scenario, and Lab 7 |
| Data Governance | Section 8, all integrated scenarios, and Lab 7 |
| Debugging and Deploying | Section 9, failing-pipeline scenario, and Lab 8 |
| Data Modelling | Section 10, regulated-events scenario, and Labs 3 and 6 |

The review reconciles the detailed official live-version PDF dated July 3, 2026 with the live ten-domain weighted page checked September 1. Every objective maps to production code/configuration, data/state, identity, quality, observability, cost/performance, privacy, deployment, failure and recovery evidence. Three scenarios, eight labs and 37 original checks cover modular Python/bundles/dependencies/UDFs/tests; batch/stream acquisition; Lakeflow/Structured Streaming/AUTO CDC/control flow; transformations/quarantine; D2D/open sharing and federation; system tables/profiles/Spark/event/API evidence and alerts; managed-table maintenance/deletion vectors/skipping/clustering/CDF; layered access/privacy/purge; metadata/inheritance; repair/CI/CD; and Delta/dimensional modeling. All 30 guide URLs are cataloged: 28 were reachable and the O'Reilly/Udemy searches were automation-blocked; none was missing or broken. Commercial entries are explicitly discovery routes rather than claimed complete current courses, and the official retired sample questions are linked rather than reproduced. Blueprint SHA-256: `5c0abb75889e84a3f4b06c9ccf1d0598cf18b5e5edfaaa10e0b41b198fdd8c08`.

## Databricks Data Analyst Associate coverage record

| Official objective group | Guide coverage |
|---|---|
| Understanding of Databricks Data + AI Platform | Section 1, all integrated scenarios, and Lab 1 |
| Managing Data | Section 2, executive-dashboard scenario, and Labs 1–2 |
| Importing Data | Section 3, supplier-data scenario, and Lab 2 |
| Executing queries using Databricks SQL and Databricks SQL Warehouses | Section 4, all integrated scenarios, and Labs 3–4 |
| Analyzing Queries | Section 5, supplier-data scenario, and Lab 5 |
| Creating Dashboards and Visualizations in Databricks | Section 6, executive-dashboard scenario, and Lab 6 |
| Developing, Sharing, and Maintaining AI/BI Genie spaces | Section 7, trusted-sales-Genie scenario, and Lab 7 |
| Data Modeling with Databricks SQL | Section 8, executive-dashboard and trusted-sales-Genie scenarios, and Labs 3 and 7 |
| Securing Data | Section 9, all integrated scenarios, and Lab 8 |

The review reconciles the detailed official PDF current as of October 30, 2025 with the live nine-domain weighted certification page checked September 1, 2026. Every objective maps to a platform, data, SQL, model, compute, evidence, sharing, identity, failure or recovery decision. Three scenarios, eight labs and 36 original checks cover Catalog Explorer, certification/tags/lineage and Marketplace; governed cleanup and intake; ANSI SQL, warehouses, joins/sets/aggregates, managed/external tables, views, federation and history; Query Insights/profile/history, Photon, cache and clustering; AI/BI dashboards, parameters, sharing, embedding, refresh and alerts; grounded Genie spaces, Trusted Assets, benchmarks and feedback; star/snowflake/Data Vault; and layered Unity Catalog security. All 27 guide URLs are cataloged: 26 were reachable and the community forum was automation-blocked; none was missing or broken. The Academy course-replacement note is labeled as a learning-catalog transition rather than an exam announcement, commercial duration/freshness limitations are explicit, and vendor sample questions are linked rather than reproduced. Blueprint SHA-256: `84145c88ff4e5f780829aa1d29cf42da67b9a93e2be247338804daca37c7c6f4`.

## Databricks Data Engineer Associate coverage record

| Official objective group | Guide coverage |
|---|---|
| Databricks Intelligence Platform | Section 1, all integrated scenarios, and Lab 1 |
| Data Ingestion and Loading | Section 2, governed-incremental-orders scenario, and Labs 2–3 |
| Data Transformation and Modeling | Section 3, governed-incremental-orders and slow-consumer scenarios, and Labs 4 and 7 |
| Working with Lakeflow Jobs | Section 4, governed-incremental-orders scenario, and Lab 5 |
| Implementing CI/CD | Section 5, multi-environment-pipeline scenario, and Lab 6 |
| Troubleshooting, Monitoring, and Optimization | Section 6, slow-and-unsafe-consumer scenario, and Lab 7 |
| Governance and Security | Section 7, all integrated scenarios, and Lab 8 |

The review reconciles the detailed official PDF effective May 4, 2026 with the live seven-domain weighted certification page checked September 1. Every objective maps to mechanism, selection, state, identity, evidence, failure, and recovery decisions. Three scenarios, eight labs, and 36 original checks cover platform/compute; `COPY INTO`, Auto Loader, Lakeflow Connect and custom ingestion; schema/replay; PySpark/SQL transformation, joins, modeling, quality and tuning; Lakeflow Jobs; Git folders and Declarative Automation Bundles; run/Spark diagnosis; and Unity Catalog lifecycle, privileges and fine-grained controls. All 28 guide URLs are cataloged: 27 were reachable and the O'Reilly book was automation-blocked; none was missing or broken. Learning times and older-content gaps are explicit. The official sample questions are linked rather than reproduced. Blueprint SHA-256: `b2dca1b253c3174ca4d8a4f5bdf9d7e16ef624a5f34f717476a12dd460853081`.

## Databricks Generative AI Engineer Associate coverage record

| Official objective group | Guide coverage |
|---|---|
| Design Applications | Section 1, all integrated scenarios, and Labs 1 and 4 |
| Data Preparation | Section 2, governed-policy scenario, and Labs 2–3 |
| Application Development | Section 3, all integrated scenarios, and Labs 4–5 |
| Assembling and Deploying Apps | Section 4, support-action and analytics-supervisor scenarios, and Labs 6–7 |
| Governance | Section 5, all integrated scenarios, and Labs 2, 4 and 7 |
| Evaluation and Monitoring | Section 6, all integrated scenarios, and Labs 5 and 8 |

The review reconciles the detailed March 18, 2026 live-version PDF with the current six-domain weighted page and uses live assessment metadata where the PDF differs. Three scenarios, eight labs and 37 original checks cover requirement/prompt/task/chain/tool and Agent Bricks choices; governed extraction, chunking, embeddings, AI Search/Vector Search, retrieval metrics and reranking; model/framework selection, layered guardrails, Agent Framework and Genie/multi-agent behavior; packaging/registration, Foundation Model/batch inference, persistent state, CI/CD, prompt lifecycle, MCP and secure Apps; Unity Catalog, masking, source licensing and deletion controls; and traced evaluation, judges/scorers, inference/usage/cost monitoring and calibrated SME feedback. All 12 guide URLs are cataloged: 9 were reachable and the two Udemy pages plus O'Reilly search were automation-blocked; none was missing or broken. Agent Bricks, MCP, Apps, AI Search, MLflow evaluation, AI Gateway and prompt-management names and release stages are explicitly volatile; vendor sample questions are linked rather than reproduced. Blueprint SHA-256: `27994e2dbc5874f47708356b3ff39a38a9e98d835e9ddcb6cc7d6c9f322fc2ca`.

## Databricks Associate Developer for Apache Spark coverage record

| Official objective group | Guide coverage |
|---|---|
| Apache Spark Architecture and Components | Section 1, all integrated scenarios, and Lab 1 |
| Using Spark SQL | Section 2, daily-customer-file scenario, and Lab 2 |
| Developing Apache Spark™ DataFrame/DataSet API Applications | Section 3, all integrated scenarios, and Labs 3–4 |
| Troubleshooting and Tuning Apache Spark DataFrame API Applications | Section 4, skewed-clickstream scenario, and Lab 5 |
| Structured Streaming | Section 5, skewed-clickstream scenario, and Lab 6 |
| Using Spark Connect to deploy applications | Section 6, remote-application scenario, and Lab 7 |
| Using Pandas API on Apache Spark | Section 7, all integrated scenarios, and Labs 4 and 8 |

The review reconciles the detailed October 30, 2025 live-version PDF with the current seven-domain weighted page. It explicitly distinguishes the active 45-question, 90-minute, Python-focused, no-test-aid exam from the retired Spark 3.0 Python/Scala credential and stale commercial format metadata. Three scenarios, eight labs and 39 original checks cover driver/executor/resources, session/structured APIs, application-job-stage-task execution, partitions/shuffles/cache/GC/fault tolerance; schema-aware file/JDBC SQL I/O, modes/tables/views; column/null/dedup/aggregate/date/join/union/I/O/UDF/shared-variable operations; repartition/coalesce/skew/AQE/UI/log diagnosis; streaming output/state/watermark/checkpoint/recovery; Connect versus deployment modes; and Pandas API/Pandas UDF boundaries. All 11 guide URLs are cataloged: 7 were reachable and Databricks Community, two O'Reilly books and Udemy were automation-blocked; none was missing or broken. The broken Spark 4.2 pandas path discovered during review was replaced with its current canonical route, and vendor sample questions are linked rather than reproduced. Blueprint SHA-256: `b99b2c70f389d4626fa92d378fddd8caf10253dd24357b6bb5040e7f8a61430f`.

## AIF-C01 coverage record

| Official objective group | Guide coverage |
|---|---|
| Fundamentals of AI and ML | Section 1, all integrated scenarios, and Labs 1–2 |
| Fundamentals of GenAI | Section 2, all integrated scenarios, and Labs 3 and 7 |
| Applications of Foundation Models | Section 3, all integrated scenarios, and Labs 3–5 |
| Guidelines for Responsible AI | Section 4, all integrated scenarios, and Labs 5–6 and 8 |
| Security, Compliance, and Governance for AI Solutions | Section 5, all integrated scenarios, and Labs 6–8 |

The review reconciles revision 1.0 dated March 26, 2026 with the live certification page, five detailed domain pages, and current in-scope list. It explicitly covers the added agentic AI, MCP, multi-agent communication, memory/tool/workflow, Amazon Quick, Kiro, Strands Agents, and Bedrock AgentCore scope and treats older courses as gap-fill resources. Three scenarios, eight safe labs and 35 original checks cover rules/traditional ML/FM/agent choices; problem/data/lifecycle/metric alignment; tokens, context and adaptation; RAG, prompting and evaluation; responsible-AI evidence; and identity, data, application, tool, monitoring and governance controls. All 25 guide URLs are cataloged: 23 were reachable and O'Reilly and Udemy were automation-blocked; none was missing or broken. Product names, release stages, regions, service behavior, price and learning metadata are labeled volatile. The guide links official/vendor practice but uses no recalled questions. Blueprint SHA-256: `7ff78e9b2aac28fcc1440e8465c85e881dca3010fdb837e51de552f6ae5118f6`.

## AIB-C01 coverage record

| Official objective group | Guide coverage |
|---|---|
| AI Fundamentals and Literacy | Section 1, all integrated scenarios, and Labs 1 and 5 |
| AI Strategy and Business Value Creation | Section 2, all integrated scenarios, and Labs 2–4 and 8 |
| AI Governance and Responsible AI Leadership | Section 3, all integrated scenarios, and Labs 5–6 and 8 |
| Business Readiness, Leadership, and AI Transformation | Section 4, all integrated scenarios, and Labs 7–8 |

The review captures the initial September 1, 2026 four-domain beta blueprint and launch materials before delivery begins September 29. It makes the 170-minute/85-question live beta contract distinct from the detailed guide's 130-minute standard-duration statement, and treats GA format, scoring, languages, dates and learning assets as pending. Three scenarios, eight document-based labs and 36 original checks cover solution-type and data decisions; use-case portfolios, build/buy/partner, baselines, TCO/ROI, metrics and durable advantage; principle tradeoffs, governance operating models, risk tiers and lifecycle evidence; plus capability maturity, change, workforce adoption and pilot-to-scale gates. All 16 guide URLs are cataloged: 13 were reachable and ISO, O'Reilly and Udemy were automation-blocked; none was missing or broken. The exact AWS 13-module and exam-prep routes are separated from adjacent learning, and the absence of a beta official practice exam and mature third-party AIB-C01 catalog is explicit. Blueprint SHA-256: `84365cfe2180906cec213c48075b2823a10204c07eb9b01f983fb0817a58255d`.

## CLF-C02 coverage record

| Official objective group | Guide coverage |
|---|---|
| Cloud Concepts | Section 1, all integrated scenarios, and Labs 2–3 and 7 |
| Security and Compliance | Section 2, regulated-analytics scenario, and Labs 1, 4–5 and 8 |
| Cloud Technology and Services | Section 3, all integrated scenarios, and Labs 2–6 |
| Billing, Pricing, and Support | Section 4, all integrated scenarios, and Labs 1, 7–8 |

The review reconciles the current four-domain CLF-C02 guide with its detailed domain pages, in-scope service list and live certification page. It preserves the official 24/30/34/12 percent weighting, the 50-scored-plus-15-unscored contract and the foundational out-of-scope boundary while adding decision depth rather than implementation trivia. Three scenarios, eight safe labs and 30 original checks cover cloud value and economics; Well-Architected and adoption context; shared responsibility, IAM, governance, monitoring and protection; global infrastructure and compute/storage/database/network/service-category selection; and pricing, allocation, budgets, optimization and support. All 29 guide URLs are cataloged: 25 were reachable and two AWS decision-guide routes, O'Reilly and Udemy were automation-blocked; none was missing or broken. Service behavior, prices, support entitlements, console interfaces and commercial metadata are labeled as volatile, and the guide uses no recalled exam questions. Blueprint SHA-256: `f7672b5ced01847d85eb6909ef171881785be1263868286068422231d7b7a5da`.

## SOA-C03 coverage record

| Official objective group | Guide coverage |
|---|---|
| Monitoring, Logging, Analysis, Remediation, and Performance Optimization | Section 1, all integrated scenarios, and Labs 1–3 and 8 |
| Reliability and Business Continuity | Section 2, integrated scenarios 1–2, and Labs 3–4 and 8 |
| Deployment, Provisioning, and Automation | Section 3, integrated scenarios 1–2, and Labs 2, 5, and 8 |
| Security and Compliance | Section 4, integrated scenarios 2–3, and Labs 6 and 8 |
| Networking and Content Delivery | Section 5, integrated scenarios 2–3, and Labs 7–8 |

The review reconciles the current five-domain SOA-C03 blueprint, detailed domain pages, in-scope service list, comparison appendix, and live certification page. It explicitly separates SOA-C03 from the retired six-domain SOA-C02 blueprint and covers the newer CloudOps name plus containers, multi-account and multi-Region operations, CDK, Terraform and Git, Kiro, AWS DevOps Agent, AWS Security Agent, and Amazon S3 Files scope. Three integrated scenarios, eight safe labs, and 40 original checks cover evidence-chain troubleshooting; metrics, logs, traces, alarms, remediation, and performance; scaling, availability, backup, RTO/RPO, and disaster recovery; images, IaC, deployments, and automation; identity, SCPs, encryption, findings, and compliance evidence; and VPC, DNS, edge, and network diagnosis. All 26 guide URLs are cataloged: 24 were reachable and O'Reilly and Udemy were automation-blocked; none was missing or broken. Service behavior, release stages, regions, pricing, exam metadata, and commercial learning metadata are labeled volatile, and the guide uses no recalled exam questions. Blueprint SHA-256: `0ad821a84709cd5d39eb724aa1b3c040d14f67e4e705ac3fdc7f129021cec466`.

## DEA-C01 coverage record

| Official objective group | Guide coverage |
|---|---|
| Data Ingestion and Transformation | Section 1, all integrated scenarios, and Labs 1–4 and 8 |
| Data Store Management | Section 2, integrated scenarios 1–2, and Labs 1, 3, and 5 |
| Data Operations and Support | Section 3, all integrated scenarios, and Labs 3–6 and 8 |
| Data Security and Governance | Section 4, all integrated scenarios, and Labs 7–8 |

The review reconciles the December 12, 2025 version 1.1 DEA-C01 guide with its four detailed domain pages, current in-scope list, revision record, and live certification page. It explicitly closes the additions for LLM processing, Iceberg/open-table formats, HNSW/IVF vector indexes, vectorization and Bedrock knowledge bases, SageMaker Catalog/Unified Studio governance, and service-scope changes while labeling older version 1.0 training as incomplete. Three integrated scenarios, eight safe labs, and 40 original checks cover batch, stream, CDC and API contracts; partitioning, checkpointing, idempotency and replay; Glue/Spark and orchestration; store, model, format, catalog, lineage, lifecycle and schema decisions; SQL, monitoring, troubleshooting and data quality; plus IAM, Lake Formation, KMS, masking, audit, privacy, sharing and sovereignty. All 28 guide URLs are cataloged: 25 were reachable and two O'Reilly books plus Udemy were automation-blocked; none was missing or broken. Product names, features, limits, price, delivery and commercial-learning metadata are labeled volatile, and the guide uses no recalled exam questions. Blueprint SHA-256: `5a5952f0c845f8757499fade268fd25b2689663589c2734d82379d2a49c0196f`.

## DVA-C02 coverage record

| Official objective group | Guide coverage |
|---|---|
| Development with AWS Services | Section 1, all integrated scenarios, and Labs 1–3 and 8 |
| Security | Section 2, integrated scenarios 1–2, and Labs 4–5 and 8 |
| Deployment | Section 3, integrated scenario 2, and Labs 6–7 |
| Troubleshooting and Optimization | Section 4, integrated scenario 3, and Labs 3, 7, and 8 |

The review reconciles the current version 2.1 DVA-C02 guide with its four weighted domain pages, technologies/concepts page, service scope, revision record, and live certification page. It explicitly maps the added EventBridge, third-party resilience, near-real-time Lambda, specialized-store, fine-grained/cross-service authorization, masking/multi-tenancy, AppConfig, event-test, health/readiness, caching, Q Developer, and performance skills and notes removed service scope. It also keeps AWS's AI-assisted development, AI security, testing, CI/CD, error-analysis and optimization list separate as possible unscored pretest material rather than scored objectives. Three scenarios, eight safe labs and 40 original checks cover SDK/API resilience; serverless events, messages, streams and data; authentication, tenant authorization, KMS, secrets and masking; artifacts, SAM/IaC, tests, configuration, deployment and rollback; plus telemetry, incident evidence, concurrency, caching and measured optimization. All 25 guide URLs are cataloged: 21 were reachable and two O'Reilly plus two Udemy pages were automation-blocked; none was missing or broken. Volatile product, exam and learning metadata is labeled, and the guide uses no recalled exam questions. Blueprint SHA-256: `8fbdbecdbab1931b6307b0afcf33b5bf3cc81937d40563ea4209c4eb18db8b0c`.

## MLA-C01 coverage record

| Official objective group | Guide coverage |
|---|---|
| Data Preparation for Machine Learning | Section 1, all integrated scenarios, and Labs 1–3 and 8 |
| ML Model Development | Section 2, all integrated scenarios, and Labs 4 and 6–7 |
| Deployment and Orchestration of ML Workflows | Section 3, all integrated scenarios, and Labs 5–7 |
| ML Solution Monitoring, Maintenance, and Security | Section 4, all integrated scenarios, and Labs 7–8 |

The review reconciles the complete retiring MLA-C01 blueprint with all four detailed domain pages, current service scope, the live credential transition notice, and the public MLA-C02 replacement guide. It prominently records the September 28, 2026 English cutoff, continued Korean/Japanese/Simplified Chinese C01 delivery until C02 general availability, and ME1-C02 English beta delivery code; it also makes C02's explicit foundation-model, generative-AI, Amazon Bedrock, and agentic-workflow expansion a study boundary rather than implying that a C01 course is enough. Three scenarios, eight safe labs and 40 original checks cover data contracts, formats, batch/stream behavior, quality, leakage, features, bias and protection; approach/algorithm selection, reproducible training, tuning, metrics and approval; inference modes, containers, IaC, autoscaling, pipelines, tests, canaries and retraining; plus drift, telemetry, cost, quotas, IAM, KMS, private networking and artifact security. All 17 external guide URLs are cataloged: 14 were reachable and O'Reilly plus two Udemy pages were automation-blocked; none was missing or broken. The replacement is a local link to the separately validated C02 page. Volatile exam, service, price and provider metadata is labeled, and the guide uses no recalled exam questions. Blueprint SHA-256: `91c5a0ed3fae7d2606bfed410b968599e65b38d058eb0047ef72d7b03e0ab4b7`.

## MLA-C02 coverage record

| Official objective group | Guide coverage |
|---|---|
| Data Preparation for ML and AI | Section 1, all integrated scenarios, and Labs 1–3 and 8 |
| ML Model and Foundation Model Development | Section 2, all integrated scenarios, and Labs 4–5 and 7 |
| Deployment and Orchestration of ML and AI Workflows | Section 3, all integrated scenarios, and Labs 6–8 |
| Operating, Monitoring, and Securing ML and AI Solutions | Section 4, all integrated scenarios, and Labs 5–8 |

The review captures the complete initial September 1, 2026 MLA-C02 beta blueprint, all four detailed domain pages, exact C01 comparison, live credential page and launch announcement. It preserves traditional ML/MLOps while mapping every added vector-database, multimodal-data, embedding, RAG preparation/monitoring, FM selection/customization/deployment, Bedrock evaluation/prompt, human/LLM judge, knowledge/index, agent/tool/protocol/state/version, GPU/AI scaling, generative/agent observability, token/vector/agent cost, vulnerability, credential and Guardrails skill. Three scenarios, eight safe labs and 42 original checks cover data/features/chunks/embeddings/vectors; traditional and FM selection/customization; retrieval/generation/human/judge evaluation; model/knowledge/prompt/agent/tool/state delivery; and layered monitoring, unit economics and security. The ME1-C02 beta appointment code, September 29 delivery, 170-minute/85-question/USD-75/English-only contract, typical result timing and early-2027 standard plan are explicit and volatile. All 16 guide URLs are cataloged: 15 were reachable and the O'Reilly C01 foundation book was automation-blocked; none was missing or broken. The launch-day absence of mature exact commercial paths and the C01 internals still visible on a newly C02-labeled practice page are stated rather than hidden. No recalled questions are used. Blueprint SHA-256: `81bd9db7252f56b633e9666c692b98ad8806a21b3602497b82600522070299d7`.

## SAA-C03 coverage record

| Official objective group | Guide coverage |
|---|---|
| Design Secure Architectures | Section 1, all integrated scenarios, and Labs 2–3, 6, and 8 |
| Design Resilient Architectures | Section 2, all integrated scenarios, and Labs 4 and 6–8 |
| Design High-Performing Architectures | Section 3, all integrated scenarios, and Labs 3, 5, and 7–8 |
| Design Cost-Optimized Architectures | Section 4, all integrated scenarios, and Labs 1, 5, and 7–8 |

The review reconciles the current four-domain SAA-C03 blueprint with all detailed domain pages, the live certification page and the non-exhaustive official service list. It organizes the large service surface around requirement-driven decisions, trust/failure boundaries, end-to-end paths, measurable failure testing, total cost and operational ownership rather than treating the exam as a catalog-memory exercise. Three integrated scenarios, eight safe labs and 42 original checks cover federation, multi-account access, IAM evaluation, request-path defense and data protection; queues/events/streams, idempotency, scaling, caching, Multi-AZ design and measurable disaster recovery; compute, storage, database, hybrid network, load-balancing and ingestion choices; plus commitments, right-sizing, lifecycle, data-transfer and total-system cost. All 20 external URLs are cataloged: 18 were reachable and O'Reilly plus Udemy were automation-blocked; none was missing or broken. Service behavior, regions, quotas, price, free-tier, interface and learning metadata are labeled volatile. No recalled exam questions are used. Blueprint SHA-256: `1bc3fe0024229545cd208ae873b0d02844ef3553bbc94eb99fea07be60b717ce`.

## DOP-C02 coverage record

| Official objective group | Guide coverage |
|---|---|
| SDLC Automation | Section 1, Integrated scenarios 1 and 3, and Labs 1–2 |
| Configuration Management and IaC | Section 2, Integrated scenarios 1–2, and Labs 3–4 |
| Resilient Cloud Solutions | Section 3, all integrated scenarios, and Labs 2 and 6–7 |
| Monitoring and Logging | Section 4, all integrated scenarios, and Labs 2 and 5–7 |
| Incident and Event Response | Section 5, Integrated scenarios 2–3, and Labs 5–7 |
| Security and Compliance | Section 6, Integrated scenarios 1–2, and Labs 1, 4, and 8 |

The review reconciles the current six-domain DOP-C02 blueprint with every detailed domain page, the live certification page and the non-exhaustive official service list. It treats DevOps as a complete evidence loop rather than a list of Code services. Three integrated scenarios, eight safe labs and 42 original checks cover build-once provenance and immutable promotion; testing, secrets, artifacts and deployment/database compatibility; reusable CloudFormation/CDK/SAM/Terraform components, desired-state drift and multi-account onboarding; measured scaling, bounded self-healing, backup and regional recovery; centralized SLO/metric/log/trace/deployment/audit/security telemetry; evidence-preserving diagnosis, runbooks and game days; plus pipeline identities, supply-chain controls, findings, data protection and auditable continuous compliance. All 18 external URLs are cataloged: 17 were reachable and Udemy was automation-blocked; none was missing or broken. Changing service, integration, region, quota, price and learning details are labeled volatile. No recalled exam questions are used. Blueprint SHA-256: `b9484c48770968d736ef141383ef32e85b8f372496e29adeedb9d2d7b4a9f1d9`.

## AIP-C01 coverage record

| Official objective group | Guide coverage |
|---|---|
| Foundation Model Integration, Data Management, and Compliance | Section 1, all integrated scenarios, and Labs 1–3, 7–8 |
| Implementation and Integration | Section 2, all integrated scenarios, and Labs 3–6, 8 |
| AI Safety, Security, and Governance | Section 3, all integrated scenarios, and Labs 1–2, 5, 7–8 |
| Operational Efficiency and Optimization for GenAI Applications | Section 4, all integrated scenarios, and Labs 3, 6, and 8 |
| Testing, Validation, and Troubleshooting | Section 5, all integrated scenarios, and Labs 3–8 |

The review reconciles the current standard five-domain AIP-C01 blueprint with every detailed domain page, the live certification page, the non-exhaustive official service list and AWS's March 2026 post-beta scope refresh. It treats production GenAI as an evidence-bearing system rather than model trivia. Three integrated scenarios, eight safe labs and 42 original checks cover use-case/evaluation contracts, multimodal data rights and lineage, chunks/embeddings/hybrid retrieval/reranking, prompt lifecycles, bounded tool-using agents and human approval, streaming/asynchronous integration, layered safety/privacy/identity/network controls, token/latency/cost optimization, observability, multi-perspective evaluation and troubleshooting. All 17 unique external URLs are cataloged: 15 were reachable and two Udemy routes were automation-blocked; none was missing or broken. Model/service/region/API/quota/price and training metadata are labeled volatile. The guide explicitly separates the current AgentCore-era standard exam from early beta outlines and unofficial codes. No recalled exam questions are used. Blueprint SHA-256: `b5654086954cdac1322092486e79c2b90267a3848117954fd153f40b490597cf`.

## SAP-C02 coverage record

| Official objective group | Guide coverage |
|---|---|
| Design Solutions for Organizational Complexity | Section 1, all integrated scenarios, and Labs 1–3, 6, and 8 |
| Design for New Solutions | Section 2, Integrated scenarios 1–2, and Labs 2–6 and 8 |
| Continuous Improvement for Existing Solutions | Section 3, all integrated scenarios, and Labs 3–6 and 8 |
| Accelerate Workload Migration and Modernization | Section 4, Integrated scenario 3, and Labs 2 and 7–8 |
| Emerging topics (unscored pretest) | Dedicated emerging-topic section and Checks 39–41; explicitly excluded from scored weights |

The review reconciles the current four-domain SAP-C02 blueprint with every detailed domain page, the live certification page, the non-exhaustive service list, and the separately labeled unscored emerging-topic section. It treats professional architecture as traceable enterprise decision-making rather than a larger service list. Three scenarios, eight safe labs and 42 original checks cover hybrid/global routing and DNS, multi-account identity/governance, layered security, organization-scale cost visibility, distributed reliability and recovery, immutable delivery/data compatibility, evidence-led improvement, portfolio/7R/wave decisions, transfer/database/application migration, modernization and decommissioning. All 18 external URLs are cataloged: 14 were reachable and three O'Reilly routes plus Udemy were automation-blocked; none was missing or broken. Changing service, integration, Region, quota, SLA, price, purchase, migration-tool and training details are labeled volatile. Responsible/agentic-AI controls remain explicitly separated as possible unscored pretest content. No recalled exam questions are used. Blueprint SHA-256: `a26c57062d9b296a68c6977a3eccb000e1dd64d57c67ffff43a4776da813588d`.

## ANS-C01 coverage record

| Official objective group | Guide coverage |
|---|---|
| Network Design | Section 1, all integrated scenarios, and Labs 1–7 |
| Network Implementation | Section 2, all integrated scenarios, and Labs 2–5 and 8 |
| Network Management and Operation | Section 3, all integrated scenarios, and Labs 1–3 and 5–8 |
| Network Security, Compliance, and Governance | Section 4, all integrated scenarios, and Labs 1–2 and 5–8 |

The review reconciles the current four-domain ANS-C01 blueprint with every detailed domain page, the non-exhaustive service list, and the live English certification page. It separately records the December 31, 2026 retirement, the superseded August 25 date still visible on some localized pages, and the absence of a named replacement. Three scenarios, eight safe labs and 42 original checks cover edge/global ingress, authoritative/private/hybrid DNS, ALB/NLB/GWLB, BGP and Direct Connect/VPN/TGW Connect, multi-account/Region/VPC topology, IaC and semantic reachability tests, layered packet troubleshooting, ENI/ENA/EFA/MTU, cost/reliability, SG/NACL/WAF/firewall/GWLB controls, multi-source audit and TLS/IPsec/MACsec/DNSSEC/PKI boundaries. All 16 external URLs are cataloged: 11 were reachable and three O'Reilly plus two Udemy routes were automation-blocked; none was missing or broken. Changing lifecycle, service, route-preference, Region, quota, bandwidth, MTU, encryption, price and training details are labeled volatile. No recalled exam questions are used. Blueprint SHA-256: `6e641ee1f39d66f182de5da5a84b2664cae1c119bc4377faa184f6de05d64e01`.

## SCS-C03 coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: six current domains—Detection (16%), Incident Response (14%), Infrastructure Security (18%), Identity and Access Management (20%), Data Protection (18%), and Security Foundations and Governance (14%)
- Coverage evidence: guide sections 1–6, three integrated scenarios, eight hands-on labs, 42 original checks, and an explicit C02-to-C03 transition checklist
- Link evidence: 18 unique external URLs; 16 reachable, two automation-blocked, zero missing/broken in the dated source-health run
- Volatile boundaries: exam delivery, revisions, in-scope services, product features and names, Organizations/IAM/KMS behavior, Regions, quotas, price, course revision, duration, and access

The review reconciles the root SCS-C03 guide with every detailed domain page, the live certification page, non-exhaustive service list, and AWS's official C02-to-C03 comparison. It records both official candidate-experience descriptions rather than flattening them, and gives old C02 learning material a concrete gap checklist covering the six-domain split, finding validation, OCSF, third-party WAF rules, GenAI protections, inter-resource encryption, imported key material, masking, and multi-Region keys/certificates. Three scenarios, eight safe labs and 42 original checks cover protected telemetry, evidence-preserving response, edge/compute/GenAI/network controls, authentication and layered authorization, KMS/secret/certificate/backup controls, account guardrails, IaC and audit evidence. All 18 URLs are cataloged: 16 were reachable and two Udemy routes were automation-blocked; none was missing or broken. Changing delivery, service and training details are labeled volatile. No recalled exam questions are used. Blueprint SHA-256: `aa33d827db1d7b239d34aca34ad3c1a6be21faf2d0d6b34d03d329f4d46d177f`.

## EX200 coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: ten unweighted RHEL 10 performance groups covering tools, software, scripts, running systems, storage, filesystems, deployment/maintenance, networking, users/groups, and security
- Coverage evidence: guide sections 1–10, three integrated scenarios, eight performance labs, 40 original checks, and a RHEL 9-to-10 gap checklist
- Link evidence: 12 unique external URLs; 10 reachable, two automation-blocked, zero missing/broken in the dated source-health run
- Volatile boundaries: exam delivery, RHEL 10 minor version, objective text, product behavior, course version, runtime, schedule, price, and access

The review reconciles every public EX200 task with RHEL 10 documentation and current official RH124/RH134/RH199 preparation routes. It treats the exam as observable system administration, not command trivia: every lab follows inspect → minimal change → runtime/policy validation → persistence → reboot → revalidation → recovery. Three scenarios, eight safe labs and 40 original checks cover shell/local documentation, RPM and Flatpak, defensive Bash, boot/process/systemd/logging, GPT/LVM/filesystems/NFS/autofs, schedulers/time/bootloader, IPv4/IPv6/NetworkManager/firewalld, users/sudo/aging, SSH and SELinux. All 12 URLs are cataloged: 10 were reachable and two O'Reilly routes were automation-blocked; none was missing or broken. RHEL 9 resources have an explicit RHEL 10 gap boundary and no recalled exam tasks are used. Blueprint SHA-256: `69fa2bc5a08fc6c1cf183b89d6123a1564edab0d8e0e3ca12f80bc70b45916d4`.

## EX294 coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: eight unweighted current task groups covering RHCSA foundations, Ansible components, control/managed-node configuration, navigator and development workflows, resilient playbooks, roles/collections, automated RHEL administration, templates, and Vault
- Coverage evidence: guide sections 1–8, three integrated scenarios, eight performance labs, 40 original checks, and an explicit old-course/current-page gap checklist
- Link evidence: eight unique external URLs; five reachable, three automation-blocked, zero missing/broken in the dated source-health run
- Volatile boundaries: purchasable exam version, RHEL/AAP/Ansible versions, objectives, product behavior, course revision, duration, schedule, price, and access

The review reconciles every public EX294 task with the current AU294 baseline of RHEL 10, Ansible Core 2.16, and development tools aligned with Ansible Automation Platform 2.5/2.6. It preserves Red Hat's warning that multiple exam versions may be purchasable and explains the current Advanced System Administrator in Ansible credential name versus older RHCE course labels. Three scenarios, eight safe labs and 40 original checks cover inventories, controller/managed-node configuration, execution environments and collections, navigator, Git and VS Code development containers, modules, conditions and error handling, roles, RHEL administration, templates, Vault, idempotence, second-run evidence, and replay against fresh hosts. All eight URLs are cataloged: five were reachable and O'Reilly plus two Udemy routes were automation-blocked; none was missing or broken. Older material has an explicit gap checklist and no recalled exam tasks are used. Blueprint SHA-256: `e95d8682f731a4bd566b4bac9f0695ee8c46977a595f1eb99402a041cafd0376`.

## EX280 coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: nine unweighted task groups covering platform management, declarative resources, application deployment, authentication/authorization, network security, non-HTTP/SNI exposure, developer self-service, Operators, and application security
- Coverage evidence: guide sections 1–9, three integrated scenarios, eight performance labs, 40 original checks, and an explicit 4.18/4.22 assigned-version checklist
- Link evidence: 12 unique external URLs; ten reachable, two automation-blocked, zero missing/broken in the dated source-health run
- Volatile boundaries: assigned exam version, objectives, APIs, console/CLI behavior, networking, Operators, SCCs, course version, environment limits, delivery, price, duration, schedule, and access

The review reconciles every public EX280 task with the live page and official 4.18 and 4.22 documentation. It preserves the page's internal 4.22 headline/4.18 delivery conflict and its explicit instruction that the LMS-assigned version is binding. Three scenarios, eight safe labs and 40 original checks cover console/CLI evidence, images and layered troubleshooting, clean manifests and Kustomize, Deployments/templates/Helm/configuration, HTPasswd and least-privilege RBAC, packet paths/routes/TLS/NetworkPolicy/L4 exposure, quotas/limits/project templates, Operator lifecycle, service accounts/SCCs/secrets/Jobs/CronJobs, and declarative replay. All 12 URLs are cataloged: ten were reachable and O'Reilly plus Udemy were automation-blocked; none was missing or broken. Older content has an explicit assigned-version gap checklist and no recalled exam tasks are used. Blueprint SHA-256: `7f06f83b3e8c273d4c24065c54ad45411416e25aa528a8651e7e74016c724040`.

## EX378 coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: 11 unweighted Red Hat Build of Quarkus 3.8 coding groups covering configuration, fault tolerance, health, metrics, MP-JWT, REST, Panache, reactive messaging, OpenAPI, REST clients, and OpenTelemetry
- Coverage evidence: guide sections 1–11, three integrated microservice scenarios, eight coding labs, 40 original checks, and an explicit newer/older-course-to-3.8 gap checklist
- Link evidence: nine unique external URLs; seven reachable, two automation-blocked, zero missing/broken in the dated source-health run
- Volatile boundaries: objectives, Red Hat BOM/extension support, documentation, APIs, Java/runtime requirements, course versions/runtimes/access, delivery, price, and schedule

The review reconciles all 11 EX378 task groups with Red Hat Build of Quarkus 3.8 documentation and the archived upstream 3.8 guide set. The guide evolves one persistent service so configuration, resilience, health, metrics, MP-JWT, RESTEasy Reactive/Jakarta REST, Panache/JPA, Reactive Messaging, OpenAPI, REST Client Reactive and OpenTelemetry are exercised together. Three scenarios, eight safe labs and 40 original checks cover positive and negative paths, database/transaction state, acknowledgment/redelivery, blocking boundaries, telemetry correlation and package-mode restart. All nine URLs are cataloged: seven were reachable and O'Reilly plus Udemy were automation-blocked; none was missing or broken. Newer resources have an explicit 3.8 API/name gap checklist and no recalled exam tasks are used. Blueprint SHA-256: `68272e22e491f3168f3e9c1eaf2520a0be7b132212234e221135205fc9e9ec1a`.

## EX267 coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: 12 unweighted OpenShift AI 3.3 task groups on OpenShift 4.20, including a final deploy/store refinement of the earlier model-serving group
- Coverage evidence: guide sections 1–10, three lifecycle scenarios, eight performance labs, 40 original checks, and an explicit older/newer-to-3.3/4.20 gap checklist
- Link evidence: ten unique external URLs; eight reachable, two automation-blocked, zero missing/broken in the dated source-health run
- Volatile boundaries: objective text, OpenShift AI/OpenShift versions, dashboard/API/CRD behavior, serving modes/runtimes, model catalog/licenses, hardware, course revision, access, price, delivery, and duration

The review reconciles all public EX267 tasks with the Red Hat OpenShift AI 3.3 and OpenShift Container Platform 4.20 baselines. It treats the repeated deploy/store group as an explicit refinement rather than an invented weighted domain. Three scenarios, eight safe labs and 40 original checks follow governed predictive, LLM, and RAG/agentic lifecycles through projects, permissions, workbenches, custom images, connections, placement, Git/training, pipelines/experiments, OCI/registry lineage, KServe with OpenVINO/vLLM/custom runtimes, TrustyAI/hardware monitoring, compression/LMEval, streaming, retrieval, tools, guardrails, persistence, and rollback. All ten URLs are cataloged: eight reachable and O'Reilly plus Udemy automation-blocked; none missing or broken. Older 2.x and rolling content has an explicit 3.3/4.20 gap checklist, and no gated course labs or recalled exam tasks are used. Blueprint SHA-256: `b741b76b2ba6259872d38449c397048d494185090c80d53064aa5d9ab32208fe`.

## FC0-U71 coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: six weighted V6 domains—Tech concepts and terminology (13%), Infrastructure (24%), Applications and software (18%), Software development concepts (13%), Data and database fundamentals (13%), and Security (19%)
- Coverage evidence: guide sections 1–6, three cross-domain scenarios, eight safe labs, 40 original checks, and explicit FC0-U71/FC0-U71-CE lifecycle wording
- Link evidence: ten unique external URLs; eight reachable, two automation-blocked, zero missing/broken in the dated source-health run
- Volatile boundaries: objectives, delivery, credential-series validity, languages, passing score, hardware/network/software/AI behavior, and provider revision, duration, bundle, price, and access

The review maps every public V6 domain and listed subtopic to a connected beginner mental model rather than professional-level trivia. Three scenarios, eight labs and 40 original checks cover the computing cycle, notation and units, controlled troubleshooting, devices/components/storage/interfaces, peripherals, virtualization/cloud responsibility, basic networks/Wi-Fi, operating systems/files/applications/browsers/AI, programming representations and control flow, relational/non-relational data and restore evidence, CIA/identity/device hygiene/passwords/encryption/social engineering, and safe escalation. All ten URLs are cataloged: eight reachable and O'Reilly plus Udemy automation-blocked; none missing or broken. The official page's no-expiration FC0-U71 and five-year FC0-U71-CE distinction is preserved. No proprietary objective PDF, course content, or recalled questions are reproduced. Blueprint SHA-256: `454e6bd5ab99966ebdbfda2b06dcbd4949a4bffea30cfe7b75a731e4526a3791`.

## 220-1201 coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: five weighted V15 domains—Mobile devices (13%), Networking (23%), Hardware (25%), Virtualization and cloud computing (11%), and Hardware and network troubleshooting (28%)
- Coverage evidence: guide sections 1–5, three support scenarios, eight hands-on labs, 40 original checks, and an explicit 220-1101-to-220-1201 gap checklist
- Link evidence: eight unique external URLs; six reachable, two automation-blocked, zero missing/broken in the dated source-health evidence
- Volatile boundaries: objectives, delivery/languages/score, estimated retirement, device/component/connector compatibility, protocols, Wi-Fi/security, firmware, cloud behavior, and provider revision, runtime, bundle, price, and access

The review maps all five public V15 domains and summary tasks to compatibility-first installation and evidence-led support. Three scenarios, eight safe labs and 40 original checks cover laptop/mobile parts and charging/display/dock/radio/synchronization paths; protocols/ports, devices, media, IP/DHCP/DNS, Wi-Fi, SOHO/IoT and network tools; board/CPU/RAM/storage/GPU/PSU/cooling/cables/peripherals/printers; hypervisors, VM networks and cloud responsibility; plus the 28% troubleshooting domain across power, POST, thermal, storage, display, printer and wired/wireless symptoms. All eight guide URLs are cataloged: six reachable and O'Reilly plus Udemy automation-blocked; none missing or broken. The same-version rule and non-dated estimated-2028 retirement are explicit; no proprietary objectives, PBQs or recalled items are used. Blueprint SHA-256: `81a5721116c570f081c1abbd75b494a05e2cfdf4185d4e1051a03981d1565448`.

## 220-1202 coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: four weighted V15 domains—Operating systems (28%), Security (28%), Software troubleshooting (23%), and Operational procedures (21%)
- Coverage evidence: guide sections 1–4, three controlled-support scenarios, eight hands-on labs, 40 original checks, and an explicit 220-1102-to-220-1202 gap checklist
- Link evidence: eight unique external URLs; six reachable, two automation-blocked, zero missing/broken in the dated source-health evidence
- Volatile boundaries: objectives, delivery/languages/score, estimated retirement, OS/app/tool support and behavior, threats/security recommendations, licensing/privacy/policy, and provider revision, runtime, bundle, price, and access

The review maps all four public V15 domains to a controlled support lifecycle: understand state, preserve evidence/data, make the smallest authorized change, validate function/security/restart/recovery, and communicate/document. Three scenarios, eight safe labs and 40 original checks cover supported multi-OS selection/install/filesystems; Windows tools/commands/configuration plus macOS/Linux/mobile; identity/permissions/encryption/endpoint/SOHO/browser/mobile controls; evidence-preserving malware response and approved disposal; Windows/application/mobile/security troubleshooting; tickets/change/backup/restore/safety/environment/privacy/licensing/professionalism; script review and consent-based remote support. All eight guide URLs are cataloged: six reachable and O'Reilly plus Udemy automation-blocked; none missing or broken. Same-version and non-dated estimated-2028 boundaries are explicit; no proprietary objectives, PBQs, course labs or recalled items are used. Blueprint SHA-256: `802af49e1791f2aca4dd6fa98b272100badecd2be659ab001325bfb8cb5503c9`.

## N10-009 coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: five weighted V9 domains—Networking concepts (23%), Network implementation (20%), Network operations (19%), Network security (14%), and Network troubleshooting (24%)
- Coverage evidence: guide sections 1–5, three operational scenarios, eight authorized labs, 42 original checks, and an explicit N10-008-to-N10-009 gap checklist
- Link evidence: nine unique external guide URLs; seven reachable, two automation-blocked, zero missing/broken in the dated source-health evidence
- Volatile boundaries: objectives, delivery/languages/score, estimated retirement, protocols/standards, wireless/regulatory behavior, firmware/cloud responsibility, threats/security guidance, and provider revision, runtime, bundle, bank, price, and access

The review maps every public V9 domain and summary task to an end-to-end packet-walk and evidence model. Three scenarios, eight safe labs and 42 original checks cover OSI/encapsulation, appliances/cloud/traffic, services and subnetting, media/transceivers/topologies, routing/NAT/first hop, VLAN/STP/MTU, wireless and physical deployment, documentation/lifecycle/change/configuration, monitoring, recovery and network services, secure management, identity/segmentation/attacks/hardening, and the complete physical-through-application troubleshooting method. All nine guide URLs are cataloged: seven reachable and O'Reilly plus Udemy automation-blocked; none missing or broken. The estimated-2027 statement is explicitly not represented as an exact retirement date. No proprietary objective PDF, PBQ, course lab or recalled item is used. Blueprint SHA-256: `c567a0adcbbf9a3ad2348be7a8187bbe7650479c142fb14b1b8c583fd64783f3`.

## SY0-701 coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: five weighted V7 domains—General security concepts (12%), Threats, vulnerabilities, and mitigations (22%), Security architecture (18%), Security operations (28%), and Security program management and oversight (20%)
- Coverage evidence: guide sections 1–5, three governance-to-operations scenarios, eight isolated/authorized labs, 42 original checks, and an explicit SY0-601-to-SY0-701 gap checklist
- Link evidence: eight unique external guide URLs; six reachable, two automation-blocked, zero missing/broken in the dated source-health evidence
- Volatile boundaries: objectives, delivery/languages/score, estimated retirement and replacement status, threats/vulnerabilities, crypto/standards, products/cloud responsibility, legal/compliance/privacy requirements, and provider revision, runtime, bundle, bank, price, and access

The review maps every public V7 domain and summary task into an asset → threat/vulnerability → business risk → layered control → telemetry/response → recovery/governance lifecycle. Three scenarios, eight safe labs and 42 original checks cover controls/CIA/AAA/zero trust/change/cryptography; actors/vectors/vulnerabilities/indicators/mitigation; on-premises/cloud/virtual/container/serverless/IaC/IoT/ICS architecture, infrastructure, data and resilience; baselines/assets/vulnerability management, SIEM/SOAR/EDR/XDR, enterprise controls, IAM/automation/incident/forensics; plus governance/risk/BIA, third parties, compliance/privacy, audits/testing and awareness. All eight guide URLs are cataloged: six reachable and O'Reilly plus Udemy automation-blocked; none missing or broken. The official estimated-2026 statement is explicitly separated from unconfirmed V8/SY0-801 dates or drafts. No proprietary objectives, PBQs, course labs, leaked drafts or recalled items are used. Blueprint SHA-256: `c0f718feec0907360d7a17eb01a40bf9c0f8508ccbe87a375d7f608d5d8d02db`.

## XK0-006 coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: five weighted V8 domains—System management (23%), Services and user management (20%), Security (18%), Automation, orchestration, and scripting (17%), and Troubleshooting (22%)
- Coverage evidence: guide sections 1–5, three operational scenarios, eight cross-distribution break/fix labs, 42 original checks, and an explicit XK0-005-to-XK0-006 gap checklist
- Link evidence: seven unique external guide URLs; five reachable, two automation-blocked, zero missing/broken in the dated source-health evidence
- Volatile boundaries: objectives, delivery/language/score, estimated retirement, distributions/kernels/packages/commands/configuration owners, security guidance, automation/container/cloud tools, AI behavior, and provider revision, runtime, bundle, bank, price, and access

The review maps every public V8 domain and summary task to runtime state → persistent configuration → restart/reboot/recreate → revalidation. Three scenarios, eight labs and 42 original checks cover boot/kernel/hardware/filesystems, LVM/RAID/mounts/backup, network/shell/virtualization, files/links/permissions/accounts/processes/jobs/packages, systemd/logs/timers/containers, PAM/LDAP/Kerberos/audit/MFA, firewalls/hardening/SSH/SELinux/AppArmor/crypto/compliance, Ansible/Puppet/IaC/CI-CD, Bash/Python/Git/responsible AI, and systematic boot/storage/service/network/security/performance troubleshooting. All seven guide URLs are cataloged: five reachable and O'Reilly plus Udemy automation-blocked; none missing or broken. Distribution-specific behavior is identified as a verification boundary. No proprietary objectives, PBQs, course labs or recalled items are used. Blueprint SHA-256: `145e8c39625ce15055b7d8e0098b2cbde174c84538e11eb25b3b81ae8e0f4832`.

## CV0-004 coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: six weighted V4 domains—Cloud architecture (23%), Deployment (19%), Operations (17%), Security (19%), DevOps fundamentals (10%), and Troubleshooting (12%)
- Coverage evidence: guide sections 1–6, three integrated cloud scenarios, eight safe multi-provider labs, 42 original checks, and an explicit CV0-003-to-CV0-004 gap checklist
- Link evidence: nine unique external guide URLs; seven reachable, two automation-blocked, zero missing/broken in the dated source-health evidence
- Volatile boundaries: objectives, delivery/languages/score, estimated retirement, cloud service names/limits/regions/interfaces, standards/security guidance/legal obligations, and provider revision, runtime, bundle, bank, price, and access

The review maps every public V4 domain into a requirement → service/control selection → reviewed IaC deployment → observable operation/security/recovery → layered troubleshooting lifecycle. Three scenarios, eight labs and 42 original checks cover service/deployment/responsibility models; availability, networks, virtualization/containers, compute/storage/database and cost; migration/IaC/provisioning; lifecycle/scaling/backup/observability; IAM/data/network/workload/vulnerability/compliance controls; source control/CI-CD/integrations/event-driven flows; and control-plane-through-application troubleshooting. All nine URLs are cataloged: seven reachable and O'Reilly plus Udemy automation-blocked; none missing or broken. The estimated-2027 statement is separated from an exact retirement date or unannounced replacement. No proprietary objective PDF, PBQ, course lab or recalled item is used. Blueprint SHA-256: `6fb337abbad0ccde4c7a29dceb3c7e3611211edf97a676fe7bd7800406c0a192`.

## LFCA coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: September 16, 2025 six-domain map—Linux Fundamentals (16%), System Administration Fundamentals (30%), Cloud Computing Fundamentals (18%), Security Fundamentals (14%), DevOps Fundamentals (12%), and IT Project Management Fundamentals (10%)
- Coverage evidence: guide sections 1–6, three integrated beginner scenarios, eight safe labs, 40 original checks, and explicit pre-update/LFCA-JP boundaries
- Link evidence: seven unique external guide URLs; all seven reachable in the dated source-health evidence
- Volatile boundaries: objectives/effective date, assessment delivery/eligibility/retake/validity, distributions/packages/commands, cloud/security/project/license behavior, and provider revision, duration, bundle, price and access

The review maps every current domain to one connected host → administration/network/recovery → cloud → security → DevOps → project/application/open-source model. Three scenarios, eight labs and 40 original checks cover Linux/command-line use, identities/packages/services/storage/network/troubleshooting/recovery, cloud models/availability/performance/cost, security/data/compliance, Git/CI-CD/containers and current project/functional/architecture/licensing fundamentals. All seven URLs are cataloged and reachable. The September 16, 2025 effective baseline, retired LFCA-JP and older Supporting Applications and Developers wording are explicit. No proprietary questions or course content are used. Blueprint SHA-256: `fd4278c4b59fa86cc2c014f67f60263670b72193b2f83354fa3712b0f97a77cf`.

## LFCS coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: five distribution-independent domains—Operations Deployment (25%), Networking (25%), Storage (20%), Essential Commands (20%), and Users and Groups (10%)
- Coverage evidence: guide sections 1–5, three integrated administration scenarios, eight safe labs, 40 original checks, and explicit runtime/persistent/restart/recovery boundaries
- Link evidence: six unique external guide URLs; five reachable, one automation-blocked, zero missing/broken in the dated source-health evidence
- Volatile boundaries: objectives, delivery/eligibility/retake/validity, distributions/kernels/packages/services/configuration owners, security guidance, virtualization/container/network behavior, and provider revision, duration, bundle, price and access

The review maps every current domain to one connected observe → change the correct persistent owner → restart/reload/reboot only as required → validate function, security, persistence and recovery workflow. Three scenarios, eight labs and 40 original checks cover kernels, processes, jobs, packages, failure recovery, libvirt, containers, SELinux, IPv4/IPv6, time, SSH, filtering/NAT, routing, bridges/bonds, proxies/load balancers, LVM/filesystems/remote storage/swap/automount/performance, Git/service configuration/resource constraints/certificates, identities/profiles/limits/ACLs and LDAP. All six URLs are cataloged: five reachable and O'Reilly automation-blocked; none missing or broken. The distribution-independent assessment and no-prerequisite policy are explicit; no proprietary simulator tasks, course labs or recalled exam tasks are used. Blueprint SHA-256: `7e81f913990e564ad0238c7842735843375ec30d94f036f88e194dcbfe77cb63`.

## CKA coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Kubernetes v1.35 and five weighted domains—Cluster Architecture, Installation & Configuration (25%), Workloads & Scheduling (15%), Services & Networking (20%), Storage (10%), and Troubleshooting (30%)
- Coverage evidence: guide sections 1–5, three integrated administration scenarios, eight safe performance labs, 40 original checks, and explicit quarterly version/course-gap boundaries
- Link evidence: eight unique external guide URLs; six reachable, two automation-blocked, zero missing/broken in the dated source-health evidence
- Volatile boundaries: exam Kubernetes version and quarterly alignment, objectives, delivery/eligibility/retake/validity, Kubernetes APIs/features/skew, kubeadm/runtime/CNI/CSI/controllers, documentation policy, and provider revision, duration, bundle, price and access

The review maps every v1.35 domain to a confirm context/namespace/owner → inspect desired and observed state → change the correct controlling resource → verify readiness, traffic, persistence, security and recovery workflow. Three scenarios, eight labs and 40 original checks cover RBAC, kubeadm/HA/lifecycle/etcd, Helm/Kustomize/interfaces/CRDs/operators, controllers/configuration/probes/scaling/admission/scheduling, Pod/Service/EndpointSlice/DNS/NetworkPolicy/Ingress/Gateway paths, StorageClass/PV/PVC/CSI behavior, and node/control-plane/workload/network/storage troubleshooting. All eight URLs are cataloged: six reachable and O'Reilly plus Udemy automation-blocked; none missing or broken. The official page's v1.35 baseline is preserved even though newer Kubernetes documentation exists, and the quarterly-update watch is explicit. No proprietary simulator tasks, course labs or recalled exam tasks are used. Blueprint SHA-256: `e4b196b215d9a8a74203f309fa7b755633fe99955e638e541b3a6eac147d2857`.

## CKAD coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Kubernetes v1.35 and five weighted domains—Application Design and Build (20%), Application Deployment (20%), Application Observability and Maintenance (15%), Application Environment, Configuration and Security (25%), and Services and Networking (20%)
- Coverage evidence: guide sections 1–5, three integrated application scenarios, eight safe performance labs, 40 original checks, and explicit 4–8-week version alignment/course-gap boundaries
- Link evidence: eight unique external guide URLs; six reachable, two automation-blocked, zero missing/broken in the dated source-health evidence
- Volatile boundaries: exam Kubernetes version/alignment, objectives, delivery/eligibility/retake/validity, OCI images and Kubernetes APIs/features/security/admission, package/controller behavior, documentation policy, and provider revision, duration, bundle, price and access

The review maps every v1.35 domain to one source/image → workload/volume → rendered release → observable runtime → least-privilege identity/configuration → Service/policy/Ingress lifecycle. Three scenarios, eight labs and 40 original checks cover image contracts, controllers, multi-container patterns and volumes; rolling/blue-green/canary delivery plus Helm/Kustomize; probes, CLI metrics, streams/debugging and API deprecations; CRDs/operators, authentication/authorization/admission, requests/limits/quotas, ConfigMaps/Secrets/ServiceAccounts and security contexts/capabilities; and Service/EndpointSlice/NetworkPolicy/Ingress paths. All eight URLs are cataloged: six reachable and O'Reilly plus Udemy automation-blocked; none missing or broken. The official page's v1.35 baseline and approximately 4–8-week release alignment are explicit. No proprietary simulator tasks, course labs or recalled exam tasks are used. Blueprint SHA-256: `58b0290b61ba14ad68c02e06bcd2fbec14d23c4e555e69eb67a5615047e02ca1`.

## CKS coverage record

- Reviewed: September 1, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Kubernetes v1.35 and six live-page weighted domains—Cluster Setup (15%), Cluster Hardening (15%), System Hardening (10%), Minimize Microservice Vulnerabilities (20%), Supply Chain Security (20%), and Monitoring, Logging and Runtime Security (20%)
- Coverage evidence: guide sections 1–6, three integrated defensive scenarios, eight authorized performance labs, 40 original checks, and explicit live-page/CNCF-page/PDF and CKA-prerequisite boundaries
- Link evidence: nine unique external guide URLs; seven reachable, two automation-blocked, zero missing/broken in the dated source-health evidence
- Volatile boundaries: Kubernetes version and approximately 4–8-week alignment, domain weights/competencies, lagging CNCF v1.34 curriculum, prerequisite/CARE policy, delivery/eligibility/retake/validity, vulnerabilities/advisories/APIs/security tools/policy engines, and provider revision, duration, bundle, price and access

The review maps every live v1.35 domain to an asset/trust-boundary/threat → narrow preventive control → positive and negative validation → telemetry/detection → authorized containment/recovery lifecycle. Three scenarios, eight labs and 40 original checks cover network/CIS/TLS/metadata/binary setup; RBAC/ServiceAccounts/API access/upgrades; minimal hosts/IAM/network/seccomp/AppArmor; current Pod Security, Secrets, tenancy/sandboxing and Pod-to-Pod encryption; minimal images, SBOM/provenance, CI/artifact repositories, signatures/admission and static/image analysis; plus behavioral detection, cross-layer investigation, runtime immutability and Kubernetes audit. All nine URLs are cataloged: seven reachable and O'Reilly plus Udemy automation-blocked; none missing or broken. The guide follows the live Linux Foundation 15/15/10 first-three weights while clearly flagging CNCF's lingering 10/15/15 overview and v1.34 PDF, and corrects the prerequisite to previously passed CKA with no active-status requirement. No offensive target instructions, proprietary simulator tasks, course labs or recalled exam tasks are used. Blueprint SHA-256: `26ca4b0afc590f0df1dbf0ed60a435ce420efc6ac6d4ae95ec41dac302925c98`.

## GOOGLE-CLOUD-DIGITAL-LEADER coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: August 12, 2026 six-domain guide—Digital Transformation (18%), Data Transformation (18%), Artificial Intelligence (18%), Infrastructure and Application Modernization (18%), Trust and Security (18%), and Operations (10%)
- Coverage evidence: guide sections 1–6, three integrated business/architecture scenarios, eight decision-oriented labs, 36 original checks, and a precise pre-August objective and terminology gap checklist
- Link evidence: ten unique external guide URLs; eight reachable, two automation-blocked, zero missing/broken in the dated source-health evidence
- Volatile boundaries: objectives and renewal/delivery contract; Gemini Enterprise Agent Platform, agents and AI Hypercomputer; data, security and hybrid/multicloud product names and availability; price/regional behavior; and learning-provider revision, duration, access and practice material

The review follows the launched August PDF rather than the older ~17/16/16/17/17/17 HTML guide. It maps every current domain through business outcome, requirement and data shape, service/control selection, shared ownership, validation, observability and lifecycle operation. Three scenarios, eight labs and 36 checks cover cloud models and network geography; governed data and store/pipeline/BI selection; ML, generative and agentic AI choice/evaluation/safety; migration, compute, containers and APIs; layered identity/data/AI/security operations and trust evidence; plus hierarchy, financial governance, recovery, observability and SRE. All ten URLs are cataloged: eight reachable and O'Reilly plus Udemy automation-blocked; none missing or broken. No proprietary course content, question bank or recalled exam item is used. Blueprint SHA-256: `998892823a5a1a3cf2b508e3145f723c4c9e17181d62f59ec78d2e633f4eca8d`.

## GOOGLE-GENERATIVE-AI-LEADER coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: four domains—Fundamentals of gen AI (30%), Google Cloud's gen AI offerings (35%), Techniques to improve gen AI model output (20%), and Business strategies for a successful gen AI solution (15%)
- Coverage evidence: guide sections 1–4, three integrated enterprise scenarios, eight safe decision/evaluation labs, 40 original checks, and an explicit Vertex/Agentspace-to-current-Agent-Platform terminology checklist
- Link evidence: ten unique external guide URLs; eight reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: undated detailed PDF; certification delivery/renewal; model and product names/versions, limits, price, regions, data terms and release stages; threat/policy/legal guidance; and learning-provider revision, duration, access and practice material

The review maps the complete public guide through business outcome → permitted data and model/layer choice → Google application/platform/API/tool selection → prompting/grounding/customization/evaluation → constrained human/agent workflow → secure, responsible and measurable operation. Three scenarios, eight labs and 40 checks cover AI/ML/foundation models, modalities/data/lifecycle, Gemini/Gemma/Imagen/Veo, Gemini/Workspace/enterprise search/customer engagement, Agent Platform/Studio/Search/AutoML and specialized APIs, RAG and agents/tools, prompt/sampling/evaluation/change controls, SAIF-style defense, responsible AI, portfolio/adoption and value. All ten URLs are cataloged: eight reachable and O'Reilly plus Udemy automation-blocked; none missing or broken. No proprietary course content, question bank or recalled exam item is used. Blueprint SHA-256: `d5154002a04c5a259a6d825a4ba3b84dcc9ee0e2fb075a012e510f17f641c324`.

## GOOGLE-ASSOCIATE-CLOUD-ENGINEER coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: current four-domain guide—Setting up an environment (20%), Planning and implementing (30%), Ensuring successful operation (30%), and Configuring access and security (20%)
- Coverage evidence: guide sections 1–4, three integrated operational scenarios, eight hands-on labs, 40 original checks, and an explicit old-outline and current-branding gap checklist
- Link evidence: nine unique external guide URLs; eight reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: undated detailed PDF and published branding notice; certification delivery/renewal; product names, release stages, regions, limits, quotas, prices, policy/security guidance; and learning-provider revision, duration, access and practice material

The review maps every detailed current consideration through hierarchy/policy/billing/quota readiness; compute, container, agent, accelerator, data, storage, network and IaC selection; inventory, change, scaling, backup/restore, monitoring and diagnosis; plus IAM, service accounts, impersonation and federation. Three scenarios, eight labs and 40 checks make the decision and failure boundaries concrete. All nine guide URLs are cataloged: eight reachable and O'Reilly automation-blocked; none missing or broken. The older five-domain outline and former Cloud Functions, Vertex AI Agent Engine and Vertex AI Workbench names are explicitly reconciled with the current four-domain, Cloud Run functions and Gemini Enterprise Agent Platform baseline. No proprietary course content, question bank or recalled exam item is used. Blueprint SHA-256: `1c26e61d687b69b9e2b0b00e59d537b271eae0647d525dd9d40284ea28c11d74`.

## GOOGLE-PROFESSIONAL-CLOUD-ARCHITECT coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: six weighted domains—Design and plan (25%), Manage and provision (17.5%), Security and compliance (17.5%), Optimize technical/business processes (15%), Manage implementation (12.5%), and Solution/operations excellence (12.5%)—plus all six Well-Architected pillars and four V6.1 cases
- Coverage evidence: guide sections 1–6, a ten-part official case-study method, three additional scenarios, eight evidence labs, 36 original checks, and an explicit current AI/agent/security/product-name gap checklist
- Link evidence: 13 unique external guide URLs; 12 reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: undated detailed PDF and branding notice; case-study versions; delivery/renewal; models, agents, APIs, product names/stages/regions/quotas/prices; compliance/security guidance; and provider revision, duration, access and practice material

The review maps every current objective through requirement → option/tradeoff → decision → owner → validation → operation → revisit. It connects the six Well-Architected pillars to workload disposition, service/data/network/AI selection, migration, landing zones, security/compliance evidence, SDLC/recovery/cost/skills/change processes, API and IaC implementation, observability/releases/support/quality/resilience. The four linked V6.1 cases get a reusable fact-to-decision method rather than a memorized answer architecture. Three scenarios, eight labs and 36 checks reinforce the model. All 13 URLs are cataloged: 12 reachable and O'Reilly automation-blocked; none missing or broken. No proprietary question bank, recalled item or copied course content is used. Blueprint SHA-256: `fceaa0587ed0fa26fcf66a037a2abb7e4103231cccb6ad9052153ca3cb328ec2`.

## GOOGLE-PROFESSIONAL-DATA-ENGINEER coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: five weighted domains—Design systems (22%), Ingest/process (25%), Store (20%), Prepare/use for analysis (15%), and Maintain/automate (18%)
- Coverage evidence: guide sections 1–5, three production data scenarios, eight evidence labs, 36 original checks and an old-course/current-product gap checklist
- Link evidence: eight unique external guide URLs; seven reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: undated detailed PDF; delivery/renewal; products, AI/model/query behavior, regions, quotas, prices, governance/security interfaces; and provider revision, duration, access and practice material

The review maps every current consideration through contract/ownership/security → ingestion semantics → deterministic processing → governed store/model → authorized BI/ML/RAG/sharing → repeatable orchestration → capacity, data/platform observability, repair/replay and tested recovery. Three scenarios, eight labs and 36 checks cover batch/stream correctness, current BigQuery/BigLake/Dataplex/Dataflow/Dataproc/Dataform/Composer choices, migration/CDC, query performance, federated governance, capacity/cost and failure handling. All eight URLs are cataloged: seven reachable and O'Reilly automation-blocked; none missing or broken. No proprietary bank, recalled item or copied course content is used. Blueprint SHA-256: `d9fc9ddb90e3c6f965fb09311b060710a297ba36f18025518dca3d5154d785bc`.

## GOOGLE-PROFESSIONAL-CLOUD-SECURITY-ENGINEER coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: five weighted domains—Access (25%), Communications/boundary protection (22%), Data protection (23%), Operations (19%), and Compliance support (11%)
- Coverage evidence: guide sections 1–5, three defensive scenarios, eight authorized evidence labs, 36 original checks and an explicit current-control gap checklist
- Link evidence: seven unique external guide URLs; six reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: undated PDF; live page currently omits a validity signal; delivery, products/tiers/regions, IAM/policy, threats, crypto, AI, vulnerabilities and compliance contracts; provider revision, duration, access and practice material

The review maps every detailed current objective through asset/data and identity/boundary → threat or obligation → preventive control → positive/negative validation → telemetry/detection → authorized response/recovery → evidence/owner. Three scenarios, eight authorized labs and 36 checks cover workforce/workload identity, privilege/hierarchy, NGFW/private/perimeter paths, sensitive-data/key/secret/AI controls, supply chain/posture, centralized security logs/detections/response and compliance evidence. All seven URLs are cataloged: six reachable and O'Reilly automation-blocked; none missing or broken. No exploit target, proprietary bank, recalled item or copied course content is used. Blueprint SHA-256: `356877767ac663f5102c9f398ba61909d074668c92d54e0e09584341f5a48166`.

## GOOGLE-PROFESSIONAL-MACHINE-LEARNING-ENGINEER coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: June 1, 2026 six-domain guide—Low-code AI (13%), Collaboration/data/models (16%), Scale prototypes/training (21%), Serve/scale (20%), Pipelines (18%), and Monitoring (13%); published approximations total 101%
- Coverage evidence: guide sections 1–6, three production AI scenarios, eight evidence labs, 36 original checks and an explicit Vertex-to-Gemini-Enterprise-Agent-Platform translation
- Link evidence: eight unique external guide URLs; seven reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: branding/transition notices, live page and current `_new.pdf`; models/APIs/platform names/stages/regions/quotas/accelerators/prices; AI evaluation, security and responsible practice; provider revision, duration, access and practice material

The review follows the actual linked `_new.pdf` dated June 1, 2026; a different older PDF still resolves at the non-`_new` address and is explicitly not used as current. Every domain is mapped across task/data/model choice, governed features/notebooks/experiments/lineage, reproducible training/tuning/accelerators, batch/online registry/serving/rollout, validation and CI/CD/CT pipelines, and predictive/gen-AI quality, drift/skew, safety, security, cost, retraining and rollback. Three scenarios, eight labs and 36 checks are included. All eight URLs are cataloged: seven reachable and O'Reilly automation-blocked; none missing or broken. Blueprint SHA-256: `14f8953554d4c9762d0ac1fc7b0b4449d624895b2e1c3c9d4670009726c5bd5c`.

## GOOGLE-PROFESSIONAL-AGENTIC-ARCHITECT coverage record

- Reviewed: September 2, 2026, one day before announced beta registration opening
- Outcome: **sources + objectives checked; human review pending**
- Official scope: five beta domains—Low-code agents (13%), Coding agents (17%), Custom agents (33%), Evaluate/deploy (22%), and Secure/govern (15%)—plus a Pearson conceptual/design exam and Google Skills hands-on labs
- Coverage evidence: guide sections 1–5, three end-to-end agent scenarios, eight safe evidence labs, 36 original checks, complete named-tool coverage and explicit beta/GA volatility
- Link evidence: seven unique external guide URLs; all seven reachable after replacing a misleading HTTP-200 soft-404 A2A page
- Volatile boundaries: registration/exam/lab windows, two-part completion and scoring/results, eventual GA; product names/commands/APIs/stages/regions/quotas/prices; MCP/A2A, agent identity/gateway/registry/runtime, evaluation/security; provider availability

The review maps the complete beta guide and tool list through goal/responsibility → authorized data/context/memory → model/retrieval → tool identity/action contract → MCP/A2A/multi-agent orchestration → layered response/retrieval/tool/system evaluation → runtime/trace/AgentOps → OAuth/IAM/PAB/gateway/registry/policy/Model Armor/HITL → incident stop/reversal. Three scenarios, eight labs and 36 checks cover low-code, sandboxed coding agents, ADK/custom agents and production operations. All seven URLs are reachable; an A2A link that returned HTTP 200 with a rendered 404 title was detected and replaced. No leaked/recalled beta item, dump, proprietary lab or copied course content is used. Blueprint SHA-256: `eac2f3a291d2910ff1c9cd4968e04b84c9d3cf3d98b685e7b14135aca4804347`.

## 100-150 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: active CCST Networking exam, six public topic groups and the complete first-party exam-aligned course objective list; Cisco's checked public interface does not expose stable domain weights, so the guide does not invent them
- Coverage evidence: guide sections 1–6, three support scenarios, eight authorized evidence labs and 36 original checks
- Link evidence: ten unique external guide URLs; eight reachable, two O'Reilly automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: exam price/languages/delivery and lifetime-badge policy; JavaScript-rendered detailed topics; device/OS command output, Wi-Fi/security guidance; path/account access, commercial editions, durations and practice material

The review maps all six topic groups and every objective on Cisco's current exam-aligned training page through application/transport/address → local media/frame/switch → gateway/route → remote service/return path → observable evidence/safe test → security and documentation. It adds IPv4/IPv6 calculation and classification, media/transceiver/endpoint decisions, read-only endpoint and IOS evidence, a controlled diagnostic method, ticket discipline, three scenarios, eight labs and 36 checks. The primary snapshot monitors Cisco's stable exam landing-page baseline; the dynamic detailed topics and Cisco Public training PDF are separately registered for health and human review. No recalled/live item, answer dump, unauthorized capture target or copied book/course content is used. Blueprint SHA-256: `06e3901b4e9a03657e2111d7a02b484c1a8629ab595f54b32e03f1197680d194`.

## 100-160 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: active CCST Cybersecurity exam, five public work areas and all 23 first-party exam-aligned course objectives; no stable domain weights are exposed by the checked public interface, so none are invented
- Coverage evidence: guide sections 1–5, three defensive scenarios, eight authorized evidence labs and 36 original checks
- Link evidence: nine unique external guide URLs; eight reachable, one O'Reilly automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: exam price/languages/delivery and lifetime badge policy; JavaScript-rendered topics; threats, vulnerabilities, platform/log/tool behavior, regulation/incident obligations; path/account access, book update, duration and practice material

The review maps the current public work areas and every detailed official training outcome through asset/business process → threat/vulnerability → contextual risk → administrative/technical/physical control → endpoint/network/identity evidence → authorized response → continuity/recovery and lessons learned. It covers access and cryptography, TCP/IP/network/wireless defense, endpoint baseline/update/log/malware procedure, authorized vulnerability assessment and contextual prioritization, threat intelligence, BIA/RTO/RPO/backups, event triage, chain of custody, escalation and incident communication. Three scenarios, eight safe labs and 36 checks are included. The primary snapshot monitors Cisco's stable exam landing-page baseline; dynamic detailed topics and the Cisco Public training PDF are separately health checked. No exploit target, recalled/live item, answer dump or copied course/book content is used. Blueprint SHA-256: `8c759c20e7564e89bf453d83dd80b60b78716c3c06790073e531065e5d891418`.

## 200-301 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: current CCNA v1.1 through February 2, 2027—Network Fundamentals (20%), Network Access (20%), IP Connectivity (25%), IP Services (10%), Security Fundamentals (15%), and Automation and Programmability (10%)—with the separately published v2.0 replacement beginning February 3
- Coverage evidence: guide sections 1–6, a complete v1.1 objective map, explicit v2.0 transition table/callouts, three integrated network scenarios, eight authorized labs and 36 original checks
- Link evidence: ten unique external guide URLs; eight reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: scheduled v2.0 launch and exam price; delivery, languages, recertification policy, IOS/controller/API/tool behavior, security guidance; simulator/platform access; and commercial revision, duration and practice material

The review maps every current v1.1 objective through requirement → packet/control-plane behavior → minimum configuration → verification output → likely fault → safe correction and rollback. It covers components/media/addressing/switching; VLANs/trunks/LACP/Rapid PVST+/wireless; route selection, static routing, OSPFv2 and FHRP; NAT/NTP/DHCP/DNS/SNMP/syslog/QoS/SSH; risk/access/VPN/ACL/Layer 2/wireless controls; and controllers/APIs/JSON/AI/Ansible/Terraform. The five-domain v2.0 map separately identifies its deeper troubleshooting/configuration plus OSPFv3, HSRP/VRRP status, DNS records, central AAA, SFTP/SCP, storm control, IPv6 RA Guard, agentic AI/prompting and Ansible execution. Three scenarios, eight labs and 36 checks are included. Eight links are reachable; O'Reilly and Udemy are automation-blocked; none are broken. No recalled/live item, answer dump, copied course material or unauthorized target is used. Blueprint SHA-256: `507885a84f0680df787cde210d2181632c549ce95c9581ad8b516143dd4d2ddc`.

## 200-901 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: six-domain CCNAAUTO v1.1—Software Development and Design (15%), Understanding and Using APIs (20%), Cisco Platforms and Development (15%), Application Deployment and Security (15%), Infrastructure and Automation (20%), and Network Fundamentals (15%)
- Coverage evidence: guide sections 1–6, three integrated automation scenarios, eight authorized evidence labs and 46 original checks
- Link evidence: 11 unique external guide URLs; nine reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: exam page v1.0 versus detailed/current-training v1.1 label; inconsistent first-party language listings; DevNet-era names/content; Cisco platform/API/SDK/model/product versions; sandbox availability; book release and provider revision/duration/practice access

The review maps every detailed v1.1 objective through intent → data/API contract → authentication/authorization → code/configuration → test → review → controlled execution → evidence → rollback. It covers XML/JSON/YAML/Python structures, TDD/methods/patterns/Git; REST/RPC/sync/async/webhooks/auth/HTTP diagnosis/Python requests; Cisco platform/SDK/DevNet-resource selection and YANG/NETCONF/RESTCONF; deployment/container/CI-CD/unit-test/Bash/DevOps/secret/data/web-risk controls; IaC/Ansible/Terraform/NSO/CML/pyATS plus Python/playbook/script/diff/sequence interpretation; and network paths, planes, services, ports, connectivity and application constraints. Three scenarios, eight labs and 46 checks are included. The guide explicitly reconciles the February 2026 DevNet-to-CCNA Automation rename, current first-party version-label mismatch and language-list mismatch. Nine URLs are reachable; O'Reilly and Udemy are automation-blocked; none are broken. No production target, exploit exercise, recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `b741522983500658e43c1a9a0200c142e4a626ff8d0ad8a01859f92d0670c60f`.

## SOL-C01 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: retired May 4, 2026; six preserved public abilities covering UI/notebooks, objects/stages/compute, structured/semi-structured/unstructured loading, roles/access, account structure, and Cortex LLM functions; no stable detailed weights are invented
- Coverage evidence: guide sections 1–6, three integrated scenarios, eight authorized evidence labs, 36 original checks, the frozen last official-page snapshot, and the current replacement/badge boundary
- Link evidence: seven unique external guide URLs; all seven reachable and zero missing/broken in dated source-health evidence
- Volatile boundaries: replacement course/assessment access, Snowflake product names/interfaces/roles/editions/limits, data-protection behavior, AI functions/models/regions/privileges/consumption, and commercial-course availability

The review preserves the former public SOL-C01 capability map while telling new learners not to buy a voucher or prepare for an unavailable attempt. It connects each ability to current architecture, compute and object context, validated/restartable loading, least-privilege role graphs, recovery/sharing boundaries, and evaluated Cortex use. Three scenarios, eight labs and 36 checks require observable evidence and cleanup. The official transition FAQ establishes the retirement, the free directly issued non-expiring Platform Skills Badge replacement, continued validity for existing holders, and the distinction between an educational badge and proctored SnowPro certification. The removed exam landing page remains only as a dated local snapshot; live objective monitoring skips retired records while source health checks all seven surviving URLs. No retired question bank, recalled item, dump or copied course material is used. Blueprint SHA-256: `a930a723415ca1b8dfead2cf60a3d27b6c7eaf3d336fefc301421adee9123d57`.

## COF-C03 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: active SnowPro Core with seven public abilities—AI Data Cloud architecture; account/warehouse management; loading/unloading/transformation; structured/semi-structured/unstructured data; performance; collaboration/protection; and connectivity—and a six-month experience recommendation
- Coverage evidence: guide sections 1–7, three integrated scenarios, eight authorized evidence labs, 40 original checks, and an explicit detailed-guide form/current-documentation reconciliation step
- Link evidence: ten unique external guide URLs; eight reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: form-delivered detailed objectives; delivery, price, language, policy and renewal; editions/regions, objects/interfaces/integrations, AI, identity/governance, performance behavior and costs; provider revision/duration/practice access

The review maps every ability through requirement and context → feature or architecture choice → least-privilege implementation → observable history/profile/grant/result → cost/security/recovery consequence → cleanup. It covers layers, hierarchy, data/object forms and interfaces; account context, roles, authentication and warehouses; governed restartable load/unload/transformation; evidence-led query/compute optimization; sharing/listings/reader/clean-room and recovery/governance boundaries; plus secure diagnosable client/integration paths. Three scenarios, eight labs and 40 checks are included. The live page is the monitored public baseline; candidates must reconcile the detailed guide they receive through Snowflake's form because inaccessible subobjectives and weights are not reconstructed here. Eight links are reachable and O'Reilly on-demand plus Udemy are automation-blocked; none are broken. No recalled/live item, dump, guaranteed-pass source or copied course content is used. Blueprint SHA-256: `fc6ba90a44c29eb3380a41bd9609357c29247bbe81be8003dcbe89ad71a8063c`.

## DEA-C02 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: active SnowPro Advanced: Data Engineer with five public abilities—source lake/API/on-premises data; transform/replicate/share across clouds; near-real-time streams; scalable data-engineering compute; and performance metrics—and a two-year production-experience recommendation
- Coverage evidence: guide sections 1–5, three production scenarios, eight authorized evidence labs, 40 original checks, and an explicit detailed-guide form/current-documentation reconciliation step
- Link evidence: ten unique external guide URLs; eight reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: form-delivered detailed objectives; exam delivery/price/language/policy; pipeline/connectors/Openflow/Snowpipe Streaming/dynamic-table behavior; compute/serverless/replication/sharing/governance; metrics/views/costs; provider revision/access

The review maps every public ability through source and consumer contracts → identity/network/data path → deterministic state/checkpoint → validation/reconciliation → idempotent retry/replay → latency/quality/security/recovery/cost evidence. It distinguishes batch, file-event and row-stream ingestion; streams/tasks/dynamic tables; sharing versus movement and replication; scale-up versus scale-out and managed versus serverless compute; plus query/pipeline evidence, controlled optimization, DataOps delivery and incident recovery. Three scenarios, eight labs and 40 checks are included. The live page is the monitored baseline and the candidate must reconcile the form-delivered detailed guide; inaccessible weights/subobjectives are not reconstructed. Eight links are reachable and two O'Reilly books are automation-blocked; none are broken. No recalled/live item, dump, guaranteed-pass source or copied course content is used. Blueprint SHA-256: `5d27aac73433eb775a5d5b4ff7af013755ab26751154413fa84c363d200909c0`.

## GES-C02 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: active SnowPro Specialty: Gen AI with four public abilities—principles/capabilities/best practices; Cortex AI features/functions and LLM use cases; open-model fine-tuning through Snowpark Container Services and Model Registry; and document-processing pipelines—plus a one-year enterprise-experience recommendation
- Coverage evidence: guide sections 1–4, three production scenarios, eight authorized evidence labs, 40 original checks, and an explicit detailed-guide form/current-documentation reconciliation step
- Link evidence: 11 unique external guide URLs; all 11 reachable and zero missing/broken in dated source-health evidence
- Volatile boundaries: form-delivered detailed objectives; delivery, price, language and policy; models/functions/legacy names/regions/limits/consumption; Agent/Analyst/Search/Intelligence/Code/MCP behavior; SPCS instance/serving, Model Registry frameworks; document formats/limits; provider revision/access

The review maps every public ability through business decision/action and data authority → narrowest suitable surface → identity and least privilege → versioned prompt/context/retrieval/model/tool/document contract → component and system evaluation → observed quality/safety/latency/cost → containment, replay or rollback. It covers canonical and legacy Cortex function boundaries; RAG, semantic views, Agents and MCP trust; reproducible open-model tuning, image/service/compute-pool and Registry lifecycle; and staged parse/extract/chunk/index pipelines with provenance, deletion and idempotent replay. Three scenarios, eight labs and 40 checks are included. The live page is the monitored baseline and candidates must reconcile the form-delivered detailed guide; inaccessible weights/subobjectives are not reconstructed. All 11 URLs are reachable. No recalled/live item, dump, guaranteed-pass source or copied course content is used. Blueprint SHA-256: `c6dcc5ab29e74f1ba7c2778039589727d42e249a5b732ff57bbbd323cf002a25`.

## CC coverage record

- Reviewed: September 2, 2026, one day after the new outline took effect
- Outcome: **sources + objectives checked; human review pending**
- Official scope: September 1, 2026 five-domain outline—Security Principles (24%), Security Governance (17.3%), IAM Concepts (20%), Networking and Cloud Security Concepts (21.3%), and Security Operations and Incident Response (17.3%)
- Coverage evidence: guide sections 1–5, three defensive scenarios, eight authorized evidence labs, 40 original checks and an explicit pre-September/current-outline gap boundary
- Link evidence: nine unique external guide URLs; five reachable, four automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: newly effective outline/AI guidance; CAT delivery, appointment language windows and policy; laws/frameworks/threats/crypto/Zero Trust/cloud/security-testing practice; training access/offers, commercial revision/duration/practice

The review maps all current domains and detailed topics through asset/business process → threat/vulnerability → likelihood/impact → selected administrative/technical/physical control → implementation owner → observable positive/negative evidence → authorized response/recovery. It covers CIA/AAA/privacy/ethics and risk; GRC/BC/DR/awareness/metrics; complete identity lifecycle and access models; packet/control/segmentation/Zero Trust/cloud responsibility; plus data/assets, event triage/intelligence, evidence-led response and authorized testing. AI examples remain integrated into ordinary security principles rather than treated as an unsourced extra domain. Three scenarios, eight labs and 40 checks are included. Five links are reachable; O'Reilly and Udemy are automation-blocked; none are broken. No recalled/live item, dump, exploit target or copied course content is used. Blueprint SHA-256: `e78550c6ab0a65fb1dbff89436b7e7d72dfc575393ffd439c42929acf180aea4`.

## SSCP coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: October 1, 2025 seven-domain outline—Security Concepts and Practices (16%), Access Controls (15%), Risk Identification, Monitoring and Analysis (15%), Incident Response and Recovery (14%), Cryptography (9%), Network and Communication Security (16%), and Systems and Application Security (15%)
- Coverage evidence: guide sections 1–7, three operational scenarios, eight authorized evidence labs, 40 original checks and an explicit exam-versus-certification boundary
- Link evidence: nine unique external guide URLs; eight reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: CAT delivery and language availability; experience/waiver/Associate/endorsement/member/CPE/AMF policy; security standards, threats, cryptography, platforms and commercial training revision/access

The review maps all current objectives through asset and requirement → failure or threat → appropriate control → implementation owner → observable positive and negative evidence → authorized response, recovery and lessons learned. It covers governance and risk, identity lifecycle and access models, monitoring and vulnerability management, evidence-preserving incident response and resilience, cryptographic purpose/key lifecycle, network paths and segmentation, plus hardened systems and secure application operations. Three scenarios, eight safe labs and 40 checks are included. Seven URLs are reachable; O'Reilly and Udemy are automation-blocked; none are broken. The guide distinguishes passing the exam from experience, Associate status, endorsement, membership, ethics, the 60-CPE three-year cycle and current AMF. No recalled/live item, answer dump, unauthorized exploit target or copied course content is used. Blueprint SHA-256: `0d643f2af74b12b015f5607516ba3da57ea3192481c800c76963d2fc27f9875e`.

## CCSP coverage record

- Reviewed: September 2, 2026, after the August 1 revision took effect
- Outcome: **sources + objectives checked; human review pending**
- Official scope: August 1, 2026 six-domain outline—Cloud Concepts, Architecture and Design (17%), Cloud Data Security (20%), Cloud Platform and Infrastructure Security (17%), Cloud Application Security (16%), Cloud Security Operations (17%), and Legal, Risk and Compliance (13%)
- Coverage evidence: guide sections 1–6, three cloud scenarios, eight authorized evidence labs, 40 original checks and an explicit exam-versus-certification boundary
- Link evidence: ten unique external guide URLs; eight reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: new outline and AI/ML/LLM/cloud-native material; CAT/language windows; experience/waiver/CISSP/Associate/endorsement/member/CPE/AMF policy; provider services/contracts, laws/standards/assurance and training revision/access

The review maps every objective through business/data obligation → service/deployment model and cloud roles → responsibility/trust boundary → control and contract dependency → positive/negative evidence → failure, response, recovery and tested exit. It covers reference architecture/provider evaluation and governed AI/ML; complete data lifecycle/storage/protection/rights/events; facility-to-management-plane risk/control/resilience; secure SDLC and cloud-native/API/supply-chain/IAM assurance; hardened operations, service management, SOC/forensics/response; plus jurisdiction/privacy, audit scope, enterprise/provider risk and enforceable contracts. Three scenarios, eight safe labs and 40 checks are included. Eight URLs are reachable; O'Reilly and Udemy are automation-blocked; none are broken. The guide distinguishes passing the exam from experience/waiver/CISSP substitution, Associate status, endorsement, ethics, the 90-CPE three-year cycle and current AMF. No recalled/live item, answer dump, unauthorized test or copied course content is used. Blueprint SHA-256: `9ee040484826df7b98700a44891301a9fc46fb76351c0a941221e6f5cf1b8288`.

## CISSP coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: April 15, 2024 eight-domain outline—Security and Risk Management (16%), Asset Security (10%), Security Architecture and Engineering (13%), Communication and Network Security (13%), IAM (13%), Security Assessment and Testing (12%), Security Operations (13%), and Software Development Security (10%)
- Coverage evidence: guide sections 1–8, three cross-domain leadership scenarios, eight authorized evidence labs, 40 original checks and an explicit exam-versus-certification boundary
- Link evidence: 11 unique external guide URLs; ten reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: two-plus-year baseline and embedded AI guidance; CAT/language windows; experience/waiver/Associate/endorsement/member/CPE/AMF policy; law/standards/threats/technology/provider/course revision and access

The review maps every objective through mission/stakeholders and ethics/law/policy → owned assets/data and threat/vulnerability → likelihood/impact/risk appetite → architecture/control/people choices → accountable decision → assessment and operational evidence → incident/recovery/continuity → improvement. It covers governance, investigations, risk, supply chain, personnel and awareness; asset/data lifecycle; secure models/architecture/crypto/facilities/system lifecycle; network paths/components/channels; human/device/workload/federated IAM; authorized risk-based assurance; investigations/monitoring/configuration/response/recovery/physical safety; and governed SDLC/ecosystem/acquisition/coding. AI assets and security activities are integrated across domains rather than invented as a ninth domain. Three scenarios, eight safe labs and 40 checks are included. Ten URLs are reachable and O'Reilly is automation-blocked; none are broken. The guide distinguishes passing the exam from experience/waiver, Associate status, endorsement, ethics, the 120-CPE three-year cycle and current AMF. No recalled/live item, answer dump, unauthorized test or copied course content is used. Blueprint SHA-256: `4b2491ad3b07a5d582a38e6c8dd3afd87e4861e26e2cadb58a67fc0bb9d8edb3`.

## NCA-GENL coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: five weighted domains—Core Machine Learning and AI Knowledge (30%), Software Development (24%), Experimentation (22%), Data Analysis and Visualization (14%), and Trustworthy AI (10%)
- Coverage evidence: guide sections 1–5, three lifecycle scenarios, eight evidence labs, 40 original checks and an explicit 50-versus-50–60-question source discrepancy
- Link evidence: eight unique external guide URLs; seven reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: exam question-count discrepancy; delivery/price/language/validity; fast-moving NVIDIA model, software and training catalog; third-party course revision/access

The review maps every public domain through authorized use case and success criteria → governed data → model, adaptation, retrieval and prompt decision → tested application contract → controlled experiment and error analysis → deployment, monitoring and rollback → privacy, safety, security, transparency and fairness evidence. It covers ML/training/inference and transformer foundations, Python/tensor/application integration, prompting/RAG and untrusted-output handling, split/leakage/metric/reproducibility discipline, data-quality and honest-visualization practice, plus system cards, guardrails, monitoring and escalation. Three scenarios, eight labs and 40 checks are included. Seven URLs are reachable and Udemy is automation-blocked; none are broken. No recalled/live item, dump or copied course content is used. Blueprint SHA-256: `220607c5f839a196b22d3211345d8fcd09128190fd7f21ffb6d4fd7d2c4bf5c7`.

## NCA-AIIO coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Essential AI Knowledge (38%), AI Infrastructure (40%), and AI Operations (22%)
- Coverage evidence: guide sections 1–3, three infrastructure scenarios, eight safe evidence labs, 40 original checks and an explicit first-party USD 125-versus-USD 135 price discrepancy
- Link evidence: eight unique external guide URLs; seven reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: certification/learning-path price mismatch; hardware, supported topology, software and compatibility matrices; cloud services; course catalog/access; virtualization/licensing

The review maps all public objectives through workload requirement → CPU/GPU/memory and training/inference behavior → node/cluster topology → network/storage movement → facility constraints → supported software stack → scheduling/orchestration → correlated GPU/system/service evidence → safe change, recovery or escalation. It covers AI/ML/DL, accelerator/software roles, sizing and scaling, power/cooling, Ethernet/InfiniBand/RoCE/RDMA/DPU context, storage and deployment models, lifecycle and compatibility, Slurm/Kubernetes/GPU Operator, `nvidia-smi`/DCGM, diagnosis, passthrough/vGPU/MIG/time slicing, and operational governance. Three scenarios, eight labs and 40 checks are included. Seven URLs are reachable and Udemy is automation-blocked; none are broken. No recalled/live item, dump, unsafe production instruction or copied course content is used. Blueprint SHA-256: `11cca6a173f82698164dde31c281949bfe89a574be3b6979f77b9968f1746824`.

## NCP-AIO coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Installation and Deployment (31%), Administration (23%), Workload Management (23%), and Troubleshooting and Optimization (23%)
- Coverage evidence: guide sections 1–4, three cross-control-plane operations scenarios, eight authorized performance labs, 48 original checks and an explicit 30-question/three-integrated-lab/120-minute contract
- Link evidence: ten unique external guide URLs; all ten reachable, zero blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: exam lab image/tool versions; BCM/Mission Control/Run:ai/DOCA/GPU Operator interfaces; firmware/driver/CUDA/fabric/storage compatibility; professional training duration/price; policy and validity

The review maps every objective to confirm scope/impact/authorization/desired state → inspect the smallest useful layer and recent change → form a falsifiable hypothesis → safely discriminate → apply the narrowest reversible authorized correction → verify system/workload outcome → document, roll back or escalate. It covers BCM Base View/categories/images/users/network/patch/firmware/reporting, Mission Control and DPU Arm DOCA placement, Slurm/Kubernetes/Run:ai installation and administration, MIG, NGC training/inference deployment and team allocation, plus Docker, Fabric Manager, BCM, Magnum IO and storage diagnosis/optimization. Three scenarios, eight labs and 48 checks are included. All ten URLs are reachable. No recalled/live item, dump, unsafe production target or copied course content is used. Blueprint SHA-256: `5ae751ccfd49da6291f68a72d54a31199afb39b9374a3c081d4118be4bb28f9e`.

## SALESFORCE-PLATFORM-ADMINISTRATOR coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: current eight-domain Trailhead baseline—Configuration and Setup (15%), Object Manager and Lightning App Builder (15%), Sales and Marketing Applications (10%), Service and Support Applications (10%), Productivity and Collaboration (10%), Data and Analytics Management (17%), Automation (15%), and Agentforce (8%)
- Coverage evidence: guide sections 1–8, three integrated administration scenarios, eight authorized evidence labs, 40 original checks and an explicit current-weights/stale-season-label reconciliation
- Link evidence: nine unique external guide URLs; seven reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: seasonal exam version and objective detail; delivery, fees, passing score and language; editions/licenses/limits; Agentforce surfaces and terminology; learning-path revision/access; annual maintenance deadline

The review maps each domain through business requirement and data owner → license/persona and least privilege → declarative configuration → data/automation/UI dependency → deployment and representative-user test → operational evidence and rollback. It covers org/user/security setup, data models and Lightning pages, sales and service lifecycles, collaboration/mobile/extensions, controlled data operations and audience-correct analytics, bulk-safe Flow/approvals, and bounded Agentforce use. Three scenarios, eight labs and 40 checks are included. The December 15, 2025 refresh and stale Summer ’25 Help label are preserved. No recalled/live item, dump, shared superbadge solution or copied course content is used. Blueprint SHA-256: `b2f9f40f925247562d8d19eed5ad7a33a4b5c10e03b705d2fe34ec88678b7c97`.

## SALESFORCE-PLATFORM-APP-BUILDER coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: corrected Summer ’26 baseline—Salesforce Fundamentals (18%), Data Modeling and Management (20%), Business Logic and Process Automation (32%), User Interface (17%), and App Deployment (13%)
- Coverage evidence: guide sections 1–5, three integrated application scenarios, eight authorized evidence labs, 40 original checks and an explicit August-refresh reconciliation
- Link evidence: nine unique external guide URLs; seven reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: seasonal objective/version changes; delivery, fees, passing score and language; editions/licenses/limits; Flow, Agentforce and UI surfaces; training revision/access; annual maintenance deadline

The review maps each public objective through business requirement and data owner → declarative/programmatic boundary → least privilege and data model → formulas, validation, Flow/approval and bounded agent action → persona/form-factor UI → versioned dependency-aware deployment → verification, monitoring and rollback evidence. It covers sharing and analytics, relationship and field consequences, controlled data movement, bulk-safe and observable automation, Lightning/mobile activation, sandboxes/change sets/packages and ALM. Three scenarios, eight labs and 40 checks are included. The corrected August 21, 2026 weights replace the stale 23/22/28/17/10 material. Eight URLs are reachable and one O'Reilly video page is automation-blocked; none are broken. No recalled/live item, dump, shared superbadge solution or copied course content is used. Blueprint SHA-256: `5365cb37f260db38aa6b4a306dd826258e3d85f058b8111352e56a065a965f14`.

## SALESFORCE-PLATFORM-DEVELOPER coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Developer Fundamentals (27%), Process Automation and Logic (28%), User Interface (25%), and Testing, Debugging, and Deployment (20%)
- Coverage evidence: guide sections 1–4, three integrated application scenarios, eight authorized evidence labs, 40 original checks and an explicit display-title/seasonal-label reconciliation
- Link evidence: ten unique external guide URLs; nine reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: official Help seasonal label versus current Trailhead emphasis; delivery, fees, passing score and language; governor limits/order of execution/tool syntax; Agentforce and UI surfaces; course revision/access; annual maintenance deadline

The review maps every public objective through requirement and data/access model → declarative/code boundary → limit-aware SOQL/SOSL/DML and bulk Apex → Flow/Apex ownership → secure LWC/Flow/Visualforce contract → deterministic testing and correlated diagnosis → source-driven promotion, verification and rollback. It covers multitenancy/MVC, formulas/rollups/external IDs, Apex constructs/control flow/classes/triggers/exceptions/order, UI/data-access threats, developer tools/environments, asynchronous monitoring and release evidence. Three scenarios, eight labs and 40 checks are included. The current display name, legacy PD1 alias, and Help Summer ’25/current Trailhead discrepancy are explicit. Nine URLs are reachable and O'Reilly is automation-blocked; none are broken. No recalled/live item, dump, shared superbadge solution or copied course content is used. Blueprint SHA-256: `4843c3b24a93a1c4da79e50db00e79c38fa5921c6127df89e37a6754c5cddbfe`.

## SALESFORCE-AGENTFORCE-SPECIALIST coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Spring ’26 six-domain outline—Prompt Engineering (20%), Data 360 Fundamentals (20%), AI Agents (35%), Testing, Deployment, and Maintenance (10%), Governance and Observability (10%), and Multi-Agent Orchestration (5%)
- Coverage evidence: guide sections 1–6, three integrated agent scenarios, eight authorized evidence labs, 40 original checks, and an explicit exam-baseline-versus-weekly-product-change boundary
- Link evidence: 11 unique external guide URLs; ten reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: weekly Agentforce product changes versus Spring ’26 exam baseline; April 2026 subagent terminology; delivery, fees and languages; org/license availability; model, Builder, Data 360, channel, MCP/A2A and SOMA behavior; maintenance assignment/deadline; course revision/access

The review maps every public objective through approved use case and identity → governed source/chunk/index/retriever → bounded prompt/template → agent/subagent, hybrid reasoning and deterministic action contract → representative evaluation → dependency-aware promotion → correlated quality/safety/cost/business observability → rollback, incident response and improvement. It covers Prompt Builder types/access/grounding/activation/Trust Layer/model control; Data Libraries and retrieval evaluation; standard/custom subagents and actions, Agent Script, channels, execution context, Employee/Service agents and Agent API; Testing Center and lifecycle; governance and analytics; plus SOMA, MCP and A2A. Three scenarios, eight safe labs and 40 checks are included. Ten URLs are reachable and O’Reilly is automation-blocked; none are broken. The Spring ’26 outline is kept separate from Summer ’26 maintenance and later product releases. No recalled/live item, answer dump, shared superbadge solution or copied course content is used. Blueprint SHA-256: `e18e94e62ef0339b9c06f955ffd0b9d23f3ab7348e16bab214ba15f61b3e4e5b`.

## MONGODB-ASSOCIATE-DEVELOPER coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: MongoDB Overview and the Document Model (8%), CRUD (51%), Indexes (17%), Data Modeling (4%), Tools and Tooling (2%), and language-specific Drivers (18%)
- Coverage evidence: guide sections 1–6, three application scenarios, eight authorized evidence labs, 40 original checks, and an explicit selected-language/free-enrollment-guide boundary
- Link evidence: nine unique external guide URLs; seven reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: no public exam-version label; C#/Java/Node.js/PHP/Python registration and driver versions; UI/tool names; server/Atlas/operator defaults and limits; exam delivery/policy; course revision/access

The review maps every domain through typed document contract → exact filter/options/update/projection and predicted result → atomicity/concurrency behavior → workload/model boundary → query-shaped index and `explain` evidence → shell/tool verification → selected official-driver syntax, pool, cursor, error and security behavior. It includes BSON, flexible shapes, array and embedded queries, replacement/operator/upsert/delete/find-and-modify, common aggregation, index costs, embedding/referencing, Atlas sample exploration, URIs and injection-resistant application construction. Three scenarios, eight safe labs and 40 checks are included. Seven URLs are reachable; O’Reilly and Udemy are automation-blocked; none are broken. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `7b8ee2749e9fe5f87fefc15268c82cd74a50ee45e682d1c6c83a552568fc25d6`.

## MONGODB-ASSOCIATE-DATA-MODELER coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Requirements Gathering (10%), Entities (13%), Relationships (8.5%), Workload/Usage (10%), Data Model Design (28%), Modeling for Technical Requirements (10%), Indexing (13%), and Monitoring and Evolving Data Models (7.5%)
- Coverage evidence: guide sections 1–8, three integrated scenarios, eight authorized evidence labs, 40 original readiness checks, and an explicit current-contract/free-enrollment-guide boundary
- Link evidence: 12 unique external guide URLs; nine reachable, three automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: current 75-question/110-minute landing page versus stale 70/105 course route; no public exam-version label; enrolled guide revision; August 2026 skill-badge/path alignment and discount; server/Atlas/query-engine/UI behavior; exam delivery, price and policy

The review maps all eight weighted domains through requirements and ownership, entity/relationship/cardinality analysis, measurable workloads, compared document models and patterns, technical constraints, query-shaped indexes, and observable compatible evolution. Three scenarios, eight safe labs and 40 original checks are included. The current-versus-stale exam contract and free-enrollment guide boundary are explicit. Nine URLs are reachable and three paid pages are automation-blocked; none are broken. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `e3b9632a8ab5b80cdb74a5ccd557cdc482917c1aca71f116b804b9fd6f92fd10`.

## MONGODB-ASSOCIATE-ATLAS-ADMINISTRATOR coverage record

- Reviewed: September 2, 2026
- Outcome: **public sources + official learning-path scope checked; enrolled-objective reconciliation still required**
- Official public scope: 13 current required path skills—MongoDB Overview; CRUD Operations; Fundamentals of Data Transformation; Indexing Design Fundamentals; Query Optimization; Sharding Strategies; Monitoring Tooling; Performance Tools and Techniques; Data Resilience: Atlas; Cluster Reliability; Secure MongoDB Atlas: AuthN and AuthZ; Networking Security: Atlas; and Encryption at Rest
- Coverage evidence: guide sections 1–7, three integrated scenarios, eight authorized evidence labs, 40 original readiness checks, and an explicit unweighted-public-path versus enrolled-detailed-guide boundary
- Link evidence: 12 unique external guide URLs; nine reachable, three automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: detailed objective weights behind free enrollment; live 70-question/95-minute contract versus stale two-hour path card; current 13-hour path versus superseded 11.5-hour v1; feature/tier/provider/region eligibility and limits; Atlas UI/CLI/API/IaC; identity/network/KMS/backup/monitoring behavior; exam policy and price

The review maps the complete current public 13-skill learning path as the available official objective scope through MongoDB operations and query evidence, Atlas topology and sharding, separated control/data-plane identities, layered network/encryption controls, observable performance diagnosis, tested resilience/recovery, and safe UI/CLI/API/IaC administration. Three scenarios, eight safe labs and 40 original checks are included. MongoDB gates the more detailed objective guide behind free enrollment, so a maintainer must still reconcile that enrolled outline; no hidden weights are invented. Nine URLs are reachable and three paid pages are automation-blocked; none are broken. No recalled/live item, answer dump or copied course content is used. Public-scope SHA-256: `7aa8a437967e8cbf16e95913b1aeb5854e8acff22fd223793292aa2774d6a273`.

## SERVICENOW-CSA coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Platform Overview and Navigation (7%), Instance Configuration (10%), Configuring Applications for Collaboration (20%), Self Service and Automation (20%), Database Management and Platform Security (30%), and Data Migration and Integration (13%)
- Coverage evidence: guide sections 1–6, three integrated scenarios, eight authorized nonproduction labs, 40 original readiness checks, and explicit mainline-versus-delta and UI-visibility-versus-authorization boundaries
- Link evidence: 11 unique external guide URLs; nine reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: twice-yearly release documentation and UI labels; course/entitlement/duration; PDI availability; Pearson/OnVUE policy, fee and language; registration window; conditional-result review; undisclosed cut score; yearly CMP and assigned annual delta

The review maps all six weighted domains through role-aware navigation and record context, supported instance change, collaborative lists/forms/tasks/analytics/notifications, governed knowledge/catalog/flow/Virtual Agent paths, controlled schema/import/CMDB/security design, and testable UI policies, Business Rules, scripting and update-set transport. Three scenarios, eight safe labs and 40 checks are included. The January 2026 mainline scope is kept separate from the release-specific 2026 delta guide, whose window has closed. Nine URLs are reachable and two are automation-blocked; none are broken. Only ServiceNow's official MeasureUp product is listed for exam-style practice, consistent with ServiceNow's dump warning. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `9a7543abda6dcc1af08f0fba350c382652ed41eac6a2de9599f7c80d223b99e9`.

## SERVICENOW-CAD coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Designing and Creating an Application (15%), Application User Interface (20%), Security and Restricting Access (20%), Application Automation (20%), Working with External Data (10%), and Managing Applications (15%)
- Coverage evidence: guide sections 1–6, three integrated application scenarios, eight authorized nonproduction labs, 40 original readiness checks, and explicit mainline/MeasureUp-weighting, client/server, visibility/authorization and lifecycle-tool boundaries
- Link evidence: 11 unique external guide URLs; eight reachable, three automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: the official MeasureUp 20/20/20/20/10/10 practice-bank distribution versus the KB0011498 15/20/20/20/10/15 baseline; twice-yearly release UI/API/tooling; dynamic course access/duration; PDI availability; Pearson policy/price/language; scoring review; annual delta and CMP

The review maps all six January 2026 domains through requirement and platform-fit decisions, scoped data/application design, persona-tested client and server behavior, layered access and cross-scope security, idempotent declarative/scripted automation, reconciled CSV/Excel and REST integration, and controlled repository/Git/delegated-development delivery with tests and rollback. Three scenarios, eight safe labs and 40 checks are included. The official MeasureUp bank's displayed distribution is treated as a practice-product discrepancy, not used to overwrite the mainline blueprint. Eight URLs are reachable and three are automation-blocked; none are broken. Only ServiceNow's official MeasureUp product is listed for exam-style questions. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `d0d60a1f5b77d3baa45857b05b7e01c67ab7f5afdbc53dc0558c660f244b21b0`.

## PANW-CYBERSECURITY-APPRENTICE coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Cybersecurity (16%), Network Fundamentals (16%), Network Security (14%), Endpoint Security (10%), Cloud Security (13%), Security Operations (13%), and Identity Security (18%)
- Coverage evidence: guide sections 1–7, three integrated security scenarios, eight authorized labs, 40 original readiness checks, and explicit vendor-neutral-concept-versus-product and published-versus-omitted-contract boundaries
- Link evidence: 12 unique external guide URLs; ten reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: datasheet/version replacement; Pearson duration, item count and price; handbook, retake and renewal rules; product family names and capabilities; learning-path access and duration; cloud/provider features and standards

The review maps all seven May 2026 domains through threat, vulnerability, control and Zero Trust reasoning; packet and protocol flow; segmentation, inspection, secure transport and DLP; endpoint/IoT hardening and recovery; cloud responsibility and CI/CD; evidence-led SOC response; and identity, federation, PAM, PKI and secrets lifecycle. Three scenarios, eight safe labs and 40 checks are included. The public datasheet does not state base duration, item count or price, so the guide preserves those omissions and directs candidates to live Pearson registration. Ten links are reachable and two are automation-blocked; none are broken. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `fbd3b8491d4f5a04b8592653652089dcb6e1fe7f7e1948a974dd37469f1673b7`.

## NSE-4-FORTIOS coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Deployment and system configuration (20–25%), Firewall policies and authentication (20–25%), Content inspection (25–30%), Routing (10–15%), and VPNs (10–15%)
- Coverage evidence: guide sections 1–5, three integrated traffic scenarios, eight authorized FortiOS labs, 40 original readiness checks, and explicit current-NSE-versus-old-FCP and range-versus-false-normalization boundaries
- Link evidence: 14 unique external guide URLs; 12 reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: FortiOS product/exam version; count/time/language/price and delivery; July 2026 transition terminology; model/license/feature availability; course naming/access/duration; firmware/upgrade path; FortiGuard, cloud and SASE behavior; renewal/recertification assessments

The review maps every current 7.6.0 task through management and recoverability, log/HA/resource/failure evidence, FortiGate VM/CNF and FortiSASE boundaries, first-match policy/session/NAT and LDAP/RADIUS/FSSO identity, flow/proxy and certificate/full inspection, web/application/AV/IPS controls, route and SD-WAN decisions, and complete redundant IPsec paths. Three scenarios, eight safe labs and 40 checks are included. The five published ranges are preserved as ranges; no artificial point distribution is invented. The old FCP/FortiGate Administrator wording is kept separate from the live NSE 4 FortiOS credential. Twelve links are reachable and two commercial pages are automation-blocked; none are broken. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `1b33e766a66667a35836c8bdc2632bd72c3489d5d265e3cf4fe52452c72cfc6f`.

## SPLK-5001 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: The Cyber Landscape, Frameworks, and Standards (10%); Threat and Attack Types, Motivations, and Tactics (20%); Defenses, Data Sources, and SIEM Best Practices (20%); Investigation, Event Handling, Correlation, and Risk (20%); SPL and Efficient Searching (20%); Threat Hunting and Remediation (10%)
- Coverage evidence: guide sections 1–6, three integrated SOC scenarios, eight authorized labs, 40 original readiness checks, and explicit blueprint-era-versus-current-ES and publicly-visible-versus-course-gated boundaries
- Link evidence: 17 unique external guide URLs; 13 reachable, four automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: unversioned blueprint; ES notable/risk-event versus finding/intermediate-finding terminology; dashboards, navigation and SOAR pairing; course availability/duration; item/time/price/delivery and lifecycle policy; acceleration/source/schema state

The review maps all detailed objectives 1.1–6.4 through SOC roles, assurance,
framework and risk reasoning; attacks, intelligence, TTPs and annotations;
source selection, sourcetypes, CIM, data models, acceleration, assets and
identities; reproducible investigation, disposition, dashboards and risk-based
alerting; command semantics, early filtering and Job Inspector; and
hypothesis-led hunting with reversible, approved response. Three scenarios,
eight safe labs and 40 checks are included. The thin live track page is the
monitored snapshot and the four-page PDF is registered as the full detailed
authority. Blueprint-era terms are reconciled with current ES terminology. The
five official investigation-stage labels are not reconstructed because the
public course description confirms but does not enumerate them. Thirteen links
are reachable and four are automation-blocked; none are broken. No recalled or
live item, dump, guaranteed-match simulation or copied course content is used.
Blueprint SHA-256: `a2bd1aa1350f373525e5d2f66cfc38f7023f6b84cf9275f594421412fbd704f5`.

## CISA coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Information Systems Auditing Process (18%), Governance and Management of IT (18%), Information Systems Acquisition, Development, and Implementation (12%), Information Systems Operations and Business Resilience (26%), and Protection of Information Assets (26%)
- Coverage evidence: guide sections 1–5, three integrated assurance scenarios, eight safe evidence labs, 40 original readiness checks, and explicit exam-pass-versus-certification and auditor-versus-management boundaries
- Link evidence: 14 unique external guide URLs; 13 reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: outline/job-practice revision; price, delivery, identification and retake rules; experience waivers and application; standards and regulation; technology examples; preparation-product access; January 2027 CPE policy

The review maps every published CISA topic and supporting task through risk-based
planning, sampling and reproducible evidence, finding and follow-up, enterprise
governance and supplier assurance, controlled acquisition/development/release,
operational control and dependency-aware recovery, and layered identity,
infrastructure, data and incident protection. Three scenarios, eight labs and 40
checks are included. Passing the exam is not represented as holding CISA: the
experience, application, ethics, audit-standards and CPE obligations are explicit.
Thirteen URLs are reachable and O'Reilly is automation-blocked; none are broken.
No recalled/live item, answer dump or copied course content is used. Blueprint
SHA-256: `1b6d14e1c7adfd585869f75f8ea1fb822dcb73a696cabca5c6dc7e7c9ea9d25e`.

## CISM coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope through November 2: Information Security Governance (17%), Information Security Risk Management (20%), Information Security Program (33%), and Incident Management (30%)
- Coverage evidence: guide sections 1–4, three integrated management scenarios, eight safe labs, 40 original checks, and explicit risk-owner, manager-versus-operator and exam-pass-versus-designation boundaries
- Link evidence: 14 unique external guide URLs; 11 reachable, three automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: mandatory November 3, 2026 outline change; undisclosed replacement weights; preparation-material version; delivery/fee/retake rules; experience/application; technology/regulation; January 2027 CPE policy

The review maps all current domains and supporting tasks through accountable
governance and strategy, scenario-led risk assessment and treatment, a complete
people/process/technology/supplier program, and tested incident readiness,
containment, recovery, communications and improvement. Three scenarios, eight
labs and 40 checks are included. The guide does not invent the November outline:
it remains explicitly usable only through November 2 unless reconciled after
publication. Eleven URLs are reachable and two O'Reilly pages plus Udemy are
automation-blocked; none are broken. Only ISACA resources are named as official
item-style sources. Blueprint SHA-256:
`4e9e04334324b59c3a0c64acb24760b722d7319b15ffa7ab7b81ec9c21cbff46`.

## CRISC coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Governance (26%), Risk Assessment (22%), Risk Response and Reporting (32%), and Technology and Security (20%)
- Coverage evidence: guide sections 1–4, three integrated risk scenarios, eight safe labs, 40 original checks, and explicit risk-owner/control-owner/assurance and exam-pass/designation boundaries
- Link evidence: 12 unique external guide URLs; ten reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: outline/job-practice revision; risk terminology and method choices; technology/threat/regulation; supplier and cloud responsibilities; exam delivery/fee/retake; experience/application; January 2027 CPE policy

The review maps every effective-2025 topic through aligned governance, risk
appetite/tolerance and accountable roles; scenario identification, BIA and
defensible analysis; owned response, control design/implementation/testing and
decision-ready indicators; and technology architecture, operations, delivery,
data, resilience, security and privacy implications. Three scenarios, eight labs
and 40 checks are included. Ten URLs are reachable and O'Reilly/Udemy are
automation-blocked; none are broken. Only ISACA resources are presented as
official item-style sources. Blueprint SHA-256:
`8a607e350fc322e463cf56ebad620f53e5c2826017f3235aab6f04baf97bd614`.

## PCEP-30-02 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Computer Programming and Python Fundamentals (18%); Control Flow — Conditional Blocks and Loops (29%); Data Collections — Tuples, Dictionaries, Lists, and Strings (25%); Functions and Exceptions (28%)
- Coverage evidence: guide sections 1–4, three integrated programming scenarios, eight hands-on labs, 40 original readiness checks, and explicit aliasing/mutability, error/exception, current/future-version, and syllabus/practice-weight boundaries
- Link evidence: 12 canonical external guide URLs; ten reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: PCEP-30-03 Q3 2026 release; active/purchasable exam version; credential validity; delivery, price, language and retake policy; Python runtime behavior; learning-product access/runtime; official practice-product weight discrepancy

The review maps every published PCEP-30-02 topic through source execution,
lexis/syntax/semantics, literals and names, scalar types, conversions, operators
and console I/O; precise conditional and loop tracing; list/tuple/dictionary/string
operations and object aliasing; and function calls, scope, recursion, generation,
exception hierarchy and propagation. Three scenarios, eight labs and 40 checks
require prediction followed by execution and explanation. The detailed syllabus's
18/29/25/28 weights remain authoritative; the official practice product's
18/28/26/28 display is recorded as a discrepancy. PCEP-30-03 is not treated as
current until the credential page says it is. Ten URLs are reachable and
O'Reilly/Udemy are automation-blocked; none are broken. No recalled/live item,
answer dump or copied paid-course question is used. Blueprint SHA-256:
`fc0a0b67b1f15a4430075b889978a82e162d98642f0b822768bc3796c322ca57`.

## CPE-20-01 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Syntax, Literals, and Operators (28%); Flow Control and Functions (28%); Vectors and Pointers (24%); Structures and Strings (20%)
- Coverage evidence: guide sections 1–4, three integrated programming scenarios, eight hands-on labs, 40 original readiness checks, and explicit type/lifetime, reference/pointer, array/vector, raw/modern-ownership, and `std::string`/character-array boundaries
- Link evidence: 11 unique external guide URLs; nine reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: active exam version; syllabus revision; language-standard assumptions; count/time/format/language/price/delivery and retake policy; credential validity; learning-product access/runtime

The review maps every published CPE-20-01 objective through translation and
diagnostics, declarations/types/literals/conversions/operators and stream state;
structured selection/iteration plus function declaration, return, parameter
mechanisms and recursion; arrays, multidimensional data, vectors and `data()`
invalidation, pointer validity, named-cast purpose and matching manual allocation;
and structures, vectors of records, and owned strings. Three scenarios, eight
labs and 40 original checks require prediction, compilation, testing and
explanation. Raw `new`/`delete` are covered because the syllabus names them,
while container/resource ownership is labeled as related practical context.
Nine URLs are reachable and O'Reilly/Udemy are automation-blocked; none are
broken. The objective monitor's Python transport encountered a local
certificate-chain error even though the source-health client and browser fetched
the official page; its exact public objective block was therefore preserved as
the dated snapshot without changing the content. No recalled/live item, answer
dump or copied course content is used. Blueprint SHA-256:
`faf4501642933ecdc38efb270dda58a7db3a7c95a0028bda125b61544a34f60d`.

## JSE-40-01 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Introduction to JavaScript and Computer Programming; Variables, Data Types, and Type Casting; Operators and User Interaction; Control Flow — Conditional Execution and Loops; Functions; Errors, Exceptions, Debugging, and Troubleshooting
- Coverage evidence: guide sections 1–6, three integrated browser scenarios, eight hands-on labs, 40 original readiness checks, and explicit core-language/host, conversion/validation, primitive/reference, `for...in`/`for...of`, synchronous/asynchronous-callback, and exception/logic-error boundaries
- Link evidence: 11 unique external guide URLs; nine reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: active exam version; unweighted main scope versus official practice-kit distribution; count/time/format/language/price/delivery and retake policy; browser/runtime behavior; learning-product access/runtime and archived supporting content

The review maps every JSE-40-01 objective through browser/client/server execution;
declaration, scope, shadowing and hoisting; primitive types, strings, arrays,
record objects, aliases and conversion; operator semantics and dialog return
values; selection and all named loop forms; declaration/expression/arrow
functions, first-class values, recursion and timer callbacks; and the four named
error types, handling, throwing and evidence-led debugging. Three scenarios,
eight labs and 40 original checks require prediction, browser execution and
explanation. The main scope remains the objective authority and publishes no
weights; the 8/20/18/21/21/12 figures are explicitly attributed to the official
JSE-40-01 practice kit's content distribution. Nine URLs are reachable and
O'Reilly/Udemy are automation-blocked; none are broken. No recalled/live item,
answer dump or copied course content is used. Blueprint SHA-256:
`8e693613dc23a1fcc95ab41c1675897253aa341764d5d9127ff7fc48aeb29e46`.

## CLE-10-01 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Basic Concepts (13.25%); Data Types, Evaluations, and Basic I/O Operations (13.25%); Arithmetic, Logical, and Bitwise Operators (13.25%); Decision-Making Statements (13.25%); Loops (16.50%); Arrays, Pointers, and Memory Management (16.50%); String Manipulation (7%); Functions (7%)
- Coverage evidence: guide sections 1–8, three integrated C-programming scenarios, eight hands-on labs, 30 original readiness checks, and explicit translation-stage, type/conversion, input-validation, short-circuit/bitwise, array/pointer, storage-lifetime, string-capacity, and value/pointer-parameter boundaries
- Link evidence: 10 unique external guide URLs; seven reachable, three automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: active exam version; July 2025 syllabus baseline; implementation and language-standard behavior; count/time/format/language/price/delivery and retake policy; learning-product access and runtime

The review maps every CLE-10-01 objective through preprocessing, compilation,
linking and runtime diagnosis; literals, numeral systems, declarations, types,
conversions and formatted I/O; arithmetic, logical, bitwise and control-flow
tracing; arrays, pointer validity, allocation ownership and object lifetime;
null-terminated strings and capacity; and function declarations, definitions,
returns and pointer parameters. Three scenarios, eight labs and 30 original
checks require prediction, compilation, testing and explanation. Precise C
terminology is used where the official syllabus is informal, and implementation
or version-dependent behavior is not presented as portable fact. The SEI,
O'Reilly and Udemy pages were automation-blocked rather than missing. No
recalled/live item, answer dump or copied course content is used. Blueprint
SHA-256:
`24a914783ae6dd53544f35edc1e6fdae598a2998c7187d1d0008adf8c1703ec9`.

## PCAP-31-03 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Modules and Packages (12%); Exceptions (14%); Strings (18%); Object-Oriented Programming (34%); Comprehensions, Lambdas, Closures, and I/O (22%)
- Coverage evidence: guide sections 1–5, three integrated Python scenarios, ten hands-on labs, 27 original knowledge checks, and explicit import/binding, exception propagation, Unicode/encoding, class/instance, inheritance/composition, closure binding, and text/binary stream boundaries
- Link evidence: 11 unique external guide URLs; ten reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: active PCAP-31-03 versus announced PCAP-31-04; March 2022 syllabus; current Python version versus tested outline; count/time/format/language/price/delivery, validity and retake policy; learning-product access/runtime

The review maps every PCAP-31-03 objective through explicit imports and package
structure, the named `math`, `random`, and `platform` operations, exception
matching and custom hierarchies, Unicode and all listed string methods,
class/instance state, introspection, inheritance and polymorphism,
comprehensions, functional tools, closure binding, and safe text/binary I/O.
Three scenarios, ten labs and 27 original checks require prediction,
implementation, boundary testing and explanation. PCAP-31-04 remains in
development while the live page identifies PCAP-31-03 as current. An initially
supplied practice-product URL returned 404 and was replaced with the verified
live OpenEDG page before publication. O'Reilly was automation-blocked rather
than missing. No recalled/live item, answer dump or copied course content is
used. Blueprint SHA-256:
`189719f136c042874d3fb6530214fa39ee69cc34f73f26675db41dd50e3eca85`.

## JSA-41-01 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Classless Objects (25%); Classes and Class-Based Approach (23%); Built-in Objects (27%); Advanced Functions (25%)
- Coverage evidence: guide sections 1–4, three integrated JavaScript scenarios, eight hands-on labs, 40 original readiness checks, and explicit identity/copy, own/inherited property, receiver, class/prototype, mutation, iteration, promise-settlement, HTTP-status, and event-loop boundaries
- Link evidence: 14 unique external guide URLs; 12 reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: active exam version; September 2025 syllabus; runtime and host-API behavior; count/time/format/language/price/delivery; learning-product access/runtime

The review maps all 40 published objectives through classless object creation,
property access/enumeration/configuration, shallow-copy and prototype reasoning;
classes, inheritance, static members and constructor equivalence; every named
built-in and collection; and parameter, closure, context, decorator, iterator,
callback, promise, async/await, XHR and Fetch behavior. Three scenarios, eight
labs and 40 original checks require prediction, implementation, boundary testing
and explanation. O'Reilly and Udemy were automation-blocked rather than missing.
No recalled/live item, answer dump or copied course content is used. Blueprint
SHA-256:
`00f65a3f8edeefdc02faacdef875af8d2535c1077cc8e932109c3d2709e75628`.

## WDE-40-01 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: HTML Fundamentals (15%); Text Formatting and Structure (20%); Multimedia and Hyperlinks (20%); Forms and Styling (25%); Accessibility, Best Practices, and Modern HTML (20%)
- Coverage evidence: guide sections 1–5, three integrated web-page scenarios, eight hands-on labs, 40 original readiness checks, and explicit source/DOM, semantics/presentation, link/embed, client/server validation, native/ARIA, storage/permission, and automated/manual accessibility-testing boundaries
- Link evidence: 13 unique external guide URLs; 11 reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: active exam version; September 2025 syllabus; count/time/format/language/price/delivery and practice-product code; browser/API behavior; WCAG version; learning-product access/runtime

The review maps all 40 objectives through a standards-mode skeleton, text and
data-table semantics, accessible links and media, labelled constrained forms,
foundational CSS and the box model, native semantics and synchronized ARIA,
microdata, Geolocation, Web Storage, SVG, performance practice and layered
accessibility testing. Three scenarios, eight labs and 40 original checks
require building, validation and explanation. The live page's WDE-41-01
practice-product wording is flagged rather than treated as the active WDE-40-01
exam code. O'Reilly and Udemy were automation-blocked rather than missing. No
recalled/live item, answer dump or copied course content is used. Blueprint
SHA-256:
`52a8efac1190c7d5b3e863705d0a0b7d4ea88ad72834aff4990051f21a9a7521`.

## WDA-41-01 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: HTML Fundamentals (25%); CSS Fundamentals (22.5%); Integrating HTML and CSS (25%); Responsive Web Design and Layout Techniques (12.5%); Accessibility, Usability, and Best Practices (15%)
- Coverage evidence: guide sections 1–5, three integrated production-page scenarios, ten hands-on labs, 40 original readiness checks, and explicit semantic/presentation, cascade/specificity, position/stacking, framework/standards, source/delivery, automated/manual testing, mobile-first, enhancement/fallback, performance/quality, and analytics/privacy boundaries
- Link evidence: 17 unique external guide URLs; 15 reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: active exam version; September 2025 syllabus; contradictory official duration wording; browser/CSS/platform behavior; Core Web Vitals; delivery/price/practice; learning-product access/runtime

The review maps all 40 objectives through semantic HTML; CSS syntax, cascade,
specificity, boxes, positioning, effects, framework and preprocessor concepts;
style delivery, component construction, accessible forms and debugging; Flexbox,
Grid, media queries, responsive assets and fallbacks; accessibility, usability,
quality, SEO, performance and privacy-aware analytics. Three scenarios, ten labs
and 40 original checks require construction, inspection, measurement, testing
and explanation. The official page's 60-minute label versus approximately
65-minute exam text remains an explicit booking-time check. O'Reilly and Udemy
were automation-blocked rather than missing. No recalled/live item, answer dump
or copied course content is used. Blueprint SHA-256:
`747cb21a7c881c08b2b1107feb22733528ec25faab300998abb8ac499af07c5d`.

## CLA-11-03 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Language and Structures (29%); Data Operations (38%); Control Flow (25%); Environment (8%)
- Coverage evidence: guide sections 1–4, three integrated multi-file C scenarios, eight hands-on labs, 30 original readiness checks, and explicit declaration/definition, scope/linkage/duration/lifetime, precedence/evaluation, pointer/range, allocation/ownership, macro/function, and parse/EOF/error boundaries
- Link evidence: 10 unique external guide URLs; seven reachable, three automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: active exam version; July 2025 syllabus; language-standard and implementation behavior; count/time/format/language/price/delivery; course access/runtime

The review maps all 21 objectives through lexical structure, declarations and
definitions, arrays and structures, storage classes; conversions, side effects,
pointers, allocation, scope, linkage and lifetime; control statements, loops and
function contracts; preprocessing, conditional compilation and checked stream
I/O. Three scenarios, eight labs and 30 original checks require prediction,
compilation, diagnostics and explanation. SEI, O'Reilly and Udemy were
automation-blocked rather than missing. No recalled/live item, answer dump or
copied course content is used. Blueprint SHA-256:
`3d7fc7742d22fe30306494be170081e0b38d81887ca0192d7b4ff6c9f10b2fd5`.

## CLP-12-01 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Applied Evolution of C (14.5%); Variadic Functions and Macros (9%); Low-Level I/O (13%); Memory and String Handling (16%); Process and Thread Management (9%); Numerical Types and Computations (11%); Network Socket Programming (13%); Specialized Considerations (14.5%)
- Coverage evidence: guide sections 1–8, three integrated systems-programming scenarios, eight hands-on labs, 30 original readiness checks, and explicit ISO-C/platform, API/ABI, partial-I/O/message, object/value-representation, volatile/atomic, specification/implementation, and defined/unspecified/implementation-defined/undefined boundaries
- Link evidence: 10 unique external guide URLs; eight reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: active exam version; C11-and-history blueprint versus later language standards; current POSIX and Windows documentation; count/time/format/language/price/delivery; course access/runtime

The review maps all 30 objectives through language evolution, variadic calls,
low-level descriptors, memory/string/sort/search operations, processes and C11
threads, exceptional numeric behavior, socket framing and byte order, volatile,
non-local jumps, sequencing, undefined behavior and complex declarations. Three
scenarios, eight labs and 30 original checks require explicit language/platform
labels, testing and explanation. SEI and O'Reilly were automation-blocked rather
than missing. No recalled/live item, answer dump or copied course content is
used. Blueprint SHA-256:
`ca46317388e8217cdca5a716c497f3c1b715a76d371d2c79247e1cfe7d0d0603`.

## CPA-21-02 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Types and Operators (24.5%); Control and Exceptions (18%); Functions and Preprocessor (17.5%); Pointers (11%); Classes and Namespaces (29%)
- Coverage evidence: guide sections 1–5, three integrated object-oriented C++ scenarios, eight hands-on labs, 30 original readiness checks, and explicit precedence/evaluation, reference/value, manual/RAII ownership, construction/assignment, static/dynamic type, override/overload, current/legacy-exception, and source-page consistency boundaries
- Link evidence: 11 unique external guide URLs; nine reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: active CPA-21-02 versus retired 21-01; July 2025 syllabus; tested legacy throw() versus current standards; official course's CLA-21-02 field typo; count/time/format/language/price/delivery; course access/runtime

The review maps all 35 objectives through types, conversions, expressions,
strings and aggregates; control transfers and exception unwinding; function
overloads, parameters, recursion and macros; pointer ranges and allocation; and
class invariants, special members, inheritance, dispatch, casts, friends,
operators and namespaces. Three scenarios, eight labs and 30 original checks
require prediction, compilation, diagnostics and explanation. O'Reilly and
Udemy were automation-blocked rather than missing. No recalled/live item,
answer dump or copied course content is used. Blueprint SHA-256:
`3d25434609c18c0dc30b6225e052b44235407d3d6968a3125b30d2cd77a776e0`.

## CPP-22-02 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: nine published blocks covering sequence/adaptor and associative containers; non-modifying, modifying, sorting/search, merge/set/min/max algorithms; function objects; advanced I/O; templates
- Coverage evidence: guide sections 1–9, three integrated generic-programming scenarios, ten hands-on labs, 30 original readiness checks, and explicit size/capacity, iterator/invalidation, logical/physical end, comparator/order, input/output range, persistent/one-shot format-state, deduction/conversion, and current/legacy feature boundaries
- Link evidence: 11 unique external guide URLs; nine reachable, two automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: active CPP-22-02; July 2025 page; official 40-question versus 32 counted-item and 107%-weight inconsistency; legacy ptr_fun; aligned course's CPP-22-01 label; count/time/format/language/price/delivery; course access/runtime

The review maps every named container, adapter, iterator, algorithm, callable,
stream-formatting and template objective through preconditions, returned values,
invalidation and runnable evidence. Three scenarios, ten labs and 30 original
checks are included. The provider's internally inconsistent block counts and
weights are preserved—not silently normalized—and its aligned course's stale
version is explicit. A broken provisional Pluralsight path was rejected and
replaced before publication. O'Reilly and Udemy were automation-blocked. No
recalled/live item, answer dump or copied course content is used. Blueprint
SHA-256:
`c107cc84fb7b04ddebd32b529e9e319869dd8b9d8fb91748daeec025621b9776`.

## PCPP-32-101 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Advanced Object-Oriented Programming (35%); Coding Conventions, Best Practices, and Standardization (12%); GUI Programming (20%); Network Programming (18%); File Processing and Communicating with the Environment (15%)
- Coverage evidence: guide sections 1–5, an integrated professional Python build, hands-on labs, original readiness checks, and explicit identity/value, inheritance/composition, decorator/metaclass, PEP/convention, event-loop/thread, socket/HTTP, transport/application-status, serialization/trust, and path/encoding boundaries
- Link evidence: 11 unique external guide URLs; ten reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: active PCPP-32-101 versus in-development 32-102; March 2022 syllabus versus current Python; lifetime/current-version validity; count/time/format/language/price/delivery; no official practice test; course/runtime access

The review maps every named PCPP1 objective through advanced OOP, special
methods, decorators, metaclasses and persistence; PEP 8/257 and documentation;
Tkinter event-driven design; sockets, HTTP, REST, XML and JSON; and database,
file, logging, configuration and environment modules. The labs and original
checks require an integrated application and failure-path evidence. PCPP-32-102
remains separate in-development work with no published release date. O'Reilly
was automation-blocked rather than missing. No recalled/live item, answer dump
or copied course content is used. Blueprint SHA-256:
`b36342ae9b7e21da6ba93845b94bfe42e1b72b2813c8f853e91e08c679637631`.

## PCED-30-02 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Introduction to Data and Data Analysis Concepts (22.5%); Python Basics for Data Analysis (32.5%); Working with Data and Performing Simple Analyses (32.5%); Communicating Insights and Reporting (12.5%)
- Coverage evidence: guide sections 1–4, an integrated source-to-report lab, 16 original readiness checks, and explicit collection/bias, privacy/anonymization, raw/clean, missing/invalid, sample/population, correlation/causation, outlier/error, and evidence/claim boundaries
- Link evidence: 9 unique external guide URLs; nine reachable, zero automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: active PCED-30-02 versus retired 30-01; July 2025 syllabus; exam logistics, cost, validity, delivery, official practice availability, course access and runtime

The review maps all four blocks through data concepts and ethics; Python core
constructs; file, CSV and NumPy workflows; cleaning, descriptive statistics,
exploratory analysis and outliers; and audience-aware visualization and
reporting. The integrated lab preserves raw data and requires every claim to be
traced to code and source evidence. No recalled/live item, answer dump or
copied course content is used. Blueprint SHA-256:
`d3b9a519347510e7f6564eb07ef2bbaebf8774f7d2bc61560f944717bc770d12`.

## PCAD-31-02 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Data Acquisition and Pre-Processing (29.2%); Programming and Database Skills (33.3%); Statistical Analysis (8.3%); Data Analysis and Modeling (18.8%); Data Communication and Visualization (10.4%)
- Coverage evidence: guide sections 1–5, an integrated analysis portfolio lab, 20 original readiness checks, and explicit collection/permission, raw/clean, imputation/exclusion, parameter/data, descriptive/inferential, association/causation, validation/test, metric/decision, and evidence/claim boundaries
- Link evidence: 12 unique external guide URLs; all twelve reachable, zero automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: active PCAD-31-02 versus retired 31-01; July 2025 syllabus; in-development PD101 and PCPD; library versions; exam logistics, price, validity, official practice and course availability

The review maps every published block through data acquisition, integrity and
preprocessing; Python, SQL, OOP and exception handling; statistics; Pandas and
NumPy analysis; introductory models and evaluation; and visualization and
reporting. The portfolio lab requires reproducible transformations, tests,
figures and an executive summary. No recalled/live item, answer dump or copied
course content is used. Blueprint SHA-256:
`987bb1bd68b7df55fb008bb96de6a3b1b407c1d63c042e35437ab2eadd4532bf`.

## PCET-30-01 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Core Software Testing Concepts (17.1%); Software Testing Types, Levels, and Processes (22.9%); Static Analysis, Dynamic Testing, and Code Refactoring (28.6%); Debugging, Assertions, and Testing Techniques (31.4%)
- Coverage evidence: guide sections 1–4, an integrated requirements-to-report lab, original readiness checks, and explicit error/defect/failure, verification/validation, level/type, isolated/integrated, statement/decision, refactoring/behavior-change, assertion/validation, and expected/actual boundaries
- Link evidence: 7 unique external guide URLs; six reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: official 30-01 header/alignment versus 30-02 introductory prose; December 2024 syllabus; exam logistics and price; official practice test still in development; course availability and runtime

The review maps all four blocks through testing foundations, test process and
documentation, levels/types and doubles, reviews and static analysis, coverage,
refactoring, debugging, assertions, unittest and test-design techniques. The
provider's exam-code inconsistency is preserved rather than silently corrected.
O'Reilly was automation-blocked. No recalled/live item, answer dump or copied
course content is used. Blueprint SHA-256:
`2ba098e2104bb457258687cdcd07afcc3a531ab146c27b0022a9bebb5d793aec`.

## PCAT-31-01 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Software Testing Essentials (16.7%); Test Automation and Code Refactoring (9.5%); Assertions, Context Managers, Decorators, and Python Methods (11.9%); Foundations of Unit Testing (28.6%); Advanced Unit Testing Techniques (26.2%); Test-Driven and Behavior-Driven Development (7.1%)
- Coverage evidence: guide sections 1–6, an integrated multi-module test suite, original readiness checks, and explicit principle/heuristic, automation/value, assertion/validation, unit/integration, mock/fake, patch/lookup, expected-failure/ignored-failure, TDD/after-the-fact, and BDD/UI boundaries
- Link evidence: 8 unique external guide URLs; all eight reachable, zero automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: active PCAT-31-01 and in-development 31-02; official 31-02/four-block introductory prose versus 31-01/six-block header/table; July 2024 syllabus; practice test in development; logistics, price and course access

The review maps every six-block objective through runnable unittest work,
fixtures and discovery, assertions, parameterization, selection, mocks and
patching, exception paths, refactoring, TDD and BDD. The provider's conflicting
introductory text is preserved as a version warning. No recalled/live item,
answer dump or copied course content is used. Blueprint SHA-256:
`d93b7e4da42b76c0263e9ea2964b023f65d3aa2ac20d43384e0686e0dca7b724`.

## PCES-30-01 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Security Essentials (22%); IT Systems Security (27%); Python for Security Operations (29%); Secure Development and Implementation in Python (22%)
- Coverage evidence: guide sections 1–4, an authorized local defensive-automation lab, original readiness checks, and explicit threat/risk, authentication/authorization, scan/attack, encoding/encryption, hash/integrity, secret/configuration, subprocess/shell, detection/response, and evidence/conclusion boundaries
- Link evidence: 10 unique external guide URLs; nine reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: August 2025 syllabus; PCES practice tests still described as coming Q3/Q4 2026; PCAS described as coming Q4 2026; library versions, logistics, price and access

The review maps all four blocks through risk, system and network safeguards,
identity and remote/cloud basics, authorized Python monitoring and automation,
and secure implementation with named libraries. Labs are explicitly limited to
owned or authorized systems. O'Reilly was automation-blocked. No recalled/live
item, answer dump or copied course content is used. Blueprint SHA-256:
`20acb805135538b41982013c936788e9324272472a840145161037a56ef6f38f`.

## PCEA-30-01 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Fundamentals of Automation (13%); Basic Command-Line Automation with Python (19.5%); Logging and Monitoring Essentials (15%); Basic File and Data Automation (17.5%); Basic Web and API Automation (17.5%); Scheduling, Notifications, and Reporting (17.5%)
- Coverage evidence: guide sections 1–6, an integrated bounded-automation lab, original readiness checks, and explicit candidate/judgment, argument/configuration, stdout/stderr/log, source/backup, API/scrape, shell/argument-list, scheduled/overlapping, notification/incident, and run/report boundaries
- Link evidence: 8 unique external guide URLs; seven reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: credential page says limited availability/small-market-trial/beta while syllabus says active; September 2025 syllabus; availability, objectives, scoring, policies, libraries and paid access

The review maps every beta objective through an automation that is safe to
rerun, observable, configurable, recoverable and schedulable. The provider's
status disagreement is shown prominently and availability must be verified
before purchase. O'Reilly was automation-blocked. No recalled/live item,
answer dump or copied course content is used. Blueprint SHA-256:
`9f423ac89c4180e798cb2bda0bfa89ca5316710b48f39a374a55332771577cdd`.

## PCEI-30-01 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Artificial Intelligence Fundamentals (14%); Machine Learning Fundamentals (16.5%); Data Handling, Analysis, and Visualization (16.5%); Neural Networks, Deep Learning, and Generative AI (22.5%); Responsible AI, Ethics, and Critical Thinking (16.5%); AI Projects, Collaboration, and Communication (14%)
- Coverage evidence: guide sections 1–6, an integrated bounded-AI lab, original readiness checks, and explicit training/inference, feature/label, validation/test, association/causation, model/metric, capability/claim, prompt/evidence, fairness/equality, automation/accountability, and prototype/production boundaries
- Link evidence: 11 unique external guide URLs; ten reachable, one automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: December 2025 syllabus; objective 2.2's mismatched testing heading; past-due Q1 2026 PCAI/practice announcements and separate Q3/Q4 2026 practice pricing; library and course changes

The review maps every module through small auditable Python tasks and explicit
problem, data, metric, limitation and human-decision evidence. The provider's
mislabeled objective heading and unreconciled dated announcements are preserved
as warnings. O'Reilly was automation-blocked. No recalled/live item, answer
dump or copied course content is used. Blueprint SHA-256:
`e5fdda2adf0c6e0b035be96b13269a63f7ca7aaf52183c123a3d2af3a9a1301e`.

## SPLUNK-CORE-USER coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Splunk Basics (5%); Basic Searching (22%); Using Fields in Searches (20%); Search Language Fundamentals (15%); Using Basic Transforming Commands (15%); Creating Reports and Dashboards (12%); Creating and Using Lookups (6%); Creating Scheduled Reports and Alerts (5%)
- Coverage evidence: guide sections 1–8, three integrated scenarios, safe hands-on labs, original readiness checks, and explicit event/index-time, filter/transform, lookup/join, schedule/time-window, report/dashboard, and alert/incident boundaries
- Link evidence: 14 unique external guide URLs; five reachable, nine automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: unversioned blueprint; SPL versus SPL2 availability; product UI and permissions; price, delivery and lifecycle policy; course availability and runtime

The review maps every detailed objective through a single evidence-led search-to-alert path. Learners must constrain data and time, interpret events and fields, explain each SPL stage, validate transformations and unmatched lookups, and preserve permissions and schedule semantics when sharing or alerting. The current public blueprint remains the authority; newer product features do not silently replace its classic SPL contract. Splunk Help, O'Reilly and Udemy endpoints were automation-blocked rather than missing. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `12b7fe480f890afd5f9bab87a17cd67eb1952d32720b92f86d57b9e5fae42c77`.

## SPLUNK-CORE-POWER-USER coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Transforming Commands for Visualizations (5%); Filtering and Formatting Results (10%); Correlating Events (15%); Creating and Managing Fields (10%); Field Aliases and Calculated Fields (10%); Tags and Event Types (10%); Macros (10%); Workflow Actions (10%); Data Models (10%); Common Information Model Add-On (10%)
- Coverage evidence: guide sections 1–10, connected scenarios, safe labs, original checks, and explicit transaction/stats, search/where, field-alias/calculated-field, event-type/tag, private/shared and raw/CIM boundaries
- Link evidence: 14 unique external guide URLs; six reachable, eight automation-blocked, zero missing/broken in dated source-health evidence
- Volatile boundaries: unversioned blueprint; SPL versus SPL2; knowledge-object scope and permissions; CIM release; course availability; price, delivery and lifecycle policy

The review maps the full blueprint through searches whose transformations can be explained and reusable objects whose scope, ownership, permissions and dependencies can be inspected. The integrated work requires a two-sourcetype normalization path, equivalent correlation approaches and validation of both matched and unmatched data. Eight commercial or Splunk Help endpoints were automation-blocked rather than missing. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `e5715fa538ca2139d8472fd5aa4122ddf4651abe8f41794ddb6347760aa5f1d1`.

+## SPLUNK-ADVANCED-POWER-USER coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Exploring Statistical Commands (4%); Exploring eval Command Functions (4%); Exploring Lookups (4%); Exploring Alerts (4%); Advanced Field Creation and Management (4%); Working with Self-Describing Data and Files (3%); Advanced Search Macros (3%); Acceleration: Reports and Summary Indexing (4%); Acceleration: Data Models and tsidx Files (4%); Using Search Efficiently (4%); More Search Tuning (3%); Manipulating and Filtering Data (6%); Working with Multivalued Fields (7%); Using Advanced Transactions (5%); Working with Time (2%); Using Subsearches (6%); Creating a Prototype (4%); Using Forms (5%); Improving Performance (6%); Customizing Dashboards (6%); Adding Drilldowns (7%); Adding Advanced Behaviors and Visualizations (5%)
- Coverage evidence: guide sections 1–22, integrated scenarios, safe hands-on labs, original readiness checks, and explicit architecture, governance, performance and security boundaries where relevant
- Link evidence: 13 unique external guide URLs; 5 reachable, 8 automation-blocked, 0 missing/broken in dated source-health evidence
- Volatile boundaries: live certification status, blueprint revision, product behavior and terminology, course availability and exam logistics

The review maps every published objective group to applied evidence rather than memorized labels. Related items are explicitly separated from the blueprint contract, and commercial resources remain optional supplements. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `88bf95c61b865a715feb43849ff3ba24a64fff0218c4c17d8f7cd589b2232815`.


+## SPLUNK-CLOUD-ADMIN coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Splunk Cloud Overview (5%); Index Management (5%); User Authentication and Authorization (5%); Splunk Configuration Files (5%); Getting Data in Cloud (15%); Forwarder Management (5%); Monitor Inputs (15%); Network and Other Inputs (10%); Fine-tuning Inputs (5%); Parsing Phase and Data Preview (10%); Manipulating Raw Data (10%); Installing and Managing Apps (5%); Working with Splunk Cloud Support (5%)
- Coverage evidence: guide sections 1–13, integrated scenarios, safe hands-on labs, original readiness checks, and explicit architecture, governance, performance and security boundaries where relevant
- Link evidence: 13 unique external guide URLs; 5 reachable, 8 automation-blocked, 0 missing/broken in dated source-health evidence
- Volatile boundaries: live certification status, blueprint revision, product behavior and terminology, course availability and exam logistics

The review maps every published objective group to applied evidence rather than memorized labels. Related items are explicitly separated from the blueprint contract, and commercial resources remain optional supplements. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `ef925e6aab94980171d47b8162c03c13e5c3800eabc87783f58807030e2b4955`.


+## SPLUNK-ENTERPRISE-ADMIN coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Splunk Admin Basics (5%); License Management (5%); Splunk Configuration Files (5%); Splunk Indexes (10%); Splunk User Management (5%); Splunk Authentication Management (5%); Getting Data In (5%); Distributed Search (10%); Getting Data In – Staging (5%); Configuring Forwarders (5%); Forwarder Management (10%); Monitor Inputs (5%); Network and Scripted Inputs (5%); Agentless Inputs (5%); Fine Tuning Inputs (5%); Parsing Phase and Data (5%); Manipulating Raw Data (5%)
- Coverage evidence: guide sections 1–17, integrated scenarios, safe hands-on labs, original readiness checks, and explicit architecture, governance, performance and security boundaries where relevant
- Link evidence: 5 unique external guide URLs; 3 reachable, 2 automation-blocked, 0 missing/broken in dated source-health evidence
- Volatile boundaries: live certification status, blueprint revision, product behavior and terminology, course availability and exam logistics

The review maps every published objective group to applied evidence rather than memorized labels. Related items are explicitly separated from the blueprint contract, and commercial resources remain optional supplements. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `5d446f18d95406a4a21e6b7f3ead1530c6bd7b7faa89719d8ecaa3593c179c5c`.


+## SPLUNK-ENTERPRISE-ARCHITECT coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Introduction (2%); Project Requirements (5%); Infrastructure Planning: Index Design (5%); Infrastructure Planning: Resource Planning (7%); Clustering Overview (5%); Forwarder and Deployment Best Practices (6%); Performance Monitoring and Tuning (5%); Splunk Troubleshooting Methods and Tools (5%); Clarifying the Problem (5%); Licensing and Crash Problems (5%); Configuration Problems (5%); Search Problems (5%); Deployment Problems (5%); Large-scale Splunk Deployment Overview (5%); Single-site Indexer Cluster (5%); Multisite Indexer Cluster (5%); Indexer Cluster Management and Administration (7%); Search Head Cluster (5%); Search Head Cluster Management and Administration (5%); KV Store Collection and Lookup Management (3%)
- Coverage evidence: guide sections 1–20, integrated scenarios, safe hands-on labs, original readiness checks, and explicit architecture, governance, performance and security boundaries
- Link evidence: 6 unique external guide URLs; 3 reachable, 3 automation-blocked, 0 missing/broken in dated source-health evidence
- Volatile boundaries: live status, blueprint revision, topology guidance, product terminology, course completion and exam logistics

The review maps every published objective group to applied evidence rather than memorized labels. Related items are explicitly separated from the blueprint contract. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `0c28e1dbc996a44c1bfad21e83bfcea0bd69645bbee8432a0a93e23262d102f4`.


+## SPLUNK-CORE-CONSULTANT coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Deploying Splunk (5%); Monitoring Console (8%); Access and Roles (8%); Data Collection (15%); Indexing (14%); Search (14%); Configuration Management (8%); Indexer Clustering (18%); Search Head Clustering (10%)
- Coverage evidence: guide sections 1–9, integrated scenarios, safe hands-on labs, original readiness checks, and explicit architecture, governance, performance and security boundaries where relevant
- Link evidence: 6 unique external guide URLs; 3 reachable, 3 automation-blocked, 0 missing/broken in dated source-health evidence
- Volatile boundaries: live certification status, blueprint revision, product behavior and terminology, course availability and exam logistics

The review maps every published objective group to applied evidence rather than memorized labels. Related items are explicitly separated from the blueprint contract, and commercial resources remain optional supplements. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `4fe612b351b9c761b9032259a223155b6e4e3c3773d9edd2fac17d5b0731ea73`.


+## SPLUNK-O11Y-METRICS-USER coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Get Metrics In with OpenTelemetry (10%); Metrics Concepts (15%); Monitor Using Built-in Content (10%); Introduction to Visualizing Metrics (15%); Introduction to Alerting on Metrics with Detectors (10%); Create Efficient Dashboards and Alerts (10%); Finding Insights Using Analytics (15%); Detectors for Common Use Cases (15%)
- Coverage evidence: guide sections 1–8, integrated scenarios, safe hands-on labs, original readiness checks, and explicit architecture, governance, performance and security boundaries where relevant
- Link evidence: 5 unique external guide URLs; 4 reachable, 1 automation-blocked, 0 missing/broken in dated source-health evidence
- Volatile boundaries: live certification status, blueprint revision, product behavior and terminology, course availability and exam logistics

The review maps every published objective group to applied evidence rather than memorized labels. Related items are explicitly separated from the blueprint contract, and commercial resources remain optional supplements. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `53592e027c6e076c752a7fdbda7be355bcc4cde7d02c379d87ff5bb0b85faa01`.


+## SPLK-5002 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Data Engineering (10%); Detection Engineering (40%); Building Effective Security Processes and Programs (20%); Automation and Efficiency (20%); Auditing and Reporting on Security Programs (10%)
- Coverage evidence: guide sections 1–5, integrated scenarios, safe hands-on labs, original readiness checks, and explicit architecture, governance, performance and security boundaries where relevant
- Link evidence: 7 unique external guide URLs; 5 reachable, 2 automation-blocked, 0 missing/broken in dated source-health evidence
- Volatile boundaries: live certification status, blueprint revision, product behavior and terminology, course availability and exam logistics

The review maps every published objective group to applied evidence rather than memorized labels. Related items are explicitly separated from the blueprint contract, and commercial resources remain optional supplements. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `8c0b091c2e53985d8ccfd27c19ff36fe4379d18e43fcdfb93c04a0847f18c751`.


+## SPLK-5003 coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Advanced Threat Intelligence and Analysis (5%); Security Data Management (20%); Advanced Incident Response and Management (10%); Advanced Automation and Orchestration (10%); Scaling Cybersecurity Defenses and DevSecOps (15%); Governance, Risk, and Compliance (10%); Measuring and Improving Security Program Effectiveness (15%); Security Capability Selection, Placement, Configuration (15%)
- Coverage evidence: guide sections 1–8, integrated scenarios, safe hands-on labs, original readiness checks, and explicit architecture, governance, program, evidence and capability-placement boundaries
- Link evidence: 14 unique external guide URLs; 11 reachable, 3 automation-blocked, 0 missing/broken in dated source-health evidence
- Volatile boundaries: publicly schedulable status after earlier beta messaging; blueprint revision; product and framework versions; course access and exam logistics

The review maps the architect blueprint through requirement-led designs, decision records, security-data and response architecture, safe automation, DevSecOps scale, governance and measurable program outcomes. The obsolete Lantern path was replaced with the working Security Use Cases collection. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `10121cd48a63fb12ca9073996c56aa52248a86bbcf124729f358798ba7331161`.


+## PANW-CYBERSECURITY-PRACTITIONER coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Cybersecurity (19%); Network Security (19%); Secure Access (14%); Cloud Security (20%); Endpoint Security (15%); Security Operations (13%)
- Coverage evidence: guide sections 1–6, integrated scenarios, authorized labs, original readiness checks, and explicit product, architecture, governance and security boundaries
- Link evidence: 14 unique external guide URLs; 13 reachable, 1 automation-blocked, 0 missing/broken in dated source-health evidence
- Volatile boundaries: live status, datasheet revision, product packaging, learning-path access and exam logistics

The review maps every published domain to applied evidence. The stale Cortex Cloud path was replaced with the live official product index, and related items remain separate from the objective contract. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `600eac4ecbdddea9b5ce0e0dba159accac70b13b677dbcfdeaa0e19926dcd34b`.


+## PANW-CLOUD-SECURITY-PROFESSIONAL coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Security Operations Center Fundamentals (10%); Cortex Fundamentals (15%); Cloud Posture Security (29%); Cloud Runtime Security (26%); Application Security (20%)
- Coverage evidence: guide sections 1–5, integrated scenarios, authorized labs, original checks, and explicit product, architecture, governance and security boundaries
- Link evidence: 12 unique external guide URLs; 11 reachable, 1 automation-blocked, 0 missing/broken in dated source-health evidence
- Volatile boundaries: live status, datasheet revision, Cortex Cloud packaging, learning access and exam logistics

The review maps every published domain to applied evidence. Reorganized Cortex Cloud documentation and the retired Microsoft Learn path were reconciled to current official surfaces. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `85d843c3d92c883b854add6b05c2bae20e18c18da44ce42d9f62ec7d9f8a89ae`.


+## PANW-NETWORK-SECURITY-PROFESSIONAL coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Network Security Fundamentals (17%); NGFW and SASE Solution Functionality (13%); Platform Solutions, Services, and Tools (30%); NGFW and SASE Solution Maintenance and Configuration (10%); Infrastructure Management and CDSS (17%); Connectivity and Security (13%)
- Coverage evidence: guide sections 1–6, integrated scenarios, authorized labs, original readiness checks, and explicit product, architecture, governance and security boundaries
- Link evidence: 12 unique external guide URLs; 12 reachable, 0 automation-blocked, 0 missing/broken in dated source-health evidence
- Volatile boundaries: live certification status, datasheet revision, product behavior, tenant access, learning-path availability and exam logistics

The review maps every published domain to applied evidence and keeps related items separate from the objective contract. No unverified practice product is presented as authoritative. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `682be74c10edf47fb23e61e21cb7544cf34fa962a9926b3b5265758bb66c6483`.


+## PANW-SECURITY-OPERATIONS-PROFESSIONAL coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Security Operations Fundamentals (25%); Threat Intelligence and Incident/Case Response (16%); Cortex XDR (23%); Cortex XSOAR (16%); Cortex XSIAM (20%)
- Coverage evidence: guide sections 1–5, integrated scenarios, authorized labs, original checks, and explicit product, operations, governance and security boundaries
- Link evidence: 12 unique external guide URLs; 11 reachable, 1 automation-blocked, 0 missing/broken in dated source-health evidence
- Volatile boundaries: live status, datasheet revision, Cortex packaging, tenant access, learning paths and exam logistics

The review maps every domain to applied evidence. The retired XSIAM path was replaced with the live Cortex documentation portal. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `4b118e221e1a6158afc9f749efc6e977b60f8e1a012f89efd5c512cdd2211acd`.


## PANW-NETWORK-SECURITY-ANALYST coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Object Configuration Creation and Application (30%); Policy Creation and Application (30%); Management and Operations (26%); Troubleshooting (14%)
- Coverage evidence: guide sections 1–4, integrated scenarios, authorized labs, original readiness checks, and explicit product, architecture, governance and security boundaries
- Link evidence: 10 unique external guide URLs; 10 reachable, 0 automation-blocked, 0 missing/broken in dated source-health evidence
- Volatile boundaries: live certification status, datasheet revision, product behavior and terminology, tenant access, learning availability and exam logistics

The review maps every published domain to applied evidence and keeps related items separate from the objective contract. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `10b40a968bc62f35505e71b5972b161cedebdc723bf0f12bd31a90942d657ece`.


## PANW-XSIAM-ANALYST coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Alerting and Detection Processes (19%); Incident Handling and Response (20%); Automation and Playbooks (15%); Data Analysis with XQL (14%); Endpoint Security Management (12%); Threat Intelligence Management and ASM (20%)
- Coverage evidence: guide sections 1–6, integrated scenarios, authorized labs, original readiness checks, and explicit product, architecture, governance and security boundaries
- Link evidence: 11 unique external guide URLs; 10 reachable, 1 automation-blocked, 0 missing/broken in dated source-health evidence
- Volatile boundaries: live certification status, datasheet revision, product behavior and terminology, tenant access, learning availability and exam logistics

The review maps every published domain to applied evidence and keeps related items separate from the objective contract. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `c1f175c79813c8b994e1a1d61270ef393a4162a9e9b0f674399d5b7969c80137`.


## PANW-XDR-ANALYST coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Alerting and Detection Processes (23%); Incident Handling and Response (34%); Data Analysis (28%); Endpoint Security Management (15%)
- Coverage evidence: guide sections 1–4, integrated scenarios, authorized labs, original readiness checks, and explicit product, architecture, governance and security boundaries
- Link evidence: 10 unique external guide URLs; 9 reachable, 1 automation-blocked, 0 missing/broken in dated source-health evidence
- Volatile boundaries: live certification status, datasheet revision, product behavior and terminology, tenant access, learning availability and exam logistics

The review maps every published domain to applied evidence and keeps related items separate from the objective contract. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `3c06e6862b0b7301795c65038b2313ba160aea3d244bef736cb252585ee42f44`.


## PANW-CLOUD-SECURITY-ENGINEER coverage record

- Reviewed: September 2, 2026
- Outcome: **sources + objectives checked; human review pending**
- Official scope: Planning and Installation (12%); Integration (16%); Posture Security (22%); Runtime Security (18%); Application Security (16%); Troubleshooting (16%)
- Coverage evidence: guide sections 1–6, integrated scenarios, authorized labs, original readiness checks, and explicit product, architecture, governance and security boundaries
- Link evidence: 26 unique external guide URLs; 25 reachable, 1 automation-blocked, 0 missing/broken in dated source-health evidence
- Volatile boundaries: live certification status, datasheet revision, product behavior and terminology, tenant access, learning availability and exam logistics

The review maps every published domain to applied evidence and keeps related items separate from the objective contract. No recalled/live item, answer dump or copied course content is used. Blueprint SHA-256: `8a226a5c7f86018cb4d6767ded061b772eeabe8c0bcff84e9fb4371970f8f0d1`.


## Revalidation triggers

A guide returns to **REVIEW REQUIRED** when its official objective or status snapshot changes. Source-health findings create review work but do not automatically rewrite or demote content because redirects, access controls, page-title changes, and provider metadata changes require human interpretation. A new source-validation record is required after the guide is reconciled with a changed blueprint.
