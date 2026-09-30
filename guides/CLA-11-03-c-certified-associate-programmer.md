---
exam_code: CLA-11-03
vendor_id: cpp-institute
official_blueprint: https://cppinstitute.org/cla
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# CLA-11-03 C Certified Associate Programmer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, links, lifecycle, and exam-integrity compliance were checked September 29, 2026. This does not guarantee that every explanation is error-free or remains current. The [official CLA page and syllabus](https://cppinstitute.org/cla) are authoritative.

**CURRENT BLUEPRINT — current baseline:** CLA-11-03, active; four-block syllabus last updated July 24, 2025<br>
**Upcoming blueprint change:** none announced on the official exam or certification-catalog pages when checked<br>
**VERIFY CURRENT — delivery snapshot:** 40 single- and multiple-select questions; 65-minute exam plus approximately 10 minutes for the NDA/tutorial; 70% cumulative passing score; Pearson VUE; English<br>
**VERIFY CURRENT — purchase snapshot:** no formal prerequisite; from USD 325 exam or USD 375 exam-plus-retake when checked<br>

The [dated deep-review record](../docs/research/2026-09-29-cla-11-03-deep-review.md) maps all **23 objectives**, grouped 6/7/6/4. Original multi-file examples ran through hosted GCC 15.2 and Clang 20.1 in **C17 mode**, an author practice choice rather than an exam requirement. Both passed 181 loader checks and 53 language checks; selected optimized, configuration and sanitizer runs also passed. No local compiler was installed. Eight broader activities remain proposed.

## How to use this guide

CLA expects a coherent model of translation, declarations, storage, pointers, control flow, preprocessing, and streams. Build multi-file programs, not only isolated expressions. Before running code, identify each declaration's scope, linkage, storage duration, initialization, owner, and valid pointer range.

Study in a tight loop:

1. map the task to the four official blocks;
2. predict diagnostics, types, state, output, and resource lifetime;
3. compile in a declared C language mode with strong warnings;
4. use a debugger plus address/undefined-behavior sanitizers where available;
5. rerun normal, boundary, malformed, and failure-path cases.

C Essentials Parts 1 and 2 together are the provider's full aligned path. CLE knowledge is not a formal prerequisite, but it is operationally assumed here; close any gaps before spending most of your time on storage/linkage, pointer arithmetic, macros, and files.

> **About related items:** A `Related item:` callout supplies adjacent, prerequisite, operational, or modern-practice context. It helps you understand an objective; it does not claim that the extra item appears verbatim in the exam blueprint.

## Weighted objective map

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| 1. Language and Structures | 12 | 29% | Explain declarations/definitions and model arrays, structs, storage classes, and tokens |
| 2. Data Operations | 14 | 38% | Trace conversions, pointers, memory layout, scope, linkage, and lifetime |
| 3. Control Flow | 10 | 25% | Prove branch/loop/function behavior and caller-visible mutation |
| 4. Environment | 4 | 8% | Expand macros/conditionals mentally and use formatted file I/O safely |

Items carry different point values; the official page states a 100-point maximum and a normalized cumulative score. Forty items do not imply equal points per item. The weights guide study time but do not justify skipping the environment block.

