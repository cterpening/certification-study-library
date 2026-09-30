# Splunk Core User deep review — September 30, 2026

The [guide](../../guides/SPLUNK-CORE-USER-splunk-core-certified-user.md) maps all **40 objectives**, grouped **5/8/3/4/3/7/5/5**, and retains 40 original questions and answers with clearer reasoning for command order, missing values, counts and scheduling. This is a best-effort public-source review with documented follow-ups. **None of the eight Splunk labs was executed.**

## Blueprint and lifecycle evidence

The complete indexed [credential page](https://www.splunk.com/en_us/training/certification-track/splunk-core-certified-user.html) and three-page [blueprint](https://www.splunk.com/content/dam/splunk2/en_us/pdfs/training/splunk-test-blueprint-user.pdf) were read after direct DNS failures. The contract remains an optional entry point without prerequisite exams, 60 questions and 60 minutes including three agreement minutes; the credential page lists USD 130 / Pearson VUE. No booking or account availability was tested. Objective 4.4 says “tables”; the command is `table`. The historical September 2 normalized snapshot remains intact. Manual source comparison is not a newly successful objective-monitor hash. PDF screenshots did not surface for inspection; the reading claim is parsed text.

Selected [candidate handbook](https://www.splunk.com/en_us/pdfs/training/splunk-certification-candidate-handbook.pdf) lines 235–356 cover results/badges, retakes, accommodations and the opening renewal sections. The three-year cycle and final-year renewal retake boundary are reflected in the guide. The rest of the 26-page handbook and individual eligibility were not reviewed. No retirement or replacement was found in the credential and blueprint checked; this does not establish that no announcement exists elsewhere.

## Concrete improvements

The representative-event example now sorts before deduplication. The [SPL sort reference 10.2](https://help.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/sort), selected lines 500–613, supports the 10,000 default result cap and the resource caveat for `sort 0`. The [SPL dedup reference, Cloud 10.4.2604](https://help.splunk.com/en/splunk-cloud-platform/spl-search-reference/10.4.2604/search-commands/dedup), selected lines 500–632, supports input-order selection and missing-key behavior. Later command examples were not read.

An original three-event worksheet predicts a different surviving row when time order changes. It separates retaining missing keys from counting events and explains why sorting afterwards cannot restore discarded rows. It is a paper exercise, not an SPL emulator or engine result. Scheduling answers distinguish cadence from window width and configured alerts from fired instances and delivered actions. Source review does not prove execution.

## Learning resources and gaps

The [Search Tutorial introduction](https://help.splunk.com/en/splunk-enterprise/search/search-tutorial/10.0/introduction/about-the-search-tutorial), substantive lines 575–620, and [Search Reference introduction](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.0/introduction/welcome-to-the-search-reference), lines 499–546, were read. Linked lessons and the full manual were not. The complete indexed seven-page [2024 curated training sheet](https://www.splunk.com/en_us/pdfs/training/platform-curated-learning.pdf) supports historical durations; current access and prices remain unverified. The six selected modules total 13h45, not the complete Search Expert path.

The complete 16,880-character Lantern landing/index was read, without opening its linked articles. YouTube returned only a 176-character shell. Udemy and the previously recorded O'Reilly listing were blocked; the book's exact edition/format and current duration remain unverified. It is now explicitly a historical lead. Other hour ranges are author planning budgets, not course-completion evidence.

## Next pass and validation boundary

There are 17 direct source receipts:2 successful, 13 DNS errors and 2 blocked. A local DNS error does not establish that a public URL is dead; indexed reading is recorded separately. The existing 10.4 UI, reporting and lookup pages were not freshly read. No Splunk executable or approved endpoint was available, so all eight navigation/search/command/report/lookup/scheduling/alert labs remain unexecuted. The guide includes the evidence a community reproduction should provide. No installation, service, upload, account, purchase or notification occurred.

More research is needed on unavailable UI pages, fresh objective retrieval, current course/book metadata and runtime results. Independent human content/accessibility review remains pending. These limitations do not prevent publishing useful supported explanations. Repository tests, strict site generation, repository/site/catalog consistency and whitespace checks are recorded only after those gates finish, in `ADLC_Docs/operations/2026-09-30-splunk-core-user-deep-review.json`.
