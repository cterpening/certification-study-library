# Practice-first diagram review — November 10, 2026

This follow-up applies the staged review process to the AZ-900 governance-scope
and DP-900 SQL-choice exercises. Both remain independent AI-assisted resources
with human review pending. The official
[AZ-900](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900)
and [DP-900](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)
blueprints define exam scope. This is selected-topic exercise review, not a
whole-guide audit or an exam-readiness assessment.

## Roles and sequence

The coordinator and two fresh-context reviewers used **`gpt-6-astra`**, reasoning
effort **`ultra`**. The coordinator verified these values in the active turn
metadata for all three runs, rather than assuming the saved model default was
active. No model override was requested. This records the current follow-up;
it does not retrospectively identify the models used for earlier authorship.

Each reviewer first received only its practice SVG and rendered PNG, with
permission to read repository policies. The study sheet, answer, source guide,
exercise README, brief, builder, prior reviews, and authoring conversation were
withheld. Reviewers solved the rendered worksheet before inspecting its SVG
title/description. Both reported that no external sources or answer materials
were used in this first stage. Their responses were recorded below at
**17:24:41 UTC, before the second-stage handoff**.

This is independent-context review using the same model. Its existing product
knowledge can help solve the exercise; the attempt is not evidence of novice
learning or model diversity. Source verification follows separately.

## Stage 1: AZ-900 response, preserved before answers were released

The reviewer identified the subscription-level location policy as the reason
for the block: East US is allowed, West US is requested, and the stated role
permission does not satisfy the location requirement. It proposed inspecting
the failed deployment error, policy evaluation details, assignment parameters,
scope, exclusions, and exemptions. A broader role would not resolve the stated
violation; use an allowed location or pursue an authorized policy adjustment or
exemption if West US is required.

The reviewer initially assumed that the policy was enforced and no exclusion or
exemption applied. It then found that the accessible description explicitly
supplied that premise while the rendered sheet only said “Applicable here.”
This is a difference in information available between presentations. The
description also omitted the visible instruction to explain the answer before
opening the study version. Neither accessibility field directly named the cause
or supplied the broader-role answer.

The main text, nested boundaries, and prompts were readable without observed
clipping. Smaller footer text and the role card's position inside the
subscription enclosure were noted as potential novice/reduced-size concerns;
the role's explicit resource-group scope and connector resolve its intended
meaning. No actual Azure execution or screen-reader test occurred.

Original practice SVG, raw SHA-256:
`ab71b0b518ad3af958d0a6993d0869b7d193d5cb57425dc14abd5b045307a03c`.
Original viewed PNG, raw SHA-256:
`9684265cb69275f277d370fec43fbe382356438c411e1a2bc135835281e74564`.

## Stage 1: DP-900 response, preserved before answers were released

| Requirement | Reviewer's candidate and tradeoff | Reviewer's next check |
|---|---|---|
| A: one compatible database; no instance/OS dependency | Azure SQL Database; managed platform with reduced OS/instance control | SQL features, performance needs, and recovery configuration |
| B: instance-level features and managed OS upkeep | Azure SQL Managed Instance; instance scope with compatibility and OS-control constraints | Exact features, migration dependencies, support, and recovery plan |
| C: guest OS agent and SQL installation control | SQL Server on Azure Virtual Machines; greater OS/SQL administration responsibility | Vendor support for the VM, OS, SQL version, agent, and recovery configuration |

The reviewer retained customer responsibility for application, data, access,
and business recovery decisions across all three. It treated the choices as
candidates requiring exact compatibility checks, not complete deployment
decisions. Missing capacity, cost, availability, recovery, and migration details
limit production conclusions. Requirement A assumes compatibility; B does not
establish support for every possible instance-level feature.

The stacks, labels, and boundaries were readable without observed clipping.
The reviewer noted smaller secondary/footer text, limited handwriting space,
and strong reference cues: this is guided application practice with little
evidence of unaided product recall. The visible “SQL engine platform” label
could imply too much Microsoft responsibility. The accessible description's
clarification that the app/data/access layer represents decisions rather than
hosting inside the SQL service was absent from the rendered sheet.

No keyed answer leakage was found in the title/description: neither assigns
a product to A, B, or C. No current-source check, vendor validation, screen-reader
test, print test, or learner test occurred in this stage.

Original practice SVG, raw SHA-256:
`fbc175be72062782477f46008226a8ecc3a685816e94e63953adf3abfbd20bef`.
Original viewed PNG, raw SHA-256:
`5ec10ccd13cd99a54d91a4a0389b20d307c14afab3b6e2c174f77800302a162f`.

## Stage 2 and repair/recheck

The second-stage handoff supplied the complete unchanged guide, accepted
objective snapshot, source package and unit, all exercise files, rendered study
sheet, source URLs, and repository rubric. Each reviewer compared its recorded
solution with the worked answer and opened the relevant current Microsoft pages.
Both independently arrived at the intended answers. Technical distinctions and
selected-objective mappings passed, with the following required visual repairs.

