# Splunk Advanced Power User deep review — September 30, 2026

The [guide](../../guides/SPLUNK-ADVANCED-POWER-USER-splunk-core-certified-advanced-power-user.md) maps 104 objectives in 22 groups, reviews 40 original answers, and records all ten labs as unexecuted. This best-effort review publishes supported corrections with explicit follow-ups.

## Blueprint and learning-path corrections

The complete indexed [credential page](https://www.splunk.com/en_us/training/certification-track/splunk-core-certified-advanced-power-user.html) and six-page parsed [blueprint](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-advanced-power-user.pdf) were read. They retain the named Core Power User prerequisite and 70 questions in 60 minutes including three agreement minutes; the credential page lists USD 130 and Pearson VUE. Eligibility and booking were not tested. No retirement or replacement was found within those pages; other release channels were not exhaustively checked.

Adding the weights gives **67% for domains 1–16 and 33% for domains 17–22**, correcting the guide's 59/41 split. The final page names **14 suggested courses**, correcting 13. Course names do not verify current availability, duration, access or completion. All guide time estimates are author planning budgets. PDF page-number concatenation artifacts were excluded from objective matching; no image-based PDF inspection is claimed. The September 2 normalized snapshot remains unchanged because direct retrieval and objective monitoring failed DNS. Manual indexed comparison is recorded separately from automated retrieval/hash success.

## Technical repairs and reading limits

Selected [tstats 10.0](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.0/search-commands/tstats) lines 500–746 clarify indexed-data and model paths, summary-only omission and dataset selection. Acceleration is not a universal requirement. An original paper example contrasts 120 intended events with 90 summarized events; no Splunk count or performance result is claimed.

Selected [Simple XML token usage 10.4](https://help.splunk.com/en/splunk-enterprise/create-dashboards-and-reports/simple-xml-dashboards/10.4/drilldown-and-dashboard-interactivity/token-usage-in-dashboards) lines 927–990 distinguish context-specific filters from the `n` filter, which disables escaping. Token visibility does not stop background searches. Selected [makeresults 10.0](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.0/search-commands/makeresults) lines 500–654 support the execution-time timestamp and temporary-result clarification. Remaining portions of these references were not reviewed.

The earlier September 30 reading of selected [transaction 10.4](https://help.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.4/search-commands/transaction) lines 500–699 is reused as dated evidence, not a fresh successful body/hash. Command closure and business completeness are now distinguished. The multivalue example explicitly requires aligned equal-length arrays and a delimiter absent from values; unequal/missing/collision cases remain runtime follow-ups. Independent expansion of two two-value arrays produces four logical combinations, not proof of the intended two relationships. No SPL was run.

## Source access and next pass

There are 17 direct receipts: three successful link-health checks, twelve DNS failures and two blocked searches. Lantern's initial HTTP 200 was followed by a body connection reset; it does not establish a fresh article read. YouTube returned a 176-character shell. The complete 3,919-character Pluralsight response contained navigation and an unrendered template, not actual course results. O'Reilly and Udemy searches were blocked. Older dashboard/event-handler/knowledge-management bodies were not freshly read. DNS failures are not evidence that links are dead.

All ten labs require a Splunk runtime or approved endpoint and remain unexecuted. The guide lists the missing evidence for each: input/schema/nulls, lookups and safe side effects, extraction performance, macro expansion, summary completeness, search equivalence, multivalue/time edges, transaction/subsearch limits, form tokens, and dashboard jobs/permissions/accessibility. No service, installation, account, webhook, lookup write, upload or configuration change occurred.

More research is needed on these labs, unavailable source bodies, current courses, framework availability and independent human review. Contributors can submit minimal public or synthetic reproductions with version, exact queries, expected/observed output and conflicting dated sources. Repository unit tests, strict build and repository/site/catalog checks are recorded after completion in `ADLC_Docs/operations/2026-09-30-splunk-advanced-power-user-deep-review.json`; they are not Splunk lab execution.
