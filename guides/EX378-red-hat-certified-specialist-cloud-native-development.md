---
exam_code: EX378
vendor_id: red-hat
official_blueprint: https://www.redhat.com/en/services/training/ex378-red-hat-certified-specialist-in-cloud-native-developer-exam
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# EX378 Red Hat Certified Specialist in Cloud-native Development Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ex378-coverage-record). The [official EX378 objectives](https://www.redhat.com/en/services/training/ex378-red-hat-certified-specialist-in-cloud-native-developer-exam) are authoritative.

**Current baseline:** Red Hat Build of Quarkus 3.8<br>
**Upcoming blueprint change:** None announced when checked September 1, 2026<br>
**Important freshness boundary:** Current upstream Quarkus releases use newer extension names and APIs. Build the final practice environment from the Red Hat 3.8 BOM and the dependencies/documentation supplied for the exam; translate newer courses rather than copying them blindly.<br>
**Official source:** [Red Hat EX378 exam page](https://www.redhat.com/en/services/training/ex378-red-hat-certified-specialist-in-cloud-native-developer-exam)

## How to use this guide

EX378 is a hands-on Java development exam. You implement the server side of a complete Quarkus microservice backed by persistent data. There is no internet or personal documentation; for most Red Hat exams, documentation shipped with the product is available. Code and configuration must remain functional after restart, so a dev-mode demonstration alone is insufficient.

Red Hat recommends DO378 or equivalent hands-on experience, VS Code/VSCodium familiarity in RHEL, strong Java SE skills (including exceptions, annotations, and collections), and some Kafka/messaging and OpenShift familiarity. These are preparation dependencies, not invented certification prerequisites.

Build one small system throughout your study—for example, an order API with `Customer` and `Order` entities, an inventory REST client, asynchronous order events, JWT roles, health/metrics/traces, and fault tolerance. For each change:

1. inspect the 3.8 BOM, installed extensions, generated project, configuration sources, and test baseline;
2. make one focused code/configuration change and explain its thread, transaction, security, and failure behavior;
3. compile and run targeted unit/integration tests, then exercise the endpoint or channel;
4. observe HTTP status/body, database state, acknowledgment, health, metrics, and traces as appropriate;
5. restart in a production-like mode and prove configuration and behavior persist.

Public objectives are unweighted. Do not invent domain percentages.

## Objective map

| Official task group | What mastery looks like |
|---|---|
| Configuration | Inject/look up values, map objects, reason about source precedence, add a custom source, and use profiles |
| MicroProfile Fault Tolerance | Apply timeout, retry, fallback, circuit breaker, bulkhead, async behavior, and externalized policy intentionally |
| MicroProfile Health | Implement startup/liveness/readiness/reactive/grouped/wellness checks and useful responses |
| Micrometer metrics | Instrument tagged counters, gauges, timers, summaries, and long tasks; expose/export observations |
| MP-JWT RBAC | Validate bearer tokens, require authentication/roles, and map claims/identity to container APIs |
| RESTEasy Reactive and Jakarta REST | Implement JSON CRUD endpoints, HTTP semantics, CDI, validation, and non-blocking behavior |
| JPA with Panache | Map entities/relationships and implement CRUD/custom operations using active-record or repository style |
| Reactive Messaging | Use channels, incoming/outgoing flows, reactive concepts, and correct acknowledgment |
| MicroProfile OpenAPI | Produce/customize a contract, inspect Swagger UI, and reason about versioned remote endpoints |
| REST Client Reactive | Configure typed synchronous/asynchronous clients, headers, parameters, and exception mapping |
| OpenTelemetry | Produce and follow traces, spans, context propagation, correlation identifiers, and baggage |

## 1. Configuration and profiles

Configuration separates deploy-time policy from compiled code. Practice `application.properties` and environment-aware overrides with `@ConfigProperty`, programmatic lookup, and `@ConfigMapping` interfaces that group related values into a typed object. Decide whether a value is required, optional, or has a safe default; a missing critical secret or endpoint should fail clearly rather than silently choosing an unsafe value.

Know source precedence in the 3.8 environment. Higher-ordinal sources override lower ones; system properties, environment variables, `.env`, external/config-directory files, classpath configuration, profile-aware files, and custom `ConfigSource` implementations occupy defined positions. Inspect the actual 3.8 ordering instead of relying on a newer diagram. A custom source needs an explicit name, properties, and ordinal strategy; test collision behavior.

Profiles express differences such as `%dev`, `%test`, and `%prod`, plus named profiles. They do not excuse duplicating the whole configuration. Test the effective value under each target profile and distinguish build-time-fixed properties from runtime-overridable properties.

> **Related item:** Twelve-factor configuration is a useful architectural lens, but the objective is practical Quarkus behavior: injection, lookup, mapping, precedence, custom sources, and profiles.

## 2. Fault-tolerant microservices

Start from the failure contract. A timeout bounds how long a call may consume resources. Retry handles transient failures but can amplify load or duplicate side effects. Fallback provides a degraded result. Circuit breaker stops repeated calls while a dependency is unhealthy. Bulkhead limits concurrent pressure. Async execution changes when and where completion/failure is observed.

Compose policies deliberately. Retrying a non-idempotent POST can create duplicates; a fallback that returns plausible stale data can hide an outage; a timeout does not necessarily cancel all underlying work. Know annotation placement, defaults, exception inclusion/exclusion, breaker thresholds/windows/states, semaphore versus thread-pool bulkheads where applicable, and how configuration can override annotation values.

Write deterministic tests using a fake dependency that fails, delays, or recovers on command. Assert call counts, final exception/result, timing boundary, breaker transition, concurrency rejection, and metrics/log evidence. Understand the relationship with MicroProfile Config: operational policy should be adjustable without code edits where the 3.8 implementation supports it.

> **Related item:** Idempotency keys and deduplication are not named fault-tolerance annotations, but they make retries safe in real distributed systems.

## 3. Health checks

Health answers different platform questions. Startup indicates initialization completion, liveness whether restart may help, and readiness whether the instance should receive traffic. Do not make liveness depend on every remote system; a database outage should not necessarily trigger a restart storm. Readiness can reflect a required dependency while still returning diagnostic data.

Implement the relevant health-check interface/annotations and construct `HealthCheckResponse` with human-readable names, UP/DOWN state, and non-secret diagnostic data. Practice synchronous and reactive checks, health groups with `@HealthGroup`, and the 3.8 `@Wellness` behavior named by the blueprint. Use the Health UI only as an inspection aid; also call the health endpoints and verify status payloads.

Tests should switch a controllable dependency between healthy/unhealthy and assert both the aggregate and component result. Bound health-check latency. Never expose credentials, tokens, personal data, or raw internal exceptions in the response.

> **Related item:** Kubernetes/OpenShift probes consume health signals, but application health design remains useful even when deployment manifests are not the coding focus of a particular EX378 task.

## 4. Micrometer metrics

Metrics describe behavior over time. Counters measure monotonically increasing events; gauges sample current state; timers measure event count and duration; distribution summaries observe non-time values; long-task timers track in-progress operations. Choose the type from the question you need to answer, not from whichever annotation you remember.

Tags create dimensions but also series. Use bounded values such as operation or result class; never tag by user ID, request ID, free-form error, or another high-cardinality value. Practice annotation-based instrumentation and direct registry APIs, then query the exposed metrics endpoint and verify names, tags, counts, and units after controlled requests.

Know how Quarkus exposes metrics and how a management agent/scraper consumes them. An application that exposes data is not automatically monitored: scrape/export configuration, aggregation, dashboards, and alerts are downstream concerns. Keep business metrics separate from JVM/HTTP framework metrics and avoid double-counting.

> **Related item:** Service-level indicators combine metrics into user-centered reliability evidence. An exam task may ask for one timer or counter; production engineering asks what decision that observation supports.

## 5. JWT authentication and RBAC

A JWT is a signed token carrying claims; base64url encoding is not encryption. Validate signature, issuer, audience where required, time claims, and the trust/key configuration before using identity or roles. Separate authentication (is this token valid and who is the subject?) from authorization (may this identity perform this operation?).

Configure MP-JWT bearer authentication for the 3.8 application, mark endpoints/application security, and apply role constraints. Map token claims and groups to container APIs such as the security principal and role checks. Practice public, authenticated, and role-restricted endpoints; test missing, malformed, expired, wrong-issuer/audience/signature, valid-but-wrong-role, and authorized tokens.

Do not log whole tokens. Use short-lived generated lab credentials and local keys in ignored test resources. A passing positive test is incomplete without denied-path evidence and correct 401-versus-403 semantics: unauthenticated is different from authenticated-but-forbidden.

> **Related item:** OAuth 2.0/OIDC define broader authorization and identity flows; MP-JWT focuses the service's bearer-token validation and RBAC boundary. Know which component issues tokens and which validates them.

## 6. RESTEasy Reactive and Jakarta REST

Model resources, not procedure names. `GET` retrieves without changing state; `POST` commonly creates or invokes a non-idempotent operation; `PUT` replaces/updates an identified resource with idempotent semantics; `DELETE` removes idempotently from the client's perspective. Use status codes and bodies deliberately: distinguish successful retrieval, creation with location, no-content deletion, invalid input, missing resource, conflict, authentication failure, authorization denial, and server/dependency failure.

Implement root resource classes with paths, HTTP-method annotations, media types, path/query/header parameters, and JSON mapping. Keep transport DTOs separate from persistence entities when boundary stability or validation requires it. Use CDI scopes/injection rather than manually constructing managed components.

Bean Validation belongs at the boundary and may also protect service operations. Handle constraint failures consistently. Reactive/non-blocking endpoints must not perform blocking JDBC or remote calls on an event-loop thread. Understand when a synchronous return is treated as blocking and when `Uni`, completion stages, or explicit annotations change execution.

Test behavior, not just the happy response: validation payloads, content type, status, location header, duplicate/missing IDs, transactions, and async failures. Keep error mapping stable and avoid leaking stack traces.

> **Related item:** An API's idempotency and concurrency contract often needs ETags/version columns or idempotency keys. These are adjacent production patterns, not a claim that every mechanism appears verbatim in EX378.

## 7. JPA and Panache

Panache supports active record (entities inherit behavior and expose operations) and repository (persistence operations live in injected repository classes) patterns. Choose one coherently for a type. Repository style often separates domain objects from data access; active record minimizes scaffolding. Be able to implement both, because the objective names their difference.

Map identifiers, fields, constraints, and a bidirectional one-to-many relationship. Both sides must be consistent in memory: helper methods should add/remove the child and set/clear the parent. Understand owning side, `mappedBy`, cascade, orphan removal, fetch implications, and JSON recursion risk. Database cascade and JPA cascade are related but distinct.

Implement create/read/update/delete in transaction boundaries. Panache convenience methods do not remove JPA concepts: managed versus detached state, flush timing, optimistic locking, lazy loading, N+1 queries, and constraint violations still matter. Add custom entity or repository queries using parameters rather than string-concatenated input.

Integration tests should use a disposable database, assert both HTTP and database state, roll back or reset predictably, and cover relationship updates/deletes. A test that passes only because dev mode auto-creates a schema is not production-like evidence.

> **Related item:** Database migrations are the durable way to evolve schemas. Migration tooling is adjacent to the named Panache objective, but relying on destructive auto-generation hides important persistence failures.

## 8. Reactive Messaging

Reactive Messaging connects named channels. `@Incoming` consumes, `@Outgoing` produces, and a processing method may transform between them. Distinguish payloads from `Message<T>` when metadata or explicit acknowledgment is needed. Channel names in code must match connector configuration.

Acknowledgment defines when upstream considers work complete. Acknowledge too early and a later database failure can lose work; fail to acknowledge and messages may be redelivered. Understand the 3.8 strategies and how method signatures/processing stages affect them. Make consumers idempotent because at-least-once delivery can produce duplicates.

Reactive code must respect asynchronous completion and back pressure. Do not block event-loop processing with JDBC, sleeps, or synchronous remote calls. Test with controlled messages: success, malformed payload, downstream failure, duplicate, ordering-sensitive sequence, and recovery. Assert emitted output and side effects rather than merely checking logs.

> **Related item:** Kafka partitions, consumer groups, offsets, and delivery guarantees explain real connector behavior. The public task group names core messaging/channels/acknowledgment; broker administration is not automatically exam scope.

## 9. OpenAPI

OpenAPI is a machine-readable service contract; Swagger UI is one way to explore it. Quarkus can derive a default document from Jakarta REST and annotations, and you can add static/custom information. Verify paths, methods, parameters, schemas, content types, status responses, security requirements, and version metadata against actual behavior.

Avoid documenting a 200 response while code returns 201 or omitting validation/error shapes. Retrieve the generated document in tests and exercise representative operations. The blueprint also names linking to semantic-versioned remote service endpoints: understand how a client selects an API version and how compatibility expectations differ across major, minor, and patch changes.

> **Related item:** Contract tests catch drift between producer behavior and consumer expectations. Generating documentation is not enough if no test proves it matches the service.

## 10. REST Client Reactive

Define a type-safe client interface with Jakarta REST and MicroProfile annotations, register it, configure its base URI/key, and inject/use it. Apply path/query/header parameters and content types exactly. Separate base endpoint configuration from resource paths and keep environment differences in configuration.

For non-blocking calls, return the supported async/reactive type and keep the chain non-blocking. Add required custom headers through parameters, annotations, or a header factory as appropriate; do not forward credentials indiscriminately. Convert non-success responses with an exception mapper into domain-relevant failures while preserving useful status/context and closing response resources.

Test against a stub server for success, timeouts, malformed JSON, 4xx/5xx mapping, headers, URI configuration, and async cancellation/failure. Then compose with the fault-tolerance policies from Section 2 without creating unsafe retries.

## 11. OpenTelemetry tracing

A trace represents a distributed request; spans represent timed operations and parent-child relationships. Context propagation carries correlation identifiers across process/thread boundaries so downstream spans join the trace. Baggage carries selected application context but is propagated data—not a safe place for secrets or unbounded personal information.

Instrument an inbound REST request, database/service operation, REST-client call, and message send/receive where supported. Inspect trace/span IDs, parentage, names, attributes, events, status, and timing in an exporter/collector. Add manual spans only where automatic instrumentation lacks useful semantic boundaries; excessive spans create cost and noise.

Async/reactive execution can lose context if code steps outside supported propagation. Write a test/demo that follows one request across services and verifies the chain. Distinguish logs, metrics, and traces: correlation helps them work together, but none substitutes for the others.

> **Related item:** Sampling and telemetry retention control observability cost and privacy. They are important production controls even when the hands-on task focuses on creating and following spans.

## Integrated scenarios

### Scenario 1: Secured order service

Build JSON CRUD endpoints with bean validation, JWT roles, Panache entities/repository, bidirectional customer-orders relationship, profile-based database configuration, correct HTTP semantics, OpenAPI, health, tagged metrics, and traces. Prove authorized and denied paths plus database state after restart.

### Scenario 2: Resilient inventory integration

Call a versioned inventory endpoint with REST Client Reactive, configured URI/headers, exception mapping, timeout/retry/circuit breaker/bulkhead/fallback policy, readiness impact, metrics, and trace propagation. Use a controllable stub to prove slow, failing, recovering, unauthorized, and malformed-response behavior.

### Scenario 3: Asynchronous fulfillment

Publish accepted orders to an outgoing channel and consume fulfillment updates through an incoming channel. Choose acknowledgment deliberately, make persistence idempotent, expose processing health/metrics, and preserve trace context. Test duplicate, poison, downstream-failure, and replay paths.

## Hands-on labs

1. **3.8 project baseline:** create from the Red Hat 3.8 BOM, inventory extensions, run tests/dev mode/package mode, and record local-documentation paths.
2. **Configuration matrix:** implement injection, lookup, typed mapping, custom source and profiles; assert precedence and required/default behavior.
3. **REST + validation:** implement all four HTTP methods, CDI service boundary, JSON DTOs, correct responses and reactive endpoint behavior with negative tests.
4. **Panache persistence:** implement active-record and repository examples, bidirectional mapping, transactions, CRUD/custom query, and clean database replay.
5. **Security + contract:** secure endpoints with MP-JWT roles, test invalid/forbidden/allowed tokens, and verify OpenAPI matches behavior.
6. **Client + resilience:** build REST Client Reactive with configuration, headers and exception mapping; add each fault-tolerance strategy and deterministic failure tests.
7. **Messaging + acknowledgment:** implement incoming/outgoing channels, async transformation and explicit failure behavior; prove success, duplicate and redelivery safety.
8. **Observability + restart:** implement health groups/wellness/reactive checks, all named Micrometer instrument types and cross-service OpenTelemetry; package, restart, re-run the complete evidence suite.

## Original knowledge checks

1. Why must final labs use the Red Hat 3.8 BOM rather than latest upstream defaults?
2. What makes a configuration value required, optional, or safely defaulted?
3. How does source ordinal affect the effective value?
4. What problem does a typed configuration mapping solve?
5. When should a custom `ConfigSource` have a higher ordinal?
6. Why can a retry make an outage or side effect worse?
7. How do timeout, fallback, circuit breaker, and bulkhead differ?
8. What deterministic evidence proves a circuit breaker recovered?
9. Why should liveness avoid depending on every remote service?
10. How do startup, readiness, liveness, wellness, and health groups differ?
11. What data is unsafe in a health response?
12. When should you use a counter, gauge, timer, summary, or long-task timer?
13. Why are user IDs dangerous metric tags?
14. What separates exposed metrics from an operational monitoring system?
15. Which JWT properties must be validated before trusting roles?
16. When should an endpoint return 401 versus 403?
17. Why must token tests include invalid and wrong-role cases?
18. How do POST and PUT idempotency expectations differ?
19. Which status/body/location behavior should creation use?
20. Why can blocking persistence not run on an event-loop thread?
21. How does CDI improve testability and lifecycle management?
22. When should API DTOs differ from persistence entities?
23. How do Panache active record and repository patterns differ?
24. Which side owns a bidirectional JPA relationship?
25. Why should relationship helper methods update both sides?
26. What transaction and flush behavior can hide until integration testing?
27. How do `@Incoming` and `@Outgoing` connect channels?
28. When is explicit `Message<T>` handling valuable?
29. Why can acknowledgment timing cause loss or redelivery?
30. What makes a message consumer safe under duplicate delivery?
31. What does Swagger UI provide that an OpenAPI document does not, and vice versa?
32. How can a contract test expose status/schema drift?
33. What belongs in REST-client base URI configuration?
34. Why should a response exception mapper preserve status/context?
35. How can an async REST client accidentally become blocking?
36. How do a trace, span, trace ID, and parent span relate?
37. What is the purpose and risk of baggage?
38. How can reactive execution lose trace context?
39. Why are logs, metrics, health, and traces complementary?
40. What evidence proves the complete microservice works after restart?

## Version and course-gap checklist

For every current or older resource, compare it with Red Hat Build of Quarkus 3.8:

- Red Hat BOM/plugin coordinates and supported extensions;
- Java/Jakarta namespace and runtime requirements;
- RESTEasy Reactive versus newer Quarkus REST naming;
- MicroProfile Config source order, mappings, profiles, and custom sources;
- fault-tolerance annotations/configuration and async return types;
- health annotations including wellness/groups/reactive checks;
- Micrometer instrument and registry APIs;
- MP-JWT configuration and role mapping;
- Panache/JPA transaction and relationship APIs;
- Reactive Messaging acknowledgment and connector configuration;
- OpenAPI, REST Client Reactive, and exception-mapper APIs;
- OpenTelemetry extension/configuration/context propagation.

Newer syntax is not automatically wrong in production, but it is wrong preparation if unavailable in the assigned 3.8 environment. Older `javax.*`, RESTEasy Classic, OpenTracing, or pre-Micrometer examples require explicit migration.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Pick resources that match your Java background, then implement every public objective in one coherent 3.8 project. Estimated time includes selected reading or coding where stated; access and metadata can change.

| Resource | Access | Estimated time |
|---|---|---:|
| EX378 objectives + Red Hat/Quarkus 3.8 docs | Public | 20–40 selected hours |
| Red Hat DO378 | Paid | About 5 training days plus 40–80 hours independent coding |
| Red Hat DO078 | Free account | 2–4 hours estimated plus 5–10 hours coding |
| Red Hat Developer Quarkus learning hub | Public / free account | 3–10 selected hours |
| Pluralsight Quarkus path | Paid | 10 hours listed plus 30–60 hours coding |
| O'Reilly/Manning Quarkus in Action | Paid | 416 pages / 12 hours 2 minutes plus 30–60 hours coding |
| Udemy Cloud-native Microservices with Quarkus | Paid | 9 hours 51 minutes plus 30–60 hours coding |

- **Official scope and build:** [Red Hat Build of Quarkus 3.8 getting started](https://docs.redhat.com/en/documentation/red_hat_build_of_quarkus/3.8/html/getting_started_with_red_hat_build_of_quarkus/index) establishes supported project/BOM tooling. The archived [upstream Quarkus 3.8 guides](https://quarkus.io/version/3.8/guides/) provide focused exercises for every major objective; prefer Red Hat-supported coordinates where they differ.
- **Official route:** [DO378 Cloud-native Microservices Development with Quarkus](https://www.redhat.com/en/services/training/red-hat-cloud-native-microservices-development-quarkus-do378) uses Quarkus 3.8 and OpenShift 4.14 and is the closest end-to-end route. Allow about five instructor-led days plus extensive independent coding.
- **Free orientation:** [DO078 Quarkus Technical Overview](https://www.redhat.com/en/services/training/do078-quarkus-technical-overview) covers project generation, REST, JDBC/Panache, health, OpenAPI, containers/native builds and OpenShift. The [Red Hat Developer Quarkus learning hub](https://developers.redhat.com/learn/quarkus) collects learning paths and interactive tutorials; select 3–10 relevant hours, and do not treat it as a fixed 3.8 exam map.
- **Current broad video/labs:** [Pluralsight Quarkus path](https://www.pluralsight.com/paths/quarkus) lists four courses, three guided labs and ten hours, with 2025–2026 REST, persistence, reactive and event-driven content. Map security, configuration details, all observability types and 3.8 APIs explicitly.
- **Detailed book:** [O'Reilly/Manning Quarkus in Action](https://www.oreilly.com/library/view/quarkus-in-action/9781633438958/) is a January 2025, 416-page/12-hour-2-minute reference covering configuration, REST, security, Panache, messaging, health, metrics, tracing and fault tolerance. It is broader than EX378 and may use a newer Quarkus stream; backport examples to 3.8.
- **Current commercial course:** [Udemy / Ansgar Schulte Cloud-native Microservices with Quarkus](https://www.udemy.com/course/quarkus-by-example/) lists 9 hours 51 minutes, 116 lectures, and a June 2026 update. Its latest sections discuss newer Quarkus REST naming; use its hands-on REST/Panache/config/security/client/resilience/messaging coverage only after a 3.8 API check.

No exact current EX378 MeasureUp, Whizlabs, official practice test, or complete certification-specific O'Reilly/Pluralsight route was independently verified September 1. Avoid “certified questions,” real/recalled tasks, and answer banks; this is a coding exam. Plan **140–240 hours** with strong modern Java/Jakarta experience, or **300–500 hours** if CDI, JPA, reactive programming, messaging, security, and observability are new.

## Related-item note

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Source map and freshness notes

The EX378 page defines scope and the Red Hat Build of Quarkus 3.8 baseline. Red Hat 3.8 documentation and the archived upstream 3.8 guides control implementation details; DO378 describes the official learning route. Commercial content supplies explanation and practice, not scope.

Volatile: objective text, Red Hat BOM/extension support, documentation availability, APIs, Java/runtime requirements, course version/runtime/access, delivery, price, and schedule. Recheck the official page and build a clean 3.8 project before the final study sprint.

This guide uses only public objective language and original scenarios, labs, and checks. It does not reproduce or solicit recalled exam tasks.
