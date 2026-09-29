# NCP-AIO deep review — September 29, 2026

The [guide](../../guides/NCP-AIO-nvidia-ai-operations-professional.md) now answers 48 readiness prompts and includes 25 executed local rendering/accounting checks. All 31 canonical objectives remain mapped. The review found an unresolved conflict in NVIDIA's linked preparation PDF; it is recorded as a source-freshness blocker, while the guide retains the canonical webpage's scope.

## Official scope discrepancy

The [canonical page](https://www.nvidia.com/en-us/learn/certification/ai-operations-professional/) lists 31/23/23/23 weights across 13/5/7/6 detailed topics. Its exam remains 30 questions plus three hands-on exercises within 120 minutes, USD 500, English and pass/fail. Both monitored snapshots are unchanged; no baseline write occurred.

The actual [linked PDF](https://dam-cdn.nvd.orangelogic.com/AssetLink/ub08c12vdc5l53ksln5d4dlpt3346464.pdf) has seven pages and 19 numbered body topics with 28/20/32/20 weights, including Fleet Command and cloud VMI deployment. Its contents visibly adds a 10% Cognition/Planning/Memory entry without a corresponding body section; the listed total is 110%. The complete text was read and PDF pages 2, 3 and 7 were visually checked. Its FEB26 mark is not proof of an announced transition.

The PDF additionally describes 50/50 section scoring and a performance report. These details are not confirmed on the canonical exam page; the general FAQ says pass/fail without a score. The guide discloses these unresolved differences instead of combining the scopes. Vendor clarification is pending; no support message or exam booking was sent.

## Technical work

Selected BCM 11 manual sections clarify category/group membership, Boolean inheritance, role priorities, closed versus drained nodes, and running-node image updates. Selected September 11 release notes add concrete acceptance checks for scheduler hooks, monitoring, drain reporting and runtime ownership. The downloaded administrator manual has 1094 pages; only the recorded sections were reviewed.

Slurm documentation clarifies discovery/GRES limits, pre-partitioned MIG, accounting gaps and script/step/signal results. Kubernetes documentation supports GPU request/limit semantics, namespace quota, transitional rollout capacity and local Kustomize composition. Run:ai's self-hosted v2.26 reference distinguishes hierarchical quota, rank, priority, preemptibility and placement. Container Toolkit guidance separates cosmetic group-name warnings from device-injection or permission failures.

The original public workbook ran with Python 3.13.14, kubectl 1.35.9, Kustomize 5.7.1 and PyYAML 6.0.3. Its 25 checks include actual local rendering, synthetic GPU budget comparisons, percentage rounding, CSV exit interpretation and temporary-file cleanup. It uses an empty kubeconfig and local fixed resources only. No API, cluster, service, image pull, Slurm or GPU was used.

The nonexistent image/digest is a deliberate placeholder. Rendering does not validate server admission or scheduling, and the budget calculation omits topology, other namespace usage and termination delays. Synthetic Slurm rows do not establish real job outcome or artifact correctness. All eight infrastructure activities and three scenarios remain proposed.

## Learning resources

All 24 fetched source URLs returned successful HTTP responses, but content verification has narrower limits. The old professional workshop PDF URL redirects to generic training HTML; its former 20-hour schedule is unverified. The current learning-path card lists a 24-hour/USD 3000 course, while its exam card still shows USD 400/1.5h instead of the canonical USD 500/2h. The Fundamentals endpoint has an empty course shell. No paid interiors, checkout or account were accessed.

The final learning table uses Resource, Access and Estimated time. It distinguishes listed runtime from author estimates and identifies the conflicting PDF. The original teaching avoids recalled exam content and does not imply actual vendor-lab access.

## Validation record

`ADLC_Docs/operations/2026-09-29-ncp-aio-deep-review.json` preserves prior records, hashes, all 31 mappings, source fetches, workbook output and final repository/site gate results. Independent human review, vendor clarification, course metadata/checkout and infrastructure execution remain pending. The five reserved GitHub guides and disabled notification pilot are unchanged.
