---
exam_code: CPE-20-01
vendor_id: cpp-institute
official_blueprint: https://cppinstitute.org/cpe
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# CPE-20-01 C++ Certified Entry-Level Programmer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, volatility labels, links, and exam-integrity compliance were checked September 29, 2026. This is not a guarantee that the guide is error-free or current after that date. See the [sources-and-objectives record](../docs/SOURCE-VALIDATION.md#cpe-20-01-coverage-record). The [official CPE page and embedded syllabus](https://cppinstitute.org/cpe) are authoritative.

**CURRENT BLUEPRINT — current baseline:** CPE-20-01, active; embedded four-block syllabus last updated July 22, 2025<br>
**VERIFY CURRENT — upcoming blueprint change:** none announced on the official exam or certification-catalog pages when checked<br>
**VERIFY CURRENT — official delivery snapshot:** 30 questions; 45-minute exam plus approximately 5 minutes for the NDA/tutorial; 70% cumulative passing score; TestNow; English<br>
**VERIFY CURRENT — credential snapshot:** no formal prerequisite; USD 69 exam or USD 86 exam-plus-retake when checked; current C/C++ Institute certificates are lifetime and retain the completed exam version<br>

## How to use this guide

CPE asks whether you can read and construct small C++ programs, not whether you can recognize isolated terms. For every topic, predict the compile result, program output, changed state, pointer target, or resource lifetime before using a compiler. Then compile with warnings enabled, run safe inputs, and explain every difference.

Use one loop:

1. write or trace a minimal program;
2. label every value with its type and every object with its lifetime;
3. compile with a modern conforming implementation and warnings;
4. test normal, boundary, empty, and invalid inputs;
5. map the result to one of the four syllabus blocks.

The public outline uses `std::vector`, `std::string`, `nullptr`, and named casts but does not state a language-standard switch. This guide pins its original examples to **C++17**, using GCC 14.2 remotely through Compiler Explorer; the trace workbook was also checked with Clang 19.1. This is a reproducible practice choice, not a claim that the exam specifies C++17. Avoid implementation-specific extensions. Objective 3.5 explicitly includes both named pointer casts, so a minimal polymorphic hierarchy belongs in cast practice. Wider class design, template authoring, exception taxonomy, smart pointers and build systems are **PRACTICAL DEPTH** rather than added exam requirements.

The [deep-review record](../docs/research/2026-09-29-cpe-20-01-deep-review.md) separates executed original examples from the eight proposed learner activities. Remote sandbox execution checks selected code behavior; it does not establish course completion, exam performance or human review.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context that makes the current topic easier to understand. It is useful supporting knowledge, not a claim that the item appears verbatim in the published exam objectives.

## Weighted objective map

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| 1. Syntax, Literals, and Operators | 9 | 28% | Read declarations and expressions, predict types/results, and use stream I/O correctly |
| 2. Flow Control and Functions | 8 | 28% | Trace all branches and loops, and explain call, return, recursion, and parameter behavior |
| 3. Vectors and Pointers | 7 | 24% | Distinguish containers, arrays, references, addresses, pointer targets, casts, and allocation lifetimes |
| 4. Structures and Strings | 6 | 20% | Model simple records and manipulate `std::string` values without confusing them with raw character arrays |

The provider describes different item point values, a maximum raw score of 120 points and normalization of the final result. A 70% threshold is not a promise that any 21 of the 30 answers will pass. The provider explicitly says the passing result is cumulative rather than a simple per-block average; do not try to reverse-engineer individual item values from these weights.

The embedded syllabus contains **26 numbered objectives: 7/8/6/5** across the four blocks. These are objective counts, distinct from item counts and weights.

| Objective numbers | Where to practice |
|---|---|
| 1.1–1.3 | Translation, types, hosted main and arguments; trace workbook |
| 1.4–1.6 | Operators, grouping, conversions and short-circuit traces |
| 1.7 | Numeric prefixes, stream recovery, line input and setw |
| 2.1–2.4 | Branches, loops, labels/goto and menu switch |
| 2.5–2.8 | Functions, parameter mechanisms and bounded recursion |
| 3.1–3.2 | Fixed/two-dimensional arrays, vector size/capacity and data() |
| 3.3–3.6 | Pointer targets, null, both casts and paired allocation/deallocation |
| 4.1–4.3 | Product program and inventory vector of structures |
| 4.4–4.5 | String ownership, concatenation, comparison, indexing and input |

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

