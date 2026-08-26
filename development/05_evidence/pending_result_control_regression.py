#!/usr/bin/env python3
"""Deterministic producer model for the WP-011 pending-result control.

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
    complete: bool = True
    evidence_only: bool = True
    inspectable: bool = True


@dataclass(frozen=True)
class Resolution:
    pr: int
    head: str


INDEPENDENT = "INDEPENDENT"
INTEGRATOR_RESULT = "INTEGRATOR_RESULT"
INTEGRATOR_RESOLUTION = "INTEGRATOR_RESOLUTION"
INTEGRATOR_CONFLICT = "INTEGRATOR_CONFLICT"
BLOCKED_DISCOVERY = "BLOCKED_DISCOVERY"
BLOCKED_INVALID_RESOLUTION = "BLOCKED_INVALID_RESOLUTION"


def is_current(candidate: Candidate, expected: Key) -> bool:
    return (
        candidate.inspectable
        and candidate.complete
        and candidate.evidence_only
        and candidate.key == expected
    )


def classify(expected, candidates, resolutions=(), discovery_available=True):
    if not discovery_available:
        return BLOCKED_DISCOVERY

    same_wp = [candidate for candidate in candidates if candidate.key.wp == expected.wp]
    resolved = {(resolution.pr, resolution.head) for resolution in resolutions}

    # A resolution cannot lawfully hide a candidate that validates as current.
    if any(
        (candidate.pr, candidate.head) in resolved and is_current(candidate, expected)
        for candidate in same_wp
    ):
        return BLOCKED_INVALID_RESOLUTION

    unresolved = [
        candidate
        for candidate in same_wp
        if (candidate.pr, candidate.head) not in resolved
    ]
    current = [candidate for candidate in unresolved if is_current(candidate, expected)]
    invalid = [candidate for candidate in unresolved if not is_current(candidate, expected)]

    if len(current) > 1:
        return INTEGRATOR_CONFLICT
    if invalid:
        return INTEGRATOR_RESOLUTION
    if len(current) == 1:
        return INTEGRATOR_RESULT
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
        classify(verifier, [stale], [Resolution(20, "old-head")]),
        INDEPENDENT,
    )

    moved = Candidate(20, "new-head", stale.key)
    expect(
        "head movement reopens inspection",
        classify(verifier, [moved], [Resolution(20, "old-head")]),
        INTEGRATOR_RESOLUTION,
    )

    malformed = Candidate(21, "bad", verifier, complete=False)
    expect("malformed candidate", classify(verifier, [malformed]), INTEGRATOR_RESOLUTION)
    expect(
        "resolved exact malformed head",
        classify(verifier, [malformed], [Resolution(21, "bad")]),
        INDEPENDENT,
    )

    current = Candidate(22, "valid", verifier)
    expect(
        "resolution cannot suppress valid current result",
        classify(verifier, [current], [Resolution(22, "valid")]),
        BLOCKED_INVALID_RESOLUTION,
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

    # Initial Step 1A sees no result; publication occurs during Steps 2/3; the
    # mandatory final re-check sees it and changes the route before commitment.
    expect("initial check before publication", classify(verifier, []), INDEPENDENT)
    expect("final re-check after publication", classify(verifier, [current]), INTEGRATOR_RESULT)


if __name__ == "__main__":
    main()