**VERIFY CURRENT — delivery and lifecycle.** The [certification catalog](https://cppinstitute.org/certification-exams) describes lifetime credentials tied to the completed exam version. The [Pearson scheduling page](https://cppinstitute.org/schedule-exam-pvue), revised October 14, 2025, explicitly includes CLA-11-03 in its test-center/OnVUE overview. The associate/professional section of the [exam policies](https://cppinstitute.org/exam-policies) specifies a **15-day failed-retake wait** and no repeat of a passed exam version; the entry-level seven-day TestNow rule does not apply. Rescheduling copy conflicts between “anytime before” and a 24-hour threshold; the newer scheduling page generally says 24 hours. Confirm the actual appointment rules, region, accommodations and product before payment. No authenticated booking was inspected.

## 1. Language and structures — 29%

### Declarations, definitions, and lexical structure

A declaration introduces an identifier and its type/attributes; an object definition supplies storage, and a function definition supplies its body. `extern int count;` normally declares an externally linked object without defining it; one translation unit should supply `int count = 0;`. At file scope, `int count;` is a tentative definition: if the translation unit has no full definition, it supplies a zero-initialized definition at the end. Repeating compatible tentative declarations in one translation unit differs from placing competing external definitions in multiple source files. An initializer makes `extern int count = 0;` a definition. The workbook and diagnostic checks demonstrate these distinctions. See the selected scope/linkage clauses of the [WG14 N1570 C11 draft](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf); this historical committee draft is not a claim that CLA prescribes C11.

C source becomes preprocessing tokens and then tokens such as identifiers, keywords, constants, string literals, operators, and punctuators. Identifiers are case-sensitive, cannot be keywords, and have context-dependent significance limits. Comments behave like whitespace during translation; they do not nest. Choose meaningful names such as `reading_count`; a leading digit, keyword or punctuation such as a hyphen cannot be part of an ordinary identifier in the intended way. Avoid reserved implementation/library names and leading-underscore naming schemes in learner code. Character constants such as `'A'` have type int in C17; `"A"` includes a terminating byte. Do not assume C++ rules or ASCII letter values.

Use headers for declarations shared by translation units and source files for definitions. An include guard prevents repeated header contents within one preprocessing translation:

The complete `reading.h` below uses `CLA_READING_H` as its guard. It declares the structure and API once per translation unit; `reading.c` supplies the external function definitions.

> **Related item:** A linker error is often a declaration/definition or linkage problem, not evidence that the header should contain another non-`static` definition.

### Arrays and structures

An array owns a fixed sequence of elements. Initialization may supply all values or a prefix, with remaining elements zero-initialized where the rules apply. A `struct` groups named members; its padding and alignment mean its object representation is not necessarily the arithmetic sum of member sizes.

The public header defines `struct Reading`; the tests initialize records with compound literals and access only initialized elements. A declaration such as `struct Reading readings[3] = {{1u, 2.5}};` initializes the remaining members and records to their appropriate zero values.

Use `object.member` for an object and `pointer->member` for a valid pointer. Structure assignment copies members, but a pointer member still copies an address rather than cloning the pointed-to allocation.

### Storage classes and duration

At this level, distinguish automatic, static, and allocated duration; block/file scope; internal/external/no linkage; and storage-class specifiers.

- an ordinary block local has automatic storage duration;
- a block `static` object retains its value for the program's execution but keeps block scope;
- a file-scope object has static storage duration;
- file-scope `static` gives a name internal linkage;
- `extern` commonly declares a name defined elsewhere;
- allocated storage lasts from successful allocation until deallocation.

In this C17 practice mode, `auto` declares automatic block storage; it is not C++-style type inference. `register` is a storage-class hint, not a promise of hardware placement, and taking that object’s address violates a constraint. A visible prior file-static declaration can make a later `extern` declaration inherit internal linkage. C11/C17 also have thread storage duration; threading is adjacent context, not a new numbered CLA objective. Scope is where a name is visible; linkage determines whether declarations denote the same entity; storage duration is how long storage exists; lifetime is when the object exists. Do not collapse these into “global versus local.”

## 2. Expressions, pointers, and storage — 38%

### Expressions and conversions

For arithmetic, relational, logical, bitwise, assignment, increment, conditional, and comma expressions, determine operand types first, then promotions/usual conversions, grouping, evaluation requirements, result type, and side effects. Precedence is not execution order. `&&`, `||`, conditional `?:`, and the comma operator impose specific sequencing; many other operand evaluation orders are not fixed.

Use unsigned types deliberately for modular arithmetic and bit masks. Mixed signed/unsigned comparisons can convert a negative signed value to a large unsigned value. Floating-point values are approximations. Casts communicate intended conversions but cannot establish that a value fits or that pointer lifetime is valid. Signed overflow is undefined; unsigned arithmetic is modular after applicable promotions. A finite floating-to-integer cast truncates toward zero only when the integral result is representable. Casting after `7 / 2` cannot recover the lost fraction. The safe-addition check follows [SEI INT32-C](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/integers-int/int32-c).

Under [SEI EXP30-C](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/expressions-exp/exp30-c), separate conflicting scalar side effects into full expressions. The comma operator sequences its operands; commas separating function arguments do not. Unspecified argument order is not automatically undefined, but unsequenced conflicting access to the same scalar can be. The workbook runs only defined cases.

### Pointer model and arithmetic

A pointer value can designate an object/function, be null, or hold another value with strict rules on use. `&x` takes an address; `*p` designates the object only while `p` is valid. Pointer arithmetic is defined within a single array object and its one-past value. Subtracting two pointers is meaningful only within that relationship. One-past may participate in valid traversal/comparison but may not be dereferenced. Forming a pointer farther outside the array can already be undefined; checking it afterward is too late. Subtraction also requires a representable ptrdiff_t result. In `int grid[2][3]`, `grid[0][3]` does not become valid because the next row is adjacent. Use `int (*row)[3]` for a pointer to a row; `int *pointers[2]` is an array of pointers. See [SEI ARR30-C](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/arrays-arr/arr30-c).

Array expressions frequently convert to pointers to their first elements, but exceptions such as `sizeof array` preserve array identity. A function parameter written as `int values[10]` is adjusted to `int *values`; it does not carry length ten. Pass lengths explicitly and prove all bounds. sizeof a fixed array measures the array, while sizeof an adjusted parameter measures a pointer. The usual unevaluated-operand explanation of sizeof needs a variable-length-array qualification; these examples deliberately use fixed sizes.

`void *` can carry an object pointer through generic interfaces, but type information and size are then external responsibilities. A pointer to freed or ended storage dangles. Setting one alias to null does not repair other aliases.

### Memory layout, allocation, and duration

Objects can contain padding, and alignment restricts valid addresses. Do not serialize a structure by assuming a portable raw byte layout. Character-type access has special object-representation uses, but interpreting arbitrary bytes as another incompatible type can violate aliasing, alignment, or lifetime requirements.

Use overflow-aware allocation sizing and an ownership plan:

The complete `reading_bytes` and `store_reserve` functions below check sizes before multiplication and commit the pointer/capacity only after successful allocation. The declared type appears before its size is used. The previous fragment referred to `items` before declaring it; a negative compile check reproduced that diagnostic.

`malloc` storage begins indeterminate. `calloc` sets all bits to zero, which is not a universal guarantee of null-pointer or floating zero representations. For a **positive** requested size, failed realloc preserves the original allocation; successful realloc ends the old object’s lifetime even when the returned address looks unchanged. Do not compare or reuse old aliases after success. The example handles zero capacity without a zero-size allocation, initializes each element before incrementing count, and frees only the allocation base. `free(NULL)` is allowed. See [SEI MEM35-C](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/memory-management-mem/mem35-c) and [MEM30-C](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/memory-management-mem/mem30-c).

> **Related item:** AddressSanitizer, UndefinedBehaviorSanitizer, and leak detectors help expose mistakes, but absence of a diagnostic is not proof that undefined behavior cannot occur.

## 3. Control flow and functions — 25%

Trace `if`/`else`, `switch`, `while`, `do ... while`, and `for` with exact boundary values. `else` binds to the nearest unmatched `if`. `switch` falls through unless control transfers. `break` exits the nearest loop or switch; `continue` advances the nearest loop, including the update step of a `for`. `goto` transfers to a label within the same function but can obscure invariants and cleanup.

For every loop, state initial condition, invariant, progress, valid bounds, and termination. For nested loops, trace each counter independently and calculate the number of body executions.

### Functions and parameter behavior

A prototype provides parameter types for argument checks and conversions. In C17, `int task(void)` explicitly takes no arguments; a declaration `int task()` does not provide a parameter-type prototype. Arguments are passed by value. Pointer parameters let the callee affect pointed-to objects; there is no C reference parameter:

The complete `update_if_positive` below includes `<limits.h>`, rejects a null target or nonpositive delta, and checks `*target > INT_MAX - delta` before adding. Rejection leaves the target unchanged; a merely positive delta does not prevent signed overflow.

Distinguish changing `*target` from reseating the local pointer `target`. To change a caller's pointer, pass a pointer to that pointer. `const` on a pointer parameter can document whether pointee modification is allowed.

Function-local automatic objects end when the block exits, so returning their addresses dangles. A `static` local persists but creates shared state. Recursive functions require a base case and progress and consume finite execution resources.

> **Related item:** A good function contract states valid inputs, output/return meaning, ownership transfer, aliasing assumptions, and failure behavior—not just its types.

## 4. Preprocessor and stream I/O — 8%

### Directives and macros

`#include` processes another source file; `#define` creates object-like or function-like macros; `#undef` removes a macro; `#if`, `#ifdef`, `#ifndef`, `#elif`, and `#else` select preprocessing branches. Macro arguments are token substitutions, not typed function parameters, and can be evaluated more than once:

The language workbook defines both `SQUARE_BAD(x)` as `x * x` and `SQUARE_PAREN(x)` as `((x) * (x))`. For the side-effect-free argument `2 + 3`, they produce 11 and 25 respectively.

Even the parenthesized square macro is unsafe with an increment argument: its conflicting modifications are unsequenced. Parentheses repair grouping, not evaluation count. [SEI PRE31-C](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/preprocessor-pre/pre31-c) also warns about side effects that disappear when a macro omits evaluation, such as assertions disabled by NDEBUG. Not every repeated evaluation is unsequenced: a conditional expression can sequence operations while still doing more work than the caller intended. Prefer functions when type checking and single evaluation matter. Know expansion order well enough to predict nested macro results, but use macros narrowly.

### Files and formatted streams

`fopen` returns a `FILE *` or null. The mode determines read/write/append, text/binary, and update behavior. Always check open and I/O results, close successfully opened streams exactly once, and distinguish end-of-file from error where required.

`fprintf` writes formatted data; `fscanf` reads formatted data and returns successful assignments. Match formats and pointer destinations. `%d`, `%x`, `%o`, and `%s` have type and capacity requirements. For printf, `%d` takes int, `%x`/`%o` take unsigned int, `%s` takes a terminated string, and `%f` takes double after default promotions. For scanf-family input, `%lf` requires double*, `%f` float*, and `%x`/`%o` unsigned int*. With `char word[4]`, `%3s` reserves room for NUL; `%c` does not append it. Never use untrusted text as the format string.

An assignment count of zero is a matching failure; EOF means an input failure before the first conversion completes. Checking that count does **not** make out-of-range numeric conversion safe. The parser uses strtol/strtod, checks end pointers and ERANGE, then enforces its own finite-value limits; see [SEI ERR34-C](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/error-handling-err/err34-c).

Keep fgetc’s result in int until checking EOF, then inspect the stream indicator. These examples require UCHAR_MAX <= INT_MAX, enforced at compile time; [SEI FIO34-C](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/input-output-fio/fio34-c) explains the rarer equal-width complication. EOF is a result to handle after a read, not a prediction from `while (!feof(stream))`. A successful fgets call can still read an embedded NUL; [FIO37-C](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/input-output-fio/fio37-c) explains why subtracting one from strlen can underflow. The loader explicitly rejects NUL and overlong lines. [FIO42-C](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/input-output-fio/fio42-c) supports checking fclose as well as earlier operations.

The integrated loader below reads bounded lines, classifies parse errors separately from stream errors, and closes its owned file even after a failed load. It never uses an unrepresentable formatted numeric conversion as a validation test.

## Integrated scenarios

### Multi-file inventory library and record loader

**PRACTICAL DEPTH — executed original program.** Save the next five C blocks under their stated filenames in one directory. The application reads a fictional sensor file: one record per line, decimal ID 0..1000, whitespace, then a finite value in -1000..1000. IDs may have a sign/leading zeros; values use strtod syntax in the initial C locale, including decimal exponents and hexadecimal floating notation. Surrounding whitespace is accepted. Blank lines, embedded NUL, trailing non-whitespace, overlong lines, range errors and a seventeenth record fail. At most 127 data bytes precede each newline; a final line without newline is accepted.

The loader owns its allocated records, borrows streams passed to load_readings, and owns streams opened by load_path. A failed load preserves the caller’s existing store; success replaces it, including an empty-file success. The Store contract requires a uniquely owned allocation and valid count/capacity fields. Spare capacity is not initialized and must not be read. Copies of the Store do not create independent owners. The allocation-failure switch is a bounded test seam, not a claim of inducing real exhaustion.

#### reading.h

```c
#ifndef CLA_READING_H
#define CLA_READING_H

#include <stddef.h>
#include <stdio.h>

enum { READING_LIMIT = 16, LINE_CAPACITY = 128 };
struct Reading { unsigned id; double value; };
struct Store { struct Reading *items; size_t count, capacity; };
enum LoadStatus { LOAD_OK, LOAD_TEXT, LOAD_IO, LOAD_MEMORY, LOAD_LIMIT };

/* Callers supply live objects and preserve count <= capacity <= READING_LIMIT.
   Initialize a Store with {0}; clear it once when its ownership ends.
   Each nonnull items pointer is the unique owning allocation base. */
int reading_bytes(size_t count, size_t *bytes);
int store_reserve(struct Store *store, size_t capacity, int fail_allocation);
void store_clear(struct Store *store);
int update_if_positive(int *target, int delta);
int parse_reading(const char *text, struct Reading *out);
/* Borrow stream. On failure preserve out; on success replace its old contents.
   fail_allocation is an explicit test seam, not real memory exhaustion. */
enum LoadStatus load_readings(FILE *stream, struct Store *out, int fail_allocation);
/* Own the opened stream and commit only after a successful close. */
enum LoadStatus load_path(const char *path, struct Store *out);

#endif
```

#### reading.c

```c
#include "reading.h"
#include <ctype.h>
#include <errno.h>
#include <limits.h>
#include <math.h>
#include <stdint.h>
#include <stdlib.h>

_Static_assert(UCHAR_MAX <= INT_MAX, "This byte reader requires int to represent every unsigned char");

int reading_bytes(size_t count, size_t *bytes) {
    if (bytes == NULL || count == 0 || count > SIZE_MAX / sizeof(struct Reading))
        return 0;
    *bytes = count * sizeof(struct Reading);
    return 1;
}

int store_reserve(struct Store *store, size_t capacity, int fail_allocation) {
    if (capacity <= store->capacity) return 1;
    size_t bytes;
    if (capacity > READING_LIMIT || !reading_bytes(capacity, &bytes)) return 0;
    struct Reading *next = fail_allocation ? NULL : realloc(store->items, bytes);
    if (next == NULL) return 0;
    store->items = next;
    store->capacity = capacity;
    return 1;
}

void store_clear(struct Store *store) {
    free(store->items);
    *store = (struct Store){0};
}

int update_if_positive(int *target, int delta) {
    if (target == NULL || delta <= 0 || *target > INT_MAX - delta) return 0;
    *target += delta;
    return 1;
}

int parse_reading(const char *text, struct Reading *out) {
    if (text == NULL || out == NULL) return 0;
    char *end;
    errno = 0;
    long id = strtol(text, &end, 10);
    if (end == text || errno == ERANGE || id < 0 || id > 1000) return 0;
    if (!isspace((unsigned char)*end)) return 0;
    while (isspace((unsigned char)*end)) ++end;
    const char *start = end;
    errno = 0;
    double value = strtod(start, &end);
    if (end == start || errno == ERANGE || !isfinite(value) ||
        value < -1000.0 || value > 1000.0) return 0;
    while (isspace((unsigned char)*end)) ++end;
    if (*end != '\0') return 0;
    *out = (struct Reading){(unsigned)id, value};
    return 1;
}

enum LineStatus { LINE_OK, LINE_END, LINE_BAD, LINE_IO };

/* Fixed capacity, reject NUL/overlong lines and consume their remainder. */
static enum LineStatus read_line(FILE *stream, char text[LINE_CAPACITY]) {
    size_t used = 0;
    int bad = 0, any = 0, ch;
    while ((ch = fgetc(stream)) != EOF) {
        any = 1;
        if (ch == '\n') break;
        if (ch == 0) bad = 1;
        if (used < LINE_CAPACITY - 1) text[used++] = (char)ch;
        else bad = 1;
    }
    text[used] = '\0';
    if (ferror(stream)) return LINE_IO;
    if (!any) return LINE_END;
    return bad ? LINE_BAD : LINE_OK;
}

enum LoadStatus load_readings(FILE *stream, struct Store *out, int fail_allocation) {
    struct Store next = {0};
    enum LoadStatus status = LOAD_OK;
    char line[LINE_CAPACITY];
    for (;;) {
        enum LineStatus line_status = read_line(stream, line);
        if (line_status == LINE_END) break;
        if (line_status == LINE_IO) { status = LOAD_IO; goto fail; }
        struct Reading item;
        if (line_status == LINE_BAD || !parse_reading(line, &item)) {
            status = LOAD_TEXT; goto fail;
        }
        if (next.count == READING_LIMIT) { status = LOAD_LIMIT; goto fail; }
        if (next.count == next.capacity) {
            size_t capacity = next.capacity == 0 ? 2 : next.capacity * 2;
            if (!store_reserve(&next, capacity, fail_allocation)) {
                status = LOAD_MEMORY; goto fail;
            }
        }
        next.items[next.count++] = item;
    }
    store_clear(out);
    *out = next;
    return LOAD_OK;
fail:
    store_clear(&next);
    return status;
}

enum LoadStatus load_path(const char *path, struct Store *out) {
    FILE *stream = fopen(path, "r");
    if (stream == NULL) return LOAD_IO;
    struct Store next = {0};
    enum LoadStatus status = load_readings(stream, &next, 0);
    if (fclose(stream) != 0) status = LOAD_IO;
    if (status != LOAD_OK) { store_clear(&next); return status; }
    store_clear(out);
    *out = next;
    return LOAD_OK;
}
```

#### app.c

```c
#include "reading.h"

int main(int argc, char *argv[]) {
    struct Store store = {0};
    if (argc != 2) {
        fputs("Usage: readings INPUT_FILE\n", stderr);
        return 2;
    }
    enum LoadStatus status = load_path(argv[1], &store);
    if (status != LOAD_OK) {
        fprintf(stderr, "Load failed: %d\n", (int)status);
        return 1;
    }
    int failed = 0;
    for (size_t i = 0; i < store.count; ++i) {
        if (printf("%u %.2f\n", store.items[i].id, store.items[i].value) < 0) {
            failed = 1; break;
        }
    }
    if (fflush(stdout) == EOF) failed = 1;
    store_clear(&store);
    return failed;
}
```

#### checks.c

This complete driver checks allocation sizing, successful growth and preserved data on injected failure, signed-addition boundaries, parser output preservation, accepted/rejected syntax, line limits/NUL, empty/final-no-newline input, record limits and file-open/close success. Temporary named fixtures use exclusive creation and are removed after success; an existing learner file is not overwritten.

```c
#include "reading.h"
#include "reading.h"
#include <limits.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

static unsigned checks;
#define CHECK(condition) do { \
    ++checks; \
    if (!(condition)) { fprintf(stderr, "Check failed at line %d\n", __LINE__); exit(1); } \
} while (0)

static void load_case(const void *bytes, size_t length, enum LoadStatus expected,
                      size_t count, int fail_allocation) {
    FILE *stream = tmpfile();
    CHECK(stream != NULL);
    CHECK(fwrite(bytes, 1, length, stream) == length);
    CHECK(fseek(stream, 0, SEEK_SET) == 0);
    struct Store store = {0};
    CHECK(store_reserve(&store, 1, 0));
    store.items[0] = (struct Reading){9u, 7.0}; store.count = 1;
    CHECK(load_readings(stream, &store, fail_allocation) == expected);
    CHECK(store.count == count);
    if (expected != LOAD_OK) {
        CHECK(store.items[0].id == 9u && store.items[0].value == 7.0);
        CHECK(store.capacity == 1);
    } else if (count != 0) {
        CHECK(store.items[0].id == 1u && store.items[0].value == 2.5);
    }
    CHECK(fclose(stream) == 0);
    store_clear(&store);
    CHECK(store.items == NULL && store.count == 0 && store.capacity == 0);
}

int main(void) {
    size_t bytes = 17;
    CHECK(!reading_bytes(0, &bytes) && bytes == 17);
    CHECK(!reading_bytes(SIZE_MAX, &bytes) && bytes == 17);
    CHECK(!reading_bytes(1, NULL));
    CHECK(reading_bytes(3, &bytes) && bytes == 3 * sizeof(struct Reading));
    struct Store store = {0};
    CHECK(store_reserve(&store, 0, 1));
    CHECK(!store_reserve(&store, 2, 1) && store.items == NULL);
    CHECK(store_reserve(&store, 2, 0));
    store.items[0] = (struct Reading){8u, -2.5}; store.count = 1;
    CHECK(!store_reserve(&store, 4, 1));
    CHECK(store.capacity == 2 && store.count == 1 && store.items[0].value == -2.5);
    CHECK(!store_reserve(&store, SIZE_MAX, 0));
    CHECK(store_reserve(&store, 4, 0));
    CHECK(store.items[0].id == 8u && store.items[0].value == -2.5);
    CHECK(store_reserve(&store, 3, 1) && store.capacity == 4);
    store_clear(&store); store_clear(&store);
    CHECK(store.items == NULL && store.count == 0 && store.capacity == 0);

    int target = INT_MAX;
    CHECK(!update_if_positive(NULL, 1));
    CHECK(!update_if_positive(&target, 1) && target == INT_MAX);
    CHECK(!update_if_positive(&target, 0) && target == INT_MAX);
    CHECK(!update_if_positive(&target, -1) && target == INT_MAX);
    target = INT_MAX - 1;
    CHECK(update_if_positive(&target, 1) && target == INT_MAX);
    target = INT_MIN;
    CHECK(update_if_positive(&target, INT_MAX) && target == INT_MIN + INT_MAX);

    const char *bad[] = {"", " ", "1", "1x 2", "-1 2", "1001 2", "1 1001",
        "1 -1001", "1 nan", "1 inf", "1 1e9999", "1 1e-9999", "1 2 tail",
        "999999999999999999999999999999 2", "0x1 2", "1.0 2", "1 \t"};
    for (size_t i = 0; i < sizeof bad / sizeof *bad; ++i) {
        struct Reading item = {88u, 99.0};
        CHECK(!parse_reading(bad[i], &item));
        CHECK(item.id == 88u && item.value == 99.0);
    }
    struct Reading item = {0};
    CHECK(!parse_reading(NULL, &item)); CHECK(!parse_reading("1 2", NULL));
    CHECK(parse_reading(" \t+001 2.5 \r", &item) && item.id == 1u && item.value == 2.5);
    CHECK(parse_reading("1000 -1000", &item) && item.id == 1000u && item.value == -1000.0);
    CHECK(parse_reading("0 1e3", &item) && item.value == 1000.0);
    CHECK(parse_reading("1 0x1.4p+1", &item) && item.value == 2.5);

    load_case("", 0, LOAD_OK, 0, 0);
    load_case("1 2.5\n", 6, LOAD_OK, 1, 0);
    load_case("1 2.5", 5, LOAD_OK, 1, 0);
    load_case("1 2.5\r\n2 -3\n", 12, LOAD_OK, 2, 0);
    load_case("1 2.5\n", 6, LOAD_MEMORY, 1, 1);
    load_case("1 2.5\nwrong\n", 12, LOAD_TEXT, 1, 0);
    load_case("\n", 1, LOAD_TEXT, 1, 0);
    const char nul[] = {'1',' ','2','\0','x','\n'};
    load_case(nul, sizeof nul, LOAD_TEXT, 1, 0);
    char line[130]; memset(line, ' ', sizeof line);
    memcpy(line, "1 2.5", 5); line[127] = '\n';
    load_case(line, 128, LOAD_OK, 1, 0);
    line[127] = ' '; line[128] = '\n';
    load_case(line, 129, LOAD_TEXT, 1, 0);
    char many[17 * 6];
    for (size_t i = 0; i < 17; ++i) memcpy(many + i * 6, "1 2.5\n", 6);
    load_case(many, 16 * 6, LOAD_OK, 16, 0);
    load_case(many, sizeof many, LOAD_LIMIT, 1, 0);
    CHECK(load_path("/cla-example-missing-directory/input.txt", &store) == LOAD_IO);
    CHECK(store.items == NULL);
    /* Exclusive create: never overwrite an existing learner file. */
    FILE *fixture = fopen("cla-checks-input.tmp", "wx");
    CHECK(fixture != NULL);
    CHECK(fputs("1 2.5\n2 -3\n", fixture) >= 0);
    CHECK(fclose(fixture) == 0);
    CHECK(load_path("cla-checks-input.tmp", &store) == LOAD_OK);
    CHECK(store.count == 2 && store.items[1].id == 2u && store.items[1].value == -3.0);
    CHECK(remove("cla-checks-input.tmp") == 0);
    store_clear(&store);
    printf("%u loader checks passed\n", checks);
    return 0;
}
```

#### language.c

### Preprocessor portability build

The language workbook checks defined expression results, tentative definitions, inherited linkage, scope/static lifetime, array/row types, shallow structure copies, pointer parameters, bounded recursion, control transfers and representable formatted input. PRACTICE_LEVEL selects basic or extended wording; neither setting changes the exam scope. Stringizing is adjacent practice. The unsafe square macro receives only side-effect-free arguments.

```c
#include <limits.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifndef PRACTICE_LEVEL
#define PRACTICE_LEVEL 1
#endif
#if PRACTICE_LEVEL == 1
#define CONFIG_NAME "basic"
#elif PRACTICE_LEVEL == 2
#define CONFIG_NAME "extended"
#else
#error Unsupported practice level
#endif
#define SQUARE_BAD(x) x * x
#define SQUARE_PAREN(x) ((x) * (x))
#define LABEL_INNER(x) #x
#define LABEL(x) LABEL_INNER(x)
#define CLA_TRANSIENT 7
#undef CLA_TRANSIENT
#ifdef CLA_TRANSIENT
#error Undef did not remove the macro
#endif

static unsigned checks;
#define CHECK(condition) do { \
    ++checks; \
    if (!(condition)) { fprintf(stderr, "Check failed at line %d\n", __LINE__); exit(1); } \
} while (0)

int tentative;
int tentative;
static int private_value = 4;
extern int private_value; /* Inherits the preceding internal linkage. */
static int next_call(void) { static int calls; return ++calls; }
static int square(int value) { return value * value; } /* Only -100..100 here. */
static void reseat_local(int *p) { p = NULL; (void)p; }
static void reset_owner(int **p) { *p = NULL; }
static unsigned triangular(unsigned n) { return n == 0 ? 0 : n + triangular(n - 1); }

int main(void) {
    CHECK(__STDC_VERSION__ == 201710L);
    CHECK(tentative == 0 && private_value == 4);
    CHECK(next_call() == 1); CHECK(next_call() == 2);
    auto int local = 3;
    { int local = 8; CHECK(local == 8); }
    CHECK(local == 3);
    CHECK(sizeof(char) == 1 && CHAR_BIT >= 8);
    CHECK(sizeof 'A' == sizeof(int)); CHECK(sizeof "A" == 2);
    CHECK(7 / 2 == 3); CHECK(-7 / 2 == -3); CHECK(-7 % 2 == -1);
    CHECK((double)(7 / 2) == 3.0); CHECK((double)7 / 2 == 3.5);
    CHECK((int)-2.75 == -2); CHECK((unsigned)-1 == UINT_MAX);
    CHECK(UINT_MAX + 1u == 0u);
    CHECK(2 + 3 * 4 == 14); CHECK((2 + 3) * 4 == 20);
    unsigned mask = 5u;
    CHECK((mask & 1u) == 1u); CHECK((mask | 2u) == 7u);
    CHECK((mask ^ 1u) == 4u); CHECK((mask << 1) == 10u);
    int effects = 0;
    CHECK(!(0 && ++effects) && effects == 0);
    CHECK((1 || ++effects) && effects == 0);
    CHECK((1 ? 7 : ++effects) == 7 && effects == 0);
    int sequence = (++effects, effects + 3);
    CHECK(sequence == 4 && effects == 1);
    int value = 5;
    CHECK(sizeof(value++) == sizeof(int) && value == 5);
    int a[4] = {1, 2};
    CHECK(a[2] == 0 && a[3] == 0);
    CHECK(sizeof a / sizeof *a == 4);
    int *p = a;
    CHECK(p + 4 == a + 4); CHECK((a + 4) - a == (ptrdiff_t)4);
    CHECK(*(p + 1) == 2);
    int grid[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int (*row)[3] = grid;
    CHECK(row[1][2] == 6 && sizeof *row == 3 * sizeof(int));
    int *pointers[2] = {&a[0], &a[1]};
    CHECK(*pointers[1] == 2);
    struct Pair { int n; int *alias; } first = {2, &value}, second = first;
    second.n = 8; *second.alias = 7;
    CHECK(first.n == 2 && value == 7);
    reseat_local(p); CHECK(p == a);
    reset_owner(&p); CHECK(p == NULL);
    CHECK(triangular(5) == 15);
    int total = 0;
    for (int i = 0; i < 6; ++i) {
        if (i == 2) continue;
        if (i == 5) break;
        total += i;
    }
    CHECK(total == 8);
    int once = 0; do { ++once; } while (0); CHECK(once == 1);
    int choice = 2, route = 0;
    switch (choice) {
        case 2: route += 2; /* fall through */
        case 3: route += 3; break;
        default: route = -1;
    }
    CHECK(route == 5);
    CHECK(SQUARE_BAD(2 + 3) == 11);
    CHECK(SQUARE_PAREN(2 + 3) == 25);
    int input = 2;
    CHECK(square(++input) == 9 && input == 3);
    CHECK(strcmp(LABEL(PRACTICE_LEVEL), PRACTICE_LEVEL == 1 ? "1" : "2") == 0);
    char text[40];
    CHECK(snprintf(text, sizeof text, "%d %x %o %s", -12, 31u, 9u, "ok") == 12);
    CHECK(strcmp(text, "-12 1f 11 ok") == 0);
    unsigned hex = 0, octal = 0; double real = 0; char word[4] = {0};
    CHECK(sscanf("1f 11 2.5 cat", "%x %o %lf %3s", &hex, &octal, &real, word) == 4);
    CHECK(hex == 31u && octal == 9u && real == 2.5 && strcmp(word, "cat") == 0);
    int parsed = -1;
    CHECK(sscanf("12x", "%d", &parsed) == 1 && parsed == 12);
    CHECK(sscanf("x", "%d", &parsed) == 0 && parsed == 12);
    CHECK(sscanf("", "%d", &parsed) == EOF && parsed == 12);
    printf("%u language checks passed (%s)\n", checks, CONFIG_NAME);
    return 0;
}
```

### Build and observed results

With an existing GCC-compatible driver, compile `reading.c` together with either `app.c` or `checks.c`; compile `language.c` separately. Use C17 mode and `-Wall -Wextra -Wpedantic -Werror`. The following optional CMake file builds all three executables with those switches; it assumes GCC or Clang, not MSVC.

#### CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.16)
project(cla_practice C)
set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)
add_executable(checks checks.c reading.c)
add_executable(readings app.c reading.c)
add_executable(language language.c)
foreach(target checks readings language)
  target_compile_options(${target} PRIVATE -Wall -Wextra -Wpedantic -Werror)
