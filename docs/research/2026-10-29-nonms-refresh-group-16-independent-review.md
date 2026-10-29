# Group 16 independent semantic review

**Review date:** 2026-10-29
**Mode:** Read-only, fresh-context AI semantic review
**Rubric:** `docs/AI-AUDIT.md`, rubric version 2
**Manifest:** `.maintenance/2026-10-29-nonms-refresh/g16-audit-manifest.json`

I reviewed the complete guide text, front matter, objective and status snapshots, catalog rows and certification seeds, dated source-validation records, registered source metadata and health records for all ten items. I also checked relevant public first-party pages and documentation, especially where lifecycle, product behavior or official-source contradictions matter. All guide and objective snapshot hashes match the manifest. No tracked guide, catalog, snapshot, source, health or review record was changed.

## Binding and evidence summary

| Code | Guide SHA-256 | Objective snapshot SHA-256 | Latest source-validation receipt |
|---|---|---|---|
| SY0-701 | `4bf5c3922b15b5e2f90c210da49e70321dae545f9ae06812f28a7c2122ef6947` | `152af64f7b23ff8a264ea9aa465c610cc797fcdd6b771d8f7dfe15cdab6b9040` | `sy0-701-2026-10-29-source-validation`, passed |
| XK0-006 | `129dc9d029d11a26520e2c7b93e78d416259acf04eefc30f8a9171a2d29ad7dc` | `7092fafe78142df3f4be33e42aea257143769cc6268b90a4e1059f994c00496e` | `xk0-006-2026-10-29-source-validation`, passed |
| SOL-C01 | `1c2ea489f9e69407bfb904ad545b4b1d8a3dcfa2f28e722540a70f1cc8d98337` | `a930a723415ca1b8dfead2cf60a3d27b6c7eaf3d336fefc301421adee9123d57` | `sol-c01-2026-10-29-source-validation`, passed |
| SSCP | `72e1c109d49736ae189372894dc0218c9a9ccccf13d0db354ddbb4108267dc42` | `5b6e5e57f166741802957b515a7ec737606e5d43ca796a3691127de083d0a6d4` | `sscp-2026-10-29-source-validation`, passed |
| SERVICENOW-CSA | `a58d433383ce405b6f4189826934cfa6b7e69d3367d1000c46fa7e60c84c1061` | `7b94b0c2b2f331a2e878694c8b9aaa6db8e998bfc0424d75dca80e6cdbe1d553` | `servicenow-csa-2026-10-29-source-validation`, passed |
| SERVICENOW-CAD | `32982f9f2eea0c23566a70c3310c343ec195a8e96af70f5a7481b5d1528e0852` | `f71371fc8583ec438fbdde805d2e69d8034607333e1bc033ccc74ae5a261b59a` | `servicenow-cad-2026-10-29-source-validation`, passed |
| SPLK-5001 | `ca5df8d4b90b29d9c03ce64b648f9e9d56d94b857aebf48cfdf183c3d2228115` | `a2bd1aa1350f373525e5d2f66cfc38f7023f6b84cf9275f594421412fbd704f5` | `splk-5001-2026-10-29-source-validation`, passed |
| WDE-40-01 | `4a2a90bcbfa531fa052e1b1c7fa0cd9dd9a7b6ddf19066d0677392b8ed0a8d82` | `52a8efac1190c7d5b3e863705d0a0b7d4ea88ad72834aff4990051f21a9a7521` | `wde-40-01-2026-10-29-source-validation`, passed |
| WDA-41-01 | `bc72ba612cc3499a0c94984057c806328a28f75edf1c4610db5996f83b06c90f` | `747cb21a7c881c08b2b1107feb22733528ec25faab300998abb8ac499af07c5d` | `wda-41-01-2026-10-29-source-validation`, passed |
| PCET-30-01 | `453345f470b3711932cce23e374dc1ea28edbe636940e408e11b984f5b1c5baf` | `2ba098e2104bb457258687cdcd07afcc3a531ab146c27b0022a9bebb5d793aec` | `pcet-30-01-2026-10-29-source-validation`, passed |

Each exam code resolves to a matching vendor/title/guide row in `config/exams.json` and vendor/title/official URL in `config/certification-seeds.json`. Catalog lifecycle is active for all except SOL-C01, which is retired May 4, 2026; its guide identifies itself as a retired reference and directs new candidates away from booking it.

