---
exam_code: JSE-40-01
vendor_id: js-institute
official_blueprint: https://jsinstitute.org/jse-certification
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# JSE-40-01 Certified Entry-Level JavaScript Programmer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked September 2, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#jse-40-01-coverage-record). The [official JSE exam page and scope](https://jsinstitute.org/jse-certification) are authoritative.

**Current baseline:** JSE-40-01, active; six-block public scope<br>
**Upcoming blueprint change:** none announced on the official exam or certification-catalog pages when checked<br>
**Official delivery snapshot:** 30 single- and multiple-select questions; 40-minute exam plus 5-minute tutorial/NDA; 70% passing score; TestNow; English and Spanish<br>
**Purchase snapshot:** no formal prerequisite; exam from USD 69, exam-plus-retake from USD 86, and exam-plus-retake-plus-practice from USD 95 when checked; standalone official practice was USD 29<br>

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

The main official scope does not display weights. The percentages above come from the provider's JSE-40-01 Practice Test Kit page, which says its content is organized to those six blocks. Treat them as a study-allocation signal, not proof of individual item counts or scoring values.

## 1. Introduction to JavaScript and computer programming — 8%

### Language, engine, and host

JavaScript source is parsed and executed by an engine inside a host environment. Modern engines commonly combine interpretation and just-in-time compilation; do not reduce real behavior to “JavaScript is only interpreted.” The host supplies capabilities outside the core language. A browser supplies a document, console, dialogs, timers, and Web APIs. Node.js supplies a different server/local runtime and APIs.

Client-side code runs in the user's browser; server-side code runs in a server environment and returns results or resources to clients. The same core syntax can run in either, but a host-specific global may not exist in the other. Always ask two questions: “Is this JavaScript language behavior?” and “Which host provides this function or object?”

For JSE practice, create a minimal HTML file with a `<script>` block or linked `.js` file, and also run expressions directly in browser developer tools. Source order matters. A classic script ordinarily executes when encountered; loading strategies such as modules or `defer` are useful related context but beyond the core objective.

> **Related item:** ECMAScript is the language specification standardized by Ecma International; JavaScript is the widely used implementation name. Browser compatibility and Web APIs are separate from the core standard even when developers use them together.

### From problem to program

Translate a problem into inputs, state, decisions, repetition, functions, output, and error paths. Syntax determines whether tokens form valid code. Semantics determines what valid code means. A correct program also needs the intended result for normal and boundary cases.

Use pseudocode or a small trace table before code. Record the statement, relevant variable values/types, selected branch, and output. Test empty values, zeros, boundaries, invalid input, and repeated use—not only the happy path.

## 2. Variables, data types, and type casting — 20%

### Declarations, scope, shadowing, and hoisting

`let` creates a reassignable block-scoped binding. `const` creates a block-scoped binding that cannot be reassigned after initialization; it does not make a referenced object immutable. `var` is function-scoped rather than block-scoped and has legacy hoisting behavior. Use `const` when the binding should remain and `let` when it must change; learn `var` well enough to trace it.

Scope determines where a binding is visible. A block such as `{ ... }` creates scope for `let` and `const`; a function creates local scope. An inner declaration can shadow an outer one. Shadowing creates a different binding—it does not rename or overwrite the outer binding.

Declarations are processed before ordinary execution in ways collectively described as hoisting, but access rules differ. A function declaration can commonly be called before its source position. A `var` binding exists with value `undefined` before its declaration executes. A `let` or `const` binding exists in a temporal dead zone until initialization and cannot be accessed there. “Everything moves to the top” is an inaccurate mental model.

### Primitive values and dynamic typing

The scope names `boolean`, `number`, `bigint`, `undefined`, `null`, and `string`. JavaScript is dynamically typed: a binding can later refer to a value of another type. `typeof` reports a string describing a value, with important boundaries: `typeof undefined` is `"undefined"`, `typeof 1n` is `"bigint"`, and historical behavior makes `typeof null` return `"object"` even though null is a primitive value.

`number` represents ordinary numeric values, including floating-point values, `NaN`, and infinities. Binary floating-point cannot exactly represent every decimal. `NaN` means a numeric result is not a valid number; use appropriate number checks instead of assuming equality with `NaN`. `bigint` represents arbitrary-size integers and uses literals such as `10n`; ordinary `number` and `bigint` arithmetic cannot be mixed without explicit conversion.

Strings are immutable sequences. Single or double quotes create ordinary literals; backticks create template literals, where `${expression}` interpolates a value. Escapes such as `\n` represent special characters. String methods return values rather than modifying individual characters in place.

`undefined` commonly means no value has been supplied; `null` is an explicit null value. They are not interchangeable even though loose equality can obscure their distinction.

### Explicit conversion and coercion

`String(value)`, `Number(value)`, `Boolean(value)`, and `BigInt(value)` perform explicit conversions when defined. Implicit coercion can occur in operators, comparisons, and conditions. Predict both value and type:

```javascript
const entered = prompt("Quantity"); // string or null
const quantity = Number(entered);

if (!Number.isFinite(quantity) || quantity < 0) {
  console.error("Enter a non-negative number");
}
```

