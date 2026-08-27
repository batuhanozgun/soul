# PENDING RESULT CONTROL — [WP / PR / HEAD OR STREAM]

**Control mode:** exact-head resolution / moving-candidate containment / candidate-set containment
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

For candidate-set containment, also record:

- the earlier canonical exact-head resolution or moving-candidate containment;
- the later distinct PR identity and directly inspected immutable invalid head;
- proof that both candidate identities belong to the exact canonical repository
  and unchanged complete active key;
- why another PR-scoped control would recreate the fresh-identity denial path.

Containment is not available for a first invalid head, a current-valid head, a
multiple-current-result conflict, global discovery failure, or an uninspectable
candidate without the applicable directly inspected repeated-movement or
fresh-identity trigger.

## Non-suppression proof

Explain which current-result validation rule the candidate fails. If it validates against the complete expected key and evidence-only scope, stop: this template cannot exclude it. Multiple valid current results require conflict preservation plus a fresh canonical attempt.

Record the complete discovered candidate set and demonstrate that direct
current-result validation was evaluated before invalid-residue routing. Exactly
one current-valid result routes to Integrator even when uncontained invalid
residue coexists.

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

### Candidate-set containment

This mode is available only after an earlier canonical invalid-candidate
control and a later directly inspected invalid candidate at a distinct PR
identity prove identity rotation in the same exact canonical repository under
one unchanged complete active key. Its identity is:

`(canonical repository, active WP, role, exact target, attempt)`.

After canonical integration, every later same-WP candidate in that repository
is still classified head by head:

- exactly one directly validating current head routes to Integrator before any
  invalid residue;
- multiple current heads remain a conflict;
- inspectable invalid/stale/malformed heads at any PR identity are recorded as
  contained and cannot demand another canonical resolution;
- candidate-specific inaccessible heads are contained non-valid, never absent
  or valid, and later inspectability reopens direct validation;
- repository-wide discovery failure remains fail-closed and cannot be covered.

The control does not cross a repository or complete-key boundary. Mutable
repository names, fork/source identity, URL spellings, remotes, branch names and
candidate-authored metadata cannot widen or reset it. Only a separate
Integrator can create or correct the canonical record.

## Recovery / reopen condition

For exact-head resolution, state how work resumes and how movement reopens
inspection. For either containment mode, state how later heads remain directly
eligible for current-result validation, how the PR/repository and canonical-key
boundaries end the control scope, and how proof that the triggering
classification was wrong is corrected.

## Next responsibility

Name the exact canonical responsibility that remains after this bounded resolution.
