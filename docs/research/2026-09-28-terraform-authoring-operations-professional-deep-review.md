# Terraform Authoring and Operations Advanced deep review — September 28, 2026

Read the complete guide and all 27 subobjectives in six domains. The current certification root specifies Terraform 1.6; Associate's 1.12 baseline must not be imported into Advanced preparation. Objective/status monitor results match accepted snapshots. The Professional-to-Advanced rename is already reflected; the legacy catalog identifier remains stable. Azure delivery is still announced for late 2026. Public Azure practice material is not evidence of bookable delivery. Add an October 28 library recheck, explicitly not a launch date.

## Learning changes

Explain backend migration versus reconfiguration, modern S3 locking versus the 1.6 baseline, full-state exposure through remote-state reads, provider aliases and lifetime, and advisory/mandatory external checks. Add four worked cases and 20 answers. The native test example uses plan operations and custom-condition expected failures. Mark ephemeral/write-only/mocking features with minimum-version boundaries.

Dan Barr's [October 4, 2023 Terraform 1.6 article](https://www.hashicorp.com/en/blog/terraform-1-6-adds-a-test-framework-for-enhanced-code-validation) supplies useful release-era test context, corroborated with current product documentation and local 1.6.6 execution. Web retrieval was readable; direct HTTP was blocked. HCP's current changelog was read separately. No paid content or live exam material was inspected.

## Actual validation

Downloaded Terraform 1.6.6 into the ignored review directory and verified the archive against the official SHA-256 list. A local built-in-provider adaptation of Lab 2 moved two indexed root resources into keyed child-module resources, producing no-op resource actions and retaining both IDs. The Lab 3 adaptation passed three native tests: valid port, expected invalid-port rejection, and upper boundary. Five behavior assertions passed; cleanup left empty state. Exact command/status evidence is in the operational receipt.

These Windows checks do not validate cloud APIs, HCP controls, external concurrency or Linux exam fluency. Other labs and independent practitioner review remain pending. The public practice catalog contains two import activities, so the learning table now states their limited coverage. No accepted baseline was rewritten.
