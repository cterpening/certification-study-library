# Automation and maintenance

## What the workflow automates

The repository’s weekly workflow monitors the official Microsoft Learn study-guide pages for GH-900, GH-300, GH-200, GH-100, and GH-500. It stores normalized objective and exam-status snapshots under `data/objective-snapshots` and proposes changes through a pull request.

The workflow detects:

- A changed “skills measured as of” date
- A newly announced future update or retirement
- The appearance of more than one published skills version
- Added, removed, or renamed objective groups
- Changed percentage weightings
- Added, removed, or reworded objective bullets

## What it deliberately does not automate

It does not rewrite the explanatory study guides. A changed bullet might require:

- New technical research
- Removal of a retired feature
- Updated labs or screenshots
- A terminology migration
- Changes to security or data-handling guidance
- New **VERIFY CURRENT** flags

A generated prose rewrite could look convincing while misunderstanding the exam change. The automation therefore produces evidence and a review task.

## First run

The first successful run creates normalized snapshots for all configured exams and opens a pull request. Review the extracted text against each linked official page before merging. Later runs compare against those approved snapshots.

## Required repository settings

1. Enable GitHub Actions.
2. In **Settings → Actions → General**, allow workflows to create pull requests if the organization permits it.
3. Ensure the default `GITHUB_TOKEN` can receive the workflow permissions declared in the workflow.
4. Create a `maintenance` label or change the failure step to use an existing label.
5. Protect `main` with a pull-request requirement and normal review.

No PAT or external API key is required. The workflow uses the repository-scoped `GITHUB_TOKEN`.

## Manual execution

Run **Actions → Check certification objectives → Run workflow** after:

- A GitHub product announcement
- A Microsoft Learn blueprint update
- A guide revision
- An exam scheduling decision

## Local tests

```bash
python3 -m unittest discover -s tests -v
```

The live download may be run locally when Microsoft Learn is reachable:

```bash
python3 scripts/check_official_study_guides.py --write
```

## Review checklist for an objective-change PR

- [ ] Confirm the extraction is genuine and not page-navigation noise.
- [ ] Record the new skills-measured date.
- [ ] Check whether the page announces a future update or retirement and update the guide status line.
- [ ] Update the affected guide’s objective map and weights.
- [ ] Add or remove technical coverage.
- [ ] Recheck all product names, paths, permissions, and preview status.
- [ ] Update labs and readiness checklist.
- [ ] Verify links against official Microsoft/GitHub sources.
- [ ] Run tests and inspect Markdown rendering.
- [ ] Merge the snapshot and guide changes together when practical.

## Optional Copilot-assisted maintenance

An objective-change issue can be assigned to a configured coding agent to prepare a draft guide update. Keep human review mandatory. The agent should receive:

- The changed snapshot diff
- The affected guide path
- A requirement to use official sources
- A prohibition on invented product behavior or exam questions
- Instructions to retain **VERIFY CURRENT** labels
- Required Markdown and link validation
