# SC-200 deep review — September 27, 2026

The complete [guide](../../guides/SC-200-microsoft-security-operations-analyst.md)
was read and **54 October objectives in nine groups** were individually mapped.
The accepted July 28 baseline remains separate from the October 21 revision.
The credential confirms a 100-minute assessment, twelve-month renewal and ten
exam languages. The instructor-led course remains four days.

## Learning changes

Five original worked examples explain custom collection budgets, identity-safe
automation, retained versus searchable history, same-event detection evidence
and source/ingestion/alert clocks. The guide now has **ten labs and 44 answered
checks**, including two new tabletop labs with explicit expected evidence.

The review updates September 23 Sentinel onboarding by customer cohort, historical
query selection and Fabric preview mirroring without backfill. It separates
Defender Continuous from Sentinel NRT, clarifies event/scoped-alert fields,
preserves threat-intelligence version/deletion order, and tests silent producers
against inventory rather than trusting a green connector. Live response, Graph
request evidence and MCP tool prerequisites have explicit operational limits.

Twelve offline checks verified the synthetic arithmetic, event tuple and identity
counterexamples, and public module/course/question sums. KQL was not executed.
No tenant, endpoint, incident, playbook, connector, Spark/Fabric, Graph/MCP or
destructive action was run. All ten labs remain learner exercises/tabletops.

## Open documentation findings

Two Microsoft source conflicts keep this review **reviewed with blockers**:

The new September 27 source-validation record is blocked. The original September 1
passed record is retained unchanged so earlier audits remain tied to their dated
evidence; it does not establish that the current product-documentation gaps are resolved.

- The [custom-detection guide](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules)
  lists Sentinel tables for Continuous, while
  [unified-hunting known issues](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender)
  still say Sentinel NRT custom detections are unavailable. Exact tenant/table
  eligibility needs authoritative clarification and validation.
- [Table settings](https://learn.microsoft.com/en-us/azure/sentinel/manage-table-tiers-retention)
  broadly warn of losing Advanced Hunting when moving to lake tier. Newer
  [release guidance](https://learn.microsoft.com/en-us/azure/sentinel/whats-new)
  and hunting guidance describe lake access, with a separate restriction for
  extended Analytics history. The guide records cohort, table and time-range
  distinctions; it does not promise universal access.

October 1 follow-ups target these findings, including related SC-100 architecture
guidance. A March 1 checkpoint precedes the March 31, 2027 Azure-portal support end.
The existing blueprint monitor separately tracks the October objective change.

## Resource and blog decisions

Ten Learn landing pages list 59 modules; earlier durations are historical and
individual modules were not timed or completed. Pluralsight lists three 2022–2024
courses totaling 6h09, rounded to six path hours. MeasureUp lists 170 questions
and an August 2026 update; no paid questions were reviewed. Microsoft Press
corrects the guide's older book metadata to Yuri Diogenes and Sarah Young,
320 pages, May 11, 2026. Its public contents do not prove complete July/October
coverage. O'Reilly/Packt and Udemy blocked retrieval; YouTube returned shells.
The public O'Reilly live agenda shows six hours, without verified event availability.
The lab README was read, not every lab instruction. Partner PDF retrieval did not
establish current event dates. No paid lesson or signed-in assessment was reviewed.

Two public Microsoft articles supply bounded exercises:

- [sagiyagen365's account-mapping post](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/update-changing-the-account-name-entity-mapping-in-microsoft-sentinel/4489040),
  February 10: use the July payload change to test identity-specific automation.
  The guide adds original counterexamples showing why substring compatibility
  filters alone are not authorization.
- [Microsoft Security Research, Yossi Weizman and Tushar Mudi's Storm-3168 report](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/),
  September 25: construct an operator timeline from workload identities,
  resource operations and data-plane evidence. Preserve uncertain initial access
  and unconfirmed exfiltration/ransom; do not reproduce destructive activity.

Public article text was read; videos, gated intelligence and deployments were not
reviewed or tested. Research, repair and checks used the same AI context;
independent and human review remain pending.

The evidence ledger is
`ADLC_Docs/operations/2026-09-27-sc-200-deep-review.json`.
It preserves the previous records, objective mapping, source observations,
guide hashes, findings and completed local validation.
