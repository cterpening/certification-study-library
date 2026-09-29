# Salesforce Platform Developer deep review — September 29, 2026

The [guide](../../guides/SALESFORCE-PLATFORM-DEVELOPER-salesforce-certified-platform-developer.md) now maps 21 saved objectives, answers 40 original readiness prompts and includes 31 executed local checks. The review adds version-specific Apex security guidance, stronger browser/server boundaries and evidence for bulk and transaction reasoning. Salesforce org activities and independent human review remain pending.

## Scope and current-source comparison

The complete browser-rendered [exam article](https://help.salesforce.com/s/articleView?id=005298965&language=en_US&type=1) matches all 21 objective statements across four groups of 4/9/4/4, at 27/28/25/20 percent. The contract and annual maintenance wording match the saved status. Existing baseline files were retained. Direct HTML remains a loading/CSS shell, and the automated monitor correctly returns manual review; browser comparison is not an automatic current-source hash match. The Summer ’25 seasonal label remains a watch rather than being silently changed to match current product releases.

## Technical corrections and source conflicts

[Current Apex security guidance](https://developer.salesforce.com/docs/platform/lwc/guide/apex-security.html) and the [API 67 database release note](https://help.salesforce.com/s/articleView?id=release-notes.rn_apex_default_user_mode.htm&language=en_US&release=262&type=5) make access modes and compilation versions essential to reasoning about old code. The guide distinguishes invocation permission, sharing, CRUD/FLS and business authorization, and recommends explicit operation modes and negative-persona evidence. It explains the API 67 removal of WITH SECURITY_ENFORCED without claiming to have compiled Apex.

The [specific trigger release note](https://help.salesforce.com/s/articleView?id=release-notes.rn_apex_triggers_system_mode.htm&language=en_US&release=262&type=5) distinguishes a trigger's without-sharing context from user-mode database defaults. That conflicts with a broad trigger bullet in the [Summer ’26 roundup](https://developer.salesforce.com/blogs/2026/06/the-salesforce-developers-guide-to-the-summer-26-release). The guide follows the detailed rule, retains the discrepancy and records that indexed first-party text was readable while direct/browser release-page opens returned shells. No vendor was contacted and no org runtime was used.

The community LWC article's CDN advice is corrected using [first-party CSP rules](https://developer.salesforce.com/docs/platform/lightning-components-security/guide/content-security-policy-intro.html): external JavaScript libraries belong in org static resources, and a Trusted URL is not sufficient permission to load arbitrary CDN scripts. [LWS documentation](https://developer.salesforce.com/docs/platform/lightning-components-security/guide/lws-sanitize-html.html) also distinguishes DOM HTML filtering from arbitrary input validation. The community sample was not copied, installed or executed. Current DX documentation supplies the Vibes Extension/IDE naming distinction while the guide preserves the exam's Agentforce for Developers wording.

## Actual local execution

The original Python workbook uses standard-library SQLite and 400 synthetic requests. Trace callbacks independently count 200 configuration SELECTs for the per-record strategy and one for the grouped strategy on the first 200 inputs. Both strategies produce the same desired values. The first batch totals 69,800 cents; processing the next batch gives 139,850. Replay plans no writes, and a changed rate identifies 100 legitimate recalculations, giving 141,840 cents.

Further checks reject duplicate keys, negative/Boolean quantities and missing configuration before changing persisted results. A bound quoted string remains query data. Three separate in-memory transaction fixtures demonstrate partial rows that commit, a caught atomic-operation failure that can retain an earlier header update, and a later failure that removes earlier successful partial work. Every connection closes.

All 31 checks passed. SQLite executemany performs individual writes; savepoints explicitly implement the selected operation policy. These tests do not emulate Salesforce DML, permissions, trigger recursion, governor limits, asynchronous work, Flow or LWC, and prove nothing about concurrent edits or production performance. The eight expanded org activities specify the missing platform evidence.

## Learning catalog and evidence limits

The public prep trail lists 75 minutes across four cards. Winter ’26 maintenance lists 45 minutes, split into a 10-minute introduction and 35-minute combined Apex/Flow activity. The introductory body was read, but detailed claims about features such as GraphQL deprecation or Trusted Mode were not adopted without deeper product verification, and no assessment/activity was completed.

Pluralsight's six Adam Olshansky cards total 598 minutes (9h58) against a rounded ten-hour header. Dates span September 2022, October 2023 and May 2024; card metadata does not prove current API 67 or exam coverage. Trailmix and Academy bodies were blank, while O’Reilly and Udemy returned403. Earlier metadata is explicitly marked unverified. Focus on Force remains a general catalog reference, and no paid lesson or question-bank quality claim is made.

All 23 direct sources have receipts: 21 HTTP successes and two blocked. Several successes expose only shells or empty bodies. Browser/indexed reading boundaries are recorded separately from transport status. The three-column learning table separates listed durations, earlier observations and our study-time estimates.

The operational ledger is `ADLC_Docs/operations/2026-09-29-salesforce-platform-developer-deep-review.json`. It retains prior records, hashes, objective mapping, manual source comparison, source receipts and reading limits, local execution and validation results. Remaining work includes source-access limits, the official trigger-wording discrepancy, live org activities and independent human review. Five reserved GitHub guides and the disabled notification pilot remain untouched.
