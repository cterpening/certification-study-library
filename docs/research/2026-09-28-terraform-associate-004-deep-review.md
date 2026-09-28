# Terraform Associate (004) deep review — September 28, 2026

Read the complete guide and map all 37 detailed objectives across eight domains against the official certification page and content list. The current Terraform 1.12 exam baseline and accepted objective/status snapshots match. No new retirement notice was found on those pages. Product release versions remain separate from exam scope.

## Changes that improve learning

Clarify multiple provider plugins versus aliases, replace a fictional service resource with built-in `terraform_data`, explain write-only update/version signals and residual secret copies, and add opt-in S3 locking/deprecated DynamoDB context. Repair the Lab 3/4 root-address sequencing and explain why `terraform_data` cannot simulate independently changed remote infrastructure. Add four original worked decisions and answers to all 20 existing questions.

The [March 10, 2025 ephemeral-values article](https://www.hashicorp.com/en/blog/ephemeral-values-in-terraform) supports a secret-flow exercise. The [June 2, 2026 project-run-task article](https://www.hashicorp.com/en/blog/hcp-terraform-adds-project-level-run-tasks) supports a governance worksheet and identifies public beta. Both were readable through web retrieval while the direct HTTP checker was blocked. Current write-only documentation and the HCP changelog supply separate behavior/release evidence; no article deployment was executed.

## Execution and limitations

Downloaded Terraform 1.12.2 into the ignored review directory and matched its archive SHA-256 against the official release checksum list; the globally installed CLI was left in place. Ran the guide's provider-free Lab 1 and root-address Lab 4: 22 commands produced expected exit statuses and eight behavior assertions passed, including create/no-op, input/precondition failures, delete/create without a move, identity preservation with a move, and cleanup to empty state. No external provider or cloud account was used. These results do not validate HCP, secret rotation or remote backend concurrency.

Pluralsight still lists six courses/seven hours. KodeKloud lists 15 lessons and 126 topics; fix the earlier lesson count. O'Reilly/Udemy access was blocked, so prior durations/revisions are qualified. Course consumption estimates include study/practice and are not provider guarantees. Independent human review and other labs remain pending.

The operational receipt records objective hashes, prior records, fetched-source evidence and the local command log summary. Accepted snapshots were preserved.
