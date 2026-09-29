# Fortinet NSE 4 FortiOS deep review — September 29, 2026

The [guide](../../guides/NSE-4-FORTIOS-fortinet-nse-4-fortios.md) maps 18 current tasks and 89 supporting details, answers 40 original readiness prompts and includes three worked scenarios, eight proposed device activities and 41 executed offline Python checks. Live infrastructure and human review remain pending.

## Current and announced scope

The complete visible [exam page](https://training.fortinet.com/local/staticpage/view.php?page=fortios_administrator_exam) still marks 7.6 Available: FortiOS 7.6.0, 100 minutes, 50–55 questions and English/Japanese. Five published domain ranges remain 20–25/20–25/25–30/10–15/10–15 percent; they are not normalized point weights. The 18 tasks contain 89 details, distributed 34/17/22/10/6. Snapshot differences affect five heading formats only. The old exact objective/status bytes are archived and historical review/audit references preserved; the checklist’s old 80–90 minutes is corrected.

The same page marks 8.0 Coming Soon without a visible date or detailed contract. An initial web parser exposed details from an HTML comment. Direct DOM inspection established that they are not visible published scope; none were adopted. The catalog’s existing scheduled label records an undated announcement, not a launch date. The status extractor now handles inline/separate statuses on mixed current/future pages; a regression check also excludes HTML comments. Fresh live extraction agrees with the accepted snapshots.

The complete track and assessment FAQ distinguish next-version exams, conditional newer assessments and higher-level renewal routes. Transitioned FCP dates remain the original dates; no automatic new two-year term is assumed. The public track lists centers/OnVUE, but booking availability, fees and personal eligibility were not inspected. All-or-nothing item credit does not establish the passing percentage.

## Technical corrections and evidence

VIP policy priority qualifies simple first-match teaching. A deny without VIP matching may lose to a lower VIP allow. Central SNAT uses its map instead of the IPv4 policy NAT option. Unused VIP/IP-pool objects can affect local address ownership with ARP reply enabled. The guide adds original negative cases and explains the difference between tuple transformation and successful application access.

HA TCP synchronization differs from UDP/ICMP/QUIC handling and cannot guarantee every session survives. Conserve-mode reachability can coexist with inspection bypass. Certificate-only inspection can still generate an HTTPS replacement page signed by the firewall CA; this is not evidence of full payload decryption. Authorized inspection CA trust is distinguished from the untrusted-marker CA. No certificates, policies, services or devices were changed.

Versioned routing/SLA sources support blackhole fallback, reverse-path checks, application-relevant targets and failure/restore counters. FSSO agent/collector/polling distinctions and DHCP pool/relay dependencies are explicit. Cloud/SASE sources were read only at introduction/overview level; their full onboarding and compatibility remain pending.

Some phase 2 prose overgeneralizes selector and replay behavior. Selected RFC 7296 section 2.9 explains address/port/protocol traffic selectors and narrowing; selected RFC 4303 section 3.4.3 explains a receive window and integrity before state advancement. These qualify the guide without claiming a complete standards audit or installed-device verification. Questionable algorithm wording and legacy choices in configuration lists were not adopted as security recommendations.

All 41 local checks passed. Real IP address arithmetic and chosen models cover static route candidates, two prequalified VIP rules, tuple translation, SLA thresholds/counters, selected inspection-pressure outcomes, HA synchronization candidates and a synthetic DHCP range. The interrupted failure sequence resets the counter; three selected failures mark down and two successes restore. Eleven synthetic lease addresses remain. Models omit actual forwarding, dynamic metrics, RPF, NAT state/allocation, cryptography, device inspection engines and live continuity; no timing, performance or deployment result is claimed.

## Sources and resource boundaries

Thirty-seven direct receipts show 34 HTTP successes and 3 blocked sources. The official 7.6 course, Udemy and O’Reilly interiors remain inaccessible; no samples or paid lessons were consumed. The public course-description page actually describes 7.4.1 with 12 hours lecture and 10 hours lab. It does not verify the 7.6 course. Pluralsight’s older public metadata and CBT’s 233-video/zero-practice-exam 7.6 listing are separated from lesson quality, entitlement and unpublished duration. No video playback occurred.

The full April 6 vendor 8.0 blog supplies product context only; marketing and cryptography wording were not adopted as verified requirements or an exam cutover. The 7.6 new-features directory contains later maintenance features distinguished by version suffix. Reading boundaries for each article, partial standard and directory are retained in the operation record.

## Remaining work

The operation at `ADLC_Docs/operations/2026-09-29-nse-4-fortios-deep-review.json` records original snapshots, manual acceptance, all source boundaries, detailed task mapping, exact executed code/output and repository gates. Remaining work is signed-in learning access, account-specific booking/renewal details, real device/cluster/cloud/identity/PKI activities and human review. The five reserved GitHub guides and disabled notification pilot remain untouched.
