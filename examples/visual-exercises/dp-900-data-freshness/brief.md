# Completed visual brief: DP-900 data freshness

**Status:** Independent AI-assisted draft; human review pending. Selected-objective
exercise based on the [official exam scope](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900),
accepted July 21, 2026 baseline. See [the exercise and exact source links](README.md).

**Learning question:** Why can a report omit a sale after ingestion and transformation
have completed? What evidence should the learner inspect first?

**Source:** [DP-900 guide](../../../guides/DP-900-microsoft-azure-data-fundamentals.md),
sections **Follow the evidence through the pipeline**, **Power BI concepts**,
and **6. Trace a freshness problem**. Reuse unit `analytics-to-insight` from
`examples/study-packs/dp-900-data-decisions`. Map the published objectives
**Describe considerations for data ingestion and processing** and **Describe
features of data models in Power BI**. Refresh latency diagnosis is an original
application of those concepts, not a prediction of a live exam question.

**Technical fact:** An Import model needs refresh to keep imported data current.
Registered source: `microsoft-power-bi-semantic-models`. Ingestion, transformation,
and coordination are separate responsibilities; source: `dp900-3-analytics-unit`.
The supporting model-versus-display caveat uses registered source
`pl300-refresh-data`, [Data refresh in Power BI](https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-data),
under **Power BI refresh types**. It is supporting context, not a new exam objective.

**Invented inputs:** Sale committed 10:00; ingestion done 10:03; transformation done
10:05; report checked 10:10; successful model refresh including the sale done 10:15.
The successful refresh's inclusion of this row is an explicit scenario assumption.
No duration is an actual service measurement or guarantee.

**Misconception:** A successful upstream job means that the report must already be
current, so the visual itself must be broken.

**Visual choice:** Five timestamped event cards connected in sequence. The 10:10
observation has a question mark and contrasting label as well as a different color.
Spacing is explicitly labeled as not measuring elapsed time. Titles and body text
remain editable text; no vendor logo or external font is required.

**Study version:** Present the inputs, identify the unfinished refresh, calculate
15 minutes from sale to updated model and 10 minutes after transformation, and
explain the first diagnostic check.

**Practice version:** Keep all evidence needed to solve the problem. Replace the
three explanations with prompts and space for notes. Its SVG description contains
the given scenario and questions, without the study version's answers. The
README provides an equivalent text exercise before the answer section.

**Boundary:** Model data availability is separate from an already-open report
display updating. This is an illustrative Import workflow, not a universal Power BI
architecture or a claim about all access modes. **VERIFY CURRENT:** actual access
mode and refresh settings.

**Success criteria:** The learner locates the unfinished step using timestamps,
calculates both intervals, chooses a relevant first check, and explains why chart
design alone cannot update the imported data. No score is a claim of exam readiness.

**Reuse:** The same scenario already appears in the DP-900 podcast script. Other
visual forms should be chosen from their teaching task: comparisons for management
boundaries, matching cards for access patterns, and maps for concept relationships.

**Exact inputs:** SHA-256 of UTF-8 text with CRLF/CR normalized to LF, except the
accepted objective snapshot which is a raw-byte hash.

```text
Canonical guide:
1c618b776923450c7bbf59aac51ce2bf3b64cfb5dcc214e6b4b388a718332991
Accepted objective snapshot:
7cef780d1a9e8e88b587fba89acb994985c4aedbd491710e814686ce5dc6559f
Source study-package manifest:
2473aca4a6044d59c7b2b31c13a117aee35216198c6781f174ca117c469b1db1
Selected unit, serialized with study_material.json_text:
68289c5b5f879ea8f6c2db3d0cd21172f6853e053bd5d7905b51a1e60e9ae845
```

The generated manifest binds the renderer, current package, selected unit, and
both SVG outputs. [Review evidence](review.md) is separate from generation.
