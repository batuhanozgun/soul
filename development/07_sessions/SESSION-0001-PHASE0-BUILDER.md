# SESSION-0001 — Phase 0 builder

**Date:** 2026-08-25  
**Work package:** WP-000 — SOUL Development Operating System  
**Role:** designer/builder  
**Branch / PR:** `phase0/development-os` / PR #1

## Required inputs read

This builder session used the current conversation's agreed SOUL objective, the three-part KEEL/production-agent analysis, and the existing `batuhanozgun/keel` architecture review as prior evidence. Repository bootstrap began from an empty `batuhanozgun/soul` repository.

The canonical result of that prior context has been written into the Phase 0 repository artefacts; future sessions are not required to replay this chat in order to continue.

## Responsibility for this session

Create the first version of the repository-based development operating system that can carry SOUL design across fresh sessions without depending on chat memory or builder self-certification.

## Work performed

- bootstrapped the repository and opened `phase0/development-os`,
- defined foundation vision, boundaries, success criteria and non-negotiables,
- defined source-of-truth, cold-start/handoff, role, decision, verification and change policies,
- created reusable ADR, WP, evidence, verification, adversarial-review and session templates,
- created the phased development roadmap and live project state,
- separated `development/` from the future reusable `system/` product,
- created WP-000 and opened draft PR #1.

## Outputs produced

See the 23-file change set in PR #1. Canonical entry points:

- `development/00_foundation/`
- `development/01_governance/`
- `development/03_plan/ROADMAP.md`
- `development/03_plan/STATE.md`
- `development/04_work/WP-000-DEVELOPMENT-OS.md`
- `system/README.md`

## Decisions

No ADR was accepted in this builder session. The foundation and governance content on the branch is proposed project truth pending the WP-000 verification/review gate.

The bootstrap decision to use repository state as authoritative and fresh sessions as the unit of independent work is encoded in the proposed Phase 0 documents and must be independently verified before merge.

## Evidence used or produced

The builder's conceptual inputs include the prior KEEL repository analysis and production agent architecture comparison. No external research evidence artefact was created in this session because WP-000 acceptance is about repository-operating discipline, not a claim that a specific external framework is authoritative.

## Verification status

**NOT INDEPENDENTLY VERIFIED.**

This session produced the artefacts and therefore cannot certify them under `VERIFICATION_POLICY.md`.

## Unresolved items

- WP-000 acceptance criteria have not yet been independently checked against the exact PR head.
- Adversarial review has not yet been performed.
- Any finding that causes a material repair will invalidate earlier verification and require re-verification of the new commit.

## Next required responsibility

**Verifier, fresh session:** open PR #1, cold-read `development/01_governance/VERIFICATION_POLICY.md` and WP-000 before reading this builder handoff, derive the expected result from WP-000, inspect the exact PR head, and write the verification artefact under `development/06_reviews/`. Do not repair findings in the verifier session.
