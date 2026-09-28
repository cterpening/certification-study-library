---
exam_code: AB-730
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-730
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-27
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-27
---

# AB-730 AI Business Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The complete guide and current public sources were reviewed September 27, 2026. All 41 published October objectives are mapped in the [deep-review record](../docs/research/2026-09-27-ab-730-deep-review.md); the accepted July 22 baseline remains separately dated. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ab-730-coverage-record). The [official AB-730 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-730) is authoritative.

**Current baseline:** Skills measured as of July 22, 2026.<br>
**Upcoming blueprint change (checked September 27, 2026):** The English blueprint changes October 20, 2026. The revision introduces a fourth domain for agents, rebalances domain weights, and adds Copilot Cowork and Work IQ. Use the dated preparation supplement below for an appointment on or after the change. The current baseline below remains dated separately. See the [official revision](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-730).<br>
**Lifecycle:** The [AI Business Professional credential](https://learn.microsoft.com/en-us/credentials/certifications/ai-business-professional/) and 45-minute exam are active; the credential page currently lists 13 languages. Recheck the revision date for your exam language.<br>
**Official source:** [AB-730 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-730)

## How to use this guide

AB-730 is a beginner business-user exam, but useful preparation is not a list of Copilot buttons. For every task, trace:

1. the business outcome, audience, decision, and definition of a good result;
2. the right Microsoft 365 app, chat, agent, page, notebook, Researcher, or Analyst experience;
3. the goal, context, sources, constraints, and expected output in the prompt;
4. what organizational or web data may be used and what the user is allowed to access;
5. the risk of fabrication, prompt injection, oversharing, bias, copyright, or over-reliance;
6. the verification and human judgment required before the output is used;
7. whether the reusable prompt, conversation, page, notebook, or agent should be saved, shared, scheduled, or deleted.

Practice with realistic, nonsensitive material in Word, Excel, PowerPoint, Outlook, Teams, and Microsoft 365 Copilot. Build a small agent from a template if your tenant permits it. The role improves work with AI; it does not build AI applications or write code.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Preparation supplement for October 20, 2026

**Future scope, checked September 27:** Keep the July map below for earlier appointments. The [October blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-730) has four domains:

| October study area (paraphrased) | Weight | Preparation focus |
|---|---:|---|
| Generative AI foundations | 25–30% | Permission-aware context, responsible use, choosing chat or delegated work |
| Copilot prompts and chats | 20–25% | Model choice, prompt refinement, memory/instructions, chat and notebook management |
| Business content and collaboration | 20–25% | Connectors, Work IQ, cross-app output, visualizations, meeting preparation and recap |
| Business outcomes with agents | 20–25% | Prebuilt/custom-agent choices, Cowork skills, task supervision and scheduling |

The earlier custom-agent construction group is removed. The choice between prebuilt and custom remains, while the new domain requires applying agents, filtering their chats, and supervising Cowork. Sections 2–4 cover the added model, notebook, connector, visual, meeting, skill, and automation objectives. Keep the older agent-construction exercise for the July baseline and optional practical context.

### Context, delegation, and checking the result

[Work IQ](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/) combines organizational information, context, and tools under permission-aware governance. A useful study question is which authorized sources support a business conclusion. Specify the reporting period, people, files, and expected deliverable; verify that the cited evidence actually supports the answer. A persuasive summary does not establish that every relevant source was available.

[Copilot Cowork](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/) performs tasks across Microsoft 365 and loads skills for particular kinds of work. Study the difference between generating an answer and authorizing actions that affect files, messages, or calendars. Review the proposed work, inspect progress, and verify the resulting artifacts. **VERIFY CURRENT:** Account type, organizational controls, preview features, and approval settings affect available behavior. The overview distinguishes generally available work/school access from personal-account preview; that does not establish eligibility for every feature.

The [Cowork operating guide](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/use-cowork) explains skills, session controls and schedules. Section 4 distinguishes a single action, a session-wide approval and automation preauthorization. Record scope, timing, expected output and how to stop recurring work; inspect a run before relying on it.

### Original practice extension

Use a disposable work area and synthetic project files. Ask for a weekly project brief with unresolved decisions, evidence links, a small chart, and a draft follow-up. Define who may receive the output before starting. Compare an ordinary chat response with a delegated Cowork task; explain which parts need source retrieval, a document skill, and an action approval. Inspect the proposed recipients and generated numbers before allowing any communication. If scheduling is available, create a test recurrence, verify its settings, and disable it after the exercise. If unavailable, document the intended setup and the access limitation.

Readiness: explain why a fluent answer may still lack evidence; justify chat versus a prebuilt agent versus Cowork; distinguish a reusable skill from a scheduled task; and identify where a person checks the plan, actions, and final result.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Understand generative AI fundamentals | 25–30% | Can you select an appropriate Copilot experience and use it responsibly with permitted context? |
| Manage prompts and conversations by using AI | 35–40% | Can you create reusable prompts, manage conversations, and configure a focused agent? |
| Draft and analyze business content by using AI | 25–30% | Can you create, transform, analyze, and collaborate on content while retaining human accountability? |

---

## 1. Understand generative AI fundamentals

### Understand what generation does—and does not prove

Generative AI predicts useful output from instructions and context. It can draft, summarize, reorganize, compare, brainstorm, translate, explain, extract, and analyze. Fluent output is not evidence that the result is true, complete, current, authorized, unbiased, or suitable for the decision. Treat the response as a proposed work product whose verification depends on its use.

The model has learned patterns from training. The current conversation, referenced files, web results, app context, organizational content, and configured instructions can ground a response. Grounding makes a response more relevant and checkable; it does not guarantee truth. If the source is incomplete, outdated, ambiguous, or inaccessible, the output can inherit the problem.

Ask whether the task is:

- **creative or exploratory:** ideas, variants, outlines, tone changes;
- **transformative:** summarize, rewrite, compare, translate, extract;
- **analytical:** trends, explanations, formulas, charts, risks, recommendations;
- **research-oriented:** gather and synthesize multiple sources with citations;
- **action-oriented:** an agent uses knowledge or capabilities for a repeatable task.

The higher the consequence, the stronger the source, verification, approval, and record needed. A brainstorm can tolerate uncertainty; financial reporting, personnel decisions, customer commitments, safety instructions, and legal claims cannot.

### Understand context and organizational protection

Microsoft 365 Copilot can use the prompt, conversation, current app, attached or referenced material, permitted Microsoft 365 work content, and sometimes web content. Microsoft Graph connects the experience to organizational data the signed-in user can access. Copilot does not grant a user new permissions, but existing oversharing can make too-broad content discoverable and usable. “Copilot respects permissions” is not the same as “all existing permissions are correct.”

Context changes the response:

- In Word, the current document and referenced files support drafting and revision.
- In Outlook, a message or thread supplies communication context.
- In Teams, meeting transcript/chat and channel context support summaries and follow-up.
- In PowerPoint, a prompt or source document can seed a presentation.
- In Excel, a structured table and explicit analytical question support formulas, insights, and visuals.
- In Microsoft 365 Copilot Chat, work or web grounding and selected sources shape a cross-app response.

Check which context is active, whether it is complete and current, and whether every intended recipient may access the resulting content. A generated summary can reproduce sensitive details from its source even when the summary itself looks harmless.

> **Related item:** Data hygiene precedes AI hygiene. Clear ownership, sensible sharing, sensitivity labels, retention, and accurate source documents improve both conventional search and Copilot results.

### Distinguish chat, agents, Researcher, Analyst, pages, and notebooks

| Experience | Strong fit | Important boundary |
|---|---|---|
| Copilot Chat | Flexible one-off or iterative prompting across work/web context | Conversation and available grounding vary; verify sources and permissions |
| Copilot Cowork | Delegate a deliverable spanning several actions or apps | Inspect action authority, skills, usage budget, progress and final artifacts |
| App Copilot | Work grounded in the active Word, Excel, PowerPoint, Outlook, or Teams context | Each app exposes different capabilities; do not assume feature parity |
| Agent Store agent | A discoverable prebuilt or organization-published agent already fits the task | Review publisher, knowledge, capabilities, sharing, and approved use |
| Custom agent | A repeatable, bounded task needs tailored instructions, knowledge, suggested prompts, or capabilities | Build only when an existing agent does not fit; test and share deliberately |
| Researcher | Multistep research and synthesis across allowed sources with an evidence trail | Inspect citations, source quality, omissions, and recency |
| Analyst | Deeper data reasoning, calculations, analysis, and visual exploration | Validate input shape, assumptions, computations, and business interpretation |
| Copilot Page | Editable, shareable canvas that turns a response into collaborative content | Sharing the page can broaden the audience; verify content and access |
| Notebook | Persistent project context that collects conversations and sources | Curate source scope, remove stale material, and understand who can access it |

A chat responds inside a conversation. An agent has a more durable purpose, instructions, knowledge, capabilities, and sharing boundary. Create an agent when a repeated task needs controlled reuse; do not create one merely to rename a prompt. **VERIFY CURRENT:** agent availability, Agent Store content, Researcher/Analyst capabilities, Pages/Notebooks behavior, licensing, regions, sharing, and supported apps change frequently.

### Connect work context without assuming complete access

[Copilot connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/overview) bring external systems into the context available to Copilot. Synced connectors index content; federated connectors fetch it live without building that index. Both depend on source permissions and organizational configuration. A live fetch still might omit a source or return incomplete data. As checked September 27, federated connectors are read-only; write actions are announced for early October, not established support for every connector today.

For a missing customer ticket, [check the source directly](https://support.microsoft.com/en-us/microsoft-365-copilot/understand-copilot-connectors), your access, connector enablement/authentication, query scope, and indexing delay when applicable. Record a missing source as a limitation. Do not turn “no ticket found” into “the customer has no problems.” Name account, time period and system, request citations, and reconcile conflicting records with their owners.

Work IQ supplies business context; it is not permission to see every record. Its API billing is separate from the included experience described for licensed Copilot users. Do not infer entitlement from a button or an API announcement. New Dynamics 365/Power Platform grounding has a September 30 preview start and staged October rollout; see the dated blog exercise below.

### Apply responsible AI and data protection

Common user-level risks include:

- **fabrication:** confident but unsupported facts, citations, calculations, or events;
- **prompt injection:** untrusted text tries to override instructions or obtain data/actions;
- **over-reliance:** a person accepts the result because it is polished or fast;
- **oversharing:** sensitive source or generated content reaches an unintended audience;
- **bias and exclusion:** source patterns or framing produce unfair or incomplete results;
- **privacy/copyright risk:** personal, licensed, confidential, or third-party material is used inappropriately;
- **stale context:** old policies, files, conversations, or memory shape the result;
- **purpose drift:** a draft or analysis is reused for a higher-stakes decision than intended.

Use a verification plan proportionate to the task:

1. inspect cited or referenced sources and confirm they support each material claim;
2. compare critical facts, dates, names, totals, quotations, and policy statements with an authoritative source;
3. recalculate important numbers and test assumptions;
4. ask what is missing, uncertain, conflicting, or based on inference;
5. check audience, tone, accessibility, bias, confidentiality, and sensitivity labels;
6. obtain a qualified human review before consequential use;
7. preserve source and approval evidence where the business process requires it.

Sensitivity labels, DLP, permissions, and organizational policy can restrict which content is used, returned, copied, or shared. A restricted result is not a prompt failure to bypass. Remove unauthorized sources, request legitimate access, or use an approved alternative. Never paste confidential information into an unapproved consumer AI tool merely because an enterprise response is constrained.

---

## 2. Manage prompts and conversations by using AI

### Create a prompt with a testable contract

A useful prompt specifies:

- **Goal:** the action and business outcome—draft, compare, summarize, analyze, recommend, or plan.
- **Context:** audience, situation, background, constraints, and decision that follows.
- **Sources:** the files, messages, meeting, data, or web sources it may use; state whether it must avoid outside knowledge.
- **Expectations:** output format, length, tone, language, fields, assumptions, citations, quality checks, and what to do when evidence is missing.

Example structure: “Create a one-page management summary for regional directors from the attached approved report. Cover performance versus target, three material risks, owners, and next actions in a table. Cite the report page or section for every number. Do not infer missing values; list them under Questions.”

Begin with the minimum relevant context. Adding every available file can introduce conflicts, stale material, sensitive content, and distraction. Choose authoritative, current, permitted sources. Name the desired viewpoint and audience without asking the model to impersonate a person or conceal uncertainty.

Iterate deliberately. First inspect whether the response followed the task and sources. Then correct missing context, ambiguous instructions, unsupported claims, format, tone, or length. Ask the model to identify assumptions and uncertainties, but verify those statements independently. A longer prompt is not automatically better; clarity and relevant evidence matter more.

> **Related item:** A prompt library becomes business process documentation. Give important reusable prompts an owner, purpose, approved sources, example input/output, validation checklist, version date, and retirement trigger.

### Choose the available model for the task

The [Copilot model selector](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-chat-considerations) offers Auto, Quick response and Think deeper: select for routine speed or more involved reasoning, then compare outputs against the same evidence. Model names and availability change by app, license and policy. Longer reasoning does not grant source access or prove correctness.

[Researcher model choice](https://support.microsoft.com/en-us/office/use-model-choice-in-the-researcher-agent) has its own conditions: Claude needs administrator enablement, and the newer Auto/Model Council experiences require Frontier access. A second model's agreement is not independent confirmation when both use the same faulty source. Check citations and resolve disagreements in the source material. In [Excel](https://support.microsoft.com/en-us/excel/copilot/copilot-in-excel-tips), model choice is session-specific and editing can change the workbook directly; use a disposable copy and review changes/version history.

### Save, schedule, and share prompts safely

Save a prompt when the task repeats and the prompt is worth curating. Give it a meaningful title and remove case-specific sensitive content. Retest it with different representative inputs. Schedule a prompt only when the source availability, timing, recipient, review step, and output destination are appropriate for unattended recurrence. A scheduled prompt that generates a weekly report still needs ownership and exception handling.

Share a prompt when colleagues can legitimately use its instructions and sources. Explain prerequisites, expected references, limitations, and verification. Sharing the words of a prompt does not necessarily share source access, licensing, or identical context; recipients can receive different results. Avoid embedding secrets, personal data, customer details, or inaccessible file paths.

[Copilot Chat scheduled prompts](https://support.microsoft.com/en-us/microsoft-365-copilot/schedule-your-most-used-copilot-prompts) require an eligible Copilot license and enabled Optional connected experiences. The current limit is ten; scheduling is supported in Chat, Teams and Outlook. Inspect run count, time, notification and resulting chat; turn off or delete the recurrence when finished. Cowork has a separate automation surface and currently allows 25 scheduled prompts. These limits are experience-specific and should be rechecked.

### Manage conversation history and notebooks

Use the [Chats list and its More menu](https://support.microsoft.com/en-us/microsoft-365-copilot/how-microsoft-365-copilot-chat-history-works) to revisit, rename, move to a notebook, or delete a conversation. Name it so purpose and sensitivity are recognizable. Delete a chat when it is erroneous, obsolete, unnecessarily sensitive, or no longer required—subject to organizational retention and eDiscovery policies. Deleting from the user's visible history is not a promise that every compliance record disappears.

Start a new chat when prior context would confuse or contaminate the next task. Keep one conversation when iterative context is intentional. Before continuing an old conversation, inspect its sources, assumptions, audience, and date.

Add a conversation to a notebook when it belongs to a durable project context with curated sources and repeated work. A notebook is not a dumping ground for every related chat. Remove stale or contradictory material, organize it around the project outcome, and review access before adding sensitive content.

[Notebook references](https://support.microsoft.com/en-us/microsoft-365-copilot/add-references-to-your-microsoft-365-copilot-notebook) define the grounding scope; unrelated organizational content is not automatically included. Adding a site or folder can widen that scope beyond one selected file. The current page distinguishes up to the first 300 grounded references for Copilot users from 50 for Copilot Chat users. A notebook with more references is not evidence that every item influenced the answer.

**Sharing can change file access.** Notebook sharing invites recipients to linked files when you have permission to share them, subject to source/plan restrictions; otherwise they need to request access. Review every reference before sharing, including sources that did not appear in the latest answer.

#### Worked example: the summary is harmless but its references are not

Alice's notebook contains a public team plan and a synthetic compensation worksheet. Bob needs only the plan. Alice can technically share both files, but the business purpose permits only the plan. Sending the notebook can invite Bob to both references even if the displayed summary mentions no compensation. Create a separate notebook with the plan alone, check its reference list and recipient access, then share that scoped copy. Removing sensitive words from the summary does not remove the referenced file.

### Separate memory, history and instructions

[Memory controls](https://support.microsoft.com/en-us/microsoft-365-copilot/personalize-what-microsoft-365-copilot-remembers) distinguish saved details, inferences from chat/work content, and explicit preferences. Deleting one saved memory does not necessarily remove other personalization sources. Review the relevant controls and [custom instructions](https://support.microsoft.com/en-us/microsoft-365-copilot/customize-how-microsoft-365-copilot-responds-to-you). The history control documents a 30-day deletion period; switching it back on within that window can restore inferred memories.

A temporary chat avoids using/updating personalization and is absent from visible history, but organizational retention can still apply. This is not a way around records policy. Keep durable formatting preferences separate from changing facts such as this month's target or a customer's approval status.

### Select, create, configure, and share an agent

Search the Agent Store before building. An existing agent is preferable when its publisher, task, knowledge, capabilities, permissions, and support fit. Create a new agent when the task is distinct, repeated, and bounded enough to justify tailored behavior.

Templates accelerate creation but still require review. Define:

- a precise name, purpose, intended audience, and tasks it must refuse or escalate;
- instructions describing workflow, tone, output, boundaries, verification, and uncertainty;
- current, authoritative, minimum-necessary knowledge that intended users may access;
- capabilities required for the task and no unnecessary action surface;
- suggested prompts that teach users safe, valuable starting interactions;
- owner, reviewers, test set, support route, and retirement/update triggers.

Test expected, vague, incomplete, sensitive, out-of-scope, conflicting-source, and malicious prompts. Confirm the agent does not reveal inaccessible knowledge or imply authority it lacks. Share first with a small team, communicate limitations, collect failures, and expand only after the evidence supports it. Sharing an agent does not automatically grant users access to every knowledge source.

---

## 3. Draft and analyze business content by using AI

### Draft a new document from a prompt

Specify document type, audience, outcome, source, structure, tone, length, and required action. Ask for placeholders rather than invented facts. A first draft should expose assumptions and questions. Review organization, factual accuracy, policy alignment, confidentiality, accessibility, and whether the content actually helps the audience decide or act.

For communications, distinguish internal update, customer email, executive brief, proposal, policy, and persuasive message. Tone is not the only difference: authority, evidence, approval, disclosures, and retention vary. Do not let Copilot send a consequential message merely because it created a plausible draft.

### Generate from an existing document and create management summaries

When transforming an existing document, define whether to preserve facts, terminology, voice, citations, or layout. Ask the response to separate what came from the source from suggestions. Compare the output with the complete document, especially limitations, footnotes, exceptions, tables, and appendices.

A management summary should identify purpose, current state, material results, risks, decisions, owners, deadlines, and missing evidence at an appropriate level. It should not erase dissent, uncertainty, or a low-frequency high-impact risk. Verify every figure and named commitment. If two source sections conflict, report the conflict rather than picking the more convenient one.

Researcher can help collect and synthesize allowed sources for a richer draft. Inspect its citations, publisher authority, dates, source diversity, and whether the conclusion exceeds the evidence. Analyst can explore a data set and produce calculations or visuals; validate schema, filters, units, missing values, outliers, formulas, and the business meaning of correlation or trend.

### Generate visuals that answer the business question

Choose a chart for comparison, trend or composition; specify units, dates, denominators, filters and how to treat missing values. Generate a concept image only when an illustration is appropriate, and check labels, accessibility, rights and whether it could be mistaken for evidence. A polished image of a chart is not a substitute for a chart tied to verified data.

#### Worked example: gross growth is not net growth

A synthetic workbook has gross revenue of 120 in Q1 and 150 in Q2, with returns of 10 and 30 respectively, all in the same units. Gross growth is `(150 - 120) / 120 = 25%`. Net revenue is 110 then 120, so net growth is `(120 - 110) / 110 ≈ 9.09%`. A slide claiming “net revenue grew 25%” is wrong even if its chart exactly matches gross revenue. Name the measure, retain formulas, reconcile the brief and deck, and show missing periods as missing rather than zero.

### Move data and insights across Microsoft 365 apps

A useful workflow often crosses app boundaries:

1. summarize a Teams meeting and confirm decisions/owners;
2. turn approved decisions into an Outlook follow-up;
3. analyze a structured Excel table and validate totals;
4. create a Word management brief using the approved analysis;
5. build a PowerPoint narrative for a defined audience;
6. place working content in a Copilot Page for collaboration.

Each transition can lose source context, formatting, permissions, sensitivity labels, or nuance. Recheck audience and access at the destination, keep a link to the authoritative source, and distinguish live data from a copied snapshot. Do not move restricted data into a broadly shared page or deck just because Copilot makes the transfer easy.

### Use Copilot for meetings and collaboration

Before a meeting, use allowed documents, email, and prior action items to develop an agenda and questions. During or after a meeting, Copilot can summarize discussion, decisions, disagreements, unanswered questions, owners, and follow-ups when transcript and policy settings support it. Participants should know recording/transcription practices, and a human should confirm consequential decisions.

Ask for evidence: “Which transcript passage supports this decision?” Verify names, due dates, and speaker attribution. Silence is not consent, and absence from a transcript is not proof that something did not occur. Handle sensitive HR, legal, customer, and security meetings according to policy.

Copilot Pages turns a response into an editable shared workspace. Use it to refine plans, briefs, research, or meeting outcomes with colleagues. Before sharing, remove irrelevant private context, verify facts, set the right audience, and assign ownership. Edits can make the page diverge from its generated sources, so retain provenance for important claims.

### Distinguish the three meeting experiences

| Experience | Useful task | Required check |
|---|---|---|
| Private Copilot catch-up | Ask what you missed or identify disagreement during a meeting | Available spoken context depends on meeting settings; private prompts differ from shared notes |
| Facilitator | Shared live notes, agenda tracking and meeting-chat assistance | License, meeting type, organizer/presenter controls, and participant visibility |
| Intelligent recap | Review notes, tasks and supported recording markers afterward | Transcript/recording, language, license and permissions determine available features |

[Real-time catch-up](https://support.microsoft.com/en-us/teams/copilot/catch-up-on-meetings-with-microsoft-365-copilot-in-teams) can work in the “Only during” mode without saved transcription. To ask afterward about spoken discussion, a transcript is needed; chat-only context is different. “Off” disables meeting Copilot/recording/transcription, but does not mean the separate chat has vanished. Protected meetings can also block exporting responses.

[Facilitator](https://support.microsoft.com/en-us/teams/copilot/facilitator-in-microsoft-teams-meetings) requires a Copilot license to add/enable it; internal participants can see shared updates. The scheduled online-meeting route excludes channel meetings, instant meetings and calls; the documented mobile in-person capture is a separate experience. Its Loop notes are editable, so they are not an immutable transcript. Task management by @mention is currently public preview. Automatically captured tasks require accepting sync; directly requested tasks can sync to Planner. Check task owners and dates before treating them as commitments.

[Intelligent recap](https://support.microsoft.com/en-us/teams/meetings/recap-in-microsoft-teams) is available through Teams Premium or Copilot. AI summaries need a supported-language transcript and an event at least five minutes long; some recording markers need both recording and transcription. A copied recap link still requires access; explicitly sharing a recap can grant it. Review the audience and any draft summary email before sending.

#### Worked example: incomplete capture is incomplete evidence

A synthetic 40-minute meeting starts at 10:00, but transcription starts at 10:20. Its transcript covers only the last 20 minutes. A recap that finds no budget decision cannot establish that no decision happened in the first half. Record the coverage gap, ask the owner to confirm the decision against an approved record, and distinguish that confirmation from the generated recap.

Memory and instruction settings are covered in Section 2. Avoid assuming the same personalization or chat-deletion controls exist in every app: Excel's current help does not offer individual conversation deletion.

> **Related item:** The value of Copilot is a better business outcome, not maximum generated volume. Measure time saved together with correction rate, decision quality, adoption, risk, accessibility, customer or employee impact, and rework.

---

## 4. Apply agents and supervise Cowork — October preparation

### Select an agent and return to its work

Choose a prebuilt agent when its approved task and data scope fit; choose a custom agent when repeatable requirements need different instructions or sources. Researcher fits cited synthesis; Analyst fits deeper data exploration; neither replaces verification. Apply the agent from a supported Copilot surface and confirm its name, publisher and available sources. [Agent availability](https://learn.microsoft.com/en-us/microsoft-365/copilot/agent-essentials/m365-agents-admin-guide) depends on organizational deployment, access and supported channels.

The October blueprint explicitly requires filtering chats by agent. Practice finding a known agent conversation using the agent filter available in your chat-history experience, then reopen it and verify the agent and date before continuing. If the filter is absent in your rollout, record that limitation and use clearly named history as a fallback; the public history article reviewed here does not establish a universal filter location. Filtering history organizes prior work; it does not change permissions or convert an ordinary chat into that agent.

### Choose a skill, then supervise the deliverable

A skill supplies reusable task instructions; a connector supplies access to a data service; a plugin can package both. These are different from a schedule that decides when work starts. Begin with an appropriate built-in skill. Use a custom skill for a repeated process with specific outputs, boundaries and review steps.

In [Cowork Customize](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-customize), inspect the skill's source and instructions, create or edit it, then test in a new conversation. Shared updates require Re-share. Only import trusted material. The operating guide describes automated skill evaluation, while the [application card](https://learn.microsoft.com/en-us/microsoft-365/copilot/responsible-ai/copilot-cowork-application-card) warns that user-authored skills are not Microsoft-validated: a quality score is not certification that your business process is correct. Test missing inputs, wrong recipients and malicious source instructions.

Delegate a concrete result: scope, sources, file destination, audience, deadline, and what needs review. Inspect the plan, progress, active skills and final artifacts. Not every internal operation has a visible step. [Cowork controls](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq) distinguish pausing after the current step, immediate pause and cancel; none promises to undo completed work. Check existing outputs before retrying so an interrupted run does not duplicate an action.

### Understand the approval you give

The action dialog can approve one action, all currently pending actions, or similar actions for the rest of the session. Recipient/domain-scoped options can narrow message approvals. Review and revoke session approvals in the Permissions panel. An existing Office file can be edited in place after approval, affecting collaborators; inspect version history rather than assuming every output is a separate draft.

#### Worked example: one approval can cover a later message

In a synthetic session, Alice authorizes messages only to Bob for the rest of that session. A later message to Bob may not prompt again. That is different from approving only the displayed first message; neither grants a new conversation the same approval. An automation may have separately preauthorized actions, so inspecting only the current conversation is insufficient. Review the actual approval scope and task definition before relying on a future pause.

### Manage recurring work and access

In Cowork, inspect both schedule definitions and run history; verify timezone, recurrence, source scope, destination and action permissions. “Activate and run now” differs from activating for the next scheduled time. Pause or delete test schedules after verifying one result. Event-driven email/Teams tasks are related context, separate from time schedules.

[Organizational governance](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance) says automated work runs as its creator and asks before sensitive actions by default, but users can preauthorize actions during setup. Do not assume every unattended run waits for a fresh approval. Cowork access comes through a spending policy selecting the service; a tiny credit allowance still grants access. Model enablement and discoverability are separate controls. Review expected usage and the approved service with your administrator, without treating a small budget as an access denial.

### Check the execution surface

Cowork can misinterpret instructions, omit steps or use incomplete evidence. Its application card lists protected-file and cloud-file deletion limitations; permissions alone do not establish feature support. Explicit upload is different from unrestricted access to local files.

[Local browser tasks](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-local-browser) use supported Edge on the user's device and its signed-in session. They require tenant enablement and are currently unavailable in the desktop/mobile app. Review the actual site account and let the user complete credentials, MFA or human-verification handoffs. Browser capability does not imply permission to bypass a blocked site or approve a form submission.

---

## Integrated scenarios

### Scenario A: Weekly executive status

A project manager references approved project files and meeting notes. A saved prompt requests progress versus milestones, decisions, top risks, owners, dates, and questions in a one-page format with citations. Analyst checks the structured tracker; the manager independently verifies totals. A scheduled run creates a draft, not an automatic executive publication. The manager reviews sensitivity, corrections, and changes before moving approved content to Word and PowerPoint.

### Scenario B: Client proposal team

Researcher gathers approved internal case studies and current public client/industry sources. A prompt separates sourced facts, assumptions, and proposed language. The team creates a Word draft, uses a Copilot Page to collaborate, then builds a PowerPoint deck. Every claim, image right, price, capability, and commitment receives owner approval. Restricted internal references do not move into the client deliverable.

### Scenario C: Reusable policy assistant

The HR team first checks Agent Store, then creates a bounded agent from a template because no approved agent fits. Knowledge contains current employee-facing policies, not confidential cases. Instructions cite the policy, state uncertainty, refuse personal determinations, and route exceptions to HR. Suggested prompts cover common questions. Tests include obsolete policy, conflicting sources, prompt injection, sensitive requests, and two user personas. Sharing starts with a pilot team.

---

## Practical labs

1. **Context comparison:** Run one business task in Copilot Chat and two relevant Microsoft 365 apps; record which context and capabilities change the result.
2. **Responsible-AI review:** Seed ten benign inaccuracies, missing facts, sensitive fields, and malicious instructions into test material; build and apply a proportionate verification checklist.
3. **Prompt clinic:** Write and compare at least 12 prompts using goal, context, sources, and expectations; keep evidence of why revisions improved the result.
4. **Prompt lifecycle:** Save, rename, share with a test colleague, and—if available—schedule a nonsensitive prompt; document differences in access, context, results, and controls.
5. **Conversation/notebook:** Continue and restart the same task, rename and find chats, test deletion behavior, and curate selected work into a notebook without stale sources.
6. **Agent pilot:** Compare Agent Store options, create from a template, configure instructions/knowledge/capabilities/suggested prompts, test adversarial cases, and share narrowly.
7. **Cross-app workflow:** Move a validated analysis from Excel through a Word brief and PowerPoint deck, tracking source, permissions, labels, figures, and human approvals.
8. **Meeting/collaboration:** Use a synthetic meeting transcript to create decisions and actions, verify attribution, publish a sanitized Copilot Page, and review memory/instruction effects. Compare private catch-up, Facilitator notes and recap; retain an explicit missing-transcript example.
9. **Context and sharing audit:** Use synthetic files you own and permitted test accounts. Compare notebook reference scope and sharing before/after, a missing connector source, and the gross-versus-net chart example. Record source timestamps, recipients, observed access and corrected calculations; remove the test share afterward.
10. **Supervised delegation:** In an enabled test environment, use a built-in skill for a draft brief, then compare a narrowly scoped custom skill in a new session. Inspect single-action/session approval options without sending to real recipients; verify in-place file edits and recovery on a disposable copy. Run one test schedule, inspect its result and permissions, and disable it. Locate the agent's prior chat/filter where available. If access is unavailable, submit a tabletop plan with the limitation rather than claiming execution.

Use synthetic or approved nonsensitive data. Save prompts, expected outcomes, sources, output, errors, corrections, decisions, and what a human had to add.

---

## Knowledge checks

1. Why is fluent output not evidence that a claim is true?
2. What kinds of context can change a Copilot response?
3. Why can Copilot-respected permissions still expose an oversharing problem?
4. When should work stay in an app Copilot instead of Copilot Chat?
5. How does a chat differ from an agent?
6. When are Researcher and Analyst appropriate, and what must be verified?
7. What is the purpose of a Copilot Page and a notebook?
8. When should you create an agent instead of using Agent Store?
9. What are fabrication, prompt injection, and over-reliance?
10. Which verification steps fit a high-consequence business decision?
11. Why should a user not bypass a data-protection restriction?
12. How can sensitivity and audience change during cross-app reuse?
13. What are the goal, context, sources, and expectations in an effective prompt?
14. Why can too many references make a prompt worse?
15. How should a prompt handle missing evidence?
16. What makes iterative prompting deliberate rather than random?
17. When is a prompt worth saving?
18. What must be true before scheduling a prompt?
19. Why can two people get different results from a shared prompt?
20. When should a new chat replace an old conversation?
21. What does deleting visible chat history not necessarily change?
22. What belongs in a curated notebook?
23. What must be checked before choosing an Agent Store agent?
24. Which fields define a bounded custom agent?
25. Why does sharing an agent not automatically share its knowledge?
26. Which adversarial tests should an agent pilot include?
27. What belongs in a good first-draft request?
28. How should a generated document distinguish source facts from suggestions?
29. What can a management summary accidentally hide?
30. How do you validate Analyst output?
31. How do you validate Researcher citations?
32. What can be lost when content moves between apps?
33. How should Copilot meeting decisions and attribution be verified?
34. What must be checked before sharing a Copilot Page?
35. What information is inappropriate for memory or persistent instructions?
36. Which outcome measures matter beyond the volume of generated content?
37. When should model choice change, and what can it never establish?
38. How do synced and federated connectors differ, and what does a missing result prove?
39. Why can sharing a notebook expose a reference absent from its latest summary?
40. Why is the example's net growth about 9.09% rather than 25%?
41. How do private catch-up, Facilitator and intelligent recap differ?
42. How are a skill, connector, plugin and schedule different?
43. Why might Cowork take a later action without displaying a new approval?
44. What must be checked before retrying or stopping delegated work?

### Answer checkpoints

1. Fluency reflects plausible generation; corroborating evidence establishes the claim.
2. Prompt, app, conversation, referenced material, authorized work/web sources and personalization.
3. Existing broad access can make inappropriate source content available without new privilege.
4. Use the app when its active artifact and editing tools fit; compare available context.
5. Chat supports an exchange; an agent applies a durable task purpose and configured capabilities.
6. Researcher supports synthesis; Analyst supports data reasoning. Verify sources, computations and interpretation.
7. Pages supports collaborative output; notebooks organize the references and conversations for focused work.
8. Build when approved prebuilt choices cannot meet a repeatable, bounded requirement.
9. Unsupported output, hostile instructions embedded in content, and accepting output without sufficient scrutiny.
10. Authoritative source checks, independent calculations, missing-evidence review and accountable human judgment.
11. The restriction expresses a data/access policy; use a legitimate authorized path.
12. Copied content can enter a different audience or lose protections; inspect the destination.
13. Outcome, situation/audience, allowed evidence, and the required format/quality/boundaries.
14. Irrelevant, stale or conflicting material can obscure the needed evidence.
15. Identify the gap and request the source; do not manufacture a value or commitment.
16. Change a specific defect and compare the revision against explicit acceptance criteria.
17. It repeats, has a clear owner and works on varied representative inputs.
18. Confirm entitlement, timing, sources, ownership, destination, review and stop behavior.
19. The prompt text does not reproduce another person's permissions or context.
20. When earlier context would distort the new task; separately check personalization settings.
21. Compliance retention and other personalization sources might remain.
22. Current, relevant, permitted references with a defined project purpose.
23. Publisher, task, data/action scope, availability, permissions and support.
24. Purpose, audience, instructions, knowledge, capabilities, prompts, tests and escalation.
25. Agent access and source access are separate checks; inspect the actual sharing mechanism.
26. Missing/conflicting/obsolete sources, injection, sensitive requests, wrong identities and out-of-scope actions.
27. Audience, purpose, evidence, structure, tone, constraints and placeholders for unknowns.
28. Mark supported facts, uncertainty and proposed additions separately; preserve provenance.
29. Exceptions, dissent, coverage gaps and important low-frequency risks.
30. Inspect schema, units, filters and missing values; independently reconcile key calculations.
31. Open the cited source, check date/authority and whether it supports the particular claim.
32. Source links, units, meaning, permissions, labels and live-versus-snapshot status.
33. Check captured evidence and ask accountable participants about uncertain attribution or decisions.
34. Content, audience, source permissions, protections and ownership of later edits.
35. Secrets and transient facts that should be rechecked for the current task.
36. Quality, correction/rework, time, decision usefulness, accessibility and business impact.
37. Match speed/reasoning and allowed models to the task; choice cannot grant data access or prove truth.
38. Synced content is indexed; federated content is fetched live. Missing results do not establish absence.
39. Sharing can invite recipients to linked files the sharer can share, including unused references.
40. Net values are 110 and 120 after returns; gross values use a different measure and denominator.
41. Private questions, shared live assistance, and post-meeting review have different visibility and capture requirements.
42. Instructions, data access, a package of capabilities, and a timing/trigger definition respectively.
43. A session-wide approval or separately preauthorized automation may already cover it.
44. Check completed actions, file versions, pending permissions, schedules and duplicates; cancel is not rollback.

---

## Places to learn

This is a selective starting set, not a complete list and not a requirement to consume everything. Pick the explanation, hands-on practice, and assessment style that works for you, and map each resource to the blueprint effective for your appointment. Current public listings were checked September 27; this is not a review of paid lessons or assessment questions.

| Resource | Access | Estimated time |
|---|---|---:|
| Official self-paced path | Free | Now 4 modules; prior 4h31 estimate is not verified for this revision |
| AB-730T00-A instructor-led course | Paid or partner-sponsored | 1 day |
| Microsoft Practice Assessment | Free | 45–75 minutes per attempt plus review |
| Microsoft exam-prep video | Free | Public page retrieved; runtime/video content not independently reviewed |
| Pluralsight AB-730 path | Paid | 3 rounded hours / 2 courses (3h01 summed); path still in production |
| O'Reilly AB-730 Crash Course | Paid | About 3 hours of agenda plus breaks/exercises |
| MeasureUp AB-730 | Paid | 110 questions; allow 5–8 hours across remediation |
| Udemy Scott Duffy practice | Paid | Earlier 100-question listing; current retrieval blocked |
| Partner Skilling Hub | Partner-restricted | Event-specific; verify signed-in start/end times |

- **Primary route:** [Microsoft Learn AB-730T00](https://learn.microsoft.com/en-us/training/courses/ab-730t00) and the linked [Enhance business workflows with AI path](https://learn.microsoft.com/en-us/training/paths/transform-business-workflows-with-ai/). It now lists four modules: content, data/visuals, meetings/collaboration, and Cowork. It is no longer the earlier six-module listing; use the full course and objective map to identify remaining fundamentals and prompt-management needs.
- **Readiness:** [free official Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/ai-business-professional/practice/assessment?assessment-type=practice&assessmentId=650120434&practice-assessment-type=certification) and [official AB-730 prep video](https://www.youtube.com/live/T_Y3GTEb8pY). Use the assessment diagnostically; investigate every miss in first-party documentation.
- **Structured subscription path:** [Pluralsight AB-730](https://www.pluralsight.com/paths/ab-730-ai-business-professional) now lists Vlad Catrinescu's 1h16 fundamentals course (August 22) and 1h45 prompt/conversation course (September 11), plus a practice exam. The path remains in production and its three-domain description does not establish complete October coverage.
- **Live guided preparation:** [O'Reilly AB-730 Crash Course](https://www.oreilly.com/live-events/microsoft-ai-business-professional-ab-730-crash-course/0642572353940/0642572353933/) by Renaldi Gondosubroto has a 180-minute teaching/exercise agenda plus breaks. It still describes three domains and custom-agent construction; verify October coverage, the actual event date and local start/end time before enrolling.
- **Paid assessment:** [MeasureUp AB-730](https://www.measureup.com/microsoft-ab-730-ai-business-professional-practice-test.html), 110 questions released June 2026. Its generic overview text incorrectly mentions Azure AI workloads, while its detailed mapping follows the earlier three-domain AB-730 scope. Neither establishes coverage of the new October agent domain; verify revision coverage before purchase.
- **Previously listed additional assessment:** [Udemy AB-730 practice by Scott Duffy and Jordi Koenderink](https://www.udemy.com/course/ab730-tests/), previously listed 100 questions and an August 2026 update mapped to July 22. Current retrieval was blocked; treat those as historical observations and recheck before buying.
- **Partner-restricted learning:** [Partner Skilling Hub](https://www.skilling-hub.com/en-US); sign in to confirm current AB-730 delivery, exact start/end times, seats, and prerequisites.

No exact Whizlabs AB-730 product was independently verified in the earlier September 1 catalog review; this deep review did not establish a new product listing. Avoid unusually large banks, “real questions,” pass guarantees, or content that claims to mirror live questions. A small set of original scenarios plus hands-on Copilot use is more useful than memorizing hundreds of unsupported answers.

---

## Useful blog reading with an exercise

- [Introducing Copilot Home, Code and Autopilot](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/) — Jared Spataro, September 25, 2026. Classify a lookup, a delegated brief and recurring work by required context, actions and supervision. The article announces staged Frontier/private previews; it does not establish that Home, Code or Autopilot is available in your tenant or add those product names to AB-730's objectives.
- [Work IQ business and workplace intelligence](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/09/25/work-iq-business-and-workplace-intelligence-in-the-flow-of-work/) — James Oleinik, September 25, 2026. Draw a renewal-evidence table linking opportunity, unresolved case, contract and customer message; identify the missing source or approval that would change the recommendation. The described business-app preview starts September 30 and rolls through October, with Finance/Operations planned for late October. Use a tabletop exercise until your environment has the supported feature.

Both public article texts were read. Marketing performance claims, videos, customer deployments and preview access were not independently validated. Use their scenarios to ask better questions, then verify feature behavior in current product documentation.

---

## Final readiness checklist

- [ ] I can explain how context, grounding, permissions, app choice, chat, agents, Researcher, Analyst, Pages, and Notebooks affect a result.
- [ ] I can identify fabrication, injection, over-reliance, oversharing, bias, privacy/copyright, and stale-context risk and choose verification.
- [ ] I can create, iterate, save, schedule, share, and retire a prompt with goal, context, sources, expectations, owner, and test evidence.
- [ ] I can manage chat history and curate a notebook without carrying irrelevant or sensitive context forward.
- [ ] I can choose Agent Store or a custom template agent, then configure knowledge, settings, suggestions, tests, sharing, and escalation.
- [ ] I can draft and transform documents, create management summaries, and validate Researcher and Analyst results.
- [ ] I can move insight across Microsoft 365 apps without losing provenance, permissions, labels, meaning, or approval.
- [ ] I can use meetings, Pages, memory, and instructions while preserving participant, audience, and human-accountability boundaries.
- [ ] I can explain connector freshness, model selection, notebook sharing, meeting capture and Cowork approval/retry boundaries.
- [ ] For October preparation, I can apply a prebuilt agent, find its chats, choose a skill, supervise a delegated task and manage its schedule.
- [ ] I completed the three scenarios, ten labs, and 44 original checks without using exam dumps, or recorded unavailable environment steps honestly.
- [ ] I rechecked the official blueprint, Practice Assessment, credential lifecycle, and product availability immediately before scheduling.
