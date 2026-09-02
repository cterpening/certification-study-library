---
exam_code: 220-1202
vendor_id: comptia
official_blueprint: https://www.comptia.org/en-us/certifications/a/core-2-v15/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-01
---

# 220-1202 CompTIA A+ Core 2 (V15) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#220-1202-coverage-record). The [official Core 2 V15 page](https://www.comptia.org/en-us/certifications/a/core-2-v15/) is authoritative.

**Current baseline:** A+ V15, Core 2 exam 220-1202; launched March 25, 2025<br>
**Version rule:** Core 1 and Core 2 must be passed from the same version; do not mix 1200- and 1100-series exams<br>
**Lifecycle watch:** No exact retirement date is announced. CompTIA says usually three years after launch and estimates 2028; verify before scheduling.<br>
**Official delivery snapshot:** Maximum 90 questions, including multiple-choice, drag-and-drop, and performance-based questions; 90 minutes; 700/900 passing score; English, German, and Japanese listed

## How to use this guide

Core 2 is the operating-system, security, software-repair, and support-process half of A+. Its central skill is controlled change: understand current state, protect data and evidence, choose the correct tool/control, make the smallest authorized repair, validate the full workflow, then document and communicate.

Build disposable Windows, Linux, and—where legitimately available—macOS/mobile practice environments. Keep clean snapshots or reinstall media, non-sensitive test accounts/files, and a ticket log. For each objective:

1. identify the platform, symptom, user impact, recent change, and security/data risk;
2. inspect with native tools and record a baseline;
3. back up or preserve evidence before a destructive action;
4. implement one authorized change or escalate;
5. verify function, security, persistence/restart, recovery, and user outcome.

Core 1 hardware/network concepts remain prerequisites for many symptoms. A software fix cannot repair a failing drive, and a network complaint can be DNS, identity, application, VPN, proxy, firewall, or endpoint security.

## Weighted objective map

| Domain | Weight | Readiness evidence |
|---|---:|---|
| 1. Operating systems | 28% | Select/install/configure Windows, understand macOS/Linux/mobile, use tools/commands, storage/filesystems, applications, and networking |
| 2. Security | 28% | Apply identity, permissions, hardening, wireless/SOHO/browser/mobile controls, malware response, encryption, and disposal |
| 3. Software troubleshooting | 23% | Diagnose Windows/application/mobile/performance/security symptoms without destroying evidence or data |
| 4. Operational procedures | 21% | Use tickets/docs/change, backups/recovery, safety/environment, policy/licensing/privacy, professional communication, scripting, and remote support |

## 1. Operating systems — 28%

### Choose and install the right OS

Match edition and platform to hardware support, CPU architecture, application/driver needs, domain/enterprise management, encryption/virtualization features, lifecycle/support, licensing, user accessibility, and security. Windows, macOS, Linux distributions, ChromeOS, iOS/iPadOS, Android, and embedded systems have different update, installation, management, and application models. “Runs today” is not sufficient if the release is unsupported or lacks the required business control.

Before installation or upgrade, inventory hardware/firmware compatibility, storage and free space, drivers, applications, accounts/keys, encryption/recovery material, network, licensing, user data, and rollback. Clean installation, in-place upgrade, repair/reset/recovery, image deployment, and network installation have different preservation and risk boundaries. Verify boot mode and partitioning; do not delete/format an unknown disk before protecting data.

File systems have capability and compatibility differences. NTFS supports Windows permissions and features; FAT32/exFAT trade capability for broad/removable compatibility; APFS and ext-family systems serve their platforms. GPT and MBR describe partitioning structures, not file systems. Permissions, ownership, encryption, journaling, maximum sizes, and boot support are distinct.

### Windows tools and configuration

Know why you would open each tool, not only its name:

