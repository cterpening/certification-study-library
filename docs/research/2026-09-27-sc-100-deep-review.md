# SC-100 deep review — September 27, 2026

The complete [guide](../../guides/SC-100-microsoft-cybersecurity-architect.md)
was read and **81 October objectives in 14 groups** were individually mapped.
The accepted July 28 baseline remains separate from the October 21 revision.
The current credential's third prerequisite is Cloud and AI Security Engineer,
replacing the guide's older Azure Security Engineer listing. Course advice is
distinguished from certification requirements. Current exam/credential pages list
ten languages; the instructor-led course remains four days.

## Learning changes

Five examples cover recovery dependencies/RPO, containment latency, three agent
token subjects, changing inventory coverage and version-bound malware decisions.
The guide now includes **ten labs and 44 answered checks**.

New and clarified boundaries include:

- Locked backup immutability, time-limited protection and separate Resource Guard
  permissions are distinct; retention alone does not establish recoverability.
- MCSB v2 remains preview. Its AI article labels itself recommended guidance last
  reviewed in December 2025, not an attestation or proof of current enforcement.
- Sentinel portal migration changes routing, correlation, automation, latency and
  CMK coverage. Batched incident updates do not preserve every intermediate event.
- Agent identity, delegated user and agent user need different Conditional Access
  targets. All-users and blueprint policies leave agent-user coverage gaps.
- Key Vault new-resource RBAC defaults and existing-resource access migration are
  separate from the February 2027 management-API retirement.
- Azure Policy evaluation does not itself remediate existing resources.
- New-subscription Foundational CSPM opt-in, individual recommendations and reduced
  AWS/GCP CIEM detail require explicit onboarding and evidence checks.
- Branch traffic forwarding does not prove user Conditional Access enforcement;
  tenant restrictions and resource-tenant guest governance serve different purposes.
- Copilot DLP actions differ by prompt, source, external email and web search.
- Management locks do not protect every data-plane operation; Shared Key has its
  own authorization and compatibility implications.
- Malware tags are mutable and scan results must match current content. Errors,
  unscanned items and overwrites remain unresolved until validated.

Thirteen offline arithmetic/set checks verified the synthetic numbers and published
module/course sums. No tenant, agent, malware scan, recovery, policy, network,
incident response or destructive cloud action was executed. All ten labs remain
learner exercises, with tabletop alternatives and missing capabilities recorded.

## Resource and blog decisions

Four Learn-path landing pages now show 19 modules. Earlier durations are historical;
individual modules were not completed or timed. Pluralsight's four listed Tim Warner
courses total 4h58, rounded to five path hours. Coursera lists 39 hours across four
course estimates, separate from its five-month pacing suggestion. MeasureUp lists
148 questions last updated November 2025; current objective completeness is unproven.

Both O'Reilly URLs and Udemy blocked retrieval. YouTube returned a shell. Their
earlier metadata is qualified rather than freshly asserted. The lab README and
first Exam Readiness Zone chapter list were read; individual labs, total video
runtime, paid lessons and signed-in assessments were not reviewed. Partner PDF
retrieval did not provide reliable parsed event metadata, so current offerings
remain unverified.

Two public Microsoft articles supply bounded exercises:

- Rob Lefferts, September 23: use the ISOC preview announcement to draw a supervised
  signal-to-action control map. Preview availability and performance were not tested.
- Microsoft Security Research, Yossi Weizman and Tushar Mudi, September 25: use the
  Storm-3168 report for a credential exposure and recovery tabletop. Preserve the
  authors' uncertainty about initial access, exfiltration and ransom evidence.

The blog's general product recommendations do not override current plan-enablement
or retirement guidance. No destructive reproduction instructions were added.

## Maintenance and evidence

Five dated checkpoints cover Foundational CSPM opt-in, the grouped vulnerability
recommendation retirement, Key Vault management APIs, Sentinel's portal deadline
and the IoT device-builder micro-agent retirement. These checkpoints do not imply
retirement of every related product, data-plane API or OT sensor.

`ADLC_Docs/operations/2026-09-27-sc-100-deep-review.json` records source observations,
objective mappings, blog decisions, guide hashes, arithmetic and repository/site
validation after execution. This is a same-context AI review; independent and
human review remain pending.
