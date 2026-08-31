# Source-validation records

Source validation is a documented quality gate, not a claim that a guide is error-free. A **SOURCE-VALIDATED** guide has been checked against the current official objective snapshot, its material explanations have supporting public sources, volatile details are marked **VERIFY CURRENT**, repository and external links validate, and the content passes the project's exam-integrity policy.

The machine-readable evidence is in [`data/reviews.json`](https://github.com/cterpening/certification-study-library/blob/main/data/reviews.json). Repository validation recomputes blueprint hashes, exact source registration, and source-health counts so a stale review record fails the build. A separate human contributor review is still required before a guide can become **COMMUNITY REVIEWED**.

## Current source-validated guides

| Exam | Reviewed | Blueprint snapshot | External-link evidence | Result |
|---|---|---|---|---|
| GH-900 | August 31, 2026 | January 2026 objectives; unchanged during review | 66 registered links: 65 reachable, 1 access-blocked, 0 missing/error | Passed |
| GH-300 | August 31, 2026 | August 7, 2026 objectives; unchanged during review | 52 registered links: 51 reachable, 1 access-blocked, 0 missing/error | Passed |

The access-blocked link in each guide is an O'Reilly landing page that returned HTTP 403 to the automated client. An access-controlled response is recorded separately from a missing or failing page and does not establish that the resource is unavailable to a browser or subscriber.

## GH-900 coverage record

| Published objective group | Guide coverage |
|---|---|
| Understand Git and GitHub basics | Parts 1–5, 7, and 10 |
| Work with GitHub repositories | Parts 4–6 and 13–15 |
| Collaborate using GitHub | Parts 7–8 |
| Apply modern development practices | Parts 9–11 |
| Manage projects with GitHub | Parts 8 and 12 |
| Understand privacy, security, and administration | Parts 5 and 13–15 |
| Explore the GitHub community | Parts 7 and 16 |

The review removed a duplicated GH-300-specific chapter from the GH-900 guide, retained a concise related-guide handoff, and added primary-reference blocks near each substantive part. The official blueprint snapshot SHA-256 is `bd1c323a21723f8479a7b79ec41a576044ebe6afbc5bf57715acf431fe90828b`.

## GH-300 coverage record

| Published objective group | Guide coverage |
|---|---|
| Use GitHub Copilot responsibly | Part 0, Parts 4–5, and Labs 3–5 |
| Use GitHub Copilot features | Parts 2–4, Part 6, and Labs 2–5 |
| Understand GitHub Copilot data and architecture | Part 0 and Parts 4–5 |
| Apply prompt engineering and context crafting | Part 0, Parts 3–4, and Labs 3 and 5 |
| Improve developer productivity with GitHub Copilot | Part 0, Parts 3–4, and Labs 1–3 |
| Configure privacy, content exclusions, and safeguards | Parts 5–6 and Lab 4 |

The review added first-party citations beside the responsible-AI principles, service-flow explanation, prompt-engineering model, productivity guidance, refactoring practice, and test-generation practice. The official blueprint snapshot SHA-256 is `2043edf29c68926236ec3a6e417058609e4e6cfec55e1e201e48e57c1b4fff9b`.

## Revalidation triggers

A guide returns to **REVIEW REQUIRED** when its official objective or status snapshot changes. Source-health findings create review work but do not automatically rewrite or demote content because redirects, access controls, page-title changes, and provider metadata changes require human interpretation. A new source-validation record is required after the guide is reconciled with a changed blueprint.
