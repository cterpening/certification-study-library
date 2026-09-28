---
exam_code: MB-500
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-500
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# MB-500 Microsoft Dynamics 365 Finance and Operations Apps Developer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Checked against the January 30, 2026 official objective baseline and cited public sources on September 28, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#mb-500-coverage-record). The [official MB-500 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-500) is authoritative.

**Current baseline:** Skills measured as of January 30, 2026.<br>
**Upcoming blueprint change:** None announced as of September 28, 2026.<br>
**Lifecycle:** The [Finance and Operations Apps Developer Associate credential](https://learn.microsoft.com/en-us/credentials/certifications/d365-finance-and-operations-apps-developer-associate/) is active. The exam is 100 minutes, offered in English and Japanese, lists no retirement date, and links a free Practice Assessment. Renewal is every 12 months; the direct practice endpoint returned no substantive body during this review.<br>
**Platform transition:** Current objectives explicitly include Unified Developer Experience (UDE) environments in Power Platform admin center and the Implementation portal. Treat older LCS/VM-only instructions as context and verify current ownership for each environment action.<br>
**Official source:** [MB-500 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-500)

**September deep review:** All 89 published objectives are mapped in the [review report](../docs/research/2026-09-28-mb-500-deep-review.md). The old repository snapshot was a 22-bullet summary; it is archived, with full canonical wording now restored. This is not a newly announced exam baseline.

## How to use this guide

For every requirement, produce a small technical contract:

1. business event and transaction boundary;
2. standard capability/configuration before custom code;
3. extension point and AOT/data elements;
4. security entry point, role/duty/privilege and record scope;
5. synchronous/asynchronous integration and retry/idempotency behavior;
6. automated test and performance budget;
7. source/build/package/environment promotion and rollback evidence.

Build in a disposable developer environment and keep code in version control. A feature that works only in a debugger or with administrator permissions is not finished.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Domain | Weight | Central question |
|---|---:|---|
| Plan architecture and solution design | 5–10% | Can you choose deployment/ecosystem boundaries and promote changes safely? |
| Apply developer tools | 5–10% | Can you develop, debug, version, merge and deliver metadata/code reproducibly? |
| Design and develop AOT elements | 15–20% | Can you extend UI, data and classes without overlayering or upgrade breakage? |
| Develop and test code | 20–25% | Can you write correct X++, use frameworks and prove behavior? |
| Implement reporting | 10–15% | Can you choose and secure the appropriate operational/analytical/document tool? |
| Integrate and manage data solutions | 15–20% | Can you select and operate APIs, entities, events and Power Platform integration? |
| Implement security and optimize performance | 10–15% | Can you enforce least privilege and tune from evidence? |

---

## 1. Plan architecture and solution design

Cloud environments are Microsoft-operated with service-update and platform constraints; on-premises deployment has different infrastructure, update and integration responsibilities. Do not infer feature parity. Map user/browser, application metadata/runtime, database, reporting, Dataverse/Power Platform, Azure services and external systems, then record identity, network, data-residency, latency and availability boundaries.

Extend into the Microsoft ecosystem only when the responsibility fits: Dataverse/Power Apps for cross-app data/experiences, Power Automate for governed workflow/orchestration, Power BI for analytics, Azure for scalable integration/compute/secrets, Microsoft 365 for productivity. Prefer configuration and supported extension points before X++ customization.

ALM spans requirement → model/project → code/metadata → build/test → deployable package → sandbox validation → production promotion → monitoring/rollback. Lifecycle Services still supports specified tools, Issue Search, asset libraries and package activities; UDE developer environments are managed through Power Platform admin center, and implementation work increasingly uses the Implementation portal. Record the environment’s actual management plane and supported operation before following a portal-specific procedure.

Asset libraries hold deployable packages and other implementation assets. Package dependencies and all-in-one deployment expectations matter. Record package version/source commit, build result, database synchronization need, target compatibility, downtime, smoke tests and rollback. Never compile or make untracked production changes.

> **Related item:** Environment management is split across PPAC, LCS and Implementation portal during platform convergence. “Where the button is” can change; the durable knowledge is which service owns development, implementation, package, monitoring and production actions.

---

### Current environment and migration boundaries

The [February 16 LCS project-creation freeze](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/lcs-project-creation-freeze) applies to new cloud implementations for Finance, SCM and Project Operations. Existing active projects, Commerce, AX 2012 upgrades, on-premises implementations and tenant-to-tenant migration scenarios have documented exceptions. It does not mean all LCS operations disappeared.

[Self-service migration](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/lifecycle-services/migrate-lifecycle-services-environments-power-platform-admin-center) is **public preview** in September 2026: it changes each environment's management plane, not the project or database location. It is one-way for customer-initiated operations; LCS becomes read-only for that environment. Microsoft recommends sandboxes first and not production during preview. Cloud-hosted developer environments and Commerce workloads are unsupported; the prerequisite checker does not detect Commerce usage. Validate the workload separately and prepare unified deployment pipelines before a sandbox migration.

In the [unified admin model](https://learn.microsoft.com/en-us/power-platform/admin/unified-experience/finance-operations-apps-overview), license/capacity and environment type matter. A [UDE](https://learn.microsoft.com/en-us/power-platform/admin/unified-experience/unified-environment-types-and-templates) is a **Sandbox** with developer tooling, intended for one X++ developer with one AOS. It is not the Power Platform Developer environment type, a shared development server or a performance-test environment. USE and UDE cannot be converted into each other after provisioning.

---

## 2. Apply developer tools

An extension model groups custom metadata/code and references required packages. Minimize references and dependency direction. Application Explorer exposes AOT metadata; element designers create/extend tables, forms, classes, entities and other elements. Build validates code/metadata, while database synchronization applies data-dictionary changes to the development database. Know when each is required.

Debug with breakpoints, call stack, variables, infolog and server/client context. Reproduce with least privilege and representative data; do not “fix” a race or query problem by stepping through it slowly. Resolve compiler and best-practice warnings intentionally.

Use Azure DevOps with a documented Git or TFVC strategy appropriate to the supported environment/toolchain. Keep solution artifacts with code, review diffs, link work items, isolate branches, merge small changes and resolve semantic—not merely textual—conflicts. CI should restore/build/synchronize as applicable, run analyzers/tests, produce immutable versioned packages and retain evidence. CD promotion requires approvals and environment-specific controls.

> **Related item:** Source control preserves authored artifacts; the build produces deployable output; the asset library distributes approved packages. None substitutes for environment configuration/data or deployment validation.

---

The [UDE development overview](https://learn.microsoft.com/en-us/power-platform/developer/unified-experience/finance-operations-dev-overview) separates local tooling from code execution/debugging in the cloud. The current [installation instructions](https://learn.microsoft.com/en-us/power-platform/developer/unified-experience/finance-operations-install-config-tools) specify Visual Studio 2022, its required workloads/components, Power Platform Tools and environment-matched F&O assets. Do not assume the newest Visual Studio major release is supported. The developer sandbox account requires System Administrator for setup/development; still test the finished extension with its intended business identities.

---

## 3. Design and develop AOT elements

### UI and navigation

Create a form only when no standard experience or extension meets the requirement. Use appropriate form patterns, data sources, controls, commands and responsive/accessibility behavior. A form extension adds supported controls/properties without modifying the base form. Menus organize navigation; display/action/output menu items invoke forms, operations or reports. Labels externalize user text for translation—never hard-code visible strings.

Test personalization, saved views, keyboard use, validation messages, data-source joins, refresh, concurrency and security. A hidden control is not authorization.

### Data model

Tables own persisted business data and behavior; extensions add supported fields/indexes/relations/methods. EDTs and enums supply reusable semantic types. Views shape read models, queries express reusable joins/ranges/order, maps normalize access across compatible structures, and data entities define external/data-management contracts with staging, keys and mappings.

Choose surrogate/natural keys deliberately, enforce relations and indexes aligned with access paths, and specify delete actions and company scope. Adding a mandatory field to a populated table requires default/migration behavior. An entity contract needs public fields, keys, validation, sequencing, change tracking and backward compatibility.

### Classes and extensibility

Create cohesive classes with clear dependencies and transaction ownership. Attributes add framework metadata; modifiers determine visibility/extension behavior. Prefer supported Chain of Command for wrapping extensible methods and call `next` unless the contract explicitly supports replacement. Event handlers subscribe without changing base code; delegates publish intentional extension points.

Assess whether a standard method/table/form is extensible before design. Avoid overlayering, fragile reflection or assumptions about private implementation. Preserve method pre/postconditions and upgrade compatibility.

> **Related item:** CoC participates in a method chain, an event handler reacts at a published event, and a delegate is an explicit publisher-defined contract. Choose by ordering, return/control needs and coupling.

---

[CoC documentation](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/extensibility/method-wrapping-coc) does not promise wrapper order. Ordinary wrappers must call `next` unconditionally; `[Replaceable]` permits an intentional conditional break. `[Wrappable(false)]` prevents wrapping, while `[Wrappable(true)]` can permit a final method to be wrapped. `[Hookable(false)]` also prevents CoC wrapping; setting Hookable to true is not a universal override. Inspect the actual extension point and write order-independent logic.

---

## 4. Develop and test code

X++ includes types, classes, exceptions, loops/conditions and database statements. Use `select`, `insert`, `update`, `delete` and set-based operations with company/locking/transaction semantics understood. Scope variables narrowly; dispose/release resources according to framework conventions. Validate at the correct layer so imports, services and UI paths share business rules.

Use `ttsBegin`/`ttsCommit` for a coherent atomic boundary and handle exceptions without swallowing failure. Avoid long transactions and external calls inside locks. Global functions should have deliberate discoverability and dependency behavior rather than becoming a dumping ground.

Inheritance and abstract classes define stable polymorphic contracts. Query objects and QueryBuild* classes support dynamic sources, joins, ranges and fields; validate generated shape and parameterize ranges. Attribute classes support discovery/registration patterns. SysExtensionSerializer provides supported serialization scenarios; understand versioning and type registration.

**SysOperation** separates data contract, service and controller for synchronous/batch operations. Define serialization, validation, retry, batch grouping and idempotency. Workflow separates configurable approval/state from business code; implement document, participant, event and state behavior with resubmit/cancel/recovery. Async and Sandbox frameworks isolate suitable work under their current contracts.

SysTest unit tests need arrange/act/assert, isolated data, deterministic company/time, positive/negative/concurrency cases and cleanup. Task recorder can generate process evidence or support test assets; it is not a substitute for unit-level logic tests. Run tests in Test Explorer and CI. Treat best-practice checks as quality gates with reviewed suppressions.

> **Related item:** Unit tests prove small code contracts, SysTest integration tests exercise framework/data behavior, and RSAT/UAT proves business journeys. A healthy release uses layers rather than one enormous end-to-end script.

---

### Transaction and retry failures to rehearse

[X++ integrity checks](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/dev-ref/xpp-data/xpp-transaction) require both selection for update and updating in the same transaction scope. Selecting a row before `ttsBegin` and updating inside it can fail the scope check. Inner commits do not make changes durable before the outermost commit. Check for a missing row explicitly; a successful query invocation is not evidence that the required record exists.

[Exception handling](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/dev-ref/xpp-exceptions) usually aborts the transaction and handles the failure outside its scope. Explicit UpdateConflict/DuplicateKeyException catches have special rules; a catch-all inside the transaction is not a universal recovery mechanism. `retry` restarts its associated try block and clears its intervening Infolog messages. Bound attempts, preserve separate diagnostic evidence and re-read state before retrying.

[Batch retry settings](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/retryable-batch) distinguish general task failures from SQL transient connection errors. `BatchRetryable`/idempotent flags enable a retry mechanism; they do not make business effects safe to repeat. The page's generic dynamic-task setup wording is broader than its runtime-task note. Its FAQ clarifies that the static controller monitors and requeues failed runtime children with bounded attempts; ordinary runtime-task failures are not automatically retried like SQL transient connection errors. Preserve the original transient exception when rethrowing, because replacing it with a generic error loses that classification. Validate the exact task type in the sandbox.

[SysTest guidance](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/perf-test/testing-validation) covers unit/component tests and generating test assets from Task recorder. Its older VM/Fleet Management walkthrough is not the current UDE provisioning procedure. Isolate fixture data and test failure/cleanup paths without granting the business user administrator rights.

---

## 5. Implement reporting

Choose by user decision and data latency:

- SSRS for parameterized, paginated operational documents/reports;
- Power BI for interactive analytics and governed semantic models;
- Excel/OData for controlled ad-hoc analysis or editable entity experiences;
- Electronic Reporting for configurable regulatory/business document formats;
- workspaces/KPIs for role-based operational monitoring and drill-through.

SSRS design connects query or report data provider, contract, controller, design and deployment. Secure both menu/report entry and underlying data. Power BI needs a supported store/model, refresh/DirectQuery choice, row security and lifecycle. Excel requires entity/OData permissions, field behavior and refresh/publish constraints. ER uses model, mapping and format configurations; prefer configuration over code where the document requirement fits.

Workspaces combine tiles, lists, KPIs and embedded visuals around a role. Each number needs grain, filter, time, owner and drill-through target. Test empty/large data, company context, localization, export, accessibility and performance.

> **Related item:** Reporting datastore selection is separate from visualization choice. A beautiful report over an unsupported or stale data path is still a poor design.

---

## 6. Integrate and manage data solutions

### Select the pattern

Synchronous patterns serve bounded request/response needs with strict latency/availability coupling. Asynchronous patterns serve volume, decoupling and retry. Compare OData/entity endpoints, custom REST/SOAP services, Batch OData, data-management packages/recurring jobs, business events, ER and Power Platform/Azure integration by direction, volume, latency, transactionality, ordering, error model and security.

Custom services expose a deliberate contract when standard entities/APIs do not fit. Version payloads, authenticate/authorize, validate input, correlate calls, bound timeouts and avoid leaking internal exceptions. Business events notify external consumers of committed business facts; consumers must be idempotent because retries/duplicates are normal. Store secrets in Azure Key Vault under managed access, not code/config exports.

[OData batch](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/odata) is a request envelope; **each changeset** is the atomic unit. Separate changesets do not make the entire batch all-or-nothing. Follow server-driven pagination for reads instead of assuming the first page is the whole result. Batching does not turn a synchronous entity API into the asynchronous data-management package API.

[Business events](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/business-events/home-page) are lightweight notifications, not bulk exports. Activate the event and intended company scope. The control number identifies duplicates; it is **not a sequential business version**, and delivery order is not guaranteed. Persist deduplication together with the local business effect. Handle downstream side effects using an outbox or a downstream idempotency contract; recording a receipt separately can lose or repeat work.

### Manage data through entities

The exam's **[Batch OData API](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/batch-odata-api)** manages batch-job requeueing. It is distinct from sending entity CRUD requests in OData `$batch`. The `SetBatchJobToWaiting` POST action takes a `batchJobId`; successful requeue means the job is waiting, not that its work completed. Validate the target job and current eligible state, classify the failure, cap attempts and follow subsequent job results. Do not automatically replay every job whose event arrives. The page's terminal-state description is narrower than a later list including “started”; use the terminal failure recovery scenario and verify state eligibility before invoking it.

Data entities abstract target tables for import/export and OData. Composite entities group related contracts; aggregate entities serve summarized scenarios. Data projects define entity order, source/staging/target mappings, filters and package. Recurring jobs automate supported import/export. Monitor staging errors, execution status, entity availability and throughput.

Change tracking supports deltas but needs a stable key/watermark and deletion strategy. Map conversions/defaults explicitly and reconcile counts/totals. Large migrations require rehearsal, sequencing, parallelism constraints, restartability and business validation—not merely a successful job status.

For the [data-management package API](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-management-api), capture the execution ID and query execution status/errors. An accepted request does not prove success, and `PartiallySucceeded` needs reconciliation. The documentation explicitly warns against calling `ImportFromPackage()` on parallel client threads; use its supported data-management parallel-processing rules. Reconcile source, staging and target by stable keys and business totals before deciding what to retry.

### Connect the ecosystem

Dual-write synchronizes mapped data between finance/operations and Dataverse with ownership, filters, ordering and error handling; virtual entities/tables expose F&O data without copying it for supported scenarios. Choose based on ownership, latency, supported operations, offline/reporting needs and failure tolerance. Power Apps/Power Automate should use least-privilege connectors and avoid chatty row-by-row designs.

Excel uses OData/entity contracts. Azure services can broker, transform or process integrations; document exactly-once expectations honestly—most distributed systems provide at-least-once delivery plus idempotent handling.

> **Related item:** Data migration moves a bounded historical/configuration set, master-data synchronization maintains shared facts, and business events publish occurrences. Treating all three as “integration” hides different reliability contracts.

---

[Dual-write](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/dual-write/dual-write-overview) maintains mapped copies with synchronization lifecycle/error concerns. [Virtual entities](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/power-platform/virtual-entities-overview) invoke the F&O entity using an associated user context; Dataverse SYSTEM is not blanket F&O access. A virtual table avoids that data copy but still depends on live service, permissions and supported operations. Mapping an identity is not proof that every security mechanism propagates.

---

## 7. Implement security and optimize performance

Roles collect duties; duties collect privileges; privileges grant entry-point permissions to menu items, service operations, entities or other securable objects. Extend the smallest appropriate artifact. Segregation of duties detects risky combinations. XDS policies restrict supported table access through constrained tables/queries. Test forms, reports, batch and integration paths independently; a successful form restriction is not evidence that an entity endpoint inherits it. Do not rely on UI visibility.

Performance work begins with measurement. Table/form caching reduces repeated reads but introduces scope/staleness decisions. Global cache/singletons require key, company/user isolation, invalidation and memory discipline. InMemory and TempDB tables have different scale/join/lifecycle behavior. Prefer set-based work when semantics permit; avoid N+1 queries, unnecessary fields/joins, broad ranges and row-by-row updates.

Keep variable scope and transactions narrow. Design indexes for selective predicates, joins and ordering while accounting for write cost. Analyze optimistic/pessimistic concurrency, lock order, retry and batch parallelism. Never use `firstOnly` or a cache to mask nondeterministic business logic.

Capture traces and use Trace Parser to identify call/query cost. Optimize entity queries, batch, reports and forms from representative volume. Establish baseline, hypothesis, one change, comparable measurement and regression test. Async/Sandbox frameworks move suitable work but add queues, serialization, quotas and monitoring; they do not make inefficient code free.

---

### Security boundaries and performance semantics

[Data-entity security](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/security-data-entities) explicitly says that **data entities do not support XDS**. Configure separate DataServices and DataManagement entry points and least-privilege duties; `IntegrationMode=All` broadens access. Table Protection Framework restrictions on sensitive fields still matter. If a required subset cannot be enforced through a supported integration design, withhold the broader entity access and use a suitably authorized contract.

For supported table paths, [multiple XDS policies intersect](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/extensible-data-security-policies); they do not union their allowed records. A bypass role disables that supplemental filtering. Do not apply XDS directly to financial-dimension data. Test an ordinary user, another company and the real integration identity; document each independent access boundary.

[Set-based statements may fall back to record-by-record execution](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/dev-ref/xpp-data/xpp-data-perf) depending on table/method/logging behavior. Trace the actual workload. The [update documentation](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/dev-ref/xpp-data/xpp-update) warns that `doUpdate()` bypasses update logic, handlers and CoC; it is not a harmless performance replacement. Preserve required behavior before optimizing call count.

---

## Integrated scenarios

### Scenario 1: governed order extension

A table/form extension and labels capture an approved customer attribute. CoC validates it before a standard operation without changing base code. A role/duty/privilege grants the menu/entity entry, supported table policies constrain the intended records while entity integrations receive their own access controls, SysTest proves valid/invalid/concurrent updates, and CI creates a versioned package promoted through sandbox with trace comparison and rollback evidence.

### Scenario 2: high-volume external fulfillment

An entity/OData API accepts bounded synchronous queries while OData changesets handle bounded atomic groups and data-management packages handle asynchronous bulk transfer. A committed business event triggers downstream fulfillment through an idempotent consumer. Key Vault protects credentials, correlation IDs connect logs, recurring jobs surface staging failures, and performance tests compare set-based processing/index changes. Dual-write is rejected because F&O remains owner and the external platform does not need a Dataverse copy.

### Scenario 3: executive-to-operational reporting

SSRS produces the paginated customer document, ER handles a configurable regulatory format, Power BI provides governed trends, and a workspace KPI drills into an actionable query. Each path enforces security, uses the appropriate store/freshness, handles company context and is load-tested. Excel is retained for controlled entity maintenance rather than becoming an unmanaged reporting database.

---

## Worked examples

These original models illustrate contracts to test. The Python example ran locally; no X++ compilation, Dynamics API, migration or tenant test was executed.

### 1. Wrapper order changes a result

The base method returns 100. Wrapper A adds 10 after `next`; wrapper B doubles the result after `next`. A outside B returns 210; B outside A returns 220. Both call `next`, yet the result depends on order. Do not use wrapper registration as an ordering contract. Move a dependent calculation into an explicitly owned workflow or redesign contributions to commute under the required business rules.

### 2. A transaction boundary is more than balanced braces

Transaction level 0 selects a row for update, then level 1 updates it: the scopes differ. Select and update within the same intended scope. For nested work, outer begin → inner begin → inner commit still leaves an outer transaction open; a later failure rolls back its changes. An external HTTP payment sent before the failure is not rolled back by the database. Keep remote effects outside locks and design a durable handoff instead.

### 3. Deduplicate the effect and receipt together

This SQLite teaching model stores an event receipt and a local counter update in one transaction. The key includes origin and company so repeated IDs from unrelated scopes do not collide. It rejects an inconsistent replay and rolls back the receipt if the target is missing or a simulated failure occurs. It models sequential local retries, not distributed exactly-once delivery or X++ concurrency.

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE counters(company TEXT PRIMARY KEY, value INTEGER NOT NULL);
INSERT INTO counters VALUES ('USMF', 0), ('DEMF', 0);
CREATE TABLE receipts(
    origin TEXT, company TEXT, event_id TEXT, amount INTEGER NOT NULL,
    PRIMARY KEY(origin, company, event_id));
""")

def apply_event(origin, company, event_id, amount, fail=False):
    key = (origin, company, event_id)
    with db:
        inserted = db.execute(
            "INSERT INTO receipts VALUES (?, ?, ?, ?) "
            "ON CONFLICT(origin, company, event_id) DO NOTHING",
            (*key, amount),
        ).rowcount
        if not inserted:
            previous = db.execute(
                "SELECT amount FROM receipts WHERE origin=? "
                "AND company=? AND event_id=?", key,
            ).fetchone()[0]
            if previous != amount:
                raise ValueError("Conflicting replay")
            return False
        changed = db.execute(
            "UPDATE counters SET value=value+? WHERE company=?",
            (amount, company),
        ).rowcount
        if changed != 1:
            raise ValueError("Unknown company")
        if fail:
            raise RuntimeError("Failure before commit")
    return True

apply_event("source-A", "USMF", "evt-9", 7)
apply_event("source-A", "USMF", "evt-9", 7)  # replay has no effect
apply_event("source-A", "DEMF", "evt-9", 3)  # separate company
print(db.execute("SELECT * FROM counters ORDER BY company").fetchall())
# [('DEMF', 3), ('USMF', 7)]
```

A local commit followed by an acknowledgment failure is safe to replay under this model. Sending an email or calling a fulfillment API inside this function would introduce a separate failure boundary. Use a durable outbox and a consumer that deduplicates the external action; the local transaction cannot prove external delivery.

### 4. One HTTP batch can contain several commit boundaries

Put a header create and an invalid line create in one OData changeset: the failed line prevents that changeset from committing. Put the header in one changeset and the invalid line in a second: the first may already have committed. Keep related operations in the supported transaction boundary and inspect individual responses. A timeout still needs correlation/reconciliation before retrying an operation whose commit status is unknown.

### 5. Test a security intersection and an integration separately

For a supported table path, policy A permits records {1, 2, 3} and policy B permits {2, 3, 4}; the intersection is {2, 3}. Record 1 does not become available because one role's policy allows it. Now test an entity API with its own privileges: the XDS result above is not an entity-access guarantee. Record actual allowed/denied entity operations before granting the integration identity access. Also test without a bypass or administrator role.

### 6. Compare performance without dropping work

A page makes one header query plus one line query for each of 200 headers: 201 calls. A candidate design batches the lines in a second query: two calls, a reduction of 199. At an assumed 8 ms overhead per call, overhead falls from 1,608 ms to 16 ms—a theoretical saving of 1,592 ms before database work, serialization or contention. Confirm identical record/company scope, totals and business logic, then measure actual latency and query plans. If 10,000 imported rows split into 9,700 target successes and 300 failures, retry only reconciled failures; replaying the full file can repeat previously successful effects.

## Useful articles and follow-up reading

- **[Unified trial and developer environments](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2023/09/15/announcing-unified-trial-and-developer-environments-for-dynamics-365-finance-and-operations-apps/)** — Lane Swenka, September 15, 2023. Useful architectural history: local tooling, cloud runtime and shared Power Platform administration. Draw the tool/runtime/data boundaries, then check today's setup and environment-type docs. Its preview, trial, capacity and add-in examples are historical, not a current provisioning checklist.
- **[UDE TechTalk article](https://learn.microsoft.com/en-us/dynamics365/guidance/techtalks/unified-developer-experience)** — Microsoft FastTrack. Read the sections on local tools, cloud execution and debugging; map an extension from source to sandbox. This is X++ Finance/SCM context, not Business Central development. The article was read; its video was not watched, and general productivity claims are not measured evidence.
- **[Roadmap transition](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/08/25/one-always-on-roadmap-dynamics-365-power-platform-and-dataverse-join-the-ai-at-work-roadmap/)** — Richard Riley, August 25, 2026. Use the linked AI at Work roadmap for new disclosures, current product docs for supported behavior and the study guide for exam scope. Historical release-wave pages alone no longer cover new announcements. Recheck the planned November 15 Release Planner retirement after its date.

## Hands-on labs

1. **Architecture/ALM:** Write a portal/service responsibility matrix; create release flow with work item, model, CI tests, package/asset, sandbox gates, production and rollback.
2. **Tools/source:** Create an extension model/project, element, label and DB sync; branch, review, merge conflict, build/package and debug a least-privilege failure.
3. **AOT/UI/data:** Extend a table/form/menu, create query/view/map/entity, keys/relations/index and migration default; test company, accessibility and entity contract.
4. **X++/extensibility:** Implement CRUD/transaction, QueryBuild*, attribute, CoC, handler and delegate; document why each extension mechanism fits.
5. **Frameworks/tests:** Build SysOperation batch with idempotency, a workflow state path, SysExtensionSerializer example and layered SysTest/Task Recorder tests.
6. **Reporting:** Implement or design SSRS, Power BI, Excel, ER and workspace/KPI for one dataset; compare security/store/latency and measure one path.
7. **Integration/data:** Compare OData, batch, package, custom service, event, dual-write and virtual entity; build one sync and one async path with retries/reconciliation.
8. **Security/performance:** Create role/duty/privilege and XDS matrix; capture a trace, change query/index/cache/loop behavior, remeasure and regression-test.

9. **Replay and failure recovery:** Run the local receipt/counter model, inject a pre-commit failure, replay it and test an inconsistent payload and unknown company. Then design the equivalent transaction/outbox contract for a sandbox SysOperation or event consumer.
10. **Boundary test matrix:** Compare a least-privilege form user, DataServices identity, DataManagement identity and virtual-table caller. Document supported filtering and denied operations separately. Rehearse a two-changeset failure and one supported X++ concurrency/retry case in a disposable environment.

For each lab record version, identity, company, expected/actual result, negative case and cleanup. The repository review executed only the local model and calculations; tenant labs remain tasks for the learner.

## Knowledge checks with explained answers

Original conceptual prompts, not recalled exam items. Answer first, then compare the explanation.

1. **Which requirements differ between cloud and on-premises deployment?** Infrastructure ownership, servicing, integration support and operational responsibility differ; verify feature support for the actual deployment.
2. **When should Power Platform/Azure own an extension rather than X++?** Choose the platform that owns the data/process and can enforce its contract. Use X++ for appropriate core logic and supported ecosystem services for their strengths.
3. **Which environment actions belong to PPAC, LCS and Implementation portal now?** Record the actual management plane. New affected cloud projects use PPAC; existing LCS exceptions remain; the Implementation portal serves implementation work. Preview migration is separate.
4. **What must accompany a deployable package for safe promotion?** Source commit, dependencies, build/test evidence, target compatibility, data/schema changes, smoke tests and a tested recovery plan.
5. **Why minimize model/package references?** Smaller, directional dependencies reduce coupling, build scope and upgrade risk. Reference only the packages the extension actually needs.
6. **When are build and database synchronization each required?** Build checks code/metadata; database synchronization applies relevant data-dictionary changes. A successful compile does not prove the runtime schema is current.
7. **What makes a merge conflict semantic rather than textual?** Two individually valid edits can violate a shared contract after merging. Review behavior, metadata and tests, not just conflict markers.
8. **Which evidence should CI retain?** Retain source/package identity, tool versions, analyzers, test results and deployment evidence so the promoted artifact is reproducible.
9. **Compare form creation and form extension.** Extend supported standard forms when possible; create a form for a distinct unmet need and test pattern, usability and security.
10. **Distinguish table, view, query, map and data entity.** Tables persist data; views shape reads; queries define retrieval; maps unify compatible structures; entities expose integration/data-management contracts.
11. **Which entity changes break external consumers?** Changed keys, required fields, types, validation or meaning can break consumers even when the entity name remains the same.
12. **Compare CoC, event handlers and delegates.** CoC wraps an extensible method; handlers respond to published events; delegates expose an explicit extension contract. None implies arbitrary execution ordering.
13. **Why must a CoC wrapper usually call `next`?** It preserves the rest of the chain and original implementation. Replaceable methods allow a deliberate exception under their contract.
14. **What belongs inside one X++ transaction?** Include one coherent database unit with short locks. Same-scope selection/update matters; remote effects need a separate durable handoff.
15. **When is set-based CRUD unsafe?** It is unsafe when it changes required per-record behavior or scope. It may also fall back to row-by-row execution; trace and verify semantics.
16. **How do QueryBuild ranges affect security and performance?** Ranges affect data volume and query shape. Validate inputs and authorization independently; a user-controlled filter is not an access boundary.
17. **What separates SysOperation contract/service/controller?** Contract holds serialized inputs, service performs work and controller orchestrates execution. Make retries, validation and transaction ownership explicit.
18. **Which workflow failure states require recovery?** Rejected, canceled, failed, resubmitted or partially completed work needs supported state transitions and evidence without replaying completed effects.
19. **Compare SysTest, Task Recorder and RSAT/UAT.** SysTest checks unit/component behavior; Task recorder captures business actions and can generate assets; RSAT/UAT validates broader journeys.
20. **When use SSRS, Power BI, Excel, ER or a workspace?** Choose by output, audience, interactivity, freshness and governance: paginated SSRS, analytical Power BI, controlled Excel, configurable ER or actionable workspace.
21. **Why is datastore choice independent from report surface?** The data store defines available facts, latency and access; the surface defines presentation. A different chart cannot fix a stale or unsupported store.
22. **How do report entry-point and row-level security interact?** Entry permissions authorize access to the report; supported row controls constrain its data path. Test the actual identity and underlying retrieval.
23. **What makes a KPI actionable?** Define its grain, period, filter, owner, threshold and drill-through action; verify the number and the records it opens.
24. **Compare synchronous and asynchronous coupling.** Synchronous requests couple completion/latency to dependencies; asynchronous work introduces durable state, delayed outcomes, retries and reconciliation.
25. **When choose standard entity/OData over custom service?** Prefer a supported standard entity contract that fits. Use a custom service when needed for a specific authorized business operation, not to bypass controls.
26. **How does an idempotent business-event consumer work?** Persist a stable receipt with the local effect atomically, reject inconsistent replays and design external effects for their own retry boundary.
27. **What must a recurring data job expose when staging fails?** Execution ID, status, source/staging/target errors, failed keys and successful effects; accepted or partially succeeded is not complete success.
28. **Compare composite and aggregate entities.** Composite entities group related contracts; aggregates represent summarized data. Confirm supported import/export semantics before choosing either.
29. **How do dual-write and virtual entities differ in data ownership/copying?** Dual-write synchronizes mapped copies; virtual entities call the F&O source without that replication. Both require identity, availability and lifecycle design.
30. **Distinguish migration, synchronization and event notification.** Migration transfers a bounded set; synchronization maintains shared records; notifications announce occurrences and are not bulk export.
31. **How do role, duty, privilege and permission relate?** Roles group duties, duties group privileges and privileges grant permissions to entry points/resources. Grant the narrowest supported access.
32. **Which paths must an XDS test cover?** Test supported table paths plus each entity/integration independently. Entities do not support XDS; a form result is not their authorization contract.
33. **When use table cache, global cache or temporary tables?** Choose by reuse and data lifetime, including company/user isolation and invalidation. Temporary storage has its own join, scale and transaction behavior.
34. **Which query pattern creates N+1 cost?** One initial query followed by one query for each result row; compare an equivalent grouped retrieval and measure the actual workload.
35. **How do indexes improve reads but tax writes?** An index can reduce read work but must be maintained on changes, consuming storage and write resources. Match it to measured predicates and workload.
36. **What makes a performance optimization evidence-based?** Keep comparable scope/load, a baseline, a specific change, correctness checks and before/after measurements; fewer calls alone is not proof.
37. **Is UDE the Power Platform Developer environment type?** No. It is a Sandbox with developer tooling for a single X++ developer.
38. **Does preview LCS migration move the database or allow easy rollback?** It changes the environment management plane; customer-initiated migration back to LCS is not available.
39. **Does a green migration prerequisite check establish Commerce support?** No. Commerce is unsupported during preview and its usage is not detected by that check.
40. **Can CoC wrappers depend on registration order?** No. The documented chain does not guarantee their order.
41. **Why can select-for-update before ttsBegin fail later?** The update runs at a different transaction scope; forUpdate alone is insufficient.
42. **Does retryability make an external action idempotent?** No. Repeated execution still requires stable identity, transaction design and a downstream contract.
43. **Is a business-event control number a business sequence?** No. It identifies duplicate delivery, can have gaps and does not guarantee delivery order.
44. **Does a changeset make every request in the HTTP batch atomic?** Only requests in that changeset share its atomic boundary.
45. **Do two applicable XDS policies union their allowed records?** No. Supported table access is their intersection; entity access is a separate boundary.
46. **Is doUpdate a safe speed-only replacement?** No. It bypasses update logic, handlers and CoC, changing behavior.
47. **Why inspect successful rows before retrying a partial import?** Already-applied effects may repeat; reconcile keys/totals and retry the intended failure population.
48. **Does a local SQLite test prove X++ concurrency or tenant security?** No. It demonstrates a local transaction pattern only; compile, concurrency and access tests remain separate.

---

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one primary route, build and deploy a secure extension end to end, and add another resource only for a measured gap.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MB-500 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-500) | Free | 1–2 hours to map seven domains/change log |
| [Introduction to developing](https://learn.microsoft.com/en-us/training/paths/introduction-develop-finance-operations/) | Free | 8 modules; allow 18–28 hours with tools/tests (editor estimate) |
| [Build finance and operations apps](https://learn.microsoft.com/en-us/training/paths/build-finance-operations/) | Free | 9 modules; allow 25–40 hours with X++/AOT builds (editor estimate) |
| [Extend finance and operations apps](https://learn.microsoft.com/en-us/training/paths/extending-finance-operations/) | Free | 4 modules; allow 12–20 hours with extension exercises (editor estimate) |
| [Connect to finance and operations apps](https://learn.microsoft.com/en-us/training/paths/connect-finance-operations/) | Free | 8 modules; allow 18–30 hours with integrations (editor estimate) |
| [Migrate data and go live](https://learn.microsoft.com/en-us/training/paths/migrate-data-go-live-finance-operations/) | Free | 4 modules; select data-management objectives and allow 10–16 hours (editor estimate) |
| [Analytics and reporting path](https://learn.microsoft.com/en-us/training/paths/configure-analytics-reporting-finance-operations/) | Free | 2 modules; allow 8–16 hours building/report testing (editor estimate) |
| [MB-500T00-A: Develop Finance and Operations Apps with Dynamics 365](https://learn.microsoft.com/en-us/training/courses/mb-500t00) | Paid/provider-dependent | 5 days; English |
| [MicrosoftLearning MB-500 labs](https://github.com/MicrosoftLearning/MB-500-Microsoft-Dynamics-365-Finance-and-Operations-Apps-Developer) | Free; MIT | 15–30 hours selected labs; verify UDE/current portal behavior |
| [Free MB-500 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/d365-finance-and-operations-apps-developer-associate/practice/assessment?assessment-type=practice&assessmentId=74&practice-assessment-type=certification) | Free | 45–90 minutes plus remediation |
| [Finance and Operations developer documentation](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/) | Free | 20–50 hours selected reference/troubleshooting |
| [O’Reilly: Extending D365 F&O Apps with Power Platform](https://www.oreilly.com/library/view/extending-dynamics-365/9781801811590/) | Subscription/trial | Book by Adrià Ariste Santacreu, Packt, January 2024, 274 pages; 5h48 platform estimate. Public indexed metadata only; direct fetch blocked |
| [Udemy MB500 by Arezou Behnam](https://www.udemy.com/course/mb-500-d365fnodev/) | Paid | 4h04, 8 sections/34 lectures; October 2024 update. Indexed foundation outline only; direct fetch blocked and current UDE gaps remain |
| [MeasureUp MB-500 practice test](https://www.measureup.com/microsoft-practice-test-mb-500-microsoft-dynamics-365-finance-and-operations-apps-developer.html) | Paid; free demo | 2–4 hours; 119 questions released January 2022 and public outline is older than current seven domains |
| [Microsoft Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner login required | Use five-day course pattern; verify exact signed-in event times |

The six paths contain **35 module placements and 34 distinct modules**; the migration-preparation module appears in both Connect and Migrate. Current public pages do not show aggregate runtimes, so the earlier 43h02 sum is withdrawn. Study-hour ranges above are editorial estimates. Reconcile LCS-era lessons with current UDE/PPAC instructions. Allow roughly **120–200 hours** for a developer new to F&O to complete a primary route, build/deploy the labs and remediate assessment gaps. No exact Pluralsight or Whizlabs MB-500 product was established in the earlier review; neither catalog was comprehensively searched again. Partner events require login verification and the practice endpoint exposed no question content. Bulk question-bank and guaranteed-pass listings were excluded.

## Final readiness checklist

- [ ] I can map cloud/on-prem/ecosystem responsibilities and use current PPAC/LCS/Implementation portal ownership.
- [ ] I can develop, debug, version, build, test, package, promote and roll back a model reproducibly.
- [ ] I can create/extend AOT UI/data/class elements using upgrade-safe mechanisms.
- [ ] I can write transactional X++, dynamic queries and SysOperation/workflow/serialization code with layered tests.
- [ ] I can choose and secure SSRS, Power BI, Excel, ER and workspace reporting.
- [ ] I can design APIs/entities/jobs/events/dual-write/virtual-entity integrations with retries and reconciliation.
- [ ] I can implement least-privilege roles/duties/privileges/XDS and tune from trace evidence.
- [ ] I rechecked the official blueprint, lifecycle, Practice Assessment and portal transitions before scheduling.

## Source notes

The January 30, 2026 study guide defines scope. Microsoft Learn, developer docs and MIT course labs support behavior but may include adjacent or transitioning portal content. Commercial material is supplemental and does not define objectives. All questions and labs here are original; no dumps or recalled items were used.
