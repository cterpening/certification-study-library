# Weekly notification pilot

Selected September 28, 2026. Reserve the **first five pending certificates** for the notification pilot while the remaining guide reviews continue.

## Reserved certificates

Selection is reproducible: read `config/exams.json` in its existing order, exclude certificates with a receipt in `data/deep-reviews.json`, and take the first five. This records the current review program's queue; earlier source validation and guide development remain separate evidence. GH-300 is skipped because it already has a receipt.

| Order | Certificate | Pilot review status |
|---|---|---|
| 1 | [GH-900 — GitHub Foundations](../guides/GH-900-github-foundations.md) | Reserved; manual baseline review pending |
| 2 | [GH-200 — GitHub Actions](../guides/GH-200-github-actions.md) | Reserved; manual baseline review pending |
| 3 | [GH-100 — GitHub Enterprise Administrator](../guides/GH-100-github-enterprise-administration.md) | Reserved; manual baseline review pending |
| 4 | [GH-500 — GitHub Advanced Security](../guides/GH-500-github-advanced-security.md) | Reserved; manual baseline review pending |
| 5 | [GH-600 — Developing in Agentic AI Systems](../guides/GH-600-developing-agentic-ai-systems.md) | Reserved; manual baseline review pending |

This is a reservation in the review process, not a filter in the monitoring scripts. Scheduled source checks continue to include these guides. Keep urgent retirement, deadline and accuracy corrections current, recording the evidence before and after each change. Do not defer an urgent correction merely to preserve a test case.

The next ordinary review batch moves past this reserved GitHub set to AWS, following the agreed vendor sequence. The five pilot guides return for manual review when establishing the notification test baseline. Commit and push each completed certificate's changes separately.

## Establish expected results before testing

1. Manually review each reserved guide and its current official sources. Record what is confirmed, unresolved, newly changed and due for another check. The reservation does not establish current vendor status or completed review.
2. Preserve the guide, accepted objective snapshot, source evidence and report versions used for comparison. Apply supported content corrections and record the actual review outcome.
3. Derive expected notification decisions from that evidence before executing the notification logic. A certificate awaiting review is not automatically an unchanged control.
4. Use isolated fixture copies for cases absent from current vendor evidence. Label those inputs synthetic; never change accepted production snapshots or published retirement dates to manufacture an alert.

## Required scenarios

These are acceptance criteria for the future notification implementation, not results of executed tests. Keep the reserved set fixed; use its review packets to cover the following behaviors.

| Scenario | Expected notification decision |
|---|---|
| All checks complete, no new changes and no review due | No notification |
| Confirmed new objective or lifecycle change | Notify with affected exam, evidence and required review |
| A tracked review becomes due | Notify when it first becomes due, even if source content is unchanged |
| Required source or collection step fails | Report the incomplete check; never describe it as a clean pass |
| The same finding is seen again without a new change or due date | Keep it visible in the report; suppress a duplicate notification |

Record the expected and actual decisions, report version, finding identity, notification text and any discrepancy. A failed comparison blocks notification rollout. These five guides share a vendor; their results do not establish coverage of every vendor's extraction format.

## Rollout boundary

First run the pilot with notification delivery disabled. Then inspect one complete weekly report and its proposed notification. Enable conditional delivery only after expected and actual outcomes agree and the recipient's GitHub email settings are confirmed. Keep AI research/editing manually triggered initially.

**Current state:** selection recorded; five manual baseline reviews pending; notification scenarios not executed; conditional email delivery not implemented or enabled. The existing weekly checks and maintenance issue workflow continue as documented in [Automation](AUTOMATION.md). This pilot does not claim that existing GitHub issue or workflow notifications are disabled.
