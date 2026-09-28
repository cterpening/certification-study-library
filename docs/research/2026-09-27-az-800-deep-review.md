# AZ-800 deep review — September 27, 2026

The complete AZ-800 guide was reviewed against all 101 detailed objectives in 16
subgroups. The January 21 blueprint and captured retirement notice are unchanged.
The guide now contains ten labs and 29 answered checks, including five new worked
examples and two supplementary blog readings. The September 30 retirement warning
and the AZ-802 path remain prominent.

Source validation **remains blocked**. Microsoft documentation does not establish a
current end-to-end SSH Direct support contract, and the Entra Windows VM sign-in
article makes conflicting Conditional Access statements. Completed research is
recorded separately from a clean validation pass and live infrastructure testing.

## Changes that help learners

| Topic | Correction or learning addition |
|---|---|
| Entra join and guest access | Scope the server join example to supported Azure VMs; distinguish VM management permissions from guest-login roles, identity and extension health |
| Service accounts | Cite dMSA requirements directly and teach a bounded one-service migration with host authorization, logs and retained account dependencies |
| PowerShell second hop | State the explicit WinRM limitation and compare downstream SMB with nested WinRM; prove which identity reaches the resource |
| SMB | Teach connection direction, edition-specific signing defaults and diagnosis of an older NAS without an estate-wide protection downgrade |
| File Sync and migration | Add a cache-budget example, offline-access test, independent backup requirement and explicit cutover/rollback acceptance points |
| AKS | Separate platform, Kubernetes version, Windows node image and container base image; bound node-pool retirement and gMSA statements to the documented Azure Local configurations |

The [guide](../../guides/AZ-800-administering-windows-server-hybrid-core-infrastructure.md)
links each technical claim to its supporting documentation. The shared
[SSH Direct evidence review](../SSH-DIRECT-EVIDENCE.md) now identifies a missing
historical CentOS package artifact instead of presenting it as current evidence.

## Blog intake

Two public articles were accepted as supplementary reading with explicit limits:

- **SriniThumala, Microsoft FastTrack, March 8, 2026:** the File Sync/Storage Mover
  comparison helps distinguish lasting hybrid operation from a migration project.
  Current product documentation controls compatibility; the article's NFS/preview,
  deployment and scale claims were not adopted. Backup and zero-downtime wording is
  qualified. No separate update date was shown.
- **Ned Pyle, Microsoft, August 23, 2024:** the SMB hardening article explains the
  purpose of the security controls. It is a preview-era article; current signing
  documentation controls edition and direction details. Its complete public body
  was inspected in the page's embedded data because the main HTML representation
  was nearly empty. Embedded videos were not reviewed; no later article update date
  was verified.

The attributed links, reading estimates and original exercises are in the guide's
Places to learn section. Neither article is treated as an exam blueprint, universal
support matrix or substitute for product documentation.

## Evidence and validation boundary

The machine-readable operations record
`ADLC_Docs/operations/2026-09-27-az-800-deep-review.json` preserves the prior records,
guide hashes, per-objective positions/hashes and section mappings, source fetch
observations, findings, link totals and validation results. It retains both the
source gap and the explicit Conditional Access contradiction. Source reachability
does not prove access to gated lessons, videos or assessment questions.

The cache arithmetic was checked offline. PowerShell examples were syntax checked;
no Windows Server, AD DS, Hyper-V, Azure or tenant lab was executed. Review and repair
were performed by the same AI context; independent and human reviews remain pending.
Publication uses the shared unit-test, repository-validation and strict-site gate.

The [Microsoft review tracker](../MICROSOFT-REVIEW-STATUS.md) includes this completed
research with blockers and keeps the remaining certifications in the review queue.
