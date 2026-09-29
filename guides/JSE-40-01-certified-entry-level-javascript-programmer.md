---
exam_code: JSE-40-01
vendor_id: js-institute
official_blueprint: https://jsinstitute.org/jse-certification
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# JSE-40-01 Certified Entry-Level JavaScript Programmer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked September 29, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#jse-40-01-coverage-record). The [official JSE exam page and scope](https://jsinstitute.org/jse-certification) are authoritative.

**CURRENT BLUEPRINT — current baseline:** JSE-40-01, active; six-block public scope<br>
**VERIFY CURRENT — upcoming blueprint change:** none announced on the official exam or certification-catalog pages when checked<br>
**VERIFY CURRENT — official delivery snapshot:** 30 single- and multiple-select questions; 40-minute exam plus 5-minute tutorial/NDA; 70% passing score; TestNow; English and Spanish<br>
**VERIFY CURRENT — purchase snapshot:** no formal prerequisite; exam from USD 69, exam-plus-retake from USD 86, and exam-plus-retake-plus-practice from USD 95 when checked; standalone official practice was USD 29<br>

## How to use this guide

JSE tests core language understanding through short-program reasoning. For each topic, predict the value, type, output, branch, changed object, scheduled callback order, or error before using a console. Then run the smallest possible example in a modern browser, explain the result, and change one boundary.

Use this loop:

1. identify the runtime and whether a feature belongs to JavaScript or its host;
2. trace declarations, values, references, control flow, calls, and pending callbacks;
3. execute in an isolated browser page and developer console;
4. use breakpoints and inspect state rather than adding random changes;
5. map the lesson to one of the six official blocks.

The scope explicitly includes browser dialog functions and asynchronous timers, so a browser is the clearest primary lab runtime. Node.js is valuable related context, but it does not provide browser `alert`, `confirm`, or `prompt` globals. DOM frameworks, modules, promises, `async`/`await`, classes, and package tooling should not displace the published entry-level boundary.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map and study emphasis

| Block | Official practice-kit distribution | Evidence of readiness |
|---|---:|---|
| 1. Introduction to JavaScript and Computer Programming | 8% | Distinguish language from runtime and run code in a page and console |
| 2. Variables, Data Types, and Type Casting | 20% | Trace declarations, scope, primitive values, arrays/objects, references, and conversions |
| 3. Operators and User Interaction | 18% | Predict operator results and use browser dialogs with correct return types |
| 4. Control Flow — Conditional Execution and Loops | 21% | Trace every decision and loop, including `for...in` versus `for...of` |
| 5. Functions | 21% | Use calls/returns/scope, first-class functions, recursion, callbacks, timers, and arrows |
| 6. Errors, Exceptions, Debugging, and Troubleshooting | 12% | Classify failures, handle/throw exceptions, and debug reproducibly |

The canonical scope has **30 listed skill bullets**, grouped **3/5/5/5/7/5** under its six blocks; the subsequent certification-holder profile is supporting prose rather than extra scope bullets. The main official scope does not display weights. The percentages above come from the provider's JSE-40-01 Practice Test Kit page, which says its content is organized to those six blocks. Treat them as a study-allocation signal, not proof of individual item counts or scoring values.

The [deep-review record](../docs/research/2026-09-29-jse-40-01-deep-review.md) separates actual execution from proposed activities. The original core workbook passed 114 checks in Chrome 154.0.8037.58 and Node.js 24.18.1; browser scenarios passed 109 additional checks, including 19 real dialog flows handled by automation. Actual Chrome debugger protocol work inspected and changed a paused local variable. No installation, paid lesson completion, account action or human review is claimed. Use a fresh page for each standalone example so bindings and timers from earlier examples do not interfere.

## 1. Introduction to JavaScript and computer programming

### Language, engine, and host

JavaScript source is parsed and executed by an engine inside a host environment. Modern engines commonly combine interpretation and just-in-time compilation; do not reduce real behavior to “JavaScript is only interpreted.” The host supplies capabilities outside the core language. A browser supplies a document, console, dialogs, timers, and Web APIs. Node.js supplies a different server/local runtime and APIs.

Client-side code runs in the user's browser; server-side code runs in a server environment and returns results or resources to clients. The same core syntax can run in either, but a host-specific global may not exist in the other. Always ask two questions: “Is this JavaScript language behavior?” and “Which host provides this function or object?”

For JSE practice, create a minimal HTML file with a `<script>` block or linked `.js` file, and also run expressions directly in browser developer tools. Source order matters. A classic script ordinarily executes when encountered; loading strategies such as modules or `defer` are useful related context but beyond the core objective.

> **Related item:** ECMAScript is the language specification standardized by Ecma International; JavaScript is the widely used implementation name. Browser compatibility and Web APIs are separate from the core standard even when developers use them together.

### From problem to program

Translate a problem into inputs, state, decisions, repetition, functions, output, and error paths. Syntax determines whether tokens form valid code. Semantics determines what valid code means. A correct program also needs the intended result for normal and boundary cases.

Use pseudocode or a small trace table before code. Record the statement, relevant variable values/types, selected branch, and output. Test empty values, zeros, boundaries, invalid input, and repeated use—not only the happy path.

## 2. Variables, data types, and type casting

### Declarations, scope, shadowing, and hoisting

`let` creates a reassignable block-scoped binding. `const` creates a block-scoped binding that cannot be reassigned after initialization; it does not make a referenced object immutable. `var` belongs to its function or surrounding script/module scope and does not acquire scope from an ordinary block. It has legacy hoisting behavior. Use `const` when the binding should remain and `let` when it must change; learn `var` well enough to trace it.

Scope determines where a binding is visible. A block such as `{ ... }` creates scope for `let` and `const`; a function creates local scope. An inner declaration can shadow an outer one. Shadowing creates a different binding—it does not rename or overwrite the outer binding.

Declarations are processed before ordinary execution in ways collectively described as hoisting, but access rules differ. A function declaration can commonly be called before its source position. A `var` binding exists with value `undefined` before its declaration executes. A `let` or `const` binding exists in a temporal dead zone until initialization and cannot be accessed there. “Everything moves to the top” is an inaccurate mental model. `typeof missingName` can return `"undefined"` for an unresolved name, while `typeof` applied to a same-scope `let` before initialization throws `ReferenceError`. In a classic browser script, a top-level `var` can create a global-object property, but top-level `let` does not; module top-level `var` is module-scoped. The review executed separate classic-script and module probes to verify this boundary. See [grammar/types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types), the more precise [let reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let) and [typeof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof). Broad "all globals are object properties" wording must not erase lexical bindings.

