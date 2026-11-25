# Repeatable study guides, visual aids, and podcasts

The library has two separate production processes. Study production reads an exam's
existing guide, accepted objectives, and source records to prepare a bounded writing
task. An author or research agent expands the material, and the builder turns that
authored content into a study companion, recall cards, and editable SVG diagrams.
Podcast production consumes a particular study package and creates a two-host
script, transcript, and parts that can be rendered through a speech service.

The [study podcast library](../examples/podcasts/README.md) includes recordings of
the two original pilots and four follow-up conversations about cloud reliability,
hosting responsibilities, delayed event counts and relational joins. The index
provides audio, measured durations and transcripts.

The first example teaches three AZ-900 governance distinctions: role-based access
control versus Policy, resource locks versus data protection, and tags versus access
and cost allocation. It is selected-objective practice, not a replacement for the
complete [AZ-900 guide](../guides/AZ-900-microsoft-azure-fundamentals.md).

Read the [example visual companion](../examples/study-packs/az-900-governance/study-guide.md)
and [two-host transcript](../examples/podcasts/az-900-governance/part-01/transcript.md).
The script was originally estimated at nine minutes. These are dated, reproducible
examples. Rebuild from reviewed
inputs when their source binding becomes stale.

The second pilot is [DP-900 data decisions](../examples/study-packs/dp-900-data-decisions/study-guide.md),
with four visual chapters and a [two-host transcript](../examples/podcasts/dp-900-data-decisions/part-01/transcript.md)
estimated at 11.5 minutes. It samples all four domains through selected objectives,
without claiming complete exam coverage. Use the [ElevenLabs/GenFM pilot guide](GENFM-PILOT.md)
for signup and ready-to-upload source files for either pilot.

Both processes retain **AI-generated draft; human review pending** status. Reading
files, matching hashes, rendering diagrams, and synthesizing speech do not establish
technical correctness. The official exam blueprint remains authoritative.

## Add an inline guide diagram

Use this workflow when a learner needs to **trace a relationship**. In the
[AZ-900 example](../guides/diagrams/az-900/role-scope.svg), one role assignment
branches into three questions a learner can ask when inspecting it.
A side-by-side feature comparison often reads better as a table.
Use the [visual study brief](templates/VISUAL-STUDY-BRIEF.md) when the task calls
for a timeline, a scope map, or a separate practice sheet with a withheld answer.

1. **Choose the question and evidence.** Pick one heading in the guide and one
   objective from its accepted snapshot under `data/objective-snapshots/`. Open the
   supporting source and check what each arrow will mean. Use the IDs from
   `data/sources.json` registered for that exam. For the example, see *How Azure
   RBAC works* and the AZ-900 identity and access objective. [RBAC overview](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) · [Official AZ-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900)
2. **Describe the figure.** In your checkout, copy
   `guides/diagrams/az-900/role-scope.json` to
   `guides/diagrams/<lowercase-exam-code>/<topic>.json`. Use a short lowercase
   filename with hyphens between words. Set `exam_code` to the catalog code and
   fill in the exact `guide_section`, `objective`, and `source_ids`. Give the
   figure a title. Each node has an ID and a visible label. Each edge names a
   starting node, an ending node, and the relationship between them.
3. **Build and inspect.** Run the first command below from the repository root.
   Open the sibling SVG in a browser at the size a learner will see it. Follow
   each arrow aloud and check that its direction, label, and destination express
   the sourced claim. Check the equivalent text printed by the command as well.
4. **Place it beside the explanation.** Paste the printed Markdown image on its
   own line under the selected heading. Use the accompanying relationship text
   and source links to write a natural caption, or integrate them into the
   paragraph if it already explains the figure. For the example, a caption could
   read “The principal identifies who gets access, the role defines the permissions,
   and the scope identifies the resources they apply to.” Keep the full-size link
   so phone readers can open and zoom the SVG. Check that the topic still makes
   sense with images turned off.
