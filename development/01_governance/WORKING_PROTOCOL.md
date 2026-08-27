# WORKING PROTOCOL

This protocol is the manual precursor of the operating discipline SOUL itself is expected to automate later.

## Unit of work

No substantial development begins as an unbounded conversation topic. It begins as a **Work Package (WP)** with:

- objective,
- problem statement,
- scope and non-scope,
- required inputs and readings,
- dependencies,
- outputs,
- acceptance criteria,
- required verification,
- decision authority,
- current status.

A WP may span multiple sessions. A session should have one primary responsibility within the WP.

## Session cold-start

A new session does not assume the previous chat is available or correct.

The **single sequencing authority** for fresh-session bootstrap is `development/03_plan/COLD_START.md`. This protocol does not define a second ordered reading procedure.

`COLD_START.md` loads `REASONING_POLICY.md` as common governance for every role before substantive work. The reasoning policy governs how material premises, evidence, framing, alternatives, failure causes and completion claims are examined; it does not redefine the active WP or widen role authority.

A WP's `Required reading` section is loaded at the point assigned by `COLD_START.md`. A WP may prescribe an internal order among those Step 3 readings when needed for independence or evidence handling, but it may not silently reorder the earlier bootstrap steps. Historical launch briefs and handoffs may point to `COLD_START.md`; they are not competing sequencing authorities.

When canonical state assigns an independent verifier or adversarial reviewer,
`COLD_START.md` performs pending-result discovery before role selection and
repeats the live check immediately before independent-role commitment. The guard
may route the session to bounded Integrator/result-control handling, including
exact-head resolution, moving-candidate containment or repository/key-wide
candidate-set containment, but it does not itself change canonical state or
promote evidence into authority.

Every active independent verification/review WP must declare a result-control
key consisting of WP identifier, role, exact target and attempt number. Changing
an attempt is a canonical WP/state transition performed only through the bounded
Integrator recovery rules; an evidence producer cannot advance its own key.
Candidate containment is likewise canonical Integrator state bound to that
complete key. Stream containment additionally binds one PR identity;
candidate-set containment binds the exact canonical repository. A candidate
author cannot create, widen or reset either control by moving a PR head,
changing branch/PR state, opening a fresh PR identity or editing locator
metadata. Neither control suppresses direct current-valid-result routing.

If repository state is insufficient or internally contradictory, that is a finding. The session must not repair the gap by silently inventing prior intent.

## Session role

Each substantial session declares one primary role before work begins, for example:

- designer/builder,
- researcher,
- verifier,
- adversarial reviewer,
- integrator.

The same session should not produce a material design and then act as its only independent verifier.

## During work

- Apply `REASONING_POLICY.md` proportionally: baseline epistemic rules always apply; deeper checks are triggered by material risk/uncertainty/novelty rather than every atomic edit.
- New assumptions are written down when they materially affect the result.
- New architecture choices are not buried in implementation prose; they enter the decision process.
- Research results are stored as evidence, not silently promoted into decisions.
- Scope expansion requires updating the WP or opening a new WP.
- If required capability is missing, the session records the missing capability explicitly; creating or integrating it requires its own controlled work path.

## Session close

A substantial session is not complete until repository state is updated as required by the role and current transition. The close must leave:

1. produced or changed artefacts,
2. evidence references,
3. any decision record created or required,
4. WP status update,
5. `STATE.md` update when the project state changed and the session has authority to perform that transition,
6. a session handoff record in `07_sessions/`.

The handoff record contains:

- session ID and date,
- WP,
- role,
- inputs read,
- outputs produced,
- decisions taken or proposed,
- evidence created/used,
- verification status,
- unresolved items,
- exact next required responsibility,
- relevant commit or PR reference when available.

A new session should be able to continue from these artefacts without reading the old chat.

### Verifier close and canonical transition

A verifier records the result and verifier handoff, binds both to the complete active result-control key, and publishes them in a dedicated evidence PR targeting the active development branch. A result is not a completed published result for cold-start routing until that PR exists. A branch-only or local result is incomplete publication.

The evidence PR contains only the result artefact and corresponding handoff. It contains no repair, canonical state/WP transition, acceptance-criteria change, ADR acceptance, target merge or Phase transition. PR metadata is a locator; direct artefact/handoff/scope inspection is required.

The verifier does **not** use verifier authority to integrate its own result into canonical project state, resolve/exclude its own evidence, advance the attempt key or repair findings. After publication, a separate Integrator performs the result-dependent canonical-state transition defined in `VERIFICATION_POLICY.md`. Adversarial reviewers follow the same publication and separation rules.

This separation prevents a verification result from being silently converted into acceptance, repair, or a new active-work decision by the verifier that issued it.

### Result-control activation bridge

When a proposed general pending-result control is itself still unmerged/unaccepted, the active verification/review WP used to test that proposal must carry a **WP-local activation bridge**. The bridge is a Step-3/Step-4 precondition, not a second bootstrap authority: it preserves COLD_START Steps 1–2, declares the exact result-control key, requires same-WP candidate discovery/resolution handling, and requires the final live re-check immediately before independent-role commitment.

The bridge is activated canonically only by routing `STATE.md` to that active WP. It must be labelled provisional, scoped to the one WP/key, bound to an exact canonical activation commit, and inspected as rollout evidence by the verifier/reviewer. It does not merge or accept the proposed general governance and must not be described as transition-only if it adds substantive temporary control semantics.

Once accepted general governance provides the same control, later WPs use `COLD_START.md` directly and do not retain duplicated bridge text.

## Branch and PR discipline

- `main` represents accepted project truth.
- Material work occurs on a branch associated with a WP or controlled bootstrap activity.
- A WP is merged only after its declared acceptance criteria and verification requirements are satisfied.
- A producing agent's statement that the WP is complete is not a merge condition.
- PR discussion may explain a change, but canonical decisions and state must still live in repository artefacts.

## No silent shortcuts

Temporary choices that alter architecture, authority, evidence quality, state continuity, verification, or future extensibility must be recorded as explicit decisions or constraints. "We can fix it later" is not an acceptable substitute for a known architectural obligation.
