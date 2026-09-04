---
exam_code: 1Z0-171
vendor_id: oracle
official_blueprint: https://mylearn.oracle.com/ou/learning-path/earn-the-oracle-ai-database-sql-associate-credential/140075
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-04
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-04
---

# 1Z0-171 Oracle AI Database SQL Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide maps Oracle University's current public learning-path scope checked September 4, 2026. It is unofficial and may contain errors. The [official Oracle AI Database SQL Associate learning path](https://mylearn.oracle.com/ou/learning-path/earn-the-oracle-ai-database-sql-associate-credential/140075) is authoritative.

**Assessment contract exposed by the current path:** Oracle AI Database SQL Associate, exam 1Z0-171, 120 minutes.<br>
**Published scope:** relational and Oracle AI Database architecture; retrieval, filtering, and sorting; functions and aggregation; joins, subqueries, set operators, and hierarchical queries; tables, views, indexes, sequences, constraints, DML, transactions, multitable inserts, `MERGE`, and flashback queries; users, privileges, and roles; SQL Developer and SQL*Plus; selected 26ai SQL enhancements.<br>
**Source boundary:** no weights, question count, or passing score are published on the public path. **VERIFY CURRENT** in MyLearn before scheduling.

## How to use this guide

Run every statement against disposable sample schemas. Before execution, predict row count, column names/types, null behavior, duplicate behavior, sort order, changed data, transaction state, privilege requirement, and likely error. Then prove the prediction with a minimal query.

> **About related items:** A `Related item:` callout adds practical SQL engineering context. It is supporting knowledge, not a claim that its wording appears in Oracle's published scope.

## Objective map

| Oracle-published skill group | SQL proof |
|---|---|
| SQL fundamentals | Correct projection, filtering, sorting, expressions, and substitution behavior |
| Data transformation and functions | Correct single-row, numeric, text, date, conversion, conditional, and JSON results |
| Data aggregation and analysis | Correct grouping, filtering of groups, and subtotal semantics |
| Definition and manipulation | Correct objects, constraints, DML, and transaction boundaries |
| Advanced queries | Correct joins, subqueries, set operations, hierarchy, flashback, and merge behavior |
| Security and access control | Minimum user, system, object, role, and schema privileges |
| AI Database enhancements | Version-aware use of published 26ai SQL additions |

## 1. Relational model and SELECT processing

Tables represent relations through columns, rows, keys, and constraints. Oracle architecture separates database files from the instance that manages them; SQL operates through sessions and transactions. Use aliases to make intent clear.

Reason about logical query processing: source and joins, row filtering, grouping, group filtering, projection, duplicate handling, and ordering. Only `ORDER BY` guarantees presentation order. `NULL` means unknown or inapplicable, so comparisons use three-valued logic and `IS NULL` rather than `= NULL`.

## 2. Expressions, functions, and conversion

Character, numeric, date/time, conversion, and conditional functions operate per row unless aggregated. Distinguish data type from display format. Prefer explicit conversion with a format model when input is not guaranteed by the session environment.

Know concatenation, arithmetic, precedence, `CASE`, `DECODE`, `NVL`-family behavior, and null propagation. Date arithmetic, time zones, and implicit conversions can make a query depend on session settings.

## 3. Aggregation and analytical summaries

Aggregate functions reduce rows; grouping defines each reduction set. Nonaggregated selected expressions must align with the grouping rules. `WHERE` filters before grouping; `HAVING` filters groups afterward. Understand how nulls and empty inputs affect each aggregate.

`ROLLUP`, `CUBE`, and `GROUPING SETS` generate different subtotal combinations. Use grouping metadata to distinguish an aggregated null from a null stored in the data.

## 4. Joins, subqueries, and set operators

Choose inner or outer joins from preservation requirements, then write complete predicates. Cross joins may be intentional but accidental many-to-many multiplication is a common error. Self joins apply roles to repeated table references.

Single-row, multiple-row, correlated, and scalar subqueries have different cardinality rules. `EXISTS` asks whether a match exists; `IN` and `NOT IN` require careful null reasoning. Set operators align column counts and compatible types; their duplicate and ordering behavior differs.

## 5. Objects, constraints, and transactions

Create and alter tables with appropriate types, defaults, identity behavior, and constraints. Primary, unique, foreign, check, and not-null constraints protect different invariants. Indexes can support access and uniqueness but create storage and DML cost. Views expose stored queries; sequences generate independent values; synonyms provide alternate names.

`INSERT`, `UPDATE`, `DELETE`, and `MERGE` change data. Multitable inserts route rows to multiple targets. `COMMIT` makes transaction changes durable; `ROLLBACK` reverses uncommitted work; savepoints provide partial rollback markers. Understand statement atomicity and the effect of DDL on transaction boundaries.

## 6. Advanced retrieval and flashback

Hierarchical queries traverse parent/child relationships and need start, connection, ordering, and cycle reasoning. Correlated subqueries evaluate with outer-row context. Flashback query syntax reads eligible earlier committed versions subject to undo retention and privilege; it is not a replacement for backup.

Use SQL Developer or SQL*Plus intentionally: statement terminators, script execution, substitution variables, formatting, and transaction behavior differ by client context.

