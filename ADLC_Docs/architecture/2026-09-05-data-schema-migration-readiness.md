# Data and Schema Migration Readiness Assessment

## Assessment envelope

- Target: `certification-study-library`; reference-only accelerator revision `82d4bca`.
- Source revision: `858bdfc664f1b8e94ce03ab041acf3fbba7c4f07`; assessed on 2026-09-06. September 5 filenames preserve the approved action-plan paths.
- Mode/profile: Snapshot / standard; status: **partial**. Public repository files and bounded local Git only; no project tests, builds or scanners executed in this pass.
- Budget: target 10 minutes, ceiling 20 minutes per lane; maximum eight assessment checks; zero external evidence requests. Shared reads and the validated September 5 facts were reused.
- Finding set: [validated JSON](../findings/2026-09-05-data-schema-migration-readiness.json). Findings below retain canonical fingerprints across overlapping reports; do not sum repeated findings as unique risks.
- Handling: approved-external. Selected public repository evidence was processed by the active Codex session; artifact publication to the existing Git origin is separately user-authorized. No other evidence-provider requests occurred.
- Retention/review: repository owner; artifacts retained under the approved `ADLC_Docs/` paths and Git history. Retention period, expiry action and assistant service retention/region are unspecified. Findings review pending; no risk acceptance or implementation approval inferred.

## Decision summary

Overall migration readiness: **not assessed**; catalog integrity: **not ready for an unqualified compatibility claim**. Git-tracked JSON is the observed system of record and the public site is derived. The repository maintainer is the proposed decision-owner role; no named data owner or target-platform decision is recorded. The safe next decision is to review catalog integrity and compatibility requirements. Migration execution is not authorized.

## Evidence coverage and access gaps

| Domain | State | Evidence and decision impact |
|---|---|---|
| Ownership and system of record | Observed / owner unknown | `docs/ARCHITECTURE.md`; canonical catalogs feed disposable output |
| Classification, residency, retention | Public-content policy observed; retention unknown | `docs/CONTENT-POLICY.md`; internal work mirror excluded |
| Lineage and contract compatibility | Partial | Catalogs, ten schemas, validator and site generator are visible; external consumers unknown |
| Workload, consistency, availability | Partial / unknown | File-based batch processing; no service SLO, concurrency requirement or recovery target supplied |
| Security, cutover, reconciliation and rollback | Partial / not assessed | Git review boundary and local invariants visible; no migration or restore rehearsal supplied |
| Operability and cost | Partial / unknown | Maintainer CLI workflow documented; no cost or downtime constraint supplied |

## Data boundary and handling

Only the intended-public metadata, schema structure, aggregate counts and relevant automation were inspected. No live store, credentials, records export or private work mirror was accessed. Owner classification/retention decisions beyond the repository public-content policy remain unknown.

## System of record, producers, consumers, and lineage

| Component | Reads / writes | Evidence / state |
|---|---|---|
| Maintainer review | Seeds, exams, sources, reviews and guides | `docs/ARCHITECTURE.md`; stated workflow |
| Objective/source monitors | Public URL metadata → reviewed snapshots | `docs/AUTOMATION.md`; local implementation |
| Validator | Catalogs, schema declarations, guide metadata and snapshot hashes | `scripts/validate_repository.py`; observed |
| Site preparation | Approved catalogs/guides → `.site-build/` | `scripts/prepare_site.py`; observed |
| Work mirror / external consumers | Downstream documentation or unknown consumers | `docs/WORK-MIRROR.md`; not accessed, compatibility unknown |

## Workload and non-functional requirements

Observed workload is batch file processing over 222 published exams and 3,255 health records representing 3,248 IDs. Stable identifiers join catalogs, reviews and guides. Freshness records are historical batches; health is consumed as a current snapshot. Growth rates, concurrent writers, latency goals, transaction guarantees, availability, downtime, RPO/RTO and retention/deletion requirements are unknown. No database transaction or online cutover need is inferred.

