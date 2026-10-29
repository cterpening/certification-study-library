# Group 15 independent guide review

**Audit date:** 2026-10-29
**Rubric:** `docs/AI-AUDIT.md`, rubric 2
**Mode:** fresh-context, read-only semantic review; no human review or live product/lab execution is claimed.

## Scope and binding

All ten current guides were hashed against `.maintenance/g15-review-hashes.json` before reading. The four Python guides with final intro wording updates were rehashed against the refreshed manifest and those changed sections reread. Every current guide and objective hash matched the manifest; all official-status snapshot hashes also matched. Objective hashes below are raw-byte SHA-256; guide hashes use LF-normalized UTF-8 per rubric 2.

| Exam | Guide SHA-256 | Objective snapshot SHA-256 | Current objective snapshot | Status snapshot |
|---|---|---|---|---|
| PANW-CYBERSECURITY-APPRENTICE | `1aa17fc40af87140a82c3bb0c58d6b9a3d47b8fcfd1ebe2c70a23b7e25463ec2` | `fbd3b8491d4f5a04b8592653652089dcb6e1fe7f7e1948a974dd37469f1673b7` | `data/objective-snapshots/panw-cybersecurity-apprentice-official-objectives.txt` | `7b407d7ea6ba74b7d4f83f5c772c68c7d584c3c362aa493daf616a16576d667a` |
| PCAD-31-02 | `4056afbda7081210965b59ed2d0a4537712c86347c5a08dbbd18799fe3314d1e` | `c0e03d205f2bb78e1902508ab699839dee11825423eebe0da9a68832ca657275` | `data/objective-snapshots/pcad-31-02-official-objectives.txt` | `8178d5edb47a3a3d20344cd419a57b99dc42cfd9adb20eedb88ca274d4a6875b` |
| PCAP-31-03 | `f225c056f77d88884f1601f1b9af222eca11116b16618f04f96b8bf12f3f8437` | `49589f9a3aaa766a2b2c1a640ac5dbbf7842c01d2517397519ab35ac86a060b0` | `data/objective-snapshots/pcap-31-03-official-objectives.txt` | `ab75604aee1f40a143c9ba5fbce23606f529c6f52ce07fb4e9597aa8aaa0d1fb` |
| PCED-30-02 | `d69f4e937425583e779afc7495b4feb5b45f9e790515be8844971f9167a650e3` | `27c6f07ec4b1e1063e5cbb6effd00e13406e15d8ee54a2e748c50dff86c24b90` | `data/objective-snapshots/pced-30-02-official-objectives.txt` | `14d32bf3107f551ab157e5573e50b0b6c4f4f82756a75d89bf5baf47ed5f191e` |
| PCEP-30-02 | `e523e67f4cd17f3891a0c8f2aaa3567c5ebeefc0cc017253220af6b4fb3524ba` | `fc0a0b67b1f15a4430075b889978a82e162d98642f0b822768bc3796c322ca57` | `data/objective-snapshots/pcep-30-02-official-objectives.txt` | `ad75cb4b5b36f8384b966f2ad58b6bc6d7cda8885ef0d27734ee298df2ae8bfb` |
| PCPP-32-101 | `0b37d42a584933c74608dba200f33e4181f0d93a2522978d2ce23a76453a5e56` | `899426a902f78aba1471211f0c1eeace8016a66eb8dac3407d013d97cdaafcd6` | `data/objective-snapshots/pcpp-32-101-official-objectives.txt` | `babc889d49f5b7df2aa0a84e89235b3e9ed91affc09a4b9b97e97d0a29d6d96e` |
| SALESFORCE-AGENTFORCE-SPECIALIST | `3c8d089864e680fee1aa378924b0894e30204952ed5830f0fb742d270f80cdb7` | `a633fd73b5f733d78426c5c66eebf566a7867d80a36ddadd505dbd8ef29b5664` | `data/objective-snapshots/salesforce-agentforce-specialist-official-objectives.txt` | `48706738384bf7c928d7da53489404ad7476ac71685ce277441ddb0a4e874a01` |
| SALESFORCE-PLATFORM-ADMINISTRATOR | `9e795c46047c3ff2e32c331c1383cda66eb8723c04d089ca11f2094d7fba7f52` | `b2f9f40f925247562d8d19eed5ad7a33a4b5c10e03b705d2fe34ec88678b7c97` | `data/objective-snapshots/salesforce-platform-administrator-official-objectives.txt` | `e50e41ee5c99d5f6ebf5baa313f8f98ec6ed4501fc11b091d8db38b040600468` |
| SALESFORCE-PLATFORM-APP-BUILDER | `889ee71ec7bdf8f000fdb37d5c9fc39148fe8737b7ef91fa38a1a537994cef75` | `5365cb37f260db38aa6b4a306dd826258e3d85f058b8111352e56a065a965f14` | `data/objective-snapshots/salesforce-platform-app-builder-official-objectives.txt` | `6071f7bbdab29492836235f2378d741b09c5ba98456669289d7b39e5f3690aa6` |
| SALESFORCE-PLATFORM-DEVELOPER | `666723c1574b0ce91386435e6813c0da6bf48692d41d9dc5d9fecc9c0d06d94b` | `4843c3b24a93a1c4da79e50db00e79c38fa5921c6127df89e37a6754c5cddbfe` | `data/objective-snapshots/salesforce-platform-developer-official-objectives.txt` | `a279edd220b1830daae23557891304a55628774c29db7c520002411a2512074a` |

