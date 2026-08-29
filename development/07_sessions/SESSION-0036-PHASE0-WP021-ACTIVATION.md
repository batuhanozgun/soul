# SESSION-0036 — Phase 0 WP-021 Activation

**Date:** 2026-08-29  
**WP:** WP-021 — Development OS Lifecycle and Work-Selection Improvement  
**Primary responsibility:** owner-directed work activation / project-state routing before candidate design work  
**Starting canonical commit:** `c4ebef9e58a4a94edce22ebbb94d94414dffd92c`

## Inputs read

- `development/03_plan/STATE.md`
- `development/04_work/WP-020-PHASE0-UNCONTAINED-INSPECTION-FAIL-CLOSED-REPAIR.md`
- `development/01_governance/SOURCE_OF_TRUTH.md`
- `development/01_governance/WORKING_PROTOCOL.md`
- `development/01_governance/REASONING_POLICY.md`
- `development/01_governance/ROLE_MODEL.md`
- `development/01_governance/DECISION_POLICY.md`
- `development/01_governance/CHANGE_POLICY.md`
- `development/01_governance/VERIFICATION_POLICY.md`
- `development/03_plan/COLD_START.md`
- `development/03_plan/PR_GATE.md`
- `development/03_plan/PHASE_GATE.md`
- `development/03_plan/ROADMAP.md`
- `development/04_work/WP-000-DEVELOPMENT-OS.md`
- `development/04_work/WP-005-DEVELOPMENT-REASONING-POLICY.md`
- `development/02_architecture/decisions/ADR-0001-DEVELOPMENT-REASONING-POLICY.md`
- `development/01_governance/ADR_TEMPLATE.md`
- owner-directed exploratory planning records in `batuhanozgun/keel-research` scratch branch, including the target model and safe transition plan, treated as non-authoritative evidence/input only.

## Why activation precedes design work

The prior Development OS recorded PD-002 when material work began before canonical active-WP transition. This activation deliberately occurs before WP-021 candidate design is written into SOUL.

The owner authorised the Development OS improvement study and explicitly allowed execution to begin when planning was judged mature. The improvement is now treated as Phase-0 work because it concerns the operating system used to develop SOUL, not SOUL product/runtime architecture.

## State transition

- Created immutable fallback checkpoint branch `checkpoint/phase0-pre-lifecycle-v2-c4ebef9` at `c4ebef9e58a4a94edce22ebbb94d94414dffd92c`.
- Activated WP-021 as the current Phase-0 work.
- Blocked WP-020 from execution without resolving, cancelling or weakening F-AR-008.
- Preserved PR #22 and all WP-018/WP-019 exact-target/result bindings unchanged.
- Did not create or accept a new lifecycle architecture, ADR or F-AR-008 repair.

## Decisions taken

This session does not decide the substantive Development OS architecture.

It records only the authorised sequencing decision that the Development OS lifecycle/work-selection problem must be designed and evaluated before another F-AR-008 repair is executed under the old automatic repair-shaped route.

## Evidence/status

The underlying execution-bias/work-selection hypothesis remains **supported but not causally proven as the sole root cause**. WP-021 therefore requires pre-build challenge and historical replay/evaluation before candidate governance implementation.

## Exact next responsibility

Continue WP-021 on a separate candidate branch in an existing `designer/builder` **design-only** responsibility. Produce:

- proposed `development/02_architecture/DEVELOPMENT_LIFECYCLE.md`;
- proposed ADR-0003;
- function/motivation justification;
- historical replay protocol;
- design-stage handoff.

Then stop implementation and route the exact frozen design to a fresh pre-build adversarial reviewer. Do not modify operational governance policies to enact the new lifecycle before that challenge and replay/evaluation gate is satisfied.
