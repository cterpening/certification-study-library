---
exam_code: SALESFORCE-PLATFORM-DEVELOPER
vendor_id: salesforce
official_blueprint: https://help.salesforce.com/s/articleView?id=005298965&language=en_US&type=1
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Salesforce Certified Platform Developer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The official guide, current Trailhead preparation content, learning resources, links, and integrity boundary were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#salesforce-platform-developer-coverage-record).

**Current baseline:** Developer Fundamentals 27%, Process Automation and Logic 28%, User Interface 25%, and Testing, Debugging, and Deployment 20%. Salesforce’s current display title omits the old “I”; Platform Developer I and PD1 remain useful search aliases for this same credential.<br>
**Version caveat:** The official Help guide still labels the exam Summer ’25, while current Trailhead preparation keeps the same weights and now explicitly includes Agentforce for Developers. Treat the Help objective list and contract as the published baseline, use Trailhead for current emphasis, and recheck both before scheduling.<br>
**Exam contract:** The Help guide lists 60 scored multiple-choice questions, up to five unscored questions, 105 minutes, 68% passing, USD 200 registration, USD 100 retake, and no formal prerequisite. The scheduling SKU may appear as `Plat-Dev-201`. Verify local taxes, languages, delivery, accommodations, version, and checkout details.<br>
**Experience target:** Salesforce describes a typical candidate as having one to two years of development experience and at least six months on Lightning Platform. Platform Administrator is recommended, not required. This credential is the prerequisite for Platform Developer II.<br>
**Upcoming change:** No retirement or dated blueprint replacement was found September 2, 2026. The stale seasonal label is itself a revalidation trigger.<br>
**Maintenance:** Complete the certification-specific Trailhead maintenance requirement once per year by its deadline or the credential expires.

## How to use this guide

Build one small application repeatedly rather than memorizing isolated syntax. Trace requirement → data/access model → declarative/code boundary → transaction → secure UI → tests → source-driven deployment → telemetry and rollback. For each feature, explain why it fits, what platform limit or security context applies, and how failure becomes observable.

Use an authorized Developer Edition, Trailhead Playground, scratch org, or sandbox. The scenarios and checks here are original. Do not use dumps, recalled live questions, copied superbadge solutions, or material marketed as “actual questions.”

> **About related items:** A `Related item:` callout adds prerequisite, architectural, release, or operational context. It supports the topic but does not assert that Salesforce uses that wording in the public blueprint.

## Blueprint map

| Domain | Weight | Evidence to produce |
|---|---:|---|
| Developer Fundamentals | 27% | Architecture/data/access decision record and limit-aware boundary |
| Process Automation and Logic | 28% | Bulk-safe Apex plus declarative interaction tests |
| User Interface | 25% | Secure LWC/Flow/Visualforce behavior across allowed and denied personas |
| Testing, Debugging, and Deployment | 20% | Deterministic tests, correlated diagnosis, versioned promotion and rollback |

## 1. Developer Fundamentals — 27%

Salesforce is multitenant: tenants share platform resources while metadata, data, and access remain logically isolated. Governor limits protect shared capacity. Design every transaction with bounded queries, DML, CPU, heap, callouts, asynchronous work, and data volume in mind. Limits are architectural constraints, not errors to catch after production.

The platform maps broadly to model–view–controller: sObjects and data form the model; Lightning Web Components, Flow screens, and Visualforce render views; Apex, platform services, controllers, and event handlers coordinate behavior. Real applications cross layers, so use MVC as a responsibility model rather than forcing every artifact into one box.

Prefer declarative behavior when it expresses the requirement clearly with acceptable scale, transaction, security, testability, source/deployment, and observability. Use Apex when logic, data access, transaction control, reuse, or execution semantics require code. Formulas calculate values; roll-up summaries aggregate eligible children; validation rejects invalid writes; Flow orchestrates supported processes. Mixing tools is normal, but overlapping writers and unclear order are dangerous.

Model durable business entities, cardinality, ownership, access, delete behavior, reporting, and integrations before writing code. Standard and custom objects expose fields and relationships through schema metadata. Lookup and master-detail have different dependency, sharing, ownership, cascade, and roll-up consequences. External IDs support deterministic matching and upsert; uniqueness and case-sensitivity choices matter.

Agentforce for Developers can assist with code, tests, explanation, or supported development work, subject to current product capability. Treat generated output as untrusted: avoid secrets and restricted data, constrain context, inspect dependencies and security, compile and test, review diffs, and retain human accountability. An agent’s plausible answer does not override platform documentation.

