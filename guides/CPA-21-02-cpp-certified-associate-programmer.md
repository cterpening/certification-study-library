---
exam_code: CPA-21-02
vendor_id: cpp-institute
official_blueprint: https://cppinstitute.org/cpa
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# CPA-21-02 C++ Certified Associate Programmer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, links, lifecycle, and exam-integrity compliance were checked September 29, 2026. This does not guarantee that every explanation is error-free or remains current. The [official CPA page and syllabus](https://cppinstitute.org/cpa) are authoritative.

**Current baseline:** CPA-21-02, active; CPA-21-01 retired; five-block syllabus last updated July 22, 2025<br>
**Upcoming blueprint change:** none announced on the official exam or certification-catalog pages when checked<br>
**Official delivery snapshot:** 40 single- and multiple-choice questions; 65-minute exam plus approximately 10 minutes for the NDA/tutorial; 70% cumulative passing score on a normalized maximum of 200 points; Pearson VUE/OnVUE; English<br>
**Purchase snapshot:** no formal prerequisite; from USD 325 exam or USD 375 exam-plus-retake when checked<br>

## How to use this guide

CPA is the bridge from procedural C++ to object-oriented design. You need to trace expressions and memory, but almost one-third of the published weighting is classes and namespaces. For every class exercise, draw object lifetime, base/derived subobjects, access, virtual dispatch, ownership, copy behavior, and exception paths.

Use this loop:

1. map the problem to the five official blocks;
2. predict compilation, overload choice, lifetime, dispatch, state, output, or exception;
3. compile in a declared standard mode with strong warnings;
4. use debugger and address/undefined-behavior diagnostics where available;
5. test construction, copying, inheritance, error, and cleanup paths.

**CURRENT BLUEPRINT:** The five blocks contain **35 numbered objectives**, not 40 objectives: 40 is the question count. **PRACTICAL DEPTH:** This workbook deliberately uses C++17; that is a teaching baseline, not a newly discovered exam-mandated compiler version. Binary literals require C++14 or later. Recognize older constructs under the language mode actually specified.

The exception-specification timeline matters: typed `throw(T)` was deprecated in C++11 and removed in C++17. Empty `throw()` remained valid but deprecated in C++17, equivalent to `noexcept(true)`, and was removed in C++20. Use `noexcept` in new examples. Compiler acceptance alone does not establish standard validity; see the observed mode matrix below.

> **About related items:** A `Related item:` callout supplies adjacent, prerequisite, operational, or modern-practice context. It helps you understand an objective; it does not claim that the extra item appears verbatim in the exam blueprint.

## Weighted objective map

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| 1. Types and Operators | 9 | 24.5% | Trace types, conversions, strings, aggregates, literals, and expressions |
| 2. Control and Exceptions | 8 | 18% | Trace all paths and explain exception matching/unwinding |
| 3. Functions and Preprocessor | 9 | 17.5% | Resolve overloads/defaults, pass correctly, recurse, and expand macros |
| 4. Pointers | 4 | 11% | Prove pointer targets/ranges and manual allocation cleanup |
| 5. Classes and Namespaces | 10 | 29% | Design, construct, copy, inherit, dispatch, cast, overload, and organize types |

The weights total 100% and the item counts total 40. Because questions are weighted and scores normalized, do not turn 70% into a guaranteed count of ordinary correct answers. The automated objective monitor timed out; manual comparison of the complete canonical July 22, 2025 syllabus retained the existing snapshot.

### Every numbered objective

| Block | Explicit coverage in the corresponding section and workbook |
|---|---|
| 1 — nine objectives | 1.1 operator forms/precedence; 1.2 operator families/short circuit; 1.3 conditional expressions; 1.4 types/ranges; 1.5 literals; 1.6 strings; 1.7 aggregates/containers/enums; 1.8 conversions/casts/sizeof; 1.9 modifiers |
| 2 — five | 2.1 control transfers; 2.2 switch; 2.3 return; 2.4 exception handling; 2.5 hierarchies/legacy specifications |
| 3 — eight | 3.1 declarations/definitions/calls; 3.2 typed/void functions; 3.3 overloads/defaults; 3.4 parameter passing; 3.5 recursion; 3.6 main; 3.7 conditional compilation; 3.8 macros |
| 4 — four | 4.1 pointer targets; 4.2 address/dereference; 4.3 ranges/comparisons; 4.4 allocation/deallocation/leaks |
| 5 — nine | 5.1 OOP principles; 5.2 access/scope/this; 5.3 special members; 5.4 member/operator overloading; 5.5 inheritance/access; 5.6 hierarchy conversions; 5.7 overrides/const; 5.8 friends; 5.9 namespaces |

### Booking and resource boundaries

