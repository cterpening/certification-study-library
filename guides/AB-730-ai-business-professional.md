---
exam_code: AB-730
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-730
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# AB-730 AI Business Professional Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide was checked against the July 22, 2026 objectives and cited public sources on September 1, 2026. It may still contain errors or become outdated. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ab-730-coverage-record). The [official AB-730 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-730) is authoritative.

**Current baseline:** Skills measured as of July 22, 2026.<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 1, 2026.<br>
**Lifecycle:** The [AI Business Professional credential](https://learn.microsoft.com/en-us/credentials/certifications/ai-business-professional/) and 45-minute exam are active.<br>
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
| App Copilot | Work grounded in the active Word, Excel, PowerPoint, Outlook, or Teams context | Each app exposes different capabilities; do not assume feature parity |
| Agent Store agent | A discoverable prebuilt or organization-published agent already fits the task | Review publisher, knowledge, capabilities, sharing, and approved use |
| Custom agent | A repeatable, bounded task needs tailored instructions, knowledge, suggested prompts, or capabilities | Build only when an existing agent does not fit; test and share deliberately |
| Researcher | Multistep research and synthesis across allowed sources with an evidence trail | Inspect citations, source quality, omissions, and recency |
| Analyst | Deeper data reasoning, calculations, analysis, and visual exploration | Validate input shape, assumptions, computations, and business interpretation |
| Copilot Page | Editable, shareable canvas that turns a response into collaborative content | Sharing the page can broaden the audience; verify content and access |
| Notebook | Persistent project context that collects conversations and sources | Curate source scope, remove stale material, and understand who can access it |

A chat responds inside a conversation. An agent has a more durable purpose, instructions, knowledge, capabilities, and sharing boundary. Create an agent when a repeated task needs controlled reuse; do not create one merely to rename a prompt. **VERIFY CURRENT:** agent availability, Agent Store content, Researcher/Analyst capabilities, Pages/Notebooks behavior, licensing, regions, sharing, and supported apps change frequently.

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

### Save, schedule, and share prompts safely

Save a prompt when the task repeats and the prompt is worth curating. Give it a meaningful title and remove case-specific sensitive content. Retest it with different representative inputs. Schedule a prompt only when the source availability, timing, recipient, review step, and output destination are appropriate for unattended recurrence. A scheduled prompt that generates a weekly report still needs ownership and exception handling.

Share a prompt when colleagues can legitimately use its instructions and sources. Explain prerequisites, expected references, limitations, and verification. Sharing the words of a prompt does not necessarily share source access, licensing, or identical context; recipients can receive different results. Avoid embedding secrets, personal data, customer details, or inaccessible file paths.

**VERIFY CURRENT:** Prompt Gallery naming, save/share/schedule availability, supported licenses and experiences, recurrence options, sharing scope, and organizational controls.

### Manage conversation history and notebooks

Find a previous conversation when its context remains useful and authorized. Rename it so purpose and sensitivity are recognizable. Delete a chat when it is erroneous, obsolete, unnecessarily sensitive, or no longer required—subject to organizational retention and eDiscovery policies. Deleting from the user's visible history is not a promise that every compliance record disappears.

Start a new chat when prior context would confuse or contaminate the next task. Keep one conversation when iterative context is intentional. Before continuing an old conversation, inspect its sources, assumptions, audience, and date.

Add a conversation to a notebook when it belongs to a durable project context with curated sources and repeated work. A notebook is not a dumping ground for every related chat. Remove stale or contradictory material, organize it around the project outcome, and review access before adding sensitive content.

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

Memory and instructions can personalize recurring responses. Use them for durable preferences—role, style, recurring context—not secrets or assumptions that should be revalidated. Inspect, update, or remove stale instructions. State task-critical constraints in the current prompt rather than trusting memory alone. **VERIFY CURRENT:** memory behavior, user controls, supported licenses/regions, source interaction, retention, and organizational administration.

> **Related item:** The value of Copilot is a better business outcome, not maximum generated volume. Measure time saved together with correction rate, decision quality, adoption, risk, accessibility, customer or employee impact, and rework.

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
8. **Meeting/collaboration:** Use a synthetic meeting transcript to create decisions and actions, verify attribution, publish a sanitized Copilot Page, and review memory/instruction effects.

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

---

## Places to learn

This is a selective starting set, not a complete list and not a requirement to consume everything. Pick the explanation, hands-on practice, and assessment style that works for you, and map every exam resource to the July 22, 2026 blueprint.

| Resource | Access | Estimated time |
|---|---|---:|
| Official self-paced path | Free | 4h31 listed; 8–15 hours with practice |
| AB-730T00-A instructor-led course | Paid or partner-sponsored | 1 day |
| Microsoft Practice Assessment | Free | 45–75 minutes per attempt plus review |
| Microsoft exam-prep video | Free | About 1 hour; verify current runtime |
| Pluralsight AB-730 path | Paid | 1h16 published now plus practice exam; path in production |
| O'Reilly AB-730 Crash Course | Paid | About 3 hours of agenda plus breaks/exercises |
| MeasureUp AB-730 | Paid | 110 questions; allow 5–8 hours across remediation |
| Udemy Scott Duffy practice | Paid | 100 questions; allow 4–7 hours with source review |
| Partner Skilling Hub | Partner-restricted | Event-specific; verify signed-in start/end times |

- **Primary route:** [Microsoft Learn AB-730T00](https://learn.microsoft.com/en-us/training/courses/ab-730t00) and its [six-module path](https://learn.microsoft.com/en-us/training/paths/transform-business-workflows-with-ai/), covering fundamentals, Copilot Chat, drafting/Researcher, analysis/Analyst, meetings/Pages/Notebooks, and three business workflows.
- **Readiness:** [free official Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/ai-business-professional/practice/assessment?assessment-type=practice&assessmentId=650120434&practice-assessment-type=certification) and [official AB-730 prep video](https://www.youtube.com/live/T_Y3GTEb8pY). Use the assessment diagnostically; investigate every miss in first-party documentation.
- **Structured subscription path:** [Pluralsight AB-730](https://www.pluralsight.com/paths/ab-730-ai-business-professional) currently contains Vlad Catrinescu's 1h16 fundamentals course and a practice exam, with the remaining two domains explicitly in production as of review.
- **Live guided preparation:** [O'Reilly AB-730 Crash Course](https://www.oreilly.com/live-events/microsoft-ai-business-professional-ab-730-crash-course/0642572353940/0642572353933/) with an agenda totaling about three hours of domain instruction/exercises plus breaks; verify the listed event date and local start/end time before enrolling.
- **Paid assessment:** [MeasureUp AB-730](https://www.measureup.com/microsoft-ab-730-ai-business-professional-practice-test.html), 110 questions released June 2026. Its generic overview text incorrectly mentions Azure AI workloads, while its detailed objective mapping matches AB-730; rely on the official blueprint for scope.
- **Current additional assessment:** [Udemy AB-730 practice by Scott Duffy and Jordi Koenderink](https://www.udemy.com/course/ab730-tests/), 100 questions, updated August 2026 and explicitly mapped to the July 22 update. Use explanations as leads and verify them against first-party sources.
- **Partner-restricted learning:** [Partner Skilling Hub](https://www.skilling-hub.com/en-US); sign in to confirm current AB-730 delivery, exact start/end times, seats, and prerequisites.

No exact Whizlabs AB-730 product was independently verified in the public catalog during review. Avoid unusually large banks, “real questions,” pass guarantees, or content that claims to mirror live questions. A small set of original scenarios plus hands-on Copilot use is more useful than memorizing hundreds of unsupported answers.

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
- [ ] I completed the three scenarios, eight labs, and 36 original checks without using exam dumps.
- [ ] I rechecked the official blueprint, Practice Assessment, credential lifecycle, and product availability immediately before scheduling.
