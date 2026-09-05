# Infrastructure Inventory — Certification Study Library

> **Last updated:** 2026-09-05 · **Discovery version:** 1 (initial brownfield baseline)

## Assessment result

No owned Azure infrastructure, ARM export, Resource Graph result, Terraform/Bicep configuration, container definition, Kubernetes/Helm configuration, application database, queue, cache, private endpoint, or runtime network configuration was present in the approved local evidence.

This result means **no application infrastructure was observable in this repository**. It does not prove that no externally configured hosting or repository service exists.

## Resource groups

Not applicable. No Azure resource-group evidence was supplied or collected.

## Resources

| Resource or service | State | Evidence | Limitation |
|---|---|---|---|
| GitHub repository | Stated by local configuration and documentation | Local Git configuration, `docs/PUBLISHING.md` | Remote settings and current service state were not queried |
| GitHub Actions | Local definitions observed | `.github/workflows/` | Enablement, run history, required checks, and artifacts are unknown |
| GitHub Pages | Deployment intent observed | `.github/workflows/deploy-pages.yml`, `docs/PUBLISHING.md` | Pages setting, environment protection, deployed commit, and availability are unknown |
| Python package source | Installation dependency stated | `requirements-site.txt`, workflow install steps | Registry/mirror, resolved transitive graph, and current availability were not queried |

The certification subjects described in the guides—Azure, AWS, Oracle, IBM, and other vendor services—are educational content and are not treated as deployed infrastructure evidence.

## Networking

- No owned VNet, subnet, firewall, private endpoint, DNS zone, ingress, or application egress policy was found.
- `scripts/check_official_study_guides.py` and `scripts/check_source_health.py` are capable of outbound HTTPS requests to registered public sources.
- No network request was performed during Brownfield discovery.
- GitHub-hosted runner and Pages network behavior remains provider-managed and unassessed.

## Identity and access

| Identity | Type | Scope | Evidence state |
|---|---|---|---|
| GitHub Actions `GITHUB_TOKEN` | Repository-scoped workflow identity | Issue, content, and pull-request operations according to each workflow's declared permissions | Configuration observed; actual grants and use not verified |
| Repository collaborators/teams | Human or group identities | Repository administration and review | Unknown; remote access prohibited |
| Pages deployment identity/environment | Provider-managed workflow boundary | Static-site deployment | Definition observed; environment protections unknown |

No credential value, service principal, managed identity, cloud role assignment, or secret-store configuration was found locally.

## Cross-system dependencies

- Official vendor sites supply public blueprint and product evidence to network-capable maintenance scripts.
- GitHub Actions supplies scheduled and change-triggered execution.
- GitHub Issues and pull requests receive proposed maintenance work from workflows when remote permissions permit.
- GitHub Pages receives the validated static artifact.
- The work-mirror flow described by repository documentation is a separate downstream boundary; no mirror repository was included in this assessment.

## Infrastructure-as-code decision

Terraform starter generation is **not applicable and not authorized** for this component. There is no local or supplied live infrastructure baseline to import, and creating placeholder infrastructure would manufacture state rather than document it.

## Blocked evidence

Remote GitHub settings, Actions history, Pages configuration, environment protection, release state, and deployment status require a separately approved authenticated read-only evidence pass.

