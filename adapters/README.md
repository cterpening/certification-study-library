# Vendor adapters

Adapters will discover and normalize public certification catalogs and objective pages without embedding vendor-specific behavior in the guide format.

The GitHub certification seed currently uses the standard-library monitor in `scripts/check_official_study_guides.py`. Extract that behavior into a Microsoft Learn adapter only when another vendor proves which interface is genuinely shared.

An adapter may retrieve public metadata and objective text. It must not access authenticated training, assessments, subscriptions, or private material.
