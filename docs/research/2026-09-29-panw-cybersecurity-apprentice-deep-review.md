# Palo Alto Networks Cybersecurity Apprentice deep review — September 29, 2026

The [Apprentice guide](../../guides/PANW-CYBERSECURITY-APPRENTICE-palo-alto-networks-cybersecurity-apprentice.md) now maps 39 objective entries, answers 40 original prompts and includes three worked scenarios, eight proposed infrastructure activities and 43 executed local Python checks. Infrastructure and independent human review remain pending.

## Scope and contract

The complete five-page [May 2026 datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/apprentice-datasheet.pdf) retains seven weights: 16/16/14/10/13/13/18. The saved counts 6/7/6/3/6/7/4 remain accurate; the four identity entries include the 13 nested IAM, PAM, PKI and secrets topics. Both blueprint table pages were visually checked. The snapshot is unchanged. Automatic extraction of the shorter certification landing still requires manual review; this is separate from manual PDF verification.

The handbook is now dated September 2026, superseding the guide's July 2025 citation. Its complete eight pages were read. The complete four-page September FAQ supplies a published $150 foundational fee before applicable extras, although the datasheet omits price. Its fee table was visually checked. Item count and base duration remain unverified. Pearson's public main distinguishes total appointment time and links a program-specific OnVUE information page; the handbook describes test centers. Actual delivery eligibility and personal terms still require the booking. No account, registration, purchase, system test or policy change occurred.

## Actual local evidence

All 43 standard-library Python checks passed. Real `ipaddress` arithmetic partitions a documentation-only /24 into four nonoverlapping /26 networks. Small routing and policy models illustrate a more specific discard route, same-zone default access and an earlier broad allow shadowing a later deny. These models omit actual routing, App-ID, NAT, wildcard exceptions and session state; no packets or device configuration were used.

Ten synthetic events at threshold60 produce TP2/FP1/FN1/TN6: observed precision and recall are2/3. Threshold40 yields TP3/FP3/FN0/TN4: precision1/2 and observed recall1. With an assumed eight minutes per alert, workload grows from24 to48 minutes. Two known malicious events outside the collected set reduce threshold60 population recall to2/5. Real unknown ground truth cannot be inferred from this fixed fixture; collection health and detector quality need separate evidence.

A partial PRI parser separates facility/severity and rejects malformed values. A timezone exercise normalizes equivalent instants, computes a seven-second supplied timestamp difference and flags a negative value as a clock/order question. It is not a complete syslog parser or latency measurement. Trusted-label access cases deny wrong audience, write permission, expiration, revoked access, disabled owner and unverified issuer. They perform no cryptographic verification, real authentication or revocation propagation.

## Technical source boundaries

The complete [policy reference](https://docs.paloaltonetworks.com/network-security/security-policy/administration/security-rules) explains ordered matching, predefined intra/interzone rules and configurable logging. Its TCP-only DNS example is not adopted as a universal DNS transport rule: RFC7766 introduction/section5 require general-purpose UDP and TCP support. Exact installed application definitions remain unverified. Model-specific quota wording was not adopted.

Selected RFC5424 transport, header, time-quality and security sections support the distinction between parsed messages, accurate time, authenticated delivery and complete collection. The full RFC and separate TLS transport standard were not reviewed. Selected current NIST authenticator sections distinguish OTP replay resistance from phishing resistance and human-password requirements from machine-secret lifecycle. The official publication landing confirms the 2025 final edition. The Zero Trust publication abstract was read, not its whole PDF. AWS's complete responsibility page supplies one provider example; no cross-provider universal boundary is asserted.

## Catalog and release review

Twenty-three direct receipts show20HTTPsuccesses and3blocked sources. Generic HTML extraction of PDF bytes is not meaningful text evidence; genuine PDF bytes, hashes and local extraction were captured separately. The digital learning path remains a loading shell. Academy's public free-course entry was read without course access. Both CISA main/PDF routes were blocked; only a selected indexed primary excerpt was readable. O'Reilly's earlier publication/duration metadata was not reverified.

Pluralsight's full public catalog main includes current path cards alongside older exam labels and an expired October2025 offer. No paid lessons, entitlement, Apprentice-specific coverage or quality guarantee was established. CSA's public landing lists12domains but the full download asks for login; no document interior was accessed. The vendor video channel was not played.

The September17 vendor identity article by Avihay Nathan was fully read through its FAQ. It supplies context for machine/agent inventory, constrained access and audit attribution; product claims, adoption/incident ratios and linked Gartner research were not independently validated. The technical directory's PAN-OS12.2 metadata and NIST's draft AI-assisted CSF guide are separate from exam scope. No Apprentice retirement or dated blueprint replacement was identified in the reviewed primary material.

## Remaining work

The operation at `ADLC_Docs/operations/2026-09-29-panw-cybersecurity-apprentice-deep-review.json` records objective mapping, PDF comparison/receipts, source reading boundaries, exact local code/output, resource observations and repository checks. Pending work consists of public access gaps, booking specifics, installed behavior, infrastructure exercises and human review. The five reserved GitHub guides and disabled notification pilot remain untouched.
