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

When canonical state assigns an independent verifier or adversarial reviewer, `COLD_START.md` also performs the pending independent-result guard before role selection. That guard may block duplicate independent execution and route the current session to a bounded Integrator check, but it does not itself change canonical state or promote evidence into authority.

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

### Independent-result publication contract

A verifier or adversarial reviewer may finish its analysis without changing canonical `STATE.md`, but a **completed repository-visible independent result** is not considered published until the role has created a dedicated evidence PR targeting the active development branch.

The publication PR must:

- contain the completed verification/review artefact and the corresponding session handoff;
- bind both records to the active WP/role and exact target artefact/version/commit;
- contain only authorised evidence/session files, with no repair, canonical-state/WP transition, acceptance-criteria change, ADR acceptance, target merge, Phase acceptance, or other authority-widening change;
- use PR metadata that makes the active WP discoverable; metadata is a locator only and does not replace direct artefact/changed-file inspection.

A branch-only result, local draft, or handoff that has not been published through this evidence-PR boundary is **not** a completed published result for cold-start routing. If the environment cannot publish the evidence PR, the independent session closes as blocked/incomplete publication rather than claiming that a completed result is awaiting integration.

After evidence-PR publication, canonical `STATE.md` intentionally remains unchanged until a separate Integrator validates and integrates the result. During that interval, the pending-result guard in `COLD_START.md` prevents a generic fresh session from repeating the just-completed independent role.

This publication rule does not make PR metadata canonical project state. `STATE.md` + active WP remain the canonical current-work authority; the evidence PR is a discoverable, lower-authority trigger that must be validated by the Integrator before any canonical transition.

### Verifier close and canonical transition

A verifier records the result and verifier handoff, publishes the dedicated evidence PR, but does **not** use verifier authority to integrate its own result into canonical project state or to repair findings. After the verifier closes, a separate integrator performs the result-dependent canonical-state transition defined in `VERIFICATION_POLICY.md`.

This separation prevents a verification result from being silently converted into acceptance, repair, or a new active-work decision by the verifier that issued it.

An adversarial reviewer follows the same publication/separation rule for its review artefact and handoff: the reviewer publishes evidence but does not repair findings or canonically transition its own result.

## Branch and PR discipline

- `main` represents accepted project truth.
- Material work occurs on a branch associated with a WP or controlled bootstrap activity.
- A WP is merged only after its declared acceptance criteria and verification requirements are satisfied.
- A producing agent's statement that the WP is complete is not a merge condition.
- PR discussion may explain a change, but canonical decisions and state must still live in repository artefacts.

## No silent shortcuts

Temporary choices that alter architecture, authority, evidence quality, state continuity, verification, or future extensibility must be recorded as explicit decisions or constraints. "We can fix it later" is not an acceptable substitute for a known architectural obligation.
