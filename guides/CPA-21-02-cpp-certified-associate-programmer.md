---
exam_code: CPA-21-02
vendor_id: cpp-institute
official_blueprint: https://cppinstitute.org/cpa
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# CPA-21-02 C++ Certified Associate Programmer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, links, lifecycle, and exam-integrity compliance were checked September 2, 2026. This does not guarantee that every explanation is error-free or remains current. The [official CPA page and syllabus](https://cppinstitute.org/cpa) are authoritative.

**Current baseline:** CPA-21-02, active; CPA-21-01 retired; five-block syllabus last updated July 22, 2025<br>
**Upcoming blueprint change:** none announced on the official exam or certification-catalog pages when checked<br>
**Official delivery snapshot:** 40 single- and multiple-choice questions; 65-minute exam plus approximately 10 minutes for the NDA/tutorial; 70% cumulative passing score; Pearson VUE/OnVUE; English<br>
**Purchase snapshot:** no formal prerequisite; from USD 325 exam or USD 375 exam-plus-retake when checked<br>

## How to use this guide

CPA is the bridge from procedural C++ to object-oriented design. You need to trace expressions and memory, but almost one-third of the published weighting is classes and namespaces. For every class exercise, draw object lifetime, base/derived subobjects, access, virtual dispatch, ownership, copy behavior, and exception paths.

Use this loop:

1. map the problem to the five official blocks;
2. predict compilation, overload choice, lifetime, dispatch, state, output, or exception;
3. compile in a declared standard mode with strong warnings;
4. use debugger and address/undefined-behavior diagnostics where available;
5. test construction, copying, inheritance, error, and cleanup paths.

The outline names legacy dynamic exception specifications such as `throw()`. They remain exam-recognition material, but current standard C++ uses `noexcept`; dynamic exception specifications were deprecated and later removed. Answer according to the code's declared language version and do not introduce `throw()` into new production code.

> **About related items:** A `Related item:` callout supplies adjacent, prerequisite, operational, or modern-practice context. It helps you understand an objective; it does not claim that the extra item appears verbatim in the exam blueprint.

## Weighted objective map

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| 1. Types and Operators | 9 | 24.5% | Trace types, conversions, strings, aggregates, literals, and expressions |
| 2. Control and Exceptions | 8 | 18% | Trace all paths and explain exception matching/unwinding |
| 3. Functions and Preprocessor | 9 | 17.5% | Resolve overloads/defaults, pass correctly, recurse, and expand macros |
| 4. Pointers | 4 | 11% | Prove pointer targets/ranges and manual allocation cleanup |
| 5. Classes and Namespaces | 10 | 29% | Design, construct, copy, inherit, dispatch, cast, overload, and organize types |

The provider weights individual questions and normalizes the total. The published block percentages are study-allocation guidance, not permission to skip a smaller block.

## 1. Types and operators — 24.5%

### Types, literals, and conversions

Know integral, character, Boolean, and floating families; exact-width/range assumptions must be verified rather than guessed. Literal spelling determines candidate type: decimal, octal, hexadecimal, binary where supported by the baseline, floating suffixes, character/string literals, and `true`/`false`.

Integral promotions and usual arithmetic conversions affect mixed expressions. Signed/unsigned comparison can transform a negative value unexpectedly. `static_cast` expresses supported conversions; `dynamic_cast` checks polymorphic hierarchy conversions at runtime; `const_cast` changes cv qualification; `reinterpret_cast` expresses low-level reinterpretation with strict safety limits. A cast does not repair lifetime or ownership.

`sizeof` yields the size of a type/object representation in bytes of `char`; it does not generally evaluate its operand expression. Padding and alignment mean class/struct size is not just the arithmetic sum of members.

### Operators and expression tracing

Understand unary, binary, and conditional operators; arithmetic, comparison, logical, bitwise, assignment, increment/decrement, and short-circuit rules. Precedence groups syntax; it is not a universal evaluation-order rule. Parentheses communicate intent. Avoid expressions that modify/read one scalar without defined sequencing.

Logical `&&`/`||` short-circuit and yield `bool`; bitwise operators work on promoted integral representations. The conditional operator selects one of two expressions and has type-combination rules—not merely “compact if.”

### Strings and aggregates

`std::string` owns a sequence and supports `size`, comparison, `substr`, `insert`, and other operations. Check position/count behavior and distinguish character indexing from substring creation. A string literal and `std::string` are different types and lifetimes.

Arrays own fixed sequences; vectors own resizable sequences. Structures/classes group members. A union's members share storage and active-member rules matter. Scoped and unscoped enumerations differ in qualification/conversion behavior. `const` restricts modification through a particular object/access path; `static` meaning depends on context.

