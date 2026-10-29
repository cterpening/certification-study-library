# Non-Microsoft certification refresh — group 4

**Completed:** 2026-10-28  
**Guides:** 10 (Palo Alto Networks)  
**Selection:** Fourth group of ten from the frozen 167-guide queue, ordered by last source-validation date, vendor ID, and exam code.  
**Objective snapshots:** 10 retained unchanged; the current datasheet/objective maps matched the accepted snapshots.  
**Source health:** 95 scoped links checked; 90 OK, 5 externally blocked, 0 broken.  
**Independent review:** Fresh-context rubric v2; 7 pass, 3 pass-with-notes, 0 fix-required/blocked. Three low-severity source-association notes remain open; they do not indicate unsupported guide claims.

## Guides refreshed

- PANW-NETWORK-SECURITY-ARCHITECT
- PANW-NETWORK-SECURITY-PROFESSIONAL
- PANW-NGFW-ENGINEER
- PANW-SD-WAN-ENGINEER
- PANW-SECURITY-OPERATIONS-ARCHITECT
- PANW-SECURITY-OPERATIONS-PROFESSIONAL
- PANW-SSE-ENGINEER
- PANW-XDR-ANALYST
- PANW-XDR-ENGINEER
- PANW-XSIAM-ANALYST

## Changes applied

- Checked each current official exam datasheet and credential page against the accepted snapshot. All ten credentials remain active; no retirement, replacement, or locale changes were found. We kept every objective snapshot unchanged.
- Replaced stale July 2025 handbook references with the September 2026 *Palo Alto Networks Certification Handbook*. Refreshed the shared catalog entry and added the current two-year validity, same-track higher-level renewal, 545-day repeat-after-pass wait, and 15/30/90-day failed-attempt waits.
- Rechecked each vendor learning route. The digital paths are free and self-paced but require Learning Center sign-in; their module count and total runtime are not publicly stated. Added optional instructor-led course names and published runtimes where offered, along with access/prerequisite caveats. No dedicated ILT is listed for the Network Security or Security Operations Architect/Professional guides.
- Added bounded, dated product context where it fits the existing guide: PAN-OS 12.1/12.2 behavior and upgrade constraints; Prisma Access 6.2 IPv6, resilience and Secure Agentless Access; Prisma SD-WAN 2026 Site Protection Profiles, Site Snapshots and lifecycle notices; and Cortex XDR/XSIAM release changes. Every item is marked as product context, not a new exam objective, and retains its version, rollout, entitlement, or validation limits.
- Replaced a dead Cortex XSIAM 2.5 documentation route (404) with Palo Alto Networks’ accessible July 2026 Cortex release post. Cortex documentation route redirects/availability limits are recorded in the research notes; the affected product statements stay bounded to sources that opened.
- Added 17 reviewed official learning/release sources and aligned the handbook’s supported-exam metadata. Updated 10 source-validation receipts. Objective and lifecycle snapshots were not changed.

## Evidence and limitations

- The September 2026 handbook was checked directly. It records the current certification validity and retake rules above. Each dynamic exam PDF was reviewed manually against the retained local objective snapshot; automated extraction alone was not treated as proof of unchanged content.
- The course Learning Center is sign-in/JavaScript gated. Public sources support free self-paced access and specific ILT names/runtimes, but do not show complete digital-path modules or runtime. Course interiors were not accessed.
- Source health found five blocked links already in guide resource lists (including HHS, EU Data Act, LIVEcommunity, and two O’Reilly pages); the linked claims are not dependent solely on those pages. No newly added official training/release source was blocked or broken. The dead XSIAM 2.5 docs URL was excluded and replaced by an accessible official July 2026 Cortex release post.
- Cortex XDR 6.0 was announced on October 19, 2026; this is recorded as an announcement and not as a generally available release. Product availability, licensing, supported software/hardware, and tenant rollout remain **VERIFY CURRENT** where noted.
- No product tenant, lab, API or hardware was exercised. No live exam material was used.

## Selected first-party references

- [Palo Alto Networks Certification Handbook](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/ebooks/panw-certification-handbook.pdf)
- [Palo Alto Networks Education Services](https://www.paloaltonetworks.com/services/education)
- [PAN-OS 12.1 default behavior changes](https://docs.paloaltonetworks.com/ngfw/release-notes/12-1/changes-to-default-behavior/changes-to-default-behavior-in-pan-os-12-1)
- [Prisma Access 6.2 features](https://docs.paloaltonetworks.com/prisma-access/new-features/by-version/prisma-access/6-2-preferred-innovation)
- [Prisma SD-WAN features introduced in 2026](https://docs.paloaltonetworks.com/prisma-sd-wan/release-notes/new-features/prisma-sd-wan-release-information/prisma-sd-wan-features-introduced-in-2026)
- [Cortex XDR 6.0 announcement](https://www.paloaltonetworks.com/blog/security-operations/cortex-xdr-6-0/)
- [What’s New in Cortex — July 2026](https://www.paloaltonetworks.com/blog/security-operations/whats-new-in-cortex-july-2026/)

## Research records

The independent audit found three low-severity metadata-only gaps: a few already registered supplementary sources linked in the Network Security Architect, Security Operations Professional, and XDR Analyst guides omit those exam codes from their `supported_exams` metadata. All ten guides passed the substantive checks; the current handoff and source health are recorded in the operation evidence. Detailed exact URLs, per-guide reconciliation, learning-resource evaluation and product constraints are in the dated research reports under `.maintenance/2026-10-29-nonms-refresh/`; source-health detail is in `.maintenance/2026-10-29-nonms-refresh/g04-source-health.md` and the full independent review is in `.maintenance/2026-10-29-nonms-refresh/g04-independent-review.md`.

