---
exam_code: EX294
vendor_id: red-hat
official_blueprint: https://www.redhat.com/en/services/training/ex294-red-hat-certified-engineer-rhce-exam-red-hat-enterprise-linux
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# EX294 Red Hat Certified Advanced System Administrator in Ansible Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ex294-coverage-record). The [official EX294 objectives](https://www.redhat.com/en/services/training/ex294-red-hat-certified-engineer-rhce-exam-red-hat-enterprise-linux) are authoritative.

**Current baseline:** Most-recent-product public EX294 objectives; companion AU294 baseline is RHEL 10, Ansible Core 2.16, and development tools aligned with Ansible Automation Platform 2.5/2.6<br>
**Upcoming blueprint change:** None announced when checked September 1, 2026<br>
**Important version boundary:** Red Hat says multiple exam versions may be purchasable and the public objectives describe the most recent product version. Confirm the exact exam version at checkout and align the course, execution environment, navigator behavior, collections, and RHEL targets to it.<br>
**Naming boundary:** The current credential is **Red Hat Certified Advanced System Administrator in Ansible** and contributes toward Red Hat Certified Engineer/Architect in Ansible. Many courses still use the older RHCE/EX294 label; the live objectives—not the marketing title—define scope.<br>
**Official source:** [Red Hat EX294 exam page](https://www.redhat.com/en/services/training/ex294-red-hat-certified-engineer-rhce-exam-red-hat-enterprise-linux)

## How to use this guide

EX294 is a performance exam in desired-state automation. Red Hat provides multiple systems; you configure Ansible Automation Platform, write playbooks, and automate standard administration. Evaluation applies your playbooks to freshly installed systems and checks the requested end state. A host that you repaired manually is not sufficient if the playbook cannot reproduce that state.

The public page recommends RH124/RH134 or RH199-equivalent administration experience, AU294 or equivalent Ansible experience, and review of EX200 plus EX294 objectives. During the exam there is no internet or personal documentation; for most exams, shipped product documentation is available. Public objectives are unweighted, so do not invent domain percentages.

Use this loop for every exercise:

1. convert prose into inventory scope, inputs, desired state, validation, persistence, and failure behavior;
2. inspect `ansible.cfg`, navigator configuration, inventory, execution environment, collections, credentials, and target facts;
3. choose a purpose-built fully qualified module name and express state idempotently;
4. syntax/lint where available, run narrowly, inspect changed/failed/skipped/handler output, and validate on targets;
5. rerun to prove idempotence, apply to a fresh target, reboot when state must persist, and validate again;
6. commit only nonsecret reproducible content and retain a rollback path.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Official task group | Performance outcome |
|---|---|
| RHCSA capabilities and shell analysis | Understand the target state well enough to automate and troubleshoot it. |
| Core Ansible components | Use inventories, modules, variables, facts, loops, conditions, plays, failure control, configs and roles. |
| Configure Ansible and managed nodes | Establish configuration, inventory, SSH, escalation and file deployment correctly. |
| Run playbooks and development workflow | Use `ansible-playbook`, navigator, execution environments, Git and VS Code workflows. |
| Create plays and playbooks | Express a specified state with modules, registered data, conditionals and error handling. |
| Roles and Content Collections | Build, install and consume reusable namespaced automation. |
| Automate RHCSA tasks | Manage packages, repositories, services, firewall, storage, files, archives, schedules, security, users and groups. |
| Manage content | Render templates and protect sensitive variables with Vault. |

## 1. RHCSA capability is the automation substrate

You must recognize correct end state for tools, running systems, storage, filesystems, services, users/groups, and security. If you cannot diagnose an `fstab`, systemd, firewalld, permission, SELinux, repository, or LVM failure manually, you cannot reliably design or verify automation for it. Review the [EX200 guide](EX200-red-hat-certified-system-administrator.md) and perform those tasks on RHEL 10.

Analyze simple shell scripts: inputs, quoting, exit codes, conditionals, loops, side effects and error handling. Prefer Ansible modules over shell/command, but understand a supplied script before executing it and accurately define `changed_when`, `failed_when`, idempotence and security when no module fits.

**Related item:** Automation multiplies both correct intent and mistakes. Inventory scoping, `--limit`, check/diff previews where supported, backups, serial rollout and verification are blast-radius controls.

## 2. Core Ansible components

### Inventory, configuration, plays, modules and data

Inventory defines managed hosts and groups plus variables, but group hierarchy and variable precedence can change the effective value. Be able to render/inspect inventory and host variables rather than reading one file in isolation. Separate environment data from reusable logic and never store plaintext secrets in Git.

An `ansible.cfg` selection depends on location/environment; know which configuration is active and inspect it. Configure inventory, remote user, privilege escalation, host-key behavior, roles/collections paths and execution behavior deliberately. `ansible-navigator.yml` controls navigator mode, execution environment, artifacts, inventory and other settings for the current product workflow.

A play maps hosts to ordered tasks with variables, privilege and handlers. Modules implement desired actions. Use fully qualified collection names when ambiguity or portability matters. Facts describe targets; registered variables capture a task result; magic variables describe Ansible execution context. Understand when facts are gathered and when a value is undefined.

Loops apply a task to items; `when` controls execution per host/item; handlers run when notified by a changed task and normally at play boundaries; blocks group tasks and support `rescue`/`always`. A handler is not a substitute for explicit validation, and `ignore_errors` is rarely correct error design.

**Related item:** YAML parses values before Ansible evaluates Jinja. Indentation, scalar types, quoting and templating boundaries can produce syntactically valid but semantically wrong automation.

## 3. Configure control and managed nodes

Create static INI or YAML inventory with meaningful groups. Validate with inventory graph/list/host views and an ad hoc reachability test. Configure SSH keys and target accounts, verify host keys and permissions, and establish privilege escalation with least privilege. Diagnose unreachable versus failed: DNS/route/SSH/auth/Python is different from a module or sudo failure.

Deploy files using `copy`, `template`, `file`, `fetch`, `synchronize` only where appropriate, and manage owner/group/mode/SELinux context/backup/content source. Avoid manual preconfiguration that the playbook does not encode, because fresh targets will not contain it.

Use separate control/development dependencies from managed-node requirements. An execution environment container supplies `ansible-core`, collections and Python dependencies consistently. Inspect image/content versions and do not assume the local host's installed collection is available inside the execution environment.

## 4. Run and develop playbooks

Use both `ansible-playbook` and `ansible-navigator` as listed in the objective. Know inventory selection, playbook path, variables, tags, limit, verbosity, check/diff mode, syntax validation and result interpretation. `ansible-navigator` can browse documentation/content, inspect inventory/environment and run within an execution environment. Practice its text/stdout interaction without internet.

Use VS Code to create YAML, configure navigator, run through a development container/execution environment, and work with Git. The objective names basic Git: clone a repository, add files, commit logically, inspect status/diff/log and push playbooks. Keep Vault passwords, private keys, generated artifacts and credentials out of the repository with appropriate ignore and secret handling.

**Related item:** Check mode is a prediction implemented by modules, not proof of final state; some modules do not fully support it. Validate actual application on disposable targets.

## 5. Create resilient plays and playbooks

Express desired state with modules rather than a chain of imperative shell commands. Set `state`, `enabled`, source/destination, ownership, type, mount state, policy and other parameters explicitly. A second clean run should report no changes unless the requirement is inherently dynamic.

Use variables at the correct scope and precedence; use defaults for roles, inventory data for environment, Vault for secrets and `set_fact` only when computed runtime state is intended. Register command/module results and test documented fields. Use facts and filters to make platform-aware decisions without hiding invalid assumptions.

Conditionals should test exact supported data. Loops should use readable item structures and labels. Notify handlers only when a service-relevant resource changes. Use `block`/`rescue`/`always`, `failed_when`, `changed_when`, assertions and explicit validation to distinguish expected state from concealed failure. Do not blanket-ignore errors.

Troubleshoot in layers: YAML parse → inventory/variable rendering → collection/module resolution → execution environment dependency → connection/escalation → module arguments → target policy/state → handler/validation. Increase verbosity purposefully and inspect the first causal failure.

## 6. Roles and Content Collections

A role packages tasks, handlers, defaults, variables, templates, files, metadata and dependencies under a predictable interface. Create a standard skeleton, put overridable inputs in defaults, reserve vars for stronger internal values, qualify modules, notify role handlers, and keep the role idempotent and independently testable.

Install and use roles from the provided source and record dependencies. A Content Collection is a namespace/package containing roles, modules, plugins and documentation. Install the required version into the configured collections path or execution environment and use its FQCN. Use `requirements.yml` or the specified dependency declaration so fresh environments can reproduce content.

**Related item:** “Works on my control node” usually means an undeclared collection, Python dependency, path or version. Recreate the controller/execution environment from declared inputs and test on fresh hosts.

## 7. Automate standard RHEL administration

Build a module-to-outcome map and verify each on RHEL 10:

- packages/repositories: repository trust/availability, package present/absent/latest only when requested, transaction evidence;
- services: unit enabled and started/stopped, handler on configuration change, post-start validation;
- firewalld: correct zone/source/interface/service/port, runtime and permanent state, reload and peer test;
- storage/filesystems: device facts, partition/LVM/filesystem/mount/swap layers, stable identifiers, nondestructive change and reboot validation;
- files/content/archives: owner/group/mode/context, correct source, atomic/template/backup decisions and extracted final structure;
- schedules: user, command/path/environment, calendar, enablement and observed run;
- security: SSH, SELinux contexts/ports/booleans, default permissions and minimum access;
- users/groups: UID/GID, home/shell, memberships without accidental replacement, password/aging and scoped privilege.

Use purpose-built modules and current collection documentation. Apply storage and security automation first to disposable targets. `lineinfile` is not a universal template engine; a template is preferable when the whole file is owned by automation, while targeted modules are preferable when the service has a structured interface.

## 8. Templates and Vault

Jinja templates should render deterministic configuration from explicit inputs. Use conditionals/loops/filters sparingly, validate required variables with assertions, quote/escape for the target format, set owner/group/mode/context, notify a handler, and validate syntax before or during replacement where the module supports it. Inspect rendered output for each inventory class.

Ansible Vault encrypts data at rest in files/variables; it does not prevent a playbook from logging, writing or exposing decrypted values. Use Vault IDs/password sources according to the provided environment, `no_log` for sensitive task output when appropriate, restrictive target permissions, and no plaintext secret in Git/history/artifacts. Test rekey/edit/view/encrypt/decrypt workflows only with lab values.

**Related item:** `no_log` reduces output exposure but makes troubleshooting harder and does not sanitize the target system or external service logs. Design secret flow end to end.

## Integrated scenarios

### Scenario 1: Reproducible web role

Build inventory groups for staging/production, a role that installs the package/repository, templates configuration, creates content/ownership/context, opens the correct firewall service, enables/starts the unit and validates the listener/HTTP outcome. Use group variables, a handler, assertions and a serial/canary rollout. Run twice, apply to fresh hosts, reboot and revalidate.

### Scenario 2: Storage and identity rollout

Automate a group, users, SSH keys, sudo rule, GPT/LVM/filesystem/mount and scheduled maintenance across selected nodes. Derive device/size data from explicit inventory inputs and facts, assert safe preconditions, avoid overwriting existing data, persist by stable identifier, validate permissions/SELinux, rerun idempotently, reboot and confirm every host.

### Scenario 3: Broken automation pipeline

A Git-cloned play works locally but fails in navigator. Trace active config, inventory, execution-environment image, collection path/version, variables/Vault ID, SSH/escalation, module resolution and target policy. Correct declared dependencies rather than modifying the container interactively. Prove the fix from a clean clone, fresh target and second no-change run.

## Hands-on labs

Use disposable RHEL 10 control/managed VMs and only harmless lab secrets.

1. **Controller contract:** create `ansible.cfg`, `ansible-navigator.yml`, static grouped inventory, SSH and escalation; inspect effective configuration/inventory and diagnose one unreachable and one privilege failure.
2. **Data/control flow:** build a play using facts, inventory variables, registered output, loops, conditions, handlers, assertions and a block/rescue; predict per-host results before running.
3. **Git/development environment:** clone/init, create playbooks in VS Code, use navigator execution environment, commit nonsecret content, reconstruct from clean clone and prove dependency completeness.
4. **Reusable role:** create a configurable service role with defaults/tasks/templates/handlers/meta, install a required collection, validate, rerun idempotently and consume from two plays.
5. **RHEL admin matrix:** automate packages, service, firewall, file/template/archive, schedule and users/groups across two nodes; verify target state with both Ansible and native commands.
6. **Safe storage:** automate a disposable disk through partition/LVM/filesystem/mount/swap with assertions, stable persistence and reboot verification; fail safely on an unexpected existing signature.
7. **SELinux and Vault:** manage a nonstandard service port/context/boolean where required, encrypt a lab secret, prevent log/repository leakage and validate policy after reboot.
8. **Timed fresh-host assessment:** randomly select public objectives, build/apply playbooks to clean nodes, reserve validation time, rerun for zero unintended change, reboot and score only requested end state.

## Original knowledge checks

1. Why can a manually corrected target still fail EX294 evaluation?
2. What proves a playbook is reproducible on fresh systems?
3. Why is RHCSA-level diagnosis still essential?
4. How do inventory and effective host variables differ?
5. Which `ansible.cfg` is active and how would you prove it?
6. How do facts, registered values and magic variables differ?
7. When does a handler run, and what can delay it?
8. Why is `ignore_errors` usually weaker than explicit failure design?
9. How do unreachable and failed results differ?
10. What belongs in an execution environment?
11. Why can a locally installed collection be invisible to navigator?
12. What does check mode not prove?
13. Which Git content must never include a Vault password or private key?
14. Why use an FQCN?
15. How does an idempotent second run behave?
16. When is a command task justified, and what must define change/failure?
17. How do role defaults and vars differ?
18. What makes a role interface reusable?
19. How do roles and collections differ?
20. Why pin or declare content dependencies?
21. Which controls limit automation blast radius?
22. Why validate a rendered template before service restart?
23. When is `lineinfile` weaker than a template or purpose-built module?
24. What storage preconditions should be asserted before partitioning?
25. Which layers must be verified after LVM/filesystem extension?
26. How do firewalld runtime and permanent state affect automation?
27. What must persist after a reboot?
28. How can adding a group accidentally remove other memberships?
29. Why is a running service insufficient validation?
30. How do SELinux file context, port label and boolean differ?
31. What does Vault protect, and what does it not protect?
32. Why can `no_log` still be insufficient secret protection?
33. How should a task use registered command output safely?
34. What is the purpose of `block`, `rescue` and `always`?
35. How would you prove a scheduled task actually ran?
36. Why reserve time for a second run and fresh-target validation?
37. Which layer should be inspected first after a YAML syntax error?
38. Which layer is likely when navigator cannot find a module that the host CLI finds?
39. What current product/version facts must be checked at purchase?
40. Which gaps make an older RHCE/EX294 resource incomplete for the current page?

## Version and older-course checklist

Before relying on RHEL 8/9 or pre-AAP-2.5 material, confirm coverage for the purchasable version and the live objectives:

- `ansible.cfg` and `ansible-navigator.yml` configuration;
- both `ansible-playbook` and `ansible-navigator`, including content discovery, inventory and execution environment;
- VS Code and Ansible development-container workflow;
- Git clone/add/commit/push workflow without secrets;
- roles plus namespaced/versioned Content Collections and declared dependencies;
- current RHEL 10 administration behavior and supported modules;
- fresh-system evaluation, idempotence, persistence and reboot validation;
- AU294's current RHEL 10, Ansible Core 2.16 and AAP 2.5/2.6 alignment—without assuming that course labels alone identify the exact purchased exam version.

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. Choose one current version-aligned course, use official docs for exact modules and navigator behavior, and spend most preparation time building repeatable playbooks against fresh RHEL 10 hosts.

| Resource | Access | Estimated time |
|---|---|---:|
| EX294 objectives, EX200 refresh, AAP/RHEL docs | Public | 12–25 selected hours |
| Red Hat AU294 | Paid/RHLS | About 4–5 instructor-led days plus labs |
| Red Hat AU094 Ansible Basics | Public/free offering varies | 3–6 hours orientation estimated |
| Udemy / Imran Afzal EX294 | Paid | 7 hours 48 minutes video plus 30–60 hours labs |
| O'Reilly / Sander van Vugt RHCE 8 book | Paid/book | 516 pages / 12 hours 59 minutes; concepts only, substantial current gaps |
| Ansible upstream documentation | Public | 12–25 hours selected module/playbook practice |

- **Official route:** [Red Hat AU294](https://www.redhat.com/en/services/training/au294-red-hat-linux-automation-with-ansible) is the current companion course, based on RHEL 10, Ansible Core 2.16 and tooling aligned with AAP 2.5/2.6. Allow **4–5 instructor-led days plus substantial lab repetition**; verify delivery length and selected exam version.
- **Official orientation:** [AU094 Ansible Basics](https://www.redhat.com/en/services/training/au094-ansible-essentials-simplicity-automation-technical-overview) can establish vocabulary (**3–6 hours estimated**), but is not EX294 preparation by itself.
- **Current product reference:** [AAP 2.6 documentation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6) and [Ansible community documentation](https://docs.ansible.com/ansible/latest/) provide current navigator, execution-environment, collection, playbook and module detail (**12–25 selected hours**).
- **Commercial video:** [Udemy / Imran Afzal Linux Red Hat Certified Engineer EX294](https://www.udemy.com/course/linux-red-hat-certified-engineer-rhce-ex294/) is **7 hours 48 minutes**, 72 lectures, updated June 2026. Map navigator/development-container/Git/current-AAP objectives explicitly before using it as the main route.
- **Hands-on practice:** [Udemy / Ghada Atef RHEL 10 EX294 practice](https://www.udemy.com/course/rhce-ex294-practice-exams-master-ansible-automation/) lists six current RHEL 10 scenarios/sets and was updated July 2026. Use only as a prompt to build original fresh-host labs; its page mixes claims beyond the exact public objectives, so do not treat it as scope authority.
- **Older detailed reference:** [O'Reilly/Pearson Red Hat RHCE 8 EX294 Cert Guide](https://www.oreilly.com/library/view/red-hat-rhce/9780136872481/) is **516 pages / 12 hours 59 minutes**, October 2020. It remains useful for roles, variables and RHEL automation but predates navigator, execution environments, VS Code development containers, Git and current RHEL 10/AAP; close all gaps above.

No exact current EX294 Pluralsight, Whizlabs, MeasureUp, KodeKloud, or RHEL-10/AAP-2.6 O'Reilly end-to-end product was independently verified September 1. Avoid multiple-choice “exam simulation” as primary preparation for a fresh-system performance assessment. Plan **100–180 hours** after solid RHCSA skills, or **220–350 hours** if Linux administration and automation are both new.

---

## Source map and freshness notes

The live EX294 page defines public tasks and says they represent the most recent product version; the purchase flow defines which versions are actually available. AU294 supplies the current public training baseline, and AAP/RHEL/upstream Ansible documentation supplies technical behavior.

- **VERIFY CURRENT:** purchasable exam version, RHEL/AAP/ansible-core/navigator/execution-environment/collection versions, delivery rules, objective text, module behavior, course duration/access and credential naming.
- **Stable performance pattern:** declare dependencies → inspect effective inventory/config/data → express desired state → limit/canary → validate → rerun idempotently → fresh target → reboot → validate again.
- **Older RHCE material:** retain as conceptual support only after closing every navigator, execution-environment, VS Code/Git, collection and RHEL 10 gap.

This guide uses no recalled exam tasks or restricted course content. Its scenarios, labs and checks are original transformations of public objectives.
