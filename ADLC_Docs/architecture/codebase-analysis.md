# Codebase Analysis — Certification Study Library

> **Last updated:** 2026-09-05 · **Discovery version:** 1 (initial brownfield baseline)

## Executive summary

This repository is an inherited, public-facing certification content system rather than a conventional deployed application. Markdown guides and schema-backed JSON catalogs are the source of truth. Python command-line programs validate those sources, monitor public vendor material, prepare independent audit/freshness batches, and generate an allowlisted MkDocs site. GitHub Actions and GitHub Pages are the documented delivery platform, but their remote settings and execution history were outside the approved evidence boundary. The repository has strong content-governance and test foundations; its main brownfield constraints are scale, stable catalog contracts, centralized automation, and incomplete independent/human assurance coverage.

## Discovery identity and boundary

| Field | Value |
|---|---|
| Target | `certification-study-library` |
| Commit | `8c1ceaf01279ebc51058d77f91369bf6f24193f1` |
| Evidence | Local files, local Git history, and existing validated repository-health artifacts |
| Network/authentication | None |
| Project commands during discovery | None |
| Infrastructure input | No ARM export, Resource Graph result, cloud inventory, or IaC supplied |
| Adoption | Reference-only; no accelerator content copied into the target |

## Technology stack

| Area | Observed technology | Role |
|---|---|---|
| Primary content | Markdown with structured front matter | Canonical study guides and project documentation |
| Structured data | JSON governed by ten JSON schemas | Exams, vendors, collections, sources, reviews, health, freshness, and audit state |
| Automation | Python 3.13 in checked-in workflows; standard-library-heavy scripts | Validation, monitoring, batch preparation, and site generation |
| Tests | Python `unittest` | Unit and contract-oriented regression checks |
| Site generator | MkDocs 1.6.1 and MkDocs Material 9.7.7 | Static documentation site |
| Delivery definitions | GitHub Actions YAML | Pull-request validation, scheduled monitoring, and Pages deployment |
| Presentation | Maintained Markdown, HTML templates, JavaScript, and CSS under `website/` | Homepage and generated-site experience |
| Dependency installation | pip with `requirements-site.txt` | Three exactly pinned site packages |

No `pyproject.toml`, package lockfile, formatter configuration, linter configuration, type-checker configuration, Node package manifest, container definition, Terraform/Bicep, Kubernetes/Helm, application database, queue, or cache was found in the bounded tracked-file inventory.

## Repository scale

| Surface | Observed count |
|---|---:|
| Tracked files | 758 |
| Guide Markdown files | 222 |
| Data files and objective/status snapshots | 451 |
| Repository JSON schemas | 10 |
| Python automation scripts | 8 |
| Python test files | 8 |
| GitHub workflow definitions | 4 |
| Structured issue-form files | 5 |
| Registered sources | 3,248 |

## Components and entry points

| Component | Entry or source | Responsibility | Brownfield constraint |
|---|---|---|---|
| Guide corpus | `guides/*.md` | Learner-facing certification material | Public URLs, front matter, objective maps, citations, and review labels are contract-like |
| Catalog model | `config/*.json`, `data/*.json`, `schemas/*.json` | Publication inventory, source provenance, reviews, lifecycle, and assurance state | Stable IDs and cross-file references must remain compatible |
| Repository validator | `scripts/validate_repository.py` | Central schema, content, link, chronology, and aggregate consistency gate | Approximately 1,900 physical lines; currently overlooks duplicate source-health IDs |
| Objective monitor | `scripts/check_official_study_guides.py` | Provider-specific public objective/status retrieval and comparison | Approximately 2,200 physical lines with 26 routed adapter keys |
| Source-health monitor | `scripts/check_source_health.py` | Public URL reachability and metadata change signals | Network-capable; reviewed writes are deliberately separate |
| Assurance batch preparation | `scripts/prepare_ai_audit_batch.py`, `scripts/prepare_source_freshness_scan.py` | Risk-ranked read-only review inputs | Results remain bound to baselines and rubrics |
| Site preparation | `scripts/prepare_site.py` | Creates allowlisted generated source and navigation | `.site-build/` and `site/` are disposable boundaries |
| Site validation | `scripts/validate_site.py` | Checks generated pages, links, anchors, headings, and skip-link behavior | Requires generated site input |
| Certification list generator | `scripts/generate_certification_list.py` | Renders the text inventory from canonical configuration | Imports rendering behavior from the validator module |
| Delivery | `.github/workflows/*.yml` | Validation, monitoring, artifacts, issues/PRs, and Pages deployment | Remote enablement, protections, history, and success are unknown |

All eight Python scripts expose `main` entry points. The scripts use `snake_case` functions, `PascalCase` parser/test classes, uppercase module constants, `pathlib`, type annotations, and standard-library JSON/HTTP handling. The repository's own conventions take precedence over the accelerator Python profile's pytest/Ruff defaults.

