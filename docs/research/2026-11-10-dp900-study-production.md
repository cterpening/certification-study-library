# DP-900 second study and podcast pilot — November 10, 2026

The second pilot adds a [visual study companion](../../examples/study-packs/dp-900-data-decisions/study-guide.md),
four original recall cards, four accessible SVG diagrams, a
[two-host transcript](../../examples/podcasts/dp-900-data-decisions/part-01/transcript.md),
and an [offline GenFM upload](../../examples/genfm/dp-900-data-decisions/source.txt).
The [signup and trial instructions](../GENFM-PILOT.md) also link the AZ-900 upload.

## Selected scope and evidence

The companion maps 15 selected objectives across four units: five core data
concepts, three relational objectives, three non-relational objectives, and four
analytics objectives. It is not complete DP-900 coverage. The published blueprint
still identifies the July 21, 2026 skills baseline. The complete unchanged guide
was read by the researcher and separately by the fresh-context content reviewer.

Exact official evidence opened during this bounded research and review:

| Source | Applied distinction |
|---|---|
| [DP-900 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900) | Baseline and exact selected objectives |
| [Core data concepts](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/) | Data representation and workload are separate decisions |
| [Data formats](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats) | Structured, semi-structured and unstructured representations |
| [Transactional processing](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing) | Operational transactions |
| [Analytical processing](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing) | Historical aggregation and analysis |
| [Relational data](https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data) | Tables, keys and relationships |
| [Normalization](https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization) | Redundancy and update anomalies |
| [Azure SQL options](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview) | Database, instance and VM management boundaries; OS access |
| [Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction) | Object access; supported NFS/SFTP capabilities prevent an HTTP-only generalization |
| [Azure Files](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-introduction) | Managed file shares and supported protocols |
| [Cosmos DB resource model](https://learn.microsoft.com/en-us/azure/cosmos-db/resource-model) | Containers and items |
| [Cosmos DB partitioning](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview) | Access patterns and uneven request distribution |
| [Ingestion pipelines](https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines) | Orchestration, ingestion and transformation |
| [Batch and stream processing](https://learn.microsoft.com/en-us/training/modules/explore-fundamentals-stream-processing/2-batch-stream) | Bounded batches and continuing event processing |
| [Power BI semantic models](https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-understand) | Model modes and Import refresh |
| [Star schema guidance](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema) | Facts, dimensions and modeling |
| [Select report visuals](https://learn.microsoft.com/en-us/training/modules/power-bi-effective-reports/5-report-visuals) | Reviewer followed the registered training hub to this lesson; line, bar and table choices |

The bookshop scenarios, SQL management decision, and example freshness timeline
are original teaching examples. Their timestamps are hypothetical, not measured
service latency or a service-level agreement. No assessment questions were used.
Source-health records remain historical reachability evidence. This scoped work
does not advance the canonical guide's full-review date or change the source
catalog, objective baseline, source-health records, or whole-guide review ledgers.

## Production and review

The prepared podcast contains 1,667 spoken words in one part: approximately
11.5 minutes at 145 words per minute. No duration target was supplied. The existing
renderer plans 10 requests containing 10,954 spoken characters. These are input
estimates, not actual runtime, measured cost, or generated audio.

A separate fresh-context reviewer checked the full guide as context, all selected
objectives, source evidence, original questions and answers, diagrams, text
alternatives, and spoken explanations. Its scoped rubric-2 verdict is
**pass-with-notes**, with no medium, high or critical findings. All 32 authored
unit turns agree with the script and transcript; four diagram descriptions agree
with their nodes and relationships. The coordinator also viewed a rendered image
of all four diagrams; labels and relationships were readable without clipping.

One **low citation-precision finding remains open**: the analytics unit registers
the broad Power BI training hub for visual selection. The reviewer navigated to
and read the exact supporting lesson linked in the table above. The advice is
correct, but the package citation should eventually use a dedicated lesson record.
That source-catalog refinement is tracked in the production backlog. The script
review receipt records this note and binds the actual reviewed script and package.

Both pilots now have deterministic GenFM source exports. The exporter reads a
validated study package, includes its teaching content, diagram descriptions,
original scenarios, caveats and citations, and excludes prepared dialogue. Its
instructions request two hosts and content-dependent length, with natural parts
when useful. Checking an export revalidates the upstream package and rederives
the exact text, so replacing an artifact hash does not excuse unsupported edits.

The GenFM export is an offline handoff, not an execution of GenFM. Generated-script
review, actual audio, pronunciation, speaker continuity, credit usage, listening
review and human content review remain pending. No ElevenLabs account, purchase,
API request, Azure resource, Fabric item or Power BI report was created.

A separate fresh-context implementation review found no material issues in the
exporter, its path restrictions, provenance checks or documented commands. The
245-test suite passed with two existing Windows symlink-privilege skips. The
offline smoke runner rebuilt both study packages, prepared both podcasts, planned
their requests, and built and checked both GenFM handoffs successfully.

## Reviewed input and artifact hashes

Text hashes normalize CRLF/CR to LF; the accepted objective snapshot hash is raw.

```text
DP-900 canonical guide:
1c618b776923450c7bbf59aac51ce2bf3b64cfb5dcc214e6b4b388a718332991
DP-900 accepted objective snapshot:
7cef780d1a9e8e88b587fba89acb994985c4aedbd491710e814686ce5dc6559f
Authored data/study-content/dp-900-data-decisions.json:
5863d90e06fec6fde17b1d00e61d4d5d78404be2f6651eda784202f71c4f306a
Study package manifest.json:
2473aca4a6044d59c7b2b31c13a117aee35216198c6781f174ca117c469b1db1
Study companion study-guide.md:
3e882c1720913e2452fd7f50444ded9d8e2f1b141d501fb685dfe4ecb9a992aa
Podcast part-01/script.json:
6de74c826eb667126c7e4707265c68656ddd92583de35e010a4dbd7bcbbcdcc6
Podcast part-01/transcript.md:
cc0ed9c8fd1947b5a3abfcacddbf8e467e6e608095ced5ad4e737b7fc931aa97
```

The package and GenFM manifests record their complete artifact bindings. Matching
hashes establish which files were checked; they do not establish factual accuracy.
