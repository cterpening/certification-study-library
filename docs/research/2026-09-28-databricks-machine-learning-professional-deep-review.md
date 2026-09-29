# Databricks Machine Learning Professional deep review — September 28, 2026

Read the complete guide and all 47 leaf objectives from the still-linked September 30, 2025 PDF. The three weighted domains and lifecycle snapshots are unchanged. Unbulleted subsection labels are excluded from the objective count; vendor sample questions were not reproduced.

## Unresolved source wording

The [profiling overview](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/) describes a last-30-days limit. The [API guide](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-api) describes an initial backfill followed by new data, and the metric reference qualifies the initial window. The SDK and bounded primary-source search did not resolve old-event/late-label refresh behavior. Preserve the ambiguity, provide an authorized disposable test matrix, and follow up October 5. Mark this review reviewed-with-blockers.

## Improvements

Separate anomaly freshness/completeness checks from former Lakehouse Monitoring data profiling. Identify the current API, numeric versus categorical drift measures, refresh completion and label coverage. Correct the online-store link's third-party/native distinction, document Ray integration constraints and replace the inaccessible old Optuna link with a current upstream tutorial. Add four original operational decisions and ten answered checks.

The February 4 [monitoring article](https://www.databricks.com/blog/data-quality-monitoring-scale-agentic-ai) adds product context for that capability distinction, corroborated by current documentation. It does not redefine exam scope.

## Local execution

Twenty assertions passed with MLflow 3.16.1, Optuna 5.0.0, pandas 3.0.6 and NumPy 2.5.3. Saved and reloaded the guide's custom PyFunc, repeated inference in a fresh Python process, and checked valid/negative-output, empty and invalid-input behavior. Ran four serial Optuna trials training Ridge on synthetic data, verified four child runs linked to one parent in a local SQLite MLflow store, recorded metrics/artifact and verified the chosen minimum. Checked canary rates, label coverage and a CPU-only concurrency bound.

No network listener or remote tracking service was started. No Spark, Ray, distributed worker, Unity Catalog, online store, monitoring service or endpoint was executed. Local reload used the existing isolated environment; it is not a clean dependency-environment or deployment test. All eight service labs remain proposed. Human review and signed-in course review remain pending; paid metadata access limits are recorded in the guide and receipt.
