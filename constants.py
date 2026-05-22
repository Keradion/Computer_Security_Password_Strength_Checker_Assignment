"""Constants for password strength evaluation."""

COMMON_PASSWORDS = frozenset(
    {
        "password",
        "123456",
        "qwerty",
        "admin",
        "password123",
    }
)

REPEATED_PATTERNS = (
    "aaaaaa",
    "111111",
    "abcabc",
    "123123",
)

SEQUENTIAL_PATTERNS = (
    "123456",
    "abcdef",
)

SPECIAL_CHARACTERS = set("!@#$%^&*()_+-=[]{}|;:',.<>?/")

STRENGTH_LABELS = (
    (0, 1, "Very Weak"),
    (2, 2, "Weak"),
    (3, 3, "Medium"),
    (4, 4, "Strong"),
    (5, 6, "Very Strong"),
)
