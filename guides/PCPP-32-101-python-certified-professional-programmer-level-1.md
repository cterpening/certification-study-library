---
exam_code: PCPP-32-101
vendor_id: python-institute
official_blueprint: https://pythoninstitute.org/pcpp1-exam-syllabus
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-29
---

# PCPP-32-101 Certified Professional Python Programmer Level 1 Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage and exam status were checked September 29, 2026. Validate important details against the [official PCPP1 syllabus](https://pythoninstitute.org/pcpp1-exam-syllabus).

**Current baseline:** PCPP-32-101, active; syllabus last updated March 11, 2022<br>
**Upcoming blueprint change:** PCPP-32-102 remains in development with no announced release date; its page describes five-year validity, distinct from the active 101 lifetime credential<br>
**Official delivery snapshot:** 45 questions; 65 minutes plus 10-minute NDA/tutorial; 70%; Python 3.x; single- and multiple-select; Pearson VUE/OnVUE, with limited TestNow availability<br>
**Credential snapshot:** no formal prerequisite; PCAP recommended; PCPP-32-101 credential validity is lifetime; exam from USD 325 when checked; 15-day retake wait; no official PCPP1 practice test currently listed<br>

The exam page lists single- and multiple-select questions, while the live syllabus introduction also mentions coding, scenario and interactive items. Treat that difference as unresolved delivery wording. The syllabus allows variable points per item and reports a normalized score; **70% does not establish a fixed number of correct answers out of 45**. A search-visible table from the dated official PDF lists section raw maxima totaling 120, but the full PDF could not be opened in this review. Confirm the purchased version and appointment instructions rather than inferring a current scoring formula.

The Pearson policy page also contains both “any time before” and 24-hour rescheduling wording. Verify the terms attached to the actual appointment. No booking, voucher redemption, account or OnVUE system test was performed.

## How to use this guide

This is a build-and-debug credential. Create one medium-size application that uses a domain model, Tkinter UI, REST client, SQLite store, CSV/XML exchange, logging, and configuration. Add one concern at a time and explain how failures propagate across boundaries.

> **About related items:** A `Related item:` callout supplies adjacent professional context. It helps explain the objective but is not a claim that the item is independently tested.

## Weighted objective map

| Section | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| Advanced OOP | 15 | 35% | Design, extend, inspect, copy, serialize, and troubleshoot a nontrivial object model |
| Conventions and standardization | 7 | 12% | Review code against the named PEPs and produce useful documentation/type hints |
| GUI programming | 8 | 20% | Build a responsive Tkinter form with layout, validation, events, and dialogs |
| Network programming | 8 | 18% | Explain sockets/HTTP and build a defensive JSON REST client |
| Files and environment | 7 | 15% | Use SQLite, XML, CSV, logging, and configuration with correct lifecycle handling |

## 1. Advanced object-oriented programming — 35%

### Model behavior and relationships

Start from contracts: what state is valid, what operations preserve it, and what failures callers may handle. Use inheritance for a substitutable **is-a** relation and composition for **has-a** collaboration. Python's MRO determines lookup under multiple inheritance; cooperative methods use `super()` consistently.

Special methods connect classes to core syntax: `__eq__` to equality, numeric methods to operators, `__int__` to conversion, `__str__` to human-readable text, `__getattr__` to missing-attribute fallback, and `__getitem__` to subscription. Return `NotImplemented` from binary comparison where the other operand is unsupported; do not return a convenient false value that prevents reflected/cooperative comparison.

Duck typing depends on supported behavior rather than declared ancestry. `isinstance()` and `issubclass()` remain useful when a type boundary genuinely matters.

### Subclass built-in classes without breaking their contracts

A built-in class can be extended directly when the new type remains substitutable for the original. Initialize the base with `super()`, retain the expected return values and exception behavior, and add behavior that does not make ordinary built-in operations surprising:

The complete `TaggedList` in `objects.py` below adds a label while retaining list mutation behavior. Its checks cover construction, `append`, `extend`, slice assignment, `+=`, iteration and copying. In this runtime, `tagged.copy()` returns a base `list`; `copy.copy(tagged)` preserves the subclass and its label. A new outer list still shares its element references.

Do not assume every built-in operation will route through one method you override. For example, guarding only `append()` does not necessarily enforce an invariant across construction, `extend()`, slice assignment, `+=`, or other mutation paths. If the type needs strict validation or substantially different semantics, composition or a purpose-built wrapper such as `collections.UserList`, `UserDict`, or `UserString` is often easier to reason about. Test construction, copying, comparison, iteration, mutation, and inherited methods—not merely the new method.

> **Related item:** Inheriting storage is not the same as inheriting a safe domain contract. A wrapper exposes only the operations the domain intends, while a direct built-in subclass inherits a broad API that must remain coherent.

### Decorators, callable objects, and method types

`*args` collects extra positional arguments and `**kwargs` extra keyword arguments; the same syntax unpacks during a call. Preserve wrapper metadata with `functools.wraps` in real code. A decorator factory receives configuration and returns the actual decorator. Decorator expressions are evaluated top-to-bottom; the resulting decorators are applied bottom-up. Calls then enter the outer wrapper first and unwind in reverse order. The workbook records all three phases, forwards arguments, and checks `__name__`, `__doc__`, annotations and `__wrapped__`. A closure retains access to its enclosing bindings; it does not freeze every value by copying it.

An instance method receives `self`; `@classmethod` receives `cls` and can access class state or implement an inheritance-aware alternate constructor; `@staticmethod` receives neither automatically and simply namespaces a related function. `__call__` makes instances callable.

Abstract base classes define required operations through `abc.ABC` and `@abstractmethod`. They prevent ordinary instantiation until concrete subclasses implement the contract. Properties use getter/setter/deleter methods behind attribute syntax; validation belongs at the boundary where state changes. An abstract method can contain an implementation reached with `super()`. Registering a virtual subclass changes `isinstance`/`issubclass` recognition but supplies no method implementation or MRO entry, and does not enforce the abstract methods on that unrelated class.

The workbook's mutable `Value` deliberately rejects booleans and accepts only bounded integers. A failed setter preserves the old value; deleting the property resets it to zero by this class's documented choice. Its equality returns `NotImplemented` for other exact types, and defining equality without a compatible hash makes instances unhashable. It implements `<` for the exercise, not a complete total-order API. Single-leading-underscore attributes are a convention, not an access-control barrier.

> **Related item:** A protocol can express structural typing without forcing inheritance. Protocols are useful modern context but are not named in this 2022 blueprint.

### Exceptions, copying, persistence, and metaclasses

Exception objects expose `__traceback__`; implicit handling context appears in `__context__`, while `raise NewError(...) from cause` establishes `__cause__`. Explicit chaining explains abstraction boundaries without discarding the original failure. `raise ... from None` suppresses implicit context in the displayed traceback; it does not erase `__context__`. Inspect causes and tracebacks when debugging, but do not catch every error merely to make an operation appear successful.

Assignment aliases an object. `copy.copy()` duplicates only the outer object; nested mutable values remain shared. `copy.deepcopy()` recursively copies while tracking already visited objects, but external resources and identity-sensitive objects may require custom policy. Memoization both handles cycles and preserves repeated references inside the copied graph; two references to one child normally remain two references to one copied child.

`pickle` serializes Python object graphs to bytes, and `shelve` stores pickled values behind string keys. Never unpickle untrusted data: deserialization can execute attacker-controlled behavior. Persistence compatibility across code changes is also not guaranteed. Ordinary functions and classes are identified by importable qualified names; their implementation is not embedded as source. Default instance reconstruction generally bypasses `__init__`. An explicit protocol describes a format choice, not a promise that every Python version or changed class definition can restore the data.

With `shelve(writeback=False)`, mutating a retrieved list does not write it back: retrieve, edit and assign it to the key. `writeback=True` caches accessed values and writes them on synchronization/close, with memory and shutdown costs. Use a context manager, inspect the selected `dbm` backend, and do not assume one portable file or safe concurrent writers. The workbook uses only data generated during its own run and removes the temporary shelf afterward.

Classes are instances of a metaclass, normally `type`. A metaclass can control class creation, but ordinary class decorators or `__init_subclass__` are often clearer. Know `__class__`, `__bases__`, `__dict__`, and the one-argument versus three-argument roles of `type()`. The metaclass prepares the namespace, the class body populates it, and construction produces the class object before class decorators run. A class dictionary is exposed through a mapping proxy; it is not an ordinary writable instance dictionary. Cooperative `super()` follows the MRO of the actual instance, which can send a call through a sibling in a diamond.

## 2. Conventions, best practices, and standardization — 12%

PEP 1 explains the proposal process and PEP types; PEP 8 covers style; PEP 20 summarizes design aphorisms; PEP 257 specifies docstring conventions; PEP 484 defines type-hint semantics. Style tools can detect inconsistency, but a clean checker result does not prove correctness.

Use imports in conventional groups, four-space indentation, readable continuation, consistent naming, and whitespace that reveals structure. Comments explain why or risk; docstrings document the public contract. A one-line docstring is a concise summary; multi-line docstrings add detail after a blank line. Type hints support tools and readers and are not automatically runtime enforcement.

