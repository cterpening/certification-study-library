---
exam_code: MB-820
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-820
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# MB-820 Microsoft Dynamics 365 Business Central Developer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Checked against the June 10, 2025 official objective baseline and cited public sources on September 1, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#mb-820-coverage-record). The [official MB-820 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-820) is authoritative.

**Current baseline:** Skills measured as of June 10, 2025.<br>
**Upcoming blueprint change:** None announced as of September 1, 2026.<br>
**Lifecycle:** The [Business Central Developer Associate credential](https://learn.microsoft.com/en-us/credentials/certifications/d365-business-central-developer-associate/) is active, renews every 12 months, and has no announced retirement. The exam is 100 minutes, is offered in seven languages, and has a free Practice Assessment.<br>
**Freshness warning:** The published objective baseline is more than a year old. The 2025 change log mainly revised environment details and APIs; verify current Business Central runtime, AL extension, AppSource, authentication, testing, telemetry and API guidance before implementing a lab.<br>
**Official source:** [MB-820 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-820)

## How to use this guide

For each requirement, create a small extension contract:

1. business process and standard behavior being extended;
2. object model, table ownership and upgrade-safe extension point;
3. permissions, data classification and company scope;
4. transaction, validation, error and concurrency behavior;
5. user, report or API contract and accessibility/localization;
6. install/upgrade/uninstall and backward-compatibility behavior;
7. automated tests, telemetry and performance evidence;
8. build, validation, deployment and rollback path.

Work in a sandbox with source control. Publish small vertical slices, then test with least privilege and realistic data. Code that compiles but cannot survive an update, diagnose a failure or preserve accounting behavior is not production-ready.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Domain | Weight | Central question |
|---|---:|---|
| Describe Business Central | 10–15% | Can you place an extension in the product/app/update/AppSource architecture? |
| Install, develop and deploy | 10–15% | Can you configure, debug, package, publish, upgrade and maintain a multilanguage extension? |
| Develop by using AL objects | 35–40% | Can you model data, UI, reports, exchange, logic, permissions and queries with appropriate objects? |
| Develop by using AL | 15–20% | Can you implement Business Central patterns and safe, understandable AL behavior? |
| Work with development tools | 10–15% | Can you prove behavior with tests and operate it through telemetry? |
| Integrate with other applications | 10–15% | Can you build secure REST clients and durable Business Central API contracts? |

---

## 1. Describe Business Central

### Architecture and extension model

Business Central combines web/mobile clients, service tier/runtime, application packages and a database, with environment administration, authentication, telemetry and external services around them. Online is Microsoft-operated SaaS with managed updates and platform constraints. On-premises gives the customer more infrastructure/control and corresponding installation, security, update, capacity and compatibility responsibilities. Do not assume identical deployment, file-system, .NET, authentication or administration options.

The core solution exposes application behavior. The System Application supplies reusable platform-facing modules; the Base Application contains core business functionality; other first-party apps add capabilities. Extensions declare dependencies and add or extend objects without modifying the base package. Prefer public interfaces/events and supported extension objects. Never copy standard code merely because an event or interface has not yet been located.

An update lifecycle includes platform/runtime, Microsoft applications, dependencies and your app. Record compatibility ranges, obsolete-state progression, breaking-change policy, data schema evolution and upgrade code. Test against upcoming releases in a sandbox. Online update cadence rewards small dependencies and supported extension points; on-premises does not make overlayering a sustainable design.

> **Related item:** Platform, System Application, Base Application and partner extensions have different ownership and release cadence. An extension can compile against a dependency yet still break behavior if it relied on undocumented implementation.

### Apps and AppSource

An app package contains compiled AL objects, metadata, permissions, translations and declared resources/dependencies. Distinguish a per-tenant/customer customization from a broadly distributed AppSource app. AppSource submission adds technical validation, analyzers, object ranges/naming, licensing/monetization, privacy/security, documentation, support and marketing obligations.

Design the trial, setup, upgrade, uninstall and data-retention experience as product features. Validation begins in CI, not after upload. Treat AppSourceCop, CodeCop, PerTenantExtensionCop and UICop findings according to the target channel, current requirements and reviewed suppressions.

> **Related item:** “Published” can mean uploaded to a development tenant, installed for one customer, or validated/listed through AppSource. Each has a different trust and lifecycle contract.

---

## 2. Install, develop and deploy for Business Central

### Configure the development environment

Use Visual Studio Code with the current AL Language extension and an appropriate Business Central sandbox/container/on-premises instance. Authentication, server/environment/tenant, startup object, breakpoint and launch behavior live in current launch configurations; extension identity, publisher, name, version, dependencies, application/platform/runtime targets, object ranges, features and resource exposure belong in `app.json`. Workspace settings and analyzers belong at a reproducible scope rather than one developer's untracked machine.

Download symbols for declared dependencies. A workspace may contain multiple AL projects; make dependency direction explicit and avoid circular or “god library” packages. Namespaces reduce collisions and communicate ownership. Pin tool/runtime assumptions in source and CI, and keep credentials out of configuration files.

### Create, debug and deploy extensions

Start from a thin app, add an object, compile/package, publish to a sandbox and confirm installation. Debug with breakpoints, conditional breakpoints, call stack, variables, event subscribers and representative user/company context. Attach or snapshot debugging can help with existing/background behavior under supported conditions. Reproduce without administrator permissions and measure before changing code.

Deployment has distinct publish, synchronize, install, upgrade and uninstall stages. Development publishing may combine stages for convenience; production automation must surface each failure and retain package/version evidence. Increment versions, preserve dependency compatibility, and decide whether data is retained on uninstall. Installation code initializes new setup safely; upgrade code migrates existing data exactly once. Make it idempotent, resumable where possible and test from every supported prior version.

Translation uses generated XLIFF and stable labels. Localize captions, messages, reports and user assistance; do not concatenate grammar-dependent sentences. `ResourceExposurePolicy` affects source/debug exposure and must match support/IP needs. Maintain deprecation with obsolete reason/state/tag and a migration path before removal.

> **Related item:** Schema synchronization makes metadata compatible; install code establishes first-use state; upgrade code transforms an installed prior version. They solve different lifecycle problems.

---

## 3. Develop by using AL objects

### Tables, enums and pages

Tables own persisted fields, keys, relations, validation triggers, calculated FlowFields and data classification. Choose a stable primary key, selective secondary keys and SumIndexFields only when their read benefit justifies write/storage cost. Table extensions add fields/keys/field groups to supported tables. Preserve standard validation by using `Validate` when business rules must run; direct assignment has different semantics.

Enums provide named extensible values when the domain is finite; use interfaces or event-driven behavior when each value requires varying implementation. Treat enum ordinal compatibility carefully across integrations and upgrades.

Choose page types by interaction: List/Card for master records, Document/Worksheet for transactional entry, ListPart/CardPart for composition, RoleCenter for role navigation/activity, API pages for service contracts and other specialized types when warranted. Page extensions add fields/actions/parts or modify supported properties without cloning the base page. Set `ApplicationArea`, captions, tooltips, usage category and accessibility-relevant behavior. UI visibility is never authorization.

Role Centers combine navigation, activities/cues, lists, headlines and parts around a job. Cues should have a clear filter, time/company scope and drill-through. Avoid expensive synchronous calculations on page open.

> **Related item:** A table defines durable data and rules; a page presents an interaction; a page extension modifies presentation; a profile selects a role experience. Keeping business logic out of pages improves reuse and testing.

### Reports

A report object defines data items/columns, request page, triggers/functions and one or more layouts. Model parent/child data items with correct links, filters, sort and temporary/aggregated data. Use a query when it produces a clearer or more efficient dataset. Request pages expose parameters and saved settings; validate them before expensive work.

Choose RDLC for precise paginated output, Word for editable business-document layouts and Excel for analytical/tabular output under current support. Use labels/translations and recipient language/region. A document report needs header/line/totals, copy/currency/tax, pagination and empty/large-data tests. Report extensions add to supported datasets/layouts; substitution replaces a report for a registered context and must preserve expected contract. Processing-only reports run logic without rendered output and need progress, locking, retry and telemetry design.

### XMLports and queries

An XMLport defines schema nodes, element/attribute/text/field nodes, direction, format, encoding, namespaces, separators and triggers. Use it when its structured import/export pipeline fits. Validate external input, avoid leaking sensitive fields and make imports restartable. Invoking an XMLport from AL does not remove its transaction and error obligations.

Query objects join data items, select/filter/sort columns and aggregate supported values. Understand join type and cardinality before assuming row counts. Set filters before opening, read results through the query lifecycle and close resources. A query can outperform nested record loops and feed a report/API, but only when keys, selectivity, company scope and result size are controlled.

> **Related item:** XMLports define structured file/data exchange, queries define read models, reports define user output and APIs define service contracts. Similar-looking rows do not make these objects interchangeable.

### Codeunits, events and interfaces

Codeunits encapsulate business behavior, services, subscribers, tests and lifecycle code. Keep procedures cohesive and expose the smallest stable surface. A table/page trigger belongs to that object's lifecycle; an integration/business event announces an extensibility point; a subscriber reacts without modifying the publisher. Avoid ordering assumptions among independent subscribers. IncludeHandled patterns can be powerful but create coupling and should follow current standard guidance.

Interfaces separate contract from implementations and can pair with enums for strategy selection. Define default/unknown behavior so a new extension value does not crash older consumers. Installation codeunits initialize new installs; upgrade codeunits move data based on versions/tags and must be tested with realistic prior data.

### Entitlements, permission sets and queries

Permission-set objects grant object permissions and may include/extend other sets. Entitlements determine which permissions a licensed user can receive; inherent permissions let code operate under specifically declared behavior and require careful threat modeling. Troubleshoot the complete call: UI/API entry, tabledata read/insert/modify/delete, indirect permissions and codeunit execution. Test least-privilege users rather than expanding rights until an error disappears.

> **Related item:** An entitlement establishes license-level availability; a permission set grants capabilities to users; inherent permissions apply to code execution. None should substitute for validating record scope or sensitive operations.

---

## 4. Develop by using AL

### UI experience and onboarding

Profiles connect users to Role Centers and page customizations; views package filters/sort/display for repeated work. The user-assistance model links tooltips, context help and conceptual guidance. Assisted Setup registers a guided wizard and completion state. Teaching tips/in-app tours explain controls in context, while onboarding checklists guide multi-step adoption. Make every layer dismissible, localizable, accessible and safe to resume.

Design for first-run, empty state, error recovery and repeated use. A wizard must validate before commit and avoid partial setup. A checklist item needs a meaningful completion signal, not merely a click.

### Development standards and data process

Business Central's functional table patterns communicate behavior: setup, master, supplemental/subsidiary, journal, document header/line, ledger entry, detailed entry, register and others. Follow standard field, key, numbering, blocking, posting and navigation conventions so integrations and users encounter predictable semantics.

The data process model separates mutable source/master/document data from posted, auditable ledger history. Transactions often validate documents, create entries/registers and update application/remaining state. Extend through events/interfaces around the standard posting process rather than creating parallel ledgers. Document patterns need header/line relationships, numbering, status, totals, release/post/correction behavior. Master patterns need setup defaults, number series, blocked state, lookup/drilldown and rename/delete policy.

> **Related item:** A journal prepares postings, a document models a business commitment/process, a ledger records posted facts, and a register groups entry creation. Reusing the names without the behavior produces misleading software.

### AL language and safe data behavior

Use clear variables, intrinsic/complex types, enums, records, collections, dates, options where legacy contracts require them, and explicit conversions. Procedures define parameters by value or `var`, return values and access modifiers. Use local/internal/public/protected behavior deliberately; broad public APIs become compatibility promises.

Statements and expressions implement branches, loops and calculations. Built-in functions cover text, date, numeric, collection, record and system behavior. Prefer readable intent over clever compression. When manipulating records, understand `Get`, `Find*`, `SetRange`, `SetFilter`, `SetCurrentKey`, `CalcFields`, `Insert`, `Modify`, `Delete`, validation triggers, locking and transaction boundaries. Filter before loops, retrieve only needed data and avoid repeated database calls.

Files in cloud scenarios generally flow through streams, temporary blobs and upload/download abstractions rather than arbitrary server paths. Validate type/size/encoding, sanitize names, protect content and dispose/clear state. Never store secrets in source, labels or downloadable configuration.

Errors roll back the current transaction under the applicable behavior. Use `Error` for invalid operations, try methods only where recovery is intentional, and error collection where multiple validation findings improve the user experience. Do not swallow exceptions. User messages must explain action, context and remediation without exposing secrets or internals.

> **Related item:** Access modifiers limit which AL consumers call code; permission sets limit what a user/code path may access; data classification describes sensitivity. Secure extensions need all three.

---

## 5. Work with development tools

### Automated and semiautomated testing

Install/run the Test Toolkit in an appropriate test environment and know the difference between Microsoft standard tests, your extension tests and user acceptance/page scripting. Test codeunits and test procedures need deterministic setup, action and assertion; use handler functions for UI interactions and isolation/rollback behavior as supported.

Cover happy path, validation, permission, upgrade, localization, concurrency, posting and integration failure. Create data through supported APIs/helpers where possible so tests do not depend on a tenant snapshot. CI should compile with analyzers, run tests, retain results and block incompatible artifacts. Page scripting can accelerate acceptance paths, but it does not replace AL unit/integration tests.

### Telemetry and performance

Configure Application Insights/telemetry using current environment and extension guidance. Correlate environment/tenant, company/user pseudonymous dimensions as permitted, app name/version, operation, duration, result and failure. Platform telemetry provides standard signals; custom telemetry records business/technical milestones that are not otherwise observable. Never emit personal data, secrets or full payloads.

Start performance work with evidence: slow AL/database calls, long-running reports, API latency, locks, errors or page load. Use telemetry, debugger/profiler and performance tooling under representative volume. Fix excessive reads, nested queries, wrong keys, unnecessary FlowField calculations, large result sets and synchronous external calls. Establish a baseline and regression test.

> **Related item:** Logs explain individual events, metrics summarize behavior, traces/correlation connect a request across steps, and alerts turn a signal into action. Custom telemetry without ownership and thresholds is only extra data.

---

## 6. Integrate Business Central with other applications

### Call REST services from AL

Use `HttpClient`, request/response/content/header types and JSON types to build a bounded outbound contract. Define method/URI, authentication, headers, timeout, request body, success statuses, response schema, correlation, retry and idempotency before coding. Outbound HTTP calls may need explicit permission/configuration. Keep credentials in an approved secret mechanism, use TLS and least privilege, and never log tokens or payload secrets.

Serialize with `JsonObject`, `JsonArray`, `JsonToken` and `JsonValue`; test missing, null, additional, wrong-type and oversized data. Check both transport completion and HTTP status. Bound retries to transient responses with jitter and idempotency; do not retry validation/authentication failures blindly. Avoid external calls inside a long database transaction because remote latency/failure extends locks and complicates rollback.

### Implement Business Central APIs

Prefer standard API endpoints where they satisfy the contract. A custom API page defines stable publisher/group/version/entity set/name metadata, source table, fields, keys/SystemId, insert/update/delete policy, delayed insert and supported isolation. Treat names/types/nullability/key semantics as a versioned public interface, separate from the UI page model.

Bound actions operate on a resource; unbound actions represent service operations not tied to one instance. Implement current OData action conventions, permissions, validation, transactionality and error mapping. Test ETags/concurrency, pagination, filters, company/environment identifiers, batch behavior and partial failure. Read Scale-Out can route read-only API/query workloads to a replica under supported configuration, which introduces read-after-write consistency considerations; never use it for a flow that requires immediate primary consistency.

> **Related item:** An API page exposes an inbound service resource, while `HttpClient` calls an outbound service. Both use HTTP/JSON, but ownership, authentication, retries, versioning and transaction boundaries reverse.

---

## Integrated scenarios

### Scenario 1: upgrade-safe compliance extension

A table extension adds classified compliance fields, a page extension presents them, and a permission set grants least privilege. An enum plus interface selects policy behavior; event subscribers extend validation/posting without cloning base code. Install/upgrade code initializes and migrates data idempotently. Multilanguage labels/help support users, automated tests cover prior versions and posting, AppSource analyzers run in CI, and telemetry proves validation outcomes without recording sensitive values.

### Scenario 2: operational document and report

A standard-pattern header/line document uses number series, status, validation and posting events. Role Center cues and views surface actionable records; Assisted Setup and checklist configure first use. A report uses a filtered data model, recipient language and Word/RDLC layout. A query replaces nested loops. Permission, concurrency, empty/large data, correction and performance tests protect the source-to-ledger behavior.

### Scenario 3: resilient fulfillment integration

A versioned API page exposes a bounded outbound-order resource with SystemId/ETag semantics and least privilege. A bound action requests a controlled transition. Separate AL code calls a carrier REST API with secret-safe authentication, JSON schema validation, timeout, correlation and idempotent retry outside the posting transaction. Telemetry connects request, response and business state; reconciliation finds uncertain outcomes. Read Scale-Out is used only for stale-tolerant status queries.

---

## Hands-on labs

1. **Architecture/app:** Diagram online/on-prem and platform/System/Base/extension ownership; create dependency/update/AppSource validation and breaking-change policies.
2. **Environment/lifecycle:** Configure AL project/workspace, symbols, analyzers and source; debug, package, publish, install, upgrade from prior data and test uninstall/data retention.
3. **Data/UI/security:** Build/extend table, enum, page, Role Center and profile; add keys/relations/FlowField/classification, permission set and least-privilege tests.
4. **Reports/exchange/query:** Build a document report with request page/two layouts/language, an XMLport and an aggregated query; measure nested-loop replacement.
5. **Logic/patterns:** Implement codeunit, procedures, event publisher/subscribers and interface strategy using master/document/ledger conventions and transaction-safe errors.
6. **Onboarding/files:** Add Assisted Setup, teaching tips, tour and checklist; import/export through streams/temp blob with size/type/encoding/error controls.
7. **Tests/telemetry:** Create test codeunits for validation, permissions, posting, upgrade and failure; run standard/custom tests and add privacy-safe custom telemetry/alert criteria.
8. **Integration/API:** Build outbound HttpClient/JSON logic and a versioned API page/action with auth, pagination, ETag, retry/idempotency, reconciliation and read-scale consistency tests.

## Knowledge checks

1. Which responsibilities differ between Business Central online and on-premises?
2. How do platform, System Application, Base Application and extensions differ?
3. Why can a supported dependency still hide behavioral coupling?
4. How does an AppSource app differ from a per-tenant extension?
5. Which settings belong in `app.json` versus launch/workspace configuration?
6. How do multi-project workspaces and dependencies avoid circular coupling?
7. Compare publish, synchronize, install, upgrade and uninstall.
8. What makes upgrade code safe across every supported prior version?
9. When use a table versus table extension?
10. How do key selection and FlowField/SumIndexField use affect performance?
11. When should an enum work with an interface?
12. How do page, page extension, profile and permission set divide responsibility?
13. What makes a Role Center cue actionable and performant?
14. How do report data model, request page and layout differ?
15. When use report extension, substitution or processing-only report?
16. When is XMLport the right exchange tool?
17. Why can a query outperform record loops, and when might it not?
18. Compare object triggers, event publishers and subscribers.
19. What ordering assumption must independent event subscribers avoid?
20. How do install and upgrade codeunits differ?
21. Compare entitlement, permission set and inherent permission.
22. What paths should least-privilege troubleshooting trace?
23. How do profiles, views, Assisted Setup, teaching tips and checklists differ?
24. Why should a checklist have a real completion signal?
25. Distinguish setup, master, document, journal, ledger and register tables.
26. Why should posting extensions use standard events rather than parallel ledgers?
27. When does `Validate` differ materially from assignment?
28. How should AL filtering and key selection precede loops?
29. Why are arbitrary server file paths a poor cloud design?
30. When use try methods or collected errors?
31. How do standard, extension and acceptance tests complement one another?
32. What makes custom telemetry safe and actionable?
33. Which evidence should precede a performance change?
34. How should an outbound HTTP retry policy classify failures?
35. What makes an API page a stable versioned contract?
36. When does Read Scale-Out create an unacceptable consistency risk?

---

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one primary route, build and upgrade one secure extension end to end, and add another resource only for a measured gap.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MB-820 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-820) | Free | 1–2 hours to map six domains and freshness gaps |
| [Application development best practices](https://learn.microsoft.com/en-us/training/paths/use-application-development-business-central/) | Free | 6 hours 17 minutes listed; 12–20 hours with AppSource/upgrade/test work |
| [Customization foundation](https://learn.microsoft.com/en-us/training/paths/foundation-customize-business-central/) | Free | 10 hours 8 minutes listed; 22–35 hours building/deploying objects |
| [Build reports](https://learn.microsoft.com/en-us/training/paths/build-reports/) | Free | 8 hours 2 minutes listed; 15–25 hours with layouts/data/performance |
| [AL application foundation](https://learn.microsoft.com/en-us/training/paths/application-foundation-al-language/) | Free | 9 hours 33 minutes listed; 20–35 hours coding/testing exercises |
| [Data management foundation](https://learn.microsoft.com/en-us/training/paths/data-management-foundation-business-central/) | Free | 3 hours 25 minutes listed; 8–15 hours with XMLport/query/file builds |
| [Interface with Business Central](https://learn.microsoft.com/en-us/training/paths/interface-with-business-central/) | Free | 4 hours 43 minutes listed; 12–25 hours with resilient API integrations |
| [Tailor roles and design the UI](https://learn.microsoft.com/en-us/training/paths/tailor-roles-design-ui/) | Free | 4 hours 16 minutes listed; 8–15 hours with onboarding/accessibility |
| [Essential development standards](https://learn.microsoft.com/en-us/training/paths/essential-development-standards/) | Free | 3 hours 43 minutes listed; 10–20 hours implementing standard patterns |
| [MB-820T00-A course](https://learn.microsoft.com/en-us/training/courses/mb-820t00) | Paid/provider-dependent | 5 days |
| [MicrosoftLearning MB-820 labs](https://github.com/MicrosoftLearning/MB-820-Business-Central-Developer-Certification) | Free; MIT | 12–25 hours; repository title/README retain sample-course artifacts, so use hosted lab index and verify current instructions |
| [Free MB-820 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/d365-business-central-developer-associate/practice/assessment?assessment-type=practice&assessmentId=66154329&practice-assessment-type=certification) | Free | 45–90 minutes plus remediation |
| [AL developer documentation](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/) | Free | 25–60 hours selected current reference/troubleshooting |
| [O’Reilly: MB-820 Certification Companion](https://www.oreilly.com/library/view/dynamics-365-business/9798868809262/) | Subscription/trial | 3 hours 48 minutes; November 2024 hands-on companion, gap-check against June 2025 APIs/current runtime |
| [Plataan MB-820 exam-preparation webinar](https://app-plataantv-web-prd-euw.azurewebsites.net/en/plataan/training-course/business-central/mb-820-exam-preparation-webinar) | Paid/live | 2 days; listed 2026 sessions including September 29–30, verify seats/times |
| [Microsoft Community MB-820 awareness session](https://techcommunity.microsoft.com/event/d3f367f5-77c3-4097-92a4-2bf95e15d11c/mb-820-certification-essentials-your-complete-guide-to-becoming-a-business-centr/4537934) | Free registration; event availability varies | About 1–2 hours estimated; verify recording/event access |
| [Microsoft Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner login required | Use the five-day course pattern for planning; signed-in event start/end times control |

The eight directly relevant official paths total **50 hours 7 minutes** before labs. Allow roughly **120–200 hours** for a developer new to Business Central to build, test, integrate, upgrade and operate the extension portfolio. No exact current Pluralsight, MeasureUp or Whizlabs MB-820 product was independently verified. Udemy products found during review were dominated by 157–1,500 question banks or guaranteed-pass claims, so none was included.

## Final readiness checklist

- [ ] I can explain online/on-prem, platform/System/Base/extension and AppSource lifecycle boundaries.
- [ ] I can configure, debug, package, publish, install, upgrade, translate and maintain multi-project AL extensions.
- [ ] I can choose/build/extend every measured AL object with data, UI, permission, performance and upgrade contracts.
- [ ] I can implement standard data/document patterns and safe AL procedures, records, files, transactions and errors.
- [ ] I can build deterministic test codeunits and privacy-safe telemetry tied to operational action.
- [ ] I can implement secure outbound REST/JSON and stable inbound API/action contracts, including concurrency and consistency.
- [ ] I can trace a requirement through source, analyzer, build, test, package, deployment, telemetry and rollback evidence.
- [ ] I rechecked the older official blueprint, lifecycle, runtime/API guidance and Practice Assessment before scheduling.

## Source notes

The June 10, 2025 study guide defines exam scope. Current Microsoft Learn paths, AL documentation and public course labs support implementation, but their platform/runtime detail may evolve beyond the older blueprint. Commercial sources are optional supplements and do not define objectives. All scenarios, labs and checks here are original; no dumps or recalled questions were used.
