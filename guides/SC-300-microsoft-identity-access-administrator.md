---
exam_code: SC-300
vendor_id: microsoft
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-01
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-01
---

# SC-300 Microsoft Identity and Access Administrator Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked on September 1, 2026; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#sc-300-coverage-record). The [official SC-300 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) is authoritative.

**Current baseline:** Skills measured as of April 27, 2026; official study-guide page last updated March 27, 2026.<br>
**Exam state:** Active; the official credential page lists no retirement date.<br>
**Upcoming blueprint change:** None announced on the official study guide as of September 1, 2026.<br>
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

Read Sections 1–4, work the three integrated scenarios, complete or tabletop all eight labs, and answer the 36 original checks. Use a disposable tenant where licensing permits; many governance, risk, application-control, and Global Secure Access tasks require licenses or infrastructure beyond a free tenant. Never weaken a production tenant merely to reproduce a learning exercise.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

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

Custom security attributes are typed, tenant-defined key/value data assigned to supported Entra objects. Their attribute-definition and attribute-assignment roles are deliberately separate, and their values can support filtering or attribute-based access scenarios. They are not the same as directory extensions or dynamic-group attributes. Define an owner, allowed values, sensitivity, deactivation/change procedure, and permitted consumers before using them. Microsoft's [custom-security-attributes overview](https://learn.microsoft.com/en-us/entra/fundamentals/custom-security-attributes-overview) explains the separate definition and assignment control planes.

Bulk operations in the admin center, Microsoft Graph PowerShell, or Graph API need input validation, duplicate handling, throttling/retry, dry-run or pilot scope, structured error capture, and post-change reconciliation. Prefer the Microsoft Graph PowerShell SDK over obsolete AzureAD/MSOnline examples. Never assume that a command succeeded for all records because the script returned without a terminating error.

Device **registration** normally represents a personally owned device associated with a work account; Microsoft Entra **join** makes Entra the primary device identity for an organization-owned device; **hybrid join** combines AD DS domain join with Entra registration. Device identity enables signals and SSO, while Intune compliance expresses management posture. Neither should be mistaken for user authentication or resource authorization.

License assignment can be direct or group-based. Model prerequisite service plans, mutually exclusive products, usage location, delayed processing, and license removal. Report both assigned licenses and provisioning errors. Group-based licensing improves lifecycle automation but does not replace entitlement review or application authorization.

> **Related item:** A stable object ID is safer for automation than a mutable UPN or email address. Human-readable identifiers change during mergers and name/domain changes; design correlation and audit evidence accordingly.

### Implement external and cross-tenant identity deliberately