PEP 1 distinguishes Standards Track, Informational and Process proposals; a PEP is not automatically an accepted language requirement. PEP 20 offers design judgments to weigh together, not nineteen mechanical pass/fail rules. PEP 8 recommends 79-character code and 72-character flowing comments/docstrings, with project-specific agreements and compatibility taking precedence. Public functions need a useful contract; a docstring becomes `__doc__`, while an ordinary comment does not.

PEP 484 is historical type-hint context, not the complete current typing specification. An annotated function can still receive a different runtime type unless its code validates it. A formatter rewrites layout, a linter checks configured rules, a type checker analyzes declared relationships, and a documentation tool renders supplied contracts. None proves requirements or runtime behavior. The workbook was checked with the already installed Ruff 0.16.4 using `E4,E7,E9,F,W,E501` and a 79-character limit; this selected rule set is not a complete PEP 8/257 audit or a static typing proof. Exact-type checks are intentional where the small wire/domain contract excludes booleans or subclasses.

> **Related item:** Automated formatting and linting work best as repository policy with pinned configuration; otherwise contributors can produce conflicting “clean” results.

## 3. GUI programming — 20%

Event-driven programs register callbacks and enter a main loop. `Tk()` creates the root window; `mainloop()` processes events. Widgets such as `Frame`, `Label`, `Entry`, `Button`, `Radiobutton`, and `Canvas` have configuration and geometry.

Use `grid` for rows/columns, `pack` for edge/sequence layout, and `place` for explicit coordinates. **Do not mix `pack` and `grid` for children of the same container.** Different nested containers can use different managers. `place` can coexist with `grid` on distinct widgets in a container; explicit placement can overlap other children, so that permission is not a layout-quality guarantee. Observable Tk variables connect widget state to callbacks. `bind()` associates an event pattern with a handler, while a button's `command` accepts a no-argument callable.

Validate input in the callback boundary, display actionable dialogs, and leave the UI in a consistent state after failure. `destroy()` ends a window. Long blocking work freezes the event loop. `after(ms, callback)` schedules work; it does not make a blocking callback asynchronous. Calling `after(ms)` without a callback blocks without processing events. The workbook sends source I/O to one worker, passes results through a queue and polls with `after`; only the Tk thread touches widgets and the bounded SQLite snapshot. It cancels callbacks, removes variable observers, joins its bounded worker and destroys the root.

Keep references to `StringVar`/`IntVar` wrappers while widgets use them. A variable trace receives the name, index and access mode, unlike a no-argument button command or a one-argument bound-event handler. `Radiobutton` choices share a variable with distinct values. `Canvas` creates graphical items identified by IDs/tags; widget options and item options are different layers. Validate the application's action even if entry validation is also configured. The executable desk captures dialog calls and keeps its root withdrawn, so it establishes callback behavior rather than manual visual or accessibility quality.

## 4. Network programming — 18%

A host/domain resolves to an address; a port identifies a service endpoint; a protocol defines communication rules. TCP is connection-oriented and stream-based; UDP is connectionless and datagram-based. A client initiates communication and a server listens/accepts.

Raw sockets require address family/type, connection, byte encoding, partial `send`/`recv` awareness, timeouts, and guaranteed close. `recv(n)` returns up to `n` bytes, not one complete application message. A zero-length result means peer EOF; an empty application message needs an explicit framing rule. The workbook uses a two-byte length, a 4096-byte cap and a loop that rejects truncated frames. Reads are deliberately capped at seven bytes to exercise assembly without assuming how TCP divides packets. `sendall()` completes the submitted bytes or raises; after an error, do not assume none were delivered. Socket timeouts are operation limits, not automatically a whole-protocol deadline. HTTP framing and TLS are reasons to prefer a mature HTTP client over hand-built HTTP sockets.

JSON represents objects, arrays, strings, numbers, booleans, and null; `json.dumps()` serializes a Python value to text and `json.loads()` parses text. XML is hierarchical and supports attributes; DTD concepts belong to the published scope. JSON parsing does not validate an application schema. Tuples become JSON arrays/lists, and non-string dictionary keys become strings. Python's default decoder retains the last repeated object name and accepts non-finite numeric extensions; strict applications need explicit policies such as `allow_nan=False` when encoding and suitable decoding hooks. Repeated `dump()` calls do not frame multiple documents.

A DTD declares an XML grammar, such as permitted elements and attributes, through internal/external subsets. Well-formed nesting is distinct from DTD validity. A small original ElementTree probe parses a document whose child violates an `EMPTY` declaration; successful tree construction does not prove DTD validation. The workbook's XML is trusted, created locally, and checked against a narrow application schema. Size checks alone do not establish a safe general untrusted-XML parser; consult the primary XML processing guidance and deployed parser version.

With `requests`, set a timeout, select `GET`/`POST`/`PUT`/`DELETE` from the intended operation, inspect status and headers, then parse only the expected body. CRUD and HTTP often align conceptually, but an API's documented contract determines semantics. The fixture uses GET for a list, POST for creation, PUT for replacement and DELETE with 204/no JSON body. `raise_for_status()` detects HTTP error status; it does not reject every unexpected success or redirect, and valid JSON can still describe an error. Check those separately.

Requests has no default timeout. A `(connect, read)` tuple distinguishes connection attempts from waiting for response bytes; neither is an overall wall-clock budget. Multiple address attempts or repeated slow progress can extend total time. Close streamed responses and owned sessions on every path. The workbook rejects redirects, checks JSON media type, caps decoded bytes while streaming, validates exact record fields and chains a `SourceError` to its cause. It disables inherited environment proxy/auth settings for its disposable loopback fixture. TLS, production authentication, retries, adversarial parser complexity and distributed failure recovery are outside this finite exercise.

> **Related item:** Retrying a non-idempotent request can duplicate side effects. Production retry policy must consider method semantics, idempotency keys, backoff, and failure class.

## 5. File processing and environment — 15%

### SQLite and transactions

`sqlite3.connect()` opens a database connection; cursors `execute`/`executemany` statements and `fetchone`/`fetchall` results. Parameterize values with placeholders; never concatenate untrusted SQL. `commit()` makes a transaction durable and `rollback()` abandons it. Always define who owns the connection and when it closes. In Python 3.12+, the `autocommit` option makes the transaction policy explicit. The workbook requires Python 3.12+ and sets `autocommit=False`: a transaction remains open, and commit/rollback starts a new one. Python 3.13's default is `LEGACY_TRANSACTION_CONTROL`, which has different implicit-DML behavior; `autocommit=True` makes connection `commit()`/`rollback()` no-ops. Do not silently transfer behavior between these modes.

`with connection:` commits on a successful exit and rolls back on failure, but **does not close the connection**. Use `close()` or `contextlib.closing` separately. A failed `executemany` batch can have earlier pending writes; let the error leave the transaction context so all of that unit rolls back. `fetchone()` returns `None` at exhaustion and `fetchall()` an empty list. `execute()` accepts one statement; legacy `executescript()` can commit pending work before the script, so it is not a drop-in transactional replacement.

Placeholders bind values, not table names or SQL keywords. Keep identifiers fixed or select them from an explicit allowlist. The workbook proves that a SQL-looking name remains data, a duplicate-key failure rolls back a prior delete and insert, and an uncommitted delete disappears when the connection closes.

