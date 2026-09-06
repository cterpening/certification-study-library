# SSH Direct evidence and validation boundary

> **VERIFY CURRENT — provisional evidence review, September 6, 2026.** This page
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

A successful run validates only the recorded host/guest/version combination. Promote the
relevant sources and update the guides only after review confirms the commands, security
boundary, failure evidence, and cleanup. Keep searching for a current Microsoft SSH Direct
article or compatibility statement; it should supersede this provisional synthesis.

## Candidate status

All seven exact sources are queued in `data/source-candidates.json`. They are not yet in
the trusted source catalog, and no runtime lab was performed during this research pass.