`Related item:` CRUD, field-level security, sharing, and execution context are different layers. Apex can run in contexts that do not automatically enforce every user-facing data-access expectation; make the intended sharing and user-mode behavior explicit and test denied cases.

## 2. Process Automation and Logic — 28%

Apex is strongly typed and object-oriented. Know primitives, sObjects, collections, enums, classes, interfaces, access modifiers, static versus instance state, method signatures, constructors, properties, annotations, and exceptions. Read control flow precisely: conditions, loops, early returns, collection iteration, null handling, and short-circuit evaluation all affect paths and limit use.

SOQL queries records and relationships; SOSL searches text across eligible objects; DML changes records. Bind variables separate values from query structure. Select only needed fields, constrain cardinality, understand parent/child relationship syntax, and never place per-record queries or DML inside an unbounded loop. Use lists, sets, and maps to collect keys, query once, compute in memory, and write in bulk. Database methods expose partial-success results when that behavior is intentionally handled; ordinary DML is atomic within the transaction.

Triggers receive batches, not single records. Keep entry logic thin, separate reusable service/domain behavior, compare old/new values when relevant, and make repeated execution safe. Do not use a static Boolean as a universal recursion strategy: transactions can contain multiple chunks and legitimate second passes. Prefer changed-field guards, idempotent results, ownership of each field, and explicit transaction design.

Order of execution connects validation, before-save flows, before/after triggers, duplicate and assignment behavior, after-save automation, rollups, commits, and post-commit work. Exact order is release-sensitive. Map every writer and side effect, test the full transaction, and diagnose observed logs rather than relying on a memorized oversimplification.

Choose asynchronous mechanisms by contract. Future methods are limited legacy-style fire-and-forget work; Queueable Apex supports richer job structure and chaining; Batch Apex processes large sets in executions; Schedulable Apex starts work on a schedule. Know what state serializes, which limits reset, how jobs are monitored, and how retries, duplicate delivery, partial work, and callouts are controlled.

Exceptions separate expected business outcomes from system failures. Catch only where you can add context, compensate, translate safely, or recover; do not swallow errors. Preserve record/job/correlation identifiers without exposing secrets. Custom exceptions communicate domain failures, while transaction rollback or savepoints must match the intended atomicity.

Combine Flow and Apex through stable contracts: invocable inputs/outputs, bulk behavior, null/error semantics, security context, versioning, and idempotency. Apex should not duplicate logic that Flow already owns, and Flow should not obscure code-required transaction behavior.

`Related item:` Platform events and callouts are useful application patterns, but the public guide excludes integration design from the expected candidate role. Learn only enough context to recognize transaction boundaries; do not displace the four published domains with advanced integration study.

## 3. User Interface — 25%

Use Lightning Web Components for modern reusable UI. Understand component files, public properties/methods, reactive state, templates, lifecycle, composition, Lightning Data Service/wire versus imperative calls, and event flow. Data generally travels down through properties and events travel up; avoid hidden coupling across components.

Prefer base components and Lightning Data Service where they meet the requirement because they provide platform integration and important security behavior. Apex controllers must expose only intentional methods, validate inputs, enforce the intended record/object/field access, and return safe errors. Cache only read operations whose results are actually cacheable. Never trust client-side visibility or validation as authorization.

Flow supplies guided UI and orchestration; LWC can host or extend experiences; Apex can supply controlled server behavior. Agentforce actions may invoke supported Apex/Flow contracts, but generated input is untrusted and potentially adversarial. Validate identity, authorization, types, ranges, records, side-effect confirmation, and replay/idempotency before changing data.

Visualforce remains in the published scope. Know standard versus custom controllers, extensions, expressions, view state, page actions, component use, output escaping, and how Visualforce behaves in Lightning Experience. It is often a legacy or specialized surface, not the default for new UI.

Prevent cross-site scripting by using framework escaping and avoiding unsafe DOM sinks; prevent SOQL injection with static queries/binds or strict allowlists for unavoidable dynamic structure; protect state-changing operations from unauthorized invocation; do not expose secrets in markup, JavaScript, URLs, logs, or errors. Test object, field, and record denial—not only the happy path.

`Related item:` Lightning Web Security and Content Security Policy reduce classes of browser risk but do not make arbitrary third-party JavaScript, unsafe DOM manipulation, or insecure Apex safe.

## 4. Testing, Debugging, and Deployment — 20%

Apex tests must be isolated, deterministic, assertion-rich, and meaningful beyond coverage. Create only the data needed, use `@testSetup` when shared setup helps, exercise bulk and limit-sensitive paths, call `Test.startTest()`/`Test.stopTest()` deliberately, and assert records, side effects, errors, and authorization behavior. Do not depend on org data unless a narrow platform case requires it. Mock callouts and control asynchronous completion.

