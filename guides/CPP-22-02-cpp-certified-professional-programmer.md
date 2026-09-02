---
exam_code: CPP-22-02
vendor_id: cpp-institute
official_blueprint: https://cppinstitute.org/cpp
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# CPP-22-02 C++ Certified Professional Programmer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, links, lifecycle, and exam-integrity compliance were checked September 2, 2026. This does not guarantee that every explanation is error-free or remains current. The [official CPP page and syllabus](https://cppinstitute.org/cpp) are authoritative.

**Current baseline:** CPP-22-02, active; nine-block syllabus last updated July 22, 2025<br>
**Upcoming blueprint change:** none announced on the official exam or certification-catalog pages when checked<br>
**Official delivery snapshot:** 40 single- and multiple-choice questions; 65-minute exam plus approximately 10 minutes for the NDA/tutorial; 70% cumulative passing score; Pearson VUE; English<br>
**Purchase snapshot:** CPA recommended; from USD 325 exam or USD 375 exam-plus-retake when checked<br>

## How to use this guide

CPP is primarily an STL, algorithms, iterators, function-object, stream-formatting, and templates exam. Practice by writing the preconditions and postconditions of every operation before calling it. For algorithms, name the input range, output destination, ordering/predicate, invalidation effects, returned iterator, and complexity-relevant container choice.

Use this loop:

1. choose the container from access, insertion, ordering, uniqueness, and invalidation needs;
2. express work as half-open iterator ranges `[first, last)`;
3. state every sorted-range, output-capacity, and comparator/predicate precondition;
4. predict the returned iterator and logical versus physical container state;
5. compile in an explicit standard mode and test empty, singleton, duplicate, boundary, and invalidation cases.

The blueprint includes `std::ptr_fun`, a legacy adapter deprecated in C++11 and removed in C++17. Recognize it for the published objective, but use lambdas or modern callable adapters in new code. The provider-aligned C++ Advanced course page still labels its associated version CPP-22-01 while the live exam page says CPP-22-02; use the live exam syllabus as canonical and verify alignment before relying on course assessments.

The live page also contains an internal arithmetic inconsistency: it says the exam has 40 questions, while its nine block counts total 32 and its displayed weights total 107%. The table below preserves the provider-published block values so future source checks can detect a correction. Do not treat the percentages as a normalized study plan; cover every listed objective.

> **About related items:** A `Related item:` callout supplies adjacent, prerequisite, operational, or modern-practice context. It helps you understand an objective; it does not claim that the extra item appears verbatim in the exam blueprint.

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

### Adapters

`std::stack` exposes last-in/first-out operations (`top`, `push`, `pop`). `std::queue` exposes first-in/first-out (`front`, `back`, `push`, `pop`). `std::priority_queue` exposes the highest-priority element under its comparison convention. These are adapters over underlying containers and deliberately do not expose general iteration.

```cpp
std::priority_queue<int> pending;
pending.push(4);
pending.push(9);
int next = pending.top(); // 9
pending.pop();
```

Calling `front`, `back`, `top`, or `pop` on an empty container/adapter violates its precondition. Check `empty()` first.

> **Related item:** Iterator category constrains algorithms. A list supplies bidirectional—not random-access—iterators, so `std::sort` does not apply; `list::sort` is the container-specific operation.

## 2. Associative containers — 13.25%

`std::set` stores unique keys; `multiset` permits equivalent keys. `map` stores unique key/value pairs; `multimap` permits equivalent keys. These ordered associative containers organize elements according to a comparison and traverse in that order—not insertion order.

Use `find` when you need an iterator, `count` for occurrence count, `lower_bound`/`upper_bound` for an equivalent-key range, `equal_range` for both boundaries, and `erase` with exact awareness of whether an iterator/key/range overload is selected. Test against `end()` before dereference.

Map iterator values are key/value pairs whose key is not modifiable through the iterator, because changing it in place would break ordering. `operator[]` on `map` inserts a default-mapped value when a key is missing; use `find`/`at` when lookup should not mutate.

Custom comparison must provide a strict weak ordering and remain consistent for stored keys. For a user-defined key, encode the intended fields deliberately and do not let mutable external state change ordering behavior.

