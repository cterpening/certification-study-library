---
exam_code: CLP-12-01
vendor_id: cpp-institute
official_blueprint: https://cppinstitute.org/clp
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# CLP-12-01 C Certified Professional Programmer Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Objective coverage, citations, links, lifecycle, and exam-integrity compliance were checked September 29, 2026. This does not guarantee that every explanation is error-free or remains current. The [official CLP page and syllabus](https://cppinstitute.org/clp) are authoritative.

**Current baseline:** CLP-12-01, active; 29 numbered objectives in eight public blocks (July 24, 2025 syllabus)<br>
**Upcoming blueprint change:** none announced on the official exam or certification-catalog pages when checked<br>
**Official delivery snapshot:** 55 single- and multiple-select questions; 65-minute exam plus approximately 10 minutes for the NDA/tutorial; 70% passing score on a normalized maximum of 1,000 points; Pearson VUE; English<br>
**Purchase snapshot:** no formal prerequisite; CLA or equivalent experience recommended; from USD 325 exam or USD 375 exam-plus-retake when checked<br>

## How to use this guide

CLP spans standard C, historical constructs, operating-system interfaces, concurrency, numeric behavior, sockets, and undefined behavior. It is not safe to study everything as one portable dialect. For every program, label the language version, hosted/freestanding assumption, operating system/API, compiler, and library.

Use this cycle:

1. map work to one of the eight official blocks;
2. state which rule belongs to ISO C and which belongs to POSIX, Win32, or another library;
3. predict observable behavior, failure, cleanup, and portability limits;
4. compile on at least two toolchains or operating-system environments where practical;
5. use warnings, sanitizers, race diagnostics, packet capture, and regression tests appropriately.

The blueprint explicitly emphasizes C11 and older history even though later standards now exist. Learn the tested baseline and identify later changes as related context; do not silently rewrite a C11 question according to C23. Similarly, POSIX calls such as `open` are not ISO C library calls.

> **About related items:** A `Related item:` callout supplies adjacent, prerequisite, operational, security, or modern-practice context. It helps you understand the objective; it does not claim that the extra item appears verbatim in the exam blueprint.

## Weighted objective map

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| 1. Applied Evolution of C | 8 | 14.5% | Compare language eras and recognize old/new constructs in declared modes |
| 2. Variadic Functions and Macros | 5 | 9% | Implement a disciplined variadic wrapper without type/count mismatches |
| 3. Low-Level I/O | 7 | 13% | Distinguish API/ABI and safely drive POSIX descriptor operations |
| 4. Memory and String Handling | 9 | 16% | Select allocation/copy/search/sort/text representations with explicit contracts |
| 5. Process and Thread Management | 5 | 9% | Compare models and build a race-free C11 thread exercise |
| 6. Numerical Types and Computations | 6 | 11% | Classify exceptional floating values and quantify precision loss |
| 7. Network Socket Programming | 7 | 13% | Build framed client/server exchanges with byte-order and partial-I/O handling |
| 8. Specialized Considerations | 8 | 14.5% | Reason about volatile, non-local jumps, sequencing, UB, and complex declarations |

The weights total 100% and the item counts total 55. The normalized score does not imply that exactly 39 ordinary questions must be correct: item weighting matters. The retained objective snapshot was manually compared with the complete public syllabus after the automated monitor timed out.

### Every numbered objective

| Block | Explicit coverage within the numbered section below |
|---|---|
| 1 — four objectives | 1.1 language history; 1.2 old versus modern constructs; 1.3 trigraphs, digraphs and declarations; 1.4 C11 keywords |
| 2 — three | 2.1 calling conventions and variadic arguments; 2.2 list macros/lifetimes; 2.3 variadic I/O |
| 3 — three | 3.1 POSIX/API/ABI/WinAPI; 3.2 descriptor I/O; 3.3 descriptor controls |
| 4 — four | 4.1 byte/string operations; 4.2 sorting/searching; 4.3 allocation; 4.4 wide/Unicode/internationalization |
| 5 — four | 5.1 processes/threads/history; 5.2 Unix/Windows models; 5.3 safety/environment; 5.4 C11 threads |
| 6 — three | 6.1 exceptional floating values; 6.2 precision; 6.3 external precision libraries |
| 7 — three | 7.1 endpoints/protocols; 7.2 client/server lifecycle; 7.3 byte order/framing |
| 8 — five | 8.1 qualifiers; 8.2 jumps; 8.3 saved environments; 8.4 sequencing/behavior classes; 8.5 declarations/callbacks/VLAs |

### Scheduling and resource boundaries

