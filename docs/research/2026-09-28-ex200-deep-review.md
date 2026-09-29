# EX200 deep review — September 28, 2026

Read the complete guide and all 62 tasks from the current [RHEL 10 exam objectives](https://www.redhat.com/en/services/training/ex200-red-hat-certified-system-administrator-rhcsa-exam). Ten groups contain 11/4/4/10/6/5/6/4/4/8 tasks. Objective and lifecycle snapshots are unchanged. Clarify that the prerequisite section accepts the named courses or comparable experience; another certification is not listed.

## Learning improvements

Add an original Bash record-report exercise with quoted paths, literal content, final unterminated lines and invalid-input handling. Explain why caller redirection can truncate an old report before a script validates its input. Supply answers to all 40 existing questions and retain the three integrated scenarios.

Make [XFS/ext4 resize boundaries](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_file_systems/overview-of-available-file-systems) explicit and account for the [RHEL 10 XFS size/format changes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/considerations_in_adopting_rhel_10/file-systems-and-storage). Explain persistent-versus-live firewall state, SELinux mappings versus applied labels, creation-mode masks and clock-source verification.

Add a service/timer pair and qualify catch-up and active-service behavior using the [upstream timer manual](https://raw.githubusercontent.com/systemd/systemd/main/man/systemd.timer.xml). Readers must verify installed-version support. Morgan Peterman's June 6, 2022 [chrony article](https://www.redhat.com/en/blog/chrony-time-services-linux) contributes a useful client validation method, corroborated with the current RHEL 10 reference. Server configuration remains related context.

## Execution boundary

Twenty-one local checks passed. Sixteen covered Bash syntax/behavior, input preservation, whitespace/backslashes/globs, empty/comment files, missing final newline, invalid inputs and the caller-redirection failure case. Three checked structural INI parsing; two checked permission-mask arithmetic. Bash version was 5.3.15(2)-release from Git for Windows.

The timer pair was not validated by systemd or activated. No RHEL VM, SELinux, firewalld, disk/LVM/filesystem, account, network-time, boot or reboot lab ran. The session's WSL startup problem remains deferred. All eight system labs are proposed, and this review does not establish performance-exam readiness. Independent human review remains pending.

## Learning catalog

Official preparation pages were read. Coursera publicly describes four RHEL 10 courses and four weeks at ten hours/week; the guide distinguishes that pacing from independent practice estimates. O'Reilly book/video pages blocked automated access, and KodeKloud's fetched public page did not independently establish the previously reported RHEL 10 replacement version. Preserve those access limits and verify signed-in course details separately. Move source notes ahead of the final Places to learn section.
