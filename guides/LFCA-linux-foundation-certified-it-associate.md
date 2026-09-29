---
exam_code: LFCA
vendor_id: linux-foundation
official_blueprint: https://training.linuxfoundation.org/certification/certified-it-associate/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# LFCA Linux Foundation Certified IT Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 29, 2026. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#lfca-coverage-record). The [official LFCA page](https://training.linuxfoundation.org/certification/certified-it-associate/) is authoritative.

**Current baseline:** Six-domain objectives effective September 16, 2025<br>
**Lifecycle watch:** No replacement or objective change is announced; the Japanese LFCA-JP offering retired with the 2025 update<br>
**Official delivery snapshot:** Online, remotely proctored, multiple-choice; 90 minutes; English; certification valid for two years; one retake and 12 months of exam eligibility listed<br>
**Prerequisite:** None; Linux Foundation labels the credential beginner/pre-professional

## How to use this guide

LFCA is broad. Build one connected model rather than six piles of terms:

1. a Linux host runs processes that use CPU, memory, storage, devices and a network;
2. administrators configure identities, software, services, monitoring, backup and recovery;
3. cloud, virtualization and containers change where responsibility and resources live;
4. security protects identities, systems, networks and sensitive data under policy;
5. DevOps and Git make change repeatable and reviewable;
6. project and functional analysis connect technical work to user value, architecture and open-source obligations.

For each concept, explain its purpose, recognize a simple scenario, perform a safe lab where possible, and name the evidence that proves the result. The exam is multiple-choice, but hands-on work makes distractors easier to reject. Practice on a disposable VM; confirm paths and permissions; never run destructive commands copied from a source without understanding the target and recovery plan.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Weighted objective map

| Domain | Weight | Readiness evidence |
|---|---:|---|
| 1. Linux fundamentals | 16% | Explain OS roles and use the command line to navigate, inspect and manipulate files/processes safely |
| 2. System administration fundamentals | 30% | Operate users, software, services, storage, networking, monitoring, troubleshooting, backup and recovery |
| 3. Cloud computing fundamentals | 18% | Compare models, virtualization/containers, availability/performance, networking, budgeting and responsibility |
| 4. Security fundamentals | 14% | Apply CIA, identity, least privilege, network/system/data protection, incident and compliance basics |
| 5. DevOps fundamentals | 12% | Explain collaboration/automation, Git, CI/CD, containers and observable reliable change |
| 6. IT project management fundamentals | 10% | Connect scope, requirements, architecture, delivery methods and open-source licensing to outcomes |

**CURRENT BLUEPRINT:** The official page and September 2025 notice list **22 competencies**, grouped 2/5/5/3/3/4. They do not publish a detailed command-by-command syllabus. The examples below provide original teaching and practice; they are not additional official objectives.

| Domain | Published competency coverage |
|---|---|
| Linux | Operating-system model; command line |
| Administration | Administration; best practices; networking; troubleshooting; disaster recovery |
| Cloud | Cloud concepts; performance/availability; budgeting; best practices; networking |
| Security | Security; sensitive data; compliance |
| DevOps | DevOps basics; Git concepts; containers |
| IT projects | Project management; application architecture; functional analysis; open-source software/licensing |