Know `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, and `DELETE`, including the danger of modifying/deleting without the intended `WHERE` condition.

### XML, CSV, logs, and configuration

ElementTree `find`/`findall` searches a parsed tree; `Element` and `SubElement` build one. CSV requires the `csv` module because quoting, delimiters, and embedded newlines defeat naïve splitting. `DictReader`/`DictWriter` map rows by field name. Open text CSV files with `newline=''` and a known encoding. Validate headers and row widths: extra fields are collected under the rest key (normally `None`), and missing fields receive the rest value. Strings do not automatically become integers. Writer conversion of `None` to an empty string is not reversible without a separate schema.

ElementTree `find()` returns `None` if no match exists; test `is None`, not element truthiness, which can depend on child count and is deprecated. A default namespace expands tag names to `{uri}local`, so an unqualified lookup may miss the element. Match qualified names or provide a namespace map. Build XML with `Element`/`SubElement` and let serialization escape text/attributes; compare parsed meaning rather than attribute order or byte formatting.

Logging levels communicate severity: DEBUG, INFO, WARNING, ERROR, CRITICAL. A `LogRecord` carries event metadata; a formatter renders it; a handler sends it to a destination. Libraries should generally obtain a named logger and avoid configuring the entire application implicitly. Both the originating logger threshold and handler threshold affect emission; propagated records go directly to ancestor handlers, without reapplying ancestor logger levels. Attaching handlers at multiple levels can duplicate output. Formatter `style="{"` changes the layout template, not the `%` argument interpolation of `logger.info("row %s", value)`. Remove and close handlers you own after use.

`ConfigParser` reads INI-style sections and values; interpolation substitutes referenced values. Values are stored as strings: use `getint`, `getfloat` and `getboolean`, since `bool("no")` is true. DEFAULT values outrank an explicit fallback. Option names are case-insensitive by default; section names retain case. Basic interpolation uses `%(option)s`; extended interpolation can use `${section:option}`. Missing substitutions raise errors on access. `read()` silently skips files that cannot be opened and returns those read; use an explicit open plus `read_file()` for a required file. Configuration is data, and its converted values still need domain validation.

## Integrated build and labs

The original workbook below executes a bounded service-status desk with a current snapshot. The following fuller build and twelve learner labs remain proposed; this review does not mark your personal completion, production readiness, automatic retries, historical retention or manual GUI review as done.

Extend it into a small **service-status desk**:

1. abstract `StatusSource` and concrete REST/file sources;
2. decorated retry/timing callbacks with explicit error chaining;
3. Tkinter form to refresh, filter, and show details;
4. `requests` JSON client with timeout and status validation;
5. SQLite history with parameterized queries and transactions;
6. CSV export, XML import, structured logging, and INI configuration.

Then complete these focused labs:

1. Implement and test six special methods on a value object; then subclass one built-in collection, preserve its ordinary contract, and compare the design with composition or a `collections` wrapper.
2. Compare MRO behavior with inheritance against an equivalent composition design.
3. Stack decorators and prove definition/application/call order.
4. Demonstrate instance, class, static, abstract, and property methods.
5. Draw alias/shallow/deep object graphs before running the copy code.
6. Round-trip a trusted object through pickle, then document why the boundary must be trusted.
7. Run a style/docstring/type-hint review against the named PEPs.
8. Build a Tkinter form with grid, validation, bound event, dialog, and clean close.
9. Exchange one message over a loopback socket with timeout and guaranteed cleanup.
10. Exercise all four HTTP methods against a disposable local/test API.
11. Prove transaction commit and rollback paths in SQLite.
12. Round-trip quoted CSV and structured XML; route log levels to a custom formatter.

## Original executable workbook

Save the five files below in one dedicated writable folder. They use the existing CPython 3.13.14 runtime, Requests 2.34.2, SQLite 3.50.4 and Tcl/Tk 8.6.15 from this review; the SQLite transaction example requires Python 3.12+. The exam names Python 3.x, not these particular patch versions. The selected 3.13 documentation currently identifies 3.13.15, while the generic index is 3.14.7; these are distinct from the executed runtime. No package or interpreter was installed.

Run `python objects.py`, `python network.py`, `python storage.py` and `python desk.py`, then repeat each with `python -O`. The four programs report **71, 34, 37 and 31 checks** respectively: **173 per mode**, not 173 separate learner labs. `checks.py` keeps checks active under optimization. The selected Ruff check also passed; source hashes and exact command/output receipts are in the linked review record.

The scripts create only original temporary files beside themselves and ephemeral loopback sockets, close all owned resources and remove temporary directories. `desk.py` keeps Tk withdrawn and captures dialog calls. Its current-snapshot demonstration integrates abstract REST/file sources, decorated tracing, configuration, a worker/queue, Tk controls and Canvas, SQLite, CSV/XML and logging. It does not implement the full proposed history/retry application. The finite JSON byte cap and trusted XML fixtures are not a general hostile-input security assessment. Tests cover selected success/failure paths on this Windows runtime, not other OSes, every API, cancellation of arbitrary unbounded work or manual visual accessibility.

### checks.py

```python
"""Keep workbook checks active even when Python runs with -O."""


class Checks:
    """Count checks and stop immediately on an unexpected result."""

    def __init__(self):
        """Start with no completed checks."""
        self.count = 0

    def equal(self, actual, expected):
        """Require equality and show both values on failure."""
        self.count += 1
        if actual != expected:
            raise AssertionError((actual, expected))

    def true(self, condition):
        """Require a true condition without using an assert statement."""
        self.equal(bool(condition), True)

    def raises(self, kind, operation, *args, **kwargs):
        """Return the expected exception; propagate unrelated failures."""
        self.count += 1
        try:
            operation(*args, **kwargs)
        except kind as error:
            return error
        raise AssertionError(f"Expected {kind.__name__}")
```

### objects.py

```python
"""Exercise bounded OOP, copying and trusted persistence contracts.

Run this module directly. All persisted input is created within this run;
no external pickle or shelf is accepted. Temporary files are removed.
"""

from abc import ABC, abstractmethod
import copy
import dbm
from functools import wraps
from pathlib import Path
import pickle
import shelve
import tempfile

from checks import Checks


class Value:
    """Represent a mutable integer count in the range -1000 through 1000."""

    created = 0

    def __init__(self, number):
        """Validate the count and record construction on the concrete class."""
        self.number = number
        type(self).created += 1

    @property
    def number(self):
        """Return the current count."""
        return self._number

    @number.setter
    def number(self, number):
        if type(number) is not int or not -1000 <= number <= 1000:
            raise ValueError("a bounded integer is required")
        self._number = number

    @number.deleter
    def number(self):
        # Clearing this property deliberately resets the domain value.
        self._number = 0

    @classmethod
    def from_text(cls, text):
        """Create an instance of the receiving class from decimal text."""
        return cls(int(text))

    @staticmethod
    def unit():
        """Return the shared presentation unit without an implicit receiver."""
        return "units"

    def __eq__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return self.number == other.number

    def __lt__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return self.number < other.number

    def __abs__(self):
        return type(self)(abs(self.number))

    def __int__(self):
        return self.number

    def __str__(self):
        return f"{self.number} {self.unit()}"

    def __repr__(self):
        return f"{type(self).__name__}({self.number})"

    def __getitem__(self, key):
        return {"number": self.number, "unit": self.unit()}[key]

    def __getattr__(self, name):
        if name == "magnitude":
            return abs(self.number)
        raise AttributeError(name)


class TaggedList(list):
    """Add a label without imposing a new invariant on list mutations."""

    def __init__(self, values=(), *, tag=""):
        """Copy the input elements into this list and retain its label."""
        super().__init__(values)
        self.tag = tag


class Root:
    """End a cooperative method chain."""

    def steps(self):
        """Return the terminal step."""
        return ["root"]


class Left(Root):
    """Add a step before the next implementation in the MRO."""

    def steps(self):
        """Continue through a possible sibling, not a hard-coded parent."""
        return ["left"] + super().steps()


class Right(Root):
    """Add a second cooperative step."""

    def steps(self):
        """Continue the same method contract."""
        return ["right"] + super().steps()


class Diamond(Left, Right):
    """Combine both steps using C3 lookup."""


class Runner:
    """Compose any collaborator that provides steps()."""

    def __init__(self, provider):
        """Keep the collaborator without requiring a particular ancestry."""
        self.provider = provider

    def run(self):
        """Delegate to the collaborator's behavioral contract."""
        return self.provider.steps()


class Source(ABC):
    """Require a read operation from normal concrete subclasses."""

    @abstractmethod
    def read(self):
        """Return a sequence; an abstract method may have an implementation."""
        return []


class LocalSource(Source):
    """Provide a concrete source with one locally defined record."""

    def read(self):
        """Extend the abstract base implementation through super()."""
        return super().read() + [7]


def trace(name, events):
    """Build a decorator that records evaluation, application and calls."""
    events.append("factory:" + name)

    def decorate(function):
        events.append("apply:" + name)

        @wraps(function)
        def wrapper(*args, **kwargs):
            events.append("enter:" + name)
            try:
                return function(*args, **kwargs)
            finally:
                events.append("leave:" + name)

        return wrapper

    return decorate


class Multiplier:
    """Make a configured instance callable."""

    def __init__(self, factor):
        """Keep the multiplication factor."""
        self.factor = factor

    def __call__(self, value):
        return self.factor * value


def translate_error(suppress=False):
    """Translate a local parse error, optionally suppressing its display."""
    try:
        int("bad")
    except ValueError as error:
        if suppress:
            raise RuntimeError("invalid measurement") from None
        raise RuntimeError("invalid measurement") from error


