#!/usr/bin/env python3
"""Deterministic producer model for the WP-014 pending-result control.

This models routing semantics only. It does not query GitHub, certify governance,
or replace exact artefact/PR inspection by an independent verifier.
"""

from dataclasses import dataclass


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


@dataclass(frozen=True)
class Containment:
    """Canonical stream-level recovery after repeated invalid head movement."""

    pr: int
    key: Key
    triggering_heads: tuple[str, str]
    repository: str = "batuhanozgun/soul"


INDEPENDENT = "INDEPENDENT"
INTEGRATOR_RESULT = "INTEGRATOR_RESULT"
INTEGRATOR_RESOLUTION = "INTEGRATOR_RESOLUTION"
INTEGRATOR_CONTAINMENT = "INTEGRATOR_CONTAINMENT"
INTEGRATOR_CONFLICT = "INTEGRATOR_CONFLICT"
BLOCKED_DISCOVERY = "BLOCKED_DISCOVERY"
BLOCKED_INVALID_RESOLUTION = "BLOCKED_INVALID_RESOLUTION"
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
    discovery_available=True,
):
    if not discovery_available:
        return BLOCKED_DISCOVERY

    same_wp = [candidate for candidate in candidates if candidate.key.wp == expected.wp]
    resolved = {
        (resolution.repository, resolution.pr, resolution.head)
        for resolution in resolutions
        if resolution.key == expected
    }
    contained = {
        (containment.repository, containment.pr)
        for containment in containments
        if containment.key == expected
    }

    # A resolution cannot lawfully hide a candidate that validates as current.
    if any(
        (candidate.repository, candidate.pr, candidate.head) in resolved
        and is_current(candidate, expected)
        for candidate in same_wp
    ):
        return BLOCKED_INVALID_RESOLUTION

    unresolved = [
        candidate
        for candidate in same_wp
        if (candidate.repository, candidate.pr, candidate.head) not in resolved
    ]
    current = [candidate for candidate in unresolved if is_current(candidate, expected)]
    invalid = [candidate for candidate in unresolved if not is_current(candidate, expected)]
    contained_invalid = [
        candidate
        for candidate in invalid
        if (candidate.repository, candidate.pr) in contained
    ]
    uncontained_invalid = [
        candidate
        for candidate in invalid
        if (candidate.repository, candidate.pr) not in contained
    ]

    if len(current) > 1:
        return INTEGRATOR_CONFLICT
    if uncontained_invalid:
        moved_after_resolution = any(
            resolution.key == expected
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
    if len(current) == 1:
        return INTEGRATOR_RESULT
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
        BLOCKED_INVALID_RESOLUTION,
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

    # Initial Step 1A sees no result; publication occurs during Steps 2/3; the
    # mandatory final re-check sees it and changes the route before commitment.
    expect("initial check before publication", classify(verifier, []), INDEPENDENT)
    expect("final re-check after publication", classify(verifier, [current]), INTEGRATOR_RESULT)


if __name__ == "__main__":
    main()
