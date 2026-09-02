---
exam_code: 200-901
vendor_id: cisco
official_blueprint: https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccnaauto.html
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-02
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-02
---

# CCNA Automation (200-901 CCNAAUTO) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** Public objectives, citations, links, volatility labels, and exam-integrity compliance were checked September 2, 2026. See the [coverage record](../docs/SOURCE-VALIDATION.md#200-901-coverage-record). Cisco's [exam page](https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccnaauto.html) and [detailed v1.1 blueprint](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-901-CCNAAUTO_v.1.1.pdf) are authoritative.

**Current baseline:** 200-901 CCNAAUTO v1.1, six domains weighted 15/20/15/15/20/15<br>
**Upcoming change:** No replacement or retirement announcement found as of September 2, 2026<br>
**First-party inconsistency:** The detailed blueprint and 2026 training overview say v1.1, but the exam landing page still renders v1.0; the exam page/list includes English and Japanese while the certification page lists English only. Use v1.1 for scope and verify language in the scheduling interface.<br>
**Credential history:** Cisco renamed DevNet Associate to CCNA Automation on February 3, 2026. Older v1.1 learning material may still use `DEVASC` or “DevNet Associate”; validate its objectives and product names rather than rejecting it solely for the former brand.

## How to use this guide

Study every automation workflow as intent → data/API contract → authentication and authorization → code/configuration → test → review → controlled execution → evidence → rollback. Do not stop at recognizing syntax: construct small requests and scripts, interpret responses, explain failure behavior, and make unsafe actions fail closed.

Build a disposable local environment with Git, Python, a virtual environment, `requests`, a YAML library, a test runner, Bash or an equivalent shell, a REST client, and Docker where permitted. Use mocks first, then Cisco's authorized sandboxes. Never put a production token in source code, logs, screenshots, shell history, or a shared collection.

> **About related items:** A `Related item:` callout adds prerequisite, operational, architectural, or adjacent context. It is supporting knowledge, not a claim that the item appears verbatim in the published objectives.

## Objective map

| Domain | Weight | Proof to produce |
|---|---:|---|
| Software Development and Design | 15% | Convert XML/JSON/YAML to Python structures; explain TDD, methods, patterns and Git; resolve a simple merge conflict |
| Understanding and Using APIs | 20% | Build and troubleshoot documented HTTP requests, authentication and Python `requests` calls; distinguish REST/RPC and sync/async behavior |
| Cisco Platforms and Development | 15% | Select platform/resource/API, use an SDK or reference to construct code, and reason about YANG/NETCONF/RESTCONF |
| Application Deployment and Security | 15% | Explain deployment choices and CI/CD; test Python, interpret Dockerfiles, operate local containers, protect secrets/data, identify common web risks |
| Infrastructure and Automation | 20% | Interpret Python/Ansible/Bash/YANG/diff/sequence artifacts and design a reviewed, testable, idempotent infrastructure workflow |
| Network Fundamentals | 15% | Read a topology and explain MAC/VLAN/IP/routes/gateways, planes, services/ports, connectivity faults and application-facing constraints |

---

## 1. Software Development and Design — 15%

### Data representations and parsing

JSON maps naturally to Python dictionaries, lists, strings, numbers, booleans and `None`. YAML adds human-friendly features but indentation and implicit types can surprise; use a safe loader for untrusted input. XML represents elements, attributes and text in a tree and commonly uses namespaces. Compare them by structure, schema/tooling, readability, comments, ordering expectations and API contract—not by a blanket “best” format.

Parsing is a boundary. Decode transport bytes correctly, validate content type, parse, validate required fields and types, normalize into an internal model, and handle missing/null/empty/extra values deliberately. Serialization reverses the process but does not prove that the receiver accepts your schema. Keep samples that test valid, incomplete, malformed and unexpected payloads.

```python
from dataclasses import dataclass
import json

@dataclass(frozen=True)
class Device:
    device_id: str
    reachable: bool

def parse_device(text: str) -> Device:
    raw = json.loads(text)
    if not isinstance(raw.get("id"), str):
        raise ValueError("id must be a string")
    return Device(raw["id"], bool(raw.get("reachable", False)))
```

### Development method, structure and tests

Waterfall emphasizes planned sequential phases; agile uses short feedback cycles; lean reduces waste and optimizes flow. A team can combine practices. Pick based on uncertainty, risk, feedback cost, regulation and deployment constraints, then explain how requirements and evidence remain traceable.

