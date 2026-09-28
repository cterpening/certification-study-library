# Runnable learning labs and validation

These original exercises turn selected guide examples into small, repeatable experiments. They use Python 3.10 or later and the standard library, with synthetic data and no service credentials. Run commands from a clone of this repository. On Windows, an existing project environment can use `.venv\Scripts\python.exe` in place of `python`.

| Guide | Runnable exercise | Local result, September 28, 2026 | Service / independent review |
|---|---|---|---|
| AB-100 | [Service-case release gate](labs/ab-100.md) | 13 tests passed; starter blocked as expected | Not run / pending |

A passing local suite verifies the limited Python contracts described in each lab. Synthetic trace labels are fixtures, not evidence of a vendor service execution. These labs were developed and checked with AI; they do not confer a **Community reviewed** status on any guide.

## Review packet

Each starter directory contains `review-record.json`. Copy it for a real review; leave unknown and unexecuted fields explicit. Keep sensitive tenant identifiers, tokens, personal records, and raw production traces out of published evidence.

1. The learner reads the requirement and writes expected results before inspecting the reference implementation. Record any disagreement with the provided oracle.
2. Run the original suite and the documented failure drills. Record the repository commit, runtime, command, output, and changed files. An expected failure is successful evidence only when the intended assertion fails.
3. A practitioner independently checks the contract, expected results, failure coverage, and explanation. Record their identity, date, findings, corrections, and disposition. An AI rerun is not independent practitioner review.
4. For service validation, record the approved disposable environment and budget, precise product/client/model versions, effective identities and permissions, input dataset version, run IDs, and observed destination state. Follow each lab's service checklist. A local stub result cannot fill these fields.
5. Record cleanup of only the resources created for the lab, any remaining charges or artifacts, and unresolved findings. Publish sanitized evidence and retain sensitive evidence in an appropriate private location.

**Current boundary:** no usable authenticated Azure session was available during this work. A disposable Power Platform/Foundry environment, spending limit, and independent reviewer have not been supplied. GH-300's local fallback has no Copilot session evidence. Live outcomes and human sign-off remain pending; none has been inferred from these local checks.

## What this phase covers

This is a focused validation of selected AB-100, AI-103, and GH-300 exercises, not execution of every cloud, tenant-policy, multimodal, or administration lab in those guides. The separate [source blocker follow-up](research/2026-09-28-microsoft-blocker-followup.md) records unresolved vendor statements. Scheduled source-monitoring changes are a separate discussion.
