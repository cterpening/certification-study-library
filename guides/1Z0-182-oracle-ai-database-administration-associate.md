---
exam_code: 1Z0-182
vendor_id: oracle
official_blueprint: https://mylearn.oracle.com/ou/learning-path/earn-the-oracle-ai-database-administration-associate-credential/140076
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-04
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-04
---

# 1Z0-182 Oracle AI Database Administration Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide maps Oracle University's current public learning-path scope checked September 4, 2026. It is unofficial and may contain errors. The [official Oracle AI Database Administration Associate learning path](https://mylearn.oracle.com/ou/learning-path/earn-the-oracle-ai-database-administration-associate-credential/140076) is authoritative.

**Assessment contract exposed by the current path:** Oracle AI Database Administration Associate, exam 1Z0-182, 120 minutes.<br>
**Published scope:** instance startup/shutdown and architecture; Oracle Net; multitenant CDB/PDB administration; tablespaces and undo; users, roles, privileges, profiles, and auditing; RMAN backup/recovery; SQL*Loader, Data Pump, and external tables; AWR, ADDM, SQL Tuning Advisor, SQL Access Advisor, and basic tuning; automated tasks and resource plans; current Oracle AI Database enhancements.<br>
**Source boundary:** the public path does not publish weights, question count, or passing score. **VERIFY CURRENT** in MyLearn before scheduling.

## How to use this guide

Practice each task as current state → prerequisite → scoped command → expected control/data-file effect → verification query/log → recovery path. Use a disposable database or authorized lab; never improvise backup, recovery, user, or storage commands on production.

> **About related items:** A `Related item:` callout adds practical database-operations context. It is supporting knowledge, not a claim that its wording appears in Oracle's published scope.

## Objective map

| Oracle-published skill group | Administrative proof |
|---|---|
| Instance and network configuration | Sessions connect to the intended service and instance state is verified |
| Multitenant architecture | CDB/PDB lifecycle, service, state, and scope are explicit |
| Storage management | Tablespace, datafile, compression, and undo choices match workload/recovery needs |
| Security administration | Common/local users, privileges, roles, profiles, and audit policies are minimal and testable |
| Backup and recovery | RMAN configuration and restores meet declared recovery objectives |
| Data movement | Loads, external access, and Data Pump jobs preserve intended objects/data |
| Performance monitoring and tuning | Evidence identifies the constrained resource or SQL before change |
| Maintenance, automation, and auditing | Scheduled work, resource plans, and unified/FGA evidence are governed |

## 1. Architecture, instance, and connection path

Distinguish database files and logical structures from the instance's memory and processes. Know startup phases, shutdown modes, parameter files, control files, redo, undo, and diagnostic destinations at an associate reasoning level. Confirm state from database views and logs rather than command success alone.

Trace Oracle Net from client connect descriptor or Easy Connect string through listener and service registration to the intended container/service. Separate name resolution, reachability, listener, service, authentication, and authorization failures.

## 2. Multitenant administration

A CDB contains the root, seed, and PDBs. Common and local objects/users have different scopes. Practice creating, opening, closing, saving state, cloning, unplugging/plugging, and dropping disposable PDBs with correct container context. DBCA and SQL provide different workflows toward the same governed lifecycle.

Services should direct workloads to the intended PDB. Verify container before changing users, storage, parameters, or data. Plan file placement, compatibility, keys, and recovery when moving or cloning PDBs.

## 3. Storage and undo

Tablespaces are logical storage; datafiles/tempfiles are physical files. Understand permanent, temporary, and undo roles, extent/segment growth, autoextend risk, quotas, read-only/offline state, and space evidence. Compression trades CPU and change behavior for capacity/I/O benefits depending on feature and workload.

Undo supports transaction rollback, read consistency, and eligible flashback. Retention is influenced by workload and space; a requested value alone does not guarantee unlimited history.

## 4. Users, privilege, profiles, and audit

Create common or local users in the correct container. Distinguish system privileges, object privileges, roles, quotas, profiles, and administrative privilege. Grant only the actions required, test a denial, and understand how roles and direct grants affect stored program units and administration.

Unified auditing centralizes policy-based records; fine-grained auditing with `DBMS_FGA` targets selected access conditions. Define actor, object, action, condition, success/failure, retention, and review owner.

## 5. RMAN backup and recovery

Start with RPO, RTO, failure modes, retention, control-file/spfile protection, archive mode, and backup location. RMAN tracks backup metadata and performs full/incremental backup, validation, restore, recovery, and point-in-time workflows. A successful backup job is not proof of recoverability.

Practice recovery decisions for lost datafiles, control files, server parameter files, user error, and whole-database/time objectives only in a lab. Know when recovery requires mounted versus open state and when logs/archivelogs are needed.

## 6. Data movement

SQL*Loader uses data and control-file rules to load rows with reject/discard evidence. External tables expose external data through table metadata. Data Pump exports/imports database metadata and data through server-side jobs and directory objects. These are not interchangeable file-copy tools.

Plan character sets, types, constraints, triggers, indexes, privileges, object selection, remapping, job monitoring, and validation totals/checksums.

## 7. Performance and automated maintenance

