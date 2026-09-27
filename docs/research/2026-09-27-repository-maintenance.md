# Repository maintenance review — September 27, 2026

The sweep included **all 223 published guides across 26 vendors**, **42 official
catalog/announcement sources**, and **3,374 registered source URLs** including six
new citations. **20 guides were updated.** The new [recurring process](../AUTOMATION.md#complete-recurring-maintenance-review)
collects these checks into a weekly review task with a row for every guide.

This is a source-change and lifecycle review, not a fresh technical or lab audit of
every guide. Historical full-review dates and accepted objective snapshots remain
unchanged. Future exam material is labeled separately from current study baselines.

## Evidence and coverage

| Check | Result |
|---|---:|
| Final automated objective/status comparisons: unchanged | 102 |
| Final automated comparisons: candidate difference | 80 |
| Objective checks requiring manual extraction | 40 |
| Retired objective baseline preserved | 1 |
| Unresolved unexpected objective transport/extraction errors after recovery | 0 |
| Official PDFs downloaded and parsed | 28 |
| PDF bytes identical to September 17 evidence | 28 |
| Registered source URLs reachable / blocked / missing | 2,560 / 809 / 5 |
| Source metadata differences needing triage | 135 |
| Catalog/announcement scopes unchanged / changed / blocked / new baseline | 32 / 3 / 6 / 1 |

The first objective run had 100 unchanged results, 71 differences, 40 manual
results and 11 errors. Bounded retries recovered ten Microsoft/MOS requests.
Security+ required a canonical version-page correction. The CompTIA adapter now
also captures the `Duration:` label, which adds a monitoring signal without
implying that the exam duration changed. Candidate differences include old
unaccepted differences, status-only signals, formatting and extraction changes;
they are **not 80 newly revised blueprints**.

The PDF check covers 17 Palo Alto Networks blueprints, ten Splunk blueprints, and
the retired Snowflake SOL-C01 transition FAQ. Identical downloaded bytes establish
that those files have not changed since the prior review; the HTML monitor's
manual-review results remain intact. Thirteen other manual objective checks
remain: three Salesforce, three MongoDB, two ServiceNow, two Python Institute and
three JS Institute guides. An HTTP shell is not a readable blueprint.

The machine-readable per-guide evidence ledger at
`ADLC_Docs/operations/2026-09-27-repository-maintenance.json`
records all 223 outcomes, affected source URLs, current extraction hashes,
before/after guide hashes, PDF comparisons, catalog differences and limitations.
Full local monitor output and candidate diffs are under the ignored
`.maintenance/2026-09-27-reviewed/` directory. The workflow retains equivalent
artifacts for 90 days. Public vendor PDFs and full page bodies were not republished.

## Applied updates

| Guides | Applied change and official evidence |
|---|---|
| AB-730 | Added the October 20 four-domain preparation map, Work IQ/Cowork explanations, an original practice exercise and readiness checks. The [revised blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-730), [Cowork documentation](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/) and [Work IQ documentation](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/) support distinct scope and implementation claims. |
| DP-750, DP-800 | Added October 19 scope notices for bundle naming, clustering terminology, vector-search terminology and the removed CES mention. Existing implementation material remains labeled against its original baseline. See [DP-750](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-750) and [DP-800](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-800). |
| DP-600, DP-700 | Added October 19 notices for editorial terminology changes; no new weighted domain claimed. See [DP-600](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-600) and [DP-700](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-700). |
| SC-900, SC-100, SC-200 | Added October 21 notices covering workload identities/threat-intelligence naming, SOAR/Copilot terminology, and Azure activity-log wording respectively. See [SC-900](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900), [SC-100](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100), and [SC-200](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200). |
| MB-330 | Added the October 21 revision notice and removed the claim that the June 2025 outline is the only published authority. The [change log](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/mb-330) identifies minor revisions; weighted domains remain unchanged. |
| DP-300, MD-102, MS-700 | Added October 27 notices for secure-enclave scope, current Intune terminology, and Teams terminology respectively. See [DP-300](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-300), [MD-102](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/md-102), and [MS-700](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ms-700). |
| DP-420, PL-400 | Added future transition maps and original design exercises for October 6 and October 16. These identify additional preparation; they are not complete technical rewrites of the replacement scopes. See [DP-420](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-420) and [AB-400](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-400). |
| AB-100 | Reconciled Expert credential naming in the guide and seed inventory while keeping the exam/credential prerequisite distinction. See the [credential page](https://learn.microsoft.com/en-us/credentials/certifications/agentic-ai-business-solutions-architect/). |
| AZ-802 | Removed current-beta claims and recorded active delivery in the guide, exam/seed catalogs, README and inventory documentation. The [credential page](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-administrator-associate/) and [exam page](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-802/) no longer carry the beta designation. |
| SY0-701 | Pointed the blueprint monitor at the [V7 page](https://www.comptia.org/en-us/certifications/security/v7/), replaced the unconfirmed-successor claim with the announced [SY0-801/V8 scope and planned November 17 launch](https://www.comptia.org/en-us/certifications/security/v8/), and retained V7's language-specific 2027 retirement dates. Added version-selector monitoring. |
| NSE-7-SASE | Added Japanese to the delivery languages from the [FortiSASE 26 Architect page](https://training.fortinet.com/local/staticpage/view.php?page=fortisase_architect_exam). |
| GH-100, GH-900 | Added dated GHES release/version-selection guidance and the current browser-editor name. See the [GHES release ledger](https://docs.github.com/en/enterprise-server@latest/admin/all-releases) and [VS Code for the Web documentation](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor). |

The source catalog and link-evidence counts include the six added official
citations. None of these changes constitutes independent human review.

## Catalog findings

Microsoft's AB-100 title change, CompTIA's DataSys+/Client Pro URL changes, and an
Oracle ClearTrial implementation credential listing differ from the September 17
catalog baseline. The CompTIA URL differences do not establish new exam families;
the Oracle listing remains an intake candidate requiring individual blueprint
and eligibility review. No speculative new guide was added from a catalog label.

The Security+ root page now links V7 and V8. Its separate selector scope is new,
and its baseline was accepted after both version pages were inspected. The
discovery Markdown renderer was fixed so an unchanged exam-reference field no
longer hides a changed credential title.

Cisco, MongoDB, ServiceNow, IBM and two OpenAI catalog/status pages still require
manual retrieval in this run. Prior browser reviews remain historical evidence.
Catalog listing comparisons do not validate every linked credential or every
technical statement in a guide.

## Remaining access and source work

Most initial link failures recovered on a slower retry. These five URLs still
returned 404 twice:

| Registered source | Affected guides | Disposition |
|---|---|---|
| `az-ssh-direct-centos-stream9-hv-sock-package` | AZ-800, AZ-802 | The version-pinned RPMFind page is missing. Keep the historical packaging claim separate from a current support statement; locate current package evidence before updating it. |
| `cisa-qae-database` | CISA | The store URL is missing to the monitor; a cached search result is not proof of current availability. Confirm the current QAE product route. |
| `nse-5-secure-networking-source-4` | NSE-5-SECURE-NETWORKING | Reconfirm the FortiSwitch 7.6 documentation route; do not substitute another product/version. |
| `nse-5-security-operations-source-4` | NSE-5-SECURITY-OPERATIONS | Reconfirm the FortiAnalyzer 7.6 documentation route. |
| `nse-6-secure-networking-source-7` | NSE-6-SECURE-NETWORKING | Reconfirm the FortiVoice documentation route and tested version. |

The 809 blocked source responses include rate limits, provider bot controls and
access barriers; they are not 809 confirmed broken links. A separate supplemental
fetch attempted 323 overview/reference URLs, but failures and application shells
prevent claiming a new lifecycle review for every overview. Exact responses are
retained in the evidence ledger. The unresolved SC-401 and AWS replacement-date
conflicts from the [September 17 review](2026-09-17-exam-validation.md) remain
explicit dated tasks rather than silently selected dates.

## Repeatable follow-through

The new maintenance calendar at `config/certification-maintenance.json`
contains 27 review tasks, including imminent AWS/Windows Server transitions,
October blueprint revisions, the Security+ replacement and language deadlines.
The weekly workflow preserves failed checks, produces candidate diffs and
refreshes one review issue. It does not automatically rewrite explanations,
advance full-review dates, retire exams, or accept changed snapshots.

For each finding, inspect the official evidence, update the affected guide and
registered sources, validate the repository/site, and accept only the reviewed
baseline. Keep future scope, current delivery and uncertain vendor claims
separate throughout that process.
