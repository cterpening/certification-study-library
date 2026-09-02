---
exam_code: PCEP-30-02
vendor_id: python-institute
official_blueprint: https://pythoninstitute.org/pcep-exam-syllabus/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-02
---

# PCEP-30-02 Certified Entry-Level Python Programmer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked September 2, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#pcep-30-02-coverage-record). The [official PCEP syllabus](https://pythoninstitute.org/pcep-exam-syllabus/) is authoritative.

**Current baseline:** PCEP-30-02, whose detailed syllabus is dated February 23, 2022 and remains marked active<br>
**Upcoming blueprint change:** PCEP-30-03 is in development and was announced for Q3 2026; the live credential page still identifies PCEP-30-02 as the current version, so verify the code and syllabus immediately before purchase<br>
**Official delivery snapshot:** 30 questions; 40-minute exam plus 5-minute NDA/tutorial; 70% passing score; TestNow delivery; English, Spanish, Portuguese, Polish, and Japanese listed<br>
**Credential snapshot:** no formal prerequisite; five-year validity; exam from USD 69 when checked; a failed attempt requires a seven-day wait<br>

## How to use this guide

PCEP is an entry-level programming exam, but it is not merely a vocabulary test. You need to trace short programs precisely, predict values and types, recognize syntax and runtime failures, and choose a small construct that fits a stated problem.

Use one repeatable loop:

1. predict a snippet's output, final state, or exception without running it;
2. run it in a disposable Python 3 environment;
3. explain every difference between your prediction and the result;
4. change one boundary, type, branch, collection, argument, or exception;
5. map the lesson back to one syllabus block.

Write code throughout your preparation. Reading can create recognition without recall, while typing, tracing, testing, and debugging expose gaps quickly. Stay inside the published entry-level boundary: classes, third-party frameworks, concurrency, packaging, and advanced language internals may be useful later, but they should not displace the four current blocks.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Weighted objective map

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| 1. Computer Programming and Python Fundamentals | 7 | 18% | Explain execution and syntax, evaluate literals/operators/types, and use console I/O |
| 2. Control Flow — Conditional Blocks and Loops | 8 | 29% | Trace nested decisions and every loop path, including `else`, `break`, and `continue` |
| 3. Data Collections — Tuples, Dictionaries, Lists, and Strings | 7 | 25% | Predict indexing, slicing, mutation, copying, membership, iteration, and method results |
| 4. Functions and Exceptions | 8 | 28% | Trace arguments, returns, scope, recursion/generation, exception hierarchy, and handlers |

The table follows the detailed official syllabus. The OpenEDG store's practice-product page currently shows 28% for control flow and 26% for collections instead of 29% and 25%. Do not average or combine them: use the syllabus for study allocation and treat the product-page mismatch as a source-maintenance issue.

## 1. Computer programming and Python fundamentals — 18%

### From source to behavior

A programming language supplies vocabulary, grammar, and meaning. **Lexis** determines valid tokens such as names, keywords, operators, and literals. **Syntax** determines how those tokens may be arranged. **Semantics** determines what a valid arrangement means when executed. A misspelled keyword is lexical/token trouble; a missing delimiter or invalid arrangement is syntax trouble; a valid expression that computes the wrong business result is a semantic or logic problem.

Compilation translates code before a later execution step; interpretation executes through another program. Avoid treating Python as a one-word exception to either model. A common CPython execution path compiles source into bytecode and executes that bytecode in the Python virtual machine. For PCEP, understand the conceptual distinction and that the interpreter reports failures; do not memorize implementation internals.

Python uses indentation to define suites beneath statements such as `if`, `for`, `while`, and `def`. A colon introduces the suite and consistently indented statements belong to it. Comments beginning with `#` are ignored as program instructions, but a `#` inside a string remains data. Keywords are reserved and cannot be ordinary variable names.

> **Related item:** A parser can reject syntactically invalid code before the intended path runs. A runtime exception occurs only after execution reaches a failing operation; a logic error can run successfully and still return the wrong answer.

### Literals, variables, and types

The core scalar types in scope are `bool`, `int`, `float`, and `str`. `True` and `False` are Boolean literals. Integers have no fractional part; floats approximate real-number values and can use scientific notation such as `1.5e3`. Strings are ordered immutable sequences of characters.

