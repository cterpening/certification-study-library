# Reusable icons for study diagrams

This independent AI-assisted project uses a selected collection of original
Microsoft artwork to illustrate named services. The starter bundle contains
**14 Azure SVGs**, grouped for **AZ-900** and **DP-900**. These groups are authoring
conveniences, not new exam objectives or complete coverage. The official
[AZ-900](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900)
and [DP-900](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900)
blueprints continue to define scope.

The separate `study-visual-library` repository maintains selections, original
assets, provenance, update scripts and portable exports. This repository contains
an accepted copy under `website/assets/study-icons/`, so building the study site
does not require access to another repository or a live icon download.

## Starter catalog

| Icon | Product or resource label | Profiles |
|---|---|---|
| ![](../website/assets/study-icons/assets/azure-sql-database.svg) | Azure SQL Database | AZ-900, DP-900 |
| ![](../website/assets/study-icons/assets/azure-sql-managed-instance.svg) | Azure SQL Managed Instance | DP-900 |
| ![](../website/assets/study-icons/assets/sql-server-on-azure-vm.svg) | SQL Server on Azure Virtual Machines | DP-900 |
| ![](../website/assets/study-icons/assets/azure-cosmos-db.svg) | Azure Cosmos DB | AZ-900, DP-900 |
| ![](../website/assets/study-icons/assets/azure-storage-account.svg) | Azure storage account | AZ-900, DP-900 |
| ![](../website/assets/study-icons/assets/azure-files.svg) | Azure Files | AZ-900, DP-900 |
| ![](../website/assets/study-icons/assets/azure-block-blob.svg) | Azure block blob | AZ-900, DP-900 |
| ![](../website/assets/study-icons/assets/azure-data-factory.svg) | Azure Data Factory | DP-900 |
| ![](../website/assets/study-icons/assets/azure-virtual-machine.svg) | Azure Virtual Machine | AZ-900 |
| ![](../website/assets/study-icons/assets/azure-virtual-network.svg) | Azure Virtual Network | AZ-900 |
| ![](../website/assets/study-icons/assets/azure-resource-group.svg) | Azure resource group | AZ-900 |
| ![](../website/assets/study-icons/assets/azure-policy.svg) | Azure Policy | AZ-900 |
| ![](../website/assets/study-icons/assets/azure-cost-management.svg) | Azure Cost Management | AZ-900 |
| ![](../website/assets/study-icons/assets/azure-resource-tag.svg) | Azure resource tag | AZ-900 |

Keep a visible product label beside the icon and preserve its appearance and
proportions. A block-blob icon does not represent every storage feature. The
source pack's Power BI Embedded icon is excluded; it should not silently stand in
for all Power BI or Fabric products. Follow the supplied
[Microsoft terms](../website/assets/study-icons/notices/Microsoft_Terms_of_Use.pdf)
and [third-party notices](../THIRD-PARTY-NOTICES.md).

## What we found in the supplied pack

The supplied folder has 714 SVGs, including duplicates and older product labels.
Its original release is unknown. On November 10, 2026, all 14 selected icons and
both supplied PDFs matched Microsoft's currently linked V25 archive byte-for-byte.
The current full archive contains 721 SVGs. Differences are seven new assets and
a moved/redrawn Microsoft Discovery icon, all outside this selection.

The unselected Foundry Control Plane SVG has a malformed viewBox attribute in
both packs. We excluded it. The old FAQ still contains historical Visio plans;
the [current official icon page](https://learn.microsoft.com/en-us/azure/architecture/icons/)
is the source for current distribution guidance. These issues do not require
modifying any of the 14 selected originals.

The [bundle manifest](../website/assets/study-icons/manifest.json) records stable
IDs, original paths, profiles, publisher references and raw file hashes. It records
the source folder's release as unknown; equality of selected files does not
identify the entire original folder as V25. Catalog/hash checks establish file
integrity, not current product behavior or factual review of a study guide.

## Use and update

Choose an asset by its stable ID in the manifest. In HTML/Markdown, reference its
SVG as an image so internal gradient IDs remain isolated. Keep meaningful labels
and accessible explanations in the surrounding diagram or text. For standalone
SVG diagrams, use an embedding method that preserves the original artwork and
check the actual renderer. Do not redraw or recolor vendor symbols.

The [visual-study brief](templates/VISUAL-STUDY-BRIEF.md) still determines the
learning question, facts, relationships, practice version and answer. The icons
support those explanations. Azure SQL comparisons and storage matching activities
are the next planned uses; the existing timeline remains a separate exercise.

Run the independent offline bundle check from this repository:

```powershell
python scripts/check_visual_assets.py
```

For an update, use the producer repository's read-only plan and explicit import
commands, export the requested profiles into a new staging directory, compare
with this bundle, and replace only the accepted bundle contents. Run the checker,
inspect affected visuals, and complete the normal repository/site checks before
committing. The producer contains the detailed update procedure and dated source
comparison. Do not fetch or accept new artwork silently during site builds.