> **Related item:** Prefer enum classes, containers, and explicit conversions in new code. You still need to recognize older idioms because the blueprint spans core and legacy constructs.

## 2. Control and exceptions — 18%

Trace `if`, `switch`, `while`, `do`, `for`, `break`, `continue`, `goto`, and `return`. `else` binds to the nearest unmatched `if`; `switch` falls through without a transfer. `continue` in a `for` proceeds to the update. A return ends the current function, triggering destruction of automatic objects whose scopes are exited normally.

`throw expression` creates/initializes an exception object. Stack unwinding destroys fully constructed automatic objects between the throw and matching handler. Handlers are considered in order; catch by reference avoids slicing and copying. `catch (...)` catches otherwise unmatched exceptions but supplies no typed object. A `throw;` inside a handler rethrows the current exception.

```cpp
try {
    process(input);
} catch (const validation_error& ex) {
    std::cerr << ex.what() << '\n';
} catch (const std::exception& ex) {
    std::cerr << "operation failed: " << ex.what() << '\n';
}
```

Place derived handlers before base handlers. Destructors should not let exceptions escape during unwinding. Resource-owning objects provide cleanup through destruction.

The legacy `throw()` specification historically promised no escaping exception in older modes; it is not a modern substitute to memorize without version context. `noexcept` is the current related mechanism and affects termination/optimization and some library choices.

> **Related item:** RAII binds a resource to object lifetime so returns and exceptions use the same cleanup path. It is the central connection between classes, exceptions, and memory safety.

## 3. Functions and preprocessor — 17.5%

### Calls, overloads, defaults, and recursion

A declaration states a function signature; a definition provides the body. Overload resolution forms viable candidates, ranks conversions, and selects a best match or diagnoses ambiguity. Return type alone cannot distinguish overloads. Default arguments are supplied at the call site from visible declarations and should generally be stated once.

Pass by value creates a parameter object, reference parameters alias a caller object, pointer parameters receive an address value and can represent null. Use `const T&` for required non-mutating access to an existing object where copying is undesirable. Understand that reseating a pointer parameter does not reseat the caller's pointer unless another level of indirection/reference is used.

Recursion needs a reachable base case and progress and consumes finite stack resources. `main` has standard forms returning `int`; do not invent `void main` as portable C++.

### Preprocessing

`#include`, `#define`, `#if`, `#ifdef`, `#else`, and `#endif` act before C++ parsing. Function-like macros perform token substitution without types or single-evaluation guarantees. Parenthesize parameters and replacement expressions, but prefer functions/templates when evaluation and types matter.

Use conditional compilation for true build/platform variation, not ordinary runtime business logic. Inspect preprocessed output to understand expansion and guard against duplicate definitions through include guards or equivalent facilities.

## 4. Pointers — 11%

A pointer object stores an address/null and has its own lifetime. `&object` obtains an address; `*pointer` designates a valid target. `nullptr` is the null-pointer literal. Pointers can target objects, array elements, functions, or aggregate members with compatible types.

Pointer arithmetic and ordering are meaningful only within an array relationship. A one-past pointer may be formed/compared but not dereferenced. Function pointers enable callbacks; their declaration and invocation types must match.

`new T(...)` creates an object and `delete` destroys/releases it. `new T[n]` pairs with `delete[]`. Leaks, use-after-free, double deletion, mismatch, and exception paths make raw ownership fragile.

```cpp
Widget* widget = new Widget(args);
try {
    use(*widget);
} catch (...) {
    delete widget;
    throw;
}
delete widget;
```

This illustrates why direct ownership should normally be replaced by an automatic object or smart owner; CPA still requires understanding the raw operations.

> **Related item:** `std::unique_ptr` represents single ownership and is the default related replacement for a raw owning pointer. Raw pointers remain useful non-owning observers when lifetime is guaranteed elsewhere.

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

```cpp
class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
};
```

Friend functions/classes receive access but are not members and can weaken encapsulation if overused. Use them when an operation genuinely needs symmetric/non-member access, not as a default escape hatch.

### Namespaces

Named namespaces organize declarations and avoid collisions. `namespace alias = long_name;` shortens qualification. An unnamed namespace gives internal linkage to eligible names in that translation unit. A broad `using namespace` directive in a header pollutes every includer; prefer qualification or narrow using-declarations.

> **Related item:** Abstract interfaces and composition often reduce coupling compared with deep inheritance. The exam requires inheritance mechanics; design still asks whether inheritance is the right relationship.

## Integrated scenarios

### Shape hierarchy

Implement an abstract `Shape`, two derived types, virtual area/output, checked `dynamic_cast` for one type-specific operation, and a collection of owning pointers. Trace construction/destruction, slicing, access, failed casts, copy restrictions, and virtual deletion.

### Resource-owning buffer

