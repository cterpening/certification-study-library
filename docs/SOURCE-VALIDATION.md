# Source-validation records

Source validation is a documented quality gate, not a claim that a guide is error-free. A **SOURCE-VALIDATED** guide has been checked against the current official objective snapshot, its material explanations have supporting public sources, volatile details are marked **VERIFY CURRENT**, repository and external links validate, and the content passes the project's exam-integrity policy.

The machine-readable evidence is in [`data/reviews.json`](https://github.com/cterpening/certification-study-library/blob/main/data/reviews.json). Repository validation recomputes blueprint hashes, exact source registration, and source-health counts so a stale review record fails the build. A separate human contributor review is still required before a guide can become **COMMUNITY REVIEWED**.

## Current source-validated guides

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

Access-blocked course pages returned HTTP 403 to the automated client. An access-controlled response is recorded separately from a missing or failing page and does not establish that the resource is unavailable to a browser or subscriber.

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

The review retained the guide's architecture and production-operations depth while adding primary Microsoft citations at the decisions they support. It explicitly separates the durable platform concepts from volatile Foundry naming, project types, models, deployment types, role names, quotas, SDKs, analyzer modes, preview features, regions, and licensing. The official blueprint snapshot SHA-256 is `3fbf0ebd6b3d5e591d7354de47f8d87baaea121330a209e9104045447ac70f63`.

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

## Terraform Associate (004) coverage record

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

## Revalidation triggers

A guide returns to **REVIEW REQUIRED** when its official objective or status snapshot changes. Source-health findings create review work but do not automatically rewrite or demote content because redirects, access controls, page-title changes, and provider metadata changes require human interpretation. A new source-validation record is required after the guide is reconciled with a changed blueprint.
