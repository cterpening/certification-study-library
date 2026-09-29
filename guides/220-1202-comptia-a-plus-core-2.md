---
exam_code: 220-1202
vendor_id: comptia
official_blueprint: https://www.comptia.org/en-us/certifications/a/core-2-v15/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-28
---

# 220-1202 CompTIA A+ Core 2 (V15) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 28, 2026. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#220-1202-coverage-record). The [official Core 2 V15 page](https://www.comptia.org/en-us/certifications/a/core-2-v15/) is authoritative.

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

**CURRENT BLUEPRINT:** The official page summarizes scope in 11 topic rows. The publicly linked [V15 objectives PDF, document version 4.0](https://lecbyo.files.cmp.optimizely.com/download/cefedfb2b8a511ef809306d06d323538?checkExpiry=false) provides **36 numbered objectives**, in groups of 11/11/4/10. CompTIA’s [public resource portal](https://www.comptia.org/en-us/partner-portal/partner-resources/) supplies the document. PDF version 4.0 and exam version V15 are different identifiers.

| Objective IDs | Practice coverage |
|---|---|
| 1.1–1.3 | OS/file-system choices, installation methods, Windows editions |
| 1.4–1.7 | Windows tools, commands, settings, client networking |
| 1.8–1.11 | macOS, Linux, application installation, cloud productivity |
| 2.1–2.3 | Security controls, Windows identity/access, wireless/authentication |
| 2.4–2.6 | Malware and detection, threats/social engineering, response sequence |
| 2.7–2.11 | Workstation/mobile hardening, disposal, SOHO, browsers |
| 3.1–3.4 | Windows faults, mobile OS/apps, mobile security, PC security |
| 4.1–4.3 | Documentation/assets, change control, backup/recovery |
| 4.4–4.7 | Safety, environment, privacy/licensing/policy, communication |
| 4.8–4.10 | Scripting, remote access, AI concepts and limitations |

## 1. Operating systems — 28%

### Choose and install the right OS

Match edition and platform to hardware support, CPU architecture, application/driver needs, domain/enterprise management, encryption/virtualization features, lifecycle/support, licensing, user accessibility, and security. Windows, macOS, Linux distributions, ChromeOS, iOS/iPadOS, Android, and embedded systems have different update, installation, management, and application models. “Runs today” is not sufficient if the release is unsupported or lacks the required business control.

Before installation or upgrade, inventory hardware/firmware compatibility, storage and free space, drivers, applications, accounts/keys, encryption/recovery material, network, licensing, user data, and rollback. Clean installation, in-place upgrade, repair/reset/recovery, image deployment, and network installation have different preservation and risk boundaries. Verify boot mode and partitioning; do not delete/format an unknown disk before protecting data.

File systems have capability and compatibility differences. NTFS supports Windows permissions and features; FAT32/exFAT trade capability for broad/removable compatibility; APFS and ext-family systems serve their platforms. GPT and MBR describe partitioning structures, not file systems. Permissions, ownership, encryption, journaling, maximum sizes, and boot support are distinct.

### Editions, support, and storage decisions

**VERIFY CURRENT:** Windows 10 and 11 appear in the published outline, but exam coverage does not extend a product’s support. Microsoft records ordinary Windows 10 support ending October 14, 2025; ESU eligibility and individual LTSC releases have separate conditions. Check the exact edition, version, enrollment, and current [release/lifecycle table](https://learn.microsoft.com/en-us/windows/release-health/release-information) before approving a deployment. For example, Enterprise LTSC 2021 and IoT Enterprise LTSC 2021 have different support end dates. The current [Windows 10 options page](https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025) is preferable to memorizing an old consumer ESU deadline.

| Requirement | Decision and verification |
|---|---|
| Managed Windows endpoint | Home, Pro, Enterprise and N are not interchangeable labels. Compare domain join, policy tools, application/media dependencies and licensing; an N edition has different media components. |
| Remote Desktop host | Windows Home can be a client but cannot host the built-in RDP service; check the target edition and approved connectivity. See [Microsoft’s Remote Desktop guidance](https://support.microsoft.com/en-us/windows/experience/connectivity-networking/how-to-use-remote-desktop). |
| Windows drive encryption | Full BitLocker management is available in supported Pro/Enterprise/Education editions. Eligible Home devices can offer Device Encryption; “Home” does not mean “unencrypted.” |
| Windows installation | Confirm supported CPU/architecture, TPM/UEFI/Secure Boot requirements for the chosen release, storage, drivers, app compatibility and recovery before changing firmware or partitions. |
| File-system choice | Compare NTFS, FAT32/exFAT, ReFS, APFS, ext4 and XFS by platform, permissions, resilience and use case. Recognition of ReFS/XFS is not permission to assume every OS edition can create or boot from them. |

An unattended installation supplies repeatable answers; imaging deploys a prepared state; a clean install replaces the OS environment; an in-place upgrade attempts to retain supported apps/data. They still need compatible drivers, activation, update/security configuration and user acceptance. Check application architecture, CPU/RAM/storage, dependencies, license/DRM and trusted package source before installation. A web app avoids some local deployment work but still depends on browser, identity, network and service availability.

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

Configure local users/groups, sign-in, permissions/shares, mapped resources, printers, applications/defaults, updates, time/region, power, accessibility, display, and Windows networking. Distinguish local account, workgroup, domain, and cloud/work identity. Share permissions and file-system permissions can both affect effective access. Check public/private network profile, application firewall exception, proxy, metered connection, mapped network path and VPN/wired/Wi-Fi/WWAN state independently. For settings practice, explain sleep versus hibernate, lid behavior, fast startup and USB selective suspend; also inspect file extensions/hidden-file display, indexing, default apps, accessibility and privacy permissions before changing them.

### Command intent and shell context

The following are study examples, not a repair script. Use the correct shell and a disposable target for changes. Windows command-shell built-ins such as `dir`, `copy`, `del` and `rd` do not necessarily have identical semantics to similarly named PowerShell aliases.

| Support question | Tool/example and boundary |
|---|---|
| Which identity and applied policy? | `whoami /groups`, `gpresult /r`: inspect context. `gpupdate` requests policy refresh and can change effective configuration. |
| Which IP configuration, DNS result, connections? | `ipconfig /all`, `nslookup example.com`, `netstat -ano`; distinguish local inspection from DNS queries. `ipconfig /release` changes networking and may disconnect support. |
| Which process or path? | `tasklist`, `cd`, `dir`; `taskkill`, `del`, `rd` and `shutdown` change state. Check the exact PID/path/session first. |
| Which file permissions? | `icacls "C:\Practice\notes.txt"` displays the DACL; `/grant`, `/deny`, `/reset` and `/restore` alter it. |
| Protected OS-file integrity? | `sfc /verifyonly` checks without repairing; `sfc /scannow` attempts repairs and needs an administrative context. A successful scan is not a malware-clearance certificate. |
| Disk, image, boot or file-system repair? | Distinguish `chkdsk`, `dism`, `diskpart` and `format`; inspect help and exact target/flags. Disk selection is not proof that formatting is authorized. |
| Copy and compare a practice tree? | `robocopy` has its own return-code convention. Codes below 8 can represent successful work or differences; 8 or more indicates a copy failure. `/L` lists intended work, while `/MIR` can delete destination extras. |

Read the [icacls](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls), [SFC](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sfc) and [Robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy) references for exact flags. Local work below executes only the synthetic copy/restore example; it does not execute these OS repair, account, ACL or network changes.

### macOS, Linux, and mobile basics

On macOS, recognize Finder, System Settings, Activity Monitor, Disk Utility, Terminal, Keychain, Time Machine, force quit, file permissions, application packages, and update/recovery concepts. On Linux, recognize shell, package management, files/directories, permissions/ownership, processes/services, logs, networking, mounts, desktop utilities, and repository trust. Commands and paths vary by distribution/version; use local help and current documentation.

On macOS, distinguish a `.dmg` disk image, `.pkg` installer and `.app` application bundle. `/Applications`, each user’s home, `/Library`, the user’s `~/Library` and `/System` have different scopes; a user preference repair is not a reason to change protected system files. Spotlight searches, Mission Control/desktops organize work, and Keychain stores credentials. Check corporate restrictions before account, cloud-sync or application changes.

On mobile OSs, understand application stores/sideloading policy, permissions, accounts/synchronization, radios, notifications, location, storage, updates, backup/reset, screen lock/biometrics, and management profiles. Preserve authentication/recovery and backup state before reset.

For Linux evidence, connect `pwd`/`ls` to paths, `cat`/`less`/`grep` to content, `ps`/`top` to processes, `df`/`du` to capacity/use, `ip`/`ping`/`dig` to networking, and `man` to the installed tool’s behavior. Recognize `cp`, `mv`, `rm`, `chmod`, `chown`, `sudo`, package tools and service controls as possible changes. Package managers and init systems differ; do not paste a distribution-specific command into an unrelated platform.

For an ordinary file, mode `640` means owner read/write, group read, others no access: 6 = 4 + 2, 4 = read, 0 = none. Directory execute means search/traversal, so a directory with read permission alone is not equivalent to an accessible file. See the [GNU numeric-permission reference](https://www.gnu.org/software/coreutils/manual/html_node/Numeric-Modes.html). ACLs and additional controls can further affect access; no Linux permission changes were run here.

On a Mac with Apple silicon or T2, automatic storage encryption and enabling FileVault are distinct protection states. FileVault adds password-bound access protection; keep the chosen recovery route usable and separate from the device. See [Apple’s FileVault guidance](https://support.apple.com/en-gb/guide/mac-help/mh11785/26/mac). Time Machine backup, iCloud synchronization and a FileVault recovery key solve different problems.

### Cloud productivity support — objective 1.11

Separate email, storage/sync, collaboration, identity synchronization and license assignment. Successful sign-in does not prove a mailbox or application license is provisioned, and a license does not grant access to every shared document. Inspect account/tenant, entitlement, client/web behavior, connection, quota, sync state and sharing scope before resetting a profile.

**Worked case:** A new hire can sign in through a browser but the desktop app reports no entitlement and a shared folder is absent. Verify the intended account and assigned product/service, then client activation and token refresh. Separately check folder membership/link scope and whether files are actually downloaded for offline use. Test sign-in, licensed use, allowed sharing and denied access independently. Record evidence without copying the person’s mailbox or credentials. This is a reasoning case; no tenant was changed.

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

### Controls and recovery are separate checks

SSO reduces repeated sign-ins; federation such as SAML conveys identity assertions; MFA adds independent factors. JIT access limits the time of an elevated grant, PAM manages privileged access, and DLP helps govern sensitive-data movement. None automatically makes an authenticated device trustworthy. Compare physical access controls, logging and Zero Trust verification as complementary controls.

Windows UAC prompts/elevation, AD identity/group membership, NTFS/share permissions, EFS file encryption and BitLocker volume encryption act at different layers. For a simple network-share case, a user with share Read and NTFS Modify cannot write through that share. Local access does not traverse the share-permission layer. Avoid the blanket rule “deny always wins”: the [documented ACE ordering](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls) distinguishes explicit and inherited entries. Inspect actual identity, groups and effective access.

[Device Encryption](https://support.microsoft.com/en-us/windows/security/encryption/device-encryption-in-windows) availability depends on the device and configuration. [BitLocker’s overview](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/) also distinguishes encrypted data from active protection: a clear key or suspended protection changes the security outcome. Verify protection state and the authorized [recovery process](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-recovery-guide-plan) before firmware, boot or repair work. Never place a recovery secret in a ticket, screenshot or public exercise. BitLocker To Go covers removable-drive scenarios; EFS needs its own certificate/key recovery planning.

For wireless access, distinguish personal shared-secret deployment from enterprise authentication, WPA2/WPA3 from legacy TKIP, and RADIUS/TACACS+/Kerberos roles from the Wi-Fi cipher itself. Hiding an SSID or filtering an address is not encryption. Restrict router management, review UPnP/port-forwarding exposure and test guest isolation according to policy. EDR is endpoint detection/response, MDR adds a managed response service, and XDR correlates across sources; an alert still requires triage and an authorized response.

**PRACTICAL DEPTH:** The outline names password length, complexity and expiration as concepts to understand. That is not a universal recommendation for routine rotation. Current [NIST digital-identity guidance](https://pages.nist.gov/800-63-4/sp800-63b.html) distinguishes password-only authentication from passwords used within MFA and emphasizes compromised-password screening and change after compromise. Apply the organization’s documented policy and the relevant authenticator context instead of inventing one rule for every device PIN or local account.

### Malware response and disposal

**CURRENT BLUEPRINT, objective 2.6:** Learn the published sequence: investigate/confirm symptoms; quarantine; disable System Restore in Windows Home; remediate; update anti-malware; scan using the appropriate safe/preinstallation environment; reimage or reinstall when needed; schedule ongoing scans/updates; re-enable System Restore and create a point in Windows Home; educate the user. These are objective milestones, not an instruction to disable protection on the computer you are using.

For real incidents, use the approved response runbook, preserve evidence and escalation requirements, and protect recovery options before any destructive change. Microsoft describes [System Protection](https://support.microsoft.com/en-us/windows/experience/backup-recovery/system-protection) and [System Restore](https://support.microsoft.com/en-us/windows/experience/backup-recovery/system-restore) separately from personal-file backup: a restore point concerns system state, not recovery of every deleted document. A point may not exist, and encrypted recovery may require an authorized key. Reimaging does not itself revoke stolen sessions or recover compromised identities. Verify accounts, application/data function, updates and security, then document and educate.

**PRACTICAL DEPTH:** [NIST SP 800-88 revision 2, September 2025](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r2.pdf) distinguishes clear, purge and destroy by the required recovery resistance and whether reuse remains possible. Match the approved method to the media and data. An SSD’s spare/remapped cells make ordinary overwriting an incomplete guarantee; degaussing is not a flash-erasure method. Drilling or bending a device alone does not prove adequate destruction, even though the exam asks you to recognize disposal methods. Cryptographic erase needs suitable prior encryption and control of all relevant key copies; merely deleting a password is insufficient. Check operation results, then decide whether the outcome is adequate and record the disposition. No sanitization or disposal was performed for this guide.

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

### Narrow a symptom with discriminating evidence

| Symptom | First comparison | What it does not prove |
|---|---|---|
| Slow profile load | Same device with another authorized test account; profile/service/network timeline | That the disk must be replaced |
| Time drift and sign-in/certificate trouble | Clock/time-zone/time-service state versus the expected source | That every certificate warning should be bypassed |
| USB controller resource warning | Device/controller topology, driver and recent additions | That free storage space is the USB resource limit |
| One app crashes after update | Exact version, event, dependency and known-good test file/profile | That reinstalling the OS is the next step |
| Repeated mobile reboots | Update, storage, battery/thermal and management evidence | That rooting or disabling controls is a fix |

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

**Original restore-chain example:** A Sunday full backup captures files A and B. Monday changes A; Tuesday deletes B and adds C. A Tuesday incremental strategy needs the Sunday full plus Monday and Tuesday increments; the deletion must be represented to recover the intended Tuesday state. A Tuesday differential needs the Sunday full plus Tuesday’s changes since Sunday. A synthetic full assembles a new full recovery set from an existing full and subsequent changes at the backup system; it is not simply renaming the newest incremental file. Exact chaining and metadata handling depend on the product.

GFS rotates daily/weekly/monthly generations; a 3-2-1 design considers copy count, different storage and an offsite copy. Also test separation of credentials/failure domains and an offline or otherwise protected recovery copy. Choose in-place versus alternate-location restore deliberately: the latter lets you inspect results before replacing current files. A matching hash checks content, not restored permissions, application consistency or all recovery objectives.

Use ESD protection, power isolation, correct lifting, cable management, PPE, ventilation, and safety data guidance for chemicals/consumables. Never open a PSU or CRT/high-voltage equipment without qualifications. Handle swollen batteries, toner, solvents, and electronic waste through approved processes. Environmental controls include temperature, humidity, dust, airflow, power quality, noise, and responsible recycling/disposal.

Privacy, data handling, acceptable use, prohibited content/activity, licensing, intellectual property, and regulatory/policy obligations control what a technician may view, copy, retain, install, or report. Technical access is not permission. Minimize exposure and use chain of custody when required.

### Communication, scripting, and remote support

Listen, clarify, avoid jargon/blame, set honest expectations, communicate delays, protect confidentiality, and confirm resolution with the user. Handle difficult interactions calmly and escalate threats, discrimination, unsafe or policy-sensitive requests appropriately. Never invent certainty or criticize prior staff to the user.

Recognize basic script elements in PowerShell, shell, batch, JavaScript, Python or platform tools: interpreter, comments, variables, conditionals, loops, parameters, environment variables, file/network/process operations, errors, and output. Read before running; confirm author/source, target, privilege, secrets, input validation, idempotence, logging, rollback, and a test environment. Do not download-and-execute unknown scripts.

Remote support options include screen sharing/assistance, remote desktop, SSH, VPN, management agents, and ticket/collaboration tools. Confirm identity/consent, use approved encrypted tools and least privilege, communicate visible actions, protect clipboard/files/credentials, disconnect/close access, and document. Unsolicited remote-support calls are a common scam pattern.

RDP provides a remote desktop; VPN provides a network path; SSH provides a secure remote shell and related channels. VNC, SPICE, WinRM, RMM and screen-sharing tools have different deployment/authentication/encryption controls. A VPN connection does not authorize every reachable system. Close the session and any temporary grant separately. Script extensions `.bat`, `.ps1`, `.vbs`, `.sh`, `.js` and `.py` identify different interpreters; a familiar extension is not a trust signal. Microsoft states that [PowerShell execution policy](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies) is not a security boundary. Do not weaken policy merely to make an unknown script run.

### AI in support work — objective 4.10

An AI feature can summarize an approved ticket, suggest a hypothesis or draft a knowledge article inside an application. The technician still checks accuracy, bias, source quality and permission to use the data. A convincing command or citation may be fabricated. A “private” product label does not by itself establish retention, access, training use or acceptable handling of customer information; inspect the applicable settings and policy. Attribute reused work and follow intellectual-property and acceptable-use rules.

**Original review case:** A generated answer proposes deleting a user profile and pasting its logs into a public chat. Reject that recommendation until the exact fault, backup, authorized data handling and a less destructive diagnosis are established. Verify each proposed command against the installed tool’s help and vendor documentation. Draft a sanitized ticket update with evidence and uncertainty; obtain the normal change approval for any actual repair. This case uses invented facts, not a customer ticket.

### Local PowerShell copy-and-restore exercise

**PRACTICAL DEPTH:** Save the following as `copy_restore_demo.ps1` and use PowerShell on Windows with an existing ordinary practice directory. Review the whole script first and use the environment’s approved script-execution process. Run `./copy_restore_demo.ps1 -PracticeRoot 'C:\Practice'` only after that directory exists. The script creates a new random child directory, works solely on its synthetic files, verifies content and removes that child after checking its absolute path. It does not mirror, purge, change ACLs or repair the OS. Logs are temporary and are removed with the child; inspect a failed copy in a separately reviewed diagnostic adaptation if persistent evidence is required.

```powershell
[CmdletBinding()]
param([Parameter(Mandatory)][string]$PracticeRoot)

$ErrorActionPreference = 'Stop'
# Robocopy uses nonzero success codes; inspect its native code explicitly.
$PSNativeCommandUseErrorActionPreference = $false
$rootItem = Get-Item -LiteralPath $PracticeRoot
if (-not $rootItem.PSIsContainer -or
    ($rootItem.Attributes -band [IO.FileAttributes]::ReparsePoint)) {
    throw 'Choose an existing ordinary practice directory.'
}
$practiceBase = [IO.Path]::GetFullPath($rootItem.FullName)
if ($practiceBase.TrimEnd('\') -eq [IO.Path]::GetPathRoot($practiceBase).TrimEnd('\')) {
    throw 'Choose a practice subdirectory, not a drive root.'
}
$runName = 'core2-demo-' + [guid]::NewGuid().ToString('N')
$runRoot = Join-Path $practiceBase $runName
$source = Join-Path $runRoot 'source'
$backup = Join-Path $runRoot 'backup'
$restore = Join-Path $runRoot 'restored'
$null = New-Item -ItemType Directory -Path $source, $backup, $restore

function Copy-PracticeTree([string]$From, [string]$To, [string]$Log) {
    # /E includes empty folders. No mirror/purge, ACL override or retry loop.
    & robocopy.exe $From $To /E /R:0 /W:0 /COPY:DAT /DCOPY:DAT "/LOG:$Log" /NFL /NDL /NJH /NJS /NP | Out-Null
    $copyCode = $LASTEXITCODE
    if ($copyCode -ge 8) { throw "Robocopy failure code $copyCode; inspect the local log." }
    return $copyCode
}

try {
    $file = Join-Path $source 'notes.txt'
    Set-Content -LiteralPath $file -Value 'Synthetic lesson notes, version 1.' -Encoding utf8
    $null = New-Item -ItemType Directory -Path (Join-Path $source 'empty-folder')
    $expectedHash = (Get-FileHash -LiteralPath $file -Algorithm SHA256).Hash
    $first = Copy-PracticeTree $source $backup (Join-Path $runRoot 'first.log')
    $repeat = Copy-PracticeTree $source $backup (Join-Path $runRoot 'repeat.log')
    $copiedHash = (Get-FileHash -LiteralPath (Join-Path $backup 'notes.txt') -Algorithm SHA256).Hash
    if ($copiedHash -ne $expectedHash) { throw 'Backup content did not match.' }

    # Change only this newly created synthetic working file, after its backup.
    Set-Content -LiteralPath $file -Value 'Synthetic later edit.' -Encoding utf8
    $restoredCode = Copy-PracticeTree $backup $restore (Join-Path $runRoot 'restore.log')
    $restoredHash = (Get-FileHash -LiteralPath (Join-Path $restore 'notes.txt') -Algorithm SHA256).Hash
    if ($restoredHash -ne $expectedHash) { throw 'Restored content did not match.' }

    [pscustomobject]@{
        FirstCopyCode = $first
        RepeatCopyCode = $repeat
        RestoreCopyCode = $restoredCode
        BackupHashMatches = ($copiedHash -eq $expectedHash)
        RestoredHashMatches = ($restoredHash -eq $expectedHash)
        LaterEditDiffers = ((Get-FileHash -LiteralPath $file).Hash -ne $expectedHash)
        EmptyDirectoryRestored = (Test-Path -LiteralPath (Join-Path $restore 'empty-folder') -PathType Container)
    }
}
finally {
    # Resolve and verify the exact newly created child before recursive cleanup.
    $resolvedRun = (Get-Item -LiteralPath $runRoot).FullName
    $expectedRun = [IO.Path]::GetFullPath((Join-Path $practiceBase $runName))
    if (-not [string]::Equals($resolvedRun, $expectedRun, [StringComparison]::OrdinalIgnoreCase) -or
        -not [string]::Equals([IO.Path]::GetDirectoryName($resolvedRun), $practiceBase.TrimEnd('\'), [StringComparison]::OrdinalIgnoreCase)) {
        throw 'Cleanup target failed the practice-directory check.'
    }
    Remove-Item -LiteralPath $resolvedRun -Recurse -Force
}
```

The example and a separate test harness passed **18 checks** with PowerShell 7.6.6 and Windows Robocopy 10.0.26100.1. The first copy and restore returned 1; the unchanged repeat returned 0. Additional synthetic cases produced code 2 for a retained destination extra, code 3 for list-only differences without changing content, and code 16 for a missing source. The harness also verified cleanup and operation when the caller treats native nonzero exit codes as errors. The script handles Robocopy’s convention within its own scope. No host policy was changed.

This proves local file copying, content comparison and alternate-location restore for the synthetic example. It does not prove offsite protection, retention, ACL recovery, full-system/application consistency, encryption recovery or incident eradication. The eight complete labs below remain proposed.

> **Related item:** A blameless review asks which system/process controls allowed recurrence. It improves reliability without hiding individual accountability for unsafe choices.

## Integrated scenarios

### Scenario 1: Failed update and encrypted laptop

A managed laptop boot-loops after an update. Confirm user/asset, backup and encryption recovery key, exact boot/error state, storage health, and recent deployment. Use approved recovery/safe-mode tools, rollback or repair only after data protection, validate sign-in/apps/network/security/update state after reboot, document, and link the broader change incident.

### Scenario 2: Suspected account and browser compromise

A user sees popups and unexpected MFA prompts. Isolate as policy requires, preserve URLs/times/alerts, verify the account from a trusted device, revoke sessions/reset credentials with MFA review, inspect extensions/proxy/DNS/apps/protection, scan or reimage according to confidence, restore trusted data, patch/harden, validate, report, and educate without blame.

### Scenario 3: Remote new-hire setup

Choose a supported OS/edition, install from trusted media/image, partition and encrypt, apply identity/least privilege, updates/security baseline, VPN/remote support, applications/licensing, backup, privacy settings, accessibility and documentation. Use a change/ticket record and test standard-user work, denied admin action, recovery, and secure remote-support closure.

## Hands-on labs

All eight are proposed platform labs; execute them only in an authorized disposable environment and retain sanitized evidence. The local PowerShell subset above has separate execution evidence.

1. **Multi-OS inventory:** record OS edition/version/support, file system, apps, users, processes, network and recovery for available Windows/Linux/macOS platforms. Compare two tools that answer the same support question. Success: explain a real platform difference; negative case: identify a feature unavailable on the chosen edition.
2. **Windows native tools:** capture a baseline with Task Manager, Event Viewer, services, Device/Disk Management and safe read commands. Introduce one harmless test-app fault, correlate the event/time and restore the baseline. Success: evidence distinguishes the cause from a coincidental warning; do not clear logs to make the result look clean.
3. **Install/recovery:** install a disposable OS using documented partition/driver/account choices. Add synthetic data, create an approved backup/recovery point and test an alternate-location file restore. Success: content and intended application access work; explain why the restore point alone cannot recover every user document.
4. **Permissions and hardening:** create disposable standard/admin identities and a synthetic share, then test allowed and denied read/write paths as each identity. Compare share and file-system layers, review firewall/encryption recovery and undo test grants. Success: least privilege survives sign-out/restart; record recovery-key availability without recording the key.
5. **Malware-response tabletop:** use invented alerts, not live malware. Walk the objective 2.6 milestones alongside the approved incident runbook, identifying evidence preservation, containment and reimage/account-recovery decisions. Success: state what additional evidence is needed before declaring recovery; do not disable host protection for this tabletop.
6. **Software/mobile faults:** use one reversible test-app permission, startup or proxy setting at a time. Compare affected and known-good accounts/apps/networks and restore the setting. Success: original task works and security settings remain correct; explain when physical battery or thermal symptoms require escalation.
7. **Operations packet:** write an asset/ticket/change record, an incremental/differential/synthetic-full recovery plan and a sanitized knowledge article. Test restore to a separate location and record time/data loss against stated targets. Success: a second reader can repeat the approved process and identify rollback, privacy, licensing and disposal responsibilities.
8. **Remote-support capstone:** verify consent and the intended test identity, use an approved remote tool and review any script before execution. Test permitted and denied access, licensed cloud-app use and document-sharing scope. Review an invented AI repair suggestion for correctness and data handling. Success: user workflow works, temporary privileges/session are closed and the ticket records evidence without secrets.

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

41. Why can a licensed cloud app still fail to open a shared file?
42. Why can a plausible AI-generated repair command still be unsuitable?

## Answers and reasoning

1. CompTIA prohibits mixing versions; both V15 component exams are required.
2. Hardware, apps/drivers, management/domain, features, support lifecycle, license, accessibility and security.
3. User data, backup/restore proof, encryption/recovery keys, licenses, accounts and rollback state.
4. GPT/MBR organize partitions; the others organize files/data inside volumes.
5. Event Viewer and Reliability Monitor provide time-correlated history; live tools complement them.
6. It can broadly change system/application behavior and lacks automatic safe intent; back up and target precisely.
7. Source, exact target, read/write effect, parameters, output, required rights, risk, rollback and authorization.
8. A network-share request must pass both share and file-system checks: share Read constrains NTFS Modify to read through that share. Local access bypasses the share layer. Explicit/inherited ACE order and group membership require an actual effective-access check.
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
19. A format can leave recoverable content, especially outside an SSD’s ordinary addressable space. Use a media-appropriate approved method, verify its execution and validate adequacy; degaussing flash or merely drilling a hole is not proof of sanitization.
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
30. Full restores one set; incremental needs the relevant full plus every subsequent increment through the recovery point; differential needs the full plus latest differential. A synthetic full is assembled from prior backup data. Preserve deletion/metadata semantics and verify the restored application state.
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

41. Entitlement, identity, client activation and resource authorization are separate checks; verify account, service state and the file’s actual sharing scope.
42. It may be fabricated, wrong for the installed version, destructive, unauthorized or based on private data that should not have been submitted. Verify source, target, effects, recovery and policy before action.

## 220-1102-to-220-1202 gap checklist

Map older content line by line to V15. Verify current Windows editions/features/tools/commands and supported lifecycle, macOS/Linux/mobile behavior, installation/recovery and file systems, MFA/passkeys/identity and current wireless/browser/SOHO controls, modern threats and malware response, mobile/application/security symptoms, ticket/change/backup/privacy/licensing expectations, scripting, cloud productivity and its identity/license boundaries, synthetic-full recovery, responsible AI use and approved remote support. Do not combine an older 1101 or 1102 pass with a V15 component.

## Source and freshness notes

- CompTIA controls the V15 weights, delivery, score/languages, same-version rule, and estimated lifecycle.
- OS versions/support, utilities/commands, threats, security recommendations, remote tools, licensing and privacy requirements change. Verify implementation against current vendor and organizational documentation.
- This guide contains original scenarios, labs, checks, and explanations from public scope; it does not copy proprietary objectives, PBQs, course labs, or exam items.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Select one V15 path, practice on disposable multi-OS systems, and use one explanation-led assessment to guide remediation.

| Resource | Access | Estimated time |
|---|---|---:|
| CompTIA [CertMaster Perform](https://www.comptia.org/en-us/resources/certmaster-training/perform/), [Learn](https://www.comptia.org/en-us/resources/certmaster-training/learn/), [Labs](https://www.comptia.org/en-us/resources/certmaster-training/labs/) and [Practice](https://www.comptia.org/en-us/resources/certmaster-training/practice/) | Paid official options; select exact 220-1202 product and avoid double-counting overlapping bundles | Provider estimates: Perform 30–60h; Learn 25–40h; Labs 15–25h; Practice 10–20h |
| [Pluralsight A+ Core 2 path](https://www.pluralsight.com/paths/comptia-a-core-2-220-1202) | Subscription; 5 courses and practice exam; public outline includes older Windows wording, so compare lesson scope with V15 | 12 listed hours plus 20–40 lab/review hours |
| [LinkedIn Learning / Total Seminars Core 2](https://www.linkedin.com/learning/comptia-a-plus-core-2-220-1202-cert-prep) | Subscription; 22 quizzes; public page released September 26, 2025 | 21 hours 45 minutes plus 20–40 lab/review hours |
| [Complete A+ Guide V15](https://www.oreilly.com/library/view/complete-a-guide/9780135439883/) | O'Reilly/Pearson subscription book covering both cores | About 25–45 selected reading/lab hours for Core 2 |
| [Udemy / Jason Dion Core 2](https://www.udemy.com/course/comptia-a-core-2/) | Paid marketplace course and practice exam | Verify current runtime; allow 25–50 hours plus labs/review |
| [MeasureUp Core 2](https://www.measureup.com/comptia-a-core-2-practice-test.html) | Paid explanation-led practice; public page lists 287 questions, July 2025 update | About 6–12 hours across attempts and review; bank is volatile |
| [Professor Messer free 220-1202 course](https://www.professormesser.com/free-a-plus-training/220-1202/220-1202-video/220-1202-training-course/) | Free 74-video course; optional paid notes/practice | 13 hours 41 minutes plus 20–40 hands-on hours |

No exact Whizlabs 220-1202 route was independently verified. Reject “actual questions” and dumps. Provider durations, prices, bundles, banks, updates, and access are volatile.

Public metadata was checked September 28, 2026. Pluralsight lists 12 hours; LinkedIn lists 21h45 and correctly names 220-1202 in its description; Messer lists 74 videos/13h41. Paid lesson interiors were not reviewed, and public outlines do not prove complete current coverage. O’Reilly and Udemy blocked automated rechecking. Times beyond provider-listed durations are planning estimates.
