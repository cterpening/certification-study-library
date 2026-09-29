---
exam_code: SERVICENOW-CAD
vendor_id: servicenow
official_blueprint: https://learning.servicenow.com/lxp/en/credentials/certified-application-developer-mainline-exam-blueprint?id=kb_article_view&sysparm_article=KB0011498
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# ServiceNow Certified Application Developer (CAD) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The September 29 review maps 22 canonical subtopics, answers 40 original readiness prompts and executes 38 local JavaScript checks. Eight ServiceNow activities remain proposed. See the [coverage record](../docs/SOURCE-VALIDATION.md#servicenow-cad-coverage-record) and [deep-review evidence](../docs/research/2026-09-29-servicenow-cad-deep-review.md).

**CURRENT BLUEPRINT:** Designing and Creating an Application 20%; Application User Interface 20%; Security and Restricting Access 20%; Application Automation 20%; Working with External Data 10%; Managing Applications 10%. The canonical January 2026 page was fully read in a fresh unsigned browser on September 29. Its listed subskills are not exhaustive.<br>
**Snapshot repair:** The September 17 guide headers already used these weights, but the saved snapshot and final checklist retained 15/20/20/20/10/15. This review aligns them and preserves the earlier snapshots and reviews. It records a correction, not a newly announced exam cutover.<br>
**Exam contract:** The blueprint lists 60 multiple-choice/multiple-select questions in 90 minutes, Pearson test-center or OnVUE delivery, and 90 days from registration/payment to both schedule and complete the attempt. Multiple-select questions have no partial credit. Results are conditional and may be audited; the cut score is undisclosed and not always 70%. Section percentages must not be averaged into a pass prediction.<br>
**Experience and preparation:** The vendor recommends six months of hands-on application development, appropriate development/administration roles and groups, and Welcome to ServiceNow, Scripting in ServiceNow Fundamentals and Application Development Fundamentals. These recommendations are distinct from mandatory registration prerequisites. Practice JavaScript and platform administration as foundations for the work.<br>
**VERIFY CURRENT:** Check your actual booking for price, language, ID, accommodations, delivery and rescheduling rules. Credential holders must follow assigned annual delta and CMP requirements. No account-specific maintenance deadline or future window was verified. No dated mainline retirement/replacement was identified in accessible certification material.<br>
**Access boundary:** The simple HTTP monitor and web reader still receive shells; the unsigned browser recovered the main blueprint without login or enrollment. Paid lessons, practice questions and instance behavior were not accessed. The current documentation can show Brazil while indexed pages still show Australia; neither product-family metadata nor a preview event establishes exam scope.<br>
**Practice boundary:** MeasureUp's public March 2026 listing has 120 questions distributed 24/24/24/24/12/12, matching the blueprint percentages. Its generic roughly-150 wording differs. No demo or question interior was opened; advertised translations, readiness percentages and guarantees are not official exam languages or cut scores.

## How to use this guide

Build one small scoped application end to end in a Personal Developer Instance (PDI), official training lab, or other authorized nonproduction instance. For every feature, record requirement → declarative-or-script choice → execution context → data/security effect → test evidence → deployment and rollback path. Test as an authorized user, unauthorized user, delegated developer, and administrator; administrator-only success is weak evidence.

ServiceNow releases, interfaces, APIs, and recommended builders evolve. Record the family release used in each lab. Treat Studio/App Engine Studio, Workflow/Flow Designer, workspace/platform UI, application repository, Git, and transport behavior as version-sensitive. Never copy a course solution or production data into a public lab.

> **About related items:** A `Related item:` callout adds prerequisite, architecture, security, testing, operations, or lifecycle context. It connects an official objective to production practice but does not claim that wording is part of the published blueprint.

## Blueprint map

| Domain | Weight | Evidence to produce |
|---|---:|---|
| Designing and Creating an Application | 20% | Fit decision, scoped data model, roles, modules, ownership and lifecycle boundary |
| Application User Interface | 20% | Persona-tested form/list/record-producer behavior with client/server separation |
| Security and Restricting Access | 20% | Table/field/module/cross-scope allow-and-deny matrix with debug evidence |
| Application Automation | 20% | Idempotent declarative/scripted flow with timing, error and observability proof |
| Working with External Data | 10% | Repeatable import and REST exchange with credentials, validation and reconciliation |
| Managing Applications | 10% | Versioned source/repository workflow with review, test, promotion and rollback evidence |

## 1. Designing and Creating an Application — 20%

**CURRENT BLUEPRINT — named subtopics:** Determine if an application is a good fit with ServiceNow; Design and implement a data model; Create modules; Use Application scope.

Begin with fit. ServiceNow is a strong candidate when work is record-centered, role-governed, auditable, workflow-heavy, and benefits from platform capabilities. A high-volume compute pipeline, hard real-time system, unsupported user experience, or capability already provided by a supported application may belong elsewhere. Define actors, outcomes, data sensitivity, volume, integrations, service levels, reporting, ownership, licensing, upgrade tolerance, and exit path before creating tables.

Model business records rather than screens. Identify entities, keys, lifecycle states, relationships, ownership, retention, and authoritative sources. Choose whether to extend an existing table only when inherited fields, behavior, security, reporting, and licensing semantics genuinely fit. Use reference fields for governed relationships and many-to-many tables when the relationship has its own meaning. Avoid duplicate truth, unbounded text where structure is required, and fields created solely to make one form convenient.

A scoped application namespaces artifacts and establishes boundaries. Know the difference between application scope, current scope, accessible-from settings, cross-scope privileges, table application-access settings, and user authorization. Scope helps isolate artifacts and APIs; it does not replace ACLs or secure data design. Use unique, stable internal names and document any deliberately exposed contract.

Applications contain menus, modules, tables, roles, scripts, flows, properties, security rules, and other application files. A module is navigation, not data authorization. Give modules clear audience and filter behavior, and verify that bypassing navigation does not expose data.

Choose the supported development experience for the task and release. App Engine Studio emphasizes guided low-code construction; Studio exposes application files and source-control workflows. Avoid building the same concern independently in several tools. Name the authoritative artifact and test how each experience renders it.

`Related item:` An architecture decision record should capture why the app belongs on ServiceNow, why its table model was chosen, which supported capability was not reused, and what would trigger redesign or retirement.

