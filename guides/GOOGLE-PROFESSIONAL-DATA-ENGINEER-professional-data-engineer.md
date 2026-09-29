---
exam_code: GOOGLE-PROFESSIONAL-DATA-ENGINEER
vendor_id: google-cloud
official_blueprint: https://cloud.google.com/learn/certification/data-engineer
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# Google Cloud Professional Data Engineer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, links, volatility labels, and exam-integrity compliance were checked September 29, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#google-professional-data-engineer-coverage-record). The [official page](https://cloud.google.com/learn/certification/data-engineer) and [detailed guide](https://services.google.com/fh/files/misc/professional_data_engineer_exam_guide_english.pdf) are authoritative.

**CURRENT BLUEPRINT:** Five domains weighted approximately 22%, 25%, 20%, 15%, and 18%; actual five-page PDF read September 29, 2026. The mapping covers 67 main considerations under 19 numbered objectives; four transformation sub-bullets remain within their parent consideration<br>
**Upcoming blueprint change:** The live page says a branding update is coming, without a dated replacement blueprint. Continue using its linked standard guide; do not infer a new exam date from a product rename.<br>
**Official source:** [Professional Data Engineer certification](https://cloud.google.com/learn/certification/data-engineer) · [official exam guide](https://services.google.com/fh/files/misc/professional_data_engineer_exam_guide_english.pdf)

## How to use this guide

Study one connected lifecycle: requirement and governed data contract → ingestion → validation/transformation/enrichment → storage/model → consumption/sharing → orchestration/CI-CD → observability, optimization and recovery. For every choice, state semantics, scale, latency, locality, identity, failure/replay behavior, cost and evidence. A pipeline that runs once is not a production data system.

The exam is two hours, USD 200 before applicable tax or regional differences, 40–50 multiple-choice and multiple-select questions, English/Japanese, online or onsite, and valid for two years. Google lists no prerequisite and recommends three or more years of industry experience including at least one year designing and managing Google Cloud data solutions. Verify the live page before scheduling.

**VERIFY CURRENT — renewal routes:** The same page separately lists a one-hour, USD 100 renewal exam with 20 questions, English/Japanese, and two-year validity for eligible active holders. Designated Google Skills courses/badges instead renew for one year, with linked accounts and completion within the last active year. This guide maps the standard exam; the separate renewal PDF was not independently reviewed.

The September 29 [deep-review record](../docs/research/2026-09-29-google-professional-data-engineer-deep-review.md) records source reading, 40 executed local checks, 48 answered checks and eight proposed cloud labs. Independent human review and live-cloud practice remain pending.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context. It is supporting knowledge, not a claim that the item appears verbatim in the published objectives.

## Objective map

| Domain | Weight | Core proof |
|---|---:|---|
| Designing data processing systems | ~22% | Requirements become secure, reliable, portable and migratable architecture |
| Ingesting and processing data | ~25% | Batch/stream pipelines preserve defined semantics and can be deployed repeatedly |
| Storing data | ~20% | Storage, warehouse, lake and platform choices match access/governance/cost |
| Preparing and using data for analysis | ~15% | Governed data performs for BI, ML/RAG and sharing |
| Maintaining and automating data workloads | ~18% | Capacity, schedules, telemetry, diagnosis, restart and recovery are controlled |

---

## 1. Designing data processing systems — about 22%

### Establish the data contract and trust boundaries

Capture source/owner, schema and semantics, event/business keys, timestamps/time zone, units, classification, allowed purposes/users/regions, volume/rate/growth, freshness/latency, completeness/accuracy/uniqueness, retention/deletion, lineage, RTO/RPO and consumers. Separate event time from processing time. Define how schema evolution, duplicates, late data, correction, deletion and replay behave before choosing a product.

Use organization/folder/project, dataset and table boundaries to express administration, environment and data-domain ownership. IAM grants minimum roles to groups/workload identities; organization policy constrains permitted configurations. Separate development/test/production data and identities. For PII, minimize/tokenize/mask where possible, govern purpose and access, use regional placement required by sovereignty, and map legal obligations to controls and evidence.

Encryption in transit/at rest is baseline. CMEK changes key control and adds permission, rotation, availability and destruction failure modes. VPC Service Controls may reduce supported-service exfiltration paths but do not replace IAM, application authorization or classification.

### Design for fidelity, reliability and portability

Data quality rules need owner, threshold and action: reject/quarantine, correct, warn or stop. Validate at intake and after material transformations; preserve raw/replayable evidence where policy allows. ACID transactions fit multi-change invariants, but not every analytical pipeline needs row-level transactions. State the consistency, isolation, idempotency and availability requirements rather than selecting ACID reflexively.

Dataflow/Apache Beam fits unified managed batch/stream processing. Dataproc fits Spark/Hadoop ecosystem workloads and migration. Dataform manages SQL transformations and dependencies in BigQuery. Cloud Data Fusion provides visual/integration pipelines. LLM-assisted query generation can improve productivity, but validate syntax, semantics, permissions, cost, prompt/data disclosure and output against trusted tests.

Reliability design covers retries, duplicate delivery, checkpoint/state, windowing, late data, poison records, dead letters, backpressure, restart, regional failure, corruption and missing input. Orchestration must not hide the processing engine’s semantics.

Portability may be a requirement, not an absolute virtue. Open formats/APIs, Apache Beam/Spark/Kafka ecosystems and decoupled storage can help, but lowest-common-denominator design can sacrifice managed value. Record exit needs, cost and migration mechanism. Catalog, profile and discover data with governed metadata/lineage; a catalog entry is not proof that data is correct or authorized.

### Define what a replay is allowed to change

**PRACTICAL DEPTH:** Record source epoch, entity key, immutable event ID, operation, source order, event time, ingestion time and schema version. An event ID suppresses the same delivery; a source order prevents an older event from overwriting a newer state. A deletion needs retained ordering evidence until the permitted replay horizon closes, otherwise an old insert can resurrect it. Sequence resets after migration or failover need an explicit epoch/cutover rule. These are application design requirements, not one universal CDC format.

[Datastream](https://docs.cloud.google.com/datastream/docs/events-and-streams) delivers at least once and does not promise delivery order. Its BigQuery destination uses event metadata and an internal sequence to merge changes; a custom Cloud Storage consumer must implement the required source-specific ordering and duplicate handling. Do not sort all connectors by arrival time or assume one timestamp field is sufficient for every database. Reconcile current rows, deleted keys and business aggregates across the backfill/CDC overlap.

### Plan migrations

Inventory sources, owners, dependencies, data volume/change rate, quality, access, retention, downstream jobs and validation. Choose online replication, scheduled transfer, bulk appliance or rebuild based on downtime, bandwidth and consistency. BigQuery Data Transfer Service targets supported source ingestion; Database Migration Service targets supported database migrations; Datastream supplies change data capture; Transfer Appliance supports offline bulk movement. Define initial load, CDC/coexistence, reconciliation, performance, cutover, rollback and decommission.

> **Related item:** A data contract makes producer/consumer expectations testable. A schema registry covers structure, but the contract also needs semantics, quality, ownership, privacy and change policy.

---

## 2. Ingesting and processing — about 25%

### Select the ingestion pattern

| Need | Starting option | Critical semantics |
|---|---|---|
| Asynchronous events | Pub/Sub | at-least-once behavior, ordering scope, retention, retry/dead letter, idempotency |
| Database changes | Datastream | supported source/target, initial load, CDC ordering, schema change, reconciliation |
| Managed scheduled SaaS/data transfer | BigQuery Data Transfer Service | connector schedule, backfill, quota, source semantics |
| Files/objects | Cloud Storage + event/schedule/transfer | atomic arrival convention, version, checksum, lifecycle, replay |
| Kafka ecosystem | Managed Service for Apache Kafka or compatible integration | partitions, ordering, offsets, retention, consumer recovery |
| Online database migration | Database Migration Service | compatibility, CDC, network, cutover and fallback |

Define source and sink contracts, network route/private access, workload identity, encryption/key behavior, transformation DAG and orchestration. Design backfill/replay separately from steady state so a historical load does not overwhelm production or duplicate output.

### Build batch and stream pipelines

Batch processes bounded inputs and commonly optimizes throughput/cost. Streaming processes unbounded inputs and requires windows, triggers, watermarks/state and late-data policy. Window type—fixed, sliding or session—must match the business question. Watermark estimates event-time completeness; allowed lateness and triggers determine when/refinement behavior occurs. Exactly-once claims are end-to-end only if sources, engine, sinks and business side effects support them; idempotent writes and deterministic keys remain powerful.

Dataflow manages Beam pipelines; choose transforms, coders/schemas, parallelism, shuffle, state/timers, autoscaling and worker/network settings. Dataproc runs Spark/Hadoop jobs when ecosystem control or migration matters; ephemeral job clusters reduce idle cost/isolation risk while persistent clusters fit interactive/shared contexts if governed. BigQuery SQL and Dataform fit warehouse-native transformations. Data Fusion fits low-code connectors/mappings. AI enrichment adds model/version, batch/online, privacy, quality, safety, token/accelerator cost and reprocessing concerns.

Data cleansing includes parsing, types, normalization, validation, deduplication, missing/outlier policy and reference-data reconciliation. Never silently “fix” data without retaining rule/version and rejected evidence. Partition outputs for common filters and size files to avoid both tiny-file overhead and unmanageable objects.

### Distinguish processing, commit and business effects

[Dataflow](https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once) can commit pipeline results once while executing a transform more than once, even concurrently during retry. A remote charge, email or custom database write inside a transform needs its own correct contract. A processing log is not a commit receipt. Exactly-once processing also does not make a window complete when the configured late-data policy discards events.

Use [windows, watermarks and triggers](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-pipelines) to explain three different choices: which event-time group a record belongs to, how far completeness is estimated to have progressed, and when a pane is emitted. A late accepted record can revise an aggregate. If panes contain accumulated totals, summing every pane can count earlier records again; design the sink's replacement/version or delta contract explicitly.

[BigQuery Storage Write API](https://docs.cloud.google.com/bigquery/docs/write-api) defaults to an immediately queryable stream with at-least-once writes. Application-created streams can use offsets for exactly-once writes within a stream. Pending streams buffer data until an atomic commit; finalizing a stream and committing it are different steps. None of these labels deduplicates separately published business events automatically. Preserve stream/offset state and reconcile ambiguous acknowledgments in a real client lab.

For [BigQuery CDC](https://docs.cloud.google.com/bigquery/docs/change-data-capture), the documented path uses the default stream, protobuf, declared primary keys and sufficient apply capacity. Custom `_CHANGE_SEQUENCE_NUMBER` values compare up to four hexadecimal sections numerically in order; ordinary string sorting is wrong. Identical sequences fall back to ingestion time, and mixing supplied/missing sequences has unpredictable order. Define conflict handling upstream. `max_staleness` trades accepted freshness for query latency/cost: a stale baseline can trigger a runtime merge. Monitor apply watermark and backlog; the configured value is not proof of the business freshness SLO. Background apply and query-time merges use different reservation assignment types.

### Deploy and operationalize

Cloud Composer is managed Apache Airflow for DAG orchestration; Workflows orchestrates services/APIs with stateful steps. Neither replaces Dataflow/Spark/BigQuery processing. DAG tasks should be idempotent, parameterized, observable, retry-safe, time-zone aware, backfillable and bounded by dependencies/SLAs.

[Dataform assertions](https://docs.cloud.google.com/dataform/docs/assertions) find violating rows after table creation; manual assertion queries pass by returning zero rows. Pair uniqueness and non-null checks where the contract requires both. A dependency on the producing table alone does not make a failed assertion block the consumer. Set [assertion dependencies](https://docs.cloud.google.com/dataform/docs/dependencies) explicitly; `dependOnDependencyAssertions` adds direct dependency assertions, while per-action `includeDependentAssertions` takes precedence. Inspect the compiled graph and exercise a deliberately invalid fixture before publication.

For [Airflow tasks](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html), use a stable data interval and versioned inputs. Reading “latest” or using wall-clock time for business computation can change the result on retry. Pass small references between tasks and keep durable data in shared storage; a worker's local file may be unavailable to the next task. A retry-safe UPSERT still needs the correct key, source version and publication transaction.

CI/CD versions code, SQL, schemas/contracts, dependencies, infrastructure, pipeline/template, configuration and tests. Validate representative data, quality, security, performance/cost and rollback. Promote immutable artifacts through environments; do not edit production notebooks/jobs as the source of truth.

> **Related item:** Orchestration decides when and in what dependency order work runs; processing performs transformations. A successful orchestrator task can still produce wrong data.

---

## 3. Storing data — about 20%

### Choose from requirements, not product familiarity

| Data/access pattern | Candidate | Design focus |
|---|---|---|
| Objects, raw zones, archive | Cloud Storage | location/class, lifecycle, retention, object naming/format, request/egress cost |
| Analytics warehouse | BigQuery | partition/cluster, model, workload/capacity, governance, query cost/performance |
| Open lake/lakehouse access | BigLake + Cloud Storage/BigQuery | format/catalog, fine-grained governance, metadata, engine interoperability |
| Managed relational | Cloud SQL / AlloyDB | compatibility, transaction/HA/backup, read scale, connections, maintenance |
| Global/horizontal relational | Spanner | key/schema, consistency, locality, capacity and cost |
| Wide-column operational | Bigtable | row key, hotspot avoidance, cluster/replication, latency/throughput |
| Documents | Firestore | query/index model, hierarchy, transaction/consistency and cost |
| Cache | Memorystore | engine, eviction, HA/persistence, invalidation and source of truth |

Estimate storage plus read/write/operation, compute, capacity/reservation, retrieval, network egress, replication, backup and people costs. Lifecycle management implements class transition, retention, archive and deletion; legal hold and deletion guarantees require explicit validation.

### Prove the key and the grain

[BigQuery primary and foreign keys](https://docs.cloud.google.com/bigquery/docs/primary-foreign-keys) are **not enforced**. The optimizer can use them; incorrect declarations can lead to incorrect query results. Validate unique, non-null business keys and referential relationships before relying on constraints. State the grain of each table and join: two dimension rows for one customer can turn a 100-cent sale into 200 cents. `DISTINCT` on a final result is not a general repair for a broken join contract.

[Bigtable row keys](https://docs.cloud.google.com/bigtable/docs/schema-design) should serve expected exact-key, prefix and range reads while distributing traffic. A timestamp-first key can concentrate new writes; an entity-first key helps entity/time reads but does not make a global time query efficient. Numeric text requires consistent encoding/padding for lexical order. An intensely active entity can still be hot. Choose sharding only after accounting for the resulting read fanout and merge cost. Row-level atomicity does not supply multirow relational transactions or joins.

### Warehouse, lake and governed platform

Warehouse models should support business grain, keys, dimensions/facts, history, measures and access patterns. Normalize to protect transactional integrity; denormalize/star models to simplify analytical access when appropriate. Partition pruning reduces scanned data; clustering improves locality for common filters. Materialized views and BI Engine can accelerate repeated BI patterns but require freshness, eligibility, capacity and cost decisions.

A lake needs zones, file/table format, schema/quality, catalog/lineage, access, lifecycle, compaction/optimization, discoverability and cost control. An unmanaged bucket is not a governed lake. The blueprint names Dataplex and Dataplex Catalog; current documentation calls the catalog Knowledge Catalog. These services can organize/discover/govern distributed data; BigQuery/BigLake and Cloud Storage supply analytical/storage surfaces. Federated governance assigns domain ownership within central policies, interoperability and evidence. It is not “every team chooses anything.”

**VERIFY CURRENT — naming versus scope:** [Knowledge Catalog documentation](https://docs.cloud.google.com/dataplex/docs/introduction) retains existing Dataplex API, client, CLI and IAM names. The [April 22, 2026 announcement](https://cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog), by Chai Pydimukkala and Sam McVeety, describes aggregation, enrichment and search, with a mix of release stages. Use it as dated context, then check the current feature documentation. Generated descriptions and suggested joins still need owner review; catalog discoverability, permission to read underlying data and correctness of a generated answer are separate checks. Product naming does not alter the linked exam blueprint by itself.

> **Related item:** Data mesh is an organizational and architectural operating model around domain-owned data products, self-service platform, federated governance and interoperability—not a single Google Cloud product.

---

## 4. Preparing and using data for analysis — about 15%

### BI and query performance

Expose stable semantic definitions, correct grain, documented freshness and authorized views. Precalculate only when latency/cost justifies the added freshness and pipeline complexity. Diagnose slow/expensive BigQuery work using execution details, bytes scanned, partition pruning, shuffle/skew, join strategy, repeated computation, materialization, slots/capacity, concurrency and BI Engine—not folklore.

Use IAM at appropriate project/dataset/table/view scopes, authorized views/datasets, row-level security, column policy tags/data policies and dynamic masking according to current product behavior. Sensitive Data Protection (formerly Cloud DLP) discovers/classifies/de-identifies sensitive content; it does not assign business purpose or replace access review.

### AI/ML and RAG preparation

Prevent label leakage by making training features available only from information known at prediction time. Split by entity/time where appropriate, handle missing/outlier/imbalance policy, version transformations and preserve lineage. BigQuery ML trains/evaluates models with SQL and can integrate broader AI functions; validate task metric, slice behavior, drift, privacy, cost and serving consistency.

**PRACTICAL DEPTH — point-in-time features:** A historical event can arrive after a prediction. Filter on both the event timestamp and the time its feature was available, then apply a deterministic version rule. Filtering only by event time leaks late backfills into offline training. Preserve predictions without a matching historical feature as an explicit missing-value case; an inner join can silently change the evaluated population. The local SQL example demonstrates this with synthetic integer timestamps, not a deployed feature store.

For unstructured RAG data: authorize source → parse/OCR → clean/deduplicate → chunk → attach metadata/permissions/freshness → embed/index → retrieve/filter/rerank → evaluate. Test relevance/recall, permission trimming, answer faithfulness/citations, missing-answer behavior, deletion and re-index. An embedding is not a permission or truth score.

### Governed sharing

Define recipient, purpose, allowed fields/rows, freshness, duration, onward-use, audit, revocation and cost. Analytics Hub/BigQuery sharing can publish governed data products without copying in some patterns; reports/visualizations still need row/column/source permissions. Public publishing requires classification, legal/privacy and re-identification review.

---

## 5. Maintaining and automating workloads — about 18%

### Capacity and cost

Optimize for required outcome, not minimum resource count. Attribute cost by project/reservation/labels and job/query, then inspect bytes, slots, workers, shuffle, storage class, egress and idle clusters. BigQuery Editions/reservations provide capacity-management choices; on-demand and reserved capacity fit different predictability/isolation requirements. Interactive jobs prioritize response; batch jobs can wait for capacity. Dataproc ephemeral clusters fit scheduled isolated work; persistent clusters may fit interactive/shared use but need utilization governance.

### Repeatability and operations

Composer DAGs and schedules need explicit start/time zone, catchup/backfill policy, dependencies, concurrency, retry/backoff, timeout, SLA, data interval, idempotency and alert ownership. Version infrastructure, pipeline templates, SQL, schema and configuration. Automation includes validation, release, rollback, repair, replay and teardown—not just scheduling.

Observe source lag/freshness, throughput, backlog, late/invalid/duplicate rates, task/job state, worker/slot/cluster capacity, error/retry, sink commit, data-quality outcome and cost. Cloud Monitoring/Logging show platform evidence; BigQuery admin/resource views expose jobs/capacity. Correlate pipeline run, code/config version, data interval and output partition.

Troubleshoot from first bad/missing output backward through sink commit, transform/quality, worker/job, source offset/file, network/identity/quota and scheduler. Preserve evidence before blind restart. A retry may duplicate side effects; a successful rerun may overwrite later corrections.

Design restart checkpoints and deterministic outputs. Multi-zone/region processing helps only when input, metadata, orchestrator, sink, keys and dependencies also survive. Prepare for corruption/missing data with immutable/replayable source where permitted, validation/reconciliation, version/time-travel or backup, quarantine and tested restoration. Cloud SQL and Redis/Memorystore replication/failover semantics differ; verify RPO/RTO and client reconnection.

### Separate corruption recovery from regional continuity

[BigQuery time travel](https://docs.cloud.google.com/bigquery/docs/time-travel) has a configurable two-to-seven-day window, seven by default. A deleted table uses the window in force when it was deleted; increasing today's setting does not retroactively extend that window. The additional seven-day fail-safe period requires Cloud Customer Care for recovery and cannot be directly queried. Tables that have or had row access policies require the documented override permission for historical access. Time travel does not restore all table metadata. Plan longer retention and restore validation separately; do not equate a delete request with immediate disappearance of every retained copy.

[Managed BigQuery disaster recovery](https://docs.cloud.google.com/bigquery/docs/managed-disaster-recovery) uses Enterprise Plus failover reservations and paired dataset replicas after backfill. Hard failover can lose unreplicated data and access-control changes; soft failover waits for replication and needs both regions available. The reserved baseline is available after failover, while additional autoscaling depends on secondary-region capacity. Scheduled queries do not automatically relocate: recreate them in the new primary location, and account for regional job history. Test clients, permissions, schedules, replay and reconciliation alongside the data replica.


> **Related item:** Data observability combines platform health with data health—freshness, volume, distribution, schema, lineage and quality. A green VM/job metric does not prove a correct dataset.

---

## Integrated scenarios

### 1. Late and duplicated commerce events

Pub/Sub events arrive out of order and may repeat. Assign stable event/order IDs and event time, process with Beam/Dataflow windows/watermarks, write idempotently, quarantine malformed records, and reconcile against the transactional system. Track source backlog, late/duplicate/invalid rates, window completeness and BigQuery partition freshness. Make replay bounded by interval/version and prove it does not double revenue.

### 2. Governed clinical analytics and RAG

Separate identifiable raw data from de-identified analytical products; enforce region, IAM, key and VPC-SC controls as required. Catalog/lineage each dataset, use row/column/masking controls, create approved warehouse models, and retain audit evidence. For RAG, carry source permissions into chunk metadata/filtering, evaluate retrieval/faithfulness and deletion, constrain model/tool data flow, and require human review for clinical consequence.

### 3. Warehouse migration with coexistence

Inventory sources/queries/SLAs, land historical data, capture changes, translate and test SQL, reconcile counts/checksums/business aggregates, compare performance/cost, run parallel, cut consumers in waves, retain rollback, then decommission. CI/CD versions Dataform/SQL/schema/IaC; capacity and query telemetry determine reservations and optimization.

## Hands-on evidence path

**Executed locally:** The following original Python program passed **40 checks** using only the standard library: 24 SQLite CDC/transaction checks, six point-in-time feature checks, four join-grain checks and six window-policy checks. Save it as `pde_data_workbook.py` and run `python pde_data_workbook.py` with Python 3.10+ and SQLite 3.24+. It creates only in-memory databases and closes them. [SQLite UPSERT documentation](https://www.sqlite.org/lang_upsert.html) explains the native conflict operation.

The CDC exercise retains a tombstone, ignores older source versions, rejects conflicting event IDs/equal versions, injects failure between state and ledger writes, proves rollback and retries successfully. Its source-order contract is an invented single-epoch integer sequence; it does not implement Datastream metadata, BigQuery's hexadecimal ordering/tie rule, distributed delivery, persistent crash recovery or concurrency. SQLite enforces its local keys; BigQuery key declarations do not. The feature query selects 10 rather than a late correction of 90 at prediction time 10. A broken dimension join raises 150 cents to 250; removing the known synthetic duplicate restores 150.

The final six checks are a deliberately limited fixed-window policy model with integer seconds, half-open intervals and an explicit close-at-boundary rule. They do not execute Beam triggers, watermarks, state or panes. No cloud account, API, model, notification, scheduler or infrastructure is used.

```python
"""Original synthetic practice: real SQLite, plus a small window-policy model.
Requires Python 3.10+ and SQLite 3.24+. No cloud services or external files.
"""
import json
import sqlite3


def database():
    db = sqlite3.connect(':memory:', isolation_level=None)
    db.executescript('''
        CREATE TABLE current_rows (
          id TEXT PRIMARY KEY NOT NULL, seq INTEGER NOT NULL CHECK(seq >= 0),
          deleted INTEGER NOT NULL CHECK(deleted IN (0,1)), cents INTEGER,
          CHECK((deleted=1 AND cents IS NULL) OR
                (deleted=0 AND cents IS NOT NULL AND cents>=0)));
        CREATE TABLE event_ledger (
          event_id TEXT PRIMARY KEY NOT NULL, payload TEXT NOT NULL);
    ''')
    return db


def apply_event(db, event_id, key, seq, deleted, cents, fail=False):
    # Deliberately restricted contract: one source epoch, per-key integer order.
    # Equal-version conflicting content is rejected, unlike BQ ingestion-time ties.
    if not event_id or not key or type(seq) is not int or seq < 0:
        raise ValueError('invalid identity or sequence')
    if type(deleted) is not bool:
        raise ValueError('deleted must be boolean')
    if (deleted and cents is not None) or (
        not deleted and (type(cents) is not int or cents < 0)
    ):
        raise ValueError('invalid amount')
    payload = json.dumps([key, seq, deleted, cents], separators=(',', ':'))
    db.execute('BEGIN IMMEDIATE')
    try:
        old_event = db.execute(
            'SELECT payload FROM event_ledger WHERE event_id=?', (event_id,)
        ).fetchone()
        if old_event:
            if old_event[0] != payload:
                raise ValueError('event ID reused with different content')
            db.execute('COMMIT')
            return 'duplicate'
        old = db.execute(
            'SELECT seq,deleted,cents FROM current_rows WHERE id=?', (key,)
        ).fetchone()
        if old and seq == old[0] and (int(deleted), cents) != old[1:]:
            raise ValueError('same sequence, conflicting content')
        changed = not old or seq > old[0]
        db.execute('''INSERT INTO current_rows VALUES(?,?,?,?)
          ON CONFLICT(id) DO UPDATE SET
            seq=excluded.seq, deleted=excluded.deleted, cents=excluded.cents
          WHERE excluded.seq > current_rows.seq''', (key, seq, deleted, cents))
        if fail:
            raise RuntimeError('injected failure before ledger insert')
        db.execute('INSERT INTO event_ledger VALUES(?,?)', (event_id, payload))
        db.execute('COMMIT')
        return 'applied' if changed else 'ignored'
    except Exception:
        db.execute('ROLLBACK')
        raise


def window_state(event_second, watermark, width=60, allowed_lateness=30):
    # Teaching policy, not Beam's timestamp precision or trigger implementation.
    if any(type(x) is not int or x < 0 for x in
           (event_second, watermark, allowed_lateness)) or width <= 0:
        raise ValueError('invalid window inputs')
    start = event_second // width * width
    end = start + width  # Half-open [start,end).
    state = ('closed' if watermark >= end + allowed_lateness else
             'late-accepted' if watermark >= end else 'on-time')
    return start, state


def run():
    checks = []
    def check(label, actual, expected):
        if actual != expected:
            raise AssertionError((label, actual, expected))
        checks.append(label)
    def rejects(label, error, action):
        try:
            action()
        except error:
            checks.append(label)
        else:
            raise AssertionError(label)

    db = database()
    row = lambda key='A': db.execute(
        'SELECT seq,deleted,cents FROM current_rows WHERE id=?', (key,)
    ).fetchone()
    seen = lambda event: db.execute(
        'SELECT count(*) FROM event_ledger WHERE event_id=?', (event,)
    ).fetchone()[0]
    check('initial update', apply_event(db, 'e3', 'A', 3, False, 100), 'applied')
    check('retry', apply_event(db, 'e3', 'A', 3, False, 100), 'duplicate')
    check('one effect', row(), (3, 0, 100))
    check('old snapshot ignored', apply_event(db, 'e1', 'A', 1, False, 70), 'ignored')
    check('old snapshot cannot overwrite', row(), (3, 0, 100))
    check('delete retained', apply_event(db, 'e4', 'A', 4, True, None), 'applied')
    check('tombstone', row(), (4, 1, None))
    check('old update after delete', apply_event(db, 'e2', 'A', 2, False, 80), 'ignored')
    check('no resurrection', row(), (4, 1, None))
    check('explicit newer create', apply_event(db, 'e5', 'A', 5, False, 150), 'applied')
    rejects('event collision', ValueError,
            lambda: apply_event(db, 'e5', 'A', 6, False, 999))
    check('collision unchanged', row(), (5, 0, 150))
    rejects('sequence conflict', ValueError,
            lambda: apply_event(db, 'bad5', 'A', 5, False, 999))
    check('conflict not acknowledged', seen('bad5'), 0)
    rejects('failure between writes', RuntimeError,
            lambda: apply_event(db, 'e6', 'A', 6, False, 200, fail=True))
    check('state rollback', row(), (5, 0, 150))
    check('ledger rollback', seen('e6'), 0)
    check('retry after rollback', apply_event(db, 'e6', 'A', 6, False, 200), 'applied')
    check('repaired state', row(), (6, 0, 200))
    check('independent key order', apply_event(db, 'b1', 'B', 1, False, 40), 'applied')
    check('same version same content', apply_event(db, 'e6-copy', 'A', 6, False, 200), 'ignored')
    rejects('boolean sequence', ValueError,
            lambda: apply_event(db, 'bool', 'A', True, False, 0))
    rejects('negative amount', ValueError,
            lambda: apply_event(db, 'negative', 'A', 7, False, -1))
    check('only live amounts', db.execute(
        'SELECT sum(cents) FROM current_rows WHERE deleted=0').fetchone()[0], 240)
    db.close()

    db = sqlite3.connect(':memory:')
    db.executescript('''
        CREATE TABLE features(entity TEXT,event_at INT,available_at INT,revision INT,value INT);
        INSERT INTO features VALUES
          ('A',8,9,1,10),('A',8,12,2,90),('A',11,11,1,30),('B',3,4,1,7);
        CREATE TABLE predictions(id INT,entity TEXT,at INT);
        INSERT INTO predictions VALUES(1,'A',10),(2,'A',12),(3,'B',5),(4,'C',10),(5,'A',8);
    ''')
    rows = db.execute('''SELECT p.id,(SELECT f.value FROM features f
      WHERE f.entity=p.entity AND f.event_at<=p.at AND f.available_at<=p.at
      ORDER BY f.event_at DESC,f.available_at DESC,f.revision DESC LIMIT 1)
      FROM predictions p ORDER BY p.id''').fetchall()
    check('as known at prediction', rows[0], (1, 10))
    check('most recent event', rows[1], (2, 30))
    check('other entity', rows[2], (3, 7))
    check('unknown entity retained', rows[3], (4, None))
    check('not yet available', rows[4], (5, None))
    check('event-time-only leakage', db.execute('''SELECT value FROM features
      WHERE entity='A' AND event_at<=10
      ORDER BY event_at DESC,available_at DESC LIMIT 1''').fetchone()[0], 90)

    db.executescript('''
        CREATE TABLE orders(id TEXT,customer TEXT,cents INT);
        INSERT INTO orders VALUES('o1','A',100),('o2','B',50);
        CREATE TABLE dimensions(customer TEXT,label TEXT);
        INSERT INTO dimensions VALUES('A','current'),('A','duplicate'),('B','current');
    ''')
    check('source grain', db.execute('SELECT sum(cents) FROM orders').fetchone()[0], 150)
    check('join fanout', db.execute('''SELECT sum(cents) FROM orders
      JOIN dimensions USING(customer)''').fetchone()[0], 250)
    check('uniqueness gate finds offender', db.execute('''SELECT customer,count(*)
      FROM dimensions GROUP BY customer HAVING count(*)<>1''').fetchall(), [('A', 2)])
    db.execute("DELETE FROM dimensions WHERE label='duplicate'")
    check('corrected grain', db.execute('''SELECT sum(cents) FROM orders
      JOIN dimensions USING(customer)''').fetchone()[0], 150)
    db.close()

    check('half-open first window', window_state(59, 50), (0, 'on-time'))
    check('boundary next window', window_state(60, 50), (60, 'on-time'))
    check('accepted late event', window_state(10, 70), (0, 'late-accepted'))
    check('closed policy boundary', window_state(10, 90), (0, 'closed'))
    check('same event later window state', window_state(60, 90), (60, 'on-time'))
    rejects('invalid event time', ValueError, lambda: window_state(-1, 0))
    return len(checks)


if __name__ == '__main__':
    print(f'{run()} local checks passed')
```

**Proposed cloud practice — not executed in this review:** Use an isolated authorized project with synthetic data, a cost budget, minimum roles and a cleanup inventory. The prior local check found `gcloud` absent from PATH; cloud installation and authentication were not attempted. For each lab retain configuration/code, expected versus observed results, failure evidence, repair and cleanup receipts.

| Lab | Build and inject | Acceptance, recovery and cleanup |
|---|---|---|
| 1. Contract and CDC | Define keys, source order/epoch, deletion and replay horizon. Backfill synthetic orders while applying newer updates, duplicate deliveries and deletes. | Reconcile exact current rows, deleted keys and revenue; show stale input cannot overwrite a newer state. Test a source-epoch transition. Stop the stream and remove synthetic destinations after retaining non-sensitive receipts. |
| 2. Stream completeness | Build a Beam/Dataflow windowed pipeline with explicitly selected triggers, accumulation and lateness. Inject early, late, duplicate and beyond-horizon events plus a worker retry. | Explain every pane and final total, source backlog and late/drop counters. Verify the sink's commit and business-ID contract separately. Stop jobs/subscriptions and delete owned state/output. |
| 3. BigQuery writes and quality | Compare default, offset-aware committed and pending streams; simulate an ambiguous acknowledgment. Build duplicate dimensions and null keys. | Show offset/commit behavior, zero-row violation queries and correct join grain; do not rely on `NOT ENFORCED` constraints. Remove tables, streams and job resources. |
| 4. Governed lake and catalog | Land synthetic files with schemas, owners, quality and retention. Register/catalog the assets and test two identities, including denied underlying-data access. | Discovery does not bypass data authorization; record lineage, quality failures, approved metadata and deletion/reindex behavior. Remove catalog entries and owned files under the selected retention policy. |
| 5. Dataform release gate | Version transformations and assertions; compile a consumer graph with explicit assertion dependencies. Inject duplicate keys or an invalid amount. | Demonstrate a failing assertion blocks the intended consumer, repair the fixture and rerun the same interval. Retain graph/action evidence and remove repositories, schedules and synthetic tables. |
| 6. Composer backfill | Orchestrate fixed intervals using immutable input references. Fail a task after output write, retry and backfill an overlapping interval. | No doubled totals or overwritten newer correction; inspect shared-storage references, retries, capacity and alerts. Remove DAG/schedules, environment and owned storage. |
| 7. ML and RAG data | Preserve event/availability times and feature versions. Prepare documents with identities, permissions and source versions; inject a late correction and revoked/deleted document. | Historical predictions use only available features; unauthorized/stale chunks cannot ground output. Measure retrieval/answer quality and missing-feature rate. Remove indexes, models/endpoints and input/output data. |
| 8. Recovery and capacity | Rehearse a deleted-table restore, then a separately planned regional recovery with replica, reservation, schedules, keys and clients. | Measure recovery and loss against agreed targets; validate ACLs, relocated schedules, totals and jobs after replay. Distinguish soft from hard failover. Restore intended topology and remove all lab reservations/replicas. |

## Original readiness checks and answers

1. **What belongs in a data contract beyond schema?** Semantics, keys/time, quality, privacy, owner, SLA, retention and change.
2. **Event time versus processing time?** When event occurred versus when system handled it.
3. **Why is a watermark not a guarantee?** It estimates completeness.
4. **Why are idempotent sinks important?** Retries/replays can repeat writes.
5. **When does Dataproc fit better than Dataflow?** Spark/Hadoop ecosystem/control/migration requirements.
6. **What does Composer orchestrate?** Task/service dependency and schedule, not transformation semantics itself.
7. **Why can a successful DAG produce bad data?** Orchestration success does not validate data correctness.
8. **What decides warehouse normalization?** Workload, grain, integrity, usability and performance.
9. **What causes Bigtable hotspots?** Poor row-key distribution.
10. **Why partition BigQuery?** Pruning/cost/performance/manageability.
11. **What does clustering add?** Locality within partitions for common filters.
12. **Why is an object bucket not automatically a data lake?** It lacks automatic schema, quality, catalog, governance and operations.
13. **What is federated governance?** Domain ownership under shared policies/interoperability/evidence.
14. **How can CMEK cause outage?** Missing/disabled/destroyed key or permission.
15. **What does VPC-SC not replace?** IAM, encryption, application authorization/classification.
16. **When use Datastream?** Supported database CDC.
17. **What must be reconciled in migration?** Counts/checksums/business aggregates, changes, schema and consumers.
18. **Why keep raw/replayable data where allowed?** Deterministic repair/reprocessing.
19. **What is label or time leakage?** Target/future information enters training; late backfills also leak when their availability timestamp is ignored.
20. **What permission problem can RAG introduce?** Retrieval can expose documents the user cannot access.
21. **Why is a citation insufficient?** It may not entail the claim or be authorized/current.
22. **What does Sensitive Data Protection do?** Discovery/classification/de-identification of sensitive data.
23. **On-demand versus reservation decision?** Predictability, utilization, isolation, concurrency and cost.
24. **Ephemeral versus persistent Dataproc?** Scheduled isolation/cost versus interactive/shared continuity.
25. **What should an actionable data alert contain?** User/data impact, threshold, owner, runbook and evidence.
26. **Why can blind restart be harmful?** Duplicate/overwrite/evidence loss.
27. **What must survive for regional recovery?** Input, metadata, orchestration, identity/keys, sink and dependencies.
28. **What proves backup usefulness?** Successful timed restore and reconciliation.
29. **Why version query-generating prompts?** Reproducibility, evaluation, security and rollback.
30. **What does Analytics Hub sharing still require?** Purpose, recipient access, row/column policy, audit/revocation.
31. **How do batch and stream optimize differently?** Throughput/cost for bounded data versus latency/state for unbounded data.
32. **What does late-data policy affect?** Result timing, revisions, state/cost and correctness.
33. **Why track data quality and platform metrics?** A healthy job can emit wrong/stale data.
34. **What makes a backfill safe?** Bounded interval, versioned code, idempotent output, capacity, validation and rollback.
35. **How should a data engineer use LLM query generation?** Treat output as proposed code: restrict data, review plan/cost/permission, test and version.
36. **What makes a data platform production-ready?** Governed contracts, repeatable delivery, observable semantics, controlled cost/security and tested recovery.
37. **Does exactly-once Dataflow processing make a remote side effect run once?** No. A transform may retry or run concurrently; the external operation needs its own commit/idempotency contract.
38. **Why retain deletion ordering evidence?** To reject an older insert/update after deletion rather than resurrect the row during replay.
39. **What does an event ID fail to establish?** It identifies one event; it does not order different changes to the same entity or resolve a reused-ID conflict.
40. **Does a BigQuery primary key reject duplicates?** No. Keys are unenforced and can inform optimization; validate the data or risk incorrect results.
41. **When does a Dataform quality failure block a consumer?** When the relevant assertion is explicitly included as a dependency; depending on the table alone is insufficient.
42. **What does the Storage Write API default stream guarantee?** At-least-once writes with immediate query visibility; offset-based exactly-once semantics require the appropriate application-created stream contract.
43. **How are custom BigQuery CDC sequences compared?** Numerically by hexadecimal section; equal sequences use ingestion time, so upstream ties and omitted sequences need explicit handling.
44. **Why can a stale CDC table increase query latency?** A query outside the allowed staleness interval can require a runtime merge of pending changes.
45. **Why is latest-data input dangerous on Airflow retry?** It may read a different dataset; bind business processing to the data interval and input version.
46. **Can an older event timestamp prove a feature was available?** No. Check availability time too; retain explicit missing-feature cases instead of dropping predictions.
47. **What can hard BigQuery failover lose beyond data?** Unreplicated ACL changes; also validate schedules, clients and regional job evidence after recovery.
48. **Is BigQuery fail-safe a normal historical query window?** No. It is an additional recovery period through Customer Care; ordinary queries cannot read it.

## Source and freshness notes

- **CURRENT BLUEPRINT:** The linked five-page PDF was fully read and all 67 main considerations mapped. The monitored objective text is unchanged. A missing lifecycle snapshot was initialized only after review; the subsequent check was unchanged. No printed PDF revision date or future exam-change date is invented.
- **VERIFY CURRENT:** Branding, feature release stages, APIs, regions, IAM, retention, connector semantics, capacity and provider catalogs change. Preserve exam terms while checking current product behavior. The Knowledge Catalog announcement is dated context, not proof of perfect generated answers or an exam transition.
- **PRACTICAL DEPTH:** Forty exact public-code checks ran locally. Eight cloud labs, provider course/lab interiors and independent human review remain pending. Public titles and release dates cannot prove a paid lesson's depth or accuracy.
- This is original public-source synthesis. No recalled exam item, proprietary question bank, dump, private data or paid course content was used. Official sample questions were observed only through their public form landing page.

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. Select one route, map it to the five standard-exam domains, and use first-party docs/labs for gaps. Public metadata was checked September 29, 2026. Suggested reading/practice budgets are planning estimates, not measured completion times.

| Resource | Access | Estimated time | Best use / currency note |
|---|---|---|---|
| [Official exam guide](https://services.google.com/fh/files/misc/professional_data_engineer_exam_guide_english.pdf) | Public | Suggested 1–2h then weekly | Canonical scope; actual five-page PDF reviewed; map every consideration to evidence |
| [Google Skills Data Engineer path](https://www.skills.google/paths/16) | Account; labs may require credits | 13 activities; current per-activity durations not exposed | First-party modular route. The earlier 77h45m total was not reverified; the page's relative four-month update age is not a duration |
| [Official sample questions](https://docs.google.com/forms/d/e/1FAIpQLSfkWEzBCP0wQ09ZuFm7G2_4qtkYbfmk_0getojdnPdCYmq37Q/viewform) | Public | Suggested 30–60m plus review | Familiarity with format; form landing page checked, question contents not used in this review |
| [Google Cloud Coursera certificate](https://www.coursera.org/professional-certificates/gcp-data-engineering) | Paid/subscription; audit varies | Five cards: 5+11+8+7+2 = 33h; landing estimate 4 weeks at 10h/week | Lakes/warehouses, batch, streaming, smart analytics/ML and Gemini Notebook study preparation. FAQ still says 3.5 months at 5h/week and names a starting course absent from the five cards; verify enrollment view |
| [Pluralsight PDE path](https://www.pluralsight.com/paths/google-cloud-professional-data-engineer-by-pluralsight) | Paid/subscription | Five courses 12h20m plus three 30m labs = 13h50m; header rounds to 14h | Janani Ravi courses February–May 2026; April labs cover partitioning/RLS, Dataflow/DLQs and Bigtable. All five domain titles are visible but an “actively in production” notice remains. Public metadata only |
| [Official Google Cloud Certified Professional Data Engineer Study Guide](https://www.oreilly.com/library/view/official-google-cloud/9781119618454/) | Paid O'Reilly | Suggested 12–18h reading plus practice; historical record: 2019, 352 pages | Current page returned 403; edition/page metadata not independently reverified. Older foundations need a current-domain gap check |
| [Whizlabs Professional Data Engineer](https://www.whizlabs.com/google-cloud-certified-professional-data-engineer/) | Paid; limited free items may vary | Suggested 25–45h selected study; current catalog duration unavailable | Direct fetch exposed only a title. Current lesson/lab coverage and counts were not verified; no practice questions read |
| [Google Cloud data analytics documentation](https://cloud.google.com/docs/data) | Public | Suggested 12–30h targeted | Index for official product docs; follow the cited behavior-specific pages and practice the failure cases |

No PDE-specific MeasureUp listing was verified in this review. Older routes need an explicit gap check for BigLake/AlloyDB, Knowledge Catalog versus exam-era Dataplex names, Dataform assertion dependencies, CDC ordering/staleness, BigQuery Editions, point-in-time feature preparation, permission-aware RAG and regional recovery. Provider metadata does not certify that any course covers every current behavior.
