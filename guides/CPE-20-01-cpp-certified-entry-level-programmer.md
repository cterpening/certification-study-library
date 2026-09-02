---
exam_code: CPE-20-01
vendor_id: cpp-institute
official_blueprint: https://cppinstitute.org/cpe
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# CPE-20-01 C++ Certified Entry-Level Programmer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked September 2, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#cpe-20-01-coverage-record). The [official CPE page and embedded syllabus](https://cppinstitute.org/cpe) are authoritative.

**Current baseline:** CPE-20-01, active; embedded four-block syllabus last updated July 22, 2025<br>
**Upcoming blueprint change:** none announced on the official exam or certification-catalog pages when checked<br>
**Official delivery snapshot:** 30 questions; 45-minute exam plus approximately 5 minutes for the NDA/tutorial; 70% cumulative passing score; TestNow; English<br>
**Credential snapshot:** no formal prerequisite; USD 69 exam or USD 86 exam-plus-retake when checked; current C/C++ Institute certificates are lifetime and retain the completed exam version<br>

## How to use this guide

CPE asks whether you can read and construct small C++ programs, not whether you can recognize isolated terms. For every topic, predict the compile result, program output, changed state, pointer target, or resource lifetime before using a compiler. Then compile with warnings enabled, run safe inputs, and explain every difference.

Use one loop:

1. write or trace a minimal program;
2. label every value with its type and every object with its lifetime;
3. compile with a modern conforming implementation and warnings;
4. test normal, boundary, empty, and invalid inputs;
5. map the result to one of the four syllabus blocks.

The public outline uses `std::vector`, `std::string`, `nullptr`, and named casts but does not state a language-standard switch. Use at least C++11 for practice and avoid relying on implementation-specific extensions. Classes, templates, exceptions, smart pointers, algorithms, and build systems matter in real C++, but most are beyond this entry-level outline.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Weighted objective map

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| 1. Syntax, Literals, and Operators | 9 | 28% | Read declarations and expressions, predict types/results, and use stream I/O correctly |
| 2. Flow Control and Functions | 8 | 28% | Trace all branches and loops, and explain call, return, recursion, and parameter behavior |
| 3. Vectors and Pointers | 7 | 24% | Distinguish containers, arrays, references, addresses, pointer targets, casts, and allocation lifetimes |
| 4. Structures and Strings | 6 | 20% | Model simple records and manipulate `std::string` values without confusing them with raw character arrays |

The 30 items have different point values and the final result is normalized. The provider explicitly says the passing result is cumulative rather than a simple per-block average; do not try to reverse-engineer individual item values from these weights.

## 1. Syntax, literals, and operators — 28%

### Translation, structure, and names

A small program normally includes required headers, declares names before use, and defines `main`, where hosted program execution begins:

```cpp
#include <iostream>

int main() {
    int count{3};
    std::cout << count << '\n';
    return 0;
}
```

The preprocessor handles directives such as `#include`; the compiler analyzes and translates source; the linker resolves definitions into a program. A compiler diagnostic can arise from invalid syntax or types, a linker diagnostic from a missing or duplicate definition, and a runtime or logic fault after a program has been built. Braces delimit compound statements, semicolons terminate many statements, and `//` and `/* ... */` form comments. C++ names are case-sensitive and keywords cannot be ordinary identifiers.

A declaration introduces a name and type. A definition also supplies the entity or storage. Initialization gives an object its starting value; assignment changes an existing object. Prefer initialization and never reason from the value of an uninitialized fundamental local variable.

> **Related item:** Compiler warnings are evidence, not decoration. Enable a strong warning level and treat warnings about conversion, uninitialized use, and unreachable code as study prompts even when compilation succeeds.

### Types and literals

Know Boolean, character, integer, and floating-point categories and recognize their literals: `true`, `'A'`, `42`, `42u`, `3.5`, and `3.5f`. A double-quoted literal such as `"A"` is not a `char`; it represents a character array used as a string literal. Exact sizes and ranges can vary by implementation, so use `sizeof` or numeric limits when an exact platform fact matters rather than inventing a universal size.

