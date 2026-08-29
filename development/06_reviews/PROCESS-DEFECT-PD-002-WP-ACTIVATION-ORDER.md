# PROCESS DEFECT — PD-002 — Work-package activation order

**Status:** observed during Phase 0 bootstrap; corrected in canonical state; fresh verification required  
**Date:** 2026-08-26

## Observed failure

After WP-004's bounded F2-R1 repair was materially completed, the builder created material WP-005 reasoning-policy artefacts before first transitioning canonical `development/03_plan/STATE.md` from active WP-004 to active WP-005.

The owner-directed reasoning-policy change had already been explicitly queued in `STATE.md`, and `WP-005-DEVELOPMENT-REASONING-POLICY.md` was created before its implementation artefacts. However, the canonical active-WP pointer still named WP-004 while WP-005 material work began.

## Why this matters

`STATE.md` + the active WP are the authoritative current-work home. A material session should not rely on an intended/queued next WP while canonical state still names the previous responsibility. Doing so weakens the exact discipline Phase 0 is intended to establish.

## Immediate cause

The session treated completion of WP-004 plus the already-recorded owner direction as sufficient to begin the next builder responsibility, but did not execute the explicit canonical state transition before the first WP-005 material write.

## System cause

The result-transition path is explicit after verification, but ordinary owner-directed WP-to-WP activation is currently procedural rather than mechanically gated. The builder focused on creating the new bounded WP and outputs and failed to sequence the state transition first.

This is not evidence that a new permanent mechanism is automatically required; one observed bootstrap failure is insufficient to justify additional machinery without verification/adversarial assessment. It is evidence that the current process must be tested for activation-order clarity.

## Correction

- Canonical `STATE.md` is transitioned to WP-005 before further WP-005 material work continues.
- The defect remains recorded rather than erased by the correction.
- The fresh verifier must inspect whether current governance unambiguously requires active-WP state before substantive work and whether the final repository has a single coherent active responsibility.
- If the same class repeats, `CHANGE_POLICY.md` should be used to determine whether a stronger activation gate is justified.

## What this defect does not mean

- It does not invalidate the owner's approval of the reasoning-policy direction.
- It does not independently prove the WP-005 artefacts are semantically wrong.
- It does mean the builder cannot present the development process as defect-free or use its own correction as independent verification.