Coverage is a deployment gate, not a quality metric. Test positive, negative, boundary, bulk, repeat, exception, mixed-success, recursion/order, and least-privilege paths. Controllers and flows need representative user/context testing as well as Apex classes and triggers. If generated tests only mirror implementation, they can preserve the same mistake; derive assertions from requirements.

Choose tools by evidence need. Salesforce CLI and DX projects support source, org authentication, retrieve/deploy, test, data, and automation workflows. VS Code provides a development surface. Developer Console can inspect logs and execute anonymous code for bounded diagnosis. Setup surfaces expose debug logs, Apex Jobs, Scheduled Jobs, Flow interviews/errors, and deployment results. Names and commands evolve, so verify current CLI help and documentation.

Debug from symptom and correlation ID to transaction/job, user, input, automation path, query/DML/CPU use, exception, and downstream effect. Reproduce with minimal synthetic data. Change one hypothesis at a time, add targeted instrumentation, and remove or reduce verbose logging afterward. A log that ends successfully does not prove the business outcome.

Use source control as the reviewed source of truth. A promotion record should include artifact/version, target org, dependencies, permissions, tests, destructive/manual/data steps, validation, approver, deployment result, post-deploy user journeys, monitoring, and rollback. Sandboxes and scratch orgs serve different fidelity and lifecycle needs. Change sets may fit connected-org metadata movement; Salesforce CLI and packaging support source-driven repeatability.

`Related item:` Metadata deployment does not automatically migrate business data, secrets, certificates, endpoint authorization, or every org-specific setting. Separate and verify those steps.

## Integrated scenarios

### Scenario 1: Bulk-safe entitlement calculation

When service records change, calculate entitlement outcomes from related configuration and expose status in an LWC. Produce the object/relationship and access model, declarative-versus-Apex decision, bulk trigger/service design, one-query/one-write collection approach, changed-field/idempotency guard, tests for 1/200 records and denied fields, and deploy/rollback evidence.

### Scenario 2: Guided partner request

A screen Flow collects a request, an LWC supplies a specialized editor, and invocable Apex validates and creates related records. Define the Flow/Apex contract, server-side authorization, tamper/duplicate handling, safe error display, transaction ownership, representative persona tests, monitoring, and what happens if an optional Agentforce front end proposes the inputs.

### Scenario 3: Observable asynchronous recalculation

A large configuration change queues recalculation. Select Queueable, Batch, or scheduled behavior based on volume and contract; define job state, chunking, limits, retry/idempotency, partial failure, correlation, operator dashboard, cancellation/escalation, tests, deployment order, and recovery without editing production data by hand.

## Hands-on evidence labs

1. **Data/access contract (60–90 min):** Build a three-object model and prove CRUD, field, sharing, relationship, external-ID, delete, and reporting consequences.
2. **Bulk Apex service (120–180 min):** Implement trigger plus service for 1 and 200 synthetic records with query/DML/CPU evidence and repeat safety.
3. **Query/search/data operations (75–120 min):** Exercise bound SOQL, relationships, aggregate query, SOSL, atomic DML, and handled partial success.
4. **Flow/Apex boundary (90–150 min):** Build an invocable bulk contract, fault behavior, versioning, and a Flow that does not duplicate field ownership.
5. **Secure LWC (120–180 min):** Build a component with LDS or Apex, allowed/denied personas, safe errors, input tampering tests, and accessible states.
6. **Visualforce/legacy review (60–90 min):** Trace controller, view state, escaping, access, and Lightning compatibility; document an LWC migration boundary.
7. **Testing and diagnosis (120–180 min):** Add positive/negative/bulk/async/security tests, reproduce one fault, correlate logs/job/records, and prove the correction.
8. **Source-driven release (90–150 min):** Promote a versioned project through disposable orgs, validate tests/user journeys, record dependencies, and rehearse rollback.

## Readiness checks

