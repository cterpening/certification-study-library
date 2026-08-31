---
exam_code: GH-500
vendor_id: github
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: ai-generated-draft
last_verified: 2026-08-30
upcoming_change_status: none-announced
upcoming_change_checked: 2026-08-30
---

# GH-500 GitHub Advanced Security Study Guide

> **Independent AI-assisted resource — AI-GENERATED DRAFT.** This guide uses public sources and may contain errors or become outdated. The [official GH-500 blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500) is authoritative.

**Current baseline:** Skills measured as of July 2026<br>
**Upcoming blueprint change:** None announced on the official study guide as of August 30, 2026.<br>
**Official source:** [GH-500 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500)

## How to use this guide

Study each suite as a lifecycle: enable, prevent, detect, prioritize, remediate, verify, measure, and govern. Complete the labs with a disposable repository, and practice explaining why an alert is actionable rather than merely recognizing its UI label.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map

| Domain | Weight |
|---|---:|
| Describe GitHub Security suites, features, and ecosystem | 15–20% |
| Configure and use Secret Protection | 15–20% |
| Configure and use supply-chain security | 15–20% |
| Configure and use Code Security | 10–15% |
| Security operations, prioritization, and remediation | 15–20% |
| GitHub Security suites administration | 10–15% |

The July 2026 blueprint uses newer suite terminology. Map older training terms carefully:

| Older/common term | Current blueprint grouping |
|---|---|
| Secret scanning and push protection | Secret Protection |
| Dependabot, dependency graph, dependency review | Supply Chain Security |
| Code scanning with CodeQL | Code Security |

**VERIFY CURRENT:** Packaging, entitlement, public-repository availability, GHES support, and UI names.

---

# 1. Secure-development operating model

GitHub security works across the development lifecycle:

```text
author → push protection → pull-request checks → merge policy
   → default-branch scanning → alert triage → remediation/campaign
```

Three broad risk classes:

- **Secrets:** Credentials or tokens exposed in code/history.
- **Dependencies:** Known vulnerabilities, malicious packages, licenses, and provenance.
- **Code:** Vulnerable data flows or coding patterns in first-party source.

## Prevention-first versus gate-based security

- Prevention-first controls stop defects close to creation: IDE feedback, push protection, secure templates, dependency policies, and pre-merge analysis.
- Gate-based controls block merge/deployment when defined checks fail.

Use both. Gates without early feedback create late friction; prevention without enforcement may be ignored.

## Roles

- Developers prevent, investigate, and remediate findings in their code.
- Security teams define risk policy, prioritize, advise, and coordinate campaigns.
- Administrators enable suites, configure defaults, permissions, policies, and integrations.
- Repository owners maintain workflows and respond within the product team.

Avoid giving broad organization ownership merely to let a security analyst manage alerts; use security-focused roles where available.

---

# 2. Security Overview, alerts, and campaigns

Security Overview aggregates posture and risk across repositories for authorized users. Use it to find:

- Repositories without expected features
- Alert totals and severity
- Secret, dependency, and code risk
- Remediation progress
- Teams or repositories needing attention

A security alert has a lifecycle: created/open, investigated, fixed or remediated, dismissed/closed, and sometimes reopened. Exact states vary by suite.

## Dismissal is a risk decision

Legitimate dismissal reasons can include false positive, test-only use, revoked credential, accepted risk, or code not used. Require rationale, evidence, approver, scope, and reconsideration trigger. Dismissal is not remediation and can hide exposure if used to improve dashboard numbers.

## Security campaigns

Campaigns coordinate remediation of selected alerts across repositories. They help define scope, owners, due dates, progress, and communications. Use them for a coherent risk-reduction goal—not as a replacement for routine alert ownership.

---

# 3. Secret Protection

## Detection

Secret Protection scans supported content/history for known partner patterns and custom patterns. Depending on feature and configuration, validity checks can identify whether some tokens appear active, helping prioritize response.

## Push protection

Push protection detects supported secrets during push and blocks or prompts before the secret enters the repository. It is prevention, not proof that the repository contains no secrets.

When bypass is allowed, governance may require a reason such as:

- False positive
- Test credential
- Will fix later

