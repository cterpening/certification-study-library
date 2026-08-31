# Certification inventory

The repository keeps discovery separate from publication:

- `config/certification-seeds.json` is the source-backed research inventory.
- `CERTIFICATIONS.txt` is its generated, tab-separated Python query input.
- `config/exams.json` contains only credentials with complete study guides and
  the metadata needed to publish and monitor them.

An entry in the seed catalog means “research or enrich this credential.” It does
not mean that a guide exists, that its sources have been reviewed, or that it is
ready for the website. Repository validation requires every published guide to
have a seed, but research-only seeds are allowed and expected.

## Current coverage baseline

The catalog was verified on August 31, 2026.

### Microsoft Azure

The scope is the official [Microsoft Learn certification catalog filtered to the
Azure product](https://learn.microsoft.com/en-us/credentials/browse/?credential_types=certification&products=azure).
The August 31 check also enumerated the live Microsoft Learn credentials API and
filtered its results to non-hidden entries whose `credential_types` contains
`certification` and whose `products` contains `azure`. Both views returned 24
certifications. The broader Azure study scope adds the current AZ-802 exam and
SC-100, which Microsoft does not tag with the Azure product. The query file
therefore contains 27 Azure-scope exam rows for 26 credentials; Microsoft
Certified: Windows Server Hybrid Administrator Associate requires both AZ-800
and AZ-801.

The rule deliberately includes cross-product certifications when Microsoft tags
them with Azure, including AB-900, AB-620, and the SC credentials. It then adds
current `AZ-*` exams that the product facet misses and SC-100 because it is the
expert cybersecurity architecture path over Azure security, identity, and
operations credentials. It excludes Applied Skills and retired credentials.
AB-100 and PL-900 are retained separately because this library already publishes
those guides. AI-500 and AZ-802 are explicitly marked beta.

AZ-800 and AZ-801 remain in the current catalog, but Microsoft has announced
that both exams retire on September 30, 2026. Their seed lifecycle is therefore
`retirement-announced`, not merely `active`.

AZ-204 retired on July 31, 2026, and AZ-500 has a retirement date of August 31,
2026. They are not new study targets; AI-200 and SC-500 are their current
successor paths respectively.

### HashiCorp

The scope is every credential shown in the official [HashiCorp certification
catalog](https://developer.hashicorp.com/certifications):

- HashiCorp Certified: Terraform Associate (004)
- HashiCorp Certified: Terraform Authoring and Operations Professional
- HashiCorp Certified: Vault Associate (003)
- HashiCorp Certified: Vault Operations Professional

HashiCorp publishes numeric versions for the associate credentials but does not
display short exam codes for the two professional credentials. The uppercase
professional identifiers in this repository are stable query keys, not claimed
vendor-issued exam codes.

## Updating the inventory

1. Recheck each `catalog_sources` URL and apply its written `selection` rule.
2. Add, change, retire, or remove entries in `config/certification-seeds.json`.
3. Preserve retired entries only when a published guide or downstream history
   still needs the identity, and mark the lifecycle state accurately.
4. Update the source's `last_verified` date.
5. Regenerate and validate:

   ```bash
   python scripts/generate_certification_list.py
   python scripts/validate_repository.py
   ```

The JSON catalog retains official URLs, lifecycle state, provenance, and review
dates. The generated text file intentionally keeps only the three fields useful
as search keys so downstream enrichment can discover its own metadata without
silently overwriting the public source of truth.
