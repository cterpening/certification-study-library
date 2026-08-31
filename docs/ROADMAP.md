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
- [x] Establish machine-readable review evidence and promote GH-900 and GH-300 after source validation.
- [x] Deepen and source-validate all five GitHub certification guides.
- [x] Add structured correction/source forms and weekly source-health monitoring.
- Add alternative learning formats where they materially help, such as concise reviews, diagrams, and labs.
- Record known gaps without ranking one learning style as universally best.

## Phase 3: Public site

- [x] Add a searchable static-site configuration.
- [x] Generate navigation and guide cards from the exam catalog.
- [x] Show provenance, freshness, review state, and **VERIFY CURRENT** warnings prominently.
- [x] Add a strict site build and generated-link validation.
- [ ] Complete keyboard, contrast, mobile, screen-reader, and print review.
- [x] Add and approve the GitHub Pages deployment workflow.

## Phase 4: Microsoft expansion (in progress)

- Use AI-103 and AB-100 to test the common schemas and guide template across engineering and architecture exams.
- Cover all active Microsoft 900/901 Fundamentals exams as of August 31, 2026: AZ-900, DP-900, PL-900, SC-900, AB-900, and AI-901.
- Complete source validation and practitioner review of the Microsoft first drafts.
- [x] Establish the Azure fundamentals depth and source-validation pattern with AZ-900.
- [x] Deepen and source-validate DP-900 against the July 21, 2026 objective baseline.
- Revisit breadth only when Microsoft publishes or retires a 900/901 credential; AI-900 retired June 30, 2026 and is replaced here by AI-901.
- [x] Add a genuinely different blueprint platform before generalizing discovery adapters, using HashiCorp Terraform Associate (004) as the pilot.
- [x] Extract the first shared objective-monitor boundary from demonstrated Microsoft Learn and HashiCorp Developer differences.

## Phase 5: Vendor-neutral pilot (in progress)

- [x] Generate provider navigation, cards, catalogs, and labels from `data/vendors.json` rather than fixed GitHub/Microsoft lists.
- [x] Add HashiCorp Terraform Associate (004) as the first non-Microsoft-platform guide.
- [x] Support provider-published objective maps that do not include percentage weights.
- [x] Add and test a HashiCorp Developer objective adapter alongside the Microsoft Learn adapter.
- [x] Complete source validation of the Terraform Associate draft.
- Complete practitioner review of the Terraform Associate guide.
- Use the next provider pilot to test a third blueprint format before defining a broader adapter interface.

## Work integration

The work repository remains downstream. It may add private content and reformat public guides through a private overlay or build step. Internal content, branding, and presentation rules never become dependencies of the public project.