### Primitive values and dynamic typing

The scope names `boolean`, `number`, `bigint`, `undefined`, `null`, and `string`. JavaScript is dynamically typed: a binding can later refer to a value of another type. `typeof` reports a string describing a value, with important boundaries: `typeof undefined` is `"undefined"`, `typeof 1n` is `"bigint"`, and historical behavior makes `typeof null` return `"object"` even though null is a primitive value.

`number` represents ordinary numeric values, including floating-point values, `NaN`, and infinities. Binary floating-point cannot exactly represent every decimal. `NaN` means a numeric result is not a valid number; use appropriate number checks instead of assuming equality with `NaN`. `bigint` represents integers with literals such as `10n`. Mixed numeric arithmetic such as `1n + 1` throws `TypeError`, but `1n + "2"` concatenates text; do not generalize the numeric restriction to every operator. `Number(7n)` is permitted explicitly, while unary `+7n` throws. `7n / 2n` gives `3n`, with the fractional part discarded.

The safe integer range for `number` is ±(2^53 − 1): some larger integers are exactly representable, but adjacent integer values are no longer reliably distinct. For example, `Number.MAX_SAFE_INTEGER + 1` and `Number.MAX_SAFE_INTEGER + 2` compare equal. Construct a large exact integer from its text with `BigInt`, rather than first rounding it through `Number`. `BigInt(1.5)` throws `RangeError`; `BigInt("1.5")` throws `SyntaxError`; `BigInt(null)` throws `TypeError`. See [Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number), [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt) and the [BigInt conversion function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt/BigInt). The named syllabus list is not a list of every JavaScript type: Symbol also exists, but is not named in this exam's primitive-type bullet.

Strings are immutable sequences. Single or double quotes create ordinary literals; backticks create template literals, where `${expression}` interpolates a value. Escapes such as `\n` represent special characters. String methods return values rather than modifying individual characters in place. In strict mode, assigning to a string index throws; it does not edit the string. String length/indexes count UTF-16 code units: `"😄".length` is 2, while `for...of` visits one code point for that example. A code point is not always a complete displayed grapheme. See the [String reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String); full Unicode text processing is **PRACTICAL DEPTH**, not an added exam domain.

`undefined` commonly means no value has been supplied; `null` is an explicit null value. They are not interchangeable even though loose equality can obscure their distinction.

### Explicit conversion and coercion

`String(value)`, `Number(value)`, `Boolean(value)`, and `BigInt(value)` perform explicit conversions when defined. Implicit coercion can occur in operators, comparisons, and conditions. Predict both value and type:

```javascript
(() => {
  const entered = prompt("Quantity: decimal digits, 0..1000");
  if (entered === null) {
    console.log("Cancelled");
  } else if (entered.trim() === "") {
    console.error("Quantity is blank");
  } else if (!/^[0-9]+$/.test(entered.trim())) {
    console.error("Use decimal digits only");
  } else {
    const quantity = Number(entered);
    if (!Number.isSafeInteger(quantity) || quantity > 1000) {
      console.error("Quantity must be 0..1000");
    } else {
      console.log("Quantity:", quantity);
    }
  }
})();
```

The check order is deliberate: `Number(null)` and `Number(" ")` both produce zero, so conversion must follow cancel/blank handling. This demo's fictional input contract permits surrounding whitespace and decimal digits (including leading zeros), but rejects signs, fractions, exponent notation, hexadecimal, suffixes and counts above 1000. A different application can choose a different grammar. `Number("12x")` is `NaN`; `parseInt("12x", 10)` accepts the prefix 12 and is not whole-input validation. `Number.isNaN("word")` is false because it does not coerce the string; convert first when that is the intended contract.

Falsy values include `false`, `0`, `-0`, `0n`, `""`, `null`, `undefined`, and `NaN`; objects and arrays are truthy, including an empty array. Prefer explicit validation where `0`, empty text, and absence have different meanings.

### Arrays, objects, and references

An array is an indexed object with a `length` and methods. Indices begin at zero. Recognize adding and removing values (`push`, `unshift`, `pop`), finding positions (`indexOf`), reversing, slicing, and concatenating. Ask whether a method mutates the original or returns a new array. Out-of-range indexed access normally yields `undefined` rather than throwing. `push` and `unshift` return the new length, `pop` returns the removed value (or `undefined` when empty), and `reverse` returns the same mutated array. `slice` and `concat` create new outer arrays with shared nested objects. `delete array[1]` leaves an empty slot and does not shorten length; reducing `length` removes later elements. Do not treat missing slots as identical to own properties whose value is `undefined`. See the [Array reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array); the workbook checks method results as well as changed state.

An object used as a record associates property names with values. Dot notation uses a literal property name; bracket notation can use a computed key. `delete object.key` removes an own configurable property; it is not a general tool for deleting lexical bindings.

Objects and arrays are reference values. Assignment copies the reference, so two bindings may designate the same object. `const` prevents rebinding but permits mutation through the reference:

```javascript
const first = { count: 1 };
const second = first;
second.count += 1;
// first.count is now 2
```

> **Related item:** Equality of objects compares identity, not a recursive comparison of properties. Draw bindings as arrows to objects when tracing aliasing and mutation.

## 3. Operators and user interaction

### Operator families and evaluation

Know assignment and compound assignment, arithmetic, comparison, logical, conditional `?:`, `typeof`, `instanceof`, and `delete`. Unary operators take one operand, binary operators two, and the conditional operator three.

Precedence determines grouping and associativity determines grouping direction among comparable operators. Parentheses communicate intended grouping. `**` exponentiates; `%` computes a remainder; `+` may add or concatenate after coercion. Prefix/postfix increment differ in the value produced by the expression. Exponentiation groups right-to-left: `2 ** 3 ** 2` is 512. `-2 ** 2` is rejected by the grammar; choose `(-2) ** 2` for 4 or `-(2 ** 2)` for -4. Grouping does not reverse operand evaluation: JavaScript evaluates ordinary operands from left to right, while short-circuit rules may skip one. See [operator precedence and short-circuiting](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence).

Prefer strict equality `===` and inequality `!==` for predictable type-aware comparisons. Loose `==` and `!=` can coerce operands; understand that behavior when reading code but do not use memorized coercion oddities as a design technique. Relational comparisons can also convert types.