## Ten-check status

Legend: **P** passed. Check order: official scope; objective coverage; material claim support; exam-contract integrity; technical coherence; volatility/lifecycle; lab safety/feasibility; readiness checks; review-evidence accuracy; duplication/contamination.

| Exam | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| PANW-CYBERSECURITY-APPRENTICE | P | P | P | P | P | P | P | P | P | P |
| PCAD-31-02 | P | P | P | P | P | P | P | P | P | P |
| PCAP-31-03 | P | P | P | P | P | P | P | P | P | P |
| PCED-30-02 | P | P | P | P | P | P | P | P | P | P |
| PCEP-30-02 | P | P | P | P | P | P | P | P | P | P |
| PCPP-32-101 | P | P | P | P | P | P | P | P | P | P |
| SALESFORCE-AGENTFORCE-SPECIALIST | P | P | P | P | P | P | P | P | P | P |
| SALESFORCE-PLATFORM-ADMINISTRATOR | P | P | P | P | P | P | P | P | P | P |
| SALESFORCE-PLATFORM-APP-BUILDER | P | P | P | P | P | P | P | P | P | P |
| SALESFORCE-PLATFORM-DEVELOPER | P | P | P | P | P | P | P | P | P | P |

## Per-guide findings and evidence

### PANW-CYBERSECURITY-APPRENTICE

- **Checks 1–8 and 10: passed.** The complete May 2026 datasheet's seven domains and 16/16/14/10/13/13/18 weights match the guide's map. Its 39 objective entries, including nested identity details, are represented substantively across the seven sections, examples, labs and original questions. The handbook and FAQ claims are kept distinct from the datasheet omissions; booking details are explicitly left to the appointment. The local/synthetic lab boundaries and proposed infrastructure activities are stated. Winter/product content is not introduced into this guide.
- **Check 9: passed.** The current passed source-validation receipt is dated 2026-10-29 and binds the exact current objective hash. The October 29 record reports 26 links, 23 reachable, three access-blocked and zero missing/error; its notes distinguish browser-observed source content from automated HTTP health.
- The prior low-severity PAN-OS source-association note is repaired: `panw-panos-122-new-features.supported_exams` now includes this guide. Product-version detail remains explicitly outside the exam scope.

### PCAD-31-02

