# Contributing

Contributions should make the library more useful without pretending that every learner needs the same explanation or resource.

This is a best-effort library based on public information. Publish useful, supported findings while making uncertainty visible. If sources conflict, cite both, describe the conflict and mark **More research needed — next pass** rather than choosing an unsupported answer. Document lab errors, unavailable tools and steps that were not executed; distinguish observed results from expected results. Community fixes are welcome with reproduction steps or public evidence. An unresolved limitation does not mean the rest of a guide is unusable.

When a credential is renamed, preserve its former name in the inventory's `aliases` list under the same vendor and exam code. The LMS lookup export uses both current and former names; an alias alone does not establish that older course content covers the current blueprint.

## Guide changes

Every substantive guide change should:

1. identify the official skills-measured version being targeted;
2. map the change to a published objective;
3. prefer official vendor documentation for technical claims;
4. place descriptive citations near the claims they support;
5. mark volatile behavior with **VERIFY CURRENT**;
6. distinguish blueprint coverage from useful practical depth;
7. update labs, distinctions, and readiness checks when affected;
8. avoid recalled exam questions, answer dumps, confidential material, and unsupported predictions.

Different formats are welcome when they help learners approach the material differently. Concise reviews, deeper explanations, diagrams, examples, and hands-on labs should agree on the underlying facts even when their teaching styles differ.

Use the [guide depth and related-item standard](docs/GUIDE-QUALITY-STANDARD.md) when expanding a guide. Prefix adjacent context with `Related item:` so readers can distinguish useful supporting knowledge from the published objective map.

## Resource additions

Evaluate a specific resource rather than endorsing an entire marketplace or provider. Record enough information for a learner to decide whether it fits their needs, including format, access model, coverage, strengths, gaps, publication or update date, and source quality.

New, unevaluated links belong in `data/source-candidates.json`, following [Adding a source for review](docs/SOURCE-INTAKE.md). Accepted candidates move to the master `data/sources.json` catalog only after source-quality, licensing, exam-integrity, and objective-fit review.

Do not copy protected content. A public landing page may support factual catalog metadata, but it is not evidence for technical product behavior.

## Pull-request evidence

Include:

- the affected objective and authoritative source;
- what changed and why;
- affected guide sections;
- known product, plan, or preview limitations;
- validation performed;
- any remaining **VERIFY CURRENT** items.

Review the [content policy](docs/CONTENT-POLICY.md) and [source-quality policy](docs/SOURCE-QUALITY.md) before contributing.

## Local validation

For a repository-wide currency review, run `python scripts/run_certification_maintenance.py --output-dir .maintenance/<new-run-name> --mode monthly`.
Follow the [maintenance review process](docs/AUTOMATION.md#complete-recurring-maintenance-review), including dated transitions and blocked sources. Do not advance historical full-review dates solely because an automated extraction matches.

```bash
python -m unittest discover -s tests -v
python scripts/validate_repository.py
python scripts/prepare_site.py
python -m mkdocs build --strict --config-file .site-build/mkdocs.yml
python scripts/validate_site.py
```

Install the pinned website dependency with `python -m pip install -r requirements-site.txt` before running the site build. Site navigation comes from `config/exams.json`; do not hand-edit generated files under `.site-build/` or `site/`.

External links are not automatically stable facts. Confirm that each linked page directly supports the associated claim.

For a small correction or source report, use the repository's structured issue forms rather than preparing a pull request. Choose content correction, objective change, source problem, or source suggestion so the report includes the exam, exact URL or section, evidence, and public-source/exam-integrity confirmation.

Promoting a guide to the internal `source-validated` state—displayed publicly as **Sources + objectives checked — human review pending**—also requires a passed record in `data/reviews.json`. The validator checks that the record uses the current blueprint hash, that every external guide link has an exact source-catalog entry, and that its link-health counts still match the tracked baseline.

The sources-and-objectives gate may be performed by an AI agent when it follows the documented [AI-agent validation workflow](docs/SOURCE-VALIDATION.md#ai-agent-validation-workflow). AI validation does not qualify a guide for the **Community reviewed** label; that label remains reserved for a separately recorded complete human review.
