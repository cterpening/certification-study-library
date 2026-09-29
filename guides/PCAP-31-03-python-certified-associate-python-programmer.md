---
exam_code: PCAP-31-03
vendor_id: python-institute
official_blueprint: https://pythoninstitute.org/pcap-exam-syllabus
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-29
---

# PCAP-31-03 Certified Associate Python Programmer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked September 29, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#pcap-31-03-coverage-record). The [official PCAP syllabus](https://pythoninstitute.org/pcap-exam-syllabus) is authoritative.

**Current baseline:** PCAP-31-03, active; detailed five-section syllabus last updated March 7, 2022<br>
**Upcoming blueprint change:** PCAP-31-04 is in development and was announced for Q3 2026, but the live credential page still identifies PCAP-31-03 as current; verify the purchasable code immediately before booking<br>
**Official delivery snapshot:** 40 questions; 65-minute exam plus 10-minute NDA/tutorial; 70% passing score; single-select, multiple-select, interactive, and scenario-based items; TestNow or Pearson VUE/OnVUE<br>
**VERIFY CURRENT — credential snapshot:** the English page lists no formal prerequisite, five-year validity, exam from USD 295 and a 15-day failed-retake wait. The [Japanese credential page](https://pythoninstitute.org/ja/pcap) still says lifetime validity. Confirm the terms for your exam/version before purchase; this review did not inspect booking or an account.<br>

The September 29 review manually compared all **21 numbered objectives**, grouped 5/2/3/6/5, with the public English syllabus. Direct fetching and automated monitoring failed; the retained snapshots are not a successful new hash comparison. The syllabus HTML contains an unusual per-item scoring statement, while its [dated PDF cover](https://pythoninstitute.org/assets/627e61fa6fe27591613128.pdf) reports section raw-score totals. Use the published weights and overall pass threshold; do not infer equal points per question or a number of correct answers that guarantees a pass.

The [PCAP TestNow policy](https://www.pythoninstitute.org/pcap-testing-policies) specifies proctoring and 15 days after failure, but a generic footer says seven days. The [Pearson policy](https://pythoninstitute.org/pvue-testing-policies) also specifies 15 days for failure and prohibits retaking the same passed version. The exam-specific rule is the study baseline; confirm channel-specific terms before booking. The English page still announces Q3 2026 for version 31-04 without marking it active as of this review; the calendar alone does not establish a launch.

## How to use this guide

PCAP moves from isolated Python statements to maintainable, multi-module programs. Study by predicting behavior, implementing the smallest example, and then deliberately breaking it. For each syllabus item:

1. explain the concept without looking it up;
2. trace a short example, including object identity and exception paths;
3. implement it in a disposable Python 3 environment;
4. add a boundary or failure case;
5. state why you would choose the construct in a real program.

**Practice version:** original examples were executed on existing CPython 3.13.14. The unversioned documentation index currently shows 3.14.7; pinned 3.13 references below describe the tested behavior. No exact exam-required Python patch version is inferred.

PCEP-level control flow, collections, functions, and basic exceptions are assumed foundations even when they are not separate PCAP sections. Type annotations, async programming, web frameworks, and packaging/build standards are useful professional knowledge, but do not let them displace this exact blueprint.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Weighted objective map

| Section | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| 1. Modules and Packages | 6 | 12% | Build a small nested package, predict import bindings, and diagnose search-path behavior |
| 2. Exceptions | 5 | 14% | Design a useful custom hierarchy and trace `raise`, matching, propagation, `else`, and `finally` |
| 3. Strings | 8 | 18% | Reason about Unicode/code points and predict every listed string operation |
| 4. Object-Oriented Programming | 12 | 34% | Model a domain with class/instance state, inheritance, overriding, introspection, and constructors |
| 5. Comprehensions, Lambdas, Closures, and I/O | 9 | 22% | Transform data functionally and process text/binary files with explicit failure handling |

The numbered scope maps as follows; item counts differ from weights. The code below exercises examples of these contracts, not every possible input.

| Objective IDs | Teaching and executed evidence |
|---|---|
| 1.1–1.5 | Import bindings, six math calls, random boundaries, seven platform calls, package and cache probes |
| 2.1–2.2 | Core control-flow traces, domain hierarchy, propagation and re-raise checks |
| 3.1–3.3 | Unicode/string workbook and strict UTF-8 catalog |
| 4.1–4.6 | Object-state/MRO workbook and report package |
| 5.1–5.3 | Nested comprehension order, lazy iterators, closure capture |
| 5.4–5.5 | Stream contracts, binary checksum buffer and actual temporary-file checks |

## 1. Modules and packages — 12%

### Imports are namespace operations

`import package.module` binds the top-level package name and keeps qualification visible. `from package import module` binds `module` directly. `from module import name` copies that object reference into the importing namespace; later rebinding in either module does not automatically update the other binding. An alias changes the local name, not the imported object's identity.

Avoid `from module import *`: the imported public-name set is less obvious, collisions become easy, and readers cannot see where a name came from. The exam includes it, so know how it behaves, but treat explicit imports as the maintainable default. A module’s `__all__` defines its star exports when present, even permitting explicitly listed underscore names. Otherwise names beginning with `_` are omitted. A package star import does not discover every file recursively.

`dir(object)` returns available attribute names for inspection; without an argument it describes the current local namespace. It is discovery, not a contractual API. `sys.path` is the ordered module search path. The current working context, environment, installation, and runtime configuration can affect it, so a module that imports on one machine may fail on another.

> **Related item:** A virtual environment isolates an interpreter and its installed distributions. It does not make arbitrary changes to `sys.path` safe, nor does it replace a declared dependency file.

### User-defined modules and packages

A module is normally a Python file; a package organizes modules beneath a package namespace. `__init__.py` traditionally marks and initializes a regular package. Modern namespace packages can omit it, but the published PCAP objective explicitly includes it, so practice regular packages first.

When a module executes, `__name__` is its import name; for the directly executed top-level file, it is `"__main__"`. Put reusable definitions at module level and launch-only work beneath `if __name__ == "__main__":` so importing the module does not unexpectedly run the program.

Imports normally reuse the object already cached under that name in `sys.modules`; repeatedly importing it does not repeatedly execute its body. Removing cache entries or explicitly reloading changes that situation. Imported names share object references, so mutating an imported list is visible through both bindings even though rebinding a scalar is not.

Python may cache compiled bytecode in `__pycache__`. That is an implementation artifact, not source to edit or a dependency to commit. A leading underscore communicates non-public intent; it does not enforce privacy.

Build and explain this structure:

```text
shop/
  __init__.py
  pricing.py
  reports/
    __init__.py
    daily.py
```

Predict which names are bound by `import shop.pricing`, `from shop import pricing`, and `from shop.pricing import calculate`. Then run them from a stable project root. The complete report package below demonstrates relative imports with `python -m reports`; invoking its `__main__.py` as a bare file loses that package context. The [modules chapter](https://docs.python.org/3.13/tutorial/modules.html) explains import initialization, search and cache behavior.

### Standard-library modules in scope

- `math.ceil(x)` moves to the least integer not below `x`; `floor(x)` moves to the greatest integer not above it; `trunc(x)` removes the fractional part toward zero. Their difference is clearest for negatives.
- `factorial(n)` requires a nonnegative integer; an integral-valued float such as `6.0` is rejected in Python 3.10 and later. For ordinary real inputs, `sqrt(-1)` raises `ValueError`; `hypot(5, 12)` returns `13.0`. See the [math reference](https://docs.python.org/3.13/library/math.html).
- `random.random()` produces a float in `[0.0, 1.0)`; `choice(sequence)` selects one member; `sample(population, k)` selects occurrences without replacement and leaves the population unchanged. Equal values can appear twice when the population contains duplicates. `choice([])` raises `IndexError`; invalid sample sizes raise `ValueError`. The tested 3.13 sampler requires a sequence, not a set.
- `random.seed()` supports reproducible pseudo-random sequences for testing. Replay requires the same calls, input order and compatible implementation; do not promise that `sample()` produces an identical sequence across all Python versions. A separate `random.Random(seed)` instance isolates its state from the module generator. The [random reference](https://docs.python.org/3.13/library/random.html) limits its cross-version guarantee to `random()` with a compatible seeder. The generator is unsuitable for secrets.
- `platform` functions expose reported machine, processor, system, version, implementation, and Python version tuple. The scoped calls are `platform()`, `machine()`, `processor()`, `system()`, `version()`, `python_implementation()` and `python_version_tuple()`. The last returns three strings, not integers. Reported OS/machine detail may be empty or platform-dependent; `platform()` is for human display, not a stable parser input. See the [platform reference](https://docs.python.org/3.13/library/platform.html).

> **Related item:** Security tokens, password reset links, and cryptographic keys require the `secrets` module or a suitable security library, not `random`. That distinction is operational context beyond the listed PCAP calls.

## 2. Exceptions — 14%

### Matching, control flow, and propagation

When code inside `try` raises, Python searches `except` clauses from top to bottom and runs the first compatible handler. A parent class catches its descendants, so specific handlers must precede broad ones. `except (TypeError, ValueError) as exc` groups alternatives and binds the current exception.

The `else` suite runs only after normal fall-through from `try`: no exception and no `return`, `break` or `continue`. An exception in `else` is not handled by the preceding `except` clauses. Place success-only work there. `finally` runs as control leaves the construct whether execution succeeded, returned, or raised, making it suitable for unavoidable cleanup. A `return` or new exception from `finally` can replace an earlier result or failure; keep cleanup free of control-flow overrides. Abrupt process termination is outside this guarantee. Prefer context managers for resources that support them. See [exception handling](https://docs.python.org/3.13/tutorial/errors.html) and the precise [try-statement rules](https://docs.python.org/3.13/reference/compound_stmts.html).

`raise DomainError("message")` starts an exception. Bare `raise` inside a handler re-raises the current exception while preserving its traceback. `raise exc` raises the named object from that line and can change traceback presentation. Exceptions propagate through callers until a matching handler is found or the program terminates.

`assert condition, message` raises `AssertionError` when the condition is false, but assertions can be disabled with optimization. Use them for internal invariants, not validation of untrusted input or required business rules.

### Custom exception hierarchies

Derive ordinary application exceptions from `Exception`, usually with one domain base:

```python
class PricingError(Exception):
    pass

class UnknownCurrencyError(PricingError):
    pass
```

This lets callers catch one precise condition or the whole domain family. `BaseException` is intentionally above ordinary application errors and includes exit/interrupt signals you usually should not absorb. The `.args` tuple contains constructor arguments unless a subclass defines a different contract. The `as exc` target is cleared after its handler, so explicitly save information you need later. A sibling handler does not catch a new exception raised inside the selected handler.

> **Related item:** Translate an exception only when the new type adds a meaningful abstraction boundary. Chaining with `raise NewError(...) from exc` is professional context that preserves cause, although explicit chaining is developed further in PCPP1.

## 3. Strings — 18%

### Characters, code points, and encodings

Unicode assigns code points to characters; an encoding such as UTF-8 maps text to bytes and bytes back to text. ASCII covers a small historical character set and is compatible with UTF-8 for its 0–127 range. A Python `str` is text; a `bytes` value is encoded binary data. Confusing the two causes both program errors and corrupted text.

`ord(character)` returns a code point integer and `chr(integer)` performs the inverse for a valid code point. Escape sequences represent characters in source, but the resulting string contains the interpreted character. `len()` counts Python string elements/code points, not encoded byte length and not necessarily user-perceived grapheme clusters.

> **Related item:** Unicode normalization can make visually identical text have different code-point sequences. Normalization is not listed explicitly, but it explains why production identity and search logic may need more than lowercasing.

### Operations and methods

Strings are immutable ordered sequences. Indexing returns one-character strings; slicing returns a new string; an overlong slice is tolerated while an invalid direct index raises `IndexError`. Concatenation and repetition create new values. Comparisons between strings are lexicographic by code point, not natural-language collation. `"12" == 12` is false; ordering `"12" < 12` raises `TypeError`. No implicit numeric parsing occurs.

Know the contracts and failure behavior:

- `isalpha()` and `isalnum()` require at least one character and permit Unicode letters/numbers. `isdecimal()` is narrower than `isdigit()`, which is narrower than `isnumeric()`; superscript `²` is a digit but not a decimal digit, and fraction `⅓` is numeric but not a digit. None of these is a complete signed-number parser.
- `islower()`/`isupper()` examine cased characters and require at least one: `"a7!".islower()` is true. `"7!".islower()` is false. `"".isascii()` is true, so “all classification methods reject empty text” is wrong. `isspace()` requires nonempty whitespace.
- `separator.join(iterable)` places the separator between string items; the separator is the method receiver.
- `text.split(separator)` returns pieces; omitting the separator uses runs of whitespace and has different empty-field behavior.
- `strip(chars)` removes matching characters from both ends, not a literal prefix/suffix.
- `index(sub)` returns a position or raises `ValueError`; `find(sub)`/`rfind(sub)` return `-1` when absent.
- `sorted(text)` returns a new list of characters; strings have no `.sort()` method. A mutable list’s `.sort()` changes that list and returns `None`. Read [string contracts](https://docs.python.org/3.13/library/stdtypes.html) and [built-in functions](https://docs.python.org/3.13/library/functions.html).

Test empty strings, missing substrings, repeated substrings, non-ASCII text, leading/trailing whitespace, and mixed case.

## 4. Object-oriented programming — 34%

### State belongs either to the class or an instance

A class describes construction and shared behavior; an instance carries individual state. `__init__(self, ...)` initializes an already created instance and should establish its invariant. Instance methods receive the instance as `self` by convention.

A class variable is found through the class and may be shared by instances. Assignment through an instance normally creates/shadows an instance attribute; mutation of a shared mutable class attribute affects every instance that reaches it. Put per-instance mutable state in `__init__`.

`obj.__dict__` commonly shows that instance's writable attributes; `Class.__dict__` is the class namespace mapping. Attribute lookup also follows inheritance, so absence from an instance dictionary does not mean attribute access will fail. `__dict__` is not universal: a slotted instance may lack it. `hasattr(obj, name)` performs real lookup, including custom lookup/property behavior; it returns false for `AttributeError` but propagates other errors. It is not a side-effect-free dictionary membership test.

Within a class definition, a name with at least two leading underscores and at most one trailing underscore is mangled using the defining class; `__name__`-style special names are not covered by that rule. It reduces accidental collision in subclasses but is not security or strict privacy. A single leading underscore remains the usual non-public convention.

### Inheritance, overriding, and polymorphism

Inheritance models an **is-a** relationship; composition models **has-a** and is often less coupled. A subclass can override a method, and polymorphism lets calling code use the same interface across different concrete types. `isinstance(obj, Class)` accounts for subclasses; `type(obj) is Class` requires an exact type. `is` tests object identity, while `==` asks for value equality.

Multiple inheritance creates a method-resolution order (MRO). In a diamond, Python's C3 MRO provides one consistent lookup sequence. Inspect `Class.__mro__` while learning, even though the blueprint names `__bases__` specifically. `super()` searches after the defining class in the actual instance’s MRO, so its next method can belong to a sibling. Cooperative methods/constructors use compatible signatures and `super()` consistently; directly invoking selected parents can initialize one branch twice or skip another.

Override `__str__` to provide a useful human-readable representation. Returning a non-string from `__str__` is an error. Introspection properties in scope include a class's `__name__`, `__module__`, and direct-base tuple `__bases__`.

```python
class Report:
    category = "general"

    def __init__(self, title):
        self.title = title

    def render(self):
        return self.title

    def __str__(self):
        return f"Report({self.title!r})"

class LabeledReport(Report):
    def render(self):
        return f"Title: {self.title}"
```

This example renders plain text. The [classes chapter](https://docs.python.org/3.13/tutorial/classes.html) explains instance state, method binding and inheritance. `__init__` initializes an already allocated object and must return `None`; when a subclass supplies its own initializer, call the inherited initializer deliberately if its setup is required.

Trace `category` through class and instance access, inspect both dictionaries, override it through one instance, and call `render()` through a list containing both types.

> **Related item:** Substitutability is a better inheritance test than code reuse alone: code expecting the parent contract should continue to work correctly with the child.

## 5. Comprehensions, lambdas, closures, and I/O — 22%

### Compact transformation without hidden behavior

A list comprehension combines an output expression, iteration, and optional filter. Nested comprehensions follow the same order as equivalent nested `for` statements. Rewrite any dense comprehension as ordinary loops until you can prove its order, scope, and output. The leftmost `for` supplies the outer iteration; the inner expression runs only after filters pass. See [comprehensions](https://docs.python.org/3.13/tutorial/datastructures.html).

A lambda creates an anonymous single-expression function. It is useful for a small callback/key, not for hiding multi-step logic. `map(function, iterable)` lazily transforms items and `filter(predicate, iterable)` lazily keeps matching items; both iterators are consumed as they are read. `map` with multiple inputs stops at the shortest in the tested version; convert to a list only when materialization is needed. A comprehension is often clearer when the transformation/filter is simple.

A closure is a function that retains access to names from an enclosing function after that enclosing call finishes. Closures capture bindings, not frozen snapshots. In loops, late binding can make several closures observe the same final variable; bind a value intentionally through a factory call or default parameter. A default argument stores the object reference at definition time, not a deep copy of a mutable object. The [lambda section](https://docs.python.org/3.13/tutorial/controlflow.html) demonstrates enclosing-scope references.

### Text and binary I/O

A stream transfers data; the file object returned by `open()` is the Python handle used to interact with it. The predefined streams `sys.stdin`, `sys.stdout` and `sys.stderr` normally provide text input, ordinary output and diagnostics; they may be redirected/replaced, so do not assume a terminal or hard-code an encoding. Text mode decodes/encodes `str`; binary mode transfers `bytes`. Common modes include read (`r`), write/truncate (`w`), append (`a`), exclusive creation (`x`), update (`+`), binary (`b`), and text (`t`). Choose a mode from the intended safety behavior, not habit.

Use `with open(path, mode, encoding="utf-8") as stream:` so the stream closes even on failure. `read()` consumes some or all data, `readline()` one line, and `readlines()` a list of remaining lines. Iterating the stream is usually memory-efficient. `readline()` preserves a present line ending: `"\n"` is a blank line, while `""` indicates text EOF. Binary EOF is `b""`. `write()` returns the number of characters/bytes accepted and does not add a newline automatically. Text newline translation is separate from encoding. An accepted write is not a promise of crash durability. See the [I/O tutorial](https://docs.python.org/3.13/tutorial/inputoutput.html).

`bytearray` is a mutable byte buffer suitable for binary I/O. For a blocking regular binary file, `readinto(buffer)` returns a count; consume only `buffer[:count]`, since the unused tail can contain bytes from a previous read. A zero count with a nonempty buffer indicates EOF. Nonblocking streams have additional behavior; the worked example deliberately uses blocking regular files. See [stream methods](https://docs.python.org/3.13/library/io.html). Do not decode arbitrary bytes without knowing their encoding. `OSError` and subclasses expose operating-system failures; `errno` constants let code compare portable symbolic conditions when handling a truly expected case. For example, [`errno.ENOENT`](https://docs.python.org/3.13/library/errno.html) describes a missing path; `PermissionError` is a different failure. Do not catch every `OSError` and continue as though a write succeeded.

> **Related item:** A safe update often writes to a temporary file, flushes it, and atomically replaces the destination where the platform supports that pattern. This operational technique is beyond the basic calls but protects against partial output.

## Executed core workbook

Save as `workbook.py` and run `python workbook.py`. Its explicit checks run even if assertions are optimized away; the separate optimization demonstration uses `assert` only to show that boundary. The tested CPython 3.13.14 run prints `78 core checks passed`. Original fixtures cover defined language behavior; they are not certification items.

```python
"""Original PCAP practice. Run normally, not with -O."""
import math
import platform
import random

checks = 0


def check(condition):
    global checks
    if not condition:
        raise AssertionError(f"Check {checks + 1} failed")
    checks += 1


def rejects(error, function, *args):
    try:
        function(*args)
    except error:
        check(True)
    else:
        raise AssertionError(f"Expected {error.__name__}")


for value, expected in [(-2.75, (-2, -3, -2)), (2.75, (3, 2, 2))]:
    check((math.ceil(value), math.floor(value), math.trunc(value)) == expected)
check(math.factorial(0) == 1)
check(math.factorial(6) == 720)
rejects(ValueError, math.factorial, -1)
rejects(TypeError, math.factorial, 6.0)
check(math.sqrt(81) == 9)
rejects(ValueError, math.sqrt, -1)
check(math.hypot(5, 12) == 13)
rng = random.Random(91)
check(0 <= rng.random() < 1)
check(rng.choice(["only"]) == "only")
rejects(IndexError, rng.choice, [])
check(rng.sample(["same", "same"], 2) == ["same", "same"])
rejects(ValueError, rng.sample, [1], 2)
rng.seed(19)
first = [rng.random() for _ in range(4)]
rng.seed(19)
check(first == [rng.random() for _ in range(4)])
for name in ("platform", "machine", "processor", "system", "version",
             "python_implementation"):
    check(isinstance(getattr(platform, name)(), str))
version = platform.python_version_tuple()
check(len(version) == 3 and all(isinstance(part, str) for part in version))


class DataError(Exception):
    pass


class EmptyError(DataError):
    pass


def trace(mode, events):
    try:
        events.append("try")
        if mode == "child":
            raise EmptyError("empty", 0)
        if mode == "parent":
            raise DataError("bad")
        if mode == "return":
            return "early"
        if mode == "unhandled":
            raise TypeError("wrong type")
    except EmptyError as exc:
        events.append(("child", exc.args))
    except DataError:
        events.append("parent")
    else:
        events.append("else")
    finally:
        events.append("finally")
    return "end"


for mode, expected in [
    ("ok", ["try", "else", "finally"]),
    ("child", ["try", ("child", ("empty", 0)), "finally"]),
    ("parent", ["try", "parent", "finally"]),
    ("return", ["try", "finally"]),
]:
    events = []
    check(trace(mode, events) == ("early" if mode == "return" else "end"))
    check(events == expected)
events = []
rejects(TypeError, trace, "unhandled", events)
check(events == ["try", "finally"])

check(ord("Z") == 90 and chr(90) == "Z")
check(len("e\u0301") == 2 and len("é".encode("utf-8")) == 2)
check("é" != "e\u0301")
check("trail"[-1] == "l" and "trail"[50:] == "")
rejects(IndexError, "trail".__getitem__, 50)
check("ab" * 2 == "abab" and "ab" + "c" == "abc")
check("Z" < "a" and "ail" in "trail" and "x" not in "trail")
check("12" != 12)
rejects(TypeError, lambda: "12" < 12)
for text, expected in [("", (False, False, False)),
                       ("7", (True, True, True)),
                       ("²", (False, True, True)),
                       ("⅓", (False, False, True))]:
    check((text.isdecimal(), text.isdigit(), text.isnumeric()) == expected)
check("é".isalpha() and "é7".isalnum())
check("a7!".islower() and "A7!".isupper())
check(not "7!".islower() and not "".isupper())
check(" \t".isspace() and not "".isspace())
check("".isascii() and not "é".isascii())
check("|".join(["a", "b"]) == "a|b")
rejects(TypeError, "|".join, ["a", 1])
check("a,,b,".split(",") == ["a", "", "b", ""])
check(" \ta  b ".split() == ["a", "b"])
check("".split() == [] and "".split(",") == [""])
check("abbaXba".strip("ab") == "X")
check("ababa".find("ba") == 1 and "ababa".rfind("ba") == 3)
check("ababa".find("x") == -1)
rejects(ValueError, "ababa".index, "x")
check(sorted("cba") == ["a", "b", "c"])
rejects(AttributeError, getattr, "cba", "sort")


class Record:
    category = "shared"

    def __init__(self, name):
        self.name = name
        self.tags = []
        self.__token = "internal"

    def __str__(self):
        return self.name


one, two = Record("one"), Record("two")
one.tags.append("new")
check(two.tags == [] and one.tags is not two.tags)
check("category" not in one.__dict__ and Record.__dict__["category"] == "shared")
one.category = "local"
check(one.category == "local" and two.category == "shared")
check(one.__dict__["_Record__token"] == "internal")
check(not hasattr(one, "__token") and hasattr(one, "_Record__token"))
check(str(one) == "one" and Record.__name__ == "Record")
check(Record.__bases__ == (object,))


class Root:
    def route(self):
        return ["Root"]


class Left(Root):
    def route(self):
        return ["Left"] + super().route()


class Right(Root):
    def route(self):
        return ["Right"] + super().route()


class Join(Left, Right):
    pass


joined = Join()
check(joined.route() == ["Left", "Right", "Root"])
check(Join.__mro__ == (Join, Left, Right, Root, object))
check(isinstance(joined, Root) and type(joined) is Join)
check(joined is joined and joined is not Join())
check([(x, y) for x in [1, 2] for y in [2, 3] if x != y]
      == [(1, 2), (1, 3), (2, 3)])
mapped = map(lambda n: n * 3, [1, 2])
check(list(mapped) == [3, 6] and list(mapped) == [])
check(list(filter(lambda n: n > 0, [-1, 0, 2])) == [2])
late = [lambda: i for i in range(3)]
early = [lambda i=i: i for i in range(3)]
check([f() for f in late] == [2, 2, 2])
check([f() for f in early] == [0, 1, 2])


def threshold(minimum):
    return lambda value: value >= minimum


check(threshold(3)(3) and not threshold(3)(2))
print(f"{checks} core checks passed")
```

## Integrated scenarios

### Scenario 1: Report package

Create the following files beneath a disposable project directory. Both concrete renderers accept a list/tuple of text rows, store an immutable tuple snapshot and return text. Plain output preserves embedded newlines for display, so it is not a reversible row format. CSV writes one field per row and quotes commas, quotes and newlines through the [standard CSV writer](https://docs.python.org/3.13/library/csv.html). CSV is adjacent implementation context; inheritance, imports and exceptions are the objectives practiced here.

File `reports/__init__.py`:

```python
"""Original report package; importing it prints nothing."""
```

File `reports/errors.py`:

```python
class ReportError(Exception):
    pass


class ReportFormatError(ReportError):
    pass
```

File `reports/base.py`:

```python
from .errors import ReportFormatError


class Report:
    category = "plain data"

    def __init__(self, rows):
        if not isinstance(rows, (list, tuple)):
            raise ReportFormatError("rows must be a list or tuple")
        if not all(isinstance(row, str) for row in rows):
            raise ReportFormatError("every row must be text")
        self.rows = tuple(rows)

    def render(self):
        raise NotImplementedError("choose a concrete renderer")

    def __str__(self):
        return f"{type(self).__name__}({len(self.rows)} rows)"
```

File `reports/renderers/__init__.py`:

```python
"""Renderers are imported explicitly from their modules."""
```

File `reports/renderers/text.py`:

```python
from ..base import Report


class TextReport(Report):
    def render(self):
        return "\n".join(self.rows) + ("\n" if self.rows else "")
```

File `reports/renderers/csv_report.py`:

```python
import csv
from io import StringIO
from ..base import Report


class CsvReport(Report):
    def render(self):
        output = StringIO(newline="")
        writer = csv.writer(output, lineterminator="\n")
        for row in self.rows:
            writer.writerow([row])
        return output.getvalue()
```

File `reports/__main__.py`:

```python
from .renderers.text import TextReport
from .renderers.csv_report import CsvReport


def main():
    for report in (TextReport(["pear", "plum"]), CsvReport(["pear, plum"])):
        print(report.render(), end="")


if __name__ == "__main__":
    main()
```

From that project directory run `python -m reports`. It prints `pear`, `plum`, then the quoted CSV field `"pear, plum"`, each followed by a newline. Importing either the package or its entry module prints nothing. Running `python reports/__main__.py` directly is intentionally unsupported because the relative imports need package context.

The review executed import-binding, cache/bytecode, explicit/default star-export and shared-object/rebinding probes. It also round-tripped comma/quote/newline/Unicode/empty fields with the CSV reader, rejected invalid row types, verified tuple snapshot isolation and checked polymorphic render calls.

### Scenario 2: Unicode catalog

Save as `catalog.py`; run `python -X utf8 catalog.py` for a temporary-file demonstration. The small-file contract is one product per LF-delimited line, optionally CRLF; surrounding whitespace is stripped, interior blank rows rejected, and an empty file accepted. Case and Unicode normalization are preserved. Grouping is by the first code point, so visually similar spellings need not share a key. This is not a streaming large-file processor.

The digest covers the exact raw bytes captured once, including whitespace/newlines. It is a [SHA-256 checksum](https://docs.python.org/3.13/library/hashlib.html), not an authenticity check. Strict decode and validation occur before exclusive output creation, preserving existing output. An operating-system failure during writing may still leave a partial newly created output; the function propagates that failure and does not promise an atomic transaction.

```python
"""Small, trusted local catalog; one product per LF-delimited line."""
import hashlib


class CatalogError(Exception):
    pass


def load_catalog(source, digest_destination):
    # Read once: names and digest describe the same captured bytes.
    with open(source, "rb") as stream:
        raw = stream.read()
    text = raw.decode("utf-8")  # Strict decoding; no silent replacement.
    lines = text.split("\n")
    if lines[-1] == "":
        lines.pop()  # Empty file or one final LF, not interior blank rows.
    groups = {}
    for number, line in enumerate(lines, 1):
        name = line.strip()
        if not name:
            raise CatalogError(f"empty product on line {number}")
        groups.setdefault(name[0], []).append(name)
    digest = hashlib.sha256(raw).digest()
    # Exclusive creation preserves any existing destination.
    with open(digest_destination, "xb") as stream:
        stream.write(digest)
    return groups


def read_payload(path, chunk_size=7):
    if type(chunk_size) is not int or chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")
    result = bytearray()
    buffer = bytearray(chunk_size)
    with open(path, "rb") as stream:
        while True:
            count = stream.readinto(buffer)
            if count == 0:
                break
            result.extend(buffer[:count])  # Tail bytes may be stale.
    return bytes(result)


if __name__ == "__main__":
    from pathlib import Path
    from tempfile import TemporaryDirectory
    with TemporaryDirectory(prefix="pcap-catalog-") as directory:
        source = Path(directory) / "products.txt"
        destination = Path(directory) / "digest.bin"
        source.write_bytes("éclair\nemoji🙂\n".encode("utf-8"))
        print(load_catalog(source, destination))
        print(len(read_payload(destination)), "digest bytes")
```

The demo reports the `é` and `e` groups and `32 digest bytes`. Actual temporary-file checks include a final line without LF, accents, emoji, combining characters, case differences, empty input, embedded blank rows, invalid UTF-8, missing paths, existing output and buffer sizes that do not divide 32. Compare only the valid prefix after each `readinto` call; a stale tail must never be appended.

### Scenario 3: Reproducible sampler

Save as `sampler.py`; run `python sampler.py`. Here record identity is a nonempty string, duplicate IDs are rejected, and `k` and the seed must be actual integers rather than booleans. These are deliberate application rules, not extra restrictions imposed by every `random` API. The original input and the global random generator remain unchanged.

```python
"""Select unique string IDs from a small in-memory list or tuple."""
import random


class SamplingError(Exception):
    pass


def select_ids(record_ids, k, seed):
    if not isinstance(record_ids, (list, tuple)):
        raise SamplingError("IDs must be a list or tuple")
    if any(not isinstance(item, str) or not item for item in record_ids):
        raise SamplingError("each ID must be a nonempty string")
    if len(set(record_ids)) != len(record_ids):
        raise SamplingError("duplicate IDs")
    if type(k) is not int or not 0 <= k <= len(record_ids):
        raise SamplingError("k must be an integer within the population size")
    if type(seed) is not int:
        raise SamplingError("seed must be an integer")
    return random.Random(seed).sample(record_ids, k)


if __name__ == "__main__":
    selected = select_ids(["r1", "r2", "r3", "r4"], 2, 17)
    print(selected)
```

The tested CPython 3.13.14 demonstration prints `['r4', 'r2']`. Replay is checked within that runtime and call order; do not treat the exact sequence as a cross-version promise. Boundary checks cover zero/full samples, bad size/type/seed, duplicate IDs, mutation and global-state isolation. This is reproducible test-data selection, not a secrets generator.

## Hands-on labs

These ten broader activities are proposed learner work. The review executed the specific code and boundary checks described above; it did not complete every activity in every environment.

1. **Import matrix:** build nested modules and record the bindings and `__name__` produced by each import form and direct execution.
2. **Library boundary lab:** compare `ceil`, `floor`, and `trunc` for negatives; sample with/without seeding; record which `platform` values vary by environment.
3. **Exception control-flow tracer:** exercise success, handled child, handled parent, propagated error, re-raise, `else`, and `finally`; log the exact order.
4. **Custom hierarchy:** design a three-level domain exception family and prove that narrow and broad callers can choose appropriate recovery.
5. **Unicode lab:** round-trip text through UTF-8 bytes, inspect `ord`/`chr`, and compare `index` with `find` on missing values.
6. **String contract table:** test every listed string method with normal, empty, absent, whitespace, and non-ASCII inputs.
7. **Object-state lab:** compare class and instance variables, dictionaries, mangled names, `hasattr`, equality, and identity.
8. **Inheritance lab:** implement single and diamond hierarchies; inspect bases/MRO, override `__str__`, and demonstrate polymorphism.
9. **Functional-tools lab:** express one transformation as loops, comprehension, `map`, and `filter`; build closures that demonstrate late and intentional early binding.
10. **I/O capstone:** process a text input into a binary output with a mutable buffer; handle only recoverable failures and verify cleanup.

Use only your own programs and disposable data. Do not seek, reproduce, or share recalled certification items.

## Original knowledge checks

1. What local names do `import x.y`, `from x import y`, and `from x.y import z` bind?
2. Why can editing `sys.path` make a program fragile?
3. How does `__name__` distinguish import from direct execution?
4. Why is a leading underscore not access control?
5. Contrast `floor(-2.3)` with `trunc(-2.3)`.
6. Why is a seeded `random` sequence inappropriate for secrets?
7. In what order are exception handlers considered?
8. When do `else` and `finally` run in a `try` statement?
9. Contrast bare `raise` and `raise exc` inside a handler.
10. Why must assertions not enforce untrusted-input validation?
11. What benefit does a domain exception base class provide?
12. Distinguish Unicode code points, UTF-8 bytes, and Python strings.
13. How do `find()` and `index()` differ when a substring is absent?
14. Why does `strip("ab")` not mean “remove the prefix `ab`”?
15. What does `sorted("cab")` return?
16. Where should per-instance mutable state be initialized?
17. What can class and instance `__dict__` prove—and not prove?
18. Why is name mangling not privacy?
19. Contrast `is`, `==`, `isinstance`, and exact-type comparison.
20. What problem does the MRO solve in a diamond hierarchy?
21. When is composition preferable to inheritance?
22. In what order do clauses of a nested list comprehension execute?
23. Why can loop-created closures all return the final loop value?
24. Contrast text and binary file modes.
25. Why is a context manager preferable to a manual `close()` at the end?
26. What operational risk follows from catching `OSError` and continuing blindly?
27. What must you verify about PCAP-31-03 before buying an exam now?

## Answers and reasoning

1. `import x.y` binds `x`; `from x import y` binds `y`; `from x.y import z` binds `z`. Aliases replace the local binding name, not the referenced object.
2. Search order can depend on invocation and environment; a local same-named file may shadow a library. Prefer a coherent project/package entry point over ad hoc path edits.
3. An ordinary import uses the qualified module name. A script or module launched as the top-level program receives `__main__`; `python -m` also establishes useful package context.
4. A leading underscore is a convention. Without `__all__` it also affects star exports, but explicit access remains possible.
5. `floor(-2.3)` gives `-3`; `trunc(-2.3)` gives `-2`. Floor moves toward negative infinity, while truncation removes the fractional part toward zero.
6. Its deterministic state is for simulation/testing, not adversarial unpredictability. Repeating a seed also needs matching calls and compatible algorithms to replay a sample.
7. Top to bottom, first matching class or tuple. A parent catches descendants, so an early parent handler hides later child handlers.
8. `else` needs normal fall-through: no exception, return, break or continue. `finally` runs on ordinary exit/propagation paths, but a return/raise there can replace an earlier outcome.
9. Bare `raise` re-raises the active exception; `raise exc` adds the named raise site to its traceback. Preserve context and do not claim that naming it creates a new exception object.
10. Optimization can remove `assert`. Required validation needs explicit conditions and stable exceptions; assertions are for internal checks.
11. It provides a deliberate catch boundary: recover from one subtype or the domain family without swallowing unrelated programming and system errors.
12. A code point is a Unicode number; UTF-8 encodes text as bytes; `str` stores text. A visible character can involve multiple code points and multiple encoded bytes.
13. `find()` returns `-1`, while `index()` raises `ValueError`. Never use the truthiness of the returned index: zero is a valid match and negative one is truthy.
14. It repeatedly strips any `a` or `b` from either end until another character stops that side. It does not remove one exact prefix.
15. A new list, `['a', 'b', 'c']`; the original string stays unchanged. Strings have no `.sort()` method.
16. Create the mutable value on each instance, usually in `__init__`. A class list is shared; copying an outer container may still share nested mutable elements.
17. They show entries held in those mappings. Inheritance, descriptors and custom lookup may supply other attributes, and some instances lack `__dict__`. `hasattr` executes lookup.
18. Mangling avoids accidental name collisions across classes; callers can still use the transformed name. It does not protect secrets or enforce authorization.
19. `is` tests identity; `==` asks for equality; `isinstance` includes subclasses; `type(obj) is C` checks the exact type. Do not infer identity from equal immutable values.
20. The MRO establishes a consistent lookup sequence through shared ancestors. Cooperative `super()` follows that sequence and can call a sibling before the common base.
21. Prefer composition when the model is has-a or behavior should vary independently. Inheritance is appropriate when the child preserves the parent’s usable contract.
22. Read `for` and filter clauses in written order, with the leftmost loop outermost. Evaluate the output expression only after that combination passes its filters.
23. Closures retain bindings, so later calls see the final loop value. A factory or default argument binds separately; a default retains a reference, not an automatic deep copy.
24. Text streams exchange `str` with encoding/newline handling. Binary streams exchange bytes; do not pass an encoding to binary `open()`.
25. It closes the file on normal exit, an exception or early return. Close may itself report a write failure, and successful cleanup does not establish crash durability.
26. It can hide missing data, permissions errors or partial output and falsely report success. Catch only an expected condition you can actually recover from; otherwise propagate.
27. Confirm the purchasable code, syllabus and channel terms. The English page still marks 31-03 active and 31-04 in development; localized validity and generic retake wording conflict. An announced quarter alone proves no launch.

## Readiness checklist

- [ ] I can build and invoke a nested package without relying on accidental working-directory behavior.
- [ ] I can predict every named `math`, `random`, and `platform` operation and explain its boundary conditions.
- [ ] I can order handlers, use `else`/`finally`, re-raise, and design a small custom hierarchy.
- [ ] I can distinguish text, code points, encodings, and bytes and trace all listed string methods.
- [ ] I can explain class versus instance state, constructors, introspection, mangling, inheritance, overriding, identity, and polymorphism.
- [ ] I can rewrite comprehensions, lambdas, `map`/`filter`, and closures into equivalent explicit code.
- [ ] I can select text/binary modes, process streams safely, and handle expected I/O errors without masking failure.
- [ ] I have completed the labs using original code and can explain the output without running it first.
- [ ] I rechecked the official page for the PCAP-31-03 to PCAP-31-04 transition.

## Source and freshness notes

- The [official syllabus](https://pythoninstitute.org/pcap-exam-syllabus) controls section names, item counts, weights, scope, and its March 7, 2022 baseline.
- The [credential page](https://pythoninstitute.org/pcap) controls current version, delivery, price, languages, validity, prerequisite, retake policy, aligned course, and the PCAP-31-04 announcement.
- The [current Python documentation index](https://docs.python.org/3/) and selected pinned 3.13 pages were read; their individual reading boundaries are in the deep-review evidence. The exam remains tied to its published outline, so newly added features do not become objectives automatically.
- Twelve public Python blocks and the multi-file package were verified against their executed source. The core workbook passed 78 checks, with additional real package/file/language tests. Ten broader learner activities remain proposed; paid lesson interiors, authenticated UI and human review remain pending.
- This guide paraphrases public objectives and contains original scenarios, labs, questions, and answers. It contains no recalled/live items or copied paid-course questions.

## Places to learn

This is not a complete list and is not meant to be consumed in full. Choose one coherent primary course, build multi-module programs for every section, and use an explanation-led assessment only to locate gaps. Reconcile every resource against the official syllabus, especially during the PCAP-31-04 transition.

| Resource | Access | Estimated time |
|---|---|---:|
| [PCAP-31-03 syllabus](https://pythoninstitute.org/pcap-exam-syllabus) | Free official blueprint | 2–3 hours to map and recheck |
| [Python Essentials 2](https://edube.org/study/pe2) | Free official aligned course; public four-module listing read; account for study | Provider lists 58 hours, suggested 7/week |
| [Cisco Python Essentials 2](https://www.netacad.com/courses/python-essentials-2) | Official partner link; direct response was a shell, curriculum not inspected | Author budget 40–60 hours; runtime unverified |
| [Official PCAP practice-test compendium](https://ums.edube.org/products/1-pi-pcap-3103-pt) | Paid official practice; public product details only, no questions inspected | Author budget 5–8 hours including remediation |
| [Python tutorial](https://docs.python.org/3/tutorial/) and [library reference](https://docs.python.org/3/library/) | Free primary documentation; use the pinned topic links above | Author budget 12–20 selected hours plus coding |
| [Python 3 Object-Oriented Programming, 4th ed.](https://www.oreilly.com/library/view/python-3-object-oriented/9781804611864/) | O'Reilly subscription/book; request blocked, current contents/edition not verified | Author budget 15–25 selected hours |
| [Pluralsight: Python 3 path](https://www.pluralsight.com/paths/python-3) | Subscription; public 16-course/21-lab path, broad rather than PCAP aligned | Provider total 53 hours; author suggests 12–20 selected hours |
| [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/) | Free ten-week OpenCourseWare; account for submission/feedback; public landing reviewed | Author budget 20–35 selected hours |

OpenEDG’s course listing also covers PIP, generators and additional libraries; those do not override the 21 numbered exam objectives. Its retained 31-02/31-03 alignment merits checking during the transition. The practice landing lists USD 49, a 12-month redemption period and five launches per test, with no official exam attempt included (**VERIFY CURRENT**). Its Test Candidate redemption wording conflicts with the credential page’s Learner instructions; current account navigation was not verified. No enrollment, voucher, checkout, paid questions or external message was used in this review.

No exact current PCAP-31-03 course or practice exam from MeasureUp or Whizlabs was independently verified. Marketplace courses can lag an exam transition; verify their exact code, syllabus coverage, runtime, and update date before purchase.