For objective 1.3, recognize both portable hosted forms: `int main()` and `int main(int argc, char* argv[])` (the latter parameter adjusts to `char**`). `argc` is nonnegative; `argv[argc]` is null. When `argc > 0`, entries through `argv[argc - 1]` are C strings; `argv[0]` represents the invocation name or an empty string. Check the count before indexing. Arguments are text, not prevalidated integers. Falling off the end of `main` returns zero; this special rule does not apply to ordinary non-void functions. The [C++17 main rules](https://timsong-cpp.github.io/cppwp/n4659/basic.start.main) take precedence over platform-specific `wmain`, `void main` or environment-parameter extensions in the [Microsoft reference](https://learn.microsoft.com/en-us/cpp/cpp/main-function-command-line-args?view=msvc-170).

A declaration introduces a name and type. A definition also supplies the entity or storage. Initialization gives an object its starting value; assignment changes an existing object. Prefer initialization and never reason from the value of an uninitialized fundamental local variable.

> **Related item:** Compiler warnings are evidence, not decoration. Enable a strong warning level and treat warnings about conversion, uninitialized use, and unreachable code as study prompts even when compilation succeeds.

### Types and literals

Know Boolean, character, integer, and floating-point categories and recognize their literals: `true`, `'A'`, `42`, `42u`, `3.5`, and `3.5f`. A double-quoted literal such as `"A"` is not a `char`; it represents a character array used as a string literal. Exact sizes and ranges can vary by implementation, so use `sizeof` or numeric limits when an exact platform fact matters rather than inventing a universal size.

Implicit conversions happen in mixed expressions, assignments, and calls. They can lose range or precision. `static_cast<T>(value)` makes an intended supported conversion visible. Do not assume a cast validates an input or makes an out-of-range result portable.

In C++17, integer division truncates toward zero: `-11 / 4 == -2`, `-11 % 4 == -3`, and `11 % -4 == 3`. A nonzero remainder follows the dividend's sign. When the quotient is representable, `a == (a / b) * b + a % b`. Casting before division changes the calculation (`static_cast<double>(11) / 4` gives `2.75`); casting afterward cannot restore the fraction. Integer division by zero, an unrepresentable signed quotient and signed overflow have undefined behavior with no guaranteed diagnostic. We do not execute those cases. The [C++17 multiplicative rules](https://timsong-cpp.github.io/cppwp/n4659/expr.mul) resolve older implementation-defined remainder wording on the [Microsoft operator page](https://learn.microsoft.com/en-us/cpp/cpp/multiplicative-operators-and-the-modulus-operator?view=msvc-170). Floating-point values are approximations, so direct equality may not match a mathematical expectation.

### Operators and expression tracing

Separate these families:

- arithmetic: `+ - * / %`;
- relational and equality: `< <= > >= == !=`;
- logical: `! && ||`;
- bitwise: `~ & ^ | << >>`;
- assignment: `=` and compound forms such as `+=`;
- increment/decrement: `++ --`.

Precedence groups an expression; associativity resolves grouping within a level: `20 - 6 - 2` is `(20 - 6) - 2`, and `a = b = 7` is `a = (b = 7)`. Neither grants a general left-to-right evaluation order. Keep side effects in separate statements; do not infer a portable answer for `i++ + i++`, whose conflicting updates are unsequenced. Read the [precedence table](https://learn.microsoft.com/en-us/cpp/cpp/cpp-built-in-operators-precedence-and-associativity?view=msvc-170) alongside the [C++17 sequencing rules](https://timsong-cpp.github.io/cppwp/n4659/intro.execution). Parentheses are clearer than memory when intent matters. Do not confuse assignment `=` with equality `==`, logical `&&` with bitwise `&`, or a prefix increment with a postfix increment: prefix changes and yields the new value, while postfix changes the object but yields its prior value in that expression.

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

The example checks conversion failure, but **does not validate the whole line**: input `12x` produces `Quantity: 12` and leaves `x` unread. For a single integer per line, use `getline`, parse into a temporary with `istringstream`, skip trailing whitespace, and require end of input before assigning the destination. The workbook's `whole_int` accepts whitespace and a sign, rejects fractions, suffixes, empty lines and out-of-range values, and preserves the destination on rejection. Domain checks are separate: parsing `-3` does not make it a valid purchase quantity.

After failed formatted input, clear the error state and consume the bad line with `ignore(std::numeric_limits<std::streamsize>::max(), '\n')`. Clearing alone leaves the offending characters. Use `streamsize`, not an assumed `int` limit; compare [formatted extraction](https://learn.microsoft.com/en-us/cpp/standard-library/basic-istream-class?view=msvc-170) and the [C++17 ignore contract](https://timsong-cpp.github.io/cppwp/n4659/istream.unformatted). Recovery cannot manufacture input at EOF. The [formatting reference](https://learn.microsoft.com/en-us/cpp/standard-library/iomanip-functions?view=msvc-170) supports `setw`: width is a minimum and does not truncate longer values.

## 2. Flow control and functions — 28%

### Selection and repetition

`if` selects a path by a condition; an `else` binds to the nearest unmatched `if`. Braces make that ownership explicit. An `if`/`else if` chain selects at most one branch, while separate `if` statements can select several.

`switch` compares one integral or enumeration expression with constant case labels. Execution begins at a matching `case` or `default`; without `break`, it falls through into later labels. Deliberate fallthrough should be obvious. A `switch` is not a range matcher and duplicate case values are invalid.

Use `while` when continuation is tested before the body, `do ... while` when the body must run at least once, and `for` when initialization, condition, and update form a clear loop. `break` leaves the nearest loop or switch; `continue` advances to the next loop iteration. In a `for`, the update expression still occurs after `continue`; in `while`, ensure the state needed for progress is not skipped.

The outline asks you to recognize labels and `goto`. A label names a statement and `goto label;` transfers within the same function under language constraints. Understand the syntax and trace a tiny example, but prefer structured loops, functions, and early returns in normal code.

> **Related item:** A loop invariant is a fact preserved by every iteration. Write the invariant, progress step, and termination condition to uncover off-by-one and infinite-loop defects.

### Functions and parameter mechanisms

A function declaration gives its name, parameter types, and return type; a definition supplies its body; a call transfers control with arguments. A non-`void` function must produce an appropriate value on every reachable required path. A `void` function returns no value, though a bare `return;` can end it early.

These are function definitions to place before a calling `main`; the review compiled them in that context.

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
unsigned long long factorial(unsigned n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

This function fragment requires its **caller to establish `0 <= n <= 12` before converting to unsigned**. The menu below enforces that contract. `0!` and `1!` are 1; `5!` is 120; `12!` is 479001600. `unsigned long long` has enough range here; an unsigned type alone does not prevent wraparound for larger inputs. The bound also limits call depth. For `factorial(3)`, pending work is `3 * factorial(2)`, then `2 * factorial(1)`; returns unwind as 1, 2, 6.

## 3. Vectors and pointers — 24%

### Arrays, vectors, and dimensions

A built-in array has a fixed element count in its type. Indices begin at zero; valid indices end at size minus one. The language does not automatically bounds-check `array[index]`. A multidimensional array is an array whose elements are arrays, so row and column bounds must both be correct.

`std::vector<T>` from `<vector>` is a resizable sequence that owns its elements. Initialize it, query `size()`, index only valid positions, append with `push_back`, and iterate without mixing signed counters carelessly with its unsigned size type. `at()` performs bounds checking and differs from unchecked `operator[]`.

`vector.data()` returns a pointer to contiguous element storage (or a value that must not be dereferenced when there is no element). `reserve(n)` requests room without creating elements; `resize(n)` changes the number of elements (new `int` elements are zero-initialized here). Reallocation invalidates all previous element pointers, references and iterators. An append within reserved capacity preserves pointers to existing elements; the old end iterator still changes. Other operations have additional invalidation rules. Never read or compare a stale pointer to "see if it changed"; discard it before forced reallocation and reacquire `data()` afterward. See the [vector reference](https://learn.microsoft.com/en-us/cpp/standard-library/vector-class?view=msvc-170) and [C++17 capacity rules](https://timsong-cpp.github.io/cppwp/n4659/vector.capacity). A raw pointer returned by `data()` does not transfer ownership.

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

`static_cast` handles supported compile-time conversions, including explicit numeric conversion and certain related-pointer conversions. It does not add runtime proof that an assumed downcast matches the object's actual type. `dynamic_cast` performs checked conversions in a polymorphic class hierarchy; a failed pointer cast produces `nullptr`, while a failed reference cast throws. Both pointer casts are explicit in objective 3.5. In the workbook, `Temperature` and `Pressure` derive publicly from `Reading`; its virtual destructor makes it polymorphic. A safe `static_cast<Reading*>(&temperature)` goes up to the base; `dynamic_cast<Temperature*>(base)` succeeds, `dynamic_cast<Pressure*>(base)` returns null, and a null source remains null. The failed reference form throws `std::bad_cast`. We never execute an invalid static downcast. The [static_cast](https://learn.microsoft.com/en-us/cpp/cpp/static-cast-operator?view=msvc-170) and [dynamic_cast](https://learn.microsoft.com/en-us/cpp/cpp/dynamic-cast-operator?view=msvc-170) references also cover platform extensions and more advanced hierarchies. A dangling source does not acquire safety from a runtime cast.

Never use a cast merely to silence a compiler when the type relationship is not understood. No named cast repairs a dangling pointer or extends an object's lifetime.

### Dynamic storage

`new T(...)` creates a dynamically allocated object and returns a pointer. `delete p` destroys/releases a single object created by compatible single-object `new`. `new T[n]` must be paired with `delete[] p`. Losing the last pointer leaks the allocation; using a pointer after deletion dangles; deleting twice or using the wrong form has undefined behavior. Assigning `nullptr` after deletion may reduce accidental reuse of that one pointer but does not repair aliases.

This is a statement fragment for a function body; the review supplied `main` and checked the saved sum and cleared pointer after deletion.

```cpp
int* values = new int[3]{4, 5, 6};
int total = values[0] + values[1] + values[2];
delete[] values;
values = nullptr;
```

Normal throwing `new` reports allocation failure with `std::bad_alloc`; do not assume it returns null. The separate nothrow form has a different contract. See [new and delete](https://learn.microsoft.com/en-us/cpp/cpp/new-and-delete-operators?view=msvc-170). No allocation-failure simulation or deliberately invalid memory access was executed.

The practical alternative here is `std::vector<int> values{4, 5, 6};`, whose lifetime follows its owning object.

## 4. Structures and strings — 20%

### Structures and records

A `struct` defines a user-defined type whose members are public by default. Define a type, create objects, initialize fields, and use `.` with an object:

```cpp
#include <iostream>
#include <string>
#include <vector>

struct Product {
    int id;
    std::string name;
    double price;
};

int main() {
    std::vector<Product> products{
        {101, "Cable", 8.50},
        {102, "Adapter", 14.00}
    };
    products[0].price += 1.00;
    std::cout << products[0].price << '\n';
    return 0;
}
```

If `Product* p` points to an object, `p->price` is shorthand for `(*p).price`. The published objective names the dot operator, but recognizing arrow prevents confusion when structures and pointers meet. Copying a simple structure copies its members according to their own copy behavior: its `std::string` and `std::vector` members manage their own resources, unlike a raw owning pointer.

> **Related item:** A structure groups fields that belong to one record; a vector groups repeated records. This “record versus collection” distinction is a durable modeling tool across languages and databases.

### `std::string`

`std::string` from `<string>` owns a mutable character sequence. You can initialize, assign, concatenate with supported `+` combinations, append with `+=`, compare lexicographically, query `size()` or `length()`, index valid positions, and extract substrings. An empty string has no content element. In C++17, reading `s[s.size()]` returns the null sentinel, including `empty[0]`; it does not add an element. `empty.at(0)` throws `std::out_of_range`. Never write a non-null character into the sentinel or index beyond it. This differs from `vector[size()]`, which is out of bounds. See [C++17 string access](https://timsong-cpp.github.io/cppwp/n4659/string.access) and the [string reference](https://learn.microsoft.com/en-us/cpp/standard-library/basic-string-class?view=msvc-170); older const-only wording does not narrow the C++17 sentinel-read rule.

Input with `std::cin >> text` stops at formatted whitespace; `std::getline(std::cin, text)` reads a line. If formatted extraction leaves a newline before `getline`, consume or design around that delimiter. The workbook demonstrates the leftover newline and subsequent full line. The [C++17 string I/O rules](https://timsong-cpp.github.io/cppwp/n4659/string.io) explain delimiter consumption. Using `std::ws` before `getline` also discards leading whitespace and blank lines, so it is not always the right contract.

Do not confuse a `std::string`, a string literal, and a null-terminated character array. They can interoperate, but they have different types and ownership. Relational operators between `std::string` objects compare content; comparing raw character pointers compares addresses rather than the text they appear to identify.

## Executed trace workbook

**PRACTICAL DEPTH — original executable practice.** Predict each check before running this complete program with C++17 and warnings (`-std=c++17 -Wall -Wextra -pedantic`). The review used Compiler Explorer's public API without accounts or local installation; GCC 14.2 and Clang 19.1 both passed. `check` throws on a mismatch and counts each successful runtime condition; compiler acceptance is separate evidence. The small helper classes and catches expose cast and lifetime behavior, not a new advanced syllabus. No undefined-behavior example is executed.

```cpp
#include <iomanip>
#include <iostream>
#include <limits>
#include <sstream>
#include <stdexcept>
#include <string>
#include <typeinfo>
#include <vector>

int checks = 0;
void check(bool condition, const char* name) {
    if (!condition) throw std::runtime_error(name);
    ++checks;
}
bool whole_int(const std::string& line, int& value) {
    std::istringstream input(line);
    int candidate{};
    if (!(input >> candidate)) return false;
    input >> std::ws;
    if (!input.eof()) return false;
    value = candidate;
    return true;
}
int by_value(int n) { n += 5; return n; }
void by_reference(int& n) { n += 5; }
void by_pointer(int* n) { if (n != nullptr) *n += 5; }
void reseat_copy(int* n) { n = nullptr; (void)n; }
struct Reading { virtual ~Reading() = default; };
struct Temperature : Reading { int value{21}; };
struct Pressure : Reading {};
struct Counted {
    static int destroyed;
    ~Counted() { ++destroyed; }
};
int Counted::destroyed = 0;

int main(int argc, char* argv[]) {
    check(argc >= 0 && argv[argc] == nullptr, "main argument sentinel");
    int initialized{};
    initialized = 3;
    check(initialized == 3, "initialization then assignment");
    check(sizeof(char) == 1, "sizeof char is one C++ byte");
    check(true && 'A' != 'B' && 42u == 42 && 3.5f == 3.5,
          "literal categories with exactly representable values");
    check(11 / 4 == 2 && 11 % 4 == 3, "positive quotient and remainder");
    check(-11 / 4 == -2 && -11 % 4 == -3 && 11 % -4 == 3,
          "negative operands truncate toward zero");
    check(static_cast<double>(11) / 4 == 2.75, "cast before division");
    check(static_cast<double>(11 / 4) == 2.0, "cast after division");
    check(2 + 3 * 4 == 14 && (2 + 3) * 4 == 20, "precedence");
    check(20 - 6 - 2 == 12, "left grouping");
    int left{}, right{};
    left = right = 7;
    check(left == 7 && right == 7, "right grouping of assignment");
    check((6u & 3u) == 2u && (6u | 3u) == 7u && (6u ^ 3u) == 5u,
          "unsigned bitwise operations");
    check((1u << 3) == 8u && (8u >> 2) == 2u, "safe shift counts");
    check(!false && 3 < 4 && 4 >= 4 && 4 != 5, "logical and comparisons");
    int count{4};
    int old = count++;
    int fresh = ++count;
    check(old == 4 && fresh == 6 && count == 6, "separate increments");
    count += 3;
    count *= 2;
    check(count == 18, "compound assignment");
    int calls{};
    bool stop_and = false && (++calls > 0);
    bool stop_or = true || (++calls > 0);
    check(!stop_and && stop_or && calls == 0, "short circuit skips work");
    bool called = true && (++calls > 0);
    check(called && calls == 1, "right side runs when needed");
    int parsed{99};
    check(whole_int("  +12  ", parsed) && parsed == 12, "whole integer");
    check(whole_int("-3", parsed) && parsed == -3, "negative integer");
    check(whole_int("0", parsed) && parsed == 0, "zero integer");
    for (const std::string& bad : std::vector<std::string>{
            "", "   ", "word", "12x", "2.5", "1 2",
            "999999999999999999999999999999"}) {
        parsed = 77;
        check(!whole_int(bad, parsed) && parsed == 77,
              "invalid line preserves destination");
    }
    std::istringstream prefix("12x");
    prefix >> parsed;
    check(parsed == 12 && !prefix.fail() && prefix.peek() == 'x',
          "formatted numeric prefix is accepted");
    std::istringstream recovery("word\n17\n");
    recovery >> parsed;
    check(recovery.fail(), "failed numeric extraction");
    recovery.clear();
    recovery.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    recovery >> parsed;
    check(parsed == 17 && !recovery.fail(), "clear and consume bad line");
    std::istringstream lines("5\nAda Lovelace\n");
    std::string name;
    lines >> parsed;
    std::getline(lines, name);
    check(name.empty(), "leftover newline gives empty line");
    std::getline(lines, name);
    check(name == "Ada Lovelace", "whole line retains spaces");
    std::ostringstream formatted;
    formatted << std::setw(4) << 7 << 8;
    check(formatted.str() == "   78", "setw applies to next numeric field");
    int branch{};
    if (parsed < 0) branch = -1;
    else if (parsed == 5) branch = 1;
    else branch = 2;
    check(branch == 1, "one conditional branch");
    int sum{};
    for (int i = 0; i < 6; ++i) {
        if (i == 2) continue;
        if (i == 5) break;
        sum += i;
    }
    check(sum == 8, "for continue update and break");
    int visits{};
    while (visits < 0) ++visits;
    check(visits == 0, "while can run zero times");
    do { ++visits; } while (visits < 0);
    check(visits == 1, "do body runs once");
    int selected{};
    switch (2) {
        case 1: selected = 10; break;
        case 2: selected += 2; [[fallthrough]];
        default: selected += 3;
    }
    check(selected == 5, "deliberate switch fallthrough");
    int marker{};
    goto finish_trace;
    marker = 99;
finish_trace:
    check(marker == 0, "label within one function");
    int amount{10};
    int returned = by_value(amount);
    check(returned == 15 && amount == 10, "value parameter has own integer");
    by_reference(amount);
    check(amount == 15, "reference aliases caller");
    by_pointer(&amount);
    check(amount == 20, "pointer changes pointee");
    by_pointer(nullptr);
    check(amount == 20, "null is explicitly handled");
    int* pointer = &amount;
    reseat_copy(pointer);
    check(pointer == &amount, "pointer parameter itself is copied");
    { int amount{8}; check(amount == 8, "inner shadow"); }
    check(amount == 20, "outer object survives inner scope");
    int grid[2][3]{{1, 2, 3}, {4, 5, 6}};
    sum = 0;
    for (const auto& row : grid) for (int cell : row) sum += cell;
    check(sum == 21 && grid[1][2] == 6, "multidimensional bounds");
    std::vector<int> values{4, 5};
    values.reserve(8);
    check(values.size() == 2 && values.capacity() >= 8, "reserve keeps size");
    int* first = values.data();
    values.push_back(6);
    check(first == values.data() && *first == 4, "reserved append keeps pointer");
    values.resize(5);
    check(values.size() == 5 && values[3] == 0 && values[4] == 0,
          "resize creates initialized elements");
    first = nullptr;
    auto previous_capacity = values.capacity();
    values.reserve(previous_capacity + 1);
    check(values.capacity() > previous_capacity && values[0] == 4,
          "forced reallocation; discarded old pointer is never used");
    bool bounds = false;
    try { (void)values.at(values.size()); }
    catch (const std::out_of_range&) { bounds = true; }
    check(bounds, "vector checked boundary");
    const int* read_only = &amount;
    int* const fixed_pointer = &amount;
    *fixed_pointer = 22;
    check(*read_only == 22, "pointee constness differs from pointer constness");
    Temperature temperature;
    Reading* base = static_cast<Reading*>(&temperature);
    check(dynamic_cast<Temperature*>(base) == &temperature, "checked downcast");
    check(dynamic_cast<Pressure*>(base) == nullptr, "wrong pointer type fails");
    Reading* absent = nullptr;
    check(dynamic_cast<Temperature*>(absent) == nullptr, "null cast stays null");
    bool bad_cast = false;
    try { (void)dynamic_cast<Pressure&>(*base); }
    catch (const std::bad_cast&) { bad_cast = true; }
    check(bad_cast, "wrong reference type throws");
    int* single = new int{9};
    check(*single == 9, "single allocation");
    delete single;
    single = nullptr;
    check(single == nullptr, "owner variable cleared after deletion");
    int* buffer = new int[3]{4, 5, 6};
    check(buffer[0] + buffer[1] + buffer[2] == 15, "array allocation");
    delete[] buffer;
    buffer = nullptr;
    Counted* owned = new Counted[3];
    delete[] owned;
    check(Counted::destroyed == 3, "array deletion calls each destructor");
    std::string empty;
    check(empty.empty() && empty.size() == 0 && empty[0] == '\0',
          "C++17 empty string sentinel read");
    bounds = false;
    try { (void)empty.at(0); }
    catch (const std::out_of_range&) { bounds = true; }
    check(bounds, "empty string has no content element");
    std::string text{"Ada"};
    text += " Lovelace";
    check(text.size() == 12 && text.substr(4, 8) == "Lovelace", "append and slice");
    check(std::string("12") < std::string("2"), "text comparison is not numeric");
    std::string copy = text;
    copy[0] = 'E';
    check(text[0] == 'A' && copy[0] == 'E', "string value copy");
    std::cout << checks << " checks passed\n";
}
```

## Integrated scenarios

These are original worked programs. Monetary values and business limits are fictional. Input and arithmetic bounds are part of each program's contract. Each block is a separate translation unit with its own `main`.

### Scenario 1: Inventory valuation

The request is one line with exactly two integers. Parsing, catalog integrity, quantity range and lookup are separate checks. Integer cents avoid decimal rounding: 1,000,000 cents times at most 1,000 units fits in `long long`. Duplicate IDs invalidate the catalog; an empty catalog has no match. Rejection leaves the caller's total unchanged.

```cpp
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

struct Product {
    int id;
    std::string name;
    long long price_cents;
};
bool valid_catalog(const std::vector<Product>& products) {
    for (std::size_t i = 0; i < products.size(); ++i) {
        if (products[i].id <= 0 || products[i].name.empty() ||
            products[i].price_cents < 0 || products[i].price_cents > 1000000)
            return false;
        for (std::size_t j = 0; j < i; ++j)
            if (products[i].id == products[j].id) return false;
    }
    return true;
}
std::string quote(const std::vector<Product>& products, int id, int quantity,
                  long long& total) {
    if (!valid_catalog(products)) return "Invalid catalog";
    if (quantity < 1 || quantity > 1000) return "Quantity must be 1..1000";
    for (const Product& product : products) {
        if (product.id == id) {
            total = product.price_cents * quantity;
            return "OK";
        }
    }
    return "Unknown product";
}
int main() {
    const std::vector<Product> products{{101, "Cable", 850}, {102, "Adapter", 1400}};
    std::string line;
    int id{}, quantity{};
    if (!std::getline(std::cin, line)) {
        std::cerr << "Missing request\n";
        return 1;
    }
    std::istringstream input(line);
    if (!(input >> id >> quantity)) {
        std::cerr << "Use: product-id quantity\n";
        return 1;
    }
    input >> std::ws;
    if (!input.eof()) {
        std::cerr << "Unexpected trailing input\n";
        return 1;
    }
    long long total{};
    std::string status = quote(products, id, quantity, total);
    if (status != "OK") {
        std::cerr << status << '\n';
        return 1;
    }
    std::cout << "ID " << std::setw(3) << id << " cents " << total << '\n';
    return 0;
}
```

Input `101 3` prints `ID 101 cents 2550`; `102 1` prints `ID 102 cents 1400`. `101 0`, `101 -1` and `101 1001` fail the quantity contract. `101 2x` fails whole-line validation; an unknown ID reports a missing product. The review also calls `quote` directly for empty/duplicate catalogs, zero and maximum prices, and valid quantity boundaries. These helper checks do not imply the console program loads arbitrary catalogs.

### Scenario 2: Sensor buffer

One summary function accepts a fixed array or live vector storage. A reference identifies the total destination; a null output pointer means no highest-reading result is requested. Empty input has no maximum and returns false without changing outputs. A pointer plus count cannot prove storage validity: the caller must provide enough live elements. Count/range checks bound arithmetic.

```cpp
#include <cstddef>
#include <iostream>
#include <vector>

// Contract: at most 100 readings, each in -1000..1000.
// A non-null data pointer must designate at least count live elements.
bool summarize(const int* data, std::size_t count, long long& total, int* highest) {
    if (count == 0 || count > 100 || data == nullptr) return false;
    long long candidate_total{};
    int candidate_high = data[0];
    for (std::size_t i = 0; i < count; ++i) {
        if (data[i] < -1000 || data[i] > 1000) return false;
        candidate_total += data[i];
        if (data[i] > candidate_high) candidate_high = data[i];
    }
    total = candidate_total;
    if (highest != nullptr) *highest = candidate_high;
    return true;
}
int main() {
    int fixed[3]{12, 18, 23};
    std::vector<int> owned{12, 18, 23};
    long long total{};
    int highest{};
    if (!summarize(fixed, 3, total, &highest)) return 1;
    std::cout << "array " << total << ' ' << highest << '\n';
    if (!summarize(owned.data(), owned.size(), total, &highest)) return 1;
    std::cout << "vector " << total << ' ' << highest << '\n';
    owned.reserve(10);
    int* saved = owned.data();
    owned.push_back(24); // Fits reserved capacity; saved still designates first element.
    std::cout << "first " << *saved << '\n';
    saved = nullptr;
    owned.reserve(owned.capacity() + 1); // Reallocates; old addresses are discarded.
    if (!summarize(owned.data(), owned.size(), total, nullptr)) return 1;
    std::cout << "expanded " << total << '\n';
    return 0;
}
```

Output is `array 53 23`, `vector 53 23`, `first 12`, then `expanded 77`, one per line. The workbook separately covers two-dimensional arrays and paired manual allocation. The review tests empty/null input, optional output, negative readings, range rejection and count boundaries; it never dereferences or compares an invalidated address.

### Scenario 3: Menu and recursive calculation

Each line is `s a b`, `p a b`, `f n` or `q`. Sum/product operands are restricted to -1000..1000; factorial accepts 0..12 before conversion to unsigned. Malformed input reports a diagnostic and exits with code 1; EOF or `q` exits successfully. An empty line is malformed. No operation uses a guessed value after extraction fails.

```cpp
#include <iostream>
#include <sstream>
#include <string>

// Caller establishes n <= 12. This bound also keeps recursion deliberately small.
unsigned long long factorial(unsigned n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
int main() {
    bool running = true;
    do {
        std::string line;
        if (!std::getline(std::cin, line)) return 0;
        std::istringstream input(line);
        char choice{};
        long long a{}, b{};
        if (!(input >> choice)) {
            std::cerr << "Missing choice\n";
            return 1;
        }
        if (choice == 's' || choice == 'p') {
            if (!(input >> a >> b) || a < -1000 || a > 1000 || b < -1000 || b > 1000) {
                std::cerr << "Use two integers in -1000..1000\n";
                return 1;
            }
        } else if (choice == 'f') {
            if (!(input >> a) || a < 0 || a > 12) {
                std::cerr << "Factorial needs 0..12\n";
                return 1;
            }
        }
        input >> std::ws;
        if (!input.eof()) {
            std::cerr << "Unexpected trailing input\n";
            return 1;
        }
        switch (choice) {
            case 's': std::cout << a + b << '\n'; break;
            case 'p': std::cout << a * b << '\n'; break;
            case 'f': std::cout << factorial(static_cast<unsigned>(a)) << '\n'; break;
            case 'q': running = false; break;
            default: std::cerr << "Unknown choice\n"; return 1;
        }
    } while (running);
    return 0;
}
```

Lines `s 7 -2`, `p -3 4`, `f 0`, `f 5`, `f 12`, `q` produce 5, -12, 1, 120 and 479001600. `f -1`, `f 13`, `f 2x`, missing operands, extra tokens and unknown choices are rejection cases. Every arithmetic case ends with `break`; the workbook has a separate deliberate fallthrough example. These are selected remote program checks, not a completed interactive learner session.

## Hands-on labs

These eight broader activities remain **proposed**. Remote execution of worked examples is recorded separately; debugger sessions, sanitizer runs and all learner variations are not claimed.

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
13. The next applicable formatted field. Width is a minimum, not truncation; `setw(4) << 7 << 8` prints three spaces followed by `78`.
14. Detect failed state; clear and consume bad input or exit. Success alone does not reject `12x`: whole-line validation checks the suffix, and domain limits are separate.
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
25. A reachable base case, progress and an input/range contract. The factorial caller validates 0..12 before unsigned conversion; separate calls unwind their results.
26. Scope is where a name is visible; lifetime is when its object exists.
27. Index `4`.
28. A built-in array has fixed extent; a vector owns a resizable element sequence.
29. Vector `at()` throws `std::out_of_range` for an invalid index; `[]` requires an existing element. The C++17 string sentinel is a separate rule.
30. Reallocation invalidates all element pointers/references. Reserve changes capacity without size; resize changes size. Appending within reserved capacity preserves existing element addresses. Other operations have further invalidation rules.
31. `&` obtains an object's address; unary `*` accesses the object designated by a valid pointer.
32. A reference aliases a required object and is not reseated; a pointer is a reseatable object and may be null.
33. Dereferencing null has undefined behavior.
34. Checked downcasts use a polymorphic source; dynamic pointer failure returns null, reference failure throws `std::bad_cast`. Static casts do not prove dynamic type. Both pointer casts are objective 3.5; neither repairs an invalid lifetime.
35. `delete`.
36. `delete[]`.
37. Unreleased storage; a pointer whose target lifetime ended; and deallocating the same allocation more than once.
38. `object.member` uses `.`, while `pointer->member` is shorthand for `(*pointer).member`.
39. Formatted extraction stops at whitespace; `getline` reads through a delimiter and can encounter a newline left by earlier extraction.
40. Recheck the active code, 26 objectives, format, price, language, delivery and policies. CLE/CPE currently has a seven-day failed-retake wait; the separate 15-day associate/professional rule does not apply.

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
| [OpenEDG C++ Essentials 1](https://edube.org/study/cppe1) | Free account; public listing read, lessons not entered | 42 hours listed; 7 hours/week suggested |
| [Cisco Networking Academy C++ Essentials 1](https://www.netacad.com/courses/c-plus-plus-essentials-1?courseLang=en-US) | Free account; application shell retrieved | 35–45 hours is an author estimate; provider duration unverified |
| [Microsoft C++ console calculator tutorial](https://learn.microsoft.com/en-us/cpp/get-started/tutorial-console-cpp?view=msvc-170) | Free; selected setup, calculator and validation sections read | 1–2 hours plus variations is an author estimate |
| [cppreference C++ language reference](https://en.cppreference.com/cpp/language) | Free third-party index; linked chapters not fully reviewed | 3–6 hours targeted lookup is an author estimate |
| [Pluralsight C++ path](https://www.pluralsight.com/paths/c-plus-plus) | Subscription; public listing: 13 courses/44 hours; lessons not watched | First two: 5h19m + 5h48m = 11h07m; full path exceeds CPE scope |
| [O'Reilly C++ Crash Course](https://www.oreilly.com/library/view/c-crash-course/9781098122553/) | Subscription; HTTP 403; prior 19h42m not reverified | Select early chapters; 8–12 hours is an author estimate |
| [Udemy Beginning C++ Programming — From Beginner to Beyond](https://www.udemy.com/course/beginning-c-plus-plus-programming/) | Paid marketplace; HTTP 403; prior 45h51m not reverified | Select fundamentals/pointers; 15–25 hours is an author estimate |
| [freeCodeCamp C++ Tutorial for Beginners](https://www.youtube.com/watch?v=vLnPwxZdW4Y) | Free; title/shell only, no playback or transcript | Prior approximately 4h02m not reverified; add coding time |

**Source boundaries and conflicts:** The [exam page](https://cppinstitute.org/cpe), [catalog](https://cppinstitute.org/certification-exams) and [policies](https://cppinstitute.org/exam-policies) were read through a public web reader after direct timeouts. The objective monitor did not complete a successful hash comparison; snapshots were retained after manual comparison. Policies separate TestNow CLE/CPE from Pearson VUE associate/professional exams: use CPE-specific delivery and its seven-day failed-retake wait. No booking/account UI was inspected.

The Edube listing confirms 42 hours and C++ Essentials 1, but contains inconsistent C-language/CLE-20-01 labels and obsolete standards prose; those copy errors do not replace the current CPE blueprint. Microsoft's calculator demonstrates an IDE workflow, but its shown loop does not fully handle failed input/EOF. Older Microsoft reference wording about remainder signs, string sentinel constness and ignore's maximum count is reconciled against the C++17 draft. Successful HTTP retrieval is not proof of rendered course content. No paid lessons, official practice items, video playback, IDE installation or local C++ execution were claimed. [Compiler Explorer API documentation](https://github.com/compiler-explorer/compiler-explorer/blob/main/docs/API.md) was read for the remote execution interface; only original public examples were submitted.

No exact current MeasureUp or Whizlabs CPE-20-01 practice product was verified during this review. Prefer the provider-aligned course assessments and your own objective-based code checks over products that do not state the active exam version.