Integer literals can express bases with prefixes: binary `0b`, octal `0o`, and hexadecimal `0x`; the value is still an integer after evaluation. A variable binds a name to an object. Assignment changes the binding and does not declare a permanently fixed type. Choose legal, descriptive names; distinguish case; avoid keywords; and apply the PEP 8 naming conventions included by the syllabus.

Floating-point values are finite binary approximations. A decimal-looking expression such as `0.1 + 0.2` may not equal the exact decimal `0.3`. This is not random corruption. For entry-level questions, recognize the limitation and avoid assuming printed decimal appearance proves exact equality.

### Operators and evaluation

Know arithmetic `**`, `*`, `/`, `//`, `%`, `+`, and `-`; unary signs; comparisons; Boolean `not`, `and`, and `or`; bitwise `~`, `&`, `^`, `|`, `<<`, and `>>`; assignment and augmented assignment; and string concatenation/repetition.

Precedence decides which operation groups first; associativity/binding decides how operators at a comparable level group. Parentheses make intent explicit. Exponentiation binds differently from ordinary left-to-right arithmetic, and unary minus versus exponentiation is a classic trace boundary. `/` produces floating-point division. `//` performs floor division, which matters for negative results. `%` is related to the floor-division result rather than a simple “drop the sign” remainder rule.

Comparisons yield Booleans. `not` negates truth, `and` requires both conditions to be truthy, and `or` requires at least one. Boolean operations short-circuit, so a later expression may not execute. Bitwise operators act on integer bit patterns; do not confuse `&` with logical `and` or `|` with logical `or`.

`int()` and `float()` convert compatible values but can raise `ValueError` for unsuitable text. `str()` produces text. Conversion is different from merely displaying a value.

### Console input and output

`input()` returns a string, even when the user types digits. Convert before numeric arithmetic. `print()` accepts multiple values; `sep=` controls the text between them and `end=` controls the trailing text. Trace types as well as values:

```python
width = int(input("Width: "))
height = float(input("Height: "))
print("Area", width * height, sep=": ", end="\n")
```

Ask what happens for valid numeric input, decimal input to `int()`, empty input, and nonnumeric text. PCEP may ask you to identify behavior; production code would also validate and handle failures.

## 2. Control flow — 29%

### Decisions

An `if` suite runs when its condition is truthy. `elif` adds mutually exclusive tests evaluated in order, and `else` catches the remaining path. Separate `if` statements are not equivalent to one `if`/`elif` chain: multiple separate conditions can all run.

Nested decisions belong to the suite indicated by indentation. Trace the exact path rather than reading what you think the program intends. For compound conditions, use a small truth table and note short-circuit behavior. Test boundaries such as `<` versus `<=`, especially where adjacent ranges must neither overlap nor leave gaps.

### Iteration

`while` repeats while a condition remains truthy. Identify initialization, condition, state change, and termination. Missing or ineffective state change can cause an infinite loop. `for` iterates over items from an iterable. `range(start, stop, step)` produces integers beginning at `start` and stopping before `stop`; the defaults are start zero and step one. A negative step requires compatible boundaries, and a zero step is invalid.

`break` exits the nearest loop. `continue` skips the remainder of the current iteration and begins the next. `pass` performs no action and can preserve a syntactically required suite. In nested loops, a `break` affects only the innermost loop containing it.

A loop's `else` suite runs when the loop finishes normally, including a `for` that receives no items or a `while` whose condition starts false. It does not run when that loop exits through `break`. The construct is useful for a search: break when found; otherwise report not found in `else`.

> **Related item:** A loop invariant is a fact that remains true before and after each iteration. Even though formal proof is beyond PCEP, writing the invariant and termination condition makes off-by-one and infinite-loop errors much easier to detect.

### A reliable trace table

For any loop, create columns for iteration number, condition or current item, changed variables, printed value, and control transfer. For nested code, add the branch taken. Do not execute the next line in your head until you have recorded the current line's side effects.

```python
total = 0
for number in range(1, 6):
    if number % 2 == 0:
        continue
    total += number
else:
    print(total)
```

