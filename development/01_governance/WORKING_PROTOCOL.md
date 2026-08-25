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

Before substantive work it must read, in order:

1. this repository's foundation and source-of-truth rules,
2. `03_plan/STATE.md`,
3. the active WP,
4. the WP's `Required reading` references,
5. only the additional evidence or architecture material needed for its assigned responsibility.

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

A substantial session is not complete until repository state is updated. The close must leave:

1. produced or changed artefacts,
2. evidence references,
3. any decision record created or required,
4. WP status update,
5. `STATE.md` update when the project state changed,
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

## Branch and PR discipline

- `main` represents accepted project truth.
- Material work occurs on a branch associated with a WP or controlled bootstrap activity.
- A WP is merged only after its declared acceptance criteria and verification requirements are satisfied.
- A producing agent's statement that the WP is complete is not a merge condition.
- PR discussion may explain a change, but canonical decisions and state must still live in repository artefacts.

## No silent shortcuts

Temporary choices that alter architecture, authority, evidence quality, state continuity, verification, or future extensibility must be recorded as explicit decisions or constraints. "We can fix it later" is not an acceptable substitute for a known architectural obligation.
