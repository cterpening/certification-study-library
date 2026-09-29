# Professional Machine Learning Engineer deep review — September 29, 2026

The guide now maps **52 considerations under 14 numbered objectives** from the actual five-page exam PDF, which prints June 1, 2026. Counts by domain are 9/10/12/10/5/6. The approximate 13/16/21/20/18/13 weights total 101% as published; no replacement percentages were invented.

The objective digest is unchanged. The canonical page describes an already-completed branding update, not a future effective date. Its two-hour, USD 200, 50–60-question English/Japanese exam details were reviewed. It has no formal prerequisite and recommends three years of industry experience including one year with Google Cloud. A missing lifecycle baseline was explicitly initialized after that review, and a subsequent check was unchanged. Separate official certification help supplies the generic professional two-year validity statement; renewal offers are not borrowed from other exams.

## Teaching changes and primary evidence

Latest feature serving and historical training now have explicit boundaries. Current [Feature Store source preparation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/prepare-data-source) distinguishes registered historical time series from direct one-row-per-entity sources. The guide adds late-arrival leakage, event/availability cutoffs and null/synchronization behavior. A null does not universally remove an older serving value.

The experiment and readiness material separate fitted preprocessing, validation threshold selection, final held-out evaluation, support counts and aggregate versus subgroup performance. Model artifacts bind preprocessing, data fingerprints and decision threshold. BigQuery ML prediction follows its stored transformation contract; unused columns can pass through without influencing predictions.

Custom-container teaching separates TCP connectivity, model readiness and traffic removal from restart behavior. Online scaling metrics, quotas and current Scale To Zero Preview restrictions are distinct from batch prediction's starting-replica contract. The [pipeline cache](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-caching) has no automatic TTL; immutable data/image versions and explicit fingerprints must express meaningful changes.

[Model Monitoring](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview) v1 remains GA and endpoint configured. V2 is Preview, model-version associated and currently tabular; externally served reference models cannot use feature attribution monitoring. Scheduled and on-demand jobs each perform a batch execution. These facts do not establish universal real-time LLM evaluation. Drift initiates investigation and candidate evaluation rather than granting deployment approval.

Previously read same-session primary sources, re-fetched successfully, support separate retention, enforcement integration and permission-aware retrieval boundaries. The full April 22, 2026 Brian Delahunty/Michael Gerstenhaber announcement supplies naming context only. Product-page reading was selective; detailed per-source limits are retained in the operational evidence.

## Executed evidence and remaining work

The exact public standard-library Python program passed **36 checks**. It actually trains a logistic classifier on 120 synthetic rows, fits normalization only on training data, selects a threshold from five candidates using 30 validation rows, serializes/restores the model contract in memory, and then evaluates 30 held-out rows. Threshold 0.35, training loss approximately 0.1934, validation cost 4 and held-out cost 2 were observed. Held-out results were 13 TP / 15 TN / 2 FP / 0 FN, or28/30 correct. Slice B has just 6 rows and 1 positive; its perfect result is insufficient release evidence.

A separate original fixture improves aggregate accuracy 82% → 90% while slice B recall collapses 100% → 0%; a declared slice-support/recall gate rejects it. Another fixture leaves inputs unchanged while reversing labels, demonstrating the limit of input-only drift detection. Undefined metrics retain their missing denominators rather than becoming perfect scores.

This is a tiny deterministic synthetic experiment with structural assertions, not a calibrated model, statistically powered benchmark or cloud implementation. The interleaved split does not implement real temporal/entity splitting. The five-positive/0.8 recall toy gate is not statistical assurance. Exact public-code digest, runtime, output and reading receipts are recorded. No third-party ML dependencies were installed, and no filesystem data, network, authentication or infrastructure was used by the workbook.

The guide includes **48 answered checks**, three integrated scenarios and **eight proposed cloud labs** with failure cases, evidence and cleanup. Live training, accelerator recovery, feature serving, pipeline caching, endpoint readiness and monitoring still need execution in an authorized cloud environment. Independent human review remains pending.

## Catalog comparison and validation

Google Skills exposes 17 activities and a relative two-month update, without durations; the older 57h45 estimate is unverified. Coursera currently exposes two courses of 15h and 4h, totaling 19h. Its landing estimate of two months at 10h/week conflicts with an FAQ of six months at 5h/week; the FAQ also names a first course absent from the visible cards. Treat these as inconsistent public metadata.

The current Pluralsight path has six courses totaling 446 minutes (7h26), versus a rounded 7h header, dated February–June 2026 by Victor Dantas and Abhishek Kumar. It still displays an in-production notice. Whizlabs returned an empty readable body; O'Reilly returned 403. Paid interiors and proprietary assessments were not accessed. Suggested lab budgets are editorial estimates, not provider durations or guarantees of exam readiness. Places to learn is last.

The operational record captures local execution and, once completed, repository/unit/catalog/strict-site/generated-site/diff validation. Source freshness is current; the program outcome remains **reviewed with blockers** for live-cloud execution and independent human review.