- **Checks 1–2, 4–8 and 10: passed.** Five current objective blocks and weights are mapped to substantive analysis, code, labs and answers. PCAD-31-02 remains active; the guide correctly distinguishes the PCED-aligned PD101 course from full PCAD coverage. NumPy's stated Python 3.12–3.14 support and Pandas 3 compatibility caveats are separated from exam requirements. Workbook data and HTTP examples are synthetic/local; broader exercises are accurately marked pending.
- **Checks 3 and 6: passed.** The Oct 29 guide text labels the exact observation date, distinguishes the web-reader observation from the automated 404, and tells readers to confirm live pages and purchased entitlements. The Oct 29 source-catalog rows document full-page browser observations for the exact practice kit and bundle, including the limits/profile wording and the health-client disagreement. This supports the bounded provider claims without treating HTTP 404 as proof of product removal. The issuer credential page independently supports the current exam contract and prices.
- **Check 9: passed.** The current passed source-validation receipt is dated 2026-10-29 and references the current objective hash `c0e03d205f2bb78e1902508ab699839dee11825423eebe0da9a68832ca657275`; the previous byte-exact snapshot remains archived.

### PCAP-31-03

- **Checks 1–8 and 10: passed.** The five-section syllabus map and weights align to the current 31-03 outline. The Oct 31 change is accurately presented as pending: official issuer page says 31-03 active and 31-04 pending as of Oct 29. The Python runtime release note is labeled context rather than a required interpreter. Examples use bounded local programs; questions remain original and the credential/retake/source conflicts are bounded.
- **Check 9: passed.** The current passed source-validation receipt is dated 2026-10-29 and references objective hash `49589f9a3aaa766a2b2c1a640ac5dbbf7842c01d2517397519ab35ac86a060b0`; the prior byte-exact snapshot remains archived.

### PCED-30-02

- **Checks 1–2, 4–8 and 10: passed.** The four objective domains are taught with an original synthetic data workbook and clearly limited claims. PCED-30-02 remains active, the 30-01 voucher caveat is attributed to the issuer, and PD101 is labeled PCED-aligned while explicitly not claimed as full PCAD preparation. Numeric comparisons and the chart describe invented observations and disclaim real-world or causal inference.
- **Checks 3 and 6: passed.** The updated line 25 labels the exact Oct 29 web-reader observation and discloses that the automated health client returned 404 for both cited store URLs; it asks candidates to confirm current page and purchased entitlement before relying on launch limits or instructions. The source-catalog rows record the full-page browser observations, exact URLs, terms read and automation disagreement. Product/version conflict is visible and bounded.
- **Check 9: passed.** The current passed source-validation receipt is dated 2026-10-29 and references objective hash `27c6f07ec4b1e1063e5cbb6effd00e13406e15d8ee54a2e748c50dff86c24b90`; the prior bytes remain archived.

### PCEP-30-02

- **Checks 1–8 and 10: passed.** Fifteen objectives and four weights remain substantive in code, scenarios and answer explanations. The issuer page confirms PCEP-30-02 active and 30-03 pending for Oct 31, 2026; guide explicitly directs candidates to recheck the purchasable code and version. Current runtime patch versions are not promoted to exam scope. Local examples and labs do not require a remote service.
- **Check 9: passed.** A passed source-validation receipt dated 2026-10-29 uses the current objective hash `fc0a0b67b1f15a4430075b889978a82e162d98642f0b822768bc3796c322ca57` and reports zero missing/error links.

### PCPP-32-101

- **Checks 1–8 and 10: passed.** Current 32-101 sections and objectives are covered by explanation, original runnable examples, 12 focused labs and checks. Issuer status still says 32-101 active, 32-102 pending for Oct 31; validity distinction is retained. The guide contains the previously missing built-in subclassing explanation/example/lab/check and keeps wrappers distinct. Current review evidence now maps 12 labs; the old ledger's lab-count mismatch was corrected and is marked resolved in its separate repair-verification audit.
- **Check 9: passed.** A passed source-validation receipt dated 2026-10-29 uses the current objective hash `899426a902f78aba1471211f0c1eeace8016a66eb8dac3407d013d97cdaafcd6`; the previous byte-exact snapshot remains archived.

### SALESFORCE-AGENTFORCE-SPECIALIST

