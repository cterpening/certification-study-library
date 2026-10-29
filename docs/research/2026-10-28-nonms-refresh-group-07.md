# Non-Microsoft certification refresh — Group 7

**Completed:** October 28, 2026  
**Guides:** 10 (Fortinet, GitHub, AWS)  
**Queue:** Group 7 of 17 from the frozen 167-guide eligible non-Microsoft queue. **Remaining after this group: 97 guides, approximately 10 groups.**

## Work completed

- Rechecked the current official objective or credential page, status and lifecycle information, and applicable first-party learning/product release channels for each guide.
- Refreshed ten guides and their objective/status check dates; synchronized learning-resource catalog entries for NSE-8, NSE-I-MSSP-SECURITY, GH-100 and GH-600.
- Added ten first-party source records for current GitHub, AWS and Fortinet material. Group source health covered 269 registered URLs: **248 returned HTTP 200, 21 were access-limited, and none were missing or errored** after classifying one Fortinet login redirect as blocked. Nineteen source metadata changes were flagged for inspection.
- Preserved changed Fortinet objective/status snapshots under dated October 28 names and restored stable snapshot paths for earlier receipt integrity. GH-600's July 2026 published outline remains current; its credential page now presents a regular active certification rather than beta.
- Kept Fortinet MSSP Security in `review-required`: its canonical page still says “Coming soon!” and publishes no objectives or availability date. The guide remains a preparation foundation, not an exam blueprint.

## Guide-specific updates

| Exam | Current finding or useful new content |
|---|---|
| NSE-8 | Rechecked the Core Practical plus one elective path, prerequisites, two-year credential term, renewal and transition rules. The top-level page is a brief program summary; the Core and elective detail pages remain the technical outline. Electives remain scheduled for Dec 2026, Jan 2027 and Mar 2027. |
| NSE-I-MSSP-SECURITY | Canonical page still has no published blueprint or date. The current broader catalog gives only the purpose and prerequisite summary. Fortinet's Industry exam price is scheduled to rise from USD 200 to USD 400 on Nov 2; verify current availability and price before booking. |
| GH-100 | July 2026 exam outline is unchanged. October enterprise updates cover enforceable enterprise Advanced Security configurations and externally synchronized, read-only repository properties usable in filters and ruleset targeting. |
| GH-600 | Current Microsoft credential page lists a regular certification, a 120-minute proctored exam, potential interactive components, English and annual renewal. GitHub Agentic Workflows reached GA Oct 28, with read-only defaults, sandboxing, safe outputs and threat detection; this is related product context, not an exam objective by itself. |
| AIB-C01 | Beta delivery began Sep 29. Credential page lists 85 questions, 170 minutes, USD 50 beta pricing (USD 100 standard), English/Japanese, and an early-adopter badge through Feb 15, 2027. It conflicts with the detailed guide's 130-minute duration; the discrepancy remains explicit, not silently reconciled. |
| AIF-C01 | April 30 revision 1.1 remains current. The Italian and German exam languages retired Oct 15; the certification remains active. Guide distinguishes practitioner-level AWS AI service knowledge from AIB-C01 business strategy. |
| AIP-C01 | Current guide remains in effect. AgentCore Runtime V2 and October Gateway inference protocol changes are dated service context, qualified by version and regional availability. |
| ANS-C01 | Current English AWS page confirms Dec 31, 2026 retirement. Credentials earned earlier retain three-year validity; no replacement certification is named. The Japanese-page date discrepancy and scheduler caveat remain visible. |
| CLF-C02 | Added Amazon ECS Gateway (Oct 20) as a managed ingress option for ECS. The service/account setup and application opt-in, supported `awsvpc` launch types and continuing underlying charges are included as current service context. |
| DEA-C01 | Added S3 Tables Iceberg V3 data types, column defaults, deletion vectors and row lineage (Sep 30); Redshift V3 support remains separately dated. These changes do not alter the published exam outline. |

## Source health and review limits

The source sweep checked 269 registered URLs: 248 returned HTTP 200, 21 blocked automated fetching, and none were missing or errored after classifying the Fortinet exam-pricing article's `login_required` redirect as access-limited. Fortinet's article was reviewed through the public indexed vendor page. Other access limits include paid course listings, CISA, several AWS documentation pages, and ISO/O'Reilly/Udemy pages. Automated access limits are not treated as evidence that a page is dead or technically incorrect.

No authenticated exam, Pearson VUE booking, Fortinet candidate portal, paid course interior, live cloud tenant, or product lab was accessed. All refresh work and the final audit are AI-assisted and same-context; no independent or human review is claimed.

## Selected first-party sources

- [Fortinet NSE 8 certification requirements](https://helpdesk.training.fortinet.com/support/solutions/articles/73000665295-what-are-the-nse-8-certification-requirements-and-prerequisites-) and [renewal points](https://helpdesk.training.fortinet.com/support/solutions/articles/73000665764-how-do-i-renew-my-nse-8-certification-after-july-15-2026-)
- [Fortinet certification program catalog](https://www.fortinet.com/training-certification) and [exam-fee change](https://helpdesk.training.fortinet.com/support/solutions/articles/73000671071-what-will-be-the-exam-prices-and-recertification-assessments-after-july-15-2026-)
- [GH-600 credential page](https://learn.microsoft.com/en-us/credentials/certifications/agentic-ai-developer/) and [GitHub Agentic Workflows GA announcement](https://github.blog/changelog/2026-10-28-github-agentic-workflows-generally-available/)
- [October GitHub enterprise roundup](https://github.com/resources/insights/enterprise-content-roundup-october-26)
- [AWS AIB-C01 certification page](https://aws.amazon.com/certification/certified-ai-business-strategist/) and [launch announcement](https://aws.amazon.com/blogs/training-and-certification/introducing-aws-certified-ai-business-strategist-built-for-the-people-who-scale-ai/)
- [AWS AgentCore release notes](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html)
- [AWS ECS Gateway announcement](https://aws.amazon.com/blogs/aws/introducing-amazon-ecs-gateway-a-fully-managed-ingress-solution-for-ecs-services/)
- [Amazon S3 Tables Iceberg V3 announcement](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-s3-tables-iceberg-v3-data-types/)
- [ANS-C01 live lifecycle page](https://aws.amazon.com/certification/certified-advanced-networking-specialty/)

## Evidence

The [operations record](../../ADLC_Docs/operations/2026-10-28-nonms-refresh-group-07.json) binds guide hashes, objective/status snapshots, source-validation receipts, source health, and audit status. Structured source-freshness, audit and deep-review receipts are recorded in `data/source-freshness.json`, `data/ai-audits.json` and `data/deep-reviews.json`.
