# Microsoft blocker follow-up — September 28, 2026

All **14 certification records with blockers** were rechecked against 30 current primary pages. **None can be closed from the evidence obtained.** This is a focused follow-up, not a new full-guide audit or a live-service test. It preserves the existing guide warnings, full-review dates and accepted objective snapshots.

The next dated checks remain in the [review tracker](../MICROSOFT-REVIEW-STATUS.md). Today is September 28: a scheduled September 30 retirement or October revision has not happened merely because its date appears in a source. The [Windows Server credential](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-administrator-associate/) still states that AZ-800 and AZ-801 retire September 30 and AZ-802 remains. The [central retirement page](https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams) still lists MS-102 for November 30.

## Findings and closure criteria

### AZ-800

The Windows Server sign-in article still both excludes Conditional Access with the extension and describes enforcing it. Client/device-policy caveats do not explicitly reconcile the blanket exclusion. Hyper-V sockets documents transport prerequisites, not a current supported end-to-end SSH Direct guest setup.

**Evidence needed to close:** Microsoft must specify the supported server/client/extension/authentication combination and scope of the exclusion. A current Microsoft-supported host/guest/package/command recipe or explicit retirement/support statement is needed.

Sources: [az800-entra](https://learn.microsoft.com/en-us/entra/identity/devices/howto-vm-sign-in-azure-ad-windows), [hyperv-socket](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/make-integration-service), [windows-credential](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-administrator-associate/).

### AZ-802

The transport reference still lacks a supported end-to-end SSH Direct guest recipe. AZ-802 remains the documented path after AZ-800/AZ-801 retire.

**Evidence needed to close:** Obtain a supported current host/guest recipe; keep SSH-over-IP distinct from SSH Direct.

Sources: [hyperv-socket](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/make-integration-service), [windows-credential](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-administrator-associate/).

### AB-210

The knowledge article denies Opportunity Agent custom-field support and immediately instructs adding those fields. Close Agent management stops in-process work, while setup says existing orchestrations continue after deactivation.

**Evidence needed to close:** Clarify agent type, feature stage and supported custom fields. Clarify whether Stop and deactivation differ, and document the disposition of already-running work.

Sources: [ab210-knowledge](https://learn.microsoft.com/en-us/dynamics365/sales/configure-sqa-knowledge-source), [ab210-close-manage](https://learn.microsoft.com/en-us/dynamics365/sales/manage-sales-close-agent), [ab210-close-setup](https://learn.microsoft.com/en-us/dynamics365/sales/configure-sales-close-agent).

### MS-102

The policy permits a two-year recovery window, while the restore-frequency table covers only days 0–365 and the prose refers to weeks 2–52. The central retirement page still gives November 30, 2026 for MS-102.

**Evidence needed to close:** Publish recovery-point intervals for each workload in days 366–730; do not extrapolate first-year intervals.

Sources: [backup-policy](https://learn.microsoft.com/en-us/microsoft-365/backup/backup-view-edit-policies?view=o365-worldwide), [backup-restore](https://learn.microsoft.com/en-us/microsoft-365/backup/backup-restore-data?view=o365-worldwide), [backup-updates](https://learn.microsoft.com/en-us/microsoft-365/backup/backup-whats-new?view=o365-worldwide), [retirements](https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams).

### AB-650

The same second-year recovery-frequency gap as MS-102 remains.

**Evidence needed to close:** Use the shared Backup clarification; a longer retention setting does not establish a second-year restore-point interval.

Sources: [backup-policy](https://learn.microsoft.com/en-us/microsoft-365/backup/backup-view-edit-policies?view=o365-worldwide), [backup-restore](https://learn.microsoft.com/en-us/microsoft-365/backup/backup-restore-data?view=o365-worldwide), [backup-updates](https://learn.microsoft.com/en-us/microsoft-365/backup/backup-whats-new?view=o365-worldwide).

### AB-250

The Contact Center migration plan uses September 30, 2026 for new-customer number restrictions; its deprecation ledger uses September 23. Existing-resource and existing-number eligibility statements also differ.

**Evidence needed to close:** Confirm the applicable service, tenant/resource/number cohort and acquisition/port-in cutoff through authoritative service guidance before planning an affected action.

Sources: [ab250-migrate](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/migrate-from-azure-communication-services), [ab250-deprecated](https://learn.microsoft.com/en-us/dynamics365/contact-center/implement/deprecations-contact-center), [acs-retirement](https://learn.microsoft.com/en-us/azure/communication-services/acs-retirement-and-breaking-changes-guide).

### AI-200

The creation guide forbids changing clustering policy; the 2025-07-01 update contract allows changes from NoCluster and architecture adds a geo-replication restriction.

**Evidence needed to close:** Publish one supported migration recipe identifying source/target policy, API version, replication/module constraints, availability and data-loss implications.

Sources: [redis-create](https://learn.microsoft.com/en-us/azure/redis/quickstart-create-managed-redis), [redis-update](https://learn.microsoft.com/en-us/rest/api/redis/redisenterprisecache/databases/update?view=rest-redis-redisenterprisecache-2025-07-01), [redis-architecture](https://learn.microsoft.com/en-us/azure/redis/architecture).

### MS-700

The platform overview still calls private-channel Flow bot support unfinished. The newer dated developer update says private channels are supported through Power Automate and describes Teams-app rollout. Historical paragraphs on that same announcement remain.

**Evidence needed to close:** Reconcile bot versus user identity, portal versus Teams entry point, cloud and rollout cohort. Do not promote a planned rollout date to observed tenant delivery.

Sources: [teams-webhooks](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/what-are-webhooks-and-connectors), [teams-retirement](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/).

### SC-300

The authentication/access summary gives 25–30%, but its detailed heading gives 20–25% in the same current outline.

**Evidence needed to close:** Microsoft must correct the conflicting domain weights; retain the caveat and cover the objective content.

Sources: [sc300-outline](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300).

### SC-200

The Continuous/NRT supported-table list includes Sentinel tables; unified hunting known issues still excludes Sentinel NRT. Table-management text says moving to Lake tier stops Advanced Hunting; September and unified-hunting guidance describe lake access with onboarding-cohort and retention restrictions.

**Evidence needed to close:** Clarify exact table/cloud/cohort eligibility for Sentinel continuous custom detection. Reconcile lake-only versus extended Analytics retention and the September 23 onboarding boundary, with an explicit supported query path.

Sources: [sc200-detections](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules), [sc200-hunting](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender), [sc200-tiers](https://learn.microsoft.com/en-us/azure/sentinel/manage-table-tiers-retention), [sc200-updates](https://learn.microsoft.com/en-us/azure/sentinel/whats-new).

### SC-401

The skills heading and change log use October 28, 2026; the credential announcement uses October 14.

**Evidence needed to close:** Microsoft must reconcile the effective date. Keep accepted historical snapshots unchanged until the applicable revision is established.

Sources: [sc401-outline](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401), [sc401-credential](https://learn.microsoft.com/en-us/credentials/certifications/information-security-administrator/).

### AB-100

The exam prerequisite list still includes MB-280 and PL-200; the credential list omits them. A source-only check cannot determine whether an individual historical award satisfies eligibility.

**Evidence needed to close:** Obtain authoritative eligibility clarification for the disputed credentials and award dates; no account-specific eligibility claim.

Sources: [ab100-credential](https://learn.microsoft.com/en-us/credentials/certifications/agentic-ai-business-solutions-architect/), [ab100-exam](https://learn.microsoft.com/en-us/credentials/certifications/exams/ab-100/).

### AB-410

The connector procedure includes SAP, while the limitations enumerate Dataverse, Salesforce, Oracle and Zendesk without SAP.

**Evidence needed to close:** Clarify current SAP prompt-data support and its runtime/connector conditions.

Sources: [ab410-knowledge](https://learn.microsoft.com/en-us/ai-builder/use-your-own-prompt-data).

### AZ-120

Native HSR groups nodes into one logical backup item and tracks the primary; the FAQ recommends stopping protection on a secondary and resuming when primary without clearly identifying a different protection model.

**Evidence needed to close:** Identify which protection model the FAQ recipe applies to before executing any stop/resume procedure.

Sources: [az120-architecture](https://learn.microsoft.com/en-us/azure/backup/azure-backup-architecture-for-sap-hana-backup), [az120-faq](https://learn.microsoft.com/en-us/azure/backup/sap-hana-faq-backup-azure-vm).

## Evidence and next action

The receipt at `ADLC_Docs/operations/2026-09-28-microsoft-blocker-followup.json` records timestamps, HTTP results, source URLs, response and extracted-text hashes, prior reports and the per-certification observations above. All 30 target pages were fetched; HTTP success alone did not resolve any conflict. Relevant sections were read, not every section of each long manual. Bounded discovery did not identify a current authoritative SSH Direct recipe or a second-year Backup interval table. This is not a claim that no such evidence can exist.

The Backup question is shared by MS-102 and AB-650; SSH Direct is shared by AZ-800 and AZ-802. A single authoritative clarification can inform both affected guides. The closure criteria above are ready for a practitioner or vendor support discussion; no messages or support tickets were sent. User-specific prerequisite eligibility needs account-specific confirmation.

Local learning exercises and vendor-service validation are recorded separately. A simulated positive result must not be used to remove a vendor-documentation blocker. The existing September 30 and October checkpoints remain due for fresh evidence.
