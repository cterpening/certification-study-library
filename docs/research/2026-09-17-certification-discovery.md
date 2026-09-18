# Certification discovery review — September 17, 2026

Follow-up: the [broader catalog audit](2026-09-17-catalog-audit.md) covers all
registered vendors and adds verified findings beyond this original shortlist.

This targeted review compares public vendor pages with `config/exams.json` and
`config/certification-seeds.json`. It identifies gaps in the library, not necessarily
credentials first announced since September 7. It is not an exhaustive vendor census.
No new credential has been registered as a published guide in this review.

| Candidate | Official evidence and current boundary | Repository disposition |
|---|---|---|
| Google Gemini Certified Educator | [Google for Education catalog](https://edu.google.com/learning-center/certifications/) lists an exam, preparation path, and three-year validity; free of charge. | Missing; useful education-focused pilot. |
| Google Gemini Certified Faculty | Same catalog lists a higher-education faculty route with an exam and three-year validity; free of charge. | Missing; evaluate separately from the educator route. |
| Google Gemini Certified Student | Same catalog lists separate K–12 (ages 13+) and university (18+) routes, free with three-year validity. | Missing; preserve audience and eligibility distinctions before defining guide identities. |
| Cisco AI Technical Practitioner, 810-110 AITECH | [Official exam page](https://www.cisco.com/site/us/en/learn/training-certifications/exams/aitech.html) provides scheduling and a public blueprint covering generative AI, prompting, security, research, code/workflow optimization, and agents. | Missing; strong technical AI candidate. Cisco's AIBIZ learning badge is a different offering. |
| Cisco Data Center AI Infrastructure Specialist, 300-640 DCAI | [Official exam page](https://www.cisco.com/site/us/en/learn/training-certifications/exams/dcai.html) describes the specialist credential and its use as a CCNP Data Center concentration. | Missing; infrastructure-focused candidate. |
| NVIDIA Professional Agentic AI, NCP-AAI | [Official page](https://www.nvidia.com/en-us/learn/certification/agentic-ai-professional/) publishes scope and a study guide, but still displays “Coming soon” alongside registration links. | Missing; verify actual delivery availability and reconcile the published weights before promoting to the current inventory. |
| NVIDIA Professional Generative AI LLMs, NCP-GENL | [Official page](https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-professional/) publishes scope, but also retains “Coming soon” beside registration links. | Missing; availability watch item, not a confirmed newly available exam. |
| AWS SAP-C03 and DVA-C03 | [September 1 announcement](https://aws.amazon.com/blogs/training-and-certification/september-2026-new-offerings/) schedules registration for October 27, SAP-C03 delivery for November 17, and DVA-C03 delivery for December 1. Detailed guides are due when registration opens. | Future versions, not new credential families; retain SAP-C02/DVA-C02 as the current exams and review their transition warnings. |

The Gemini credentials above belong to Google for Education. Google's Cloud catalog
separately includes Generative AI Leader and Professional Agentic Architect, both
already represented here. AWS AI Business Strategist (AIB-C01), the MLA-C02 beta,
Microsoft AI-500, and GitHub GH-600 are also already represented; they are not new
library gaps found by this review.

Suggested next production choices are Gemini Certified Educator and Cisco AITECH,
followed by the other education audiences and DCAI. This ordering is a maintainer
decision; first recheck each public blueprint and lifecycle contract. NVIDIA remains
a watch item until its availability wording is reconciled. Revisit the AWS replacement
blueprints on October 27 rather than inventing their detailed objectives now.