Falsy values include `false`, `0`, `-0`, `0n`, `""`, `null`, `undefined`, and `NaN`; objects and arrays are truthy, including an empty array. Prefer explicit validation where `0`, empty text, and absence have different meanings.

### Arrays, objects, and references

An array is an indexed object with a `length` and methods. Indices begin at zero. Recognize adding and removing values (`push`, `unshift`, `pop`), finding positions (`indexOf`), reversing, slicing, and concatenating. Ask whether a method mutates the original or returns a new array. Out-of-range indexed access normally yields `undefined` rather than throwing.

An object used as a record associates property names with values. Dot notation uses a literal property name; bracket notation can use a computed key. `delete object.key` removes an own configurable property; it is not a general tool for deleting lexical bindings.

Objects and arrays are reference values. Assignment copies the reference, so two bindings may designate the same object. `const` prevents rebinding but permits mutation through the reference:

```javascript
const first = { count: 1 };
const second = first;
second.count += 1;
// first.count is now 2
```

> **Related item:** Equality of objects compares identity, not a recursive comparison of properties. Draw bindings as arrows to objects when tracing aliasing and mutation.

## 3. Operators and user interaction — 18%

### Operator families and evaluation

Know assignment and compound assignment, arithmetic, comparison, logical, conditional `?:`, `typeof`, `instanceof`, and `delete`. Unary operators take one operand, binary operators two, and the conditional operator three.

Precedence determines grouping and associativity determines grouping direction among comparable operators. Parentheses communicate intended grouping. `**` exponentiates; `%` computes a remainder; `+` may add or concatenate after coercion. Prefix/postfix increment differ in the value produced by the expression.

Prefer strict equality `===` and inequality `!==` for predictable type-aware comparisons. Loose `==` and `!=` can coerce operands; understand that behavior when reading code but do not use memorized coercion oddities as a design technique. Relational comparisons can also convert types.

Logical `&&` and `||` short-circuit and return one of their operands, not necessarily a Boolean. `!` converts to Boolean then negates. This supports compact patterns but can incorrectly replace meaningful falsy values such as zero. Use explicit conditions when the distinction matters.

`instanceof` checks whether a constructor's prototype occurs in an object's prototype chain; it is not a primitive type test. `typeof` suits broad primitive categories but has the `null` exception. `delete` acts on object properties, not object values or block-scoped declarations.

### Browser dialogs

`alert(message)` displays a message and returns `undefined`. `confirm(message)` returns a Boolean. `prompt(message, defaultValue)` returns entered text or `null` when canceled. Even numeric-looking prompt input is text until converted. Treat cancel, blank text, whitespace, invalid number text, and valid zero separately.

Dialogs are blocking browser conveniences useful for tiny labs, not a production UI architecture. Node.js does not supply them by default.

> **Related item:** Input validation decides whether data is acceptable; conversion only changes representation. `Number(" ")` producing zero does not prove that blank input met a business rule.

## 4. Control flow — conditional execution and loops — 21%

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

For every loop, identify initial state, continuation condition, progress, termination, and the effect of each transfer. Trace empty input and the exact last iteration.

## 5. Functions — 21%

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

Arrow functions have lexical behavior for `this` and no own `arguments`; those details matter beyond simple JSE examples. Do not mechanically replace object methods with arrows without understanding call context.

### Recursion and callbacks

Recursion needs a reachable base case and a step that moves toward it. Trace each call and pending return. Invalid inputs and excessive depth still require consideration; JavaScript does not guarantee optimization that makes unbounded recursion safe.

A callback is a function supplied for another operation to invoke. Synchronous callbacks run during the current call. `setTimeout(callback, delay)` schedules a one-time timer and `setInterval(callback, delay)` schedules repeated timer tasks. The delay is a minimum scheduling threshold, not an exact execution appointment; current synchronous work completes before a timer callback can run.

Store timer identifiers when cancellation may be required. An interval continues scheduling until cleared or its environment ends. Avoid writing `setTimeout(work(), 1000)`, which calls `work` immediately and passes its result; pass the function value as `setTimeout(work, 1000)` or wrap arguments in another function.

> **Related item:** The event loop coordinates queued tasks after the call stack becomes available. Promises use additional scheduling semantics but are outside this JSE scope; master timer callback order first.

## 6. Errors, exceptions, debugging, and troubleshooting — 12%

### Classify before fixing

A syntax error prevents valid parsing. A semantic/runtime failure occurs when an operation cannot be performed as executed. A logic error runs but produces the wrong result. The public scope names `SyntaxError`, `ReferenceError`, `TypeError`, and `RangeError`:

- malformed syntax can produce `SyntaxError`;
- using an unresolved identifier can produce `ReferenceError`;
- performing an unsupported operation for a value can produce `TypeError`;
- a value outside an allowed numeric range for an operation can produce `RangeError`.

The exact exception depends on the operation, so reproduce a minimal case rather than guessing from a symptom.

### Handling and throwing

Place operations that may throw inside `try`; use `catch` to inspect and handle an exception; use `finally` for work that must run whether completion or throwing occurs. `throw` raises a supplied value, though using `Error` objects preserves useful message and stack conventions.

