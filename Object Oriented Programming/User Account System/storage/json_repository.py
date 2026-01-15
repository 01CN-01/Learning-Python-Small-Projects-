import json
from typing import List

from models.user import User
from storage.repository import UserRepository


class JsonUserRepository(UserRepository):
    def __init__(self, file_path: str) -> None:
        """Store the file path used for reading and writing users."""
        # Path to the JSON file on disk.
        self._file_path = file_path

    def load_all(self) -> List[User]:
        """Load all users from disk; returns an empty list if missing."""
        try:
            with open(self._file_path, "r") as file_handle:
                raw_data = json.load(file_handle)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

        users = []
        raw_users = raw_data.get("users")
        if raw_users is None:
            raw_users = raw_data.get("user_account", [])

        for item in raw_users:
            normalized = {
                "social": item.get("social", ""),
                "first_name": item.get("first_name", item.get("firstname", "")),
                "last_name": item.get("last_name", item.get("lastname", "")),
                "email": item.get("email", ""),
                "password": item.get("password", ""),
            }
            users.append(User.from_dict(normalized))
        return users

    def save_all(self, users: List[User]) -> None:
        """Persist the provided user list to disk as JSON."""
        payload = {"users": [user.to_dict() for user in users]}
        with open(self._file_path, "w") as file_handle:
            json.dump(payload, file_handle, indent=4)

