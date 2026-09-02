---
exam_code: WDE-40-01
vendor_id: js-institute
official_blueprint: https://jsinstitute.org/wde-exam-syllabus
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# WDE-40-01 Certified Entry-Level Web Developer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The public syllabus, exam status, links, technical references, and exam-integrity boundaries were checked September 2, 2026. This guide contains original explanations and questions, not exam items. Recheck the [official WDE page](https://jsinstitute.org/wde-certification) and [WDE-40-01 syllabus](https://jsinstitute.org/wde-exam-syllabus) before scheduling.

**Current baseline:** WDE-40-01, active; syllabus last updated September 18, 2025<br>
**Upcoming blueprint change:** none announced on the official exam, syllabus, or certification-roadmap pages when checked<br>
**Official delivery snapshot:** 40 single- and multiple-select items; approximately 60-minute exam plus 2–5-minute tutorial/NDA; 75% passing score; TestNow; English and Spanish<br>
**Purchase snapshot:** no formal prerequisite; exam from USD 69, exam-plus-retake from USD 86, exam-plus-retake-plus-practice from USD 95, and standalone practice USD 29 when checked<br>

## How to use this guide

WDE rewards correct, semantic markup and foundational CSS more than visual decoration. Build one small multi-page site while working through the objectives. Validate every page, navigate it using only the keyboard, inspect its accessibility tree, test narrow and wide viewports, and explain each element by meaning—not by how a browser happens to draw it.

Use this cycle:

1. write valid source without copying a framework template;
2. inspect the parsed DOM and computed CSS in browser developer tools;
3. validate markup and test keyboard, zoom, contrast, and text alternatives;
4. change a boundary such as a missing image, long label, empty form value, denied permission, or small viewport;
5. map the evidence back to one of the 40 public objectives.

The syllabus includes introductory CSS, Geolocation, Web Storage, SVG, structured data, and ARIA, but remains primarily an HTML credential. Do not let advanced JavaScript or CSS frameworks displace foundational markup practice.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map and study emphasis

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| 1. HTML Fundamentals | 6 | 15% | Produce a valid standards-mode skeleton with correct encoding, entities, comments, and element categories |
| 2. Text Formatting and Structure | 8 | 20% | Mark up headings, prose, quotations, code, lists, and accessible data tables by meaning |
| 3. Multimedia and Hyperlinks | 8 | 20% | Build descriptive links and responsive, accessible images/media/embeds |
| 4. Forms and Styling | 10 | 25% | Construct labelled, constrained forms and apply maintainable foundational CSS |
| 5. Accessibility, Best Practices, and Modern HTML | 8 | 20% | Use semantics/ARIA, structured data, Web APIs, SVG, performance practices, and layered testing |

The counts and weights are from the official syllabus. Block 4 is largest, but the certification requires a cumulative score and the skills reinforce one another.

## 1. HTML fundamentals — 15%

### Standards-mode document and metadata

`<!DOCTYPE html>` selects the modern HTML parsing/rendering mode. It is a declaration, not an HTML element. A document has one root `<html>` element; set its `lang` to the primary language so assistive technology and translation tools can interpret content. Put metadata in `<head>` and rendered page content in `<body>`.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Workshop registration</title>
</head>
<body>
  <main><h1>Workshop registration</h1></main>
