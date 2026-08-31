# Vendor adapters

Adapters discover and normalize public objective pages without embedding vendor-specific HTML behavior in the guide format.

`scripts/check_official_study_guides.py` currently contains two deliberately small adapters:

- `microsoft-learn` extracts skills-version headings, weighted objective sections, and announced changes.
- `hashicorp-developer` extracts the Terraform Associate exam/product baseline and unweighted objectives from the HashiCorp certification page.

Both produce normalized objective text plus a status record containing baseline labels and future announcements. Keep retrieval, comparison, snapshots, reports, and review workflow common; keep page markers and extraction rules provider-specific.

An adapter may retrieve public metadata and objective text. It must not access authenticated training, assessments, subscriptions, or private material.