Bypass should be delegated only to appropriate roles, logged, reviewed, and monitored. “Will fix later” is not a safe routine workflow.

## Correct incident response order

If a real secret is committed:

1. Revoke or rotate it immediately.
2. Determine scope, permissions, age, and evidence of use.
3. Contain affected systems and investigate misuse.
4. Remove the secret from current content.
5. Decide whether history rewriting is required.
6. Coordinate rewritten-history impact with clones/forks/caches.
7. Document the incident and strengthen prevention.

Deleting the file, closing the alert, or adding `.gitignore` does not invalidate a credential already exposed.

## Configuration

Understand:

- Repository and organization enablement/defaults
- Public versus private/enterprise behavior
- Alert recipients and access
- Push-protection bypass and delegated bypass
- Exclusions and their risk
- Custom secret patterns
- APIs, webhooks, and external notifications

## Custom patterns

Create custom patterns for organization-specific token formats. Test against positive and negative examples. A pattern that is too broad creates alert fatigue and disruptive pushes; one that is too narrow misses variants. Avoid placing real secrets in test fixtures.

---

# 4. Supply Chain Security

## Dependency graph

The dependency graph derives dependencies and dependents from supported manifests, lock files, and submitted dependency data. It supplies context to alerts and SBOM export.

- Direct dependency: explicitly declared by the project.
- Transitive dependency: pulled in by another dependency.
- Dependency submission API: lets external build systems provide resolved dependency data.

## Vulnerability intelligence

- **CVE:** Identifier for a publicly disclosed vulnerability.
- **CWE:** Category of software weakness.
- **GitHub Security Advisory:** GitHub’s advisory record, often connected to CVEs and affected package ranges.
- **CVSS:** Severity scoring framework.
- **EPSS:** Probability-oriented estimate of exploitation likelihood in a future period.

Prioritization should combine severity, exploitability, reachability, exposure, asset importance, fix availability, and compensating controls. A high CVSS does not automatically outrank an actively exploitable lower-score issue on an internet-facing critical service.

## Dependabot alerts and updates

- Alert: dependency matches known vulnerable range.
- Security update: PR intended to remediate an alert.
- Version update: scheduled update to keep dependencies current.
- Grouped update: combines compatible dependency changes according to configuration.

Review generated PRs for breaking changes, tests, provenance, license, and transitive impact. Automatic PR creation is not automatic risk acceptance.

## Dependency Review

Dependency Review analyzes changes introduced by a PR. It can identify:

- Added or changed dependencies
- Vulnerability severity
- License information
- Dependency scope and relationship

Use it as a pre-merge control through Actions and rulesets. Configure fail criteria to match organizational policy.

## SBOM

An SBOM inventories software components and relationships. GitHub can export supported formats such as SPDX. An SBOM supports vulnerability response, customer/compliance requests, and supply-chain analysis, but it does not by itself verify provenance or absence of vulnerabilities.

## Automation and integration

Know alert permissions, assignment, APIs, webhooks, external notifications, update rules, auto-dismiss behavior, campaigns, and remediation PRs. Auto-dismiss reduces noise only when the rule accurately represents accepted risk.

---

# 5. Code Security and CodeQL

## Code scanning choices

GitHub can ingest results from CodeQL and third-party static-analysis tools. Choose based on language support, query depth, existing tooling, compliance, performance, and integration.

**SARIF** is the interoperable results format used to upload supported static-analysis findings. Uploading SARIF does not transform the third-party engine into CodeQL; it centralizes compatible results.

## CodeQL mental model

CodeQL builds a database representing the code and runs queries over it. Dataflow and taint-tracking queries can follow potentially unsafe data from a source to a sensitive sink through intermediate transformations.

Important concepts:

- Language detection and support
- Build mode and compilation requirements
- Default setup versus advanced configuration
- Query suites and custom queries
- Scheduled, push, and pull-request analysis
- Matrix strategies for languages
- Database creation, query execution, and result upload

## Default versus advanced setup

- Default setup minimizes maintenance and uses GitHub-managed configuration.
- Advanced setup provides workflow-level control over languages, builds, queries, schedules, packs, and integration.

Choose advanced configuration because requirements need it—not merely because it looks more sophisticated.

## Scan frequency

