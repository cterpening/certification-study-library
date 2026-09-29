---
exam_code: CCSP
vendor_id: isc2
official_blueprint: https://www.isc2.org/certifications/ccsp/ccsp-certification-exam-outline
content_basis: public-sources-only
generation_method: AI-assisted synthesis
authority: unofficial
review_status: source-validated
last_verified: 2026-09-29
upcoming_change_status: none-announced
upcoming_change_checked: 2026-09-29
---

# ISC2 Certified Cloud Security Professional (CCSP) Study Guide

> **Independent AI-assisted resource — SOURCES + OBJECTIVES CHECKED; HUMAN REVIEW PENDING.** The August 1, 2026 outline, claims, links, credential contract and exam-integrity boundary were checked September 29, 2026. This review maps 38 numbered objectives and executes 24 local encryption/policy checks; independent human review and infrastructure labs remain pending. See the [coverage record](../docs/SOURCE-VALIDATION.md#ccsp-coverage-record).

**Current baseline:** The August 1, 2026 CCSP outline is active. The CAT exam is three hours with 100–150 multiple-choice/advanced items, 700/1000 passing, and English, Chinese, Japanese and German delivery at Pearson testing centers; Chinese appointments use selected windows. The monitored label shortened from Pearson VUE without changing the numbered objectives.<br>
**Upcoming change:** No later revision or retirement announcement was present on the checked outline September 29, 2026.<br>
**Exam versus certification:** ISC2 requires five cumulative years in IT, including three in cybersecurity and one in a current CCSP domain. A relevant degree or CSA CCSK can waive one year only; an active CISSP can substitute for the whole experience requirement. Part-time work and internships may count. A passer without the experience can become an Associate of ISC2 and has six years to earn it. Confirm endorsement/application rules.<br>
**Maintenance — VERIFY CURRENT:** CCSP requires 90 CPEs over three years, including at least 60 Group A; the remaining 30 may be Group A or B. The suggested annual total is 30. Member AMF is USD 135; Associates have separate annual 15 Group A and USD 50 requirements. Check the applicable cycle/category in the [member policies](https://www.isc2.org/policies-procedures/member-policies).

**CURRENT BLUEPRINT:** The [web outline](https://www.isc2.org/certifications/ccsp/ccsp-certification-exam-outline) is canonical. Its [15-page August 2026 PDF](https://edge.sitecorecloud.io/internationf173-xmc4e73-prodbc0f-9660/media/Project/ISC2/Main/Media/documents/exam-outlines/EXAMS-CCSP-Exam-Outline-English-01-2026-V2.pdf) confirms the six weights and detailed scope. The [June 30 announcement](https://www.isc2.org/insights/2026/06/isc2-ccsp-exam-outline-revised) describes a refresh that is now active, not a future change. Keep the explicit AI/ML objectives 1.6 and 2.9 in the study map.

**VERIFY CURRENT:** The public outline's Chinese-window notice includes an impossible April 31 date; use actual booking availability rather than copying that calendar. The [CAT policy](https://www.isc2.org/certifications/computerized-adaptive-testing) distinguishes unscored pretest items, no answer review and breaks that consume exam time. A course percentage or stopping point is not the scaled exam result. [Experience rules](https://www.isc2.org/certifications/ccsp/ccsp-experience-requirements) allow only one year of the degree/CCSK waiver, not two stacked years; the active CISSP substitution and Associate route are separate.

## How to use this guide

CCSP tests vendor-neutral judgment across a shared-responsibility system. For every design, identify business/data obligations, cloud service and deployment model, customer/provider/partner roles, trust boundaries, selected control, contract dependency, observable evidence, failure mode and exit/recovery path. Build in disposable accounts with synthetic data and budgets. Do not scan, intercept or alter a tenant, provider or third-party system without written authority.

> **About related items:** A `Related item:` callout adds prerequisite, architectural or operational context. It supports the topic but does not assert that ISC2 used the wording in the public outline.

## Domain map

| Domain | Weight | Practitioner evidence |
|---|---:|---|
| 1. Cloud Concepts, Architecture and Design | 17% | Responsibility/control matrix, reference architecture, provider evaluation, resilience/exit and governed AI/ML design |
| 2. Cloud Data Security | 20% | Data flow/lifecycle, classification/location, storage and cryptographic controls, rights/retention and attributable events |
| 3. Cloud Platform and Infrastructure Security | 17% | Physical/logical/management-plane architecture, contextual risk, layered controls and tested BC/DR |
| 4. Cloud Application Security | 16% | Threat-modeled secure SDLC, pipeline assurance, dependency/API/workload protections and federated IAM |
| 5. Cloud Security Operations | 17% | Hardened configuration, controlled change, capacity/availability, monitoring/response/forensics and stakeholder records |
| 6. Legal, Risk and Compliance | 13% | Jurisdiction/privacy map, assurance limits, enterprise/provider risk treatment and enforceable cloud contracts |

---

## 1. Cloud Concepts, Architecture and Design — 17%

Cloud characteristics—on-demand self-service, broad network access, resource pooling/multi-tenancy, rapid elasticity and measured service—create both value and control consequences. Distinguish cloud customer, provider, partner, broker and regulator responsibilities. Trace the building blocks: compute/virtualization, storage, network, database and orchestration. A control inherited from the provider still needs customer evidence that the right service, region, feature and configuration are in use.

Compare SaaS, PaaS and IaaS by who operates identity, data, application, runtime, middleware, OS, virtualization, infrastructure and facility layers. Compare public, private, hybrid, community and multi-cloud by governance and dependency, not merely location. Capture portability, interoperability, reversibility, availability, privacy, resiliency, performance, versioning/maintenance, service levels, auditability, regulation and outsourcing. “Multi-cloud” does not automatically remove concentration risk if identity, DNS, keys, deployment or staff remain a single dependency.

Design from data and business obligations. Map the secure data lifecycle; threat-model identities, management/control/data planes, tenant isolation and supply chain; apply cryptography/key management, IAM, sanitization, network inspection/geofencing, hypervisor/container/serverless isolation, patching, hardening, baselines and immutable replacement. Select secure-by-design patterns and a relevant Well-Architected/CSA enterprise framework, then validate functional requirements and non-functional qualities.

BC/DR starts with BIA and dependency mapping. RTO is acceptable restoration time; RPO is acceptable data-loss window. Consider recovery service levels, failover/failback, clean credentials/configuration/data, provider/regional/control-plane failure and exercise results. CBA/ROI informs treatment but cannot silently override mandatory legal or contractual obligations. DevSecOps makes security an owned, automated and evidenced delivery constraint.

Evaluate a CSP against defined criteria: financial/operational viability, architecture, responsibility, security/privacy, location, certifications/attestations, SLA, incident/forensic cooperation, data access/return/deletion and exit. Product certifications such as Common Criteria or FIPS 140 validation apply to defined products/modules and versions—not the entire tenant or application.

For AI/ML, govern intended decision/action, validated data sources, dataset/model access and lineage, detection quality, SOAR permissions, human approval, ethics and regulation. Protect against poisoning, evasion, prompt injection, excessive agency, leakage and model theft; monitor drift and false decisions. AI can prioritize signals but does not transfer accountability.

**Related item:** Portability is the ability to move data/workloads; interoperability is the ability to work together; reversibility is the practical, tested ability to exit and restore an acceptable operating state. A contract promise without export, dependency and restoration evidence is not an exit plan.

---

### Verify a module claim and its current status

**CURRENT BLUEPRINT / PRACTICAL DEPTH:** Objective 1.5 still names FIPS 140-2 as an example. NIST's [CMVP FAQ](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/faqs) says only FIPS 140-3 validations remain on the active list from September 22, 2026. Historical status is distinct from revocation. The [transition guidance](https://csrc.nist.gov/Projects/FIPS-140-3-Transition-Effort) discusses historical modules for existing systems; do not turn that into a blanket rule that every historical module is revoked or acceptable for every new system.

Check the actual certificate, module/version, operational environment and applicable security policy against the proposed deployment. Algorithm support, a vendor's “compliant” claim and a validated module are different evidence. A module validation also does not validate the whole application protocol or cloud tenant. The local workbook below makes no FIPS-validation claim.

The [ISC2 AI guidance](https://edge.sitecorecloud.io/internationf173-xmc4e73-prodbc0f-9660/media/Project/ISC2/Main/Media/exam-guidance/ISC2-Exam-Guidance.pdf), CCSP pages 12–14, extends the existing six domains to AI workloads: shared responsibility, protected training/model data, isolated compute, secured APIs/dependencies, monitored operations and accountable risk/legal review. Record provider versus customer duties for an AI service as explicitly as for storage or identity. An alert score or model drift is a signal to investigate, not proof of compromise.

## 2. Cloud Data Security — 20%

Map data from create/acquire through store, use/process, share, archive and destroy. Record owner/controller, custodian/processor, steward, classification, location/residency, format, flow, trust boundary, identity, key, retention/legal hold and evidence. Dispersion includes replicas, caches, logs, backups, snapshots, indexes, queues, analytics/features and support copies. A primary-record deletion does not prove lifecycle deletion.

Choose storage architecture by workload and obligation: object, block/volume, file, database, raw/data-lake, archival and ephemeral storage differ in access semantics, durability and lifecycle. Threats include public exposure, weak tenant/IAM policy, stolen keys/tokens, insecure snapshots, metadata leakage, remanence, replication/location mismatch, ransomware and unverified deletion. Apply least privilege, private paths, encryption, versioning/immutability where appropriate, backup, monitoring and lifecycle controls.

Use encryption in transit and at rest with explicit key ownership and trust boundaries. Document generation/import, HSM/KMS storage, separation of duties, access, use, backup/recovery, rotation, revocation, expiration and destruction. Hashes demonstrate integrity when used appropriately; signatures can support authenticity/non-repudiation under protected keys and identity/process evidence. Masking, anonymization and tokenization solve different exposure/linkability/use needs; validate re-identification risk. DLP detects or restricts defined sensitive movement but depends on classification and cannot understand every business context.

Discover structured, semi-structured and unstructured data across sanctioned and shadow services, including exact region/account/project/subscription, replicas and downstream copies. Classification policy defines categories, criteria, handling and owners; mapping records flows/relationships; labels/tags carry machine-usable handling context. Test inheritance, downgrade/relabel authority and drift.

Information Rights Management applies persistent usage conditions such as view/edit/copy/print/forward/offline/expiry, supported by identity, encryption and certificate/license provisioning/revocation. It complements—not replaces—source access, endpoint controls and contractual duties. Test offline, revoked-user and exported-content behavior.

Retention schedules reconcile legal, regulatory, contractual, business, privacy and technical constraints. Archive preserves accessibility/integrity for a defined period; deletion uses supported mechanisms and covers copies; legal hold suspends ordinary disposal for scoped material. Document crypto-erasure assumptions, provider media sanitization, backup expiry and proof. Never promise immediate physical overwrite where the service cannot provide it.

Define auditable data events and fields: actor/workload, action, object/classification, result, time/time source, IP/device/location, request/correlation ID and policy decision. Centralize tamper-resistant logs with access/retention/integrity controls. Preserve chain of custody and separate raw evidence from analysis. For AI/ML data and models, protect training/evaluation sets, features, prompts/context, embeddings, weights, endpoints and outputs; validate provenance, privacy, quality, access and tamper resistance.

**Related item:** Data sovereignty is a jurisdiction’s authority over data; residency is where data is stored/processed; localization is a requirement to keep it in a place. The terms affect architecture differently and must be confirmed with qualified legal/privacy stakeholders.

---

### Encryption, authorization and deletion have different evidence

Envelope encryption protects object data with a data-encryption key (DEK), then protects that key with a key-encryption key (KEK). The [AWS KMS hierarchy and ownership documentation](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) is one vendor example: customer-managed, AWS-managed and AWS-owned keys provide different lifecycle and audit control. Provider encryption does not automatically give the customer control of every key or evidence trail.

In AWS KMS symmetric encryption, [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) is authenticated, non-secret metadata; decryption needs the matching context. It can also participate in policy conditions and is logged in plaintext. Keep sensitive values out of it. Binding a tenant/object/version into authenticated data can detect substitution, but only a trusted authorization decision can decide which caller may request that context. Taking the tenant label from an untrusted request does not authenticate the tenant.

[KMS rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) changes key material while retaining the logical key and older decryption capability. It does not automatically rotate DEKs, re-encrypt object data or remedy a compromised DEK. Rewrapping a DEK under a different KEK is another distinct operation, demonstrated locally below; that example does not reproduce AWS KMS's wire format or rotation implementation.

For deletion, inventory replicas, exported ciphertext, plaintext, cached DEKs, old wrapping keys, backups and legal holds. [NIST sanitization guidance](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r2.pdf) distinguishes operation verification from deciding whether the outcome satisfies the sanitization need. Removing a key from an application dictionary cannot retract a copy already held elsewhere. Avoid promising that a successful decrypt-policy change proves cryptographic erase.

## 3. Cloud Platform and Infrastructure Security — 17%

Model facility, power/cooling, physical access, network/communications, compute, hypervisor/container substrate, storage and management plane. In public cloud, customers usually consume provider evidence for lower layers while retaining configuration and workload duties. In private cloud, the organization may own the full stack. Protect admin interfaces, automation identities and orchestration because management-plane compromise can bypass data-plane segmentation.

Secure data-center design includes logical tenant partitioning and access, physical location/build-or-buy, environmental HVAC/fire/water/power and diverse connectivity pathways. Resilience removes correlated single points: distinct failure domains, capacity, power, network, identity/DNS/key dependencies and tested procedures. Duplication without separation is not resilience.

Assess threats and vulnerabilities in business context: insecure APIs/configuration, exposed storage, weak IAM, credential theft, supply chain, shared-technology/isolation failure, availability attack, insider misuse, provider concentration, jurisdiction and limited visibility. Record inherent risk, existing controls/evidence, residual risk, owner, appetite/tolerance and treatment—avoid, mitigate, transfer/share or accept. Insurance/contract transfer does not transfer operational harm or accountability.

Plan layered controls across physical/environmental, system/storage/communications, identification/authentication/authorization and audit. Use federated MFA, workload identity, least privilege and time-bounded administration; private/segmented paths, filtering and encryption; hardened supported images; centralized logging/correlation and authorized packet capture. Validate allowed and denied behavior and ensure telemetry remains available during failure.

Build BC/DR from business requirements and dependency order. Define RTO, RPO and recovery service level; choose backup/restore, active-passive, active-active, regional or provider-diverse approaches according to risk and complexity. Test loss of region, control plane, identity, key service, network and operator access. Restore clean configuration, secrets and data; validate integrity/security/function, failback and lessons learned.

**Related item:** High availability reduces interruption for expected component failures; disaster recovery restores after severe disruption; business continuity maintains critical outcomes. One architecture may support all three, but each has different evidence and success criteria.

---

### A recovery region must include the dependencies

**PRACTICAL DEPTH:** A fictional service has cross-region object replicas but only one usable identity/key-service path. Replicating bytes does not prove recovery. List the required identity trust, network/DNS, key access, object versions, application configuration, quota/capacity and operator access. Exercise permitted recovery reads and prohibited administration as separate tests; preserve the service/data checkpoints and failure evidence.

For a 10:00 outage, a 09:40 recoverable checkpoint and validated service at 10:25, restoration takes 25 minutes and the data gap is 20 minutes. Against RTO 30 and RPO 15, only RTO is met. These are original scenario values, not measured cloud results. [NIST Zero Trust tenets](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) also prevent treating the recovery network's location as implicit authorization.

## 4. Cloud Application Security — 16%

Train architects, developers, testers, operators and product owners in cloud primitives, shared responsibility and common failures. Use current OWASP Top 10, API Security Top 10, ASVS, LLM Application Top 10 and relevant weakness lists as inputs—not substitute requirements. Teach how identity, metadata/service tokens, public endpoints, tenant context, secrets, dependencies and ephemeral/serverless behavior change attack paths.

The secure SDLC carries business/security/privacy/operability requirements through architecture, threat model, code, build, test, release, operate and retire. Agile and waterfall organize work differently but both need traceable acceptance criteria and accountable gates. Threat modeling identifies assets, actors/trust boundaries, flows, threats and mitigations; STRIDE, PASTA and other methods structure analysis, while risk determines priority. Review model and data flows for AI applications as first-class assets.

Apply secure coding: input/schema validation, output encoding, parameterized access, authorization on every object/action, secure session/token handling, SSRF/path/deserialization prevention, safe errors/logging and no embedded secrets. Govern repositories, branches, reviews, artifacts, configuration and versions. CI/CD should use isolated least-privilege identities, protected secrets, reproducible builds, signed/provenanced artifacts, approvals for material risk, immutable promotion and rollback.

Assurance combines functional and non-functional tests, unit/integration/system/acceptance, SAST, DAST, IAST, software-composition/secret/IaC/container scanning, black/gray/white-box perspectives, abuse cases, fuzzing where suitable and authorized penetration testing. Triage findings by exploit path and business impact; manage exceptions; retest fixes. QA asks whether the product satisfies requirements, while security testing specifically challenges misuse and control claims.

Secure APIs with strong identity/token validation, per-object/function authorization, schema/rate/size limits, replay protection where needed, TLS, gateway policy, safe errors and attributable logs. Govern commercial/open-source/third-party components through supplier assessment, license, inventory/SBOM, provenance/integrity, supported version, vulnerability response and replacement plan.

Use WAF, API gateway, database activity monitoring, load balancer and specialized filters for their actual layer. Sandboxing limits execution but is not absolute. Microservices, containers and Kubernetes add image/registry, orchestrator, service identity, secret, network policy, admission, runtime, resource and supply-chain boundaries. Federation/IdP/SSO/MFA, CASB and secrets/key/certificate systems need end-to-end trust and lifecycle validation.

**Related item:** SAST examines code without running it; DAST observes a running application externally; IAST combines runtime instrumentation; SCA evaluates components. No single technique proves secure business authorization or cloud configuration.

---

### Test the object decision across every layer

For an original multi-tenant invoice API, test an authenticated user requesting another tenant's object, a substituted object identifier, an earlier version, a replayed authorized request and a revoked entitlement. Bind the cryptographic context to the trusted object decision. A valid authentication tag establishes integrity under its key/context assumptions; it does not establish freshness, business authorization or that the data is the newest version.

The workbook uses AES-GCM from a maintained library with fresh 96-bit nonces and full tags. Its [API documentation](https://cryptography.io/en/50.0.1/hazmat/primitives/aead/) distinguishes encrypted payload from authenticated but unencrypted associated data and rejects altered ciphertext, keys, nonces or context. Production applications need a reviewed protocol, durable state, secure key custody and correct nonce management across processes; this small fixture is not a storage format to deploy.

Treat prompt/model output as untrusted input to tools. Enforce allowed actions and object authorization outside the model, validate tool arguments, restrict credentials, and record human escalation. Input validation and rate limits help, but do not prove that prompt injection or unauthorized tool use is impossible. Encrypting training data at rest does not, by itself, stop authorized inference from revealing sensitive information.

## 5. Cloud Security Operations — 17%

Build secure-by-default templates for HSM/TPM use, management-plane tooling, hypervisor/virtual hardware and guest operating systems. Separate host, guest, container and serverless responsibilities. Limit local/remote administration through federation/MFA, jump/bastion or approved console, secure terminal/SSH and time-bounded privilege; restrict and record emergency access.

Operate networks with reviewed VLAN/virtual-network/subnet/route/security-group/firewall policy, TLS, protected DNS/DHCP where applicable, VPN/private access, segmentation and inspection. Harden supported Windows/Linux/hypervisor images, continuously assess drift, patch by risk and test replacement/rollback. Monitor cluster and guest availability, compute/memory/storage/network latency/capacity, provider limits and application SLOs. Capacity evidence should distinguish demand, leak, attack, dependency latency and throttling.

Protect backup/restore of host, guest, configuration, identity/key and application data; test clean recovery. Orchestration and schedulers need least-privilege service identities, signed/versioned artifacts, controlled maintenance and logs. Do not allow automation to turn a mistaken change into fleet-wide failure.

Map NIST, ISO, CIS, COBIT, COSO, ITIL, ISO/IEC 20000-1 and sector requirements to the organization’s actual obligations rather than treating framework names as interchangeable. Operate change, continuity, information-security, continual-improvement, incident, problem, release, deployment, configuration, service-level, availability and capacity management as connected processes. An incident restores and contains now; problem management finds/removes systemic cause; change/release/deployment govern correction.

Support cloud forensics with pre-agreed authority, provider capabilities, logging, retention, clock context, snapshot/export methods, identity and chain of custody. Acquire and preserve evidence through approved procedures; cloud administrators may not have physical media or hypervisor access. Contracts and runbooks must address provider cooperation. Communicate facts, hypotheses, impact, actions and decisions to vendors, customers, partners, regulators and other stakeholders through approved need-to-know channels.

The SOC must monitor control health and security signals across identity, management/API, network, workload, data and application. Correlate SIEM/log/threat intelligence evidence; tune AI-assisted ranking and automation; define severity, owner and runbook. Perform authorized vulnerability assessment and penetration testing under provider policy and rules of engagement. Incident response prepares, detects/analyzes, contains, eradicates, recovers and learns while protecting evidence and legal/privacy needs.

**Related item:** A configuration baseline says what should be true; posture/drift monitoring asks whether it remains true; SIEM/SOC analysis asks what activity means; incident response acts when evidence and risk cross an authorized threshold.

---

### An operational decision should preserve its evidence

The [SP 800-61 Revision 3 executive summary](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf) connects incident work to all six CSF 2.0 Functions. Preparation and improvement span Govern, Identify and Protect; operational detection, response and recovery span Detect, Respond and Recover. Preserve the useful activities in the outline while checking current organizational procedures.

For a failed key-service call, correlate the caller, key identifier, request context, authorization outcome, service health and the object checkpoint. Do not log a plaintext key or sensitive context. Distinguish a denied request from service unavailability before changing policy. Test credential/key-service failure in recovery plans; a repeated retry or a clean dashboard is not proof of restored access or data completeness.

## 6. Legal, Risk and Compliance — 13%

Identify conflicting laws and the jurisdiction of customer, provider, subject, processing and storage with qualified counsel. Map regulated versus contractually protected data, applicable privacy rules and standards, purpose/legal basis, minimization, rights, transfer, retention and breach duties. Examples such as GDPR, HIPAA/HITECH, FERPA, PIPEDA and India’s DPDP Act are jurisdiction/context dependent; certification study is not legal advice. Perform privacy impact assessments before material high-risk processing.

Plan eDiscovery and forensics for identification, preservation/legal hold, collection, processing, review and production. Cloud elasticity, multi-tenancy, encryption, provider control, location and ephemeral resources complicate scope and chain of custody. Align applicable guidance/standards and contract for evidence availability, integrity, export format, timing and expert testimony support.

Audit assurance has boundaries. Define internal/external control objective, criteria, scope, period, population/sampling, evidence, exception and remediation. Read SOC/SSAE/ISAE and certifications for exact service, region, system boundary, customer complementary controls, subservice carve-outs, dates and opinion; a logo is not assurance for your workload. Use gap analysis, risk/control self-assessment, audit plans, ISMS, policies and stakeholder ownership. Distributed services can cross both organizational and legal boundaries.

Integrate provider risk into enterprise risk: evaluate control method/evidence, policies, risk profile, appetite, concentration/subprocessor/supply-chain, incident transparency and metrics. Distinguish data owner/controller, steward, custodian/processor responsibilities. Treat risks explicitly and retain accountable acceptance. Metrics should show exposure and control outcomes, not only ticket volume.

Translate business requirements into MSA, SOW, SLA and data-processing/security terms. Cover definitions, roles, data ownership/access/location/return/deletion, security/privacy controls, breach and regulatory cooperation, logging/eDiscovery/forensics, right to audit and assurance, subcontractors, availability/performance/support metrics, credits/remedies, cyber insurance, change, termination/transition, escrow/portability and dispute/litigation. Assess vendor lock-in, viability and the full ISO 27036-style supply chain.

**Related item:** Compliance demonstrates conformance to stated criteria at a point/period; assurance increases confidence in evidence; risk management decides what uncertainty and impact the organization will treat. Passing an audit does not prove that all material cloud risk is acceptable.

---

### Versioned control frameworks support evidence, not blanket assurance

The [CSA CCM overview](https://cloudsecurityalliance.org/research/cloud-controls-matrix) has a version 4.1 banner but still describes 197 controls. The [version 4.1 release page](https://cloudsecurityalliance.org/artifacts/cloud-controls-matrix-v4-1) specifies 207 controls across 17 domains and distinguishes the reference CAIQ from the form accepted for STAR Level 1 submission. Use the versioned release when labeling the framework. The public release description was reviewed; this review did not audit all control rows or submit a questionnaire.

CSA's [February 2026 transition guidance](https://cloudsecurityalliance.org/blog/2026/02/19/ccm-v4-1-transition-timeline) describes acceptance of both versions during transition, with version 4.1-only submissions in its December 2027 timetable and withdrawal of 4.0.x in January 2028. Older versions are not already withdrawn as of this review. Confirm the rules for a particular submission or assurance engagement rather than treating a framework release as automatic recertification.

Create an original evidence row with control requirement, shared responsibility, asset/service scope, implementation, test result, assessor/date, exception and expiry. A provider's questionnaire answer needs corroboration appropriate to the decision. Separate self-assessment, independent assurance and the customer's own configuration obligations. A service credit can remedy a contractual measurement without restoring lost data or meeting your recovery objective.

## Integrated scenarios

### Scenario 1: Regulated SaaS selection and exit

Two fictional providers offer similar storage encryption and audit logos, but only one demonstrates an export containing required data, access metadata and usable key arrangements. **Reasoning:** compare the exact assurance scope, customer responsibilities, locations, retention/hold behavior and exit dependencies. Test a synthetic export and restore; record remaining gaps with accountable risk treatment. A logo or contractual promise alone does not prove that the workload can exit.

### Scenario 2: Multi-tenant application and key exposure

A synthetic invoice service rotates its wrapping key after a DEK is copied. **Reasoning:** key-material rotation, rewrapping and encrypting data under a fresh DEK solve different problems. The copied DEK can still read ciphertext protected by it; old copies and disclosed plaintext are not recalled. Scope exposure, control access, replace affected material through the approved process and preserve incident evidence.

### Scenario 3: Provider-region incident and legal hold

A replicated object is available in another region, but the identity/key path is unavailable and a subset of records is under hold. **Reasoning:** invoke approved response/communications, preserve scoped evidence, restore dependencies and validate both RTO and RPO. Do not bypass the hold to simplify cleanup. Record who authorizes retention, access, failover and later disposal.

## Executed local envelope workbook

**PRACTICAL DEPTH — execution boundary:** This original example performs actual AES-GCM encryption, key wrapping, decryption and tamper rejection in memory. It combines those operations with explicitly trusted principal, grant and version fixtures. The policy fixtures do not authenticate users or reproduce a cloud IAM/KMS service. Only synthetic data and disposable keys are used; the workbook makes no file, network, cloud or account calls.

It was run with Python 3.13.14 and cryptography 50.0.1 in an existing environment; the review installed nothing. Save the block as `ccsp_envelope.py` in an approved disposable environment with the dependency available and run `python ccsp_envelope.py`. It is not a production encryption protocol or FIPS-validated deployment.

| Observation | Meaning and boundary |
|---|---|
| Wrong tenant/object/version context, altered bytes/nonces or substituted keys/ciphertext fail | Actual authentication-tag checks bind the controlled context and ciphertext |
| A rewrapped object retains the same data ciphertext | Changing a KEK wrapper is different from encrypting data with a fresh DEK |
| The application denies access after its grant is removed | A fixture policy decision governs calls through that wrapper only |
| A copied DEK still decrypts old ciphertext | Policy revocation and rewrapping cannot retract already copied key material |
| Authentic older ciphertext still decrypts | Encryption authenticity alone does not prevent rollback; the trusted version fixture supplies that decision |

```python
"""Original in-memory envelope-encryption and policy-boundary demonstration."""
import json
import os
from dataclasses import dataclass, replace
import cryptography
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

@dataclass(frozen=True)
class Context:
    tenant: str
    object_id: str
    version: int

@dataclass(frozen=True)
class Envelope:
    key_id: str
    wrap_nonce: bytes
    wrapped_key: bytes
    data_nonce: bytes
    ciphertext: bytes

def aad(context, purpose, key_id=None):
    # Context comes from the trusted request/manifest fixture, not a blob label.
    fields = {"schema": 1, "tenant": context.tenant, "object": context.object_id,
              "version": context.version, "purpose": purpose}
    if key_id is not None:
        fields["key_id"] = key_id
    return json.dumps(fields, sort_keys=True, separators=(",", ":")).encode("utf-8")

keys = {name: AESGCM.generate_key(bit_length=256) for name in ("old", "new")}
used_nonces = set()

def nonce():
    # Every encryption gets a fresh 96-bit value; this run rejects collisions.
    while True:
        value = os.urandom(12)
        if value not in used_nonces:
            used_nonces.add(value)
            return value

def seal(plaintext, context, key_id):
    data_key = AESGCM.generate_key(bit_length=256)
    dn, wn = nonce(), nonce()
    ciphertext = AESGCM(data_key).encrypt(dn, plaintext, aad(context, "data"))
    wrapped = AESGCM(keys[key_id]).encrypt(wn, data_key, aad(context, "key", key_id))
    # Returning the data key is deliberate for the captured-key demonstration.
    return Envelope(key_id, wn, wrapped, dn, ciphertext), data_key

def unwrap(envelope, context):
    return AESGCM(keys[envelope.key_id]).decrypt(
        envelope.wrap_nonce, envelope.wrapped_key,
        aad(context, "key", envelope.key_id))

def open_raw(envelope, context):
    return AESGCM(unwrap(envelope, context)).decrypt(
        envelope.data_nonce, envelope.ciphertext, aad(context, "data"))

def rewrap(envelope, context, new_id):
    data_key = unwrap(envelope, context)
    wn = nonce()
    wrapped = AESGCM(keys[new_id]).encrypt(wn, data_key, aad(context, "key", new_id))
    return replace(envelope, key_id=new_id, wrap_nonce=wn, wrapped_key=wrapped)

# These are trusted policy/version fixtures, not an identity or storage service.
grants = {("alice", "tenant-a", "object-7")}
latest = {("tenant-a", "object-7"): 1}

def read_current(principal, envelope, context):
    if (principal, context.tenant, context.object_id) not in grants:
        raise PermissionError("read not granted")
    if latest[(context.tenant, context.object_id)] != context.version:
        raise ValueError("version differs from trusted current manifest")
    return open_raw(envelope, context)

results = []

def check(name, condition):
    assert condition, name
    results.append({"case": name, "result": "passed"})

def reject(name, error_type, operation):
    try:
        operation()
    except error_type:
        results.append({"case": name, "result": error_type.__name__})
    else:
        raise AssertionError(name + " unexpectedly accepted")

def flip(value):
    return bytes([value[0] ^ 1]) + value[1:]

ctx = Context("tenant-a", "object-7", 1)
plaintext = b"synthetic invoice: 125 cents"
original, captured_data_key = seal(plaintext, ctx, "old")
other, _ = seal(b"other synthetic object", Context("tenant-b", "object-9", 1), "old")
captured_old_key = keys["old"]
check("authorized current read", read_current("alice", original, ctx) == plaintext)
reject("ungranted principal", PermissionError, lambda: read_current("bob", original, ctx))
for label, wrong in (("tenant", replace(ctx, tenant="tenant-b")),
                     ("object", replace(ctx, object_id="object-8")),
                     ("version", replace(ctx, version=2))):
    reject("wrong authenticated " + label, InvalidTag,
           lambda wrong=wrong: open_raw(original, wrong))
for field in ("ciphertext", "wrapped_key", "data_nonce", "wrap_nonce"):
    changed = replace(original, **{field: flip(getattr(original, field))})
    reject("tampered " + field, InvalidTag, lambda changed=changed: open_raw(changed, ctx))
reject("different wrapping key", InvalidTag,
       lambda: open_raw(replace(original, key_id="new"), ctx))
reject("cross-object wrapped-key substitution", InvalidTag,
       lambda: open_raw(replace(original, wrapped_key=other.wrapped_key,
                               wrap_nonce=other.wrap_nonce), ctx))
reject("cross-object ciphertext substitution", InvalidTag,
       lambda: open_raw(replace(original, ciphertext=other.ciphertext,
                               data_nonce=other.data_nonce), ctx))

rotated = rewrap(original, ctx, "new")
check("rewrapped object decrypts", read_current("alice", rotated, ctx) == plaintext)
check("rewrapping leaves data ciphertext intact",
      (rotated.data_nonce, rotated.ciphertext) == (original.data_nonce, original.ciphertext))
keys.pop("old")
reject("old wrapping key absent from fixture", KeyError, lambda: open_raw(original, ctx))
check("new wrapping key remains usable", read_current("alice", rotated, ctx) == plaintext)

stolen_dek = AESGCM(captured_old_key).decrypt(
    original.wrap_nonce, original.wrapped_key, aad(ctx, "key", "old"))
check("old key copy still opens archived envelope",
      AESGCM(stolen_dek).decrypt(original.data_nonce, original.ciphertext,
                                aad(ctx, "data")) == plaintext)
grants.clear()
reject("application revocation denies future wrapper call", PermissionError,
       lambda: read_current("alice", rotated, ctx))
check("captured data key bypasses wrapper revocation",
      AESGCM(captured_data_key).decrypt(rotated.data_nonce, rotated.ciphertext,
                                        aad(ctx, "data")) == plaintext)

ctx2 = replace(ctx, version=2)
replacement, _ = seal(plaintext, ctx2, "new")
check("fresh data key and version decrypt", open_raw(replacement, ctx2) == plaintext)
reject("old data key cannot decrypt new ciphertext", InvalidTag,
       lambda: AESGCM(captured_data_key).decrypt(replacement.data_nonce,
                                                replacement.ciphertext, aad(ctx2, "data")))
check("old authentic ciphertext is still decryptable", open_raw(rotated, ctx) == plaintext)
grants.add(("alice", "tenant-a", "object-7"))
latest[("tenant-a", "object-7")] = 2
reject("trusted manifest rejects rollback", ValueError,
       lambda: read_current("alice", rotated, ctx))
check("trusted manifest accepts current version", read_current("alice", replacement, ctx2) == plaintext)

print(json.dumps({"checks": results, "cryptography": cryptography.__version__,
                  "boundary": "Synthetic in-memory cryptography and trusted policy fixtures; no files or cloud calls"}))
print(str(len(results)) + " local envelope checks passed")
```

Expected final line: `24 local envelope checks passed`. The example deliberately returns and retains synthetic DEKs to demonstrate exposure. It does not zeroize Python memory, prove secure deletion, supply durable nonce/version coordination, authenticate principals, enforce a hardware boundary, protect a production multi-tenant process, or implement a cloud API. Its nonce collision tracking and state live only for this run. A production design must also address format parsing, replay, concurrency, crash recovery, key custody, side channels and independent review.

## Hands-on evidence labs

These eight infrastructure activities remain **proposed** and are separate from the executed local workbook. Use owned disposable resources, synthetic data, explicit scope, budget limits and cleanup evidence.

1. **Responsibility architecture:** Draw one SaaS, PaaS and IaaS data flow. Assign each control and its evidence to provider/customer/partner, including identity, DNS, key service and support dependencies. Pass when no critical control is left ownerless and the proposed recovery/exit path is testable.
2. **Data lifecycle:** Create a synthetic classified object and map replicas, cache, logs, export and backup. Test allowed and denied access, retention/hold decisions and supported deletion/expiry. Record which copies remain and why; do not claim physical sanitization from an API success.
3. **Provider assurance:** Inspect a legitimately public artifact and sample terms. Record service, region, period, criteria, customer controls, subservice exclusions and evidence gaps. Use a dated CCM version for mapping; compare the control claim with actual supporting evidence instead of copying a logo.
4. **Platform controls:** Build an approved isolated workload from a hardened template. Test permitted service traffic, denied management access, a harmless configuration drift and restoration. Verify logging survives the failure path; roll back and remove test resources.
5. **Secure delivery:** Threat-model a small synthetic invoice API. Test cross-tenant object requests, dependency provenance, secret handling, pipeline rejection and rollback. Include negative business-authorization cases alongside scanners; remove temporary identities, artifacts and credentials.
6. **Operations and SOC:** Correlate synthetic identity, control-plane, workload and data events. Add a duplicate record and collector gap; distinguish event count from incident count. Exercise one approved containment decision and preserve timestamps, identifiers, authority and rationale.
7. **Resilience and forensics:** Simulate loss of a required identity/key dependency. Restore usable application/data state, measure RTO and RPO separately, and retain hashed synthetic evidence with a custody record. Explain which provider cooperation would be required in a real event.
8. **Cloud security decision pack:** Link requirements, responsibility, risk, control test, assurance scope, contract, incident and exit records. Have a reviewer trace one claim end-to-end, list exceptions/expiry, and verify cleanup and residual cost before closing the activity.

## Readiness checks

These are original teaching prompts, not recalled or predicted exam items. Cover the answer, explain a decision and identify evidence before checking the response.

1. **Can you distinguish cloud roles, characteristics and building blocks?** Name customer, provider, partner, broker and regulator, then trace compute, storage, network, databases and orchestration against on-demand access, pooling, elasticity and measured service.
2. **How do SaaS, PaaS and IaaS shift control and evidence?** The provider operates progressively more of the stack from IaaS through PaaS to SaaS; customer identity, data, configuration and evidence obligations still need explicit assignment.
3. **How do deployment models alter—not erase—shared responsibility?** Public, private, hybrid, community and multi-cloud change ownership and dependencies. They do not remove accountability or the need to inspect the actual service contract.
4. **Can you explain portability, interoperability and reversibility separately?** Portability concerns moving workloads/data; interoperability concerns working together; reversibility includes a tested exit and an acceptable restored operating state.
5. **What belongs in secure cloud design and the data lifecycle?** Start with business/data obligations and trust boundaries, then design identities, isolated paths, approved cryptography, controlled change, monitoring, recovery and retirement.
6. **How do BIA, RTO, RPO, CBA and ROI inform architecture?** BIA establishes impact and priorities; RTO bounds restoration time and RPO the data-loss window. Cost/return estimates inform choices but cannot silently waive mandatory requirements.
7. **What does a provider product certification actually prove?** Only the stated module/product version, environment and criteria are covered. Inspect the current validation entry; an entire cloud application is not validated because one component is.
8. **What controls and evidence make AI/ML use governable?** Define purpose, data/model provenance, access, permitted tools, quality/drift monitoring, accountable decisions and human escalation. A model output does not transfer responsibility.
9. **Can you find every dispersed copy of a cloud data object?** Inventory replicas, snapshots, backups, caches, logs, exports, indexes and derived/model data. A primary-row deletion alone cannot demonstrate all-copy deletion.
10. **How do storage types and their threats differ?** Object, volume, file/database, archive and ephemeral storage differ in access and lifecycle. Evaluate exposure, identity, remanence, copies, location and recovery requirements for the actual service.
11. **What is the full encryption/key/secrets/certificate lifecycle?** Record generation, custody, authorized use, distribution, rotation, backup/recovery, revocation and destruction, including every retained key or plaintext copy relevant to the claim.
12. **When do masking, anonymization and tokenization fit?** Masking limits visible detail; tokenization substitutes a managed reference; anonymization attempts to prevent identification. Evaluate reversibility and re-identification in the actual data context.
13. **How do discovery, classification, mapping, labels and tags connect?** Discovery finds data and location; classification assigns handling rules; mapping traces flows; labels/tags carry those rules. Test who can relabel and how downstream copies inherit them.
14. **What does IRM control, including revocation and offline use?** IRM can constrain supported usage through identity and licensing, but offline licenses, exports and captured plaintext limit revocation. Test the actual client and policy behavior.
15. **How do retention, archive, legal hold and deletion differ?** Retention sets how long to keep data; archiving preserves it for later access; a scoped hold suspends disposal; deletion uses approved mechanisms and evidence across copies.
16. **Which event fields support attribution and chain of custody?** Capture actor, action, object, result, time, request/policy context and source. Protect raw records and document acquisition and transfers; a hash alone is not a custody history.
17. **How do you protect AI datasets, models, context and outputs?** Apply classification, provenance, access, integrity and retention to datasets, features, prompts/context, weights, endpoints and outputs, with tests for sensitive disclosure and unauthorized tool actions.
18. **Can you map facility through management plane and workload?** List facility, hardware, network, storage, virtualization, management plane and workload dependencies, assigning customer versus provider implementation and evidence duties.
19. **What makes physical/logical/environmental design resilient?** Separate failure domains and preserve power, cooling, connectivity, identity, keys, capacity and operator access. Duplicate components with the same dependency may fail together.
20. **Who owns cloud risk acceptance and what evidence supports it?** An authorized risk owner accepts residual risk against policy; record likelihood/impact assumptions, control evidence, treatment, exception expiry and review.
21. **What controls protect management and data planes?** Restrict privileged identities and automation, segment administration and data traffic, protect secrets, log decisions and verify both permitted work and denied access.
22. **How do HA, DR and BC differ and how are they tested?** HA handles expected component failures, DR restores after severe disruption, and BC maintains critical outcomes. Test each against its own scope and acceptance criteria.
23. **What training changes cloud developer behavior?** Use role-specific secure development tasks, relevant misuse cases and demonstrated behavior; course attendance does not prove secure coding or release decisions.
24. **Can you trace requirements through every secure-SDLC phase?** Track requirements through design/threat model, implementation, build/test, release, operation and retirement, with accountable acceptance and change evidence.
25. **How do threat-model methods structure—not decide—risk?** A method organizes assets, boundaries, threats and mitigations. Business impact, likelihood, obligations and authorized ownership determine risk treatment.
26. **How do SAST, DAST, IAST, SCA and abuse testing differ?** SAST inspects code, DAST probes running behavior, IAST adds runtime instrumentation, and SCA examines components; abuse tests challenge misuse and business-control assumptions.
27. **What makes an API and its authorization observable and safe?** Validate identity and per-object/action authorization, schemas and limits, protected transport, safe errors and attributable results. A gateway or valid token is insufficient by itself.
28. **What proves a dependency/artifact is authentic and supported?** Check trusted origin/signature/provenance, exact version, licensing, support and vulnerability response. Integrity confirms bytes under assumptions, not that the component is safe.
29. **How do WAF, API gateway, DAM and load balancer roles differ?** WAF inspects selected application traffic, an API gateway governs API entry, DAM monitors database activity, and a load balancer distributes traffic. Each has a specific visibility and enforcement boundary.
30. **What IAM trust and credential lifecycles span the application?** Inspect IdP trust, issuer/audience/session behavior, entitlement mapping, workload credentials, rotation/revocation and downstream access, including failure and emergency paths.
31. **What belongs in secure host/guest/container/serverless operation?** Use supported baselines, least-privilege administration, protected configuration/secrets, patch/drift monitoring, telemetry and recovery; assign substrate versus workload duties explicitly.
32. **How do you patch, measure capacity and prove clean restore?** Prioritize patches by exposure/impact, use tested deployment and rollback, correlate capacity with workload/dependencies, and validate restored service, data and security separately.
33. **How do incident, problem, change, release and deployment connect?** Incident handling contains/restores now; problem management addresses underlying causes; change authorizes modifications, release packages them, and deployment implements them with validation.
34. **What cloud evidence must be contracted before an incident?** Agree authority, available logs, export format, preservation/retention, identity/time context, provider cooperation and response timing before evidence becomes ephemeral or inaccessible.
35. **How do SOC monitoring, assessment and penetration testing differ?** Monitoring interprets ongoing signals; assessment identifies/control-tests weaknesses; penetration testing validates scoped attack paths. Each requires authority and clear limits.
36. **How can jurisdiction and privacy change a technical design?** Location, processing, subjects, contracts and governing obligations can constrain architecture. Obtain qualified privacy/legal interpretation for the actual case rather than inferring compliance from a region name.
37. **What limits the assurance in a cloud audit report?** The service/system boundary, criteria, period, opinion, sampling, exceptions, customer controls and subservices limit the claim. Match them to the proposed workload.
38. **How do enterprise, provider and supply-chain risks connect?** Provider and subprocessor dependencies contribute to enterprise exposure and concentration risk. Assign treatment and evidence through the chain; a contract transfer does not remove operational harm.
39. **Which MSA/SOW/SLA/exit terms make controls enforceable?** Define scope, measurement, data rights/location/return/deletion, incident/evidence cooperation, assurance, remedies and termination/transition. Test whether the promised exit is technically usable.
40. **Have you reconciled every resource with the August 2026 outline?** Map every current numbered objective, including 1.6/2.9, to teaching and evidence. Older course dates and broad cloud-security titles are not proof of August 2026 completeness.
41. **Does AWS KMS rotation automatically replace every DEK?** No. Current KMS documentation separates key-material rotation from DEK rotation and data re-encryption; compromised DEKs require their own response.
42. **Why is encryption context unsuitable for secrets?** It is authenticated but unencrypted metadata and, in AWS KMS, appears in audit logs. Use non-sensitive values and derive authorization context from trusted decisions.
43. **What did the copied-key checks demonstrate?** A copied DEK can still decrypt ciphertext protected by it after wrapper revocation or rewrapping. A copied old KEK can also open a retained old envelope.
44. **Does a valid authentication tag establish the newest version?** No. Authentic old ciphertext may still verify. The example’s independent trusted version fixture rejects rollback; it is not a durable production manifest.
45. **What changed in FIPS validation status in September 2026?** NIST’s FAQ places only FIPS 140-3 validations on the active list from September 22. Historical status differs from revocation; inspect the module and applicable deployment requirements.
46. **Which current CCM control count should be labeled version 4.1?** The versioned release specifies 207 controls across 17 domains; the overview’s 197 count is inconsistent. Do not claim a full control implementation from a catalog review.
47. **Does a 75% adaptive-course score establish CCSP certification?** No. Course completion, the CAT exam’s scaled 700/1000 passing score, and experience/application requirements are separate.
48. **What remains unproven by the local workbook?** Cloud IAM/KMS behavior, authenticated principals, durable/concurrent nonce/version state, secure deletion, hardware custody, infrastructure recovery and production readiness remain untested.

## Places to learn

This is not a complete list. Select a route and map it against the current outline before adding references or practical work. Public catalog observations were checked September 29, 2026; no paid lessons, book interiors or question banks were accessed. Planning estimates are this guide's suggestions, not verified provider runtimes.

| Resource | Access | Estimated time |
|---|---|---|
| [Current CCSP outline](https://www.isc2.org/certifications/ccsp/ccsp-certification-exam-outline) — canonical 38-objective August 2026 scope | Public | Planning: 5–8h mapping and review |
| [ISC2 self-study resources](https://www.isc2.org/certifications/ccsp/ccsp-self-study-resources) — official outline, training and study-aid hub | Public hub; linked account/paid resources | Planning: 1–2h selection; study varies |
| [Official adaptive CCSP training](https://www.isc2.org/training/online-self-paced/ccsp-online-self-paced) — six public domain descriptions; included textbook/questions are catalog claims only | Paid/account; English; 90/180-day access starts at purchase | No fixed runtime verified; previous 20–40h “official range” not reverified |
| [LinkedIn Learning/Cybrary CCSP Cert Prep](https://www.linkedin.com/learning/isc2-certified-cloud-security-professional-ccsp-cert-prep) — July 3, 2025 listing, six domains/six quizzes; close current objective gaps | Paid/trial; public contents reviewed | Header 10h02m; 94 listed clips total 10h02m39s; planning: add 30–50h practical work |
| [Pluralsight Cloud Security path](https://www.pluralsight.com/paths/cloud-security) — five 2025 course cards on architecture, detection, authorized testing, APIs and compliance; generic supplement, not CCSP-specific | Paid/trial; public catalog reviewed | Header 5h; cards total 4h54m; planning: add 25–40h practical work |
| [O'Reilly/Sybex CCSP study guide, 3rd edition](https://www.oreilly.com/library/view/isc-2-ccsp-certified/9781119909378/) — current public access blocked; earlier edition/date/alignment claims unverified here | Paid/trial or book; HTTP 403 | Earlier 11h47m not reverified |
| [Udemy/Dion CCSP Full Course](https://www.udemy.com/course/isc2-ccsp-full-course-practice-exam/) — public access blocked; earlier August 2026 revision/current-alignment claim unverified | Paid; HTTP 403 | Earlier 19h59m not reverified |
| [CSA Cloud Controls Matrix](https://cloudsecurityalliance.org/research/cloud-controls-matrix) — control/responsibility context; use the versioned 4.1 release to resolve overview metadata | Public overview; download routes have separate access/licensing terms | Planning: 4–8h selective mapping; full control rows not reviewed here |
| [ISC2 member policies](https://www.isc2.org/policies-procedures/member-policies) — applicable CCSP/Associate CPE and AMF categories | Public | Planning: 45–90m |
| [ISC2 Code of Ethics](https://www.isc2.org/ethics) — authority, competence, assurance, disclosure and public trust | Public | Planning: 30–60m plus scenarios |

**VERIFY CURRENT:** Adaptive-course completion requires at least 75% on domain and final assessments plus its acknowledgement/evaluation requirements. This is separate from the certification exam and experience. Training access, exam entitlements and any extension/guarantee have their own conditions; no purchase, account eligibility or course quality was assessed here.

Avoid recalled questions, “actual exam” banks and guaranteed passing. Use original reasoning practice and current primary evidence. The [dated deep-review report](../docs/research/2026-09-29-ccsp-deep-review.md) records source limitations, executed checks and pending human/infrastructure review.
