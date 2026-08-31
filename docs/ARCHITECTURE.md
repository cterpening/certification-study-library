# Architecture

## Public content flow

```text
vendor catalog and official blueprint
                ↓
      reviewed objective snapshot
                ↓
 registered public sources + guide template
                ↓
        AI-assisted draft guide
                ↓
 citation, policy, link, and coverage review
                ↓
             publication
```

The exam catalog identifies the credential, canonical blueprint, guide path, freshness date, and review state. The source catalog records authority and provenance. Objective snapshots provide dated change evidence. A guide remains a draft until its objective coverage and material claims have been reviewed.

The initial monitor is intentionally specific to Microsoft Learn because all five seed credentials publish their blueprints there. Vendor adapters should be extracted only after another catalog demonstrates a stable shared boundary.

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
