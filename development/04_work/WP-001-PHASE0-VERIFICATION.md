# WP-001 — Phase 0 Independent Verification

**Status:** ready  
**Owner role:** verifier  
**Decision authority:** verifier issues PASS / FAIL / NOT VERIFIED; no repair authority  
**Branch:** verifier should work from a fresh branch based on current `phase0/development-os` PR head or add review artefact through a dedicated verification branch/PR  
**Target:** draft PR #1 exact head commit at verification start

## Objective

Independently determine whether WP-000 and the Phase 0 development operating system satisfy their declared acceptance criteria and are sufficient for reliable cold-start continuation across fresh sessions.

## Problem

The Phase 0 artefacts were produced by a builder session. Under the proposed governance, that session cannot certify its own output. Before Phase 0 can be accepted, a fresh verifier must derive the expected result from the authoritative specification and inspect the exact reviewed commit.

## Scope

- every WP-000 acceptance criterion,
- internal consistency of foundation/governance/state/work-package artefacts,
- cold-start sufficiency from repository contents,
- stale/duplicate authority risks visible from the documents,
- verification freshness and exact-target binding.

## Non-scope

- repairing findings,
- redesigning the operating system,
- beginning Phase 1 product definition,
- accepting ADR-0000 on behalf of the human owner.

## Required reading

Read in this order:

1. `development/01_governance/VERIFICATION_POLICY.md`
2. `development/04_work/WP-000-DEVELOPMENT-OS.md`
3. `development/00_foundation/`
4. `development/01_governance/SOURCE_OF_TRUTH.md`
5. `development/01_governance/WORKING_PROTOCOL.md`
6. other governance/plan/templates required to test each criterion
7. only after expected results are derived: `development/07_sessions/SESSION-0001-PHASE0-BUILDER.md`

## Outputs

- `development/06_reviews/VERIFICATION-WP-000-<date>.md`
- verifier session handoff under `development/07_sessions/`
- no repair commits to Phase 0 artefacts.

## Acceptance criteria

1. All eleven WP-000 acceptance criteria receive PASS / FAIL / NOT VERIFIED with exact evidence.
2. The review identifies the exact commit SHA it certifies.
3. The verifier explicitly tests whether a fresh session can determine state, active work, authority, required readings, role and next responsibility without prior-chat replay.
4. The verifier checks for contradictory authoritative homes or duplicated state that could drift.
5. Findings are not repaired in the verifier session.
6. Overall PASS is issued only if every mandatory WP-000 criterion passes; NOT VERIFIED remains legitimate.

## Required verification

This WP is itself the independent verification activity. Its own procedural completion can later be checked by the integrator against this specification and the review artefact.

## Handoff

- PASS → separate adversarial-review session before Phase 0 acceptance.
- FAIL / NOT VERIFIED → fresh builder repair session, then a new verifier pass against the changed commit.
