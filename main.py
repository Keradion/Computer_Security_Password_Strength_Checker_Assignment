#!/usr/bin/env python3
"""Password Strength Checker - CLI entry point."""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from display import print_banner, print_results
from evaluator import evaluate_password


def prompt_for_password() -> str:
    """Prompt the user for a password with visible input."""
    while True:
        password = input("🔑 Enter your password: ")
        if password:
            return password
        print("❌ Password cannot be empty. Please try again.\n")


def main() -> None:
    print_banner()
    password = prompt_for_password()
    result = evaluate_password(password)
    print_results(result)


if __name__ == "__main__":
    main()
