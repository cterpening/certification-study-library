---
exam_code: SC-300
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: review-required
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# SC-300 Microsoft Identity and Access Administrator Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; OFFICIAL WEIGHTING CONFLICT OPEN; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 28, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#sc-300-coverage-record). The [official SC-300 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) is authoritative.

**Current baseline:** Skills measured as of April 27, 2026; official study-guide page last updated March 27, 2026.<br>
**Exam state:** Active; the official credential page lists no retirement date.<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 28, 2026.<br>
**Published weighting discrepancy:** The study guide's “Skills at a glance” assigns authentication and access management 25–30%, while its detailed heading says 20–25%. This guide uses 25–30% for planning because it is the summary-table value, but the Microsoft page remains the source of truth. **VERIFY CURRENT** before allocating study time.<br>
**Localized exams:** Microsoft says localized versions normally follow the English update by approximately eight weeks; verify your language version before scheduling.<br>
**Official source:** [SC-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300)

## How to use this guide

SC-300 tests whether you can operate identity as a control plane, not whether you recognize portal labels. For every feature, practice this reasoning chain:

```text
business subject and resource
  -> authoritative identity and lifecycle owner
  -> authentication and authorization decision
  -> least-privilege scope and time boundary
  -> policy, provisioning, and application dependencies
  -> logs, investigation, remediation, and recurring review
```

Read Sections 1–4, work the three integrated scenarios, complete or tabletop all ten labs, and answer the 48 original checks with the answer key. Use a disposable tenant where licensing permits; many governance, risk, application-control, and Global Secure Access tasks require licenses or infrastructure beyond a free tenant. Never weaken a production tenant merely to reproduce a learning exercise.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

The [September 28 deep review](../docs/research/2026-09-28-sc-300-deep-review.md) maps all **98 objectives in 16 groups**. The April baseline remains unchanged. Operational changes below include the September 30 Connect deadline, October 1 legacy risk-policy retirement, November 3 `memberOf` deadline and January 6 Cloud Apps file-policy retirement. These are product lifecycle dates, not invented exam revisions.

## Exam profile and complete objective map

