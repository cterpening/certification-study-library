---
exam_code: WDA-41-01
vendor_id: js-institute
official_blueprint: https://jsinstitute.org/wda-exam-syllabus
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# WDA-41-01 Certified Associate Web Developer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The public syllabus, exam status, links, technical references, and exam-integrity boundaries were reviewed September 29, 2026. The complete current indexed HTML syllabus was manually compared with all 40 retained objective subjects after direct fetching and automated monitoring failed. This same-context AI review includes original executed examples; independent human review remains pending. This guide contains original explanations and questions, not exam items. Recheck the [official WDA page](https://jsinstitute.org/wda-certification) and [WDA-41-01 syllabus](https://jsinstitute.org/wda-exam-syllabus) before scheduling.

**Current baseline:** WDA-41-01, active; syllabus last updated September 16, 2025<br>
**Upcoming blueprint change:** no replacement identified in the inspected current credential, HTML syllabus and certification overview; this is not a claim that every announcement channel or booking system was audited<br>
**Official delivery snapshot:** 40 single- and multiple-select items; 75% passing score; TestNow; English and Spanish. The official page is internally inconsistent about duration—it labels the duration as 60 minutes but also describes an approximately 65-minute exam plus a 2–5-minute tutorial/NDA—so confirm the appointment duration before booking.<br>
**Purchase snapshot:** no formal exam prerequisite; exam from USD 195, exam-plus-retake from USD 225, and standalone practice USD 49 when checked; prices are public listings, not checkout quotations<br>

The credential page contains unrelated roadmap copy describing a future JavaScript-oriented WDA and mislabels WDE as Associate; the certification overview also has an entry-level title label for WDA. These are not authoritative replacements for the active **WDA-41-01 HTML/CSS syllabus**. The linked PDF cover says September 15, 2025, while current HTML says September 16; only the indexed PDF cover and first two objectives were accessible. Confirm duration, delivery and voucher/retake terms against the actual product before purchase. No account, booking or checkout was entered.

## How to use this guide

WDA joins semantic HTML, maintainable CSS, responsive layout, accessibility, quality, performance, SEO, and analytics. Build one progressively enhanced site instead of isolated visual snippets. For every change, inspect the DOM, accessibility tree, computed styles, cascade, box model, grid/flex overlays, network behavior, responsive layout, and keyboard interaction.

Use this loop:

1. translate a design/content requirement into semantic HTML before styling;
2. implement a low-specificity mobile-first baseline;
3. validate and inspect the winning rules rather than guessing;
4. test content expansion, zoom, reduced motion, keyboard use, multiple viewports, and failure states;
5. measure asset/layout performance and document the tradeoff;
6. map the evidence to all 40 published objectives.

Frameworks and preprocessors are only part of one CSS objective. Know their purpose and basic workflow, but do not let memorized Bootstrap classes or Sass syntax replace standards-based CSS skills.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map and study emphasis

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| 1. HTML Fundamentals | 10 | 25% | Author standards-mode metadata, semantic content, tables, media, forms, iframes, and navigation |
| 2. CSS Fundamentals | 9 | 22.5% | Resolve the cascade and build maintainable typography, boxes, positioning, effects, framework/preprocessor use, and optimized styles |
| 3. Integrating HTML and CSS | 10 | 25% | Structure files/styles, build accessible forms/interactions, validate, and diagnose with developer tools |
| 4. Responsive Web Design and Layout Techniques | 5 | 12.5% | Deliver mobile-first Flexbox/Grid layouts across devices with performant assets and fallbacks |
| 5. Accessibility, Usability, and Best Practices | 6 | 15% | Demonstrate inclusive interaction, usability, maintainability, quality, SEO, performance, and privacy-aware analytics |

The official syllabus publishes both counts and weights. Blocks 1 and 3 together represent half of the published weight, so HTML/CSS integration and debugging deserve as much attention as CSS feature recall. The 75% requirement is a normalized cumulative score; do not turn it into an unsupported “30 equally weighted questions” rule.

## 1. HTML fundamentals — 25%

### Document structure and metadata

Start with `<!doctype html>`, one language-labelled `<html>` root, a `<head>` for metadata/resources, and a `<body>` for rendered content. Declare UTF-8 early and configure the viewport for device-width rendering. Use a unique, concise `<title>` and a useful description that accurately summarizes the page.

Social preview metadata is platform-specific. A favicon supports browser identity. Robots metadata communicates crawl/index preferences but is not an access control. Keep metadata valid, non-duplicative, and inside the head.

Well-formed source uses valid nesting, unique IDs, quoted attribute values, appropriate closing tags, and escaped reserved characters. HTML's parser may repair mistakes, but repaired output can differ from intent; validate source and inspect the DOM.

### Semantic content

Use `<main>` once for the page's primary content, `<nav>` for a major navigation collection, `<article>` for a self-contained composition, `<section>` for a thematically grouped section that normally has a heading, `<aside>` for tangential content, and header/footer for introductory or ending content at the relevant scope.

Paragraphs contain prose; ordered/unordered lists communicate sequence or collection; description lists pair names and descriptions. Use tables for data, with a caption, row groups where useful, and header cells whose `scope` expresses simple relationships. Build a logical heading hierarchy; use `<hr>` for thematic shifts and `<br>` only for meaningful line breaks.

A semantic element is not automatically a landmark. A named `section` can expose a region; an `article` is not a landmark. Header/footer roles depend on their ancestor context. Name multiple navigation regions meaningfully and distinguish them when their link sets differ. Adding ARIA never supplies missing keyboard behavior. See the [WAI landmark guidance](https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/).

### Media, embeds, forms, and navigation

Informative images require purpose-based alternative text; decorative images use empty `alt`. Intrinsic dimensions reduce layout shifts while `srcset` and `sizes` allow source selection. Audio/video need controls and equivalent content such as captions and, where the content requires it, a transcript. Figure/figcaption groups self-contained media with its caption.

Give every iframe a descriptive title and make it responsive. `sandbox`, `allow`, and `referrerpolicy` affect capability/security/privacy; grant only required capabilities.

Use native form controls with visible labels, names, stable IDs, fieldset/legend grouping, suitable types, useful autocomplete, and native constraints. GET suits safe repeatable retrieval; POST suits state-changing/body-submitted operations. Input constraints do not remove server validation requirements.

A `datalist` offers suggestions and still permits other valid input; use `select` when the user must choose an allowed option. Native suggestion presentation and assistive-technology support vary, so do not make the popup the only way to finish. `output` names a calculated result and its `for` attribute lists contributing control IDs, but its name/value are not submitted. `inputmode` is a keyboard hint, not a validation rule. A file control needs a real user selection; an `accept` hint cannot establish file safety. Date widgets vary while a valid date value uses an ISO-style date string. Native validation is bypassable, and constructing `FormData` does not run it. [MDN datalist](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist), [output](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output) and [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation) explain these boundaries.

Boolean attributes are controlled by presence: `disabled="false"` still disables. Hidden inputs are not secret; disabled controls are generally omitted from submission while eligible readonly controls remain included. Use `getAll` for repeated form names. For detailed HTML/media examples, the [WDE workbook](WDE-40-01-certified-entry-level-web-developer.md) separately exercises native GET/POST serialization and original media; those tests are not counted again as WDA execution.

Navigation links need meaningful destinations and labels, consistent structure, human-readable URLs, and correct relative/absolute references. Skip links let keyboard users bypass repeated content. If a new browsing context is justified, make that expectation clear and apply suitable `rel` protection.

The [MDN HTML learning module](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content) is a current reference for these foundations.

> **Related item:** Semantic HTML is an API shared by browsers, assistive technologies, search systems, reader modes, tests, and CSS/JavaScript. Choosing elements by meaning improves all of those consumers at once.

## 2. CSS fundamentals — 22.5%

### Syntax, selectors, values, and the cascade

A rule contains selectors and declaration blocks. Know type, class, ID, attribute, pseudo-class, and pseudo-element selectors. Use units according to the quantity: unitless line-height where appropriate, relative `rem`/`em` for scalable dimensions, percentages for context-relative values, viewport/container-related units when justified, and pixels for deliberate fixed CSS-pixel dimensions.

The cascade does more than compare specificity. It filters relevant rules, considers origin and importance (including cascade layers), then specificity, scoping proximity where applicable, and order of appearance. Inline style has high author specificity but is not universally “stronger than everything.” Inheritance supplies values for selected properties when no winning declaration sets them on the element.

Specificity broadly compares ID, class/attribute/pseudo-class, and type/pseudo-element components. Prefer low-specificity classes and predictable layers/source order. `!important` reverses some cascade ordering and should solve a defined priority requirement—not compensate for an unclear architecture.

Use a naming convention such as BEM if it helps a team, but understand the purpose: predictable ownership, reuse, and low collision. CSS custom properties store reusable values and participate in the cascade, making them useful for themes and design tokens.

See [MDN Cascade, specificity, and inheritance](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_conflicts) for the current model.