- Pull-request scans provide feedback before merge.
- Push/default-branch scans protect integrated code.
- Scheduled scans can detect newly understood vulnerabilities without code changes.

## Triage and remediation

Inspect severity, precision, path, source-to-sink flow, affected branch, introduced commit, and query help. CodeQL autofix can propose changes for supported alerts, but humans must review correctness, completeness, tests, and side effects.

Dismiss only with documented evidence. A result may be false positive, test-only, not used, or accepted risk; reasons and permissions matter.

## Troubleshooting

Check language support, workflow permissions, event, build commands, generated code, memory/disk/time, runner image, query pack versions, database creation, SARIF limits, and upload category. For compiled languages, a failed or incomplete build can produce missing analysis.

---

# 6. Security operations and remediation

## Risk-based workflow

1. Establish coverage and ownership.
2. Validate the alert and affected asset.
3. Assess exposure, exploitability, and business impact.
4. Contain urgent risk.
5. Select upgrade, code fix, rotation, configuration, or compensating control.
6. Test and deploy remediation.
7. Confirm alert closure and absence of regression.
8. Record decision and prevention improvement.

## Rules and SLAs

Define severity/remediation policies using business context. Example:

| Class | Example response |
|---|---|
| Exposed valid production secret | Immediate rotation and incident response |
| Critical reachable code vulnerability | Urgent containment and expedited remediation |
| High vulnerable production dependency | Time-bound upgrade with owner |
| Low-confidence unreachable finding | Normal triage with documented evidence |

Do not memorize an invented SLA as a GitHub requirement; organizations define risk appetite and regulatory obligations.

## Collaboration

Route findings to teams that can act. Use issues, PRs, assignments, campaigns, code owners, and security roles. Protect sensitive vulnerability details until disclosure is appropriate.

## Custom detection

- Custom CodeQL queries detect organization-specific vulnerable patterns.
- Query suites group queries by purpose.
- Custom secret patterns recognize internal credentials.
- Dependency policy can enforce vulnerability and licensing thresholds.

Custom detection requires tests, version control, ownership, performance monitoring, documentation, and a false-positive process.

---

# 7. Administration at scale

Rollout hierarchy:

```text
enterprise entitlement/policy
    → organization defaults and security managers
        → repository enablement/configuration
            → developer workflow and alert response
```

## Rollout plan

1. Inventory repositories, languages, visibility, criticality, and existing tools.
2. Assign security roles and alert owners.
3. Establish default configurations and approved advanced variants.
4. Pilot on representative repositories.
5. Enable suites in phases.
6. Define bypass, dismissal, and exception governance.
7. Integrate alerts with operational systems.
8. Measure coverage, age, remediation, bypass, and recurrence.
9. Improve preventive controls.

## Permissions and enforcement

Separate permission to view alerts, manage configurations, dismiss findings, bypass push protection, administer policies, and own repositories. Use delegated security roles and least privilege.

Rulesets and required workflows can enforce pre-merge security evidence. Enterprise/organization policies define availability and defaults. APIs support bulk configuration and reporting.

## GHEC versus GHES

**VERIFY CURRENT:** Security suite availability, update cadence, supported CodeQL versions/languages, default setup, campaigns, validity checks, and APIs differ between GitHub Enterprise Cloud and GHES releases.

---

# 8. Objective-by-objective security deep dive

## Use one lifecycle across all three suites

Secret, dependency, and code findings differ technically, but a common operating lifecycle makes them manageable:

```text
inventory → enable → prevent → detect → enrich → prioritize
          → assign → contain → remediate → verify → learn → measure
```

- **Inventory** determines which repositories, languages, manifests, branches, and teams exist.
- **Enable** establishes supported features and configurations.
- **Prevent** moves feedback before exposure or merge.
- **Detect** produces findings through patterns, advisory matching, or analysis.
- **Enrich** adds validity, reachability, exploitability, ownership, and business context.
- **Prioritize** decides what must happen first.
- **Assign** gives an accountable team and deadline.
- **Contain** limits urgent exposure before the full fix.
- **Remediate** removes or safely mitigates the risk.
- **Verify** confirms the change and alert state.
- **Learn** improves coding, dependency, secret, and platform controls.
- **Measure** shows coverage, flow, age, recurrence, and accepted residual risk.

