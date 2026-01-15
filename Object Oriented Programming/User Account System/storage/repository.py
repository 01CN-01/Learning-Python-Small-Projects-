from abc import ABC, abstractmethod
from typing import List

from models.user import User


class UserRepository(ABC):
    """Abstract repository for user persistence."""

    @abstractmethod
    def load_all(self) -> List[User]:
        """Load all users."""
        raise NotImplementedError

    @abstractmethod
    def save_all(self, users: List[User]) -> None:
        """Persist all users."""
        raise NotImplementedError

