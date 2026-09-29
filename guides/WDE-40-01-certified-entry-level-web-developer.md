---
exam_code: WDE-40-01
vendor_id: js-institute
official_blueprint: https://jsinstitute.org/wde-exam-syllabus
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# WDE-40-01 Certified Entry-Level Web Developer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Selected public sources and all 40 numbered objectives were reviewed September 29, 2026. Original HTML and browser examples were executed. Direct official-page fetching failed; indexed current content supported manual scope comparison. Booking, paid interiors and human review remain pending. This guide contains original explanations and questions, not exam items. Recheck the [official WDE page](https://jsinstitute.org/wde-certification) and [WDE-40-01 syllabus](https://jsinstitute.org/wde-exam-syllabus) before scheduling.

**Current baseline:** WDE-40-01, active; syllabus last updated September 18, 2025<br>
**Upcoming blueprint change:** none announced on the official exam, syllabus, or certification-overview pages when checked; no unseen release feed or booking availability was verified<br>
**Official delivery snapshot:** 40 single- and multiple-select items; approximately 60-minute exam plus 2–5-minute tutorial/NDA; 75% cumulative normalized passing score; the credential page names TestNow; English and Spanish<br>
**Purchase snapshot:** no formal prerequisite; exam from USD 69, exam-plus-retake from USD 86, exam-plus-retake-plus-practice from USD 95, and standalone practice USD 29 when checked<br>

