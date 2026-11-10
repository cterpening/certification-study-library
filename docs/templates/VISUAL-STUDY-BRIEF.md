# Visual study brief: [one topic]

Use this brief to turn one reviewed guide topic into a study infographic and an
original active-recall exercise. Replace bracketed fields; keep the scope small
enough that a learner can explain one distinction, decision, or process. Follow
the [study production process](../STUDY-PRODUCTION.md),
[content policy](../CONTENT-POLICY.md), and [source standard](../SOURCE-QUALITY.md).

## 1. Bind the topic to its evidence

- **Certification and topic:** [exam code, credential name, topic].
- **Canonical exam guide:** [exact official URL]; **accepted objective version:**
  [effective date/version].
- **Published objective:** [exact wording and identifier if one exists]. Mark
  supporting material outside that wording with **Related item:**.
- **Library guide:** [exact repository path and section heading/anchor];
  **SHA-256:** [complete guide hash].
- **Accepted objectives:** [exact snapshot path]; **SHA-256:** [hash].
- **Study package:** [directory, exact study-guide.md path and heading, unit ID];
  **study-guide.md SHA-256:** [hash]; **manifest.json SHA-256:** [hash]. If no package
  exists, state that explicitly and identify the reviewed guide as the sole input.
- **Authored content, if present:** [exact path and unit]; **SHA-256:** [hash].
- **Source records:** [catalog/health/evidence paths and SHA-256 values used by the
  package]. **Hash convention:** [use the package convention; otherwise state
  whether hashes use file bytes or normalized text].
- **Review basis:** [dated review record, reviewer and AI/human kind, scope and
  remaining findings]. A reviewed topic can still have human review pending.

Use registered exact URLs, not invented references. Record each material claim:

| Fact to teach | Registered source ID and exact URL/section | Evidence date and confidence | Qualification |
|---|---|---|---|
| [One factual proposition] | [ID; descriptive link; heading] | [Actual check date; Confirmed / Corroborated — verify current / Unconfirmed — validation needed] | [Version/mode/scope; VERIFY CURRENT when required] |

The blueprint defines exam scope; product evidence supports technical behavior.
A stored catalog check is historical evidence. Record unavailable or conflicting
evidence and the next useful check; do not turn a hypothesis into a correct answer.

## 2. Choose the learning task and visual

- **Learner question:** [One question the learner should be able to answer after
  studying the visual].
- **Prerequisite:** [Only the knowledge needed to follow it].
- **Takeaway:** [One sentence, supported by the claims above].
- **Likely misconception:** [Plausible wrong inference and the fact that corrects it].
- **Invented scenario:** [Original actors, requirements, numbers, timestamps, and
  assumptions]. Label these as illustrative, not measured results, product
  guarantees, or remembered exam content. Separate them from sourced facts.

Choose the format that makes the relationship visible:

| Candidate | Useful when the learner must… |
|---|---|
| Timeline or staged flow | Trace order, dependencies, delays, or missing evidence |
| Side-by-side comparison | Distinguish similar concepts using the same criteria |
| Decision tree | Choose from explicit requirements and explain the branch |
| Annotated system/boundary diagram | Locate responsibility, access, or data movement |
| Worked example with callouts | Apply a rule and inspect its consequences |

**Selected format and reason:** [Format; what its layout helps the learner reason
about]. **Visual plan:** [Nodes, labels, arrows, units, reading order, and emphasis].
Use original wording and artwork. Include a visible scenario label and essential
qualifications; avoid vendor endorsement or decorative detail that obscures the task.

## 3. Author the paired versions

**Study version — [output path]:** [Show the explanation, relationships, and worked
reasoning]. Cite the supporting sources in the accompanying text and link back to
the exact guide topic. Keep labels legible at the intended viewing/print size.

**Practice version — [output path]:** [Retain the evidence and assumptions; remove
the conclusion or selected labels]. **Prompt:** [Ask the learner to infer, order,
calculate, diagnose, or justify]. **Required response:** [What the learner writes
or says]. It should test reasoning, not just recognition of the study layout.

**Accessible text alternatives — [paths/locations]:**

- Study: [Equivalent explanation of all meaningful labels and relationships].
- Practice: [Equivalent givens, relationships, blanks, and question only]. Do not
  reveal the solution in alt text, SVG title/description, hidden labels, filenames,
  or other assistive text. Keep answers in a separate, clearly labeled location.
- Both: [Reading order; descriptive labels; meaning available without color alone;
  checks for contrast, clipping, and readable text].

**Answer and rationale — [separate path/section]:** [Correct response, reasoning
from the givens and sourced facts, acceptable alternatives, and why the likely
misconception fails]. State what evidence is insufficient to conclude. Do not add
new unsupported behavior to make the answer work.

**Learner-facing status:** Include: “Independent AI-assisted resource. [Generation
and review state.] The official exam blueprint is authoritative.” Link the canonical
exam guide, identify this as selected-topic practice, and preserve **VERIFY CURRENT**
and unresolved limitations. Do not claim complete exam coverage or human review
unless the corresponding work was performed and recorded.

## 4. Review, record, and rebuild

1. Check the guide, objectives, claim table, both visuals, text alternatives, and
   answer together. Verify that the prompt is answerable from its givens and that
   the two versions teach the same facts without practice-answer leakage.
2. Render both visuals and inspect them at the intended size. Check labels, units,
   arrow direction, reading order, contrast, and clipping. A successful render or
   matching hash establishes neither technical correctness nor learning outcomes.
3. Give a fresh-context reviewer the exact inputs, outputs, hashes, source evidence,
   and this brief. Resolve material findings. Record author/same-context review,
   independent AI review, human review, and actual product execution separately;
   state plainly when any did not occur.
4. Keep a short review record: [date; reviewer/kind; exact artifact paths and
   SHA-256 values; checks actually completed; findings/fixes; limitations; next
   check]. Record link/structure validation and visual inspection as distinct evidence.
5. Recheck and rebuild when a bound guide, objective, package, content input, source
   record, or answer changes; when evidence becomes stale or contradictory; or when
   a learner/reviewer finds an ambiguity or accessibility defect. Follow the package's
   existing fingerprint rules, including whole-catalog changes. Preserve the previous
   dated output, review the change, and record new output hashes. Do not advance review
   dates merely to clear a stale hash or treat a rebuild as a fresh technical review.