| Tool area | Evidence or action |
|---|---|
| Task Manager / Resource Monitor / Performance Monitor | processes, startup, CPU/memory/disk/network pressure and time-based counters |
| Event Viewer / Reliability Monitor | correlated errors, warnings, crashes, updates, and timeline |
| Services / Task Scheduler | service state/startup/dependencies and scheduled actions |
| Device Manager | detected devices, driver/status, enable/disable/rollback/update |
| Disk Management | disks, partitions/volumes, letters, status; destructive risk requires care |
| System Configuration / startup settings | controlled boot/startup diagnosis |
| System Information / DirectX tools | hardware, firmware, drivers, graphics/audio context |
| Settings / Control Panel / MMC consoles | platform configuration, users, network, security, applications |
| Registry Editor / Group Policy tools | advanced configuration; export/backup and scope before change |

At the command line, recognize navigation and file commands, `ipconfig`, `ping`, `tracert`, `nslookup`, `netstat`, `hostname`, `whoami`, process/task tools, `sfc`, `dism`, disk/check utilities, `gpupdate`/`gpresult`, shutdown, and package or update tooling where in scope. Understand whether a command reads or changes state, required privilege, target path/host, output evidence, and rollback. Never run a memorized destructive command on an unknown target.

Configure local users/groups, sign-in, permissions/shares, mapped resources, printers, applications/defaults, updates, time/region, power, accessibility, display, and Windows networking. Distinguish local account, workgroup, domain, and cloud/work identity. Share permissions and file-system permissions can both affect effective access.

### macOS, Linux, and mobile basics

On macOS, recognize Finder, System Settings, Activity Monitor, Disk Utility, Terminal, Keychain, Time Machine, force quit, file permissions, application packages, and update/recovery concepts. On Linux, recognize shell, package management, files/directories, permissions/ownership, processes/services, logs, networking, mounts, desktop utilities, and repository trust. Commands and paths vary by distribution/version; use local help and current documentation.

On mobile OSs, understand application stores/sideloading policy, permissions, accounts/synchronization, radios, notifications, location, storage, updates, backup/reset, screen lock/biometrics, and management profiles. Preserve authentication/recovery and backup state before reset.

> **Related item:** Desired-state management can enforce settings at scale, but a technician must still distinguish local state from policy that will reapply after the next sync.

## 2. Security — 28%

### Threats, vulnerabilities, and social engineering

Threats include malware, credential attacks, social engineering, malicious insiders, vulnerable/unpatched software, misconfiguration, lost devices, unsafe wireless, physical access, and data exposure. Virus/worm/trojan/ransomware/spyware/rootkit/keylogger/bot behavior overlaps; identify symptoms and response needs rather than relying only on labels.

Phishing can arrive by email, text, voice, QR code, social platform, search ad, or collaboration system. Urgency, authority, fear, reward, unexpected attachment/link, unusual payment/reset request, or MFA prompt should trigger independent verification. Do not “test” a suspicious link on a production endpoint.

### Identity, permissions, encryption, and hardening

Authentication proves identity; authorization grants actions; accounting/audit records them. Use long unique passwords in a password manager, MFA with independent factors, least privilege, separate admin/standard use, appropriate lockout/session lock, and secure recovery. Biometrics are convenient but need fallback and privacy consideration.

File/share permissions, user/group membership, inheritance, ownership, and elevated tokens affect access. Grant a group the minimum required rights instead of individually accumulating permissions. Test allowed and denied cases as the intended identity.

Encryption at rest protects storage if a device/media is lost; encryption in transit protects communications. Manage keys/recovery credentials separately and test recovery. TPM/secure boot, supported OS, updates, host firewall, anti-malware/endpoint protection, application control, screen lock, disabled unnecessary services, trusted software sources, backups, and logging form layers. No single control is “secure.”

Secure Wi-Fi/SOHO with supported modern encryption, strong unique admin credentials, updated firmware, safe remote management, guest/IoT separation, controlled port forwarding, DNS/network settings, and configuration backup. Harden browsers through updates, safe extensions, site permissions, HTTPS/certificate awareness, download controls, popup/tracking/privacy choices, cache/cookie understanding, and password protection. Private browsing is not anonymity.

Mobile/embedded security includes updates, lock/biometrics, encryption, account/MFA, permission review, trusted store/source, backup, location/remote lock/wipe under policy, and safe disposal. Remote wipe needs connectivity and does not replace encryption or inventory.

### Malware response and disposal

