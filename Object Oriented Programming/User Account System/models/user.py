from dataclasses import dataclass
from typing import Dict


@dataclass
class User:
    social: str         # Social platform or service name (e.g., Instagram).
    first_name: str     # User's first name.
    last_name: str      # User's last name.
    email: str          # User's email address.
    password: str       # User's password (stored as plain text for learning purposes only).

    def to_dict(self) -> Dict[str, str]:
        """Convert this User into a JSON-serializable dictionary."""
        return {
            "social": self.social,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
        }

    @staticmethod
    def from_dict(data: Dict[str, str]) -> "User":
        """Create a User from a dictionary with the expected keys."""
        return User(
            social=data.get("social", ""),
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", ""),
            email=data.get("email", ""),
            password=data.get("password", ""),
        )
