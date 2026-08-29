# WP-004 — Phase 0 F2-R1 Repair

**Status:** materially complete — awaiting fresh independent verification  
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

## Repair performed

`development/03_plan/BUILDER_STOP.md` was deleted rather than rewritten.

Reason: the file had no independent durable responsibility after `STATE.md`, the active WP, `COLD_START.md`, and the role/verification policies became the canonical routing controls. Retaining a second stop/routing artefact would preserve the exact duplication class that caused F2-R1 and create future drift risk.

The subordinate `WORKSPACE_INDEX.md` is updated separately and must not recreate a specific current-work pointer outside its explicitly derived section.

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

The owner-approved reasoning-policy change is intentionally not hidden inside this verifier-triggered repair. It is handled as a separate material governance work package before the next fresh verification target is cut.

## Acceptance criteria builder check

1. `BUILDER_STOP.md` no longer materialises a stale pointer: **builder claim PASS** — file removed.
2. File removed rather than retained without independent responsibility: **builder claim PASS**.
3. Current planning/control surfaces inspected for the same exact class: **builder claim PASS** for the surfaces named by WP-003/F2-R1; `STATE.md` remains authoritative, `NEXT_SESSION.md` is derived and does not materialise current values, `WORKSPACE_INDEX.md` is explicitly subordinate.
4. WP-000 acceptance criteria and owner/ADR/adversarial/Phase gates remain unchanged by this bounded repair: **builder claim PASS**.
5. Builder records repair as material and does not claim independent verification: **PASS**.

These are producer claims, not independent verification.

## Required verification

Fresh independent verification is required after the complete material target is ready. The next verifier must re-check all WP-000 criteria and explicitly regression-test F2-R1 on the exact changed target.

## Completion state

**Material repair complete; awaiting superseding fresh verification.**

WP-000 and Phase 0 remain unverified/unaccepted.
