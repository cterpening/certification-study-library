---
exam_code: MONGODB-ASSOCIATE-ATLAS-ADMINISTRATOR
vendor_id: mongodb
official_blueprint: https://learn.mongodb.com/courses/mongodb-associate-atlas-administrator-exam-study-guide
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# MongoDB Associate Atlas Administrator Study Guide

> **Independent AI-assisted resource — PUBLIC PATH REVIEWED; CURRENT DETAILED OBJECTIVES AND HUMAN REVIEW PENDING.** The September 29, 2026 review adds 40 answered prompts and 36 executed local checks, including an actual SQLite backup/restore exercise. No Atlas account, deployment, network control, CLI/API request or MongoDB server lab was executed. See the [coverage record](../docs/SOURCE-VALIDATION.md#mongodb-associate-atlas-administrator-coverage-record).

**CURRENT BLUEPRINT — public scope boundary:** The current public path still shows 13 required skill areas across foundations, performance, sharding, resilience and security. The saved 13 summaries are a public learning-path outline, **not detailed exam objectives or weighted domains**. The canonical [study-guide landing](https://learn.mongodb.com/courses/mongodb-associate-atlas-administrator-exam-study-guide) lists a free 30-minute guide and enrollment. Its public viewer failed and published document asset returned 403; no current objective body was acquired. Historical snapshots remain intact and require reconciliation before scheduling.

**VERIFY CURRENT — exam contract:** The [main exam page](https://learn.mongodb.com/pages/mongodb-associate-atlas-administrator-exam) and [course route](https://learn.mongodb.com/courses/mongodb-associate-atlas-administrator-exam) agree on 70 questions, 95 minutes, online proctoring, English, no prerequisite and USD 150. The course specifies multiple choice. The learning path's separate exam card still says two hours. The main/course contract is the preparation reference; verify the appointment and detailed policies before purchase. No passing percentage or current policy interior was established.

**Experience target:** Use a small-to-medium, single-cloud, single-region service as the starting exercise, then state its limits. That is preparation advice, not a newly verified formal prerequisite. Free tiers cannot exercise every recovery, private networking or encryption feature.

**VERIFY CURRENT — learning and release changes:** The [August 18, 2026 announcement](https://www.mongodb.com/company/blog/news/introducing-a-more-connected-flexible-path-to-certifications) connects paths and skill badges and advertises a full-path completion discount; it does not announce a replacement exam. No dated replacement was identified in accessible pages while the objective body remains unavailable. The [CLI changelog](https://www.mongodb.com/docs/atlas/cli/current/atlas-cli-changelog/) lists 1.58.3 released September 10, 2026. The [Atlas overview](https://www.mongodb.com/docs/atlas/) now distinguishes Core from Infinite public preview; edition-specific limitations must be checked. Selected [9.0 server release headings](https://www.mongodb.com/docs/manual/release-notes/9.0/) still say Upcoming despite current/preview manual wording. None of these observations establishes a new certification version.

## How to use this guide

Build one small Atlas environment from a written service contract, secure it, load synthetic data, observe it, create and test recovery evidence, then recreate selected configuration with CLI or API. The UI alone is not proof: capture configuration intent, commands or exported state, metrics, logs, alerts, restore results, and rollback steps.

Use free or low-cost disposable resources where features permit, set budgets and alerts, and delete them afterward. Some private networking, customer-managed key, dedicated tier, continuous backup, sharding, and advanced monitoring exercises may incur cost; use documented designs or an authorized sandbox when direct implementation is impractical. Never weaken production controls for practice.

> **About related items:** A `Related item:` callout adds prerequisite, cloud, security, reliability, automation, or governance context. It helps the public learning-path skill make sense in production but does not claim that MongoDB uses that wording in the enrolled exam guide.

## Public scope map

| Guide section | Current required path skills | Evidence to produce |
|---|---|---|
| 1. MongoDB foundations | Overview, CRUD, Data Transformation, Indexing | Correct data operations and explain-supported index evidence |
| 2. Atlas topology and scale | Sharding Strategies, Data Resilience | Tier/topology/region/shard decisions with failure and growth reasoning |
| 3. Identity and authorization | Secure Atlas: AuthN and AuthZ | Separate workforce, programmatic and database identities with least privilege |
| 4. Network and encryption | Networking Security, Encryption at Rest | Layered connectivity and key-lifecycle design with denied-path tests |
| 5. Monitoring and performance | Monitoring Tooling, Performance Tools and Techniques | Symptom-to-metric/log/query/index diagnosis and actionable alerts |
| 6. Reliability and recovery | Data Resilience, Cluster Reliability | Tested backup/restore, failover, maintenance and incident runbooks |
| 7. Administration and automation | Atlas administration tasks across the path | Repeatable UI/CLI/API workflow, drift controls, audit trail and cost guardrails |

## 1. MongoDB foundations

Atlas is a managed MongoDB service, not a different document database. Know databases, collections, BSON documents, `_id`, flexible shapes, nesting, arrays, single-document atomicity, replica sets, and the role of `mongod`/`mongos` conceptually. Distinguish the Atlas control plane—organizations, projects, users, policies, APIs—from the database data plane and database users.

An administrator must reason about application operations. Trace filters, projections, sorts, updates, deletes, and common aggregation stages enough to identify risky broad operations and expensive query shapes. Use synthetic data to compare intended and actual returned/modified counts. Application correctness remains the developer’s responsibility, but administrators need evidence to diagnose behavior.

Indexes exchange storage, memory, and write work for supported query efficiency. Derive compound indexes from equality, sort, range, projection, frequency, and selectivity. Understand `_id`, single-field, compound, multikey, unique, partial, TTL, and specialized indexes at a practical level. Use `explain("executionStats")`, query profiler evidence where authorized, and performance tools instead of guessing.

Aggregation pipelines are ordered transformations; early filtering and reduced document flow can matter. Identify whether a slow workload is caused by query shape, model, index, resource saturation, distribution, or concurrency. One fast run on sample data is not capacity evidence.

`Related item:` Shared responsibility matters. Atlas operates managed infrastructure and service controls, while the customer still owns identities, network choices, database permissions, data classification, application queries, retention, recovery objectives, and correct configuration.

### Use database evidence within its limits

[Single-document atomicity](https://www.mongodb.com/docs/manual/core/write-operations-atomicity/) does not make every multi-document maintenance task atomic. Guard expected current values and inspect actual match results when changing shared state. For query diagnosis, [ESR guidance](https://www.mongodb.com/docs/manual/tutorial/equality-sort-range-guideline/) supports index hypotheses, including range-before-sort for sufficiently selective ranges. The [explain reference](https://www.mongodb.com/docs/manual/reference/explain-results/) distinguishes returned results, examined keys and document examinations, which can repeat. Explain ignores existing plan-cache entries and its execution timing excludes network transfer. Compare application latency and query identities separately; this review produced no actual MongoDB plan or benchmark.

## 2. Atlas topology, deployment, and scale

Start with requirements: cloud provider/region, latency, residency, availability, recovery objectives, workload profile, data/index size, memory working set, CPU, IOPS, connections, growth, maintenance constraints, and budget. Then choose an available cluster type/tier and topology. Atlas names, limits, eligible features, and pricing change; verify the current docs and pricing calculator.

Organizations contain projects; projects scope clusters and many security/operational resources. Establish naming, ownership, billing, environment isolation, roles, tags, and audit expectations before provisioning. Avoid placing unrelated production and test workloads in one project merely for convenience.

Replication provides redundant members and automated elections. Understand primary/secondary roles, read preference, read/write concerns, replication lag, oplog window, and failure behavior conceptually. Region and node placement determine which failures can be tolerated and what latency/cost is introduced. Do not claim high availability without mapping concrete failure domains.

Vertical scaling changes cluster resources; storage and cluster auto-scaling can respond within configured boundaries. Horizontal scaling distributes data across shards. Sharding requires a well-chosen shard key based on cardinality, frequency, monotonicity, targeting, growth, and hotspot risk. Know chunks, balancing, `mongos`, config servers, shard-aware queries, and how poor distribution appears in metrics.

Plan capacity from representative load and headroom. Account for indexes, compression, backups, maintenance, connection pools, growth, and peak—not just current data bytes. Validate scale actions for application timeout, election/reconnect, cost, and rollback effects.

`Related item:` Multi-region and multi-cloud can improve particular failure or residency properties but also add latency, data-transfer cost, operational complexity, and provider dependencies. State the threat/failure being addressed before adding regions.

### Plan capacity per actual limit boundary

The following is an original arithmetic exercise, not an Atlas tier limit: assume 200 connections per server, an 80% planning target and 20 connections reserved for operational use. Twelve application processes with a maximum pool of 20 each could demand 260 including the reserve. A cap of 11 per process gives 152; 12 gives 164 and exceeds the chosen 160 target. Count all pools, processes, monitoring connections and topology changes against the correct per-server boundary. A configured pool maximum is not observed utilization, and this exercise does not model driver monitoring sockets or predict real throughput.

**VERIFY CURRENT — editions:** The current overview calls the familiar coupled compute/storage architecture Atlas Core and describes Atlas Infinite as public preview with separate compute and storage. The reviewed restore overview applies to Core. Do not transfer its recovery steps or assume preview features, regions and compatibility across editions. Broad “no downtime” descriptions are not an application-specific failover guarantee.

## 3. Identity and authorization

Separate Atlas users, teams, service accounts/API identities, federated workforce identities, and database users. Atlas roles govern control-plane resources; database roles govern operations inside MongoDB. A project owner is not the same security principal as an application database user. Map human, CI/CD, monitoring, backup, and application actors independently.

Apply least privilege at organization, project, and database levels. Prefer groups/teams and role assignment over unmanaged one-off grants. Use built-in database roles where they fit and custom roles only with a tested need. Scope privileges by database/collection/action, separate administration from application access, and use distinct identities for environments and workloads.

Choose authentication supported by the deployment and actor: SCRAM database credentials, certificates, cloud/workload identity, OIDC or federated mechanisms where available. Exact eligibility varies by tier and configuration. Store secrets in an approved secret manager, rotate them, bound lifetime, revoke on ownership changes, and test expired/disabled paths.

Review effective access, not only intended group membership. Audit changes, protect emergency access, require strong workforce authentication, and avoid shared administrator or application accounts. Test that a principal can perform required tasks and is denied unrelated tenant, database, control-plane, and destructive actions.

`Related item:` Identity lifecycle is an operational dependency. Provisioning, rotation, offboarding, break-glass use, evidence retention, and recovery from an identity-provider or KMS outage belong in the runbook.

### Separate token, role, source and database identity

The [API authentication reference](https://www.mongodb.com/docs/api/doc/atlas-admin-api-v2/authentication) describes OAuth 2.0 service accounts as the recommended method and HTTP Digest API keys as legacy. A service account exchanges its client ID and secret through the client-credentials flow; the documented bearer token lifetime is one hour. A token can be issued from an address that is not allowed to make the subsequent API call when an API access list is required. Token issuance therefore does not prove effective access. No credentials or tokens were requested in this review.

| Check | Question to prove in an authorized lab |
|---|---|
| Control-plane identity | Can the automation principal inspect the intended project, and is unrelated administration denied? |
| Data-plane identity | Can the application read/write only its intended database resources? |
| API source rule | Does the actual CI/automation egress address satisfy the control-plane access list? |
| Database connection route | Do DNS, route, TLS and the selected connection string reach the intended cluster? |
| Database authorization | After connection and authentication, are unrelated actions and data still denied? |

The local Boolean model illustrates separate gates using trusted fixture values. It does not authenticate anyone or reproduce Atlas role inheritance. The [security overview](https://www.mongodb.com/docs/atlas/setup-cluster-security/) establishes distinct database-user and network requirements. An IP range is a permitted source, not proof of an application or human identity.

## 4. Network security and encryption

Atlas connections require both network reachability and successful database authentication/authorization. IP access lists permit configured sources but are not user identity. Avoid broad public ranges and temporary entries that silently become permanent. Document DNS, egress, proxy/firewall, port, and TLS requirements for each client path.

Compare public access plus restricted IP lists, network peering, and private endpoints against routing, transitivity, overlapping CIDRs, DNS, cross-region/provider, availability, cost, and ownership. Private connectivity reduces public exposure; it does not replace authentication, authorization, TLS, monitoring, or application isolation. Test intended and denied routes from realistic client locations.

Encryption in transit protects network data through TLS. Encryption at rest is managed by Atlas, with customer-managed key options on eligible configurations. For BYOK, design cloud KMS permissions, key identifiers, rotation, regional relationships, audit, separation of duties, deletion protection, outage behavior, and recovery. Revoking or deleting a key can make data unavailable; rehearse the process in a safe environment.

Distinguish server-side storage encryption from client-side field-level or queryable encryption. Field-level approaches can protect selected data from infrastructure/database operators but shift key and query/schema responsibilities to applications. Select them from a threat model and current feature constraints.

`Related item:` Layered controls should fail closed without becoming unrecoverable. Maintain tested emergency access that preserves approval, short lifetime, audit, and post-use review.

### Private connectivity and key availability need their own evidence

The [private-endpoint reference](https://www.mongodb.com/docs/atlas/security-private-endpoint/?cloud-provider=aws) explicitly allows other connection methods to remain enabled. Creating an endpoint does not remove an existing public path. Inventory all methods and connection strings, then test both approved and unintended routes. The [network guidance](https://www.mongodb.com/docs/atlas/architecture/current/network-security/) distinguishes programmatic control-plane access lists from project data-plane lists. Its introductory shorthand about IP-based “authentication” should not replace the database identity requirement. Its Terraform access-list example uses an API-key resource under broader project wording; do not treat that as proof a database connection was allowed.

**VERIFY CURRENT:** Private endpoints require eligible dedicated tiers; Free/Flex do not support this route. The reference announces that non-port-mapped GCP endpoints will stop working April 30, 2027. That is a product migration watch, not an exam replacement. Regionalized endpoint changes can change connection strings and cause downtime. Provider-specific ports, DNS and failover behavior need exact deployment checks; no endpoint was created here.

The [customer-key reference](https://www.mongodb.com/docs/atlas/security-kms-encryption/) distinguishes a KMS network failure from invalid credentials or a disabled/deleted key. Invalid credentials or keys can stop database processes at a validation check; a connectivity failure alone is documented differently and does not by itself trigger the same shutdown. Key recovery, restart and restore dependencies still matter. Do not promise continued availability or recoverability after permanent key loss. The page scopes Infinite preview to AWS KMS and constrains its encrypted restores; apply the edition-specific rule. Search-node encryption/rebuild behavior adds separate recovery work.

## 5. Monitoring, logging, and performance

Define service indicators before alert thresholds: availability, operation latency, error/timeout rate, connections, CPU, memory/cache/working set, disk/IOPS/queue, network, replication lag/oplog window, query targeting, storage growth, backup health, and shard distribution. Correlate database metrics with application releases, traffic, cloud events, and configuration changes.

Atlas metrics, real-time views, logs, profiler/query insights, Performance Advisor, and alerts answer different questions. Treat recommendations as hypotheses. A suggested index may help one query but increase write and memory cost; reproduce the query shape, measure representative data, and verify downstream impact.

Create alerts that are actionable: condition, duration, severity, environment, owner, routing, runbook, context, suppression/maintenance behavior, and recovery notification. Test delivery and escalation. Avoid thresholds that fire continually or only after service failure. Use organization/project activity and audit evidence for administrative events where supported.

Troubleshoot from symptom to scope and timeline. Check recent changes, affected clients/regions/operations, saturation, connection behavior, slow query shapes, scans/sorts, lock/ticket or cache pressure, replication, distribution, and provider status. Change one controlled variable where practical and record before/after evidence.

Capacity and cost are related signals. Overprovisioning can hide inefficient queries; undersizing can make healthy queries fail. Use load tests, growth trends, performance thresholds, and budget alerts to decide query/index/model fixes versus scale.

`Related item:` Observability data can contain query values, identifiers, hostnames, or other sensitive context. Apply access control, minimization, masking, retention, secure export, and incident-evidence handling.

### Distinguish missing evidence from a healthy metric

The [monitoring overview](https://www.mongodb.com/docs/atlas/monitoring-alerts/) separates query diagnosis, deployment metrics, logs and alerts. The [alert basics](https://www.mongodb.com/docs/atlas/alert-basics/) page warns that ticket counts are dynamically adjusted on MongoDB 7.0 and later, so queued readers/writers are the relevant overload signal instead of a universal low-ticket threshold. Later generic ticket examples on the same page should not override that version caveat. Published thresholds are starting examples, not measured limits for this fictional service.

The workbook chooses a simple policy: three consecutive above-80 observations, exactly 60 seconds apart. A missing observation or time gap breaks the evidence; a single spike and equality at 80 do not pass. Three samples at 0, 60 and 120 seconds span two minutes, not three minutes of proven continuous breach. This is a local policy exercise, not Atlas alert-engine emulation, and it sends no notifications. Record sampling cadence, missing-data behavior, owner and recovery routing in a real alert lab.

## 6. Resilience, backup, recovery, and maintenance

Availability, durability, backup, and disaster recovery are distinct. Replica sets improve service continuity and redundancy but replicate accidental deletes and corruption. Backups create recovery points. Define recovery-point and recovery-time objectives, retention, immutability/protection, region/account dependencies, legal holds, and restoration ownership.

Choose supported Atlas backup and point-in-time capabilities for the tier and topology. Understand schedules, retention, snapshot storage, continuous restore window, restore targets, and constraints at a conceptual level, then verify current docs. Monitor backup success and age; a green policy is not recovery evidence.

Test restoration into an isolated authorized target. Validate access, indexes, counts, invariants, application compatibility, secret/network changes, and actual RPO/RTO. Prevent restored systems from sending production messages or being mistaken for current data. Record cleanup and evidence.

Plan node, zone/region, provider, network, identity, KMS, and accidental-change failures. For each, define expected automation, application behavior, detection, decision owner, manual steps, communication, validation, fallback, and failback. A topology is only resilient for failures it was designed and tested to tolerate.

Atlas manages much maintenance, but administrators still own version windows, application/driver compatibility, deprecations, maintenance policies, scaling impact, and communication. Review release notes, test in representative lower environments, back up appropriately, observe after change, and know which changes are reversible.

`Related item:` Chaos testing should be bounded and authorized. Begin with tabletop and restore exercises; do not inject failure into production without approvals, guardrails, stop conditions, and a recovery owner.

### Recovery is more than a completed restore job

[Cloud Backup](https://www.mongodb.com/docs/atlas/backup/cloud-backup/overview/) is unavailable on Free clusters; the overview includes Flex and higher but individual restore/PIT features have additional eligibility. Snapshot redundancy depends on provider and region: do not assume every Azure region has the same zone redundancy. A backup in one region does not automatically address loss of that region.

The [backup architecture guidance](https://www.mongodb.com/docs/atlas/architecture/current/backups/) explains snapshot-plus-oplog recovery and why transfer, replay and disk warming affect recovery time. Its advertised minute-level RPO and broad instant-access language are not measured results for a particular service. Use observed recoverable timestamps and restore validation. Its blanket development/test backup advice is also conditional on data recoverability and the purpose of the environment; a restore-training environment needs recovery evidence.

For a fictional incident at minute 137, the latest usable snapshot at 120 leaves a 17-minute recovery gap. An assumed usable continuous point at 135 leaves two minutes. Neither is a measured Atlas result. Detection 4 + decision 6 + transfer 18 + replay 7 + validation 9 + cutover 3 gives 47 minutes of recovery work. The 25-minute transfer/replay job alone would conceal failure of a 30-minute service recovery target.

The [Core restore overview](https://www.mongodb.com/docs/atlas/backup/cloud-backup/restore-overview/) requires preventing client requests to the target during restoration and documents version/topology constraints. Prefer an isolated target, then verify identities, values, indexes, permissions and application behavior before routing traffic. The SQLite example actually backs up and restores a local database, proves a later good write is absent from the snapshot, and explicitly replays that known fixture update. It does not implement MongoDB oplog replay or Atlas PIT restore.

The [Backup Compliance Policy](https://www.mongodb.com/docs/atlas/backup/cloud-backup/backup-compliance-policy/) restricts deletion, retention reductions and disabling backups. Disabling usually requires the named security/legal representative and MongoDB Support verification; the page documents an exception for empty projects with no retained snapshots. Extra retention beyond the protected period is not the same protection: appropriately authorized users can delete those extra-retained snapshots. Understand the cost and recovery obligations before enabling a policy in a real sandbox. No policy was enabled here.

## 7. Administration, automation, and governance

Be able to locate and inspect organizations, projects, clusters, database deployments, users/teams, database access, network access, backups, metrics, alerts, activity, and billing in the Atlas UI. Labels move; learn the intent and verify the current interface. Record who can change what and where audit evidence lives.

The Atlas CLI and Administration API enable repeatable work. Authenticate with a least-privilege nonhuman identity, select the correct organization/project explicitly, inspect before changing, use structured output, handle pagination/errors/rate limits, and avoid secrets in shell history/logs. Test destructive commands with a disposable target and require approval in automation.

Infrastructure as code can manage Atlas resources through supported providers/operators. Pin and review versions, protect state and credentials, separate environments, use plan/review/apply evidence, detect drift, constrain destructive replacement, and document imports/upgrades. UI emergency changes need reconciliation back into code.

Tagging, naming, ownership, budgets, cost alerts, expiration, and policy checks make a growing estate manageable. Inventory unused clusters, oversized tiers, uncontrolled storage auto-scaling, old snapshots, stale access entries, and orphaned identities cautiously. Never delete solely because a resource appears idle; verify owner, dependency, retention, backup, and recovery.

`Related item:` Automation expands blast radius. Use scoped credentials, policy gates, concurrency controls, canaries, idempotency, approvals, audit logs, and tested rollback rather than translating a manual click sequence into an unrestricted script.

### Check command purpose and inventory completeness

The [CLI overview](https://www.mongodb.com/docs/atlas/cli/current/) says `atlas setup` can create an account, deployment, database user and access-list entry. It is a provisioning workflow, not a harmless inventory probe. The original command templates below are **unexecuted** and contain placeholders; use the installed version's help and an already authorized identity before adapting them.

```text
atlas dbusers list --projectId PROJECT_ID --output json --page 1 --limit 100
atlas backups restores list CLUSTER_NAME --projectId PROJECT_ID --output json --page 1 --limit 100
atlas backups restores describe RESTORE_JOB_ID --clusterName CLUSTER_NAME --projectId PROJECT_ID --output json
```

The dedicated [database-user inventory](https://www.mongodb.com/docs/atlas/cli/current/command/atlas-dbusers-list/), [restore list](https://www.mongodb.com/docs/atlas/cli/current/command/atlas-backups-restores-list/) and [restore detail](https://www.mongodb.com/docs/atlas/cli/current/command/atlas-backups-restores-describe/) references supply the command syntax and scope flags. The database-user command documents a `results` envelope for ordinary JSON and a different shape with `--compact`. Pagination defaults to 100, with a maximum page size of 500. One successful page is not necessarily a full inventory; stable count and identity reconciliation still matter during concurrent changes.

**Documentation discrepancy:** The restore overview incorrectly places `atlas accessLists create` under restore details and describes a detail command as a list command. The dedicated restore pages also show older singular spellings in examples while their syntax headings use plural forms. Use the dedicated syntax and installed help, not the unrelated mutation. The overview permits backup-specific roles for viewing jobs, while CLI pages state Project Owner; verify the exact API/CLI authorization requirement rather than automatically granting a broad role. No CLI command was installed, parsed against an Atlas binary or executed here.

The [AWS landing-zone pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-aws-landing-zone-that-includes-mongodb-atlas.html) provides architecture context for multi-AZ layout, secrets, Terraform and private connectivity. It also instructs using an AWS AdministratorAccess access key for its example. That is not a least-privilege default for a project factory. Its strong no-interruption and PrivateLink-encryption wording should not replace application failure tests and TLS requirements. No repository was cloned, Terraform run or cloud credential created for this review.

## Integrated scenarios

### Scenario 1: Regional customer application

Start with a defined single-region failure model, data volume, recovery target and cost budget. Compare eligible Core topology and features, then map project/control-plane identities separately from application/database roles and routes. A private endpoint alone does not close public access. Produce a route inventory, denied-action matrix, per-server connection budget and isolated recovery plan. The workbook's 17-minute snapshot gap and 47-minute recovery timeline demonstrate which assumptions fail tighter targets; replace them with actual evidence before a production decision.

### Scenario 2: Performance degradation after release

A release doubles p95 latency and connection demand. Compare process count and pool ceilings before deciding the cluster needs more capacity. Inspect complete query shapes, returned identities, keys/documents examined and separate end-to-end latency. Check saturation, replication and version-appropriate queues, then choose one controlled correction with a rollback path. Missing metric samples must be an observability gap, not evidence of health. Save the rejected hypotheses and rerun under representative skew; the local arithmetic is not a load test.

### Scenario 3: Secure automated project factory

Define explicit organization/project scope, a minimal control-plane role and a separate application identity. Record API source restrictions, database routes, backup obligations, KMS dependencies, alert owners and decommission constraints. Paginate inventories and identify a database user by its full scope, not username alone. Review a concrete plan before mutations and reconcile UI emergency changes afterward. Refuse to treat `atlas setup` or an access-list create command as an inventory operation. The AWS pattern is a supporting example whose broad credential grant requires redesign for this factory.

## Hands-on evidence labs

**Execution boundary:** All 36 local workbook checks passed. They include actual in-memory SQLite backup/restore/integrity operations, arithmetic, IP membership and original decision models. SQLite is not MongoDB or Atlas. No real identity, API access list, network, KMS, alert delivery, Atlas CLI, backup service, benchmark or deployment was tested. All eight service activities below are proposed.

| Lab | Procedure and evidence | Failure or counterexample |
|---|---|---|
| 1. Foundations | In an authorized disposable database, perform bounded CRUD/aggregation and compare query identities before/after an index | Correct counts can still hide incorrect identities; explain is not client latency |
| 2. Topology and capacity | Record edition/tier/region, failure domains, measured resource demand and pool topology | Pool maxima across processes can exceed a per-server budget |
| 3. Least privilege | Test human, control-plane automation and application roles independently | Valid identity with denied route; allowed route with invalid identity; wrong plane/action |
| 4. Network and keys | Inventory public/private paths and provider-specific DNS/TLS/KMS requirements | Existing public access survives private-endpoint creation; KMS network outage differs from invalid key |
| 5. Observability | Design condition, cadence, missing-data treatment, owner and runbook; test delivery only in an authorized sandbox | Sparse samples cannot prove sustained breach; no notifications were sent here |
| 6. Performance | Reproduce one slow shape at realistic skew, compare query/index/model and pool hypotheses | Over-indexing or scaling can move cost; save write/resource evidence |
| 7. Recovery | Restore to isolation with client requests stopped; validate identities, values, access and application behavior | A successful job omits detection/cutover time; same count/sum can hide wrong records |
| 8. Automation | Review commands and scope, paginate inventory, detect drift and rehearse a bounded failed run | Wrong command family, incomplete page, broad credentials or retention protection block unsafe assumptions |

### Executed local recovery and decision workbook

Save as `atlas_workbook.py` and run with Python 3. Expected output is 36 passes, a planning cap of 11 connections per process per server, three scoped inventory identities, 350 restored cents and a 47-minute assumed recovery timeline. All times are invented inputs. The backup and SQL replay are real local operations, but no elapsed Atlas restore time or service SLA is measured. The Boolean access fixture uses trusted labels rather than authentication; the alert policy is illustrative and sends nothing. The inventory uses local pages with a known expected count, not a consistent live API snapshot.

```python
import ipaddress
import json
import sqlite3

checks = []


def check(name, condition):
    assert condition, name
    checks.append(name)


def rejects(name, call):
    try:
        call()
    except ValueError:
        checks.append(name)
    else:
        raise AssertionError(name)


def allowed(plane, action, network_ok, authenticated, grants):
    return network_ok and authenticated and (plane, action) in grants


app = {("data", "read"), ("data", "write")}
observer = {("control", "inventory")}
check("application read allowed", allowed("data", "read", True, True, app))
check("application cannot edit control plane", not allowed("control", "inventory", True, True, app))
check("observer cannot read application data", not allowed("data", "read", True, True, observer))
check("network is not authentication", not allowed("data", "read", True, False, app))
check("identity does not supply reachability", not allowed("data", "read", False, True, app))
check("token does not bypass API source rule", not allowed("control", "inventory", False, True, observer))
approved = ipaddress.ip_network("192.0.2.16/28")
check("allowed test address", ipaddress.ip_address("192.0.2.20") in approved)
check("outside test address", ipaddress.ip_address("192.0.2.40") not in approved)
private_route_enabled, public_route_allowed = True, True
check("private route does not remove public route", private_route_enabled and public_route_allowed)

per_server_limit, target_fraction, operational_reserve = 200, 0.8, 20
app_processes, per_process_pool = 12, 20
check("pool budget can exceed ceiling", app_processes * per_process_pool + operational_reserve == 260)
pool_cap = int((per_server_limit * target_fraction - operational_reserve) // app_processes)
check("planning cap", pool_cap == 11)
check("cap fits selected target", app_processes * pool_cap + operational_reserve == 152)
check("next cap exceeds selected target", app_processes * (pool_cap + 1) + operational_reserve == 164)


def inventory(pages, expected_count):
    found = {}
    for page in pages:
        for row in page["results"]:
            identity = (row["project"], row["database"], row["username"])
            if identity in found:
                raise ValueError("duplicate identity across pages; reconcile")
            found[identity] = row
    if len(found) != expected_count:
        raise ValueError("incomplete or changing inventory")
    return set(found)


u1 = {"project": "p1", "database": "admin", "username": "reader"}
u2 = {"project": "p1", "database": "$external", "username": "reader"}
u3 = {"project": "p2", "database": "admin", "username": "reader"}
pages = [{"results": [u1, u2]}, {"results": [u3]}]
check("compound identity preserves three users", len(inventory(pages, 3)) == 3)
check("username alone loses identities", len({r["username"] for p in pages for r in p["results"]}) == 1)
rejects("first page is incomplete", lambda: inventory(pages[:1], 3))
rejects("duplicate page rejected", lambda: inventory(pages + pages[:1], 3))
rejects("changed count requires reconciliation", lambda: inventory(pages, 4))

live = sqlite3.connect(":memory:")
snapshot = sqlite3.connect(":memory:")
restored = sqlite3.connect(":memory:")
live.execute("CREATE TABLE balances (id TEXT PRIMARY KEY, cents INTEGER NOT NULL)")
live.executemany("INSERT INTO balances VALUES (?, ?)", [("A", 100), ("B", 200)])
live.commit()
live.backup(snapshot)
live.execute("UPDATE balances SET cents = cents + 50 WHERE id = 'A'")
live.commit()
expected_before_bad_write = [("A", 150), ("B", 200)]
check("known good post-snapshot state", live.execute("SELECT * FROM balances ORDER BY id").fetchall() == expected_before_bad_write)
live.execute("DELETE FROM balances WHERE id = 'B'")
live.commit()
check("bad write is visible", live.execute("SELECT COUNT(*) FROM balances").fetchone()[0] == 1)
snapshot.backup(restored)
check("actual SQLite restore integrity", restored.execute("PRAGMA integrity_check").fetchone()[0] == "ok")
check("snapshot total", restored.execute("SELECT SUM(cents) FROM balances").fetchone()[0] == 300)
check("snapshot misses later good write", restored.execute("SELECT * FROM balances ORDER BY id").fetchall() != expected_before_bad_write)
restored.execute("UPDATE balances SET cents = cents + 50 WHERE id = 'A'")
restored.commit()
check("explicit fixture replay repairs good write", restored.execute("SELECT * FROM balances ORDER BY id").fetchall() == expected_before_bad_write)
check("restore did not mutate source", live.execute("SELECT * FROM balances ORDER BY id").fetchall() == [("A", 150)])
wrong_id_same_totals = [("X", 150), ("B", 200)]
check("count and sum can both agree", len(wrong_id_same_totals) == 2 and sum(v for _, v in wrong_id_same_totals) == 350)
check("identity comparison catches wrong restore", sorted(wrong_id_same_totals) != expected_before_bad_write)

incident_minute, snapshot_minute, latest_recoverable_minute = 137, 120, 135
check("snapshot recovery gap", incident_minute - snapshot_minute == 17)
check("assumed continuous recovery gap", incident_minute - latest_recoverable_minute == 2)
detection, decision, transfer, replay, validation, cutover = 4, 6, 18, 7, 9, 3
check("end-to-end recovery time", sum((detection, decision, transfer, replay, validation, cutover)) == 47)
check("restore job alone understates recovery", transfer + replay == 25 and 47 > 30)


def sustained(samples, limit=80, required=3, spacing=60):
    streak = 0
    previous_time = None
    for timestamp, value in samples:
        contiguous = previous_time is None or timestamp - previous_time == spacing
        streak = streak + 1 if contiguous and value is not None and value > limit else (1 if value is not None and value > limit else 0)
        previous_time = timestamp
        if streak >= required:
            return True
    return False


check("three regular high samples", sustained([(0, 90), (60, 91), (120, 92)]))
check("single spike is insufficient", not sustained([(0, 90), (60, 40), (120, 40)]))
check("missing sample breaks evidence", not sustained([(0, 90), (60, None), (120, 92)]))
check("time gap breaks evidence", not sustained([(0, 90), (120, 91), (180, 92)]))
check("threshold equality is not above", not sustained([(0, 80), (60, 80), (120, 80)]))
for database in (live, snapshot, restored):
    database.close()

print(json.dumps({"passed": len(checks), "checks": checks,
                  "results": {"pool_cap_per_process_per_server": pool_cap,
                              "compound_inventory_count": 3, "restored_cents": 350,
                              "snapshot_gap_minutes": 17, "continuous_gap_minutes": 2,
                              "assumed_recovery_minutes": 47}}, indent=2))
```

## Readiness checks

These are original learning prompts, not recalled exam items. Answer first, then compare the explanation.

1. **Can I distinguish Atlas control-plane and MongoDB data-plane identities and permissions?**

   Atlas identities and roles manage organizations/projects and service configuration; database users and roles govern data operations. Test both planes independently.

2. **Can I explain document, collection, database, replica set, shard, and `mongos` roles?**

   Documents live in collections and databases. Replica sets replicate and elect a primary; shards partition a dataset; mongos routes sharded requests. An Atlas project is a separate control-plane boundary.

3. **Can I safely trace CRUD and aggregation behavior needed for diagnosis?**

   Use synthetic data, narrow filters and predicted identities/counts before running operations. Trace aggregation row grain and review mutation scope; administrative access does not make a broad delete safe.

4. **Can I derive and verify an index from a complete query shape?**

   Record filter, sort, range, projection, distribution and result bound. Compare plans and correct identities under representative data, then measure actual workload latency and write cost.

5. **Can I identify when query/model correction is better than scaling?**

   Prefer a supported correction when a changed query or bad model creates avoidable work. Scale for measured capacity needs; neither option removes correctness or access requirements.

6. **Can I translate availability, latency, residency, growth, and cost into topology choices?**

   Name the failure domain, latency and residency constraints, growth envelope and cost. Pick edition/tier/region/topology only after checking feature eligibility and evidence for that failure.

7. **Can I explain replication, elections, lag, read preference, and concerns conceptually?**

   Replication/elections support continuity but lag and concerns affect observations and acknowledgment. Read preference chooses eligible read targets, not an automatic guarantee of freshness or durability.

8. **Can I compare vertical scale, auto-scaling, and sharding tradeoffs?**

   Vertical scale changes resources; bounded auto-scaling automates eligible adjustments; sharding adds distribution and key/operation complexity. Test reconnect, cost and reversibility for the actual change.

9. **Can I identify shard-key cardinality, targeting, monotonicity, and hotspot risks?**

   Check cardinality, uneven key frequency, monotonic insertion and query targeting together. A numerous key space can still have a hot value or cause scatter/gather reads.

10. **Can I capacity-plan data, indexes, working set, CPU, IOPS, connections, and headroom?**

   Measure peak demand and growth with headroom per resource and server. The original pool exercise totals 260 potential connections against an assumed 200 limit; it is not an Atlas tier specification.

11. **Can I separate organization, project, team, service, and database roles?**

   Organizations/projects scope administration; teams assign workforce roles; service accounts authenticate automation; database roles govern data access. Names alone do not establish effective permissions.

12. **Can I implement and prove least privilege for humans, automation, and applications?**

   Define required actions/resources, assign the narrowest supported role, then test allowed and denied cases with the actual actor. Do not grant Project Owner merely to bypass a documentation ambiguity.

13. **Can I choose an appropriate supported authentication method per actor?**

   Choose an available method for the actor and deployment; API service-account OAuth is different from database authentication. Verify edition/tier/version and lifecycle requirements.

14. **Can I rotate, revoke, and recover credentials without shared accounts?**

   Use separate identities, managed secret storage, planned overlap and revocation evidence. Token issuance does not prove API source authorization or database access.

15. **Can I test effective access and denied operations?**

   Test the intended action and wrong project, database, action and source. Trusted Boolean labels in a local model demonstrate reasoning, not real authentication.

16. **Can I explain why IP access lists are not authentication?**

   An IP list constrains the source that can attempt access. Database identity and authorization remain necessary, and API lists are separate from database connection lists.

17. **Can I compare public lists, peering, and private endpoints including DNS/routing limits?**

   Compare route and trust boundaries, DNS, CIDR overlap, regional reachability, provider ports, tier support and cost. Private endpoints can coexist with public access.

18. **Can I prove intended network paths work and unintended paths fail?**

   Resolve and connect from realistic approved and denied locations using the intended connection string; then test authorized and denied data actions. A successful ping alone is incomplete.

19. **Can I distinguish transit, server-side at-rest, BYOK, and field-level encryption?**

   TLS protects transport; managed storage encryption protects disks/snapshots; customer-managed keys add key ownership and availability obligations; field-level approaches change application/codec responsibilities.

20. **Can I design KMS permission, rotation, deletion-protection, and outage recovery?**

   Define KMS principal/network permissions, valid key versions, rotation, deletion protection and recovery. Network unreachability and invalid/deleted keys have different documented behavior; permanent key loss is not a routine rollback.

21. **Can I define useful service indicators before configuring alerts?**

   Choose service latency/errors/availability and supporting resource/replication/backup signals. State load, window and missing-data behavior before setting thresholds.

22. **Can I correlate metrics, logs, query evidence, releases, and provider events?**

   Build a scoped timeline across application deployment, query shapes, pool counts, resource metrics, replication and provider events. Correlation creates a hypothesis that still needs a controlled test.

23. **Can I turn an alert into an owned actionable runbook?**

   Specify condition, duration/cadence, severity, owner, route, runbook and recovery signal. Three samples a minute apart span two minutes, not proof of three continuous minutes.

24. **Can I evaluate Performance Advisor output rather than apply it blindly?**

   Reproduce the query and verify result semantics, read benefit, write/storage cost and observation window. A recommendation is evidence to review, not a command to apply.

25. **Can I diagnose connection, query, resource, replication, and distribution symptoms?**

   Separate affected client/operation/server and recent changes. Compare pools, scans/sorts, CPU/cache/IO, lag and key distribution; use queued readers/writers for the documented 7.0+ overload distinction.

26. **Can I separate availability, durability, backup, and disaster recovery?**

   Availability concerns continued service; durability concerns acknowledged data; backup offers a recovery point; disaster recovery restores the business service and its dependencies. Replication propagates bad writes too.

27. **Can I map backup schedule/retention/restore capabilities to RPO and RTO?**

   Use actual recoverable timestamps and successful retention/restore evidence. Continuous backup adds oplog replay within a window; snapshot frequency and advertised RPO do not prove the observed gap.

28. **Can I restore into isolation and validate application-level correctness?**

   Prevent client requests to the restore target, isolate side effects and validate exact identities/values, indexes, roles and application behavior. The SQLite counterexample has equal totals with the wrong identity.

29. **Can I plan node, region, network, identity, KMS, and operator-error incidents?**

   Map each failure to detection, decision, dependencies, automation, manual recovery, validation and failback. A multi-AZ layout does not prove uninterrupted application service under every outage.

30. **Can I verify application/driver compatibility before version maintenance?**

   Record server, feature compatibility, driver, CLI and provider versions; review release changes and actual restore compatibility. Current navigation labels and preview announcements are not deployment validation.

31. **Can I navigate core Atlas administration surfaces despite UI label changes?**

   Navigate by intent: projects, deployments, database/network access, backup, metrics, alerts, activity and billing. Verify current labels and required roles rather than memorizing a click path.

32. **Can I use CLI/API with explicit scope, pagination/error handling, and secret safety?**

   Select scope explicitly, use documented output shape and pagination, handle failures and protect secrets. One page is incomplete evidence; list/describe must not be confused with create.

33. **Can I design safe plan/review/apply and drift workflows for IaC?**

   Pin versions, review a concrete plan, protect state/credentials, constrain replacement and reconcile observed state. Provider examples and aliases need version-specific validation.

34. **Can I reconcile emergency UI changes back to managed configuration?**

   Record emergency intent, actor and actual state, then review code changes to reconcile it without overwriting necessary fixes. Preserve audit and recovery evidence.

35. **Can I assign naming, tags, owners, budgets, expiration, and audit controls?**

   Assign owners and lifecycle metadata with budgets/expiry and audit expectations. Tags help accountability but do not by themselves enforce cost or authorization.

36. **Can I review unused/oversized resources without unsafe deletion?**

   Check owner, dependencies, retention, recoverability and protection policies before cleanup. Idle does not mean disposable, and terminating a cluster may leave retained backup costs.

37. **Can I bound automation blast radius with credentials, approvals, and canaries?**

   Use scoped principals, explicit target selection, reviewed changes, canaries and stop/recovery conditions. A broad AWS AdministratorAccess example is not a suitable default.

38. **Can I state which features require paid tiers or an authorized sandbox?**

   Check each feature against edition/tier/provider and current docs. Free lacks cloud backup; private endpoints need eligible dedicated tiers; preview behavior and key/restore support have extra limits.

39. **Can I reconcile every section with the enrolled current objective guide?**

   Retrieve the enrolled canonical document through authorized access and compare every statement to the evidence map. Thirteen public skill summaries are not a completed detailed objective audit.

40. **Can I defend an end-to-end Atlas design and show tested recovery evidence?**

   Present assumptions, rejected alternatives, observed access/performance/recovery results and unresolved limits. Local SQLite/model checks support reasoning but cannot stand in for an Atlas restore or live security test.

## Final preparation

- Enroll in and read the official study guide; map every detailed objective to a section, lab, and evidence artifact.
- Reopen the live exam page and verify contract, delivery, price, accommodations, retake and system-check policies.
- Use the current path and reconcile its 13-hour headline with the 14h05 visible required cards; the separate two-hour exam card differs from the 95-minute exam pages.
- Rebuild one scenario from a clean project using least privilege and recover data into an isolated target.
- Practice timed diagnosis from symptoms and requirements, not memorized UI locations.
- Stop using any source that promises recalled live items, guaranteed passes, or “actual questions.”
- Treat certification as a checkpoint; production changes still require peer review, change control, security, backups, tested rollback, and incident ownership.


## Places to learn

This is not a complete list or a prescription to consume everything. Public outlines and metadata are not proof of lesson quality or exam completeness. Publisher times are labeled; other ranges are study estimates. No paid lesson, practice interior or enrollment was accessed.

| Resource | Access | Estimated time |
|---|---|---|
| [Main exam page](https://learn.mongodb.com/pages/mongodb-associate-atlas-administrator-exam) and [course route](https://learn.mongodb.com/courses/mongodb-associate-atlas-administrator-exam): agree on current public contract | Public browser pages; direct captures are shells | 10–15 min review estimate; both list 95-minute exam |
| [Official study guide](https://learn.mongodb.com/courses/mongodb-associate-atlas-administrator-exam-study-guide): detailed scope still requires reconciliation | Free enrollment listed; public viewer failed and published asset returned 403 | Publisher lists 30 min; objective body unavailable here |
| [Atlas Administrator Path](https://learn.mongodb.com/learning-paths/mongodb-atlas-admin-certification-learning-path): public 13-skill outline, not a substitute for detailed objectives | Free/account learning; advertised 50% full-path completion discount, eligibility unverified | Headline 13 hr; required cards 845 min (14h05); separate 120-min exam card makes 16h05 |
| [Official practice questions](https://learn.mongodb.com/courses/associate-atlas-administrator-practice-questions): public landing only | Free enrollment; questions/explanations not read | Publisher lists 6 hr, plus personal review |
| [August 18 path announcement](https://www.mongodb.com/company/blog/news/introducing-a-more-connected-flexible-path-to-certifications): badge/path context | Public; reading reused from preceding Data Modeler review | Publisher lists 4 min |
| [Atlas overview](https://www.mongodb.com/docs/atlas/) and [security features](https://www.mongodb.com/docs/atlas/setup-cluster-security/): editions, shared responsibility and layered controls | Public; main pages read, not every linked feature | 2–4 hr selected reading/design estimate |
| [Monitoring overview](https://www.mongodb.com/docs/atlas/monitoring-alerts/) and [alert basics](https://www.mongodb.com/docs/atlas/alert-basics/): diagnosis and version-aware signals | Public; no alerts sent or metrics collected | 2–4 hr selected lab estimate |
| [Cloud Backup](https://www.mongodb.com/docs/atlas/backup/cloud-backup/overview/) and [Core restore overview](https://www.mongodb.com/docs/atlas/backup/cloud-backup/restore-overview/): eligibility and recovery evidence | Public; restore command discrepancy recorded | 1–2 hr reading, plus an authorized restore exercise |
| [CLI overview](https://www.mongodb.com/docs/atlas/cli/current/) and [changelog](https://www.mongodb.com/docs/atlas/cli/current/atlas-cli-changelog/): verify version, command purpose and output | Public; selected current changelog entries; no install/auth/CLI execution | 2–4 hr selected lab estimate |
| [AWS landing-zone pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-aws-landing-zone-that-includes-mongodb-atlas.html): supporting architecture by Igor Alekseev and Anuj Panchal; broad example credentials require redesign | Public main read; repository/code not cloned or deployed | 2–4 hr selected reading/paper-lab estimate |
| [The Official MongoDB Guide](https://www.oreilly.com/library/view/the-official-mongodb/9781837021970/): optional broader depth | Paid/O’Reilly; request returned 403, no interior review | Earlier 8h51/2025 metadata not reverified |
| [MongoDB 8.0 in Action, Third Edition](https://www.oreilly.com/library/view/mongodb-8-0-in/9781633436077/): optional administration context | Paid/O’Reilly; request returned 403, no current alignment verified | Earlier 16h46 metadata not reverified |
| [Complete MongoDB Administration Guide](https://www.udemy.com/course/mongodb-essentials-m/): optional task-oriented format | Paid/Udemy; request returned 403, no interior review | Earlier about 11 hr not reverified |

Visible required card minutes are overview 60, CRUD 90, transformation 50, indexing 60, query optimization 90, sharding 90, monitoring 60, performance 60, resilience 45, reliability 90, authentication/authorization 60, networking 45 and encryption 45: 845 minutes. The 13-hour headline and two-hour exam card are separate published measures, not observed study times. The historical May 29 replacement note for the earlier v1 path was not revalidated during this review; use the currently linked path.
