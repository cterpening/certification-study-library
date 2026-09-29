# EX378 deep review — September 28, 2026

Same-context AI review; independent human review pending. [Study guide](../../guides/EX378-red-hat-certified-specialist-cloud-native-development.md).

## Complete scope and monitoring repair

Read all 64 current [public tasks](https://www.redhat.com/en/services/training/ex378-red-hat-certified-specialist-in-cloud-native-developer-exam), in eleven groups with 5/8/8/6/4/9/4/5/3/8/4 tasks. Compared the complete ordered group/task text against EX378V38K in the [official version PDF](https://training-lms.redhat.com/public_content/redhat/training/Red%20Hat%20Certification%20Exam%20Objectives%20by%20Version.pdf); it agrees after punctuation, case, whitespace and ligature normalization. Same-day public PDF bytes were reused from EX280 research; the EX378 sections were separately read and compared. The page and DO378 retain the Red Hat Quarkus 3.8 baseline. Other PDF versions do not establish an assigned appointment or a future change date.

The previous monitor treated any line containing Readiness as an end marker. It stopped before the @Readiness objective and omitted most tasks. Changed extraction to recognize a complete section-heading line, with a regression test covering both documented terminal headings and later objectives. Live read-only checks for EX200, EX280, EX294 and EX267 retain their previous objective and lifecycle hashes.

After this source review, explicitly accepted the complete EX378 objective baseline: old hash `68272e22e491f3168f3e9c1eaf2520a0be7b132212234e221135205fc9e9ec1a`, new hash `32e199f02055ec50b3c82c71f5abcfa09a1f7d598c97c552656ef37623cda239`. The lifecycle hash remains unchanged. The byte-identical earlier snapshot is archived; historical review and audit dates, hashes and conclusions are preserved, with their source paths redirected to that archive. The receipt preserves the initial observation, corrected observation, acceptance and four-guide regression comparison. This is a parser correction, not evidence that Red Hat just announced a scope change.

## Teaching and original implementation

Added all 40 answers and a complete original Maven/Java REST/Panache example with HTTP boundary tests. The [full Red Hat 3.8 build guide](https://docs.redhat.com/en/documentation/red_hat_build_of_quarkus/3.8/html-single/getting_started_with_red_hat_build_of_quarkus/index) supplies the pinned BOM/plugin coordinates. JDK 17 or 21 and Maven 3.8.6+ are the documented build prerequisites; local execution used the versions recorded below.

Added the [configuration ordinal/profile](https://quarkus.io/version/3.8/guides/config-reference/) table and collision examples; [health](https://quarkus.io/version/3.8/guides/smallrye-health/) qualifiers/endpoints and wellness boundaries; [fault-tolerance](https://quarkus.io/version/3.8/guides/smallrye-fault-tolerance/) overrides and SmallRye async mode; [Micrometer](https://quarkus.io/version/3.8/guides/telemetry-micrometer/) gauge retention; [JWT](https://quarkus.io/version/3.8/guides/security-jwt/) verification and clock-skew testing; [REST](https://quarkus.io/version/3.8/guides/resteasy-reactive/) dispatch and [Panache](https://quarkus.io/version/3.8/guides/hibernate-orm-panache/) dirty checking/flush/rollback.

The [Kafka](https://quarkus.io/version/3.8/guides/kafka/) failure matrix separates acknowledgment, offset commit and database durability. Additional [OpenAPI](https://quarkus.io/version/3.8/guides/openapi-swaggerui/), [REST-client mapper](https://quarkus.io/version/3.8/guides/rest-client-reactive/) and [OpenTelemetry](https://quarkus.io/version/3.8/guides/opentelemetry/) notes cover build-time UI inclusion, blocking response processing and actual exporter/instrumentation requirements. Reading these references does not claim their complete integrated lab execution.

## Blog and catalog

Clement Escoffier's August 25, 2021 [RESTEasy Reactive dispatch article](https://quarkus.io/blog/resteasy-reactive-smart-dispatch/) is useful historical explanation, corroborated with the 3.8 reference. Do not copy its old javax imports or infer an atomic relational-database/Kafka transaction. No blog/plugin skill was invoked.

DO378 still lists Quarkus 3.8/OpenShift 4.14. The Pluralsight path lists four courses, three labs and ten hours. OReilly and Udemy blocked automated rechecking; inherited runtime, count and date claims are marked unverified. The final guide section remains Places to learn.

## Actual validation and limits

Executed **18 passing local Quarkus test cases**, including the exact three public tests plus expanded malformed/null/blank input, HTTP status/location, missing resource, repeated update/delete, unchanged state after rejected update, test-profile resolution, health and failed-after-flush rollback cases. Tests compile the original Java source against the Red Hat 3.8.6.SP3-redhat-00002 BOM using a checksummed workspace-local Temurin JDK and Maven. H2 is in memory, Dev Services are disabled and HTTP test listeners bind loopback on a dynamic port. Maven's first attempt failed on a repository 502. An expanded private test fixture then failed compilation because its generated JSON strings were incorrectly escaped; this was corrected before all tests passed. The attempt logs are retained locally.

No JWT, Kafka broker, remote-client/resilience, telemetry collector, OpenShift or durable package/restart lab ran. The always-UP original readiness component is an endpoint-shape test; it does not prove a real dependency is healthy. These local tests cover parts of the integrated lab ideas, not completion of all eight labs or execution in the assigned RHEL environment. The operational receipt records source/artifact hashes and repository/unit/site/catalog/diff gates after execution.
