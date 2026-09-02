# Sources-and-objectives validation records

These records document an AI-assisted quality gate: objective coverage, citations, volatility labels, link evidence, and exam-integrity checks. They do **not** claim that an independent person has reviewed every explanation or technical judgment. A guide is labeled **Community reviewed** only after a complete contributor review is recorded separately.

The internal `source-validated` state powers the repository workflow. On the public site it is deliberately displayed as **Sources + objectives checked — human review pending**. The guide was checked against the current official objective snapshot, its material explanations have supporting public sources, volatile details are marked **VERIFY CURRENT**, repository and external links validate, and the content passes the project's exam-integrity policy.

The machine-readable evidence is in [`data/reviews.json`](https://github.com/cterpening/certification-study-library/blob/main/data/reviews.json). Repository validation recomputes blueprint hashes, exact source registration, and source-health counts so a stale review record fails the build. A separate human contributor review is still required before a guide can become **COMMUNITY REVIEWED**.

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

## Revalidation triggers

A guide returns to **REVIEW REQUIRED** when its official objective or status snapshot changes. Source-health findings create review work but do not automatically rewrite or demote content because redirects, access controls, page-title changes, and provider metadata changes require human interpretation. A new source-validation record is required after the guide is reconciled with a changed blueprint.