Read specificity as **three columns compared from left to right**, not decimal points: `(1,0,0)` beats `(0,11,0)`. `:where(...)` contributes zero; `:is(...)`, `:not(...)` and `:has(...)` take the most specific selector in their argument list. An ordinary comma-separated rule uses the specificity of the matching selector, so a nonmatching ID elsewhere in that list does not increase a matched class selector's weight. Inherited values are considered only after declarations on the child: a parent's important color does not defeat the child's directly declared normal color.

For normal author rules, later layers beat earlier layers and unlayered rules beat layered rules. Important declarations reverse the layer order; important rules in an earlier layer beat those in later layers and unlayered important rules. Important inline author declarations have their own higher author precedence, but user/user-agent important rules and active transitions can outrank them. Keyframe animation values beat normal declarations but lose to important declarations; active transitions outrank even important endpoints. These are precedence rules, not extra specificity points. Consult the complete [cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascade/Cascade), [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascade/Specificity) and [layer](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer) references.

Custom-property names are case-sensitive. A `var()` fallback handles a missing or guaranteed-invalid custom property, not a valid token sequence of the wrong type for its destination. If `--tone: 12px`, then `color: blue; color: var(--tone, red)` does not restore blue or choose red: the winning declaration becomes invalid at computed-value time and color inherits (or uses its initial value when appropriate). In contrast, the literal invalid declaration `color: 12px` is discarded before the cascade. `revert-layer` can reveal a lower layer; it is not the same as `initial`, `inherit` or `revert`. [Custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties) explain the distinction.

### Typography, colors, sizing, and boxes

Choose readable font families, sizes, weights, line heights, and line lengths; include appropriate fallbacks. Preserve contrast and never convey state only with color. Background, border, padding, and margin affect different layers. `box-sizing: border-box` makes declared width/height include padding and border.

Use `display`, intrinsic sizing, `min`/`max`/`clamp`, overflow, aspect ratio, and logical properties deliberately. Logical properties such as `margin-inline` adapt to writing mode. Shadows, filters, blend modes, and rounded corners are presentation; keep readability and performance ahead of decoration.

### Positioning, stacking, transitions, and animation

Static positioning follows normal flow. Relative positioning preserves the original flow space and establishes positioning context in common cases. Absolute positioning is removed from normal flow and uses a containing block. Fixed positions relative to a viewport-like containing block; sticky behaves relatively until a scroll threshold within its scrolling context.

`z-index` orders within stacking contexts, not globally across the document. Opacity, transforms, positioning, containment, and other properties can create stacking contexts. Inspect them rather than escalating arbitrary numbers.

For example, a 200px content-box width with 10px padding and 5px border on each side occupies 230px; border-box keeps the outer width at 200px. Absolute percentages commonly use the positioned ancestor's padding box. A transformed ancestor can also establish the containing block for a fixed descendant, so “fixed always means viewport” is wrong. Sticky needs an inset on the relevant axis, a scroll mechanism and available travel within its containing block. A child at `z-index:9999` cannot escape a parent context below a sibling context. Flex and Grid items can use non-auto z-index even without non-static positioning. See [containing blocks](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_display/Containing_block) and [stacking contexts](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_positioned_layout/Stacking_context).

Transitions interpolate a changed property; keyframe animations define staged changes. Favor `transform` and `opacity` for smooth effects when they fit, measure rather than assuming, and honor `prefers-reduced-motion`. `will-change` is a targeted hint that can consume resources; do not apply it broadly.

### Frameworks, preprocessors, and CSS delivery

Bootstrap supplies a grid, utilities, and components. Use its documented structure and accessibility expectations, then customize through tokens/build configuration or narrow overrides. A framework does not make content semantic or accessible automatically.

Sass and Less compile extended syntax to CSS. Understand variables, nesting, mixins/functions, partial/module organization, compilation, autoprefixing, and source maps. Avoid excessive nesting and selector generation. Modern Sass favors its module system (`@use`/`@forward`) over legacy `@import`; know the syllabus concept while using current tooling.