> **Related item:** `unordered_*` containers are useful modern alternatives but are outside this published container list. Do not replace ordered-container study with hash-table assumptions.

## 3. Non-modifying sequence algorithms — 13.25%

Algorithms consume iterator ranges, usually `[first, last)`. Non-modifying means they do not modify elements through the range; a supplied function can still have external side effects, so use that power carefully.

- `for_each` invokes an operation for each element;
- `find`/`find_if` locate a value/predicate match;
- `find_end` finds the last occurrence of a subsequence;
- `find_first_of` finds an element matching any in another range;
- `adjacent_find` locates neighboring matches;
- `search` locates a subsequence and `search_n` repeated matching elements;
- `count`/`count_if` count matches;
- `mismatch` finds first differing paired elements;
- `equal` checks range equivalence under applicable overloads.

Search algorithms generally return the end iterator when no match is found. Never dereference before checking. Two-range algorithms require a sufficiently long second range under the selected overload/version; pass explicit end bounds where available.

Predicates should not invalidate the range or rely on an unstable order of invocation. If you need transformed output, use `transform` rather than hiding mutation in a supposedly observational predicate.

## 4. Modifying sequence algorithms — 13.25%

Destination-writing algorithms require enough valid output space unless an insertion iterator grows a container. `copy` and `copy_backward` have different overlap allowances/directions; use the correct tool or a container member operation. `fill` assigns a value; `generate` obtains each value from a callable.

`transform` writes transformed results. `swap`, `iter_swap`, and `swap_ranges` exchange objects/ranges under their preconditions. `replace` changes matching elements.

`remove`/`remove_if` do not erase container elements. They move retained elements toward the front and return a new logical end; erase the tail for sequence containers:

```cpp
values.erase(
    std::remove_if(values.begin(), values.end(), is_invalid),
    values.end());
```

Likewise, `unique` coalesces consecutive equivalent elements and returns a logical end; sort first only if the desired rule is “remove all duplicates regardless of original adjacency.” `unique_copy` writes retained values to a destination.

`reverse`, `rotate`, `partition`, and `stable_partition` reorder elements. Partition separates elements by a predicate but does not necessarily sort either group; stable partition preserves relative order within groups. Returned iterators identify meaningful boundaries—capture and use them.

> **Related item:** C++20 ranges and `std::erase_if` can make intent clearer, but the exam names classic STL algorithms. Understand iterator-based mechanics before translating to newer interfaces.

## 5. Sorting and binary search — 16.5%

`sort` requires random-access iterators and does not preserve equivalent-element order. `stable_sort` preserves it. A custom comparator must act like strict weak ordering: irreflexive, asymmetric in the necessary sense, and transitively consistent. Use `left.field < right.field`, not `<=`.

`lower_bound` returns the first position not ordered before a value; `upper_bound` returns the first position ordered after it; `[lower, upper)` is the equivalent range. `binary_search` reports presence, not position. These algorithms require ranges partitioned/sorted consistently with the comparison and searched value.

Do not sort with one criterion and binary-search with an incompatible one. Mutating keys/order-relevant fields behind an ordered range invalidates the precondition even if container iterators remain technically valid.

```cpp
std::sort(records.begin(), records.end(), by_id);
auto first = std::lower_bound(records.begin(), records.end(), id, record_before_id);
```

Be precise about heterogeneous comparator overloads: the callable signatures can differ between element-element sorting and element-value bounds.

## 6. Merge, set, and min/max algorithms — 16.5%

`merge` combines two sorted input ranges into a sorted output range; destination capacity and non-overlap requirements apply. `inplace_merge` merges two consecutive sorted subranges `[first, middle)` and `[middle, last)` in the original range.

`includes`, `set_union`, `set_intersection`, `set_difference`, and `set_symmetric_difference` operate on sorted ranges under the same ordering. Despite their names, duplicate multiplicity follows algorithm rules; inputs need not be `set` containers.

`min_element` and `max_element` return iterators, including `last` for an empty range. They compare elements under the supplied/default ordering. Capture the iterator and prove it is dereferenceable before access.

