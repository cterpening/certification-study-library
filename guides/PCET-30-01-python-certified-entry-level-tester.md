---
exam_code: PCET-30-01
vendor_id: python-institute
official_blueprint: https://pythoninstitute.org/pcet-exam-syllabus
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-30
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-30
---

# PCET-30-01 Certified Entry-Level Tester with Python Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Deep-reviewed September 30, 2026; exact original Python examples executed with recorded limits. The [official PCET syllabus](https://pythoninstitute.org/pcet-exam-syllabus) is authoritative, subject to the documented code inconsistency below.

**Current baseline:** PCET-30-01, active; syllabus last updated December 10, 2024<br>
**Upcoming blueprint change:** none formally announced; the syllabus header/alignment and credential page say `PCET-30-01`, but introductory syllabus prose says `PCET-30-02`, so verify the code before purchase<br>
**Official delivery snapshot:** 35 questions; 45 minutes plus NDA; 75% cumulative passing score; single-/multiple-select and scenario items; TestNow; English and Spanish<br>
**Credential snapshot:** no formal prerequisite; basic Python/testing or ISTQB Foundation-level experience recommended; seven-year validity; USD 69 exam or USD 86 with retake when checked; seven-day wait after a failed attempt<br>

**VERIFY CURRENT:** The complete public [credential page](https://pythoninstitute.org/pcet) still describes the dedicated PCET practice test as in development. The available PT101 course's Pro assessment is a separate description, not proof that this dedicated product has launched. The [PCET policy page](https://pythoninstitute.org/pcet-testing-policies) could not be retrieved; scheduling, voucher and remote-testing procedures beyond the credential page remain unverified. No account, booking, purchase or private practice questions were accessed.

## How to use this guide

Test tiny Python programs from requirements outward: define risk and expected behavior, choose technique/level, design cases, execute and observe, report evidence, and improve the code without changing behavior.

> **About related items:** A `Related item:` callout adds adjacent context; it is not a new exam objective.

## Weighted objective map

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| Core concepts | 6 | 17.1% | Explain why/when testing adds information and how defects become failures |
| Types, levels, processes | 8 | 22.9% | Choose level/type, plan the lifecycle, document cases/results, and isolate dependencies |
| Static, dynamic, refactoring | 10 | 28.6% | Review/analyze code, measure meaningful coverage, and refactor behavior safely |
| Debugging, assertions, techniques | 11 | 31.4% | Diagnose behavior and derive white-, black-, and experience-based tests |

The retained snapshot contains **22 numbered objectives**, grouped 4/6/6/6, while the exam table assigns **35 items**, grouped 6/8/10/11. Objectives and question counts are different measures. Rounded weights total 100%; they are not separate block pass thresholds. All numbered objectives, detailed bullets and the minimum-qualified-candidate profile were read manually after the direct fetch and automated monitor timed out. This does not constitute a successful automated snapshot comparison. The full downloadable PDF was not read.

The publisher's header, alignment and credential page identify **PCET-30-01**, but introductory syllabus prose says **30-02** and refers to data analysis. Objective 1.4 has a data-storage heading over testing-principle content. Preserve the testing objectives and confirm the purchased code; these wording conflicts are unresolved.

## 1. Core testing concepts — 17.1%

Testing evaluates work products to reveal defects, reduce uncertainty, and provide decision evidence. An **error** is a human mistake, a **defect/bug** is a flaw in an artifact, and a **failure** is externally observed incorrect behavior during execution. A defect may never execute; one error may introduce multiple defects.

Testing shows defect presence, not their absence. Exhaustive testing is infeasible except in trivial spaces, so prioritize risk. Test early; expect defects to cluster; revise tests as repeated suites lose discovery power (pesticide paradox); adapt to context; and remember that fixing all known bugs does not help if the product solves the wrong need.

Waterfall concentrates formal execution later; Agile integrates testing within iterations; DevOps automates feedback across delivery/operation. Shift-left brings reviews and tests earlier, but it does not eliminate production observation. Entry/exit criteria define when an activity is ready and sufficient for the decision.

### Requirements, risk and decision evidence

Use these **original teaching requirements**, expressed before the examples. Fees are synthetic tokens, not currency; the lockout is a state-model exercise, not a real authentication service.

| ID | Required observable behavior | Main risk and evidence |
|---|---|---|
| R1 | Quantity is an exact Python `int`, excluding `bool`, in inclusive range 1–10; priority is an exact `bool` | Wrong type or off-by-one acceptance; valid/invalid partitions and boundary oracles |
| R2 | Regular fee is 10 + 2q; priority fee is 20 + 3q | Wrong branch or amount; independently written expected-value tables |
| R3 | Sum fees for an iterable; empty input returns zero; invalid items propagate failure | Skipped/doubled iterations or swallowed failure; zero/one/many and iterator cases |
| R4 | Read a JSON list, validate each quantity and leave the caller-owned stream open | Malformed data or resource ownership error; in-memory file, exception and cleanup checks |
| R5 | Validate before using clock/client; send exactly one receipt with quantity, fee and time; propagate send failure without retry | Unintended side effect or false success; dummy, stub, fake and interaction evidence |
| R6 | Three consecutive failures lock; earlier success resets count; locked attempts cannot unlock; only explicit authorized reset opens | Incorrect history-dependent transition; fresh state and event-sequence assertions |

The `fee` contract rejects subclasses as well as booleans because it deliberately uses exact types. This is a teaching choice, not a universal Python API rule. `total_fees([], priority=...)` returns zero without validating priority because no fee is evaluated; strict validation of that otherwise-unused argument is outside R3. Write this decision down before arguing that a test is missing.

An error such as misreading “inclusive 10” can produce the defect `quantity < 10`; input 10 exposes the failure `False` where `True` is required. A non-executed defect is still a defect. Static review can reveal it before a failure occurs.

For this fixture, wrong fee and lockout transitions merit early attention because they violate its central requirements. A production risk ranking would additionally need impact, likelihood, usage and stakeholder evidence; arbitrary numeric scores are not measured business risk. Entry criteria could require agreed R1–R6, a reproducible runtime, isolated fixtures and expected outcomes. Exit criteria could require selected cases passing, failures triaged, traceability reviewed and outstanding risks accepted by the responsible person. A green suite alone is not that acceptance decision.

Review requirements during planning, cases during implementation and regression evidence during delivery. Waterfall does not forbid early reviews, and Agile does not remove documentation or acceptance decisions. Continuous testing supplies feedback throughout a pipeline; it does not mean exhaustive testing or automatic permission to release. Developers, testers and domain specialists need a shared understanding of the oracle and remaining uncertainty.

## 2. Types, levels, processes, and doubles — 22.9%

Manual testing enables observation, exploration, and human judgment; automation supports repeatability, scale, and frequent regression. Functional tests examine required behavior; non-functional tests examine qualities such as performance, security, accessibility, and usability.

Unit tests isolate small code units; integration tests examine collaborations; system tests examine the assembled product; acceptance tests evaluate stakeholder/business fitness. The test pyramid favors many fast isolated tests, fewer integration tests, and a smaller number of expensive end-to-end tests. It is a strategy heuristic, not an absolute count.

The lifecycle includes planning, design, environment setup, execution, reporting, and closure. A test plan records scope, objectives, risks, resources, and schedule. A scenario states what to evaluate; a case states preconditions, data, steps, expected result, and traceability; a report distinguishes evidence, defects, coverage, risk, and recommendation.

Test doubles replace collaborators: a dummy only fills a parameter; stub returns controlled answers; fake has a lightweight working implementation; spy records use; mock is configured around expected interaction. Choose the least powerful double that communicates the test.

> **Related item:** Interaction-heavy mocks can couple tests to implementation. Prefer observable outcomes unless collaborator interaction is itself the contract.

### Worked case and test-double choices

A scenario is “reject an out-of-range quantity before sending a receipt.” A reproducible case records R1/R5, fresh collaborators, quantity 0, priority False, one `publish_receipt` call, expected `ValueError`, and no collaborator use. The exact test passes plain `object()` dummies: accidentally calling either would produce a different error and fail the expected-exception check. A report records the command, runtime, observed result, requirement, scope and unresolved risk. A test plan additionally defines responsibilities, data/environment, priorities, entry/exit criteria and schedule; a case is not a complete plan.

| Collaborator | Least powerful suitable choice here | What it establishes |
|---|---|---|
| Clock | Fixed-return function stub | Receipt time is controlled without changing the system clock |
| Readable file | `StringIO` working in-memory substitute | JSON behavior and caller ownership, without disk/network dependency |
| Failing reader | Stubbed `read` raising `OSError` | Read failure propagates |
| Receipt client | Working `FakeClient` storing copied flat dictionaries | Observable synthetic receipt state; no delivery occurs |
| Invalid-input collaborators | Dummies that cannot be called | Validation precedes collaborator use |
| Client call under observation | Spy wrapping the fake's real `send` | The call is recorded while fake behavior still runs |
| Declared client interface | `create_autospec(..., spec_set=True)` mock | Expected call shape and missing-attribute detection; no real client behavior |

The roles overlap: `Mock` can implement a stub or spy; the role in a particular test matters more than the class name. Autospec checks a signature, not remote semantics or a complete protocol. Patch the name **where the code under test looks it up**, and restore it afterward. See the selected [Python 3.13 mock documentation](https://docs.python.org/3.13/library/unittest.mock.html).

Use a fresh `Lockout` in `setUp`, specific `TestCase` assertions and `subTest` labels for input tables. Register owned cleanup with `addCleanup`; a fixture that fails partway through setup still needs cleanup of already-acquired resources. Do not close streams owned by callers. Subtests are input cases, not additional test-method counts. Selected [unittest contracts](https://docs.python.org/3.13/library/unittest.html) cover these choices.

These tests provide unit and small in-process collaboration evidence. `StringIO` is not a real filesystem integration test, and a fake client cannot establish API, system or acceptance behavior. A real provider-contract test, assembled-product test and stakeholder acceptance check would require separate scope and fixtures. Performance/security/accessibility/usability claims require corresponding evidence; a fast local run proves none of them. Manual exploration can discover unexpected behavior, while repeatable automated regression preserves known expectations.

## 3. Static/dynamic testing, coverage, and refactoring — 28.6%

Static testing examines artifacts without executing the code: reviews, walkthroughs, inspections, type/style checks, and linters. Dynamic testing executes code and observes behavior. PEP 8 consistency helps review, but style is not correctness.

Line coverage records executed lines; branch coverage records decision outcomes; method/function coverage records invoked units. High coverage cannot prove good assertions, correct requirements, or important input selection. Dead/unreachable code may indicate obsolete logic or untested design.

Refactoring changes internal structure while preserving external behavior. First establish characterizing tests, make one small change, rerun tests, and commit/review. AAA separates Arrange state, Act behavior, and Assert result. DRY reduces duplicated knowledge, while KISS resists unnecessary complexity; blindly deduplicating superficially similar code can create harmful coupling.

### Review, lint and meaningful coverage

An informal review can inspect R1 against the comparison without a process ceremony. An author-led walkthrough explains intent and invites questions; a structured inspection assigns roles, prepares individually, records defects and follows them to resolution. Define a review checklist: requirement traceability, boundaries/types, exception paths, collaborator ownership, state transitions and diagnostic data. Review artifacts include plans and requirements as well as executable code. No independent human inspection has been completed here.

The selected [PEP 8 passage](https://peps.python.org/pep-0008/) recommends 79-character code lines and shorter prose/docstrings; project agreement and readability still matter. The selected lint run checks `E4,E7,E9,F,W,E501` at 79 columns. It is not a complete PEP 8 audit, formatter run, type proof or correctness guarantee.

The syllabus names Pylint and Flake8. Their invocation and output need tool-specific interpretation. The read [Pylint running page](https://pylint.readthedocs.io/en/latest/user_guide/usage/run.html) identifies development documentation (4.2.0-dev0) and bit-coded exit categories: fatal 1, error 2, warning 4, refactor 8, convention 16, usage 32; combinations add bits, so 20 means warning plus convention. The complete public [Flake8 index/quickstart](https://flake8.pycqa.org/en/stable/index.html) identifies 7.4.1 and shows module invocation and select/ignore controls. These observations are not exam-mandated versions. **Neither tool is installed or executed in this review.** The following commands are preparation only for an environment that already has them:

```text
python -m pylint utility.py
python -m flake8 utility.py test_utility.py
```

Existing Ruff 0.16.4 supplies bounded static evidence: an isolated `F401` probe finds an unused `math` import (exit 1), while a wrong token amount passes that same selected rule (exit 0). [Ruff's linter documentation](https://docs.astral.sh/ruff/linter/) distinguishes diagnostics from abnormal execution and warns about fix safety. No automatic fixes or package installations were performed. Triage a finding against its location and rule, decide whether to fix the cause, then rerun the relevant check and behavioral tests; do not suppress a rule merely to obtain green output.

The exact `probes.py` measures an original eight-line module whose contract is 80 tokens for a member and 100 otherwise. Measurement includes the import/definition and calls, targets only that file and adds no exclusions. It uses [coverage.py branch measurement](https://coverage.readthedocs.io/en/latest/branch.html), the selected [API](https://coverage.readthedocs.io/en/latest/api_coverage.html) and [JSON report](https://coverage.readthedocs.io/en/latest/commands/cmd_json.html). Runtime 7.15.4 differs from the current 7.16.2 documentation.

| Run and weak oracle | Statements | Branch destinations | Combined percentage | Observed outputs |
|---|---:|---:|---:|---|
| Member True; check only integer type | 5/5 = 100% | 1/2 = 50% | 6/7 ≈ 85.71% | 80 |
| False and True; check only integer type | 5/5 = 100% | 2/2 = 100% | 100% | 100, 80 |
| Deliberately change 80 to 81; same two inputs/type checks | 5/5 = 100% | 2/2 = 100% | 100% | 100, 81 |

The first run misses the false branch arc from line 6 to line 8 even though every executable statement ran. The strong, independently written expected values `[100, 80]` catch the mutant's 81. This intentional demonstration failure is expected evidence, not a failing repository test. It shows a specific weak oracle's limit; it is not a general mutation score or production coverage measurement. Function invocation counts alone would also miss this wrong result. Exclusions change denominators, and coverage must name its measured files and criteria.

Statement coverage is weaker than branch coverage in this example. Branch coverage still does not enumerate every combination of decisions, possible loop count or path. Loops and state histories can make full path enumeration unbounded. Exercise zero/one/many iterations and relevant early failures, and combine structure-based evidence with requirements-based oracles.

For a small refactor, `probes.py` changes duplicate base/rate arithmetic into a selected `(base, rate)` pair. Both representations are checked against a handwritten 20-value table for quantities 1–10 and both priorities. This exhausts **that finite valid domain**, not invalid inputs or arbitrary programs. Characterization records existing behavior, including possible defects; compare it with requirements before preserving it. Keep the validation boundary intact, make a small change, verify observable behavior and review the difference. Avoid merging unrelated business concepts just because their present arithmetic matches.

## 4. Debugging, assertions, and test techniques — 31.4%

Debugging localizes and fixes a known failure; testing discovers and evaluates behavior. Print tracing is quick but noisy; a debugger uses breakpoints, stepping, watches, and stack inspection. Reproduce first, minimize the failing case, form a hypothesis, gather evidence, fix the cause, and add a regression test.

Python `assert` documents/checks internal assumptions but can be removed under optimized execution. Use explicit validation for security, input, and business rules. Logging creates durable context: DEBUG detail, INFO normal milestones, WARNING recoverable concern, ERROR failed operation, CRITICAL severe/system-level failure. Avoid sensitive values.

White-box techniques use internal structure: statement, branch, path, and loop testing. Full path coverage is usually impossible. Black-box techniques derive from behavior: equivalence partitioning, boundary-value analysis, decision tables, and state transitions. Experience-based techniques include error guessing, exploratory testing, and checklists. Combine them because each reveals different risk.

### Boundary, decision and state evidence

For exact integer quantities, choose valid partition 1–10, invalid partitions below 1 and above 10, and separate type partitions. Representative boundaries are **0, 1, 2, 9, 10, 11**. Boolean values require attention because `bool` is an `int` subclass; R1 explicitly excludes them. Strings, floats, None and lists do not become valid merely because they resemble a number. Empty input belongs to the collection contract, not to an integer partition. Error guessing suggests malformed JSON, misspelled collaborator methods and failures after partial iteration; each guess needs a concrete oracle.

| Valid integer range? | Priority | Representative input | Expected outcome |
|---|---|---|---|
| No | False | q=0 | `ValueError`, no fee |
| No | True | q=0 | `ValueError`, no fee |
| Yes | False | q=2 | 14 tokens |
| Yes | True | q=2 | 26 tokens |

This four-row decision table covers the selected combinations, not all invalid types or boundary values. Those have separate tests. A decision table expresses combinations of conditions; a state model captures how prior events alter later behavior.

| Current state | Event | Result and next state |
|---|---|---|
| Open, 0 or 1 consecutive failures | Incorrect attempt | Reject; increase failures by one; remain open |
| Open, 2 failures | Incorrect attempt | Reject; failures=3; become locked |
| Open, any permitted failure count | Correct attempt | Accept; failures=0 |
| Locked | Correct or incorrect attempt | Reject; remain locked at failures=3 |
| Any | Authorized reset True | Open; failures=0 |
| Any | Reset False or non-Boolean event | Raise the specified error; preserve state |

The tests exercise the three-failure transition, earlier success, a correct attempt while locked, denied/authorized reset and invalid event types. They do not model timing, concurrent requests, identity stores or production authorization. The `authorized` Boolean is a supplied test event, not an authentication mechanism. A full state-transition coverage claim would require enumerating and executing every intended state/event pair, including locked incorrect attempts; that claim is not made here.

### Reproducible diagnosis and stable validation

The seeded function uses `1 <= quantity < 10`. A print trace records `quantity=10, expected=True, actual=False`. An actual scripted [Python 3.13 pdb](https://docs.python.org/3.13/library/pdb.html) session prints quantity, sets a temporary breakpoint on the return line, continues, prints `accepted`, steps and continues. The transcript observes 10 and False. The hypothesis is an exclusive upper bound; the diagnosis is supported by the expression and state, and the production teaching `fee` already uses inclusive `<= 10` with regression oracles 30/50. The deliberately buggy fixture remains for repeatable diagnosis. This is not an interactive IDE session or a repaired deployed defect.

A useful defect report states the original requirement, exact revision/runtime, minimal input, steps, expected/actual result, transcript and affected boundary. Severity concerns impact; priority concerns scheduling and may differ. Logs or screenshots without reproducible steps do not fully explain a defect.

The [Python 3.13 assert specification](https://docs.python.org/3.13/reference/simple_stmts.html) explains why an `assert` statement cannot enforce mandatory input rules under optimization. An isolated child process rejects 0 with `AssertionError` normally and prints `accepted: 0` with `-O` for the same deliberately unsafe validator. The real utility uses explicit `TypeError`/`ValueError`; `unittest.TestCase` assertion methods and the probe's explicit `raise` checks remain active in optimized runs. Assertions also should not contain required side effects.

The isolated logging probe emits all five standard levels, restores its handler, level and propagation setting, and leaves the root logger unchanged. [Python 3.13 logging](https://docs.python.org/3.13/library/logging.html) defines levels DEBUG=10, INFO=20, WARNING=30, ERROR=40, CRITICAL=50. A logger's effective level and its handlers' levels/filters both matter. Hierarchical propagation can duplicate messages when handlers are attached at multiple points. Use event/context fields that help diagnosis while excluding secrets; these examples contain only synthetic events. Logging is diagnostic evidence, not an assertion that behavior is correct.

For exploratory testing, propose a charter such as “investigate unexpected input and event sequences around R1/R6 for 30 minutes.” Record time, ideas, actions, observations, reproducible findings and follow-up risks, then debrief. Checklists remind the tester about known risks; exploration adapts to new observations. **No timed exploratory session or human debrief was conducted here.**

## Exact original executable workbook

Save the three following blocks as the named files in one directory. The utility and its 25 test methods use the standard library. `probes.py` additionally requires existing coverage.py and Ruff; this review used CPython 3.13.14, coverage.py 7.15.4 and Ruff 0.16.4. No dependencies were installed. Run from that directory:

```text
python -B -Werror -m unittest -v test_utility
python -B -Werror -O -m unittest -v test_utility
python -B -Werror probes.py
python -B -Werror -O probes.py
python -m ruff check utility.py test_utility.py probes.py --select E4,E7,E9,F,W,E501 --line-length 79
```

Exact extracted files are compared with the executed sources. The recorded runs pass **25 test methods in each mode and 55 probe checks in each mode**, with selected lint passing. Subtests do not inflate the method count. Temporary original modules/JSON reports are created only beneath the workbook directory and removed; no persistent coverage database, external API, real login or delivery service is used. The probe's JSON records the intentional mutant and debugger failures along with the successful checks that detect them. Reusing this workbook alone does not complete all ten broader labs.

### utility.py

```python
"""Provide original, synthetic PCET requirements for testing exercises.

Fees are teaching tokens, not currency. No real login, network call,
account or payment is implemented. Streams and clients are caller-owned.
"""

import json
import logging


LOGGER = logging.getLogger(__name__)


def fee(quantity, priority=False):
    """Price 1..10 integer items: regular 10+2q, priority 20+3q tokens.

    Reject booleans/non-int quantities and non-bool priority with TypeError;
    reject integers outside the inclusive range with ValueError.
    """
    if type(quantity) is not int:
        raise TypeError("quantity must be an int, not bool")
    if type(priority) is not bool:
        raise TypeError("priority must be bool")
    if not 1 <= quantity <= 10:
        raise ValueError("quantity must be in 1..10")
    if priority:
        return 20 + 3 * quantity
    return 10 + 2 * quantity


def total_fees(quantities, priority=False):
    """Return the sum for an iterable; empty input returns zero tokens."""
    total = 0
    for quantity in quantities:
        total += fee(quantity, priority)
    return total


def read_quantities(reader):
    """Read a JSON list from a caller-owned stream and validate its items."""
    values = json.load(reader)
    if not isinstance(values, list):
        raise TypeError("expected a JSON list")
    for value in values:
        fee(value)
    return values


def publish_receipt(quantity, priority, clock, client):
    """Send one synthetic receipt using injected clock and client objects.

    Validate the fee before calling either collaborator. Propagate a client
    exception without retrying; a send failure is not a successful receipt.
    """
    amount = fee(quantity, priority)
    payload = {"quantity": quantity, "fee": amount, "time": clock()}
    client.send(payload)
    return payload


class ReceiptClient:
    """Declare the one-method contract used by a test double."""

    def send(self, payload):
        """Accept one receipt; concrete collaborators define delivery."""
        raise NotImplementedError


class Lockout:
    """Model a toy three-failure lockout, not a production auth control.

    A success before lockout resets consecutive failures. Once locked,
    attempts cannot unlock the state. An explicit authorized reset can.
    """

    def __init__(self):
        self.failures = 0
        self.locked = False

    def attempt(self, correct):
        """Return acceptance for a Boolean simulated credential outcome."""
        if type(correct) is not bool:
            raise TypeError("correct must be bool")
        if self.locked:
            LOGGER.info("attempt blocked; state=locked")
            return False
        if correct:
            self.failures = 0
            LOGGER.info("attempt accepted; failures=0")
            return True
        self.failures += 1
        if self.failures == 3:
            self.locked = True
        LOGGER.info("attempt rejected; failures=%d", self.failures)
        return False

    def reset(self, authorized):
        """Reset state only for explicit True; reject other inputs."""
        if type(authorized) is not bool:
            raise TypeError("authorized must be bool")
        if not authorized:
            raise PermissionError("reset denied")
        self.failures = 0
        self.locked = False

```

### test_utility.py

```python
"""Test original PCET requirements with explicit expected outcomes.

Run python -B -Werror -m unittest -v test_utility. These TestCase assertions
remain active under -O. Subtests are input cases, not separate test methods.
"""

from io import StringIO
import json
import unittest
from unittest.mock import Mock, create_autospec, patch

import utility


class FakeClient(utility.ReceiptClient):
    """Keep shallow copies of flat receipts in memory, without delivery."""

    def __init__(self):
        self.receipts = []

    def send(self, payload):
        self.receipts.append(dict(payload))


class FeeTests(unittest.TestCase):
    def test_regular_boundaries(self):
        for quantity, expected in [(1, 12), (2, 14), (9, 28), (10, 30)]:
            with self.subTest(quantity=quantity):
                self.assertEqual(utility.fee(quantity), expected)

    def test_priority_boundaries(self):
        for quantity, expected in [(1, 23), (2, 26), (9, 47), (10, 50)]:
            with self.subTest(quantity=quantity):
                self.assertEqual(utility.fee(quantity, True), expected)

    def test_outside_partitions(self):
        for quantity in [-100, 0, 11, 100]:
            with self.subTest(quantity=quantity):
                with self.assertRaisesRegex(ValueError, r"1\.\.10"):
                    utility.fee(quantity)

    def test_wrong_quantity_types(self):
        for quantity in [True, False, 1.0, "1", None, []]:
            with self.subTest(quantity=quantity):
                with self.assertRaises(TypeError):
                    utility.fee(quantity)

    def test_priority_is_boolean(self):
        for priority in [0, 1, "yes", None]:
            with self.subTest(priority=priority):
                with self.assertRaises(TypeError):
                    utility.fee(1, priority)

    def test_zero_one_many_loop_iterations(self):
        for values, expected in [([], 0), ([1], 12), ([1, 2, 10], 56)]:
            with self.subTest(values=values):
                self.assertEqual(utility.total_fees(values), expected)
        self.assertEqual(utility.total_fees(iter([1, 10]), True), 73)

    def test_invalid_item_propagates(self):
        with self.assertRaises(ValueError):
            utility.total_fees([1, 0, 2])

    def test_validity_priority_decision_table(self):
        rows = [(0, False, None), (0, True, None),
                (2, False, 14), (2, True, 26)]
        for quantity, priority, expected in rows:
            with self.subTest(quantity=quantity, priority=priority):
                if expected is None:
                    with self.assertRaises(ValueError):
                        utility.fee(quantity, priority)
                else:
                    self.assertEqual(utility.fee(quantity, priority), expected)


class StreamTests(unittest.TestCase):
    def test_working_in_memory_file(self):
        stream = StringIO("[1, 2, 10]")
        self.addCleanup(stream.close)
        self.assertEqual(utility.read_quantities(stream), [1, 2, 10])
        self.assertFalse(stream.closed)

    def test_empty_list(self):
        with StringIO("[]") as stream:
            self.assertEqual(utility.read_quantities(stream), [])

    def test_invalid_json_and_shape(self):
        with StringIO("{") as stream:
            with self.assertRaises(json.JSONDecodeError):
                utility.read_quantities(stream)
        with StringIO('{"quantity": 1}') as stream:
            with self.assertRaises(TypeError):
                utility.read_quantities(stream)

    def test_invalid_json_item(self):
        for text, error in [("[0]", ValueError), ("[true]", TypeError)]:
            with self.subTest(text=text), StringIO(text) as stream:
                with self.assertRaises(error):
                    utility.read_quantities(stream)

    def test_reader_failure(self):
        reader = Mock(spec_set=["read"])
        reader.read.side_effect = OSError("synthetic read failure")
        with self.assertRaisesRegex(OSError, "synthetic read failure"):
            utility.read_quantities(reader)


class ReceiptTests(unittest.TestCase):
    def test_stub_clock_and_working_fake(self):
        # Arrange a fixed-time stub and an in-memory working fake.
        client = FakeClient()
        def clock():
            return 123
        # Act once, then assert observable state and the complete contract.
        result = utility.publish_receipt(2, False, clock, client)
        expected = {"quantity": 2, "fee": 14, "time": 123}
        self.assertEqual(result, expected)
        self.assertEqual(client.receipts, [expected])
        result["fee"] = -1
        self.assertEqual(client.receipts[0]["fee"], 14)

    def test_dummy_collaborators_not_used_on_invalid_input(self):
        with self.assertRaises(ValueError):
            utility.publish_receipt(0, False, object(), object())

    def test_spy_wraps_real_fake_operation(self):
        client = FakeClient()
        with patch.object(client, "send", wraps=client.send) as spy:
            result = utility.publish_receipt(1, True, lambda: 9, client)
            spy.assert_called_once_with(result)
        self.assertEqual(len(client.receipts), 1)

    def test_autospec_mock_and_call_contract(self):
        client = create_autospec(utility.ReceiptClient, instance=True,
                                 spec_set=True)
        clock = Mock(return_value=77)
        utility.publish_receipt(10, True, clock, client)
        client.send.assert_called_once_with(
            {"quantity": 10, "fee": 50, "time": 77})
        clock.assert_called_once_with()
        with self.assertRaises(TypeError):
            client.send()
        with self.assertRaises(AttributeError):
            client.sned

    def test_client_failure_is_not_success_or_retry(self):
        client = create_autospec(utility.ReceiptClient, instance=True)
        client.send.side_effect = OSError("synthetic send failure")
        with self.assertRaises(OSError):
            utility.publish_receipt(1, False, lambda: 0, client)
        self.assertEqual(client.send.call_count, 1)

    def test_patch_lookup_and_restore(self):
        original = utility.fee
        with patch("utility.fee", autospec=True, return_value=99) as mock_fee:
            result = utility.publish_receipt(1, False, lambda: 0, FakeClient())
            self.assertEqual(result["fee"], 99)
            mock_fee.assert_called_once_with(1, False)
        self.assertIs(utility.fee, original)
        self.assertEqual(utility.fee(1), 12)


class StateTests(unittest.TestCase):
    def setUp(self):
        self.gate = utility.Lockout()

    def test_three_consecutive_failures_lock(self):
        for count in [1, 2, 3]:
            with self.subTest(count=count):
                self.assertFalse(self.gate.attempt(False))
                self.assertEqual(self.gate.failures, count)
                self.assertEqual(self.gate.locked, count == 3)

    def test_success_before_lock_resets_count(self):
        self.gate.attempt(False)
        self.gate.attempt(False)
        self.assertTrue(self.gate.attempt(True))
        self.assertEqual(self.gate.failures, 0)
        self.assertFalse(self.gate.locked)

    def test_locked_success_cannot_unlock(self):
        for _ in range(3):
            self.gate.attempt(False)
        with self.assertLogs(utility.LOGGER, level="INFO") as captured:
            self.assertFalse(self.gate.attempt(True))
        self.assertEqual(captured.records[0].getMessage(),
                         "attempt blocked; state=locked")
        self.assertTrue(self.gate.locked)
        self.assertEqual(self.gate.failures, 3)

    def test_only_authorized_reset_unlocks(self):
        for _ in range(3):
            self.gate.attempt(False)
        with self.assertRaises(PermissionError):
            self.gate.reset(False)
        self.assertTrue(self.gate.locked)
        self.gate.reset(True)
        self.assertFalse(self.gate.locked)
        self.assertEqual(self.gate.failures, 0)
        self.assertTrue(self.gate.attempt(True))

    def test_wrong_event_types_do_not_mutate(self):
        for event in [None, 0, 1, "yes"]:
            with self.subTest(event=event):
                with self.assertRaises(TypeError):
                    self.gate.attempt(event)
                with self.assertRaises(TypeError):
                    self.gate.reset(event)
                self.assertEqual((self.gate.failures, self.gate.locked),
                                 (0, False))

    def test_new_instance_is_independent(self):
        self.gate.attempt(False)
        other = utility.Lockout()
        self.assertIsNot(other, self.gate)
        self.assertEqual(other.failures, 0)


if __name__ == "__main__":
    unittest.main()
```

### probes.py

```python
"""Demonstrate coverage limits, mutation, refactoring and debugger evidence.

Use existing coverage.py and Ruff packages. Run python -B -Werror probes.py.
Only original temporary modules under this script's directory are created;
they are removed on exit. This prints a JSON report, not a real test verdict
about a production system. Expected demonstration failures are inspected.
"""

from contextlib import redirect_stdout
from hashlib import sha256
import importlib.util
from io import StringIO
import json
import logging
from pathlib import Path
import pdb
import platform
import subprocess
import sys
from tempfile import TemporaryDirectory

import coverage


CHECKS = []
REBATE = '''"""Original contract: 80 tokens for members, 100 for others."""


def rebate(member):
    tokens = 100
    if member:
        tokens = 80
    return tokens
'''
DEBUG_SOURCE = '''"""Original off-by-one defect for a debugger exercise."""


def buggy_quantity(quantity):
    accepted = 1 <= quantity < 10
    return accepted
'''


def check(condition, label):
    """Record a condition without depending on removable assert syntax."""
    if not condition:
        raise AssertionError(label)
    CHECKS.append(label)


def load_module(path, name):
    """Load a fresh original temporary module by its verified local path."""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def measure(folder, name, body, inputs):
    """Measure only one original module, including its import statements."""
    path = folder / (name + ".py")
    path.write_text(body, encoding="utf-8")
    monitor = coverage.Coverage(data_file=None, config_file=False,
                                branch=True, include=[str(path)])
    values = []
    monitor.start()
    try:
        module = load_module(path, name)
        for member in inputs:
            value = module.rebate(member)
            check(type(value) is int, name + " weak type-only assertion")
            values.append(value)
    finally:
        monitor.stop()
    report_path = folder / (name + ".json")
    monitor.json_report(morfs=[str(path)], outfile=str(report_path))
    report = json.loads(report_path.read_text(encoding="utf-8"))
    check(len(report["files"]) == 1, name + " single measured module")
    detail = next(iter(report["files"].values()))
    return {"summary": detail["summary"],
            "executed_lines": detail["executed_lines"],
            "missing_lines": detail["missing_lines"],
            "missing_branches": detail["missing_branches"],
            "values": values,
            "source_sha256": sha256(body.encode()).hexdigest()}


def coverage_limits(folder):
    """Compare weak coverage assertions with a semantic oracle."""
    partial = measure(folder, "partial", REBATE, [True])
    complete = measure(folder, "complete", REBATE, [False, True])
    mutated = REBATE.replace("tokens = 80", "tokens = 81")
    mutant = measure(folder, "mutant", mutated, [False, True])
    for label, result in [("partial", partial), ("complete", complete),
                          ("mutant", mutant)]:
        summary = result["summary"]
        check(summary["missing_lines"] == 0, label + " all statements ran")
        check(summary["num_branches"] == 2, label + " two branch outcomes")
    check(partial["summary"]["covered_branches"] == 1,
          "one branch missing despite full statement coverage")
    check(complete["summary"]["covered_branches"] == 2,
          "both original branch outcomes covered")
    check(mutant["summary"]["covered_branches"] == 2,
          "both mutant branch outcomes covered")
    expected = [100, 80]
    check(complete["values"] == expected, "strong original value oracle")
    failures = [{"member": member, "expected": want, "actual": actual}
                for member, want, actual in zip([False, True], expected,
                                                mutant["values"])
                if want != actual]
    check(failures == [{"member": True, "expected": 80, "actual": 81}],
          "strong oracle kills the deliberately changed mutant")
    return {"one_input_weak_assertion": partial,
            "both_inputs_weak_assertion": complete,
            "mutant_both_inputs_weak_assertion": mutant,
            "strong_oracle_expected_failures": failures,
            "denominator": "This original module only; no added exclusions."}


def refactoring():
    """Compare both representations over the small stated input domain."""
    def before(quantity, priority):
        if priority:
            return 20 + 3 * quantity
        return 10 + 2 * quantity

    def after(quantity, priority):
        base, rate = (20, 3) if priority else (10, 2)
        return base + rate * quantity

    expected = {False: [12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
                True: [23, 26, 29, 32, 35, 38, 41, 44, 47, 50]}
    comparisons = 0
    for priority, values in expected.items():
        for quantity, value in enumerate(values, 1):
            check(before(quantity, priority) == value
                  and after(quantity, priority) == value,
                  f"refactor oracle {quantity} {priority}")
            comparisons += 1
    return {"domain": "int quantity1..10 and bool priority only",
            "comparisons": comparisons,
            "limit": "No claim about invalid inputs or arbitrary refactors."}


def debugging(folder):
    """Capture print tracing and an actual scripted pdb breakpoint session."""
    path = folder / "debug_target.py"
    path.write_text(DEBUG_SOURCE, encoding="utf-8")
    target = load_module(path, "debug_target")
    output = StringIO()
    with redirect_stdout(output):
        print("quantity=10, expected=True, actual=",
              target.buggy_quantity(10), sep="")
    return_line = target.buggy_quantity.__code__.co_firstlineno + 2
    commands = (f"p quantity\ntbreak {return_line}\nc\n"
                "p accepted\nn\nc\n")
    transcript = StringIO()
    prior_trace = sys.gettrace()
    debugger = pdb.Pdb(stdin=StringIO(commands), stdout=transcript,
                       nosigint=True, readrc=False)
    debugger.use_rawinput = False
    actual = debugger.runcall(target.buggy_quantity, 10)
    text = transcript.getvalue().replace(str(folder).lower(), "<temporary>")
    text = text.replace(str(folder), "<temporary>")
    check(actual is False, "debugger reproduces off-by-one defect")
    check("10" in text and "False" in text and "Breakpoint" in text,
          "debugger captured input, breakpoint and wrong state")
    check(sys.gettrace() is prior_trace, "debugger restored tracing state")
    check("expected=True, actual=False" in output.getvalue(),
          "print trace exposes contract failure")
    return {"print_trace": output.getvalue(), "pdb_commands": commands,
            "pdb_transcript": text, "expected": True, "actual": actual,
            "diagnosis": "Upper bound rejects 10; the contract includes it.",
            "limit": "Scripted stdlib pdb, not an interactive IDE session."}


def optimization():
    """Show why mandatory validation must not rely on an assert statement."""
    source = (
        "def validate(q):\n"
        "    assert 1 <= q <= 10\n"
        "    return q\n"
        "try:\n"
        "    print('accepted:', validate(0))\n"
        "except AssertionError:\n"
        "    print('AssertionError')\n"
    )
    rows = []
    for optimized in [False, True]:
        args = [sys.executable, "-B", "-Werror"]
        if optimized:
            args.append("-O")
        result = subprocess.run(args + ["-c", source], capture_output=True,
                                text=True, timeout=10)
        check(result.returncode == 0 and not result.stderr,
              "assert demonstration subprocess completed " + str(optimized))
        rows.append({"optimized": optimized, "stdout": result.stdout.strip()})
    check(rows[0]["stdout"] == "AssertionError", "normal assertion enforces")
    check(rows[1]["stdout"] == "accepted: 0", "optimization removes assertion")
    return {"source": source, "results": rows}


def logging_probe():
    """Capture levels without changing the root logger or leaving handlers."""
    logger = logging.getLogger("pcet.original.probe")
    prior_level, prior_propagate = logger.level, logger.propagate
    prior_handlers = tuple(logger.handlers)
    sink = StringIO()
    handler = logging.StreamHandler(sink)
    handler.setFormatter(logging.Formatter("%(levelname)s:%(message)s"))
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    logger.addHandler(handler)
    try:
        for level in [logging.DEBUG, logging.INFO, logging.WARNING,
                      logging.ERROR, logging.CRITICAL]:
            logger.log(level, "synthetic event %d", level)
        text = sink.getvalue()
    finally:
        logger.removeHandler(handler)
        handler.close()
        logger.setLevel(prior_level)
        logger.propagate = prior_propagate
        sink.close()
    check([v.split(":")[0] for v in text.splitlines()]
          == ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
          "five logging levels captured")
    check(tuple(logger.handlers) == prior_handlers
          and logger.level == prior_level
          and logger.propagate == prior_propagate, "logger settings restored")
    return text


def lint_probe():
    """Triage an unused import; show a wrong value can pass selected lint."""
    bodies = {"unused_import": "import math\n" + REBATE,
              "wrong_value": REBATE.replace("tokens = 80", "tokens = 81")}
    receipts = {}
    args = [sys.executable, "-B", "-Werror", "-m", "ruff", "check",
            "--isolated", "--select", "F401", "--output-format", "json",
            "--stdin-filename", "original_probe.py", "-"]
    for label, source in bodies.items():
        result = subprocess.run(args, input=source, capture_output=True,
                                text=True, timeout=15)
        check(not result.stderr, label + " lint has no tool error")
        diagnostics = json.loads(result.stdout)
        receipts[label] = {"exit_code": result.returncode,
                           "codes": [d["code"] for d in diagnostics]}
    check(receipts["unused_import"] == {"exit_code": 1, "codes": ["F401"]},
          "unused import detected by selected static rule")
    check(receipts["wrong_value"] == {"exit_code": 0, "codes": []},
          "incorrect business value passes selected static rule")
    return {"rule": "F401 only, isolated configuration", "results": receipts,
            "limit": "No Pylint/Flake8 execution or complete style audit."}


def main():
    """Run bounded probes and confirm temporary-directory cleanup."""
    root = Path(__file__).resolve().parent
    with TemporaryDirectory(prefix="pcet-probe-", dir=root) as temporary:
        folder = Path(temporary).resolve()
        check(folder.is_relative_to(root), "temporary path inside workbook")
        report = {"python": platform.python_version(),
                  "coverage": coverage.__version__,
                  "coverage_limits": coverage_limits(folder),
                  "refactoring": refactoring(), "debugging": debugging(folder),
                  "optimization": optimization(), "logging": logging_probe(),
                  "static_analysis": lint_probe()}
    check(not folder.exists(), "temporary modules/reports removed")
    report["checks"] = CHECKS
    report["passed_checks"] = len(CHECKS)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
```

## Practical labs

1. Trace one error into a defect and demonstrate an input that exposes the failure.
2. Write entry/exit criteria and a risk-ranked plan for a four-function Python utility.
3. Classify 20 proposed tests by level, functional/non-functional, and manual/automated suitability.
4. Replace a clock, file reader, and API client with the least powerful suitable test double; explain each choice.
5. Run a review and a linter, triage findings, and show why passing the linter is insufficient.
6. Measure line/branch coverage, add boundary cases, and demonstrate a weak assertion that still yields high coverage.
7. Refactor a duplicated function in small tested steps using AAA, DRY, and KISS.
8. Diagnose a seeded defect using both print tracing and a debugger; compare evidence.
9. Derive equivalence partitions/boundaries, a decision table, and a state model for login lockout.
10. Conduct a 30-minute exploratory session with a charter, notes, and reproducible report.

The workbook executes components of these labs with original synthetic fixtures. The four-function plan, 20-test classification, independent review, named Pylint/Flake8 runs, full IDE exercise, broader lockout exploration and timed session still require learner work. No complete-lab count or human readiness approval is claimed.

## Original knowledge checks

1. Distinguish error, defect, and failure.
2. Why can testing not establish absence of defects?
3. What does the pesticide paradox imply?
4. How does shift-left change cost/feedback?
5. Contrast unit, integration, system, and acceptance testing.
6. Why is the test pyramid a heuristic?
7. Contrast a scenario, case, plan, and report.
8. Distinguish dummy, stub, fake, spy, and mock.
9. Contrast static and dynamic testing.
10. Why can 100% line coverage be weak?
11. What preserves safety during refactoring?
12. When can DRY conflict with good design?
13. Why are assertions unsuitable for mandatory validation?
14. Contrast testing and debugging.
15. Derive boundary values for accepted integers 1 through 10.
16. When use a decision table versus state transitions?
17. What must be checked about the PCET exam code?

## Answers and reasoning

1. An error is a human mistake, a defect is a flaw in an artifact, and a failure is observed incorrect behavior. Misreading inclusive 10 can create `< 10`; executing input 10 then exposes False where True is required. Static review can find the defect before execution.
2. Most input/state spaces are too large to exhaust, requirements can be wrong, and the oracle can be weak. The 20-case refactor probe exhausts only its explicitly finite valid domain; it says nothing about invalid inputs or external systems.
3. Preserve valuable regression tests but add or revise cases as risks, requirements and observed defects change. Repeated green runs of an unchanged suite do not show continuing discovery of new defect classes.
4. Earlier requirement review and rapid local feedback can reduce the distance between introduction and discovery. They complement later system/operational evidence; they do not guarantee a fixed cost reduction or eliminate downstream testing.
5. Unit tests examine small units; integration tests examine real collaborations; system tests examine an assembled product; acceptance tests examine stakeholder fitness. A fake receipt client supports isolated evidence and does not prove a real provider contract or acceptance.
6. The pyramid balances speed, confidence, maintenance cost and architecture. A system with important external contracts may need a different mix. Counting tests without considering their oracles and scope is not a strategy.
7. A scenario states behavior to investigate; a case specifies preconditions, inputs, actions and expected results; a plan defines scope/risk/resources/process; a report records observed evidence and remaining uncertainty. Link all four to requirements.
8. A dummy is unused, a stub supplies controlled answers, a fake has a limited working implementation, a spy records calls while optionally running behavior, and a mock supports configured interaction checks. Choose by test purpose; autospec checks call shape, not real delivery.
9. Static review/lint inspects without executing the target behavior; dynamic testing executes and checks outcomes. Ruff F401 finds the unused import but passes the incorrect 81-token value, which a requirement-derived dynamic oracle catches.
10. The single-input rebate probe executes all five statements but only one of two branches. The two-input mutant reaches 100% statement/branch coverage while returning 81 instead of 80; type-only assertions miss it. Name the denominator and assess the oracle.
11. Establish requirements and characterization, use small changes and independent expected outcomes, rerun relevant tests and review the difference. The 20-value table supports only the stated valid fee domain. Tests cannot generally prove arbitrary refactors safe.
12. Two similar expressions may represent different concepts with different future rules. Consolidate duplicated knowledge when it actually shares a contract; an abstract framework may violate KISS without reducing meaningful risk.
13. `assert` can disappear under `-O`, as the isolated zero-quantity probe demonstrates. Mandatory rules use explicit checks/exceptions. TestCase assertion methods remain active, and production behavior must not rely on assertion side effects.
14. Testing discovers/evaluates behavior and provides evidence; debugging reproduces, localizes and repairs a particular failure. The print/pdb transcript identifies the exclusive upper bound; regression tests then preserve the inclusive requirement.
15. Test 0, 1, 2, 9, 10, 11, plus representative distant invalid integers and separate type partitions such as True, float, text, None and list. Empty input is relevant to a collection contract. Expected outcomes must be explicit, not derived by calling the same implementation twice.
16. Use decision tables for combinations of present conditions, such as validity and priority; use state transitions for history-dependent behavior, such as three failures then a correct attempt while locked. Selected rows/sequences do not automatically imply complete coverage.
17. The credential page, header and alignment say PCET-30-01; introductory syllabus prose says PCET-30-02 and contains unrelated data-analysis wording. Objective 1.4 also has a mismatched heading. Confirm the active purchased code and preserve all 22 testing objectives; do not invent a new version from conflicting prose.

## Readiness checklist

- [ ] I can explain foundational principles, risk, lifecycle, and development-model differences.
- [ ] I can select levels/types/doubles and create traceable documentation.
- [ ] I can combine review, analysis, dynamic execution, coverage, and safe refactoring.
- [ ] I can debug systematically and use assertions/logging appropriately.
- [ ] I can derive white-box, black-box, and experience-based tests from one system.
- [ ] I completed the labs with original code and reports.
- [ ] I verified the active PCET code before purchase.

## Source and freshness notes

- [Official syllabus](https://pythoninstitute.org/pcet-exam-syllabus) controls weights/objectives but contains the documented `30-01`/`30-02` wording conflict and a mislabeled Objective 1.4 heading.
- [Official PCET page](https://pythoninstitute.org/pcet) identifies PCET-30-01 as active and controls delivery details.
- The current generic [unittest](https://docs.python.org/3/library/unittest.html) and [logging](https://docs.python.org/3/library/logging.html) pages were fetched but not reread in full for this review. The explicitly selected Python 3.13 sections linked above support the executed runtime contracts. Successful retrieval is not a whole-manual audit.
- Source evidence contains 21 direct receipts: 16 successful responses, three errors, one blocked book page and one missing Flake8 candidate URL. The current stable Flake8 index was then verified separately. Indexed primary syllabus/exam reading is distinguished from direct network health.
- Pylint/Flake8 execution, full policy/PDF reading, ten broader labs, independent human content/accessibility review and readiness approval remain pending.

## Places to learn

This is not a complete list and is not intended to be consumed in full. Use one testing foundation, write tests for your own Python project, and use practice to find conceptual gaps.

| Resource | Access | Estimated time |
|---|---|---:|
| [PCET syllabus](https://pythoninstitute.org/pcet-exam-syllabus) | Public official blueprint; code/heading conflicts recorded | Author planning budget: 2–3 hours to map all 22 objectives |
| [Python for Testing 101](https://edube.org/study/pt101) | Free Core lessons/module tests; USD 49 Full/Pro adds interactive work, practice assessment and diploma when checked; account required | Provider estimate: four weeks at about one hour/day; provider advertises 38 labs, not independently completed |
| [ISTQB Foundation overview](https://www.istqb.org/certifications/certified-tester-foundation-level) | Public overview and syllabus link; CTFL is a broader, different exam; linked PDF not read here | Author planning budget: 8–15 selected hours; no verified course runtime |
| [Python 3.13 unittest](https://docs.python.org/3.13/library/unittest.html) | Public primary reference; selected contracts reviewed | Author planning budget: 5–10 hours with original coding |
| [Software Testing, 2nd ed.](https://www.oreilly.com/library/view/software-testing-2nd/9780134698298/) | Prior paid-book lead; page automation-blocked and present access/contents unverified | No verified runtime; optional after checking contents and access |

The complete public PT101 outline describes beginner-level testing with basic Python recommended and no formal prerequisite. Free Core and paid interactive features are different entitlements. Its full practice assessment does not establish availability of the separate dedicated PCET practice kit. The complete ISTQB overview identifies CTFL 4.0 and a 4.0.1 syllabus download; its question count, timing and passing rule belong to CTFL and must not replace PCET's rules. Neither enrolled lessons nor linked sample questions were accessed.

Verify exact course availability, entitlement, price, runtime and exam code before purchase. Author budgets are suggestions, not provider runtimes. Avoid products built around recalled certification questions.