Sass variables are compile-time values; CSS custom properties remain in the output and can change through the browser's cascade. Configure a module's `!default` variable on its first `@use`; later attempts to reconfigure an already loaded module fail, and the module's CSS is emitted once. A source map associates generated CSS with source locations; enabling the JavaScript compiler's `sourceMap` option returns a map but does not automatically write files or a `sourceMappingURL` comment. The browser build has no filesystem importer. The example below uses an explicit in-memory importer for two original files. See [Sass modules](https://sass-lang.com/documentation/at-rules/use/), [browser compilation](https://sass-lang.com/blog/sass-in-the-browser/) and [compiler options](https://sass-lang.com/documentation/js-api/interfaces/options/).

Sass `@import` and global built-in functions have emitted deprecation warnings since Dart Sass 1.80.0; warnings are not proof of a failed build. Bootstrap 5.3's documented Sass setup still uses its ordered imports. Do not mechanically replace each of those with `@use`, and do not claim that the standalone Sass panel below compiles Bootstrap itself. Autoprefixing is a separate support-policy-dependent build step, not an automatic Sass feature. [Bootstrap Sass customization](https://getbootstrap.com/docs/5.3/customize/sass/) and the [Sass deprecation notice](https://sass-lang.com/documentation/breaking-changes/import/) support these distinctions.

Bootstrap's local button variables allow a scoped variant, while its grid supplies mobile-first breakpoint classes. Native buttons retain keyboard behavior without the framework's JavaScript; interactive components such as a collapsed navbar need their documented behavior. The framework's own [accessibility guidance](https://getbootstrap.com/docs/5.3/getting-started/accessibility/) warns that results depend on author markup and colors, and its [validation documentation](https://getbootstrap.com/docs/5.3/forms/validation/) warns that custom validation styles/tooltips are not fully exposed to assistive technology. The service example uses native constraints with associated text, rather than claiming that adding validation classes completes accessibility.

Minify production CSS, cache versioned assets, remove safely verified unused rules, and reduce blocking work. Concatenation is not universally optimal under modern HTTP; bundle according to measurement, caching, and delivery architecture. Critical-CSS inlining can improve first rendering but creates duplication and maintenance costs.

> **Related item:** CSS optimization is a system tradeoff. File count, cache reuse, compression, render blocking, HTTP version, and change frequency all affect the best packaging choice.

## 3. Integrating HTML and CSS — 25%

### Stylesheet placement, precedence, and project structure

Link external CSS in the document head. Internal `<style>` suits a prototype or page-local rule set. Inline `style` can express a truly dynamic/one-off value but raises specificity and mixes concerns. Source order matters only after higher cascade criteria tie.

Organize styles in a documented order such as reset/base, layout, components, and utilities—or use explicit cascade layers. Keep class selectors reusable, IDs unique, and `!important` rare and explained. Store assets in predictable paths; understand that a relative URL is resolved from the file containing it (CSS `url(...)` resolves from the stylesheet), not always from the page.

Separate editable source from generated output when a build exists, and do not manually patch minified/generated files. Source maps connect browser observations to source.

In the service example, `styles/service.css` is resolved from `service.html`; a hypothetical `url("../assets/bench.svg")` inside that CSS resolves from the stylesheet's directory. A path that works at a site root may break under a subdirectory. Inspect the requested URL and response type when a stylesheet silently fails; a 200 response containing an HTML error page is not a valid stylesheet.

### Forms and interactive states

Lay out forms with Grid or Flexbox and `gap`; allow controls and labels to wrap under text expansion and narrow viewports. Do not use fixed heights that clip errors. Reuse type, color, spacing, and border tokens.

Native validation comes first. A small script can coordinate custom messages or submit behavior, but do not replace a native control unnecessarily. Associate error text with the field, move focus deliberately after a failed submission when helpful, and announce a compact error summary with a live region/alert only at the right time.

Use links for navigation and buttons for actions. Design `:hover`, `:focus-visible`, `:disabled`, checked/invalid, and pressed/expanded states as appropriate. Keyboard focus must follow a logical DOM order; positive tabindex values usually create fragile ordering. Provide comfortable targets and spacing, contrast, and a reduced-motion path.

The demonstration leaves its fieldset disabled until its small script installs the local-only submit handler. Without JavaScript, the information remains readable and the estimate action is unavailable. Native invalid submission focuses a failing control; the handler exposes the field's associated error and removes it after correction. The initial implementation placed `[hidden]` in an earlier layer than `.error { display:block }`, which made corrected messages visible. Moving the hidden guard outside the layers fixed the actual browser failure. Hiding content and setting an attribute are only reliable when the final computed styles agree.

### Validation and browser developer tools

Run HTML and CSS validators to find syntax/standards problems. Linting enforces selected project rules; autoprefixing adds prefixes according to a support policy. Neither proves visual correctness or accessibility.

When a style is wrong:

1. inspect the intended element and matched rules;
2. find the computed value and winning declaration;
3. check inheritance, specificity, layer, source order, shorthand reset, and invalid declarations;
4. inspect box dimensions and layout overlays;
5. test the fix across breakpoints, states, and themes;
6. persist it in source and rerun regression checks.

Browser responsive mode is a useful simulation, not proof on every real device/browser. Performance and rendering panels can expose layout, paint, and animation cost.

## 4. Responsive web design and layout — 12.5%

### Mobile-first, fluid foundations

Set the viewport metadata, establish a usable narrow-screen baseline, and add `min-width` queries when content needs more room—not solely for named device models. Fluid tracks and sizes can use percentages, `fr`, `minmax`, `min`, `max`, and `clamp`. Flexible images use appropriate intrinsic size, `max-width`, and responsive sources.

Do not reorder content visually in a way that creates a confusing keyboard/screen-reader sequence. Avoid horizontal overflow, test long words and translated labels, and allow target spacing. Approximately 44×44 CSS pixels is a useful comfortable-target goal named in the syllabus detail; applicable accessibility criteria and exceptions still require separate evaluation.

### Flexbox and Grid

Flexbox is primarily one-dimensional: align and distribute items along main/cross axes, allow wrapping, size flexible items, and use `gap`. Grid is two-dimensional: define rows/columns, place items, use named areas, and build responsive patterns with `repeat`, `auto-fit`/`auto-fill`, and `minmax`.

Choose based on relationships rather than “newest feature.” They can be nested: Grid for page regions, Flexbox within a component. Preserve semantic source order.

Growth factors divide **positive free space**, not final widths. In a 600px row with 100px and 200px bases and growth factors 1 and 2, 300px remains: final widths are 200px and 400px. Shrink uses factors scaled by the bases: 200px/400px items with equal shrink factors in 300px become 100px/200px, assuming no padding, borders, gaps or minimum-size clamp. A default automatic minimum can stop shrinking; apply a deliberate `min-inline-size:0` and handle overflow where the content permits it. Growth factors totaling less than one can leave free space: two 100px items with `.25` growth each in 400px become 150px each. See [flex sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Controlling_ratios_of_flex_items_along_the_main_axis) and the [Flexbox specification](https://www.w3.org/TR/css-flexbox-1/).

Grid fractions share remaining space after fixed tracks and gaps. In 620px with `100px 1fr 2fr` and two 10px gaps, the fractional tracks receive approximately 166.67px and 333.33px. With two items, `repeat(auto-fit,minmax(200px,1fr))` collapses an unused third track; `auto-fill` retains it. `minmax(0,1fr)` can avoid an automatic minimum forcing a track wider than intended, but long content still needs a wrapping or scrolling policy. The [repeat reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat) distinguishes these cases.

### Compatibility and performance

Use progressive enhancement: begin with a usable core, then add supported improvements. `@supports` can conditionally apply a feature. Define a browser/device support policy, inspect compatibility data, and test representative real combinations.

Reserve image dimensions, use correctly sized compressed formats such as WebP/AVIF where supported with fallbacks as needed, lazy-load noncritical offscreen media, and defer noncritical assets. Minify production assets and use caching/resource hints only when measured. A performance budget turns “fast” into testable thresholds.

The [web.dev responsive design course](https://web.dev/learn/design/) and [MDN CSS layout module](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout) provide standards-oriented practice.

> **Related item:** Container queries respond to the space available to a component rather than the viewport. They are valuable current CSS context, but the published WDA objective explicitly names media queries, so master those first.

## 5. Accessibility, usability, and best practices — 15%

### Accessible and usable experiences

Provide alternatives for non-text content, captions/transcripts, semantic landmarks/headings, keyboard access, visible focus, meaningful focus order, skip links, sufficient contrast, named controls, clear errors, and reduced-motion handling. Do not hide focused or essential content from the accessibility tree.

Usability asks whether intended people can complete intended tasks effectively. Use descriptive labels, consistent navigation, breadcrumbs where they aid location, readable typography, scannable hierarchy, and clear loading/success/empty/error feedback. Observe a few representative users or conduct a structured review, record friction, and retest after changes.

The current normative accessibility reference is [WCAG 2.2](https://www.w3.org/TR/WCAG22/), and the [W3C WAI tutorials](https://www.w3.org/WAI/tutorials/) translate common page patterns into implementation guidance.

### Maintainability and quality assurance

Separate HTML structure, CSS presentation, and JavaScript behavior conceptually and in project organization while allowing pragmatic component co-location. Use reusable components, custom-property tokens, a documented naming approach, predictable paths, version control, and focused changes.

Validate source; test keyboards, zoom/reflow, contrast, a screen reader, internationalized content, print output, supported browsers/devices, and failure states. Measure the current Core Web Vitals—Largest Contentful Paint, Cumulative Layout Shift, and Interaction to Next Paint—using lab and field evidence where available. [web.dev Web Vitals](https://web.dev/articles/vitals) is the current source for definitions and thresholds.

Use the **75th percentile of real page experiences**, segmented by mobile and desktop, for the good thresholds: LCP at most 2.5 seconds, INP at most 200 milliseconds and CLS at most 0.1. All three matter. CLS is the largest session-window sum of unexpected shifts, not the sum of every shift for an entire visit; windows use gaps below one second and a maximum duration below five seconds. INP concerns click/tap/keyboard interactions through the visit and includes input delay, processing and presentation delay. A load-only Lighthouse run cannot establish INP; TBT is a proxy, not the same metric.

The original `quality.js` uses a stated nearest-rank percentile for synthetic arrays and implements only shift-window arithmetic. `measure.html` collects raw local entries and deliberately demonstrates one slow interaction. Neither handles the complete field metric lifecycle, iframe aggregation, back/forward-cache resets or representative user sampling. A raw LCP candidate or Event Timing entry is not automatically a complete metric. Read the selected [LCP](https://web.dev/articles/lcp), [CLS](https://web.dev/articles/cls) and [INP](https://web.dev/articles/inp) measurement guidance before choosing a production collector. Source byte counts are not compressed transfer sizes or proof of user-perceived speed.

### SEO and analytics

SEO basics include accurate unique titles/descriptions, semantic headings/content, crawlable descriptive links, useful image alternatives, canonical URL signaling, sitemaps, robots directives, structured data, mobile usability, and performance. A robots rule is not security, a canonical link is a signal rather than authorization, and structured data must match visible content.

Google may generate a title link or snippet from content other than the supplied title or description. Canonicalization helps consolidate duplicate URLs; it does not guarantee which URL a search engine chooses. A crawler must be allowed to fetch a page to read its `noindex` instruction: disallowing that URL in robots.txt can prevent discovery of the instruction. Metadata cannot replace authentication for private content. The [SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) and [robots directives](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) describe these limits.

Analytics begins with a decision and a measurable KPI. Define consistently named events and parameters for meaningful actions—not every possible click. Campaign UTM conventions support attribution. Segment by dimensions only when they answer a question and sample sizes are responsible.

For example, count a successfully completed estimate, not just a submit-button click that might fail validation. Keep event names stable and use a broad participant band only if that answers the question; do not copy a visitor's topic/date/free text into the event. The example's opt-in count is held only in tab memory and is cleared when disabled. It does not load Google Analytics, send a beacon, set consent cookies or prove legal compliance. A real implementation additionally needs transport/deduplication, applicable policy and access/retention decisions. The [Analytics event guide](https://developers.google.com/analytics/devguides/collection/ga4/events) distinguishes automatically collected, enhanced, recommended and custom events and provides separate verification tools.

Collect the least data needed, disclose use, obtain consent where required, restrict access/retention, and avoid sending sensitive data in URLs or analytics parameters. Privacy and consent rules vary by jurisdiction and change; follow current organizational and legal guidance rather than treating an exam summary as compliance advice.

> **Related item:** A technically valid tracking implementation can still be ethically or legally inappropriate. Data minimization and purpose limitation should be design inputs, not cleanup tasks.

## Executed browser workbook

The exact examples below passed **42 CSS fixture checks and 90 additional harness checks** in existing Chrome 154.0.8037.58 on September 29, 2026. Five complete HTML files returned zero W3C Nu messages. `baseline.css` and `styles/service.css` passed the W3C CSS3 validator with zero errors and warnings through its SOAP response; initial JSON POST attempts returned HTTP500 and are retained in the evidence. These are actual execution results, not a claim of full browser/device, assistive-technology or WCAG coverage.

Save the JSON operation record linked by the [review report](../docs/research/2026-09-29-wda-41-01-deep-review.md) as `wda-review.json`, then run this standard-library extractor. It verifies all fourteen original assets before creating a new `wda-workshop` directory. The record preserves source hashes, the original harnesses, compiler provenance and receipts. Vendor library bytes are not embedded in the original asset archive.

```python
from pathlib import Path
import base64, hashlib, json

record = json.loads(Path("wda-review.json").read_text(encoding="utf-8"))
names = ("workbook.html", "workbook.js", "service.html", "styles/service.css",
         "service.js", "assets/bench.svg", "framework.html", "_tokens.scss",
         "panel.scss", "compile-sass.js", "sass.html", "quality.js", "measure.html", "baseline.css")
assets = {}
for name in names:
    data = base64.b64decode(record["original_assets_base64"][name], validate=True)
    if hashlib.sha256(data).hexdigest() != record["browser_execution_receipt"]["source_sha256"][name]:
        raise ValueError("Asset hash mismatch: " + name)
    assets[name] = data
destination = Path("wda-workshop")
destination.mkdir()  # Refuse to overwrite an existing destination.
for name, data in assets.items():
    target = destination / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
print("Prepared", len(assets), "original files in", destination)
```

Use an existing local development setup to serve the files over HTTP. The review instead used isolated intercepted HTTPS requests, without a persistent server or package installation. Opening a file URL is not equivalent to that environment, especially for module and fetch behavior. `framework.html` requests the pinned Bootstrap CSS; `sass.html` loads the pinned compiler and dependency when its button is activated. Network/CDN failure remains possible.

### Cascade and geometry

Run `workbook.html`. The visible button repeats the same original fixtures that the harness invoked. Each fixture records observed/expected values, and a failure stops the run. Geometry examples intentionally remove padding, borders and minimum-size effects unless the check is about those effects. The temporary frame is always removed.

**`workbook.html`**

```html
<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>WDA cascade and layout workbook</title></head>
<body><main><h1>Cascade and layout workbook</h1>
<p>Run original fixtures in a disposable frame. Results describe this browser, not every browser.</p>
<button id="run" type="button">Run workbook</button><pre id="report" role="status"></pre></main>
<script src="workbook.js"></script>
<script>
document.querySelector('#run').addEventListener('click', async event => {
  event.target.disabled = true;
  try { document.querySelector('#report').textContent = JSON.stringify(await wdaWorkbook(), null, 2); }
  catch (error) { document.querySelector('#report').textContent = error.message; }
  finally { event.target.disabled = false; }
});
</script></body></html>
```

**`workbook.js`**

```javascript
"use strict";
async function wdaWorkbook() {
  const frame = document.createElement('iframe');
  frame.title = 'Disposable original CSS fixtures';
  frame.style.cssText = 'width:700px;height:400px;border:0;display:block';
  document.body.append(frame);
  const d = frame.contentDocument, w = frame.contentWindow, results = [];
  const q = selector => d.querySelector(selector);
  const css = (selector, property) => w.getComputedStyle(q(selector)).getPropertyValue(property);
  const width = selector => q(selector).getBoundingClientRect().width;
  const check = (name, actual, expected, tolerance = 0) => {
    const passed = typeof expected === 'number' ? Math.abs(actual - expected) <= tolerance : actual === expected;
    results.push({name, actual, expected, passed});
    if (!passed) throw new Error(JSON.stringify(results.at(-1)));
  };
  const fixture = (rules, markup = '<div id="x" class="x">Sample</div>') => {
    d.head.innerHTML = '<style>html,body{margin:0}*{box-sizing:content-box}</style>';
    const style = d.createElement('style'); style.textContent = rules; d.head.append(style);
    d.body.innerHTML = markup; // Only the fixed, original fixture strings below.
  };
  const tick = () => new Promise(resolve => w.requestAnimationFrame(() => w.requestAnimationFrame(resolve)));
  try {
    fixture('#x{color:red}.a.b.c.d.e.f.g.h.i.j.k{color:blue}', '<div id="x" class="a b c d e f g h i j k">Columns</div>');
    check('one ID beats eleven classes', css('#x','color'), 'rgb(255, 0, 0)');
    fixture(':where(#x){color:red}.x{color:blue}');
    check('where contributes zero', css('#x','color'), 'rgb(0, 0, 255)');
    fixture(':is(#absent,.x){color:red}.x{color:blue}');
    check('is takes maximum argument specificity', css('#x','color'), 'rgb(255, 0, 0)');
    fixture('#absent,.x{color:red}.x{color:blue}');
    check('ordinary list uses matching selector weight', css('#x','color'), 'rgb(0, 0, 255)');
    fixture('@layer base,theme;@layer base{#x{color:red}}@layer theme{.x{color:blue}}');
    check('later normal layer beats earlier ID', css('#x','color'), 'rgb(0, 0, 255)');
    fixture('@layer base{#x{color:red}}.x{color:blue}');
    check('unlayered normal wins', css('#x','color'), 'rgb(0, 0, 255)');
    fixture('@layer base,theme;@layer base{.x{color:red!important}}@layer theme{#x{color:blue!important}}#x{color:green!important}');
    check('important layer order reverses', css('#x','color'), 'rgb(255, 0, 0)');
    q('#x').style.setProperty('color','purple','important');
    check('important inline beats author important layers', css('#x','color'), 'rgb(128, 0, 128)');
    fixture('body{color:red!important}.x{color:blue}');
    check('direct declaration beats inherited important', css('#x','color'), 'rgb(0, 0, 255)');
    fixture('body{color:green}.x{color:blue;color:12px}');
    check('invalid literal declaration discarded', css('#x','color'), 'rgb(0, 0, 255)');
    fixture('body{color:green}.x{--tone:12px;color:blue;color:var(--tone,red)}');
    check('invalid computed value inherits; fallback is not type validation', css('#x','color'), 'rgb(0, 128, 0)');
    fixture('.x{--Tone:red;color:var(--tone,blue)}');
    check('custom property names are case sensitive', css('#x','color'), 'rgb(0, 0, 255)');
    fixture('@layer base,theme;@layer base{.x{color:red}}@layer theme{.x{color:blue;color:revert-layer}}');
    check('revert-layer reveals earlier layer', css('#x','color'), 'rgb(255, 0, 0)');
    fixture('.x{width:200px;padding:10px;border:5px solid}');
    check('content-box outer width', width('#x'), 230, .01);
    q('#x').style.boxSizing = 'border-box';
    check('border-box outer width', width('#x'), 200, .01);
    fixture('.x{width:100px;height:20px;position:relative;left:30px}.next{height:10px}', '<div id="x" class="x"></div><div class="next"></div>');
    check('relative moves painted box', q('#x').getBoundingClientRect().left, 30, .01);
    check('relative preserves flow space', q('.next').getBoundingClientRect().top, 20, .01);
    fixture('.parent{position:relative;margin:40px;padding:20px;width:200px;height:100px}.x{position:absolute;left:0;top:0;width:50%;height:10px}', '<div class="parent"><div id="x" class="x"></div></div>');
    check('absolute percentage uses padding-box width', width('#x'), 120, .01);
    check('absolute begins at positioned padding edge', q('#x').getBoundingClientRect().left, 40, .01);
    fixture('.parent{margin:40px;transform:translateX(0);height:80px}.x{position:fixed;top:0;left:0}', '<div class="parent"><div id="x" class="x">Fixed</div></div>');
    check('transform establishes fixed containing block', q('#x').getBoundingClientRect().left, 40, .01);
    q('.parent').style.transform = 'none';
    check('fixed returns to viewport without transform', q('#x').getBoundingClientRect().left, 0, .01);
    fixture('.scroll{height:100px;overflow:auto}.x{position:sticky;top:0;height:20px}.filler{height:300px}', '<div class="scroll"><div id="x" class="x">Sticky</div><div class="filler"></div></div>');
    q('.scroll').scrollTop = 80; await tick();
    check('sticky respects scrollport inset', q('#x').getBoundingClientRect().top, 0, .01);
    fixture('.back,.front{position:absolute;inset:0;width:100px;height:100px}.back{z-index:1}.front{z-index:2}.x{position:absolute;inset:0;z-index:9999}', '<div class="back"><div id="x" class="x">Nested</div></div><div class="front">Front</div>');
    check('nested high z-index stays in parent context', d.elementFromPoint(50,50).className, 'front');
    fixture('.row{display:flex}.x,.other{width:100px;height:100px}.x{z-index:2}.other{margin-left:-50px;background:red}', '<div class="row"><div id="x" class="x">Static flex</div><div class="other"></div></div>');
    check('static flex item accepts z-index', d.elementFromPoint(75,50).id, 'x');
    fixture('.row{display:flex;width:600px}.a{flex:1 1 100px}.b{flex:2 1 200px}.row>*{min-width:0}', '<div class="row"><div class="a"></div><div class="b"></div></div>');
    check('growth A uses share of free space', width('.a'), 200, .02);
    check('growth B includes its base', width('.b'), 400, .02);
    fixture('.row{display:flex;width:300px}.a{flex:0 1 200px}.b{flex:0 1 400px}.row>*{min-width:0}', '<div class="row"><div class="a"></div><div class="b"></div></div>');
    check('shrink A scaled by base', width('.a'), 100, .02);
    check('shrink B scaled by base', width('.b'), 200, .02);
    fixture('.row{display:flex;width:400px}.row>*{flex:.25 0 100px;min-width:0}', '<div class="row"><div class="a"></div><div class="b"></div></div>');
    check('grow sum below one leaves space A', width('.a'), 150, .02);
    check('grow sum below one leaves space B', width('.b'), 150, .02);
    fixture('.row{display:flex;width:150px}.x{flex:1 1 0;font:16px monospace;white-space:nowrap}', '<div class="row"><div id="x" class="x">ABCDEFGHIJKLMNOPQRSTUVWXYZ</div></div>');
    check('automatic minimum can overflow flex container', width('#x') > 150, true);
    q('#x').style.minWidth = '0';
    check('explicit zero minimum permits shrink', width('#x'), 150, .02);
    fixture('.grid{display:grid;width:620px;gap:10px;grid-template-columns:100px 1fr 2fr}', '<div class="grid"><div class="a"></div><div class="b"></div><div class="c"></div></div>');
    check('grid fixed track', width('.a'), 100, .02);
    check('grid first fraction after fixed and gaps', width('.b'), 500/3, .03);
    check('grid second fraction after fixed and gaps', width('.c'), 1000/3, .03);
    fixture('.grid{display:grid;width:620px;gap:10px;grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}', '<div class="grid"><div class="a"></div><div class="b"></div></div>');
    check('auto-fit collapses unused third track', width('.a'), 305, .02);
    q('.grid').style.gridTemplateColumns = 'repeat(auto-fill,minmax(200px,1fr))';
    check('auto-fill retains empty third track', width('.a'), 200, .02);
    fixture('.x{margin-inline-start:25px;width:100px}', '<div dir="rtl"><div id="x" class="x"></div></div>');
    check('logical start maps to right in horizontal RTL', css('#x','margin-right'), '25px');
    fixture('.x{display:block}@supports(display:grid){.x{display:grid}}');
    check('feature query selects supported enhancement', css('#x','display'), 'grid');
    fixture('@keyframes shade{from{opacity:0}to{opacity:1}}.x{animation:shade 1s linear both paused}');
    await tick(); q('#x').getAnimations()[0].currentTime = 500;
    check('paused keyframe midpoint', Number(css('#x','opacity')), .5, .01);
    q('#x').style.setProperty('opacity','.8','important');
    check('important declaration beats keyframe', Number(css('#x','opacity')), .8, .01);
    fixture('.x{opacity:0!important;transition:opacity 1s linear}');
    await tick(); q('#x').style.setProperty('opacity','1','important'); await tick();
    const transition = q('#x').getAnimations()[0]; transition.pause(); transition.currentTime = 500;
    check('active transition outranks important endpoint', Number(css('#x','opacity')), .5, .02);
    return {passed:results.length, checks:results};
  } finally {frame.remove();}
}
```

## Integrated scenarios

### Scenario 1: Responsive service site

This original page combines semantic regions, cards, a simple table, a labelled form, optional datalist suggestions, calculated output and a native disclosure. The form never books a visit; its scripted submission produces a local estimate. The service script does not send form values or analytics events. Tests covered invalid/corrected values, serialization, keyboard navigation, reduced motion, print, RTL, 320/375/768/1280px widths and doubled root font at 320px. Root-font doubling is not an actual browser-zoom test. Screen-reader announcements and real devices remain to be reviewed.

**`service.html`**

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Repair workshop — local WDA demonstration</title>
  <meta name="description" content="Plan a practice repair workshop and compare accessible responsive layouts.">
  <meta name="robots" content="noindex">
  <link rel="stylesheet" href="styles/service.css"><script src="service.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
<header class="wrap"><p>Community workshop practice</p><nav aria-label="Main"><a href="#sessions">Sessions</a> <a href="#plan">Plan a visit</a></nav></header>
<main id="main" tabindex="-1" class="wrap">
  <h1>Repair together</h1><p>This original local demo makes an estimate. It does not book or send anything.</p>
  <figure><img src="assets/bench.svg" width="640" height="240" alt="Two work surfaces with space between them"><figcaption>A simple layout sketch; the written session details remain available.</figcaption></figure>
  <section id="sessions" aria-labelledby="sessions-title"><h2 id="sessions-title">Practice sessions</h2>
    <div class="cards"><article class="card"><h3>Small repairs</h3><p>Bring a question and compare possible approaches.</p><a href="#plan">Plan small repairs</a></article>
    <article class="card"><h3>Tool introduction</h3><p>Discuss tool choices with a facilitator. This is demonstration content.</p><a href="#plan">Plan a tool introduction</a></article></div>
    <table><caption>Original sample schedule</caption><thead><tr><th scope="col">Session</th><th scope="col">Duration</th></tr></thead><tbody><tr><th scope="row">Small repairs</th><td>45 minutes</td></tr><tr><th scope="row">Tool introduction</th><td>30 minutes</td></tr></tbody></table>
  </section>
  <section id="plan" aria-labelledby="plan-title"><h2 id="plan-title">Estimate a visit</h2>
    <p id="form-help">Topic, date and participant count are required. All work stays on this page.</p>
    <form id="visit" action="#plan" method="get" aria-describedby="form-help">
      <fieldset id="fields" disabled><legend>Visit details</legend><div class="form-grid">
        <div><label for="topic">Topic</label><input id="topic" name="topic" list="topics" required aria-describedby="topic-error"><datalist id="topics"><option value="Small repairs"></option><option value="Tool introduction"></option></datalist><span class="error" id="topic-error" hidden>Enter a topic; suggestions are optional.</span></div>
        <div><label for="date">Preferred date</label><input id="date" name="date" type="date" required aria-describedby="date-error"><span class="error" id="date-error" hidden>Choose a valid date.</span></div>
        <div><label for="people">Participants (1–6)</label><input id="people" name="people" type="number" inputmode="numeric" min="1" max="6" step="1" value="1" required aria-describedby="people-error"><span class="error" id="people-error" hidden>Use a whole number from 1 through 6.</span></div>
        <div><label for="estimate">Estimated materials, sample units</label><output id="estimate" name="estimate" for="people">3</output></div>
      </div>
      <button type="submit">Review estimate</button></fieldset><p id="result" role="status"></p>
    </form>
    <noscript><p>Enable scripting to calculate this local estimate. The session information above is available without it.</p></noscript>
    <details><summary>What happens to the information?</summary><p>The scripted demo sends no requests. A real service requires server validation and an appropriate data policy.</p></details>
    <label class="opt-in"><input id="collect" type="checkbox"> Keep a local count of completed estimates in this tab</label>
    <p id="counter" role="status">Local counting is off.</p>
  </section>
</main><footer class="wrap"><p>Original WDA exercise. No real organization or booking service.</p></footer>
</body></html>
```

**`styles/service.css`**

```css
@layer reset, base, components;
@layer reset {
  *, *::before, *::after { box-sizing: border-box; }
  body { margin: 0; }
}
@layer base {
  :root { --ink: #142535; --paper: #fff; --accent: #174f75; --space: 1rem; }
  body { color: var(--ink); background: var(--paper); font: 1rem/1.6 system-ui, sans-serif; }
  .wrap { max-inline-size: 65rem; margin-inline: auto; padding: var(--space); }
  h1 { font-size: clamp(2rem, 6vw, 3.5rem); line-height: 1.1; }
  a { color: var(--accent); text-underline-offset: .2em; }
  :focus-visible { outline: 3px solid #174f75; outline-offset: 4px; }
  img { display: block; max-inline-size: 100%; block-size: auto; }
  figure { margin-inline: 0; }
  table { border-collapse: collapse; inline-size: 100%; margin-block: 1rem; }
  th, td { border: 1px solid #667; padding: .4rem; text-align: start; overflow-wrap: anywhere; }
  label { display: block; }
  fieldset { min-inline-size: 0; margin: 0; border: 0; padding: 0; }
  input, button { font: inherit; }
  input:not([type="checkbox"]) { inline-size: 100%; min-inline-size: 0; padding: .5rem; border: 1px solid #667; }
  button { background: var(--accent); color: white; border: 2px solid var(--accent); padding: .6rem 1rem; cursor: pointer; }
  button:hover { background: #10344d; }
  button:disabled { cursor: default; opacity: .65; }
  output { display: block; padding: .5rem; }
}
@layer components {
  .skip { position: absolute; inset-inline-start: 1rem; top: -10rem; background: white; padding: .5rem; z-index: 2; }
  .skip:focus { top: 1rem; }
  nav { display: flex; flex-wrap: wrap; gap: 1rem; }
  .cards { display: flex; flex-wrap: wrap; gap: 1rem; }
  .card { flex: 1 1 18rem; min-inline-size: 0; border: 1px solid #667; padding: 1rem; overflow-wrap: anywhere; transition: box-shadow .2s ease; }
  .card:hover { box-shadow: 0 0 .5rem #789; }
  .form-grid { display: block; }
  .form-grid > div { margin-block-end: 1rem; min-inline-size: 0; }
  @supports (display: grid) { .form-grid { display: grid; gap: 1rem; grid-template-columns: minmax(0,1fr); } }
  .error { display: block; color: #922; font-weight: 600; }
  .opt-in { margin-block-start: 1rem; }
  @media (min-width: 42rem) { .form-grid { grid-template-columns: repeat(2,minmax(0,1fr)); } }
  @media (prefers-reduced-motion: reduce) { .card { transition: none; } }
  @media print { nav, .skip, .opt-in, #counter { display: none; } .wrap { max-inline-size: none; } }
}
[hidden] { display: none; } /* Unlayered guard wins over the component display rule. */
```

**`service.js`**

```javascript
"use strict";
const visit = document.querySelector('#visit');
const people = document.querySelector('#people');
const estimate = document.querySelector('#estimate');
const collect = document.querySelector('#collect');
const events = []; // This tab's memory only. No analytics provider or network transport.
const controls = [...visit.querySelectorAll('input')];
function updateEstimate() {
  estimate.value = people.validity.valid ? String(people.valueAsNumber * 3) : 'Enter 1–6 whole participants';
}
for (const input of controls) {
  const error = document.querySelector('#' + input.id + '-error');
  input.addEventListener('invalid', () => {input.setAttribute('aria-invalid','true'); error.hidden = false;});
  input.addEventListener('input', () => {
    if (input.validity.valid) {input.removeAttribute('aria-invalid'); error.hidden = true;}
  });
}
people.addEventListener('input', updateEstimate);
visit.addEventListener('submit', event => {
  event.preventDefault();
  document.querySelector('#result').textContent = `Local estimate: ${estimate.value} sample units. Nothing was sent.`;
  if (collect.checked) events.push({name:'estimate_completed', participantBand:people.valueAsNumber <= 3 ? '1–3' : '4–6'});
  document.querySelector('#counter').textContent = collect.checked ? `Local completed estimates: ${events.length}` : 'Local counting is off.';
});
collect.addEventListener('change', () => {
  if (!collect.checked) events.length = 0;
  document.querySelector('#counter').textContent = collect.checked ? 'Local completed estimates: 0' : 'Local counting is off.';
});
updateEstimate();
document.querySelector('#fields').disabled = false;
```

**`assets/bench.svg`**

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="640" height="240" viewBox="0 0 640 240"><rect width="640" height="240" fill="#eff5f8"/><g fill="#174f75"><rect x="30" y="60" width="230" height="100" rx="12"/><rect x="380" y="60" width="230" height="100" rx="12"/></g><path d="M320 40v160" stroke="#667" stroke-width="4" stroke-dasharray="8 8"/></svg>
```

### Scenario 2: Framework and preprocessor comparison

`framework.html` compares original native buttons using small author rules and Bootstrap variables. The actual pinned 5.3.8 stylesheet was fetched, its official SHA-384 SRI matched, and the browser rendered it. Tests inspected base/hover/focus/disabled states, reduced motion and the 768px grid breakpoint. Bootstrap's 232,111 downloaded CSS bytes are the uncompressed file length, not a measured production transfer budget; a larger library buys more than this single component. See the [Bootstrap introduction](https://getbootstrap.com/docs/5.3/getting-started/introduction/), [grid](https://getbootstrap.com/docs/5.3/layout/grid/) and [buttons](https://getbootstrap.com/docs/5.3/components/buttons/).

**`framework.html`**

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>WDA framework comparison</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
<style>
.btn-workshop { --bs-btn-color:#fff; --bs-btn-bg:#174f75; --bs-btn-border-color:#174f75; --bs-btn-hover-color:#fff; --bs-btn-hover-bg:#10344d; --bs-btn-hover-border-color:#10344d; --bs-btn-active-color:#fff; --bs-btn-active-bg:#10344d; --bs-btn-active-border-color:#10344d; --bs-btn-disabled-color:#fff; --bs-btn-disabled-bg:#174f75; --bs-btn-disabled-border-color:#174f75; }
.btn-workshop:focus-visible { outline:3px solid #174f75; outline-offset:4px; box-shadow:none; }
.plain-button { background:#174f75; color:white; border:1px solid #174f75; border-radius:.375rem; font:inherit; padding:.375rem .75rem; }
.plain-button:hover { background:#10344d; }
.plain-button:focus-visible { outline:3px solid #174f75; outline-offset:4px; }
.plain-button:disabled { opacity:.65; }
</style></head><body><main class="container py-4"><h1>Compare native action buttons</h1>
<div class="row g-3"><section class="col-12 col-md-6"><h2>Small custom rule set</h2><button id="plain" class="plain-button" type="button">Plain action</button></section>
<section class="col-12 col-md-6"><h2>Bootstrap variables</h2><button id="framework" class="btn btn-workshop" type="button">Framework action</button></section></div>
<p class="mt-4">Both retain native button semantics. This page needs no framework JavaScript.</p>
<button id="disabled" class="btn btn-workshop" type="button" disabled>Unavailable action</button>
</main></body></html>
```

The original Sass module compiles independently. Actual Dart Sass 1.105.0 in the browser produced 16px panel padding at a 16px root, 8px nested spacing, a source map containing both original sources and a smaller compressed result with the same tested padding. Reusing the module emits its CSS once; reconfiguring it after first load throws. These versions are observed review tools, not exam version requirements. The official playground and documented JSPM route were inaccessible here; the genuine pinned npm browser build from jsDelivr and its Immutable dependency were fetched and served in the isolated browser. Their URLs, byte lengths and hashes are recorded. No Sass/Less installation, Bootstrap source build, autoprefixer or production bundler was executed.

**`_tokens.scss`**

```scss
$gap: .75rem !default;
$ink: #174f75 !default;
@function rhythm($steps) { @return $gap * $steps; }
@mixin panel { padding: rhythm(2); border: 2px solid $ink; }
.module-marker { --loaded: once; }
```

**`panel.scss`**

```scss
@use "tokens" with ($gap: .5rem);
.sass-panel {
  @include tokens.panel;
  color: tokens.$ink;
  & > strong { display: block; margin-block-end: tokens.rhythm(1); }
}
```

**`compile-sass.js`**

```javascript
async function compileOriginalSass(sass, files, style = 'expanded') {
  const importer = {
    canonicalize(url) {
      return ['tokens','memory:tokens'].includes(url) ? new URL('memory:tokens') : null;
    },
    load(url) {
      return url.href === 'memory:tokens' ? {contents:files.tokens, syntax:'scss', sourceMapUrl:url} : null;
    }
  };
  return sass.compileString(files.panel, {
    url:new URL('memory:panel.scss'), importers:[importer], style,
    sourceMap:true, sourceMapIncludeSources:true
  });
}
```

**`sass.html`**

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Original Sass compilation</title></head><body><main><h1>Compile the original panel</h1>
<p>This demonstration loads a pinned Sass browser module from jsDelivr when requested. No local package installation is needed.</p>
<button id="compile" type="button">Compile original Sass</button><p id="status" role="status"></p>
<div class="sass-panel"><strong>Workshop panel</strong>Inspect padding, border and nested strong element.</div><pre id="css"></pre>
</main><script src="compile-sass.js"></script><script type="module">
document.querySelector('#compile').addEventListener('click', async event => {
  event.target.disabled = true;
  try {
    const sass = await import('https://cdn.jsdelivr.net/npm/sass@1.105.0/+esm');
    const read = async path => {const response = await fetch(path); if (!response.ok) throw new Error(path); return response.text();};
    const files = {tokens:await read('_tokens.scss'), panel:await read('panel.scss')};
    const result = await compileOriginalSass(sass, files);
    const style = document.createElement('style'); style.textContent = result.css; document.head.append(style);
    document.querySelector('#css').textContent = result.css;
    document.querySelector('#status').textContent = 'Compiled in this browser. Source map sources: ' + result.sourceMap.sources.join(', ');
  } catch (error) {document.querySelector('#status').textContent = 'Compilation unavailable: ' + error.message;}
  finally {event.target.disabled = false;}
});
</script></body></html>
```

### Scenario 3: Quality and measurement release

For synthetic samples `[1900,2100,2500,4000]` milliseconds, nearest-rank p75 selects 2500, rather than taking an average. The tests cover inclusive thresholds, malformed samples, input preservation and shift-window boundaries. The arrays below are authored exercises, not user data. An observed good synthetic result does not certify the site.

**`quality.js`**

```javascript
"use strict";
// Original synthetic-data exercise, not a field collector or a complete Web Vitals implementation.
function nearestRank75(values) {
  if (!Array.isArray(values) || !values.length || values.some(x => !Number.isFinite(x) || x < 0)) {
    throw new TypeError('Expected nonempty, finite, nonnegative samples');
  }
  return [...values].sort((a,b) => a-b)[Math.ceil(.75 * values.length)-1];
}
function assessSamples(samples) {
  const limits = {lcp:2500, inp:200, cls:.1}; // Milliseconds for LCP/INP; CLS is unitless.
  return Object.fromEntries(Object.entries(limits).map(([metric,limit]) => {
    const p75 = nearestRank75(samples[metric]); return [metric,{p75,good:p75 <= limit}];
  }));
}
// Caller supplies already-excluded unexpected shifts. This is only the session-window arithmetic.
function largestShiftWindow(shifts) {
  if (!Array.isArray(shifts)) throw new TypeError('Expected ordered shift samples');
  let start = 0, previous = -Infinity, total = 0, largest = 0;
  for (const {time,value} of shifts) {
    if (!Number.isFinite(time) || time < 0 || time < previous || !Number.isFinite(value) || value < 0) {
      throw new TypeError('Expected ordered, finite, nonnegative samples');
    }
    if (time - previous >= 1000 || time - start >= 5000) {start = time; total = 0;}
    total += value; largest = Math.max(largest,total); previous = time;
  }
  return largest;
}
```

The harness opened `measure.html`, waited beyond the recent-input exclusion window, inserted 80px of space above existing text and clicked the deliberately slow button. It observed a raw LCP candidate, an unexpected layout-shift entry and a slow interaction entry. Their values are retained as observations, with no field percentile or complete INP claim. The fixture sends no telemetry. Remove the intentional busy loop from any real application.

**`measure.html`**

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bounded local performance observations</title><script src="quality.js"></script>
<script>
window.localObservations = {lcpCandidates:[], shifts:[], events:[], supported:PerformanceObserver.supportedEntryTypes};
for (const [type,key] of [['largest-contentful-paint','lcpCandidates'],['layout-shift','shifts'],['event','events']]) {
  if (localObservations.supported.includes(type)) {
    const observer = new PerformanceObserver(list => {
      for (const entry of list.getEntries()) {
        const row = {name:entry.name,startTime:entry.startTime,duration:entry.duration};
        if (type==='layout-shift') {row.value=entry.value;row.hadRecentInput=entry.hadRecentInput;}
        if (type==='event') row.interactionId=entry.interactionId;
        localObservations[key].push(row);
      }
    });
    observer.observe(type==='event' ? {type,buffered:true,durationThreshold:16} : {type,buffered:true});
  }
}
</script></head><body><main>
<h1>Observe a local rendering change</h1>
<p>These raw browser entries are a bounded laboratory demonstration. They are not a complete LCP, CLS or INP field measurement.</p>
<div id="space"></div><p id="moving">This text can move when space is inserted above it.</p>
<button id="delay" type="button">Demonstrate an 80 ms synchronous task</button>
<pre id="sample"></pre>
</main><script>
document.querySelector('#sample').textContent = JSON.stringify(assessSamples({lcp:[1900,2100,2500,4000],inp:[100,150,200,300],cls:[0,.02,.1,.5]}),null,2);
document.querySelector('#delay').addEventListener('click', () => {
  const until = performance.now()+80; while (performance.now()<until) { /* Deliberately poor responsiveness, only for this exercise. */ }
});
</script></body></html>
```

This small separate baseline stylesheet provides a simple validator comparison. A successful syntax/profile check cannot establish visual correctness or accessibility, and validator implementations can lag newer CSS. The modern service stylesheet was also checked successfully on the review date.

**`baseline.css`**

```css
body { color: #142535; background-color: #fff; font-family: sans-serif; }
.card { border: 1px solid #667; padding: 16px; margin: 16px; }
a { color: #174f75; text-decoration: underline; }
```

## Hands-on labs

These ten broader learner activities remain **proposed**. The bounded examples above execute selected behaviors; they do not complete the full labs, production pipeline, real-device matrix or human usability review.

1. **Semantic foundation:** build metadata, landmarks, headings, lists, tables, media, iframes, forms, and navigation; validate and inspect the DOM/accessibility tree.
2. **Cascade workbook:** create origin/layer/source-order/specificity/inheritance conflicts, predict winners, inspect computed styles, and refactor to low-specificity classes and tokens.
3. **Box and positioning lab:** trace box dimensions, overflow, aspect ratio, logical properties, all five positioning schemes, containing blocks, and stacking contexts.
4. **Motion and effects lab:** implement transitions, transforms, keyframes, filters/shadows, and reduced-motion behavior; compare rendering performance and avoid broad `will-change`.
5. **Framework/preprocessor pipeline:** build a Bootstrap component and a Sass/Less component, compile with source maps/autoprefixing, minify, and document customization and payload tradeoffs.
6. **Form integration:** create a responsive Grid/Flex form with native constraints and a small validation script; test keyboard order, focus-visible, errors, live announcements, zoom, and long content.
7. **Responsive layout matrix:** implement equivalent Flexbox/Grid patterns, mobile-first queries, flexible sources, `@supports` fallback, and device tests; prevent overflow/layout shift.
8. **Performance budget:** record bounded load/interaction lab observations and any available real-user LCP/CLS/INP evidence, image/CSS/network costs, then optimize and explain each measured result rather than relying only on a score.
9. **Accessibility/usability review:** combine validator, automated scan, keyboard, zoom/reflow, contrast, screen reader, reduced motion, and a lightweight task observation; record and retest defects.
10. **SEO/analytics/privacy plan:** implement title/description/canonical/robots/sitemap/structured-data basics, define two KPIs/events and UTM rules, and document consent, minimization, access, and retention decisions.

## Original readiness checks

1. Which metadata is essential to a responsive standards-mode page?
2. Why is robots metadata not a security control?
3. When should section and article be selected?
4. What makes a table accessible at this level?
5. How do width/height and `srcset` solve different image problems?
6. What should an iframe security review decide?
7. Which responsibilities remain on the server after native form validation?
8. Why do skip links matter?
9. Which selector families are named in the syllabus?
10. What cascade factors are considered before final source order?
11. Why is inline style not universally stronger than every other declaration?
12. How do specificity and inheritance differ?
13. Why are low-specificity classes easier to maintain?
14. What does border-box change?
15. When are logical properties useful?
16. How do absolute and fixed positioning differ?
17. Why does an arbitrarily high z-index sometimes fail?
18. Which properties commonly animate efficiently, and what must still be done?
19. Why should `will-change` be applied narrowly?
20. What does a CSS framework not guarantee?
21. Why is deep preprocessor nesting risky?
22. Why may concatenating every CSS file be counterproductive?
23. From where is a relative CSS `url()` resolved?
24. When is an internal or inline style justified?
25. What should accessible form error handling communicate and focus?
26. Why are positive tabindex values usually avoided?
27. What evidence does an HTML/CSS validator provide—and not provide?
28. How do computed styles help solve cascade bugs?
29. Why are breakpoints based on content preferable to a device-name list?
30. How do Flexbox and Grid differ in primary dimensional model?
31. What does progressive enhancement mean?
32. What is `@supports` for?
33. Which media should normally be lazy-loaded?
34. What turns a performance preference into a testable requirement?
35. Which accessibility checks cannot be replaced by an automated scan?
36. What are the three current Core Web Vitals?
37. Why must structured data match visible content?
38. What makes an analytics event useful?
39. What duration caveat exists on the official exam page?
40. What must be rechecked before purchase?

## Answer key

1. Use a standards-mode doctype, document language, early charset, useful title and device-width viewport without disabling zoom. Description summarizes the actual page; a favicon and platform-specific social tags serve separate consumers. Browser parser repair is not validation.
2. A robots instruction addresses cooperating crawlers and never prevents someone fetching a public URL. A crawler must fetch the page to discover noindex; blocking it in robots.txt can hide that instruction. Private material needs access control.
3. Use section for a thematic group with an appropriate heading and article for self-contained content. A named section may become a region landmark; article is not automatically a landmark. Choose meaning before styling.
4. Provide a useful caption, real header cells and row/column scope for simple relationships. Preserve table semantics at narrow widths. Complex tables need a separate association review; visual bolding alone does not identify headers.
5. Width/height establish intrinsic aspect/space information and reduce avoidable shifts. Srcset with accurate sizes helps select an appropriate resource; it does not replace alternatives or guarantee the smallest candidate. Do not routinely lazy-load the likely above-the-fold LCP image.
6. Decide trust/origin, minimum sandbox and permission-policy capabilities, referrer exposure, a meaningful title and useful fallback. Sandbox and allow solve different concerns. Granting a capability in markup does not establish user consent or cross-browser availability.
7. The server still validates untrusted input and files, authorizes actions and safely processes/stores/responds. Client checks and accept/inputmode hints can be bypassed; FormData construction does not validate. A local-only demonstration has no production server assurance.
8. A visible-on-focus skip link gives keyboard users a short path past repeated navigation. Its target must actually receive a useful navigation/focus result. The example tests the link reaching main, not every assistive technology.
9. Type, class, ID, attribute, pseudo-class and pseudo-element selectors. Distinguish zero-weight where from max-argument is/not/has, and distinguish a matching comma-list selector from the weight of a nonmatching one.
10. Filter relevance, compare origin/importance and layers, then specificity, applicable scoping proximity and finally source order. Keyframes and transitions occupy their own precedence positions. Counting selector columns first can yield the wrong result.
11. Normal inline author style loses to important declarations, while important inline author style still loses to user/user-agent important rules and active transitions. Layers reverse order for important declarations; important is not a specificity increment.
12. Specificity compares three columns among otherwise eligible competing declarations. Inheritance supplies a value only when the child has no effective own value; directly declaring blue on a child beats red inherited from an important parent declaration.
13. Low-specificity classes reduce dependence on markup ancestry and make overrides understandable within layers and source order. One ID still beats eleven classes in a tied layer/origin context. Avoid decimal-score arithmetic and deep nesting.
14. Border-box includes padding and border inside the declared width/height. With width 200, padding 10 and border 5 on both sides, content-box occupies 230 while border-box occupies 200. Margins remain outside; minimum content constraints still need consideration.
15. Logical start/end properties adapt to writing direction and mode. In horizontal RTL, margin-inline-start maps to the right. Changing dir does not translate strings or validate every writing mode; test wrapping and reading order too.
16. Absolute and fixed both leave normal flow. Absolute commonly uses the nearest positioned ancestor padding box; fixed commonly uses the viewport, but a transformed ancestor can establish its containing block. Inspect the actual ancestor chain.
17. Each stacking context participates as a unit in its parent. A large child number cannot outrank an outside sibling whose parent context is higher. Static flex/grid items may still use z-index; adding position is not always the fix.
18. Transform and opacity often avoid layout work, but efficiency depends on the actual rendering workload. Measure and provide a reduced-motion path. Keyframe values lose to important declarations; active transitions can temporarily override important endpoints.
19. Will-change can reserve resources and establish contexts before a visual change. Use it only for a measured need, for a limited duration when appropriate, and inspect side effects rather than placing it on every element.
20. A framework does not guarantee semantics, accessible validation, contrast, keyboard flow or efficient payload. Bootstrap warns about custom validation styles/tooltips and default color combinations. Verify the authored component and its real states.
21. Deep nesting produces tightly coupled selectors and potentially large output. Sass variables resolve at compilation; CSS custom properties remain dynamic. Configure a module once on first use and inspect generated CSS and source maps; Sass does not automatically autoprefix.
22. A single large bundle may invalidate caches unnecessarily or send unused page styles. HTTP version, compression, reuse, dependency order and change frequency affect the tradeoff. Compare measured transferred bytes and user timing, not only source-file count.
23. A relative URL in an external stylesheet resolves from that stylesheet URL. HTML link href resolves from the document base. A successful HTTP status containing the wrong content type/body can still leave the style unusable.
24. Internal styles can suit a prototype or genuinely page-local rule set; inline styles can express a justified dynamic value. Neither escapes the full cascade. Keep reusable rules and tokens organized and avoid editing generated output by hand.
25. Identify the affected control, explain the problem and how to correct it, and associate the text programmatically. Use native constraint behavior when suitable; focus an appropriate failed control or summary deliberately. Clear aria-invalid and visible errors after correction.
26. Positive tabindex makes a separate ordering scheme that becomes fragile as content changes. Prefer semantic DOM order and native focusability; visual Flexbox/Grid reordering does not automatically change keyboard or reading order.
27. Validators check the supported syntax/profile and certain structural requirements. The five HTML pages and two CSS files passed their dated checks, but that does not prove layout, keyboard interaction, contrast, full WCAG conformance or useful content.
28. Computed styles reveal the browser result; matched-rule/cascade tools explain why declarations win or lose. The hidden-error defect was caused by a later layer overriding display:none, not a missing attribute. Check invalid-at-computed-value behavior too.
29. Content determines when controls wrap, navigation becomes cramped or reading measure becomes awkward; device names are not stable layout contracts. Test around each chosen breakpoint and with long text, root-font enlargement and representative real devices.
30. Flexbox distributes along a primary axis; Grid coordinates rows and columns. Grow factors divide free space, shrink factors are scaled by bases, and automatic minima can constrain both. Grid fr units share space after fixed tracks and gaps.
31. Start with useful semantic content and a usable baseline, then add capabilities when available. In the service demo, information works without script while the local estimate controls remain disabled until their handler is ready. Do not make core content depend on an optional enhancement.
32. A supports query conditionally applies rules for a recognized declaration or selector. It does not prove a bug-free implementation, accessibility or full browser compatibility. Keep a baseline and test the actual supported browser set.
33. Normally defer noncritical offscreen media after checking the result. Reserve dimensions and provide suitable responsive sources/formats. Eagerly loading a likely LCP asset may be appropriate; lazy-loading everything can worsen visible loading.
34. State thresholds, units, pages/interactions, device/network conditions and a repeatable method. Separate source bytes from transfer sizes and bounded lab observations from representative field percentiles. An unlabelled Lighthouse score is an incomplete requirement.
35. Human review is needed for alternative-text meaning, understandable errors, reading/focus order, real screen-reader use, task success and many zoom/device cases. Automated results guide that work; the Chrome/root-font checks do not replace it.
36. LCP measures perceived loading, CLS visual stability and INP interaction responsiveness. Good field p75 thresholds are 2500ms,0.1 and 200ms respectively, segmented by mobile/desktop. Raw candidate/event entries, total shift sums or load-only TBT are not interchangeable with these metrics.
37. Structured data must accurately represent visible content and the relevant type. Syntax validity only establishes one layer of correctness; it does not guarantee a rich result. Metadata and canonical hints also do not force search presentation.
38. A useful event answers a stated decision/KPI at the correct semantic point, such as successful completion after validation. Use stable names and minimal parameters; do not include free text or identifiers unnecessarily. Local demo counts are not a deployed analytics or consent system.
39. The current credential headline says 60 minutes while the detail describes approximately 65 exam minutes plus a 2–5-minute tutorial/NDA. Preserve that contradiction and confirm the actual appointment; do not silently average or select one number.
40. Recheck the active 41-01 syllabus, language, actual delivery/supervision, appointment length, public price versus checkout, voucher/retake terms and practice alignment. The accessible HTML is the scope basis; unrelated roadmap copy and a PDF cover date are not a new-version announcement.

## Final readiness checklist

- [ ] I can author and validate the complete HTML objective set without relying on framework markup.
- [ ] I can calculate/explain cascade outcomes and fix conflicts without selector or `!important` escalation.
- [ ] I can build predictable boxes, positioning, stacking, transitions, and reduced-motion behavior.
- [ ] I understand basic Bootstrap and Sass/Less workflows, customization, source maps, and delivery tradeoffs.
- [ ] I can structure styles/assets and debug winning rules, boxes, Grid, Flexbox, and responsive states in developer tools.
- [ ] I can build mobile-first Flexbox/Grid layouts with suitable media queries, sources, fallbacks, and real-device tests.
- [ ] I can demonstrate accessibility, usability, internationalization, print, compatibility, and performance evidence.
- [ ] I can implement accurate SEO basics and a purpose-limited, privacy-aware analytics plan.
- [ ] I completed the ten labs and retained before/after evidence and regression notes.
- [ ] I rechecked the official WDA-41-01 page, especially its duration ambiguity.

## Places to learn

Public course/index comparison is not course completion. The official CSS landing lists 40 hours, nine modules and 45+ lessons; the HTML landing lists 25 hours and six modules. The public Pluralsight listing reports 31 hours, ten courses and seven labs, but subscriber interiors were not reviewed. Tutorial directories were read as indexes, not every linked lesson. Except for explicitly listed provider totals, hours below are author planning budgets. This is not a complete list, and it is not meant to be consumed in full. Pick one primary path, add focused documentation where useful, and spend at least as much time building, inspecting, measuring, and testing as watching. Commercial resources are supplementary; reconcile them with the current official syllabus.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official WDA-41-01 syllabus](https://jsinstitute.org/wda-exam-syllabus) | Free canonical objectives and weights | 2–3 hours to map and recheck |
| [Official WDA certification page](https://jsinstitute.org/wda-certification) | Free version, format, price, delivery, and policy links; duration needs confirmation | 30–60 minutes before purchase |
| [OpenEDG Web Dev 102: CSS](https://jsinstitute.org/css-essentials) | Public landing lists free Core / USD49 Pro and nine modules; prose places 45+ labs/diploma in Pro; repeated text-only tier lists remain ambiguous | 40 hours listed |
| [OpenEDG Web Dev 101: HTML](https://jsinstitute.org/html-essentials) | Free core / paid Pro; prerequisite foundation rather than WDA substitute | 25 hours listed if HTML needs rebuilding |
| [Cisco Networking Academy CSS Essentials](https://www.netacad.com/courses/css-essentials) | Partner link returned a 14-character application shell; access, account terms and lesson contents unverified | Author budget: about 40 hours; verify live listing |
| [MDN Learn CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics) and [CSS layout](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout) | Free current standards-oriented lessons | 20–30 hours with projects |
| [web.dev Learn CSS](https://web.dev/learn/css/) and [Responsive Design](https://web.dev/learn/design/) | Free modern modules and exercises | 15–25 hours for WDA-relevant portions |
| [W3C WAI Tutorials](https://www.w3.org/WAI/tutorials/) | Free authoritative accessibility patterns | 6–10 hours plus manual testing |
| [Pluralsight HTML and CSS path](https://www.pluralsight.com/paths/html-and-css) | Subscription; 10 courses and 7 labs, including 2026 guided labs | 31 hours listed; select layout, APIs, debugging, and optimization as needed |
| [O'Reilly Learning Web Design, 6th Edition](https://www.oreilly.com/library/view/learning-web-design/9781098137670/) | Subscription/buy; HTTP403 prevented fresh listing/interior verification; old page-count, date and runtime claims removed | Author budget: 18–25 hours for selected CSS/layout/responsive/quality topics; verify actual contents |
| [Udemy Learn HTML and CSS in 7 Days](https://www.udemy.com/course/learn-html-and-css-in-7-days-web-developer-bootcamp/) | Paid marketplace course; HTTP403 prevented current listing and lesson verification | Author budget: 8–12 hours project/test work; supplement frameworks, preprocessors, SEO, and analytics |

No exact current MeasureUp or Whizlabs WDA-41-01 product was verified. Use the official practice product if questions help diagnose weak blocks, and reject sources that cannot identify the active version or question provenance.
