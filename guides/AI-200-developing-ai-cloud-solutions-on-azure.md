---
exam_code: AI-200
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-08-31
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-31
---

# AI-200 Developing AI Cloud Solutions on Azure Study Guide

> **Independent AI-assisted resource — SOURCE-VALIDATED.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on August 31, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [source-validation record](../docs/SOURCE-VALIDATION.md). The [official AI-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200) is authoritative.

**Current baseline:** The official page was last updated May 5, 2026; it does not publish a separate “skills measured as of” date.<br>
**Upcoming blueprint change:** None announced as of August 31, 2026.<br>
**Lifecycle status:** Active; no retirement or replacement was announced on the official pages checked.<br>
**Exam page:** [Azure AI Cloud Developer Associate](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-cloud-developer-associate/) · 120-minute assessment · English only on the page checked.<br>
**Official course:** [AI-200T00 Develop AI cloud solutions on Azure](https://learn.microsoft.com/en-us/training/courses/ai-200t00) · five instructor-led days.<br>
**Practice:** Microsoft says a Practice Assessment is not currently available and is normally added within eight weeks after an exam becomes generally available. Recheck the credential page; use the [exam sandbox](https://aka.ms/examdemo) only for interface familiarity.

## How to use this guide

AI-200 is the production back end around an AI workload. Trace every implementation through these chains:

```text
commit -> image digest -> registry -> revision/deployment -> identity/config -> request -> trace
source -> embedding model/version -> vector store/index -> filtered retrieval -> grounded response
command -> queue/topic -> lock/checkpoint -> idempotent worker -> result -> dead-letter/recovery
event -> Event Grid filter -> retry/dead-letter -> function -> downstream state -> correlation
symptom -> trace ID -> application/container/data/message telemetry -> cause -> correction -> proof
```

Use Python for SDK exercises and keep IaC/manifests/configuration in source control. For each lab retain image digest, deployment/revision, environment/cluster configuration, principal and role assignments, data partition/index/vector schema, messaging identifiers and delivery count, trace/correlation ID, KQL query, latency/error/backlog/cost evidence, failure injection, recovery and cleanup. Current service tiers, SDKs, vector algorithms, region support, limits, retirements and preview features change; recheck linked documentation before implementing or booking.

> **About related items:** A `Related item:` callout adds prerequisite, architectural, migration, security, operational, or adjacent context that makes the objective easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in Microsoft's published exam objectives.

## Objective map

| Published domain | Weight | Production question |
|---|---:|---|
| Develop containerized solutions on Azure | 20–25% | Can you build an immutable image and run, scale, revise and diagnose it on the appropriate Azure host? |
| Develop AI solutions by using Azure data management services | 25–30% | Can you choose and implement Cosmos DB, PostgreSQL/pgvector or Managed Redis from data, vector and latency requirements? |
| Connect to and consume Azure services | 20–25% | Can you build idempotent asynchronous flows with Service Bus, Event Grid and Functions? |
| Secure, monitor, troubleshoot Azure solutions | 20–25% | Can the workload use passwordless secrets/config and produce end-to-end OpenTelemetry/KQL evidence? |

---

# 1. Build the operating model

## Separate model capability from cloud application capability

AI-103 focuses on building AI apps and agents; AI-200 emphasizes the cloud back-end components that host, feed, connect, secure and operate them. A model call alone is not an AI cloud solution. Define:

- user/API and async workload SLOs, concurrency, payload and failure behavior;
- image supply chain, host/orchestrator, networking, identity and configuration;
- transactional/state/cache/vector stores and source-of-truth ownership;
- message/event contracts, idempotency and replay/dead-letter path;
- model/embedding dependency, rate limits, latency, safety and cost;
- trace/metric/log correlation and owned operational response.

Use an evidence-first loop: state requirement, choose service/configuration, deploy immutable code, test positive/negative/failure paths, observe, correct, compare and retain proof.

## Choose the compute boundary deliberately

| Host | Strong fit | You operate | Key AI-workload concern |
|---|---|---|---|
| App Service custom container | web/API with simple managed platform and deployment slots | app/image/config/scale; platform manages host | startup/health, port, persistent storage, registry pull, scale plan |
| Azure Container Apps | serverless containers, HTTP/event scale, revisions and jobs | container/revision/scaling/rules; managed environment | KEDA event metadata/auth, scale-to-zero, revision traffic and connection pools |
| AKS | Kubernetes control, complex networking/scheduling, custom operators/GPU and portability | cluster/node pools/manifests/add-ons/upgrades plus workloads | pod/node autoscaling, probes, secrets, workload identity, GPU/capacity, cluster operations |
| Azure Functions | event/HTTP serverless code with bindings | function code/config/plan; platform runtime | trigger delivery, timeout/concurrency, cold start, retry/idempotency |

Container Instances appears in broader Azure documentation but is not a published AI-200 hosting objective. Know it as a simple container primitive, not a substitute for studying the listed App Service, Container Apps and AKS behaviors.

> **Related item:** Horizontal application replicas do not remove a downstream bottleneck. Scale model quota, database RU/connections, Redis memory/operations and message consumers as one system, with backpressure.

---

# 2. Develop containerized solutions on Azure (20–25%)

## Build an image as an immutable supply-chain artifact

Use a multi-stage Dockerfile, small supported base image, pinned dependencies, nonroot user, explicit port/entry point, deterministic build context and `.dockerignore`. Do not put secrets or environment-specific endpoints in an image layer. Add application health endpoints that distinguish process liveness from dependency readiness.

```dockerfile
FROM python:3.12-slim AS runtime
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
RUN useradd --uid 10001 --create-home appuser
USER 10001
ENV PORT=8000
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
```

Tag human-readable releases but deploy by immutable digest where practical. Record source commit, build identity, base/dependency versions, scan/signature/SBOM and image digest. A mutable `latest` tag cannot prove what is running.

## Store and manage images with Azure Container Registry

An ACR registry contains repositories; manifests/tags reference content-addressed layers. Configure SKU/region, network access, encryption/retention/soft-delete policy where supported, diagnostic logs and least-privileged pull/push roles. Use managed identity/workload identity for Azure hosts. The [ACR overview](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-intro) and [authentication guidance](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication) distinguish identity choices.

Operational tasks:

- build/login/push/pull/import and list repository/tag/manifest;
- grant pull to the runtime identity and push/build only to automation;
- scan and block deployment by policy where required;
- replicate/cache/import according to network and regional needs;
- protect delete/untag operations and define retention for untagged manifests;
- diagnose DNS/network/firewall, authentication/RBAC, architecture and manifest/tag problems.

## Build and run with ACR Tasks

ACR Tasks performs cloud image builds and can run containers/commands. A quick task is one-off; a multi-step task defines a workflow; a task can trigger from source commit, base-image update or schedule. Start with [ACR Tasks overview](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-tasks-overview).

```bash
az acr build --registry "$REGISTRY_NAME" \
  --image ai-api:${GIT_COMMIT} \
  --file Dockerfile .
```

Treat as a conceptual shell example: validate variables and never expose secrets in arguments/logs. Configure task identity, source context/credential, registry/data-plane permissions, platform architecture, timeout and logs. A base-image trigger improves patch flow only if testing/promotion gates prevent an unverified rebuild from entering production.

> **Related item:** Build identity and runtime identity should be separate. The runtime normally needs pull plus downstream access; it should not be able to overwrite its own image repository.

## Deploy a custom container to App Service

App Service pulls a supported Linux/Windows image, starts it and routes requests to the configured listening port. Use the [custom container guide](https://learn.microsoft.com/en-us/azure/app-service/configure-custom-container) and [managed identity image pull](https://learn.microsoft.com/en-us/azure/app-service/configure-custom-container?pivots=container-linux#use-managed-identity-to-pull-image-from-azure-container-registry).

Configure:

- app service plan OS/region/size and scale;
- image registry/repository/tag or digest and pull identity;
- container listening port/startup command only if image defaults are insufficient;
- app settings as environment variables and Key Vault references for secrets;
- health check, Always On/startup time and logs;
- networking/private endpoints/VNet integration and outbound DNS/routes;
- deployment slot, validation and swap where the plan supports it.

App settings are injected at runtime and can restart the app on change. They are configuration, not automatically secret; restrict read access and use Key Vault references for secret values. Avoid writing durable state into the container filesystem. Diagnose in order: image pull, process/start command/port, health/startup, app logs, identity/config and downstream connectivity.

## Deploy and revise Azure Container Apps

A Container Apps **environment** provides a boundary for networking/logging and hosts apps/jobs. An app has immutable revisions; a revision has replica(s). Revision mode controls whether one revision receives all traffic or multiple active revisions split traffic. See [revisions](https://learn.microsoft.com/en-us/azure/container-apps/revisions) and [environment overview](https://learn.microsoft.com/en-us/azure/container-apps/environment).

Define:

- image/digest and registry identity;
- ingress target port, external/internal exposure and transport;
- CPU/memory, min/max replicas and probes;
- environment variables, secrets and secret references;
- managed identity and downstream RBAC;
- revision suffix/labels and single versus multiple revision mode;
- Log Analytics destination, diagnostics and Dapr only where required.

A revision-scope change such as image or resource settings creates a new revision; application-scope settings can affect all revisions. Use labels/traffic weights for blue-green or canary, test the exact revision, shift traffic and retain rollback until evidence is stable.

### Scale with KEDA

Container Apps uses KEDA-compatible scale rules for HTTP, TCP and supported event/custom scalers. Configure the scaler's metric/metadata, authentication through a secret or managed identity where supported, polling/cooldown, min/max replicas and per-replica concurrency/queue target. Read [scale rules](https://learn.microsoft.com/en-us/azure/container-apps/scale-app).

Scale-to-zero is valuable for asynchronous/idle workloads but can add cold-start latency. A queue length target is meaningful only with measured processing time and downstream capacity. Ensure each worker is idempotent because scaling/retries can result in repeated delivery. Monitor desired/actual replicas, activation/scaler errors, backlog age, processing rate and downstream throttle.

## Deploy and manage AKS with manifests

AKS fits when the solution requires Kubernetes APIs/control, node pools/GPU, custom networking/scheduling or a broader cluster platform. Start with [deploy an application to AKS](https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-cli) and [AKS workload identity](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview).

Core manifest objects:

- `Deployment`: desired replicas, selector, pod template, rolling strategy and image;
- `Service`: stable virtual address/load balancing to selected ready pods;
- `ConfigMap`: nonsecret configuration; `Secret` is not secure merely because it is base64;
- `ServiceAccount`: workload identity association;
- `PersistentVolumeClaim`: requested durable storage where workload actually needs it;
- `HorizontalPodAutoscaler`: pod replicas from resource/custom/external metric;
- `Ingress`/Gateway: controlled inbound routing with TLS/policy.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-api
spec:
  replicas: 2
  selector:
    matchLabels: { app: ai-api }
  template:
    metadata:
      labels: { app: ai-api }
    spec:
      serviceAccountName: ai-api
      containers:
        - name: api
          image: contoso.azurecr.io/ai-api@sha256:REPLACE
          ports: [{ containerPort: 8000 }]
          readinessProbe:
            httpGet: { path: /ready, port: 8000 }
          livenessProbe:
            httpGet: { path: /live, port: 8000 }
          resources:
            requests: { cpu: "250m", memory: "512Mi" }
            limits: { memory: "1Gi" }
```

Treat as a template: use a real digest, compatible API versions and validated security context. Readiness removes a pod from service; liveness restarts it; startup protects slow initialization. Do not make liveness depend on a temporarily unavailable model/database and trigger a restart storm.

Separate pod and node scaling. HPA needs useful resource requests/metrics; cluster autoscaler adds/removes nodes for unschedulable demand; KEDA can drive event metrics. Plan max surge/unavailable, disruption budgets, zones, upgrades, quotas and model/GPU scheduling.

## Troubleshoot Container Apps and AKS end to end

Use an outside-in sequence:

1. Resolve hostname/TLS/routing/ingress and confirm request reaches the environment/cluster.
2. Inspect revision/deployment desired versus ready replicas and rollout state.
3. Inspect pod/replica status, restarts, exit code, events, probes and logs.
4. Confirm image pull identity, registry network/DNS and architecture.
5. Confirm config/secret references and workload identity token/role.
6. Test service/endpoints/port selectors and network policy/DNS from inside the workload.
7. Trace database/cache/broker/model dependency and throttling.
8. Compare the failing deployment/revision/digest/config with last known good; rollback and preserve evidence.

Use [Container Apps logs and monitoring](https://learn.microsoft.com/en-us/azure/container-apps/log-monitoring) and [AKS monitoring data](https://learn.microsoft.com/en-us/azure/aks/monitor-aks). `kubectl describe`, `get events`, logs including previous container, rollout status, endpoints and resource pressure often explain the failure before a redeploy does.

> **Related item:** A healthy HTTP endpoint that never exercises authentication or dependencies can route traffic to a broken revision. Readiness should be cheap and stable but meaningful enough to prove the instance can serve.

---

# 3. Develop AI solutions with Azure data management services (25–30%)

## Choose source of truth, retrieval store and cache separately

| Service | Strong fit | Vector role | Primary constraints |
|---|---|---|---|
| Azure Cosmos DB for NoSQL | globally distributed JSON aggregates, partition-key access, change feed and elastic throughput | vectors colocated with documents and filtered by document metadata | partition distribution, RU/index cost, consistency, vector policy/index and limits |
| Azure Database for PostgreSQL Flexible Server | relational integrity/joins/SQL plus extensions | `pgvector` exact/approximate vector search with relational metadata filters | compute/memory/storage/IOPS, connections, vacuum/statistics and index tuning |
| Azure Managed Redis | in-memory low-latency cache/data structures and supported vector index | hot semantic cache/retrieval with Redis Search | memory/eviction/persistence/tier, connection count, index memory and source-of-truth durability |

Do not select by latency alone. Model write/read pattern, scale, durability, transaction/consistency, query/filter, tenancy, recovery, region, operations and cost. A common design uses PostgreSQL or Cosmos DB as durable source, Redis as cache/hot index, and a durable queue for asynchronous embedding updates.

## Implement Cosmos DB for NoSQL access

The Python SDK path is `CosmosClient -> DatabaseProxy -> ContainerProxy`. Prefer managed identity with `DefaultAzureCredential` and Cosmos data-plane RBAC; reuse one client for connection management. See [Python SDK examples](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/how-to-python-get-started).

```python
from azure.cosmos import CosmosClient, PartitionKey
from azure.identity import DefaultAzureCredential

client = CosmosClient(endpoint, credential=DefaultAzureCredential())
container = client.get_database_client("ai").get_container_client("chunks")
item = container.read_item(item="chunk-42", partition_key="tenant-a")
```

Point reads by ID plus full partition key are normally the most efficient lookup. Parameterize queries and include the partition key when known; cross-partition fan-out costs more. Handle `CosmosHttpResponseError` by status/substatus and use SDK retry for documented transient cases without blindly repeating non-idempotent business work.

### Partition, indexing and consistency

Choose a partition key with high cardinality, even storage/request distribution, immutable availability in every item and alignment with common transactional/query scope. A synthetic or hierarchical key can address skew/access requirements when currently supported. Partitioning cannot be changed in place casually.

The default indexing policy indexes properties automatically. Exclude unused/high-cardinality paths or define included paths/composite indexes from measured queries. Vector indexes require vector embedding policy plus path, data type, dimensions and a supported index type. Indexing increases write RU and storage; excluding a query path can force scans or unsupported vector behavior.

Consistency ranges from strong/bounded staleness through session, consistent prefix and eventual. Session is a common balance for a client/session; carry session token when read-your-writes must span client instances. Stronger consistency and multi-region choices affect availability/latency/RU. Use [consistency levels](https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels) and [indexing policies](https://learn.microsoft.com/en-us/azure/cosmos-db/index-policy).

Measure request charge, diagnostics, latency, throttled requests and hot partitions. Reduce RU by point reads, partition predicates, projections, appropriate indexes, smaller documents, bounded page size and batch scope—not by suppressing retry evidence.

## Store embeddings and run Cosmos DB vector search

Define a vector embedding policy on the vector path and a compatible index. Current index choices and limits depend on account/API/feature state; use [vector search in Cosmos DB for NoSQL](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/vector-search).

Store source ID/version/hash, chunk text/metadata, embedding model/version/dimensions and ACL/tenant beside or linked to vector. Generate query and document embeddings with the same model/dimensions. Apply tenant/category/security filters as part of the query design and verify index/filter support.

Cosmos vector distance queries consume RU and return a similarity/distance ordering according to the chosen metric/index. Test exact versus approximate options, candidate count, partition/filter selectivity, recall against labeled questions, p95 latency and RU. Avoid treating a raw score as universal confidence.

> **Related item:** Embeddings inherit the sensitivity and retention duties of their source. A vector is not anonymized simply because humans cannot read it directly.

## Process changes with the Cosmos DB change feed

The change feed records item creates/updates in partition-key order; delete representation depends on mode/design, so tombstones may be required. The change feed processor library distributes lease ownership across host instances and checkpoints progress. See [change feed processor](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/change-feed-processor).

Use a separate lease container, stable processor name and instance names. Make handlers idempotent because delivery can repeat after failure/checkpoint. Persist a derived-state version/source hash so an older embedding result cannot overwrite a newer source. Handle poison items with durable failure/quarantine and alert; checkpoint only after required output is safely committed.

Monitor lease balance, lag/estimated pending work, handler latency/failures, RU throttling and derived-state reconciliation. A processor can be “running” while embeddings remain stale.

## Implement PostgreSQL and pgvector

Azure Database for PostgreSQL Flexible Server provides managed PostgreSQL with configurable compute, storage, HA/network and extensions. Connect with a supported Python driver/SDK path, TLS, Microsoft Entra token or protected credential, and a bounded pool. Use [connect with Python](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/connect-python) and the [service overview](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/overview).

Model relational grain, primary/foreign/unique/check constraints and types first. Normalize where integrity/updates require it; use `jsonb` plus GIN indexes for genuinely variable attributes. Select B-tree key order from equality/range/order predicates; partial/expression/covering indexes can help specific workloads but add write/vacuum/storage cost. Keep statistics current and inspect `EXPLAIN (ANALYZE, BUFFERS)`.

### Store and index vectors with pgvector

Enable the approved `vector` extension, define matching dimensions and load compatible embeddings. The Azure [pgvector guidance](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/how-to-use-pgvector) documents current enablement and examples.

```sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE chunk (
    chunk_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    tenant_id uuid NOT NULL,
    content text NOT NULL,
    embedding vector(1536) NOT NULL,
    source_version text NOT NULL
);

CREATE INDEX chunk_embedding_hnsw
ON chunk USING hnsw (embedding vector_cosine_ops);

SELECT chunk_id, content,
       embedding <=> $1::vector AS cosine_distance
FROM chunk
WHERE tenant_id = $2
ORDER BY embedding <=> $1::vector
LIMIT $3;
```

Treat dimensions/model as examples. Understand operators for Euclidean, inner product and cosine distance and choose the operator class to match. Exact scan gives ground truth. IVFFlat needs training/data/list/probe tuning; HNSW offers a different build/memory/recall/write tradeoff. Current extension/index support changes—verify exact service version.

Metadata filters can reduce vector candidates but interact with ANN. Use suitable relational indexes, current iterative-scan/filter capabilities, partitioning or bounded tenant design, and measure filtered recall. Hybrid retrieval can combine PostgreSQL full-text rank and vector rank using RRF.

### Size compute, memory, storage and connections

- CPU handles query/embedding-distance work and concurrency; memory supports shared buffers, connection/work memory and HNSW build/search.
- Storage size/type/IOPS/throughput and WAL/vacuum behavior affect latency and index build.
- Too many client connections consume memory and scheduling. Reuse bounded application pools; use PgBouncer where supported and compatible.
- Tune `work_mem` per operation/concurrency, not globally to one large value; monitor spills.
- Maintain autovacuum/analyze so dead tuples and stale statistics do not destroy vector/relational performance.

Use [server parameters](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-server-parameters) and [PgBouncer](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-pgbouncer). Load test representative vector counts, filters and concurrent application behavior; compare CPU, memory, disk latency/IOPS, connections, plans, recall and p95.

## Integrate Azure Managed Redis

Azure Managed Redis is Microsoft's current fully managed Redis offering with Redis Stack capabilities. Use the [Azure Managed Redis overview](https://learn.microsoft.com/en-us/azure/redis/overview) and current [Python client connection guidance](https://learn.microsoft.com/en-us/azure/redis/python-get-started).

**Current transition:** Azure Cache for Redis SKUs are on a published retirement path. Enterprise and Enterprise Flash have a March 31, 2027 migration deadline; Basic, Standard and Premium retire September 30, 2028. On the August 2026 update, new customers had been blocked from creating the latter tiers since April 1, 2026, while qualifying existing customers could continue until retirement. New designs should use/evaluate Azure Managed Redis, and existing deployments should follow Microsoft's [Azure Cache for Redis retirement FAQ](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/retirement-faq). Do not copy old tier, authentication or migration instructions into a new Managed Redis design without checking.

### Data operations and caching

Choose data structure from operation: strings for value/cache, hashes for fields, sets/sorted sets for membership/rank, streams for durable-ish ordered processing patterns and pub/sub for ephemeral notification. Use key namespaces and tenant boundaries.

For cache-aside:

1. request cache key; on hit deserialize/validate version;
2. on miss read source of truth;
3. populate with bounded TTL/jitter and return;
4. on authoritative update invalidate or version the key;
5. prevent stampede with single-flight/lock/stale-while-revalidate where required.

Expiration limits staleness; eviction occurs because of memory policy/pressure. Neither guarantees source consistency. Choose max-memory/eviction and persistence/HA from loss tolerance. Reuse a thread-safe connection/pool, set timeouts, backoff only transient failures and fall back to durable source where acceptable. Monitor memory fragmentation/usage, evictions, expirations, operations/latency, connections, CPU and server load.

### Vector indexing

Redis Search can index vector fields with current algorithms such as FLAT or HNSW and combine KNN/vector search with metadata filters. Define data representation (hash/JSON), dimensions, numeric type, distance metric, index schema and key prefix. Use the [vector search concepts](https://learn.microsoft.com/en-us/azure/redis/overview#vector-search) plus current Redis command documentation linked by the service docs.

FLAT provides exact/brute-force behavior and lower index complexity; HNSW trades memory/build/update cost for approximate latency at scale. Measure recall against exact ground truth, p95, memory/index size, writes and filtering. Redis should not silently become the only durable copy unless the chosen persistence/HA/recovery design meets the requirement.

> **Related item:** A semantic cache needs a correctness policy. Similar prompts may require different answers because tenant, authorization, conversation, model/prompt version or source freshness differs; include those dimensions in the key/validation boundary.

---

# 4. Connect to and consume Azure services (20–25%)

## Distinguish commands/messages from events

| Need | Azure Service Bus | Azure Event Grid |
|---|---|---|
| Intent | deliver work/command or enterprise message to a receiver | notify subscribers that a discrete event happened |
| Delivery model | brokered queue; topics and subscriptions; peek-lock/settlement | push/pull delivery to handlers; event subscriptions and filters |
| State features | lock, delivery count, DLQ, sessions, duplicate detection, transactions/scheduling by tier/capability | retry policy, dead-letter destination, CloudEvents/Event Grid schema, filters |
| Backpressure | queue buffers work; competing consumers | destination retry/expiration; use broker/queue when long buffering/work control is required |
| Common AI use | embedding/inference jobs, ordered conversation/session work | blob/document-created notification, resource/business state event |

An event may trigger code that sends a Service Bus command for durable processing. Do not use Event Grid as a work queue merely because both are asynchronous.

## Queue back-end work with Service Bus

Use the [Service Bus messaging overview](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview) and the current [Python SDK quickstart](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-python-how-to-use-queues). Prefer passwordless `DefaultAzureCredential`/managed identity and sender/receiver data roles.

### Queue, topic and subscription design

- A queue provides competing-consumer delivery to one logical receiver group.
- A topic copies each message to matching subscriptions; each subscription behaves like a virtual queue and can filter/actions.
- Sessions group related messages for ordered, stateful processing when supported and correctly keyed.
- Duplicate detection uses message ID within a configured window; it does not replace consumer idempotency.
- Scheduled delivery delays availability; TTL controls expiry, not processing timeout.

Define an envelope with stable message/business/idempotency ID, type/schema version, correlation/trace context, tenant, occurred/enqueued time, payload reference and retry-relevant metadata. Keep large documents/prompts in protected storage and send a reference when message-size or sensitivity argues against inline data.

### Receive, settle and retry correctly

Peek-lock receive grants a temporary lock. Complete after durable success; abandon to make available; dead-letter when no automatic retry should continue; defer for an explicitly retrievable out-of-order dependency. Auto-lock renewal only buys time—it does not make a non-idempotent handler safe.

```python
from azure.identity.aio import DefaultAzureCredential
from azure.servicebus.aio import ServiceBusClient

credential = DefaultAzureCredential()
client = ServiceBusClient(namespace, credential)
async with client:
    receiver = client.get_queue_receiver(queue_name="embedding-work", max_wait_time=5)
    async with receiver:
        async for message in receiver:
            try:
                await process_idempotently(str(message.message_id), message)
                await receiver.complete_message(message)
            except PermanentContractError as exc:
                await receiver.dead_letter_message(message, reason="Contract", error_description=str(exc)[:1024])
            except Exception:
                await receiver.abandon_message(message)
```

Treat as a pattern: classify SDK exceptions, close credential/client, bound concurrency, renew locks and avoid sensitive error text. If processing exceeds practical lock time, split/stage the operation. Persist idempotency result before completion. Monitor active/dead-letter count, oldest age, incoming/completed/abandoned/dead-letter rate, delivery count, lock lost, throttling and handler latency.

### Operate the dead-letter queue

Messages dead-letter after configured max delivery, explicit rejection, expiry/dead-letter behavior or filter/session errors. The DLQ does not clean itself. Follow [dead-letter queues](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues).

Build an owned workflow: alert, inspect without exposing payload, classify code/config/data/dependency failure, fix, replay through a controlled path with original identity/correlation, verify result, then settle. Blindly resubmitting a poison message creates a loop.

> **Related item:** Retry count is not the same as attempt identity. A message can be redelivered after the external model succeeded but before settlement; the handler needs a stable operation key and result state.

## Implement Event Grid workflows

Event Grid routes events from system/custom/partner sources through topics/namespaces and event subscriptions to handlers. Use [Event Grid concepts](https://learn.microsoft.com/en-us/azure/event-grid/concepts) and [custom events](https://learn.microsoft.com/en-us/azure/event-grid/custom-event-quickstart).

Design the event contract with stable event ID, source, type, subject, time, schema version and minimal data/reference. Prefer CloudEvents where interoperability fits. Publishers state facts, not subscriber-specific commands.

### Filter deliberately

Subject-begins/ends filters route hierarchical names; event-type filters choose semantic types; advanced filters inspect supported data fields/operators. Filtering reduces noise and handler cost but creates a silent-loss risk if subject/schema changes. Test accepted and rejected samples and monitor publisher versus matched/delivered counts.

### Retry and dead-letter

Event Grid retries eligible delivery failures with exponential backoff until TTL/attempt limits; some response codes can stop retry sooner. Configure a storage dead-letter destination and grant Event Grid's identity required access. Read [delivery and retry](https://learn.microsoft.com/en-us/azure/event-grid/delivery-and-retry).

Handlers should authenticate/validate source, return promptly, be idempotent by event ID/business version and offload long work to a queue. Dead-letter storage needs alert, retention, access control and replay tooling. Event ordering is not generally guaranteed; use source version/sequence and convergence.

## Build serverless APIs and workers with Azure Functions

Functions execute code from HTTP, timer, queue, Service Bus, Event Grid and other triggers; input/output bindings reduce connection boilerplate. Use the current Python programming model and [Functions Python developer guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python).

```python
import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="health", methods=["GET"])
def health(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("ok")
```

Function keys are not a complete end-user authorization architecture. Use App Service authentication/Microsoft Entra, API Management or application authorization as required; use managed identity for resources.

### Trigger and binding semantics

- The trigger controls invocation and retry/checkpoint behavior; a binding maps approved input/output without eliminating SDK needs for advanced behavior.
- Separate host configuration (`host.json`), local development secrets (`local.settings.json`, never commit) and Azure app settings/Key Vault references.
- Reuse SDK/HTTP clients outside invocation where safe. Bound concurrency to database/model quotas.
- Return HTTP response within client/gateway timeout; queue long inference/embedding work and expose status/result.
- Make message/event functions idempotent and poison-aware. Understand plan/runtime timeout and scale behavior.

Deploy with a repeatable package or container and compatible Python/runtime/extension versions. Configure plan, storage, identity, networking, app settings, telemetry and slots where supported. Use [deployment technologies](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies) and [Functions best practices](https://learn.microsoft.com/en-us/azure/azure-functions/functions-best-practices).

> **Related item:** Durable Functions can orchestrate long-running stateful workflows, but it is supporting knowledge rather than an explicit AI-200 objective. Its orchestrator determinism and replay model differ from an ordinary function.

---

# 5. Secure, monitor, and troubleshoot Azure solutions (20–25%)

## Use workload identity before application secrets

For each deployed workload:

1. assign system- or user-assigned managed identity, or AKS workload identity;
2. grant the smallest data-plane role at the narrowest resource scope;
3. use `DefaultAzureCredential` in Azure and an approved developer identity locally;
4. restrict network paths/private endpoints and DNS where requirements demand;
5. test the permitted action and a neighboring denied action;
6. audit role changes and resource access.

Do not confuse management-plane Contributor with data access. A role that creates a Cosmos account, registry or Key Vault may not read its data, and vice versa.

## Retrieve and rotate secrets with Key Vault

Key Vault protects secrets, keys and certificates with Microsoft Entra authentication, Azure RBAC/access policy model, versioning and audit. Prefer managed identity plus RBAC. Use [Key Vault secrets quickstart for Python](https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python) and [Key Vault security guidance](https://learn.microsoft.com/en-us/azure/key-vault/general/security-features).

```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

client = SecretClient(vault_url=vault_url, credential=DefaultAzureCredential())
secret_value = client.get_secret("legacy-api-token").value
```

Retrieve only when no passwordless/identity mechanism exists. Never log/cache indefinitely or expose the value through environment dumps/errors. Cache briefly with a rotation-aware policy rather than calling Key Vault per request; handle throttling/outage according to availability and revocation requirements.

### Rotation

Define producer, consumer and revocation sequence. For dual-credential services: create new, store new Key Vault version, update/reload consumers, verify, then revoke old. Event Grid can react to Key Vault near-expiry events and an Automation/Function workflow can rotate supported targets, but the workflow's identity and failure path are highly privileged. Read [secret rotation guidance](https://learn.microsoft.com/en-us/azure/key-vault/secrets/tutorial-rotation).

Enable soft delete and purge protection according to policy; separate vaults/boundaries by environment and blast radius; restrict network/data-plane administration; alert on failures/near expiry and test recovery.

## Centralize nonsecret configuration with App Configuration

Azure App Configuration stores versioned key-values, labels, feature flags, snapshots and references; it is not a general secret store. Use labels for environment/ring/version, key prefixes for application/domain and Key Vault references for secret indirection. Start with the [Python quickstart](https://learn.microsoft.com/en-us/azure/azure-app-configuration/quickstart-python-provider).

The provider can load/select/trim prefixes and refresh configuration. Register sentinel/key refresh and ensure request/background refresh semantics meet freshness. Feature flags need owner, targeting, expiry and fallback; stale cache behavior must be explicit when App Configuration is unavailable. Use managed identity/data-reader role and private networking where required.

> **Related item:** A feature flag can change production behavior without an image deployment. Treat flag permission, review, audit, telemetry and rollback as part of the release control plane.

## Instrument with OpenTelemetry

OpenTelemetry supplies vendor-neutral traces, metrics and logs/signals through SDK/provider/exporter. Azure Monitor's OpenTelemetry distribution exports supported telemetry to Application Insights. Use [Azure Monitor OpenTelemetry overview](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-overview).

Instrument spans across HTTP ingress, Service Bus/Event Grid/Functions, database/Redis and model calls. Propagate W3C trace context through message application properties/event metadata; preserve correlation even if processing occurs minutes later.

Record safe attributes:

- deployment/revision/image/commit, operation and tenant pseudonymous ID;
- broker entity, message/event type and delivery count—not secret payload;
- data service operation, partition/query identifier, RU/latency/connection outcome;
- embedding/completion model deployment/version, token/latency/status and retrieval result count;
- cache hit/miss, queue/backlog age and end-to-end duration.

Avoid prompt/document/secret/PII bodies by default. Configure sampling so errors and critical async flows remain diagnosable; understand head versus tail sampling and cross-service consistency. Metrics need stable, low-cardinality dimensions. Logs need structured fields and trace IDs.

## Query telemetry with KQL

Kusto Query Language filters, projects, parses, summarizes and joins time-series log tables. The exact table names vary between Application Insights classic/workspace schema and resource-specific diagnostic tables. Use the [KQL overview](https://learn.microsoft.com/en-us/kusto/query/?view=microsoft-fabric) and [Application Insights data model](https://learn.microsoft.com/en-us/azure/azure-monitor/app/data-model-complete).

```kusto
requests
| where timestamp > ago(1h)
| summarize Requests=count(), Failures=countif(success == false),
            P95=percentile(duration, 95) by cloud_RoleName, bin(timestamp, 5m)
| order by timestamp asc
```

```kusto
dependencies
| where timestamp > ago(1h)
| where type in ("Azure Service Bus", "Azure DocumentDB", "Redis", "HTTP")
| summarize Count=count(), Failures=countif(success == false),
            P95=percentile(duration, 95) by type, target
```

Validate column/table names in the actual workspace. Use `where` early, narrow time range, `project` required fields, `summarize` with sensible bins and guarded joins. Build queries for user symptoms (availability/p95), saturation/backlog, dependency failure/throttle, deployment comparison and data freshness—not just resource CPU.

## Troubleshoot through one trace and one resource path

1. Confirm impact, operation, tenant, deployment/revision/digest and time window.
2. Find failed/slow request or async correlation/trace ID.
3. Follow service map/spans through container/function, broker, data/cache and model endpoint.
4. Check platform events/logs: image/probe/restart/scale, broker delivery/DLQ, RU/connection/throttle, Key Vault/App Config denial, model quota.
5. Compare last known good release/config/flag and regional/service health.
6. Mitigate safely: rollback revision/image/flag, shed/load-buffer, scale within downstream capacity, or fail over according to tested plan.
7. Correct root cause and replay only idempotent work; reconcile durable source, message state, embeddings/cache and user result.
8. Prove p95/error/backlog/freshness recovery and document prevention.

> **Related item:** A trace can show a successful call but not prove a correct business result. Pair technical telemetry with reconciliation and quality signals such as embedding coverage, retrieved-authorized result count and citation validity.

---

# 6. Integrated design scenarios

## Scenario A: asynchronous document ingestion and RAG API

**Requirements:** uploaded documents searchable within ten minutes, tenant isolation, burst handling, 99.9% API SLO and source deletion propagation.

1. Blob-created Event Grid event filters approved containers/extensions and invokes a small Function that validates contract and sends a Service Bus work message.
2. Container Apps workers scale on queue backlog through KEDA; a managed identity reads the document, chunks/embeds it and writes Cosmos DB vectors with tenant/source hash/model version.
3. Worker uses stable source-version idempotency, tombstones/deletes, DLQ for permanent content and completes only after durable output.
4. API runs on Container Apps revisions, authenticates user, applies tenant metadata filter before vector retrieval and calls approved model outside a database transaction.
5. Key Vault holds only unavoidable external secret; App Configuration supplies model deployment, feature flag and retrieval settings.
6. OpenTelemetry correlates event, message, worker, Cosmos RU/vector query and model call. Alert on oldest queue age, embedding reconciliation gap, p95 and denied-access anomalies.

**Failure trap:** Event Grid delivery success only proves the Function accepted the event, not that the document became searchable. Monitor the full event-to-index freshness SLO and reconcile source versions.

## Scenario B: relational catalog with low-latency semantic cache

**Requirements:** relational product truth, vector/metadata filtering, popular query responses under 100 ms, controlled staleness and no cross-tenant cache reuse.

1. PostgreSQL stores products/chunks/vectors with constraints, tenant and source/model version. HNSW is selected only after ENN recall/latency baseline.
2. App Service custom container uses managed identity, bounded PostgreSQL pool and parameterized queries; deploy by digest through a validated slot.
3. Azure Managed Redis cache key includes tenant, normalized query hash, model/prompt/index/source version; TTL jitter and invalidation control freshness.
4. A PostgreSQL/outbox publisher sends product-change commands through Service Bus; worker re-embeds and invalidates affected keys idempotently.
5. Trace spans expose pool wait, PostgreSQL plan/latency, Redis hit/miss and model call. Load test database/Redis/model together.

**Failure trap:** increasing app replicas exhausts PostgreSQL connections and increases latency. Bound per-instance pools and scale database/PgBouncer plus workers as a system.

## Scenario C: AKS batch inference platform

**Requirements:** GPU/custom scheduling, queue-based jobs, rolling upgrades, long model processing, replayable failure and cost control.

1. AKS uses separate system and GPU node pools, workload identity, ACR pull identity, requests/limits, taints/tolerations and meaningful startup/readiness/liveness.
2. Service Bus sessions preserve per-job ordering if required; consumers lock/renew, checkpoint durable output and complete with idempotency.
3. KEDA/HPA scale pods on backlog; cluster autoscaler supplies nodes within quota. Backlog target incorporates processing duration/model quota.
4. Deployment uses digest, rolling strategy and disruption budget; canary jobs compare output/latency/cost before full rollout.
5. OpenTelemetry and AKS/container/broker metrics correlate job ID, pod/node, model version, delivery and GPU/resource utilization.

**Failure trap:** liveness tied to a slow model dependency restarts every pod during a provider outage, losing work and amplifying load. Keep liveness local; expose dependency readiness separately and buffer/back off.

---

# 7. Hands-on labs

Use an isolated subscription/resource group, synthetic data and budgets. Retain source, manifests/IaC, image digest, identities/grants, SDK/config, trace/KQL, metrics, failure and cleanup evidence.

## Lab 1: ACR supply chain and App Service container

1. Build a nonroot multi-stage Python API image locally and with ACR Task; tag commit and record digest.
2. Grant App Service managed identity ACR pull; deny push.
3. Supply nonsecret setting and Key Vault reference; deploy by immutable version to a slot.
4. Test health/startup/logs, swap and rollback. Break port, registry role and downstream DNS separately; diagnose each.
5. Compare source commit, SBOM/scan result, digest and running configuration.

## Lab 2: Container Apps revisions and KEDA

1. Deploy API plus Service Bus worker into a Container Apps environment using managed identities.
2. Configure probes, CPU/memory and queue scale rule with min zero/max bound.
3. Create a new revision, apply label/traffic split and compare telemetry; rollback without rebuilding.
4. Generate controlled backlog and measure activation, replicas, oldest age, throughput, downstream throttling and scale-down.
5. Inject poison/repeated message and prove idempotency/DLQ.

## Lab 3: AKS manifest deployment and incident

1. Deploy by digest using Deployment, Service, ConfigMap and workload-identity ServiceAccount.
2. Add startup/readiness/liveness and requests/limits; inspect endpoints and rollout.
3. Configure HPA or KEDA plus cluster autoscaler in a budget-safe range.
4. Break image pull, selector/port, readiness, identity and memory separately; diagnose with events/logs/metrics/trace.
5. Roll forward/back and retain evidence linking commit/digest/pod/revision.

## Lab 4: Cosmos DB vector and change feed

1. Create synthetic multi-tenant chunks and choose/test partition key.
2. Connect through managed identity, implement point read/parameterized query and capture RU/diagnostics.
3. Define embedding policy/vector index, load model-versioned vectors and compare search with metadata/tenant filters.
4. Change indexing/consistency one decision at a time; compare RU/latency and read semantics.
5. Implement change feed processor with leases, repeated delivery, stale-version guard, delete tombstone and reconciliation.

## Lab 5: PostgreSQL pgvector and connection tuning

1. Connect by approved identity/TLS with bounded Python pool; create relational constraints and vector column.
2. Load a labeled corpus; run exact vector query and inspect `EXPLAIN (ANALYZE, BUFFERS)`.
3. Compare HNSW/IVFFlat where supported across build time, memory, writes, filtered recall and p95.
4. Combine full-text and vector ranks with metadata authorization; test selective tenants.
5. Load-test pool sizes and PgBouncer/current server parameters; observe connection, CPU/memory/IO and vacuum/statistics.

## Lab 6: Managed Redis cache and vector index

1. Connect through current secure identity/credential guidance and reusable client pool.
2. Implement cache-aside with TTL jitter, versioned tenant key, invalidation and source fallback.
3. Simulate stampede, eviction, timeout and stale version; measure hit rate/p95/source load.
4. Create FLAT and HNSW vector indexes where supported; compare exact recall, memory and filtered latency.
5. Fail/cache flush according to lab safety and prove the durable source rebuild path.

## Lab 7: Service Bus, Event Grid and Functions

1. Publish filtered custom/Event Grid events with trace/business/version IDs to a Function.
2. Function validates and sends a Service Bus command; worker processes with managed identity and idempotency record.
3. Test queue versus topic/subscription filters, lock expiry/renewal, duplicate, session/order and transient failure.
4. Route permanent message to DLQ; inspect, correct and controlled-replay it.
5. Configure Event Grid retry/dead-letter storage; test handler 5xx, filter rejection and duplicate/out-of-order event.
6. Reconcile published events, matched deliveries, queued/completed/DLQ and durable outputs.

## Lab 8: secrets, configuration and distributed troubleshooting

1. Give workload identity only Key Vault secret read and App Configuration data read; prove neighboring denial.
2. Implement rotation with two versions and consumer refresh; test revoked old credential and vault outage behavior.
3. Add a feature flag/sentinel refresh with safe default and audit.
4. Instrument HTTP, Service Bus, Cosmos/PostgreSQL/Redis and model dependency with OpenTelemetry trace context.
5. Write KQL for p95/error, dependency failure, deployment comparison and async end-to-end duration.
6. Inject one bad revision, throttled store, poison message and stale embedding; diagnose, mitigate, replay/reconcile and prove recovery.

---

# 8. Original knowledge checks

These are original prompts, not recalled exam questions. Answer with requirements, dependencies, implementation, evidence, failure behavior and correction.

1. Choose App Service, Container Apps, AKS or Functions for four AI back-end workloads.
2. Why are a release tag and an immutable image digest both useful, and which proves deployed bytes?
3. Which ACR permissions should build automation and runtime identities receive?
4. Compare quick, multi-step, source-triggered, base-image-triggered and scheduled ACR Tasks.
5. How do App Service app settings, Key Vault references, port/start command, health and slot swap interact?
6. Distinguish Container Apps environment, app, revision, replica, label and traffic weight.
7. Design a KEDA queue scale rule without overwhelming the model/database.
8. Compare readiness, liveness and startup probes; how can a dependency-based liveness probe cause an outage?
9. Distinguish HPA, KEDA and AKS cluster autoscaler.
10. What evidence separates image-pull, port/selector, probe, identity and downstream-network failures?
11. Choose Cosmos DB, PostgreSQL/pgvector or Managed Redis for durable JSON, relational truth and hot cache.
12. Why is ID plus partition-key point read normally cheaper than a Cosmos query?
13. How do partition key, indexing policy, consistency and query shape influence RU and latency?
14. Which embedding/vector policy metadata must agree before Cosmos vector search can be trusted?
15. Why must a change feed processor be idempotent, and how are deletes/stale embedding writes handled?
16. Design PostgreSQL tables/types/constraints/indexes for tenant chunks and vectors.
17. Compare exact pgvector scan, IVFFlat and HNSW for recall/build/memory/write/latency.
18. Why can an ANN query with a selective metadata filter return too few relevant results?
19. How do pool size, PgBouncer, work memory, storage IOPS and autovacuum affect vector workload throughput?
20. Explain cache-aside, expiration, invalidation, eviction and stampede as different concerns.
21. When is Redis vector search appropriate, and why might Redis remain a rebuildable serving layer?
22. How does Azure Cache for Redis retirement affect a new AI-200 design?
23. Compare a Service Bus queue with a topic/subscription and Event Grid event subscription.
24. Explain peek-lock complete, abandon, dead-letter and defer. When can work repeat after success?
25. What belongs in a message/event envelope for idempotency, versioning and trace propagation?
26. Design an owned DLQ repair/replay workflow that cannot loop indefinitely.
27. How do Event Grid subject/event-type/advanced filters reduce cost and create schema risk?
28. Which Event Grid failures retry or dead-letter, and why should a long handler enqueue work?
29. Compare a Functions trigger with input/output bindings; where do retry and checkpoint semantics live?
30. Why should a long AI HTTP operation become asynchronous, and how does the client get status/result?
31. Distinguish management-plane and data-plane RBAC for a managed identity.
32. Design a safe Key Vault secret rotation and outage/caching strategy.
33. Why is App Configuration not a secret store, and how can a feature flag become a release risk?
34. Which OpenTelemetry context and safe attributes must cross HTTP, event, message, data and model calls?
35. Write the reasoning for a KQL query that detects p95 regression after one revision.
36. A request succeeded but used a stale embedding and unauthorized cache entry. Which nontechnical-health signals should catch it?

---

# 9. Final readiness checklist

- [ ] I can map every May 5, 2026 objective to a section, lab and evidence artifact.
- [ ] I can build, version, store, authenticate, scan and run immutable images with ACR/Tasks.
- [ ] I can configure and troubleshoot App Service custom containers and runtime settings/secrets.
- [ ] I can deploy Container Apps environments/apps/revisions, traffic and KEDA scaling.
- [ ] I can deploy AKS manifests and diagnose image, pod, probe, service, identity, scaling and connectivity.
- [ ] I can implement Cosmos SDK/query, partition/index/consistency/RU, vectors and change feed processing.
- [ ] I can implement PostgreSQL schema/index, pgvector exact/ANN/filter/RAG and compute/memory/storage/connection tuning.
- [ ] I can implement Managed Redis operations, cache expiration/invalidation/eviction and vector indexes while following the current service transition.
- [ ] I can choose queue/topic/subscription, settle/retry/dead-letter Service Bus messages and preserve idempotency.
- [ ] I can publish/filter/retry/dead-letter custom/system Event Grid workflows.
- [ ] I can build, configure and deploy Python Functions with understood trigger/binding/scale semantics.
- [ ] I can use managed/workload identity and data-plane least privilege.
- [ ] I can retrieve/rotate unavoidable Key Vault secrets and refresh App Configuration/flags safely.
- [ ] I can propagate OpenTelemetry context and query end-to-end application/dependency telemetry with KQL.
- [ ] I can troubleshoot from user symptom through image/revision/container, broker, data/cache, identity/config and model dependencies.
- [ ] I have rechecked the blueprint, lifecycle, Practice Assessment availability, service tiers/limits/SDKs/vector support and Redis retirement immediately before the exam.

---

# Places to learn

This is **not a complete list**, and it is not a recommendation to consume everything. Pick one current primary path, build the labs, and use targeted references or practice for gaps. Times are page-published when available; otherwise they are clearly labeled estimates. Catalogs, schedules, access, duration, price and alignment change. Avoid dumps or anything claiming recalled/live exam questions.

## Start with Microsoft

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official AI-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200) | Public | 30–60 min | Authoritative objectives, weights and lifecycle |
| [AI-200T00 Microsoft Learn course](https://learn.microsoft.com/en-us/training/courses/ai-200t00) | Public self-study; paid instructor option | 5 instructor-led days; 32h4 displayed across 9 paths plus labs | Primary structured coverage; choose targeted modules after gap mapping |
| [Azure Architecture Center AI architecture](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/) | Public | 4–12 hours selectively (estimate) | Production tradeoffs, reliability and service composition |
| [Microsoft Azure samples](https://github.com/Azure-Samples) | Public | 8–20 hours selectively (estimate) | Current SDK and deployable examples; verify maintenance and security before reuse |
| [Microsoft exam sandbox](https://aka.ms/examdemo) | Public | 20–30 min | Interface familiarity; no technical questions |

Microsoft's credential page explicitly said no AI-200 Practice Assessment was available on August 31, 2026. Recheck rather than substituting an assessment for a different exam.

## Courses and video

| Resource | Access | Estimated time | Best use and freshness note |
|---|---|---:|---|
| [O'Reilly Azure AI Cloud Developer Associate AI-200 Crash Course](https://www.oreilly.com/live-events/azure-ai-cloud-developer-associate-ai-200-crash-course/0642572385149/0642572385132/) | Paid subscription/live event | About 4 hours from displayed agenda; scheduled October 1, 2026 | Blueprint-wide live review with Reza Salehi; upcoming after this guide's validation date, so verify schedule/recording |
| [Udemy AI-200 Complete Course by Luke Ginn](https://www.udemy.com/course/ai-200-azure-ai-cloud-developer-associate-complete-course/) | Paid; price varies | 21h19 displayed / 55 lectures | Updated August 2026, broad hands-on coverage; includes adjacent agent content, so map to blueprint |
| [Udemy AI-200 Exam Prep by Kuljot Singh Bakshi](https://www.udemy.com/course/azure-ai-cloud-developer/) | Paid; price varies | 18h5 displayed / 135 lectures | Updated June 2026, objective-oriented demos and labs |
| [Udemy AI-200 course by Scott Duffy](https://www.udemy.com/course/ai200-azure/) | Paid; price varies | 3h54 displayed / 29 lectures | Concise overview updated May 2026; supplement with implementation labs |
| [Microsoft Reactor YouTube](https://www.youtube.com/@MicrosoftReactor) | Public | 3–10 hours selectively (estimate) | Search current Container Apps, Cosmos vector, PostgreSQL/pgvector, Redis, eventing and observability sessions |
| [John Savill Azure Master Class repository](https://github.com/johnthebrit/AzureMasterClass) | Public | 3–8 hours selectively (estimate) | Broad Azure platform/network/identity architecture and whiteboards; not a complete AI-200 path and may predate current vector/Managed Redis objectives |

No dedicated current AI-200 Pluralsight path was found publicly on the checked date. Use current service-specific courses only when their release date and terminology match the objective; do not infer certification coverage from an older AZ-204/AI-102 path.

## Practice and labs

| Resource | Access | Estimated time | Best use and caution |
|---|---|---:|---|
| [AI-200 Practice Assessment status on credential page](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-cloud-developer-associate/) | Public status; assessment unavailable when checked | Recheck in 1–2 min | Use the official assessment first if Microsoft later publishes it |
| [Udemy AI-200 practice tests by Scott Duffy](https://www.udemy.com/course/ai200-tests/) | Paid; price varies | Four 25-question tests plus explanation review; 3–6 hours (estimate) | New third-party practice; verify explanations against current Microsoft docs and reject live-question claims |
| This guide's eight labs | Azure access; costs vary | 28–50 hours (estimate) | End-to-end build, failure, identity, replay, observability and recovery proof |
| [Azure-Samples GitHub organization](https://github.com/Azure-Samples) | Public; Azure use may cost | 8–20 hours selectively (estimate) | Extend official samples with negative tests, identity, telemetry and cleanup |

No dedicated MeasureUp or Whizlabs AI-200 practice product was found in the public pages checked on August 31, 2026. Recheck later; do not relabel AZ-204, AI-102 or AI-103 practice as AI-200 coverage.

## A practical study sequence

1. Map the official blueprint to one deployable architecture and record the currently unavailable Practice Assessment.
2. Complete the Microsoft Learn paths or one current structured course; do not stack passive courses.
3. Build Labs 1–3 until container deployment, identity, rollout, scaling and diagnosis are routine.
4. Build Labs 4–6 and compare Cosmos, PostgreSQL and Redis using the same corpus/SLO evidence.
5. Build Labs 7–8 and prove duplicate, retry, DLQ, rotation, distributed trace, KQL and reconciliation behavior.
6. If an official Practice Assessment appears, use it once as a diagnostic; remediate by objective and lab.
7. Recheck the blueprint, credential page, SDK/service limits, vector/index support, course schedule and Azure Managed Redis transition immediately before the exam.

---

*This independent guide is based only on public sources and original synthesis. It is not affiliated with or endorsed by Microsoft, GitHub, HashiCorp, or any learning vendor.*
