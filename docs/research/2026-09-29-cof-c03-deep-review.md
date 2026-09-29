# COF-C03 SnowPro Core deep review — September 29, 2026

The guide now maps the seven current public abilities to explanations, forty-eight original answered readiness prompts and eight concrete proposed account labs. An original analytical workbook passed twenty-four local checks. Current authentication, notebook, pipeline and performance boundaries replace vague or stale advice. This is a same-context AI review; independent human review and live Snowflake work remain pending.

## Scope and lifecycle evidence

The entire public [COF-C03 page](https://learn.snowflake.com/en/certifications/snowpro-core-c03/) was read. Its objective text is unchanged at `fc6ba90a44c29eb3380a41bd9609357c29247bbe81be8003dcbe89ad71a8063c`. The missing lifecycle baseline was explicitly initialized after checking the page, at `ad98df3b8191fa4f26724f33236295724fddeeafbe3c903515f5c6cf8ec48677`; a second read-only monitor run reported both unchanged. No objective text was replaced or fabricated archive created.

The detailed-guide control embeds a request form without a direct PDF link. Targeted public searches did not recover a current detailed guide; an older COF-C02 result was not adopted. No form, registration or authentication was submitted. The seven public abilities therefore remain the mapping boundary, without inferred exam weights, duration or question count.

The actual [prep-course PDF](https://www.snowflake.com/wp-content/uploads/2022/03/OD-Cert_Prep-Datasheet.pdf), four pages and code 25L19, was fully read and retained with its binary digest and page count. Its five teaching areas have 6/3/3/4/3 bullets: nineteen in total. These provide study prompts, not a replacement detailed exam blueprint. The PDF calls duration preparation-dependent; the current live course separately says four hours.

The program policy confirms two-year validity, qualifying renewal before expiry, full-retake renewal within six months, a seven-day wait after failures and four retakes within twelve months. A scaled 750 on a 0–1000 scale does not imply 75% correct. Current Core price is USD175; the practice-page FAQ repeating that figure is not verified practice pricing.

## Technical repairs and release intake

The [strong-authentication notice](https://docs.snowflake.com/en/user-guide/security-mfa-rollout) was fully read: phase 3 is listed for August–October 2026 with each account receiving its enforcement date. Once applied, password-using humans need MFA and service users cannot use passwords; legacy service types migrate. The notice excludes trial/reader accounts and Snowflake Postgres. The guide does not turn a dated rollout window into a universal account-state claim.

The [Legacy Notebook notice](https://docs.snowflake.com/en/release-notes/bcr-bundles/un-bundled/bcr-disable-legacy-notebooks) was fully read: creation disabled September 1, execution/editing planned to stop in November, with view/export/migration retained. These are product changes, not an announced COF-C03 retirement. Release intake uses the actual primary notices, without inventing a blog publication date or performing a migration.

New pipeline explanations distinguish file-load metadata from permanent business identity, ambiguous MERGE matches from duplicate unmatched inserts, stream SELECT from committed consumption and filtered consumption from a retained subset. Dynamic-table target lag is best-effort freshness relative to root sources, not an exact interval; a terminal DOWNSTREAM table lacks an automatic refresh consumer. Original proposed labs require rollback, replay, failure and cleanup evidence.

Performance teaching now connects grain, orphan rows, window peers, cache conditions and time-weighted concurrency. Query Insight flags lead to profile investigation rather than an automatic warehouse-size prescription. Persisted-result controls do not disable warehouse-local caching, and measured correctness must precede speed/credit comparisons.

Additional corrections cover missing JSON paths versus JSON null and malformed forgiving parses; current standard-table NOT NULL/CHECK enforcement versus unenforced primary/unique/foreign keys; primary-role creation versus secondary-role access; warehouse-monitor cost limits; same-region sharing; temporary-name shadowing; and connector-specific binding/autocommit behavior. Source notes identify the exact selected sections read, rather than asserting full documentation audits.

## Executed local evidence

The exact public Python code ran with Python 3.13.14, SQLite and standard-library arithmetic: **24 checks passed**. Its digest, stdout, interpreter version and result values are recorded in `ADLC_Docs/operations/2026-09-29-cof-c03-deep-review.json`.

Five fictional orders total 675 cents. A naive inner join to customer-version history returns seven rows and 900 cents while also dropping an orphan. Aggregating facts before the same bad dimension join leaves the error; SUM(DISTINCT cents) instead drops a legitimate equal-value order. Validation rejects ambiguous customer/version ties before selecting the current dimension, and a left join retains five rows, the orphan and the correct total. A deliberately conflicting version is rolled back. Explicit ROWS/RANGE windows demonstrate peers; reversing fixture insertion preserves results with the stated ordering. A SQL-looking input bound as data does not broaden selection.

Synthetic query intervals are clipped to a sixty-second observation window. Seventy-five running query-seconds produce average running load 1.25; twelve queued seconds produce 0.2. This is arithmetic on invented intervals, not actual warehouse telemetry or CPU measurement.

The exercise uses a single in-memory SQLite connection and controlled fixtures, with no credentials, network, cloud charges or filesystem data. SQLite key enforcement differs from standard Snowflake. Current-customer-region selection is an explicit reporting policy, not historical as-of attribution. The exercise does not execute Snowflake MERGE, streams, connectors, authentication, pruning or VARIANT, or establish production concurrency, durability or complete application-security guarantees.

## Learning comparison

Public course metadata was compared without entering paid content. The official prep course is four hours with six months or order-expiry access, whichever ends first; the exam fee is separate. Level Up has eight teaching items plus a final assessment, without a verified provider duration. Official practice must be accessed and completed within twenty-four hours of purchase, with one attempt; a missed window loses the fee and imposes a forty-eight-hour-from-purchase re-registration boundary. No practice questions were opened.

Pluralsight lists four June–August 2026 course cards totaling 307 minutes (5h7m), versus a five-hour header. The path remains in production; collaboration is planned rather than among those four published cards. No lesson-quality or completeness endorsement is made. The public O'Reilly bootcamp agenda by Tomáš Sobotík has fourteen timed topics each day: 240 and 245 minutes, excluding un-timed breaks/Q&A. No upcoming booking date was verified. O'Reilly on-demand and Udemy both returned HTTP403; their earlier durations/revision dates remain explicitly unverified.

The source register includes thirty-one sources, twenty-nine reachable and two access-blocked. All thirty-one are cited in the guide; actual PDF receipt and commercial metadata observations are retained separately from first-party freshness findings. There was no account creation, enrollment, assessment, paid recording or trial activation.

## Validation and remaining work

The operational ledger records local unit tests, repository validation, learning-catalog consistency, strict site build, generated-site validation and diff checks once complete. The eight account labs and three integrated scenarios remain proposed. Outstanding limits are the detailed-guide request boundary, account-specific product behavior, unavailable commercial metadata, live execution and independent human review. The five reserved GitHub guides and disabled notification pilot remain untouched.
