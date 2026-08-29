# WP-005 — Development Reasoning Policy

**Status:** materially complete — awaiting fresh independent verification  
**Owner role:** designer/builder  
**Decision authority:** architecture proposal under ADR-0001; human owner approved the direction, but independent review/verification remains required before Phase 0 acceptance  
**Branch:** `phase0/development-os`  
**Parent:** `WP-000-DEVELOPMENT-OS.md`

## Objective

Add one canonical repository-based reasoning policy for SOUL development sessions, synthesize it from prior KEEL/KEEL-Work/OS-Architect/KEEL-Research lessons, and load it through the existing single `COLD_START.md` sequence without creating a second bootstrap authority.

## Owner direction

On 2026-08-26 the human owner approved this direction after review of the source synthesis and the explicit objection against copying prior instructions wholesale or placing a second reading order in ChatGPT Project Instructions.

Owner approval authorises the work; it does not replace independent verification or adversarial review of the resulting architecture.

## Material outputs

- `development/01_governance/REASONING_POLICY.md`
- `development/05_evidence/REASONING-POLICY-SYNTHESIS-2026-08-26.md`
- proposed `development/02_architecture/decisions/ADR-0001-DEVELOPMENT-REASONING-POLICY.md`
- updated `development/03_plan/COLD_START.md`
- updated `development/01_governance/WORKING_PROTOCOL.md`
- updated `development/01_governance/README.md`
- strengthened `development/04_work/WP-000-DEVELOPMENT-OS.md` with acceptance criterion 12
- derived `development/03_plan/CHATGPT_PROJECT_ENTRY.md`
- updated state/index/handoff material

## Scope preserved

The implementation does not:

- expose or persist private chain-of-thought;
- import predecessor prompts wholesale;
- create a second cold-start sequence;
- replace independent verification with self-checks;
- accept ADR-0001, ADR-0000 or Phase 0;
- implement the final reusable SOUL runtime reasoning architecture.

## Acceptance criteria — builder check only

1. Every fresh role loads `REASONING_POLICY.md` through `COLD_START.md`: **builder claim PASS**.
2. No second bootstrap order is introduced: **builder claim PASS**; Project entry points only to COLD_START.
3. Observed/inferred/assumed/verified distinction and proof limits exist: **builder claim PASS**.
4. Objective/method/state/evidence separation and no authority widening exist: **builder claim PASS**.
5. Material premise/framing/necessity/alternative/falsification/authority checks exist: **builder claim PASS**.
6. Reasoning depth is explicitly risk-proportional: **builder claim PASS**.
7. Failure analysis requires immediate + system/root cause and regression path: **builder claim PASS**.
8. Research/analytical provenance includes claim → computation/method → inputs/data → source/version: **builder claim PASS**.
9. Producer completion remains separate from verification: **builder claim PASS**.
10. Private chain-of-thought is explicitly excluded: **builder claim PASS**.
11. Technical decisions are not unnecessarily transferred to owner: **builder claim PASS**.
12. WP-000 was transparently strengthened rather than weakened: **builder claim PASS**.
13. Source synthesis separates observed source principles from SOUL-specific synthesis and treats duplicate predecessor files accordingly: **builder claim PASS**.
14. ADR-0001 remains proposed: **PASS**.
15. F2-R1 repair remains separate in WP-004: **PASS**.

These are producer claims and are not independent verification.

## Process defect PD-002

During this bootstrap session, WP-005 material writes began after WP-005 was created and owner direction was already queued, but before canonical `STATE.md` was transitioned from completed WP-004 to active WP-005.

The defect is preserved at `development/06_reviews/PROCESS-DEFECT-PD-002-WP-ACTIVATION-ORDER.md`; canonical state was corrected before further material work. This WP does not declare the defect harmless or self-verified. The fresh verifier must inspect it.

## Required verification

A fresh verifier must inspect the final exact PR #1 target and:

- re-run all twelve WP-000 acceptance criteria;
- regression-test F2-R1 on the same exact target;
- verify COLD_START sequencing and no second instruction authority;
- verify the reasoning policy's scope, proportionality and chain-of-thought boundary;
- inspect PD-002 and current active-WP discipline;
- treat all builder checks above as claims, not proof;
- preserve ADR/adversarial/owner gates.

A later separate adversarial review must attempt to show that the new policy creates ritualised overthinking, duplicate authority, hidden owner-decision transfer, prompt-only false assurance, or excessive cold-start burden.

## Completion state

**Material architecture work complete; fresh independent verification required.**

ADR-0001 remains proposed. WP-000 and Phase 0 remain unverified/unaccepted for the current target.
