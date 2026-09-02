---
exam_code: LFCA
vendor_id: linux-foundation
official_blueprint: https://training.linuxfoundation.org/certification/certified-it-associate/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# LFCA Linux Foundation Certified IT Associate Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#lfca-coverage-record). The [official LFCA page](https://training.linuxfoundation.org/certification/certified-it-associate/) is authoritative.

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

## 2. System administration fundamentals — 30%

### Identities, software, services and storage

Users have numeric UID, primary/supplementary groups, home and shell. Groups simplify shared authorization. Account tools manage creation, membership, password/expiry and removal; offboarding also addresses files, keys, scheduled jobs and service ownership. `sudo` delegates bounded privilege and should be audited; logging in as root for routine work expands risk.

Package managers install signed packages from configured repositories, resolve dependencies and track updates/removal. APT/dpkg and DNF/RPM represent common families. Verify distribution/release, repository trust, architecture, configuration changes and whether a service restart or reboot is needed. Do not pipe an unreviewed Internet script into a privileged shell.

Service managers start, stop, restart, reload, enable and inspect units. “Active” means a process/unit state, not necessarily that users can reach a healthy application. Check configuration, logs, listening socket, identity/permissions, firewall and a real request. Schedule recurring work with cron or timers while defining identity, environment, working directory, output and failure handling.

Disks contain partitions or logical volumes; filesystems organize data; mounts attach a filesystem to the tree. Use capacity tools to distinguish block space from inode/file-count exhaustion. Backups are copies retained for recovery; snapshots and RAID can support operations but are not automatically independent backups. Protect and periodically restore-test data plus configuration, keys and documentation.

### Networking

A host needs an address and prefix, route/default gateway and usually DNS resolver. IPv4 uses dotted decimal; a subnet/prefix divides network and host portions. MAC addresses identify local link interfaces; ARP/neighbor discovery resolves local delivery. Switches forward within a network, routers move between networks, firewalls filter traffic, and NAT translates addresses/ports.

DNS maps names to records; DHCP supplies address configuration; NTP synchronizes time. Common application protocols include HTTP/HTTPS, SSH, SMTP, DNS and DHCP; use secure alternatives and current documentation rather than memorizing a port without purpose. Diagnose from link/interface → address/prefix → route → DNS → firewall → listening service → application and return path. Compare a name with a direct address to isolate DNS.

### Monitoring, troubleshooting and recovery

Observe CPU/load, memory/swap, disk capacity/latency, network state, processes, services and logs. A high value is evidence, not cause: CPU can be busy because of valid load, memory can be cache, and a full filesystem can be blocks, inodes or deleted-open data. Correlate time, workload, recent change and user impact.

Troubleshoot by defining expected/actual behavior, scope, time, impact and recent changes; gather evidence; form a theory; test the least-invasive discriminator; plan rollback; make one controlled change; validate direct and dependent behavior; document root cause and prevention. Preserve evidence before rebooting or deleting.

Disaster recovery begins with business priorities, RTO (target restoration time) and RPO (tolerated data-loss window). Recovery needs protected copies, access, dependencies, capacity and rehearsed runbooks. Business continuity keeps critical outcomes operating; high availability reduces interruption; neither replaces backup.

> **Related item:** Incident recovery restores service; problem management finds recurring cause; change management controls the repair and its risk.

## 3. Cloud computing fundamentals — 18%

Cloud computing supplies shared, network-accessed resources with self-service, elasticity and measured consumption. Public, private, hybrid and multicloud describe deployment relationships. IaaS exposes virtual infrastructure; PaaS manages more runtime; SaaS supplies an application; FaaS/serverless runs event-driven code. Shared responsibility changes by service: the provider secures underlying infrastructure while the customer retains identities, data, configuration and usage responsibilities.

Virtual machines emulate hardware and run guest operating systems. Containers package applications and dependencies while sharing the host kernel. Images are templates; containers are runtime instances; volumes preserve data; orchestration schedules and recovers workloads. Serverless reduces server administration but still requires secure identity, input, dependency, data, logging and cost controls.

Availability zones/failure domains separate faults; load balancing distributes healthy traffic; horizontal scaling adds instances and vertical scaling enlarges one. Elasticity adjusts capacity with demand. Performance involves latency, throughput, IOPS, CPU, memory and dependency behavior. Redundancy is useful only when health detection, data consistency and failover are designed and tested.

Cloud virtual networks still use addresses, subnets, routes, DNS, firewalls/security groups, load balancers and VPN/private connectivity. Follow traffic end to end. Cloud cost includes resource size/time, licenses, storage, operations/requests and data transfer. Use budgets, alerts, tags, rightsizing, schedules, autoscaling and lifecycle tiers; deleting unknown resources purely to reduce cost is unsafe.

> **Related item:** “Managed” moves tasks to a provider; it does not remove architecture, configuration, security, data or recovery decisions.

## 4. Security fundamentals — 14%

