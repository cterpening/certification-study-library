# Accessibility evidence — 2026-09-06

## Outcome

**Partial evidence; manual accessibility review remains open.** The generated-site contract
and a four-page responsive browser smoke sample passed. No keyboard-only session, screen-reader
session, browser-zoom review, contrast inspection, or print review was performed, so this record
is not a WCAG conformance claim and does not close the manual-evidence finding.

## Environment and scope

| Item | Recorded value |
|---|---|
| Date | 2026-09-06 |
| Operating system | Windows (local repository runner) |
| Browser | Microsoft Edge 152.0.4191.66, headless DevTools Protocol |
| Generated site | Strict local MkDocs build; 290 HTML pages |
| Representative pages | Homepage, study-guide catalog, CLF-C02 short guide, GH-300 long guide |
| Themes sampled | Light and dark |
| Widths sampled | 320, 768, 1024, and 1440 CSS pixels |
| Assistive technology | Not available in the execution environment; NVDA was not found |

## Automated structural checks

`scripts/validate_site.py` passed all 290 generated HTML pages after its accessibility contract
was expanded. Each non-error page must have a document language and title, exactly one main
landmark and H1, a skip link whose fragment exists, unique IDs, `alt` attributes on images,
programmatic names for enabled form controls and buttons, and header cells in every table.
The existing local-link and anchor checks run in the same pass.

These rules are regression guards for testable markup properties. They do not establish correct
reading order, useful alternative text, control operability, announcement quality, contrast,
reflow usability, or semantic quality in context.

## Browser rendering smoke sample

Edge was started headlessly with an isolated ignored profile. Device metrics and color-scheme
preferences were set through the browser's DevTools Protocol; after navigation, the rendered DOM
was queried for its actual inner width, document scroll width, title, main landmark, and H1.

| Page | Theme | Requested / actual width | Document width | Horizontal overflow | Main / H1 |
|---|---|---:|---:|---|---:|
| Homepage | Light | 320 / 320 | 320 | No | 1 / 1 |
| Study-guide catalog | Dark | 768 / 768 | 768 | No | 1 / 1 |
| CLF-C02 short guide | Light | 1024 / 1024 | 1024 | No | 1 / 1 |
| GH-300 long guide | Dark | 1440 / 1440 | 1440 | No | 1 / 1 |

This is evidence that the four pages loaded with their expected landmarks and did not overflow
horizontally at those widths. It is not a substitute for visual, zoom, keyboard, or assistive-
technology inspection. Disposable screenshots and the browser profile remain under the ignored
`.site-build/` directory and are not retained as repository evidence.

## Manual matrix still required

| Check | State | Gap to close |
|---|---|---|
| Keyboard-only path and focus order | Not run | A person must exercise all interactive regions and record focus visibility, order, and traps. |
| Screen reader on four representative pages | Not run | Run NVDA or another supported reader and record headings, landmarks, controls, tables, code, links, and status announcements. |
| Browser zoom at 200% and 400% | Not run | Visually inspect reflow, clipping, overlap, and necessary two-dimensional regions. |
| Responsive visual review in both themes | Partial | Width and overflow telemetry passed; a person must inspect content visibility and usability. |
| Contrast and non-color cues | Not run | Re-run an approved contrast tool and visually inspect focus, links, badges, controls, and both themes. |
| Print / PDF | Not run | Inspect a long guide for content visibility, page breaks, tables, code, and link treatment. |
| Reduced motion | Not run | Confirm the operating-system preference suppresses non-essential transitions during interaction. |

## Re-run triggers

Repeat the structural and browser checks after theme, template, navigation, search, or custom CSS
changes. Repeat the complete manual matrix after a material interaction or visual-system change
and before representing the site as accessibility-reviewed.
