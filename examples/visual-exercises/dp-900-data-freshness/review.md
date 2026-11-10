# DP-900 visual exercise review — November 10, 2026

This record covers the [study/practice exercise](README.md) and its [visual brief](brief.md).
It does not renew the canonical guide's whole-guide review or change the accepted
objective baseline. Human review and live Power BI execution remain pending.

The coordinator read the source unit, current package binding, and relevant guide
context. The registered [semantic-model documentation](https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-understand)
was opened and read for the Import-refresh claim; the registered
[ingestion lesson](https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)
was opened and read for pipeline responsibilities. Only text was reviewed; no video
or assessment was consumed. Timing and refresh inclusion are explicitly invented
scenario assumptions. The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)
defines scope; exact source/objective bindings are recorded in the brief.

The registered [data-refresh documentation](https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-data),
source ID `pl300-refresh-data`, was independently read by the reviewer and then the
coordinator. Its **Power BI refresh types** section directly supports the caveat
that updating the model is separate from refreshing an open report's visuals.
The source already exists in the catalog; no catalog or whole-guide review change
was needed to cite this supporting distinction in the exercise.

A separate fresh-context AI reviewer read the complete unchanged DP-900 guide for
context and checked the two selected objectives, source unit, exact bindings,
source evidence, both SVGs and descriptions, renderer, and brief. Its scoped checks
found no material correctness, answer-leakage or source-binding issue. The practice
description contains the given evidence and questions without the worked answer.
An in-memory changed-unit hash was rejected. This is a bounded exercise review,
not a whole-guide audit or human validation.

The coordinator rendered both SVGs in a headless browser and inspected the images;
labels, timing, reading order, answer panels, and writing space were readable and
unclipped. The study title was refined to **The refresh is incomplete** to avoid
implying whether a refresh was queued or running. Its final rendering was checked.
The reviewer also viewed the supplied renders. The small connecting line's arrowhead
is covered by the last event marker; left-to-right timestamps and numbering still
establish sequence. Spacing is explicitly not a scaled time axis.

The 245-test suite passed with two Windows symlink-privilege skips. The offline
study/podcast/GenFM smoke run passed and now checks this exercise's generated SVGs
and source binding. No new test suite was added for this fixed visual layout.

Reviewed SVG SHA-256 values (UTF-8 text, CRLF/CR normalized to LF):

```text
study.svg:
b00f2b208fbaaba5209ff9d29911d0781903fb8f1562491fec955bd4c520d273
practice.svg:
dbdc1ff5281a4bece3c3ade8580a646f0a18d4649d9f9a599905556081c2ae6f
```

The generated manifest records renderer, source-unit and package fingerprints.
Matching hashes establish the checked versions, not factual accuracy or learning
outcomes. Human review, actual learner feedback, and live product use remain open.