Confidentiality limits disclosure, integrity prevents/detects unauthorized change, and availability keeps authorized use possible. Risk connects asset value, threat, vulnerability, likelihood and impact. Controls may be preventive, detective, corrective, deterrent, compensating or recovery-oriented and may be administrative, technical or physical. Defense in depth uses independent layers.

Authentication proves identity; authorization permits action; accounting records it. Prefer least privilege, groups/roles, MFA, secure recovery and separate administrative identities. Passwords should be long/unique and stored through one-way password hashing; secrets/keys require protected storage and rotation. Encryption protects readable data with keys, while hashing supports integrity; digital signatures support integrity/authenticity and certificates bind keys to identities through trust.

Harden by using supported software, timely patches, minimal services, safe configuration, secure remote access, firewalling, malware controls, logging and tested backup. Phishing and social engineering target human trust; verify requests out of band and report them. Vulnerability scanning finds potential issues; validate exposure and remediate according to risk rather than assuming a scan equals security.

Classify sensitive data, collect the minimum, restrict access, encrypt appropriately, define retention and dispose safely. Compliance begins by identifying applicable law, contract, policy or framework, then mapping requirements to controls, evidence, tests and accountable owners. Privacy concerns appropriate collection/use and individual rights according to jurisdiction. Escalate legal interpretation.

Incident response prepares, detects/analyzes, contains, eradicates, recovers and learns. Preserve relevant logs and timestamps; do not destroy evidence to make a symptom disappear.

## 5. DevOps fundamentals — 12%

DevOps connects development and operations through collaboration, feedback, automation, shared responsibility and small reliable change. CI builds and tests each change; delivery/deployment promotes a versioned artifact through environments. A pipeline commonly includes source, build, test/security checks, artifact, approval, deploy, observe and rollback. Automation should be repeatable, least privilege, logged and tested.

Git is distributed version control. A repository holds history; a working tree contains current files; staging selects the next commit. Use `clone`, `status`, `diff`, `add`, `commit`, `log`, branch, merge, fetch/pull and push conceptually and in a lab. A branch isolates work; a merge combines histories; conflicts require understanding and retesting. Do not commit secrets, huge generated files or unclear binary artifacts.

Containers support consistent packaging but are not automatically secure or stateless. Pin trusted images, scan dependencies, use non-root and minimum capability, externalize configuration/secrets, set resource limits, restrict networks and recreate to prove persistence. Orchestration provides desired replicas, health, networking, storage, configuration and rollout behavior.

Monitoring supplies metrics/logs/events; feedback connects production behavior to planning. Reliable change includes small batches, peer review, automated tests, immutable artifacts, gradual rollout, rollback and learning—not only speed.

> **Related item:** DevOps is a socio-technical operating model. A tool purchase cannot replace ownership, communication or safe change practice.

## 6. IT project management fundamentals — 10%

A project has a defined outcome, stakeholders, scope, constraints, plan, risks, dependencies, resources and acceptance criteria. Initiation clarifies value and sponsor; planning defines work/schedule/budget/risk; execution produces deliverables; monitoring controls variance/change; closure obtains acceptance and captures lessons. Operations are ongoing; a project is temporary.

Waterfall-style work sequences phases and suits stable requirements; iterative/incremental approaches deliver and learn in smaller steps; Agile values collaboration and response to change. Scrum commonly uses product backlog, sprint, product owner, Scrum Master and team; Kanban visualizes flow and work-in-progress. Methods are tools, not guarantees.

Functional requirements describe behavior; non-functional requirements describe qualities such as availability, performance, security, usability and maintainability. Functional analysis identifies actors, workflows, inputs/outputs, rules, exceptions and acceptance. Trace a requirement to design, implementation, test and outcome. Uncontrolled scope change affects schedule, cost, risk and quality.

Application architecture may be monolithic or service-oriented/microservice, layered, client-server, event-driven or serverless. Compare coupling, deployment, data consistency, operational complexity and failure modes. APIs define contracts between components; synchronous communication couples response time/availability, while asynchronous queues decouple at the cost of ordering/retry/observability complexity.

Open source makes source available under a license; it does not mean no copyright, no obligations or zero cost. Permissive and copyleft licenses impose different conditions. Track components, notices, source/attribution/distribution obligations and security maintenance; obtain qualified legal guidance for license decisions. Communities use governance, contribution processes and codes of conduct.

## Integrated scenarios

### Scenario 1: Small web service fails after an update

Confirm user symptom, scope and change. Check host capacity, service state/logs, package/configuration, port, permissions, firewall, DNS and a local request. Roll back or repair with approval, validate security and dependent access, then update the change record and add a pre-deployment test. This connects Linux, administration, networking, security and DevOps.

### Scenario 2: Move a community application to cloud

Capture functional and non-functional requirements, data sensitivity, dependencies, availability and budget. Choose service/deployment model and responsibility owners, design network/identity/backup/monitoring, estimate cost, pilot and test failure/restore. Record open-source licenses and user acceptance. Do not assume cloud automatically improves security or availability.

