# SESSION-0039 — Phase 0 WP-021 Pre-Build Adversarial Reviewer

**Date:** 2026-08-29  
**WP:** WP-022 — WP-021 Development Lifecycle Pre-Build Adversarial Review  
**Role:** fresh separate adversarial reviewer  
**Primary responsibility:** independently attack exact frozen WP-021 design
target; publish review + handoff only; do not repair or implement  
**Reviewed repository:** `batuhanozgun/soul`  
**Reviewed PR:** `#28`  
**Exact design target:** `acf6ddc621c644e5a0960e3382b25928d2518041`  
**Exact design base:** `6fca29474ab97d22e363108b8be6438456316e01`  
**Result-control key:** `WP-022 / adversarial reviewer / acf6ddc621c644e5a0960e3382b25928d2518041 / attempt 1`

## Cold-start and independence

The session cold-started from live `origin/phase0/development-os` rather than the
stale/dirty local checkout. The original checkout and its user changes were left
untouched; review work used a clean isolated worktree and branch
`codex/wp022-prebuild-adversarial-review` based on canonical commit `68af9c9...`.

The expected attack matrix was persisted in commit `38e5ee8` before the exact
design or producer rationale was read. The first-pass lifecycle/ADR attack was
persisted in commit `a5f7836` before producer function analysis, replay protocol
or SESSION-0037 was read.

## Inputs read

Canonical state and common governance:

- `development/03_plan/STATE.md`;
- active WP-022;
- `SOURCE_OF_TRUTH.md`, `WORKING_PROTOCOL.md`, `REASONING_POLICY.md`;
- `ROLE_MODEL.md`, `DECISION_POLICY.md`, `CHANGE_POLICY.md`,
  `VERIFICATION_POLICY.md`;
- `COLD_START.md`, `PR_GATE.md`, `PHASE_GATE.md`;
- all four foundation files and `ROADMAP.md`;
- WP-000, parent WP-021, blocked WP-020 and exact historical F-AR-005 through
  F-AR-008 evidence needed to test the lineage/preservation claims;
- adversarial review template.

Exact target and live metadata:

- live GitHub PR #28 metadata: open/draft, base branch
  `phase0/development-os`, base `6fca294...`, head
  `work/wp021-development-lifecycle-improvement` at `acf6ddc...`, one commit,
  five changed files, 1,200 additions, zero deletions;
- direct Git diff/base/head/tree scope for the exact five files;
- proposed `DEVELOPMENT_LIFECYCLE.md` and ADR-0003 at exact target;
- producer function/role/motivation analysis, historical blind-replay protocol
  and SESSION-0037, read only after the attack model and first pass were frozen.

## Output produced

- `development/06_reviews/PREBUILD-ADVERSARIAL-REVIEW-WP-021-acf6ddc6-2026-08-29.md`;
- this SESSION-0039 handoff.

No target/design/governance/WP/state/ADR repair or acceptance change was made.

## Review result

**Overall judgement:** **Requires design revision**.

Surviving findings:

1. **F-AR-009 — Technical design acceptance and material finding disposition
   are circular or unowned** — medium/material, stands.
2. **F-AR-010 — The replay bundles multiple changes and cannot establish that a
   permanent Planner is necessary** — medium/material, stands.
3. **F-AR-011 — Context-selection metadata can hide required evidence without
   detection** — medium/material, stands.
4. **F-AR-012 — Rollback is claimed as mitigation but has no design contract** —
   medium/material, stands.

The review also recorded bounded/disproved attacks and limitations. In
particular, exact-scope preservation, proposal-only status, Integrator
non-reinterpretation, rejection of consensus-as-independence and explicit limits
on historical replay generalisation survived the performed attack.

## Evidence and verification status

- Exact target/base/five-file scope: directly inspected and live-validated at
  review start; must be live-validated again immediately before publication.
- Semantic review: bound only to `acf6ddc...`; any material target change is a
  new target.
- Replay execution: not performed by this reviewer and remains a separate WP-021
  gate.
- Operational implementation: not begun and not authorised.
- ADR-0003: proposed, not accepted.
- WP-020/F-AR-008: blocked/unresolved and unchanged.

## Unresolved items

- A separate design/synthesis responsibility must resolve or explicitly route
  F-AR-009 through F-AR-012 without weakening WP-021 criteria.
- Any changed lifecycle/ADR/replay target must preserve exact history and receive
  the independent challenge required by current governance.
- Historical replay remains separately required, but its design must be capable
  of testing the permanent Planner hypothesis rather than only the bundled
  lifecycle package.

## Exact next responsibility

After this two-file evidence branch is published, stop for a **separate
Integrator**. The Integrator must validate exact target/freshness and exact
two-file evidence scope, preserve **Requires design revision** and F-AR-009
through F-AR-012 without reinterpretation, integrate evidence only, and route
WP-021 back to authorised design/synthesis.

The Integrator must not treat evidence integration as design/ADR/PR/Phase
acceptance. This reviewer does not repair the design, execute replay synthesis,
implement governance, accept ADR-0003, merge PR #28/#22/#1, execute WP-020,
accept Phase 0 or begin Phase 1.
