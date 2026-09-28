# AZ-801 deep review — September 27, 2026

The complete guide was read and mapped against 115 detailed objectives in 19
subgroups. The October 6, 2025 blueprint and captured retirement notice are unchanged.
The guide retains the September 30 retirement warning, AZ-802 replacement route and
explicit discrepancy between the canonical blueprint weights and the exam page.
The canonical study guide remains the teaching authority.

## Content improvements

- Explain OSConfig policy ownership and why removing an assignment does not guarantee
  restoration of the original configuration.
- Add the installed-update boundary for 2026 Kerberos RC4 enforcement, with a service
  failure example separating supported algorithms, available keys and actual tickets.
- Add September's fixed-duration immutability support, distinguishing the immutable
  window from retained recovery points and an irreversible vault lock.
- Add an original recovery timeline that measures dependency repair and application
  validation as well as the VM restore job.
- Flag the retired direct AMA-to-Storage/Event-Hubs preview and teach how to identify
  its DCR kind and verify the supported replacement route.

Four worked learning examples, a ninth evidence lab and six new answers extend the
guide to **nine labs and 30 answered checks**. The new lab distinguishes a completed
tabletop review from executed infrastructure evidence. Existing ADE, ADMT, legacy
agent and VM Insights Map lifecycle boundaries remain explicit.

## Blog selection

Matthew Palko's **Beyond RC4 for Windows authentication** (Microsoft, December 3,
2025; updated February 4, 2026) was accepted for its account-key and event reasoning.
The current rollout KB controls the dated update phases; linked scripts were not
executed. Attribution, a reading estimate and an original exercise appear in the
[guide](../../guides/AZ-801-configuring-windows-server-hybrid-advanced-services.md).

The July 22, 2026 Tech Community article **Some tools and techniques for hardening
Windows Server** was considered but not added. Targeted OSConfig and SMB sections
use a scenario path and Server 2025 signing-default description that conflict with
current implementation documentation. Its public embedded article was readable after
decoding a compressed response. This was a targeted suitability check, not an audit
of every section, linked script or video. Publication recency alone did not justify
recommending it.

## Evidence and remaining limits

`ADLC_Docs/operations/2026-09-27-az-801-deep-review.json` preserves prior records,
guide hashes, objective positions/hashes and section mappings, source observations,
blog decisions, citation counts and validation results. Accepted objective/status
baselines were not rewritten. Three paid training pages remain access-blocked;
reachable public catalogs do not prove access to their lessons or questions.

Synthetic recovery arithmetic was checked offline. No Azure, AD DS, OSConfig,
Windows Server or recovery lab was executed. Research and repair used the same AI
context; independent and human review remain pending. The shared publication gate
covers unit tests, repository validation, strict site build and generated-site checks.
See the [Microsoft review tracker](../MICROSOFT-REVIEW-STATUS.md) for the remaining work.
