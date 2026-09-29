---
exam_code: CLE-10-01
vendor_id: cpp-institute
official_blueprint: https://cppinstitute.org/cle
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# CLE-10-01 C Certified Entry-Level Programmer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, links, lifecycle, and exam-integrity compliance were checked September 29, 2026. This does not guarantee that every explanation is error-free or remains current. The [official CLE page and syllabus](https://cppinstitute.org/cle) are authoritative.

**CURRENT BLUEPRINT — current baseline:** CLE-10-01, active; eight-block syllabus last updated July 24, 2025<br>
**Upcoming blueprint change:** none announced on the official exam or certification-catalog pages when checked<br>
**VERIFY CURRENT — delivery snapshot:** 30 questions; 45-minute exam plus approximately 5 minutes for the NDA/tutorial; single-choice, multiple-choice, gap-fill, and drag-and-drop items; 70% cumulative passing score; TestNow; English<br>
**VERIFY CURRENT — purchase snapshot:** no prerequisite; USD 69 exam or USD 86 exam-plus-retake when checked<br>

The [dated deep-review record](../docs/research/2026-09-29-cle-10-01-deep-review.md) maps all **36 numbered objectives**. Canonical scope was compared manually after direct monitoring timed out; existing snapshots were retained. This review executed original programs remotely in C11 mode using Compiler Explorer GCC 14.2 and Clang 19.1. C11 is an author practice choice; the exam page does not prescribe a language-version switch. No local compiler was installed. Eight broader activities remain proposed.

## How to use this guide

CLE measures whether you can read, trace, and assemble small C programs. Do not prepare by memorizing isolated definitions. Before compiling an example, predict its output, changed objects, branch, loop count, pointer target, and allocation lifetime. Compile with a conforming compiler and strong warnings, then explain discrepancies.

Use one repeatable cycle:

1. map a topic to the eight-block objective table;
2. write or trace the smallest program that demonstrates it;
3. label every expression with its type and every object with its lifetime;
4. test normal, empty, boundary, and invalid input;
5. fix warnings and preserve the failing input as a regression case.

The syllabus uses some informal terminology—for example, “initiators” where C programmers normally say *initializers*, and “references” while describing addresses/pointers. Follow the published intent, but use precise C terminology in your explanations.

> **About related items:** A `Related item:` callout supplies adjacent, prerequisite, operational, or modern-practice context. It helps you understand the objective; it does not claim that the extra item appears verbatim in the exam blueprint.

## Weighted objective map

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| 1. Basic Concepts | 4 | 13.25% | Explain translation and write a minimal program with valid literals and output |
| 2. Data Types, Evaluations, and Basic I/O | 4 | 13.25% | Select types, trace conversions, and validate formatted input/output |
| 3. Arithmetic, Logical, and Bitwise Operators | 4 | 13.25% | Predict expression types/results using precedence and truth tables |
| 4. Decision-Making Statements | 4 | 13.25% | Trace nested conditions and switch fallthrough |
| 5. Loops | 5 | 16.50% | Prove initialization, progress, bounds, and termination |
| 6. Arrays, Pointers, and Memory Management | 5 | 16.50% | Draw storage and safely pair pointer operations and allocations |
| 7. String Manipulation | 2 | 7% | Manage null-terminated arrays within capacity |
| 8. Functions | 2 | 7% | Declare, define, invoke, parameterize, and return correctly |

Questions carry different point values; the official page states a 30-point maximum and normalizes the cumulative result. Its weights sum to 100%, but they do not establish equal points per item. The 36 numbered objectives are grouped 6/5/5/4/4/5/4/3 across the eight blocks. Treat every block as required.

