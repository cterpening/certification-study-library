# ElevenLabs signup and the first podcast trials

The second study/podcast pilot is **DP-900 Azure Data Fundamentals**. Its four
chapters cover workload decisions, relational management boundaries, non-relational
access patterns, and analytics-to-insight reasoning. AZ-900 governance remains the
first pilot. Both cover selected objectives and retain human-review-pending status.

## Account and plan

Create an account at [ElevenLabs](https://elevenlabs.io/). The
[GenFM plan requirement](https://elevenlabs.io/docs/help-center/product/studio/studio/on-what-plans-can-i-use-studio)
says that creating a podcast with GenFM requires a paid subscription.
**VERIFY CURRENT — November 10, 2026:** the [monthly pricing page](https://elevenlabs.io/pricing)
lists Starter at **US$6/month before tax**, with 30,000 monthly credits. Starter is
a reasonable first trial tier; verify the checkout amount and available credits.
No subscription or charge has been created by this repository.

The web trial needs an account, not an API key. The separate repository audio
renderer uses an API key and two voice IDs when automation is wanted. Keep those
credentials in the local environment or a secrets store, outside repository files.

## Ready-to-upload study material

| Trial | Source file | Focus instructions | Study companion | Prepared two-host script |
|---|---|---|---|---|
| 1: AZ-900 governance | [source.txt](../examples/genfm/az-900-governance/source.txt) | [instructions.txt](../examples/genfm/az-900-governance/instructions.txt) | [Visual companion](../examples/study-packs/az-900-governance/study-guide.md) | [Transcript](../examples/podcasts/az-900-governance/part-01/transcript.md) |
| 2: DP-900 data decisions | [source.txt](../examples/genfm/dp-900-data-decisions/source.txt) | [instructions.txt](../examples/genfm/dp-900-data-decisions/instructions.txt) | [Visual companion](../examples/study-packs/dp-900-data-decisions/study-guide.md) | [Transcript](../examples/podcasts/dp-900-data-decisions/part-01/transcript.md) |

Download the source file for the trial. It contains the teaching material, original
checks and answers, diagram explanations, exact scope, and public source references.
It does not contain the prepared dialogue: GenFM will write its own conversation.
The existing transcript provides a comparison version based on the same material.

In Studio, choose **Audio → Workflows → Generate a podcast**, then upload the TXT
file. Select a conversation with two voices, choose a length preference, and paste
the focus instructions. The current [GenFM instructions](https://elevenlabs.io/docs/help-center/product/distribution-publishing/gen-fm/how-do-i-use-gen-fm)
describe short/default/long preferences rather than an exact duration guarantee.
Let the content determine the useful length; split topics into parts when useful.

Review the generated text before exporting audio. Check every answer and technical
distinction against the source. For DP-900, watch for these mistakes:

- choosing a database solely because the input is JSON;
- equating managed SQL compatibility with guest operating-system access;
- treating Blob Storage, shared files, and document queries as interchangeable;
- treating successful ingestion as proof that an Import-model report is current.

After reviewing the script and service estimate, export the audio and listen for
pronunciation, omitted caveats, changed answers, and speaker consistency. Record
the actual credits used and runtime. The prepared DP-900 script is estimated at
about 11.5 minutes; GenFM may create a different script and duration.

If using our prepared transcript instead, start an appropriate blank/imported audio
project rather than asking GenFM to generate another script. For reproducible local
automation, use the [existing renderer](STUDY-PRODUCTION.md#podcast-production).
The [Studio API](https://elevenlabs.io/docs/api-reference/studio-api-information)
has separate access-on-request requirements; a paid web subscription is not proof
that the Studio API is enabled. The current adapter uses Text to Dialogue.

## Repeat the export

Export a current study package into a new folder, then check its binding:

```powershell
python scripts/export_genfm_source.py build --package examples/study-packs/dp-900-data-decisions --output-dir .learning-output/dp900-genfm
python scripts/export_genfm_source.py check --export .learning-output/dp900-genfm
```

The exporter is offline. A changed study package invalidates an older export.
Rebuild from reviewed content before uploading a new trial. The manifest records
which source package produced the text; it is not evidence that GenFM ran or that
its generated script was reviewed.
