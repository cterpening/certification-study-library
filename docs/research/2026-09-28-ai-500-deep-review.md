# AI-500 deep review — September 28, 2026

The [AI-500 guide](../../guides/AI-500-designing-implementing-multi-agent-ai-solutions.md)
was read in full and mapped to **55 detailed objectives across twelve groups**.
It now includes six worked examples, ten labs, 44 answered checks and two focused
Microsoft engineering blog exercises. Nineteen offline assertions passed, including
execution of the guide's original standard-library replay example.

This is same-context AI research and repair, with independent human review pending.
No cloud resource, identity, policy, tool, SDK/framework, model, migration or paid
question bank was executed or accessed. The fake action service is an in-memory,
single-process illustration, not a test of durable storage, concurrency or actual
process-crash recovery. Cloud and framework labs remain learner exercises.

## Exam and learning baseline

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500)
retains its July 16, 2026 page date without a separate skills-effective date.
Objective and status hashes are unchanged; accepted snapshots were preserved.
The [exam](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-500/)
still describes beta, English availability and no Practice Assessment. The
[credential](https://learn.microsoft.com/en-us/credentials/certifications/multi-agent-ai-solutions-expert/)
still requires AI-103. No fixed exam duration or exact GA date was verified.

The four Learn paths expose **17 modules: 4 + 4 + 4 + 5**. Their older first-three
duration total is now historical because the fetched pages do not expose those
totals. The guide's 14–20-hour path and 16–30-hour lab budgets are editorial estimates.
The [four-day English course](https://learn.microsoft.com/en-us/training/courses/ai-500t00)
still lists September 30 availability, two days after this review.

The public [Pluralsight syllabus](https://www.pluralsight.com/courses/microsoft-foundry-building-intelligent-applications)
identifies Clint Bonnett, February 13, 2026 and 1h 02m. The public
[O'Reilly live outline](https://www.oreilly.com/live-events/hands-on-microsoft-foundry/0642572231088/0642572231071/)
by Razi Rais totals four instructional hours before breaks; a current occurrence
was not verified. The O'Reilly book and Udemy practice-test pages were directly
access-blocked. Udemy's indexed description advertises 100 questions and an August
update; its August 22 blueprint-update claim remains uncorroborated. Paid content,
originality and objective coverage were not inspected. Bounded catalog searches
did not verify a complete current AI-500 Pluralsight path, Whizlabs course or
MeasureUp test; this does not prove absence.

The earlier certification announcement returned HTTP 200 with only a title/content
shell. Its previously recorded October GA target is retained as historical, not
fresh article-body verification or evidence that launch occurred.

## Objective coverage

Every detailed bullet has a hashed guide mapping in the operation record.

| Objective group | Count | Teaching and evidence |
|---|---:|---|
| Logical architecture | 8 | Decomposition, autonomy, HAX, topology, protocols, memory and models |
| Technology components | 7 | Identity, persistence, compute, telemetry, monitoring and development environment |
| Advanced prompts | 3 | Examples, dynamic context, defense, lifecycle and fine-tuning decisions |
| Memory/context/knowledge | 4 | Token budget, authenticated scope, deletion, retrieval and filter recall |
| Tools | 4 | Function contracts, MCP, APIM capability, errors and result validation |
| Orchestration | 8 | Patterns, approval, caches, quotas, A2A, frameworks, Transformers and middleware |
| Evaluation | 2 | Human calibration, component measures, stored outputs and critical slices |
| Optimization | 3 | Critical path, rate limits, continuity failures and improvement loops |
| Observability | 5 | Reliability, platform limits, tokens, outcome cost and correlated traces |
| Security | 4 | Identity/resource access, auth flows, Key Vault and scoped adversarial testing |
| Guardrails | 3 | Intervention points, tool support, custom policy and synthetic validation |
| Deployment | 4 | DTAP, rollout/rollback, test layers and versioned CI/CD/IaC artifacts |

## Material corrections and additions

- **Hosted migration:** the initial backend's August 20 support deadline has
  passed. Current deployment uses distinct agent identities, endpoints, protocol
  packages and configuration. Compute idle timeout does not delete session data.
  The classic migration page also records August 26 inference-package/Assistants
  deadlines. SDK, service API, platform-generation and protocol versions are
  separate axes. Legacy Agent Application identity guidance retains its stated scope.
- **Protocol support:** incoming A2A v1.0 is GA while unversioned requests default
  to preview v0.3. Add explicit selection, selector-conflict errors, authenticated
  discovery, scoped roles, transport/content limits and latest-write retention.
  API Management's current MCP implementation supports tools, with workspace and
  tier limits; generic MCP capabilities do not establish gateway support.
- **Retrieval:** correct the claim that all filtering after ranking leaks data.
  Search's server-side post-filter modes can enforce scope while reducing recall;
  discarding unauthorized material after it enters prompts/logs is different.
- **Recovery and memory:** distinguish thread checkpoints from cross-thread stores,
  trusted identity from user-supplied IDs, async extraction from immediate visibility,
  and checkpoint replay from atomic external deduplication. LangGraph interrupt
  resume restarts the node. Add a failure-point lab and a deliberately bounded
  standard-library example.
- **Implementation:** extend HAX and Transformers coverage with explicit correction,
  ownership, model/version, validation, abstention and benchmarking decisions.
- **Evaluation and operations:** distinguish stored-output scoring from rerunning
  an agent, completion from correct outcomes, aggregate scores from critical slices,
  and total spend from cost per valid outcome. Qualify dashboard preview features,
  telemetry retention and illustrative operating thresholds.
- **Guardrails and red teaming:** configured moderation does not run for unsupported
  tool paths. Red-team target/tool support has a different matrix. Unsupported and
  unexecuted paths remain visible; synthetic/mock data is not complete isolation.

The guide cites the specific implementation pages beside each changed explanation.
Large retained reference pages were freshly retrieved but not exhaustively audited;
per-source notes identify the sections read or the narrower link-only check.

## Blog intake

Both public main articles were read; linked samples, videos, benchmarks and cloud
behavior were not reproduced.

- [Dan Taylor, September 24](https://devblogs.microsoft.com/agent-framework/interactive-experiences-memory-and-resilient-execution/):
  accept a recovery worksheet covering stable IDs, checkpoint state and a lost
  acknowledgement. Preserve the application's responsibility for external-effect
  idempotency and distinguish runtime capabilities and async memory behavior.
- [Theo van Kraay, July 24](https://devblogs.microsoft.com/cosmosdb/native-agent-memory-for-microsoft-agent-framework-powered-by-azure-cosmos-db/):
  accept a preview memory-provider worksheet covering authenticated scope,
  extraction lag, corrections and deletion. A clean shutdown draining background
  work is not proof of crash durability; profiles do not grant authorization.

Each exercise has an editorial 45–75-minute budget. These articles supplement the
official objectives rather than establishing additional exam requirements.

## Verification and follow-up

The six examples cover critical-path/quota arithmetic, reserved context space,
candidate-set filtering, replay deduplication, critical evaluation slices and
cost per valid outcome. Fifteen arithmetic/set/catalog assertions and four
assertions in the actual Python block passed. No model tokenization, Search HNSW,
real crash, SDK or service behavior was executed.

All **40** guide citations are registered: **38** returned reachable HTTP responses,
**two** commercial pages were access-blocked, and none returned a missing/error
classification. The certification announcement's content shell is explicitly a
semantic access limitation despite its successful HTTP response. Source retrieval
alone is not proof of correctness or a complete content review.

Three dated events recheck the September 30 course, October 5 beta/credential state,
and October 12 implementation support matrices. The central learning catalog is
synchronized from the guide and checked for drift. Repository/unit/site validation
results are recorded after execution in
`ADLC_Docs/operations/2026-09-28-ai-500-deep-review.json`.