The sequence is 1 through 5, even values skip the addition, no `break` occurs, and the `else` prints 9. This one trace connects range boundaries, remainder, branching, `continue`, augmented assignment, and loop `else`.

## 3. Data collections — 25%

### One model: sequence, mapping, mutability, aliasing

Lists, tuples, and strings are ordered sequences and support integer indexing and slicing. Dictionaries are mappings accessed by keys. Lists and dictionaries are mutable; tuples and strings are immutable. Immutability means the object's contained references cannot be reassigned through that object—it does not recursively freeze a mutable object nested inside a tuple.

Index zero is the first element and negative indices count from the end. A slice uses start-inclusive, stop-exclusive, and optional step behavior. Out-of-range direct indexing raises `IndexError`, while a slice can safely stop beyond the sequence. `len()` returns the number of top-level elements or characters.

Assignment does not automatically copy an object. If `second = first` for a list, both names refer to the same list, so mutation through either is visible through both. A full slice or appropriate copy operation makes a shallow outer copy; nested mutable elements can still be shared.

> **Related item:** Identity asks whether two names refer to the same object; equality asks whether values compare equal. PCEP's copying questions become much easier when you draw names as arrows to objects.

### Lists

Lists are mutable sequences. Build them with brackets, access by index/slice, and update, insert, append, or delete elements. `append(x)` adds one object at the end; `insert(i, x)` places an item at a position; `index(x)` returns the first matching position or raises `ValueError`; `del` removes a selected item or slice. `sorted(values)` returns a new sorted list, while mutating list methods generally change the existing object and commonly return `None`.

`in` and `not in` test membership. Iterating directly over a list visits its elements. Be cautious when adding or removing from the same list you are traversing because indices and remaining items shift. A list comprehension creates a new list by combining an expression, iteration, and optional condition.

Nested lists can model rows, matrices, or cubes, but every bracket level matters. Beware repeated inner-list aliases from multiplication: creating several references to the same nested list is different from constructing independent rows.

### Tuples

Tuples are immutable sequences, commonly built with commas. Parentheses help grouping, but the comma makes a one-element tuple: `(7,)`. You may index, slice, iterate, unpack, and test membership. You cannot replace or delete an element in place. Lists and tuples both preserve ordered positions; lists suit changing collections, while tuples suit fixed groupings and can be used where immutability is required, subject to their contents.

### Dictionaries

A dictionary maps unique hashable keys to values. Build key-value pairs with braces, retrieve by key, assign a new key or replace an existing value, and delete a key. Missing direct lookup raises `KeyError`; checking membership tests keys, not values.

`keys()`, `values()`, and `items()` provide views of keys, values, and key-value pairs. Iterating a dictionary directly iterates keys. Use `.items()` when both key and value are needed. Do not confuse a key's existence with its associated value being truthy.

### Strings

