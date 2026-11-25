# Microsoft certification refresh, group 3

Checked November 20, 2026. [Scope and results](2026-11-20-microsoft-refresh.md)

## AZ-104

[Study guide](../../guides/AZ-104-microsoft-azure-administrator.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104)

Credential: Microsoft Certified: Azure Administrator Associate. The public credential links to exam scheduling.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-104/)

**Product documentation.** For an application running on a VM that reads an SMB Azure file share, identify the VM's managed identity and authorize it to the share. The same storage account can support end-user identities. The two principals authenticate independently, so success as one does not validate the other's permissions.

[Use Managed Identities with Azure Files | Microsoft Learn](https://learn.microsoft.com/en-us/azure/storage/files/files-managed-identities)

Check supported client versions and the required storage account configuration before a lab. A share was not mounted.

**Lab 02b - Manage Governance via Azure Policy.** The lab covers resource-group tagging and the effects of assigning Azure Policy to an environment. About 30 minutes for the exercise (publisher estimate); provisioning or setup can add time. Execution requires suitable Azure permissions. Policy evaluation can be asynchronous, and its timing is separate from the lab estimate. [Publisher resource](https://microsoftlearning.github.io/AZ-104-MicrosoftAzureAdministrator/Instructions/Labs/LAB_02b-Manage_Governance_via_Azure_Policy.html)

Current official rendering labels both sections as of/prior to October 26, 2023; article edited October 30, 2026. Accepted outline dated April 17, 2026. Same five domain weights.

Configure soft delete for blobs and containers is explicit only in April. The current rendering retains Azure Files snapshot/soft delete. April names encryption at host for VMs. The 2023 rendering names Azure Disk Encryption. Five wording-only changes: Azure Files/Azure Storage for file shares, Azure Blob Storage/Blob Storage for containers, Azure Container Registry/registry capitalization, user-defined routes/network routes, Connection monitor/Monitor.

## AZ-120

[Study guide](../../guides/AZ-120-planning-administering-azure-sap-workloads.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-120)

Credential: Microsoft Certified: Azure for SAP Workloads Specialty. The public credential links to exam scheduling.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/azure-for-sap-workloads-specialty/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-120/)

**Product documentation.** If a design uses SAP Landscape Management to relocate or clone an SAP system on Azure, verify that the estate runs LaMa Enterprise Edition. The connector supplies the VM and managed disk operations used in that workflow.

[Set up the SAP LaMa connector for Azure | Microsoft Learn](https://learn.microsoft.com/en-us/azure/sap/workloads/lama-installation)

The connector documentation identifies the Enterprise Edition dependency. It does not establish a customer's SAP entitlement or current SAP lifecycle support.

**Deploy SAP Deployment Automation Framework for enterprise scale.** The enterprise-scale SAP deployment automation guide separates management and workload zones and lists deployment prerequisites. About 25–40 minutes to diagram the zones and their dependencies before deployment (editorial estimate). This is a planning reading route; deployment needs a suitable subscription, permissions, networking and SAP-specific inputs. An isolated wait step is not the tutorial runtime. [Publisher resource](https://learn.microsoft.com/en-us/azure/sap/automation/tutorial)

## AZ-140

[Study guide](../../guides/AZ-140-configuring-operating-azure-virtual-desktop.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-140)

Credential: Microsoft Certified: Azure Virtual Desktop Specialty. The public credential links to exam scheduling.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/azure-virtual-desktop-specialty/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-140/)

**Product documentation.** To restrict clipboard or redirected drives by session trust, map a Conditional Access authentication context to the redirection. Microsoft's Azure Virtual Desktop guidance also covers RemoteApp sessions and lists printers and USB among the supported redirections.

[Configure context-based redirection | Microsoft Learn](https://learn.microsoft.com/en-us/windows-365/enterprise/context-based-redirections?tabs=windows-365)

Use the Azure Virtual Desktop instructions in the product selector. A Windows 365 policy example does not establish the exact AVD configuration.

**Lab - Implement monitoring by using Azure Virtual Desktop Insights.** The lab uses an existing Azure Virtual Desktop environment, prerequisite labs and Azure Virtual Desktop Insights to examine monitoring data. About 25 minutes for the exercise (publisher estimate); provisioning or setup can add time. The 25-minute estimate assumes the lab dependencies are present. It excludes creation of the environment and data ingestion delays. [Publisher resource](https://microsoftlearning.github.io/AZ-140-Configuring-and-Operating-Microsoft-Azure-Virtual-Desktop/Instructions/Labs_EntraID/03_LAB_41_01_Implement_monitoring_by_using_Azure_Virtual_Desktop_Insights.html)

## AZ-305

[Study guide](../../guides/AZ-305-designing-microsoft-azure-infrastructure-solutions.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305)

Credential: Microsoft Certified: Azure Solutions Architect Expert. The credential expressly requires Azure Administrator Associate plus the expert exam.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-305/)

**Product documentation.** When planning a cache migration, capture the legacy tier first. Microsoft publishes March 31, 2027 for Enterprise and Enterprise Flash and September 30, 2028 for Basic, Standard, and Premium. Size the destination and test the client's cluster behavior before assigning a cutover window.

[Frequently asked questions (FAQ) on the retirement of Azure Cache for Redis - Azure Cache for Redis | Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/retirement-faq)

The service retirement deadline is distinct from reservation end dates. No workload sizing or failover was executed.

**Architecture strategies for performing failure mode analysis.** The Azure Well-Architected guidance decomposes a workload, identifies dependencies and failure points, and relates mitigation to detection. About 25–40 minutes to read the method and draft a failure-mode worksheet for one critical flow (editorial estimate). The reading describes an analysis method. Actual resilience requires tests against the particular architecture. [Publisher resource](https://learn.microsoft.com/en-us/azure/well-architected/reliability/failure-mode-analysis)

## AZ-400

[Study guide](../../guides/AZ-400-designing-implementing-microsoft-devops-solutions.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400)

Credential: Microsoft Certified: DevOps Engineer Expert. Retirement lists and AZ-401 launch announce exam and credential retirement February 1, 2027. The earned-credential prerequisite is still one of Azure Administrator Associate or Azure Developer Associate. Azure Developer Associate retired July 31. AZ-401 is a separate beta expert credential.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/devops-engineer/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-400/) · [Microsoft notice](https://techcommunity.microsoft.com/blog/skills-hub-blog/new-microsoft-certified-agentic-devops-engineer-expert/4528356) · [Microsoft notice](https://learn.microsoft.com/en-us/partner-center/announcements/2026-july) · [Publisher evidence](https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams)

**Product documentation.** For a pipeline that must block publication when tests fail or when the runner emits no results, make both outcomes explicit. PublishTestResults@2 has separate failTaskOnFailedTests and failTaskOnMissingResultsFile inputs and both default to false.

[PublishTestResults@2 - Publish Test Results v2 task | Microsoft Learn](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/publish-test-results-v2?view=azure-pipelines)

This is the contract for version 2 of the task. An earlier test runner or surrounding job can independently fail the build.

**Create your first pipeline.** The tutorial offers language-specific routes for creating and reviewing a first Azure Pipeline. About 20–40 minutes for one language-specific example and a pipeline run review, excluding queue and environment setup (editorial estimate). Execution needs a suitable organization/project, repository access and an available agent or parallel-job entitlement. [Publisher resource](https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline?view=azure-devops)

## AZ-401

[Study guide](../../guides/AZ-401-designing-implementing-microsoft-agentic-devops-solutions.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401)

Credential: Microsoft Certified: Agentic DevOps Engineer Expert (beta). The credential and precise exam page both label it beta. Microsoft launch announcement explicitly requires passing AZ-401 plus GH-300 or AZ-104. AZ-400 retires February 1, 2027; December is a GA target.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/agentic-devops-engineer-expert/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-401/) · [Microsoft notice](https://techcommunity.microsoft.com/blog/skills-hub-blog/new-microsoft-certified-agentic-devops-engineer-expert/4528356)

**Product documentation.** An SRE agent's review mode asks for approval for Azure infrastructure changes. For an external action such as posting to Teams, assess tool access policies or hooks separately. Check the managed identity's permissions before assuming an approved change can execute.

[Run Modes in Azure SRE Agent | Microsoft Learn](https://learn.microsoft.com/en-us/azure/sre-agent/run-modes)

Review mode has a documented action boundary. A live response plan and tenant permissions were not exercised.

**Introduction to agentic DevOps using Microsoft tools on Azure.** Seven units introduce the role of AI agents in Microsoft’s agentic DevOps workflow, including tool and platform choices. 47 minutes for the module (publisher estimate, 7 Units). This is an introductory module. Reading the overview does not exercise an installed agent or validate permissions in an organization. [Publisher resource](https://learn.microsoft.com/en-us/training/modules/introduction-agentic-devops-microsoft-tools-azure/)

Initial collector candidate incorrectly stops at 'Configure collaboration and communication' because the next objective contains 'change logs'. The corrected extractor locates the actual study-resources heading. All 76 tasks in all five domains appear verbatim in the hand-captured accepted snapshot in the same order. October 13 is the article date; skills are undated.

Manual provenance fields, closing notes and physical line breaks differ from a normalized collector snapshot. There is no material teaching-scope change.

## AZ-700

[Study guide](../../guides/AZ-700-designing-implementing-azure-networking-solutions.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-700)

Credential: Microsoft Certified: Azure Network Engineer Associate. The public credential links to exam scheduling.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/azure-network-engineer-associate/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-700/)

**Product documentation.** Application Gateway v1 reached retirement April 28, 2026. For a surviving legacy deployment, treat migration to v2 as a service-continuity task and verify traffic on the replacement before removing an old route.

[Application Gateway V1 retirement and migration to V2 - Azure Application Gateway | Microsoft Learn](https://learn.microsoft.com/en-us/azure/application-gateway/v1-retirement)

A listed v1 resource does not establish a support agreement or confirm continued traffic. No live migration was performed.

**M01 - Unit 6 Configure DNS settings in Azure.** The lab creates a private DNS zone and a virtual-network link for auto-registration, then tests name resolution. About 25 minutes for the exercise (publisher estimate); provisioning or setup can add time. The published lab time excludes provisioning dependencies or troubleshooting an existing DNS setup. No Azure resources were created. [Publisher resource](https://microsoftlearning.github.io/AZ-700-Designing-and-Implementing-Microsoft-Azure-Networking-Solutions/Instructions/Exercises/M01-Unit%206%20Configure%20DNS%20settings%20in%20Azure.html)

## AZ-800

[Study guide](../../guides/AZ-800-administering-windows-server-hybrid-core-infrastructure.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-800)

Credential: Microsoft Certified: Windows Server Administrator Associate. Exact retired exam route and official retired list show September 30, 2026. Renamed credential continues through AZ-802.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-hybrid-administrator/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-800/) · [Microsoft notice](https://techcommunity.microsoft.com/blog/skills-hub-blog/microsoft-credentials-roundup-june-2026/4528350) · [Publisher evidence](https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams)

**Product documentation.** Historical Windows Server note. On covered Windows Server 2025 devices with Credential Guard disabled and BlockNtlmv1SSO unset, the October 13, 2026 security update changed the implicit NTLMv1-derived SSO behavior from Audit to Enforce. Scope any legacy dependency review to that configuration.

[Manage NTLMv1 changes and prevent network authentication issues in Windows | Microsoft Support](https://support.microsoft.com/en-us/servicing/os/windows/docs/2025/08/upcoming-changes-to-ntlmv1-in-windows-11-version-24h2-and-windows-server-2025)

Archived exam. Use as dated product context only. The article does not apply the change to every Windows Server release or every NTLM use.

**Administer Windows Server.** Microsoft’s Administer Windows Server course targets Windows Server administration and the successor training route. 5 days of instructor-led training (publisher listing); provider scheduling and fees vary. The course is a successor resource. Its duration and syllabus do not describe the retired or retiring AZ-800 course or prove booking availability. [Publisher resource](https://learn.microsoft.com/en-us/training/courses/az-802t00)

**Resource follow-up.** The catalog entry `az-ssh-direct-centos-stream9-hv-sock-package` returned this result: 404 confirmed on version-pinned third-party rpmfind package. [Available publisher resource](https://mirror.stream.centos.org/9-stream/BaseOS/x86_64/os/repodata/repomd.xml)

**Resource follow-up.** The catalog entry `az-ssh-direct-ubuntu-vsock-regression` returned this result: same URL recovered on retry, redirects to canonical public bug, HTTP 200. [Available publisher resource](https://bugs.launchpad.net/bugs/2110468)

## AZ-801

[Study guide](../../guides/AZ-801-configuring-windows-server-hybrid-advanced-services.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-801)

Credential: Microsoft Certified: Windows Server Administrator Associate. Exact retired exam route and official retired list show September 30, 2026. Renamed credential continues through AZ-802.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-hybrid-administrator/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-801/) · [Microsoft notice](https://techcommunity.microsoft.com/blog/skills-hub-blog/microsoft-credentials-roundup-june-2026/4528350) · [Publisher evidence](https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams)

**Product documentation.** Historical monitoring note. Microsoft schedules VM Insights Map and its Dependency Agent to retire June 30, 2028. Identify process and connection visualizations that rely on that agent separately from the rest of VM monitoring.

[VM Insights Map and Dependency Agent retirement guidance - Azure Monitor | Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-monitor/vm/vminsights-maps-retirement)

Archived exam. This is a specific component retirement and does not retire Azure Monitor VM insights as a whole.

**Tutorial: Set up disaster recovery for Azure VMs.** The Site Recovery tutorial covers checking settings and permissions, preparing Azure VMs and enabling replication to another region. About 25–45 minutes to identify source, target and verification steps without enabling replication (editorial estimate). This retained scenario is useful for hybrid-server study and current practice; read the current support matrix before a live test, and keep successor exam scope separate. [Publisher resource](https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-tutorial-enable-replication)

## AZ-802

[Study guide](../../guides/AZ-802-administering-windows-server.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-802)

Credential: Microsoft Certified: Windows Server Administrator Associate. AZ-802 is the single new exam for Windows Server Administrator Associate. The old AZ-800/801 pair retired September 30, 2026.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-administrator-associate/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-802/) · [Microsoft notice](https://techcommunity.microsoft.com/blog/skills-hub-blog/microsoft-credentials-roundup-june-2026/4528350)

**Product documentation.** For an isolated Hyper-V guest, distinguish a host-to-guest socket from a connection through the guest's IP network. Hyper-V sockets provide a local host-to-VM communication path without depending on the guest's virtual network.

[Make your own integration services | Microsoft Learn](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/make-integration-service)

A transport capability does not establish that a guest service or a specific administration tool is enabled. No VM connection was performed.

**Lab: Monitoring and troubleshooting Windows Server.** Lab 08 establishes a Performance Monitor baseline and diagnoses a performance problem using captured data. About 40 minutes for the exercise (publisher estimate); provisioning or setup can add time. The published 40 minutes assumes its Windows Server lab environment. Data availability and setup can take additional time. [Publisher resource](https://microsoftlearning.github.io/AZ-802-Windows-Server-Administrator-Associate/Instructions/Labs/LAB_08_Monitoring_and_troubleshooting_Windows_Server.html)

**Resource follow-up.** The catalog entry `az-ssh-direct-centos-stream9-hv-sock-package` returned this result: 404 confirmed on version-pinned third-party rpmfind package. [Available publisher resource](https://mirror.stream.centos.org/9-stream/BaseOS/x86_64/os/repodata/repomd.xml)

**Resource follow-up.** The catalog entry `az-ssh-direct-ubuntu-vsock-regression` returned this result: same URL recovered on retry, redirects to canonical public bug, HTTP 200. [Available publisher resource](https://bugs.launchpad.net/bugs/2110468)

## AZ-900

[Study guide](../../guides/AZ-900-microsoft-azure-fundamentals.md) · [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900)

Credential: Microsoft Certified: Azure Fundamentals. The public credential links to exam scheduling.

[Credential](https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/) · [Exam route](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-900/)

**Product documentation.** For a service with variable eligible usage, model the savings plan hour by hour. Eligible usage draws down the hourly commitment, excess usage is charged at the applicable pay-as-you-go rate, and unused commitment expires at the end of the hour.

[What are savings plans? - Microsoft Cost Management | Microsoft Learn](https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/savings-plan-overview)

Coverage depends on eligible usage, scope and benefit ordering. A savings plan changes billing, not service capacity.

**Describe cost optimization options in Azure.** The unit distinguishes reservations, savings plans and Spot pricing and ends with a decision guide. 4 minutes for the unit (publisher page). This four-minute unit supports a conceptual distinction; actual discounts, availability and commitments require current pricing terms. [Publisher resource](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/7a-describe-cost-optimization-options)
