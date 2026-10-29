# Google Professional Agentic Architect tool coverage repair — October 29, 2026

## Scope and source review

The official Google Cloud exam guide PDF was reopened at https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf and the certification page at https://cloud.google.com/learn/certification/agentic-architect/. The guide still lists five weighted domains and 28 named tool-list entries. The existing objective snapshot remains byte-identical (SHA-256 `116a4f1d0a6ee037866c312dc554b8f132248f1cbaddaf837fdce48c0116d454`). Official product documentation was checked for the expanded entries; source IDs and URLs are registered in `data/sources.json`.

## Repair

The Google Agentic Architect guide now has an individually mapped table for every named tool entry. Each row explains the tool's role, when to select it, a failure or authorization boundary, and a learner validation check. Agent Retrieval (the current name for Vector Search 2.0) and Vector Search 1.0 are distinct rows. Preview and naming volatility is labeled. The table is study guidance, not a claim that any product was deployed or executed.

## Link evidence and limits

The 49 unique external links in the guide resolve to registered catalog sources. Automated source-health evidence reports 48 healthy and one blocked; none are missing or broken. The Antigravity Workbench CLI page timed out in the local fetcher, but direct browser access on October 29 confirmed the official page and its Preview documentation. The catalog and report retain the blocked automated status.

The refresh and this repair used public documentation only. No recalled exam items or live product behavior are represented. A fresh-context independent audit is required before closing the prior finding.