An alert dashboard covers only part of this lifecycle. A mature program connects detection to people, engineering workflows, and evidence.

> **Related item:** Mean time to remediate is a flow metric, while open-alert count is an inventory metric. A falling inventory can mean remediation, dismissal, or disabled scanning; pair metrics so improvement cannot be faked by changing classification alone.

## Security suites and architecture

### Map control to risk and development phase

| Risk | Earliest useful control | Pre-merge control | Post-merge/continuous control |
|---|---|---|---|
| Secret exposure | Local secret hygiene and push protection | Secret scanning on proposed content where supported | History scanning, validity, alert response |
| Vulnerable dependency | Approved ecosystems and update policy | Dependency Review with policy | Dependency graph, alerts, security updates, campaigns |
| Vulnerable first-party code | Secure patterns and IDE feedback | Code scanning on pull request | Default-branch and scheduled analysis |

The earliest control reduces remediation cost, but later controls remain necessary. Developers can bypass a local practice; a vulnerability may be disclosed after merge; a query or advisory can improve without a code change.

### Separate product coverage from operational coverage

Product coverage asks whether a feature is enabled and successfully analyzing the relevant content. Operational coverage asks whether findings have an owner, severity model, response process, exception path, and verification. Track both.

Example coverage questions:

- Which repositories are eligible for each suite?
- Which default branches and active release branches are analyzed?
- Which languages, package managers, manifests, lock files, and build systems are supported?
- Which repositories have failed or stale scans?
- Which alerts have no accountable team?
- Which exceptions have expired?

> **Related item:** An asset inventory should include archived, generated, template, fork, and inactive repositories because their treatment may differ. Excluding them silently produces misleading coverage percentages.

## Alert triage as a documented decision

### Build an alert evidence packet

For any suite, capture:

- repository, visibility, branch, and affected version;
- finding type, severity/priority, and detection source;
- introduced commit, path, dependency chain, or credential type;
- application exposure and business criticality;
- likely exploitability, validity, or reachability;
- available remediation and breaking-change risk;
- owner, due date, decision, and verification evidence.

Triage answers “what does this finding mean in this system?” It is not a synonym for closing the alert.

### Choose an outcome precisely

| Outcome | Meaning | Required evidence |
|---|---|---|
| Remediate | Remove the vulnerable condition or exposed credential | Fix, tests, deployment/rotation, rescan or alert closure |
| Mitigate | Reduce likelihood or impact without removing root condition | Compensating control, scope, owner, review date |
| False positive | Detection does not represent the claimed condition | Technical explanation and reproducible evidence |
| Not affected / unreachable | Component exists but vulnerable path is not usable in this context | Dependency or dataflow evidence and change trigger |
| Accept risk | Accountable owner accepts residual risk | Rationale, authority, duration, and compensating controls |

Do not use “used in tests” as a universal dismissal. Test code can expose real credentials, enter distributed packages, or run in privileged CI environments.

> **Related item:** Threat modeling asks how an attacker reaches an asset and what trust boundaries are crossed. Adding even a lightweight data-flow or dependency-path view makes alert prioritization more defensible than severity alone.

## Secret Protection in depth

### Understand detection boundaries

Secret scanning uses supported partner patterns and, where configured, custom patterns. Detection quality depends on the content scanned, token format, pattern quality, exclusions, and product availability. A clean result does not detect credentials with unknown formats, encrypted payloads, dynamically assembled values, unsupported storage, or secrets held outside scanned GitHub content.

Validity checking, when available for a token type and configuration, enriches prioritization. “Inactive” does not prove the historical exposure was harmless, and “unknown” does not prove safety.

### Design custom patterns using precision and recall

- **Precision** asks what fraction of matches are genuine secrets.
- **Recall** asks what fraction of genuine secrets the pattern detects.

Create a recognizable prefix and structure for internal credentials when you control their format. Combine a focused regular expression with additional match requirements where supported. Test with generated, nonfunctional positive cases; near-miss negative cases; boundary cases; encoded or formatted variants; and representative repository text.

Roll a pattern out in stages. Observe detection volume before turning on disruptive prevention. Assign an owner for pattern changes and regressions.

### Push-protection decision flow

