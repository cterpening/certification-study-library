---
exam_code: EX294
vendor_id: red-hat
official_blueprint: https://www.redhat.com/en/services/training/ex294-red-hat-certified-engineer-rhce-exam-red-hat-enterprise-linux
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# EX294 Red Hat Certified Advanced System Administrator in Ansible Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 28, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ex294-coverage-record). The [official EX294 objectives](https://www.redhat.com/en/services/training/ex294-red-hat-certified-engineer-rhce-exam-red-hat-enterprise-linux) are authoritative.

**Current baseline:** Most-recent-product public EX294 objectives; companion AU294 baseline is RHEL 10, Ansible Core 2.16, and development tools aligned with Ansible Automation Platform 2.6<br>
**Upcoming blueprint change:** None announced when checked September 28, 2026<br>
**Important version boundary:** Red Hat says multiple exam versions may be purchasable and the public objectives describe the most recent product version. Confirm the exact exam version at checkout and align the course, execution environment, navigator behavior, collections, and RHEL targets to it.<br>
**Naming boundary:** The current credential is **Red Hat Certified Advanced System Administrator in Ansible** and contributes toward Red Hat Certified Engineer/Architect in Ansible. Many courses still use the older RHCE/EX294 label; the live objectives—not the marketing title—define scope.<br>
**Official source:** [Red Hat EX294 exam page](https://www.redhat.com/en/services/training/ex294-red-hat-certified-engineer-rhce-exam-red-hat-enterprise-linux)

**CURRENT BLUEPRINT:** The public [version-specific objectives PDF](https://training-lms.redhat.com/public_content/redhat/training/Red%20Hat%20Certification%20Exam%20Objectives%20by%20Version.pdf) contains `EX294V26K`, which matches the current page's 56 tasks in eleven groups. This guide combines related groups into eight teaching sections; Git and VS Code remain explicit objectives. Older PDF versions have different lists.

**VERIFY CURRENT — product versus upstream:** The [AAP lifecycle policy](https://access.redhat.com/support/policy/updates/ansible-automation-platform) identifies core 2.16 as the AAP 2.6 default while also describing other execution-environment streams. A community documentation banner or a newer upstream core release does not by itself determine Red Hat product support or the assigned exam runtime. Record the actual EE image, core/Python versions and installed collections before selecting examples.

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

The [core 2.16 configuration reference](https://docs.ansible.com/projects/ansible-core/2.16/reference_appendices/config.html) selects the first applicable file: `ANSIBLE_CONFIG`, the current directory's `ansible.cfg`, the home configuration, then `/etc/ansible/ansible.cfg`. These files are not merged. A world-writable current directory is not automatically trusted for configuration. Use `ansible --version` and `ansible-config dump --only-changed` inside the actual execution context; repeat inside the EE when that is where the play runs. Configuration-file selection is separate from variable precedence and CLI/environment overrides.

A play maps hosts to ordered tasks with variables, privilege and handlers. Modules implement desired actions. Use fully qualified collection names when ambiguity or portability matters. Facts describe targets; registered variables capture a task result; magic variables describe Ansible execution context. Understand when facts are gathered and when a value is undefined.

Loops apply a task to items; `when` controls execution per host/item; handlers run when notified by a changed task at normal or explicit flush points; blocks group tasks and support `rescue`/`always`. A handler is not a substitute for explicit validation, and `ignore_errors` is rarely correct error design.

**Related item:** YAML parses values before Ansible evaluates Jinja. Indentation, scalar types, quoting and templating boundaries can produce syntactically valid but semantically wrong automation.

## 3. Configure control and managed nodes

Create static INI or YAML inventory with meaningful groups. Validate with inventory graph/list/host views and an ad hoc reachability test. Configure SSH keys and target accounts, verify host keys and permissions, and establish privilege escalation with least privilege. Diagnose unreachable versus failed: DNS/route/SSH/auth/Python is different from a module or sudo failure.

Deploy files using `copy`, `template`, `file`, `fetch`, `synchronize` only where appropriate, and manage owner/group/mode/SELinux context/backup/content source. Avoid manual preconfiguration that the playbook does not encode, because fresh targets will not contain it.

Use separate control/development dependencies from managed-node requirements. An execution environment container supplies `ansible-core`, collections and Python dependencies consistently. Inspect image/content versions and do not assume the local host's installed collection is available inside the execution environment.

## 4. Run and develop playbooks

Use both `ansible-playbook` and `ansible-navigator` as listed in the objective. Know inventory selection, playbook path, variables, tags, limit, verbosity, check/diff mode, syntax validation and result interpretation. `ansible-navigator` can browse documentation/content, inspect inventory/environment and run within an execution environment. Practice its text/stdout interaction without internet.

Use VS Code to create YAML, configure navigator, run through a development container/execution environment, and work with Git. The objective names basic Git: clone a repository, add files, commit logically, inspect status/diff/log and push playbooks. Keep Vault passwords, private keys, generated artifacts and credentials out of the repository with appropriate ignore and secret handling.

**Related item:** Check mode is a prediction implemented by modules, not proof of final state; some modules do not fully support it. Validate actual application on disposable targets.

For [check/diff modes](https://docs.ansible.com/projects/ansible-core/2.16/playbook_guide/playbooks_checkmode.html), inspect each module's support and task overrides. `check_mode: false` can execute a task normally even during `--check`. Registered results from skipped or simulated work can differ from a real run. Diff output may reveal sensitive rendered content; use appropriate `diff: false` and `no_log` controls for secret tasks, then inspect target permissions separately.

## 5. Create resilient plays and playbooks

Express desired state with modules rather than a chain of imperative shell commands. Set `state`, `enabled`, source/destination, ownership, type, mount state, policy and other parameters explicitly. A second clean run should report no changes unless the requirement is inherently dynamic.

Use variables at the correct scope and precedence; use defaults for roles, inventory data for environment, Vault for secrets and `set_fact` only when computed runtime state is intended. Register command/module results and test documented fields. Use facts and filters to make platform-aware decisions without hiding invalid assumptions.

Conditionals should test exact supported data. Loops should use readable item structures and labels. Notify handlers only when a service-relevant resource changes. Use `block`/`rescue`/`always`, `failed_when`, `changed_when`, assertions and explicit validation to distinguish expected state from concealed failure. Do not blanket-ignore errors.

### Failures, recovery and handlers are separate outcomes

The [error-handling reference](https://docs.ansible.com/projects/ansible-core/2.16/playbook_guide/playbooks_error_handling.html) makes two easy-to-miss distinctions. A list of `failed_when` expressions means AND; use an explicit `or` when either condition should fail. `changed_when: false` only changes reporting/notification; it does not stop a command from changing the machine. For a hypothetical read-only health command, these results illustrate the contract `result.rc != 0 or result.stdout != 'ready'`:

| Return code | stdout | Explicit OR fails? | Two-condition AND list fails? |
|---:|---|---|---|
| 0 | ready | No | No |
| 0 | degraded | Yes | No |
| 2 | ready | Yes | No |
| 2 | degraded | Yes | Yes |

Use raw expressions for `when`/`failed_when`, without wrapping the whole condition in `{{ }}`. Check the command's documented result fields and normalize output deliberately; do not assume a return-code convention shared by every utility.

With [blocks](https://docs.ansible.com/projects/ansible-core/2.16/playbook_guide/playbooks_blocks.html), a successful rescue permits continuation but is not an automatic rollback or proof that the original requested state exists. If recovery only collects evidence, explicitly fail afterward when the target is still invalid. Unreachable hosts and malformed tasks are outside ordinary block-failure recovery; `always` is not a guarantee that remote cleanup can run after the connection disappears.

A notified [handler](https://docs.ansible.com/projects/ansible-core/2.16/playbook_guide/playbooks_handlers.html) can be suppressed if a later task fails on that host. `force_handlers` changes that behavior but cannot restore lost connectivity or make invalid configuration safe. Validate the candidate before notification; use a deliberate `meta: flush_handlers` point when later checks depend on the handler's effect. Repeated notification is deduplicated within a flush cycle, not a promise of only one execution across an entire multi-play run.

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

The [template module](https://docs.ansible.com/projects/ansible-core/2.16/collections/ansible/builtin/template_module.html) can validate a temporary candidate before replacing the destination. Its validation command needs `%s` for the temporary path; shell pipes and expansion are not available there. A valid rendered file can still express the wrong intent, so validate input types and final service behavior as well. Avoid timestamps or random values in otherwise stable configuration.

### Original typed-input and candidate-validation exercise

Save the following as `inventory.yml`, `study.yml`, `templates/study.ini.j2` and `files/validate_study.py`. Use two disposable Linux hosts with working SSH/Python and an ordinary account able to create `/var/tmp/ex294-study`. This example writes only that lab directory and does not start a service. Replace the inventory names with your own lab hosts before a real run.

`inventory.yml`:

```yaml
all:
  children:
    study:
      hosts:
        study-a:
          app_port: 8080
          app_enabled: false
          app_backends: [beta, alpha]
        study-b:
          app_port: 8443
          app_enabled: true
          app_backends: [gamma]
```

`study.yml`:

```yaml
- name: Validate and render original study configuration
  hosts: study
  gather_facts: false
  become: false
  vars:
    study_directory: /var/tmp/ex294-study
  tasks:
    - name: Enforce the input contract
      ansible.builtin.assert:
        that:
          - app_port is integer
          - app_port >= 1024 and app_port <= 65535
          - app_enabled is boolean
          - app_backends is sequence and app_backends is not string and app_backends is not mapping
          - app_backends | length > 0
          - app_backends | unique | list | length == app_backends | length
    - name: Permit only the fixture's known backend names
      ansible.builtin.assert:
        that:
          - item in ['alpha', 'beta', 'gamma']
      loop: "{{ app_backends }}"
    - name: Create the owned lab directory
      ansible.builtin.file:
        path: "{{ study_directory }}"
        state: directory
        mode: '0700'
    - name: Install the candidate validator
      ansible.builtin.copy:
        src: files/validate_study.py
        dest: "{{ study_directory }}/validate_study.py"
        mode: '0700'
    - name: Validate and install the rendered candidate
      ansible.builtin.template:
        src: templates/study.ini.j2
        dest: "{{ study_directory }}/study.ini"
        mode: '0640'
        validate: "/usr/bin/python3 {{ study_directory }}/validate_study.py %s"
      notify: Report a configuration change
    - name: Finish pending notifications before later verification
      ansible.builtin.meta: flush_handlers
  handlers:
    - name: Report a configuration change
      ansible.builtin.debug:
        msg: Study configuration changed; no service is installed by this exercise.
```

`templates/study.ini.j2`:

```jinja
[listener]
port={{ app_port }}
enabled={{ 'true' if app_enabled else 'false' }}
[backends]
{% for backend in app_backends | sort %}
backend_{{ loop.index }}={{ backend }}
{% endfor %}
```

`files/validate_study.py`:

```python
import configparser
from pathlib import Path
import sys


def valid(path):
    cfg = configparser.ConfigParser(interpolation=None, strict=True)
    with Path(path).open(encoding="utf-8") as stream:
        cfg.read_file(stream)
    if cfg.defaults() or set(cfg.sections()) != {"listener", "backends"}:
        return False
    listener = cfg["listener"]
    if set(listener) != {"port", "enabled"}:
        return False
    if not listener["port"].isascii() or not listener["port"].isdecimal():
        return False
    if not 1024 <= int(listener["port"]) <= 65535:
        return False
    if listener["enabled"] not in {"true", "false"}:
        return False
    peers = cfg["backends"]
    expected = {"backend_" + str(i) for i in range(1, len(peers) + 1)}
    values = list(peers.values())
    return (bool(values) and set(peers) == expected
            and len(values) == len(set(values))
            and all(v in {"alpha", "beta", "gamma"} for v in values))


if __name__ == "__main__":
    try:
        accepted = len(sys.argv) == 2 and valid(sys.argv[1])
    except (OSError, ValueError, configparser.Error):
        accepted = False
    raise SystemExit(0 if accepted else 1)
```

For `study-a`, expect port 8080, literal `enabled=false`, and alpha/beta in sorted order. `study-b` renders port 8443, `enabled=true` and gamma. Quoting an input as `app_enabled: "false"` must fail the **input** assertion: bypassing it would render `true`, which is syntactically valid and would pass the candidate validator. Input validation and file validation therefore protect different boundaries.

On your lab controller, inspect `ansible-inventory -i inventory.yml --graph` and host variables, then use `ansible-playbook -i inventory.yml study.yml --syntax-check`, preview supported tasks, and run narrowly before both hosts. Run a second time and expect no unintended changes or notification; reverse the input backend order and expect identical sorted content. Change one port and expect one configuration change. Remove a required value or use an unknown backend and expect failure before file replacement. A fresh-target check run may encounter dependencies not yet created; that is not the same as a failed real apply. Perform an actual fresh-target run afterward. These are expected Ansible observations, not claims that this review executed a playbook.

[Ansible Vault](https://docs.ansible.com/projects/ansible-core/2.16/vault_guide/vault.html) encrypts data at rest in files/variables; it does not prevent a playbook from logging, writing or exposing decrypted values. Use Vault IDs/password sources according to the provided environment, `no_log` for sensitive task output when appropriate, restrictive target permissions, and no plaintext secret in Git/history/artifacts. Test rekey/edit/view/encrypt/decrypt workflows only with lab values.

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

## Answers to the original knowledge checks

1. Evaluation reapplies your automation to fresh systems; undocumented manual repairs will be absent.
2. A clean controller/EE and fresh targets reach the required state from declared inputs, followed by independent checks and a repeat run.
3. You need to recognize correct Linux state and identify the failed layer before choosing modules or validation.
4. Inventory sources, groups and host variables combine through precedence; inspect the effective host view, not one file alone.
5. Inspect ansible --version and ansible-config dump --only-changed in the real execution context. The first applicable configuration file is selected; environment, CLI and variables can still override settings.
6. Facts describe gathered target state; registered values hold task results; magic variables describe the execution context.
7. A changed notifying task queues the handler for a normal or explicit flush point. Later failure can suppress it, and unreachable hosts may prevent execution even with force_handlers.
8. It can continue after a failed task without establishing the required state and does not handle every failure category.
9. Unreachable means a connection cannot perform the task; failed means an executed task returned a failure. Diagnose transport separately from module or escalation errors.
10. Declare the core/runner runtime, collections, Python/system dependencies and needed configuration; credentials still require deliberate runtime handling.
11. Navigator may run inside a container with different filesystem paths and installed content. Inspect that EE, not only the host installation.
12. It does not prove real target changes, every dependency, handler outcome or application health. Unsupported modules may skip, and check_mode: false can still change state.
13. No tracked file, commit history, template, inventory, log, artifact or remote repository should contain those plaintext credentials. Encryption and repository cleanup are separate concerns.
14. It identifies the collection and module precisely and avoids ambiguous short-name resolution.
15. The same requested state remains correct without unintended changes; independently verify it because changed=0 alone can hide a faulty changed_when.
16. Use it when no suitable module fits and the command contract is understood. Define real guards for repeated execution plus accurate changed_when and failed_when; reporting alone is not idempotence.
17. Defaults are intended for ordinary caller overrides; role vars have higher precedence and should not casually fix configurable inputs.
18. Explicit inputs/defaults, documented dependencies and supported targets, clear outputs, safe failure behavior and independent repeated/fresh-host tests.
19. A role packages a reusable task/configuration structure; a namespaced collection can distribute roles, modules, plugins and docs together.
20. A fresh controller must resolve the same required APIs and dependencies rather than relying on locally accumulated packages.
21. Inventory/limit review, a small canary, serial batches, preconditions, supported previews, scoped identities and health gates; none replaces knowing the task effects.
22. Reject malformed candidate content before replacement or restart; validate application health after activation as a separate check.
23. When a whole file belongs to automation or a structured module manages the state. Repeated line edits can miss duplicates, ordering and format rules.
24. Confirm host/device identity, existing signatures and ownership, free space, requested sizes, backups and the exact permitted destructive boundary.
25. Physical/block capacity, partition/PV/VG/LV as applicable, filesystem size and mount state; these layers need separate evidence.
26. Live rules and saved rules can differ. Set the intended zone and both required states, then verify after reload/reboot and from a peer.
27. The requested enabled services, storage/mount/swap configuration, accounts, access controls and application behavior must recover without manual repair.
28. The user module's supplementary groups can replace existing memberships unless append behavior is appropriate; distinguish primary and supplementary groups.
29. A process can run with incorrect configuration, no reachable listener, bad authorization or failed dependencies. Test the requested behavior.
30. File contexts label paths, port labels classify listening ports, and booleans toggle permitted policy behavior; none is an interchangeable bypass.
31. Vault encrypts stored data; decrypted task output, target files, process arguments, editor copies and external logs still require protection.
32. It does not change target permissions, prevent every downstream log or fix a task that intentionally writes plaintext. Restrict diff and artifacts too.
33. Check documented result fields and skipped/failed states, quote arguments instead of concatenating shell commands, and test the exact return/output contract.
34. A block groups tasks; rescue handles returned task failures; always performs follow-up within that execution flow. Recovery is not automatic rollback and cannot guarantee cleanup on unreachable systems.
35. Correlate schedule configuration with timestamped job/service output and the intended artifact or effect; an installed schedule is only intent.
36. They expose hidden manual dependencies, unstable templates, inaccurate change reporting and missing persistence before evaluation.
37. Start with YAML indentation/types/quoting and the reported file/line; module and network diagnosis comes after parsing.
38. The selected execution-environment image, collection paths/versions and declared dependencies, including navigator settings.
39. Assigned exam version and objective list, RHEL target version, AAP/core/EE/navigator versions, available collections and allowed documentation. A course label does not assign an exam version.
40. Uncovered navigator and EE use, VS Code/development-container work, Git, collections and current RHEL administration. Compare the exact assigned list and keep old material supplemental.

## Version and older-course checklist

Before relying on RHEL 8/9 or pre-AAP-2.5 material, confirm coverage for the purchasable version and the live objectives:

- `ansible.cfg` and `ansible-navigator.yml` configuration;
- both `ansible-playbook` and `ansible-navigator`, including content discovery, inventory and execution environment;
- VS Code and Ansible development-container workflow;
- Git clone/add/commit/push workflow without secrets;
- roles plus namespaced/versioned Content Collections and declared dependencies;
- current RHEL 10 administration behavior and supported modules;
- fresh-system evaluation, idempotence, persistence and reboot validation;
- AU294's current RHEL 10, Ansible Core 2.16 and AAP 2.6 alignment—without assuming that course labels alone identify the exact purchased exam version.

## Source map and freshness notes

The live EX294 page defines public tasks and says they represent the most recent product version; the purchase flow defines which versions are actually available. AU294 supplies the current public training baseline, and AAP/RHEL/upstream Ansible documentation supplies technical behavior.

- **VERIFY CURRENT:** purchasable exam version, RHEL/AAP/ansible-core/navigator/execution-environment/collection versions, delivery rules, objective text, module behavior, course duration/access and credential naming.
- **Stable performance pattern:** declare dependencies → inspect effective inventory/config/data → express desired state → limit/canary → validate → rerun idempotently → fresh target → reboot → validate again.
- **Older RHCE material:** retain as conceptual support only after closing every navigator, execution-environment, VS Code/Git, collection and RHEL 10 gap.

This guide uses no recalled exam tasks or restricted course content. Its scenarios, labs and checks are original transformations of public objectives.

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. Choose one current version-aligned course, use official docs for exact modules and navigator behavior, and spend most preparation time building repeatable playbooks against fresh RHEL 10 hosts.

| Resource | Access | Estimated time |
|---|---|---:|
| EX294 objectives, EX200 refresh, AAP/RHEL docs | Public | 12–25 selected hours |
| Red Hat AU294 | Paid/RHLS | About 4–5 instructor-led days plus labs |
| Red Hat AU094 Ansible Basics | Public/free offering varies | 3–6 hours orientation estimated |
| Udemy / Imran Afzal EX294 | Paid; page blocked this review | Previously listed 7 hours 48 minutes video plus 30–60 hours labs |
| O'Reilly / Sander van Vugt RHCE 8 book | Paid/book; page blocked this review | Previously listed 516 pages / 12 hours 59 minutes; concepts only, substantial current gaps |
| Ansible upstream documentation | Public | 12–25 hours selected module/playbook practice |

- **Official route:** [Red Hat AU294](https://www.redhat.com/en/services/training/au294-red-hat-linux-automation-with-ansible) is the current companion course, based on RHEL 10, Ansible Core 2.16 and tooling aligned with AAP 2.6. Allow **4–5 instructor-led days plus substantial lab repetition**; verify delivery length and selected exam version.
- **Official orientation:** [AU094 Ansible Basics](https://www.redhat.com/en/services/training/au094-ansible-essentials-simplicity-automation-technical-overview) describes a free on-demand AAP 2.5 introduction and can establish vocabulary (**3–6 hours estimated**, not a verified video runtime), but is not EX294 preparation by itself.
- **Current product reference:** [AAP 2.6 documentation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6) and [Ansible community documentation](https://docs.ansible.com/ansible/latest/) provide current navigator, execution-environment, collection, playbook and module detail (**12–25 selected hours**).
- **Commercial video:** [Udemy / Imran Afzal Linux Red Hat Certified Engineer EX294](https://www.udemy.com/course/linux-red-hat-certified-engineer-rhce-ex294/) was previously listed as **7 hours 48 minutes**, 72 lectures, updated June 2026; the page blocked access on September 28, so those details were not reverified. Map navigator/development-container/Git/current-AAP objectives explicitly before using it as the main route.
- **Hands-on practice:** [Udemy / Ghada Atef RHEL 10 EX294 practice](https://www.udemy.com/course/rhce-ex294-practice-exams-master-ansible-automation/) was previously listed as six RHEL 10 scenarios/sets updated July 2026; the page blocked access in this review, so neither details nor item contents were reverified. Use only as a prompt to build original fresh-host labs; its page mixes claims beyond the exact public objectives, so do not treat it as scope authority.
- **Older detailed reference:** [O'Reilly/Pearson Red Hat RHCE 8 EX294 Cert Guide](https://www.oreilly.com/library/view/red-hat-rhce/9780136872481/) was previously listed as **516 pages / 12 hours 59 minutes**, October 2020; its page blocked access in this review, so this metadata remains unverified. It remains useful for roles, variables and RHEL automation but predates navigator, execution environments, VS Code development containers, Git and current RHEL 10/AAP; close all gaps above.

- **Operational reading:** John Wadleigh's April 9, 2019 [Ansible deployment lessons](https://www.redhat.com/en/blog/adventures-ansible-lessons-learned-real-world-deployments) offers useful context on repeatable desired state and clear role/task interfaces. Allow its listed five-minute reading time plus 1–2 hours to review your own role. It is historical: use current documentation for handler timing, supported tools and exact APIs.

**PRACTICAL DEPTH — evidence boundary:** The [September 28 review](../docs/research/2026-09-28-ex294-deep-review.md) executed local Jinja rendering, the original Python candidate validator and expression checks. It did not run ansible-playbook, navigator, an EE, SSH, RHEL service/storage/security changes, Vault encryption or reboot/fresh-host assessment. All eight platform labs remain proposed.

No exact current EX294 Pluralsight, Whizlabs, MeasureUp, KodeKloud, or RHEL-10/AAP-2.6 O'Reilly end-to-end product was independently verified September 28. Avoid multiple-choice “exam simulation” as primary preparation for a fresh-system performance assessment. Plan **100–180 hours** after solid RHCSA skills, or **220–350 hours** if Linux administration and automation are both new.
