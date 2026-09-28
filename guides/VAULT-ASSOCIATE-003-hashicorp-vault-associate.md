---
exam_code: VAULT-ASSOCIATE-003
vendor_id: hashicorp
official_blueprint: https://developer.hashicorp.com/vault/tutorials/associate-cert-003/associate-review-003
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# HashiCorp Certified: Vault Associate (003) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were reviewed on September 28, 2026 across all 40 detailed objectives; this is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#vault-associate-003-coverage-record). The [official Vault Associate (003) content list](https://developer.hashicorp.com/vault/tutorials/associate-cert-003/associate-review-003) is authoritative.

**Current baseline:** Vault Associate (003), 40 detailed objectives; reviewed September 28, 2026. **VERIFY CURRENT — version discrepancy:** the [certification page](https://developer.hashicorp.com/certifications/security-automation) says **Vault 1.19**, while the learning path still says **1.16**<br>
**Upcoming blueprint change:** No future update or retirement announcement was found in the official certification material as of September 28, 2026.<br>
**Official source:** [Vault Associate (003) exam content list](https://developer.hashicorp.com/vault/tutorials/associate-cert-003/associate-review-003)

HashiCorp presents the credential as **Vault Associate (003)** rather than a short exam code. This library uses `VAULT-ASSOCIATE-003` as a stable catalog identifier.

## How to use this guide

The credential covers the control flow that turns an external identity into a narrowly authorized, time-bounded interaction with a secret or cryptographic service. Build that flow before memorizing commands:

```text
human or workload
       ↓ proves identity through an auth method
identity entity + groups + aliases
       ↓ policies are attached
token with capabilities and TTL
       ↓ authorizes a path operation
secrets engine or system endpoint
       ↓ may return secret + lease
renew, revoke, rotate, audit, or expire
```

Choose a route:

- **New to Vault:** Follow all nine domains in order and complete Labs 1–5.
- **Experienced user:** Use the official content list as an objective checklist and focus on token lineage, lease behavior, response wrapping, storage/seal boundaries, replication, Agent, and Vault Secrets Operator.
- **Application developer:** Concentrate on auth methods, policy paths/capabilities, tokens, leases, KV/database/transit, response wrapping, and workload delivery.
- **Operator:** Concentrate on seal/unseal, storage, HCP versus self-managed responsibilities, replication, and client integration; then continue to the Vault Operations Advanced guide.

HashiCorp's [official learning path](https://developer.hashicorp.com/vault/tutorials/associate-cert-003/associate-study-003) still specifies 1.16 and links versioned 1.16 material, while the credential overview specifies 1.19. Use the current published objectives, check version-specific behavior and confirm the tested version before scheduling. The [deep-review report](../docs/research/2026-09-28-vault-associate-003-deep-review.md) preserves this unresolved discrepancy; the library will recheck October 5. Current Vault 2.x releases are separate from either stated exam baseline.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

HashiCorp publishes nine domains and detailed subobjectives without percentage weights.

| Published domain | Weight | Guide coverage |
|---|---:|---|
| 1. Authentication methods | Not published | Human/workload auth, entities/groups, aliases, and UI/CLI/API workflows |
| 2. Vault policies | Not published | Path matching, capabilities, policy composition, and requirement-driven choice |
| 3. Vault tokens | Not published | Service/batch/root tokens, accessors, TTL, parents, orphans, and creation |
| 4. Vault leases | Not published | Lease IDs, renewal, revocation, expiration, and dynamic-secret lifecycle |
| 5. Secrets engines | Not published | Static/dynamic secrets, KV, database, transit, response wrapping, enable/access workflows |
| 6. Encryption as a Service | Not published | Transit encrypt/decrypt, key rotation, and application responsibility |
| 7. Vault architecture fundamentals | Not published | Encryption barrier, seal/unseal, recovery and key boundaries |
| 8. Vault deployment architecture | Not published | HCP/self-managed clusters, storage, Shamir, replication, and responsibility boundaries |
| 9. Access management architecture | Not published | Vault Agent and Vault Secrets Operator delivery patterns |

## 1. Authentication methods

### Authentication creates a Vault identity context

Vault does not treat an external username, Kubernetes service account, cloud role, or OIDC subject as permission by itself. An auth method validates external evidence and returns a token carrying policies and metadata. The [authentication concepts](https://developer.hashicorp.com/vault/docs/concepts/auth) distinguish the mechanism used to prove identity from the authorization expressed in policies.

Choose an auth method by workload and trust source:

| Scenario | Likely method | Trust question |
|---|---|---|
| Employee interactive sign-in | OIDC, LDAP, or another human directory integration | Which identity provider, groups, MFA, and session claims are authoritative? |
| Application with stable bootstrap credential | AppRole | How are role ID and secret ID delivered, constrained, and rotated? |
| Kubernetes workload | Kubernetes auth | Which cluster, service account, namespace, issuer, and audience can assert identity? |
| Cloud workload | AWS, Azure, or GCP auth | Which signed platform identity and role bindings are accepted? |
| Existing trusted Vault token | Token auth | How was the parent token issued and which policies/TTL limits apply? |

Human-oriented and machine-oriented are usage patterns, not hard product categories. Prefer workload identity over repurposing a human credential for automation.

### Entities, groups, and aliases

Vault's [identity system](https://developer.hashicorp.com/vault/docs/concepts/identity) represents a logical actor as an entity. Aliases connect identities from mounted auth methods to that entity; groups collect entities and can carry policies. This allows one person authenticating through different mechanisms to map to a common identity context when configured correctly.

Keep these objects separate:

- **Auth mount:** one configured instance of an auth method at a path.
- **Alias:** an auth-provider-specific identity attached to an entity.
- **Entity:** Vault's logical representation of a person or workload.
- **Group:** collection of entities or external-group mappings used for policy assignment.
- **Token:** time-bounded credential produced by successful authentication.

A frequent error is attaching policies directly in multiple places without understanding the effective union. Trace policies from the auth role, entity, groups, and token creation path.

### UI, CLI, and API are interfaces to the same API

The UI and CLI ultimately invoke Vault APIs. Learn all three at an associate level:

```bash
# CLI: enable and inspect an auth method in a disposable dev server
vault auth enable -path=study userpass
vault auth list -detailed

# API shape: method and path matter
curl --header "X-Vault-Token: $VAULT_TOKEN" \
  --request POST \
  --data '{"password":"replace-in-lab"}' \
  "$VAULT_ADDR/v1/auth/study/users/learner"
```

Never place real tokens or passwords in shell history. The example is for a disposable local dev environment.

> **Related item:** Mount paths are part of the API namespace. Enabling the same auth type at `auth/team-a` and `auth/team-b` creates distinct mounts with distinct accessors and configuration.

## 2. Vault policies

Vault policies are deny-by-default authorization rules evaluated against request paths and operations. Vault first chooses the applicable policy path using its specificity/priority rules. Identical patterns across policies combine capabilities; different matching patterns do not simply union. A deny in the applicable result takes precedence. Review the [policy concepts and syntax](https://developer.hashicorp.com/vault/docs/concepts/policies).

### Paths and capabilities

A policy stanza targets an API path pattern and grants capabilities such as `create`, `read`, `update`, `delete`, `list`, `patch`, `sudo`, or `deny` where meaningful to that endpoint.

```hcl
path "secret/data/apps/payments/*" {
  capabilities = ["read"]
}

path "secret/metadata/apps/payments/*" {
  capabilities = ["list"]
}

path "secret/data/apps/payments/admin" {
  capabilities = ["deny"]
}
```

Do not infer an HTTP verb mechanically from a capability name. The API endpoint defines which operations and capabilities apply. For KV v2, data and metadata use different API paths; UI-friendly logical paths can hide that distinction.

`*` is a trailing prefix glob, not a regular expression; `+` matches a single path segment. When rules overlap, inspect the documented priority order and test the exact request. The exact admin deny above overrides the broader read rule for that endpoint. A list response is not filtered by the caller's permission on each listed key: avoid sensitive data in names and do not equate discovery with read access.

`*` and `+` have different matching semantics. Build the narrowest pattern that represents the requirement, then test allowed and denied operations. Avoid broad administrative prefixes merely to make a UI page render.

### Policy design method

1. Identify the actor and authentication path.
2. Enumerate exact required API operations.
3. Translate them to paths and capabilities.
4. Separate read, write, list, and administrative duties.
5. Add an explicit deny for a real exception only when needed.
6. test positive and negative cases with a nonroot token.

The built-in `default` policy is normally attached unless disabled; the `root` policy is unrestricted. Do not use root tokens for ordinary application or administration workflows.

## 3. Vault tokens

Tokens are Vault credentials that carry policies, metadata, TTL information, and lineage. The [token concepts](https://developer.hashicorp.com/vault/docs/concepts/tokens) describe service and batch token behavior.

| Token type | Use | Important boundary |
|---|---|---|
| Service token | Full-featured token lifecycle, parent/child relationships, accessors, renewal where allowed | Stored and tracked by Vault; can create children |
| Batch token | Lightweight, encrypted token suited to high-scale short-lived use | Limited features; not persisted like service tokens and cannot be renewed |
| Root token | Unrestricted emergency/bootstrap authority | Minimize creation and lifetime; revoke after use |

Root describes unrestricted policy authority, not a third peer lifecycle type alongside service and batch; the token reference says batch tokens cannot be root tokens. Test policies with a nonroot token or the root bypass can hide errors.

### Parents, children, and orphans

Service tokens normally form a tree. Revoking a parent revokes its nonorphan descendants. An orphan token has no parent, so its lifecycle is independent of the creating token. Use orphaning deliberately for long-running systems whose issuer should not remain a dependency; constrain its policies and TTL.

### TTL, renewal, and periodic behavior

The effective TTL can be limited by the token request, auth role, mount tune values, system defaults, and explicit maximums. Renewable means a client may request more time; it does not mean renewal is automatic or unlimited. Periodic tokens can renew repeatedly by their period while the issuing role/configuration remains valid, but an explicit maximum TTL still caps their total lifetime. Missing the renewal window still expires the token.

Applications should treat expiration as normal: renew when appropriate, reauthenticate when renewal is unavailable, and stop using revoked credentials cleanly.

### Accessors

A token accessor is an identifier that supports lookup or revocation without revealing the token value. Protect it because it still enables administrative actions, but distinguish it from the bearer credential that authenticates requests.

> **Related item:** A token TTL and a secret lease TTL can differ. Revoking the token can revoke child leases; renewing the token does not automatically mean every issued secret has the same lifetime.

## 4. Vault leases

Vault attaches a lease to many dynamic secrets and some auth results. A lease ID identifies the issued object so it can be renewed or revoked. The [lease concepts](https://developer.hashicorp.com/vault/docs/concepts/lease) connect TTL, renewal, and revocation.

```text
request dynamic credential
        ↓
Vault creates external account/key
        ↓ returns value + lease_id + lease_duration + renewable
client uses credential
        ↓
renew before expiry OR reauthenticate/reissue
        ↓
revoke/expire → Vault removes or disables external credential
```

Renewal extends a lease within backend and role limits. Revocation asks Vault to invalidate the leased secret; prefix revocation affects a group of leases and requires careful scope. Lease expiration reduces exposure only if the secrets engine can successfully revoke the remote credential and the application handles expiry.

Operational failure modes include a client that never renews, a revocation queue that cannot reach the target system, an overly long max TTL, or a static secret mistaken for a leased dynamic one.

## 5. Secrets engines

Secrets engines are mounted components that store, generate, transform, or broker data. The [secrets-engine catalog](https://developer.hashicorp.com/vault/docs/secrets) includes general-purpose and product-specific engines.

### Choose by lifecycle

| Need | Engine/pattern | Main decision |
|---|---|---|
| Store application-owned static values | KV v1/v2 | Versioning, metadata, deletion/recovery, and rotation remain your responsibility |
| Generate database accounts | Database secrets engine | Database connection/config, role statements, TTL, revocation, and root rotation |
| Encrypt/sign without returning the encryption key | Transit | Application sends plaintext/ciphertext; Vault performs cryptographic operation |
| Issue cloud credentials | Cloud-specific engine | Role scope, TTL, credential type, revocation behavior |
| Issue certificates | PKI | CA hierarchy, role constraints, TTL, revocation and distribution |

The [database secrets engine](https://developer.hashicorp.com/vault/docs/secrets/databases) demonstrates dynamic credentials: Vault uses a configured privileged connection to create narrowly scoped, leased database users. Protect and rotate that root connection; ensure revocation statements work.

### Mounts and API paths

Enable an engine at an explicit path and configure it before use:

```bash
vault secrets enable -path=study-kv kv-v2
vault secrets list -detailed
vault kv put study-kv/app username=demo password=not-a-real-secret
vault kv get study-kv/app
```

The `vault kv` command abstracts KV version-specific API paths. When writing policies or raw API calls, know whether the mount is KV v1 or v2.

### KV versioning, deletion and concurrent writes

[KV v2](https://developer.hashicorp.com/vault/docs/secrets/kv) separates soft deletion, irreversible destruction of a version, and deletion of all versions plus metadata. Undelete restores a soft-deleted version; it cannot restore destroyed data. Retention limits can also remove old versions, so version history is not an independent backup.

Use [check-and-set](https://developer.hashicorp.com/vault/docs/commands/kv/put) when a write must depend on an observed version. If the current version is 4 and another writer creates 5, a write expecting 4 must be rejected and reconciled. `cas=0` is create-only for a key with no version history; soft deletion does not make an existing versioned key new. KV rotation remains the application's responsibility, and deleting a stored password does not revoke the external account.

### Response wrapping

[Response wrapping](https://developer.hashicorp.com/vault/docs/concepts/response-wrapping) replaces a sensitive response with a short-lived single-use wrapping token. The intended recipient unwraps it; the delivery system need not see the underlying value. A wrapping token is still a bearer capability: whoever obtains it may race the recipient. Verify its creation path and TTL using wrapping lookup before unwrapping; an unexpected or already-consumed token needs investigation. Lookup does not consume it, and rewrap is distinct from retrieving the contents. A wrapping token is not encryption of an arbitrary local file and does not eliminate the need to authenticate the recipient.

> **Related item:** Response wrapping supports secure introduction—the problem of delivering the first sensitive value to a client. The trust still depends on how the wrapping token reaches the intended recipient and how the recipient verifies the expected wrap metadata.

## 6. Encryption as a Service

The [transit secrets engine](https://developer.hashicorp.com/vault/docs/secrets/transit) performs encryption, decryption, signing, verification, hashing, HMAC, and key-management operations without returning managed encryption keys to the client.

```text
application plaintext
       ↓ authenticated request + policy
transit key operation inside Vault
       ↓
ciphertext carrying a key-version marker
```

Key rotation creates a new version for future encryption. Existing ciphertext can normally still be decrypted with retained older key versions. Rewrap moves ciphertext to the latest version without exposing plaintext to the caller. Setting a minimum decryption version can intentionally make old ciphertext unusable, so treat it as a migration decision.

Transit does not secure plaintext before it reaches Vault or after the application receives decrypted data. The application still owns TLS, memory, logging, access, and data-lifecycle controls.

## 7. Vault architecture fundamentals

Vault encrypts persisted data behind a cryptographic barrier before writing it to storage. When sealed, Vault cannot decrypt that protected data. The [seal concepts](https://developer.hashicorp.com/vault/docs/concepts/seal) explain initialization, unseal mechanisms, and recovery-key differences.

Keep the layers distinct:

| Layer | Purpose |
|---|---|
| Storage backend | Persists encrypted Vault data and coordination metadata |
| Encryption barrier | Protects data before storage |
| Seal mechanism | Protects the key material needed to open the barrier |
| TLS | Protects client/node traffic in transit |
| Auth + policy | Decides who can perform which API operations after unseal |

Shamir seal splits an unseal key into shares with a threshold. Auto unseal delegates barrier-key protection to a supported KMS/HSM/seal service; recovery keys retain selected recovery operations but do not behave exactly like Shamir unseal keys. Recovery shares do not substitute for a permanently lost external seal key. Backup, custody, rotation, quorum, and outage dependencies must be designed.

> **Related item:** Auto unseal improves restart automation but introduces a dependency on the external seal service, its credentials, network path, and key lifecycle. It changes the recovery design rather than removing it.

### Configure the client environment (objective 7c)

Use the [CLI reference](https://developer.hashicorp.com/vault/docs/commands) to distinguish the server address, TLS trust, identity and namespace:

| Variable | Purpose and failure clue |
|---|---|
| `VAULT_ADDR` | API scheme/host/port; a wrong target can produce connection or TLS errors before policy evaluation |
| `VAULT_CACERT` | PEM CA file used to verify the server; fix trust/name problems rather than bypassing verification |
| `VAULT_TOKEN` | Bearer credential for requests; avoid logging or committing its value |
| `VAULT_NAMESPACE` | Request namespace in supported Enterprise/HCP setups; wrong scope can make a valid path inaccessible |

For an intentionally disposable local dev server, set `VAULT_ADDR` to `http://127.0.0.1:8200` in its client shell; production uses verified TLS. Bash uses `export VAULT_ADDR=...`; PowerShell uses `$env:VAULT_ADDR = '...'`. Read `vault status` and confirm the target before writing. `vault login` can cache a token through a token helper; clearing an environment variable does not erase that cache or revoke the token. Revoke disposable tokens and remove only the test environment's cached credentials during cleanup.

## 8. Vault deployment architecture

### Self-managed and HCP Vault

With self-managed Vault, the organization owns deployment, storage, TLS, upgrades, monitoring, backup, recovery, replication, capacity, and underlying infrastructure. HCP Vault Dedicated shifts selected platform operations to HashiCorp while the customer still owns identity integrations, policies, secrets engines, client networking, and application use.

**VERIFY CURRENT:** editions, HCP responsibilities, supported features, service tiers, regions, limits, and UI names change. Use the current service agreement and documentation for architecture decisions.

### Storage and clustering

Vault requires a supported [storage backend](https://developer.hashicorp.com/vault/docs/configuration/storage). Integrated Storage uses the Raft consensus protocol and supports high-availability clustering. Storage choice affects consistency, backups, operational complexity, and failure recovery; it is not interchangeable with seal configuration.

### Replication

Vault Enterprise [replication](https://developer.hashicorp.com/vault/docs/enterprise/replication) has different purposes:

| Mode | Purpose | Important distinction |
|---|---|---|
| Performance replication | Serve geographically distributed or high-scale traffic using replicated data with local operations | Supports active workloads; some data remains cluster-local |
| Disaster Recovery replication | Maintain a warm recovery copy for primary failure | Secondary does not normally serve regular client traffic until promoted |

Replication is not a substitute for tested snapshots, recovery procedures, or application failover. Know what data is replicated, which operations are local, and how promotion changes client routing.

## 9. Access management architecture

### Vault Agent

Vault Agent can authenticate on behalf of a workload, manage token renewal, cache/proxy requests, and render secrets into templates depending on configuration. [Auto-auth](https://developer.hashicorp.com/vault/docs/agent-and-proxy/autoauth) combines a method with one or more sinks. Protect sink files and process boundaries: automating delivery does not make the token nonsensitive.

### Vault Secrets Operator

In its synchronization mode, Vault Secrets Operator copies selected Vault secrets into Kubernetes-native Secret objects for workloads that require that interface. The [VSO documentation](https://developer.hashicorp.com/vault/docs/deploy/kubernetes/vso) describes supported resources and delivery patterns.

**Related item — VERIFY CURRENT:** Current VSO documentation also describes an Enterprise CSI mode that mounts secrets without creating Kubernetes Secret objects. That changes the persistence boundary, but pod/node access, refresh and application reload still need verification. Do not assume all VSO deployments have the same storage path or that this newer feature adds an Associate objective.

Choose deliberately:

| Pattern | Advantage | Exposure tradeoff |
|---|---|---|
| Agent template/file | Application reads rendered file; rotation can update it | Secret exists on pod/node filesystem and needs permissions/lifecycle control |
| Agent proxy/API | Application uses local proxy/API path | Application integration and token/cache boundary remain |
| Secrets Operator sync | Works with Kubernetes Secret-consuming applications | Secret is copied into Kubernetes/etcd and RBAC boundary |
| Direct Vault SDK/API | No intermediary copy required | Application must implement auth, renewal, error handling, and availability behavior |

## Integrated request analysis

For any scenario, trace:

1. **Identity source:** What attests to the actor?
2. **Auth mount and role:** Which Vault configuration validates it?
3. **Entity/group mapping:** How is it represented and grouped?
4. **Policies:** Which exact paths and capabilities result?
5. **Token:** What type, parentage, TTL, renewal, and metadata apply?
6. **Engine/endpoint:** What operation is authorized?
7. **Lease or key version:** What ongoing lifecycle exists?
8. **Delivery boundary:** Where does the returned value travel or persist?
9. **Evidence and failure:** How will denial, expiry, revocation, outage, or misuse be observed?

This turns product vocabulary into a security decision path.

## Worked security decisions and useful reading

These original scenarios are documentation-based reasoning exercises. No Vault server, Kubernetes cluster or HCP service was executed during this review.

1. **Resolve policy matching:** Compare read permission for `secret/data/apps/payments/*` with the exact admin deny above. Explain which stanza applies to an ordinary key, the admin key and a metadata list request. Expected: ordinary data read permitted, admin denied, metadata listing evaluated at its own endpoint. Test with a nonroot token and separately inspect returned names.
2. **Handle a concurrent edit:** Two clients read KV version 4. A writes using CAS 4 and creates version 5. B's CAS 4 write should fail; B must reread and reconcile rather than disable CAS. A soft-deleted version 5 still does not make CAS 0 a safe create operation.
3. **Bound a periodic token:** A token issued at 09:00 has a 20-minute period and explicit maximum lifetime of one hour. Successful renewals before each expiry cannot extend it past 10:00. Reauthenticate before the cap and separately manage each issued secret lease. These times are a synthetic model, not a measured scheduler guarantee.
4. **Rotate transit keys safely:** Ciphertext made with v1 remains tied to v1 after rotating the key to v2. Rewrap the old ciphertext, verify recovery and only then consider raising the minimum decryption version. Raising the floor too early can strand older ciphertext. Key rotation alone does not rewrite application storage.
5. **Separate delivery from consumption:** VSO updates a Kubernetes Secret, but a process with a copied value or environment variable can continue using the old credential. Plan the supported rollout/reload behavior, overlap window and final revocation. A synchronized object alone does not prove that every client has switched.

**Beyond the exam — VERIFY CURRENT:** The September 1, 2026 [Vault agentic IAM announcement](https://www.hashicorp.com/en/blog/hashicorp-vault-agentic-iam-is-now-generally-available), by Claudia Cornali-Motta, Bianca de Azevedo Moreira and Isabela Palanca Aureus, describes Vault Enterprise 2.1 capabilities for agent identity and delegated authorization. Use it for a 20–30-minute worksheet: name the caller, accepted issuer, permitted resource/action and independent enforcement point. It does not establish coverage in Associate (003), nor does a new identity feature make an arbitrary agent action safe.

The [2.x release notes](https://developer.hashicorp.com/vault/docs/updates/release-notes) corroborate GA in 2.1 and state that revoking an OAuth JWT through Vault prevents its use with Vault; an immutable JWT may still be accepted elsewhere. A useful architecture check therefore identifies every verifier's revocation/expiry behavior. No Enterprise feature was configured here.

## Hands-on labs

Use `vault server -dev` or an explicitly disposable personal environment. Dev mode is not secure or persistent and must never be used as a production pattern.

### Lab 1: Trace authentication to policy

Start a dev server, enable `userpass` at a custom path, create a learner policy, user, and password, then authenticate with CLI and API. Inspect token policies, entity/alias data, accessor, TTL, and renewal status. Verify one allowed and two denied paths.

### Lab 2: Compare service, orphan, and batch tokens

Create narrowly scoped examples with short TTLs. Inspect parent relationships and accessors. Revoke a parent and observe child behavior. Explain which features make batch tokens unsuitable for a given scenario. Revoke everything afterward.

### Lab 3: Observe KV and lease differences

Enable KV v2 and store a disposable value. Compare its metadata/version lifecycle with the lease metadata returned by a dynamic or test secrets engine available in your lab. Draw which component owns rotation and revocation in each case.

### Lab 4: Transit key rotation

Enable transit, create a key, encrypt a nonsecret sample, rotate the key, encrypt again, and inspect ciphertext version markers. Decrypt both, then rewrap the older ciphertext. Do not raise minimum decryption versions until you can explain the recovery consequence.

### Lab 5: Seal and storage design tabletop

Design a three-node production cluster using Integrated Storage. Document TLS identities, seal method, key/recovery custody, snapshot schedule, restore test, quorum failure, monitoring, and client retry behavior. Compare self-managed responsibility with HCP Vault Dedicated.

### Lab 6: Choose a workload delivery pattern

For one Kubernetes application, compare direct API, Agent template, Agent proxy, and Secrets Operator sync; separately assess Enterprise CSI if available. Specify identity, policy, token/lease renewal, storage location, rotation behavior, Kubernetes RBAC, logging risk, and failure behavior. Implement only in an authorized disposable cluster.

## Knowledge checks

1. What does an auth method prove, and what does it not authorize by itself? **Answer:** It validates identity evidence and produces a Vault token/context; policy still governs the requested endpoint operation.
2. How do auth mounts, aliases, entities, groups, policies, and tokens relate? **Answer:** An auth mount validates identity; its alias maps to an entity, groups contribute policy context, and the issued token authorizes requests.
3. Why can two mounts of the same auth type produce different identity contexts? **Answer:** Each mount has its own configuration and accessor, so identical usernames need not map to the same entity.
4. How do policy paths differ from UI navigation paths? **Answer:** The UI abstracts API routes; KV v2 data and metadata have distinct policy paths and capabilities.
5. What happens when attached policies grant overlapping capabilities and one explicitly denies a path? **Answer:** Resolve the applicable path by priority, combine identical-pattern capabilities, and apply deny precedence in that result; overlapping patterns are not all unioned.
6. Contrast service, batch, and root tokens. **Answer:** Service tokens support tracked lifecycle/renewal/accessors; batch tokens are lightweight with restrictions. Root is unrestricted policy authority, not an ordinary workload credential.
7. How does token parent revocation affect children and orphans? **Answer:** Normal child tokens and their leases are revoked with the parent; orphan tokens have an independent lineage.
8. Why can a renewable token still expire? **Answer:** Renewal can fail, arrive too late or hit maximum lifetime; an explicit max TTL also caps periodic tokens.
9. What can an accessor do without revealing the bearer token? **Answer:** With proper authority it enables lookup, capability inspection, renewal or revocation; it is not itself a login credential.
10. How do token TTL and secret lease TTL differ? **Answer:** One limits the Vault session, the other the issued secret. Parent revocation and independent renewal rules can couple their lifetimes.
11. What makes a dynamic secret operationally different from a KV value? **Answer:** Dynamic credentials are generated with a lease and revocation mechanism; a KV value remains application-managed and is not externally revoked just because it is deleted from Vault.
12. What problem does response wrapping solve? **Answer:** It gives a short-lived, single-use bearer handle for a response, allowing delivery without revealing its contents to intermediaries; verify origin and protect the handle.
13. What does transit key rotation change for old ciphertext? **Answer:** Rotation creates a new encryption-key version; old ciphertext is not automatically rewritten and depends on retained usable versions.
14. Which plaintext boundaries remain outside transit? **Answer:** Plaintext at the caller, transport endpoints, process memory, logs and downstream consumers still needs protection.
15. Contrast storage, encryption barrier, seal, TLS, and policy. **Answer:** Storage holds encrypted data; barrier protects it; seal protects unlock material; TLS protects traffic; policy controls operations.
16. What dependency does auto unseal introduce? **Answer:** Available and authorized access to the external seal service/key; recovery shares alone cannot replace a permanently lost seal key.
17. How do performance and DR replication differ? **Answer:** Performance replicas serve supported active workloads with cluster-local distinctions; DR replicas need promotion for normal service. Neither replaces backups.
18. Which responsibilities remain with a customer using HCP Vault? **Answer:** Customer identity, policies, secrets configuration, allowed networking, client behavior and applicable data/recovery responsibilities remain.
19. How do Agent templates and Secrets Operator sync change the secret's persistence boundary? **Answer:** Templates create files; synchronization copies into Kubernetes Secrets. Enterprise CSI is a distinct current option, with its own version/entitlement limits.
20. Why should every Vault scenario be traced from external identity through lease/revocation? **Answer:** Authorization, lifetime, data copies and revocation failures cross several components; a successful login alone proves little about end-to-end control.

## High-value distinctions

| Contrast | Remember |
|---|---|
| Authentication vs authorization | Prove identity vs permit path operations |
| Auth method vs auth mount | Plugin type vs one configured instance/path |
| Entity vs alias | Logical Vault identity vs identity at one auth mount |
| Policy vs token | Authorization rules vs credential carrying effective rules |
| Service vs batch token | Full stored lifecycle vs lightweight limited token |
| Parent vs orphan | Revocation lineage vs independent lifecycle |
| Token TTL vs lease TTL | Vault session lifetime vs issued-secret lifetime |
| Static vs dynamic secret | Stored application value vs generated leased credential |
| KV v1 vs KV v2 | Direct value path vs versioned data/metadata APIs |
| Transit vs secret storage | Cryptographic operation vs retrieving stored key/value data |
| Storage vs seal | Persist encrypted data vs protect barrier-unlock material |
| Shamir vs auto unseal | Human-share threshold vs delegated seal service |
| HA vs DR | Local service continuity vs recovery-cluster promotion |
| Performance vs DR replication | Active distributed service vs standby recovery copy |
| Agent vs Secrets Operator | Client-side auth/proxy/template vs Kubernetes Secret synchronization |

## Readiness checklist

- [ ] I can trace an external identity through auth, entity/group, policy, token, engine, and lease.
- [ ] I can choose and configure a human or workload auth method in a disposable environment.
- [ ] I can write narrow policies and explain path matching and capabilities.
- [ ] I can distinguish service, batch, root, child, orphan, periodic, and renewable token behavior.
- [ ] I can explain lease issuance, renewal, revocation, and failure handling.
- [ ] I can choose among KV, database, transit, and other engine patterns by lifecycle.
- [ ] I can explain response wrapping and secure introduction.
- [ ] I can rotate transit keys and explain ciphertext version behavior.
- [ ] I can separate storage, barrier, seal, TLS, authentication, and policy boundaries.
- [ ] I can compare self-managed and HCP Vault responsibilities.
- [ ] I can distinguish HA, snapshots, performance replication, and DR replication.
- [ ] I can choose among direct API, Agent, and Secrets Operator delivery patterns.
- [ ] I completed safe hands-on work and checked the current official blueprint.

## Primary references

- [Official Vault Associate (003) content list](https://developer.hashicorp.com/vault/tutorials/associate-cert-003/associate-review-003)
- [Official Vault Associate learning path](https://developer.hashicorp.com/vault/tutorials/associate-cert-003/associate-study-003)
- [Vault authentication](https://developer.hashicorp.com/vault/docs/concepts/auth)
- [Vault policies](https://developer.hashicorp.com/vault/docs/concepts/policies)
- [Vault tokens](https://developer.hashicorp.com/vault/docs/concepts/tokens)
- [Vault leases](https://developer.hashicorp.com/vault/docs/concepts/lease)
- [Vault seal concepts](https://developer.hashicorp.com/vault/docs/concepts/seal)

## Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Pick the official reading, hands-on path, video, and assessment format that fits your gaps. Times are approximate consumption time at normal speed; labs, pausing, notes, troubleshooting, and review add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [HashiCorp Vault Associate (003) learning path](https://developer.hashicorp.com/vault/tutorials/associate-cert-003/associate-study-003) | Free; some exercises require a local sandbox or account | About 18–30 hours for linked reading and labs (library estimate; the page's nine-minute read time excludes linked work) | Official ordered coverage of nine domains; its 1.16 statement conflicts with the credential page's 1.19 claim, so verify the version before scheduling |
| [Vault Associate (003) content list](https://developer.hashicorp.com/vault/tutorials/associate-cert-003/associate-review-003) | Free | About 3–6 hours for an active pass through objectives and selected docs | Best checklist for targeted remediation; its six-minute page time excludes linked documentation and tutorials |
| [Official sample questions](https://developer.hashicorp.com/vault/tutorials/associate-cert-003/associate-questions-003) | Free | About 30–60 minutes including documentation-backed review | First-party format orientation for true/false, multiple-choice, and multiple-answer items; too small to establish readiness |
| [HashiCorp Vault tutorials](https://developer.hashicorp.com/vault/tutorials) | Free; selected HCP, Kubernetes, or cloud labs require a sandbox | About 1–4 hours per selected gap | Hands-on remediation for auth, policies, secrets engines, transit, deployment, Agent, and Kubernetes integration |
| [HashiCorp Vault documentation](https://developer.hashicorp.com/vault/docs) | Free | About 6–12 hours for a deliberate objective-mapped reference pass | Primary behavior reference; current 2.x docs are newer than both conflicting exam-version statements; select and record the relevant version |

No exact current third-party Vault Associate (003) course or commercial practice exam was added during this review without a verifiable public scope and runtime. That is an open catalog gap. Compare any candidate with the official 003 content list and reject products advertising dumps, “actual questions,” or guaranteed exam content.