Follow policy: identify symptoms and scope; isolate/quarantine when appropriate; preserve/report evidence; disable recovery mechanisms only if the approved procedure requires; update tools/signatures; scan/remediate; schedule boot/offline scanning if needed; restore or reimage from trusted sources; patch and harden; re-enable protection; verify accounts/data/network; educate and document. Do not promise that deleting one file proves eradication.

Data destruction must match media, sensitivity, policy, and legal requirements: clear/overwrite or cryptographic erase where supported, purge/degauss for appropriate magnetic media, or physically destroy through approved processes. Formatting and deleting are not universally secure erasure. Retain chain-of-custody/disposal evidence.

> **Related item:** Incident response and ordinary troubleshooting diverge when evidence, containment, notification, or legal obligations matter. Preserve before “fixing” when compromise is plausible.

## 3. Software troubleshooting — 23%

Use symptoms to select evidence. A blue screen/kernel failure suggests stop code, dump/event, driver/hardware/update history. Slow startup suggests startup items, services, resources, storage health/capacity, update/malware and profile evidence. A frozen app suggests process/resource/event/log and dependency state. Boot failure suggests firmware/boot loader/system files/storage/update; repeated popups or redirected browser suggests unwanted software, extensions, DNS/proxy, notifications, or compromise.

### Windows and application path

1. Establish scope: one user, one app, one device, or many.
2. Capture exact error/time/reproduction and recent changes.
3. Check resource, disk, event/reliability, service/process, update/driver, network/DNS, permissions, and security evidence.
4. Test safe modes, clean boot, alternate user, known-good file/profile/network, repair tool, update/rollback, or reinstall in a controlled sequence.
5. Use restore/recovery/reset/reimage only after data, encryption keys, licenses, and rollback implications are understood.
6. Reboot where required, repeat the original workflow, check security and logs, and document.

Application failures can come from compatibility/architecture, missing runtime/dependency, permissions, damaged configuration/profile/cache, network/service, resource limit, security control, update, or corrupted installation/data. Reinstalling first may remove logs/settings and not fix external dependencies.

### Mobile and security symptoms

For mobile apps: verify storage, memory/battery/thermal state, OS/app version, permissions, account/sync, network/VPN, service status, cache/data, and management policy before reset. For battery drain or overheating, isolate app/radio/screen/background activity and physical battery risk. For failed rotation, sound, notifications, or location, inspect both OS and app controls.

Compromise indicators include changed browser settings, unexpected apps/extensions/admins, popups, high resource/network use, disabled protection, account alerts, encryption/ransom note, altered files, certificates/proxy/DNS changes, or unauthorized location/camera/microphone access. Isolate and escalate per policy; do not log in broadly from a suspected system.

> **Related item:** Correlation is stronger than coincidence. Align user report, event time, deployment/update, process, network and security telemetry before declaring root cause.

## 4. Operational procedures — 21%

### Tickets, documentation, and change

A useful ticket records requester/contact, asset/system, exact symptom/error, impact/urgency, time, environment, recent changes, reproduction, evidence, actions/results, escalation, resolution, validation, and closure communication. Separate observed fact from user report, hypothesis, and action. Protect sensitive data; do not paste passwords, tokens, private records, or unnecessary logs.

Asset inventories, network diagrams, knowledge bases, standard operating procedures, acceptable-use/security policies, and incident records reduce repeated discovery. Keep owner, version, date, scope, and rollback/current-state information.

Change management defines reason, scope, risk/impact, affected assets/users, dependencies, approval, schedule/window, communication, implementation, testing, rollback, documentation, and review. An emergency can shorten the path but should not erase accountability.

### Backup, recovery, safety, and environment

Full, incremental, differential, file-level, image/system, snapshot, local, network, and cloud backups have different restore chains and failure domains. Define recovery-point and recovery-time needs; encrypt and restrict backups; monitor jobs; keep an independent/offline/offsite copy appropriate to risk; test file and full-system restoration. Synchronization, RAID, snapshots, and availability are not automatically backups.

Use ESD protection, power isolation, correct lifting, cable management, PPE, ventilation, and safety data guidance for chemicals/consumables. Never open a PSU or CRT/high-voltage equipment without qualifications. Handle swollen batteries, toner, solvents, and electronic waste through approved processes. Environmental controls include temperature, humidity, dust, airflow, power quality, noise, and responsible recycling/disposal.