Registered source and health records were reviewed per manifest. The health exceptions are disclosed in the guides/source-validation notes: blocked or inaccessible third-party/paid pages for Security+, Linux+, SOL-C01, SSCP, ServiceNow and Python Institute; Splunk has 15 blocked, one error and 15 `ok` among 31 registered records; WDE and WDA official issuer pages have automated timeout/blocked health statuses despite manual public-browser review being recorded; PCET records blocked official pages and one missing Flake8 candidate URL, alongside separate current source checks. A missing or blocked health result was not treated as technical evidence. For the time-sensitive Splunk ES terminology, public official Splunk ES 8 documentation independently corroborates the guide’s distinction between `notable event`/`risk event` and `finding`/`intermediate finding`, and its use of Mission Control/analyst queue. Source health is only reachability metadata.

## Rubric check results

`P` = passed. The status applies to the full guide at the hash above. Open observations are listed separately below; none is a failed required check.

| Code | 1 Scope | 2 Coverage | 3 Claims | 4 Contract | 5 Technical | 6 Volatility | 7 Labs | 8 Readiness | 9 Evidence | 10 Duplication / contamination | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SY0-701 | P | P | P | P | P | P | P | P | P | P | Pass |
| XK0-006 | P | P | P | P | P | P | P | P | P | P | Pass |
| SOL-C01 | P | P | P | P | P | P | P | P | P | P | Pass |
| SSCP | P | P | P | P | P | P | P | P | P | P | Pass |
| SERVICENOW-CSA | P | P | P | P | P | P | P | P | P | P | Pass |
| SERVICENOW-CAD | P | P | P | P | P | P | P | P | P | P | Pass |
| SPLK-5001 | P | P | P | P | P | P | P | P | P | P | Pass |
| WDE-40-01 | P | P | P | P | P | P | P | P | P | P | Pass-with-notes |
| WDA-41-01 | P | P | P | P | P | P | P | P | P | P | Pass-with-notes |
| PCET-30-01 | P | P | P | P | P | P | P | P | P | P | Pass-with-notes |

### Findings (all open informational observations)

