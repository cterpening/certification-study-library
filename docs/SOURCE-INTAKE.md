# Adding a source for review

The repository separates proposed sources from the approved source catalog:

- `data/source-candidates.json` is the low-friction review inbox.
- `data/sources.json` is the master catalog of evaluated sources used by guides and the website.

Adding a candidate does not endorse it or make it part of a study guide. It records what should be checked and why it may be useful.

## Add a candidate

Add an object to the `candidates` array:

```json
{
  "id": "creator-course-or-resource",
  "title": "Visible resource title",
  "url": "https://example.com/exact-resource",
  "added_on": "2026-08-31",
  "suggested_exams": ["AB-100"],
  "reason": "Architecture walkthroughs may support the data, identity, and governance objectives.",
  "review_status": "queued"
}
```

Use the exact course, playlist, repository, book, or documentation page rather than a search result or marketplace homepage. `suggested_exams` may be empty when the fit is not known yet.

Candidate IDs use lowercase letters, numbers, and hyphens. They must not duplicate an approved source ID or URL.

## Review a candidate

Set `review_status` to `in-review` while evaluating:

- author, publisher, and ownership;
- official objective coverage;
- publication and update dates;
- technical accuracy and first-party support;
- access model and realistic consumption time;
- licensing and attribution requirements;
- exam-integrity concerns;
- whether a narrower exact resource is better than the submitted URL.

Claims about real exam questions, dumps, guaranteed passes, or reconstructed confidential material are rejection signals.

## Promote or reject

When accepted, create the full evaluated record in `data/sources.json`, update the relevant guide or learning-resource page, and remove the candidate from the inbox in the same change. Git history preserves the decision.

Use one of the catalog's explicit access models: `public`, `free-account`, `partner-restricted`, or `paid`. Use `partner-restricted` when organizational eligibility is required even if the resource has no additional cost for an eligible organization, and explain the requirement in `notes` and in the guide's access column.

When rejected, leave the candidate in the inbox with `review_status` set to `rejected`, plus `reviewed_on` and a concise `review_notes` explanation. This prevents the same unsuitable source from being repeatedly reconsidered without new evidence.

## Validate

```bash
python scripts/validate_repository.py
python -m unittest discover -s tests -v
```

Validation checks candidate IDs, URLs, dates, exam references, duplicate approved sources, and the allowed review states. A future workflow can create a review issue or pull request for queued entries without automatically promoting them.

Approved sources are also included in the weekly health monitor. The tracked `data/source-health.json` baseline stores public reachability, redirect, page-title, canonical-URL, and duration signals. Monitor findings trigger review; they never promote, remove, or rewrite a source automatically.