### Scenario 3: Lost laptop and exposed repository token

Report the incident, revoke/rotate the token, inspect audit/repository/pipeline logs for use, protect accounts with MFA and scope, assess sensitive data, and follow notification/evidence policy. Restore work from trusted remote history or backup, validate artifacts, document lessons and add secret scanning/device encryption. Deleting a local file alone is not containment.

## Hands-on labs

1. **Linux tour:** install a disposable Ubuntu or Fedora-family VM; identify kernel/distribution, filesystem purposes, users/groups, processes, packages, services and logs.
2. **Command-line evidence:** create a lab tree; navigate, search, filter, redirect, archive, set permissions/ownership and use help; preview and safely remove only the lab path.
3. **Administration:** create a user/group, install a trusted package, configure a simple service, inspect logs/socket, schedule a health check, restart and confirm persistence; clean up.
4. **Network break/fix:** record address/route/DNS/listeners, serve a test page privately, introduce one safe DNS/firewall/service fault at a time and troubleshoot through the layer sequence.
5. **Backup/recovery:** archive sample data and configuration, record checksum/permissions, delete the working copy in the lab, restore to a new location and validate integrity and elapsed time.
6. **Cloud comparison:** diagram one small workload as local VM, IaaS VM, managed platform and container; map responsibility, failure domains, networking, security, backup and cost drivers.
7. **Git/container delivery:** version a small static app, branch/change/merge it, build or run a non-root container with external configuration and a volume, inspect logs and recreate it.
8. **Project capstone:** write users, functional/non-functional requirements, risks, milestones, acceptance tests, architecture, open-source inventory and incident/recovery plan for the sample application.

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

## September 2025 baseline checklist

Do not use an older LFCA route without remapping it. The current six domain names remain familiar, but the September 16, 2025 baseline replaces “Supporting Applications and Developers” with **IT Project Management Fundamentals** and explicitly lists project management, application architecture, functional analysis, and open-source software/licensing. LFCA-JP is retired. Verify all six weights and current delivery on the official page.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one primary route, add hands-on Linux/network/Git/container labs, and close the September 2025 project-management/licensing gap explicitly.

| Resource | Access | Estimated time | Best use and boundary |
|---|---|---:|---|
| [Official LFCA page](https://training.linuxfoundation.org/certification/certified-it-associate/) and [2025 change notice](https://training.linuxfoundation.org/lfca-program-changes-2025/) | Public | 3–5 hours | Map the six weights, delivery and current IT-project domain |
| [Official LFCA curriculum path](https://training.linuxfoundation.org/wp-content/uploads/2024/10/LFCA.pdf) | Public | 30–90 minutes | Choose among suggested free courses; the path estimates 3–6 months overall, not mandatory seat time |
| [LFCA free resources](https://training.linuxfoundation.org/resources/lfca-free-resources/) | Free | 25–60 selected hours estimated | Linux, DevOps/SRE, cloud and open-source foundations; select gaps rather than taking all |
| [Fundamentals of Open Source IT and Cloud Computing (LFS200)](https://training.linuxfoundation.org/training/fundamentals-of-open-source-it-and-cloud-computing-lfs200/) | Paid | 10–15 hours listed plus labs | Official aligned course; use a current distribution rather than its Ubuntu 20.04 lab example alone |
| [Pluralsight LFCA path](https://www.pluralsight.com/paths/linux-foundation-certified-it-associate-lfca) | Paid | 11 hours 47 minutes listed plus labs | Coherent six-part course updated August 2025; gap-check the September project-management domain wording |
| [Coursera Learning Linux for LFCA specialization](https://www.coursera.org/specializations/linux-for-lfca-certification/) | Paid/subscription | 35–70 hours estimated | Deeper Linux practice; supplement cloud, security, DevOps and current project/licensing scope |

No exact current O’Reilly, MeasureUp or Whizlabs LFCA product was independently verified. Marketplace practice banks vary sharply in quality; use original explanation-led questions only, reject any claim of real/recalled items, and return to the official map for scope.

## Source and freshness notes

- Scope, delivery, prerequisite, validity and exam duration: [official LFCA page](https://training.linuxfoundation.org/certification/certified-it-associate/), checked September 1, 2026.
- Current effective baseline and retired Japanese version: [official September 2025 change notice](https://training.linuxfoundation.org/lfca-program-changes-2025/).
- Course hours and third-party metadata were checked September 1, 2026; access, price, paths and content change.
- Distribution commands, package names, cloud services, security guidance, project practices and license interpretation are verification boundaries.
- Objective snapshot SHA-256: `fd4278c4b59fa86cc2c014f67f60263670b72193b2f83354fa3712b0f97a77cf`.
- This guide uses public scope and independently written labs/checks. It does not reproduce proprietary questions or course content.
