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

The Azure and HashiCorp baseline was verified on August 31, 2026. The broader
Microsoft catalog expansion was rechecked on September 1, 2026 and is being
published one source-validated guide at a time.

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

### Microsoft beyond Azure

The broader Microsoft expansion uses the unfiltered official Microsoft Learn
certification catalog while excluding Applied Skills and Microsoft Office
Specialist credentials. Microsoft Certified Educator is also deferred. A
credential enters the generated query list when its guide is published, so each
per-certification commit remains independently valid and reviewable.

MS-102 is included as an announced-retirement credential because its exam and
Microsoft 365 Certified: Administrator Expert certification remain earnable
through November 30, 2026. Microsoft had not named a direct replacement as of
the September 1 review.

AB-650 is included as a beta credential. Its official study guide was last
updated July 27, 2026 without a separate “skills measured as of” date, and Microsoft had
not yet published a Practice Assessment as of the September 1 review. Beta exam
status, objectives, product surfaces, languages, scoring timing, and assessment
availability must be rechecked before scheduling.

SC-401 is included as the active Microsoft Certified: Information Security
Administrator Associate exam. Its current skills baseline is July 28, 2026;
Microsoft publishes a free Practice Assessment and lists no retirement date.

### Lifecycle and replacement rule

- An already retired exam is not a current study target and is omitted from the
  generated query list unless an existing published guide or downstream history
  requires its identity to be preserved.
- An exam with an announced future retirement remains in scope. Its seed records
  `retirement-announced` and the exact `retirement_date`; its guide must show the
  date prominently.
- When the vendor names a replacement, the seed also records
  `replacement_exam_code` and `replacement_official_url`. A replacement code must
  exist in this inventory. Beta replacements remain labeled beta.
- A retiring guide explains that earned-credential and transition behavior must
  be verified with the vendor; it does not imply automatic conversion to the new
  credential.

AZ-800 and AZ-801 remain in the current catalog, but Microsoft has announced
that both exams retire on September 30, 2026. Their seed lifecycle is therefore
`retirement-announced`, not merely `active`.

[AZ-204](https://learn.microsoft.com/en-us/credentials/support/credential-retirement)
retired on July 31, 2026, and
[AZ-500](https://learn.microsoft.com/en-us/credentials/certifications/azure-security-engineer/)
retired on August 31, 2026. They are not new study targets. The current successor
paths are [AI-200](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-cloud-developer-associate/)
and [SC-500](https://learn.microsoft.com/en-us/credentials/certifications/cloud-and-ai-security-engineer-associate/),
respectively; these are new credentials rather than an assertion that an earned
retired credential converts automatically.

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
   still needs the identity, and mark the lifecycle state accurately. For every
   announced or completed retirement, record its date; when the vendor identifies
   a replacement, record and validate the replacement code and official URL.
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
