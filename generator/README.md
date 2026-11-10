# Guide generation

The [study production process](../docs/STUDY-PRODUCTION.md) now provides runnable
authoring packets and study-pack builds through `scripts/build_study_pack.py`.
`scripts/build_study_podcast.py` separately prepares two-host episodes from a
versioned package. Both use authored, source-linked content; neither silently
promotes a draft or treats structural validation as factual review.

The initial guides are curated Markdown brought forward from the prototype. Future generation should consume registered exams, reviewed objective snapshots, registered sources, and `templates/guide.md`.

Generation creates an **AI-GENERATED DRAFT**. It must not promote content to **SOURCE-VALIDATED** or silently publish a changed interpretation when an upstream blueprint changes.