Test-driven development is the red → green → refactor loop: express a failing behavior, implement the smallest passing change, then improve structure without changing behavior. Unit tests isolate a function; integration tests exercise boundaries; end-to-end tests validate a workflow. For network automation, also test idempotency, dry-run/diff, partial failure, retry limits, timeout, authorization denial and rollback.

Functions isolate reusable behavior; classes bind state and behavior where that model helps; modules/packages create ownership and dependency boundaries. MVC separates model, view and controller responsibilities. Observer allows subscribers to react to events without the producer knowing their concrete behavior. Patterns are tradeoffs, not requirements to force onto small scripts.

### Git as the change record

Know `clone`, stage/add/remove, `commit`, `push`, `pull`, branch, merge, conflict resolution and `diff`. A safe infrastructure change is a small branch with an issue/intent, tests, generated diff, peer review and traceable commit. Resolve conflicts by understanding both intents and retesting—not by choosing “ours” or “theirs” blindly. Do not commit credentials, generated secrets or large captured responses.

**Related item:** A commit records content and ancestry; a branch is a movable name; a remote-tracking reference reflects the last fetched remote state. This distinction makes divergence and merge failures easier to explain.

---

## 2. Understanding and Using APIs — 20%

### Construct a request from documentation

Start with base URL/version and resource path. Select method and encode path/query parameters, headers and body exactly as documented. Add authentication without exposing it. Set `Accept` and, when sending a body, `Content-Type`. Define timeout, pagination, rate-limit and retry behavior. Validate TLS; do not “fix” certificate errors by globally disabling verification.

HTTP methods commonly express read (`GET`), create/action (`POST`), replace (`PUT`), partial update (`PATCH`) and delete (`DELETE`). Idempotency means repeating the same request has the same intended effect, not that every response is byte-identical. Never infer safety solely from the verb; follow the specific contract.

Interpret the full response: status describes the outcome class, headers carry metadata such as content type, pagination, location, caching and rate limits, and the body carries representation or structured error. Common classes are 2xx success, 3xx redirection, 4xx request/auth/resource/rate problems and 5xx provider faults. Distinguish malformed/authentication/authorization/not-found/conflict/rate/timeout problems using the documentation and error body.

```python
import os
import requests

def list_devices(base_url: str) -> list[dict]:
    token = os.environ["LAB_API_TOKEN"]
    response = requests.get(
        f"{base_url.rstrip('/')}/devices",
        headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
        params={"limit": 50},
        timeout=10,
    )
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload.get("items"), list):
        raise ValueError("unexpected response schema")
    return payload["items"]
```

This example still needs pagination, bounded retry, logging with redaction and tests before production. Retry only transient and safe/idempotent operations unless the API supplies an idempotency mechanism. Add exponential backoff and jitter, honor `Retry-After`, and cap total attempts.

### Authentication and API styles

Basic authentication sends a reusable credential encoding, not encryption; require TLS. API keys identify/cap an integration but need least privilege, secure storage, rotation and revocation. Custom/bearer tokens often expire and may encode scopes. Keep authentication (who/what) distinct from authorization (allowed action) and audit attribution.

REST commonly manipulates resources through uniform HTTP semantics. RPC expresses operations/functions. Synchronous interaction waits for completion; asynchronous interaction returns an acknowledgement/job/event and requires status, callback or subscription handling. These axes can combine.

Webhooks deliver events to a registered endpoint. Verify signature and timestamp, reject replay, acknowledge within the provider's window, queue work, make processing idempotent, deduplicate event IDs, handle out-of-order delivery and monitor dead letters. Never treat an inbound JSON body as trustworthy because it arrived at the expected URL.

**Related item:** Polling controls cadence but costs repeated requests and adds latency; webhooks reduce polling but introduce endpoint availability, authenticity, replay and delivery-order responsibilities.

---

## 3. Cisco Platforms and Development — 15%

### Select platform, interface and resource

Know the purpose rather than memorizing every endpoint:

- Meraki Dashboard manages cloud-controlled organizations, networks, devices and clients.
- Cisco Catalyst Center provides campus inventory, assurance, intent and automation APIs.
- ACI exposes data-center fabric policy and operational objects through APIC.
- Cisco Catalyst SD-WAN provides controller-based WAN policy, inventory and operations.
- NSO models and orchestrates multi-vendor services with transactional behavior.
- UCS Manager and Intersight manage compute/infrastructure domains.
- Webex covers spaces, participants, messages and devices; Unified CM integrations include AXL configuration and UDS user-facing services.
- Security surfaces include XDR, Secure Firewall/Firepower, Secure Connect, Secure Endpoint, ISE and Secure Malware Analytics.
- IOS XE and NX-OS offer device-level interfaces whose supported RESTCONF/NETCONF/REST/CLI details depend on platform and release.

