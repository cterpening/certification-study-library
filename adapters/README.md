# Vendor adapters

Adapters discover and normalize public objective pages without embedding vendor-specific HTML behavior in the guide format.

`scripts/check_official_study_guides.py` contains deliberately small adapters for the public objective formats currently represented in the library:

- `microsoft-learn` extracts skills-version headings, weighted objective sections, and announced changes.
- `hashicorp-developer` extracts the Terraform Associate exam/product baseline and unweighted objectives from the HashiCorp certification page.
- `databricks-certification` extracts the live weighted coverage map and public assessment details; detailed downloadable PDFs remain preserved separately.
- `aws-exam-guide` extracts an exam identity, capability summary, and weighted content domains from AWS Documentation exam guides.
- `comptia-certification` extracts the public version/code/lifecycle details and weighted objective summary from an exact CompTIA exam page.
- `red-hat-exam` extracts public performance-task lists and tested product-version baselines from Red Hat exam pages.
- `linux-foundation-certification` extracts domains, competencies, format, duration, validity, and software-version details from Linux Foundation and CNCF certification pages.

Both produce normalized objective text plus a status record containing baseline labels and future announcements. Keep retrieval, comparison, snapshots, reports, and review workflow common; keep page markers and extraction rules provider-specific.

An adapter may retrieve public metadata and objective text. It must not access authenticated training, assessments, subscriptions, or private material.