The official block title mentions heap, but the listed numbered objectives/keywords on the live page name merge, sorted-set operations, and min/max rather than individual heap algorithms. Prioritize the explicit objectives; treat heap operations as adjacent container/`priority_queue` context unless the provider updates the detailed list.

> **Related item:** Complexity depends on iterator category and algorithm/container choice. Correct output is necessary; professional selection also avoids repeatedly doing linear work where a maintained index/order is appropriate.

## 7. STL function objects and utilities — 7%

A function object is an object callable with `operator()`. Standard objects such as `std::plus<>` and `std::minus<>` can be passed to `transform` and other algorithms. Functions, lambdas, and callable objects must meet the algorithm's expected argument/result contract.

```cpp
std::transform(a.begin(), a.end(), b.begin(), result.begin(), std::plus<>{});
```

This requires `b` and `result` to cover enough elements (or an insertion iterator for output). A stateful function object can carry configuration, but copies and invocation order must not silently violate expectations.

`std::ptr_fun` wrapped function pointers for older adapter ecosystems. It was deprecated in C++11 and removed in C++17. Recognize its historic role for the blueprint; use lambdas, `std::function` when type erasure is genuinely needed, or `std::bind`/`std::mem_fn` selectively in current code.

## 8. Advanced I/O — 7%

Streams carry formatting state. Flags such as base, float, adjustment, show-point, and Boolean text can persist; some manipulators are one-shot. `setw` normally affects the next formatted field, whereas `fixed`, `boolalpha`, precision, and many flags persist until changed.

`setf` sets flags, optionally within a mask field; `unsetf` clears flags. `boolalpha` writes/reads textual Booleans. `fixed` changes floating formatting interpretation; `setprecision` means digits after the decimal in fixed notation but has different meaning under default formatting. `noshowpoint` disables forced decimal/trailing-zero display. Check stream state after input/output operations.

Preserve caller stream settings when a reusable formatter should not leak its choices. One approach is to save and restore flags, precision, and fill deliberately.

> **Related item:** Formatting is presentation, not numerical accuracy. Displaying two decimal digits does not make a binary floating calculation exact or implement monetary rounding policy.

## 9. Templates — 7%

Function and class templates define families parameterized by types or values. Instantiation substitutes arguments and checks the resulting use. Template definitions generally must be visible where implicitly instantiated, which is why they commonly live in headers.

```cpp
template<class T>
T clamp_low(T value, const T& minimum) {
    return value < minimum ? minimum : value;
}
```

Template argument deduction does not perform every conversion ordinary overload resolution might. Constraints are often implicit in operations used (`<`, copyability). A specialization customizes a template for particular arguments; distinguish full specialization from ordinary overloads. The blueprint names specialized functions and classes; ensure declaration order and namespace placement are valid.

Nested template usage produces closing angle brackets and dependent types/names that can require `typename` or `template` disambiguation in applicable contexts. Operator functions can support template classes when their declarations, access, and deduction are designed correctly.

> **Related item:** Concepts express constraints directly in C++20, but they are not named in this blueprint. Use them as modern context only after you can diagnose the unconstrained template mechanics being tested.

## Integrated scenarios

### Event-processing pipeline

Store events in a vector, sort stably by time, group/filter with partition/remove idioms, count/search by predicates, and build map indexes. Document every invalidation, output capacity, comparator, and returned iterator. Format a final report while restoring stream state.

### Catalog comparison

Load two sorted product sequences and calculate union, intersection, and both differences. Use `lower_bound`/`upper_bound` for duplicate ranges and templates for generic reporting. Test empty, duplicate-heavy, differently sorted, and user-defined-key cases.

### Scheduler simulator

Use a priority queue for runnable work, queue for FIFO arrivals, and set/map for identity/state. Transform and search records with stateful/stateless callables. Explain why adapters are not iterated and why comparator direction makes the expected item appear at `top`.

## Hands-on labs