Select an API/SDK from requirement, source of truth, desired scope, supported version, authorization model, rate/scale constraint and rollback behavior. Given SDK documentation, construct client initialization, authentication, arguments, call, response validation, exceptions and cleanup. Do not guess a method name from another SDK version.

Cisco DevNet documentation gives API references; Sandbox gives authorized environments; Learning Labs teach focused workflows; Code Exchange offers sample projects; support/forums help diagnose; choose the resource that matches the task. Treat samples as starting points and inspect licenses, dependencies, secrets, versions and destructive behavior.

### Model-driven programmability

YANG defines hierarchical configuration/state data, types, constraints and operations. NETCONF exchanges XML-encoded RPCs and can work with datastores, filters, validation, locking and commit behavior. RESTCONF exposes YANG-modeled data using HTTP and commonly XML or JSON encodings. A path is meaningful only with the correct module, namespace, datastore and platform implementation.

Interpret a basic YANG tree by separating containers/lists/leaves, keys, type/range, config versus operational state and module prefix. For a NETCONF or RESTCONF result, match returned hierarchy to the model; absence can mean unsupported, filtered, unauthorized, empty or wrong path. Capture error tags/status/body rather than retrying blindly.

The blueprint may provide documentation and ask you to construct code that lists devices or clients/hosts, or manages Webex spaces/participants/messages. The transferable method is documentation → required auth → endpoint/SDK method → parameters/pagination → schema → error handling → minimal test → redacted evidence.

**Related item:** Controller-level management expresses broader intent and inventory context; device-level management can expose precise features. Choose deliberately, and avoid two authorities fighting over the same configuration.

---

## 4. Application Deployment and Security — 15%

### Deployment and delivery choices

Private, public and hybrid cloud differ in ownership, control, elasticity, connectivity, data location and operating responsibility. Edge computing places compute near devices/users/data to reduce latency or tolerate intermittent upstream connectivity, but distributes security, patching and observability.

Bare metal provides direct hardware control; virtual machines isolate complete guest operating systems; containers package processes while sharing a host kernel. Pick based on isolation, startup/density, hardware access, portability, operational tooling and risk. A container image is immutable input; a running container adds writable/runtime state.

A CI/CD pipeline commonly includes source, build, dependency and secret scanning, unit/integration tests, artifact/image production, signed provenance, registry, deployment, post-deployment validation and rollback/promotion. Separate build from deploy identity. Promote the same tested artifact rather than rebuilding per environment.

Be able to interpret a Dockerfile: base image, working directory, copied files, package install, user, environment, exposed port, entrypoint and command. Pin trusted dependencies/images, minimize layers and contents, run as non-root when possible, exclude secrets/build clutter, scan the result, and keep runtime configuration outside the image. Locally know pull/build/list/run/inspect/logs/stop/remove operations and port/volume/environment mapping.

### Test and secure the application

Construct a focused Python unit test using known input and an explicit expected result. Mock the network boundary, not the logic under test. Assert outgoing method/path/header/body and handling of success, schema error, 401/403, 404/409, 429 and transient 5xx/timeout. A test that only checks “no exception” is weak evidence.

Protect secrets using a secret manager or appropriately protected runtime injection, not source or image layers. Encrypt data in transit and at rest, restrict data collection/retention, redact logs, validate inputs and authorize every sensitive operation. Firewall rules constrain flows; DNS resolves names; load balancers distribute/health-check traffic; reverse proxies terminate/front applications and can enforce routing/security controls. A failure at any layer can resemble an application fault.

Understand examples from the OWASP web-risk set: injection mixes untrusted data with commands/queries; XSS executes attacker-controlled content in a user's browser; CSRF induces an authenticated browser to send an unwanted request. Use parameterization, contextual output encoding, content/security controls, anti-CSRF design and SameSite/session protections as appropriate. Never practice exploitation outside a deliberately vulnerable, isolated, authorized lab.

Bash scope includes navigation and file operations plus environment variables. Quote variables, check exit status, enable safe failure behavior deliberately, avoid printing secrets and test paths. DevOps joins development and operations through shared ownership, feedback, automation, observability and incremental, reversible change; it is not a synonym for a toolchain.

