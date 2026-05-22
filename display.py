"""CLI output formatting for password strength results."""

STRENGTH_STYLE = {
    "Very Weak": ("🔴", "Very Weak — easily cracked"),
    "Weak": ("🟠", "Weak — needs improvement"),
    "Medium": ("🟡", "Medium — acceptable, but not ideal"),
    "Strong": ("🟢", "Strong — good password"),
    "Very Strong": ("💪", "Very Strong — excellent password"),
}


def print_banner() -> None:
    print()
    print("=" * 50)
    print("   🔐  PASSWORD STRENGTH CHECKER")
    print("=" * 50)
    print()


def _variety_icon(detail: str) -> str:
    return "✅" if "+1 point" in detail else "❌"


def _variety_label(detail: str) -> str:
    label = detail.split(":")[0]
    replacements = {
        "Contains lowercase letters (a-z)": "Lowercase letters",
        "Contains uppercase letters (A-Z)": "Uppercase letters",
        "Contains numbers (0-9)": "Numbers",
        "Contains special characters": "Special characters",
    }
    return replacements.get(label, label)


def print_results(result: dict) -> None:
    """Display a clear, concise evaluation summary."""
    emoji, strength_text = STRENGTH_STYLE.get(
        result["classification"],
        ("⚪", result["classification"]),
    )

    print()
    print("📊  EVALUATION RESULT")
    print("-" * 50)
    print(f"  🎯 Score      : {result['final_score']} / 7")
    print(f"  {emoji} Strength   : {strength_text}")
    print()
    print("📋  BREAKDOWN")
    print("-" * 50)
    print(f"  📏 Length ({result['password_length']} chars)  : +{result['length_score']} points")

    for detail in result["variety_details"]:
        icon = _variety_icon(detail)
        label = _variety_label(detail)
        print(f"  {icon} {label}")

    print(f"  🔤 Variety total : +{result['variety_score']} points")

    if result["weak_patterns"]:
        print()
        print("  ⚠️  Security warnings:")
        for finding in result["weak_patterns"]:
            print(f"     🚨 {finding}")
        if result["forced_very_weak"]:
            print("     ⛔ Multiple weak patterns — forced to Very Weak")
        elif result["base_score"] != result["final_score"]:
            print(f"     📉 Penalty applied: -2 points")
    else:
        print()
        print("  ✅ No weak patterns detected")

    print("=" * 50)
    print()
