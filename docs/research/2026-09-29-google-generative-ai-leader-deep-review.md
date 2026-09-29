# Generative AI Leader deep review — September 29, 2026

Same-context AI review; independent human review pending. [Study guide](../../guides/GOOGLE-GENERATIVE-AI-LEADER-generative-ai-leader.md).

## Scope and terminology

Read the actual [five-page exam PDF](https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf) and the full extracted text of the [eleven-page study workbook](https://services.google.com/fh/files/misc/generative_ai_leader_study_guide_english.pdf). There are 61 enumerated considerations under 15 numbered objectives: groups 21/18/10/12, weights 30/35/20/15. Three data considerations repeat in two objectives and remain mapped as published. Both monitor hashes are unchanged; no accepted snapshot was rewritten. Actual PDF bytes and hashes are retained. The workbook extractor reported malformed numeric graphics operands; diagram completeness was not independently established.

The [certification page](https://cloud.google.com/learn/certification/generative-ai-leader) says the exam was recently rebranded but supplies no revision date. Delivery and lifecycle details remain unchanged. The exam still names Cloud Functions and Customer Engagement Suite while workbook labels differ; the guide preserves the exam boundary and explains product aliases. Cloud Digital Leader's separate course-renewal details are not imported.

## Teaching improvements

The full [Google Research soft-prompt article](https://research.google/blog/guiding-frozen-language-models-with-learned-soft-prompts/) supplies the conceptual distinction between learned input vectors and manually engineered text. Its historical benchmarks and training settings are not recommendations for current models. A lifecycle table now separates Model Garden discovery, [Registry version management](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction), serving, feature management and drift evidence.

Current [Developer API terms](https://ai.google.dev/gemini-api/terms) and [Agent Platform retention documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention) establish why account/service treatment and stored data must be evaluated separately. No-training commitments do not eliminate all retention. The guide distinguishes personal notebook use from the preview enterprise notebook API and checks the exact Gemma version's license boundary.

[Identity configuration](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider) makes custom-source access control a creation/migration design decision. Structured JSON is separated from semantic correctness, authorization, exact approval and safe replay. Model Armor detection and model refusal do not themselves prove integration enforcement. The full [original SAIF article](https://blog.google/innovation-and-ai/technology/safety-security/introducing-googles-secure-ai-framework/) adds six control areas tied to owners and evidence; its linked PDFs were not reviewed. The previously read April 2026 app/platform announcement supplies naming context only.

An exact public Python worksheet passed **27 local checks**. An explicitly limited per-user ACL model checks context construction against trusted current metadata, including revoked/deleted/missing-ACL records. Twenty **invented rubric observations**, not actual model outputs, show an overall pass with a failed group and a task pass with a safety failure. Missing coverage is rejected. Fictional economics distinguish gross time, review/rework, potential capacity value and realized cash savings; break-even adoption depends on the stated fixed-cost assumptions.

There are **48 answered checks**, three integrated scenarios and acceptance/negative cases for **eight proposed labs**. No LLM, cloud ACL, connector, managed retrieval, notebook, model deployment, provider evaluation or real transaction was executed. The small synthetic samples establish no statistical production claim.

## Learning resources and validation

Google Skills confirms five activities but did not expose current durations fully. The [Google-authored Coursera series](https://www.coursera.org/professional-certificates/generative-ai-for-leaders) lists an eight-hour landing estimate while its five cards total twenty hours. [Pluralsight](https://www.pluralsight.com/paths/google-cloud-generative-ai-leader-by-pluralsight) lists four courses totaling 5h44m plus a 30-minute August 11, 2026 lab, rounded to six hours. Metadata and domain titles support comparison, not completed lessons or proven current-feature alignment. O'Reilly/Udemy access was blocked and inherited claims are explicitly unverified. No sample or proprietary assessment questions were read. Places to learn remains last.

The operational receipt records the local checks and, after execution, repository tests, repository validation, catalog consistency, strict site generation, generated-site checks and diff checks. Source freshness is current; the program outcome remains **reviewed with blockers** because live model/cloud verification and independent human review remain outstanding.
