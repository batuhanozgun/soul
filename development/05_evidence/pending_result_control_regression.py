#!/usr/bin/env python3
"""Deterministic producer model for the WP-017 pending-result control.

This models routing semantics only. It does not query GitHub, certify governance,
or replace exact artefact/PR inspection by an independent verifier.
"""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Key:
    wp: str
    role: str
    target: str
    attempt: int


@dataclass(frozen=True)
class Candidate:
    pr: int
    head: str
    key: Key
    repository: str = "batuhanozgun/soul"
    complete: bool = True
    evidence_only: bool = True
    inspectable: bool = True
    state: str = "open"


@dataclass(frozen=True)
class Resolution:
    pr: int
    head: str
    key: Key
    repository: str = "batuhanozgun/soul"
    canonical: bool = True
    integrator_owned: bool = True
    proven_invalid: bool = True


@dataclass(frozen=True)
class Containment:
    """Canonical stream-level recovery after repeated invalid head movement."""

    pr: int
    key: Key
    triggering_heads: tuple[str, str]
    repository: str = "batuhanozgun/soul"
    canonical: bool = True
    integrator_owned: bool = True
    proven_invalid: bool = True


@dataclass(frozen=True)
class CandidateSetContainment:
    """Repository/key recovery after invalid claims rotate PR identities."""

    key: Key
    triggering_candidates: tuple[tuple[int, str], tuple[int, str]]
    repository: str = "batuhanozgun/soul"
    canonical: bool = True
    integrator_owned: bool = True
    proven_invalid: bool = True


INDEPENDENT = "INDEPENDENT"
INTEGRATOR_RESULT = "INTEGRATOR_RESULT"
INTEGRATOR_RESOLUTION = "INTEGRATOR_RESOLUTION"
INTEGRATOR_CONTAINMENT = "INTEGRATOR_CONTAINMENT"
INTEGRATOR_CANDIDATE_SET_CONTAINMENT = "INTEGRATOR_CANDIDATE_SET_CONTAINMENT"
INTEGRATOR_CONFLICT = "INTEGRATOR_CONFLICT"
BLOCKED_DISCOVERY = "BLOCKED_DISCOVERY"
BLOCKED_INSPECTION = "BLOCKED_INSPECTION"
INDEPENDENT_CONTAINED = "INDEPENDENT_CONTAINED"


def is_current(candidate: Candidate, expected: Key) -> bool:
    return (
        candidate.inspectable
        and candidate.complete
        and candidate.evidence_only
        and candidate.key == expected
    )


def classify(
    expected,
    candidates,
    resolutions=(),
    containments=(),
    candidate_set_containments=(),
    discovery_available=True,
    repository="batuhanozgun/soul",
):
    if not discovery_available:
        return BLOCKED_DISCOVERY

    same_wp = [
        candidate
        for candidate in candidates
        if candidate.repository == repository and candidate.key.wp == expected.wp
    ]
    resolved = {
        (resolution.repository, resolution.pr, resolution.head)
        for resolution in resolutions
        if resolution.key == expected
        and resolution.canonical
        and resolution.integrator_owned
        and resolution.proven_invalid
    }
    contained = {
        (containment.repository, containment.pr)
        for containment in containments
        if containment.key == expected
        and containment.canonical
        and containment.integrator_owned
        and containment.proven_invalid
        and containment.triggering_heads[0] != containment.triggering_heads[1]
    }
    contained_sets = {
        containment.repository
        for containment in candidate_set_containments
        if containment.key == expected
        and containment.canonical
        and containment.integrator_owned
        and containment.proven_invalid
        and containment.triggering_candidates[0][0]
        != containment.triggering_candidates[1][0]
    }

    # Direct validity is evaluated before any recovery control or invalid
    # residue. A control can classify invalid evidence; it cannot hide a result.
    current = [candidate for candidate in same_wp if is_current(candidate, expected)]
    invalid = [candidate for candidate in same_wp if not is_current(candidate, expected)]
    contained_invalid = [
        candidate
        for candidate in invalid
        if (candidate.repository, candidate.pr) in contained
        or candidate.repository in contained_sets
    ]
    uncontained_invalid = [
        candidate
        for candidate in invalid
        if (candidate.repository, candidate.pr, candidate.head) not in resolved
        and (candidate.repository, candidate.pr) not in contained
        and candidate.repository not in contained_sets
    ]

    # Deliberate red-capable mutation used only by the producer mutation run.
    if (
        os.environ.get("WP017_MUTATE_INVALID_FIRST") == "1"
        and len(current) == 1
        and uncontained_invalid
    ):
        return INTEGRATOR_RESOLUTION

    if len(current) > 1:
        return INTEGRATOR_CONFLICT
    if len(current) == 1:
        return INTEGRATOR_RESULT
    if any(not candidate.inspectable for candidate in uncontained_invalid):
        return BLOCKED_INSPECTION
    if uncontained_invalid:
        prior_invalid_prs = {
            (resolution.repository, resolution.pr)
            for resolution in resolutions
            if resolution.key == expected
            and resolution.canonical
            and resolution.integrator_owned
            and resolution.proven_invalid
        } | {
            (containment.repository, containment.pr)
            for containment in containments
            if containment.key == expected
            and containment.canonical
            and containment.integrator_owned
            and containment.proven_invalid
        }
        fresh_identity_after_control = any(
            candidate.repository == repository and candidate.pr != prior_pr
            for candidate in uncontained_invalid
            for repository, prior_pr in prior_invalid_prs
        )
        if fresh_identity_after_control:
            return INTEGRATOR_CANDIDATE_SET_CONTAINMENT
        moved_after_resolution = any(
            resolution.key == expected
            and resolution.canonical
            and resolution.integrator_owned
            and resolution.proven_invalid
            and any(
                candidate.repository == resolution.repository
                and candidate.pr == resolution.pr
                and candidate.head != resolution.head
                for candidate in uncontained_invalid
            )
            for resolution in resolutions
        )
        if moved_after_resolution:
            return INTEGRATOR_CONTAINMENT
        return INTEGRATOR_RESOLUTION
    if contained_invalid:
        return INDEPENDENT_CONTAINED
    return INDEPENDENT