Implicit conversions happen in mixed expressions, assignments, and calls. They can lose range or precision. `static_cast<T>(value)` makes an intended supported conversion visible. Do not assume a cast validates an input or makes an out-of-range result portable.

Integer division discards the fractional portion when both operands are integers. `%` gives an integer remainder. Division by zero is invalid; signed overflow is not a wraparound guarantee. Floating-point values are approximations, so direct equality may not match a mathematical expectation.

### Operators and expression tracing

Separate these families:

- arithmetic: `+ - * / %`;
- relational and equality: `< <= > >= == !=`;
- logical: `! && ||`;
- bitwise: `~ & ^ | << >>`;
- assignment: `=` and compound forms such as `+=`;
- increment/decrement: `++ --`.

Precedence groups an expression; associativity resolves comparable operators. Parentheses are clearer than memory when intent matters. Do not confuse assignment `=` with equality `==`, logical `&&` with bitwise `&`, or a prefix increment with a postfix increment: prefix changes and yields the new value, while postfix changes the object but yields its prior value in that expression.

`&&` and `||` short-circuit left to right. In `ready && read_value()`, the function is not called when `ready` is false. This can prevent an invalid operation, but hidden side effects make code hard to reason about.

### Streams and formatting

`std::cin >> value` performs formatted input and sets stream state on failure. `std::cout` is ordinary output; `std::cerr` is conventionally used for diagnostics. Chained insertion and extraction associate from left to right. `std::endl` writes a newline and flushes; `'\n'` writes a newline without requiring a flush. `std::setw(n)` from `<iomanip>` sets the minimum width for the next formatted field, not every later field.

Check stream state before using a value that an extraction was supposed to replace:

```cpp
#include <iostream>

int main() {
    int quantity{};
    if (!(std::cin >> quantity)) {
        std::cerr << "Quantity must be an integer\n";
        return 1;
    }
    std::cout << "Quantity: " << quantity << '\n';
}
```

## 2. Flow control and functions — 28%

### Selection and repetition

`if` selects a path by a condition; an `else` binds to the nearest unmatched `if`. Braces make that ownership explicit. An `if`/`else if` chain selects at most one branch, while separate `if` statements can select several.

`switch` compares one integral or enumeration expression with constant case labels. Execution begins at a matching `case` or `default`; without `break`, it falls through into later labels. Deliberate fallthrough should be obvious. A `switch` is not a range matcher and duplicate case values are invalid.

Use `while` when continuation is tested before the body, `do ... while` when the body must run at least once, and `for` when initialization, condition, and update form a clear loop. `break` leaves the nearest loop or switch; `continue` advances to the next loop iteration. In a `for`, the update expression still occurs after `continue`; in `while`, ensure the state needed for progress is not skipped.

The outline asks you to recognize labels and `goto`. A label names a statement and `goto label;` transfers within the same function under language constraints. Understand the syntax and trace a tiny example, but prefer structured loops, functions, and early returns in normal code.

> **Related item:** A loop invariant is a fact preserved by every iteration. Write the invariant, progress step, and termination condition to uncover off-by-one and infinite-loop defects.

### Functions and parameter mechanisms

A function declaration gives its name, parameter types, and return type; a definition supplies its body; a call transfers control with arguments. A non-`void` function must produce an appropriate value on every reachable required path. A `void` function returns no value, though a bare `return;` can end it early.

```cpp
void add_fee_by_value(int amount) { amount += 5; }
void add_fee_by_reference(int& amount) { amount += 5; }
void add_fee_by_pointer(int* amount) {
    if (amount != nullptr) {
        *amount += 5;
    }
}
```

By value initializes a separate parameter, so reassigning it does not change the caller's integer. A reference parameter aliases the caller's object and cannot represent “no object” in this form. A pointer parameter receives an address by value; dereferencing can change the pointed-to object, and `nullptr` must be considered. Passing a pointer by value does not mean the pointer variable itself in the caller is passed by reference.

