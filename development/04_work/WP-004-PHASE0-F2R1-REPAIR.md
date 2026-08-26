# WP-004 — Phase 0 F2-R1 Repair

**Status:** active  
**Owner role:** designer/builder  
**Decision authority:** repair only within the exact verifier finding and existing governance; no acceptance-criteria weakening, verifier self-certification, ADR acceptance, adversarial review, target merge, or Phase 1 authority  
**Branch:** `phase0/development-os`  
**Parent:** `WP-000-DEVELOPMENT-OS.md`  
**Trigger:** WP-003 exact-target FAIL, finding F2-R1

## Objective

Remove or explicitly subordinate the stale current-work/next-responsibility pointer in `development/03_plan/BUILDER_STOP.md` so the repository has one authoritative current-work home under `STATE.md` + active WP.

## Exact finding

WP-003 verification against `a02e36e5e71522995b74fb018a6b28235f1d7848` found that `BUILDER_STOP.md` still stated that WP-001 was the next legitimate execution unit while canonical `STATE.md` named WP-003. The file was not marked historical, derived, or subordinate.

Canonical evidence: `development/06_reviews/VERIFICATION-WP-000-2026-08-26.md`, finding F2-R1.

## Scope

- repair `development/03_plan/BUILDER_STOP.md` so it cannot act as a competing current-work pointer;
- inspect current planning/governance surfaces for the same exact stale-pointer class exposed by F2-R1;
- update only subordinate navigation/handoff material required to preserve single-source discipline;
- leave a builder handoff stating the exact material change and verification requirement.

## Non-scope

- changing WP-000 acceptance criteria to make the failure pass;
- changing F1 or PD-001 controls except if a direct contradiction is mechanically exposed by this bounded repair;
- redesigning the Development Operating System;
- implementing the separately owner-approved SOUL reasoning policy;
- independent verification;
- adversarial review;
- ADR acceptance;
- merging PR #1 or beginning Phase 1.

The owner-approved reasoning-policy change is intentionally not hidden inside this verifier-triggered repair. It will be handled as a separate material governance work package after this bounded defect repair is complete, with both changes included in the next fresh verification target.

## Required reading

Enter through `development/03_plan/COLD_START.md`. After Steps 1–2, read within Step 3:

1. `development/06_reviews/VERIFICATION-WP-000-2026-08-26.md`
2. `development/01_governance/SOURCE_OF_TRUTH.md`
3. `development/01_governance/CHANGE_POLICY.md`
4. `development/03_plan/STATE.md`
5. `development/03_plan/BUILDER_STOP.md`
6. `development/03_plan/NEXT_SESSION.md`
7. `development/03_plan/WORKSPACE_INDEX.md`
8. `development/04_work/WP-000-DEVELOPMENT-OS.md`

## Acceptance criteria

1. `BUILDER_STOP.md` no longer materialises a specific current WP or next responsibility that can become stale.
2. The file is either removed if it has no remaining independent responsibility, or rewritten as an explicitly historical/derived/subordinate control whose current routing is obtained from `STATE.md`.
3. No other current planning/control artefact inspected for the same class contains an unqualified competing current-work pointer.
4. WP-000 acceptance criteria and owner/ADR/adversarial/Phase gates remain unchanged by this repair.
5. The builder records the repair as material and does not claim independent verification.

## Required verification

Fresh independent verification is required after this material repair. The next verifier must re-check all WP-000 criteria and explicitly regression-test F2-R1 on the exact changed target.

## Completion state

Current: **active — bounded builder repair required**.

The builder may mark this package materially complete / awaiting verification, but may not mark WP-000 or Phase 0 verified-complete.
