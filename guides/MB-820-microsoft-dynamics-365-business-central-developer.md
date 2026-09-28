---
exam_code: MB-820
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-820
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# MB-820 Microsoft Dynamics 365 Business Central Developer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Checked against the June 10, 2025 official objective baseline and cited public sources on September 28, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#mb-820-coverage-record). The [official MB-820 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-820) is authoritative.

**Current baseline:** Skills measured as of June 10, 2025.<br>
**Upcoming blueprint change:** None announced as of September 28, 2026.<br>
**Lifecycle:** The [Business Central Developer Associate credential](https://learn.microsoft.com/en-us/credentials/certifications/d365-business-central-developer-associate/) is active, renews every 12 months, and has no announced retirement. The exam is 100 minutes, is offered in seven languages, and has a free Practice Assessment.<br>
**Freshness warning:** The published objective baseline is more than a year old. The 2025 change log mainly revised environment details and APIs; verify current Business Central runtime, AL extension, AppSource, authentication, testing, telemetry and API guidance before implementing a lab.<br>
**Official source:** [MB-820 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-820)

The [September deep review](../docs/research/2026-09-28-mb-820-deep-review.md) maps **75 detailed objectives**. The older 17-bullet summary is archived; the June 2025 baseline has not changed. Current runtime behavior and announced future removals are distinguished below.

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

### Current deployment and endpoint transitions

The [platform deprecation register](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/upgrade/deprecated-features-platform) describes these version boundaries. Record the actual tenant version before reproducing older training:

| Area | Documented boundary | Learning action |
|---|---|---|
| SaaS per-tenant app administration | From 2026 wave 1, use Business Central Admin Center or its API; in-client upload/installation is expected to be removed in 2027 wave 1 | Distinguish viewing installed apps from deploying a package; update CI deployment targets |
| Microsoft UI pages exposed as SOAP | Removal specified for v29 / 2026 wave 2 | Inventory affected endpoints and design supported APIs; this is not a claim that every SOAP endpoint is already removed |
| Microsoft-published pages exposed as OData | Removal specified for v30 / 2027 wave 1 | Use a purpose-built integration contract; the announced scope is not all OData queries or custom APIs |
| On-premises data-only permission sets | `UsePermissionSetsFromExtensions=false` ceases to be supported in v29 | Migrate permission definitions to AL objects and test effective access |

These are product changes, not newly added exam objectives. Future release dates are not proof that a particular tenant has been upgraded.

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

**Upgrade proof needs old data.** [Upgrade codeunits](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-upgrading-extensions) run preconditions, transformation and validation at company or database scope. Order among separate upgrade codeunits is not guaranteed. An upgrade tag prevents repeating a completed migration; register applicable tags for new companies and first-time installations too. Distinguish the installed data version from the target app version. Test a fresh install, every supported upgrade origin, failure/retry and a second company.

[AL-Go for GitHub](https://github.com/microsoft/AL-Go) provides separate PTE and AppSource templates plus build/test/release workflows. Use its documented update mechanism for shared workflow files, review the change and rerun compatibility tests. A successful pipeline is evidence about the tested artifact/environment; it does not replace data-upgrade or business acceptance checks.

## 3. Develop by using AL objects

### Tables, enums and pages

Tables own persisted fields, keys, relations, validation triggers, calculated FlowFields and data classification. Choose a stable primary key, selective secondary keys and SumIndexFields only when their read benefit justifies write/storage cost. Table extensions add fields/keys/field groups to supported tables. Preserve standard validation by using `Validate` when business rules must run; direct assignment has different semantics.

Enums provide named extensible values when the domain is finite; use interfaces or event-driven behavior when each value requires varying implementation. Treat enum ordinal compatibility carefully across integrations and upgrades.

Choose page types by interaction: List/Card for master records, Document/Worksheet for transactional entry, ListPart/CardPart for composition, RoleCenter for role navigation/activity, API pages for service contracts and other specialized types when warranted. Page extensions add fields/actions/parts or modify supported properties without cloning the base page. Set `ApplicationArea`, captions, tooltips, usage category and accessibility-relevant behavior. UI visibility is never authorization.

Role Centers combine navigation, activities/cues, lists, headlines and parts around a job. Cues should have a clear filter, time/company scope and drill-through. Avoid expensive synchronous calculations on page open.

> **Related item:** A table defines durable data and rules; a page presents an interaction; a page extension modifies presentation; a profile selects a role experience. Keeping business logic out of pages improves reuse and testing.

**FlowFields are calculations, not stored values.** [FlowField documentation](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-flowfields) explains that hidden page FlowFields can still be calculated. From v26, the Calculate only visible FlowFields feature can change that behavior. Record the feature state before comparing timings, and use explicit calculation when code needs a value. Hiding a field does not revoke access.

### Reports

A report object defines data items/columns, request page, triggers/functions and one or more layouts. Model parent/child data items with correct links, filters, sort and temporary/aggregated data. Use a query when it produces a clearer or more efficient dataset. Request pages expose parameters and saved settings; validate them before expensive work.

Choose RDLC for precise paginated output, Word for editable business-document layouts and Excel for analytical/tabular output under current support. Use labels/translations and recipient language/region. A document report needs header/line/totals, copy/currency/tax, pagination and empty/large-data tests. Report extensions add to supported datasets/layouts; substitution replaces a report for a registered context and must preserve expected contract. Processing-only reports run logic without rendered output and need progress, locking, retry and telemetry design.

### XMLports and queries

An XMLport defines schema nodes, element/attribute/text/field nodes, direction, format, encoding, namespaces, separators and triggers. Use it when its structured import/export pipeline fits. Validate external input, avoid leaking sensitive fields and make imports restartable. Invoking an XMLport from AL does not remove its transaction and error obligations.

Query objects join data items, select/filter/sort columns and aggregate supported values. Understand join type and cardinality before assuming row counts. Set filters before opening, read results through the query lifecycle and close resources. A query can outperform nested record loops and feed a report/API, but only when keys, selectivity, company scope and result size are controlled.

> **Related item:** XMLports define structured file/data exchange, queries define read models, reports define user output and APIs define service contracts. Similar-looking rows do not make these objects interchangeable.

### Codeunits, events and interfaces

Codeunits encapsulate business behavior, services, subscribers, tests and lifecycle code. Keep procedures cohesive and expose the smallest stable surface. A table/page trigger belongs to that object's lifecycle; an integration/business event announces an extensibility point; a subscriber reacts without modifying the publisher. Avoid ordering assumptions among independent subscribers. The pattern is named `IsHandled`. Microsoft recommends minimizing it because one subscriber can bypass validation and suppress later events. Prefer a meaningful interface or additive event; where the pattern is unavoidable, respect an already handled result and test coexistence with another extension. See [IsHandled guidance](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-use-ishandled-pattern).

Interfaces separate contract from implementations and can pair with enums for strategy selection. Define default/unknown behavior so a new extension value does not crash older consumers. Installation codeunits initialize new installs; upgrade codeunits move data based on versions/tags and must be tested with realistic prior data.

### Entitlements, permission sets and queries

Permission-set objects grant object permissions and may include/extend other sets. Entitlements determine which permissions a licensed user can receive; inherent permissions let code operate under specifically declared behavior and require careful threat modeling. Troubleshoot the complete call: UI/API entry, tabledata read/insert/modify/delete, indirect permissions and codeunit execution. Test least-privilege users rather than expanding rights until an error disappears.

> **Related item:** An entitlement establishes license-level availability; a permission set grants capabilities to users; inherent permissions apply to code execution. None should substitute for validating record scope or sensitive operations.

---

**Inherent permission has a narrow but consequential scope.** [InherentPermissions](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-inherent-permissions) applies only to objects in the same extension. Its optional scope can cover permissions, entitlements or both; the default is Both. It grants capability during the method/event execution, and administrators cannot remove that grant through ordinary permission-set management. Use small, controlled operations with explicit output boundaries; it is not a blanket override for another publisher's sensitive tables.

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

An unhandled error normally aborts the current uncommitted database work; it does not undo earlier commits or remote effects. A caught [try-method error](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-handling-errors-using-try-methods) is different: database writes in that method are not automatically rolled back. Consuming the Boolean return catches the error; calling the same attributed procedure without consuming its return behaves like an ordinary call. Online permits writes inside try methods, while on-premises blocks them by default. Keep recoverable parsing/validation separate from writes.

Consuming the Boolean result of [Codeunit.Run](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/methods-auto/codeunit/codeunit-run-method) introduces its own transaction contract: success commits that codeunit's changes, and an existing transaction must be committed before such a call. Do not add that precommit casually to a business operation that must be atomic. [CommitBehavior](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/attributes/devenv-commitbehavior-attribute) affects explicit commits within its scope, not the implicit commit from Codeunit.Run. Use error collection for user-correctable validation findings and preserve actionable error details without secrets.

> **Related item:** Access modifiers limit which AL consumers call code; permission sets limit what a user/code path may access; data classification describes sensitivity. Secure extensions need all three.

---

For read-heavy loops, [partial records](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-partial-records) select required fields before fetching. Touching an unloaded field triggers another load and can expose a concurrent modification/delete. Passing a partial record by value can cause repeated loads because the original iterator is not updated. Select the fields needed by called code; benchmark reads and writes separately instead of adding `SetLoadFields` everywhere.

## 5. Work with development tools

### Automated and semiautomated testing

Install/run the Test Toolkit in an appropriate test environment and know the difference between Microsoft standard tests, your extension tests and user acceptance/page scripting. Test codeunits and test procedures need deterministic setup, action and assertion; use handler functions for UI interactions and isolation/rollback behavior as supported.

Cover happy path, validation, permission, upgrade, localization, concurrency, posting and integration failure. Create data through supported APIs/helpers where possible so tests do not depend on a tenant snapshot. CI should compile with analyzers, run tests, retain results and block incompatible artifacts. Page scripting can accelerate acceptance paths, but it does not replace AL unit/integration tests.

The [testing support matrix](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-testing-application) disallows automated tests in Business Central online production. Online sandboxes support bounded manual verification, with restrictions on long or extensive runs; container-based environments are the documented default for large suites and CI gates. Test pages simulate interaction without displaying the actual client UI. Use a test runner and handlers so unexpected dialogs fail the test, and use `ASSERTERROR` only in test code.

### Telemetry and performance

Configure Application Insights/telemetry using current environment and extension guidance. Correlate environment/tenant, company/user pseudonymous dimensions as permitted, app name/version, operation, duration, result and failure. Platform telemetry provides standard signals; custom telemetry records business/technical milestones that are not otherwise observable. Never emit personal data, secrets or full payloads.

Start performance work with evidence: slow AL/database calls, long-running reports, API latency, locks, errors or page load. Use telemetry, debugger/profiler and performance tooling under representative volume. Fix excessive reads, nested queries, wrong keys, unnecessary FlowField calculations, large result sets and synchronous external calls. Establish a baseline and regression test.

> **Related item:** Logs explain individual events, metrics summarize behavior, traces/correlation connect a request across steps, and alerts turn a signal into action. Custom telemetry without ownership and thresholds is only extra data.

---

Use the supported [custom telemetry destinations](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-instrument-application-for-telemetry): Application Insights for online/on-premises, and Windows event log only on-premises. Define event meaning, correlation and dimensions before writing a signal. Count eventual business outcomes separately from retry attempts; otherwise a healthy recovery mechanism can make an attempt-based chart look like a business failure spike.

## 6. Integrate Business Central with other applications

### Call REST services from AL

Use `HttpClient`, request/response/content/header types and JSON types to build a bounded outbound contract. Define method/URI, authentication, headers, timeout, request body, success statuses, response schema, correlation, retry and idempotency before coding. Outbound HTTP calls may need explicit permission/configuration. Keep credentials in an approved secret mechanism, use TLS and least privilege, and never log tokens or payload secrets.

Serialize with `JsonObject`, `JsonArray`, `JsonToken` and `JsonValue`; test missing, null, additional, wrong-type and oversized data. Check both transport completion and HTTP status. Bound retries to transient responses with jitter and idempotency; do not retry validation/authentication failures blindly. Avoid external calls inside a long database transaction because remote latency/failure extends locks and complicates rollback.

**Current outbound controls.** The [HttpClient reference](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-httpclient) requires Allow HttpClient Requests for each relevant app, including libraries. Distinguish failure to obtain an HTTP response from a non-success response and from an invalid successful payload. Server-certificate checks default on from v26; v27 removes the old feature-key bypass. Fix the endpoint trust/hostname/chain rather than using disabled validation as the lab solution. A client certificate does not validate the server certificate. Online anti-SSRF controls block internal-IP destinations and cannot be disabled; on-premises behavior depends on supported platform settings. Keep those deployment differences explicit.

An external service may succeed before AL reports a timeout or a later local failure. A retried write needs a stable operation identity and recipient-side deduplication or a genuinely idempotent business operation. A local Processed flag alone cannot close that failure window.

### Implement Business Central APIs

Prefer standard API endpoints where they satisfy the contract. A custom API page defines stable publisher/group/version/entity set/name metadata, source table, fields, keys/SystemId, insert/update/delete policy, delayed insert and supported isolation. Treat names/types/nullability/key semantics as a versioned public interface, separate from the UI page model.

Bound actions operate on a resource; unbound actions represent service operations not tied to one instance. Implement current OData action conventions, permissions, validation, transactionality and error mapping. Test ETags/concurrency, pagination, filters, company/environment identifiers, batch behavior and partial failure. Read Scale-Out can route read-only API/query workloads to a replica under supported configuration, which introduces read-after-write consistency considerations; never use it for a flow that requires immediate primary consistency.

> **Related item:** An API page exposes an inbound service resource, while `HttpClient` calls an outbound service. Both use HTTP/JSON, but ownership, authentication, retries, versioning and transaction boundaries reverse.

---

### API compatibility, atomicity and read consistency

[API pages and queries cannot be extended](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-api-pagetype) through ordinary extension objects; publish a new supported API contract when the existing one lacks a field. Follow [custom-API identity guidance](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-develop-custom-api): a stable SystemId GUID and explicit publisher/group/version/entity names make a better integration key than a mutable display number. An API page supports permitted writes; an API query provides a read model. Select based on required operations, joins, shape, subscriptions and measured performance.

For [transactional OData batches](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/webservices/use-odata-batch), `Isolation: snapshot` runs the inner requests in one session. Atomic rollback depends on the invoked AL code not committing partway through. Explicit commits split the transaction; review implicit Codeunit.Run boundaries too. A batch envelope or successful outer HTTP response alone does not prove every business operation succeeded.

[Data-access intent](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-connect-apps-tips) can be overridden: the Database Access Intent List takes precedence over the request header, which takes precedence over the object's default. Modification requests require ReadWrite. ReadOnly expresses intent and does not guarantee replica routing. Most importantly, [online sandboxes cannot enable read scale-out](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/administration/database-read-scale-out-overview): their objects run against the primary, so a sandbox cannot demonstrate production replica delay. Use a local lag model for learning and authorized production-like telemetry for an actual routing/consistency claim.

## Worked examples

These original models isolate specific behaviors. The Python example runs locally; no AL compiler, Business Central server or external service was used.

### 1. Trace what an error can still leave behind

Start with an uncommitted update from 100 to 120. If an ordinary unhandled error aborts that transaction, the durable value remains 100. If the update was committed before the error, 120 remains. If a try-method error is caught, do not infer rollback: continuing and later committing can preserve earlier writes. Add a remote shipment to the timeline; a database rollback cannot recall that shipment. Label each boundary before deciding where recovery belongs.

### 2. Retry an external effect with the same identity

The recipient must atomically combine its deduplication record and effect. This single-threaded model demonstrates the contract only; it does not implement concurrency, persistence, authentication or retry scheduling.

```python
class Recipient:
    def __init__(self):
        self.requests = {}
        self.shipped = 0

    def accept(self, company, operation_id, quantity):
        key = (company, operation_id)
        if key in self.requests:
            if self.requests[key] != quantity:
                raise ValueError("Same operation ID has different content")
            return "existing"
        self.requests[key] = quantity
        self.shipped += quantity
        return "created"

recipient = Recipient()
pending = ("CRONUS-A", "dispatch-17", 4)
first = recipient.accept(*pending)
# Assume the sender fails before recording the response; pending survives.
retry = recipient.accept(*pending)
print(first, retry, recipient.shipped)  # created existing 4
```

Generating a new ID on retry would create another four-unit shipment. Reusing the ID with a different quantity must fail rather than silently return an unrelated result. A retained outbox row supplies identity across retries; recreating it requires preserving the original business-operation identity. Do not treat every DELETE 404 as success without checking endpoint and resource identity.

### 3. Joining at the wrong grain doubles a report

An order has two lines worth 100 and 50 and two shipment records. Joining lines to shipments by order alone produces four rows and a line sum of 300. The correct order value is 150. Aggregate each child collection to order grain first, or link by the intended line relationship. A query that executes quickly can still be wrong; reconcile row counts and totals before measuring speed.

### 4. A commit breaks all-or-nothing batching

Suppose a transactional batch sets A to 10, then B to 20, then fails validation, starting from A=B=0. With no intermediate commit, both remain zero after rollback. If the first request commits, A can remain 10 while later work rolls back. Inspect called code and subscribers; CommitBehavior is not a universal shield against every implicit commit. Compare returned inner results with persisted records.

### 5. Upgrade every company exactly once

Company A has 100 legacy records and B has 40. A company-scoped migration must transform 140 records across the two companies, then zero on a completed rerun. A single incorrectly shared completion flag could skip B's 40. Test a failure before completion, successful retry, new company and fresh installation; tag registration is part of the lifecycle, not merely a final line in a migration procedure.

### 6. Measure payload and business outcomes separately

For a hypothetical 1,000-row response, reducing selected data from 1,000 to 160 bytes per row changes the payload model from 1,000,000 to 160,000 bytes: 84% less, excluding protocol overhead. This is not an 84% latency guarantee, and subsequent JIT loads can erase the benefit.

Separately, 100 business operations make 120 HTTP attempts. Eighty succeed first time; twenty retry, fifteen then succeed and five ultimately fail. Eventual success is 95/100 = 95%; successful attempts are 95/120 ≈ 79.17%. Record both denominators and the five unresolved operations. A replica-lag demonstration needs observed lag; a sandbox's immediate primary read cannot establish a production bound.

## Integrated scenarios

### Scenario 1: upgrade-safe compliance extension

A table extension adds classified compliance fields, a page extension presents them, and a permission set grants least privilege. An enum plus interface selects policy behavior; event subscribers extend validation/posting without cloning base code. Install/upgrade code initializes and migrates data idempotently. Multilanguage labels/help support users, automated tests cover prior versions and posting, AppSource analyzers run in CI, and telemetry proves validation outcomes without recording sensitive values.

### Scenario 2: operational document and report

A standard-pattern header/line document uses number series, status, validation and posting events. Role Center cues and views surface actionable records; Assisted Setup and checklist configure first use. A report uses a filtered data model, recipient language and Word/RDLC layout. A query replaces nested loops. Permission, concurrency, empty/large data, correction and performance tests protect the source-to-ledger behavior.

### Scenario 3: resilient fulfillment integration

A versioned API page exposes a bounded outbound-order resource with SystemId/ETag semantics and least privilege. A bound action requests a controlled transition. Separate AL code calls a carrier REST API with secret-safe authentication, JSON schema validation, timeout, correlation and idempotent retry outside the posting transaction. Telemetry connects request, response and business state; reconciliation finds uncertain outcomes. Read Scale-Out is used only for stale-tolerant status queries.

---

## Hands-on labs

Use synthetic data in an appropriate development/test environment. These tenant labs were not executed during this review.

1. **Architecture and release:** Map ownership/dependencies and compare current tenant version with the v29/v30 deprecation scopes. Inventory one endpoint and one deployment job requiring migration.
2. **Lifecycle:** Build a small extension and test publish/sync/install/upgrade from prior data. Add a company-scoped upgrade tag; prove retry, second company and fresh install behavior.
3. **Data/UI/security:** Extend a table/page, enum/interface, Role Center and profile. Test validation, permissions and inherent-permission output under a nonadministrator.
4. **Reports/query/XMLport:** Build a two-layout multilingual report and an import/export. Inject the fan-out from example 3, repair the grain and compare totals; check empty and large inputs.
5. **Errors/events:** Compare ordinary errors, caught try methods and Boolean Codeunit.Run using disposable records. Observe persisted results and test two subscribers without an ordering dependency.
6. **Onboarding/files:** Add Assisted Setup, tips and checklist with a durable completion test. Reject malformed/oversized files without leaving partial setup.
7. **Automated tests:** Use a test runner, handlers and expected-error assertions. Execute a larger suite only in a suitable container/CI setup; retain results for the exact package and version.
8. **Performance/telemetry:** Benchmark selected fields and intentional JIT loads, test FlowField feature states and count attempt versus eventual outcomes. Keep confidential values out of telemetry.
9. **Outbound integration:** Reproduce the lost-response/retry model locally, then use an authorized mock service for transport/status/payload errors, idempotency conflict and certificate failure. Verify the stable identity reaches the recipient.
10. **Inbound API:** Test SystemId, versioning, permissions, concurrency, pagination and bound/unbound actions. Inject a transactional-batch failure with and without a deliberate intermediate commit. Label sandbox read-intent results as primary-only; model lag separately.

## Knowledge checks with answers

1. **Online versus on-premises ownership?** Online is managed SaaS; on-premises adds server, database, identity, patching and capacity responsibilities.

2. **System app versus Base app?** Reusable platform-facing modules versus core business application functionality, with declared extension dependencies.

3. **Does compilation prove update compatibility?** No. Test behavior, dependency versions, schema and data upgrades.

4. **PTE versus AppSource?** A tenant customization versus a distributed product with technical, commercial, support and lifecycle validation.

5. **Where should current SaaS PTE deployment run?** Business Central Admin Center or its API; distinguish in-client viewing from the changing upload surface.

6. **Does v29 remove all SOAP?** The cited announced removal concerns Microsoft pages exposed as SOAP; do not widen its scope.

7. **What does the v30 OData removal concern?** Pages in Microsoft-published apps exposed as OData, not all custom APIs and queries.

8. **What belongs in app.json?** Identity/version, dependencies, runtime/application/platform targets, ranges and exposure policy; launch settings describe connection/debug behavior.

9. **How avoid workspace coupling?** Use explicit acyclic dependencies, reproducible symbols/tooling and appropriately scoped public contracts.

10. **Publish, synchronize, install and upgrade?** Package availability, schema compatibility, new-install initialization and existing-data transformation.

11. **What controls migration replay?** Correctly scoped version/tag checks, with fresh-install and new-company registration and failure tests.

12. **Can upgrade codeunits depend on execution order?** No. Separate codeunit order is not guaranteed.

13. **How test multilingual behavior?** Use stable labels/XLIFF, recipient context and layout/grammar tests rather than concatenated messages.

14. **Table versus table extension?** Own a new durable model versus add supported fields/keys to another model without cloning it.

15. **Does direct assignment run field validation?** It differs from Validate; use the supported validation path when business rules must run.

16. **Does hiding a FlowField prevent computation?** Not by default; the v26 visible-FlowFields feature changes the relevant page behavior.

17. **When pair enum and interface?** When named alternatives select implementations of a stable behavioral contract.

18. **Page versus profile versus permission?** Interaction, role experience and access control are separate concerns.

19. **What makes a useful cue?** A defined company/filter/time scope, cheap calculation and correct drill-through.

20. **Dataset, request page and layout?** Data/relationships, user parameters and presentation respectively.

21. **Why reconcile a report after a join?** Child-table fan-out can duplicate values even when the SQL and layout work.

22. **When substitute rather than extend a report?** When the required replacement contract cannot be met through supported dataset/layout extension.

23. **What is a processing-only report?** A report object running logic without rendered output, still requiring transaction and recovery controls.

24. **What must XMLport design specify?** Nodes, format/encoding/direction and validated restartable input/output handling.

25. **Why minimize IsHandled?** It can bypass validation and suppress events; prefer explicit interfaces or additive events.

26. **What ordering can event subscribers assume?** No dependency on the ordering of independent subscribers.

27. **How far can inherent permissions reach?** Only objects in the same extension; choose permission/entitlement scope and constrain output.

28. **Can an admin remove an inherent grant through ordinary sets?** No. The code-defined grant requires a design change, so use it narrowly.

29. **What makes onboarding completion real?** Validated persisted setup, not simply opening a page or clicking Next.

30. **Document, journal, ledger and register?** A business process, prepared postings, posted facts and the grouping of resulting entries.

31. **When do partial records help?** Read-heavy code that selects all needed fields before fetching; omitted fields and write operations can cause extra loads.

32. **Why can pass-by-value hurt partial-record loops?** Loads on the copy do not update the original iterator’s field selection.

33. **How handle files in online code?** Streams and supported upload/download abstractions, with size/type/encoding checks.

34. **Does a caught try-method error roll back writes?** No. Do not treat error capture as an atomic rollback boundary.

35. **What if a try method return is unused?** It behaves as an ordinary call rather than the caught Boolean-return pattern.

36. **What does Boolean Codeunit.Run change?** It commits successful codeunit work and requires an existing transaction to be committed first.

37. **Does CommitBehavior stop implicit Codeunit.Run commits?** No. It controls explicit commits in its scope.

38. **Where run a large automated suite?** A suitable container-based CI environment; online production is disallowed and sandboxes have limits.

39. **Why use handlers and a test runner?** Unexpected UI becomes a test failure and expected UI can be answered and asserted deterministically.

40. **What does telemetry need beyond a message?** Stable event meaning, correlation, safe dimensions, ownership and a metric with a clear denominator.

41. **Which HTTP success levels must be checked?** Transport response obtained, acceptable status and valid business payload/outcome.

42. **Does a client certificate validate the server?** No. Server trust and client authentication are separate.

43. **Can online anti-SSRF be disabled for an internal IP?** No. Use a supported integration architecture and current platform guidance.

44. **What makes an external retry safe?** Stable operation identity plus recipient-side atomic deduplication or an idempotent operation; a local flag alone is insufficient.

45. **Can an API page be extended like a UI page?** No. Create a new versioned contract when needed.

46. **Bound versus unbound action?** An operation tied to a resource instance versus a service operation without that instance binding.

47. **Does Isolation: snapshot guarantee atomicity despite commits?** No. Intermediate commits split the transaction; inspect inner outcomes and stored state.

48. **What does a sandbox prove about read scale-out?** It can exercise the object contract on the primary, but cannot prove replica routing or lag.

---

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one primary route, build and upgrade one secure extension end to end, and add another resource only for a measured gap.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MB-820 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-820) | Free | 1–2 hours to map six domains and freshness gaps |
| [Application development best practices](https://learn.microsoft.com/en-us/training/paths/use-application-development-business-central/) | Free | 7 modules; runtime not shown; 12–20 hours with AppSource/upgrade/test work |
| [Customization foundation](https://learn.microsoft.com/en-us/training/paths/foundation-customize-business-central/) | Free | 8 modules; runtime not shown; 22–35 hours building/deploying objects |
| [Build reports](https://learn.microsoft.com/en-us/training/paths/build-reports/) | Free | 11 modules; runtime not shown; 15–25 hours with layouts/data/performance |
| [AL application foundation](https://learn.microsoft.com/en-us/training/paths/application-foundation-al-language/) | Free | 10 modules; runtime not shown; 20–35 hours coding/testing exercises |
| [Data management foundation](https://learn.microsoft.com/en-us/training/paths/data-management-foundation-business-central/) | Free | 3 modules; runtime not shown; 8–15 hours with XMLport/query/file builds |
| [Interface with Business Central](https://learn.microsoft.com/en-us/training/paths/interface-with-business-central/) | Free | 6 modules; runtime not shown; 12–25 hours with resilient API integrations |
| [Tailor roles and design the UI](https://learn.microsoft.com/en-us/training/paths/tailor-roles-design-ui/) | Free | 5 modules; runtime not shown; 8–15 hours with onboarding/accessibility |
| [Essential development standards](https://learn.microsoft.com/en-us/training/paths/essential-development-standards/) | Free | 4 modules; runtime not shown; 10–20 hours implementing standard patterns |
| [MB-820T00-A: Develop solutions with Dynamics 365 Business Central](https://learn.microsoft.com/en-us/training/courses/mb-820t00) | Paid/provider-dependent | 5 days; English |
| [MicrosoftLearning MB-820 labs](https://github.com/MicrosoftLearning/MB-820-Business-Central-Developer-Certification) | Free; MIT | 12–25 hours; repository title/README retain sample-course artifacts, so use hosted lab index and verify current instructions |
| [Free MB-820 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/d365-business-central-developer-associate/practice/assessment?assessment-type=practice&assessmentId=66154329&practice-assessment-type=certification) | Free | 45–90 minutes plus remediation |
| [AL developer documentation](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/) | Free | 25–60 hours selected current reference/troubleshooting |
| [O’Reilly: MB-820 Certification Companion](https://www.oreilly.com/library/view/dynamics-365-business/9798868809262/) | Subscription/trial | 317-page Apress book by Dr. Gomathi S, November 2024; 3h48 platform reading estimate; gap-check current runtime |
| [Microsoft Community MB-820 awareness session](https://techcommunity.microsoft.com/event/d3f367f5-77c3-4097-92a4-2bf95e15d11c/mb-820-certification-essentials-your-complete-guide-to-becoming-a-business-centr/4537934) | Free registration; event availability varies | About 1–2 hours estimated; verify recording/event access |
| [Microsoft Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner login required | Use the five-day course pattern for planning; signed-in event start/end times control |

The eight official paths expose **54 module placements** (7/8/11/10/3/6/5/4). Current public pages do not expose runtime, so the old 50h07 total is withdrawn. Linked units were not exhaustively read; barcode/control-add-in/Dataverse material can be adjacent to the detailed objective list. Allow roughly **120–200 hours** for a developer new to Business Central to build, test, integrate, upgrade and operate the extension portfolio. No exact current Pluralsight, MeasureUp or Whizlabs MB-820 product was independently verified. Earlier Udemy discovery did not establish a suitable course; this pass did not comprehensively repeat those commercial searches.

## Useful developer articles

- [Stefano Demiliani: job queues and idempotent external effects](https://demiliani.com/2026/09/01/why-your-business-central-job-queue-needs-idempotent-external-effects-when-integrating-external-systems/) (September 1, 2026) supplies a useful failure scenario. Trace remote success followed by local failure and retry. Use the original local model above; the article's snippets are illustrative and were not compiled, and its broad rollback language must be read alongside current try/commit rules.
- [Steven Renders: API pages versus API queries](https://thinkaboutit.be/2026/03/api-pages-vs-api-queries-in-business-central-when-to-use-each/) (March 17, 2026) helps frame a contract-selection worksheet. Keep the CRUD/read-model distinction, then measure your actual query and integration. Its broad SOAP/OData retirement statements and unconditional replica-routing implication exceed the primary documentation; do not adopt those claims or a universal query-first performance rule.
- [Microsoft’s AI at Work roadmap transition](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/08/25/one-always-on-roadmap-dynamics-365-power-platform-and-dataverse-join-the-ai-at-work-roadmap/) (August 25, 2026) informs release discovery. Confirm announcements against current product documentation and the tenant version before changing implementation instructions.

The [Plataan webinar listing](https://app-plataantv-web-prd-euw.azurewebsites.net/en/plataan/training-course/business-central/mb-820-exam-preparation-webinar) now shows October 13–14 and November 26–27, 2026, rather than the previously recorded September dates. It is removed from the recommended route because its public description refers to real exam questions; the wording does not establish whether its exercises are original. No session or question content was accessed. The community awareness page and partner portal returned only shells, so current recording/event access remains unverified.

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