def expect(name, actual, wanted):
    if actual != wanted:
        raise AssertionError(f"{name}: expected {wanted}, got {actual}")
    print(f"PASS {name}: {actual}")


def main():
    target = "new-target"
    verifier = Key("WP-012", "verifier", target, 1)
    reviewer = Key("WP-013", "adversarial-reviewer", target, 1)

    pr14_shape = Candidate(14, "814e588", verifier)
    pr15_shape = Candidate(15, "51fcdd0", reviewer)
    expect("PR14 post-result interval", classify(verifier, [pr14_shape]), INTEGRATOR_RESULT)
    expect("PR15 post-result interval", classify(reviewer, [pr15_shape]), INTEGRATOR_RESULT)

    stale = Candidate(20, "old-head", Key("WP-012", "verifier", "old-target", 1))
    expect("unresolved stale head", classify(verifier, [stale]), INTEGRATOR_RESOLUTION)
    expect(
        "canonically resolved exact stale head",
        classify(verifier, [stale], [Resolution(20, "old-head", verifier)]),
        INDEPENDENT,
    )

    moved = Candidate(20, "new-head", stale.key)
    expect(
        "head movement reopens inspection",
        classify(verifier, [moved], [Resolution(20, "old-head", verifier)]),
        INTEGRATOR_CONTAINMENT,
    )

    moving_containment = Containment(20, verifier, ("old-head", "new-head"))
    expect(
        "contained third invalid generation",
        classify(
            verifier,
            [Candidate(20, "third-head", stale.key)],
            [Resolution(20, "old-head", verifier)],
            [moving_containment],
        ),
        INDEPENDENT_CONTAINED,
    )
    for generation in range(4, 13):
        expect(
            f"contained invalid generation {generation}",
            classify(
                verifier,
                [Candidate(20, f"head-{generation}", stale.key)],
                [Resolution(20, "old-head", verifier)],
                [moving_containment],
            ),
            INDEPENDENT_CONTAINED,
        )

    later_valid = Candidate(20, "corrected-valid", verifier)
    expect(
        "contained stream later valid head",
        classify(
            verifier,
            [later_valid],
            [Resolution(20, "old-head", verifier)],
            [moving_containment],
        ),
        INTEGRATOR_RESULT,
    )

    contained_inaccessible = Candidate(
        20,
        "deleted-fork-head",
        stale.key,
        inspectable=False,
        state="closed",
    )
    expect(
        "contained inaccessible closed candidate",
        classify(
            verifier,
            [contained_inaccessible],
            [Resolution(20, "old-head", verifier)],
            [moving_containment],
        ),
        INDEPENDENT_CONTAINED,
    )

    malformed = Candidate(21, "bad", verifier, complete=False)
    expect("malformed candidate", classify(verifier, [malformed]), INTEGRATOR_RESOLUTION)
    expect(
        "resolved exact malformed head",
        classify(verifier, [malformed], [Resolution(21, "bad", verifier)]),
        INDEPENDENT,
    )

    current = Candidate(22, "valid", verifier)
    expect(
        "resolution cannot suppress valid current result",
        classify(verifier, [current], [Resolution(22, "valid", verifier)]),
        INTEGRATOR_RESULT,
    )

    forged_containment = Containment(22, verifier, ("bad-1", "bad-2"))
    expect(
        "containment cannot suppress valid current result",
        classify(verifier, [current], containments=[forged_containment]),
        INTEGRATOR_RESULT,
    )

    second = Candidate(23, "valid-2", verifier)
    expect(
        "multiple valid results preserved as conflict",
        classify(verifier, [current, second]),
        INTEGRATOR_CONFLICT,
    )

    unrelated = Candidate(24, "other", Key("WP-099", "verifier", target, 1))
    expect("another-WP history", classify(verifier, [unrelated]), INDEPENDENT)
    expect(
        "discovery unavailable",
        classify(verifier, [], discovery_available=False),
        BLOCKED_DISCOVERY,
    )

    wrong_attempt_containment = Containment(
        20,
        Key("WP-012", "verifier", target, 2),
        ("old-head", "new-head"),
    )
    expect(
        "wrong-key containment cannot unblock",
        classify(
            verifier,
            [Candidate(20, "third-head", stale.key)],
            [Resolution(20, "old-head", verifier)],
            [wrong_attempt_containment],
        ),
        INTEGRATOR_CONTAINMENT,
    )

    wrong_repository_containment = Containment(
        20,
        verifier,
        ("old-head", "new-head"),
        repository="attacker/fork",
    )
    expect(
        "wrong-repository containment cannot unblock",
        classify(
            verifier,
            [Candidate(20, "third-head", stale.key)],
            [Resolution(20, "old-head", verifier)],
            [wrong_repository_containment],
        ),
        INTEGRATOR_CONTAINMENT,
    )

    first_invalid = Candidate(30, "first-invalid", stale.key)
    expect(
        "valid plus first invalid routes current result",
        classify(verifier, [current, first_invalid]),
        INTEGRATOR_RESULT,
    )
    expect(
        "valid plus moved invalid routes current result",
        classify(
            verifier,
            [current, moved],
            [Resolution(20, "old-head", verifier)],
        ),
        INTEGRATOR_RESULT,
    )
    expect(
        "valid plus multiple fresh invalid routes current result",
        classify(
            verifier,
            [current, first_invalid, Candidate(31, "second-invalid", stale.key)],
        ),
        INTEGRATOR_RESULT,
    )
    expect(
        "multiple valid plus invalid remains conflict",
        classify(verifier, [current, second, first_invalid]),
        INTEGRATOR_CONFLICT,
    )
    expect(
        "valid plus inaccessible invalid routes current result",
        classify(
            verifier,
            [current, Candidate(32, "inaccessible", stale.key, inspectable=False)],
        ),
        INTEGRATOR_RESULT,
    )
    expect(
        "uncontained inaccessible candidate fails closed",
        classify(
            verifier,
            [Candidate(32, "inaccessible", stale.key, inspectable=False)],
        ),
        BLOCKED_INSPECTION,
    )

    first_identity_resolution = Resolution(40, "pr40-invalid", verifier)
    fresh_identity = Candidate(41, "pr41-invalid", stale.key)
    expect(
        "second invalid PR identity escalates candidate set",
        classify(verifier, [fresh_identity], [first_identity_resolution]),
        INTEGRATOR_CANDIDATE_SET_CONTAINMENT,
    )
    set_containment = CandidateSetContainment(
        verifier,
        ((40, "pr40-invalid"), (41, "pr41-invalid")),
    )
    for pr in range(42, 62):
        expect(
            f"fresh invalid PR {pr} cannot reset candidate set",
            classify(
                verifier,
                [Candidate(pr, f"pr{pr}-invalid", stale.key)],
                [first_identity_resolution],
                candidate_set_containments=[set_containment],
            ),
            INDEPENDENT_CONTAINED,
        )

    set_valid = Candidate(62, "set-valid", verifier)
    expect(
        "candidate set later valid routes result",
        classify(
            verifier,
            [set_valid, Candidate(63, "set-invalid", stale.key)],
            candidate_set_containments=[set_containment],
        ),
        INTEGRATOR_RESULT,
    )
    expect(
        "candidate set multiple valid remains conflict",
        classify(
            verifier,
            [set_valid, Candidate(64, "set-valid-2", verifier), first_invalid],
            candidate_set_containments=[set_containment],
        ),
        INTEGRATOR_CONFLICT,
    )
    expect(
        "candidate set inaccessible residue is contained non-valid",
        classify(
            verifier,
            [Candidate(65, "set-inaccessible", stale.key, inspectable=False)],
            candidate_set_containments=[set_containment],
        ),
        INDEPENDENT_CONTAINED,
    )

    wrong_attempt_set = CandidateSetContainment(
        Key("WP-012", "verifier", target, 2),
        ((40, "pr40-invalid"), (41, "pr41-invalid")),
    )
    expect(
        "wrong-key candidate set cannot unblock",
        classify(
            verifier,
            [fresh_identity],
            [first_identity_resolution],
            candidate_set_containments=[wrong_attempt_set],
        ),
        INTEGRATOR_CANDIDATE_SET_CONTAINMENT,
    )
    wrong_repository_set = CandidateSetContainment(
        verifier,
        ((40, "pr40-invalid"), (41, "pr41-invalid")),
        repository="attacker/fork",
    )
    expect(
        "wrong-repository candidate set cannot unblock",
        classify(
            verifier,
            [fresh_identity],
            [first_identity_resolution],
            candidate_set_containments=[wrong_repository_set],
        ),
        INTEGRATOR_CANDIDATE_SET_CONTAINMENT,
    )
    local_set = CandidateSetContainment(
        verifier,
        ((40, "pr40-invalid"), (41, "pr41-invalid")),
        canonical=False,
    )
    expect(
        "local candidate set cannot unblock",
        classify(
            verifier,
            [fresh_identity],
            [first_identity_resolution],
            candidate_set_containments=[local_set],
        ),
        INTEGRATOR_CANDIDATE_SET_CONTAINMENT,
    )
    candidate_authored_set = CandidateSetContainment(
        verifier,
        ((40, "pr40-invalid"), (41, "pr41-invalid")),
        integrator_owned=False,
    )
    expect(
        "candidate-authored set cannot unblock",
        classify(
            verifier,
            [fresh_identity],
            [first_identity_resolution],
            candidate_set_containments=[candidate_authored_set],
        ),
        INTEGRATOR_CANDIDATE_SET_CONTAINMENT,
    )
    unproven_resolution = Resolution(
        40,
        "pr40-invalid",
        verifier,
        proven_invalid=False,
    )
    expect(
        "unproven prior control cannot escalate candidate set",
        classify(verifier, [fresh_identity], [unproven_resolution]),
        INTEGRATOR_RESOLUTION,
    )
    unproven_set = CandidateSetContainment(
        verifier,
        ((40, "pr40-invalid"), (41, "pr41-invalid")),
        proven_invalid=False,
    )
    expect(
        "unproven candidate set cannot unblock",
        classify(
            verifier,
            [Candidate(42, "pr42-invalid", stale.key)],
            candidate_set_containments=[unproven_set],
        ),
        INTEGRATOR_RESOLUTION,
    )
    same_pr_trigger = CandidateSetContainment(
        verifier,
        ((40, "old"), (40, "new")),
    )
    expect(
        "same-PR trigger cannot create candidate set",
        classify(
            verifier,
            [fresh_identity],
            [first_identity_resolution],
            candidate_set_containments=[same_pr_trigger],
        ),
        INTEGRATOR_CANDIDATE_SET_CONTAINMENT,
    )
    next_attempt = Key("WP-012", "verifier", target, 2)
    expect(
        "candidate set does not carry to next attempt",
        classify(
            next_attempt,
            [Candidate(66, "attempt-two-invalid", verifier)],
            candidate_set_containments=[set_containment],
        ),
        INTEGRATOR_RESOLUTION,
    )
    foreign_current = Candidate(
        67,
        "foreign-current",
        verifier,
        repository="attacker/fork",
    )
    expect(
        "foreign repository current claim is outside candidate set",
        classify(verifier, [foreign_current]),
        INDEPENDENT,
    )

    # Initial Step 1A sees no result; publication occurs during Steps 2/3; the
    # mandatory final re-check sees it and changes the route before commitment.
    expect("initial check before publication", classify(verifier, []), INDEPENDENT)
    expect("final re-check after publication", classify(verifier, [current]), INTEGRATOR_RESULT)


if __name__ == "__main__":
    main()