Privacy, data handling, acceptable use, prohibited content/activity, licensing, intellectual property, and regulatory/policy obligations control what a technician may view, copy, retain, install, or report. Technical access is not permission. Minimize exposure and use chain of custody when required.

### Communication, scripting, and remote support

Listen, clarify, avoid jargon/blame, set honest expectations, communicate delays, protect confidentiality, and confirm resolution with the user. Handle difficult interactions calmly and escalate threats, discrimination, unsafe or policy-sensitive requests appropriately. Never invent certainty or criticize prior staff to the user.

Recognize basic script elements in PowerShell, shell, batch, JavaScript, Python or platform tools: interpreter, comments, variables, conditionals, loops, parameters, environment variables, file/network/process operations, errors, and output. Read before running; confirm author/source, target, privilege, secrets, input validation, idempotence, logging, rollback, and a test environment. Do not download-and-execute unknown scripts.

Remote support options include screen sharing/assistance, remote desktop, SSH, VPN, management agents, and ticket/collaboration tools. Confirm identity/consent, use approved encrypted tools and least privilege, communicate visible actions, protect clipboard/files/credentials, disconnect/close access, and document. Unsolicited remote-support calls are a common scam pattern.

> **Related item:** A blameless review asks which system/process controls allowed recurrence. It improves reliability without hiding individual accountability for unsafe choices.

## Integrated scenarios

### Scenario 1: Failed update and encrypted laptop

A managed laptop boot-loops after an update. Confirm user/asset, backup and encryption recovery key, exact boot/error state, storage health, and recent deployment. Use approved recovery/safe-mode tools, rollback or repair only after data protection, validate sign-in/apps/network/security/update state after reboot, document, and link the broader change incident.

### Scenario 2: Suspected account and browser compromise

A user sees popups and unexpected MFA prompts. Isolate as policy requires, preserve URLs/times/alerts, verify the account from a trusted device, revoke sessions/reset credentials with MFA review, inspect extensions/proxy/DNS/apps/protection, scan or reimage according to confidence, restore trusted data, patch/harden, validate, report, and educate without blame.

### Scenario 3: Remote new-hire setup

Choose a supported OS/edition, install from trusted media/image, partition and encrypt, apply identity/least privilege, updates/security baseline, VPN/remote support, applications/licensing, backup, privacy settings, accessibility and documentation. Use a change/ticket record and test standard-user work, denied admin action, recovery, and secure remote-support closure.

## Hands-on labs

1. **Multi-OS inventory:** compare supported Windows, Linux and available macOS/mobile tools, filesystems, package/apps, permissions, updates, processes/logs, network and recovery.
2. **Windows native tools:** capture a baseline with Task Manager, Event Viewer, services, Device/Disk Management, system info and safe read commands; map each output to a support question.
3. **Install/recovery:** perform a clean disposable OS install or scripted simulation, handle partition/filesystem/driver/update/user setup, then restore a file and system state.
4. **Permissions and hardening:** configure standard/admin users, groups, file/share access, firewall, encryption/recovery, updates, browser and Wi-Fi settings; test allowed and denied paths.
5. **Malware-response tabletop/lab:** use benign test indicators in an isolated VM to practice detection, isolation, evidence, scan/reimage decision, recovery, hardening and reporting.
6. **Software/mobile faults:** inject safe startup, service, profile/cache, DNS/proxy, permission or mobile-app settings faults and diagnose one variable at a time.
7. **Operations packet:** write a ticket, asset/change record, knowledge article, backup/restore proof, privacy-safe evidence, user update, escalation and rollback plan.
8. **Remote-support capstone:** obtain consent, connect through an approved lab tool, run a pre-read safe script or manual repair, protect credentials/data, validate, disconnect and document.

## Original knowledge checks