**VERIFY CURRENT:** The [canonical exam page](https://cppinstitute.org/cpa) lists no formal prerequisite, active CPA-21-02, retired CPA-21-01, English, Pearson VUE/OnVUE and USD 325/375 purchase options. The [exam policies](https://cppinstitute.org/exam-policies) distinguish the 15-day failed-retake wait for Pearson associate/professional exams from seven days for entry-level TestNow. Public rescheduling wording differs between anytime before an appointment and 24 hours; check actual appointment terms. The [Pearson scheduling page](https://cppinstitute.org/schedule-exam-pvue) includes CPA. No booking, account, system test or eligibility determination was performed.

Both Edube course landings list 42 hours, but Part 1's associated-certification field says CLE/CLE-20-01 and Part 2 says CLA-21-02 despite C++/CPA course context. These appear to be editorial errors; the canonical exam syllabus controls scope. Cisco returned an application shell. Paid course interiors were not accessible. Public landings and selected reference sections are not equivalent to completing a course.

## 1. Types and operators — 24.5%

### Types, literals, and conversions

Know integral, character, Boolean, and floating families; exact-width/range assumptions must be verified rather than guessed. Literal spelling determines candidate type: decimal, octal, hexadecimal, binary where supported by the baseline, floating suffixes, character/string literals, and `true`/`false`.

Integral promotions and usual arithmetic conversions affect mixed expressions. Signed/unsigned comparison can transform a negative value unexpectedly. `static_cast` expresses supported conversions; `dynamic_cast` checks polymorphic hierarchy conversions at runtime; `const_cast` changes cv qualification; `reinterpret_cast` expresses low-level reinterpretation with strict safety limits. A cast does not repair lifetime or ownership.

`sizeof` yields the size of a type/object representation in bytes of `char`; its expression operand is unevaluated in ISO C++. Padding and alignment mean class/struct size is not just the arithmetic sum of members.

### Operators and expression tracing

Understand unary, binary, and conditional operators; arithmetic, comparison, logical, bitwise, assignment, increment/decrement, and short-circuit rules. Precedence groups syntax; it is not a universal evaluation-order rule. Parentheses communicate intent. Avoid expressions that modify/read one scalar without defined sequencing.

Logical `&&`/`||` short-circuit and yield `bool`; bitwise operators work on promoted integral representations. The conditional operator selects one of two expressions and has type-combination rules—not merely “compact if.”

### Strings and aggregates

`std::string` owns a sequence and supports `size`, comparison, `substr`, `insert`, and other operations. Check position/count behavior and distinguish character indexing from substring creation. A string literal and `std::string` are different types and lifetimes.

Arrays own fixed sequences; vectors own resizable sequences. Structures/classes group members. A union's members share storage and active-member rules matter. Scoped and unscoped enumerations differ in qualification/conversion behavior. `const` restricts modification through a particular object/access path; `static` meaning depends on context.

> **Related item:** Prefer enum classes, containers, and explicit conversions in new code. You still need to recognize older idioms because the blueprint spans core and legacy constructs.

### Boundary cases worth predicting

`sizeof(array)` measures the whole array while the array type is preserved; a function parameter declared `int a[]` is adjusted to a pointer. `sizeof(seven())` in the workbook does not call `seven`. Required type/access checks still apply to an unevaluated operand. Variable-length arrays accepted as compiler extensions do not create an ISO C++ exception to this rule. [C++17 draft sizeof](https://timsong-cpp.github.io/cppwp/n4659/expr.sizeof)

Unsigned arithmetic wraps modulo its representable range; signed overflow is undefined. Converting a negative integer to unsigned follows unsigned conversion rules and may change a comparison's meaning. Floating-to-integer conversion truncates toward zero only when the resulting value fits. The workbook uses bounded inputs and does not execute overflow or invalid conversion cases.

`string::compare` promises a negative, zero or positive result, not exactly -1/0/+1. `substr(size())` is empty, `substr(pos)` beyond size throws, and an excessive count is clipped to the remaining characters. `at(size())` throws; in C++17 `operator[](size())` permits reading the terminating zero, but this is not an ordinary element to overwrite with a nonzero character. `insert(0, ...)` prepends and `insert(size(), ...)` appends. [Comparison reference](https://learn.microsoft.com/en-us/cpp/standard-library/basic-string-class?view=msvc-170), [substring](https://timsong-cpp.github.io/cppwp/n4659/string.substr), [access](https://timsong-cpp.github.io/cppwp/n4659/string.access), [insertion](https://timsong-cpp.github.io/cppwp/n4659/string.insert)

`vector::reserve` changes capacity when reallocation is required and leaves size unchanged. Reallocation invalidates all element references, pointers and iterators; reacquire them afterward. The example never dereferences a stale observer. A trivial union assignment establishes the member used next; reading another inactive member is not a general portable conversion technique. [Vector capacity](https://timsong-cpp.github.io/cppwp/n4659/vector.capacity)

An assignment through `condition ? a : b` requires the result to be an assignable expression. Two `int` lvalues can preserve that property; mixing `int` and `short` in this example produces a converted value and rejects assignment. The latter is retained only as a compilation diagnostic. Precedence and associativity still do not supply a general left-to-right evaluation rule. [Execution and sequencing](https://timsong-cpp.github.io/cppwp/n4659/intro.execution)

## 2. Control and exceptions — 18%

Trace `if`, `switch`, `while`, `do`, `for`, `break`, `continue`, `goto`, and `return`. `else` binds to the nearest unmatched `if`; `switch` falls through without a transfer. `continue` in a `for` proceeds to the update. A return ends the current function, triggering destruction of automatic objects whose scopes are exited normally.

`throw expression` creates/initializes an exception object. Stack unwinding destroys fully constructed automatic objects between the throw and matching handler. Handlers are considered in order; catch by reference avoids slicing and copying. `catch (...)` catches otherwise unmatched exceptions but supplies no typed object. A `throw;` inside a handler rethrows the current exception.

The complete `hierarchy.cpp` below throws an original `InputError`, observes reverse destruction through two calls, catches the derived type first and rethrows with `throw;`. Its fixed-capacity trace does not allocate in a destructor.

Place derived handlers before base handlers. Destructors should not let exceptions escape during unwinding. Resource-owning objects provide cleanup through destruction.

The legacy `throw()` specification historically promised no escaping exception in older modes; it is not a modern substitute to memorize without version context. `noexcept` is the current related mechanism and affects termination/optimization and some library choices.

> **Related item:** RAII binds a resource to object lifetime so returns and exceptions use the same cleanup path. It is the central connection between classes, exceptions, and memory safety.

### Unwinding, matching and language versions

Handlers match types and permitted hierarchy/pointer relationships, not arbitrary arithmetic conversions: an `int` exception is not caught by `catch(double)`. An earlier public base handler can hide a later derived handler. `throw;` preserves the current exception, while `throw e;` creates a new exception from the expression and can slice a base reference. Catch where recovery or useful translation is possible; RAII handles cleanup without redundant catch/rethrow blocks. [Handler rules](https://timsong-cpp.github.io/cppwp/n4659/except.handle), [Core Guidelines E.6/E.15/E.17](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)

If an ordinary nondelegating constructor throws before the complete object is constructed, completed bases/members are destroyed in reverse completion order; that incomplete object's destructor is not called. A delegating constructor whose target completed has different complete-object destruction behavior. The workbook demonstrates the ordinary case: `BXYDyxb` lacks the derived destructor's `d`, while normal destruction produces `BXYDdyxb`. Unwinding with no matching handler is not guaranteed to complete before termination. [Construction and exceptions](https://timsong-cpp.github.io/cppwp/n4659/except.ctor)

| Form | C++11/14 | C++17 | C++20 |
|---|---|---|---|
| `throw(int)` | Valid but deprecated dynamic specification | Removed | Removed |
| `throw()` | Deprecated nonthrowing dynamic specification | Deprecated alias of `noexcept(true)` | Removed |
| `noexcept` | Nonthrowing specification | Nonthrowing specification | Nonthrowing specification |

An escaping exception crossing a C++17 nonthrowing boundary calls `std::terminate`; `noexcept` does not prove that the body contains no throwing call. Older dynamic specifications used the historical `unexpected` mechanism. An override cannot loosen a base's nonthrowing contract. Destructors and cleanup should not propagate failures. [C++11 specifications](https://timsong-cpp.github.io/cppwp/n3337/except.spec), [C++17 specifications](https://timsong-cpp.github.io/cppwp/n4659/except.spec), [C++20 removal](https://timsong-cpp.github.io/cppwp/n4861/diff.cpp17.except)

In ten separate hosted probes, GCC 15.2 and Clang 20.1 each ran a C++17 smoke program, accepted empty `throw()` in C++17, accepted typed `throw(int)` in C++14, and rejected typed `throw(int)` in C++17. Both also accepted empty `throw()` with `-std=c++20 -Wall -Wextra -Wpedantic` without a diagnostic. That last observation is compiler acceptance of a removed form, not evidence that the C++20 grammar permits it. GCC warned on the C++14 typed form; Clang did not under these flags. No probe threw through a nonthrowing boundary.

## 3. Functions and preprocessor — 17.5%

### Calls, overloads, defaults, and recursion

A declaration states a function signature; a definition provides the body. Overload resolution forms viable candidates, ranks conversions, and selects a best match or diagnoses ambiguity. Return type alone cannot distinguish overloads. Default arguments are supplied at the call site from visible declarations and should generally be stated once.

Pass by value creates a parameter object, reference parameters alias a caller object, pointer parameters receive an address value and can represent null. Use `const T&` for required non-mutating access to an existing object where copying is undesirable. Understand that reseating a pointer parameter does not reseat the caller's pointer unless another level of indirection/reference is used.

Recursion needs a reachable base case and progress and consumes finite stack resources. `main` has standard forms returning `int`; do not invent `void main` as portable C++.

### Preprocessing

`#include`, `#define`, `#if`, `#ifdef`, `#else`, and `#endif` act before C++ parsing. Function-like macros perform token substitution without types or single-evaluation guarantees. Parenthesize parameters and replacement expressions, but prefer functions/templates when evaluation and types matter.

Use conditional compilation for true build/platform variation, not ordinary runtime business logic. Inspect preprocessed output to understand expansion and guard against duplicate definitions through include guards or equivalent facilities.

### Resolving a call before predicting its body

For ordinary standard conversions, an exact match ranks above a promotion, which ranks above a conversion. With `choose(int)` and `choose(double)`, a `short` promotes to `int`; with `choose(long)` and `choose(double)`, an `int` argument leaves competing conversions and is ambiguous. Multi-argument ranking requires one candidate to be no worse for every argument and better for at least one, subject to further tie-breakers. The diagnostic workbook also rejects return-type-only overloading. [Selected overload rules](https://timsong-cpp.github.io/cppwp/n4659/over.match.best)

Default arguments belong to visible declarations and are selected using the static type at the call site. Virtual dispatch can then choose a derived implementation: the workbook gets 21 through `CallBase&` and 22 through `CallDerived`, using defaults 1 and 2 respectively. Explicit qualification suppresses virtual dispatch. Defaults are not part of the function type and must not be redefined in the same scope. [Default arguments](https://timsong-cpp.github.io/cppwp/n4659/dcl.fct.default), [virtual calls](https://timsong-cpp.github.io/cppwp/n4659/class.virtual)

A `void` function performs work without returning a value; a typed function must supply a value on every required returning path. Falling off hosted `main` is specifically equivalent to returning zero. `return` from `main` destroys its automatic objects; calling `std::exit` directly does not unwind them. The portable hosted forms are `int main()` and `int main(int, char**)`; `argv[argc]` is null and argument presence must be checked before indexing. [main rules](https://timsong-cpp.github.io/cppwp/n4659/basic.start.main)

The macro workbook calls a function twice rather than placing two unsequenced ordinary increments in one expression. Its counter observes two calls versus one for an inline function. Function executions do not interleave in this single-threaded case. Parentheses do not fix repeated evaluation. `PRACTICE_LEVEL` selects one compiled branch; an additional build exercises level 2. The recursive factorial rejects values above 12 before multiplication and handles zero explicitly.

## 4. Pointers — 11%

A pointer object stores an address/null and has its own lifetime. `&object` obtains an address; `*pointer` designates a valid target. `nullptr` is the null-pointer literal. Pointers can target objects, array elements, functions, or aggregate members with compatible types.

For ordinary array traversal, prove that pointer arithmetic, subtraction and relational comparisons stay within the same array, including its one-past position. Equality comparisons with null or other object pointers do not have that same-array precondition. A one-past pointer may be formed/compared but not dereferenced. Function pointers enable callbacks; their declaration and invocation types must match.

`new T(...)` creates an object and `delete` destroys/releases it. `new T[n]` pairs with `delete[]`. Leaks, use-after-free, double deletion, mismatch, and exception paths make raw ownership fragile.

The complete `Buffer` below demonstrates actual `new[]`/`delete[]` ownership, checked access, deep copying and exception-safe assignment. The earlier cleanup fragment was a valid ownership pattern when completed correctly, but left its types and operations undefined.

This illustrates why direct ownership should normally be replaced by an automatic object or smart owner; CPA still requires understanding the raw operations.

> **Related item:** `std::unique_ptr` represents single ownership and is the default related replacement for a raw owning pointer. Raw pointers remain useful non-owning observers when lifetime is guaranteed elsewhere.

### Allocation is a construction operation

Distinguish a new-expression from the allocation function `operator new`: the expression obtains storage and initializes an object. Ordinary throwing allocation reports failure with `std::bad_alloc`; a nothrow allocation form can return null, but a subsequently invoked constructor can still throw. If construction throws, matching deallocation normally releases the acquired storage. A zero-length array allocation is permitted; this workbook instead represents an empty buffer as `{0, nullptr}`. [New expressions](https://timsong-cpp.github.io/cppwp/n4659/expr.new)

Match scalar/array deletion, accept null deletion, and delete only an owned allocation with the correct contract. In the C++17 baseline, deleting a derived object through a base pointer without the required virtual destructor is undefined behavior; it is not a portable demonstration of “only the base destructor runs.” The guide does not execute it. [Delete expressions](https://timsong-cpp.github.io/cppwp/n4659/expr.delete)

`Buffer::fail_next_allocation` is a deterministic single-threaded test seam before actual allocation. It verifies the caller's failure behavior, not operating-system exhaustion, allocator hooks or `new_handler` recovery. The manual owner bounds size to 32 and uses zero initialization; `ContainerBuffer` demonstrates how a vector member removes the need for custom ownership special members.

## 5. Classes and namespaces — 29%

### Encapsulation, construction, and copying

A class defines state and operations. Access specifiers control member accessibility; encapsulation protects invariants rather than merely hiding fields. `this` points to the current object inside a non-static member. `ClassName::member` uses scope resolution; a static member belongs to the class rather than each object.

Constructors establish invariants. Use member-initializer lists; members initialize in declaration order, not list order. `explicit` prevents unintended converting construction in applicable contexts. A destructor releases owned resources. A copy constructor creates an object from another; copy assignment replaces an already-live object's state. Compiler-generated copying performs memberwise operations, which is unsafe when a raw member uniquely owns a resource.

The rule of three connects destructor, copy constructor, and copy assignment for manual resource ownership. Modern rule-of-zero/five is related context, but you must first understand the tested copy/destruction mechanics.

Operator overloads implement language operators for user-defined types. At least one operand must involve an appropriate user-defined type; precedence, associativity, and operand count do not change. Preserve familiar semantics and const-correctness.

### Inheritance and polymorphism

Inheritance models an accessible base subobject plus derived additions. Public/protected/private inheritance and member access are distinct concepts. Multiple inheritance can create ambiguity and repeated base subobjects; virtual inheritance is related advanced context.

Virtual functions enable dynamic dispatch through a base pointer/reference. Override signatures must match; use `override` in modern code to request compiler checking. A polymorphic base intended for deletion through a base pointer needs a virtual destructor. Passing/storing a derived object by base value slices the derived portion.

`dynamic_cast` safely checks down/cross-casts within a polymorphic hierarchy: a failed pointer conversion yields null and a failed reference conversion throws `std::bad_cast`. `static_cast` can express certain hierarchy conversions but does not validate the dynamic type.

The complete hierarchy workbook below defines an abstract `Shape`, concrete rectangle/circle types, a collection of `unique_ptr<Shape>`, public multiple inheritance and successful/failed checked casts.

Friend declarations grant access to the named function/class; a free friend function does not become a member of the granting class. Friendship can weaken encapsulation if overused. Use them when an operation genuinely needs symmetric/non-member access, not as a default escape hatch.

### Namespaces

Named namespaces organize declarations and avoid collisions. `namespace alias = long_name;` shortens qualification. An unnamed namespace gives internal linkage to eligible names in that translation unit. A broad `using namespace` directive in a header pollutes every includer; prefer qualification or narrow using-declarations.

> **Related item:** Abstract interfaces and composition often reduce coupling compared with deep inheritance. The exam requires inheritance mechanics; design still asks whether inheritance is the right relationship.

### Invariants across copying, construction and access

`Buffer` maintains size at most 32 and uniquely owns exactly that many initialized integers when nonempty. Its copy constructor creates independent storage. Copy assignment builds a temporary before a nonthrowing swap, so an allocation exception preserves the destination. Self-copy and self-move are deliberate no-ops; other moves leave the source empty and usable. Empty copies do not form ranges from null pointers. The static counter belongs to the class and measures this owner's live blocks, not all process allocations. [Copy constructors](https://timsong-cpp.github.io/cppwp/n4659/class.copy.ctor), [assignment](https://timsong-cpp.github.io/cppwp/n4659/class.copy.assign)

Ordinary nondelegating construction initializes virtual bases for the most-derived object, direct bases in declaration order, members in declaration order, then the body. Writing a different initializer-list order does not change that sequence. During construction/destruction, a virtual call on the current object dispatches within the current constructor/destructor class, not to a not-yet-constructed or already-destroyed derived part. The workbook's base initializer observes kind 1; the completed object observes kind 2. [Initialization](https://timsong-cpp.github.io/cppwp/n4659/class.base.init), [construction dispatch](https://timsong-cpp.github.io/cppwp/n4659/class.cdtor)

| Inheritance mode | Base public members become | Base protected members become | Outside implicit derived-to-base conversion |
|---|---|---|---|
| Public | Public | Protected | Available if unambiguous |
| Protected | Protected | Protected | Restricted by access |
| Private | Private | Private | Restricted by access |

Base private state still exists but cannot be accessed directly by a derived member. A const object permits applicable const member calls; mismatching `const` in a purported override is diagnosed with `override`. A friend equality operator can inspect two buffers symmetrically without exposing their storage.

Runtime down/cross-casts generally require a polymorphic source and an accessible, unambiguous relationship. A simple permitted upcast does not require a virtual function merely because it uses `dynamic_cast`. Pointer failure yields null; reference failure throws `bad_cast`. `static_cast` downcasts do not validate dynamic type, so the workbook uses one only after establishing the actual rectangle object. A `const_cast` cannot make modifying an originally const object valid, and `reinterpret_cast` does not establish an object's lifetime. [dynamic_cast](https://timsong-cpp.github.io/cppwp/n4659/expr.dynamic.cast), [static_cast](https://timsong-cpp.github.io/cppwp/n4659/expr.static.cast)

Rule-of-zero/five guidance is design advice alongside language rules. The manual class explicitly supplies all five ownership special members; its vector counterpart supplies none. A public virtual base destructor supports owned polymorphic deletion; a protected nonvirtual destructor can instead prevent that deletion interface. [Core Guidelines C.20/C.21/C.35/C.82](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)

## Original executable workbook

Save these six files together. The CMake example uses GCC/Clang warning flags; it is not an MSVC build recipe. On an existing suitable toolchain, configure with `cmake -S . -B build`, build with `cmake --build build`, then run `checks`, `language` and `hierarchy` from the build directory. No local compiler or package installation was performed for this review.

Thirteen hosted CMake build/runs passed: all three programs with GCC 15.2 and Clang 20.1, three GCC optimized variants, the alternative language macro branch, and three Clang AddressSanitizer/UndefinedBehaviorSanitizer variants. Each final CMake build compiles all three targets before executing the selected one. GCC uses its 15.2 standard-library toolchain; hosted Clang reports the GCC 14.2 external toolchain. These results do not establish MSVC/libc++ portability or complete language conformance.

Expected output is `buffer: 50 checks; live blocks=0`, `language: 49 checks; level=1` (or level 2), and `hierarchy: 20 checks; lifetime and dispatch passed`. Checks remain active in optimized builds. They exercise empty/maximum buffers, independent copies, both access overloads, copy/move self-assignment, injected allocation failures, unwinding, defaults, slicing, virtual deletion and checked casts. Sanitizers cover only the executed paths; no actual exhaustion, debugger session, termination path or deliberately undefined runtime is claimed.

Sixteen separate strict compile probes, eight on each compiler, reject return-type-only overloading, ambiguous conversions, implicit use of an explicit constructor, a const-mismatched override, private access, abstract instantiation, a loosened noexcept override, and assignment to the mixed-type conditional result. These diagnostic sources are in the operation evidence; they are not linked into the working programs.

### buffer.hpp

```cpp
#ifndef CPA_BUFFER_HPP
#define CPA_BUFFER_HPP
#include <cstddef>
namespace practice {
class Buffer {
    std::size_t size_ = 0;
    int* data_ = nullptr;
    static int blocks_;
    static bool fail_next_;
    static int* allocate(std::size_t n);
public:
    explicit Buffer(std::size_t n = 0);
    ~Buffer() noexcept;
    Buffer(const Buffer& other);
    Buffer& operator=(const Buffer& other);
    Buffer(Buffer&& other) noexcept;
    Buffer& operator=(Buffer&& other) noexcept;
    void swap(Buffer& other) noexcept;
    std::size_t size() const noexcept { return size_; }
    int& at(std::size_t i);
    const int& at(std::size_t i) const;
    friend bool operator==(const Buffer& a, const Buffer& b) noexcept;
    static int live_blocks() noexcept { return blocks_; }
    // Single-threaded test seam: fail the next nonempty allocation attempt.
    static void fail_next_allocation() noexcept { fail_next_ = true; }
};
}
#endif
```

### buffer.cpp

```cpp
#include "buffer.hpp"
#include <new>
#include <stdexcept>
#include <utility>
namespace practice {
int Buffer::blocks_ = 0;
bool Buffer::fail_next_ = false;
int* Buffer::allocate(std::size_t n) {
    if (n > 32) throw std::length_error("buffer capacity");
    if (n == 0) return nullptr;
    if (fail_next_) {
        fail_next_ = false;
        throw std::bad_alloc();
    }
    int* p = new int[n]{};
    ++blocks_;
    return p;
}
Buffer::Buffer(std::size_t n) : size_(n), data_(allocate(n)) {}
Buffer::~Buffer() noexcept {
    if (data_) --blocks_;
    delete[] data_;
}
Buffer::Buffer(const Buffer& other) : Buffer(other.size_) {
    for (std::size_t i = 0; i < size_; ++i) data_[i] = other.data_[i];
}
Buffer& Buffer::operator=(const Buffer& other) {
    if (this != &other) {
        Buffer temporary(other); // failure leaves *this unchanged
        swap(temporary);         // temporary now owns the old allocation
    }
    return *this;
}
Buffer::Buffer(Buffer&& other) noexcept { swap(other); }
Buffer& Buffer::operator=(Buffer&& other) noexcept {
    if (this != &other) {
        Buffer temporary(std::move(other));
        swap(temporary);
    }
    return *this;
}
void Buffer::swap(Buffer& other) noexcept {
    std::swap(size_, other.size_);
    std::swap(data_, other.data_);
}
int& Buffer::at(std::size_t i) {
    if (i >= size_) throw std::out_of_range("buffer index");
    return data_[i];
}
const int& Buffer::at(std::size_t i) const {
    if (i >= size_) throw std::out_of_range("buffer index");
    return data_[i];
}
bool operator==(const Buffer& a, const Buffer& b) noexcept {
    if (a.size_ != b.size_) return false;
    for (std::size_t i = 0; i < a.size_; ++i)
        if (a.data_[i] != b.data_[i]) return false;
    return true;
}
}
```

### checks.cpp

```cpp
#include "buffer.hpp"
#include "buffer.hpp" // include guard is deliberately exercised
#include <iostream>
#include <new>
#include <stdexcept>
#include <utility>
#include <vector>
namespace pb = practice;
namespace {
int checks = 0;
void check(bool value) {
    ++checks;
    if (!value) throw std::runtime_error("buffer check failed");
}
template<class E, class F> void rejects(F operation) {
    bool caught = false;
    try { operation(); } catch (const E&) { caught = true; }
    check(caught);
}
struct ContainerBuffer { std::vector<int> values; }; // rule of zero
}
int main() {
    try {
        check(pb::Buffer::live_blocks() == 0);
        {
            pb::Buffer empty;
            check(empty.size() == 0);
            rejects<std::out_of_range>([&] { empty.at(0); });
            rejects<std::length_error>([] { pb::Buffer excessive(33); });
            for (std::size_t n : {std::size_t{1}, std::size_t{32}}) {
                pb::Buffer a(n);
                check(a.at(n - 1) == 0);
                a.at(0) = 7;
                pb::Buffer b(a);
                check(a == b);
                check(&a.at(0) != &b.at(0));
                b.at(0) = 9;
                check(a.at(0) == 7);
                check(!(a == b));
                b = a;
                check(a == b);
                pb::Buffer* alias = &b;
                b = *alias;
                check(b.at(0) == 7);
                const pb::Buffer& view = b;
                check(view.at(0) == 7);
                rejects<std::out_of_range>([&] { view.at(n); });
                rejects<std::out_of_range>([&] { b.at(n); });
                b.at(0) = 11;
                const int before = pb::Buffer::live_blocks();
                pb::Buffer::fail_next_allocation();
                rejects<std::bad_alloc>([&] { b = a; });
                check(b.size() == n && b.at(0) == 11);
                check(pb::Buffer::live_blocks() == before);
                pb::Buffer::fail_next_allocation();
                rejects<std::bad_alloc>([&] { pb::Buffer failed(a); });
                check(pb::Buffer::live_blocks() == before);
                pb::Buffer moved(std::move(b));
                check(b.size() == 0 && moved.at(0) == 11);
                rejects<std::out_of_range>([&] { b.at(0); });
                b = std::move(moved);
                check(moved.size() == 0 && b.at(0) == 11);
                b = std::move(*alias);
                check(b.at(0) == 11);
                b = empty;
                check(b.size() == 0);
                check(!(a == b));
            }
            pb::Buffer copy(empty);
            check(copy == empty);
            check(pb::Buffer::live_blocks() == 0);
            ContainerBuffer a{{1, 2}}, b = a;
            b.values[0] = 8;
            check(a.values[0] == 1 && b.values[0] == 8);
        }
        check(pb::Buffer::live_blocks() == 0);
        std::cout << "buffer: " << checks << " checks; live blocks=0\n";
    } catch (const std::exception& e) {
        std::cerr << e.what() << '\n';
        return 1;
    }
}
```

### language.cpp

```cpp
#include <cstddef>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <type_traits>
#include <vector>
#ifndef PRACTICE_LEVEL
#define PRACTICE_LEVEL 1
#endif
#define CPA_TWICE(x) ((x) + (x))
namespace {
int checks = 0;
void check(bool value) {
    ++checks;
    if (!value) throw std::runtime_error("language check failed");
}
template<class E, class F> void rejects(F operation) {
    bool caught = false;
    try { operation(); } catch (const E&) { caught = true; }
    check(caught);
}
int choose(int) { return 1; }
int choose(double) { return 2; }
int by_value(int n) { return ++n; }
void by_reference(int& n) { ++n; }
void reseat(int* p, int* other) { p = other; check(*p == 8); }
int square(int n) { return n * n; } // workbook callers use only small n
int defaulted(int n = 3) { return n; }
unsigned long long factorial(unsigned n) {
    if (n > 12) throw std::out_of_range("factorial domain");
    return n < 2 ? 1 : n * factorial(n - 1);
}
int calls = 0;
int seven() { ++calls; return 7; }
inline int twice(int x) { return x + x; }
int visits() { static int n = 0; return ++n; }
struct Record { int value; };
enum OldColor { red = 1, blue = 2 };
enum class Color : unsigned { red = 1, blue = 2 };
union Number { int i; double d; };
}
int main() {
    try {
        static_assert(std::is_same<decltype(1.0f), float>::value, "float suffix");
        static_assert(std::is_same<decltype(sizeof(int)), std::size_t>::value, "sizeof type");
        check(010 == 8 && 0x10 == 16 && 0b10 == 2);
        check(sizeof(char) == 1);
        check(std::numeric_limits<unsigned>::max() >= 65535u);
        unsigned u = std::numeric_limits<unsigned>::max();
        check(u + 1u == 0);
        check(static_cast<unsigned>(-1) == u);
        check(static_cast<int>(3.75) == 3);
        short small = 4;
        check(choose(small) == 1 && choose(2.5) == 2);
        int n = 1;
        check(sizeof(seven()) == sizeof(int));
        check(calls == 0 && n == 1);
        bool left = false;
        check(!(left && ++n > 0));
        check(n == 1);
        left = true;
        check(left || ++n > 0);
        check(n == 1);
        check((0xau & 0xcu) == 8u && (0xau ^ 0xcu) == 6u);
        check(2 + 3 * 4 == 14);
        int alternate = 4;
        (left ? alternate : n) = 5; // two int lvalues preserve an assignable result
        check(alternate == 5 && n == 1);
        std::string s = "cat";
        check(s.size() == 3 && s.compare("cat") == 0);
        check(s.compare("car") > 0);
        check(s.substr(1, 99) == "at");
        check(s.substr(s.size()).empty());
        rejects<std::out_of_range>([&] { (void)s.substr(4); });
        check(s[s.size()] == '\0');
        rejects<std::out_of_range>([&] { (void)s.at(s.size()); });
        s.insert(0, "s");
        check(s == "scat");
        s.insert(s.size(), "!");
        check(s == "scat!");
        std::vector<int> v{2, 4};
        const auto size = v.size();
        const auto capacity = v.capacity();
        v.reserve(capacity + 1); // reacquire every observer after reallocation
        check(v.size() == size && v.capacity() > capacity && v[1] == 4);
        Number number{};
        number.i = 9; check(number.i == 9);
        number.d = 2.5; check(number.d == 2.5); // no inactive-member read
        check(blue == 2 && static_cast<unsigned>(Color::red) == 1u);
        int array[]{3, 5, 7};
        int* end = array + 3;
        check(end - array == 3 && array + 1 < end);
        check(*(end - 1) == 7);
        int (*callback)(int) = square;
        check(callback(4) == 16);
        Record item{6}; Record* object = &item;
        int Record::* member = &Record::value;
        check(object->value == 6 && item.*member == 6);
        int other = 8;
        int* pointer = &n;
        reseat(pointer, &other);
        check(pointer == &n);
        check(by_value(n) == 2 && n == 1);
        by_reference(n); check(n == 2);
        check(defaulted() == 3 && defaulted(9) == 9);
        check(factorial(0) == 1 && factorial(12) == 479001600ULL);
        rejects<std::out_of_range>([] { factorial(13); });
        check(CPA_TWICE(seven()) == 14 && calls == 2);
        calls = 0;
        check(twice(seven()) == 14 && calls == 1);
        check(visits() == 1); check(visits() == 2);
        int total = 0;
        for (int i = 0; i < 6; ++i) {
            if (i == 1) continue;
            if (i == 5) break;
            total += i;
        }
        check(total == 9);
        int count = 0;
        while (count < 2) ++count;
        do { ++count; } while (count < 2);
        check(count == 3);
        switch (count) {
        case 3: ++count; [[fallthrough]];
        case 4: ++count; break;
        default: count = -1;
        }
        check(count == 5);
        goto finished;
        count = -1;
finished:
        check(count == 5);
#if PRACTICE_LEVEL == 2
        check(factorial(5) == 120);
#else
        check(factorial(1) == 1);
#endif
        std::cout << "language: " << checks << " checks; level=" << PRACTICE_LEVEL << '\n';
    } catch (const std::exception& e) {
        std::cerr << e.what() << '\n';
        return 1;
    }
}
```

### hierarchy.cpp

```cpp
#include <array>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string_view>
#include <typeinfo>
#include <vector>
namespace {
int checks = 0;
void check(bool value) {
    ++checks;
    if (!value) throw std::runtime_error("hierarchy check failed");
}
struct Trace {
    std::array<char, 64> data{};
    std::size_t used = 0;
    bool overflow = false;
    void add(char c) noexcept {
        if (used < data.size()) data[used++] = c;
        else overflow = true;
    }
    std::string_view view() const noexcept { return {data.data(), used}; }
} trace;
struct Part {
    char closing;
    Part(char opening, char end) : closing(end) { trace.add(opening); }
    ~Part() noexcept { trace.add(closing); }
};
struct Root {
    Part base{'B', 'b'};
    int observed_in_base = kind();
    virtual int kind() const noexcept { return 1; }
    virtual ~Root() = default;
};
struct Derived final : Root {
    Part first{'X', 'x'};
    Part second{'Y', 'y'};
    explicit Derived(bool fail = false) {
        trace.add('D');
        if (fail) throw std::domain_error("construction seam");
    }
    int kind() const noexcept override { return 2; }
    ~Derived() override { trace.add('d'); }
};
struct CallBase {
    virtual int call(int n = 1) const { return 10 + n; }
    virtual ~CallBase() = default;
};
struct CallDerived : CallBase {
    int call(int n = 2) const override { return 20 + n; }
};
struct Shape {
    virtual double area() const = 0;
    virtual ~Shape() = default;
};
struct Tagged {
    virtual int tag() const = 0;
    virtual ~Tagged() = default;
};
struct Rectangle final : Shape, Tagged {
    double area() const override { return 6.0; }
    int tag() const override { return 7; }
};
struct Circle final : Shape {
    double area() const override { return 3.141592653589793 * 2.0 * 2.0; }
};
struct InputError : std::runtime_error {
    InputError() : std::runtime_error("input seam") {}
};
void inner() { Part b('B', 'b'); throw InputError(); }
void outer() { Part a('A', 'a'); inner(); }
}
int main() {
    try {
        {
            auto object = std::make_unique<Derived>();
            check(object->observed_in_base == 1);
            check(object->kind() == 2);
            check(trace.view() == "BXYD");
            std::unique_ptr<Root> owner = std::move(object);
            check(owner->kind() == 2);
        }
        check(trace.view() == "BXYDdyxb" && !trace.overflow);
        trace = {};
        bool construction_failed = false;
        try { Derived incomplete(true); }
        catch (const std::domain_error&) { construction_failed = true; }
        check(construction_failed);
        check(trace.view() == "BXYDyxb" && !trace.overflow);
        trace = {};
        bool preserved_type = false;
        try {
            try { outer(); }
            catch (const InputError&) {
                check(trace.view() == "ABba");
                throw;
            }
        } catch (const std::exception& e) {
            preserved_type = dynamic_cast<const InputError*>(&e) != nullptr;
        }
        check(preserved_type && !trace.overflow);
        CallDerived derived;
        const CallBase& base = derived;
        check(derived.call() == 22);
        check(base.call() == 21); // base default, derived implementation
        check(derived.CallBase::call() == 11); // qualified call suppresses dispatch
        CallBase sliced = derived;
        check(sliced.call() == 11);
        std::vector<std::unique_ptr<Shape>> shapes;
        shapes.push_back(std::make_unique<Rectangle>());
        shapes.push_back(std::make_unique<Circle>());
        const double total_area = shapes[0]->area() + shapes[1]->area();
        check(total_area > 18.56 && total_area < 18.57);
        Shape* shape = shapes[0].get();
        check(dynamic_cast<Rectangle*>(shape) != nullptr);
        check(dynamic_cast<Circle*>(shape) == nullptr);
        Tagged* tag = dynamic_cast<Tagged*>(shape); // public sibling cross-cast
        check(tag && tag->tag() == 7);
        bool bad_cast = false;
        try { (void)dynamic_cast<Circle&>(*shape); }
        catch (const std::bad_cast&) { bad_cast = true; }
        check(bad_cast);
        auto* rectangle = static_cast<Rectangle*>(shape); // established actual type
        check(rectangle->tag() == 7);
        bool catch_all = false;
        try { throw 7; } catch (const std::exception&) { check(false); }
        catch (...) { catch_all = true; }
        check(catch_all);
        std::cout << "hierarchy: " << checks << " checks; lifetime and dispatch passed\n";
    } catch (const std::exception& e) {
        std::cerr << e.what() << '\n';
        return 1;
    }
}
```

### CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.16)
project(cpa_workbook LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
add_executable(checks checks.cpp buffer.cpp)
add_executable(language language.cpp)
add_executable(hierarchy hierarchy.cpp)
foreach(target checks language hierarchy)
  target_compile_options(${target} PRIVATE -Wall -Wextra -Wpedantic -Werror)
endforeach()
```

## Integrated scenarios

### Shape hierarchy

Implement an abstract `Shape`, two derived types, virtual area/output, checked `dynamic_cast` for one type-specific operation, and a collection of owning pointers. Trace construction/destruction, slicing, access, failed casts, copy restrictions, and virtual deletion.

### Resource-owning buffer

First implement a small manual buffer with destructor, copy constructor, and copy assignment, including self-assignment and allocation failure reasoning. Then replace ownership with a standard container and explain which special members become unnecessary.

### Namespaced command processor

Use overloaded functions, defaults, an enum, a class operator, exception types, and conditional compilation in a guarded multi-file program. Test ambiguous overload candidates, macro double evaluation, handler ordering, and all cleanup paths.

## Hands-on labs

These eight broader learner labs remain proposed. The bounded workbook above exercises selected mechanics; it is not completion of every scenario, debugger investigation or integrated application.

1. **Type/expression workbook:** predict 30 cases covering literals, promotions, signed/unsigned, casts, `sizeof`, short-circuiting, strings, enums, unions, and vectors.
2. **Control/exception tracer:** run every branch/loop transfer and throw through multiple stack frames; record destructor order and handler selection.
3. **Overload laboratory:** create overload sets with exact matches, promotions, conversions, defaults, references, and one deliberate ambiguity; explain candidate ranking.
4. **Macro-to-function refactor:** inspect conditional expansion and repeated evaluation, then replace unsafe macros with inline/template functions.
5. **Pointer ownership audit:** diagram array/function/object pointers and raw allocation paths; classify leak/mismatch/use-after-free defects on paper and use sanitizers on the valid repaired owner; never rely on a particular output from undefined behavior.
6. **Special-member lab:** implement and test construction, destruction, copy construction, copy assignment, self-assignment, and exceptions for a manual resource owner.
7. **Inheritance matrix:** vary member/inheritance access, overrides, virtual/nonvirtual calls, base deletion, slicing, multiple inheritance, and checked casts.
8. **Integrated application:** finish the namespaced processor with multiple files, exceptions, RAII, tests, warnings, and no owning raw pointer in the final version.

## Original readiness checks

1. Why must exact type ranges be verified rather than guessed?
2. What problem can mixed signed/unsigned comparison cause?
3. How do `static_cast` and `dynamic_cast` differ for hierarchy conversion?
4. Does `sizeof(expression)` normally evaluate the expression?
5. Why is precedence not execution order?
6. How do arrays and vectors differ in ownership/resizing?
7. What does a union's active member represent?
8. What happens during stack unwinding?
9. Why catch exceptions by reference?
10. In what order should derived/base exception handlers appear?
11. Why is `throw()` legacy study material?
12. What is RAII?
13. Why can return type not distinguish overloads?
14. Where are default arguments supplied?
15. How do value, reference, and pointer parameters differ?
16. Why is `void main` not the portable choice?
17. Why can function-like macros evaluate an argument twice?
18. What is a one-past pointer allowed to do?
19. Which deletion matches `new T[n]`?
20. What is the related modern owner for a single allocation?
21. In what order are members initialized?
22. What does `explicit` prevent?
23. How do copy construction and copy assignment differ?
24. Why does a raw owning pointer make generated copying dangerous?
25. Can operator overloading change precedence?
26. What enables virtual dispatch?
27. What is slicing?
28. When does a base class need a virtual destructor?
29. Why avoid `using namespace` in headers?
30. What must you recheck before scheduling?

## Answer key

1. The standard constrains type ranges and representations but leaves implementation choices. Use `<limits>` and the declared implementation rather than assuming every `int` is 32 bits; `sizeof(char)` is one byte, whose bit width is a separate question.

2. Usual arithmetic conversions can turn a negative signed operand into a large unsigned value. Establish the actual operand types and range before choosing a comparison or cast; a cast does not itself validate input.

3. `static_cast` permits specified conversions but does not check an actual derived object before a downcast. Runtime `dynamic_cast` down/cross-casts check a polymorphic hierarchy and fail with null for pointers or `bad_cast` for references; permitted upcasts are simpler.

4. No: the expression operand is unevaluated in ISO C++. `sizeof(seven())` does not call the function, although the expression must meet applicable type/access rules. Compiler VLA extensions are not an ISO C++ exception.

5. Precedence and associativity determine grouping. Sequencing is a separate set of rules: short-circuit operators sequence selected evaluations, whereas parentheses alone do not fix an unsequenced modification/read.

6. A built-in array has a fixed extent and owns its elements as part of its containing storage. A vector owns a dynamic sequence; size and capacity differ, and reallocation invalidates observers. Neither permits out-of-bounds access.

7. It identifies the member whose lifetime is active in the overlapping storage. The workbook writes and reads one trivial member at a time; it does not use an inactive read as a portable numeric conversion.

8. Fully constructed automatic objects and subobjects on the unwound path are destroyed in reverse completion order. A failed ordinary constructor cleans completed bases/members without invoking the incomplete complete-object destructor; unhandled exceptions do not guarantee full unwinding.

9. Catching an exception hierarchy by const reference avoids a by-value base copy and slicing. Use `throw;` to preserve the active exception when rethrowing; `throw e;` creates a new exception from the expression.

10. Place a derived/specific handler before its public base/general handler because handlers are considered in order. Catch-all goes last. Catching an unrelated arithmetic type does not perform a normal numeric conversion.

11. The blueprint names historical specifications. Typed `throw(T)` was removed in C++17, while empty `throw()` survived as a deprecated noexcept alias until removal in C++20. Both tested compilers still accepted the latter in C++20 mode, which does not change the standard.

12. RAII puts resource ownership in an object whose destructor releases it. Normal scope exit and exception unwinding then follow the same ownership contract; a raw observer alone does not establish ownership.

13. For these ordinary function overloads, changing only the return type cannot distinguish declarations. Candidate viability and argument conversions resolve a call; equally good competing conversions can make it ill-formed.

14. Defaults come from declarations visible at the call site, using the static type. A virtual call can then run a derived body with the base default, as the workbook demonstrates with results 21 and 22.

15. Value parameters receive their own object/value, references alias an existing valid object, and pointer parameters receive a pointer value that may be null. Reseating a copied pointer does not reseat the caller's pointer; modifying a valid pointee can affect the caller.

16. Portable hosted main returns int: `int main()` or `int main(int, char**)`. Falling off main returns zero; this exception does not excuse missing returns in ordinary value-returning functions.

17. A macro substitutes its argument tokens at every occurrence. Parenthesizing those occurrences fixes grouping, not repeated evaluation; the workbook observes two calls versus one with the inline function.

18. It may mark the end of a valid same-array range and participate in permitted comparison/subtraction. It must not be dereferenced or incremented beyond that allowed range; unrelated object ordering is a different issue.

19. Use `delete[]` on the correctly owned array allocation. Scalar/array mismatch is undefined behavior, not a reliably catchable exception. Deleting a null pointer is allowed.

20. `std::unique_ptr<T>` commonly owns one object; `std::unique_ptr<T[]>` can own an array, while a standard container often gives a more useful array interface. Raw pointers can remain non-owning observers with a proven lifetime.

21. For a nondelegating constructor: relevant virtual bases, direct bases, members in declaration order, then the body. Initializer-list spelling does not reorder members; destruction reverses completed construction.

22. An explicit constructor is excluded from the relevant implicit conversions/copy-initialization. Direct initialization can still use it; the Buffer size constructor is explicit to prevent an integer silently becoming an owner.

23. Copy construction establishes a new object; copy assignment updates one that already owns state. Buffer assignment creates a temporary first, swaps only after success, and safely handles self-assignment.

24. Memberwise pointer copying duplicates an address, not the resource. Two unique owners would then release the same allocation. Define correct copying/moving or use members such as vector that already implement ownership.

25. No: operator overloads keep the language's precedence, associativity and operand count. The friend equality operator compares buffer contents while respecting access and constness.

26. A virtual call selects the final overrider for the relevant dynamic object, subject to construction/destruction rules. Explicit qualification suppresses dispatch; defaults are still chosen statically.

27. Initializing a base object from a derived object copies the base subobject and omits derived state. The resulting independent base object dispatches as a base; use references/pointers where polymorphic identity must be retained.

28. In this C++17 baseline, deleting a derived object through a base pointer requires the appropriate virtual destructor. Alternatively, a protected nonvirtual destructor can prevent public base deletion; do not promise a fixed output for an invalid deletion.

29. A header-level broad using-directive changes lookup for every includer and can introduce ambiguity. Prefer qualified names or narrow declarations; an unnamed namespace is appropriate for translation-unit-local helpers.

30. Recheck active code, syllabus, language, delivery, format, normalized score, price, prerequisites and actual booking/retake terms. Resolve the public rescheduling conflict with the provider before purchase; course marketing fields do not override the canonical blueprint.

## Final readiness checklist

- [ ] I trace literal types, promotions, conversions, casts, operators, strings, and aggregates.
- [ ] I can predict branch/loop transfers and exception matching/unwinding/destruction.
- [ ] I resolve overloads/defaults and explain value/reference/pointer parameters.
- [ ] I identify unsafe macro expansion and use conditional compilation deliberately.
- [ ] I prove pointer ranges, allocation/deallocation pairing, and raw ownership paths.
- [ ] I establish class invariants and distinguish every constructor, destructor, and copy operation.
- [ ] I reason about access, inheritance, slicing, virtual dispatch, casting, and base destruction.
- [ ] I use namespaces and friends without bypassing design boundaries casually.
- [ ] I recognize legacy `throw()` while using current RAII/`noexcept` context appropriately.
- [ ] I rechecked the live official page immediately before purchase.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick one aligned primary path, then use current references for difficult language rules and write substantial class/exception projects. Reconcile third-party examples with the active CPA-21-02 outline and their declared C++ version.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official CPA page and syllabus](https://cppinstitute.org/cpa) | Free canonical blueprint | 2–3 hours to map and recheck |
| [C++ Institute exam policies](https://cppinstitute.org/exam-policies) | Free official policy | 20–40 minutes before scheduling |
| [OpenEDG C++ Essentials Part 1](https://edube.org/study/cppe1) | Free account; prerequisite coverage; associated CLE/CLE-20-01 field conflicts with C++ course context | 42 hours listed; landing only |
| [OpenEDG C++ Essentials Part 2](https://edube.org/study/cppe2) | Free account; officially aligned; its associated-certification field says `CLA-21-02`, an apparent typo, while the course text and canonical exam page say CPA-21-02 | 42 hours listed |
| [Cisco Networking Academy C++ Essentials 2](https://www.netacad.com/courses/c-plus-plus-essentials-2) | Free account; official partner delivery | Duration unverified; application shell only |
| [Microsoft C++ language reference](https://learn.microsoft.com/en-us/cpp/cpp/cpp-language-reference?view=msvc-170) | Free official implementation documentation | 8–15 hours targeted reading |
| [cppreference C++ language](https://en.cppreference.com/w/cpp/language.html) | Free community reference | Ongoing; 8–15 hours targeted lookup |
| [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) | Free community/ISO C++ project guidance; modern context | 8–15 hours selected sections |
| [Pluralsight C++ path](https://www.pluralsight.com/paths/c-plus-plus) | Subscription; broader than CPA; public path lists 13 courses and a 44-hour banner | 15–25 hours suggested selection; paid videos not read |
| [O'Reilly C++ Crash Course, 2nd Edition](https://www.oreilly.com/library/view/c-crash-course/9781098136217/) | Subscription; modern and broader | 15–25 hours selected chapters/labs |
| [Udemy Beginning C++ Programming — From Beginner to Beyond](https://www.udemy.com/course/beginning-c-plus-plus-programming/) | Paid marketplace course; broad | Select OOP, inheritance, exceptions, 15–25 hours |

No exact current MeasureUp or Whizlabs CPA-21-02 practice product was verified. Prefer official aligned assessments plus original compile-and-trace labs; reject practice material that does not identify the active exam version.

Primary technical reading for this review uses selected publicly rendered WG21 draft sections, not a complete standard audit. Microsoft implementation documentation may include extensions and legacy examples: its allocation page contains examples and generalizations that should not be copied as portable ownership contracts. The original workbook follows the explicit C++17 draft rules above. The [research report](../docs/research/2026-09-29-cpa-21-02-deep-review.md) records source-reading, execution and remaining human-review boundaries.
