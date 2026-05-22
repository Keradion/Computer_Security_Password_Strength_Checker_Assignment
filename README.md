# Password Strength Checker (CLI Tool)

A simple command-line tool that evaluates the strength of a password based on length, character diversity, and common security weaknesses. Built for educational purposes in a Computer Security course.

---

## Features

- Evaluates password strength using a rule-based scoring system
- Checks:
  - Length
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Detects weak patterns (common passwords, sequences, repetition)
- Provides:
  - Numeric score
  - Strength label
  - Detailed breakdown report

---

## Strength Levels

| Score | Strength |
|------|----------|
| 0–1 | Very Weak |
| 2 | Weak |
| 3 | Medium |
| 4 | Strong |
| 5–6 | Very Strong |

---

## Setup & Installation

### Requirements

- Python 3.9 or later

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Computer_Security_Password_Strength_Checker_Assignment.git
cd Computer_Security_Password_Strength_Checker_Assignment
```

### 2. Run the tool

No additional dependencies are required. From the project directory:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

---

## Usage

1. Start the program with `python main.py`.
2. Enter a password when prompted (input is hidden for security).
3. Review the score, strength classification, and detailed breakdown.

Example:

```bash
$ python main.py

============================================================
           PASSWORD STRENGTH CHECKER
============================================================

Enter a password to evaluate.
(Input is hidden for security.)

Password:
------------------------------------------------------------
EVALUATION RESULTS
------------------------------------------------------------

  Final Score          : 5
  Strength Classification : Very Strong
```

---

## Scoring Overview

### Length

| Length | Score |
|--------|-------|
| Less than 6 characters | 0 |
| 6–7 characters | 1 |
| 8–11 characters | 2 |
| 12 or more characters | 3 |

### Character Variety

Add 1 point for each of the following:

- Lowercase letters (a–z)
- Uppercase letters (A–Z)
- Numbers (0–9)
- Special characters (`!@#$%^&*()_+-=[]{}|;:',.<>?/`)

Maximum: 4 points

### Weak Pattern Penalties

The tool detects:

- **Common passwords** — e.g. `password`, `123456`, `qwerty`, `admin`, `password123`
- **Repeated patterns** — e.g. `aaaaaa`, `111111`, `abcabc`, `123123`
- **Sequential patterns** — e.g. `123456`, `abcdef`

Penalties:

- **One** weak pattern detected → subtract 2 points from the total score
- **Multiple** weak patterns detected → classification is forced to **Very Weak**

---

## Project Structure

```
Computer_Security_Password_Strength_Checker_Assignment/
├── main.py         # CLI entry point
├── evaluator.py    # Scoring and weak-pattern detection logic
├── constants.py    # Password lists and classification thresholds
├── display.py      # Formatted output
└── README.md
```

---

## Design Notes

- Rule-based evaluation inspired by NIST, OWASP, and general cybersecurity practices
- Deterministic scoring: the same password always produces the same result
- Modular design using separate functions for input, evaluation, and display
- Password input is handled with Python's `getpass` module (no echo to the terminal)

---

## License

Educational project — use and modify as needed for coursework and learning.