- **Checks 1–8 and 10: passed.** The current Spring ’26 six-domain outline and weights remain distinct from Winter ’27 product notes. The October update is labeled related implementation context and carries rollout/API/access conditions; it does not present MCP or Agent Script additions as exam changes. Org activities are proposed, use synthetic data and note that evaluations can mutate CRM data/consume credits. The practical worksheet is optional and its no-code study path is stated.
- **Check 9: passed.** A passed source-validation receipt dated 2026-10-29 references current objective hash `a633fd73b5f733d78426c5c66eebf566a7867d80a36ddadd505dbd8ef29b5664` and accounts for the new Winter ’27 context as separate from exam scope.

### SALESFORCE-PLATFORM-ADMINISTRATOR

- **Checks 1–8 and 10: passed.** The Trailhead prep unit currently states the eight 15/15/10/10/10/17/15/8 weights, including Agentforce. The guide distinguishes these current learning weights from the Help exam guide's retained Summer ’25 label and flags booking logistics for verification. The Winter ’27 API 68 flow/security detail is tied to eligible versions/callers and explicitly not used to assert a new exam outline. Labs use authorized orgs and synthetic data.
- **Check 9: passed.** A passed source-validation receipt dated 2026-10-29 binds current objective hash `b2f9f40f925247562d8d19eed5ad7a33a4b5c10e03b705d2fe34ec88678b7c97` and records the current Trailhead weights separately from the still-season-labeled Help guide logistics.

### SALESFORCE-PLATFORM-APP-BUILDER

- **Checks 1–8 and 10: passed.** Current Summer ’26 exam outline and weights are mapped across the five domains, including AgentExchange, external data sources, Agentforce and Flow maintenance/troubleshooting. Its maintenance discrepancy is accurately represented: the exam guide says three badges yearly, while the dedicated policy says one annual badge and the current schedule assigns App Builder to Winter ’26, available Dec 11, 2025 and due Dec 4, 2026 (Pacific time). The guide keeps both source claims visible and directs candidates to their assigned profile. Current product context stays separate from exam scope.
- **Check 9: passed.** A passed source-validation receipt dated 2026-10-29 binds objective hash `5365cb37f260db38aa6b4a306dd826258e3d85f058b8111352e56a065a965f14`, with the maintenance discrepancy and Summer ’26 outline still visible.

### SALESFORCE-PLATFORM-DEVELOPER

- **Checks 1–8 and 10: passed.** The current 21-objective 27/28/25/20 map is substantively represented. The Help page's stale Summer ’25 label remains an explicit uncertainty; API 67 and Winter ’27 API 68 behavior are bounded to versioned product context and are not presented as exam updates. The 10 MB/25 MB heap limits and CLI secret-output change agree with Salesforce's Winter ’27 developer guide; the guide preserves API/version and rollout caveats. Local code/testing guidance is scoped to scratch/sandbox environments, and labs remain proposed where live org access is needed.
- **Check 9: passed.** A passed source-validation receipt dated 2026-10-29 binds objective hash `4843c3b24a93a1c4da79e50db00e79c38fa5921c6127df89e37a6754c5cddbfe` and preserves the Summer ’25 label uncertainty separately from API 67/68 product behavior.

## Follow-up on first-pass findings

The first read-only pass, before the final targeted edits and receipts, recorded G15-01 through G15-03 as open. The present hashes bind a later verification pass. A summary of the earlier findings and their initial evidence is retained in this report; this reviewer does not alter their ledger disposition. The repairs below were verified against current repository state:

- **G15-01 (check 9, all ten guides):** The missing current receipts are now present. Each is passed, dated 2026-10-29, and uses the exact current objective snapshot hash. All ten current guide/objective/status hashes match the refreshed manifest. These receipts include current link evidence and disclose limits; link-health observations are not represented as technical verification.
- **G15-02 (check 3, PCAD/PCED):** The guide claims now date the Oct 29 web-reader observations and disclose the automated 404 beside the launch/profile terms. The four catalog rows record full-page first-party browser observations on the same date, what was read, and the automated 404 disagreement. The source-health status remains `blocked`/404, correctly reflecting the automated checker; it is not presented as proof the products were withdrawn. The exact URLs returned 404 again in this reviewer’s direct web open, so the guide’s “verify current page and purchased entitlement” caveat remains warranted.
- **G15-03 (check 9, PANW):** `panw-panos-122-new-features.supported_exams` now includes PANW-CYBERSECURITY-APPRENTICE. The guide retains the out-of-scope label, so the source association does not expand exam content.

