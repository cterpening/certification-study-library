---
exam_code: MO-111
vendor_id: microsoft-office
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/mos-word-expert-m365-apps/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-28
---

# MO-111 Microsoft Word Expert (Microsoft 365 Apps) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** This guide follows the live MO-111 scope checked September 28, 2026. It is unofficial and may contain errors. The [official MO-111 page](https://learn.microsoft.com/en-us/credentials/certifications/mos-word-expert-m365-apps/) is authoritative.

**Assessment contract:** 50-minute proctored practical assessment; about 150 hours of advanced hands-on use is Microsoft preparation guidance.<br>
**Current scope:** document options/settings; advanced editing/formatting; custom elements; advanced Word features.<br>
**Change watch:** No retirement or replacement is listed on the credential page, checked September 28, 2026. The current [Microsoft expiration policy](https://learn.microsoft.com/en-us/credentials/support/credential-expiration-policy) gives MOS a five-year lifetime; check the dates on your earned credential.<br>
**Detailed coverage:** All 47 tasks in the [three-page skills PDF](https://arch-center.azureedge.net/Learning/Credentials/MO-111_OD_MOS365_WordExpert.pdf) are mapped in the [review report](../docs/research/2026-09-28-mo-111-deep-review.md). The automatic page monitor covers four broad domains. No desktop Word lab was executed during this review.

## How to use this guide

Expert work is systems work: reusable templates, durable styles, controlled sections, dynamic fields, automated bulk output, and safe review. Practice long documents in copies so you can diagnose field, section, protection, and automation failures without losing evidence. The current credential page lists ten exam languages and no dedicated Learn training collection. Use the desktop application and confirm the testing center’s environment; a web workflow or an Insider feature is not proof of exam availability. All study-time estimates below are suggested practice budgets, not provider runtimes.

> **About related items:** A `Related item:` callout adds architecture, governance, or troubleshooting context. It is supporting knowledge, not a claim that its wording is in the published objectives.

## Objective map

| Published domain | Working question |
|---|---|
| Manage document options and settings (20–25%) | Can the file be prepared, protected, navigated, and delivered for a specialized audience? |
| Use advanced editing and formatting features (20–25%) | Is complex structure reusable and stable as content changes? |
| Create custom document elements (20–25%) | Can templates, styles, building blocks, indexes, and references be maintained centrally? |
| Use advanced Word features (25–30%) | Can forms, mail merge, fields, macros, and collaborative controls produce verified output? |

## 1. Document options and settings

Configure themes, style sets, defaults, properties, templates, compatibility, language, hyphenation, line numbering, pagination, and print/export behavior. Use sections for distinct headers, footers, numbering, columns, orientation, or page setup; control Link to Previous explicitly.

Restrict formatting/editing, mark final, and use document inspection according to the actual control requirement. Protection influences editing behavior but does not replace storage permissions, encryption, records controls, or a retained source copy. Create reusable templates without overwriting the master with case-specific data.

A template defines the starting environment, but an existing document is its own artifact. To change a template, open that template for editing and save a new version; creating a document from it does not edit the master. Changes to [Normal.dotm](https://support.microsoft.com/en-us/word/change-the-normal-template-normal-dotm), including its default font, apply to future documents based on it. Preserve a copy of custom templates before a practice change. Keep a template containing macros in a macro-enabled format, and distinguish that template from a macro-enabled document.

Customize the Quick Access Toolbar with the commands the task requires, and expose hidden tabs such as Developer through ribbon customization. Check whether a customization belongs to the application, a document or a template before relying on it on another machine. Editing/proofing language controls language-specific assistance and hyphenation; display language controls the interface. Neither setting translates existing text.

Version history, comparison and combination solve different problems: history retrieves a saved revision where the storage system supports it; comparison shows differences; combination consolidates reviewers' revisions. A link to external content retains a dependency on its source, unlike a pasted copy. Test refresh behavior with the source available and unavailable, and decide which form the recipient needs. A password to open a file differs from editing restrictions inside it; verify the specific requested operation.

## 2. Advanced editing and formatting

Use advanced Find/Replace for styles, formats, fields, special characters, and patterns; prove the scope before replacement. Define multilevel lists linked to heading styles. Control pagination through section/page breaks, Keep settings, widow/orphan control, and table-row behavior.

Manage styles by inheritance: base style, following style, priority, visibility, and direct-formatting exceptions. Use columns, tabs, leaders, drop caps, text direction, and linked text boxes deliberately. Sort lists/tables and perform calculations only after confirming data type and range.

> **Related item:** A long document is maintainable when meaning drives formatting. If every heading is merely bold 16-point text, navigation, automatic contents, outline numbering, and global revision all become fragile.

Word wildcard patterns are not general-purpose regular expressions. Enable the appropriate search mode, test on a copy, inspect several matches and check formatting/style criteria separately. After replacing, verify both the replacement count and nearby text. Choose an insertion point deliberately before using [paste options](https://support.microsoft.com/en-us/word/control-the-formatting-when-you-paste-text): preserving source formatting, adopting destination characteristics, retaining text only, and pasting a picture produce different editable results. Plain-text paste can still preserve list markers according to the application's settings.

Create and modify paragraph, character and table styles separately. Use the style Organizer to copy a named style into the required document/template and confirm the destination before overwriting a same-named style. Test it on representative content: transferring a style definition does not itself prove all intended paragraphs now use it. Hyphenation and line numbering are layout controls; they do not replace paragraph pagination rules.

## 3. Custom document elements

Create, modify, organize, and reuse custom styles, templates, themes, Quick Parts/building blocks, AutoText, headers/footers, and content controls. Understand whether an element lives in the document, its attached template, or another template so it travels and updates as intended.

Build and update tables of contents, figures, authorities, citations/bibliographies, captions, cross-references, indexes, bookmarks, and fields. Mark entries consistently, choose formats/options, then update all fields before output. Field codes and results are distinct; locking a field prevents an accidental update but can also leave stale output.

For Quick Parts, save the selected reusable content with a recognizable name, gallery/category and intended template. Retrieve it into a second document to prove it is available there. Custom color/font sets feed a theme; a style set coordinates styles. Change one layer at a time and inspect text with direct formatting, which may not follow the expected theme change.

An index is built from marked entries, not from a table of contents. Mark a main entry and a subentry, insert the index, move the source text and update the index. Captions supply the labels and numbering for tables of figures: distinguish a figure label from a table label and verify the corresponding generated list. Maintain bibliography source records, insert citations tied to them and then generate the bibliography; editing typed citation text is not equivalent to correcting its source record.

## 4. Advanced features

Mail merge separates main document, data source, field mapping, filtering/sorting, rules, preview, and final merge. Validate several records—including blank and long values—before producing all labels, envelopes, email, or documents. Never send directly until recipients and individualized fields have been checked.

Build forms with content controls, properties, instructional text, grouping, and protection that permits intended entry. Record or run a macro only in a trusted file and understand what range/selection assumptions it makes. Use compare/combine, tracked changes, comments, coauthoring, and version control without confusing a hidden view with accepted changes.

Insert a field through Word's field command rather than typing characters that merely look like field braces. Review its code, properties and displayed result. Content controls need appropriate types, titles, default instructions and allowed choices; locking the control against deletion is a different requirement from preventing edits to its contents. Test entry after applying protection.

[Field updates](https://support.microsoft.com/en-us/word/update-fields) need verification. Ctrl+A then F9 is useful, but Microsoft notes that tables containing fields/formulas may need separate selection and F9. Inspect headers, footers, cross-references and generated lists in their own context. A deleted bookmark must be repaired; refreshing cannot reconstruct the missing reference. [Word table formulas](https://support.microsoft.com/en-us/word/use-a-formula-in-a-word-table) are fields, so do not assume spreadsheet-style continuous recalculation. Table calculations are useful supporting practice, not a separately named MO-111 objective.

For [macro practice](https://support.microsoft.com/en-us/word/create-or-run-a-macro), choose an unambiguous name and the intended storage document/template before recording. Record a harmless formatting operation, stop recording, inspect or edit the simple procedure, then copy it with Organizer to a second disposable template. Keyboard selection can be recorded; mouse selection is not captured by the recorder. Confirm the target selection before each run. Word for the web cannot run the desktop VBA workflow.

[Internet-origin macros are blocked by default in supported Office on Windows](https://learn.microsoft.com/en-us/microsoft-365-apps/security/internet-macros-blocked). A macro-enabled extension does not grant permission to execute. Use a locally authored exercise and follow the organization's approved trust policy; a blocked downloaded file is not evidence that the recorded procedure is incorrect. No blanket macro-enablement change is required for learning this distinction.

Prepare [merge data](https://support.microsoft.com/en-us/word/prepare-your-excel-data-source-for-a-word-mail-merge) before connecting it: clear headers, one record per recipient, consistent types and postal identifiers imported as text. Changing the format after zeros were discarded does not recover the original identifier. Apply filters, inspect missing values and [preview individual recipients](https://support.microsoft.com/en-us/word/mail-merge-preview-results). Finish into documents first. For labels, verify record progression rather than repeating the first recipient in every position; for envelopes, inspect address placement and paper size.

### Useful article and its limits

Ali Forelli's [paste-default article, originally published May 7, 2024](https://techcommunity.microsoft.com/blog/microsoft365insiderblog/updated-default-paste-option-in-word-for-windows/4225168/), explains why Merge Formatting helps when pasting from other programs. Its Windows 2405/build 17624.20000 boundary and configurable setting are historical feature context, not a claim that every workstation has the same default. Use the current support reference for detailed list behavior: its default text-only paste can preserve bullets/numbers, qualifying the article's broader simplification. Try all three text-paste choices on the same synthetic source and compare editable output.

## Worked examples

1. **A template repair seems to disappear.** A learner creates a new report from a template and changes its font. The next new report remains unchanged because the master was never edited. Open the correct template, change its definition, save it, then create a fresh document to verify the result. Preserve any report-specific exceptions deliberately.
2. **Pasted content carries unexpected formatting.** A browser paragraph contains emphasized words and a table. Compare source formatting, merged formatting and text-only paste at the same destination. Inspect styles, retained emphasis, table editability and list settings; an attractive result alone does not prove the requested structure survived.
3. **A field pass leaves an incorrect total.** A supporting table contains 120, 80 and 50; its sum should be 250. Change 80 to 100; the expected total becomes 270. Refresh the table's field and inspect the result rather than assuming it recalculated immediately. Separately repair a cross-reference whose bookmark was deleted.
4. **A merge produces too many letters.** A six-record source has one inactive recipient and one active record with an invalid address. Four records remain eligible after those two independent exclusions. Preview all four, including one with a blank optional title, and verify four recipient identities in the output. Count recipients rather than pages because a long letter can span pages. No email is sent in this exercise.
5. **A macro exists but cannot be used elsewhere.** A procedure stored in one document does not automatically belong to every template. Copy it into the intended practice template, preserve a macro-enabled format, then confirm both its availability and permitted execution. Repeating a run with a different selection tests its assumptions, not merely whether a button exists.

## Integrated practice scenarios

1. **Policy manual:** Create a template, linked outline numbering, section-specific headers, contents, figures, index, cross-references, and protected final output.
2. **Contract pack:** Use content controls and building blocks, compare revisions, limit editing, inspect metadata, and retain clean/review copies.
3. **Personalized letters:** Clean a recipient source, apply conditional merge rules, preview exception records, merge to documents, and verify totals/output.

## Hands-on labs

These are proposed desktop exercises using synthetic records and disposable copies.

| Lab | Task | Completion evidence |
|---|---|---|
| 1 | Edit a template's defaults, theme, style set and building blocks; customize a toolbar and expose Developer | A newly created document gets the intended defaults; the original practice template remains recoverable |
| 2 | Repair wildcard replacements, style inheritance, outline numbering, hyphenation, pagination and section links | Match counts and representative before/after text agree; styles copied into another template are available there |
| 3 | Build an index, figure/table captions, generated figure list, citations and bibliography | Moving content and changing source records produces correct regenerated output |
| 4 | Build a form with several standard control types, field properties and suitable protection | Intended entries work, invalid choices are constrained, and required controls cannot accidentally be removed |
| 5 | Filter and merge recipients with blank/long values and textual postal codes into letters, labels and envelopes | Eligible identities and output totals reconcile; address layout and record progression are verified |
| 6 | Compare two revisions, combine reviewers, manage versions and test a link to external content | The source dependency and review trail are understood; final changes are deliberately accepted/rejected |
| 7 | Record, name, edit and copy a simple formatting macro into a disposable template | Correct storage and selection are demonstrated; no global trust-policy relaxation is needed |
| 8 | Inspect fields, table calculations, metadata, accessibility, compatibility and PDF output | A changed input yields the expected displayed value after refresh; no unresolved reference errors remain |
| 9 | Configure separate editing/display language settings and test language-specific behavior in a mixed 50-minute task | Proofing behavior, interface choice and actual document text are distinguished; delivery checks fit the time budget |

## Original readiness checks

1. Why link list levels to heading styles? 2. What does Link to Previous affect? 3. Template versus document? 4. Field code versus result? 5. Why update fields before output? 6. What can locked fields cause? 7. Why preview several merge records? 8. Main document versus data source? 9. What does restricting editing not provide? 10. Why retain the template master? 11. What is a building block? 12. Why organize styles? 13. Compare versus combine? 14. What does hiding markup do? 15. Why test macro selection assumptions? 16. What makes a form usable? 17. What creates an index? 18. Why inspect section boundaries? 19. What should document inspection precede? 20. What proves expert readiness?

### Answer guide

1. Numbering then follows document structure. 2. Headers and footers across section boundaries. 3. A reusable starting system versus one content instance. 4. Instruction versus displayed value. 5. To remove stale references, contents, dates, and numbering. 6. Stale output. 7. Blanks, lengths, rules, and mapping fail differently. 8. Layout/rules versus recipient records. 9. A full security or access-control boundary. 10. To avoid case-specific contamination. 11. Reusable formatted content stored in a gallery/template. 12. Predictable reuse, navigation, and maintenance. 13. Differences between versions versus consolidated reviewers' revisions. 14. Only the view; revisions remain. 15. A macro may change the wrong content. 16. Clear controls, order, instructions, and appropriate protection. 17. Marked entries plus an inserted/updated index field. 18. They govern layout and header/footer behavior. 19. External delivery. 20. Building and repairing reusable, dynamic documents under time with verified output.

### Additional answer checkpoints

21. **Does changing a document change its template?** Not automatically; edit and save the intended template definition.
22. **What does changing Normal.dotm affect?** Defaults of future documents based on it, not an automatic repair of every existing document.
23. **Does changing the display language translate the document?** No; interface language and document text are separate.
24. **Why verify the style-copy destination?** A same-named style in the wrong document/template does not meet the requirement.
25. **Does text-only paste always remove list markers?** No; current Word settings can preserve bullets/numbers.
26. **Does F9 fix a deleted bookmark?** No; restore or retarget the reference before refreshing.
27. **What is the expected total after changing 80 to 100 in a 120/80/50 table?** 270; confirm the field result after updating.
28. **Does a macro-enabled extension make a macro trusted?** No; storage format and execution policy are separate.
29. **Are mouse selections recorded by Word's macro recorder?** No; use the supported keyboard selection workflow and test it.
30. **Can a postal-code display format recover lost digits?** No; retain the original text during import or recover it from the source.
31. **Why reconcile recipient IDs instead of page count?** Letters can have different lengths, so pages do not measure the number of intended recipients.
32. **Is a standalone Word Expert certification the same as a multi-application MOS Expert credential?** No; check the specific credential's requirements rather than inferring the aggregate award from one exam.

## Readiness checklist

- I can repair styles, numbering, fields, and sections in an unfamiliar long document.
- I understand where templates, building blocks, and macros are stored.
- I preview and reconcile mail-merge output before release.
- I can preserve review evidence while producing a clean final document.
- I complete mixed advanced tasks inside 50 minutes with a field/output inspection pass.

## Places to learn

This is a selective learning path, not a complete list of Word Expert resources.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official MO-111 page](https://learn.microsoft.com/en-us/credentials/certifications/mos-word-expert-m365-apps/) | Public | **20 minutes** for scope and logistics |
| [Microsoft Word help and learning](https://support.microsoft.com/en-us/word) | Public | **12–18 hours** for advanced targeted practice |
| Nine labs in this guide | Microsoft 365 Apps required | **12–18 hours** plus two timed repeats |
| [Detailed skills PDF](https://arch-center.azureedge.net/Learning/Credentials/MO-111_OD_MOS365_WordExpert.pdf) | Public; task-by-task planning | **30–45 minutes** |
| Microsoft task references linked above | Public; focused task practice | **3–4 hours**, included in targeted practice above |
| [Ali Forelli’s paste article](https://techcommunity.microsoft.com/blog/microsoft365insiderblog/updated-default-paste-option-in-word-for-windows/4225168/) | Public; bounded historical workflow explanation | **15 minutes** plus a comparison exercise |
