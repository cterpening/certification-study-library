# Source and citation quality

## Best-effort principle

All repository research, validation, and discrepancy handling is best effort. That means
doing the most useful bounded investigation available with the authorized evidence and
tools, not claiming that a search is exhaustive or that missing evidence proves a feature
does not exist. Record where and when the search was performed, the source classes checked,
the strongest supported answer, conflicting or unavailable evidence, confidence, and the
specific work that could improve the answer later.

Best effort is not permission to lower the evidence standard. When certainty is unavailable,
prefer a useful provisional explanation and a safe validation path over either unsupported
certainty or an unexplained omission. Keep the gap visible, preserve failed and contradictory
findings, and replace the provisional answer when stronger evidence becomes available.

## Authority hierarchy

| Tier | Source | Permitted use |
|---|---|---|
| 1 | Official exam blueprint | Exam identity, domains, objectives, weighting, and status |
| 2 | Official product documentation | Current technical behavior and configuration |
| 3 | Official training | Vendor explanations, labs, and approved preparation |
| 4 | Structured third-party training | Learning sequence and additional explanation |
| 5 | Named expert or maintained repository | Practical examples and specialist explanation |
| 6 | Independent assessment | Gap detection, never canonical dispute resolution |

## Citation requirements

- Place a descriptive link near the claim it supports.
- Cite the final authoritative page, not a search-result page.
- Do not cite a course landing page as evidence of product behavior.
- Do not let a model invent URLs. New generated references must come from the registered source set; seed-guide links should be registered as they are reviewed.
- Record publisher, authority class, last check, and supported objectives.
- Mark a dependent page for review when a canonical source changes.
- Treat publication dates and update dates as different fields.

## Volatile claims

Pricing, discounts, exam duration, delivery vendors, languages, product UI, model lists, quotas, credits, retention, preview status, feature availability, and command syntax must be labeled **VERIFY CURRENT** unless directly synchronized from a current official source.

## Blockers and source discrepancies

When first-party documentation is missing, contradictory, or too shallow to teach a
published objective, apply the best-effort principle before declaring the topic
unresearchable. Check, in order: current vendor documentation; vendor-owned source
code, examples, issue trackers, and training; maintained upstream projects; named
experts; and independent implementation reports. Search results are leads, not evidence.

Record promising exact URLs in `data/source-candidates.json` with the proposition each
could support, its age/ownership, conflicts, and what still needs validation. Two sources
repeating the same claim do not make it official, particularly when one copied the other.
Do not promote a candidate merely to remove a blocker.

A guide may summarize a provisional model only when it clearly separates:

- what the blueprint requires;
- what current first-party evidence confirms;
- what supplementary sources consistently suggest;
- what remains unknown, version-sensitive, or contradictory; and
- the safe test and evidence needed to validate the hypothesis.

Mark provisional material **VERIFY CURRENT**, avoid production-ready wording, and do not
turn unverified commands into a required lab. Prefer a disposable, authorized validation
matrix that records versions, expected/observed behavior, logs, failure cases, and cleanup.
Keep the review blocked until accepted evidence or reproducible validation meets the
normal source standard. Recheck the candidate set during later freshness passes so better
first-party guidance can replace provisional material without erasing the earlier gap.

## Third-party evaluation

Evaluate an individual resource rather than an entire marketplace. Record:

- author or publisher;
- format and access model;
- publication and update dates;
- objectives covered;
- strengths and known gaps;
- whether explanations cite first-party evidence;
- whether the source contains independent practice or questionable exam claims.

Claims such as “actual questions,” “real exam dump,” or guaranteed passing are exclusion signals.

## Practice-assessment boundary

Practice assessments are Tier 6 sources because of how they are used, even when the exam sponsor publishes them. They may help identify weak objectives, exercise time management, and provide explanations or first-party references. They cannot establish exam scope, technical truth, scoring rules, or the contents of a live exam. Prefer the free Microsoft assessment as the first baseline when one is available, then use a paid provider only when another question style or explanation set would add value.

Link an exact exam-specific product only after checking its publisher, visible objective map, question count or format when published, update signals, access model, and exam-integrity language. Record contradictory or stale public copy as a caveat. Estimate consumption time for an initial timed attempt, targeted practice, and explanation review rather than implying that every learner should memorize or exhaust the bank.

When a source declares a permissive license but its linked license file is missing, record the declaration and missing notice in `THIRD-PARTY-NOTICES.md`, attribute the author and source, prefer independently written synthesis, and add the exact notice if it becomes available. Do not infer that publicly readable material is in the public domain.

## Seed training sources

The initial catalog may include Microsoft Learn, GitHub Docs, O'Reilly, Pluralsight, Whizlabs, Udemy, John Savill's Technical Training, and Timothy Warner's public repositories. Inclusion is not endorsement; each resource receives its own metadata and coverage review.
