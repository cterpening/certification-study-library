# AZ-900 study conversation — Part 1

> Independent AI-assisted resource — AI-GENERATED DRAFT; HUMAN REVIEW PENDING.

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) is authoritative.

Scope: Three selected governance distinctions: permissions and Policy, management locks and data protection, and tags and cost allocation. This companion does not cover the entire AZ-900 exam. Technical evidence for these distinctions was checked on November 10, 2026; human review and live Azure execution remain pending.

Baseline: Skills measured as of July 20, 2026. Recorded blueprint check: 2026-10-28.

This is a production script, not an assertion that audio has been generated or listened to.

[Companion study guide, practice questions and visual aids](<../../../study-packs/az-900-governance/study-guide.md>)

[Full source study guide](<../../../../guides/AZ-900-microsoft-azure-fundamentals.md>)

## Introduction

**Host:** Welcome to our AZ-900 study conversation, part 1 of 1. This is an independent, AI-assisted study resource with synthetic voices. Human review is pending. The official exam blueprint is authoritative. Our source package uses this baseline: Skills measured as of July 20, 2026. Its recorded blueprint check was 2026-10-28; preparing this episode does not renew that review. Today's scope: Three selected governance distinctions: permissions and Policy, management locks and data protection, and tags and cost allocation. This companion does not cover the entire AZ-900 exam. Technical evidence for these distinctions was checked on November 10, 2026; human review and live Azure execution remain pending.

**Learner:** We will work through the ideas, compare common choices, and pause for recall. The linked guide and show notes contain the sources and visual aids.

## Azure RBAC and Azure Policy answer different questions

**Host:** We will use one imaginary project to connect three ideas: permissions and policy, locks and recovery, and tags and cost. Picture a small team building a document service. These are original learning scenarios, not recalled exam questions.

**Learner:** Engineers need to deploy it, operations wants to avoid accidental deletion, and finance needs to understand the bill. Saying turn on governance is too vague. Each requirement needs a control, and each control needs evidence that it addresses the requirement.

**Host:** Start with the engineer. They can sign in, but their deployment fails. What should we ask before changing their permissions?

**Learner:** Identify the requested action, the target scope, and the failure message. Azure role-based access control, or R-B-A-C, associates a principal with a role at a scope. The question is whether that identity has the required permission there. Successful sign-in alone does not settle it.

**Host:** Now suppose the engineer already has the required deployment permission. Our organization allows resources only in selected locations, and the request chooses another location. An applicable deny policy blocks the deployment. Adding a more powerful role sounds tempting, but it would answer the wrong question.

**Learner:** The deployment must satisfy the applicable policy as well. We should inspect the rule and the requested configuration. We might correct the location, or follow a legitimate exception process if the requirement warrants one. We should not treat an organizational restriction as a reason to give the engineer unnecessarily broad access.

**Host:** Our visual aid is a question map, not a sequence of internal Azure checks. One arrow connects permission questions to role assignments. Another connects governance requirements to policy assignments. Both lead to inspecting the evidence. Other service checks can matter too. Here is a recall check: an existing resource is marked noncompliant. Has Azure necessarily repaired it? Pause and explain your reasoning before continuing.

**Learner:** No. A finding describes a condition; it does not prove a successful repair. Policy effects differ. For supported remediation, an appropriately configured task and authorized managed identity do the work. Check the result. Also avoid memorizing that Policy never examines identity: current capabilities include identity-aware rules. Verify those details in current documentation. Keep the central distinction: permission grants and governance requirements serve different purposes.

## A management lock is not a data-recovery plan

**Host:** Let us move to operations. Our document service now exists, and someone proposes a delete lock on its storage account. They say, that will stop us losing documents. What is missing from that statement?

**Learner:** They have not identified the operation or the thing being protected. Deleting the storage account through the management application programming interface, or A-P-I, differs from deleting a document through the Blob service. A management lock addresses the first boundary. It does not turn all the account's contents into undeletable data.

**Host:** The two familiar lock levels also deserve attention. A cannot-delete lock and a read-only lock are different choices. We should select the restriction that matches the requirement instead of assuming that the strongest-sounding label is automatically the best operational design.

**Learner:** Consider a virtual machine that an authorized operator cannot start. An inherited read-only lock can explain the failure. Starting the virtual machine requires a management operation affected by that lock. Troubleshooting should therefore include the actual operation and parent scopes. Repeatedly changing the operator's role would miss that cause. Check current documentation for the particular operation and service.

