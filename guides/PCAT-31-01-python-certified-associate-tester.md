---
exam_code: PCAT-31-01
vendor_id: python-institute
official_blueprint: https://pythoninstitute.org/pcat-exam-syllabus
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-30
upcoming_change_status: scheduled
upcoming_change_checked: 2026-09-30
---

# PCAT-31-01 Certified Associate Tester with Python Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Deep-reviewed September 30, 2026; exact original multi-module suite and framework/TDD probes executed with explicit limits. Use the [official PCAT syllabus](https://pythoninstitute.org/pcat-exam-syllabus) with the documented inconsistencies below.

**Current baseline:** PCAT-31-01, active; six-block syllabus last updated July 5, 2024<br>
**Upcoming blueprint change:** PCAT-31-02 is in development, with no launch date found in the reviewed public pages; the current syllabus introduction prematurely names `31-02` and says four blocks while its header, alignment, table, and objective codes describe `31-01` and six blocks<br>
**Official delivery snapshot:** 42 questions; 60 minutes plus NDA; 75% cumulative passing score; single-/multiple-select and scenarios; TestNow; English<br>
**Credential snapshot:** no formal prerequisite; PCET plus PCEP/PCAP-equivalent and field skills recommended; six-year validity; USD 195 exam or USD 225 with retake when checked; 15-day retake wait; official practice tests still described as in development<br>

