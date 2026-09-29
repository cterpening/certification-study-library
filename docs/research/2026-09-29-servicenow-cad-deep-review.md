# ServiceNow CAD deep review — September 29, 2026

The [CAD guide](../../guides/SERVICENOW-CAD-servicenow-certified-application-developer.md) now maps 22 canonical subtopics, answers 40 original readiness prompts and includes three worked scenarios, eight proposed instance activities and 38 executed local JavaScript checks. Live ServiceNow testing and independent human review remain pending.

## Current scope and preserved history

The [canonical blueprint](https://learning.servicenow.com/lxp/en/credentials/certified-application-developer-mainline-exam-blueprint?id=kb_article_view&sysparm_article=KB0011498) still carries January 2026. A fresh unsigned browser recovered the complete main body before the sample-question section. The six domains have 4/5/4/4/2/3 subtopics and weights 20/20/20/20/10/10. September 17 guide headers already used those weights, but the final checklist and saved snapshot retained 15/20/20/20/10/15. This review repairs the drift, preserves the prior exact snapshot bytes and redirects historical audit/review references. It does not announce a new exam cutover. Sample questions were excluded before saving or printing and were not used.

The blueprint confirms 60 multiple-choice/multiple-select questions in 90 minutes, Pearson test-center/OnVUE delivery and a 90-day registration-to-completion window. It recommends six months of application-development experience and three named courses; recommendations are not formal registration prerequisites. Cut score is undisclosed, results conditional and section percentages not a pass formula. Annual maintenance remains separate. The direct monitor still returns an empty body: manual browser verification is not successful automated extraction.

## Teaching and actual execution

All 38 original checks passed in Node.js. Trusted-label access cases distinguish cross-scope script requirements from web-service enablement and caller permissions. A junior role fails an explicitly senior-only requirement; a field grant cannot repair failed table access. These are chosen teaching policies, not authentication or a complete ACL engine.

A fixed six-record pagination fixture applies the limit before access filtering: its first page is empty, but later pages yield authorized IDs 3 and 6. Bounded continuation rejects cycles and duplicate identities. The fixture supplies its own continuation and does not claim the live Table API supplies that field, offers a consistent concurrent snapshot or follows this exact collector contract. A small structured-filter validator rejects unknown fields, operators, extra properties and encoded-clause injection; it is not an encoded-query parser.

An in-memory receipt model applies a version-3 close once, distinguishes exact replay from conflicting key reuse, rejects stale writes and preserves a later version-5 repair when an old request repeats. It proves sequential behavior only, not crash durability, transactional coupling or distributed atomicity. Two practice-bank arithmetic checks confirm the public 120-question allocation, not exam readiness. No instance, credentials, platform scripts, API calls, paid questions or external messages were used.

## Primary findings

The [API reference](https://www.servicenow.com/docs/r/api-reference/scripts/p_GlideServerAPIs.html) separates GlideRecordSecure's standard ACL checks from query-ACL opt-in and identifies distinct methods for untrusted user queries and trusted system conditions. Only those indexed primary sections were read, not the whole API reference. The guide requires a narrow input contract, explicit permitted outputs and installed-version verification.

The [REST reference](https://www.servicenow.com/docs/r/api-reference/rest-api-explorer/c_RESTAPI.html) states that limits precede ACL filtering, invalid query portions can be dropped and cross-scope CRUD switches do not govern web-service requests. The guide separates web-service enablement and caller permissions from script privileges, explains empty-page continuation and avoids suggesting a global query-property change as a local fix. REST Explorer can mutate data; no requests were submitted.

The primary ACL overview supports table-plus-field authorization, qualifying a community junior/senior example that omitted the table grant. The article's broad server-script claims, illustrative ACL-call arithmetic and pasted code were not adopted as execution evidence. The [Deny-Unless page](https://www.servicenow.com/docs/r/platform-security/access-control/acl-denial-behavior.html) contradicts itself on the no-Allow-If case; that remains unresolved.

The [source-control reference](https://www.servicenow.com/docs/r/application-development/servicenow-studio-classic/source-control-integration.html) supports nonproduction global/scoped metadata workflows and describes shared repository credentials and external-edit sanitization. Git history alone does not prove individual credential isolation or installed-state safety. The ATF design reference requires isolated fixtures and documents custom UI retrieval/transport limits. Proposed labs preserve nonproduction boundaries; no ATF or promotion was run. Planning, Business Rule, coalesce and tracked-customization sources supply the documented scope, context and transport qualifications.

## Catalog and release boundaries

MeasureUp's complete public product main lists 120 questions dated March 2026, allocated 24/24/24/24/12/12. That matches the current blueprint and resolves the earlier allocation discrepancy; generic roughly-150 wording remains inconsistent. Translation, guarantee and readiness advertising is not official exam language or scoring policy. No demo or question interiors were opened.

Course routes remain loading shells. Older three-day course anchors, three-hour Welcome duration, O'Reilly's 2017 context/11–15 hour estimate and Udemy's February 2026/6h37 metadata were not reverified. Three resources returned HTTP 403. The May community thread's four-domain 80% calculation now matches the canonical weights, but its replies cannot guarantee preparation sufficiency or exclusions from a non-exhaustive blueprint. The vendor YouTube channel was not played.

The August 13 Developer Passport announcement advertises eleven September 14–18 Brazil preview sessions. Its article main was read during the preceding same-session CSA review; videos were not watched. Fresh primary documents show Brazil/September 10 while indexed references can still show Australia/March 12. Neither metadata nor previews establish general availability or exam cutover.

Public Pearson and CMP main bodies were read in the same session, but no assigned maintenance deadline or future window was verified. Per-source records distinguish those readings from direct empty captures and other indexed/browser bodies. Twenty-nine direct receipts show 26 HTTP successes and three blocked resources; success alone does not establish a readable article.

## Evidence and remaining work

The operation at `ADLC_Docs/operations/2026-09-29-servicenow-cad-deep-review.json` records prior records, objective mapping, manual acceptance and archive hashes, source reading boundaries, exact local code/output and repository gates. Remaining work is contradictory primary wording, installed behavior, assigned maintenance, inaccessible course/practice interiors and human review. The five reserved GitHub guides and disabled notification pilot remain untouched.
