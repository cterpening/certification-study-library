# UX, Responsive, and Accessibility Conformance Report

## Assessment envelope

- Target: `certification-study-library`; reference-only accelerator revision `82d4bca`.
- Source revision: `858bdfc664f1b8e94ce03ab041acf3fbba7c4f07`; assessed on 2026-09-06. September 5 filenames preserve the approved action-plan paths.
- Mode/profile: Snapshot / standard; status: **partial**. Public repository files and bounded local Git only; no project tests, builds or scanners executed in this pass.
- Budget: target 10 minutes, ceiling 20 minutes per lane; maximum eight assessment checks; zero external evidence requests. Shared reads and the validated September 5 facts were reused.
- Finding set: [validated JSON](../findings/2026-09-05-ux-accessibility-conformance.json). Findings below retain canonical fingerprints across overlapping reports; do not sum repeated findings as unique risks.
- Handling: approved-external. Selected public repository evidence was processed by the active Codex session; artifact publication to the existing Git origin is separately user-authorized. No other evidence-provider requests occurred.
- Retention/review: repository owner; artifacts retained under the approved `ADLC_Docs/` paths and Git history. Retention period, expiry action and assistant service retention/region are unspecified. Findings review pending; no risk acceptance or implementation approval inferred.

## Scope

Product area: homepage, catalog, short/long guides, navigation, search and reading controls. Devices/breakpoints tested in this assessment: none. Intended review widths from the repository checklist are 320, 768, 1024 and 1440 CSS pixels, in both themes.

## Conformance summary

| Check area | Status | Severity / limitation | Evidence | Notes |
|---|---|---|---|---|
| Keyboard navigation | Not assessed | Manual evidence gap | `docs/ACCESSIBILITY.md`; focus-visible CSS | No end-to-end keyboard path |
| Focus management | Partial source evidence | Runtime behavior unknown | `website/assets/stylesheets/extra.css`; search labeling JS | No focus-order/trap verification |
| Contrast | Historical diagnostic only | Current conformance unknown | Documented August 31 Lighthouse results and prior fixes | No fresh color/theme measurement |
| Semantic structure | Partial | Structure checks are narrower than accessibility | `scripts/validate_site.py`, tests, template headings/labels | Skip-link/H1 checks exist; no new test run |
| Responsive layout | Partial source evidence | Mobile/tablet/desktop behavior unverified | CSS breakpoints and manual checklist | No viewport/zoom execution |
| Reduced motion / print | Partial source evidence | User experience unverified | Media queries in custom CSS | No rendered verification |
| Discoverability / status labels | Observed source intent | Usability not tested | Catalog hierarchy and human-review labels | No participant usability evidence |

## Historical evidence

The repository describes a mobile homepage Lighthouse run on August 31 and a GH-300 sample. Those are dated diagnostic statements in local documentation; raw reports and a repeat run were not supplied. Their high scores do not close the nine unchecked manual tasks.

## Remediation plan

| Priority | Issue | Proposed approach | Owner | Due date |
|---|---|---|---|---|
| 1 | Unrecorded manual accessibility evidence | Execute the existing checklist on representative pages and retain browser/AT/date/results | Site maintainer | Not supplied |
| 2 | Runtime evidence after theme/navigation changes | Repeat applicable viewport, zoom, focus and contrast checks | Site maintainer | Change-triggered, owner to schedule |

No specific WCAG criterion failure or compliant-site verdict is invented from static inspection.

## Canonical findings

### Accessibility verification has no recorded completion evidence

- Fingerprint: `repository-health:accessibility:manual-evidence-unrecorded`; low severity, high confidence; disposition: open.
- Observation: The repository provides a concrete nine-item manual accessibility checklist, but every item remains unchecked. The local CI definitions validate generated structure and links but do not record keyboard, screen-reader, zoom, responsive, contrast, print, or reduced-motion results. This is an evidence gap, not a finding that the site itself fails accessibility requirements.
- Evidence: `docs/ACCESSIBILITY.md`; `.github/workflows/validate-repository.yml`.
- Proposed action: Execute the documented manual accessibility matrix against a representative site build and retain dated evidence, automating only repeatable checks that complement rather than replace assistive-technology review.
- Proposed owner: site maintainers; due date not supplied.

## Limitations and next decision

No browser, assistive technology, screenshot test or fresh accessibility scan was run. Historical Lighthouse descriptions and source CSS/HTML cannot establish current WCAG 2.2 AA conformance or responsive behavior.

No collection error was reported. Observations above come from local evidence; consequences and recommended actions are assessment judgments. Historical checks are labeled with their original date. Review the findings before any backlog, specification or implementation work.

