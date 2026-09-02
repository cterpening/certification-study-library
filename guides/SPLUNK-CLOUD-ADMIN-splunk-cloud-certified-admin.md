---
exam_code: SPLUNK-CLOUD-ADMIN
vendor_id: splunk
official_blueprint: https://www.splunk.com/content/dam/splunk2/en_us/pdfs/training/splunk-test-blueprint-cloud-admin.pdf
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# Splunk Cloud Certified Admin Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The live certification page, four-page public blueprint, current Splunk Cloud Platform service/admin/data-ingestion documentation, and selected learning resources were checked September 2, 2026. This guide contains original learning material, not exam items. Recheck the [official certification page](https://www.splunk.com/en_us/training/certification-track/splunk-cloud-certified-admin.html) and [test blueprint](https://www.splunk.com/content/dam/splunk2/en_us/pdfs/training/splunk-test-blueprint-cloud-admin.pdf) before scheduling.

**Current baseline:** Cloud Overview (5%); Index Management (5%); Authentication/Authorization (5%); Configuration Files (5%); Getting Data in Cloud (15%); Forwarder Management (5%); Monitor Inputs (15%); Network/Other Inputs (10%); Input Fine-tuning (5%); Parsing/Data Preview (10%); Raw Data Manipulation (10%); Apps (5%); Cloud Support (5%). Related topics may appear and the blueprint may change without notice.<br>
**Exam contract:** professional; 60 multiple-choice questions; 75 total minutes including three minutes for the exam agreement; USD 130 per attempt; Pearson VUE delivery<br>
**Prerequisite contract:** Splunk Core Certified Power User is explicitly required.<br>
**Upcoming/product boundary:** no retirement or replacement was announced. Cloud capabilities vary by subscription, region, release, role, and deployment experience. The blueprint's “Self-Service Cloud” versus “Managed Cloud” wording must be learned for the exam, while current work should follow the live service description, Admin Config Service compatibility, and the controls exposed to the actual tenant.<br>

## How to use this guide

Treat every ingestion change as a pipeline change with cost, privacy, retention, search, and rollback consequences. Practice on customer-managed forwarders and a nonproduction Cloud stack or official lab. Never send production data, credentials, tokens, personal data, or listening ports to an unmanaged lab.

For each data source, preserve:

1. owner, purpose, source system, volume, format, time zone, sensitivity, and retention;
2. supported collection topology, network path, certificate/authentication method, and least-privileged token;
3. input, source/host/sourcetype/index, parsing/transform definitions, and precedence;
4. sample-to-preview-to-search validation, ingestion health, and duplicate/loss tests;
5. rollback, support boundary, app/config ownership, and operational contact.

> **About related items:** A `Related item:` callout adds architecture, governance, security, operations, or current-platform context. It makes the objective more useful in practice but does not imply the extra phrase appears verbatim in the public blueprint.

## Blueprint map

| Domain group | Weight | Evidence to produce |
|---|---:|---|
| Cloud platform, indexes, identity, configuration | 20% | Responsibility map, governed index/RBAC design, and effective-config/processing trace |
| Forwarding and forwarder management | 20% | Authenticated/tested forwarding plus deployment-server/app rollout and rollback |
| Monitor, network, Windows, script, and HEC inputs | 25% | Source-specific input definitions with duplicate/loss/security evidence |
| Fine-tuning, parsing, and raw transformation | 25% | Representative Data Preview suite and reversible props/transforms/SEDCMD design |
| Apps and Support | 10% | Entitlement-aware app process and reproducible support case package |

## 1. Splunk Cloud overview — 5%

Splunk Cloud Platform is a SaaS delivery of Splunk search/index capabilities. Splunk operates specified service infrastructure, upgrades, backups, and platform controls; the customer remains responsible for data-source setup, forwarders/collectors, connectivity, identity/roles, data correctness, configuration within entitlement, contacts, and use. Do not transpose access to operating systems or indexer files from self-managed Enterprise.

