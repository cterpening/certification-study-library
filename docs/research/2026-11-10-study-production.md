# Study production pilot — November 10, 2026

This change implements two repeatable processes in the certification library:
study-content preparation/building and separate podcast preparation/rendering.
See the [operating instructions](../STUDY-PRODUCTION.md),
[visual study companion](../../examples/study-packs/az-900-governance/study-guide.md),
and [two-host transcript](../../examples/podcasts/az-900-governance/part-01/transcript.md).

## Scope and evidence

The pilot covers five AZ-900 objectives through three original learning units:
Azure RBAC and Azure Policy; resource locks; and tags with cost management.
The complete unchanged AZ-900 guide and its accepted objectives were read during
research and independently during review. The official blueprint still identifies
the July 20, 2026 skills baseline. This investigation does not renew the guide's
October 28 review date or constitute a complete technical refresh.

Exact official evidence opened for this scoped work:

| Source | Supported distinction |
|---|---|
| [AZ-900 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) | Five selected objectives and published baseline |
| [Azure RBAC overview](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) | Principal, role definition, scope, and permission grants |
| [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview) | Governance rules and effects, including current identity-aware capabilities |
| [Policy remediation](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources) | A noncompliance finding is not a completed remediation |
| [Resource locks](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources) | Lock levels, inheritance, management operations, and data-plane boundaries |
| [Resource tags](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources) | Parent resource tags are not automatically copied onto child resources |
| [Cost Management tag inheritance](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/enable-tag-inheritance) | Supported inheritance enriches usage records rather than resource metadata |

These sources were already registered for AZ-900; no source catalog, accepted
baseline, review ledger, or canonical guide was changed. New explanations,
scenarios, diagrams, and dialogue remain AI-generated draft, human review pending.
There was no Azure execution or use of assessment questions.

## Production results

The study builder reads full existing inputs, validates exact references, and
renders a companion, three SVG diagrams with text alternatives, and three original
recall cards. Its manifest binds all outputs to the inputs. The authoring packet
supports semantic expansion by an agent or person; the deterministic builder does
not claim to perform unattended research or write substantive teaching by itself.
Registered seeds without guides receive an explicit new-guide intake task.

Podcast preparation produced 1,349 spoken words in one two-host part, estimated at
9.3 minutes at 145 words per minute. The 15-minute example target did not pad or
truncate the content. Smaller targets split at topic boundaries. Its render plan
contains 8 service requests and 8,989 spoken characters. This is an estimate of
production input, not measured runtime, service cost, or recorded audio.

The first adapter is ElevenLabs Text to Dialogue; the [service comparison](../../adapters/podcast-services.md)
records official API evidence and alternatives. No external speech request was
made. Tests use synthetic PCM and a local HTTP server. Service availability for
the chosen account, voice quality, pronunciation, continuity between chunks,
actual cost, and listening review remain untested.

## Review and repair

The coordinator performed implementation and output checks. A separate fresh-context
agent reviewed the selected-objective content and script after reading the complete
unchanged guide, exact objective snapshot, generated outputs, and official sources.
It found one low navigation issue, repaired by adding guide and visual-companion
links. It verified the changed artifacts and unchanged script, concluding **pass,
zero open scoped findings**. The podcast's script-review receipt records AI review.

A separate fresh-context implementation reviewer found that a truncated HTTP
chunk could escape the renderer's failure receipt, that authored unit IDs could
collide with generated chapter IDs, and that blueprint administrative labels could
be mistaken for objectives. All were repaired and covered by regression checks.
The reviewer confirmed the transport fix with a loopback reproduction and checked
the input-validation repairs. No material implementation finding remained.

Neither agent review is human/community review or a full-guide semantic audit.
No new full-guide review receipt was entered. Browser rendering confirmed the
three SVGs have readable, unclipped labels and arrows; the accessible text retains
the same relationships. Audio listening remains pending.

## Reviewed version bindings

Text hashes normalize CRLF/CR to LF. The objective snapshot's raw hash matches its
normalized hash because its committed line endings are fixed to LF.

| Input or artifact | SHA-256 |
|---|---|
| Full source guide | `09dafd7ca0dffee692577828c9efca74232f668469361d83e4a2b081c0d021f0` |
| Accepted objectives | `8b4c89d325b3ce339eb881aa2dc4b251888e6d7a07d6351d81bcc2123b1c4449` |
| Authored content JSON | `b24c70e3032ec2a59ea63cbd168368ba72283f9f193919bb6bc5ea0d4dfabd23` |
| Study companion | `38fe4bffe5dd1e56d6340cdf7743ea0acdc735e65e1f6d6786096bc31865fa60` |
| Package manifest | `fa82722db742d1e1889f3a80192487b691452596e613963c755dd76be4157d28` |
| Podcast script | `dc05cff6ccef090f8e9a243d4162ce8027a69a0894d642aad7f135b22666a232` |
| Transcript | `57605e310d4afdd6cdae53472e803ccf043ca686938ef6e2d9ecf329e8097861` |

## Validation boundary

Local validation includes the complete unit suite, focused failure regressions,
an offline command-line run of both processes, repository validation, reviewed
learning-resource drift checks, a strict MkDocs build, and generated-site checks.
The final full suite ran 238 tests successfully, with two Windows symlink privilege
skips. All 39 study/podcast tests passed with the same two skips in the focused run.
GitHub check results are recorded with the delivery pull request.

The manual Actions workflows produce reviewable artifacts using read-only repository
permissions. They do not run an unattended editor, call a paid speech service, or
publish audio. Existing scheduled objective/discovery/source-health checks continue
to identify updates. The next production step is a small service/voice trial and
listening review, followed by a complete-certification series.
