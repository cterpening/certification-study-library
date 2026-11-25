---
exam_code: GH-700
vendor_id: github
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-700
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: ai-generated-draft
last_verified: 2026-11-20
upcoming_change_status: none-announced
upcoming_change_checked: 2026-11-20
---

# GH-700 Agentic AI Business Professional

> **Independent AI-assisted resource.** Beta study guide, checked November 20, 2026. Human review and live GitHub exercises are pending. The [official GH-700 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-700) is authoritative.

GitHub maintains this certification for business professionals who organize work, use Copilot and supervise automated decisions. Microsoft delivers the exam. A useful study project is a weekly delivery brief. It draws on issues and pull requests, drafts a report and gives a named person authority to approve changes before the report reaches its audience. [Credential and intended audience](https://learn.microsoft.com/en-us/credentials/certifications/agentic-ai-business-professional/)

**VERIFY CURRENT.** GitHub lists English, no prerequisites and 90 minutes. Microsoft's scheduling page lists 100 minutes, Pearson VUE and a passing score of 700. Check the duration on your booking confirmation. The October 20 launch notice targets December 2026 for general availability. Both Microsoft sources describe delayed beta results and give different estimates for their release. [GitHub certification details](https://learn.github.com/certification/agenticbusiness) · [Microsoft scheduling details](https://learn.microsoft.com/en-us/credentials/certifications/agentic-ai-business-professional/) · [Beta launch notice](https://techcommunity.microsoft.com/blog/skills-hub-blog/new-github-certified-agentic-ai-business-professional/4564534)

## Objective map

The English study guide shows an October 13, 2026 page update and gives four weighted domains. A separate skills-effective date is unpublished. [Official objectives](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-700)

| Domain | Weight | Artifact to produce |
|---|---:|---|
| GitHub platform features | 20–25% | A project view that connects a business outcome to issues, owners and proposed changes. |
| Productivity with GitHub Copilot | 20–25% | A reusable prompt and a draft that cites the supplied records. |
| Agentic workflows and automations | 25–30% | A workflow design that specifies its trigger, inputs, allowed tools, output and stopping condition. |
| Human oversight | 20–25% | A review decision, a reason for it, and a record of any revisions or escalation. |

> **About related items:** A **Related item:** explains adjacent knowledge that helps you apply the published objectives.

## Organize the work before asking for a summary

Create a small project for a fictional product launch. Make one issue for each deliverable and give it an owner, deadline and status. Link the proposed change to its issue. Configure a board for the delivery team and a table filtered to the coming week for the reviewer. Both views should tell the same story about a blocked item. [GitHub Projects overview](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)

> **Related item:** Ask a colleague with the intended reader's access to open the project view and the issue links in the brief. If they cannot inspect the evidence for a claim, resolve the access question with the record owner before sharing it.

## Get a draft you can check

Give Copilot three fictional issues and ask for one row per issue with its owner, source link, stated risk and next decision. Require it to write *unknown* when a due date is missing. Then supply an issue comment that changes one date. Check whether the model updates the correct row and preserves the other two. Record the model, inputs, output and observed cost so you can compare results when the prompt changes. Check your organization's rules before putting business records into a session. [GitHub Copilot prompt engineering](https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering)

A prompt describes one request. Custom instructions can carry recurring requirements, such as linking each risk to an issue. An agent skill packages instructions and resources for a relevant task. An MCP server can supply an external tool or data source. For this exercise the three issues already supply the evidence. Add an external integration only when you can name the missing information, the permitted access and the reviewer responsible for its use. [Agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) · [Official GH-700 scope](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-700)

## Design the workflow around a decision

Sketch a weekly scheduled workflow that reads project items and produces a draft risk summary. Specify a maximum number of items and one revision attempt. A missing owner goes to the project lead, and conflicting dates go to the issue owner. Use deterministic checks for required fields. Reserve the model for explaining the risk in plain language. GitHub Agentic Workflows use Markdown instructions and GitHub Actions. Their declared *safe outputs* limit which writes a workflow may request. Choose a draft or a reviewable change that fits the business process. **VERIFY CURRENT** for product availability, billing and the organization's allowed tools. [GitHub Agentic Workflows](https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/about-github-agentic-workflows)

## Rehearse the handoffs

| Decision | What to try and what to keep |
|---|---|
| Who owns a change? | Assign the issue, link the pull request and request a review. Record the team convention in a wiki. Check project visibility, branch policy and reviewer permissions before treating a moved project card as approval. |
| Which model and session fit the brief? | Use the same three fictional issues and the same output format in two fresh sessions. Compare source accuracy, omissions, cost and clarity. Resume one session and change a due date. Save the before-and-after output so you can tell changes in the inputs from differences between models. |
| What should a custom agent be able to do? | Draft a repository agent profile for the weekly brief. Give it instructions, an explicit tool list and a requirement to cite every status claim. If a task needs public web research, enable that capability only where supported. Select the agent, inspect its activity and review any proposed change before publishing. [Custom agent configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration) |
| Should the agent use a skill or an MCP tool? | Package the team's brief format as a skill with a description, instructions and a synthetic example. Inspect a third-party skill before installing it. Load the skill and ask for the same brief to test when it is selected. If a milestone lives in a separate tracker, connect an authorized read-only MCP tool and verify the retrieved record against its source. [Adding skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) · [Configuring agents, skills and MCP](https://docs.github.com/en/copilot/how-tos/github-copilot-app/customize-github-copilot-app) |
| When should automation pause? | Use interactive work for a disputed status, planning mode for a proposed sequence, and unattended execution only for approved, bounded work. Set a cost limit and a stop condition. Give one person ownership of escalations. An agent's ability to propose a write does not authorize publication. |
| How do you recover a failed run? | Find the run, job and first failed step. Check whether any output or write already succeeded. Stop a run operating on the wrong inputs. Correct the cause, obtain approval for a retry where needed, then verify the output and any duplicate side effects. Keep the run link with the review decision. [Workflow run logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs) |

## Practice human review

Suppose a draft says a delivery is complete. The linked issue is open and the pull request is awaiting review. Ask for a revision citing both records. If the revised draft still claims completion, stop the run and route the discrepancy to the owner. A second model agreeing with the first draft supplies no new evidence about whether the work shipped.

**Readiness check.** Run the exercise on paper twice, once with read-only access and once with permission to propose a pull request. In each case, identify who can publish the brief, what evidence makes approval reasonable, and what happens if that reviewer is unavailable. Save the inputs, draft, decision and follow-up action so another reviewer can reconstruct the result.

## Key terms and phrases

**Organize the work before asking for a summary**

| Term or phrase | Meaning |
|---|---|
| [Project view](#organize-the-work-before-asking-for-a-summary) | A table, board or other presentation of project items configured for a particular audience or decision. |
| [Issue](#organize-the-work-before-asking-for-a-summary) | A record that tracks a deliverable or problem, its owner and the discussion about its progress. |
| [Pull request](#organize-the-work-before-asking-for-a-summary) | A proposal to merge changes from one branch into another, with a place to discuss and review the differences. |
| [Assignee](#organize-the-work-before-asking-for-a-summary) | The person given responsibility for following up on an issue or completing a tracked task. |
| [Project field](#organize-the-work-before-asking-for-a-summary) | A structured property of a project item, such as its status or due date, used for grouping and filtering work. |
| [Board view](#organize-the-work-before-asking-for-a-summary) | A project layout displaying items in columns, often grouped by their current status. |
| [Table view](#organize-the-work-before-asking-for-a-summary) | A project layout displaying items as rows with selected fields as columns. |
| [Filtered view](#organize-the-work-before-asking-for-a-summary) | A view restricted to matching items, such as open deliverables due this week. |

**Get a draft you can check**

| Term or phrase | Meaning |
|---|---|
| [Prompt](#get-a-draft-you-can-check) | The request and context supplied to the model for a particular task, such as drafting a weekly brief. |
| [Custom instructions](#get-a-draft-you-can-check) | Standing guidance that carries recurring requirements, such as citing each reported risk, across requests. |
| [Agent skill](#get-a-draft-you-can-check) | A reusable bundle of instructions and resources for a particular kind of work. |
| [Model Context Protocol (MCP) server](#get-a-draft-you-can-check) | A service that makes specific tools or data available to an AI client through a common protocol. |
| [Grounding](#get-a-draft-you-can-check) | Supplying relevant source material so the assistant can base its response on inspectable evidence. |
| [Context](#get-a-draft-you-can-check) | The code, conversation and selected supporting material available to the model for the current request. |
| [Token](#get-a-draft-you-can-check) | A unit of model input or output that may represent part of a word, a whole word or another symbol. |
| [Source link](#get-a-draft-you-can-check) | A reference back to the record supporting a claim in a generated brief. |
| [Model choice](#get-a-draft-you-can-check) | The decision about which model to use based on the task's quality, cost and response requirements. |

**Design the workflow around a decision**

| Term or phrase | Meaning |
|---|---|
| [Safe output](#design-the-workflow-around-a-decision) | A declared type of change an agentic workflow is allowed to request, such as opening an issue for review. |
| [Trigger](#design-the-workflow-around-a-decision) | The event or schedule that starts an automated process. |
| [Workflow input](#design-the-workflow-around-a-decision) | Information supplied at the start of a workflow, such as a set of project items to summarize. |
| [Stop condition](#design-the-workflow-around-a-decision) | A stated condition that ends a run, such as a revision limit or unresolved conflict. |
| [Deterministic check](#design-the-workflow-around-a-decision) | A repeatable rule, such as testing whether every item has an owner, that yields the same result for the same inputs. |

**Rehearse the handoffs**

| Term or phrase | Meaning |
|---|---|
| [Custom agent](#rehearse-the-handoffs) | A specialized assistant configuration with instructions and a chosen set of tools. |
| [Plan mode](#rehearse-the-handoffs) | A working mode for analyzing a request and proposing steps before the user authorizes implementation. |
| [Session](#rehearse-the-handoffs) | A particular conversation or work context whose messages and tool activity help interpret later requests. |
| [Job](#rehearse-the-handoffs) | A group of steps assigned to a runner. Dependencies can require another job to finish first. |
| [Step](#rehearse-the-handoffs) | One unit within a job that runs a command or calls a reusable action. |
| [Tool permissions](#rehearse-the-handoffs) | The allowed operations and resources available to an agent when it invokes a tool. |
| [Cost limit](#rehearse-the-handoffs) | A spending boundary used to bound authorized agent activity. |
| [Escalation](#rehearse-the-handoffs) | Routing an unresolved issue or decision to the person with the authority to resolve it. |
| [Retry](#rehearse-the-handoffs) | Another attempt after a failure, made after checking whether the earlier attempt already produced any effects. |
| [Run log](#rehearse-the-handoffs) | The recorded events and outputs used to locate the first failure in a workflow run. |

**Practice human review**

| Term or phrase | Meaning |
|---|---|
| [Human oversight](#practice-human-review) | A person's responsibility to check a proposed result against the original evidence and approve, return or escalate it. |
| [Approval](#practice-human-review) | A named reviewer's decision to authorize a specific proposed action on the evidence available. |
| [Revision request](#practice-human-review) | A review decision that returns a draft for changes and identifies the unsupported or incorrect part. |
| [Read-only access](#practice-human-review) | Permission to inspect records without changing them. |
| [Review evidence](#practice-human-review) | The source records, proposed output and recorded decision that let another person reconstruct the review. |

## Places to learn

This is a starting sequence, not a complete list. Times are editorial estimates for the selected activities. Reading is public. Running Copilot or Actions depends on account access, organizational policy and applicable usage limits.

| Resource | Access | Estimated time |
|---|---|---|
| [GH-700 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-700) | Public outline | 15–25 minutes to map the four domains to the delivery brief. |
| [GitHub Projects overview](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) | Public GitHub Docs | 20–30 minutes to design two views of the same work. |
| [GitHub Agentic Workflows](https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/about-github-agentic-workflows) | Public GitHub Docs | 25–40 minutes to annotate a trigger, permissions, outputs and an approval decision. |
| [Build a repository status report](https://github.github.com/gh-aw/setup/quick-start/) | Public GitHub walkthrough. Execution requires a repository you can configure, Actions, GitHub CLI and access to an AI engine. | GitHub estimates 10 minutes. Allow extra time for account setup and review of the generated report. |