Scope determines where a name can be used; lifetime determines when its object exists. A local automatic object is destroyed when its block ends. A local name can shadow an outer name, but identical spelling does not make the objects identical.

### Recursion

A recursive solution needs a reachable base case and a recursive step that moves toward it. Trace each call's parameter and pending return:

```cpp
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

This illustrates mechanics, not full validation: a negative input is silently treated like the base case, and results overflow quickly. Unbounded recursion consumes call-stack space and eventually fails.

## 3. Vectors and pointers — 24%

### Arrays, vectors, and dimensions

A built-in array has a fixed element count in its type. Indices begin at zero; valid indices end at size minus one. The language does not automatically bounds-check `array[index]`. A multidimensional array is an array whose elements are arrays, so row and column bounds must both be correct.

`std::vector<T>` from `<vector>` is a resizable sequence that owns its elements. Initialize it, query `size()`, index only valid positions, append with `push_back`, and iterate without mixing signed counters carelessly with its unsigned size type. `at()` performs bounds checking and differs from unchecked `operator[]`.

`vector.data()` returns a pointer to contiguous element storage (or a value that must not be dereferenced when there is no element). An operation that changes the vector's capacity can invalidate earlier element pointers, references, and iterators. A raw pointer returned by `data()` does not transfer ownership.

> **Related item:** Modern production C++ normally prefers containers and resource-owning types over manually allocated arrays. The exam includes raw `new` and `delete` so you must understand them, not because they are the default design for new code.

### Pointers, references, and addresses

`&object` obtains an address; a compatible pointer stores it; `*pointer` dereferences the pointer to access its target. `nullptr` is the C++ null-pointer literal. Never dereference a null, dangling, one-past-the-end, or otherwise invalid pointer.

Keep four concepts distinct:

- the pointer object has its own address and lifetime;
- the stored pointer value identifies a target or is null;
- the pointee has its own type and lifetime;
- `*p` designates the pointee only while the pointer is valid.

A reference is an alias established at initialization; a pointer is an object that can be reseated and may be null. `const int* p` prevents modification of the integer through `p`; `int* const p` prevents reseating that pointer. Parenthesize and read declarations carefully.

### Named conversions

`static_cast` handles supported compile-time conversions, including explicit numeric conversion and certain related-pointer conversions. It does not add runtime proof that an assumed downcast matches the object's actual type. `dynamic_cast` performs checked conversions in a polymorphic class hierarchy; a failed pointer cast produces `nullptr`, while a failed reference cast throws. That full class machinery is adjacent to this entry outline, so learn the purpose and safety distinction without letting advanced inheritance replace core pointer practice.

Never use a cast merely to silence a compiler when the type relationship is not understood. No named cast repairs a dangling pointer or extends an object's lifetime.

### Dynamic storage

`new T(...)` creates a dynamically allocated object and returns a pointer. `delete p` destroys/releases a single object created by compatible single-object `new`. `new T[n]` must be paired with `delete[] p`. Losing the last pointer leaks the allocation; using a pointer after deletion dangles; deleting twice or using the wrong form has undefined behavior. Assigning `nullptr` after deletion may reduce accidental reuse of that one pointer but does not repair aliases.

```cpp
int* values = new int[3]{4, 5, 6};
int total = values[0] + values[1] + values[2];
delete[] values;
values = nullptr;
```

The safe practical alternative here is `std::vector<int> values{4, 5, 6};`, whose lifetime follows its owning object.

## 4. Structures and strings — 20%

### Structures and records

A `struct` defines a user-defined type whose members are public by default. Define a type, create objects, initialize fields, and use `.` with an object:

```cpp
#include <string>
#include <vector>

struct Product {
    int id;
    std::string name;
    double price;
};

std::vector<Product> products{
    {101, "Cable", 8.50},
    {102, "Adapter", 14.00}
};

