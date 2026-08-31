# Project brief

## Summary

Certification Study Library is a public, vendor-neutral site that turns public certification objectives and documentation into cited, AI-assisted study guides. It also catalogs legitimate official and third-party training without copying protected material.

## Problem

Certification blueprints, product behavior, training catalogs, exam logistics, and feature names change independently. Learners must reconcile official objectives with books, courses, videos, repositories, labs, and practice assessments that may target different blueprint versions.

## Goals

- Discover active, beta, changing, and retired credentials.
- Preserve dated snapshots of canonical public objectives.
- Generate a useful page for every registered exam.
- Map each objective to cited explanations and training resources.
- Identify source gaps and volatile product claims.
- Publish through a searchable static site.
- Make provenance and AI involvement visible.
- Support public corrections without accepting confidential exam content.

## Non-goals

- Reproducing live exam questions or paid question banks.
- Predicting undisclosed exam questions.
- Replacing vendor documentation or instructor-led training.
- Scraping authenticated course material.
- Automatically publishing unsupported AI claims.
- Storing employer, customer, or proprietary content.

## Initial scope

The five original public-source GitHub certification guides are the reference implementation. AI-103 and AB-100 test the common schema across developer and solution-architect roles. AZ-900, DP-900, PL-900, SC-900, AB-900, and AI-901 extend the Microsoft sample across all active 900/901 Fundamentals credentials as of August 31, 2026. Terraform Associate (004) is the first non-Microsoft-platform pilot: it proves dynamic provider navigation, an unweighted objective map, and a HashiCorp-specific objective adapter.

Discovery is intentionally broader than publication. The research inventory now covers every certification in Microsoft Learn's Azure product facet and every current HashiCorp certification, while the published exam registry contains only complete, reviewed guide drafts. Adding a discovery seed never creates an empty page or implies that a guide exists. Later guide samples from AWS, Google Cloud, Databricks, or other vendors should continue testing genuinely different blueprint platforms before full guide coverage is attempted.

## Success criteria

- Every registered exam has a canonical source and freshness state.
- Every material generated claim can be traced to a registered source.
- A source change marks dependent content for review.
- The site builds with no broken local links or malformed metadata.
- Contributors can add an exam or training resource without changing generator code.
- Public-content and exam-integrity policies are enforced during review.

## Publication states

| State | Meaning |
|---|---|
| AI-generated draft | Generated from registered sources; full review incomplete |
| Source-validated | Objective coverage and citations checked |
| Community reviewed | A contributor reviewed the complete guide |
| Review required | A canonical source changed after review |
| Retired | The credential is no longer active |