Strings support indexing, slicing, iteration, membership, concatenation, and repetition but not in-place character replacement. Methods return new values because strings are immutable. Single and double quotes can delimit strings; escaping with `\` represents special characters or embeds a conflicting quote. Triple-quoted strings can span lines. Track the difference between characters in source and characters in the resulting string.

> **Related item:** A data structure should match the question you need to ask: ordered changing sequence → list; ordered fixed record → tuple; lookup by key → dictionary; immutable text sequence → string. That decision model transfers beyond the exam.

## 4. Functions and exceptions — 28%

### Functions, arguments, and results

`def` creates a function object and binds its name when execution reaches the definition. Calling invokes the body. Parameters are names in the definition; arguments are values supplied at the call. Positional arguments match by position, keyword arguments by parameter name, and default values supply omitted optional arguments. Required positional arguments must precede defaulted parameters in an ordinary definition, and positional arguments generally precede keyword arguments in a call.

`return` ends the current call and supplies a value. Falling off the end or using bare `return` returns `None`. Printing a value is a side effect and is not the same as returning it. Each call has its own local parameter bindings.

Names assigned inside a function are normally local. Name resolution can also find enclosing, global, and built-in names, but the current syllabus emphasizes local/global behavior and shadowing. A local name can hide an outer name. `global name` directs assignments in that function to the module-level binding; use it only when the behavior is intentional and traceable.

Default argument expressions are created when the definition executes, not anew for every call. A mutable default can therefore retain changes between calls. Even at entry level, recognize the difference between rebinding a local parameter and mutating a passed list.

### Recursion and generators

A recursive function calls itself on a smaller or simpler case and needs a reachable base case. Trace each call's arguments and pending return. Without progress toward the base case, recursion continues until an error rather than solving the problem.

A generator function uses `yield` to produce values while preserving its execution state between requests. Calling it creates a generator; iteration resumes it until the next yield and eventually completion. Do not equate `yield` with `return`: `return` ends the call, while `yield` suspends and can later resume it.

> **Related item:** Decomposition is more important than merely having functions. A useful function has a coherent responsibility, clear inputs and output, limited side effects, and testable normal and boundary behavior.

### Exception hierarchy and handling

An exception is an object describing an abnormal condition. The syllabus names `BaseException`, `Exception`, `SystemExit`, `KeyboardInterrupt`, `ArithmeticError`, `LookupError`, `IndexError`, `KeyError`, `TypeError`, and `ValueError`.

Hierarchy determines which handlers match. `IndexError` and `KeyError` are kinds of `LookupError`; numeric failures can derive from `ArithmeticError`. Many ordinary application errors derive from `Exception`. `SystemExit` and `KeyboardInterrupt` derive directly from `BaseException`, so a handler for `Exception` does not catch them. This distinction helps ordinary error handling avoid swallowing exit and interrupt signals.

A `try` suite contains operations that may fail. Matching `except` branches are considered in order, and the first match handles the exception. Put specific handlers before broader parents; otherwise the broader branch makes a later specific branch unreachable. If no local handler matches, the exception propagates to the caller. Handle an error where the code can add context, recover, choose a fallback, or deliberately translate it; do not catch errors merely to hide them.

Differentiate common failures:

- invalid conversion such as `int("three")` → `ValueError`;
- incompatible operation such as adding a number and string → `TypeError`;
- missing list position → `IndexError`;
- missing dictionary key → `KeyError`;
- division by zero → an `ArithmeticError` descendant.

## Integrated scenarios

### Scenario 1: Shipping quote

Read package weight and destination zone as strings, convert them, validate positive and supported ranges, choose a rate through an `if`/`elif` chain, compute the amount, and print a labeled result. Add `try`/`except` for invalid conversion. Test a normal package, every rate boundary, zero/negative weight, unsupported zone, blank text, and nonnumeric input.

### Scenario 2: Student score summary

Store names and score lists in a dictionary, calculate each average with a function, build a list of passing names with iteration or a comprehension, and print a compact report. Copy the data before a simulated adjustment and explain shallow alias risks. Test an empty score list and a missing student deliberately, then decide whether prevention, a default, or exception handling is appropriate.

### Scenario 3: Inventory search

Represent immutable item records as tuples inside a list. Search by code with `for` and `break`; use loop `else` for the not-found path. Update quantities in a dictionary, and create a generator that yields low-stock codes. Trace existing, missing, first, last, empty, and duplicate-input cases without turning the exercise into an advanced application.

## Hands-on labs

1. **Execution and failure map:** create examples of lexical/name, syntax, runtime, and logic failures; record when each is detected and how you verified the correction.
2. **Types and operator laboratory:** build a table of literal, expression, predicted value, actual value, and type covering bases, scientific notation, division/floor/modulo, precedence, Boolean/bitwise operators, strings, and conversions.
3. **Console validator:** accept two values, convert safely, calculate a result, and vary `sep`/`end`; test empty, invalid, negative, zero, and fractional inputs.
4. **Control-flow tracer:** hand-trace nested conditions and loops with `range`, `break`, `continue`, `pass`, and loop `else`; confirm each trace by running the code.
5. **Collection identity lab:** compare aliasing, shallow list copies, nested lists, tuple-contained lists, dictionary views, slices, membership, deletion, and sorting; draw name-to-object diagrams.
6. **String transformation lab:** predict and test indexes, slices, escapes, multiline strings, concatenation, repetition, membership, and methods while proving the original string remains unchanged.
7. **Function call laboratory:** trace positional/keyword/default arguments, `None`, local/global shadowing, list mutation, a safe recursive function, and a small generator.
8. **Exception and capstone lab:** build one of the integrated scenarios; trigger `ValueError`, `TypeError`, `IndexError`, and `KeyError`; order handlers correctly; document input, path, output/exception, fix, and regression checks.

Run labs only with your own code and disposable data. Do not seek, reproduce, or share recalled certification items.

## Original knowledge checks

1. How do lexis, syntax, and semantics differ?
2. Why is simply calling Python “interpreted” an incomplete execution model?
3. What makes indentation part of program structure?
4. What values and types result from `0b1010`, `0o12`, and `0xA`?
5. Why might `0.1 + 0.2 == 0.3` be false?
6. What does assignment bind, and why can the same name later reference another type?
7. Compare `/`, `//`, and `%`, including a negative operand.
8. Why can parentheses be preferable even when you know precedence?
9. Distinguish Boolean `and` from bitwise `&`.
10. Why does `input()` often require conversion?
11. What do `sep=` and `end=` change in `print()`?
12. How do separate `if` statements differ from an `if`/`elif` chain?
13. Which boundaries should you test for adjacent numeric ranges?
14. What four facts should you record before trusting a `while` loop?
15. What values does `range(5, 0, -2)` produce?
16. What loop does `break` exit in nested iteration?
17. What work does `continue` skip?
18. When does a loop's `else` run?
19. Why can list mutation during iteration skip items?
20. Compare direct out-of-range indexing with an overlong slice.
21. Why do `a = values` and `a = values[:]` behave differently?
22. What does a shallow copy still share?
23. Why is `(7)` not a one-element tuple but `(7,)` is?
24. Can a list inside a tuple change? Explain.
25. What does dictionary membership test by default?
26. When should you use `.items()` rather than direct dictionary iteration?
27. Why can a missing dictionary key and a false value require different tests?
28. Why do string methods return a new string?
29. What distinction should you track when reading escape sequences?
30. How do parameters and arguments differ?
31. Compare a function that prints a value with one that returns it.
32. What does a function return if it reaches the end without `return value`?
33. What is name shadowing?
34. Why can a mutable default retain state across calls?
35. What two properties make a recursive solution terminate correctly?
36. How does `yield` differ from `return`?
37. Why should a specific exception handler precede its parent handler?
38. Which named exceptions derive directly from `BaseException` rather than ordinary `Exception`?
39. Distinguish likely `ValueError`, `TypeError`, `IndexError`, and `KeyError` cases.
40. What must you verify about PCEP-30-02 before purchasing an attempt now?