**Host:** Return to the document service. An application has permission to delete a blob, and it uses the data API to do so. The account has a delete lock. Does that lock guarantee that the document remains available? Pause here and name the boundary before answering.

**Learner:** It does not. For the recovery part of the design, inspect the data-protection settings. Our selected objective is resource locks; recovery is related learning that explains the limit of that control. We are not claiming that any particular backup, retention, or recovery feature is enabled. Establish what the configured service can restore and under what conditions.

**Host:** Read our visual aid as three separate questions. The management-operation arrow points to the applicable lock. The data-operation arrow points to data authorization. The recovery arrow points to configuration and test evidence. A useful worksheet has two columns: prevention and recovery. In prevention, record the operation and the control intended to restrict it. In recovery, record what can be restored, under which conditions, and what evidence would demonstrate that restoration works.

**Learner:** That worksheet keeps our claims honest. Reading documentation supports an expected result. A completed recovery exercise supplies observed evidence. We have done the reading here, not a live Azure test. Before relying on a design, verify supported features and test the intended recovery path in an appropriate environment.

## Resource tags, cost records, and access are separate

**Host:** Finance now asks for a research cost center on our document service. Someone adds a tag to the resource group and assumes every resource has inherited it. How would you check that assumption?

**Learner:** Inspect the resources themselves. Parent tags do not automatically become child resource tags. A tagging policy or another deliberate process may help apply them. We should establish which process is in use and check its outcome, rather than inferring resource metadata from the resource group's label.

**Host:** Here is the twist: the cost report already shows spending under Research, even though a virtual machine lacks the resource tag. It looks contradictory until we ask which record each screen displays. Pause and decide whether one of those observations must be wrong.

**Learner:** They can both be right. Cost Management tag inheritance can add parent labels to usage records where the feature is enabled and supported. That can explain the financial report without changing the virtual machine. A resource-compliance check and a financial classification check can therefore produce different answers. Verify current billing-scope support before assuming that feature is available.

**Host:** Our diagram follows the record. Resource metadata and supported inheritance feed usage records, and those records feed cost reporting. A separate arrow connects role assignments to resource authorization. There is no automatic parent-tag-to-child-resource arrow, and the cost-center label itself does not grant access. Does that label automatically decide how to divide the bill for a shared service?

**Learner:** No. Cost allocation needs a business rule. Imagine Research directly spends three hundred dollars, Operations spends five hundred, and a shared service costs two hundred. If the teams agree to split that shared amount equally, the allocated totals become four hundred and six hundred dollars.

**Host:** The arithmetic still totals one thousand dollars. The equal split is our invented agreement, not an Azure rule discovered from a tag. A different organization might use measured consumption or another allocation method. The useful lesson is to name the assumption so someone else can understand or challenge the result.

**Learner:** Finish by explaining four sentences in your own words. R-B-A-C grants scoped permissions. Policy applies configured governance requirements. Locks restrict management operations, while recovery needs its own design. Tags organize information, and financial records can differ from resource metadata. Apply those distinctions to the document service and identify the evidence you would inspect. That gives you a practical way to reason through this selected part of Azure governance.

## Next steps

**Learner:** Before moving on, explain the distinctions from this episode without looking at your notes. Use the original practice questions in the study pack to find gaps.

**Host:** Then check the current official sources and complete the relevant hands-on work. This conversation covers selected objectives; listening alone is not evidence of readiness or complete exam coverage.

## Show notes

These registered sources are pinned through the study package's input fingerprints.

- **Azure RBAC and Azure Policy answer different questions** — [What is Azure role-based access control?](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview), [What is Azure Policy?](https://learn.microsoft.com/en-us/azure/governance/policy/overview), [Remediate resources with Azure Policy](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources). Guide sections: Authentication and authorization; Governance controls; Apply governance controls at the correct scope; Worked example 6 — permission, policy, lock and data protection.
- **A management lock is not a data-recovery plan** — [Lock Azure resources to protect infrastructure](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources). Guide sections: Governance controls; Select storage from data shape through recovery; Worked example 6 — permission, policy, lock and data protection; Lab 6: Offline cost and control worksheet.
- **Resource tags, cost records, and access are separate** — [Resource tags and inheritance](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources), [Cost Management tag inheritance](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/enable-tag-inheritance), [What is Azure role-based access control?](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview), [What is Azure Policy?](https://learn.microsoft.com/en-us/azure/governance/policy/overview). Guide sections: Cost management; Budgets, limits, commitments and tags; Governance controls; Worked example 3 — allocate shared cost without changing access.