The current [planning reference](https://www.servicenow.com/docs/r/application-development/plan-before-you-build.html) makes scope and instance selection early decisions. It distinguishes a disposable proof of concept from an organizational application and warns against importing a PDI prototype into a different company namespace. The suggested scope prefix affects application files; renaming a display label does not establish a safe namespace migration. Global applications have different capabilities, including the documented lack of delegated development. Record the exception before choosing global scope.

## 2. Application User Interface — 20%

**CURRENT BLUEPRINT — named subtopics:** Create, design, and customize forms; Add/Remove fields from forms and tables; Write, test, and debug client-side scripts for desktop; Write, test, and debug server-side scripts; Use a Record Producer as an application's UI.

Forms organize fields, sections, related lists, formatters, views, and actions over a record. Tables and dictionary entries define stored data; form layouts/views define presentation. A hidden or read-only client control is not security. Validate server-side data rules and ACLs independently from every client experience.

Design fields intentionally: type, length, default, reference qualifier, choice ownership, mandatory/read-only behavior, encryption or sensitivity, indexing need, and migration impact. Adding a field to a table does not automatically make it appropriate on every view. Removing a field from a form does not remove it from APIs, lists, reports, or storage.

UI Policies declaratively control form behavior. Client Scripts run in a browser context and commonly use `g_form`, `g_user`, and supported client APIs. Know onLoad, onChange, onSubmit, and onCellEdit contexts, and do not assume APIs available on a platform form work identically in a workspace, portal, mobile, or catalog experience. Avoid synchronous calls, fragile DOM manipulation, secrets, and client-side decisions that must be trusted by the server.

Server-side code uses server APIs and has no browser `g_form`. Business Rules, Script Includes, data policies, flows, and other server artifacts should own enforceable business logic. When a client needs server data, expose the smallest supported asynchronous contract and re-check authorization server-side.

A record producer gives a requester-friendly input experience that creates a record. Map variables deliberately, validate and normalize data, control the resulting record's security, and give the requester a clear outcome. Do not confuse record producer, catalog item, order guide, form, or portal/workspace page.

Test a matrix: create/read/update, normal/error/empty input, desktop/target experience, and allowed/denied roles. Capture the actual changed record and logs, not only a screenshot of the form.

`Related item:` Accessibility, localization, browser behavior, and responsive layout are production requirements even when a blueprint subskill says “desktop.” Avoid encoding critical meaning only in color, order, hover, or an English-only label.

## 3. Security and Restricting Access — 20%

**CURRENT BLUEPRINT — named subtopics:** Restrict access to applications and application modules; Manually and automatically create, test, and debug Access Controls; Use GlideSystem methods to script security; Use Application Scope to protect application artifacts.

Separate navigation, execution, and data authorization. Application/menu/module roles control discovery; ACLs protect records and fields; roles and application settings govern development/admin actions; application scope and cross-scope privileges govern artifact interaction. A user who cannot see a module may still reach a table through another route unless data access is enforced.

Access controls are evaluated for an operation and target. Understand table versus field rules, inheritance/wildcards, required roles, conditions, and scripts. For a matching ACL, its role, condition, and script requirements must pass. Multiple applicable rules and inheritance can make intuition unreliable, so use the platform's security-debugging tools and impersonated test users. Record both an allowed and denied trace.

Create ACLs automatically where a supported builder provides the intended baseline, then inspect them. Manual ACLs require a named requirement and tests. Keep security scripts small and deterministic; use server-side APIs appropriately and avoid query-per-record patterns. `GlideSystem` methods can inspect user roles or context, but embedded special-user logic is usually less maintainable than a clear role/group and ACL model.

Table Application Access settings define how other scopes may perform operations such as read, create, update, delete, and web-service access. Cross-scope privileges record allowed interactions between application scopes. Grant the narrowest contract, do not approve unknown runtime access reflexively, and retest after cloning or promotion.

Consider elevated privilege, delegated developer access, secrets, personally identifiable data, logging, and admin override. An admin test cannot prove least privilege. Where supported, prefer secure record access patterns and return only fields the caller is authorized to see.

`Related item:` Threat-model the application: direct URL/API access, crafted input, reference traversal, over-broad roles, cross-scope calls, attachment leakage, unsafe script evaluation, credential exposure, and aggregate/report inference.

### Three access questions that need separate answers

Use the [application access overview](https://www.servicenow.com/docs/r/application-development/c_ApplicationAccessSettings.html) to distinguish caller-owned cross-scope privileges, target-table settings and target-owned restricted-caller decisions. Then assess the executing user's permissions. One approved scope relationship does not prove that a requester may see every field.

The [table access fields](https://www.servicenow.com/docs/r/application-development/r_TableApplicationAccessFields.html) govern cross-scope script CRUD separately from the web-service checkbox. The [REST reference](https://www.servicenow.com/docs/r/api-reference/rest-api-explorer/c_RESTAPI.html) explicitly says those cross-scope CRUD switches do not apply to web-service requests; web-service enablement and caller authorization still matter. Do not grant a script privilege as a workaround for an unrelated API authorization failure.

The [Glide Server API reference](https://www.servicenow.com/docs/r/api-reference/scripts/p_GlideServerAPIs.html) distinguishes ordinary GlideRecord checks from GlideRecordSecure's standard ACL enforcement. Secure does not automatically opt into query ACLs. The documented `addUserEncodedQuery` path applies query checks to untrusted query input; `addSystemEncodedQuery` is for trusted system conditions. Verify availability and behavior in the installed release. Prefer a narrow structured input contract to accepting arbitrary encoded queries, and explicitly select permitted output fields. A class name alone does not prove a safe endpoint.

**Source correction:** The employee-authored [scoped-app article](https://www.servicenow.com/community/developer-articles/servicenow-custom-scoped-app-security-a-developer-s-guide-to/ta-p/3484927) usefully proposes an access matrix, but its junior-analyst example says a junior passes a senior-only table rule without establishing role inheritance or another table grant. A field grant cannot repair a failed table decision. Its blanket server-script authorization claims, illustrative ACL-call arithmetic and pasted code are not accepted as runtime evidence. Use primary API documentation and measured tests; no attached spreadsheet or source code was run.

The [ACL overview](https://www.servicenow.com/docs/r/platform-security/access-control/exploring-access-control-list.html) requires applicable table and field access and distinguishes applicability from conditions. The [Deny-Unless page](https://www.servicenow.com/docs/r/platform-security/access-control/acl-denial-behavior.html) has contradictory prose about the no-Allow-If case. That edge case remains unresolved; the local workbook is an explicit chosen policy, not a complete ACL engine.

## 4. Application Automation — 20%

**CURRENT BLUEPRINT — named subtopics:** Write, test, and debug Workflow and Flow Designer; Create and use Application Properties; Create Events, Scheduled Script Executions (Scheduled Jobs), and Utils (application) Script Includes; Send and receive email.

Pick the simplest supported mechanism whose execution context matches the requirement. Flow Designer/Workflow Studio provides triggers, actions, subflows, conditions, data pills, connections, and execution details. Business Rules run on database operations; Script Includes package reusable server logic; scheduled script executions handle time-based work; events decouple occurrences from handlers such as notifications. Legacy Workflow may still exist, but new design should follow current platform guidance.

Know Business Rule timing: before rules can change the current record before persistence; after rules react after the write; async rules defer work; display rules prepare server data for a form. Avoid recursive updates, broad queries, long synchronous external calls, and duplicated logic across rules and flows. Conditions should be precise enough to prevent accidental re-entry.

Application properties externalize supported configuration. Give each a documented type, default, scope, owner, sensitive-value rule, environment strategy, and safe missing/invalid behavior. Do not put credentials in ordinary properties when a credential/connection mechanism is intended.

Events should have clear names, producers, payload meaning, consumers, failure behavior, and retention/diagnostic story. Scheduled jobs need an idempotent selection boundary, checkpointing, concurrency guard, safe rerun, and observable outcome. Utility Script Includes need narrow functions, stable inputs/outputs, error handling, access settings, and automated tests.

Email can be inbound or outbound. Validate sender/recipient trust, watermark or correlation behavior, parsing, restricted data, templates, localization, loops, spoofing, and nonproduction mail controls. Never let a forged message perform a sensitive action without server-side identity and authorization checks.

Design external actions for timeout, retry, duplicate delivery, partial failure, and compensation. Test Flow execution details and logs, but prevent logs from leaking secrets. Measure duration, success, retries, backlog, and business outcome rather than “the flow ran.”

`Related item:` Automated Test Framework (ATF), code review, static analysis, and negative tests turn an automation from a demo into a maintainable change. Cover trigger conditions, prohibited users, repeat execution, failures, and upgrades.

The [current Business Rule documentation](https://www.servicenow.com/docs/r/api-reference/business-rules-classic/c_BusinessRules.html) recommends Workflow Studio for new process automation while documenting existing rule behavior. Changes made by before rules participate in the current record’s save; calling `current.update()` again risks recursion. Async scripts do not have `previous`, and their order is not guaranteed. Condition-builder change checks differ from script availability. Some write paths bypass rule processing, so a rule is neither universal input validation nor proof that ACLs were honored. Identify every writer and its execution context.

## 5. Working with External Data — 10%

**CURRENT BLUEPRINT — named subtopics:** Import data in CSV or Excel format; Integrate to, including testing and debugging, an external data source using REST.

For CSV/Excel import, profile the source before loading: authoritative owner, identifiers, duplicates, types, required values, references, volume, encoding, sensitivity, and rollback. Import sets stage data. Transform maps map and convert it; coalesce identifies update-versus-insert behavior. Transform scripts can add power and risk. Trial a small subset, capture counts, reconcile rejects and duplicates, then make reruns safe.

Do not use an update set as a business-data migration tool. Decide whether data belongs in an import set, integration, clone, deployment artifact, or another supported mechanism. Protect attachments and temporary staging tables; remove or retain them under policy.

For REST, distinguish outbound REST messages/steps from inbound APIs. Define endpoint, method, contract/schema, authentication, credential alias/connection, network route or MID Server need, pagination, rate limits, timeout, retries, idempotency, correlation, error mapping, and observability. Validate TLS and never log tokens or complete sensitive payloads.

Test success, authentication failure, invalid data, timeout, throttling, duplicate delivery, unavailable dependency, and partial completion using a controlled endpoint. Reconcile ServiceNow state with the authoritative external system after recovery. Mock external dependencies in automated tests where practical.

`Related item:` Integration ownership crosses application boundaries. Document who can rotate credentials, change schemas, approve network access, handle incidents, replay failed work, and decide which system wins a conflict.

### Pagination, query validation and uncertain outcomes

The REST overview states that `sysparm_limit` is applied before ACL evaluation. An empty visible result can therefore coexist with later authorized records. The workbook's first two source records are inaccessible, yet later pages contain IDs 3 and 6. It follows explicit fixture continuation data instead of stopping on the empty page. A real client needs documented endpoint pagination, stable ordering and a completeness strategy under concurrent changes; this fixture is not a Table API snapshot implementation.

Invalid encoded-query components can be ignored, broadening the result to the valid portion. Reject unknown input fields/operators before building a query; do not silently drop them. Response field selection is also separate from security. Test the endpoint's actual error, empty and denied-field behavior with an authorized identity. The REST Explorer can mutate the current instance, so treating it as a harmless code generator is unsafe.

For imports, the [coalesce reference](https://www.servicenow.com/docs/r/integrate-applications/system-import-sets/c_ImportSetCoalesce.html) documents all-field matching, first-match behavior for duplicate targets and case/empty options. Validate target uniqueness and reference identity before the transform. For external writes, record a stable business operation key and the payload/result it represents. A timeout can occur after the external operation succeeded; reconcile the receipt before retrying. In-memory deduplication, a transport success or an unchanged row count alone does not establish durable business correctness.

## 6. Managing Applications — 10%

**CURRENT BLUEPRINT — named subtopics:** Download and install applications; Use Delegated Development to manage source code and code review; Use the ServiceNow Git integration to manage source code.

Application lifecycle includes creation, local development, source/version management, review, testing, packaging, installation, upgrade, rollback, ownership, and eventual retirement. Identify every artifact and dependency before promotion. A technically installable application is not necessarily licensed, secure, supported, compatible, or ready for production.

The ServiceNow application repository distributes scoped applications between instances under vendor-defined rules. Git integration synchronizes supported global or scoped application files with a repository for collaboration and history. Update sets transport captured configuration and are not equivalent to Git or application repository packages. Know what each mechanism captures, its collision model, and the intended direction of travel.

Use short-lived branches, meaningful commits, peer review, protected credentials, and a clean application/scope context. Avoid simultaneous edits to the same artifact through conflicting mechanisms. Pull/rebase/commit behavior is product- and workflow-specific; reproduce it in an authorized sandbox and follow current docs rather than generic Git intuition.

Delegated Development grants controlled creation or modification capabilities without broad administrator access. Define application, developer/group, permitted file types, publish/deploy rights, code review, expiry, separation of duties, and audit. Test what the delegate cannot do.

Before promotion, inventory dependencies, roles/ACLs, properties, credentials, data prerequisites, flows, scheduled jobs, plugins, tests, and operational dashboards. Use preview or collision review where supported, preserve an evidence bundle, smoke-test with real personas, and know how to restore configuration and data. Upgrades require regression tests for supported APIs and every intentional customization.

`Related item:` Production readiness includes ownership, service level, support runbook, security/privacy review, release notes, monitoring, incident response, data retention, accessibility, and decommissioning—not merely successful installation.

### Version control and tests are different evidence

The [Studio source-control reference](https://www.servicenow.com/docs/r/application-development/servicenow-studio-classic/source-control-integration.html) describes global or scoped application metadata on nonproduction instances. Its workflow uses one repository per application and one shared repository credential set for developers on the instance. A generic Git branch plan does not prove individual attribution, least privilege or production deployment support. Review the installed tool's permissions and transport path. Limited external-file support includes validation/sanitization; matching a repository commit does not by itself prove the installed application contains every intended artifact.

The [update-set capture reference](https://www.servicenow.com/docs/r/application-development/system-update-sets/customizations-tracked-update-sets.html?contentId=Wesk3KW7yiI5hKC5y~QwUA) distinguishes configuration from transaction data and documents destructive schema limits. Preview can miss type mismatches; a dropped column can lose data. Plan a versioned migration and recovery for data as well as configuration.

[ATF design guidance](https://www.servicenow.com/docs/r/application-development/automated-test-framework-atf/automated-test-framework-design-considerations.html) recommends isolated test-created data and users, avoiding shared system-record mutations and declaring conflicts between tests. Run tests only in nonproduction. Custom UI components must be retrieved again after moving tests; their presence is not automatically transported as metadata. An installed test or green suite proves only its exercised assertions, not every persona, interface or external side effect.

The [Developer Passport announcement](https://www.servicenow.com/community/developer-passport-blog/introducing-the-developer-passport-brazil-release-preview/ba-p/3586556) lists eleven September 14–18 Brazil preview sessions. The article was read, but no video playback or PDI availability was verified. Keep preview learning, release-specific API behavior and mainline scope separate.

## Integrated scenarios

### Scenario 1: Governed equipment-request application

**Given:** Requesters see their own equipment requests; fulfillers work assignments; only cost reviewers see restricted prices. A delegated developer may change selected application files but cannot publish to production.

**Worked decision:** Design data identity and access before the form. Table access must include the intended requester policy, while sensitive fields remain separately restricted. A record producer creates the record through a validated server contract; hiding a variable is insufficient. Scope permissions, the executing user's access and development permissions are distinct. Capture an allowed requester, another requester denied the record, a permitted fulfiller denied cost, and a delegate denied the prohibited action.

**Evidence:** Trace requirement, application file, effective access decision and persisted business result. Include derived/report exposure and direct API paths. Transport configuration and data migrations through the supported release process, then verify the target rather than equating a Git commit with an installed outcome. No application, identity or permission was created here.

### Scenario 2: Vendor-status REST integration

**Given:** The first source page contains two inaccessible rows, while later pages expose IDs 3 and 6. An update succeeds but its acknowledgment is lost. A later legitimate repair arrives before the original request is retried.

**Worked result:** The original JavaScript fixture follows continuation information across the empty visible page and returns exactly `[3, 6]`. It rejects repeated continuation offsets and duplicate identities. A bounded filter contract rejects misspelled fields, extra properties and an injected encoded clause instead of dropping invalid conditions. These are local models, not real REST requests.

The receipt example closes version 3 at version 4. An exact retry returns the existing receipt; changed content under the same key conflicts. A separate repair reopens the record at version 5. Replaying the old close again reports that prior operation without overwriting the repair. A receipt is historical evidence, not a claim that current state still equals its original result. Durable atomic receipts, crash recovery and cross-system reconciliation remain live-design requirements.

### Scenario 3: Delegated departmental application

**Given:** A prototype was created in a PDI namespace, the target belongs to a different company namespace, and a team proposes importing it directly, enabling broad scope access and relying on shared Git credentials for approval evidence.

**Worked decision:** Apply the documented namespace/instance plan before adoption. Rebuild the proof of concept in the organizational development context when the namespace differs; do not treat a display rename as migration. Define the delegated file/action boundaries, credential ownership, reviewer evidence and supported promotion method. Cross-scope script permission and REST table enablement are separate gates in the workbook, and neither replaces user authorization.

**Evidence:** Test fresh installation and upgrade, exact dependencies, denied delegate actions, target data and rollback/fix-forward. ATF fixtures create isolated test records instead of changing shared system records. Check how custom UI components are retrieved on the target and which external effects are outside test rollback. No repository credential, source integration, application install or deployment was performed in ServiceNow.

## Hands-on evidence labs

All eight activities are **proposed**, not executed in ServiceNow. Use authorized nonproduction access, synthetic data and the organization's normal permission/change process. Record family, scope, artifact version, persona, expected/observed result, failure evidence and cleanup.

1. **Fit and model:** Produce an application-fit decision, entity/reference map, ownership/retention rules and namespace plan. Compare extension versus a new table. Confirm the intended artifacts and licensing before building; prove a rejected fit case as well as an accepted one.
2. **Interface and validation:** Use two personas and the actual target experience to exercise a form, UI Policy, record producer and server validation. Test empty, malformed and unauthorized input through both UI and an approved alternate interface. Retain resulting record/log evidence, not just screenshots.
3. **Access boundaries:** Define table and field permissions, one cross-scope contract and a separate web-service decision. Test caller and target scope restrictions, a table-denied/field-allowed case and restricted output fields. Record effective ACL decisions without broadening permissions to make tests pass.
4. **Automation:** Map a flow, reusable script, property, before/after/async responsibilities and event to an owned business outcome. Test duplicate triggers, stale data, recursion protection and failure recovery. Inspect notification recipients/content with delivery disabled.
5. **Import:** Preflight synthetic source keys, target duplicates, references, case/empty options and disjoint row outcomes. Transform a small permitted batch twice and compare exact records. Rehearse scoped reversal without deleting later legitimate updates; clean staging data.
6. **REST:** In a controlled environment test auth failure, malformed response, throttling, timeout after success, empty filtered page, continuation cycle and duplicate identity. Record stable ordering, operation receipts and reconciliation. Redact secrets and avoid sending requests through a production REST Explorer.
7. **Source and delegation:** Inspect the installed Studio/repository workflow and shared credential boundary. Exercise branches/review and a delegate's allowed/denied file actions with approved test identities. Verify exported artifacts and target installation separately; remove disposable test credentials only under their normal lifecycle process.
8. **Release and recovery:** Use isolated ATF fixtures or an equivalent written regression pack for clean install, upgrade and negative personas. Inventory excluded data/configuration, schema loss risk and custom UI component retrieval. Restore a specific version/data set in nonproduction and prove later valid changes survive the recovery plan.

### Executed local JavaScript workbook

**PRACTICAL DEPTH:** Run the following as a `.js` file with Node.js. All 38 checks passed using Node 24.18.1. No packages, ServiceNow APIs, authenticated instance, outbound endpoint or notification are used. The access function uses trusted fixture labels and an explicit application policy; it is not authentication or an ACL engine. Pagination has known fixture continuations and no concurrent changes. Receipts are sequential and in memory, with no claim of crash-safe or distributed atomicity. Node execution does not establish compatibility with a particular ServiceNow JavaScript mode.

```javascript
'use strict';
const assert = require('node:assert/strict');
const checks = [];
function check(name, actual, expected) {
  assert.deepStrictEqual(actual, expected, name);
  checks.push(name);
}

// Trusted fixture labels, not authentication or a ServiceNow ACL engine.
function allow(route, controls) {
  if (!controls.authenticated || !controls.userAcl) return false;
  if (route === 'script') {
    return controls.scopeRead && controls.callingPrivilege && controls.targetCaller;
  }
  if (route === 'rest') return controls.webService;
  return false;
}
const permitted = { authenticated: true, userAcl: true, scopeRead: true,
  callingPrivilege: true, targetCaller: true, webService: true };
check('script gates allow', allow('script', permitted), true);
check('rest gates allow', allow('rest', permitted), true);
check('script scope read matters', allow('script', {...permitted, scopeRead: false}), false);
check('rest uses its own route gate', allow('rest', {...permitted, scopeRead: false}), true);
check('rest web-service gate matters', allow('rest', {...permitted, webService: false}), false);
check('script does not use web-service gate', allow('script', {...permitted, webService: false}), true);
check('caller privilege matters', allow('script', {...permitted, callingPrivilege: false}), false);
check('target caller decision matters', allow('script', {...permitted, targetCaller: false}), false);
check('user permission remains necessary', allow('rest', {...permitted, userAcl: false}), false);
check('identity label alone insufficient', allow('script', {...permitted, userAcl: false}), false);
check('unauthenticated fixture denied', allow('rest', {...permitted, authenticated: false}), false);
check('unknown route denied', allow('other', permitted), false);

function rolePass(actual, required) {
  return actual.some(role => required.includes(role));
}
check('junior fails senior-only table requirement', rolePass(['junior'], ['senior']), false);
check('intentional table policy includes junior', rolePass(['junior'], ['junior', 'senior']), true);
check('private field still excludes junior', rolePass(['junior'], ['senior']), false);
check('derived value needs every contributor', [true, false].every(Boolean), false);

// Page limit is applied to the source slice, then access filtering occurs.
// Explicit next offsets come from this fixed fixture, not a real Table API.
const source = [1, 2, 3, 4, 5, 6].map(id => ({id, visible: id === 3 || id === 6}));
function page(offset, limit) {
  return { rows: source.slice(offset, offset + limit).filter(row => row.visible).map(row => row.id),
    next: offset + limit < source.length ? offset + limit : null };
}
function collect(readPage) {
  const seen = new Set();
  const records = new Set();
  const output = [];
  let offset = 0;
  while (offset !== null) {
    if (seen.has(offset) || seen.size >= 10) throw new Error('continuation cycle or bound');
    seen.add(offset);
    const result = readPage(offset, 2);
    for (const id of result.rows) {
      if (records.has(id)) throw new Error('duplicate identity');
      records.add(id);
      output.push(id);
    }
    offset = result.next;
  }
  return output;
}
function throws(action) { try { action(); return false; } catch { return true; } }
check('first page is empty but has continuation', page(0, 2), {rows: [], next: 2});
check('later authorized records remain reachable', collect(page), [3, 6]);
check('empty-page stop would omit both records', page(0, 2).rows.length, 0);
check('cycle rejected', throws(() => collect(() => ({rows: [], next: 0}))), true);
check('duplicate record rejected', throws(() => collect(offset =>
  ({rows: [3], next: offset === 0 ? 2 : null}))), true);

// Deliberately small application query contract; never parses encoded queries.
function validFilter(filter) {
  return filter !== null && typeof filter === 'object' && !Array.isArray(filter)
    && Object.keys(filter).sort().join(',') === 'field,op,value'
    && ['state', 'number'].includes(filter.field) && filter.op === 'eq'
    && typeof filter.value === 'string' && filter.value.length > 0
    && filter.value.length <= 32 && !/[\^\r\n]/.test(filter.value);
}
check('allowed structured filter', validFilter({field: 'state', op: 'eq', value: 'open'}), true);
check('unknown field rejected', validFilter({field: 'satte', op: 'eq', value: 'open'}), false);
check('unexpected operator rejected', validFilter({field: 'state', op: 'script', value: 'open'}), false);
check('encoded clause injection rejected', validFilter({field: 'state', op: 'eq', value: 'open^ORactive=true'}), false);
check('extra field rejected', validFilter({field: 'state', op: 'eq', value: 'open', admin: true}), false);
check('array rejected', validFilter([]), false);

// Sequential in-memory receipt and version guard: no crash durability guarantee.
const target = {version: 3, state: 'open'};
const receipts = new Map();
function apply(operation) {
  if (!operation || typeof operation.key !== 'string' || !operation.key
      || !Number.isInteger(operation.expected) || !['open', 'closed'].includes(operation.state)) {
    return 'invalid';
  }
  const payload = JSON.stringify([operation.expected, operation.state]);
  if (receipts.has(operation.key)) {
    return receipts.get(operation.key) === payload ? 'replayed' : 'conflict';
  }
  if (target.version !== operation.expected) return 'stale';
  target.version += 1;
  target.state = operation.state;
  receipts.set(operation.key, payload);
  return 'applied';
}
const close = {key: 'request-7-close', expected: 3, state: 'closed'};
check('first operation applies', apply(close), 'applied');
check('lost acknowledgment retry finds receipt', apply(close), 'replayed');
check('key reuse with different body conflicts', apply({...close, state: 'open'}), 'conflict');
check('stale distinct operation rejected', apply({...close, key: 'another'}), 'stale');
check('newer repair applies', apply({key: 'repair', expected: 4, state: 'open'}), 'applied');
check('old exact replay does not overwrite repair', apply(close), 'replayed');
check('current state preserves repair', target, {version: 5, state: 'open'});
check('only applied operations have receipts', receipts.size, 2);
check('Boolean revision rejected', apply({key: 'invalid', expected: true, state: 'closed'}), 'invalid');
const counts = [24, 24, 24, 24, 12, 12];
check('public practice count total', counts.reduce((a, b) => a + b, 0), 120);
check('practice proportions match current blueprint', counts.map(n => n / 120 * 100), [20,20,20,20,10,10]);
console.log(JSON.stringify({passed: checks.length, checks, authorizedIds: collect(page),
  target, receiptCount: receipts.size, nodeVersion: process.version}, null, 2));
```

Expected output includes `passed: 38`, authorized IDs `[3, 6]`, target version 5/state `open` and two applied-operation receipts. Practice-bank arithmetic describes public catalog metadata; it computes no passing score.

## Readiness checks

These are original explanation prompts, not reconstructed exam items. Answer, explain a failure case and identify the evidence you would collect.

1. **Can I explain when ServiceNow is and is not a good application platform fit?**

   Describe the work, actors, data, workflows and operational constraints. Reuse a supported capability where it fits; reject a platform choice whose latency, volume, UX or ownership requirements cannot be supported.

2. **Can I turn actors, outcomes and authoritative data into a lifecycle model?**

   Give every entity a stable identity, authoritative owner, state transitions, permitted writers and retention/recovery rules. Model the business lifecycle before choosing screens.

3. **Can I justify extending a table versus creating one?**

   Extension inherits fields and behavior, including security and automation. Choose it only when those semantics fit; document licensing and upgrade implications rather than extending solely to save typing.

4. **Can I model references and many-to-many relationships intentionally?**

   A reference links a governed record; a many-to-many table represents multiple relationships and can carry relationship-specific data. Avoid duplicating display values as if they were stable keys.

5. **Can I distinguish scope isolation from user authorization?**

   Scope controls artifact interaction; user authorization governs what an executing identity may do. A permitted cross-scope call does not authorize every user or field.

6. **Can I identify application files and the current scope in each development tool?**

   Inventory tables, scripts, flows, roles and other files under their actual scope. Verify the active context and stored artifact instead of assuming two builder views create independent copies.

7. **Can I explain why a module role does not secure a table?**

   Module roles control navigation. Effective table/field authorization must still reject direct API or record access when the user lacks permission.

8. **Can I compare App Engine Studio and Studio without assuming release-static behavior?**

   Compare the supported tasks and authoritative artifacts in the installed release. A tool name or screenshot from an older course does not establish current source-control or deployment behavior.

9. **Can I distinguish dictionary data definition, form layout, and view?**

   Dictionary entries define stored fields and metadata; layouts and views expose selected presentation. Removing a form field does not remove its database value or API accessibility.

10. **Can I choose UI Policy, Client Script, data policy, Business Rule, or flow by context?**

   Use client mechanisms for interaction, ACLs for authorization, server validation for required data behavior and workflow tools for process coordination. List alternate writers and bypass/context assumptions.

11. **Can I state which client/server APIs are available in a given execution context?**

   Client APIs belong to their supported browser experience; server APIs belong to server execution contexts. A Node or browser JavaScript example does not prove ServiceNow runtime API availability.

12. **Can I avoid client-side-only enforcement of trusted rules?**

   Enforce trusted requirements on the server and test a permitted alternate entry point that omits the UI. A hidden field, onSubmit check or module filter alone is insufficient.

13. **Can I design and secure a record producer and resulting record?**

   Constrain variables, normalize validated input and secure the resulting table/fields. Record producer convenience does not supply all downstream authorization or lifecycle rules.

14. **Can I test platform UI/workspace/portal boundaries for the actual target?**

   Test actual workspace, portal or platform behavior with allowed and denied personas. Capture stored results and failures rather than inferring compatibility from a classic form.

15. **Can I distinguish navigation, execution, record, field, and cross-scope control?**

   Navigation, callable execution, record/field decisions and scope interaction are separate controls. Identify which gate failed before changing any permission.

16. **Can I explain table/field ACL matching, roles, conditions and scripts?**

   An applicable rule combines its required checks, with a qualifying role from its role list. Both table and field access matter; multiple rules, inheritance and Deny-Unless require actual effective-decision evidence.

17. **Can I capture both allowed and denied security-debug evidence?**

   Pair each intended operation with a near-miss denied identity and preserve the rule trace. Administrator success or one allowed screenshot cannot establish least privilege.

18. **Can I use GlideSystem security methods without hard-coded identity shortcuts?**

   Use documented context/role methods with explicit business policy. Avoid hard-coded user IDs, client-supplied identity claims and assumptions that every server API enforces ACLs automatically.

19. **Can I interpret Application Access and cross-scope privilege settings?**

   Distinguish calling-application privileges, target-table settings and restricted-caller decisions. Cross-scope CRUD switches govern scripts; the web-service route has its own enablement and still requires user permission.

20. **Can I design a least-privilege delegated developer role?**

   Limit the application, file types and allowed development actions, then test prohibited edits and deployment. Delegation is not a reason to give broad administrator access; global-scope support differs.

21. **Can I choose a flow, rule, Script Include, event, or schedule by timing and ownership?**

   Choose by synchronous data requirements, reusable logic, process orchestration and ownership. Separate a durable business action from its event or notification so retries can be reconciled.

22. **Can I explain before, after, async, and display Business Rule behavior?**

   Before logic participates in the current save, after logic suits related work, display prepares form context and async work is deferred without guaranteed ordering. Async scripts lack previous-record context.

23. **Can I prevent automation recursion and duplicate side effects?**

   Use precise conditions, stable operation identity and durable receipts. Do not call current.update again merely to persist before-rule changes, and do not disable workflow as a generic recursion fix.

24. **Can I make properties typed, documented, safe, and environment-aware?**

   Specify type, default, owner, allowed values, environment scope and failure behavior. Manage secrets through the intended credential mechanism and validate missing/invalid configuration.

25. **Can I design event, schedule, and email failure/abuse behavior?**

   Define trustworthy producers, recipients, payload, schedules and correlation. Test duplicates, spoofed/invalid input, partial failures and cleanup without enabling real notification delivery here.

26. **Can I find Flow execution and server diagnostic evidence without leaking secrets?**

   Trace a stable operation identifier through flow/server evidence and the resulting business state. Log only necessary diagnostics and avoid recording credentials or full sensitive payloads.

27. **Can I build ATF and negative tests around consequential automation?**

   Assert the business result and negative paths with isolated test-created records/users. ATF runs in nonproduction; transported tests and rolled-back fixture data do not guarantee external side effects were undone.

28. **Can I profile imported source data before creating a transform?**

   Check source ownership, stable keys, duplicate/null values, types, encoding, reference validity and sensitivity before loading. Preflight the existing target as well as the incoming file.

29. **Can I explain staging, transform maps, coalesce, scripts, rejects and reconciliation?**

   Staging receives data; transforms map it; coalesce matches it. Matching alone does not validate uniqueness or prevent stale overwrites. Reconcile disjoint outcomes and exact target identities/values.

30. **Can I make an import safe to rerun and roll back?**

   Define repeat semantics and retain the affected before/after identities or a recoverable migration plan. Reversal must account for later legitimate changes rather than deleting everything touched by a run.

31. **Can I distinguish inbound/outbound REST and supported connection mechanisms?**

   Inbound exposes a ServiceNow contract; outbound calls another system. Each needs its own scoped identity, supported connection, endpoint/version, schema, network and error policy.

32. **Can I handle authentication, pagination, timeout, rate limit, retry and idempotency?**

   Separate response success, business completion and durable acknowledgment. Paginate with endpoint-specific continuation and ordering; an empty ACL-filtered page may not be the end. Reconcile uncertain writes before retrying.

33. **Can I test an integration's denied and failure paths in a controlled environment?**

   Use synthetic data and a controlled endpoint to exercise 401, malformed input, timeout, throttling, empty/duplicate pages and partial completion. Confirm denied fields and exact business state, not just HTTP status.

34. **Can I choose repository, Git, or update set for the intended artifact?**

   Git records supported application metadata/history; application repository distributes versions; update sets transport selected configuration. None is a full business-data backup or a substitute for installed-state checks.

35. **Can I prevent conflicting development and protect repository credentials?**

   Follow the supported Studio workflow, coordinate edits and review credential scope/ownership. The documented shared repository credential set limits what a generic Git identity model proves.

36. **Can I inventory dependencies and environment-specific configuration before release?**

   List plugins, schemas, roles, scripts, flows, environment values, credentials and data migrations. Identify excluded artifacts and dependency order before promotion, with accountable owners.

37. **Can I demonstrate clean install, persona smoke test, observability and rollback?**

   Start from a clean target or known base, verify intended/denied personas, inspect operational signals and rehearse a specific recovery. Prove configuration and data outcomes independently.

38. **Can I keep the mainline blueprint separate from release delta material?**

   The canonical mainline blueprint governs study scope; product previews and annual maintenance are separate. A new documentation family does not establish an exam transition.

39. **Can I state the 60-question/90-minute Pearson and 90-day registration contract?**

   The fresh canonical browser main states 60 questions, 90 minutes and Pearson/OnVUE delivery. Registration/payment starts the 90-day schedule-and-complete window; recheck the actual appointment terms.

40. **Can I explain the undisclosed cut score, conditional result, annual delta and CMP boundaries?**

   The cut score is undisclosed, results may be audited and section percentages are not a passing formula. Holders must follow assigned annual deltas and CMP obligations; practice scores and old public dates do not prove compliance.

## Final preparation

- Reopen KB0011498 and verify its date, 20/20/20/20/10/10 split, objectives, Pearson contract, scoring statement and maintenance terms.
- Compare the official MeasureUp distribution with the blueprint; allocate by the blueprint and treat a mismatch as a revalidation signal.
- Rebuild one scoped application without a tutorial, using non-admin allow/deny tests, repeatable imports/integrations, source review, automated tests, clean promotion and rollback.
- Use only ServiceNow's official MeasureUp practice for exam-style questions; convert every miss into a blueprint, current-documentation, or lab task.
- Verify actual release and UI/API context rather than combining legacy Workflow, old Studio instructions, current Flow/Workflow Studio, and a delta guide as if they were one baseline.
- Treat the certification as a checkpoint. Production development still requires architecture, security/privacy, accessibility, testing, change control, operational ownership and recovery review.


## Places to learn

This is not a complete list. Select resources for demonstrated gaps. Public landing metadata is not a lesson, exam-question or quality audit. Times are planning estimates unless identified as earlier publisher metadata; account-only content, blocked resources and proposed instance work remain distinct.

| Use and reading boundary | Resource | Access | Estimated time |
|---|---|---|---:|
| Full fresh unsigned browser main; 22 subtopics and exam contract | [Certified Application Developer Mainline Exam Blueprint](https://learning.servicenow.com/lxp/en/credentials/certified-application-developer-mainline-exam-blueprint?id=kb_article_view&sysparm_article=KB0011498) | Public browser; direct shell | 20–30 min estimate |
| Official path entry; current assignments/duration not visible | [Certified Application Developer Learning Path](https://learning.servicenow.com/lxp/en/now-platform/certified-application-developer?course_id=4c12ba8c87c39ad4a3bc40c5cebb3526&id=learning_content_prev) | Account/loading shell | 30–45 min planning estimate |
| Earlier three-day ILT anchors not reverified; PDF blocked | [ServiceNow University Technical Training Catalog](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/other-document/technical-training-portfolio.pdf) | HTTP 403 | Earlier 10–20 min reading estimate |
| Older Washington-labeled course route; interior/duration unavailable | [Scripting in ServiceNow Fundamentals](https://learning.servicenow.com/lxp/en/now-platform/scripting-in-servicenow-fundamentals-on-demand-washington?course_id=f424ca5a87f71e143a3a84c7cebb3509&id=learning_course_prev) | Account/loading shell | Earlier three ILT days not reverified |
| Find current Application Development Fundamentals assignment | [ServiceNow University Credential Catalog](https://learning.servicenow.com/lxp/en/credentials) | Account/entry shell | Current course duration unverified |
| Current Welcome recommended by blueprint; no lesson interior | [Welcome to ServiceNow — current recommended course](https://learning.servicenow.com/lxp/en/now-platform/welcome-to-servicenow?course_id=386f3cf847b36a90c00af235126d430c&id=learning_course_prev) | Account/loading shell | Earlier three hours not reverified |
| Product entry only; specific references below provide technical evidence | [ServiceNow Product Documentation](https://www.servicenow.com/docs/) | Public shell/browser docs | 15–30 hr selected study estimate |
| PDI/learning entry only; no instance allocated | [ServiceNow Developer Program](https://developer.servicenow.com/) | Public entry/account | 1–2 hr setup plus 20–40 hr labs estimate |
| Public 120-question March 2026 listing; no demo/question interior | [ServiceNow CAD Practice Test](https://www.measureup.com/servicenow-cad-practice-test.html) | Paid product/public metadata | 3–5 hr study estimate |
| Official channel title/footer only; no playback | [ServiceNow Developers YouTube Channel](https://www.youtube.com/@servicenowdevprogram) | Public video platform | 3–8 hr selected study estimate |
| Brazil September 10 main body: scope, namespace and instance planning | [Plan before you build](https://www.servicenow.com/docs/r/application-development/plan-before-you-build.html) | Public/browser | 30–60 min plus practice |
| Employee article main read; junior/senior example and API claims qualified, no attachment | [ServiceNow Custom Scoped App Security: A Developer's Guide to Access Control Lists](https://www.servicenow.com/community/developer-articles/servicenow-custom-scoped-app-security-a-developer-s-guide-to/ta-p/3484927) | Public/community | 60–90 min plus practice |
| May 6–7 discussion/replies read; no guaranteed course sufficiency or mock endorsement | [CAD Exam Prep community discussion](https://www.servicenow.com/community/training-and-certifications/cad-exam-prep/td-p/3538814) | Public/community | 15–30 min estimate |
| Paid interior unavailable; earlier 2017 context remains historically dated | [ServiceNow Application Development](https://www.oreilly.com/library/view/servicenow-application-development/9781787128712/) | Paid/HTTP 403 | Earlier 11–15 hr reading estimate unverified |
| Paid syllabus/interior unavailable; earlier February 2026 metadata not reverified | [ServiceNow Certified Application Developer Ultimate Course](https://www.udemy.com/course/servicenow-certified-application-developer-cad-course-cloud-guru-amit/) | Paid/HTTP 403 | Earlier 6 hr 37 min unverified |
| Scheduling andprovider policy; full browser FAQ read during preceding CSA review | [Pearson VUE transition and scheduling FAQ](https://learning.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0013209) | Public/browser | 15–25 min estimate |
| Annual payment context; no assigned deadline or future window | [Certification Maintenance Program payment FAQ](https://learning.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0011114) | Public/browser | 10–20 min estimate |
| Selected effective-access main sections; no full engine execution | [Access control rules overview](https://www.servicenow.com/docs/r/platform-security/access-control/exploring-access-control-list.html) | Public/browser | 30–60 min estimate |
| Priority and unresolved no-Allow-If wording | [Deny-Unless ACL behavior](https://www.servicenow.com/docs/r/platform-security/access-control/acl-denial-behavior.html) | Public/browser | 15–30 min estimate |
| Timing, context, bypass and recursion main body | [Classic Business Rules](https://www.servicenow.com/docs/r/api-reference/business-rules-classic/c_BusinessRules.html) | Public/browser | 30–60 min estimate |
| Matching,duplicate target,case/empty options; indexed primary body | [Updating records using coalesce](https://www.servicenow.com/docs/r/integrate-applications/system-import-sets/c_ImportSetCoalesce.html) | Public/indexed body | 30–60 min estimate |
| Configuration capture and schema loss limits; complete main body | [Customizations tracked by update sets](https://www.servicenow.com/docs/r/application-development/system-update-sets/customizations-tracked-update-sets.html?contentId=Wesk3KW7yiI5hKC5y~QwUA) | Public/browser | 30–45 min estimate |
| Vendor August 13 announcement of eleven September 14–18 preview sessions; no playback | [Developer Passport Brazil release preview](https://www.servicenow.com/community/developer-passport-blog/introducing-the-developer-passport-brazil-release-preview/ba-p/3586556) | Public/vendor program | 15–25 min article estimate |
| Selected indexed GlideRecord/Secure/query ACL sections; not whole API reference | [Glide Server APIs — GlideRecordSecure and query ACLs](https://www.servicenow.com/docs/r/api-reference/scripts/p_GlideServerAPIs.html) | Public/indexed body | 45–90 min selected study estimate |
| Caller, target and restricted-caller settings; indexed main body | [Application access settings](https://www.servicenow.com/docs/r/application-development/c_ApplicationAccessSettings.html) | Public/indexed body | 20–40 min estimate |
| Cross-scope script CRUD versus web-service enablement | [Table design and runtime access settings](https://www.servicenow.com/docs/r/application-development/r_TableApplicationAccessFields.html) | Public/indexed body | 20–40 min estimate |
| Brazil September 10main: nonproduction metadata integration, shared credential and sanitization | [Source control integration in ServiceNow Studio](https://www.servicenow.com/docs/r/application-development/servicenow-studio-classic/source-control-integration.html) | Public/browser | 30–60 min estimate |
| Brazil September 10main: isolated fixtures, nonproduction and custom UI transport limits | [Automated Test Framework design considerations](https://www.servicenow.com/docs/r/application-development/automated-test-framework-atf/automated-test-framework-design-considerations.html) | Public/browser | 30–60 min estimate |
| Brazil September 10main: pagination before ACLs, invalid queries, security and Explorer mutation | [ServiceNow REST API overview and query/security behavior](https://www.servicenow.com/docs/r/api-reference/rest-api-explorer/c_RESTAPI.html) | Public/browser | 45–90 min estimate |

The current bank's four 24-question domains and two 12-question domains total 120 and match 20/20/20/20/10/10. That resolves the older allocation discrepancy, not lesson completeness or passing readiness. The community discussion's four-domain 80% arithmetic now matches these weights, but a forum reply cannot guarantee which unlisted details are excluded from an explicitly non-exhaustive blueprint.

The [Pearson FAQ](https://learning.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0013209) distinguishes the test-center rescheduling threshold from OnVUE's timing. Recheck the current appointment before relying on either. The [CMP payment FAQ](https://learning.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0011114) is general policy; it does not verify your assigned annual task or deadline.
