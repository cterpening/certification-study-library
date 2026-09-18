# Monitor maintenance — September 17, 2026

## Scope and status

Local repairs for GitHub issues [#17](https://github.com/cterpening/certification-study-library/issues/17) and [#18](https://github.com/cterpening/certification-study-library/issues/18). Neither issue is closed by this record. Changes require publication and a scheduled-run recheck.

## Objective workflow (#18)

The [September 14 run](https://github.com/cterpening/certification-study-library/actions/runs/34878597896) reported 63 changed exams, zero unexpected errors, and 40 documented manual-review limitations. It pushed a snapshot branch, then failed because GitHub Actions is not permitted to create pull requests. The original issue incorrectly described unknown source failures.

Repairs distinguish setup/test, extraction, and publication failures; provide the run and branch links; retain diagnostics for 30 days; use body files; and keep the PR title short regardless of the number of changed exams. Failures still fail the workflow.

Repository administration must allow workflow-created PRs, or a maintainer must create the PR from [the existing snapshot branch](https://github.com/cterpening/certification-study-library/pull/new/automation/objective-update-34878597896). Snapshot changes have not been merged or represented as reviewed guide changes.

## Source health (#17)

The [September 15 run](https://github.com/cterpening/certification-study-library/actions/runs/35000140355) reported 3,367 sources, two request errors, and 109 metadata changes. The September 17 local full scan reported four errors and 139 metadata changes; runner/provider differences mean these totals are not directly interchangeable.

Completed:

- Replaced the SEI C wiki URL with its officially linked GitHub Pages successor in the catalog and three guides.
- Replaced the broken OWASP API project URL and Salesforce Secure route with current official pages. Salesforce guidance now distinguishes customer Agent Users from employee agents using the logged-in user context.
- NTIA and the temporarily timed-out OWASP NoSQL page both passed local rechecks. NTIA still needs a GitHub-runner TLS recheck; certificate verification remains enabled.
- Accepted 63 reviewed title-only changes. This is metadata acceptance, not a claim that all underlying technical content was freshly audited.
- Made duration ordering deterministic and comparison independent of ordering. Real duration changes remain reviewable.
- Six Fortinet SAML sign-in redirects now correctly report blocked access, without storing per-request signed login parameters. Live targeted checks confirmed all six.
- Fixed subset baseline writes so reviewed selections cannot erase unrelated observations.
- Refreshed link-evidence counts and dated the maintenance notes without claiming a new practitioner review.

## Remaining review

Validation of the local repairs passed: all 124 unit tests, repository validation,
strict MkDocs build, generated-site validation, workflow YAML/shell syntax checks,
and `git diff --check`. These are local results; no changed workflow has run on GitHub.

A replay of the captured full scan, replacing only the targeted recheck results and comparing against the selectively updated baseline, leaves **67 metadata changes and 1 request error**. This is not a second full live scan. Unreviewed baseline entries remain unchanged.

The remaining request error is `az-ssh-direct-centos-stream9-hv-sock-package`: its version-specific rpmfind page returns 404. Find authoritative replacement package evidence before changing the documented SSH Direct evidence boundary.

Priority: DP-420 title/scope, AI-500 and Windows Server lifecycle labels, Fortinet exam durations, then course runtimes and documentation moves. MongoDB generic course shells continue to need enrolled reconciliation. Updated guide hashes remain eligible for the next AI audit; no old audit was rebound to changed text.

| Source ID | Changed metadata |
|---|---|
| `ab-650-control-system-overview` | final_url, page_title, canonical_url |
| `ab-650-copilot-control-measurement` | final_url, page_title, canonical_url |
| `ab-730-learn-path` | page_title |
| `ab-730-pluralsight` | duration_signals |
| `ai-500-certification-page` | page_title |
| `ai-500-exam-page` | page_title |
| `anthropic-develop-tests` | duration_signals |
| `anthropic-learning-resources` | duration_signals |
| `aws-ans-c01-whizlabs` | page_title |
| `az-104-pluralsight-path` | duration_signals |
| `az-305-measureup-practice-test` | duration_signals |
| `az-305-whizlabs-resources` | final_url, page_title, canonical_url |
| `az-800-replacement-credential` | page_title |
| `az-801-doc-33-azure-to-azure-tutorial-enable-replication` | duration_signals |
| `az-ssh-direct-fedora44-selinux-vsock` | page_title |
| `comptia-220-1201-linkedin` | duration_signals |
| `comptia-220-1202-linkedin` | duration_signals |
| `comptia-fc0-u71-linkedin` | duration_signals |
| `databricks-dep-system-tables` | duration_signals |
| `databricks-genai-evaluation` | page_title |
| `dp-300-pluralsight-path` | duration_signals |
| `dp-420-blueprint` | page_title |
| `dp-700-eventhouse-monitoring` | page_title, duration_signals |
| `fortimanager-adoms-7-6-6` | canonical_url |
| `fortinet-fortios-760-admin-guide` | canonical_url |
| `fortinet-nse4-fortios-76-exam` | duration_signals |
| `github-docs-actions-retention` | page_title |
| `github-docs-copilot-mcp-management` | final_url, canonical_url |
| `github-docs-copilot-policies` | final_url, canonical_url |
| `github-docs-ghes-admin` | final_url, page_title, canonical_url |
| `github-docs-ghes-high-availability` | final_url, page_title, canonical_url |
| `github-docs-ghes-support-bundles` | final_url, page_title, canonical_url |
| `github-ghes-release-ledger` | final_url, page_title, canonical_url |
| `github-status` | duration_signals |
| `google-paa-cloud-storage-overview` | duration_signals |
| `hcp-terraform-policy-enforcement` | final_url, page_title, canonical_url |
| `hcp-terraform-policy-sets` | final_url, canonical_url |
| `lf-ckad-pluralsight` | duration_signals |
| `linkedin-isc2-ccsp-cert-prep` | duration_signals |
| `linkedin-isc2-cissp-2024-cert-prep` | duration_signals |
| `linkedin-isc2-sscp-cert-prep` | duration_signals |
| `mb-310-pluralsight` | duration_signals |
| `microsoft-365-copilot-architecture-ab900` | duration_signals |
| `microsoft-ai-at-work-roadmap-transition` | duration_signals |
| `mongodb-atlas-administrator-path` | page_title |
| `mongodb-developer-practice-questions` | page_title |
| `mongodb-python-developer-path` | page_title |
| `nse-5-cloud-security-source-2` | duration_signals |
| `nse-5-sase-blueprint` | duration_signals |
| `nse-5-secure-networking-source-2` | duration_signals |
| `nse-6-cloud-security-source-4` | duration_signals |
| `nse-6-sase-source-1` | duration_signals |
| `nse-6-sase-source-6` | duration_signals |
| `nse-6-secure-networking-source-3` | duration_signals |
| `nse-6-security-operations-source-3` | duration_signals |
| `nse-6-security-operations-source-6` | duration_signals |
| `nse-7-sase-blueprint` | duration_signals |
| `nse-7-secure-networking-blueprint` | duration_signals |
| `nse-8-source-1` | duration_signals |
| `panw-cloud-security-professional-source-5` | final_url, page_title, canonical_url |
| `panw-xsoar-engineer-source-5` | final_url |
| `pl-400-credential` | duration_signals |
| `pluralsight-200-301-path` | duration_signals |
| `pluralsight-gh-300` | duration_signals |
| `pluralsight-professional-javascript-path` | duration_signals |
| `pluralsight-python-essentials` | duration_signals |
| `salesforce-agentblazer-legend-2026` | duration_signals |

## Accepted title-only observations

The explicit acceptance set is retained for review:

- `ab100-google-production-ready-agents`
- `ai-500-agent-a2a-endpoint`
- `ai-500-agent-framework-human-loop`
- `ai-500-agent-framework-orchestrations`
- `ai-500-agent-identity-concepts`
- `ai-500-agent-obo-flow`
- `ai-500-ai-red-teaming-agent`
- `ai-500-apim-mcp-overview`
- `ai-500-blueprint`
- `ai-500-course`
- `ai-500-guardrail-intervention-points`
- `ai-500-learn-architect-path`
- `ai-500-learn-build-path`
- `ai-500-learn-govern-path`
- `ai-500-learn-operate-path`
- `ai-500-multiple-agent-architecture`
- `anthropic-academy-ai-capabilities`
- `anthropic-academy-ai-fluency`
- `anthropic-partner-network-certification-announcement`
- `anthropic-services-track-partner-hub`
- `aws-aif-c01-whizlabs`
- `aws-clf-c02-whizlabs`
- `aws-dea-c01-whizlabs`
- `aws-dop-c02-whizlabs`
- `aws-dva-c02-whizlabs`
- `aws-saa-c03-whizlabs`
- `aws-sap-c02-whizlabs`
- `az-104-whizlabs`
- `az-700-whizlabs-course`
- `az-800-whizlabs`
- `az-801-whizlabs`
- `az-802-official-labs`
- `cisa-certification-requirements`
- `cisa-exam-content-outline`
- `cisa-free-practice-quiz`
- `cisa-maintenance-requirements`
- `cisa-qae-database`
- `cism-certification-page`
- `cism-certification-requirements`
- `cism-exam-content-outline`
- `cism-free-practice-quiz`
- `cism-maintenance-requirements`
- `cism-review-manual-16`
- `crisc-certification-page`
- `crisc-certification-requirements`
- `crisc-exam-content-outline`
- `crisc-free-practice-quiz`
- `crisc-maintenance-requirements`
- `google-ace-whizlabs`
- `google-pca-whizlabs`
- `google-pde-whizlabs`
- `isaca-online-review-courses`
- `matplotlib-documentation`
- `md-102-windows-laps`
- `microsoft-power-apps-code-apps-overview-pl900`
- `panw-network-security-professional-source-5`
- `pluralsight-cisa-2024-path`
- `pluralsight-cof-c03-path`
- `pluralsight-crisc-path`
- `python-3-library-reference`
- `whizlabs-ab-900`
- `whizlabs-ai-901`
- `whizlabs-az-900`
