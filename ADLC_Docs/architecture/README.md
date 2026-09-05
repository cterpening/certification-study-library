# Architecture Overview — Certification Study Library

> **Last updated:** 2026-09-05 · **Discovery version:** 1 (initial brownfield baseline)

## Executive summary

Certification Study Library is a schema-backed, AI-assisted public content system. Its canonical Markdown guides and JSON catalogs are validated by Python automation, transformed through an explicit publication allowlist, built as a strict MkDocs static site, and intended for GitHub Pages. The architecture deliberately separates official-source evidence, generated explanation, independent audit, human review, and repair decisions. No application runtime, database, container, IaC, or owned Azure infrastructure was found. The current modernization complexity is **M**: runtime architecture is simple, but 222 guides, 3,248 source records, ten interrelated schemas, 26 provider-adapter keys, and existing assurance/data-integrity debt create a meaningful compatibility and review burden.

## Current architecture

| Aspect | Current state |
|---|---|
| Pattern | Version-controlled content/data pipeline with deterministic gates and static-site generation |
| Hosting intent | GitHub Pages through a checked-in Actions workflow; remote state unverified |
| Data tier | Markdown and schema-backed JSON in Git; no application database |
| Integration | Public vendor HTTP retrieval by maintenance scripts; GitHub workflow/issue/PR/Pages services |
| Build | Allowlisted site preparation followed by strict MkDocs build and generated-site validation |
| Trust model | Official source authority, candidate promotion gate, AI disclosure, independent audit, separate human review, and separate repair pass |
| Ownership model | Repository contribution/security guidance and structured issue forms; path ownership and remote enforcement unknown |

See:

- `ADLC_Docs/architecture/codebase-analysis.md` for the component and convention inventory;
- `ADLC_Docs/architecture/dependency-map.md` for internal and external relationships;
- `ADLC_Docs/architecture/infrastructure-inventory.md` for the explicit no-IaC/no-cloud-evidence result;
- `ADLC_Docs/discovery/current-style-baseline.json` for preserved inherited conventions; and
- `ADLC_Docs/discovery/target-standards-intent.json` for proposed, unapproved future intent.

## Brownfield constraints

1. Guide and catalog formats are public and cross-referenced contracts; broad rewrites can affect the whole library.
2. Official-source provenance, volatile-claim labels, exam-integrity boundaries, and AI/human review distinctions must remain visible.
3. Stable identifiers and snapshot hashes bind catalogs, source health, objective baselines, reviews, audits, and freshness results.
4. The site preparation allowlist is a security boundary, not merely a build convenience.
5. Current Python/unittest/CLI conventions outrank generic accelerator defaults until a modernization change is approved.
6. Remote GitHub governance and operational state cannot be inferred from checked-in workflow files.

## Modernization assessment

- **T-shirt size:** M
- **Sizing basis:** Small runtime/dependency footprint, offset by high content volume, schema relationships, provider diversity, central automation modules, and public compatibility requirements.
- **Not included:** No platform migration, cloud move, schedule, budget, or implementation estimate was requested or produced.
- **Primary complexity drivers:** catalog referential integrity; content-assurance scale; provider parser variability; public-site compatibility; workflow and remote-control unknowns.
- **Primary risks:** silent data drift, incomplete semantic/freshness coverage, automation review load, duplicated validation definitions, and unrecorded accessibility evidence.

## Recommended next steps

These are assessment-routing recommendations, not approved backlog work:

1. Review the five existing normalized repository-health findings and decide their dispositions.
2. Approve a small local-only assessment wave focused on source-health schema integrity, test maturity, content/AI assurance, and documentation/style conformance.
3. Decide whether a separate authenticated read-only GitHub evidence pass is permitted for protections, workflow history, Pages, and release state.
4. Confirm repository/assessment data classification, artifact retention, and a human review owner.
5. Keep all code, content, schema, workflow, and modernization changes behind later finding, candidate, specification, and implementation gates.

The proposed lanes and exact boundaries are in `ADLC_Docs/architecture/action-plan.md`.

## Discovery handoff status

| Criterion | Status |
|---|---|
| Current code/content/data inventory | Complete for bounded local Snapshot |
| Infrastructure inventory | Complete as a local no-IaC/no-cloud-evidence result; remote delivery services remain unknown |
| Dependency map | Complete for observed local relationships |
| Current style separated from target intent | Complete |
| Catalog assessment decisions | Complete and awaiting human review |
| Assessment operations approved | No |
| Findings reviewed | Pending |
| Backlog/spec/implementation authority | None |

## Changes since the previous discovery version

Not applicable. This is Discovery version 1.
