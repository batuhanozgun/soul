# ADR-0002 — Pending Independent Result Control and Bounded Convergence

**Status:** proposed — pending fresh independent verification, fresh adversarial re-review, and Phase 0 decision gates
**Decision class:** Architecture decision
**Date:** 2026-08-26; revised 2026-08-27 under WP-014 and WP-017
**Supersedes:** none
**Superseded by:** none

## Problem

F-AR-001 established that a generic cold-start can repeat an independent verifier/reviewer after that role publishes evidence but before a separate Integrator transitions canonical state. The first proposed repair at PR #13 exact target `a45b463b083604d3f59d75bdca5ba97d5bc170e6` added evidence-PR discovery, but WP-010 found three surviving defects:

- F-AR-002: the unmerged guard did not protect its own verifier/reviewer result intervals;
- F-AR-003: resolved same-WP stale/malformed residue had no durable exclusion lifecycle and could block forever;
- F-AR-004: one early check left a publication-during-bootstrap race.

The immediate failures are missing rollout activation, missing resolution identity/lifecycle and missing final freshness control. The system cause is that the first design treated discovery as a one-time binary check, while safe execution needs a bounded state machine spanning canonical assignment, subordinate evidence publication, candidate resolution and role commitment.

PR #16 exact target `adf067e4289e4c0b51cf40c1940193e8252b22e0`
implemented that state machine. WP-012 issued exact-target **PASS**, but WP-013
later issued **Requires repair** and preserved F-AR-005: exact-head resolution
converges only while an invalid candidate head stays fixed. The same mutable
lower-authority PR can move after every resolution and force an unbounded series
of Integrator routes and canonical commits. Closing, force-pushing or attempt
advancement does not provide bounded recovery, while broad PR-wide exclusion
could hide a later current valid result.

PR #19 exact target `2f5508c1d6941e951d494bb2a700ef861860431d`
implemented PR-scoped moving-candidate containment. WP-015 issued exact-target
**PASS**, but WP-016 later issued **Requires repair** and preserved two defects:

- F-AR-006: fresh PR identities restart every PR-scoped recovery lifecycle, so
  lower-authority candidate creation retains unbounded repository-level denial;
- F-AR-007: the executable producer model routes uncontained invalid residue
  before one current-valid result, contradicting normative result precedence.

The immediate causes are a containment identity one level narrower than the
failure class and an invalid-first decision-table ordering. The system cause is
that recovery was bounded per locator while the active responsibility and
result-control key are repository-level facts.

## Decision scope

This decision governs only the SOUL development operating system's independent verifier/adversarial-review result lifecycle. It does not define the eventual reusable runtime, change WP-000 acceptance criteria, accept any historical result, or grant producers canonical-transition authority.

## Constraints

- `STATE.md` + active WP remain the sole canonical current-work authority.
- `COLD_START.md` remains the single bootstrap sequencing authority.
- Result evidence and resolution records remain subordinate.
- Verifier/reviewer output remains non-canonical until a separate Integrator acts.
- Current valid results cannot be hidden by an ignore mechanism.
- Discovery/inspection failures fail closed but have explicit recovery conditions.
- The proposal must protect its own verification/re-review rollout without claiming that proposed general governance is accepted.
- A lower-authority candidate must not be able to reset canonical recovery by
  repeated head, branch or PR-state mutation.
- Fresh PR identity creation under one unchanged repository/key must not reset
  canonical recovery indefinitely.
- A stream-level recovery rule must continue to admit a later current-valid
  exact-key result from the same PR identity.
- Exactly one current-valid result must route before invalid residue across the
  whole discovered candidate set; multiple current-valid results remain a
  conflict.

## Options considered

### Keep one early scan and add more warning text

Rejected. It leaves F-AR-004 and does not create durable recovery.

### Let the evidence producer update `STATE.md`

Rejected. It removes the interval by collapsing producer/Integrator separation.

### Add a second canonical pending-result database or pointer

Rejected. It creates competing current-state authority and its own drift/recovery problem.

### Use a repository lease/lock branch

Rejected for this Phase 0 repair. A lease would require ownership, expiry, stale-lease adjudication and atomic release semantics that are not otherwise present. It adds a larger recovery system than the timing-dependent finding requires. A platform-native transaction remains a reopen condition.

### Keyed discovery + exact-head resolutions + final re-check + WP-local rollout bridge

Chosen by WP-011, but insufficient alone after F-AR-005. It extends the existing
repository/PR mechanism with the minimum state needed for fixed-head recovery;
the later head-movement attack shows that immutable-head resolution alone is not
a bounded convergence rule.

### Permanently ignore or freeze a PR after movement

Rejected. A blind PR-wide exclusion can suppress a later corrected current-valid
head. Repository policy also cannot enforce a platform freeze on every
lower-authority branch or fork.

### Trust only selected authors or branches

Rejected as the primary control. Authorship narrows exposure but does not solve
accidental or compromised mutation by an otherwise authorised producer, and it
couples correctness to mutable host identity policy.

### Canonical moving-candidate containment with per-head validity override

