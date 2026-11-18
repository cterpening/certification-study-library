# Completed visual brief: AZ-900 governance scope

**Status:** Independent AI-assisted draft; human review pending. Selected-objective
practice under the [official AZ-900 scope](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900),
accepted **Skills measured as of July 20, 2026** baseline. Technical source reading
on November 10, 2026 does not establish live Azure execution or human review.

**Learning question:** Why can a VM-create request be blocked when the identity
already has permission at the target resource group? Which evidence should be
checked before changing access?

**Exact objectives:** Describe Azure role-based access control (RBAC); Describe
the purpose of Azure Policy.

**Source binding:** Reuse unchanged unit `permissions-and-policy` from
`examples/study-packs/az-900-governance`. Its guide sections are Authentication and
authorization; Governance controls; Apply governance controls at the correct
scope; Worked example 6 — permission, policy, lock and data protection. The
[README](README.md) links the source package, canonical guide and exact registered
technical sources `azure-rbac-overview` and `azure-policy-overview`.

**Invented inputs:** Identity `app-deploy` has permission to create the requested
VM at `rg-research` inside `learning-sub`. An applicable subscription-level Policy
assignment requires East US and denies other locations. The request for `vm-study`
selects West US. No exclusion or exemption applies. The request is blocked.
The role description is a teaching shorthand, not an invented built-in role name.

**Visual decision:** Use a scope map rather than a row of fact cards. A large
subscription boundary encloses a labeled resource group. The identity sits
outside that boundary and connects to its role assignment and proposed request.
Two separate assignment connections reach the target resource-group scope.
The Policy connection starts from a subscription assignment; it is not a step
after RBAC. A dashed VM-request box marks proposed configuration rather than an
existing resource. This exposes the spatial relationships the learner must reason
about without asserting a service-internal evaluation sequence.

**Artwork and readability:** 1200 × 1400 editable SVG, original navy/teal/amber
layout consistent with the adjacent DP-900 timeline. Main body text is 24–28 px;
smaller text is reserved for short labels and provenance. The original Microsoft
resource-group, Policy and VM assets are isolated, byte-preserving SVG embeds with
visible product labels. The generic requester is original geometry. There is no
Policy icon standing in for RBAC. Meaning does not depend on color alone: borders,
line patterns, scope labels and request text also carry it.

**Study version:** Read the already-granted permission and the location mismatch;
identify the applicable deny; inspect error, configuration and assignment; use an
approved location or seek a legitimate approved exception. A broader role does
not resolve the stated Policy denial.

**Practice version:** Preserve all input evidence, boundaries and connections,
including the observed block. Replace diagnosis and correction with questions
asking for causal justification, evidence to inspect and a proposed next step.
The practice description contains only givens and prompts, not the worked answer.
The equivalent text exercise precedes the separate answer in README.

**Boundaries:** This is a simplified relationship map, not an exhaustive model of
deployment checks. No deployed resource is shown or claimed. Do not infer that
meeting the location rule guarantees success, that a permission grant bypasses
Policy, or that Policy never uses identity. **VERIFY CURRENT:** assignment scope,
effects, exclusions, exemptions and the actual error in a real environment.

**Success criteria:** The learner distinguishes the role's principal–permission–
scope association from the applicable governance requirement, uses the two
location values as evidence, and inspects the relevant failure before changing
access. This exercise does not claim exam readiness or recall an exam item.

**Exact inputs:** SHA-256 of UTF-8 text with CRLF/CR normalized to LF. The selected
unit uses `study_material.json_text` serialization; icon hashes use original bytes.

```text
Canonical guide:
09dafd7ca0dffee692577828c9efca74232f668469361d83e4a2b081c0d021f0
Accepted objective snapshot:
8b4c89d325b3ce339eb881aa2dc4b251888e6d7a07d6351d81bcc2123b1c4449
Source study-package manifest:
fa82722db742d1e1889f3a80192487b691452596e613963c755dd76be4157d28
Selected unit:
b582037da541e60d1f129e28eaf634a9cd3962a227f98dbcfb2e334847b3f68f
```

The generated [manifest](manifest.json) binds the source package, selected unit,
builder, shared helper, icon bundle and both SVGs. Rebuilding checks consistency;
content review remains separate and human review remains pending.