## Schema, contract, and compatibility risks

The two canonical findings below cover duplicate health identity and incomplete schema enforcement. Before a contract change, reconcile one row per source ID, required fields/types, references to exam/vendor/source IDs, dates, hashes and consumer behavior. Schema version fields alone do not prove backward compatibility.

## Security, identity, network, and operations constraints

The public-content policy and review gate are observed. Remote GitHub controls and downstream/private storage remain unassessed. Keep migration data public and scoped to approved repository files; an accountable owner must define recovery and retention requirements before a target decision.

## Target options and decision inputs

No platform comparison or product selection was performed. Retaining versioned files is the observed current shape, not an approved migration recommendation. Alternative storage shapes cannot be evaluated without workload, owner, consistency and recovery constraints.

## Migration, cutover, reconciliation, and rollback readiness

| Stage | Required evidence | State |
|---|---|---|
| Contract change | Old/new schema and all affected readers/writers | Partial |
| Reconciliation | Counts, unique IDs, referential rules, hashes and rejected records | Existing checks plus documented gaps |
| Cutover | Coordinated consumer compatibility and acceptance criteria | Not assessed; no migration requested |
| Rollback | Retained prior Git revision plus verification of consumer compatibility | Mechanism available; rehearsal unavailable |
| Decommission | Owner retention and downstream completion decision | Not assessed |

## Blocked decisions and evidence requests

Repository owner: identify external consumers and the authoritative health-record policy before contract migration. Supply recovery/downtime and classification constraints only if a storage migration is proposed. No decision deadline was supplied.

## Proposed findings and delivery handoff

Review the two existing/normalized concerns below. Counts, identity and consumer tests are verification inputs for any later change; no candidate or specification has been generated.

## Assumptions, exclusions, and re-run triggers

Assume only the locally declared consumers. Re-run after schema/identifier changes, new consumers, a failed reconciliation, or an approved migration requirement. Remote provider state and private mirrors remain excluded.

## Canonical findings

### Source-health rows are not unique by source identifier

- Fingerprint: `repository-health:source-health:duplicate-identifiers`; medium severity, high confidence; disposition: open.
- Observation: The source-health ledger contains 3,255 rows for 3,248 registered source IDs. Six IDs are duplicated, including one ID with three rows. The current repository validator reduces health rows to a dictionary keyed by ID before comparing coverage, so duplicates are overwritten and the validator still passes. This can distort aggregate reporting and makes duplicate records invisible to the main consistency gate.
- Evidence: `data/source-health.json`; `scripts/validate_repository.py`; `test.result.repository-validator`.
- Proposed action: Canonicalize source-health output to one record per source ID and make duplicate IDs a schema or repository-validation failure.
- Proposed owner: repository automation maintainers; due date not supplied.

### Declared catalog schemas are not uniformly applied

- Fingerprint: `assessment:data-contracts:uneven-schema-enforcement`; medium severity, high confidence; disposition: open.
- Observation: Only the source-freshness catalog is passed to validate_json_schema in main. The other schemas are parsed as JSON, while their catalogs rely on handwritten checks. Those checks cover many business rules but do not establish parity with every declared constraint, creating a compatibility gap when schemas evolve.
- Evidence: `scripts/validate_repository.py:1520`; `scripts/validate_repository.py:1800`; `schemas/source-health.schema.json`.
- Proposed action: Make schema-to-catalog validation explicit while retaining the cross-catalog business rules.
- Proposed owner: repository automation maintainers; due date not supplied.

## Limitations and next decision

External consumers, accountable data ownership, availability/downtime targets, recovery objectives and migration requirements have not been supplied. No database, migration target or live data access is in scope.

No collection error was reported. Observations above come from local evidence; consequences and recommended actions are assessment judgments. Historical checks are labeled with their original date. Review the findings before any backlog, specification or implementation work.

