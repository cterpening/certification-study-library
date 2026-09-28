# SC-500 deep review — September 28, 2026

The entire guide was reviewed against 87 objectives in twelve groups. It now includes seven original worked examples, ten proposed labs, and 48 answered checks. Local fixtures verify permission and coverage unions, event completeness, detection latency, recovery time, gateway outcomes, and catalog totals. No infrastructure, security plan, live agent, paid lesson, assessment, or destructive incident operation was executed. Independent human review remains pending.

## Scope and evidence

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-500) is unchanged. Its May 13, 2026 page-update date is not a separately published skills-effective date. Both canonical snapshots retain their hashes, and the historical September 1 review remains preserved. The current credential lists 120 minutes and ten languages. Its Practice Assessment remains unavailable; usual publication timing is not a promise.

The receipt `ADLC_Docs/operations/2026-09-28-sc-500-deep-review.json` records each objective hash/mapping, prior records, fetch evidence, source-reading boundaries, article decisions, local checks, and validation gates.

## Material changes

- **Key Vault defaults and network exceptions:** API version 2026-02-01 and later defaults newly created vaults to RBAC. Existing vaults do not migrate automatically. The [resource schema](https://learn.microsoft.com/en-us/azure/templates/microsoft.keyvault/vaults) explicitly retains trusted-service traffic when public access is disabled; that specific exception qualifies the network article’s broader private-only wording. The guide adds caller/bypass/DNS/authorization checks.
- **Agent policy scope:** The [Conditional Access reference](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id) distinguishes delegated users, application identities, and agent user accounts. Blueprint and all-users targeting do not establish agent-user coverage. API-key calls bypass this token-policy path.
- **AI protection coverage:** The [threat-protection overview](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection) scopes scanning to text tokens on supported Azure services/models, with commercial-cloud and trial-cap limits. [Agent-level posture](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture) requires Agent 365 licensing, unlike CSPM discovery of Foundry accounts/projects.
- **Operational evidence:** A plan switch does not prove healthy EDR or recent scan coverage. A destination row count does not prove complete unique-event delivery. Gateway client authentication does not grant the gateway backend access. Recovery includes provisioning and application validation, not just data transfer.
- **Sentinel and Copilot:** Lake onboarding affects CMK compatibility, regional workspace enrollment, query access, billing, and support-assisted offboarding. Copilot platform roles and Microsoft-plugin source roles remain distinct. The guide adds these preflight boundaries without claiming a live configuration was validated.
- **Source routing:** The old database introduction URL now covers open-source relational databases. The guide uses the multicloud plan matrix for broader database-plan selection and keeps engine/cloud-specific limits explicit.

The [Defender release notes](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes) support updates for individual recommendations, the CVE detail resource, AWS/GCP permission-use evidence, October 27 Foundational CSPM opt-in for new Azure subscriptions, December 14 recommendation removal, and August 16, 2027 classic SQL API retirement. The existing March 31, 2027 Sentinel portal and September 15, 2028 ADE dates remain qualified future transitions. Only the recorded release sections were reviewed, not the entire history or every sovereign-cloud lifecycle notice.

## Learning and article decisions

Twelve official Learn paths expose **63 module placements**: 3/4/6/4/3/4/9/7/6/6/8/3. Every displayed title/description and path overview was read, but linked units were not. Current runtimes are absent, so the old 30h08 total is withdrawn. The separate four-module Foundry protection path and six-unit Copilot Studio protection module were also inspected at overview level, outside that count. The instructor-led course remains four days and now lists ten languages.

Pluralsight’s legacy AZ-500 path contains six course entries totaling 46h27, including a 12h31 practice entry, plus five labs totaling 3h30: **49h57**, consistent with its rounded 50-hour header. The previous guide mistook the practice entry for the path duration. It remains supplemental infrastructure preparation for a retired exam.

Public indexed Udemy listings show Alan Rodrigues at 36h35, 11 sections/460 lectures, September 2026; John Christopher at 18h31, 17 sections/151 lectures, August 2026; and Duffy/Koenderink with four 25-question tests, August 2026. All three direct fetches were blocked. No paid content or question quality was reviewed. O’Reilly direct access was also blocked; its old AZ-500 runtime/date and the unwatched Savill video runtime are clearly historical/unverified. Partner and Reactor shells do not establish current SC-500 offerings.

Tim Warner’s public root/README identifies an MIT companion with a fifteen-lesson outline and active development. Individual lessons/scripts were not audited, and a current publisher catalog listing was not established. Its alignment and approximate video duration remain author claims.

[Microsoft’s September 25 Storm-3168 article](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/) was reviewed for its incident overview, uncertainty about initial compromise, and mitigation guidance. It supplies a defensive credential/scope/recovery tabletop. The guide does not claim the exposed credential was proven to be the initial entry path or reproduce destructive activity.

[Rob Lefferts’s September 23 SOC article](https://www.microsoft.com/en-us/security/blog/2026/09/23/reimagining-the-soc-for-the-agentic-era-in-microsoft-defender/) was read through the main announcement and retained as context for connecting signals to controlled response. ISOC is explicitly preview. The recording and whitepaper were not reviewed, and the announcement does not establish tenant entitlement or a new exam domain.

## Validation and follow-up

Thirty-nine local assertions passed across the original examples and catalog calculations. They model outcomes; they do not test actual IAM, ingestion, detection, restore throughput, or product enforcement. Repository, catalog, unit, and strict generated-site checks are recorded after passing.

Follow-ups are scheduled for October 26 (CSPM default, coverage, catalog/assessment), December 7 (recommendations), March 15, 2027 (Sentinel portal), July 19, 2027 (SQL APIs), and June 12, 2028 (ADE migration). Long product references were read only in recorded sections; complete feature/role/cloud matrices and linked procedures remain outside this review’s execution boundary.