These follow-up checks leave **no open finding for the current guide hashes**. The prior findings remain historical first-pass observations and should be closed in their owning evidence record by the coordinator after using this verification note.

**First-pass finding record (preserved):** G15-01 was Medium, check 9, for all ten guides because Oct 29 catalog dates lacked same-date source-validation receipts; recommendation was to record current passed receipts against exact objective baselines. G15-02 was Medium, check 3, for PCAD/PCED at their entitlement statements because precise launch/profile terms could not be independently retrieved and the guides did not yet date/disclose the 404; recommendation was to date the browser observation, disclose the automated access discrepancy beside the claims, and retain only issuer-supported terms. G15-03 was Low, check 9, for the PANW guide because the cited PAN-OS source's `supported_exams` array omitted the foundational credential; recommendation was to add that association or remove the citation. The first pass reported all three open; no historical disposition is silently rewritten here.

## Verified resolved issues

- The prior PCPP-32-101 built-in subclassing objective gap is resolved in the current guide: explanation, a direct collection-subclass example, focused lab, readiness item and answer are present.
- The prior PCPP source-review lab map mismatch is resolved in the 2026-09-29 source-validation record; it reports 12 focused labs with the expected domain allocation.
- The prior September guide audits for PCEP, PCAP, PCED, PCAD, PANW and Salesforce guides are treated as historical only; their old content hashes do not bind to this current guide set.

## Source checks and verdict

First-party pages opened directly include:

- Palo Alto Networks [May 2026 Apprentice datasheet](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/education/apprentice-datasheet.pdf), [credential page](https://www.paloaltonetworks.com/services/education/panw-cybersecurity-apprentice), and PAN-OS 12.2 documentation cited in the guide.
- Python Institute [PCEP](https://pythoninstitute.org/pcep), [PCAP](https://pythoninstitute.org/pcap), [PCPP1](https://pythoninstitute.org/pcpp1), [PCED](https://pythoninstitute.org/pced), and [PCAD](https://pythoninstitute.org/pcad) exam pages. As of Oct 29, PCEP-30-03, PCAP-31-04 and PCPP-32-102 are marked pending for Oct 31; current guides retain 30-02, 31-03 and 32-101 scope. Python 3.15.2 / 3.14.10 are runtime context only.
- Salesforce [Administrator certification prep](https://trailhead.salesforce.com/content/learn/modules/administrator-certification-prep-setup-and-objects/get-started-with-administrator-certification-prep), [Platform App Builder exam guide](https://help.salesforce.com/s/articleView?id=005298964&language=en_US&type=1), dedicated [maintenance policy](https://help.salesforce.com/s/articleView?id=005298841&language=de&type=1), [maintenance schedule](https://help.salesforce.com/s/articleView?id=005298922&language=de&type=1), and [Winter ’27 developer overview](https://developer.salesforce.com/blogs/2026/10/developers-guide-to-the-winter-27-release).
- Every guide-cited registered source and matching `data/source-health.json` row was checked. Most blocked rows are commercial/publisher pages explicitly described as paywalled, unreadable, or historical. The PCAD/PCED store pages remain `blocked`/404 in automated health, while the date-bound first-party browser observations and adjacent guide caveats are recorded in the source catalog and guides.

**Overall verdict: pass for the current guide hashes.** All ten applicable checks pass for every guide and there are no open findings under the current binding. The official-source seasonal conflicts and store automation 404s remain visibly bounded, with current receipts recording what was reviewed and what remains inaccessible. This report is fresh-context AI review, not human review or live lab execution.

## Completion note

This file was written read-only except for the explicitly requested report artifact. All listed guide, objective, and status hashes matched the refreshed `.maintenance/g15-review-hashes.json` manifest during the final check.
