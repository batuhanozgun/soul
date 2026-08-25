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

A WP's `Required reading` section is loaded at the point assigned by `COLD_START.md`. A WP may prescribe an internal order among those Step 3 readings when needed for independence or evidence handling, but it may not silently reorder the earlier bootstrap steps. Historical launch briefs and handoffs may point to `COLD_START.md`; they are not competing sequencing authorities.

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

A verifier records the result and verifier handoff but does **not** use verifier authority to integrate its own result into canonical project state or to repair findings. After the verifier closes, a separate integrator performs the result-dependent canonical-state transition defined in `VERIFICATION_POLICY.md`.

This separation prevents a verification result from being silently converted into acceptance, repair, or a new active-work decision by the verifier that issued it.

## Branch and PR discipline

- `main` represents accepted project truth.
- Material work occurs on a branch associated with a WP or controlled bootstrap activity.
- A WP is merged only after its declared acceptance criteria and verification requirements are satisfied.
- A producing agent's statement that the WP is complete is not a merge condition.
- PR discussion may explain a change, but canonical decisions and state must still live in repository artefacts.

## No silent shortcuts

Temporary choices that alter architecture, authority, evidence quality, state continuity, verification, or future extensibility must be recorded as explicit decisions or constraints. "We can fix it later" is not an acceptable substitute for a known architectural obligation.
