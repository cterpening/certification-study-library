# Professional Data Engineer deep review — September 29, 2026

## Scope and source evidence

The complete existing guide was reviewed against the canonical certification page and actual **five-page standard exam PDF**, read with layout extraction and byte/hash receipts. The map covers **67 main considerations under 19 numbered objectives**, grouped 17/11/13/11/15 with weights 22/25/20/15/18. Four nested transformation items remain within their parent consideration. No printed revision date or future exam effective date is invented.

The monitored objective digest remains `d9fc9ddb90e3c6f965fb09311b060710a297ba36f18025518dca3d5154d785bc`. The lifecycle baseline was previously absent. After explicit review, it was initialized as `50ccd813bba439b2b05cd37c6834841b1d8f855584b90d3a6fb696859e369931`; the subsequent observation is unchanged. Before, accepted and post-check receipts are retained. Initialization is not evidence of a changed blueprint.

The [canonical page](https://cloud.google.com/learn/certification/data-engineer) distinguishes the standard two-hour USD 200 exam, 40–50 questions and two-year validity from a one-hour USD 100 renewal exam with 20 questions and two-year validity. Both list English/Japanese. Designated Google Skills renewal gives one year and has separate linked-account/active-year conditions. This review maps the standard guide; the renewal PDF was not independently reviewed. The page's coming-branding notice supplies no dated replacement blueprint.

## Teaching and practical changes

The guide distinguishes committed pipeline results from repeated external side effects and incomplete late-data windows. It separates delivery IDs, entity keys, source order/epoch, tombstones and replay horizons, then explains default versus offset-aware/pending Storage Write API contracts and CDC ordering/staleness. These are separate guarantees, not a universal exactly-once label.

[BigQuery keys](https://docs.cloud.google.com/bigquery/docs/primary-foreign-keys) are unenforced, so the guide adds quality checks and join-grain evidence. [Dataform dependency guidance](https://docs.cloud.google.com/dataform/docs/dependencies) supports explicitly gating consumers on assertions. Stable Airflow intervals, shared input references, Bigtable key/access-pattern tradeoffs and feature availability timestamps address common silent correctness failures.

The full [April 22, 2026 Knowledge Catalog announcement](https://cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog), by Chai Pydimukkala and Sam McVeety, supplies naming and aggregation/enrichment/search context. The guide preserves blueprint-era Dataplex names and current technical API/CLI/IAM names. Marketing accuracy claims and the entire dated preview list are not adopted as current guarantees.

Recovery teaching separates time travel, support-assisted fail-safe and regional continuity. Managed BigQuery recovery needs the appropriate reservation/replica/backfill setup; hard versus soft failover, unreplicated ACLs, baseline versus autoscaled capacity, relocated schedules and regional history all affect the recovery plan. No cloud recovery was executed.

## Executed evidence and limits

The exact public program passed **40 checks**: 24 native in-memory SQLite CDC/transaction checks, six native point-in-time SQL checks, four native join-grain checks and six restricted window-policy model checks. Its public code hash, Python version and SQLite version are recorded. A stale update cannot resurrect a deleted key; conflicting delivery IDs and equal-version payloads are rejected. An injected exception between state and event-ledger writes rolls back both, and the next retry succeeds.

The feature query uses both event time and availability time: at prediction time 10 it selects 10 rather than a late correction of 90. Missing features retain the prediction row. A duplicate dimension increases a synthetic 150-cent total to 250; repairing the known fixture restores 150.

This is a single-epoch integer-order application exercise, not Datastream or BigQuery CDC emulation. SQLite keys are locally enforced. There is no distributed delivery, concurrent-writer test, durable crash-recovery test or source-epoch transition. The six integer-second window cases use a deliberately stated close-at-boundary policy; they do not execute Beam triggers, watermarks or panes.

There are **48 answered checks**, three integrated scenarios and **eight proposed cloud labs** with failure/repair/cleanup evidence requirements. Prior ACE evidence that `gcloud` was absent from PATH is reused. No installation, authentication, cloud API, scheduler, infrastructure, model or notification was attempted. Independent human review remains pending.

## Catalog comparison and verification

Google Skills confirms 13 activities but does not expose the earlier 77h45m duration. [Coursera](https://www.coursera.org/professional-certificates/gcp-data-engineering) now has five public cards totaling 33 hours, including Gemini Notebook study preparation, versus its 40-hour landing estimate. Its FAQ still gives 3.5 months at five hours/week and recommends a starting course absent from those cards. Public outcomes were read; paid lessons were not.

A current [Pluralsight PDE path](https://www.pluralsight.com/paths/google-cloud-professional-data-engineer-by-pluralsight) has five Janani Ravi courses totaling 12h20m plus three 30-minute labs, or 13h50m versus its rounded 14-hour header. Course dates are February–May 2026; lab dates are in April. All five domain titles are visible, although an active-production notice remains. This corrects the prior no-verified-path statement without claiming paid-lesson coverage.

Whizlabs exposes a title-only shell and O'Reilly returned 403. Historical book metadata and study budgets are qualified. The official sample form was observed only as a landing page. No paid lessons/books/provider labs, proprietary assessment or recalled exam item was accessed. Places to learn is last.

The operational receipt records exact local execution and, once completed, unit tests, repository validation, catalog consistency, strict site build, generated-site validation and diff checks. Source freshness is current; the program outcome remains **reviewed with blockers** for live-cloud execution and independent-human verification.