When a push is blocked:

1. Identify the match without exposing it further.
2. If it is a real credential, remove it from the commit and rotate if it was ever usable or shared.
3. If it is generated test data, replace it with an unmistakably nonfunctional fixture where possible.
4. If it is a false positive, document evidence and improve the custom pattern.
5. Use bypass only through the governed reason/role process.
6. Review bypass telemetry for repeated workflow or training problems.

“Will fix later” creates an exposure and cleanup obligation. It should be exceptional and visible.

### Incident scope is broader than Git history

After a credential enters a repository, investigate clones, forks, pull-request refs, Actions logs and artifacts, caches, package outputs, notifications, mirrors, search indexes, and downstream systems as appropriate. Rotation contains future credential use; history cleanup reduces continued disclosure. They solve different problems.

> **Related item:** Secretless design reduces the amount of secret material that scanning must catch. OIDC federation, managed identities, short-lived tokens, and runtime vault retrieval shrink credential lifetime and repository exposure, though they still require authorization and audit design.

## Supply-chain security in depth

### Interpret the dependency graph

Manifest files express desired dependencies; lock files often record resolved versions and transitive relationships. Build-time dependency submission can fill gaps for ecosystems or build processes whose resolved graph is not fully visible from repository files. If the graph is incomplete, alerts and SBOMs derived from it are incomplete too.

When an alert names a transitive dependency, trace which direct dependency introduced it and whether an updated direct version resolves the chain. Removing an unused manifest or regenerating a lock file can change the graph, but verify the built artifact rather than optimizing the dashboard.

### Evaluate an advisory

Read:

- affected ecosystem/package and vulnerable version range;
- patched versions and workarounds;
- severity and scoring vector;
- weakness and attack prerequisites;
- exploit maturity or EPSS where appropriate;
- whether the vulnerable functionality is present and reachable;
- whether the component ships to or executes in the affected environment.

A dependency in a developer tool, test scope, container layer, and production runtime creates different exposure. Do not dismiss solely from dependency scope without considering CI and build privileges.

### Design Dependabot update policy

A `.github/dependabot.yml` configuration should reflect ecosystems, directories, schedules, target branches, grouping, reviewers/assignees, labels, open-PR limits, and organization policy. Group compatible low-risk updates to reduce noise, but keep urgent or high-risk changes visible and independently deployable when needed.

Security updates respond to known vulnerabilities; version updates reduce age and future upgrade distance. Both need tests and ownership. Auto-merge should require trustworthy test evidence, bounded update types, and branch controls—not merely a bot-authored pull request.

### Dependency Review as change control

Dependency Review answers what a pull request adds, removes, or changes in the supply chain. Configure the action and enforcement to match vulnerability severity, license policy, and repository risk. A blocked PR should provide a remediation path so developers understand whether to upgrade, choose an alternative, request an exception, or correct generated dependency data.

### SBOM, provenance, and signing

An SBOM inventories components. Provenance describes how an artifact was built. A signature binds an identity to content or a claim. None replaces the others:

| Question | Evidence |
|---|---|
| What components are included? | SBOM |
| Which build produced this artifact from which source? | Provenance/attestation |
| Has this content or claim changed, and who signed it? | Signature verification |
| Are included components vulnerable now? | Current advisory matching and context |

> **Related item:** Vulnerability status changes after release as advisories evolve. Preserve or regenerate component inventory and continuously reassess deployed artifacts; a one-time clean build is not permanent assurance.

## Code Security and CodeQL in depth

### Choose the analysis path

Use CodeQL where supported languages and its semantic/dataflow analysis match the requirement. Use a third-party scanner when it provides required language, rule, regulatory, or specialized analysis. Upload SARIF when centralized GitHub alert workflow is useful. Multiple tools can coexist, but duplicate findings need ownership and categorization.

### CodeQL database and query mental model

CodeQL extracts a relational representation of source and, for some languages/build modes, build information. Queries select patterns and paths from that representation. A taint-tracking query typically defines:

```text
source of untrusted data
    → allowed propagation steps
    → sanitizers/barriers
    → sensitive sink
```

The displayed path explains why the engine connected source to sink. Review the code and query help to decide whether the path is feasible and whether validation truly blocks it.

