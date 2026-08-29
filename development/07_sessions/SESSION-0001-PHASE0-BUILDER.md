# SESSION-0001 — Phase 0 builder

**Date:** 2026-08-25  
**Work package:** WP-000 — SOUL Development Operating System  
**Role:** designer/builder  
**Branch / PR:** `phase0/development-os` / PR #1

## Required inputs read

This builder session used the agreed SOUL objective, the three-part KEEL/production-agent analysis, and the existing `batuhanozgun/keel` architecture review as prior evidence. Repository bootstrap began from an empty `batuhanozgun/soul` repository.

The canonical result of that prior context has been written into the Phase 0 repository artefacts; future sessions are not required to replay this chat in order to continue.

## Responsibility for this session

Create the first version of the repository-based development operating system that can carry SOUL design across fresh sessions without depending on chat memory or builder self-certification.

## Work performed

- bootstrapped the repository and opened `phase0/development-os`,
- defined foundation vision, boundaries, success criteria and non-negotiables,
- defined source-of-truth, cold-start/handoff, role, decision, verification and change policies,
- created reusable ADR, WP, evidence, verification, adversarial-review and session templates,
- created phased roadmap, phase/PR gates, workspace index and live project state,
- separated `development/` from the future reusable `system/` product,
- created proposed ADR-0000 documenting the development-governance bootstrap decision,
- created WP-000 and draft PR #1,
- created WP-001 and the fresh-verifier launch brief,
- corrected a builder-created duplicate-state defect by restoring `STATE.md` as the single current-state home and deleting temporary state files.

## Outputs produced

The current PR #1 change set is the authoritative builder output. Canonical entry points:

- `development/00_foundation/`
- `development/01_governance/`
- `development/02_architecture/decisions/ADR-0000-DEVELOPMENT-GOVERNANCE-BOOTSTRAP.md`
- `development/03_plan/STATE.md`
- `development/03_plan/COLD_START.md`
- `development/03_plan/ROADMAP.md`
- `development/04_work/WP-000-DEVELOPMENT-OS.md`
- `development/04_work/WP-001-PHASE0-VERIFICATION.md`
- `development/06_reviews/`
- `system/README.md`

## Decisions

No ADR was accepted in this builder session. ADR-0000 remains **proposed**. The foundation and governance content on the branch is proposed project truth pending the WP-000 verification/review gate.

## Evidence used or produced

The builder's conceptual inputs include the prior KEEL repository analysis and production agent architecture comparison. No external research evidence artefact was created in this session because WP-000 acceptance is about repository-operating discipline, not a claim that a specific external framework is authoritative.

## Verification status

**NOT INDEPENDENTLY VERIFIED.**

This session produced the artefacts and therefore cannot certify them under `VERIFICATION_POLICY.md`.

## Unresolved items

- WP-000 acceptance criteria have not yet been independently checked against the exact live PR head.
- Adversarial review has not yet been performed.
- Any finding that causes a material repair will invalidate earlier verification and require re-verification of the new commit.
- ADR-0000 has not been accepted by the human owner.

## Next required responsibility

**Verifier, fresh session:** follow `development/03_plan/COLD_START.md` and `development/04_work/WP-001-PHASE0-VERIFICATION.md`. Read the verification policy and derive expected results before this builder handoff. Inspect the exact live PR #1 head and write the verification artefact under `development/06_reviews/`. Do not repair findings in the verifier session.