The [official language table](https://docs.linuxfoundation.org/tc-docs/certification/lf-handbook2/language) confirms English for LFCA. The [multiple-choice FAQ](https://docs.linuxfoundation.org/tc-docs/certification/faq-mc) currently lists a 75% passing score and two-year validity. **VERIFY CURRENT:** recheck scheduling, eligibility, retake terms and delivery requirements before purchase; this guide does not supply recalled questions or infer a question count.

## 1. Linux fundamentals — 16%

### Operating system and distribution model

An operating system manages processor scheduling, memory, devices, storage/filesystems, processes, networking and security while exposing interfaces to applications and users. The Linux kernel is combined with user-space tools, package management, configuration and a release/support policy to form a distribution. Debian/Ubuntu and Red Hat/Fedora-family systems share Linux concepts but differ in package tools, defaults, file locations and lifecycle.

The shell interprets commands; a terminal is an interface to a shell; a graphical desktop is another interface. Root has extensive authority, while ordinary users should elevate only for an authorized task. The filesystem tree starts at `/`; common purposes include `/etc` configuration, `/var` changing data/logs, `/home` user data, `/usr` installed userland, `/tmp` temporary files, `/dev` devices, and `/proc`/`/sys` kernel views.

Boot moves from firmware and bootloader to kernel, initial userspace and service manager. A process is a running program with an identity, parent, environment and resources. A daemon/service normally runs in the background. Know that a running state now differs from configuration that persists after restart.

### Command-line literacy

Use `pwd`, `cd`, `ls`, `file`, `stat`, `cat`, `less`, `head`, `tail`, `touch`, `mkdir`, `cp`, `mv` and `rm` deliberately. Absolute paths begin at `/`; relative paths begin at the current directory. `.` is current and `..` is parent. Hidden names begin with a dot. Globs such as `*` are expanded by the shell, so preview selections before copying, moving or deleting.

Search with `find` for filesystem entries and `grep` for matching text. Transform or select with tools such as `sort`, `uniq`, `cut`, `wc`, `sed` and `awk` at a beginner level. A pipe passes standard output to another command; `>` replaces a file, `>>` appends and `2>` redirects standard error. Quote variable expansions and paths with spaces. Read `man`, `--help` and distribution documentation instead of guessing.

Linux records owner, group and other permission bits. Read/write/execute have different meanings on files and directories; `chmod` changes mode and `chown` changes ownership. Symbolic links store another path; hard links name the same inode. Use `ps`, `top`, `pgrep` and `kill` only after identifying the correct process and owner.

> **Related item:** A command that succeeds is not automatically persistent, secure or correct. Verify output, affected object, permissions and behavior after restart when relevant.

### Original stream and exit-status exercise

**PRACTICAL DEPTH:** Run the following Bash example in a new disposable directory with synthetic files only. Inspect `counts.txt`, `combined.txt` and `normal-only.txt`. The [Bash maintainer’s reference](https://tiswww.case.edu/php/chet/bash/bashref.html) explains left-to-right redirection and the pipeline-status rules demonstrated here. Quoting preserves the space in the input name; `uniq` counts adjacent duplicates, so sorting comes first.

```bash
#!/usr/bin/env bash
set -u
# Run in a new disposable directory; these are synthetic files.
printf 'ok\nfail\nok\n' > 'sample events.txt'
sort 'sample events.txt' | uniq -c > counts.txt
emit() { printf 'normal\n'; printf 'diagnostic\n' >&2; }
emit > combined.txt 2>&1     # both streams go to the file
emit 2>&1 > normal-only.txt # diagnostic goes to the original stdout

set +o pipefail
false | cat
printf 'default pipeline status=%s\n' "$?"
set -o pipefail
false | cat
printf 'pipefail pipeline status=%s\n' "$?"

if grep -q 'absent' 'sample events.txt'; then
  printf 'matched\n'
else
  result=$?
  printf 'grep result=%s (1 means no match; larger means error)\n' "$result"
fi
```

Expected: one `fail` and two `ok` records; `combined.txt` contains both streams, while the second redirection leaves `diagnostic` on the original standard output. The failed first pipeline command is hidden by a successful final command under the default rule; `pipefail` exposes it. Save `$?` immediately because the next command replaces it. This script intentionally continues after the failed pipeline to display its result; do not assume `set -e` is a universal error-handling policy. Interpret exit codes for the specific command: a grep no-match result is different from a missing-input error.

### Permissions and evidence before modification

For a regular file, read permits reading its bytes, write changing them and execute requesting execution, subject to other controls. For a directory, read lists names, execute searches/traverses and write changes directory entries. Removing a file generally depends on write/search permission on its parent and path traversal, not the file’s write bit. [Linux unlink documentation](https://man7.org/linux/man-pages/man2/unlink.2.html) describes additional restrictions such as sticky directories; ACLs, read-only mounts and security policy can also matter. A mode such as 640 is not a complete effective-access test.

Use `id`, `ls -ld`, `stat` and the relevant ACL tools in an authorized Linux lab before changing ownership or mode. An ordinary user may be able to modify one file but not rename it, or list a directory but not open its children. Predict the operation, test as the intended identity and record the error. The MSYS exercise above does not establish native Linux permission behavior.

## 2. System administration fundamentals — 30%

### Identities, software, services and storage

Users have numeric UID, primary/supplementary groups, home and shell. Groups simplify shared authorization. Account tools manage creation, membership, password/expiry and removal; offboarding also addresses files, keys, scheduled jobs and service ownership. `sudo` delegates bounded privilege and should be audited; logging in as root for routine work expands risk.

Package managers obtain packages from configured repositories, resolve dependencies and track updates/removal. Authentication details differ by ecosystem: [APT authenticates repository metadata and its chain of package checksums](https://manpages.debian.org/trixie/apt/apt-secure.8.en.html), which is not the same as verifying a signature inside every downloaded package. Repository trust does not prove that a package is free of malicious code. APT/dpkg and DNF/RPM represent common families. Verify distribution/release, repository trust, architecture, configuration changes and whether a service restart or reboot is needed. Do not pipe an unreviewed Internet script into a privileged shell.

Service managers start, stop, restart, reload, enable and inspect units. “Active” means a process/unit state, not necessarily that users can reach a healthy application. Check configuration, logs, listening socket, identity/permissions, firewall and a real request. Schedule recurring work with cron or timers while defining identity, environment, working directory, output and failure handling.

Disks contain partitions or logical volumes; filesystems organize data; mounts attach a filesystem to the tree. Use capacity tools to distinguish block space from inode/file-count exhaustion. Backups are copies retained for recovery; snapshots and RAID can support operations but are not automatically independent backups. Protect and periodically restore-test data plus configuration, keys and documentation.

### Service state and a beginner troubleshooting record

On systemd systems, [systemctl’s manual](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html) distinguishes starting a unit now from enabling its configured activation links. `enable` alone does not start it, and `disable` alone does not stop it. `--now` combines the corresponding runtime action. A static, socket-activated or dependency-started unit may work without being enabled in the usual way. Do not edit a real host merely to reproduce this distinction.

| Observation in an authorized Linux lab | What it helps establish | What it does not establish |
|---|---|---|
| `systemctl is-active` / `is-enabled` for the chosen unit | Runtime versus configured activation state | End-user availability or every activation path |
| `journalctl -u` for the chosen unit | Recorded service events and errors | Complete application or remote-client evidence |
| `ss -lnt` | Local listening TCP sockets | Firewall allowance, correct TLS identity or successful request |
| `df -h` and `df -i` | Block and inode capacity | Why space is consumed or application consistency |

An original incident record should include expected behavior, actual response, timestamp, recent change, one hypothesis, one discriminating test, planned repair/rollback and the final acceptance result. For example, a healthy local request but a failed remote request narrows the path; it does not automatically identify the firewall as the cause.

### Networking

A host needs an address and prefix, route/default gateway and usually DNS resolver. IPv4 uses dotted decimal; a subnet/prefix divides network and host portions. MAC addresses identify local link interfaces; ARP/neighbor discovery resolves local delivery. Switches forward within a network, routers move between networks, firewalls filter traffic, and NAT translates addresses/ports.

DNS maps names to records; DHCP supplies address configuration; NTP synchronizes time. Common application protocols include HTTP/HTTPS, SSH, SMTP, DNS and DHCP; use secure alternatives and current documentation rather than memorizing a port without purpose. Diagnose from link/interface → address/prefix → route → DNS → firewall → listening service → application and return path. Compare resolver evidence and name/address requests to isolate DNS while preserving the intended HTTPS host name, SNI and certificate verification; a raw-IP HTTPS failure alone does not prove application failure.

### Monitoring, troubleshooting and recovery

Observe CPU/load, memory/swap, disk capacity/latency, network state, processes, services and logs. A high value is evidence, not cause: CPU can be busy because of valid load, memory can be cache, and a full filesystem can be blocks, inodes or deleted-open data. Correlate time, workload, recent change and user impact.

Troubleshoot by defining expected/actual behavior, scope, time, impact and recent changes; gather evidence; form a theory; test the least-invasive discriminator; plan rollback; make one controlled change; validate direct and dependent behavior; document root cause and prevention. Preserve evidence before rebooting or deleting.

Disaster recovery begins with business priorities, RTO (target restoration time) and RPO (tolerated data-loss window). Recovery needs protected copies, access, dependencies, capacity and rehearsed runbooks. Business continuity keeps critical outcomes operating; high availability reduces interruption; neither replaces backup.

> **Related item:** Incident recovery restores service; problem management finds recurring cause; change management controls the repair and its risk.

### Original recovery and measurement cases

A service fails at 12:05; the newest recoverable data is from 11:55 and usable recovery finishes at 12:50. The ten-minute data-loss window meets a 15-minute RPO, but 45 minutes of restoration misses a 30-minute RTO. Validate application behavior and keys/permissions after the copy completes. These are invented timestamps, not a performed Linux restore.

Three failed requests among 120 attempted requests give a 2.5% observed error fraction. Record the time window, caller mix and denominator; a small synthetic sample does not establish long-term availability. Monitoring an average can hide a slow tail or a failed minority.

## 3. Cloud computing fundamentals — 18%

Cloud computing supplies shared, network-accessed resources with self-service, elasticity and measured consumption. Public, private, hybrid and multicloud describe deployment relationships. IaaS exposes virtual infrastructure; PaaS manages more runtime; SaaS supplies an application; FaaS/serverless runs event-driven code. Shared responsibility changes by service: the provider secures underlying infrastructure while the customer retains identities, data, configuration and usage responsibilities.

Virtual machines emulate hardware and run guest operating systems. Containers package applications and dependencies while sharing the host kernel. Images are templates; containers are runtime instances; volumes preserve data; orchestration schedules and recovers workloads. Serverless reduces server administration but still requires secure identity, input, dependency, data, logging and cost controls.

Availability zones/failure domains separate faults; load balancing distributes healthy traffic; horizontal scaling adds instances and vertical scaling enlarges one. Elasticity adjusts capacity with demand. Performance involves latency, throughput, IOPS, CPU, memory and dependency behavior. Redundancy is useful only when health detection, data consistency and failover are designed and tested.

Cloud virtual networks still use addresses, subnets, routes, DNS, firewalls/security groups, load balancers and VPN/private connectivity. Follow traffic end to end. Cloud cost includes resource size/time, licenses, storage, operations/requests and data transfer. Use budgets, alerts, tags, rightsizing, schedules, autoscaling and lifecycle tiers; deleting unknown resources purely to reduce cost is unsafe.

> **Related item:** “Managed” moves tasks to a provider; it does not remove architecture, configuration, security, data or recovery decisions.

### Original cloud decision and budget cases

| Requirement | Compare | Evidence to collect |
|---|---|---|
| Control an unusual guest operating system | IaaS versus a managed application platform | Supported OS, patch owner, licensing and recovery responsibilities |
| Survive one zone loss while serving four capacity units | Three zones with two units each | Four units remain in the simple model; test actual placement, health and dependency behavior |
| Preserve uploaded files when an app instance is recreated | External data service/volume versus instance-local writes | Restore/recreation test, identity, consistency and retention |
| Bound costs | Resource quantities, usage duration and transfer | An estimate plus accountable usage review; alerts alone do not establish a spending cap |

With invented rates, three VMs for 100 hours at $0.05/hour, 80 GB storage at $0.10 for the period and 20 GB transfer at $0.20/GB total **$27**. This is arithmetic practice, not a vendor quotation; requests, licenses, backups, taxes and support are omitted. Consider the whole workload and remaining failure capacity before choosing the cheapest component.

[Docker’s container overview](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) describes isolated processes sharing a kernel. On a non-Linux workstation, Linux containers may run inside a Linux VM supplied by the runtime; they do not directly share the Windows or macOS kernel. A container image is not a backup of an application’s external data. No container or VM was launched in this review.

## 4. Security fundamentals — 14%

Confidentiality limits disclosure, integrity prevents/detects unauthorized change, and availability keeps authorized use possible. Risk connects asset value, threat, vulnerability, likelihood and impact. Controls may be preventive, detective, corrective, deterrent, compensating or recovery-oriented and may be administrative, technical or physical. Defense in depth uses independent layers.

Authentication proves identity; authorization permits action; accounting records it. Prefer least privilege, groups/roles, MFA, secure recovery and separate administrative identities. Passwords should be long/unique and stored through one-way password hashing; secrets/keys require protected storage and rotation. Encryption protects readable data with keys, while hashing supports integrity; digital signatures support integrity/authenticity and certificates bind keys to identities through trust.

Harden by using supported software, timely patches, minimal services, safe configuration, secure remote access, firewalling, malware controls, logging and tested backup. Phishing and social engineering target human trust; verify requests out of band and report them. Vulnerability scanning finds potential issues; validate exposure and remediate according to risk rather than assuming a scan equals security.

Classify sensitive data, collect the minimum, restrict access, encrypt appropriately, define retention and dispose safely. Compliance begins by identifying applicable law, contract, policy or framework, then mapping requirements to controls, evidence, tests and accountable owners. Privacy concerns appropriate collection/use and individual rights according to jurisdiction. Escalate legal interpretation.

Incident response prepares, detects/analyzes, contains, eradicates, recovers and learns. Preserve relevant logs and timestamps; do not destroy evidence to make a symptom disappear.

### Original data and control evidence matrix

For a fictional appointment system, collect only a synthetic name and requested time in practice; keep access logs separate from application records. Define who may read, edit, export and administer each dataset, plus retention, backup and deletion owners. A successful authorized request and a denied unauthorized request test different sides of the control.

| Proposed control | Useful evidence | Remaining question |
|---|---|---|
| MFA for administrators | Enforced policy and a tested sign-in path | Do recovery accounts or exceptions bypass it? |
| Encryption for backups | Key access policy and a successful isolated restore | Can an attacker delete both data and recovery keys? |
| Retention for logs | Applied settings and an expiry test with synthetic records | Are exports and backups governed too? |
| Patch management | Inventory, version and post-update behavior | Are unsupported components or failed deployments missing? |

These are original control-design examples, not an assertion of compliance with any law or standard. A hash comparison only proves agreement with the chosen reference; if both file and reference were replaced, it does not establish trusted origin. Password storage requires a suitable salted password-hashing scheme, not an ordinary fast file hash.

## 5. DevOps fundamentals — 12%

DevOps connects development and operations through collaboration, feedback, automation, shared responsibility and small reliable change. CI builds and tests each change; delivery/deployment promotes a versioned artifact through environments. A pipeline commonly includes source, build, test/security checks, artifact, approval, deploy, observe and rollback. Automation should be repeatable, least privilege, logged and tested.

Git is distributed version control. A repository holds history; a working tree contains current files; staging selects the next commit. Use `clone`, `status`, `diff`, `add`, `commit`, `log`, branch, merge, fetch/pull and push conceptually and in a lab. A branch isolates work; a merge combines histories; conflicts require understanding and retesting. Do not commit secrets, huge generated files or unclear binary artifacts.

Containers support consistent packaging but are not automatically secure or stateless. Pin trusted images, scan dependencies, use non-root and minimum capability, externalize configuration/secrets, set resource limits, restrict networks and recreate to prove persistence. Orchestration provides desired replicas, health, networking, storage, configuration and rollout behavior.

Monitoring supplies metrics/logs/events; feedback connects production behavior to planning. Reliable change includes small batches, peer review, automated tests, immutable artifacts, gradual rollout, rollback and learning—not only speed.

> **Related item:** DevOps is a socio-technical operating model. A tool purchase cannot replace ownership, communication or safe change practice.

### Git snapshots and original conflict-recovery exercise

[Git add](https://git-scm.com/docs/git-add) captures the selected content at that moment. A later edit stays outside the staged snapshot until staged again. [Git diff](https://git-scm.com/docs/git-diff) normally compares working files with staging; `--cached` compares staging with HEAD. [Restore with `--staged`](https://git-scm.com/docs/git-restore) normally resets only staging from HEAD, preserving later working-file edits. Restoring the working tree can discard changes, so inspect the intended target first.

Save the following outside a new empty practice directory, enter that directory and run the script with Bash. It makes synthetic local commits with a fictional identity, disables signing/hooks only in that disposable repository and configures no remote. It refuses a nonempty directory. Review each step and keep the repository until you have inspected both parents of the merge.

```bash
#!/usr/bin/env bash
set -euo pipefail
# Run only in a NEW, empty, disposable directory. No remote is used.
if [ -n "$(ls -A)" ]; then
  printf 'Choose an empty practice directory.\n' >&2
  exit 2
fi
git init --template= --initial-branch=main .
git config --local user.name 'Practice Learner'
git config --local user.email 'practice@example.invalid'
git config --local commit.gpgsign false
git config --local core.autocrlf false
mkdir .git/empty-hooks
git config --local core.hooksPath .git/empty-hooks

printf 'timeout=10\n' > settings.txt
git add -- settings.txt
git commit -m 'Record starting configuration'
printf 'timeout=20\n' > settings.txt
git add -- settings.txt
printf 'timeout=30\n' > settings.txt
git diff --cached -- settings.txt  # HEAD -> staging: 10 -> 20
git diff -- settings.txt           # staging -> working tree: 20 -> 30
git restore --staged -- settings.txt
git diff -- settings.txt           # working copy is still 30
git add -- settings.txt
git commit -m 'Review timeout 30'

git switch -c experiment
printf 'timeout=40\n' > settings.txt
git add -- settings.txt
git commit -m 'Try timeout 40'
git switch main
printf 'timeout=20\n' > settings.txt
git add -- settings.txt
git commit -m 'Try timeout 20'
if git merge --no-edit experiment; then
  printf 'Expected a conflict in this fixture.\n' >&2
  exit 3
fi
git status --short
git merge --abort
git status --short             # clean; main still contains timeout=20
test "$(cat settings.txt)" = 'timeout=20'
test -z "$(git status --porcelain)"
if git merge --no-edit experiment; then
  printf 'Expected a conflict in this fixture.\n' >&2
  exit 3
fi
# The fictional acceptance requirement is now an agreed timeout of 30.
printf 'timeout=30\n' > settings.txt
test "$(cat settings.txt)" = 'timeout=30'
git add -- settings.txt
git commit -m 'Resolve with agreed timeout 30'
git log --oneline --graph --all
git status --short             # clean; no push occurs
```

The first conflict is aborted; the second is resolved against a newly agreed fictional requirement of 30. That decision is visible and tested, rather than blindly selecting one branch. This tiny content assertion does not test a running application. [Git merge](https://git-scm.com/docs/git-merge) warns that abort may not reconstruct pre-existing uncommitted changes reliably, so begin a real merge from a reviewed clean state.

[Ignore patterns](https://git-scm.com/docs/gitignore) affect untracked files. Adding a tracked file to `.gitignore` does not stop tracking it or remove old commits. `git rm --cached` removes the selected path from staging while preserving its working copy; it does not erase history. For real exposed credentials, revoke/rotate and investigate use before following an approved cleanup process. Only synthetic logs were used to test this behavior.

**Executed September 29, 2026:** both exact public scripts and a harness passed **35 checks**, using Git 2.55.0.windows.5, MSYS Bash 5.3.15 and Python 3.13.14. Checks covered three Git snapshots, staging/unstaging, two merge conflicts with abort/resolution, ignored versus tracked files, retained history, quoted paths, stream order, pipeline/grep statuses and original planning arithmetic. All owned temporary files and repositories were cleaned. No remote, credential, network service, global Git configuration, Linux VM, account, package, firewall, container or cloud was changed. Full Linux administration labs remain proposed; the native Linux runtime blocker is deferred.

## 6. IT project management fundamentals — 10%

A project has a defined outcome, stakeholders, scope, constraints, plan, risks, dependencies, resources and acceptance criteria. Initiation clarifies value and sponsor; planning defines work/schedule/budget/risk; execution produces deliverables; monitoring controls variance/change; closure obtains acceptance and captures lessons. Operations are ongoing; a project is temporary.

Waterfall-style work sequences phases and suits stable requirements; iterative/incremental approaches deliver and learn in smaller steps; Agile values collaboration and response to change. The [2020 Scrum Guide](https://scrumguides.org/scrum-guide.html) defines a Scrum Team with Developers, a Product Owner and a Scrum Master. The Product Owner is accountable for value and backlog management, Developers for the plan and a usable increment, and the Scrum Master for establishing Scrum and helping team effectiveness. Kanban visualizes flow and work-in-progress. Methods are tools, not guarantees.

Functional requirements describe behavior; non-functional requirements describe qualities such as availability, performance, security, usability and maintainability. Functional analysis identifies actors, workflows, inputs/outputs, rules, exceptions and acceptance. Trace a requirement to design, implementation, test and outcome. Uncontrolled scope change affects schedule, cost, risk and quality.

Application architecture may be monolithic or service-oriented/microservice, layered, client-server, event-driven or serverless. Compare coupling, deployment, data consistency, operational complexity and failure modes. APIs define contracts between components; synchronous communication couples response time/availability, while asynchronous queues decouple at the cost of ordering/retry/observability complexity.

The [Open Source Definition](https://opensource.org/osd) requires more than readable source: distribution terms must also meet conditions concerning redistribution, modification and permitted use. A public repository without a suitable license does not automatically grant those rights. Open source does not mean no copyright, no obligations or zero cost. Permissive and copyleft licenses impose different conditions. Track components, notices, source/attribution/distribution obligations and security maintenance; obtain qualified legal guidance for license decisions. Communities use governance, contribution processes and codes of conduct.

### Original functional-analysis and project worksheet

For a fictional equipment-booking app, a functional requirement is “an authorized user can reserve an available item.” Derive cases for available/unavailable items, overlapping requests, unauthorized users and cancelled reservations. A non-functional requirement might set an explicitly measured response-time threshold under a defined load; “fast and secure” alone is not testable. Trace each requirement to its owner, design decision, test result and acceptance decision.

Start with the least complex architecture that meets the evidence. A single application can simplify deployment and transactions; separate services may support independent change but introduce network, identity, data-consistency and recovery boundaries. An asynchronous notification can avoid holding up a reservation, but duplicates and retries need a design. The architecture label alone establishes neither quality nor scalability.

An invented plan has two days of discovery, then four days of implementation and three days of documentation in parallel, followed by one day of acceptance after both finish. With independent resources and no other delays, elapsed time is **seven days**, not ten. A shared person, review delay or rework changes the calculation. Record dependencies, ownership, assumptions and change impact instead of summing parallel work blindly.

For each reused component, record exact version/source, license text, modifications, notices, distribution context, security owner and unresolved questions. The [SPDX License List](https://spdx.org/licenses/) supplies standardized identifiers and texts; an identifier is not permission to omit an obligation or a compatibility opinion. Keep legal interpretation with the appropriate reviewer. Licensing detail here supports the public competency; it is not a promise that a particular license combination is suitable.

## Integrated scenarios

### Scenario 1: Small web service fails after an update

Confirm user symptom, scope and change. Check host capacity, service state/logs, package/configuration, port, permissions, firewall, DNS and a local request. Roll back or repair with approval, validate security and dependent access, then update the change record and add a pre-deployment test. This connects Linux, administration, networking, security and DevOps.

### Scenario 2: Move a community application to cloud

Capture functional and non-functional requirements, data sensitivity, dependencies, availability and budget. Choose service/deployment model and responsibility owners, design network/identity/backup/monitoring, estimate cost, pilot and test failure/restore. Record open-source licenses and user acceptance. Do not assume cloud automatically improves security or availability.

### Scenario 3: Lost laptop and exposed repository token

Report the incident, revoke/rotate the token, inspect audit/repository/pipeline logs for use, protect accounts with MFA and scope, assess sensitive data, and follow notification/evidence policy. Restore work from trusted remote history or backup, validate artifacts, document lessons and add secret scanning/device encryption. Deleting a local file alone is not containment.

## Hands-on labs

All eight complete labs remain proposed. The executed Git/MSYS exercises above cover narrower command behavior; native Linux administration and container/cloud execution remain unverified. Use an authorized disposable Linux environment, synthetic data and a recorded cleanup inventory.

1. **Linux tour:** identify kernel, distribution, shell, current identity and filesystem purposes on a disposable VM. Compare a normal process with a managed service. Success: explain observed output and separate runtime state from configuration; retain the VM inventory and remove only owned practice resources.
2. **Command-line evidence:** run the stream exercise, then create a Linux lab tree and predict quoting, matching, redirects and permission results. Test allowed and denied operations as the intended identity. Success: distinguish no-match, command error and success, plus file permissions versus parent-directory deletion rights; preview every cleanup target.
3. **Administration:** create a practice user/group, install one trusted package and configure a local service. Compare active/enabled states and verify behavior after a controlled VM restart. Success: record package trust, dependencies, logs and an actual request; remove the test account/package/service without touching other workloads.
4. **Network break/fix:** record addresses, prefix, route, resolver and listening sockets. Introduce one reversible DNS, firewall or listener fault in the sandbox. Success: isolate it with a discriminating test, preserve HTTPS identity checks and restore the baseline; no scanning unrelated networks.
5. **Backup/recovery:** protect synthetic files and configuration, restore to a separate location and test changed/missing data, permissions and necessary keys. Success: report achieved RPO/RTO with defined timestamps and usable application criteria; a completed archive command alone is insufficient.
6. **Cloud comparison:** map the same workload to local VM, IaaS and managed-platform options. Record service responsibilities, network/identity flows, failure capacity, recovery and invented cost assumptions. Success: explain one condition under which each option fails the requirement; create billable resources only in an authorized bounded sandbox.
7. **Git/container delivery:** run the exact Git exercise, inspect all three snapshots and both merge parents, then demonstrate a synthetic ignored-versus-tracked file. In a separate approved container lab, recreate an app and verify external data/configuration. Success: prove the reviewed artifact and negative access case, and distinguish source history from backup; no real secrets or external repository push is needed.
8. **Project capstone:** define actors, functional/non-functional requirements, dependencies, acceptance tests, risk owners and a component/license inventory. Compare two architectures and calculate a schedule with parallel tasks. Success: trace every accepted requirement to evidence, record unresolved tradeoffs and obtain a fictional stakeholder acceptance decision rather than declaring success from task completion alone.

## Original knowledge checks

1. How do kernel, distribution, shell and terminal differ?
2. What makes an absolute path different from a relative path?
3. Why should globs be previewed before a destructive command?
4. What are standard input, output and error?
5. What do read/write/execute mean for a directory?
6. How do a process and a service differ?
7. Why can a successful runtime change fail after restart?
8. What account facts must offboarding address?
9. Why use a trusted package repository?
10. How do filesystem, partition and mount point differ?
11. Why are RAID and snapshots not automatically backups?
12. Which layers belong in a basic network troubleshooting path?
13. How do DNS, DHCP and NTP differ?
14. Why can a running service still be unavailable?
15. What separates evidence from a troubleshooting conclusion?
16. How do incident, problem and change management relate?
17. What must a restore test prove?
18. Distinguish RTO from RPO.
19. Compare public, private, hybrid and multicloud.
20. How do IaaS, PaaS and SaaS change responsibility?
21. Compare a VM and a container.
22. How do scalability and elasticity differ?
23. What must a cloud budget account for beyond VM price?
24. Why does a managed service still need customer controls?
25. How do threat, vulnerability and risk relate?
26. Distinguish authentication, authorization and accounting.
27. How do encryption, hashing and signing differ?
28. What makes least privilege more than a small role name?
29. Why does a scan not prove security?
30. What steps follow suspected credential exposure?
31. How should sensitive data be governed through its lifecycle?
32. What turns a compliance requirement into evidence?
33. What does CI validate, and what does CD promote?
34. How do Git working tree, staging and commit differ?
35. Why must a merge conflict be retested?
36. Which controls make a container safer?
37. How does a project differ from operations?
38. Compare functional and non-functional requirements.
39. When does asynchronous architecture help, and what complexity follows?
40. Why does open source still require license review?

41. A file is staged at value 20 and then edited to 30. Which version will a normal commit record, and what does unstaging preserve?
42. Why can the two redirection orders in the stream example produce different destinations for standard error?
43. Does enabling a systemd service guarantee it is running and serving users?
44. Why does adding a tracked file to an ignore rule fail to remove it from history?
45. What is wrong with treating readable source and an SPDX identifier as proof of unrestricted use?
46. How long is the example project with two days of discovery, parallel four/three-day tasks and one day of acceptance, and what assumption could change it?

## Answers and reasoning

1. Kernel manages hardware/resources; distribution packages kernel/userland/policy; shell interprets; terminal presents the session.
2. Absolute starts at `/`; relative is resolved from the current directory.
3. The shell may match more targets than intended; preview bounds scope and protects data.
4. They are the default input stream and normal/error output streams that commands can redirect or pipe.
5. Read lists names, write creates/removes entries and execute traverses/searches the directory, subject to other controls.
6. A process is any running program; a service is a managed background capability, often with startup and health configuration.
7. Runtime state and persistent configuration are different; generated files or unenabled units may be lost.
8. Login/expiry, groups, files, keys/tokens, scheduled jobs, service ownership, audit and retention.
9. Signed metadata, version/dependency tracking and supported updates reduce supply-chain and maintenance risk.
10. Partition allocates disk region, filesystem organizes data and mount attaches it to the directory tree.
11. They may share failure/control plane and can copy corruption; backup needs isolated retention and proven restore.
12. Link/interface, address/prefix, route, DNS, firewall, listener/service, application and return path.
13. DNS resolves names, DHCP assigns network settings and NTP synchronizes time.
14. It may listen incorrectly, fail health, lack permission, be blocked by firewall/DNS/route or have failed dependencies.
15. Evidence is observed state; a conclusion is a tested explanation that accounts for the symptom.
16. Incident restores, problem finds recurring cause and change controls the repair/risk.
17. Integrity, permissions/keys, dependency order, application behavior and achieved recovery time/data point.
18. RTO is targeted restoration time; RPO is tolerated data-loss interval.
19. They describe provider/ownership combinations; hybrid joins private/on-prem and public, multicloud uses multiple providers.
20. The provider manages progressively more layers, but customer identity, data, configuration and usage remain.
21. VM has a guest OS/virtual hardware; container shares host kernel and packages app/userland, usually starting lighter.
22. Scalability handles growth; elasticity adjusts capacity with demand.
23. Licenses, storage/operations, transfer, requests, support, idle resources and recovery/headroom.
24. Managed shifts tasks but customer still configures identities, data, network, backup, observability and use.
25. A threat may exploit a vulnerability; risk combines likelihood and impact to an asset/business outcome.
26. Authenticate proves identity, authorize permits action and accounting records activity.
27. Encryption is reversible with key for confidentiality; hashing is one-way integrity representation; signing uses asymmetric trust for authenticity/integrity.
28. It narrows action, resource, source/condition, time and session, with review and removal.
29. Coverage may be incomplete and a finding still needs exposure, exploitability, impact and remediation validation.
30. Revoke/rotate, contain access, determine scope/use from logs, assess data, recover and add prevention/notification.
31. Classify, minimize, authorize, encrypt, monitor, retain and dispose according to applicable policy/law.
32. Map applicable requirement to control, owner, implementation, protected artifact, test and exception/remediation.
33. CI builds/tests each change; CD promotes the same versioned artifact through controlled environments.
34. Working tree is current files, staging selects the next snapshot and commit records it in history.
35. Resolution can silently change either intent; tests prove the combined behavior.
36. Trusted pinned/scanned image, non-root/minimum capability, scoped network/secrets, resource controls, logs and recreated persistence.
37. Project is temporary with a defined outcome; operations continuously deliver a service.
38. Functional says what behavior; non-functional says quality/constraint such as security, availability or performance.
39. It decouples availability/rate but adds queues, duplicates, ordering, retry, dead-letter and observability needs.
40. Copyright and license obligations still apply to use, modification and distribution; track components and obtain legal guidance.

41. It records the staged value 20 unless staged again. Restoring only staging from HEAD preserves the working-file value 30; inspect the correct diff before committing.
42. Redirections are processed left to right. Copying standard output into standard error before changing standard output preserves the earlier destination.
43. No. Activation configuration, current state and application readiness are distinct. Enable alone does not start; socket/dependency activation and static units add other paths.
44. Ignore rules primarily govern untracked paths; existing tracking and historical commits persist. Untracking a path does not erase history or contain credential exposure.
45. Source visibility alone is not an open-source license grant, and an identifier identifies terms rather than deciding obligations or compatibility. Review the actual license and use/distribution context.
46. Seven days if the two tasks can run independently after discovery. Shared staffing, approvals, rework or additional dependencies can extend the critical path.

## September 2025 baseline checklist

Do not use an older LFCA route without remapping it. The current six domain names remain familiar, but the September 16, 2025 baseline replaces “Supporting Applications and Developers” with **IT Project Management Fundamentals** and explicitly lists project management, application architecture, functional analysis, and open-source software/licensing. LFCA-JP is retired. Verify all six weights and current delivery on the official page.

## Source and freshness notes

- Scope, delivery, prerequisite, validity and exam duration: [official LFCA page](https://training.linuxfoundation.org/certification/certified-it-associate/), checked September 29, 2026.
- Current effective baseline and retired Japanese version: [official September 2025 change notice](https://training.linuxfoundation.org/lfca-program-changes-2025/).
- Course hours and third-party metadata were checked September 29, 2026; access, price, paths and content change.
- Distribution commands, package names, cloud services, security guidance, project practices and license interpretation are verification boundaries. Bash’s GNU-hosted manual timed out during this review; the maintainer-hosted reference and installed runtime supplied the targeted shell evidence.
- Objective snapshot SHA-256: `fd4278c4b59fa86cc2c014f67f60263670b72193b2f83354fa3712b0f97a77cf`.
- This guide uses public scope and independently written labs/checks. It does not reproduce proprietary questions or course content.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one primary route, add hands-on Linux/network/Git/container labs, and close the September 2025 project-management/licensing gap explicitly.

| Resource | Access | Estimated time | Best use and boundary |
|---|---|---:|---|
| [Official LFCA page](https://training.linuxfoundation.org/certification/certified-it-associate/) and [2025 change notice](https://training.linuxfoundation.org/lfca-program-changes-2025/) | Public | 3–5 hours | Map the six weights, delivery and current IT-project domain |
| [Official LFCA curriculum path](https://training.linuxfoundation.org/wp-content/uploads/2024/10/LFCA.pdf) | Public | 30–90 minutes | Choose among suggested free courses; the path estimates 3–6 months overall, not mandatory seat time |
| [LFCA free resources](https://training.linuxfoundation.org/resources/lfca-free-resources/) | Free | 25–60 selected hours estimated | Linux, DevOps/SRE, cloud and open-source foundations; select gaps rather than taking all |
| [Fundamentals of Open Source IT and Cloud Computing (LFS200)](https://training.linuxfoundation.org/training/fundamentals-of-open-source-it-and-cloud-computing-lfs200/) | Paid | 10–15 hours listed plus labs | Official course; public Chapter 11 still uses Supporting Applications and Developers, and its lab page lists Ubuntu 20.04; gap-check current scope and distribution support |
| [Pluralsight LFCA path](https://www.pluralsight.com/paths/linux-foundation-certified-it-associate-lfca) | Paid | 11 hours 47 minutes listed plus labs | One A Cloud Guru course dated August 6, 2025; public outline still says Supporting Applications and Developers, so map the current project domain explicitly |
| [Coursera Learning Linux for LFCA specialization](https://www.coursera.org/specializations/linux-for-lfca-certification/) | Paid/subscription | 59 hours summed from four listed courses | LearnQuest: 16/17/14/12-hour courses; landing estimate is four weeks at ten hours/week, so treat timing as approximate and map current project/licensing scope |

**VERIFY CURRENT:** Public catalogs checked September 29, 2026; paid course interiors, assessments and labs were not accessed. Pluralsight rounds its one-course path to 12 hours; the course row lists 11h47. The curriculum PDF is a one-page suggested route with a 3–6 month estimate and explicitly says its courses are not required. Other study-hour ranges in this table are planning suggestions, not provider seat-time guarantees.

[Canonical’s release table](https://ubuntu.com/about/release-cycle) lists Ubuntu 20.04’s standard security maintenance ending in May 2025, with separate extended coverage. A course’s old VM image is not evidence of current standard support. Select an appropriate supported training release and recheck command differences; this review did not install or upgrade a distribution.

No exact current O’Reilly, MeasureUp or Whizlabs LFCA product was independently verified. Marketplace practice banks vary sharply in quality; use original explanation-led questions only, reject any claim of real/recalled items, and return to the official map for scope.