</body>
</html>
```

Place UTF-8 declaration early and keep the editor, HTTP header, and document encoding consistent. Mojibake is evidence that bytes were decoded with the wrong character encoding. A unique, descriptive title helps navigation, history, bookmarks, and search results.

### Block and inline behavior, entities, and comments

“Block” and “inline” in this entry objective describe common default layout behavior, not permanent element identity. CSS can change `display`, but element semantics remain. Use a paragraph because content is a paragraph and a link because it navigates, not merely because their default boxes look convenient.

Escape syntax-significant characters when they should appear as text: `&amp;`, `&lt;`, `&gt;`, and when needed in the context, quotes. `&nbsp;` creates a non-breaking space, not a general spacing tool. CSS controls visual spacing.

HTML comments use `<!-- ... -->`. They are visible to anyone who receives source, so never put credentials, private notes, or sensitive implementation details in them.

The [MDN Introduction to HTML](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content) is a current companion to this block.

> **Related item:** The browser parses source into a DOM tree. Developer tools may display implied or repaired nodes that were not written literally. Validation catches source problems; DOM inspection shows what the browser actually constructed.

## 2. Text formatting and structure — 20%

### Meaningful inline text

`<strong>` communicates strong importance and `<em>` stress emphasis. Underlining, marking, deletion, superscript, and subscript each carry contextual meaning; CSS handles appearance when no semantic distinction exists. Avoid choosing elements only to obtain bold, italic, or small text.

Use `<blockquote>` for a block quotation and `<q>` for an inline quotation. `<cite>` identifies a cited creative work, not an arbitrary person's name. `<abbr title="...">` can expose an expansion where it aids readers.

Use `<code>` for code fragments and place it inside `<pre>` when whitespace/newlines must be preserved. `<kbd>` represents user input and `<samp>` program output.

### Headings, paragraphs, and separation

Headings label sections and create a navigable hierarchy. The syllabus recommends a page-level `h1` and nested levels; do not select a heading rank for its default size. A section heading should describe what follows. Do not insert empty paragraphs or repeated `<br>` for space. Use `<br>` only for meaningful line breaks such as an address or poem and `<hr>` for a thematic change.

### Lists and tables

Use `<ul>` when order does not matter, `<ol>` when sequence/rank does, and `<dl>` with `<dt>`/`<dd>` for name-description groups. A list item belongs directly under `ul`/`ol`; a nested list belongs inside the relevant `li`.

Tables represent relationships in tabular data, not page layout. Include a concise `<caption>`, use `<th>` for headers, and identify simple row/column relationships with `scope`. `thead`, `tbody`, and `tfoot` group rows. `rowspan` and `colspan` can express real structures but complicate navigation, so keep them as simple as the data permits. The [W3C WAI tables tutorial](https://www.w3.org/WAI/tutorials/tables/) demonstrates accessible patterns.

## 3. Multimedia and hyperlinks — 20%

### Images and alternatives

`alt` replaces an image's meaning when the image is unavailable. Describe informative purpose concisely; use `alt=""` for an image that is entirely decorative and should be ignored. If an image is the only content of a link, its alternative must communicate the destination/action. A nearby caption does not automatically eliminate the need for alternative text.

Set intrinsic `width` and `height` to give the browser an aspect ratio and reduce layout shift. `srcset` offers candidate images and `sizes` describes expected rendered width so the browser can choose. `loading="lazy"` can defer noncritical offscreen images; do not lazily load the primary above-the-fold image without measuring the effect.

Use `<figure>` for self-contained content referenced as a unit and `<figcaption>` for its caption; not every image requires either.

### Links

An anchor with `href` navigates. Use descriptive link text that makes sense out of context. Relative URLs locate content within a site; absolute URLs include the full scheme/host. Fragment links target an element ID. `mailto:` and `tel:` express email and telephone destinations; `download` suggests downloading when same-origin/policy conditions allow.

Avoid opening new contexts unexpectedly. If `target="_blank"` is justified, the syllabus expects a suitable `rel` such as `noopener noreferrer`. Never use “click here” when the destination can be named.

### Audio, video, image maps, iframes, and favicons

Give audio/video user controls. Multiple `<source>` children can provide supported formats. Video captions use `<track kind="captions">`; provide a transcript when the information requires it. Avoid autoplay, particularly audible autoplay, and provide fallback text.

Image maps associate `<area>` regions with coordinates, but responsive resizing and keyboard/text equivalents make them fragile. If required, give each active region a meaningful alternative and provide equivalent ordinary links.

An iframe needs a concise `title` describing its embedded content. `sandbox` restricts capabilities; adding permissions relaxes restrictions, so grant only what the embed needs. `referrerpolicy` controls referrer information. CSS `aspect-ratio` or a responsive wrapper can preserve proportions.

Favicons are linked in `<head>`; test the selected formats/sizes in real tabs and bookmarks. A web app manifest is related application-installation context, not a substitute for the basic icon link.

> **Related item:** Responsive media has two different concerns: CSS controls layout size, while `srcset`/`sizes` can reduce transfer cost by selecting an appropriate source. Test both visual behavior and network selection.

## 4. Forms and styling — 25%

### Form semantics and controls

Every form control needs an accessible name, normally a visible `<label>` connected by `for`/`id`. `name` identifies submitted data; `id` identifies a document element. Choose input types such as `email`, `url`, `number`, or `password` for their semantics and user-agent behavior, but server-side validation remains essential.

Checkboxes represent independent Boolean choices; radios sharing a `name` represent one selection from a group. `<textarea>` handles multi-line text. `<select>` contains `<option>` values and `<optgroup>` can label groups. Give buttons an explicit `type` so an action button does not accidentally submit a form.

`fieldset` groups related controls and `legend` labels the group. A placeholder is a hint, not a label, because it disappears and may be unavailable to some users. `disabled` controls are unavailable and not submitted; `readonly` controls remain focusable and are submitted. Test those differences.

### Submission and validation

GET encodes form data in the URL and is appropriate for safe, repeatable queries such as search. POST sends data in the request body and is used for operations that create/change state or should not place fields in the URL. Neither method encrypts data; HTTPS provides transport protection. File uploads commonly require `multipart/form-data`.

Native constraints include `required`, `min`, `max`, `minlength`, `maxlength`, `pattern`, and `step`. `autocomplete` communicates field purpose/history expectations. Constraints improve interaction but do not establish trust at the server. Preserve input and provide specific, programmatically associated error guidance.

```html
<form method="post" action="/register">
  <fieldset>
    <legend>Contact</legend>
    <label for="email">Email</label>
    <input id="email" name="email" type="email" autocomplete="email" required>
  </fieldset>
  <button type="submit">Register</button>
