---
exam_code: CPP-22-02
vendor_id: cpp-institute
official_blueprint: https://cppinstitute.org/cpp
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# CPP-22-02 C++ Certified Professional Programmer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, links, lifecycle, and exam-integrity compliance were checked September 29, 2026. This does not guarantee that every explanation is error-free or remains current. The [official CPP page and syllabus](https://cppinstitute.org/cpp) are authoritative.

**Current baseline:** CPP-22-02, active; nine-block syllabus last updated July 22, 2025<br>
**Upcoming blueprint change:** none announced on the official exam or certification-catalog pages when checked<br>
**Official delivery snapshot:** 40 single- and multiple-choice questions, one point each (maximum 40); 65-minute exam plus approximately 10 minutes for the NDA/tutorial; 70% cumulative passing score; Pearson VUE; English<br>
**Purchase snapshot — VERIFY CURRENT:** canonical exam page says CPA recommended; Pearson and issuer-badge wording requires it (unresolved); from USD 325 exam or USD 375 exam-plus-retake when checked<br>

## How to use this guide

CPP is primarily an STL, algorithms, iterators, function-object, stream-formatting, and templates exam. Practice by writing the preconditions and postconditions of every operation before calling it. For algorithms, name the input range, output destination, ordering/predicate, invalidation effects, returned iterator, and complexity-relevant container choice.

Use this loop:

1. choose the container from access, insertion, ordering, uniqueness, and invalidation needs;
2. express work as half-open iterator ranges `[first, last)`;
3. state every sorted-range, output-capacity, and comparator/predicate precondition;
4. predict the returned iterator and logical versus physical container state;
5. compile in an explicit standard mode and test empty, singleton, duplicate, boundary, and invalidation cases.

