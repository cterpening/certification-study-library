---
exam_code: C1000-184
vendor_id: ibm
official_blueprint: https://www.ibm.com/training/credentials/getExam/C1000-184
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-04
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-04
---

# C1000-184 IBM Db2 13 for z/OS Database Administrator Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide maps the live IBM exam contract checked September 4, 2026. It is unofficial and may contain errors. The [official C1000-184 exam record](https://www.ibm.com/training/credentials/getExam/C1000-184) is authoritative.

**Assessment contract:** 60 questions; 44 required to pass; 90 minutes.<br>
**Product baseline:** Db2 13 for z/OS.<br>
**Current status:** Live; no replacement or withdrawal notice appeared when checked.

## How to use this guide

Study each database change through object design, authority, SQL/application behavior, concurrency, logging/recovery, utilities, catalog evidence, access path, monitoring, and rollback. Use a sanctioned training subsystem or simulations; never experiment on production z/OS.

> **About related items:** A `Related item:` callout adds mainframe operations or database-design context. It is supporting knowledge, not a claim that its wording appears in the official objectives.

## Objective map

| Official domain | Weight | Central question |
|---|---:|---|
| Planning | 12% | How do subsystem settings, address spaces, migration, and data sharing shape operation? |
| Operations | 20% | Can the subsystem connect, start, stop, log, recover, and run utilities safely? |
| Security | 5% | Are privileges granted through the intended authorization hierarchy? |
| Database Design | 20% | Do relational objects, types, keys, and relationships support integrity and access? |
| Application Development | 21% | How do DML, routines, triggers, static/dynamic SQL, and BIND affect execution? |
| Data Concurrency | 12% | Do locking, isolation, and units of work balance integrity and availability? |
| Performance | 10% | Can EXPLAIN, statistics, traces, and reports support an access-path decision? |

## 1. Planning

Subsystem parameters (zparms) control operational behavior and require change ownership, dependency review, activation method, and rollback. Identify major Db2 address spaces and their purposes conceptually: system services, database services, IRLM lock management, distributed access, and stored-procedure/user-managed work. Diagnose by function rather than memorizing names alone.

Migration uses supported modes and Db2 continuous delivery introduces function through maintenance and activation levels. Separate code maintenance from function activation and application compatibility. Data sharing coordinates members over shared data with coupling-facility structures and group-level recovery/concurrency implications; plan member resilience, workload routing, catalog/directory, logs, and retained evidence.

## 2. Operations

Connections may be local or distributed; verify identity, location/alias, protocol, package/plan, authorization, and application compatibility. Distinguish Db2 commands, DSN subcommands, SQL, and z/OS commands by control plane and context.

Understand normal startup phases and dependencies, controlled shutdown, restart, and outstanding recovery. Logging supports rollback, restart, recovery, and audit needs. Recovery design ties image copies, logs, catalog information, utilities, recovery points, object dependencies, and tested procedures to RTO/RPO.

Utilities perform copy, recover, reorganize, load/unload, run statistics, check, repair, and related maintenance. Choose based on goal, object state, availability, concurrency, restartability, resources, and post-utility actions. Read utility control/output and verify object status. The catalog/directory describe definitions, packages, privileges, statistics, and internal structures; query documented catalog interfaces rather than altering internal data.

> **Related item:** A successful utility return code does not alone prove service recovery. Verify object status, data reconciliation, applications, replicas/data-sharing members, and follow-up statistics or copies.

## 3. Security

Use DCL `GRANT` and `REVOKE` with primary/secondary authorization IDs, roles, trusted contexts, ownership, administrative/system authorities, object privileges, and package/plan execution concepts. Apply least privilege and group/role-based administration where appropriate. Trace both privilege source and downstream dependency before revocation.

## 4. Database design

Relational design uses tables, columns, rows, keys, constraints, indexes, views, aliases/synonyms, databases, table spaces, and storage attributes. Select data types for domain, precision, scale, encoding, length, time, nullability, and application compatibility. Primary/unique keys enforce uniqueness; foreign keys describe referential relationships; checks enforce predicates.

Normalize to reduce anomalies, then denormalize only for measured needs with integrity ownership. DDL creation and alteration have dependency, availability, package, recovery, and utility implications. Define table-space/index organization from access, volume, growth, partitioning, maintenance, and recovery requirements.

## 5. Application development

DML retrieves and changes data through `SELECT`, `INSERT`, `UPDATE`, `DELETE`, and `MERGE` patterns. Validate predicates, null logic, join cardinality, transaction boundaries, host-variable types, error/SQLCODE handling, and affected row counts. Stored procedures encapsulate callable work, UDFs add reusable functions, and triggers respond to data events; all introduce authority, determinism/side-effect, dependency, and performance considerations.