1. Why must 220-1202 be paired with 220-1201 rather than 220-1101?
2. Which requirements determine a Windows edition or alternate OS choice?
3. What must be protected before deleting partitions or resetting an OS?
4. Distinguish GPT/MBR from NTFS/APFS/ext4.
5. Which tool best supplies a crash/update timeline rather than live utilization?
6. Why is Registry Editor a high-risk first action?
7. What should be known before running a command with administrative privilege?
8. How can share and file-system permissions combine?
9. Which Linux evidence parallels Windows process/service/event inspection?
10. Why can management policy undo a local mobile or desktop change?
11. Distinguish authentication, authorization, and auditing.
12. Why use a separate standard and administrative context?
13. What does full-disk encryption not protect after sign-in?
14. Which controls complement encryption on a lost laptop?
15. Why is private browsing not anonymity?
16. What should happen after an unexpected MFA prompt?
17. Why can deleting one malware file be insufficient?
18. When should incident evidence be preserved before repair?
19. Why is formatting not universal secure erasure?
20. Which evidence separates one-user application failure from system-wide failure?
21. What can a clean boot or alternate profile isolate?
22. Why can immediate reinstallation weaken diagnosis?
23. Which evidence should precede OS reset for a slow computer?
24. How can DNS/proxy change appear as a browser infection?
25. Which mobile checks precede factory reset?
26. What makes overheating a safety issue rather than only performance trouble?
27. What separates observation, report, hypothesis, and action in a ticket?
28. Which secrets should never be pasted into a ticket?
29. What belongs in a safe change record?
30. Distinguish full, incremental, and differential restore chains.
31. Why are sync, RAID, and snapshots not automatically backups?
32. What proves that a recovery plan works?
33. Which hardware conditions require immediate stop/escalation?
34. Why is technical access not permission to inspect user data?
35. How should a technician communicate an uncertain completion time?
36. Which script properties must be reviewed before execution?
37. Why are secrets in command history or scripts risky?
38. What consent and closure evidence belongs in remote support?
39. What makes the compromise scenario complete after malware removal?
40. What exactly is announced about 220-1202 retirement?

## Answers and reasoning

1. CompTIA prohibits mixing versions; both V15 component exams are required.
2. Hardware, apps/drivers, management/domain, features, support lifecycle, license, accessibility and security.
3. User data, backup/restore proof, encryption/recovery keys, licenses, accounts and rollback state.
4. GPT/MBR organize partitions; the others organize files/data inside volumes.
5. Event Viewer and Reliability Monitor provide time-correlated history; live tools complement them.
6. It can broadly change system/application behavior and lacks automatic safe intent; back up and target precisely.
7. Source, exact target, read/write effect, parameters, output, required rights, risk, rollback and authorization.
8. Effective access is constrained by applicable layers and group/inheritance/deny behavior.
9. Process tools, service manager, journal/syslog/application logs, package history and network commands.
10. Desired state can reapply centrally governed configuration on synchronization.
11. Prove identity, decide permitted actions, and record activity.
12. It limits routine exposure and makes elevation an explicit controlled event.
13. Malware or an unauthorized person using an unlocked authenticated session can read accessible data.
14. Screen lock, MFA/account controls, remote action policy, inventory, backup and prompt loss reporting.
15. It mainly reduces local browsing traces; sites, accounts, networks and providers can still observe activity.
16. Deny, inspect from a trusted device, secure credentials/sessions if needed, and report.
17. Persistence, additional payloads, changed settings/accounts, stolen credentials or corrupted trust may remain.
18. Whenever compromise, policy/legal notification, chain of custody, or root-cause evidence may matter.
19. It may leave recoverable data and differs by media/controller; use an approved clear/purge/destroy method.
20. Alternate user/device/app/file tests plus service/resource/log/network evidence.
21. Third-party startup/service effects versus profile-specific configuration/data.
22. It can erase logs/configuration, user data and root-cause evidence without fixing external dependencies.
23. Resource/time trends, storage health/capacity, startup/processes, logs/updates, malware and thermal/hardware evidence.
24. It redirects or blocks destinations outside the browser content while resembling hijacking.
25. Storage/resources, OS/app version, permission, account/sync, network/VPN, service, cache and policy, plus backup/recovery.
26. A damaged/swollen battery or excessive heat can cause injury/fire and requires approved handling.
27. Label who observed what, what was alleged, what theory was tested, and what change/result occurred.
28. Passwords, tokens, private keys, full sensitive records, recovery codes and unnecessary personal content.
29. Reason/scope, risk/impact, approval, window/communication, steps, dependencies, tests, rollback, owner and review.
30. Full restores one set; incremental needs full plus every later increment; differential needs full plus latest differential.
31. They share deletion/corruption/system failures or serve availability/state needs rather than independent recovery.
32. A monitored successful restore meeting required recovery point/time with usable applications/data.
33. Swollen/hot/leaking batteries, smoke/odor, exposed high voltage, damaged power, unsafe chemicals or unqualified CRT/PSU work.
34. Privacy, policy, consent, scope and legal purpose still restrict access.
35. State known evidence, next action, honest range/checkpoint, impact/workaround and escalation—never invent certainty.
36. Trusted author/source, target, inputs, privilege, destructive/network behavior, secrets, validation, logging, idempotence and rollback.
37. They can leak through files, repositories, logs, process inspection, backups or shell history.
38. Verified identity/consent, approved tool/session, actions/files transferred, validation, disconnection/access closure and communication.
39. Account/session recovery, eradication/reimage confidence, trusted restore, patch/hardening, validation, notification, education and documentation.
40. No exact date; the page says usually three years after launch and estimates 2028.