### Select setup and build mode

Default setup is appropriate when supported language detection and managed configuration cover the repository. Advanced setup is justified when you need explicit languages, custom build commands, custom queries/packs, schedules, categories, runner selection, or integration with an existing workflow.

For compiled code, analysis quality depends on extracting the relevant build. Automatic or no-build modes may be available for supported languages/scenarios; a manual build gives control when generation, flags, or unusual layouts matter. **VERIFY CURRENT** the supported build modes for each language.

### Design scan events

- Pull-request analysis finds introduced problems before merge and typically compares relevant changes.
- Push analysis protects integrated branches and establishes default-branch alerts.
- Scheduled analysis can apply new query knowledge to unchanged code.
- External CI can create a database/run analysis and upload SARIF with appropriate authentication.

Do not grant a scan workflow unnecessary write permission. Keep analysis of untrusted contributions separated from privileged deployment or secret-bearing jobs.

### Interpret SARIF categories

When uploading multiple result sets for a commit—such as different languages, tools, or build variants—use stable categories so GitHub distinguishes analyses rather than treating one upload as a replacement for another. Ensure result locations map to repository paths and that upload limits and supported schema behavior are respected.

### Triage a dataflow alert

1. Read the query help, severity, precision, and CWE mapping.
2. Follow the source-to-sink path.
3. Determine whether the source is attacker controlled in this deployment.
4. Inspect guards and sanitizers for semantic effectiveness, not just their names.
5. Identify affected branches/releases and similar patterns.
6. Fix near the appropriate boundary and add a regression test.
7. Review an autofix as an untrusted proposed change.
8. Rescan and verify the deployed remediation where risk requires it.

> **Related item:** Static analysis reasons about code without observing every runtime state; dynamic testing observes executions but misses untested paths. Combining static analysis, tests, runtime controls, and review produces stronger assurance than expecting one tool to prove safety.

## Security operations at scale

### Prioritize with a context stack

Use layers rather than a single score:

1. **Finding confidence:** Is the detection precise and technically valid?
2. **Exposure:** Can an attacker reach the affected code, secret, or component?
3. **Exploitability/validity:** Is exploitation plausible or is the credential active?
4. **Impact:** What privilege, data, service, or business process is affected?
5. **Prevalence:** How many repositories, artifacts, or environments share it?
6. **Fixability:** Is a safe patch, rotation, or mitigation available?
7. **Time pressure:** Is exploitation active, disclosure imminent, or a deadline applicable?

Then assign a response class. Preserve the factors so another reviewer can understand the decision.

### Use campaigns for bounded outcomes

A campaign should have a coherent selection rule, affected owners, due date, communication, exception path, and closure definition. Good examples include removing one vulnerable library line, rotating a family of internal credentials, or fixing a high-confidence CodeQL query across a service portfolio.

Avoid a campaign containing every open alert. It provides no useful priority and competes with routine ownership.

### Measure flow and control health

Track:

- eligible versus enabled repositories;
- successful versus failed/stale analysis;
- new, closed, dismissed, and reopened findings by suite;
- age and time to triage/remediate by risk class;
- push-protection blocks and bypass reasons;
- dependency-update merge and failure rates;
- campaign progress and overdue exceptions;
- recurrence of the same weakness, token type, or package;
- repositories without owners or with inaccessible alerts.

Segment by repository criticality and team. Enterprise averages can hide a high-risk backlog in one business unit.

> **Related item:** A security service needs an error budget for its own reliability: failed scans, unavailable runners, stale indexes, noisy rules, and broken update PRs all reduce the protection developers actually receive.

## Administration and governance in depth

### Define configuration tiers

One configuration rarely fits every repository. Define approved tiers such as:

- **Baseline:** standard suites and managed defaults for supported repositories.
- **Enhanced:** protected branches, dependency review enforcement, scheduled scans, stricter secret policy, and shorter response goals for production code.
- **Specialized:** advanced CodeQL builds, custom queries/patterns, external CI, or regulatory reporting for exceptional architectures.

Repositories should inherit the highest appropriate tier from classification, with documented overrides. A specialized configuration must still meet baseline outcomes.

### Separate duties and permissions

