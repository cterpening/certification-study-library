---
exam_code: SOL-C01
vendor_id: snowflake
official_blueprint: https://publish-p93462-e887935.adobeaemcloud.com/content/dam/SnowProAssociateCertificationTransitionSnowflakeUniversityPlatformSkillsBadgeFAQs.pdf
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# SnowPro Associate: Platform (SOL-C01) Retired Reference

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Public scope, lifecycle evidence, citations, links, and exam-integrity compliance were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#sol-c01-coverage-record).

**Status:** Retired May 4, 2026; it can no longer be scheduled<br>
**Replacement:** Snowflake University Platform Skills course + assessment, available from May 5, 2026 as a free, directly issued, non-expiring skills badge<br>
**Important distinction:** The replacement validates the same foundational course knowledge, but Snowflake says it is an educational skills badge—not a SnowPro certification. SnowPro is now reserved for proctored professional exams.<br>
**Official lifecycle source:** [Snowflake's transition FAQ](https://publish-p93462-e887935.adobeaemcloud.com/content/dam/SnowProAssociateCertificationTransitionSnowflakeUniversityPlatformSkillsBadgeFAQs.pdf). The retired exam page was captured for this repository's September 2 baseline but has since been removed; automated objective checks intentionally freeze retired baselines while source-health checks continue to test their surviving references.

## How to use this reference

If you are starting now, do not buy an SOL-C01 voucher or build a plan around taking the retired exam. Use this page as a technical companion to the current free Platform Skills course/assessment, then consider active COF-C03 SnowPro Core when you need a proctored professional credential.

If you already hold SOL-C01, Snowflake says the credential remains valid until its original expiration date. This reference helps preserve what it represented and lets you extend the same skills through current documentation. Product names, interfaces, AI functions, editions, limits and role behavior can change even though the former exam no longer does.

For every topic, produce evidence in a disposable trial/training account: object tree, query, role/privilege path, load history, warehouse behavior, protected recovery/share behavior, or a Cortex result with cost and safety notes. Avoid practicing broad account-level grants in a shared environment.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context. It is supporting knowledge, not a claim that the item appeared verbatim in the retired published objectives or appears in the replacement assessment.

## Preserved public scope map

Snowflake's surviving public overview lists six abilities but no longer exposes stable detailed domain weights. This reference does not reconstruct weights from commercial practice products.

| Public ability | Proof to produce now |
|---|---|
| Set up and navigate the UI and Snowflake Notebooks | Locate account/role/warehouse/database/schema context; run and inspect a worksheet/notebook safely |
| Create databases and stages, and use compute | Build an object hierarchy and stage with least privilege; start/suspend/resize a warehouse and explain cost/concurrency consequences |
| Load structured, semi-structured and unstructured data | Select file format/stage/load path; validate, load, query, inspect history and handle malformed data |
| Understand roles and data access management | Trace user → active role → inherited role → privilege → object, including ownership and managed-access boundaries |
| Understand and manage account structure | Explain organization/account/database/schema/object hierarchy and separate administrative duties |
| Use Snowflake Cortex LLM functions | Select an authorized AI function, define input/output/evaluation, observe consumption and avoid exposing sensitive data |

---

## 1. Navigate Snowflake, notebooks and architecture

### Know the layers and current context

Snowflake separates database storage, compute and cloud services. Persisted Snowflake table data is stored in optimized columnar micro-partitions. Virtual warehouses supply independent compute for SQL and supported code workloads; one warehouse does not share compute resources with another. Cloud services coordinate authentication, metadata, optimization and requests. Separation lets workloads scale and suspend independently, but does not eliminate governance or cost.

Snowsight is the web interface for worksheets, notebooks, data, monitoring and administration according to privilege. Before running anything, identify current account, region, role, secondary-role behavior, warehouse, database and schema. A successful unqualified object reference can target the wrong context; prefer deliberate qualification and a visible context check in labs.

Snowflake Notebooks combine code/SQL, Markdown and results in an interactive environment. Treat a notebook as executable software: pin or record dependencies, separate secrets/configuration, make cells restartable, control data exposure, and distinguish an exploratory result from a reproducible pipeline.

### Account and object hierarchy

An organization can contain accounts across regions/clouds. An account contains databases, warehouses, roles, users, integrations and other account objects. A database contains schemas; schemas contain tables, views, stages, functions and related schema objects. Storage hierarchy and access-control hierarchy intersect but are not the same tree.

Database and schema provide namespacing, ownership and privilege boundaries. Temporary objects serve session-scoped work; transient and permanent objects differ in data-protection behavior. Object type, edition and current documentation determine supported capabilities.

**Related item:** `USE ROLE`, `USE WAREHOUSE`, `USE DATABASE`, and `USE SCHEMA` change session context. They do not grant missing privileges and should not be confused with object creation.

---

## 2. Create data objects, stages and compute

### Tables, views and stages

Create a database/schema/table from an explicit owner role. Tables persist data; views store query definitions and expose results subject to privileges and view behavior. Use columns and data types that express the contract rather than storing everything as text. Constraints and table behavior differ from traditional engines; confirm what Snowflake enforces versus records as metadata.

A stage is a named or implicit location used in file workflows. Internal stages store files managed within Snowflake; external stages refer to supported cloud storage. Named stages make file format, credentials/integration and reuse more manageable than embedding values repeatedly. Prefer storage integrations over long-lived cloud credentials.

File formats describe parsing/serialization behavior such as delimiter, header handling, compression, encoding, nulls and error conditions. A stage does not parse files by itself; `COPY` combines stage/path, target, file format and load options.

### Virtual warehouses

A virtual warehouse provides compute. Size affects available resources and consumption; auto-suspend limits idle use, and auto-resume improves convenience. Multi-cluster behavior addresses concurrency rather than making one query inherently faster. Resize can help resource-heavy work, but query shape, pruning, caching and data design still matter.

Separate warehouses by workload/owner when isolation, chargeback or service-level behavior matters. Give roles only the usage/operation privileges they require. Monitor query history, load history and warehouse load rather than tuning by intuition. Always clean up or suspend lab compute.

**Related item:** Storage and compute separation means dropping or suspending a warehouse does not drop tables. It also means data protection and compute availability are different recovery concerns.

---

## 3. Load and use structured, semi-structured and unstructured data

### Choose the path

Structured data fits declared rows/columns. Semi-structured formats such as JSON, Avro, ORC, Parquet or XML retain nested/flexible structure; Snowflake's `VARIANT`, `OBJECT` and `ARRAY` support common patterns. Unstructured files can be held in stages and referenced with directory/file capabilities. Pick a path based on volume, latency, source control, schema evolution and failure/replay needs.

Bulk file loading commonly follows source → stage → file format → validation → `COPY INTO` table → load history/reconciliation. Snowpipe supports event-driven file ingestion; Snowpipe Streaming supports low-latency row ingestion. The retired introductory scope centered basic stage/file loading, but recognizing adjacent choices prevents using batch `COPY` as a universal answer.

Validate representative files before broad load. Decide how to handle malformed rows, duplicates, late files and schema changes. `COPY` metadata/load history helps explain loaded, skipped or failed files. Preserve source identity and batch/event keys so retry is deterministic.

### Query and transform safely

Parse semi-structured paths deliberately and use `FLATTEN` when arrays/objects need relational rows. Cast types and handle absent versus JSON null versus SQL `NULL`. For unstructured data, keep file privileges, scoped URLs and sensitive content controlled.

A useful lab proves row counts, rejected records, null/type rules, duplicate behavior and rerun behavior. A query returning rows is not sufficient evidence of a correct pipeline.

**Related item:** Micro-partition pruning reduces scanned data when filters align with metadata. It is automatic; clustering decisions require evidence from real query patterns and scale.

---

## 4. Roles, privileges and data access

### Trace effective authorization

Snowflake combines discretionary access through object ownership, role-based access through roles, and limited user-based grants. Prefer privileges → custom database/account role → parent functional role → user. Database roles scope privileges within one database and must be granted to an account role for activation. Role inheritance flows upward through grants.

For a query, distinguish:

- authentication: how the identity proves itself;
- session role: which role is primary and whether secondary roles contribute;
- `USAGE`: ability to traverse warehouse/database/schema;
- object privilege: for example `SELECT` on a table;
- ownership/grant authority: who controls the object or grants;
- future grants: policy for objects created later, not retroactive magic.

Managed access schemas centralize grant decisions with the schema owner or a role with grant-management authority. This prevents every object owner from independently granting access. Transfer ownership carefully because ownership carries control and existing grants have explicit handling.

### Separate duties

System roles carry account-management responsibilities. Build custom roles for business/workload access instead of placing application privileges directly on administrative roles. Separate user/security/account administration, object ownership, data use and warehouse operation. Use service identities and modern authentication appropriate to automation; do not share human passwords.

Prove least privilege with a positive test and a negative test from the intended role. Record the grant chain. `ACCOUNTADMIN` success proves almost nothing about whether the application role is correct.

**Related item:** Object access and warehouse access are independent. A role can see a table but lack compute, or operate a warehouse but lack data access.

---

## 5. Data protection and collaboration

Time Travel can query or restore historical object state within the configured/supported retention. Fail-safe is Snowflake-managed recovery assistance after Time Travel for eligible permanent data; it is not a user-queryable backup or a substitute for tested recovery design. Temporary/transient objects have different protection behavior.

Zero-copy clone initially reuses storage metadata and then diverges through changed micro-partitions. It is useful for isolated development/testing and recovery workflows, but cloned privileges, dependencies, governance and later storage still need review.

Secure Data Sharing lets a provider expose selected database objects to consumers without copying the underlying data into each consumer account. The provider controls the share; the consumer creates a database from it and supplies compute for queries. Listings and Marketplace add discovery/distribution patterns. Reader accounts can support consumers without a Snowflake account, with provider-managed implications.

Design collaboration from owner, approved data, freshness, masking/row policy, region/cloud, consumer role, cost, revocation and audit requirements. A share does not grant arbitrary access to the provider account.

**Related item:** Replication/failover addresses cross-region/account continuity and is distinct from Time Travel, Fail-safe, clone and sharing. Select recovery controls from RPO/RTO and failure scope.

---

## 6. Cortex AI functions

The surviving SOL-C01 overview explicitly included Cortex LLM functions. Current documentation groups evolving AI SQL functions for tasks such as completion, summarization, extraction, classification, translation and other unstructured analytics. Function names, model availability, regions, privileges and consumption change quickly; use the live AI SQL documentation rather than retired course screenshots.

Start with a bounded task and evaluation set. Define input columns, allowed data, expected output schema, quality/safety checks, model/function, latency and consumption. Protect sensitive data, grant the minimum Cortex capabilities, and record model/function version or observable behavior. LLM output is nondeterministic and can be unsupported by source data; validate before business action.

Use SQL to keep governed data near the operation where appropriate, but do not assume “inside Snowflake” removes privacy, residency, prompt-injection, cost or human-review responsibilities. Limit output use and log enough metadata for evaluation without logging protected prompts/results broadly.

**Related item:** Retrieval/grounding, agents and custom model workflows belong to more advanced current capabilities. The retired foundational scope asked for basic Cortex LLM-function use, not full production AI architecture.

---

## Integrated scenarios

### Scenario 1: Safe analyst workspace

Create database/schema/table/view roles, a small warehouse with auto-suspend, and one analyst role. Load a clean CSV through a named stage, grant only traversal/select/warehouse use, run in Snowsight/Notebook, and prove a protected raw table is denied. Capture object and role trees plus cleanup.

### Scenario 2: Semi-structured support events

Load JSON containing nested events and one malformed record. Validate first, quarantine/reject deliberately, query `VARIANT`, flatten nested values, cast timestamps, reconcile file/row counts and rerun without accidental duplication. Explain when Snowpipe would replace batch loading.

### Scenario 3: Governed AI summary

Use synthetic support text and an authorized Cortex AI function. Define expected facts and prohibited data, grant a narrow role, measure a small sample, review unsupported claims/sensitive output and record consumption. Share only an approved view/result, then revoke and prove access removal.

## Hands-on evidence labs

1. **Context map:** In a disposable account, record organization/account/role/warehouse/database/schema and show how fully qualified names avoid wrong-context changes.
2. **Objects and compute:** Create a database, schema, table, view, named stage and auto-suspending warehouse; resize/suspend/resume and capture history/cleanup.
3. **Structured load:** Define a CSV file format, validate/load known data, reconcile counts, inspect load history and safely rerun.
4. **Semi-structured load:** Load nested JSON with missing/null/malformed cases, query `VARIANT`, flatten an array and document error behavior.
5. **Least privilege:** Build a custom role hierarchy, grant traversal/select/warehouse use, prove expected success and denied write/admin actions.
6. **Protection:** In an authorized lab, update/drop controlled data and use supported Time Travel/clone behavior to inspect or restore; write the Fail-safe boundary.
7. **Sharing design:** Create a share or a paper design if account features are unavailable; map provider/consumer object, compute, cost, access and revocation evidence.
8. **Cortex proof:** Run one synthetic-data AI function with a small evaluation set; capture role, input contract, output review, consumption and cleanup.

## Readiness checks

1. Why are storage, compute and cloud services separate?
2. What persists when a warehouse suspends?
3. Can you identify current role, warehouse, database and schema before execution?
4. What makes a notebook reproducible rather than merely interactive?
5. How do organization, account, database, schema and object relate?
6. When should names be fully qualified?
7. What is the difference between a table and a view?
8. How do internal and external stages differ?
9. What does a file format control?
10. Why prefer a storage integration to embedded cloud credentials?
11. How do size, auto-suspend and auto-resume affect compute behavior/cost?
12. When does multi-cluster compute help?
13. How would you separate analyst, loading and BI workloads?
14. Can you trace stage → validation → `COPY` → history → reconciliation?
15. How do batch COPY, Snowpipe and Snowpipe Streaming differ?
16. How do SQL `NULL`, JSON null and a missing key differ?
17. When is `FLATTEN` appropriate?
18. What makes a load retry safe?
19. How do DAC, RBAC and UBAC appear in Snowflake?
20. Can you trace user → active role → inherited role → privilege → object?
21. Why are `USAGE` and object privileges both required?
22. How do database and account roles differ?
23. What changes in a managed-access schema?
24. Why is `ACCOUNTADMIN` a poor application test?
25. What are positive and negative authorization tests?
26. How do Time Travel and Fail-safe differ?
27. What does zero-copy clone copy initially, and what later diverges?
28. How does Secure Data Sharing avoid consumer-side data copies?
29. Who supplies compute for a shared database query?
30. How do sharing, clone and replication solve different problems?
31. What task contract belongs before a Cortex call?
32. How do you evaluate factual quality and unsafe output?
33. Which AI details must be rechecked in live documentation?
34. Why is a Cortex result not automatically trustworthy?
35. Can you explain why SOL-C01 is no longer schedulable?
36. Can you state why the Platform Skills Badge is not a SnowPro certification?

### Check key

- **Ready:** You can demonstrate it with fresh evidence and explain failure/cleanup.
- **Review:** You recognize the term but cannot yet produce or interpret the object, query, grant, load, recovery, share or AI result.
- **Gap:** You guessed or relied on retired practice questions. Return to current documentation and an authorized lab.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. For new learners, use the replacement Platform Skills course as the primary path, current documentation for depth, and only selected labs/supplements. Durations and availability were checked September 2, 2026 and can change.

| Resource | Access | Estimated time | Best use and freshness boundary |
|---|---|---:|---|
| Snowflake University Platform Skills course + assessment | Free account | 8–15h estimate | Current replacement named in the transition FAQ. Complete it inside Snowflake University; the badge is directly issued and non-expiring, but is not SnowPro certification. |
| [SOL-C01 transition FAQ](https://publish-p93462-e887935.adobeaemcloud.com/content/dam/SnowProAssociateCertificationTransitionSnowflakeUniversityPlatformSkillsBadgeFAQs.pdf) | Public | 15–30m | Authority for dates, free replacement, badge/certification distinction, expiry and existing-holder treatment. |
| [Key concepts and architecture](https://docs.snowflake.com/en/user-guide/intro-key-concepts) | Public | 2–4h + 4–8h labs | Current architecture, objects, loading, AI and collaboration map; broader than the retired introduction. |
| [Access control overview](https://docs.snowflake.com/en/user-guide/security-access-control-overview) | Public | 2–4h + 3–6h labs | Role/privilege/object hierarchy and managed-access depth; verify current system-role guidance. |
| [Data loading overview](https://docs.snowflake.com/en/user-guide/data-load-overview) | Public | 2–4h + 4–8h labs | Current bulk/continuous loading choices and operational references. Use a trial/training account and synthetic data. |
| [Secure Data Sharing overview](https://docs.snowflake.com/en/user-guide/data-sharing-intro) | Public | 1–2h + 2–4h lab/design | Provider/consumer sharing model. Account edition/region/features can constrain a live lab. |
| [Cortex AI SQL functions](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions) | Public | 2–4h + 3–6h labs | Current replacement for retired screenshots/function names. Recheck models, regions, privilege and consumption. |
| [Udemy SOL-C01 course](https://www.udemy.com/course/snowpro-associate-platform/) | Paid | 3h19m + 6–10h labs | Updated April 2026 but tied to a retired exam. Use only hands-on fundamentals you verify against current docs; do not buy it for an exam attempt. |

Do not use products advertising “actual SOL-C01 questions,” dumps or guaranteed passing. The exam is retired, so current practical evidence and the official replacement path have more value than memorizing its former assessment.