## Dependencies

### Local build dependencies

| Dependency | Declared version | Use |
|---|---|---|
| `jsonschema` | 4.26.0 | Repository schema validation |
| `mkdocs` | 1.6.1 | Static site build |
| `mkdocs-material` | 9.7.7 | Site theme and extensions |

### External systems represented by local evidence

| Dependency | Relationship | Observed evidence | Current-state limitation |
|---|---|---|---|
| Official certification and product sites | Upstream public scope and technical evidence | Source catalog, objective snapshots, HTTP clients | No network access used in discovery; live state not verified |
| GitHub repository service | Source collaboration and issue/PR workflow | Local remote configuration, issue forms, documentation | Repository settings and branch governance unavailable |
| GitHub Actions | Validation and scheduled maintenance | Four workflow definitions | Enablement, history, artifacts, duration, and reliability unavailable |
| GitHub Pages | Static-site hosting | Publishing documentation and deployment workflow | Actual configuration and deployed state unavailable |
| Python package index or approved mirror | Supplies site dependencies when installing | Requirements and workflow install step | No package access or installation during discovery |

## Configuration and secrets approach

- Repository-relative paths are normally derived from `Path(__file__)` rather than environment variables.
- Network-capable scripts use command-line arguments and explicit `--write` or output options; monitoring and mutation are deliberately separated.
- Checked-in workflows use the repository-scoped `GITHUB_TOKEN` according to declared permissions; no token value is stored in the repository.
- No application connection string, database configuration, committed `.env`, credential file, or secret store integration was found.
- The earlier bounded heuristic found no common private-key or token signatures. That result is not equivalent to a comprehensive secret scan.

## Architecture characteristics

| Characteristic | Current state |
|---|---|
| Pattern | Content/data pipeline with deterministic validation and static-site generation |
| Runtime service | None in the repository; output is a static artifact |
| Containerized | No |
| Platform coupling | Moderate at delivery and maintenance boundaries through GitHub Actions/Pages |
| Configuration | Checked-in JSON/YAML/Markdown; no runtime environment configuration observed |
| Multi-module | Yes: content, catalogs/schemas, validation, monitoring, assurance batches, site preparation, and delivery |
| Data persistence | Version-controlled JSON and Markdown; no application database |
| External I/O | Public HTTP retrieval by two maintenance scripts; not used during discovery |
| Trust boundary | Generated content is untrusted until source/review gates pass; site publication uses an explicit allowlist |

## Current conventions to preserve

- Official blueprints define exam scope; product documentation supports technical behavior.
- AI assistance, unofficial status, review state, and volatile claims remain visible to readers.
- Candidate sources do not enter the approved catalog without review.
- Objective/source change automation creates evidence and review work rather than rewriting guides automatically.
- JSON schemas and repository validation guard the catalog relationships.
- Generated `.site-build/` and `site/` content remains disposable and uncommitted.
- Existing Python standard-library, unittest, CLI, typing, and repository-relative path conventions remain authoritative until a separate modernization decision is approved.

The machine-readable baseline is `ADLC_Docs/discovery/current-style-baseline.json`. Proposed future intent is separate in `ADLC_Docs/discovery/target-standards-intent.json`.

## Observations and existing validated concerns

The following are existing normalized findings, not new backlog items:

1. `repository-health:content-assurance:coverage-gap` — independent AI audit covers 39 of 222 guides, freshness review covers 33, ten audit findings remain open, and no guide is marked community-reviewed.
2. `repository-health:source-health:duplicate-identifiers` — 3,255 source-health rows represent 3,248 IDs; duplicate IDs are silently collapsed by validation.
3. `repository-health:maintainability:automation-concentration` — two large automation modules centralize validation and provider routing, while adapter documentation trails implementation.
4. `repository-health:ci:duplicated-validation-and-partial-update-coverage` — validation steps are duplicated and dependency-update governance is partial.
5. `repository-health:accessibility:manual-evidence-unrecorded` — the documented manual accessibility checklist has no retained completion evidence.

## Evidence gaps

- Remote default branch, branch protection, rulesets, required checks, review requirements, workflow history, Pages settings, releases, and deployment status.
- Clean-machine setup/build evidence, repeated test runs, coverage, mutation, lint, formatting, type-checking, dependency vulnerability, and support-lifecycle evidence.
- A formal ADR set and a current system diagram predating this discovery output.
- Named ownership for repository paths and retention/review ownership for the assessment artifacts.
- Completed browser, keyboard, screen-reader, responsive, contrast, print, and reduced-motion evidence.

## Changes since the previous discovery version

Not applicable. This is Discovery version 1. Future refreshes should update this document in place and summarize changes here.

