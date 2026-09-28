# AZ-802 deep review — September 27, 2026

The complete guide was read and mapped against **115 detailed objectives in 18
subgroups**. Accepted objective and status snapshots are unchanged. Active delivery
is retained and stale beta wording removed. The separate five-day AZ-802T00 course
is available despite unavailable-training text on the credential page; practice
assessment availability must still be checked before relying on it.

## Content improvements

- Add prerequisite-based service-account reasoning, including supported dMSA hosts,
  a discoverable Windows Server 2025 DC and unsupported migration combinations.
- Explain why a PowerShell second-hop decision needs the downstream protocol and
  principal; constrained delegation is not a supported nested WinRM solution.
- Separate GPU-P compatibility, migration requirements and surviving capacity. A
  two-node example has eight partitions normally but only four after losing a node,
  leaving a two-partition deficit for six modeled workloads.
- Explain File Sync offline availability: a visible tiered filename does not prove
  that its contents are cached. Separate client SMB traffic from agent HTTPS traffic.
- Correct Server 2025 SMB signing defaults; clarify OSConfig policy authority and
  restoration limits, installed-update phases for RC4, retired direct AMA telemetry
  and VM Insights Map's restricted onboarding and retirement.

Four worked examples, a ninth evidence lab and six new answers bring the guide to
**nine labs and 34 answered checks**. The new lab requires recording versions,
prerequisites, a success and a failure case, evidence and rollback. A paper worksheet
is explicitly distinguished from executed infrastructure evidence.

## Blog selection

Orin Thomas's **GPU Partitioning in Windows Server 2025 Hyper-V** (Microsoft Tech
Community, July 2, 2025) was accepted as a bounded architecture reading. Its public
embedded article was read. Current product documentation supersedes the article's
one-partition-per-VM limit; the guide assumes one partition per modeled workload
only for its arithmetic. Hardware support does not guarantee spare capacity or
successful live migration. Linked commands were not executed.

Matthew Palko's **Beyond RC4 for Windows authentication** (Microsoft, December 3,
2025; updated February 4, 2026) was accepted for account-key and event reasoning.
Current KB5073381 controls the rollout dates and support boundaries; linked scripts
were not executed. Both readings have attribution, a time estimate, an original
exercise and current primary documentation in the
[guide](../../guides/AZ-802-administering-windows-server.md).

## Evidence and remaining limits

`ADLC_Docs/operations/2026-09-27-az-802-deep-review.json` preserves prior records,
guide hashes, objective positions/hashes and section mappings, source observations,
blog decisions, citation counts and validation results. Historical accepted
objective/status snapshots were not rewritten.

SSH Direct remains an official objective without a verified current supported
end-to-end guest recipe. The historical CentOS package URL now returns 404; the
[shared SSH evidence](../SSH-DIRECT-EVIDENCE.md) preserves that limitation. Five
paid catalog pages remain access-blocked. Historical displayed course durations and
contents do not establish current lesson access.

Synthetic GPU capacity arithmetic was checked offline. No GPU, Hyper-V, Azure,
Windows Server, AD DS or File Sync infrastructure lab was executed. Research and
repair used the same AI context; independent and human review remain pending. The
shared publication gate covers unit tests, repository validation, strict site build
and generated-site checks. See the
[Microsoft review tracker](../MICROSOFT-REVIEW-STATUS.md) for remaining work.
