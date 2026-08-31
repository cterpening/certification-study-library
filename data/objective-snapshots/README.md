# Official objective snapshots

The normalized objective text and status JSON files are generated from the official URLs configured in `config/exams.json` using the provider adapters registered in `data/vendors.json`. Status snapshots record the provider's published skills/exam/product baseline and explicit future-update or retirement announcements. Microsoft Learn and HashiCorp Developer are currently supported.

Future runs compare live objectives with these committed baselines. Do not treat a generated replacement as trusted until its pull request has been checked against the official page.
