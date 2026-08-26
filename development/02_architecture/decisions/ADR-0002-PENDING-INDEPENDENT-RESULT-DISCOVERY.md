# ADR-0002 — Pending Independent Result Control and Bounded Recovery

**Status:** proposed — pending fresh independent verification, fresh adversarial re-review, and Phase 0 decision gates
**Decision class:** Architecture decision
**Date:** 2026-08-26
**Supersedes:** none
**Superseded by:** none

## Problem

F-AR-001 established that a generic cold-start can repeat an independent verifier/reviewer after that role publishes evidence but before a separate Integrator transitions canonical state. The first proposed repair at PR #13 exact target `a45b463b083604d3f59d75bdca5ba97d5bc170e6` added evidence-PR discovery, but WP-010 found three surviving defects:

- F-AR-002: the unmerged guard did not protect its own verifier/reviewer result intervals;
- F-AR-003: resolved same-WP stale/malformed residue had no durable exclusion lifecycle and could block forever;
- F-AR-004: one early check left a publication-during-bootstrap race.

The immediate failures are missing rollout activation, missing resolution identity/lifecycle and missing final freshness control. The system cause is that the first design treated discovery as a one-time binary check, while safe execution needs a bounded state machine spanning canonical assignment, subordinate evidence publication, candidate resolution and role commitment.

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

Chosen. It extends the existing repository/PR mechanism with the minimum state needed to distinguish current attempts, resolve only proven-invalid immutable candidates, re-check freshness at the role-commit edge, and self-host provisionally through the active verification/review WP.

## Evidence used

- immutable WP-010 adversarial re-review and SESSION-0017;
- real WP-009 verifier evidence PR #14 / merge `37f4bceb8f7ad4e0552f52af3ce878db03eb694f`;
- real WP-010 reviewer evidence PR #15 / merge `c8fc17bc50ca04893cc6a87e492408c078c79311`;
- historical PR #10 / PR #12 F-AR-001 lifecycle evidence;
- GitHub's documented create/update-reference conflict behaviour, considered and rejected as a new lease dependency for this repair;
- WP-011 producer regression evidence and executable decision-table model.

## Decision

1. **Canonical result-control key.** Every active independent WP declares WP, role, exact target and positive attempt. Evidence/handoff must match all four values.
2. **Two freshness checks.** Candidate discovery runs after canonical Step 1 and again live immediately before independent-role commitment. Nothing substantive occurs between the final check and commitment.
3. **Exact-head resolution.** A separate Integrator may resolve only a candidate proven not to be a current valid result. The canonical record binds repository, PR number and immutable PR head SHA plus observed/expected keys, scope and evidence. Head movement reopens inspection.
4. **No valid-result suppression.** A validating current result cannot be excluded. Multiple valid current results remain a conflict; the Integrator preserves them and canonically activates a fresh attempt/key.
5. **Bounded recovery.** Invalid/stale/malformed candidates recover after an exact-head resolution is integrated canonically. Uninspectable/discovery-unavailable cases recover only when inspection becomes possible. Closing a PR alone has no resolution effect.
6. **Authority separation.** Evidence PRs and resolution records only affect routing. `STATE.md` + active WP remain canonical, and only a separate Integrator transitions them.
7. **Provisional self-hosting bridge.** While the general proposal is unmerged, the exact verification/re-review WP carries a WP-local Step-3/Step-4 guard bound to one key and one canonical activation commit. It is explicitly provisional material rollout control, not accepted general governance and not a transition-only change.

## Rationale

Attempt identity prevents later executions from being conflated with historical same-WP evidence. Exact-head resolution is narrower than an ignore label: it cannot survive head movement and cannot lawfully suppress a validating current result. The final re-check directly addresses the observed check-then-act window without inventing a lease subsystem. The WP-local bridge uses an already authoritative active WP to protect the proposal's own rollout while preserving the one canonical bootstrap sequence and making the provisional activation visible for review.

## Consequences and new risks

Positive consequences:

- PR #14/#15-shaped post-result intervals route generically to Integrator;
- resolved stale/malformed residue does not block indefinitely;
- arbitrary suppression is constrained by immutable identity and validation rules;
- publication during long Step-2/3 reading is detected at the final gate;
- rollout does not require a human-selected scheduler.

Costs/risks:

- independent WPs must carry an attempt key;
- rare invalid candidates require an Integrator resolution record;
- a canonical resolution record that is itself wrong remains reviewable governance evidence and must be corrected through a new exact record/state transition;
- GitHub/PR inspection availability remains an external dependency and fails closed;
- no platform transaction spans final PR inspection and a model's first substantive action, leaving a narrow documented residual edge;
- the temporary WP-local bridge duplicates control semantics once and must be removed from later WPs after general acceptance.

## Rejected alternatives and why

See Options considered. Reminder-only control is too weak; producer self-transition violates authority separation; a second canonical store violates single-source discipline; and a lease introduces a larger stale-lock system than WP-011 requires.

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

A fresh separate adversarial re-review must then attack resolution forgery, head movement, attempt confusion, bridge drift, final-check timing and authority leakage.

## Reopen conditions

Reopen if a supported host cannot expose immutable PR heads/candidate scopes reliably; resolution records repeatedly cause false exclusions or operational burden; the WP-local bridge cannot protect generic cold-start; the residual final-check edge reproduces material duplicate work; or a platform-native atomic handoff becomes available with less state and equal authority separation.

## Relation to the earlier proposal

PR #13 remains the immutable rejected WP-008 candidate at `a45b463...`. This revised ADR is published from current canonical development head in the WP-011 superseding repair PR. PR #13 is not amended or merged; the new PR supersedes it while preserving its historical verification/re-review bindings.