## 220-1102-to-220-1202 gap checklist

Map older content line by line to V15. Verify current Windows editions/features/tools/commands and supported lifecycle, macOS/Linux/mobile behavior, installation/recovery and file systems, MFA/passkeys/identity and current wireless/browser/SOHO controls, modern threats and malware response, mobile/application/security symptoms, ticket/change/backup/privacy/licensing expectations, scripting and approved remote support. Do not combine an older 1101 or 1102 pass with a V15 component.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Select one V15 path, practice on disposable multi-OS systems, and use one explanation-led assessment to guide remediation.

| Resource | Access | Estimated time |
|---|---|---:|
| CompTIA [CertMaster Learn](https://www.comptia.org/en-us/resources/certmaster-training/learn/), Labs, and Practice | Paid official platform; select exact 220-1202 product/bundle | About 35–70 hours across learning, labs, and remediation |
| [Pluralsight A+ Core 2 path](https://www.pluralsight.com/paths/comptia-a-core-2-220-1202) | Subscription; 5 courses and practice exam | 12 listed hours plus 20–40 lab/review hours |
| [LinkedIn Learning / Total Seminars Core 2](https://www.linkedin.com/learning/comptia-a-plus-core-2-220-1202-cert-prep) | Subscription; 22 quizzes | 21 hours 45 minutes plus 20–40 lab/review hours |
| [Complete A+ Guide V15](https://www.oreilly.com/library/view/complete-a-guide/9780135439883/) | O'Reilly/Pearson subscription book covering both cores | About 25–45 selected reading/lab hours for Core 2 |
| [Udemy / Jason Dion Core 2](https://www.udemy.com/course/comptia-a-core-2/) | Paid marketplace course and practice exam | Verify current runtime; allow 25–50 hours plus labs/review |
| [MeasureUp Core 2](https://www.measureup.com/comptia-a-core-2-practice-test.html) | Paid explanation-led practice | About 6–12 hours across attempts and review; verify current bank size |
| [Professor Messer free 220-1202 course](https://www.professormesser.com/free-a-plus-training/220-1202/220-1202-video/220-1202-training-course/) | Free 74-video course; optional paid notes/practice | 13 hours 41 minutes plus 20–40 hands-on hours |

No exact Whizlabs 220-1202 route was independently verified. Reject “actual questions” and dumps. Provider durations, prices, bundles, banks, updates, and access are volatile.

## Source and freshness notes

- CompTIA controls the V15 weights, delivery, score/languages, same-version rule, and estimated lifecycle.
- OS versions/support, utilities/commands, threats, security recommendations, remote tools, licensing and privacy requirements change. Verify implementation against current vendor and organizational documentation.
- This guide contains original scenarios, labs, checks, and explanations from public scope; it does not copy proprietary objectives, PBQs, course labs, or exam items.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.