1. **Container decision table:** implement the same dataset with vector, deque, list, stack, queue, priority queue, set/multiset, and map/multimap; record operations, iterator category, and invalidation.
2. **Iterator-return workbook:** exercise every named non-modifying algorithm on empty/no-match/duplicate/boundary cases and explain each returned iterator.
3. **Destination-safety lab:** compare pre-sized output, `back_inserter`, overlapping copies, transform, fill, and generate. Prove every output range has capacity.
4. **Remove/unique pipeline:** demonstrate logical ends, erase-remove, adjacency of `unique`, stable/unstable partitioning, reverse, and rotate.
5. **Ordering laboratory:** write valid and invalid comparators; apply sort/stable sort and lower/upper/binary search under consistent/inconsistent ordering.
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

1. When an operation reallocates its storage; other operations have their own invalidation rules.
2. Finding the insertion position is linear and node/cache/allocation costs remain.
3. Random-access.
4. The adapter must not be empty.
5. Unique keys versus permitted equivalent keys.
6. It inserts a default-mapped value when the key is absent.
7. A stable strict weak ordering consistent for stored keys.
8. The supplied end iterator.
9. Older/applicable overloads can otherwise read beyond it; explicit paired ends or a proven length are required.
10. Existing sufficient writable elements or an insertion iterator that grows storage.
11. No; it returns a new logical end, after which erase changes physical size.
12. Consecutive equivalent elements.
13. Both group by predicate; stable partition preserves relative order within groups.
14. Stable sort preserves relative order of equivalent elements.
15. It is not irreflexive and therefore not a strict weak ordering.
16. First position not ordered before the value.
17. A range partitioned/sorted consistently with the same ordering relation.
18. Both inputs are sorted under the same ordering, plus valid output where applicable.
19. The supplied `last` iterator.
20. Merge/in-place merge, sorted set operations, includes, and min/max element search; no numbered heap operation is currently listed.
21. Accept the dereferenced input element types and produce a value writable to output.
22. It was deprecated in C++11 and removed in C++17; modern callables/lambdas replace it.
23. Many flags and precision persist; `setw` ordinarily affects the next field.
24. Precision becomes the number of digits after the decimal point.
25. To prevent surprising formatting changes in the caller's later output.
26. The definition must generally be visible where implicit instantiation occurs.
27. To customize the family for specified template arguments.
28. Conversions not considered during deduction even though they may occur after a match.
29. That a dependent qualified name is a type.
30. Active version, detailed syllabus, course-version alignment, delivery, language, price, format, and policies.

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
| [OpenEDG C++ Advanced](https://edube.org/study/cpp) | Free account; provider-aligned content, but page still labels CPP-22-01 | 42 hours listed; cross-check every module |
| [Cisco Networking Academy C++ Advanced](https://www.netacad.com/courses/c-plus-plus-advanced) | Free account if currently available; official partner | Plan about 42 hours; verify live version |
| [Microsoft C++ Standard Library reference](https://learn.microsoft.com/en-us/cpp/standard-library/cpp-standard-library-reference?view=msvc-170) | Free official implementation documentation | Ongoing; 10–20 hours targeted use |
| [cppreference containers library](https://en.cppreference.com/w/cpp/container.html) | Free community reference | 6–10 hours targeted study |
| [cppreference algorithms library](https://en.cppreference.com/w/cpp/algorithm.html) | Free community reference | 10–20 hours plus labs |
| [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) | Free modern guidance; extends blueprint | 8–15 hours selected sections |
| [Pluralsight C++ path](https://www.pluralsight.com/paths/c-plus-plus) | Subscription; broad 44-hour path with current container and algorithm courses | Select containers/iterators/algorithms/templates, 15–25 hours |
| [O'Reilly C++20 STL Cookbook, 2nd Edition](https://www.oreilly.com/library/view/c20-stl-cookbook/9781803248714/) | Subscription; modern examples beyond blueprint | 15–25 hours selected recipes |
| [Udemy Mastering the C++ Standard Library](https://www.udemy.com/course/mastering-the-cpp-standard-library/) | Paid marketplace course; verify syllabus/version | Select matching material, 12–20 hours |

No exact current MeasureUp or Whizlabs CPP-22-02 practice product was verified. The official aligned course page's version label is stale relative to the live exam page, so validate practice objectives against the canonical nine-block syllabus rather than trusting a product title.
