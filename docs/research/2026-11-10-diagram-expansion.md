# AZ-900 and DP-900 diagram expansion — November 10, 2026

Two new [study/practice pairs](../../examples/visual-exercises/README.md) improve
explanations of already-selected topics. The AZ-900 scope map makes role and
policy assignments visible around an original blocked-deployment scenario. The
DP-900 comparison shows management responsibilities across the three Azure SQL
options, followed by original requirement-to-candidate exercises.

The four SVGs include original Microsoft icons, accessible descriptions, visible
labels, and separate worked and practice versions. They remain independent
AI-assisted drafts with human review pending. Official exam blueprints define
scope; adding another format does not add objective coverage.

## Scope and first-party evidence

| Exercise | Accepted baseline | Exact mapped objective |
|---|---|---|
| AZ-900 scope and governance | July 20, 2026 | Describe Azure role-based access control (RBAC) |
| AZ-900 scope and governance | July 20, 2026 | Describe the purpose of Azure Policy |
| DP-900 SQL choices | July 21, 2026 | Describe the Azure SQL family of products, including Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines |

The [AZ-900 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900)
and [DP-900 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)
are the authority for those objectives. Each reviewer checked the exact accepted
snapshot and read the complete unchanged canonical guide as context.

Technical evidence opened during this bounded work and independently by the
relevant content reviewer:

| First-party source | Supported explanation |
|---|---|
| [Azure RBAC overview](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview) | Principal, role, and scope relationships |
| [Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview) | Assignment applicability, location requirements, and deny effects |
| [Azure SQL comparison](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview?view=azuresql) | Product choices, platform/guest-OS responsibilities, recovery qualifications, and VM automation |

The AZ-900 drawing shows scope associations, not an internal execution sequence.
Its dashed VM is a proposed request. The DP-900 application/data/access layer
describes responsibility, not application hosting inside a database service.
Product candidates follow the invented requirements; actual application and
vendor compatibility still need validation. The SQL exercise does not claim
normalization coverage from the broader source unit.

## Review and reproducibility

Two separate fresh-context, read-only content reviews returned **pass**, with no
material findings. Reviewers checked the full guides as context, accepted
objective snapshots, selected source units, exercise files, gallery, current SVG
descriptions, and rendered study/practice previews. They found no observed
clipping or overlaps. Labels and boundaries convey meaning without relying only
on color. Practice text and accessible descriptions retain givens without the
worked answers. The coordinator also inspected all four rendered previews.

A separate implementation reviewer found no material issues in the shared
`scripts/visual_exercise.py` helper. Scratch probes checked deterministic output,
exact embedded icon bytes, stale source/output rejection, declared icon/profile
validation, and path restrictions. These were targeted probes, not added unit
tests. The helper supports fixed authored layouts; it does not create new
teaching content unattended or sanitize arbitrary untrusted SVG input.

Each exercise manifest binds the selected unit, package manifest, builder,
shared helper, accepted icon bundle, embedded original icon bytes, and output
SVGs. Both exercise `build.py --check` commands passed in independent review.
The offline production smoke runner now checks both pairs alongside the earlier
DP-900 data-freshness pair. Public-site preparation includes the gallery,
exercise text, SVGs, and linked manifests.

This is bounded AI review of new exercises. It is not whole-guide semantic
review, human review, screen-reader testing, learner testing, live Azure
execution, or vendor compatibility certification. Canonical guides, accepted
baselines, source catalogs, and whole-guide review dates remain unchanged.

## Reviewed hashes

SHA-256 text hashes normalize UTF-8 CRLF/CR to LF. Objective snapshots and
original icon bytes use raw hashes. Each linked exercise manifest contains the
individual icon hashes and builder bindings.

| Input or artifact | AZ-900 | DP-900 |
|---|---|---|
| Complete canonical guide | `09dafd7ca0dffee692577828c9efca74232f668469361d83e4a2b081c0d021f0` | `1c618b776923450c7bbf59aac51ce2bf3b64cfb5dcc214e6b4b388a718332991` |
| Accepted objective snapshot, raw | `8b4c89d325b3ce339eb881aa2dc4b251888e6d7a07d6351d81bcc2123b1c4449` | `7cef780d1a9e8e88b587fba89acb994985c4aedbd491710e814686ce5dc6559f` |
| Selected unit | `b582037da541e60d1f129e28eaf634a9cd3962a227f98dbcfb2e334847b3f68f` | `e507e0e26816ca2acd4009f4e537a9538d8638e86a399c7744edeed6db05ac22` |
| Source-package manifest | `fa82722db742d1e1889f3a80192487b691452596e613963c755dd76be4157d28` | `2473aca4a6044d59c7b2b31c13a117aee35216198c6781f174ca117c469b1db1` |
| Study SVG | `1589191872c4c2a1847d8bb1829cde0fb42fb44d9cccb3bd9ab7d93c2c30b3f2` | `73e4d9c60ae72772610854ace19890633e1c82b07d6dd9de319bb5dde736eba0` |
| Practice SVG | `ab71b0b518ad3af958d0a6993d0869b7d193d5cb57425dc14abd5b045307a03c` | `fbc175be72062782477f46008226a8ecc3a685816e94e63953adf3abfbd20bef` |
| Exercise manifest | `dd85348276fde97942723587532442d4f80550130ed9dd9f65d7f3c47a693824` | `69d1c412f08248ff75e23638c09d6464669f25342476f8d9e7040cb112d96b13` |

Shared helper: `26e8058aae6bc28011f3e85e3b016b6fae270c71cd5b364cc865c19af2871e2f`.
Accepted icon-bundle manifest, raw:
`8e8331d7c36ab30f9a748bcae153dfefedfcd708f4be19cb87e990b51395cc62`.

See the [AZ-900 manifest](../../examples/visual-exercises/az-900-governance-scope/manifest.json)
and [DP-900 manifest](../../examples/visual-exercises/dp-900-sql-choices/manifest.json).
The reviewed gallery hash was
`313b85236bfbe5256288e07e660da84cd58cbc008b45da5824884ea62458e7d5`;
the coordinator subsequently added only a link to this review record.
