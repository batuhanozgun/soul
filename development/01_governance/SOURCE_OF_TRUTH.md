# SOURCE OF TRUTH

This document defines authority when project artefacts disagree.

## Authority order

From highest to lowest:

1. `00_foundation/VISION.md`, `DEFINITION.md`, `NON_NEGOTIABLES.md`
2. Accepted architecture decision records (ADRs)
3. Accepted architecture specifications and models
4. Active work-package specification, including its acceptance criteria and required readings
5. `03_plan/STATE.md`
6. Verified evidence and independent review artefacts
7. Session handoff records
8. Pull-request discussion and issue discussion
9. Chat history, model memory, verbal recollection, and unrecorded reasoning

A lower layer may add context but may not silently override a higher layer.

## Procedure versus semantic authority

The hierarchy above decides **which project claim is authoritative when contents conflict**. It does not independently define fresh-session reading order.

Fresh-session sequencing has one designated procedural authority: `03_plan/COLD_START.md`. The active WP can require additional readings and can order material within the COLD_START step allocated to WP-required reading, but it cannot silently replace the bootstrap sequence itself. Session launch briefs, handoffs, indexes, and chat instructions are subordinate to that procedure.

This distinction prevents a high-authority WP from accidentally creating a second bootstrap protocol while preserving the WP's higher semantic authority over its own scope, acceptance criteria, and work definition.

## Conflict rule

When two authoritative artefacts at the same level conflict, the system must not choose whichever is convenient. The conflict becomes explicit work and is resolved through the decision process. Until resolved, affected downstream work is blocked or marked as conditional.

## Derived views

Dashboards, summaries, indexes, generated tables, status reports, and launch convenience views are views. They are not independent sources of truth unless explicitly designated as the authoritative home of a fact.

Each material fact should have one authoritative home. Other artefacts reference or derive from it.

The current phase, active work package, and current next responsibility have their authoritative home in `03_plan/STATE.md` together with the active WP it names. A derived view must either reproduce those values mechanically and declare itself subordinate, or avoid materialising the values at all.

## Conversation rule

A statement such as "we decided this in the previous chat" has no architectural authority unless the decision was recorded in the repository. A session may recover missing context from conversation history, but recovered content becomes authoritative only after it is reconciled with the repository and recorded through the normal change process.

## Evidence rule

Evidence supports a claim or decision; it does not automatically become a decision. Research, benchmark results, model opinions, external documentation, experiments, and code traces remain evidence until an authorised decision process interprets them.
