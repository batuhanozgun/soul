# ChatGPT Project Entry — derived convenience

This file is a **derived convenience artefact** for configuring the ChatGPT Project that hosts the main SOUL development conversation. It is not a source of project state, architecture truth, current work, or a second cold-start sequence.

The repository remains authoritative. If this file ever conflicts with `COLD_START.md`, `STATE.md`, the active WP, or governance, this file is stale and must be updated.

## Minimal Project Instructions text

Use the following as the SOUL ChatGPT Project instruction:

> Use GitHub repository `batuhanozgun/soul` as the authoritative project source. At the start of every new SOUL development chat, before substantive work, locate the current development line from repository/PR state rather than relying on Project memory, then read `development/03_plan/COLD_START.md` from that line and follow it exactly. Do not create or infer a second reading order in Project Instructions. Project memory and prior chats are non-authoritative continuity aids only. The repository determines current state, active work, role, reasoning policy, authority and completion gates. If the user says “Başlat”, perform this cold-start and continue the repository-defined next responsibility without asking the user to manually identify WP/file/branch names. Ask the human owner only when repository governance identifies a genuine owner/value/scope/high-impact decision.

## Why this stays minimal

The reasoning policy itself lives in `development/01_governance/REASONING_POLICY.md` and is loaded by `COLD_START.md`. Copying it into Project Instructions would create an independently drifting instruction surface and reproduce the duplicated-authority failure class already observed in Phase 0.

## Branch resolution during bootstrap

Project Instructions deliberately do not hard-code an active WP, current responsibility, or mutable branch SHA. If the default branch does not yet contain `development/03_plan/COLD_START.md`, inspect the repository's current open development PR metadata and use its head branch; do not guess from conversation memory. Once the development operating system is accepted into the default branch, this fallback becomes unnecessary without changing the instruction's semantic rule.
