# WP-005 — Development Reasoning Policy

**Status:** active  
**Owner role:** designer/builder  
**Decision authority:** architecture proposal under ADR-0001; human owner has approved the direction, but independent review/verification remains required before Phase 0 acceptance  
**Branch:** `phase0/development-os`  
**Parent:** `WP-000-DEVELOPMENT-OS.md`

## Objective

Add one canonical repository-based reasoning policy for SOUL development sessions, synthesize it from prior KEEL/KEEL-Work/OS-Architect/KEEL-Research lessons, and load it through the existing single `COLD_START.md` sequence without creating a second bootstrap authority.

## Owner direction

On 2026-08-26 the human owner approved this direction after review of the source synthesis and the explicit objection against copying prior instructions wholesale or placing a second reading order in ChatGPT Project Instructions.

Owner approval authorises the work; it does not replace independent verification or adversarial review of the resulting architecture.

## Scope

- `development/01_governance/REASONING_POLICY.md`;
- source/evidence synthesis record;
- architecture decision ADR-0001;
- integration into `COLD_START.md` as shared governance for every role;
- explicit WP-000 strengthening so the new policy is part of Phase 0 acceptance rather than an unverified side artefact;
- minimal ChatGPT Project entry instruction that points to repository cold-start rather than duplicating the policy;
- state/index/handoff updates needed to cut a fresh exact verification target.

## Non-scope

- implementing the final reusable SOUL runtime reasoning architecture;
- exposing or persisting private chain-of-thought;
- importing predecessor repo prompts wholesale;
- creating a second cold-start order in Project Instructions;
- replacing independent verification with self-checks;
- redesigning Phase 1 capability architecture;
- accepting ADR-0001, ADR-0000 or Phase 0 inside the builder session.

## Required reading

Enter through `development/03_plan/COLD_START.md`. After current bootstrap rules are loaded, inspect:

1. `development/05_evidence/REASONING-POLICY-SYNTHESIS-2026-08-26.md`
2. `development/01_governance/DECISION_POLICY.md`
3. `development/01_governance/CHANGE_POLICY.md`
4. `development/01_governance/VERIFICATION_POLICY.md`
5. `development/04_work/WP-000-DEVELOPMENT-OS.md`
6. `development/03_plan/COLD_START.md`
7. ADR-0001

## Outputs

- `development/01_governance/REASONING_POLICY.md`
- `development/05_evidence/REASONING-POLICY-SYNTHESIS-2026-08-26.md`
- `development/02_architecture/decisions/ADR-0001-DEVELOPMENT-REASONING-POLICY.md`
- updated `development/03_plan/COLD_START.md`
- updated `development/04_work/WP-000-DEVELOPMENT-OS.md`
- a minimal Project-entry instruction artefact that can be copied into ChatGPT Project Instructions without reproducing governance content
- updated state/index/session handoff

## Acceptance criteria

1. Every fresh development role loads `REASONING_POLICY.md` through the single authoritative `COLD_START.md` sequence before substantive work.
2. No Project instruction, WP, launch view or policy creates a second bootstrap order that competes with `COLD_START.md`.
3. The policy distinguishes observed/inferred/assumed/verified claims and prevents tool success, retrieval, model agreement or fluent prose from becoming proof by default.
4. The policy separates objective, method, current state and evidence, and does not allow the reasoning policy itself to widen active-WP authority.
5. Material decisions include triggered premise/framing inspection, necessity testing, credible alternatives/layer comparison, falsification, evidence/uncertainty and authority checks.
6. Reasoning depth is risk-proportional; routine reversible actions are not forced through a full first-principles ritual.
7. Failure analysis requires both immediate cause and why the system/process failed to anticipate, prevent or detect it, with a regression path.
8. Research/analytical claims preserve source quality and claim → computation/method → inputs/data → source/version provenance when relevant.
9. Producer completion remains separate from independent verification; exact-target freshness and adversarial/human gates are preserved.
10. The policy explicitly does not require disclosure or storage of private chain-of-thought and records only decision-relevant rationale/evidence.
11. Technical decisions are not unnecessarily transferred to the human owner; owner authority remains vision/value/scope and declared high-impact choices.
12. WP-000 is transparently strengthened to include the reasoning policy in Phase 0 acceptance; no prior FAIL is edited or weakened to obtain a PASS.
13. The source synthesis distinguishes source-observed rules from SOUL-specific design choices and does not treat duplicate predecessor files as independent evidence.
14. ADR-0001 remains proposed until required independent review/verification is complete.
15. F2-R1 repair remains independently visible as WP-004 rather than being hidden inside this change.

## Required verification

A fresh verifier must inspect the final exact PR #1 target after WP-005 closes. It must:

- re-run all WP-000 acceptance criteria including the new reasoning-policy criterion;
- regression-test F2-R1 on the same exact target;
- verify COLD_START sequencing and no second instruction authority;
- verify the policy's scope and chain-of-thought boundary;
- treat the builder's synthesis/rationale as claims, not proof;
- preserve ADR/adversarial/owner gates.

A separate adversarial review must attempt to show that the new policy creates ritualised overthinking, duplicate authority, hidden owner-decision transfer, prompt-only false assurance, or excessive cold-start burden.

## Risks

- prompt/governance bloat;
- checklist ceremony without behavioural value;
- false confidence from self-reported policy compliance;
- overfitting SOUL to predecessor failure models;
- turning Project Instructions into an unversioned second authority;
- increasing session startup cost enough to harm practical use.

## Completion state

Current: **active — material architecture change in progress**.

The builder may leave it materially complete / awaiting fresh verification. It cannot accept ADR-0001 or Phase 0.
