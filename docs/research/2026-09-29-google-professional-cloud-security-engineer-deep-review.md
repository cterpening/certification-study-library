# Professional Cloud Security Engineer deep review — September 29, 2026

## Scope and source evidence

The full existing guide and actual **four-page exam PDF** were reviewed. Layout extraction and byte/hash receipts support **70 considerations under 14 numbered objectives**, grouped 26/14/13/12/5 with weights 25/22/23/19/11. The monitored objective digest remains `356877767ac663f5102c9f398ba61909d074668c92d54e0e09584341f5a48166`.

The lifecycle baseline was previously missing. After explicit canonical-page review it was initialized as `144d4a0e903ac71ec0ae4dccba849ebf68ade9b1f515b397ecf0bfc86ba19945`; the next observation is unchanged. Before/accepted/post observations are retained. This is initialization, not a changed blueprint. No printed PDF date or future effective date is invented.

The canonical page lists two hours, USD 200, 50–60 questions, English/Japanese and no formal prerequisite. Its monitored excerpt has no validity line. The separately read [official Certification Help page](https://support.google.com/cloud-certification/answer/9750149?hl=en) supplies the professional two-year validity statement. The guide no longer treats an absent monitor field as absent credential terms and does not borrow PCA/PDE renewal options.

## Changes to teaching

The review adds effective inherited allow/deny evaluation, immutable federation claims, eventually consistent revocation and the distinction between deleting a service-account key and containing tokens already issued from it. PAM entitlement versus grant, optional approvals and current preview/tier limits gain explicit boundaries.

[Secret Manager scheduling](https://docs.cloud.google.com/secret-manager/docs/secret-rotation) triggers a notification; it does not complete source-credential replacement and application rollout. Envelope encryption, key-version selection, DEK rewrapping and payload re-encryption are separated, with direct-KMS and service-specific CMEK behavior kept distinct.

Network teaching now tests preview versus enforcement, header/body phases, configured inspection/parser limits and request-log enablement. Audit coverage distinguishes service defaults, metadata reads, public-access gaps, reader roles and routing failures. Cloud Run deployment controls include activation/organization-policy requirements and the [persistent breakglass annotation warning](https://docs.cloud.google.com/binary-authorization/docs/run/using-breakglass-cloud-run). Provider Access Approval enrollment, exclusions, outage behavior and response ownership remain separate from workload authorization and PAM.

Previously read same-session primary sources support GKE workload versus node identity, PSC direction, VPC-SC dry-run, log routing and AI retrieval/tool/retention boundaries. Current fetches are healthy. The April 22, 2026 app/platform announcement supplies naming context only; no blanket AI-security guarantee or exam-transition date is inferred.

## Executed local evidence

The exact public JavaScript program passed **35 checks** in Node.js **24.18.1**, using built-in cryptography without installing dependencies. The receipt records its SHA-256, runtime version and output. It performs real AES-256-GCM encryption/decryption with process-local random keys, 12-byte nonces and 16-byte tags. Cases include round trips, structural constraints, wrong-key rejection, altered nonce/ciphertext/tag, context and key-ID binding, mismatched payload/wrapper, DEK rewrapping, old-key availability and replay/version behavior.

The program returns plaintext only after authentication succeeds. Rewrapping leaves payload bytes and the data key unchanged. It can rewrap a valid key wrapper for a damaged payload; later decryption correctly rejects that payload. A valid old envelope still decrypts on replay unless a trusted expected version changes.

The local key map is an availability model, not KMS/HSM custody or secure erasure; old key bytes remain for the recovery demonstration. AAD metadata is visible and expected context must come from trusted application authorization. No cloud IAM, key service, persistent rotation, nonce inventory, memory erasure, concurrency, deployment, network or provider access was tested. This is an educational exercise, not an independently audited production cryptographic design.

There are **48 answered checks**, three integrated scenarios and **eight proposed cloud labs** with positive/negative tests, recovery and cleanup criteria. Prior ACE evidence that `gcloud` was absent from PATH is reused. No installation, authentication, real credential, external notification or runtime/service change was attempted. Independent human review remains pending.

## Catalog comparison and validation

Google Skills confirms 21 activities without exposing the earlier 82h30m duration. The fresh direct [Pluralsight path](https://www.pluralsight.com/paths/google-cloud-professional-security-engineer) lists six courses totaling 6h56m and two 30-minute labs, or 7h56m versus the rounded eight-hour header. Course dates range from November 2025 to July 2026; labs are dated September 21 (API controls) and September 11 (DLP/CMEK), 2026. Older search results still showed one lab/seven hours; the direct catalog governs. Public metadata does not prove paid-lesson depth.

O'Reilly returned 403 and Whizlabs exposed only a title. Historical book metadata and suggested study budgets are qualified. No paid interiors, provider labs, proprietary questions or recalled exam items were accessed. Places to learn is last.

The operational receipt records exact local execution and, once completed, repository validation, unit tests, catalog consistency, strict site build, generated-site validation and diff checks. Source freshness is current; the program outcome remains **reviewed with blockers** for live-cloud execution and independent human review.
