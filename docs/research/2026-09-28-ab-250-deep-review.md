# AB-250 deep review — September 28, 2026

The [AB-250 guide](../../guides/AB-250-transforming-contact-center-experiences-ai-dynamics-365.md)
was read in full and mapped to **119 detailed objectives across fifteen groups**.
It now has six worked examples, ten labs, 48 answered checks and two focused WEM
blog exercises. Sixteen offline assertions passed. The review retains an unresolved
conflict in Microsoft's ACS phone-number eligibility and cutoff documentation.

This is same-context AI research and repair; independent human review is pending.
No tenant, telephony, number, carrier, campaign, message, agent, simulation, billing,
workforce record, API/SDK or cloud lab was executed. Paid lessons and signed-in
partner offerings were not accessed.

## Exam and learning baseline

The [official blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-250)
retains its May 15, 2026 page date, with no separate skills-effective date or upcoming
revision. All **119 detailed bullet texts match** the previous accepted baseline.
The monitor found presentation changes: introductory/domain headings, bullet markers,
line wrapping and the synthetic status label. The normalized current snapshots were
accepted only after comparison. Original bytes are archived under
`data/objective-snapshots/ab-250-2026-09-01-official-objectives.txt` and the corresponding
status JSON. Historical review/audit paths now locate those bytes; their dates,
hashes, outcomes and substantive evidence remain unchanged.