def run():
    """Check the documented behaviors and report the shelf backend used."""
    check = Checks()
    value = Value(-3)
    check.equal(int(value), -3)
    check.equal(abs(value), Value(3))
    check.equal(str(value), "-3 units")
    check.equal(repr(value), "Value(-3)")
    check.equal(value["number"], -3)
    check.equal(value.magnitude, 3)
    check.raises(KeyError, value.__getitem__, "absent")
    check.raises(AttributeError, getattr, value, "absent")
    check.true(value.__eq__(3) is NotImplemented)
    check.true(value != 3)
    check.true(value < Value(2))
    check.raises(TypeError, hash, value)  # Mutable equality implies no hash.
    check.raises(ValueError, setattr, value, "number", True)
    check.raises(ValueError, setattr, value, "number", 1001)
    check.equal(value.number, -3)
    value.number = 8
    check.equal(value.number, 8)
    del value.number
    check.equal(value.number, 0)

    class ChildValue(Value):
        """Inherit the alternate constructor."""

    child = ChildValue.from_text("12")
    check.true(type(child) is ChildValue and isinstance(child, Value))
    check.true(issubclass(ChildValue, Value))
    check.equal(child.unit(), Value.unit())
    check.true("created" in ChildValue.__dict__)

    tagged = TaggedList([1], tag="sample")
    check.true(tagged.append(2) is None)
    tagged.extend([3])
    tagged[1:2] = [8, 9]
    tagged += [4]
    check.equal(list(tagged), [1, 8, 9, 3, 4])
    check.equal(tagged.tag, "sample")
    check.true(type(tagged.copy()) is list)
    check.true(type(copy.copy(tagged)) is TaggedList)
    check.equal(copy.copy(tagged).tag, "sample")
    check.equal(Diamond().steps(), ["left", "right", "root"])
    check.equal(
        [cls.__name__ for cls in Diamond.__mro__],
        ["Diamond", "Left", "Right", "Root", "object"],
    )
    check.equal(Runner(Diamond()).run(), ["left", "right", "root"])
    check.raises(TypeError, Source)
    check.equal(LocalSource().read(), [7])

    class Unrelated:
        """Have no read method even after virtual registration."""

    Source.register(Unrelated)
    virtual = Unrelated()
    check.true(isinstance(virtual, Source))
    check.true(Source not in Unrelated.__mro__)
    check.true(not hasattr(virtual, "read"))

    events = []

    @trace("outer", events)
    @trace("inner", events)
    def combine(*values: int, bonus: int = 0) -> int:
        """Return the sum of the supplied values and bonus."""
        return sum(values) + bonus

    check.equal(events, [
        "factory:outer", "factory:inner", "apply:inner", "apply:outer",
    ])
    check.equal(combine(*[2, 3], **{"bonus": 4}), 9)
    check.equal(events[4:], [
        "enter:outer", "enter:inner", "leave:inner", "leave:outer",
    ])
    check.equal(combine.__name__, "combine")
    check.true(combine.__doc__.startswith("Return the sum"))
    check.equal(combine.__annotations__["return"], int)
    check.equal(combine.__wrapped__.__wrapped__(1, bonus=2), 3)
    check.equal(Multiplier(3)(4), 12)

    def unchecked(number: int) -> int:
        return number

    check.equal(unchecked("text"), "text")  # Hints do not enforce types.
    error = check.raises(RuntimeError, translate_error)
    check.true(isinstance(error.__cause__, ValueError))
    check.true(error.__context__ is error.__cause__)
    check.true(error.__traceback__ is not None)
    hidden = check.raises(RuntimeError, translate_error, True)
    check.true(hidden.__cause__ is None and hidden.__suppress_context__)
    check.true(isinstance(hidden.__context__, ValueError))

    creation = []

    class Meta(type):
        """Record namespace preparation and class construction."""

        @classmethod
        def __prepare__(mcls, name, bases):
            creation.append("prepare:" + name)
            return {}

        def __new__(mcls, name, bases, namespace):
            creation.append("new:" + name)
            return super().__new__(mcls, name, bases, namespace)

    def mark(cls):
        creation.append("decorate:" + cls.__name__)
        cls.marked = True
        return cls

    @mark
    class Built(metaclass=Meta):
        """Demonstrate metaclass work before class decorator application."""

        answer = 7

    check.equal(creation, ["prepare:Built", "new:Built", "decorate:Built"])
    check.true(type(Built) is Meta and Built.marked)
    check.equal(Built.__bases__, (object,))
    check.equal(Built.__dict__["answer"], 7)
    dynamic = type("Dynamic", (), {"answer": 9})
    check.equal(dynamic().answer, 9)

    shared = [1]
    graph = [shared, shared]
    shallow = copy.copy(graph)
    deep = copy.deepcopy(graph)
    check.true(shallow is not graph and shallow[0] is shared)
    check.true(deep[0] is deep[1] and deep[0] is not shared)
    shared.append(2)
    check.equal(shallow, [[1, 2], [1, 2]])
    check.equal(deep, [[1], [1]])
    cycle = []
    cycle.append(cycle)
    copied_cycle = copy.deepcopy(cycle)
    check.true(copied_cycle is not cycle and copied_cycle[0] is copied_cycle)
    restored = pickle.loads(pickle.dumps(graph, protocol=4))
    check.true(restored == graph and restored[0] is restored[1])
    check.true(restored[0] is not shared)
    original = Value(23)
    before = Value.created
    restored_value = pickle.loads(pickle.dumps(original, protocol=4))
    check.equal(restored_value, original)
    check.true(restored_value is not original)
    check.equal(Value.created, before)  # Default unpickling bypasses __init__.

    workspace = Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory(
        prefix="pcpp-objects-", dir=workspace,
    ) as tmp:
        folder = Path(tmp).resolve()
        check.true(folder.parent == workspace)
        path = str(folder / "records")
        with shelve.open(path, protocol=4, writeback=False) as shelf:
            shelf["items"] = [1]
            shelf["items"].append(2)
            check.equal(shelf["items"], [1])
            edited = shelf["items"]
            edited.append(3)
            shelf["items"] = edited
        with shelve.open(path, protocol=4) as shelf:
            check.equal(shelf["items"], [1, 3])
        with shelve.open(path, protocol=4, writeback=True) as shelf:
            shelf["items"].append(4)
        with shelve.open(path, protocol=4) as shelf:
            check.equal(shelf["items"], [1, 3, 4])
        backend = dbm.whichdb(path)
    check.true(not folder.exists())
    print(f"objects: {check.count} checks; shelf backend={backend}")


if __name__ == "__main__":
    run()
```

### network.py

```python
"""Exercise bounded TCP framing and a disposable loopback JSON service.

Run directly. No external endpoint, credential, proxy or persistent service
is used. HTTP paths and records are original fixtures, not an API promise.
"""

from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import socket
from threading import Event, Thread

import requests

from checks import Checks


class SourceError(Exception):
    """Represent a transport, response or application-contract failure."""


def records(value):
    """Validate the complete small status-list contract before returning it."""
    if type(value) is not list or len(value) > 20:
        raise ValueError("expected at most 20 records")
    seen = set()
    for item in value:
        if type(item) is not dict or set(item) != {"id", "name", "status"}:
            raise ValueError("unexpected record fields")
        if type(item["id"]) is not int or item["id"] <= 0:
            raise ValueError("positive integer id required")
        if item["id"] in seen:
            raise ValueError("duplicate id")
        seen.add(item["id"])
        if type(item["name"]) is not str or not 1 <= len(item["name"]) <= 80:
            raise ValueError("bounded name required")
        if item["status"] not in ("up", "down"):
            raise ValueError("unknown status")
    return value


class StatusClient:
    """Own one Requests session for the supplied loopback fixture."""

    def __init__(self, base_url):
        """Keep the fixture URL and disable ambient proxy/auth inheritance."""
        if not base_url.startswith("http://127.0.0.1:"):
            raise ValueError("this workbook uses its loopback fixture only")
        self.base_url = base_url
        self.session = requests.Session()
        self.session.trust_env = False

    def close(self):
        """Release this client's pooled connections."""
        self.session.close()

    def request(self, method, path="/records", payload=None, timeout=(1, 1)):
        """Check status, media type, size, JSON and the record schema."""
        try:
            with self.session.request(
                method, self.base_url + path, json=payload, timeout=timeout,
                stream=True, allow_redirects=False,
            ) as response:
                response.raise_for_status()
                if response.status_code == 204 and method == "DELETE":
                    return None
                if response.status_code not in (200, 201):
                    raise ValueError("unexpected success/redirect status")
                media = response.headers.get("Content-Type", "")
                media = media.partition(";")[0].strip().lower()
                if media != "application/json":
                    raise ValueError("expected application/json")
                body = bytearray()
                for part in response.iter_content(chunk_size=512):
                    body.extend(part)
                    if len(body) > 4096:
                        raise ValueError("response exceeds 4096 decoded bytes")
                return records(json.loads(body))
        except (requests.RequestException, ValueError) as error:
            raise SourceError("status request failed") from error

    def read(self):
        """Return the fixture's current status records."""
        return self.request("GET")


@contextmanager
def fixture():
    """Serve original finite responses on an ephemeral loopback port."""
    state = {1: {"id": 1, "name": "mail", "status": "up"}}
    release = Event()

    class Handler(BaseHTTPRequestHandler):
        """Implement only the methods and paths used by this workbook."""

        def log_message(self, *args):
            pass

        def reply(self, status, body, media="application/json"):
            self.send_response(status)
            self.send_header("Content-Type", media)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if body:
                self.wfile.write(body)

        def do_GET(self):
            if self.path == "/slow":
                release.wait(2)
                return  # Client times out before any response headers.
            cases = {
                "/fail": (500, b'{"error":"fixture"}', "application/json"),
                "/html": (200, b"<p>not json</p>", "text/html"),
                "/badjson": (200, b"{", "application/json"),
                "/invalid": (200, b'{"items":[]}', "application/json"),
                "/large": (200, b" " * 4097, "application/json"),
                "/redirect": (302, b"", "application/json"),
            }
            if self.path in cases:
                self.reply(*cases[self.path])
            else:
                self.reply(200, json.dumps(list(state.values())).encode())

        def write_record(self, status):
            size = int(self.headers["Content-Length"])
            item = json.loads(self.rfile.read(size))
            records([item])
            state[item["id"]] = item
            self.reply(status, json.dumps([item]).encode())

        def do_POST(self):
            self.write_record(201)

        def do_PUT(self):
            self.write_record(200)

        def do_DELETE(self):
            state.pop(int(self.path.rsplit("/", 1)[-1]), None)
            self.reply(204, b"")

    server = HTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(
        target=server.serve_forever, kwargs={"poll_interval": 0.01},
    )
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}", release
    finally:
        release.set()
        server.shutdown()
        server.server_close()
        thread.join(3)
        if thread.is_alive():
            raise RuntimeError("fixture thread did not stop")


