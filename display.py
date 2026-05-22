"""CLI output formatting for password strength results."""


def print_banner() -> None:
    print()
    print("=" * 60)
    print("           PASSWORD STRENGTH CHECKER")
    print("=" * 60)
    print()


def print_results(result: dict) -> None:
    """Display evaluation results in a structured format."""
    print("-" * 60)
    print("EVALUATION RESULTS")
    print("-" * 60)
    print()
    print(f"  Final Score          : {result['final_score']}")
    print(f"  Strength Classification : {result['classification']}")
    print()
    print("-" * 60)
    print("DETAILED BREAKDOWN")
    print("-" * 60)
    print()
    print("  [Length Scoring]")
    print(f"    {result['length_detail']}")
    print(f"    Length subtotal: {result['length_score']} point(s)")
    print()
    print("  [Character Variety Scoring]")
    for detail in result["variety_details"]:
        print(f"    {detail}")
    print(f"    Variety subtotal: {result['variety_score']} point(s)")
    print()
    print(f"  Base score (before penalties): {result['base_score']}")
    print()
    print("  [Weak Pattern Detection]")
    if result["weak_patterns"]:
        for finding in result["weak_patterns"]:
            print(f"    - {finding}")
    else:
        print("    - No weak patterns found")
    print()
    print(f"  [Penalty Application]")
    print(f"    {result['penalty_detail']}")
    print()
    print("-" * 60)
    print("SCORING REFERENCE")
    print("-" * 60)
    print("  Length:        0-3 points")
    print("  Variety:       0-4 points")
    print("  Penalty:       -2 points (or forced Very Weak if multiple patterns)")
    print()
    print("  Classifications:")
    print("    0-1  -> Very Weak")
    print("    2    -> Weak")
    print("    3    -> Medium")
    print("    4    -> Strong")
    print("    5-6  -> Very Strong")
    print("=" * 60)
    print()