Establish symptom, time window, workload, and baseline. Use wait events, sessions, system/SQL metrics, execution plans, AWR, ADDM, SQL Tuning Advisor, and SQL Access Advisor as evidence and recommendations—not automatic permission to change production. Validate benefit and regression risk.

Automated maintenance tasks run in defined windows. `DBMS_AUTO_TASK_ADMIN` controls supported tasks; resource plans allocate and constrain resources. Record why a task is disabled or a plan changed and monitor the consequence.

## 8. Current features and operating discipline

The path expects awareness of current Oracle AI Database architecture and enhancements. **VERIFY CURRENT** feature name, licensing/availability, compatibility, and container scope in the lab/database you use.

> **Related item:** Before a risky database change, write the verification and rollback query first. If rollback depends on a backup, prove that backup can be restored within the required time.

## Integrated practice scenarios

1. **New application PDB:** Provision a PDB/service, tablespace, local users/roles, profile, audit policy, backup, and health checks.
2. **Failed data load:** Diagnose listener/authentication, directory/privilege, format, rejected rows, constraints, and transaction effects; reconcile counts.
3. **Performance regression and user error:** Preserve AWR/SQL evidence, choose a bounded tuning test, then execute an RMAN or flashback recovery drill with measured RPO/RTO.

## Hands-on labs

1. Map instance memory/processes and database files; practice startup/shutdown and evidence checks.
2. Configure and troubleshoot an Easy Connect/listener/service path to a disposable PDB.
3. Create, clone, open, save state, unplug/plug, and remove lab PDBs with container checks.
4. Manage permanent, temporary, and undo space; reproduce and diagnose a safe space pressure condition.
5. Create least-privilege common/local accounts, roles, profiles, unified audit, and FGA policies; test denial.
6. Configure RMAN, take/validate backups, restore to an alternate lab target, and measure recovery.
7. Move synthetic data with SQL*Loader, an external table, and Data Pump; reconcile objects and rows.
8. Investigate a controlled SQL slowdown using waits, plans, AWR/ADDM/advisor evidence, and a rollback-ready test.

## Original readiness checks

1. Database versus instance? 2. Startup phases? 3. Listener versus service? 4. CDB root versus PDB? 5. Common versus local user? 6. Why verify container? 7. Tablespace versus datafile? 8. Temporary-space role? 9. Undo's three uses? 10. Autoextend risk? 11. System versus object privilege? 12. Role versus profile? 13. Unified versus FGA focus? 14. Backup versus restore proof? 15. Full versus incremental? 16. Restore versus recover? 17. Point-in-time consequence? 18. SQL*Loader control file? 19. External table role? 20. Data Pump directory object? 21. Why reconcile counts? 22. AWR versus ADDM? 23. Tuning Advisor caution? 24. Automated-maintenance window? 25. Resource-plan purpose? 26. What must be version-verified? 27. What remains unpublished? 28. What proves readiness?

### Answer guide

1. Persistent logical/physical data versus memory/processes managing it. 2. Nomount, mount, open. 3. Connection endpoint process versus registered workload identity. 4. Multitenant system container versus isolated user workload container. 5. Cross-container identity versus PDB-scoped identity. 6. Avoid changing the wrong scope. 7. Logical allocation versus physical file. 8. Work areas for sorts/hashes and temporary results. 9. Rollback, read consistency, eligible flashback. 10. Unbounded storage consumption. 11. Class of action versus action on an object. 12. Grant collection versus password/resource limits. 13. Broad unified policy records versus conditional object access. 14. Job completion versus tested recoverability. 15. Baseline blocks versus blocks changed since a level. 16. Copy files back versus apply redo to consistency. 17. Later changes may be lost and coordination is required. 18. Maps input fields and load behavior. 19. Query external data through table metadata. 20. Server-side filesystem/object access authorization. 21. Detect omissions, duplicates, rejects, or transforms. 22. Captured workload history versus analysis/recommendation. 23. Test applicability, benefit, cost, and regression. 24. Governed schedule for automatic tasks. 25. Allocate/cap resources among consumers. 26. Feature, edition/service, license/availability, compatibility, and container scope. 27. Weights, count, and score. 28. Correct scoped operations plus tested connection, privilege, backup/recovery, movement, and tuning evidence.

## Readiness checklist

- I verify instance, container, service, storage, and transaction state before acting.
- I can restore and recover a disposable database/PDB rather than merely describe backups.
- I test least privilege and audit evidence for common and local identities.
- I diagnose data movement and performance from logs, views, row/object reconciliation, and measured outcomes.

## Places to learn

This is a selective learning path, not a complete list of Oracle database administration resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official Oracle AI Database Administration Associate learning path](https://mylearn.oracle.com/ou/learning-path/earn-the-oracle-ai-database-administration-associate-credential/140076) | Oracle account/subscription may be required | **12+ hours** as published by Oracle University |
| [Oracle AI Database 26 Administrator's Guide](https://docs.oracle.com/en/database/oracle/oracle-database/26/admin/index.html) | Public | **15–25 hours** targeted reference work |
| Eight labs in this guide | Disposable Oracle AI Database environment | **32–48 hours** plus two recovery/tuning rehearsals |
