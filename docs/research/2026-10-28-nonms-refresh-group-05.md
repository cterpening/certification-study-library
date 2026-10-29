# Non-Microsoft certification refresh — group 5

**Completed:** 2026-10-28  
**Guides:** 10 (Palo Alto Networks, Splunk, IBM)  
**Selection:** Fifth group of ten from the frozen 167-guide eligible queue, after Groups 1–4.  
**Objective snapshots:** 10 retained unchanged; official exam identity, lifecycle, and current objective evidence were checked.  
**Source health:** The scoped sweep checked 104 URLs: 69 OK, 29 blocked to automation, 6 transport/TLS errors or missing routes, and 1 metadata change. A follow-up check on the replacement XSOAR SaaS release index and docs index returned 2 OK.  
**Independent review:** Fresh-context rubric v2: 10 pass-with-notes, 0 pass, 0 fix-required, 0 blocked. The XSOAR citation-route finding was repaired and verified.  
**Queue after this group:** **117 guides in 12 groups remain.**

## Guides refreshed

- PANW-XSIAM-ENGINEER
- PANW-XSOAR-ENGINEER
- SPLK-5002
- SPLK-5003
- SPLUNK-CLOUD-ADMIN
- SPLUNK-CORE-CONSULTANT
- SPLUNK-ENTERPRISE-ADMIN
- SPLUNK-ENTERPRISE-ARCHITECT
- SPLUNK-O11Y-METRICS-USER
- C1000-156

## Changes applied

- Rechecked current exam identity, lifecycle and official objective material for all ten guides; the accepted objective snapshots did not change. Updated the guide verification metadata and current source-validation receipts.
- Added bounded current product context outside exam-objective maps. Palo Alto XSIAM now cites the July 2026 Cortex announcement. XSOAR now points to the canonical SaaS release index, which lists 8.15 GA (July 26, 2026) and 8.14 GA (May 3, 2026), and describes Azure Blob Storage incident export and continuous Strata Logging Service authentication. SaaS and on-prem release streams remain distinct.
- Updated Splunk Enterprise Security context for ES 8.7 GA and 8.8 Controlled Availability; captured the Enterprise 10.4.2 forwarder stall fix in 10.4.3; and refreshed Cloud ACS compatibility boundaries for version, role, topology and region.
- Corrected Splunk learning-resource details using current official course-track/course descriptions: Cloud Admin’s 18-hour course; Consultant’s 14-course Advanced Power User substitution and authorization exception; Enterprise Admin’s 12-hour System Admin and 18-hour Data Admin courses; and the Architect required course/lab paths. We did not invent aggregate time where course runtimes are absent or restricted.
- Updated O11y context for October 2026 APM missing-tag behavior and Controlled Availability metric sets, with production-change limits. IBM QRadar content notes the Auto Update hostname migration and preserves the conflict between IBM public update-index signals instead of asserting a “latest” update level.
- Refined QRadar learning resources: the official SLA6910 prep is free, 1.5 hours, sign-in required, and marked retiring soon.
- Corrected the XSOAR product-context citation after the independent review found the former May route redirected to a 404. The canonical release index and product documentation index passed a follow-up source-health check.
- Added 28 net new source records across release notes, course tracks, product documentation and official learning resources. Synchronized `docs/LEARNING-RESOURCES.md`; its read-only drift check reported no catalog changes.

## Selected first-party references

- [What’s New in Cortex — July 2026](https://www.paloaltonetworks.com/blog/security-operations/whats-new-in-cortex-july-2026/)
- [Cortex XSOAR 8 SaaS releases](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-8-saas-releases/cortex-xsoar-8-saas-releases.md)
- [Cortex XSOAR documentation index](https://cortex-docs.paloaltonetworks.com/cortex-xsoar-docs/)
- [Splunk Enterprise Security 8.8 release notes](https://help.splunk.com/en/splunk-enterprise-security-8/release-notes-and-resources/8.8/splunk-enterprise-security-release-notes)
- [Splunk Cloud Platform 10.5.2605 release notes](https://help.splunk.com/en/splunk-cloud-platform/release-notes/10.5.2605/splunk-cloud-platform-release-notes/admin-configuration-service)
- [Splunk Observability Cloud October 2026 release notes](https://help.splunk.com/en/splunk-observability-cloud/release-notes/october-2026)
- [IBM QRadar Auto Update endpoint migration notice](https://www.ibm.com/support/pages/node/7278729)
- [IBM C1000-156 exam preparation course SLA6910](https://www.ibm.com/training/course/qradar-siem-v75-administration-exam-c1000-156-preparation-guide-SLA6910)

## Evidence and limitations

The objective monitor found no objective or status snapshot changes. IBM credential and catalog pages were checked; dynamic exam-detail and QRadar docs endpoints had connection resets under the automated checker. Splunk Help pages commonly returned 403 to automation, and the NTIA SBOM reference had a local TLS-chain error. These outcomes are recorded as access or transport limits, not as proof that the technical sources are dead. IBM’s public QRadar update indexes disagree, so the guide leaves the latest update level unresolved and directs learners to verify the installed-version release notes.

The original XSOAR May 2026 documentation route returned 404 after redirection. The current official SaaS release index and general XSOAR documentation index were then opened and checked; both replacement URLs returned HTTP 200. The independent reviewer verified the repaired guide and marked its prior citation-route finding resolved.

No live exam material was used. No product tenant, API, hardware, or lab was exercised, and paid course interiors were not accessed. Independent AI review is not human/community review.

## Research and operations records

The [operations ledger](../../ADLC_Docs/operations/2026-10-28-nonms-refresh-group-05.json) records final guide/objective/status hashes, source-validation receipt IDs, source-health results, independent review status, and build validation. Detailed exam, technical, learning-resource, source-health, and independent-review notes remain in the local `.maintenance/2026-10-29-nonms-refresh/` research handoff.