The [credential](https://learn.microsoft.com/en-us/credentials/certifications/d365-contact-center-ai-engineer-associate/)
still describes an active English, 120-minute exam without a Practice Assessment.
The four Learn paths expose **16 modules: 4 + 4 + 5 + 3**. Their previously recorded
11h 40m total is historical because the retrieved current pages do not expose those
durations. The three-day course remains listed. The guide's 40–70-hour preparation
budget is editorial, not a vendor completion guarantee.

The public [LinkedIn Learning outline](https://www.linkedin.com/learning/microsoft-dynamics-365-contact-center-ai-engineer-associate-ab-250-cert-prep/)
identifies Tutorials Dojo, July 27, 2026 and **4h 38m**. Its outline includes adjacent
cloud/AI topics; learners should filter it against the blueprint. Paid lessons and
their technical accuracy were not inspected. Bounded exact-exam searches for
Pluralsight, O'Reilly, MeasureUp and Whizlabs returned no results in this review;
that is not proof of catalog absence. The partner hub returned a public shell,
not a verified signed-in schedule.

## Objective coverage

Every detailed bullet has a hashed guide mapping in the operation record.

| Objective group | Count | Teaching and evidence |
|---|---:|---|
| Deployment and integration | 7 | Architecture, connectors, embedded UI, agent and simulation boundaries |
| Agent rollout and ALM | 4 | Plans, solutions, environments, dependencies and rollback |
| Users and capacity | 4 | Identity, roles, bookable resources and intersecting profiles |
| Chat and digital channels | 13 | Workstreams, widgets, authentication, SDKs and lifecycle |
| Voice channel | 7 | ACS/Teams paths, numbers, IVR, recording and migration |
| Advanced channel capabilities | 26 | Context, masking, proactive modes, WEM, APIs and cost |
| Representative Copilot | 6 | Grounding, approved knowledge, tools, summaries and adoption |
| Voice agents | 10 | Variables, security, handoff, models, language and tests |
| Queues and assignment | 5 | Priority, hours, methods, overflow and fallback |
| Routing | 10 | Classification, skills, intent, rules, records and diagnostics |
| Representative profiles | 5 | Tabs, inbox, sessions, notifications and persona |
| Productivity | 6 | Panels, scripts, macros, collaboration and APIs |
| Knowledge | 5 | Search, publishing, tables, harvesting and access |
| Supervisor experience | 5 | Roles, quality, monitoring, dashboards and privacy |
| Analytics | 6 | Power BI, models, report access, Application Insights and correlation |

## Material corrections and additions

- **Lifecycle:** separate ACS deprecation, new-service sign-up, new-number access
  and removal dates. Existing affected services have a 2028 migration horizon;
  that does not settle new-customer eligibility. Track September 30 Apple
  configuration removal and October 30 legacy forecasting removal separately.
- **Telephony:** distinguish the ACS and Teams Phone extensibility procedures,
  resource accounts, number synchronization, carrier choices and voice workstreams.
  During Direct Routing coexistence, ACS and Teams cannot share one SBC FQDN;
  alias/certificate and full-cutover paths have different implications.
- **Integration and agents:** separate CRM synchronization from embedded UI,
  clarify current agent responsibilities, supported Service Operations actions,
  preview simulation limits and feature-specific rollout deactivation behavior.
- **Capacity and routing:** explain profile intersections, release/reset rules,
  custom-limit propagation, calendar migration limits, hit policies, routing
  percentages, prequeue/postqueue actions and fallback bypass of overflow checks.
- **Privacy and engagement:** qualify message versus voice masking, first-answer
  timing, independent destinations and requested versus completed recording pauses.
  Explain unique contact keys, engagement priority, UTC fallback, quiet hours,
  queued-call cancellation and the documented progressive/predictive constraint.
- **Workforce and quality:** add current forecast-scenario constraints and the
  limited three-tool WEM MCP catalog. Separate quality criteria, plans, guardrail
  violations, sampling and numeric scores; retain documented use restrictions.
- **Diagnosis:** use event-time eligibility and supported assignment paths,
  acknowledge telemetry lag, deduplicate overlapping diagnostic categories and
  distinguish containment from verified correct outcomes.

The guide cites implementation sources beside the changed explanations. Long
reference and release pages were reviewed in the sections identified by individual
source notes; retrieval is not an exhaustive audit of every linked procedure.

## Unresolved evidence gap

The [Contact Center migration plan](https://learn.microsoft.com/en-us/dynamics365/contact-center/administer/migrate-from-azure-communication-services)
says September 30, 2026 for new-resource phone-number restrictions, while the
[deprecation ledger](https://learn.microsoft.com/en-us/dynamics365/contact-center/implement/deprecations-contact-center)
says September 23 for new customers. Resource-only eligibility language also
differs from the existing-number requirements in the
[ACS retirement guide](https://learn.microsoft.com/en-us/azure/communication-services/acs-retirement-and-breaking-changes-guide).
The latter's October 23 new retiring-service sign-up date has a different scope.
No acquisition guarantee can be inferred by substituting one date for another.
The guide and tracker retain a blocker pending authoritative clarification.

## Blog intake

Both public main articles were read; linked videos, code, integrations, commercial
claims and live service behavior were not reproduced.

- [Edgar Wilson III, September 3](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/09/03/dynamics-365-workforce-engagement-management-mcp-tools/):
  accept a 45–60-minute persona/request/action worksheet. Current tools list and
  inspect requests and decide pending time off; future scheduling, balances and
  clock-in/out ideas are not current tool guarantees.
- [Alan Ross, June 22](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/06/22/workforce-engagement-management-dynamics-3/):
  accept a 45–75-minute staffing/outcome worksheet. The article states June 30
  GA; its adapter and commercial claims were not independently reproduced.

These are supplemental learning exercises, not additional exam requirements.

## Verification and follow-up

Sixteen offline assertions cover capacity, simulation wall/aggregate time,
fixed-offset quiet hours, workload/staffing, sampling/weighted score, diagnostic
set union, containment denominators and catalog arithmetic. They do not test
the scheduler, billing unit, random sampler, routing engine, forecast accuracy,
queueing SLA or DST behavior. Simulation credits are not extrapolated from an
ambiguous multi-conversation billing unit.

Three dated follow-ups cover September 30 number/Apple changes, October 30
forecasting removal and October 12 feature-support matrices. The shared learning
catalog is synchronized from the guide and checked for drift. Exact citation
counts, fetch results and executed repository/unit/site checks are recorded in
`ADLC_Docs/operations/2026-09-28-ab-250-deep-review.json`. A successful HTTP response
does not establish full content access, semantic accuracy or independent review.

All **50** guide citations are registered and returned reachable HTTP responses;
none returned a missing/error classification. The partner hub's content shell is
explicitly a semantic access limitation despite its successful HTTP response.
