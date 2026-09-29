# Databricks Associate Developer for Apache Spark deep review — September 28, 2026

Read the complete guide and all 32 leaf objectives from the still-linked October 30, 2025 PDF: 7/4/10/3/4/2/2 by domain. No vendor sample questions were reproduced. The weighted objective hash is unchanged. The monitor's changed flag comes from a missing prior lifecycle snapshot, not a demonstrated change to exam status. Accepted snapshots remain untouched.

## Repairs

Clarify [JDBC partition stride versus row filtering](https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html), [ANSI default changes](https://spark.apache.org/docs/latest/sql-migration-guide.html), and [stateless-streaming AQE support](https://spark.apache.org/docs/latest/streaming/ss-migration-guide.html). The stateful-streaming scenario no longer assumes batch/stateless AQE applies.

Separate classic ID-only and ID-plus-time deduplication from [within-watermark deduplication](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.dropDuplicatesWithinWatermark.html). Add original DataFrame fixtures, four decision cases and twelve answered checks. Murali Talluri's January 10, 2025 [employee walkthrough](https://community.databricks.com/t5/technical-blog/deep-dive-streaming-deduplication/ba-p/105062) supports the comparison method, cross-checked with current upstream references. It was readable through the web tool despite blocked automated collection.

## Local validation and deferred blocker

Both Python blocks parse. Ten SQLite assertions verify portable expectations for null filters/counts, deterministic latest-row selection, left-join preservation, duplicate-dimension multiplication and duplicate-preserving union. They do not verify Spark execution.

Attempted isolated Spark 4.2.0 setup in WSL Ubuntu-26.04. An initial temporary environment disappeared when WSL shut down. A second attempt in a persistent location encountered package-host timeouts. Downloaded the official PyPI archive through Windows and verified its SHA-256; subsequent WSL exec startup stalled before the lab ran. Stopped the owned pending Windows launcher commands. No host reboot, global Java/Python installation or cloud deployment was performed.

**Blocker for the next session:** restore reliable WSL startup or use an authorized disposable Spark environment, then execute the two guide blocks and the retained checkpoint/watermark, Parquet, Arrow/Pandas and restart checks. No Spark or streaming success is claimed; all eight runtime labs remain proposed. Keep this review marked reviewed-with-blockers until that validation is resolved.

Pluralsight's public 11-course/5-lab/9-hour metadata was verified. Academy lessons require sign-in; paid O'Reilly/Udemy metadata and the earlier retirement-thread claim could not be reverified. Independent human review remains pending.
