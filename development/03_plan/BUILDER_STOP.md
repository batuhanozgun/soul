# BUILDER STOP — PHASE 0

The Phase 0 builder session has reached its authority boundary.

It must not:

- perform WP-001 independent verification in the same conversation,
- mark WP-000 verified-complete,
- accept ADR-0000,
- merge PR #1,
- begin Phase 1.

The next legitimate execution unit is a fresh verifier session defined by `WP-001-PHASE0-VERIFICATION.md`.

This stop is not an unfinished shortcut. It is the independence gate required by the operating system being established.