**VERIFY CURRENT:** The [credential FAQ](https://pythoninstitute.org/pcat) describes dedicated practice tests as in development, even though its voucher instructions mention a practice bundle and the [PT102 store listing](https://ums.edube.org/products/pi-pt102-courseware) promises a PCAT practice test and 20% exam discount with premium course access. Availability and exact entitlement are unresolved; these statements do not prove that the same standalone practice product has launched. No account, cart, purchase or protected questions were accessed.

The complete [PCAT testing policy](https://pythoninstitute.org/pcat-testing-policies) has a specific **15-day failed-retake rule** matching the credential FAQ, while generic footer prose says seven days after failing or passing. Preserve the specific rule and confirm eligibility before acting. Local partner appointments generally require at least 24 hours for rescheduling; the global unredeemed-voucher route has different scheduling procedures. No booking or device system test was performed.

## How to use this guide

Choose a multi-module Python application and make its unit-test suite the study artifact. Every objective should appear in working test code or an explicit design note. Deliberately inject faults so you know which test catches them and why.

> **About related items:** A `Related item:` callout is adjacent professional context, not additional exam scope.

## Weighted objective map

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| Testing essentials | 7 | 16.7% | Explain risks, principles, levels, pyramid, and coverage |
| Automation/refactoring | 4 | 9.5% | Automate stable checks and refactor incrementally under tests |
| Python mechanisms | 5 | 11.9% | Use assertions, context managers, decorators, and method types correctly |
| Unit-testing foundations | 12 | 28.6% | Build discoverable `unittest` suites with precise assertions and fixtures |
| Advanced unit testing | 11 | 26.2% | Parameterize, select/mark, mock/patch, and test errors without leakage |
| TDD and BDD | 3 | 7.1% | Apply red-green-refactor and Given/When/Then at the right abstraction |

The retained snapshot contains **34 numbered objectives**, grouped 7/4/5/8/7/3, versus **42 exam items**, grouped 7/4/5/12/11/3. Do not confuse objective counts with question counts. The canonical page's Block 2 heading says three objectives but lists four (2.1–2.4). Its introductory text also says 31-02, four blocks and data analysis, contrary to its active 31-01 header, six-block table and testing content. All numbered objectives and the complete minimum-qualified-candidate profile were read manually after the direct fetch and automated monitor timed out. The snapshot was retained; no successful automated hash comparison or complete PDF reading is claimed.

## 1–2. Testing essentials, automation, and refactoring — 26.2%

Testing provides evidence and exposes defects; it cannot prove perfection. Understand unit, integration, system, and acceptance scopes; errors/defects/failures; the seven testing principles; entry/exit criteria; risk; and the test pyramid. Coverage identifies executed structure, not assertion quality.

Automate frequent, deterministic, valuable checks whose maintenance cost is justified. Keep exploratory/usability judgment where humans add value. Refactor in a loop: establish green characterizing tests, make one behavior-preserving change, rerun, and review. AAA clarifies setup, one principal action, and observable result. DRY removes duplicated knowledge; KISS avoids premature architecture.

### Requirements, test scope and automation decisions

The original workbook uses a tiny **synthetic token catalog**, not payments or real inventory. Requirements are stated independently of the tests:

| Contract | Required behavior and selected oracle |
|---|---|
| Code and price | Nonempty exact text codes are stripped/uppercased; positive exact integer prices exclude booleans; canonical collisions are rejected; caller data is copied |
| Quote | Exact integer quantity 1–5 inclusive; validate quantity before lookup; A costs 7 tokens and B costs 11, so A×5=35 and B×5=55 |
| Unknown item | Raise `UnknownItem` with canonical code, specific message/args and a `KeyError` cause; preserve catalog contents |
| Construction | `from_pairs` constructs the actual subclass; exact duplicate raw keys follow ordinary `dict` behavior, while different raw codes that normalize to one key are rejected |
| Resource ownership | Own files opened by the service; propagate parsing errors after context exit; successful resource entry leads to exit on normal/body-error paths; failed entry cleans up its own partial acquisition |
| Publishing | Validate before reading the clock or calling the client; post one complete quote with explicit timeout; propagate a collaborator exception without retry |

Test levels describe scope, not a file naming convention. `Catalog.quote` tests are small unit checks; `service.publish` tests combine the real catalog with a fake interface boundary. Mocked file and HTTP-shaped calls do not establish real filesystem, provider, assembled-system or stakeholder acceptance behavior. Those require separate tests and access. Non-functional performance, security and usability also need their own requirements and evidence.

The seven principles guide decisions: a detected mismatch demonstrates a defect, while green samples cannot show absence; exhaustive testing is generally infeasible; earlier review shortens feedback; clustered defects suggest focused investigation; unchanged regression suites need new cases as risk evolves; a tiny teaching catalog has different risks from a production service; and perfect conformance to the wrong requirements still fails the user's need. These are judgment aids, not numerical guarantees of defect density or savings.

Entry criteria could require agreed contracts, a repeatable environment, owned fixtures and known expected values. Exit criteria could require selected cases passing, defects triaged and unresolved risk accepted by the responsible person. Skips, expected failures and untested integrations must appear in that decision. A pyramid usually favors fast independent checks, but architecture, risk and maintenance cost determine a useful mix.

Automate stable, repeatable checks with clear oracles. A frequently changing UI, external nondeterminism or subjective usability judgment may need a different approach. Mocks make local tests faster but create a contract-verification obligation; they do not remove the external dependency's real behavior. Keep targeted selection for rapid feedback and a full relevant suite for integration decisions.

### Observed coverage limit

The [coverage.py branch documentation](https://coverage.readthedocs.io/en/latest/branch.html) distinguishes executable statements from decision destinations. The original `allowed` probe deliberately uses `1 <= quantity < 5` where the integer contract includes 5. Inputs **0 and 1** return the expected False/True and execute **4/4 statements and 2/2 branches: 100% combined coverage**. Only a later, independent boundary-5 check exposes expected True versus actual False. Coverage identifies execution opportunities, not all important values or correct oracles.

The probe measures only that temporary module, starting before import, with no added exclusions or persistent coverage database. [The selected API contracts](https://coverage.readthedocs.io/en/latest/api_coverage.html) support start/stop and JSON reporting. Runtime coverage.py 7.15.4 differs from documentation 7.16.2. No whole-catalog coverage, method-coverage total or type-policy completeness is inferred. Unexecuted code may be untested, unreachable under current assumptions or obsolete; investigate before labeling it dead or excluding it from a denominator.

## 3. Assertions, contexts, decorators, and method types — 11.9%

Language `assert` may be disabled and is not a production validation mechanism. Test-framework assertions remain normal method calls and are not removed by `-O`. A successful context-manager entry is followed by exit during normal completion or exception unwinding through `with`; the “code sandwich” places variable work between stable acquisition and release.

A function decorator receives/replaces a function; a class decorator receives/replaces a class. Decorators execute at definition time and stacked decorators apply bottom-up. Preserve metadata and avoid hidden global state.

Instance methods receive `self`, class methods receive `cls`, and static methods receive no implicit first argument. Choose from the state/contract required, not to avoid passing an argument.

### Executed mechanism contracts

The custom `Lease` records `enter` then `exit:ok` on success, or `exit:LookupError` while propagating the **same** body exception. `__exit__` returns False; returning True would suppress a body exception. If `__enter__` raises, Python does not call that manager's `__exit__`: the example performs its partial-acquisition cleanup inside entry and verifies that the body never runs. This is normal interpreter control-flow evidence, not a guarantee against process termination. The generator-based `owned_lease` yields once and uses `finally`; catching an exception without reraising it can accidentally suppress it. See [the with statement](https://docs.python.org/3.13/reference/compound_stmts.html) and selected [contextlib](https://docs.python.org/3.13/library/contextlib.html).

The original `traced` decorator logs application as **inner, outer** at definition time; calling the decorated function records **outer entry, inner entry, body, inner exit, outer exit**. `finally` preserves both cleanup events and the exact raised exception. [functools.wraps](https://docs.python.org/3.13/library/functools.html) preserves name/docstring metadata and provides `__wrapped__` access. Metadata preservation does not prove that a wrapper preserves every behavior.

The class decorator adds a teaching label and returns the original class; tests verify identity. Other decorators can replace a class, so callers must understand the contract. `Catalog.from_pairs` is a class method because it constructs `cls`, preserving a subclass. The normalizer is static because it uses neither class nor instance state; `quote` is an instance method because it reads that catalog's prices. See the selected [classmethod/staticmethod contracts](https://docs.python.org/3.13/library/functions.html). Do not choose method types merely for stylistic variety.

Mandatory catalog validation uses explicit exceptions. Its `TestCase` assertions and the probe's explicit checks run normally and with `-O`; this verifies that these checks remain active. Language `assert` still belongs to optional internal invariants, not input, authorization or required side effects. Optimization behavior does not automatically transfer to every third-party testing framework's assertion machinery.

## 4. Unit-testing foundations — 28.6%

FIRST tests are Fast, Independent, Repeatable, Self-validating, and Timely. xUnit architecture organizes test cases into suites, uses fixtures for controlled state, and a runner for discovery/execution/reporting. Keep production and test files clearly separated and use discoverable `test_...` names.

Subclass `unittest.TestCase`. Use `setUp`/`tearDown` for per-test state and discovery from the command line or runner. Prefer the assertion that communicates intent: equality, approximate numeric equality, truth/falsehood, identity, membership, ordering, and `assertRaises` for exceptions. A test is executable documentation only when its name, setup, and expected outcome reveal a stable contract.

The complete `test_catalog.py` below is executable and imports its dependencies explicitly. For an unknown item it checks type, canonical code, exact contractual message/args, preserved cause and unchanged catalog contents. This is more informative than a broad `except Exception: pass`, which can accept the wrong failure or no failure at all.

### Assertion precision, discovery and reproducibility

Use `assertEqual` for expected values, `assertIs` for object identity, `assertIn` for membership and greater/less assertions for ordering. `assertTrue(x)` checks truthiness, not necessarily identity with the singleton True. The original suite exercises every specialized assertion named in Objective 4.5 against catalog, resource and exception behavior; it also distinguishes type and value rejection using labeled subtests.

The ratio of A's one-item quote to its five-item quote is compared with 0.2 using an explicit absolute tolerance of `1e-12`. [unittest's assertAlmostEqual](https://docs.python.org/3.13/library/unittest.html) defaults to rounding the difference to seven decimal places, not seven significant digits or a relative tolerance. Choose a tolerance from the domain, not merely one that makes a failure disappear. Exact token amounts remain integers and use exact equality.

FIRST means keep feedback quick, isolate state, control nondeterminism, assert outcomes automatically and write tests in time to guide the work. Timely does not justify accepting flaky or order-dependent tests. AAA separates fixture construction, the action and meaningful expectations; several assertions about one returned contract can be appropriate. Do not regenerate the expected value with the same production function.

Python 3.13 discovery imports modules; use valid names, an intentional top-level directory and regular packages where required. Import-time side effects can occur during discovery, so keep expensive or external work out of module import. The workbook uses separate `catalog.py`, `service.py`, `test_catalog.py` and `probes.py`; the discovery pattern selects only the intended test file. Test names and explicit outputs document contracts, but the suite cannot replace a complete specification or integration plan.

## 5. Advanced unit testing — 26.2%

Use method fixtures for isolated state, class fixtures for genuinely read-only expensive state, and module fixtures sparingly. Shared mutable fixtures create order dependence. Parameterization runs the same behavioral claim against multiple data rows; `subTest` is the standard `unittest` mechanism for distinguishable iterations.

`@unittest.skip`, `skipIf`, and `expectedFailure` report intentional conditions. A skip needs a current reason; expected failure should not become a permanent hiding place. Selective execution speeds feedback, but the full suite remains the integration gate.

`Mock` records/configures calls; `MagicMock` supplies magic-method behavior. `patch` replaces the name looked up by the system under test—usually patch where used, not where originally defined. Use autospeccing when suitable to catch invalid calls. Configure return values/side effects, assert meaningful interactions, and let patch cleanup restore state.

Test exceptions with `assertRaises` or its context form, then inspect the captured exception when message/attributes are contractual. Cover success, expected failure, cleanup, and propagation.

> **Related item:** Prefer a small fake or dependency injection when a web of mocks merely recreates the implementation. Test doubles should simplify the contract boundary.

### Fixture lifecycle and honest result interpretation

The actual grouped fixture probe records this order: module setup, class setup, each method's setup/body/teardown/cleanup, class teardown/cleanup, then module teardown/cleanup. Each method gets a fresh list; test A's mutation does not reach test B. Class/module hooks are controlled by suite ordering and may run more than once if a custom order interleaves classes/modules. Treat shared mutable fixtures carefully; expensive does not automatically mean safe to share.

A separate seeded setup error registers two cleanups, then raises. The observed trace is **setup, second cleanup, first cleanup**; the body and `tearDown` do not run. It is reported as one error, not a body assertion failure. Register cleanup as resources are acquired, because `tearDown` only runs after successful `setUp`. The selected [unittest fixture and result contracts](https://docs.python.org/3.13/library/unittest.html) explain this distinction.

| Original inner experiment | Observed result | Interpretation |
|---|---|---|
| Two explicit unavailable-adapter demonstration skips and one known body defect marked expected failure | 3 methods reported; 2 skipped, 1 expected failure; `wasSuccessful()` True | Success does not mean all three behaviors executed and passed |
| Repair the seeded defect while retaining expected-failure marker | 1 unexpected success; `wasSuccessful()` False | Remove the obsolete marker after confirming the fix |
| Expected-failure method whose setup raises | 1 setup error, no expected failure | The marker does not absorb fixture errors |
| Select only the empty-state test | 1 passing method | It passes in isolation |
| Run mutation then empty-state expectation against shared class state | 2 methods, 1 assertion failure | The full suite exposes contamination |
| Reverse those two methods | Both pass | Order can hide the same defect |
| Give each method its own list | Both pass | The fixture addresses the demonstrated shared-state issue |

These are intentional **inner demonstration results** inspected by 31 outer checks; they are not hidden green production tests. The 25-method application suite has no skips or expected failures. A real skipped integration test needs a concrete dependency/reason, an owner and a removal/revisit condition. The demonstration does not stand in for a working real adapter. Expected failures should not be permanent hiding places, and a filtered run should report its selected count.

CLI `-k boundary` uses case-sensitive substring matching when no wildcard is present; programmatic `TestLoader.testNamePatterns` uses shell-style patterns, so the probe uses `*requires_empty`. The actual CLI subset runs one boundary method, while full discovery runs 25. Selected success establishes only the subset's result.

### Mocks, patching and exception paths

The service imports `monotonic` and aliases `open` as `open_text`. Tests patch **`service.monotonic` and `service.open_text`**, the names it looks up, and verify restoration. Patching the original definition elsewhere after import may not affect an already-bound name. Patch contexts restore state on exit; manually started patches need registered cleanup. See [unittest.mock](https://docs.python.org/3.13/library/unittest.mock.html).

`mock_open` supplies a limited file-like/context-manager substitute. Tests observe normal exit, parse-error exit arguments and exact propagated errors; this does not prove real filesystem behavior or every stream operation. `MagicMock` supports selected protocol methods such as `__enter__`/`__exit__`; magic calls appear in `mock_calls`, and defaults can mask an unconfigured behavior. Configure the part of the protocol that matters.

An autospecced HTTP-shaped client's `post(payload, *, timeout)` rejects missing timeout or misspelled attributes. Tests verify one complete original payload, no clock/client use after invalid lookup, and propagation of the same timeout exception without retry. **There is no HTTP implementation or real request.** Signature checking is not contract validation against a live provider. The clock value is monotonic elapsed time, not a calendar timestamp or event identity.

## 6. TDD and BDD — 7.1%

TDD cycles: write a small failing test (**red**), implement the simplest correct behavior (**green**), improve design under green tests (**refactor**). Red must fail for the expected reason; otherwise it may not test the new requirement.

BDD expresses shared behavior in domain language. Given establishes context, When identifies the event/action, Then states observable outcome. BDD is collaboration/specification, not merely a syntax wrapper around low-level unit tests.

### Recorded red–green–refactor slice

The original requirement is to split a list into consecutive chunks of positive exact integer size, retain a final short chunk, preserve order and leave the input unchanged. Wrong containers/sizes raise explicit errors; booleans are rejected as sizes.

| Phase | Executed implementation | Recorded result against the same three test methods |
|---|---|---|
| Red | Validate, then return the entire nonempty list as one chunk | Exactly one assertion failure: `[[1, 2, 3]]` differs from `[[1, 2], [3]]`; no errors |
| Green | Advance an index through a loop, appending slices | All three methods pass |
| Refactor | Use a list comprehension over the same slice starts, retain validation | All three methods pass |

The fixed oracles include empty input, one item, a remainder, size one, an oversized chunk, invalid sizes and an invalid container. The red phase fails for missing boundary behavior, not an import/setup error. Sources, hashes and results for all three phases are recorded. This is one original test-first slice, not five refactor commits, exhaustive proof, a project history reconstructed after the fact or a measured productivity gain. TDD helps expose an API from the caller's perspective but cannot establish good requirements or all integration behavior.

An original Given/When/Then statement is: **Given** the ordered list `[1,2,3]`, **when** it is grouped by two, **then** the result is `[[1,2],[3]]` and the input is unchanged. A domain stakeholder would usually use meaningful item names and discuss examples/ambiguities before automation. BDD's collaboration matters more than keywords. No stakeholder workshop, `behave` step binding or browser scenario was executed.

## Exact original executable workbook

Save these four blocks under their exact filenames in one directory. The application and 25 tests use the standard library; `probes.py` additionally uses existing coverage.py. Recorded execution uses CPython 3.13.14, coverage.py 7.15.4 and Ruff 0.16.4, with no installations. From that directory:

```text
python -B -Werror -m unittest discover -s . -p test_catalog.py -v
python -B -Werror -O -m unittest discover -s . -p test_catalog.py -v
python -B -Werror -m unittest -v test_catalog -k boundary
python -B -Werror probes.py
python -B -Werror -O probes.py
python -m ruff check catalog.py service.py test_catalog.py probes.py --select E4,E7,E9,F,W,E501 --line-length 79
```

Exact extracted files match the executed sources: **25 application test methods per normal/optimized run, one selected boundary method, and 31 probe checks per mode**. Subtest rows and inner demonstration cases are reported separately, not added to the 25. Selected [Ruff rules](https://docs.astral.sh/ruff/linter/) pass at 79 columns; this is neither complete style conformance nor semantic proof. Normal/optimized probe reports match. Temporary original modules and coverage reports stay beneath the workbook directory and are removed; no persistent database, real service, package installation or external request is used.

### catalog.py

```python
"""Provide original synthetic token quotes for PCAT test exercises.

There are no payments, real inventory reservations or external services.
Codes are nonempty stripped uppercase strings. Prices are positive exact
integers; quantities are exact integers in 1..5. Booleans are not integers
for these deliberately strict contracts.
"""

from contextlib import contextmanager
from functools import wraps


class UnknownItem(LookupError):
    """Expose the missing canonical code as a contractual attribute."""

    def __init__(self, code):
        self.code = code
        super().__init__(f"unknown item: {code}")


def teaching_model(cls):
    """Add an original class label while retaining the same class object."""
    cls.category = "synthetic-token-catalog"
    return cls


@teaching_model
class Catalog:
    """Copy and validate caller data; expose quotes without mutation."""

    def __init__(self, prices):
        self._prices = {}
        for raw_code, price in dict(prices).items():
            code = self.canonical_code(raw_code)
            if type(price) is not int:
                raise TypeError("price must be an exact int")
            if price <= 0:
                raise ValueError("price must be positive")
            if code in self._prices:
                raise ValueError("duplicate canonical code")
            self._prices[code] = price

    @staticmethod
    def canonical_code(code):
        """Normalize nonempty text without needing instance or class state."""
        if type(code) is not str:
            raise TypeError("code must be text")
        result = code.strip().upper()
        if not result:
            raise ValueError("code must not be empty")
        return result

    @classmethod
    def from_pairs(cls, pairs):
        """Construct the actual class; duplicate raw keys follow dict rules."""
        return cls(dict(pairs))

    def quote(self, code, quantity=1):
        """Return a token amount; validate quantity before looking up code."""
        if type(quantity) is not int:
            raise TypeError("quantity must be an exact int")
        if not 1 <= quantity <= 5:
            raise ValueError("quantity must be in 1..5")
        key = self.canonical_code(code)
        try:
            price = self._prices[key]
        except KeyError as exc:
            raise UnknownItem(key) from exc
        return price * quantity

    def codes(self):
        """Return a sorted immutable snapshot of the available codes."""
        return tuple(sorted(self._prices))


def traced(label, events):
    """Record decorator application/calls in a caller-owned teaching list."""
    def decorate(function):
        events.append("decorate:" + label)

        @wraps(function)
        def wrapper(*args, **kwargs):
            events.append("enter:" + label)
            try:
                return function(*args, **kwargs)
            finally:
                events.append("exit:" + label)
        return wrapper
    return decorate


class Lease:
    """Model an owned resource with explicit entry, closure and propagation."""

    def __init__(self, events, fail_enter=False):
        self.events = events
        self.fail_enter = fail_enter
        self.closed = False

    def __enter__(self):
        self.events.append("enter")
        if self.fail_enter:
            # Entry owns cleanup of its partial acquisition.
            self.closed = True
            self.events.append("entry-cleanup")
            raise RuntimeError("synthetic acquisition failure")
        return self

    def __exit__(self, exc_type, exc, traceback):
        self.closed = True
        self.events.append("exit:" + (exc_type.__name__ if exc_type else "ok"))
        return False


@contextmanager
def owned_lease(events):
    """Yield exactly once and propagate body errors after local cleanup."""
    resource = Lease(events)
    try:
        yield resource
    finally:
        resource.closed = True
        events.append("generator-cleanup")
```

### service.py

```python
"""Compose original catalog, file and HTTP-shaped interfaces.

Tests replace every file/clock/client boundary. No network is implemented.
"""

from builtins import open as open_text
import json
from time import monotonic

from catalog import Catalog


class QuoteClient:
    """Declare a synthetic HTTP-shaped collaborator, with no transport."""

    def post(self, payload, *, timeout):
        """Post one quote; concrete implementations define delivery."""
        raise NotImplementedError


def load_catalog(filename):
    """Own the opened file and close it on success or parsing failure."""
    with open_text(filename, encoding="utf-8") as stream:
        values = json.load(stream)
    if not isinstance(values, dict):
        raise TypeError("catalog JSON must be an object")
    return Catalog(values)


def publish(catalog, code, quantity, client):
    """Validate first, capture monotonic time and post exactly once.

    Propagate collaborator exceptions without retry. The time value is an
    elapsed-clock reading, not a calendar timestamp or durable event identity.
    """
    amount = catalog.quote(code, quantity)
    payload = {"code": catalog.canonical_code(code), "quantity": quantity,
               "tokens": amount, "clock": monotonic()}
    client.post(payload, timeout=1.0)
    return payload
```

### test_catalog.py

```python
"""Discover original PCAT tests with unittest; no real I/O is required."""

import json
import unittest
from unittest.mock import create_autospec, MagicMock, mock_open, patch

import catalog
import service


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.source = {" a ": 7, "B": 11}
        self.catalog = catalog.Catalog(self.source)

    def test_boundary_quotes(self):
        for code, quantity, expected in [("A", 1, 7), ("A", 5, 35),
                                         ("B", 1, 11), ("B", 5, 55)]:
            with self.subTest(code=code, quantity=quantity):
                self.assertEqual(self.catalog.quote(code, quantity), expected)

    def test_quantity_types_and_partitions(self):
        for quantity in [True, 1.0, "1", None]:
            with self.subTest(quantity=quantity):
                self.assertRaises(TypeError, self.catalog.quote, "A", quantity)
        for quantity in [-10, 0, 6, 100]:
            with self.subTest(quantity=quantity):
                with self.assertRaisesRegex(ValueError, r"1\.\.5"):
                    self.catalog.quote("A", quantity)

    def test_canonical_code_and_snapshot(self):
        self.assertEqual(self.catalog.canonical_code(" b "), "B")
        codes = self.catalog.codes()
        self.assertEqual(codes, ("A", "B"))
        self.assertIsInstance(codes, tuple)
        self.assertIn("A", codes)
        self.assertNotIn("C", codes)
        self.assertTrue(codes)
        self.assertFalse(catalog.Catalog({}).codes())

    def test_invalid_codes(self):
        for code in [True, 7, None]:
            with self.subTest(code=code):
                self.assertRaises(TypeError, self.catalog.canonical_code, code)
        for code in ["", "  "]:
            with self.subTest(code=code):
                with self.assertRaises(ValueError):
                    self.catalog.canonical_code(code)

    def test_missing_item_attributes_cause_and_message(self):
        with self.assertRaises(catalog.UnknownItem) as caught:
            self.catalog.quote(" absent ", 1)
        self.assertEqual(caught.exception.code, "ABSENT")
        self.assertEqual(str(caught.exception), "unknown item: ABSENT")
        self.assertEqual(caught.exception.args, ("unknown item: ABSENT",))
        self.assertIsInstance(caught.exception.__cause__, KeyError)
        self.assertEqual(self.catalog.codes(), ("A", "B"))

    def test_quantity_validation_precedes_lookup(self):
        with self.assertRaises(ValueError):
            self.catalog.quote("ABSENT", 0)

    def test_prices_reject_types_nonpositive_and_collisions(self):
        for price in [True, 1.0, "7"]:
            with self.subTest(price=price):
                self.assertRaises(TypeError, catalog.Catalog, {"A": price})
        for price in [0, -1]:
            with self.subTest(price=price):
                self.assertRaises(ValueError, catalog.Catalog, {"A": price})
        self.assertRaises(ValueError, catalog.Catalog, {"A": 7, " a ": 9})

    def test_caller_mutation_does_not_change_catalog(self):
        self.source[" a "] = 999
        self.assertEqual(self.catalog.quote("A"), 7)

    def test_alternate_constructor_preserves_subclass(self):
        class SpecialCatalog(catalog.Catalog):
            pass
        created = SpecialCatalog.from_pairs([("A", 7)])
        self.assertIs(type(created), SpecialCatalog)
        self.assertEqual(created.quote("A", 2), 14)
        self.assertEqual(created.category, "synthetic-token-catalog")

    def test_ordering_and_explicit_float_tolerance(self):
        low, high = self.catalog.quote("A"), self.catalog.quote("A", 5)
        self.assertGreater(high, low)
        self.assertLess(low, high)
        self.assertAlmostEqual(low / high, 0.2, delta=1e-12)


class MechanismTests(unittest.TestCase):
    def test_function_decorator_order_metadata_and_unwrap(self):
        events = []

        @catalog.traced("outer", events)
        @catalog.traced("inner", events)
        def double(value):
            """Return twice the original input."""
            events.append("body")
            return value * 2

        self.assertEqual(events, ["decorate:inner", "decorate:outer"])
        self.assertEqual(double(4), 8)
        self.assertEqual(events[2:], ["enter:outer", "enter:inner", "body",
                                     "exit:inner", "exit:outer"])
        self.assertEqual(double.__name__, "double")
        self.assertEqual(double.__doc__, "Return twice the original input.")
        self.assertEqual(double.__wrapped__.__wrapped__(3), 6)

    def test_wrapper_finally_preserves_same_exception(self):
        events = []
        failure = ValueError("synthetic body failure")

        @catalog.traced("one", events)
        def fail():
            raise failure

        with self.assertRaises(ValueError) as caught:
            fail()
        self.assertIs(caught.exception, failure)
        self.assertEqual(events, ["decorate:one", "enter:one", "exit:one"])

    def test_class_decorator_retains_identity(self):
        class Original:
            pass
        self.assertIs(catalog.teaching_model(Original), Original)
        self.assertEqual(Original.category, "synthetic-token-catalog")

    def test_class_context_normal_exit(self):
        events = []
        resource = catalog.Lease(events)
        with resource as entered:
            self.assertIs(entered, resource)
            self.assertFalse(resource.closed)
        self.assertTrue(resource.closed)
        self.assertEqual(events, ["enter", "exit:ok"])

    def test_context_propagates_same_body_exception(self):
        events = []
        resource = catalog.Lease(events)
        failure = LookupError("original body failure")
        with self.assertRaises(LookupError) as caught:
            with resource:
                raise failure
        self.assertIs(caught.exception, failure)
        self.assertTrue(resource.closed)
        self.assertEqual(events, ["enter", "exit:LookupError"])

    def test_entry_failure_has_own_cleanup_without_exit(self):
        events = []
        resource = catalog.Lease(events, fail_enter=True)
        with self.assertRaises(RuntimeError):
            with resource:
                self.fail("body must not execute")
        self.assertTrue(resource.closed)
        self.assertEqual(events, ["enter", "entry-cleanup"])

    def test_generator_context_cleanup_and_propagation(self):
        for fails in [False, True]:
            with self.subTest(fails=fails):
                events = []
                try:
                    with catalog.owned_lease(events) as resource:
                        self.assertFalse(resource.closed)
                        if fails:
                            raise ValueError("original failure")
                except ValueError as error:
                    self.assertTrue(fails)
                    self.assertEqual(str(error), "original failure")
                else:
                    self.assertFalse(fails)
                self.assertTrue(resource.closed)
                self.assertEqual(events, ["generator-cleanup"])


class ServiceTests(unittest.TestCase):
    def setUp(self):
        self.catalog = catalog.Catalog({"A": 7})

    def test_owned_file_mock_context_and_restore(self):
        original = service.open_text
        opener = mock_open(read_data='{"A": 7}')
        with patch("service.open_text", opener):
            result = service.load_catalog("synthetic.json")
        self.assertIs(service.open_text, original)
        self.assertEqual(result.quote("A", 2), 14)
        opener.assert_called_once_with("synthetic.json", encoding="utf-8")
        opener.return_value.__exit__.assert_called_once_with(None, None, None)

    def test_malformed_json_exits_context_and_propagates(self):
        opener = mock_open(read_data="{")
        with patch("service.open_text", opener):
            with self.assertRaises(json.JSONDecodeError) as caught:
                service.load_catalog("synthetic.json")
        args = opener.return_value.__exit__.call_args.args
        self.assertIs(args[0], json.JSONDecodeError)
        self.assertIs(args[1], caught.exception)

    def test_wrong_json_shape_rejected(self):
        with patch("service.open_text", mock_open(read_data="[]")):
            self.assertRaises(TypeError, service.load_catalog, "unused.json")

    def test_open_failure_propagates_without_real_file(self):
        failure = OSError("original file failure")
        with patch("service.open_text", side_effect=failure):
            with self.assertRaises(OSError) as caught:
                service.load_catalog("unused.json")
        self.assertIs(caught.exception, failure)

    def test_magicmock_context_protocol(self):
        manager = MagicMock(spec_set=["__enter__", "__exit__"])
        manager.__enter__.return_value = self.catalog
        manager.__exit__.return_value = False
        with manager as entered:
            amount = entered.quote("A", 3)
        self.assertEqual(amount, 21)
        manager.__enter__.assert_called_once_with()
        manager.__exit__.assert_called_once_with(None, None, None)

    def test_post_contract_clock_lookup_and_restore(self):
        original = service.monotonic
        client = create_autospec(service.QuoteClient, instance=True,
                                 spec_set=True)
        with patch("service.monotonic", return_value=42.5) as clock:
            result = service.publish(self.catalog, " a ", 2, client)
            clock.assert_called_once_with()
        self.assertIs(service.monotonic, original)
        self.assertEqual(result, {"code": "A", "quantity": 2,
                                  "tokens": 14, "clock": 42.5})
        client.post.assert_called_once_with(result, timeout=1.0)
        with self.assertRaises(TypeError):
            client.post(result)
        with self.assertRaises(AttributeError):
            client.pots

    def test_invalid_quote_has_no_clock_or_client_side_effect(self):
        client = create_autospec(service.QuoteClient, instance=True)
        with patch("service.monotonic") as clock:
            with self.assertRaises(catalog.UnknownItem):
                service.publish(self.catalog, "MISSING", 1, client)
            clock.assert_not_called()
        client.post.assert_not_called()

    def test_client_exception_propagates_without_retry(self):
        client = create_autospec(service.QuoteClient, instance=True)
        failure = TimeoutError("synthetic post timeout")
        client.post.side_effect = failure
        with patch("service.monotonic", return_value=1):
            with self.assertRaises(TimeoutError) as caught:
                service.publish(self.catalog, "A", 1, client)
        self.assertIs(caught.exception, failure)
        self.assertEqual(client.post.call_count, 1)


if __name__ == "__main__":
    unittest.main()
```

### probes.py

```python
"""Record original PCAT framework, TDD and coverage experiments.

Expected inner-suite failures are inspected, not concealed as passing tests.
Run with existing coverage.py; temporary modules stay under this directory.
"""

from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import platform
import sys
from tempfile import TemporaryDirectory
from types import ModuleType
import unittest

import coverage


CHECKS = []


def check(condition, label):
    """Keep verification active even in optimized Python."""
    if not condition:
        raise AssertionError(label)
    CHECKS.append(label)


def run_suite(suite):
    """Return an explicit inner result without printing expected failures."""
    result = unittest.TestResult()
    suite.run(result)
    return result


def summarize(result):
    """Record counts and full diagnostics with a portable workbook path."""
    def diagnostic(text):
        return text.strip().replace(str(Path(__file__).resolve()), "probes.py")

    return {"tests_run": result.testsRun, "successful": result.wasSuccessful(),
            "failures": [diagnostic(text) for _, text in result.failures],
            "errors": [diagnostic(text) for _, text in result.errors],
            "skipped": [reason for _, reason in result.skipped],
            "expected_failures": len(result.expectedFailures),
            "unexpected_successes": len(result.unexpectedSuccesses)}


def fixture_lifecycle():
    """Observe grouped module/class/method setup and LIFO cleanup."""
    events = []
    name = "_original_pcat_fixture_probe"
    check(name not in sys.modules, "fixture module name is unused")
    module = ModuleType(name)

    def module_setup():
        events.append("module.setup")
        unittest.addModuleCleanup(events.append, "module.cleanup")

    def module_teardown():
        events.append("module.teardown")

    module.setUpModule = module_setup
    module.tearDownModule = module_teardown

    class FixtureTests(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            events.append("class.setup")
            cls.addClassCleanup(events.append, "class.cleanup")

        @classmethod
        def tearDownClass(cls):
            events.append("class.teardown")

        def setUp(self):
            events.append("setup:" + self._testMethodName)
            self.values = []
            self.addCleanup(events.append, "cleanup:" + self._testMethodName)

        def tearDown(self):
            events.append("teardown:" + self._testMethodName)

        def test_a(self):
            events.append("test_a")
            self.assertEqual(self.values, [])
            self.values.append(7)

        def test_b(self):
            events.append("test_b")
            self.assertEqual(self.values, [])

    FixtureTests.__module__ = name
    sys.modules[name] = module
    try:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(FixtureTests)
        result = run_suite(suite)
    finally:
        del sys.modules[name]
    expected = ["module.setup", "class.setup", "setup:test_a", "test_a",
                "teardown:test_a", "cleanup:test_a", "setup:test_b", "test_b",
                "teardown:test_b", "cleanup:test_b", "class.teardown",
                "class.cleanup", "module.teardown", "module.cleanup"]
    check(result.wasSuccessful() and result.testsRun == 2,
          "two grouped fixture tests pass with fresh method state")
    check(events == expected, "module/class/method trace matches oracle")
    check(name not in sys.modules, "temporary module registration restored")
    return {"result": summarize(result), "events": events}


def failed_setup():
    """Prove cleanup runs even when method setup never reaches the body."""
    events = []

    class BrokenSetup(unittest.TestCase):
        def setUp(self):
            events.append("setup")
            self.addCleanup(events.append, "cleanup:first")
            self.addCleanup(events.append, "cleanup:second")
            raise RuntimeError("original setup failure")

        def tearDown(self):
            events.append("teardown")

        def test_body(self):
            events.append("body")

    result = run_suite(unittest.TestSuite([BrokenSetup("test_body")]))
    check(len(result.errors) == 1 and not result.failures,
          "setup failure is one error, not a body assertion failure")
    check(not result.wasSuccessful(), "failed setup cannot be reported green")
    check(events == ["setup", "cleanup:second", "cleanup:first"],
          "failed setup skips body/teardown but performs LIFO cleanup")
    return {"result": summarize(result), "events": events}


def marking_results():
    """Distinguish justified demonstration skips, xfail and unexpected pass."""
    events = []

    class Marked(unittest.TestCase):
        def setUp(self):
            events.append("setup:" + self._testMethodName)

        @unittest.skip("Original demonstration: external service not provided")
        def test_external(self):
            events.append("external-body")

        @unittest.skipIf(True, "Original example: optional adapter absent")
        def test_optional(self):
            events.append("optional-body")

        @unittest.expectedFailure
        def test_known_boundary_defect(self):
            events.append("known-body")
            # Original contract accepts 5; this seeded expression rejects it.
            self.assertTrue(1 <= 5 < 5)

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Marked)
    result = run_suite(suite)
    check(result.testsRun == 3 and len(result.skipped) == 2
          and len(result.expectedFailures) == 1, "skip/xfail counts explicit")
    check(result.wasSuccessful(), "xfail and skips allow successful result")
    check(events == ["setup:test_known_boundary_defect", "known-body"],
          "decorated skips do not execute setup or body")

    class Repaired(unittest.TestCase):
        @unittest.expectedFailure
        def test_now_passes(self):
            self.assertTrue(1 <= 5 <= 5)

    surprise = run_suite(unittest.TestSuite([Repaired("test_now_passes")]))
    check(len(surprise.unexpectedSuccesses) == 1,
          "repaired behavior exposes obsolete expectedFailure marker")
    check(not surprise.wasSuccessful(), "unexpected success makes result fail")

    class BadFixture(unittest.TestCase):
        def setUp(self):
            raise RuntimeError("original fixture error")

        @unittest.expectedFailure
        def test_not_reached(self):
            self.fail("not reached")

    fixture_suite = unittest.TestSuite([BadFixture("test_not_reached")])
    fixture = run_suite(fixture_suite)
    check(len(fixture.errors) == 1 and not fixture.expectedFailures,
          "expectedFailure does not absorb setup errors")
    return {"marked": summarize(result), "events": events,
            "obsolete_marker": summarize(surprise),
            "fixture_error": summarize(fixture),
            "removal": "Provide adapter; repair defect and remove marker."}


def selection_and_order():
    """Show why a selected green test cannot establish full-suite isolation."""
    class Shared(unittest.TestCase):
        values = []

        def test_a_mutates(self):
            self.values.append(7)
            self.assertEqual(self.values, [7])

        def test_b_requires_empty(self):
            self.assertEqual(self.values, [])

    loader = unittest.TestLoader()
    loader.testNamePatterns = ["*requires_empty"]
    selected = run_suite(loader.loadTestsFromTestCase(Shared))
    check(selected.testsRun == 1 and selected.wasSuccessful(),
          "selected empty-state case passes alone")
    Shared.values = []
    full_suite = unittest.defaultTestLoader.loadTestsFromTestCase(Shared)
    together = run_suite(full_suite)
    check(together.testsRun == 2 and len(together.failures) == 1,
          "full suite exposes the original shared-state defect")
    check(not together.errors, "order defect is assertion mismatch, not error")
    Shared.values = []
    reversed_order = run_suite(unittest.TestSuite([
        Shared("test_b_requires_empty"), Shared("test_a_mutates")]))
    check(reversed_order.wasSuccessful(), "reverse order hides same defect")

    class Isolated(Shared):
        def setUp(self):
            self.values = []

    repaired_suite = unittest.defaultTestLoader.loadTestsFromTestCase(Isolated)
    repaired = run_suite(repaired_suite)
    check(repaired.testsRun == 2 and repaired.wasSuccessful(),
          "method fixture removes shared-state contamination")
    Shared.values = []
    return {"selected": summarize(selected), "together": summarize(together),
            "reversed": summarize(reversed_order),
            "isolated": summarize(repaired)}


def load_original(path, name, body):
    """Load one locally authored module, never input from a user or network."""
    path.write_text(body, encoding="utf-8")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def tdd(folder):
    """Execute actual red, green and refactor stages against fixed oracles."""
    prefix = '''def chunks(values, size):
    if type(values) is not list:
        raise TypeError("values must be a list")
    if type(size) is not int:
        raise TypeError("size must be an exact int")
    if size <= 0:
        raise ValueError("size must be positive")
'''
    bodies = {
        "red": prefix + '    return [values[:]] if values else []\n',
        "green": prefix + '''    result = []
    start = 0
    while start < len(values):
        result.append(values[start:start + size])
        start += size
    return result
''',
        "refactor": prefix + '''    return [values[i:i + size]
            for i in range(0, len(values), size)]
'''}
    reports = {}
    for phase, source in bodies.items():
        module = load_original(folder / (phase + ".py"), phase, source)

        class ChunkTests(unittest.TestCase):
            def test_structural_oracles(self):
                cases = [([], 2, []), ([1], 2, [[1]]),
                         ([1, 2, 3], 2, [[1, 2], [3]]),
                         ([1, 2, 3], 1, [[1], [2], [3]]),
                         ([1, 2, 3], 5, [[1, 2, 3]])]
                for values, size, expected in cases:
                    original = values[:]
                    self.assertEqual(module.chunks(values, size), expected)
                    self.assertEqual(values, original)

            def test_bad_sizes(self):
                for size in [0, -1]:
                    self.assertRaises(ValueError, module.chunks, [1], size)
                for size in [True, 1.5, "2"]:
                    self.assertRaises(TypeError, module.chunks, [1], size)

            def test_bad_container(self):
                self.assertRaises(TypeError, module.chunks, "123", 2)

        result = run_suite(
            unittest.defaultTestLoader.loadTestsFromTestCase(ChunkTests))
        check(result.testsRun == 3 and not result.errors,
              phase + " runs the intended three tests without errors")
        if phase == "red":
            check(len(result.failures) == 1 and not result.wasSuccessful(),
                  "red fails the missing chunk-boundary behavior")
            check("Lists differ" in result.failures[0][1],
                  "red is the expected value mismatch, not unrelated failure")
        else:
            check(result.wasSuccessful(), phase + " satisfies fixed oracles")
        reports[phase] = {"result": summarize(result), "source": source,
                          "sha256": sha256(source.encode()).hexdigest()}
    return {"phases": reports,
            "given_when_then": "Given [1,2,3], when grouped by 2, then "
                               "[[1,2],[3]] with input unchanged.",
            "limit": "One original slice; no BDD framework or team workshop."}


def coverage_boundary(folder):
    """Measure full branch coverage that still misses a boundary defect."""
    source = '''"""Original contract: accept exact integers 1 through 5."""


def allowed(quantity):
    if 1 <= quantity < 5:
        return True
    return False
'''
    path = folder / "coverage_boundary.py"
    monitor = coverage.Coverage(data_file=None, config_file=False,
                                branch=True, include=[str(path)])
    monitor.start()
    try:
        module = load_original(path, "coverage_boundary", source)
        observed = [module.allowed(value) for value in [0, 1]]
    finally:
        monitor.stop()
    check(observed == [False, True], "selected original coverage oracles pass")
    target = folder / "coverage.json"
    monitor.json_report(morfs=[str(path)], outfile=str(target))
    report = json.loads(target.read_text(encoding="utf-8"))
    check(len(report["files"]) == 1, "only original boundary module measured")
    detail = next(iter(report["files"].values()))
    summary = detail["summary"]
    check(summary["missing_lines"] == 0
          and summary["covered_branches"] == summary["num_branches"] == 2,
          "both branches and all statements ran despite boundary omission")
    actual = module.allowed(5)
    check(actual is False, "independent boundary5 oracle exposes defect")
    return {"source": source, "sha256": sha256(source.encode()).hexdigest(),
            "summary": summary, "measured_inputs": [0, 1],
            "outputs": observed, "later_boundary_check": {
                "input": 5, "expected": True, "actual": actual},
            "limit": "Small integer examples; no type-policy/whole-app proof."}


def main():
    root = Path(__file__).resolve().parent
    with TemporaryDirectory(prefix="pcat-probe-", dir=root) as temporary:
        folder = Path(temporary).resolve()
        check(folder.is_relative_to(root), "temporary path stays in workbook")
        report = {"python": platform.python_version(),
                  "coverage": coverage.__version__,
                  "fixtures": fixture_lifecycle(),
                  "setup_error": failed_setup(),
                  "markers": marking_results(),
                  "selection_order": selection_and_order(),
                  "tdd": tdd(folder),
                  "coverage_boundary": coverage_boundary(folder)}
    check(not folder.exists(), "temporary modules/reports removed")
    report["passed_checks"] = len(CHECKS)
    report["checks"] = CHECKS
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
```

## Practical labs

1. Build a layered test plan and pyramid for a three-module application.
2. Measure line/branch coverage, then demonstrate high coverage with a missing boundary assertion.
3. Refactor duplicated validation through five individually green changes.
4. Write a custom context manager and verify cleanup on success and exception.
5. Implement function/class decorators and prove stacking order.
6. Create a discoverable `TestCase` suite using every named specialized assertion.
7. Compare method, class, and module fixtures and expose an order-dependent shared mutation.
8. Parameterize boundary cases with `subTest`.
9. Mark one justified skip and expected failure, then document their removal conditions.
10. Mock time, filesystem, and HTTP collaborators; patch each where looked up and prove restoration.
11. Test an exception's type, attributes, and propagation.
12. Implement one feature via red-green-refactor and express its stakeholder behavior as Given/When/Then.

The workbook executes components of these 12 labs. The complete layered plan, five individually reviewed refactor changes, real filesystem/HTTP integration, independent inspection, course/plugin work and stakeholder BDD discussion remain learner tasks. No complete-lab count or human readiness approval is claimed. The fake client and mocked file are explicitly isolated examples.

## Original knowledge checks

1. Why does high coverage not imply strong tests?
2. What makes an automated test a poor candidate?
3. What behavior must refactoring preserve?
4. How does framework assertion differ from language `assert`?
5. In what order do stacked decorators apply?
6. When use a class method rather than static method?
7. How does FIRST independence affect fixture design?
8. Why is `assertAlmostEqual` preferable for some numeric results?
9. What risk comes from a shared mutable class fixture?
10. What does `subTest` add to parameterized iterations?
11. When is `expectedFailure` different from `skip`?
12. Why patch where a name is looked up?
13. When is `MagicMock` appropriate?
14. What should an exception-path test verify beyond type?
15. Why must TDD's red phase fail for the expected reason?
16. What makes Given/When/Then useful to non-developers?
17. What official-source issues require checking before booking?

## Answers and reasoning

1. The original wrong upper bound reaches 4/4 statements and 2/2 branches with inputs 0 and 1 but rejects valid boundary 5. Execution counts do not establish important input selection or a correct oracle; record measured files and criteria.
2. Poorly controlled nondeterminism, low repeat value, costly maintenance and subjective judgment can reduce automation's value. Isolate dependencies where appropriate, while retaining separate real integration evidence. A fast fake does not prove provider behavior.
3. Preserve the agreed observable contract, including values, exceptions, side effects and ownership. Characterization may preserve a defect; compare it with requirements. The chunk refactor supports only the stated examples/domain and keeps validation intact.
4. `TestCase` assertion methods are ordinary method calls and remain active under `-O`, as both runs demonstrate. Language `assert` can be removed and must not implement mandatory validation or required side effects. Do not generalize this explanation to every third-party framework's rewritten assertions.
5. Decorator expressions execute at definition time and replacements apply bottom-up. The example records inner then outer application; invocation enters outer then inner, then unwinds inner then outer. `wraps` preserves selected metadata and `__wrapped__`, not all possible behavior.
6. Use a class method when the actual class matters: `SpecialCatalog.from_pairs` constructs a SpecialCatalog through `cls`. Static normalization needs no instance/class state; a quote needs its instance's price table. Class decorators may return the same class or a replacement.
7. Give tests fresh owned state or a reliable reset, and register cleanup when acquiring resources. The observed shared-list suite fails in one order but passes in another; a per-method list removes that demonstrated contamination.
8. It communicates a bounded approximate numeric comparison, but its default is decimal-place rounding of the difference, not relative error or significant digits. Choose an explicit tolerance justified by the domain; use exact equality for integer token prices.
9. A previous mutation can change later expectations and make filtered/reordered results misleading. Class/module setup grouping can also change under custom ordering. Shared fixtures need an appropriate immutable or reliably reset contract.
10. `subTest` labels input cases and lets iterations report distinguishable failures within a method. It does not create separate TestCase methods or automatically fix a weak oracle, bad shared state or incomplete partition choice.
11. A decorator-based skip avoids method setup/body; expected failure executes the body and records its failure/error specially. An unexpected pass makes unittest's result unsuccessful; a setup error is still an error. Report all counts and revisit reasons/markers.
12. Code may already hold an imported alias. Patch `service.monotonic` and `service.open_text`, then verify restoration, because those are the names used by the service. Patching the original definition after import can miss that bound name.
13. Use it when protocol behavior such as context entry/exit matters. Configure return values and suppression deliberately; default magic behavior can mask a missing setup. Autospec restricts interface shape, not real remote semantics.
14. Check contractual message/attributes, cause and exact propagation where relevant, plus cleanup and absence of unintended side effects. The unknown-item test checks canonical code and KeyError cause; the publish failure test verifies a single attempted call and no retry.
15. An unrelated import/setup error cannot show that a test detects the new behavior. The recorded red phase has one list-value mismatch and no errors, followed by green/refactor passes against the same three methods and fixed oracles.
16. It makes preconditions, event and observable result discussable in shared language. Keywords alone do not constitute BDD collaboration. The chunk statement is original illustrative syntax, not a completed stakeholder workshop or executed behave scenario.
17. Active 31-01 versus in-development 31-02, four-block/data-analysis introductory prose versus six-block testing content, Block 2's three-versus-four objective count, and practice/retake wording conflicts require attention. No launch date was found; verify the exact code and entitlement before purchase.

## Readiness checklist

- [ ] I can explain the testing principles, levels, pyramid, coverage limits, and automation economics.
- [ ] I can refactor under tests and correctly apply AAA, DRY, and KISS.
- [ ] I can implement assertions, contexts, decorators, and all method types.
- [ ] I can build a clean `unittest` suite with precise assertions, fixtures, and discovery.
- [ ] I can parameterize, mark/select, mock/patch, and test exception paths without shared-state leakage.
- [ ] I completed one feature with TDD and a stakeholder-readable BDD example.
- [ ] I verified the current PCAT version and source corrections.

## Source and freshness notes

- [Official PCAT syllabus](https://pythoninstitute.org/pcat-exam-syllabus) controls the six-block map but currently contains contradictory introductory text.
- [Official PCAT page](https://pythoninstitute.org/pcat) identifies `31-01` as active and `31-02` in development and says practice tests are in development.
- Generic current [unittest](https://docs.python.org/3/library/unittest.html), [unittest.mock](https://docs.python.org/3/library/unittest.mock.html) and [contextlib](https://docs.python.org/3/library/contextlib.html) were fetched but not reviewed for this pass. The selected pinned Python 3.13 passages linked above supply technical support.
- Nineteen direct receipts contain 16 successful responses and three errors. Indexed canonical syllabus/credential/policy reading is distinguished from direct network health. Selected chapters and hash-verified reused passages are not whole-manual or enrolled-course audits.
- The full PDF, 12 broader labs, real integrations, course/BDD plugins, stakeholder discussion and independent human content/accessibility review remain pending. No readiness approval is implied.

## Places to learn

This is not a complete list and is not intended to be consumed in full. Use the official PT102 outline to select aligned material, maintain your own test suite, and choose targeted resources for gaps.

| Resource | Access | Estimated time |
|---|---|---:|
| [PCAT syllabus](https://pythoninstitute.org/pcat-exam-syllabus) | Public canonical blueprint; documented code/block/count conflicts | Author planning budget: 2–4 hours to map all 34 objectives |
| [Python for Testing 102](https://edube.org/study/pt102) | Free Core lessons/module tests; USD 49 Full/Pro adds interactive work, assessments and diploma; enrolled features require account | Public outline: 30–40 hours, recommended 5–7 hours/week; store instead says six weeks at one hour/day |
| [Python 3.13 unittest](https://docs.python.org/3.13/library/unittest.html) | Public primary reference; selected contracts reviewed | Author planning budget: 8–15 hours with original coding |
| [Python 3.13 unittest.mock](https://docs.python.org/3.13/library/unittest.mock.html) | Public primary reference; selected contracts reviewed | Author planning budget: 6–12 hours with original labs |
| [Test-Driven Development with Python](https://www.obeythetestinggoat.com/) | Author landing advertises free online reading and paid options; landing/blog index read, not book chapters | Author planning budget: 15–30 selected hours; no provider runtime verified |
| [Architecture Patterns with Python](https://www.cosmicpython.com/book/preface.html) | Public author-hosted preface read; broader architecture/TDD context, chapters not audited | Author planning budget: 10–20 selected hours; no provider runtime verified |

PT102 advertises 40+ labs; none of its enrolled exercises was accessed or copied. Its public outline duplicates a module number and repeats unittest wording in a pytest section; use the canonical exam map for scope. The store describes at least 12 months of premium access after redemption and a voucher valid for 12 months after purchase; these are different clocks, and exact entitlement was not tested. The store's practice/discount claim conflicts with the exam FAQ's in-development practice description. Confirm current terms before purchase.

Pytest, pytest-mock, pytest-cov, pytest-html and behave appear in the course outline as broader tooling. The canonical objectives emphasize unittest and BDD concepts; course additions do not silently become new exam objectives. Pytest is installed locally but was not used for this workbook; the four named plugins/BDD package are absent and were not installed. Their exercises remain pending.

The Testing Goat landing includes a dated August 2024 third-edition progress post; that alone does not verify a current edition's complete content or software versions. The Cosmic Python preface describes domain modeling, architectural boundaries and testability for readers with experience of complex Python applications. Neither book's chapters or code were copied into this original workbook. Free reading access does not mean unrestricted redistribution.

Verify the current exam version, course entitlement and practice product before purchase. Author planning budgets are suggestions, not provider runtimes. Avoid recalled-item material.