**Related item:** A healthy service process does not prove a reachable application. Validate DNS, route, NAT/VPN/proxy, firewall, listener, TLS, reverse proxy/load balancer and application dependency layers independently.

---

## 5. Infrastructure and Automation — 20%

### A controlled workflow

Model-driven automation separates declared intent/data from imperative screen scraping and supports validation/reuse. Infrastructure as code makes desired state reviewable, versioned, testable and repeatable. Declarative tools describe outcome; imperative code describes steps. Idempotency means convergence without repeated unintended change.

Ansible commonly runs ordered YAML tasks against inventory using modules; interpret hosts, variables, privilege, tasks, handlers, conditionals and reported changed/failed state. Terraform builds a dependency graph from declarative configuration and tracks managed state; protect and coordinate that state. Cisco NSO models services and can coordinate transactional multi-device changes. Tool capability does not replace ownership, policy, tests or rollback.

A safe infrastructure pipeline validates syntax/schema, lints, tests code, renders proposed changes, uses authorized simulation, requires review/approval based on risk, executes in a bounded canary, verifies service/telemetry, and stops or rolls back on failed gates. Separate read/test/deploy credentials and preserve evidence.

Cisco Modeling Labs emulates network topologies; pyATS provides Python-based test/validation and parsers. Use simulation to test logic and failure paths, but account for differences from hardware/software releases and external dependencies.

### Interpret automation artifacts

For Python using ACI, Meraki, Catalyst Center or RESTCONF, trace inputs/authentication → request → pagination/transformation → decision → write → verification → exception. For Bash, trace quoting, variables, command exit behavior and file/user/package effects. For an Ansible playbook, identify inventory target, module, variables, desired state, privilege, handler and idempotency.

NETCONF/RESTCONF output must be related to the YANG model and requested path/filter. A unified diff uses context plus removed (`-`) and added (`+`) lines; determine the effective change and whether order/indentation is semantic. A sequence diagram orders actors and calls over time; identify synchronous/asynchronous behavior, authentication, retry, callback and failure gaps.

Code review should verify intent, scope, readability, tests, secrets/dependencies, error and retry behavior, concurrency, least privilege, blast radius, observability, idempotency and rollback. Review the generated infrastructure diff as well as the source diff.

**Related item:** “Dry run” and “check mode” are tool-specific predictions. They reduce risk but may not model runtime side effects, unsupported modules, race conditions or external systems; follow with bounded validation.

---

## 6. Network Fundamentals — 15%

### Read the path before automating it

A switch forwards frames within a VLAN using MAC learning. A router forwards packets between IP networks using the routing table. A firewall enforces flows; a load balancer presents a service and distributes requests. A host decides whether a destination is local from address/prefix and otherwise sends to its gateway. VLAN tags separate Layer 2 broadcast domains; routes and gateways connect Layer 3 networks.

Given a topology, annotate source/destination addresses and ports, VLANs, gateways, routes, NAT, firewall/proxy/VPN and service/listener. Management plane handles administration, control plane learns/decides topology or policy, and data plane forwards traffic. Controller-based systems may centralize control intent while distributed devices still forward.

DHCP supplies addressing parameters; DNS maps names and records; NAT translates address/port information; SNMP supports monitoring/management; NTP synchronizes time. Recognize SSH 22, Telnet 23, HTTP 80, HTTPS 443 and NETCONF-over-SSH 830 as common defaults, while remembering services can use different ports.

Application connectivity diagnosis follows evidence: name resolution → local address/route → path/VPN/proxy → NAT/firewall → listener/TLS → authentication/API → dependency. A 200 HTTP response from the wrong endpoint is not success; a TCP timeout differs from connection refused, TLS failure or HTTP denial.

Network constraints shape applications: latency affects round trips and synchronous chains; jitter affects real-time traffic; loss triggers retransmission; bandwidth limits throughput; MTU/fragmentation breaks particular payloads; intermittent paths require queueing/retry; NAT/proxy/firewall changes reachability; asymmetric paths complicate stateful inspection. Design timeouts, pooling, backoff, batching, compression and observability from measured behavior.

**Related item:** Automation can repeat a mistake faster. Preserve a known-good state, bound targets/concurrency, test negative paths, require review, observe during rollout and prove restoration.

---

## Integrated scenarios

### Scenario 1: Read-only inventory collector