def receive_exact(connection, size):
    """Read the requested byte count, rejecting an early EOF."""
    result = bytearray()
    while len(result) < size:
        part = connection.recv(min(7, size - len(result)))
        if not part:
            raise EOFError("peer closed during frame")
        result.extend(part)
    return bytes(result)


def receive_frame(connection):
    """Read a two-byte big-endian length followed by bounded UTF-8 text."""
    size = int.from_bytes(receive_exact(connection, 2), "big")
    if size > 4096:
        raise ValueError("frame too large")
    return receive_exact(connection, size).decode("utf-8")


@contextmanager
def tcp_pair():
    """Create and close a real IPv4 loopback connection without a daemon."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.bind(("127.0.0.1", 0))
        listener.listen(1)
        listener.settimeout(1)
        with socket.create_connection(listener.getsockname(), timeout=1) as a:
            b, _ = listener.accept()
            with b:
                b.settimeout(1)
                yield a, b


def run():
    """Check success, framing, HTTP contract failures and cleanup paths."""
    check = Checks()
    message = "caf\u00e9 status is up".encode("utf-8")
    with tcp_pair() as (sender, receiver):
        wire = len(message).to_bytes(2, "big") + message
        sender.sendall(wire[:1])
        sender.sendall(wire[1:] + b"\0\0")
        check.equal(receive_frame(receiver), "caf\u00e9 status is up")
        check.equal(receive_frame(receiver), "")
        sender.shutdown(socket.SHUT_WR)
        check.raises(EOFError, receive_frame, receiver)
    check.equal(sender.fileno(), -1)
    check.equal(receiver.fileno(), -1)
    with tcp_pair() as (sender, receiver):
        sender.sendall(b"\0\5ab")
        sender.shutdown(socket.SHUT_WR)
        check.raises(EOFError, receive_frame, receiver)
    with tcp_pair() as (sender, receiver):
        sender.sendall((4097).to_bytes(2, "big"))
        check.raises(ValueError, receive_frame, receiver)
    with tcp_pair() as (sender, receiver):
        receiver.settimeout(0.05)
        check.raises(TimeoutError, receive_frame, receiver)

    with fixture() as (url, release):
        client = StatusClient(url)
        try:
            check.equal(client.read()[0]["name"], "mail")
            item = {"id": 2, "name": "queue", "status": "down"}
            check.equal(client.request("POST", payload=item), [item])
            check.equal(len(client.read()), 2)
            item["status"] = "up"
            check.equal(client.request("PUT", payload=item), [item])
            check.true(client.request("DELETE", "/records/2") is None)
            check.equal(len(client.read()), 1)
            for path, cause in [
                ("/fail", requests.HTTPError), ("/html", ValueError),
                ("/badjson", json.JSONDecodeError), ("/invalid", ValueError),
                ("/large", ValueError), ("/redirect", ValueError),
            ]:
                error = check.raises(SourceError, client.request, "GET", path)
                check.true(isinstance(error.__cause__, cause))
            error = check.raises(
                SourceError, client.request, "GET", "/slow",
                timeout=(1, 0.05),
            )
            check.true(isinstance(error.__cause__, requests.Timeout))
            release.set()
            check.equal(len(client.read()), 1)
        finally:
            client.close()
    check.raises(
        ValueError, records, [{"id": True, "name": "x", "status": "up"}],
    )
    item = {"id": 1, "name": "x", "status": "up"}
    check.raises(ValueError, records, [item, item])
    check.equal(json.loads(json.dumps({1: (True, None)})), {"1": [True, None]})
    check.raises(ValueError, json.dumps, float("nan"), allow_nan=False)
    check.equal(json.loads('{"x":1,"x":2}'), {"x": 2})
    print(f"network: {check.count} checks; requests={requests.__version__}")


if __name__ == "__main__":
    run()
```

### storage.py

```python
"""Exercise transactions, trusted XML, CSV, logging and INI settings.

All files and XML are original fixtures created within this run. XML parsing
here is not a general-purpose untrusted-document ingestion boundary.
"""

import configparser
from contextlib import closing
import csv
import io
import logging
from pathlib import Path
import sqlite3
import tempfile
import xml.etree.ElementTree as ET

from checks import Checks
from network import records


class StatusStore:
    """Own a connection with explicit Python 3.12+ transaction behavior."""

    def __init__(self, path):
        """Create and commit the schema before accepting status batches."""
        self.connection = sqlite3.connect(path, autocommit=False)
        self.connection.row_factory = sqlite3.Row
        try:
            with self.connection:
                self.connection.execute(
                    "CREATE TABLE IF NOT EXISTS status ("
                    "id INTEGER PRIMARY KEY, name TEXT NOT NULL, "
                    "status TEXT NOT NULL CHECK(status IN ('up','down')))"
                ).close()
        except Exception:
            self.connection.close()
            raise

    def close(self):
        """Close the owned connection; pending changes are rolled back."""
        self.connection.close()

    def replace(self, items):
        """Validate a batch, then replace all rows in one transaction."""
        records(items)
        with self.connection:
            self.connection.execute("DELETE FROM status").close()
            with closing(self.connection.cursor()) as cursor:
                cursor.executemany(
                    "INSERT INTO status VALUES (:id, :name, :status)", items
                )

    def read(self):
        """Return an independent ordered snapshot of the current rows."""
        with closing(self.connection.execute(
            "SELECT id, name, status FROM status ORDER BY id"
        )) as cursor:
            return [dict(row) for row in cursor.fetchall()]


def write_csv(path, items):
    """Export a validated status list with explicit newline handling."""
    records(items)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["id", "name", "status"])
        writer.writeheader()
        writer.writerows(items)


def read_csv(path):
    """Validate headers, row width and values for a small local CSV file."""
    result = []
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != ["id", "name", "status"]:
            raise ValueError("unexpected CSV header")
        for row in reader:
            if None in row or None in row.values():
                raise ValueError("unexpected CSV row width")
            row["id"] = int(row["id"])
            result.append(row)
            if len(result) > 20:
                raise ValueError("too many rows")
    return records(result)


def write_xml(items):
    """Build original XML using attributes, text and escaped values."""
    records(items)
    root = ET.Element("statuses")
    for item in items:
        node = ET.SubElement(root, "service", id=str(item["id"]))
        ET.SubElement(node, "name").text = item["name"]
        ET.SubElement(node, "status").text = item["status"]
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def read_trusted_xml(body):
    """Read this workbook's XML; reject a different application schema."""
    if len(body) > 4096:
        raise ValueError("fixture XML too large")
    root = ET.fromstring(body)
    if root.tag != "statuses" or root.attrib:
        raise ValueError("unexpected XML root")
    result = []
    for node in root:
        if node.tag != "service" or set(node.attrib) != {"id"}:
            raise ValueError("unexpected service element")
        if [child.tag for child in node] != ["name", "status"]:
            raise ValueError("unexpected service children")
        if any(child.attrib or len(child) for child in node):
            raise ValueError("expected simple text children")
        result.append({
            "id": int(node.get("id")), "name": node.find("name").text,
            "status": node.find("status").text,
        })
    return records(result)


def read_settings(path):
    """Require a settings file and validate its typed polling interval."""
    parser = configparser.ConfigParser()
    with path.open(encoding="utf-8") as stream:
        parser.read_file(stream)
    delay = parser.getint("desk", "poll_ms")
    if not 5 <= delay <= 1000:
        raise ValueError("poll_ms must be between 5 and 1000")
    return parser, delay


