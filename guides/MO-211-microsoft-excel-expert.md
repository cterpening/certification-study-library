---
exam_code: MO-211
vendor_id: microsoft-office
official_blueprint: https://learn.microsoft.com/en-us/credentials/certifications/mos-excel-expert-m365-apps/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-10-28
upcoming_change_status: none-announced
upcoming_change_checked: 2026-10-28
---

# MO-211 Microsoft Excel Expert (Microsoft 365 Apps) Study Guide

> **Independent AI-assisted resource — HUMAN REVIEW PENDING.** The October 28, 2026 team refresh reconciles this complete guide and detailed objectives with current public exam, product and learning evidence. See the [current group report](../docs/research/2026-10-28-microsoft-refresh-group-05.md#mo-211) and [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#mo-211-coverage-record). Source limits and unexecuted exercises remain explicit. This is not human review or live product validation. The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/mos-excel-expert-m365-apps/) is authoritative.

**Assessment:** 50 minutes, proctored; the current page lists seven languages. Approximately 150 hours of instruction and hands-on experience is preparation guidance, not a formal prerequisite. The page has no dedicated Microsoft Learn training collection.<br>
**Lifecycle:** No retirement or replacement notice found on October 28, 2026. The credential shows a 60-month renewal frequency; read the [current MOS expiration policy](https://learn.microsoft.com/en-us/credentials/support/credential-expiration-policy) for applicability to your award date. Exam retirement and credential expiration are different events.

## How to use this guide

> **About related items:** Supplementary tools deepen understanding without adding requirements to the published exam outline.

Start with a copy of a small workbook. Predict the answer, perform the task, then change an input and prove the result remains correct. Practice on your target desktop build. UI paths and feature availability can vary; the proposed labs below have not been executed in Excel. Local calculations check the examples' expected arithmetic, dates, ordering and totals only.

**Detailed objective source:** The [official MO-211 detailed skills outline](https://arch-center.azureedge.net/Learning/Credentials/MO-211_OD_MOS365_ExcelExpert.pdf) supplies the individual assessed tasks; the credential page gives the broader domains.

**VERIFY CURRENT — practice platform:** Confirm the testing center's exact delivery/build before scheduling. For Compass Cloud: In-Center, Certiport's October 22, 2026 candidate guide says MOS Live-in-the-App exams run in a Windows VM even when the client is a Mac or Chromebook. This does not establish that every center uses Cloud. Mac and web product practice can teach concepts, but it does not establish parity with the assessed Windows workflow. Keep the platform boundaries beside each task. See [Certiport candidate platform guidance](https://certiport.pearsonvue.com/Support/Install/Compass-Cloud/Test-Candidate/CC_Guide_TestCandidate). The public [MOS Microsoft 365 Apps interface tutorial](https://certiport.pearsonvue.com/Educator-resources/Exam-details/Exam-tutorials/MOS_365Apps_Tutorial.pdf) distinguishes exam controls from ordinary application practice: some commands, including Encrypt with Password, are disabled in the exam environment. Local product exercises below are learning tasks, not a promise of the available exam UI or actual assessment items.

## Objective map

| Domain | Weight | Practice outcome |
|---|---:|---|
| Workbook options and settings | 10–15% | Deliver a controlled workbook with understood dependencies |
| Data management and formatting | 30–35% | Generate, validate, summarize and flag data accurately |
| Advanced formulas and macros | 25–30% | Explain calculation behavior and automate a bounded task |
| Advanced charts and tables | 25–30% | Reconcile and present refreshable analysis |

## 1. Workbook options and settings

Use a separate source and destination workbook to practice external references. Identify the source file, worksheet and cell; compare values before and after a source edit. A displayed cached value is not evidence that the source was refreshed. Manage versions by saving a checkpoint and, where supported by storage/account settings, inspecting version history before restoring a copy.

Unlock intended input cells, configure allowed ranges/actions, then protect the worksheet and test both permitted and forbidden edits. Protecting workbook **structure** controls sheet operations; it does not replace worksheet protection or file access controls. Neither is encryption. Keep formulas locked where the editing requirement calls for it.

Configure calculation mode deliberately. After changing an input in Manual mode, trigger calculation and verify dependent outputs. A strikethrough may identify a stale formula value on supported builds. Turning off **Format Stale Values** hides that indication; it does not calculate anything. External-source values and formulas dependent on Data Table cells have documented gaps in this indication, so the absence of a warning is not proof of freshness. See [current stale-value guidance](https://support.microsoft.com/en-US/Excel/stale-value-formatting).

Enable only locally created or otherwise verified macros within the environment's policy. Retain VBA in `.xlsm` or `.xlsb`; saving as `.xlsx` does not preserve it. To reuse a macro, open both files and copy its module through the Visual Basic Editor's Project Explorer. Inspect references to the original workbook before running the copy. A copied module can exist while execution remains blocked by policy. See [Microsoft's module-copy instructions](https://support.microsoft.com/en-us/excel/copy-a-macro-module-to-another-workbook).

## 2. Manage and format data

Use **Flash Fill** for a recognizable transformation, then check exceptional rows: its output is static, not a live formula. Compare linear, growth and date series through the Fill Series dialog. With [RANDARRAY](https://support.microsoft.com/en-us/excel/functions/randarray-function), specify dimensions, bounds and integer/decimal output: `=RANDARRAY(4,2,1,6,TRUE)` requests eight random integers in a 4-by-2 spill. Expect repeats; do not treat generated values as unique keys. For reproducible practice evidence, retain a values-only copy with its generation settings.

Custom number formats alter display, not the stored value: `00000` displays numeric 123 as 00123, but cannot restore information lost on import. Practice positive/negative/zero/text sections, then inspect the formula bar. Configure validation type, limits, input message and error alert. **Stop** blocks invalid direct entry; Warning/Information permit override. Copy/fill, formula results and macros can bypass entry alerts. Use [Circle Invalid Data](https://support.microsoft.com/en-US/Excel/display-or-hide-circles-around-invalid-data) to find existing violations; clearing circles does not repair them.

Group/ungroup rows or columns and expand/collapse the outline without deleting detail. For the Subtotal command, sort a normal range by its grouping key before inserting subtotals; convert a table to a range when necessary. Choose the right function and reconcile grand totals. Removing duplicates deletes rows according to the **selected key columns**: compare those keys and keep a backup before removal.

Create custom conditional rules, including formulas. Write the condition for the top-left cell of **Applies to** and reason through each `$` anchor. Inspect rule order, overlapping ranges and **Stop If True**. Test a boundary value and a second row; one correctly colored cell is insufficient. Example 2 shows a rule that highlights complete records.

## 3. Advanced formulas and macros

### Logic, criteria and lookup

The PDF names `IF`, `IFS`, `SWITCH`, `SUMIF`, `AVERAGEIF`, `COUNTIF`, `SUMIFS`, `AVERAGEIFS`, `COUNTIFS`, `MAXIFS`, `MINIFS`, `AND`, `OR`, `NOT` and `LET`. Practice each family deliberately:

- Use IF for two branches, ordered IFS tests for the first true branch, and SWITCH to select by a value. Provide a deliberate fallback. AND requires every condition; OR requires any; NOT reverses a logical result.
- Single-criterion and multiple-criterion aggregates have different argument orders. For example, SUMIF begins with the criteria range, while SUMIFS begins with the sum range. Match corresponding range dimensions and include boundary/empty-result cases.
- Use LET to name a repeated expression locally, then return the final calculation: `=LET(net,B2-C2,IF(net>=0,net,0))`. The name improves readability; it does not create a workbook-level defined name.

The required lookup set is `XLOOKUP`, `VLOOKUP`, `HLOOKUP`, `MATCH` and `INDEX`. Explicit `FALSE` in VLOOKUP/HLOOKUP and `0` in MATCH request exact matching. Positional VLOOKUP column indexes can become wrong after structural changes; INDEX with MATCH separates the returned range from the match search. Approximate legacy lookups require suitable ordering and a justified interval rule.

[XLOOKUP](https://support.microsoft.com/en-us/excel/functions/xlookup-function) defaults to exact matching and a forward search. Reverse search selects the last matching row; it does not establish which record is authoritative. Match mode and search mode are separate arguments. Binary search requires appropriately sorted lookup data. Use an explicit not-found outcome and test duplicates; see Example 1.

### Worked logic and legacy lookup checks

Reuse Example 2's four records (amounts **120, 80, 200, 60**). Add `=COUNTIF(A2:A5,"East")` → **3**, `=AVERAGEIF(A2:A5,"East",C2:C5)` → **260/3**, and `=SUMIF(A2:A5,"East",C2:C5)` → **260**. The existing multi-criterion example narrows this to East/Open and **180**. On row 2, compare `=IF(AND(A2="East",NOT(B2="Closed")),"Queue","Skip")` → **Queue** with `=IF(OR(A2="West",C2>=200),"Escalate","Routine")` → **Routine**. Copy down and explain why row 4 escalates. Use `=IFS(C2>=200,"High",C2>=100,"Mid",TRUE,"Low")` → **Mid**; reverse those first two tests and show why 200 could be classified too early. `=SWITCH(B2,"Open","Queue","Closed","Archive","Review")` → **Queue**. Retain the LET example above and combine the locally named calculation with a logical gate; its name should not appear as a workbook defined name. See [logical-function decisions](https://support.microsoft.com/en-us/excel/logical-functions-reference), [nested IF/AND/OR/NOT](https://support.microsoft.com/en-us/excel/using-if-with-and-or-and-not-functions-in-excel) and [criteria aggregate reference](https://support.microsoft.com/en-us/excel/statistical-functions-reference?ad=us&rs=en-us&ui=en-us).

On another worksheet put unique keys A/B/C in A2:A4 and amounts **10/20/30** in B2:B4. `=VLOOKUP("B",A2:B4,2,FALSE)` and `=INDEX(B2:B4,MATCH("B",A2:A4,0))` both return **20**; `=MATCH("B",A2:A4,0)` returns **2**, a position rather than an amount. Put A/B/C across E1:G1 with **10/20/30** below; `=HLOOKUP("B",E1:G2,2,FALSE)` returns **20**. Replace B with a missing key and inspect the error; use the explicit not-found argument for the existing XLOOKUP version. For approximate practice, use ascending thresholds **0/50/100** with band labels **Low/Mid/High**; a VLOOKUP with TRUE for **75** should select **Mid**, while a below-minimum value has no interval. Shuffle the thresholds to demonstrate why ordering matters, then restore them. See [legacy lookup orientation, exact matching and INDEX/MATCH](https://support.microsoft.com/en-us/excel/look-up-values-with-vlookup-index-or-match?trk=article-ssr-frontend-pulse_little-text-block).

### Dates, analysis and arrays

Use TODAY for the current date and NOW for date/time; their results change when recalculated and should not be used as immutable entry timestamps. WEEKDAY's return-type argument determines the numbering convention. [WORKDAY](https://support.microsoft.com/en-us/excel/functions/workday-function) offsets by working days, excluding Saturday/Sunday and supplied holiday dates. Store real dates, not ambiguous date strings; document the holiday list. Custom-weekend WORKDAY.INTL is related knowledge, not a separately named function in this outline.

Use **Consolidate** to summarize multiple ranges: consolidate by position only when layouts align; choose labels/categories when the same items occupy different rows. Identify whether the output links to source data or represents a snapshot. **Goal Seek** adjusts one input to meet one formula target; **Scenario Manager** stores alternative input sets. Sensitivity Data Tables are useful supplementary practice; they are not separately named in this PDF.

### Worked consolidation and what-if analysis

On two sheets, create Item/Amount lists: North has **A/10, B/20** and South has **B/7, A/3**. In a clear destination, Data → Consolidate → Sum, add both source ranges including labels and select Top row/Left column. Expect **A 13, B 27, grand total 40**. Without category labels, positional combination would pair unlike rows and produce **17/23**. Choose deliberately whether to create links to source data. Change South's A amount to **5**: expected recomputed results are **A 15, B 27, total 42**; a snapshot requires rerunning consolidation. See [source-range and label configuration](https://support.microsoft.com/en-us/excel/consolidate-data-in-multiple-worksheets).

In a separate model put units **20** in B2, price **10** in B3 and `=B2*B3` in B4. Use Data → What-If Analysis → Goal Seek: Set cell **B4**, To value **300**, By changing cell **B2**. Expect units near **30**, then verify B4 and retain/restore the result deliberately. A changing cell that the target formula does not use cannot solve this relationship. See [Goal Seek input and formula contract](https://support.microsoft.com/en-au/excel/use-goal-seek-to-find-the-result-you-want-by-adjusting-an-input-value).

Use Scenario Manager to save **Base** with changing cells B2:B3 = **20/10** and **Stretch** = **30/12**. Show each and expect revenue **200** and **360**. Generate a scenario summary using B4 as the result cell. Change a scenario and regenerate the summary: the earlier summary is static. These are saved assumptions, not forecasts established by the tool. See [scenario input sets and static summary reports](https://support.microsoft.com/en-us/excel/switch-between-various-sets-of-values-by-using-scenarios).

[PMT](https://support.microsoft.com/en-us/excel/functions/pmt-function) solves a constant periodic payment; [NPER](https://support.microsoft.com/en-us/excel/functions/nper-function) solves the number of periods. Use consistent rate/payment units, opposite cash-flow signs for borrowing and repayment, and the correct beginning/end-of-period setting. The PDF's forecasting objective names AND, IF and NPER: gate assumptions with logical conditions, then evaluate the period estimate. These are model calculations, not predictions of future interest rates. Example 4 isolates sign and unit behavior with a zero-rate model.

[FILTER](https://support.microsoft.com/en-us/excel/functions/filter-function) selects records using a same-sized Boolean include array. Supply `if_empty` for no matches; this does not suppress errors already present in the include array. [SORTBY](https://support.microsoft.com/en-us/excel/functions/sortby-function) orders a returned array by corresponding keys, including keys outside its returned columns. Match dimensions and use 1/-1 for ascending/descending. Both spill results into free cells; put spill formulas outside Excel Tables. Linked dynamic arrays have limited support across workbooks and require both workbooks open when refreshed. Sorting a returned array does not rearrange source records.

### Audit and automate

Trace **precedents** to inputs and **dependents** to affected outputs. Use the Watch Window while navigating elsewhere, inspect error-checking warnings, and step through Evaluate Formula to locate the first incorrect intermediate result. Recheck calculation mode, reference movement and data types before replacing a formula with a hard-coded answer.

### Worked formula diagnosis

On a disposable Windows desktop sheet enter numeric **100** in B2, **0.1** in C2 and the deliberately wrong formula `=B2+C2` in D2. The required result is a 10% increase, **110**, but the formula gives **100.1**. Select D2 → Formulas → Trace Precedents to inspect B2/C2; select B2 → Trace Dependents to find D2. Add D2 through Watch Window → Add Watch, navigate elsewhere and change B2 to **200**; watch the wrong result **200.1**. Return to D2 and use Evaluate Formula to step through the expression before repairing it to `=B2*(1+C2)`; expect **220**. Remove tracer arrows/watches after preserving evidence. The [tracer guidance](https://support.microsoft.com/en-us/excel/display-the-relationships-between-formulas-and-cells) bounds untraceable objects and closed external workbooks.

Next enter `=B2/0` in E2. Enable the relevant formula-error checking rule, run Formulas → Error Checking and inspect the cause rather than selecting Ignore Error as a repair. Correct the denominator according to a stated requirement and recalculate. The first wrong example may have **no** error warning: a syntactically valid formula can implement the wrong business operation. [error rules, Watch Window and Evaluate Formula](https://support.microsoft.com/en-us/excel/detect-formula-errors-in-excel) describes the Windows evaluation workflow and separate Mac settings. These are expected states for local reproduction, not captured Excel results.

Record a small formatting macro with a meaningful name such as `FormatInputCells`. Stop recording before unrelated actions. Compare absolute references with relative recording from a different start cell. In the editor, inspect and change a simple formatting instruction, then rerun on a disposable copy. Test assumptions about active workbook/sheet, selection and range size. Copying code and enabling execution are separate operations; format, signature or a familiar filename alone does not establish trust.

## 4. Advanced charts and tables

Choose the analytical relationship before the chart: Combo mixes series types; a labeled secondary axis handles differing units; Box & Whisker compares distributions; Histogram shows frequencies; Funnel represents stages; Sunburst shows hierarchy; Waterfall explains contributions to a running total. Edit data/series, titles, labels and scale, then explain what would mislead a reader if an axis or total marker were wrong.

### Worked advanced-chart workbook

Use separate synthetic source sheets, select each complete labeled range and insert the intended chart; save the editable workbook, not just screenshots. Use Chart Design → Change Chart Type to modify the selected chart and inspect the result. The [chart-type reference](https://support.microsoft.com/en-us/excel/available-chart-types-in-office) supplies the analytical distinctions; [chart creation/data controls](https://support.microsoft.com/en-us/excel/creating-charts-from-start-to-finish) supports the shared editing workflow.

| Source and operation | Expected artifact and failure check |
|---|---|
| Jan/Feb Units **100/150**, Rate **10%/20%**; create a Combo using columns for Units and a line for Rate on a secondary axis | Two clearly labeled units/percent axes; confirm Rate remains 0.1/0.2 rather than 10/20 |
| Team A observations **3,4,5**, Team B **6,7,8**; create Box & Whisker and modify its display options | Two distributions with medians **4** and **7**; raw observations remain available, not pre-aggregated totals |
| Observations **1,1,2,3,3**; insert Histogram and change its bin width | Frequencies across all displayed bins still account for **five** observations; different widths change the grouping, not the source count |
| Stages **Contacted/Qualified/Selected**, counts **100/60/20**; insert Funnel and edit the last source count to **25** | Ordered stages and revised last-stage value, without interpreting widths as independent probabilities |
| Region/City/Amount: **East/A/20, East/B/30, West/C/40**; insert Sunburst | Nested parent/child rings and total **90**; swapping the two hierarchy columns changes meaning and must be deliberate |
| Opening **100**, Increase **30**, Decrease **-10**, Closing **120**; insert Waterfall, treating opening/closing as totals | Closing value **120**, with the negative movement lowering the running amount; an ending total must not be counted as an additional contribution |

Change one source value and inspect the selected series/range if the chart stays stale. These are prospective artifact checks, not measured chart-renderer output. Keep specialized charts separate from PivotCharts where type support differs.

Create a PivotTable from a clean rectangular source with a header for each field. Set row/column/filter/value fields and their options explicitly. Numeric fields generally default to Sum; text-containing fields may default to Count. Confirm the chosen aggregation and number format in Value Field Settings. **Show Values As** changes the presentation calculation, such as percent of total; it is distinct from choosing Sum versus Count.

Group date or numeric fields, add slicers and inspect filter connections. Reconcile the filtered population and totals. Refresh after adding source rows and verify the source covers those rows; refresh alone cannot repair a wrong source definition, grain or data type. Create a PivotChart, modify field/filter options and styles, then use supported drill controls to examine hierarchy detail. Record the filters active during drill-down.

For a classic, non-OLAP PivotTable, calculated fields operate on aggregated source fields. That can differ from calculating each source row and then summing it; Example 6 demonstrates the error. OLAP/Data Model features have different calculation mechanisms and restrictions; do not apply classic calculated-field instructions universally. See [Microsoft's PivotTable calculation reference](https://support.microsoft.com/en-us/excel/calculate-values-in-a-pivottable).

### Worked PivotTable and PivotChart navigation

Create a table with **Region, City, Amount** and rows **East/A/100**, **East/B/150**, **West/C/200**. Insert a PivotTable into a clear sheet, put Region then City in Rows and Amount in Values. Set Sum and an appropriate numeric format in Value Field Settings: East should total **250**, West **200**, grand total **450**. Add a Region slicer; select East and check the table/chart population, then clear it. On a separate date-based copy, group valid dates by months and reconcile monthly totals; text or blank date entries need repair before treating a failed grouping as missing functionality.

Create a PivotChart from the PivotTable, choose a column style and apply a built-in chart style. Move Region/City between axis/legend/filter areas and observe the associated PivotTable instead of assuming the chart has an independent source. Right-click an East category label → Expand/Collapse to show cities A/B; collapse it to return to East. Expect **100 + 150 = 250** at either level. Expanding hierarchy levels differs from double-clicking a **PivotTable value**, which can place its contributing source records on a new worksheet. See [platform-specific PivotChart creation](https://support.microsoft.com/en-us/Excel/get-started/create-a-pivotchart) and [chart hierarchy and table value details](https://support.microsoft.com/en-us/excel/expand-collapse-or-show-details-in-a-pivottable-or-pivotchart). On Mac, Microsoft documents creating the PivotTable first and then inserting a supported chart; this is separate from the Windows Insert PivotChart route.

Add **East/A/50** to the source table, refresh and confirm **East 300, grand total 500** with slicers cleared. If the result stays 450, check source extent and refresh; if it is 300, check whether East remains selected. Keep Example 6's classic calculated-field versus row-product exercise separate so a correct hierarchy total does not mask a wrong revenue definition.

## Worked examples

Formulas below use English names and comma separators. Each example has its own worksheet. Expected values were independently calculated locally; Excel execution remains a proposed exercise.

### 1. Duplicate lookup keys

Enter keys `A, B, A` in A2:A4 and amounts `100, 200, 150` in B2:B4. `=XLOOKUP("A",A2:A4,B2:B4,"Missing")` returns **100**; adding `,0,-1` after the not-found argument returns **150**. Looking up C returns **Missing**. Neither lookup gives the total for A: `=SUMIF(A2:A4,"A",B2:B4)` returns **250**. Ask whether the business question requires one record or an aggregate.

### 2. Row rules and multiple criteria

Enter Region, Status, Amount in A1:C1. Rows 2–5 are `East/Open/120`, `East/Closed/80`, `West/Open/200`, `East/Open/60`. `=SUMIFS(C2:C5,A2:A5,"East",B2:B5,"Open")` returns **180**; COUNTIFS with those two criteria returns **2**; AVERAGEIFS returns **90**, MAXIFS **120**, MINIFS **60**. Apply `=AND($A2="East",$B2="Open",$C2>=100)` to A2:C5: only **row 2** qualifies. `$A$2` would incorrectly reuse the first record's region for every row.

### 3. Filter and sort different projections

Use Example 2's records. `=FILTER(A2:C5,(A2:A5="East")*(B2:B5="Open"),"No matches")` returns two complete records in original order, amounts **120 then 60**. In a separate clear output range, `=SORTBY(C2:C5,C2:C5,-1)` returns **200, 120, 80, 60**. Replacing East with North in FILTER returns **No matches**. A blocked destination is a spill-space problem, not proof that the criteria are wrong.

### 4. Payment periods and a feasibility gate

For a hypothetical **zero-interest**, 1,200-unit loan repaid over 12 end-of-month periods, `=PMT(0,12,1200)` returns **-100** and `=NPER(0,-100,1200)` returns **12**. With payment magnitude in B2 and balance in B3, `=IF(AND(B2>0,B3>=0),NPER(0,-B2,B3),"Check inputs")` gives 12 for B2=100/B3=1200 and **Check inputs** for B2=0. For a positive annual rate and monthly payments, use annual rate/12 and a monthly period count. Interest, fees, changing payments and rounding require additional model assumptions.

### 5. Working days

Put September 25, 2026 in A2 as a real date (Friday). Put September 28, 2026 in H2 as a **fictional company closure**, not a claim about a public holiday. `=WEEKDAY(A2,2)` returns **5**. `=WORKDAY(A2,2)` returns **September 29**; `=WORKDAY(A2,2,H2)` returns **September 30**. Adding 2 directly to A2 instead gives **Sunday, September 27**. Format results as dates to see the difference.

### 6. A plausible Pivot total can be wrong

Two source records have Quantity/UnitPrice values `6/10` and `4/20`. The required revenue is **6×10 + 4×20 = 140**. At their combined total, a classic calculated field `=Quantity*UnitPrice` uses **(6+4)×(10+20) = 300**. Add a source Revenue column with each row's product, refresh, and sum that field: **140**. Compare to the independent row calculation before trusting either a PivotTable or its chart. These are different products with different prices, so multiplying total units by summed unit prices has no useful business meaning.

## Hands-on labs

These ten labs are proposed desktop exercises. Keep before/after copies, expected results, actual results and explanations for failures. Study budgets are author suggestions.

| Lab | Task | Completion evidence |
|---|---|---|
| 1 | Set editable inputs, protected formulas and protected structure; test external links, versions and calculation mode | Permitted edits succeed; forbidden edits fail; a changed input is recalculated and reconciled |
| 2 | Compare Flash Fill, linear/growth/date series and RANDARRAY | Static versus recalculated outputs explained; random output dimensions and bounds checked |
| 3 | Combine custom number formats, validation, grouped outlines, subtotals and duplicate removal on copies | Stored values, invalid pasted entries, subtotal population and selected duplicate keys documented |
| 4 | Rebuild Example 2 with rule priority and a boundary amount of exactly 100 | Expected aggregate values and highlighted rows; test below/equal/above threshold |
| 5 | Implement every named logic/criteria function; rebuild lookups with XLOOKUP, VLOOKUP, HLOOKUP and INDEX/MATCH | Duplicate, missing, approximate-boundary and changed-layout outcomes explained |
| 6 | Build FILTER/SORTBY reports and a two-workbook array dependency | Matching/no-match/blocked-spill cases and closed-source behavior recorded |
| 7 | Rebuild date/payment examples; consolidate two aligned and two differently ordered ranges; compare Goal Seek and scenarios | Calendar, units, signs and consolidation method justified; one solved input distinguished from stored input sets |
| 8 | Repair wrong references, stale values and a broken formula using all four audit tools | First bad dependency identified; Watch Window and recalculated output evidence |
| 9 | Record, name, edit and copy a local formatting macro | Correct destination module, retained VBA format, absolute/relative behavior and allowed execution documented |
| 10 | Rebuild Example 6, then create PivotChart, grouping/slicers, drill-down and specialized charts | 140 reconciled total; new source rows included after refresh; chart selection and axis labels explained |

## Original readiness checks and answers

1. **Worksheet versus structure protection?** One controls cell/edit actions; the other controls sheet structure operations.
2. **Why unlock inputs first?** Otherwise protection can block the intended entry cells too.
3. **Does a macro-enabled extension prove safety?** No; it only supports retaining code.
4. **Does copying a module enable it?** No; execution still depends on settings and policy.
5. **Does hiding stale-value formatting calculate cells?** No; trigger calculation and verify outputs.
6. **Does no stale warning prove an external value is current?** No; external sources have documented warning limitations.
7. **Flash Fill versus a formula?** Flash Fill produces static inferred values; formulas can recalculate from inputs.
8. **Does RANDARRAY guarantee uniqueness?** No; random values may repeat.
9. **Does a custom format change the stored number?** No.
10. **Can pasted values bypass validation alerts?** Yes; inspect existing data, including with invalid-data circles.
11. **What determines duplicate removal?** The selected key columns, not necessarily every field.
12. **Why sort before grouped Subtotal insertion?** Equal grouping keys must form the intended contiguous groups.
13. **What anchors a whole-row conditional rule?** Lock its tested columns and allow the record row to move.
14. **What else can change a conditional result?** Rule order, Stop If True and the Applies-to range.
15. **First true IFS branch versus SWITCH?** IFS tests conditions in order; SWITCH compares one expression to candidate values.
16. **SUMIF versus SUMIFS argument order?** SUMIFS starts with the sum range; SUMIF starts with the criteria range.
17. **Is a LET name a workbook defined name?** No; it is local to that formula.
18. **XLOOKUP's default match?** Exact, searching from the first item.
19. **Does reverse XLOOKUP aggregate duplicates?** No; it selects the last matching record.
20. **What does binary lookup require?** Lookup data sorted in the specified direction.
21. **Why specify FALSE/0 in legacy lookups?** To request an exact match rather than unintentionally use approximate behavior.
22. **Can FILTER's if_empty hide a criteria error?** No; it handles no matching records, not errors in include.
23. **Does SORTBY reorder source cells?** No; it returns a separate sorted array.
24. **Can a linked dynamic array reliably refresh with its source closed?** This scenario is unsupported and can yield #REF!.
25. **What does WORKDAY exclude?** Saturday/Sunday and explicitly supplied holiday dates.
26. **Is NOW an immutable entry timestamp?** No; its result changes when recalculated.
27. **PMT versus NPER?** Payment amount versus period count under constant-rate/payment assumptions.
28. **Goal Seek versus Scenario Manager?** Solve one changing input for a target versus compare saved input sets.
29. **Precedents versus dependents?** Inputs to a formula versus outputs affected by it.
30. **Why test a recorded macro from a different cell?** To reveal absolute or relative reference assumptions.
31. **Why can a classic calculated-field total differ from row products?** It calculates from aggregates, as 300 versus 140 illustrates.
32. **What does refresh not fix?** Wrong source range, record grain, types, aggregation or business definitions.

## Places to learn

This is a selective learning path, not a complete list of Excel Expert resources or a requirement to consume every item. All time estimates below are author suggestions.

### Focused source-to-evidence route

**A Pivot report with a reconciliation trail — public task reference; about 60–90 minutes.** Use [Create a PivotChart](https://support.microsoft.com/en-us/excel/get-started/create-a-pivotchart) with your own monthly expense table. Produce a PivotTable, linked chart and category filter; reconcile the displayed values with a manually checked source subtotal. Change one source value, refresh, and retain the saved `.xlsx` plus a change log. This estimate adds original workbook creation and verification to a short article, not a vendor course duration. **VERIFY CURRENT:** Microsoft documents separate Windows, Mac and web routes; Mac and web begin from a PivotTable, and Mac chart-type limits apply. Follow your platform tab rather than copying Windows clicks. This focused chart route does not replace advanced-formula or macro practice. No visible article date was established; text was inspected October 28, 2026 without Excel execution.

Joe McDaid's [Stale Value Formatting announcement](https://techcommunity.microsoft.com/blog/excelblog/stale-value-formatting/3887098), originally published August 8, 2023, explains the calculation-mode problem clearly. Its Windows Beta availability paragraph is historical. Use the current Support reference in section 1 for present behavior and limitations. Read the warning as a prompt to verify calculation, not as ordinary font styling. The article adds useful context; it does not establish an additional exam objective. Its embedded demonstration was not evaluated here.

| Resource | Access | Estimated time |
|---|---|---:|
| Official credential page and linked detailed outline above | Public | **25 minutes** for scope and logistics |
| Function and workflow references linked in each section | Public | **3–5 hours**, including small experiments |
| [Excel help and learning](https://support.microsoft.com/en-us/excel) | Public directory; linked lessons not comprehensively audited | About 30–60 min to locate one weak-topic route; estimate for directory browsing and planning, with task practice budgeted separately |
| Ten labs and six worked examples in this guide | Suitable Excel desktop environment required | **15–22 hours** plus two timed repeats |

Before a timed attempt, explain every named function, recover from a broken formula, reconcile a filtered Pivot total and deliver a correctly protected workbook. Reserve part of the 50-minute practice session for checking the saved result.
