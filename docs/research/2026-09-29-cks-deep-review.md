# CKS deep review — September 29, 2026

Same-context AI review; independent human review pending. [Study guide](../../guides/CKS-certified-kubernetes-security-specialist.md).

## Scope and conflicting artifacts

Read the full [Linux Foundation CKS scope](https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/): 26 competencies, groups 5/4/4/4/4/5, weighted 15/15/10/20/20/20. The [CNCF overview](https://www.cncf.io/training/certification/cks/) still has older 10/15/15 first-three weights. However, the actual [v1.34-named PDF](https://raw.githubusercontent.com/cncf/curriculum/master/CKS_Curriculum%20v1.34.pdf), fully read at three pages and 170,239 bytes, matches the current competencies and weights apart from minor wording/case differences. Repository contents still list only that CKS filename. The guide now distinguishes filename age from actual outline content; the live LF page governs.

Both monitor hashes remain unchanged and no accepted baseline was rewritten. The canonical exam remains v1.35, two hours, with two-year validity, 12-month eligibility, one retake and two 36-hour simulator activations. Its current simulator listing is **17 questions**, replacing the guide's older 20–25 figure; this is not a real-exam question count. Prior CKA passage is required; CNCF expressly says it need not remain active. The approximate v1.37 alignment watch remains, with no announced exam switch date, so unsupported scheduled metadata becomes none-announced.

## Teaching and actual execution

Two exact public Python examples passed **29 checks**: **17 actual OpenSSL 3.5.7 signature/claim checks** and **12 restricted audit-policy model checks**. Both examples are hash-matched. Synthetic EC P-256 keys signed a custom teaching statement; valid inputs passed and wrong keys, changed bytes, mismatched artifact digest, wrong release/repository/builder/schema and malformed/incomplete claims were rejected. A valid signature alone did not establish deployment approval. Temporary keys and payloads were removed; the verification key is an explicit local trust assumption.

This is not an OCI image, SBOM, standard provenance/attestation implementation, keyless identity proof, transparency check, image scan or admission controller. No registry or real credentials were used. The audit model covers exact group/resource/namespace/verb selection and stage omission only, rejects unsupported selectors, and demonstrates first-match ordering and omitted-stage behavior. It generated no API audit record and tested no log backend.

Expanded PSA workload-template versus Pod enforcement, exemptions/versioned standards, requested versus effective seccomp/AppArmor, RBAC named-access/delegation boundaries, explicit webhook rejection versus call failure, at-rest writes versus migration/key retention, and effective Secret/runtime permissions. Added Istio authentication/authorization separation, Cilium encryption coverage and Falco severity/event-quality distinctions. There are 46 answered checks and stronger success/failure evidence for eight proposed cluster labs.

All eight full labs remain **proposed**. The earlier same-session Docker Linux-engine probe failed and native Linux execution remains deferred; no services were started/restarted. No CIS, cluster/kernel/admission, storage encryption, mesh, network policy, runtime sensor, audit backend or incident containment operation was performed. Current product documentation is qualified by installed version and mode.

## Public learning and release evidence

[LFS260](https://training.linuxfoundation.org/training/kubernetes-security-essentials-lfs260/) lists 26–30 hours and nine chapters, with self-managed Linux plus cloud/VirtualBox labs and possible charges. [Pluralsight](https://www.pluralsight.com/paths/certified-kubernetes-security-specialist-cks) retains seven courses, three labs and 12 hours: a 2022 introduction, 2025 courses, 2026 cluster courses and July/August/September 2026 labs. [KodeKloud](https://kodekloud.com/courses/certified-kubernetes-security-specialist-cks/) lists 8.75 video hours, eight modules and 150 lessons; its public history still says v1.33 in progress in May 2025. Optional Pod Security Policies remain visible and no SBOM/signature lesson titles appear in the public outline. These are metadata gaps, not findings about paid contents or current lab runtime. O'Reilly and Udemy were blocked; inherited durations/dates are expressly unverified. Added study times are planning estimates and Places to learn remains last.

The previously read ingress-nginx retirement notice remains controller-specific and does not remove the Ingress API/TLS objective. The v1.37 release article remains a date-only watch, without importing its features into the exam baseline.

## Validation

The operational receipt records repository tests, repository validation, strict site generation, generated-site checks, catalog consistency and diff checks after execution. Source freshness is current under the explicit canonical-source precedence; the program outcome remains **reviewed with blockers** because native cluster behavior needs live validation.
