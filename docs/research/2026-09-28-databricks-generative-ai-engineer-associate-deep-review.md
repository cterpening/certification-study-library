# Databricks Generative AI Engineer Associate deep review — September 28, 2026

Read the complete guide and all 56 detailed objectives from the still-linked March 18, 2026 PDF. Counts by domain are 6, 8, 13, 15, 4 and 10. Vendor sample questions were not reproduced.

## Objective observation

The live monitor reports changed hashes. Comparing a private current snapshot with the accepted text shows only hyphen-to-en-dash changes in the six weighted domains. The prior status snapshot is absent, so this is an initial lifecycle observation rather than evidence of a newly changed lifecycle. Public assessment metadata still matches the guide. Accepted snapshots were preserved; the PDF objectives were separately read and mapped.

## Changes and source evidence

Clarify the [AI Search permission limitation](https://docs.databricks.com/aws/en/ai-search/ai-search) and supported synchronization boundaries. Explain why source row policies and UI login do not establish index access control. Distinguish the [App service principal and scoped user authorization](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/auth), including the difference between delegated SQL policy enforcement and index capabilities.

Add retrieval-denominator calculations, a deterministic PyFunc chain contract, four original operational decisions and twelve answered checks. Explain [scorer errors and missing production expectations](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-scorer-reference); completed runs require coverage checks before release.

Daniel Liden's March 23 [code-corpus experiment](https://www.databricks.com/blog/building-knowledge-assistant-over-code) informs the chunking comparison method. Retain its workload and measurement limits; do not generalize its percentages. LinkedIn's public 71-minute duration was verified. Academy lessons were inaccessible without sign-in, and Udemy/O'Reilly metadata could not be reverified.

## Local execution

Twenty-seven assertions passed with MLflow 3.16.1 and pandas 3.0.6. Executed both guide Python examples; exercised ranking cutoffs, missing/no-answer evidence, duplicate IDs and invalid cutoffs, PyFunc input errors, abstention and save/reload equality.

A real local `mlflow.genai.evaluate` run used three fixed output records and one code-based scorer. Two passed and one deliberately raised. The run finished, its aggregate mean was 1.0, but one row had an error with no value. Verified two-thirds coverage and an incomplete release decision. MLflow synthesized local evaluation traces; these are not production agent traces.

No LLM or embedding API, AI Search, Databricks App, remote tracking server, cloud endpoint or workspace lab was used. No network listener was started. Reload used the same isolated environment, not a clean deployment environment. All eight workspace labs remain proposed. Independent human review remains pending.
