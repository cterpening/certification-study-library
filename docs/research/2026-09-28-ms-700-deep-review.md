# MS-700 deep review — September 28, 2026

Read the whole guide and mapped all 97 detailed objectives in twelve groups from the published October 27 revision. Preserve the accepted July 29 objective/status snapshots until the change takes effect. Domain weights are unchanged. Credential metadata lists 100 minutes and seven languages; the course lists four days and English.

## Learning changes

Five worked examples cover directional bandwidth, policy precedence, distinct app audiences, callback timing and session-versus-participant rates. Add two labs (ten total) and eight answers (44 total). Update network tools/QoS, roles and workload boundaries, granular federation/shared-channel access, app migration/consent, room identity, VDI support, unified events/Copilot, voice funding and current telemetry behavior. All examples are synthetic; no tenant, device, network executable, call, flow or media lab was run.

## Source decisions

The [updated developer announcement](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/) provides the controlling connector retirement update. Older text remains on that page and the platform overview; readers must select the dated update rather than the original deadline. **Unresolved:** its private-channel support statement differs from the [platform overview](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/what-are-webhooks-and-connectors). Keep rollout instructions conditional on current cloud, identity, entry point and observed delivery; source reachability does not resolve the difference.

The [July Teams blog](https://techcommunity.microsoft.com/blog/microsoftteamsblog/what%E2%80%99s-new-in-microsoft-teams--july-2026/4542510) was read as main article text, with app-request and room-authentication exercises selected. The legacy Rooms authentication article does not establish a complete new passwordless migration procedure. Comments, embedded demos and unrelated device announcements were not used as authoritative implementation evidence.

Catalog comparison verified four Learn paths/20 modules, five Pluralsight course listings totaling 18h58, and MeasureUp’s 155-question public listing. Learn runtimes retained only as historical estimates; four O’Reilly/Udemy pages were blocked. Paid lessons/questions, course completeness, originality and interactive practice were not verified. Do not adopt vendor exam-duration or question-count claims over the credential page.

## Follow-up and validation

Schedule the October blueprint recheck, Windows VDI support/end-of-availability milestones, private-channel documentation reconciliation, and live-events grace-period check. Repository validation, unit tests, strict site build and generated-site validation must pass before publication; final results are in the operation record `ADLC_Docs/operations/2026-09-28-ms-700-deep-review.json`. The review is same-context AI work; independent human review remains pending.