def run():
    """Check rollback, resource ownership and common format boundaries."""
    check = Checks()
    workspace = Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory(
        prefix="pcpp-storage-", dir=workspace,
    ) as temporary:
        folder = Path(temporary).resolve()
        check.true(folder.parent == workspace)
        path = folder / "status.sqlite"
        store = StatusStore(path)
        item = {"id": 1, "name": 'a,"b"\nc & <d>', "status": "up"}
        try:
            store.replace([item])
            check.equal(store.read(), [item])
            injection = "x'); DROP TABLE status;--"
            store.replace([{**item, "name": injection}])
            check.equal(store.read()[0]["name"], injection)
            store.replace([item])
            try:
                with store.connection:
                    store.connection.execute("DELETE FROM status").close()
                    store.connection.executemany(
                        "INSERT INTO status VALUES (?, ?, ?)",
                        [(2, "queue", "down"), (2, "duplicate", "up")],
                    ).close()
            except sqlite3.IntegrityError:
                check.equal(store.read(), [item])
            else:
                raise AssertionError("duplicate primary key was accepted")
            check.true(store.connection.in_transaction)
            with store.connection:
                with closing(store.connection.execute(
                    "UPDATE status SET status=? WHERE id=?", ("down", 1)
                )) as cursor:
                    check.equal(cursor.rowcount, 1)
            check.equal(store.read()[0]["status"], "down")
            with store.connection:
                store.connection.execute(
                    "DELETE FROM status WHERE id=?", (1,)
                ).close()
            check.equal(store.read(), [])
            store.replace([item])
            # A connection context manages transactions, not lifetime.
            check.equal(store.connection.execute("SELECT 7").fetchone()[0], 7)
            store.connection.execute("DELETE FROM status").close()
        finally:
            store.close()  # Rolls back that final uncommitted DELETE.
        check.raises(sqlite3.ProgrammingError, store.read)
        with closing(StatusStore(path)) as reopened:
            check.equal(reopened.read(), [item])

        csv_path = folder / "status.csv"
        write_csv(csv_path, [item])
        check.equal(read_csv(csv_path), [item])
        check.true('""b""' in csv_path.read_text(encoding="utf-8"))
        csv_path.write_text("id,name,status\n1,x,up,extra\n", encoding="utf-8")
        check.raises(ValueError, read_csv, csv_path)
        csv_path.write_text("id,name,status\n1,x\n", encoding="utf-8")
        check.raises(ValueError, read_csv, csv_path)
        csv_path.write_text("name,id,status\nx,1,up\n", encoding="utf-8")
        check.raises(ValueError, read_csv, csv_path)
        xml = write_xml([item])
        check.true(b"&amp;" in xml and b"&lt;" in xml)
        check.equal(read_trusted_xml(xml), [item])
        check.raises(ET.ParseError, read_trusted_xml, b"<statuses>")
        check.raises(ValueError, read_trusted_xml, b"<other/>")
        check.raises(
            ValueError, read_trusted_xml,
            b'<statuses><service id="1"><name>x</name></service></statuses>',
        )
        namespaced = ET.fromstring('<s xmlns="urn:desk"><item/></s>')
        check.true(namespaced.find("item") is None)
        check.true(namespaced.find("d:item", {"d": "urn:desk"}) is not None)
        # Well-formed parsing is not DTD validity checking.
        dtd = '<!DOCTYPE s [<!ELEMENT s EMPTY>]><s><child/></s>'
        check.equal(ET.fromstring(dtd).find("child").tag, "child")

        config_path = folder / "desk.ini"
        config_path.write_text(
            "[DEFAULT]\npoll_ms=10\nlabel=Desk\n"
            "[desk]\ntitle=%(label)s status\nenabled=no\n", encoding="utf-8",
        )
        parser, delay = read_settings(config_path)
        check.equal(delay, 10)
        check.equal(parser["desk"]["TITLE"], "Desk status")
        check.equal(parser.getint("desk", "poll_ms", fallback=99), 10)
        check.equal(parser.getboolean("desk", "enabled"), False)
        check.true(bool(parser["desk"]["enabled"]))
        check.equal(parser.read(folder / "absent.ini"), [])
        check.raises(FileNotFoundError, read_settings, folder / "absent.ini")
        parser["desk"]["poll_ms"] = "bad"
        check.raises(ValueError, parser.getint, "desk", "poll_ms")
        parser["desk"]["title"] = "%(missing)s"
        check.raises(
            configparser.InterpolationMissingOptionError,
            parser.get, "desk", "title",
        )
        extended = configparser.ConfigParser(
            interpolation=configparser.ExtendedInterpolation()
        )
        extended.read_string("[a]\nroot=data\n[b]\npath=${a:root}/status\n")
        check.equal(extended["b"]["path"], "data/status")

    check.true(not folder.exists())
    output = io.StringIO()
    logger = logging.getLogger("pcpp.workbook")
    old_level, old_propagate = logger.level, logger.propagate
    handler = logging.StreamHandler(output)
    handler.setLevel(logging.WARNING)
    handler.setFormatter(logging.Formatter("{levelname}:{message}", style="{"))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    try:
        logger.debug("hidden %s", "debug")
        logger.info("hidden %s", "info")
        logger.warning("queue %s", "down")
        logger.error("read %s", "failed")
        logger.critical("desk %s", "stopped")
        check.equal(output.getvalue().splitlines(), [
            "WARNING:queue down", "ERROR:read failed", "CRITICAL:desk stopped",
        ])
        record = logging.LogRecord(
            "pcpp", 20, __file__, 1, "row %s", (7,), None,
        )
        check.equal(record.getMessage(), "row 7")
    finally:
        logger.removeHandler(handler)
        handler.close()
        logger.setLevel(old_level)
        logger.propagate = old_propagate
        output.close()
    print(f"storage: {check.count} checks; sqlite={sqlite3.sqlite_version}")


if __name__ == "__main__":
    run()
```

### desk.py

```python
"""Exercise a withdrawn Tk status desk with bounded original fixtures.

The worker handles source I/O; only the Tk thread touches widgets and the
small SQLite store. Dialog calls are captured, not displayed, by this run.
"""

from contextlib import closing
import logging
from pathlib import Path
from queue import Empty, Queue
import sqlite3
import tempfile
from threading import Event, Thread
import tkinter as tk
from tkinter import messagebox
import xml.etree.ElementTree as ET

from checks import Checks
from network import SourceError, StatusClient, fixture
from objects import Source, trace
from storage import (
    StatusStore, read_csv, read_settings, read_trusted_xml,
    write_csv, write_xml,
)


class RestSource(Source):
    """Read the loopback service using a session owned by the worker."""

    def __init__(self, url):
        """Retain the fixture URL without opening a connection."""
        self.url = url

    def read(self):
        """Create and close the HTTP client on the calling thread."""
        with closing(StatusClient(self.url)) as client:
            return client.read()


class FileSource(Source):
    """Read a trusted XML fixture through the same source contract."""

    def __init__(self, path):
        """Retain the path to this run's original local file."""
        self.path = path

    def read(self):
        """Return records from the original small XML fixture."""
        try:
            return read_trusted_xml(self.path.read_bytes())
        except (OSError, ValueError, ET.ParseError) as error:
            raise SourceError("invalid status file") from error


class Desk:
    """Coordinate source refreshes, storage and a small status display."""

    def __init__(self, root, source, store, poll_ms=10, dialog=None):
        """Create widgets; the caller owns the root and store lifetimes."""
        self.root, self.source, self.store = root, source, store
        self.poll_ms = poll_ms
        self.dialog = dialog or messagebox.showerror
        self.closed = False
        self.pending = None
        self.worker = None
        self.results = Queue()
        self.events = []
        self.visible = []
        self.logger = logging.getLogger("pcpp.desk")
        self.frame = tk.Frame(root)
        self.frame.grid(row=0, column=0)
        self.query = tk.StringVar(root, "")
        self.mode = tk.StringVar(root, "all")
        self.summary = tk.StringVar(root, "Ready")
        tk.Label(self.frame, text="Filter name").grid(row=0, column=0)
        self.entry = tk.Entry(self.frame, textvariable=self.query)
        self.entry.grid(row=0, column=1)
        self.button = tk.Button(
            self.frame, text="Refresh", command=self.refresh,
        )
        self.button.grid(row=0, column=2)
        choices = tk.Frame(self.frame)
        choices.grid(row=1, column=0, columnspan=3)
        self.radios = []
        for mode in ("all", "up", "down"):
            radio = tk.Radiobutton(
                choices, text=mode, variable=self.mode, value=mode,
                command=self.render,
            )
            radio.pack(side="left")  # Different parent from grid-managed rows.
            self.radios.append(radio)
        self.canvas = tk.Canvas(self.frame, width=280, height=80)
        self.canvas.grid(row=2, column=0, columnspan=3)
        tk.Label(self.frame, textvariable=self.summary).grid(
            row=3, column=0, columnspan=3,
        )
        self.trace_id = self.query.trace_add("write", self.query_changed)
        self.binding = root.bind("<<RefreshStatus>>", self.on_refresh)

    def query_changed(self, *args):
        """Adapt Tk's three trace arguments to a parameterless render."""
        self.render()

    def on_refresh(self, event):
        """Adapt an Event callback to the button command contract."""
        self.events.append("bound-event")
        self.refresh()

    def render(self):
        """Filter the stored snapshot and update simple Canvas graphics."""
        query = self.query.get().casefold()
        mode = self.mode.get()
        self.visible = [
            item for item in self.store.read()
            if query in item["name"].casefold()
            and (mode == "all" or item["status"] == mode)
        ]
        self.canvas.delete("all")
        for index, item in enumerate(self.visible):
            self.canvas.create_rectangle(
                index * 12, 10, index * 12 + 10, 40,
                fill="green" if item["status"] == "up" else "red",
            )
        self.summary.set(f"{len(self.visible)} visible")

    def refresh(self):
        """Validate first and start at most one source read at a time."""
        if self.closed or self.pending is not None:
            return
        if len(self.query.get()) > 80:
            self.dialog("Filter", "Use at most 80 characters.")
            return
        self.button.configure(state="disabled")
        self.summary.set("Loading")

        @trace("read", self.events)
        def work():
            try:
                result = self.source.read()
            except Exception as error:
                # Forward the exception object; never touch Tk in this thread.
                self.results.put((False, error))
            else:
                self.results.put((True, result))

        self.worker = Thread(target=work)
        self.worker.start()
        self.pending = self.root.after(self.poll_ms, self.poll)

    def poll(self):
        """Consume a worker result on the Tk thread and retain good state."""
        self.pending = None
        try:
            success, result = self.results.get_nowait()
        except Empty:
            self.pending = self.root.after(self.poll_ms, self.poll)
            return
        self.worker.join()
        try:
            if not success:
                raise result
            self.store.replace(result)
            self.render()
            self.logger.info("refresh records=%s", len(result))
        except (SourceError, ValueError, OSError, sqlite3.Error) as error:
            self.summary.set("Refresh failed; previous records retained")
            self.logger.warning("refresh failed: %s", type(error).__name__)
            self.dialog("Refresh failed", str(error))
        finally:
            self.button.configure(state="normal")

    def close(self):
        """Cancel callbacks, remove observers and join the bounded worker."""
        if self.closed:
            return
        self.closed = True
        if self.pending is not None:
            self.root.after_cancel(self.pending)
            self.pending = None
        if self.worker is not None:
            self.worker.join(3)
            if self.worker.is_alive():
                raise RuntimeError("source worker did not stop")
        self.query.trace_remove("write", self.trace_id)
        self.root.unbind("<<RefreshStatus>>", self.binding)
        self.frame.destroy()


