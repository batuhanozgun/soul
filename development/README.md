# SOUL Development Operating System

This directory is the operating environment used to design SOUL before SOUL itself exists.

Its purpose is to make development independent from chat memory, session length, and a single model's self-assessment. A new session must be able to cold-start from repository state, perform one bounded responsibility, leave evidence, and hand off without requiring the previous conversation.

## Directory map

- `00_foundation/` — what SOUL is, what it must achieve, and what cannot be traded away.
- `01_governance/` — how work, decisions, verification, changes, sessions, and authority operate.
- `02_architecture/` — capability architecture, failure model, target architecture, and later core models.
- `03_plan/` — roadmap and current project state.
- `04_work/` — active and completed work-package specifications.
- `05_evidence/` — research and evidence used by decisions; evidence is not itself a decision.
- `06_reviews/` — independent verification and adversarial review artefacts.
- `07_sessions/` — append-only human-readable handoff records for completed work sessions.

`../system/` is deliberately separate. Development records, research, temporary reasoning, and process artefacts must not leak into the distributable product merely because they were useful while building it.

## Prime rule

Repository state is authoritative. Conversation history and model memory may help locate context, but they cannot silently override a recorded decision, work-package scope, acceptance criterion, or project state.
