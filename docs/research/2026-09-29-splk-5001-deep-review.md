# Splunk Defense Analyst deep review — September 29, 2026

The [guide](../../guides/SPLK-5001-splunk-certified-cybersecurity-defense-analyst.md) maps 24 public objectives, answers 40 original prompts and adds three worked investigations, eight proposed activities, 49 executed offline Python checks and two unexecuted SPL demonstrations. Course access, real platform practice and human review remain pending.

## Exam scope and lifecycle

All four pages of the [detailed blueprint](https://www.splunk.com/en_us/pdfs/training/splunk-test-blueprint-cybersecurity-defense-analyst.pdf) and the complete one-page track were read from genuine PDF bytes. Objective counts remain 3/5/3/6/3/4 and weights 10/20/20/20/20/10 percent. The 66-question exam provides 75 total minutes including three for the agreement. The public certification page still lists $130 per attempt, Pearson delivery and no formal exam prerequisite; Power User knowledge is recommended. No replacement was announced on that page.

The preexisting monitored snapshot intentionally covers the landing overview. Its unchanged result does not verify every PDF objective. This review preserves that baseline and separately records detailed manual mapping, extracted objective text, PDF hashes and reading boundaries. No historical snapshot was rewritten.

Selected [candidate handbook](https://www.splunk.com/en_us/pdfs/training/splunk-certification-candidate-handbook.pdf) pages, version 05.05.26, distinguish career progression from renewal. Defense Analyst has no next-level or downstream renewal entry in its tables; Engineer/Architect recommendations in the learning track do not establish that eligibility. Same-exam recertification belongs in the final year. Account state and booking details were not inspected. The full handbook and its legal agreement were not audited.

## Technical teaching and executed evidence

The [tstats reference](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/search-commands/tstats) distinguishes default mixed summarized/unsummarized searches from explicit summary-only coverage. Null grouping fields can also explain missing rows. Authentication teaching clarifies client source, initiating versus target user and the difference between test-required field markings and universal event requirements. Processing order is separated from chronological order; transaction bounds and memory behavior are qualified.

The [detection documentation](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.6/detections/use-detections-to-search-for-threats-in-splunk-enterprise-security) has a general prohibition on both output types alongside explicit 8.1+ support through risk modifiers. The guide uses version-specific teaching and records the contradiction. Risk entity normalization and context zones explain why identical display names are insufficient identity keys. Some user/system examples appear swapped and were not adopted verbatim.

The original Python fixture shows replay inflation from 100 to 130, summary-only evidence of 50 and a later distinct contribution raising the deduplicated value to 125. A chosen threshold is neither a probability nor a vendor default. Missing identity, event/ingest time, half-open windows, independent tenant/type keys, ordering, timezone normalization and misleading incident averages are exercised. A fictional approval object rejects changed plans, expiry and revocation. Its digest is not authentication or a production authorization system. All 49 checks passed; no Splunk engine or response action ran.

Newer [agent workflow documentation](https://help.splunk.com/en/splunk-enterprise-security-8/administer/8.7/ai-assistant-in-security-and-agentic-capabilities/setting-up-the-ai-soc-analyst-agentic-workflow-in-splunk-enterprise-security) also contains overly broad read-only language beside settings for investigation creation, finding closure and response. Specific configuration and inherited permissions govern actions. Suggested disposition differs from analyst disposition. The September vendor blog and AI workflow provide practical context, not additional exam scope; no entitlement or deployment was tested.

## Sources and remaining boundaries

Twenty-nine direct receipts contain 15 HTTP successes and 14 blocks. Several blocked primary help pages were readable through the indexed web reader; their exact selected or complete-main boundaries are recorded separately from direct HTTP health. No access control was bypassed. Genuine PDF captures include four-page blueprint, one-page track, 26-page handbook, 32-page study guide and two-page investigation-course description. Only the first three study-guide pages were read; sample items were not used. Blueprint page 2 and the handbook next-level renewal table were also visually inspected.

The [Art of Investigation description](https://www.splunk.com/en_us/pdfs/training/the-art-of-investigation-course-description.pdf) confirms five stages but does not name them. Its three ride-along ranges total 200–285 minutes, excluding introduction and quiz. Exact labels remain a course-access blocker. Free-training cards are listings, while the dynamic general catalog returned no results. Public Pluralsight metadata lists 1 hour 36 minutes; paid interiors and blocked Udemy/O'Reilly metadata were not verified. No videos were played.

The complete [BOTS v3 README](https://github.com/splunk/botsv3) is historical compatibility evidence, not a recommendation to install its old versions. No dataset or solution material was consumed. Lantern categories and Security Content inventory do not establish tested deployment coverage.

The operation record at `ADLC_Docs/operations/2026-09-29-splk-5001-deep-review.json` retains prior records, all reading boundaries, detailed PDF mapping, exact executed code/output and repository gates. The five reserved GitHub guides and disabled notification pilot remain untouched.
