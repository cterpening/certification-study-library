# Non-Microsoft certification refresh — Group 8

**Completed:** October 28, 2026  
**Guides:** 10 (HashiCorp and Databricks)  
**Queue:** Group 8 of 17 from the frozen 167-guide eligible non-Microsoft queue. **Remaining after this group: 87 guides, approximately 9 groups.**

## Work completed

- Rechecked current official exam/credential pages, objectives, lifecycle state, relevant official learning listings, and first-party release channels for all ten guides.
- Refreshed ten guides and exam-check dates; updated HashiCorp's public credential names and provider availability in the catalog, and synchronized the shared learning-resource catalog.
- Added ten first-party sources covering current HashiCorp credential pages, HCP Terraform changelog, Vault 2.x release notes, Databricks October release notes, Agent Memory, AI Runtime, and a prompt-registry engineering example.
- Preserved three changed objective/status captures under dated October 28 names and restored prior stable paths to keep older receipts verifiable. Terraform Advanced's public status/title changed; its objective list is unchanged. Databricks GenAI's live Domain 4 label changed to “Assembling and Deploying Apps”; weights and exam details did not change.
- The objective monitor could not parse HashiCorp's Terraform Associate and Vault Associate pages after their current-page layout changed. The public pages were reviewed directly: Terraform Associate 004 still lists eight domains and 37 detailed objectives, and Vault Associate 003 still lists nine domains and 40 detailed objectives. Their current-version and assessment details were manually compared with the guide.
- Replaced the Data Engineer Associate guide's Academy course URL after automated DNS resolution failed and the course was not discoverable in public search. The guide now points to Databricks' current public Data Engineering learning-path catalog, which presents course and lab entitlements as variable rather than promising a course runtime.

## Guide-specific updates

| Exam | New information added |
|---|---|
| Terraform Associate 004 | Current credential page still tests Terraform 1.12, and the official 004 content list remains the same. HCP Terraform now supports organization-scoped Azure DevOps PAT connections ahead of Microsoft's Dec 1, 2026 retirement of global PATs; this is adjacent HCP workflow context. |
| Terraform Authoring and Operations Advanced | HashiCorp's Advanced rename is complete. Both AWS and Azure versions now appear on the current credential page for one credential; the exam still tests Terraform 1.6 and keeps the same objectives and lab-plus-multiple-choice format. Added the HCP Azure DevOps PAT migration note. |
| Vault Associate 003 | Current credential page lists Vault 1.19 and the existing nine objective domains. Older preparation pages may still say 1.16, so the current credential page controls the tested version. Added Vault 2.2/2.2.1 current operator context without asserting exam scope changes. |
| Vault Operations Advanced | Confirmed the Professional-to-Advanced rename and unchanged scenario objectives. Vault 2.2.1 includes an October policy-alias security fix; the guide retains Vault 1.16 as the exam version and treats 2.x as newer operator context. |
| Data Analyst Associate | October release notes add AI Search support for streaming tables, materialized views, and managed Iceberg V3 sources. The October guide version and in-scope AI/BI Genie content remain the exam baseline. |
| Data Engineer Associate | The official May 4, 2026 guide remains current. Added Lakeflow Jobs multi-trigger beta, group run-as identity, and GA pipeline system tables as dated orchestration and monitoring context. Replaced a DNS-failing course deep link with the current public learning-path catalog. |
| Data Engineer Professional | The Nov 30, 2025 official guide remains current. Added atomic transactions for managed Delta and Iceberg tables, requiring catalog commits, and GA Lakeflow pipeline system tables. |
| Machine Learning Associate | The Mar 1, 2025 guide remains current. AI Runtime reached GA Oct 21 with managed GPU training, Unity Catalog governance, MLflow observability, and Lakeflow integration; availability varies by account and region. |
| Machine Learning Professional | The Sept 30, 2025 guide remains current. Added AI Runtime GA and an Oct 27 Databricks engineering example using MLflow Prompt Registry to version prompts and schemas, evaluate against a fixed human-reviewed set, then promote or roll back changes. |
| Generative AI Engineer Associate | All six published weights and assessment terms remain. Domain 4 now reads “Assembling and Deploying Apps.” Added Agent Memory beta (managed sessions, memory, and background pipelines on Lakebase), default OAuth IDs for external AI agents, and MCP jailbreak-screening beta as current product examples. |

## Source health and review limits

The source sweep checked **263 registered URLs: 240 returned HTTP 200, 23 blocked automated fetching, and none were missing or errored** after the Data Engineering learning-path reference was updated. Academy lesson interiors require an account; no paid course interior or exam booking was inspected. Databricks feature rollout is staged, and beta/GA statements are dated. HCP and Vault product updates are separated from the tested product versions.

No Databricks workspace, HCP organization, paid course interior, or exam lab was accessed. The final audit is same-context and AI-assisted; no independent or human review is claimed.

## Selected first-party sources

- [Terraform Associate 004 credential page](https://developer.hashicorp.com/certifications/terraform-associate), [official 004 content list](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-review-004), and [HCP Terraform changelog](https://developer.hashicorp.com/terraform/cloud-docs/changelog)
- [Terraform Authoring and Operations Advanced credential page](https://developer.hashicorp.com/certifications/terraform-advanced) and [Advanced rename announcement](https://developer.hashicorp.com/terraform/tutorials/pro-cert/adv-update)
- [Vault Associate credential page](https://developer.hashicorp.com/certifications/vault-associate), [Vault Operations Advanced content list](https://developer.hashicorp.com/vault/tutorials/ops-pro-cert/ops-advanced-review), and [Vault release notes](https://developer.hashicorp.com/vault/docs/updates/release-notes)
- [Databricks October 2026 product release notes](https://docs.databricks.com/aws/en/release-notes/product/2026/october)
- [Agent Memory beta announcement](https://www.databricks.com/blog/introducing-agent-memory-databricks)
- [AI Runtime GA announcement](https://www.databricks.com/blog/ai-runtime-generally-available)
- [Prompt Registry and extraction evaluation example](https://www.databricks.com/blog/spot-fixes-measured-gains-improving-document-extraction-accuracy-aiextract-and-mlflow-prompt)
- [Current Databricks Data Engineering learning paths](https://community.databricks.com/t5/learning-paths/ct-p/databricks-learning-paths)

## Evidence

The [operations record](../../ADLC_Docs/operations/2026-10-28-nonms-refresh-group-08.json) binds guide hashes, objective/status snapshots, source-validation receipts, source health, and audit status. Structured source-freshness, audit, and deep-review receipts are recorded in `data/source-freshness.json`, `data/ai-audits.json` and `data/deep-reviews.json`.
