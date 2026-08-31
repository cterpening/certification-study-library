# Accessibility review

The Certification Study Library aims for WCAG 2.2 AA-compatible presentation while recognizing that automated tools cannot prove complete accessibility. Accessibility review is evidence-based and repeated when the theme, navigation, search, templates, or visual system changes.

## Automated baseline

On August 31, 2026, the deployed homepage was tested in a mobile Lighthouse profile using headless Microsoft Edge. The recorded scores were:

| Category | Score |
|---|---:|
| Accessibility | 100 |
| Best practices | 100 |
| SEO | 100 |
| Performance | 99 |

The same run measured first contentful paint at 1.1 seconds, largest contentful paint at 1.7 seconds, cumulative layout shift at 0, and total blocking time at 120 milliseconds. These values are a point-in-time diagnostic, not a performance guarantee.

The production build's GH-300 long-guide page was also sampled in the mobile profile after adding the guide-start panel and source-validation presentation. Its automated accessibility, best-practices, and SEO scores were each 100. That audit identified and drove fixes for syntax-token contrast, link distinction within prose, and accessible names on generated readiness-checklist controls before release.

Repository validation also checks generated links, and the site uses semantic navigation landmarks, a skip link supplied by the theme, visible focus styling, reduced-motion handling, responsive layouts, dark/light themes, and print-specific CSS.

## Manual review checklist

The following checks require a person using the rendered site. Record the browser, operating system, assistive technology, date, pages sampled, and observed result when completing them.

- [ ] Complete the entire header, navigation, search, theme toggle, guide table of contents, copy buttons, and footer path using only the keyboard.
- [ ] Confirm focus order matches visual and reading order and focus never becomes trapped or invisible.
- [ ] Use NVDA or another supported screen reader to inspect the homepage, catalog, one short guide, and one long guide.
- [ ] Confirm headings, landmarks, tables, admonitions, code blocks, links, and status labels are announced meaningfully.
- [ ] Test browser zoom at 200% and 400% without loss of content or two-dimensional scrolling except where a table or code block requires it.
- [ ] Test representative widths around 320, 768, 1024, and 1440 CSS pixels in both themes.
- [ ] Confirm information is never distinguished by color alone and that focus, text, links, badges, and controls retain sufficient contrast.
- [ ] Print or save a long guide to PDF and verify headings, links, tables, code, page breaks, and hidden navigation.
- [ ] Test with reduced motion enabled and confirm decorative transitions do not interfere with navigation.

Do not mark the project roadmap's manual accessibility item complete until the keyboard, screen-reader, zoom, responsive, contrast, and print evidence is recorded here.

## Reporting a problem

Use the repository's content-correction issue form for an accessibility defect. Include the affected URL, browser or assistive technology, steps to reproduce, expected result, and observed result. Do not include private information in a public issue.