Requirement: collect device identity from two Cisco platforms without configuration access. Define a normalized schema, least-privilege tokens, platform adapters, pagination, timeouts and redacted logs. Unit-test fixture parsing; run read-only against an authorized sandbox; compare counts and rejected records; store evidence without credentials. Explain how one platform's 429 and another's malformed record remain isolated.

### Scenario 2: Reviewed VLAN workflow

Requirement: add a VLAN consistently to a lab. Put intent in Git, validate inputs, render a change, test in CML, inspect unified/configuration diff, require approval, canary one device, verify VLAN/path/service and then expand. Define wrong-interface, lost-management and partial-failure stops plus rollback. Explain controller- versus device-level ownership.

### Scenario 3: Webhook-driven incident notification

Requirement: transform an authenticated network event into a Webex notification. Verify signature/timestamp, deduplicate event ID, enqueue, redact sensitive fields, map severity, call Webex with scoped identity, retry bounded transient failures, dead-letter permanent errors and audit correlation IDs. Test replay, out-of-order, 429, expired token and Webex outage.

## Hands-on evidence labs

1. **Formats and Git:** Parse equivalent XML/JSON/YAML fixtures into one model. Add malformed cases, commit on a branch, create and correctly resolve a controlled conflict, and inspect the unified diff.
2. **HTTP contract:** With a local mock API, construct GET/POST/PATCH calls, authentication, pagination and schema validation. Capture behavior for 2xx, 400, 401, 403, 404, 409, 429, 5xx and timeout.
3. **Cisco read-only API:** Use an authorized Always-On sandbox to list devices or clients. Keep the token outside code; save sanitized request/response structure, pagination and error evidence.
4. **YANG and model-driven query:** Read a small YANG tree, identify keys/config/state, perform an authorized RESTCONF or NETCONF read, and map response nodes to the model.
5. **Containerized collector:** Write and interpret a minimal Dockerfile, build and run locally as non-root where possible, inject runtime configuration safely, test/log/inspect, scan, stop and remove it.
6. **Infrastructure review:** Interpret a Python workflow, Ansible playbook, Bash script, YANG result, unified diff and sequence diagram. Record intent, side effects, idempotency, privilege, failure and rollback for each.
7. **Network-aware failure:** In an isolated lab, introduce one DNS, route, port/firewall, proxy or NAT fault at a time. Capture symptoms from transport through HTTP and show why application retry cannot repair every class.
8. **Mini delivery pipeline:** Combine lint, unit tests, secret scan, mocked integration, proposed diff, approval, bounded sandbox execution, post-check and rollback. Produce a short evidence packet tied to a Git commit.

## Readiness checks

1. When would you select JSON, YAML or XML, and what parsing risks differ?
2. How do transport decoding, parsing, schema validation and normalization differ?
3. What does red → green → refactor mean?
4. Which tests prove an automation is safe to repeat?
5. When do functions, classes and modules improve a script?
6. What responsibilities do MVC and Observer separate?
7. Can you clone, branch, stage, commit, diff, merge and resolve a conflict?
8. Why must a conflict be resolved by intent rather than marker removal?
9. Can you build an HTTP request strictly from API documentation?
10. How do method safety and idempotency differ?
11. What do status, headers and body each tell you?
12. How do 401, 403, 404, 409, 429 and 5xx drive different actions?
13. What protections belong around retries?
14. How do Basic, API-key and token authentication differ operationally?
15. When is RPC a better description than REST?
16. What changes when an operation is asynchronous?
17. How do you authenticate, deduplicate and replay-protect a webhook?
18. Can you construct a tested Python `requests` call without leaking a token?
19. Which Cisco platform owns the requirement in a given scenario?
20. When should you use documentation, Sandbox, Learning Labs, Code Exchange or support?
21. Can you construct an SDK call from the supplied version's documentation?
22. How do YANG, NETCONF and RESTCONF relate?
23. Can you interpret a YANG list key and config/state leaf?
24. How would you diagnose an empty NETCONF/RESTCONF result?
25. Why choose edge, private, public or hybrid deployment?
26. What tradeoffs distinguish bare metal, VM and container?
27. Can you trace a secure CI/CD pipeline and its identities?
28. Can you interpret and improve a Dockerfile?
29. Can you construct a focused Python unit test with a mocked API?
30. Which controls address secrets, encryption and data handling?
31. How do injection, XSS and CSRF differ?
32. What roles can firewall, DNS, load balancer and reverse proxy play?
33. Can you make a Bash script fail safely without printing secrets?
34. How do model-driven automation, IaC and idempotency connect?
35. What operational differences matter among Ansible, Terraform and NSO?
36. Can you interpret Python, Bash, Ansible, YANG, unified diff and sequence artifacts?
37. What must a code/infrastructure review prove before execution?
38. How do CML and pyATS reduce—but not eliminate—risk?
39. Can you annotate MAC/VLAN/IP/gateway/route/NAT/port on a topology?
40. How do management, control and data planes differ?
41. What do DHCP, DNS, NAT, SNMP and NTP provide?
42. Which default ports belong to SSH, Telnet, HTTP, HTTPS and NETCONF?
43. Can you isolate DNS, route, NAT, blocked-port, proxy and VPN failures?
44. How should latency, jitter, loss, bandwidth and MTU change application design?
45. Can you explain the credential's old DEVASC and current CCNAAUTO names without assuming content equivalence blindly?
46. Did you recheck the live version, language and scheduling interface?

