# NCA-AIIO deep review — September 29, 2026

The [study guide](../../guides/NCA-AIIO-nvidia-ai-infrastructure-operations-associate.md) now answers all 40 readiness prompts and includes a locally executed telemetry/capacity workbook. All 22 public objectives remain covered. This is a same-context AI review; independent human review and hardware practice are pending.

## Scope and evidence

The [canonical exam page](https://www.nvidia.com/en-us/learn/certification/ai-infrastructure-operations-associate/) and its [six-page study guide](https://dam-cdn.nvd.orangelogic.com/AssetLink/x874j05hy3m3r2sor84kpvp70750m468.pdf) agree on eight knowledge, ten infrastructure and four operations objectives, weighted 38%, 40% and 22%. The complete PDF text was read and its printed page 2 was visually checked. Both monitored snapshots are unchanged; neither was rewritten. Recommended education/experience and optional training remain distinct from admission requirements.

Eighteen distinct public sources were fetched: seventeen returned successful HTTP responses and one commercial page returned 403. Reading boundaries and content limitations are recorded per source in the operational evidence. A successful HTTP response does not establish that a course body is available.

## Teaching changes

The guide now explains field-specific units and entity scope, stale or unsupported observations, Xid codes versus sampled records, time-slicing limitations, and shared memory within a MIG GPU instance. The operational discussion uses selected release notes to show why exact versions and installation routes matter. An original checkpoint example calculates a 4 GiB/s payload requirement before overhead and requires a restore criterion.

The added standard-library Python workbook executed 34 checks. It parses synthetic JSON, normalizes percentage/ratio and MiB/byte fields, rejects selected invalid records and prevents duplicate counting of physical/GI memory. Eight logical replicas retain one 65,536 MiB physical capacity; three CI records describe two GIs totaling 30,720 MiB. These are teaching fixtures, not supported GPU profile specifications or measured performance.

The workbook has no external calls or file writes. It trusts supplied identity/status and a complete fixture shape. It does not implement a DCGM binding, Prometheus parser, complete production validation, actual discovery, typed DCGM sentinel decoding, tenant isolation or scheduling. Eight infrastructure activities and three original scenarios remain proposed.

## Catalog findings

The canonical and DGX learning-path pages still list a seven-hour Fundamentals course. Its direct public page does not expose populated course details, and the PDF-linked Academy route redirects to generic training. The learning-path card lists USD 50 for the course and USD 135 for the exam; the canonical exam page lists USD 125. Checkout was not accessed. The blocked third-party page does not substantiate the earlier June 2026/about 7h or popularity claims.

The final learning table uses Resource, Access and Estimated time, with author estimates distinguished from vendor runtime. No subscriptions, private lessons, course accounts or exam questions were accessed. The January 2023 storage article supplies historical planning context rather than a current performance promise.

## Validation and remaining boundaries

The operational receipt at `ADLC_Docs/operations/2026-09-29-nca-aiio-deep-review.json` retains fetch hashes, prior records, all 22 objective mappings, workbook hash/output, findings and final repository/site gate results. No GPU, driver, cluster, cloud or facility was changed. No installation or reboot was performed. Human review, paid course verification, individual checkout and hardware exercises remain pending.

The five reserved GitHub guides and disabled notification pilot remain unchanged.
