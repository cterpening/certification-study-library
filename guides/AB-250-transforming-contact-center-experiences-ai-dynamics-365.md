---
exam_code: AB-250
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-250
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: review-required
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# AB-250 Transforming Contact Center Experiences with AI in Dynamics 365 Study Guide

> **Independent AI-assisted resource — DEEP REVIEW COMPLETED; LIFECYCLE EVIDENCE GAP; HUMAN REVIEW PENDING.** This guide was checked against the official page last updated May 15, 2026 and cited public sources on September 28, 2026. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ab-250-coverage-record). The [official AB-250 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-250) is authoritative.

**Current baseline:** Official study guide last updated May 15, 2026; Microsoft publishes no separate skills-effective date.<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 28, 2026.<br>
**Lifecycle:** The [Dynamics 365 Contact Center AI Engineer Associate credential](https://learn.microsoft.com/en-us/credentials/certifications/d365-contact-center-ai-engineer-associate/) and 120-minute English exam are active. The credential page does not offer a Practice Assessment.<br>
**Transition:** Microsoft added AB-250 to partner skilling after MB-240 retired, but [explicitly says it is not a direct replacement](https://learn.microsoft.com/en-us/partner-center/announcements/2026-july).<br>
**Official source:** [AB-250 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-250)

### Current changes and evidence limits

The [September 28 deep review](../docs/research/2026-09-28-ab-250-deep-review.md) maps all **119 detailed objectives**. Their wording is unchanged; the old accepted snapshot used different heading, bullet and wrapping formats. This review adds six worked examples, ten labs and answers to 48 original checks. Only offline arithmetic/set checks were executed; tenant, telephony, campaign, agent, SDK and paid-course exercises remain unexecuted.

The [Contact Center migration plan](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/migrate-from-azure-communication-services) and [deprecation ledger](https://learn.microsoft.com/en-us/dynamics365/contact-center/implement/deprecations-contact-center) agree that affected ACS-dependent voice/messaging paths need migration before **September 30, 2028**. They conflict on new-customer phone-number acquisition/port-in restrictions: the plan says **September 30, 2026**, while the ledger says **September 23**. The [ACS retirement guide](https://learn.microsoft.com/en-us/azure/communication-services/acs-retirement-and-breaking-changes-guide) separately gives **October 23** for new retiring-service sign-ups and has phone-number-specific eligibility wording. Do not substitute that sign-up date for a phone-number cutoff or assume an existing resource without numbers qualifies. Current acquisition eligibility needs Microsoft confirmation; it is an unresolved source gap, not a tested tenant result.

Also track **September 30, 2026** removal of Apple Messages for Business configuration options and **October 30, 2026** removal of the older case/conversation and representative forecasting features. Their documented replacement is workforce engagement management (WEM) forecast scenarios. Existing ACS channels do not become unsupported merely because a deprecation notice is published.

## How to use this guide

For each interaction, trace:

1. customer intent, channel, authentication, consent, language and accessibility;
2. workstream, context/classification, queue, routing/assignment and capacity;
3. AI self-service, representative assistance or autonomous-agent responsibility;
4. knowledge, CRM/contact data, variables, tools and least-privilege identity;
5. escalation/transfer, transcript/recording, masking, retention and human accountability;
6. representative/supervisor workspace, productivity and operational recovery;
7. customer outcome, quality, service, cost, workforce and safety evidence.

Use a nonproduction environment and synthetic customers. Draw an end-to-end conversation sequence before configuring isolated features. Voice, telephony, digital providers, SDKs, agents, licensing, capacity, proactive engagement and workforce-management behavior change quickly; verify current first-party documentation and tenant availability.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Deploy Dynamics 365 Contact Center | 15–20% | Can you choose a deployment model and govern users, agents, environments, connectors and ALM? |
| Implement channels | 30–35% | Can you configure secure chat/digital/voice/proactive/WFM experiences and their advanced lifecycle? |
| Configure agents and AI capabilities | 10–15% | Can you ground representative assistance and build secure, compliant voice agents? |
| Configure work distribution | 10–15% | Can you classify, prioritize, queue and assign work with fallback and diagnostics? |
| Configure the representative experience | 15–20% | Can you tailor workspace, productivity, collaboration and knowledge by persona? |
| Manage analytics | 10–15% | Can supervisors act safely and can reporting/telemetry support improvement and diagnosis? |

---

## 1. Deploy Dynamics 365 Contact Center

### Choose the architecture and deployment mode

Dynamics 365 Contact Center is a CCaaS platform spanning voice and digital engagement, unified routing, representative/supervisor experiences, Copilot and agents, analytics and workforce capabilities. Start with service outcomes, current CRM/telephony, regions, scale, compliance, availability and total cost.

- **Standalone/full Dynamics deployment:** use Microsoft’s Dataverse-based service workspace and contact-center stack when the organization wants the integrated platform.
- **Embedded mode:** embed Contact Center capability in an existing CRM/representative experience when retaining that system is a requirement.
- **Third-party CCaaS plus Copilot:** connect supported third-party service/CRM context to Microsoft assistance capabilities when replacing the contact platform is not justified.

Connectors need a data contract, authentication/authorization, field mapping, latency, throttling, error/retry, observability and version ownership. Extending a connector does not excuse data minimization or least privilege. Test unavailable/slow external systems and reconcile actions that partially complete.

Evaluate total cost across licenses, telephony/PSTN, numbers, channel providers, messages/minutes, storage/recording, AI/agents, data integration, Power Platform capacity, analytics, implementation, support, workforce/change and compliance—not just per-user price.

The [any-CRM connector procedure](https://learn.microsoft.com/en-us/dynamics365/contact-center/extend/configure-custom-connector) synchronizes contacts/accounts into Dataverse using initial and incremental flows. Keep Power Apps and Power Automate in the same environment, preserve source CRM/ID/URL fields, paginate initial loads and reconcile create/update/delete events. A successful contact sync does not establish authorization for every customer record. The [embedded Salesforce procedure](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/set-up-embedded-experience) separately configures the conversation widget, call-center users and softphone layout; embedding a UI does not migrate the CRM or replace its access controls.

### Configure workspace, agents and operational helpers

Copilot Service workspace is the representative’s multi-session app. Configure it through profiles/templates rather than granting every persona every tool. The Agent hub supports discovery, rollout and management of service-oriented agents. Stage releases by environment, pilot cohort, supported intents, channel and autonomy.

Study the blueprint's feature names alongside the [current agent organization](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/overview-contact-center-agents): Customer Assist covers self-service/representative assistance, Quality Assurance covers conversation quality/coaching, and Service Operations covers setup and diagnostics. These are responsibility boundaries, not proof that every older feature name is an exact rename.

[Service Operations Agent](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/use-service-operations-agent) is English-only, requires the documented administrator roles, Dataverse/MCP connection and consumption billing; troubleshooting also needs Application Insights. It can manage supported queues/workstreams and unconditional route-to-queue rules. Custom assignment, classification/overflow rules, rule conditions and percentage-based multi-queue distribution require the dedicated admin experience. Review the exact proposed changes and resulting records; natural-language setup does not remove ALM or rollback requirements.

[Agentic simulation](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/configure-simulation-agent) is **preview, inbound voice only and English only**. It requires a provisioned simulation number and administrator roles. One organization runs one simulation at a time; a prompt requests up to five conversations, with at most two concurrent calls, up to five minutes per accepted call, and no DTMF. Use other controlled tests for digital, outbound, multilingual and keypad journeys. A simulation is an actual configured service workload with consumption, not a free offline mock.

The [rollout manager](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/create-rollout-plans) uses existing agent settings. Deactivating/deleting a plan **does not disable Customer Intent or Customer Knowledge Management settings**; Case Management rules have different behavior and are deactivated/deleted with the plan. A rollback checklist must inspect each underlying feature, not just the plan status.

> **Related item:** “Agent” is overloaded: the product may mean an AI agent, while older contact-center language uses agent for a human representative. This guide uses **representative** for the human and **agent** for AI unless quoting a feature name.

### Apply ALM and environment governance

Create solutions for configuration and custom components. Use development/test/production environments, publishers, environment variables, connection references and automated validation. Inventory dependencies such as workstreams, queues, channels, skills, templates, agents and knowledge. Some environment-specific or telephony setup may require controlled post-deployment configuration; document it rather than making ad hoc production changes.

Back up/export supported configuration, test deployment order, validate secrets/connections and define rollback or disable procedures. Agents, prompts, topics, tools and knowledge changes require versioned review like other production behavior.

Operating-hour calendars have a specific ALM exception: the [current procedure](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/create-operating-hours) says the Calendar entity cannot migrate through its export/import options, so recreate and verify the target hours/time zone/holidays. Phone-number/environment bindings also require a telephony-specific migration plan.

### Manage users, security and capacity

Provision identities, licenses and roles for administrators, supervisors and representatives. Security roles govern Dataverse/app privileges; custom roles should start from actual job needs. Capacity profiles express how much concurrent work a representative can take, often by channel/work type. Coordinate presence, capacity, assignment and operating hours so routing reflects real availability.

[Capacity profiles](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/capacity-profiles) are assignment constraints, not staffing forecasts. Users need bookable-resource configuration. A workstream profile plus a classification-appended profile requires capacity in **both**, consuming both on assignment. Reset frequency cannot be edited after creation; end-of-day reset can admit new work next shift despite earlier open conversations. Conversation capacity normally releases after ending the conversation **and closing its session**; record/activity routing has different release rules.

Custom user limits affect new assignments without evicting existing work; changes can take up to 15 minutes to synchronize. Manual/forced assignment can produce negative capacity. Assignment blocking can stop other automatic work and set Busy-DND. Do not diagnose these effects as a broken queue solely because one profile still shows room.

### Worked example 1 — Capacity is an intersection

A synthetic representative has total daily capacity 6, high-priority capacity 2 and normal capacity 5. After two high-priority and three normal cases, total remaining is **1**, high-priority remaining **0**, and normal remaining **2**. Another high-priority case is ineligible; only **one** additional normal case fits both constraints. This models profile arithmetic, not every presence/skill/assignment condition. Lowering a custom limit below current usage does not move the existing cases.

Use service identities for integrations and tools; do not share personal accounts. Separate administration, content/knowledge ownership, routing operations, quality review and analytics access where duties require it. Test access with each persona and verify that transcripts, recordings, knowledge and customer fields are appropriately restricted.

### Worked example 2 — Simulation scope and a rough budget

For five synthetic three-minute conversations, two concurrent slots require at least three waves: **9 minutes** if every call lasts three minutes and there is no setup delay. Aggregate conversation time is still **15 minutes**. The documentation gives approximately 40 credits for a three-minute simulation; inspect the actual billing unit and recorded consumption before extrapolating to a multi-conversation run. The example measures neither a run nor a bill. An English voice simulation does not validate Spanish, DTMF or SMS behavior.


---

## 2. Implement channels

### Configure chat and digital engagement

A channel moves interactions into a workstream; the workstream determines context, classification, routing and behavior. Configure chat, record-based and supported digital channels (such as SMS or social/messaging providers) only after provider, identity, consent, retention and regional requirements are understood.

For a web chat widget define branding, domain placement, pre-chat survey, context variables, authentication, availability/off-hours, file attachment, proactive invitation and escalation. Authentication can connect a conversation to a known customer; unauthenticated chat requires cautious identity claims. Never trust hidden/client-supplied context without validation.

Use the Live Chat SDK for supported web customization, the Messaging SDK for native mobile integration and messaging APIs for a custom channel. SDK/API work needs versioning, error/reconnect behavior, accessibility, secure tokens, telemetry and a support owner. A custom channel still feeds unified routing and should preserve conversation context.

[Authenticated chat](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/create-chat-auth-settings) requires a token-provider function, trusted public-key endpoint and authentication record attached to the channel. Keep token creation/signing server-side, align context-variable names with the workstream and check the representative's authenticated indicator. A claimed customer ID in an unauthenticated pre-chat field is not verified identity. Test invalid/expired tokens and ambiguous contact matching. The same page still mentions Apple Messages for Business; check its separate deprecation before planning new onboarding.

Real-time translation can help multilingual service but may alter meaning, names, policy and sensitive details. Show language state, preserve original text where required and provide a human/interpreter escalation for high-risk cases.

### Provision voice

Separate the two documented telephony paths:

| Path | Provisioning and lifecycle |
|---|---|
| Existing ACS Direct Offer/Direct Routing | Native voice documentation describes an ACS resource linked to the environment; assess carrier, numbers, workstreams and eventual migration |
| Teams Phone extensibility | Teams Calling Plan service numbers, Operator Connect or Teams Direct Routing; resource account and licensing per service number, sync into Contact Center and attach the voice workstream |

The [Teams Phone procedure](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/configure-teams-phone-in-voice-channel) is a supported integration with its own roles, delegated permissions, resource-account association and synchronization. The older [voice FAQ](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/voice-channel-faqs) blanket statement about native Teams numbers does not describe this dedicated integration. Follow the selected path's current procedure rather than treating the two setups as interchangeable.

For [ACS connections](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/voice-channel-acs-resource), map one application instance to one ACS resource; purchased numbers linked to an environment are not ordinary solution components transferable to another environment. For [ACS-to-Teams Direct Routing migration](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/migrate-azure-communication-services-direct-routing-to-teams-direct-routing), an SBC FQDN cannot be assigned to both simultaneously. Coexistence needs a different name/alias and appropriate certificate coverage; reusing the name requires a cutover/propagation plan. Pilot inbound/outbound, consult/transfer, caller ID, routing and emergency-location behavior before retiring old routes.

The [deployment guidance](https://learn.microsoft.com/en-us/dynamics365/guidance/resources/contact-center-deploy-voice-channel-best-practices) distinguishes carrier/SBC responsibility and metadata preservation. PSTN handoffs can strip SIP context. An external IVR integration needs an explicit call-state, context and failure contract. The [installation page](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/voice-channel-install) documents a two-hour maximum call duration; design recovery/callback behavior without assuming unlimited calls.

Configure recording and transcription only with a legal basis, notice/consent, retention, access, encryption and redaction policy. Real-time translation and AI analysis add data flows to document. Outbound caller ID, emergency/regulatory behavior and number ownership are operational concerns.

The CCaaS SDK/API can support voice integration/custom experiences. Test call setup, hold, consult, transfer, disconnect, failover, latency, duplicate events and correlation. Voice quality, network readiness and carrier dependencies are as important as application configuration.

### Configure conversation lifecycle features

Context variables carry information used for display, classification, routing or handoff. Name/type/validate them and avoid sensitive values unless required and protected. Automatic customer identification needs strong matching and ambiguity behavior; a false match can disclose another customer’s data.

Configure automatic closure, consult/transfer, custom presence, active conversation settings, quick replies and message templates. Automated/outbound messages need owner, localization, approval and stop behavior. Mask sensitive data in displayed/stored content where supported; masking is not a substitute for avoiding collection.

The timeline presents related activities; custom connectors can surface external events when their identity, authorization and error behavior are governed. Channel Integration Framework supports third-party telephony/widgets in model-driven apps; distinguish it from native voice provisioning.

Manage attachments by type/size/malware scanning/storage/retention. Configure feedback through Copilot Studio with clear survey triggers and avoid biasing the response. Conversation management must cover state, assignment, escalation, wrap-up and closure.

### Distinguish message masking, voice masking and recording controls

[Message masking](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/data-masking-settings) uses active regex rules, with a maximum of ten including built-ins, for chat/asynchronous messages. Customer-to-representative masking covers both views in live chat but only the representative UI for asynchronous channels; representative-to-customer masking has its own scope. Test the sender, recipient and transcript path separately.

[Voice-agent sensitive variables](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/agent-sensitive-data-masking) pause supported recording/transcription sections and insert silence in the recording. The procedure warns that the **first answer can escape redaction**, unexpected sensitive input in unflagged variables is not covered, and pause latency matters. Explicit Dataverse writes, transfer payloads, generative-AI inputs and custom telemetry do not inherit blanket protection. Leave sensitive activity logging disabled and verify destination handling independently. This is different from claiming the whole digital conversation is masked.

The [recording/transcription API](https://learn.microsoft.com/en-us/dynamics365/contact-center/extend/api/record-transcription-api) exposes separate operations and completion events. Treat a requested pause and an acknowledged pause as distinct states; avoid soliciting sensitive values before the relevant controls are effective. No API or call was exercised here.

### Configure proactive outbound engagement

Proactive chat initiates an invitation based on configured conditions; proactive campaigns can create outbound voice/SMS work from an audience, trigger and workstream. Define AI-led versus representative-led engagement, dialing mode, routing, outcomes, retries, frequency caps, quiet hours, suppression/opt-out and compliance. The dashboard should expose delivery, contact, outcome, abandonment/failure and complaint signals.

Use the [current proactive-engagement procedure](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/configure-proactive-engagement) to distinguish Copilot, preview, progressive and predictive modes. Preview accepts a representative before dialing; timer/manual delayed-start options require Teams Phone extensibility, while ACS starts automatically after acceptance. Customer identity uses the configured unique attribute for contact upsert; validate external IDs before loading a list.

Queue/skill eligibility, engagement priority, call order, frequency caps, quiet hours and suppression are separate controls. A higher-priority engagement can take work ahead of another using the same representatives. Missing/invalid custom priority falls back to FIFO. Supply contact time zones explicitly: the service does not infer them, and missing local time zones fall back to **UTC**. Upload can start processing immediately; the CSV itself is not retained for download. Cancellation policies affect **queued calls**, not calls already in progress. SMS fallback after retry exhaustion is preview.

The procedure specifically identifies a TCPA compliance limitation for representative-led progressive/predictive call-connection timing. Treat that as a documented deployment constraint requiring the organization's telecommunications review; a product switch does not establish permission to call customers.

### Worked example 3 — Missing time zone changes quiet-hour decisions

Assume synthetic quiet hours of 20:00–08:00 and a customer at UTC−04:00 on the example date. At **10:00 UTC**, their local clock is **06:00**, inside quiet hours. If the time-zone attribute is missing, evaluating the same configured hours at UTC sees **10:00**, outside quiet hours. A missing field can change eligibility. This is fixed-offset arithmetic, not a test of the provider's scheduler; also validate DST, consent, opt-out and retry behavior in the real implementation.

### Configure workforce management

WFM forecasts contact volume and workload, converts it to staffing requirements, creates shifts/schedules and tracks alignment/adherence. Inputs include historical interaction volume, handle time, channel, interval, seasonality and service target. Bad data or structural change produces bad forecasts.

Configure shift management, representative availability/skills, rules and schedule publication. Balance service levels, fairness, labor requirements, preferences and cost. Third-party WFM integration needs data freshness, identity, schedule/forecast ownership, conflict handling and reconciliation.

The [WEM forecast-scenario procedure](https://learn.microsoft.com/en-us/dynamics365/contact-center/use/workforce-management-forecast-scenarios) supports short-term intraday forecasts up to **42 days** and long-term daily forecasts up to **1,095 days**. Select data, channel/queue, time zone and seasonality. A planning group makes its time zone/channel/queue authoritative and read-only in the scenario. External data does not support automatic refresh; a saved scenario does not run immediately. Check job history and output snapshots. Forecast type, interval, entity and data source cannot be changed after creation; a scenario used by a capacity plan cannot simply be deleted.

### Worked example 4 — Workload arithmetic is only a staffing starting point

A synthetic hour has 120 contacts at 6 minutes average handling time: **720 workload minutes**, or **12 occupied seats**. At 85% target occupancy and 25% shrinkage, `ceil(12 / 0.85 / 0.75)` gives **19 scheduled seats**. This arithmetic excludes queueing/service-level models, arrival variability, skill mix, concurrency and absence correlation. It is not a forecast-engine result or a promise that 19 people meet a service target. Compare forecast versus actual volume/AHT before publishing schedules.

The [WEM MCP catalog](https://learn.microsoft.com/en-us/dynamics365/customer-service/develop/workforce-mcp-tools-overview-service-agent) has three documented tools: list requests, get details and decide pending **time-off** requests. Supervisors see their authorized planning group; representatives see their own records. Decisions require reviewer permission, record reviewer/time, require a rejection reason and do not overwrite an already decided request. Listing shift swaps/bids does **not** provide a tool to approve them. Future schedule, leave-balance and clock-in/out ideas in the blog are not current tool guarantees.

> **Related item:** Routing optimizes the next work assignment; WFM plans future capacity. A perfect routing rule cannot compensate for systemic understaffing.

---

## 3. Configure agents and AI capabilities

### Configure Copilot-assisted guidance

Copilot summaries and “Ask a question” should use approved, current case/conversation/knowledge context. Configure knowledge sources and filters so answers respect language, audience, lifecycle and permissions. Representatives must verify material policy, customer and action details.

Prompt plugins and tools extend Copilot. Define input/output schemas, authentication, authorization, allowed records/actions, timeout/retry, logging and human confirmation. Treat conversation/customer text as untrusted; prompt injection must not authorize data access or tools.

Copilot analytics can show usage and outcome signals. Interpret alongside quality, acceptance/correction, handle time, first-contact resolution, escalation and satisfaction; raw invocation does not prove value. A smart assist bot surfaces contextual suggestions in the representative workflow; keep its triggers, sources and ownership clear.

### Configure voice agents

An IVR collects intent/input and routes or resolves. Classic orchestration uses explicit topics/branches and is predictable; generative orchestration selects actions/topics more flexibly and requires stronger evaluation/guardrails. Use DTMF where keypad input is necessary, NLU for supported intent/entity recognition and speech for conversational interaction.

Copilot Studio variables preserve state such as customer choice or authenticated identifier; validate type, scope and lifetime. Voice triggers start supported conversational paths. SIP headers can pass routing/context metadata during transfer, but never trust or expose them casually. The Real-time Speech agent supports low-latency voice experiences; test interruption, noise, accents, latency, recognition and safe fallback.

Compliant recording requires current Copilot Studio/channel configuration plus organizational legal/retention controls. Secure the voice channel with verified identities, least-privilege tools, protected secrets/data and explicit transfer/escalation. Multilingual agents need per-language prompts, voices, knowledge, compliance messages and evaluation—not machine translation alone.

The [current real-time-agent overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/voice-realtime-voice-agents) separates speech-to-speech models from a text-LLM voice pipeline and labels digital messaging preview. Model/region choices affect processing geography; data storage geography does not by itself prove local inference. Digital preview does not support OAuth/Microsoft agent authentication and escalates conversations beyond 60 minutes. That limitation is separate from authenticating the surrounding chat channel. Do not use an unauthenticated agent as proof of permission for account-changing tools. Text-LLM voice transcripts can omit turns/responses, affecting monitoring evidence.

The [transparency note](https://learn.microsoft.com/en-us/dynamics365/contact-center/implement/transparency-note-real-time-voice-agents) documents that switching a real-time voice configuration back to classic requires a new agent, and that strict sensitive-audio masking and multilingual behavior have limits. Test barge-in, noise, tool failures, hallucinated commitments and deterministic escalation. Product DTMF support does not mean the simulation feature supports DTMF.

> **Related item:** A voice agent has less time for a user to inspect output than text chat. Latency, barge-in, confirmation, ambiguity and safe transfer are core safety/usability controls.

---

## 4. Configure work distribution

### Design queues and capacity behavior

Queues group work and eligible representatives. Define channel/type, membership, priority, operating hours, capacity and service target. Configure overflow to another queue or destination and fallback for unclassified/unassignable work. Avoid silent backlog.

Assignment methods may push work based on availability/capacity or allow selection depending on supported configuration. Queue priority affects relative order; classification/routing rules determine destination. Test fairness, starvation, aging, reconnect and representatives becoming unavailable mid-assignment.

The [queue procedure](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/queues-omnichannel) limits selection/transfer to compatible messaging, record or voice queues. **Lower numeric priority means higher queue priority**. Highest capacity, advanced round robin and least active still depend on eligibility; queue membership alone is insufficient. No configured operating hours means 24-hour availability.

[Prequeue overflow](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/manage-overflow) runs once before entry; a transfer to another queue does not repeat that same prequeue check. Classification/routing errors or no matching rule send work to fallback **without applying fallback overflow settings**. Adding hours defaults the out-of-hours action to “assign anyway”; review the action explicitly. Queue-count checks can use values cached for ten seconds, so a configured limit is not an atomic hard cap.

Postqueue wait handling and conversation-orchestration playbooks have different evaluation points. Wait-time overflow can run again in the destination queue; current playbook conditions can monitor changing availability/hours continuously. Direct-inward-dial overflow playbooks are preview. Document which engine applies before diagnosing a seeming contradiction.

### Build basic and unified routing

A workstream defines the channel/record intake and common distribution behavior. Classification rules derive attributes such as intent, language, priority or skills from context. Route-to-queue rules choose a queue; assignment finds the representative.

- **Skills-based routing:** matches explicit required skills and proficiency to representatives.
- **AI-enabled skills matching:** uses supported AI to infer/assist skill identification; validate inferred matches.
- **Intent-based routing:** uses detected intent to direct work.
- **Preferred representative routing:** favors continuity with a known representative when availability/policy allows.
- **Record routing/basic rule sets:** route non-conversation Dataverse work or simpler scenarios.
- **Engagement agent:** supports configured engagement behavior; define its place in the workstream and handoff.

[Route-to-queue rules](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/configure-route-to-queue-rules) run after classification, with one ruleset per workstream. Default **hit-all** evaluates matching queues and overflow to choose a suitable destination; **hit-first** honors the first match regardless of its overflow state. Percentage allocation supports up to five queues totaling 100%, but overflow can change the final destination and small samples need not match the exact percentages.

[Customer Intent Agent](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/manage-customer-intent-agent) uses lines of business to scope intents, user groups, workstreams and queues. Configure the chat workstream in its line-of-business rule; otherwise the chat and workstream can belong to different business scopes. Review discovered intents, knowledge associations and self-service eligibility before use. A suggestion is not a guaranteed correct route or an authorized action.

Order and stop-processing behavior matter. Design deterministic fallback when no rule or representative matches. Conversation diagnostics should show classification, routing, queue and assignment evidence. Correlate diagnostics with workstream/queue/user/presence/capacity configuration before changing rules.

---

## 5. Configure the representative experience

### Tailor profiles, sessions and inbox

Experience profiles assign workspace behavior to personas. Configure channels, productivity pane, Copilot features, inbox and templates to match role. Application tab templates define what opens within a session; session templates define the workspace session structure/context; notification templates control incoming-work prompts.

The inbox centralizes assigned/personal work. Create views with useful filters and permissions. Test multiple sessions, reconnect, notification acceptance/decline, tab context, wrap-up and accessibility. More panels/tabs can reduce productivity rather than improve it.

### Configure productivity tools

Scripts guide representatives through consistent steps; slugs insert dynamic context. Macros automate repeated UI/actions. Validate variables, permissions, idempotency and failure messaging. Custom productivity panels embed focused tools; Teams collaboration supports expert consultation while preserving customer-data policy.

The app profile manager JavaScript API extends productivity-panel/profile behavior; the Omnichannel JavaScript API interacts with supported conversation events/actions. Custom code needs supported API versions, error handling, security review, performance testing and ALM. Do not use unsupported DOM automation.

### Govern knowledge

Configure knowledge settings, tables, article lifecycle, categories, versions, translations and internal search. External sources require indexing/connectors, authentication, freshness, permissions and source attribution. Portal integration publishes only approved content to the intended audience.

[Customer Knowledge Management Agent](https://learn.microsoft.com/en-us/dynamics365/customer-service/administer/admin-km-agent) compares resolved-case/closed-conversation content with the internal Dynamics knowledge base and can create articles under configured rules. Connections, flows and the published agent are distinct readiness checks. Control mapped source attributes, real-time versus historical harvesting, and custom-table preview support. Internal knowledge access for this feature does not imply that every external source used elsewhere by Copilot is supported. Preserve author/reviewer/publisher accountability; review generated content before exposing it to an audience. Measure search success, article use, deflection, representative correction, stale results and customer outcomes.

---

## 6. Manage analytics

### Configure supervisors and quality

Supervisors need access to real-time/historical dashboards and actions such as monitoring, consult/intervention or assignment where supported. Configure roles and privacy boundaries; live monitoring and recordings are sensitive employee/customer data.

The Quality Evaluation agent can evaluate interactions at scale against configured criteria. Define sampling, rubric, calibration, human appeal/review, representative transparency and bias monitoring. Microsoft explicitly says this feature is not intended for employment decisions, including compensation or other entitlements; human review does not remove that product-use boundary. Configure the supervisor app and settings around operational personas.

[Quality Evaluation settings](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/manage-quality-evaluation-agent) separate Quality Administrator, Quality Manager and Quality Evaluator privileges. Validate connection references, enabled flows, published agent, credits and required environment settings. Cases, conversations and preview email evaluation are distinct record types. **Criteria scoring cannot be disabled after being enabled**; review that decision before configuration. Corrected answers can regenerate a summary when the corresponding setting is enabled.

[Quality and coaching](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/configure-quality-coach) separately uses quality indicators, guardrails and evaluation plans. Indicators contribute numeric scores; guardrails report prioritized violations. Plans choose conditions, sampling and either real-time actions/nudges or on-close scoring weights. Activate criteria and plans explicitly. A nudge or high aggregate score is not evidence that a prohibited action was blocked.

### Worked example 5 — Sampling and quality use different denominators

An exercise plan evaluates 25% of 800 queue-A conversations and 50% of 200 queue-B conversations: **200 + 100 = 300 of 1,000**, or **30% overall**, not the simple average 37.5%. For a separate synthetic score, indicators 95 and 65 weighted 60%/40% produce **83**. A critical guardrail violation remains a separate finding; do not average it away. These calculations illustrate planned sample sizes and weights, not guaranteed random-sample counts or an executed quality evaluation.

### Customize reports and telemetry

Built-in analytics answer common real-time/historical questions. Use the embedded Power BI editor for supported KPI/report customization and embed approved reports in Copilot Service workspace. Use Power BI/Desktop extension when a governed model needs additional data or calculations; preserve row-level security, refresh, semantic definitions and performance.

Application Insights conversation diagnostics/telemetry help trace lifecycle events and failures. Configure the connection, correlation, retention, sampling and access; avoid logging secrets or unnecessary personal content. Embed operational analytics only after defining which metric triggers which action.

The [Diagnose dashboard](https://learn.microsoft.com/en-us/dynamics365/contact-center/use/diagnose-dashboard) supports out-of-box assignment methods and presence/capacity/skill checks; transfer/consult diagnostics are not supported there. Initial complete synchronization can take about 24 hours and the out-of-box Application Insights tab can lag up to 15 minutes. Use conversation IDs and event-time configuration rather than a representative's current presence. “No eligible representative” and “representative rejected” can both count the same conversation.

### Worked example 6 — Overlapping diagnostics and correct containment

Suppose 50 conversations have a no-eligible-representative event and 30 have a rejection, with 20 in both sets. The union is **60 conversations**, not 80. Separately, of 100 AI-handled starts, 70 avoid human escalation but only 56 of those pass an outcome audit. Apparent containment is **70%**, verified correct containment **56% of starts**, and audited correctness among the contained cases **80%**. State the denominator and measurement window before comparing dashboards.

Distinguish service metrics (wait, abandonment, answer/service level), efficiency (handle/wrap time, occupancy), quality/outcome (resolution, transfer, repeat contact, satisfaction), AI performance (containment with correct outcome, escalation, groundedness, unsafe action), workforce (forecast error, adherence) and platform health (latency, failures). Optimizing one metric can harm another.

---

## Integrated scenarios

### Scenario 1: authenticated digital self-service

Embed an authenticated chat widget, pass validated context, route by language/intent and ground an agent in approved knowledge. The agent handles bounded requests and transfers with transcript/context when uncertain or when an action needs a representative. Mask sensitive fields, restrict attachments/tools and monitor correct resolution, escalation, wait, unsafe output and satisfaction.

### Scenario 2: regulated multilingual voice

Provision voice and numbers, configure consent-compliant recording/transcription, a multilingual voice agent with DTMF fallback and skills-based human transfer. Preserve original transcript/audio according to policy, use SIP/context carefully and provide interpreter/escalation paths. Test latency, noise, accents, ambiguous identity and emergency/high-risk requests.

### Scenario 3: proactive service campaign and staffing

Forecast demand, schedule skills and configure a representative-led outbound campaign with audience consent, frequency/reattempt caps and quiet hours. Route responses through a workstream with overflow. Supervisors monitor outcome/abandonment/complaint and quality; Power BI and Application Insights separate business result from technical failure.

---

## Hands-on labs

1. **Architecture/ALM:** Compare standalone, embedded and third-party CCaaS patterns; produce environment, connector, solution, identity, cost and rollback decisions.
2. **Digital channel:** Design a chat/digital workstream with widget, survey, authentication, context, translation, attachment, masking and mobile/custom-channel boundaries.
3. **Voice/IVR:** Draw telephony, number, workstream, queue, recording/transcription, IVR/voice-agent, transfer and failure paths.
4. **Routing:** Configure or model classification, skills/intent, queue priority, operating hours, capacity, overflow/fallback and diagnostics for ten cases.
5. **AI assistance:** Define knowledge, summaries, Ask a question, plugin/tool, smart assist and analytics tests including injection and permission failures.
6. **Representative/knowledge:** Create an experience profile, app/session/notification templates, inbox view, script/macro and knowledge lifecycle.
7. **Supervisor/analytics:** Define permissions, Quality Evaluation rubric/appeal, KPIs, Power BI extension and Application Insights correlation/retention.
8. **Operations:** Create WFM forecast/schedule, proactive campaign, agent/channel dashboards and incident runbooks with scale/stop thresholds.

9. **Migration and support evidence:** Inventory synthetic voice/SMS/WhatsApp paths, existing resources/numbers, CRM dependencies and target providers. Compare the September 23/30 phone-acquisition claims separately from October service sign-up wording. Design a pilot and rollback with SBC-name/certificate, sync, routing, caller-ID and retention checks. Do not execute a cutover or release a number as part of this worksheet.
10. **Scope and failure matrix:** For each agent/feature, record channel, language, auth, region, lifecycle, billing, test method and unsupported cases. Include simulation versus DTMF, first-answer redaction, async masking direction, rollout deactivation, quality-score enablement, queued versus active campaign cancellation and WEM request types. Run only explicitly provisioned sandbox steps; keep unexecuted cases visible.

The six worked examples are offline models. No calls, messages, campaigns, credits, tenant settings, migration commands, simulations or workforce decisions were performed for this review.

## Knowledge checks

1. When does standalone differ from embedded Contact Center mode?
2. What must a CRM/CCaaS connector contract define?
3. How do simulation and Health Agent support safer operations?
4. Which Contact Center artifacts require solution/ALM planning?
5. How do roles, personas and capacity profiles differ?
6. What connects a channel interaction to unified routing?
7. Which controls make a chat widget safe to embed?
8. When do Live Chat SDK, Messaging SDK and messaging APIs apply?
9. Why can automatic customer identification be risky?
10. Which components are required to provision voice?
11. What must recording/transcription governance define?
12. When does Channel Integration Framework fit?
13. What should context variables contain and how are they trusted?
14. Which settings govern attachments and sensitive-data masking?
15. What controls a compliant proactive outbound campaign?
16. How do dial mode and available representatives affect customer experience?
17. Distinguish WFM forecasting, scheduling and adherence.
18. What is the boundary between routing and workforce planning?
19. What sources should ground Copilot summaries and answers?
20. Which controls are required for prompt plugins/tools?
21. Compare classic and generative voice orchestration.
22. When do DTMF, NLU and speech input each fit?
23. What must be tested for a Real-time Speech agent?
24. Why does multilingual voice require more than translation?
25. How do priority, overflow and fallback differ?
26. Trace classification, route-to-queue and assignment.
27. Compare explicit, AI-enabled, intent and preferred-representative routing.
28. What evidence does conversation diagnostics provide?
29. Distinguish experience, app-tab, session and notification templates.
30. How do scripts, slugs and macros work together?
31. What engineering obligations accompany JavaScript API extensions?
32. How is external knowledge governed differently from internal articles?
33. What controls make a Quality Evaluation agent defensible?
34. When use built-in, embedded-editor or Power BI Desktop reporting?
35. What should Application Insights log—and avoid logging?
36. Which balanced metrics justify scaling an AI-enabled contact-center change?

37. Why does deprecating ACS messaging not mean existing channels stop immediately?
38. Which phone-acquisition date remains unresolved, and why is the service sign-up date different?
39. Why does deleting a rollout plan fail to disable some agents?
40. Which journeys does agentic simulation fail to cover?
41. Why can a representative with spare normal capacity be ineligible for priority work?
42. Why might fallback work enter a queue that has overflow rules?
43. Why can a missing time zone change outbound eligibility?
44. What does a voice sensitive-variable flag fail to protect automatically?
45. Why does a real-time-agent transcript not prove complete conversational coverage?
46. Which quality setting requires a deliberate irreversible decision?
47. Can a WEM tool approve a shift swap simply because it can list it?
48. Why do no-eligible and rejected counts need deduplication?

## Answers and reasoning

1. Standalone uses the service workspace and platform; embedded puts conversation capability inside the retained CRM. Compare data ownership, identity, integration and user experience rather than assuming the CRM is migrated.
2. Source IDs, mapped fields, authorization, initial/incremental sync, deletes, pagination, latency, throttling, retries, reconciliation and an owner.
3. Simulation exercises supported configured inbound voice journeys; operational diagnostics helps inspect configuration and telemetry. Neither replaces unsupported-channel, language, security or live-environment tests.
4. Solutions, environment variables, connection references, workstreams, queues, templates, tools, agent behavior and dependencies. Calendars and phone numbers have separate documented migration limitations.
5. Roles grant privileges, personas shape the experience, and capacity profiles constrain assignment. A role or persona does not supply available capacity.
6. Its channel/workstream supplies context to classification, route-to-queue and assignment stages.
7. Trusted deployment domain, valid authentication, scoped context, safe attachments, availability, notices, accessible UI and tested failure/escalation behavior.
8. Live Chat SDK customizes supported web chat; Messaging SDK supports native mobile; messaging APIs implement custom channel integrations. Each still needs an identity, lifecycle and routing contract.
9. Similar names or untrusted identifiers can attach a conversation to the wrong customer. Validate identity, handle ambiguity and restrict disclosed records.
10. A selected ACS or Teams Phone extensibility path, eligible/licensed numbers/resources, configured voice channel, workstream, queues, inbound/outbound profiles and tested routing. Teams needs its resource-account/sync configuration.
11. Organizational consent/notice policy, supported controls, retention, access and destination handling. Recording and transcription states, sensitive-variable timing and telemetry need separate verification.
12. For supported third-party telephony/widgets in model-driven apps; it is separate from native voice provisioning or moving numbers to Teams.
13. Typed, necessary, scoped values with provenance. Validate client-supplied data and distinguish a customer claim from an authenticated identity.
14. Message-direction/channel-specific active masking rules and attachment type/size, inspection, storage and retention controls. A masked UI does not establish protection in every downstream system.
15. Valid audience/identity and consent, authorized channel, frequency/quiet hours, local time zone, retries, suppression and stop behavior. Confirm documented dial-mode constraints with the responsible business/telephony owners.
16. Preview reserves a representative before dialing; progressive/predictive use availability and pacing in different ways. Check actual product/platform support, abandonment and the stated representative-led compliance limitation.
17. Forecasting estimates future volume/AHT; capacity planning translates assumptions into staffing; scheduling assigns shifts/activities; adherence compares actual activity with the schedule.
18. Routing chooses the next eligible assignment; workforce planning supplies future staffing. One cannot compensate for the other's missing capacity or incorrect data.
19. Approved, current, appropriately scoped case/conversation and knowledge evidence; validate material facts and distinguish source-access permissions from a fluent answer.
20. Typed inputs/results, effective-user authorization, bounded operations, state checks, retry/idempotency, audit, safe failures and appropriate confirmation. Prompts alone grant no permissions.
21. Classic topics provide explicit branches; generative orchestration chooses more flexibly and needs stronger evaluation/controls. Current real-time configurations also have documented conversion and model/channel limits.
22. DTMF uses keypad input, NLU interprets language, and speech adds recognition/voice interaction. Test the selected channel; DTMF support in the product does not imply support in its simulation tool.
23. Barge-in, noise/accent/language variation, latency, geography, tools, identity, sensitive audio, missing transcript turns, hallucinated commitments and safe escalation.
24. Voices, prompts, knowledge, notices, routing, terminology and measured behavior must work in each supported language. A model's language ability alone does not establish deployment readiness.
25. Priority orders work/queues; overflow responds to defined conditions; fallback receives unmatched or failed routing. Fallback can bypass configured overflow, and lower queue-priority numbers rank higher.
26. The workstream supplies input; classification enriches it; route rules select compatible queues; assignment checks membership, skills, presence and capacity under its configured strategy.
27. Explicit skills use known requirements; AI can infer them; intent routing uses detected/business-scoped intents; preferred routing favors continuity subject to configured availability rules. Test fallback and misclassification.
28. Applied classification/routing rules, resulting queue and assignment-event eligibility. Correlate timestamps and recognize dashboard support/delay limits.
29. Experience profiles shape persona tools; app tabs choose content; sessions organize the conversation context; notifications control offered-work prompts. Inbox views must respect data access.
30. A script guides steps, slugs insert context and macros execute supported repetitive actions. Validate the current session, variables, access and effects before retrying.
31. Supported API/version use, permissions, schema/error handling, session/event correlation, performance, accessible behavior and ALM; avoid unsupported DOM assumptions.
32. External content needs connector/source permissions, freshness, indexing, attribution and audience enforcement. Knowledge-harvesting support is narrower than every source Copilot might use.
33. Clear criteria/conditions, appropriate roles, source access, calibrated review, sampling evidence, corrections and product-use limits. Quality features are not intended for employment decisions.
34. Start with built-in reports for standard metrics, embedded editing for supported presentation changes, and Desktop/model extension when governed data/calculations require it. Preserve access, refresh and metric definitions.
35. Necessary IDs, stage/status, timing and diagnostic evidence under restricted retention/access. Avoid raw secrets and unnecessary personal content; sensitive-variable flags do not sanitize custom logs automatically.
36. Verified resolution/containment, quality/guardrails, customer outcomes, waits/abandonment, availability, workforce assumptions and total cost. State populations and uncertainty before expanding scope.
37. The lifecycle pages distinguish deprecation from September 30, 2028 removal. Existing supported channels continue during the transition; deployment/migration and new-number eligibility have separate rules.
38. Contact Center pages disagree between September 23 and September 30, 2026 for new-customer acquisition/port-in. October 23 in the ACS overview describes retiring-service sign-ups; it does not resolve the phone-number rule or existing-resource eligibility differences.
39. Intent and Knowledge Management underlying settings remain enabled when their plan is deleted/deactivated; Case Management rules behave differently. Verify each actual setting.
40. The preview covers English inbound voice, bounded concurrency/duration and no DTMF. It cannot prove digital, outbound, other-language or keypad behavior.
41. Work must satisfy every attached profile plus other assignment conditions. The example has total capacity but no high-priority capacity left.
42. Classification/routing failures and no-match fallback bypass fallback overflow. Prequeue checks also differ from postqueue waits and continuously evaluated playbooks.
43. Missing local time-zone data falls back to UTC, potentially placing the same moment outside configured quiet hours even when it is inside the customer's local quiet hours.
44. First-answer timing, unflagged unexpected input, explicit writes, transfer payloads, generative-AI input and custom/destination logs can escape protection. Verify each path and control completion.
45. Current text-LLM voice logging may omit turns or responses. Correlate other evidence and leave gaps visible rather than scoring an incomplete transcript as the entire interaction.
46. Enabling criteria scoring cannot be reversed by simply turning the feature off. Review configuration and change controls before enabling it.
47. No. The current decision tool only decides pending time-off requests with reviewer authorization; shift swaps/bids are list/detail capabilities.
48. A conversation may be rejected and later have no eligible representative. Use distinct IDs and set unions before interpreting counts or rates.

---

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one primary route, build representative end-to-end journeys, and add another resource only for a measured gap.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official AB-250 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-250) | Free | 1–2 hours to map objectives |
| [Implement an AI-powered contact center](https://learn.microsoft.com/en-us/training/paths/implement-dynamics-365-contact-center/) | Free | 4 modules; previous 2h 51m runtime not reverified |
| [Configure Contact Center channels](https://learn.microsoft.com/en-us/training/paths/configure-channels-dynamics-365-contact-center/) | Free | 4 modules; previous 3h 11m runtime not reverified |
| [Empower service representatives](https://learn.microsoft.com/en-us/training/paths/empower-service-representatives-contact-center/) | Free | 5 modules; previous 3h 52m runtime not reverified |
| [Monitor and optimize Contact Center](https://learn.microsoft.com/en-us/training/paths/monitor-optimize-dynamics-365-contact-center/) | Free | 3 modules; previous 1h 46m runtime not reverified |
| [AB-250T00-A course](https://learn.microsoft.com/en-us/training/courses/ab-250t00) | Paid/provider-dependent | 3 days |
| [Dynamics 365 Contact Center documentation](https://learn.microsoft.com/en-us/dynamics365/contact-center/) | Free | 10–25 hours selected implementation/troubleshooting |
| [LinkedIn Learning AB-250 Cert Prep](https://www.linkedin.com/learning/microsoft-dynamics-365-contact-center-ai-engineer-associate-ab-250-cert-prep/) | Subscription/trial | 4h 38m public runtime, July 27, 2026; Tutorials Dojo; paid lessons not viewed |
| [Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner login required | Verify current session start/end time after sign-in |

The four official paths expose **16 modules (4 + 4 + 5 + 3)**. Their old **11h 40m** duration total is historical; the fetched current outlines do not expose those totals. Allow roughly **40–70 hours** with journey design and ten labs as an editorial planning estimate. The three-day course remains listed; a partner schedule requires sign-in and was not verified. The official credential page does not offer a Practice Assessment. No exact current AB-250 product from Pluralsight, O'Reilly, MeasureUp or Whizlabs was independently verified on September 28, 2026. These bounded catalog searches do not establish market-wide absence. The LinkedIn outline includes broad Azure/AI material, so map lessons to the actual objectives instead of treating the full runtime as exam-specific coverage. Reject recalled live content, “valid questions” and pass guarantees.

### Useful blogs and focused exercises

- [Workforce management meets AI: WEM MCP tools](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/09/03/dynamics-365-workforce-engagement-management-mcp-tools/) — Edgar Wilson III, September 3, 2026. Build a request/action matrix for representative and supervisor personas. Separate list/detail from time-off decisions, then add unauthorized planning-group access, decided-request replay and missing rejection reasons. Keep V2/V3 schedule, leave-balance and clock tools in a future column. Allow 45–60 minutes; use synthetic records and perform no real workforce decisions.
- [Optimize workforce operations across people and AI agents](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/06/22/workforce-engagement-management-dynamics-3/) — Alan Ross, June 22, 2026, with a June 30 GA date in the article. Connect demand, staffing assumptions, schedules, adherence and quality in one worksheet. Use worked example 4, then vary volume/AHT/shrinkage and explain why queueing targets still need a proper model. Treat adapter and commercial claims as leads requiring current product verification. Allow 45–75 minutes.

Both main articles were read; linked videos, integrations, tenant behavior and performance claims were not reproduced. Their exercises supplement the blueprint. The [historical release plan](https://learn.microsoft.com/en-us/dynamics365/release-plan/2026wave1/service/dynamics365-contact-center/) says new capabilities move to the AI at Work roadmap from September 2026. Use it with current implementation and deprecation pages; a planned release date or a generic [what's-new landing page](https://learn.microsoft.com/en-us/dynamics365/contact-center/implement/whats-new) is not tenant availability evidence. The [26073 release notes](https://learn.microsoft.com/en-us/dynamics365/released-versions/dynamics365-omnichannel/26073) provide additional targeted messaging/voice regression ideas; only relevant sections were reviewed, not the entire release archive.

## Final readiness checklist

- [ ] I can design standalone, embedded or third-party CCaaS integration with users, security, connectors, ALM and TCO.
- [ ] I can trace chat, digital, custom/mobile and voice interactions through workstream, queue, routing, representative/agent and closure.
- [ ] I can govern authentication, recording, transcription, translation, attachments, masking and proactive outreach.
- [ ] I can configure WFM and explain its relationship to routing/capacity.
- [ ] I can distinguish Copilot assistance, smart assist, voice agents and service-oriented autonomous agents.
- [ ] I can configure queue priority, overflow/fallback, classification and assignment and diagnose the result.
- [ ] I can tailor profiles, templates, inbox, scripts, macros, Teams and knowledge.
- [ ] I can configure supervisor actions, quality evaluation, Power BI and Application Insights responsibly.
- [ ] I verify current telephony, SDK/API, agent, licensing, capacity, provider and regional details.
- [ ] I use original practice and evidence without seeking live exam content.
