"""Rule-based password strength evaluation."""

import re

from constants import (
    COMMON_PASSWORDS,
    REPEATED_PATTERNS,
    SEQUENTIAL_PATTERNS,
    SPECIAL_CHARACTERS,
    STRENGTH_LABELS,
)


def score_length(password: str) -> tuple[int, str]:
    """Return length score and a human-readable explanation."""
    length = len(password)

    if length < 6:
        return 0, f"Length is {length} characters (less than 6): 0 points"
    if length <= 7:
        return 1, f"Length is {length} characters (6-7): 1 point"
    if length <= 11:
        return 2, f"Length is {length} characters (8-11): 2 points"
    return 3, f"Length is {length} characters (12 or more): 3 points"


def score_character_variety(password: str) -> tuple[int, list[str]]:
    """Return variety score and a breakdown of matched character classes."""
    checks = [
        ("Contains lowercase letters (a-z)", bool(re.search(r"[a-z]", password))),
        ("Contains uppercase letters (A-Z)", bool(re.search(r"[A-Z]", password))),
        ("Contains numbers (0-9)", bool(re.search(r"[0-9]", password))),
        (
            "Contains special characters",
            any(character in SPECIAL_CHARACTERS for character in password),
        ),
    ]

    details = []
    score = 0
    for label, matched in checks:
        if matched:
            score += 1
            details.append(f"{label}: +1 point")
        else:
            details.append(f"{label}: not present")

    return score, details


def detect_weak_patterns(password: str) -> list[str]:
    """Detect common, repeated, and sequential weak patterns."""
    normalized = password.lower()
    findings = []

    if normalized in COMMON_PASSWORDS:
        findings.append(f'Common password detected: "{normalized}"')

    for pattern in REPEATED_PATTERNS:
        if pattern in normalized:
            findings.append(f'Repeated pattern detected: "{pattern}"')

    for pattern in SEQUENTIAL_PATTERNS:
        if pattern in normalized:
            findings.append(f'Sequential pattern detected: "{pattern}"')

    if len(password) >= 6 and len(set(password)) == 1:
        findings.append("Repeated pattern detected: all characters are identical")

    return findings


def apply_penalties(base_score: int, weak_patterns: list[str]) -> tuple[int, str, bool]:
    """
    Apply weak-pattern penalties.

    Returns final score, penalty explanation, and whether the password was
    forced to Very Weak due to multiple weak patterns.
    """
    if not weak_patterns:
        return base_score, "No weak patterns detected: no penalty applied", False

    if len(weak_patterns) >= 2:
        explanation = (
            f"Multiple weak patterns detected ({len(weak_patterns)}): "
            "classification forced to Very Weak"
        )
        return base_score, explanation, True

    penalized_score = max(base_score - 2, 0)
    explanation = (
        f"One weak pattern detected: subtract 2 points "
        f"({base_score} -> {penalized_score})"
    )
    return penalized_score, explanation, False


def classify_strength(score: int, forced_very_weak: bool) -> str:
    """Map a numeric score to a strength label."""
    if forced_very_weak:
        return "Very Weak"

    if score >= 5:
        return "Very Strong"

    for minimum, maximum, label in STRENGTH_LABELS:
        if minimum <= score <= maximum:
            return label

    return "Very Weak"


def evaluate_password(password: str) -> dict:
    """Evaluate a password and return a structured result dictionary."""
    length_score, length_detail = score_length(password)
    variety_score, variety_details = score_character_variety(password)
    base_score = length_score + variety_score

    weak_patterns = detect_weak_patterns(password)
    final_score, penalty_detail, forced_very_weak = apply_penalties(
        base_score,
        weak_patterns,
    )
    classification = classify_strength(final_score, forced_very_weak)

    return {
        "password_length": len(password),
        "length_score": length_score,
        "length_detail": length_detail,
        "variety_score": variety_score,
        "variety_details": variety_details,
        "base_score": base_score,
        "weak_patterns": weak_patterns,
        "penalty_detail": penalty_detail,
        "forced_very_weak": forced_very_weak,
        "final_score": final_score,
        "classification": classification,
    }
