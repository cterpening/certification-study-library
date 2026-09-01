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

Access-blocked course pages returned HTTP 403 to the automated client. An access-controlled response is recorded separately from a missing or failing page and does not establish that the resource is unavailable to a browser or subscriber.

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

## Revalidation triggers

A guide returns to **REVIEW REQUIRED** when its official objective or status snapshot changes. Source-health findings create review work but do not automatically rewrite or demote content because redirects, access controls, page-title changes, and provider metadata changes require human interpretation. A new source-validation record is required after the guide is reconciled with a changed blueprint.