5. **Check and maintain.** Run the second command, then the normal
   [contributor checks](../CONTRIBUTING.md#local-validation). Commit the JSON,
   SVG, and guide edit together. Site preparation checks the diagrams embedded
   in each guide and copies those SVGs to the published guide path. When a
   source or explanation changes, revisit the arrows and caption and rerun both
   commands. Record the source and actual review in the change description.
   The automated check verifies the guide heading, objective text, source IDs,
   and rendered SVG. Reviewers check what the arrows teach.

Try both commands on the included AZ-900 example, then substitute your JSON path
to repeat the process. Building a diagram gives you a local preview. Adding its
image line to a guide makes it appear in that guide on GitHub and on the site.

```powershell
python scripts/build_guide_diagram.py guides/diagrams/az-900/role-scope.json
python scripts/build_guide_diagram.py guides/diagrams/az-900/role-scope.json --check
```

For a reusable authoring request, fill in the three brackets below.

> In [exam code], help the learner answer [question] under [guide heading].
> Follow the inline guide diagram workflow. Check each relationship against the
> registered sources, show the SVG preview and caption, and explain how to rebuild it.

## Study production

Run commands from the repository root with Python 3.13 (the CI-tested version). The builders use
the standard library and do not need a model subscription or API key. Choose a new
output directory for each run; existing outputs are preserved.

```powershell
python scripts/build_study_pack.py prepare --exam-code AZ-900 --output-dir .learning-output/az900-authoring
```

Give the resulting writing task and complete input packet to your preferred research
agent, or use them yourself. The process is deliberately independent of the agent
runtime. Follow these steps:

1. Read the entire guide and accepted objectives. Identify weak explanations,
   missing examples, and distinctions that would benefit from visual treatment.
2. Recheck the relevant official evidence. Use the existing [source freshness
   process](SOURCE-FRESHNESS.md) and [maintenance queue](AUTOMATION.md). A stored
   catalog date is historical evidence, not a new live check.
3. Write substantive guide changes where needed, following the [guide quality
   standard](GUIDE-QUALITY-STANDARD.md). For a new registered certification, the
   prepare command creates an intake task; establish public objectives and source
   records before publishing a new guide. Do not invent a blueprint for a gated exam.
4. Author a focused content JSON file under `data/study-content/`, using the AZ-900
   example as the format. Each unit identifies exact guide headings, accepted
   objectives, and registered source IDs. Include an explanation, key distinctions,
   an original scenario and answer, a diagram, and a two-host spoken explanation.
5. Build the companion, inspect it, and have a fresh-context reviewer check the
   exact source and output versions. Fix material findings before audio production.

```powershell
python scripts/build_study_pack.py build --content data/study-content/az-900-governance.json --output-dir .learning-output/az900-study
python scripts/build_study_pack.py check --package .learning-output/az900-study
```

For the second pilot, substitute `DP-900` in the prepare command and use
`data/study-content/dp-900-data-decisions.json` as the content input. Select a new
output folder such as `.learning-output/dp900-study`. Podcast preparation can use
that package with no duration target, or a soft target when parts would help.

The package contains a readable study companion, recall cards, diagrams with text
alternatives, the authored units, and a manifest. Hashes bind the outputs to the
guide, objectives, content input, and supporting records. A subsequent change makes
the package stale; review the change and rebuild into a new directory. Never renew
a review date merely to make a hash check pass.

For question-led infographics, use the [visual-study brief template](templates/VISUAL-STUDY-BRIEF.md)
to identify one learner decision, the evidence needed to make it, and an original
recall task. Produce a study version with the explanation and a practice version
that preserves the problem inputs while withholding the answer, including in its
text alternative. The [DP-900 data-freshness exercise](../examples/visual-exercises/dp-900-data-freshness/README.md)
is the first example. Its editable SVG timeline has a custom renderer; it does not
replace the standard study-pack diagrams or automatically author other formats.
For diagrams that name Azure services, select original icons from the
[visual asset catalog](VISUAL-ASSETS.md). The accepted bundle is maintained through
the separate visual-library repository and checked locally without network access.
The [paired diagram gallery](../examples/visual-exercises/README.md) adds a scope
map for AZ-900 and a management-boundary comparison for DP-900. Both embed the
selected original SVG bytes and bind their outputs to exact source-unit versions.
Their practice descriptions preserve givens without the worked answers. The
gallery also identifies the next useful formats; additional images of the same
topic are not counted as new objective coverage.

For each paired exercise, use one author and a separate fresh-context reviewer.
Give the reviewer the practice sheet first and record its answer before supplying
the study sheet, full guide, sources, and brief. Review technical accuracy and
visual/teaching quality separately, repair substantive findings, and recheck the
corrected artifact. Record the actual model and reasoning effort when observable,
the reviewed versions, findings, and what remains untested. The
[visual-study brief](templates/VISUAL-STUDY-BRIEF.md#4-review-record-and-rebuild)
defines the handoff. An AI practice attempt is distinct from actual learner
feedback; a person can later try a new variant and explain their reasoning.

This first implementation conservatively fingerprints entire catalogs and health
records, so even a catalog change for another exam invalidates an old package.
That may require rebuilding more often than strictly necessary. A successful
rebuild confirms structural consistency; it does not substitute for content review.

The builder validates references and structure. It does not invent explanations or
silently rewrite the main guide. The writing step is real editorial work, whether
performed by a person or an agent. Existing objective, discovery, and source-health
monitoring continues to supply the update queue. No additional unattended model
editor or new scheduled publishing job is enabled by this change.

## Podcast production

Use two hosts: one explains; the other asks useful questions, challenges a common
misconception, or works through the scenario. Describe diagrams aloud. Expand
acronyms when introduced, and keep references in the show notes rather than reading
URLs. Preserve uncertainty and scope limits in the spoken material.

Episode length follows the content. A target length is a planning hint, not a
minimum, maximum, or reason to pad or truncate an explanation. Split long guides
into coherent parts at unit boundaries. A single long topic can exceed the target;
split its authoring units if it needs an editorial break. Estimated spoken duration
is not a measured audio runtime.

```powershell
python scripts/build_study_podcast.py prepare --package .learning-output/az900-study --output-dir .learning-output/az900-podcast --target-minutes 15
```

Inspect the generated transcript and script. Follow the podcast command's review and
render steps to bind the review to the exact script before requesting audio.
Audio generation is a separate invocation; preparing study material or a transcript
never calls a speech service. Source or script changes invalidate the relevant
production checks. Keep the script, source version, voice configuration, and audio
receipt together so corrections can identify the affected episode.

```powershell
python scripts/build_study_podcast.py plan --episode-dir .learning-output/az900-podcast/part-01
python scripts/build_study_podcast.py review --episode-dir .learning-output/az900-podcast/part-01 --reviewer "Your name or agent identity" --kind human --notes "Describe the source and script checks actually completed"
python scripts/build_study_podcast.py render --episode-dir .learning-output/az900-podcast/part-01 --max-new-requests 10
```

Use `--kind ai` for agent review; only a person who performed the review should use
`--kind human`. The final command requires `ELEVENLABS_API_KEY`,
`ELEVENLABS_HOST_VOICE_ID`, and `ELEVENLABS_LEARNER_VOICE_ID` in the process environment
and can incur service charges. Repeat the plan/review/render steps for each part.

The initial speech adapter uses ElevenLabs Text to Dialogue. See the
[service comparison and setup](../adapters/podcast-services.md) for account,
voice, API, request-size, and cost considerations. The service renderer requires
an account and two configured voices. The six MP3s in the podcast library were
produced separately using local Supertonic 3 inference and its stock voices. Each
episode folder includes a recording record that binds the MP3 to its script and
transcript. [Narration provenance](../THIRD-PARTY-NOTICES.md#synthetic-narration-for-the-study-podcasts)

After rendering, listen to every part. Check pronunciation, speaker continuity,
omissions, truncation, spoken uncertainty, and scenario answers. Record that
listening pass separately from script review. Hosting, RSS distribution, artwork,
music, and automatic publication are follow-on work, not consequences of rendering.

## Running in GitHub Actions

The **Prepare study materials** workflow prepares an authoring packet and can build
an existing authored content file. The separate **Prepare study podcast** workflow
builds a current study package and prepares its two-host script. Both expose artifacts
for inspection and use read-only repository permissions. They do not commit content,
change review records, publish audio, or spend speech-service credits.

The repository validation gate exercises the new builders and their stale-input,
reference, script-review, and audio-failure boundaries. See the [production backlog](STUDY-PRODUCTION-BACKLOG.md)
for subsequent service and publishing work.
