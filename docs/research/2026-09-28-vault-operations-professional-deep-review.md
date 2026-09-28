# Vault Operations Advanced deep review — September 28, 2026

Read the complete guide and all 29 detailed objectives across eight domains. Objective/status monitor snapshots are unchanged. The [credential page](https://developer.hashicorp.com/certifications/security-automation) states Vault 1.16 for Advanced. The [shared rename announcement](https://developer.hashicorp.com/terraform/tutorials/pro-cert/adv-update) supplies fall 2026 and explicitly preserves content/format; the guide's earlier claim that no notice was found is superseded. Keep the legacy internal identifier and accepted objective snapshots. No future scope change or retirement was found on checked official pages.

## Learning improvements

Teach audit delivery to at least one enabled device, independent destinations, request/response correlation, hashing boundaries and evidence preservation. Add health response roles and probe caveats, voting quorum, join/seal dependencies, snapshot recovery limits, Sentinel evaluation order, and method-versus-sink wrapping lifecycle. Preserve the PKCS#11 objective while acknowledging broader supported seal implementations. Add five original incident decisions and answers to all 20 knowledge checks.

The [June 24 HCP cluster DR article](https://www.hashicorp.com/en/blog/hcp-vault-dedicated-introduces-cluster-disaster-recovery-public-preview) supports a bounded managed-service responsibility worksheet. It announces a support-enabled public preview, not a new exam objective or independently measured RTO. Current 2.x release notes are product context beyond the stated 1.16 baseline. Direct blog HTTP access was blocked; web retrieval read the article. Official catalogs were compared; no exact current third-party Advanced course with verified objective mapping/runtime was added.

## Local validation and limits

An isolated, checksum-verified Vault 1.16.3 dev server bound to loopback executed a narrow portion of Lab 3. A synthetic key was denied before policy repair, readable after a narrow grant, inaccessible on an unrelated path and inaccessible after token revocation. Audit request/response pairs and HMAC-protected values were inspected. The synthetic key/policy were deleted, the server stopped and its listener verified closed. The receipt records eight assertions and API-request count without tokens or raw audit data.

This is not production cluster validation. No TLS, persistent Raft, snapshot restore, replication, HSM, Kubernetes, Agent, Sentinel, control group, Enterprise or HCP feature was executed. Other lab instructions remain proposed. Independent human review remains pending. The operational receipt preserves source fetches, prior records, objective mapping and sanitized local evidence.
