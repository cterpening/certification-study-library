# Repeatable study guides, visual aids, and podcasts

The library has two separate production processes. Study production reads an exam's
existing guide, accepted objectives, and source records to prepare a bounded writing
task. An author or research agent expands the material, and the builder turns that
authored content into a study companion, recall cards, and editable SVG diagrams.
Podcast production consumes a particular study package and creates a two-host
script, transcript, and parts that can be rendered through a speech service.

The first example teaches three AZ-900 governance distinctions: role-based access
control versus Policy, resource locks versus data protection, and tags versus access
and cost allocation. It is selected-objective practice, not a replacement for the
complete [AZ-900 guide](../guides/AZ-900-microsoft-azure-fundamentals.md).

Read the [example visual companion](../examples/study-packs/az-900-governance/study-guide.md)
and [two-host transcript](../examples/podcasts/az-900-governance/part-01/transcript.md).
The transcript is approximately nine minutes at the planning rate; no audio runtime
has been measured. These are dated, reproducible examples. Rebuild from reviewed
inputs when their source binding becomes stale.

The second pilot is [DP-900 data decisions](../examples/study-packs/dp-900-data-decisions/study-guide.md),
with four visual chapters and a [two-host transcript](../examples/podcasts/dp-900-data-decisions/part-01/transcript.md)
estimated at 11.5 minutes. It samples all four domains through selected objectives,
without claiming complete exam coverage. Use the [ElevenLabs/GenFM pilot guide](GENFM-PILOT.md)
for signup and ready-to-upload source files for either pilot.

Both processes retain **AI-generated draft; human review pending** status. Reading
files, matching hashes, rendering diagrams, and synthesizing speech do not establish
technical correctness. The official exam blueprint remains authoritative.

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
voice, API, request-size, and cost considerations. No key is committed. Until a
service account and voices are configured, the transcript is the deliverable;
it is not represented as a completed podcast recording.

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
