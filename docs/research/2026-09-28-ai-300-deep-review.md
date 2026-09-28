# AI-300 deep review — September 28, 2026

The [AI-300 guide](../../guides/AI-300-operationalizing-machine-learning-generative-ai-solutions.md)
was read in full and mapped to **58 detailed objectives in 14 groups**. It now
contains six worked examples, ten labs and explanations for 48 original checks.
Twenty-seven offline assertions cover feature timing, shadow load, delayed labels,
PTU/cache arithmetic, evaluation failures, rank fusion and catalog totals. One
local Python gate was executed and one YAML workflow fragment parsed.

This is same-context AI research and repair; independent human review is pending.
No cloud, SDK, model, ML job, deployment, traffic shift, network, telemetry query,
fine-tuning, purchase or paid-course content was exercised. Synthetic results do
not establish deployed controls, representative quality or available capacity.

## Exam and catalog evidence

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-300)
retains its March 5 page date, no separate skills-effective date and no announced
change. All 58 objectives and accepted objective/status hashes are unchanged.
The [credential](https://learn.microsoft.com/en-us/credentials/certifications/operationalizing-machine-learning-and-generative-ai-solutions/)
lists an active **120-minute English** exam. Its AI Skills Navigator assessment
requires sign-in; only a shell was retrieved, with no questions or results read.
The [course](https://learn.microsoft.com/en-us/training/courses/ai-300t00) lists
four days and 12 course languages. Its current syllabus remained a loading shell;
the old two-path/12h24 total was not reproduced and is no longer presented as
current. Self-study and lab budgets are editorial estimates.

The [O'Reilly bootcamp](https://www.oreilly.com/live-events/mlopsllmops-bootcamp/0642572182861/0642572243333/)
names Ammar Mohanna and two sessions. Embedded metadata places the linked event
on **November 3–5, 2025**, with `PT10H`; the two public agendas total **300 + 300 =
600 minutes**. This is a historical, broad MLOps/LLMOps event. A current recording
or replacement event was not verified.

Direct Udemy retrieval was blocked. Indexed public outlines show
[Aseem Mankotia's preparation course](https://www.udemy.com/course/ai-300-mlops-genaiops-engineer-exam-preparation/)
updated July 2026, one section, 11 lectures and 3h27. Its advertised 100-minute
simulation differs from Microsoft's 120-minute assessment.
[VARONTO Academy's practice listing](https://www.udemy.com/course/ai-300-operationalizing-ml-and-generative-ai-practice-tests/)
is dated June 2026 and lists five 150-question sets plus one 161-question set:
911 total. Its prose still says 900. Neither paid questions nor claimed exam
realism/originality were evaluated.

A [Whizlabs AI-300 product](https://www.whizlabs.com/ai-300-microsoft-machine-learning-operations-engineer-associate/)
now exists, correcting the previous missing-product note. Direct retrieval
exposed a title shell; its indexed catalog advertises 100 videos and three quizzes
(one free, two paid). Duration and question count remain unverified. Its exam
language claim differs from Microsoft's English-only listing. Bounded searches
did not identify dedicated Pluralsight/MeasureUp products; this is not proof of
absence. Broad sample repositories and Reactor remain discovery/context sources.

## Technical corrections and learning value

- **MLOps:** distinguish already-ended v1 toolchain support from continuing
  service operation. Explain submission versus completed/evaluated jobs, exact
  reuse inputs and forced-rerun behavior, point-in-time feature lineage, and the
  narrower support of the Responsible AI dashboard.
- **Rollout and monitoring:** distinguish shadow copies from routed canaries;
  account for duplicated execution and effects. Require inference collection,
  disjoint monitoring windows, mature-label coverage and subgroup evidence.
- **GenAIOps infrastructure:** scope managed VNet to outbound agent traffic and
  document irreversible transitions/provisioning prerequisites. Separate PTU
  quota, capacity and billing reservations; use fictional model parameters to
  calculate demand and cache-loss headroom. Scope spillover by matching
  model/version/resource and preserve response attribution.
- **Evaluation:** describe current project SDK and scenario contracts, stored
  interaction evaluation without replay, eligible GenAI spans and missing-content
  failures. Keep privacy, sample selection, evaluator coverage and pass rate as
  separate decisions. The local gate rejects missing, duplicate, failed and severe
  records; malformed input must block through caller error handling.
- **Retrieval and customization:** explain RRF versus vector/reranker scores,
  method-specific tuning signals/access and separate training/deployment
  retirement. Preserve an actually available compatible rollback target.

Primary references sit beside the applied claims in the guide. Source-specific
notes identify the sections read. Long model tables, code samples, complete
release archives and retained broad references were not exhaustively audited.

## Blog intake

Selected policy/control and observability sections of
[Sarah Bird's June 2 article](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/)
support an original authorization/control worksheet. Linked ASSERT/ACS
implementations and partner results were not executed or reproduced. A control
path using a probabilistic judge does not guarantee correct classification.

Selected operations summaries in
[Nick Brady's May 30 roundup](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-may-2026/)
support a feature/API/status/permission/data-boundary worksheet. Current product
documentation governs exact support and preview scope; the complete roundup,
linked SDK samples and model catalog were not audited.

## Maintenance and validation

The weekly/manual workflow already detects source/objective changes and dated
follow-ups; it queues semantic review rather than claiming to perform it. Two
October 12 follow-ups cover evaluation/network/model support and learning-catalog
evidence. The guide's learning tables are synchronized into the shared catalog.
Historical review dates, hashes and outcomes are retained, and accepted snapshots
are unchanged.

The operation receipt is
`ADLC_Docs/operations/2026-09-28-ai-300-deep-review.json`. It records objective
mapping, source retrieval and indexed observations, findings, offline checks and
the actual repository/site validation result. Reachable links alone do not
establish that lessons, videos or full references were reviewed.
