# Remaining catalog review — September 17, 2026

Reviewed all seven catalog scopes left unresolved by the [initial audit](2026-09-17-catalog-audit.md).
Public browser rendering recovered the listings; GitHub and Microsoft also expose
the public JSON feeds used by their current websites. No account login was needed.
This completes catalog enumeration for the scopes below, not technical validation
of every exam or production of the missing guides.

## Coverage reconciliation

| Scope | What was checked | Result |
|---|---|---|
| [GitHub](https://learn.github.com/certifications) | Six certifications in the rendered catalog and public website feed | All six reconcile to GH-100/200/300/500/600/900. The two Applied Skills listings are separate credentials, not missing certification families |
| [Microsoft](https://learn.microsoft.com/en-us/credentials/browse/?credential_types=certification) | Browse page reports 74; its current public feed returned all 74 unique results, the same total, and no next page | 60 listings reconcile: 49 Microsoft families, six GitHub, five MOS. The 50 Microsoft guides include separate AZ-800/801 exams for one family. Fourteen remaining listings comprise Educator, seven Office 2019 app credentials, two job-focused Excel credentials, and four aggregate MOS awards |
| [Cisco](https://www.cisco.com/site/us/en/learn/training-certifications/exams/list.html) | Both current-exam tables: 54 career entries and 23 channel/partner/other entries | Career entries include 46 numbered exams and eight labs/practicals. Four match existing guides. These 77 entries are not 77 certification families; shared core/concentration exams and partner tests need separate intake |
| [MongoDB](https://learn.mongodb.com/pages/certification-program) | All four exam families | Three covered; self-managed Database Administrator is missing. Developer programming-language choices do not create additional credential families |
| [ServiceNow](https://learning.servicenow.com/lxp?id=amap_home) | All four role branches: Administrator, Architect, Implementer, Developer | CSA/CAD are covered. Implementer has 34 paths, including 17 explicitly CIS-coded entries; the rest mix suites, accreditations and other routes. Architect lists CMA, CTA and CRM Architect; Developer also lists a Citizen Developer micro path |
| [IBM](https://www.ibm.com/training/search) | Certification filter with retired/withdrawn excluded; 74 returned records match the total displayed by the live search | Six guides match. Records comprise 58 with primary C-series exams, seven S-series specialties and nine combined credentials. Those categories must not be flattened into 68 new standalone exams |
| [OpenAI Academy](https://help.openai.com/en/articles/20001270-openai-academy-courses) | Fresh successful extraction of all 14 courses | Matches the corrected reference. Badges and eligible pathway completion certificates remain distinct from formal OpenAI certification |

Microsoft's feed here is the interface requested by today's Browse Credentials
page. It is neither the deprecated Learn Catalog API nor the authenticated Learn
Platform API. Its schema and pagination are checked before accepting a snapshot.

## Changes needing attention first

| Item | Verified finding | Action |
|---|---|---|
| **PL-400 → AB-400** | AB-400 delivery starts October 16, 2026. PL-400 registration closes October 16; registered candidates may take PL-400 through October 30. The credential family remains Power Platform Developer Associate. The AB-400 blueprint is already public | Added transition notice and lifecycle metadata to the existing guide. Map the replacement blueprint before producing AB-400 coverage. [Credential notice](https://learn.microsoft.com/en-us/credentials/certifications/power-platform-developer-associate/), [AB-400 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-400) |
| **DP-420** | October 6, 2026 objective revision and credential rename to Azure Cosmos DB AI Developer Associate. Exam code stays DP-420; future objectives include AI retrieval and agent memory | Added scheduled-change notice and metadata. Existing guide retains its July baseline; a substantive October revision remains production work. [Credential notice](https://learn.microsoft.com/en-us/credentials/certifications/azure-cosmos-db-developer-specialty/), [future blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-420) |
| **IBM C1000-207** | watsonx Orchestrate AI Engineer v1 — Associate; public exam record reports Live and includes objectives | Missing; prioritize for agentic AI expansion. [Credential](https://www.ibm.com/training/certification/ibm-certified-watsonx-orchestrate-ai-engineer-v1-associate-C9009400), [exam contract](https://www.ibm.com/training/credentials/getExam/C1000-207) |
| **IBM C1000-195** | watsonx Governance Lifecycle Advisor v1 — Associate; public exam record reports Live and includes objectives | Missing; prioritize AI governance coverage. [Credential](https://www.ibm.com/training/certification/ibm-certified-watsonx-governance-lifecycle-advisor-v1-associate-C9008000), [exam contract](https://www.ibm.com/training/credentials/getExam/C1000-195) |
| **MongoDB self-managed DBA** | Public page offers registration and links a study guide; online proctored, 75 questions, 90 minutes | Add a guide candidate distinct from Atlas administration. Detailed blueprint retrieval/mapping remains intake work. [Exam page](https://learn.mongodb.com/pages/mongodb-associate-database-administrator-exam) |
| **MOS MO-220 / MO-230** | Excel for Accounting Associate and Excel for Business Finance Associate each have a scheduling route and public skills outline | Confirmed missing job-specific credentials, already outside the selected MOS wave. [Accounting](https://learn.microsoft.com/en-us/credentials/certifications/mos-excel-for-accounting-associate/), [Business Finance](https://learn.microsoft.com/en-us/credentials/certifications/mos-excel-for-business-finance-associate/) |
| **ServiceNow CIS-DF** | Data Foundations (CMDB and CSDM) path explicitly describes a proctored exam and links registration | Missing; check its full blueprint and current prerequisites during intake. Do not infer eligibility or deadlines from community posts. [Official path](https://learning.servicenow.com/lxp?id=amap_detail&summary_id=79d64e311bfcf01002ed2f89bd4bcb51&achievement_id=0e97835c47ea2e10c00af235126d431b) |

Microsoft's transition pages also say AB-400 registration is available now while
describing October 16 as the exclusive registration switch. Keep registration
availability distinct from the stated delivery start; check the scheduler when
booking. The short AB-400 study-guide redirect failed during research, but the
canonical Learn blueprint above was publicly readable.

Three more missing IBM watsonx exams have public objectives and report Live:
[C1000-177 Data Scientist](https://www.ibm.com/training/certification/ibm-certified-watsonx-data-scientist-associate-C9006400),
[C1000-190 Data Lakehouse Engineer](https://www.ibm.com/training/certification/ibm-certified-watsonx-data-lakehouse-engineer-v1-associate-C9007300),
and [C1000-180 AI Assistant Engineer](https://www.ibm.com/training/certification/ibm-certified-watsonx-ai-assistant-engineer-v1-professional-C9006900).
These are confirmed coverage gaps, not claims that the exams just launched.

Cisco's broader list confirms the previously identified AITECH/DCAI candidates
and exposes existing breadth beyond the four selected guides: CCNA Cybersecurity,
CCST IT Support, Field Technician, professional/expert tracks, Wireless and
AppDynamics. The current-exam table uses current Automation/Cybersecurity names;
older marketing summaries still contain DevNet/CyberOps labels. Use individual
exam pages and the current table to establish identity before adding duplicates.

ServiceNow's **AI System Administrator**, **AI Implementer** and **AI Developer**
headings are role-path labels. They do not establish three new AI exams. Its
implementation paths include CIS-CSM, DF, DISCO, EM, FSM, HAM, HR, ITSM, PA, RC,
SIR, SM, SP, SAM, SPM, TPRM and VR. Public Sector Digital Services appears in two
forms and needs identity/classification review. Older CSA release variants and
suite/micro-credential combinations are preserved as context, not counted as new
mainline certifications.

## Recurring checks and evidence

The follow-up scheduled-style attempt returned **three usable sources, four
manual-review results, and zero errors**. GitHub and Microsoft now have guarded
JSON extraction; OpenAI succeeded on retry. Cisco's source now targets the full
current-exam table, and ServiceNow points to the working credential-path route.
Cisco, MongoDB, ServiceNow and IBM still need a browser for this catalog check.
Their successful manual reviews do not make the unattended HTML extractors pass.
OpenAI can also intermittently return access challenges.

The accepted automatic baseline now contains **37 sources and 766 listing
observations** across the unchanged 41-source configuration. These are overlapping
observations, not distinct certifications. Browser-only evidence is stored
separately and was not inserted into that baseline.

Reconciliation, source methods, normalized listings and capture hashes are in
`ADLC_Docs/operations/2026-09-17-catalog-follow-up.json`. The follow-up fetch results
are in `ADLC_Docs/operations/2026-09-17-catalog-follow-up-automation.json`.
Temporary captures contain the rendered pages/feed responses; the repository
retains listing metadata rather than copies of vendor course or exam materials.
No seed verification date, technical audit date, or historical review hash was
renewed by this catalog review. New guides remain queued for source mapping and
production; schedules activate after merge to the default branch.