Map permissions for enabling suites, editing configuration, viewing alerts, dismissing, bypassing, managing custom patterns/queries, creating campaigns, changing enforcement, and administering repositories. Grant security managers or other delegated roles where sufficient. Reserve organization ownership for responsibilities that truly require it.

### Automate safely

Use APIs to inventory, enable, report, and integrate at scale, but account for pagination, rate limits, partial failure, retries, and idempotency. Log desired and actual state. Test policy changes in a representative organization before broad rollout. Protect the automation identity and its source/release pipeline.

### Plan GHEC and GHES separately

For GHES, connect feature planning to the exact supported appliance release, CodeQL bundle/query compatibility, update cadence, Actions/runners, network egress, and external integration constraints. For GHEC, account for service-side rollout, enterprise policy, data location, and current entitlement. Never copy a cloud configuration matrix into a server plan without checking the target release documentation.

> **Related item:** Configuration drift can be intentional. A useful compliance report distinguishes approved exception, temporary migration state, unsupported repository, failed automation, and unauthorized drift instead of labeling all differences identically.

## Knowledge checks

1. Secret scanning reports a token as inactive. What historical and downstream exposure questions remain before closing the incident?
2. A custom pattern blocks many UUIDs. Which precision/recall problem is visible, and how would you test a safer revision?
3. A transitive dependency alert has a patch, but the package is used only by a build tool. Which CI and artifact risks should be assessed before dismissal?
4. A Dependency Review check reports a forbidden license but the merge is still allowed. Which enforcement connection is missing?
5. Two SARIF uploads for the same commit overwrite one another. What stable classification should be investigated?
6. CodeQL shows a source-to-sink path through a function named `sanitize`. Why is the function name not sufficient evidence?
7. An enterprise reports 100% feature enablement but half its CodeQL runs fail. Which coverage measure is misleading?
8. A security campaign closes many alerts through accepted-risk dismissals. Which flow and exception metrics reveal whether risk actually decreased?

For each answer, identify prevention, detection, evidence, owner, exception, and verification.

---

# 9. Hands-on labs

## Lab 1: Secret response

Use a nonfunctional test pattern. Configure a custom secret pattern, observe push protection, practice justified bypass governance, and write a response beginning with revocation—not file deletion.

## Lab 2: Dependency Review

Create a sample application with a lock file. Add a dependency through a PR, enable dependency review, configure severity/license policy, and inspect the dependency graph and generated alert/update flow.

## Lab 3: SBOM and prioritization

Export an SBOM. Select sample advisories and rank them using CVSS, EPSS, reachability, exposure, asset criticality, and fix availability. Document why severity alone is insufficient.

## Lab 4: CodeQL setup

Enable default setup, inspect a dataflow alert, then design when advanced configuration would be justified. Upload a harmless sample SARIF file from a third-party scanner.

## Lab 5: Security campaign

Design a campaign for a vulnerable dependency across multiple repositories. Define inclusion, owners, due date, progress measurement, exceptions, and closure criteria.

## Lab 6: Enterprise rollout

Create a rollout plan for Terraform, PowerShell, Python, and application repositories. Include suite defaults, unsupported-language strategy, security roles, APIs, bypass, metrics, and GHES/GHEC differences.

---

# 10. Exam distinctions

| Contrast | Remember |
|---|---|
| Secret detection vs push protection | Finds exposure versus prevents supported push |
| Revoke vs delete | Invalidates credential versus removes one copy |
| Dependency graph vs SBOM | GitHub relationship model versus exportable inventory document |
| Alert vs security update | Reports risk versus proposes remediation PR |
| Version update vs security update | Currency maintenance versus vulnerability remediation |
| CVE vs CWE | Vulnerability instance versus weakness category |
| CVSS vs EPSS | Severity characteristics versus exploitation probability estimate |
| Dependency Review vs Dependabot alert | PR change analysis versus known-vulnerable dependency alert |
| CodeQL vs SARIF | Analysis engine/query system versus results interchange format |
| Default vs advanced setup | Managed simplicity versus workflow customization |
| Dismissal vs remediation | Close/accept classification versus remove or contain risk |
| Prevention vs gate | Stop defect early versus block progression at checkpoint |
| Security Overview vs audit log | Risk posture aggregation versus event history |