def wait_until(root, condition):
    """Run real Tk events until a condition holds, with a two-second guard."""
    pending = None
    expired = []

    def inspect():
        nonlocal pending
        pending = None
        if condition():
            root.quit()
        else:
            pending = root.after(2, inspect)

    def timeout():
        expired.append(True)
        root.quit()

    watchdog = root.after(2000, timeout)
    pending = root.after(0, inspect)
    try:
        root.mainloop()
    finally:
        root.after_cancel(watchdog)
        if pending is not None:
            root.after_cancel(pending)
    if expired:
        raise AssertionError("GUI condition timed out")


def run():
    """Check refreshes, responsive waiting and retained-state errors."""
    check = Checks()
    workspace = Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory(
        prefix="pcpp-desk-", dir=workspace,
    ) as temporary:
        folder = Path(temporary).resolve()
        check.true(folder.parent == workspace)
        config_path = folder / "desk.ini"
        config_path.write_text("[desk]\npoll_ms=5\n", encoding="utf-8")
        _, delay = read_settings(config_path)
        with fixture() as (url, release), closing(StatusStore(
            folder / "desk.sqlite"
        )) as store:
            root = tk.Tk()
            root.withdraw()
            dialogs, callbacks = [], []
            def report_error(*args):
                callbacks.append(args)

            root.report_callback_exception = report_error
            desk = Desk(root, RestSource(url), store, delay,
                        dialog=lambda *args: dialogs.append(args))
            logger = desk.logger
            handler = logging.NullHandler()
            logger.addHandler(handler)
            old_propagate = logger.propagate
            logger.propagate = False
            try:
                check.equal(root.state(), "withdrawn")
                layout = tk.Frame(root)
                layout.grid(row=1, column=0)
                gridded = tk.Label(layout, text="grid")
                gridded.grid(row=0, column=0)
                placed = tk.Label(layout, text="place")
                placed.place(x=30, y=30)
                packed = tk.Label(layout, text="pack")
                check.raises(tk.TclError, packed.pack)
                check.equal(gridded.winfo_manager(), "grid")
                check.equal(placed.winfo_manager(), "place")
                layout.destroy()
                desk.button.invoke()
                check.equal(str(desk.button["state"]), "disabled")
                wait_until(root, lambda: desk.pending is None)
                check.equal(len(store.read()), 1)
                check.equal(desk.visible[0]["name"], "mail")
                check.equal(len(desk.canvas.find_all()), 1)
                check.equal(desk.events, [
                    "factory:read", "apply:read", "enter:read", "leave:read",
                ])
                desk.query.set("missing")
                check.equal(desk.visible, [])
                desk.query.set("MAIL")
                check.equal(len(desk.visible), 1)
                desk.radios[2].invoke()
                check.equal(desk.visible, [])
                desk.radios[0].invoke()
                desk.query.set("x" * 81)
                desk.button.invoke()
                check.equal(dialogs[-1][0], "Filter")
                check.true(desk.pending is None)
                desk.query.set("")

                xml_path = folder / "status.xml"
                item = {"id": 2, "name": "queue", "status": "down"}
                xml_path.write_bytes(write_xml([item]))
                desk.source = FileSource(xml_path)
                root.event_generate("<<RefreshStatus>>")
                wait_until(root, lambda: desk.pending is None)
                check.true("bound-event" in desk.events)
                check.equal(store.read(), [item])
                write_csv(folder / "status.csv", store.read())
                check.equal(read_csv(folder / "status.csv"), [item])
                xml_path.write_bytes(b"<statuses>")
                desk.button.invoke()
                wait_until(root, lambda: desk.pending is None)
                check.equal(store.read(), [item])
                check.equal(
                    dialogs[-1], ("Refresh failed", "invalid status file"),
                )

                class Broken(Source):
                    def read(self):
                        raise SourceError("fixture offline")

                desk.source = Broken()
                desk.button.invoke()
                wait_until(root, lambda: desk.pending is None)
                check.equal(store.read(), [item])
                check.equal(dialogs[-1], ("Refresh failed", "fixture offline"))
                check.equal(str(desk.button["state"]), "normal")

                gate = Event()

                class Waiting(Source):
                    def read(self):
                        if not gate.wait(1):
                            raise SourceError("gate expired")
                        return [item]

                desk.source = Waiting()
                desk.button.invoke()
                heartbeat = []

                def tick():
                    heartbeat.append(desk.worker.is_alive())
                    gate.set()

                root.after(0, tick)
                wait_until(root, lambda: desk.pending is None)
                check.equal(heartbeat, [True])
                check.equal(store.read(), [item])
                check.equal(callbacks, [])
                gate.clear()
                desk.button.invoke()
                check.true(desk.pending is not None)
                gate.set()
                desk.close()
                desk.close()
                check.equal(desk.query.trace_info(), [])
                check.true(not desk.worker.is_alive())
                check.equal(root.after_info(), ())
                version = root.tk.call("info", "patchlevel")
            finally:
                desk.close()
                root.destroy()
                logger.removeHandler(handler)
                handler.close()
                logger.propagate = old_propagate
    check.true(not folder.exists())
    print(f"desk: {check.count} checks; Tcl/Tk={version}; root destroyed")


if __name__ == "__main__":
    run()
