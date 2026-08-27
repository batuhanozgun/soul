# PENDING RESULT CONTROL — [WP / PR / HEAD OR STREAM]

**Control mode:** exact-head resolution / moving-candidate containment
**Status:** proposed Integrator control / canonically integrated
**Integrator session:**
**Canonical development branch:**
**Canonical integration commit:**
**Candidate repository:**
**Candidate PR:**
**Immutable candidate head SHA:**

## Expected result-control key

- WP:
- role:
- exact target:
- attempt:

## Observed candidate claims

- WP:
- role:
- exact target:
- attempt:
- result state:
- changed files:

## Direct inspection evidence

Record the inspected artefact, handoff, PR metadata, immutable head and changed-file scope. PR title/body/labels are locators only.

## Classification

Choose one and justify it:

- stale target or attempt;
- malformed/incomplete publication;
- unauthorised changed-file scope;
- exact duplicate already preserved by a canonical conflict transition;
- other proven non-current condition.

`uninspectable` / `discovery unavailable` is not resolvable by exclusion and must remain blocked.

For moving-candidate containment, also record:

- the earlier canonically resolved invalid head;
- the later directly inspected invalid moved head;
- proof that both observations are the same repository + PR identity under the same active key;
- why another exact-head resolution would recreate the repeated-movement denial path.

Containment is not available for a first invalid head, a current-valid head, a
multiple-current-result conflict, global discovery failure, or an uninspectable
candidate without a directly inspected repeated-movement trigger.

## Non-suppression proof

Explain which current-result validation rule the candidate fails. If it validates against the complete expected key and evidence-only scope, stop: this template cannot exclude it. Multiple valid current results require conflict preservation plus a fresh canonical attempt.

## Control effect and boundary

### Exact-head resolution

This mode excludes only the exact tuple `(repository, PR number, candidate head
SHA)` from repeated pending-result blocking after this record is present on the
canonical development branch. It does not apply after candidate head movement.

### Moving-candidate containment

This mode is available only after one exact-head resolution and one later
directly inspected invalid head prove repeated movement for the same repository
+ PR identity under the same complete active key. Its identity is:

`(repository, PR number, active WP, role, exact target, attempt)`.

After canonical integration, every later observed head is still classified:

- a directly validating current head routes to Integrator and containment has
  no suppressive effect;
- multiple current heads remain a conflict;
- an inspectable invalid/stale/malformed later head is recorded as contained
  and does not require another canonical exact-head resolution;
- a later inaccessible/deleted head from the contained identity is recorded as
  contained rather than allowed to reset recovery; if it later becomes
  inspectable and validates, it routes normally;
- repository-wide discovery failure remains fail-closed and cannot be covered
  by candidate containment.

Containment does not reinterpret or accept a result, change the active key,
authorise verifier/reviewer self-transition, or apply after a canonical key
change. The Integrator owns creation/correction of the canonical record; the
candidate author cannot reset it by changing PR state, branch state or head.

## Recovery / reopen condition

For exact-head resolution, state how work resumes and how movement reopens
inspection. For containment, state how later heads remain directly eligible for
current-result validation, how a canonical key change ends the containment
scope, and how proof that the triggering classification was wrong is corrected.

## Next responsibility

Name the exact canonical responsibility that remains after this bounded resolution.