1. How does multitenancy lead to governor-limit-aware design?
2. Where do data, UI, and control responsibilities sit in the platform’s MVC model?
3. Which facts decide declarative, Apex, or a deliberate combination?
4. How do formula and roll-up fields differ from stored Apex results?
5. Which relationship choices affect ownership, sharing, delete, and aggregation?
6. Why do external ID, uniqueness, and case choices matter?
7. How will you validate Agentforce-generated development output?
8. Which access layers must code explicitly honor and test?
9. When does SOQL fit, and when does SOSL fit?
10. Why are queries and DML inside record loops unsafe?
11. When should partial-success Database methods be chosen?
12. What makes a trigger genuinely bulk-safe?
13. Why is one static recursion flag unreliable?
14. How do changed-field and idempotency guards differ?
15. Which writers participate in the complete save transaction?
16. When do Queueable, Batch, scheduled, and future work fit?
17. Which asynchronous failures and duplicates must be designed explicitly?
18. When should an exception be caught, translated, or allowed to roll back?
19. What belongs in a stable invocable Apex contract?
20. How do you prevent Flow and Apex from owning the same effect?
21. Which LWC data path fits LDS/wire versus imperative Apex?
22. Why can component visibility never provide authorization?
23. How do parent/child events and public APIs reduce component coupling?
24. Which input checks are required when an agent invokes an action?
25. When is Visualforce still relevant to this blueprint?
26. How do escaping, binds, and allowlists mitigate different vulnerabilities?
27. What does Lightning Web Security not guarantee?
28. Why is code coverage insufficient evidence of quality?
29. Which tests expose bulk, repeat, order-of-execution, and access defects?
30. What do `Test.startTest()` and `Test.stopTest()` isolate or complete?
31. How do Salesforce CLI, DX projects, Developer Console, and logs differ?
32. What is the smallest evidence chain for an asynchronous failure?
33. Why should verbose debug logging be time-bounded?
34. Which environment best matches each test objective?
35. What does source-driven deployment add beyond manual configuration?
36. Which data, secret, permission, and post-deploy steps stay separate from metadata?
37. What does the Summer ’25 label/current-Trailhead discrepancy require you to verify?
38. Which legacy “PD1” resources remain useful, and which gaps make them unsafe alone?
39. What annual action keeps the credential current?
40. Which authoritative pages will you recheck before scheduling?

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick resources that fit your gaps and learning style. Older “Platform Developer I” material can still teach Apex, SOQL, testing, Visualforce, and LWC, but reconcile it against the current four-domain scope, Flow, current tooling, and Agentforce for Developers.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official exam guide](https://help.salesforce.com/s/articleView?id=005298965&language=en_US&type=1) and [current credential page](https://trailhead.salesforce.com/credentials/platformdeveloperi) | Public | 25–40 min | Authoritative objectives, role boundary, contract, current display title, and version caveat |
| [Study for the Platform Developer Exam](https://trailhead.salesforce.com/content/learn/trails/platform-developer-i-certification-study-guide) | Free Trailhead | ~1 hr 15 min | Current domain orientation, official scenario practice, flashcards, and integrity rules |
| [Prepare for Your Salesforce Platform Developer Certification](https://trailhead.salesforce.com/users/strailhead/trailmixes/prepare-for-your-salesforce-platform-developer-i-credential) | Free Trailhead | ~31 hr 25 min across listed timed steps | Broad hands-on curriculum; select gaps rather than treating completion as exam readiness |
| [Platform Developer Maintenance (Winter ’26)](https://trailhead.salesforce.com/content/learn/modules/platform-developer-certification-maintenance-winter-26) | Free Trailhead | ~45 min | Recent platform-development change and combined Apex/Flow testing context |
| [Build Applications Programmatically (DEX450)](https://trailheadacademy.salesforce.com/classes/dex450-build-applications-programmatically-on-the-salesforce-platform) | Paid instructor-led | 5 days | Official guided Apex, LWC, Visualforce, testing, limits, and deployment practice |
| [Salesforce Certified Platform Developer I path](https://www.pluralsight.com/paths/salesforce-certified-platform-developer-i-update) | Paid | ~10 hr plus practice exam | Six-course structured route; verify Agentforce/current seasonal tooling gaps |
| [Salesforce Developer I Certification](https://www.oreilly.com/library/view/salesforce-developer-i/9798868803000/) | O’Reilly subscription/book | 4 hr 10 min listed / 205 pages | Compact 2024 Apex, LWC, Flow, security, testing, and DX foundation; supplement current deltas |
| [Complete Salesforce Certified Platform Developer 1](https://www.udemy.com/course/salesforce-developer/) by Anthony and Mike Wheeler | Paid | 13 hr 49 min | June 2026 guided code/application route; verify the official four-domain map |
| [Focus on Force Salesforce certification resources](https://focusonforce.com/) | Paid | 15–30 hr selected plus timed practice | Targeted explanations and original practice; verify current display title, release, and objective coverage |

Reject guaranteed-pass products, “actual question” files, VCE collections, unexplained answer banks, and courses advertising dumps. Quality practice explains why alternatives fail and sends you back to first-party documentation and hands-on evidence.
