---
exam_code: JSA-41-01
vendor_id: js-institute
official_blueprint: https://jsinstitute.org/jsa-exam-syllabus
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# JSA-41-01 Certified Associate JavaScript Programmer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Selected public sources and all 40 numbered objectives were reviewed September 29, 2026. Original code was executed in existing Node and Chrome runtimes. Direct official-page fetching failed; indexed public content supported manual scope comparison. Paid interiors and human review remain pending. This is not a guarantee that every explanation is error-free or that the provider will not change the exam. Recheck the [official JSA certification page](https://jsinstitute.org/jsa-certification) and [JSA-41-01 syllabus](https://jsinstitute.org/jsa-exam-syllabus) before scheduling.

**Current baseline:** JSA-41-01, active; syllabus last updated September 22, 2025<br>
**Upcoming blueprint change:** none announced on the official exam, syllabus, or certification-overview pages when checked; no unseen announcement feed or booking availability was verified<br>
**Official delivery snapshot:** 40 single- and multiple-select items; 60-minute exam plus 5-minute tutorial/NDA; 70% cumulative normalized passing score; English and Spanish, with the overview qualifying Spanish as TestNow delivery<br>
**Purchase snapshot:** no formal prerequisite; JSE-40-01 recommended; exam from USD 295 and exam-plus-retake from USD 345 when checked; delivery through TestNow, OnVUE, or a Pearson VUE test center<br>

