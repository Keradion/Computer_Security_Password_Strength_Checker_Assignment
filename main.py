#!/usr/bin/env python3
"""Password Strength Checker - CLI entry point."""

from getpass import getpass

from display import print_banner, print_results
from evaluator import evaluate_password


def prompt_for_password() -> str:
    """Securely prompt the user for a password."""
    print("Enter a password to evaluate.")
    print("(Input is hidden for security.)")
    print()

    while True:
        password = getpass("Password: ")
        if password:
            return password
        print("Password cannot be empty. Please try again.\n")


def main() -> None:
    print_banner()
    password = prompt_for_password()
    result = evaluate_password(password)
    print_results(result)


if __name__ == "__main__":
    main()
