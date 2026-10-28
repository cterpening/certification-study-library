# IBM Bob v2 certification intake — October 28, 2026

Added [C3000-006 IBM Bob v2 Developer Associate](../../guides/C3000-006-ibm-bob-v2-developer-associate.md)
to the research inventory, generated certification list, publishing catalog and three relevant
collections. This is a targeted addition; the older six IBM entries were not reverified.

## Research scope and source selection

Resolved the supplied LinkedIn short link to Ahmed Azraq's launch announcement, then used
[IBM's credential page](https://www.ibm.com/training/certification/ibm-certified-bob-v2-developer-associate-C9010800)
and [public exam API](https://www.ibm.com/training/credentials/getExam/C3000-006) as canonical sources.
The API confirms live credential C9010800 / exam C3000-006, 42 questions, 29 to pass,
90 minutes, English and US$200. These are October 28 observations, not future booking guarantees.
The record's last-modified date is October 21, 2026; no prerequisite exam, replacement or
withdrawal was listed. A last-modified date is not treated as an exam launch or blueprint-effective date.

Read the official 24-page preparation PDF reached through the credential page. Its signed
download expires, so the repository links to the stable credential page. The PDF is not
republished. The sample-test link was verified as present; its questions were not read or used
to write this guide's checks. No paid or authenticated assessment content was accessed.
The API's internal operational fields and generated signed download URLs are excluded from
the committed objective/status snapshots.

Additional online research covered current IBM Bob IDE and Shell documentation, the first-party
v2 architecture announcement, and an IBM Developer agent/MCP tutorial. Inspected topics include
prompts, initialization, tools, mode configuration, rules, skills, lifecycle hooks, context,
MCP transports, approvals, ignore files, code review, PR generation, rollback, Bobalytics,
API keys, Bobcoins, Enterprise and self-hosted operation. The guide registers 37 exact public
IBM URLs with authority, access and limitation notes in the source catalog. Search results
advertising actual exam questions or guaranteed passes were excluded. This was a bounded
first-party investigation, not an exhaustive course-market survey.

## Confirmed findings and remaining gaps

- **Exam scope confirmed:** six domains, weights 17/23/19/17/8/16, and 52 objectives.
  The objective/status monitor re-fetched the API and matched the saved snapshots with no errors.
- **Marketplace workflow unverified:** the exam blueprint includes downloading extensions from
  a marketplace. The official preparation PDF explicitly asks for product-team confirmation of
  a general-purpose VS Code Marketplace/Open VSX browser inside Bob IDE. It supplies related
  package/companion mechanisms, which do not establish such a browser. The guide preserves
  this uncertainty beside the objective and invents no installation menu. Next pass: inspect
  an installed current IDE and obtain product-specific documentation or support confirmation.
- **Task limits need client validation:** the blueprint includes Bobcoin task limits; the PDF's
  configuration discussion emphasizes context management. Current Shell docs expose max-cost
  and max-turns. The guide distinguishes context capacity, task budgets and subscription
  overage without asserting a universal UI, unit conversion or runtime enforcement result.
- **Transport discrepancy preserved:** the [transport documentation](https://bob.ibm.com/docs/ide/configuration/mcp/server-transports)
  begins with a three-transport list but later states standalone HTTP+SSE was removed. The
  guide follows the specific removal statement and distinguishes SSE inside Streamable HTTP.
- **Approval scopes distinguished:** task tool-group controls, global defaults/command rules,
  per-tool MCP allowances and one-time approvals are separate. Mode names and ignore rules
  are not evidence of an operating-system sandbox.
- **Client support notice:** the [IDE documentation](https://bob.ibm.com/docs/ide) directs an
  upgrade to 2.0.2+ and says support for 2.0.1 ends October 31, 2026. This is not an exam change.
- **Execution and review pending:** all eight product labs are proposed, not executed. No Bob
  account, IDE installation, paid Enterprise environment, key creation, PR publication or
  remote deployment was used. Product correctness and independent human review are not claimed.

## Objective coverage

Numbers below identify domain and item order in the public API snapshot, not guaranteed
numbering in every IBM preparation artifact. Section labels are exact guide subheadings.
The review ledger also records all 52 individual mappings.

| Public objective | Guide section |
|---|---|
| 1.1 Write effective prompts | Effective prompts and project initialization |
| 1.2 Initiate a project (AGENTS.md) | Effective prompts and project initialization |
| 1.3 Why use an MCP server | MCP and skill structure |
| 1.4 Define and Illustrate the structure of  Bob Skills | MCP and skill structure |
| 2.1 Use Bob file's system to read, create and modify project files | Files, tools, and default modes |
| 2.2 Highlight the purpose of the IBM Premium Packages | Premium packages and SDLC work |
| 2.3 Define the role of bobignore | Ignore files and project boundaries |
| 2.4 Define and differentiate between the 3 default Bob modes | Files, tools, and default modes |
| 2.5 How Bob selects LLM models | Architecture, model routing, and deployment |
| 2.6 Use Bob shell to perform AI-Assisted activities from the command line | Bob Shell and code functions |
| 2.7 Define the component of Bob architecture | Architecture, model routing, and deployment |
| 2.8 Explain IBM Bob as AI Development partner across the SDLC | Premium packages and SDLC work |
| 2.9 Describe Bob hybrid deployment capabilities | Architecture, model routing, and deployment |
| 2.10 Monitor Bob usage, activities, and Bobcoin consumption using Bobalytics | Bobalytics and Enterprise administration |
| 2.11 Explain how Bob optimize tokens consumption (intelligent routing) | Architecture, model routing, and deployment |
| 2.12 Identify different ways of using Code Functions | Bob Shell and code functions |
| 2.13 Integrate Bob with external tools and services through MCP and supported  integrations | MCP deployment and tool development |
| 2.14 Identify what components fill the context window | Context, rules, and usage |
| 2.15 Standardize Bob behavior with Rules | Context, rules, and usage |
| 3.1 Create, inspect, and refine a solution architecture and implementation plan before coding | Plan, implement, debug, and modernize |
| 3.2 Use literate code to create code from comments | Plan, implement, debug, and modernize |
| 3.3 Apply Bob core SDLC capabilities to understand, generate, modify, document, and automate development workflows | Plan, implement, debug, and modernize |
| 3.4 Distinguish when to use Modes, Skills, Rules, Hooks, and AGENTS.md | Choose the right customization |
| 3.5 Evaluate when to use Bob Shell versus Bob IDE | Bob Shell and code functions |
| 3.6 Evaluate when Bob should work alone versus with specialized tools or external applications | Specialized tools, agents, and delegated work |
| 3.7 Use subagents and subtasks to divide complex development work into focused parallel workstreams | Specialized tools, agents, and delegated work |
| 3.8 Modernize applications using Bob | Plan, implement, debug, and modernize |
| 3.9 Build AI agents using Bob | Specialized tools, agents, and delegated work |
| 3.10 Debug application problems and correct code defects with Bob debugging and documenting code | Plan, implement, debug, and modernize |
| 3.11 Utilize Code Review and Bob Findings | Code review and Bob Findings |
| 4.1 Familiarize self with tools: Read, command, subtask, MCP | Tool groups, task limits, mentions, and extensions |
| 4.2 Configure task limits for Bob coins | Tool groups, task limits, mentions, and extensions |
| 4.3 Utilize context mentions @ file | Tool groups, task limits, mentions, and extensions |
| 4.4 Download extensions from marketplace | Tool groups, task limits, mentions, and extensions |
| 4.5 Distinguish between local and remote MCP server deployment / transport options | MCP deployment and tool development |
| 4.6 Develop and add MCP tools to environment | MCP deployment and tool development |
| 4.7 Create a custom Bob Modes | Custom modes, skills, and rules |
| 4.8 Develop Bob skills | Custom modes, skills, and rules |
| 4.9 Create custom Bob rules global vs project | Custom modes, skills, and rules |
| 4.10 Generate pull requests and PR descriptions directly from your IDE | Pull requests |
| 5.1 Administer Bobalytics | Bobalytics and Enterprise administration |
| 5.2 Authenticate with API | API authentication |
| 5.3 Determine the features of enterprise plan | Bobalytics and Enterprise administration |
| 5.4 Define Bob Coins | Bobcoins, tokens, and spending controls |
| 5.5 Understand Token Usage for Prompting | Bobcoins, tokens, and spending controls |
| 6.1 Modify mode permissions in a context/task | Permissions and approval scope |
| 6.2 Reduce content poisoning | Context poisoning and secure development |
| 6.3 Identify and enable correct Permissions restrictions for projects | Permissions and approval scope |
| 6.4 Produce .bobignore file | Ignore files and project boundaries |
| 6.5 Apply correct permissions and understand approval workflows | Permissions and approval scope |
| 6.6 List the best security practices and capabilities for developing with Bob | Context poisoning and secure development |
| 6.7 Rollback changes | Rollback and recovery |

## Supplemental source discovery

A second October 28 search checked IBM Developer, IBM Bob docs/blog, IBM-owned GitHub
repositories and public workshop sites, plus exact video links. Added ten evaluated resources:
an external-audience workshop; Bob Level 3 courseware; Galaxium Travels; the Bob demo
collection; changelog-skill, architecture-diagram, MCP-server and actor-critic tutorials;
a workflow/context article; and a monolith-modernization walkthrough. They are linked with
scope, prerequisites, editorial time estimates and limitations in the guide's Places to learn.
The introductory workshop's 60-minute agenda and separate 30-minute presentation are
published durations. No other newly listed reading/practice estimate is claimed as a runtime.

Public source inspection found material caveats. Level 3 contains older setup and trial
details, while Galaxium main has changed since some exercises. The demo collection explicitly
disclaims ongoing maintenance, retains five older mode names, and has malformed front matter
and an inconsistent script path in its skill example. Its Apache-2.0 LICENSE and the workshop
license were inspected; no code or course content was copied. The MCP tutorial has different
tool names/result limits in prose and code and omits XML/formatting helpers. The security
tutorial's rules/compliance language is not treated as an assurance, and its example identity
header needs real authentication. These remain bounded optional practice resources, with
current product docs authoritative for behavior. None of the tutorials or demos was executed.

The PR-review short linked by IBM's workflow article was throttled by the video reader.
Its exact URL is queued in the source-candidate inbox; video contents, author metadata and
runtime remain unverified. The employee-targeted Power User workshop was inspected as a
lead but not added as an unrestricted learning path; it also contains older Shell syntax.
No exact certification-specific commercial course was verified in this bounded search.
These findings do not resolve the marketplace-browser gap.

All ten additional URLs returned HTTP 200. The guide now links **47 registered sources**;
the original 37 observations remain preserved and ten new health observations were appended.
Repository validation and resource synchronization passed. The strict site build is rerun
for these additional resources; the command output records its result.

## Validation evidence

- Objective snapshot SHA-256: `d4573e943742dfca30eb28ace0a1953957e412b90b8c4165c315cf9e617db5e3`.
- Read-only official-objective monitor: unchanged objective and status hashes; zero errors.
- Initial link-health check: **37/37 HTTP 200**, zero blocked, missing or error responses. Reachability
  is not a claim of product execution or independent accuracy review.
- Repository validation passed; **188 unit tests passed**, followed by **14 site-preparation tests**
  after adding this note to the publication allowlist.
- Strict MkDocs build passed. Generated-site validation passed across **467 HTML pages**;
  the Bob guide appears in the IBM catalog and all three selected collections.
- Learning-resource synchronization is current, and the patch passes whitespace checks.
  Existing exam, seed, source, health and review rows were compared with HEAD and preserved.
- Objective snapshot bytes use LF line endings, with a Git attribute preserving them across
  platforms so the recorded SHA-256 survives Windows/Linux checkout normalization.

The guide's source-validation label records traceability, visible uncertainty and objective mapping.
It does not close the marketplace gap or assert that proposed exercises have run successfully.
