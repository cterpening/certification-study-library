---
exam_code: EX200
vendor_id: red-hat
official_blueprint: https://www.redhat.com/en/services/training/ex200-red-hat-certified-system-administrator-rhcsa-exam
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# EX200 Red Hat Certified System Administrator Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#ex200-coverage-record). The [official EX200 objectives](https://www.redhat.com/en/services/training/ex200-red-hat-certified-system-administrator-rhcsa-exam) are authoritative.

**Current baseline:** EX200 based on Red Hat Enterprise Linux 10<br>
**Upcoming blueprint change:** None announced when checked September 1, 2026<br>
**Important freshness boundary:** RHEL 9 and older RHCSA material remains useful for durable Linux concepts, but the current public objectives add or emphasize RHEL 10 details such as Flatpak software management and systemd timers. Practice on RHEL 10 and reconcile every objective.<br>
**Official source:** [Red Hat Certified System Administrator exam (EX200)](https://www.redhat.com/en/services/training/ex200-red-hat-certified-system-administrator-rhcsa-exam)

## How to use this guide

EX200 is a performance-based administration exam. You configure real systems without internet access or personal notes; for most exams, product documentation shipped with the environment is available. Red Hat explicitly requires configurations to persist after reboot. Preparation therefore means repeatedly doing each public objective from a clean RHEL 10 machine, verifying the requested outcome, rebooting when safe, and diagnosing failures without a copied recipe.

Red Hat recommends RH124 plus RH134 for learners following the standard path, or RH199 for experienced Linux administrators. These are recommendations, not certification prerequisites. The public exam page does not expose one universal price or appointment duration before location selection; verify the scheduler and the current Certification Program Guide before booking. A Red Hat skills-path resource lists a three-hour exam, but delivery metadata is volatile.

For each task, use a five-part loop:

1. inspect current state, devices, dependencies, policy, and the exact requested end state;
2. make the smallest correct change with a native RHEL tool or well-understood configuration file;
3. validate runtime behavior, configuration syntax, permissions, logs, and exit status;
4. make the change persistent and test the next boot/mount/service activation path;
5. record a rollback/recovery method and repeat later from memory using local documentation only.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

Red Hat publishes task groups but no percentage weights. Do not invent a priority ranking from page order.

| Official task group | Performance outcome |
|---|---|
| Understand and use essential tools | Work accurately at the shell, transform text, manage files/links/archives/permissions, use SSH, and find local help. |
| Manage software | Configure RPM and Flatpak repositories and install/remove software. |
| Create simple shell scripts | Use inputs, command output, conditionals, tests, and loops safely. |
| Operate running systems | Control boot/targets/processes/tuning/logs/services and transfer files. |
| Configure local storage | Manage GPT partitions, PVs, VGs, LVs, swap, labels/UUIDs, and nondestructive additions. |
| Create and configure file systems | Build/use VFAT, ext4, XFS, NFS, autofs, extend LVs, and fix permission failures. |
| Deploy, configure, and maintain systems | Schedule work, manage service/boot state/time/software updates, and modify the bootloader. |
| Manage basic networking | Configure IPv4/IPv6, resolution, activation, and firewall restrictions. |
| Manage users and groups | Administer accounts, groups, memberships, aging, and privileged access. |
| Manage security | Apply firewalld, default permissions, SSH keys, and SELinux modes/contexts/ports/booleans. |

## 1. Understand and use essential tools

### Shell, redirection, text, and local documentation

Know command syntax, quoting, globbing, variables, paths, exit status, standard input/output/error, pipes, and redirection. `>` replaces a file; `>>` appends; `2>` redirects standard error; a pipeline passes one command's output to the next process. Avoid destructive redirections until you have confirmed the target. Use `grep` with basic/extended regular expressions deliberately and distinguish a regular expression from a shell glob.

Use `man`, `info`, `--help`, `/usr/share/doc`, package file lists, examples, and configuration comments. Search by purpose with `man -k`/`apropos`, then inspect synopsis, options, files, examples, and related pages. Build the habit of solving an unfamiliar option from local help because internet access is unavailable during the exam.

Manage files/directories with ownership and metadata in mind. Understand absolute/relative paths, hidden files, recursive operations, safe copying, hard links (same inode/filesystem constraints), symbolic links (path reference and dangling behavior), archives versus compression, and `tar` with gzip/bzip2. Verify results with `ls -l`, `stat`, `file`, `find`, checksums, and content inspection rather than assuming a command succeeded.

Access remote systems with SSH and transfer files securely using the supported SSH tools. Confirm host/user/key, permissions, target path, and ownership. Switching identities with `su` and privileged commands through `sudo` have different environment, authentication, and audit behavior.

**Related item:** A command that returns zero can still produce the wrong operational result. Validate the required state, not only the exit code—for example, archive contents, resolved link target, ownership, and service behavior.

## 2. Manage software

RPM is the package format/database; DNF resolves repositories, dependencies, installation, removal, and updates. Configure repositories with correct base URL, enabled state, GPG checking/key, and reachability. Inspect `dnf repolist`, package availability/version/info, owning package, installed files, dependencies, history, and transaction result. Installing an RPM directly does not give the same dependency workflow as DNF.

Flatpak uses remotes and application/runtime refs rather than RPM repositories. Add/list/remove a remote, search/install/list/update/uninstall applications, and understand system-versus-user scope. Validate application/runtime state and source. Keep RPM and Flatpak mental models separate.

**Related item:** A repository being syntactically configured does not prove its metadata, GPG trust, architecture, or required package is available. Test the actual transaction path.

## 3. Create simple shell scripts

Write small Bash scripts with a shebang, executable permission or explicit interpreter, meaningful variables, quoted expansions, positional parameters, command substitution, tests, `if`/`elif`/`else`, and `for` loops. Validate required arguments and files, handle failure, and emit useful errors to standard error. Use `shellcheck` only if available during study; the final script must be understandable without it.

Distinguish string, numeric, and file tests. Quote `"$1"` and command output when word splitting/globbing is not intended. Prefer an idempotent state change where repeated execution should be safe. Test empty input, whitespace, missing resources, and a failed command—not just the happy path.

**Related item:** Scripting is a force multiplier for both success and mistakes. Limit input scope, verify targets, use temporary test data, and avoid unbounded recursive or destructive operations.

## 4. Operate running systems

### Boot, targets, processes, tuning, and services

Use `systemctl` to inspect and change default target, isolate an appropriate target when safe, start/stop/restart/reload services, enable/disable boot activation, and distinguish active from enabled. Read unit status and dependencies. A service can be enabled but currently failed, or active now but not persistent.

Understand the boot path sufficiently to diagnose firmware/bootloader, kernel/initramfs, root filesystem, systemd target, mount, and service failures. Practice interrupting the boot process and recovering administrative access only in disposable VMs using the current RHEL 10 procedure. Back up relevant configuration and test normal reboot afterward.

Inspect processes with `ps`, `top` and `/proc`; identify CPU/memory consumers; distinguish PID, parent, user, state, priority/nice, and command; send appropriate signals; manage shell jobs; and adjust scheduling with `nice`/`renice`. Prefer graceful termination before force when possible. Use `tuned` profiles by workload requirement and verify the active/recommended profile.

Use `journalctl` and conventional log files to filter by unit, boot, priority, time, and fields. Configure persistent journal storage when required and verify across reboot. Accurate time and hostname identity make logs useful. Transfer files securely and validate ownership/permissions at the destination.

**Related item:** Restarting a failed service before reading logs may obscure the original state. Capture status, journal, configuration syntax and dependency evidence first, then change one cause at a time.

## 5. Configure local storage

Inventory devices and topology with `lsblk`, `blkid`, `findmnt`, LVM reporting, and partition tools before writing. Know disk/device versus partition versus filesystem versus mount point. Use GPT partitioning, reread/verify the table, and never infer a device name from memory in a multi-disk system.

For LVM, understand physical volume → volume group → logical volume → filesystem/swap. Create and remove the correct layer in safe order; inspect extents and free capacity; name devices predictably; and avoid deleting a layer still in use. Add partitions, LVs, and swap non-destructively. Activate and verify swap runtime and persist it with a stable identifier.

Mount file systems at boot by UUID or label where required. An `/etc/fstab` typo can break boot, so create the mount point, choose correct type/options, use `mount -a` as a preflight, validate with `findmnt`, and test a reboot in the lab. Understand `nofail` and timeout options as operational design choices, not universal fixes.

**Related item:** Extending an LV and extending its filesystem are distinct operations. The filesystem-specific growth tool and online/offline behavior matter; inspect both block device and filesystem size afterward.

## 6. Create and configure file systems

Create, mount, unmount, label, and use VFAT, ext4, and XFS according to the requested interoperability and Linux-feature needs. Do not assume shrink/grow behavior is the same: XFS and ext4 have different supported resize semantics. Ensure no busy process prevents unmounting, and validate ownership/mode after mount because the mounted filesystem hides the underlying directory contents.

For NFS clients, identify server export/path, network/DNS reachability, mount type/options, persistence, and identity/permission behavior. Use autofs maps for on-demand mounts, restart/reload safely, trigger the map, and confirm the path unmounts according to policy. Diagnose failures across name resolution, route/firewall, export, client package/service, SELinux, mount options, ownership and permissions.

Permission diagnosis requires traversing every directory component, comparing owner/group/other mode, default `umask`, special bits where relevant, mount options, ACL/extended attributes if present, and SELinux context. Avoid `chmod 777`; determine the intended principal and minimum access.

## 7. Deploy, configure, and maintain systems

Schedule one-time work with `at`, recurring work with cron, and service-linked schedules with systemd timer/service units. Validate command path, user, environment, permissions, calendar expression, enablement, next/last run, output/logging, and persistence. A script that works interactively can fail under a minimal scheduler environment.

Install/update packages from Red Hat CDN, remote repositories, or local files as requested. Control services and default target. Configure time clients and verify source/synchronization, not merely that a daemon runs. Modify the bootloader only from a known-good backup/recovery plan and verify generated/current configuration plus a normal reboot.

**Related item:** systemd timers can express dependencies, missed-run persistence, random delay, and logging through their service unit. Cron remains appropriate for simpler calendar execution. Choose by required behavior.

## 8. Manage basic networking

Use NetworkManager tools such as `nmcli` to inspect connections/devices and configure IPv4/IPv6 addresses, prefix/gateway, DNS, search domains, autoconnect, and hostname resolution. Distinguish a connection profile from the live device state. Activate the correct profile, verify addresses/routes/DNS/listening services, and test the exact protocol from a peer.

Use `/etc/hosts` for deliberate static host mappings and understand its relationship to resolver configuration. A ping test does not validate DNS or the application port. Diagnose local interface → address/prefix → route/gateway → DNS → service listener → firewall/SELinux → remote path.

Restrict network access with firewalld using the correct zone, interface/source binding, service or port/protocol, runtime/permanent state, reload behavior, and rich/direct features only where required. Verify both allowed and denied behavior after reload and reboot.

## 9. Manage users and groups

Create, modify, lock/unlock, and remove local users; set shell, home, UID, primary/supplementary groups, password, and aging. Know when removal should retain or delete a home directory and how orphaned numeric ownership appears. Create/modify groups and memberships without accidentally replacing existing supplementary groups.

Configure privileged access with `sudoers` and included files, edit safely with `visudo`, scope users/groups/hosts/commands, and test as the target identity. Avoid broad passwordless root access unless explicitly required. Password aging, account expiration, shell locking, and password locking solve different requirements.

**Related item:** Numeric UID/GID ownership is stored on the filesystem. Reusing an identifier can grant a new account access to old files; inspect and resolve orphaned ownership deliberately.

## 10. Manage security

### Permissions, SSH, firewalld, and SELinux as layers

Use standard user/group/other read-write-execute permissions, ownership, directory traversal semantics, default `umask`, and special permissions only when intended. Generate and deploy SSH public keys with correct account and `.ssh`/`authorized_keys` ownership/modes; verify key authentication before disabling or changing fallback access.

SELinux mode (enforcing/permissive), policy decisions, process domain, file type, port label, and boolean are different concepts. Inspect with `getenforce`, `ls -Z`, `ps -eZ`, `semanage`, `getsebool`, and AVC/journal tools. Restore a known default context with `restorecon`; use persistent file-context mappings for nonstandard paths rather than repeatedly applying a transient label. Add/modify a port type or boolean only when it expresses the intended policy. Permissive mode is diagnostic, not a permanent repair.

Firewalld controls network traffic; SELinux constrains processes even after network access arrives; Unix permissions constrain filesystem access; service configuration determines whether anything listens. Troubleshoot all layers and keep the minimum necessary opening.

**Related item:** `chcon` can be useful for an experiment but its label can be lost on relabel. A persistent `semanage fcontext` rule followed by `restorecon` expresses the durable intent.

## Integrated scenarios

### Scenario 1: New application host that survives reboot

Create a service account and group, scoped sudo rule, application directory with least permissions and persistent SELinux context, RPM repository/package, simple systemd-managed script/service, configuration file, log path, static network profile, time client, and firewalld service access. Verify from a peer, inspect journal/context/listener/firewall, reboot, and repeat every validation. Roll back the repository, service, user, firewall, and context changes cleanly.

### Scenario 2: Expand storage without an outage

Inventory a test disk and existing VG/LV/filesystem. Add a GPT partition and PV to the VG, extend the target LV and its supported filesystem, create a separate LV/filesystem labeled for application data, persist by stable identifier, and add swap. Use `mount -a`, confirm sizes and swap, fill only with safe test data, reboot, and verify. Then diagnose a deliberately incorrect UUID or mount option from rescue/console access.

### Scenario 3: “The service is down” layered diagnosis

Given a host that cannot be reached, do not immediately disable controls. Confirm connection profile/address/route/DNS, process/unit state and enablement, configuration syntax, listening socket, journal, file permissions, SELinux contexts/AVCs/port/boolean, firewalld zone/rules, and client-side error. Correct one root cause, validate allowed and denied paths, make persistence explicit, reboot, and confirm the incident is resolved.

## Hands-on labs

Use disposable RHEL 10 VMs from an authorized [no-cost Developer subscription](https://developers.redhat.com/products/rhel/download) or an entitled lab. Snapshot before boot/storage recovery exercises and never practice destructive commands on production or personal-data disks.

1. **Shell and local-help circuit:** complete 20 file/text/archive/link/permission tasks using only `man`, `info`, `--help`, and `/usr/share/doc`; write assertions that prove every result.
2. **RPM and Flatpak sources:** create/use a safe test RPM repository and Flatpak remote, install/remove one item from each, inspect provenance/state, break one source, and diagnose it.
3. **Scripted account report:** accept a file/group as inputs, validate them, loop through records/members, test conditions, capture command output, send errors correctly, and rerun safely.
4. **Boot/service/log recovery:** change a disposable VM's target and service activation, persist the journal, adjust a tuning profile, create one recoverable boot/service failure, and restore normal boot from console.
5. **Partition/LVM/filesystem:** create GPT storage, PV/VG/LVs, XFS/ext4/VFAT and swap as appropriate, mount by UUID/label, extend supported layers, run `mount -a`, reboot, and verify.
6. **NFS/autofs and permissions:** export or use an authorized test NFS path, mount directly and through autofs, diagnose a permission/identity/context failure, and verify on-demand behavior.
7. **Network/security layers:** configure IPv4 and IPv6 profiles, resolver/hostname, SSH keys, a test service, firewalld, and an SELinux nonstandard port/context; prove allowed and denied paths after reboot.
8. **Timed rebuild:** from a clean two-VM snapshot, complete a randomized checklist spanning all ten groups, score only observable persistent outcomes, preserve 20% of time for validation, and write an error log.

## Original knowledge checks

1. How do a shell glob and a regular expression differ?
2. What should be verified after creating an archive?
3. How do hard and symbolic links behave differently when the original name is removed?
4. Which local sources help discover an unfamiliar command option without internet access?
5. Why can a successful exit code still be insufficient evidence?
6. How do RPM and DNF responsibilities differ?
7. How does a Flatpak remote differ from a DNF repository?
8. Which checks prove repository trust and usability?
9. Why should positional parameters usually be quoted?
10. How would a script handle a missing input without partially changing state?
11. What is the difference between active and enabled for a systemd service?
12. Which evidence should be captured before restarting a failed service?
13. How do process priority and a tuned profile differ?
14. What makes journal storage persistent across reboot?
15. Why must a boot-recovery procedure end with a normal reboot test?
16. How do partition, PV, VG, LV, filesystem, and mount point relate?
17. Why use UUID or label rather than a guessed device name in `fstab`?
18. What two layers may need growth after extending storage?
19. Which preflight catches many `fstab` failures before reboot?
20. Why is “non-destructive” a separate requirement from “command succeeded”?
21. How do XFS and ext4 resize capabilities differ?
22. Why can permissions change when a filesystem is mounted on a directory?
23. What layers can cause an NFS client mount failure?
24. When is autofs preferable to a permanent boot-time mount?
25. How do cron, `at`, and systemd timers differ?
26. Why can an interactive script fail under a scheduler?
27. What proves time synchronization rather than just daemon activity?
28. How do a NetworkManager profile and current device state differ?
29. Why does ping not prove that name resolution or an application works?
30. What is the firewalld runtime/permanent distinction?
31. What happens if supplementary groups are replaced instead of appended?
32. How do password lock, account expiry, and an unusable shell differ?
33. Why can UID reuse expose old files?
34. How should a sudo rule be syntax-checked and tested?
35. How do Unix mode, firewalld, SELinux, and service configuration layer together?
36. Why is permissive SELinux mode not a durable fix?
37. When is `restorecon` preferable to `chcon`?
38. What must be correct for SSH public-key authentication to work?
39. Which validations should be repeated after every exam-style reboot?
40. What RHEL 10 objective gaps must older RHCSA material be checked for?

## RHEL 9-to-10 preparation checklist

Before relying on older material, map it line by line to the live objectives. Specifically confirm current practice for:

- RPM repository structure and current DNF behavior;
- Flatpak repository and package operations;
- simple shell scripts using arguments, command substitution, conditions and loops;
- systemd timer units alongside `at` and cron;
- GPT partitioning, LVM, UUID/label persistence, swap, VFAT/ext4/XFS and supported extension paths;
- current NetworkManager, IPv4/IPv6, hostname resolution, firewalld, SSH, SELinux and bootloader/recovery procedures;
- any removed older objectives—do not study a legacy task as current solely because it appears in an old course;
- a complete reboot-and-validate loop on the RHEL 10 minor version available to you.

## Places to learn

This is **not a complete list**, and it is not meant to be consumed in full. Select one primary RHEL 10 route, use current documentation for gaps, and spend at least as much time performing and recovering tasks as watching or reading. Provider runtimes are shown where visible; other totals are planning estimates.

| Resource | Access | Estimated time |
|---|---|---:|
| EX200 objectives and [RHEL 10 documentation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10) | Public | 8–16 hours selected mapping/reference |
| Red Hat RH124 + RH134 | Paid/RHLS | About 10 instructor-led days plus labs |
| Red Hat RH199 rapid track | Paid/RHLS | About 5 instructor-led days plus labs |
| O'Reilly / Sander van Vugt RHEL 10 video | Paid/trial | 15 hours 7 minutes plus 30–60 hours labs |
| O'Reilly / Sander van Vugt RHCSA 10 Cert Guide | Paid/book | 714 pages / 15 hours 39 minutes listed plus labs |
| O'Reilly live RHEL 10 prep | Paid | Four live days with labs and practice review |
| KodeKloud RHCSA RHEL 10 | Paid | Runtime varies; plan 35–60 hours with labs/mock exams |
| Coursera RHCSA Certification Preparation | Paid/audit varies | 45–80 hours estimated across four RHEL 10 courses/projects |

- **Official standard route:** [RH124](https://www.redhat.com/en/services/training/rh124-red-hat-system-administration-i) plus [RH134](https://www.redhat.com/en/services/training/rh134-red-hat-system-administration-ii), both based on RHEL 10. Red Hat's skills path has historically listed five days each; delivery format and lab entitlement vary.
- **Official experienced route:** [RH199](https://www.redhat.com/en/services/training/rh199-red-hat-certified-system-administrator-rapid-track-course) combines the core path for experienced Linux administrators (**about five instructor-led days** historically). It is intentionally too fast for a new Linux user.
- **Official free orientation:** [RH024](https://www.redhat.com/en/services/training/rh024-red-hat-linux-technical-overview) is a free technical overview (**about three hours**), useful before RH124 but not complete EX200 preparation.
- **Current video:** [O'Reilly/Pearson Red Hat RHCSA RHEL 10 with Exam Labs](https://www.oreilly.com/videos/red-hat-rhcsa/9780135493137/) by Sander van Vugt is **15 hours 7 minutes**, published August 2025, with lesson labs and a sample exam.
- **Current book:** [O'Reilly/Pearson Red Hat RHCSA 10 Cert Guide](https://www.oreilly.com/library/view/red-hat-rhcsa/9780135576625/) is **714 pages / 15 hours 39 minutes listed**, June 2026, with chapter labs and four practice exams.
- **Live option:** [O'Reilly Red Hat RHCSA RHEL 10 Prep](https://www.oreilly.com/live-events/red-hat-rhcsa-rhel-10-prep/0642572442705/0642572442699/) is structured as **four live days** with labs and final practice review; verify the next session times and availability.
- **Interactive labs:** [KodeKloud RHCSA](https://kodekloud.com/courses/red-hat-certified-system-administrator-rhcsa) includes extensive labs and mock exams. KodeKloud identified the current Andrei Balint course as its RHEL 10 replacement in August 2026; allow **35–60 hours** because a stable current combined runtime was not exposed.
- **Structured alternative:** [Coursera RHCSA Certification Preparation](https://www.coursera.org/specializations/rhcsa-certification-prep) is a four-course, hands-on RHEL 10 route. Allow **45–80 hours** across demonstrations, assignments, projects and independent repetition; verify individual course estimates after sign-in.
- **Practice environment:** [RHEL downloads](https://developers.redhat.com/products/rhel/download) are available through no-cost Red Hat Developer membership. Match the major version, use disposable VMs, snapshot risky exercises, and never expose an insecure lab to the internet.

No exact current EX200 Pluralsight, Whizlabs, or MeasureUp product was independently verified September 1. Avoid question-dump claims: performance readiness is demonstrated by observable system state, recovery, and persistence. A realistic total is **120–200 hours** for an experienced Linux user and **250–400 hours** for a Linux beginner.

---

## Source map and freshness notes

The live Red Hat exam page is the objective and product-version contract. RHEL 10 documentation is the technical authority. Official course pages describe recommended preparation; third-party resources are optional learning paths.

- **VERIFY CURRENT:** exact exam appointment duration/price/delivery rules, RHEL 10 minor version, objective text, DNF/Flatpak/NetworkManager/systemd/firewalld/SELinux/boot behavior, course versions, runtimes and access.
- **Stable performance pattern:** inspect → change minimally → validate runtime and policy → persist → reboot → validate again → recover/rollback.
- **Older resources:** retain for durable Linux knowledge only after closing every current RHEL 10 objective gap.

This guide uses no recalled exam tasks or restricted course content. The scenarios, labs and checks are original and test only public objectives and product behavior.
