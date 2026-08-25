# PROCESS DEFECT PD-001 — Missing verifier-result → canonical-state transition

**Status:** open  
**Date recorded:** 2026-08-25  
**Recorded by:** Phase 0 integrator session  
**Repair owner:** WP-002 builder

## Defect

The Phase 0 operating system specifies what responsibility follows a verifier PASS, FAIL, or NOT VERIFIED result, but it does not explicitly define the control-plane transition that turns a completed verifier result into canonical repository state.

In particular, there is no single explicit procedure that assigns an actor and sequence for:

- integrating a verification-only branch/PR into the Phase 0 development line when the target result is FAIL or NOT VERIFIED,
- distinguishing integration of verifier evidence from acceptance of the failed target,
- changing the completed verification WP status,
- updating `development/03_plan/STATE.md` from "verifier required" to the result-dependent next state,
- creating/activating the required repair WP after FAIL / NOT VERIFIED,
- preserving exact-target verification freshness after subsequent repair changes,
- routing a future PASS to adversarial review rather than directly to Phase 0 acceptance.

## Evidence

- `development/04_work/WP-001-PHASE0-VERIFICATION.md` defines the outcome handoff (`PASS → adversarial review`; `FAIL / NOT VERIFIED → builder repair`) but does not define who performs the canonical state transition or how verifier records are integrated.
- `development/01_governance/WORKING_PROTOCOL.md` requires repository state and a handoff to be updated when project state changes, but provides only a generic session-close rule rather than a verifier-result transition.
- `development/03_plan/PR_GATE.md` requires material findings to be repaired/re-verified before a material PR is accepted and requires post-merge state truth, but does not explicitly distinguish a verification-record PR whose legitimate purpose is to record a FAIL from the failed target PR itself.
- `development/03_plan/COLD_START.md` tells an integrator to read `PR_GATE.md` and relevant verification/review artefacts, but contains no result-integration/state-transition procedure.
- After WP-001 verification completed in PR #2 with an overall FAIL, canonical `STATE.md` still said a fresh verifier was required until this integrator session performed an owner-requested transition.

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

## Integration note

This integrator session is recording and performing the currently missing transition under the human owner's explicit instruction so that repository state can continue. That one-time action is **not** evidence that an explicit reusable mechanism already exists and must not be treated as the permanent process design.
