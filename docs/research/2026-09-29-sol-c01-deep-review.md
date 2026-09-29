# SOL-C01 retired Platform reference deep review — September 29, 2026

The reference preserves the six archived public abilities without reconstructing a detailed retired blueprint or inventing weights. It now explains the active replacement course, current notebook/constraint/Cortex changes and practical loading/access boundaries. An exact public workbook passed 45 local checks, and 42 original answers support eight concrete proposed Snowflake labs. This is a same-context AI review; independent human review and live Snowflake exercises remain pending.

## Retired scope and current replacement

The September 2 objective snapshot remains frozen at `a930a723415ca1b8dfead2cf60a3d27b6c7eaf3d336fefc301421adee9123d57`. It supplies the six abilities and May 4, 2026 retirement statement. The actual objective-monitor run returned no results because retired exams are intentionally skipped; that is not a fresh unchanged-blueprint verification. No objective or lifecycle snapshot was rewritten.

The actual two-page [transition FAQ](https://publish-p93462-e887935.adobeaemcloud.com/content/dam/SnowProAssociateCertificationTransitionSnowflakeUniversityPlatformSkillsBadgeFAQs.pdf) was fully read and retained with binary/page receipts. It establishes May 5 voucher disablement and the free University course assessment, a non-expiring educational badge, original expiry for existing Associate holders and the distinction from proctored SnowPro professional credentials. The guide does not encourage a retired voucher purchase or claim assessment completion.

Following the actual public catalog link located the current [OD-SPT listing](https://learn.snowflake.com/en/courses/OD-SPT/): four hours estimated effort, 30 days of lab access, basic database knowledge and assessment/badge availability after training completion. The former 8–15h was a study budget. No enrollment, individual lab expiry, assessment or badge was accessed.

## Current teaching changes

The [Legacy Notebook notice](https://docs.snowflake.com/en/release-notes/bcr-bundles/un-bundled/bcr-disable-legacy-notebooks) stops new legacy creation September 1 and plans to stop execution/editing in November 2026 while preserving view/export/migration. Selected migration documentation distinguishes Workspaces notebook-service Container Runtime compute from warehouse execution of SQL/Snowpark, and requires deliberate file context. No migration was executed, and the planned November date is not presented as already effective.

The current constraint matrix and April 10.12 release notes show enforced standard-table NOT NULL and CHECK, while standard primary/unique/foreign keys remain unenforced. Hybrid key behavior differs. This boundary is especially visible around the SQLite exercise, whose primary-key enforcement must not be mistaken for standard Snowflake behavior.

COPY file metadata expires after 64 days; uncertain old files are skipped by default under documented conditions. LOAD_UNCERTAIN_FILES and FORCE have different replay effects. The guide now separates file-load tracking from business-event identity and requires source/rejection/duplicate reconciliation. Selected COPY reference sections were read; the entire command reference was not audited.

Missing JSON paths, JSON null, the string "null" and failed forgiving parses must not be collapsed blindly. Current IS_NULL_VALUE and TRY_PARSE_JSON descriptions support the explanation. The Python exercise labels only its own controlled missing/None/value states, not SQL NULL or VARIANT semantics.

Access-control guidance now distinguishes primary-role creation from ordinary access through active secondary roles, role ownership from inheritance, managed-access grants and existing/future objects. Temporary tables can shadow identically qualified permanent names in a session. Resource monitors cover warehouse usage rather than all serverless/AI costs and can overshoot while a warehouse stops. Same-region direct sharing is kept separate from cross-region delivery and reader-account implications.

For ordinary AI_COMPLETE usage, the guide explains function/account privileges, database-role grants and model availability/access separately. Broad grants can survive a narrow revocation. The current access guide distinguishes the model bootstrap application role SNOWFLAKE.PUBLIC from account-role PUBLIC. The [phased model-access notice](https://docs.snowflake.com/en/release-notes/bcr-bundles/un-bundled/bcr-2378) includes an August–November timeline, while the [2026_07 bundle page](https://docs.snowflake.com/en/release-notes/bcr-bundles/2026_07_bundle) is still labeled disabled by default. The guide preserves that qualification and requires actual account-state verification instead of assuming uniform enforcement. No account settings or permissions were changed.

## Executed local evidence

The exact public code ran with Python 3.13.14 and standard-library CSV, Decimal, JSON and SQLite: **45 checks passed**. The code digest, stdout, interpreter version, source receipts and final validation are recorded in `ADLC_Docs/operations/2026-09-29-sol-c01-deep-review.json`.

The exercise validates small CSV fixtures, converts amounts to exact integer cents, binds file identity to content hash and reconciles event identity/value pairs. Identical duplicates are skipped; a conflicting duplicate rolls back preceding inserts. A separate injected failure before the file receipt also rolls back, followed by a successful retry. The final state is five events, three receipts and 1,740 cents. Controlled nested JSON fixtures retain element positions and distinguish missing/null/string values.

All data and the SQLite database stay in memory; there are no network calls, credentials, cloud actions or filesystem data files. This is a single-connection application contract, not a Snowflake emulator. The manifest does not expire during the process and provides no durable, concurrent or external-side-effect guarantee. Its digest identifies bytes without authenticating the source. SQLite key enforcement differs from standard Snowflake. The JSON helper is not a full untrusted-input validator or an implementation of Snowflake FLATTEN/VARIANT.

## Learning comparison and source boundaries

The actual four-page Platform Training datasheet, code 25A24, was fully read: half-day instructor-led delivery, nine modules, a basic-database prerequisite and older notebook/function names. It is not a current assessment runtime or proof that every pictured workflow still works. The May 20, 2026 four-hour event was fully read, including closed registration and instructor Matthias Kolitsch; it is historical context rather than an upcoming available class.

The separate public Data Warehousing Workshop Badge 1 page says six hours in its effort field and 8–12 hours typical completion in its description. Both observations remain visible, and Hands-On Essentials Badge 1 is not conflated with the Platform Skills replacement. Its public course instructions say to wait for the prescribed trial-account setup. Neither DORA work nor lessons were accessed. Udemy returned HTTP403, so former 3h19m/April 2026 metadata is unverified.

Primary technical documents were read selectively as detailed in their source notes; the two actual PDFs were fully read. Release intake used official dated release notes, behavior-change notices and the training event, not an invented blog publication date. No private, paid, assessment-question or leaked material was used.

## Validation and remaining work

The operational record records repository tests, repository validation, learning-catalog consistency, strict site build, generated-site validation and diff checks when complete. The eight Snowflake labs and three integrated scenarios remain proposed, with permissions, failure evidence and cleanup requirements. Remaining limits are live execution, account-specific availability/behavior, inaccessible commercial metadata and independent human review. The five reserved GitHub guides and disabled notification pilot remain untouched.
