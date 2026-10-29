# Non-Microsoft certification refresh — group 3

**Completed:** 2026-10-28  
**Guides:** 10 (IBM and Oracle)  
**Selection:** Third group from the frozen 167-guide eligibility queue, ordered by last source-validation date, vendor ID, and exam code.  
**Independent review:** Fresh-context rubric 2; 10 pass, 0 findings.  
**Source health:** 57 scoped source records checked; 57 OK, 0 blocked, 0 broken.  

## Changes applied

- Refreshed IBM's QRadar, Db2, watsonx.ai, Guardium, and AI Associate guides with current release/product context and relevant learning routes.
- Added the IBM QRadar UP16 maintenance note, keeping it separate from exam scope and preserving upgrade/version constraints. Added Db2 13 FL509 context with APPLCOMPAT/tool compatibility caveats; Guardium 12.2.4 as a dated release example; and watsonx.governance/AI learning paths as supporting examples.
- Added the QRadar QNI-versus-QIF distinction and Basic, Enriched, and Advanced QNI inspection levels, backed by IBM documentation.
- Refreshed five OCI guides with current documentation, release examples, and task-specific learning resources. Added Japan-only `-JPN` routes as distinct language options with the contracts published on Oracle Japan’s current exam list.
- Clarified that custom images, scaling, DNS, load balancing, and troubleshooting in the OCI Operations guide are derived practice examples, not separately enumerated Oracle objectives.
- Added 34 IBM/Oracle sources to the catalog, plus three primary IBM sources for the QRadar material. The timed-out Oracle Data Safe LiveLabs candidate was excluded after two retries.

## Verification and limits

Repository validation passed, the strict MkDocs build passed, and generated-site validation passed. The objective monitor surfaced title and extraction-boilerplate changes in Oracle learning-path output and a trailing-space change for C1000-185; no objective/status snapshot changes were accepted. Seven guides were current on source freshness and three IBM exam-detail checks were blocked because the dynamic `getExam` pages were not readable. IBM credential/catalog evidence confirms identity; existing accepted contracts and snapshots remain with visible access caveats.

Source freshness recorded 25 applied findings and 3 blocked findings across ten guides; 0 review-required findings. Course interiors and product labs were not executed. The AI review was fresh-context but not human review. Oracle MyLearn direct-reader output was blank; accepted snapshots and same-day source-validation receipts anchor the English scope. Oracle -JPN contracts remain separate from the English routes.

## Research and audit evidence

The full role research and audit are included below.


---

## Exam, credential, and lifecycle research

# Group 3 exam and lifecycle research

**Reviewed:** 2026-10-28  
**Scope:** IBM C1000-175, C1000-184, C1000-185, C1000-197, C1000-206; Oracle 1Z0-1067-26, 1Z0-1072-26, 1Z0-1084-26, 1Z0-1085-26, 1Z0-1104-26.  
**Role boundary:** official credential, exam, and lifecycle research only; no repository files were edited.

## Summary

- All five IBM guides have active credential records on IBM Training's live certification catalog/pages available through web indexing. Direct `getExam` URLs for C1000-175/184/185/197/206 did not open in the public reader, so contract claims below distinguish readable official credential pages from inaccessible exam-detail routes.
- IBM’s readable exam pages show C1000-175, C1000-185 and C1000-206 as **Live**, with contract and weighted objectives. I found no retirement/replacement announcement for the five in the official pages reviewed. For C1000-184, IBM's public catalog and IBM-issued Credly badge identify the current credential and exam pairing; direct contract page was inaccessible. For C1000-197, the IBM catalog lists the v12.x credential; the direct exam page could not be retrieved.
- Oracle’s official Japan announcement dated **2026-09-04** began offering Japanese-language versions for all five Oracle exams in this batch, and the current official Japanese exam list still lists them. These are distinct `-JPN` codes; this is a useful language/scheduling route update, not evidence that English blueprint scope changed.
- No confirmed objective-map change for any guide. Current group-specific technical or objective changes require the technical researcher’s corroboration and snapshot comparison.

## IBM exams

