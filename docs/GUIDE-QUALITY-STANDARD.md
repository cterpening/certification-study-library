# Guide depth and related-item standard

This project measures guide quality by useful objective coverage, not by forcing every guide to the same word count. A mature guide should help a learner recognize a concept, explain it, distinguish it from nearby concepts, apply it, troubleshoot it, and decide when it is appropriate.

## Objective treatment

For each published objective, include the elements that materially improve learning:

1. **Plain-language explanation** — what the product, feature, or decision means.
2. **Mental model** — how the parts relate and where the control or data boundary sits.
3. **Decision guidance** — when to choose one option instead of another.
4. **Example** — configuration, command, scenario, architecture, or workflow.
5. **Failure mode** — a common misconception, security risk, or troubleshooting clue.
6. **Hands-on check** — something the learner can configure, inspect, or explain.
7. **Current source** — the official blueprint for scope; current first-party product
   documentation for behavior when available; otherwise evaluated, cited supplementary evidence
   with an adjacent confidence label and validation gap.

Not every objective needs all seven in equal depth. High-weight, operationally risky, or easily confused topics deserve more treatment than straightforward vocabulary.

Non-vendor sources are welcome when they improve explanation, distribution coverage, operational
realism, or reproducibility. They must be attributed and evaluated under `docs/SOURCE-QUALITY.md`.
They do not define what an exam covers. When first-party behavior cannot be confirmed, label the
passage **Corroborated — verify current** or **Unconfirmed — validation needed**, state what is
missing, and give a safe way to test it. Never turn uncertain material into a production-ready
instruction or an unlabeled fact.

## Related items

Use the exact prefix below when adjacent knowledge makes an objective easier to understand or apply:

> **Related item:** Explain the related prerequisite, operational concern, architecture pattern, or neighboring product concept and why it matters here.

A related item is deliberately outside the strict wording of the objective or is broader than the exam requires. It must be relevant, concise enough not to displace the published objective, and supported by an appropriate source. It must not be presented as a prediction about undisclosed exam content.

Good related items include:

- a prerequisite that explains why a feature behaves as it does;
- an operational consequence such as incident response, cost, or observability;
- a neighboring control that is commonly confused with the objective;
- a later certification or job-role topic that gives the current concept context.

Poor related items include unrelated trivia, provider marketing, remembered exam content, and speculative claims that something is likely to appear on the exam.

## Study-depth entry points

Long guides must preserve their depth without requiring every learner to follow the same route. The generated guide-start panel exposes three choices:

- **Exam essentials** for the objective map, key distinctions, and readiness checklist;
- **Deep understanding** for explanations, decisions, failure modes, and related items; and
- **Hands-on labs** for practice that produces inspectable evidence.

These are navigation aids, not separate review states. Within a guide, use `Related item:` for adjacent supporting knowledge. Use an explicit **Beyond the exam** label only when material is useful professional depth but is neither a published objective nor necessary foundation.

## Heading structure

Give each guide a level-two **Key terms and phrases** section immediately before **Places to learn**. Work through the published domains and their teaching sections when choosing terms. Include the concepts, product features, mechanisms and measurements a learner will encounter across the guide. Around 35–60 entries suits many guides. Broader outlines may need more. Organize entries in short tables by topic and keep closely related concepts together so readers can compare them.

Link each term to the passage that teaches it. Explain its meaning in this certification's context and expand unfamiliar acronyms. Use a short example for a decision or behavior. For a quantity, a calculation with units and a clear denominator can supply the definition. For elective paths, supporting knowledge or unpublished objectives, preserve the scope stated in the teaching passage.

Every guide has exactly one level-one heading for its title. Major guide parts use level-two headings, with level three and level four reserved for nested topics. The website limits the visible right-side table of contents to major level-two sections; search and in-page headings still expose the full detail.

## Depth review

Before calling a guide rebaselined, verify that:

- every published domain and subdomain has visible coverage;
- major distinctions have examples or decision tables;
- labs exercise the highest-value workflows instead of only asking the learner to click through a UI;
- knowledge checks are independently written and test reasoning;
- volatile behavior is marked **VERIFY CURRENT**;
- `Related item:` callouts are clearly distinguished from blueprint coverage;
- the final public section remains `Places to learn` for a consistent reading and publishing experience;
- that section says it is a curated starting point, not a complete list or a requirement to consume every resource.
- each listed learning resource includes a transparent consumption-time estimate; use the published duration or agenda when available, otherwise give an `about` range and state the estimate's basis.