---

# 11. Readiness checklist

- [ ] I distinguish Secret Protection, Supply Chain Security, and Code Security.
- [ ] I can explain prevention-first and gate-based controls across the SDLC.
- [ ] I can configure and respond to secret detection, push protection, bypass, exclusions, and custom patterns.
- [ ] My secret response begins with rotation/revocation and investigation.
- [ ] I understand dependency graph, alerts, updates, Dependency Review, SBOM, CVE, CWE, CVSS, and EPSS.
- [ ] I can choose default/advanced CodeQL or a third-party SARIF integration.
- [ ] I can inspect dataflow, triage alerts, evaluate autofix, and troubleshoot scans.
- [ ] I can design risk-based remediation, campaigns, SLAs, dismissals, and exceptions.
- [ ] I can assign security roles and govern alert, bypass, dismissal, and policy permissions.
- [ ] I can roll out suites using defaults, policies, rulesets, APIs, metrics, and approved variants.
- [ ] I know which plan, public/private, GHEC/GHES, UI, and preview details require current documentation.

## Primary references

- [GitHub security documentation](https://docs.github.com/en/code-security)
- [Secret scanning and push protection](https://docs.github.com/en/code-security/secret-scanning)
- [Supply-chain security](https://docs.github.com/en/code-security/supply-chain-security)
- [Dependency Review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review)
- [SBOM export](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository)
- [Code scanning](https://docs.github.com/en/code-security/code-scanning)
- [CodeQL documentation](https://codeql.github.com/docs/)
- [SARIF support](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)
- [Security Overview](https://docs.github.com/en/code-security/security-overview)
- [Security campaigns](https://docs.github.com/en/code-security/securing-your-organization/fixing-security-alerts-at-scale/about-security-campaigns)

Recheck suite names, entitlement, feature availability, GHES support, validity checks, campaigns, APIs, and default configurations immediately before the exam.

---

# Places to learn

This is a curated starting point, not a complete list, and it is not meant to be consumed in full. Start with the official paths, then pick the explanations, formats, and practice that work for you and close specific blueprint gaps. Times are approximate consumption time at normal speed; labs, note-taking, review, and independent practice add time.

| Resource | Access | Estimated time | Best use and caveat |
|---|---|---:|---|
| [Microsoft Learn — GitHub Advanced Security Part 1](https://learn.microsoft.com/en-us/training/paths/github-advanced-security/) and [Part 2](https://learn.microsoft.com/en-us/training/paths/github-advanced-security-2) | Free | About 12–16 hours | Official starting point, including secret, supply-chain, CodeQL, and administration modules |
| [Microsoft Learn GH-500 video course](https://www.youtube.com/playlist?list=PLahhVEj9XNTcJZjBU671JAiX8St3CV5dA) | Free | About 6–8 hours | Official instructor-led reinforcement for visual learners |
| GitHub Skills: [Secure repository supply chain](https://github.com/skills/secure-repository-supply-chain) and [Secure Code Game](https://github.com/skills/secure-code-game) | Free account | About 2–4 hours | Practical security exercises; some enterprise controls require an appropriately licensed lab |
| [Pluralsight — GH-500 GitHub Advanced Security](https://www.pluralsight.com/paths/gh-500-github-advanced-security) | Subscription | 13 hours | Seven-course 2026 path taught by [Timothy Warner](https://www.pluralsight.com/authors/tim-warner), with feature courses and exam strategy |
| [GitHub Security Lab](https://securitylab.github.com/) | Free | Select 3–8 hours by gap | CodeQL research, queries, and security concepts beyond minimum exam preparation |
| [MeasureUp — GH-500 practice test](https://www.measureup.com/microsoft-gh-500-github-advanced-security-practice-test.html) | Paid test or subscription; free demo may be available | About 4–8 hours for simulation and review | Tier 6 assessment with 100 questions; the detailed domains cover Advanced Security, but unrelated Copilot copy appears on the public page, so resolve conflicts with the official blueprint and GitHub Docs |

No current individual Whizlabs, O'Reilly, or instruction-first Udemy GH-500 course was verified during the August 30, 2026 review. See the broader [Places to learn catalog](../docs/LEARNING-RESOURCES.md).