Chosen for WP-014. After one exact-head invalid resolution and one later directly
inspected invalid moved head, a separate Integrator may canonically contain the
repository + PR identity under the complete active key. Later heads are still
classified. A valid head always bypasses containment and routes normally;
inspectable-invalid or candidate-specifically inaccessible later heads cannot
reset recovery or demand another canonical resolution.

### Freeze admission, trust authors, rate-limit PRs or add a host lease

Rejected for this repair. These mechanisms either depend on mutable host
administration, add ownership/expiry state, fail repository-only continuation,
or can block legitimate later result publication. They are broader than the
demonstrated repository/key recovery requirement.

### Canonical repository/key candidate-set containment with validity precedence

Chosen for WP-017. Retain exact-head and per-PR containment as narrow first
responses. After an earlier canonical invalid-candidate control and a later
directly inspected invalid claim at a distinct PR identity under the same
canonical repository and complete active key, a separate Integrator may create
one repository/key candidate-set containment. Every inspectable head is still
validated; one current-valid result routes before all invalid residue, multiple
current-valid results remain conflict, and only invalid or
candidate-specifically inaccessible residue loses reset authority.

## Evidence used

- immutable WP-010 adversarial re-review and SESSION-0017;
- real WP-009 verifier evidence PR #14 / merge `37f4bceb8f7ad4e0552f52af3ce878db03eb694f`;
- real WP-010 reviewer evidence PR #15 / merge `c8fc17bc50ca04893cc6a87e492408c078c79311`;
- historical PR #10 / PR #12 F-AR-001 lifecycle evidence;
- GitHub's documented create/update-reference conflict behaviour, considered and rejected as a new lease dependency for this repair;
- WP-011 producer regression evidence and executable decision-table model.
- immutable WP-013 adversarial re-review, SESSION-0022 and its independent
  five-generation moving-head trace;
- WP-014 producer regression evidence and expanded executable decision-table
  model, used only as producer evidence.
- immutable WP-016 adversarial re-review, SESSION-0028 and the reproduced
  nine-identity rotation plus mixed-state mutation traces;
- WP-017 producer regression evidence and corrected executable decision-table
  model, used only as producer evidence.

## Decision

1. **Canonical result-control key.** Every active independent WP declares WP, role, exact target and positive attempt. Evidence/handoff must match all four values.
2. **Two freshness checks.** Candidate discovery runs after canonical Step 1 and again live immediately before independent-role commitment. Nothing substantive occurs between the final check and commitment.
3. **Exact-head resolution.** A separate Integrator may resolve only a candidate proven not to be a current valid result. The canonical record binds repository, PR number and immutable PR head SHA plus observed/expected keys, scope and evidence. The first head movement reopens inspection.
4. **Current-valid precedence and no suppression.** Directly validate every
   inspectable same-WP head before routing invalid residue. Exactly one current
   valid result routes to Integrator regardless of resolved, contained or
   uncontained invalid residue. Multiple valid current results remain a
   conflict; the Integrator preserves them and canonically activates a fresh
   attempt/key.
5. **Bounded recovery.** Invalid/stale/malformed candidates recover after an exact-head resolution is integrated canonically. Uninspectable/discovery-unavailable cases recover only when inspection becomes possible. Closing a PR alone has no resolution effect.
6. **Authority separation.** Evidence PRs and resolution records only affect routing. `STATE.md` + active WP remain canonical, and only a separate Integrator transitions them.
7. **Provisional self-hosting bridge.** While the general proposal is unmerged, the exact verification/re-review WP carries a WP-local Step-3/Step-4 guard bound to one key and one canonical activation commit. It is explicitly provisional material rollout control, not accepted general governance and not a transition-only change.
8. **Bounded moving-candidate escalation.** If a candidate moves after an
   exact-head invalid resolution and the Integrator directly proves the later
   head invalid under the same complete active key, the Integrator may create
   canonical moving-candidate containment keyed by repository, PR number and all
   four key fields. This is the final canonical recovery escalation for that
   identity; candidate mutation cannot reset it.
9. **Validity override and contained states.** Containment never converts a head
   into valid evidence and never suppresses one. Each inspectable later head is
   validated directly: current-valid routes to Integrator; multiple-current
   remains a conflict; inspectable-invalid is contained. Candidate-specific
   inaccessibility after containment is an explicit contained non-valid state,
   Repository-wide discovery loss remains fail-closed.
10. **Bounded candidate-set escalation.** After an earlier canonical
    invalid-candidate control and a later directly inspected invalid candidate
    at a distinct PR identity under the same exact repository and active key,
    the Integrator may create canonical candidate-set containment keyed by
    `(canonical repository, WP, role, exact target, attempt)`. This is the final
    recovery escalation for fresh PR identities under that repository/key.
    Later inspectable candidates remain directly validated; invalid or
    candidate-specifically inaccessible residue is contained non-valid; one
    current-valid result and multiple-current conflict retain their normal
    precedence. Repository-wide discovery failure remains blocked.

## Rationale

