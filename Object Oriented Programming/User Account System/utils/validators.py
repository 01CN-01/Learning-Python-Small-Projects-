def get_int(prompt: str) -> int:
    """Prompt until the user enters a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid. Use a number.")


def get_int_in_range(prompt: str, min_value: int, max_value: int) -> int:
    """Prompt for an integer within the inclusive range min_value-max_value."""
    while True:
        value = get_int(prompt)
        if min_value <= value <= max_value:
            return value
        print(f"Enter a number between {min_value} and {max_value}.")


def get_non_empty(prompt: str) -> str:
    """Prompt until the user enters a non-empty string."""
    while True:
        answer = input(prompt).strip()
        if answer:
            return answer
        print("Cannot leave blank.")


# Allowed social platforms for this learning project.
_ALLOWED_SOCIALS = {
    "instagram": "Instagram",
    "facebook": "Facebook",
    "twitter": "Twitter",
}


def get_social(prompt: str) -> str:
    """Prompt for a social platform limited to allowed values."""
    while True:
        social_input = get_non_empty(prompt).lower()
        if social_input in _ALLOWED_SOCIALS:
            return _ALLOWED_SOCIALS[social_input]
        print("Invalid social name. Use Instagram, Facebook, or Twitter.")


def get_email(prompt: str) -> str:
    """Prompt for a basic email format like name@domain.com."""
    while True:
        email_check = input(prompt).strip()
        if email_check.count("@") != 1:
            print("Invalid email format. Use name@domain.com.")
            continue

        local_part, domain_part = email_check.split("@", 1)
        if not local_part or not domain_part:
            print("Invalid email format. Use name@domain.com.")
            continue

        if "." not in domain_part:
            print("Invalid email format. Use name@domain.com.")
            continue

        domain_sections = domain_part.split(".")
        if any(not section for section in domain_sections):
            print("Invalid email format. Use name@domain.com.")
            continue

        return email_check