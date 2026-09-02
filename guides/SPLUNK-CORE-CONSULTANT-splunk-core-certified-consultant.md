---
exam_code: SPLUNK-CORE-CONSULTANT
vendor_id: splunk
official_blueprint: https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-consultant.pdf
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Splunk Core Certified Consultant Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live track page, four-page public blueprint, current Splunk Enterprise documentation, and selected resources were checked September 2, 2026. This contains original learning material, not exam items. Recheck the [certification page](https://www.splunk.com/en_us/training/certification-track/splunk-core-certified-consultant.html) and [official blueprint](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-consultant.pdf) before planning or scheduling.

**Current baseline:** Deploying 5%; Monitoring Console 8%; Access/Roles 8%; Data Collection 15%; Indexing 14%; Search 14%; Configuration Management 8%; Indexer Clustering 18%; Search Head Clustering 10%.<br>
**Exam contract:** expert; 86 questions; 120 total minutes including three minutes for the exam agreement.<br>
**Required exams:** Core Power User, Core Advanced Power User, Enterprise Admin, and Enterprise Architect.<br>
**Required instruction/labs:** Indexer Cluster Implementation Lab; Distributed Search Migration Lab; Implementation Fundamentals Lab; Architect Implementation Labs 1–3; Services Core Implementation. Confirm records in the live learning path; these are certification requirements, not optional study suggestions.<br>
**Lifecycle:** active; no retirement/replacement announcement was visible. Blueprint topics can change without notice; implementation details must follow documentation for the deployed version and supported topology.<br>

## How to use this guide

The consultant standard is evidence plus communication. For each lab produce requirements, assumptions, risk, design, implementation plan, acceptance test, operational handoff, and rollback—not only a working command. Use synthetic data and disposable clusters.

> **About related items:** `Related item:` adds practical architecture, governance, security, or current-platform context and is not claimed as verbatim blueprint wording.

## Blueprint map

| Cluster | Weight | Proof |
|---|---:|---|
| Architecture, Monitoring Console, access | 21% | Traceable design, health coverage, effective least privilege |
| Collection and indexing | 29% | End-to-end pipeline evidence and retention/failure tests |
| Search | 14% | Job Inspector-backed optimization and correctness tests |
| Configuration management | 8% | Controlled targeting, canary, drift evidence, rollback |
| Indexer and search-head clusters | 28% | Failure-domain design, lifecycle operations, recovery evidence |

## 1. Deployment evolution, SVA, HA, and DR — 5%

Splunk Validated Architectures are prescriptive reference architectures for proven topology patterns. Use the current SVA version as a starting point; map requirements and exceptions rather than claiming every valid deployment is identical. A standalone instance can combine ingest/index/search for a bounded workload. Growth, concurrency, availability, governance, and operational separation can justify distributed indexing, multiple search heads, indexer clustering, then search-head clustering.

High availability keeps service through component failures within a designed failure domain. Disaster recovery restores service/data after a broader site/region/control-plane event and needs recovery-time/recovery-point objectives, independent dependencies, backups, runbooks, and tests. Replication can support both but does not replace recoverable backup or a DR plan.

> **Related item:** Record SVA deviations with requirement, risk, compensating control, approver, support validation, and review date.

## 2. Monitoring Console — 8%

Use a dedicated Monitoring Console for a substantial distributed environment; avoid placing it where failure or workload makes monitoring unavailable. Configure standalone or distributed mode correctly, register monitored instances/search peers, establish credentials/connectivity, and assign accurate server roles. MC groups scope views and alerts; wrong roles/groups create misleading dashboards.

Health checks combine documented checks over platform telemetry. Learn thresholds, suppression, history, drilldown, and the distinction between symptom and root cause. Extend monitoring with supported custom searches/alerts/dashboards while preserving upgrades and limiting load. Validate that monitoring still works during peer, search-head, network, storage, and certificate failures.

## 3. Access and roles — 8%

Authentication options include local, LDAP, SAML/SSO, and other version-supported methods. LDAP needs TLS/connectivity, bind/search, base DNs, filters/attributes, group-to-role mapping, nested-group handling, timeouts, and rollback. SAML needs metadata/endpoints, entity IDs, signing/encryption certificates, attributes/groups, clock accuracy, session/logout, certificate rollover, and emergency local access.

Roles combine capabilities, allowed/default indexes, search filters/quotas, inheritance, and object permissions. Grants are additive. Design roles from tasks/data boundaries, separate platform/security/content duties, test positive and negative access, protect service/break-glass identities, and monitor identity lifecycle. Search filters are not a substitute for sound index/data architecture in every case.

## 4–5. Collection, S2S, indexing, and retention — 29%

Collection choices include file/monitor, network, HEC, scripted/modular, Windows, API/add-ons, forwarders, and supported collectors. Choose using source support, parsing location, reliability/checkpoint, authentication/TLS, volume, latency, topology, backpressure, data sensitivity, management, and ownership.

Splunk-to-Splunk (S2S) carries forwarded data between Splunk components. Secure/authenticate endpoints, use destination groups/load balancing, understand acknowledgments/queues, and validate events after indexing. Trace faults through source, input, checkpoint, forwarder queues, DNS/network/TLS, receiver, parsing/routing, index, timestamp/metadata, and search. A connected socket is not proof of complete/correct data.

Event processing moves conceptually through input, parsing, and indexing queues. The first full parsing tier determines boundaries, timestamps, metadata transformation/routing, and raw changes; UFs do not perform the full parse. Buckets hold journal/raw data and index structures plus metadata, moving hot → warm → cold → frozen; restored archives use thawed. Know `indexes.conf` retention/size/bucket controls, archive behavior, replication copies, and fishbucket checkpoint purpose.

Retention occurs under the first relevant time/size/storage constraint; frozen deletes by default unless archiving is configured. Build from measured ingest, searchable/total retention, data shape, replication, growth, maintenance/failure reserve, legal/privacy requirements, archive/restore tests, and ownership.

> **Related item:** Prevent or mask sensitive data upstream where possible. Search-time redaction does not remove values already stored in raw buckets.

## 6. Search internals and efficiency — 14%

Know how a search is parsed/planned, dispatched, distributed to peers, processed, reduced/merged, finalized, and retained as a job/artifact. Search categories can include historical versus real-time and transforming versus non-transforming; commands can be distributable streaming, centralized streaming, transforming, generating, or dataset-processing. Classification affects where work runs and data movement.

Job Inspector shows execution phases, component durations/counts, scan/match volume, peer behavior, and messages. Optimize from evidence: narrow time/index/source early; use selective predicates; avoid unnecessary fields/events; choose appropriate commands; manage lookups/knowledge bundles; use summaries/accelerations only with ownership and freshness/cost controls; distribute schedules; and validate semantic equivalence.

Subsearches run separately and inject formatted results into an outer search, with limits/timeouts. Large subsearches can truncate or explode query size. Consider joins/lookups/data models/summary approaches based on semantics, and always test empty, duplicate, high-cardinality, and boundary results.

## 7. Configuration management — 8%

A deployment app is a directory/package of configuration distributed to deployment clients. A deployment server uses server classes to match clients and deliver apps; clients phone home and apply content/restart behavior. Use single-purpose apps, deterministic ownership, precise allow/deny rules, checksums/version labels, canaries, validation, observability, and rollback.

Operate deployment server capacity and security deliberately: client count/phone-home load, network/TLS, content size, app changes, access, backup of authored content and server-class configuration, and separation from unrelated heavy workloads. Inspect actual client/app status and effective `btool` output; “deployed” does not prove desired state. Use tier-specific mechanisms for indexer clusters and SHC rather than deployment server.

## 8. Indexer clustering — 18%

The manager node coordinates peers/buckets; peers ingest/store/search; search heads query the cluster. Replication factor governs total copies and search factor searchable copies. In multisite designs, site RF/SF and site identity place copies across failure domains; consider cross-site bandwidth/latency, search affinity, site-loss capacity, and manager/dependency recovery.

Trace bucket lifecycle, primary/searchable copies, fix-up, generation, and peer state. Failure responses differ for transient offline, maintenance, graceful decommission, forced removal, storage loss, manager loss, and site loss. Preserve cluster health, use supported offline/decommission commands, monitor fix-up, and avoid taking away more capacity than RF/SF and workload permit.

Migration demands source/target compatibility, capacity, network, data movement path, cluster/search configuration, apps, certificates, health gates, rollback point, and acceptance tests. Common patterns—standalone/distributed to cluster, single-site to multisite, hardware/storage changes—have different supported procedures. Follow current docs; never improvise bucket copying.

## 9. Search-head clustering — 10%

Use SHC when coordinated search-head availability, configuration replication, and scheduler behavior justify the operational complexity. It may not suit tiny workloads, unsupported apps/topologies, or cases where independent search heads meet requirements. Members share a security key and replication port, elect a captain with RAFT, and sit behind a health-aware load balancer.

The captain coordinates cluster activities and scheduling; it is not a fixed primary. The deployer distributes supported app/configuration bundles; user/runtime artifacts replicate within the cluster. Test election/quorum, captain/member loss, artifact replication, scheduler behavior, bundle compatibility, search-peer connectivity, and load-balancer draining. Use supported member add/remove and captaincy transfer procedures.

> **Related item:** SHC availability still depends on external identity, DNS/load balancing, search peers, KV Store health, certificates, and network; include them in failure tests.

## Integrated scenarios

### Scenario 1: Standalone-to-cluster migration

Turn measured growth/availability requirements into an SVA-aligned design. Plan indexes, S2S, config distribution, identity, MC, single-/multisite RF/SF, SHC, migration stages, acceptance gates, rollback, handoff, and capacity triggers.

### Scenario 2: Missing-data incident

Trace synthetic loss across source, monitor checkpoint, UF queues, S2S/TLS, parsing/routing, bucket/index, retention, and permissions. Use MC/internal evidence; avoid resets that create duplicates; prove recovery and prevention.

### Scenario 3: Search degradation after deployment

Correlate server-class/app rollout with Job Inspector, MC, peer/SHC health, bundles, scheduler, and resource telemetry. Roll back safely, establish root cause, and redesign the canary gate.

## Hands-on labs

1. SVA fit/gap and HA-versus-DR requirements matrix.
2. Configure MC roles/groups and extend one health check/alert safely.
3. Implement/test LDAP or SAML mapping, least-privilege roles, and break-glass rollback.
4. Compare five input types and failure-test one S2S pipeline.
5. Trace raw bytes through parsing/index artifacts and test retention/archive/thaw.
6. Optimize three searches from Job Inspector evidence, including a bounded subsearch rewrite.
7. Deliver a deployment app via canary server class; detect drift and roll back.
8. Build/failure-test single-site indexer cluster RF/SF and peer lifecycle.
9. Design/test multisite site-loss capacity and recovery.
10. Build/failure-test SHC election, member lifecycle, deployer content, and load balancer.
11. Plan and rehearse a standalone-to-distributed migration with health gates.
12. Produce a consultant handoff: as-built, credentials ownership, runbooks, monitoring, risks, and acceptance signatures.

## Original readiness checks

1. What is an SVA? 2. When should standalone evolve? 3. How do HA and DR differ? 4. Why dedicate MC? 5. What do MC roles/groups control? 6. Why can a green health check still need investigation? 7. What belongs in LDAP configuration? 8. What belongs in SAML certificate rollover? 9. Why is role access additive? 10. Which negative access tests matter? 11. What factors choose an input type? 12. What is S2S? 13. Why is connectivity insufficient ingest validation? 14. How should a missing event be traced? 15. Name three pipeline phases. 16. Where does full parsing begin? 17. Name bucket lifecycle states. 18. Which constraints enforce retention? 19. Why is search-time masking inadequate? 20. What does Job Inspector reveal? 21. How do streaming and transforming commands differ operationally? 22. Why can a subsearch truncate? 23. What should search optimization preserve? 24. What is a deployment app? 25. What does a server class do? 26. Why verify `btool` after deployment? 27. Which tools distribute indexer/SHC content? 28. RF versus SF? 29. What additional concerns enter multisite? 30. Why distinguish offline from decommission? 31. What must a migration gate prove? 32. Why not copy buckets manually? 33. When is SHC not recommended? 34. What does the captain do? 35. What does the deployer own? 36. What does RAFT provide? 37. Which objective has the largest weight? 38. What are all prerequisite exams? 39. What are the prerequisite labs/course groups? 40. What must be rechecked before scheduling?

## Answer key

1. A Splunk-validated reference architecture. 2. When measured scale, concurrency, availability, governance or isolation requires it. 3. Continuity within failures versus recovery after broad disaster against RTO/RPO. 4. Preserve monitoring availability/capacity and role clarity. 5. Which instances are classified and which views/alerts apply. 6. Threshold coverage can miss new or cross-system failure modes. 7. TLS/bind/search/base/filter/attributes/groups/roles/timeouts/rollback. 8. New/old metadata, signing trust, timing, validation and emergency access. 9. Assigned/inherited grants combine. 10. Forbidden indexes/capabilities/objects and privilege escalation. 11. Support, checkpoint/reliability, security, volume, parsing, topology, management. 12. Splunk-to-Splunk forwarded-data protocol/path. 13. It does not prove parsing/routing/indexing/time/metadata/search. 14. Source through input/checkpoint/queues/network/TLS/receiver/parse/route/index/access. 15. Input, parsing, indexing. 16. First full parsing tier, not UF. 17. Hot/warm/cold/frozen/thawed. 18. First applicable time/size/storage policy. 19. Raw value is already stored. 20. Search phases, durations/counts, peers/messages and costs. 21. Where/how much data processes and centralizes differs. 22. Result/time limits and formatting into outer query. 23. Semantics, permissions, time range, freshness and correctness. 24. Managed configuration package delivered to clients. 25. Selects clients/apps. 26. Delivery is not proof of effective precedence/state. 27. Manager-node bundle and SHC deployer. 28. Total copies versus searchable copies. 29. Site RF/SF, bandwidth/latency, affinity, site-loss capacity/dependencies. 30. Temporary maintenance and permanent copy-safe removal need different workflows. 31. Compatibility, capacity, health, data/search correctness, rollback. 32. Unsupported movement can corrupt/invalidate cluster state. 33. Small/unsupported/operationally unjustified cases. 34. Coordinates cluster/scheduling activities. 35. Supported SHC configuration/app bundles. 36. Captain election/consensus behavior. 37. Indexer Clustering, 18%. 38. Core Power User, Advanced Power User, Enterprise Admin, Enterprise Architect. 39. Indexer Cluster, Distributed Search Migration, Implementation Fundamentals, Architect Implementation 1–3, Services Core Implementation. 40. Live page/blueprint, prerequisites, release docs, price/delivery/retake/renewal.

## Final readiness checklist

- [ ] I can translate stakeholder requirements into an SVA-aligned design and HA/DR contract.
- [ ] I can configure MC and prove monitoring through failures.
- [ ] I can secure identity/data access and trace ingestion/indexing end to end.
- [ ] I can improve searches using Job Inspector without changing semantics.
- [ ] I can govern deployment server and tier-specific configuration safely.
- [ ] I can design, migrate, failure-test, and operate indexer and search-head clusters.
- [ ] I completed all labs and can produce a clear consultant handoff.
- [ ] Every required exam, course, and lab is recorded complete.

## Places to learn

This is not a complete list, and it is not meant to be consumed end to end. Choose resources for measured gaps. Times are planning estimates; access, price, version, and schedules change.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official certification page](https://www.splunk.com/en_us/training/certification-track/splunk-core-certified-consultant.html) and [blueprint](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-consultant.pdf) | Free | 60–90 min | Canonical scope/prerequisites |
| [Splunk Enterprise docs](https://help.splunk.com/en/splunk-enterprise) | Free | 35–70 hr targeted | Deployed release and clustering/admin/search manuals |
| Required five course/lab groups in the official learning path | Paid and often partner/employer-gated | 40–80+ hr | Required learning; verify current delivery/duration |
| [Splunk Validated Architectures](https://help.splunk.com/en/splunk-enterprise/get-started/splunk-validated-architectures/introduction-to-splunk-validated-architectures/about-splunk-validated-architectures) | Free | 5–10 hr | Verify edition and applicability |
| [Splunk How-To YouTube channel](https://www.youtube.com/@SplunkHowTo) | Free | 6–15 hr selected | Supplement; verify age/version |
| Multi-node disposable implementation portfolio | Infrastructure/software terms vary | 60–120 hr | Synthetic data and repeatable rebuilds |
| [Splunk Community](https://community.splunk.com/) | Free | 5–12 hr targeted | Corroborate with official docs |