**VERIFY CURRENT:** The [official exam page](https://cppinstitute.org/clp) says there is no formal prerequisite. The issuer's [Credly badge criteria](https://www.credly.com/org/openedg/badge/clp-12-01-clp-c-certified-professional-programmer), visible in an indexed public result, list both CLA and CLP passes. These statements differ; this guide does not decide an individual candidate's eligibility. Confirm current credential and booking requirements before paying.

The [exam policies](https://cppinstitute.org/exam-policies) put CLP in the Pearson associate/professional group: a failed attempt has a 15-day retake wait, distinct from the seven-day TestNow rule for entry-level exams. The [Pearson scheduling page](https://cppinstitute.org/schedule-exam-pvue) explicitly includes CLP and describes test-center/OnVUE delivery. Public wording about rescheduling anytime before an appointment conflicts with a 24-hour window; use the actual appointment terms. No account, appointment, system test or paid course interior was inspected.

## 1. Applied evolution of C — 14.5%

### Standards and feature eras

Know why K&R-era/implicit declarations, ANSI C/C89, C99, and C11 differ. C89 standardized prototypes and a common portable base. C99 added or standardized major facilities including `//` comments, declarations mixed with statements, `inline`, `restrict`, variable-length arrays, designated initializers, and new headers/features. C11 added `_Alignof`/`_Alignas`, `_Generic`, atomics, a thread API, static assertions, and other library/language changes.

Feature availability depends on implementation and compilation mode. A conforming program can query version macros, but implementations can support features selectively. Obsolescent or removed constructs can remain accepted as extensions. Never equate “my compiler accepted it” with “portable in the stated version.”

Trigraphs historically encoded otherwise unavailable characters and were processed early; digraphs are alternate tokens. Recognize their effect and era. Do not introduce them into new code without a genuine constrained-environment reason.

`_Alignof(type)` queries an alignment requirement. `_Generic` chooses an association based on the type of a controlling expression and enables type-directed macros:

The original workbook below uses `KIND(x)` with `int` and `double` associations and verifies that `KIND(n++)` does not increment `n`. The controlling expression is not evaluated; the chosen expression still has normal evaluation rules. Keep associations valid and avoid depending on disputed qualifier/array edge cases.

> **Related item:** C23 changes and removes some historical features. Treat them as migration context; the published CLP outline remains explicitly anchored in history through C11.

### Reading old source under an explicit mode

In C11, `int f(void)` specifies no parameters; a declaration `int f()` does not specify their types/count. A prototype such as `int f(int)` allows checking. Old identifier-list definitions and implicit declarations must be classified by era, not normalized by whatever extensions a compiler accepts. C99 removed implicit `int` and implicit function declarations. The historical sequence `??=` spells `#` at the trigraph stage; `<:` and `:>` are bracket digraphs. Recognize them in old code without inserting them into new examples.

Use [GCC's dialect options](https://gcc.gnu.org/onlinedocs/gcc-15.2.0/gcc/C-Dialect-Options.html) with strict diagnostics. The observed matrix below includes accepted C89 prototypes, rejected C89 mixed declarations, accepted C99 mixed declarations, rejected C99 `_Generic`, and accepted C11 `_Generic`/bounded VLA programs. These are specific probes, not a conformance test suite. `_Alignas` requests alignment; `_Alignof` queries it. Feature-test macros and library availability still matter.

## 2. Variadic functions and macros — 9%

A variadic function has fixed parameters followed by `...`; the fixed contract must communicate how many optional arguments follow and their promoted types. Default argument promotions apply: for example, `float` is passed as `double`, and narrow integer types undergo integer promotions.

`va_list` plus `va_start`, `va_arg`, `va_copy`, and `va_end` manage traversal. Fetching a value with a type incompatible with what was passed, or reading beyond supplied arguments, is undefined behavior. Each initialized/copied list needs the correct `va_end` handling.

The complete `mean` and `format_twice` implementations in `language.c` below replace an incomplete fragment that omitted the declaration of `size_t`. They include the required headers, document promoted argument types, bound finite values, close every initialized list and test truncation. A count cannot detect an argument of the wrong type.

The caller must pass `double` values here; passing an `int` violates the unstated runtime type contract. `vprintf` consumes a `va_list` according to a format string. Buffer-writing variants require special care: `vsprintf` cannot know destination capacity, while size-bounded alternatives support a defensible capacity contract.

> **Related item:** Prefer a counted typed array or structure when you control both sides. Variadic APIs trade compile-time type information for convenience and must reconstruct the contract at runtime.

### Calling convention and list ownership

Do not implement variadic traversal by guessing stack addresses. In the [Microsoft x64 ABI](https://learn.microsoft.com/en-us/cpp/build/x64-calling-convention?view=msvc-170), the first four argument positions use registers, the caller reserves shadow space, and variadic floating arguments in those positions are also represented in general-purpose registers. That is an ABI example, not an ISO C rule or a description of every Unix target. C passes argument values; passing a pointer permits access to its pointee without making C a pass-by-reference language.

For C11 `va_start`, the last named parameter must satisfy the language constraints; `unsigned count` works for this workbook. A list passed to a consuming `v...` function cannot simply be reused. Copy before consumption with `va_copy`, then match each initialized list with `va_end`. `vprintf` formats to a stream and reports output failure; `vsprintf` has no capacity argument. `vsnprintf` reports the would-have-written length, excluding the terminator, or a negative error. A nonnegative result at least as large as capacity signals truncation. Neither capacity nor a format string repairs mismatched argument types. [SEI variadic contracts](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/recommendations/declarations-and-initialization-dcl/dcl10-c/)

## 3. Fundamentals of low-level I/O — 13%

An API defines source-level callable behavior. An ABI defines binary-level conventions such as calling, object layout, and symbol rules. POSIX specifies portable operating-system interfaces across conforming systems; Win32 is Microsoft's Windows API. ISO C streams (`FILE *`, `fopen`) are a different abstraction from POSIX integer file descriptors (`open`, `read`, `write`, `close`).

For POSIX descriptor I/O, check every result and account for interruption, short reads/writes, EOF, blocking mode, and cleanup:

The complete `descriptors.c` below checks failure before using a returned descriptor, loops over byte counts, reports errors and closes owned descriptors. Empty error-handler comments are not a recovery strategy.

`fcntl` performs descriptor controls such as flags and locking operations defined by the platform. `ioctl` is device/interface-specific control with request-dependent arguments. Neither is “just another read”; consult the exact platform documentation, and do not assume request values or structure layouts are portable.

Mixing buffered `FILE *` operations and descriptor operations on the same underlying open file description requires synchronization rules and careful ownership. Duplication and inheritance can create several descriptors referring to related state.

### Progress, ownership and platform differences

For a positive byte request, a successful `read` may be short; zero indicates EOF for an ordinary stream/file. A request for zero bytes returning zero does not establish EOF. Retry an interrupted read/write only when the call returned failure with `EINTR`; otherwise advance by the positive result. Keep requests within the implementation's limits. The workbook caps writes at 32 bytes and copies in two-byte chunks. Its injected EINTR/zero-progress/I/O-error cases are deterministic test seams, not signals or disk failures. [POSIX read](https://pubs.opengroup.org/onlinepubs/9799919799/functions/read.html), [Linux write](https://man7.org/linux/man-pages/man2/write.2.html)

The workbook follows [Linux close semantics](https://man7.org/linux/man-pages/man2/close.2.html): relinquish a descriptor once and do not retry a failed close, because the descriptor number may already have been released and reused. Linux's EINTR behavior differs from POSIX.1-2024's specified behavior; write a platform policy instead of copying a universal close-retry loop. Successful write/close does not establish durable storage.

`F_GETFL`/`F_SETFL` read/change status flags on the open file description; preserve existing flags when adding `O_NONBLOCK`. Descriptor flags such as close-on-exec are a different category. The pipe test observes would-block while a writer exists, then EOF after all writers close and data is drained. `ioctl(FIONREAD)` returns unread pipe bytes on the tested Linux host; it is not a universal ISO/POSIX operation. [Status flags](https://man7.org/linux/man-pages/man2/F_GETFL.2const.html), [Linux pipes](https://man7.org/linux/man-pages/man7/pipe.7.html)

## 4. Memory and string handling — 16%

### Allocation and byte operations

Choose automatic/static storage for bounded lifetimes and allocated storage when size/lifetime requires it. Check multiplication overflow before allocation. `realloc` can move or fail; preserve the original pointer through a temporary. Define exactly who owns a returned block and which function releases it.

`memcpy` requires non-overlapping valid ranges; `memmove` handles overlap. `memcmp` compares byte sequences, not necessarily semantic object values. `memset` sets bytes, which is not a universal typed-value initializer. String functions require valid null termination and adequate destinations.

### Sorting and searching

`qsort` and `bsearch` operate on untyped element bytes via a comparison function. The comparator must impose a consistent ordering and avoid arithmetic-overflow shortcuts:

Use `(x > y) - (x < y)` for an integer comparator after safely reading the pointed-to values. The complete workbook tests `INT_MIN`, `INT_MAX`, duplicates and a missing search key. Never substitute `x - y`, which can overflow.

`bsearch` requires an array sorted under the same comparison. Returned pointers designate elements in that array and share its lifetime.

### Wide characters and internationalization

Bytes, multibyte character sequences, wide characters, Unicode code points, and displayed grapheme clusters are different units. C's `<wchar.h>` and `<wctype.h>` operate in the active locale and implementation model; `wchar_t` is not universally a Unicode scalar value. Conversion functions carry state and can fail on invalid sequences.

> **Related item:** Unicode security and user-visible text require normalization, grapheme, locale, and protocol decisions beyond simply changing `char` to `wchar_t`.

### Choosing storage and a text contract

For this workbook, small fixed arrays make ownership and bounds visible. For an unbounded production collection, impose an application limit, check `count > SIZE_MAX / sizeof *items` before multiplying, allocate a positive size through a temporary pointer, and update the owner only after success. Every alias to an old allocation becomes invalid after successful `realloc`; do not inspect the old pointer to decide whether it moved. A pool can make allocation predictable but requires its own capacity/reuse policy. No real memory exhaustion is claimed here.

`strcpy` requires room for the terminator; `strncpy` is not a general truncating-string replacement because a full-width copy may be unterminated. `strlen` requires a string, while `memchr` can search a specified byte range that contains NUL. `qsort` is not promised stable; `bsearch` need not select the first equal element. Compare structure members semantically rather than relying on padding bytes.

The text exercise keeps its own `mbstate_t`. An incomplete `mbrtowc` result consumes the offered prefix into that state; feed only the remaining bytes next. After an encoding error, reset the state before a new conversion. The C-locale ASCII cases are separate from an optional `C.UTF-8` branch: the latter succeeded on the tested hosts, but that locale name is not portable. Changing the process locale while other threads use locale-sensitive operations requires coordination. Unicode normalization, grapheme boundaries and display width need separate rules.

## 5. Processes and threads — 9%

A process supplies an execution/address-space context; threads within a process share much state while retaining execution stacks and thread-local state. POSIX threads, Windows threads, and C11 `<threads.h>` expose different APIs and availability. Label which model a call belongs to.

C11 threads include concepts such as `thrd_t`, creation/join, mutexes, condition variables, and thread-specific storage when the implementation supports them. A data race on ordinary conflicting accesses yields undefined behavior. Mutexes protect invariants; atomics support particular indivisible operations and ordering, not automatic correctness of a multi-object protocol.

Thread-safe design considers shared mutable state, library functions with hidden/static state, lifetime across worker completion, error propagation, cancellation/termination, and environment effects. `volatile` is not a thread-synchronization primitive.

> **Related item:** A race detector observes particular executions. Combine it with a written happens-before/ownership argument and repeatable stress tests.

### State shared by threads

Historically, separate processes gave programs independently scheduled execution and resource contexts; threads enabled multiple execution flows within one process. Unix and Windows differ in process creation, handle inheritance, scheduling and APIs. The [Windows process/thread overview](https://learn.microsoft.com/en-us/windows/win32/procthread/processes-and-threads) distinguishes processes, threads, pools, jobs and fibers. Those objects are not interchangeable with C11 `thrd_t`, and this review did not execute Win32 or Unix process creation.

In the queue below, the mutex protects `head`, `used`, `data` and `done`; it also protects each wait predicate. Wait in a `while` loop and recheck after waking. [WG14 issue 0480, fixed in C17](https://open-std.org/JTC1/SC22/WG14/issues/c11c17/issue0480.html), clarifies that a condition wait can wake for an unspecified reason; a signal alone does not publish arbitrary unprotected data. The example uses mutex synchronization and joins the worker before reading its private totals or destroying synchronization objects. It does not claim to have forced a spurious wakeup.

A bare memory fence or `volatile` does not turn conflicting ordinary accesses into a correct atomic communication protocol. Even a resource described as compliant needs a complete ownership and synchronization argument. Thread-safe code must also consider locale, environment, static library buffers and resource lifetime. [SEI data-race guidance](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/rules/concurrency-con/con43-c/)

## 6. Numerical types and computations — 11%

IEEE 754 models common floating formats and exceptional values. Know NaN, positive/negative infinity, positive/negative zero, rounding, subnormal values, and why decimal fractions may not be exact in binary. Comparisons involving NaN do not behave like ordinary numbers; use classification functions such as `isnan` and `isfinite`.

Catastrophic cancellation loses significant digits when subtracting nearby values. Repeated accumulation magnifies error; rearrangement or compensated summation can help. Signed zero can affect certain functions and reciprocals. Floating environment support can expose rounding modes and exceptions but is implementation-sensitive.

Multiple-precision libraries provide integers or floating values beyond built-in limits. Their types, allocation, precision, rounding, and cleanup are library contracts—external libraries are not added to ISO C merely because C bindings exist.

### A bounded numerical comparison

The numeric workbook declares binary64 `double`, round-to-nearest and no fast-math. It accumulates `1e16, 1, -1e16`: naive accumulation produces 0 on the observed host; Neumaier compensation preserves 1. This illustrates lost low-order information during addition and subsequent cancellation, not a promise that compensation fixes every ill-conditioned or overflowing computation. Reordering operations can change results. Relative-error tests need special care near zero; choose tolerances from the problem rather than applying one magic epsilon everywhere.

For exact values, initialize every GMP object, then clear it when finished. `mpz_ui_pow_ui` computes 2^100 without a built-in integer overflow; `mpq` represents exact rational arithmetic. Assigning 2/20 requires canonicalization before arithmetic, while 1/5 is already canonical. The program checks 1/10 + 1/5 = 3/10 and reports the actual linked GMP version, observed as 6.3.0. [GMP initialization](https://gmplib.org/manual/Initializing-Integers), [integer powers](https://gmplib.org/manual/Integer-Exponentiation), [rational contracts](https://gmplib.org/manual/Rational-Number-Functions)

Arbitrary precision still uses memory and has library-specific failure rules; GMP initialization is not an allocation-status-returning ISO API. MPFR provides a different floating-point precision/rounding contract. Its header was unavailable in the hosted probe, so no MPFR numerical result is claimed.

## 7. Network socket programming — 13%

Sockets expose endpoints for communication through platform APIs. A typical TCP server creates a socket, binds, listens, accepts, exchanges data, and closes; a client creates, resolves/connects, exchanges, and closes. UDP has different connection/reliability semantics.

TCP is a byte stream: one send does not establish one receive-sized message. Define framing through fixed sizes, delimiters, or length prefixes, and loop for partial sends/receives. A zero return from a positive-length receive on a stream indicates peer shutdown; distinguish it from a zero-sized request or datagram. Negative results require platform-specific handling.

Network byte-order conversions (`htons`, `htonl`, `ntohs`, `ntohl`) address multi-byte integer endianness. Do not send a native C structure as a wire format: padding, width, alignment, endianness, and representation vary. Serialize fields explicitly and validate all lengths before allocating or indexing.

> **Related item:** Production network code also needs timeouts, address-family handling, resource limits, authentication/encryption, and hostile-input defenses. These extend rather than replace the blueprint's socket fundamentals.

### Separate transport setup from frame decoding

A [Linux socket](https://man7.org/linux/man-pages/man2/socket.2.html) has a domain, type and protocol. AF_UNIX is local communication; AF_INET/AF_INET6 select IP families. Stream, datagram and sequenced-packet semantics differ. For a [TCP service](https://man7.org/linux/man-pages/man7/tcp.7.html), the listening socket remains separate from each accepted connection; clients connect before ordinary exchange. A successful send reports local progress, not that the remote application processed a message.

The original decoder below uses a two-octet big-endian length and a fictional 32-byte maximum. It validates the header before reading into bounded temporary storage, then commits output only for a complete frame. An empty frame is valid and differs from EOF before a header. EOF after a partial header or body is truncation. A reversed 00 03 header becomes 03 00 (768), which the receiver rejects; the parser cannot guess the sender's intent.

The exercise uses [socketpair](https://pubs.opengroup.org/onlinepubs/9799919799/functions/socketpair.html) with local streams, one-byte receive requests, and adjacent frames sent together. It is not a TCP listener/client deployment or packet capture. With a positive requested length, stream `recv` zero denotes peer shutdown; zero-sized datagrams and zero-sized requests need different interpretation. [Receive results](https://man7.org/linux/man-pages/man2/recv.2.html)

## 8. Specialized considerations — 14.5%

`const` expresses a restriction on modification through a particular access path; it does not necessarily mean immutable storage. `volatile` tells the implementation that accesses are observable in ways it cannot infer, useful for certain hardware/signal contexts. It does not provide atomicity, ordering between threads, or a lock.

`setjmp` records an environment and `longjmp` performs a non-local transfer. Automatic non-volatile objects modified after `setjmp` can have indeterminate values after the jump under the language rules. Non-local transfer bypasses normal structured cleanup, so resource invariants need an explicit design.

Undefined behavior places no requirements on the implementation. Examples include out-of-bounds access, signed overflow, invalid shifts, use-after-free, incompatible variadic retrieval, and unsequenced conflicting side effects. Unspecified behavior permits one of several outcomes without documentation; implementation-defined behavior requires the implementation to document its choice. Do not use a single observed run to “prove” UB's result.

Read complex declarations from the identifier outward while respecting parentheses. A function pointer can hold a compatible function address and enables callbacks. Variable-length arrays use runtime sizes with scope/lifetime constraints and optional support in later language modes; check the intended standard and implementation.

### Declarations and jumps you can reason about

`const int *p` restricts modification through `p`; `int *const p` prevents reassignment of that pointer. Casting away `const` does not permit modification of an object originally defined const. `int (*callback)(int)` is a pointer to a function taking/returning int; `int *factory(int)` is a function returning an int pointer. Call only through compatible function types, and retain the lifetime of any callback context. An array `int (*table[3])(int)` holds three such function pointers.

In C11, a VLA's evaluated bound must be positive; bound its storage use and check implementation support before choosing it over an explicit allocation. A pointer to a VLA is not an owning resizable array. A structured `goto cleanup` can centralize release; jumping into a variably modified scope is constrained. Non-local jumps require a still-active target invocation in the same thread and a permitted `setjmp` context. The workbook uses `if (setjmp(env) == 0)`, not an initializer assignment, and keeps its changed local volatile. It neither jumps across owned resources nor calls a dead frame. [SEI MSC22-C](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/recommendations/miscellaneous-msc/msc22-c/)

For sequencing, the comma operator sequences its left expression before its right; a comma separating arguments does not. Split conflicting increments into statements. Undefined behavior has no required result; unspecified argument evaluation order need not be documented; implementation-defined plain-char signedness must be documented. Review invalid examples as text rather than running them to infer guarantees.

## Original executable workbook

These five independent programs are original teaching exercises. Save each block under its displayed filename. They use hosted C11; the descriptor and frame programs additionally require the demonstrated Linux interfaces, and `numbers.c` needs GMP. Read every declared bound before adapting them. The [C11 committee draft](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf) is a historical primary reference, not the final current standard or an exam-edition promise.

Build commands on an already suitable environment:

```sh
cc -std=c11 -Wall -Wextra -Wpedantic -Werror language.c -lm -o language
cc -std=c11 -Wall -Wextra -Wpedantic -Werror queue.c -pthread -o queue
cc -std=c11 -Wall -Wextra -Wpedantic -Werror numbers.c -lgmp -lm -o numbers
cc -std=c11 -Wall -Wextra -Wpedantic -Werror descriptors.c -o descriptors
cc -std=c11 -Wall -Wextra -Wpedantic -Werror frames.c -o frames
```

The review executed exact copies through [Compiler Explorer](https://github.com/compiler-explorer/compiler-explorer/blob/main/docs/API.md) with GCC 15.2 and Clang 20.1. Each compiler passed 31 language checks (including the optional UTF-8 branch), 11 descriptor checks and 69 framing checks. Each queue run processed ten batches of 1,000 items with sum 500,500; the numeric results matched both exact GMP checks. Three optimized variants and four Clang address/undefined sanitizer runs also passed: 17 successful workbook build/runs in total. Seven separate header/dialect probes produced the expected outcomes: four builds/runs and three diagnostic rejections.

ThreadSanitizer compiled the queue but terminated with a runtime SEGV. A minimal C11 create/join program reproduced the failure on both compilers. The cause remains unresolved; these runs are not clean race-detector evidence. No runtime or permission settings were changed. Sanitizer success on other runs covers tested paths only.

### language.c — Language, variadic and text contracts

The mean rejects invalid count/output before traversing arguments. For valid counts, callers must supply enough correctly promoted doubles; no runtime type introspection is available. Formatting assumes trusted formats without `%n` and distinct valid output buffers; truncation leaves a terminated prefix, not transactional output. No mismatched variadic call or invalid jump was executed.

```c
#include <errno.h>
#include <limits.h>
#include <locale.h>
#include <math.h>
#include <setjmp.h>
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <wchar.h>

static unsigned checks;
#define CHECK(e) do { ++checks; if (!(e)) { \
    fprintf(stderr, "check failed at %d: %s\n", __LINE__, #e); \
    exit(EXIT_FAILURE); } } while (0)
#define KIND(x) _Generic((x), int: "int", double: "double", default: "other")

/* Contract: out is writable; count promoted doubles actually follow.
   Count 1..8 and finite magnitudes <=1000 keep the sum bounded. */
static int mean(double *out, unsigned count, ...) {
    if (!out || count == 0 || count > 8) return 0;
    va_list ap;
    va_start(ap, count);
    double total = 0.0;
    for (unsigned i = 0; i < count; ++i) {
        double x = va_arg(ap, double);
        if (!isfinite(x) || fabs(x) > 1000.0) {
            va_end(ap);
            return 0;
        }
        total += x;
    }
    va_end(ap);
    *out = total / count;
    return 1;
}

/* Trusted, side-effect-free format (no %n); matching argument types.
   Distinct writable arrays of capacity a_cap and b_cap are required.
   Returns the required length, or -1 on error/truncation. */
static int format_twice(char *a, size_t a_cap, char *b, size_t b_cap,
                        const char *fmt, ...) {
    va_list ap, copy;
    va_start(ap, fmt);
    va_copy(copy, ap);
    int n = vsnprintf(a, a_cap, fmt, ap);
    int m = vsnprintf(b, b_cap, fmt, copy);
    va_end(copy);
    va_end(ap);
    if (n < 0 || m < 0 || n != m ||
        (size_t)n >= a_cap || (size_t)m >= b_cap) return -1;
    return n;
}

static int compare_int(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}

static void jump_check(void) {
    jmp_buf env;
    volatile int changed = 0;
    /* setjmp is the left operand of == with integer constant 0,
       and that comparison is the entire if controlling expression. */
    if (setjmp(env) == 0) {
        changed = 7;
        longjmp(env, 0); /* The resumed setjmp returns 1, never 0. */
    } else {
        CHECK(changed == 7);
    }
}

int main(void) {
    int n = 1;
    CHECK(strcmp(KIND(n++), "int") == 0 && n == 1);
    CHECK(strcmp(KIND(1.0), "double") == 0);
    CHECK(_Alignof(double) > 0);
    double out = 99.0;
    CHECK(mean(&out, 3u, 1.0, 2.0, 3.0) && out == 2.0);
    CHECK(mean(&out, 2u, (float)2.0, (float)4.0) && out == 3.0);
    CHECK(!mean(&out, 0u) && out == 3.0);
    CHECK(!mean(&out, 9u) && out == 3.0);
    CHECK(!mean(NULL, 1u, 1.0));
    CHECK(!mean(&out, 1u, INFINITY) && out == 3.0);
    CHECK(!mean(&out, 1u, NAN) && out == 3.0);
    CHECK(!mean(&out, 1u, 1001.0) && out == 3.0);
    CHECK(mean(&out, 8u, 1000.0, -1000.0, 0.0, 0.0,
               0.0, 0.0, 0.0, 0.0) && out == 0.0);
    char a[32], b[32];
    CHECK(format_twice(a, sizeof a, b, sizeof b, "%s:%d", "ok", 42) == 5);
    CHECK(strcmp(a, "ok:42") == 0 && strcmp(a, b) == 0);
    CHECK(format_twice(a, 3, b, sizeof b, "%s", "abcd") == -1);
    CHECK(strcmp(a, "ab") == 0 && strcmp(b, "abcd") == 0);
    char overlap[] = "abcdef";
    memmove(overlap + 1, overlap, 5);
    CHECK(strcmp(overlap, "aabcde") == 0);
    char separate[sizeof overlap];
    memcpy(separate, overlap, sizeof separate);
    CHECK(memcmp(separate, overlap, sizeof separate) == 0);
    int values[] = {INT_MAX, 0, INT_MIN, 7, 7};
    qsort(values, 5, sizeof *values, compare_int);
    CHECK(values[0] == INT_MIN && values[4] == INT_MAX);
    int key = 7;
    int *found = bsearch(&key, values, 5, sizeof *values, compare_int);
    CHECK(found && *found == 7); /* No promise which duplicate. */
    key = 8;
    CHECK(bsearch(&key, values, 5, sizeof *values, compare_int) == NULL);
    jump_check();
    CHECK(setlocale(LC_CTYPE, "C") != NULL);
    mbstate_t state = {0};
    wchar_t wc = 0;
    CHECK(mbrtowc(&wc, "A", 1, &state) == 1 && wc == L'A');
    CHECK(mbrtowc(&wc, "", 1, &state) == 0 && wc == L'\0');
    int utf8 = setlocale(LC_CTYPE, "C.UTF-8") != NULL;
    if (utf8) {
        state = (mbstate_t){0};
        CHECK(mbrtowc(&wc, "\xE2", 1, &state) == (size_t)-2);
        CHECK(mbrtowc(&wc, "\x82\xAC", 2, &state) == 2);
        CHECK(mbsinit(&state));
        state = (mbstate_t){0};
        errno = 0;
        CHECK(mbrtowc(&wc, "\xFF", 1, &state) == (size_t)-1 && errno == EILSEQ);
        state = (mbstate_t){0}; /* State after an encoding error is unspecified. */
        CHECK(mbrtowc(&wc, "B", 1, &state) == 1 && wc == L'B');
    }
    CHECK(setlocale(LC_CTYPE, "C") != NULL);
    printf("language: %u checks; UTF-8 branch=%d\n", checks, utf8);
    return EXIT_SUCCESS;
}
```

### queue.c — Bounded producer and consumer

Capacity is three; the producer sends 1..1000, and one worker consumes in FIFO order. Queue invariants hold under one mutex; worker-only totals become visible after join. Normal shutdown drains the queue. Initialization unwinds only initialized objects; the injected startup failure occurs before any worker exists. Unexpected synchronization failure aborts rather than returning through unsafe cleanup. The exercise does not guarantee scheduler fairness or inject real resource exhaustion.

```c
#include <stdio.h>
#include <stdlib.h>
#include <threads.h>

enum { CAP = 3, COUNT = 1000 };
typedef struct {
    mtx_t lock;
    cnd_t readable, writable;
    int data[CAP];
    unsigned head, used;
    int done;
    long sum;
    unsigned consumed;
} Queue;

/* A synchronization failure after startup is fatal. Returning through
   cleanup while a worker might still use these objects would be unsafe. */
static void must(int status) {
    if (status != thrd_success) {
        fputs("synchronization failed\n", stderr);
        abort();
    }
}

static int consume(void *arg) {
    Queue *q = arg;
    for (;;) {
        must(mtx_lock(&q->lock));
        while (q->used == 0 && !q->done)
            must(cnd_wait(&q->readable, &q->lock));
        if (q->used == 0 && q->done) {
            must(mtx_unlock(&q->lock));
            break;
        }
        int value = q->data[q->head];
        q->head = (q->head + 1) % CAP;
        --q->used;
        must(cnd_signal(&q->writable));
        must(mtx_unlock(&q->lock));
        /* Only this worker accesses these fields until main joins. */
        q->sum += value;
        ++q->consumed;
    }
    return 0;
}

static int run(int inject_start_failure) {
    Queue q = {0};
    if (mtx_init(&q.lock, mtx_plain) != thrd_success) return -1;
    if (cnd_init(&q.readable) != thrd_success) {
        mtx_destroy(&q.lock);
        return -1;
    }
    if (cnd_init(&q.writable) != thrd_success) {
        cnd_destroy(&q.readable);
        mtx_destroy(&q.lock);
        return -1;
    }
    thrd_t worker;
    int status = inject_start_failure ? thrd_error : thrd_create(&worker, consume, &q);
    if (status != thrd_success) {
        cnd_destroy(&q.writable);
        cnd_destroy(&q.readable);
        mtx_destroy(&q.lock);
        return inject_start_failure ? 1 : -1;
    }
    for (int value = 1; value <= COUNT; ++value) {
        must(mtx_lock(&q.lock));
        while (q.used == CAP) must(cnd_wait(&q.writable, &q.lock));
        q.data[(q.head + q.used) % CAP] = value;
        ++q.used;
        must(cnd_signal(&q.readable));
        must(mtx_unlock(&q.lock));
    }
    must(mtx_lock(&q.lock));
    q.done = 1;
    must(cnd_signal(&q.readable));
    must(mtx_unlock(&q.lock));
    int result;
    must(thrd_join(worker, &result));
    int good = result == 0 && q.consumed == COUNT && q.sum == 500500L;
    cnd_destroy(&q.writable);
    cnd_destroy(&q.readable);
    mtx_destroy(&q.lock);
    return good ? 0 : -1;
}

int main(void) {
    if (run(1) != 1) return EXIT_FAILURE;
    for (int i = 0; i < 10; ++i)
        if (run(0) != 0) return EXIT_FAILURE;
    puts("queue: 10 x 1000 items; sums=500500; startup seam passed");
    return EXIT_SUCCESS;
}
```

### numbers.c — Floating and exact arithmetic

The observed first two numeric fields are naive=0 and compensated=1. GMP objects are all cleared, including an object initialized by a parsing call even if that call fails. NaN, infinity and signed zero use library facilities; the exercise does not deliberately divide by zero. This is a small fixed dataset, not a universal error bound.

```c
#include <fenv.h>
#include <float.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>

/* Declared experiment: binary64 double, round-to-nearest, no fast-math.
   Values are bounded; this is not a general overflow-proof accumulator. */
int main(void) {
    if (FLT_RADIX != 2 || DBL_MANT_DIG != 53 || DBL_MAX_EXP != 1024 ||
        fegetround() != FE_TONEAREST) {
        fputs("unsupported floating experiment\n", stderr);
        return 2;
    }
    volatile double values[] = {1e16, 1.0, -1e16};
    double sum = 0.0, correction = 0.0, naive = 0.0;
    for (size_t i = 0; i < 3; ++i) {
        double x = values[i], next = sum + x;
        if (fabs(sum) >= fabs(x)) correction += (sum - next) + x;
        else correction += (x - next) + sum;
        sum = next;
        naive += x;
    }
    double compensated = sum + correction;
    double nan_value = NAN, negative_zero = copysign(0.0, -1.0);
    int good = naive == 0.0 && compensated == 1.0 && isnan(nan_value) &&
        nan_value != nan_value && isinf(INFINITY) && !isfinite(INFINITY) &&
        signbit(negative_zero) && negative_zero == 0.0;
    mpz_t power, expected;
    mpz_init(power);
    int parsed = mpz_init_set_str(expected, "1267650600228229401496703205376", 10);
    mpz_ui_pow_ui(power, 2UL, 100UL);
    good = good && parsed == 0 && mpz_cmp(power, expected) == 0;
    mpq_t a, b, total, want;
    mpq_init(a); mpq_init(b); mpq_init(total); mpq_init(want);
    mpq_set_ui(a, 2UL, 20UL);
    mpq_canonicalize(a);
    mpq_set_ui(b, 1UL, 5UL);
    mpq_set_ui(want, 3UL, 10UL);
    mpq_add(total, a, b);
    good = good && mpq_equal(total, want);
    printf("numbers: naive=%.0f compensated=%.0f; GMP=%s; exact=%s\n",
           naive, compensated, gmp_version, good ? "passed" : "failed");
    mpq_clear(want); mpq_clear(total); mpq_clear(b); mpq_clear(a);
    mpz_clear(expected); mpz_clear(power);
    return good ? EXIT_SUCCESS : EXIT_FAILURE;
}
```

### descriptors.c — A pipe-to-file transfer with controls

Run in a disposable writable directory. The program creates one fixed-name file exclusively, never overwrites or removes a pre-existing file, and removes its own fixture after closing it. An unexpected CHECK failure exits immediately; OS teardown closes handles, but that diagnostic path can leave the newly created fixture for inspection. Normal and returned-error paths attempt cleanup. This is not a durable or cross-platform copier, and a partially written file is not rolled back.

```c
#define _POSIX_C_SOURCE 200809L
#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ioctl.h>
#include <unistd.h>

typedef ssize_t (*Writer)(int, const void *, size_t);
static unsigned checks;
#define CHECK(e) do { ++checks; if (!(e)) { \
    fprintf(stderr, "descriptor check %d: %s\n", __LINE__, #e); \
    exit(EXIT_FAILURE); } } while (0)

/* This exercise accepts at most 32 bytes per call. Return -1 on failure;
   bytes already written remain written. No transactional rollback. */
static int write_all(int fd, const unsigned char *data, size_t count, Writer writer) {
    if (count > 32) { errno = EINVAL; return -1; }
    size_t offset = 0;
    while (offset < count) {
        ssize_t n = writer(fd, data + offset, count - offset);
        if (n < 0 && errno == EINTR) continue;
        if (n < 0) return -1;
        if (n == 0 || (size_t)n > count - offset) { errno = EIO; return -1; }
        offset += (size_t)n;
    }
    return 0;
}

static ssize_t read_retry(int fd, void *buffer, size_t count) {
    ssize_t n;
    do { n = read(fd, buffer, count); } while (n < 0 && errno == EINTR);
    return n;
}

/* Linux close policy: relinquish ownership once, report errors, no retry. */
static int close_owned(int *fd) {
    if (*fd < 0) return 0;
    int old = *fd;
    *fd = -1;
    return close(old);
}

/* Single-thread test seam: one EINTR, then real two-byte-limited writes. */
static unsigned calls;
static ssize_t interrupted_short(int fd, const void *p, size_t n) {
    if (calls++ == 0) { errno = EINTR; return -1; }
    return write(fd, p, n > 2 ? 2 : n);
}
static ssize_t no_progress(int fd, const void *p, size_t n) {
    (void)fd; (void)p; (void)n;
    return 0;
}
static ssize_t fail_io(int fd, const void *p, size_t n) {
    (void)fd; (void)p; (void)n;
    errno = EIO;
    return -1;
}

static int exercise(void) {
    const unsigned char data[] = {'a', 0, 'b', 'c', 'd', 'e'};
    unsigned char buffer[32] = {0};
    int pair[2] = {-1, -1}, fd = -1, created = 0, result = -1;
    const char *path = "clp-exclusive-fixture.tmp";
    fd = open(path, O_RDWR | O_CREAT | O_EXCL, 0600);
    if (fd < 0) goto cleanup; /* Never remove a pre-existing path. */
    created = 1;
    if (pipe(pair) != 0) goto cleanup;
    int flags = fcntl(pair[0], F_GETFL);
    if (flags < 0 || fcntl(pair[0], F_SETFL, flags | O_NONBLOCK) < 0) goto cleanup;
    errno = 0;
    CHECK(read(pair[0], buffer, 1) == -1 && (errno == EAGAIN || errno == EWOULDBLOCK));
    if (fcntl(pair[0], F_SETFL, flags) < 0) goto cleanup;
    calls = 0;
    if (write_all(pair[1], data, sizeof data, interrupted_short) != 0) goto cleanup;
    CHECK(calls == 4);
    int available = -1;
    if (ioctl(pair[0], FIONREAD, &available) < 0) goto cleanup;
    CHECK(available == (int)sizeof data);
    if (close_owned(&pair[1]) != 0) goto cleanup;
    size_t copied = 0;
    for (;;) {
        ssize_t n = read_retry(pair[0], buffer, 2);
        if (n < 0) goto cleanup;
        if (n == 0) break;
        if (write_all(fd, buffer, (size_t)n, write) != 0) goto cleanup;
        copied += (size_t)n;
    }
    CHECK(copied == sizeof data);
    if (lseek(fd, 0, SEEK_SET) == (off_t)-1) goto cleanup;
    size_t used = 0;
    while (used < sizeof data) {
        ssize_t n = read_retry(fd, buffer + used, sizeof data - used);
        if (n <= 0) goto cleanup;
        used += (size_t)n;
    }
    CHECK(memcmp(buffer, data, sizeof data) == 0);
    CHECK(read_retry(fd, buffer, 1) == 0);
    errno = 0;
    CHECK(write_all(fd, data, 1, no_progress) == -1 && errno == EIO);
    CHECK(write_all(fd, data, 1, fail_io) == -1 && errno == EIO);
    CHECK(write_all(fd, data, 33, write) == -1 && errno == EINVAL);
    CHECK(write_all(fd, data, 0, write) == 0);
    CHECK(write_all(-1, data, 1, write) == -1 && errno == EBADF);
    result = 0;
cleanup:
    if (close_owned(&pair[1]) != 0) result = -1;
    if (close_owned(&pair[0]) != 0) result = -1;
    if (close_owned(&fd) != 0) result = -1;
    if (created && unlink(path) != 0) result = -1;
    return result;
}

int main(void) {
    if (exercise() != 0) { fputs("descriptor operation failed\n", stderr); return 1; }
    printf("descriptors: %u checks; fixture removed\n", checks);
    return 0;
}
```

### frames.c — A bounded stream decoder

The driver transmits at most 34 bytes per test and performs no listener setup or external network communication. Test failures terminate the process, allowing the OS to reclaim descriptors. Normal paths close both ends. Linux close behavior and `MSG_NOSIGNAL` are explicit platform choices; the latter also appears in POSIX.1-2008. Invalid lengths discard the connection. This blocking demonstration has no timeout or multi-client resource policy. [Send behavior](https://man7.org/linux/man-pages/man2/send.2.html)

```c
#define _POSIX_C_SOURCE 200809L
#include <errno.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

_Static_assert(CHAR_BIT == 8, "wire format requires octets");
enum { LIMIT = 32, OK = 0, EOF_FRAME = 1, TRUNCATED = 2, OVERSIZE = 3, IO_ERROR = 4 };
static unsigned checks;
#define CHECK(e) do { ++checks; if (!(e)) { \
    fprintf(stderr, "frame check %d: %s\n", __LINE__, #e); \
    exit(EXIT_FAILURE); } } while (0)

/* Blocking, bounded local exercise. Deliberately request one byte at a
   time to test loop progress; this says nothing about network packets. */
static int receive_exact(int fd, unsigned char *data, size_t count) {
    size_t offset = 0;
    while (offset < count) {
        ssize_t n = recv(fd, data + offset, 1, 0);
        if (n < 0 && errno == EINTR) continue;
        if (n < 0) return IO_ERROR;
        if (n == 0) return offset == 0 ? EOF_FRAME : TRUNCATED;
        offset += (size_t)n;
    }
    return OK;
}

/* On failure, output bytes and length are unchanged. A rejected frame
   invalidates this connection; do not try to resynchronize by guessing. */
static int receive_frame(int fd, unsigned char output[LIMIT], size_t *length) {
    unsigned char header[2], body[LIMIT];
    int status = receive_exact(fd, header, sizeof header);
    if (status != OK) return status;
    size_t count = (size_t)header[0] * 256u + header[1];
    if (count > LIMIT) return OVERSIZE;
    status = receive_exact(fd, body, count);
    if (status != OK) return status == EOF_FRAME ? TRUNCATED : status;
    if (count != 0) memcpy(output, body, count);
    *length = count;
    return OK;
}

static int send_bytes(int fd, const unsigned char *data, size_t count) {
    size_t offset = 0;
    while (offset < count) {
        ssize_t n = send(fd, data + offset, count - offset, MSG_NOSIGNAL);
        if (n < 0 && errno == EINTR) continue;
        if (n <= 0) return -1;
        offset += (size_t)n;
    }
    return 0;
}

static void one(const unsigned char *wire, size_t wire_length, int expected,
                const unsigned char *payload, size_t payload_length) {
    int pair[2];
    CHECK(socketpair(AF_UNIX, SOCK_STREAM, 0, pair) == 0);
    CHECK(send_bytes(pair[0], wire, wire_length) == 0);
    CHECK(shutdown(pair[0], SHUT_WR) == 0);
    unsigned char output[LIMIT], before[LIMIT];
    memset(output, 0x5A, sizeof output);
    memcpy(before, output, sizeof before);
    size_t length = 99;
    CHECK(receive_frame(pair[1], output, &length) == expected);
    if (expected == OK) {
        CHECK(length == payload_length);
        CHECK(payload_length == 0 || memcmp(output, payload, payload_length) == 0);
        CHECK(receive_frame(pair[1], output, &length) == EOF_FRAME);
    } else {
        CHECK(length == 99 && memcmp(output, before, sizeof before) == 0);
    }
    /* Linux: check close once; never retry a failed close. */
    int a = close(pair[0]), b = close(pair[1]);
    CHECK(a == 0 && b == 0);
}

int main(void) {
    const unsigned char abc[] = {0, 3, 'a', 'b', 'c'};
    const unsigned char empty[] = {0, 0};
    const unsigned char oversize[] = {0, 33};
    const unsigned char reversed[] = {3, 0};
    one(abc, sizeof abc, OK, abc + 2, 3);
    one(empty, sizeof empty, OK, empty, 0);
    one(empty, 0, EOF_FRAME, empty, 0);
    one(abc, 1, TRUNCATED, empty, 0);
    one(abc, 2, TRUNCATED, empty, 0);
    one(abc, 4, TRUNCATED, empty, 0);
    one(oversize, sizeof oversize, OVERSIZE, empty, 0);
    one(reversed, sizeof reversed, OVERSIZE, empty, 0);
    unsigned char boundary[34] = {0, LIMIT};
    for (unsigned i = 0; i < LIMIT; ++i) boundary[i + 2] = (unsigned char)i;
    one(boundary, sizeof boundary, OK, boundary + 2, LIMIT);
    int pair[2];
    CHECK(socketpair(AF_UNIX, SOCK_STREAM, 0, pair) == 0);
    unsigned char together[] = {0, 1, 'x', 0, 1, 'y'};
    CHECK(send_bytes(pair[0], together, sizeof together) == 0);
    CHECK(shutdown(pair[0], SHUT_WR) == 0);
    unsigned char output[LIMIT];
    size_t length = 0;
    CHECK(receive_frame(pair[1], output, &length) == OK && length == 1 && output[0] == 'x');
    CHECK(receive_frame(pair[1], output, &length) == OK && length == 1 && output[0] == 'y');
    CHECK(receive_frame(pair[1], output, &length) == EOF_FRAME);
    CHECK(close(pair[1]) == 0);
    errno = 0;
    CHECK(send_bytes(pair[0], together, 1) == -1 && errno == EPIPE);
    CHECK(close(pair[0]) == 0);
    printf("frames: %u checks; bounded local streams\n", checks);
    return 0;
}
```


## Integrated scenarios

### Cross-platform file copier

Implement a POSIX descriptor version and a Windows-native or ISO-stream comparison version. Handle short operations, interruption where applicable, binary/text distinctions, permissions/flags, resource cleanup, and error reporting. Document API versus ABI assumptions.

### Concurrent numeric pipeline

Read values, partition work across C11 threads where supported, calculate partial results, and merge them safely. Compare naive and compensated accumulation. Inject allocation/thread-creation failures and use race diagnostics plus written synchronization reasoning.

### Framed protocol service

Build a small length-prefixed client/server exchange. Serialize integers explicitly, loop over partial I/O, reject oversized frames, and close on every error path. Test fragmented delivery, zero length, unexpected disconnect, opposite byte order, and multiple clients.

These three scenarios are proposed extensions. The executed workbook establishes bounded parts of each; no Windows copier, live TCP service, packet capture, multiple-client test, real allocation failure or complete end-to-end scenario is claimed.

## Hands-on labs

The eight activities below remain learner assignments, with partial evidence supplied by the workbook. ThreadSanitizer validation needs a compatible runtime investigation before it can be counted as successful.

1. **Standards matrix:** compile focused examples in C89/C99/C11 modes; identify prototypes, VLAs, `_Generic`, `_Alignof`, threads, extensions, and diagnostics.
2. **Variadic contract:** implement a safe logging wrapper with `va_copy` and bounded formatting; test count/type mismatches only through code review, not intentional UB execution.
3. **Descriptor toolkit:** implement robust read/write loops and explore `fcntl` flags on a disposable file or pipe; label every POSIX-specific assumption.
4. **Memory/string harness:** compare `memcpy`/`memmove`, safe allocation growth, `qsort`/`bsearch`, and multibyte/wide conversions under declared locales.
5. **Threaded queue:** protect a bounded queue with C11 mutex/condition concepts where available; prove shutdown, wake-up, lifetime, and data-race behavior.
6. **Floating notebook:** generate NaN/infinities/signed zeros, classify values, demonstrate cancellation and rounding, then compare a multi-precision library with explicit cleanup.
7. **Socket pair:** complete the framed service and inspect packets. Test partial transport, invalid lengths, endianness, EOF, and cleanup.
8. **UB audit:** review a deliberately flawed codebase for sequencing, lifetime, bounds, format, shift, and non-local-jump defects; classify UB versus unspecified versus implementation-defined behavior.

## Original readiness checks

1. Why must a CLP example declare its C version and platform API?
2. Name two notable C99 and two C11 additions.
3. What purpose did trigraphs and digraphs serve?
4. What does `_Generic` select on?
5. Which default promotions matter in variadic calls?
6. What makes `va_arg` unsafe when the type/count contract is wrong?
7. Why is a counted typed array often safer than `...`?
8. How do API and ABI differ?
9. How does a POSIX descriptor differ from an ISO C `FILE *`?
10. Why must `read` and `write` loops handle partial results?
11. What are `fcntl` and `ioctl` broadly used for?
12. When should `memmove` replace `memcpy`?
13. Why can `memcmp` be wrong for semantic structure comparison?
14. What requirement precedes `bsearch`?
15. Why is subtraction a dangerous integer comparator implementation?
16. Why is `wchar_t` not synonymous with Unicode code point?
17. How do process and thread memory models differ broadly?
18. What makes an ordinary conflicting unsynchronized access dangerous?
19. Why is `volatile` not a mutex?
20. How should a race detector's clean run be interpreted?
21. How do NaN comparisons differ from ordinary numeric comparisons?
22. What is catastrophic cancellation?
23. Is a multiple-precision library part of ISO C by default?
24. Why does TCP require application framing?
25. Why must native structures not be sent as wire formats?
26. What do host/network byte-order conversions solve?
27. How do `const` and `volatile` differ?
28. What lifetime/value hazard follows `longjmp`?
29. How do undefined, unspecified, and implementation-defined behavior differ?
30. What must you verify before scheduling CLP?

## Answer key

1. The outline mixes language editions, OS APIs and external libraries. A POSIX descriptor example may be valid on Linux yet unavailable in a freestanding or Windows-native C implementation; name the contract before predicting results.
2. C99 examples include mixed declarations and designated initializers; C11 examples include `_Generic` and alignment facilities. Optional library support and compiler extensions mean acceptance alone does not establish an edition requirement.
3. They supplied alternate spellings in constrained source environments: `??=` historically becomes `#`, while `<:` is a bracket token. Their translation stages differ, so classify the actual mode before interpreting old source.
4. It selects a compatible type association using its controlling expression, which is not evaluated. `KIND(n++)` leaves n unchanged in the workbook; a selected expression can still have effects if the macro defines one.
5. Integer promotions affect narrow integer arguments, and float promotes to double. Passing integer 1 to a routine that retrieves double is not equivalent to passing 1.0, even if a cast after retrieval seems plausible.
6. The list has no automatic argument count/type schema. Over-reading and incompatible retrieval can be undefined; narrow exceptions in the standard are not a substitute for a matching contract. Never exercise a mismatch to prove its result.
7. The element type is visible and the count can be checked before access. A variadic count or format is only a promise by the caller and cannot recover lost type information.
8. An API describes source-level operations and contracts; an ABI includes register/stack usage, layout and binary linkage. The Microsoft x64 variadic register convention is one ABI, not an ISO requirement that every argument be on a stack.
9. A descriptor is an OS integer handle; FILE is an ISO buffered-stream abstraction. Check ownership and synchronization before mixing them, and do not assume two handles have independent offsets or status flags.
10. Positive progress can be smaller than the request. Advance by that count; retry EINTR only after a failure with no transfer; distinguish EOF, would-block and fatal errors. A zero-progress write must not cause an endless loop.
11. fcntl controls categories such as flags/locks; ioctl interprets an operation-specific request. FIONREAD on a tested Linux pipe is not a universal portable operation, and F_SETFL is distinct from descriptor close-on-exec flags.
12. Use memmove when valid ranges overlap. Both functions still require valid bounds and lifetimes; memmove cannot repair a dangling pointer or oversized count.
13. Padding bytes and alternate object representations can differ without changing member values. Compare fields according to the type contract; byte comparison is appropriate for the explicit wire arrays in the workbook.
14. Sort under a comparison consistent with the search key and elements. For duplicate keys, any matching element may be returned; its pointer is borrowed and expires with the array.
15. INT_MAX minus INT_MIN can overflow signed int. Comparing relationally and subtracting the resulting 0/1 values yields -1/0/1 without that overflow.
16. Its width/encoding are implementation-dependent, and a displayed character may contain multiple code points. Stateful multibyte conversion also depends on the current locale and requires invalid/incomplete-input handling.
17. Processes generally have separate address spaces/resource contexts; threads share much process state while retaining execution-local state. Sharing is explicit through mechanisms such as shared memory across processes, and thread APIs still vary by platform.
18. Conflicting non-atomic accesses in different threads without a required happens-before relation can be a data race and undefined behavior. The queue protects shared queue fields with a mutex and reads worker-only totals after join.
19. Volatile access semantics do not supply mutual exclusion or inter-thread synchronization. A bare fence also needs a valid atomic communication protocol; it is not a general repair for ordinary racy variables.
20. It covers only the instrumented executions and the tool's supported runtime. Here ThreadSanitizer crashed even on a minimal create/join probe, so there is no clean race-detector result to interpret as proof.
21. NaN is not equal to itself and ordinary ordered comparisons are false; use isnan/isfinite for classification. Positive and negative zero compare equal but may have different sign bits and function behavior.
22. Subtracting nearby approximate quantities can magnify existing relative error. The bounded accumulation example first loses a low-order 1, then cancellation exposes the loss; compensation improves that example but is not a universal cure.
23. No. GMP/MPFR have separate type, precision, allocation and cleanup contracts. The observed GMP6.3.0 example verifies exact integer/rational values; missing MPFR headers prevent a claim about executed MPFR results.
24. A stream transports ordered bytes without preserving send boundaries. A receiver must accumulate a complete header and payload, reject excessive lengths and distinguish clean EOF from a truncated frame.
25. Padding, type width, representation and endianness vary. Encode a documented sequence of bytes; the workbook uses two octets for a bounded length rather than dumping a structure.
26. They normalize the representation of supported multi-byte integers for transmission. They do not specify message framing, floating encodings, text encoding, validation or application delivery acknowledgments.
27. Const restricts writes through an access path; volatile makes accesses observable under the implementation's rules. Neither creates a general thread protocol, and casting away const cannot legalize a write to an originally const object.
28. The target must still be active in the same thread and scope constraints must hold. Certain changed automatic non-volatile locals become indeterminate; owned resources skipped by the transfer still need cleanup. The workbook uses a permitted conditional context and a volatile local.
29. Undefined behavior has no required result; unspecified behavior permits choices without documentation; implementation-defined behavior requires the choice to be documented. Unsequenced conflicting modifications, argument order, and plain-char signedness illustrate different categories.
30. Recheck CLP-12-01 scope, version, language, fees, delivery and policies. Resolve the no-prerequisite versus badge-criteria discrepancy and appointment change window using current booking terms; no account inspection in this review establishes personal eligibility.

## Final readiness checklist

- [ ] I separate ISO C version rules from POSIX, Win32, compiler, and external-library contracts.
- [ ] I can recognize historical constructs and apply the C11 features named by the blueprint.
- [ ] I implement variadic traversal with a written type/count contract and proper list lifetime.
- [ ] I handle descriptor failures, interruptions, partial operations, controls, and cleanup.
- [ ] I select memory/string/sort/search operations by range, overlap, ordering, and ownership contracts.
- [ ] I can explain a race-free thread design and why `volatile` is not synchronization.
- [ ] I classify exceptional floating values and demonstrate precision limits.
- [ ] I implement explicit network framing, serialization, byte order, validation, and partial I/O.
- [ ] I distinguish undefined, unspecified, and implementation-defined behavior and audit lifetimes/sequencing.
- [ ] I rechecked the live official page immediately before purchase.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Use one aligned primary path, then select platform documentation and labs for the interfaces you are practicing. Reconcile older courses with the current official CLP-12-01 syllabus and label every language/platform version.

| Resource | Access | Estimated time |
|---|---|---:|
| [Official CLP page and syllabus](https://cppinstitute.org/clp) | Free canonical blueprint | 2–3 hours to map and recheck |
| [C++ Institute exam policies](https://cppinstitute.org/exam-policies) | Free official policy | 20–40 minutes before scheduling |
| [OpenEDG C Advanced](https://edube.org/study/clp) | Public landing: free, English, advanced, CLP-12-01 alignment; enrolled lessons not read | 42 hours listed; seven/week advertised |
| [Cisco Networking Academy C Advanced](https://www.netacad.com/courses/c-advanced) | Public request returned only an application shell; enrollment/content unverified | Duration not verified from the rendered listing |
| [POSIX.1-2024 online specification](https://pubs.opengroup.org/onlinepubs/9799919799/) | Free primary specification | Ongoing; 8–15 hours targeted lookup |
| [Microsoft Windows API index](https://learn.microsoft.com/en-us/windows/win32/apiindex/windows-api-list) | Free official Windows documentation | Ongoing; 5–10 hours for comparison topics |
| [SEI CERT C Coding Standard](https://cmu-sei.github.io/secure-coding-standards/sei-cert-c-coding-standard/) | Free authoritative secure-coding reference | 10–20 hours targeted review |
| [cppreference C language and library](https://en.cppreference.com/w/c.html) | Free community reference | Ongoing; 8–15 hours targeted lookup |
| [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/) | Free community book; POSIX-oriented | 10–15 hours including labs |
| [O'Reilly Modern C, 3rd Edition](https://www.oreilly.com/library/view/modern-c-3rd/9781633437777/) | Subscription; broader/current language treatment | 20–35 hours selected chapters and exercises |

Only the public Edube landing was read; it advertises a completion-based discount, but checkout eligibility was not tested. Cisco returned a shell, O'Reilly denied access, and Beej/cppreference/SEI index navigation does not establish that all linked chapters were audited. Time ranges above, except the provider's Edube listing, are planning estimates.

No exact current MeasureUp or Whizlabs CLP-12-01 practice product was verified. Because this blueprint mixes portable C and platform APIs, prefer runnable objective-based labs to decontextualized question banks.
