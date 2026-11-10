# Podcast service selection

Research checked **November 10, 2026**. **VERIFY CURRENT:** API models, limits,
availability, prices and usage rights can change. This is an implementation
comparison, not a listening-quality benchmark. No paid audio was generated.

The first adapter uses **ElevenLabs Text to Dialogue**. It accepts the exact
reviewed script with a separate voice ID for each speaker. This makes a technical
study conversation easier to trace back to its sources than a service that writes
a new conversation while generating audio. Voice quality still needs a listening
trial using the same sample on the shortlisted services.

| Service | Fit for this library | Current integration decision |
|---|---|---|
| [ElevenLabs Text to Dialogue](https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert) | Ordered text/voice pairs; script and speaker choices remain in the repository. | Implemented optional renderer. The API documents `eleven_v3` as its default. Requests use at most 2,000 spoken characters, following current reliability guidance. |
| [Google Cloud Gemini TTS](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts) | Multi-speaker synthesis and delivery prompts; another route for rendering a controlled script. | Strong next adapter for an A/B listening trial. Recheck the exact model, endpoint, region and quota before implementation. |
| [Gemini Notebook Enterprise audio overviews](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-audio-overview) | Produces a conversation from selected notebook sources and an episode-focus prompt. | Useful editorial alternative; the notebook API is Preview and allows one audio overview per notebook. It does not promise to preserve our reviewed script verbatim. Review its newly generated claims before publication. |
| [Google standalone Podcast API](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api) | Previously a direct source-to-podcast API. | Excluded for a new integration: the current page explicitly says it is deprecated and Google is not allowlisting new customers. Do not confuse it with notebook audio overviews. |

Google's [notebook API setup](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks)
requires an active Gemini Notebook Enterprise license assigned to an authenticated
user and the Cloud NotebookLM User role. A consumer NotebookLM subscription should
not be treated as proof of access to that enterprise API.

## Production contract

`scripts/build_study_podcast.py prepare` is offline and has no service dependency.
It reads a validated study package, keeps both speakers, and writes a transcript,
source references, episode script and version bindings. By default all selected
units form one episode. `--target-minutes` is an editorial hint, not a duration
cap: parts break only between units, and an oversized topic stays intact with a
warning. Estimates use 145 words per minute; actual speech, pauses and delivery
determine the final duration. Split an unwieldy unit in the authored content when
it contains multiple teaching ideas.

The script review receipt records who actually reviewed it and whether that was
AI or human review. It binds to the script and study package hashes. It does not
promote the source guide, establish community review, or claim anyone listened to
audio. Edit the source learning units and rebuild when wording changes.

Only the explicit `render` command sends text to ElevenLabs. It reads
`ELEVENLABS_API_KEY`, `ELEVENLABS_HOST_VOICE_ID`, and
`ELEVENLABS_LEARNER_VOICE_ID` from the process environment; no credentials are
stored in the repository or generated metadata. Choose two distinct voices you
are entitled to use. The CLI has no endpoint override and refuses HTTP redirects.

The renderer requests `wav_24000`, validates each PCM response and joins the
chunks into one `audio/episode.wav` with `audio/chapters.json` and a production
receipt. ElevenLabs documents WAV support on the dialogue endpoint in its
[February 2, 2026 changelog](https://elevenlabs.io/docs/changelog/2026/2/2).
Topic boundaries determine chapters; shorter service requests are just transport
chunks. Sentence/word splitting preserves long turns rather than truncating them.
No music, cloned voice, publishing feed, or account enrollment is required by the
adapter.

Each cache entry binds the request parameters to its audio hash. A retry reuses
verified completed chunks; stale scripts and corrupt cache entries fail visibly.
`--max-new-requests` limits new calls in a run (default 20). Failed requests are
not automatically retried because a timeout can happen after a service has begun
billable work. A partial render retains successful chunks and records its state.
Listen to the completed result for pronunciation, dropped words, speaker swaps,
audible seams and technical meaning before publishing it. A valid WAV file is
not proof that its spoken content matches the script.

## Cost and rights trial

Use `plan` to count characters and requests before rendering. Check
[ElevenLabs API pricing](https://elevenlabs.io/pricing/api) against that estimate;
this repository does not assume a free allowance or subscribe to a plan.
ElevenLabs' [dialogue overview](https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue)
distinguishes paid-plan commercial rights from ownership of generated outputs
and says dashboard regenerations have separate rules. Do not assume an API retry
is free. Check the chosen account's terms and voice availability when doing the
trial.

For the first service comparison, render the same one-topic script with two
stable voice choices, then compare technical pronunciation, conversational flow,
speaker consistency, content fidelity, completion time and measured cost. Expand
to longer multi-part material only after the short sample is satisfactory.