The certification is intermediate and renews every 12 months. The current exam page gives 100 minutes for the proctored assessment and provides a free Practice Assessment and exam sandbox. Microsoft expects Azure and Microsoft 365 familiarity, AD DS knowledge, and practical PowerShell and KQL skill. Confirm administrative details on the [Identity and Access Administrator Associate credential page](https://learn.microsoft.com/en-us/credentials/certifications/identity-and-access-administrator/).

| Official domain | Planning weight | Operating question |
|---|---:|---|
| Implement and manage user identities | 20–25% | How are tenant, workforce, device, external, and hybrid identities created, delegated, licensed, synchronized, and removed? |
| Implement authentication and access management | 25–30%* | How should strong authentication, Conditional Access, risk, sessions, and Global Secure Access combine without locking out the organization? |
| Plan and implement workload identities | 20–25% | Which nonhuman identity and application-integration pattern gives the required access without unmanaged credentials or excessive consent? |
| Plan and automate identity governance | 20–25% | How is access requested, approved, time-bounded, reviewed, monitored, and removed? |

\*The detailed heading on the same official page says 20–25%; see the disclosure above.

### Published objective-to-guide map

| Published objective area | Primary coverage | Practice evidence |
|---|---|---|
| Tenant roles, administrative units, effective permissions, domains, branding, and tenant/user/group/device settings | Section 1 | Scenario 1; Lab 1 |
| Users, groups, custom security attributes, bulk operations, devices, and licenses | Section 1 | Scenarios 1–2; Labs 1–2 |
| External collaboration, invitations/accounts, cross-tenant access/synchronization, and external IdPs | Section 1 | Scenario 2; Lab 2 |
| Connect Sync, Cloud Sync, PHS, PTA, seamless SSO, AD FS migration, and Connect Health | Section 1 | Scenario 1; Lab 3 |
| CBA, TAP, OAuth 2.0 tokens, Authenticator, passkeys, MFA, SSPR, Windows Hello, session revocation, password protection, and Entra Kerberos | Section 2 | All scenarios; Lab 4 |
| Conditional Access assignments/controls/testing/sessions/device restrictions/CAE/authentication context/protected actions/templates | Section 2 | All scenarios; Lab 5 |
| User/sign-in/workload risk and authentication registration | Section 2 | Scenarios 1 and 3; Labs 4–5 |
| Global Secure Access client, Private Access, Internet Access, and Microsoft 365 traffic | Section 2 | Scenario 3; Lab 5 |
| Managed identities, service principals, user/service accounts, and Azure resource access | Section 3 | Scenario 3; Lab 6 |
| Enterprise applications, App Proxy, SaaS integration, assignments/app roles/consent/collections | Section 3 | Scenario 2; Labs 6–7 |
| App registrations, authentication, API permissions, and app roles | Section 3 | Scenario 3; Labs 6–7 |
| Defender for Cloud Apps discovery, connectors, restrictions, Conditional Access app control, access/session/OAuth policies, and catalog | Section 3 | Scenario 2; Lab 7 |
| Entitlement management, catalogs, access packages/requests, terms of use, external lifecycle, and connected organizations | Section 4 | Scenario 2; Lab 8 |
| Access reviews; PIM for Entra roles/Azure resources/Groups; approvals; audit; emergency access | Section 4 | All scenarios; Lab 8 |
| Sign-in/audit/provisioning logs, diagnostics destinations, KQL, workbooks/reporting, and Identity Secure Score | Section 4 | All scenarios; Labs 5 and 8 |

## 1. Implement and manage user identities

### Model the tenant and administrative boundary first

A Microsoft Entra tenant is an identity and policy boundary. Before creating objects, identify verified domains, data and regulatory boundaries, administrative ownership, external collaboration model, device strategy, emergency access, and whether the organization actually needs another tenant. Multiple tenants add isolation but also add cross-tenant policy, provisioning, monitoring, lifecycle, and incident-response work.

Separate Microsoft Entra directory roles from Azure RBAC roles. A directory role authorizes management of Entra and connected Microsoft services; an Azure role authorizes operations at management-group, subscription, resource-group, or resource scope. Assign the least privileged built-in role at the narrowest workable scope. Create a custom role only after proving that built-in roles cannot express the task, and test effective permissions including direct assignments, role-assignable groups, administrative-unit scope, PIM state, ownership, and default user permissions.

Administrative units (AUs) scope supported directory-role management to selected users, groups, or devices. They are delegation containers, not security walls: AU members may still be discoverable and users retain default directory permissions. Restricted management AUs provide stronger protection for sensitive objects but have constraints. The current [administrative-units overview](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/administrative-units) documents supported objects, licensing, and limitations.

Use this selection model:

| Need | Prefer | Avoid assuming |
|---|---|---|
| Help desk manages users only in one region | AU-scoped supported role | AU hides every object outside the region |
| Team manages one Azure resource group | Azure RBAC at resource-group scope | An Entra role grants data-plane access |
| Rare tenant-wide privileged task | Eligible Entra role through PIM | Permanent Global Administrator |
| Permission set absent from built-ins | Tested custom Entra role | Custom roles can contain every Microsoft service permission |

### Worked example 1: effective permission depends on the object and operation

Assume Alice belongs to an ordinary regional AU and Bob belongs to a [restricted management AU](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/admin-units-restricted-management). Neither is a privileged administrator, and the actors have no additional assignments.

| Actor and attempted operation | Expected boundary |
|---|---|
| Regional AU-scoped User Administrator resets Alice | Allowed within supported role/scope |
| Tenant-scoped User Administrator resets Bob | Blocked by restricted AU protection |
| User Administrator explicitly scoped to Bob's restricted AU resets Bob | Allowed within supported role/scope |
| Azure resource-group Reader resets either user | Azure read permission does not grant directory password-reset authority |

Global Administrator can administer the restricted AU and assign a scoped role, creating an auditable privilege path; the restriction is not an absolute barrier against tenant administrators. It blocks protected directory-object changes, not every related Exchange, Intune or SharePoint operation, and does not hide normal read properties. Graph application permissions alone do not bypass it: the application needs the applicable Entra role at restricted-AU scope.

Restricted management must be chosen at AU creation. Current limitations exclude Microsoft 365/mail-enabled/distribution groups and prevent supported governance workflows such as PIM, access reviews and entitlement management from managing protected users/groups. A role-assignable group placed there cannot have its membership changed through the normal role paths. Test lifecycle and recovery before using the feature; do not put every privileged object there by reflex.

Custom domains require ownership verification through DNS before they can be used as Entra sign-in domains. Plan the initial `.onmicrosoft.com` dependency, default-domain change, DNS ownership, federated-domain behavior, and workload/service accounts before renaming users. Company branding affects sign-in experience and anti-phishing recognition, but it is not an authentication control. Tenant properties and user, group, and device settings should be deliberately baselined and periodically exported rather than left at inherited defaults.

> **Related item:** Separate configuration authority from business approval. A User Administrator might execute a change, while HR, the resource owner, or a data steward remains accountable for why the identity or access should exist.

### Create and govern workforce identities

Treat user identity as a joiner–mover–leaver lifecycle:

1. Establish the authoritative source and immutable matching identifier.
2. Create or synchronize the account with required attributes and manager/organization context.
3. Assign access through governed groups, app roles, access packages, or eligible roles—not a growing set of direct grants.
4. Update access when the job, geography, employment type, or risk changes.
5. Disable access promptly, revoke sessions where necessary, remove licenses and privileged eligibility, transfer ownership, retain evidence, then delete according to policy.

Choose groups by workload and authorization behavior. Security groups govern access broadly; Microsoft 365 groups also provide collaboration resources. Assigned membership is explicit; dynamic membership evaluates a rule and is not instantaneous. Role-assignable groups protect privileged role assignment and have creation/management constraints. Nesting behavior varies by consuming service, so validate the effective resource authorization rather than only the group graph.

[Role-assignable groups](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/groups-concept) must be created with the immutable role-assignable setting; an existing group cannot be converted. They use assigned membership and have stronger membership/credential administration controls. Keep these distinct from ordinary PIM-enabled groups, which do not all need to be role-assignable.

Audit [memberOf-based rules before November 3](https://learn.microsoft.com/en-us/entra/identity/users/groups-dynamic-rule-member-of). Affected dynamic groups, dynamic AUs and entitlement auto-assignment policies stop updating and keep their last state. Replace them with supported rules or explicit assignment, then test membership and downstream authorization; frozen membership can preserve excessive access.

Custom security attributes are typed, tenant-defined key/value data assigned to supported Entra objects. Their attribute-definition and attribute-assignment roles are deliberately separate, and their values can support filtering or attribute-based access scenarios. They are not the same as directory extensions or dynamic-group attributes. Define an owner, allowed values, sensitivity, deactivation/change procedure, and permitted consumers before using them. Microsoft's [custom-security-attributes overview](https://learn.microsoft.com/en-us/entra/fundamentals/custom-security-attributes-overview) explains the separate definition and assignment control planes.

Custom security attributes require separately assigned definition/assignment permissions, even for broad administrators. An attribute value is useful only if the consuming authorization mechanism supports it; cross-tenant synchronization does not copy custom security attributes. Do not treat them as a universal replacement for groups or synchronized directory extensions.

Bulk operations in the admin center, Microsoft Graph PowerShell, or Graph API need input validation, duplicate handling, throttling/retry, dry-run or pilot scope, structured error capture, and post-change reconciliation. Prefer the Microsoft Graph PowerShell SDK over obsolete AzureAD/MSOnline examples. Never assume that a command succeeded for all records because the script returned without a terminating error.

Device **registration** normally represents a personally owned device associated with a work account; Microsoft Entra **join** makes Entra the primary device identity for an organization-owned device; **hybrid join** combines AD DS domain join with Entra registration. Device identity enables signals and SSO, while Intune compliance expresses management posture. Neither should be mistaken for user authentication or resource authorization.

License assignment can be direct or group-based. Model prerequisite service plans, mutually exclusive products, usage location, delayed processing, and license removal. Report both assigned licenses and provisioning errors. Group-based licensing improves lifecycle automation but does not replace entitlement review or application authorization.

For [group licensing](https://learn.microsoft.com/en-us/entra/identity/users/licensing-groups-assign), nested-only users do not inherit the group's assignment. When moving users between licensed groups, add the destination, verify successful license application and service plans, then remove the source; asynchronous processing can otherwise interrupt access.

> **Related item:** A stable object ID is safer for automation than a mutable UPN or email address. Human-readable identifiers change during mergers and name/domain changes; design correlation and audit evidence accordingly.

### Implement external and cross-tenant identity deliberately

External collaboration settings control who can invite guests, guest directory visibility, and domain restrictions. Cross-tenant access settings govern inbound and outbound B2B collaboration/direct-connect access with Entra organizations and whether to trust MFA or compliant/hybrid-device claims from a partner tenant. These are different layers. Microsoft’s [cross-tenant access overview](https://learn.microsoft.com/en-us/entra/external-id/cross-tenant-access-overview) explains default, organization-specific, inbound, outbound, and trust settings.

Invite an individual or bulk set of external users only after defining sponsor, purpose, resource, expiry, acceptable-use/terms, and removal conditions. The resource tenant controls authorization; the home tenant normally controls authentication. Do not trust a partner's MFA or device claim merely for convenience—document the assurance agreement, scope it, monitor it, and maintain a fallback if the partner configuration changes.

Cross-tenant synchronization is a push provisioning process from a source tenant into a target tenant. It creates, updates, and deprovisions B2B collaboration objects in scope; configure automatic redemption, attribute mappings, scoping, and target-tenant inbound synchronization trust together. It does not make two tenants one boundary. Microsoft's [cross-tenant synchronization overview](https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-overview) is the current starting point.

Cross-tenant sync supports source internal members, not source external users or internal guests. A source-to-target relationship is directional; reverse synchronization requires its own configuration. The documented cycle starts at 40-minute intervals, with additional processing time: it is not an emergency revocation SLA. Removing an in-scope source user from scope soft-deletes the target object, but incident response must also consider existing sessions and application access. Target-side edits are not continuously overwritten just because the source is authoritative; the engine processes source changes. Verify a user's manager is also in scope before expecting manager provisioning.

For external IdPs, know protocol and lifecycle boundaries. SAML/WS-Fed federation can authenticate supported external users, but claims mapping, issuer/certificate rollover, domain discovery, fallback, account linking, and deprovisioning still require design. Test both successful authentication and loss of eligibility. Invitation redemption and authorization must not depend on an email address remaining unique forever.

> **Related item:** B2B access, cross-tenant synchronization, multitenant organizations, and entitlement management can complement one another. Draw which tenant owns the human, guest object, app, policy, access package, logs, and removal action before selecting a feature.

### Select and operate hybrid identity

Microsoft Entra Connect Sync runs a synchronization engine on a Windows server and supports mature/customized hybrid scenarios. Cloud Sync uses lightweight provisioning agents and cloud configuration, including useful multi-forest and high-availability patterns. Microsoft's current [hybrid scenarios comparison](https://learn.microsoft.com/en-us/entra/identity/hybrid/common-scenarios) should drive selection; feature coverage and migration eligibility change, so **VERIFY CURRENT** before committing to an architecture.

Synchronization and authentication are separate decisions:

| Pattern | Credential validation | Resilience and security implication |
|---|---|---|
| Password hash synchronization (PHS) | Entra validates a derived hash synchronized from AD DS | Cloud authentication can continue through on-prem outage; supports leaked-credential risk detection; protect sync path and writeback |
| Pass-through authentication (PTA) | On-prem agents validate the password against AD DS | Avoids cloud password-hash validation but depends on healthy, secured agents and connectivity |
| Federation/AD FS | Federated service authenticates and issues token/claims | Supports special cases but adds certificates, endpoints, farm, proxy, monitoring, and outage/attack dependencies |
| Seamless SSO | Provides intranet SSO alongside PHS or PTA | Convenience feature, not a fourth primary authentication method |

Inventory relying-party trusts, claims rules, authentication methods, domain settings, certificates, network paths, legacy authentication, and rollback before migrating AD FS. Pilot a domain or group, use staged rollout where supported, test modern and legacy application paths, retain emergency cloud-only administration, and validate sign-in logs before final cutover.

Connect Health and synchronization/provisioning logs reveal agent health, export/import errors, latency, duplicate attributes, and authentication-agent problems. Build alerts and ownership around them. A green sync scheduler does not prove that every object and attribute arrived correctly; reconcile samples and error populations at both ends.

**VERIFY CURRENT:** Microsoft now describes Cloud Sync as the future direction and has phased migration tooling, but not every Connect Sync customization is supported. Use the [Connect-to-Cloud-Sync migration guidance](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/migrate-azure-ad-connect-to-cloud-sync) for the actual tenant's eligibility and coexistence constraints.

### Current hybrid maintenance boundaries

[Connect Sync and Health hardening](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/security-updates-pks) requires Connect Sync **2.5.79.0 or later by September 30**, with a separate Health-agent minimum **4.5.2466.0**. Old Sync versions lose synchronization; old Health agents lose specified alerts. Neither absence of alerts nor a green agent proves every object is synchronized.

The [current release history](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history) lists 2.6.92.0 (September 23), fixing PTA registration in 2.6.91.0; the minimum 2.5.79.0 reaches its listed support end on October 23. Download through the Entra admin center and validate staging, compatibility, app-scoped CA and rollback. Minimum enforcement and supported release selection are separate decisions.

[Application authentication](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/authenticate-application-id) also has its own lifecycle: new installations configure it; existing legacy-account servers are not automatically converted by background sync. Managed certificates depend on the Connect scheduler for rotation; BYOC makes the operator responsible for certificates, while BYOA adds app/permission ownership. Verify configured app ID, certificate expiry, key protection, scheduler and rotation rather than inferring success from a version number.

## 2. Implement authentication and access management

### Build an authentication-method strategy

Start with threat resistance and recovery, not “enable MFA.” Inventory user populations, devices, platforms, accessibility, offline/emergency requirements, privileged roles, contractors, and legacy protocols. Use the Authentication methods policy as the current control plane and phase out duplicated legacy MFA/SSPR settings. Microsoft's [authentication-methods management reference](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods-manage) explains how policies coexist.

Understand the methods and their roles:

- Passkeys/FIDO2 and certificate-based authentication can provide phishing-resistant authentication when correctly configured. Validate attestation/AAGUID or certificate trust, revocation, mapping, and recovery requirements.
- Microsoft Authenticator supports push/number matching and passwordless phone sign-in; configure context and suspicious-activity reporting deliberately.
- A Temporary Access Pass (TAP) is a time-limited bootstrap/recovery credential for registering stronger methods. Scope policy and issuance roles, choose one-time versus reusable behavior, verify the user before issuance, and audit use. See the [TAP configuration guide](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-temporary-access-pass).
- OAuth 2.0 access/refresh tokens and OpenID Connect ID tokens serve different protocol purposes. An ID token describes authentication to the client; it is not an API access token. Revoking a session does not guarantee immediate rejection of every cached access token; resource support, token lifetime, CAE, and application behavior matter.
- SMS, voice, and passwords may be needed for transitional populations but are weaker than phishing-resistant methods. Do not count every MFA combination as equivalent assurance.

[Certificate-based authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-certificate-based-authentication) can authenticate directly to Entra without AD FS, but requires your own PKI, trusted issuers, certificate-to-user binding and revocation design. Issuer/policy-OID rules determine single-factor versus multifactor status; a certificate alone does not prove the configured authentication strength was met. The current overview supports one HTTP CRL distribution point per trusted CA, not OCSP/LDAP URLs. Windows web sign-in and Office/browser support are distinct scenarios; test the exact client and recovery path.

The [SMS/voice transition](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement) separates default/preferred passkeys, registration and actual enforcement. Microsoft-provided delivery is scheduled to end February 1, 2027 for most users, including internal guests; Global Administrators and external users move to July 1. Provider alternatives have their own private-preview prerequisites. [System-preferred MFA](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-system-preferred-multifactor-authentication) preference is not a guarantee that every sign-in uses a phishing-resistant method.

Tenant-wide MFA can be achieved through Conditional Access or, for simpler tenants, security defaults; per-user MFA is a legacy control. Keep emergency access protected with phishing-resistant credentials while excluding it from policies that could make it unusable. Registration campaigns can nudge users toward Authenticator or passkeys, and Microsoft-managed defaults can change. **VERIFY CURRENT:** the current [registration-campaign guidance](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-mfa-registration-campaign) describes passkey-targeting rollouts that older courses will not show.

SSPR requires scope, allowed methods, registration, authentication count, writeback for applicable hybrid users, notifications, and help-desk verification/recovery design. Combined MFA/SSPR registration reduces duplicate enrollment but policy requirements still combine. Monitor reset and registration events and test a user who has lost every normal factor.

Windows Hello for Business binds a user gesture to device-protected asymmetric credentials; the PIN is local to the device, not a reusable network password. Choose Entra-only or hybrid deployment and the applicable cloud Kerberos, key, or certificate trust. Microsoft's [Windows Hello authentication flow](https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/how-it-works-authentication) explains PRT and on-premises Kerberos behavior.

For [Entra Kerberos hybrid access](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-passwordless-security-key-on-premises), prepare the supported clients/DCs, synchronized SID/domain/account attributes, required deployment roles and Entra Kerberos server object for the domain. The object is not a physical domain controller. Entra supplies a partial TGT; the client still contacts on-premises AD DS to obtain a full TGT and service tickets. Cloud authentication therefore does not remove on-premises authorization or network dependencies. Validate key lifecycle and the supported sign-in scenario before assuming a FIDO2 desktop demonstration also supports RDP, server sign-in or another client.

Password protection blocks weak/global/custom terms in cloud password changes and can extend to AD DS using agents. Plan proxy/DC-agent health, audit-to-enforce rollout, custom banned terms, and monitoring. For a suspected compromise, distinguish disabling the account, resetting credentials, revoking sessions, revoking application consent, disabling devices, and confirming/remediating risk; one action rarely covers every token and workload path.

> **Related item:** Authentication strength is a Conditional Access abstraction describing acceptable method combinations. It lets policy express “phishing-resistant” instead of hard-coding one method, but enrollment and recovery still need their own design.

### Design, test, and troubleshoot Conditional Access

Conditional Access evaluates signals and policy assignments, then applies grant and session controls. Think in four blocks:

```text
assignments: users/workload identities + target resources + conditions
  -> grant: block or require one/more controls
  -> session: frequency, persistence, app control, token protection, CAE behavior
  -> evidence: report-only result, sign-in log, policy detail, user impact
```

Build a baseline set rather than one enormous policy: protect administrators, require appropriate MFA/authentication strength, block legacy authentication, handle device/location/risk, protect registration and administrative actions, and control guests/workloads as required. Exclude only emergency accounts and documented technical exceptions. Use named locations as a signal, not as proof of identity.

Deploy in report-only to a representative pilot, inspect sign-in results, use the What If tool, test positive and negative cases, document dependencies, then enforce progressively. During troubleshooting, identify the exact sign-in, user, client, resource, device state, IP/location, risk, authentication details, applied/not-applied policy, grant/session result, and token timing. Do not edit several policies until the symptom disappears; that destroys causal evidence.

### Worked example 2: an excluded client can still request a protected resource

[Baseline-scope enforcement](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-enforcement-resource-exclusions) changes certain All resources policies that contain resource exclusions. Its dedicated guidance and updated Microsoft blog specify rollout beginning June 15; older general resource-targeting prose mentions March. Use current tenant settings and sign-in evidence rather than assuming a calendar date proves rollout.

| Request under the affected policy configuration | Enforcement change described in current guidance |
|---|---|
| Public client, only `openid`/`profile` | Baseline scopes now evaluated; configured controls can challenge |
| Excluded confidential client, only baseline directory scopes such as `User.Read` | Baseline directory access now evaluated |
| Excluded confidential client, only OIDC scopes | No change from this update |
| Request includes nonbaseline API scopes | Existing resource evaluation continues; this update does not create a blanket bypass |

Distinguish initiating client, requested API/resource, scopes and Conditional Access audiences. Do not add unnecessary API permissions to avoid a challenge. A custom placeholder resource is a documented policy-specific compatibility mechanism, not a way to distinguish every individual client requesting the same baseline resource. Tenant-wide Disable enforcement preserves the older coverage gap. Prefer fixing client challenge handling and narrowing legitimate exceptions, then test in a disposable tenant. Enabling this setting can enforce immediately; it is not an observation-only simulation.

[New-policy app protection](https://learn.microsoft.com/en-us/entra/identity/conditional-access/migrate-approved-client-app) must be separated from the old approved-client-app grant. Since June 30, legacy policies are read-only but enabled policies still enforce; they can be disabled/deleted. Test a supported app-protection replacement before retiring the legacy policy.

Session controls include sign-in frequency, persistent browser behavior, application-enforced restrictions, Conditional Access app control, token protection, and customized continuous access evaluation. CAE lets supported resources react to critical events and policy/location changes without waiting for ordinary token expiry; it does not make every application continuously reevaluate. Consult the current [Conditional Access session-control reference](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-session) for support boundaries.

Authentication context lets an application label a sensitive operation/resource so Conditional Access can require step-up controls. Protected actions apply authentication context to supported Entra permissions such as high-impact policy changes. Confirm that the calling tool supports the context and retain a recovery path. Policy templates are accelerators, not organization-specific designs: review assignments, exclusions, controls, licenses, and interactions before enabling.

Device-enforced restrictions depend on the consuming application and device signal. For example, an unmanaged browser may receive a limited SharePoint experience rather than universal device control. Map the policy to the application's supported behavior and test desktop, browser, and mobile clients.

> **Related item:** Conditional Access is a policy engine after first-factor authentication, not a firewall and not an entitlement system. It cannot repair excessive app permissions, stale group membership, or an unauthenticated network path by itself.

### Manage identity risk and registration

Microsoft Entra ID Protection produces risk detections and calculates sign-in risk (likelihood this authentication is not legitimate) and user risk (likelihood the identity is compromised). Workload identity risk covers service principals. Use risk-based Conditional Access for user self-remediation where appropriate, and investigate the underlying detections, sign-in context, device, application, and correlated security evidence.

A risky sign-in may be remediated by strong MFA; user risk may require secure password change or administrator action. “Dismiss risk” is not containment. Confirming safe, confirming compromised, blocking, resetting, revoking, and dismissing have different meanings and audit effects. Microsoft's current [risk-remediation guidance](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock) describes self, system, threat-informed, and administrator remediation.

[Legacy user/sign-in risk policies retire October 1, 2026](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies). Create separate CA policies for user risk and sign-in risk, inspect report-only results, enable the replacements and then disable the old policies. Combining both risk conditions can unintentionally narrow coverage. Verify MFA registration and hybrid writeback before requiring remediation.

Current [Require risk remediation guidance](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-policies) handles **user risk**, with password or passwordless remediation depending on the detected threat. It automatically adds authentication strength and Every time sign-in frequency. Passwordless reauthentication is not always a password change; an attacker-added device can require device disablement. External/guest users are unsupported for this remediation control. Keep sign-in-risk remediation separate, and distinguish secure password change within the remediation flow from ordinary SSPR or a password change elsewhere. Inspect the resulting risk/session/device evidence rather than treating dismissal as containment.

For risky workload identities, there is no human to perform MFA or a password reset. Investigate owners, credential use, permissions, service-principal sign-ins, source, code/deployment changes, and affected resources. Disable or isolate safely, rotate/remove credentials, prefer managed identity or federated credential, reduce permissions, restore the workload, and verify logs. Do not break a critical service without a tested recovery owner.

[Workload Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity) covers directly targeted single-tenant service principals registered in the tenant. Managed identities and Microsoft/third-party multitenant SaaS apps are excluded. A group containing a service principal does not make a group-targeted CA policy apply to it. The grant is Block, not human MFA; use the enterprise application's service-principal object ID and inspect its sign-in results. Workload Identities Premium is required to create/edit these policies.

Registration policy is part of risk reduction. Scope authentication methods, use registration campaigns, bootstrap securely with TAP, require strong authentication to change security info, protect registration events with Conditional Access, and monitor anomalous additions. An attacker who registers their own factor can retain access after a password reset.

### Implement Global Secure Access as identity-aware networking

Global Secure Access unifies Microsoft Entra Internet Access and Private Access. Traffic profiles acquire Microsoft, private, or internet traffic through supported clients or remote-network paths and apply the service's security and Conditional Access capabilities. The [Global Secure Access overview](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access) is the current product boundary.

- **Private Access** is ZTNA for defined private FQDN/IP resources and ports/protocols. Quick Access covers broad primary destinations; per-app Global Secure Access applications provide finer segmentation. Private network connectors broker access without publishing the resource directly.
- **Internet Access** routes supported internet/SaaS traffic for filtering and threat protection.
- **Internet Access for Microsoft services** (the Microsoft traffic profile) optimizes and secures supported Microsoft traffic and can enforce tenant restrictions.

Plan client deployment, remote networks, connectors, DNS/FQDN/IP segments, overlapping routes, traffic-profile assignment, Conditional Access, logging, high availability, bypasses, coexistence with VPN/SSE tools, and rollback. Validate user traffic with the traffic logs and client diagnostics, not merely a green configuration blade.

**VERIFY CURRENT:** client/platform support, remote-network acquisition, licensing, TLS inspection, traffic categories, and Conditional Access limitations change quickly. Read [known Global Secure Access limitations](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-current-known-limitations) immediately before a design or exam.

Current limitations are architectural constraints, not just a setup checklist. Clientless remote-network acquisition supports Microsoft/Internet profiles but does **not** enforce the user CA controls supplied by the GSA client. Private Access requires the client; apply its CA to the Quick Access/GSA application, not an assumed traffic-profile control. Compliant-network checks are not supported for Private Access apps. The Internet profile's custom bypass does not apply to branch connectivity, so configure any required branch bypass on the CPE. Verify platform/version-specific Universal CAE and explicit-forward-proxy targeting separately.

> **Related item:** Application Proxy remains a strong option for publishing supported web applications with Entra preauthentication. Private Access covers broader private network resources and protocols; choose based on resource type, segmentation, client, connector, and policy requirements rather than treating one as a universal replacement.

## 3. Plan and implement workload identities

### Select the correct nonhuman identity

Avoid human accounts for unattended work. Select by hosting, ownership, lifetime, and resource boundary:

| Identity | Best fit | Credential/lifecycle concern |
|---|---|---|
| System-assigned managed identity | One Azure resource with the same lifetime | Service principal is deleted with resource; sharing is not the goal |
| User-assigned managed identity | Several Azure resources or independent identity lifecycle | Explicit assignment/removal and permission ownership required |
| Service principal from app registration | Application must work across tenants, outside supported managed-identity hosting, or expose APIs | Prefer certificate/federated credential; govern owners, permissions, consent, and rollover |
| Managed service account/gMSA | Supported on-premises Windows service | AD DS scope, host authorization, and password management still matter |
| User account | Interactive human work | Poor choice for automation; MFA, employment, password, and license lifecycle can break it |

A managed identity is represented by a service principal but has no app-registration application object. Azure manages its authentication material. The workload requests a token for a resource/audience and authorization is still granted at the destination. Managed identity removes stored credentials; it does not automatically grant least privilege. See the [managed-identities FAQ](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/managed-identities-faq).

Treat the hosting resource as a managed identity security boundary: code running there may request its tokens. Explicitly choose the identity when a host has multiple user-assigned identities; adding another identity can break a request that relied on an implicit default. A successful token request still needs the correct audience and destination role/app permission.

The FAQ documents a backend cache per resource URI for around **24 hours**, with permission changes potentially taking hours and no forced early token refresh. Reauthentication alone is not proof that a managed identity lost access. Use a verified resource/host containment action during an incident, and test actual resource operations after permission removal. Preserve user-assigned identity lifetime separately from the compute resource.

For every workload identity, record owner, purpose, hosting resource, tenant, allowed resources/scopes, credential or federation method, expiry/rotation, deployment path, sign-in baseline, incident action, and deletion dependency. Prefer workload identity federation for supported external CI/CD or Kubernetes scenarios over static secrets.

> **Related item:** Authentication asks “which workload is this?” Authorization asks “what may it do?” Secretless authentication solves credential handling, not excessive RBAC or API permissions.

### Integrate and govern enterprise applications

An **application object** is the app definition in its home tenant. A **service principal** is a tenant-local instance used for sign-in, consent, assignment, and policy. The Enterprise applications blade primarily manages service principals; App registrations primarily manages application objects. Be able to trace a setting to the correct object.

For a gallery or custom SaaS application, determine protocol (SAML, OIDC/OAuth, password-based where unavoidable), identifiers and reply URLs, signing/encryption certificates, claims, user assignment, group/app-role mapping, provisioning method such as SCIM, owners, consent, Conditional Access, test users, monitoring, rollover, and decommissioning. Requiring user assignment limits who can sign in even after tenant-wide consent. Collections organize apps in My Apps; they do not create a security boundary.

Application Proxy publishes supported on-premises web apps through outbound connectors. Plan connector groups, capacity/HA, DNS/certificates, preauthentication, SSO method, Conditional Access, backend authorization, headers, timeouts, and legacy protocol constraints. Test when a connector, certificate, backend, or identity provider is unavailable.

User consent grants delegated permissions within policy. Admin consent can grant tenant-wide delegated or application permissions. Configure verified-publisher and permission-classification boundaries, use the admin-consent workflow for exceptions, and periodically review grants. The [user/admin consent overview](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/user-admin-consent-overview) distinguishes the flows. A trusted publisher is not proof that every requested permission is justified.

Assign application-management roles by task: Application Administrator and Cloud Application Administrator differ, and highly privileged Microsoft Graph application permissions can require stronger authority. Ownership grants substantial object management ability and must be reviewed. Do not give Global Administrator merely to configure SSO.

### Register applications securely

Plan supported account types, redirect URIs, client type, token version, scopes, app roles, delegated versus application permissions, owner model, credential/federation, and multitenant provisioning before clicking Register.

- **Delegated permission:** the app acts for a signed-in user; effective access is constrained by user access and granted scopes.
- **Application permission:** the app acts as itself without a user; it can be broad and normally requires administrator consent.
- **Scope:** delegated API permission represented in an access token's `scp` claim.
- **App role:** role that can be assigned to users/groups or applications and represented in the `roles` claim.

Use least-privilege API permissions, exact redirect URIs, certificates or federation instead of client secrets, short and monitored credential lifetimes, multiple owners with accountable review, and separate development/test/production registrations. Validate token audience, issuer, tenant, signature, lifetime, and required claims in the API; possession of any token is not authorization. Microsoft's [app-registration security guidance](https://learn.microsoft.com/en-us/entra/identity-platform/security-best-practices-for-app-registration) covers credentials, redirects, permissions, ownership, and instance locking.

Credential rollover must overlap safely: add the new credential, deploy and verify its use, then remove the old credential and monitor failures. Emergency rotation needs an application owner, dependency inventory, and rollback. Deleting an app registration can affect service principals and production integrations; disable/test/decommission through a controlled process.

> **Related item:** OAuth consent phishing abuses legitimate authorization. Restrict user consent, verify publishers, investigate unusual grants, review service-principal permissions, and connect consent events to workload sign-ins and resource activity.

### Discover and control cloud application access

Defender for Cloud Apps (MDCA) uses Cloud Discovery data to identify app use and assess cloud-app risk. Connected-app connectors use provider APIs for visibility and control. The Cloud app catalog supplies app characteristics and scores; organizational sanctioning remains a risk decision, not an automatic verdict.

Application-enforced restrictions pass device/session context to supported apps for their native limited experience. Conditional Access app control uses a reverse-proxy session between the user and supported app to monitor or enforce activity such as download, upload, copy, print, or step-up authentication. Access policies control entry; session policies control activity after entry. Test application/client compatibility, user experience, data classification, and bypass paths. See the current [Conditional Access app-control overview](https://learn.microsoft.com/en-us/defender-cloud-apps/conditional-access-app-control-how-to-overview).

OAuth app policies detect and govern applications based on permissions, publisher, usage, and other risk signals. Investigate owners, consent grant, permissions, activity, users, and business purpose before revoking, then monitor reauthorization. Cloud Discovery policies can alert on high-volume, new, risky, or unsanctioned apps; connected security products may enforce tags.

**VERIFY CURRENT:** MDCA policy types and portals are changing. Microsoft currently states that file policies retire January 6, 2027 in favor of Purview DLP or auto-labeling. Use the [current cloud-app policy reference](https://learn.microsoft.com/en-us/defender-cloud-apps/control-cloud-apps-with-policies) and do not build new study notes around a retiring workflow.

The [file-policy migration tool](https://learn.microsoft.com/en-us/defender-cloud-apps/migrate-file-policies-to-purview) currently supports SharePoint/OneDrive DLP policies in commercial Production environments. Auto-labeling and non-Microsoft-app migrations are not covered by the tool. Inspect full/partial/unsupported verdicts and payloads. New Purview policies start in **Test with notifications**, keep the originals, and require deployment plus enforcement validation; a Created in Purview result is not protection equivalence. A policy targeting both locations can become two policies. Check conditions, governance-action gaps and per-policy results before disabling the originals.

The [Cloud Apps release feed](https://learn.microsoft.com/en-us/defender-cloud-apps/release-notes) also distinguishes August default unified RBAC for **new customers** from existing deployments. Suppressing informational unsanctioned-app alerts does not turn off the corresponding block. Confirm effective roles and enforcement independently of alert volume.

## 4. Plan and automate identity governance

### Design entitlement management as a lifecycle

Entitlement management packages resources and policy into repeatable access experiences:

- A **catalog** is a governed collection of resources and access packages with delegated owners.
- An **access package** bundles resource roles such as groups, applications, and SharePoint sites.
- A **policy** defines who may request, approval, justification, lifecycle/expiry, access reviews, and compatible external users/organizations.
- A **connected organization** represents an external directory/domain relationship for request policy—not automatic trust of all users.
- **Terms of use** records acceptance but does not replace legal review, authorization, or technical enforcement.

Start with resource owner and access rationale. Separate requestor, sponsor, approver, catalog owner, and reviewer where risk warrants. Time-bound assignments, require justification, configure escalation/fallback, review recurring access, and define what happens to an external account after its last assignment ends. The [entitlement-management overview](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-overview) explains automatic invitation and external lifecycle behavior.

Automatic assignment can use supported user attributes for scalable birthright access, but bad source data becomes bad authorization at scale. Validate mappings, exclusion/removal behavior, and a sample of effective access. API automation should be idempotent, preserve request/approval evidence, handle throttling, and reconcile actual assignments to policy.

> **Related item:** Access packages govern resource access; lifecycle workflows automate joiner/mover/leaver tasks; HR-driven provisioning supplies identity events. They can form one lifecycle but have different triggers, evidence, and failure modes.

### Implement access reviews that actually remove stale access

Choose the review subject (group, application, access package, Entra/Azure role, or PIM group), scope, reviewer, recurrence, duration, decision helpers, reminder/escalation, default decision, and apply-results behavior. Resource owners often judge business need better than central IT; users can attest but may rubber-stamp their own access.

An access review captures the population for an instance. Nested groups and indirect assignments can prevent an apparent denial from removing underlying access. Confirm the review decision was applied, inspect exceptions/errors, verify effective resource access, and retain evidence. Microsoft's [access-review creation guide](https://learn.microsoft.com/en-us/entra/id-governance/create-access-review) documents current snapshot and nesting behavior.

Use denial by default only when the organization is prepared for missed reviews. Make recommendations explainable, include last sign-in/access context where available, and establish a manual route for ambiguous cases. Measure completed decisions, denied access actually removed, exceptions, reviewer latency, and recurrence—not merely review creation.

### Worked example 3: count removed access, not only review decisions

Across review results, assume 12 denied access relationships: five direct cloud group memberships, three nested-group paths, two on-premises-synchronized memberships and two disconnected-app entitlements. After successfully applying the five supported direct removals, **five are removed and seven still require action**. A denial alone proves none removed. [Apply-results guidance](https://learn.microsoft.com/en-us/entra/id-governance/complete-access-review) also distinguishes dynamic groups and application access inherited from group assignments: changing the decision does not change the underlying rule or group membership. Inspect errors, authoritative owner and effective resource access for each path.

[Catalog reviews](https://learn.microsoft.com/en-us/entra/id-governance/catalog-access-reviews) combine groups, applications and custom data resources in a user-oriented review. They require Governance or Suite licensing, and changes within 12 hours before review start might not be included. The catalog is a review scope, not proof of complete tenant-wide access visibility.

For [disconnected resources](https://learn.microsoft.com/en-us/entra/id-governance/custom-data-resource-access-reviews), upload access data during Initializing, within the documented two-hour window. Use stable principal/permission/resource identifiers and validate the upload in audit logs. Current custom-resource setup instructions describe a single-stage manager-review path; do not assume every general catalog multi-stage option applies. Remove denied access in the external system, verify it, then record the apply result manually or through integration. Creating a ticket or marking Applied successfully is not proof that the external permission disappeared.

### Implement privileged access and emergency recovery

PIM provides eligible/time-bound activation, approval, MFA/authentication context, justification/ticket information, notifications, access reviews, and audit for Entra directory roles, Azure resource roles, and group membership/ownership. These are related but separate resource planes. Configure role settings per role/resource based on impact.

An effective privileged model includes separate daily/admin identities, phishing-resistant authentication, privileged workstations, least scope, eligible rather than standing access, approval for critical roles, short activation, monitored actions, and periodic review. Avoid approval by another equally exposed account or a circular dependency where the only approver cannot activate.

PIM for Groups makes membership or ownership eligible. The group can then confer application, Azure, Entra, SQL, Key Vault, Intune, or other access. This is powerful and can hide privilege behind nesting; trace the group to every downstream assignment. Microsoft's [PIM for Groups overview](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups) distinguishes member and owner activation policies.

### Worked example 4: activation and downstream readiness have different clocks

Eight users activate a PIM group for the same provisioned application within ten seconds. Current PIM documentation describes expedited SCIM provisioning for the first **five**, normally 2–10 minutes; the remaining **three** fall back to the next normal 40-minute cycle. These are documented processing expectations, not a guarantee of usable application access at a specific second. Target-app propagation and sessions add another boundary. Test both grant and expiry/removal in the application.

Use a baseline low-privilege group to keep required app accounts provisioned, with a separate eligible privileged group for elevation. For Entra roles governing Exchange, SharePoint or Purview, Microsoft recommends role eligibility with active group membership to avoid the longer activation delays of eligible group membership. PIM for Groups excludes dynamic and on-premises-synced groups. Active nesting into a role-assignable group is prohibited; an eligible-group path activates the requesting individual, not every member of the eligible group.

Review PIM audit history, role assignments, activations, approvals/denials, expired assignments, alerts, and changes to role settings. Correlate them with directory audit logs, sign-ins, and Azure activity/resource logs. A justified activation proves a request was made, not that every subsequent action was appropriate.

Maintain at least two cloud-only emergency access accounts with permanent active Global Administrator, independent phishing-resistant credentials, secure storage, monitoring, and regular validation. Exclude them from Conditional Access controls that could block emergency use while continuing to monitor report-only results. Microsoft's [emergency-access guidance](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access) currently recommends validation at least every 90 days. **VERIFY CURRENT** authentication and mandatory-MFA requirements when testing.

> **Related item:** Emergency access is an availability control and a high-value attack path. A perfect lockout bypass that is never monitored is not a safe design.

### Monitor identity activity and prove control effectiveness

Know the evidence types:

| Evidence | Primary question |
|---|---|
| Sign-in logs | Who/what attempted authentication to which resource, under what client/device/location/risk, and what authentication/CA result occurred? |
| Audit logs | Which actor or service changed which directory object or policy, and what was the result? |
| Provisioning logs | Which source object was evaluated, matched, created/updated/skipped/failed, and why? |
| PIM/access-review/entitlement records | Who requested, approved, activated, reviewed, expired, or removed governed access? |
| Workload identity sign-ins | Which service principal or managed identity requested tokens and from where? |

Configure diagnostic settings to send required Entra log categories to Log Analytics for KQL/alerting, a storage account for cost-effective retention, Event Hubs for streaming to external systems, or a supported partner destination. Destinations serve different uses; choose retention, immutability, latency, access, residency, and cost deliberately. The [Entra diagnostic-log options](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-diagnostic-settings-logs-options) list current categories.

### Worked example 5: a license upgrade cannot recreate expired logs

A tenant upgrades from Free to P1 and requests the previous 30 days of sign-ins. Without earlier export, only the **seven days** still retained under Free are available; **23 days** of the requested window cannot be recovered merely by upgrading. Current [retention guidance](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/reference-reports-data-retention) lists seven days for Free audit/sign-in logs and 30 for P1/P2. Risky sign-in retention differs by license, while unresolved risky-user/workload records have a different lifecycle.

Entra activity logs and the Microsoft 365 Unified Audit Log are separate stores. Diagnostic routing must precede the evidence you need to retain. Graph activity logs begin when enabled and require storage/analytics integration; they are not automatically held in a portal history. In investigations, record event and ingestion times, pagination, source category, stable IDs and the unobserved interval before calculating coverage or asserting no activity occurred.

Build KQL around an investigative question and normalize time, identities, applications, IPs, and result codes. Useful exercises include failed-then-successful sign-ins, new credential plus privileged action, unusual service-principal source, Conditional Access failure by policy, provisioning failures by reason, emergency-account use, or risky user without remediation. Join only on stable keys and account for ingestion latency and table/category availability.

Workbooks should expose a decision—authentication-method adoption, risky identity trend, legacy-auth usage, CA impact, provisioning health, privileged activations, or external-user aging—with time/scope parameters and drill-through to raw records. Reporting is not control effectiveness until an owner responds to thresholds.

Identity Secure Score measures alignment with Microsoft recommendations. Use it to prioritize and track improvement, but validate applicability, license, compensating controls, business impact, and actual implementation. A higher score is not proof that identity is secure. See [Identity Secure Score](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-identity-secure-score).

> **Related item:** Preserve evidence outside the identity plane for high-impact incidents. If an attacker changes diagnostic settings or deletes an identity, independently retained SIEM/storage records may be the only defensible timeline.

## Integrated scenarios

### Scenario 1: Hybrid enterprise removes standing privilege and AD FS

**Situation:** A company has one forest, AD FS, permanent tenant administrators, per-user MFA, weak recovery, and no reliable identity monitoring. It wants cloud authentication and time-bound administration without interrupting a legacy claims application.

**Reasoning:** Inventory sync scope, claims, certificates, authentication methods, service accounts, roles, applications, break-glass dependencies, and logs. Establish two tested cloud-only emergency accounts. Pilot converged authentication registration and phishing-resistant methods; use TAP only through verified issuance. Choose PHS unless an evidenced requirement justifies PTA/federation, and use staged rollout for cloud authentication. Preserve the legacy app's federation until claims compatibility is tested. Convert suitable admin roles to PIM eligibility with task-specific settings and approvals. Export sign-in, audit, provisioning, PIM, and risk records to Log Analytics; alert on emergency-account use and role-setting change.

**Evidence of success:** Pilot authentication works on/off corporate network; SSPR/writeback and lost-factor recovery are tested; sync and sign-in errors are owned; legacy claims match; emergency access works independently; PIM activation and denial paths are logged; rollback is timed; permanent privilege is reduced without losing recovery.

### Scenario 2: Govern partner access to a sensitive SaaS application

**Situation:** Consultants from three companies need six-month access to a SaaS case-management system. Downloads must be limited on unmanaged devices, and access must disappear when the engagement ends.

**Reasoning:** Configure organization-specific cross-tenant access only after agreeing whether partner MFA/device claims are trusted. Use entitlement-management connected organizations, a catalog, an access package, sponsor/owner approval, terms of use, expiration, and recurring review. Assign an app role rather than broad direct access and require user assignment. Configure SSO/provisioning, Conditional Access, and supported MDCA session controls for unmanaged access. Test invitation/redemption, access, provisioning, limited session, denial, expiry, deprovisioning, and guest-object cleanup.

**Evidence of success:** Every consultant has sponsor, package/policy, app role, expiry, accepted terms, authentication source, and review decision; app and resource logs show expected controls; expired/denied users lose effective access; exceptions are visible and owned.

### Scenario 3: Secure a deployment workload and private administration plane

**Situation:** A CI service uses an expiring client secret with subscription Contributor. Administrators reach a private deployment API by VPN, and a risky workload sign-in has appeared.

**Reasoning:** Investigate service-principal sign-ins, credential changes, consent, owners, pipeline history, and Azure activity. Contain with the workload owner and rotate/remove the suspected credential. Replace static secret authentication with workload identity federation or a managed identity where hosting supports it. Narrow Azure RBAC to the deployment resources/actions and separate application API permission. Publish the private API with Private Access or Application Proxy according to protocol, deploy redundant connectors/client path, and enforce Conditional Access. Monitor workload sign-ins, role/credential changes, resource operations, and GSA traffic.

**Evidence of success:** Pipeline deploys without stored secret; token audience/issuer/subject and resource scope are exact; old credential fails; unrelated subscription actions are denied; private access fails closed as designed; connector/client failure and rollback are tested; risky workload state is resolved with a documented timeline.

## Hands-on labs

Use a disposable tenant and synthetic identities. Where a license or infrastructure is unavailable, perform a tabletop with screenshots/documentation and write the expected evidence. Clean up resources and assignments after each lab.

### Lab 1 — Delegate tenant administration safely (60–90 minutes)

1. Create synthetic users/groups and, if licensing permits, an administrative unit.
2. Assign a supported AU-scoped role to a test administrator; compare with a tenant-scoped role and Azure RBAC.
3. Test allowed and denied operations in separate sessions.
4. Inspect effective role assignments and audit logs.
5. Export a before/after configuration record and remove assignments.

**Deliverable:** permission matrix showing directory versus Azure scope, inheritance/group/PIM state, successful/denied operations, and log evidence.

### Lab 2 — Automate identity and external lifecycle (75–120 minutes)

1. Use Microsoft Graph PowerShell to create/update a small batch of synthetic users or groups with validation and error capture.
2. Define a custom security attribute set/value if available and assign it with separately delegated roles.
3. Invite a guest, record sponsor and expiry, and compare external collaboration with cross-tenant settings.
4. Disable/delete test objects and verify audit evidence and cleanup.

**Deliverable:** idempotent script or runbook, input/output reconciliation, guest lifecycle record, and rollback/cleanup proof.

### Lab 3 — Compare hybrid identity designs (60–90 minutes tabletop; longer with AD DS)

1. Document requirements for one-forest and multi-forest cases.
2. Compare Connect Sync and Cloud Sync current support, then PHS, PTA, and federation.
3. Draw agents/servers, network paths, credential validation, monitoring, outage behavior, and rollback.
4. Build a migration runbook with pilot, staged rollout, sign-in-log tests, and go/no-go gates.

**Deliverable:** evidence-based decision record and failure-mode diagram, with volatile feature assumptions marked **VERIFY CURRENT**.

### Lab 4 — Bootstrap and recover strong authentication (60–90 minutes)

1. Build an authentication-method policy for a pilot group.
2. Issue a short-lived synthetic TAP under a documented identity-verification process.
3. Register a passkey/FIDO2 or other strong method; inspect registration audit events.
4. Test lost-factor recovery, account disable, and session revocation behavior.
5. Remove the test method/TAP and restore tenant policy.

**Deliverable:** enrollment/recovery threat model, audit timeline, and explanation of which tokens/sessions each response action affects.

### Lab 5 — Deploy and troubleshoot Conditional Access (90–120 minutes)

1. Create a report-only pilot policy using assignments, a grant control, and an explicit emergency-account exclusion.
2. Test allowed, blocked, out-of-scope, and exception cases; use What If and sign-in logs.
3. Add a session/device/risk or authentication-strength condition if licensed.
4. Design a GSA Private Access or Internet Access test and list current limitations if it cannot be deployed.
5. Produce enforcement and rollback criteria before cleanup.

**Deliverable:** policy interaction matrix, four sign-in evidence records, GSA dependency map, and controlled rollout decision.

### Lab 6 — Replace a workload secret (75–120 minutes)

1. Register a test application and inspect its application object and service principal.
2. Grant a minimal test resource/API permission and demonstrate a denied operation outside scope.
3. Replace a client secret with managed identity, certificate, or federated credential as the environment supports.
4. Rotate/remove the old credential and inspect workload sign-in, consent, audit, and resource logs.

**Deliverable:** identity/object diagram, token claim checklist, least-privilege proof, credential rollover record, and cleanup evidence.

### Lab 7 — Integrate and control an enterprise application (90–150 minutes)

1. Configure a safe gallery/test application or tabletop SAML/OIDC integration.
2. Require assignment, create an app role, assign a test group, and document consent.
3. Add provisioning or Application Proxy design where applicable.
4. Design/test MDCA access or session policy behavior and an OAuth-risk investigation.
5. Remove assignment/consent and verify that effective access ends.

**Deliverable:** SSO/provisioning sequence, certificate/credential rollover plan, consent record, session-policy test, and decommission checklist.

### Lab 8 — Govern, review, and monitor access (90–150 minutes)

1. Design or create a catalog/access package with request, approval, expiry, and review policy.
2. Configure/tabletop PIM for an Entra role, Azure role, and group; compare their resource scopes.
3. Perform an approve/deny/expire cycle and verify effective access removal.
4. Route available logs to Log Analytics and write KQL for privileged activity or provisioning failures.
5. Build a small workbook/report and assess one Identity Secure Score recommendation.

**Deliverable:** lifecycle evidence chain from request through removal, KQL query/result, dashboard decision, and control-effectiveness assessment.

### Lab 9 — Prove access removal across four authorities

Use synthetic direct, nested, synchronized and disconnected assignments to reproduce the twelve-denial example. Record each authoritative system, decision, apply state, change operation and actual resource test. Build a catalog-review upload using fake IDs/data, with initialization deadline and integration outcome evidence; do not upload production personal data for practice. Compare a regular AU with restricted-AU governance constraints before choosing a design.

**Deliverable:** decision-to-removal ledger, exception owners, timestamps, external-system verification and cleanup. A successful status alone is insufficient. No review or external access change was executed during this repository review.

### Lab 10 — Test identity change and delayed evidence

Tabletop the baseline-scope matrix, legacy-risk replacement, sync/Health minimums and app-certificate rotation. Model eight simultaneous PIM activations, then trace directory membership through provisioning to the target app. Compare a managed-identity permission change with its resource test, and a 30-day investigation with seven retained days. With disposable licensed resources available, test only approved harmless cases and preserve emergency access.

**Deliverable:** expected/observed timeline, policy audiences, scope/client conditions, negative tests, missing-data boundaries and rollback. Remove test policies/assignments/resources after verification. No tenant operation, token request, KQL execution or live policy test was performed here.

## Knowledge checks

These are original prompts, not recalled or reconstructed exam questions. Answer with a decision, why alternatives are weaker, implementation boundaries, evidence, and rollback.

### User identities

1. A regional help desk must reset only its own users. When is an AU-scoped role appropriate, and what does it not isolate?
2. An engineer has no direct role but can change an enterprise app. Which effective-permission paths must you inspect?
3. When should an authorization design use a custom security attribute rather than a group or directory extension?
4. What failure and reconciliation controls belong in a Graph PowerShell bulk-user process?
5. Contrast Entra registered, Entra joined, and hybrid joined devices without equating join state with compliance.
6. How can group-based licensing fail even when the user is a group member, and what evidence would you collect?
7. Contrast external collaboration settings, cross-tenant access settings, and cross-tenant synchronization.
8. What must be agreed before trusting a partner tenant's MFA or device claims?
9. Compare Connect Sync and Cloud Sync, then separately compare PHS, PTA, and federation.

### Authentication and access

10. Design a secure TAP issuance and passkey enrollment process for a remote new starter.
11. Why is “MFA enabled” insufficient as an authentication assurance statement?
12. Which actions would you combine after suspected account takeover, and why is session revocation alone insufficient?
13. How would you deploy a Conditional Access policy without locking out administrators?
14. Which sign-in-log fields distinguish a policy assignment problem from a failed grant control?
15. Contrast sign-in frequency, CAE, authentication context, and protected actions.
16. When do application-enforced restrictions differ from device compliance requirements?
17. Contrast sign-in risk, user risk, and workload identity risk and their remediation paths.
18. Design GSA acquisition and policy for private, Microsoft, and general internet traffic; list the current limitations you must verify.

### Workload identities and applications

19. Choose between system-assigned and user-assigned managed identity for two resources that share an authorization identity.
20. Why does managed identity eliminate a stored secret but not eliminate permission risk?
21. Draw the relationship between an app registration's application object and tenant service principal.
22. Contrast delegated permission, application permission, scope, app role, and Azure RBAC.
23. What belongs in a safe certificate/secret rollover procedure for a production app?
24. How do requiring assignment and granting tenant-wide admin consent interact?
25. When would Application Proxy be preferable to Private Access, and which dependencies would decide?
26. Design a least-privilege SaaS SSO/provisioning integration with evidence for deprovisioning.
27. Contrast Cloud Discovery, connected apps, the cloud app catalog, an OAuth policy, an access policy, and a session policy.

### Governance and monitoring

28. How do catalog, access package, policy, connected organization, and terms of use relate?
29. What source-data failure could turn an automatic access-package assignment into mass overauthorization?
30. Why might a denied access review not remove effective access?
31. Compare PIM for Entra roles, Azure resources, and Groups, including how hidden privilege can arise.
32. Why should emergency accounts be permanently active yet excluded from blocking Conditional Access policies?
33. Which logs prove an identity was provisioned, authenticated, activated a role, and changed a resource?
34. Choose among Log Analytics, storage, and Event Hubs for identity logs under three different requirements.
35. Write the reasoning for a KQL detection joining a new app credential to subsequent workload sign-in and privileged action.
36. Why can Identity Secure Score improve while material identity risk remains?

### Answer key

1. Use a supported directory role scoped to the regional AU; it does not grant Azure permissions or hide the rest of the tenant.
2. Inspect ownership, group-based roles, eligible/active PIM, default user permissions, app-specific assignments and scope.
3. Use one when a supported consumer needs governed typed attributes with separate definition/assignment roles; validate source and consumer support.
4. Validate input, scope a pilot, handle throttling/partial failures, log per-object outcomes and reconcile resulting objects.
5. Registration associates a work identity; join uses Entra device identity; hybrid join combines AD DS join with Entra registration. Compliance is separate.
6. Check direct versus nested membership, processing state, available units, usage location, conflicting/dependent service plans and workload provisioning.
7. Collaboration governs invitations/guest visibility; cross-tenant settings govern B2B directions and claims trust; sync provisions scoped objects.
8. Agree assurance, supported methods/device state, scope, ownership, monitoring, emergency response and changes to the partner configuration.
9. Sync selection depends on topology/features; authentication selection separately determines who validates credentials and outage dependencies.
10. Verify the person through an approved channel, delegate issuance, limit TAP lifetime/use, register a stronger factor and verify/audit recovery.
11. Methods have different phishing resistance; availability, registration, policy requirement and actual sign-in method differ.
12. Investigate and combine account/session/credential/device/consent actions as evidenced; cached tokens and unsupported resources can outlive revocation.
13. Preserve tested emergency access, use a representative pilot/report-only, inspect logs and positive/negative cases, then enforce with rollback.
14. Use identity/client/resource/audiences, assignments and conditions, policy result, device state, method, grant/session details and correlation/time.
15. Frequency governs reauthentication; CAE reacts for supported resources; authentication context requests step-up; protected actions bind that context to supported permissions.
16. The app can provide a limited session based on context without establishing device compliance; verify client/resource support.
17. Sign-in risk concerns a request, user risk an identity, workload risk a service principal; remediation and supported controls differ.
18. Map each traffic profile to supported client/branch acquisition, connectors, DNS/routes and policy; branch acquisition does not imply per-user CA.
19. Use a user-assigned identity when shared hosting or independent lifetime is required, while testing permissions and explicit identity selection.
20. Azure manages credentials; excessive destination roles, app permissions and compromised host code still create risk.
21. An application object defines the app in its home tenant; each service principal represents a tenant-local instance. Managed identities have only the latter.
22. Delegated scopes constrain acting for a user; app permissions authorize the workload; app roles express API/app roles; Azure RBAC governs Azure operations.
23. Add the new credential, verify deployment/use, retire the old credential and monitor failures, with owner/dependency/rollback evidence.
24. Consent authorizes permissions; assignment limits eligible users where supported. Neither supplies the other or removes backend authorization requirements.
25. Choose App Proxy for supported web publishing/preauthentication; compare protocol, client, connector, DNS/certificates and segmentation needs with Private Access.
26. Scope owners, protocol/claims, assignments/roles, consent, CA and provisioning; prove expiry/removal in the target application.
27. Discovery observes use; connectors ingest/apply supported API actions; catalog supplies characteristics; OAuth policies govern apps; access controls entry and sessions control activity.
28. Catalog contains resources/packages; a package bundles resource roles; policies govern request/lifecycle; connected organizations define external relationships; ToU records acceptance.
29. An incorrect department/employee-type/source attribute can match many unintended users; validate input, negative tests and resulting access.
30. It may be unapplied, indirect, dynamic, synchronized, group-assigned or disconnected; inspect source ownership/errors and actual access.
31. Each PIM plane has its own scope/settings. Trace group membership to all downstream roles and distinguish activation from provisioning.
32. Emergency roles must survive PIM/CA dependency failure; permanent active access still needs independent phishing-resistant credentials, monitoring and regular tests.
33. Use provisioning, sign-in, PIM/audit, and the destination Azure/workload resource logs with correlated IDs and timestamps.
34. Use Log Analytics for KQL/alerts, storage for governed longer retention, and Event Hubs for a streaming consumer; set retention and access deliberately.
35. Correlate credential audit event, service-principal ID, token request and destination operation; include time/ingestion bounds, duplicates and legitimate deployment context.
36. Scores measure recommendation alignment, not all threats, excess privilege, unobserved assets or verified containment.

### Additional reasoning checks

37. **Can a tenant-wide role reset every user in a restricted AU?** No; explicit applicable restricted-AU scope is required, though privileged administrators can manage that scope.
38. **Does a resource exclusion always exempt the initiating client?** No; inspect requested scopes, target resource and CA audiences.
39. **Do confidential clients requesting only OIDC scopes change under this update?** The dedicated guidance says no; distinguish them from public clients and directory-scope requests.
40. **Can user risk and sign-in risk be combined casually into one policy?** No; Microsoft's guidance calls for separate policies.
41. **Does Require risk remediation always change a password?** No; passwordless/session/device remediation depends on the detected threat, and guests are unsupported.
42. **Does a group-targeted CA policy cover its service-principal members?** No; supported workload principals must be targeted directly. Managed identities are excluded.
43. **Do 12 denied relationships in the example prove 12 removals?** No; after the five direct removals succeed, seven still require action.
44. **Does a disconnected review marked Applied prove access disappeared?** No; verify the external-system change before recording success.
45. **Do eight PIM activations in ten seconds all get the expedited path?** No; the documented per-app threshold permits the first five, with three falling back to the normal cycle.
46. **Can a Free-to-P1 upgrade retrieve expired sign-in logs?** No; absent earlier export, the missing 23 days in the example stay unavailable.
47. **Does requesting a fresh managed-identity token instantly apply every permission change?** No; backend caching and resource authorization must be verified.
48. **Does Created in Purview mean the migrated file policy enforces?** No; it starts in test mode and still needs deployment, parity and enforcement validation.


## Study plan and readiness rubric

### Four-week practical plan

| Week | Focus | Evidence to produce |
|---|---|---|
| 1 | Tenant roles/AUs, workforce/external/hybrid identity | Identity lifecycle, delegation matrix, external trust diagram, hybrid decision record; Labs 1–3 |
| 2 | Authentication methods, recovery, Conditional Access, risk, GSA | Method/recovery design, four sign-in traces, risk playbook, traffic-profile map; Labs 4–5 |
| 3 | Workload identities, apps, consent, App Proxy, MDCA | Object/token diagram, secretless workload, SaaS lifecycle and session-control evidence; Labs 6–7 |
| 4 | Entitlement, reviews, PIM, logs/KQL/workbooks/score | Request-to-removal evidence, privileged audit timeline, KQL/workbook; Lab 8, scenarios, all checks, Practice Assessment |

### Ready-to-schedule standard

You are close to ready when you can:

- map every published subobjective to a decision and an evidence source without relying on portal memorization;
- distinguish directory role, Azure role, app role, API permission, group membership, ownership, consent, and policy effect;
- troubleshoot a sign-in and provisioning failure from logs without randomly changing controls;
- design joiner/mover/leaver, external access, strong-auth recovery, workload identity, and privileged access lifecycles;
- explain Connect/Cloud Sync, PHS/PTA/federation, app object/service principal, and access/session policy tradeoffs;
- complete the labs safely or produce credible table-top evidence where licensing prevents deployment;
- score consistently on the official Practice Assessment while explaining every incorrect option from current documentation.

## Places to learn

This is a curated list, not a complete list. Do **not** try to consume every resource. Pick the format that works for you, use the official blueprint and documentation to resolve disagreements, and spend substantial time practicing. Commercial durations and catalogs can change; estimates below are planning aids, not promises.

### Two blog readings with practical tasks

| Reading | Learning task | Limits |
|---|---|---|
| [Improved enforcement for policies with resource exclusions](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/upcoming-conditional-access-change-improved-enforcement-for-policies-with-resour/4488925), Swaroop Krishnamurthy, January 28, 2026, with updated June 15 rollout note | Budget 25–40 minutes to draw client → scopes → resource/audience → policy and work the four-case matrix. | Main article reviewed. Dedicated current docs supply the confidential-client/OIDC exception and configuration behavior; the announcement alone does not establish tenant rollout. Comments and linked demos are not implementation authority. |
| [What's new in Microsoft Entra: September 2026](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/what%E2%80%99s-new-in-microsoft-entra-september-2026/4545179), Yina Arenas, September 1, 2026 | Budget 25–40 minutes to build a catalog review across connected and disconnected permissions, with a separate owner/evidence step for external removal. | Main article reviewed. GA announcement does not mean all resources/remediation paths are automatic; current catalog/custom-resource instructions supply scope, licensing and upload/apply limits. |

Four Learn paths list **18 modules**. Earlier path times below total **15h11** but are historical, since the current pages did not expose durations. Public catalog/module outlines, the lab repository README and one Readiness Zone landing page were inspected; paid lessons/questions, full lab instructions and videos were not reviewed. Three O'Reilly/Udemy item pages blocked retrieval; Whizlabs/partner/video responses were shells. Use the blueprint and product documentation to reconcile coverage.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official SC-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) and [credential page](https://learn.microsoft.com/en-us/credentials/certifications/identity-and-access-administrator/) | Public | 1–2 hours initially; 15 minutes on each recheck |
| [Implement an identity management solution](https://learn.microsoft.com/en-us/training/paths/implement-identity-management-solution/) | Public | Historical 4h16; current runtime unverified |
| [Implement an authentication and access management solution](https://learn.microsoft.com/en-us/training/paths/implement-authentication-access-management-solution/) | Public | Historical 4h58; current runtime unverified |
| [Implement access management for apps](https://learn.microsoft.com/en-us/training/paths/implement-access-management-for-apps/) | Public | Historical 2h34; current runtime unverified |
| [Plan and implement an identity governance strategy](https://learn.microsoft.com/en-us/training/paths/plan-implement-identity-governance-strategy/) | Public | Historical 3h23; current runtime unverified |
| [SC-300T00 instructor-led course](https://learn.microsoft.com/en-us/training/courses/sc-300t00) | Paid/partner delivery | 4 days listed |
| [MicrosoftLearning SC-300 labs](https://github.com/MicrosoftLearning/SC-300-Identity-and-Access-Administrator) | Public (MIT) | 12–24 hours selectively; tenant/license setup extra |
| [Official Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/identity-and-access-administrator/practice/assessment?assessment-type=practice&assessmentId=60) and exam sandbox from the credential page | Public | 1–2 hours per assessment/review cycle |
| [Exam Readiness Zone: workload identities (part 3)](https://learn.microsoft.com/en-us/shows/exam-readiness-zone/preparing-for-sc-300-plan-and-implement-workload-identities) and linked series | Public | Historical estimate: about two hours/four parts, February 2024; part 3 landing page only, videos unreviewed; reconcile April objectives |
| [Pluralsight SC-300 path](https://www.pluralsight.com/paths/microsoft-certified-identity-and-access-administrator-associate-sc-300) | Paid/trial | 10h20 across four public listings, Nov 2025–Apr 2026 (path rounds to ten hours); in-production notice remains. Paid lessons/practice and full current coverage unverified |
| [O'Reilly/Packt SC-300 Exam Guide, Second Edition](https://www.oreilly.com/library/view/microsoft-identity-and/9781836200390/) | Paid | Historical 13h03 / 594 pages, March 2025; page blocked. Current edition/content unverified |
| [O'Reilly SC-300 crash course with Razi Rais](https://www.oreilly.com/live-events/exam-sc-300-microsoft-identity-and-access-administrator-crash-course/0636920056976/0636920056975/) | Paid | Public agenda totals three hours; older Azure AD terminology. Event availability and paid session unverified |
| [Microsoft Press Exam Ref SC-300](https://www.oreilly.com/library/view/exam-ref-sc-300/9780137886661/) | Paid | Historical 9h52 / 384 pages, December 2022; page blocked. Current edition/content unverified; supplement later additions |
| [Udemy SC-300 course by John Christopher](https://www.udemy.com/course/sc-300-course-microsoft-identity-and-access-administrator/) | Paid | Historical 16h31, August 2026 update; page blocked. Current runtime/content/coverage unverified |
| [MeasureUp SC-300 practice test](https://www.measureup.com/microsoft-practice-test-sc-300-microsoft-identity-and-access-administrator.html) | Paid | Public listing: 158 questions (35/50/32/41), February 2026 update. Paid questions unreviewed; 3–6 hours is a planning estimate |
| [Whizlabs SC-300 training and practice test](https://www.whizlabs.com/microsoft-identity-and-access-administrator-sc-300/) | Paid/trial | Plan 8–15 hours; exact current duration/question count was not exposed publicly, so verify before purchase |
| [John Savill SC-300 Study Cram](https://www.youtube.com/watch?v=LGpgqRVG65g) | Public | Historical three hours, March 2022; shell-only retrieval. Video content unreviewed; supplement GSA and April 2026 changes |
| [John Savill's public whiteboards and certification materials](https://github.com/johnthebrit/CertificationMaterials) | Public | 1–3 hours selectively; use the video description/repository to find the applicable whiteboard and check its date |
| [Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner-restricted | Varies by scheduled offering; partner sign-in is required to confirm current SC-300 catalog and exact session length |

Avoid any provider claiming actual/live/leaked exam questions. Use legitimate practice assessments to diagnose weak objectives, then return to product documentation and labs.
