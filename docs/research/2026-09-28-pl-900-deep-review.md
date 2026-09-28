# PL-900 deep review — September 28, 2026

The entire guide was reviewed against all 37 objectives in nine groups. It now includes six original worked examples, eight proposed labs, and 37 answered checks. Local validation covers 27 assertions for a delegation fixture, access unions, approval delivery counts, time savings, evaluation/adoption denominators, and course runtimes. No tenant, app, flow, pipeline, agent, paid lesson, or assessment was executed. Independent human review remains pending.

## Scope and corrections

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-900) still uses July 24, 2026. Both canonical objective and status snapshots are unchanged; the previous August review remains attached to the same objective bytes. The credential page lists a 45-minute assessment and twelve languages, with no retirement displayed.

The receipt `ADLC_Docs/operations/2026-09-28-pl-900-deep-review.json` contains the objective hashes and mappings, previous records, fetch evidence, reading boundaries, article decisions, and validation gates.

- **Knowledge access depends on the source.** [Uploaded-file documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/nlu-documents) explicitly makes that content available to users chatting with the agent irrespective of original file permissions. The guide corrects its universal permission-filtering implication and adds an audience/source exercise.
- **App-building experiences differ.** The [vibe overview](https://learn.microsoft.com/en-us/power-apps/vibe/overview) remains preview and includes environment, language, and region constraints. The transition banner and September announcement do not make all generation features GA. Ordinary code-app source control is distinct from Power Platform Git integration.
- **Connector policies have different modes and coverage.** [Advanced connector policies](https://learn.microsoft.com/en-us/power-platform/admin/advanced-connector-policies) use an allowlist; mixed mode enforces both policy systems and ACP-only ignores classic policies for the scope. Current custom, HTTP, and virtual connector exclusions matter. This is supporting governance depth, not an additional exam domain.
- **Small demonstrations can hide incorrect results.** A local filter over 2,000 of 2,500 rows can miss all 400 eligible records. A broader Dataverse grant remains effective when a narrower role is added. App sharing and connector allowance do not grant source-data rights.
- **Process lifetime differs from run lifetime.** [Long-running approvals](https://learn.microsoft.com/en-us/power-automate/modern-approvals) persist state and separate response handling. The example distinguishes 500 intended effects from 520 deliveries and explains why a non-atomic flow lookup cannot guarantee concurrency safety.
- **Deployment and evaluation need explicit evidence.** Pipelines do not move Dataverse business rows. An 82% aggregate evaluation can conceal 50% edge-case success. The current standard-harness scope, GCC/Fabric evaluation exclusions, one-way agent-flow conversion, and Agent 365 service boundary are visible.

## Article and learning decisions

[Ryan Cunningham’s September 10 app-building announcement](https://www.microsoft.com/en-us/copilot/blog/copilot-studio/build-apps-in-copilot-cowork-and-copilot-studio/) was read through its main article. It is useful for comparing surfaces and reviewing generated applications; Frontier and public-preview rollout distinctions are preserved. It does not establish tenant entitlement or exam scope.

Selected app-building and learning sections of the [September feature roundup](https://www.microsoft.com/en-us/power-platform/blog/power-apps/whats-new-in-power-platform-september-2026-feature-update/) were reviewed. Its large linked documentation digest was not exhaustively audited. The guide accepts plan-review exercises and discovery links, without extending an individual GA claim to other features. The linked Power CAT Power Series directory contains relevant cloud-flow, app, RPA, and governance exercises. Only the directory was inspected; individual labs were not validated.

The official course still lists one day and twelve languages. Its public overview emphasizes apps, flows, and Power Pages, and its fetched syllabus does not expose a complete module list. The guide therefore points learners back to the current blueprint for agent, code-app, and Plan-designer coverage.

Pluralsight lists eight courses totaling **536 minutes (8h56)**, dated 2024–2025. LinkedIn’s Craig Zacker course remains six hours, released March 17, 2025. MeasureUp lists 120 questions and an August 2025 update. These are supplemental resources with explicit July 2026 coverage gaps, not proof of current completeness.

Udemy’s public indexed listing shows Phillip Burton’s course updated September 2026 with 25 sections, 132 lectures, and 11h01; direct access was blocked and paid coverage was not checked. The O’Reilly listing could not be re-established, so its old runtime is labeled historical/unverified. Partner, Whizlabs, and assessment shells do not establish signed-in access or current syllabi. No paid or recalled-question content was accessed.

## Validation and follow-up

The local fixture and arithmetic checks passed; they do not test actual connector delegation, service authorization, or concurrent flow execution. Repository, learning-catalog, unit, and strict generated-site gates are recorded after passing. Long references were read in the sections recorded in the receipt; a successful fetch is not a claim that every linked procedure was audited.

An October 12 follow-up checks app-building surfaces, harness and policy coverage, and course gaps. PL-900 also joins the shared November 16 roadmap-transition follow-up. Tenant labs and independent human review remain outstanding.