### Check key

- **Ready:** You can demonstrate or explain it from fresh evidence without prompts.
- **Review:** You recognize it but cannot yet produce the request, code, interpretation or failure diagnosis.
- **Gap:** You guessed, memorized a label, or depended on an answer bank. Return to documentation and a safe lab.

## Places to learn

This is not a complete list, and it is not meant to be consumed in full. Pick a primary format, use the official blueprint as the checklist, add labs, and choose only the supplements that close measured gaps. Durations and availability were checked September 2, 2026 and can change.

| Resource | Access | Estimated time | Best use and freshness boundary |
|---|---|---:|---|
| Cisco exam page + v1.1 blueprint | Public | 2–4h first map; 30–60m weekly | Start with the links at the top. The PDF is the detailed scope authority; the landing-page v1.0 label is a known inconsistency. |
| [Cisco CCNAAUTO training](https://www.cisco.com/site/us/en/learn/training-certifications/training/courses/ccnaauto.html) | Cisco U. paid/subscription; overview public | 32h30m; instructor-led commonly 5 days | Cisco's [dated roundup](https://blogs.cisco.com/learning/evolve-and-optimize-your-skills-for-the-ai-networking-era) supplies the path duration; the training page and [public PDF](https://www.cisco.com/c/dam/en_us/training-events/training/courses/ccnaauto.pdf) expose objectives/labs. Verify the selected delivery. |
| [Cisco DevNet Sandbox](https://developer.cisco.com/docs/sandbox/) | Free account | 12–25h estimate | Use Always-On for immediate read/API work and reservations for private/full-access labs. Availability, versions, VPN needs and resets vary. |
| [Learn with Cisco prep series](https://www.youtube.com/watch?v=wunfbjsGSh4) | Public | 12–24h estimate as series develops | First-party live coding/Q&A on REST, formats, Git, RESTCONF/NETCONF and Python. Check playlist completeness against all six domains. |
| [Official Cert Guide, 2nd edition](https://www.pearson.com/en-us/subject-catalog/p/devnet-associate-devasc-200-901-official-cert-guide/P200000012978/9780135368114) | Paid; forthcoming September 15, 2026 | 25–40h estimate + practice | Pearson's page mixes DevNet and current CCNA Automation names. Verify publication and edition before purchase. |
| [LinkedIn Learning DEVASC 1.1 cert prep](https://www.linkedin.com/learning/cisco-certified-devnet-associate-devasc-1-1-200-901-cert-prep) | Paid/trial | 13h02m + 10–20h labs | Six-domain map with transcripts/exercise files; March 2024 former-name course. Gap-check current platform names. |
| [O'Reilly DevNet Associate video](https://www.oreilly.com/videos/cisco-certified-devnet/9781835883341/) | Paid | 15h44m + 12–20h labs | January 2024 six-domain supplement; close 2025/2026 platform-name deltas from first-party sources. |
| [Udemy CCNA Network Automation](https://www.udemy.com/course/cisco-certified-devnet-associate-course-netdevops/) | Paid | 10h06m + 12–20h labs | Updated April 2026 with Python/Linux/API/Git/Docker/NETCONF/RESTCONF/Ansible labs. Verify reviews, maintenance and exact v1.1 coverage. |
| Cisco U. practice exam | Paid/subscription | 2h + 3–6h review | Access from the official exam page. Use explanations to locate gaps; a score is not proof of production skill. |

For every provider, verify revision, access model, lab availability and blueprint alignment before spending money. Avoid products that claim live questions, guaranteed pass, “actual exam” reproductions, or unexplained answer-only banks.
