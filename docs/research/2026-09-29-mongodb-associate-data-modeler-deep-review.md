# MongoDB Associate Data Modeler deep review — September 29, 2026

The [guide](../../guides/MONGODB-ASSOCIATE-DATA-MODELER-mongodb-associate-data-modeler.md) now answers 40 original readiness prompts and includes 34 executed Python predictions, three worked scenarios and eight proposed deployment activities. Fifteen historical objective statements are mapped; current enrolled scope was not confirmed.

## Exam evidence and unresolved contract

The [main exam page](https://learn.mongodb.com/pages/mongodb-associate-data-modeler-exam) displays 75 questions and 110 minutes. The [course route](https://learn.mongodb.com/courses/mongodb-associate-data-modeler-exam), linked from the public learning path, displays 70 questions, including 60 scored and 10 unscored, and 105 minutes. Both list English, no prerequisite and USD 150. The main page states online proctoring. The discrepancy is explicit; no actual booking or detailed policy was verified.

The canonical study-guide public landing lists a free 30-minute guide and enrollment. Its linked viewer failed with 500 and the published document asset returned 403. No document body, account access, enrollment or access-control change was obtained. Existing September 2 objective/status snapshots remain intact; their hashes and the access receipt are preserved. The automated objective monitor remains manual review, with no unchanged claim.

The August 18, 2026 announcement aligns skill badges and paths and advertises a full-path completion discount. It does not announce a replacement exam. No dated replacement was identified in the accessible material, which is a limited observation while the objective body is unavailable. Selected 9.0 release headings remain Upcoming despite current/preview manual labels; neither availability nor exam version is inferred.

## Original teaching and actual local execution

The guide follows one fictional shop from a measurable workload through ownership, skew, pattern tradeoffs, indexes and evolution. Ninety-nine customers have 10 orders and one has 10,010, giving a misleading mean of 110. A recent-20 count cap leaves 1,010 hot and 9,990 archived items. This proves arithmetic, not chronological selection, actual BSON size or archive lifecycle.

A deliberately smaller 12 MiB planning budget with a 1,024-byte base and assumed 512-byte items permits 24,574 items arithmetically; doubling item size halves the approximate capacity to 12,287. The real 16 MiB document limit still requires encoded measurement and growth headroom. Count-only caps are insufficient.

An original event fixture totals 1,800 cents; a duplicate delivery inflates a naive sum to 2,600. Sequential process-local receipts recover 1,800, reject changed payloads and expose a 50-cent derived-value drift. They do not provide durable or concurrent exactly-once processing.

A pure migration transforms a single shipment into a list, preserves unit/reader meaning and checks a revision. Replay with a current revision is a no-op; stale revisions and unknown versions fail. A two-shipment state cannot reverse into the old one-slot shape without loss, so the example refuses that rollback. Revision-test indivisibility is assumed by the function, not observed on MongoDB. A checkpoint at 4 with missing identity 3 demonstrates why identity reconciliation must accompany checkpoints and counts.

All 34 Python checks passed. No MongoDB server/shell/driver, BSON codec, Atlas account, actual index plan, database benchmark, authentication or physical deletion was tested. The eight deployment activities and independent human review remain pending. The public code hash and actual output are retained in the operational record.

## Technical distinctions and reading limits

The [validation-level reference](https://www.mongodb.com/docs/manual/core/schema-validation/specify-validation-level/) supports an explicit distinction: strict applies to future inserts/updates, not retrospective proof of every stored document; moderate can exempt updates to already invalid legacy documents. The 9.0 constraint level has separate preparation and scan requirements and remains version-specific further reading. The local matrix decides whether a write should be checked; it does not run MongoDB's BSON-aware JSON Schema validator.

The [TTL reference](https://www.mongodb.com/docs/manual/core/index-ttl/) supports asynchronous expiry, missing/non-date and earliest-date-array behavior, primary-side deletion and backlog cautions. Its time-series sections disagree about the indexed field. No time-series TTL recipe is prescribed until the version-specific discrepancy is resolved. Application visibility deadlines and physical deletion evidence remain separate.

Selected [explain sections](https://www.mongodb.com/docs/manual/reference/explain-results/) distinguish plan-cache isolation, execution time excluding network, repeated document examinations and returned results. Primary ESR/unique/multikey rules constrain candidate index hypotheses. These are reading-based explanations, not actual plan or performance results. Six primary references reuse complete or explicitly selected reading from the immediately preceding Developer review, with fresh captures and per-source limits.

The 2020 first-party data-modeling/memory article supplies historical locality and working-set context. Its then-current Atlas feature language is not treated as a present availability guarantee. No vendor example code, practice-question interior or paid lesson was copied.

## Learning catalog and receipts

Both the current certification-path URL and earlier path URL show eight required cards:90,75,60,60,60,50,60,60 minutes. Their 515-minute total is 8h35, compared with an 8-hour headline. Adding the separate 105-minute exam makes 10h20; that exam card repeats the unresolved contract difference. Completion-discount advertising is recorded without eligibility verification. The practice landing lists one hour; the announcement lists four minutes.

Three paid requests returned 403, so earlier O'Reilly and Udemy metadata remains unverified. The YouTube capture contains title/footer only; the video was not played. Catalog metadata does not establish lesson quality or complete exam coverage.

Thirty-one source receipts record 28 HTTP successes and three blocked requests. Several successes contain application shells, with browser reading documented separately. The failed public document access is an additional receipt. The operational ledger is `ADLC_Docs/operations/2026-09-29-mongodb-associate-data-modeler-deep-review.json`; it preserves prior evidence, objective mapping, source boundaries, catalog arithmetic, snapshot/code hashes and validation results. Five reserved GitHub guides and the disabled notification pilot remain untouched.
