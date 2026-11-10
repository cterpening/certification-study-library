# Completed visual brief: DP-900 SQL management choices

**Status:** Independent AI-assisted draft; human review pending. The
[official DP-900 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)
is authoritative. Accepted objective baseline: **July 21, 2026**. This is selected
objective practice, not complete exam coverage.

## Evidence and scope

**Exact objective:** Describe the Azure SQL family of products, including Azure
SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines

**Source unit:** `relational-management` in
[DP-900 data decisions / units.json](../../study-packs/dp-900-data-decisions/units.json).
Reuse its vendor-agent requirement and conditional service reasoning without
changing the source package. Its normalized `study_material.json_text` SHA-256 is
`e507e0e26816ca2acd4009f4e537a9538d8638e86a399c7744edeed6db05ac22`.
The source unit's other objectives are deliberately outside this exercise.

**Guide context:** [Azure relational services / Choose the management boundary
before the SKU](../../../guides/DP-900-microsoft-azure-data-fundamentals.md#choose-the-management-boundary-before-the-sku).
The accepted objective file is
[`data/objective-snapshots/dp-900-official-objectives.txt`](../../../data/objective-snapshots/dp-900-official-objectives.txt).
The upstream package manifest binds the canonical guide, accepted objectives,
authored content and source records. This exercise's manifest binds the current
package manifest as well as its own inputs and artifacts.

| Fact to teach | Registered source and exact section | Evidence and qualification |
|---|---|---|
| Database and Managed Instance maintain the engine/OS platform; customer database and security work remains | `microsoft-azure-sql-options-overview`, [What is Azure SQL? — Administration](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview#administration) | Read November 10, 2026; confirmed first-party behavior. The drawing separates engine maintenance from customer data/access decisions. |
| VM control includes guest OS, SQL installation and added software; management automation exists | Same [Administration](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview#administration) and **SQL Server on Azure VMs** sections | Read November 10, 2026; confirmed control boundary. An unspecified vendor's support remains unverified. |
| Database, instance and OS requirements suggest different candidates | Same [comparison page](https://learn.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview), **Comparison table** and product sections | Read November 10, 2026; conditional teaching synthesis. VERIFY CURRENT: exact features, support and recovery configuration. |

## Learning design

**Question:** Which control boundary fits the workload, and what work remains with
the customer? **Prerequisite:** A database stores application data; an operating
system hosts software. No purchasing model, service tier, or SQL syntax is needed.

**Misconceptions:** PaaS means the customer has no data/access/recovery duties;
VM management must all be manual; broader control is always better; “SQL Server
compatible” means every feature and vendor application will work unchanged.

**Selected form:** Three equal columns comparing the same four layers. App/data/
access is at the top, SQL engine platform and guest OS in the middle, Microsoft
Azure infrastructure underneath all three. A dashed boundary moves downward for
the VM, showing the additional customer administration. Text labels carry every
responsibility distinction, so color is redundant. The top row is a responsibility
model, not a claim that an application is hosted inside a database service.

**Visual language:** 1200-pixel width and 1400-pixel height; navy `#102b40`, teal
and amber match the existing DP-900 timeline. Equal column widths communicate
comparison, not ranking. Original Microsoft icons identify their named services;
they are embedded as unchanged source bytes with preserved proportions through
the shared helper. No icon is redrawn or recolored. Reference:
[accepted visual-assets guide](../../../docs/VISUAL-ASSETS.md),
[bundle manifest](../../../website/assets/study-icons/manifest.json), and
[Microsoft icon terms](../../../website/assets/study-icons/notices/Microsoft_Terms_of_Use.pdf).

**Original requirements:** A database-oriented cloud app; an existing workload
needing instance features without an OS agent; and the source unit's vendor
requirement for a guest OS agent and SQL installation control. These are invented
inputs, not real deployment findings. They establish a candidate to evaluate,
not a complete architecture decision.

## Paired outputs and accessibility

**Study:** [study.svg](study.svg) keeps the comparison visible, then presents each
requirement beside a candidate and operational tradeoff. It states the VM choice
explicitly for the guest-agent scenario.

**Practice:** [practice.svg](practice.svg) preserves the same service labels,
responsibility stacks, qualifications and requirements. The answer column is
replaced by neutral writing prompts and lines. Its title, description, visible
labels and image alt text do not contain the worked answers. Facts in the
comparison are intentionally supplied; the task is to apply them and explain a
tradeoff. It is not a memorization test.

**Text alternatives:** The README first provides a table of all meaningful stack
labels and the three questions, then a distinct **Study answers and rationale**
section. Each SVG has its own title and description, readable source text and
logical column order. The service name appears beside its icon. The dashed
boundary and explicit CUSTOMER/MICROSOFT labels carry meaning without color.

**Success:** Identify a reasonable candidate from each requirement, connect the
choice to the needed control layer, explain remaining customer work, and name a
validation step. Recovery requirements and access decisions remain customer work;
managed backups do not choose business recovery needs. This is not a claim of
exam readiness or product certification.

## Reproduction and review

Run `build.py` to regenerate the pair and manifest; `build.py --check` checks
bound inputs and outputs without writing. Inputs are local. The shared helper
validates the upstream package and original icon bundle. Its manifest records
normalized text fingerprints, original icon byte fingerprints and output hashes.

Evidence reading and author checks are AI work. Human review and live Azure
execution are pending. Rendering, visual inspection and any independent review
are separate coordinator checks; this brief does not assert that they have
occurred. Recheck the labels, answers, qualifications, text alternatives and
source evidence whenever a bound input changes. A rebuild cannot renew factual
or human review by itself.