endforeach()
# These warning switches are for the GCC/Clang builds used in this review.
```

The review submitted these exact files through [Compiler Explorer’s API](https://github.com/compiler-explorer/compiler-explorer/blob/main/docs/API.md), with no account or saved-code link. Hosted GCC 15.2 and Clang 20.1 each produced **181 loader checks passed** and **53 language checks passed (basic)**. GCC -O2 repeated the loader checks; the -O2/PRACTICE_LEVEL=2 language build passed with extended wording. Clang’s loader build also passed with AddressSanitizer/UndefinedBehaviorSanitizer enabled at compile and link time. Clean sanitizer output covers these executed paths, not arbitrary inputs or every platform.

Eleven final build/run receipts include successful application output (`1 2.50` and `2 -3.00`), malformed-file failure, missing-file failure and usage failure. For success/malformed-file runs, a small driver created a fixture in the remote execution directory and called the unchanged application body with explicit arguments; source files supplied to the build were not assumed to survive in the execution sandbox. The ordinary application entry point handled the missing-file/usage runs. Actual low-level read, output-flush and close failures were not induced; no debugger session or deliberately undefined runtime example was executed.

Six diagnostic checks separately rejected the old undeclared-items fragment, conflicting function declarations, a missing definition, duplicate external definitions across two source files, taking a register object’s address, and an unsupported preprocessing configuration. Diagnostic wording and stage reporting are toolchain-specific. A successful preprocessing-only request captured 457 lines with the extended branch selected and macro names expanded. These are compile/link failures, not predictable output claims for undefined programs.

The [GCC dialect reference](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/C-Dialect-Options.html) matters because GCC 15 defaults to GNU C23: select C17 explicitly for these exercises. Its [warning options](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Warning-Options.html) distinguish warning groups from full conformance checks. [Instrumentation options](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/Instrumentation-Options.html) describe runtime checks and caution that combining sanitizers with Werror can cause false-positive warning failures; this review’s final combination passed. No compiler flags establish that all possible executions are correct.

## Hands-on labs

These eight broader learner activities remain proposed; the bounded runs above support parts of them. Completing a test driver does not complete every debugging, platform or failure-injection exercise.

1. **Declarations/linkage:** build a header plus three source files; exercise `extern`, file-scope `static`, block `static`, and linker failure cases.
2. **Structure/array model:** initialize arrays of structures, copy records with and without pointer members, inspect `sizeof`, and explain padding without assuming a fixed layout.
3. **Expression workbook:** predict 30 conversion, signed/unsigned, precedence, short-circuit, bit-mask, and side-effect cases before compiling.
4. **Pointer boundary lab:** traverse arrays by index and pointer, mark one-past, compare/subtract valid pointers, and classify invalid cases without assuming a particular result from undefined execution.
5. **Allocator wrapper:** safely implement allocate/grow/free with overflow and failure handling. Verify the original allocation survives failed `realloc`.
6. **Control/function tracer:** implement a parser with nested decisions/loops, pointer outputs, recursion, and exact return contracts; test every branch.
7. **Macro explorer:** inspect preprocessed output for include guards, conditional branches, nested expansion, stringizing/token pasting if studied, and double evaluation.
8. **File mini-project:** finish the dynamic record loader and test modes, formatted conversions, EOF versus error, cleanup, and malformed lines.

## Original readiness checks

1. How does a declaration differ from a definition?
2. Where should shared declarations and external definitions normally live?
3. What does file-scope `static` change?
4. How do scope, linkage, storage duration, and lifetime differ?
5. What happens to remaining aggregate members after partial initialization where zero-initialization applies?
6. Why may a structure contain padding?
7. What does structure assignment do to a pointer member?
8. Why is precedence not an evaluation-order rule?
9. What risk appears in mixed signed/unsigned comparisons?
10. Where is pointer arithmetic defined?
11. May a one-past pointer be dereferenced?
12. Why does an array parameter not communicate its written bound?
13. When can a pointer dangle?
14. Why assign `realloc` to a temporary?
15. What must be checked before multiplying allocation dimensions?
16. How do `break` and `continue` differ?
17. What causes switch fallthrough?
18. How does C implement caller-visible mutation?
19. How would a function change a caller's pointer value?
20. Why is returning a local automatic object's address invalid?
21. What does a prototype enable?
22. What two properties make recursion terminate?
23. Why are macro parameters not function parameters?
24. Why is `SQUARE(i++)` unsafe even with parentheses?
25. What does `fopen` return on failure?
26. What does `fscanf`'s return value represent?
27. How should EOF and stream error be distinguished?
28. Why must `%s` input be bounded?
29. Which block deserves the most study by published weight?
30. What must you recheck before scheduling?

## Answer key

1. A declaration introduces a name/type; an object definition supplies storage and a function definition supplies a body. File-scope tentative definitions are a separate case: compatible repeats within one translation unit can lead to one zero-initialized definition.
2. Put shared types and prototypes in a guarded header and external definitions in source files. Include guards prevent repeated contents within each translation unit; they do not solve duplicate external definitions across source files.
3. For a file-scope object or function, static gives its name internal linkage. A block-static object instead has block scope, no linkage and static storage duration.
4. Scope controls visibility; linkage determines identity across declarations; storage duration classifies storage persistence; lifetime is the interval in which an object exists. A block-static variable shows why local visibility does not imply a short lifetime.
5. The omitted aggregate elements/members receive the appropriate zero initialization, including null pointer values. That value-level rule differs from assuming an arbitrary all-bits-zero buffer represents every type’s zero.
6. Alignment can require internal or trailing padding. Member sizes alone do not define a portable serialized layout; compare fields rather than treating padding as meaningful data.
7. Structure assignment copies the pointer value, preserving an alias to the same target. It does not duplicate ownership or allocate a deep copy; freeing through both copies would be wrong.
8. Precedence and associativity group operands. Sequencing rules determine permitted evaluation order; parentheses alone do not sequence conflicting side effects.
9. Usual arithmetic conversions can turn a negative signed value into a large unsigned value. Determine the promoted types and ranges before predicting the comparison; adding a cast is not automatically a fix.
10. Arithmetic must stay within one array and its one-past boundary. Even forming a farther pointer can be invalid; subtracting valid related pointers additionally requires a representable ptrdiff_t result.
11. No. One-past can mark traversal termination, but only positions designating actual elements can be dereferenced.
12. An array parameter adjusts to a pointer type, so its ordinary written bound is not a runtime length. Pass a length and honor the caller’s live-storage contract; sizeof that parameter measures a pointer.
13. A pointer becomes dangling when the referenced object’s lifetime ends, including free, successful realloc and automatic block exit. Nulling one owner does not repair other aliases.
14. For a positive requested size, failure returns null while preserving the old allocation. Update both pointer and capacity only after success; do not use a zero-size call as a portable free/reallocation shortcut.
15. Reject inappropriate zero counts and check count against SIZE_MAX divided by element size before multiplication. Use the actual element type, keep the result in size_t, and handle allocation failure before any access.
16. Break leaves the nearest loop or switch; continue advances the nearest loop to its continuation point. In a for loop that includes the update expression; a switch does not intercept continue.
17. Execution continues into the following case if no control transfer intervenes. A deliberate fallthrough must be distinguished from a missing break; the workbook observes the former.
18. Every argument is passed by value, including pointer values. A copied pointer can still designate the caller’s object, allowing mutation through a valid writable pointer.
19. Pass the address of the caller’s pointer and assign through the resulting pointer-to-pointer. Merely reseating the callee’s local pointer parameter changes only that local copy.
20. The automatic object no longer exists once its block ends. Return a value, write into caller-provided storage, or transfer a separately allocated object under an explicit ownership contract.
21. A prototype supplies parameter types for argument diagnostics and conversions, and the declaration supplies the return type. In the selected C17 mode, task(void) and a non-prototype task() declaration are different.
22. A reachable base case and progress toward it are necessary. Inputs must also be bounded so depth and arithmetic remain within available resources and representable values.
23. Macro arguments are tokens substituted during preprocessing; they have no parameter type or inherent single-evaluation guarantee. A typed function gives a different semantic contract.
24. In a square expansion, the two increments are unsequenced relative to each other, so the execution is undefined. Parenthesizing each occurrence fixes grouping but cannot repair that conflict.
25. A null pointer. Stop or choose an explicit recovery path before using the stream; the application reports an I/O status without treating missing input as an empty successful file.
26. The count of assignments completed, with EOF for input failure before the first conversion completes. A successful prefix is not whole-input validation, and checking the count does not make unrepresentable numeric conversions safe.
27. Attempt the read first, then distinguish feof from ferror when the read reports failure. Parse/matching failure is separate; check fclose too, and do not retry use of an already closed stream.
28. The width limits data characters while the destination still needs an extra terminator byte: %3s fits char[4]. A bounded token conversion is not necessarily a complete-line parser, and %c does not append NUL.
29. Data Operations has 38%, with 14 items, but every block remains required. Published weights and a normalized cumulative result do not establish equal item point values.
30. Recheck CLA-11-03 scope/status, language, timing, price, delivery and the actual appointment terms. Use the Pearson associate/professional retake policy; resolve the conflicting rescheduling copy with the current booking rules.

## Final readiness checklist

- [ ] I can build and diagnose a guarded multi-file C program.
- [ ] I explain declarations, definitions, storage classes, scope, linkage, duration, and lifetime separately.
- [ ] I trace conversions and side effects without confusing precedence with evaluation order.
- [ ] I prove pointer ranges, allocation sizes, ownership, and every cleanup path.
- [ ] I can trace all control constructs and design explicit function contracts.
- [ ] I can predict macro expansion and replace unsafe macros with typed functions where appropriate.
- [ ] I use formatted streams with matching types, bounded text, and checked results.
- [ ] I distinguish EOF, I/O failure, parse failure, and application validation.
- [ ] I completed the integrated projects under warnings and runtime diagnostics.
- [ ] I rechecked the live official page immediately before purchase.

## Places to learn

The public CE1 and CE2 landings each list 42 hours and seven hours/week: CE1 covers modules 0–5; CE2 covers functions/structures, files/streams and preprocessor/declarations. CE2 lists both historical CLA-11-02 and active CLA-11-03 alignment; course labeling does not reactivate an old exam. CE1 has inconsistent Basics/Intermediate wording and overbroad array/pointer shorthand; the language contracts above govern. No enrolled lessons or assessments were reviewed.

Microsoft’s index is organized around ANSI C89 plus Microsoft extensions, while cppreference is a community index with version labels. SEI’s development pages explicitly warn that examples may be incomplete or erroneous; selected snippets contain placeholder handling or flawed ownership/boundary logic. The guide’s code is original and independently exercised, not a copy of those snippets. Paid O’Reilly/Udemy contents were inaccessible and Cisco returned an application shell. Except for Edube’s public 42-hour listings, the times below are author planning estimates, not verified runtimes.

This is not a complete list, and it is not meant to be consumed in full. Pick one primary path, use references for specific gaps, and spend at least as much time building, testing, and debugging as watching. Reconcile third-party material with the current official syllabus.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official CLA page and syllabus](https://cppinstitute.org/cla) | Free canonical blueprint | 1–2 hours to map and recheck |
| [C++ Institute exam policies](https://cppinstitute.org/exam-policies) | Free official policy | 20–40 minutes before scheduling |
| [OpenEDG C Essentials Part 1](https://edube.org/study/ce1) | Free account; officially aligned prerequisite coverage | 42 hours listed; target weak areas |
| [OpenEDG C Essentials Part 2](https://edube.org/study/ce2) | Free account; officially aligned | 42 hours listed |
| [Cisco Networking Academy C Essentials 2](https://www.netacad.com/courses/c-essentials-2) | Free account; official partner delivery | Plan 35–45 hours; verify live listing |
| [SEI CERT C Coding Standard](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/) | Free authoritative secure-coding reference | 5–10 hours targeted by topic |
| [Microsoft C language reference](https://learn.microsoft.com/en-us/cpp/c-language/c-language-reference?view=msvc-170) | Free implementation documentation | 5–10 hours targeted reading |
| [cppreference C language and library](https://en.cppreference.com/w/c.html) | Free community reference | Ongoing; 5–10 hours targeted lookup |
| [O'Reilly Effective C](https://www.oreilly.com/library/view/effective-c/9781098144778/) | Subscription; current practice extends beyond blueprint | 12–18 hours selected chapters and exercises |
| [Udemy Advanced C Programming Course](https://www.udemy.com/course/advanced-c-programming-course/) | Paid marketplace course; verify syllabus fit | Select matching sections, 10–20 hours |

No exact current MeasureUp or Whizlabs CLA-11-03 practice product was verified. Use the provider-aligned course tests and original multi-file labs; reject practice content that does not identify its source and active exam version.
