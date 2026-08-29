# DECISION POLICY

Architecture must not emerge accidentally from implementation details or chat momentum.

## Decision classes

### A. Foundation decision
Changes the vision, definition, or a non-negotiable property.

Requires:
- explicit ADR,
- impact analysis against existing architecture and success criteria,
- independent verification of the claimed need,
- human-owner approval.

### B. Architecture decision
Changes core concepts, system boundaries, authority, state, evidence, verification, runtime behaviour, extensibility, or another cross-cutting property.

Requires an ADR and independent review before acceptance.

### C. Work-package design decision
Affects only the active WP and does not alter higher-level architecture. It may be recorded in the WP if the decision, rationale, and consequences are explicit.

### D. Local implementation decision
Reversible choice within an already accepted design that does not change public contracts, authority, acceptance criteria, state semantics, evidence obligations, or architecture. It may remain in implementation artefacts and commit history.

If uncertain between classes, choose the higher-impact class until the scope is established.

## ADR minimum schema

Every ADR must contain:

- ID and status: proposed / accepted / superseded / rejected,
- problem,
- decision scope,
- constraints,
- options considered,
- evidence used,
- decision,
- rationale,
- consequences and new risks,
- rejected alternatives and why,
- verification required,
- what new evidence or condition would justify reopening the decision,
- supersedes / superseded-by links when applicable.

## Research is not decision

Evidence may show that an approach is common, recommended, performant, safe, or well supported. That does not automatically make it correct for SOUL. The decision process must connect the evidence to SOUL's own requirements and constraints.

## No invisible defaults

When a choice materially affects architecture, leaving it unspecified is itself a decision risk. The system must either make and record the decision, or mark the question unresolved and block dependent commitments as necessary.

## Decision ownership

Technical complexity alone does not make a question a human-owner decision. Researchable and derivable technical choices belong to the responsible system role. Human approval is used for foundation changes, declared owner value choices, and defined high-impact boundaries.