</form>
```

The [W3C WAI forms tutorial](https://www.w3.org/WAI/tutorials/forms/) covers labels, grouping, instructions, validation, and notifications.

### Foundational CSS

Inline styles live in a `style` attribute and are difficult to reuse. Internal styles live in a page's `<style>` element. External stylesheets are related best practice for multi-page reuse/caching even though the objective emphasizes inline/internal application.

Classes are reusable tokens; IDs must be unique and work for fragments and scripting. Keep selectors simple and prefer classes for reusable styles. Use `div` as a block grouping container and `span` for inline grouping only when no semantic element fits.

The box model is content, padding, border, then margin. With default `content-box`, declared width/height apply to content; `box-sizing: border-box` includes padding and border in the declared size. Margins create outer separation. Set readable font family, size, weight, style, and line height; ensure foreground/background colors retain sufficient contrast.

## 5. Accessibility, best practices, and modern HTML — 20%

### Accessibility and ARIA

WCAG organizes accessibility under perceivable, operable, understandable, and robust principles. At this level, provide text alternatives, keyboard operation, visible focus, headings/landmarks, labels/instructions, sufficient contrast, and understandable errors. The live normative reference is [WCAG 2.2](https://www.w3.org/TR/WCAG22/).

Native HTML semantics normally provide roles, states, focus, and keyboard behavior together. Add ARIA only when native markup cannot express the component. `aria-expanded` describes whether a controlled region is expanded; `aria-checked` exposes check state for an appropriate ARIA widget; `aria-hidden="true"` removes content from the accessibility tree and must not hide focusable/essential content. ARIA changes accessibility semantics, not visual behavior or keyboard logic.

Use landmarks such as header, nav, main, article, section, aside, and footer according to their definitions. Not every visual wrapper is a section, and a section generally needs a heading.

### Structured data

Microdata uses attributes such as `itemscope`, `itemtype`, and `itemprop` to attach machine-readable vocabulary, often from Schema.org. Microformats use class/value conventions. Validate structured data and ensure it matches visible content; it does not guarantee a search-result feature.

### Geolocation, storage, and SVG

The syllabus labels Geolocation and Web Storage as HTML APIs, though they are browser Web APIs used from JavaScript. Geolocation requires a secure context and user permission; code must handle denial/unavailability. Do not request location before it is clearly needed.

`localStorage` persists by origin beyond a page session; `sessionStorage` is scoped to the origin and browser tab session. Both store strings and can fail or be restricted. They are synchronous and unsuitable for secrets. Treat storage as a cache/convenience, not guaranteed durable truth.

Inline SVG can scale without raster blur and can be styled. Give meaningful standalone graphics a suitable accessible name, and hide decorative graphics from assistive technology. `<symbol>` and `<use>` can form a reusable icon system.

### Quality and testing

Readable source, semantic elements, limited wrappers, deferred noncritical resources, sensible media size, and validation improve maintainability and performance. Automated accessibility tools find only some defect classes. Pair them with keyboard testing, zoom/reflow, contrast inspection, and a screen-reader spot check of critical flows. Record regressions.

> **Related item:** Accessibility is an outcome of the rendered experience, not a score from one scanner. Automated, manual, and user testing provide different evidence and should complement rather than replace one another.

## Integrated scenarios

### Scenario 1: Accessible event page

Build a standards-mode event page with landmarks, a sound heading hierarchy, schedule data table, speaker figures, responsive images, video captions/transcript, contact links, and a registration form. Validate it, navigate without a pointer, zoom to 200%, and test missing media.

### Scenario 2: Resource library

Create internal/fragment/external/download links, a description list, code samples, an accessible iframe, favicon, structured data, and a small SVG icon system. Explain every `alt`, `title`, relationship, and semantic container choice.

### Scenario 3: Permission-aware preference page

Ask for location only after a user action, handle denial, and store a non-sensitive display preference in Web Storage. Group and constrain controls, preserve valid zero/empty distinctions, and show errors without relying on color alone.

## Hands-on labs

1. **Document parser lab:** create valid and deliberately malformed skeletons; compare source, validator output, DOM tree, title, language, and standards/quirks behavior.
2. **Semantic text lab:** mark up an article containing every named text element, quotation, code/input/output sequence, nested list, and accessible table; defend each element choice.
3. **Responsive media lab:** produce informative/decorative/linked images, `srcset`/`sizes`, figure captions, audio/video sources and captions, an iframe, and fallback states. Inspect layout and network behavior.
4. **Link laboratory:** test relative, absolute, fragment, email, telephone, download, and new-context links; audit text out of context and keyboard focus.
5. **Form state matrix:** implement every named control/attribute and test initial, valid, invalid, blank, disabled, readonly, keyboard, autofill, GET, and POST behaviors.
6. **CSS foundation lab:** style the project with inline and internal CSS, classes/IDs, color/type, div/span, and each box layer; inspect computed styles and refactor repeated rules.
7. **Accessibility lab:** test landmarks/headings, alternatives, forms, ARIA state, focus order, focus visibility, contrast, zoom, reduced viewport, and one screen-reader flow; compare automated findings.
8. **Modern feature lab:** add valid microdata, permission-aware geolocation, local/session storage, and accessible SVG; exercise denial, disabled storage, invalid data, and missing-script fallbacks.

## Original readiness checks

1. What does the HTML doctype accomplish?
2. Why should the root language be declared?
3. What belongs in head versus body?
4. Why must editor, server, and document encodings agree?
5. Why is `&nbsp;` not a layout tool?
6. Can source comments contain secrets safely?
7. Why does changing CSS display not change an element's semantic meaning?
8. How do strong and em differ from purely visual bold/italic styling?
9. When are br and hr appropriate?
10. How should heading levels be chosen?
11. How do ul, ol, and dl differ?
12. Why should tables not be used for page layout?
13. What do caption and `th scope` contribute?
14. What should informative and decorative images use for alt?
15. Why specify image width and height?
16. How do CSS sizing and `srcset` solve different problems?
17. What should a linked image's accessible name describe?
18. What is the purpose of an iframe title?
19. Why can iframe sandbox permissions be dangerous when over-granted?
20. What makes link text useful out of context?
21. What is the difference between label, name, and id on a form control?
22. How do checkbox and radio semantics differ?
23. Why is placeholder not a label?
24. How do disabled and readonly submission/focus behavior differ?
25. When should GET and POST be selected?
26. Does client-side validation make server validation unnecessary?
27. Which form encoding is commonly needed for file upload?
28. When are classes preferable to IDs for styling?
29. When should div or span be used?
30. What are the four box-model layers?
31. What does border-box change?
32. What are the four WCAG principles?
33. Why is native HTML preferred over ARIA?
34. What must code do when an ARIA state changes visually?
35. What do itemscope and itemprop express?
36. What two boundaries must a Geolocation design handle?
37. How do localStorage and sessionStorage differ?
38. Why is one automated accessibility scan insufficient?
39. Which block has the largest official weight?
40. What must be rechecked before purchase?

## Answer key

1. It requests modern standards-mode HTML parsing/rendering.
2. It helps assistive technology, translation, and language-sensitive processing.
3. Metadata/resources in head; rendered page content in body.
4. Otherwise the same bytes may be decoded differently and display incorrectly.
5. It prevents a line break; CSS should create visual spacing.
6. No; delivered source is visible to users.
7. CSS changes presentation/layout, not the element's defined meaning.
8. They communicate importance/emphasis; appearance alone belongs in CSS.
9. Br for a meaningful line break and hr for a thematic change.
10. By document/section hierarchy, not desired font size.
11. Unordered choices, ordered sequence/rank, and name-description groups.
12. It creates incorrect structure and harms responsive/accessibility behavior.
13. A table name/context and explicit simple header relationships.
14. Concise purpose text and an empty `alt`, respectively.
15. To reserve aspect-ratio space and reduce layout shift.
16. CSS controls rendered layout; responsive-source attributes help choose an appropriate transferred file.
17. The link destination or action.
18. It names/describes the embedded content to users of assistive technology.
19. Each token relaxes a restriction and increases the embed's capabilities.
20. It identifies the destination/action without surrounding prose.
21. Label names the field to users; name identifies submitted data; id uniquely identifies/connects the element.
22. Checkboxes are independent; same-name radios select one from a group.
23. It disappears and does not reliably provide the control's persistent name.
24. Disabled is unfocusable and not submitted; readonly remains focusable and submits.
25. GET for safe repeatable retrieval; POST for state-changing/body-submitted operations.
26. No; client input is untrusted and server rules remain authoritative.
27. `multipart/form-data`.
28. For reusable styling patterns with lower, manageable specificity.
29. For generic block/inline grouping only when no semantic element fits.
30. Content, padding, border, margin.
31. Declared width/height include padding and border.
32. Perceivable, operable, understandable, robust.
33. Native controls bundle semantics, keyboard behavior, focus, and states.
34. Update the exposed ARIA state to match the actual component state.
35. An item and its vocabulary property in HTML microdata.
36. Secure-context/permission requirements and denial/unavailability/error handling.
37. Local storage persists for an origin; session storage is scoped to an origin and tab session.
38. Automation detects only a subset and cannot judge every semantic or usability outcome.
39. Forms and Styling at 25%.
40. Active version, syllabus, format, language, price, delivery, practice alignment, and policies.

## Final readiness checklist

- [ ] I can produce and validate a correct HTML skeleton from memory.
- [ ] I select text, list, table, landmark, and generic elements by meaning.
- [ ] I can make links, images, audio/video, iframes, and linked media understandable without visual context.
- [ ] I build labelled, grouped, constrained forms and explain GET/POST and disabled/readonly boundaries.
- [ ] I can predict the box model and apply low-complexity foundational CSS.
- [ ] I use native semantics before ARIA and keep exposed states synchronized.
- [ ] I can implement the named structured-data, browser-storage, location, and SVG basics safely.
- [ ] I combine validation, automation, keyboard, zoom/reflow, contrast, and screen-reader spot checks.
- [ ] I completed the eight labs and can show the resulting pages and test notes.
- [ ] I rechecked the official WDE-40-01 page and policies.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick one primary path, add focused references where useful, and spend at least as much time building, validating, and testing pages as watching. Commercial resources are supplementary; reconcile them with the current official syllabus.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official WDE-40-01 syllabus](https://jsinstitute.org/wde-exam-syllabus) | Free canonical objectives and weights | 2–3 hours to map and recheck |
| [Official WDE certification page](https://jsinstitute.org/wde-certification) | Free version, format, cost, delivery, and policy links | 30–60 minutes before purchase |
| [OpenEDG Web Dev 101: HTML](https://jsinstitute.org/html-essentials) | Free core / paid Pro; officially aligned; Pro adds 45+ labs | 25 hours listed |
| [Cisco Networking Academy HTML Essentials](https://www.netacad.com/courses/html-essentials) | Free account; official partner delivery | Plan about 25 hours; verify live listing |
| [MDN Learn: Structuring content with HTML](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content) | Free current lessons and challenges | 12–20 hours with project work |
| [W3C WAI Tutorials](https://www.w3.org/WAI/tutorials/) | Free authoritative accessibility patterns | 6–10 hours for page structure, images, tables, forms, and menus |
| [web.dev Learn HTML](https://web.dev/learn/html) | Free modern companion; broader in selected areas | 8–12 hours with examples |
| [Pluralsight HTML and CSS path](https://www.pluralsight.com/paths/html-and-css) | Subscription; broader 10-course/7-lab path | 31 hours listed; select entry-level HTML/CSS and relevant API labs |
| [O'Reilly Learning Web Design, 6th Edition](https://www.oreilly.com/library/view/learning-web-design/9781098137670/) | Subscription/buy; June 2025, 912 pages/30h04m listed | 12–18 hours for HTML, forms, media, accessibility, and SVG chapters |
| [Udemy Learn HTML and CSS in 7 Days](https://www.udemy.com/course/learn-html-and-css-in-7-days-web-developer-bootcamp/) | Paid marketplace course; broader CSS project path | 7h10m video plus 6–10 hours building; map carefully to WDE |

No exact current MeasureUp or Whizlabs WDE-40-01 product was verified. Use the official practice kit if practice questions are useful, and reject sources that do not identify the active version or question provenance.
