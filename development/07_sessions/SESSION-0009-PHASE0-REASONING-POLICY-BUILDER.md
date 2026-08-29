# SESSION-0009 — Phase 0 Reasoning Policy Builder

**Role:** Designer / Builder  
**Primary responsibility:** Implement the owner-approved development reasoning-policy architecture without creating a second session-bootstrap authority  
**Date:** 2026-08-26  
**Branch:** `phase0/development-os`  
**WP:** WP-005

## Inputs used

- prior KEEL-Work, keel-dev, oyun2, os-architect and keel-research instruction/research files recorded in the synthesis evidence;
- `DECISION_POLICY.md`;
- `CHANGE_POLICY.md`;
- `VERIFICATION_POLICY.md`;
- `COLD_START.md`;
- strengthened WP-000 requirements;
- owner approval of the proposed direction.

## Outputs produced

- canonical `development/01_governance/REASONING_POLICY.md`;
- `development/05_evidence/REASONING-POLICY-SYNTHESIS-2026-08-26.md` separating source observations from SOUL synthesis;
- proposed ADR-0001;
- COLD_START integration as common governance for every role;
- WORKING_PROTOCOL/governance index integration;
- strengthened WP-000 acceptance criterion 12;
- derived minimal `CHATGPT_PROJECT_ENTRY.md` that points to repository cold-start rather than copying the policy;
- updated workspace/state material.

## Design decisions proposed

- repository policy, not Project Instructions, is the canonical reasoning-policy home;
- COLD_START remains the one sequencing authority;
- deeper reasoning checks are triggered by material risk/ambiguity/novelty/irreversibility rather than every atomic action;
- observable decision rationale/evidence is recorded, not private chain-of-thought;
- prompt policy is a bootstrap control, not a substitute for mechanical enforcement or independent verification.

These decisions remain proposed under ADR-0001 until independent review/Phase 0 acceptance.

## Process defect encountered

PD-002 records that WP-005 material work began before the canonical active-WP pointer was transitioned from completed WP-004 to WP-005. The defect was recorded rather than erased; `STATE.md` was corrected before further material work. Fresh verification must inspect the final current-work discipline and whether stronger activation mechanics are justified.

## Verification status

**NOT independently verified.**

All WP-005 acceptance checks recorded by the builder are producer claims only. Historical WP-003 PASS fragments are stale for the changed target.

## Handoff

Next responsibility: **fresh Verifier** against the exact current PR #1 head after the fresh verification WP/state handoff is activated.

The verifier must re-derive expected results from the strengthened WP-000/current governance before reading this builder handoff, verify all twelve criteria, regression-test F2-R1, inspect reasoning-policy integration and PD-002, and perform no repair.
