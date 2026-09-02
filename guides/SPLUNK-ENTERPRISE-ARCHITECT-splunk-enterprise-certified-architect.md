---
exam_code: SPLUNK-ENTERPRISE-ARCHITECT
vendor_id: splunk
official_blueprint: https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-architect.pdf
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Splunk Enterprise Certified Architect Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live certification page, five-page public blueprint, current Splunk Enterprise documentation, and selected resources were checked September 2, 2026. This is original learning material, not an exam dump. Recheck the [certification page](https://www.splunk.com/en_us/training/certification-track/splunk-enterprise-certified-architect.html) and [official blueprint](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-architect.pdf) before planning or scheduling.

**Current baseline:** 20 domains totaling 100%; the largest are Resource Planning and Indexer Cluster Management (7% each), Forwarder/Deployment Best Practices (6%), with most remaining domains at 5%, KV Store 3%, and Introduction 2%.<br>
**Exam contract:** expert; 85 questions; 90 total minutes including three minutes for the exam agreement.<br>
**Required exams:** Splunk Core Certified Power User and Splunk Enterprise Certified Admin.<br>
**Required instruction:** Architecting Splunk Enterprise Deployments; Troubleshooting Splunk Enterprise; Splunk Enterprise Cluster Administration; and Splunk Enterprise Deployment Practical Lab. These are certification prerequisites, not optional recommendations; confirm completion records in the official learning path.<br>
**Lifecycle:** active; no retirement/replacement announcement was visible. The blueprint retains historical terms such as “license master” and “master app bundles”; current documentation generally uses **license manager** and **manager-node app bundle** terminology. Learn the published objective wording while using the supported terms and commands for your deployed release.<br>

## How to use this guide

Architecture answers begin with requirements and failure domains, then produce a supportable design plus evidence. Build a disposable multi-instance lab; snapshot it; automate repeatable builds; inject failures; measure recovery; and record rollback. Do not infer production sizing solely from a small lab.

> **About related items:** A `Related item:` callout adds architecture, security, governance, or current-product context. It does not claim the exact phrase is in the public blueprint.

## Blueprint map

| Capability | Weight | Evidence |
|---|---:|---|
| Plan, requirements, index/resource sizing | 19% | Requirements trace, assumptions, capacity model, index/app design |
| Clustering and deployment practices | 11% | Failure-domain topology and tier-specific configuration flow |
| Performance and troubleshooting | 35% | Baseline, hypothesis tree, diagnostics, controlled remediation |
| Large-scale/indexer clustering | 22% | Single-/multisite design, bundle, maintenance, monitoring evidence |
| Search-head clustering and KV Store | 13% | SHC lifecycle/failover and KV Store recovery plan |

## 1–4. Requirements, indexes, resources, and deployment planning — 19%

A deployment plan names outcomes, stakeholders, scope, assumptions, dependencies, environments, topology, security/compliance, migration, test/acceptance criteria, operations, training, cutover, rollback, and risks. The process should move from discovery and measurement through logical/physical design, validated build, data/search migration, performance/failure tests, controlled cutover, handoff, and iterative capacity review.

Gather peak and average ingest by data type, retention/searchable/archival periods, event shape, source count and geography, concurrent/scheduled searches, acceleration and summary needs, user/role model, apps (especially ES/ITSI), availability/recovery objectives, network/storage constraints, growth, maintenance windows, security/privacy, and operational maturity. Mark every figure measured, contractual, assumed, or estimated.

Index boundaries follow retention, access, data type, ownership, and operational needs—not one index per source. For non-SmartStore sizing, model daily ingest, retention by tier, compression/index overhead measured from representative data, replication factor, high-water marks, filesystem reserve, growth, rebuild/maintenance headroom, and archive/thaw. Separate storage capacity from IOPS/latency and search compute.

Resource sizing starts from the current official sizing guidance and app-specific guidance. CPU, memory, disk, network, scheduler/concurrency, data models, knowledge bundles, replication, and management roles interact. ES and ITSI add substantial workload/topology requirements; use their current sizing calculators/guides and measured searches/entities/data models rather than a generic multiplier.

Security design covers identities, least privilege, TLS/certificate lifecycle, encryption/storage, network segmentation, management-plane isolation, secrets, app/supply-chain review, audit, privacy minimization/retention, integrity, backup/recovery, hardening, and support access.

> **Related item:** A useful capacity model includes confidence ranges and trigger points. “Add capacity when X reaches Y for Z duration” is more operational than a single three-year number.

## 5–6. Cluster and deployment foundations — 11%

Indexer clustering provides replicated raw/indexed data and searchable copies across peer nodes, coordinated by a manager node. Replication factor and search factor describe different requirements. Site awareness maps copies across failure domains; storage must account for configured copies plus bucket state, maintenance, and reserve. Search-head clustering provides coordinated member availability and replicated search artifacts, with a captain and a separate deployer for supported app distribution.

Forwarder tiers should minimize parsing hops, avoid single points of failure, use load-balanced destinations/TLS, isolate special collection where justified, and make queue/throughput/failure behavior observable. Configuration distribution is tier-specific: deployment server for supported clients, manager-node bundle for indexer peers, deployer for SHC members, and other supported mechanisms for standalone/management roles. Never send all content through one tool indiscriminately.

## 7–13. Performance and evidence-led troubleshooting — 35%

Establish baseline workload and health before tuning. `limits.conf` controls many concurrency/resource limits; raising one value can move contention elsewhere. `indexes.conf` bucket sizing affects rolling, recovery, search parallelism, and storage overhead. `props.conf` parsing changes can alter CPU, event quality, or irreversible stored data. Improve searches first through time/index constraints, selective predicates, appropriate commands, field/data-model strategy, schedule distribution, and Job Inspector evidence.

Use a disciplined loop: define expected/actual and impact; bound time/users/hosts/data/searches; identify recent changes; reproduce safely; form competing hypotheses; collect evidence; change one variable; validate side effects; roll back; document root cause/prevention. Useful tools include Monitoring Console, health checks, internal indexes/logs, Job Inspector, REST/CLI status, `btool --debug`, `splunk diag`, operating-system/storage/network telemetry, and support-approved debug logging. Redact secrets and personal data from diagnostics.

Know internal evidence: `$SPLUNK_HOME/var/log/splunk` contains component logs, while `_internal`, `_audit`, and telemetry/introspection indexes expose platform activity subject to role/retention. Licensing issues require entitlement/usage/pool/time-window evidence. Crashes require exact time, component/version, workload, resource pressure, crash files/core policy, and recurrence—not a blind restart.

For inputs, trace source availability, permissions, checkpoint, queues, parsing tier, routing, index, and searchable event. For search, separate SPL correctness, permissions, scheduling/concurrency, knowledge bundle, peer availability, storage, and expensive operators. For forwarding and deployment server, test network/TLS, outputs, queues, target groups/server classes, phone-home, app checksum/state, restart, and effective configuration.

> **Related item:** Observability of the platform should survive a tier failure. Keep time synchronization, external infrastructure telemetry, certificate/secret expiry monitoring, and tested escalation paths.

## 14–17. Large-scale and indexer-cluster architecture — 22%

Map every role and its failure domain: manager node, peer nodes, search heads/SHC, deployer, deployment server, license manager, monitoring console, forwarder/collection tiers, and optional app-specific roles. The blueprint says “License Master”; current term is **license manager**. Avoid unsupported role co-location and document dependencies during restart, maintenance, and disaster.

In a single-site cluster, choose replication/search factors, peer count, storage, discovery, management/search connectivity, and maintenance workflow. Validate primary-bucket handling, searchable factor, peer loss, fix-up, restart, rolling upgrade, and manager recovery. In multisite, configure site IDs, site-aware replication/search factors, search affinity where supported, cross-site bandwidth/latency, and explicit site-failure capacity. A site does not automatically equal a full disaster-recovery design.

Upgrades/migrations require a supported version path, compatibility matrix, app/add-on checks, backups, health gates, rollback boundary, rolling procedure, adequate replication/search health, and acceptance tests. Never take a peer offline by simply stopping or deleting it when maintenance/decommission commands and cluster state are required. Graceful decommission preserves/rebuilds required copies; forced paths are exceptional and risk-bearing.

Manager-node app bundles distribute indexer-cluster configuration. Validate the bundle, scope only peer-compatible content, apply through the supported command, monitor restart/rolling behavior and cluster health, and retain rollback. Monitoring Console should track RF/SF health, fix-up queues, bucket/peer state, disk, indexing/search load, and manager health.

> **Related item:** SmartStore changes local-cache and remote-object-storage capacity/failure models. The blueprint explicitly asks some **non-SmartStore** sizing; do not substitute one model for the other.

## 18–20. Search-head clusters and KV Store — 13%

An SHC uses an odd-sized supported member set, shared security key, replication port, captain election, and load-balanced user access. The captain coordinates activities; it is not a permanent manually chosen “primary.” A deployer distributes supported configuration bundles, while runtime search artifacts replicate within the cluster. Validate captain election, member loss/rejoin, replication status, scheduler behavior, load balancer health, and search-peer connectivity.

Use supported member addition/removal and captaincy-transfer procedures, checking cluster health and artifact replication before and after. Maintenance mode and forced actions solve specific conditions, not routine shortcuts. Preserve user/search availability and session/load-balancer behavior during change.

KV Store backs collections used by apps and lookups and has its own replication, storage, backup/restore, compatibility, and health concerns in an SHC. Inventory collection owner/schema/size/TTL and app dependencies; monitor status; use supported backup/restore/migration; and test recovery. KV Store replication is not a substitute for recoverable backups.

## Integrated scenarios

### Scenario 1: Multisite security analytics platform

Turn measured ingest, ES search/data-model workload, retention, two-site failure objectives, privacy, and growth into a topology, RF/SF/site policy, storage/network model, deployment flows, acceptance tests, and expansion triggers.

### Scenario 2: Cluster upgrade with failure injection

Validate compatibility and bundles; back up management/KV Store/content; establish health gates; perform a supported rolling upgrade; inject peer and SHC-member loss; prove search/ingest/recovery; document rollback cutoff.

### Scenario 3: Slow-and-incomplete search incident

Use Job Inspector, internal logs/indexes, cluster health, bundle status, storage/network telemetry, and effective config to distinguish SPL, peer, bucket, permissions, and resource hypotheses. Make one measured correction and capture prevention.

## Hands-on labs

1. Requirements interview and traceability matrix with assumptions/confidence.
2. Non-SmartStore index/storage/compute/network sizing model with growth and failure headroom.
3. ES/ITSI topology delta using their current official sizing guidance.
4. Tier-specific configuration-delivery matrix and canary/rollback.
5. Baseline and tune one search using Job Inspector; reject a harmful limit increase.
6. Diagnose license, crash, input, search, forwarder, and deployment-server synthetic faults.
7. Build and failure-test a single-site indexer cluster.
8. Convert it to/design a multisite cluster and calculate site-loss capacity/bandwidth.
9. Validate and deploy a manager-node bundle, then roll it back.
10. Gracefully take a peer offline and decommission a disposable peer.
11. Build/failure-test an SHC; transfer captaincy and add/remove a member via supported workflows.
12. Back up, modify, restore, and validate a synthetic KV Store collection.

## Original readiness checks

1. What belongs in a deployment plan? 2. Which requirement figures must be labeled assumptions? 3. Which boundaries justify separate indexes? 4. Why must non-SmartStore sizing include replication and reserve? 5. How do capacity and IOPS differ? 6. Why do ES/ITSI need app-specific sizing? 7. What security controls protect the management plane? 8. How do replication factor and search factor differ? 9. What does site awareness model? 10. Which tool distributes apps to UFs? 11. Which mechanism distributes indexer-peer configuration? 12. Which mechanism serves SHC members? 13. Why can raising `limits.conf` worsen performance? 14. What should precede tuning? 15. What does Job Inspector establish? 16. Name three internal evidence sources. 17. What belongs in a crash evidence package? 18. Why is restart not root-cause analysis? 19. How should an input fault be traced? 20. How do forwarding and deployment-server faults differ? 21. What is the current term for license master? 22. Which roles should a cluster topology show? 23. What must single-site failure testing prove? 24. What extra constraints enter multisite design? 25. Why is multisite not automatically DR? 26. What are upgrade health gates? 27. Why is `stop` not a decommission plan? 28. What is in a manager-node app bundle? 29. What should Monitoring Console show for an indexer cluster? 30. How does SmartStore change sizing? 31. What does an SHC captain coordinate? 32. Why should a load balancer health-check SHC members? 33. What does a deployer not own? 34. What must be checked before member removal? 35. What does KV Store hold? 36. Why does replication not replace backup? 37. Which domains weigh 7%? 38. Which domain weighs 2%? 39. What are the four required course/lab items? 40. What must be rechecked before scheduling?

## Answer key

1. Outcomes through requirements/design/build/test/cutover/rollback/operations/risks. 2. Any unmeasured workload, growth, compression, concurrency, or recovery input. 3. Retention, access, data type, ownership, operations. 4. Copies, lifecycle, maintenance and failure capacity consume disk. 5. Space versus operation rate/latency. 6. Their searches, entities/data models and components materially change load. 7. Segmentation, least privilege, TLS, secrets, hardening, audit, resilient access. 8. Total raw copies versus searchable copies. 9. Failure domains and placement. 10. Deployment server. 11. Manager-node app bundle. 12. SHC deployer bundle. 13. It moves contention to CPU/memory/I/O/scheduler. 14. A representative baseline and hypothesis. 15. Search phases/costs and execution evidence. 16. Splunk logs, `_internal`, `_audit`, Monitoring Console/diag; any three. 17. Exact time/version/component/workload/resources/crash artifacts/recurrence. 18. It removes symptoms without explaining/preventing them. 19. Source through permissions/checkpoint/queues/parsing/routing/index/search. 20. Data-path/TLS/queues versus client targeting/phone-home/app state. 21. License manager. 22. Manager, peers, search heads/SHC, deployer, deployment server, license manager, Monitoring Console, collection tier. 23. Ingest/search continuity, RF/SF repair, peer/manager recovery. 24. Site RF/SF, bandwidth/latency, affinity, independent capacity and operations. 25. Dependencies, control planes and recovery objectives may still span/fail across sites. 26. Compatibility, backups, healthy replication/search, capacity, acceptance and rollback checks. 27. It can strand required copies and violate safe cluster state. 28. Supported peer configuration/apps. 29. RF/SF, fix-up, bucket/peer/disk/load/manager health. 30. Remote object storage and local cache replace parts of classic local-tier math. 31. Cluster activities/election/scheduling coordination. 32. To avoid routing users to unavailable/unready members. 33. Runtime replicated search artifacts/user content. 34. Health, artifact replication, captain/member state, capacity, load-balancer/drain plan. 35. App collections and lookup-like structured records. 36. Corruption/operator error can replicate; restore needs an independent recovery point. 37. Resource Planning and Indexer Cluster Management. 38. Introduction. 39. Architecting, Troubleshooting, Cluster Administration, Deployment Practical Lab. 40. Live blueprint/page, all prerequisites, product-version docs, price/delivery/renewal/retake.

## Final readiness checklist

- [ ] I can turn measured requirements into a traceable, secure, supportable capacity/topology plan.
- [ ] I can distinguish classic storage from SmartStore and all tier-specific configuration flows.
- [ ] I can baseline, diagnose, tune, and prove root cause across the blueprint failure classes.
- [ ] I can build, operate, upgrade, and failure-test single-/multisite indexer clusters and SHC.
- [ ] I can safely manage peer/member lifecycle, bundles, captaincy, and KV Store recovery.
- [ ] I completed the twelve labs and can defend decisions with evidence and rollback.
- [ ] Both prerequisite certifications and all four required course/lab records are complete.

## Places to learn

This is not a complete list, and it is not meant to be consumed end to end. Pick resources for measured gaps. Times are planning estimates; access, price, version, and schedules change.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official certification page](https://www.splunk.com/en_us/training/certification-track/splunk-enterprise-certified-architect.html) and [blueprint](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-architect.pdf) | Free | 60–90 min | Canonical prerequisites/scope; recheck before scheduling |
| [Splunk Enterprise documentation](https://help.splunk.com/en/splunk-enterprise) | Free | 30–60 hr targeted | Deployed release and clustering/admin manuals |
| Required Architecting, Troubleshooting, Cluster Administration courses and Deployment Practical Lab | Paid/partner/employer access | Roughly 35–60 hr total | Required completion; verify current delivery/durations |
| [Splunk Validated Architectures](https://help.splunk.com/en/splunk-enterprise/get-started/splunk-validated-architectures/introduction-to-splunk-validated-architectures/about-splunk-validated-architectures) | Free | 4–8 hr selected | Validate currency and applicability; not a sizing substitute |
| [Splunk How-To YouTube channel](https://www.youtube.com/@SplunkHowTo) | Free | 5–12 hr selected | Supplement; verify version/UI age |
| Disposable multi-node lab and failure journal | Infrastructure/software terms vary | 45–90 hr | Synthetic data and automated rebuilds |
| [Splunk Community](https://community.splunk.com/) | Free | 4–10 hr targeted | Corroborate answers with current official docs |