External collaboration settings control who can invite guests, guest directory visibility, and domain restrictions. Cross-tenant access settings govern inbound and outbound B2B collaboration/direct-connect access with Entra organizations and whether to trust MFA or compliant/hybrid-device claims from a partner tenant. These are different layers. Microsoft’s [cross-tenant access overview](https://learn.microsoft.com/en-us/entra/external-id/cross-tenant-access-overview) explains default, organization-specific, inbound, outbound, and trust settings.

Invite an individual or bulk set of external users only after defining sponsor, purpose, resource, expiry, acceptable-use/terms, and removal conditions. The resource tenant controls authorization; the home tenant normally controls authentication. Do not trust a partner's MFA or device claim merely for convenience—document the assurance agreement, scope it, monitor it, and maintain a fallback if the partner configuration changes.

Cross-tenant synchronization is a push provisioning process from a source tenant into a target tenant. It creates, updates, and deprovisions B2B collaboration objects in scope; configure automatic redemption, attribute mappings, scoping, and target-tenant inbound synchronization trust together. It does not make two tenants one boundary. Microsoft's [cross-tenant synchronization overview](https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-overview) is the current starting point.

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

## 2. Implement authentication and access management

### Build an authentication-method strategy

Start with threat resistance and recovery, not “enable MFA.” Inventory user populations, devices, platforms, accessibility, offline/emergency requirements, privileged roles, contractors, and legacy protocols. Use the Authentication methods policy as the current control plane and phase out duplicated legacy MFA/SSPR settings. Microsoft's [authentication-methods management reference](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods-manage) explains how policies coexist.

Understand the methods and their roles:

- Passkeys/FIDO2 and certificate-based authentication can provide phishing-resistant authentication when correctly configured. Validate attestation/AAGUID or certificate trust, revocation, mapping, and recovery requirements.
- Microsoft Authenticator supports push/number matching and passwordless phone sign-in; configure context and suspicious-activity reporting deliberately.
- A Temporary Access Pass (TAP) is a time-limited bootstrap/recovery credential for registering stronger methods. Scope policy and issuance roles, choose one-time versus reusable behavior, verify the user before issuance, and audit use. See the [TAP configuration guide](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-temporary-access-pass).
- OAuth 2.0 access, ID, and refresh tokens serve different protocol purposes. Revoking a session does not guarantee immediate rejection of every cached access token; resource support, token lifetime, CAE, and application behavior matter.
- SMS, voice, and passwords may be needed for transitional populations but are weaker than phishing-resistant methods. Do not count every MFA combination as equivalent assurance.

Tenant-wide MFA can be achieved through Conditional Access or, for simpler tenants, security defaults; per-user MFA is a legacy control. Keep emergency access protected with phishing-resistant credentials while excluding it from policies that could make it unusable. Registration campaigns can nudge users toward Authenticator or passkeys, and Microsoft-managed defaults can change. **VERIFY CURRENT:** the current [registration-campaign guidance](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-mfa-registration-campaign) describes passkey-targeting rollouts that older courses will not show.

SSPR requires scope, allowed methods, registration, authentication count, writeback for applicable hybrid users, notifications, and help-desk verification/recovery design. Combined MFA/SSPR registration reduces duplicate enrollment but policy requirements still combine. Monitor reset and registration events and test a user who has lost every normal factor.

Windows Hello for Business binds a user gesture to device-protected asymmetric credentials; the PIN is local to the device, not a reusable network password. Choose Entra-only or hybrid deployment and the applicable cloud Kerberos, key, or certificate trust. Microsoft's [Windows Hello authentication flow](https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/how-it-works-authentication) explains PRT and on-premises Kerberos behavior.

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

Session controls include sign-in frequency, persistent browser behavior, application-enforced restrictions, Conditional Access app control, token protection, and customized continuous access evaluation. CAE lets supported resources react to critical events and policy/location changes without waiting for ordinary token expiry; it does not make every application continuously reevaluate. Consult the current [Conditional Access session-control reference](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-session) for support boundaries.

Authentication context lets an application label a sensitive operation/resource so Conditional Access can require step-up controls. Protected actions apply authentication context to supported Entra permissions such as high-impact policy changes. Confirm that the calling tool supports the context and retain a recovery path. Policy templates are accelerators, not organization-specific designs: review assignments, exclusions, controls, licenses, and interactions before enabling.

Device-enforced restrictions depend on the consuming application and device signal. For example, an unmanaged browser may receive a limited SharePoint experience rather than universal device control. Map the policy to the application's supported behavior and test desktop, browser, and mobile clients.

> **Related item:** Conditional Access is a policy engine after first-factor authentication, not a firewall and not an entitlement system. It cannot repair excessive app permissions, stale group membership, or an unauthenticated network path by itself.

### Manage identity risk and registration

Microsoft Entra ID Protection produces risk detections and calculates sign-in risk (likelihood this authentication is not legitimate) and user risk (likelihood the identity is compromised). Workload identity risk covers service principals. Use risk-based Conditional Access for user self-remediation where appropriate, and investigate the underlying detections, sign-in context, device, application, and correlated security evidence.

A risky sign-in may be remediated by strong MFA; user risk may require secure password change or administrator action. “Dismiss risk” is not containment. Confirming safe, confirming compromised, blocking, resetting, revoking, and dismissing have different meanings and audit effects. Microsoft's current [risk-remediation guidance](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock) describes self, system, threat-informed, and administrator remediation.

For risky workload identities, there is no human to perform MFA or a password reset. Investigate owners, credential use, permissions, service-principal sign-ins, source, code/deployment changes, and affected resources. Disable or isolate safely, rotate/remove credentials, prefer managed identity or federated credential, reduce permissions, restore the workload, and verify logs. Do not break a critical service without a tested recovery owner.

Registration policy is part of risk reduction. Scope authentication methods, use registration campaigns, bootstrap securely with TAP, require strong authentication to change security info, protect registration events with Conditional Access, and monitor anomalous additions. An attacker who registers their own factor can retain access after a password reset.

### Implement Global Secure Access as identity-aware networking

Global Secure Access unifies Microsoft Entra Internet Access and Private Access. Traffic profiles acquire Microsoft, private, or internet traffic through supported clients or remote-network paths and apply the service's security and Conditional Access capabilities. The [Global Secure Access overview](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access) is the current product boundary.

- **Private Access** is ZTNA for defined private FQDN/IP resources and ports/protocols. Quick Access covers broad primary destinations; per-app Global Secure Access applications provide finer segmentation. Private network connectors broker access without publishing the resource directly.
- **Internet Access** routes supported internet/SaaS traffic for filtering and threat protection.
- **Internet Access for Microsoft services** (the Microsoft traffic profile) optimizes and secures supported Microsoft traffic and can enforce tenant restrictions.

Plan client deployment, remote networks, connectors, DNS/FQDN/IP segments, overlapping routes, traffic-profile assignment, Conditional Access, logging, high availability, bypasses, coexistence with VPN/SSE tools, and rollback. Validate user traffic with the traffic logs and client diagnostics, not merely a green configuration blade.

**VERIFY CURRENT:** client/platform support, remote-network acquisition, licensing, TLS inspection, traffic categories, and Conditional Access limitations change quickly. Read [known Global Secure Access limitations](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-current-known-limitations) immediately before a design or exam.

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

### Implement privileged access and emergency recovery

PIM provides eligible/time-bound activation, approval, MFA/authentication context, justification/ticket information, notifications, access reviews, and audit for Entra directory roles, Azure resource roles, and group membership/ownership. These are related but separate resource planes. Configure role settings per role/resource based on impact.

An effective privileged model includes separate daily/admin identities, phishing-resistant authentication, privileged workstations, least scope, eligible rather than standing access, approval for critical roles, short activation, monitored actions, and periodic review. Avoid approval by another equally exposed account or a circular dependency where the only approver cannot activate.

PIM for Groups makes membership or ownership eligible. The group can then confer application, Azure, Entra, SQL, Key Vault, Intune, or other access. This is powerful and can hide privilege behind nesting; trace the group to every downstream assignment. Microsoft's [PIM for Groups overview](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/concept-pim-for-groups) distinguishes member and owner activation policies.

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

| Resource | Access | Estimated time |
|---|---|---:|
| [Official SC-300 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) and [credential page](https://learn.microsoft.com/en-us/credentials/certifications/identity-and-access-administrator/) | Public | 1–2 hours initially; 15 minutes on each recheck |
| [Implement an identity management solution](https://learn.microsoft.com/en-us/training/paths/implement-identity-management-solution/) | Public | 4 hours 16 minutes listed |
| [Implement an authentication and access management solution](https://learn.microsoft.com/en-us/training/paths/implement-authentication-access-management-solution/) | Public | 4 hours 58 minutes listed |
| [Implement access management for apps](https://learn.microsoft.com/en-us/training/paths/implement-access-management-for-apps/) | Public | 2 hours 34 minutes listed |
| [Plan and implement an identity governance strategy](https://learn.microsoft.com/en-us/training/paths/plan-implement-identity-governance-strategy/) | Public | 3 hours 23 minutes listed |
| [SC-300T00 instructor-led course](https://learn.microsoft.com/en-us/training/courses/sc-300t00) | Paid/partner delivery | 4 days listed |
| [MicrosoftLearning SC-300 labs](https://github.com/MicrosoftLearning/SC-300-Identity-and-Access-Administrator) | Public (MIT) | 12–24 hours selectively; tenant/license setup extra |
| [Official Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/identity-and-access-administrator/practice/assessment?assessment-type=practice&assessmentId=60) and exam sandbox from the credential page | Public | 1–2 hours per assessment/review cycle |
| [Exam Readiness Zone: workload identities (part 3)](https://learn.microsoft.com/en-us/shows/exam-readiness-zone/preparing-for-sc-300-plan-and-implement-workload-identities) and linked series | Public | About 2 hours for four parts; February 2024, so reconcile with current blueprint |
| [Pluralsight SC-300 path](https://www.pluralsight.com/paths/microsoft-certified-identity-and-access-administrator-associate-sc-300) | Paid/trial | 10 hours listed plus practice exam; four courses dated Nov 2025–Apr 2026 |
| [O'Reilly/Packt SC-300 Exam Guide, Second Edition](https://www.oreilly.com/library/view/microsoft-identity-and/9781836200390/) | Paid | 13 hours 3 minutes / 594 pages listed; March 2025, so supplement 2026 changes |
| [O'Reilly SC-300 crash course with Razi Rais](https://www.oreilly.com/live-events/exam-sc-300-microsoft-identity-and-access-administrator-crash-course/0636920056976/0636920056975/) | Paid | 3 hours listed; older Azure AD terminology and outline, so use as foundation |
| [Microsoft Press Exam Ref SC-300](https://www.oreilly.com/library/view/exam-ref-sc-300/9780137886661/) | Paid | 9 hours 52 minutes / 384 pages listed; December 2022 and materially outdated for current additions |
| [Udemy SC-300 course by John Christopher](https://www.udemy.com/course/sc-300-course-microsoft-identity-and-access-administrator/) | Paid | 16 hours 31 minutes listed; updated August 2026; independently validate coverage/claims |
| [MeasureUp SC-300 practice test](https://www.measureup.com/microsoft-practice-test-sc-300-microsoft-identity-and-access-administrator.html) | Paid | 3–6 hours across practice/certification cycles; last update February 2026 listed |
| [Whizlabs SC-300 training and practice test](https://www.whizlabs.com/microsoft-identity-and-access-administrator-sc-300/) | Paid/trial | Plan 8–15 hours; exact current duration/question count was not exposed publicly, so verify before purchase |
| [John Savill SC-300 Study Cram](https://www.youtube.com/watch?v=LGpgqRVG65g) | Public | 3 hours; published March 2022—strong foundations, but supplement GSA and all April 2026 changes |
| [John Savill's public whiteboards and certification materials](https://github.com/johnthebrit/CertificationMaterials) | Public | 1–3 hours selectively; use the video description/repository to find the applicable whiteboard and check its date |
| [Partner Skilling Hub](https://www.skilling-hub.com/en-US) | Partner-restricted | Varies by scheduled offering; partner sign-in is required to confirm current SC-300 catalog and exact session length |

Avoid any provider claiming actual/live/leaked exam questions. Use legitimate practice assessments to diagnose weak objectives, then return to product documentation and labs.
