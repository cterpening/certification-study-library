---
exam_code: PCEP-30-02
vendor_id: python-institute
official_blueprint: https://pythoninstitute.org/pcep-exam-syllabus/
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-29
---

# PCEP-30-02 Certified Entry-Level Python Programmer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked September 29, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#pcep-30-02-coverage-record). The [official PCEP syllabus](https://pythoninstitute.org/pcep-exam-syllabus/) is authoritative.

**CURRENT BLUEPRINT — current baseline:** PCEP-30-02, whose detailed syllabus is dated February 23, 2022 and remains marked active<br>
**VERIFY CURRENT — upcoming blueprint change:** PCEP-30-03 is in development and was announced for Q3 2026; the live credential page still identifies PCEP-30-02 as the current version, so verify the code and syllabus immediately before purchase<br>
**VERIFY CURRENT — official delivery snapshot:** 30 questions; 40-minute exam plus 5-minute NDA/tutorial; 70% passing score; TestNow delivery; English, Spanish, Portuguese, Polish, and Japanese listed<br>
**VERIFY CURRENT — credential snapshot:** no formal prerequisite; five-year validity; exam from USD 69 when checked; a failed attempt requires a seven-day wait<br>

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

### Detailed coverage and source reconciliation

The fifteen numbered objectives are 1.1–1.5, 2.1–2.2, 3.1–3.4 and 4.1–4.4. Their individual bullets are mapped in the [dated deep-review report](../docs/research/2026-09-29-pcep-30-02-deep-review.md). The HTML block 4 introduction says “7 objectives & 19 sub-objectives,” but actually lists four numbered objectives. Follow the displayed numbered topics and the matching [five-page syllabus PDF](https://pythoninstitute.org/assets/627e61bc29de3989767095.pdf), rather than treating that introductory count as additional hidden scope. The MQC prose also groups topics differently from the weighted table; it does not replace that table.

| Objective group | Practice evidence in this guide |
|---|---|
| 1.1–1.2: execution, language structure | Compilation versus runtime failures, indentation and style distinction |
| 1.3: literals, bases, naming | Base conversion, scientific notation, PEP 8 guidance |
| 1.4: operators and types | Signed floor/modulo, power grouping, bitwise operations, short-circuit values |
| 1.5: I/O | Real `input()` behavior, conversions, prompt/output capture and integer-cent quote formatting |
| 2.1–2.2: decisions and iteration | Rate boundaries, empty loops, `continue`, nearest-loop `break`, `else`, early return |
| 3.1–3.4: collections | Copy depth, independent matrix rows, slicing, tuple contents, dictionary views, string return types |
| 4.1–4.2: functions | Arguments, implicit `None`, default state, mutation/rebinding, scope, recursion and generator timing |
| 4.3–4.4: exceptions | Hierarchy, first matching handler, cross-function propagation and specific recovery |

The item counts are not percentages: `7/30` is not the published 18% weight. Neither these weights nor a count of correct practice answers establishes the vendor's partial-credit scoring algorithm. Use the published 70% threshold without inventing a raw-question pass count.

## 1. Computer programming and Python fundamentals — 18%

### From source to behavior

A programming language supplies vocabulary, grammar, and meaning. **Lexis** determines valid tokens such as names, keywords, operators, and literals. **Syntax** determines how those tokens may be arranged. **Semantics** determines what a valid arrangement means when executed. Classify the actual failure, not just the spelling mistake: `iff True:` has invalid grammar, while `pritn("hello")` contains a valid identifier and compiles, then raises `NameError` when executed without that binding. An invalid numeral such as `0b102` is rejected during compilation. A program can also execute successfully and calculate the wrong business result. See the [lexical reference](https://docs.python.org/3.13/reference/lexical_analysis.html) and [error tutorial](https://docs.python.org/3.13/tutorial/errors.html).

Compilation translates code before a later execution step; interpretation executes through another program. Avoid treating Python as a one-word exception to either model. A common CPython execution path compiles source into bytecode and executes that bytecode in the Python virtual machine. For PCEP, understand the conceptual distinction and that the interpreter reports failures; do not memorize implementation internals.

Python uses indentation to define suites beneath statements such as `if`, `for`, `while`, and `def`. A colon introduces the suite and consistently indented statements belong to it. Comments beginning with `#` are ignored as program instructions, but a `#` inside a string remains data. Reserved keywords such as `if` cannot be ordinary variable names. Some newer spellings are context-dependent soft keywords; that does not add newer language features to this syllabus. PEP 8 recommends four spaces per indentation level, lowercase names with underscores for functions/variables, and uppercase names for constants. These style recommendations differ from syntax: consistently using two spaces can parse even though it does not follow the four-space recommendation. The [PEP 8 guide](https://peps.python.org/pep-0008/) also recommends 79-character code lines and 72-character comments/docstrings, with stated project-specific exceptions.

> **Related item:** A parser can reject syntactically invalid code before the intended path runs. A runtime exception occurs only after execution reaches a failing operation; a logic error can run successfully and still return the wrong answer.

### Literals, variables, and types

The core scalar types in scope are `bool`, `int`, `float`, and `str`. `True` and `False` are Boolean literals. Integers have no fractional part; floats approximate real-number values and can use scientific notation such as `1.5e3`. Strings are ordered immutable sequences of characters.

Integer literals can express bases with prefixes: binary `0b`, octal `0o`, and hexadecimal `0x`; the value is still an integer after evaluation. A variable binds a name to an object. Assignment changes the binding and does not declare a permanently fixed type. Choose legal, descriptive names; distinguish case; avoid keywords; and apply the PEP 8 naming conventions included by the syllabus.

Finite floating-point values use binary representations, so many decimal fractions can only be approximated. The type also supports infinities and NaN; do not assume every successful `float()` conversion produces a finite ordinary measurement. A decimal-looking expression such as `0.1 + 0.2` may not equal the exact decimal `0.3`. This is not random corruption. For entry-level questions, recognize the limitation and avoid assuming printed decimal appearance proves exact equality. The [floating-point tutorial](https://docs.python.org/3.13/tutorial/floatingpoint.html) explains the representation and display distinction.

### Operators and evaluation

Know arithmetic `**`, `*`, `/`, `//`, `%`, `+`, and `-`; unary signs; comparisons; Boolean `not`, `and`, and `or`; bitwise `~`, `&`, `^`, `|`, `<<`, and `>>`; assignment and augmented assignment; and string concatenation/repetition.

Precedence decides which operation groups first; associativity/binding decides how operators at a comparable level group. Parentheses make intent explicit. Exponentiation binds differently from ordinary left-to-right arithmetic, and unary minus versus exponentiation is a classic trace boundary. `/` produces floating-point division. `//` performs floor division, which matters for negative results. `%` is related to the floor-division result rather than a simple “drop the sign” remainder rule.

Comparisons between the built-in values used here yield Booleans. `not` always returns a Boolean, but `and` and `or` return an operand: `"ready" and 8` produces integer `8`; `[] and 8` produces the empty list; `"" or "fallback"` produces the fallback string. They stop evaluating once that operand is determined. Thus `False and 1 / 0` does not divide at all. The [expression reference](https://docs.python.org/3.13/reference/expressions.html) supplies the exact grouping and short-circuit rules. Bitwise operators act on integer bit patterns; do not confuse `&` with logical `and` or `|` with logical `or`.

`int()` and `float()` convert compatible values but can raise `ValueError` for unsuitable text. `str()` produces text. Conversion is different from merely displaying a value. For finite floats, `int()` truncates toward zero: `int(-2.75)` is `-2`, whereas `-11 // 4` floors to `-3`. `int("2.5")` raises `ValueError`; it does not first parse a float. Check the [built-in functions reference](https://docs.python.org/3.13/library/functions.html) when tracing conversions and console I/O.

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

A loop's `else` suite runs when the loop finishes normally, including a `for` that receives no items or a `while` whose condition starts false. It does not run when that loop exits through `break`, returns from the function, or propagates an exception out of the loop. The construct is useful for a search: break when found; otherwise report not found in `else`. The [control-flow tutorial](https://docs.python.org/3.13/tutorial/controlflow.html) also explains default arguments and function calls.

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

Lists are mutable sequences. Build them with brackets, access by index/slice, and update, insert, append, or delete elements. `append(x)` adds one object at the end; `insert(i, x)` places an item at a position; `index(x)` returns the first matching position or raises `ValueError`; `del` removes a selected item or slice. `sorted(values)` returns a new sorted list, while `list.sort()`, `append()`, and `insert()` mutate and return `None`. Do not generalize that to every mutator: `pop()` removes and returns an item.

`in` and `not in` test membership. Iterating directly over a list visits its elements. Be cautious when adding or removing from the same list you are traversing because indices and remaining items shift. A list comprehension creates a new list by combining an expression, iteration, and optional condition.

Nested lists can model rows, matrices, or cubes, but every bracket level matters. Beware repeated inner-list aliases from multiplication: creating several references to the same nested list is different from constructing independent rows.

### Tuples

Tuples are immutable sequences, commonly built with commas. Parentheses help grouping, but the comma makes a one-element tuple: `(7,)`. You may index, slice, iterate, unpack, and test membership. You cannot replace or delete an element in place. Lists and tuples both preserve ordered positions; lists suit changing collections, while tuples suit fixed groupings and can be used where immutability is required, subject to their contents. A tuple containing a list is still immutable as a tuple, but is unhashable and cannot be a dictionary key. The [data-structures tutorial](https://docs.python.org/3.13/tutorial/datastructures.html) distinguishes these cases.

### Dictionaries

A dictionary maps unique hashable keys to values. Build key-value pairs with braces, retrieve by key, assign a new key or replace an existing value, and delete a key. Missing direct lookup raises `KeyError`; checking membership tests keys, not values.

`keys()`, `values()`, and `items()` provide views of keys, values, and key-value pairs. Iterating a dictionary directly iterates keys. Use `.items()` when both key and value are needed. Do not confuse a key's existence with its associated value being truthy. With `{"A": 0}`, `"A" in stock` is true while `bool(stock["A"])` is false. Views reflect subsequent dictionary changes; a view is not a frozen copy.

### Strings

Strings support indexing, slicing, iteration, membership, concatenation, and repetition but not in-place character replacement. A transformation such as `.upper()` returns a string value and leaves the original text unchanged; object identity is not the learning contract. Other methods return other types: `.find()` returns an index or `-1`, and `.split()` returns a list. The [built-in types reference](https://docs.python.org/3.13/library/stdtypes.html) documents these method results, dictionary views and sequence copying. Single and double quotes can delimit strings; escaping with `\` represents special characters or embeds a conflicting quote. Triple-quoted strings can span lines. Track the difference between characters in source and characters in the resulting string.

> **Related item:** A data structure should match the question you need to ask: ordered changing sequence → list; ordered fixed record → tuple; lookup by key → dictionary; immutable text sequence → string. That decision model transfers beyond the exam.

## 4. Functions and exceptions — 28%

### Functions, arguments, and results

`def` creates a function object and binds its name when execution reaches the definition. Calling invokes the body. Parameters are names in the definition; arguments are values supplied at the call. Positional arguments match by position, keyword arguments by parameter name, and default values supply omitted optional arguments. Required positional arguments must precede defaulted parameters in an ordinary definition, and positional arguments generally precede keyword arguments in a call.

`return` ends the current call and supplies a value. Falling off the end or using bare `return` returns `None`. Printing a value is a side effect and is not the same as returning it. Each call has its own local parameter bindings.

Names assigned inside a function are normally local. Name resolution can also find enclosing, global, and built-in names, but the current syllabus emphasizes local/global behavior and shadowing. A local name can hide an outer name. Assignment anywhere in an ordinary function body makes that name local unless declared otherwise: reading it before a value is bound can raise `UnboundLocalError`, even if a global binding exists. `global name` directs assignments in that function to the module-level binding; use it only when the behavior is intentional and traceable. The [names, scope and generators tutorial](https://docs.python.org/3.13/tutorial/classes.html) is a reference for these selected topics; its class-design material is broader than this exam.

Default argument expressions are created when the definition executes, not anew for every call. A mutable default can therefore retain changes between calls. Even at entry level, recognize the difference between rebinding a local parameter and mutating a passed list.

### Recursion and generators

A recursive function calls itself on a smaller or simpler case and needs a reachable base case. Trace each call's arguments and pending return. Without progress toward the base case, recursion continues until an error rather than solving the problem.

A generator function uses `yield` to produce values while preserving its execution state between requests. Calling it creates a generator; iteration resumes it until the next yield and eventually completion. Do not equate `yield` with `return`: `return` ends the call, while `yield` suspends and can later resume it.

> **Related item:** Decomposition is more important than merely having functions. A useful function has a coherent responsibility, clear inputs and output, limited side effects, and testable normal and boundary behavior.

### Exception hierarchy and handling

An exception is an object describing an abnormal condition. The syllabus names `BaseException`, `Exception`, `SystemExit`, `KeyboardInterrupt`, `ArithmeticError`, `LookupError`, `IndexError`, `KeyError`, `TypeError`, and `ValueError`.

Hierarchy determines which handlers match. `IndexError` and `KeyError` are kinds of `LookupError`; numeric failures can derive from `ArithmeticError`. Many ordinary application errors derive from `Exception`. `SystemExit` and `KeyboardInterrupt` derive directly from `BaseException`, so a handler for `Exception` does not catch them. This distinction helps ordinary error handling avoid swallowing exit and interrupt signals.

A `try` suite contains operations that may fail. Matching `except` branches are considered in order, and the first match handles the exception. Put specific handlers before broader parents; otherwise the broader branch makes a later specific branch unreachable. If no local handler matches, the exception propagates to the caller. Handle an error where the code can add context, recover, choose a fallback, or deliberately translate it; do not catch errors merely to hide them. “Abstract exceptions” here means useful grouping bases such as `LookupError` and `ArithmeticError`; it does not mean Python forbids constructing them. Compare the [built-in exception hierarchy](https://docs.python.org/3.13/library/exceptions.html).

Differentiate common failures:

- invalid conversion such as `int("three")` → `ValueError`;
- incompatible operation such as adding a number and string → `TypeError`;
- missing list position → `IndexError`;
- missing dictionary key → `KeyError`;
- division by zero → an `ArithmeticError` descendant.

## Integrated scenarios

### Scenario 1: Shipping quote

Use fictional integer-gram inputs and integer cents: 1–1000 grams costs 500 cents, 1001–5000 costs 900, and 5001–10000 costs 1400. Zone B doubles the amount; zone A does not. Conversion and range checks precede pricing. Thus 1001 grams to B produces `Quote: 18.00`, while `"2.5"` is rejected as integer text. The choice of grams and cents avoids adding floating-point money rounding to this entry-level exercise. These are teaching rules, not a carrier tariff.

### Scenario 2: Student score summary

Mina's `[60, 80]` averages 70 and passes the chosen 70-point cutoff; Lee's `[50]` does not. Ari's empty list produces `None`, preserving the distinction between “no scores” and a real zero average. Copying each score list before changing Mina's 60 to 100 produces an adjusted average of 90 while the original stays 70. This copying method is sufficient for these lists of immutable integers; it is not a general recursive deep copy. Scores must be integers in 0–100, a rule chosen for this exercise.

### Scenario 3: Inventory search

The records `[("P", 0), ("Q", 4), ("R", 1)]` contain three unique codes. Lookup of P must return `0`; lookup of Z returns `None`. Checking truthiness alone would conflate those results. `for`/`else` expresses the missing path, and the generator yields P then R below the chosen threshold of 2. Construction explicitly rejects duplicate codes so a later dictionary assignment cannot silently overwrite an earlier quantity. The search helper assumes that uniqueness contract; it returns the first matching record if used independently with duplicates.

### Worked implementation and output

**PRACTICAL DEPTH:** this complete program was executed locally. Its functions assume text inputs for the quote, lists of integers for scores, and `(code, quantity)` records with string codes for inventory. It is a small teaching program with no persistent state, accounts or external services. Dictionary comprehensions and formatted strings are supporting implementation context, not additional numbered objectives.

```python
"""Original small programs with fictional business rules and integer inputs."""


def shipping_quote(grams_text, zone_text):
    grams = int(grams_text)
    zone = zone_text.strip().upper()
    if not 1 <= grams <= 10000:
        raise ValueError("weight must be 1 through 10000 grams")
    if zone not in ("A", "B"):
        raise ValueError("zone must be A or B")
    if grams <= 1000:
        cents = 500
    elif grams <= 5000:
        cents = 900
    else:
        cents = 1400
    if zone == "B":
        cents *= 2
    return cents


def show_quote(grams_text, zone_text):
    try:
        cents = shipping_quote(grams_text, zone_text)
    except ValueError:
        return "Invalid weight or zone"
    return f"Quote: {cents // 100}.{cents % 100:02d}"


def average(scores):
    if not scores:
        return None
    for score in scores:
        if type(score) is not int:
            raise TypeError("scores must be integers")
        if not 0 <= score <= 100:
            raise ValueError("score must be 0 through 100")
    return sum(scores) / len(scores)


def summarize(records):
    averages = {name: average(scores) for name, scores in records.items()}
    passing = [name for name, result in averages.items()
               if result is not None and result >= 70]
    return averages, passing


def build_stock(records):
    stock = {}
    for code, quantity in records:
        if code in stock:
            raise ValueError("duplicate code")
        if type(quantity) is not int:
            raise TypeError("quantity must be an integer")
        if quantity < 0:
            raise ValueError("quantity cannot be negative")
        stock[code] = quantity
    return stock


def find_quantity(records, wanted):
    for code, quantity in records:
        if code == wanted:
            break
    else:
        return None
    return quantity


def low_stock(stock, threshold=2):
    for code, quantity in stock.items():
        if quantity < threshold:
            yield code


scores = {"Mina": [60, 80], "Lee": [50], "Ari": []}
adjusted = {name: values[:] for name, values in scores.items()}
adjusted["Mina"][0] = 100
records = [("P", 0), ("Q", 4), ("R", 1)]
print(show_quote("1001", "B"))
print(show_quote("2.5", "A"))
print(summarize(scores))
print(average(adjusted["Mina"]), average(scores["Mina"]))
print(find_quantity(records, "P"), find_quantity(records, "Z"))
print(list(low_stock(build_stock(records))))
```

Observed output:

```text
Quote: 18.00
Invalid weight or zone
({'Mina': 70.0, 'Lee': 50.0, 'Ari': None}, ['Mina'])
90.0 70.0
0 None
['P', 'R']
```

Test both sides of the 1000- and 5000-gram boundaries, the 1/10000 endpoints, zero, negatives, oversized input, empty and fractional text, and unsupported zones. For scores, distinguish empty, zero, cutoff and invalid data. For inventory, include empty, first, last, absent and duplicate records. The dated review records the actual execution results; these fictional examples do not validate a production application.

## Hands-on labs

1. **Execution and failure map:** create examples of invalid literals, syntax, runtime name lookup, and logic failures; record when each is detected and how you verified the correction.
2. **Types and operator laboratory:** build a table of literal, expression, predicted value, actual value, and type covering bases, scientific notation, division/floor/modulo, precedence, Boolean/bitwise operators, strings, and conversions.
3. **Console validator:** accept two values, convert safely, calculate a result, and vary `sep`/`end`; test empty, invalid, negative, zero, and fractional inputs.
4. **Control-flow tracer:** hand-trace nested conditions and loops with `range`, `break`, `continue`, `pass`, and loop `else`; confirm each trace by running the code.
5. **Collection identity lab:** compare aliasing, shallow list copies, nested lists, tuple-contained lists, dictionary views, slices, membership, deletion, and sorting; draw name-to-object diagrams.
6. **String transformation lab:** predict and test indexes, slices, escapes, multiline strings, concatenation, repetition, membership, and methods while proving the original string remains unchanged.
7. **Function call laboratory:** trace positional/keyword/default arguments, `None`, local/global shadowing, list mutation, a safe recursive function, and a small generator.
8. **Exception and capstone lab:** build one of the integrated scenarios; trigger `ValueError`, `TypeError`, `IndexError`, and `KeyError`; order handlers correctly; document input, path, output/exception, fix, and regression checks.

These eight activities are learner extensions, not claims that all their variations were completed during review. Run them only with your own code and disposable data. Do not seek, reproduce, or share recalled certification items.

## Executed trace workbook

**PRACTICAL DEPTH:** the following original, offline workbook passed 82 named checks using the already installed CPython 3.13.14. The cited 3.13 documentation displayed 3.13.15 at review time; the general `/3/` tutorial displayed 3.14.7. This is a disclosed local test version, not a claim about the exam platform's interpreter. No installation or upgrade was required. Assertions concern the documented fundamental behavior shown here, not every Python version or every input.

Predict each value before running. When the program stops, inspect the named mismatch and trace the relevant objects and control path. `check` compares values; identity checks explicitly use `is`. `raises` accepts the expected exception or a subclass. The fixed-string compilation examples demonstrate failure stages and should not be replaced with untrusted input. The small recursive function assumes integer arguments and demonstrates small inputs; recursion depth is still finite.

```python
"""Original PCEP traces: run locally with Python 3; no network or packages."""
import json

passed = []


def check(label, actual, expected):
    if actual != expected:
        raise AssertionError((label, actual, expected))
    passed.append(label)


def raises(label, expected, operation):
    try:
        operation()
    except expected:
        passed.append(label)
    else:
        raise AssertionError((label, "expected", expected.__name__))


# Values, types and the difference between grouping and evaluation.
check("bases", [0b1101, 0o15, 0xD], [13, 13, 13])
check("scientific notation", (1.25e2, type(1.25e2).__name__), (125.0, "float"))
check("unary minus and power", (-3 ** 2, (-3) ** 2, 2 ** -3), (-9, 9, 0.125))
check("power groups right", 2 ** 3 ** 2, 512)
check("negative division", (-11 // 4, -11 % 4, int(-11 / 4)), (-3, 1, -2))
check("integer division identity", (-11 // 4) * 4 + (-11 % 4), -11)
check("negative divisor", (11 // -4, 11 % -4), (-3, -1))
check("bitwise", (6 & 3, 6 | 3, 6 ^ 3, ~6, 3 << 2, 12 >> 2),
      (2, 7, 5, -7, 12, 3))
check("and returns operand", ("ready" and 8, [] and 8), (8, []))
check("or returns operand", ("" or "fallback", 5 or 1 / 0), ("fallback", 5))
check("not returns bool", (not [], type(not []).__name__), (True, "bool"))
check("short circuit", False and 1 / 0, False)
check("float approximation", 0.1 + 0.2 == 0.3, False)
check("exact binary fraction", 0.125 * 8, 1.0)
check("numeric text", (int(" 13 "), float("1.25e2")), (13, 125.0))
raises("decimal text is not integer text", ValueError, lambda: int("2.5"))
raises("incompatible addition", TypeError, lambda: "2" + 5)
check("string repetition", "ab" * 3, "ababab")

# Only these fixed strings are compiled; no external source is executed.
raises("invalid binary literal", SyntaxError,
       lambda: compile("value = 0b102", "literal", "exec"))
raises("missing colon", SyntaxError,
       lambda: compile("if True\n    value = 1", "suite", "exec"))
raises("keyword spelling changes grammar", SyntaxError,
       lambda: compile("iff True:\n    pass", "keyword", "exec"))
typo = compile("pritn('hello')", "name", "exec")
raises("valid name can fail at runtime", NameError, lambda: exec(typo, {}))
dead_path = compile("if False:\n    1 / 0", "unreached", "exec")
check("unreached runtime failure", exec(dead_path, {}), None)
style_scope = {}
exec(compile("if True:\n  MixedName = 7", "style", "exec"), style_scope)
check("style is not syntax", style_scope["MixedName"], 7)

# Control flow: every path has an explicit expected result.
check("descending range", list(range(7, 0, -3)), [7, 4, 1])
check("incompatible range direction", list(range(0, 7, -1)), [])
raises("zero range step", ValueError, lambda: range(0, 7, 0))


def loop_trace(values, stop):
    seen = []
    for value in values:
        if value == stop:
            break
        if value < 0:
            continue
        seen.append(value)
    else:
        seen.append("exhausted")
    return seen


check("empty loop else", loop_trace([], 9), ["exhausted"])
check("continue permits else", loop_trace([-1, 2], 9), [2, "exhausted"])
check("break skips else", loop_trace([2, 9, 3], 9), [2])
pairs = []
for row in range(2):
    for column in range(3):
        if column == 1:
            break
        pairs.append((row, column))
check("inner break only", pairs, [(0, 0), (1, 0)])
count = 2
while count:
    count -= 1
else:
    count = "finished"
check("while false condition reaches else", count, "finished")


def early_return():
    for value in [1]:
        return value
    else:
        return "exhausted"


check("return skips loop else", early_return(), 1)

# Collections: compare object identity separately from equal contents.
original = [[1], [2]]
alias = original
shallow = original[:]
independent = [row[:] for row in original]
check("outer identities", (alias is original, shallow is original), (True, False))
original[0].append(9)
check("shallow nested sharing", shallow, [[1, 9], [2]])
check("copied rows isolated", independent, [[1], [2]])
shallow.append([3])
check("outer append isolated", len(original), 2)
bad_grid = [[0, 0]] * 2
bad_grid[0][1] = 7
check("repeated row alias", bad_grid, [[0, 7], [0, 7]])
grid = [[0, 0] for _ in range(2)]
grid[0][1] = 7
check("independent rows", grid, [[0, 7], [0, 0]])
values = [4, 1, 3]
check("sorted copy", sorted(values), [1, 3, 4])
check("sort return", values.sort(), None)
check("sort mutation", values, [1, 3, 4])
check("pop returns removed item", values.pop(), 4)
values.insert(1, 8)
del values[0]
check("insert and delete", values, [8, 3])
check("reverse slice", values[::-1], [3, 8])
check("overlong slice", values[:100], [8, 3])
raises("direct index past end", IndexError, lambda: values[2])
raises("missing list value", ValueError, lambda: values.index(99))
check("singleton tuple", ((7), (7,)), (7, (7,)))
record = ("A", [2])
record[1].append(3)
check("tuple nested mutation", record, ("A", [2, 3]))
raises("tuple with list is unhashable", TypeError, lambda: hash(record))
stock = {"A": 0}
keys = stock.keys()
stock["B"] = 3
check("dictionary view updates", list(keys), ["A", "B"])
check("present zero differs from absent", ("A" in stock, bool(stock["A"]),
      "C" in stock), (True, False, False))
check("items carry pairs", list(stock.items()), [("A", 0), ("B", 3)])
raises("missing dictionary key", KeyError, lambda: stock["C"])
text = "a\nb"
check("escape has one character", (len(text), text[1]), (3, "\n"))
check("string transform", (text.upper(), text), ("A\nB", "a\nb"))
check("string methods have varied result types", (text.find("b"), text.split()),
      (2, ["a", "b"]))

# Function state, scope, deferred execution and exception propagation.
def accumulate(value, history=[]):
    history.append(value)
    return history


check("first mutable default", accumulate("A")[:], ["A"])
check("second mutable default", accumulate("B")[:], ["A", "B"])


def isolated(value, history=None):
    if history is None:
        history = []
    history.append(value)
    return history


check("fresh default state", (isolated("A"), isolated("B")), (["A"], ["B"]))


def alter(values):
    values.append(3)
    values = [99]
    return values


data = [1]
check("local rebind return", alter(data), [99])
check("caller sees mutation", data, [1, 3])
count = 10


def bump():
    count += 1


def bump_global():
    global count
    count += 1


raises("assignment makes local name", UnboundLocalError, bump)
bump_global()
check("global changes module binding", count, 11)


def add(left, right=2):
    return left + right


check("argument binding", (add(3), add(right=4, left=3)), (5, 7))
raises("duplicate argument", TypeError, lambda: add(3, left=4))
raises("unknown argument", TypeError, lambda: add(3, extra=4))


def do_nothing():
    pass


check("implicit return", do_nothing(), None)


def sum_to(n):
    if n < 0:
        raise ValueError("nonnegative input required")
    if n == 0:
        return 0
    return n + sum_to(n - 1)


check("recursive base case", sum_to(0), 0)
check("recursive small result", sum_to(4), 10)
raises("recursive negative input rejected", ValueError, lambda: sum_to(-1))
events = []


def small_generator():
    events.append("started")
    yield 4
    events.append("resumed")
    yield 6


stream = small_generator()
check("generator call is deferred", events[:], [])
check("first yield", next(stream), 4)
check("state before resumption", events[:], ["started"])
check("second yield", next(stream), 6)
raises("generator exhaustion", StopIteration, lambda: next(stream))
check("generator side effects", events, ["started", "resumed"])


def convert(text):
    return int(text)


def handled(text):
    try:
        return convert(text)
    except ValueError:
        return "bad value"
    except Exception:
        return "other ordinary error"


check("exception crosses call boundary", handled("oops"), "bad value")
check("different handler", handled(None), "other ordinary error")
check("normal path", handled("7"), 7)
check("hierarchy", (issubclass(IndexError, LookupError),
      issubclass(KeyError, LookupError), issubclass(ZeroDivisionError, ArithmeticError),
      issubclass(SystemExit, Exception), issubclass(KeyboardInterrupt, Exception)),
      (True, True, True, False, False))

print(json.dumps({"passed": len(passed), "checks": passed}, indent=2))
```

The JSON output reports `"passed": 82` and the labels of all passing checks. The 40 questions below remain separate reasoning prompts; an automated pass count does not prove understanding or predict an exam score.

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
28. How do the results of `.upper()`, `.find()` and `.split()` differ while preserving the original string?
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
7. For integers, `/` gives a float, `//` floors, and `%` supplies the matching remainder: `-11 // 4 == -3` and `-11 % 4 == 1`; `(-3)*4 + 1 == -11`. Truncating `-11/4` with `int()` gives `-2`, so it is a different operation.
8. They communicate intent and protect against a mistaken precedence assumption.
9. `and` short-circuits and returns an operand: `6 and 3` is `3`. Integer `6 & 3` is `2` because only the shared set bits remain. `not` returns a Boolean.
10. It returns text; arithmetic needs a compatible numeric conversion.
11. The separator between printed values and the text appended after the final value.
12. Separate conditions may all run; an `elif` chain selects the first truthy branch.
13. Values immediately below, exactly at, and immediately above each boundary.
14. Initial state, continuation condition, state change, and reachable termination.
15. `5, 3, 1`; stop zero is excluded.
16. Only the nearest enclosing loop.
17. The remainder of the current iteration, then execution proceeds to the next iteration test/item.
18. After normal exhaustion or a false `while` condition, including zero iterations. A `break`, return or exception escaping the loop skips its `else`; `continue` alone does not.
19. Removing or inserting changes indices and the remaining traversal while it is in progress.
20. Direct indexing raises `IndexError`; slicing can stop beyond the sequence without that error.
21. Assignment aliases the same list; a full slice creates a new outer list.
22. References to nested mutable objects.
23. Parentheses group the expression; the comma defines the tuple item.
24. Yes. The tuple's reference cannot be replaced, but the referenced list remains mutable.
25. Keys.
26. When the loop needs both each key and its associated value.
27. Absence and presence-with-a-false-value represent different states; use explicit membership for existence.
28. `.upper()` returns transformed string text, `.find()` an integer position or `-1`, and `.split()` a list of strings. None mutates the original string. Avoid assuming every method returns a string or a distinct object identity.
29. Source characters such as backslash-plus-letter versus the one resulting escaped character.
30. Parameters are definition-side names; arguments are call-side supplied values.
31. Printing is an output side effect; returning passes a value to the caller for reuse.
32. `None`.
33. A nearer-scope binding hides an outer one. Assignment makes a name local in an ordinary function unless declared otherwise; reading that local before binding raises `UnboundLocalError`. `global` targets the module binding.
34. The default object is created when the definition executes and reused by later omitted-argument calls.
35. A reachable base case and progress toward it on every recursive path.
36. Calling a generator function creates its iterator without running the body. `next()` or iteration resumes it to a `yield`; later requests resume after that point. Completion raises `StopIteration` to the iterator consumer. `return` ends execution.
37. The parent also matches child exceptions, so placing it first captures the case too early.
38. `SystemExit` and `KeyboardInterrupt` in the published set.
39. Unsuitable value for a valid operation; incompatible operand/type; missing sequence index; missing mapping key.
40. Confirm that PCEP-30-02 is still the active purchasable version and that your resources match its syllabus; PCEP-30-03 is announced but not yet shown as current.

## Readiness checklist

- Trace values, types and object identity without treating them as the same question.
- Explain negative floor/modulo and power grouping; distinguish Boolean operand selection from bitwise operations.
- Separate compile-time syntax rejection, runtime exceptions and incorrect logic that raises nothing.
- Trace all loop exits, empty input and nested `break` scope.
- Draw outer and nested aliases; predict mutating method returns and dictionary view changes.
- Bind arguments, identify retained default state, and explain local/global names.
- Trace a small terminating recursion, deferred generator execution and exception propagation.
- Recheck the actual purchasable exam version and current policies before booking.

## Source and freshness notes

- The detailed syllabus controls the four block names, item counts, weights, and topic boundary. The [PCEP credential page](https://pythoninstitute.org/pcep/) controls current version, delivery, price, language, prerequisite, validity, and retake details.
- The official practice product currently disagrees with the syllabus by one percentage point in blocks 2 and 3. The syllabus is used here; revalidate both pages when PCEP-30-03 launches.
- The direct source checker timed out for Python Institute and Harvard, while the web reader retrieved their public pages. Those access paths are reported separately; no successful direct monitor/hash comparison is claimed. The current displayed syllabus was compared with the retained objective snapshot, which was not rewritten. The PDF was read through extracted page text, not downloaded as a locally hashed PDF.
- The [PCEP testing policies](https://pythoninstitute.org/pcep-testing-policies) describe proctored delivery and a seven-day wait after failure. The credential page and practice store disagree about which account role redeems practice access; follow current vendor instructions for your account. No account, purchase, voucher redemption or exam attempt was performed.
- Python behavior is grounded in the versioned references above and the [Python tutorial](https://docs.python.org/3/tutorial/). Only selected documentation sections were read; source capture does not mean the entire language reference or linked courses were completed.
- This guide paraphrases the public objectives and uses original examples, scenarios, labs, checks, and answers. It contains no recalled/live items, answer dumps, or copied paid-course questions.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one coherent primary course or book, write and debug code for every block, and use one explanation-led assessment to identify gaps. The official syllabus—not any third-party “pass” claim—is the final scope authority.

| Resource | Access | Estimated time |
|---|---|---:|
| [PCEP-30-02 exam syllabus](https://pythoninstitute.org/pcep-exam-syllabus/) | Free official blueprint | 1–2 hours to map and recheck |
| [Python Essentials 1](https://edube.org/study/pe1) | Free official aligned self-study; account required | 42 hours listed |
| [Cisco Networking Academy Python Essentials 1](https://www.netacad.com/courses/python-essentials-1) | Free official partner listing; direct response was an application shell | Current runtime not verified; earlier 30–42-hour estimate retained only as historical context |
| [OpenEDG PCEP practice-test compendium](https://ums.edube.org/products/0-pi-pcep-3002-pt) | Paid official practice; public terms describe five launches per test and 12-month voucher redemption validity; items not accessed | 4–8 hours is an author planning estimate, not a listed runtime |
| [Microsoft Learn: Python Programming Fundamentals](https://learn.microsoft.com/en-us/training/paths/get-started-with-python-fundamentals/) | Free four-module fundamentals/tooling path; public descriptions read, lessons not completed | Current total not displayed in capture; prior 3h12m not reverified |
| [Pluralsight Python Essentials](https://www.pluralsight.com/paths/python-essentials) | Subscription; public list shows 17 courses, 25 labs and broader material; interiors not accessed | Headline 47 hours; Foundations + Data Structures + Functions/Modules listings total 6h15m, before practice |
| [Learning Python, 6th Edition](https://www.oreilly.com/library/view/learning-python-6th/9781098171292/) | O'Reilly subscription/book; direct HTTP 403; current metadata/interior unverified | Author estimate 15–25 hours selectively; historical 42h20m not reverified |
| [Udemy: Python PCEP by Adrian Wiech](https://www.udemy.com/course/python-pcep/) | Paid marketplace listing; direct HTTP 403; current contents unverified | Historical 4h27m not reverified; author estimate 6–10 extra practice hours |
| [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/) | Free Harvard OpenCourseWare; web reader confirmed ten-week course and first four topic headings; lectures/problems not completed | Select weeks 0–3; 15–25 hours is an author estimate |
| [freeCodeCamp beginner Python course](https://www.youtube.com/watch?v=rfscVS0vtbw) | Free older YouTube course; direct capture only verified title, no playback | Historical about 4h26m not reverified; add coding time |

No exact current PCEP product from Whizlabs or MeasureUp, and no dedicated PCEP path on Pluralsight or O'Reilly, was independently verified in this review; that is a search boundary, not proof none exists. Generic resources can teach Python well without matching every exam edge; reconcile them against the four blocks. Prices, access, runtimes, course revisions, practice weights, and exam-version claims are volatile—verify before purchase, especially during the PCEP-30-03 transition.

The Edube landing lists 42 hours and four course sections, but an account would be needed to assess the lessons. The practice store lists voucher redemption and launch limits; it does not establish paid-item quality. Pluralsight lists Foundations (2h41m), Data Structures (1h56m) and Simplifying Python Applications Through Functions and Modules (1h38m): the 6h15m sum is catalog arithmetic, not a full PCEP coverage claim. Microsoft's path currently lists first code, data, VS Code setup and decisions; neither its four-module count nor its tooling overview proves functions, generators and exception coverage. None of these courses was completed during this review.
