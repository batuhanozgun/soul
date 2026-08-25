# PROCESS DEFECT PD-001 — Missing verifier-result → canonical-state transition

**Status:** repair implemented — pending independent verification  
**Date recorded:** 2026-08-25  
**Recorded by:** Phase 0 integrator session  
**Repair owner:** WP-002 builder

## Defect

The Phase 0 operating system specified what responsibility follows a verifier PASS, FAIL, or NOT VERIFIED result, but did not explicitly define the control-plane transition that turns a completed verifier result into canonical repository state.

In particular, there was no single explicit procedure that assigned an actor and sequence for:

- integrating a verification-only branch/PR into the Phase 0 development line when the target result is FAIL or NOT VERIFIED,
- distinguishing integration of verifier evidence from acceptance of the failed target,
- changing the completed verification WP status,
- updating `development/03_plan/STATE.md` from "verifier required" to the result-dependent next state,
- creating/activating the required repair WP after FAIL / NOT VERIFIED,
- preserving exact-target verification freshness after subsequent repair changes,
- routing a future PASS to adversarial review rather than directly to Phase 0 acceptance.

## Evidence

- `development/04_work/WP-001-PHASE0-VERIFICATION.md` defined the outcome handoff (`PASS → adversarial review`; `FAIL / NOT VERIFIED → builder repair`) but did not define who performs the canonical state transition or how verifier records are integrated.
- The pre-repair `development/01_governance/WORKING_PROTOCOL.md` required repository state and a handoff to be updated when project state changes, but provided only a generic session-close rule rather than a verifier-result transition.
- The pre-repair `development/03_plan/PR_GATE.md` required material findings to be repaired/re-verified before a material PR is accepted and required post-merge state truth, but did not explicitly distinguish a verification-record PR whose legitimate purpose is to record a FAIL from the failed target PR itself.
- The pre-repair `development/03_plan/COLD_START.md` told an integrator to read `PR_GATE.md` and relevant verification/review artefacts, but contained no result-integration/state-transition procedure.
- After WP-001 verification completed in PR #2 with an overall FAIL, canonical `STATE.md` still said a fresh verifier was required until SESSION-0004 performed an owner-requested transition.

## Why this is separate from verifier findings F1 and F2

- **F1** concerns mutually incompatible mandatory cold-start/read-order procedures.
- **F2** concerns a stale duplicated current-work pointer in `NEXT_SESSION.md`.
- **PD-001** concerns the missing state-machine/control-plane mechanism between a completed verifier outcome and canonical project state.

Repairing F1 and F2 alone would not define this transition for future verification cycles.

## Required repair property

WP-002 must define an explicit verifier-result → canonical-state mechanism that, at minimum, specifies:

1. the authorised role responsible for the transition;
2. the triggering evidence and exact-target freshness checks;
3. how verification records are integrated without treating a FAIL / NOT VERIFIED result as acceptance of the target;
4. how the completed verification WP and canonical `STATE.md` are updated;
5. how PASS, FAIL, and NOT VERIFIED route to their distinct next responsibilities;
6. how a repair WP is created/activated when required;
7. how material repair invalidates the previous verification for the changed target;
8. how the mechanism preserves role separation, acceptance criteria, owner gates, and no-false-completion controls.

The repair builder may choose the appropriate authoritative document structure, but must not solve the gap by adding another independent duplicate of current state.

## Implemented repair

WP-002 implements the missing mechanism through existing governance surfaces rather than adding a new state store:

- `development/01_governance/VERIFICATION_POLICY.md` now defines the authorised **Integrator** transition, trigger/preconditions, evidence-only integration sequence, PASS / FAIL / NOT VERIFIED routing, exact-target freshness/staleness rules, and no-false-completion controls.
- `development/01_governance/ROLE_MODEL.md` now makes that Integrator authority and its prohibitions explicit while preserving verifier/builder separation.
- `development/01_governance/WORKING_PROTOCOL.md` now makes verifier close distinct from canonical result integration and delegates the transition to `VERIFICATION_POLICY.md`.
- `development/03_plan/PR_GATE.md` now distinguishes a verification/review evidence PR from the material target PR and states that merging failed verification evidence is not acceptance of the target.
- proposed `development/02_architecture/decisions/ADR-0000-DEVELOPMENT-GOVERNANCE-BOOTSTRAP.md` records the governance design change without changing its proposed status or bypassing the human-owner decision gate.

The mechanism explicitly treats any later substantive repair/design/acceptance/authority/verification-rule change as material and therefore stale for the prior exact-target verification. Result integration itself does not retarget or rewrite the verifier's historical result.

## Verification status

This file records a **builder repair claim, not proof**. PD-001 remains pending until a fresh verifier independently tests the mechanism against WP-002 and the unchanged WP-000 acceptance criteria.

The historical SESSION-0004 one-time transition remains evidence of the defect; it is not retroactively treated as proof that the reusable mechanism existed before this repair.
