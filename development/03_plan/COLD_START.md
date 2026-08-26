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

After Step 1 and before choosing/loading an independent verifier or adversarial-reviewer execution role, apply this guard when the active WP says that the completed result requires a separate Integrator transition.

The active independent WP must declare one **result-control key** containing all four values below:

- active WP identifier;
- independent role;
- exact material target SHA/version;
- positive attempt number.

The key is canonical only because it is part of the active WP named by `STATE.md`. PR metadata, result artefacts, handoffs, resolution records and branch names remain subordinate evidence. A result artefact and handoff must bind themselves to the complete key; WP/role/target equality without attempt equality is not a current match.

Perform the guard in this order:

1. **Resolve the expected key from canonical state.** Read it from the active WP. Do not infer or repair a missing/incomplete key from chat, PR metadata, a handoff or a result artefact. Missing or contradictory key material is a fail-closed blocker.
2. **Discover same-WP candidates.** Inspect repository PRs targeting the active development branch, including open and merged/closed evidence PRs. PR title/body/labels are locators only.
3. **Apply only canonical exact-head resolutions.** A resolution record may exclude a candidate from repeated blocking only when the record is already present on the canonical development branch, was produced by a separate Integrator under `VERIFICATION_POLICY.md`, names the candidate PR number and immutable candidate head SHA, records the observed key/scope defect and supporting inspection, and does not purport to exclude a candidate that validates as a current result. A moved PR head is a new candidate; an old resolution does not apply to it.
4. **Validate every unresolved candidate directly.** A current pending result has the complete expected key in both the result artefact and handoff, a completed result, and evidence/session-only changed-file scope with no repair, canonical-state/WP transition, acceptance, ADR, target-merge or Phase change.
5. **Classify before acting.** Distinguish:
   - no unresolved same-WP candidate;
   - exactly one current-match candidate;
   - one or more invalid, stale, target/attempt-mismatched, incomplete, malformed or uninspectable candidates;
   - multiple current-match or otherwise conflicting candidates;
   - unavailable repository/PR discovery or inspection.
6. **Route deterministically.** No unresolved candidate permits bootstrap to continue. One current match routes to Integrator and blocks repeat independent execution. Any unresolved invalid/stale/ambiguous candidate, any conflict, or unavailable discovery/inspection fails closed to Integrator/blocker handling; it never permits arbitrary result selection or duplicate independent execution. Clearly unrelated another-WP evidence and exact-head candidates covered by valid canonical resolution records do not block.

An Integrator resolution is bounded by `VERIFICATION_POLICY.md` and `PR_GATE.md`. In particular, an exact-head resolution may classify only a candidate that fails current-result validation; it cannot suppress a valid current result. Multiple valid current results are preserved as a conflict and routed to a fresh canonical attempt instead of choosing one.

## Step 2 — Load common reasoning governance, then role-relevant governance

First, every role reads:

- `development/01_governance/REASONING_POLICY.md`

This is a common reasoning discipline, not a second bootstrap authority. It does not redefine the active WP, role authority or source-of-truth hierarchy.

Then load the material relevant to the effective execution route after Step 1A (normally the active WP owner role; Integrator/blocker handling when the guard routes there):

- Designer/builder: `ROLE_MODEL.md`, `DECISION_POLICY.md`, `CHANGE_POLICY.md`
- Researcher: `ROLE_MODEL.md`, `SOURCE_OF_TRUTH.md`, active WP evidence obligations
- Verifier: `ROLE_MODEL.md`, `VERIFICATION_POLICY.md`
- Adversarial reviewer: `ROLE_MODEL.md`, active WP, review template
- Integrator: `ROLE_MODEL.md`, `VERIFICATION_POLICY.md`, `PR_GATE.md`, relevant verification/review artefacts

## Step 3 — Load foundation and WP-required readings

Read the foundation files and exact `Required reading` references named by the active WP. A WP may specify an order **within this Step 3 material** when independence or evidence handling requires it; that local order begins only after Steps 1–2 are complete and cannot retroactively reorder the bootstrap.

When Step 1A routes to Integrator/blocker handling, the active WP and key remain canonical until an authorised transition. Read only the candidate/result/resolution evidence and Integrator governance needed to classify or recover; do not execute the blocked independent role's substantive procedure.

Historical session records and launch briefs are evidence/continuity artefacts, not alternative cold-start authorities. Project Instructions and remembered chat context are entry conveniences only; do not substitute them for missing repository material.

## Step 4 — Declare session responsibility

### Final independent-role commitment gate

Immediately before declaring or beginning an independent verifier/adversarial-reviewer responsibility, re-run Step 1A against live repository/PR state and the still-current canonical result-control key. No other reading, planning, branch creation or substantive action may occur between this final re-check and role commitment.

- If the key, canonical state, candidate set, candidate head, candidate inspection result or discovery capability changed, use the new Step 1A outcome.
- If the re-check cannot complete, fail closed; do not treat inability to inspect as absence.
- If it still yields no unresolved candidate, declare the independent role and begin the bounded responsibility.

This second check closes the publication-during-Steps-2/3 path. The repository host does not provide an atomic transaction spanning evidence-PR publication and a model session's first substantive action, so a publication after the final check remains a residual boundary. The control bounds that interval to the immediate check-to-commit edge and requires later result conflict handling; it does not claim a platform-level lock that does not exist.

Before substantive work, state the session role and one primary responsibility. If Step 1A routes a pending result or unresolved candidate, declare Integrator/blocker handling rather than the independent role while preserving canonical state until an authorised transition. If the requested responsibility conflicts with the active WP, guard outcome or authority hierarchy, stop and record the conflict rather than silently widening scope.

## Step 5 — Work and close through repository state

Apply `REASONING_POLICY.md` proportionally to the work: baseline epistemic rules always apply; deeper framing/necessity/falsification/root-cause checks are invoked only when their documented triggers apply.

When the responsibility is complete, follow the session-close requirements in `WORKING_PROTOCOL.md` and leave a session handoff. Verifier/reviewer sessions bind result + handoff to the complete result-control key, publish through the evidence-PR contract, and leave canonical-state transition to a separate Integrator. Verifier sessions additionally follow `VERIFICATION_POLICY.md`.

A cold-start is successful when the new session can determine what is true, what work is active, whether a completed or unresolved independent-result candidate changes the execution route, what it is authorised to do, what reasoning discipline applies, and what completion means without replaying the previous chat.