| Finding | Severity | Author repair | Recheck |
|---|---|---|---|
| AZ-900: exclusion/exemption premise appeared only in accessible/accompanying text | Medium | Added the premise visibly inside the Policy card in both sheets | Closed; both rendered sheets and text checked |
| AZ-900: practice description omitted the practice-before-study instruction | Low | Added the visible instruction to the practice description | Closed; no answer leakage introduced |
| DP-900: layers could imply application hosting or complete Microsoft responsibility for SQL administration | Medium | Labeled customer decisions and engine upkeep, clarified hosting separately, and retained database administration/tuning/security responsibilities visibly and in text | Closed; rendering and text agree |
| DP-900: Managed Instance example did not clearly state a tradeoff | Low | Explained managed OS upkeep with relinquished guest OS control, while retaining exact-feature verification | Closed; study sheet and README agree |

The coordinator repaired the source builders and DP-900 text explanation,
regenerated both pairs and manifests, and rendered four new previews. The same
reviewers received those exact revised artifacts for targeted recheck. Original
stage-one responses and original preview files were preserved; no second blind
attempt is claimed after answers had been exposed.

**Final scoped verdict: both pairs pass after repair and recheck.** Both reviewers
closed their medium and low findings, found no new blocking issues or clipping
at 1200 × 1400, and passed the respective `build.py --check` command. This verdict
applies to the exact revised artifacts below. It does not establish learner
effectiveness, human review, or print usability.

Technical evidence opened by the reviewers includes the official blueprints
linked above, [RBAC overview](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview),
[Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview),
and [Azure SQL Administration comparison](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview?view=azuresql#administration).
These support the scope/permission/requirement distinction and the separation
of platform upkeep from continuing customer database administration. The
scenario-specific names, locations, and requirements are original invented
teaching inputs.

## Version bindings and limits

| Input | AZ-900 | DP-900 |
|---|---|---|
| Complete guide, normalized SHA-256 | `09dafd7ca0dffee692577828c9efca74232f668469361d83e4a2b081c0d021f0` | `1c618b776923450c7bbf59aac51ce2bf3b64cfb5dcc214e6b4b388a718332991` |
| Accepted objectives, raw SHA-256 | `8b4c89d325b3ce339eb881aa2dc4b251888e6d7a07d6351d81bcc2123b1c4449` | `7cef780d1a9e8e88b587fba89acb994985c4aedbd491710e814686ce5dc6559f` |
| Revised study SVG, normalized SHA-256 | `178b8e00a468d3a9e03accf2951bfe22c93aa9c2d6d2f4d9a28a76bec0c68de6` | `5f16442a2c6ffb86adbf2be8a3ae74e680f844c8888a29e68511bcfc5d8ef1a5` |
| Revised practice SVG, normalized SHA-256 | `cd0ae6e98c5ed800e2d4e8bbaa9da4167b228c1cf993dadc8f773caa293d8c68` | `44e452c67be79fda57a9e3344a06342fe09340bfa0a489726b09fa0266c54bee` |

The [AZ-900 manifest](../../examples/visual-exercises/az-900-governance-scope/manifest.json)
and [DP-900 manifest](../../examples/visual-exercises/dp-900-sql-choices/manifest.json)
bind revised outputs/builders to unchanged source units and original icon bytes.
The [earlier review](2026-11-10-diagram-expansion.md) remains a historical record
of the earlier artifact versions; this follow-up does not rewrite its verdict.

These are zoomable screen exercises. Small footer/ownership labels, fixed
layouts, and limited handwriting space need separate validation or a different
layout before claiming standard-page print usability. A reference matrix makes
the SQL task guided application practice; it does not test unaided product
recall. No screen reader, physical print, actual learner, vendor compatibility,
or live Azure execution was tested. Human review and informal learner feedback
remain pending. Canonical guides, accepted baselines, source catalogs, and
whole-guide review dates are unchanged.

## Optional learner trial, not yet performed

Ask a person to explain one diagram, then present a new variant without showing
its answer. Record their reasoning, misunderstandings, and help needed:

- **AZ-900:** Keep the stated permission and assignments but request East US.
  Which demonstrated obstacle is removed, and what remains insufficient to
  guarantee deployment?
- **DP-900:** A workload needs instance-level SQL features and must install a
  guest OS agent. Which requirement determines the initial candidate, and what
  must be verified before deployment?

Facilitator expectations: the AZ-900 location mismatch is removed, while other
deployment checks remain unknown; the DP-900 OS-control requirement points to
evaluating SQL Server on Azure VMs, subject to exact feature/vendor support and
operational validation. These are original transfer questions, not exam items.
Until someone actually participates, this section is a trial plan rather than
learner evidence or human approval.
