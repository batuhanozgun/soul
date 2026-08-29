# ADVERSARIAL REVIEW — <WP / ARTEFACT>

**Reviewer session:** SESSION-XXXX  
**Reviewed commit/artefact:** <exact ref>  
**Authoritative specification:** <WP / ADR / architecture refs>  
**Date:** YYYY-MM-DD

## Attack surface considered

List the relevant areas rather than using a fixed finding quota. Typical areas include hidden assumptions, authority leaks, self-modification, state drift, stale context, provenance gaps, circular verification, false completion, tool misuse, privilege escalation, silent failure, recovery dead ends, and agent-to-agent error propagation.

## Findings

For each finding:

### <Finding title>

- **Claim:** what is wrong or vulnerable?
- **Evidence:** exact artefact/line/trace/test supporting the claim.
- **Failure path:** how the defect can produce an incorrect or uncontrolled state.
- **Impact:** what property is lost.
- **Severity:** high | medium | low, with rationale.
- **Disproof attempt:** what was checked that could have invalidated this finding?
- **Result:** stands | disproved | not-verifiable.

## No-finding statement

If no findings survive review, state that explicitly. Do not invent issues to make the review look substantive.

## Overall judgement

State whether the artefact is suitable to proceed to integration, requires repair, or cannot yet be assessed.
