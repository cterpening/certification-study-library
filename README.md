# Certification Study Library

An independent, AI-assisted, source-driven library of certification study guides. The collection began with GitHub and Microsoft credentials and now includes HashiCorp Terraform as its first non-Microsoft-platform pilot. Each guide connects public exam objectives with original explanations, practical exercises, and further learning resources.

> **Independent project:** This repository is not affiliated with, sponsored by, or endorsed by GitHub, Microsoft, HashiCorp, IBM, or any listed certification or training provider.

> **Use the official blueprint:** Guides may contain errors or become outdated. The current official vendor exam guide is always authoritative. Recheck every item marked **VERIFY CURRENT** before relying on it.

## What this library is

People learn in different ways. This project does not prescribe one learning path or claim that one resource is best for everyone. It provides several ways to approach the same published objective:

- concise notes for review;
- deeper explanations and distinctions;
- practical examples and independent labs;
- readiness checklists and original scenario questions;
- links to official documentation and legitimate public resources.

Quality here means that material is current enough to be useful, traceable to public sources, clear about uncertainty, aligned with the published objectives, and respectful of exam integrity.

## What this library is not

This is not an exam dump or a reconstruction of live exam content. The repository does not accept recalled questions, leaked items, VCE files, scraped question banks, paid-course reproductions, confidential training, or employer and customer material. See the [content and exam-integrity policy](docs/CONTENT-POLICY.md).

## GitHub certification seed

| Exam | Guide | Canonical blueprint | Review state |
|---|---|---|---|
| GH-900 | [GitHub Foundations](guides/GH-900-github-foundations.md) | [Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900) | Source-validated |
| GH-300 | [GitHub Copilot](guides/GH-300-github-copilot.md) | [Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300) | Source-validated |
| GH-200 | [GitHub Actions](guides/GH-200-github-actions.md) | [Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200) | Source-validated |
| GH-100 | [GitHub Enterprise Administrator](guides/GH-100-github-enterprise-administration.md) | [Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100) | Source-validated |
| GH-500 | [GitHub Advanced Security](guides/GH-500-github-advanced-security.md) | [Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500) | Source-validated |

These guides are the seed content brought forward from the earlier `CertificationNotes` prototype. All five now have dated [source-validation records](docs/SOURCE-VALIDATION.md); a separate human contributor review is still required before any guide becomes community reviewed.

## Microsoft certification expansion

| Exam | Guide | Canonical blueprint | Review state |
|---|---|---|---|
| AI-103 | [Developing AI Apps and Agents on Azure](guides/AI-103-developing-ai-apps-and-agents-on-azure.md) | [Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103) | Source-validated |
| AB-100 | [Agentic AI Business Solutions Architect](guides/AB-100-agentic-ai-business-solutions-architect.md) | [Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-100) | Source-validated |
| AZ-900 | [Microsoft Azure Fundamentals](guides/AZ-900-microsoft-azure-fundamentals.md) | [Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900) | Source-validated |
| DP-900 | [Microsoft Azure Data Fundamentals](guides/DP-900-microsoft-azure-data-fundamentals.md) | [Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-900) | Source-validated |
| PL-900 | [Microsoft Power Platform Fundamentals](guides/PL-900-microsoft-power-platform-fundamentals.md) | [Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-900) | Source-validated |
| SC-900 | [Microsoft Security, Compliance, and Identity Fundamentals](guides/SC-900-microsoft-security-compliance-identity-fundamentals.md) | [Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900) | Source-validated |
| AB-900 | [Microsoft 365 Copilot and Agent Administration Fundamentals](guides/AB-900-microsoft-365-copilot-agent-administration-fundamentals.md) | [Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-900) | AI-generated draft |
| AI-901 | [Microsoft Azure AI Fundamentals](guides/AI-901-microsoft-azure-ai-fundamentals.md) | [Microsoft Learn](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901) | Source-validated |

These are substantial first drafts, not finished certification products. They establish the cross-vendor content pattern while leaving room for source validation and practitioner review. AI-900 is not included because Microsoft retired it on June 30, 2026; AI-901 is its active successor.

## HashiCorp certification pilot

