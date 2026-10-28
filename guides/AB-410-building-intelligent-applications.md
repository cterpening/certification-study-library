---
exam_code: AB-410
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-410
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: review-required
last_verified: 2026-10-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-10-28
---

# AB-410 Building Intelligent Applications Study Guide

> **Independent AI-assisted resource — HUMAN REVIEW PENDING.** The October 28, 2026 team refresh reconciles this complete guide and detailed objectives with current public exam, product and learning evidence. See the [current group report](../docs/research/2026-10-28-microsoft-refresh-group-05.md#ab-410) and [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ab-410-coverage-record). Source limits and unexecuted exercises remain explicit. This is not human review or live product validation. The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-410) is authoritative.

**Current baseline:** Official study guide last updated October 16, 2026; Microsoft does not publish a separate skills-effective date on this blueprint. The 48 detailed objectives match the accepted objective wording.<br>
**Upcoming blueprint change:** None announced on the official study guide as of October 28, 2026.<br>
**Lifecycle:** The 120-minute exam, currently listed in 13 languages, and [Intelligent Applications Builder Associate credential](https://learn.microsoft.com/en-us/credentials/certifications/intelligent-applications-builder-associate/) are active. The adjacent Power Platform Functional Consultant Associate credential [retired August 31, 2026](https://learn.microsoft.com/en-us/credentials/support/credential-retirement); Microsoft's [retired-course catalog](https://learn.microsoft.com/en-us/credentials/certifications/retired-courses) names AB-410T00 as the replacement for the retired PL-200T00 course, not as a one-to-one replacement statement for every PL-200 credential outcome.<br>
**Official source:** [AB-410 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-410)

## How to use this guide

AB-410 tests whether you can turn a business process into a governed, usable, AI-enabled Power Platform solution. Do not study canvas apps, Dataverse, flows, prompts, and agents as separate feature lists. For every requirement, trace:

1. the user, desired outcome, process state, data owner, and acceptance measure;
2. the smallest suitable app, automation, built-in agent, prompt, model, or extension;
3. the Dataverse tables, relationships, calculated behavior, and access model;
4. where deterministic rules end and probabilistic AI begins;
5. the user or connection identity, data policy, and human decision point;
6. the solution, environment-specific configuration, deployment path, and rollback plan;
7. accessibility, performance, monitoring, testing, and adoption evidence.

Build a small solution in a disposable developer environment. Use both a model-driven app and a responsive canvas app, call a cloud flow, build a grounded prompt, and move the solution into a second environment. The exam targets an app builder who collaborates with administrators, governance teams, agent developers, architects, and business stakeholders—not a tenant administrator or professional-code developer working alone.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

### Living-guide watch — September 28, 2026

The [September 28 deep review](../docs/research/2026-09-28-ab-410-deep-review.md) maps **48 unchanged detailed objectives**. The accepted snapshot's presentation was normalized after comparison; historical evidence bytes remain archived. That September 28 review introduced six worked examples, ten labs and 48 answered checks. Its validation used offline arithmetic, sets and synthetic records. The October 28 worked additions are source-based proposed workflows; no tenant, flow, Power Fx runtime, model, deployment or paid lesson was executed for this refresh.

The prompt-knowledge documentation contains an unresolved SAP support discrepancy: its connector instructions mention SAP, but its limitations list omits it. Treat that path as unverified rather than promising support. Other listed connectors still require their documented execution context and permissions.

Before following an older Power Apps, Power Automate, or Power Virtual Agents exercise, check Microsoft's [Power Platform deprecation ledger](https://learn.microsoft.com/en-us/power-platform/important-changes-coming). For current agent-building terminology, compare the blueprint with the [GitHub Copilot Harness agent overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/overview). A renamed surface or retired client does not by itself change the underlying exam objective; record the current object, supported replacement, and security boundary.

Future business-application features now move to the [AI at Work roadmap](https://www.microsoft.com/en-us/microsoft-365/roadmap) under the [September 2026 transition](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/08/25/one-always-on-roadmap-dynamics-365-power-platform-and-dataverse-join-the-ai-at-work-roadmap/). Treat roadmap dates as volatile planning evidence. The independent courses listed later are useful for a second explanation and guided build, but their screenshots and names require validation against Microsoft Learn.

The deprecation ledger records the Power Automate mobile app's August 31 retirement and the maker portal's PVA help-chatbot removal from September 9. Existing cloud flows continue; use current Teams, web or Power Apps mobile paths as appropriate. An old tutorial's client or help surface is not proof that its underlying flow capability retired.

## Objective map

| Published domain | Weight | Central question |
|---|---:|---|
| Create a foundation for intelligent applications | 25–30% | Can the requirement become a secure, supportable component and data design? |
| Create intelligent applications | 25–30% | Can users complete the process through accessible, performant model-driven and canvas experiences? |
| Build business application logic and automation | 40–45% | Can flows, prompts, models, columns, rules, and processes produce controlled outcomes? |

---

## 1. Create a foundation for intelligent applications

### Start with outcome, process, data, and risk

Describe the business outcome before selecting a product. Identify actors, trigger, inputs, decisions, state transitions, exceptions, evidence, owner, data classification, volume, latency, and consequence of a wrong result. Separate tasks that must be deterministic from tasks where AI can draft, classify, summarize, or recommend. A generative response should not silently become an approval, entitlement, payment, legal conclusion, or destructive update.

Map each process step to the smallest sufficient component:

| Need | Likely component | Validate before choosing |
|---|---|---|
| Structured internal process centered on related Dataverse records | Model-driven app | Table model, forms/views, privileges, mobile needs, and whether the metadata-driven UX is sufficient |
| Tailored internal experience or multiple data sources | Canvas app | Responsive layout, delegation, connector policy, accessibility, and maintenance cost |
| External or partner self-service | Power Pages | Authentication, web roles/table permissions, privacy, anonymous access, capacity, and threat model |
| Event, schedule, approval, or cross-service orchestration | Power Automate cloud flow | Trigger semantics, connection identity, DLP, retries, duplicate effects, timeout, ownership, and monitoring |
| Common classification, extraction, prediction, or document task | Built-in AI Builder model | Input quality, supported language/region, capacity, accuracy evidence, and human-review threshold |
| Controlled generation over instructions and knowledge | AI Builder prompt | Grounding, inputs/outputs, model settings, unsafe or incorrect output, evaluation, and cost |
| Conversational, multi-turn, knowledge/tool-using interaction | Copilot Studio agent | Channel, authentication, topics/tools/knowledge, escalation, governance, evaluation, and lifecycle |
| Unsupported capability behind a stable contract | Custom connector or coded extension | Whether the requirement truly exceeds low-code scope; authentication, API lifecycle, support, and ALM |

The blueprint asks you to evaluate built-in agents. First determine what the currently available agent does, its supported data and actions, required licensing/capacity, identity, environment, and governance surface. Compare that with extending an app or flow and with building a Copilot Studio agent. Product names and availability change quickly; choose from the current documented capability, not a launch-demo memory. **VERIFY CURRENT:** built-in agent names, regions, preview/GA state, license and capacity requirements.

> **Related item:** A process map exposes where an agent should stop. Mark human approval, exception, audit, safety, and irreversible-action boundaries before giving an agent tools.

### Recommend an environment and governance boundary

An environment separates apps, flows, connections, agents, and usually a Dataverse database within an Entra tenant and geographic location. The [environment overview](https://learn.microsoft.com/en-us/power-platform/admin/environments-overview) distinguishes production, sandbox, trial, developer, default, and Dataverse for Teams environments.

- Use a personal developer environment for isolated maker development, not a shared production workload.
- Use sandbox environments for shared development, test, user acceptance, training, copy/reset, and release validation.
- Use production for durable business workloads with operating ownership, security, capacity, backup, and release controls.
- Treat trial as temporary and expiry-bound.
- Treat the tenant default environment as broadly accessible personal productivity space, not the automatic home for a critical application.
- For new Teams-integrated work, choose an appropriate full Dataverse environment and add the app to Teams. **VERIFY CURRENT — October 28, 2026:** the [Power Platform deprecation ledger](https://learn.microsoft.com/en-us/power-platform/important-changes-coming) ends creation of new Dataverse for Teams environments on **November 15, 2026**. Existing environments that remain unupgraded are suspended **September 15, 2027** and decommissioned **October 30, 2027**. Inventory existing apps/data and plan an upgrade or supported move, including capacity and user licensing, before the applicable cutoff.

Recommend the type together with region/data residency, security group, Dataverse requirement, capacity, licensing, DLP, managed-environment rules, backup/recovery, release ring, and maker/admin ownership. Environment roles do not automatically grant Dataverse data access; Dataverse security must be designed separately.

### Apply a solution and ALM strategy

A solution is the transport and dependency boundary for tables, apps, flows, prompts, models, connection references, environment variables, and other components. Develop in an unmanaged solution, export a managed build for downstream test and production, and keep source control and release evidence. A managed solution discourages direct downstream customization; it does not eliminate operational change or supply a data rollback automatically.

Use environment variables for values that vary by destination, such as URLs or IDs. Use connection references for solution-aware connector bindings. Do not store secrets in ordinary solution configuration. Identify dependencies—especially data, connections, prompt/model assets, flows called by apps, and agent references—and validate activation and permissions after import.

A defensible release path has separate development, test, and production environments; a versioned solution; deployment settings; connection ownership; predeployment checks; smoke, security, accessibility, AI-evaluation, and regression evidence; approval; and rollback or forward-fix. [Power Platform pipelines](https://learn.microsoft.com/en-us/power-platform/alm/pipelines) can govern promotion, but the team must still define what evidence makes a release acceptable.

Pipelines promote the same exported artifact sequentially; they do not re-export changed development work at each stage. Table data is outside the solution package. Reconcile connection identity and target configuration separately, and preserve a data-recovery plan. The host can be an unmanaged production environment; developer environments have different requirements from other pipeline environments, which require Managed Environments and the corresponding use rights. Avoid interpreting “managed solution” and “Managed Environment” as the same control.

> **Related item:** AI behavior is a release dependency even when the app metadata did not change. Model availability, grounding data, prompt version, content filters, capacity, and service behavior need evaluation and monitoring alongside conventional app changes.

### Build a Dataverse model from business meaning

Start with business entities, stable identifiers, lifecycle, ownership, relationships, retention, and access—not with a spreadsheet's current columns. Reuse a standard table when its meaning and behavior fit; create a custom standard table when the business concept is distinct. Configure display and plural names, primary name, ownership, activities, notes/attachments, auditing, duplicate detection, search, and other properties deliberately.

Select column types for the meaning and operations required: text, number, currency, date/time, choice, lookup, customer, file/image, yes/no, or calculated/derived behavior. Requiredness improves entry quality but is not a complete integration or security control. Stable external identifiers can use alternate keys where appropriate. Avoid duplicate representations of the same concept merely to simplify one screen.

Relationships express cardinality and navigation:

- one-to-many / many-to-one uses a lookup on the many side;
- many-to-many uses an intersect relationship when the association has no attributes of its own;
- use a separate association table when the relationship needs dates, status, quantity, role, evidence, or its own security/lifecycle;
- review cascade behavior before allowing parent assign, delete, reparent, share, or unshare to affect children.

Use public views for reusable record queries and columns. Use main forms to organize the complete record experience; consider required data, tabs/sections, related data, business process, accessibility, role access, and performance. The app's forms and views do not replace table privileges or row access.

#### Worked build — request data before app screens

In a disposable Dataverse environment, open the data workspace and start a blank **Service Request** table. Choose user/team ownership for requests assigned to staff; add a short-text reference, a choice for triage state and a date/time received column. Add the existing Account table, then create a supported many-to-one lookup from each request to its customer. Save the schema and add three synthetic rows; one customer must relate to two requests. Reopen the table and change its description, rather than creating a second copy when the name is imperfect.

The [table authoring procedure](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entities-portal) distinguishes new and existing objects: removing a new table from this workspace can delete its rows, while removing an existing table from the workspace only removes its diagram representation. **VERIFY CURRENT:** the workspace does not support every column or relationship type, including many-to-many creation. Use the appropriate full table designer for an unsupported change. Extending a customizable standard table differs from creating a new custom table of standard type; preserve the existing table's business meaning and managed restrictions.

Check schema and row access separately: a customizer can author metadata without access to every customer record. Evidence is the saved column types/properties, correct lookup cardinality and actual nonadministrator data access, not the diagram alone.

### Distinguish prompt columns, row summaries, and deterministic columns

A prompt column uses generative AI to produce content from its configured instructions and row context. A row summary produces an AI-generated summary of the record. Both are probabilistic: source data can be incomplete or malicious, output can be wrong, and behavior can change. Define what input is included, who may see the source and output, when generation occurs, how stale output is handled, and whether a user must verify it.

Calculated, rollup, and formula columns are deterministic alternatives for supported calculations and aggregations. Do not use a prompt to calculate a contractual amount or an SLA deadline that a formula can produce consistently. Do not use a deterministic formula when the task genuinely requires summarizing unstructured text—but retain the source and label the generated result.

The [prompt-column procedure](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/prompt-column) describes persisted output generated on creation or referenced-input updates. Editing the prompt does not backfill existing values; on-demand execution is unsupported and prompt columns are not audited. Inspect the paired Status/Details fields: codes **2000/2001** mean execution was skipped despite the “Completed” label. Formula, file, image and prompt columns are unsupported inputs. Check both environment and column execution settings. Preserve separate review/provenance evidence where needed.

[Row summaries](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/configure-form-row-summary) require AI insight cards, apply across the table's main forms/views, and need explicit language input/instructions for user-language output. Case, Lead and Opportunity use their Dynamics-specific summaries instead. Move custom summaries through **AI Skill Config**, excluding System-owned rows. Summary text is unsuitable for authoritative arithmetic/date decisions and may misrepresent calculated values; show the source value separately.

### Worked example 1 — “Completed” is not the same as fresh output

A synthetic batch has 100 rows: 40 with status 2, 35 with 2000, 10 with 2001, 10 failed and five still running. A dashboard grouping the three “Completed” codes reports **85 completed**, but only **40** have a newly successful generation in this batch. Of that dashboard group, **40/85 = 47.06%** represent fresh successes. Validate timestamps, inputs and output quality before use. The counts do not establish credit consumption, because failed/skipped work and billing have separate rules.

### Configure Dataverse security as layered authorization

Environment access, app sharing, Dataverse security roles, teams, business units, record ownership/sharing, hierarchy behavior, and column security combine to determine effective access. Define least-privilege table permissions—create, read, write, delete, append, append to, assign, and share—at the appropriate user, business-unit, parent-child, or organization depth.

Owner teams can own records and hold roles. Entra group teams can map directory group membership to Dataverse access. Access teams support record collaboration without owning the record. Column security can restrict sensitive columns, but it is not a substitute for minimizing data collection or separating a highly sensitive entity.

Test with representative personas rather than the maker's System Administrator identity. Verify environment entry, app visibility, table privilege, row scope, form/view availability, field access, flow/connector behavior, and AI source/output access. If a generated summary exposes data a user could not otherwise read, the design has failed even if the app opens.

[Column security](https://learn.microsoft.com/en-us/power-platform/admin/field-level-security) applies across data requests, but System Administrators bypass it. Test with a nonadministrator. Read, read-unmasked, create and update permissions are separate; masking a value does not remove every possible disclosure through derived output. Secure generated or aggregate columns explicitly when their content reveals protected inputs.

---

## 2. Create intelligent applications

### Build a model-driven app from the data model

Model-driven apps are metadata-driven: tables, relationships, forms, views, navigation, commands, charts, dashboards, security, and business process create the experience. Compose the app around user tasks rather than placing every table in navigation.

Configure main, quick create, quick view, and card forms only where their interaction fits. Organize main forms with tabs and sections; make essential content discoverable, remove unused fields, and avoid too many subgrids or scripts. Multiple forms can support personas, but assigning a form to a role affects experience—not underlying authorization.

Public views define shared columns, sort, filter, and default presentation. Keep them selective and useful for the task. Charts visualize view data; dashboards combine charts, lists, and other components. Validate filter semantics and security-trimmed results instead of assuming a visual total is universal.

Generative pages use natural language to create page starting points. Treat generated content like code or configuration produced by an assistant: review the data access, formulas, components, responsiveness, accessibility, security, errors, performance, and maintainability before publishing. Natural-language creation accelerates drafting; it does not transfer accountability.

The [current generative-page procedure](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/generative-pages) separates browser authoring in the United States, Great Britain, Australia and Singapore from external-tool authoring across public clouds. Connectors and explicit custom-API calls are preview; bindings and signed-in-user authorization still matter. A form can pass `recordId` into a page, but an ID is not an access grant. Package the app, sitemap and UX Agent Project dependencies; only the first prompt and published code move, not the full editing conversation/history. Older preview pages need the documented migration. Keep source/review history separately and check all pending app changes before publishing.

To grant access, share or assign the model-driven app as appropriate and give the user security roles that provide necessary table privileges. Also review form and view role restrictions. Diagnose each layer separately when a user can see the app but cannot open or edit its records.

#### Worked build — a triage app and its evidence

For Service Request, edit a main form to place customer, triage state and received time together. Create a public **Open requests** view with an explicit open-state filter, customer/state/received columns and oldest-received-first sorting. Save and publish the changed components. In the app designer, add the table page and only the intended forms/views; arrange navigation around intake and triage. Save, publish and reopen the released app. These are separate designers within the [model-driven construction workflow](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/model-driven-designers).

Create a system chart with customer as the category and a **count** of request records as the series; choose a column chart, save and publish. Add it and the open-request list to a dashboard and include that dashboard in the app. If a newly published chart is absent, check the app's selected chart assets as well as publication. The [chart procedure](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-edit-system-chart) also distinguishes the preview view from a permanently fixed chart filter.

With synthetic records, predict each customer's open count before opening the chart. Test two least-privilege roles: each must see the correct form/view and only its authorized records. A count disagreeing with the prediction calls for checking view filter, aggregate, selected assets and effective record access separately. **VERIFY CURRENT:** designer controls and publication surfaces can change; this is a proposed workflow, not an executed build.

### Build a canvas app that remains usable and correct

Canvas apps give explicit control over screens, controls, layout, formulas, and data sources. Create from data when that gives a useful starting point, then refactor for business tasks. Use responsive containers and formulas rather than fixed coordinates for every device. Test narrow, wide, landscape, portrait, zoom, keyboard, and screen-reader paths.

Accessibility work includes semantic labels, logical tab order, visible focus, adequate contrast, noncolor status cues, captions or alternatives, sufficiently large targets, and error messages associated with the relevant input. Do not hide required operations behind hover, drag, or an unlabeled icon.

Performance and correctness meet at delegation. A delegable query executes at the source over the complete set. A nondelegable operation can return a plausible answer from only a local subset. Fix delegation warnings by using supported functions/filters, reshaping the data or query, or explicitly bounding the business set—not by only raising the row limit. Minimize repeated connector calls, large collections, unnecessary controls, startup work, and chatty formulas.

The [delegation overview](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview) documents a default local limit of **500**, configurable to **2,000**. Support depends on the connector and complete expression. Collections can conceal an incomplete source load; a collection's successful local filter does not prove that every source row was retrieved.

#### Worked build — data, selection and a verified save

Create a blank canvas app, add Service Request as a Dataverse data source and place a browse gallery and edit form in responsive containers. Set the gallery's Items to the table, the form's DataSource to that table and its Item to the gallery's selected record. Choose the required fields. A new-request action switches the form to New; a save action submits that form. Put the reset/new-record transition on the form's **OnSuccess**, and put a useful message on **OnFailure**, so a failed submission does not clear the user's input. The [data-to-form/gallery tutorial](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/add-editable-tables) demonstrates these control/data bindings; retain explicit successful-save handling rather than assuming chained actions wait for asynchronous persistence.

Create one synthetic request, select it, change its state and reopen it from the source. Deny a test persona write permission: the expected result is a clear failure and retained input, not a success banner. Repeat with a narrow screen and keyboard. A gallery refresh alone is not proof that a save reached Dataverse.

### Worked example 2 — A plausible gallery can miss most matches

In a synthetic ordered set of 5,000 requests, 400 match the business condition. The first 500 contain 80 matches, and the first 2,000 contain 180. Local filtering therefore finds **20%** or **45%** of the true matches. Raising the limit improves this example while still missing 220 records. Prove a supported delegated query or an explicitly complete bounded dataset; neither loading animation nor a fast gallery establishes completeness.

Usability means users can identify state, required action, save progress, recover from failure, and understand AI-produced content. Disable or protect duplicate submission, show flow progress, distinguish draft from approved state, and use confirmations for destructive actions. Validate under realistic latency and data volume.

### Reuse formulas and components deliberately

Use named formulas for app-level values and reusable expressions whose dependencies should recalculate declaratively. Use user-defined functions for explicit reusable calculation contracts. Use components for reusable UI/behavior inside an app and component libraries to share maintained components across apps. Keep inputs, outputs, accessibility behavior, error states, dependencies, and version expectations clear.

Variables store state:

- global variables, set with `Set`, span the app session;
- context variables, set with `UpdateContext` or navigation, are screen-oriented;
- collections are in-memory tables useful for bounded working state and offline-like interaction, not an automatic mirror of a large source;
- declarative formulas are preferable when state does not actually need to be stored.

State becomes stale and hard to debug. Use the narrowest scope and a clear update path. Never rely on client variables or hidden controls for authorization.

The [App.Formulas reference](https://learn.microsoft.com/en-us/power-platform/power-fx/reference/object-app) distinguishes immutable definitions that recalculate from stored variables. UDFs add typed parameters/returns; behavior UDFs have explicit side effects. User-defined types can describe records/tables. Keep calculation functions pure where possible and validate data at the boundary. `App.OnError` reports an error after it has occurred; it cannot substitute a value or undo prior effects.

#### Worked choice — one calculation and one reusable experience

Define a named formula for a value derived from existing controls, such as `LineTotal = Value(QuantityInput.Text) * Value(UnitPriceInput.Text);` in App.Formulas, then bind two labels to `LineTotal`. Changing either input should update both consumers without an extra Set call. If several call sites need parameters, define a typed calculation UDF, for example `LineAmount(qty: Number, price: Number): Number = qty * price;`, and call it with explicit numeric values. Validate text-to-number conversion at the input boundary. These illustrate the [named-formula and UDF contract](https://learn.microsoft.com/en-us/power-platform/power-fx/reference/object-app); verify current syntax, type support and feature availability in the target environment.

For a repeated status banner, create a component with explicit label/status inputs, accessible output and an error state. Replace two copied banners with instances; if several apps need the same maintained banner, publish it through a component library and review an update before adopting it in each app. The formula calculates; the component packages an interaction. A shared library does not automatically update every consuming app or authorize data access. Compare a valid value, missing input and invalid number, and record which layer owns each correction. No formula runtime or library deployment was executed for this review.

### Automate from the app and handle failures

A canvas app can call a cloud flow for approvals, connectors, AI processing, or orchestration. Define input and output types, caller versus connection identity, maximum wait, user feedback, safe retry, and duplicate handling. Long-running work should create a tracked request and complete asynchronously rather than holding an interactive call open.

Use `IfError`, `Errors`, validation, and connector/flow result checks to handle expected failures. Give the user an actionable message without exposing secrets or internal details, and log a correlation value for support. Decide whether partially completed work must be compensated, retried, or left for an operator.

The [IfError reference](https://learn.microsoft.com/en-us/power-platform/power-fx/reference/function-iferror) explains why semicolon-chained writes can continue after an earlier failure. Put dependent steps behind explicit success handling and keep return types compatible. Error handling does not make writes to separate systems transactional: a successful first write still needs reconciliation if the second fails.

Use [Live Monitor](https://learn.microsoft.com/en-us/power-apps/maker/monitor-overview) during authoring and published-app troubleshooting to inspect events, formulas, data calls, errors, and performance. Reproduce as the affected role with representative data. A maker-only success does not prove the released app.

### Create an agent from a canvas app with a controlled boundary

The blueprint includes creating a Copilot Studio agent from a canvas app. Define what the agent knows, can do, and must hand off. Review authentication, end-user identity, channels, knowledge sources, tools/actions, conversation state, DLP, sharing, capacity, evaluation, and escalation. The surrounding app's security does not automatically prove that every agent tool and knowledge source enforces equivalent access.

The [app-to-agent procedure](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/agent-builder) extracts metadata and convertible actions from a **canvas app**, then requires review and Copilot Studio testing/publishing. Missing connections can leave actions absent. Its prerequisites include Dataverse, the publish-AI setting, a supported Copilot Studio solution version and allowing unmanaged customization in the authoring environment. Do not weaken production controls to reproduce a tutorial.

Keep that creation route distinct from [Copilot Studio harness selection](https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview). Current GitHub Copilot harness agents and standard agents cannot simply be transferred between harnesses. The name identifies Copilot Studio technology; it does not imply that the agent runs in the GitHub Copilot service. Verify the chosen harness's tools, billing and publishing support.

Test benign, ambiguous, unsupported, sensitive, adversarial, and prompt-injection inputs. Verify citations or grounding where available, authorization for every action, confirmation before consequential operations, and a useful fallback when confidence is low. Monitor task success, unsafe output, tool failures, latency, cost, and human escalation—not just whether the agent produced fluent text.

> **Related item:** Power Pages is part of the expected experience profile and the official learning course, even though the measured implementation bullets concentrate on model-driven and canvas apps. Know when external identity, web roles, and table permissions make Power Pages a better channel, and when a conventional authenticated app is safer.

---

## 3. Build business application logic and automation

### Choose the cloud-flow trigger and connection model

Use an automated trigger for an event, an instant trigger for a user or app request, and a scheduled trigger for time-driven work. For Dataverse events, define table, change type, scope, selected/filter columns, and any expression that prevents irrelevant runs. A broad trigger followed by a condition wastes capacity and increases duplicate/concurrency risk.

For the [Dataverse row trigger](https://learn.microsoft.com/en-us/power-automate/dataverse/create-update-delete-trigger), Select columns detects inclusion in an update request, even if the value is unchanged. It is update-only and does not support lookup columns or virtual tables. Filter rows evaluates the saved row; omit the API-style `$filter=` prefix. Scope, action connection and Run As are distinct: a team-owned row using the row-owner option falls back to the flow owner. Trace the effective identity for every action.

Evaluate connectors for supported operations, authentication, connection owner, DLP group, premium/custom licensing, region, throttling, pagination, schema, retry behavior, and support lifecycle. A connector makes integration convenient; it does not change the source system's authorization or data-quality obligations.

Avoid maker-personal connections for durable shared automations. Decide who owns and supports the flow, how credentials are rotated, what happens when a maker leaves, and how run-only users supply or inherit connections. Use a service identity only where licensing and product behavior support it, and grant minimum permissions.

### Compose reliable flow control and approvals

Actions call services or transform data. Conditions branch on a Boolean expression; `Switch` is useful for one value with several explicit cases. `Apply to each` handles collections; `Do until` repeats until a condition or limit. Configure concurrency only after analyzing ordering and duplicate effects. Use variables sparingly when the dataflow can remain explicit through outputs and expressions.

Approvals require an approver-selection rule, owner, timeout/escalation, reassignment policy, decision evidence, response storage, and behavior for cancellation or no response. Treat the approval outcome as data and validate it before changing business state. A request sent to a mailbox is not necessarily a governed approval record.

Use scopes to group work and configure run-after behavior for success, failure, skip, and timeout. Separate the try path from error logging and compensation. Design idempotency so a retried trigger does not create a second payment, ticket, or approval. Prefer stable business keys and record the external operation ID. For paged data, prove the expected item count; for rate limits, honor documented retry behavior.

Test happy path, empty input, malformed data, unauthorized connection, throttling, duplicate event, timeout, partial downstream success, rejection, and support recovery. Use trigger/action inputs and outputs, run history, connection state, and correlation data. Redact or minimize sensitive content in logs.

#### Worked flow — classify a small request batch

Use an instant trigger with a synthetic list of request IDs. For each ID, retrieve the current request row through the authorized connection. A condition routes only open requests to a triage action; the other branch records **skipped — not open**. Map the retrieved row ID and current category explicitly into the action instead of passing the trigger's unvalidated text. Keep processing sequential until independent ordering and duplicate effects have been justified.

Place the retrieve/condition/action path in a try scope, with separate run-after scopes for failure/timeout and final support logging. Persist an operation key before a consequential effect. Test an empty list, one closed row, a denied row and the same operation delivered twice. The expected ledger contains one result per input, preserves a skipped/failed distinction and records no duplicate business effect. A retry must not turn a previously completed item into a second approval. The [flow invocation and branching procedure](https://learn.microsoft.com/en-us/ai-builder/use-a-custom-prompt-in-flow) illustrates action-input mapping and a condition on an explicit approval outcome; the same control discipline applies before generated output can change the record.

### Worked example 3 — Deduplicate a business operation, not just a row

Five deliveries represent `(request-7, submit-1)` twice, `(request-8, submit-1)` once and `(request-7, submit-2)` twice. There are **three intended operations**, two duplicate deliveries and two distinct request rows. Deduplicating on request ID alone would suppress a legitimate second submission. Use a stable operation/version key and an atomic claim or downstream idempotency contract. A local set demonstration cannot prove concurrency safety or exactly-once external effects.

### Worked example 4 — Separate interactive and business deadlines

A synthetic request waits 35 seconds and needs another 100 seconds: **135 seconds**, exceeding a 120-second synchronous response boundary by **15 seconds**. A 45-day approval likewise exceeds the **30-day flow-run limit** by 15 days. The [flow limits](https://learn.microsoft.com/en-us/power-automate/limits-and-config) include waiting approvals in run duration. Use persisted request state and separate response-processing flows for [long approvals](https://learn.microsoft.com/en-us/power-automate/modern-approvals). For an HTTP pattern, [asynchronous responses](https://learn.microsoft.com/en-us/power-automate/guidance/coding-guidelines/asychronous-flow-pattern) use acceptance/status polling; a canvas app can instead submit a tracked request and retrieve its result. An acceptance acknowledgement is not business completion or a grant to read another user's result.

### Build a prompt as a governed input-output contract

AI Builder can create prompts from a template or blank and consume them in apps and flows. A strong prompt contract has:

- a narrow task and intended user/process;
- typed or clearly delimited inputs with size and sensitivity expectations;
- instructions, examples, constraints, and an explicit unknown/abstain behavior;
- selected knowledge/grounding sources with access, ownership, freshness, and citation expectations;
- model and settings chosen for quality, latency, cost, and deterministic-structure needs;
- a stable output shape that the app or flow validates before use;
- evaluation cases, human-review threshold, monitoring, version, and rollback.

Do not concatenate untrusted content into instructions without separation. Treat retrieved documents, emails, webpages, and user content as data that can contain prompt injection. Limit tools and downstream permissions, validate structured output, and never let free-form generated text directly select a privileged action.

Use knowledge when responses must be grounded in approved organizational content. Adding more documents is not automatically better: define scope, permissions, update interval, conflicting-source behavior, and evidence. A user should not receive content merely because the prompt's maker can access it.

Model settings can change creativity and other behavior, but no setting guarantees truth. Evaluate with representative inputs and expected rubrics. **VERIFY CURRENT:** model choices, setting names/ranges, region/language support, content filtering, capacity consumption, feature names, and whether an option is preview or GA.

When consuming a prompt in Power Apps, provide progress and error states and validate the result before display or action. In Power Automate, put generation inside a controlled run path, parse/validate output, apply human review when warranted, and store only necessary output and provenance. Microsoft explicitly recommends human review for generated content in consequential flows.

Use the current [prompts overview](https://learn.microsoft.com/en-us/ai-builder/prompts-overview), [app invocation](https://learn.microsoft.com/en-us/ai-builder/use-a-custom-prompt-in-app) and [flow invocation](https://learn.microsoft.com/en-us/ai-builder/use-a-custom-prompt-in-flow) procedures with their stated context. Older app tutorials name GPT-4o variants; the [current model settings](https://learn.microsoft.com/en-us/ai-builder/prompt-modelsettings) list newer options and regional/release-stage differences. Model context is per call, while one agent interaction may make several calls. Do not infer a total interaction budget from the context window or assume every reasoning model has a temperature slider.

[Prompt knowledge](https://learn.microsoft.com/en-us/ai-builder/use-your-own-prompt-data) supports a bounded retrieval set: 30 records by default, configurable up to 1,000, with limited relationship depth and no virtual tables. Connector knowledge is restricted to prompts in Power Automate. The page mentions SAP in its instructions but omits it from the limitations list; SAP support remains an evidence gap. Apply trusted identity filters and test both disclosure and missing-record cases; natural-language filtering is not an authorization policy.

With [JSON output](https://learn.microsoft.com/en-us/ai-builder/process-responses-json-output), testing can change an auto-detected format until it is saved; custom examples stabilize the format, and saving fixes the runtime contract. The generated schema is inspectable but not directly editable. A valid JSON structure still needs business validation for IDs, amounts, allowed categories and authority before any action.

#### Worked build — one prompt, two callers

Create **Request triage draft** from blank or a reviewed template in AI hub's prompt builder. Add a Text input for the request body, write instructions that return a proposed category plus a brief justification, and require an explicit unknown outcome. Supply synthetic ordinary, ambiguous and hostile samples; compare responses with a rubric, revise and save. The [current creation procedure](https://learn.microsoft.com/en-us/microsoft-copilot-studio/create-custom-prompt) still gives Power Apps/Power Automate entry points despite its move into Copilot Studio documentation. That documentation move does not establish that every harness or channel supports the same prompt.

In a canvas app, add the saved prompt through Add data. Call its `.Predict` function with the text-input value, retain the returned record and bind the returned text to a review label. Inspect the actual output shape before binding: [app invocation](https://learn.microsoft.com/en-us/ai-builder/use-a-custom-prompt-in-app) demonstrates a text result, while a configured JSON contract requires its own validated handling. Wrap invocation errors and keep the result as a draft.

In a cloud flow, add **Run a prompt**, select the same saved prompt and map its Text input from the preceding validated action. Pass the returned Text to a review step; branch on the explicit approval outcome and use the accepted text only after approval. [Flow invocation](https://learn.microsoft.com/en-us/ai-builder/use-a-custom-prompt-in-flow) documents these bindings. Test denial, timeout and unsupported category before any record-changing action. **VERIFY CURRENT:** control names, models, capacity and output shape; no invocation was executed here. The separate SAP-knowledge discrepancy above remains unresolved.

### Use AI models where their task and evidence fit

AI Builder provides prebuilt and custom models for supported tasks such as document processing, prediction, category classification, object detection, or text processing. Select a model based on input/output contract, training-data requirement, language/region, accuracy metric, explainability, latency, cost/capacity, and failure consequence.

For a custom model, separate training and representative test data, label consistently, avoid leakage, publish only after meeting a business threshold, and monitor production drift and input changes. For a prebuilt model, validate on your organization's documents and edge cases; “prebuilt” does not mean universally accurate.

In an app or flow, map every model input and output explicitly. Check missing/low-confidence results, create a human-review queue, retain source evidence as allowed, and define retry/fallback. Use a deterministic parser or business rule after the model where possible. Do not silently coerce an uncertain prediction into an authoritative fact.

#### Worked build — consume an OCR model through both surfaces

For a synthetic receipt image, insert the AI Builder text recognizer in a canvas app. Load the image and bind a review label to `TextRecognizer1.FullText`; use `Selected.Text` only when the user intentionally selects a detected line. The [component contract](https://learn.microsoft.com/en-us/ai-builder/prebuilt-text-recognizer-component-in-powerapps) distinguishes full text, line results and selected text. Keep the original image beside editable extracted values; text recognition does not prove that a total, currency or date has been interpreted correctly.

For a flow, start with a file input, add **Recognize text in an image or a PDF document**, and map its Image input to the file's content. Consume the full-document text when the next step needs the complete result; use the pages/lines structure only for deliberate line-by-line processing. The [flow procedure](https://learn.microsoft.com/en-us/ai-builder/flow-text-recognition) documents these distinct outputs. Route unreadable/empty output and business-validation failures to review; do not require a confidence field that a chosen component does not expose. Compare a clean image, blurred image and missing amount. Record expected extraction versus observed values if executed later, plus license/capacity checks and cleanup. No model or paid entitlement was used for this review.

### Worked example 5 — Coverage and correctness are different measures

Of 1,000 synthetic requests, 800 pass an automatic route and 200 require review. An audit finds 760 of those 800 correct. Automation coverage is **80%**, correctness among automatically routed requests is **95%**, and verified correct automatic outcomes are **76% of all requests**. If review averages four minutes, the initial review queue needs **800 minutes (13h 20m)** before rework. A confidence threshold is a design choice requiring calibration, not proof of 95% correctness.

### Plan the credit transition by execution context and contract

[AI Builder licensing](https://learn.microsoft.com/en-us/ai-builder/administer-licensing) separates feature credits from premium flow licensing. Apps/flows use available AI Builder credits first, then Copilot Credits; Copilot Studio uses Copilot Credits. Model/prompt building and testing have different charging rules from executing them in an app or flow.

The [credit transition schedule](https://learn.microsoft.com/en-us/ai-builder/endofaibcredits) does **not** retire AI Builder features. From **November 1, 2026**, new/renewed entitlements stop providing the affected seeded credits and add-ons cannot be renewed or newly purchased; existing entitlements remain usable through their contract end. There is no automatic currency conversion. Consumption accounting can lag by days, so a dashboard is not an immediate hard spending stop. Inventory contract dates, execution context, allocation and scenario rates; do not convert an old million-credit pack one-for-one.

### Select the correct business-logic surface

| Requirement | Strong fit | Important boundary |
|---|---|---|
| Immediate field validation/default/visibility supported declaratively | Business rule | Scope and supported operations; not a full cross-system process |
| Guided multi-stage record process with phases and required steps | Business process flow | Guides work; security and automation remain separate |
| Arithmetic or supported row expression | Formula/calculated column | Deterministic and row-oriented; verify function/type support |
| Aggregate over related rows | Rollup column | Recalculation timing and supported relationships/functions |
| Cross-service, approval, event, or scheduled orchestration | Cloud flow | Asynchronous behavior, identity, limits, duplicate/retry handling |
| Generative classification, extraction, draft, or summary | Prompt or AI model | Probabilistic; grounding, evaluation, validation, and human review |
| App interaction or presentation behavior | Power Fx | Client logic is not a universal security/business-integrity boundary |

Business rules can set values, requirements, visibility, enablement, recommendations, and validation within their supported scope. Business process flows expose stages and steps across a process. Calculated/formula columns derive row values; rollup columns aggregate related records on their recalculation schedule. Know where each rule runs and whether imports, APIs, flows, and every app observe the same result.

The [business-rule procedure](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-create-business-rule) distinguishes entity/server scope from form scope. Canvas apps need table scope and do not inherit form-only visibility, enablement or recommendations. Editable subgrids are unsupported. Activate and test the rule through each relevant write path; a process stage or hidden control is not a security boundary.

[Formula columns](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/formula-columns) have their own type/function limits, not the entire canvas Power Fx surface. Currency output is unsupported; using currency inputs requires the documented conversions. Compare compatible date behaviors and verify mobile-offline requirements. [Rollups](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/define-rollup-fields) run asynchronously: the initial mass calculation normally waits 12 hours, while incremental jobs have a one-hour default minimum recurrence. Other logic reads the last calculated value. Rollup values use system context, so protect the aggregate column if totals reveal inaccessible rows.

#### Worked build — a guided triage process

Within the solution, create a business process flow for Service Request with **Intake**, **Review** and **Close** stages. Add data steps for customer, category and disposition; mark only the stage-completion requirements as required. Validate, save and activate the definition, include it in the intended app and grant the test roles the needed business-process-flow instance privileges. A saved draft is unavailable to users. The [BPF construction procedure](https://learn.microsoft.com/en-us/power-automate/create-business-process-flow) separates stage/step definition, activation and instance security.

Test a representative user with a missing category, then with a valid category; check whether stage progression matches the brief. Test a read-only observer separately. Avoid using a required two-option Boolean when either Yes or No is a valid completed answer: the documented required Boolean must be Yes. Use a suitable choice for that requirement. A stage guides work; its required steps do not replace API validation, record authorization or the flow that performs an external action. Retain the exported definition and role/test evidence; this is an unexecuted design.

### Worked example 6 — An aggregate can be correct for the wrong instant

At the last calculation, two child amounts were 120 and 80: the stored total is **200**. A later child adds 50, making the desired current total **250**. Until recalculation, a rule comparing the stored rollup with a 225 threshold sees `200 < 225`, while current children imply `250 >= 225`. Do not use an asynchronous aggregate as an immediate transaction authorization check. This arithmetic does not execute Dataverse jobs or establish their completion SLA.

> **Related item:** Deterministic rules and AI work best as a chain: deterministic validation prepares clean inputs, AI performs the fuzzy task, deterministic schema/confidence checks validate output, a human handles high-risk uncertainty, and automation records the decision.

---

## Integrated scenarios

### Scenario A: Intelligent expense intake and approval

Employees use a responsive canvas app to submit expense records and receipts. Dataverse has Expense, Expense Line, Receipt, Policy Exception, and Approval Decision tables. A document model extracts candidate fields; deterministic rules validate totals, currency, dates, and policy limits. Low-confidence extraction or a policy exception routes to human review. A cloud flow creates an idempotent approval, stores the outcome, and updates status. A model-driven app gives finance role-filtered views, forms, charts, and exception queues.

Package tables, app, flow, model/prompt references, connection references, environment variables, roles, views, and dashboards in a solution. Test screen-reader and narrow layouts, delegation, duplicate submission, expired connection, rejected/expired approval, bad extraction, prompt injection in receipt text, and deployment to test. Monitor flow runs and AI review rates with correlation to the expense record.

### Scenario B: Partner service intake and triage

Partners authenticate to Power Pages and create Service Request records through web roles and table permissions. A grounded prompt summarizes the request and proposes a category using approved product-support knowledge. A flow validates structured output and routes to a queue; high-impact or uncertain requests require an agent. Internal staff use a model-driven app with role-specific forms and views. An embedded agent can retrieve allowed knowledge and start narrowly scoped tools, but it confirms any record-changing action.

Separate external identity, site access, table permissions, internal Dataverse roles, prompt knowledge permissions, and connector identity. Test two partner accounts to prove row isolation, malicious instructions in free text, obsolete knowledge, no-result behavior, tool authorization, escalation, DLP, and output disclosure.

### Scenario C: Service-case knowledge assistant

A model-driven case app uses forms, related records, queue views, charts, and a business process flow. The Dynamics Customer Service-specific case summary helps representatives scan the case, while a grounded prompt drafts a response from approved knowledge. Deterministic business rules enforce mandatory classification, a calculated SLA deadline remains authoritative, and a scheduled flow escalates overdue cases. Human agents verify and edit every outbound response.

Track prompt/model version, cited knowledge, user edit/rejection rate, unsupported claims, latency, and capacity. Release app, flows, prompt, roles, and configuration through a pipeline, then run a regression set containing normal, sensitive, ambiguous, multilingual, malicious, and outdated cases.

---

## Practical labs

1. **Architecture and environment:** Map a real process, classify every step as deterministic, AI-assisted, or human, choose components, and justify developer/sandbox/production boundaries plus DLP and identities.
2. **Dataverse foundation:** Build at least four related tables with appropriate ownership, column types, an association table, cascade choices, public views, main forms, security roles, prompt column or row summary, and test personas.
3. **Solution lifecycle:** Add every component to an unmanaged solution, use an environment variable and connection reference, export a managed build, import to a second environment, bind configuration, smoke-test, and document recovery.
4. **Model-driven experience:** Compose navigation, role-specific forms/views, a generative page reviewed for safety, charts/dashboard, sharing, and least-privilege record access.
5. **Responsive canvas experience:** Build data entry and browsing with containers, accessible labels/tab order/contrast, named formula or UDF, component library, scoped state, delegated query, error path, and Monitor evidence.
6. **Reliable flow:** Implement an event or app-triggered flow with a connector decision, approval, condition/loop, scope/run-after handling, idempotency, timeout/failed-connection test, and support log.
7. **Prompt and model:** Build a grounded prompt or supported AI model, use it from both an app and a flow, validate output, set a human-review threshold, and evaluate at least 20 representative/adversarial cases.
8. **Agent boundary:** Create or connect a Copilot Studio agent from a canvas app, constrain knowledge and tools, test two identities plus prompt injection and denied actions, and record escalation and monitoring evidence.

9. **Freshness and support worksheet:** Model prompt-column success, skipped, failed and pending states; track definition/input versions and timestamps. Compare generic row summaries with Dynamics-specific tables, package only the correct solution artifacts, and document connector/harness/region support gaps.
10. **Recovery and asynchronous boundaries:** Use synthetic records to reproduce the six examples. Design duplicate-delivery, lost-acknowledgement, delayed-approval, partial-write and stale-rollup cases. Specify atomic operation keys, persisted status, authorized result access and reconciliation. Execute tenant steps only in a separately provisioned sandbox; this review performed no service execution.

Repeat the labs from blank instructions. Save decisions, screenshots or exports, test cases, failures, corrections, and the exact documentation used. A working happy-path demo is not sufficient evidence.

---

## Knowledge checks

1. Why should the process outcome be defined before selecting an AI feature?
2. When is a model-driven app a stronger fit than a canvas app?
3. What evidence is needed before selecting a built-in agent?
4. Why should an irreversible action not be driven directly by generated text?
5. When should you recommend developer, sandbox, and production environments?
6. Why is the default environment a poor automatic choice for a critical app?
7. What belongs in a solution, connection reference, and environment variable?
8. Why does a managed solution not constitute a complete rollback plan?
9. When should a relationship become its own association table?
10. What cascade behavior must be reviewed for a parent-child relationship?
11. How do prompt columns and row summaries differ from formula and rollup columns?
12. Which layers determine a user's effective access to a Dataverse record and field?
13. Why do form/view role restrictions not replace table privileges?
14. What must be reviewed after creating a generative page?
15. How do public views, charts, and dashboards relate?
16. Why can a nondelegable canvas formula return a plausible but incorrect answer?
17. Which accessibility behaviors should be tested beyond color contrast?
18. When should you use a named formula, UDF, component, or component library?
19. What is the risk of using a large collection as a data-source mirror?
20. Which failures should an app-triggered flow expose to the user and support team?
21. What should Live Monitor evidence tell you?
22. Which identity and authorization boundaries must be retested for an embedded agent?
23. How do automated, instant, and scheduled triggers differ?
24. What should be evaluated when choosing a connector?
25. Why are maker-personal connections fragile for production automation?
26. What makes an approval more than an email notification?
27. How do scopes and run-after settings support failure handling?
28. How does idempotency prevent a retry from duplicating a business operation?
29. What fields make a prompt a testable input-output contract?
30. How can grounding content introduce prompt injection or data leakage?
31. Why does a low temperature or model setting not guarantee factual output?
32. What validation belongs between generated output and a downstream action?
33. When is an AI Builder model preferable to a generative prompt?
34. What should happen to a low-confidence extraction or prediction?
35. When should you choose a business rule, business process flow, formula/calculated column, rollup, or cloud flow?
36. How do deterministic validation, AI, human review, and automation form one safe process?

37. Why can a Completed prompt-column status represent no fresh generation?
38. Does editing a prompt definition refresh every existing value?
39. Why must Case summaries use a different configuration path?
40. Which generative-page artifacts and history move between environments?
41. Why can increasing the canvas row limit leave a query wrong?
42. Does semicolon chaining stop after the first failed write?
43. Why can an unchanged Dataverse value trigger another flow run?
44. How should an approval survive beyond a single flow run?
45. Does saved JSON structure prove that generated values are authorized?
46. Which prompt-knowledge connector remains unclear in the documentation?
47. Does November 1 remove every existing AI Builder credit entitlement?
48. Why can a rollup mislead an immediate approval decision?

If an answer is only a feature name, deepen it: state the requirement, data, identity, security, lifecycle, failure, evidence, and recovery consequence of the choice.

## Answers and reasoning

1. It establishes actors, state, evidence and acceptance criteria so the chosen feature solves the actual business problem.
2. When related Dataverse records and a structured process fit a metadata-driven interface; choose canvas when tailored interaction is central.
3. Supported task/data/actions, identity, environment, region, lifecycle, licensing, limits and measured failure behavior.
4. Generation can be wrong or influenced by untrusted content. Validate the action and its authorization independently.
5. Developer for personal build, sandbox for shared validation and production for operated workloads with recovery and ownership.
6. Broad maker access and personal-productivity use require deliberate governance before critical workloads are placed there.
7. Solution components travel together; environment variables hold destination configuration and connection references bind supported connections. Table data and secrets need separate handling.
8. It transports application artifacts without reversing changed business records or external effects. Preserve restore and reconciliation procedures.
9. When the relationship itself has attributes, dates, status, ownership or an independent lifecycle.
10. Assign, share, unshare, reparent and delete consequences; test with least-privilege personas and recovery evidence.
11. The first two generate probabilistic text; formulas compute supported expressions and rollups asynchronously aggregate related rows.
12. Environment and app access, table privileges, row ownership/sharing/team scope, column permissions and action identity.
13. They select the experience. Data authorization must hold through APIs, flows and alternate apps too.
14. Generated code, data access, bindings, input trust, errors, accessibility, performance, preview support, dependencies and publishing scope.
15. Views select the relevant records and columns; charts visualize data; dashboards combine components under effective data access.
16. It can evaluate only a local prefix. A valid-looking result can omit most matching records.
17. Keyboard order/focus, labels, screen readers, zoom/reflow, target sizes, noncolor cues and understandable errors.
18. Named formulas for derived values, typed UDFs for reusable calculation, components for reusable UI and libraries for shared maintenance.
19. Incomplete loading, stale data, memory/startup costs and local processing that hides source-query limitations.
20. Invalid input, denied access, throttling, timeout, duplicate or partial completion, plus a stable correlation/status path.
21. Which call/formula failed, when, under which identity and conditions, and how latency/data volume relate to the user experience.
22. Effective user, connector identity, records, knowledge, tool authorization, channel, consent and escalation; embedding does not transfer all guarantees.
23. They start from an event, an explicit request or a schedule; choose using process and failure semantics.
24. Operations, auth, policy group, licensing, limits, schema, pagination, retry, region, lifecycle and ownership.
25. Departure or credential change can disrupt them. Assign supported durable ownership, rotation and recovery procedures.
26. Named authority, decision state/evidence, deadlines, rejection/cancellation, reassignment and controlled business-state changes.
27. They route success/failure/timeout paths. They do not automatically undo successful external actions.
28. A stable operation key and atomic deduplication contract prevent repeated delivery from repeating the same effect; row ID alone can be too broad.
29. Task, input types, knowledge scope, model/settings, output contract, validation, owner, version and evaluation cases.
30. Retrieved data may contain hostile instructions or material outside the caller’s rights. Scope access before use and keep content separate from authority.
31. Sampling controls do not verify facts or permissions. Evaluate actual cases and preserve abstention and review paths.
32. Schema and value checks, allowed IDs/categories, current state, authorization, confidence calibration and consequential-action approval.
33. When its defined task and measured performance fit, such as document extraction; compare input/output, training needs and operational cost.
34. Retain the source where allowed, route for review, record the correction and diagnose recurring input/model problems.
35. Choose the narrowest supported execution surface with the right scope, timing, types, identity and failure behavior.
36. Validate inputs, use AI for the uncertain subtask, validate outputs, review consequential exceptions, then record controlled actions.
37. Some statuses explicitly represent a filter or unchanged-input skip. Check the detailed code and generation evidence.
38. No. Existing values await a supported trigger; track stale versions explicitly.
39. The general custom-summary feature excludes certain Dynamics tables that already provide their own summaries.
40. The app/sitemap and page dependencies move with published code and the first prompt; full editing history does not.
41. The source may still exceed the larger prefix, with matches beyond it. Verify query support and completeness.
42. No. Guard dependent actions explicitly with compatible error-handling results; successful prior writes still need reconciliation.
43. The trigger detects included update columns, even when their values are unchanged. Design operation-level deduplication.
44. Persist the request and use a separate response-processing flow with business deadlines and authorized state transitions.
45. No. Shape validation cannot prove correctness, current state or permission to act.
46. SAP appears in connector instructions but not the limitations list. Confirm support before depending on it.
47. No. Existing qualifying contracts retain credits through their term; new/renewed entitlement and add-on rules differ. No automatic conversion occurs.
48. It may hold a prior result and uses a different access context from the viewer. Check freshness and secure aggregate disclosure.

---

## Final readiness checklist

- [ ] I can map a process to Dataverse, apps, flows, agents, prompts/models, and human decisions without adding AI where deterministic logic is safer.
- [ ] I can justify environment type, DLP, identities, roles, solution contents, configuration, pipeline, test evidence, and recovery.
- [ ] I can model tables, columns, relationships, views, forms, security, prompt columns, and row summaries from business meaning.
- [ ] I can build, share, secure, diagnose, and optimize model-driven and responsive canvas apps.
- [ ] I can explain named formulas, UDFs, components, variables, collections, delegation, error handling, and Live Monitor.
- [ ] I can create reliable flows with appropriate triggers, connectors, approvals, control, identity, failure handling, idempotency, and monitoring.
- [ ] I can build and consume a grounded prompt and AI model with validation, evaluation, human review, and responsible-AI controls.
- [ ] I can choose among business rules, business process flows, formulas/calculated columns, rollups, cloud flows, prompts, and models.
- [ ] I completed the three scenarios, ten labs, and 48 answered checks without using exam dumps.
- [ ] I rechecked the official blueprint, credential page, Practice Assessment availability, and retirement page immediately before scheduling.

---

## Places to learn

This is a selective starting set, not a complete list and not a prescription to consume everything. Pick the explanation, demonstration, hands-on practice, and assessment style that works for you. Reconcile every exam-labeled resource with the current official blueprint before investing time or money; the October 16 page update does not publish a new skills-effective date.

### Focused source-to-evidence route

**Requirements before tooling — public reading; about 45–75 minutes.** Read the [AI-powered solution-design module overview](https://learn.microsoft.com/en-us/training/modules/design-ai-powered-solutions-power-platform/) and its [requirements-to-components unit](https://learn.microsoft.com/en-us/training/modules/design-ai-powered-solutions-power-platform/3-recommend-power-platform-components) (published unit estimate: 7 minutes). For a synthetic repair-request process, produce a one-page matrix of users, data, human decisions, automation and proposed components; justify one step that should remain deterministic. The planning range adds an original worksheet and revision to the short reading, not tenant deployment. Prior canvas-app, flow and Dataverse familiarity is assumed. The module is selective design training, not proof of licensing, rollout or complete blueprint coverage; implementation needs current product documentation. Public text was reviewed October 28, 2026; no account, tenant or paid lesson was used.

| Resource | Access | Estimated time |
|---|---|---:|
| Official self-paced course | Free | 17 modules; allow 40–70 hours with builds |
| Instructor-led AB-410T00-A | Paid or partner-sponsored | 3 days |
| Official documentation | Free | 8–20 hours selectively |
| Microsoft Power Platform video | Free | 3–10 hours selectively |
| Udemy / Phillip Burton | Paid | 21h 09m total listing; exam-only portion unclear |
| Whizlabs | Paid | Allow 8–20 hours selectively; verify current totals |
| Partner Skilling Hub | Partner-restricted | Event-specific; verify signed-in start/end times |

- **Official self-paced paths — 17 modules; allow 40–70 hours with builds and notes:** [AB-410T00](https://learn.microsoft.com/en-us/training/courses/ab-410t00) links [AI-first design](https://learn.microsoft.com/en-us/training/paths/design-model-solutions-power-platform/) (3 modules), [Dataverse modeling](https://learn.microsoft.com/en-us/training/paths/build-data-model-microsoft-dataverse/) (3), [apps and portals](https://learn.microsoft.com/en-us/training/paths/build-apps-portals-power-apps/) (7), and [automation](https://learn.microsoft.com/en-us/training/paths/automate-business-processes-power-automate/) (4). The earlier 15h26 total is historical; current fetched outlines do not expose those durations. The study budget is editorial, not vendor timing.
- **Instructor-led course — three days:** [AB-410T00-A](https://learn.microsoft.com/en-us/training/courses/ab-410t00). Use the listed language and schedule filters to find a delivery; agenda timing varies by provider.
- **Official reference and product updates — selective, 8–20 hours initially:** [Microsoft Power Platform documentation](https://learn.microsoft.com/en-us/power-platform/) and [AI Builder documentation](https://learn.microsoft.com/en-us/ai-builder/). Follow links from weak objectives and recheck volatile Copilot, agent, prompt, model, capacity, and governance behavior.
- **Official video — selective, 3–10 hours:** [Microsoft Power Platform on YouTube](https://www.youtube.com/@MicrosoftPowerPlatform) for current demonstrations and release sessions. It is topical material, not an AB-410 checklist.
- **Marketplace course — 21h 09m total listing:** [Phillip Burton's Udemy AB-410 course](https://www.udemy.com/course/pl-100-microsoft-power-platform-app-maker-ms/) shows a September 2026 update, 38 sections and 213 lectures in the indexed public page. Its description still claims about 7h30 of AB-410 material and promises removal of older content from September 1. That stale description does not prove the remaining runtime is exam-aligned. Direct automated access was blocked; the indexed outline was available. Paid lessons, completeness and the removal were not verified.
- **Additional paid course/practice bundle — allow 8–20 hours selectively:** [Whizlabs AB-410](https://www.whizlabs.com/microsoft-ab-410-certification-training/). The fetched page returned only a title shell, so duration, counts and coverage remain unverified; verify before purchase.
- **Partner-restricted learning:** [Partner Skilling Hub](https://www.skilling-hub.com/en-US) may list AB-410-aligned delivery for eligible Microsoft partners. Sign-in is required to confirm the exact current event, start/end times, seat availability, and prerequisites.

**VERIFY CURRENT — checked October 28, 2026:** the [AB-410 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-410) and credential page now direct learners to the Practice Assessment on AI Skills Navigator, with sign-in required. Its public link establishes the announced access path; no signed-in questions, launch, count or performance was inspected. Allow about 1–2 hours for an initial diagnostic attempt and review, an editorial estimate. In bounded September 28, 2026 searches, no exact AB-410 offering from Pluralsight, O'Reilly, or MeasureUp could be independently verified in their public catalogs. Do not infer a product from their coverage of older Power Platform exams, and avoid sites advertising memorized or “real exam” questions. Use the official exam sandbox for interface familiarity and the original checks and labs above for readiness; use the announced official Practice Assessment diagnostically once its exam-specific signed-in access is confirmed.

---

### Useful blog exercises

- [September Power Platform update](https://www.microsoft.com/en-us/power-platform/blog/power-apps/whats-new-in-power-platform-september-2026-feature-update/) — Tiffany Treacy, September 17, 2026. Read the model-driven app-builder, embedded-page and preview connector sections. Draft a persona/data/permission plan, then list what an external tool would create, which bindings it needs and what evidence must precede publication. Allow 45–75 minutes; use a worksheet without executing tooling.
- [May Power Platform update](https://www.microsoft.com/en-us/power-platform/blog/2026/05/14/whats-new-in-power-platform-may-2026-feature-update/) — Tiffany Treacy, May 14, 2026. Read the user-defined-type section and compare typed records/functions with unvalidated model JSON. Design valid, missing, wrong-type and forbidden-value cases; a type-correct value can still violate business rules. Allow 30–60 minutes. Check current App.Formulas documentation before implementing the example.

Only those selected article sections were reviewed for these exercises. Other product announcements, linked tools, paid content, videos and performance claims were not reproduced. Blogs supplement the blueprint; their publication dates do not prove tenant rollout.
