# Architecture

## Public content flow

```text
vendor catalog and official blueprint
                ↓
      reviewed objective snapshot
                ↓
 approved public sources + guide template
                ↓
        AI-assisted draft guide
                ↓
citation, policy, link, and coverage review
                ↓
 machine-readable review evidence
                ↓
             publication
```

The certification-seed catalog records the broader research queue, exact official credential URLs, catalog scope, lifecycle state, and verification date. The exam catalog is its publication subset: it identifies the canonical blueprint, guide path, freshness date, review state, and editorial learning level for credentials with complete guides. The level is a site-wayfinding judgment—beginner, intermediate, or expert—not a claim that every provider uses the same credential taxonomy. Repository validation requires every published exam to remain present in the seed catalog. The source catalog records authority and provenance. Objective snapshots provide dated change evidence. Passed reviews in `data/reviews.json` bind a promoted state to a blueprint hash, objective map, policy checks, and link-health evidence. A guide remains a draft until its objective coverage and material claims have been reviewed.

Proposed links enter through `data/source-candidates.json`. This inbox is deliberately separate from the approved `data/sources.json` catalog so an unchecked submission cannot appear as a trusted or recommended resource. Promotion requires an explicit source-quality review; rejected candidates retain concise decision evidence to prevent repeated reconsideration.

The scheduled source-health monitor records public reachability, redirects, page titles, canonical URLs, and duration signals in `data/source-health.json`. Access controls are distinguished from missing pages. Monitor output creates review work and never edits catalog judgments or guide prose automatically.

The objective monitor selects an adapter from each provider record. The Microsoft Learn adapter handles skills-version headings, percentage-weighted domains, and future-update notices. The HashiCorp Developer adapter handles the Terraform Associate version/product baseline and its unweighted objective table. Both emit normalized objective text and status JSON while keeping provider-specific HTML assumptions outside the guide format. Add another adapter only after testing it against that provider's real public blueprint.

## Static website flow

```text
config/exams.json + config/collections.json + data/vendors.json + data/sources.json
                              │
canonical guides + allowlisted project documents
                              ↓
       scripts/prepare_site.py
                              ↓
 .site-build/docs + generated navigation/catalog
                              ↓
       strict MkDocs build
                              ↓
       site/ static artifact
```

The preparation step copies only configured guides and the explicit `PUBLIC_DOCUMENTS` allowlist. It does not treat the repository root or the entire `docs/` directory as publishable. This is a security and separation boundary: ignored working notes, private overlays, build reports, and unrelated files cannot enter the site merely because they exist locally.

The vendor catalog drives provider labels, ordering, overview pages, and objective-adapter selection. The exam catalog drives guide cards and navigation; research-only certification seeds do not appear on the site until a complete guide is registered. The collection catalog defines overlapping editorial learning lenses and must never present them as official vendor pathways. The source catalog drives the source count. `website/` contains the maintained homepage template, MkDocs configuration template, and visual assets. Generated `.site-build/` and `site/` content is disposable and must not be edited or committed.

## Public and private separation

```text
public repository ──sync──► clean work mirror
                                   │
private internal sources ──────────┤
private presentation rules ────────┘
                                   ↓
                         internal rendered library
```

The public repository controls its own Markdown and public presentation. The work environment may transform that content and combine it with a private overlay, but internal formatting and content do not flow upstream.

## Trust boundaries

- Official blueprints define scope but do not explain every product behavior.
- Official product documentation supports technical claims.
- Third-party sources may add teaching approaches and examples without becoming canonical.
- Generated prose is untrusted until reviewed against its supporting sources.
- A detected upstream change invalidates review state; it does not authorize an automatic explanatory rewrite.