| Exam | Official evidence opened | Current status / contract evidence | Recommendation and confidence |
|---|---|---|---|
| **C1000-175** QRadar SIEM V7.5 Associate | [IBM credential page](https://www.ibm.com/training/certification/ibm-certified-associate-security-qradar-siem-v75-C9006200); configured [exam record](https://www.ibm.com/training/credentials/getExam/C1000-175) was not accessible in public reader | IBM credential page names C1000-175 and states this is on-premises QRadar only, not QRadar on Cloud. Current guide contract is 62 questions, 41 to pass, 90 min. IBM page's full objective panel was not exposed by search extract; its competency list covers SIEM concepts, architecture, UI, extensions, flows, rules/building blocks, offenses, AQL/search, assets, dashboards/reporting, events, tuning/errors, and roles. No retirement/replacement signal on credential page. | Keep explicit QRadar on Cloud exclusion and V7.5 boundary. Keep contract only after the routine direct-page/source scan confirms the guide's current figures. No objective edit suggested from this evidence. **Medium** (official credential page; exam-detail URL inaccessible). |
| **C1000-184** Db2 13 for z/OS DBA Associate | [IBM catalog search result](https://www.ibm.com/training/search?mktgCategory=Data%2C+Analytics%2C%2C+and+AI&query=Db2&trainingType=Certification); [IBM-issued Credly badge](https://www.credly.com/org/ibm-professional-certification-program/badge/ibm-certified-db2-13-for-z-os-database-administrato.1); configured [exam record](https://www.ibm.com/training/credentials/getExam/C1000-184) inaccessible | IBM catalog search lists the Associate credential (asset `PWID-C9006800`) alongside the separate Db2 13 Professional and Db2 v12.1 Professional credentials. The IBM-issued badge describes the Associate as an entry-level Db2 13 for z/OS DBA and identifies C1000-184 as its criterion. Existing accepted objective snapshot/guide state: 60 questions, 44 to pass, 90 min; seven weighted domains (Planning 12%, Operations 20%, Security 5%, Database Design 20%, Application Development 21%, Data Concurrency 12%, Performance 10%). | Preserve separation from Db2 v12.1 and Db2 13 Professional. Existing exact objective baseline looks internally coherent; I could not verify the exam contract on a live IBM exam-detail page this pass. No retirement notice found in the reviewed catalog. **Medium-low** for unchanged exam contract; **high** for credential/exam identity. |
| **C1000-185** watsonx Generative AI Engineer Associate | [IBM credential/exam page](https://www.ibm.com/training/certification/ibm-certified-watsonx-generative-ai-engineer-associate-C9007000); configured [exam record](https://www.ibm.com/training/credentials/getExam/C1000-185) inaccessible | Page explicitly says credential and exam status **Live**, exam C1000-185, 62 questions, 44 required, 90 min. Six current weighted sections: Analyze/Design GenAI Solution 15%; Prompt Engineering 16%; Fine-Tuning 31%; RAG 17%; Deployment 13%; Integration with Model Orchestration 8%. IBM's description recommends six–twelve months hands-on experience and notes Python/data analysis/data science skills. It lists the follow-on learning path **IBM Certified watsonx Generative AI Engineer v1.1 - Associate**, whereas the live exam title remains “v1 - Associate”; do not infer an exam revision solely from path title. No replacement notice shown. | Keep exam v1 and its published weights separate from the v1.1 learning-path label; consider a small note that IBM's linked preparation path is v1.1 while exam page/contract is v1. Add only if useful and clearly not blueprint revision. **High**. |
| **C1000-197** Guardium Data Protection v12.x Administrator Professional | [IBM certification catalog](https://www.ibm.com/training/credentials/certifications); [IBM Training Guardium catalog search](https://www.ibm.com/training/search?query=Guardium); configured [exam record](https://www.ibm.com/training/credentials/getExam/C1000-197) inaccessible | IBM catalog identifies the current Guardium v12.x Administrator Professional credential (asset `PWID-C9008300`); IBM Training search also lists related current Guardium training. A prep-session listing in IBM MediaCenter exists but is promotional learning context, not a blueprint source. Existing guide/snapshot states 60 questions, 41 required, 90 min, eight weighted groups. I did not find a readable current first-party exam-detail page or retirement/replacement statement in the returned official sources. | Keep published baseline pending coordinator’s direct-source check. Do not use third-party dumps/practice-syllabus pages found during search; several are unauthorized recalled-question marketing and not evidence. **Medium-low** for unchanged contract, **medium** current credential presence. |
| **C1000-206** Artificial Intelligence Fundamentals v1 Associate | [IBM credential/exam page](https://www.ibm.com/training/certification/ibm-certified-artificial-intelligence-v1-associate-C9008700); configured [exam record](https://www.ibm.com/training/credentials/getExam/C1000-206) inaccessible | Page explicitly lists credential/exam status **Live**, exam C1000-206, 44 questions, 31 required, 60 min. Five weighted groups: AI Foundations 25%; Machine Learning and Deep Learning Fundamentals 23%; Generative AI and Applied AI Concepts 23%; Responsible AI, Ethics, Security, and Governance 16%; AI Use Case Implementation and Business Integration 13%. Its official resources include “Introduction to Artificial Intelligence,” described as a broad beginner course with hands-on labs/project, but that’s a learning resource rather than a blueprint change. No replacement signal shown. | Existing exam map/contract matches the current official page. No objective change suggested. **High**. |

IBM policy pages confirm exam registration is through Pearson VUE and delivery modes vary by exam/country; candidates should use the exam's current booking page for available modes. [IBM credentials FAQ](https://www.ibm.com/training/credentials/faq). This is a generic policy and does not establish a particular exam's mode.

## Oracle exams

The principal new official evidence is Oracle University's [2026 Cloud Japanese-exam launch notice](https://www.oracle.com/jp/education/news/). The page dates the notice **2026-09-04**, says Japanese versions began that day, and names each code and title below. The [current Japanese exam list](https://www.oracle.com/jp/education/certification/certification-exam-list/) lists all target `-JPN` codes and exam contract details. The list is Japan-specific and its duration/count/pass figures must not be presented as the English exam contract without direct English evidence.

| Guide exam | Japanese code and official title | Current Japanese-list contract | Recommendation and confidence |
|---|---|---|---|
| **1Z0-1067-26** OCI Cloud Ops Professional | 1Z0-1067-26-JPN, Oracle Cloud Infrastructure Cloud Ops Professional | 90 min / 50 questions / 68% | Add the Japanese exam code and localized availability path as a clearly labeled alternative. Do not replace English contract or objective status. **High**. |
| **1Z0-1072-26** OCI Architect Associate | 1Z0-1072-26-JPN, Oracle Cloud Infrastructure Architect Associate | 90 min / 50 / 68%; list marks it free in Japan | Same language-route note. Price is regional and date-sensitive; don't extrapolate it beyond Japan. **High**. |
| **1Z0-1084-26** OCI Developer Professional | 1Z0-1084-26-JPN, Oracle Cloud Infrastructure Developer Professional | 90 min / 50 / 68% | Same language-route note. **High**. |
| **1Z0-1085-26** OCI Foundations Associate | 1Z0-1085-26-JPN, Oracle Cloud Infrastructure Foundations Associate | 60 min / 40 / 65%; list marks it free in Japan | Same language-route note; keep English and JPN test-mode wording separate. The JPN list does not specify proctor mode. **High**. |
| **1Z0-1104-26** OCI Security Professional | 1Z0-1104-26-JPN, Oracle Cloud Infrastructure Security Professional | 90 min / 50 / 68% | Same language-route note. **High**. |

The notice is a launch/availability update only; it does not say the English exams were retired or their objectives changed. Exact current English contract/details were not exposed in the public MyLearn HTML extractor (the learning paths returned zero text lines), so preserve existing guide boundary that Oracle's public path exposes capabilities without inferred weights/question counts/pass scores unless another direct contract source is available.

## Exact opened URLs and source match notes

- IBM readable official pages: `https://www.ibm.com/training/certification/ibm-certified-associate-security-qradar-siem-v75-C9006200`; `https://www.ibm.com/training/certification/ibm-certified-watsonx-generative-ai-engineer-associate-C9007000`; `https://www.ibm.com/training/certification/ibm-certified-artificial-intelligence-v1-associate-C9008700`; `https://www.ibm.com/training/credentials/certifications`; `https://www.ibm.com/training/search?query=Guardium`; `https://www.ibm.com/training/search?mktgCategory=Data%2C+Analytics%2C+and+AI&query=Db2&trainingType=Certification`; `https://www.credly.com/org/ibm-professional-certification-program/badge/ibm-certified-db2-13-for-z-os-database-administrato.1`; `https://www.ibm.com/training/credentials/faq`; `https://www.ibm.com/training/terms`.
- IBM configured exam-detail pages are registered in `data/sources.json` as `c1000-175-blueprint`, `c1000-184-blueprint`, `c1000-185-blueprint`, `c1000-197-blueprint`, and `c1000-206-blueprint`, all `https://www.ibm.com/training/credentials/getExam/<code>`. Direct `open` was inaccessible for these dynamic routes. C1000-175/185/206 exam data was nevertheless visible on their first-party credential pages; C1000-184/197 contract data remains unconfirmed from first-party pages in this pass.
- Oracle official pages: `https://www.oracle.com/jp/education/news/` (dated 2026-09-04 launch notice; relevant lines 110–125); `https://www.oracle.com/jp/education/certification/certification-exam-list/` (current language-specific exam table); and public MyLearn paths already registered in `data/sources.json`: `https://mylearn.oracle.com/ou/learning-path/become-an-oci-cloud-operations-professional-2026/163390`; `https://mylearn.oracle.com/ou/learning-path/become-an-oci-architect-associate-2026/162234`; `https://mylearn.oracle.com/ou/learning-path/become-an-oci-developer-professional-2026/162926`; `https://mylearn.oracle.com/ou/learning-path/-become-an-oci-foundations-associate-2026/163541`; `https://mylearn.oracle.com/ou/learning-path/become-a-cloud-security-professional-2026/163254`. The MyLearn browser extraction returned no lines; the Japanese official list and news page were readable.

## Bounded recommendations to coordinator

1. Add/approve the Oracle Japan news and Japanese exam-list pages as official sources for the five Oracle guides. Include each corresponding `-JPN` code and Japan-scoped contract in its option/availability note; do not overwrite English exam details or imply scope/weights changed.
2. Keep IBM C1000-175, C1000-185 and C1000-206 objective maps/contracts aligned with their direct IBM credential pages. Verify final page content and source health with the repo's normal source workflow.
3. Flag the exact IBM `getExam` URLs' reader limitation for C1000-184 and C1000-197 as a source-access boundary. Do not infer a contract change from third-party prep material. Existing guide-contract numbers are present in accepted snapshots, but need current first-party revalidation before stating that they changed or remain current.
4. The C1000-185 linked `v1.1` learning path beside the current `v1` exam page is a minor naming discontinuity worth surfacing as a bounded note only if the current course source confirms it.

---

## Technical and release research

# Group 3 technical and release research

**Checked:** 2026-10-28 UTC / public web research  
**Scope:** C1000-175, C1000-184, C1000-185, C1000-197, C1000-206, 1Z0-1067-26, 1Z0-1072-26, 1Z0-1084-26, 1Z0-1085-26, 1Z0-1104-26.  
**Role:** read-only technical research; proposed changes for the coordinator, not guide edits.  
**Source rule:** vendor product docs/releases for technical behavior. Exam scope remains governed by the exact exam record/learning path.

## Findings with useful current technical additions

### C1000-175 — IBM QRadar SIEM 7.5

- IBM published QRadar 7.5.0 Update Package 16 on September 1, 2026. It is a cumulative maintenance release and the accompanying security bulletin recommends applying UP16 for systems through 7.5.0 UP15 IF06. The support note documents that UP16 cannot directly upgrade to the 7.6.0 stream; IBM says that path will be available in a later release. Sources: [UP16 technical note](https://www.ibm.com/support/pages/node/7283630), [IBM security bulletin](https://www.ibm.com/support/pages/node/7286010), [QRadar Software 101 release table](https://www.ibm.com/community/101/qradar/software/).
- **Recommendation:** Add a small dated “current release example — verify before operating” note to the operations/configuration portion or learning resources, explaining that 7.5 UP16 is the current maintenance example checked here and that upgrade paths are release-specific. Do not make UP16 an exam objective or tell learners to upgrade production systems as a lab. The existing guide teaches the 7.5 baseline and authorized lab boundary; those remain appropriate.
- **Confidence:** high. IBM support release note and bulletin are official. The QRadar community/software release table is an IBM-owned index but its page was not fully machine-readable in browser open.

### C1000-184 — Db2 13 for z/OS

- Db2 13 function level 509 (PH70028, April 2026) adds catalog/directory conversion to UTS, IPv4/IPv6 subnet wildcard and local-thread filtering in RLF, online ownership transfer for selected application objects, utility-history SHRLEVEL recording, STMT_HASHID2 catalog columns, synchronous-read I/O counters in real-time statistics, and reduced false page P-lock contention for certain data-sharing page sets. Source: [Db2 13 FL509 technical detail](https://www.ibm.com/docs/en/db2-for-zos/13.0.0?topic=levels-function-level-509); [IBM Db2 tools compatibility matrix](https://www.ibm.com/support/pages/node/6583559).
- IBM's Db2 13 model distinguishes code, catalog, activated function, and application-compatibility levels. Applying PTFs alone is not equivalent to activating a function level; SQL changes generally depend on APPLCOMPAT. The guide already teaches that distinction and version-specific change control.
- **Recommendation:** Add a short current example under Planning/Performance or Places to learn naming FL509 and one or two relevant DBA changes (e.g. utility SHRLEVEL history/RTS I/O counters); label the April 2026 date and say to inspect installed code/catalog/function/APPLCOMPAT levels and IBM/third-party tool compatibility before adoption. Avoid implying every Db2 13 subsystem has activated FL509.
- **Confidence:** high. The IBM Docs page returned 403 on direct open, but indexed IBM Docs text and IBM Support compatibility data agreed on FL509 and its date. Full APAR implementation details should be re-opened in an IBM-readable client before teaching them procedurally.

### C1000-185 — IBM watsonx Generative AI Engineer

- IBM's October 14, 2026 watsonx.governance update expands AI asset discovery to Google Cloud Gemini agents and knowledge bases, and introduces rule-based automated handling for discoveries beginning with watsonx Orchestrate and IBM Bob. It also describes IBM Bob IDE integration that scans agent-related file saves/turns to discover metadata (agent name, tools, MCP servers) and surfaces governance risk findings to developers. Source: [IBM watsonx.governance announcement, October 14](https://www.ibm.com/new/announcements/new-in-ibm-watsonx-governance-govern-ai-agents-as-you-build-expand-accountability-and-streamline-compliance).
- Official watsonx.ai docs clarify that visual Prompt Lab/Agent Lab complex RAG or agent workflows deploy as AI services, with deployment notebooks/online endpoints; saved prompt templates are not the deployment asset for complex RAG applications. Prompt Lab requires a project associated with watsonx.ai Runtime and Admin/Editor permissions to execute prompts. Sources: [Deploying AI services with visual tools](https://www.ibm.com/docs/en/watsonx/saas?topic=services-deploying-ai-visual-tools), [Prompt Lab](https://www.ibm.com/docs/en/watsonx/saas?topic=prompts-prompt-lab), [Deploying generative AI assets](https://www.ibm.com/docs/en/watsonx/saas?topic=assets-deploying-generative-ai).
- **Recommendation:** Add the Oct 14 governance announcement as an optional current product example beneath the guide's design/orchestration discussion, bounded as a watsonx.governance capability rather than a universal GenAI pattern or exam requirement. Add the official deployment/permission distinction beside deployment guidance if the guide explicitly names Prompt Lab/Agent Lab. Preserve IAM, data-entitlement and access-controlled retrieval cautions; a governance scan does not itself prove an agent is safe.
- **Confidence:** high for announcement facts; medium for detailed docs because IBM Docs returned 403 on direct open, though search extraction included the cited page contents.

### C1000-197 — IBM Guardium Data Protection v12.x

- Current IBM release evidence exposes Guardium Data Protection 12.2.4 with GPU 12.0p7240. **Important patch caveat:** p7240 replaces 12.0p240, which IBM initially released on September 30; customers already on p240 are instructed not to install p7240 and should instead install p1064. The 12.2.4 upgrade also requires the latest health-check patch and may restart appliances. Recent 12.2.3 evidence maps to GPU 12.0p230 and documents supported platforms, component patches, deprecated universal-connector combinations and 11.4/11.5 lifecycle transitions. Guardium 12.2.4 changes include Active Threat Analytics UI improvements, parallel query for newly created/cloned reports in select domains, audit workflow UI, mTLS SIEM forwarding, and other operations additions. Sources: [Guardium 12.2.4 announcement/release](https://www.ibm.com/support/pages/node/7288587), [Guardium release information](https://www.ibm.com/docs/en/gdp/12.x?topic=overview-release-information), [Guardium 12.2.3 technical release details](https://www.ibm.com/support/pages/node/7277083).
- IBM's 12.2.x landing index lists point releases, while the exam/guide baseline remains product 12.x. Avoid swapping this into a narrow version claim without checking the current C1000-197 exam record.
- **Recommendation:** Add a dated “product release watch” note near reports/alerts or health/maintenance with one or two 12.2.4 examples and a clear warning that availability depends on installed release, component patch and platform; check component-specific release notes before configuration. Keep it as current product depth outside exam baseline. Do not teach a patch-specific procedure from the announcement alone.
- **Confidence:** medium-high. IBM Support's exact 12.2.4 release record appeared in search results. Opened 12.2.3 and 12.x documentation supports patch/version granularity; coordinator should re-open/inspect exact 12.2.4 details before promoting it.

### C1000-206 — IBM Artificial Intelligence Fundamentals v1

- The same official IBM Oct 14 watsonx.governance update offers a concrete, current responsible-AI/governance case: discover agents, tools, models, MCP servers and knowledge bases; apply organization-defined rule checks; surface metadata and risk findings to developers. Source: [IBM watsonx.governance announcement, October 14](https://www.ibm.com/new/announcements/new-in-ibm-watsonx-governance-govern-ai-agents-as-you-build-expand-accountability-and-streamline-compliance).
- **Recommendation:** Add a brief optional IBM example to Responsible AI/governance: inventory and governance can include agents, tool references, MCP servers and knowledge sources, with developer-time checks. Explicitly separate product example from general AI principles; source announcement is not evidence that the feature is in every plan or required by C1000-206. The guide's existing general AI explanation need not be restructured.
- **Confidence:** high for the announced feature; medium on learner-access/entitlements because the announcement does not state commercial plan prerequisites.

### 1Z0-1067-26 — OCI Cloud Operations Professional; 1Z0-1072-26 — OCI Architect Associate

- OCI's official 90-day release index is current as of October 28 and is useful for ongoing operations review: [OCI Release Notes](https://docs.oracle.com/en-us/iaas/releasenotes/index.htm). It shows, among many unrelated releases, current 1.36.4 support in OKE (October 1) and multiple service changes. It is a discovery page, not an exam map.
- OKE's version matrix currently lists 1.36.4 GA (October 1) and 1.37.0 preview (October 8, OC1 only); it explicitly cautions against production use of preview 1.37. For 1.37 it changes default Service `LoadBalancer` shape behavior and requires TLS secrets to share the service namespace; those constraints are actionable in architecture/operations labs. Source: [OKE supported versions/release calendar and version-specific notes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutk8sversions.htm).
- **Recommendation:** For these broad OCI paths, add only a narrow current-state OKE example if the guide already discusses Kubernetes/load balancers. Distinguish GA 1.36.4 from preview-only 1.37 and date it; avoid presenting the OKE release calendar as the exam's tested version or making it a required objective. For 1Z0-1067, current cost/account/network/DR changes in the general index should be selected only where they map to a specific existing section.
- **Confidence:** high. Oracle OCI docs pages opened and their exact dates/status restrictions are directly exposed.

### 1Z0-1084-26 — OCI Developer Professional

- The guide explicitly covers OKE. The current OKE calendar and compatibility note provide concrete developer-level edge cases: TLS secret namespace enforcement on 1.37, a changed default flexible load-balancer shape/bandwidth on 1.37, preview-only/OC1 limitation, and current GA OKE Kubernetes 1.36.4. Source: [OKE supported versions/release calendar and version-specific notes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutk8sversions.htm).
- OCI's current release notes list an October 21 OKE coordinated GPU maintenance-event repair feature in enhanced clusters. It is specialized, unlikely to add value to this certification study guide unless its OKE node-maintenance section covers managed GPU nodes. Source: [OKE GPU maintenance-event repair](https://docs.oracle.com/en-us/iaas/releasenotes/conteng/conteng_node-maintenance-event-repair.htm).
- **Recommendation:** Prefer the version-specific OKE note and a safe lab check (same-namespace TLS Secret; explicitly set LoadBalancer bandwidth/shape when relying on earlier defaults). Mark 1.37 preview as non-production/limited and verify the live calendar. Do not include GPU host repair unless the current objective map and guide section support it.
- **Confidence:** high for the version matrix and release-note statements.

### 1Z0-1085-26 — OCI Foundations Associate

- The broad Oracle OCI release index exposes a high volume of regional and service-specific announcements; most are too volatile or advanced for this foundations path. The reviewed source set did not reveal a material foundational behavior change that should be promoted to this guide.
- **Recommendation:** Add the canonical Oracle release notes index as an optional “where to verify current service availability” resource only if the guide lacks a current release-discovery route. Do not import individual OKE or AI release details into the fundamentals guide without a clear objective tie.
- **Confidence:** medium; this is a bounded review of current official OCI release notes, not an exhaustive review of every service page.

### 1Z0-1104-26 — OCI Security Professional

- Oracle Data Safe introduced Crypto Posture Assessment on October 20, 2026. The release provides a centralized cryptographic-posture view of registered target databases. Source: [Cryptographic Assessment in Oracle Data Safe](https://docs.oracle.com/en-us/iaas/releasenotes/data-safe/crypto-assessment.htm). The canonical OCI release index also surfaces the date and product.
- **Recommendation:** Add a dated, optional current example to the Data Safe section, bounded to the new crypto-posture assessment for registered target databases. Do not imply that it replaces encryption, key-management, assessment scope or compliance controls, and verify region/target support in the linked Data Safe docs before suggesting a lab.
- **Confidence:** high for announcement scope/date; the linked overview should be inspected before adding procedural steps.

## Other current channel observations and limitations

- IBM QRadar's current UP16 patch/security release is meaningful maintenance currency, but the change does not redefine C1000-175 scope or require new technical explanations in the existing generic guide.
- Db2 FL509 is materially current for a Db2 13 administrator guide. Function level/API compatibility and installed tool support must remain explicit; no activation should be suggested without environment checks.
- Guardium's latest release line has interesting implementation details, but the guide is for 12.x and the exam record must be checked before choosing a product patch baseline. Oracle Data Safe is a separate Oracle product and not part of the Guardium update.
- OCI versions, dates, region eligibility and preview labels change quickly. No claim here changes the exam learning-path scope. In particular, OKE 1.37 is preview only, limited to OC1 and expressly not recommended for production.
- IBM Docs direct opens returned HTTP 403 in the web reader for Db2/watsonx pages. Search results exposed their canonical IBM documentation and substantive extracted text; IBM Support release notes and IBM New announcements were directly open. No learner-account content or product tenant was inspected.
- No lab, tenant or live product execution was performed.

## Exact official URLs reviewed

- https://www.ibm.com/support/pages/node/7283630
- https://www.ibm.com/support/pages/node/7286010
- https://www.ibm.com/community/101/qradar/software/
- https://www.ibm.com/docs/en/db2-for-zos/13.0.0?topic=levels-function-level-509
- https://www.ibm.com/support/pages/node/6583559
- https://www.ibm.com/new/announcements/new-in-ibm-watsonx-governance-govern-ai-agents-as-you-build-expand-accountability-and-streamline-compliance
- https://www.ibm.com/docs/en/watsonx/saas?topic=services-deploying-ai-visual-tools
- https://www.ibm.com/docs/en/watsonx/saas?topic=prompts-prompt-lab
- https://www.ibm.com/docs/en/watsonx/saas?topic=assets-deploying-generative-ai
- https://www.ibm.com/support/pages/node/7288587
- https://www.ibm.com/docs/en/gdp/12.x?topic=overview-release-information
- https://www.ibm.com/support/pages/node/7277083
- https://docs.oracle.com/en-us/iaas/releasenotes/index.htm
- https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutk8sversions.htm
- https://docs.oracle.com/en-us/iaas/releasenotes/conteng/conteng_node-maintenance-event-repair.htm
- https://docs.oracle.com/en-us/iaas/releasenotes/data-safe/crypto-assessment.htm

---

## Learning-resource research

# Group 3 learning-resource research

**Checked:** 2026-10-28 (web research)  
**Scope:** IBM C1000-175, C1000-184, C1000-185, C1000-197, C1000-206; Oracle 1Z0-1067-26, 1Z0-1072-26, 1Z0-1084-26, 1Z0-1085-26, 1Z0-1104-26.  
**Boundary:** This is source discovery, not an exam-content claim. Course pages establish course metadata and the vendor’s described topics, not complete blueprint coverage. I did not complete logged-in course lessons or execute cloud/database labs. No practice-question products were assessed or added.

## Findings and recommendations

| Guide | Exact first-party source | What the opened source supports | Fit, access and bounded recommendation |
|---|---|---|---|
| **C1000-175 QRadar SIEM** | [IBM QRadar SIEM Foundations (BQ105G)](https://www.ibm.com/training/course/ibm-qradar-siem-foundations-BQ105G) | IBM lists a 24-hour (three-day) paid, instructor-led course using QRadar SIEM 7.5. The description covers architecture/data flow, UI, sources/events/flows, rules, assets/apps, offenses, AQL/search, reporting and administration; it says labs are included. | Strong supplement to the existing 7.5 guide and its eight labs. List as paid/instructor-led and version-specific; course description read, labs not inspected. |
| **C1000-175 QRadar SIEM** | [IBM QRadar SIEM Foundation badge requirements](https://www.ibm.com/support/pages/how-can-i-earn-ibm-qradar-siem-foundation-badge-completing-security-learning-academy-course) | IBM support article modified 2026-08-12 says the foundation badge requires 19 free Security Learning Academy courses (13–14 hours combined) and a 63-question, 80% quiz; its stated two-hour estimate applies to the quiz, not the lessons. Focus includes navigating the interface, offenses, events/flows, assets, rules, reports and filters. | Good no-cost alternative. The 19 lesson contents require the IBM Security Learning Academy; I relied on the public IBM article, not the gated course interiors. Don't treat the badge quiz as a C1000-175 sample exam. |
| **C1000-184 Db2 13 for z/OS DBA** | [Db2 13 for z/OS: Introduction to Db2 for z/OS (IBM PDF)](https://www.ibm.com/docs/en/SSEPEK_13.0.0/pdf/db2z_13_introbook.pdf) | IBM PDF last updated 2026-04-10 includes a two-module, step-by-step DB2I/SPUFI tutorial for interactive SQL, creating tables and running utilities through DB2I or JCL. It requires a supported Db2 subsystem, sample tables, an authorized ID, and familiarity with TSO/ISPF. | Specific, free reading/practice material for an existing general documentation link. A z/OS/Db2 environment and credentials are required to execute it; the PDF states no duration, so estimate 2–4 hours for selected modules only if the coordinator wants a time estimate. |
| **C1000-184 Db2 13 for z/OS DBA** | [Db2 13 for z/OS: Introduction to System Administration (CV854G)](https://www.ibm.com/training/course/db2-for-zos-13-introduction-to-system-administration-CV854G); [IBM official current instructor-led listing](https://www.ibm.com/training/guaranteed-to-run-classes) lists **Db2 13 for z/OS Basic Database Administration (CV845G)** | CV854G is an official 24-hour paid course with z/OS lab practice for subsystem start/stop, authorization/RACF, catalog, logs, utilities, monitoring and recovery; prerequisites are about one year of relevant administration experience or equivalent. The IBM upcoming-class listing shows the exact basic DBA course CV845G, three days, with scheduled sessions, but its public listing does not expose the course syllabus. | CV845G is the closer match to this associate DBA exam; recommend linking the IBM catalog search/listing with “search CV845G” and disclosing that the detailed outline was not available from the opened IBM page. CV854G can be optional for the operational subtopics, with its higher prerequisite and 24-hour paid format made clear. Do not link third-party resellers as canonical course authority. |
| **C1000-185 watsonx GenAI Engineer** | [IBM Certified watsonx Generative AI Engineer v1.1 learning path](https://www.ibm.com/training/learning-path/ibm-certified-watsonx-generative-ai-engineer-v11-associate-1054) | IBM labels this path v1.1 and recommends it for building watsonx.ai skills. It includes **watsonx: Technical Essentials (DLP-DL19012G)**, listed as three hours, no-cost, and describes it as product-foundation learning. | Useful orientation/resource entry, but not a claim that the v1.1 path or course equals the v1 exam blueprint. The course listing is public; registration/account may be needed to enroll. Mark as foundation and verify its current release when beginning. |
| **C1000-185 watsonx GenAI Engineer** | [Get started with generative AI assets in watsonx](https://developer.ibm.com/articles/awb-get-started-with-watsonx/) | IBM Developer article groups tutorials for no-code Prompt Lab, Python/Jupyter RAG, no-code model tuning, and an end-to-end use case; each tutorial has instructions/video/resources per the article. | Strong practice supplement for prompting/RAG/tuning. An IBM watsonx account is needed to follow along. This article is older (about 2024); UI, models, service entitlement and workspace steps are volatile. Link as an optional tutorial series and recheck live UI/docs before practice. No course runtime is published; a coordinator estimate of 3–5 hours for selected tutorials is reasonable, not a vendor estimate. |
| **C1000-197 Guardium v12.x** | [Guardium Data Protection Fundamentals (8G103G)](https://www.ibm.com/training/course/guardium-data-protection-fundamentals-8G103G) | IBM currently lists a 24-hour paid instructor-led course based on Guardium 12.1 with hands-on exercises: access/groups, system and data management, backup/restore, discovery/vulnerability assessment, audit process, policies, queries/reports and alerts. | Strong broad match. Add the exact course page; label 12.1 as the course baseline and paid instructor-led access. Course description, not lab execution, was inspected. |
| **C1000-197 Guardium v12.x** | [Guardium Data Protection: Administration (8G920XG)](https://www.ibm.com/training/course/guardium-data-protection-administration-8G920XG) | IBM lists a four-hour paid IBM Intensive Learning course, based on Guardium 12.1, with hands-on exercises for access, groups, system/data-management tools, monitoring and archive/backup/restore. | Concise optional course for administration and backup objectives. Requires general Guardium UI knowledge; course outline only, no lesson completed. |
| **C1000-197 Guardium v12.x** | [IBM Guardium certification prep session](https://mediacenter.ibm.com/media/Certification%2BPrep%2BSession%3A%2BIBM%2BGuardium%2BData%2BProtection%2Bv12.x%2BAdministrator%2BProfessional/1_flq1wrlz/233881112) | IBM describes a focused review of objectives, key concepts and practical preparation for the v12.x Administrator Professional credential. No session length is stated on the accessible page. | Optional orientation before a final source-by-source objective check. Do not count it as technical lab practice or claim its duration. The page metadata was accessible, but playback was not inspected. |
| **C1000-206 AI Fundamentals** | [Artificial Intelligence Fundamentals (IBM SkillsBuild badge)](https://www.ibm.com/training/badge/artificial-intelligence-fundamentals?hss_channel=lcp-78306383) | IBM describes a prescribed SkillsBuild course set covering NLP, vision, ML/deep learning, neural networks, chatbots, AI ethics and applications, plus Watson Studio model-running concepts. The catalog shows constituent modules (typically 3–10 hours each) but not a reliable total for the full prescribed set; the badge page requires an account and completion of courses/quizzes/simulations. | Good broad no-cost foundation, not an exam-specific course. Add beside the general IBM AI article, mark account-required, and do not sum module ranges into a total duration. |
| **C1000-206 AI Fundamentals** | [Get started with artificial intelligence (IBM Developer)](https://developer.ibm.com/learningpaths/get-started-artificial-intelligence/) | IBM Developer gives a beginner 2-hour learning path covering basic AI concepts and building/testing a first Python/scikit-learn ML model. | Useful concrete machine-learning exercise for the ML/implementation domains, but narrower than the responsible-AI/GenAI/business-integration exam. Exact guide path is public; example package versions should be verified before running. |
| **1Z0-1067-26 OCI Operations** | [Monitor applications using OCI APM and OpenTelemetry](https://docs.oracle.com/en/learn/oci-apm-with-opentelemetry/index.html) | Oracle’s tutorial shows instrumenting a non-Oracle stack app and sending traces/metrics to OCI APM and logs to OCI Logging Analytics. Requires OCI tenancy and a Node.js app; example repo named `oci-observability-and-management`. | Adds a practical cross-service observability workflow beyond the guide's broad OCI docs entry. Suggest about 2–4 hours for selected steps (estimate, no publisher duration). Tenant/services may incur cost; verify current prerequisites and clean up. Keep tutorial commands/products version-sensitive. |
| **1Z0-1072-26 OCI Architect Associate** | [Define your network and connectivity architecture](https://docs.oracle.com/en/solutions/oci-best-practices/define-your-network-and-connectivity-architecture1.html) and [OCI workload-networking design playbook](https://docs.oracle.com/en/solutions/oci-best-practices-networking/index.html) | Current Oracle Architecture Center content details redundant FastConnect/VPN designs, non-overlapping CIDRs, VCN sizing, public workload HA, service gateways and hub/spoke transit choices. | Sharpens the existing best-practices/reference-architecture learning source with explicit tradeoffs to apply in the guide’s design exercises. Public reading; no stated runtime. Estimate 1–2 hours for selected design choices; don't treat the Architecture Center as a complete exam course. |
| **1Z0-1084-26 OCI Developer Professional** | [Deploy an application with OCI DevOps CI/CD on Kubernetes](https://docs.oracle.com/en/learn/oci-devops-cicd-on-kubernetes/index.html) | Oracle step-by-step tutorial builds an OCI DevOps project/pipeline and deploys a Node.js app to Kubernetes, using container/artifact registries, notification topic, log group and OKE. | New hands-on supplement for IaC/delivery/build/deploy workflows, not the whole developer blueprint. Requires an OCI tenancy, OKE and registry resources (possible charges); no vendor time estimate. Suggest about 2–4 hours with cleanup. Distinguish from the guide’s broader Functions/streaming/serverless material. |
| **1Z0-1085-26 OCI Foundations** | [Get started with OCI basics](https://docs.oracle.com/en/learn/oci-basics-tutorial/) | Oracle calls out a free Oracle-provided lab and walks through VCN, Linux compute, block volume, remote login, basic web service, termination and reuse of volumes. | Strong beginner lab beyond the guide’s concepts article; estimate 1–2 hours for this single guided task (not publisher-stated). Uses example tenancy values; learners should stay in the assigned lab compartment and terminate resources. A separate personal tenancy may incur charges. |
| **1Z0-1104-26 OCI Security Professional** | [Get Started with Oracle Data Safe Fundamentals (LiveLabs)](https://livelabs.oracle.com/ords/dbpm/r/livelabs/view-workshop?wid=598) | Oracle LiveLabs publishes a two-hour hands-on workshop: register Autonomous Database, security/user assessments, discover/mask sensitive data, audit activity, alerts and SQL Firewall. Familiarity with OCI/IAM/database basics is helpful. | Good optional, scoped practice for existing Data Safe, audit, discovery/masking and SQL Firewall topics. It does not teach the October 2026 Crypto Posture Assessment feature. For that adjacent new capability, pair only with the [current feature overview](https://docs.oracle.com/en-us/iaas/data-safe/doc/crypto-posture-assessment-overview.html): target registration, supported DB versions and IAM prerequisites apply; mark it related/current and do not imply the feature is a published exam objective. No Crypto Posture hands-on LiveLab was found in this search. |

## Search and inspection limits

- IBM’s C1000-184 public credential page was intermittently inaccessible during the parallel exam research. The learning sources above were checked independently from IBM Training/Docs; CV845G surfaced in IBM’s current class listings, but I did not obtain a first-party detailed course syllabus page for it. CV854G, IBM’s PDF tutorial, and course records were directly opened.
- IBM course descriptions and learning-path/catalog metadata were public, but actual paid or account-gated course interiors/labs were not inspected. Candidate should not say the learner completed them.
- Oracle LiveLabs pages and tutorial steps were readable. I did not sign into Oracle or run any lab, and I did not establish billing/credit requirements for a user's own tenancy beyond the page's stated access model.
- No exam dumps, recalled questions or third-party practice-test sources were used. IBM's credential pages expose official assessments/sample tests, but I did not add or inspect them here; they require a separate exam-integrity review under the repository policy.

## Bounded recommendations

1. Add at least one targeted first-party resource to each guide: IBM exact course/training/tutorial material and the Oracle task-specific labs/documentation above.
2. Keep resource access and version notes adjacent to each row; where no runtime is published, mark any coordinator estimate as an estimate rather than vendor-provided duration.
3. Do not change official objective scope or assume every course/lab covers all weighted domains. Keep Db2 and Guardium course-version boundaries visible; use available free learner options where the paid/instructor-led course cost is significant.
4. For Oracle 1Z0-1104-26, put Data Safe Crypto Posture in a clearly labeled related/new-product item and separately cite the current documentation; the release has an implementation prerequisite and is not a reason to rewrite the exam blueprint.

---

## Independent review

# Group 03 independent rubric-2 review

- **Batch:** `nonms-refresh-2026-10-28-group-03`
- **Date:** 2026-10-28
- **Mode:** Read-only, fresh-context AI review. No human review or lab execution is claimed.
- **Evidence:** Complete guides; exact objective/status snapshots; exam rows and certification seeds; latest source-validation receipts; every manifest-registered source and source-health record; relevant current first-party documentation.
- **Binding:** Recomputed every guide SHA-256 using UTF-8 with CRLF/CR normalized to LF; all ten matched the final handoff manifest. Each latest passed receipt's snapshot hash matched the manifest. All registered source-health records were `ok`; receipts report 57/57 scoped sources reachable. Reachability was not treated as claim validation.

## Check key

`OS` official scope; `OC` objective coverage; `MS` material claim support; `EC` exam-contract integrity; `TC` technical coherence; `VL` volatility/lifecycle; `LF` lab safety/feasibility; `RQ` readiness checks; `RE` review-evidence accuracy; `DC` duplication/contamination.

| Exam | OS | OC | MS | EC | TC | VL | LF | RQ | RE | DC | Verdict | Findings |
|---|---|---|---|---|---|---|---|---|---|---|---|---:|
| C1000-175 | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | 0 |
| C1000-184 | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | 0 |
| C1000-185 | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | 0 |
| C1000-197 | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | 0 |
| C1000-206 | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | 0 |
| 1Z0-1067-26 | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | 0 |
| 1Z0-1072-26 | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | 0 |
| 1Z0-1084-26 | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | 0 |
| 1Z0-1085-26 | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | 0 |
| 1Z0-1104-26 | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | Pass | 0 |

## Evidence and access limits

- **IBM exam pages:** C1000-175/184/197 dynamic `getExam` records were not exposed to the direct reader. The guides preserve the accepted contract and status baselines. IBM's current credential pages support identity and published scope; IBM docs support the QNI/QIF distinction and three inspection levels, Db2 FL509 examples, and Guardium release caveats.
- **Oracle MyLearn:** Dynamic pages returned no readable text through the direct reader. Exact accepted MyLearn snapshots and same-day passed receipts were used for English scope and status. Oracle Japan's current exam list and September 4 launch announcement confirm the separate Japan-only `-JPN` codes and localized contracts; the five English guides keep those routes separate.
- **Technical volatility:** Oracle's current OKE calendar confirms Kubernetes 1.37 is preview-only in OC1 and not recommended for production; version-specific LoadBalancer/TLS behavior is presented as dated and non-exam material.
- **Training/labs:** Account-gated IBM lessons and paid course labs were not inspected. No IBM, z/OS or OCI labs were executed. Guide requirements for authorized/nonproduction practice and volatile-product caveats were checked.

## Findings

None open. An earlier read identified a QNI/QIF and inspection-level coverage gap in C1000-175. The guide was repaired before final binding; the full corrected version was re-read and its final hash verified. IBM primary documentation supports the added teaching, so no residual finding remains. The 1Z0-1067-26 guide now explicitly separates derived examples from Oracle's six published capability groups.

## Summary

**10 pass; 0 pass-with-notes; 0 fix-required; 0 blocked; 0 open findings.** This result is fresh-context AI review only; it is not human review, live lab execution, or a guarantee of future product behavior.
