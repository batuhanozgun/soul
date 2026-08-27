# SESSION-0025 — Phase 0 WP-015 Activation Integrator

**Date:** 2026-08-27
**Work package:** WP-014 builder close → WP-015 verification activation
**Role:** integrator
**Development branch:** `phase0/development-os`
**Canonical start:** `dca520242585a80c2efaf22e18fe3d353147b93e`
**Material target PR:** #19 — `WP-014: bound moving-candidate convergence without result suppression`
**Exact material target:** `2f5508c1d6941e951d494bb2a700ef861860431d`
**Material base:** `dca520242585a80c2efaf22e18fe3d353147b93e`
**Builder-close routing head:** `80147ca0ebbf44a1dd608e10f10c514c1ab80002`
**WP-015 result-control key:** `WP-015 / verifier / 2f5508c1d6941e951d494bb2a700ef861860431d / attempt 1`
**WP-015 provisional activation:** `5368abd0f0c9a846f89120be44c19b1f1b1825d9`
**Activation-binding commit:** `3d49561b4bb87e36c4bbbf18c7a72247070f77e2`

## Entry and authority

The session entered exactly through canonical
`development/03_plan/COLD_START.md`, then read `STATE.md`, active WP-014,
`SOURCE_OF_TRUTH.md`, `WORKING_PROTOCOL.md`, common `REASONING_POLICY.md`,
Integrator role governance, `VERIFICATION_POLICY.md`, `PR_GATE.md`, all four
foundation files, WP-000, decision/change/Phase controls, WP-011/WP-012/WP-013,
the immutable WP-013 review and SESSION-0022, prior Integrator handoffs and the
subordinate index.

The declared responsibility was limited to validating the builder material and
builder-close routing scope, integrating only the authorised close records,
activating and exactly binding WP-015, and handing off to a fresh separate
verifier. No target verification, adversarial review, repair, result
integration, ADR acceptance, material merge, Phase acceptance or Phase 1 work
was authorised or performed.

## Live validation

Repository and GitHub state were refreshed independently before action.

- canonical `origin/phase0/development-os` remained exact
  `dca520242585a80c2efaf22e18fe3d353147b93e` with no partial WP-015 activation;
- all-state PR and remote-ref inspection found no WP-015 evidence candidate,
  competing Integrator branch or completed WP-015 result;
- draft PR #19 remained open against `phase0/development-os`, with exact head
  `2f5508c1d6941e951d494bb2a700ef861860431d`, exact base `dca520...` and exactly
  the declared nine material files;
- material merge-base and PR base were both exact `dca520...`; the three target
  commits were `61ea680...`, `ed1aa4e...` and `2f5508c...`;
- `git diff --check dca520... 2f5508c...` passed;
- the producer regression model was re-run at exact target and passed all 28
  declared cases; this remains producer evidence, not independent verification;
- PR #16 was live-confirmed closed, draft, unmerged and unchanged at immutable
  head `adf067e4289e4c0b51cf40c1940193e8252b22e0`, based on `8dcdc750...`, with
  eight files;
- WP-012 PASS and WP-013 **Requires repair**/F-AR-005 remain bound only to
  `adf067e...`; no historical evidence record was edited or reinterpreted;
- builder-close branch `codex/wp014-builder-routing` remained exact head
  `80147ca...`, based on `dca520...`, and changed exactly WP-014, proposed
  WP-015 and SESSION-0024;
- the main user worktree's unrelated untracked `.DS_Store` files were observed
  and left untouched.

## Work performed

1. Created a separate Integrator worktree/branch from exact canonical
   `dca520...`.
2. Fast-forwarded that branch to the exact validated builder-close head
   `80147ca...`, thereby integrating only the three builder-authorised records.
3. Transitioned canonical `STATE.md` and subordinate `WORKSPACE_INDEX.md` from
   WP-014 builder work to WP-015 verification.
4. Activated the exact WP-015 attempt-1 key and provisional verifier bridge in
   `5368abd0f0c9a846f89120be44c19b1f1b1825d9`, initially fail-closed pending
   binding.
5. Immediately bound that exact activation SHA in
   `3d49561b4bb87e36c4bbbf18c7a72247070f77e2`.
6. Left this Integrator handoff and routed only the fresh separate verifier
   responsibility.

## Change classification

- `310e0cd...` and `80147ca...` are builder-authorised close/routing records:
  WP-014 producer close, proposed WP-015 and SESSION-0024 only.
- `5368abd...` is the explicit WP-015 provisional material rollout activation,
  not target certification and not acceptance of PR #19 governance.
- `3d49561...` mechanically binds the exact activation SHA.
- this handoff and its subordinate index entry are session/routing evidence.

No commit changes the frozen PR #19 material target. WP-015 must independently
inspect the material and activation/binding chain.

## Decisions

None.

WP-015 activation is the deterministic next gate already required by WP-014 and
the governing verification separation. ADR-0002 remains proposed. PR #19, PR
#1, WP-000 and Phase 0 remain unaccepted/unmerged.

## Verification and review status

No independent verification or adversarial re-review exists for `2f5508c...`.
The 28/28 producer run is not independent proof. The only current independent
results remain WP-012 PASS and WP-013 **Requires repair** for historical target
`adf067e...` and their exact activations.

## Unresolved items

- fresh WP-015 exact-target verification under attempt 1;
- separate Integrator validation/integration of the verifier result;
- fresh separate adversarial re-review of the exact verified target;
- repair or authorised resolution of any later surviving material finding;
- ADR-0000/0001/0002, PR #19/#1, owner/PR/Phase gates;
- Phase 1 remains blocked.

## Exact next required responsibility

**Fresh separate verifier under
`development/04_work/WP-015-PHASE0-MOVING-CANDIDATE-CONVERGENCE-VERIFICATION.md`.**

The verifier must enter through canonical COLD_START, execute the first WP-015
bridge check after Steps 1–2, derive and persist expected checks before reading
producer rationale/evidence, inspect exact target and activation/binding commits,
run the final bridge check immediately before role commitment, publish only the
verification artefact plus verifier handoff PR, and stop for another separate
Integrator.

Do not continue verification, adversarial review, repair, acceptance, merge or
Phase work in this Integrator session.