## Answers and reasoning

1. Lexis defines valid tokens, syntax their valid arrangement, and semantics the meaning of valid code.
2. Common implementations can compile source to bytecode before a virtual machine executes it; compilation and interpretation can be stages, not exclusive labels.
3. Indented suites determine which statements belong to a compound statement.
4. All are integer 10; the prefixes change source representation, not the resulting type.
5. Many decimal fractions lack exact finite binary floating-point representations.
6. Assignment binds a name to an object; a later assignment may bind it to another object of another type.
7. `/` is true division, `//` floors the quotient, and `%` supplies the paired modulo result; flooring toward negative infinity affects signs and values.
8. They communicate intent and protect against a mistaken precedence assumption.
9. `and` evaluates truth with short-circuit behavior; `&` combines integer bits.
10. It returns text; arithmetic needs a compatible numeric conversion.
11. The separator between printed values and the text appended after the final value.
12. Separate conditions may all run; an `elif` chain selects the first truthy branch.
13. Values immediately below, exactly at, and immediately above each boundary.
14. Initial state, continuation condition, state change, and reachable termination.
15. `5, 3, 1`; stop zero is excluded.
16. Only the nearest enclosing loop.
17. The remainder of the current iteration, then execution proceeds to the next iteration test/item.
18. On normal exhaustion or false condition, but not when that loop exits by `break`.
19. Removing or inserting changes indices and the remaining traversal while it is in progress.
20. Direct indexing raises `IndexError`; slicing can stop beyond the sequence without that error.
21. Assignment aliases the same list; a full slice creates a new outer list.
22. References to nested mutable objects.
23. Parentheses group the expression; the comma defines the tuple item.
24. Yes. The tuple's reference cannot be replaced, but the referenced list remains mutable.
25. Keys.
26. When the loop needs both each key and its associated value.
27. Absence and presence-with-a-false-value represent different states; use explicit membership for existence.
28. Strings are immutable, so transformation creates another string value.
29. Source characters such as backslash-plus-letter versus the one resulting escaped character.
30. Parameters are definition-side names; arguments are call-side supplied values.
31. Printing is an output side effect; returning passes a value to the caller for reuse.
32. `None`.
33. A nearer-scope name hides another name of the same spelling in an outer scope.
34. The default object is created when the definition executes and reused by later omitted-argument calls.
35. A reachable base case and progress toward it on every recursive path.
36. `yield` suspends and preserves generator state; `return` ends the call.
37. The parent also matches child exceptions, so placing it first captures the case too early.
38. `SystemExit` and `KeyboardInterrupt` in the published set.
39. Unsuitable value for a valid operation; incompatible operand/type; missing sequence index; missing mapping key.
40. Confirm that PCEP-30-02 is still the active purchasable version and that your resources match its syllabus; PCEP-30-03 is announced but not yet shown as current.

