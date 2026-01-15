from typing import List
from models.user import User
from storage.repository import UserRepository


class AccountService:
    def __init__(self, repository: UserRepository) -> None:
        """Initialize the service with a repository dependency."""
        # Repository used for persistence.
        self._repository = repository
        # In-memory cache of users loaded from disk.
        self._users = self._repository.load_all()

    def add_user(self, user: User) -> None:
        """Add a user to the system and persist the change."""
        self._users.append(user)
        self._repository.save_all(self._users)

    def remove_user_by_index(self, index: int) -> bool:
        """Remove a user by 0-based index; returns True if removed."""
        if index < 0 or index >= len(self._users):
            return False
        del self._users[index]
        self._repository.save_all(self._users)
        return True

    def list_users(self) -> List[User]:
        """Return a shallow copy of the current user list."""
        return list(self._users)

    def search_by_social(self, social: str) -> List[User]:
        """Find all users matching the provided social platform name."""
        social_lower = social.lower()
        return [user for user in self._users if user.social.lower() == social_lower]

    def search_by_name(self, name: str) -> List[User]:
        """Find all users matching the provided first or last name."""
        name_lower = name.lower()
        return [
            user
            for user in self._users
            if user.first_name.lower() == name_lower or user.last_name.lower() == name_lower
        ]