## 7. Security and 26ai features

System privileges allow classes of actions; object privileges authorize operations on particular objects; roles group grants. Distinguish users and schemas, direct grants and role grants, ownership, grant options, and revocation effects. Apply least privilege and avoid practicing as a broadly privileged account.

The current path highlights `SELECT` without `FROM`, SQL `BOOLEAN`, enhanced `DEFAULT ON NULL`, and JSON-related use. **VERIFY CURRENT** syntax and database compatibility before assuming a feature exists in an older environment.

> **Related item:** A syntactically correct query can still be wrong if its join cardinality, null assumptions, time zone, or transaction boundary does not match the business requirement.

## Integrated practice scenarios

1. **Sales analysis:** Join customers/orders/items, handle missing dimensions, create monthly summaries with subtotals, and prove row counts.
2. **Schema release:** Create constrained tables, views, indexes, and sequences; load with multitable inserts/`MERGE`; test rollback and invalid rows.
3. **Delegated reporting:** Create a minimum reporting role, expose a view, test direct/role grants, and audit a denied change attempt.

## Hands-on labs

1. Write 30 small queries predicting types, nulls, row counts, and sort order before execution.
2. Test text, number, date/time, conversion, conditional, and JSON expressions under changed session settings.
3. Build `GROUP BY`, `HAVING`, `ROLLUP`, `CUBE`, and `GROUPING SETS` reports from the same data.
4. Prove inner, outer, self, semi/anti-style, and accidental many-to-many join behavior.
5. Compare scalar, correlated, `EXISTS`, `IN`, and null-affected `NOT IN` subqueries.
6. Create a constrained schema and test each constraint, index, view, sequence, and transaction boundary.
7. Use `MERGE`, a multitable insert, a hierarchy, and an eligible flashback query in a disposable database.
8. Create least-privilege users/roles and test allowed and denied access in SQL Developer and SQL*Plus.

## Original readiness checks

1. Database versus instance? 2. What guarantees order? 3. Why does `= NULL` fail? 4. `WHERE` versus `HAVING`? 5. Aggregate null behavior? 6. Why use explicit conversion? 7. `CASE` versus `DECODE` portability? 8. Inner versus outer join? 9. Accidental Cartesian symptom? 10. Scalar-subquery cardinality? 11. `EXISTS` question? 12. `NOT IN` null risk? 13. Set-operator alignment? 14. `UNION` versus `UNION ALL`? 15. Primary versus unique constraint? 16. Foreign-key purpose? 17. Index tradeoff? 18. View versus table? 19. Sequence property? 20. Commit versus savepoint? 21. DDL transaction concern? 22. `MERGE` purpose? 23. Flashback query dependency? 24. System versus object privilege? 25. Role benefit? 26. Which 26ai features are named? 27. What remains unpublished? 28. What proves readiness?

### Answer guide

1. Persistent files/logical structures versus memory/processes managing them. 2. Explicit `ORDER BY`. 3. Comparison is unknown; use `IS NULL`. 4. Filter rows before grouping versus groups after aggregation. 5. Most ignore nulls; count variants and empty sets differ. 6. Avoid session-dependent implicit behavior. 7. Standard flexible expression versus Oracle-specific compatibility function. 8. Return matches only versus preserve one/both sides. 9. Unexpected row multiplication. 10. At most one row. 11. Whether any matching row exists. 12. A null can make the predicate unknown. 13. Same number and compatible types by position. 14. Deduplicate versus retain duplicates. 15. One identifying key/not-null versus alternative uniqueness semantics. 16. Enforce referenced relationship. 17. Faster access/constraint support versus storage and DML maintenance. 18. Stored query interface versus stored rows. 19. Independent value generator with possible gaps. 20. End transaction versus partial rollback marker. 21. Implicit commit boundaries. 22. Conditional insert/update from a source. 23. Available undo/history and privilege. 24. Class of action versus action on a specific object. 25. Reusable managed grant set. 26. `SELECT` without `FROM`, `BOOLEAN`, enhanced `DEFAULT ON NULL`, and JSON use. 27. Weights, count, and score. 28. Correct pre-execution reasoning and repeatable SQL results under changed data/null/session conditions.

## Readiness checklist

- I predict query and transaction results before running SQL.
- I test duplicate, null, empty, invalid, denied, and rollback paths.
- I create schema objects and privileges without relying on administrator shortcuts.
- I can explain version-sensitive 26ai syntax and verify compatibility.

## Places to learn

This is a selective learning path, not a complete list of Oracle SQL resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official Oracle AI Database SQL Associate learning path](https://mylearn.oracle.com/ou/learning-path/earn-the-oracle-ai-database-sql-associate-credential/140075) | Oracle account/subscription may be required | **20+ hours** as published by Oracle University |
| [Oracle AI Database 26 SQL Language Reference](https://docs.oracle.com/en/database/oracle/oracle-database/26/sqlrf/index.html) | Public | **12–20 hours** targeted reference work |
| Eight labs in this guide | Disposable Oracle AI Database schema | **28–40 hours** plus timed SQL drills |
