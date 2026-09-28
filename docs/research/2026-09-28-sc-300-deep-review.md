# SC-300 deep review — September 28, 2026

The complete [guide](../../guides/SC-300-microsoft-identity-access-administrator.md)
was read and all **98 April objectives in 16 groups** individually mapped. The
accepted snapshot is unchanged. The credential remains active and lists
100 minutes and ten exam languages; instructor-led training lists four days.

## Learning changes

Five worked examples distinguish effective restricted-AU permissions, client
scope versus Conditional Access resource targeting, denied versus removed
access, PIM activation versus application readiness, and retained versus expired
logs. Two additional labs bring the total to **ten**. All 36 existing checks now
have an answer key, and 12 new answered checks bring the total to **48**.
Ten offline synthetic permission, arithmetic, time-window and catalog checks
passed. No tenant, directory, certificate, token request, SCIM, KQL, GSA, policy
deployment or paid service operation was executed.

The guide expands restricted-AU governance/application limitations, immutable
role-assignable groups, directional cross-tenant provisioning, group licensing,
Connect/Health minimums, current PTA hotfix and application-certificate ownership.
It adds CBA factor/binding/revocation prerequisites and Entra Kerberos partial/full
TGT boundaries without treating cloud authentication as on-premises authorization.

Current baseline-scope guidance distinguishes public clients, excluded
confidential clients requesting directory scopes, and confidential OIDC-only
requests. The dedicated page and updated Microsoft blog specify June 15 rollout,
qualifying older March wording in the general targeting page. Tenant settings
and actual sign-in audiences remain necessary evidence. Enabling enforcement
is an effective change, not an observation-only test.

October 1 legacy risk-policy retirement is paired with separate user/sign-in
policies, adaptive user-risk remediation and guest/passwordless boundaries.
Workload CA is scoped to directly targeted supported service principals, with
managed identities excluded. GSA client versus branch acquisition, managed
identity token caching and host boundaries are explicit.

Catalog reviews do not automatically revoke every access path. Custom-resource
uploads, reviewer/stage restrictions and external-system changes are kept
separate from the recorded apply status. The file-policy migration tool creates
limited-workload Purview policies in test mode and keeps originals: creation
alone does not demonstrate deployed, equivalent enforcement. Six dated
follow-ups complement existing shared identity deadlines.

## Open official-source issue

The [official study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300)
still gives authentication/access management **25–30% in its summary** and
**20–25% in the detailed heading**. The guide preserves both and uses the summary
only as a disclosed planning choice. This review is **reviewed with blockers**;
an October 1 checkpoint requests another authoritative check. No corrected
weight or blueprint revision is invented. The original September 1 passed
review remains unchanged as historical evidence.

## Resource and blog decisions

Four direct Learn paths list 18 modules. Earlier runtimes totaling 15h11 are
historical and were not exposed in the current retrieval. Pluralsight's four
public listings total 10h20 and span November 2025–April 2026; an in-production
notice remains. MeasureUp lists 158 questions, with domain counts 35/50/32/41,
and a February 2026 update. Neither establishes complete April coverage without
reviewing the underlying material.

Two O'Reilly book pages and Udemy blocked retrieval; historical metadata is
qualified. The O'Reilly live agenda totals three hours, but event availability
and paid session content were not verified. Whizlabs, partner and video responses
were shells. The MicrosoftLearning repository README and a Readiness Zone
landing page were read; full lab instructions, videos and paid questions/lessons
were not reviewed. The general Entra feed retrieved through June; specific
product pages and the September Microsoft blog supplied later evidence.

- [Improved enforcement for policies with resource exclusions](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/upcoming-conditional-access-change-improved-enforcement-for-policies-with-resour/4488925),
  Swaroop Krishnamurthy, January 28, with updated June 15 rollout note: main
  article read; accepted a client/scopes/resource/policy exercise. Specific
  current documentation supplies exceptions and configuration boundaries;
  comments and linked demonstrations are not implementation authority.
- [What's new in Microsoft Entra: September 2026](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/what%E2%80%99s-new-in-microsoft-entra-september-2026/4545179),
  Yina Arenas, September 1: main article read in this same session, with fresh
  retrieval. Accepted a catalog-governance exercise that preserves licensing,
  initialization and external-removal limitations from product documentation.

Research, repair and local checks used the same AI context; independent and
human review remain pending. The evidence ledger is
`ADLC_Docs/operations/2026-09-28-sc-300-deep-review.json`, preserving prior records,
objective mappings, observations, hashes, findings and local validation.
