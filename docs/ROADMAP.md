# Roadmap

## Phase 1: GitHub reference implementation

- Seed the five GitHub certification guides.
- Register the exams, vendors, canonical blueprints, and review state.
- Monitor Microsoft Learn objective changes.
- Validate guide paths, metadata, Markdown structure, and local links.
- Keep all guides explicitly marked as independent AI-generated drafts until reviewed.

## Phase 2: Source and coverage review

- Register the individual public sources already cited by the seed guides.
- Map published objectives to guide sections and supporting sources.
- Normalize guide structure and depth using `docs/GUIDE-QUALITY-STANDARD.md`; continue closing objective-level gaps independently of raw page length.
- Review material claims and promote guides independently to **SOURCE-VALIDATED**.
- Add alternative learning formats where they materially help, such as concise reviews, diagrams, and labs.
- Record known gaps without ranking one learning style as universally best.

## Phase 3: Public site

- Add a searchable static-site configuration.
- Generate navigation from the exam catalog.
- Show provenance, freshness, review state, and **VERIFY CURRENT** warnings prominently.
- Add strict site-build and accessibility checks before enabling GitHub Pages.

## Phase 4: Microsoft expansion (in progress)

- Use AI-103 and AB-100 to test the common schemas and guide template across engineering and architecture exams.
- Cover all active Microsoft 900/901 Fundamentals exams as of August 31, 2026: AZ-900, DP-900, PL-900, SC-900, AB-900, and AI-901.
- Complete source validation and practitioner review of the Microsoft first drafts.
- Revisit breadth only when Microsoft publishes or retires a 900/901 credential; AI-900 retired June 30, 2026 and is replaced here by AI-901.
- Add a genuinely different blueprint platform, such as AWS, Google Cloud, HashiCorp, or Databricks, before generalizing discovery adapters.
- Extract adapter and generator interfaces from demonstrated similarities rather than assumptions.

## Work integration

The work repository remains downstream. It may add private content and reformat public guides through a private overlay or build step. Internal content, branding, and presentation rules never become dependencies of the public project.