The blueprint includes `std::ptr_fun`, a legacy adapter deprecated in C++11 and removed in C++17. Recognize it for the published objective, but use lambdas or modern callable adapters in new code. The Edube C++ Advanced landing names CPP-22-01, 42 hours and prior completion of the CPA-level course; the [C++ Institute course landing](https://cppinstitute.org/cpp-advanced) names CPP-22-02, 50 hours and no formal prerequisite. These are unresolved source differences, not verified enrollment requirements. Both public landings describe nine modules; no enrolled lessons or assessments were inspected.

The live page also contains an internal arithmetic inconsistency: it says the exam has 40 questions, while its nine block counts total 32 and its displayed weights total 107%. The table below preserves the provider-published block values so future source checks can detect a correction. Do not treat the percentages as a normalized study plan; cover every listed objective.

> **About related items:** A `Related item:` callout supplies adjacent, prerequisite, operational, or modern-practice context. It helps you understand an objective; it does not claim that the extra item appears verbatim in the exam blueprint.

**Review boundary:** all 34 numbered objectives (6/5/5/4/2/3/2/3/4) and all 30 original answers were reviewed. The automated objective request timed out; the complete canonical public body was manually compared and the snapshot retained. No announced replacement appeared on the inspected exam/catalog material. Human review remains pending.

**Booking boundary — VERIFY CURRENT:** the [Pearson program page](https://www.pearsonvue.com/cppinstitute/) calls CPA a prerequisite, and the [issuer badge criteria](https://www.credly.com/org/openedg/badge/cpp-22-02-cpp-c-certified-professional-programmer) list CPA and CPP passes; the canonical exam page says recommended. [Policy](https://cppinstitute.org/exam-policies) and [scheduling](https://cppinstitute.org/schedule-exam-pvue) wording also differs on anytime-before versus 24-hour appointment changes. The published failed-retake wait is 15 days. Confirm actual eligibility, delivery and appointment terms with the provider before purchase; no account or booking was tested. The [catalog](https://cppinstitute.org/certification-exams) supplies broader version-specific credential context. Do not derive a definitive raw passing-answer count from the displayed percentage without the scoring/rounding rules.

## Weighted objective map

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| 1. Sequence Containers and Adapters | 4 | 13.25% | Select and safely modify vector/deque/list/stack/queue/priority queue |
| 2. Associative Containers | 4 | 13.25% | Model key uniqueness/order and use lookup/update iterators correctly |
| 3. Non-Modifying Algorithms | 4 | 13.25% | Select search/count/compare algorithms and interpret returned iterators |
| 4. Modifying Algorithms | 4 | 13.25% | Prove output capacity and complete remove/unique/reorder idioms |
| 5. Sorting and Binary Search | 5 | 16.5% | Maintain strict weak ordering and sorted-range preconditions |
| 6. Merge, Set, and Min/Max | 5 | 16.5% | Apply two-range operations to consistently sorted ranges |
| 7. Function Objects and Utilities | 2 | 7% | Supply compatible callables and recognize legacy adapters |
| 8. Advanced I/O | 2 | 7% | Control persistent/one-shot stream state and formatting |
| 9. Templates | 2 | 7% | Define, instantiate, specialize, compose, and diagnose templates |

The first six container/algorithm blocks total 86 percentage points as published. Because the complete provider table incorrectly totals 107%, do not infer a reliable share of the scored exam from that figure. Stream, callable, and template blocks remain required and also appear inside container/algorithm code.

## 1. Sequence containers and adapters — 13.25%

### Choosing a sequence

`std::vector` owns contiguous storage, offers constant-time indexed access and efficient insertion/removal at the end, and may reallocate as capacity grows. Reallocation invalidates pointers/references/iterators to elements; other changes have operation-specific invalidation rules.

`std::deque` supports efficient insertion/removal at both ends and indexed access but is not one contiguous array. `std::list` is a doubly linked sequence with bidirectional iterators, no indexed access, and stable element references/iterators except to erased elements under ordinary operations. Its node allocation/cache cost means “middle insertion is constant time” is only useful once the position is already known.

For each container, know construction, `size`/`empty`, element access where supported, `push`/`pop` variants, `insert`, `erase`, and traversal. Distinguish capacity from size in vector; `reserve` changes capacity without adding elements and can invalidate on reallocation, while `resize` changes size and constructs/destroys elements.

### Invalidation is operation-specific

| Operation | Handles you may retain |
|---|---|
| Vector reserve that reallocates | No old element pointer, reference or iterator |
| Vector insertion without reallocation | Handles strictly before the insertion point; not the old end |
| Vector erase | Handles strictly before the erased position; use the returned iterator for continued traversal |
| Deque end insertion | Element references/pointers survive; iterators are invalidated |
| Deque middle insertion | Element references and iterators are invalidated |
| List ordinary insert/erase | Insertion preserves existing handles; erasure invalidates those to erased nodes |
| Ordered associative insert/erase | Insertion preserves existing handles; erasure invalidates those to erased elements |

Deque end erasure has more specific rules: erasing the last element invalidates the past-the-end iterator; erasing the first but not the last invalidates only erased-element handles; middle erasure invalidates all element iterators/references and the end. Do not generalize list stability to every node transfer: `splice`/`merge` have allocator requirements, and transferred iterators refer into the destination. These rules follow selected [C++17 container requirements and member specifications](https://timsong-cpp.github.io/cppwp/n4659/containers).

### Adapters

`std::stack` exposes last-in/first-out operations (`top`, `push`, `pop`). `std::queue` exposes first-in/first-out (`front`, `back`, `push`, `pop`). `std::priority_queue` exposes the highest-priority element under its comparison convention. These are adapters over underlying containers and deliberately do not expose general iteration.

A default integer priority queue exposes the largest value at `top()`. With the workbook's job comparator, higher urgency wins and a smaller ID breaks ties. `queue` needs an underlying sequence with `pop_front`; `priority_queue` needs random-access iterators; `stack` needs back operations. They have no public `begin`/`end`. Objective 1.4's adapter-traversal wording does not create that interface: inspect a copy by repeated guarded access/pop, or choose a directly iterable container.

Calling `front`, `back`, `top`, or `pop` on an empty container/adapter violates its precondition. Check `empty()` first.

> **Related item:** Iterator category constrains algorithms. A list supplies bidirectional—not random-access—iterators, so `std::sort` does not apply; `list::sort` is the container-specific operation.

## 2. Associative containers — 13.25%

`std::set` stores unique keys; `multiset` permits equivalent keys. `map` stores unique key/value pairs; `multimap` permits equivalent keys. These ordered associative containers organize elements according to a comparison and traverse in that order—not insertion order.

Use `find` when you need an iterator, `count` for occurrence count, `lower_bound`/`upper_bound` for an equivalent-key range, `equal_range` for both boundaries, and `erase` with exact awareness of whether an iterator/key/range overload is selected. Test against `end()` before dereference.

Map iterator values are key/value pairs whose key is not modifiable through the iterator, because changing it in place would break ordering. `operator[]` on `map` inserts a default-mapped value when a key is missing; use `find`/`at` when lookup should not mutate.

Key equivalence means neither `comp(a,b)` nor `comp(b,a)` is true; it need not mean `a == b`. A set ordered only by a `group` field can reject a second differently labelled key in the same group. Map keys are const within `pair<const Key, T>`; mapped values remain mutable. Prefer tree-container member bounds when appropriate: generic bounds can need linear iterator steps despite logarithmic comparisons.

Custom comparison must provide a strict weak ordering and remain consistent for stored keys. For a user-defined key, encode the intended fields deliberately and do not let mutable external state change ordering behavior.

> **Related item:** `unordered_*` containers are useful modern alternatives but are outside this published container list. Do not replace ordered-container study with hash-table assumptions.

## 3. Non-modifying sequence algorithms — 13.25%

Algorithms consume iterator ranges, usually `[first, last)`. The chapter label is not a blanket ban on mutation. Serial `for_each` may modify elements through mutable iterators, visits them in order and returns the final function object. Ordinary predicates have a different contract: they must not modify their element arguments. Algorithms may copy callables; recover a serial `for_each` accumulator from its return value or deliberately pass `std::ref`. Do not transfer this model to parallel overloads.

- `for_each` invokes an operation for each element;
- `find`/`find_if` locate a value/predicate match;
- `find_end` finds the last occurrence of a subsequence;
- `find_first_of` finds an element matching any in another range;
- `adjacent_find` locates neighboring matches;
- `search` locates a subsequence and `search_n` repeated matching elements;
- `count`/`count_if` count matches;
- `mismatch` finds first differing paired elements;
- `equal` checks range equivalence under applicable overloads.

Search algorithms generally return the end iterator when no match is found. With an empty needle, `search` returns `first`, but `find_end` returns `last`; zero-count `search_n` returns `first`. `mismatch` returns a pair, including when one explicitly bounded range ends first. These distinctions are exercised in the workbook. Never dereference before checking. Two-range algorithms require a sufficiently long second range under the selected overload/version; pass explicit end bounds where available.

Predicates should not invalidate the range or rely on an unstable order of invocation. If you need transformed output, use `transform`; do not hide mutation in an observational predicate. Selected [C++17 algorithm contracts](https://timsong-cpp.github.io/cppwp/n4659/algorithms) govern the examples; every workbook algorithm call is serial.

## 4. Modifying sequence algorithms — 13.25%

Destination-writing algorithms require enough existing writable elements unless an insertion iterator grows a container. `reserve(n)` alone leaves vector size unchanged: writing to `begin()` of an empty reserved vector is still invalid. Use `resize(n)` or `back_inserter`. For serial `copy`, the destination start must not be inside `[first,last)`; a left shift into earlier existing elements can be valid. For `copy_backward`, the destination end must not be in `(first,last]`; a right shift ending after `last` can be valid. The workbook tests each allowed direction in a five-element array. Do not infer arbitrary overlap permission for `copy_if`, `swap_ranges`, merge or set output. Exact in-place `transform` is allowed, but its operation must respect the range mutation/invalidation restrictions. `fill` assigns a value; `generate` obtains each value from a callable.

`transform` writes transformed results. `swap`, `iter_swap`, and `swap_ranges` exchange objects/ranges under their preconditions. `replace` changes matching elements.

`remove`/`remove_if` do not erase container elements. They move retained elements toward the front and return a new logical end; erase the tail for sequence containers:

Capture the returned logical end and pass `[logical_end, values.end())` to the container's `erase`. The tail remains valid but unspecified; do not assert its values. By contrast, `list::remove` and `list::unique` erase nodes directly. A value argument aliasing an element moved during removal is another trap: keep the removal criterion independent.

Likewise, `unique` coalesces consecutive equivalent elements and returns a logical end; sort first only if the desired rule is “remove all duplicates regardless of original adjacency.” `unique_copy` writes retained values to a destination.

`reverse`, `rotate`, `partition`, and `stable_partition` reorder elements. Partition separates elements by a predicate but does not necessarily sort either group; stable partition preserves relative order within groups. Returned iterators identify meaningful boundaries—capture and use them.

> **Related item:** C++20 ranges and `std::erase_if` can make intent clearer, but the exam names classic STL algorithms. Understand iterator-based mechanics before translating to newer interfaces.

## 5. Sorting and binary search — 16.5%

`sort` requires random-access iterators and does not preserve equivalent-element order. `stable_sort` preserves it. A custom comparator must provide strict weak ordering: irreflexivity, transitivity of the strict relation, and transitivity of equivalence defined by neither element preceding the other. Asymmetry follows and is useful to check. Passing `a < b` on a few pairs is insufficient. Use `left.field < right.field`, not `<=`.

`lower_bound` returns the first position not ordered before a value; `upper_bound` returns the first position ordered after it; `[lower, upper)` is the equivalent range. `binary_search` reports presence, not position. These algorithms require ranges partitioned/sorted consistently with the comparison and searched value.

Do not sort with one criterion and binary-search with an incompatible one. Mutating keys/order-relevant fields behind an ordered range invalidates the precondition even if container iterators remain technically valid.

For `lower_bound`, evaluate `comp(element,key)`; `upper_bound` uses `comp(key,element)`. A range can be partitioned correctly for one key without being globally sorted: `{2,1,3,5,4}` is valid for the workbook's key `3`, but is not a reusable sorted index. The comparator checker rejects non-strict, cyclic and non-transitive-equivalence examples before any algorithm sees them. Its finite sample is diagnostic evidence, not proof over every possible input.

Be precise about heterogeneous comparator overloads: the callable signatures can differ between element-element sorting and element-value bounds.

## 6. Merge, set, and min/max algorithms — 16.5%

`merge` combines two sorted input ranges into a sorted output range; destination capacity and non-overlap requirements apply. `inplace_merge` merges two consecutive sorted subranges `[first, middle)` and `[middle, last)` in the original range.

`includes`, `set_union`, `set_intersection`, `set_difference`, and `set_symmetric_difference` operate on sorted ranges under the same ordering. Despite their names, inputs need not be `set` containers. For one equivalent value occurring `m` times on the left and `n` times on the right, union emits `max(m,n)`, intersection `min(m,n)`, left difference `max(m-n,0)`, and symmetric difference `abs(m-n)`. `includes` also respects multiplicity. Output must be writable and satisfy non-overlap requirements; capture the returned output end instead of reading unused capacity.

`min_element` and `max_element` return iterators, including `last` for an empty range. They compare elements under the supplied/default ordering. Capture the iterator and prove it is dereferenceable before access. `min_element` and `max_element` select the first equivalent extreme. Adjacent `minmax_element` selects the first minimum but the last maximum; the workbook makes that tie difference visible.

The official block title mentions heap, but the listed numbered objectives/keywords on the live page name merge, sorted-set operations, and min/max rather than individual heap algorithms. Prioritize the explicit objectives; treat heap operations as adjacent container/`priority_queue` context unless the provider updates the detailed list.

> **Related item:** Complexity depends on iterator category and algorithm/container choice. Correct output is necessary; professional selection also avoids repeatedly doing linear work where a maintained index/order is appropriate.

## 7. STL function objects and utilities — 7%

A function object is an object callable with `operator()`. Standard objects such as `std::plus<>` and `std::minus<>` can be passed to `transform` and other algorithms. Functions, lambdas, and callable objects must meet the algorithm's expected argument/result contract.

The workbook adds two equal-length integer ranges using `std::plus<>`, then subtracts with `std::minus<>` in place. All arithmetic is bounded. Typed `plus<T>` uses that type, while the `void`/transparent form forwards operands and deduces the expression result; it does not promise overflow protection or universally identical mixed-type behavior. See selected [C++17 arithmetic function objects](https://timsong-cpp.github.io/cppwp/n4659/function.objects).

A binary transform requires enough elements in the second input and output, or a valid insertion iterator for output. A stateful function object can carry configuration, but copies and invocation order must not silently violate expectations.

`std::ptr_fun` wrapped function pointers for older adapter ecosystems. It was deprecated in C++11 and removed in C++17. The [C++14 deprecated wrapper specification](https://timsong-cpp.github.io/cppwp/n4140/depr.function.pointer.adaptors) describes wrapping a unary/binary function pointer, not binding an argument by itself; the [C++17 removal note](https://timsong-cpp.github.io/cppwp/n4659/diff.cpp14.depr) removes this adapter family. Four hosted probes (two compilers, C++14/C++17 modes) still accepted `ptr_fun` with deprecation warnings and printed `6`. That library compatibility observation does not restore a removed standard feature. Use lambdas or other suitable current callables in new work.

## 8. Advanced I/O — 7%

`cin` reads standard input; `cout` writes standard output; `cerr` and `clog` use standard error. Initially `cin` and `cerr` are tied to `cout`, and `cerr` has `unitbuf` set. These are stream configuration facts, not a blanket claim that every output call reaches a device immediately. Selected [C++17 I/O specifications](https://timsong-cpp.github.io/cppwp/n4659/input.output) distinguish formatting, buffering and error state.

Streams carry formatting state. Flags such as base, float, adjustment, show-point, and Boolean text can persist; some manipulators are one-shot. `setw` normally affects the next formatted field, whereas `fixed`, `boolalpha`, precision, and many flags persist until changed.

`setf(flags)` ORs bits, whereas `setf(flags,mask)` replaces the masked field; `unsetf` clears flags. `boolalpha` writes/reads textual Booleans. `fixed` changes floating formatting interpretation; `setprecision` means digits after the decimal in fixed notation but has different meaning under default formatting. `noshowpoint` clears the showpoint flag; it does not override fixed precision, so fixed precision two still prints `2.00`. Setting both fixed and scientific bits selects hexadecimal floating output: use the field mask when switching between them. The [numeric formatting facet](https://timsong-cpp.github.io/cppwp/n4659/facet.num.put.virtuals) explains conversion, locale adjustment, padding and width reset. Check stream state after input/output operations.

Preserve caller stream settings when a reusable formatter should not leak its choices. The workbook guard saves/restores flags, precision, fill and pending width during normal return and exception unwinding. It deliberately does not copy locale, callbacks, exception masks, ties, buffers or error state; `copyfmt` has broader effects and is not a casual destructor replacement. Classic locale is selected by the test caller for deterministic strings.

Stream `bool` means no failbit/badbit, not no eofbit. Successfully extracting the last integer can set eofbit alone; a later extraction fails. Recovery requires both clearing state and consuming/replacing the offending input. Output failure sets badbit and may throw under the exception mask. The workbook uses an explicitly refusing stream buffer; this is not a real disk/device failure test.

> **Related item:** Formatting is presentation, not numerical accuracy. Displaying two decimal digits does not make a binary floating calculation exact or implement monetary rounding policy.

## 9. Templates — 7%

Function and class templates define families parameterized by types or values. Instantiation substitutes arguments and checks the resulting use. Template definitions generally must be visible where implicitly instantiated, which is why they commonly live in headers.

In the workbook, `clamp_low(2, 2.5)` cannot deduce one `T`, while `clamp_low<double>(2, 2.5)` allows conversions after explicit selection. `Box<T>` has a nested class template, a member template and a per-specialization non-template friend output operator. A function full specialization and a class full specialization are defined before use; an ordinary overload is not the same mechanism.

Template argument deduction does not perform every conversion ordinary overload resolution might. Constraints are often implicit in operations used (`<`, copyability). A specialization customizes a template for particular arguments; distinguish full specialization from ordinary overloads. The blueprint names specialized functions and classes; ensure declaration order and namespace placement are valid.

Function templates cannot be partially specialized; use overloading or another design. Member function templates cannot be virtual. Selected [C++17 template rules](https://timsong-cpp.github.io/cppwp/n4659/temp) establish the workbook contracts.

Nested template usage produces closing angle brackets and dependent types/names that can require `typename` or `template` disambiguation in applicable contexts. Operator functions can support template classes when their declarations, access, and deduction are designed correctly.

> **Related item:** Concepts express constraints directly in C++20, but they are not named in this blueprint. Use them as modern context only after you can diagnose the unconstrained template mechanics being tested.

## Original executable workbook

Save these seven exact files together. C++17 is this workbook's practice baseline, not a provider declaration of one mandatory exam language mode. Configure with `cmake -S . -B build`, then `cmake --build build`. Run the four executables (`containers`, `algorithms`, `ordering`, `reporting`) from the generated build directory; multi-configuration generators may use a configuration subdirectory. The warning flags below target GCC/Clang.

| Program | Observed checks | Focus |
|---|---:|---|
| containers | 34 | Sequence/adaptor/associative operations, valid handles, user-defined ordering |
| algorithms | 52 | Search boundaries, callable state, destinations, valid overlap, logical ends and partitions |
| ordering | 32 | Comparator diagnostics, bounds, duplicates, merge, set and extrema contracts |
| reporting | 24 | Template mechanics, formatting restoration, EOF recovery and injected output failure |

Sixteen hosted CMake builds/runs passed: all four programs on GCC 15.2 and Clang 20.1, four GCC optimized variants and four Clang AddressSanitizer/UndefinedBehaviorSanitizer variants. Each build compiles all four programs before executing the selected target. Hosted Clang uses the GCC 14.2 external toolchain, so these are not independent libc++ or MSVC results. Checks remain active in optimized builds. Only original public-purpose source was sent through the [Compiler Explorer API](https://github.com/compiler-explorer/compiler-explorer/blob/main/docs/API.md), with code-debug storage disabled.

Sixteen separate rejected-build probes (eight on each compiler) cover adapter iteration, sorting a list with `std::sort`, map-key mutation, mixed template deduction, function partial specialization, missing `typename`, missing `template`, and virtual member templates. Their diagnostics matched the intended errors. No algorithm was run with an invalid comparator, stale iterator or forbidden overlap, and no failed-build program was executed. Sanitizers cover only the paths tested; finite comparator checks do not prove a universal ordering.

### check.hpp

```cpp
#ifndef CPP_CHECK_HPP
#define CPP_CHECK_HPP
#include <cstdlib>
#include <iostream>
inline int checks = 0;
inline void check(bool ok, const char* expression, int line) {
    ++checks;
    if (!ok) {
        std::cerr << "line " << line << ": " << expression << '\n';
        std::exit(1);
    }
}
#define CHECK(...) check((__VA_ARGS__), #__VA_ARGS__, __LINE__)
#endif
```

### containers.cpp

```cpp
#include "check.hpp"
#include <algorithm>
#include <deque>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

struct Job { int urgency; int id; };
struct LowerPriority {
    bool operator()(const Job& a, const Job& b) const {
        return a.urgency < b.urgency ||
            (a.urgency == b.urgency && a.id > b.id);
    }
};
struct Key { int group; std::string label; };
struct ByGroup {
    bool operator()(const Key& a, const Key& b) const { return a.group < b.group; }
};

int main() {
    std::vector<int> v;
    v.reserve(8);
    CHECK(v.empty() && v.capacity() >= 8);
    v.resize(3, 7);
    CHECK(v == std::vector<int>({7, 7, 7}));
    int* first = &v.front();
    v.push_back(9); // Capacity is sufficient: existing element handles survive.
    CHECK(&v.front() == first && *first == 7);
    auto next = v.erase(v.begin() + 1); // Use the returned iterator.
    CHECK(v.size() == 3 && next == v.begin() + 1 && *next == 7);
    v.reserve(v.capacity() + 1); // Guaranteed reallocation. Do not use first/next.
    CHECK(v == std::vector<int>({7, 7, 9}));

    std::deque<int> d{2, 3};
    int& middle = d.front();
    d.push_front(1);
    d.push_back(4); // References survive end insertion; old iterators do not.
    CHECK(middle == 2 && &middle == &d[1]);
    CHECK(d.front() == 1 && d.back() == 4);
    d.pop_front(); d.pop_back();
    CHECK(d == std::deque<int>({2, 3}));

    std::list<int> a{3, 1}, b{2, 2};
    auto transferred = b.begin();
    a.splice(a.end(), b, transferred); // Equal default allocators.
    CHECK(a.size() == 3 && b.size() == 1 && *transferred == 2);
    a.sort();
    CHECK(std::vector<int>(a.begin(), a.end()) == std::vector<int>({1, 2, 3}));
    CHECK(*transferred == 2);
    a.merge(b);
    CHECK(b.empty() && a.size() == 4);
    a.unique();
    CHECK(a.size() == 3);
    a.remove(2); // Member remove actually erases nodes; transferred is invalid now.
    CHECK(std::vector<int>(a.begin(), a.end()) == std::vector<int>({1, 3}));
    a.reverse();
    CHECK(a.front() == 3);

    std::stack<int, std::vector<int>> lifo;
    CHECK(lifo.empty());
    lifo.push(4); lifo.push(9);
    CHECK(!lifo.empty() && lifo.top() == 9);
    lifo.pop(); CHECK(!lifo.empty() && lifo.top() == 4);
    std::queue<int, std::list<int>> fifo;
    fifo.push(4); fifo.push(9);
    CHECK(!fifo.empty() && fifo.front() == 4 && fifo.back() == 9);
    fifo.pop(); CHECK(!fifo.empty() && fifo.front() == 9);
    std::priority_queue<Job, std::vector<Job>, LowerPriority> jobs;
    jobs.push({2, 8}); jobs.push({5, 7}); jobs.push({5, 3});
    auto copy = jobs; // Draining a copy is not adapter iterator traversal.
    std::vector<int> order;
    while (!copy.empty()) { order.push_back(copy.top().id); copy.pop(); }
    CHECK(order == std::vector<int>({3, 7, 8}) && jobs.size() == 3);

    std::set<Key, ByGroup> keys;
    CHECK(keys.insert({1, "red"}).second);
    CHECK(!keys.insert({1, "blue"}).second); // Comparison equivalence, not ==.
    CHECK(keys.size() == 1 && keys.begin()->label == "red");
    std::multiset<int> duplicates{1, 2, 2, 3};
    auto range = duplicates.equal_range(2);
    CHECK(std::distance(range.first, range.second) == 2);
    CHECK(duplicates.erase(2) == 2 && duplicates.count(2) == 0);
    std::map<std::string, int> counts{{"red", 2}};
    CHECK(counts.find("blue") == counts.end() && counts.size() == 1);
    CHECK(counts["blue"] == 0 && counts.size() == 2);
    auto red = counts.find("red");
    CHECK(red != counts.end());
    red->second += 3; // The mapped value is mutable; the key is const.
    CHECK(counts.at("red") == 5);
    counts.emplace("green", 1);
    CHECK(red->second == 5); // Insertion preserves existing map iterators.
    std::multimap<int, char> letters{{2, 'a'}, {2, 'b'}, {3, 'c'}};
    auto bounds = letters.equal_range(2);
    CHECK(std::distance(bounds.first, bounds.second) == 2);
    auto after = letters.erase(bounds.first);
    CHECK(after != letters.end() && after->second == 'b' && letters.count(2) == 1);
    CHECK(letters.lower_bound(4) == letters.end());
    std::cout << "containers: " << checks << " checks\n";
}
```

### algorithms.cpp

```cpp
#include "check.hpp"
#include <algorithm>
#include <array>
#include <functional>
#include <iterator>
#include <vector>

struct Sum { int total = 0; void operator()(int n) { total += n; } };
int main() {
    std::vector<int> v{1, 2, 2, 3, 1, 2}, empty, needle{1, 2}, one{9};
    auto begin = v.begin(), end = v.end();
    CHECK(std::find(begin, end, 3) == begin + 3);
    CHECK(std::find(begin, end, 9) == end);
    CHECK(std::find(empty.begin(), empty.end(), 9) == empty.end());
    CHECK(std::find(one.begin(), one.end(), 9) == one.begin());
    CHECK(std::find_if(begin, end, [](int n) { return n > 2; }) == begin + 3);
    CHECK(std::search(begin, end, needle.begin(), needle.end()) == begin);
    CHECK(std::find_end(begin, end, needle.begin(), needle.end()) == begin + 4);
    CHECK(std::search(begin, end, empty.begin(), empty.end()) == begin);
    CHECK(std::find_end(begin, end, empty.begin(), empty.end()) == end);
    CHECK(std::find_first_of(begin, end, one.begin(), one.end()) == end);
    CHECK(std::find_first_of(begin, end, needle.begin(), needle.end()) == begin);
    CHECK(std::adjacent_find(begin, end) == begin + 1);
    CHECK(std::adjacent_find(one.begin(), one.end()) == one.end());
    CHECK(std::search_n(begin, end, 2, 2) == begin + 1);
    CHECK(std::search_n(begin, end, 0, 2) == begin);
    CHECK(std::search_n(begin, end, 3, 2) == end);
    CHECK(std::count(begin, end, 2) == 3);
    CHECK(std::count_if(begin, end, [](int n) { return n % 2 != 0; }) == 3);
    std::vector<int> short_range{1, 2};
    auto mismatch = std::mismatch(begin, end, short_range.begin(), short_range.end());
    CHECK(mismatch.first == begin + 2 && mismatch.second == short_range.end());
    CHECK(!std::equal(begin, end, short_range.begin(), short_range.end()));
    CHECK(std::equal(empty.begin(), empty.end(), empty.begin(), empty.end()));
    CHECK(std::equal(begin, begin + 2, short_range.begin())); // Proven two elements.
    auto sum = std::for_each(begin, end, Sum{});
    CHECK(sum.total == 11);
    Sum external;
    std::for_each(begin, end, std::ref(external));
    CHECK(external.total == 11);
    std::for_each(begin, end, [](int& n) { ++n; });
    CHECK(v == std::vector<int>({2, 3, 3, 4, 2, 3}));

    std::array<int, 5> left{{1, 2, 3, 4, 5}}, right = left;
    CHECK(std::copy(left.begin() + 1, left.end(), left.begin()) == left.end() - 1);
    CHECK(left == std::array<int, 5>{{2, 3, 4, 5, 5}});
    CHECK(std::copy_backward(right.begin(), right.end() - 1, right.end()) == right.begin() + 1);
    CHECK(right == std::array<int, 5>{{1, 1, 2, 3, 4}});
    std::vector<int> output(v.size()), appended;
    CHECK(std::copy(begin, end, output.begin()) == output.end() && output == v);
    appended.reserve(v.size());
    CHECK(appended.empty()); // reserve does not create writable elements.
    std::copy(begin, end, std::back_inserter(appended));
    CHECK(appended == v);
    std::vector<int> other(v.size(), 10);
    CHECK(std::transform(begin, end, other.begin(), output.begin(), std::plus<>{}) == output.end());
    CHECK(output == std::vector<int>({12, 13, 13, 14, 12, 13}));
    std::transform(output.begin(), output.end(), other.begin(), output.begin(), std::minus<>{});
    CHECK(output == v); // Exact in-place transform is permitted.
    std::swap(output.front(), output.back());
    std::iter_swap(output.begin(), output.end() - 1);
    CHECK(output == v);
    CHECK(std::swap_ranges(output.begin(), output.end(), other.begin()) == other.end());
    CHECK(other == v && output == std::vector<int>(v.size(), 10));
    std::replace(output.begin(), output.end(), 10, 4);
    std::replace_if(output.begin(), output.end(), [](int n) { return n == 4; }, 6);
    CHECK(output == std::vector<int>(v.size(), 6));
    std::fill(output.begin(), output.end(), 0);
    int calls = 0;
    std::generate(output.begin(), output.end(), [&calls] { ++calls; return 7; });
    CHECK(calls == 6 && output == std::vector<int>(6, 7));
    std::vector<int> removed{1, 2, 2, 3, 2, 4};
    auto logical_end = std::remove(removed.begin(), removed.end(), 2);
    CHECK(removed.size() == 6 && std::distance(removed.begin(), logical_end) == 3);
    CHECK(std::vector<int>(removed.begin(), logical_end) == std::vector<int>({1, 3, 4}));
    // Values in the valid but unspecified tail are not inspected.
    removed.erase(logical_end, removed.end());
    removed.erase(std::remove_if(removed.begin(), removed.end(), [](int n) { return n % 2 != 0; }), removed.end());
    CHECK(removed == std::vector<int>({4}));
    std::vector<int> adjacent{2, 2, 1, 2, 2}, unique_copy;
    std::unique_copy(adjacent.begin(), adjacent.end(), std::back_inserter(unique_copy));
    CHECK(unique_copy == std::vector<int>({2, 1, 2}));
    adjacent.erase(std::unique(adjacent.begin(), adjacent.end()), adjacent.end());
    CHECK(adjacent == unique_copy);
    std::reverse(adjacent.begin(), adjacent.end());
    CHECK(adjacent == std::vector<int>({2, 1, 2}));
    CHECK(std::rotate(adjacent.begin(), adjacent.begin() + 1, adjacent.end()) == adjacent.begin() + 2);
    CHECK(adjacent == std::vector<int>({1, 2, 2}));
    auto even = [](int n) { return n % 2 == 0; };
    std::vector<int> partitioned{1, 2, 3, 4, 5, 6}, stable = partitioned;
    auto split = std::partition(partitioned.begin(), partitioned.end(), even);
    CHECK(std::distance(partitioned.begin(), split) == 3);
    CHECK(std::all_of(partitioned.begin(), split, even));
    CHECK(std::none_of(split, partitioned.end(), even));
    std::stable_partition(stable.begin(), stable.end(), even);
    CHECK(stable == std::vector<int>({2, 4, 6, 1, 3, 5}));
    std::cout << "algorithms: " << checks << " checks\n";
}
```

### ordering.cpp

```cpp
#include "check.hpp"
#include <algorithm>
#include <functional>
#include <iterator>
#include <stdexcept>
#include <vector>

// A finite-domain diagnostic, not a proof for all possible comparator inputs.
template<class Compare>
bool strict_on(const std::vector<int>& domain, Compare less) {
    auto equiv = [&] (int a, int b) { return !less(a, b) && !less(b, a); };
    for (int a : domain) {
        if (less(a, a)) return false;
        for (int b : domain) {
            if (less(a, b) && less(b, a)) return false;
            for (int c : domain) {
                if (less(a, b) && less(b, c) && !less(a, c)) return false;
                if (equiv(a, b) && equiv(b, c) && !equiv(a, c)) return false;
            }
        }
    }
    return true;
}
std::vector<int> checked_merge(const std::vector<int>& a, const std::vector<int>& b) {
    if (!std::is_sorted(a.begin(), a.end()) || !std::is_sorted(b.begin(), b.end()))
        throw std::invalid_argument("ascending inputs required");
    std::vector<int> result;
    std::merge(a.begin(), a.end(), b.begin(), b.end(), std::back_inserter(result));
    return result;
}
struct Row { int key; char label; };
int main() {
    CHECK(strict_on({0, 1, 2}, std::less<int>{}));
    CHECK(!strict_on({0, 1, 2}, std::less_equal<int>{}));
    CHECK(!strict_on({0, 1, 2}, [](int a, int b) { return (a + 1) % 3 == b; }));
    CHECK(!strict_on({0, 1, 2}, [](int a, int b) { return a == 0 && b == 2; }));
    // Rejected comparators are never passed to sorting or ordered containers.
    std::vector<Row> rows{{2, 'a'}, {1, 'b'}, {2, 'c'}, {1, 'd'}};
    auto by_key = [](const Row& a, const Row& b) { return a.key < b.key; };
    std::stable_sort(rows.begin(), rows.end(), by_key);
    CHECK(rows[0].label == 'b' && rows[1].label == 'd' && rows[2].label == 'a' && rows[3].label == 'c');
    auto found = std::lower_bound(rows.begin(), rows.end(), 2,
        [](const Row& row, int key) { return row.key < key; });
    CHECK(found == rows.begin() + 2 && found->label == 'a');
    std::vector<int> values{3, 1, 2, 2};
    std::sort(values.begin(), values.end());
    CHECK(values == std::vector<int>({1, 2, 2, 3}));
    auto lo = std::lower_bound(values.begin(), values.end(), 2);
    auto hi = std::upper_bound(values.begin(), values.end(), 2);
    auto eq = std::equal_range(values.begin(), values.end(), 2);
    CHECK(lo == values.begin() + 1 && hi == values.begin() + 3 && eq.first == lo && eq.second == hi);
    CHECK(std::binary_search(values.begin(), values.end(), 2));
    CHECK(!std::binary_search(values.begin(), values.end(), 4));
    CHECK(std::lower_bound(values.begin(), values.end(), 4) == values.end());
    std::vector<int> partition_only{2, 1, 3, 5, 4};
    CHECK(!std::is_sorted(partition_only.begin(), partition_only.end()));
    CHECK(std::lower_bound(partition_only.begin(), partition_only.end(), 3) == partition_only.begin() + 2);
    CHECK(std::upper_bound(partition_only.begin(), partition_only.end(), 3) == partition_only.begin() + 3);
    // Partitioned for key 3 in both required directions; not a general sorted index.
    CHECK(std::binary_search(partition_only.begin(), partition_only.end(), 3));
    std::vector<int> a{1, 2, 2, 4}, b{2, 2, 2, 3}, out(8);
    auto output_end = std::merge(a.begin(), a.end(), b.begin(), b.end(), out.begin());
    CHECK(output_end == out.end() && out == std::vector<int>({1, 2, 2, 2, 2, 2, 3, 4}));
    std::vector<int> adjacent{1, 3, 5, 2, 4, 6};
    std::inplace_merge(adjacent.begin(), adjacent.begin() + 3, adjacent.end());
    CHECK(adjacent == std::vector<int>({1, 2, 3, 4, 5, 6}));
    auto end = std::set_union(a.begin(), a.end(), b.begin(), b.end(), out.begin());
    CHECK(std::vector<int>(out.begin(), end) == std::vector<int>({1, 2, 2, 2, 3, 4}));
    end = std::set_intersection(a.begin(), a.end(), b.begin(), b.end(), out.begin());
    CHECK(std::vector<int>(out.begin(), end) == std::vector<int>({2, 2}));
    end = std::set_difference(a.begin(), a.end(), b.begin(), b.end(), out.begin());
    CHECK(std::vector<int>(out.begin(), end) == std::vector<int>({1, 4}));
    end = std::set_difference(b.begin(), b.end(), a.begin(), a.end(), out.begin());
    CHECK(std::vector<int>(out.begin(), end) == std::vector<int>({2, 3}));
    end = std::set_symmetric_difference(a.begin(), a.end(), b.begin(), b.end(), out.begin());
    CHECK(std::vector<int>(out.begin(), end) == std::vector<int>({1, 2, 3, 4}));
    std::vector<int> two{2, 2}, three{2, 2, 2}, empty;
    CHECK(std::includes(a.begin(), a.end(), two.begin(), two.end()));
    CHECK(!std::includes(a.begin(), a.end(), three.begin(), three.end()));
    CHECK(std::includes(a.begin(), a.end(), empty.begin(), empty.end()));
    CHECK(checked_merge(empty, a) == a);
    bool rejected = false;
    try { (void)checked_merge({2, 1}, a); }
    catch (const std::invalid_argument&) { rejected = true; }
    CHECK(rejected);
    std::vector<int> ties{3, 1, 3, 1};
    CHECK(std::min_element(ties.begin(), ties.end()) == ties.begin() + 1);
    CHECK(std::max_element(ties.begin(), ties.end()) == ties.begin());
    auto extremes = std::minmax_element(ties.begin(), ties.end());
    CHECK(extremes.first == ties.begin() + 1 && extremes.second == ties.begin() + 2);
    CHECK(std::min_element(empty.begin(), empty.end()) == empty.end());
    CHECK(std::max_element(empty.begin(), empty.end()) == empty.end());
    std::cout << "ordering: " << checks << " checks\n";
}
```

### templates.hpp

```cpp
#ifndef CPP_TEMPLATES_HPP
#define CPP_TEMPLATES_HPP
#include <ostream>
template<class T> T clamp_low(T value, const T& minimum) {
    return value < minimum ? minimum : value;
}
template<class T> const char* type_label(const T&) { return "general"; }
template<> inline const char* type_label<int>(const int&) { return "integer"; }
template<class T> struct Label { static constexpr const char* text = "general"; };
template<> struct Label<int> { static constexpr const char* text = "integer"; };

template<class T> class Box {
    T value_;
public:
    using value_type = T;
    explicit Box(T value) : value_(value) {}
    T value() const { return value_; }
    template<class U> U converted() const { return static_cast<U>(value_); }
    template<class U> struct Pair { T left; U right; };
    // A separate non-template friend for each Box specialization.
    friend std::ostream& operator<<(std::ostream& out, const Box& box) {
        return out << box.value_;
    }
};
template<class B> typename B::value_type read_box(const B& box) {
    return box.value();
}
template<class B> double as_double(const B& box) {
    return box.template converted<double>();
}
#endif
```

### reporting.cpp

```cpp
#include "check.hpp"
#include "templates.hpp"
#include <iomanip>
#include <limits>
#include <locale>
#include <sstream>
#include <stdexcept>
#include <streambuf>
#include <string>

// Narrow contract: preserve four formatting fields. Do not clear errors or
// copy locales, callbacks, exception masks, ties or stream buffers.
class FormatGuard {
    std::ostream& out_;
    std::ios_base::fmtflags flags_;
    std::streamsize precision_, width_;
    char fill_;
public:
    explicit FormatGuard(std::ostream& out) : out_(out), flags_(out.flags()),
        precision_(out.precision()), width_(out.width()), fill_(out.fill()) {}
    FormatGuard(const FormatGuard&) = delete;
    FormatGuard& operator=(const FormatGuard&) = delete;
    ~FormatGuard() { out_.flags(flags_); out_.precision(precision_); out_.width(width_); out_.fill(fill_); }
};
void report(std::ostream& out, double value, bool fail = false) {
    FormatGuard restore(out);
    out.width(0);
    out.setf(std::ios_base::fixed, std::ios_base::floatfield);
    out.setf(std::ios_base::right, std::ios_base::adjustfield);
    out << std::noshowpoint << std::setfill('.') << std::setprecision(2) << std::setw(6) << value;
    if (fail) throw std::runtime_error("injected report failure");
}
class RefusingBuffer : public std::streambuf {
    int_type overflow(int_type) override { return traits_type::eof(); }
};
int main() {
    CHECK(clamp_low(2, 5) == 5 && clamp_low(7, 5) == 7);
    CHECK(clamp_low<double>(2, 2.5) == 2.5);
    CHECK(std::string(type_label(4)) == "integer");
    CHECK(std::string(type_label(4.0)) == "general");
    CHECK(std::string(Label<int>::text) == "integer" && std::string(Label<double>::text) == "general");
    Box<int> box(7);
    CHECK(read_box(box) == 7 && as_double(box) == 7.0);
    Box<int>::Pair<double> pair{3, 2.5};
    CHECK(pair.left == 3 && pair.right == 2.5);
    Box<Box<int>> nested(box);
    CHECK(nested.value().value() == 7);
    std::ostringstream printed;
    printed.imbue(std::locale::classic());
    printed << box;
    CHECK(printed.str() == "7");
    printed.str("");
    printed << std::setfill('_') << std::setw(3) << 7 << 8;
    CHECK(printed.str() == "__78" && printed.width() == 0 && printed.fill() == '_');
    printed.str("");
    printed << std::boolalpha << true << ' ' << false;
    CHECK(printed.str() == "true false");
    printed.str("");
    printed << std::fixed << std::noshowpoint << std::setprecision(2) << 2.0;
    CHECK(printed.str() == "2.00"); // noshowpoint does not override fixed precision.
    printed.setf(std::ios_base::scientific, std::ios_base::floatfield);
    CHECK((printed.flags() & std::ios_base::floatfield) == std::ios_base::scientific);
    printed.setf(std::ios_base::fixed); // ORs bits: both now select hexfloat.
    CHECK((printed.flags() & std::ios_base::floatfield) == std::ios_base::floatfield);
    printed << std::defaultfloat;
    CHECK((printed.flags() & std::ios_base::floatfield) == 0);
    printed.str(""); printed.precision(5); printed.width(9);
    auto old_flags = printed.flags();
    report(printed, 2.0);
    CHECK(printed.str() == "..2.00");
    CHECK(printed.flags() == old_flags && printed.precision() == 5 && printed.width() == 9 && printed.fill() == '_');
    bool thrown = false;
    try { report(printed, 3.0, true); }
    catch (const std::runtime_error&) { thrown = true; }
    CHECK(thrown && printed.flags() == old_flags && printed.precision() == 5 && printed.width() == 9 && printed.fill() == '_');

    std::istringstream input("42");
    input.imbue(std::locale::classic());
    int n = 0;
    input >> n;
    CHECK(n == 42 && input.eof() && !input.fail() && static_cast<bool>(input));
    input >> n;
    CHECK(input.eof() && input.fail() && !input);
    std::istringstream recovery("bad\n17\n");
    recovery.imbue(std::locale::classic());
    recovery >> n;
    CHECK(recovery.fail());
    recovery.clear(); // State repair alone does not consume the bad characters.
    recovery.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    recovery >> n;
    CHECK(recovery && n == 17);
    RefusingBuffer buffer;
    std::ostream failed(&buffer);
    failed.imbue(std::locale::classic());
    failed << 'x';
    CHECK(failed.bad() && failed.fail());
    failed.clear();
    failed.exceptions(std::ios_base::badbit);
    thrown = false;
    try { report(failed, 2.0); }
    catch (const std::ios_base::failure&) { thrown = true; }
    CHECK(thrown && failed.bad()); // FormatGuard did not hide the output failure.
    std::cout << "reporting: " << checks << " checks\n";
}
```

### CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.16)
project(cpp_workbook LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
foreach(target containers algorithms ordering reporting)
    add_executable(${target} ${target}.cpp)
    target_compile_options(${target} PRIVATE -Wall -Wextra -Wpedantic -Werror)
endforeach()
```

The two injected reporting failures are a deliberate thrown exception and a stream buffer that refuses output. Formatting restoration does not erase the stream error. No actual device failure, debugger session, full scheduler deployment or complete learner project was performed.

## Integrated scenarios

### Event-processing pipeline

Store events in a vector, sort stably by time, group/filter with partition/remove idioms, count/search by predicates, and build map indexes. Document every invalidation, output capacity, comparator, and returned iterator. Format a final report while restoring stream state.

### Catalog comparison

Load two sorted product sequences and calculate union, intersection, and both differences. Use `lower_bound`/`upper_bound` for duplicate ranges and templates for generic reporting. Test empty, duplicate-heavy, differently sorted, and user-defined-key cases.

### Scheduler simulator

Use a priority queue for runnable work, queue for FIFO arrivals, and set/map for identity/state. Transform and search records with stateful/stateless callables. Explain why adapters are not iterated and why comparator direction makes the expected item appear at `top`.

## Hands-on labs

These eight broader learner labs remain proposed. The workbook supplies bounded cases within them; it is not a claim that every scenario or every overload has been completed.

1. **Container decision table:** implement the same dataset with vector, deque, list, stack, queue, priority queue, set/multiset, and map/multimap; record operations, iterator category, and invalidation.
2. **Iterator-return workbook:** exercise every named non-modifying algorithm on empty/no-match/duplicate/boundary cases and explain each returned iterator.
3. **Destination-safety lab:** compare pre-sized output, `back_inserter`, overlapping copies, transform, fill, and generate. Prove every output range has existing writable elements or a valid growth mechanism, plus allowed overlap.
4. **Remove/unique pipeline:** demonstrate logical ends, erase-remove, adjacency of `unique`, stable/unstable partitioning, reverse, and rotate.
5. **Ordering laboratory:** write valid and invalid comparators; reject invalid ordering before invoking an algorithm, then apply sort/stable sort and lower/upper/binary search only under valid preconditions.
6. **Merge/set project:** combine duplicate-rich sorted ranges with every named operation, capture returned output ends, and verify multiplicity.
7. **Callable modernization:** implement operations with functions, functors, standard function objects, lambdas, and a legacy `ptr_fun` reading exercise without using it in modern-mode final code.
8. **Template/report application:** define generic functions/classes, a specialization, nested templates, and operator support; generate formatted reports and restore stream state.

## Original readiness checks

1. When does vector reallocation invalidate element handles?
2. Why is list not automatically fastest for arbitrary middle insertion?
3. Which iterator category does `std::sort` require?
4. What precondition applies before `top` or `pop`?
5. How do set and multiset differ?
6. Why can map's `operator[]` mutate during lookup?
7. What must a custom ordered-container comparator provide?
8. What does a failed search algorithm usually return?
9. Why must a two-range algorithm know the second range is long enough?
10. What destination rule applies to `copy`/`transform`?
11. Does `remove` reduce a vector's size?
12. What does `unique` consider duplicates by default?
13. How do partition and stable_partition differ?
14. How do sort and stable_sort differ?
15. Why is `<=` usually invalid as a sort comparator?
16. What does `lower_bound` return?
17. What precondition do binary-search algorithms require?
18. What input condition applies to merge and set algorithms?
19. What does `min_element` return for an empty range?
20. Which explicit objectives sit under the blueprint's “Merge, Heap, Min, Max” block?
21. What contract must `std::plus<>` meet in binary transform?
22. Why is `ptr_fun` legacy-only?
23. Which stream settings persist and which named one is usually one-shot?
24. How does `fixed` affect `setprecision`?
25. Why restore stream state in reusable code?
26. Why are template definitions commonly placed in headers?
27. When is a template specialization used?
28. What can template argument deduction refuse that an ordinary call conversion might allow?
29. What does `typename` disambiguate in dependent code?
30. What must you recheck before scheduling?

## Answer key

1. Reallocation invalidates all element pointers, references and iterators, including the old end. Insertion without reallocation and erase have position-specific rules; sufficient reserved capacity does not preserve an iterator at or after an insertion/erasure point.

2. Insertion is constant time once a valid list position is known. Finding that position can be linear, and allocation/cache costs still matter. Choose from the full access/mutation workload, not one complexity label.

3. Random-access iterators, with suitable movable/assignable/swappable elements and comparison. A list has bidirectional iterators; use `list::sort`, whose node behavior differs from generic sorting.

4. Prove the adapter is nonempty before element access/pop. Pop does not return the removed value; read/copy it first when needed. Standard adapters have no public iterator traversal.

5. Set permits one key per comparator-equivalence class; multiset permits multiple equivalent keys. Equivalence is neither key preceding the other under comparison, which can differ from operator==.

6. On a missing key, map subscript inserts an element with a value-initialized mapped value (zero for int). Use find for a nonmutating presence check, or at when absence should throw; mapped values are mutable but iterator keys are const.

7. A stable strict weak ordering: irreflexivity, transitivity and transitive induced equivalence. External mutable comparison state must not change the order of stored keys. Finite tests help expose violations but cannot prove all inputs.

8. Usually last for absence, but learn the actual contract. Empty-needle search returns first, empty-needle find_end returns last, and mismatch returns an iterator pair. Check every result before dereferencing.

9. A three-iterator overload can read beyond a short second range. Supply both ends where supported or prove sufficient length first; the workbook uses four-ended mismatch/equal to expose length differences safely.

10. The destination needs enough existing writable elements or a valid insertion iterator. Reserve alone is insufficient. Serial copy allows suitable left overlap and copy_backward suitable right overlap under their exact endpoint rules; transform permits exact in-place output but not arbitrary mutation/invalidation.

11. No. Generic remove returns a logical end and leaves a valid but unspecified tail. Erase that tail to change vector size; list::remove instead erases nodes as a member operation.

12. Adjacent equivalent elements under equality/the supplied equivalence predicate. `{2,2,1,2,2}` becomes the logical sequence `{2,1,2}`, not `{1,2}`. Sorting first changes the problem and ordering.

13. Both put predicate-true elements before predicate-false elements and return the boundary. Only stable_partition promises original relative order within those groups; assert postconditions rather than a particular unstable arrangement.

14. Stable sort preserves original relative order among comparison-equivalent elements. Neither promise replaces iterator, element-type and strict-ordering preconditions.

15. It returns true for equal operands, violating irreflexivity. Even a relation that passes irreflexivity can fail strict transitivity or equivalence transitivity; reject it before sorting.

16. The first position where comp(element,key) is false, or last. Upper bound uses the opposite argument direction comp(key,element); both can delimit duplicates without dereferencing an end.

17. The specified partition conditions for the searched key/comparator. Globally sorting consistently is the usual sufficient setup, but a range can be valid for one key without being globally sorted. Iterator validity alone does not establish ordering.

18. Sorted inputs under the required comparison, valid element operations, and sufficient nonoverlapping output where specified. Duplicate counts matter: union takes max, intersection min, left difference the positive excess, symmetric difference the absolute excess.

19. Last, which must not be dereferenced. For nonempty ranges min_element/max_element choose the first equivalent extreme; minmax_element instead chooses the last equivalent maximum.

20. Merge/in-place merge, includes and sorted-set operations, and min/max element search. The block title mentions heap but no individual heap algorithm appears in its numbered list; priority_queue supplies adjacent heap context.

21. It must accept the dereferenced operand types and produce a result writable to output; both inputs must be long enough. It provides no overflow check. Transparent plus<> forwards/deduces instead of fixing one T as plus<T> does.

22. The function-pointer adapter was deprecated in C++11 and removed from C++17. Both observed hosted library configurations retain it with warnings even in C++17 mode; acceptance is an implementation observation, not a standard guarantee.

23. Flags, precision and fill persist. Width set by setw is consumed/reset by ordinary numeric/string insertion, so repeat it for each field. Not every stream operation consumes width; a reusable guard must account for pending width.

24. For ordinary fixed decimal output, precision controls digits after the decimal. Noshowpoint does not cancel that precision: fixed precision two still emits 2.00. Defaultfloat uses different significant-digit behavior; locale affects presentation.

25. To preserve the caller's formatting contract, including exceptional exits. Define which fields you restore; do not silently clear I/O errors or copy exception masks/callbacks/locales as if those were only cosmetic settings.

26. Implicit instantiation generally needs the definition available. Header definitions are a common solution, while controlled explicit-instantiation designs are another; a declaration alone is not a universal separate-compilation recipe.

27. A full specialization supplies behavior for particular template arguments and must be declared before uses that would instantiate it. A function overload is a different mechanism; function templates cannot be partially specialized.

28. Deduction from int and double arguments can conflict for one T even though either could convert after a choice. Explicit clamp_low<double>(2,2.5) makes that choice; do not assume deduction searches all possible common types.

29. That a dependent qualified name denotes a type in a context that requires disambiguation. In C++17 the workbook uses typename B::value_type, and uses the distinct template disambiguator in box.template converted<double>().

30. Active code, every detailed objective, scoring/format, language, delivery, current prices and policies. Resolve the canonical-recommended versus Pearson/badge-required CPA conflict, the 42/50-hour and 22-01/22-02 course differences, and actual appointment change terms before relying on eligibility or purchase assumptions.

## Final readiness checklist

- [ ] I choose sequence/adaptor/associative containers from operations and invalidation, not habit.
- [ ] I express half-open ranges and check every returned iterator before dereference.
- [ ] I prove output capacity, overlap, sortedness, comparator, and predicate contracts.
- [ ] I complete erase-remove and erase-unique rather than confusing logical and physical ends.
- [ ] I use consistent strict weak ordering for sort, lookup, merge, and set operations.
- [ ] I know the named algorithms and can choose them from required postconditions.
- [ ] I provide compatible functions/functors/lambdas and recognize `ptr_fun` only as legacy scope.
- [ ] I predict and restore persistent versus one-shot stream formatting state.
- [ ] I define, instantiate, specialize, nest, and diagnose function/class templates.
- [ ] I rechecked the live official page immediately before purchase.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick one aligned primary path, then use a current reference while writing algorithm-heavy programs. Always reconcile a resource's C++ version with the active CPP-22-02 blueprint, particularly for removed `ptr_fun` examples.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official CPP page and syllabus](https://cppinstitute.org/cpp) | Free canonical blueprint | 2–3 hours to map and recheck |
| [C++ Institute exam policies](https://cppinstitute.org/exam-policies) | Free official policy | 20–40 minutes before scheduling |
| [OpenEDG C++ Advanced](https://edube.org/study/cpp) | Public landing read; enrolled interior not read; names CPP-22-01 and prior CPA-course completion | 42 hours listed; conflicts with vendor landing |
| [C++ Institute Advanced course](https://cppinstitute.org/cpp-advanced) | Public landing read; names CPP-22-02 and no formal prerequisite | 50 hours listed; conflicts with Edube |
| [Cisco Networking Academy C++ Advanced](https://www.netacad.com/courses/c-plus-plus-advanced) | HTTP 200 application shell only; rendered course not read | Duration and availability unverified |
| [Microsoft C++ Standard Library reference](https://learn.microsoft.com/en-us/cpp/standard-library/cpp-standard-library-reference?view=msvc-170) | Free official implementation documentation | Ongoing; 10–20 hours targeted use |
| [cppreference containers library](https://en.cppreference.com/w/cpp/container.html) | Free community reference | 6–10 hours targeted study |
| [cppreference algorithms library](https://en.cppreference.com/w/cpp/algorithm.html) | Free community reference | 10–20 hours plus labs |
| [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) | Free modern guidance; extends blueprint | 8–15 hours selected sections |
| [Pluralsight C++ path](https://www.pluralsight.com/paths/c-plus-plus) | Public landing read; 13 courses, rounded 44-hour banner; paid lessons not read | Listed durations total 44 h 10 m; select matching modules |
| [O'Reilly C++20 STL Cookbook, 2nd Edition](https://www.oreilly.com/library/view/c20-stl-cookbook/9781803248714/) | 403 access block; interior and alignment not verified | Estimate only: 15–25 hours selected recipes |
| [Udemy Mastering the C++ Standard Library](https://www.udemy.com/course/mastering-the-cpp-standard-library/) | 403 access block; interior and alignment not verified | Estimate only: 12–20 hours selected material |

No exact current MeasureUp or Whizlabs CPP-22-02 practice product was verified. The Edube/vendor course fields disagree, so validate practice against all 34 canonical objectives instead of trusting a title. Resource study-time ranges other than expressly listed provider durations are planning estimates, not measured completion times. The cppreference algorithm index was fetched but not read in this review; selected container-index passages were read. Core Guidelines reading was limited to selected rules in the preceding CPA review, not a new full audit. Microsoft reference reading covered its index, not every linked chapter. Primary draft reading was selective and its exact boundaries are recorded in the review evidence.