The official [TestNow policy](https://jsinstitute.org/test-now-testing-policies) states seven days after failure; the [Pearson VUE policy](https://jsinstitute.org/pvue-testing-policies) states fifteen and disallows retaking the same passed version. Keep delivery channels separate. Pearson's free-retake eligibility wording and the exam/retake bundle prices do not establish your voucher's actual terms; verify the selected product before purchase. No account, checkout or booking was entered. The certification page contains an unrelated Python credential label in one row; it does not redefine this JavaScript exam. No current credential-expiration claim is inferred from silence.

## How to use this guide

JSA is a code-reasoning exam, not a framework exam. Build small programs in a modern browser or current Node.js runtime, predict their output first, and use the console/debugger only after writing down your reasoning. For every object, draw its own properties and prototype link. For every callback or promise, draw the order in which synchronous work, fulfillment/rejection handlers, and later work can run.

Use four passes:

1. map every syllabus objective to a runnable example;
2. predict value, identity, receiver, mutation, iteration order, or asynchronous outcome;
3. change one boundary—missing property, inherited property, invalid date, empty collection, rejection, or network failure;
4. explain why the result follows from the language/API rather than memorizing output.

The scope includes both classless/prototype techniques and classes. It also includes legacy `XMLHttpRequest` beside Fetch. Know why each works, but favor maintainable modern patterns in new application code.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Objective map and study emphasis

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| 1. Classless Objects | 11 | 25% | Create, enumerate, clone, configure, and inherit objects while explaining identity and `this` |
| 2. Classes and Class-Based Approach | 7 | 23% | Implement construction, fields, accessors, inheritance, statics, and equivalent prototype mechanics |
| 3. Built-in Objects | 12 | 27% | Select and correctly apply Number, String, Date, Array, Set, Map, JSON, Math, and RegExp APIs |
| 4. Advanced Functions | 10 | 25% | Use parameters, closures, context, decorators, iteration protocols, callbacks, promises, async/await, and HTTP requests |

These item counts and weights are published in the official syllabus. The 40 numbered objectives fall into groups of 11/7/12/10. The retained snapshot abbreviates identifiers such as `1.1.1` to `1.1`; the subject mapping was compared manually with the complete indexed current English syllabus after automated monitoring failed. Existing snapshots were retained. The older 2022 PDF was only partially visible and is not used to replace the September 2025 baseline.

Every named objective matters. Weights, item counts and the normalized 70% threshold do not imply that exactly 28 equally weighted correct answers will always pass.

## 1. Classless objects — 25%

### Object creation, properties, and notation

An object literal creates an ordinary object directly. A factory is a normal function that returns an object. A constructor function is called with `new`, which creates an object linked to the constructor's `prototype`, binds `this`, and normally returns the new object. `Object.create(proto)` creates an object with an explicit prototype. Be able to recognize all four and select the simplest appropriate mechanism.

Dot notation requires a valid identifier known in source; brackets evaluate a key. Brackets therefore handle spaces, hyphens, user-selected keys, and computed names. Optional chaining such as `record.profile?.name` stops at `null` or `undefined`, but it does not prove that a property is an own property.

The `in` operator searches the object and its prototype chain. `Object.hasOwn(object, key)` checks only the object's own property. `for...in` enumerates enumerable string keys from the object and its prototypes, so filter it when inherited properties are not intended. `Object.keys`, `Object.values`, and `Object.entries` return arrays for enumerable own string-keyed properties.

```javascript
const product = { id: "A1", details: { stock: 4 } };
const field = "unit-price";
product[field] = 12.5;

for (const [key, value] of Object.entries(product)) {
  console.log(key, value);
}
```

The [MDN guide to working with objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects) is the best live reference for these behaviors.

### Identity, copying, and cloning

Object equality compares identity. Two distinct objects with equal-looking properties are not strictly equal. Assignment copies a reference, so mutations through one alias are visible through the other.

Object spread and `Object.assign` make shallow copies: they copy selected own enumerable properties, but nested objects remain shared. A general deep clone is not equivalent to `JSON.parse(JSON.stringify(value))`; JSON loses unsupported values and cannot represent cycles. `structuredClone` is useful related platform context and supports many structured-clone types, but still has defined limitations. For exam questions, identify exactly which layer is copied. Both spread and `Object.assign` read source getters and can materialize their values. `Object.assign` also uses assignment on the target, so it can invoke target setters and can leave earlier writes behind if a later write throws; object spread defines new own properties. Neither operation is a general descriptor-preserving copy. See [Object.assign](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign).

### Methods, receivers, and accessors

`this` for an ordinary function is determined by how it is called. In `account.deposit(5)`, `account` is the receiver. Extracting the same function and calling it separately loses that receiver. Arrow functions capture lexical `this` and are therefore usually the wrong choice for an object method that needs its calling object.

Getters expose a zero-argument computation with property syntax. Setters receive one assigned value and can validate or normalize it. Avoid a getter and setter recursively reading/writing their own public property; use a distinct backing property or private field.

### Descriptors and mutability controls

A property descriptor controls value/get/set plus flags such as `writable`, `enumerable`, and `configurable`. Ordinary properties created by an object literal or assignment are writable, enumerable, and configurable; flags omitted when `Object.defineProperty` creates a **new** property default to `false`. For an **existing** property, omitted attributes retain their current values. A descriptor cannot mix `value`/`writable` with `get`/`set`. A non-configurable writable data property may still change value and may become non-writable; after that it cannot be made writable again.

- `Object.preventExtensions` blocks new own properties.
- `Object.seal` prevents extension and makes existing properties non-configurable, while writable data properties can still change.
- `Object.freeze` also makes own data properties non-writable.

These operations are shallow. Freezing a container does not recursively freeze nested objects, and an existing accessor setter may still change other state. Failed writes/deletes generally throw in strict mode; some corresponding sloppy-mode operations fail silently. Read [descriptor rules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty) and [freeze boundaries](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze), then predict both the property and its nested state.

### Prototypes

Property lookup starts with the object, then follows its internal `[[Prototype]]` chain. Constructor functions expose a `.prototype` object used for instances created with `new`; the constructor function's own prototype is a different relationship. `__proto__` is a legacy accessor—recognize it, but prefer `Object.getPrototypeOf`, `Object.create`, and deliberate construction.

Changing an established object's prototype with `Object.setPrototypeOf` can harm optimization and make behavior harder to reason about. Prefer creating it with the intended prototype. `Object.create(null)` is a valid exception to the informal claim that every object inherits from another object: it has no inherited `toString` or `hasOwnProperty`. Use `Object.hasOwn(dictionary, key)`. An own `"__proto__"` key on such a dictionary is ordinary data. See [Object.create](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create).

> **Related item:** Prototype delegation is dynamic: an inherited property added to a prototype can become visible to existing descendants. An own property with the same key shadows the inherited property rather than changing it.

## 2. Classes and the class-based approach — 23%

### Declarations, fields, and instances

A class is a special function-based construct built on prototypes. A class declaration or expression can contain a constructor, methods, getters/setters, fields, and static members. Methods are shared through the prototype; instance fields are initialized for each instance. Classes can be stored and passed as values, but class declarations have temporal-dead-zone behavior and class bodies run in strict mode.

`new Type(args)` creates and initializes an instance. `instanceof` checks whether `Type.prototype` appears in the object's prototype chain; it is not a structural shape check and can be affected by realms or prototype changes.

```javascript
class Account {
  currency = "USD";

  constructor(owner, balance = 0) {
    this.owner = owner;
    this.balance = balance;
  }

  get available() { return this.balance; }
  deposit(amount) { this.balance += amount; }
  static from(record) { return new Account(record.owner, record.balance); }
}
```

This small `Account` illustrates placement of fields, methods and a static factory; it deliberately omits input validation and financial rules. The complete catalog scenario below supplies explicit bounds. Class field initializers run for each new instance, so a field initialized with `[]` is not a shared prototype array. A class expression can be assigned, passed or returned like another value.

### Inheritance, overriding, and `super`

`class PremiumAccount extends Account` links both instance and constructor inheritance. A derived constructor must call `super(...)` before accessing `this`. An overriding method replaces inherited behavior for that lookup; `super.method()` deliberately invokes the parent implementation using the current receiver.

Static members belong to the constructor/class, not each instance. A subclass can inherit static members through the constructor chain. Choose inheritance only for a genuine substitutable relationship; composition is related design context but not a replacement for knowing `extends` mechanics.

The [MDN classes guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes) covers declarations, fields, private elements, inheritance, and evaluation behavior. Private fields are useful modern context, but they are not named in this public syllabus.

### Classes versus constructors

Class syntax organizes the same broad prototype model used by constructor functions, but it is not merely textual sugar in every detail. Class calls require `new`, methods are non-enumerable, bodies are strict, and initialization rules differ. Be able to translate the essential shape:

```javascript
function Account(owner) {
  this.owner = owner;
}
Account.prototype.describe = function () {
  return this.owner;
};
```

The analogous class constructor initializes own state and its method declaration installs shared behavior on the class prototype.

## 3. Built-in objects — 27%

### Number, String, and Date

`Number(value)` converts; `new Number(value)` creates a wrapper object and is rarely desirable. Distinguish `Number.isNaN` and `Number.isFinite`, which do not coerce, from global legacy checks that can. Formatting methods such as `toFixed` return strings. Numeric text and floating-point results need explicit validation and a stated precision policy. `Number("")` and whitespace-only text become zero, so successful conversion does not prove valid input. `Number.isSafeInteger` rejects integers outside the safe range; `Number.MIN_VALUE` is the smallest positive representable value, not the most negative number. `Number.EPSILON` is the gap between 1 and the next larger representable number, not a universal tolerance at every magnitude. The [Number reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number) distinguishes encoding, coercion and checking.

Strings are immutable. Indexing and methods produce values rather than editing characters in place. Know case conversion, `split`, inclusion/index search, `replace`, padding, trimming, and comparison. `localeCompare` provides locale-aware ordering context; simple relational comparison follows code-unit ordering. String length, indexing and `split("")` operate on UTF-16 code units: `"🚀".length` is 2, while `[..."🚀"].length` is 1 because iteration follows code points. Neither count universally equals visible grapheme count. A string search passed to `replace` replaces the first match; a global regex can replace all matches. See [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String).

`Date` represents an instant as milliseconds from the epoch, while getters/setters interpret it in local time or UTC depending on method family. Parsing non-standard date strings is unreliable; prefer defined formats or numeric components. The month component is zero-based. An invalid date normally holds `NaN`; a finite timestamp alone does not prove that an entered calendar date was real because component overflow can normalize. Standard date-only text implies UTC, while a standard date-time without a zone is interpreted locally. Use UTC methods consistently for a UTC contract and round-trip a strict date-only input as the normalization scenario does. A timestamp difference measures elapsed wall-clock time but `performance.now()` is better related context for monotonic duration measurements. See [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date).

### Arrays and functional methods

Know which methods mutate: `push`, `pop`, `shift`, `unshift`, `splice`, `sort`, and `reverse` mutate the array. `slice`, `concat`, spread, `map`, and `filter` produce new arrays (with shallow element copies). Destructuring binds selected positions and rest values.

- `find` returns the first matching value or `undefined`.
- `every` requires all elements and is true for an empty array.
- `some` requires at least one and is false for an empty array.
- `filter` retains matches.
- `map` transforms each visited element; it skips missing array slots.
- `reduce` accumulates; an explicit initial value avoids empty-array and type surprises.
- Default `sort` compares string forms; numeric sorting needs a comparator such as `(a, b) => a - b`.

An empty slot differs from a present property whose value is `undefined`. `map`, `filter`, `every`, `some` and `reduce` skip holes; `find` visits them as `undefined`. `map` preserves holes, while spreading an array creates present `undefined` entries. Callbacks receive more than just the value: `array.map(parseInt)` accidentally passes the index as the radix. Use an explicit callback such as `text => parseInt(text, 10)` when that is the intended contract. Iterative methods generally capture the initial length but observe values when visited; avoid mutating the traversed array without a deliberate reason. See [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array).

### Set, Map, and plain dictionaries

`Set` stores unique values and preserves insertion order. `Map` associates arbitrary key values with values and preserves insertion order. Both expose `size`, iteration, membership, addition/update, deletion, and clearing. Plain objects remain convenient for string/symbol-keyed records, but have prototype and property-enumeration semantics. [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) and [Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) use SameValueZero: repeated `NaN` values match and `+0`/`-0` match; distinct object identities remain distinct. Updating an existing Map key preserves its position; deleting and reinserting moves it to the end. A missing key and a key mapped to `undefined` require `has` to distinguish. `set`/`add` return the collection; `delete` returns whether an entry existed; `clear` empties it. An ordinary object coerces most property keys to strings and has its own enumeration ordering rules. Select based on the required keys and contract, rather than claiming every collection has identical ordering or guaranteed constant-time operations.

### JSON, Math, regular expressions, and built-in extension

`JSON.stringify` serializes supported data to text; `JSON.parse` creates values from valid JSON text. JSON has no functions, `undefined`, BigInt, Map, Set, or reference cycles. Replacer/reviver hooks are useful deeper context. Never treat parsing as schema validation: `null`, a number or an array can be valid JSON. Without customization, unsupported object-property values such as `undefined` or functions are omitted; unsupported array entries and non-finite numbers become `null`; a top-level `undefined` produces no JSON string. Map/Set typically become `{}`, dates use their `toJSON` conversion, and cycles or BigInt throw unless a deliberate supported conversion handles them. See [JSON.stringify](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify).

Know common `Math` operations: rounding directions, absolute value, min/max, exponentiation/logs, trigonometry, and pseudorandom values. `Math.random` is not cryptographically secure and its output must be scaled carefully for integer ranges. It returns a number in `[0, 1)`; a handful of range checks is not a statistical or security assessment. Arbitrary scaling can incur floating-point endpoint rounding. `Math.floor` rounds toward negative infinity, `ceil` toward positive infinity, and `round` breaks a half tie toward positive infinity: `Math.round(-2.5)` is `-2`, with negative zero possible near zero. Trigonometric inputs use radians. See [Math](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math), [round](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/round) and [random](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random).

A regular-expression literal compiles a pattern in source; `new RegExp(text, flags)` supports dynamic patterns and needs additional string escaping. Understand character classes, quantifiers, anchors, grouping, flags, and the return differences of `test`, `exec`, `match`, `search`, and `replace`. Avoid unnecessarily complex patterns and test boundaries. Regex objects with `g` or `y` carry state in `lastIndex`, including across calls on different strings; a failed match resets it. A reused global `test` can therefore surprise you. Use a non-global validation regex or deliberately reset state. `exec` yields a match object with captures or `null`; repeated zero-length matches need explicit advancement to avoid an endless loop. See [RegExp.exec](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec).

Adding methods to standard built-in prototypes can collide with future platform additions, affect enumeration, and surprise other code. Prefer standalone functions, subclasses where genuinely appropriate, or application-owned prototypes.

The [MDN built-in object reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects) provides current API semantics and edge cases.

> **Related item:** Time zones, locale formatting, Unicode text, secure random generation, and schema validation are production concerns adjacent to this block. Learn the exam APIs first, then identify where application requirements demand a more specialized API or library.

## 4. Advanced functions — 25%

### Parameters, closures, context, and wrappers

Default parameters apply when an argument is missing or `undefined`, not for every falsy value. A rest parameter collects remaining arguments into an array and must be last. Spread expands an iterable into arguments. Destructured object parameters support a readable named-argument pattern and can carry defaults.

A closure is a function plus access to the lexical environment where it was created. Each factory call can therefore retain independent private state. A closure retains access to bindings, not an automatic frozen snapshot of their values; later reassignment can change what it observes. An IIFE executes a function expression immediately; modules and blocks often replace its historical namespace role, but recognize the pattern.

`call` invokes now with an explicit receiver and separate arguments. `apply` invokes now with an explicit receiver and an array-like argument list. `bind` returns a new function with a bound receiver and optional leading arguments. Calling a bound ordinary function with another receiver does not replace its stored receiver. Arrows already retain lexical `this`; `call`/`apply`/`bind` cannot change it. When a constructable bound function is called with `new`, construction supplies a new receiver and ignores the bound receiver while retaining leading arguments. See [Function.bind](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind).

A decorator/wrapper accepts a function and returns or exposes enhanced behavior such as logging, caching, timing, validation, or retry. Preserve the receiver, arguments, return value, and error behavior unless the wrapper intentionally changes the contract.

### Generators and iteration protocols

A generator function (`function*`) returns an iterator. Each `next()` resumes until `yield` or completion and returns `{ value, done }`. An iterable exposes `[Symbol.iterator]()` that returns an iterator. `for...of` and spread consume iterables. Keep “iterable” (provides an iterator through `Symbol.iterator`) distinct from “iterator” (has `next`). A generator object is both and returns itself from its iterator method, so consuming it exhausts that same object. A reusable iterable can return a fresh generator each time. A generator's `return` value appears with `done: true` and is not a yielded value consumed by `for...of` or spread. Early loop exit calls an iterator's `return` when available, allowing generator `finally` cleanup. See [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).

### Callbacks, promises, and async/await

Callbacks can represent later completion, but contracts must define success, failure, and whether a callback may run more than once. Nested callbacks make sequencing and error propagation difficult. An outer `try/catch` around registration does not catch an exception thrown later in a timer callback. A promise adapter must turn the callback's explicit error into rejection; a later uncaught callback throw is not magically caught by the earlier promise executor.

A promise is pending and then settles exactly once as fulfilled or rejected. `then` returns a new promise, which enables flattening chains when handlers return values or promises. `catch` handles rejection in the preceding chain; `finally` observes settlement without normally replacing the value/reason. A `catch` that returns a value recovers; rethrow to keep failure. Return a dependent promise from `then` so the chain waits for it. `finally` gets no result argument; an ordinary return value is ignored, but a throw or returned rejection replaces the prior outcome, and a returned pending promise delays completion. See [Promise.finally](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally).

- `Promise.all` fulfills with ordered results when all fulfill and rejects on the first observed rejection.
- `Promise.any` fulfills on the first fulfillment and rejects with an aggregate if all reject.
- `Promise.race` settles with the first settled input.

For empty input, [all](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all) fulfills with `[]`, [any](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/any) rejects with `AggregateError`, and [race](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race) remains pending. Even an already-settled promise runs newly registered reactions asynchronously. All results and `any` aggregate errors follow input order, not completion order. These combinators do not cancel remaining operations; cancellation belongs to the underlying API.

An `async` function always returns a promise. `await` pauses that async function until a promise settles; it does not block the entire runtime. Use `try/catch` around awaited failures you can handle. Independent operations can start together before awaiting their aggregate; blindly awaiting each in sequence can add latency. Its body begins synchronously and runs up to the first suspension. Returning an existing promise adopts its eventual outcome but does not return that exact promise object. Attach aggregate handling promptly when operations start together: awaiting already-started promises one at a time can leave an earlier rejection temporarily unhandled. Concurrency still needs product-specific limits and is not automatically preferable for dependent or rate-limited work.

See [MDN Using promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises) and [MDN async functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function).

### Network requests

`XMLHttpRequest` exposes an event/callback-based request lifecycle. Fetch returns a promise for a `Response`. Fetch normally rejects for network/request failures, not merely for HTTP 404 or 500, so check `response.ok` or `status` before parsing. Body-reading methods are asynchronous and a body is generally consumed once. Handle cancellation, timeouts, content types, parsing errors, and user-visible failure states deliberately.

The complete client below separates HTTP status, content type, JSON syntax and record shape. For XHR, `load` means the transfer ended, not that its HTTP status succeeded; handle `error`, `abort` and `timeout` separately. [XHR timeout](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/timeout) defaults to zero, meaning no timeout. Use asynchronous XHR to avoid blocking the document. [AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController) can cancel a Fetch request and body consumption; an already-aborted signal cannot be reused for a new attempt.

For cross-origin requests, browser access depends on CORS. Fetch `mode: "no-cors"` does not make a protected JSON response readable: an opaque response hides its body and exposes status zero. The [XHR guide](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest_API/Using_XMLHttpRequest) covers its event lifecycle; the executed scenario uses controlled same-origin fixtures, so it does not prove a deployed CORS configuration.

[MDN Using the Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) documents the live browser contract.

> **Related item:** Promise handlers run as microtasks, while timer callbacks are scheduled as tasks. Exact event-loop terminology goes beyond the objective wording, but it explains why promise reactions commonly run before an already-eligible timeout after synchronous code completes.

## Executed core workbook

Run this original workbook as a fresh script in a modern browser page or Node, then inspect `await jsaCore` (or `jsaCore.then(console.log)`). It passed **143 named checks** on existing Node 24.18.1 and Chrome 154.0.8037.58. The workbook briefly adds a unique, non-enumerable symbol to `Array.prototype` in a disposable runtime and removes it in `finally`; this illustrates the syllabus mechanism, not a recommendation to modify shared production prototypes. Its JSON equality helper is used only for the simple supported arrays/results shown, not as a general deep comparator. The empty-race sentinel checks an observation; the documented promise contract explains permanent pending state.

```javascript
globalThis.jsaCore = (async () => {
  "use strict";
  const passed = [];
  function check(name, condition) {
    if (!condition) throw new Error(name);
    passed.push(name);
  }
  function raises(fn, Type) {
    try { fn(); } catch (error) { return error instanceof Type; }
    return false;
  }
  async function rejects(promise, Type) {
    try { await promise; } catch (error) { return error instanceof Type; }
    return false;
  }
  const same = (a, b) => JSON.stringify(a) === JSON.stringify(b);

  const parent = { inherited: 7 };
  const row = Object.create(parent);
  row["unit-price"] = 25;
  row.details = { stock: 2 };
  check("computed own key", row["unit-price"] === 25);
  check("in searches ancestors", "inherited" in row);
  check("hasOwn excludes ancestors", !Object.hasOwn(row, "inherited"));
  check("keys excludes ancestors", same(Object.keys(row), ["unit-price", "details"]));
  const seen = []; for (const key in row) seen.push(key);
  check("for-in includes enumerable ancestor", seen.includes("inherited"));
  check("missing optional path", row.absent?.value === undefined);
  row.inherited = 9;
  check("shadowing leaves parent", row.inherited === 9 && parent.inherited === 7);
  delete row.inherited;
  check("delete reveals inherited value", row.inherited === 7);
  const copy = { ...row };
  check("copy has distinct identity", copy !== row);
  check("nested alias remains", copy.details === row.details);
  check("copy does not copy prototype", Object.getPrototypeOf(copy) === Object.prototype);
  check("empty literals differ", {} !== {});
  const dictionary = Object.create(null);
  dictionary.__proto__ = 4;
  check("null prototype dictionary", Object.getPrototypeOf(dictionary) === null);
  check("special-looking dictionary key", Object.hasOwn(dictionary, "__proto__") && dictionary.__proto__ === 4);

  const fresh = {};
  Object.defineProperty(fresh, "code", { value: "K8" });
  const flags = Object.getOwnPropertyDescriptor(fresh, "code");
  check("new descriptor false defaults", !flags.writable && !flags.enumerable && !flags.configurable);
  check("strict write to readonly throws", raises(() => { fresh.code = "other"; }, TypeError));
  const existing = { count: 1 };
  Object.defineProperty(existing, "count", { value: 3 });
  check("existing omitted flags preserved", Object.getOwnPropertyDescriptor(existing, "count").writable);
  check("data and accessor descriptors cannot mix", raises(() => Object.defineProperty({}, "x", { value: 1, get() { return 2; } }), TypeError));
  Object.defineProperty(existing, "count", { configurable: false });
  existing.count = 4;
  check("nonconfigurable may still be writable", existing.count === 4);
  Object.defineProperty(existing, "count", { writable: false });
  check("cannot restore writable after lock", raises(() => Object.defineProperty(existing, "count", { writable: true }), TypeError));
  const sealed = Object.seal({ count: 1 }); sealed.count = 2;
  check("seal permits existing writable value", sealed.count === 2);
  check("seal blocks delete", raises(() => { delete sealed.count; }, TypeError));
  const stopped = Object.preventExtensions({ count: 1 }); delete stopped.count;
  check("preventExtensions still permits delete", !Object.hasOwn(stopped, "count"));
  check("preventExtensions blocks addition", raises(() => { stopped.next = 1; }, TypeError));
  const frozen = Object.freeze({ nested: { count: 1 } }); frozen.nested.count = 5;
  check("freeze is shallow", frozen.nested.count === 5);
  let stored = 1;
  const accessor = Object.freeze({ get x() { return stored; }, set x(v) { stored = v; } });
  accessor.x = 8;
  check("freeze does not disable setter", accessor.x === 8);
  let reads = 0; const source = { get total() { reads++; return 12; } };
  const target = { set total(v) { this.observed = v; } };
  Object.assign(target, source);
  check("assign invokes getter and target setter", reads === 1 && target.observed === 12);
  const spread = { ...source };
  check("spread materializes accessor value", reads === 2 && Object.getOwnPropertyDescriptor(spread, "total").value === 12);
  const partial = {}; Object.defineProperty(partial, "locked", { value: 1 });
  check("assign may throw after partial write", raises(() => Object.assign(partial, { before: 2, locked: 3 }), TypeError) && partial.before === 2);

  const receiver = { base: 4, add(n) { return this.base + n; } };
  check("method receiver", receiver.add(3) === 7);
  const detached = receiver.add;
  check("detached strict receiver", raises(() => detached(3), TypeError));
  check("call receiver", detached.call({ base: 9 }, 2) === 11);
  check("apply array-like arguments", detached.apply(receiver, { 0: 5, length: 1 }) === 9);
  const bound = detached.bind(receiver, 6);
  check("bound receiver cannot be rebound", bound.call({ base: 99 }) === 10);
  function arrowFactory() { return () => this.base; }
  check("arrow retains lexical receiver", arrowFactory.call(receiver).call({ base: 99 }) === 4);
  function Token(value) { this.value = value; }
  Token.prototype.describe = function () { return this.value; };
  const token = new Token("T");
  check("constructor instance link", Object.getPrototypeOf(token) === Token.prototype);
  check("function object has separate link", Object.getPrototypeOf(Token) === Function.prototype);
  const BoundToken = Token.bind({ unused: true }, "B");
  check("new ignores bound receiver", new BoundToken().value === "B");
  class Base {
    tags = [];
    constructor(n) { this.n = n; }
    get doubled() { return this.n * 2; }
    label() { return `B${this.n}`; }
    static from(n) { return new this(n); }
  }
  class Child extends Base { label() { return super.label() + "!"; } }
  const child = Child.from(3);
  check("static factory preserves subclass", child instanceof Child && child instanceof Base);
  check("super keeps current receiver", child.label() === "B3!");
  check("getter computes", child.doubled === 6);
  check("instance field belongs to instance", Object.hasOwn(child, "tags"));
  check("field initializer creates independent array", child.tags !== new Base(1).tags);
  check("class methods on prototype", !Object.hasOwn(child, "label") && Object.hasOwn(Child.prototype, "label"));
  check("class methods not enumerable", !Object.getOwnPropertyDescriptor(Child.prototype, "label").enumerable);
  check("static not instance method", typeof Child.from === "function" && child.from === undefined);
  check("class requires new", raises(() => Base(1), TypeError));
  check("class lexical binding has TDZ", raises(() => { const before = Later; class Later {} return before; }, ReferenceError));
  check("derived this requires super", raises(() => { class Bad extends Base { constructor() { this.n = 1; } } return new Bad(); }, ReferenceError));
  check("class expression is a value", new (class { x = 6; })().x === 6);

  check("blank numeric conversion", Number("") === 0 && Number("  ") === 0);
  check("Number checks do not coerce", !Number.isFinite("12") && !Number.isNaN("bad"));
  check("actual NaN recognized", Number.isNaN(Number("bad")));
  check("wrapper is truthy object", Boolean(new Number(0)) && typeof new Number(0) === "object");
  check("safe integer boundary", Number.isSafeInteger(2 ** 53 - 1) && !Number.isSafeInteger(2 ** 53));
  check("MIN_VALUE is positive", Number.MIN_VALUE > 0);
  check("EPSILON is gap at one", 1 + Number.EPSILON > 1 && 1 + Number.EPSILON / 2 === 1);
  check("toFixed returns string", (12.5).toFixed(2) === "12.50");
  check("UTF16 length differs from codepoints", "A🚀".length === 3 && [..."A🚀"].length === 2);
  check("split empty uses code units", "🚀".split("").length === 2);
  check("string transforms preserve original", " Ab ".trim().toUpperCase() === "AB");
  check("replace literal replaces first", "aa".replace("a", "b") === "ba");
  check("replace global replaces both", "aa".replace(/a/g, "b") === "bb");
  check("string padding and search", "7".padStart(3, "0") === "007" && "catalog".includes("log"));
  check("string comparison", "12" < "3");
  const day = new Date("2024-02-29T00:00:00Z");
  check("UTC month is zero based", day.getUTCMonth() === 1 && day.getUTCDate() === 29);
  day.setUTCDate(day.getUTCDate() + 1);
  check("date component carry", day.toISOString() === "2024-03-01T00:00:00.000Z");
  check("invalid date timestamp", Number.isNaN(new Date("not-a-date").getTime()));
  check("date-only standard text is UTC", new Date("2024-03-01").getTime() === Date.UTC(2024, 2, 1));
  const values = [8, 12, 2];
  check("default sort uses strings", same([...values].sort(), [12, 2, 8]));
  check("numeric sort comparator", same([...values].sort((a, b) => a - b), [2, 8, 12]));
  check("some/every empty", ![].some(Boolean) && [].every(Boolean));
  check("empty reduce needs initial value", raises(() => [].reduce((a, b) => a + b), TypeError) && [].reduce((a, b) => a + b, 0) === 0);
  const holes = new Array(2); let visits = 0;
  const mapped = holes.map(() => { visits++; return 1; });
  check("map skips holes and preserves them", visits === 0 && mapped.length === 2 && !(0 in mapped));
  check("spread materializes holes", 0 in [...holes] && [...holes][0] === undefined);
  holes.find(() => { visits++; return false; });
  check("find visits holes", visits === 2);
  check("parseInt map callback trap", same(["10", "10", "10"].map(v => parseInt(v, 10)), [10, 10, 10]) && Number.isNaN(["10", "10"].map(parseInt)[1]));
  const edited = [1, 2, 3]; const removed = edited.splice(1, 1, 7);
  check("splice edits and returns removed", same(edited, [1, 7, 3]) && same(removed, [2]));
  check("slice leaves source", same(edited.slice(1), [7, 3]) && edited.length === 3);
  check("map filter reduce pipeline", values.filter(v => v > 2).map(v => v / 2).reduce((a, b) => a + b, 0) === 10);
  const key1 = {}, key2 = {}; const map = new Map([[key1, 1], [key2, 2], [NaN, 3]]);
  check("Map object keys use identity", map.size === 3 && map.get(key1) === 1 && map.get({}) === undefined);
  check("Map NaN key", map.get(NaN) === 3);
  map.set(key1, 8);
  check("Map update preserves position", [...map.keys()][0] === key1);
  map.delete(key1); map.set(key1, 9);
  check("Map reinsert moves to end", [...map.keys()].at(-1) === key1);
  map.clear(); check("Map clear", map.size === 0);
  const set = new Set([NaN, NaN, -0, +0, key1, key2]);
  check("Set SameValueZero plus identity", set.size === 4);
  check("Set delete and membership", set.delete(key1) && !set.has(key1));
  set.add("last"); check("Set iteration order", [...set].at(-1) === "last");
  set.clear(); check("Set clear", set.size === 0);
  check("JSON unsupported object values omitted", JSON.stringify({ a: undefined, b() {}, c: Symbol() }) === "{}");
  check("JSON unsupported array values null", JSON.stringify([undefined, NaN, Infinity]) === "[null,null,null]");
  check("JSON unsupported root undefined", JSON.stringify(undefined) === undefined);
  check("JSON Map is empty without conversion", JSON.stringify(new Map([["a", 1]])) === "{}");
  check("JSON BigInt rejects without custom conversion", raises(() => JSON.stringify(1n), TypeError));
  const cycle = {}; cycle.self = cycle;
  check("JSON cycle rejects", raises(() => JSON.stringify(cycle), TypeError));
  check("parse does not require object", JSON.parse("null") === null && JSON.parse("4") === 4);
  check("JSON malformed rejects", raises(() => JSON.parse("{bad}"), SyntaxError));
  check("round negative tie toward positive", Math.round(-2.5) === -2);
  check("round preserves negative zero", Object.is(Math.round(-0.1), -0));
  check("floor and ceil", Math.floor(-2.2) === -3 && Math.ceil(-2.2) === -2);
  check("Math range and powers", Math.min(3, 7) === 3 && Math.max(3, 7) === 7 && Math.abs(-3) === 3 && Math.pow(2, 4) === 16);
  check("logs and radians", Math.abs(Math.log(Math.E) - 1) < 1e-12 && Math.abs(Math.sin(Math.PI / 2) - 1) < 1e-12);
  const random = Math.random(); check("observed random range", random >= 0 && random < 1);
  const pattern = /[A-Z]/g;
  check("global regex advances", pattern.test("AB") && pattern.lastIndex === 1);
  check("global regex shares state across strings", !pattern.test("A") && pattern.lastIndex === 0);
  check("exec captures groups", /^([A-Z]+)-(\d+)$/.exec("SKU-17")[2] === "17");
  check("RegExp constructor needs escaping", new RegExp("^\\d+$").test("42"));
  check("search and match results", "x7".search(/\d/) === 1 && "a1b2".match(/\d/g).join("") === "12");
  // Only this disposable process/page is modified; always remove the symbol.
  const extension = Symbol("original JSA size");
  try {
    Object.defineProperty(Array.prototype, extension, { configurable: true, value() { return this.length; } });
    check("temporary nonenumerable prototype extension", [1, 2][extension]() === 2 && !Object.getOwnPropertyDescriptor(Array.prototype, extension).enumerable);
  } finally { delete Array.prototype[extension]; }
  check("prototype extension cleaned up", !Object.hasOwn(Array.prototype, extension));

  function options({ size = 4 } = {}) { return size; }
  check("defaults use undefined", options() === 4 && options({ size: undefined }) === 4);
  check("defaults preserve null and zero", options({ size: null }) === null && options({ size: 0 }) === 0);
  check("null is not default object", raises(() => options(null), TypeError));
  const sum = (first, ...rest) => rest.reduce((a, b) => a + b, first);
  check("rest and spread", sum(...[2, 3, 4]) === 9);
  function counter() { let n = 0; return () => ++n; }
  const one = counter(), two = counter(); one();
  check("closure state is independent per call", one() === 2 && two() === 1);
  const closed = (() => { let n = 1; const get = () => n; n = 6; return get; })();
  check("IIFE closure retains binding", closed() === 6);
  function wrap(fn) { return function (...args) { return fn.apply(this, args); }; }
  check("wrapper preserves receiver and result", wrap(detached).call(receiver, 8) === 12);
  check("wrapper preserves thrown identity", raises(() => wrap(() => { throw new RangeError(); })(), RangeError));
  function* tickets() { yield "A"; yield "B"; return "finished"; }
  const iterator = tickets();
  check("generator first next", same(iterator.next(), { value: "A", done: false }));
  iterator.next();
  check("generator return is done value", same(iterator.next(), { value: "finished", done: true }));
  check("iterable consumption excludes return", same([...tickets()], ["A", "B"]));
  check("generator iterator returns itself", iterator[Symbol.iterator]() === iterator);
  check("exhausted iterator stays exhausted", iterator.next().done);
  const iterable = { *[Symbol.iterator]() { yield 2; yield 4; } };
  check("custom iterable can restart", same([...iterable], [...iterable]) && iterable[Symbol.iterator]() !== iterable[Symbol.iterator]());
  let cleaned = false;
  function* cleanup() { try { yield 1; yield 2; } finally { cleaned = true; } }
  for (const value of cleanup()) { break; }
  check("early loop exit closes generator", cleaned);

  const order = [];
  const task = new Promise(resolve => setTimeout(() => { order.push("task"); resolve(); }, 0));
  Promise.resolve().then(() => order.push("microtask")); order.push("sync");
  await task;
  check("synchronous then microtask then timer", same(order, ["sync", "microtask", "task"]));
  const original = Promise.resolve(2); const chained = original.then(v => v + 3);
  check("then returns another promise", chained !== original && await chained === 5);
  check("catch returning recovers", await Promise.reject("bad").catch(() => 7) === 7);
  check("finally ordinary return ignored", await Promise.resolve(4).finally(() => 99) === 4);
  check("finally throw replaces outcome", await rejects(Promise.resolve(4).finally(() => { throw new RangeError(); }), RangeError));
  check("all preserves input order", same(await Promise.all([Promise.resolve("a"), "b"]), ["a", "b"]));
  check("all empty fulfills empty", same(await Promise.all([]), []));
  check("any selects fulfillment", await Promise.any([Promise.reject("bad"), Promise.resolve("good")]) === "good");
  check("any empty AggregateError", await rejects(Promise.any([]), AggregateError));
  const allErrors = await Promise.any([Promise.reject("first"), Promise.reject("second")]).catch(e => e.errors);
  check("any errors in input order", same(allErrors, ["first", "second"]));
  check("race follows rejection too", await rejects(Promise.race([Promise.reject(new RangeError()), Promise.resolve(3)]), RangeError));
  const never = Promise.race([]);
  check("empty race remains pending during sentinel", await Promise.race([never, Promise.resolve("sentinel")]) === "sentinel");
  let completed = false;
  const other = new Promise(resolve => setTimeout(() => { completed = true; resolve(); }, 0));
  await Promise.all([Promise.reject("stop"), other]).catch(() => undefined);
  await other; check("all rejection does not cancel other work", completed);
  const trace = [];
  async function pause() { trace.push("before"); await 0; trace.push("after"); return 6; }
  const pending = pause(); trace.push("caller");
  check("async runs until first await", same(trace, ["before", "caller"]));
  check("async continuation and result", await pending === 6 && same(trace, ["before", "caller", "after"]));
  async function adopt() { return original; }
  check("async adopts state but returns different promise", adopt() !== original && await adopt() === 2);
  function callbackWork(fail, done) { setTimeout(() => fail ? done(new Error("failed")) : done(null, 11), 0); }
  const asPromise = fail => new Promise((resolve, reject) => callbackWork(fail, (error, value) => error ? reject(error) : resolve(value)));
  check("callback success adapted", await asPromise(false) === 11);
  check("callback failure explicitly adapted", await rejects(asPromise(true), Error));
  return { passed: passed.length, names: passed };
})();
```

## Integrated scenarios

### Scenario 1: Catalog domain model

This complete model accepts IDs of 1–16 uppercase ASCII letters/digits/hyphens starting with a letter, prices of 0–1,000,000 integer cents, quantities of 0–1,000, and at most 20 short lowercase tags. Each own field is enumerable and non-writable/non-configurable; the tag array is copied, deduplicated and frozen. The object itself is still extensible, so this is not a general deep-immutability claim. Accessor totals are computed from validated fields. `DiscountItem.from(...)` uses the inherited static factory's `this` to construct the subtype, and `super.describe()` retains its receiver and sees the overridden total. The discount is an explicitly fictional rounding policy.

```javascript
globalThis.JsaCatalog = (() => {
  "use strict";
  function boundedInteger(value, max, name) {
    if (!Number.isSafeInteger(value) || value < 0 || value > max) {
      throw new RangeError(`${name} must be an integer from 0 through ${max}`);
    }
    return value;
  }
  class CatalogItem {
    constructor(id, unitCents, quantity, tags = []) {
      if (typeof id !== "string" || !/^[A-Z][A-Z0-9-]{0,15}$/.test(id)) {
        throw new TypeError("Invalid catalog ID");
      }
      boundedInteger(unitCents, 1000000, "unitCents");
      boundedInteger(quantity, 1000, "quantity");
      if (!Array.isArray(tags) || tags.length > 20 ||
          [...tags].some(tag => typeof tag !== "string" || !/^[a-z]{1,16}$/.test(tag))) {
        throw new TypeError("Tags must be a dense array of short lowercase words");
      }
      Object.defineProperties(this, {
        id: { value: id, enumerable: true },
        unitCents: { value: unitCents, enumerable: true },
        quantity: { value: quantity, enumerable: true },
        tags: { value: Object.freeze([...new Set(tags)]), enumerable: true }
      });
    }
    get totalCents() { return this.unitCents * this.quantity; }
    describe() { return `${this.id}: ${this.totalCents} cents`; }
    static from(record) {
      if (record === null || typeof record !== "object" || Array.isArray(record)) {
        throw new TypeError("Expected a record object");
      }
      return new this(record.id, record.unitCents, record.quantity, record.tags);
    }
  }
  class DiscountItem extends CatalogItem {
    // Fictional policy: ten percent off, then round down to whole cents.
    get totalCents() { return Math.floor(super.totalCents * 9 / 10); }
    describe() { return super.describe() + " (discount)"; }
  }
  return { CatalogItem, DiscountItem, boundedInteger };
})();
```

For example, `new JsaCatalog.CatalogItem("K-1", 125, 3, ["home", "home"]).totalCents` is 375. `JsaCatalog.DiscountItem.from({id: "D", unitCents: 101, quantity: 1}).totalCents` is 90. Predict own keys, descriptor flags and prototype links, then try a fractional quantity, lowercase ID, sparse tag array and mutation of the original tags. The earlier `Account` examples illustrate placement; this model demonstrates a stated validation contract.

### Scenario 2: Data normalization pipeline

Run after Scenario 1. This importer rejects malformed JSON or a non-array root entirely, then reports row-level validation failures while retaining valid rows. Canonical decimal strings allow `"0"` or a nonzero digit followed by digits; they reject whitespace, signs, exponent/hex syntax and redundant leading zeros. Numeric inputs still require bounded safe integers. Strict `YYYY-MM-DD` dates are parsed in UTC and round-tripped to reject normalized impossible dates. A duplicate ID keeps the **first valid row** and records later duplicates as errors, rather than silently using Map's default overwrite behavior.

```javascript
globalThis.JsaNormalize = (() => {
  "use strict";
  const { CatalogItem, boundedInteger } = JsaCatalog;
  function decimal(value, max, name) {
    if (typeof value === "string") {
      if (!/^(0|[1-9][0-9]*)$/.test(value)) throw new TypeError(`Invalid ${name} text`);
      value = Number(value);
    }
    return boundedInteger(value, max, name);
  }
  function dateOnly(value) {
    if (typeof value !== "string" || !/^[0-9]{4}-[0-9]{2}-[0-9]{2}$/.test(value)) {
      throw new TypeError("Expected YYYY-MM-DD");
    }
    const date = new Date(value + "T00:00:00Z");
    if (!Number.isFinite(date.getTime()) || date.toISOString().slice(0, 10) !== value) {
      throw new RangeError("Not a real calendar date");
    }
    return value;
  }
  function normalize(text) {
    if (typeof text !== "string") throw new TypeError("Expected JSON text");
    const rows = JSON.parse(text);
    if (!Array.isArray(rows) || rows.length > 1000) throw new TypeError("Expected at most 1000 rows");
    const candidates = rows.map((row, index) => {
      try {
        if (row === null || typeof row !== "object" || Array.isArray(row)) throw new TypeError("Expected row object");
        const item = new CatalogItem(row.id,
          decimal(row.unitCents, 1000000, "unitCents"),
          decimal(row.quantity, 1000, "quantity"), row.tags);
        return { index, item, date: dateOnly(row.date) };
      } catch (error) { return { index, error: error.message }; }
    });
    const byId = new Map();
    const accepted = candidates.filter(candidate => {
      if (candidate.error) return false;
      if (byId.has(candidate.item.id)) {
        candidate.error = "Duplicate ID: first valid row retained";
        return false;
      }
      byId.set(candidate.item.id, candidate);
      return true;
    });
    return {
      accepted,
      rejected: candidates.filter(candidate => candidate.error).map(({ index, error }) => ({ index, error })),
      byId,
      tags: new Set(accepted.flatMap(candidate => candidate.item.tags)),
      totalCents: accepted.reduce((total, candidate) => total + candidate.item.totalCents, 0)
    };
  }
  return { decimal, dateOnly, normalize };
})();
```

Call `JsaNormalize.normalize('[{"id":"A","unitCents":"125","quantity":"2","date":"2024-02-29"}]')`: one accepted row, total 250 cents, and empty tags. Add a duplicate, a `2023-02-29` date, a `null` row and an invalid numeric string; inspect diagnostic indexes. Empty input yields zero and empty collections. The 1,000-row/product bounds keep the total at or below 10^12 cents, within exact safe integer range. This does not impose a pre-parse byte limit or validate hostile executable objects: its contract is original JSON text. Returned Map/Set and result arrays remain mutable.

The catalog and normalization boundary harness passed **84 checks in each runtime**, including upper bounds, malformed roots, date rollover, sparse tags, duplicate policy and preservation of caller data. These are original fixtures, not completed external course labs.

### Scenario 3: Resilient asynchronous client

This browser script expects endpoints returning `application/json` with a nonempty string `id` of at most 80 characters and an integer `quantity` from 0 through 1,000. Extra response fields are ignored when constructing a frozen result. Other JSON media types are intentionally outside this small contract. Fetch cancellation uses the supplied signal; the XHR wrapper also enforces an explicit millisecond timeout and removes event/signal listeners after settlement. A Fetch timeout can be implemented by aborting a controller on a timer and clearing that timer in `finally`; `Promise.race` by itself would only stop waiting.

```javascript
globalThis.JsaClient = (() => {
  "use strict";
  function record(value) {
    if (value === null || typeof value !== "object" || Array.isArray(value) ||
        typeof value.id !== "string" || value.id.length === 0 || value.id.length > 80 ||
        !Number.isSafeInteger(value.quantity) || value.quantity < 0 || value.quantity > 1000) {
      throw new TypeError("Invalid record body");
    }
    return Object.freeze({ id: value.id, quantity: value.quantity });
  }
  function requireJSON(contentType) {
    if ((contentType || "").split(";")[0].trim().toLowerCase() !== "application/json") {
      throw new TypeError("Expected application/json");
    }
  }
  async function fetchRecord(url, { signal } = {}) {
    const response = await fetch(url, { signal });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    requireJSON(response.headers.get("content-type"));
    return record(await response.json());
  }
  function xhrRecord(url, { signal, timeoutMs = 3000 } = {}) {
    return new Promise((resolve, reject) => {
      if (!Number.isInteger(timeoutMs) || timeoutMs < 1 || timeoutMs > 60000) {
        reject(new RangeError("timeoutMs must be 1..60000")); return;
      }
      if (signal?.aborted) { reject(new DOMException("Cancelled", "AbortError")); return; }
      const xhr = new XMLHttpRequest();
      let settled = false;
      const cancel = () => xhr.abort();
      function finish(error, value) {
        if (settled) return;
        settled = true;
        signal?.removeEventListener("abort", cancel);
        xhr.onload = xhr.onerror = xhr.ontimeout = xhr.onabort = null;
        error ? reject(error) : resolve(value);
      }
      xhr.onload = () => {
        try {
          if (xhr.status < 200 || xhr.status >= 300) throw new Error(`HTTP ${xhr.status}`);
          requireJSON(xhr.getResponseHeader("content-type"));
          finish(null, record(JSON.parse(xhr.responseText)));
        } catch (error) { finish(error); }
      };
      xhr.onerror = () => finish(new TypeError("Network request failed"));
      xhr.ontimeout = () => finish(new DOMException("Request timed out", "TimeoutError"));
      xhr.onabort = () => finish(new DOMException("Cancelled", "AbortError"));
      try {
        xhr.open("GET", url, true);
        xhr.timeout = timeoutMs;
        signal?.addEventListener("abort", cancel, { once: true });
        xhr.send();
      } catch (error) { finish(error); }
    });
  }
  function installRetry(button, status, url, loader = fetchRecord) {
    let pending = false;
    async function retry() {
      if (pending) return;
      pending = true; button.disabled = true; status.textContent = "Loading";
      try {
        const value = await loader(url);
        status.textContent = `${value.id}: ${value.quantity}`;
      } catch (error) { status.textContent = `Try again: ${error.message}`; }
      finally { pending = false; button.disabled = false; }
    }
    button.addEventListener("click", retry);
    return () => button.removeEventListener("click", retry);
  }
  return { record, requireJSON, fetchRecord, xhrRecord, installRetry };
})();
```

Create a `<button id="retry">Load / retry</button>` and `<output id="status"></output>` on the same page. Call `JsaClient.installRetry(document.querySelector("#retry"), document.querySelector("#status"), "/record")` against your controlled endpoint; it returns a listener-removal function. The button is disabled while pending and restored after success or failure. Rendering uses `textContent`, so a returned ID containing markup stays text. This example has no overlapping requests through that button; a broader UI would need a policy for stale responses and cancellation on removal.

The review exercised actual Chrome Fetch/XHR, timers, AbortController and DOM clicks using **route-intercepted synthetic same-origin responses**. Both clients passed success, 404/500, network-abort, malformed JSON, invalid shape, wrong content type, empty 204 body, pre-aborted signal and in-flight abort checks. XHR timeout, body consumption, concurrent calls and retry/error/loading states were also checked. These 36 browser checks do not establish live server transport, authentication, CORS, cross-browser compatibility or production recovery behavior. In the workbook, an explicit callback adapter and the three combinators separately demonstrate failure propagation and non-cancellation.

## Hands-on labs

These eight broader learner activities remain **proposed**. Executing the original workbook/scenarios supplies specific evidence above, not a claim that a learner completed every activity, used a visual debugger, or finished an external course.

1. **Object identity laboratory:** create objects by literal, factory, constructor, and `Object.create`; add dynamic keys, enumerate own/inherited properties, clone shallowly, and diagram all aliases.
2. **Receiver and descriptor laboratory:** compare method, detached, `call`, `apply`, `bind`, and arrow invocations. Define descriptor combinations, then test preventExtensions, seal, freeze, and nested mutation.
3. **Class/prototype translation:** implement one model as constructor/prototype functions and as classes. Add accessors, statics, inheritance, overrides, and `super`; prove each `instanceof` result from the chain.
4. **Built-in behavior matrix:** for Number, String, Date, Array, Set, and Map, record input, returned value/type, mutation, failure boundary, and iteration order.
5. **Array pipeline:** solve one transformation with loops and with `find`/`every`/`some`/`filter`/`sort`/`map`/`reduce`; cover empty input and comparator errors.
6. **Serialization and patterns:** round-trip supported JSON, record losses/errors for unsupported values, validate the parsed shape, and build regex tests for anchors, groups, flags, replacement, and adversarial text.
7. **Closure and iteration toolkit:** build a closure-backed counter, an IIFE, a preserving decorator, a generator, and a custom iterable; trace every retained binding and `{value, done}` response.
8. **Async network workbook:** implement callback, promise-chain, and async/await forms; test fulfillment, rejection, HTTP errors, invalid JSON, cancellation, and concurrent combinators using a controlled endpoint or mock.

## Original readiness checks

1. When do dot and bracket notation differ materially?
2. How do `in`, `Object.hasOwn`, `for...in`, and `Object.keys` differ?
3. Why are two equal-looking object literals not strictly equal?
4. What remains shared after object spread copies a nested object?
5. How is an ordinary method's `this` selected?
6. What descriptor flags default to when omitted from `Object.defineProperty`?
7. How do preventExtensions, seal, and freeze differ?
8. What is the difference between an object's prototype and a constructor's `.prototype` property?
9. Why is changing a mature object's prototype usually avoided?
10. Where do instance methods declared in a class live?
11. What must a derived constructor do before accessing `this`?
12. Where is a static method called?
13. How does `instanceof` decide its result?
14. Name two semantic differences between class syntax and a simple constructor function.
15. Why is `new Number(5)` usually undesirable compared with `Number(5)`?
16. Which Number checks avoid coercion?
17. Why should non-standard date-string parsing be avoided?
18. Which common array operations in the syllabus mutate their receiver?
19. Why does numeric ascending sort need a comparator?
20. What are `every` and `some` for an empty array?
21. When is Map a better fit than a plain object?
22. What values cannot be represented faithfully in ordinary JSON?
23. Why is `Math.random` unsuitable for secrets?
24. When is `new RegExp` more useful than a literal?
25. What risks arise from extending built-in prototypes?
26. When does a default parameter apply?
27. How do rest and spread differ?
28. What state does a closure retain?
29. How do call, apply, and bind differ?
30. What contract should a function decorator preserve?
31. How do iterable and iterator differ?
32. What does each generator `next()` call return?
33. What does a `then` call return?
34. How do Promise.all, Promise.any, and Promise.race settle differently?
35. What does an async function always return?
36. Does `await` block the runtime?
37. Why must Fetch code check `response.ok`?
38. Which failures should a network lab exercise?
39. Which block carries the largest published weight?
40. What must be rechecked before purchasing the exam?

## Answer key

1. Dot notation names a literal identifier; brackets evaluate a property key and support spaces, hyphens or dynamic names. `row[field]` reads the value named by `field`, while `row.field` always names `field`.
2. `in` includes the prototype chain; `Object.hasOwn` includes only own properties; `for...in` includes enumerable string keys up the chain; `Object.keys` includes enumerable own string keys. None of these enumeration statements means every symbol/non-enumerable property is listed.
3. Each literal creates a distinct identity. An alias compares equal to its source; matching visible values do not establish identity or full structural equivalence.
4. Nested objects remain shared. Source getters may run during copying; prototypes, accessors and non-enumerable descriptors are not generally preserved by spread. A shallow top-level change differs from nested mutation.
5. The call form supplies the receiver. `obj.method()` uses `obj`; a detached ordinary function in strict mode receives `undefined`, while arrows keep lexical `this` and bound functions keep their bound receiver for ordinary calls.
6. For a new property, omitted writable/enumerable/configurable flags are false. For an existing property, omitted attributes remain unchanged. Data and accessor descriptor fields cannot be mixed.
7. `preventExtensions` blocks new own properties but can still allow deletion. Seal additionally makes existing properties non-configurable. Freeze additionally makes data properties non-writable. These are shallow, and frozen accessors can still invoke setters.
8. An object’s internal prototype is its lookup link. A constructor’s `.prototype` normally becomes that link for its new instances; the constructor function itself has a separate prototype chain. `Object.create(null)` creates no inherited lookup link.
9. Changing the link can alter every subsequent inherited lookup and can disrupt optimization. Construct with the intended prototype, then explain shadowing and dynamic inherited changes separately.
10. Methods declared with class method syntax live on the class prototype and are shared/non-enumerable. Instance field initializers run per instance; a field containing a function is a different placement.
11. Call `super(...)` before reading or writing `this` in a normal derived constructor. `super.method()` invokes a parent method using the current receiver; it does not create a separate parent instance.
12. Call a static method on the constructor/class. Subclasses can inherit it through the constructor chain; an instance does not gain it as an instance method. A factory using `new this(...)` can preserve the called subclass.
13. With ordinary built-in behavior it searches the object’s prototype chain for the constructor’s current `.prototype`. It does not validate record shape; altered prototypes, realms and customized instance checks can matter.
14. Classes require `new`, have lexical temporal-dead-zone behavior, use strict class bodies and define non-enumerable prototype methods. A simple constructor function with assigned prototype methods does not automatically have all those semantics.
15. `new Number(5)` creates a wrapper object with identity; even `new Number(0)` is truthy. `Number(5)` gives a primitive. Conversion of blank text to zero is another reason to validate the input contract separately.
16. `Number.isNaN` and `Number.isFinite` do not coerce strings; `Number.isSafeInteger` adds integer/range validation. A finite result after permissive conversion does not prove canonical numeric text.
17. Nonstandard parsing can vary by implementation. Even a finite date may reflect normalized overflow. Require a format, a local/UTC interpretation and a round-trip validity check when accepting a calendar date.
18. Push/pop/shift/unshift, splice, sort and reverse mutate. Slice/concat/map/filter create new arrays with shallow element relationships. Sort returns the same receiver; copying it first preserves the source ordering.
19. Default sorting compares string representations, so 12 can sort before 2. A numeric comparator returning `a - b` supplies numerical ordering; a boolean comparator does not supply the required negative/zero/positive contract.
20. Empty `every` is true and empty `some` false. Both skip holes; a sparse array can therefore have nonzero length without any visited entries. `find` has a different hole-visiting rule.
21. Map supports arbitrary key identities, explicit size/membership and insertion order. SameValueZero matches NaN and signed zeros; distinct objects remain distinct. Objects remain useful records, with string/symbol keys and prototype/enumeration rules.
22. Ordinary stringify omits unsupported object properties, replaces unsupported array entries/non-finite numbers with null, loses Map/Set entries without conversion, and rejects cycles/BigInt absent custom conversion. Dates become strings through toJSON. Parsing does not restore arbitrary prototypes or validate shape.
23. It supplies pseudorandom values without a cryptographic security guarantee or a user-selected seed API. Range probes do not prove unpredictability, fairness or the correctness of every floating-point scaling formula.
24. Use the constructor for a dynamic pattern/flags, accounting for string escaping: a backslash intended for the regex also needs string-literal escaping. Validate bounded patterns and remember global/sticky lastIndex state.
25. Extensions affect unrelated code using the same prototype, can collide with future names and can leak into enumeration. The workbook uses a unique non-enumerable symbol only in a disposable runtime, with cleanup; application-owned helpers are preferable.
26. A default applies to missing/undefined input. It preserves zero, false, empty string and null; destructuring a null object still throws unless the function explicitly handles it.
27. Rest gathers remaining arguments into an array. Argument/array spread consumes an iterable; object spread copies enumerable own properties, which is a distinct operation and does not require an iterable.
28. It retains access to lexical bindings. Separate factory calls can create independent state, but later changes to a captured binding are observable; a closure is not an automatic value snapshot.
29. Call invokes now with separate arguments; apply invokes with an array-like argument list; bind returns a function with a stored receiver/leading arguments. Arrows keep lexical this, and construction of a bound constructor ignores its bound receiver.
30. Preserve receiver, arguments, result and error propagation unless intentionally changing them. A normal-function wrapper using apply can forward this; returning the underlying promise matters for asynchronous completion and failure.
31. An iterable supplies Symbol.iterator returning an iterator; an iterator supplies next results. A generator object is both and returns itself, so it can be exhausted. A reusable iterable may return a fresh iterator each time.
32. A result with value and done. Yielded values have done false; a generator return arrives with done true and is not included in spread/for-of output. Subsequent next calls remain exhausted for a completed generator.
33. A new promise that follows the handler’s return or thrown error. Returning a nested promise joins its outcome to the chain; forgetting to return it can allow later work to run too early and hide failure.
34. All requires all fulfill and preserves input result order; any needs one fulfillment and aggregates rejection reasons if all fail; race follows the first observed settlement, including rejection. Empty inputs produce [], AggregateError and permanent pending respectively. None automatically cancels remaining operations.
35. A promise. The body runs synchronously until suspension; thrown errors reject the returned promise. Returning an existing promise adopts its outcome but produces a different promise identity.
36. Await suspends the surrounding async continuation, allowing other scheduled work to proceed. It does not automatically move CPU-heavy synchronous work to another thread. Handle concurrently started rejections promptly through a suitable aggregate.
37. A 404/500 normally still produces a Response. Check status, then content type, parsing and shape separately; body consumption and abort can fail too. A valid HTTP response is not a valid application record.
38. Exercise network error, HTTP status failure, content-type mismatch, invalid JSON, valid JSON with wrong shape, empty body, pre/in-flight cancellation, timeout and visible retry/cleanup. The review covered synthetic same-origin browser fixtures; deployed transport/CORS remain separate work.
39. Built-in Objects is 27%, but all 40 objectives matter. Item counts differ from weights and do not establish an equal-score shortcut to the normalized 70% threshold.
40. Recheck active code/syllabus, channel, language, timing, price, voucher/retake eligibility, policies and any stated credential validity. TestNow and Pearson waiting periods differ; contradictory page labels and unseen checkout terms require confirmation rather than assumption.

## Final readiness checklist

- [ ] I can implement and compare literals, factories, constructors, classes, and `Object.create`.
- [ ] I distinguish own/inherited properties, identity/deep equality, and shallow/deep-copy requirements.
- [ ] I can predict `this` for method, detached, arrow, call/apply, and bound calls.
- [ ] I can configure descriptors and explain every mutability-control boundary.
- [ ] I can diagram prototype and class inheritance and translate between class and constructor patterns.
- [ ] I can use every named built-in API and identify its value, type, mutation, and error boundaries.
- [ ] I can build closures, decorators, generators, iterators, and object-parameter APIs.
- [ ] I can reason through callbacks, promise chains/combinators, async/await, XHR, and Fetch failures.
- [ ] I have completed the eight labs without copying solutions.
- [ ] I have rechecked the official JSA-41-01 page and policies.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick one primary path, add focused documentation and a second explanation only where useful, and spend at least as much time writing and debugging code as watching. Commercial resources are supplementary; reconcile them with the current official syllabus.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official JSA-41-01 syllabus](https://jsinstitute.org/jsa-exam-syllabus) | Free canonical objectives and weights | 2–3 hours to map and recheck |
| [Official JSA certification page and policies](https://jsinstitute.org/jsa-certification) | Free exam/version/delivery reference | 30–60 minutes before purchase |
| [OpenEDG JavaScript Essentials 2](https://jsinstitute.org/javascript-essentials-2) | Free official intermediate course; public listing states JSA alignment and four modules; lesson interiors unreviewed | 50 provider-listed hours; public module summaries are not a complete objective crosswalk |
| [Cisco Networking Academy JavaScript Essentials 2](https://www.netacad.com/courses/javascript-essentials-2) | Partner listing returned a small application shell; account/lesson access unreviewed | About 50 hours is an author planning budget here; verify live listing |
| [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide) | Free current reference/tutorial; broader than JSA in places | 20–30 hours for relevant objects, classes, collections, functions, and promises |
| [javascript.info](https://javascript.info/) | Free community tutorial; broad browser coverage | Select Objects and Advanced Functions, 20–30 hours with exercises |
| [O'Reilly JavaScript: The Definitive Guide, 7th Edition](https://www.oreilly.com/library/view/javascript-the-definitive/9781491952016/) | Subscription; direct request HTTP403; historical edition/title retained, fresh page count/runtime and paid interior unverified | 12–18 hours for chapters matching JSA; verify modern API changes in MDN |
| [Udemy Modern JavaScript From The Beginning 2.0](https://www.udemy.com/course/modern-javascript-from-the-beginning/) | Paid marketplace course; HTTP403, current curriculum/runtime and paid interior unverified | Author budget: 15–25 selected hours; verify current OOP/async coverage |

All selected-hour ranges are author planning estimates unless explicitly labeled provider totals. JavaScript Essentials 2 publicly lists 50 hours and four modules, but the visible module bullets are shorter than the 40-objective syllabus; no claim of reading all course lessons or assessments is made. Cisco shell, O’Reilly/Udemy blocks and unreviewed tutorial chapters remain access limits.

No exact current MeasureUp or Whizlabs JSA-41-01 product was verified. Reject any practice source that cannot identify the active version and explain its question provenance; use practice for diagnosis, not memorization.
