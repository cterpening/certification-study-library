# Source-validation records

Source validation is a documented quality gate, not a claim that a guide is error-free. A **SOURCE-VALIDATED** guide has been checked against the current official objective snapshot, its material explanations have supporting public sources, volatile details are marked **VERIFY CURRENT**, repository and external links validate, and the content passes the project's exam-integrity policy.

The machine-readable evidence is in [`data/reviews.json`](https://github.com/cterpening/certification-study-library/blob/main/data/reviews.json). Repository validation recomputes blueprint hashes, exact source registration, and source-health counts so a stale review record fails the build. A separate human contributor review is still required before a guide can become **COMMUNITY REVIEWED**.

## Current source-validated guides

| Exam | Reviewed | Blueprint snapshot | External-link evidence | Result |
|---|---|---|---|---|
| GH-900 | August 31, 2026 | January 2026 objectives; unchanged during review | 69 registered links: 67 reachable, 2 access-blocked, 0 missing/error | Passed |
| GH-300 | August 31, 2026 | August 7, 2026 objectives; unchanged during review | 55 registered links: 53 reachable, 2 access-blocked, 0 missing/error | Passed |
| GH-200 | August 31, 2026 | January 2026 objectives; unchanged during review | 39 registered links: 38 reachable, 1 access-blocked, 0 missing/error | Passed |
| Terraform Associate (004) | August 31, 2026 | Terraform 1.12 objectives; unchanged during review | 33 registered links: 30 reachable, 3 access-blocked, 0 missing/error | Passed |

Access-blocked course pages returned HTTP 403 to the automated client. An access-controlled response is recorded separately from a missing or failing page and does not establish that the resource is unavailable to a browser or subscriber.

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

## GH-200 coverage record

| Published objective group | Guide coverage |
|---|---|
| Author and manage workflows | Parts 1–4, Part 10, and Labs 1–3 |
| Consume and troubleshoot workflows | Parts 4–5, troubleshooting by failure phase, and Labs 1–3 |
| Author and maintain actions | Part 6, custom-action engineering, and Lab 5 |
| Manage GitHub Actions for the enterprise | Part 7, enterprise governance and runner operations, and Lab 6 |
| Secure and optimize automation | Parts 8–10 and Labs 4–6 |

The review added official citations and decision guidance for editor validation, workflow badges, retention and REST administration, workflow templates, immutable releases, IP allow lists, hosted-runner image dependencies, and encrypted-secret APIs. The official blueprint snapshot SHA-256 is `b41c6a6832e14bf4b6c222d0b6162cff81e9ef4683480f89e89b3e0406fdf941`.

## Terraform Associate (004) coverage record

| Published objective group | Guide coverage |
|---|---|
| Infrastructure as Code (IaC) with Terraform | Domain 1 and Labs 1–2 |
| Terraform fundamentals | Domain 2 and Labs 1–2 |
| Core Terraform workflow | Domain 3 and Labs 1–2 |
| Terraform configuration | Domain 4 and Labs 1–5 |
| Terraform modules | Domain 5 and Lab 3 |
| Terraform state management | Domain 6 and Labs 4–5 |
| Maintain infrastructure with Terraform | Domain 7 and Labs 4–5 |
| HCP Terraform | Domain 8 and Lab 6 |

The review checked all 38 published subobjectives without inventing percentage weights, retained explicit **VERIFY CURRENT** treatment for volatile HCP Terraform service details, and verified that the 004-specific lifecycle, custom-condition, ephemeral/write-only, and workspace/project additions are visible. The official blueprint snapshot SHA-256 is `41390d0d2fbb8b1cfbfb7349ada41f4cf13dc65815827b802ad082fd2c1bf53b`.

## Revalidation triggers

A guide returns to **REVIEW REQUIRED** when its official objective or status snapshot changes. Source-health findings create review work but do not automatically rewrite or demote content because redirects, access controls, page-title changes, and provider metadata changes require human interpretation. A new source-validation record is required after the guide is reconciled with a changed blueprint.