1. **Info — WDE-40-01, check 4 (exam-contract integrity), lines 20, 23–25, 797, 814.** Official public pages conflict on delivery channel and supervision: the Institute homepage advertises Pearson VUE/OnVUE while the credential page says TestNow; generic TestNow policy text also conflicts about proctoring. The credential page separately labels its practice-test row `WDE-41-01` although the active exam and syllabus identify `WDE-40-01`. The guide explicitly preserves both conflicts, warns against interpreting the typo as a new version, and directs learners to verify product terms before purchase. Recommendation: retain this boundary and update only when exam-specific authoritative terms resolve it. Evidence: [WDE certification page](https://jsinstitute.org/wde-certification), [WDE syllabus](https://jsinstitute.org/wde-exam-syllabus), [Institute homepage](https://jsinstitute.org/), [TestNow policies](https://jsinstitute.org/test-now-testing-policies). These are issuer-page inconsistencies, not an unsupported guide assertion.

2. **Info — WDA-41-01, check 4 (exam-contract integrity), lines 18–20, 22 and 838.** The current certification page gives internally inconsistent duration text (`60 minutes` alongside tutorial/NDA and `~65 minutes` exam detail) and contains future JavaScript/Node.js roadmap language without a version/date. The guide flags the duration ambiguity and does not promote roadmap prose to a replacement or retirement. Recommendation: keep the duration caveat pending product-specific clarification; recheck for an actual versioned announcement. Evidence: [WDA certification page](https://jsinstitute.org/wda-certification), [WDA syllabus](https://jsinstitute.org/wda-exam-syllabus).

3. **Info — PCET-30-01, checks 1 and 4 (official scope and exam-contract integrity), lines 19, 40–42, 869, 883–891.** The official syllabus header, alignment and active credential page identify PCET-30-01, but introductory syllabus prose says PCET-30-02 and includes unrelated data-analysis language; objective 1.4 has a mismatched heading. The guide explains the conflict, retains the coherent 22-objective testing map, notes the generic credential-page code, and does not infer a launched replacement. The official page currently confirms `PCET-30-01` / `ACTIVE` while retaining the inconsistent prose. Recommendation: retain the warning and revisit only when the issuer corrects or clarifies the source. Evidence: [PCET syllabus](https://pythoninstitute.org/pcet-exam-syllabus), [PCET credential page](https://pythoninstitute.org/pcet).

No open medium, high or critical finding was identified. The informational findings concern source-page inconsistencies the guides already disclose; they do not require a content repair on the evidence reviewed.

## Guide-level semantic observations

- **SY0-701:** Correct V7 identity, weights and 28-objective structure; V8 preparation is visibly separate from current V7 scope. Retirement language distinguishes V7 availability from the announced successor. Crypto/PKI exercises distinguish locally executed synthetic examples from production CA, live revocation, hardware and TLS work. The guide bounds tests/labs and avoids asserting live CVE or deployed detection results.
- **XK0-006:** Correct V8 identity and 29-objective/weight map. The guide identifies CompTIA wording errors (`nmconnect`, `vit-manager`, `systemd-blame`) without silently substituting objective scope, and repeatedly bounds distribution/version variability. Labs require disposable systems, target checks and recovery; answer guidance is consistent with stated examples.
- **SOL-C01:** Correctly treated as retired, with May 4/May 5 transition distinction and skills badge explicitly separated from a professional certification. The guide does not represent the six preserved abilities as a current replacement-assessment blueprint. Product/UI/role/access volatility and non-executed labs are clear.
- **SSCP:** Uses the October 1, 2025 active outline and seven official domains/weights. Credential experience, CAT and maintenance details are separately labeled and bounded. Current NIST identity, response and cryptography references are presented as contextual updates rather than substitutions for the outline. Technical labs and TLS examples are separated from infrastructure execution.
- **SERVICENOW-CSA:** Matches January 2026 blueprint domains/weights and 30 subtopics. Conditional results, unpublished cut score, delivery, 90-day attempt window and maintenance are appropriately caveated. Release, account entitlement, PDI and annual delta context is separated from exam scope.
- **SERVICENOW-CAD:** Matches January 2026 six-domain blueprint and subtopics. Scoped-app design, ACLs, Glide APIs, automation, integration and transport material is described with release, execution-context and permission caveats. No production execution or PDI access is claimed.
- **SPLK-5001:** Maps six domains and 24 objectives; exam requirements are distinct from recommendation and lifecycle material. Version-specific ES terminology is explicitly contrasted with blueprint vocabulary; guides users to bridge old test terms to ES 8 and does not claim a Splunk/ES/SOAR environment or full paid course access. Offline examples are labeled as such.
- **WDE-40-01:** Maps the active 40-objective HTML credential. Browser and accessibility guidance is technically bounded; the recorded download/audio limitations are preserved. Issuer delivery/product inconsistencies are not hidden. The ten lab proposals are distinguished from the bounded earlier local browser examples.
- **WDA-41-01:** Maps the active 40-objective HTML/CSS credential and five block weights. Current standards guidance is clearly described as related context. The guide bounds the partially accessible syllabus PDF and avoids inferring an exam replacement from the roadmap text.
- **PCET-30-01:** Maps four blocks, 22 numbered objectives and 35 items without conflating measures. The complete original workbook and its limited execution claims distinguish unit/local evidence from real provider, integration, IDE and human-review evidence. It accurately warns about issuer contradictions and unverified policy/course access.

## Practical limitations

This was an AI read-only review of public repository evidence and public sources, not human/community review. I did not purchase or access paid course interiors, enter accounts, book exams, run product labs, execute the guides’ code/workbooks, use browser developer tools/tests, or validate live vendor instances. Health receipts do not establish source support or technical correctness. Some official-source automated access is blocked/timed out and issuer content may change after this date. The three informational observations remain open and are not marked resolved, accepted-risk, or dismissed.

## 2026-10-29 follow-up: ServiceNow CAD source alias

After the manifest regeneration, I rechecked the source alias and the full Group 16 bindings. All ten current guide hashes and objective snapshot hashes still match the manifest, and all ten `source_validation_review_id` values are unchanged from the prior review. SERVICENOW-CAD remains bound to guide hash `32982f9f2eea0c23566a70c3310c343ec195a8e96af70f5a7481b5d1528e0852`, objective hash `f71371fc8583ec438fbdde805d2e69d8034607333e1bc033ccc74ae5a261b59a`, and review `servicenow-cad-2026-10-29-source-validation`.

The current manifest registers `servicenow-cad-mainline-blueprint-canonical` at `https://learning.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0011498` as the public, authority-class-1 `exam-blueprint`; `data/source-health.json` records HTTP 200 / `ok` on October 29, 2026, with the same final and canonical URL. The corresponding source row says the canonical article was opened and reviewed for the January 2026 blueprint and current exam contract. The older `servicenow-cad-mainline-blueprint` row remains as a historical alias to the legacy `/lxp/en/credentials/...KB0011498` URL, with its September 29 health receipt and an explicit note that it is retained for dated freshness findings. The prior September freshness findings still reference that legacy URL and source ID; the new canonical record is separate. The Group 16 freshness result is `current` and records the canonical route.

This is a source-record/history repair only. It changes none of the reviewed guide or objective content, so the prior **7 pass / 3 pass-with-notes** verdicts remain valid. The three notes remain the already disclosed issuer inconsistencies for WDE-40-01, WDA-41-01 and PCET-30-01. This follow-up is read-only apart from this addendum; it does not claim human review or live ServiceNow product execution.