products[0].price += 1.00;
```

If `Product* p` points to an object, `p->price` is shorthand for `(*p).price`. The published objective names the dot operator, but recognizing arrow prevents confusion when structures and pointers meet. Copying a simple structure copies its members according to their own copy behavior: its `std::string` and `std::vector` members manage their own resources, unlike a raw owning pointer.

> **Related item:** A structure groups fields that belong to one record; a vector groups repeated records. This “record versus collection” distinction is a durable modeling tool across languages and databases.

### `std::string`

`std::string` from `<string>` owns a mutable character sequence. You can initialize, assign, concatenate with supported `+` combinations, append with `+=`, compare lexicographically, query `size()` or `length()`, index valid positions, and extract substrings. An empty string has length zero and no character at index zero.

Input with `std::cin >> text` stops at formatted whitespace; `std::getline(std::cin, text)` reads a line. If formatted extraction leaves a newline before `getline`, consume or design around that delimiter. This is an input-state issue, not a defect in `getline`.

Do not confuse a `std::string`, a string literal, and a null-terminated character array. They can interoperate, but they have different types and ownership. Relational operators between `std::string` objects compare content; comparing raw character pointers compares addresses rather than the text they appear to identify.

## Integrated scenarios

### Scenario 1: Inventory valuation

Define a `Product` structure and a vector of products. Read a requested identifier and quantity, search with a loop, compute a total, and print formatted fields. Test first/last/missing IDs, zero and negative quantity, malformed input, empty inventory, and a price boundary. Explain every conversion and why the vector owns the records.

### Scenario 2: Sensor buffer

Read a fixed array of readings, compute summary values in functions, and repeat using a vector. Pass one total by reference and a possibly absent result by pointer. Inspect `data()` before and after an operation that may increase capacity; never dereference an invalidated pointer. Compare an automatic array, vector ownership, and a deliberately isolated `new[]`/`delete[]` exercise.

### Scenario 3: Menu and recursive calculation

Use a `do ... while` menu and `switch` to choose sum, product, or a small recursive factorial. Validate extraction, use `cerr` for diagnostics, and prevent unsupported factorial inputs. Trace normal exit, invalid choice, input failure, fallthrough if a `break` is removed, and recursion base/progress cases.

## Hands-on labs

1. **Toolchain and diagnostics:** compile a hello-world program, then introduce one preprocessing, syntax, type, linker, and runtime/logic defect. Record which stage exposes each and enable strong warnings.
2. **Type and operator table:** predict 20 mixed integer/floating, comparison, logical, bitwise, prefix/postfix, and compound-assignment expressions. Compile only after recording type and result; avoid expressions with unsequenced side effects.
3. **Stream-state harness:** read an integer and two words, then a full line. Test whitespace, EOF, invalid numeric text, and recovery. Compare `cout`, `cerr`, `endl`, newline, and one-shot `setw` behavior.
4. **Control-flow matrix:** implement a boundary classifier with `if`, a command menu with `switch`, and equivalent `while`, `do`, and `for` counts. Trace `break` and `continue`; include a labeled `goto` only in a disposable recognition example.
5. **Parameter and recursion tracer:** call value, reference, and pointer functions with ordinary and null-capable cases. Draw objects and aliases. Trace factorial or sum recursion through every frame, including invalid and base inputs.
6. **Array/vector laboratory:** implement fixed, multidimensional, and vector-backed tables. Test empty and last-element boundaries. Compare `[]` and `at()`, observe capacity, and document when a saved `data()` pointer becomes unsafe.
7. **Dynamic-lifetime sandbox:** in a throwaway program, pair single `new`/`delete` and array `new[]`/`delete[]`. Use compiler sanitizers or equivalent diagnostics where available. Explain leak, double-delete, mismatch, and use-after-free without deliberately deploying unsafe code.
8. **Record-and-string mini-app:** finish the inventory scenario with a vector of structures, whole-line names, string concatenation/comparison, search, update, and report functions. Test empty strings, duplicate IDs, copy behavior, and every input failure.

## Original readiness checks

1. What roles do preprocessing, compilation, and linking play?
2. How do declaration, definition, initialization, and assignment differ?
3. Why is using an uninitialized local `int` unsafe?
4. How do `'7'` and `"7"` differ?
5. What result does integer `7 / 2` produce, and why?
6. Why can an implicit narrowing conversion be dangerous?
7. What is the difference between `=` and `==`?
8. When does the right operand of `&&` not run?
9. How do logical `&&` and bitwise `&` differ?
10. What is the visible-value difference between prefix and postfix increment?
11. Why prefer parentheses in a mixed-operator expression?
12. How do `cout`, `cerr`, `endl`, and `'\n'` differ?
13. How long does a `setw` setting normally apply?
14. What should happen after integer extraction from nonnumeric input fails?
15. Which `else` owns an unbraced nested `if`?
16. What happens when a matching `switch` case omits `break`?
17. How do `while` and `do ... while` differ for an initially false condition?
18. What does `continue` do in a `for` loop?
19. Which construct does `break` leave when loops are nested?
20. Why is `goto` generally inferior to structured control flow?
21. How do a function declaration and definition differ?
22. What must a non-`void` function do on its relevant paths?
23. Which parameter mechanism best expresses a required modifiable caller object?
24. How can a pointer parameter express “no object”?
25. What two properties make basic recursion terminate correctly?
26. How do scope and lifetime differ?
27. What is the last valid index of a five-element array?
28. What important ownership and sizing difference separates an array from a vector?
29. How do `vector::at()` and `operator[]` differ?
30. What can invalidate a pointer obtained from `vector::data()`?
31. What do address-of and dereference do?
32. How does a reference differ from a pointer?
33. Why must `nullptr` be checked before dereference?
34. What safety distinction separates `static_cast` from `dynamic_cast` for downcasts?
35. Which deallocation matches `new int`?
36. Which deallocation matches `new int[10]`?
37. What are a leak, a dangling pointer, and a double delete?
38. How do `.` and `->` access structure members?
39. Why can `cin >> name` and `getline(cin, name)` return different text?
40. What should you verify on the official CPE page immediately before purchasing?

## Answer key

1. Preprocessing expands directives, compilation translates/checks translation units, and linking resolves definitions into a program.
2. A declaration introduces; a definition supplies the entity/storage; initialization establishes an initial value; assignment replaces a value later.
3. Its value is indeterminate and reading it can produce undefined behavior.
4. The first is a character literal; the second is a string literal/character array.
5. `3`, because both operands are integers and the fractional part is discarded.
6. The target may not represent the original range or precision.
7. `=` assigns; `==` compares for equality.
8. When the left operand is false.
9. `&&` combines truth conditions and short-circuits; `&` combines bits and evaluates both operands.
10. Prefix yields the changed value; postfix yields the prior value while still changing the object.
11. They make intended grouping explicit and reduce precedence mistakes.
12. `cout` is ordinary output, `cerr` diagnostics; `endl` writes newline and flushes, while `'\n'` need not flush.
13. The next formatted field.
14. Detect failed stream state before using the intended input and recover or exit deliberately.
15. The nearest unmatched `if`; braces should make intent explicit.
16. Execution falls through into later labels until a transfer such as `break` or return.
17. `while` may run zero times; `do ... while` runs its body at least once.
18. It skips the rest of the body, then the update expression occurs before the next condition.
19. The nearest enclosing loop (or switch when applicable), not every outer construct.
20. It obscures structured entry/exit and makes state and correctness harder to reason about.
21. A declaration provides the signature; a definition provides the body.
22. Return an appropriate value on every path where reaching the end would be invalid.
23. A non-const reference parameter.
24. It can receive `nullptr`, which the function must handle before dereference.
25. A reachable base case and progress toward it.
26. Scope is where a name is visible; lifetime is when its object exists.
27. Index `4`.
28. A built-in array has fixed extent; a vector owns a resizable element sequence.
29. `at()` checks bounds and reports failure; `[]` requires a valid index.
30. Operations that reallocate the vector's storage, commonly capacity growth.
31. `&` obtains an object's address; unary `*` accesses the object designated by a valid pointer.
32. A reference aliases a required object and is not reseated; a pointer is a reseatable object and may be null.
33. Dereferencing null has undefined behavior.
34. `dynamic_cast` can check a polymorphic relationship at runtime; `static_cast` does not prove the object's dynamic type.
35. `delete`.
36. `delete[]`.
37. Unreleased storage; a pointer whose target lifetime ended; and deallocating the same allocation more than once.
38. `object.member` uses `.`, while `pointer->member` is shorthand for `(*pointer).member`.
39. Formatted extraction stops at whitespace; `getline` reads through a delimiter and can encounter a newline left by earlier extraction.
40. Confirm CPE-20-01 is still active and recheck the blueprint, format, price, language, delivery, and policies.

## Final readiness checklist

- [ ] I can trace expressions without depending on compiler output first.
- [ ] I distinguish compile, link, runtime, logic, and undefined-behavior concerns.
- [ ] I validate stream state and test boundary inputs.
- [ ] I trace `if`, `switch`, every loop form, `break`, `continue`, and basic labels.
- [ ] I explain value, reference, and pointer parameters with object diagrams.
- [ ] I can trace a recursive call stack and prove progress to a base case.
- [ ] I distinguish fixed arrays, vectors, storage capacity, and `data()` invalidation.
- [ ] I match every manual allocation with the correct deallocation and prefer owners in practical designs.
- [ ] I can build and search a vector of structures and handle whole-line strings.
- [ ] I have rechecked the live official page rather than relying on this dated snapshot.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick one primary path, use another source only where its explanation fits you better, and spend at least as much time predicting, coding, testing, and debugging as watching. All third-party material is supplementary; reconcile it with the current official syllabus.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official CPE exam page and syllabus](https://cppinstitute.org/cpe) | Free official blueprint | 1–2 hours to map and recheck |
| [C++ Institute exam policies](https://cppinstitute.org/exam-policies) | Free official policy | 20–40 minutes before scheduling |
| [C++ Institute certification catalog](https://cppinstitute.org/certification-exams) | Free official pathway/lifecycle | 15–30 minutes |
| [OpenEDG C++ Essentials 1](https://edube.org/study/cppe1) | Free account; officially aligned | 42 hours listed |
| [Cisco Networking Academy C++ Essentials 1](https://www.netacad.com/courses/c-plus-plus-essentials-1?courseLang=en-US) | Free account; official partner delivery | Plan 35–45 hours; verify live listing |
| [Microsoft C++ console calculator tutorial](https://learn.microsoft.com/en-us/cpp/get-started/tutorial-console-cpp?view=msvc-170) | Free documentation/tutorial | 1–2 hours plus variations |
| [cppreference C++ language reference](https://en.cppreference.com/cpp/language) | Free reference | Ongoing; 3–6 hours targeted lookup |
| [Pluralsight C++ path](https://www.pluralsight.com/paths/c-plus-plus) | Subscription; 44-hour broad path | Select the two beginner courses, about 11 hours, then targeted topics |
| [O'Reilly C++ Crash Course](https://www.oreilly.com/library/view/c-crash-course/9781098122553/) | Subscription; 19h42m, broader and deeper | Select early core-language chapters, 8–12 hours |
| [Udemy Beginning C++ Programming — From Beginner to Beyond](https://www.udemy.com/course/beginning-c-plus-plus-programming/) | Paid marketplace course; 45h51m listed | Select fundamentals through pointers, 15–25 hours |
| [freeCodeCamp C++ Tutorial for Beginners](https://www.youtube.com/watch?v=vLnPwxZdW4Y) | Free video; older beginner overview | About 4h02m plus coding time |

No exact current MeasureUp or Whizlabs CPE-20-01 practice product was verified during this review. Prefer the provider-aligned course assessments and your own objective-based code checks over products that do not state the active exam version.