**VERIFY CURRENT — lifecycle and delivery.** The [certification catalog](https://cppinstitute.org/certification-exams) describes lifetime credentials that retain the completed exam version; no replacement CLE code was announced on the examined pages. The CLE/CPE section of the [exam policies](https://cppinstitute.org/exam-policies) identifies TestNow proctoring and a seven-day failed-retake wait, with a new voucher potentially required. The associate/professional section has different delivery and retake rules. Current booking UI, availability and individual eligibility were not inspected.

## 1. Basic concepts — 13.25%

### Translation and program structure

A source file is preprocessing input. Preprocessing handles directives such as `#include`; compilation checks/translates a translation unit; linking resolves referenced definitions into a program. An IDE coordinates tools but is not the C language or compiler. Diagnose a syntax/type error, unresolved external, runtime fault, and wrong answer at their proper stages.

In a hosted program, `int main(void)` and `int main(int argc, char *argv[])` are standard forms. Returning zero indicates successful termination to the host; reaching the closing brace of the initial main call also returns zero. In the argument form, argc is nonnegative and argv[argc] is a null pointer. Only read argv[0] after checking argc > 0; its first character can be null when the program name is unavailable. Implementation-specific forms and freestanding startup are separate. The [WG14 C11 draft N1570](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf), clauses 5.1.2.2.1–3, supplies the portable contract. `puts` writes a string plus a newline; `printf` interprets a format string and corresponding arguments.

```c
#include <stdio.h>

int main(void) {
    int count = 3;
    printf("count = %d\n", count);
    return 0;
}
```

Lexical elements are tokens such as keywords, identifiers, constants, string literals, and punctuators. Syntax determines valid arrangement; semantics determines meaning. Portable code does not assume implementation choices that the standard leaves variable.

### Literals, variables, arithmetic, and numeral systems

Recognize character constants (`'A'`), string literals (`"A"`), decimal/octal/hexadecimal integer constants (`10`, `012`, `0xA`), floating and scientific notation (`2.5`, `2.5e3`). A leading zero can mean octal, so `010` is eight, not ten. Binary notation is essential for reasoning about bits, but do not assume every compiler mode accepts a particular binary-literal spelling unless the language version is known.

In C11, an ordinary character constant such as `'A'` has type int, while `"A"` is an array containing a character and a terminator. Do not import the C++ character-literal type rule. Decimal digit codes are consecutive; the numeric code for a letter is encoding-dependent.

An object declaration introduces a name and type; an object definition supplies storage. Initialization gives its first value; assignment replaces a stored value. Integer division truncates toward zero, including negative operands. For example, -7 / 2 is -3 and -7 % 2 is -1; when the quotient is representable, quotient times divisor plus remainder reproduces the dividend. Zero divisors and unrepresentable signed division are undefined, as is signed arithmetic overflow. Unsigned arithmetic is modular. A compiler accepting a program does not make every possible execution defined.

> **Related item:** Make the compiler language-version option and warning level explicit. A program accepted as a vendor extension may not be valid in the intended standard mode.

## 2. Data types, conversions, and basic I/O — 13.25%

The fundamental arithmetic families include integer and floating types. Modifiers such as `signed`, `unsigned`, `short`, and `long` alter applicable integer types. Derived types include arrays, pointers, and functions. Exact sizes are implementation-dependent; use `sizeof` and `<limits.h>` when capacity matters. sizeof(char) is 1 C byte, and CHAR_BIT reports bits per byte; a byte need not universally be eight bits. int supports at least -32767..32767, while long supports at least -2147483647..2147483647. Do not assume Windows and a remote Linux compiler give long the same size.

Usual arithmetic conversions determine a common type in mixed expressions. A cast such as `(double)total / count` makes a desired conversion explicit, but no cast validates range or repairs invalid input. Converting a finite floating value to an integer truncates toward zero; if the integral part is not representable, C11 makes the conversion undefined. Integer-to-unsigned conversion is modular; an unrepresentable integer-to-signed conversion is implementation-defined or can raise an implementation-defined signal. Cast before division when a fractional result is intended: `(double)7 / 2` is 3.5, while `(double)(7 / 2)` is already 3.0. See N1570 clauses 6.3.1.3–4. Constants can be expressed with `const` objects or macros, but they differ in type checking, scope, and preprocessing behavior.

For formatted I/O, the conversion specification must match the argument after applicable promotions. printf's `%f` consumes a double (a float argument is promoted); scanf's `%f` needs a float pointer and `%lf` a double pointer. `%ld`, `%lld` and `%zu` match long, long long and size_t respectively. `%s` output needs a valid terminated string. For input into `char word[4]`, `%3s` leaves one byte for the terminator; `%c` does not append a terminator and normally does not skip whitespace. See [Microsoft's scanf reference](https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/scanf-scanf-l-wscanf-wscanf-l?view=msvc-170) and N1570 clause 7.21.6.2. Microsoft-only `_l`, `%C`/`%S` and secure-CRT extensions are separate from portable C11.

scanf returns the count of assignments, zero on an early matching failure, or EOF if input fails before the first conversion completes. A successful numeric prefix does not validate the whole line: a known-safe input `12x` can assign 12 while leaving x. More seriously, a numeric result outside the receiving object's range makes formatted input undefined; checking the assignment count afterward does not repair it. The workbook demonstrates only representable numeric scanf-family inputs. See [SEI ERR34-C](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/error-handling-err/err34-c/) and [INT05-C](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/recommendations/integers-int/int05-c/). A platform-specific errno extension is not a portable guarantee.

**PRACTICAL DEPTH — bounded input.** The complete program below reads at most 63 data bytes, rejects embedded NUL or a longer line, and consumes a rejected line through its end. It accepts a final line without a newline. The decimal parser permits an optional sign and surrounding whitespace, requires a complete integer, checks strtol's range result and then applies the fictional 0..1000 quantity limit. A valid zero remains data. Its output argument changes only after success. The fgetc result stays int until the EOF check; character classification receives an unsigned-char value.

```c
#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

/* 1: complete line; 0: EOF before data; -1: rejected line/read error.
   The caller supplies capacity writable bytes. Rejected lines are consumed. */
int cle_read_line(FILE *input, char *buffer, size_t capacity) {
    if (input == NULL || buffer == NULL || capacity == 0) return -1;
    size_t used = 0;
    int ch, seen = 0, rejected = 0;
    while ((ch = fgetc(input)) != '\n' && ch != EOF) {
        seen = 1;
        if (ch == '\0' || used == capacity - 1) rejected = 1;
        else buffer[used++] = (char)ch;
    }
    buffer[used] = '\0';
    if (ferror(input) || rejected) return -1;
    return ch == EOF && !seen ? 0 : 1;
}

/* Decimal integer, optional sign and surrounding whitespace; output on success only. */
int cle_parse_long(const char *text, long low, long high, long *output) {
    if (text == NULL || output == NULL || low > high) return 0;
    char *end;
    errno = 0;
    long value = strtol(text, &end, 10);
    if (end == text || errno == ERANGE || value < low || value > high) return 0;
    while (isspace((unsigned char)*end)) ++end;
    if (*end != '\0') return 0;
    *output = value;
    return 1;
}

int main(void) {
    char line[64];
    long quantity;
    if (cle_read_line(stdin, line, sizeof line) != 1 ||
        !cle_parse_long(line, 0, 1000, &quantity)) {
        puts("Expected one decimal quantity in 0..1000");
        return 1;
    }
    printf("Quantity: %ld\n", quantity);
    return 0;
}
```

The reader's caller must supply the stated writable capacity; the parser needs a valid terminated string. This is bounded memory use, not a general binary-protocol parser. `12`, `+12`, and `0012` represent the same decimal value; `12x`, `1.5`, `1e2` and `0x10` are rejected by the whole-input contract. Use a fixed format string for output. A return/error branch must actually stop or recover; a documentation comment saying "handle error" is not executable handling.

> **Related item:** Input conversion and business validation are separate. Successfully reading `-2` as an integer does not make `-2` a valid quantity.

## 3. Operators — 13.25%

Know arithmetic, relational, equality, logical, bitwise, assignment, increment/decrement, conditional, and `sizeof` operators. The result of logical operators is int zero or one. sizeof yields size_t; for the fixed types used here its operand is not evaluated, but variable-length-array cases require care. Precedence and associativity group an expression; they do not generally specify the order in which C evaluates its operands. Conflicting unsequenced operations on one scalar object are undefined. Keep increments in separate full expressions when tracing. N1570 clause 6.5 distinguishes these rules.

Logical `&&`, `||`, and `!` work with zero/nonzero truth and short-circuit where specified. Bitwise `&`, `|`, `^`, `~`, `<<`, and `>>` operate on integer representations and do not replace logical operators. Avoid shifts by negative counts or counts outside the promoted type width, and use unsigned types when a bit-mask interpretation is intended.

Prefix increment changes and yields the new value; postfix changes the object but yields its prior value. Avoid packing several modifications of one object into a single expression. A truth table is useful for proving a compound condition or mask, but retain C's short-circuit evaluation when side effects or safety checks are involved.

### Rounding is an explicit objective

Objective 3.2 names rounding. Distinguish truncating conversion from [floor](https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/floor-floorf-floorl?view=msvc-170), [ceil](https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/ceil-ceilf-ceill?view=msvc-170) and [round](https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/round-roundf-roundl?view=msvc-170). These math functions return floating values; round chooses the nearest integer value with exact halfway cases away from zero, independently of the current rounding direction. They do not automatically make an out-of-range later integer cast safe.

| Input x | `(int)x`, when representable | `floor(x)` | `ceil(x)` | `round(x)` |
|---|---:|---:|---:|---:|
| 2.5 | 2 | 2.0 | 3.0 | 3.0 |
| -2.5 | -2 | -3.0 | -2.0 | -3.0 |
| -2.75 | -2 | -3.0 | -2.0 | -3.0 |

Include math.h. The remote GCC/Clang runs used `-std=c11 -Wall -Wextra -pedantic -lm`; math-library linking is a toolchain detail. Floating representation can place a decimal literal near a threshold, so the workbook uses small exact binary fractions. Microsoft C++ overloads, SSE settings and MS-specific long-double behavior are not added C requirements.

## 4. Decision-making — 13.25%

`if` chooses based on zero/nonzero. An `else` binds to the nearest unmatched `if`; braces make ownership explicit. An `if`/`else if` chain selects at most one path, whereas separate `if` statements can select several.

`switch` uses an integer-like controlling expression and constant case values. Execution starts at the matching label; without a terminating transfer, it falls through. `default` handles no match. It is not a range matcher, and duplicate case values are invalid.

When conditions combine `&&` and `||`, parenthesize business intent. Test exact boundaries, just below/above boundaries, and combinations that cause short-circuiting.

## 5. Loops — 16.50%

`while` tests before its body, `do ... while` runs its body before the first test, and `for` groups initialization, continuation, and update. For any loop, state:

- initial state;
- invariant preserved by each iteration;
- progress toward termination;
- exact valid range;
- behavior for empty input.

`break` exits the nearest loop or switch. `continue` begins the next iteration; in a `for`, the update expression still occurs before retesting. A nested loop multiplies iterations and each transfer applies only to the nearest relevant construct. Trace rather than guess off-by-one behavior.

> **Related item:** An invariant is a compact correctness argument. For a running sum, “`sum` equals the total of elements before index `i`” exposes skipped and double-counted elements.

## 6. Arrays, pointers, and memory — 16.50%

An array contains a fixed number of same-type elements. Indices begin at zero; C does not automatically bounds-check. A multidimensional array is an array whose elements are arrays, and its later dimensions matter when passing it to a function.

An array expression often converts to a pointer to its first element, but an array and pointer are not identical. `sizeof array` in its declaring scope can report the complete array size; after adjustment to a function parameter, the parameter is a pointer. `&object` obtains an address and unary `*` designates the pointed-to object. `NULL` is a null-pointer constant; never dereference it.

Pointer arithmetic must remain within one array or its one-past position; merely forming a farther pointer can already be undefined. Pointer subtraction requires the same array and a representable ptrdiff_t result. The one-past position cannot be dereferenced. In `int grid[2][3]`, each row has three elements: `grid[0][3]` is not a permitted way to access `grid[1][0]`, even if the storage is adjacent. Use the proper row/column bounds or a pointer to the row type. See [SEI ARR30-C](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/arrays-arr/arr30-c/) and N1570 clause 6.5.6. Sorting requires valid bounds and a correct compare/swap rule. Draw each pointer target and the range it may traverse.

`malloc` allocates storage with indeterminate initial contents and returns either suitable storage or null. Check size multiplication before calling it, initialize elements before reading them, and free each successful allocation once. This example rejects zero count rather than depending on implementation-defined zero-size allocation behavior. The count is fixed at eight; the size guard teaches the general calculation. See [SEI MEM35-C](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/memory-management-mem/mem35-c/) and N1570 clause 7.22.3.

```c
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    size_t count = 8;
    int *values;
    if (count == 0 || count > SIZE_MAX / sizeof *values) return 1;
    values = malloc(count * sizeof *values);
    if (values == NULL) return 1;
    long total = 0;
    for (size_t i = 0; i < count; ++i) {
        values[i] = (int)i;
        total += values[i];
    }
    free(values);
    values = NULL;
    printf("Total: %ld; owner reset: %d\n", total, values == NULL);
    return 0;
}
```

The program prints `Total: 28; owner reset: 1`. A leak leaves allocated storage unreleased after its ownership path is lost. A dangling pointer refers to ended storage; resetting one owner does not repair other aliases. Do not evaluate old aliases after free, including for a "still the same address" comparison. `free(NULL)` is harmless; freeing an interior address or freeing the same allocation twice is undefined. See [SEI MEM30-C](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/memory-management-mem/mem30-c/). The scenario checks inject a null allocation result without exhausting memory.

## 7. Strings — 7%

A C string is a character sequence terminated by `\0`, usually stored in an array. The terminator consumes capacity. `strlen` counts bytes before it; it does not include the terminator or necessarily count displayed Unicode characters. A missing terminator can make even a length query read outside live storage. `strcpy` and `strcat` require a destination large enough for the resulting text plus `\0`, and their source/destination overlap restrictions matter.

For `char text[8] = "cat"`, capacity is eight bytes and length is three; appending "s" needs five bytes including the terminator. Adding source/destination lengths without an overflow proof is insufficient. The worked append helper first bounds its destination scan, then compares the source length with remaining capacity by subtraction. Source and destination must be disjoint, valid strings. See [SEI STR31-C](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/characters-and-strings-str/str31-c/) and N1570 clauses 7.24.2.3 and 7.24.3.1.

String literals are arrays that must not be modified. ASCII is a widely used character encoding and the basic execution character set supports familiar characters, but portable code should not assume every character or locale uses an ASCII-only representation.

> **Related item:** Size-aware design begins before copying: carry destination capacity with every buffer and reject or truncate according to an explicit policy. A library call cannot infer an array's true capacity from a pointer.

## 8. Functions — 7%

A prototype provides a function's name, return type, and parameter types. In this C11 practice mode, `int work(void)` specifies no parameters, while a declaration `int work()` does not provide a parameter-type prototype. Do not treat those spellings as interchangeable across C versions. A definition supplies its body. Arguments are passed by value; a function changes a caller's object by receiving and dereferencing a pointer to it. Array parameters are adjusted to pointer parameters, so pass a length separately.

The function below permits at most 100 values, each in -1000..1000, so a long accumulator is sufficient even when int has only the minimum required range. The caller must still supply enough live elements. Zero count accepts a null input pointer because no pointer arithmetic or dereference occurs.

```c
#include <stddef.h>
#include <stdio.h>

/* Caller provides count live elements. Output changes only on success. */
int checked_sum(const int *values, size_t count, long *output) {
    if (output == NULL || count > 100 || (count != 0 && values == NULL)) return 0;
    long total = 0;
    for (size_t i = 0; i < count; ++i) {
        if (values[i] < -1000 || values[i] > 1000) return 0;
        total += values[i];
    }
    *output = total;
    return 1;
}
int main(void) {
    int values[] = {7, -2, 5};
    long total;
    if (!checked_sum(values, sizeof values / sizeof values[0], &total)) return 1;
    printf("Sum: %ld\n", total);
    return 0;
}
```

A non-`void` function must return an appropriate value on required paths. `void` states no returned value. Prefer small functions with clear ownership, input requirements, and error contracts.

## Executed core workbook

**PRACTICAL DEPTH — original traces.** Predict results before compiling this complete program. It passed **72 checks on both remote compilers**. The checks use defined inputs, small allocations and explicit bounds. They cover literals, representation limits, rounding, conversions, truth tables/masks, control flow, multidimensional arrays, value/pointer parameters, allocation lifetime, string capacity and representable formatted input. They do not promise that undefined code fails predictably.

```c
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static unsigned checks;
static void check(int condition, const char *label) {
    if (!condition) { fprintf(stderr, "Failed: %s\n", label); exit(EXIT_FAILURE); }
    ++checks;
}
static int by_value(int value) { value += 2; return value; }
static void by_pointer(int *value) { if (value != NULL) *value += 2; }
static long bounded_sum(const int *values, size_t count) {
    long total = 0;
    for (size_t i = 0; i < count; ++i) total += values[i];
    return total;
}
int main(int argc, char *argv[]) {
    check(argc >= 0 && argv[argc] == NULL, "hosted main sentinel");
    check(sizeof 'A' == sizeof(int), "ordinary character constant has int size");
    check(sizeof "A" == 2, "string literal includes terminator");
    check('9' - '0' == 9, "decimal digit codes are consecutive");
    check(010 == 8 && 0x10 == 16, "literal bases");
    check(2.5e2 == 250.0, "scientific notation");
    check(sizeof(char) == 1 && CHAR_BIT >= 8, "C byte and minimum bits");
    check(INT_MAX >= 32767 && LONG_MAX >= 2147483647L, "minimum integer ranges");
    check(7 / 2 == 3 && -7 / 2 == -3, "integer division truncates toward zero");
    check(-7 % 2 == -1 && 7 % -2 == 1, "remainder follows dividend");
    check((double)7 / 2 == 3.5, "conversion before division");
    check((double)(7 / 2) == 3.0, "conversion cannot recover discarded fraction");
    check((int)-2.75 == -2, "representable cast truncates");
    check(floor(-2.75) == -3.0 && floor(2.75) == 2.0, "floor direction");
    check(ceil(-2.75) == -2.0 && ceil(2.75) == 3.0, "ceil direction");
    check(round(-2.5) == -3.0 && round(2.5) == 3.0, "halfway away from zero");
    check(round(2.25) == 2.0 && round(-2.25) == -2.0, "nearest integer value");
    unsigned maximum = UINT_MAX;
    check(maximum + 1u == 0u, "unsigned arithmetic is modular");
    int negative = -1;
    check((unsigned)negative == UINT_MAX, "negative to unsigned conversion");
    check(2 + 3 * 4 == 14 && (2 + 3) * 4 == 20, "operator grouping");
    int counter = 4;
    int old = counter++;
    int fresh = ++counter;
    check(old == 4 && fresh == 6 && counter == 6, "separate increments");
    counter *= 2;
    check(counter == 12, "compound assignment");
    int calls = 0;
    int no_call = 0 && ++calls;
    check(no_call == 0 && calls == 0, "and short circuit");
    int yes = 7 || ++calls;
    check(yes == 1 && calls == 0, "or short circuit and normalized result");
    for (int a = 0; a <= 1; ++a) {
        for (int b = 0; b <= 1; ++b) {
            check((a && b) == a * b, "and truth table");
            check((a || b) == (a + b != 0), "or truth table");
        }
    }
    check((!0) == 1 && (!5) == 0, "logical not");
    unsigned flags = 5u;
    check((flags & 1u) != 0u && (flags & 2u) == 0u, "test masks");
    flags |= 2u;
    check(flags == 7u, "set mask");
    flags &= ~1u;
    check(flags == 6u, "clear mask");
    flags ^= 2u;
    check(flags == 4u, "toggle mask");
    check((1u << 3) == 8u && (8u >> 2) == 2u, "bounded unsigned shifts");
    unsigned left = 5u, right = 2u;
    check((left & right) == 0u && (left && right) == 1, "bitwise versus logical");
    check((0 ? 10 : 20) == 20, "conditional expression");
    int branch = 0;
    if (1) { if (0) branch = 1; else branch = 2; }
    check(branch == 2, "nested else ownership");
    int choice = 2;
    switch (choice) {
        case 1: branch = 11; break;
        case 2: branch = 22; break;
        default: branch = 99; break;
    }
    check(branch == 22, "switch selection");
    int visits = 0;
    while (visits < 0) ++visits;
    check(visits == 0, "while may run zero times");
    do { ++visits; } while (visits < 0);
    check(visits == 1, "do runs before test");
    int total = 0;
    for (int i = 0; i < 6; ++i) {
        if (i == 2) continue;
        if (i == 5) break;
        total += i;
    }
    check(total == 8, "continue still reaches for update");
    visits = 0;
    for (int row = 0; row < 2; ++row)
        for (int column = 0; column < 3; ++column) ++visits;
    check(visits == 6, "nested loop extent");
    int values[4] = {2, 4};
    check(values[2] == 0 && values[3] == 0, "remaining aggregate elements zero initialized");
    check(sizeof values / sizeof values[0] == 4, "array extent at declaration");
    int *pointer = values;
    check(pointer == &values[0] && *(pointer + 1) == 4, "element addressing");
    check((values + 4) - values == 4, "one-past subtraction without dereference");
    check(*(values + 4 - 1) == 0, "step back from one past");
    int grid[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int (*row_pointer)[3] = grid;
    check(row_pointer[1][2] == 6, "pointer to complete row");
    total = 0;
    for (size_t row = 0; row < 2; ++row)
        for (size_t column = 0; column < 3; ++column) total += grid[row][column];
    check(total == 21, "multidimensional bounds");
    int amount = 5;
    check(by_value(amount) == 7 && amount == 5, "parameter is a copy");
    by_pointer(&amount);
    check(amount == 7, "write through pointer");
    by_pointer(NULL);
    check(amount == 7, "explicit null pointer policy");
    check(bounded_sum(values, 4) == 6, "array plus explicit length");
    check(bounded_sum(NULL, 0) == 0, "empty count prevents any pointer use");
    size_t count = 4;
    int *allocated = malloc(count * sizeof *allocated);
    check(allocated != NULL, "small allocation succeeded in this run");
    for (size_t i = 0; i < count; ++i) allocated[i] = (int)i;
    check(bounded_sum(allocated, count) == 6, "initialize before reading allocation");
    free(allocated);
    allocated = NULL;
    check(allocated == NULL, "owner reset after release");
    free(allocated);
    char text[12] = "cat";
    check(strlen(text) == 3 && sizeof text == 12, "length versus capacity");
    check(text[3] == '\0', "terminator stored");
    char copy[12];
    check(strcpy(copy, text) == copy && strcmp(copy, "cat") == 0, "bounded copy result");
    check(strcat(copy, "s") == copy && strcmp(copy, "cats") == 0, "bounded append result");
    check(strlen(copy) == 4 && copy[4] == '\0', "append moves terminator");
    int parsed = 0;
    char suffix = '\0';
    check(sscanf("12x", "%d%c", &parsed, &suffix) == 2 && parsed == 12 && suffix == 'x', "known-safe prefix conversion");
    check(sscanf("word", "%d", &parsed) == 0 && parsed == 12, "matching failure preserves destination");
    check(sscanf("", "%d", &parsed) == EOF, "input failure before assignment");
    char small[4];
    check(sscanf("abcdef", "%3s", small) == 1 && strcmp(small, "abc") == 0, "text width leaves terminator space");
    float single = 0;
    double wider = 0;
    check(sscanf("1.5 2.5", "%f %lf", &single, &wider) == 2 && single == 1.5f && wider == 2.5, "distinct floating destination types");
    check(isspace((unsigned char)' ') != 0 && isspace((unsigned char)'x') == 0, "character classification contract");
    printf("%u core checks passed\n", checks);
    return 0;
}
```

## Integrated scenarios

All three programs are complete and include the shared input helpers so each can compile independently. Keep each program in its own source file. Prices, quantities and menu limits are fictional. The review ran their exact function bodies with an additional original driver that supplied temporary input/output streams inside the remote sandbox; **118 scenario checks passed on each compiler**. No account, local compiler installation or infrastructure lab was involved. See [Compiler Explorer's API documentation](https://github.com/compiler-explorer/compiler-explorer/blob/main/docs/API.md) for the execution interface used.

### Inventory calculator

Input is one decimal item count (0..8), followed by a quantity (0..1000) and unit price in cents (0..1000000) on separate lines for each item. The program consumes that request; it does not claim to validate unrelated later lines. Each product fits in long under C11's minimum range; a long long total safely holds the maximum eight billion cents. Zero items avoids allocation. Every post-allocation input failure releases the allocation and prints no successful total. `simulate_failure` is a testing seam that returns null; main passes zero for ordinary allocation.

```c
#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

/* 1: complete line; 0: EOF before data; -1: rejected line/read error.
   The caller supplies capacity writable bytes. Rejected lines are consumed. */
int cle_read_line(FILE *input, char *buffer, size_t capacity) {
    if (input == NULL || buffer == NULL || capacity == 0) return -1;
    size_t used = 0;
    int ch, seen = 0, rejected = 0;
    while ((ch = fgetc(input)) != '\n' && ch != EOF) {
        seen = 1;
        if (ch == '\0' || used == capacity - 1) rejected = 1;
        else buffer[used++] = (char)ch;
    }
    buffer[used] = '\0';
    if (ferror(input) || rejected) return -1;
    return ch == EOF && !seen ? 0 : 1;
}

/* Decimal integer, optional sign and surrounding whitespace; output on success only. */
int cle_parse_long(const char *text, long low, long high, long *output) {
    if (text == NULL || output == NULL || low > high) return 0;
    char *end;
    errno = 0;
    long value = strtol(text, &end, 10);
    if (end == text || errno == ERANGE || value < low || value > high) return 0;
    while (isspace((unsigned char)*end)) ++end;
    if (*end != '\0') return 0;
    *output = value;
    return 1;
}

/* Use cle_read_line and cle_parse_long from the input example above. */
#include <stdint.h>

long *inv_allocate(size_t count, int simulate_failure) {
    if (count == 0 || count > SIZE_MAX / sizeof(long) || simulate_failure) return NULL;
    return malloc(count * sizeof(long));
}
int inv_run(FILE *input, FILE *output, int simulate_failure) {
    char line[64];
    long requested;
    if (cle_read_line(input, line, sizeof line) != 1 ||
        !cle_parse_long(line, 0, 8, &requested)) {
        fputs("Invalid item count\n", output);
        return 1;
    }
    size_t count = (size_t)requested;
    if (count == 0) { fputs("Total cents: 0\n", output); return 0; }
    long *totals = inv_allocate(count, simulate_failure);
    if (totals == NULL) { fputs("Allocation unavailable\n", output); return 1; }
    long long total = 0;
    for (size_t i = 0; i < count; ++i) {
        long quantity, cents;
        if (cle_read_line(input, line, sizeof line) != 1 ||
            !cle_parse_long(line, 0, 1000, &quantity) ||
            cle_read_line(input, line, sizeof line) != 1 ||
            !cle_parse_long(line, 0, 1000000, &cents)) {
            free(totals);
            fputs("Invalid item\n", output);
            return 1;
        }
        totals[i] = quantity * cents;
        total += totals[i];
    }
    fprintf(output, "Total cents: %lld\n", total);
    free(totals);
    return 0;
}
int main(void) { return inv_run(stdin, stdout, 0); }
```

For lines `2`, `2`, `125`, `3`, `100`, the result is `Total cents: 550`. One thousand units at one million cents gives one billion cents; eight such items give eight billion. The harness checks those endpoints, malformed/empty/missing input, quantity/price limits, zero-item behavior and the injected allocation-failure branch. That injection verifies control flow; it does not induce actual system memory exhaustion.

### Text statistics

Read one line containing at most 63 non-NUL bytes. The word rule is a run of non-whitespace bytes under the default C locale, not linguistic segmentation. Copy into an 80-byte report only after the input bound is established, then append a suffix after proving remaining capacity. The helper rejects an unterminated destination within its declared capacity and preserves it when capacity is insufficient.

```c
#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

/* 1: complete line; 0: EOF before data; -1: rejected line/read error.
   The caller supplies capacity writable bytes. Rejected lines are consumed. */
int cle_read_line(FILE *input, char *buffer, size_t capacity) {
    if (input == NULL || buffer == NULL || capacity == 0) return -1;
    size_t used = 0;
    int ch, seen = 0, rejected = 0;
    while ((ch = fgetc(input)) != '\n' && ch != EOF) {
        seen = 1;
        if (ch == '\0' || used == capacity - 1) rejected = 1;
        else buffer[used++] = (char)ch;
    }
    buffer[used] = '\0';
    if (ferror(input) || rejected) return -1;
    return ch == EOF && !seen ? 0 : 1;
}

/* Decimal integer, optional sign and surrounding whitespace; output on success only. */
int cle_parse_long(const char *text, long low, long high, long *output) {
    if (text == NULL || output == NULL || low > high) return 0;
    char *end;
    errno = 0;
    long value = strtol(text, &end, 10);
    if (end == text || errno == ERANGE || value < low || value > high) return 0;
    while (isspace((unsigned char)*end)) ++end;
    if (*end != '\0') return 0;
    *output = value;
    return 1;
}

/* Use cle_read_line from the input example above. */
#include <string.h>

/* Destination capacity is real; source is a valid, disjoint C string. */
int text_append(char *destination, size_t capacity, const char *source) {
    if (destination == NULL || source == NULL || capacity == 0) return 0;
    size_t used = 0;
    while (used < capacity && destination[used] != '\0') ++used;
    if (used == capacity || strlen(source) > capacity - used - 1) return 0;
    strcat(destination, source);
    return 1;
}
size_t text_words(const char *text) {
    size_t words = 0;
    int inside = 0;
    for (size_t i = 0; text[i] != '\0'; ++i) {
        if (isspace((unsigned char)text[i])) inside = 0;
        else if (!inside) { ++words; inside = 1; }
    }
    return words;
}
int text_run(FILE *input, FILE *output) {
    char line[64], report[80];
    if (cle_read_line(input, line, sizeof line) != 1) {
        fputs("Expected a line of at most 63 bytes without NUL\n", output);
        return 1;
    }
    strcpy(report, line); /* At most 63 data bytes plus the terminator fit in 80. */
    if (!text_append(report, sizeof report, " | checked")) return 1;
    fprintf(output, "%zu bytes, %zu words\n%s\n", strlen(line), text_words(line), report);
    return 0;
}
int main(void) { return text_run(stdin, stdout); }
```

Input `red blue` prints `8 bytes, 2 words` and then `red blue | checked`. An accepted empty line has zero bytes/words; immediate EOF is a distinct failure. The harness covers a 63-byte line, 64-byte rejection, embedded NUL, EOF without a final newline, whitespace transitions, exact-fit append and unchanged destination on rejection. Source strings must still be terminated and disjoint; the helper does not discover arbitrary pointer validity.

### Menu and sorter

Each command is one exact lowercase letter on its own line: `a` adds the next line's integer (-1000..1000), `p` prints, `s` sorts, and `q` quits. At most eight values are stored. EOF between commands exits normally; missing data after `a`, invalid commands and a ninth insertion fail visibly. In insertion sort, elements before i are sorted; the inner loop shifts larger elements right and stops before j would underflow. The left side of `&&` protects the `j - 1` access.

```c
#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

/* 1: complete line; 0: EOF before data; -1: rejected line/read error.
   The caller supplies capacity writable bytes. Rejected lines are consumed. */
int cle_read_line(FILE *input, char *buffer, size_t capacity) {
    if (input == NULL || buffer == NULL || capacity == 0) return -1;
    size_t used = 0;
    int ch, seen = 0, rejected = 0;
    while ((ch = fgetc(input)) != '\n' && ch != EOF) {
        seen = 1;
        if (ch == '\0' || used == capacity - 1) rejected = 1;
        else buffer[used++] = (char)ch;
    }
    buffer[used] = '\0';
    if (ferror(input) || rejected) return -1;
    return ch == EOF && !seen ? 0 : 1;
}

/* Decimal integer, optional sign and surrounding whitespace; output on success only. */
int cle_parse_long(const char *text, long low, long high, long *output) {
    if (text == NULL || output == NULL || low > high) return 0;
    char *end;
    errno = 0;
    long value = strtol(text, &end, 10);
    if (end == text || errno == ERANGE || value < low || value > high) return 0;
    while (isspace((unsigned char)*end)) ++end;
    if (*end != '\0') return 0;
    *output = value;
    return 1;
}

/* Use cle_read_line and cle_parse_long from the input example above. */

/* The caller supplies count live long elements; count zero uses no element. */
void menu_sort(long *values, size_t count) {
    for (size_t i = 1; i < count; ++i) {
        long key = values[i];
        size_t j = i;
        while (j > 0 && values[j - 1] > key) {
            values[j] = values[j - 1];
            --j;
        }
        values[j] = key;
    }
}
int menu_run(FILE *input, FILE *output) {
    long values[8];
    size_t count = 0;
    char line[64];
    int done = 0;
    do {
        int status = cle_read_line(input, line, sizeof line);
        if (status == 0) break;
        if (status != 1 || line[0] == '\0' || line[1] != '\0') {
            fputs("Use one command: a, p, s, q\n", output); return 1;
        }
        switch (line[0]) {
            case 'a':
                if (count == 8) { fputs("Full\n", output); return 1; }
                if (cle_read_line(input, line, sizeof line) != 1 ||
                    !cle_parse_long(line, -1000, 1000, &values[count])) {
                    fputs("Invalid value\n", output); return 1;
                }
                ++count;
                break;
            case 'p':
                fputs("Values:", output);
                for (size_t i = 0; i < count; ++i) fprintf(output, " %ld", values[i]);
                fputc('\n', output);
                break;
            case 's': menu_sort(values, count); break;
            case 'q': done = 1; break;
            default: fputs("Unknown command\n", output); return 1;
        }
    } while (!done);
    return 0;
}
int main(void) { return menu_run(stdin, stdout); }
```

Adding 3, -2 and 3, then sorting/printing yields `Values: -2 3 3`. The harness checks reverse/already-sorted/duplicate data against complete expected sequences, plus empty/singleton input, endpoint values, invalid commands, EOF and full capacity. It never evaluates an out-of-bounds pointer or index. Warnings were resolved before the final runs; no sanitizer or interactive debugger session is claimed.

## Hands-on labs

These eight learner activities remain proposed. The executed programs and bounded checks above support parts of them; they are not evidence that every activity or tool exercise was completed.

1. **Translation laboratory:** classify one preprocessing, compilation, linking, runtime, and logic defect; safely reproduce diagnostic or explicit error paths without executing undefined behavior.
2. **Representation table:** convert small values among binary, octal, decimal, and hexadecimal; verify masks and shifts using unsigned values.
3. **Types and I/O:** build a table of literal/type/`sizeof` observations; test matching and deliberately mismatched format reasoning without deploying undefined behavior.
4. **Operator tracer:** predict 25 expressions covering precedence, conversions, short-circuiting, bitwise operators, and prefix/postfix increments.
5. **Control-flow matrix:** implement boundary classification, a switch menu, and all three loop forms; trace `break` and `continue` in nested loops.
6. **Array/pointer map:** traverse one- and two-dimensional arrays by index and pointer; draw valid ranges and one-past positions.
7. **Allocation harness:** allocate, initialize, resize by allocate-copy-free, and release a sequence. Run an address/leak sanitizer where available.
8. **String/function mini-app:** build the text-statistics scenario with capacity checks, separate functions, invalid-input cases, and regression tests.

## Original readiness checks

1. How do preprocessing, compilation, and linking differ?
2. What is the difference between syntax and semantics?
3. Why can an IDE not define whether a construct is standard C?
4. How do `'A'` and `"A"` differ?
5. What values do `010` and `0x10` represent?
6. How do declaration, definition, initialization, and assignment differ?
7. Why are exact fundamental-type sizes not universally fixed?
8. What result does integer `7 / 2` produce?
9. Why does a cast not validate input?
10. Why must a `scanf` destination usually use `&`?
11. What does `scanf` return?
12. Why must format specifiers match argument types?
13. How do `&&` and `&` differ?
14. When is the right operand of `||` skipped?
15. How do prefix and postfix increment differ?
16. Which `else` owns an unbraced nested `if`?
17. What causes switch fallthrough?
18. How do `while` and `do ... while` differ?
19. What happens after `continue` in a `for` loop?
20. What five facts should you prove for every loop?
21. What is the last valid index of a five-element array?
22. Why is an array not identical to a pointer?
23. What may a one-past pointer be used for?
24. What must happen after `malloc` returns null?
25. Define leak, dangling pointer, and double-free.
26. What terminates a C string?
27. Does `strlen` count that terminator?
28. What capacity must `strcat`'s destination have?
29. How does a function modify a caller's object in C?
30. What must you verify on the official page before buying?

## Answer key

1. Directives are expanded, translation units are checked/translated, and definitions are resolved into a program.
2. Syntax is valid arrangement; semantics is meaning.
3. It coordinates tools; the selected compiler and language mode determine acceptance.
4. An ordinary C11 character constant has type int. A string literal is an array containing its characters plus the null terminator; it must not be modified.
5. Eight and sixteen.
6. For objects: a declaration introduces the name/type; a definition supplies storage; initialization establishes the initial value; later assignment changes a stored value. A declaration may also be a definition.
7. The implementation chooses within language minimums. sizeof(char) is one C byte; CHAR_BIT gives its bit count. int and long need not have the same size on every target.
8. 3. C11 integer division truncates toward zero, so -7 / 2 is -3 as well; do not describe it as always rounding down.
9. A cast requests a conversion. It does not check a business contract; a floating-to-integer conversion outside the representable integral range is undefined in C11.
10. The function needs the object's address so it can store the converted result.
11. The assignment count, zero for an early matching failure, or EOF if input fails before the first conversion completes. A successful prefix and numeric overflow require separate reasoning.
12. The conversion and promoted argument/pointer type must match. For example, printf %f uses double, scanf %f uses float*, and scanf %lf uses double*. A mismatch can make behavior undefined.
13. Logical && normalizes truth to int 0/1 and may skip its right operand. Bitwise & combines integer representation bits and evaluates both operands; that does not specify their relative order.
14. When the left operand is already nonzero/true.
15. Both change the object; prefix yields the new value and postfix the previous value.
16. The nearest unmatched `if`.
17. Reaching the end of a case without a transfer such as `break` or `return`.
18. The former may run zero times; the latter runs its body at least once.
19. The update expression occurs before the next condition test.
20. Initial state, invariant, progress, bounds, and termination/empty behavior.
21. Four.
22. An array provides element storage and retains its array type in contexts such as sizeof. Many array expressions convert to a first-element pointer, and array parameters adjust to pointer parameters; carry the count separately.
23. Compare/order it within the relevant array, subtract compatible same-array pointers when the result fits ptrdiff_t, or step back into the array. Do not dereference it or form a farther pointer.
24. Take an actual failure branch before arithmetic or access through that pointer. Also guard size multiplication before allocation and define how zero count is handled.
25. A leak leaves allocated storage unreleased after losing its ownership path; a dangling pointer refers to ended storage; a double-free releases one allocation twice. Resetting one owner does not repair aliases.
26. A zero-valued null character, which occupies capacity. An array without a terminator is not automatically a C string.
27. No; strlen counts preceding bytes, not capacity or necessarily displayed characters. It requires a valid terminated string.
28. Enough for existing bytes, appended bytes and one terminator, with nonoverlapping valid strings. Use an overflow-safe capacity proof before strcat.
29. Pass a pointer by value and write through it while the pointed-to object is live. Reassigning the local pointer alone does not change the caller’s pointer binding.
30. Active version, syllabus, format, price, language, delivery, and policies.

## Final readiness checklist

- [ ] I trace types, conversions, rounding, operator grouping and output before compiling.
- [ ] I distinguish full-line validation from a numeric prefix and avoid undefined numeric input overflow.
- [ ] I distinguish language, compiler, linker, runtime, and IDE responsibilities.
- [ ] I validate formatted input and match every format specification to its argument.
- [ ] I prove every decision and loop boundary, including short-circuit and fallthrough.
- [ ] I distinguish arrays, pointers, addresses, valid ranges, and object lifetimes.
- [ ] I pair every successful allocation with exactly one release path.
- [ ] I manipulate null-terminated strings only with known capacity.
- [ ] I declare and define small functions with clear value/pointer parameters.
- [ ] I have completed the integrated scenarios without relying only on happy paths.
- [ ] I rechecked the live official page immediately before purchase.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick one primary path, add targeted references where they explain a difficult objective better, and spend at least as much time writing, tracing, testing, and debugging as watching. Reconcile third-party material with the current official syllabus.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official CLE page and syllabus](https://cppinstitute.org/cle) | Free canonical blueprint | 1–2 hours to map and recheck |
| [C++ Institute exam policies](https://cppinstitute.org/exam-policies) | Free official policy | 20–40 minutes before scheduling |
| [OpenEDG C Essentials Part 1](https://edube.org/study/ce1) | Free account; officially aligned | 42 hours listed |
| [Cisco Networking Academy C Essentials 1](https://www.netacad.com/courses/c-essentials-1) | Free account; only a 55-character application shell retrieved | 35–45 hours is an author estimate; provider duration unverified |
| [SEI CERT C Coding Standard](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/) | Free; development index and selected rules read; broader than exam | 3–6 hours is an author lookup estimate |
| [Microsoft C language reference](https://learn.microsoft.com/en-us/cpp/c-language/c-language-reference?view=msvc-170) | Free implementation reference; index describes a C89 base plus extensions | 4–8 hours is an author estimate; use pinned C11 primary clauses for differences |
| [cppreference C language](https://en.cppreference.com/w/c/language.html) | Free community index; linked technical chapters not reviewed here | 3–6 hours is an author lookup estimate |
| [O'Reilly Effective C](https://www.oreilly.com/library/view/effective-c/9781098144778/) | Subscription; HTTP403, current contents not reverified | 5–8 hours of selected foundational reading is an author estimate |
| [Udemy C Programming for Beginners](https://www.udemy.com/course/c-programming-for-beginners-/) | Paid marketplace; HTTP403, current contents not reverified | 15–25 selective hours is an author estimate |
| [freeCodeCamp C Programming Tutorial for Beginners](https://www.youtube.com/watch?v=KJgsSFOSQv0) | Free; 199-character title/shell, no transcript or playback review | Prior approximately 3h46m not reverified; add coding time |

No exact current MeasureUp or Whizlabs CLE-10-01 practice product was verified. Prefer official course assessments and original code exercises over practice products that do not name the active exam version.

**Source boundaries.** OpenEDG's full public landing lists 42 hours, suggested seven hours/week, English and six modules (0–5). Its Beginner/Basics versus Intermediate labels and shorthand equating arrays/pointers are inconsistent; the canonical syllabus and precise language rules govern this guide. Course lessons were not entered. SEI's development index warns that pages may be incomplete; selected rule examples contain placeholders or malformed/incomplete snippets. The original programs here do not copy those snippets or treat their error comments as working branches. In particular, the off-by-one illustration needs a nonzero-capacity contract, sizeof's unevaluated-operand shorthand has a VLA exception, and snprintf's displayed example is not a compilable general truncation check. Broader exploit histories, analyzer claims and library extensions are outside this review's teaching changes. No paid course interior, current booking, video transcript, sanitizer session or human review was completed.