## Source and freshness notes

- The detailed syllabus controls the four block names, item counts, weights, and topic boundary. The [PCEP credential page](https://pythoninstitute.org/pcep/) controls current version, delivery, price, language, prerequisite, validity, and retake details.
- The official practice product currently disagrees with the syllabus by one percentage point in blocks 2 and 3. The syllabus is used here; revalidate both pages when PCEP-30-03 launches.
- Python behavior in this guide is limited to stable Python 3 fundamentals and should still be checked in a current supported interpreter and the [Python documentation](https://docs.python.org/3/tutorial/).
- This guide paraphrases the public objectives and uses original examples, scenarios, labs, checks, and answers. It contains no recalled/live items, answer dumps, or copied paid-course questions.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one coherent primary course or book, write and debug code for every block, and use one explanation-led assessment to identify gaps. The official syllabus—not any third-party “pass” claim—is the final scope authority.

| Resource | Access | Estimated time |
|---|---|---:|
| [PCEP-30-02 exam syllabus](https://pythoninstitute.org/pcep-exam-syllabus/) | Free official blueprint | 1–2 hours to map and recheck |
| [Python Essentials 1](https://edube.org/study/pe1) | Free official aligned self-study; account required | 42 hours listed |
| [Cisco Networking Academy Python Essentials 1](https://www.netacad.com/courses/python-essentials-1) | Free official partner course; account required | About 30–42 hours; verify current catalog estimate |
| [OpenEDG PCEP practice-test compendium](https://ums.edube.org/products/0-pi-pcep-3002-pt) | Paid official practice; multiple launches and study pages | About 4–8 hours including remediation |
| [Microsoft Learn: Python Programming Fundamentals](https://learn.microsoft.com/en-us/training/paths/get-started-with-python-fundamentals/) | Free beginner path; broader tooling content | 3 hours 12 minutes listed, plus coding |
| [Pluralsight Python Essentials](https://www.pluralsight.com/paths/python-essentials) | Subscription; broad path in active production | Select 8–15 hours from the 46-hour path |
| [Learning Python, 6th Edition](https://www.oreilly.com/library/view/learning-python-6th/9781098171292/) | O'Reilly subscription/book; much broader than PCEP | Select 15–25 hours from the 42h20m listing |
| [Udemy: Python PCEP by Adrian Wiech](https://www.udemy.com/course/python-pcep/) | Paid marketplace course with coding and mock exam | 4 hours 27 minutes listed, plus 6–10 hours practice |
| [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/) | Free Harvard OpenCourseWare; substantially broader | Select weeks 0–3, about 15–25 hours with problems |
| [freeCodeCamp beginner Python course](https://www.youtube.com/watch?v=rfscVS0vtbw) | Free YouTube course; older but useful fundamentals | About 4 hours 26 minutes, plus coding |

No exact current PCEP product from Whizlabs or MeasureUp, and no dedicated PCEP path on Pluralsight or O'Reilly, was independently verified. Generic resources can teach Python well without matching every exam edge; reconcile them against the four blocks. Prices, access, runtimes, course revisions, practice weights, and exam-version claims are volatile—verify before purchase, especially during the PCEP-30-03 transition.