| Exam | Guide | Canonical blueprint | Review state |
|---|---|---|---|
| Terraform Associate (004) | [HashiCorp Certified: Terraform Associate (004)](guides/TERRAFORM-ASSOCIATE-004-hashicorp-terraform-associate.md) | [HashiCorp Developer](https://developer.hashicorp.com/certifications/infrastructure-automation) | Source-validated |

Terraform Associate proves the vendor-neutral catalog, website, objective monitor, unweighted-domain presentation, and source-validation gate against a blueprint platform other than Microsoft Learn. The guide targets Terraform 1.12 and includes the official 004 additions: lifecycle/dependency decisions, custom conditions, ephemeral and write-only data handling, and expanded HCP Terraform coverage.

## Source and review principles

1. The official vendor blueprint defines exam scope.
2. Official product documentation is preferred for technical behavior.
3. Material factual claims should be traceable to a registered or directly linked source.
4. AI-generated interpretation must remain distinguishable from source fact.
5. Pricing, UI, models, limits, availability, preview behavior, retention, and similar volatile details are **VERIFY CURRENT** topics.
6. Third-party training may be cataloged and evaluated, but not copied.
7. Blueprint changes create review work; automation does not silently rewrite study advice.

The full source hierarchy and citation expectations are in [Source and citation quality](docs/SOURCE-QUALITY.md).

## Review states

| State | Meaning |
|---|---|
| AI-generated draft | Generated or assembled with AI assistance from public sources; full review is incomplete |
| Source-validated | Objective coverage and citations have been checked |
| Community reviewed | A contributor has reviewed the complete guide |
| Review required | A canonical source changed after the last review |
| Retired | The vendor retired or replaced the credential |

## Automated blueprint monitoring

The scheduled objective monitor:

1. Downloads each configured official objective page.
2. Selects the provider's registered objective adapter and extracts a normalized objective section.
3. Records the published baseline labels and explicit future-update or retirement announcements.
4. Compares both records with the reviewed snapshots in `data/objective-snapshots`.
5. Proposes changed snapshots through a pull request.
6. Creates a review task instead of mechanically rewriting a guide.

See [Automation and maintenance](docs/AUTOMATION.md).

## Repository layout

```text
.
├── .github/workflows/          # Validation and objective monitoring
├── adapters/                   # Vendor-specific discovery-adapter design
├── config/exams.json           # Vendor-neutral exam registry
├── data/                       # Source/vendor registries and objective snapshots
├── docs/                       # Project, policy, source, and operating guidance
├── generator/                  # Generation design and future implementation
├── guides/                     # Public certification study guides
├── schemas/                    # Vendor-neutral catalog schemas
├── scripts/                    # Monitoring and repository validation
├── templates/                  # New-guide templates
└── tests/                      # Monitor and validation tests
```

## Local validation

Repository checks use the Python standard library:

```bash
python -m unittest discover -s tests -v
python scripts/validate_repository.py
```

## Website preview

The searchable website is generated from the exam and collection catalogs plus an explicit publication allowlist. The homepage supports browsing by provider or by overlapping editorial focus area. The canonical guides remain in `guides/`; `.site-build/` and `site/` are disposable generated output.

```bash
python -m pip install -r requirements-site.txt
python scripts/prepare_site.py
python -m mkdocs serve --config-file .site-build/mkdocs.yml
```

For a production-equivalent check:

```bash
python scripts/prepare_site.py
python -m mkdocs build --strict --config-file .site-build/mkdocs.yml
python scripts/validate_site.py
```

Successful pushes to `main` deploy the validated site to [GitHub Pages](https://cterpening.github.io/certification-study-library/) through the dedicated Pages workflow. See [Publishing](docs/PUBLISHING.md) for the build, deployment, and repository-setting details.

## Suggesting a learning source

Add an unevaluated course, repository, playlist, book, or documentation page to `data/source-candidates.json`. The candidate inbox requires only the exact URL, a short reason, and any likely exam mappings. Accepted resources are promoted to the evaluated master catalog in `data/sources.json`; they do not become trusted merely by being submitted.

See [Adding a source for review](docs/SOURCE-INTAKE.md) for the entry format and review lifecycle.

Approved sources are checked weekly for reachability, redirects, page-title and canonical-URL changes, duration signals, and stale review dates. Findings create review work; the automation never silently rewrites guides or source metadata.

## Public and work repositories

This public repository is intended to remain the authoritative public-source-safe project. Publicly accessible material is not necessarily in the legal public domain, so the library cites and links to external sources rather than republishing them. A work environment can synchronize the repository and combine it with a separate private overlay. Internal links, licensed training, employer guidance, and proprietary examples must never be merged into this public history.

See [Updating the work mirror](docs/WORK-MIRROR.md) for the separation model.

## Project documentation

- [Changelog](CHANGELOG.md)
- [Project brief](docs/PROJECT-BRIEF.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Content and exam-integrity policy](docs/CONTENT-POLICY.md)
- [Source and citation quality](docs/SOURCE-QUALITY.md)
- [Source-validation records](docs/SOURCE-VALIDATION.md)
- [Adding a source for review](docs/SOURCE-INTAKE.md)
- [Guide depth and related-item standard](docs/GUIDE-QUALITY-STANDARD.md)
- [Places to learn](docs/LEARNING-RESOURCES.md)
- [Roadmap](docs/ROADMAP.md)
- [Automation and maintenance](docs/AUTOMATION.md)
- [Accessibility statement and test evidence](docs/ACCESSIBILITY.md)
- [Publishing](docs/PUBLISHING.md)
- [Updating the work mirror](docs/WORK-MIRROR.md)
- [Third-party notices](THIRD-PARTY-NOTICES.md)

## License

Original repository content is provided under the [Creative Commons Attribution 4.0 International License](LICENSE). Vendor names, product names, trademarks, and linked external material remain the property of their respective owners.