Logical `&&` and `||` short-circuit and return one of their operands, not necessarily a Boolean. `!` converts to Boolean then negates. This supports compact patterns but can incorrectly replace meaningful falsy values such as zero. Use explicit conditions when the distinction matters.

`instanceof` checks whether a constructor's prototype occurs in an object's prototype chain; it is not a primitive type test. `typeof` suits broad primitive categories but has the `null` exception. `delete` acts on object properties, not object values or block-scoped declarations.

### Browser dialogs

`alert(message)` displays a message and returns `undefined`. `confirm(message)` returns a Boolean. `prompt(message, defaultValue)` returns entered text or `null` when canceled. Even numeric-looking prompt input is text until converted. Treat cancel, blank text, whitespace, invalid number text, and valid zero separately.

Dialogs normally block interaction with the page while open, but browsers can suppress them or alter waiting behavior in some contexts. A suppressed confirm can return false. These are tiny teaching interactions, not a production UI design. Read [prompt](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt), [confirm](https://developer.mozilla.org/en-US/docs/Web/API/Window/confirm) and [alert](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert); automation here handles actual browser dialogs rather than replacing those functions with mocks. Node.js does not supply them by default.

> **Related item:** Input validation decides whether data is acceptable; conversion only changes representation. `Number(" ")` producing zero does not prove that blank input met a business rule.

## 4. Control flow — conditional execution and loops

### Decisions

`if` runs a statement when its condition is truthy; `else if` creates ordered alternatives; `else` catches the remainder. Separate `if` statements may all run, unlike one exclusive chain. Use braces so ownership is visible.

`switch` compares its expression against case values using strict comparison. Without `break`, execution falls through to later clauses. `default` handles no match and can appear in different positions, though placing it last is clearest. The conditional operator `condition ? first : second` is an expression suited to choosing one value, not deeply nested workflows.

### Loops and iteration targets

`while` tests before the body. `do ... while` executes the body once before its first test. A classic `for` groups initialization, condition, and update. `break` leaves the nearest loop or switch. `continue` starts the next loop iteration; in a classic `for`, its update then occurs before the next condition.

`for...of` iterates values from an iterable such as an array or string. `for...in` iterates enumerable property keys, including inherited enumerable properties, and is primarily for object-property enumeration—not array values. If an array's indices are needed, a classic loop or entries-based approach is clearer than treating `for...in` as an array-value loop.

```javascript
const record = { name: "Ari", score: 88 };
for (const key in record) {
  console.log(key, record[key]);
}

const scores = [88, 91];
for (const score of scores) {
  console.log(score);
}
```

`for...in` visits enumerable **string** keys, including inherited ones, and skips symbols. Filter with `Object.hasOwn(record, key)` when only own keys are intended, or iterate `Object.keys(record)`. The original record above has no custom enumerable prototype properties; the workbook adds one deliberately to expose the distinction. See [for...in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in).

For every loop, identify initial state, continuation condition, progress, termination, and the effect of each transfer. Trace empty input and the exact last iteration.

## 5. Functions

### Calls, local state, and first-class values

A declaration defines a reusable function with parameters. A call supplies arguments. `return` ends that call and provides a result; without an explicit returned value, the result is `undefined`. Logging is a side effect and is not returning.

Parameters are local bindings. Primitive arguments supply primitive values; object arguments supply references by value, so a function can mutate the shared object but reassigning its local parameter does not reassign the caller's binding. Local bindings can shadow outer ones.

Functions are first-class values: store one in a variable, place it in an object, pass it as an argument, or return it. A function expression creates a function as an expression. An arrow function is concise function-expression syntax:

```javascript
function double(value) { return value * 2; }
const triple = function (value) { return value * 3; };
const quadruple = value => value * 4;

function apply(value, operation) {
  return operation(value);
}
```

The [functions guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions) supports declaration, expression, argument and recursion rules. A `const` function expression has the binding's temporal dead zone; it is not callable before initialization merely because function declarations can be.

Arrow functions have lexical behavior for `this` and no own `arguments`; those details matter beyond simple JSE examples. Do not mechanically replace object methods with arrows without understanding call context.

### Recursion and callbacks

Recursion needs a reachable base case and a step that moves toward it. Trace each call and pending return. Invalid inputs and excessive depth still require consideration; JavaScript does not guarantee optimization that makes unbounded recursion safe.

A callback is a function supplied for another operation to invoke. Synchronous callbacks run during the current call. `setTimeout(callback, delay)` schedules a one-time timer and `setInterval(callback, delay)` schedules repeated timer tasks. For ordinary small nonnegative delays, the value requests a scheduling threshold, not an exact appointment. Current synchronous work completes before a timer callback runs. Delay coercion, nested-timer minimums, background throttling and signed 32-bit overflow mean an arbitrary numeric argument is not a universal timing guarantee. The worked demo accepts integer delays from 1 to 10000 ms. Read [setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout) and [setInterval](https://developer.mozilla.org/en-US/docs/Web/API/Window/setInterval).

Store timer identifiers when cancellation may be required. An interval continues scheduling until cleared or its environment ends. Avoid writing `setTimeout(work(), 1000)`, which calls `work` immediately and passes its result; pass the function value as `setTimeout(work, 1000)` or wrap arguments in another function.

> **Related item:** The event loop coordinates queued tasks after the call stack becomes available. Promises use additional scheduling semantics but are outside this JSE scope; master timer callback order first.

## 6. Errors, exceptions, debugging, and troubleshooting

### Classify before fixing

A syntax error prevents valid parsing. A semantic/runtime failure occurs when an operation cannot be performed as executed. A logic error runs but produces the wrong result. The public scope names `SyntaxError`, `ReferenceError`, `TypeError`, and `RangeError`:

- malformed syntax can produce `SyntaxError`;
- using an unresolved identifier can produce `ReferenceError`;
- performing an unsupported operation for a value can produce `TypeError`;
- a value outside an allowed numeric range for an operation can produce `RangeError`.

The exact exception depends on the operation, so reproduce a minimal case rather than guessing from a symptom. A malformed whole script cannot run its own `try` to catch its parse failure. The workbook uses `new Function` with fixed, original source strings to make parsing an operation inside an already-running `try`; this demonstrates the boundary, not permission to compile untrusted input.

### Handling and throwing

Place operations that may throw inside `try`; use `catch` to inspect and handle an exception; use `finally` for work that must run whether completion or throwing occurs. `throw` raises a supplied value, though using `Error` objects preserves useful message and stack conventions.

Do not catch every exception merely to hide it. Handle where you can recover, add context, select a deliberate fallback, or rethrow. Validation failures you anticipate can be represented deliberately; programmer defects should remain visible. `finally` runs before the pending return/throw completes, and its own return can replace that result or hide an exception; reserve it for cleanup. Also, a `try` around a call to `setTimeout` cannot catch an exception thrown later by its callback. Handle that failure inside the callback when recovery is intended. Both boundaries were executed, including an observed browser page error. See [try/catch/finally](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch).

### A reproducible debugging loop

Reduce the failing input, state the expected and actual results, read the first relevant console error and stack location, set a breakpoint before divergence, step over or into deliberately, inspect variables and the call stack, and change one cause. Use `console.time`/`console.timeEnd` or the environment's performance tools for measurements, not intuition. Modifying a value in the debugger is an experiment, not a source-code fix. The review used actual Chrome pause, step-over, local inspection, variable mutation and resume commands on an original fixture. It did not click through the visual DevTools interface or execute Google's demo. See the [DevTools debugging workflow](https://developer.chrome.com/docs/devtools/javascript) and [Debugger protocol](https://chromedevtools.github.io/devtools-protocol/tot/Debugger/). The latter's static URL is a redirect shell; the current JavaScript-rendered viewer and selected method contracts were read.

> **Related item:** A regression check records the input that exposed a defect and the expected result after repair. Even before a formal test framework, rerunning that case prevents the same bug from silently returning.

## Executed core workbook

**PRACTICAL DEPTH — original practice.** This complete script prints `114 core checks passed` in the tested browser and Node versions. Predict each result before execution. The helper compares values with `Object.is` so `NaN` can be an expected result; it verifies exact error classes separately. Browser dialog and timer behavior belongs to the following programs, not to Node's host interface.

```javascript
(() => {
  "use strict";
  const passed = [];
  function same(actual, expected, label) {
    if (!Object.is(actual, expected)) throw new Error(label);
    passed.push(label);
  }
  function raises(action, Type, label) {
    let caught = false;
    try { action(); } catch (error) { caught = error instanceof Type; }
    same(caught, true, label);
  }
  same(beforeDeclaration(3), 6, "function declaration before source position");
  function beforeDeclaration(value) { return value * 2; }
  same(legacy, undefined, "var begins as undefined");
  var legacy = 7;
  same(legacy, 7, "var assignment occurs in sequence");
  raises(() => { return lexical; let lexical = 2; }, ReferenceError, "temporal dead zone");
  raises(() => { return typeof lexical; let lexical = 2; }, ReferenceError, "typeof in temporal dead zone");
  same(typeof jseDefinitelyUndeclaredName, "undefined", "typeof unresolved name");
  let outer = 4;
  { let outer = 9; same(outer, 9, "inner binding"); }
  same(outer, 4, "outer binding unchanged");
  const record = { count: 1 };
  record.count += 1;
  same(record.count, 2, "const object can mutate");
  raises(() => { record = {}; }, TypeError, "const binding cannot reassign");
  const values = [true, 2, 2n, undefined, null, "text"];
  const types = ["boolean", "number", "bigint", "undefined", "object", "string"];
  for (let i = 0; i < values.length; i++) same(typeof values[i], types[i], `type ${i}`);
  same(Number(null), 0, "null conversion is zero");
  same(Number("  "), 0, "blank conversion is zero");
  same(Number(undefined), NaN, "undefined conversion is NaN");
  same(Number("12x"), NaN, "Number rejects suffix");
  same(parseInt("12x", 10), 12, "parseInt accepts numeric prefix");
  same(Number("2e2"), 200, "Number accepts exponent text");
  same(Number.isFinite(Infinity), false, "infinity is not finite");
  same(Number.isNaN("word"), false, "isNaN does not coerce text");
  same(Number.isNaN(Number("word")), true, "isNaN after conversion");
  same(NaN === NaN, false, "NaN strict self equality");
  same(0.1 + 0.2 === 0.3, false, "binary fraction rounding");
  same(Number.MAX_SAFE_INTEGER + 1 === Number.MAX_SAFE_INTEGER + 2, true, "unsafe integer collision");
  same(Number.isSafeInteger(Number("9007199254740993")), false, "unsafe converted integer");
  same(BigInt("9007199254740993"), 9007199254740993n, "BigInt preserves integer text");
  same(7n / 2n, 3n, "BigInt integer division");
  same(Number(7n), 7, "explicit Number conversion");
  raises(() => 1n + 1, TypeError, "mixed numeric addition");
  raises(() => +1n, TypeError, "unary plus on BigInt");
  raises(() => BigInt(1.5), RangeError, "fractional number to BigInt");
  raises(() => BigInt("1.5"), SyntaxError, "fractional text to BigInt");
  raises(() => BigInt(null), TypeError, "null to BigInt");
  same(1n + "2", "12", "BigInt and string concatenate");
  same(2n === 2, false, "strict different numeric types");
  same(2n == 2, true, "loose numeric equality");
  for (const value of [false, 0, -0, 0n, "", null, undefined, NaN])
    same(Boolean(value), false, "falsy input");
  same(Boolean([]), true, "empty array truthy");
  same(Boolean({}), true, "empty object truthy");
  same(Boolean("false"), true, "nonempty false text truthy");
  same(0 || 10, 10, "or replaces meaningful zero");
  same("ready" && 5, 5, "and returns selected operand");
  let calls = 0;
  const skipped = false && (++calls > 0);
  same(skipped, false, "short circuit result");
  same(calls, 0, "short circuit skipped right side");
  same("2" + 3, "23", "plus concatenation");
  same("2" * 3, 6, "multiplication numeric coercion");
  same(-7 % 3, -1, "signed remainder");
  same(2 + 3 * 4, 14, "precedence grouping");
  same(2 ** 3 ** 2, 512, "right associative exponentiation");
  raises(() => new Function("return -2 ** 2;"), SyntaxError, "unparenthesized unary exponent syntax");
  same((-2) ** 2, 4, "parenthesized negative base");
  same(-(2 ** 2), -4, "negated exponent result");
  let counter = 4;
  const old = counter++;
  const fresh = ++counter;
  same(`${old},${fresh},${counter}`, "4,6,6", "separate increments");
  same(typeof [], "object", "array typeof");
  same([] instanceof Array, true, "same-realm array prototype");
  same(2 instanceof Number, false, "primitive not boxed Number");
  const name = "Ari";
  same(name.toUpperCase(), "ARI", "string method result");
  same(name, "Ari", "string unchanged");
  raises(() => { name[0] = "E"; }, TypeError, "strict string indexed assignment");
  same("😄".length, 2, "UTF16 length");
  let points = 0;
  for (const point of "😄") { points += 1; same(point, "😄", "string iterator code point"); }
  same(points, 1, "one code point in two code units");
  const items = [4, 5];
  same(items.push(6), 3, "push returns length");
  same(items.unshift(3), 4, "unshift returns length");
  same(items.pop(), 6, "pop returns removed value");
  same(items.indexOf(4), 1, "indexOf found");
  same(items.indexOf(99), -1, "indexOf absent");
  same(items.reverse() === items, true, "reverse returns same mutated array");
  same(items.join(","), "5,4,3", "reverse order");
  const slice = items.slice(0, 2);
  same(slice.join(","), "5,4", "slice end excluded");
  same(slice === items, false, "slice creates outer array");
  same(items.concat([8]).join(","), "5,4,3,8", "concat result");
  same(items.length, 3, "concat leaves source length");
  same([].pop(), undefined, "empty pop");
  same(items[99], undefined, "ordinary missing index");
  const nested = [{ count: 1 }];
  const copy = nested.slice();
  copy[0].count = 2;
  same(nested[0].count, 2, "shallow copied element still shared");
  const alias = nested;
  same(alias === nested, true, "assignment preserves identity");
  const slots = [1, 2, 3];
  delete slots[1];
  same(slots.length, 3, "delete keeps array length");
  same(1 in slots, false, "delete creates empty slot");
  slots.length = 1;
  same(2 in slots, false, "shorter length removes elements");
  const inherited = Object.create({ inherited: 7 });
  inherited.own = 8;
  const keys = [];
  for (const key in inherited) keys.push(key);
  same(keys.includes("inherited") && keys.includes("own"), true, "for-in includes inherited enumerable keys");
  same(Object.keys(inherited).join(","), "own", "own-key filter");
  let sum = 0;
  for (let i = 0; i < 6; i++) {
    if (i === 2) continue;
    if (i === 5) break;
    sum += i;
  }
  same(sum, 8, "for update after continue");
  let visits = 0;
  while (visits < 0) visits++;
  same(visits, 0, "while zero visits");
  do { visits++; } while (visits < 0);
  same(visits, 1, "do one visit");
  let branch = "";
  switch ("2") {
    case 2: branch = "number"; break;
    case "2": branch += "text";
    default: branch += ":end";
  }
  same(branch, "text:end", "strict switch matching and fallthrough");
  function mutate(value) { value.count++; value = { count: 99 }; }
  const shared = { count: 3 };
  mutate(shared);
  same(shared.count, 4, "parameter reference copied by value");
  function noResult() { const local = 1; void local; }
  same(noResult(), undefined, "no explicit result");
  const triple = function (value) { return value * 3; };
  const quadruple = value => value * 4;
  function apply(value, operation) { return operation(value); }
  same(apply(3, triple), 9, "function expression callback");
  same(apply(3, quadruple), 12, "arrow callback");
  function factorial(n) {
    if (!Number.isInteger(n) || n < 0 || n > 12) throw new RangeError("0..12 required");
    return n <= 1 ? 1 : n * factorial(n - 1);
  }
  same(factorial(0), 1, "factorial zero");
  same(factorial(5), 120, "factorial progress");
  same(factorial(12), 479001600, "factorial bounded endpoint");
  for (const invalid of [-1, 13, 1.5, NaN]) raises(() => factorial(invalid), RangeError, "factorial rejects invalid");
  raises(() => new Function("let = ;"), SyntaxError, "fixed malformed source compiled inside try");
  raises(() => jseDefinitelyUndeclaredName, ReferenceError, "unresolved identifier");
  raises(() => null.value, TypeError, "null property access");
  raises(() => new Array(-1), RangeError, "invalid array length");
  const order = [];
  try { order.push("try"); throw new Error("original fixture"); }
  catch (error) { order.push(error.message); }
  finally { order.push("finally"); }
  same(order.join(","), "try,original fixture,finally", "catch then cleanup");
  function overridingReturn() { try { return 1; } finally { return 2; } }
  same(overridingReturn(), 2, "finally return masks pending result");
  globalThis.jseTrace = { passed: passed.length, labels: passed };
  console.log(`${passed.length} core checks passed`);
})();
```

## Integrated scenarios

Each program runs in a fresh browser page or console. Monetary values, quantity limits, timing settings and inventory rules are fictional. Globals beginning `jse` expose the original demo state for inspection. There is no purchase, account, server or persistent storage.

### Scenario 1: Browser order quote

Quantity uses decimal digits in 0..1000; valid zero remains data. Basic/premium prices are 250/400 integer cents, with a 10% unit-price reduction starting at quantity 10. All possible totals under this contract are safe integers. Cancellation, empty text, invalid grammar, unknown tier and declined confirmation leave the order array empty.

```javascript
(() => {
  "use strict";
  const orders = [];
  function parseQuantity(text) {
    if (text === null) return { kind: "cancelled" };
    if (typeof text !== "string") return { kind: "invalid" };
    const cleaned = text.trim();
    if (cleaned === "") return { kind: "empty" };
    if (!/^[0-9]+$/.test(cleaned)) return { kind: "invalid" };
    const quantity = Number(cleaned);
    if (!Number.isSafeInteger(quantity) || quantity > 1000) return { kind: "invalid" };
    return { kind: "ok", quantity };
  }
  function makeQuote(quantity, tier) {
    if (!Number.isSafeInteger(quantity) || quantity < 0 || quantity > 1000)
      throw new RangeError("Quantity must be 0..1000");
    if (tier !== "basic" && tier !== "premium") throw new TypeError("Unknown tier");
    const baseCents = tier === "basic" ? 250 : 400;
    const unitCents = quantity >= 10 ? baseCents * 9 / 10 : baseCents;
    return { quantity, tier, unitCents, totalCents: quantity * unitCents };
  }
  function runOrder() {
    const parsed = parseQuantity(prompt("Quantity: decimal digits, 0..1000"));
    if (parsed.kind !== "ok") {
      console.log(`Quantity ${parsed.kind}`);
      return { status: parsed.kind };
    }
    const enteredTier = prompt("Tier: basic or premium", "basic");
    if (enteredTier === null) return { status: "cancelled" };
    const tier = enteredTier.trim().toLowerCase();
    if (tier !== "basic" && tier !== "premium") return { status: "invalid-tier" };
    const order = makeQuote(parsed.quantity, tier);
    if (!confirm(`Record ${order.quantity} ${tier} units for ${order.totalCents} cents?`))
      return { status: "declined" };
    orders.push(order);
    const alertResult = alert(`Recorded ${order.totalCents} cents`);
    return { status: "recorded", order, alertReturnedUndefined: alertResult === undefined };
  }
  // Original in-memory demo: there is no account, payment or remote order submission.
  globalThis.jseOrder = { parseQuantity, makeQuote, runOrder, orders };
  globalThis.jseOrderResult = runOrder();
})();
```

Quantity 9/basic gives 2250 cents; 10/basic also gives 2250 after the unit-price change. At 1000/premium the result is 360000 cents. The recorded return value and `orders[0]` designate the same order object; this is deliberate aliasing, not an independent copy. The review tested 19 actual dialog flows plus both tiers at quantities 0/1/9/10/11/1000, malformed input and helper failures. Accepting the alert returns `undefined`; dismissing confirm returns false. Browser suppression remains a separate platform limit.

### Scenario 2: Timed code-reading practice

The two prompts below are original language exercises. Load the definitions, then call `jseTimed.start()`, inspect `jseTimed.currentQuestion()`, and pass text to `jseTimed.answer("string")` and `jseTimed.answer("14")`. Call `jseTimed.cancel()` to stop. Every terminal path clears warning, interval and deadline identifiers. `ticks` counts callbacks and is not elapsed seconds. This is callback practice, not a reliable assessment clock: busy/background pages can delay timers and therefore the moment the demo changes to timed-out.

```javascript
(() => {
  "use strict";
  // Original code-reading prompts, not certification exam items.
  const questions = [
    { text: 'typeof "5"', answer: "string" },
    { text: "2 + 3 * 4", answer: "14" }
  ];
  const state = { status: "idle", position: 0, correct: 0, ticks: 0, events: [] };
  let warningId, intervalId, deadlineId;
  function clearTimers() {
    clearTimeout(warningId);
    clearInterval(intervalId);
    clearTimeout(deadlineId);
  }
  function finish(status) {
    if (state.status !== "running") return false;
    state.status = status;
    state.events.push(status);
    clearTimers();
    return true;
  }
  function start(warningMs = 1000, deadlineMs = 2000, tickMs = 250) {
    if (state.status === "running") throw new Error("Already running");
    for (const delay of [warningMs, deadlineMs, tickMs])
      if (!Number.isInteger(delay) || delay < 1 || delay > 10000)
        throw new RangeError("Use integer delays in 1..10000 ms");
    if (warningMs >= deadlineMs) throw new RangeError("Warning must precede deadline");
    clearTimers();
    Object.assign(state, { status: "running", position: 0, correct: 0, ticks: 0, events: ["start"] });
    warningId = setTimeout(() => {
      if (state.status === "running") state.events.push("warning");
    }, warningMs);
    intervalId = setInterval(() => {
      if (state.status === "running") state.ticks++;
    }, tickMs);
    deadlineId = setTimeout(() => finish("timed-out"), deadlineMs);
    state.events.push("setup-complete");
  }
  function answer(text) {
    if (state.status !== "running") return false;
    if (typeof text !== "string") throw new TypeError("Answer must be text");
    const question = questions[state.position];
    if (text.trim() === question.answer) state.correct++;
    state.position++;
    if (state.position === questions.length) finish("completed");
    return true;
  }
  function currentQuestion() {
    return state.status === "running" ? questions[state.position].text : null;
  }
  globalThis.jseTimed = { state, start, answer, currentQuestion, cancel: () => finish("cancelled") };
  // In a fresh browser console, use jseTimed.start(), jseTimed.currentQuestion(), jseTimed.answer(text).
  // Tick counts are callback counts, not a measurement of wall-clock seconds.
})();
```

Synchronous setup records `start` then `setup-complete`. With no answers, the tested short-delay run later recorded `warning`, then `timed-out`; its interval callback ran and stopped after termination. Immediate answers complete with two correct responses; a wrong first answer completes with one. Tests also verified cancel, restart, late-answer rejection, malformed settings and clearing every timer. They do not establish an exact callback count or timing guarantee on another run. A separate fixed callback deliberately threw an error: the surrounding scheduling try did not catch that later exception, and the harness recorded the browser page error.

### Scenario 3: Inventory and debugger

Inventory records require unique nonempty string codes and integer stock in 0..1000. `take` changes the shared record only after validation and availability checks. Zero stock, a zero request, an insufficient request and a missing code have distinct results. The own-key filter prevents inherited enumerable fields from appearing in this simple display.

```javascript
(() => {
  "use strict";
  function validateInventory(items) {
    if (!Array.isArray(items)) throw new TypeError("Inventory must be an array");
    const codes = [];
    for (const item of items) {
      if (item === null || typeof item !== "object" || typeof item.code !== "string" ||
          item.code === "" || !Number.isSafeInteger(item.stock) || item.stock < 0 || item.stock > 1000)
        throw new TypeError("Invalid inventory record");
      if (codes.includes(item.code)) throw new Error("Duplicate item code");
      codes.push(item.code);
    }
  }
  function take(items, code, quantity) {
    validateInventory(items);
    if (typeof code !== "string") throw new TypeError("Code must be text");
    if (!Number.isSafeInteger(quantity) || quantity < 0 || quantity > 1000)
      throw new RangeError("Quantity must be 0..1000");
    for (const item of items) {
      if (item.code === code) {
        if (quantity > item.stock) return { status: "insufficient", stock: item.stock };
        item.stock -= quantity;
        return { status: "ok", stock: item.stock };
      }
    }
    return { status: "missing" };
  }
  const items = [{ code: "CABLE", stock: 4 }, { code: "ADAPTER", stock: 0 }];
  const ownFields = [];
  for (const key in items[0]) {
    if (Object.hasOwn(items[0], key)) ownFields.push(`${key}=${items[0][key]}`);
  }
  const first = take(items, "CABLE", 1);
  const zero = take(items, "ADAPTER", 0);
  const missing = take(items, "OTHER", 0);
  console.log(ownFields.join(", "));
  console.log(first.status, first.stock, zero.status, zero.stock, missing.status);
  globalThis.jseInventory = { items, take, validateInventory };
})();
```

The first output is `code=CABLE, stock=4`; the second is `ok 3 ok 0 missing`. Tests cover empty/first/last/missing lookups, quantity and stock limits, duplicate/malformed records, preserved state on rejection and alias-visible mutation.

For a bounded debugger experiment, use a deliberately faulty `removeOne(stock)` with local `remaining = stock`, a `debugger;` statement, then `remaining += 1` and `return remaining`. Expected output for 4 is 3; actual output is 5. The review paused at the debugger statement, stepped across the increment and inspected the local changing from 4 to 5. On a second invocation it changed `remaining` to 2 **before the arithmetic**, producing 3 for that call. Running the unchanged source again produced 5. Correcting the source to `remaining -= 1` then produced 3. A paused-value experiment is evidence about execution state, not a persistent repair. Exact original/fixed probe sources and protocol observations are in the operation record.

## Hands-on labs

These eight broader activities remain **proposed**. The separately recorded original code, browser scenarios and bounded debugger probe cover selected cases, not every learner variation, browser or visual UI step.

1. **Runtime boundary:** run the same core expressions in a browser console, embedded page script, and optionally Node.js. Record which globals come from the host and why dialogs are browser-specific.
2. **Declaration and scope matrix:** predict `let`, `const`, and `var` behavior across global, function, and block scopes, including shadowing, use-before-initialization, reassignment, and object mutation through `const`.
3. **Type/conversion table:** record value, `typeof`, explicit conversion, Boolean result, and error for at least 25 primitive inputs including zero, blank text, whitespace, `null`, `undefined`, `NaN`, and BigInt boundaries.
4. **Arrays, records, and identity:** exercise the named basic array operations and dot/bracket properties. Draw aliases, compare object identity, copy one level, mutate nested state, and explain every observed change.
5. **Operators and dialogs:** predict precedence, strict/loose comparison, short-circuit, conditional, `typeof`, `instanceof`, and `delete` cases. Build a validated three-dialog interaction covering cancel, blank, invalid, and valid-zero input.
6. **Control-flow tracer:** implement the same bounded classification with an `if` chain and `switch` where appropriate; trace `while`, `do`, classic `for`, `for...in`, and `for...of`, plus `break` and `continue` in nested cases.
7. **Function/timer laboratory:** rewrite one operation as declaration, expression, and arrow; pass it as a callback; trace recursion; schedule and clear timeout/interval callbacks; prove that delay is not an exact execution time.
8. **Exception/debugging workbook:** reproduce the four named error categories plus a logic defect in isolated code. Use `try`/`catch`/`finally`, throw one deliberate `Error`, step with developer tools, inspect the call stack, time a small operation, and preserve regression inputs.

## Original readiness checks

1. What is the difference between the JavaScript language and a host environment?
2. Why is “JavaScript is only interpreted” incomplete?
3. How do client-side and server-side execution differ?
4. What two ways can a beginner run JavaScript in a browser?
5. How do `let`, `const`, and `var` differ in scope and reassignment?
6. Why can a `const` array still be mutated?
7. What is shadowing?
8. What occurs when `let` is read in its temporal dead zone?
9. What value does an early-read `var` binding commonly expose?
10. Which primitive types are named in the official JSE scope?
11. What surprising result does `typeof null` produce?
12. Why can ordinary `number` and `bigint` not be freely mixed in arithmetic?
13. How do `undefined` and `null` differ in intent?
14. Why is explicit conversion not the same as validation?
15. Name the falsy values relevant at this level.
16. What happens on out-of-range ordinary array indexing?
17. How do dot and bracket property access differ?
18. What does assigning one object variable to another copy?
19. Why is strict equality normally preferable?
20. What do `&&` and `||` return?
21. When is `instanceof` useful, and when is `typeof` more suitable?
22. What does `delete` normally remove?
23. What are the return types of `alert`, `confirm`, and `prompt`?
24. How should prompt cancellation differ from numeric zero?
25. How do an `if` chain and separate `if` statements differ?
26. What happens after a matching `switch` case without `break`?
27. How do `while` and `do...while` differ?
28. What is the effect of `continue` in a classic `for` loop?
29. How do `for...in` and `for...of` differ?
30. What does a function return without an explicit returned value?
31. Why is logging not the same as returning?
32. How can a function mutate a caller-visible object even though arguments are passed by value?
33. What makes functions first-class values?
34. What two conditions make basic recursion terminate?
35. Why does `setTimeout(work(), 1000)` usually not schedule `work` correctly?
36. Why is a timer delay not an exact appointment?
37. What distinguishes SyntaxError, ReferenceError, TypeError, and RangeError?
38. When does `finally` run?
39. What is the shortest dependable debugging loop?
40. What must you verify on the official JSE page before purchase?

## Answer key

1. The language defines core syntax/semantics; the host supplies APIs such as browser dialogs or Node facilities.
2. Modern engines can parse, interpret, optimize, and just-in-time compile during execution.
3. Client code runs in a user's client environment; server code runs on a server and returns results/resources.
4. A developer console and a script embedded in or linked from an HTML page.
5. `let`/`const` are block scoped; `var` uses function or surrounding script/module scope. A classic global lexical binding is not a global-object property. `let`/`var` can be rebound; `const` cannot.
6. `const` fixes the binding, not the referenced object's internal state.
7. An inner binding with the same name hides a distinct outer binding.
8. A `ReferenceError` is thrown.
9. `undefined` before its declaration assignment executes.
10. Boolean, number, bigint, undefined, null, and string.
11. The historical string result `"object"`.
12. Mixed numeric arithmetic throws, but comparisons and string concatenation have different rules. Explicit Number(BigInt) is allowed; unary plus on BigInt is not. Converting a large integer through Number can lose precision.
13. `undefined` often means absent/not supplied; `null` is an explicit null value.
14. Number(null) and Number(blank text) are both zero. Check cancellation and grammar first, then safe integer/range limits; parseInt can accept a suffix-bearing numeric prefix.
15. `false`, `0`, `-0`, `0n`, empty string, `null`, `undefined`, and `NaN`.
16. Ordinary missing indexing yields undefined, but a missing slot is distinct from an own undefined-valued property. Deleting an index does not shorten array length.
17. Dot uses a literal name; brackets can evaluate a key expression.
18. The reference, so both variables can designate the same object.
19. It avoids implicit type coercion while comparing.
20. One of their operand values, chosen through short-circuit evaluation.
21. `instanceof` checks an object/prototype relationship; `typeof` reports broad value categories, with known boundaries.
22. An object property when deletion is permitted.
23. `alert` → `undefined`; `confirm` → Boolean; `prompt` → string or `null`.
24. Check null, empty/whitespace and the intended numeric grammar before conversion. Preserve valid zero. The quote contract uses digits and 0..1000; canceled or declined dialogs do not append an order.
25. One chain selects at most one path; independent conditions may select several.
26. Execution falls through to later clauses until transferred.
27. `while` may run zero times; `do...while` runs the body at least once.
28. The rest of the body is skipped, then the update runs before the next condition.
29. `for...in` enumerates property keys; `for...of` iterates iterable values.
30. `undefined`.
31. Logging is an output side effect; returning supplies a call result and ends that call.
32. The copied argument value is a reference to the same object, whose properties can be mutated.
33. They can be stored, passed, and returned like other values.
34. A reachable base case and progress toward it.
35. It calls `work` immediately and supplies its result instead of the function value.
36. Small ordinary delays request eligibility, then current work and scheduling affect execution. Coercion, overflow and browser throttling further qualify arbitrary delays; interval ticks are not wall-clock seconds.
37. Invalid syntax; unresolved identifier; operation incompatible with a value; and an operation-specific out-of-range value.
38. Before pending control flow leaves try/catch/finally, subject to abrupt environment termination. Returning/throwing from finally can replace the pending result; it cannot make an outer scheduling try catch a later callback error.
39. Reproduce minimally, compare expected/actual, read error/stack, stop before divergence, inspect, change one cause, and rerun a regression case.
40. Confirm JSE-40-01 remains active and recheck the scope, format, language, price, delivery, practice alignment, and policies.

## Final readiness checklist

- [ ] I distinguish core JavaScript from browser and Node.js APIs.
- [ ] I trace declarations, scope, hoisting, the temporal dead zone, values, types, and references.
- [ ] I predict coercion and use explicit conversion plus separate validation.
- [ ] I distinguish arrays from record objects and identity from value-like expectations.
- [ ] I can trace all named operators and browser-dialog return values.
- [ ] I choose `for...in` for appropriate keys and `for...of` for iterable values.
- [ ] I rewrite and pass functions, trace recursion, and predict basic timer callback order.
- [ ] I classify the named errors and use `try`/`catch`/`finally`/`throw` deliberately.
- [ ] I can debug with a minimal reproduction, breakpoints, state, stack, timing, and regression input.
- [ ] I have rechecked the current official page rather than relying on this dated snapshot.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick one primary path, add a second explanation only where useful, and spend at least as much time predicting, coding, testing, and debugging as watching. Commercial and community resources are supplementary; reconcile them with the current official scope.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official JSE exam page and scope](https://jsinstitute.org/jse-certification) | Free official blueprint | 1–2 hours to map and recheck |
| [JS Institute TestNow policies](https://jsinstitute.org/test-now-testing-policies) | Free official policy | 20–40 minutes before scheduling |
| [Official JSE-40-01 Practice Test Kit](https://ums.edube.org/products/0-jsi-jse-4001-pt) | Paid official practice; USD 29 when checked | 3–6 hours across attempts and review |
| [OpenEDG JavaScript Essentials 1](https://jsinstitute.org/javascript-essentials-1) | Free account; public six-module listing read, lessons not entered | 40 hours listed |
| [Cisco Networking Academy JavaScript Essentials 1](https://www.netacad.com/courses/javascript-essentials-1) | Free account; only application shell retrieved | About 40 hours is a planning reference from the aligned course; partner duration unverified |
| [MDN Dynamic Scripting with JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting) | Free; module index and selected separate reference pages read | 15–25 hours is an author estimate; DOM/network topics exceed this scope |
| [Microsoft Beginner's Series to JavaScript](https://learn.microsoft.com/en-us/shows/beginners-series-to-javascript/) | Free Node.js series; current page does not expose episode count/runtime | Prior 51-part claim not reverified; 4–6 hours is an author estimate |
| [Pluralsight Professional JavaScript path](https://www.pluralsight.com/paths/javascript-2022) | Subscription; current public listing: 28 courses/38 labs/85 hours | Fundamentals 6h08m + Debugging 1h35m = 7h43m; selected guided labs add 3h24m |
| [O'Reilly JavaScript: The Definitive Guide, 7th Edition](https://www.oreilly.com/library/view/javascript-the-definitive/9781491952016/) | Subscription; HTTP 403; prior 21h15m not reverified | Select early language/debugging chapters; 8–12 hours is an author estimate |
| [Udemy Complete JavaScript Course by Jonas Schmedtmann](https://www.udemy.com/course/the-complete-javascript-course/) | Paid marketplace; HTTP 403; prior 71h10m not reverified | Select fundamentals/debugging; 12–18 hours is an author estimate |
| [freeCodeCamp Learn JavaScript — Full Course for Beginners](https://www.youtube.com/watch?v=PkZNo7MFNFg) | Free; title/shell only, no playback/transcript review | Prior approximately 3h27m not reverified; add coding time |

**VERIFY CURRENT — source limits:** Canonical exam, course and policy pages were read via the public web reader after direct requests timed out. The objective monitor failed its direct comparison; snapshots were retained after manual review. The exam page has an apparent copy error labeling the associated JSA credential as a Python data-analyst certification; it does not change JSE scope. The policy opening says entry-level exams default to non-proctored delivery, while its later generic delivery paragraph calls online proctoring the global default. Verify the applicable mode before booking. Failed attempts currently have a seven-day retake wait; account and booking screens were not inspected.

The official practice product describes multiple launches but the current captured page gives no exact count. Its 12-month voucher redemption validity is separate from an exam attempt, which the practice-only product does not include. Paid practice questions were not accessed. The [Microsoft supporting repository](https://github.com/microsoft/beginners-intro-javascript-node) was archived June 15, 2026; its README assumes experience with another language and uses Node. That context matters when choosing it as a beginner supplement. Pluralsight metadata came from its headline and selected novice/entry-level listings, not paid lessons; the guided variables/data, scope, and control-flow/collections labs list 100 + 40 + 64 = 204 minutes (3h24m). No lab was entered or video watched. A source landing page is not proof of complete lesson quality or exact exam coverage.

No exact current MeasureUp or Whizlabs JSE-40-01 product was verified. The OpenEDG practice kit explicitly identifies the active version; avoid third-party practice that does not state its blueprint and provenance.
