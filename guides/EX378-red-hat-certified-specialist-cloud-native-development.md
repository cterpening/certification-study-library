---
exam_code: EX378
vendor_id: red-hat
official_blueprint: https://www.redhat.com/en/services/training/ex378-red-hat-certified-specialist-in-cloud-native-developer-exam
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# EX378 Red Hat Certified Specialist in Cloud-native Development Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 28, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ex378-coverage-record). The [official EX378 objectives](https://www.redhat.com/en/services/training/ex378-red-hat-certified-specialist-in-cloud-native-developer-exam) are authoritative.

**Current baseline:** Red Hat Build of Quarkus 3.8<br>
**Upcoming blueprint change:** None announced when checked September 28, 2026<br>
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

Public objectives are unweighted. The September 28 review mapped all **64 detailed tasks in eleven groups** and compared them with EX378V38K in the [official objectives by version PDF](https://training-lms.redhat.com/public_content/redhat/training/Red%20Hat%20Certification%20Exam%20Objectives%20by%20Version.pdf). The PDF also lists other versions; verify the version assigned to your booking. Do not invent domain percentages.

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

The [3.8 configuration reference](https://quarkus.io/version/3.8/guides/config-reference/) defines these default source ordinals. Higher values win for the same resolved property; custom sources and explicit ordinal overrides can alter the result.

| Source | Default ordinal |
|---|---:|
| Java system properties | 400 |
| Environment variables | 300 |
| Working-directory `.env` | 295 |
| Working-directory `config/application.properties` | 260 |
| Classpath `application.properties` | 250 |
| Classpath `META-INF/microprofile-config.properties` | 100 |

With `study.label=classpath` and environment variable `STUDY_LABEL=environment`, the environment value wins. Adding `-Dstudy.label=system` overrides it. Test profiles separately: `%test.study.label=test-profile` is active during tests, and a profile-aware file has precedence over the matching profile entry in its same-location main file. A custom source needs a name, property values and a deliberate ordinal; choosing 450 would also override system properties, which may defeat an operator's intended emergency override.

Profiles express differences such as `%dev`, `%test`, and `%prod`, plus named profiles. They do not excuse duplicating the whole configuration. Test the effective value under each target profile and distinguish build-time-fixed properties from runtime-overridable properties.

> **Related item:** Twelve-factor configuration is a useful architectural lens, but the objective is practical Quarkus behavior: injection, lookup, mapping, precedence, custom sources, and profiles.

## 2. Fault-tolerant microservices

Start from the failure contract. A timeout bounds how long a call may consume resources. Retry handles transient failures but can amplify load or duplicate side effects. Fallback provides a degraded result. Circuit breaker stops repeated calls while a dependency is unhealthy. Bulkhead limits concurrent pressure. Async execution changes when and where completion/failure is observed.

Compose policies deliberately. Retrying a non-idempotent POST can create duplicates; a fallback that returns plausible stale data can hide an outage; a timeout does not necessarily cancel all underlying work. Know annotation placement, defaults, exception inclusion/exclusion, breaker thresholds/windows/states, semaphore versus thread-pool bulkheads where applicable, and how configuration can override annotation values.

The [3.8 fault-tolerance guide](https://quarkus.io/version/3.8/guides/smallrye-fault-tolerance/) uses the configuration shape `fully.qualified.Class/method/Retry/maxRetries=2` to override an annotation for one method. Two retries mean up to three attempts when the failure remains retryable and duration limits permit. Quarkus enables SmallRye non-compatible mode by default: supported `Uni`/`CompletionStage` return types receive asynchronous fault-tolerance behavior without requiring `@Asynchronous`. Do not infer thread dispatch or policy composition from the generic MicroProfile specification alone.

Write deterministic tests using a fake dependency that fails, delays, or recovers on command. Assert call counts, final exception/result, timing boundary, breaker transition, concurrency rejection, and metrics/log evidence. Understand the relationship with MicroProfile Config: operational policy should be adjustable without code edits where the 3.8 implementation supports it.

> **Related item:** Idempotency keys and deduplication are not named fault-tolerance annotations, but they make retries safe in real distributed systems.

## 3. Health checks

Health answers different platform questions. Startup indicates initialization completion, liveness whether restart may help, and readiness whether the instance should receive traffic. Do not make liveness depend on every remote system; a database outage should not necessarily trigger a restart storm. Readiness can reflect a required dependency while still returning diagnostic data.

Implement the relevant health-check interface/annotations and construct `HealthCheckResponse` with human-readable names, UP/DOWN state, and non-secret diagnostic data. Practice synchronous and reactive checks, health groups with `@HealthGroup`, and the 3.8 `@Wellness` behavior named by the blueprint. Use the Health UI only as an inspection aid; also call the health endpoints and verify status payloads.

Use the [3.8 health reference](https://quarkus.io/version/3.8/guides/smallrye-health/) to distinguish `/q/health/started`, `/q/health/live` and `/q/health/ready`; `/q/health` aggregates checks. Import the health `org.eclipse.microprofile.health.Startup` qualifier, not `io.quarkus.runtime.Startup`, which has a different bean-initialization purpose. Custom groups select checks under `/q/health/group/<name>`. [SmallRye wellness](https://smallrye.io/docs/smallrye-health/3.0.1/wellness.html) is a supplemental monitoring group, not inherently a restart or traffic-removal instruction; Quarkus 3.8 defaults its wellness path to `/q/health/well`. Account for customized root/management paths before copying a probe URL.

Tests should switch a controllable dependency between healthy/unhealthy and assert both the aggregate and component result. Bound health-check latency. Never expose credentials, tokens, personal data, or raw internal exceptions in the response.

> **Related item:** Kubernetes/OpenShift probes consume health signals, but application health design remains useful even when deployment manifests are not the coding focus of a particular EX378 task.

## 4. Micrometer metrics

Metrics describe behavior over time. Counters measure monotonically increasing events; gauges sample current state; timers measure event count and duration; distribution summaries observe non-time values; long-task timers track in-progress operations. Choose the type from the question you need to answer, not from whichever annotation you remember.

Tags create dimensions but also series. Use bounded values such as operation or result class; never tag by user ID, request ID, free-form error, or another high-cardinality value. Practice annotation-based instrumentation and direct registry APIs, then query the exposed metrics endpoint and verify names, tags, counts, and units after controlled requests.

The [3.8 Micrometer guide](https://quarkus.io/version/3.8/guides/telemetry-micrometer/) also warns that observed gauge objects are not strongly retained by default. Keep the application-owned measured object alive or the gauge can disappear/report NaN after collection. A timer already counts its observations; an extra counter for the same event can be redundant. Use the appropriate registry extension, such as `quarkus-micrometer-registry-prometheus`, for the intended backend.

Know how Quarkus exposes metrics and how a management agent/scraper consumes them. An application that exposes data is not automatically monitored: scrape/export configuration, aggregation, dashboards, and alerts are downstream concerns. Keep business metrics separate from JVM/HTTP framework metrics and avoid double-counting.

> **Related item:** Service-level indicators combine metrics into user-centered reliability evidence. An exam task may ask for one timer or counter; production engineering asks what decision that observation supports.

## 5. JWT authentication and RBAC

A JWT is a signed token carrying claims; base64url encoding is not encryption. Validate signature, issuer, audience where required, time claims, and the trust/key configuration before using identity or roles. Separate authentication (is this token valid and who is the subject?) from authorization (may this identity perform this operation?).

Configure MP-JWT bearer authentication for the 3.8 application, mark endpoints/application security, and apply role constraints. Map token claims and groups to container APIs such as the security principal and role checks. Practice public, authenticated, and role-restricted endpoints; test missing, malformed, expired, wrong-issuer/audience/signature, valid-but-wrong-role, and authorized tokens.

The [3.8 JWT guide](https://quarkus.io/version/3.8/guides/security-jwt/) identifies `mp.jwt.verify.publickey.location`, `mp.jwt.verify.issuer` and `mp.jwt.verify.audiences` as relevant verification settings. Test expiration beyond the configured `mp.jwt.verify.clock.skew`; a token a few seconds past `exp` can still pass within the default allowance. Map the verified `groups` claim and any configured alternate claim path deliberately before using `@RolesAllowed`.

Do not log whole tokens. Use short-lived generated lab credentials and local keys in ignored test resources. A passing positive test is incomplete without denied-path evidence and correct 401-versus-403 semantics: unauthenticated is different from authenticated-but-forbidden.

> **Related item:** OAuth 2.0/OIDC define broader authorization and identity flows; MP-JWT focuses the service's bearer-token validation and RBAC boundary. Know which component issues tokens and which validates them.

## 6. RESTEasy Reactive and Jakarta REST

Model resources, not procedure names. `GET` retrieves without changing state; `POST` commonly creates or invokes a non-idempotent operation; `PUT` replaces/updates an identified resource with idempotent semantics; `DELETE` removes idempotently from the client's perspective. Use status codes and bodies deliberately: distinguish successful retrieval, creation with location, no-content deletion, invalid input, missing resource, conflict, authentication failure, authorization denial, and server/dependency failure.

Implement root resource classes with paths, HTTP-method annotations, media types, path/query/header parameters, and JSON mapping. Keep transport DTOs separate from persistence entities when boundary stability or validation requires it. Use CDI scopes/injection rather than manually constructing managed components.

Bean Validation belongs at the boundary and may also protect service operations. Handle constraint failures consistently. Reactive/non-blocking endpoints must not perform blocking JDBC or remote calls on an event-loop thread. Understand when a synchronous return is treated as blocking and when `Uni`, completion stages, or explicit annotations change execution.

The [3.8 RESTEasy Reactive reference](https://quarkus.io/version/3.8/guides/resteasy-reactive/) places ordinary synchronous resource methods on worker threads by default and `Uni`/`CompletionStage` methods on I/O threads by default; `@Transactional` implies worker execution. Explicit `@Blocking`/`@NonBlocking` and inherited annotations can change dispatch. Returning a `Uni` does not turn blocking JDBC into non-blocking I/O. Keep the entire chain appropriate for its actual execution thread.

Test behavior, not just the happy response: validation payloads, content type, status, location header, duplicate/missing IDs, transactions, and async failures. Keep error mapping stable and avoid leaking stack traces.

> **Related item:** An API's idempotency and concurrency contract often needs ETags/version columns or idempotency keys. These are adjacent production patterns, not a claim that every mechanism appears verbatim in EX378.

## 7. JPA and Panache

Panache supports active record (entities inherit behavior and expose operations) and repository (persistence operations live in injected repository classes) patterns. Choose one coherently for a type. Repository style often separates domain objects from data access; active record minimizes scaffolding. Be able to implement both, because the objective names their difference.

Map identifiers, fields, constraints, and a bidirectional one-to-many relationship. Both sides must be consistent in memory: helper methods should add/remove the child and set/clear the parent. Understand owning side, `mappedBy`, cascade, orphan removal, fetch implications, and JSON recursion risk. Database cascade and JPA cascade are related but distinct.

Implement create/read/update/delete in transaction boundaries. Panache convenience methods do not remove JPA concepts: managed versus detached state, flush timing, optimistic locking, lazy loading, N+1 queries, and constraint violations still matter. Add custom entity or repository queries using parameters rather than string-concatenated input.

In the [3.8 Panache reference](https://quarkus.io/version/3.8/guides/hibernate-orm-panache/), a managed entity's field changes are written by dirty checking; do not invent a required second `persist()` call for updates. `persistAndFlush()` synchronizes pending SQL so many database errors surface there, but **flush is not commit**: a later failure can still roll back that transaction. A query may trigger a flush before commit. Close streams obtained from Panache with try-with-resources and keep the required transaction open while consuming them.

Integration tests should use a disposable database, assert both HTTP and database state, roll back or reset predictably, and cover relationship updates/deletes. A test that passes only because dev mode auto-creates a schema is not production-like evidence.

> **Related item:** Database migrations are the durable way to evolve schemas. Migration tooling is adjacent to the named Panache objective, but relying on destructive auto-generation hides important persistence failures.

## 8. Reactive Messaging

Reactive Messaging connects named channels. `@Incoming` consumes, `@Outgoing` produces, and a processing method may transform between them. Distinguish payloads from `Message<T>` when metadata or explicit acknowledgment is needed. Channel names in code must match connector configuration.

Acknowledgment marks processing success at the messaging boundary; a connector's offset commit is a separate step. The [3.8 Kafka reference](https://quarkus.io/version/3.8/guides/kafka/) explains payload/`Record` post-processing acknowledgment, async completion and explicit `Message<T>` acknowledgment. For Kafka, the default `throttled` strategy, when auto-commit is not enabled, commits the highest contiguous acknowledged position periodically. An acknowledged record may therefore be replayed after a crash before its offset commit. Do not acknowledge a `Message` before the database transaction actually commits; even committing the database first leaves a crash window before acknowledgment/offset commit.

| Failure or policy choice | Consequence to test |
|---|---|
| Database commit succeeds, process crashes before offset commit | Replay is possible; deduplicate by a stable event identity in the same database transaction as the effect |
| Async records complete out of order | An unacknowledged earlier record can prevent contiguous progress; inspect health/backlog rather than assuming later completions advance the safe position |
| `enable.auto.commit=true` | Kafka client periodic commits are not proof that application processing completed |
| `failure-strategy=fail` | Stop consumption/fail health on a negative acknowledgment; repair the cause |
| `failure-strategy=ignore` | Log and advance past the failed record; the business effect may be lost |
| `failure-strategy=dead-letter-queue` | Send a failed record to the configured dead-letter topic and advance the source offset; investigation/replay remains an application responsibility |

Choosing Kafka transactions does not by itself make an independent relational database update atomic with Kafka. The integrated lab must prove its own duplicate and recovery contract.

Reactive code must respect asynchronous completion and back pressure. Do not block event-loop processing with JDBC, sleeps, or synchronous remote calls. Test with controlled messages: success, malformed payload, downstream failure, duplicate, ordering-sensitive sequence, and recovery. Assert emitted output and side effects rather than merely checking logs.

> **Related item:** Kafka partitions, consumer groups, offsets, and delivery guarantees explain real connector behavior. The public task group names core messaging/channels/acknowledgment; broker administration is not automatically exam scope.

## 9. OpenAPI

OpenAPI is a machine-readable service contract; Swagger UI is one way to explore it. Quarkus can derive a default document from Jakarta REST and annotations, and you can add static/custom information. Verify paths, methods, parameters, schemas, content types, status responses, security requirements, and version metadata against actual behavior.

Avoid documenting a 200 response while code returns 201 or omitting validation/error shapes. Retrieve the generated document in tests and exercise representative operations. The blueprint also names linking to semantic-versioned remote service endpoints: understand how a client selects an API version and how compatibility expectations differ across major, minor, and patch changes.

> **Related item:** Contract tests catch drift between producer behavior and consumer expectations. Generating documentation is not enough if no test proves it matches the service.

The [3.8 OpenAPI guide](https://quarkus.io/version/3.8/guides/openapi-swaggerui/) documents static contracts under `META-INF/openapi.yaml` and the `/q/openapi` endpoint. Swagger UI is included by default in dev/test modes; production inclusion via `quarkus.swagger-ui.always-include=true` is a build-time choice. A declared security scheme describes a contract and does not enforce endpoint authorization.

## 10. REST Client Reactive

Define a type-safe client interface with Jakarta REST and MicroProfile annotations, register it, configure its base URI/key, and inject/use it. Apply path/query/header parameters and content types exactly. Separate base endpoint configuration from resource paths and keep environment differences in configuration.

For non-blocking calls, return the supported async/reactive type and keep the chain non-blocking. Add required custom headers through parameters, annotations, or a header factory as appropriate; do not forward credentials indiscriminately. Convert non-success responses with an exception mapper into domain-relevant failures while preserving useful status/context and closing response resources.

A [3.8 REST-client exception mapper](https://quarkus.io/version/3.8/guides/rest-client-reactive/) must actually be registered for the intended client. Mappers run on an event loop by default; reading a blocking response stream there can raise `BlockingNotAllowedException`. Use the documented `@Blocking` mapper boundary when such I/O is necessary, rather than assuming the remote call's completion makes all response processing safe.

Test against a stub server for success, timeouts, malformed JSON, 4xx/5xx mapping, headers, URI configuration, and async cancellation/failure. Then compose with the fault-tolerance policies from Section 2 without creating unsafe retries.

## 11. OpenTelemetry tracing

A trace represents a distributed request; spans represent timed operations and parent-child relationships. Context propagation carries correlation identifiers across process/thread boundaries so downstream spans join the trace. Baggage carries selected application context but is propagated data—not a safe place for secrets or unbounded personal information.

Instrument an inbound REST request, database/service operation, REST-client call, and message send/receive where supported. Inspect trace/span IDs, parentage, names, attributes, events, status, and timing in an exporter/collector. Add manual spans only where automatic instrumentation lacks useful semantic boundaries; excessive spans create cost and noise.

The [3.8 OpenTelemetry guide](https://quarkus.io/version/3.8/guides/opentelemetry/) uses `quarkus.otel.*` settings and W3C trace-context/baggage propagation by default. Match the OTLP exporter protocol and endpoint to the collector; an exposed receiver port alone proves no spans arrived. JDBC tracing additionally requires its instrumentation dependency and `quarkus.datasource.jdbc.telemetry=true`. Do not assume every extension or database call is traced merely because HTTP spans exist.

Async/reactive execution can lose context if code steps outside supported propagation. Write a test/demo that follows one request across services and verifies the chain. Distinguish logs, metrics, and traces: correlation helps them work together, but none substitutes for the others.

> **Related item:** Sampling and telemetry retention control observability cost and privacy. They are important production controls even when the hands-on task focuses on creating and following spans.

## Original runnable REST and persistence example

Start with this small boundary before adding JWT, messaging and remote calls. The [Red Hat 3.8 getting-started guide](https://docs.redhat.com/en/documentation/red_hat_build_of_quarkus/3.8/html-single/getting_started_with_red_hat_build_of_quarkus/index) supplies the BOM/plugin coordinates used here and requires JDK 17 or 21 and Maven 3.8.6 or later. These are pinned practice coordinates, not a claim that 3.8 is the latest product stream. Use the assigned exam environment's supported artifacts when they differ.

Create `pom.xml`:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>study</groupId><artifactId>ex378-notes</artifactId><version>1.0.0</version>
  <properties>
    <maven.compiler.release>17</maven.compiler.release>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <quarkus.platform.group-id>com.redhat.quarkus.platform</quarkus.platform.group-id>
    <quarkus.platform.version>3.8.6.SP3-redhat-00002</quarkus.platform.version>
  </properties>
  <dependencyManagement><dependencies><dependency>
    <groupId>${quarkus.platform.group-id}</groupId><artifactId>quarkus-bom</artifactId>
    <version>${quarkus.platform.version}</version><type>pom</type><scope>import</scope>
  </dependency></dependencies></dependencyManagement>
  <dependencies>
    <dependency><groupId>io.quarkus</groupId><artifactId>quarkus-resteasy-reactive-jackson</artifactId></dependency>
    <dependency><groupId>io.quarkus</groupId><artifactId>quarkus-hibernate-validator</artifactId></dependency>
    <dependency><groupId>io.quarkus</groupId><artifactId>quarkus-hibernate-orm-panache</artifactId></dependency>
    <dependency><groupId>io.quarkus</groupId><artifactId>quarkus-jdbc-h2</artifactId></dependency>
    <dependency><groupId>io.quarkus</groupId><artifactId>quarkus-smallrye-health</artifactId></dependency>
    <dependency><groupId>io.quarkus</groupId><artifactId>quarkus-junit5</artifactId><scope>test</scope></dependency>
    <dependency><groupId>io.rest-assured</groupId><artifactId>rest-assured</artifactId><scope>test</scope></dependency>
  </dependencies>
  <repositories><repository><id>redhat-ga</id><url>https://maven.repository.redhat.com/ga/</url><releases><enabled>true</enabled></releases><snapshots><enabled>false</enabled></snapshots></repository></repositories>
  <pluginRepositories><pluginRepository><id>redhat-ga</id><url>https://maven.repository.redhat.com/ga/</url><releases><enabled>true</enabled></releases><snapshots><enabled>false</enabled></snapshots></pluginRepository></pluginRepositories>
  <build><plugins>
    <plugin><groupId>${quarkus.platform.group-id}</groupId><artifactId>quarkus-maven-plugin</artifactId><version>${quarkus.platform.version}</version><extensions>true</extensions>
      <executions><execution><goals><goal>build</goal><goal>generate-code</goal><goal>generate-code-tests</goal></goals></execution></executions>
    </plugin>
    <plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-compiler-plugin</artifactId><version>3.13.0</version><configuration><parameters>true</parameters></configuration></plugin>
    <plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-surefire-plugin</artifactId><version>3.2.5</version>
      <configuration><systemPropertyVariables><java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager></systemPropertyVariables></configuration>
    </plugin>
  </plugins></build>
</project>
```

Create `src/main/java/study/Note.java`:

```java
package study;

import io.quarkus.hibernate.orm.panache.PanacheEntity;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name = "study_note")
public class Note extends PanacheEntity {
    @Column(nullable = false)
    public String title;
}
```

Create `src/main/java/study/NotesResource.java`:

```java
package study;

import jakarta.transaction.Transactional;
import jakarta.validation.Valid;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.*;
import org.eclipse.microprofile.config.inject.ConfigProperty;

@Path("/notes")
@Consumes(MediaType.APPLICATION_JSON)
@Produces(MediaType.APPLICATION_JSON)
public class NotesResource {
    @ConfigProperty(name = "study.label")
    String label;

    public record Input(@NotBlank String title) {}
    public record Output(Long id, String title, String label) {}

    private Output output(Note note) {
        return new Output(note.id, note.title, label);
    }

    @POST
    @Transactional
    public Response create(@NotNull @Valid Input input, @Context UriInfo uri) {
        Note note = new Note();
        note.title = input.title().trim();
        note.persistAndFlush(); // Flush detects SQL failures here; commit follows later.
        return Response.created(uri.getAbsolutePathBuilder().path(note.id.toString()).build())
                .entity(output(note)).build();
    }

    @GET
    @Path("/{id}")
    public Output get(@PathParam("id") Long id) {
        Note note = Note.findById(id);
        if (note == null) throw new NotFoundException();
        return output(note);
    }

    @PUT
    @Path("/{id}")
    @Transactional
    public Output replace(@PathParam("id") Long id, @NotNull @Valid Input input) {
        Note note = Note.findById(id);
        if (note == null) throw new NotFoundException();
        note.title = input.title().trim(); // Managed entity: dirty checking writes on flush.
        return output(note);
    }

    @DELETE
    @Path("/{id}")
    @Transactional
    public Response delete(@PathParam("id") Long id) {
        if (!Note.deleteById(id)) throw new NotFoundException();
        return Response.noContent().build();
    }
}
```

For tests only, create `src/test/resources/application.properties`:

```properties
quarkus.devservices.enabled=false
quarkus.datasource.db-kind=h2
quarkus.datasource.jdbc.url=jdbc:h2:mem:notes;DB_CLOSE_DELAY=-1
quarkus.hibernate-orm.database.generation=drop-and-create
quarkus.http.host=127.0.0.1
quarkus.http.test-port=0
study.label=classpath-default
%test.study.label=test-profile
```

The in-memory database and `drop-and-create` setting deliberately discard data. Keep them in test resources; they cannot demonstrate persistence across restart. Supply separately managed schema and durable database configuration for the restart lab. The service is intentionally unsecured for isolated local HTTP tests; add the JWT boundary before a shared deployment.

Create `src/test/java/study/NotesBoundaryTest.java`:

```java
package study;

import io.quarkus.test.junit.QuarkusTest;
import io.quarkus.narayana.jta.QuarkusTransaction;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.*;
import static org.junit.jupiter.api.Assertions.*;

@QuarkusTest
class NotesBoundaryTest {
    @BeforeEach
    void reset() { QuarkusTransaction.requiringNew().run(() -> Note.deleteAll()); }

    @Test
    void createThenRead() {
        var created = given().contentType("application/json").body("{\"title\":\"first\"}")
                .post("/notes").then().statusCode(201).body("label", equalTo("test-profile"))
                .extract().response();
        long id = created.jsonPath().getLong("id");
        assertTrue(created.header("Location").endsWith("/notes/" + id));
        given().get("/notes/" + id).then().statusCode(200).body("title", equalTo("first"));
    }

    @Test
    void blankInputDoesNotPersist() {
        given().contentType("application/json").body("{\"title\":\"   \"}")
                .post("/notes").then().statusCode(400);
        assertEquals(0L, Note.count());
    }

    @Test
    void failureAfterFlushStillRollsBack() {
        assertThrows(IllegalStateException.class, () -> QuarkusTransaction.requiringNew().run(() -> {
            Note note = new Note(); note.title = "rollback"; note.persistAndFlush();
            throw new IllegalStateException("controlled failure");
        }));
        assertEquals(0L, Note.count());
    }
}
```

Run `mvn test`. Expand the tests with these observable boundaries:

| Case | Expected evidence |
|---|---|
| Missing/null/blank title or null request body | 400 and no new row |
| Malformed JSON / unsupported content type | 400 / 415 and no new row |
| Missing identifier on GET or PUT | 404; this PUT contract does not create missing rows |
| Valid PUT repeated twice | Same stored title and row count; dirty checking persists the change |
| Invalid PUT | 400; original title remains |
| DELETE existing identifier, then repeat | First 204 with empty body, then 404; final state remains absent |
| Failed transaction after SQL flush | No committed row |
| Test profile configuration | Response contains `test-profile` |
| Readiness endpoint | Aggregate and expected component results; an always-UP toy check alone does not prove a dependency is healthy |

**Local validation, September 28:** the exact public Java example and three public tests, plus an expanded original suite, compiled and passed 18 Quarkus test cases using the pinned Red Hat BOM, Temurin JDK 21 and Maven 3.9.16 on Windows. Tests exercised real loopback HTTP and in-memory H2 transactions, including rollback after flush. An additional simple readiness component was used in the expanded suite. This did not execute JWT, Kafka, remote-client/fault-tolerance, OpenTelemetry collector, OpenShift or durable packaged-restart labs; the eight integrated labs below remain proposed.

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

## Answers to the original knowledge checks

1. The exam baseline is Red Hat Quarkus 3.8. A newer upstream generator may select unavailable APIs or incompatible extension names; start from the supported BOM and inspect the actual environment.
2. Required values must exist for correct operation; optional values represent a meaningful absence; defaults are safe only when absence has a deliberate valid behavior. A missing authentication key should not silently disable validation.
3. For the same resolved key, a higher-ordinal source overrides a lower one. System properties normally outrank environment variables; test profile resolution and any custom ordinal overrides as well.
4. A mapping groups related properties into a typed interface, makes nested structure explicit and reduces scattered string-key lookups. It still needs valid input and an understood source/validation policy.
5. Only when the source is deliberately authoritative over lower sources. A high ordinal can unintentionally defeat operator overrides; write a collision test before choosing it.
6. Retries multiply traffic and may repeat a side effect whose first result was lost. Bound attempts/backoff, identify retryable failures and make effects idempotent before retrying them.
7. Timeout bounds observed completion time; fallback supplies a defined alternative; a breaker stops calls after a failure threshold; a bulkhead limits concurrency. None alone proves the underlying work was canceled or rolled back.
8. Drive failures to open the breaker, verify dependency calls are rejected, advance a controlled recovery window, allow the probe and prove successful calls resume. Assert counts and results rather than relying on elapsed wall-clock guesses alone.
9. A shared database outage could otherwise restart every healthy process and increase load. Liveness should identify local states where restarting is useful; dependency readiness can control traffic separately.
10. Startup gates initialization, liveness guides restart, readiness guides traffic, wellness supplies additional monitoring checks and groups select related checks. Use the correct qualifier package and configured endpoint path.
11. Secrets, whole tokens, personal information and raw internal exception details. Return bounded non-secret diagnostic fields useful for the operator.
12. Counter: completed events; gauge: current queue depth; timer: completed request duration/count; distribution summary: payload sizes; long-task timer: currently running long operations.
13. Each unique tag combination can create a series. Unbounded IDs cause high cardinality, storage/query cost and potential personal-data exposure; use bounded categories.
14. An endpoint exposes measurements. A monitoring system must also scrape/export, store, query and evaluate actionable rules; prove collection with controlled traffic.
15. Validate the trusted signature/key, issuer, required audience, time constraints and applicable token rules before mapping groups/claims to authorization. Decoding alone establishes no trust.
16. 401 indicates missing/invalid authentication; 403 indicates the authenticated identity lacks permission. Confirm the framework configuration and denied-path tests produce the intended boundary.
17. A positive case can pass even when verification or role checks are bypassed. Wrong signature, expiration, issuer/audience and role cases expose distinct failures.
18. POST commonly creates a new effect for each call unless an explicit deduplication contract applies. Repeating PUT to one identifier must leave the same intended resource state; identical response codes are not required for idempotency.
19. For this create contract, return 201, a Location identifying the new resource and the defined representation. Test that following the location reads the stored state.
20. Blocking JDBC occupies the event-loop thread and prevents it from serving other work. Use a worker boundary for blocking persistence or a genuinely reactive persistence API throughout the chain.
21. CDI creates and injects managed components with defined scopes/interceptors and replaceable test collaborators. Constructing them with new can bypass those services.
22. When API fields, validation or versioning differ from storage, or when exposing relationships causes recursion/lazy-loading leaks. A DTO creates an explicit boundary but still needs mapping and validation.
23. Active record puts persistence operations on entity types; repositories put them in separate managed components. Both retain JPA transaction and entity-state rules.
24. The side with the relationship mapping/foreign key owns it; in a typical bidirectional one-to-many it is the child many-to-one side. The other side names that property with mappedBy.
25. Otherwise in-memory collections and the owning foreign-key reference can disagree. Helper methods should maintain both and respect the chosen cascade/orphan contract.
26. Persistence may defer SQL until a query/flush/commit; managed updates use dirty checking and an explicit flush can still roll back. Integration tests must observe committed state and constraint failures.
27. Incoming consumes from its named channel and Outgoing produces to another. A processing method can connect them; connector configuration must use those exact channel names.
28. When metadata, acknowledgment chaining or explicit success/failure control is required. The handler must acknowledge/nack at the correct completion boundary rather than ignoring the returned asynchronous stage.
29. An early ack can advance upstream progress before the effect is durable; a crash after durable work but before offset commit can replay it. Connector acknowledgment and offset commit are separate.
30. Use a stable event identity with a uniqueness/deduplication decision atomic with the business effect, and test replay after failure. An in-memory seen-ID set does not survive restart or coordinate replicas.
31. The document is the machine-readable contract; Swagger UI renders it interactively for exploration. Neither proves runtime authorization, validation or response behavior without tests.
32. Exercise real endpoints and compare media types, statuses and schemas to the declared contract, including denied and malformed requests. Generated happy-path schemas alone miss drift.
33. The remote service address and configured base path/version, resolved per environment. Keep credentials in the appropriate security/header mechanism rather than embedding secrets in a URL.
34. Callers need to distinguish missing resources, authorization errors, throttling and transient failures before retrying or falling back. Preserve bounded context while avoiding secret bodies and closing resources.
35. Calling await/join/get, sleeping, using JDBC or invoking a synchronous dependency in an I/O-thread callback can block the chain. An async return type alone does not relocate those operations.
36. A trace groups the distributed operation; spans are individual operations; the trace ID correlates spans; parent span identifiers establish causal nesting. Distinguish identifiers from the operation names.
37. Baggage propagates selected context across services. It can leak sensitive data and increase overhead; keep it bounded and non-secret, and never trust it as authorization evidence.
38. Unsupported thread/executor boundaries or manual callbacks may drop the active context. Use supported propagation and inspect the actual exported parentage across each boundary.
39. Health answers whether an instance should run/serve, metrics quantify aggregate behavior, logs provide event detail and traces follow request paths. Correlation makes them complementary; one passing health check cannot prove every business operation.
40. Package and start with durable configuration/storage, exercise the whole service, restart it, then repeat positive/negative calls and inspect retained data, security, messaging and telemetry. An in-memory test suite or dev-mode response is insufficient.

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

## Related-item note

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Source map and freshness notes

The EX378 page defines scope and the Red Hat Build of Quarkus 3.8 baseline. Red Hat 3.8 documentation and the archived upstream 3.8 guides control implementation details; DO378 describes the official learning route. Commercial content supplies explanation and practice, not scope.

Volatile: objective text, Red Hat BOM/extension support, documentation availability, APIs, Java/runtime requirements, course version/runtime/access, delivery, price, and schedule. Recheck the official page and build a clean 3.8 project before the final study sprint.

This guide uses only public objective language and original scenarios, labs, and checks. It does not reproduce or solicit recalled exam tasks.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Pick resources that match your Java background, then implement every public objective in one coherent 3.8 project. Estimated time includes selected reading or coding where stated; access and metadata can change.

| Resource | Access | Estimated time |
|---|---|---:|
| EX378 objectives + Red Hat/Quarkus 3.8 docs | Public | 20–40 selected hours |
| Red Hat DO378 | Paid | About 5 training days plus 40–80 hours independent coding |
| Red Hat DO078 | Free account | 2–4 hours estimated plus 5–10 hours coding |
| Red Hat Developer Quarkus learning hub | Public / free account | 3–10 selected hours |
| Pluralsight Quarkus path | Paid | 10 hours listed plus 30–60 hours coding |
| O'Reilly/Manning Quarkus in Action | Paid; page blocked on recheck | 30–60 coding hours estimated; current length unverified |
| Udemy Cloud-native Microservices with Quarkus | Paid; page blocked on recheck | 30–60 coding hours estimated; current runtime unverified |

- **Focused implementation references:** Work through [configuration](https://quarkus.io/version/3.8/guides/config-reference/), [health](https://quarkus.io/version/3.8/guides/smallrye-health/), [Panache](https://quarkus.io/version/3.8/guides/hibernate-orm-panache/), [RESTEasy Reactive](https://quarkus.io/version/3.8/guides/resteasy-reactive/) and [Kafka](https://quarkus.io/version/3.8/guides/kafka/) alongside the original example and failure matrix.
- **Official scope and build:** [Red Hat Build of Quarkus 3.8 getting started](https://docs.redhat.com/en/documentation/red_hat_build_of_quarkus/3.8/html/getting_started_with_red_hat_build_of_quarkus/index) establishes supported project/BOM tooling. The archived [upstream Quarkus 3.8 guides](https://quarkus.io/version/3.8/guides/) provide focused exercises for every major objective; prefer Red Hat-supported coordinates where they differ.
- **Thread-dispatch explanation:** Clement Escoffier’s August 25, 2021 [RESTEasy Reactive: To block or not to block](https://quarkus.io/blog/resteasy-reactive-smart-dispatch/) explains why blocking work and I/O threads must be separated. Corroborate it with the archived 3.8 REST reference; its historical `javax.*` imports and broader transaction examples are not drop-in 3.8 code or proof of atomic database-plus-Kafka effects.
- **Official route:** [DO378 Cloud-native Microservices Development with Quarkus](https://www.redhat.com/en/services/training/red-hat-cloud-native-microservices-development-quarkus-do378) uses Quarkus 3.8 and OpenShift 4.14 and is the closest end-to-end route. Allow about five instructor-led days plus extensive independent coding.
- **Free orientation:** [DO078 Quarkus Technical Overview](https://www.redhat.com/en/services/training/do078-quarkus-technical-overview) covers project generation, REST, JDBC/Panache, health, OpenAPI, containers/native builds and OpenShift. The [Red Hat Developer Quarkus learning hub](https://developers.redhat.com/learn/quarkus) collects learning paths and interactive tutorials; select 3–10 relevant hours, and do not treat it as a fixed 3.8 exam map.
- **Current broad video/labs:** [Pluralsight Quarkus path](https://www.pluralsight.com/paths/quarkus) lists four courses, three guided labs and ten hours, with 2025–2026 REST, persistence, reactive and event-driven content. Map security, configuration details, all observability types and 3.8 APIs explicitly.
- **Detailed book:** [O'Reilly/Manning Quarkus in Action](https://www.oreilly.com/library/view/quarkus-in-action/9781633438958/) previously supplied broad configuration, REST, security, persistence, messaging and observability coverage. Its page blocked automated access on September 28; the inherited publication date, page count and runtime were not reverified. Check the edition and backport applicable examples to 3.8.
- **Current commercial course:** [Udemy / Ansgar Schulte Cloud-native Microservices with Quarkus](https://www.udemy.com/course/quarkus-by-example/) blocked automated access on September 28. Previously recorded runtime, lecture count and update date were not reverified. Inspect the accessible syllabus and use relevant sections only after a 3.8 API check.

No exact current EX378 MeasureUp, Whizlabs, official practice test, or complete certification-specific O'Reilly/Pluralsight route was independently verified September 28. Avoid “certified questions,” real/recalled tasks, and answer banks; this is a coding exam. Plan **140–240 hours** with strong modern Java/Jakarta experience, or **300–500 hours** if CDI, JPA, reactive programming, messaging, security, and observability are new.