The [JS Institute homepage](https://www.jsinstitute.org/) names Pearson VUE/OnVUE for WDE, while the credential page names TestNow. The [TestNow policy](https://jsinstitute.org/test-now-testing-policies) describes entry-level exams as non-proctored by default but also contains a generic proctored-delivery statement. It states a seven-day wait after a failed attempt. Resolve delivery, supervision, retake eligibility and voucher terms for the actual WDE product before purchase; no account or checkout was inspected.

The credential page's headline says 60 minutes while its detail separates a 2–5-minute tutorial from approximately 60 exam minutes; do not infer the exact appointment length. Its practice-product row incorrectly names WDE-41-01 while the active exam and syllabus say WDE-40-01. That row is not evidence of a new exam version. No expiration rule is inferred from silence.

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

The complete indexed current English syllabus contains 40 numbered objectives in groups of 6/8/8/10/8. The retained snapshot abbreviates nested official identifiers into sequential block identifiers; the subjects were compared manually after direct fetching and automated monitoring failed. The current linked PDF was unavailable and was not read. Existing snapshots were retained; no successful fresh hash comparison is claimed.

Block 4 is largest, but every named subject matters. Item counts, weights and the normalized 75% threshold do not establish that exactly 30 equally weighted correct answers will always pass.

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

Place the entire UTF-8 declaration within the first 1024 bytes, as the [meta reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta) specifies, and keep the editor, HTTP header, and document encoding consistent. Mojibake is evidence that bytes were decoded with the wrong character encoding. A unique, descriptive title helps navigation, history, bookmarks, and search results.

### Block and inline behavior, entities, and comments

“Block” and “inline” in this entry objective describe common default layout behavior, not permanent element identity. CSS can change `display`, but element semantics remain. Use a paragraph because content is a paragraph and a link because it navigates, not merely because their default boxes look convenient.

Escape syntax-significant characters when they should appear as text: `&amp;`, `&lt;`, `&gt;`, and when needed in the context, quotes. `&nbsp;` creates a non-breaking space, not a general spacing tool. CSS controls visual spacing.

HTML comments use `<!-- ... -->`. They are visible to anyone who receives source, so never put credentials, private notes, or sensitive implementation details in them.

The [MDN Introduction to HTML](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content) is a current companion to this block.

> **Related item:** The browser parses source into a DOM tree. Developer tools may display implied or repaired nodes that were not written literally. Validation catches source problems; DOM inspection shows what the browser actually constructed. A repaired DOM is not proof of valid source: a `div` inside a `p` closes the paragraph during parsing. The workbook compares standards and quirks documents and checks this repair explicitly.

## 2. Text formatting and structure — 20%

### Meaningful inline text

`<strong>` communicates strong importance and `<em>` stress emphasis. `u` marks a non-textual annotation, `mark` highlights contextual relevance, `del` marks removed content, and `sup`/`sub` express typographic conventions such as exponents and formulas; CSS handles appearance when no semantic distinction exists. Avoid choosing elements only to obtain bold, italic, or small text.

Use `<blockquote>` for a block quotation and `<q>` for an inline quotation. `<cite>` identifies a cited creative work, not an arbitrary person's name. `<abbr title="...">` can expose an expansion where it aids readers.

Use `<code>` for code fragments and place it inside `<pre>` when whitespace/newlines must be preserved. `<kbd>` represents user input and `<samp>` program output.

### Headings, paragraphs, and separation

Headings label sections and create a navigable hierarchy. The syllabus recommends a page-level `h1` and nested levels; do not select a heading rank for its default size. A section heading should describe what follows. Do not insert empty paragraphs or repeated `<br>` for space. Use `<br>` only for meaningful line breaks such as an address or poem and `<hr>` for a thematic change.

### Lists and tables

Use `<ul>` when order does not matter, `<ol>` when sequence/rank does, and `<dl>` with `<dt>`/`<dd>` for name-description groups. A list item belongs directly under `ul`/`ol`; a nested list belongs inside the relevant `li`.

Tables represent relationships in tabular data, not page layout. Include a concise `<caption>`, use `<th>` for headers, and identify simple row/column relationships with `scope`. `thead`, `tbody`, and `tfoot` group rows. `rowspan` and `colspan` can express real structures but complicate navigation, so keep them as simple as the data permits. The [W3C WAI tables tutorial](https://www.w3.org/WAI/tutorials/tables/) organizes guidance on simple and complex relationships. The event example uses a caption, row groups and explicit row/column headers; its actual accessibility tree was inspected. Complex spanning tables still require a separate association review.

## 3. Multimedia and hyperlinks — 20%

### Images and alternatives

`alt` replaces an image's meaning when the image is unavailable. Describe informative purpose concisely; use `alt=""` for an image that is entirely decorative and should be ignored. If an image is the only content of a link, its alternative must communicate the destination/action. A nearby caption does not automatically eliminate the need for alternative text.

Set intrinsic `width` and `height` to give the browser an aspect ratio and reduce layout shift. `srcset` offers candidate images and `sizes` describes expected rendered width so the browser can choose. A `320w` descriptor must match that file's intrinsic width; do not mix width and density descriptors in one set. Width descriptors use `sizes`; density descriptors such as `2x` solve a different selection problem. Browser choice can depend on density, caching and other policy, so do not require one exact candidate in every environment. See the [image reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img). `loading="lazy"` can defer noncritical offscreen images; do not lazily load the primary above-the-fold image without measuring the effect.

Use `<figure>` for self-contained content referenced as a unit and `<figcaption>` for its caption; not every image requires either.

### Links

An anchor with `href` navigates. Use descriptive link text that makes sense out of context. Relative URLs locate content within a site; absolute URLs include the full scheme/host. Fragment links target an element ID. `mailto:` and `tel:` express email and telephone destinations; `download` suggests downloading when same-origin/policy conditions allow.

Avoid opening new contexts unexpectedly. If `target="_blank"` is justified, the syllabus expects a suitable `rel` such as `noopener noreferrer`. Modern `_blank` links implicitly provide the opener isolation of `noopener`; stating it explicitly documents intent. `noreferrer` also suppresses the Referer request header, a separate privacy behavior. The original browser check observed both a null opener and the missing header. The [anchor reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a) qualifies download behavior by origin and browser policy; the fixture download was initiated but its save was canceled, so successful file saving remains unverified. Never use “click here” when the destination can be named.

### Audio, video, image maps, iframes, and favicons

Give audio/video user controls. Multiple `<source>` children can provide supported formats. Video captions use `<track kind="captions">`; provide a transcript when the information requires it. Avoid autoplay, particularly audible autoplay, and provide fallback text. Boolean attributes depend on presence: `autoplay="false"` still enables the attribute. `preload` is a hint, not a transfer guarantee. Children inside `video` are the fallback for a browser that does not support the element; they do not automatically appear when every source fails. Keep a download link and transcript outside the player, as the event page does. See [video](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video) and [track](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track) for format, WebVTT, language and origin constraints. A silent animation has no speech to caption; the sample cue identifies its silence and the transcript describes its movement.

Image maps associate `<area>` regions with coordinates, but responsive resizing and keyboard/text equivalents make them fragile. If required, give each active region a meaningful alternative and provide equivalent ordinary links. The resource page deliberately keeps its map at 256 × 96 CSS pixels so its coordinates remain aligned; arbitrary responsive resizing would require a separate mapping strategy. The regions were found in Chrome's accessibility tree and activated with the keyboard.

An iframe needs a concise `title` describing its embedded content. `sandbox` restricts capabilities; adding permissions relaxes restrictions, so grant only what the embed needs. `referrerpolicy` controls referrer information. CSS `aspect-ratio` or a responsive wrapper can preserve proportions. An empty `sandbox` applies all its restrictions; each token restores a capability. Combining `allow-scripts` and `allow-same-origin` on same-origin content can let the embed remove the sandbox. A load event is not reliable proof that remote content loaded successfully. The original `srcdoc` checklist has no script permissions, a title and an adjacent text equivalent. See the [iframe reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe).

Favicons are linked in `<head>`; test the selected formats/sizes in real tabs and bookmarks. A web app manifest is related application-installation context, not a substitute for the basic icon link.

> **Related item:** Responsive media has two different concerns: CSS sets the intended layout, while `srcset`/`sizes` guide resource selection and can also affect intrinsic sizing. Test both visual behavior and network selection.

## 4. Forms and styling — 25%

### Form semantics and controls

Every form control needs an accessible name, normally a visible `<label>` connected by `for`/`id`. `name` identifies submitted data; `id` identifies a document element. Choose input types such as `email`, `url`, `number`, or `password` for their semantics and user-agent behavior, but server-side validation remains essential.

Checkboxes represent independent Boolean choices; radios sharing a `name` represent one selection from a group. `<textarea>` handles multi-line text. `<select>` contains `<option>` values and `<optgroup>` can label groups. Give buttons an explicit `type` so an action button does not accidentally submit a form.

`fieldset` groups related controls and `legend` labels the group. A placeholder is a hint, not a persistent visible label. Applicable native [disabled](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled) controls are not focusable, validated or submitted; applicable [readonly](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly) text controls remain focusable and submitted but are barred from constraint validation. `readonly` does not make a checkbox or select read-only. A disabled [fieldset](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset) disables descendant controls except those inside its first legend; a child's `.disabled` property can remain false while it matches `:disabled` through the ancestor.

Boolean attributes use presence, so `disabled="false"` still disables. Current `.value` can differ from the declared default restored by reset. Unchecked checkboxes, disabled controls and unnamed controls do not contribute ordinary submitted entries. Repeated names are valid: `FormData.getAll("topic")` preserves a multiple select; converting directly to an object loses earlier duplicate entries. `new FormData(form)` does not validate the form or include an unspecified submit button; the optional submitter argument supplies that button. See [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData/FormData) and [form](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form).

### Submission and validation

GET encodes form data in the URL and is appropriate for safe, repeatable queries such as search. POST sends data in the request body and is used for operations that create/change state or should not place fields in the URL. Neither method encrypts data; HTTPS provides transport protection. File uploads commonly require `multipart/form-data`.

Native constraints include `required`, `min`, `max`, `minlength`, `maxlength`, `pattern`, and `step`. `autocomplete` communicates field purpose/history expectations. Constraints improve interaction but do not establish trust at the server. Preserve input and provide specific, programmatically associated error guidance. The event page combines visible labels and format help with native messages and a status summary; no error is communicated through color alone.

Check the exact [constraint contract](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation): `pattern` matches the entire nonempty value using current Unicode-aware `v` syntax, without surrounding slashes. It does not replace `required`. An empty pattern rejects a nonempty value; an invalid pattern imposes no regex constraint. The [pattern page](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern) contains conflicting wording about the empty case, so the workbook verifies the behavior directly.

[`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength) counts UTF-16 code units: `🚀` uses two. Some overview tables loosely say characters or code points; do not infer a grapheme limit. `minlength`/`maxlength` constraints apply to user input, not every script assignment. Clear a custom error with `setCustomValidity("")`; passing `null` becomes a nonempty message and does not clear it. A general input-reference example says otherwise, but the original check confirms the empty-string contract.

For numeric controls, distinguish a valid zero from empty input: blank `.valueAsNumber` is `NaN`, while `Number("")` would be zero. Range and step failures differ from email/URL `typeMismatch`; setting a number's `.value` to invalid text can sanitize it to empty. `checkValidity()` checks constraints; `reportValidity()` also requests user-facing feedback. Calling `form.submit()` bypasses interactive constraint validation and the submit event; `novalidate` also changes interactive validation. Neither `FormData` construction nor a successful client check proves server trust.

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

The box model is content, padding, border, then margin. With default `content-box`, declared width/height apply to content; `box-sizing: border-box` includes padding and border in the declared size. Margins create outer separation and are not included in either declared width calculation. For a 100px width, 10px padding and 2px borders, the content-box border rectangle is 124px; border-box makes it 100px, leaving 76px for content. These dimensions were checked in Chrome. Some native controls already use border-box through user-agent CSS; declare the intended model. See [box-sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing). Set readable font family, size, weight, style, and line height; ensure foreground/background colors retain sufficient contrast.

## 5. Accessibility, best practices, and modern HTML — 20%

### Accessibility and ARIA

WCAG organizes accessibility under perceivable, operable, understandable, and robust principles. At this level, provide text alternatives, keyboard operation, visible focus, headings/landmarks, labels/instructions, sufficient contrast, and understandable errors. The live normative reference is [WCAG 2.2](https://www.w3.org/TR/WCAG22/).

Native HTML semantics normally provide roles, states, focus, and keyboard behavior together. Add ARIA only when native markup cannot express the component. `aria-expanded` describes whether a controlled region is expanded; `aria-checked` exposes check state for an appropriate ARIA widget; `aria-hidden="true"` removes content from the accessibility tree and must not hide focusable/essential content. ARIA changes accessibility semantics, not visual behavior or keyboard logic.

Use the [WAI landmark definitions](https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/): `article` is not itself a landmark; a `section` becomes a region landmark when it has an accessible name. A named form can provide a form landmark. Header/footer map to banner/contentinfo only in appropriate page contexts, not every nested article or section. Use meaningful names to distinguish repeated navigation regions. `aria-labelledby` can reuse a visible heading.

[`aria-hidden="true"`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-hidden) is inherited by descendants. It neither hides pixels nor removes keyboard focus; a descendant's `aria-hidden="false"` cannot undo an ancestor's true value. Do not put focusable content inside that hidden subtree. The [APG introduction](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/) treats a role as a promise: an ARIA button still needs keyboard and behavior code. Prefer a native button, as the resource-page disclosure does, and update `hidden` and `aria-expanded` together.

Selected WCAG 2.2 criteria distinguish text alternatives, relationships, keyboard operation, bypass links, visible focus, focus not being entirely obscured, labels, error identification, names/states and status messages. Normal text contrast requires 4.5:1 at AA, subject to the criterion's exceptions; large text has a different threshold. Text resizing to 200% and reflow at a 320-CSS-pixel equivalent are separate checks. Target Size (Minimum) uses 24 × 24 CSS pixels with listed spacing, equivalent-control, inline, user-agent and essential exceptions. These summaries do not establish conformance. The original checks cover selected colors, keyboard actions, accessibility-tree names, three viewport widths and doubled root font size; they are not actual browser zoom, a screen-reader session or a complete WCAG audit.

### Structured data

Microdata uses attributes such as `itemscope`, `itemtype`, and `itemprop` to attach machine-readable vocabulary, often from Schema.org. Microformats use class/value conventions. Validate structured data and ensure it matches visible content; it does not guarantee a search-result feature. The fictional event page uses the selected [Schema.org Event](https://schema.org/Event) vocabulary for name, description, location and an ISO date-time with offset. The inspected Schema.org page identifies itself as a development version; this example is a vocabulary exercise, not a search-engine eligibility claim.

### Geolocation, storage, and SVG

The syllabus labels Geolocation and Web Storage as HTML APIs, though they are browser Web APIs used from JavaScript. Geolocation requires a secure context and user permission; code must handle denial/unavailability. Do not request location before it is clearly needed. [getCurrentPosition](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition) can also be restricted by Permissions Policy. Handle error codes for permission denial, unavailable position and timeout, as well as unsupported/insecure contexts. Specify finite waiting behavior, retain a manual choice and preserve zero coordinates. The preference example rounds the displayed coordinates and neither saves nor transmits them. Its automated tests use fake providers; no real location request or permission grant was made.

`localStorage` persists by origin beyond a page session; `sessionStorage` is scoped to the origin and browser tab session. Both store strings and can fail or be restricted. They are synchronous and unsuitable for secrets. Treat storage as a cache/convenience, not guaranteed durable truth. Accessing the [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) getter can itself throw, and HTTP/HTTPS are different origins; `file:` behavior is not a portable contract. Private browsing and user deletion can change persistence. [sessionStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage) survives reload within a tab; a newly opened page can initially copy its opener's session storage, after which the copies are separate. A separately created tab in the test starts empty; opener copying was documented, not separately tested. The example validates stored values, catches getter/write/removal failures and removes only its own key. See the [Web Storage overview](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API).

Inline SVG can scale without raster blur and can be styled. Give meaningful standalone graphics a suitable accessible name, and hide decorative graphics from assistive technology. `<symbol>` and [`<use>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/use) can form a reusable icon system. Use `href` for the reference and give the symbol a viewBox; external references have origin/support limits. A [`title`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/title) can supply a concise name, or `aria-labelledby` can connect an existing visible label. The resource page names its meaningful SVG and hides only the decorative icon, leaving the download link's text name intact.

### Quality and testing

Readable source, semantic elements, limited wrappers, deferred noncritical resources, sensible media size, and validation improve maintainability and performance. Automated accessibility tools find only some defect classes. Pair them with keyboard testing, zoom/reflow, contrast inspection, and a screen-reader spot check of critical flows. Record regressions.

> **Related item:** Accessibility is an outcome of the rendered experience, not a score from one scanner. Automated, manual, and user testing provide different evidence and should complement rather than replace one another.

## Executed browser workbook

This original JavaScript block runs in a disposable modern browser page and returns `wdeCore` with **54 named checks**. It constructs local DOM/form fixtures without submitting them. It covers parser repair, FormData entries, Boolean attributes, native constraints, zero/empty values and disabled-fieldset inheritance. The separate browser harness checks actual typing, submissions and layout.

```javascript
globalThis.wdeCore = (() => {
  "use strict";
  const names = [];
  const check = (name, value) => { if (!value) throw new Error(name); names.push(name); };
  const parse = text => new DOMParser().parseFromString(text, "text/html");
  const standard = parse("<!doctype html><html lang='en'><title>Practice</title><p>Tea &amp; café</p></html>");
  check("standards mode", standard.compatMode === "CSS1Compat");
  check("doctype is a separate node", standard.doctype.name === "html");
  check("root language", standard.documentElement.lang === "en");
  check("parsed title", standard.title === "Practice");
  check("entities decode to text", standard.querySelector("p").textContent === "Tea & café");
  check("no doctype yields quirks", parse("<p>Practice</p>").compatMode === "BackCompat");
  const repaired = parse("<p>Before<div>Inside</div>After</p>");
  check("parser repairs invalid nesting", repaired.body.querySelector("p").textContent === "Before");
  check("div is not nested in repaired p", !repaired.querySelector("p div"));
  const comment = parse("<!-- public note --><p>Visible</p>");
  check("comment is still in document", comment.childNodes[0].nodeType === Node.COMMENT_NODE);
  check("comment not visible text", comment.body.textContent === "Visible");

  const form = document.createElement("form");
  form.innerHTML = '<input name="text" value="saved"><input name="zero" type="number" value="0">' +
    '<input name="disabled" value="omit" disabled><input name="readonly" value="keep" readonly>' +
    '<input value="unnamed"><input name="unchecked" type="checkbox">' +
    '<input name="checked" type="checkbox" checked><input name="tag" value="a"><input name="tag" value="b">' +
    '<button name="intent" value="save">Save</button>';
  const data = new FormData(form);
  check("named text included", data.get("text") === "saved");
  check("zero submitted as string", data.get("zero") === "0");
  check("disabled omitted", !data.has("disabled"));
  check("readonly included", data.get("readonly") === "keep");
  check("unnamed omitted", ![...data.values()].includes("unnamed"));
  check("unchecked checkbox omitted", !data.has("unchecked"));
  check("checkbox default value on", data.get("checked") === "on");
  check("duplicate names retained", data.getAll("tag").join() === "a,b");
  check("object conversion loses duplicates", Object.fromEntries(data).tag === "b");
  check("submitter omitted when not provided", !data.has("intent"));
  check("explicit submitter included", new FormData(form, form.querySelector("button")).get("intent") === "save");
  const named = form.elements.namedItem("text"); named.value = "edited";
  check("value and default differ", named.value === "edited" && named.defaultValue === "saved");
  form.reset(); check("reset restores defaults", named.value === "saved");
  const checkbox = form.elements.namedItem("unchecked"); checkbox.setAttribute("readonly", "");
  checkbox.click(); check("readonly does not disable checkbox", checkbox.checked);
  const disabled = form.elements.namedItem("disabled"); disabled.setAttribute("disabled", "false");
  check("Boolean attribute false string remains present", disabled.disabled);

  const input = document.createElement("input"); input.type = "text";
  input.pattern = "[A-Z]{3}"; input.value = "ABCD";
  check("pattern matches entire value", input.validity.patternMismatch);
  input.value = "ABC"; check("pattern match valid", input.checkValidity());
  input.value = ""; check("pattern alone permits empty", input.checkValidity());
  input.required = true; check("required forbids empty", input.validity.valueMissing);
  input.required = false; input.pattern = ""; input.value = "x";
  check("empty pattern rejects nonempty", input.validity.patternMismatch);
  input.pattern = "["; check("invalid regex imposes no pattern", !input.validity.patternMismatch);
  input.removeAttribute("pattern"); input.setCustomValidity("Fix this");
  check("custom message keeps invalid", input.validity.customError && !input.checkValidity());
  input.setCustomValidity(null);
  check("null becomes nonempty custom message", input.validity.customError);
  input.setCustomValidity(""); check("empty string clears custom error", input.checkValidity());
  input.type = "number"; input.min = "0"; input.max = "4"; input.step = "1";
  input.value = "0"; check("numeric zero is valid", input.checkValidity() && input.valueAsNumber === 0);
  input.value = ""; check("blank valueAsNumber is NaN", Number.isNaN(input.valueAsNumber));
  check("blank Number conversion would be zero", Number(input.value) === 0);
  input.value = "1.5"; check("numeric step mismatch", input.validity.stepMismatch);
  input.value = "5"; check("numeric upper bound", input.validity.rangeOverflow);
  input.value = "-1"; check("numeric lower bound", input.validity.rangeUnderflow);
  input.value = "bad"; check("programmatic invalid number sanitized", input.value === "" && !input.validity.typeMismatch);
  input.type = "email"; input.value = "missing-at"; check("email type mismatch", input.validity.typeMismatch);
  input.value = "person@example.test"; check("syntactic email accepted", input.checkValidity());
  input.type = "url"; input.value = "/relative"; check("URL input needs absolute URL", input.validity.typeMismatch);
  input.value = "https://example.test/"; check("absolute URL accepted", input.checkValidity());
  input.type = "text"; input.minLength = 3; input.value = "a";
  check("programmatic minlength is not enforced", !input.validity.tooShort);
  input.readOnly = true; check("readonly barred from constraint validation", !input.willValidate);
  input.readOnly = false; input.disabled = true; check("disabled barred from constraint validation", !input.willValidate);
  input.disabled = false; check("ordinary text validates", input.willValidate);
  form.append(input); input.required = true; input.value = "";
  check("form invalid", !form.checkValidity());
  check("FormData itself does not validate", new FormData(form).get("text") === "saved");
  const group = document.createElement("fieldset"); group.disabled = true;
  group.innerHTML = '<legend><input name="legend" value="enabled"></legend><input name="inside" value="disabled">';
  form.append(group);
  check("first legend exception", new FormData(form).get("legend") === "enabled");
  check("disabled fieldset descendant omitted", !new FormData(form).has("inside"));
  check("descendant disabled property differs from state", !group.querySelector('[name="inside"]').disabled && group.querySelector('[name="inside"]').matches(":disabled"));
  return { passed: names.length, names };
})();
```

## Integrated scenarios

The three complete HTML pages below were checked in existing Chrome 154.0.8037.58 and by the public W3C Nu HTML checker. **128 browser checks** passed in addition to the 54-check workbook. Native GET/POST requests used intercepted HTTPS fixtures; they did not reach a real registration service. A real backend still needs validation and application rules. This is an observed browser version, not an exam requirement.

### Reproduce the original files

Save the JSON operation record linked from the [review report](../docs/research/2026-09-29-wde-40-01-deep-review.md) as `wde-review.json`, then run this standard-library Python extractor in a working directory. It checks the recorded SHA-256 values and refuses to overwrite an existing `wde-workshop` folder. The record includes the three HTML files, workbook, two original SVG image sizes, favicon, WebVTT cue, text notes, a silent original WebM clip and a brief generated WAV tone.

```python
from pathlib import Path
import base64, hashlib, json

# Save the linked operation record as wde-review.json beside this script.
record = json.loads(Path("wde-review.json").read_text(encoding="utf-8"))
names = ("event.html", "resources.html", "preferences.html", "core.js",
         "studio-640.svg", "studio-320.svg", "mark.svg", "preview.vtt",
         "preview.webm", "tone.wav", "notes.txt")
assets = {}
for name in names:
    data = base64.b64decode(record["original_assets_base64"][name], validate=True)
    expected = record["browser_execution_receipt"]["source_sha256"][name]
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError("Asset hash mismatch: " + name)
    assets[name] = data
destination = Path("wde-workshop")
destination.mkdir()  # Deliberately refuses an existing directory.
for name, data in assets.items():
    (destination / name).write_bytes(data)
print("Prepared", len(assets), "original files in", destination)
```

Use your own local development server for ordinary page navigation. Storage behavior on `file:` URLs is not a dependable test; location requires a suitable secure context and permission. The exact review used route-intercepted HTTPS and fake location providers, with no persistent server or permission changes. Copying only the HTML blocks omits the required assets. The operation record also preserves the original harness and media generator.

### Scenario 1: Accessible event page

Save as `event.html`. The schedule connects row/column headers, responsive images keep correct candidate dimensions, and captions/transcript/download links accompany the silent preview. The registration form preserves zero, repeated topics and a readonly code. The native form sends fictional details to `/register`; supply your own test handler before trying submission outside the harness. Text wrapping and control widths were corrected after the enlarged-text check exposed overflow.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Markup workshop — event and registration</title>
  <link rel="icon" href="mark.svg" type="image/svg+xml">
  <style>
    * { box-sizing: border-box; }
    body { margin: 0; color: #172b3a; background: #fff; font: 1rem/1.6 system-ui, sans-serif; overflow-wrap: anywhere; }
    header, main, footer { max-inline-size: 52rem; margin-inline: auto; padding: 1rem; }
    a { color: #005a9c; text-underline-offset: .2em; }
    :focus-visible { outline: 3px solid #9c2b00; outline-offset: 3px; }
    .skip { position: absolute; top: -8rem; left: 1rem; background: #fff; padding: .75rem; z-index: 2; }
    .skip:focus { top: .25rem; }
    nav ul { display: flex; flex-wrap: wrap; gap: 1rem; list-style: none; padding: 0; }
    figure { margin: 1rem 0; }
    img, video { display: block; max-inline-size: 100%; block-size: auto; }
    .diagram { inline-size: 100%; }
    table { border-collapse: collapse; inline-size: 100%; }
    th, td { border: 1px solid #526677; padding: .5rem; text-align: start; overflow-wrap: anywhere; }
    caption { text-align: start; font-weight: 700; }
    fieldset { min-inline-size: 0; margin-block: 1rem; }
    .field { display: grid; gap: .25rem; margin-block: 1rem; }
    input:not([type=radio]):not([type=checkbox]), select, textarea { inline-size: 100%; max-inline-size: 30rem; }
    input, select, textarea, button { font: inherit; }
    button { min-block-size: 2.75rem; max-inline-size: 100%; padding: .5rem 1rem; }
    .help { margin: 0; }
    .notice { border-inline-start: .3rem solid #005a9c; padding-inline: 1rem; }
    [hidden] { display: none; }
  </style>
</head>
<body>
  <a class="skip" href="#main">Skip to workshop details</a>
  <header>
    <p>Learning studio</p>
    <nav aria-label="Workshop"><ul>
      <li><a href="event.html" aria-current="page">Event</a></li>
      <li><a href="resources.html">Resources</a></li>
      <li><a href="preferences.html">Preferences</a></li>
    </ul></nav>
  </header>
  <main id="main" tabindex="-1" itemscope itemtype="https://schema.org/Event">
    <h1 itemprop="name">Markup workshop</h1>
    <p class="notice">This is a fictional practice event. The form uses your own test endpoint.</p>
    <p><time itemprop="startDate" datetime="2026-10-15T10:00:00-04:00">October 15, 2026, 10:00 a.m. EDT</time>
      at <span itemprop="location">Sample Learning Studio, Room 2</span>.</p>
    <p itemprop="description">Build a clear page with <strong>meaningful structure</strong>.
      Bring a keyboard; <em>every participant</em> can use the exercises.</p>
    <section aria-labelledby="schedule-title">
      <h2 id="schedule-title">Schedule</h2>
      <table>
        <caption>Workshop sessions, Eastern time</caption>
        <thead><tr><th scope="col">Time</th><th scope="col">Topic</th></tr></thead>
        <tbody>
          <tr><th scope="row">10:00</th><td>Document structure</td></tr>
          <tr><th scope="row">10:30</th><td>Labels and form data</td></tr>
        </tbody>
        <tfoot><tr><th scope="row">Finish</th><td>11:00</td></tr></tfoot>
      </table>
      <figure>
        <img class="diagram" src="studio-640.svg" srcset="studio-320.svg 320w, studio-640.svg 640w"
          sizes="(max-width: 52rem) calc(100vw - 2rem), 50rem" width="640" height="240"
          alt="Room 2 is to the right of the information desk; both are reached from the front entrance.">
        <figcaption>Practice venue layout; ask at the desk if you need directions.</figcaption>
      </figure>
    </section>
    <section aria-labelledby="preview-title">
      <h2 id="preview-title">Workshop preview</h2>
      <video id="preview" controls preload="metadata" poster="studio-640.svg" width="640" height="240">
        <source src="preview.webm" type="video/webm">
        <track kind="captions" srclang="en" label="English" src="preview.vtt" default>
        Your browser does not support this video element.
      </video>
      <p><a href="preview.webm" download>Download the silent practice clip</a>.</p>
      <details><summary>Read the preview transcript</summary>
        <p>A blue circle moves across a light background. There is no speech or other audio.</p>
      </details>
      <p>The download and transcript remain available if playback fails.</p>
    </section>
    <section aria-labelledby="registration-title">
      <h2 id="registration-title">Practice registration</h2>
      <p>Use fictional details only. All fields marked “required” must be completed.</p>
      <form id="registration" method="post" action="/register" aria-labelledby="registration-title">
        <fieldset>
          <legend>Contact and place</legend>
          <div class="field"><label for="email">Email (required)</label>
            <input id="email" name="email" type="email" autocomplete="email" required></div>
          <div class="field"><label for="seats">Additional seats (0 through 4, required)</label>
            <input id="seats" name="seats" type="number" min="0" max="4" step="1" value="0" required></div>
          <div class="field"><label for="code">Practice code (three uppercase letters, required)</label>
            <input id="code" name="code" pattern="[A-Z]{3}" maxlength="3" title="Three uppercase letters"
              aria-describedby="code-help" required>
            <p id="code-help" class="help">For example, LAB. Spaces and digits are not accepted.</p></div>
          <div class="field"><label for="course">Workshop code</label>
            <input id="course" name="course" value="HTML-INTRO" readonly></div>
        </fieldset>
        <fieldset>
          <legend>Attendance format (required)</legend>
          <label><input type="radio" name="format" value="room" required> In the room</label>
          <label><input type="radio" name="format" value="remote"> Remote</label>
        </fieldset>
        <div class="field"><label for="topics">Topics of interest (select one or more)</label>
          <select id="topics" name="topic" multiple size="3">
            <optgroup label="HTML"><option value="structure">Structure</option><option value="forms">Forms</option></optgroup>
            <optgroup label="Practice"><option value="keyboard">Keyboard checks</option></optgroup>
          </select></div>
        <label><input id="updates" type="checkbox" name="updates" value="yes"> Include practice updates</label>
        <div class="field"><label for="notes">Optional access notes</label>
          <textarea id="notes" name="notes" rows="3" maxlength="120"></textarea></div>
        <p id="form-status" role="status"></p>
        <button type="submit" name="intent" value="register">Send practice registration</button>
        <button type="reset">Restore defaults</button>
      </form>
    </section>
  </main>
  <footer><p>Contact <a href="mailto:workshops@example.test">the practice coordinator</a>
    or <a href="tel:+12025550124">202-555-0124</a>. Fictional contact details.</p></footer>
  <script>
    const form = document.querySelector("#registration");
    const status = document.querySelector("#form-status");
    form.addEventListener("invalid", event => {
      const invalid = [...form.querySelectorAll("input:invalid, select:invalid, textarea:invalid")];
      status.textContent = "Check: " + invalid.map(control => control.labels?.[0]?.textContent || control.name).join("; ") + ".";
    }, true);
    form.addEventListener("input", () => { status.textContent = ""; });
    form.addEventListener("reset", () => { status.textContent = "Defaults restored."; });
  </script>
</body>
</html>
```

### Scenario 2: Resource library

Save as `resources.html`. Explain the semantic text, nested lists, link relationships, fixed-size image map, sandboxed checklist, disclosure state and named/decorative SVG distinction. The tests observed keyboard activation of both the disclosure and map, a null popup opener and suppressed referrer. The download's suggested name was correct, but Chrome canceled saving in this setup; saved bytes remain unverified. The audio was played muted and its duration checked, not assessed by listening.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Workshop resource library</title>
  <link rel="icon" href="mark.svg" type="image/svg+xml">
  <style>
    * { box-sizing: border-box; }
    body { max-inline-size: 52rem; margin: auto; padding: 1rem; font: 1rem/1.6 system-ui, sans-serif; color: #172b3a; background: white; overflow-wrap: anywhere; }
    a { color: #005a9c; }
    :focus-visible { outline: 3px solid #9c2b00; outline-offset: 3px; }
    nav ul { display: flex; flex-wrap: wrap; gap: 1rem; padding: 0; list-style: none; }
    pre { overflow-x: auto; padding: .5rem; background: #eef4f8; }
    iframe { inline-size: 100%; block-size: 10rem; border: 1px solid #526677; }
    audio { max-inline-size: 100%; }
    .icon { inline-size: 1.25rem; block-size: 1.25rem; vertical-align: middle; }
    .symbols { position: absolute; inline-size: 0; block-size: 0; overflow: hidden; }
    .skip { display: inline-block; padding: .5rem; }
    [hidden] { display: none; }
    button { font: inherit; padding: .5rem 1rem; min-block-size: 2.75rem; }
  </style>
</head>
<body>
  <a class="skip" href="#main">Skip to resources</a>
  <header><nav aria-label="Workshop"><ul>
    <li><a href="event.html">Event</a></li><li><a href="resources.html" aria-current="page">Resources</a></li>
    <li><a href="preferences.html">Preferences</a></li>
  </ul></nav></header>
  <main id="main" tabindex="-1">
    <h1>Workshop resource library</h1>
    <svg class="symbols" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <symbol id="bookmark" viewBox="0 0 24 24"><path d="M5 2h14v20l-7-4-7 4z" fill="currentColor"/></symbol>
    </svg>
    <section aria-labelledby="reference-title">
      <h2 id="reference-title">Reference notes</h2>
      <p><abbr title="HyperText Markup Language">HTML</abbr> names structure. Escape markup when teaching it:</p>
      <pre><code>&lt;p&gt;Tea &amp;amp; coffee&lt;/p&gt;</code></pre>
      <p>Press <kbd>Tab</kbd> to move between controls. Our practice program reports <samp>Ready</samp>.</p>
      <blockquote><p>Meaning comes before decoration.</p></blockquote>
      <p>That quotation is from the fictional handout <cite>Workshop Notes</cite>. Its author says <q>Test each boundary.</q></p>
      <p><del>Bring three devices.</del> <mark>Bring one device.</mark> The annotations <u>strcuture</u>, H<sub>2</sub>O and 2<sup>3</sup> illustrate distinct text meanings.</p>
      <dl><dt>Element</dt><dd>A structured part of a document.</dd><dt>Attribute</dt><dd>Additional information on an element.</dd></dl>
      <ol><li>Build the page.<ul><li>Choose headings.</li><li>Associate labels.</li></ul></li><li>Check the rendered result.</li></ol>
      <hr>
      <p>Practice address:<br>Learning Studio<br>Room 2</p>
      <p style="font-style: italic">The next resources are optional practice material.</p>
      <p><a id="external-reference" href="https://developer.mozilla.org/en-US/docs/Web/HTML"
        target="_blank" rel="noopener noreferrer">HTML reference (opens a new tab)</a></p>
      <p><a id="download-notes" href="notes.txt" download="workshop-notes.txt"><svg class="icon" aria-hidden="true"><use href="#bookmark"/></svg> Download practice notes</a></p>
      <p><a href="#embed-title">Read the embedded checklist</a>.</p>
      <svg id="named-graphic" viewBox="0 0 160 48" width="160" height="48" role="img" aria-labelledby="graphic-title">
        <title id="graphic-title">A three-step sequence: build, check, revise</title>
        <path d="M8 24h144" stroke="#005a9c" stroke-width="4"/>
        <circle cx="16" cy="24" r="10" fill="#172b3a"/><circle cx="80" cy="24" r="10" fill="#172b3a"/><circle cx="144" cy="24" r="10" fill="#172b3a"/>
      </svg>
    </section>
    <section aria-labelledby="map-title">
      <h2 id="map-title">Choose a practice station</h2>
      <img src="studio-320.svg" width="256" height="96" usemap="#stations" alt="Two stations: information on the left, Room 2 on the right.">
      <map name="stations">
        <area shape="rect" coords="12,12,104,60" href="#reference-title" alt="Information station: reference notes">
        <area shape="rect" coords="152,12,244,60" href="#embed-title" alt="Room 2 station: publishing checklist">
      </map>
      <p>Text alternatives: <a href="#reference-title">Information station notes</a> and <a href="#embed-title">Room 2 checklist</a>.</p>
      <h3>Optional audio</h3>
      <audio id="tone" controls muted preload="metadata"><source src="tone.wav" type="audio/wav">Your browser does not support this audio element.</audio>
      <p>The recording contains one brief tone and no speech. Start playback and unmute if you want to hear it.</p>
      <p><a href="tone.wav" download>Download the tone</a>.</p>
    </section>
    <section aria-labelledby="embed-title">
      <h2 id="embed-title">Embedded checklist</h2>
      <iframe id="checklist" title="Three checks before publishing" sandbox referrerpolicy="no-referrer"
        srcdoc="<!doctype html><html lang='en'><head><meta charset='utf-8'><title>Checklist</title></head><body><h1>Before publishing</h1><ol><li>Check labels.</li><li>Use the keyboard.</li><li>Read error messages.</li></ol></body></html>"></iframe>
      <p>The same checklist in ordinary text: check labels, use the keyboard, and read error messages.</p>
    </section>
    <section aria-labelledby="more-title">
      <h2 id="more-title">Further practice</h2>
      <button id="toggle" type="button" aria-expanded="false" aria-controls="more">Show extra practice</button>
      <div id="more" hidden><p>Repeat the form with blank, zero, and invalid values.</p></div>
    </section>
  </main>
  <footer><p>Original learning examples.</p></footer>
  <script>
    const toggle = document.querySelector("#toggle");
    const more = document.querySelector("#more");
    toggle.addEventListener("click", () => {
      more.hidden = !more.hidden;
      toggle.setAttribute("aria-expanded", String(!more.hidden));
      toggle.textContent = more.hidden ? "Show extra practice" : "Hide extra practice";
    });
  </script>
</body>
</html>
```

### Scenario 3: Permission-aware preference page

Save as `preferences.html`. The allowlist rejects unknown stored values; exceptions leave usable controls and a status message. Forgetting removes only the example's key. Location waits for an explicit click and leaves a manual region choice. Eleven fake-provider cases cover zero coordinates, out-of-range/nonfinite coordinates, denial, unavailability, timeout, unknown error, unsupported/insecure contexts, synchronous failure and repeated callbacks. They do not verify a real positioning service.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Workshop display and location preferences</title>
  <style>
    * { box-sizing: border-box; }
    body { max-inline-size: 46rem; margin: auto; padding: 1rem; color: #172b3a; background: white; font: 1rem/1.6 system-ui, sans-serif; overflow-wrap: anywhere; }
    a { color: #005a9c; }
    :focus-visible { outline: 3px solid #9c2b00; outline-offset: 3px; }
    nav ul { display: flex; flex-wrap: wrap; gap: 1rem; list-style: none; padding: 0; }
    fieldset { min-inline-size: 0; margin-block: 1rem; }
    button, select { font: inherit; min-block-size: 2.75rem; padding: .5rem; max-inline-size: 100%; }
    .sample li { padding-block: .5rem; }
    [data-density="compact"] .sample li { padding-block: .15rem; }
  </style>
</head>
<body data-density="comfortable">
  <a href="#main">Skip to preferences</a>
  <header><nav aria-label="Workshop"><ul>
    <li><a href="event.html">Event</a></li><li><a href="resources.html">Resources</a></li>
    <li><a href="preferences.html" aria-current="page">Preferences</a></li>
  </ul></nav></header>
  <main id="main" tabindex="-1">
    <h1>Workshop preferences</h1>
    <form id="preferences">
      <fieldset><legend>Display spacing</legend>
        <label for="density">Spacing</label>
        <select id="density" name="density"><option value="comfortable">Comfortable</option><option value="compact">Compact</option></select>
        <button type="submit">Apply spacing</button>
        <button id="forget" type="button">Forget saved spacing</button>
      </fieldset>
    </form>
    <p id="storage-status" role="status"></p>
    <ul class="sample"><li>Document structure</li><li>Labels and controls</li><li>Keyboard checks</li></ul>
    <section aria-labelledby="location-title">
      <h2 id="location-title">Optional approximate location</h2>
      <p>Location is optional. Requesting it may show a browser permission prompt. The demo displays rounded coordinates without saving or sending them. You can use the manual region choice instead.</p>
      <button id="locate" type="button">Use approximate location</button>
      <p id="location-status" role="status">Location has not been requested.</p>
      <label for="region">Manual region</label>
      <select id="region"><option value="">Choose when useful</option><option>East</option><option>West</option></select>
    </section>
  </main>
  <footer><p>Display preferences are optional and can be forgotten.</p></footer>
  <script>
    globalThis.WdePreferences = (() => {
      "use strict";
      const key = "wde-demo-density-v1";
      const allowed = value => value === "comfortable" || value === "compact";
      function read(getStorage = () => localStorage) {
        try {
          const value = getStorage().getItem(key);
          return { value: allowed(value) ? value : "comfortable", available: true, invalid: value !== null && !allowed(value) };
        } catch { return { value: "comfortable", available: false, invalid: false }; }
      }
      function save(value, getStorage = () => localStorage) {
        if (!allowed(value)) throw new TypeError("Unknown spacing option");
        try { getStorage().setItem(key, value); return true; } catch { return false; }
      }
      function forget(getStorage = () => localStorage) {
        try { getStorage().removeItem(key); return true; } catch { return false; }
      }
      function locate(geolocation, secure, report, done) {
        if (!secure || !geolocation) { report("Location unavailable. Use the manual region choice."); done(); return; }
        let settled = false;
        function finish(message) { if (!settled) { settled = true; report(message); done(); } }
        try {
          geolocation.getCurrentPosition(position => {
            const { latitude, longitude } = position.coords || {};
            if (!Number.isFinite(latitude) || Math.abs(latitude) > 90 ||
                !Number.isFinite(longitude) || Math.abs(longitude) > 180) {
              finish("Location unavailable. Use the manual region choice."); return;
            }
            finish(`Approximate coordinates: ${latitude.toFixed(1)}, ${longitude.toFixed(1)}. Nothing was saved.`);
          }, error => {
            const reasons = { 1: "Permission denied", 2: "Location unavailable", 3: "Location timed out" };
            finish((reasons[error.code] || "Location unavailable") + ". Use the manual region choice.");
          }, { enableHighAccuracy: false, maximumAge: 60000, timeout: 5000 });
        } catch { finish("Location unavailable. Use the manual region choice."); }
      }
      return { key, read, save, forget, locate };
    })();
    const density = document.querySelector("#density");
    const status = document.querySelector("#storage-status");
    const initial = WdePreferences.read();
    density.value = initial.value; document.body.dataset.density = initial.value;
    status.textContent = !initial.available ? "Saved preferences unavailable; using comfortable spacing." :
      initial.invalid ? "Unrecognized saved preference ignored; using comfortable spacing." : "Choose the spacing that works for you.";
    document.querySelector("#preferences").addEventListener("submit", event => {
      event.preventDefault();
      document.body.dataset.density = density.value;
      status.textContent = WdePreferences.save(density.value) ? "Spacing applied and saved." : "Spacing applied for this page; saving is unavailable.";
    });
    document.querySelector("#forget").addEventListener("click", () => {
      const removed = WdePreferences.forget();
      density.value = "comfortable"; document.body.dataset.density = "comfortable";
      status.textContent = removed ? "Saved spacing forgotten." : "Comfortable spacing applied; saved data could not be removed.";
    });
    const locate = document.querySelector("#locate");
    locate.addEventListener("click", () => {
      locate.disabled = true;
      const report = message => { document.querySelector("#location-status").textContent = message; };
      report("Waiting for location. You can keep using the manual region choice.");
      WdePreferences.locate(navigator.geolocation, isSecureContext, report, () => { locate.disabled = false; });
    });
  </script>
</body>
</html>
```

The automated layout checks used 320/768/1280 CSS-pixel viewports and doubled root font size. Selected screenshots were inspected, and the three pages had zero messages from the public Nu checker. No full screen-reader, browser-zoom, cross-browser, assistive-technology, favicon/bookmark, performance or production accessibility audit was performed. Original media decoding, caption parsing and muted audio playback were observed; broad media-failure behavior still needs learner testing.

## Hands-on labs

These eight broader activities remain **proposed**. The bounded original checks above do not establish completion of every learner activity or a complete accessibility audit.

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

1. It requests standards mode; the doctype is a declaration represented by its own DOM node, not an ordinary element. Omitting it produces quirks mode in the workbook. Validity still requires more than a doctype.
2. The root language supports pronunciation, translation and language-sensitive processing. It does not translate the text or replace a useful document title; mark passages in another language when needed.
3. Head contains document metadata and resource relationships; body contains page content. The browser may insert or repair nodes, so inspect both source and the resulting DOM and run a conformance checker.
4. Otherwise identical bytes can be decoded into the wrong characters. Declare UTF-8 early, within the first 1024 bytes, and keep actual saved bytes and server metadata consistent.
5. It means a non-breaking space, which changes line-breaking behavior. Use margin, padding or layout CSS for visual separation instead of inserting repeated entities.
6. No. Comments remain in delivered source even though ordinary rendered text omits them. The workbook locates a comment node directly.
7. Display changes the CSS box behavior, not the HTML meaning or built-in interaction contract. A styled span does not automatically become a keyboard-operable button.
8. Strong communicates importance and em stress emphasis. Use CSS for appearance alone; u, mark, del, sup and sub each express their own contextual meaning.
9. Br represents a meaningful line break, such as within an address; hr represents a thematic change. Empty paragraphs and repeated breaks are not spacing controls.
10. Follow the document hierarchy and descriptive section purpose. The event page uses a page heading and section headings; changing font size is not a reason to change heading rank.
11. Ul groups items without significant order; ol expresses sequence/rank; dl contains name-description groups. Nest a subordinate list inside its parent li, not as an unrelated sibling of that li.
12. A layout table falsely expresses data relationships and can impair reading/reflow. Use CSS layout; retain tables for information whose row/column relationships are meaningful.
13. Caption gives table context; th with scope identifies simple row/column relationships. They do not automatically solve every multi-level spanning table, which needs a more detailed association review.
14. An informative image needs a concise alternative for its purpose; a purely decorative image normally uses alt="". A caption does not automatically replace alt, and a linked image must name its destination or action.
15. Correct intrinsic dimensions establish an aspect ratio before the image loads, reducing avoidable layout movement. Responsive CSS may render another size while preserving that ratio.
16. CSS expresses layout; srcset supplies candidate resources and sizes informs width-based selection. Candidate descriptors must be accurate, and the browser may choose differently with density, cache or policy.
17. The destination or action, such as opening an event page, rather than an unhelpful filename. An adjacent visible text label may already provide the link name; avoid redundant decorative SVG announcements.
18. It describes the embedded browsing context so users can identify it. It does not repair inaccessible embedded content; the original checklist also has ordinary-text equivalents.
19. Sandbox tokens restore capabilities. Same-origin content with both script and same-origin privileges can escape the intended sandbox; the example uses an empty sandbox and verifies parent DOM access is unavailable.
20. It identifies a destination or action without vague surrounding prose. Announce a justified new tab, distinguish opener isolation from referrer suppression, and retain a clear focus indicator.
21. The label names the control for people and assistive technology; name supplies the submitted key; id identifies the element for associations, fragments and scripting. A label alone does not make an unnamed control submit data.
22. Checkboxes allow independent choices, and unchecked boxes are omitted from ordinary submission. Same-name radios form a single selection group. Repeated submitted names require getAll rather than a lossy object conversion.
23. Placeholder text is temporary hint content and disappears during entry. A visible label remains available, while aria-describedby can connect persistent format instructions.
24. Applicable disabled controls are omitted, unfocusable and barred from validation. Applicable readonly text controls still focus and submit but are barred from validation; readonly does not apply to every control. A disabled fieldset has a first-legend exception.
25. GET puts form entries in the URL for safe retrieval; POST places them in a body for the appropriate operation contract. Neither encrypts data; HTTPS supplies transport protection. Native intercepted requests verified both paths.
26. No. Constraints improve interaction but can be bypassed or changed. Script-set lengths, novalidate and form.submit illustrate limits; the server must validate syntax, authorization and business rules independently.
27. Multipart/form-data is commonly needed for file uploads. Let the browser construct the appropriate form boundary; a correct enctype does not validate file contents or authorize storage.
28. Classes express reusable styling patterns without requiring unique identifiers. IDs remain useful for label relationships, fragments and named sections; do not duplicate them for appearance.
29. Use generic containers when no more meaningful element fits. Div/span default layout is not a substitute for choosing main, nav, a heading, list, button or another semantic element.
30. Content, padding, border and margin. Margin is outside the border rectangle and remains outside the declared width in either box-sizing model.
31. Border-box includes padding and border in the declared size. The executed 100px example with 10px padding and 2px borders measured 100px versus 124px for content-box; the 3px margins were separate.
32. Perceivable, operable, understandable and robust. Apply concrete criteria such as text alternatives, keyboard access and useful labels; knowing the four words does not establish WCAG conformance.
33. Native elements supply established semantics and interaction. ARIA communicates roles/states but does not add missing keyboard logic; use a real button for the disclosure and keep its state synchronized.
34. Update the exposed state with the actual behavior, such as aria-expanded and hidden together. Aria-hidden does not hide pixels or remove focus, and a child cannot override a hidden ancestor with false.
35. Itemscope introduces an item and itemprop identifies a property within it; itemtype names a vocabulary type. The fictional Event date-time includes an offset and matches the visible event, without promising rich search results.
36. Check secure-context, browser support, permissions/policy and the actual result/error path. Use finite waiting behavior, preserve zero coordinates and retain a manual fallback. Fake providers tested the example without a real permission request.
37. Local storage is origin-scoped and may persist beyond a page session; session storage is scoped to origin and tab session, survives reload and may initially copy an opener. Both can fail, are string-based and should not be treated as durable secret storage.
38. A scanner cannot judge every meaning, interaction or user outcome. Nu validation, DOM/AX checks and selected keyboard/layout observations are useful evidence, while screen readers, real zoom and broader manual testing remain separate work.
39. Forms and Styling, at 25%, with ten published objectives/items. The other blocks remain required, and normalized scoring is not an equal-item passing shortcut.
40. Recheck active code, current syllabus, exact product/practice alignment, language, price, appointment length, delivery/proctoring and retake terms. The homepage/TestNow conflict and erroneous WDE-41-01 practice row remain unresolved at purchase level.

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

This is not a complete list, and it is not meant to be consumed in full. Pick one primary path, add focused references where useful, and spend at least as much time building, validating, and testing pages as watching. Commercial resources are supplementary; reconcile them with the current official syllabus. Times below are author planning budgets unless explicitly marked as a provider-listed total. Public contents and selected reference sections were reviewed, not every linked lesson or any paid course interior. The [review report](../docs/research/2026-09-29-wde-40-01-deep-review.md) records exact boundaries.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official WDE-40-01 syllabus](https://jsinstitute.org/wde-exam-syllabus) | Free canonical objectives and weights | 2–3 hours to map and recheck |
| [Official WDE certification page](https://jsinstitute.org/wde-certification) | Free version, format, cost, delivery, and policy links | 30–60 minutes before purchase |
| [OpenEDG Web Dev 101: HTML](https://jsinstitute.org/html-essentials) | Free Core / paid Pro; public prose attributes 45+ labs and a diploma to Pro; six modules and 45+ lessons listed | Provider lists 25 hours; no account lessons audited |
| [Cisco Networking Academy HTML Essentials](https://www.netacad.com/courses/html-essentials) | Partner landing returned only an application shell; account/curriculum details unverified | Author budget about 25 hours; verify actual access |
| [MDN Learn: Structuring content with HTML](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content) | Free current lessons and challenges | 12–20 hours with project work |
| [W3C WAI Tutorials](https://www.w3.org/WAI/tutorials/) | Free authoritative accessibility patterns | 6–10 hours for page structure, images, tables, forms, and menus |
| [web.dev Learn HTML](https://web.dev/learn/html) | Free modern companion; broader in selected areas | 8–12 hours with examples |
| [Pluralsight HTML and CSS path](https://www.pluralsight.com/paths/html-and-css) | Subscription; broader 10-course/7-lab path | 31 hours listed; select entry-level HTML/CSS and relevant API labs |
| [O'Reilly Learning Web Design, 6th Edition](https://www.oreilly.com/library/view/learning-web-design/9781098137670/) | Subscription/buy; direct access returned HTTP403, so current edition details/interiors unverified | Author budget 12–18 hours for relevant HTML/form/media/accessibility/SVG topics |
| [Udemy Learn HTML and CSS in 7 Days](https://www.udemy.com/course/learn-html-and-css-in-7-days-web-developer-bootcamp/) | Paid marketplace course; HTTP403 prevented fresh contents/runtime review | Author budget 6–10 hours building; verify listing and map to WDE |

The official course page lists free Core and USD49 Pro, but its text-rendered comparison repeats the same features for both tiers; visual disabled states may be lost. Do not infer that all Pro features are free. Pluralsight publicly lists 31 hours, ten courses and seven labs, including material beyond entry-level WDE; these are provider totals, not a prescription to complete the whole path. MDN, WAI and web.dev index review does not imply completion of their linked lessons.

No exact current MeasureUp or Whizlabs WDE-40-01 product was verified. Confirm the exact WDE-40-01 practice product and its terms if practice questions are useful, and reject sources that do not identify the active version or question provenance.
