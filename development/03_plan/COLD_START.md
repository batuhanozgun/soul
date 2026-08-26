# COLD START

This is the standard and authoritative sequencing procedure for a fresh SOUL development session.

`SOURCE_OF_TRUTH.md` defines which artefact wins when project claims conflict. This file separately defines **the order in which a fresh session discovers and loads those artefacts**. A WP, session launch brief, handoff, index, Project instruction, or chat instruction may add role-specific material, but it may not silently replace or reorder Steps 1–2 below. If another current control requires an incompatible bootstrap order, stop and record the conflict.

## Step 1 — Identify authoritative state

Read, in this order:

1. `development/03_plan/STATE.md`
2. the active WP named there
3. `development/01_governance/SOURCE_OF_TRUTH.md`
4. `development/01_governance/WORKING_PROTOCOL.md`

This bootstrap order exists so a fresh session can first discover the current work and then load the rules that govern authority and execution. Reading order does not change the semantic authority hierarchy in `SOURCE_OF_TRUTH.md`.

### Step 1A — Pending independent-result guard

After Step 1 and **before choosing/loading the active execution role**, apply this guard when the active WP assigns an independent verifier or adversarial reviewer whose completed result requires a separate Integrator transition.

The guard exists for the legitimate interval in which canonical `STATE.md` still names the independent role while that role has already published a completed result that has not yet been canonically integrated. It prevents duplicate independent execution without turning evidence into a competing state authority.

A completed independent result is discoverably published only through the evidence-PR publication contract in `WORKING_PROTOCOL.md` / `PR_GATE.md`: a dedicated evidence PR targets the active development branch and contains the completed result artefact plus the role handoff. A branch-only draft is not a completed published result.

Perform the guard in this order:

1. **Resolve the expected target.** Use the active WP's target rule and repository/PR metadata to determine the exact artefact/version/commit the active independent responsibility is supposed to inspect. Do not infer the target from chat or from an evidence PR.
2. **Discover same-WP evidence PRs.** Inspect repository PRs targeting the active development branch, including open PRs and merged/closed evidence PRs that may have been integrated before `STATE.md` was transitioned. Narrow by the active WP identifier where possible, but treat PR title/body only as discovery metadata, never as proof.
3. **Validate candidate contents.** A candidate is a current pending result only if direct inspection establishes all of the following: the result artefact and handoff both identify the active WP/independent role; they are bound to the expected exact target; the result is complete; and the PR changed-file scope is evidence/session-only with no repair, canonical-state, acceptance, ADR, target-merge, or Phase transition change.
4. **Classify before acting.** Distinguish:
   - **no same-WP candidate** — no published result for the active independent responsibility was found;
   - **one current-match candidate** — exactly one completed evidence-only result is unambiguously bound to the active WP/role and expected target;
   - **stale/target-mismatched candidate** — evidence claims the active WP/role but is bound to another target or its freshness cannot be established;
   - **conflicting/ambiguous candidates** — multiple plausible results, inconsistent role/target/result claims, incomplete publication, or evidence-only scope cannot be established.
5. **Route deterministically.**
   - no same-WP candidate → continue the normal cold-start and load the independent role;
   - one current-match candidate → **do not begin the independent role again**; the effective session role becomes **Integrator** for bounded validation/integration of that pending result and the canonical result transition;
   - stale/target-mismatched or conflicting/ambiguous candidate(s) → **fail closed**; do not start another independent execution and do not choose a result. The effective session role becomes **Integrator** for the smallest bounded freshness/conflict/result-publication resolution allowed by current governance;
   - clearly unrelated historical evidence for another WP/role is ignored after its mismatch is established.

If repository/PR discovery needed by this guard cannot be performed, the guard has **not** passed. Record the missing capability/blocker rather than assuming there is no pending result and starting duplicate independent work.

The guard changes only the **current session execution path**. It does not edit `STATE.md`, promote an evidence PR into canonical truth, reinterpret a result, or grant the independent producer authority to integrate its own output. Canonical state changes only after the separate Integrator validates the evidence and performs the authorised transition.

## Step 2 — Load common reasoning governance, then role-relevant governance

First, every role reads:

- `development/01_governance/REASONING_POLICY.md`

This is a common reasoning discipline, not a second bootstrap authority. It does not redefine the active WP, role authority or source-of-truth hierarchy.

Then load the material relevant to the **effective execution role after Step 1A** (normally the active WP owner role; Integrator when the pending-result guard routes there):

- Designer/builder: `ROLE_MODEL.md`, `DECISION_POLICY.md`, `CHANGE_POLICY.md`
- Researcher: `ROLE_MODEL.md`, `SOURCE_OF_TRUTH.md`, active WP evidence obligations
- Verifier: `ROLE_MODEL.md`, `VERIFICATION_POLICY.md`
- Adversarial reviewer: `ROLE_MODEL.md`, active WP, review template
- Integrator: `ROLE_MODEL.md`, `VERIFICATION_POLICY.md`, `PR_GATE.md`, relevant verification/review artefacts

## Step 3 — Load foundation and WP-required readings

Read the foundation files and exact `Required reading` references named by the active WP. A WP may specify an order **within this Step 3 material** when independence or evidence handling requires it; that local order begins only after Steps 1–2 are complete and cannot retroactively reorder the bootstrap.

When Step 1A routes the session to Integrator because a pending result exists, the active WP remains the canonical WP until the Integrator validates and performs the result transition. Read the active WP plus the candidate result/handoff and any Integrator-required governance needed to establish whether the candidate is current, stale, conflicting, or invalid. Do not execute the active independent role's substantive verification/review procedure while the guard is blocking it.

Historical session records and launch briefs are evidence/continuity artefacts, not alternative cold-start authorities. Project Instructions and remembered chat context are entry conveniences only; do not substitute them for missing repository material.

## Step 4 — Declare session responsibility

Before substantive work, state the session role and one primary responsibility. If Step 1A routed a pending result, declare the Integrator role and the bounded result-transition/resolution responsibility while explicitly preserving `STATE.md` as canonical until that transition is completed. Otherwise declare the active WP role/responsibility normally.

If the requested responsibility conflicts with the active WP, the Step 1A guard, or the authority hierarchy, stop and record the conflict rather than silently widening scope.

## Step 5 — Work and close through repository state

Apply `REASONING_POLICY.md` proportionally to the work: baseline epistemic rules always apply; deeper framing/necessity/falsification/root-cause checks are invoked only when their documented triggers apply.

When the responsibility is complete, follow the session-close requirements in `WORKING_PROTOCOL.md` and leave a session handoff. Verifier/reviewer sessions publish their completed independent result through the evidence-PR contract and leave canonical-state transition to a separate Integrator. Verifier sessions additionally follow `VERIFICATION_POLICY.md` result semantics.

A cold-start is successful when the new session can determine what is true, what work is active, whether a completed independent result is pending integration, what it is authorised to do, what reasoning discipline applies, and what completion means without replaying the previous chat.
