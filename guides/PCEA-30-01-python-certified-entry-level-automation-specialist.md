---
exam_code: PCEA-30-01
vendor_id: python-institute
official_blueprint: https://pythoninstitute.org/pcea-exam-syllabus
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-30
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-30
---

# PCEA-30-01 Certified Entry-Level Automation Specialist with Python Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** **BETA / SMALL-MARKET-TRIAL CREDENTIAL.** The syllabus says active, but the live credential page labels PCEA-30-01 limited availability/small market trial/beta. Availability, objectives, scoring, and policies may change. Deep-reviewed September 30, 2026; verify the [official PCEA page](https://pythoninstitute.org/pcea) before acting.

**Current baseline:** PCEA-30-01 limited-availability beta; syllabus last updated September 2, 2025<br>
**Upcoming blueprint change:** beta stabilization is the change watch; no replacement code announced<br>
**Official delivery snapshot:** 46 questions; 60 minutes plus NDA; 75%; select, input-based, scenario and analytical items; TestNow; English<br>
**Credential snapshot:** no formal prerequisite; PCEP-equivalent Python and basic scripting/data exposure recommended; seven-year validity; USD 69 exam or USD 86 with retake when checked<br>

**VERIFY CURRENT:** The complete [credential page](https://pythoninstitute.org/pcea) still labels delivery limited availability / small market trial / beta. “Active” on the syllabus describes the published outline; it does not prove general availability. The complete [testing policy](https://pythoninstitute.org/pcea-testing-policies), revised September 2, 2025, specifies seven days after a failed attempt. Generic footer wording also mentions passing, which does not establish passed-exam retake eligibility. Local partner rescheduling and the global unredeemed-voucher procedure have different conditions. No account, booking, system test or purchase occurred.

The canonical English syllabus, all detailed bullets and the full minimum-qualified-candidate profile were manually read after direct retrieval and the automated monitor timed out. The existing 46-objective snapshot is retained; manual confirmation is not a successful new automated hash observation. Full PDF reading remains pending. The MQC incorrectly groups Requests, Beautiful Soup and `schedule` with standard libraries; these are third-party dependencies. Python's `sched` module and the separate `schedule` package are different tools.

## How to use this guide

Automate one bounded task end to end, then make it safe to rerun, observable, configurable, recoverable, and schedulable. Use disposable files, test endpoints, and accounts. A script that works once interactively is not yet reliable automation.

> **About related items:** A `Related item:` callout adds operational context, not an additional published objective.

## Weighted objective map

| Block | Items | Weight | Evidence of readiness |
|---|---:|---:|---|
| Automation fundamentals | 6 | 13% | Select suitable work and estimate value/limits |
| Command-line automation | 9 | 19.5% | Run/configure scripts, isolate dependencies, redirect output, and call fixed OS tools safely |
| Logging/monitoring | 7 | 15% | Emit actionable structured events and detect success/failure/staleness |
| File/data automation | 8 | 17.5% | Manipulate files safely and round-trip CSV/JSON with privacy controls |
| Web/API automation | 8 | 17.5% | Choose permitted API/scraping, fetch/parse defensively, and log outcomes |
| Scheduling/notification/reporting | 8 | 17.5% | Schedule without overlap, notify proportionately, and report traceable results |

## 1. Automation fundamentals — 13%

Good candidates are frequent, rule-based, stable, time-consuming, and measurable, with machine-readable inputs and clear exceptions. Avoid automating a broken/unclear process or high-consequence judgment without review.

Benefits include speed, consistency, scale, repeatability, and audit evidence. Costs include development, maintenance, runtime, monitoring, incidents, access, vendor/API change, and opportunity cost. Basic ROI compares net benefit with total cost over a declared period; do not ignore exception handling and maintenance.

A script automates a bounded task; process automation coordinates a business workflow; orchestration coordinates multiple automated systems/tasks with state and dependency handling. Python is useful because it is readable, portable, library-rich, and integrates well—but deployment and dependency management remain.

### Selecting work and calculating value

| Detailed objective | Study focus |
|---|---|
| 1.1.1 | Recognize routine work and its exceptions |
| 1.2.1 | Explain consistency, speed and scale |
| 1.2.2 | Account for failure, maintenance and judgment |
| 1.3.1 | Separate a script, a workflow and orchestration |
| 1.4.1 | Calculate ROI over an explicit period |
| 1.5.1 | Match Python's capabilities to the task |

For an original fictional report job, 240 annual runs at ten manual minutes each consume 40 hours. At an assumed USD 30/hour, manual cost is USD 1,200. Automation still needs two review minutes per run (USD 240), four maintenance hours (USD 120), USD 40 runtime cost and USD 400 initial development. First-year cost is USD 800, net benefit USD 400, and ROI is `(1,200 - 800) / 800 = 50%`. Recurring cost is USD 400/year, giving a simplified build-cost payback of `400 / (1,200 - 400) = 0.5 years`. These hypothetical values are checked by the workbook; they are not observed business savings. Reduced task volume, extra exceptions or rework can reverse the result.

A file summarizer is a script; collecting, reviewing and publishing reports is a process; coordinating separate services with dependencies, retries and recorded state is orchestration. A successful subprocess alone proves none of the surrounding approvals or delivery. Begin with a written input/output contract, owner, exception route and manual fallback. Automating a creative decision or an unclear rule merely repeats uncertainty faster. Python's library ecosystem helps integration, while dependency drift, platform differences and external service availability remain costs.

## 2. Command-line automation — 19.5%

Run a script with an explicit interpreter. `sys.argv` contains raw strings including the script name at index zero; validate count, type, range, and permitted values. A virtual environment isolates interpreter packages; it does not secure secrets or guarantee reproducibility without recorded versions.

A Unix shebang selects an interpreter when the executable script is launched and platform permissions permit it. Shell redirection routes stdout/stderr; keep normal machine-readable output separate from diagnostics where appropriate. Environment variables externalize configuration but can leak through process inspection, diagnostics, or logs.

Use `subprocess.run([...], check=..., timeout=..., capture_output=..., text=...)` with a fixed executable and argument list. Avoid `shell=True` with untrusted text. Decide how nonzero status, timeout, stdout, and stderr affect the automation's own result.

> **Related item:** `argparse` provides better help, conversion, and validation than direct `sys.argv`; it is useful professional context although the published objective names `sys.argv`.

### A reproducible command contract

| Detailed objective | Study focus |
|---|---|
| 2.1.1 | Select the interpreter and working directory |
| 2.1.2 | Validate raw argument strings |
| 2.1.3 | Explain environment isolation and recreation |
| 2.2.1 | Explain a Unix shebang and execution permission |
| 2.2.2 | Separate output, diagnostics and exit status |
| 2.2.3 | Read nonsecret environment configuration |
| 2.3.1 | Combine scripts with fixed OS tools |
| 2.3.2 | Handle child status, output and timeout |
| 2.3.3 | Choose bounded command-line tasks |

[Python's `sys` contract](https://docs.python.org/3.13/library/sys.html) makes `argv[0]` the script name/path, with special values for other invocation modes; `argv[1:]` is the script's argument list. The workbook's `preview 2` validates a small decimal range and a nonsecret `PCEA_RUN_ID`; it produces one JSON record on stdout and returns zero. An invalid argument produces a fixed diagnostic on stderr, no stdout and status 2. The preview command performs no network or filesystem work. Its public files must be saved together in a directory the learner controls.

A [virtual environment](https://docs.python.org/3.13/library/venv.html) has its own package environment by default. Activation adjusts the shell's path; directly invoking the environment's interpreter also works. Record the Python and dependency versions and recreate the environment instead of moving it. Activation is not a security boundary, and `VIRTUAL_ENV` alone is not proof of which interpreter is running. Creating/activating a venv, changing Unix executable permissions and installing dependencies remain unexecuted objectives in this review.

A Unix shebang only helps when the platform, launch method and executable permission support it. A scheduler needs an explicit interpreter/path and working directory; an interactive shell's defaults are not a deployment contract. Normal output and errors can be redirected separately, but shell syntax differs across PowerShell, cmd and POSIX shells. Do not paste a `dir` builtin into a shell-free subprocess list expecting it to behave like an executable. This workbook instead launches a fixed Python script with a fixed interpreter, a list of data arguments, a timeout and no shell.

[Subprocess behavior](https://docs.python.org/3.13/library/subprocess.html) separates a returned nonzero status, `CalledProcessError` under `check=True`, and timeout. Process creation can itself extend the effective deadline. The actual child checks use `-E -B`, preserve the already installed packages and pass only a synthetic run identifier to the script's output; they do not claim isolated mode or a clean environment. An initial `-I` experiment failed because Requests is installed in the user's package location. No installation or runtime setting was changed.

[Environment variables](https://docs.python.org/3.13/library/os.html) are strings, not validation or secret storage. Read a named setting, validate it and avoid dumping the environment. Changing a child environment mapping does not update the parent shell. The test inherits existing process settings but changes only its task-specific synthetic identifier; no credentials are logged or sent by the local HTTP fixture.

## 3. Logging and monitoring — 15%

Logs answer what ran, when, on what scope, with which correlation/run ID, what changed, and why it failed. DEBUG supports diagnosis, INFO normal milestones, WARNING degraded/recoverable conditions, ERROR failed operations, and CRITICAL severe service-level conditions. Format timestamps/time zone, level, logger, run ID, operation, and safe context.

Monitoring turns events/metrics into health signals: last-success age, duration, processed/rejected counts, error rate, queue/backlog, and output freshness. A job can exit zero while producing stale/empty output, so monitor outcome semantics as well as process status. Never log credentials or unnecessary personal data.

### Logs that describe an outcome

| Detailed objective | Study focus |
|---|---|
| 3.1.1 | Use logs to explain outcomes and failures |
| 3.1.2 | Configure a basic logger |
| 3.2.1 | Choose a meaningful severity |
| 3.2.2 | Format identity, time and context |
| 3.2.3 | Log file-operation results |
| 3.3.1 | Monitor counts, duration and freshness |
| 3.3.2 | Trace a failed workflow from evidence |

[`logging.basicConfig`](https://docs.python.org/3.13/library/logging.html) offers level, format, file or stream options, but normally does nothing once the root logger already has handlers. `force=True` replaces existing root handlers, so it is not an innocent default inside a reusable library. The workbook creates its own logger and in-memory stream handler, removes/closes the handler afterward, and leaves root configuration alone. It executes INFO success and ERROR failure paths; DEBUG, WARNING and CRITICAL are explained here, not claimed as exercised file-log integrations.

The original log includes a validated run identifier, row count, changed flag and elapsed seconds. It omits source labels and exception messages because either may contain private text. A simulated disk error emits its type without its synthetic secret-like message. Reporting only a type limits diagnosis; a real system needs a separately governed diagnostic channel, not unconditional raw exception logging. A failure after data commit can still affect logging or notification, so the whole workflow is not one transaction.

[`perf_counter`](https://docs.python.org/3.13/library/time.html) measures an interval from an arbitrary reference, while a wall-clock timestamp identifies when a run happened. An injected clock gives a deterministic 0.25-second test result; that number is not a benchmark. The workbook reports elapsed duration and counts, but does not persist a last-success timestamp or implement a monitoring service. For a future scheduled job, define expected frequency, maximum acceptable age, zero-row meaning, recipient and escalation. A live process or zero exit status is insufficient evidence that a useful report was delivered.

## 4. File and data automation — 17.5%

`pathlib` models paths; `os` exposes environment/system interfaces; `shutil` copies/moves directory/file data. Resolve expected roots, reject traversal/out-of-scope paths, avoid following unexpected links, preserve metadata only when required, and handle collisions explicitly.

Use context managers, temporary output, verification, and atomic replacement where supported. Make reruns idempotent: the second execution should converge rather than duplicate/corrupt. Catch specific filesystem errors and never report success after partial work.

CSV is tabular and needs `csv` because quoting/newlines matter. JSON supports nested typed values and uses `json.load/dump`. Validate schema/fields and encoding; do not equate successful parsing with trustworthy data. Minimize copied personal/sensitive content and apply retention/access rules.

### Data validation and one-file recovery

| Detailed objective | Study focus |
|---|---|
| 4.1.1 | Bound creation, reads, writes and deletion |
| 4.1.2 | Distinguish copying bytes from metadata |
| 4.1.3 | Preserve evidence when file operations fail |
| 4.2.1 | Choose tabular CSV or structured JSON |
| 4.2.2 | Merge CSV with explicit field and duplicate rules |
| 4.2.3 | Validate JSON types and serialize predictably |
| 4.3.1 | Make writes bounded, repeatable and recoverable |
| 4.3.2 | Minimize retained data and respect ownership |

The workbook accepts one to twenty records with exactly three fields. IDs are bounded lowercase tokens, labels are bounded printable text, and counts are integers from zero through 10,000; booleans are rejected despite Python's `bool`/`int` relationship. Duplicate IDs, unexpected fields and conflicting input are errors. Sorting produces deterministic output without mutating the caller's rows. JSON decoding rejects duplicate object keys and non-finite numbers, and limits input to 4,096 bytes. This narrow schema is for synthetic fixtures; it is not a general untrusted-document parser or a proof against every resource-exhaustion case. See the [JSON contract](https://docs.python.org/3.13/library/json.html).

[CSV parsing](https://docs.python.org/3.13/library/csv.html) preserves quoted commas and quotes; it does not validate a schema or convert ordinary fields to integers. `DictReader` can represent extra/missing cells, so the original merge checks the exact header, row shape, numeric format and duplicate IDs across parts. Files normally need `newline=''`. Display exports deliberately prefix labels with `label: ` and use a different header from raw input; do not round-trip that presentation CSV as an unchanged data source. Quoting alone is not spreadsheet-formula protection, and no spreadsheet application was opened.

[`Path.resolve`](https://docs.python.org/3.13/library/pathlib.html) helps identify a location, but prechecking a path is not race-free isolation. The workbook assumes an exclusively owned [temporary directory](https://docs.python.org/3.13/library/tempfile.html), uses only the fixed `snapshot.json` name, rejects an existing symlink, and stages a closed file beside the target before `os.replace`. Existing invalid state is preserved for investigation. An unchanged canonical snapshot returns before replacement, and a simulated replacement failure leaves the previous bytes intact and removes the owned staging file.

This is one-file replacement, with atomic rename semantics subject to the operating system/filesystem contract. It is not a transaction across JSON, CSV and HTML, a power-loss durability guarantee, a race-proof reparse-point defense, or a concurrent-writer protocol. CSV and HTML are returned in memory. No `fsync`, abrupt-process crash, disk exhaustion or cross-filesystem behavior was tested. Temporary names may survive an abrupt termination; production cleanup needs its own bounded ownership policy.

[`shutil.copyfile`](https://docs.python.org/3.13/library/shutil.html) copies bytes, whereas `copy2` attempts metadata preservation and still cannot preserve every platform's owners, ACLs or alternate streams. The original experiment copies and restores an 87-byte synthetic snapshot and verifies parsed data and byte equality. It does not establish application recovery, authenticated backup origin, off-site resilience or secure erasure. Removing an owned temporary file is not proof its former bytes are unrecoverable. Minimize collected fields and define lawful purpose, access, retention and disposal with the responsible owner; mentioning a privacy standard in the syllabus is not evidence of compliance.

## 5. Web and API automation — 17.5%

Prefer a documented API when it provides stable structured access. Scraping parses presentation HTML and is more fragile. Both require authorization/terms/privacy awareness, bounded rate, identification where appropriate, and respect for `robots.txt` as one signal—not the complete legal contract.

With `requests.get`, specify timeout, inspect status/content type/size, call `raise_for_status()` when suitable, and parse JSON only from the expected response. Use BeautifulSoup selectors based on stable structure, handle absent/multiple elements, and do not treat rendered browser content as guaranteed static HTML.

REST describes resource-oriented constraints; HTTP methods commonly represent read/create/replace/update/delete patterns, but the API documentation defines actual semantics. Handle pagination, rate limits, authentication expiry, and partial results where the endpoint requires them.

### HTTP responses and static HTML have different contracts

| Detailed objective | Study focus |
|---|---|
| 5.1.1 | Compare an API contract with page scraping |
| 5.1.2 | Check permission, terms, rate and privacy |
| 5.2.1 | Fetch with bounded response handling |
| 5.2.2 | Separate HTTP success from JSON validity |
| 5.3.1 | Select and validate static HTML elements |
| 5.3.2 | Log web results without exposing payloads |
| 5.4.1 | Explain resources, methods and status |
| 5.4.2 | Interpret a small API response and its limits |

The [Requests quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/) distinguishes decoding JSON from a successful response. A JSON error body can accompany HTTP 500, and a redirect is not the intended final resource. This exercise requires status 200, an expected JSON media type, identity content encoding, a bounded streamed body and the exact schema before any state update. It uses a fresh session with `trust_env=False` to avoid ambient proxy/default-authentication settings, and disables redirects. These are explicit local-fixture choices, not a general policy for every service. The [session API](https://requests.readthedocs.io/en/latest/api/) documents these settings.

Connect/read timeout values are not a total wall-clock deadline, as the [advanced guide](https://requests.readthedocs.io/en/latest/user/advanced/) explains. A continuously slow response can require additional supervision. The response byte cap limits accumulated content; this is not a full adversarial server sandbox. Context managers close responses and sessions after failure. The public probe binds a short-lived [HTTP server](https://docs.python.org/3.13/library/http.server.html) to 127.0.0.1 on an OS-assigned port, handles one owned request, joins its worker and closes. It serves synthetic bytes only, without browsing directories or making an external API request. `http.server` is not a production server.

Eight actual HTTP cases cover success, redirect, 429, 500, wrong media type, a 4,097-byte response, unexpected compression, and a missing field. Every case records exactly one `/records` request with no Authorization or Cookie header. A separately mocked read timeout checks propagation and cleanup; it does not measure real network latency or DNS/TLS failure. The exercise rejects rate limits without retrying. A real API design needs bounded backoff, `Retry-After` interpretation, pagination, authentication, endpoint terms and a decision about whether retrying a write duplicates effects.

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) parses the supplied markup; it does not run JavaScript or retrieve the page. The original fixture explicitly chooses `html.parser`, requires exactly one `h1.title`, joins/strips its text and rejects an absent, duplicate or empty title. Parser choice can change malformed-document results. The current documentation header/body report different versions (4.14.3/4.15.0), while the installed package used here is 4.13.3. Existing Requests is 2.34.2. No dependency upgrade or claim of a mandatory exam patch version follows from these observations.

## 6. Scheduling, notifications, and reporting — 17.5%

The `schedule` library runs while its Python process remains alive; it is not a durable system service by itself. Cron and Windows Task Scheduler launch jobs at the operating-system level, but you must configure working directory, interpreter, environment, credentials, timeout, and logs explicitly.

Prevent overlapping runs with a lock or idempotent design. Bound retries and distinguish transient from permanent failures. Email through `smtplib` requires correct SMTP transport/authentication and safe handling of recipients/content; desktop notifications suit a logged-in local user, not unattended servers. Avoid alert fatigue and disclose no secrets.

Reports should include run ID/time, source/scope, counts, changes, failures, limitations, and next action. Escape dynamic content in HTML reports and link to logs rather than embedding sensitive raw values.

### Scheduling and delivery remain separate work

| Detailed objective | Study focus |
|---|---|
| 6.1.1 | Define when work should run and what a missed run means |
| 6.1.2 | Explain the in-process scheduling loop |
| 6.2.1 | Compare cron and Windows Task Scheduler |
| 6.2.2 | Account for launch context, restart and overlap |
| 6.3.1 | Separate message creation, transport and delivery |
| 6.3.2 | Recognize desktop-session notification limits |
| 6.4.1 | Produce a traceable text/HTML report |
| 6.4.2 | Connect scheduled outcomes with logs and alerts |

The complete [`schedule` landing page](https://schedule.readthedocs.io/en/stable/) describes an in-process scheduler and explicitly excludes job persistence, exact timing and concurrent execution from its basic guarantees. Long jobs affect the scheduling loop. It is not Python's standard `sched` module. The package is absent here, so installing it, running its periodic loop and testing a cron/Task Scheduler launch remain future exercises. No persistent process or system task was created.

An OS scheduler can launch a fresh process with a different identity, path, environment and network access. Specify the interpreter, working directory, timeout, overlap rule, retry policy, logs, missed-run behavior and timezone. A [threading lock](https://docs.python.org/3.13/library/threading.html) probe demonstrates nonblocking contention and release in one process. It is separate from `run_once` and is not an implemented cross-process lock or proof that two scheduled jobs cannot overlap. Independent processes require a suitable lock/lease and failure recovery; idempotency remains useful even when overlap is prevented.

The workbook computes `notification_needed` for changed output and logs failures, but sends nothing. A crash after committing data and before sending a message can lose the notification; retrying after a send can duplicate it. Exactly-once delivery is not implied by a changed flag. A future design can record an outbox/delivery state and recipient-specific deduplication, with an explicit expiry/escalation policy. These designs are not implemented or verified here.

[`EmailMessage`](https://docs.python.org/3.13/library/email.message.html) represents headers and payload; [`smtplib`](https://docs.python.org/3.13/library/smtplib.html) handles SMTP transport. A provider's TLS/authentication/recipient policy is a separate contract, and a successful transport call is not proof that a person read the message. No SMTP connection, real address, credential, desktop notification or `plyer` installation was used. Desktop popups usually depend on a usable interactive session and should not be the sole signal for an unattended job.

The workbook's HTML uses [`html.escape`](https://docs.python.org/3.13/library/html.html) for text nodes. This does not authorize arbitrary HTML, JavaScript, URL or CSS interpolation. Reports should include source scope, run identity, time, counts, failures, limits and next action; the executable function only demonstrates the bounded CSV/HTML content transformation and returns run results separately. Integrating a complete dated report, governed log retention, scheduling and delivery remains part of the full lab.

## Integrated lab

Build a **permitted public-data change reporter**:

1. estimate manual cost and automation ROI/limits;
2. accept validated CLI arguments and environment-based nonsecret configuration in a venv;
3. fetch a test API with timeout/status/content checks;
4. store raw JSON and normalized CSV under a validated root using temporary/atomic output;
5. log a run ID, counts, duration, warnings, and failures without response secrets;
6. compare against the previous snapshot idempotently;
7. produce an escaped HTML/text summary;
8. schedule via library and one OS scheduler design, preventing overlap;
9. send a notification only on meaningful change or failure;
10. prove retry, invalid data, missing field, rate limit, disk error, and partial-output behavior.

## Exact original executable workbook

**PRACTICAL DEPTH:** Save the following three files together in a disposable directory. They use existing Python 3.13.14, Requests 2.34.2 and Beautiful Soup 4.13.3. The review installed nothing. The two test commands below were executed in normal and optimized modes with warnings treated as errors; each mode passed **25 test methods and 23 computed observation checks**. The observation results match exactly. Four receipts and exact source hashes are recorded in the dated review evidence. Selected [Ruff rules](https://docs.astral.sh/ruff/linter/) pass at 79 columns; this is not a security audit or complete static-analysis proof.

```text
python -B -Werror -m unittest discover -s . -p test_automation_workbook.py -v
python -B -Werror observations.py
python -B -Werror -O -m unittest discover -s . -p test_automation_workbook.py -v
python -B -Werror -O observations.py
```

Only synthetic data, owned temporary files, short Python children and short-lived loopback listeners are used. The functions assume the trusted directory and fixtures described above. Read the code before running it: importing Requests/Beautiful Soup is required, and dependencies may be unavailable in a newly isolated environment. The ten-step integrated lab remains a plan; the workbook does not complete venv setup, external service access, persistent scheduling, desktop/email delivery, cross-process locking or human readiness review.

### automation_workbook.py

```python
"""Original PCEA workbook: synthetic data and an owned temporary root only."""
import csv
import html
import io
import json
import logging
import os
from pathlib import Path
import re
import sys
import tempfile
import time

import requests
from bs4 import BeautifulSoup


def token(value):
    if (type(value) is not str
            or not re.fullmatch(r"[a-z][a-z0-9-]{0,19}", value)):
        raise ValueError("invalid identifier")
    return value


def records(value):
    if type(value) is not list or not 1 <= len(value) <= 20:
        raise ValueError("expected one to twenty rows")
    result, seen = [], set()
    for row in value:
        if type(row) is not dict or set(row) != {"id", "label", "count"}:
            raise ValueError("unexpected fields")
        key = token(row["id"])
        label, count = row["label"], row["count"]
        if key in seen:
            raise ValueError("duplicate identifier")
        if (type(label) is not str or not 1 <= len(label) <= 80
                or not label.isprintable()):
            raise ValueError("invalid label")
        if type(count) is not int or not 0 <= count <= 10000:
            raise ValueError("invalid count")
        seen.add(key)
        result.append(dict(id=key, label=label, count=count))
    return sorted(result, key=lambda row: row["id"])


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError("non-finite JSON number")


def decode(raw):
    if type(raw) is not bytes or not 1 <= len(raw) <= 4096:
        raise ValueError("invalid byte count")
    value = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_pairs,
                       parse_constant=reject_constant)
    return records(value)


def encoded(rows):
    return json.dumps(records(rows), ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode("utf-8") + b"\n"


def combine_csv(parts):
    if type(parts) is not list or not 1 <= len(parts) <= 3:
        raise ValueError("invalid part count")
    result = []
    for part in parts:
        if type(part) is not str or not 1 <= len(part) <= 4096:
            raise ValueError("invalid CSV size")
        reader = csv.DictReader(io.StringIO(part, newline=""), strict=True)
        if reader.fieldnames != ["id", "label", "count"]:
            raise ValueError("unexpected CSV header")
        for row in reader:
            if (set(row) != {"id", "label", "count"}
                    or any(value is None for value in row.values())
                    or not re.fullmatch(r"[0-9]{1,5}", row["count"])):
                raise ValueError("invalid CSV row")
            row["count"] = int(row["count"])
            result.append(row)
            if len(result) > 20:
                raise ValueError("too many rows")
    return records(result)


def reports(rows):
    rows = records(rows)
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(["id", "display_label", "count"])
    items = []
    for row in rows:
        # This display export deliberately differs from a raw-data CSV.
        writer.writerow([row["id"], "label: " + row["label"], row["count"]])
        items.append("<li>" + html.escape(row["label"], quote=True)
                     + ": " + str(row["count"]) + "</li>")
    markup = "<ul>" + "".join(items) + "</ul>"
    return {"csv": output.getvalue(), "html": markup}


def static_title(markup):
    if type(markup) is not str or not 1 <= len(markup) <= 4096:
        raise ValueError("invalid HTML size")
    soup = BeautifulSoup(markup, "html.parser")
    matches = soup.select("h1.title")
    if len(matches) != 1:
        raise ValueError("expected exactly one title")
    value = matches[0].get_text(" ", strip=True)
    if not value or len(value) > 80 or not value.isprintable():
        raise ValueError("invalid title")
    return value


def fetch_owned(port):
    """Call only with the port of this exercise's own loopback server."""
    if type(port) is not int or not 1 <= port <= 65535:
        raise ValueError("invalid owned port")
    with requests.Session() as session:
        session.trust_env = False
        with session.get(f"http://127.0.0.1:{port}/records",
                         timeout=(2, 2), allow_redirects=False, stream=True,
                         headers={"Accept-Encoding": "identity"}) as response:
            if response.status_code != 200:
                raise ValueError("unexpected HTTP status")
            kind = response.headers.get("Content-Type", "").split(";")[0]
            if kind.strip().lower() != "application/json":
                raise ValueError("unexpected media type")
            encoding = response.headers.get("Content-Encoding", "identity")
            if encoding != "identity":
                raise ValueError("unexpected content encoding")
            raw = bytearray()
            for chunk in response.iter_content(chunk_size=512):
                if len(raw) + len(chunk) > 4096:
                    raise ValueError("response too large")
                raw.extend(chunk)
            return decode(bytes(raw))


def save_snapshot(root, rows):
    """One file in a trusted, exclusively owned temporary directory."""
    payload = encoded(rows)
    if len(payload) > 4096:
        raise ValueError("snapshot too large")
    base = Path(root).resolve(strict=True)
    if not base.is_dir():
        raise ValueError("root must be a directory")
    target = base / "snapshot.json"
    if target.is_symlink():
        raise ValueError("linked target")
    if target.exists():
        with target.open("rb") as source:
            previous = source.read(4097)
        decode(previous)  # Preserve corrupt state for investigation.
        if previous == payload:
            return False
    staging = None
    try:
        with tempfile.NamedTemporaryFile(dir=base, prefix="stage-",
                                         delete=False) as stream:
            staging = Path(stream.name)
            stream.write(payload)
        os.replace(staging, target)
    finally:
        if staging is not None and staging.exists():
            if staging.resolve().parent != base:
                raise RuntimeError("unexpected cleanup location")
            staging.unlink()
    return True


def run_once(root, rows, run_id, stream, clock=time.perf_counter):
    run_id = token(run_id)
    logger = logging.Logger("pcea-workbook", level=logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler(stream)
    handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(handler)
    started = clock()
    try:
        valid = records(rows)
        rendered = reports(valid)
        changed = save_snapshot(root, valid)
    except (ValueError, OSError) as error:
        logger.error("run=%s failed=%s", run_id, type(error).__name__)
        raise
    else:
        elapsed = round(clock() - started, 6)
        logger.info("run=%s rows=%d changed=%s seconds=%.6f",
                    run_id, len(valid), changed, elapsed)
        return dict(changed=changed, rows=len(valid), reports=rendered,
                    elapsed=elapsed, notification_needed=changed)
    finally:
        logger.removeHandler(handler)
        handler.close()


def main(argv, environment, stdout, stderr):
    try:
        if len(argv) != 2 or argv[0] != "preview":
            raise ValueError("usage")
        if not re.fullmatch(r"[0-9]{1,2}", argv[1]):
            raise ValueError("count")
        count = int(argv[1])
        if not 1 <= count <= 20:
            raise ValueError("count")
        run_id = token(environment.get("PCEA_RUN_ID", "local"))
    except (ValueError, TypeError):
        print("invalid preview arguments or run identifier", file=stderr)
        return 2
    print(json.dumps({"run_id": run_id, "requested_rows": count}), file=stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:], os.environ, sys.stdout, sys.stderr))
```

### test_automation_workbook.py

```python
"""Original behavioral contracts; all file fixtures belong to this test."""
import copy
import csv
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import automation_workbook as work


def fixture():
    return [dict(id="b", label='North, "annex"', count=0),
            dict(id="a", label="<script>synthetic</script>", count=7)]


class WorkbookTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(
            dir=Path(__file__).resolve().parent, prefix="test-owned-")
        self.root = Path(self.temp.name)
        self.assertEqual(self.root.resolve().parent,
                         Path(__file__).resolve().parent)
        self.addCleanup(self.temp.cleanup)

    def test_canonical_order_and_input_preserved(self):
        rows = fixture()
        before = copy.deepcopy(rows)
        result = work.records(rows)
        self.assertEqual([row["id"] for row in result], ["a", "b"])
        result[0]["count"] = 2
        self.assertEqual(rows, before)

    def test_boolean_is_not_a_count(self):
        for value in [True, False, -1, 10001, 1.5, "1", None]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                work.records([dict(id="a", label="A", count=value)])

    def test_count_boundaries(self):
        for value in [0, 10000]:
            self.assertEqual(work.records([
                dict(id="a", label="A", count=value)])[0]["count"], value)

    def test_schema_and_duplicate_ids(self):
        for value in [[], {}, [1], fixture() * 2,
                      [dict(id="a", label="A")],
                      [dict(id="a", label="A", count=1, secret="omitted")]]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                work.records(value)

    def test_bounds_and_control_characters(self):
        for label in ["", "A" * 81, "A\nB", "A\x00B"]:
            with self.subTest(label=label), self.assertRaises(ValueError):
                work.records([dict(id="a", label=label, count=1)])
        with self.assertRaises(ValueError):
            work.records([dict(id="A", label="A", count=1)])

    def test_json_round_trip_and_order(self):
        raw = work.encoded(fixture())
        self.assertEqual(work.decode(raw), work.records(fixture()))
        self.assertEqual(raw, work.encoded(list(reversed(fixture()))))
        self.assertTrue(raw.endswith(b"\n"))

    def test_json_duplicate_keys_rejected(self):
        raw = b'[{"id":"a","label":"A","count":1,"count":2}]'
        with self.assertRaises(ValueError):
            work.decode(raw)

    def test_json_nonfinite_utf8_and_size(self):
        for raw in [b"", b"x" * 4097, b"\xff", b"[NaN]", b"[Infinity]",
                    b"null", b"[]", b"{}", b"[", b"[true]"]:
            with self.subTest(raw=raw[:20]), self.assertRaises(ValueError):
                work.decode(raw)

    def test_csv_merge_quoted_delimiter(self):
        parts = ['id,label,count\nb,"North, annex",2\n',
                 'id,label,count\na,South,3\n']
        self.assertEqual(work.combine_csv(parts), [
            dict(id="a", label="South", count=3),
            dict(id="b", label="North, annex", count=2)])

    def test_csv_missing_extra_or_duplicate_header(self):
        for text in ['id,label,count\na,A\n', 'id,label,count\na,A,1,2\n',
                     'id,id,count\na,a,1\n', 'id,label,count\na,A,-1\n']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                work.combine_csv([text])

    def test_csv_duplicate_identifier_across_parts(self):
        part = 'id,label,count\na,A,1\n'
        with self.assertRaises(ValueError):
            work.combine_csv([part, part])

    def test_display_csv_and_html_contexts(self):
        rows = fixture() + [dict(id="c", label="=SUM(1,2)", count=1)]
        report = work.reports(rows)
        parsed = list(csv.DictReader(io.StringIO(report["csv"])))
        self.assertEqual(parsed[1]["display_label"],
                         'label: North, "annex"')
        self.assertEqual(parsed[2]["display_label"],
                         "label: =SUM(1,2)")
        self.assertNotIn("<script>", report["html"])
        self.assertIn("&lt;script&gt;synthetic&lt;/script&gt;", report["html"])

    def test_static_html_title(self):
        markup = '<h1 class="title">North <b>&amp;</b> South</h1>'
        self.assertEqual(work.static_title(markup), "North & South")

    def test_missing_multiple_or_empty_html_title(self):
        for markup in ['<p>none</p>', '<h1 class="title"></h1>',
                       '<h1 class="title">A</h1>' * 2]:
            with self.subTest(markup=markup), self.assertRaises(ValueError):
                work.static_title(markup)

    def test_first_commit_and_idempotent_rerun(self):
        self.assertTrue(work.save_snapshot(self.root, fixture()))
        target = self.root / "snapshot.json"
        before = (target.read_bytes(), target.stat().st_mtime_ns)
        with patch.object(work.os, "replace") as replacement:
            self.assertFalse(work.save_snapshot(self.root, fixture()[::-1]))
        replacement.assert_not_called()
        after = (target.read_bytes(), target.stat().st_mtime_ns)
        self.assertEqual(after, before)

    def test_changed_snapshot_replaces_old(self):
        work.save_snapshot(self.root, fixture())
        newer = fixture()
        newer[0]["count"] = 9
        self.assertTrue(work.save_snapshot(self.root, newer))
        actual = work.decode((self.root / "snapshot.json").read_bytes())
        self.assertEqual(actual, work.records(newer))

    def test_failed_replace_preserves_previous_and_cleans_stage(self):
        work.save_snapshot(self.root, fixture())
        before = (self.root / "snapshot.json").read_bytes()
        newer = fixture()
        newer[0]["count"] = 5
        failure = PermissionError("synthetic-detail-not-for-log")
        with patch.object(work.os, "replace", side_effect=failure):
            with self.assertRaises(PermissionError) as caught:
                work.save_snapshot(self.root, newer)
        self.assertIs(caught.exception, failure)
        self.assertEqual((self.root / "snapshot.json").read_bytes(), before)
        self.assertEqual(sorted(p.name for p in self.root.iterdir()),
                         ["snapshot.json"])

    def test_corrupt_previous_is_not_overwritten(self):
        target = self.root / "snapshot.json"
        target.write_bytes(b"corrupt synthetic state")
        with self.assertRaises(ValueError):
            work.save_snapshot(self.root, fixture())
        self.assertEqual(target.read_bytes(), b"corrupt synthetic state")

    def test_invalid_input_creates_no_files(self):
        with self.assertRaises(ValueError):
            work.save_snapshot(self.root, [])
        self.assertEqual(list(self.root.iterdir()), [])

    def test_path_and_directory_errors(self):
        with self.assertRaises(FileNotFoundError):
            work.save_snapshot(self.root / "missing", fixture())
        (self.root / "snapshot.json").mkdir()
        with self.assertRaises(OSError):
            work.save_snapshot(self.root, fixture())

    def test_run_logs_counts_not_labels(self):
        sink = io.StringIO()
        ticks = iter([10.0, 10.25])
        result = work.run_once(self.root, fixture(), "run-a", sink,
                               clock=lambda: next(ticks))
        self.assertEqual(result["elapsed"], 0.25)
        self.assertTrue(result["notification_needed"])
        expected = "INFO run=run-a rows=2 changed=True seconds=0.250000\n"
        self.assertEqual(sink.getvalue(), expected)
        self.assertNotIn("synthetic", sink.getvalue())

    def test_rerun_suppresses_notification_decision(self):
        work.save_snapshot(self.root, fixture())
        result = work.run_once(self.root, fixture(), "run-b", io.StringIO())
        self.assertFalse(result["notification_needed"])

    def test_failure_log_omits_exception_message(self):
        sink = io.StringIO()
        with patch.object(work, "save_snapshot",
                          side_effect=PermissionError("synthetic-secret")):
            with self.assertRaises(PermissionError):
                work.run_once(self.root, fixture(), "run-a", sink)
        self.assertEqual(sink.getvalue(),
                         "ERROR run=run-a failed=PermissionError\n")

    def test_cli_output_and_validation(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        status = work.main(["preview", "2"], {"PCEA_RUN_ID": "fixture"},
                           stdout, stderr)
        self.assertEqual(status, 0)
        self.assertEqual(json.loads(stdout.getvalue()),
                         dict(run_id="fixture", requested_rows=2))
        self.assertEqual(stderr.getvalue(), "")
        for args in [[], ["preview", "0"], ["preview", "21"],
                     ["preview", "1;echo"], ["other", "1"]]:
            output, errors = io.StringIO(), io.StringIO()
            self.assertEqual(work.main(args, {}, output, errors), 2)
            self.assertEqual(output.getvalue(), "")
            self.assertTrue(errors.getvalue())

    def test_port_validation_precedes_connection(self):
        with patch.object(work.requests, "Session") as session:
            for port in [True, 0, 65536, "80", -1]:
                with self.subTest(port=port), self.assertRaises(ValueError):
                    work.fetch_owned(port)
            session.assert_not_called()


if __name__ == "__main__":
    unittest.main()
```

### observations.py

```python
"""Original integration probes; no persistent server, scheduler or message."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import threading
from unittest.mock import patch

import automation_workbook as work


ROWS = [dict(id="a", label="A < B", count=2),
        dict(id="b", label='North, "annex"', count=3)]
PASSED = []


def check(name, condition):
    if not condition:
        raise RuntimeError(name)
    PASSED.append(name)


def exercise_http(status=200, kind="application/json", body=None,
                  encoding="identity"):
    body = work.encoded(ROWS) if body is None else body
    seen = []

    class Handler(BaseHTTPRequestHandler):
        timeout = 2

        def do_GET(self):
            seen.append(dict(path=self.path,
                             authenticated="Authorization" in self.headers,
                             cookies="Cookie" in self.headers))
            self.send_response(status)
            self.send_header("Content-Type", kind)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Content-Encoding", encoding)
            if status == 302:
                self.send_header("Location", "/never-follow")
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, format, *args):
            pass

    with HTTPServer(("127.0.0.1", 0), Handler) as server:
        server.timeout = 2
        worker = threading.Thread(target=server.handle_request)
        worker.start()
        try:
            result = work.fetch_owned(server.server_port)
            outcome = dict(result=result, error=None)
        except ValueError as error:
            outcome = dict(result=None, error=str(error))
        finally:
            worker.join(timeout=3)
        if worker.is_alive():
            raise RuntimeError("owned HTTP worker did not stop")
    if seen != [dict(path="/records", authenticated=False, cookies=False)]:
        raise RuntimeError("unexpected owned HTTP request")
    return outcome


def main():
    normal = exercise_http()
    check("owned-http-success", normal == dict(result=ROWS, error=None))
    http = {}
    cases = [
        ("redirect", dict(status=302), "unexpected HTTP status"),
        ("rate-limit", dict(status=429), "unexpected HTTP status"),
        ("server-error", dict(status=500), "unexpected HTTP status"),
        ("wrong-type", dict(kind="text/html"), "unexpected media type"),
        ("oversize", dict(body=b"x" * 4097), "response too large"),
        ("compressed", dict(encoding="gzip"), "unexpected content encoding"),
        ("missing-field", dict(body=b'[{"id":"a"}]'), "unexpected fields"),
    ]
    for name, options, message in cases:
        outcome = exercise_http(**options)
        check("owned-http-" + name,
              outcome == dict(result=None, error=message))
        http[name] = message

    timeout = work.requests.exceptions.ReadTimeout("synthetic detail")
    with patch.object(work.requests, "Session") as factory:
        session = factory.return_value.__enter__.return_value
        session.get.side_effect = timeout
        try:
            work.fetch_owned(1)  # Mocked; no connection to port 1 occurs.
        except work.requests.exceptions.ReadTimeout as caught:
            check("simulated-timeout-propagated", caught is timeout)
        else:
            raise RuntimeError("expected simulated timeout")
        options = session.get.call_args.kwargs
        check("http-configuration-observed",
              session.trust_env is False and options["timeout"] == (2, 2)
              and options["allow_redirects"] is False
              and options["stream"] is True)
    check("session-exit-after-timeout",
          factory.return_value.__exit__.call_count == 1)

    parent = Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory(dir=parent, prefix="probe-owned-") as tmp:
        root = Path(tmp)
        if root.resolve().parent != parent:
            raise RuntimeError("unexpected temporary root")
        saved_path = root
        sink = io.StringIO()
        first = work.run_once(root, ROWS, "run-a", sink)
        check("first-snapshot-and-report", first["changed"]
              and "A &lt; B" in first["reports"]["html"])
        snapshot = root / "snapshot.json"
        original = snapshot.read_bytes()
        before = snapshot.stat().st_mtime_ns
        second = work.run_once(root, ROWS[::-1], "run-b", sink)
        check("rerun-no-write-no-notification",
              not second["notification_needed"]
              and snapshot.stat().st_mtime_ns == before
              and snapshot.read_bytes() == original)
        backup = root / "backup.json"
        shutil.copyfile(snapshot, backup)
        changed = [dict(row) for row in ROWS]
        changed[0]["count"] = 4
        third = work.run_once(root, changed, "run-c", sink)
        check("meaningful-change", third["changed"]
              and snapshot.read_bytes() != original)
        shutil.copyfile(backup, snapshot)
        check("owned-byte-restore", snapshot.read_bytes() == original
              and work.decode(snapshot.read_bytes()) == ROWS)
        with patch.object(work.os, "replace",
                          side_effect=OSError("synthetic-disk-failure")):
            try:
                work.run_once(root, changed, "run-d", sink)
            except OSError:
                check("simulated-disk-failure-preserved-state",
                      snapshot.read_bytes() == original
                      and not list(root.glob("stage-*")))
            else:
                raise RuntimeError("expected simulated disk failure")
        check("failure-log-redacted", "failed=OSError" in sink.getvalue()
              and "synthetic-disk-failure" not in sink.getvalue()
              and 'North, "annex"' not in sink.getvalue())
    check("temporary-root-removed", not saved_path.exists())

    env = dict(os.environ)
    env["PCEA_RUN_ID"] = "child-fixture"
    base = [sys.executable, "-E", "-B"]
    if sys.flags.optimize:
        base.append("-O")
    base.append(str(parent / "automation_workbook.py"))
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    child = subprocess.run(base + ["preview", "2"], env=env, timeout=5,
                           capture_output=True, text=True, check=True,
                           creationflags=flags)
    check("real-child-cli-success", not child.stderr
          and json.loads(child.stdout) == dict(run_id="child-fixture",
                                              requested_rows=2))
    bad = subprocess.run(base + ["preview", "1;echo"], env=env, timeout=5,
                         capture_output=True, text=True, check=False,
                         creationflags=flags)
    message = "invalid preview arguments or run identifier"
    check("real-child-cli-failure", bad.returncode == 2 and not bad.stdout
          and bad.stderr.strip() == message)

    lock = threading.Lock()
    first_acquired = lock.acquire(blocking=False)
    try:
        check("same-process-overlap-rejected",
              first_acquired and not lock.acquire(blocking=False))
    finally:
        if first_acquired:
            lock.release()
    again = lock.acquire(blocking=False)
    check("lock-released-for-next-run", again)
    if again:
        lock.release()

    manual_cost = 240 * 10 / 60 * 30
    recurring = 240 * 2 / 60 * 30 + 4 * 30 + 40
    total_cost = recurring + 400
    roi = (manual_cost - total_cost) / total_cost * 100
    check("hypothetical-roi", manual_cost == 1200 and total_cost == 800
          and roi == 50 and 400 / (manual_cost - recurring) == 0.5)
    print(json.dumps(dict(passed_checks=len(PASSED), checks=PASSED,
                          http_failures=http, snapshot_bytes=len(original),
                          hypothetical_roi_percent=roi), sort_keys=True))


if __name__ == "__main__":
    main()
```

## Original knowledge checks

1. What makes a task suitable for automation?
2. Which costs belong in ROI?
3. Contrast script, process automation, and orchestration.
4. What is `sys.argv[0]`?
5. What does a virtual environment not solve?
6. Why separate stdout and stderr?
7. Why pass a subprocess argument list?
8. What makes a log event actionable?
9. Why monitor last-success age?
10. What makes a file automation idempotent?
11. Why use the `csv` module?
12. Why is parsed JSON not automatically trusted?
13. Why prefer an API over scraping?
14. What must be checked before parsing a response?
15. Why is the `schedule` library not durable scheduling?
16. How do you prevent overlapping runs?
17. What must an HTML report do with dynamic text?
18. Why must PCEA status be verified frequently?

## Answers and reasoning

1. Choose repeated, rule-based work with stable inputs, measurable outputs and a known exception owner. Unclear judgment or high-impact decisions still need review; frequency alone does not justify automation.
2. Count development, residual manual review, maintenance, execution, access and incident costs over one period. In the original hypothetical example, USD 1,200 manual cost versus USD 800 first-year automation cost gives USD 400 net benefit and 50% ROI. The denominator is total automation cost, not savings.
3. A script performs a bounded task; process automation coordinates a workflow; orchestration coordinates systems/tasks and dependencies. A child process exiting zero does not prove approvals, recovery or delivery.
4. For a script invocation it is the script name/path, not the first user argument. Special invocation modes differ. Validate the strings in `argv[1:]` before selecting work or constructing outputs.
5. A venv isolates package environments by default; it does not secure secrets, eliminate OS differences or reproduce unrecorded versions. Activation is optional when the interpreter path is explicit. The `-I` failure in this review demonstrates that available user packages may disappear under isolation.
6. Structured stdout can be consumed separately from human diagnostics on stderr. Exit status provides another contract. The actual child success produced one JSON result and no stderr; invalid syntax produced status 2, a fixed diagnostic and no stdout.
7. A fixed executable plus argument list preserves data boundaries without shell expansion. It does not make a dangerous executable harmless. Handle timeout/nonzero status deliberately; a Windows shell builtin is not automatically a standalone executable.
8. Include operation/run identity, timestamp where appropriate, scope, severity and outcome. Bound and redact context. The workbook logs counts and exception type, omitting source labels and a synthetic private exception message; complete production diagnostics need a governed route.
9. Process liveness does not prove useful work. Compare the last successful semantic result with the expected schedule and maximum age. The workbook measures duration and counts but does not implement durable last-success monitoring.
10. A rerun should converge to the intended state. Canonical sorting/serialization makes unchanged inputs skip replacement; the probe verifies unchanged bytes and modification time. Concurrency, notification delivery and power-loss durability still require separate design.
11. CSV quoting permits commas, quotes and newlines inside fields. A parser handles that syntax; schema, numeric conversion, extra/missing columns and duplicate identifiers still need validation. Presentation prefixes deliberately change the display export and are not a universal spreadsheet safety claim.
12. Valid JSON can have unexpected fields, duplicate keys, wrong types or unsuitable values. This workbook rejects these cases under a bounded schema, including booleans as counts and non-finite numbers. Trust in the sender and legal permission are separate questions.
13. A documented API usually provides a clearer structured contract than presentation HTML. It still has versions, limits, auth and outages. Static HTML parsing does not execute browser JavaScript, and a changed selector can silently miss data unless cardinality is checked.
14. Check expected status, redirect policy, media/encoding, bounded body, decoding and schema before committing. A valid JSON body from HTTP 500 is still a failure. Connect/read timeouts are not a complete wall-clock budget, and a 429 requires a deliberate retry/defer policy.
15. `schedule` needs a running Python process and does not supply durable job persistence or concurrent execution by itself. The package was not installed or run here; an OS scheduler launch and missed-run behavior remain separate verification.
16. Use a lock/lease appropriate to all participating processes and release/recovery rules, plus idempotency. The workbook only demonstrates same-process nonblocking lock behavior; it neither wraps `run_once` with it nor proves a cross-process scheduler policy.
17. Encode for the actual output context. `html.escape` is appropriate for the demonstrated text nodes, while script, URL, CSS and arbitrary markup contexts have different requirements. Generating a report is separate from securely storing or delivering it.
18. The credential page still describes limited beta delivery while the syllabus is active. Confirm availability, outline and applicable policies before committing time or money. A calendar date or unverified third-party alignment claim does not establish release or readiness.

## Readiness checklist

- [ ] I can identify suitable work and calculate a transparent ROI with limitations.
- [ ] I can run/configure a CLI script and invoke allow-listed tools safely.
- [ ] I can design logs/metrics that reveal semantic success and failure without secrets.
- [ ] I can perform idempotent, bounded, recoverable file/CSV/JSON automation.
- [ ] I can fetch permitted APIs/pages with timeouts, validation, rate/terms awareness, and robust parsing.
- [ ] I can schedule without overlap and produce proportionate notifications/reports.
- [ ] I completed the integrated lab and tested failure paths.
- [ ] I rechecked beta availability and objectives before purchase.

**Execution status:** The exact workbook passes its bounded checks. The complete integrated lab and independent human content/accessibility review remain pending. In particular, `schedule` and `plyer` are unavailable; venv activation, Unix permission changes, persistent scheduler runs, actual email/desktop delivery and external API/TLS/authentication behavior were not tested. A direct objective-monitor timeout remains visible despite manual syllabus confirmation.

## Source and freshness notes

- [Official PCEA syllabus](https://pythoninstitute.org/pcea-exam-syllabus) controls the six-block map and labels its syllabus active.
- [Official PCEA credential page](https://pythoninstitute.org/pcea) labels the offering limited availability/small market trial/beta; this more conservative status is used here.
- Technical behavior: [Python stdlib](https://docs.python.org/3/library/), [Requests](https://requests.readthedocs.io/en/latest/), [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), and [schedule](https://schedule.readthedocs.io/en/stable/).

## Places to learn

This is not a complete list and is not intended to be consumed in full. The reviewed credential page did not list an aligned course; that observation does not prove no such resource exists elsewhere. Choose selected documentation and one bounded project. All hour ranges below are author planning estimates, not measured completion times, publisher guarantees or proof of exam readiness.

| Resource | Access | Estimated time |
|---|---|---:|
| [PCEA syllabus](https://pythoninstitute.org/pcea-exam-syllabus) | Free canonical outline; all detailed objectives/MQC read, full PDF pending | 3–5 hours plus availability rechecks |
| [Python standard library reference](https://docs.python.org/3/library/) | Free index; selected pinned 3.13 manuals support this workbook | 15–25 selected hours |
| [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) | Author-hosted third-edition web book is free to read; broader than PCEA | Select 20–35 hours |
| [Requests documentation](https://requests.readthedocs.io/en/latest/) | Free project docs; selected quickstart/session/streaming/timeout contracts reviewed | 4–8 selected hours |
| [Beautiful Soup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) | Free primary manual; selected parser/text/selector passages reviewed | 4–8 selected hours |
| [schedule documentation](https://schedule.readthedocs.io/en/stable/) | Free project landing; linked tutorials and runtime exercise pending | 2–4 selected hours |
| [Python Automation Cookbook, Third Edition](https://www.packtpub.com/en-us/product/python-automation-cookbook-9781806702893) | Paid Packt book; public metadata and table of contents reviewed, not complete chapters | Select 20–35 hours |

The complete author landing for **Automate the Boring Stuff** identifies the current third edition and its free web reading, with chapters on files, CLI deployment, scraping, CSV/JSON/XML, scheduling and notifications. Linked chapters and companion workbook were not completed. Its video-course description follows much of the **first edition**, so do not assume the video and third-edition text are identical. No account, purchase, review-copy request or discount redemption occurred.

The former O'Reilly link ending in ISBN `9781803247300` could not be verified and is removed from the recommendation. Packt's confirmed listing identifies Jaime Buelta's third edition, June 29, 2026, 676 pages, print ISBN `9781806702893`. Its contents include relevant file/API/report/testing material alongside broader AI/MCP topics that are not additional PCEA objectives. The page labels 19 chapters while the visible numbered sequence runs 1–17 followed by other-books/index entries. Selected metadata, the complete visible contents list and only an opening portion of the public sample were read; full book content, paid entitlements and code execution were not reviewed. The old catalog entry is retained with an unverified-link note, not silently reassigned to another ISBN.

Because delivery remains beta, third-party exam-alignment claims need particular care. Use the public official outline and original exercises; avoid recalled exam questions. Direct source receipts, manual fallback boundaries, dependency versions and remaining work are documented in the [September 30 review](../docs/research/2026-09-30-pcea-30-01-deep-review.md).