Topology includes customer environments and collectors/forwarders, secured ingest endpoints, Splunk-managed indexing/search service, and user/API access. Additional collection tiers such as heavy forwarders or IDM capabilities depend on design/deployment experience. Current self-service surfaces include Splunk Web, ACS API/CLI, and supported app/administrative workflows; some changes still require Support.

The blueprint asks for Self-Service versus Managed Cloud differences. At decision time, ask who can perform the task, through which supported surface, on which deployment experience, and whether Support/app vetting/restart is required. Use the current [service details](https://help.splunk.com/en/splunk-cloud-platform/get-started/service-terms-and-policies/10.5.2605/information-about-the-service/splunk-cloud-platform-service-details), not an assumed responsibility split.

> **Related item:** SaaS removes some infrastructure operations, not customer accountability. Data classification, lawful collection, source health, identity lifecycle, search-content quality, costs, and incident response remain shared/customer responsibilities.

## 2. Index management — 5%

An index stores event or metrics data and supplies a boundary for retention, access, and search. Design names, data type, purpose/owner, retention, search defaults, sensitivity, and volume. Too many arbitrary indexes increase administration; too few can mix incompatible retention/access needs.

Current Cloud controls can create/update/delete indexes and monitor size/event/time ranges. Deleting an index permanently removes its data and index according to current docs; verify exact target, dependencies, archive/retention obligations, approval, and recovery posture before acting. This destructive topic belongs in a disposable lab only.

Monitor ingestion volume, license/workload entitlement, source distribution, earliest/latest event, storage/retention, disabled status, and unexpected changes. A stable total can hide one silent source. See [Manage Splunk Cloud Platform indexes](https://help.splunk.com/en/splunk-cloud-platform/administer/admin-manual/10.0.2503/manage-your-indexes-and-data-in-splunk-cloud-platform/manage-splunk-cloud-platform-indexes).

## 3. Authentication and authorization — 5%

Users receive capabilities, index access/defaults, search limits/filters, and object privileges through roles and role inheritance. Access is additive across held/inherited roles; a restrictive role does not subtract permission granted elsewhere. Use least privilege, separate admin duties, test effective access (“search as” where authorized), and avoid modifying Cloud system users/roles.

The blueprint names LDAP, Active Directory, and SAML. Understand directory-backed authentication versus SAML federation conceptually, identity/attribute mapping, group-to-role mapping, certificates/metadata, login/logout, local break-glass accounts, and failure/rollback. Current Cloud-supported methods, provisioning, and exact configuration vary; follow the tenant service description and current identity docs. Authentication proves identity; authorization determines actions/data.

## 4. Configuration files and processing — 5%

Splunk behavior is composed from `.conf` stanzas in system/app/user contexts. Effective settings result from precedence, not one file. Never edit default files; place managed changes in supported local/app packages. Use `btool` on customer-managed Splunk instances to inspect merged settings/source paths; Cloud service-tier files may require app, ACS, or Support workflows.

Index-time processing determines event boundaries, timestamps, metadata, routing/filtering, and stored raw data. Search-time processing extracts/enriches/normalizes fields and knowledge. Index-time errors can be costly or irreversible; prefer search-time transformations when they meet requirements.

## 5–6. Forwarding and forwarder management — 20%

Universal forwarders are lightweight collectors without the full parsing/search tier. Heavy forwarders can parse, route, run many inputs/apps, and add capacity/administration. Full Splunk Enterprise can forward but is not normally chosen merely as an agent. Select by input support, parsing/routing, topology, throughput, security, management, and failure needs.

Cloud onboarding provides a supported forwarding configuration/credentials package or documented endpoint flow. Install only on compatible versions, validate certificates, protect credentials, configure outputs and inputs separately, restart safely, and confirm both network connectivity and indexed events. A successful TCP connection does not prove correct index/sourcetype/time/event construction.

Optional forwarding settings include load balancing groups, acknowledgments, queues, compression, routing, connection/timeouts, and throughput controls. Exact options trade latency, duplicate risk, loss behavior, and capacity; test rather than enabling every option.

A customer-managed Deployment Server distributes deployment apps to deployment clients using server classes. Deployment apps package inputs/outputs/props and related settings. Separate configuration by responsibility, set target allowlists carefully, canary rollout, inspect phone-home/client status, and preserve rollback. The deployment server is not a general package manager for Splunk's managed Cloud tier.

> **Related item:** Forwarder credentials and HEC tokens are secrets. Distribute them through approved mechanisms, restrict source networks/index permissions, rotate, and make logs/support bundles redact them.

## 7. Monitor inputs — 15%

Monitor inputs follow appended data in files/directories and maintain checkpoints so restarts do not normally reread everything. A broad directory monitor recurses and can ingest rotated, compressed, temporary, or duplicate files unless include/exclude rules are correct. The `batch` input consumes/deletes files and is not interchangeable with monitor.

Define `[monitor://path]`, `index`, `sourcetype`, host behavior, allow/deny lists, recursion, ignore-older, and CRC/checkpoint-related options only from current docs. Overlapping stanzas can apply independently; test rotation, truncation, same-leading-content files, permissions, symlinks/mounts, restart, and backfill.

In Cloud, monitoring almost always occurs on a forwarder that sends to the service. The current [monitor files/directories guidance](https://help.splunk.com/splunk-cloud-platform/get-data-in/get-started-getting-data-in/9.2.2406/get-data-from-files-and-directories/monitor-files-and-directories) distinguishes the collection responsibility.

## 8. Network and other inputs — 10%

TCP has a connection and ordered stream; UDP has datagrams without delivery/order guarantees. Bind only required interfaces/ports, enforce network controls, avoid privileged/colliding ports, size queues, and understand that plain TCP/UDP inputs may expose unencrypted data. For Cloud, receive network data on a customer-controlled forwarder/collector unless the current supported service explicitly provides the endpoint.

A scripted input runs a customer-approved command on an interval or continuously and ingests stdout; stderr supports diagnostics. Use absolute paths, least privilege, timeout/locking, stable output, checkpoints/idempotency, secret hygiene, and bounded resource use. Never write secrets to stdout.

Windows inputs can include Event Logs, performance counters, registry changes, Active Directory monitoring, WMI, and file monitors depending on forwarder/version. Choose the native supported input and least privileges; verify channel, checkpoint, locale, volume, and event rendering.

HTTP Event Collector accepts token-authenticated event/metric payloads over HTTP(S). Separate tokens by producer/use, restrict allowed indexes/network, protect/rotate tokens, validate event versus raw endpoint/payload, timestamps, sourcetype/host/source, batching, acknowledgments, retry/backoff/idempotency, and load distribution. HTTP success alone does not prove searchable correctness.

## 9–11. Input, parsing, and raw transformation — 25%

Input processing reads bytes and establishes initial metadata. Fine-tune an explicit sourcetype and correct character encoding when known. Wrong encoding corrupts characters before later extraction; wrong sourcetype applies the wrong parsing/knowledge contract.

Parsing constructs events: line breaking/merging, timestamp recognition, time zone, metadata transformation/routing, and raw modification. Prefer positive event-boundary rules (`LINE_BREAKER`) and avoid unnecessary line merging; multiline configuration needs representative stack traces and maximum-size safeguards. Timestamp rules need prefix/lookahead/format, time zone, fallback behavior, and future/past bounds. Missing timestamps can receive file/input/current time depending on source/configuration.

Data Preview is a hypothesis test: use samples spanning normal, multiline, malformed, locale, DST, oversized, missing-time, new-version, and boundary cases. Validate event count, `_raw`, `_time`/zone, host/source/sourcetype/index, fields, and warnings before sending production volume.

`props.conf` selects data and invokes parsing/search-time behavior; `transforms.conf` defines reusable regex/format/destination transformations. Routing to queues/indexes, dropping data, masking, and metadata rewrites depend on the execution tier and correct stanza scope. `SEDCMD` applies sed-like raw text replacement at parsing time for suitable cases.

Mask sensitive values before they reach Splunk whenever possible. Transformations are not a retroactive privacy strategy: already indexed raw data remains governed by existing retention/deletion processes. Regex failures can leak data or destroy evidence; canary and test both matches/nonmatches.

> **Related item:** Ingest actions and edge/collector capabilities may provide newer routing/filtering/masking paths. They are valuable current alternatives, but do not replace the blueprint's explicit props/transforms/SEDCMD mechanics.

## 12. Installing and managing apps — 5%

Apps can contain search knowledge, UI content, data collection components, and configuration. Splunkbase apps, private apps, and input/forwarder components have different trust and installation paths. Check Cloud compatibility, version, dependencies, publisher, permissions/capabilities, network/file access, included indexes, upgrade/migration impact, and support ownership.

Cloud app installation may be self-service or require vetting/Support depending on app, tenant experience, entitlement, and risk. ACS can manage supported app operations programmatically for compatible deployments. Install collection components on customer-managed tiers where required. Test in nonproduction, export/backup supported configuration, document ownership, monitor after change, and plan rollback/removal.

## 13. Working with Splunk Cloud Support — 5%

Before escalation, isolate scope: user/source/index/search/app/forwarder/region, first/last occurrence, recent change, reproducibility, business impact, error/message, expected/actual, health/CMC evidence, relevant IDs/timestamps/time zone, configuration/effective output, network tests, and safe logs. Remove credentials/personal data.

Choose correct severity from actual impact, provide operational contacts and authorized access, follow Support collection instructions, preserve case chronology, test proposed changes in scope, and confirm resolution/root cause/prevention. Do not make unsupported service-tier changes to “work around” a symptom.

The [Cloud administration hub](https://help.splunk.com/en/splunk-cloud-platform/administer) links the Admin Manual, ACS, security, and operational guidance.

## Integrated scenarios

### Scenario 1: Managed log-source onboarding

Deploy a canary universal forwarder through a deployment app, monitor rotated multiline UTF-8 logs, set index/sourcetype, preview timestamps/boundaries, send securely to Cloud, and validate volume/events/search. Exercise restart, rotation, network outage, duplicate/loss, malformed lines, and rollback.

### Scenario 2: Multi-input collection tier

Use an approved heavy forwarder for TCP/UDP, a basic script, and Windows input; compare it with HEC. Apply least privilege, routing, queue/backpressure, token/certificate controls, and props/transforms masking in a synthetic dataset.

### Scenario 3: Cloud operational change

Design an event index and role, document identity mapping, install a compatible private app through the supported tenant path, monitor CMC/index activity, inject a controlled fault, and assemble a redacted Support case with effective configuration and evidence.

## Hands-on labs

1. Cloud-versus-Enterprise responsibility/topology and capability matrix using the current service description.
2. Index/RBAC design with retention, effective access tests, monitoring, and a documented destructive-delete simulation only.
3. Configuration precedence and index-time/search-time operation trace on a customer-managed forwarder.
4. Forwarder onboarding/connectivity/search validation plus deployment-server canary/rollback.
5. Monitor input rotation/restart/overlap/CRC/backfill/permission test matrix.
6. TCP/UDP/scripted/Windows/HEC comparison with authentication, reliability, metadata, and failure evidence.
7. Data Preview suite for line breaking, timestamps/zones, encoding, and malformed/oversized events.
8. Props/transforms/SEDCMD routing, filtering, and synthetic masking with leak/overmatch regression tests.
9. App compatibility/vetting/self-service/ACS/Support decision and rollback package.
10. Reproducible redacted support case from a controlled ingest fault.

## Original readiness checks

1. Which infrastructure tasks does Splunk manage, and which ingestion tasks remain customer-owned?
2. Why should Enterprise file-system assumptions not be applied to Cloud?
3. What current interfaces can expose self-service administration?
4. What design boundaries does an index provide?
5. Why is index deletion high risk?
6. How can a stable total ingest rate hide a fault?
7. Why is role access additive?
8. How do authentication and authorization differ?
9. What should an SSO rollback retain?
10. Why should default configuration files not be edited?
11. How can effective configuration be inspected on a managed forwarder?
12. When is search-time transformation preferable?
13. How do universal and heavy forwarders differ?
14. Why is a successful network connection insufficient validation?
15. What does Deployment Server distribute?
16. What makes a deployment canary useful?
17. How does monitor differ from batch?
18. What risks arise from recursive/overlapping monitor stanzas?
19. How do TCP and UDP reliability differ?
20. What must a scripted input protect?
21. Name three Windows input types.
22. What should a HEC token restrict?
23. Why are retries and acknowledgments not the same as exactly-once delivery?
24. What does explicit sourcetype selection control?
25. What happens when character encoding is wrong?
26. What does line breaking decide?
27. Which timestamp boundaries require tests?
28. What evidence should Data Preview validate?
29. How do props.conf and transforms.conf relate?
30. What does SEDCMD change?
31. Why is masking at search time too late for protected raw data?
32. Where might newer ingest actions fit?
33. What should app compatibility review include?
34. Why can an app require components outside Cloud?
35. When should ACS versus Support be used?
36. What belongs in a support reproduction package?
37. Why must support artifacts be redacted?
38. Which two domains carry 15% each?
39. What credential is prerequisite?
40. What must be rechecked before purchase/change?

## Answer key

1. The service description defines Splunk service operations; customers own source setup, compatible forwarders, connectivity, data/config/identity use, and contacts among other responsibilities.
2. Cloud restricts/manages service infrastructure through supported surfaces.
3. Splunk Web, ACS API/CLI, supported app flows, and Support depending on entitlement/task.
4. Data type, retention, access, search, ownership, and operational organization.
5. Current docs describe it as irreversible data/index removal.
6. One source can stop while another grows.
7. Capabilities/index access from multiple inherited/assigned roles combine.
8. Identity verification versus permitted actions/data.
9. Tested local emergency access, metadata/certificates, ownership, and change reversal.
10. Upgrades overwrite them and effective precedence expects supported local/app layers.
11. With `btool` and configuration-source output where supported.
12. When it meets the need without irreversibly changing stored events or ingest cost.
13. Lightweight forwarding versus a full parsing/routing/input-capable tier.
14. It does not prove authentication, routing, parsing, metadata, indexing, or search correctness.
15. Deployment apps selected by server classes to registered clients.
16. It limits impact while validating configuration and rollback.
17. Monitor follows files/checkpoints; batch consumes/removes files and has different risk.
18. Duplicate ingestion, excess recursion/volume, rotated-file reread, and conflicting settings.
19. TCP is connected/ordered; UDP does not guarantee delivery/order.
20. Privilege, paths, concurrency, time/resources, output stability, checkpoints, and secrets.
21. Event logs, performance counters, registry, AD/WMI/file inputs; any three.
22. Producer/use, source networks, allowed indexes, and least privilege.
23. Failures can occur around acknowledgment boundaries; producers need idempotency/deduplication design.
24. Parsing rules and search-time knowledge applied to that data classification.
25. Bytes decode incorrectly and can corrupt stored text/extractions.
26. Which lines become one event.
27. Missing/malformed, locale/zone, DST, future/past, multiline, and fallback cases.
28. Event count/raw, timestamp/zone, metadata/index, fields, and warnings.
29. Props selects/invokes behavior; transforms defines reusable transformations.
30. Raw text during supported parsing-time processing.
31. Sensitive text is already stored and subject to access/retention.
32. As supported routing/filtering/masking alternatives upstream/in-flight.
33. Cloud/product version, dependencies, publisher, permissions, network/files, configs/indexes, support, upgrade, and rollback.
34. Collection/input pieces may need a forwarder or other customer-managed tier.
35. Use the supported self-service API for compatible operations; Support for required/unsupported service changes.
36. Scope/times, reproduction, expected/actual, impact, recent change, errors, IDs, health/network/config evidence, and contacts.
37. They can expose tokens, credentials, personal data, or proprietary content.
38. Getting Data in Cloud and Monitor Inputs.
39. Splunk Core Certified Power User.
40. Blueprint, service description, tenant experience/entitlement, docs/version, price/delivery, renewal/retake, and support path.

## Final readiness checklist

- [ ] I distinguish Cloud/Splunk/customer responsibilities and tenant-dependent self-service/support paths.
- [ ] I can design, monitor, secure, and safely retire indexes and role access.
- [ ] I understand effective configuration and index-time versus search-time consequences.
- [ ] I can securely onboard/test forwarders and manage a canary deployment-app rollout.
- [ ] I can implement and failure-test monitor, network, script, Windows, and HEC inputs.
- [ ] I can preview and correct boundaries, timestamps/zones, encoding, routing, filtering, and synthetic masking.
- [ ] I can evaluate/install/manage apps only through the supported Cloud path.
- [ ] I can isolate a fault and produce a minimal, redacted, useful Support case.
- [ ] I completed the ten labs without touching real production data or destructive controls.
- [ ] My Power User prerequisite is valid and I rechecked the live exam/service contracts.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick the official administration course or a documentation-led lab as the primary path. Cloud service behavior changes; verify every third-party explanation against the current service description, Admin/ACS manuals, and your tenant.

| Resource | Access | Estimated time | Best use |
|---|---|---:|---|
| [Official Cloud Admin blueprint](https://www.splunk.com/content/dam/splunk2/en_us/pdfs/training/splunk-test-blueprint-cloud-admin.pdf) | Free canonical scope | 1–2 hr mapping/final review | Domains, prerequisite, contract |
| [Official Cloud Admin page](https://www.splunk.com/en_us/training/certification-track/splunk-cloud-certified-admin.html) | Free | 20–40 min before booking | Status, delivery, price, prerequisite |
| [Splunk Cloud Administration](https://www.splunk.com/en_us/training/course-catalog.html) | Paid instructor-led; USD 2,000 in 2024 map, verify current | 18 hr listed plus 15–25 hr lab/review | Net-new admin path |
| [Transitioning to Splunk Cloud](https://www.splunk.com/en_us/training/course-catalog.html) | Paid; for experienced Enterprise admins; price/schedule vary | 9 hr listed in 2024 map plus targeted labs | Responsibility/topology transition path |
| [Current Splunk Cloud service details](https://help.splunk.com/en/splunk-cloud-platform/get-started/service-terms-and-policies/10.5.2605/information-about-the-service/splunk-cloud-platform-service-details) | Free authoritative service boundary | 4–8 hr selected full review | Customer/Splunk responsibility and constraints |
| [Splunk Cloud administration hub](https://help.splunk.com/en/splunk-cloud-platform/administer) | Free | 15–25 hr selected Admin/identity/index/monitoring topics | Current tenant administration |
| [Admin Config Service manual](https://help.splunk.com/en/splunk-cloud-platform/administer/admin-config-service-manual/9.3.2411/welcome-to-the-admin-config-service-acs/about-the-admin-config-service-acs-api) | Free; compatibility/role requirements apply | 4–8 hr plus safe CLI/API lab | Self-service operations versus Support |
| [Splunk Cloud data-ingestion docs](https://help.splunk.com/en/splunk-cloud-platform/get-data-in) | Free | 15–25 hr selected inputs/parsing topics plus lab | Exact ingestion mechanics |
| [Splunk How-To YouTube](https://www.youtube.com/@SplunkHowTo) | Free official videos | 4–8 hr selected admin/ingest videos plus recreation | Visual supplement, version-check required |
| [Splunk Lantern](https://lantern.splunk.com/) | Free use cases | 6–12 hr selected Cloud onboarding/troubleshooting articles | Operational patterns |
| [O'Reilly Splunk Cloud search](https://www.oreilly.com/search/?q=Splunk%20Cloud) | Subscription; version age varies | Select 8–15 hr after publication/version review | Alternate background, never service authority |
| [Udemy Splunk Cloud Admin search](https://www.udemy.com/courses/search/?q=Splunk%20Cloud%20Admin) | Paid marketplace; catalog/version vary | Select 8–15 hr only after blueprint/lab/provenance check | Optional alternate course |

No exact current MeasureUp, Whizlabs, or Pluralsight Cloud Admin practice product was verified. Reject recalled/live/guaranteed-pass questions and any course that treats customer access to the managed service as identical to self-managed Enterprise.
