# Professional Agentic Architect deep review — September 29, 2026

The actual four-page blueprint was fully read: **31 considerations under 11 numbered objectives**, plus **28 separately mapped tool-list entries**. Domain consideration counts are 4/5/9/7/6 and published weights remain 13/17/33/22/15. No visible publication date was inferred.

The capability monitor changed only because Google added a sentence directing readers to the FAQ. Its capability list and two-part assessment description were otherwise unchanged. The review retains the before/observed text and unified diff, explicitly accepts that editorial change, initializes the missing lifecycle baseline, and records a subsequent unchanged check. The byte-identical earlier snapshot and original September 2 and September 6 source reviews are preserved; three historical audits retain their hashes, dates and conclusions, with snapshot paths redirected to the archive.

## Assessment and source changes

The current beta is open through September 30, with three hours, approximately 80 English multiple-choice questions, a USD 120 fee before tax and one-year validity. The FAQ expects multiple-choice results in late October. Only passing candidates receive separate assessment labs, estimated under five hours, with two months to complete them once available. Public preparation is optional and is not that assessment. Both components must pass.

The canonical page’s general result estimate after both windows close has a different scope from the FAQ’s multiple-choice timeline. Projected mid-November GA and its format remain subject to verification. The monitor’s empty announcement extraction does not eliminate the need to watch the dated FAQ.

The September 3 Workflow Builder entry confirms the current name and GA status while the blueprint says Agent Designer. It does not establish identical low-code interfaces or make every named service GA. Current ADK, protocol and cloud identity documentation were read selectively, with per-source boundaries in the operational evidence.

## Teaching improvements

The guide distinguishes model-proposed arguments from trusted host identity and policy. Approval binds the exact proposed effect, expiry and resource version; current access and resource state must still be checked when a paused action resumes. ADK’s Experimental confirmation feature currently excludes DatabaseSessionService and VertexAiSessionService, so a sample dialog cannot prove a durable deployment contract.

State now has explicit session/user/app/invocation scope and tracked update behavior. Parallel branches require version-pinned ownership, synchronization and merge rules. A2A context continuity differs from task identity; terminal tasks require a new task for refinements, with explicit artifact lineage.

MCP version/SDK/transport compatibility is separated from receiving-resource token validation and delegated authorization. Agent identity follows resource identity rather than a display name; deletion leaves old IAM bindings and replacement needs new grants. PAB eligibility is a union across applicable policies for supported enforcement permissions, and still does not grant access.

Evaluation separates exact, ordered and unordered trajectory matching from independent forbidden-action checks. Word overlap, semantic judges and action correctness measure different properties. A trace with required calls can still contain an unsafe extra action.

## Executed local evidence

The exact public standard-library Python program passed **31 checks: 26 transaction/validation assertions and five trace comparisons**. It uses actual in-memory SQLite transactions for synthetic capacity, approvals and idempotency records. The first authorized operation changes tenant A capacity 100 → 80; duplicate replay has no new effect. Current-access revocation blocks replay. Mismatched arguments/actor/tenant, expiry, stale resource version and excess capacity fail without changing state.

An injected interruption after capacity and approval updates but before ledger insertion rolls back all changes. Retrying commits once. A second fresh approval consumes the remaining 80, leaving tenant B at 200, two ledger entries and two used approvals. A separate trace fixture preserves required call order while adding a forbidden export, demonstrating why the order metric alone is insufficient.

The trusted actor/tenant tuple and administrative approval function are harness assumptions, not authenticated services. State is process-local, on one connection, and closed after execution. No concurrency, process-crash durability, remote side effect, distributed transaction, ADK/MCP/A2A implementation, OAuth, cloud resource or real approval/payment was tested. Exact code hash, runtime and output are recorded.

There are **52 answered checks**, three integrated scenarios and **eight proposed framework/cloud labs**, each with deliberate failures, evidence and cleanup. Cloud/framework execution and independent human review remain blockers.

## Learning resources and validation

Google Skills currently exposes 13 activities and a relative 27-day update, with no activity durations to reconfirm the older 44h estimate. It expressly says coverage is incomplete and retains stale early-September availability language. A Whizlabs exam-specific listing now exists, but direct retrieval exposes only a 48-character title; duration, content and blueprint fit remain unverified. This supersedes the earlier blanket absence statement without asserting course quality.

ADK and protocol reading budgets and proposed lab hours are editorial estimates. No paid interiors, proprietary assessment labs, recalled beta questions or customer data were accessed. Places to learn is last. The operational receipt records exact local execution and, once completed, repository/unit/catalog/strict-site/generated-site/diff validation. Source freshness is current; the program outcome remains **reviewed with blockers**.