Static SQL is prepared into packages and controlled through program preparation/BIND options; dynamic SQL is prepared at runtime. Understand precompile/compile-link/bind concepts, DBRMs/packages/plans/collections at a high level, versioning, rebind, invalidation, and application compatibility. Validate SQL execution with syntax/prepare, test data, EXPLAIN, runtime evidence, and transaction outcome.

## 6. Concurrency

Locks protect resources at granularities and modes that determine compatibility. Contention can produce waits, timeouts, or deadlocks. Isolation levels trade consistency guarantees against concurrency; choose from business correctness, not speed alone. Commit releases eligible resources and ends a unit of work; rollback reverses uncommitted changes. Keep units of work bounded and handle retry only when operations are safe/idempotent.

## 7. Performance

EXPLAIN records optimizer access-path information; statistics describe data distribution/cardinality; traces and reports show runtime behavior. An access path may use indexes, scans, join methods/order, sort, or parallelism. Diagnose from workload and elapsed/CPU/I/O/lock evidence. Refresh appropriate statistics and compare the same workload before and after a controlled change; do not force a path from one anecdote.

## Integrated practice scenarios

1. **Online table change:** Assess DDL/dependencies, authority, package effects, utilities, concurrency, recovery, statistics, access path, and rollback.
2. **Slow distributed query:** Validate connection/package, SQL predicates/types, catalog statistics, EXPLAIN, runtime traces, locks, and measured remediation.
3. **Recovery exercise:** Define failure point and objectives, choose copies/logs/utilities, recover dependencies in order, and prove data/application availability.

## Hands-on labs

1. Draw address-space, connection, log, catalog/directory, and data-sharing roles for a training subsystem.
2. Build a startup/shutdown/restart checklist and map staged status messages to responsible components.
3. Plan and simulate COPY/REORG/RUNSTATS/RECOVER choices for objects with availability constraints.
4. Create related tables with appropriate types, keys, constraints, indexes, and sample integrity failures.
5. Grant and revoke controlled privileges through users/roles and trace effective authority.
6. Write DML, a routine/trigger design, and static-versus-dynamic execution notes with error handling.
7. Reproduce a lock wait/deadlock in a disposable lab or simulation; compare isolation and commit choices.
8. Capture EXPLAIN/statistics/runtime evidence for a query, change one factor, and compare the same workload.

## Original readiness checks

1. Why control zparm changes? 2. IRLM purpose? 3. Continuous-delivery distinction? 4. Data-sharing concern? 5. Db2 command versus SQL? 6. What supports point recovery? 7. Utility-selection factors? 8. Why not update catalog internals? 9. Privilege versus authority? 10. Foreign-key purpose? 11. Why choose exact data types? 12. DDL dependency risk? 13. Static versus dynamic SQL? 14. BIND purpose? 15. Trigger risk? 16. Unit of work? 17. Timeout versus deadlock? 18. Isolation tradeoff? 19. EXPLAIN versus trace? 20. What proves a tuning improvement?

### Answer guide

1. They affect subsystem-wide behavior and activation/rollback. 2. Db2 lock management. 3. Maintenance/code level versus activated function/application compatibility. 4. Shared locking/cache/recovery/member coordination. 5. Subsystem control versus relational data/object operation. 6. Image copies, logs, metadata, utilities, and tested sequence. 7. Goal, state, availability, concurrency, resources, restartability, and follow-up. 8. It is unsupported and risks subsystem integrity. 9. Object action permission versus broader administrative capability. 10. Enforce/describe referential integrity. 11. Integrity, precision, storage, comparison, index, and application behavior. 12. Objects, packages, availability, utilities, and recovery may be affected. 13. Bound package execution versus runtime preparation. 14. Create/control packages and execution options. 15. Hidden side effects, recursion, authority, dependencies, and performance. 16. Work bounded by commit or rollback. 17. Wait exceeds limit versus cyclic wait victim detection. 18. Consistency guarantees versus concurrency. 19. Optimizer access-path record versus runtime event evidence. 20. Repeated comparable workload shows desired gain without integrity/availability regression.

## Readiness checklist

- I can connect planning, operations, design, SQL, locking, and performance decisions.
- I select utilities from availability and recovery requirements.
- I understand static/dynamic SQL and package/BIND consequences.
- I diagnose access paths with statistics and runtime evidence.
- I can complete 60 mixed questions in 90 minutes from an administrator's model.

## Places to learn

This is a selective learning path, not a complete list of Db2 for z/OS resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official C1000-184 exam record](https://www.ibm.com/training/credentials/getExam/C1000-184) | Public | **25 minutes** for contract and objectives |
| [IBM Db2 13 for z/OS documentation](https://www.ibm.com/docs/en/db2-for-zos/13.0.0) | Public; automation may be blocked | **28–44 hours** for selected administration topics |
| Eight labs in this guide | Authorized z/OS training environment or simulation | **24–40 hours** plus one timed review |