Attempt identity prevents later executions from being conflated with historical
same-WP evidence. Exact-head resolution remains the narrow first recovery for a
fixed defect. Stream containment adds state only after repeated invalid movement
is observed. Candidate-set containment adds one final state transition only
after invalid claims cross a PR-identity boundary. Its repository + complete-key
identity matches the scope of the active responsibility, so subordinate locator
creation cannot reset it. The validity-first rule is the critical
non-suppression boundary: containment removes invalid residue's blocking
authority, not a later valid result's routing eligibility. This is smaller than
admission, trust, budget, lease or host-policy systems and directly addresses
the demonstrated denial class. The final re-check and WP-local bridge remain
unchanged for publication timing and provisional rollout.

## Consequences and new risks

Positive consequences:

- PR #14/#15-shaped post-result intervals route generically to Integrator;
- resolved stale/malformed residue does not block indefinitely;
- repeated invalid head generations converge after at most one exact-head
  resolution plus one canonical containment escalation;
- fresh invalid PR identities converge after at most one additional canonical
  candidate-set containment under an unchanged repository/key;
- one current-valid result routes before invalid residue in every mixed state;
- arbitrary suppression is constrained by immutable identity and validation rules;
- publication during long Step-2/3 reading is detected at the final gate;
- rollout does not require a human-selected scheduler.

Costs/risks:

- independent WPs must carry an attempt key;
- rare invalid candidates require an Integrator resolution record;
- repeated invalid movement requires one additional Integrator containment
  record, after which later candidate mutation is non-resetting;
- fresh identity rotation may require one final Integrator candidate-set record,
  after which later PR creation is non-resetting for that repository/key;
- a canonical resolution record that is itself wrong remains reviewable governance evidence and must be corrected through a new exact record/state transition;
- GitHub/PR inspection availability remains an external dependency and fails closed;
- candidate-specific inaccessibility after canonical containment no longer
  grants the contained identity renewed blocking authority; this deliberately
  changes routing only, never result validity;
- no platform transaction spans final PR inspection and a model's first substantive action, leaving a narrow documented residual edge;
- the temporary WP-local bridge duplicates control semantics once and must be removed from later WPs after general acceptance.

## Rejected alternatives and why

See Options considered. Reminder-only control is too weak; producer
self-transition violates authority separation; a second canonical store violates
single-source discipline; a lease introduces a larger stale-lock system; broad
ignore/freeze can hide corrected results; and author trust does not cover
authorised-but-mutable producers.

## Verification required

Fresh verification must bind to the new exact material target and separately inspect the exact canonical activation commit. It must:

1. re-check all current WP-000 criteria;
2. replay F-AR-001 PR #10/#12 and F-AR-002 PR #14/#15 intervals;
3. prove exact-head stale/malformed resolution unblocks later cold-start;
4. prove moved heads and valid current results cannot be hidden by old/forged resolutions;
5. preserve conflicts as conflicts and route a fresh attempt;
6. fail closed on unavailable discovery/inspection;
7. reproduce publication between first and final checks and observe final routing;
8. inspect the documented residual boundary and activation bridge without treating them as accepted governance;
9. confirm no historical result, WP-000 criterion, ADR status or Phase gate was weakened.
10. replay more than five successive invalid heads and prove the route converges
    after containment without further canonical resolution commits;
11. prove the same contained PR can later publish a current-valid exact-key head
    that routes to Integrator, while wrong-key containment cannot unblock it;
12. cover closed, force-pushed, inaccessible/deleted and reopened/valid head
    lifecycles plus global discovery outage separately.
13. replay a long sequence of fresh invalid PR identities and prove convergence
    after one candidate-set containment without further canonical controls;
14. prove valid + first invalid, valid + moved invalid, valid + multiple fresh
    invalid and multiple-valid + invalid route by current-result precedence;
15. deliberately mutate the executable model to invalid-first ordering and
    observe the mixed-state suite fail red;
16. prove wrong-key/repository, local and candidate-authored candidate-set
    records have no effect and a key change ends their scope.

A fresh separate adversarial re-review must then attack resolution forgery, head movement, attempt confusion, bridge drift, final-check timing and authority leakage.

## Reopen conditions

Reopen if a supported host cannot expose immutable PR heads/candidate scopes
reliably; either containment mode hides or delays a later valid result;
repository identity cannot be bound without mutable aliases; containment
records cause false exclusions or operational burden; candidate creation across
repositories reproduces a demonstrated in-scope denial class; the WP-local
bridge cannot protect generic cold-start; the residual final-check edge
reproduces material duplicate work; or a platform-native atomic handoff becomes
available with less state and equal authority separation.

## Relation to the earlier proposal

PR #13 remains the immutable rejected WP-008 candidate at `a45b463...`. PR #16
remains the immutable rejected WP-011 candidate at `adf067e...`, with WP-012
**PASS** and WP-013 **Requires repair** permanently bound only to it. PR #19
remains the immutable rejected WP-014 candidate at `2f5508c...`, with WP-015
**PASS** and WP-016 **Requires repair**/F-AR-006/F-AR-007 permanently bound only
to it. WP-017 publishes this revised proposal from the later canonical
development head in a new superseding draft PR; PR #19 is not amended or
merged. The new target requires fresh verification and fresh adversarial
re-review and does not accept this ADR.