```

## Original knowledge checks

1. When is composition safer than inheritance?
2. What does returning `NotImplemented` from `__eq__` allow?
3. How does Python choose a method in multiple inheritance?
4. Contrast `*args`/`**kwargs` in definitions and calls.
5. Why use `functools.wraps` in a wrapper?
6. Which method type is inheritance-aware for alternate constructors?
7. What makes an abstract class non-instantiable?
8. When are `__context__` and `__cause__` different?
9. What does shallow copying share?
10. Why is unpickling untrusted content unsafe?
11. What creates a class in ordinary Python?
12. Contrast a comment, docstring, and type hint.
13. Why does passing a linter not establish correctness?
14. Which Tkinter geometry-manager combination is prohibited within one parent, and what can coexist?
15. Why can a network callback freeze a GUI?
16. Why can one `recv()` not be assumed to return one message?
17. What should be checked before parsing an HTTP response body?
18. Why must external values be SQL parameters?
19. What is the difference between commit and rollback?
20. Why is `.split(',')` not a CSV parser?
21. What roles do LogRecord, formatter, and handler play?
22. What must be verified before booking PCPP1 now?
23. When is composition or a `collections` wrapper safer than directly subclassing a built-in collection?

## Answers and reasoning

1. Composition fits a has-a relationship and lets a collaborator vary without inheriting an entire API. Inheritance needs substitutability. The workbook's `Runner` accepts any object with `steps()`, while the cooperative diamond intentionally relies on its shared method contract.

2. It tells Python this operand combination is unsupported so the other comparison implementation can participate. It is a special value, not `NotImplementedError`. Equality eventually has an identity fallback if neither side supports it; ordering can instead raise `TypeError`.

3. Lookup follows the class's C3 MRO. In `Diamond(Left, Right)`, `Left.steps()` calls `Right.steps()` through `super()`, then `Root.steps()`. Hard-coding `Root.steps(self)` would skip that cooperative chain.

4. Definitions collect surplus positional arguments in a tuple and keywords in a dictionary; calls unpack an iterable and mapping into arguments. Forward both forms when wrapping. Duplicate or invalid keyword bindings still fail normally.

5. It copies useful metadata and adds `__wrapped__`, making documentation and introspection more faithful. It does not validate arguments or erase the wrapper's behavior. The trace example separately proves factory evaluation, decoration and call order.

6. A class method receives the actual `cls`, so an inherited alternate constructor can build the subclass. A static method receives neither class nor instance automatically; it is appropriate for related behavior that needs neither.

7. A normal ABC subclass cannot instantiate while abstract methods remain. Those methods may still have bodies. Virtual registration only affects recognition; it neither injects methods nor enforces their implementation on the registered class.

8. Context is the exception already being handled when a new one arises. An explicit `from error` sets the cause used in traceback presentation. `from None` suppresses context display but leaves the context object inspectable; neither form makes the failure successful.

9. It creates a new outer container while retaining nested references. Deep copying uses memoization, so shared children and cycles are preserved as relationships in the new graph. Neither operation promises sensible duplication of every external resource.

10. Reconstruction can invoke executable behavior. Only restore trusted provenance, and account for importable class names, protocol compatibility and changed definitions. The shelf examples use original data from the same run; a database-like interface does not make untrusted pickle safe.

11. A metaclass, normally `type`, constructs the class object from its name, bases and namespace. `type(value)` inspects a type; `type(name, bases, namespace)` creates one. Class decorators run after creation. Prefer a simpler class decorator or subclass hook when it meets the need.

12. A comment explains context in source, a leading string docstring becomes runtime documentation, and annotations describe types for readers/tools. PEP 257 favors a concise summary followed by a blank line and details when needed; annotations alone do not check runtime values.

13. A checker covers its configured rules and assumptions. Clean naming and line lengths cannot prove rollback, responsiveness or requirements. Here selected Ruff rules and 173 behavioral checks are recorded separately, with human review still pending.

14. Tk rejects `pack` and `grid` managing children in the same container. Separate nested containers can use different managers. Distinct children using `grid` and `place` can coexist, although explicit placement can overlap the grid. The withdrawn-root probes verify both cases.

15. The main loop cannot process input, repainting or timers while a callback blocks. Scheduling that callback with `after` does not move it to another thread. The desk performs source I/O in a worker, queues the result and applies it through a short Tk-thread poll.

16. TCP supplies ordered bytes, not application-message boundaries. A read may be short or include bytes from multiple writes. Read according to a framing protocol, cap lengths, detect EOF and retain excess bytes if using a buffered delimiter parser. This workbook reads exactly each length-prefixed frame.

17. Check the intended status, redirect policy, media type, size and body contract; then handle decoding and schema failures. JSON decoding can succeed for an HTTP error. A 204 response in this fixture has no JSON body. Requests timeouts do not establish an overall deadline.

18. Binding keeps external values out of SQL syntax and handles quoting/types. SQL identifiers require a separate fixed/allowlisted choice. An injection-looking name remains a name in the workbook. Also verify transaction boundaries and the `WHERE` clause; parameterization alone does not prevent an unintended broad update.

19. Under `autocommit=False`, commit preserves the transaction's changes and rollback discards them, then a new transaction opens. A connection context manages that boundary, not resource closure. A failed batch must roll back earlier writes as well; the workbook verifies recovery after a duplicate key.

20. Quoted commas, escaped quotes and embedded newlines are part of CSV records. Use the CSV parser with `newline=""`, validate headers/width, and explicitly convert fields. The original name containing a comma, quote and newline survives a writer/reader round trip.

21. The record carries event fields and message arguments, the formatter renders it, and the handler emits it to a destination. Logger/handler thresholds can suppress it; propagation can cause duplicates if handlers are attached at several levels. Formatter style does not change message-argument interpolation.

22. Check that the purchased and schedulable version is still 101, distinguish its lifetime validity from the developing 102's five-year description, and confirm delivery formats, actual appointment change rules and retake terms. No release date or current successful booking was inferred from development wording.

23. Prefer a wrapper when construction, slice assignment, inherited copying or other mutation paths would undermine the intended invariant. The example adds metadata without restricting list behavior and shows that `list.copy()` returns a base list, whereas `copy.copy()` retains this subclass. Inspect the whole exposed contract.

## Readiness checklist

- [ ] I can implement every OOP objective, including a substitutable built-in subclass, and explain when composition or a collection wrapper is safer.
- [ ] I can trace decorator, MRO, exception-chain, and object-copy behavior before execution.
- [ ] I can review a module against PEP 1/8/20/257/484 boundaries.
- [ ] I can build and debug the required Tkinter widgets, layouts, variables, and callbacks.
- [ ] I can explain socket framing and implement a defensive REST/JSON client.
- [ ] I can transact safely with SQLite and process XML/CSV/log/config data.
- [ ] I completed the integrated build and can demonstrate recovery from each boundary failure.
- [ ] I rechecked whether PCPP-32-102 has replaced PCPP-32-101.

## Source and freshness notes

- [Official PCPP1 syllabus](https://pythoninstitute.org/pcpp1-exam-syllabus): canonical objectives, weights, and March 2022 baseline.
- [Official PCPP1 page](https://pythoninstitute.org/pcpp1): current version, format, delivery, validity, price, retake and transition status.
- Technical behavior should be checked in the [Python standard-library documentation](https://docs.python.org/3/library/), [Requests documentation](https://requests.readthedocs.io/en/latest/), and the named PEPs.
- The blueprint is older than several current Python releases. Study the named contract; do not assume every modern feature is in scope.

## Places to learn

This is not a complete list and should not be consumed in full. Use the five official advanced courses as the aligned spine, then fill documented gaps with primary references and one substantial build.

| Resource | Access | Estimated time |
|---|---|---:|
| [PCPP-32-101 syllabus](https://pythoninstitute.org/pcpp1-exam-syllabus) | Free official blueprint | 3–5 hours to map |
| [Python Advanced 1: OOP](https://edube.org/study/pcpp1-1) | Free official public outline; enrollment required for lessons | Provider: 42 hours |
| [Python Advanced 2: PEPs](https://edube.org/study/pcpp1-2) | Free official public outline | Provider: 10 hours |
| [Python Advanced 3: GUI](https://edube.org/study/pcpp1-3) | Free official public outline | Provider: 21 hours |
| [Python Advanced 4: networking](https://edube.org/study/pcpp1-4) | Free official public outline | Provider: 21 hours |
| [Python Advanced 5: files](https://edube.org/study/pcpp1-5) | Free official public outline | Provider: 21 hours |
| [Python documentation](https://docs.python.org/3/) | Free primary reference | 20–35 selected hours |
| [PEP 8](https://peps.python.org/pep-0008/), [PEP 257](https://peps.python.org/pep-0257/), [PEP 484](https://peps.python.org/pep-0484/) | Free primary standards | 4–7 hours plus review |
| [Python 3 Object-Oriented Programming](https://www.oreilly.com/library/view/python-3-object-oriented/9781804611864/) | O'Reilly subscription/book | 20–35 selected hours |
| [TkDocs tutorial](https://tkdocs.com/tutorial/) | Free independent Tkinter tutorial | 8–15 hours with implementation |
| [Requests documentation](https://requests.readthedocs.io/en/latest/) | Free project documentation | 4–8 hours |
| [Pluralsight catalog](https://www.pluralsight.com/browse/software-development/python) | URL resolves to a broad software-development catalog; no verified PCPP1 path | Author budget: 15–30 selected hours |

The five complete public Edube outlines total **115 provider hours** (42 + 10 + 21 + 21 + 21). These are provider estimates, not measured completion times. They list 32-101 alignment and recommend Python Essentials 2; the first landing retains stale CSPP1/PCPP1 “coming soon” text. No enrolled lesson or assessment was read. Add your own implementation/revision time. O'Reilly returned 403 and TkDocs could not be retrieved; current interiors and durations are unverified. The Pluralsight URL returns a broad catalog with some Python courses, not a verified PCPP1 path. Other hour ranges above are author planning estimates.

The official page explicitly says no official PCPP1 practice test is available. Any third-party product must be checked for exact `PCPP-32-101` alignment and should not be treated as an authority or a source of recalled exam questions.

## Primary contracts and review evidence

- OOP: [data model](https://docs.python.org/3.13/reference/datamodel.html), [built-ins](https://docs.python.org/3.13/library/functions.html), [ABC](https://docs.python.org/3.13/library/abc.html), [wraps](https://docs.python.org/3.13/library/functools.html), [exceptions](https://docs.python.org/3.13/library/exceptions.html), [copy](https://docs.python.org/3.13/library/copy.html), [pickle](https://docs.python.org/3.13/library/pickle.html), [shelve](https://docs.python.org/3.13/library/shelve.html).
- Conventions: [PEP 1](https://peps.python.org/pep-0001/), [PEP 20](https://peps.python.org/pep-0020/), plus the PEP 8/257/484 links above. These readings have explicit boundaries; current typing is broader than the historical PEP.
- Interfaces: [Tkinter](https://docs.python.org/3.13/library/tkinter.html), [sockets](https://docs.python.org/3.13/library/socket.html), [JSON](https://docs.python.org/3.13/library/json.html), [Requests quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/) and [advanced session/timeout guidance](https://requests.readthedocs.io/en/latest/user/advanced/).
- Data: [SQLite](https://docs.python.org/3.13/library/sqlite3.html), [closing](https://docs.python.org/3.13/library/contextlib.html), [CSV](https://docs.python.org/3.13/library/csv.html), [ElementTree](https://docs.python.org/3.13/library/xml.etree.elementtree.html), [XML processing boundaries](https://docs.python.org/3.13/library/xml.html), [XML 1.0 well-formedness and validity](https://www.w3.org/TR/xml/), [logging](https://docs.python.org/3.13/library/logging.html), [configuration](https://docs.python.org/3.13/library/configparser.html).
- Administration: [Pearson policy](https://pythoninstitute.org/pvue-testing-policies) and [scheduling](https://pythoninstitute.org/schedule-exam-pvue); actual account/appointment terms remain unverified.

The [September 29 deep-review report](../docs/research/2026-09-29-pcpp-32-101-deep-review.md) records all 24 objective mappings, source access and selected-reading boundaries, original code execution, remaining format/scoring/policy questions and human-review limits. A downloaded aggregate is not a claim that every section or linked page was read.
