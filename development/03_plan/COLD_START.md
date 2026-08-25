# COLD START

This is the standard and authoritative sequencing procedure for a fresh SOUL development session.

`SOURCE_OF_TRUTH.md` defines which artefact wins when project claims conflict. This file separately defines **the order in which a fresh session discovers and loads those artefacts**. A WP, session launch brief, handoff, index, or chat instruction may add role-specific material, but it may not silently replace or reorder Steps 1–2 below. If another current control requires an incompatible bootstrap order, stop and record the conflict.

## Step 1 — Identify authoritative state

Read, in this order:

1. `development/03_plan/STATE.md`
2. the active WP named there
3. `development/01_governance/SOURCE_OF_TRUTH.md`
4. `development/01_governance/WORKING_PROTOCOL.md`

This bootstrap order exists so a fresh session can first discover the current work and then load the rules that govern authority and execution. Reading order does not change the semantic authority hierarchy in `SOURCE_OF_TRUTH.md`.

## Step 2 — Load only role-relevant governance

- Designer/builder: `ROLE_MODEL.md`, `DECISION_POLICY.md`, `CHANGE_POLICY.md`
- Researcher: `ROLE_MODEL.md`, `SOURCE_OF_TRUTH.md`, active WP evidence obligations
- Verifier: `ROLE_MODEL.md`, `VERIFICATION_POLICY.md`
- Adversarial reviewer: `ROLE_MODEL.md`, active WP, review template
- Integrator: `ROLE_MODEL.md`, `VERIFICATION_POLICY.md`, `PR_GATE.md`, relevant verification/review artefacts

## Step 3 — Load foundation and WP-required readings

Read the foundation files and exact `Required reading` references named by the active WP. A WP may specify an order **within this Step 3 material** when independence or evidence handling requires it; that local order begins only after Steps 1–2 are complete and cannot retroactively reorder the bootstrap.

Historical session records and launch briefs are evidence/continuity artefacts, not alternative cold-start authorities. Do not substitute remembered chat context for missing repository material.

## Step 4 — Declare session responsibility

Before substantive work, state the session role and one primary responsibility. If the requested responsibility conflicts with the active WP or authority hierarchy, stop and record the conflict rather than silently widening scope.

## Step 5 — Work and close through repository state

When the responsibility is complete, follow the session-close requirements in `WORKING_PROTOCOL.md` and leave a session handoff. Verifier sessions additionally leave canonical-state transition to a separate integrator under `VERIFICATION_POLICY.md`.

A cold-start is successful when the new session can determine what is true, what work is active, what it is authorised to do, and what completion means without replaying the previous chat.
