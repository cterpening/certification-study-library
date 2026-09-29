# DEA-C02 Advanced Data Engineer deep review — September 29, 2026

The guide now distinguishes channel delivery contracts, durable acknowledgements, business correctness, task-graph recovery and coordinated replication. An original local CDC workbook passed forty checks, and forty-eight answered study prompts support eight proposed account labs. This is a same-context AI review; independent human review and Snowflake execution remain pending.

## Scope and evidence

The entire [DEA-C02 public page](https://learn.snowflake.com/en/certifications/snowpro-advanced-dataengineer-C02/) was read: five abilities, two or more years of production data-engineering experience recommended, and USD 375 per Advanced attempt. The detailed guide remains behind an embedded request form; no form was submitted and no current detailed PDF was recovered by targeted public searches. No weights, question count or exam duration were inferred.

Objective bytes remain at `5d27aac73433eb775a5d5b4ff7af013755ab26751154413fa84c363d200909c0`. The missing lifecycle snapshot was initialized after review at `0cead048921028baabe0bed9538dd2f365bf40a90b4a515a3fa5c0d38bcb53ca`; a subsequent read-only monitor check reported both unchanged. No objective archive or rewritten scope was needed.

The actual [five-page training datasheet](https://www.snowflake.com/wp-content/uploads/2022/03/standard_de_datasheet.pdf), code 25L03/copyright 2025, was fully read with a binary digest/page receipt. It describes three-day role training with Foundations-equivalent knowledge, a required data-engineering background and recommended MFA Essentials. The outline supplies practical study prompts across ingestion, transformation, orchestration, performance, delivery and observability; it is not a detailed exam blueprint. Older notebook/function names need current-product verification. Live ILT-DE metadata independently says 24 hours.

## Current product and release findings

[Elastic Channels GA on September 15](https://docs.snowflake.com/en/release-notes/2026/other/2026-09-15-snowpipe-streaming-elastic-channels-ga) and the SDK 1.8.0 release dated August 27 are distinct observations. The documented GA SDK API requires 1.8.0 or later; no installed SDK or account state was inspected. Named and Elastic channels now have an explicit comparison covering ordering, producer coordination, delivery and recovery evidence.

The complete main [Elastic overview](https://docs.snowflake.com/en/user-guide/snowpipe-streaming/snowpipe-streaming-elastic-channels-overview) establishes at-least-once unordered delivery and durable buffering before later processing/queryability. Callback append tokens and REST request IDs correlate outcomes; neither is a deduplication key. Producer RAM is not durable retention. Row-level error logging and downstream business reconciliation remain necessary.

The complete main Named Channels page explains channel-local ordering, client-interpreted committed offsets and source replay. Tokens do not automatically stop business duplicates; records must remain recoverable and channel identity matters. Thirty-day inactivity can remove offsets. REST continuation sequencing differs from source position. The guide does not substitute one architecture's methods for another or claim global ordering.

Two September 24 notices were fully read. Partitioned streaming now covers Snowflake-managed Iceberg v2/v3 with both channel types, excluding externally managed tables and Streaming Classic. Event-table monitoring supplies row/error/channel/server-processing evidence, but collection requires the schema's LOG_EVENT_LEVEL setting or inheritance and read permission. Default event-table existence alone is insufficient. No settings, alerts or accounts were changed.

Selected task-graph documentation establishes root-suspension behavior, skipped-root/finalizer boundaries, same owner/database/schema, overlap policies and task-definition versioning. Called procedures remain a separate deployment dependency. Retrying a graph does not imply earlier steps or external effects rolled back. Stream consumption/filter behavior and best-effort dynamic-table freshness are taught separately.

Selected replication sections show why stream/source/destination state must be coordinated, why pre-refresh source history is unavailable after promotion, and why old-primary commits can be ahead of the promoted target. Upstream retention must cover the replication interval and recovery margin. External-stage files, storage trust, notifications and routing are separate dependencies. This was not a full audit of the 58k-character reference or an executed failover.

Further guidance separates file-load metadata from business identity, default MERGE ambiguity errors from unmatched duplicate inserts, standard-table key declarations from enforcement, role authority from ownership, and warehouse monitors from total service consumption. Every new material claim points to a current registered primary source; per-source notes record selective reading boundaries.

## Actual local workbook

The exact public code ran using Python 3.13.14 and in-memory SQLite transactions: **40 checks passed**. The code digest, stdout, interpreter version and final values are retained in `ADLC_Docs/operations/2026-09-29-dea-c02-deep-review.json`.

The model separates partition/source offset from entity/business version. Identical input replay is harmless; a changed payload at a consumed offset fails. A retained deletion prevents a late old update from resurrecting an entity, while an explicitly allowed newer version can reactivate it. Equal business versions with conflicting values fail. Invalid records are preserved in quarantine with receipts and checkpoint advancement in the same local transaction.

An injected failure after a state write but before its receipt rolls back, and the retry succeeds. A second event's version conflict also rolls back an earlier valid update in the packet. Partition offsets remain independent; gaps, boolean offsets and unknown partitions are rejected. Corrections arrive as new source events, preserving original quarantined evidence. The final result is ten receipts, two quarantined events, checkpoints p0=9 and p1=1, and two active entities totaling 250 fictional cents.

This uses one connection, controlled fixtures, contiguous positive integer offsets and a trusted one-partition-per-entity mapping. Receipts/tombstones never expire during the process. SQLite enforces its keys; standard Snowflake primary keys do not. All state disappears when the process ends. No crash durability, concurrency, external-side-effect atomicity, Snowflake SDK/MERGE/stream/task behavior, credentials or network workload was tested. Quarantine/state/checkpoint atomicity is a deliberately local application contract.

## Learning comparison and remaining limits

The public Essentials track lists six workshops, including Data Science; courses are free and the wording says many badges are free. No aggregate provider duration was verified. Practice-exam terms were read without opening questions: 24 hours from purchase to completion, one attempt, and a missed-window 48-hour-from-purchase re-registration boundary. Practice-language availability is not real-exam language evidence.

Pluralsight's seven July–September 2025 cards total 495 minutes (8h15m), versus its 8h header, and the role path remains labeled in production. O'Reilly's DEA-C02 bootcamp by Dr. Yasir Khan has five timed day-one topics and six day-two topics, each 240 minutes; un-timed breaks/Q&A are excluded. No upcoming booking date was verified. An unrelated Databricks footer was not used as exam identity.

Both O'Reilly book URLs returned HTTP403, so old reading-time/revision metadata remains unverified. The public Manning publisher page independently confirms Maja Ferle's Snowflake Data Engineering, November 2024, ISBN 9781633436855 and 368 pages, with a SQL/cloud audience. Its public description was read; the book and paid chapters were not. A generic website ownership label is not evidence of account access.

Thirty sources are registered/cited: twenty-eight reachable and two access-blocked. Public metadata is not lesson-quality or exam-completeness evidence. Eight Snowflake labs and three integrated scenarios remain proposed, with explicit input, failure, reconciliation and cleanup plans. The operational record receives test/repository/catalog/strict-site/generated-site/diff results when those checks complete. Remaining limits include detailed-guide access, account availability, live execution, blocked catalogs and human review. The reserved five GitHub guides and disabled notification pilot remain untouched.
