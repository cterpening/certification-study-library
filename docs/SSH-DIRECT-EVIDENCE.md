# SSH Direct evidence and validation boundary

> **VERIFY CURRENT — provisional evidence review, September 7, 2026.** This page
> explains the best-supported working model for an AZ-800/AZ-802 objective. It is not
> Microsoft support documentation, and it does not convert either blocked source review
> into a pass.

## What the evidence supports

The AZ-800 and AZ-802 blueprints establish that candidates should understand SSH Direct
for managing Linux guests. A broader search found enough evidence to explain a bounded
working model, though not enough to claim a universal current procedure.

[Microsoft's current Hyper-V socket documentation](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/make-integration-service)
confirms that Hyper-V sockets can carry host/guest streams without the networking stack.
For Linux guests it maps the Windows Hyper-V socket service to `AF_VSOCK`, requires Linux
Integration Services and kernel support for `CONFIG_VSOCKET` and
`CONFIG_HYPERV_VSOCKETS`, and lists current Windows Server host families. This is the
strongest evidence for the transport, but it does not document SSH Direct or `hvc.exe`
as an end-to-end supported workflow.

The Microsoft-owned [MSLab repository](https://github.com/microsoft/MSLab) says its
experimental Linux support provisions guests through `hv_socket`, similarly to
PowerShell Direct. Its [Debian 11 template](https://github.com/microsoft/MSLab-templates/blob/main/templates/debian-11/debian-11.pkr.hcl)
loads `hv_sock` and configures OpenSSH socket activation on `vsock::22`. This is concrete
implementation evidence, but the repository labels the Linux path experimental and the
template covers one older distribution baseline rather than a Windows Server support matrix.

The public sample from Microsoft Press's
[Windows Server 2019 Inside Out](https://ptgmedia.pearsoncmg.com/images/9780135492277/samplepages/9780135492277_Sample.pdf)
describes installing Linux virtualization extensions and an SSH server, then invoking
`hvc.exe ssh user@VMName` from an elevated Hyper-V host prompt. A
[Win32-OpenSSH issue](https://github.com/PowerShell/Win32-OpenSSH/issues/2200) in a
Microsoft-owned repository independently traces the wrapper through the Windows OpenSSH
client and `hvc.exe nc` to a Hyper-V socket. The issue is community-authored and open, so
it is diagnostic evidence rather than a support commitment.

[Thomas Maurer's 2018 article](https://www.thomasmaurer.ch/2018/04/hvc-ssh-direct-for-linux-vms-on-hyper-v/)
also describes `hvc ssh user@VMName` over VMBus. Its preview-era date and reader reports
of connections falling back to normal networking expose a key gap: installing ordinary
`sshd` is not, by itself, proof that the guest is listening on the VSOCK path.

Current Ubuntu evidence reinforces that version caveat. An
[Ubuntu OpenSSH regression report](https://bugs.launchpad.net/bugs/2110468) records
Hyper-V `hvc.exe` access working on Ubuntu 22.04 but failing on 24.04 after a required
socket-activation unit was removed; restoring the unit restored connectivity. The related
package work therefore supports the mechanism while disproving any distribution-neutral
recipe.

## Distribution evidence: examples, not recipes

Linux families package kernels, OpenSSH, systemd units, and mandatory-access-control policy
differently. Treat related distributions as separate versioned observations: Fedora is not
RHEL, CentOS Stream is not a RHEL support statement, and openSUSE Factory is not a SLES
support contract. The purpose of this matrix is to give learners and operators a useful
starting point while keeping the missing Hyper-V-specific proof visible.

| Guest family | Useful evidence found | What it supports | What remains unverified |
|---|---|---|---|
| Debian | Microsoft's experimental Debian 11 MSLab template installs OpenSSH socket activation, listens on `vsock::22`, and loads `hv_sock` | A concrete older Hyper-V guest composition | Current Debian releases, security defaults, package ownership of the units, and Microsoft support |
| Ubuntu | The Launchpad report records `hvc.exe` working with Ubuntu 22.04 and failing with 24.04 when socket activation was absent | Direct version-sensitive field evidence and a known failure mode | A supported release matrix and whether current updates install/enable the required unit by default |
| RHEL | Red Hat documents built-in Hyper-V integration for RHEL 7; RHEL 8.5 added `AF_VSOCK` listen/connect support to `socat`; RHEL 10.2 documents current VSOCK namespace behavior | The family has Hyper-V integration and current user-space/kernel VSOCK building blocks | No Red Hat document found for `hvc.exe`, an SSH-on-Hyper-V-socket unit, or a supported RHEL/Windows Server combination |
| CentOS Stream / Fedora | A current CentOS Stream 9 kernel package index lists `hv_sock.ko`; Fedora 44 packages `sshd.socket`, and current Fedora SELinux policy adds rules for SSHD VSOCK sockets | Strong Red Hat-ecosystem packaging evidence for each layer of the composition | These artifacts are not interchangeable with RHEL, and no end-to-end Hyper-V `hvc.exe` reproduction was found |
| SLES / openSUSE | A current SUSE kernel package changelog includes an `hv_sock` fix; openSUSE Factory's OpenSSH packaging describes an SSHD VSOCK listener for libvirt; SUSE Package Hub's `virtme` package uses SSH over VSOCK | SUSE-family kernels and packages actively carry the socket and SSH-over-VSOCK mechanisms | The published examples target generic/KVM VSOCK rather than Hyper-V SSH Direct; SLES versions, units, AppArmor policy, and `hvc.exe` behavior need testing |
| Oracle Linux | Oracle documents generic VSOCK configuration for its KVM guests, while Microsoft's historical [LIS 4.1 guide](https://download.microsoft.com/download/7/6/B/76BE7A6E-E39F-436C-9353-F4B44EF966E9/Linux%20Integration%20Services%20v4-1c.pdf) names Oracle Linux with the Red Hat-compatible kernel when loading `hv_sock` | Another enterprise distribution family with relevant components and historical Hyper-V evidence | UEK and RHCK must be tested separately; no current Oracle end-to-end SSH Direct guidance was found |

The supporting distribution sources are registered as bounded evidence rather than treated as
an end-to-end support contract. Relevant
pages include Red Hat's [RHEL 7 Hyper-V integration note](https://access.redhat.com/articles/2443861),
[RHEL 8.5 release notes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/8.5_release_notes/new-features),
and [RHEL 10.2 VSOCK namespace documentation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/10.2_release_notes/kernel_parameters_changes);
the [CentOS Stream 9 kernel package index](https://rpmfind.net/linux/RPM/centos-stream/9/baseos/x86_64/kernel-modules-core-5.14.0-704.el9.x86_64.html),
[Fedora OpenSSH package inventory](https://packages.fedoraproject.org/pkgs/openssh/openssh-server/fedora-44.html),
and [Fedora SELinux policy changelog](https://packages.fedoraproject.org/pkgs/selinux-policy/selinux-policy-devel/fedora-44-updates.html);
the [SUSE 16 kernel package changelog](https://packagehub.suse.com/packages/kernel-default/6_12_0-160000_37_1/),
[openSUSE Factory OpenSSH change](https://www.mail-archive.com/commit@lists.opensuse.org/msg100679.html),
and [SUSE virtme package history](https://packagehub.suse.com/packages/virtme/1_35-bp157_1_1/);
and Oracle's [VSOCK interface documentation](https://docs.oracle.com/en/operating-systems/oracle-linux/cockpit/cockpit-kvm_cpu_mem_autostart.html).
Upstream systemd now documents automatic SSH binding to `AF_VSOCK` port 22 for a VM, but
that behavior begins with systemd 256 and does not by itself prove that a distribution ships,
enables, or supports the generator—or that Hyper-V `hvc.exe` interoperates with it. See the
[systemd VM interface](https://systemd.io/VM_INTERFACE/) and
[libvirt's SSH proxy documentation](https://www.libvirt.org/ssh-proxy.html) for the generic
composition.

## Read-only guest preflight

Before changing a disposable guest, collect its actual capabilities. These commands are
examples for common systemd-based distributions; a missing command, file, package, unit, or
socket is evidence to record rather than a reason to improvise a production change.

```bash
cat /etc/os-release
uname -r
systemd --version
ssh -V
modinfo hv_sock
grep -E '^CONFIG_(VSOCKETS|HYPERV_VSOCKETS)=' "/boot/config-$(uname -r)"
systemctl list-unit-files --type=socket | grep -Ei 'ssh|vsock'
systemctl cat sshd.socket sshd@.service
ss -A vsock -lpn
```

On RPM-based guests, also capture:

```bash
rpm -q kernel-core kernel-modules-core openssh-server systemd socat
```

On Debian-family guests, capture:

```bash
dpkg-query -W openssh-server systemd
```

If present, record `getenforce` or `aa-status` and relevant denials. Do not disable SELinux,
AppArmor, host-key verification, or the normal SSH service merely to make a test pass. Do not
copy a unit file across distributions without reviewing its executable paths, socket-activation
contract, authentication policy, security labels, ownership, and rollback.

## Confidence matrix

| Proposition | Confidence | Boundary |
|---|---|---|
| SSH Direct is a local Hyper-V-host-to-Linux-guest management path | High | Blueprint, Microsoft Press, Microsoft-owned code, and independent evidence agree |
| The intended data path uses Hyper-V sockets/VSOCK rather than guest IP networking | Medium-high | Hyper-V sockets are documented; the SSH composition lacks a dedicated current product article |
| The host entry point is `hvc.exe ssh user@VMName` | Medium-high | Microsoft Press and several implementations agree; current command lifecycle/support is undocumented |
| The guest needs Hyper-V/VSOCK kernel support plus an SSH server listening on VSOCK | High as a technical model | Exact unit names and configuration vary by distribution/systemd/OpenSSH version |
| Normal SSH authentication and host-key behavior apply unchanged | Medium | OpenSSH is in the observed chain, but Microsoft has not published the supported authentication contract |
| The feature works without a connected guest virtual NIC | Medium | The socket substrate is network-independent; older field reports show false positives and setup failures |
| One published recipe is supported across current Windows Server and Linux versions | Low | No current compatibility matrix, lifecycle statement, or complete support/troubleshooting article was found |

## Safe validation plan

Use only a disposable Hyper-V host/guest pair that you are authorized to change. Before
testing, record the Windows Server build, `hvc.exe` presence/help output, VM configuration,
Linux distribution/kernel, `hv_sock`/VSOCK support, systemd and OpenSSH versions, and the
exact guest socket units. Do not substitute ordinary TCP SSH for the target path.

1. Establish an ordinary network-SSH control and record the guest listener, host key, and
   authentication method.
2. Configure a distribution-appropriate VSOCK listener from a reviewed source; capture
   unit files, enabled state, listener evidence, and guest logs.
3. Invoke `hvc.exe ssh user@VMName` from an elevated local Hyper-V host and record command,
   exit status, host-key prompt, authenticated identity, and guest log correlation.
4. Disconnect or disable only the disposable guest's virtual NIC and repeat. A session
   that fails here has not demonstrated SSH Direct even if ordinary SSH worked earlier.
5. Test invalid credentials, a stopped VSOCK listener, a stopped VM, and an unknown VM name.
   Record whether failures distinguish identity, guest service, VM lookup, and transport.
6. Restore the original SSH/systemd/module configuration and virtual NIC, then prove the
   baseline state. Never weaken host-key checks or production SSH policy for convenience.

A successful run validates only the recorded host/guest/version combination. A failed run
is still useful when the exact layer, logs, and rollback result are recorded. Promote the
relevant sources and update the guides only after review confirms the commands, security
boundary, failure evidence, and cleanup. Keep searching for a current Microsoft SSH Direct
article or compatibility statement; it should supersede this provisional synthesis.

## Evidence status

The exact sources are registered in `data/sources.json` with publisher, authority, access,
supported-exam, and qualification notes. Registration means the URLs and their limited claims
were reviewed; it does not mean every source is vendor support documentation or that the
composed workflow was validated. No runtime lab was performed during this research pass, so
AZ-800 and AZ-802 retain their human-review warning and the missing Microsoft compatibility
matrix remains an explicit concern.