Do not catch every exception merely to hide it. Handle where you can recover, add context, select a deliberate fallback, or rethrow. Validation failures you anticipate can be represented deliberately; programmer defects should remain visible.

### A reproducible debugging loop

Reduce the failing input, state the expected and actual results, read the first relevant console error and stack location, set a breakpoint before divergence, step over or into deliberately, inspect variables and the call stack, and change one cause. Use `console.time`/`console.timeEnd` or the environment's performance tools for measurements, not intuition. Modifying a value in the debugger is an experiment, not a source-code fix.

> **Related item:** A regression check records the input that exposed a defect and the expected result after repair. Even before a formal test framework, rerunning that case prevents the same bug from silently returning.

## Integrated scenarios

### Scenario 1: Browser order quote

Use `prompt` for quantity and tier, distinguish cancel/blank/invalid/zero, convert deliberately, choose a rate, and build an order object. Store objects in an array and calculate totals through functions. Use `confirm` before committing and `alert` only for the final tiny-demo result. Test every tier boundary, aliasing, and input state.

### Scenario 2: Timed quiz

Represent questions as object records in an array, traverse values with `for...of`, and score answers in a callback-driven function. Schedule a one-time warning and a repeating elapsed-time display, retaining identifiers so both can be cleared. Trace synchronous setup, queued callbacks, completion, timeout, cancellation, and a callback that throws.

### Scenario 3: Inventory debugger

Read an item code, enumerate a record's keys with `for...in`, search an array of item objects, and update stock through a function. Intentionally isolate one syntax, reference, type, range, and logic failure. For each, capture expected/actual state, stack evidence, breakpoint observations, root cause, fix, and regression input.

## Hands-on labs

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
5. `let`/`const` are block scoped, `var` function scoped; `let`/`var` can be rebound while `const` cannot.
6. `const` fixes the binding, not the referenced object's internal state.
7. An inner binding with the same name hides a distinct outer binding.
8. A `ReferenceError` is thrown.
9. `undefined` before its declaration assignment executes.
10. Boolean, number, bigint, undefined, null, and string.
11. The historical string result `"object"`.
12. They are separate numeric types and arithmetic mixing requires deliberate conversion.
13. `undefined` often means absent/not supplied; `null` is an explicit null value.
14. Conversion changes representation; validation decides whether the original/converted input is acceptable.
15. `false`, `0`, `-0`, `0n`, empty string, `null`, `undefined`, and `NaN`.
16. It normally evaluates to `undefined`.
17. Dot uses a literal name; brackets can evaluate a key expression.
18. The reference, so both variables can designate the same object.
19. It avoids implicit type coercion while comparing.
20. One of their operand values, chosen through short-circuit evaluation.
21. `instanceof` checks an object/prototype relationship; `typeof` reports broad value categories, with known boundaries.
22. An object property when deletion is permitted.
23. `alert` → `undefined`; `confirm` → Boolean; `prompt` → string or `null`.
24. Check for `null`/blank before numeric conversion; preserve valid zero as data.
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
36. The callback waits for at least the threshold and for current work/earlier tasks to finish.
37. Invalid syntax; unresolved identifier; operation incompatible with a value; and an operation-specific out-of-range value.
38. After the `try`/`catch` path whether normal completion or throwing occurs, subject to abrupt environment termination.
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
| [OpenEDG JavaScript Essentials 1](https://jsinstitute.org/javascript-essentials-1) | Free account; officially aligned | 40 hours listed |
| [Cisco Networking Academy JavaScript Essentials 1](https://www.netacad.com/courses/javascript-essentials-1) | Free account; official partner delivery | Plan about 40 hours; verify live listing |
| [MDN Dynamic Scripting with JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting) | Free current tutorials and checks | 15–25 hours for JSE-relevant portions |
| [Microsoft Beginner's Series to JavaScript](https://learn.microsoft.com/en-us/shows/beginners-series-to-javascript/) | Free 51-part video series; Node.js-oriented | About 4–6 hours plus code practice |
| [Pluralsight Professional JavaScript path](https://www.pluralsight.com/paths/javascript-2022) | Subscription; 79-hour broad path | Select 6h08 fundamentals plus 3–6 hours of matching labs |
| [O'Reilly JavaScript: The Definitive Guide, 7th Edition](https://www.oreilly.com/library/view/javascript-the-definitive/9781491952016/) | Subscription; 21h15m, broader and deeper | Select chapters 1–5 and debugging/timers, 8–12 hours |
| [Udemy Complete JavaScript Course by Jonas Schmedtmann](https://www.udemy.com/course/the-complete-javascript-course/) | Paid marketplace course; 71h10m listed | Select Fundamentals 1–2 and debugging/timers, 12–18 hours |
| [freeCodeCamp Learn JavaScript — Full Course for Beginners](https://www.youtube.com/watch?v=PkZNo7MFNFg) | Free popular video; older overview | About 3h27m plus coding time |

No exact current MeasureUp or Whizlabs JSE-40-01 product was verified. The OpenEDG practice kit explicitly identifies the active version; avoid third-party practice that does not state its blueprint and provenance.