First implement a small manual buffer with destructor, copy constructor, and copy assignment, including self-assignment and allocation failure reasoning. Then replace ownership with a standard container and explain which special members become unnecessary.

### Namespaced command processor

Use overloaded functions, defaults, an enum, a class operator, exception types, and conditional compilation in a guarded multi-file program. Test ambiguous overload candidates, macro double evaluation, handler ordering, and all cleanup paths.

## Hands-on labs

1. **Type/expression workbook:** predict 30 cases covering literals, promotions, signed/unsigned, casts, `sizeof`, short-circuiting, strings, enums, unions, and vectors.
2. **Control/exception tracer:** run every branch/loop transfer and throw through multiple stack frames; record destructor order and handler selection.
3. **Overload laboratory:** create overload sets with exact matches, promotions, conversions, defaults, references, and one deliberate ambiguity; explain candidate ranking.
4. **Macro-to-function refactor:** inspect conditional expansion and repeated evaluation, then replace unsafe macros with inline/template functions.
5. **Pointer ownership audit:** diagram array/function/object pointers and raw allocation paths; run sanitizers on disposable leak/mismatch/use-after-free defects.
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

1. Their representations are implementation-dependent within language requirements.
2. A negative signed operand can convert to a large unsigned value.
3. The former expresses permitted compile-time conversions; the latter checks polymorphic dynamic type.
4. Usually no, subject to language exceptions/contexts.
5. It groups syntax but does not generally sequence operand evaluation.
6. Fixed array storage versus an owning resizable container.
7. Which overlapping member's lifetime/value is currently established under the rules.
8. Fully constructed automatic objects in exited scopes are destroyed until a matching handler is reached.
9. To avoid copying/slicing and preserve dynamic information.
10. More-derived/specific before base/general.
11. Dynamic exception specifications are obsolete/removed in current modes; the blueprint retains recognition.
12. Binding resource ownership to object lifetime for deterministic cleanup.
13. It is not part of an overload's distinguishing parameter list.
14. At the call site from visible declarations.
15. Parameter copy; required alias; nullable/reseatable address value.
16. The standard hosted forms return `int`.
17. Token substitution can place the argument expression in multiple replacement positions.
18. Participate in valid range traversal/comparison, never dereference.
19. `delete[]`.
20. `std::unique_ptr<T>` (or a container for arrays, depending on design).
21. Declaration order inside the class.
22. Unintended implicit converting construction in the relevant contexts.
23. Creation of a new object versus replacement of an existing object's state.
24. It copies the address, creating ambiguous ownership and double-release risk.
25. No.
26. A virtual function call through an appropriate base reference/pointer to a polymorphic object.
27. Copying a derived object into a base object by value, losing the derived portion.
28. When objects may be destroyed through a base pointer, or as an interface design convention supporting that use.
29. They inject names into every including translation unit and invite collisions/ambiguity.
30. Active version, syllabus, delivery, language, price, format, and policies.

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
| [OpenEDG C++ Essentials Part 1](https://edube.org/study/cppe1) | Free account; provider-aligned prerequisite coverage | 42 hours listed; target gaps |
| [OpenEDG C++ Essentials Part 2](https://edube.org/study/cppe2) | Free account; officially aligned; its associated-certification field says `CLA-21-02`, an apparent typo, while the course text and canonical exam page say CPA-21-02 | 42 hours listed |
| [Cisco Networking Academy C++ Essentials 2](https://www.netacad.com/courses/c-plus-plus-essentials-2) | Free account; official partner delivery | Plan 35–45 hours; verify live listing |
| [Microsoft C++ language reference](https://learn.microsoft.com/en-us/cpp/cpp/cpp-language-reference?view=msvc-170) | Free official implementation documentation | 8–15 hours targeted reading |
| [cppreference C++ language](https://en.cppreference.com/w/cpp/language.html) | Free community reference | Ongoing; 8–15 hours targeted lookup |
| [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) | Free community/ISO C++ project guidance; modern context | 8–15 hours selected sections |
| [Pluralsight C++ path](https://www.pluralsight.com/paths/c-plus-plus) | Subscription; broader than CPA | Select OOP, exceptions, pointers, 15–25 hours |
| [O'Reilly C++ Crash Course, 2nd Edition](https://www.oreilly.com/library/view/c-crash-course/9781098136217/) | Subscription; modern and broader | 15–25 hours selected chapters/labs |
| [Udemy Beginning C++ Programming — From Beginner to Beyond](https://www.udemy.com/course/beginning-c-plus-plus-programming/) | Paid marketplace course; broad | Select OOP, inheritance, exceptions, 15–25 hours |

No exact current MeasureUp or Whizlabs CPA-21-02 practice product was verified. Prefer official aligned assessments plus original compile-and-trace labs; reject practice material that does not identify the active exam version.
